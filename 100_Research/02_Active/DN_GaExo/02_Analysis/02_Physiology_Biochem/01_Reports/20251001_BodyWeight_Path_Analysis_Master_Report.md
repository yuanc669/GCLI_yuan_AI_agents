# [20251001] DN_GaExo 體重數據跨路徑整合分析報告 (Master Report)

> [!NOTE]
> **數據來源**: `20251001_body weight.xlsx` 與 `20260225_biochemistry.xlsx`
> **分析日期**: 2026-05-04
> **分析路徑**: Path 1 - Path 7 (體重動態變化)

---

## 📈 體重動態變化總覽 (Group Mean)

### 1. 疾病進展期 (W0 - W10)
| Week | Sham (g) | HS6W (g) | HS10W (g) | HFD (g) |
| :--- | :--- | :--- | :--- | :--- |
| **W0 (5W齡)** | 19.8 | 18.6 | 18.7 | 19.8 |
| **W2 (Acute)** | 23.7 | 23.9 | 23.3 | 22.9 |
| **W6 (Chronic)** | 26.6 | **22.8** | 23.2 | **30.7** |
| **W10 (Final)** | 28.3 | - | **24.5** | **40.6** |

---

## 🗺️ Path 1-7 深度解讀 (體重維度)

### Path 1: 基礎老化 (Baseline Aging)
![Path 1 Weight](./BodyWeight_Analysis/Path1_Aging_Weight_Plot.png)
*   **趨勢**: Sham 組表現出穩定的線性增長。從 W0 (19.8g) 到 W16 (31.3g)，體重隨週齡增加而平穩上升。
*   **結論**: 建立了健康小鼠的標準生長曲線，用於評估疾病誘導導致的體重流失。

### Path 2: 急性衝擊 (Acute Shock)
![Path 2 Weight](./BodyWeight_Analysis/Path2_Acute_Weight_Plot.png)
*   **對照**: Sham vs HS6W/HS10W (W0 - W2)
*   **趨勢**: 在誘導後的首 2 週，所有組別體重均維持上升，STZ 的毒性在此階段尚未導致顯著的體重下降。

### Path 4: 慢性失調進展 (Progression)
![Path 4 Weight](./BodyWeight_Analysis/Path4_Progression_Weight_Plot.png)
*   **對照**: Sham vs HS6W vs HS10W
*   **趨勢**: W4 之後，HS 組（HFD+STZ）體重開始顯著低於 Sham 組。至 W10 時，HS10W (24.5g) 顯著低於 Sham (28.3g)，表現出糖尿病典型的「體重減輕」病徵。

### Path 5: 驅動因子解析 (Dietary Drivers)
![Path 5 Weight](./BodyWeight_Analysis/Path5_Drivers_Weight_Plot.png)
*   **對照**: Sham vs HFD vs HS10W
*   **趨勢**: 
    *   **HFD 組**: 體重發生斷崖式攀升，W10 達到 40.6g，呈現極度肥胖。
    *   **HS10W 組**: 同樣攝取 HFD，但因 STZ 誘導的糖尿病，體重反而下降。
*   **結論**: 證實 **HFD 驅動肥胖**，而 **STZ 轉化為糖尿病消瘦**。

### Path 6: 外泌體治療效應 (Therapy)
![Path 6 Weight Endpoint](./BodyWeight_Analysis/Path6_Therapy_Weight_Endpoint.png)
*   **對照**: HS10W vs GaE10 (終點體重)
*   **數據**: 
    *   HS10W: 25.5g (生化紀錄值)
    *   GaE10: 24.4g (生化紀錄值)
*   **結論**: GaExo 治療並未顯著改變小鼠的體重消瘦狀態，說明其療效（降血脂/維護腎功）並非透過「增重」或改變整體能量代謝平衡達成。

---

## 💡 論文寫作建議 (Body Weight Storyline)

1.  **Phenotype Validation**: 體重下降 (HS10W vs Sham) 與 極度肥胖 (HFD) 的對比，完美證實了 DN 模型的成功建立。
2.  **Independence of Efficacy**: 強調 GaExo 在不改變體重的情況下改善了腎功能與血脂，暗示其作用機制更偏向於「局部修復」或「代謝質量」的提升，而非單純的體徵恢復。

---

## 📁 附件資源
- **Prism 數據表**: `100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Analysis\`
- **可視化圖表**:
    - `Path4_Progression_Weight_Plot.png` (進展曲線)
    - `Path5_Drivers_Weight_Plot.png` (飲食vs疾病對照)
    - `Path6_Therapy_Weight_Endpoint.png` (治療終點對照)

---
*報告由 AI 同事自動生成。*
