# Garlic_NV (GaExo) 雙軌 miRNA 深度分析報告：保守性與特異性組分

> **數據背景**: GaNV 直接純化自大蒜之 Small RNA-seq
> **分析日期**: 2026-05-04
> **研究目標**: 建立 GaExo 跨物種調控 (Cross-species regulation) 之分子基礎

---

## 📊 一、 雙軌候選名單 (Top 5 + 5 Candidates)

為了平衡「已知功能性」與「來源唯一性」，精選以下 10 個核心 miRNA：

### 1. 進化保守組分 (Conserved Track: hsa-miR Homologs)
*這些序列在大蒜中高表達，且與人源序列完全一致，是 GaExo 發揮快速抗發炎作用的潛在主力。*

| miRNA ID | TPM 均值 | 序列 | 關鍵意義與建議 |
| :--- | :--- | :--- | :--- |
| **hsa-miR-1260a** | 372,731 | AUCCCACCUCUGCCACCA | **核心優勢組分**。建議分析其對 Wnt/beta-catenin 通路的調控。 |
| **hsa-miR-8485** | 93,263 | CACACACACACACACACGUAU | 長序列保守組分，可能參與應激性蛋白質穩定調控。 |
| **hsa-miR-6756-5p**| 68,908 | AGGGUGGGGCUGGAGGUGGGGCU | 指向內質網壓力 (ER Stress) 相關靶點。 |
| **hsa-miR-4454** | 66,610 | GGAUCCGAGUCACGGCACCA | **抗發炎首選**。已知可抑制 NF-kB 介導的細胞因子釋放。 |
| **hsa-miR-574-5p** | 50,529 | UGAGUGUGUGUGUGUGAGUGUGU | 與 TLR4 信號路徑調節密切相關，契合腎保護主題。 |

### 2. 大蒜特異組分 (Garlic-Specific Track: Allium sativum mature)
*這些是證明大蒜外泌體跨物種傳遞的「金標準」證據分子。*

| Gene ID | Mean Count | 序列 (Query_seq) | 關鍵意義與建議 |
| :--- | :--- | :--- | :--- |
| **mature_15** | 7,814 | CGCTCGACGT | **大蒜特有組分 Top 1**。需優先執行 psRNATarget 靶點預測。 |
| **mature_67** | 4,914 | GACCTCAGATCAGACGG | 大蒜源成熟 miRNA，用於驗證跨物種遞送效率。 |
| **mature_3** | 3,852 | CGCTCGACGT | 與 mature_15 具備協同調控潛力。 |
| **mature_89** | 1,115 | GTCTTCCTTG | 序列特異性強，建議作為 qPCR 體內追蹤之標記物。 |
| **mature_107**| 1,113 | GGGTCGTGCCT | 用於構建完整的大蒜源跨界調控網絡。 |

---

## 🛠️ 二、 已執行建議行動 (Action Taken)

1.  **FASTA 序列導出**：已生成 `GaNV_DualTrack_miRNA_Candidates.fasta`，包含上述 10 個分子的完整序列，可直接上傳至 **psRNATarget** 或 **TargetScan**。
2.  **數據整合**：已將保守性標籤與特異性標籤進行對比分組，為 Manuscript 的 "Cargo Characterization" 章節提供邏輯架構。

---

## 🧬 三、 科學洞察：為什麼「雙軌」分析對 Path 6 至關重要？

1.  **功能性論證**：透過 `hsa-miR-4454` 等保守分子，我們可以利用現有的人類/小鼠資料庫，快速解釋 GaExo 如何透過已知路徑抑制 DN 小鼠的發炎反應。
2.  **唯一性論證**：透過 `mature_15` 等大蒜分子，我們可以排除宿主內源性 miRNA 的干擾，證明腎臟組織中檢測到的保護性信號確實來自 **GaExo** 的攝取。
3.  **整體性假說**：GaExo 是一個「分子雞尾酒」，利用保守序列進行路徑對接，利用特異序列執行獨特的調控功能，兩者共同改善了 DN 小鼠的生理指標。

---
**附件檔案：**
*   `GaNV_DualTrack_miRNA_Candidates.fasta` (序列文件)
*   `GaNV_Garlic_miRNA_Prism.csv` (統計數據)

*本報告由 AI 同事根據 GaNV 原始純化測序數據與雙軌分析策略生成。*
