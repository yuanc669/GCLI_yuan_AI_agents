# [20260502] Path4_Microbiome_TimeCourse_分析報告

> [!INFO]
> 數據來源: `Path4_Microbiome_TimeCourse.csv`
> 分析對象: Sham -> HS2W -> HS6W -> HS10W (疾病進展時間軸)
> 產出日期: 2026-05-02
> 狀態: [正式分析報告]

## 🔬 關鍵動態趨勢摘要

本分析追蹤了從健康狀態 (Sham) 到疾病誘導末期 (10W) 的菌相動態演變：

### 📈 持續增加組 (Disease-Associated Drivers)
| Phylum | Genus | Species | 趨勢描述 | 生物學意義預測 |
| :--- | :--- | :--- | :--- | :--- |
| Bacillota_A | Kineothrix | sp000403275 | HS2W 飆升後維持高位 (0.10) | **關鍵驅動菌**: 可能與 BUN/肌酸酐上升直接相關。 |
| Bacteroidota | Lepagella | sp900547755 | 從 0.009 (Sham) 遞增至 0.05 (10W) | **慢性化指標**: 隨病程進展穩定擴張。 |
| Bacillota_A | Romboutsia_B | R. ilealis | 從 0.0 爆發至 0.03 (10W) | **急性爆發菌**: 誘導後迅速佔據生態位。 |
| Actinomycetota | Granulimonas | unclassified | 穩步從 0.0 增加至 0.005 | **晚期共生菌**: 與慢性發炎環境相關。 |

### 📉 持續減少組 (Depleted Beneficial Taxa)
| Phylum | Genus | Species | 趨勢描述 | 生物學意義預測 |
| :--- | :--- | :--- | :--- | :--- |
| Bacteroidota | Muribaculum | M. gordoncarteri | 從 0.02 降至 0.001 (10W) | **保護性菌屬喪失**: 腸道屏障功能受損的指標。 |
| Bacteroidota | UBA7173 | sp002491305 | 從 0.06 降至 0.0001 | **核心菌屬崩潰**: 反映腸道生態系的劇烈動盪。 |
| Bacillota_A | COE1 | unclassified | 從 0.008 持續下降至 0.001 | **豐度縮減**: 隨疾病進展被排除出優勢位。 |

## 💡 時間序列洞察 (Time-Course Insights)

1. **急性衝擊期 (Sham -> HS2W)**:
   - 這是菌相變動最劇烈的階段。絕大多數 `Bacteroidota` 家族成員在此階段發生「斷崖式下降」。
   - `Kineothrix` 的爆發式增長發生在第 2 週，這與急性腎損傷的發生時間點高度契合。

2. **慢性維持期 (HS2W -> HS10W)**:
   - 菌相多樣性並未恢復，而是轉向了一種以 `Kineothrix`、`Lepagella` 與 `Romboutsia` 為主的「疾病穩定態」。
   - 此階段的變動斜率較緩，反映了腸道微環境已進入慢性發炎與代謝異常的惡性循環。

3. **轉譯與介入點**:
   - 介入實驗 (GaExo) 的最佳觀察點應在 **第 2 週至第 6 週之間**，觀察其是否能遏止 `Bacteroidota` 的持續流失並抑制 `Kineothrix` 的擴張。

---
*本報告由 `/data-interpret` 自動生成，並遵循 [日期][文件名]_分析報告 命名規範。*
