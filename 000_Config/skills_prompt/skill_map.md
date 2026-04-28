# GCLI_AI agents 完整技能地圖 (Skill Map)

## 🗂️ 000_Orchestrator (總調度)
| Skill | 觸發方式 | 功能描述 |
| :--- | :--- | :--- |
| `/inbox` | 「幫我整理 inbox」 | 全區盤點並產出積壓報告 |
| `/sync` | 「執行同步/收工」 | 調用 `shutdown.py` 進行 Git & GitHub 同步 |
| `/report` | 「進度彙整」 | 總結四域進度，產出日/週報 |

## 🔬 100_Research (研究專精)
| Skill | 觸發方式 | 功能描述 |
| :--- | :--- | :--- |
| `/gap` | 「進行 Gap 分析」 | Mechanism, Translational, Methodology 三軸分析 |
| `/analyze` | 「解讀數據」 | 結果趨勢 -> 脈絡置入 -> 機制推論 (三階論) |
| `/lit-review` | 「寫文獻綜述」 | 產出標準四段式學術摘要 |

## 📧 200_Secretary (秘書行政)
| Skill | 觸發方式 | 功能描述 |
| :--- | :--- | :--- |
| `/email-action` | 「提取信件行動項」 | 從郵件內容自動寫入 `_inbox/tasks.md` |
| `/email-reply` | 「草擬回覆」 | 根據前文與任務狀態生成 Email 草稿 |
| `/calendar` | 「安排行程」 | 檢查衝突並寫入 Google Calendar |

## 🏥 300_Life (生活管理)
| Skill | 觸發方式 | 功能描述 |
| :--- | :--- | :--- |
| `/finance` | 「記錄開支」 | 結構化紀錄財務變動 |
| `/health` | 「健康盤點」 | 彙整醫療、飲食與睡眠數據 |

## 💾 400_Data (數據庫管理)
| Skill | 觸發方式 | 功能描述 |
| :--- | :--- | :--- |
| `/data-archive` | 「數據歸檔」 | 嚴格遵守 DN/UUO 分類邏輯移動檔案 |
