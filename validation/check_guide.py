#!/usr/bin/env python3
"""Validate documentation and full prompt structure; does not execute app/model/CI.
Requires Python 3.10+ and markdown-it-py.
Run: python validation/check_guide.py [--write] [--root path]
Without --write the package is read-only; output goes to stdout.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit
try:
    from markdown_it import MarkdownIt
except ImportError:
    raise SystemExit('markdown-it-py is required; no files were modified.')


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(root: Path) -> dict:
    root=root.resolve()
    version=(root/'VERSION.txt').read_text(encoding='utf-8').strip()
    parser=MarkdownIt('commonmark').enable('table')
    files=sorted(root.rglob('*.md'))
    texts={p:p.read_text(encoding='utf-8') for p in files}
    tokens={p:parser.parse(s) for p,s in texts.items()}
    errors=[]; anchors={}; headings={}; fences=[]
    for p,ts in tokens.items():
        rel=p.relative_to(root).as_posix(); lines=texts[p].splitlines()
        if f'**ドキュメントバージョン：{version}**' not in '\n'.join(lines[:6]):
            errors.append(rel+': missing current version header')
        ids=set(); autos={}; hs=[]
        for i,t in enumerate(ts):
            if t.type=='heading_open':
                inline=ts[i+1]
                title=''.join(c.content for c in (inline.children or []) if c.type not in ('html_inline','softbreak','hardbreak'))
                slug=re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-')
                n=autos.get(slug,0); autos[slug]=n+1
                ids.add(slug if not n else f'{slug}-{n}'); hs.append((int(t.tag[1:]),title))
            for c in [t]+list(t.children or []):
                if c.type in ('html_inline','html_block'):
                    for ident in re.findall(r'\bid=["\']([^"\']+)["\']',c.content):
                        if ident in ids: errors.append(rel+': duplicate anchor '+ident)
                        ids.add(ident)
            if t.type=='fence':
                close=lines[t.map[1]-1].strip() if t.map else ''
                if not re.fullmatch(re.escape(t.markup[0])+'{'+str(len(t.markup))+',}',close):
                    errors.append(rel+': unclosed fence '+str(t.map))
                if t.info.strip()=='markdown':
                    for line in t.content.splitlines():
                        if re.match(r'^#{1,6} .+#{1,6} ',line):
                            errors.append(rel+': merged markdown heading '+line[:100])
                fences.append((p,t.info.strip(),t.content.rstrip(),t.map))
        anchors[p]=ids; headings[p]=hs
    links=[]
    for p,ts in tokens.items():
        for t in ts:
            for c in t.children or []:
                if c.type!='link_open': continue
                raw=c.attrGet('href') or ''; url=urlsplit(raw)
                if url.scheme or url.netloc: continue
                if '{' in unquote(raw): continue
                dest=(p.parent/unquote(url.path)).resolve() if url.path else p
                frag=unquote(url.fragment)
                links.append([p.relative_to(root).as_posix(),raw])
                if not dest.is_relative_to(root) or not dest.exists(): errors.append(str(p.relative_to(root))+': missing link '+raw)
                elif frag and dest.suffix=='.md' and frag not in anchors.get(dest,set()): errors.append(str(p.relative_to(root))+': missing anchor '+raw)
    collection=root/'04_prompt_templates_ja.md'
    seq=[m.group(0) for level,title in headings[collection] if level==2 and (m:=re.match(r'P\d{2}',title))]
    if seq!=[f'P{i:02d}' for i in range(1,41)]: errors.append('P01-P40 sequence mismatch')
    cores={}
    for p,info,body,span in fences:
        if p!=collection or info!='markdown': continue
        title=body.splitlines()[0]
        m=re.match(r'# (P\d{2})：',title)
        k=m[1] if m else 'C0' if title.startswith('# 共通契約 C0') else None
        if k:
            if k in cores: errors.append('duplicate core '+k)
            cores[k]=body
    if len(cores)!=41: errors.append('Expected C0 plus 40 common prompts')
    for k in cores:
        part=re.search(r'<a id="'+k.lower()+r'"></a>(.*?)(?=<a id="(?:c0|p\d{2})"></a>|\n## 関連資料|\Z)',texts[collection],re.S)
        if not part: errors.append('missing section '+k); continue
        if k!='C0':
            pre=part[1].split('````markdown')[0]
            for field in ('実行条件','省略条件','入力先','用意するもの','ユーザーの記入欄'):
                if field not in pre: errors.append(k+': missing usage field '+field)
        single=root/'prompts'/('P38_sync_idea_naming_ja.md' if k=='P38' else k+'_prompt_ja.md')
        bodies=[b for p,info,b,span in fences if p==single and info=='markdown']
        if bodies!=[cores[k]]: errors.append(k+': standalone body differs/missing')
    # Verify integrated blocks are exactly the reviewed catalog and retain core text.
    catalog=json.loads((root/'validation/prompt-catalog.json').read_text(encoding='utf-8'))
    bylabel={c['label']:c for c in catalog}
    if len(bylabel)!=len(catalog): errors.append('duplicate integrated label in catalog')
    actual={}; chapter_counts={}
    full_rx=re.compile(r'<!-- full-prompt base="(C0|P\d{2})" lesson="([^"]+)" -->.*?````markdown\n(.*?)\n````',re.S)
    for p,s in texts.items():
        for m in full_rx.finditer(s):
            k,label,body=m.groups()
            if label in actual: errors.append('duplicate integrated label '+label)
            actual[label]={'base':k,'file':p.relative_to(root).as_posix(),'sha256':hashlib.sha256(body.encode()).hexdigest()}
            if label not in bylabel: errors.append(label+': missing catalog entry'); continue
            expected=bylabel[label]
            if expected['sha256']!=actual[label]['sha256'] or expected['base']!=k:
                errors.append(label+': integrated body changed/incomplete')
            # Strip exercise section and title suffix; every base instruction remains.
            normalized=re.sub(r'^## 今回の演習で指定する対象・条件\n.*?(?=^## |\Z)','',body,flags=re.M|re.S)
            line=normalized.splitlines()[0]
            if k in cores:
                normalized=normalized.replace(line,cores[k].splitlines()[0],1)
                chunks=re.split(r'\{[^{}]+\}',cores[k])
                # whitespace-flexible full comparison, placeholders may contain their own braces.
                regex=r'[^\n]*'.join(re.escape(x) for x in chunks)
                regex=regex.replace(r'\
\
',r'\s*\n\s*\n')
                if not re.fullmatch(regex,normalized.rstrip()):
                    # Less brittle line-level preservation for deliberate replaced fields.
                    baselines=cores[k].splitlines()
                    missing=[]
                    for line in baselines[1:]:
                        if not line.strip() or re.match(r'^## ',line): continue
                        pattern=r'.*?'.join(re.escape(x) for x in re.split(r'\{[^{}]+\}',line))
                        if not re.search('^'+pattern+'$',normalized,re.M): missing.append(line)
                    if missing: errors.append(label+': missing core instructions '+repr(missing[:2]))
            else: errors.append(label+': unknown base '+k)
    if set(actual)!=set(bylabel): errors.append('integrated catalog label set mismatch')
    # Per chapter numbering and coverage; substeps must have no gaps or duplicates.
    for filename,letter,count in [('05_hands_on_text_counter_ja.md','H',22),('06_hands_on_markdown_viewer_ja.md','D',35)]:
        p=root/filename; s=texts[p]
        got=[re.match(letter+r'\d{2}',t)[0] for lv,t in headings[p] if lv==2 and re.match(letter+r'\d{2}：',t)]
        want=[letter+f'{i:02d}' for i in range(1,count+1)]
        table=re.findall(r'^\| \[('+letter+r'\d{2})\]\(#'+letter.lower()+r'\d{2}\)',s,re.M)
        if got!=want or table!=want: errors.append(filename+': chapter/table sequence mismatch')
        covered={}
        for n in range(1,count+1):
            ident=letter+f'{n:02d}'
            part=re.search(r'^## '+ident+r'：.*?(?=^<a id="'+letter.lower()+r'\d{2}"></a>|^## 3\.|\Z)',s,re.M|re.S)
            if not part: errors.append(filename+': chapter missing '+ident); continue
            nblocks=len(full_rx.findall(part[0])); covered[ident]=nblocks
            if nblocks<1 and ident not in ('H03','D03'): errors.append(ident+': no complete input')
            if ident in ('H03','D03') and ('6ファイル' not in part[0] or 'ユーザーがPC上' not in part[0]): errors.append(ident+': missing explicit manual copy procedure')
            sub=[int(m) for m in re.findall(r'^### '+ident+r'\.(\d+) ',part[0],re.M)]
            if sub and sub!=list(range(1,len(sub)+1)): errors.append(ident+': broken substep numbering')
        chapter_counts[filename]=covered
    p38copies=[(p,b) for p,info,b,span in fences if info=='markdown' and b.startswith('# P38：')]
    if len(p38copies)!=5 or len({b for p,b in p38copies})!=1: errors.append('P38 five identical bodies requirement failed')
    idea_required=['アプリ表示名','GitHub所有者','GitHubリポジトリ名','完全なリポジトリ名','リポジトリURL','GitHub作成状況','名称の正本','同期元の文書版・承認範囲']
    for field in idea_required:
        if not re.search(r'^- '+re.escape(field)+'：',cores.get('P38',''),re.M): errors.append('P38 missing field '+field)
        if '| '+field+' |' not in texts[root/'templates/docs/ideas/idea.md']: errors.append('idea schema missing '+field)
    # Essential H06 case table and complete specification controls.
    h06=next((b for p,info,b,span in fences if p.name=='05_hands_on_text_counter_ja.md' and b.startswith('# P06：')), '')
    expected_rows=[('""','0','0','0'),('"abc"','3','3','1'),('"日本語"','3','9','1'),('"A😀"','2','5','1'),('"e\\u0301"','2','3','1'),('"a\\r\\nb"','3','3','2'),('"a\\rb"','3','3','2'),('"\\n"','1','1','2'),('"a\\n"','2','2','2'),('" "','1','1','1')]
    for input_,a,b,c in expected_rows:
        row=f'| `{input_}` | {a} | {b} | {c} |'
        if row not in h06: errors.append('H06 missing/changed case '+row)
    for field in ['承認済みidea.md','docs/specs/requirements.md','REVIEW','未承認','保存','再読込み','停止']:
        if field not in h06: errors.append('H06 missing '+field)
    # No orphan Markdown input; management schema is explicitly not an input.
    for p,info,b,span in fences:
        if info!='markdown': continue
        if not (b.startswith('# P') or b.startswith('# 共通契約 C0')):
            if p.name=='02_workflow_ja.md' and b.startswith('文書状態：'): continue
            errors.append(str(p.relative_to(root))+': unclassified markdown input at '+str(span))
    rootnames=sorted(p.name for p in root.glob('[0-9][0-9]_*.md'))
    if [int(n[:2]) for n in rootnames]!=list(range(10)): errors.append('00-09 root names mismatch')
    if (root/'03_migration_and_quickstart_ja.md').exists(): errors.append('Removed quickstart file restored')
    if '## 2. 旧版の資料で作業を始めている場合' in texts[root/'03_quickstart_ja.md']: errors.append('Removed section restored')
    reference=json.loads((root/'validation/reference-baseline.json').read_text())
    ref_results=[]
    for name,digest in reference.items():
        p=root/name; match=p.exists() and sha(p)==digest
        ref_results.append({'file':name,'sha256':sha(p) if p.exists() else None,'baseline_equal':match})
        if not match: errors.append('Reference implementation changed '+name)
    if len(ref_results)!=10: errors.append('Expected 10 example implementation files')
    # v0.0.9: filled-example walkthroughs plus existing approval gates.
    example_walkthroughs={
        '05_hands_on_text_counter_ja.md':['### H01.1 実際の記入例と照合する','examples/idea_text_counter.md','集計規則','記入例をそのままコピーせず'],
        '06_hands_on_markdown_viewer_ja.md':['### D01.1 実際の記入例と照合する','examples/markdown_viewer/idea.md','examples/markdown_viewer/S-05.md','examples/markdown_viewer/T-014.md','教材ID・未承認状態・試験結果'],
    }
    for filename,phrases in example_walkthroughs.items():
        for phrase in phrases:
            if phrase not in texts[root/filename]: errors.append(filename+': missing filled-example walkthrough '+phrase)
    for k in ('P08','P34','P35','P38','P39','P40'):
        section=re.search(r'<a id="'+k.lower()+r'"></a>(.*?)(?=<a id="p\d{2}"></a>|\n## 関連資料|\Z)',texts[collection],re.S)
        pre=section[1].split('````markdown')[0] if section else ''
        if not re.search(r'^\| 入力先 \| Codex CLI',pre,re.M): errors.append(k+': must be Codex-only')
        if 'Codex' not in cores[k] or '保存' not in cores[k]: errors.append(k+': local save instructions missing')
    for k in ('P02','P33','P37'):
        for phrase in ('idea.md','naming.md','Codex CLI'):
            if phrase not in cores[k]:errors.append(k+': missing export/handoff '+phrase)
    for phrase in ('AGENTS.md','docs/workflow/state.md','docs/workflow/questions.md','docs/workflow/repo-map.md','docs/workflow/template-check.md','不明を0にしません','idea.md・naming.mdは入力として保護','一括置換は禁止','新規起動してC0'):
        if phrase not in cores['P04']:errors.append('P04 missing critical setup rule '+phrase)
    for phrase in ('対象ファイル：','根拠：','今回の工程：','試験結果','元のtemplates'):
        if phrase not in cores['P40']:errors.append('P40 missing scope rule '+phrase)
    for phrase in ('後工程の根拠として使う文書は全文承認を基本','未決・未実施・未確認','REVIEWのまま進めるのは'):
        if phrase not in cores['P08']: errors.append('P08 missing approval-gate rule '+phrase)
    for phrase in ('現在版の記載全体','全文を承認してAPPROVED','一部承認でREVIEWを維持'):
        if phrase not in cores['P35']: errors.append('P35 missing approval-gate rule '+phrase)
    for p,info,b,span in fences:
        if info!='markdown' or not re.match(r'# (P08|P34|P35|P38|P39)：',b):continue
        if re.search(r'(ChatGPTで更新版を出力|ChatGPTで全文を出力し人がPCへ保存|対象：このチャットの)',b):errors.append(str(p.relative_to(root))+': browser post-handoff operation')
    for filename in ('05_hands_on_text_counter_ja.md','06_hands_on_markdown_viewer_ja.md'):
        tx=texts[root/filename]
        for phrase in ('承認しながら進む','`REVIEW`のまま進めてよいのは','文書状態：APPROVED','全文を対象とする承認履歴'):
            if phrase not in tx: errors.append(filename+': missing approval progression '+phrase)
        for m in full_rx.finditer(tx):
            k,label,b=m.groups()
            pre=m[0].split('````markdown')[0]
            allowed=k in ('P01','P02','P33','P37')
            if ('入力先：ChatGPT.com' in pre)!=allowed:errors.append(label+': wrong execution environment')
        for phrase in ('docs/ideas/idea.md','docs/ideas/naming.md','templates/docs/workflow/state.md','templates/docs/workflow/questions.md','templates/docs/workflow/repo-map.md','templates/AGENTS.md','template-check.md'):
            if phrase not in tx:errors.append(filename+': missing copy/fill detail '+phrase)
    for k in ('P06','P09','P10','P11','P18','P19','P20','P22','P23','P25','P26','P27'):
        if '## コピー済みの文書テンプレートがある場合' not in cores[k]: errors.append(k+': template-fill contract missing')
    template_readme=texts[root/'templates/README_ja.md']
    template_paths=sorted(p.relative_to(root/'templates').as_posix() for p in (root/'templates').rglob('*.md') if p.name!='README_ja.md')
    if len(template_paths)!=22:errors.append('Expected 22 actual templates')
    for name in template_paths:
        if '| '+name+' |' not in template_readme:errors.append('Template missing mapping '+name)
    ps=(root/'tools/Copy-StarterFiles.ps1').read_text()
    expected_pairs=[('idea.md','docs/ideas/idea.md'),('naming.md','docs/ideas/naming.md'),('templates/AGENTS.md','AGENTS.md'),('templates/docs/workflow/state.md','docs/workflow/state.md'),('templates/docs/workflow/questions.md','docs/workflow/questions.md'),('templates/docs/workflow/repo-map.md','docs/workflow/repo-map.md')]
    pairs=re.findall(r"From='([^']+)'; To='([^']+)'",ps)
    if pairs!=expected_pairs:errors.append('Copy helper six-file mapping mismatch')
    for phrase in ('if ($PlanOnly)','[IO.File]::Copy($entry.Source,$entry.Destination,$false)','RejectReparseAncestors','UTF8Encoding','Get-FileHash'):
        if phrase not in ps:errors.append('Copy helper missing static guard '+phrase)
    report={'version':version,'scope':'document_and_prompt_static_checks_only',
            'markdown_count':len(files),'local_link_count':len(links),
            'fence_count':len(fences),'markdown_fence_count':sum(i=='markdown' for p,i,b,sp in fences),
            'common_prompt_count':len(cores),'integrated_input_count':len(actual),
            'standalone_prompt_count':len(cores),'p38_copies':len(p38copies),
            'chapter_coverage':chapter_counts,'reference_files':ref_results,
            'result':'FAIL' if errors else 'PASS','errors':errors,
            'not_run':['Model execution of every prompt','GUI and Wails build','GitHub Actions','Dependency version refresh','Example code test reruns','PowerShell helper execution','End-to-end P08/P35 approval execution in a user repository']}
    return report


def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root',type=Path,default=Path(__file__).resolve().parent.parent)
    ap.add_argument('--write',action='store_true')
    args=ap.parse_args()
    report=run(args.root)
    if args.write:
        (args.root/'validation/document-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        summary={k:report[k] for k in ('version','scope','common_prompt_count','integrated_input_count','standalone_prompt_count','p38_copies','result','errors','not_run')}
        (args.root/'validation/prompt-check.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('chapter_coverage','reference_files')},ensure_ascii=False,indent=2))
    return int(bool(report['errors']))
if __name__=='__main__': raise SystemExit(main())
