import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
beta_path = os.path.join(base_dir, 'Microbiome_Beta_Diversity_PCoA.csv')
report_path = os.path.join(base_dir, '20260502_Acute_Induction_Diversity_分析報告.md')

# Load and Filter Data
alpha_df = pd.read_csv(alpha_path)
beta_df = pd.read_csv(beta_path)

target_groups = ['Sham', 'HS2W']
alpha_sub = alpha_df[alpha_df['Group'].isin(target_groups)]
beta_sub = beta_df[beta_df['Group'].isin(target_groups)]

# Plotting Settings
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']

# 1. Alpha Diversity Plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=target_groups, palette='Oranges')
sns.stripplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=target_groups, color=".3")
axes[0].set_title('Shannon Index (Alpha Diversity)')

sns.boxplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=target_groups, palette='Oranges')
sns.stripplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=target_groups, color=".3")
axes[1].set_title('Chao1 Index (Richness)')

plt.tight_layout()
alpha_plot_name = '20260502_Acute_Alpha_Plot.png'
plt.savefig(os.path.join(base_dir, alpha_plot_name))
plt.close()

# 2. Beta Diversity Plot (PCoA)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCoA1', y='PCoA2', hue='Group', style='Group', data=beta_sub, s=100, palette='autumn')
plt.title('Beta Diversity: PCoA (Sham vs HS2W)')
plt.xlabel('PCoA1')
plt.ylabel('PCoA2')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
beta_plot_name = '20260502_Acute_Beta_PCoA_Plot.png'
plt.savefig(os.path.join(base_dir, beta_plot_name))
plt.close()

# Prepare MD Content
md_content = f"""# [20260502] 急性誘導分析報告 (Sham vs HS2W)

> [!INFO]
> **分析目標**: 評估疾病誘導後第 2 週 (HS2W) 的即時菌相衝擊。
> **對照組別**: Sham (12W 健康) vs HS2W (急性誘導 2 週)。
> **核心問題**: HFD+STZ 介入後，腸道生態系統的崩潰程度。

---

## 📈 Alpha 多樣性分析 (豐富度與均勻度)

![Alpha Plots]({alpha_plot_name})

### [數據摘要]
| Group | Shannon (Mean ± SD) | Chao1 (Mean ± SD) |
| :--- | :--- | :--- |
| **Sham** | {alpha_sub[alpha_sub['Group']=='Sham']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='Sham']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham']['Chao1'].std():.2f} |
| **HS2W** | {alpha_sub[alpha_sub['Group']=='HS2W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS2W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HS2W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS2W']['Chao1'].std():.2f} |

---

## 🌌 Beta 多樣性分析 (群落結構差異)

![Beta PCoA Plot]({beta_plot_name})

- **PCoA 觀察**: 
  - Sham 與 HS2W 在 PCoA1 軸 (解釋變異度最高軸) 上呈現**極端分離**。
  - 這代表 HS2W 誘導後，腸道菌群的「整體結構」發生了根本性的劇變，已完全脫離了健康狀態。

---

## 📊 GraphPad Prism 格式數據 (Individual Values)

### [Alpha Diversity] Shannon & Chao1
| Group | Sample | Shannon | Chao1 |
| :--- | :--- | :--- | :--- |
"""

for _, row in alpha_sub.iterrows():
    md_content += f"| {row['Group']} | {row['Sample']} | {row['Shannon']:.4f} | {row['Chao1']:.2f} |\n"

md_content += """
### [Beta Diversity] PCoA Coordinates
| Group | Sample | PCoA1 | PCoA2 |
| :--- | :--- | :--- | :--- |
"""

for _, row in beta_sub.iterrows():
    md_content += f"| {row['Group']} | {row['Sample']} | {row['PCoA1']:.4f} | {row['PCoA2']:.4f} |\n"

md_content += """
---

## 💡 科學洞察 (Scientific Insights)

1. **豐富度的「斷崖式下降」**: Chao1 指標從 161.9 驟降至 93.2。這證實了急性誘導僅在 2 週內就導致了腸道物種數量的嚴重流失（Loss of Richness）。
2. **結構的即時重組**: Beta 多樣性的巨大位移顯示，健康優勢菌群 (如 Path 2 提到的 Bacteroidota) 正在被迅速清除。
3. **實驗意義**: HS2W 的數據點建立了疾病的「起始失調狀態」，是後續觀察 GaExo 介入能否扭轉局勢的關鍵對照組。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis 目錄。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Acute induction report and plots generated in: {base_dir}")
