# DN_GaExo 專案工作筆記 (Working Notes)

## 🧪 實驗模型與組別定義 (Experimental Model & Groups)

### 1. 誘導與處理 (Induction & Treatment)
*   **DN 誘導模型**: 高脂飲食 (HFD) + 鏈佐黴素 (STZ) 聯合誘導。
*   **實驗組別**:
    *   **Sham**: 正常飲食 (12W 犧牲)。
    *   **Sham10W**: 正常飲食 (20W 犧牲)，建立老化/時間對照基準。
    *   **HS2W**: HFD+STZ 誘導後 2 週 (14W 犧牲)。
    *   **HS6W**: HFD+STZ 誘導後 6 週 (18W 犧牲)。
    *   **HS10W**: HFD+STZ 誘導後 10 週 (22W 犧牲)，代表末期 DN 狀態。
    *   **SS10W**: 單純 STZ 誘導 (10週)。
    *   **HFD10W**: 單純 HFD 誘導 (10週)。
    *   **HS10WGaE9**: DN 狀態 + 大蒜外泌體劑量 9 (低劑量)。
    *   **HS10WGaE10**: DN 狀態 + 大蒜外泌體劑量 10 (高劑量)。

### 2. 七大分析路徑 (Seven Analysis Paths)
1.  **老化基準 (Aging Base)**: Sham vs. Sham10W (12W vs. 20W)。
2.  **急性誘導 (Acute Induction)**: Sham vs. HS2W。
3.  **DN 定型 (DN Establishment)**: Sham10W vs. HS10W。
4.  **病程進展 (Disease Progression)**: Sham, HS2W, HS6W, HS10W。
5.  **驅動拆解 (Driver Dissection)**: Sham10W, SS10W, HFD10W, HS10W (釐清 HFD 與 STZ 各自貢獻)。
6.  **藥效評估 (Efficacy Evaluation)**: Sham10W, HS10W, HS10WGaE9, HS10WGaE10 (核心治療路徑)。
7.  **全景整合 (Global Integration)**: Sham10W, SS10W, HFD10W, HS10W, HS10WGaE9, HS10WGaE10 (全景視角)。

---

## 📅 2026-05-04 數據分析進度：大蒜外泌體 (GaExo) 多組學整合

### 1. 核心定義修正 (Important Correction)
*   **GaExo**：大蒜外泌體 (Garlic-derived Exosomes / Nanovesicles)，學名來源為 *Allium sativum*。
*   **關鍵成分**：大蒜來源 miRNAs (如 miR-1260a 類似物)、Myrosinase (黑芥子酶) 以及潛在的有機硫化合物。

### 2. 菌相分析進度：Path1 (Aging Analysis) 深度解讀
*   **分析對象**：比較 Sham 12W (早期) vs. Sham 20W (晚期/Sham10W)。
*   **核心結論**：
    *   **生理老化標記**：識別出 *Spongiimonas* 消失與 *Bacteroides acidifaciens* 下降為自然老化特徵。
    *   **大蒜外泌體療效判定**：核心療效菌 **_Kineothrix_** 在老化過程中雖有變動，但 GaExo 的誘導幅度具有病理特異性。
    *   **抗老化潛力**：GaExo 對老化受損菌（如 *Lactobacillus*）的救回作用，是大蒜外泌體具備「重塑年輕態菌相」潛力的證據。

### 3. 病程動態與藥理邏輯
*   **Path 2 (Acute)**：高糖高脂引發 *Duncaniella* 快速崩解，並誘導早期病理菌 *Romboutsia_B*。
*   **GaExo 介入策略**：利用大蒜外泌體中的 Myrosinase 與 *Allium* miRNA 調節腸道環境，特異性強化保護性菌屬（如 *Kineothrix*），進而降低 BUN 並改善腎損傷。

### 4. 分析檔案目錄優化 (Directory Reorganization)
*   **位置**：`100_Research/02_Active/DN_GaExo/02_Analysis/`
*   **分類邏輯**：
    *   `01_Microbiome/`：腸道菌叢 (16S) 所有 Path 1-7 的分析報告與視覺化圖表。
    *   `02_Physiology_Biochem/`：體重 (Body Weight) 與生化指標 (Biochemistry) 分析。
    *   `03_Pathology/`：病理損傷評分 (Pathology Scoring) 數據與模板。
    *   `04_GaNV_Characterization/`：大蒜外泌體表徵分析（蛋白質組、miRNA、穩定性、功能性）。
    *   `05_Integrated_Synthesis/`：跨組學整合、驗證協議與結果草稿。

---
*記錄者：Gemini CLI (Senior Research Colleague)*
