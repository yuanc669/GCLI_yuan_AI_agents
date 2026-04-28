    1 ---
    2 source: https://gemini.google.com/u/1/app/8d1a62988b3f6604?utm_source=app_launcher&utm_medium=owned&utm_campaign=base_all
    3 captured_at: 2026-04-28T16:29:58+08:00
    4 tags: #inbox/clipper
    5 status: unread
    6 ---
    7
    8 # ‎Google Gemini
    9
   10 Obsidian 外掛推薦：醫學研究者

## 和 Gemini 的對話

你說了

obsidian外掛建議?

## Gemini 說了

針對您的需求與專業背景，我將 Obsidian 的外掛建議分為 **學術研究、AI 自動化、工作流程優化** 三大類。

考慮到您身為醫學研究員且有執行 AI 專案（如大蒜外泌體研究）的需求，以下是 2026 年最推薦的配置：

---

## 一、 學術與文獻研究類（核心必備）

這組外掛能幫助您處理大量的文獻資料與蛋白質體學等研究數據。

- **Zotero Integration / Citations** ：
	- **用途** ：將 Zotero 中的文獻與 PDF 標註直接同步到 Obsidian。
		- **醫學應用** ：在撰寫研究計畫或論文時，能快速引用文獻並自動生成對應的 Literature Note。
- **Dataview** ：
	- **用途** ：Obsidian 的「大腦」，能用類似資料庫的語法搜尋筆記。
		- **研究應用** ：您可以建立一個儀表板，自動列出所有標記為 `status: 實驗中` 或 `tag: #exosomes` 的筆記。
- **PDF++** ：
	- **用途** ：大幅強化 Obsidian 內建的 PDF 閱讀功能，支援深層連結（Deep Link）。
		- **優點** ：您可以直接從 PDF 的某個圖表（如大蒜外泌體的電性分析圖）連到筆記中，點擊連結即跳回 PDF 該頁面。

---

## 二、 AI 整合與自動化（專業進階）

針對您對本地模型（如 Gemma-4）及量化分析的興趣。

- **Smart Connections** ：
	- **用途** ：利用向量嵌入（Embeddings）技術，自動找出您筆記中相關聯的內容。
		- **情境** ：當您在寫「腸道生態系統」時，它會自動側欄提示您半年前寫過的「DKD 病理機制」相關筆記，幫助跨學科聯想。
- **Text Generator / Copilot** ：
	- **用途** ：直接在筆記中調用 LLM（可串接您本地運行的 API）。
		- **應用** ：幫助您快速摘要學術論文、生成 Xscript 腳本雛形或翻譯複雜的醫學名詞。
- **Templater** ：
	- **用途** ：比內建模板更強大，支援 JavaScript 腳本。
		- **自動化** ：您可以設定「新建專案」模板，一鍵自動建立包含專案層級（Level 1-3）的資料夾結構與 Meta Data。

---

## 三、 工作與生活管理（效率提升）

- **Periodic Notes (日/週/月誌)** ：
	- **用途** ：管理您的研究日誌。
		- **搭配** ：配合 **Calendar** 外掛，視覺化您的實驗進度與會議紀錄。
- **Kanban** ：
	- **用途** ：將筆記看板化。
		- **應用** ：非常適合管理「論文投稿進度」或「AI 團隊分工」。
- **Excalidraw** ：
	- **用途** ：在筆記內直接繪製手繪風格的流程圖或心智圖。
		- **研究應用** ：構思外泌體作用機轉（如 Gut-Kidney Axis）的示意圖時非常直覺。

---

### 💡 給醫學研究員的特別建議

由於您提到正在處理 **DKD-Garlic-Exo-Project** 這種多層級專案，強烈建議安裝 **QuickAdd** 。它可以設定自動化的「捕獲（Capture）」流程，例如：

1. 建立一個命令「新增實驗紀錄」。
2. 執行時自動詢問「樣本編號」與「觀察結果」。
3. 自動將內容存入 `[02_Microbiome]` 的正確資料夾中，並打上當天日期。

如果您想更深入了解如何將 **Gemma-4** 與這些外掛串接，或者如何用 **Dataview** 管理您的股票代碼數據，歡迎再告訴我！

Gemini 是 AI，有時可能會出錯。