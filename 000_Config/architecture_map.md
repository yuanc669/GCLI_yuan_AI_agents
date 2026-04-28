# AI 團隊完整架構與 Skill 地圖

## 一、四域架構 (Core Domains)
- **000_Orchestrator**: 總調度。負責跨域協調、長期記憶、週報與進度追蹤。
- **100_Research**: 研究團隊。負責論文分析、數據解讀、計畫書撰寫。
- **200_Secretary**: 秘書團隊。負責 Email 起草、行程管理、會議記錄。
- **300_Life**: 生活團隊。負責家庭事務、財務規劃、健康追蹤。
- **_inbox**: 統一入口。所有外部輸入的緩衝與分流區。

## 二、已整合工具 (MCP Tools)
| 工具 | 功能 | 備註 |
| :--- | :--- | :--- |
| **Gmail** | 搜尋/讀信、建草稿 | 需人工確認才發送 |
| **Google Calendar** | 查詢/建立/更新行程 | |
| **Google Drive** | 搜尋/讀取檔案 | |
| **Obsidian** | 讀寫筆記、標籤管理 | 維護 `secondgrain/` |
| **Supabase** | 資料庫查詢與管理 | |
| **NotebookLM** | 知識庫問答、Podcast 生成 | |

## 三、完整 Skill 清單

### 🗂️ 總調度域 (000_Orchestrator)
- **Skill**: `/inbox`
  - **觸發**: 「幫我整理 inbox」
  - **功能**: 全區掃描盤點，分派處理建議。
- **Skill**: `/sync`
  - **觸發**: 「收工同步」
  - **功能**: 執行 `tools/shutdown.py` 進行 Git 推送。

### 🔬 研究域 (100_Research)
- **Skill**: `/gap`
  - **觸發**: 「分析研究缺口」
  - **功能**: 執行機制/轉譯/方法學三軸分析。
- **Skill**: `/analyze`
  - **觸發**: 「解讀這份數據」
  - **功能**: 執行結果->脈絡->推論三階解讀。

### 📧 秘書域 (200_Secretary)
- **Skill**: `/email-action`
  - **觸發**: 「處理這封郵件」
  - **功能**: 提取待辦事項至 `tasks.md`。
- **Skill**: `/email-reply`
  - **觸發**: 「幫我回信」
  - **功能**: 自動根據上下文起草回覆。

### 🏥 生活域 (300_Life)
- **Skill**: `/finance` / `/health`
  - **功能**: 記錄並提供結構化建議。
