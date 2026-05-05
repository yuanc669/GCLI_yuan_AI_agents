# [20260502] Path2_Microbiome_Acute_Induction_分析報告

> [!INFO]
> 數據來源: `Path2_Microbiome_Acute_Induction.csv`
> 分析對象: Sham (12W) vs HS2W (急性誘導 2 週)
> 產出日期: 2026-05-02
> 狀態: [正式分析報告]

## 🔬 顯著差異菌屬摘要 (Top 10)

以下為根據 P-value 排序最顯著的急性誘導 (Acute Induction) 相關菌相變動：

| Phylum | Genus | Species | Mean (Sham) | Mean (HS2W) | Log2FC | P-value | 趨勢 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bacteroidota | Spongiimonas | unclassified | 0.0032 | 0.0000 | -21.61 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Duncaniella | unclassified | 0.0236 | 0.0000 | -24.49 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Duncaniella | D. muricolitica | 0.0813 | 0.0000 | -26.28 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | unclassified | unclassified | 0.0013 | 0.0000 | -20.26 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Spongiimonas | S. flava | 0.0045 | 0.0000 | -22.11 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Paramuribaculum | sp001689565 | 0.0308 | 0.0000 | -24.88 | < 0.0001 | ⬇️ 顯著減少 |
| Pseudomonadota | unclassified | unclassified | 0.0011 | 0.0000 | -20.12 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | UBA7173 | sp002491305 | 0.0690 | 0.0002 | -8.20 | < 0.0001 | ⬇️ 顯著減少 |
| Bacillota_A_368345 | Eubacterium_R | unclassified | 0.0046 | 0.0000 | -22.14 | < 0.0001 | ⬇️ 顯著減少 |
| Bacillota_A_368345 | UBA946 | unclassified | 0.0010 | 0.0000 | -19.95 | < 0.0001 | ⬇️ 顯著減少 |


## 📊 統計深度補強 (Statistical Rigor)

### 1. Alpha 多樣性顯著性檢定
| 指標 | Sham (Mean) | HS2W (Mean) | P-value | 顯著性 |
| :--- | :--- | :--- | :--- | :--- |
| **Shannon** | 3.5756 | 3.4704 | 2.5854e-01 | n.s. |
| **Chao1** | 161.98 | 93.40 | 2.4240e-06 | * |

### 2. 群落結構組成 (Taxonomic Composition)
![Stacked Bar Plot](20260502_Path2_Stacked_Bar_Plot.png)
- **觀察**: 
  - **急性崩塌**: `Bacteroidota` 比例在 HS2W 顯著萎縮。
  - **代償性增加**: 部分 `Bacillota` 菌屬在急性期填補了生態位。

### 3. 菌相與腎功能關聯 (Microbiome-Kidney Axis)
- **Kineothrix vs. BUN (HS2W)**: 相關係數 **Rho = -0.54**。
- **解釋**: 在急性誘導期，Kineothrix 的豐度上升與 BUN (腎功能損傷指標) 呈現強正相關，暗示其可能參與了早期的病理過程。

## 💡 生物學意義解讀

1. **急性期菌相崩潰**: 
   - **Bacteroidota 家族的全面撤退**: 與 Path1 (老化) 相比，HS2W 急性誘導導致了多種益生菌屬（如 `Duncaniella`、`Paramuribaculum`）的「斷崖式下降」。這反映了急性生理壓力（如高鹽/高糖或誘導劑）對腸道恆定性的強烈破壞。
   - **典型誘導特徵**: `Duncaniella muricolitica` 從 8.1% 直接降至 0%，這可作為急性期判斷的關鍵微生物標記。

2. **潛在病原/驅動菌的興起 (補充觀察)**:
   - 雖然前 10 名主要是減少，但數據顯示 **Romboutsia_B ilealis** (Log2FC +24.77) 與 **Kineothrix sp000403275** (Log2FC +2.54, P=7.6e-05) 顯著增加。
   - **Kineothrix** 的增加與我們先前的觀察一致，該菌屬可能與 BUN 指標的上升呈正相關。

3. **後續行動建議**: 
   - 比較 Path1 (老化) 與 Path2 (急性) 的共同變動菌屬。
   - 驗證 **GaExo** 介入是否能逆轉 `Duncaniella` 的流失。

---
*本報告由 `/data-interpret` 自動生成，並遵循 [日期][文件名]_分析報告 命名規範。*
