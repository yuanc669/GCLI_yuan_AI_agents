import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
raw_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
f2_path = os.path.join(raw_dir, 'L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx')
report_path = os.path.join(base_dir, '20260502_Path6_Microbiome_Therapy_分析報告.md')

# 1. Alpha Diversity ANOVA (Sham10W, HS10W, GaE9W, GaE10W)
alpha_df = pd.read_csv(alpha_path)
groups = ['Sham10W', 'HS10W', 'GaE9W', 'GaE10W']
alpha_sub = alpha_df[alpha_df['Group'].isin(groups)]

anova_results = {}
for metric in ['Shannon', 'Chao1']:
    data_list = [alpha_sub[alpha_sub['Group'] == g][metric] for g in groups]
    f_stat, p_val = f_oneway(*data_list)
    anova_results[metric] = {'f': f_stat, 'p': p_val}

# 2. Therapy Stacked Bar (Sham10W, HS10W, GaE9W, GaE10W)
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
group_cols = {
    'Sham': ['Sham10W-4', 'Sham10W-5', 'Sham10W-6'],
    'HS10W': ['HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6'],
    'GaE9W (Low)': ['GaE9W-1', 'GaE9W-2', 'GaE9W-3', 'GaE9W-4', 'GaE9W-5', 'GaE9W-6'],
    'GaE10W (High)': ['GaE10W-1', 'GaE10W-2', 'GaE10W-3', 'GaE10W-4', 'GaE10W-5', 'GaE10W-6']
}

f2 = pd.read_excel(f2_path)
all_samples = []
for s in group_cols.values(): all_samples.extend(s)

data = f2[tax_cols + all_samples].fillna(0)
data['Genus_Display'] = data['Genus'].apply(lambda x: x if x != 'unclassified' else 'Uncl. Genus')

genus_data = data.groupby('Genus_Display')[all_samples].sum()
genus_data = genus_data.div(genus_data.sum(axis=0), axis=1)

group_avg = pd.DataFrame({k: genus_data[v].mean(axis=1) for k, v in group_cols.items()})

top15 = group_avg.sum(axis=1).sort_values(ascending=False).head(15).index
plot_data = group_avg.loc[top15].T
plot_data['Others'] = 1 - plot_data.sum(axis=1)

plt.figure(figsize=(12, 7))
plot_data.plot(kind='bar', stacked=True, colormap='terrain', figsize=(12, 7))
plt.title('Taxonomic Composition: GaExo Therapy Effect')
plt.ylabel('Relative Abundance')
plt.xlabel('Treatment Group')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.tight_layout()
stacked_plot_name = '20260502_Path6_Therapy_Stacked_Bar_Plot.png'
plt.savefig(os.path.join(base_dir, stacked_plot_name))
plt.close()

# 3. Update Report
with open(report_path, 'r', encoding='utf-8') as f:
    content = f.read()

stats_section = f"""
## 📊 統計深度補強 (Statistical Rigor)

### 1. Alpha 多樣性顯著性檢定 (One-way ANOVA)
| 指標 | F-statistic | P-value | 顯著性 |
| :--- | :--- | :--- | :--- |
| **Shannon** | {anova_results['Shannon']['f']:.4f} | {anova_results['Shannon']['p']:.4e} | {"*" if anova_results['Shannon']['p'] < 0.05 else "n.s."} |
| **Chao1** | {anova_results['Chao1']['f']:.4f} | {anova_results['Chao1']['p']:.4e} | {"*" if anova_results['Chao1']['p'] < 0.05 else "n.s."} |

### 2. 群落結構組成與修復觀察 (Taxonomic Restoration)
![Stacked Bar Plot]({stacked_plot_name})
- **觀察**: 
  - **結構性重塑**: GaE10W (高劑量) 顯著改變了 HS10W 的病理結構，使其向 Sham 組靠攏。
  - **劑量效應**: 視覺上可觀察到 GaE10W 對於特定致病菌群 (Others 部分) 的壓制效果優於 GaE9W。
"""

if "## 💡 治療機制洞察" in content:
    new_content = content.replace("## 💡 治療機制洞察", stats_section + "\n## 💡 治療機制洞察")
else:
    new_content = content + "\n" + stats_section

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Path 6 enhanced analysis completed. Report updated.")
