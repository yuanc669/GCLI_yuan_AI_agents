# 🥬 Kale NV Advanced Proteomics Analysis Report (Next Steps)

**Date:** 2026-05-04  
**Project:** PDNV  
**Subject:** Advanced Functional Enrichment & Mechanism Prediction

---

## 1. Data Preparation for Bioinformatic Tools
已提取前 100 名高豐度蛋白質之 Accession IDs，可用於後續生物資訊工具：
*   **Accession List**: [Kale_NV_Top100_Accessions.txt](./Kale_NV_Top100_Accessions.txt)
*   **推薦工具**:
    *   **GO/KEGG Enrichment**: [DAVID Functional Annotation](https://david.ncifcrf.gov/) 或 [ShinyGO](http://bioinformatics.sdstate.edu/go/)。
    *   **PPI Network**: [STRING-db](https://string-db.org/) (建議 Species 設為 *Brassica oleracea*)。

---

## 2. Key Marker Proteins & Potential Mechanisms
針對 Kale NV 中的亮點蛋白進行功能聚焦：

### A. Myrosinase (硫代葡萄糖苷酶) - A0A0D3AXF1
*   **Biological Role**: 負責將硫代葡萄糖苷 (Glucosinolates) 水解成異硫氰酸酯 (ITCs，如萊菔硫烷)。
*   **Mechanism Hypothesis**: Kale NV 可能作為載體，在跨物種環境中傳遞 Myrosinase，與宿主或飲食中的硫代葡萄糖苷反應，產生具抗癌與抗炎活性的代謝產物。

### B. Nitrilase (腈水解酶) - A0A0D3AJG2
*   **Biological Role**: 參與吲哚-3-乙酸 (IAA) 的生物合成。
*   **Mechanism Hypothesis**: 可能參與調節宿主的生長因子途徑或腸道激素平衡。

### C. Aquaporin (水通道蛋白) - A0A0D3BL75
*   **Biological Role**: 水與小分子 (如甘油、CO2) 的穿膜運輸。
*   **Mechanism Hypothesis**: 維持 NV 內部環境穩定，或協助貨物 (Cargo) 的裝載與釋放。

---

## 3. Planned Visualization (Placeholder for Prism)
完成外部富集分析後，建議產出以下圖表：

| Proposed Figure | Purpose | Data Source |
|:---|:---|:---|
| **GO Enrichment Dot Plot** | 顯示生物程序 (BP) 與細胞組分 (CC) 的富集程度。 | ShinyGO / DAVID Output |
| **KEGG Pathway Map** | 視覺化 Kale NV 蛋白在代謝路徑中的位置。 | KEGG Mapper |
| **PPI Network Map** | 展示 Myrosinase 與其夥伴蛋白的相互作用網絡。 | STRING-db Export |

---

**後續行動建議：**
1.  將 `Kale_NV_Top100_Accessions.txt` 上傳至 DAVID 進行富集，並將結果 CSV 存回 `02_Analysis` 目錄。
2.  在 STRING-db 中檢索 `A0A0D3AXF1`，並導出其交互作用蛋白清單。
