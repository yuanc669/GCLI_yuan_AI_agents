```
# 進入 Google Drive 目錄並建立根目錄
cd "G:/我的雲端硬碟/"
mkdir "GCLI_yuan_AI agents"
cd "GCLI_yuan_AI agents"

# 建立四域架構與配置資料夾
mkdir _inbox _inbox/data _inbox/text tools
mkdir 000_Config 000_Config/skills_prompt
mkdir 000_Orchestrator 000_Orchestrator/daily 000_Orchestrator/weekly
mkdir 100_Research 100_Research/drafts 100_Research/notes 100_Research/materials
mkdir 200_Secretary 200_Secretary/drafts 200_Secretary/meetings
mkdir 300_Life 300_Life/records
mkdir 400_Data 400_Data/DN 400_Data/UUO

# 建立初始控制文件
touch _inbox/tasks.md _inbox/urls.md
```   
YOUR_GEMINI_API_KEY_HERE

```
GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE
APP_ID=ai-team-core-001
ROOT_PATH="G:/我的雲端硬碟/GCLI_AI agents"
OBSIDIAN_VAULT_PATH="你的_Obsidian_Vault_G:\我的雲端硬碟\GCLI_yuan_AI agents\secondgrain"
```


```
git init
git config windows.appendAtomically false

# 建立 .gitignore
cat <<EOF > .gitignore
venv/
.env
000_Config/.env
__pycache__/
.DS_Store
# Google Drive 系統檔
Icon?
.tmp.*
~$*
EOF

git add .
git commit -m "Initial commit: 整合學術研究與同事協作技能之 AI 團隊"
```


```
import os
import subprocess
from datetime import datetime

def run_cmd(cmd):
    subprocess.run(cmd, shell=True, check=True)

def shutdown_routine():
    print("🚀 同事，我正在幫你進行收工同步程序...")
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        run_cmd("git config windows.appendAtomically false")
        run_cmd("git add .")
        run_cmd(f'git commit -m "AI 團隊自動存檔: {today} (同步研究指令與筆記)"')
        run_cmd("git push origin main")
        print("✅ GitHub 遠端同步完成。明天見！")
    except Exception as e:
        print(f"❌ 同事，Git 同步遇到了點問題: {e}")

if __name__ == "__main__":
    shutdown_routine()
```


增加Inbox

 Inbox 處理流程
         
  整體架構
                                                                                           有東西要記錄/處理
          ↓                                                                              
      丟進 _inbox/
          ↓
      說「/inbox」
          ↓
     AI 掃描 + 分類
          ↓
     確認後執行或歸檔

  ---
  五個入口對應不同內容

  ┌──────────────────────┬────────────────────────────┬─────────────────────┐
  │      丟什麼進來      │           放哪裡           │      處理指令       │
  ├──────────────────────┼────────────────────────────┼─────────────────────┤
  │ Email 行程/截止/待辦 │ 直接說 /email-action       │ → 自動寫入 tasks.md │
  ├──────────────────────┼────────────────────────────┼─────────────────────┤
  │ 臨時交代事項         │ 手動寫入 tasks.md 待處理區 │ /inbox tasks        │
  ├──────────────────────┼────────────────────────────┼─────────────────────┤
  │ 要記錄的網址         │ 貼入 urls.md               │ /inbox urls         │
  ├──────────────────────┼────────────────────────────┼─────────────────────┤
  │ 實驗數據（xlsx/csv） │ 拖進 _inbox/data/          │ /inbox data         │
  ├──────────────────────┼────────────────────────────┼─────────────────────┤
  │ 文件/論文/筆記       │ 拖進 _inbox/text/          │ /inbox text         │
  └──────────────────────┴────────────────────────────┴─────────────────────┘

  ---
  標準處理流程（每次 session）

  Step 1   /inbox          → 看全區積壓數量
  Step 2   /inbox tasks    → 更新 AI 判斷，確認急件
  Step 3   /inbox urls     → 分類網址，確認後寫入對應位置
  Step 4   /inbox data     → 提歸檔建議（AI 先問確認再移動）
  Step 5   /inbox text     → 同上

  ---
  任務三種狀態流轉

  待處理  →（AI 判斷 + 你確認）→  處理中  →（完成）→  已完成

  tasks.md 三個表格對應這三個狀態，AI 負責搬移條目。

  ---
  關鍵規則（已內建進 SKILL）

  - 任何檔案移動前必須先提建議，等你確認才執行
  - Sham、16S、OTU 相關數據 → 歸 DN（糖尿病腎病變），不是 UUO
  - Email 到 inbox 的標準路徑：先 /email-action 抓出行動項，再 /email-reply 起草回覆     
  - 對話只給摘要，完整內容寫檔案，不浪費 context

  ---
  Skill 地圖

  /email-action  ──→  tasks.md
  /email-reply   ──→  drafts/emails/
  /inbox tasks   ──→  逐項 AI 判斷 + 移至處理中/已完成
  /inbox urls    ──→  移至 contacts/ 或 research-clusters/
  /inbox data    ──→  移至 400_Data/{疾病}/
  /inbox text    ──→  移至 drafts/ 或 notes/
  /inbox         ──→  全區掃描（以上所有的入口）





