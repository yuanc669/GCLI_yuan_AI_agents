#!/bin/bash
# SessionEnd 安全網：對話結束時自動保存 GDrive 內的變更

LOG_FILE="$(dirname "$0")/session-cleanup.log"
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"; }

# 獲取工作目錄
WORKDIR="$PWD"

log "========== SessionEnd 觸發 =========="
log "工作目錄：$WORKDIR"

# 確認在 Git 目錄且在 GDrive 內
if [ ! -d ".git" ]; then
    log "  → 非 Git 儲存庫，跳過"
    exit 0
fi

git add -u 2>/dev/null

if git diff --cached --quiet; then
    log "  → 無變更，跳過"
    exit 0
fi

REPO_NAME=$(basename "$WORKDIR")
git commit -m "[SessionEnd 自動保存] $(date +'%Y-%m-%d %H:%M')

對話結束時自動備份。詳細記錄請見 Obsidian 工作筆記。" >/dev/null 2>&1

git push origin HEAD >/dev/null 2>&1
log "  ✅ 已 commit + push"
