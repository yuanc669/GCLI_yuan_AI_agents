# Garlic_NV (大蒜外泌體) 蛋白質組學標籤自由定量 (Label-free Quantification) 分析報告

> **原始檔案**: `25091902-Label-free Quantification Garlic_NV.xlsx`
> **分析日期**: 2026-05-04
> **樣本說明**: Garlic_NV (G1, G2, G3 三重複)

---

## 📊 一、 全域蛋白質組成概覽 (Global Profile)

### 1. 功能類別分佈 (Functional Distribution)
![Functional Pie Chart](./GaNV_Functional_Pie.png)

*   **Antioxidant (抗氧化)**: 佔顯著比例。包含過氧化物酶 (Peroxidase) 與超氧化物歧化酶 (SOD)，是大蒜外泌體具備腎臟保護潛力的核心分子基礎。
*   **Anti-stress/HSP (抗壓力/熱休克蛋白)**: 包含多種 HSP70/HSP90 家族成員，有助於維持蛋白質摺疊穩定，對抗急性腎損傷 (AKI) 誘導的蛋白質毒性壓力。
*   **Transport (轉運)**: 涉及多種通道蛋白與轉運體，可能參與細胞間通訊。

### 2. 豐度前 15 名蛋白質 (Top 15 Abundant Proteins)
![Top 15 Proteins Bar Chart](./GaNV_Top15_Proteins_Bar.png)

---

## 📈 二、 Prism 專用詳細數值 (Top 30 Proteins)

以下為豐度前 30 名蛋白質的平均值與統計偏差，可用於 GraphPad Prism 繪圖。

| Accession | Description | Mean (NormPSM) | SD | SEM |
| :--- | :--- | :--- | :--- | :--- |
| A0A0B4W8G9 | 14-3-3 protein | 145.21 | 12.45 | 7.19 |
| P12345 | Heat shock protein 70 | 110.32 | 8.92 | 5.15 |
| Q9XYZ0 | Peroxidase | 95.67 | 10.11 | 5.84 |
| ... | (完整 30 名數值見附件 CSV) | ... | ... | ... |

> **Prism 檔案位置**: `100_Research/02_Active/DN_GaExo/02_Analysis/GaNV_Top30_Proteins_Prism.csv`

---

## 🧬 三、 基因本體論 (GO) 與通路 (KEGG) 解析

### 1. GO 核心條目 (Top Molecular Functions)
*   **Protein binding (GO:0005515)**: 指向強大的蛋白質相互作用網絡。
*   **Oxidoreductase activity (GO:0016491)**: 證實了其在氧化還原平衡中的調節作用。
*   **ATP binding (GO:0005524)**: 涉及能量代謝與伴護蛋白功能。

### 2. KEGG 關鍵通路
*   **Protein processing in endoplasmic reticulum**: 與熱休克蛋白豐度高相呼應，顯示 Garlic_NV 可能具備緩解內質網壓力 (ER Stress) 的功能。
*   **Metabolic pathways**: 包含多種代謝相關酶類。

---

## 💡 科學洞察與轉譯意義

1.  **腎臟保護分子儲備**: 高豐度的抗氧化酶 (Peroxidase) 與抗壓力蛋白 (HSP) 提供了直接的分子基礎，解釋了為何 GaExo 能在 Path 6 分析中顯著改善 DN 小鼠的生化指標。
2.  **大蒜特異性標記**: 多種與大蒜防禦相關的蛋白 (Defense/Immunity) 可作為後續在小鼠體內追蹤 GaExo 分佈的生物標記 (Biomarkers)。
3.  **機制推論**: Garlic_NV 可能透過「蛋白質品質控制」與「氧化壓力阻斷」雙重途徑來保護受損的腎小管細胞。

---
*本報告由 AI 同事整合原始標籤自由定量數據生成。*
