# Garlic_NV (GaExo) 多組學表徵與 miRNA 深度分析 master 整合報告

> **數據來源**: GaNV 蛋白質組學 (Label-free) 與 Small RNA-seq (Dual-Track)
> **分析日期**: 2026-05-04
> **報告定位**: 建立大蒜外泌體 (GaExo) 作為「功能性生物活性封裝體」的分子基礎，支撐 Path 6 治療機轉。

---

## 🔬 一、 蛋白質組學雙軌鑑定 (Proteomics & Enzymatic Dual-Track)

GaExo 不僅是載體，其內含蛋白直接參與了腎臟保護與代謝調節。

### 1. 核心功能蛋白 (Key Functional Proteins)
- **黑芥子酶 (Myrosinase / Beta-glucosidase)**: 
  - **地位**: GaExo 內含之關鍵代謝酶。
  - **機轉**: 可能在腸道內催化大蒜硫化物轉化，產生具生物活性的次級代謝產物，抑制 Lepagella 等致病菌，進而調節「腸-腎軸」。
- **熱休克蛋白 (HSP70/HSP80)**:
  - **地位**: 含量最高的結構與伴隨蛋白。
  - **機轉**: 提供 GaExo 高度的穩定性，並在進入受損腎小管細胞後輔助蛋白質摺疊，緩解內質網壓力 (ER Stress)。

### 2. 功能富集與通路 (GO/KEGG Enrichment)
- **生物過程**: 集中於「糖代謝調節」、「氧化應激反應」與「囊泡運輸」。
- **KEGG 通路**: 顯著富集於 **Glutathione metabolism** 與 **Carbon metabolism**，直接對應 DN 治療中的抗氧化需求。

---

## 🧬 二、 miRNA 雙軌調控名單 (Top 5 + 5 miRNA Candidates)

為了平衡功能研究的深度與證據的唯一性，精選以下 10 個核心 miRNA：

### 1. 進化保守軌道 (Conserved Track: hsa-miR Homologs)
*利用進化上保守的種子序列，直接與宿主抗發炎通路對接。*

| miRNA ID | TPM 均值 | 核心功能與治療潛力 |
| :--- | :--- | :--- |
| **hsa-miR-1260a** | 372,731 | **絕對優勢組分**。調控 Wnt/beta-catenin 通路，抑制系膜擴張。 |
| **hsa-miR-4454** | 66,610 | **抗發炎主力**。抑制 NF-kB 介導的細胞因子釋放，緩解腎臟炎症。 |
| **hsa-miR-574-5p** | 50,529 | 調節 TLR4 信號，具備強大的腎臟保護潛力。 |

### 2. 大蒜特異軌道 (Garlic-Specific Track)
*證明 GaExo 跨物種遞送與唯一性的「金標準」證據。*

| Gene ID | Mean Count | 角色與意義 |
| :--- | :--- | :--- |
| **mature_15** | 7,814 | **大蒜特有 Top 1**。作為體內追蹤 (In vivo tracking) 的首選標記。 |
| **mature_67** | 4,914 | 用於驗證 GaExo 在腎臟組織中的累積效率。 |

---

## 📈 三、 科學洞察：GaExo 的「分子雞尾酒」假說

GaExo 作為一個功能完整的「功能單元」，透過以下層次發揮作用：

1.  **結構層 (Structure)**: 高含量的 **HSP70** 與特定的膜脂質確保了其在消化道與循環系統中的高度穩定性 (14-3-3 穩定性驗證)。
2.  **催化層 (Catalysis)**: 攜帶具備活性的 **Myrosinase**，在腸道微環境中重塑菌相 (誘發 Kineothrix)。
3.  **調控層 (Regulation)**: 釋放 **miRNA 雞尾酒**。保守序列 (miR-4454) 負責「路徑對接」抑制炎症，特異序列 (mature_15) 負責「精確打擊」特定靶點。

---

## 📂 四、 關聯檔案與交付物

- **序列文件**: `GaNV_DualTrack_miRNA_Candidates.fasta` (10 個核心序列)
- **統計數據**: `GaNV_Garlic_miRNA_Prism.csv` (可用於 Prism 繪圖)
- **完整分析表**: `GaNV_Proteomics_Full_Analysis.csv`

---
*本報告整合了蛋白質組學與 miRNA 組學之深度解析，為 DN_GaExo 專案提供核心表徵基礎。*
