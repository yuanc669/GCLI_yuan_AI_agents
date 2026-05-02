# Inbox 處理與自動歸檔規範 (Skill: /inbox)

## 🎯 目標
將 `_inbox/` 中的原始資料自動轉譯、提煉並歸檔至「四域架構」中，實現「丟入即忘」的自動化流程。

## 📂 檔案命名與處置邏輯
1. **檔名規範**：`[年份]_[第一作者]_[標題關鍵字].md` (例如：`2024_Lee_Exosomes_Sepsis.md`)。
2. **Markdown 主筆記**：
   - 專案相關筆記：存於 `100_Research/02_Active/[Project]/`。
   - 一般文獻筆記：存於 `400_Data/[分類]/[規範檔名].md`。
3. **原始檔案歸檔**：
   - **專案數據** (如分析用 XLSX/原始圖)：移入 `100_Research/02_Active/[Project]/01_Raw_Data/`。
   - **一般文獻** (如 PDF)：移入 `400_Data/[分類]/_assets/[原始檔名].[副檔名]`。
4. **Inbox 清空**：處理完成後，`_inbox/` 應保持整潔。

## 📝 內容結構規範 (兩段式提煉)
生成的 Markdown 筆記必須包含以下結構：

### YAML Frontmatter
```yaml
title: "[完整標題]"
author: "[作者全名]"
year: [年份]
category: "[分類]"
original_file: "./_assets/[原始檔名].[副檔名]"
processed_date: 2026-04-29
```

### 第一段：AI 精華層 (Executive Summary)
- **GAP (Research Gap)**: [一句話描述本文想解決的核心缺口]
- **METH (Methodology)**: [關鍵實驗設計或核心方法]
- **Key Finding**: [最重要的核心研究結論]

### 第二段：學術五力分析 (Academic Extraction)
- **BG (Background)**: 研究背景、核心定義、既有理論基準。
- **GAP (Research Gap)**: 現有研究未解決的矛盾、盲點或限制。
- **RQ (Research Question)**: 本文具體想回答的科學/實務問題。
- **METH (Methodology)**: 實驗設計、數據來源、關鍵模型或分析工具。
- **CONTRI (Contribution)**: 理論或實務上的原創點、解決了什麼問題。

### 第三段：全文轉譯 (Original Content)
- [接續 MarkItDown 的完整轉譯內容]

## 🛠️ 執行流程
1. **掃描**：盤點 `_inbox/` 檔案。
2. **提案**：向使用者報告分類與命名建議。
3. **執行**：
   - 使用 `markitdown` 轉譯。
   - 讀取內容並執行「兩段式提煉」。
   - 依照命名規則存檔，建立目錄並移動原始檔至 `_assets/`。
4. **回報**：完成清單。
