import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False

# Path configuration
weight_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20251001_body weight.xlsx'
biochem_data_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Cleaned_Data.csv'
output_dir = r'100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Analysis'
os.makedirs(output_dir, exist_ok=True)

# 1. Load and parse Body Weight
df_raw = pd.read_excel(weight_path, sheet_name='All')

# Extract weeks from Row 0
weeks = []
for col in df_raw.columns:
    val = str(df_raw.iloc[0][col])
    if 'W' in val and val != '週齡':
        weeks.append((col, val))

# Identify data rows and groups
data_rows = []
current_group = None
for i in range(3, len(df_raw)):
    g_val = df_raw.iloc[i, 0]
    if pd.notna(g_val):
        current_group = str(g_val).strip()
    
    mouse_id = df_raw.iloc[i, 2]
    
    # Collect weights for each week
    row_data = {'Group': current_group, 'MouseID': mouse_id}
    has_data = False
    for col_idx, w_name in weeks:
        w_val = df_raw.iloc[i][col_idx]
        try:
            val = float(str(w_val).replace('-', 'nan').replace('..', '.'))
            row_data[w_name] = val
            has_data = True
        except:
            row_data[w_name] = np.nan
    
    if has_data:
        data_rows.append(row_data)

df_w = pd.DataFrame(data_rows)

# 2. Add Therapy final weights from Biochemistry
df_biochem = pd.read_csv(biochem_data_path)
# Map biochemical groups to something compatible if needed
# Actually, let's just use biochemistry for Path 6 and Path 1-5 end-points if they match.

# Melt to long format for plotting
df_long = df_w.melt(id_vars=['Group', 'MouseID'], var_name='Week', value_name='Weight')
df_long['WeekNum'] = df_long['Week'].str.extract('(\d+)').astype(float)

# Group mappings for Paths
paths = {
    "Path1_Aging": ["Sham"], # Sham progression over time
    "Path2_Acute": ["Sham", "HS6W"], # W0-W2
    "Path4_Progression": ["Sham", "HS6W", "HS10W"], # W0-W10
    "Path5_Drivers": ["Sham", "HFD", "HS10W"] # W0-W10
}

# Generate Path 1-5 Results
for path_name, groups in paths.items():
    path_df = df_long[df_long['Group'].isin(groups)].dropna(subset=['Weight'])
    
    # Summary Table (Mean ± SEM)
    summary = path_df.groupby(['Group', 'WeekNum'])['Weight'].agg(['mean', 'sem']).reset_index()
    summary.to_csv(os.path.join(output_dir, f"{path_name}_Weight_Summary.csv"), index=False)
    
    # Plot
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=path_df, x='WeekNum', y='Weight', hue='Group', marker='o', err_style='bars')
    plt.title(f"Body Weight Progression - {path_name}")
    plt.xlabel("Weeks")
    plt.ylabel("Weight (g)")
    plt.savefig(os.path.join(output_dir, f"{path_name}_Weight_Plot.png"))
    plt.close()

# Path 6: Therapy (End-point weights from Biochemistry)
therapy_groups = ["HS10W", "HS10WGaE9", "HS10WGaE10"]
df_therapy = df_biochem[df_biochem['Group'].isin(therapy_groups)].copy()

plt.figure(figsize=(8, 6))
sns.boxplot(x='Group', y='BodyWeight (g)', data=df_therapy, palette="Set2")
sns.stripplot(x='Group', y='BodyWeight (g)', data=df_therapy, color=".3", alpha=0.5)
plt.title("End-point Body Weight (Path 6: Therapy)")
plt.savefig(os.path.join(output_dir, "Path6_Therapy_Weight_Endpoint.png"))
plt.close()

df_therapy[['Group', 'BodyWeight (g)']].to_csv(os.path.join(output_dir, "Path6_Therapy_Weight_Prism.csv"), index=False)

print(f"Body weight analysis completed. Results in {output_dir}")
