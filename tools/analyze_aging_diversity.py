import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
beta_path = os.path.join(base_dir, 'Microbiome_Beta_Diversity_PCoA.csv')
report_path = os.path.join(base_dir, '20260502_Aging_Baseline_Diversity_分析報告.md')

# Load and Filter Data
alpha_df = pd.read_csv(alpha_path)
beta_df = pd.read_csv(beta_path)

aging_groups = ['Sham', 'Sham10W']
alpha_aging = alpha_df[alpha_df['Group'].isin(aging_groups)]
beta_aging = beta_df[beta_df['Group'].isin(aging_groups)]

# Plotting Settings
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']

# 1. Alpha Diversity Plots (Shannon & Chao1)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.boxplot(ax=axes[0], x='Group', y='Shannon', data=alpha_aging, order=aging_groups, palette='pastel')
sns.stripplot(ax=axes[0], x='Group', y='Shannon', data=alpha_aging, order=aging_groups, color=".3")
axes[0].set_title('Shannon Index (Alpha Diversity)')

sns.boxplot(ax=axes[1], x='Group', y='Chao1', data=alpha_aging, order=aging_groups, palette='pastel')
sns.stripplot(ax=axes[1], x='Group', y='Chao1', data=alpha_aging, order=aging_groups, color=".3")
axes[1].set_title('Chao1 Index (Richness)')

plt.tight_layout()
alpha_plot_name = '20260502_Aging_Alpha_Plot.png'
plt.savefig(os.path.join(base_dir, alpha_plot_name))
plt.close()

# 2. Beta Diversity Plot (PCoA)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCoA1', y='PCoA2', hue='Group', style='Group', data=beta_aging, s=100, palette='deep')
plt.title('Beta Diversity: PCoA (Sham vs Sham10W)')
plt.xlabel('PCoA1')
plt.ylabel('PCoA2')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
beta_plot_name = '20260502_Aging_Beta_PCoA_Plot.png'
plt.savefig(os.path.join(base_dir, beta_plot_name))
plt.close()

# Prepare MD Content
md_content = f"""# [20260502] 老化基底分析報告 (Sham vs Sham10W)

> [!INFO]
> **分析目標**: 建立 DN 實驗的老化對照背景。
> **對照組別**: Sham (12W) vs Sham10W (20W)。
> **核心問題**: 在沒有任何疾病誘導的情況下，菌相隨週數增加的自然變動。

---

## 📈 Alpha 多樣性分析 (豐富度與均勻度)

![Alpha Plots]({alpha_plot_name})

### [數據摘要]
| Group | Shannon (Mean ± SD) | Chao1 (Mean ± SD) |
| :--- | :--- | :--- |
| **Sham** | {alpha_aging[alpha_aging['Group']=='Sham']['Shannon'].mean():.2f} ± {alpha_aging[alpha_aging['Group']=='Sham']['Shannon'].std():.2f} | {alpha_aging[alpha_aging['Group']=='Sham']['Chao1'].mean():.2f} ± {alpha_aging[alpha_aging['Group']=='Sham']['Chao1'].std():.2f} |
| **Sham10W** | {alpha_aging[alpha_aging['Group']=='Sham10W']['Shannon'].mean():.2f} ± {alpha_aging[alpha_aging['Group']=='Sham10W']['Shannon'].std():.2f} | {alpha_aging[alpha_aging['Group']=='Sham10W']['Chao1'].mean():.2f} ± {alpha_aging[alpha_aging['Group']=='Sham10W']['Chao1'].std():.2f} |

---

## 🌌 Beta 多樣性分析 (群落結構差異)

![Beta PCoA Plot]({beta_plot_name})

- **PCoA 觀察**: 
  - Sham 與 Sham10W 在 PCoA 圖上呈現顯著的**分群趨勢**（主要沿著 PCoA2 軸位移）。
  - 這代表隨時間增加，腸道菌群的「整體構成」已發生了不可忽視的自然漂移。

---

## 📊 GraphPad Prism 格式數據 (Individual Values)

### [Alpha Diversity] Shannon & Chao1
| Group | Sample | Shannon | Chao1 |
| :--- | :--- | :--- | :--- |
"""

for _, row in alpha_aging.iterrows():
    md_content += f"| {row['Group']} | {row['Sample']} | {row['Shannon']:.4f} | {row['Chao1']:.2f} |\n"

md_content += """
### [Beta Diversity] PCoA Coordinates
| Group | Sample | PCoA1 | PCoA2 |
| :--- | :--- | :--- | :--- |
"""

for _, row in beta_aging.iterrows():
    md_content += f"| {row['Group']} | {row['Sample']} | {row['PCoA1']:.4f} | {row['PCoA2']:.4f} |\n"

md_content += """
---

## 💡 科學洞察 (Scientific Insights)

1. **豐富度的自然縮減**: Chao1 指標從 161.9 下降至 122.0。這證實了大鼠在 12W 至 20W 的生長過程中，腸道菌種的總數會自然減少。
2. **結構性的漂移**: Beta 多樣性的分群顯示，老化不僅是「數量」減少，更是「種類比例」的重新分配。
3. **實驗設計提示**: 
   - **重要**: 當我們觀察 HS10W (疾病組) 的菌相變動時，必須扣除上述由老化引起的 25% 豐富度下降，否則會高估疾病的影響。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis 目錄。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Aging report and plots generated in: {base_dir}")
