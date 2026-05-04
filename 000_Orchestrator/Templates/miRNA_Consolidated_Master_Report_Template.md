# {{Sample_Name}}_NV ({{Abbreviation}}Exo) 雙軌 miRNA 深度鑑定與跨物種調控報告

> **數據來源**: {{Sample_Full_Name}}-derived Nanovesicles ({{Abbreviation}}NV) Small RNA-seq 原始數據  
> **分析日期**: {{Analysis_Date}}  
> **報告核心**: 建立{{Sample_Name}}外泌體跨物種傳遞 (Cross-species communication) 之分子證據鏈。

---

## 📊 一、 雙軌 miRNA 鑑定策略 (Dual-Track Strategy)

本分析採用雙軌並行模式，旨在同時論證 PDExo 的**藥理功能性**與**物種來源唯一性**。

### 軌道 A：進化保守組分 (Conserved Track: hsa-miR Homologs)
*這些序列在植物中高豐度表達，且與人/鼠源序列 100% 一致。它們是 PDExo 直接與宿主抗發炎通路對接的「萬能鑰匙」。*

| miRNA ID (Homolog) | TPM 均值 (表達量) | 序列 (5' -> 3') | 關鍵功能與機轉 |
| :--- | :---: | :--- | :--- |
| **{{Homolog_ID_1}}** | {{TPM_1}} | {{Seq_1}} | {{Function_1}} |
| **{{Homolog_ID_2}}** | {{TPM_2}} | {{Seq_2}} | {{Function_2}} |
| **{{Homolog_ID_3}}** | {{TPM_3}} | {{Seq_3}} | {{Function_3}} |
| **{{Homolog_ID_4}}** | {{TPM_4}} | {{Seq_4}} | {{Function_4}} |
| **{{Homolog_ID_5}}** | {{TPM_5}} | {{Seq_5}} | {{Function_5}} |

### 軌道 B：植物特異組分 (Specific Track: Plant mature)
*這些序列僅存在於{{Sample_Name}}基因組中，是證明 PDExo 確實被宿主攝取並運送至目標器官的「金標準」證據分子。*

| miRNA ID (Specific) | Mean Count | 序列 (5' -> 3') | 在專案中的角色 |
| :--- | :---: | :--- | :--- |
| **{{Specific_ID_1}}** | {{Mean_1}} | {{S_Seq_1}} | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **{{Specific_ID_2}}** | {{Mean_2}} | {{S_Seq_2}} | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **{{Specific_ID_3}}** | {{Mean_3}} | {{S_Seq_3}} | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **{{Specific_ID_4}}** | {{Mean_4}} | {{S_Seq_4}} | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **{{Specific_ID_5}}** | {{Mean_5}} | {{S_Seq_5}} | 作為體內追蹤 (In vivo tracking) 之標記。 |

---

## 📈 二、 表達量統計摘要 (Prism-Ready Data)

以下數據可用於繪製 {{Sample_Name}}NV miRNA Cargo 的特徵圖：

| miRNA (Specific ID) | Mean Count | SD | SEM |
| :--- | :---: | :---: | :---: |
| {{Specific_ID_1}} | {{Mean_1}} | {{SD_1}} | {{SEM_1}} |
| {{Specific_ID_2}} | {{Mean_2}} | {{SD_2}} | {{SEM_2}} |
| {{Specific_ID_3}} | {{Mean_3}} | {{SD_3}} | {{SEM_3}} |
| {{Specific_ID_4}} | {{Mean_4}} | {{SD_4}} | {{SEM_4}} |
| {{Specific_ID_5}} | {{Mean_5}} | {{SD_5}} | {{SEM_5}} |

### 完整數據清單 (Prism Data Format)

{{Complete_Prism_Table_Markdown}}

---

## 🖼️ 三、 數據可視化 (Visualization)

![{{Sample_Name}} miRNA Distribution]({{Image_Path}})

## 🧬 四、 科學洞察 (Scientific Insights)

1. **高豐度藥理背景**：**{{Top_Homolog}}** 在 {{Sample_Name}}NV 中的 TPM 表達極高，說明其為該 miRNA 的強效遞送系統。
2. **跨界調控基礎**：透過保守組分對應宿主通路，實現了「精確路徑對接」；透過特異組分證明其「外源唯一性」。
3. **機制驗證建議**：後續應針對 Top 5 保守組分進行靶基因驗證，並在組織中檢測 **{{Top_Specific}}** 的含量。

---
*本報告由 Gemini CLI 自動生成。*
