$sourceDir = "C:\Users\yuan\AppData\Local\Temp\wmux\"
$targetDir = "G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\data\"

if (!(Test-Path $targetDir)) {
    New-Item -ItemType Directory -Force -Path $targetDir
}

# 取得最新的一張 PNG
$latestFile = Get-ChildItem -Path $sourceDir -Filter "*.png" | Sort-Object LastWriteTime -Descending | Select-Object -First 1

if ($latestFile) {
    $timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $newName = "screenshot-$timestamp.png"
    Copy-Item $latestFile.FullName -Destination (Join-Path $targetDir $newName)
    Write-Host "✅ 已將最新截圖同步至 inbox: $newName"
} else {
    Write-Warning "❌ 在 wmux 暫存區找不到截圖。"
}
