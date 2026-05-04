# Ginger NV 短期生物資訊分析報告 (Short-term Bioinformatics Report)

**分析目標**: 快速識別功能富集趨勢、準備外部工具輸入檔案、識別潛在核心節點蛋白 (Hub Proteins)。

---

## 1. 模擬功能富集 (Simulated Functional Enrichment)
由於原始數據缺乏 GO/KEGG 標籤，我們透過關鍵字過濾對 490 個蛋白質進行了功能歸類。

| 功能類別 (Category) | 蛋白質數量 (Count) | 累計豐度 (Sum) | 核心代表蛋白 (Top Proteins) |
| :--- | :--- | :--- | :--- |
| **Translation/Ribosome** | 178 | 4239.21 | Ribosomal protein L3, 40S ribosomal protein S4 |
| **Carbohydrate Metabolism** | 46 | 386.64 | Alpha-1,4 glucan phosphorylase, Phosphoglycerate kinase |
| **Proteolysis** | 16 | 156.70 | Cysteine protease gp2a, Ubiquitin-like protein |
| **Redox/Antioxidant** | 20 | 130.16 | Peroxidase, Glutathione S-transferase |
| **Transport/Vesicle** | 12 | 90.51 | Clathrin heavy chain, Annexin, Rab protein |
| **Defense/Signaling** | 7 | 56.54 | 14-3-3 protein, Lipoxygenase |

**分析結論**: Ginger NV 的蛋白質組主要由 **蛋白質合成與翻譯機制** 驅動。此外，顯著的 **碳水化合物代謝** 與 **蛋白酶活性** (尤其是 Cysteine protease) 是其潛在的生物活性來源。

---

## 2. 潛在核心節點蛋白 (Hub Protein Candidates)
以下蛋白質在細胞信號傳導或囊泡運輸中具有關鍵作用，且在 Ginger NV 中表現豐度較高，適合作為 PPI 網絡的核心分析目標。

| Accession | Description | Mean Abundance | 功能重要性 |
| :--- | :--- | :--- | :--- |
| A0A8J5LRH6 | Lipoxygenase | 47.96 | 植物防禦信號傳導關鍵 |
| A0A8J5H3Y4 | 14-3-3 domain-containing protein | 40.52 | 廣泛的蛋白質交互作用調節 |
| A0A8J5HL63 | Clathrin heavy chain | 36.31 | 網格蛋白介導的囊泡運輸 |
| A0A8J5I765 | Annexin domain-containing protein | 14.88 | 鈣離子依賴型膜結合蛋白 |
| A0A8J5HLH3 | Rab family GTPase | 9.07 | 囊泡對接與融合調節 |

---

## 3. 外部工具操作指南 (External Tool Inputs)

我們已為您準備好外部工具所需的輸入檔案，請直接下載/上傳：

### 3.1 g:Profiler (功能富集分析)
- **檔案**: `02_Analysis/Short_Term/Ginger_Top100_Accessions.txt`
- **操作**: 
    1. 前往 [g:Profiler](https://biit.cs.ut.ee/gprofiller/gost)。
    2. 將檔案內容複製到輸入框。
    3. 在 **Organism** 選擇 "Zingiber officinale" (或相似物種如 *Oryza sativa*)。
    4. 點擊 **Run query** 查看 GO/KEGG 圖表。

### 3.2 STRING-DB (蛋白質交互網絡)
- **檔案**: `02_Analysis/Short_Term/Ginger_Top100_Accessions.txt`
- **操作**:
    1. 前往 [STRING-DB](https://string-db.org/)。
    2. 點擊 **SEARCH** ➔ **Multiple Proteins**。
    3. 上傳 Accession 列表，物種選擇 "Zingiber officinale"。
    4. 分析 Hub 節點與 Cluster。

---

## 4. 檔案位置總結
- **Top 100 ID 列表**: `02_Analysis/Short_Term/Ginger_Top100_Accessions.txt`
- **關鍵字富集表**: `02_Analysis/Short_Term/Ginger_Keyword_Enrichment.csv`
- **核心蛋白候選表**: `02_Analysis/Short_Term/Ginger_Hub_Candidates.csv`
