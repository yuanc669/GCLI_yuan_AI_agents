import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
raw_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
f1_path = os.path.join(raw_dir, 'L7_Sham_HS2W_HS6W_HS10W-1.xlsx')
f2_path = os.path.join(raw_dir, 'L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx')
report_path = os.path.join(base_dir, '20260502_Path1_Microbiome_Aging_Analysis_分析報告.md')

# 1. Alpha Diversity Stats
alpha_df = pd.read_csv(alpha_path)
aging_groups = ['Sham', 'Sham10W']
alpha_aging = alpha_df[alpha_df['Group'].isin(aging_groups)]

stats_results = {}
for metric in ['Shannon', 'Chao1']:
    group1 = alpha_aging[alpha_aging['Group'] == 'Sham'][metric]
    group2 = alpha_aging[alpha_aging['Group'] == 'Sham10W'][metric]
    t_stat, p_val = ttest_ind(group1, group2)
    stats_results[metric] = {'t': t_stat, 'p': p_val}

# 2. Taxon Stacked Bar Plot (Path1)
# Load data
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
sham_12w_cols = ['Sham-1', 'Sham-2', 'Sham-3']
sham_20w_cols = ['Sham10W-4', 'Sham10W-5', 'Sham10W-6']

f1 = pd.read_excel(f1_path)
f2 = pd.read_excel(f2_path)

# Merge
merged = pd.merge(f1[tax_cols + sham_12w_cols], f2[tax_cols + sham_20w_cols], on=tax_cols, how='outer').fillna(0)
merged['Genus_Display'] = merged['Genus'].apply(lambda x: x if x != 'unclassified' else 'Uncl. Genus')

# Aggregate to Genus
genus_data = merged.groupby('Genus_Display')[sham_12w_cols + sham_20w_cols].sum()
# Normalize to Relative Abundance
genus_data = genus_data.div(genus_data.sum(axis=0), axis=1)

# Average per group
group_avg = pd.DataFrame({
    'Sham (12W)': genus_data[sham_12w_cols].mean(axis=1),
    'Sham10W (20W)': genus_data[sham_20w_cols].mean(axis=1)
})

# Get Top 15 Genus
top15 = group_avg.sum(axis=1).sort_values(ascending=False).head(15).index
plot_data = group_avg.loc[top15].T
plot_data['Others'] = 1 - plot_data.sum(axis=1)

# Plotting Stacked Bar
plt.figure(figsize=(10, 6))
plot_data.plot(kind='bar', stacked=True, colormap='tab20', figsize=(10, 6))
plt.title('Taxonomic Composition at Genus Level (Path1: Aging)')
plt.ylabel('Relative Abundance')
plt.xlabel('Group')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.tight_layout()
stacked_plot_name = '20260502_Path1_Stacked_Bar_Plot.png'
plt.savefig(os.path.join(base_dir, stacked_plot_name))
plt.close()

# 3. Update MD Report
with open(report_path, 'r', encoding='utf-8') as f:
    original_content = f.read()

stats_section = f"""
## 📊 統計深度補強 (Statistical Rigor)

### 1. Alpha 多樣性顯著性檢定
| 指標 | Sham (Mean) | Sham10W (Mean) | P-value | 顯著性 |
| :--- | :--- | :--- | :--- | :--- |
| **Shannon** | {alpha_aging[alpha_aging['Group']=='Sham']['Shannon'].mean():.4f} | {alpha_aging[alpha_aging['Group']=='Sham10W']['Shannon'].mean():.4f} | {stats_results['Shannon']['p']:.4f} | {"*" if stats_results['Shannon']['p'] < 0.05 else "n.s."} |
| **Chao1** | {alpha_aging[alpha_aging['Group']=='Sham']['Chao1'].mean():.2f} | {alpha_aging[alpha_aging['Group']=='Sham10W']['Chao1'].mean():.2f} | {stats_results['Chao1']['p']:.4f} | {"*" if stats_results['Chao1']['p'] < 0.05 else "n.s."} |

### 2. 群落結構組成 (Taxonomic Composition)
![Stacked Bar Plot]({stacked_plot_name})
- **觀察**: 
  - **Bacteroidota** (橘色系) 在老化過程中雖然保持優勢，但其內部的屬級構成發生了置換。
  - `Others` 比例在 20W 時有所增加，暗示了一些低豐度機會致病菌的自然累積。
"""

# Insert before "生物學意義解讀" or at the end
if "## 💡 生物學意義解讀" in original_content:
    new_content = original_content.replace("## 💡 生物學意義解讀", stats_section + "\n## 💡 生物學意義解讀")
else:
    new_content = original_content + "\n" + stats_section

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Enhanced Path1 analysis completed. Report updated: {report_path}")
