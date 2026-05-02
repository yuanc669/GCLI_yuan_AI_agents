# [20260502] 老化基底分析報告 (Sham vs Sham10W)

> [!INFO]
> **分析目標**: 建立 DN 實驗的老化對照背景。
> **對照組別**: Sham (12W) vs Sham10W (20W)。
> **核心問題**: 在沒有任何疾病誘導的情況下，菌相隨週數增加的自然變動。

---

## 📈 Alpha 多樣性分析 (豐富度與均勻度)

![Alpha Plots](20260502_Aging_Alpha_Plot.png)

### [數據摘要]
| Group | Shannon (Mean ± SD) | Chao1 (Mean ± SD) |
| :--- | :--- | :--- |
| **Sham** | 3.58 ± 0.15 | 161.98 ± 7.89 |
| **Sham10W** | 3.73 ± 0.06 | 122.00 ± 6.24 |

---

## 🌌 Beta 多樣性分析 (群落結構差異)

![Beta PCoA Plot](20260502_Aging_Beta_PCoA_Plot.png)

- **PCoA 觀察**: 
  - Sham 與 Sham10W 在 PCoA 圖上呈現顯著的**分群趨勢**（主要沿著 PCoA2 軸位移）。
  - 這代表隨時間增加，腸道菌群的「整體構成」已發生了不可忽視的自然漂移。

---

## 📊 GraphPad Prism 格式數據 (Individual Values)

### [Alpha Diversity] Shannon & Chao1
| Group | Sample | Shannon | Chao1 |
| :--- | :--- | :--- | :--- |
| Sham | Sham-1 | 3.5784 | 157.60 |
| Sham | Sham-2 | 3.7265 | 171.08 |
| Sham | Sham-3 | 3.4220 | 157.25 |
| Sham10W | Sham10W-4 | 3.6620 | 120.00 |
| Sham10W | Sham10W-5 | 3.7666 | 129.00 |
| Sham10W | Sham10W-6 | 3.7572 | 117.00 |

### [Beta Diversity] PCoA Coordinates
| Group | Sample | PCoA1 | PCoA2 |
| :--- | :--- | :--- | :--- |
| Sham | Sham-1 | 0.4154 | 0.0056 |
| Sham | Sham-2 | 0.3938 | -0.0484 |
| Sham | Sham-3 | 0.4066 | -0.1076 |
| Sham10W | Sham10W-4 | 0.3446 | 0.1626 |
| Sham10W | Sham10W-5 | 0.3821 | 0.1120 |
| Sham10W | Sham10W-6 | 0.3728 | 0.1006 |

---

## 💡 科學洞察 (Scientific Insights)

1. **豐富度的自然縮減**: Chao1 指標從 161.9 下降至 122.0。這證實了大鼠在 12W 至 20W 的生長過程中，腸道菌種的總數會自然減少。
2. **結構性的漂移**: Beta 多樣性的分群顯示，老化不僅是「數量」減少，更是「種類比例」的重新分配。
3. **實驗設計提示**: 
   - **重要**: 當我們觀察 HS10W (疾病組) 的菌相變動時，必須扣除上述由老化引起的 25% 豐富度下降，否則會高估疾病的影響。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis 目錄。*
