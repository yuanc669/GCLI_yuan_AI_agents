# ImageJ Macros for IHC Analysis

## IHC Quantitative Analysis (DAB)
適用於 ImageJ 1.52e / Fiji。輸出陽性面積百分比 (%) 與 Mean Staining Intensity (x10^6)。

```javascript
// ImageJ 1.52e IHC 定量分析 Macro
// 適用：DAB 染色，輸出陽性面積% 與 Mean Staining Intensity (x10^6)

run("Set Measurements...", "area mean integrated limit redirect=None decimal=4");

input = getDirectory("請選擇圖片資料夾");
output = getDirectory("請選擇輸出資料夾");
list = getFileList(input);

for (i = 0; i < list.length; i++) {
    if (endsWith(list[i], ".tif") || endsWith(list[i], ".jpg")) {
        open(input + list[i]);
        run("Colour Deconvolution", "vectors=H_DAB");
        
        // 選取 DAB 通道 (Channel 2)
        selectWindow("Colour Deconvolution-(Colour_2)");
        run("8-bit");
        
        // 設定閾值（可依實驗條件調整 0-80）
        setThreshold(0, 80);
        run("Convert to Mask");
        
        // 測量陽性面積與強度
        run("Analyze Particles...", "size=10-Infinity show=Nothing summarize");
        
        // 計算積分光密度
        run("Measure");
        
        IJ.renameResults(list[i] + "_Results");
        saveAs("Results", output + list[i] + "_results.csv");
        run("Close All");
    }
}
```
