# 學術論文文本：AP_GiNV 蛋白質體學分析 (Materials & Methods / Results)

## 🧪 材料與方法 (Materials and Methods)

### 1. Proteomic Profiling of Ginger-derived Nanovesicles (GiNVs)
The protein composition of isolated GiNVs was characterized using liquid chromatography-tandem mass spectrometry (LC-MS/MS). Briefly, GiNV proteins were extracted, reduced, alkylated, and digested with trypsin. The resulting peptides were analyzed using an LTQ Orbitrap mass spectrometer coupled with an UltiMate 3000 RSLCnano system. 

### 2. Bioinformatic Analysis and Protein Quantification
Protein identification was performed against the *Zingiber officinale* database using Proteome Discoverer software. Label-free quantification (LFQ) was employed to determine the relative abundance of proteins across independent replicates (n=3). Normalized intensity values were used for downstream analysis. Gene Ontology (GO) enrichment analysis was conducted to categorize the identified proteins into functional groups, including biological processes, molecular functions, and cellular components. High-abundance proteins (Top 30) and enriched pathways were visualized using Python-based libraries (Seaborn/Matplotlib) and GraphPad Prism 9.0.

---

## 📈 結果描述 (Results)

### 1. Proteomic Landscape of Ginger-derived Nanovesicles
To elucidate the molecular basis of the protective effects of GiNVs against aspiration pneumonia, we performed a comprehensive proteomic analysis. A total of [Insert Total Number] proteins were identified, reflecting a diverse array of bioactive components. As shown in **Figure XA (Heatmap)**, the Top 30 most abundant proteins (indexed by Accession) exhibited high consistency across three independent GiNV batches. Notable among these were structural markers such as **Clathrin heavy chain** and **Annexin**, confirming the identity of GiNVs as intact extracellular vesicle-like particles.

### 2. Functional Enrichment Highlights Multi-targeted Protective Mechanisms
GO enrichment analysis (Pathway Bubble Plot, **Figure XB**) revealed that the GiNV proteome is significantly enriched in pathways critical for mitigating acute lung injury (ALI). Specifically, biological processes related to **Antioxidant activity** (e.g., Peroxidases, SOD), **Response to stress**, and **Protein folding** (e.g., HSP70/90 family) were prominently represented. Furthermore, we identified key regulatory proteins involved in the **Negative regulation of inflammatory response** (e.g., 14-3-3 domain proteins), suggesting that GiNVs exert their therapeutic effects through a multi-targeted approach, combining direct ROS scavenging with the modulation of pro-inflammatory signaling pathways (e.g., TLR4/NF-κB).

---

## 🔗 數據與圖表對應
- **Heatmap 數據**: `AP_GiNV_Top30_Proteins_Heatmap_v2.csv`
- **GO 氣泡圖數據**: `AP_GiNV_GO_Enrichment_v2.csv`
- **對應圖片**: `AP_GiNV_Top30_Heatmap_v2.png`, `AP_GiNV_GO_BubblePlot.png`

---
*Drafted by Gemini CLI / Senior Research Colleague*
