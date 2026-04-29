# MarkItDown 轉譯與提煉規範 (Standalone Skill)

## 🎯 功能描述
將非 Markdown 格式（PDF, XLSX, PPTX, DOCX）轉化為結構化的 Markdown 文件，並自動銜接學術架構提煉。

## 🛠️ 操作流程
1. **路徑確認**：確認目標檔案路徑。
2. **轉譯執行**：調用 `.\venv\Scripts\markitdown <source_file> > <temp_md>`。
3. **結構化提煉**：
   - AI 讀取轉譯內容。
   - 依照 `inbox_process.md` 規範生成「AI 精華層 (GAP/Method/Key Finding)」與「學術五力 (BG/GAP/RQ/METH/CONTRI)」。
4. **存檔定位**：
   - 依照規範命名：`[年份]_[作者]_[關鍵字].md`。
   - Markdown 存入 `400_Data/[分類]/`。
   - 原始檔移入 `./_assets/` 並在 YAML 中標註 `original_file` 路徑。

## 📝 輸出範本
```markdown
---
title: "Full Title of the Paper"
author: "Lead Author et al."
year: 2025
category: "Exosomes"
original_file: "./_assets/original_filename.pdf"
processed_date: 2026-04-29
---
# [年份]_[作者]_[關鍵字]

## 💡 AI 精華層
- **GAP**: ...
- **METH**: ...
- **Key Finding**: ...

## 🔬 學術五力分析
- **BG**: ...
- **GAP**: ...
- **RQ**: ...
- **METH**: ...
- **CONTRI**: ...

---
## 📄 轉譯全文
...
```
