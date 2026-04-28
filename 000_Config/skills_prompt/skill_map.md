# AI 團隊技能地圖 (Master Skill Map)

## 一、四域架構 (Core Domains)
- **000_Orchestrator**：總調度（跨域協調、記憶整合、進度報告）。
- **100_Research**：研究團隊（學術論文、實驗數據、計畫書撰寫）。
- **200_Secretary**：秘書團隊（Email 處理、行程管理、會議記錄）。
- **300_Life**：生活團隊（家庭庶務、財務管理、健康追蹤）。
- **_inbox**：統一收件區。

## 二、MCP 工具整合表
| 工具 | 功能 | 狀態 |
| :--- | :--- | :--- |
| **Gmail** | 搜尋/讀信、建草稿（需人工確認） | 整合預備 |
| **Google Calendar** | 查詢/建立/更新行程 | 整合預備 |
| **Google Drive** | 搜尋/讀取雲端檔案 | 已連線 (透過 GCLI) |
| **Obsidian** | 讀寫筆記、管理 Frontmatter | 已連線 (G:/我的雲端硬碟/...) |
| **Supabase** | 資料庫查詢與管理 | 待配置 |
| **NotebookLM** | 知識庫建立、AI 問答、Podcast 生成 | 已連線 (MCP Server) |

## 三、Skill 指令清單

### 🗂️ 總調度域 (000_Orchestrator)
- `/inbox`：全區掃描，分派處理。
- `/sync`：執行 `tools/shutdown.py` 同步 GitHub。
- `/report`：日/週報生成。

### 🔬 研究域 (100_Research)
- `/gap`：三軸缺口分析 (Mechanism/Translational/Methodology)。
- `/analyze`：三階數據解讀 (結果 -> 脈絡 -> 推論)。
- `/lit-review`：標準學術綜述撰寫。

### 📧 秘書域 (200_Secretary)
- `/email-action`：提取郵件行動項至 `tasks.md`。
- `/email-reply`：起草回覆。
- `/meeting-note`：結構化會議記錄。

### 🏥 生活域 (300_Life)
- `/finance`：收支記錄與分析。
- `/health`：健康數據追蹤。
