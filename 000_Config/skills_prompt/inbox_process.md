# Inbox 處理指令規範 (Internal Skill)

## /inbox 掃描邏輯
1. 讀取 `_inbox/tasks.md` 待處理區。
2. 讀取 `_inbox/urls.md`。
3. 列出 `_inbox/data/` 與 `_inbox/text/` 下的新檔案。
4. 彙整為「積壓摘要報告」。

## /inbox tasks 處理規則
- 識別關鍵字：日期、急件、會議。
- 更新狀態：將確認的條目搬移至「處理中」。

## /inbox data 歸檔規則
- 判斷指標：文件名包含 16S/OTU/Sham -> 建議路徑 `400_Data/DN/`。
- 其他數據 -> 建議路徑 `400_Data/UUO/`。
