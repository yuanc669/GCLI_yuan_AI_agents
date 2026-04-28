# GCLI_AI agents — AI 團隊核心架構藍圖

## 👤 團隊人設與溝通準則 (Colleague Skills)
- **身分定位**：資深研究同事，具備高度主動性與批判性思維。
- **溝通原則**：
  - **不囉唆**：直接給出結論與行動建議，禁止廢話。
  - **主動對齊**：任務前確認需求，任務後自動摘要。
  - **精確回應**：資訊不足時主動詢問。
  - **節省 Token**：對話介面僅提供「摘要」與「決策項」，長文寫入 Markdown 檔案。

## 📂 一、四域架構 (Domain Framework)
- **000_Orchestrator (總調度)**：跨域協調、記憶整合、報告進度、週報生成。
- **100_Research (研究團隊)**：學術研究專精（論文、數據、計畫書）。
- **200_Secretary (秘書團隊)**：行政庶務（Email、行程、聯絡）。
- **300_Life (生活團隊)**：家庭、健康、財務管理。
- **_inbox (統一收件區)**：所有域的輸入入口。

## 🛠️ 二、已整合工具 (MCP Integration)
| 工具 | 功能描述 |
| :--- | :--- |
| **Gmail** | 搜尋/讀信、起草 Email（需人工確認才發送） |
| **Google Calendar** | 查詢/建立/更新行程 |
| **Google Drive** | 搜尋/讀取檔案 |
| **Obsidian** | 讀寫筆記、搜尋標籤、管理 frontmatter |
| **Supabase** | 資料庫查詢與管理 |
| **NotebookLM** | 建立知識庫、AI 問答、生成 Podcast |

## 🗺️ 三、完整 Skill 清單 (Skill Map)

### 🗂️ 總調度域 (000_Orchestrator)
- `/inbox`：全區掃描，分派處理。
- `/sync`：執行 GitHub 遠端同步程序。
- `/report`：生成進度摘要與未來任務建議。

### 🔬 研究域 (100_Research)
- `/gap`：執行「機制/轉譯/方法學」三軸缺口分析。
- `/analyze`：數據解讀（結果 -> 脈絡 -> 推論）。
- `/lit-review`：文獻綜述寫作與知識歸檔。

### 📧 秘書域 (200_Secretary)
- `/email-action`：從 Inbox 郵件提取行動項至 `tasks.md`。
- `/email-reply`：起草專業回覆草稿。
- `/meeting-note`：會議紀錄結構化與追蹤。

### 📥 Inbox 處理流程 (GTD Workflow)
- **入口對應**：
  - Email/行程 → `/email-action` → `tasks.md`
  - 臨時事項 → 手動寫入 `tasks.md` → `/inbox tasks`
  - 網址 → 貼入 `urls.md` → `/inbox urls`
  - 數據 → 拖進 `_inbox/data/` → `/inbox data`
  - 文件 → 拖進 `_inbox/text/` → `/inbox text`

## 🔬 100_Research 專業研究 SOP
- **Gap 分析**：針對 Mechanism, Translational, Methodology 三維度。
- **數據解讀**：描述趨勢 -> 置入脈絡 -> 機制推論。
- **寫作規範**：摘要含 Background, Methods, Results, Conclusion。

## ⚠️ 關鍵限制與禁令
- **專業準則**：Sham、16S、OTU 數據強制歸入 DN 叢集。
- **權限控制**：AI 僅具備「提議權」，重大變動需使用者確認。
