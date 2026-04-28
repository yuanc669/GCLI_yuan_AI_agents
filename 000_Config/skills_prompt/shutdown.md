---
name: shutdown
description: 收工同步助手。當使用者說「收工」、「/sync」、「準備換電腦」或任何結束工作請求時，執行此技能。本技能會更新 Obsidian 工作筆記並執行 Git 同步。
---

# 收工同步助手 (/sync)

對話結束前，將研究進度與決策完整保存至三個核心節點：
- **GDrive**：檔案自動同步。
- **Obsidian 工作筆記**：更新 `secondgrain/GCLI_yuan_AI_agents/工作筆記.md`。
- **GitHub**：將變更推送到 `yuanc669/GCLI_yuan_AI_agents` (master 分支)。

## 收工 SOP（依序執行）

### 步驟 1：產出「資深同事」摘要
從對話歷史中提取關鍵點：
- **完成事項**：本節課完成的檔案修改、架構調整。
- **核心決策**：例如工具替換 (Firebase)、技能整合 (ai-research-skills)。
- **待辦事項**：下一次啟動時的首要任務。

### 步驟 2：定位工作目錄與筆記
- **工作目錄**：`G:\我的雲端硬碟\GCLI_yuan_AI agents`
- **Obsidian 筆記**：`secondgrain/GCLI_yuan_AI_agents/工作筆記.md`

### 步驟 3：更新 Obsidian 工作筆記
依照 `工作筆記.md` 的結構進行「精確修改」：
- **⏯️ 上次做到哪**：更新「最後動作」與「所在 repo」資訊。
- **🗓️ 最近更動紀錄**：在表格底部新增一行：`| <今天日期> | <摘要> | ✅ | ✅ | ✅ |`。
- **🕳️ 踩坑筆記**：若本節對話有解決技術問題，將其記錄下來。

### 步驟 4：Git commit + push
```powershell
git add .
git commit -m "[Session Sync] <摘要撰寫：動詞+對象>"
git push origin master
```
*注意：在 Windows 環境下，確保 git 指令不被環境變數干擾。*

### 步驟 5：報告同步狀態
使用以下三勾表格回報：

| 平台 | 變動內容 | 狀態 |
| :--- | :--- | :--- |
| **GDrive** | 雲端檔案同步 | ✅ (Auto) |
| **Obsidian** | 更新工作筆記 | ✅ |
| **GitHub** | Push 至 master | ✅ |

## 嚴格禁令
- ❌ **禁止空轉**：若本次對話僅為問答而無任何檔案變動，則跳過同步並告知使用者。
- ❌ **禁止冗長 commit**：commit message 必須簡潔（例如：`feat: 整合 ai-research-skills`）。
- ❌ **禁止忽略筆記**：必須先更新 Obsidian 筆記，再執行 Git Push。
