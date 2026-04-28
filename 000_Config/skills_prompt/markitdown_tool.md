# MarkItDown 轉譯指令規範 (Standalone Skill)

## 🎯 功能描述
將非 Markdown 格式（PDF, XLSX, PPTX, DOCX）轉化為結構化的 Markdown 文件，以便 AI 進行深度分析、檢索或寫入 Obsidian。

## 🛠️ 操作流程
1. **路徑確認**：確認目標檔案路徑。
2. **轉譯執行**：調用虛擬環境中的 `markitdown` 工具。
   - 命令格式：`.\venv\Scripts\markitdown <source_file> > <destination_md>`
3. **後續處理**：
   - 如果是 Excel，轉譯後應檢查表格結構。
   - 如果是 PDF，轉譯後應清理可能的排版亂碼。
4. **存檔定位**：
   - 預設存入原檔案所在目錄，或依據 /inbox 規則歸位至 `100_Research/notes/`。

## ⌨️ 觸發範例
- 「幫我把這個 PDF 轉成 md」
- 「使用 markitdown 處理 inbox 中的所有文件」
