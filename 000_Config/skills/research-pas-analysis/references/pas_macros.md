# ImageJ Macros for PAS Analysis

## PAS Quantitative Analysis (Mesangial Expansion)
適用於 ImageJ 1.52e / Fiji。輸出 PAS 陽性面積百分比 (%)。

```javascript
// PAS 陽性區域定量 Macro
// 核心指標：Area Fraction (%)

run("Set Measurements...", "area area_fraction integrated limit redirect=None decimal=3");

// 1. 背景扣除 (選填)
run("Subtract Background...", "rolling=50");

// 2. 執行色彩解卷積 (使用 H PAS 矩陣)
run("Colour Deconvolution", "vectors=[H PAS]");

// 3. 選擇紫紅色通道 (Channel 2)
selectWindow(getTitle() + "-(Colour_2)");
run("8-bit");

// 4. 設定閾值：建議起始值 0-130
setThreshold(0, 130);
setOption("BlackBackground", false);

// 5. 執行測量
run("Convert to Mask");
run("Measure");

// 備註：若需排除微小雜點，可改用：
// run("Analyze Particles...", "size=10-Infinity show=Outlines display summarize");
```
