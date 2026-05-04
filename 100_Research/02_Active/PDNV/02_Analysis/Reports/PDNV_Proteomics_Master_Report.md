# PDNV 蛋白質組學綜合分析報告 (PDNV Proteomics Master Report)

**日期**: 2026-05-04  
**樣本範圍**: Garlic (大蒜), Ginger (生薑), Kale (羽衣甘藍)  
**分析方法**: Label-free Quantification (Normalized PSM)

---

## 1. 跨樣本對比分析 (Comparative Analysis)

本次分析對比了三種不同來源的植物來源奈米囊泡 (PDNV)。整體而言，**Protein Synthesis (蛋白質合成)** 是所有樣本中最主要的蛋白功能類別。

![Functional Comparison](../03_Figures_Tables/PDNV_Functional_Comparison.png)

### 1.1 功能類別累計豐度表
| 功能類別 | Garlic (Sum) | Ginger (Sum) | Kale (Sum) |
| :--- | :--- | :--- | :--- |
| Protein Synthesis | 4962.12 | 4431.24 | 3824.15 |
| Antioxidant | 215.34 | 195.13 | 142.88 |
| Exosome Marker | 92.45 | 87.38 | 65.21 |
| Anti-stress/HSP | 45.12 | 34.82 | 28.67 |

---

## 2. 個別樣本詳細數據 (Individual Sample Highlights)

### 2.1 Ginger (生薑) NV
- **主要特徵**: 高豐度的核糖體蛋白 (Ribosomal proteins) 與 Alpha-1,4 glucan phosphorylase。
- ![Ginger Top 15](../03_Figures_Tables/Ginger_Top15_Bar.png)

### 2.2 Garlic (大蒜) NV
- **主要特徵**: 在抗氧化相關蛋白 (Antioxidant proteins) 上的表現略高於其他樣本。
- ![Garlic Top 15](../03_Figures_Tables/Garlic_Top15_Bar.png)

### 2.3 Kale (羽衣甘藍) NV
- **主要特徵**: 蛋白質多樣性略低，但核心代謝蛋白豐度集中。
- ![Kale Top 15](../03_Figures_Tables/Kale_Top15_Bar.png)

---

## 3. Prism 數值導出路徑 (Data for GraphPad Prism)

如需進一步統計繪圖，請參考以下路徑中的 `Full_Analysis.csv` 檔案：

- **Ginger**: `02_Analysis/Ginger_Full_Analysis.csv`
- **Garlic**: `02_Analysis/Garlic_Full_Analysis.csv`
- **Kale**: `02_Analysis/Kale_Full_Analysis.csv`

每個檔案均包含 `Mean`, `SD`, `SEM` 等欄位，適用於 Prism 的 "Mean, SD, N=3" 或 "Mean, SEM, N=3" 表格格式。

---

## 4. 結論與建議 (Conclusion)
PDNV 的蛋白質組分佈具有高度相似性，主要集中於基礎代謝與蛋白質合成機制。Garlic NV 在抗氧化潛力上具備微弱優勢，可作為後續功能實驗的參考方向。
