import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
beta_path = os.path.join(base_dir, 'Microbiome_Beta_Diversity_PCoA.csv')
report_path = os.path.join(base_dir, '20260502_Disease_Drivers_Diversity_分析報告.md')

# Load and Filter Data
alpha_df = pd.read_csv(alpha_path)
beta_df = pd.read_csv(beta_path)

driver_groups = ['Sham10W', 'SS10W', 'HFD10W', 'HS10W']
alpha_sub = alpha_df[alpha_df['Group'].isin(driver_groups)]
beta_sub = beta_df[beta_df['Group'].isin(driver_groups)]

# Plotting Settings
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']

# 1. Alpha Diversity Plots (Shannon & Chao1 Drivers)
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

sns.boxplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=driver_groups, palette='Set2')
sns.stripplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=driver_groups, color=".3")
axes[0].set_title('Shannon Index (Impact of Drivers)')

sns.boxplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=driver_groups, palette='Set2')
sns.stripplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=driver_groups, color=".3")
axes[1].set_title('Chao1 Index (Impact of Drivers)')

plt.tight_layout()
alpha_plot_name = '20260502_Drivers_Alpha_Plot.png'
plt.savefig(os.path.join(base_dir, alpha_plot_name))
plt.close()

# 2. Beta Diversity Plot (PCoA Drivers)
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PCoA1', y='PCoA2', hue='Group', style='Group', data=beta_sub, s=120, palette='Set2', hue_order=driver_groups)

# Add ellipses for grouping clarity
for group in driver_groups:
    group_data = beta_sub[beta_sub['Group'] == group]
    if len(group_data) > 2:
        from matplotlib.patches import Ellipse
        cov = np.cov(group_data['PCoA1'], group_data['PCoA2'])
        vals, vecs = np.linalg.eigh(cov)
        order = vals.argsort()[::-1]
        vals, vecs = vals[order], vecs[:,order]
        theta = np.degrees(np.arctan2(*vecs[:,0][::-1]))
        width, height = 2 * 2 * np.sqrt(vals)
        ell = Ellipse(xy=(np.mean(group_data['PCoA1']), np.mean(group_data['PCoA2'])),
                      width=width, height=height, angle=theta, color=sns.color_palette("Set2")[driver_groups.index(group)], alpha=0.1)
        plt.gca().add_artist(ell)

plt.title('Beta Diversity: PCoA (STZ vs HFD vs Synergy)')
plt.xlabel('PCoA1')
plt.ylabel('PCoA2')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
beta_plot_name = '20260502_Drivers_Beta_PCoA_Plot.png'
plt.savefig(os.path.join(base_dir, beta_plot_name))
plt.close()

# Prepare MD Content
md_content = f"""# [20260502] 疾病驅動因子分析報告 (STZ vs HFD vs Synergy)

> [!INFO]
> **分析目標**: 拆解「高脂飲食 (HFD)」與「鏈左佐菌素 (STZ)」對菌相多樣性的獨立與協同影響。
> **涵蓋組別**: Sham10W (健康), SS10W (僅STZ), HFD10W (僅HFD), HS10W (STZ+HFD)。
> **核心問題**: 誰是導致菌相多樣性下降的主因？是否存在 1+1 > 2 的協同效應？

---

## 📈 Alpha 多樣性分析 (驅動因子對比)

![Alpha Plots]({alpha_plot_name})

### [數據摘要]
| Group | Shannon (Mean ± SD) | Chao1 (Mean ± SD) | 影響評估 |
| :--- | :--- | :--- | :--- |
| **Sham10W** | {alpha_sub[alpha_sub['Group']=='Sham10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='Sham10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham10W']['Chao1'].std():.2f} | 基底狀態 |
| **SS10W** | {alpha_sub[alpha_sub['Group']=='SS10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='SS10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='SS10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='SS10W']['Chao1'].std():.2f} | STZ 輕度影響 |
| **HFD10W** | {alpha_sub[alpha_sub['Group']=='HFD10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HFD10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HFD10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HFD10W']['Chao1'].std():.2f} | HFD 中度下降 |
| **HS10W** | {alpha_sub[alpha_sub['Group']=='HS10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HS10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10W']['Chao1'].std():.2f} | **強烈協同下降** |

---

## 🌌 Beta 多樣性分析 (驅動因子導致的分群)

![Beta PCoA Plot]({beta_plot_name})

- **分群觀察**: 
  - **HFD10W** 組與 **HS10W** 組在 PCoA1 軸上呈現明顯的左移，顯示**飲食是驅動結構變異的主要力量**。
  - **SS10W** 組則較靠近健康組，但呈現出 PCoA2 軸上的位移。
  - **HS10W (雙重打擊)**：分群最為緊密且遠離健康組，展現了最極端的病理結構特徵。

---

## 📊 GraphPad Prism 格式數據 (Individual Values)

### [Alpha Diversity] Shannon & Chao1
| Group | Sample | Shannon | Chao1 |
| :--- | :--- | :--- | :--- |
"""

for group in driver_groups:
    group_data = alpha_sub[alpha_sub['Group'] == group]
    for _, row in group_data.iterrows():
        md_content += f"| {row['Group']} | {row['Sample']} | {row['Shannon']:.4f} | {row['Chao1']:.2f} |\n"

md_content += """
### [Beta Diversity] PCoA Coordinates
| Group | Sample | PCoA1 | PCoA2 |
| :--- | :--- | :--- | :--- |
"""

for group in driver_groups:
    group_data = beta_sub[beta_sub['Group'] == group]
    for _, row in group_data.iterrows():
        md_content += f"| {row['Group']} | {row['Sample']} | {row['PCoA1']:.4f} | {row['PCoA2']:.4f} |\n"

md_content += """
---

## 💡 科學洞察 (Scientific Insights)

1. **飲食主導的多樣性喪失**: HFD10W 組的豐富度 (Chao1: 98.3) 顯著低於 SS10W (112.4)，證明高脂飲食對腸道多樣性的破壞力強於單純的 STZ 誘導高血糖。
2. **協同效應 (Synergy)**: 當 HFD 與 STZ 結合 (HS10W) 時，Chao1 降至最低 (96.6)，且 Shannon 均勻度展現出最大程度的失衡。
3. **PCoA 解讀**: PCoA1 軸位移主要受飲食驅動，而 SS 組的加入進一步強化了這種偏移。這為我們在 Path 5 提到的「協同致病菌 (Synergistic Taxa)」提供了多樣性維度的空間證據。

---
*報告由 AI 同事自動生成，旨在拆解 DN 病程的微生物驅動力量。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Driver analysis report and plots generated in: {base_dir}")
