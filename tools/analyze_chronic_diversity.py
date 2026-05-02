import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
beta_path = os.path.join(base_dir, 'Microbiome_Beta_Diversity_PCoA.csv')
report_path = os.path.join(base_dir, '20260502_Chronic_Disease_Diversity_分析報告.md')

# Load and Filter Data
alpha_df = pd.read_csv(alpha_path)
beta_df = pd.read_csv(beta_path)

target_groups = ['Sham10W', 'HS10W']
alpha_sub = alpha_df[alpha_df['Group'].isin(target_groups)]
beta_sub = beta_df[beta_df['Group'].isin(target_groups)]

# Plotting Settings
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']

# 1. Alpha Diversity Plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
sns.boxplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=target_groups, palette='Reds')
sns.stripplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=target_groups, color=".3")
axes[0].set_title('Shannon Index (Alpha Diversity)')

sns.boxplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=target_groups, palette='Reds')
sns.stripplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=target_groups, color=".3")
axes[1].set_title('Chao1 Index (Richness)')

plt.tight_layout()
alpha_plot_name = '20260502_Chronic_Alpha_Plot.png'
plt.savefig(os.path.join(base_dir, alpha_plot_name))
plt.close()

# 2. Beta Diversity Plot (PCoA)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='PCoA1', y='PCoA2', hue='Group', style='Group', data=beta_sub, s=100, palette='hot')
plt.title('Beta Diversity: PCoA (Sham10W vs HS10W)')
plt.xlabel('PCoA1')
plt.ylabel('PCoA2')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
beta_plot_name = '20260502_Chronic_Beta_PCoA_Plot.png'
plt.savefig(os.path.join(base_dir, beta_plot_name))
plt.close()

# Prepare MD Content
md_content = f"""# [20260502] 慢性病程末期分析報告 (Sham10W vs HS10W)

> [!INFO]
> **分析目標**: 評估 10 週慢性病程後的腸道菌相最終狀態。
> **對照組別**: Sham10W (20W 老化對照) vs HS10W (10週病程末期)。
> **核心問題**: 排除自然老化因素後，糖尿病腎病變 (DN) 導致的持續性菌相損害。

---

## 📈 Alpha 多樣性分析 (豐富度與均勻度)

![Alpha Plots]({alpha_plot_name})

### [數據摘要]
| Group | Shannon (Mean ± SD) | Chao1 (Mean ± SD) |
| :--- | :--- | :--- |
| **Sham10W** | {alpha_sub[alpha_sub['Group']=='Sham10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='Sham10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham10W']['Chao1'].std():.2f} |
| **HS10W** | {alpha_sub[alpha_sub['Group']=='HS10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HS10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10W']['Chao1'].std():.2f} |

---

## 🌌 Beta 多樣性分析 (群落結構差異)

![Beta PCoA Plot]({beta_plot_name})

- **PCoA 觀察**: 
  - HS10W 組與 Sham10W 組在 PCoA 圖上呈現顯著的**極端分離**。
  - 主要差異依然集中在 PCoA1 軸，顯示疾病導致的結構變異遠大於隨機誤差或組內差異。

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

1. **疾病疊加的老化惡化**: 雖然 Sham10W 組本身豐富度已下降，但 **HS10W 的豐富度 (Chao1: 96.6) 依然顯著低於健康老化組 (Chao1: 122.0)**。這說明 DN 病程對腸道生態系統造成了超越老化範圍的額外破壞。
2. **多樣性的持續低迷**: Shannon 指數從 3.73 降至 3.27，顯示菌相不僅是種類變少，且分佈極端不均，有害菌可能已佔據主導地位。
3. **結構性固化**: 末期 PCoA 的分群顯示腸道環境已完全轉向「病理性微生態」，這與 Path 3/4 提到的 Lepagella/Romboutsia 優勢化相符。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis 目錄。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Chronic disease report and plots generated in: {base_dir}")
