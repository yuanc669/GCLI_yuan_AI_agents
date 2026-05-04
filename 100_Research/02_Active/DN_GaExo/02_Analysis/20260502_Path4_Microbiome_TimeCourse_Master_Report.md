# [20260502] Path 4: 小鼠 DN 病程演進 (Time Course) 完整分析報告

> [!IMPORTANT]
> **分析對象**: C57BL/6 小鼠 (Sham, HS2W, HS6W, HS10W)
> **分析核心**: 揭示腸道菌相如何隨腎病惡化（BUN/CRE 上升）同步動態演變。
> **狀態**: [正式版整合報告 - 已修正為小鼠模型]

---

## 📈 一、 多樣性演化軌跡 (Diversity Evolution)

### 1. Alpha 多樣性：從崩潰到固化
![Alpha Plots](20260502_Progression_Alpha_Plot.png)

| 階段 | Chao1 (豐富度) | Shannon (均勻度) |
| :--- | :--- | :--- |
| **Sham** | 161.98 | 3.5756 |
| **HS2W** | 93.40 | 3.4704 |
| **HS6W** | 96.23 | 3.1487 |
| **HS10W** | 96.61 | 3.2673 |
| **P-value (ANOVA)** | **8.8016e-10** | **0.0139** |

- **趨勢**: 豐富度在 HS2W 急劇下降，並在 HS6W/HS10W 階段維持低位。這標誌著疾病誘導的失調具有**不可逆性**。

### 2. Beta 多樣性：動態漂移空間
![Beta PCoA Plot](20260502_Progression_Beta_PCoA_Plot.png)
- **觀察**: 小鼠菌相隨時間沿著 PCoA1 軸發生系統性位移，HS6W 與 HS10W 呈現重疊趨勢，定義了「慢病菌相穩定態」。

---

## 🔬 二、 病程特異性物種動態 (Taxonomic Progression)

![Stacked Bar](20260502_Path4_Progression_Stacked_Bar.png)

### 1. 早期崩潰者 (Early Collapsers)
- **Duncaniella**: HS2W 即發生 90% 以上流失，且後續未見恢復。

### 2. 持續累積者 (Chronic Accumulators)
- **Lepagella**: 隨週數增加呈現階梯式上升，是慢性期最具代表性的菌屬。
- **Kineothrix**: 始終保持高位。

---

## 🌡️ 三、 菌相與病程指標之動態關聯 (Spearman Progression)

![Progression Heatmap](20260502_Path4_Progression_Heatmap.png)

- **關鍵發現**: 
  - **Kineothrix** 與 BUN 的強正相關貫穿全病程。
  - **Lepagella** 與 CRE 的相關性在後期最為顯著。

---

## 💡 整合科學洞察

1. **三階段模型**: 
   - **Phase 1 (Induction)**: 多樣性崩潰，Duncaniella 消失。
   - **Phase 2 (Adaptation)**: 菌相結構重組，機會致病菌開始累積。
   - **Phase 3 (Stability)**: 以 Lepagella 為特徵的病理穩定態，伴隨腎功能衰竭。
2. **GaExo 干預邏輯**: 
   理想的干預應在 HS2W 之前開始，以防止「失調固化」。若在後期干預，則必須展現對 `Lepagella` 的強效抑制力。

---
*本 Master Report 由 AI 同事整合碎片文件生成。原始數據已封存。*