MCP確認
並將Supabase修改為使用Firebase  不留Supabase


上傳至guthub
 目前尚未設定遠端儲存庫。請提供您的 GitHub 儲存庫 URL（例如
  https://github.com/yuanc669/GCLI_yuan_AI_agents.git），我將為您完成連結與上傳作業。


  完整工作架構與 Skill 地圖     
                                                                                           一、四域架構                                                                                                                                                                    
  AI agents/                                                                             
  ├── 000_Orchestrator/   ← 總調度（跨域協調、記憶、週報）
  ├── 100_Research/       ← 研究團隊（論文、數據、計畫書）
  ├── 200_Secretary/      ← 秘書團隊（Email、行程、聯絡）
  ├── 300_Life/           ← 生活團隊（家庭、財務、健康）
  └── _inbox/             ← 統一收件區（所有域的輸入入口）
---
  二、已整合工具（MCP）

  ┌─────────────────┬───────────────────────────────────────┐
  │      工具       │               能做什麼                │
  ├─────────────────┼───────────────────────────────────────┤
  │ Gmail           │ 搜尋/讀信、建草稿（需人工確認才發送） │
  ├─────────────────┼───────────────────────────────────────┤
  │ Google Calendar │ 查詢/建立/更新行程                    │
  ├─────────────────┼───────────────────────────────────────┤
  │ Google Drive    │ 搜尋/讀取檔案                         │
  ├─────────────────┼───────────────────────────────────────┤
  │ Obsidian        │ 讀寫筆記、搜尋標籤、管理 frontmatter  │
  ├─────────────────┼───────────────────────────────────────┤
  │ Firebase        │ 資料庫查詢與管理                      │
  ├─────────────────┼───────────────────────────────────────┤
  │ NotebookLM      │ 建立知識庫、AI 問答、生成 Podcast     │
  └─────────────────┴───────────────────────────────────────┘

  ---
  三、完整 Skill 清單

  🗂️ 總調度域（000_Orchestrator）

  ┌────────────────┬────────────────────────────┬────────────────────────────┐
  │     Skill      │          觸發方式          │            功能            │
  ├────────────────┼────────────────────────────┼────────────────────────────┤
  │ /inbox         │ 「幫我整理 inbox」         │ 全區掃描，分派處理         │
  ├────────────────┼────────────────────────────┼────────────────────────────┤
  │ /weekly-review │ 「本週回顧」「幫我做週報」 │ 掃描本週所有記錄產出週報   │
  ├────────────────┼────────────────────────────┼────────────────────────────┤
  │ /brainstorm    │ 「我有個想法」             │ 引導式問答把想法轉為計畫書 │
  ├────────────────┼────────────────────────────┼────────────────────────────┤
  │ /skill-creator │ 「幫我建一個 skill」       │ 建立/修改/測試 skill       │
  └────────────────┴────────────────────────────┴────────────────────────────┘

  🔬 研究域（100_Research）

  ┌──────────────────┬────────────────────────────────┬──────────────────────────────┐   
  │      Skill       │            觸發方式            │             功能             │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /data-interpret  │ 「幫我解讀數據」「這個結果怎麼 │ 解讀實驗數據、產出結果段落   │   
  │                  │ 看」                           │                              │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /literature-gap  │ 「幫我找研究缺口」「這篇論文的 │ 三軸缺口分析（機制/轉譯/方法 │   
  │                  │  gap」                         │ 學）                         │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /abstract        │ 「幫我寫摘要」                 │ 論文摘要撰寫                 │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /discussion      │ 「幫我寫討論」                 │ Discussion 段落撰寫          │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /experiment-desi │ 「幫我設計實驗」               │ 實驗方案設計                 │   
  │ gn               │                                │                              │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /figure-prep     │ 「幫我準備圖」                 │ 論文圖表整理與說明           │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /grant-writing   │ 「幫我寫計畫書」               │ 國科會/IRB 計畫書撰寫        │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /paper-review    │ 「幫我審這篇論文」             │ 論文審稿意見產出             │   
  ├──────────────────┼────────────────────────────────┼──────────────────────────────┤   
  │ /irb-checklist   │ 「IRB 要準備哪些」             │ IRB 申請文件確認清單         │   
  └──────────────────┴────────────────────────────────┴──────────────────────────────┘   

  📮 秘書域（200_Secretary）

  ┌───────────────┬──────────────────────────────┬───────────────────────────────────┐   
  │     Skill     │           觸發方式           │               功能                │   
  ├───────────────┼──────────────────────────────┼───────────────────────────────────┤   
  │ /email-action │ 「這封信有什麼要做的」       │ Email → 行程/截止/待辦寫入        │   
  │               │                              │ tasks.md                          │   
  ├───────────────┼──────────────────────────────┼───────────────────────────────────┤   
  │ /email-reply  │ 「幫我回信」「草擬一封       │ 信件代擬，草稿存入 drafts/emails/ │   
  │               │ email」                      │                                   │   
  ├───────────────┼──────────────────────────────┼───────────────────────────────────┤   
  │ /meeting-note │ 「幫我整理會議記錄」         │ 會議記錄整理與行動追蹤            │   
  └───────────────┴──────────────────────────────┴───────────────────────────────────┘   

  ---
  四、任務路由規則

  收到指令
      ↓
  含「論文/數據/分析/計畫書/文獻/實驗」 → 研究域
  含「Email/信件/行程/會議/截止日」     → 秘書域
  含「家庭/健康/財務/生活」              → 生活域
  跨兩個以上域                           → 先告知影響範圍再分派

  優先度衝突： IRB/國科會截止 > 論文投稿 > 一般回覆 > 其他

  ---
  五、標準工作流程

  Email 進來
     ↓ /email-action      → tasks.md（行程/截止/待辦）
     ↓ /email-reply       → drafts/emails/（草稿）

  新資料/文件進來
     ↓ 丟進 _inbox/
     ↓ /inbox             → 掃描 + 分類歸檔

  研究推進
     ↓ /literature-gap    → 找缺口
     ↓ /experiment-design → 設計實驗
     ↓ /data-interpret    → 解讀結果
     ↓ /abstract /discussion → 寫論文段落

  每週整合
     ↓ /weekly-review     → 完成/未完成/決策/下週計畫

  ---
  六、輸出位置對照

  ┌────────────────────┬────────────────────────────────────┐
  │       產出物       │              存放位置              │
  ├────────────────────┼────────────────────────────────────┤
  │ 論文/計畫書段落    │ 100_Research/drafts/papers/        │
  ├────────────────────┼────────────────────────────────────┤
  │ 實驗想法/缺口分析  │ 100_Research/notes/ideas/          │
  ├────────────────────┼────────────────────────────────────┤
  │ Email 草稿         │ 200_Secretary/drafts/emails/       │
  ├────────────────────┼────────────────────────────────────┤
  │ 行程/待辦          │ _inbox/tasks.md                    │
  ├────────────────────┼────────────────────────────────────┤
  │ 週報               │ 000_Orchestrator/weekly/           │
  ├────────────────────┼────────────────────────────────────┤
  │ 每日記錄           │ 000_Orchestrator/daily/            │
  ├────────────────────┼────────────────────────────────────┤
  │ 實驗數據（歸檔後） │ 400_Data/{疾病}/raw/ 或 processed/ │
  └────────────────────┴────────────────────────────────────┘





