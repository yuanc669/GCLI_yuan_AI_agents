# AI 團隊 Skill 地圖 (Master Skill Map)

## 🗂️ 總調度域（000_Orchestrator）
| Skill | 觸發方式 | 功能 | 輸出位置 |
| :--- | :--- | :--- | :--- |
| `/inbox` | 「幫我整理 inbox」 | 全區掃描，分派處理 | 對話摘要 |
| `/sync` | 「同步到雲端」 | 執行 Git 同步腳本 | Console |
| `/report` | 「生成週報/日報」 | 彙整進度與下一階段計畫 | `000_Orchestrator/` |

## 🔬 研究域（100_Research）
| Skill | 功能 | 核心規範 |
| :--- | :--- | :--- |
| `/gap` | 缺口分析 | 三軸分析（Mechanism, Translational, Methodology） |
| `/analyze` | 數據解讀 | 三階論（結果 -> 脈絡 -> 解讀） |
| `/lit-review`| 文獻綜述 | 標準格式（BMRC） |

## 📧 秘書域（200_Secretary）
| Skill | 功能 | 流程 |
| :--- | :--- | :--- |
| `/email-action` | 提取行動項 | 寫入 `_inbox/tasks.md` |
| `/email-reply` | 起草郵件 | 寫入 `200_Secretary/drafts/` |
| `/meeting-note` | 會議整理 | 生成 Action Items 表格 |

## 🏥 生活域（300_Life）
| Skill | 功能 | 備註 |
| :--- | :--- | :--- |
| `/finance` | 財務追蹤 | 遵守個人分類規範 |
| `/health` | 健康紀錄 | 數據分析與建議 |
