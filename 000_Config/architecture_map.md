# AI 團隊完整工作架構與 Skill 地圖

## 一、四域架構 (Core Domains)
- **000_Orchestrator**: 總調度（跨域協調、記憶整合、進度報告）。
- **100_Research**: 研究團隊（論文、數據分析、計畫書撰寫）。
- **200_Secretary**: 秘書團隊（Email 處理、行程管理、聯絡對接）。
- **300_Life**: 生活團隊（家庭事務、財務規劃、健康管理）。
- **_inbox**: 統一收件區（所有外部輸入的緩衝入口）。

## 二、已整合工具 (MCP Tools)
| 工具 | 功能 | 備註 |
| :--- | :--- | :--- |
| **Gmail** | 搜尋/讀信、建草稿 | 需人工確認才發送 |
| **Google Calendar** | 查詢/建立/更新行程 | 支援時間衝突檢測 |
| **Google Drive** | 搜尋/讀取/分析檔案 | 支援多格式文檔分析 |
| **Obsidian** | 讀寫筆記、標籤管理 | 維護 frontmatter 完整性 |
| **Supabase** | 資料庫查詢與管理 | 結構化數據存儲 |
| **NotebookLM** | 知識庫、AI 問答、Podcast 生成 | 深度文獻綜述工具 |

## 三、完整 Skill 清單 (Skill Map)

### 🗂️ 總調度域 (000_Orchestrator)
- `/inbox`：全區掃描緩衝區，自動分派任務。
- `/sync`：執行 GitHub 遠端同步與自動備份。
- `/report`：跨域整合進度，生成週報/日報。

### 🔬 研究域 (100_Research)
- `/gap`：執行「機制/轉譯/方法學」三軸分析。
- `/analyze`：執行「結果->脈絡->推論」數據解讀。
- `/lit-review`：依據專業 SOP 進行文獻綜述。

### 📧 秘書域 (200_Secretary)
- `/email-action`：提取郵件行動項至 `tasks.md`。
- `/email-reply`：情境式起草回覆郵件。
- `/meeting-note`：將原始記錄轉化為 Action Items。

### 🏥 生活域 (300_Life)
- `/finance`：收支記錄與月度財務分析。
- `/health`：健康指標追蹤與改善建議。
