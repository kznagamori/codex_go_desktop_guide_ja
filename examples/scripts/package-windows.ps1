# 開発ガイド v0.0.1: 基礎演習の文字数カウンター / Wails v3専用。異なる技術構成のアプリへそのまま適用しない。
# Run with PowerShell 7 at the application repository root, after wails3 build.
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest
$version = $env:BUILD_VERSION
if ([string]::IsNullOrWhiteSpace($version) -or $version -notmatch '^[A-Za-z0-9][A-Za-z0-9._-]{0,79}$') {
    throw 'Set BUILD_VERSION, for example v0.1.0-rc.1.'
}
$app = 'go_text_counter'
foreach ($file in @("bin/$app.exe", 'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md', 'docs/user-guide.md')) {
    if (-not (Test-Path -LiteralPath $file -PathType Leaf)) { throw "Missing required file: $file" }
}
$commit = (& git rev-parse HEAD)
if ($LASTEXITCODE -ne 0) { throw 'git rev-parse failed.' }
$name = "${app}_${version}_windows_amd64"
New-Item -ItemType Directory -Path 'dist' -Force | Out-Null
$archive = Join-Path (Get-Location) "dist/$name.zip"
if ((Test-Path -LiteralPath $archive) -or (Test-Path -LiteralPath "$archive.sha256")) {
    throw 'Refusing to overwrite existing archive.'
}
$stage = Join-Path ([IO.Path]::GetTempPath()) ('text-counter-' + [guid]::NewGuid().ToString('N'))
$package = Join-Path $stage $name
try {
    New-Item -ItemType Directory -Path $package -Force | Out-Null
    Copy-Item -LiteralPath "bin/$app.exe", 'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md' -Destination $package
    Copy-Item -LiteralPath 'docs/user-guide.md' -Destination (Join-Path $package 'user-guide.md')
    "version=$version`ncommit=$commit`nos=windows`narch=amd64" |
        Set-Content -LiteralPath (Join-Path $package 'VERSION.txt') -Encoding utf8NoBOM
    Compress-Archive -LiteralPath $package -DestinationPath $archive
    $hash = (Get-FileHash -LiteralPath $archive -Algorithm SHA256).Hash.ToLowerInvariant()
    "$hash  $name.zip" | Set-Content -LiteralPath "$archive.sha256" -Encoding utf8NoBOM
    Write-Host "Created $archive"
} finally {
    # Only remove this script's newly-created temporary directory.
    if (Test-Path -LiteralPath $stage) { Remove-Item -LiteralPath $stage -Recurse -Force }
}
