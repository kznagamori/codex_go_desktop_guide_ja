#!/usr/bin/env bash
# 開発ガイド v0.0.1: 基礎演習の文字数カウンター / Wails v3専用。異なる技術構成のアプリへそのまま適用しない。
# Run at the application repository root, after wails3 build.
set -euo pipefail
version="${BUILD_VERSION:?Set BUILD_VERSION (for example v0.1.0-rc.1)}"
[[ "$version" =~ ^[A-Za-z0-9][A-Za-z0-9._-]{0,79}$ ]] || { echo "Invalid version" >&2; exit 2; }
app="go_text_counter"
for f in "bin/$app" README.md LICENSE THIRD_PARTY_NOTICES.md docs/user-guide.md; do
  [[ -f "$f" ]] || { echo "Missing required file: $f" >&2; exit 1; }
done
commit="$(git rev-parse HEAD)"
name="${app}_${version}_linux_amd64"
mkdir -p dist
archive="dist/${name}.tar.gz"
[[ ! -e "$archive" && ! -e "$archive.sha256" ]] || { echo "Refusing to overwrite existing archive" >&2; exit 1; }
stage="$(mktemp -d "$(pwd)/dist/.stage.XXXXXX")"
trap 'rm -rf -- "$stage"' EXIT
mkdir "$stage/$name"
install -m 755 "bin/$app" "$stage/$name/$app"
cp README.md LICENSE THIRD_PARTY_NOTICES.md "$stage/$name/"
cp docs/user-guide.md "$stage/$name/user-guide.md"
printf 'version=%s\ncommit=%s\nos=linux\narch=amd64\n' "$version" "$commit" > "$stage/$name/VERSION.txt"
tar -C "$stage" -czf "$archive" "$name"
(cd dist && sha256sum "${name}.tar.gz" > "${name}.tar.gz.sha256")
echo "Created $archive"
