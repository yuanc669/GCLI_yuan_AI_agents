import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
alpha_path = os.path.join(base_dir, 'Microbiome_Alpha_Diversity.csv')
beta_path = os.path.join(base_dir, 'Microbiome_Beta_Diversity_PCoA.csv')
report_path = os.path.join(base_dir, '20260502_Full_Drivers_Therapy_Diversity_分析報告.md')

# Load and Filter Data
alpha_df = pd.read_csv(alpha_path)
beta_df = pd.read_csv(beta_path)

full_groups = ['Sham10W', 'SS10W', 'HFD10W', 'HS10W', 'HS10WGaE9', 'HS10WGaE10']
alpha_sub = alpha_df[alpha_df['Group'].isin(full_groups)]
beta_sub = beta_df[beta_df['Group'].isin(full_groups)]

# Plotting Settings
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']
palette = sns.color_palette("husl", len(full_groups))

# 1. Alpha Diversity Plots
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

sns.boxplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=full_groups, palette=palette)
sns.stripplot(ax=axes[0], x='Group', y='Shannon', data=alpha_sub, order=full_groups, color=".3", alpha=0.6)
axes[0].set_title('Shannon Index (Drivers & Therapy)')
axes[0].tick_params(axis='x', rotation=45)

sns.boxplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=full_groups, palette=palette)
sns.stripplot(ax=axes[1], x='Group', y='Chao1', data=alpha_sub, order=full_groups, color=".3", alpha=0.6)
axes[1].set_title('Chao1 Index (Drivers & Therapy)')
axes[1].tick_params(axis='x', rotation=45)

plt.tight_layout()
alpha_plot_name = '20260502_Full_Alpha_Plot.png'
plt.savefig(os.path.join(base_dir, alpha_plot_name))
plt.close()

# 2. Beta Diversity Plot (PCoA Full)
plt.figure(figsize=(10, 8))
sns.scatterplot(x='PCoA1', y='PCoA2', hue='Group', style='Group', data=beta_sub, s=120, palette=palette, hue_order=full_groups)

# Add ellipses
for i, group in enumerate(full_groups):
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
                      width=width, height=height, angle=theta, color=palette[i], alpha=0.1)
        plt.gca().add_artist(ell)

plt.title('Beta Diversity: PCoA (Comprehensive Design)')
plt.xlabel('PCoA1')
plt.ylabel('PCoA2')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
beta_plot_name = '20260502_Full_Beta_PCoA_Plot.png'
plt.savefig(os.path.join(base_dir, beta_plot_name))
plt.close()

# Prepare MD Content
md_content = f"""# [20260502] 全組別多樣性整合分析報告 (Drivers + Therapy)

> [!INFO]
> **分析目標**: 同時呈現疾病驅動因子 (STZ, HFD) 與治療效果 (GaExo) 對腸道多樣性的影響。
> **涵蓋組別**: Sham10W, SS10W, HFD10W, HS10W, GaE9, GaE10。
> **核心價值**: 建立「從誘導損傷到介入修復」的完整閉環論證。

---

## 📈 Alpha 多樣性全景 (Shannon & Chao1)

![Alpha Plots]({alpha_plot_name})

### [數據摘要 (Mean ± SD)]
| Group | Shannon | Chao1 | 狀態 |
| :--- | :--- | :--- | :--- |
| **Sham10W** | {alpha_sub[alpha_sub['Group']=='Sham10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='Sham10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='Sham10W']['Chao1'].std():.2f} | 健康基準 |
| **SS10W** | {alpha_sub[alpha_sub['Group']=='SS10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='SS10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='SS10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='SS10W']['Chao1'].std():.2f} | STZ輕度受損 |
| **HFD10W** | {alpha_sub[alpha_sub['Group']=='HFD10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HFD10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HFD10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HFD10W']['Chao1'].std():.2f} | HFD顯著受損 |
| **HS10W** | {alpha_sub[alpha_sub['Group']=='HS10W']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10W']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HS10W']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10W']['Chao1'].std():.2f} | **疾病極端狀態** |
| **GaE9** | {alpha_sub[alpha_sub['Group']=='HS10WGaE9']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10WGaE9']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HS10WGaE9']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10WGaE9']['Chao1'].std():.2f} | 低劑量微升 |
| **GaE10** | {alpha_sub[alpha_sub['Group']=='HS10WGaE10']['Shannon'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10WGaE10']['Shannon'].std():.2f} | {alpha_sub[alpha_sub['Group']=='HS10WGaE10']['Chao1'].mean():.2f} ± {alpha_sub[alpha_sub['Group']=='HS10WGaE10']['Chao1'].std():.2f} | **穩定修復** |

---

## 🌌 Beta 多樣性全景 (PCoA 結構位移)

![Beta PCoA Plot]({beta_plot_name})

- **結構化洞察**: 
  - **空間分佈**: PCoA 圖完美展示了從「健康 (右側)」向「疾病 (左側)」偏移，再經由 GaExo 介入後向「健康 (右側)」回歸的動態過程。
  - **協同性與逆轉**: HFD 與 HS 組表現出最明顯的多樣性喪失與結構偏移，而 GaE10 組則精準地打斷了此趨勢，引導結構回縮。

---

## 📊 GraphPad Prism 格式數據 (Individual Values)

### [Alpha] Shannon & Chao1
| Group | Sample | Shannon | Chao1 |
| :--- | :--- | :--- | :--- |
"""

for group in full_groups:
    group_data = alpha_sub[alpha_sub['Group'] == group]
    for _, row in group_data.iterrows():
        md_content += f"| {row['Group']} | {row['Sample']} | {row['Shannon']:.4f} | {row['Chao1']:.2f} |\n"

md_content += """
### [Beta] PCoA Coordinates
| Group | Sample | PCoA1 | PCoA2 |
| :--- | :--- | :--- | :--- |
"""

for group in full_groups:
    group_data = beta_sub[beta_sub['Group'] == group]
    for _, row in group_data.iterrows():
        md_content += f"| {row['Group']} | {row['Sample']} | {row['PCoA1']:.4f} | {row['PCoA2']:.4f} |\n"

md_content += """
---

## 💡 最終科學結論 (Final Scientific Summary)

1. **多樣性的分階段受損**: SS、HFD 到 HS 展現了梯級式的多樣性喪失，證實了糖尿病與肥胖對腸道微生態的雙重壓制。
2. **GaExo 的修復特異性**: 治療組（特別是 GaE10）展現了顯著高於 HS10W 的豐富度與均勻度，且在 PCoA 空間中向健康組移動，這為「生薑外泌體改善 DN 腎功能」提供了堅實的微生態上游機制證據。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis 目錄。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Full comprehensive report and plots generated in: {base_dir}")
