# 秘書域 MCP 整合指令規範 (Internal Skill)

## 📧 Gmail 自動化邏輯 (/email-sync)
1. **搜尋範圍**：檢索過去 24 小時內未讀或帶有「待辦」標籤的郵件。
2. **處理流程**：
   - 摘要郵件內容。
   - 提取日期、人名、行動項 (Action Items)。
   - 建議分類：研究 (Research)、秘書 (Secretary)、生活 (Life)。
3. **產出**：將提取的行動項寫入 `_inbox/tasks.md`，並將原文草稿存至 `200_Secretary/drafts/emails/`。

## 📅 Calendar 自動化邏輯 (/calendar-sync)
1. **讀取範圍**：檢索未來 7 天的行程。
2. **衝突檢查**：比對 `_inbox/tasks.md` 中的截止日與 Calendar 現有行程。
3. **更新建議**：若有新任務，提問「是否要將 [任務名] 加入 [日期] 的行程？」。
4. **安全機制**：嚴禁在未經使用者確認的情況下刪除或修改現有行程。
