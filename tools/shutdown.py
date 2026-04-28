import os
import subprocess
from datetime import datetime

def run_cmd(cmd):
    """執行 Shell 指令並捕獲錯誤"""
    subprocess.run(cmd, shell=True, check=True)

def shutdown_routine():
    print("🚀 同事，我正在幫你進行收工同步程序...")
    today = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 檢查 Git 狀態
    try:
        # 設定 Windows Google Drive 相容性
        run_cmd("git config windows.appendAtomically false")
        
        # 暫存所有變動
        run_cmd("git add .")
        
        # 檢查是否有可提交的變動
        status = subprocess.run("git status --porcelain", shell=True, capture_output=True, text=True).stdout
        if not status:
            print("💡 沒有偵測到新的變動，略過提交。")
            return

        # 執行提交
        run_cmd(f'git commit -m "AI 團隊自動存檔: {today} (同步研究指令與筆記)"')
        
        # 嘗試推送到遠端 (若已設定 origin)
        remote_check = subprocess.run("git remote", shell=True, capture_output=True, text=True).stdout
        if "origin" in remote_check:
            run_cmd("git push origin master") # 目前專案分支為 master
            print("✅ GitHub 遠端同步完成。")
        else:
            print("⚠️ 未偵測到遠端 origin，僅完成本地存檔。")
            
        print(f"👋 程序結束於 {today}。明天見！")
        
    except Exception as e:
        print(f"❌ 同事，同步程序失敗: {e}")

if __name__ == "__main__":
    shutdown_routine()
