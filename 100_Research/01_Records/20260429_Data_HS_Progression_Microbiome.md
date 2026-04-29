---
type: DataCard
domain: 100_Research
project: DN_GaExo
tags: [data-interpret, microbiome, 16S, time-series, disease-progression]
status: active
updated: 2026-04-29
llm_ready: true
---

# Data Insight: HS Disease Progression (Sham vs HS2W vs HS6W vs HS10W)

## 📌 數據來源
- **原始檔案**: `_inbox/L7_Sham_HS2W_HS6W_HS10W-1.xlsx`
- **數據類型**: 16S rRNA 腸道菌叢豐度 (Relative Abundance)

## 🧪 實驗組別設定
- **Sham**: 假手術對照組 (n=3)
- **HS2W**: 高脂飲食+STZ 誘導第 2 週 (n=5)
- **HS6W**: 高脂飲食+STZ 誘導第 6 週 (n=6)
- **HS10W**: 高脂飲食+STZ 誘導第 10 週 (n=6)

## 📊 核心發現 (Key Findings)
1. **主要優勢菌門 (Dominant Phyla)**:
   - 整體樣本中，豐度最高的菌群集中在 `Bacteroidota` (擬桿菌門) 與 `Bacillota` (厚壁菌門，原 Firmicutes)。
2. **Top 5 關鍵菌屬 (Top 5 Genera)**:
   - `Bacteroides_H_857956` (最高佔比，約 9.5%)
   - `Kineothrix` (次高，約 9.0%)
   - `Paramuribaculum` (約 4.0%)
   - *其餘為未分類 (unclassified) 菌屬。*
3. **疾病時序變化趨勢 (Temporal Trends)**:
   - 隨著疾病進程 (HS2W -> HS6W -> HS10W)，這份數據提供了從「早期代謝紊亂」到「晚期腎臟病變」過程中的動態微生態變化。

## 💡 分析建議
- **Alpha Diversity**: 建議比較 Sham 與各時間點的物種豐富度變化。
- **PCoA (Beta Diversity)**: 可預期 HS10W 的群落結構將與 Sham 及 HS2W 產生顯著分離。
- **LEfSe 分析**: 尋找在 HS10W 特異性富集，且可能與 DN (Diabetic Nephropathy) 病程惡化相關的 Biomarker 菌屬。
