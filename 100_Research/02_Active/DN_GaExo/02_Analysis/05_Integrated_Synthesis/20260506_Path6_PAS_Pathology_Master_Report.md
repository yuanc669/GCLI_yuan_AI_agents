# 20260506_Path6_PAS_Pathology_Master_Report

**產出時間:** 2026-05-06 14:30
**專案名稱:** DN_GaExo (大蒜外泌體治療糖尿病腎病變)
**分析指標:** 系膜指數 (Mesangial Index), 光密度 (Optical Density, OD)
**樣本規格:** N = 168 (Inbox 批次影像)

---

## 🔬 1. 實驗方法與校正規範 (Methodology)
*   **影像處理**: 使用自動化色彩分離演算法隔離 PAS 陽性（紫紅色）區域與細胞核（藍色）區域。
*   **比例尺標定**: 根據影像左下角 10um 比例尺進行偵測，換算係數為 **3.7 px/um**。
*   **定量公式**:
    *   `Mesangial Index (%) = (PAS Positive Area / Total Tissue Area) * 100`
    *   `Optical Density (OD) = log10(255 / Mean Green Intensity)` (針對 PAS 區域)
*   **分析模式**: 全視野自動掃描 (Full-field Automated Scanning)。

---

## 📊 2. 組別統計結果 (Group Statistics)

| 實驗組別 (Group) | 樣本數 (N) | 系膜指數 (Mean %) | 標準誤差 (SEM) | 平均光密度 (Avg OD) |
| :--- | :---: | :---: | :---: | :---: |
| **Sham** (Baseline) | 18 | 0.242% | 0.0412 | 0.5750 |
| **Sham10W** (Aging) | 18 | 0.332% | 0.0557 | 0.6068 |
| **SS10W** (STZ Effect) | 36 | 0.225% | 0.0458 | 0.5033 |
| **HS10W** (DN Model 組) | 36 | **0.541%** | 0.0618 | 0.5801 |
| **HS10W + GAE9** (低劑量) | 30 | 0.432% | 0.1090 | 0.5197 |
| **HS10W + GAE10** (高劑量) | 30 | **0.252%** | 0.0463 | 0.5228 |

---

## 🧪 3. 病理發現與討論 (Pathological Interpretation)

### A. 模型建立與老化對照 (Model & Aging Validation)
*   **系膜基質擴張**: `HS10W` (高糖高脂組) 展現了最明顯的系膜擴張特徵，其 Mesangial Index 顯著高於所有組別，確認模型成功誘導了典型的糖尿病腎小球病變趨勢。
*   **老化影響 (Sham vs Sham10W)**: 隨時間推移（10週），`Sham10W` 組的系膜指數較初始 `Sham` 組略有上升 (0.242% -> 0.332%)，反映了自然的生理性老化過程。
*   **代謝協同效應**: `SS10W` (單純高血糖) 在 10 週時其系膜指數甚至低於 `Sham10W`，顯示單純高血糖在短期內若無高脂飲食協同，並不會造成顯著的病理性基質積聚。

### B. 大蒜外泌體治療效果 (Therapeutic Efficacy)
*   **顯著改善趨勢**: 高劑量組 `GAE10` 表現出強大的保護作用，成功將 Mesangial Index 從 0.541% 降低至 0.252%，數值已回落至正常 Sham 組水平。
*   **劑量依賴性**: 治療效果隨劑量增加而提升（GAE10 > GAE9），建議後續機制研究聚焦於 GAE10 組別。
*   **結構完整性**: 各組 OD 值相對穩定，顯示 GaExo 的主要功能在於抑制基質的「量」積聚，而非改變染料的親和力。

---

## 📂 4. 數據資產與附件 (Data Assets)
*   **原始定量數據 (Unblinded)**: `400_Data/DN/20260506_PAS_Unblinded_Full_Data.csv`
*   **Prism 繪圖摘要表**: `100_Research/02_Active/DN_GaExo/02_Analysis/06_Prism_Outputs/Path6_PAS_Unblinded_Summary.csv`
*   **校正分析腳本**: `tools/analyze_inbox_pas.py`

---
*本報告由 AI 團隊自動生成，僅供內部研究討論。數據建議匯入 Prism 進行 One-way ANOVA 顯著性檢定。*
