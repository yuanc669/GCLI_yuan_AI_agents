import os
import pandas as pd
from datetime import datetime

# 1. Load Data
data_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis"
pas_file = os.path.join(data_dir, "PAS_Quantification_Results.csv")
mt_file = os.path.join(data_dir, "MT_Fibrosis_Results.csv")

df_pas = pd.read_csv(pas_file) if os.path.exists(pas_file) else pd.DataFrame()
df_mt = pd.read_csv(mt_file) if os.path.exists(mt_file) else pd.DataFrame()

# Merge if both exist, based on Group and matching sample index logic if needed, 
# but they are separate images. We'll group them for Prism.
# To make Prism ready, we need each column to be a group.

def create_prism_csv(df, value_col, groups, output_path):
    if df.empty: return
    prism_dict = {}
    max_len = 0
    for g in groups:
        vals = df[df['Group'] == g][value_col].tolist()
        prism_dict[g] = vals
        if len(vals) > max_len: max_len = len(vals)
    
    # Pad with NaN
    for g in groups:
        prism_dict[g] += [np.nan] * (max_len - len(prism_dict[g]))
        
    df_prism = pd.DataFrame(prism_dict)
    df_prism.to_csv(output_path, index=False)

import numpy as np

# Define Paths
paths = {
    "Path1_Aging": ["Sham", "Sham10W"],
    "Path2_Acute": ["Sham", "HS2W"],
    "Path3_Establishment": ["SS10W", "HS10W"],
    "Path4_Progression": ["Sham", "HS2W", "HS6W", "HS10W"],
    "Path5_Driver": ["Sham10W", "SS10W", "HFD10W", "HS10W"],
    "Path6_Efficacy": ["SS10W", "HS10W", "GAE9", "GAE10"],
    "Path7_Global": ["Sham", "Sham10W", "HS2W", "HS6W", "HS10W", "HFD10W", "SS10W", "GAE9", "GAE10"]
}

base_report_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\03_Pathology"
prism_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\06_Prism_Outputs"

if not os.path.exists(prism_dir): os.makedirs(prism_dir)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

master_summary = []

for path_name, groups in paths.items():
    # Directories
    path_res_dir = os.path.join(base_report_dir, path_name, "02_Results")
    if not os.path.exists(path_res_dir): os.makedirs(path_res_dir)
    
    # Prism CSVs
    if not df_pas.empty:
        pas_out = os.path.join(prism_dir, f"{path_name}_PAS_Mesangial_Index.csv")
        create_prism_csv(df_pas, "Mesangial_Index_Percent", groups, pas_out)
        
    if not df_mt.empty:
        mt_out = os.path.join(prism_dir, f"{path_name}_MT_CVF.csv")
        create_prism_csv(df_mt, "CVF_Percent", groups, mt_out)

    # Generate Markdown Report
    report_file = os.path.join(path_res_dir, f"{path_name}_Pathology_Report.md")
    
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(f"# DN_GaExo 病理分析報告 - {path_name}\n")
        f.write(f"**產生時間**: {timestamp}\n\n")
        f.write("## 1. 包含組別\n")
        f.write(", ".join(groups) + "\n\n")
        
        f.write("## 2. PAS 定量摘要 (Mesangial Expansion)\n")
        if not df_pas.empty:
            pas_sub = df_pas[df_pas['Group'].isin(groups)]
            f.write(pas_sub.groupby("Group")["Mesangial_Index_Percent"].agg(['mean', 'std', 'count']).to_markdown())
        f.write("\n\n")
        
        f.write("## 3. MT 定量摘要 (Tubulointerstitial Fibrosis - CVF%)\n")
        if not df_mt.empty:
            mt_sub = df_mt[df_mt['Group'].isin(groups)]
            f.write(mt_sub.groupby("Group")["CVF_Percent"].agg(['mean', 'std', 'count']).to_markdown())
        f.write("\n\n")
        
        f.write("## 4. Prism 數據連結\n")
        f.write(f"- [PAS Prism Data](../../../../06_Prism_Outputs/{path_name}_PAS_Mesangial_Index.csv)\n")
        f.write(f"- [MT Prism Data](../../../../06_Prism_Outputs/{path_name}_MT_CVF.csv)\n")
    
    print(f"Generated report and data for {path_name}")

print("All Path 1-7 reports generated successfully.")
