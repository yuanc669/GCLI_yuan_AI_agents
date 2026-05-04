# GaExo (大蒜外泌體) 治療糖尿病腎病 (DN) 之分子機制驗證設計表

> **專案背景**: Path 6 - 大蒜外泌體 (GaExo) 對 DN 小鼠的治療機制研究
> **核心假說**: GaExo 透過跨物種遞送 miRNA，下調腎臟內促炎與促纖維化靶基因表現。
> **日期**: 2026-05-04

---

## 🧪 一、 實驗分組設計

| 組別 | 處理方式 | 樣本數量 (N) | 目的 |
| :--- | :--- | :--- | :--- |
| **Sham** | 假手術 + 生理食鹽水 | 6-8 | 建立生理基準值 |
| **DN (Model)** | STZ/HFD 誘導 + 生理食鹽水 | 6-8 | 建立疾病模型病理指標 |
| **DN + GaExo** | DN 模型 + GaExo 治療 | 6-8 | 驗證 GaExo 的分子干預效果 |

---

## 🧬 二、 驗證靶點矩陣 (miRNA-mRNA Mapping)

基於 GaNV 測序數據與文獻檢索，選定以下關鍵調控軸：

| 調控軸 | 關鍵 miRNA | 驗證靶基因 (mRNA) | 預期在 GaExo 治療組中的變化 | 病理意義 |
| :--- | :--- | :--- | :--- | :--- |
| **發炎/纖維化軸** | **hsa-miR-4454** | **Sparc** | **明顯下調** | 抑制細胞外基質沉積與纖維化 |
| **早期預警軸** | **hsa-miR-574-5p** | **Hmgb1** | **下調** | 阻斷 TLR4/NF-kB 介導的發炎反應 |
| **修復/纖維化軸** | **hsa-miR-1260a** | **Ctnnb1** | **下調** | 抑制 Wnt/beta-catenin 纖維化信號 |
| **身分證(Track)** | **mature_15** | (大蒜特異性) | **高檢出** | 證明 GaExo 成功進入腎臟組織 |

---

## 📋 三、 qPCR 引物序列 (小鼠 Mus musculus)

| 基因 (Gene) | 方向 | 序列 (5' -> 3') | 產物大小 |
| :--- | :--- | :--- | :--- |
| **Sparc** | F / R | `TACAACCCCGGCTACTACCA` / `CGGTCACTGTTGTCCCTGAA` | 134 bp |
| **Hmgb1** | F / R | `GATGGGCAAAGGAGATCCTAAG` / `TCTTCCTCCTTGGTCTTGGTCT` | 158 bp |
| **Ctnnb1** | F / R | `ATGGAGCCGGACAGAAAAGC` / `TGGGAGGTGTCAACATCTTCTTC` | 182 bp |
| **Gapdh** | F / R | `AGGTCGGTGTGAACGGATTTG` / `TGTAGACCATGTAGTTGAGGTCA` | 123 bp |

---

## 🛠️ 四、 標準操作流程 (SOP) 建議

### 1. 組織處理
*   取小鼠 **腎皮質 (Cortex)** 部分，立即投入液氮或 RNA 穩定液 (RNAprotect) 中。
*   使用 Trizol 法或柱式套件提取 **Total RNA**。

### 2. 逆轉錄 (Reverse Transcription) - **雙重路徑**
*   **mRNA 組**：使用 Random Primer 或 Oligo(dT) 進行一般逆轉錄。
*   **miRNA 組**：針對 `mature_15` 與 `hsa-miR-4454` 等，需使用 **Stem-loop 專用引物** 或 **Poly-A tailing** 法。

### 3. 數據分析 (Relative Quantification)
*   使用 **2^-ΔΔCt** 法計算相對表達量。
*   內對照：mRNA 使用 *Gapdh*；miRNA 建議使用 *U6* 或 *snoRNA202*。

---

## 📈 五、 預期結果展示建議
*   **圖 A**：GaExo 在腎臟中的攝取（檢測 `mature_15` 豐度）。
*   **圖 B**：三種靶基因 (*Sparc, Hmgb1, Ctnnb1*) 在三組間的 mRNA 表現變化。
*   **圖 C**：相關性分析（miRNA 豐度與其靶點 mRNA 表現量的相關係數）。

---
*本設計表由 AI 同事整合 GaNV 數據與最新腎病文獻產出。*
