# AI 團隊 Skill 地圖 (Master Skill Map)

## 🗂️ 總調度域（000_Orchestrator）
| Skill | 觸發方式 | 功能 | 輸出位置 |
| :--- | :--- | :--- | :--- |
| `/inbox` | 「幫我整理 inbox」 | 全區掃描，分派處理 | 對話摘要 |
| `/sync` | 「同步到雲端」 | 執行 Git 同步腳本 | Console |
| `/report` | 「生成週報/日報」 | 彙整進度與下一階段計畫 | `000_Orchestrator/` |
| `/lit-reconstruct` | 「重建知識庫」 | 批量轉化文獻為結構化 T1 卡片 | `100_Research/01_Records/` |

## 🔬 研究域（100_Research）
| Skill | 功能 | 核心規範 |
| :--- | :--- | :--- |
| `/gap` | 缺口分析 | 三軸分析（Mechanism, Translational, Methodology） |
| `/analyze` | 數據解讀 | 三階論 + **Prism 格式化輸出** (Individual values) |
| `/figure-prep` | 論文圖表準備 | 產出 Results 描述、Prism 數據與統計備註 |
| `/multi-omics` | 跨組學整合 | 連結內容物、菌相與生理表型之邏輯鏈 |
| `/microbiome`| 菌叢分析 | 16S rRNA 數據流 (QC, Alpha/Beta Div, LEfSe) |
| `/ihc` | IHC 定量 | ImageJ 色彩分離、陽性面積/強度計算 |
| `/wb` | WB 定量 | 影像背景扣除、Loading Control 正規化 |
| `/skin-pathology`| 皮膚測量 | H&E 表皮厚度 8 點採樣、比例尺換算 |
| `/scoring` | 損傷評分 | 肝/肺/腎/腸公認評分標準執行 |
| `/if-coloc` | IF 共定位 | Cellpose 分割、PCC/Manders 指標計算 |
| `/mt` | MT 纖維化 | 藍色區域 Area Fraction (CVF%) 計算 |
| `/pas` | PAS 染色 | 系膜擴張 (Mesangial Area%) 量化 |
| `/graphify` | 知識圖譜增強 | 使用 GraphRAG 建立專案地圖，優化 Token 並視覺化邏輯鏈 |
| `/lit-review`| 文獻綜述 | 標準格式（BMRC） |

## 📧 秘書域（200_Secretary）
| Skill | 功能 | 流程 |
| :--- | :--- | :--- |
| `/email-sync` | 同步 Gmail | 搜尋未讀/待辦並提取行動項 |
| `/calendar-sync`| 同步行事曆 | 讀取 7 天行程並校對衝突 |
| `/email-action` | 提取行動項 | 寫入 `_inbox/tasks.md` |
| `/email-reply` | 起草郵件 | 寫入 `200_Secretary/drafts/` |
| `/meeting-note` | 會議整理 | 生成 Action Items 表格 |

## 🏥 生活域（300_Life）
| Skill | 功能 | 備註 | 輸出位置 |
| :--- | :--- | :--- | :--- |
| `/travel-plan` | 旅遊規劃 | 行程、預算、行李清單 | `300_Life/records/` |
| `/finance` | 財務追蹤 | 遵守個人分類規範 | `300_Life/records/` |
| `/health` | 健康紀錄 | 數據分析與建議 | `300_Life/records/` |