https://github.com/yuanc669/ai-research-skills
https://github.com/yuanc669/colleague-skill
評估是否適合整合至工作架構


在 Obsidian vault 建對應資料夾 + 工作筆記
```bash
mkdir -p "<vault路徑>/<總資料夾名>"
```
建立 `<vault路徑>/<總資料夾名>/工作筆記.md`：
```markdown
# <總資料夾名> 工作筆記

> 📌 進度日誌（變動快）。專案藍圖請看 GDrive 端的 `CLAUDE.md`。
> 進度只在這裡記錄，避免雙寫漂移。

## ⏯️ 上次做到哪

\*\*最後動作\*\*：（剛建好總專案、還沒做工具）
\*\*所在 repo\*\*：\[<repo名>](https://github.com/<你的帳號>/<repo名>)

## 🛠️ 工具清單

（尚無，待加）

## 🗓️ 最近更動紀錄

| 日期 | 變更摘要 | GDrive | Obsidian | GitHub |
|------|----------|--------|----------|--------|
| <今天日期> | 初始化班級工具總專案 | ✅ | ✅ | ✅ |

## 🕳️ 踩坑筆記

（之後遇到坑就記在這）
```
---
安裝 /收工 skill
步驟 5：建立 SKILL.md
```bash
mkdir -p \~/.claude-skills/shutdown
```
在 `\~/.claude-skills/shutdown/SKILL.md` 建立以下內容：
````markdown
---
name: shutdown
description: 收工同步助手。當使用者說「收工」、「結束了」、「準備換電腦」、「該同步的同步」、「先到這裡」等任何要結束工作並進行三方同步的請求時，請一定要使用此技能。本技能會智能更新 Obsidian 工作筆記、git commit + push GitHub。
---

