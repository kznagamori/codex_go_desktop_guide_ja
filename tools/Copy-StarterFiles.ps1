#requires -Version 7.0
<#
Copies two exported Markdown documents and four starter templates into a NEW directory.
No Git initialization, network, dependency installation, placeholder replacement or approval.
Use -PlanOnly first. Existing targets, nested Git repositories and reparse-point inputs are refused.
#>
[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$GuideRoot,
    [Parameter(Mandatory)][string]$HandoffRoot,
    [Parameter(Mandatory)][string]$ProjectRoot,
    [switch]$PlanOnly
)
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
function FullPath([string]$Value) {
    if ([string]::IsNullOrWhiteSpace($Value)) { throw 'A path is empty.' }
    return [IO.Path]::GetFullPath($Value)
}
function RejectReparseAncestors([string]$Value) {
    $probe = $Value
    while (-not [string]::IsNullOrEmpty($probe)) {
        if (Test-Path -LiteralPath $probe) {
            $item = Get-Item -LiteralPath $probe -Force
            if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
                throw "Reparse points are not accepted by this new-project helper: $probe"
            }
        }
        $parent = [IO.Directory]::GetParent($probe)
        if ($null -eq $parent) { break }
        $probe = $parent.FullName
    }
}
$GuideRoot = FullPath $GuideRoot
$HandoffRoot = FullPath $HandoffRoot
$ProjectRoot = FullPath $ProjectRoot
foreach ($sourceRoot in @($GuideRoot,$HandoffRoot)) {
    if (-not (Test-Path -LiteralPath $sourceRoot -PathType Container)) {
        throw "Source directory is missing: $sourceRoot"
    }
}
if (Test-Path -LiteralPath $ProjectRoot) {
    throw 'ProjectRoot already exists. Nothing is copied. Preserve existing work and use the manual procedure.'
}
RejectReparseAncestors $ProjectRoot
$parent = [IO.Directory]::GetParent($ProjectRoot)
while ($null -ne $parent) {
    if (Test-Path -LiteralPath (Join-Path $parent.FullName '.git')) {
        throw 'ProjectRoot is inside another Git repository. Choose a separate directory.'
    }
    $parent = $parent.Parent
}
foreach ($sourceRoot in @($GuideRoot,$HandoffRoot)) {
    $prefix = $sourceRoot.TrimEnd([char[]]@('\','/')) + [IO.Path]::DirectorySeparatorChar
    if ($ProjectRoot.Equals($sourceRoot,[StringComparison]::OrdinalIgnoreCase) -or
        $ProjectRoot.StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)) {
        throw 'ProjectRoot must be separate from the guide and handoff directories.'
    }
}
$map = @(
    @{Root=$HandoffRoot; From='idea.md'; To='docs/ideas/idea.md'},
    @{Root=$HandoffRoot; From='naming.md'; To='docs/ideas/naming.md'},
    @{Root=$GuideRoot; From='templates/AGENTS.md'; To='AGENTS.md'},
    @{Root=$GuideRoot; From='templates/docs/workflow/state.md'; To='docs/workflow/state.md'},
    @{Root=$GuideRoot; From='templates/docs/workflow/questions.md'; To='docs/workflow/questions.md'},
    @{Root=$GuideRoot; From='templates/docs/workflow/repo-map.md'; To='docs/workflow/repo-map.md'}
)
# Check ALL inputs before creating any output directory.
$utf8 = [Text.UTF8Encoding]::new($false, $true)
foreach ($entry in $map) {
    $source = Join-Path $entry.Root $entry.From
    if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw "Missing input file: $source" }
    RejectReparseAncestors $source
    $content = $utf8.GetString([IO.File]::ReadAllBytes($source))
    if ([string]::IsNullOrWhiteSpace($content.Trim([char]0xFEFF))) { throw "Empty input file: $source" }
    $entry.Source = $source
    $entry.Destination = Join-Path $ProjectRoot $entry.To
    if (Test-Path -LiteralPath $entry.Destination) { throw "Existing destination: $($entry.Destination)" }
    Write-Output ("{0} -> {1}" -f $source,$entry.Destination)
}
if ($PlanOnly) { Write-Output 'PLAN ONLY: no files or directories were created.'; return }
# File.Copy(..., false) also protects against a target appearing after the checks.
New-Item -ItemType Directory -Path $ProjectRoot -ErrorAction Stop | Out-Null
try {
    foreach ($entry in $map) {
        [IO.Directory]::CreateDirectory([IO.Path]::GetDirectoryName($entry.Destination)) | Out-Null
        [IO.File]::Copy($entry.Source,$entry.Destination,$false)
        $sourceHash = (Get-FileHash -LiteralPath $entry.Source -Algorithm SHA256).Hash
        $targetHash = (Get-FileHash -LiteralPath $entry.Destination -Algorithm SHA256).Hash
        if ($sourceHash -ne $targetHash) { throw "Hash mismatch: $($entry.Destination)" }
    }
} catch {
    Write-Warning 'Copy stopped. Partial files may remain; nothing will be deleted or overwritten automatically.'
    throw
}
Write-Output 'Copied 6 files unchanged. Git is not initialized. Placeholders are not filled. No approval was recorded.'
