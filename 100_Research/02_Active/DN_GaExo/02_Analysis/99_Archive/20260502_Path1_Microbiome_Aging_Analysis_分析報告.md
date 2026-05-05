# [20260502] Path1_Microbiome_Aging_Analysis_分析報告

> [!INFO]
> 數據來源: `Path1_Microbiome_Aging_Analysis.csv`
> 分析對象: Sham (12W) vs Sham (20W)
> 產出日期: 2026-05-02
> 狀態: [正式分析報告]

## 🔬 顯著差異菌屬摘要 (Top 10)

以下為根據 P-value 排序最顯著的老化相關菌相變動：

| Phylum | Genus | Species | Mean (12W) | Mean (20W) | Log2FC | P-value | 趨勢 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bacteroidota | Spongiimonas | unclassified | 0.0032 | 0.0000 | -21.61 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Duncaniella | Duncaniella dubosii | 0.0000 | 0.0013 | 20.30 | < 0.0001 | ⬆️ 顯著增加 |
| Bacteroidota | unclassified | unclassified | 0.0013 | 0.0000 | -20.26 | 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Spongiimonas | Spongiimonas flava | 0.0045 | 0.0000 | -22.11 | 0.0001 | ⬇️ 顯著減少 |
| Pseudomonadota | unclassified | unclassified | 0.0011 | 0.0000 | -20.12 | 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Bacteroides_H_857956 | B. acidifaciens | 0.1574 | 0.0716 | -1.14 | 0.0002 | ⬇️ 顯著減少 |
| Bacillota_A_368345 | Eubacterium_R | unclassified | 0.0046 | 0.0000 | -22.14 | 0.0005 | ⬇️ 顯著減少 |
| Bacteroidota | UBA3263 | sp001689615 | 0.0000 | 0.0059 | 22.50 | 0.0005 | ⬆️ 顯著增加 |
| Pseudomonadota | Escherichia | unclassified | 0.0000 | 0.0032 | 21.61 | 0.0010 | ⬆️ 顯著增加 |
| Bacteroidota | UBA7173 | sp002491305 | 0.0690 | 0.0163 | -2.08 | 0.0016 | ⬇️ 顯著減少 |


## 📊 統計深度補強 (Statistical Rigor)

### 1. Alpha 多樣性顯著性檢定
| 指標 | Sham (Mean) | Sham10W (Mean) | P-value | 顯著性 |
| :--- | :--- | :--- | :--- | :--- |
| **Shannon** | 3.5756 | 3.7286 | 0.1792 | n.s. |
| **Chao1** | 161.98 | 122.00 | 0.0023 | * |

### 2. 群落結構組成 (Taxonomic Composition)
![Stacked Bar Plot](20260502_Path1_Stacked_Bar_Plot.png)
- **觀察**: 
  - **Bacteroidota** (橘色系) 在老化過程中雖然保持優勢，但其內部的屬級構成發生了置換。
  - `Others` 比例在 20W 時有所增加，暗示了一些低豐度機會致病菌的自然累積。

## 💡 生物學意義解讀

1. **老化基底變動**: 
   - **Bacteroides acidifaciens** 的顯著減少 (-1.14 Log2FC) 值得注意。此菌通常與代謝調節有關，其隨年齡下降可能反映了腸道免疫功能的變化。
   - **Escherichia** 的增加 (+21.61 Log2FC)雖然相對豐度仍低 (0.3%)，但可能暗示了老年小鼠腸道微環境趨向於促發炎狀態。

2. **對後續實驗的影響**:
   - 在評估 **GaExo** 的療效時，必須扣除上述老化導致的基底變動。特別是 `Duncaniella` 系列的增減，應區分是 GaExo 逆轉了老化，還是與老化協同作用。

3. **HE 評分關聯預測**:
   - 預期顯著減少的益生菌屬（如部分 Bacteroidota）與腎小管間質損傷評分 (TIS) 呈負相關。

---
*本報告由 `/data-interpret` 自動生成，並遵循 [日期][文件名]_分析報告 命名規範。*
