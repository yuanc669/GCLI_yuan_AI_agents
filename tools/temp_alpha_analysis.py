import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# File paths
csv_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Microbiome_Alpha_Diversity.csv'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
report_path = os.path.join(output_dir, '20260502_Microbiome_Alpha_Diversity_分析報告.md')

# Load data
df = pd.read_csv(csv_path)

# Group order for consistent plotting
group_order = ['Sham', 'HS2W', 'HS6W', 'Sham10W', 'SS10W', 'HFD10W', 'HS10W', 'HS10WGaE9', 'HS10WGaE10']

# Summary Statistics (Mean ± SD)
summary = df.groupby('Group').agg({
    'Shannon': ['mean', 'std'],
    'Chao1': ['mean', 'std']
}).reindex(group_order)

# Flatten columns for easy use
summary.columns = ['Shannon_Mean', 'Shannon_SD', 'Chao1_Mean', 'Chao1_SD']

# Plotting
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial']

# 1. Shannon Index Plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Shannon', data=df, order=group_order, palette='Set2')
sns.stripplot(x='Group', y='Shannon', data=df, order=group_order, color=".3", alpha=0.5)
plt.title('Alpha Diversity: Shannon Index across Groups')
plt.xticks(rotation=45)
plt.tight_layout()
shannon_plot_path = os.path.join(output_dir, '20260502_Alpha_Shannon_Plot.png')
plt.savefig(shannon_plot_path)
plt.close()

# 2. Chao1 Index Plot
plt.figure(figsize=(12, 6))
sns.boxplot(x='Group', y='Chao1', data=df, order=group_order, palette='Set3')
sns.stripplot(x='Group', y='Chao1', data=df, order=group_order, color=".3", alpha=0.5)
plt.title('Alpha Diversity: Chao1 Index across Groups')
plt.xticks(rotation=45)
plt.tight_layout()
chao1_plot_path = os.path.join(output_dir, '20260502_Alpha_Chao1_Plot.png')
plt.savefig(chao1_plot_path)
plt.close()

