# DN_GaExo Project Constitution (大蒜外泌體專案執行準則)

## 🎯 專案核心目標
驗證大蒜外泌體 (GaExo) 對糖尿病腎病變 (DN) 的治療潛力，並透過 7 大路徑 (Path 1~7) 釐清腸道菌叢與生理表型之關聯。

## 📂 目錄結構規範
- `01_Raw_Data/`: 依 Microbiome, Physiology, Proteomics, Pathology 分類。
- `02_Analysis/`: 
  - `05_Integrated_Synthesis/`: 存放跨領域總結報告 (Master Reports)。
  - `06_Prism_Outputs/`: 存放 Path 1~7 的專屬分析圖表與 CSV。
- `03_Figures_Tables/`: 存放 Figure 1~7 的最終發表級圖表。

## 🔬 數據分析準則 (Analysis Rules)
1. **Path 1~7 命名強制化**：所有數據導出與圖表名稱必須包含路徑編號（例如 `Path6_Therapy_BUN_Plot`）。
2. **菌相分析層級**：預設分析 L7 (Species) 層級，並與生理指標執行 Spearman 相關性分析。
3. **生化指標集**：固定監測 BUN, CRE, AC, TG, BodyWeight。
4. **病理評分**：採用 RPS (Renal Pathology Scoring) 系統。

## ✍️ 產出規範
- **報告語言**：繁體中文為主，專業術語使用英文。
- **圖表格式**：提供 Prism-ready CSV 以便手動繪圖，並附帶 Python 生成的 PNG 預覽圖。
