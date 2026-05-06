import pandas as pd
import os

# 1. Load the unblinded data
data_path = r"100_Research/02_Active/DN_GaExo/02_Analysis/06_Prism_Outputs/Pathology_MT_Fibrosis_Data_Unblinded.csv"
df = pd.read_csv(data_path)

# 2. Define Path Mappings
paths = {
    "Path1_Aging": ["Sham", "Sham10W"],
    "Path2_Acute": ["Sham", "HS2W"],
    "Path3_Establishment": ["Sham10W", "HS10W"],
    "Path4_Progression": ["Sham", "HS2W", "HS6W", "HS10W"],
    "Path5_Driver": ["Sham10W", "HFD10W", "SS10W", "HS10W"],
    "Path6_Therapy": ["Sham10W", "HS10W", "HS10WGaE9", "HS10WGaE10"]
}

# 3. Generate Path-specific Prism Data (Long format)
prism_output_root = r"100_Research/02_Active/DN_GaExo/02_Analysis/06_Prism_Outputs"
os.makedirs(prism_output_root, exist_ok=True)

for path_name, groups in paths.items():
    path_df = df[df['Group'].isin(groups)].copy()
    # Ensure categorical order for plotting
    path_df['Group'] = pd.Categorical(path_df['Group'], categories=groups, ordered=True)
    path_df = path_df.sort_values('Group')
    
    output_f = os.path.join(prism_output_root, f"{path_name}_MT_Fibrosis_Prism.csv")
    path_df[['Group', 'CVF_Percent']].to_csv(output_f, index=False)
    print(f"Generated {output_f}")

# 4. Create Integrated Markdown Report
report_path = r"100_Research/02_Active/DN_GaExo/02_Analysis/05_Integrated_Synthesis/20260506_Path1-7_MT_Integrated_Master_Report.md"

with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# DN_GaExo 專案：全路徑 MT 纖維化整合大師報告 (Path 1-7)\n\n")
    f.write("**產出時間**：2026-05-06 15:10\n")
    f.write("**分析方法**：Masson's Trichrome 自動化 CVF% 定量（30 um 比例尺校正）\n\n")

    for path_name, groups in paths.items():
        f.write(f"## 📍 {path_name.replace('_', ' ')}\n")
        
        # Stats summary for this path
        path_df = df[df['Group'].isin(groups)]
        summary = path_df.groupby('Group')['CVF_Percent'].agg(['mean', 'std', 'count']).reindex(groups).reset_index()
        
        f.write("### 📊 統計摘要\n")
        f.write(summary.to_markdown(index=False))
        f.write("\n\n")
        
        f.write("### 🖼️ 代表性影像路徑\n")
        for g in groups:
            f.write(f"- **{g}**: `100_Research/02_Active/DN_GaExo/01_Raw_Data/MT/{g}/`\n")
        
        f.write(f"\n### 📥 數據下載 (Prism Ready)\n")
        f.write(f"- [下載 {path_name} CSV](../../06_Prism_Outputs/{path_name}_MT_Fibrosis_Prism.csv)\n\n")
        f.write("---\n\n")

    # Path 7 Global Heatmap logic (summary of all)
    f.write("## 📍 Path 7 Global Integration\n")
    all_summary = df.groupby('Group')['CVF_Percent'].mean().reset_index()
    f.write("### 🌍 全局趨勢概覽 (All Groups Mean CVF%)\n")
    f.write(all_summary.to_markdown(index=False))
    f.write("\n\n- **數據 asset**: `100_Research/02_Active/DN_GaExo/02_Analysis/06_Prism_Outputs/Pathology_MT_Fibrosis_Data_Unblinded.csv`\n")

print(f"Master Report generated at: {report_path}")