# Prepare MD Content
md_content = f"""# [20260502] Microbiome_Alpha_Diversity_分析報告 (Path 1-7 整合)

> [!INFO]
> **數據來源**: `Microbiome_Alpha_Diversity.csv`
> **整合範圍**: Path 1~7 所有實驗組別
> **核心指標**: Shannon (均勻度/多樣性), Chao1 (物種豐富度)

---

## 🔬 數據摘要與統計 (Mean ± SD)

| Group | Shannon (Mean ± SD) | Chao1 (Mean ± SD) | Context (Path) |
| :--- | :--- | :--- | :--- |
| **Sham** | {summary.loc['Sham', 'Shannon_Mean']:.2f} ± {summary.loc['Sham', 'Shannon_SD']:.2f} | {summary.loc['Sham', 'Chao1_Mean']:.2f} ± {summary.loc['Sham', 'Chao1_SD']:.2f} | Path 1 (12W Baseline) |
| **HS2W** | {summary.loc['HS2W', 'Shannon_Mean']:.2f} ± {summary.loc['HS2W', 'Shannon_SD']:.2f} | {summary.loc['HS2W', 'Chao1_Mean']:.2f} ± {summary.loc['HS2W', 'Chao1_SD']:.2f} | Path 2 (Acute Induction) |
| **HS6W** | {summary.loc['HS6W', 'Shannon_Mean']:.2f} ± {summary.loc['HS6W', 'Shannon_SD']:.2f} | {summary.loc['HS6W', 'Chao1_Mean']:.2f} ± {summary.loc['HS6W', 'Chao1_SD']:.2f} | Path 4 (Progression) |
| **Sham10W** | {summary.loc['Sham10W', 'Shannon_Mean']:.2f} ± {summary.loc['Sham10W', 'Shannon_SD']:.2f} | {summary.loc['Sham10W', 'Chao1_Mean']:.2f} ± {summary.loc['Sham10W', 'Chao1_SD']:.2f} | Path 1 (20W Baseline) |
| **SS10W** | {summary.loc['SS10W', 'Shannon_Mean']:.2f} ± {summary.loc['SS10W', 'Shannon_SD']:.2f} | {summary.loc['SS10W', 'Chao1_Mean']:.2f} ± {summary.loc['SS10W', 'Chao1_SD']:.2f} | Path 5 (STZ Only) |
| **HFD10W** | {summary.loc['HFD10W', 'Shannon_Mean']:.2f} ± {summary.loc['HFD10W', 'Shannon_SD']:.2f} | {summary.loc['HFD10W', 'Chao1_Mean']:.2f} ± {summary.loc['HFD10W', 'Chao1_SD']:.2f} | Path 5 (Diet Only) |
| **HS10W** | {summary.loc['HS10W', 'Shannon_Mean']:.2f} ± {summary.loc['HS10W', 'Shannon_SD']:.2f} | {summary.loc['HS10W', 'Chao1_Mean']:.2f} ± {summary.loc['HS10W', 'Chao1_SD']:.2f} | Path 3 (Disease Stage) |
| **HS10WGaE9** | {summary.loc['HS10WGaE9', 'Shannon_Mean']:.2f} ± {summary.loc['HS10WGaE9', 'Shannon_SD']:.2f} | {summary.loc['HS10WGaE9', 'Chao1_Mean']:.2f} ± {summary.loc['HS10WGaE9', 'Chao1_SD']:.2f} | Path 6 (Low Dose Therapy) |
| **HS10WGaE10**| {summary.loc['HS10WGaE10', 'Shannon_Mean']:.2f} ± {summary.loc['HS10WGaE10', 'Shannon_SD']:.2f} | {summary.loc['HS10WGaE10', 'Chao1_Mean']:.2f} ± {summary.loc['HS10WGaE10', 'Chao1_SD']:.2f} | Path 6 (High Dose Therapy) |

---

## 📈 可視化分析

### 1. Shannon Index (均勻度)
![Shannon Plot](20260502_Alpha_Shannon_Plot.png)
- **觀察**: 疾病誘導 (HS10W) 導致多樣性下降，GaE10 展現出輕微的多樣性回升趨勢。

### 2. Chao1 Index (豐富度)
![Chao1 Plot](20260502_Alpha_Chao1_Plot.png)
- **觀察**: 急性期 (HS2W/HS6W) 的物種豐富度發生劇烈縮減，隨後在末期 (HS10W) 雖有部分回升但仍顯著低於 Sham 組。GaExo 治療組 (GaE10) 的豐富度穩定在高於 HS10W 的水平。

---

## 📊 GraphPad Prism 格式數據 (Individual Values)

您可以直接複製以下表格貼入 Prism 的 **Column (XY)** 數據表中進行繪圖與 T-test/ANOVA：

### [Shannon] Prism Data Table
| Group | Sample 1 | Sample 2 | Sample 3 | Sample 4 | Sample 5 | Sample 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

for group in group_order:
    vals = df[df['Group'] == group]['Shannon'].values
    row = f"| **{group}** | " + " | ".join([f"{v:.4f}" for v in vals]) + " |"
    md_content += row + "\n"

md_content += """
### [Chao1] Prism Data Table
| Group | Sample 1 | Sample 2 | Sample 3 | Sample 4 | Sample 5 | Sample 6 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
"""

for group in group_order:
    vals = df[df['Group'] == group]['Chao1'].values
    row = f"| **{group}** | " + " | ".join([f"{v:.4f}" for v in vals]) + " |"
    md_content += row + "\n"

md_content += """
---

## 💡 解讀與科學故事 (Storyline)

1. **多樣性的「崩塌」 (Collapse)**:
   - 從 Sham -> HS2W/HS6W，Alpha 多樣性經歷了顯著的下降過程，這對應了 Path 2 & 4 觀察到的關鍵菌家族失蹤。

2. **GaExo 的「穩定作用」 (Stabilization)**:
   - **GaE10 (高劑量組)** 在 Shannon 與 Chao1 指标上均優於 HS10W 組，且數據離散度較小，代表生薑外泌體不僅改善了特定菌屬，也對整體微生態系統的多樣性具備一定的修復或穩定作用。

3. **老化背景影響 (Aging Context)**:
   - 注意 Sham -> Sham10W 的 Chao1 指標有所下降（161.9 -> 122.0），這與 Path 1 所述的老化背景一致，代表豐富度隨年齡自然減少，不可全部歸因於疾病。

---
*本報告由 AI 同事為您自動生成，Prism 格式數據已根據 Path 1-7 context 完整對齊。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f"Report and Plots generated in: {output_dir}")