# 收工同步助手

對話結束前，把今天的工作完整保存到三個家：
- \*\*GDrive\*\*：自動同步（不用管）
- \*\*Obsidian 工作筆記\*\*：智能更新「上次做到哪」+「最近更動紀錄」
- \*\*GitHub\*\*：commit + push 本 repo 變動

## 收工 SOP（依序執行）

### 步驟 1：盤點今天做了什麼
從對話歷史摘要：完成的檔案、決策、踩到的新坑。

### 步驟 2：找到工作目錄與工作筆記
- 當前 GDrive 工作目錄：`$PWD`（或從對話脈絡推斷）
- Obsidian 工作筆記：`<vault>/<同名資料夾>/工作筆記.md`
- 若 vault 沒對應資料夾 → 提醒使用者，但仍進行 GitHub 同步

### 步驟 3：更新 Obsidian 工作筆記
- 「⏯️ 上次做到哪」段：最後動作、完成的檔案、對話脈絡
- 「🗓️ 最近更動紀錄」表格最後加一行：今天日期 + 摘要 + ✅✅✅
- 「🕳️ 踩坑筆記」（若有新坑）：依分類加進去

### 步驟 4：Git commit + push
```bash
cd "<工作目錄>"
git config windows.appendAtomically false
git add <今天動到的檔案，不要 add .claude/>
git commit -m "<今天工作摘要的 commit message>"
git push origin <branch>
```

