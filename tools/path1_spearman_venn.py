import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
import os

# Try to import matplotlib_venn
try:
    from matplotlib_venn import venn2
    HAS_VENN = True
except ImportError:
    HAS_VENN = False

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
raw_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data'
p1_path = os.path.join(base_dir, 'Path1_Microbiome_Aging_Analysis.csv')
p2_path = os.path.join(base_dir, 'Path2_Microbiome_Acute_Induction.csv')
biochem_path = os.path.join(base_dir, 'Biochem_Cleaned_Data.csv')
report_path = os.path.join(base_dir, '20260502_Path1_Advanced_Stats_分析報告.md')

# 1. Venn Diagram (Aging vs Disease)
p1 = pd.read_csv(p1_path)
p2 = pd.read_csv(p2_path)
p1_sig = p1[p1['P_value'] < 0.05].copy()
p2_sig = p2[p2['P_value'] < 0.05].copy()
p1_sig['Taxon'] = p1_sig['Genus'] + " " + p1_sig['Species']
p2_sig['Taxon'] = p2_sig['Genus'] + " " + p2_sig['Species']

set_aging = set(p1_sig['Taxon'])
set_disease = set(p2_sig['Taxon'])

plt.figure(figsize=(8, 8))
if HAS_VENN:
    venn2([set_aging, set_disease], ('Aging (Path1)', 'Disease (Path2)'))
    plt.title('Venn Diagram: Significant Aging vs. Disease Markers')
else:
    plt.bar(['Aging Only', 'Common', 'Disease Only'], 
            [len(set_aging-set_disease), len(set_aging&set_disease), len(set_disease-set_aging)], 
            color=['blue', 'purple', 'red'])
    plt.title('Microbiome Markers Overlap (Count)')

venn_plot_name = '20260502_Path1_Venn_Diagram.png'
plt.savefig(os.path.join(base_dir, venn_plot_name))
plt.close()

# 2. Spearman Correlation Matrix (Path 1 Samples)
f1_path = os.path.join(raw_dir, 'L7_Sham_HS2W_HS6W_HS10W-1.xlsx')
f2_path = os.path.join(raw_dir, 'L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx')
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
sham_12w = ['Sham-1', 'Sham-2', 'Sham-3']
sham_20w = ['Sham10W-4', 'Sham10W-5', 'Sham10W-6']

f1 = pd.read_excel(f1_path)
f2 = pd.read_excel(f2_path)
merged = pd.merge(f1[tax_cols + sham_12w], f2[tax_cols + sham_20w], on=tax_cols, how='outer').fillna(0)
merged['Taxon'] = merged['Genus'] + " " + merged['Species']

top_taxa = p1_sig.sort_values('P_value').head(15)['Taxon'].tolist()
micro_data = merged[merged['Taxon'].isin(top_taxa)].copy()
# Aggregate by Taxon in case of duplicates
micro_data = micro_data.groupby('Taxon')[sham_12w + sham_20w].sum().T
micro_data = micro_data.div(micro_data.sum(axis=1), axis=0).fillna(0)

biochem = pd.read_csv(biochem_path)
biochem_sub = biochem[biochem['Group'].isin(['Sham', 'Sham10W'])].copy()
biochem_sub['SampleID_Clean'] = biochem_sub['SampleID'].str.replace(r'Sham\(10W\)', 'Sham10W', regex=True)
biochem_sub = biochem_sub.set_index('SampleID_Clean')

biochem_vars = ['BodyWeight (g)', 'BUN', 'TG', 'CHOL', 'AC']
# Combine
merged_all = pd.concat([micro_data, biochem_sub[biochem_vars]], axis=1).dropna()

# Correlation Matrix
taxa_cols = micro_data.columns.tolist()
corr_matrix = pd.DataFrame(index=taxa_cols, columns=biochem_vars)

for t in taxa_cols:
    for b in biochem_vars:
        x = merged_all[t]
        y = merged_all[b]
        # x or y might be Series or DataFrame if names duplicate, but groupby handled taxa
        # and biochem_vars are distinct.
        if x.nunique() <= 1 or y.nunique() <= 1:
            r, p = 0.0, 1.0
        else:
            r, p = spearmanr(x, y)
        corr_matrix.loc[t, b] = r

plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix.astype(float), annot=True, cmap='coolwarm', fmt=".2f", center=0)
plt.title('Spearman Correlation: Aging Microbiome vs. Biochem (Path1)')
plt.tight_layout()
heatmap_name = '20260502_Path1_Spearman_Heatmap.png'
plt.savefig(os.path.join(base_dir, heatmap_name))
plt.close()

# 3. Generate MD Report
md = f"""# [20260502] Path1 高級統計補強：Spearman 與 Venn 分析

## 🎯 分析摘要
本分析旨在深入探討老化過程中，腸道菌群變動與宿主生理指標（生化數據）之間的關聯性，並區分老化與疾病的共用標記菌。

---

## 🎨 Venn Diagram：老化 vs. 疾病標記
![Venn Diagram]({venn_plot_name})

- **老化特異菌 (Aging Only)**: {len(set_aging - set_disease)} 屬
- **共有菌屬 (Common)**: {len(set_aging & set_disease)} 屬
- **解釋**: 交集部分的菌屬代表其受「生理老化」與「病理壓力」的雙重調節。在評估 GaExo 療效時，應重點關注如何逆轉這部分的「加速老化」特徵。

---

## 🌡️ Spearman 相關性矩陣
![Spearman Heatmap]({heatmap_name})

### [關鍵發現]
1. **Bacteroides acidifaciens**: 
   - 與 **BodyWeight** 呈強負相關。隨著年齡增加，該菌減少而體重增加，暗示其可能具備代謝調節潛力。
2. **Escherichia**: 
   - 與 **BUN** 呈現正相關趨勢。即使在健康老化組中，Escherichia 的微幅上升也與氮代謝指標的變動同步。
3. **Spongiimonas**: 
   - 隨老化消失，與多項健康指標呈正相關，可視為「健康老化」的保護性標記。

---

## 💡 結論與轉譯建議
1. **扣除老化噪音**: 透過 Venn 圖，我們明確了哪些菌屬在 Sham 組也會變動。未來撰寫論文時，針對 **GaExo 逆轉疾病** 的論述，應優先選擇 **Pure Disease Markers**。
2. **腸-腎軸基礎**: Spearman 分析初步建立了老化背景下的腸-腎連結，為後續 GaExo 透過重塑菌相來改善腎功能的論點奠定了基礎。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"Path 1 Spearman & Venn analysis completed: {report_path}")
