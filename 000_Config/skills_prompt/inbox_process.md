# Inbox 處理指令規範 (Internal Skill)

## /inbox 掃描與轉譯邏輯
1. **全域盤點**：讀取以下目錄中的所有檔案：
   - `_inbox/` (根目錄暫存)
   - `secondgrain/_inbox/` (Obsidian 內暫存)
   - `secondgrain/Clippings/` (網頁擷取)
2. **自動轉譯 (MarkItDown Integration)**：
   - 偵測檔案後綴：`.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`。
   - **行動**：建議使用 `markitdown` 將其轉為 `.md` 格式，以便 AI 深度閱讀與搜尋。
   - **存放**：轉譯後的 `.md` 檔案優先存入對應領域的 `notes/` 或 `drafts/`。
3. **全域三層路由判定 (Lifecycle Routing)**：
   - **T1：01_Records (原始進件)**
     - 包含網頁剪輯、初步判讀摘要 ➔ 存至 `[域]/01_Records/`。
     - **標籤規範**：`#record` + `#域` + `#專案名(若有)`。
   - **T2：02_Active (進行中事項)**
     - 包含 Skill 產出的計畫、專案管理總表 ➔ 存至 `[域]/02_Active/[專案名稱]/`。
   - **T3：03_Library (永久資產)**
     - 包含結案終稿、正式證明 PDF 之連結 MD ➔ 存至 `[域]/03_Library/`。

4. **特定域歸檔細則 (Data Cluster)**：

   - **🔴 緊急**：IRB/國科會截止日、24h 內會議。
   - **🟡 重要**：論文投稿進度、實驗數據異常。
   - **🟢 一般**：一般郵件回覆、生活記錄。

## /inbox 產出格式
- **積壓報告**：分類列出待處理項。
- **轉譯建議**：列出哪些檔案可被 MarkItDown 處理。
- **行動建議**：提供分派至各域的指令。

## /inbox 歸檔自動化 (Data Cluster)
- 文件名含 16S/OTU/Sham/DN -> 強制歸入 `400_Data/DN/`。
- 其他研究數據 -> 歸入 `400_Data/UUO/`。
