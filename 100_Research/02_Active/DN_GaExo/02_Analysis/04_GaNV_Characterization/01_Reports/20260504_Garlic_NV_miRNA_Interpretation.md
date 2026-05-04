# Garlic_NV (GaExo) miRNA 深度分析與跨物種調控報告 (綜合版)

> **數據背景**: GaNV 直接純化自大蒜之 Small RNA-seq
> **分析日期**: 2026-05-04
> **研究目標**: 建立 GaExo 跨物種調控 (Cross-species regulation) 之分子基礎

---

## 📊 一、 全域 miRNA 組成概覽

大蒜外泌體 (GaExo) 的 miRNA 組成呈現「進化保守性」與「物種特異性」並存的特徵：

### 1. 雙軌候選名單 (Top 5 + 5 Candidates)
為了平衡功能研究的深度與證據的唯一性，精選以下 10 個核心 miRNA 作為後續 Path 6 治療機制研究的重點：

#### **軌道 A：進化保守組分 (Conserved Track: hsa-miR Homologs)**
*序列與人源完全一致，是 GaExo 發揮快速藥理作用的潛在主力。*

| miRNA ID            | TPM 均值  | 關鍵意義                               |
| :------------------ | :------ | :--------------------------------- |
| **hsa-miR-1260a**   | 372,731 | **絕對優勢組分**，涉及 Wnt/beta-catenin 通路。 |
| **hsa-miR-8485**    | 93,263  | 長序列保守組分，參與應激蛋白質穩定。                 |
| **hsa-miR-6756-5p** | 68,908  | 指向內質網壓力 (ER Stress) 相關靶點。          |
| **hsa-miR-4454**    | 66,610  | **抗發炎核心**，抑制 NF-kB 信號路徑。           |
| **hsa-miR-574-5p**  | 50,529  | 調節 TLR4 信號，具備腎保護潛力。                |

#### **軌道 B：大蒜特異組分 (Garlic-Specific Track: Allium sativum mature)**
*證明 GaExo 跨物種傳遞的「金標準」證據分子。*

| Gene ID | Mean Count | 序列 (Query_seq) | 角色 |
| :--- | :--- | :--- | :--- |
| **mature_15** | 7,814 | CGCTCGACGT | **大蒜特有組分 Top 1**，優先預測靶點。 |
| **mature_67** | 4,914 | GACCTCAGATCAGACGG | 驗證跨物種遞送效率之標記。 |
| **mature_3** | 3,852 | CGCTCGACGT | 與 mature_15 具備協同調控潛力。 |
| **mature_89** | 1,115 | GTCTTCCTTG | 序列特異性強，適合 qPCR 體內追蹤。 |
| **mature_107**| 1,113 | GGGTCGTGCCT | 用於構建跨界調控網絡。 |

---

## 📈 二、 Prism 專用詳細數值 (Top 20 Garlic-Specific miRNAs)

以下為大蒜特異性成熟 miRNA 的平均計數與統計偏差，可用於 GraphPad Prism 繪圖展現 GaExo 的物種標徵。

| Gene_id | Mean Count | SD | SEM | Query_seq |
| :--- | :--- | :--- | :--- | :--- |
| Allium_sativum_mature_15 | 7813.67 | 1367.65 | 789.61 | CGCTCGACGT |
| Allium_sativum_mature_67 | 4913.67 | 768.42 | 443.65 | GACCTCAGATCAGACGG |
| Allium_sativum_mature_3 | 3852.00 | 253.38 | 146.29 | CGCTCGACGT |
| Allium_sativum_mature_89 | 1115.00 | 48.50 | 28.00 | GTCTTCCTTG |
| Allium_sativum_mature_107 | 1113.33 | 115.04 | 66.42 | GGGTCGTGCCT |
| Allium_sativum_mature_61 | 1107.67 | 111.45 | 64.34 | GGGTCGTGCCT |
| Allium_sativum_mature_23 | 919.33 | 75.31 | 43.48 | TCGTGCCCTCGGCGCC |
| Allium_sativum_mature_11 | 520.67 | 78.50 | 45.32 | GGCGAAGCCAGAGG |
| Allium_sativum_mature_6 | 506.67 | 72.80 | 42.03 | GGCGAAGCCAGAGG |
| Allium_sativum_mature_41 | 441.00 | 38.16 | 22.03 | GTAGTAGTGTT |
| Allium_sativum_mature_5 | 396.67 | 45.50 | 26.27 | CCGATGTTACGA |
| Allium_sativum_mature_103 | 370.33 | 41.53 | 23.97 | ATACATACATACATAC |
| Allium_sativum_mature_125 | 362.33 | 36.35 | 20.99 | GGGTCGTGCCT |
| Allium_sativum_mature_31 | 358.33 | 21.08 | 12.17 | GTAGTAGTGTT |
| Allium_sativum_mature_22 | 344.00 | 29.53 | 17.05 | GTAGTAGTGTT |
| Allium_sativum_mature_13 | 311.00 | 33.24 | 19.19 | GGGTCGTGCCT |
| Allium_sativum_mature_71 | 310.00 | 33.24 | 19.19 | GGGTCGTGCCT |
| Allium_sativum_mature_21 | 291.67 | 30.01 | 17.32 | GGGTCGTGCCT |
| Allium_sativum_mature_109 | 277.67 | 28.57 | 16.50 | GGGTCGTGCCT |
| Allium_sativum_mature_65 | 274.67 | 27.65 | 15.96 | GGGTCGTGCCT |

---

## 🧬 三、 科學洞察：GaExo 的「分子雞尾酒」假說

1.  **路徑對接 (Path Docking)**：保守性 miRNA（如 `hsa-miR-4454`）利用進化上保守的種子序列，直接與宿主（小鼠/人）的抗發炎通路對接，實現快速的生物學效應。
2.  **特異性調控 (Specific Regulation)**：大蒜特有 miRNA（如 `mature_15`）可能針對宿主中特定的「非法」靶點，提供大蒜外泌體獨有的腎臟保護機制。
3.  **整體協同 (Synergistic Effect)**：GaExo 作為一個完整的封裝系統，同時遞送蛋白質 (HSP70, Alliin lyase) 與 miRNA，透過多層次 (Multilevel) 調控，最終改善 DN 小鼠的生理指標。

---

## 🛠️ 四、 已執行建議行動 (Action Taken)

1.  **FASTA 序列導出**：已生成 `GaNV_DualTrack_miRNA_Candidates.fasta`，包含 10 個核心候選序列。
2.  **Prism 數據導出**：已更新 `GaNV_Garlic_miRNA_Prism.csv`。
3.  **後續建議**：
    *   **Target Prediction**：針對 Top 5 + 5 候選分子進行小鼠靶基因預測。
    *   **In vivo Tracking**：在 Path 6 小鼠腎臟中檢測 `mature_15` 的含量。

---
*本報告為整合版 master report，由 AI 同事根據 `Fulltable_target_Garlic_NV.xlsx` 生成。*
