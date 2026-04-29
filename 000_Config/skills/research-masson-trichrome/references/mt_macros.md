# ImageJ Macros for Masson's Trichrome Analysis

## MT Quantitative Analysis (Fibrosis)
適用於 ImageJ 1.52e / Fiji。輸出 CVF% (Area Fraction) 與 Integrated Density。

```javascript
// ImageJ 1.52 MT 定量分析 Macro
// 核心指標：CVF% (Area Fraction)

run("Set Measurements...", "area area_fraction integrated limit redirect=None decimal=4");

// 1. 色彩解卷積 (Colour Deconvolution)
run("Colour Deconvolution", "vectors=[Masson Trichrome]");

// 2. 選取藍色通道 (Channel 1)
selectWindow(getTitle() + "-(Colour_1)");
run("8-bit");

// 3. 閾值設定 (建議預設 0-115)
setThreshold(0, 115); 
run("Convert to Mask");

// 4. 測量
run("Measure");
```
