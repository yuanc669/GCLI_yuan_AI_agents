# 20260504_ShareX 快捷鍵註冊失敗分析
**時間**：2026-05-04 09:03
**分類**：#100_Research (系統報錯診斷)

## 影像存檔
![[images/20260504_ShareX_Hotkey_Error.png]]

## AI 分析結果
### 🔍 問題描述
截圖顯示 ShareX 快捷鍵註冊失敗視窗。

### 📄 提取訊息
- **衝突快捷鍵**：
  - `Ctrl + Print Screen` (擷取區域)
  - `Alt + Print Screen` (擷取目前視窗)
- **建議動作**：選擇其他快捷鍵，或關閉衝突程式。

### 💡 診斷建議
1. **衝突來源**：通常為 OneDrive 或 Windows 11 內建的「擷取工具」。
2. **解決方案**：
   - 進入 ShareX 的 `Hotkey settings` 修改為自訂組合鍵。
   - 關閉 OneDrive 設定中的「自動儲存螢幕擷取畫面」。
