# **DN_GaExo PAS 染色定量分析計畫 (ImageJ 自動化)**

## **1. 分析目標**
利用 ImageJ Macro 自動化計算 **系膜擴張指數 (Mesangial Index %)**，以評估 **GaExo** 對糖尿病腎病變的治療效果。
*   **計算公式**：`Mesangial Index (%) = (PAS 陽性面積 / 腎小球毛細血管叢總面積) * 100`

## **2. 工具說明**
*   **腳本路徑**：`tools/Analyze_PAS_Mesangial.ijm`
*   **技術核心**：
    *   **Colour Deconvolution (H PAS)**：精準分離紫紅色 (PAS) 與藍色 (Nuclei) 信號。
    *   **Manual ROI Selection**：確保僅計算腎小球區域，排除周圍小管干擾。
    *   **Batch Logging**：自動將每張圖的數據紀錄至 CSV 總表，並生成遮罩圖 (Mask) 供 QC 檢查。

## **3. 操作 SOP**
1.  **影像準備**：將拍攝的腎小球影像（400x 放大倍率）放入獨立資料夾（建議每隻鼠 20-30 個腎小球）。
2.  **啟動腳本**：在 ImageJ/Fiji 中選擇 `Plugins -> Macros -> Run...` 並讀取 `Analyze_PAS_Mesangial.ijm`。
3.  **執行分析**：
    *   依照提示圈選 **Glomerular Tuft (毛細血管叢)**。
    *   點擊 OK 後，腳本將自動執行色彩分離、閾值判定與面積計算。
4.  **數據檢查**：檢查 `PAS_Mesangial_Results.csv` 與生成的遮罩圖，確保 Threshold 完整涵蓋紫紅色基質。

## **4. 預期產出**
*   **數據表**：包含每張影像的 `Tuft Area`、`PAS Area` 與 `Mesangial Index (%)`。
*   **Prism 準備**：將 CSV 數據匯入 Prism，進行 `STZ+Vehicle` vs `STZ+GaExo` 的顯著性檢定 (t-test/ANOVA)。

---
*Developed by Senior Research Colleague Agent (Skill: /pas).*
