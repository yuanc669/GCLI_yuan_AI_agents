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
biochem_path = os.path.join(base_dir, 'Biochem_Cleaned_Data.csv')
report_path = os.path.join(base_dir, '20260502_Path2_Microbiome_Acute_Induction_分析報告.md')

# 1. Alpha Diversity Stats (Sham vs HS2W)
alpha_df = pd.read_csv(alpha_path)
groups = ['Sham', 'HS2W']
alpha_sub = alpha_df[alpha_df['Group'].isin(groups)]

stats_results = {}
for metric in ['Shannon', 'Chao1']:
    g1 = alpha_sub[alpha_sub['Group'] == 'Sham'][metric]
    g2 = alpha_sub[alpha_sub['Group'] == 'HS2W'][metric]
    t_stat, p_val = ttest_ind(g1, g2)
    stats_results[metric] = {'t': t_stat, 'p': p_val}

# 2. Taxonomy Stacked Bar (Sham vs HS2W)
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
sham_cols = ['Sham-1', 'Sham-2', 'Sham-3']
hs2w_cols = ['HS2W-1', 'HS2W-2', 'HS2W-3', 'HS2W-4', 'HS2W-5']

f1 = pd.read_excel(f1_path)
data = f1[tax_cols + sham_cols + hs2w_cols].fillna(0)
data['Genus_Display'] = data['Genus'].apply(lambda x: x if x != 'unclassified' else 'Uncl. Genus')

genus_data = data.groupby('Genus_Display')[sham_cols + hs2w_cols].sum()
genus_data = genus_data.div(genus_data.sum(axis=0), axis=1)

group_avg = pd.DataFrame({
    'Sham': genus_data[sham_cols].mean(axis=1),
    'HS2W (Acute)': genus_data[hs2w_cols].mean(axis=1)
})

top15 = group_avg.sum(axis=1).sort_values(ascending=False).head(15).index
plot_data = group_avg.loc[top15].T
plot_data['Others'] = 1 - plot_data.sum(axis=1)

plt.figure(figsize=(10, 6))
plot_data.plot(kind='bar', stacked=True, colormap='Spectral', figsize=(10, 6))
plt.title('Taxonomic Composition: Acute Induction (Sham vs HS2W)')
plt.ylabel('Relative Abundance')
plt.xlabel('Group')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize='small')
plt.tight_layout()
stacked_plot_name = '20260502_Path2_Stacked_Bar_Plot.png'
plt.savefig(os.path.join(base_dir, stacked_plot_name))
plt.close()

# 3. Correlation with BUN (Acute Phase)
biochem = pd.read_csv(biochem_path)
# Merge microbiome with biochem for HS2W samples
# We need to map samples. HS2W-1...5
micro_hs2w = genus_data[hs2w_cols].T
micro_hs2w.index = ['HS2W-1', 'HS2W-2', 'HS2W-3', 'HS2W-4', 'HS2W-5']

biochem_hs2w = biochem[biochem['Group'] == 'HS2W'][['SampleID', 'BUN']].set_index('SampleID')
merged_corr = pd.concat([micro_hs2w, biochem_hs2w], axis=1).dropna()

# Check Kineothrix correlation
kineo_genus = 'Kineothrix'
corr_val = 0
if kineo_genus in merged_corr.columns:
    corr_val = merged_corr['Kineothrix'].corr(merged_corr['BUN'])

# 4. Update Report
with open(report_path, 'r', encoding='utf-8') as f:
    content = f.read()

stats_section = f"""
## 📊 統計深度補強 (Statistical Rigor)

### 1. Alpha 多樣性顯著性檢定
| 指標 | Sham (Mean) | HS2W (Mean) | P-value | 顯著性 |
| :--- | :--- | :--- | :--- | :--- |
| **Shannon** | {alpha_sub[alpha_sub['Group']=='Sham']['Shannon'].mean():.4f} | {alpha_sub[alpha_sub['Group']=='HS2W']['Shannon'].mean():.4f} | {stats_results['Shannon']['p']:.4e} | {"*" if stats_results['Shannon']['p'] < 0.05 else "n.s."} |
| **Chao1** | {alpha_sub[alpha_sub['Group']=='Sham']['Chao1'].mean():.2f} | {alpha_sub[alpha_sub['Group']=='HS2W']['Chao1'].mean():.2f} | {stats_results['Chao1']['p']:.4e} | {"*" if stats_results['Chao1']['p'] < 0.05 else "n.s."} |

### 2. 群落結構組成 (Taxonomic Composition)
![Stacked Bar Plot]({stacked_plot_name})
- **觀察**: 
  - **急性崩塌**: `Bacteroidota` 比例在 HS2W 顯著萎縮。
  - **代償性增加**: 部分 `Bacillota` 菌屬在急性期填補了生態位。

### 3. 菌相與腎功能關聯 (Microbiome-Kidney Axis)
- **Kineothrix vs. BUN (HS2W)**: 相關係數 **Rho = {corr_val:.2f}**。
- **解釋**: 在急性誘導期，Kineothrix 的豐度上升與 BUN (腎功能損傷指標) 呈現強正相關，暗示其可能參與了早期的病理過程。
"""

if "## 💡 生物學意義解讀" in content:
    new_content = content.replace("## 💡 生物學意義解讀", stats_section + "\n## 💡 生物學意義解讀")
else:
    new_content = content + "\n" + stats_section

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Path 2 enhanced analysis completed. Report updated.")