commit message 寫法：
- 標題行：「動詞 + 對象」
- 正文：3-5 條 bullet 描述變動 + 為什麼

### 步驟 5：報告同步狀態
給使用者一個三勾表格：

| 平台 | 動到的檔案 | 狀態 |
|------|----------|------|
| GDrive | ... | ✅（自動） |
| Obsidian | 工作筆記更新 | ✅ |
| GitHub | commit + push | ✅ |

## 不該做的事
- ❌ 對「沒實質進度」的對話也跑同步（例：使用者只是問問題沒改檔）
- ❌ 把 `.claude/settings.local.json`、`.claude/worktrees/` commit 進去
- ❌ commit message 寫「更新」、「修改」這種沒資訊的字
````
步驟 5.1：重啟 Claude Code 讓 skill 載入
🖐️ 手動操作：完全關閉 Claude Code 桌面版，再重新開啟。
驗證：對 Claude 說「收工」，看是否自動觸發 SOP。如果觸發，✅ 完成。
---
步驟 5.5（選配）：要不要裝「忘記打收工的安全網」？
🖐️ 詢問使用者：「要不要也裝 SessionEnd hook？這是『你忘記說收工、直接關 Claude Code 時，會自動做 git commit 備份』的安全網。」
不要：跳到階段四
要：繼續
5.5.1 建立 session-cleanup.sh
```bash
mkdir -p \~/.claude/scripts
```
在 `\~/.claude/scripts/session-cleanup.sh` 建立：
```bash
#!/bin/bash
# SessionEnd 安全網：對話結束時若 GDrive 內 repo 還有未提交變更，自動 commit + push

LOG\_FILE="$HOME/.claude/scripts/session-cleanup.log"
log() { echo "\[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG\_FILE"; }

INPUT=$(cat 2>/dev/null || echo "")
WORKDIR=$(echo "$INPUT" | python -c "import sys, json; d=json.load(sys.stdin); print(d.get('cwd', ''))" 2>/dev/null)
\[ -z "$WORKDIR" ] \&\& WORKDIR="$PWD"

log "========== SessionEnd 觸發 =========="
log "工作目錄：$WORKDIR"

# 只處理 GDrive 內 repo
case "$WORKDIR" in
    \*雲端硬碟\*) ;;
    \*"My Drive"\*) ;;
    \*) log "  → 非 GDrive 目錄，跳過"; exit 0 ;;
esac

cd "$WORKDIR" || exit 0
\[ -d ".git" ] || exit 0

git config windows.appendAtomically false 2>/dev/null
git add -u 2>/dev/null

if git diff --cached --quiet; then
    log "  → 無 modified tracked 檔案，跳過"
    exit 0
fi

REPO\_NAME=$(basename "$WORKDIR")
git commit -m "\[SessionEnd 自動保存] $(date +'%Y-%m-%d %H:%M')

對話結束時 SessionEnd hook 自動保存。詳細工作摘要請查 Obsidian 工作筆記：$REPO\_NAME/工作筆記.md" >/dev/null 2>\&1

git push origin HEAD >/dev/null 2>\&1
log "  ✅ 已 commit + push"
```
設可執行：
```bash
chmod +x \~/.claude/scripts/session-cleanup.sh
```
5.5.2 編輯 settings.json 加 hook
修改 `\~/.claude/settings.json`，加入 `hooks` 段（若已有 hooks 段，把 SessionEnd 加進去）：
```json
{
  "hooks": {
    "SessionEnd": \[
      {
        "hooks": \[
          {
            "type": "command",
            "command": "bash \~/.claude/scripts/session-cleanup.sh"
          }
        ]
      }
    ]
  }
}
```
> 💡 兩者\*\*不衝突\*\*：你正常打「收工」→ skill 接手；忘記打 → hook 接手做純備份。
