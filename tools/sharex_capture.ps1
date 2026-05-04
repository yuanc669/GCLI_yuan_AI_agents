# ShareX Capture Tool for Gemini CLI
$sharexPath = "C:\Program Files\ShareX\ShareX.exe"
$targetDir = "G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\screens"

# 1. Execute ShareX rectangle region capture
Write-Host "Starting ShareX region capture..."
Start-Process -FilePath $sharexPath -ArgumentList "-RectangleRegion" -Wait

# 2. Get the latest generated image
$latestFile = Get-ChildItem -Path $targetDir -Filter "*.png" | Sort-Object LastWriteTime -Descending | Select-Object -First 1

if ($latestFile) {
    Write-Host "CAPTURED: $($latestFile.FullName)"
    return $latestFile.FullName
} else {
    Write-Warning "No screenshot found in $targetDir."
    return $null
}
