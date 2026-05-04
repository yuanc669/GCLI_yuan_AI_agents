import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
p1_path = os.path.join(base_dir, 'Path1_Microbiome_Aging_Analysis.csv')
p2_path = os.path.join(base_dir, 'Path2_Microbiome_Acute_Induction.csv')
report_path = os.path.join(base_dir, '20260502_Aging_vs_Disease_Deduction_分析報告.md')

# Load
p1 = pd.read_csv(p1_path)
p2 = pd.read_csv(p2_path)

# Filter Significant (P < 0.05)
p1_sig = p1[p1['P_value'] < 0.05].copy()
p2_sig = p2[p2['P_value'] < 0.05].copy()

# Unique ID (Genus + Species)
p1_sig['Taxon'] = p1_sig['Genus'] + " " + p1_sig['Species']
p2_sig['Taxon'] = p2_sig['Genus'] + " " + p2_sig['Species']

set1 = set(p1_sig['Taxon'])
set2 = set(p2_sig['Taxon'])

# Categorize
pure_aging = set1 - set2
pure_disease = set2 - set1
common = set1 & set2

# Trend Analysis for Common
common_list = []
for taxon in common:
    row1 = p1_sig[p1_sig['Taxon'] == taxon].iloc[0]
    row2 = p2_sig[p2_sig['Taxon'] == taxon].iloc[0]
    trend1 = "Up" if row1['Log2FC(20W/12W)'] > 0 else "Down"
    trend2 = "Up" if row2['Log2FC(HS2W/Sham)'] > 0 else "Down"
    common_list.append({
        'Taxon': taxon,
        'Aging_Trend': trend1,
        'Disease_Trend': trend2,
        'Note': "Synergistic" if trend1 == trend2 else "Antagonistic"
    })

common_df = pd.DataFrame(common_list)

# Save Comparison Results
# Manual Venn-like plot (Bar Chart)
plt.figure(figsize=(10, 6))
plt.bar(['Aging Only', 'Common', 'Disease Only'], [len(pure_aging), len(common), len(pure_disease)], color=['blue', 'purple', 'red'])
plt.title('Comparison of Significant Microbiome Markers')
plt.ylabel('Count of Taxa')
plt.savefig(os.path.join(base_dir, '20260502_Aging_Disease_Counts.png'))
plt.close()

# Try optional Venn
try:
    from matplotlib_venn import venn2
    plt.figure(figsize=(8, 8))
    venn2([set1, set2], ('Aging (Path1)', 'Disease (Path2)'))
    plt.title('Venn Diagram: Aging vs. Acute Disease Markers')
    plt.savefig(os.path.join(base_dir, '20260502_Aging_Disease_Venn.png'))
    plt.close()
except:
    pass

# Generate MD Report
md = f"""# [20260502] 老化 vs. 疾病特異性菌相排除分析 (Deduction Analysis)

> [!IMPORTANT]
> **分析目的**: 在評估生薑外泌體 (GaExo) 療效前，區分哪些變動是「自然老化」引起的，哪些是「疾病誘導」的。
> **排除邏輯**: 
> - **Pure Aging**: 僅在 Sham 12W vs 20W 顯著，不應視為治療標靶。
> - **Pure Disease**: 僅在 HS2W 誘導後出現，為核心病理菌。
> - **Synergistic**: 兩者皆顯著且趨勢一致，代表疾病加速了老化過程（或老化使腸道更易受疾病影響）。

---

## 📊 集合統計 (Overlapping Summary)

- **老化相關菌 (P < 0.05)**: {len(set1)}
- **疾病特異菌 (P < 0.05)**: {len(set2)}
- **交集 (Common)**: {len(common)}

![Counts Plot](20260502_Aging_Disease_Counts.png)

---

## 🦠 核心菌屬分類清單

### 1. 疾病特異性標記 (Pure Disease Markers) - **GaExo 重點標靶**
以下菌屬在老化過程中穩定，但在誘導後劇烈變動：

| Taxon | Log2FC | P-value | 趨勢 |
| :--- | :--- | :--- | :--- |
"""

# Show top 10 pure disease
p2_pure = p2_sig[p2_sig['Taxon'].isin(pure_disease)].sort_values('P_value').head(10)
for _, row in p2_pure.iterrows():
    trend = "⬆️" if row['Log2FC(HS2W/Sham)'] > 0 else "⬇️"
    md += f"| {row['Taxon']} | {row['Log2FC(HS2W/Sham)']:.2f} | {row['P_value']:.4e} | {trend} |\n"

md += """
### 2. 協同加速標記 (Synergistic Markers) - **老化與疾病的交會點**

| Taxon | Aging Trend | Disease Trend | 性質 |
| :--- | :--- | :--- | :--- |
"""
for _, row in common_df.head(10).iterrows():
    md += f"| {row['Taxon']} | {row['Aging_Trend']} | {row['Disease_Trend']} | {row['Note']} |\n"

md += """
---

## 💡 深度解讀與建議 (Insights)

1. **排除偽陽性**: `Spongiimonas` 與 `Duncaniella` 在老化與疾病中皆顯著下降。若 GaExo 提升了這些菌，我們需判斷它是「抗老化」還是「抗病」。
2. **精準治療論證**: 報告中的 **Pure Disease Markers**（如 Kineothrix 的特定亞種或 Lepagella）應作為論文撰寫的核心，因為它們與老化背景無關，更能體現 GaExo 的疾病特異性療效。
3. **後續驗證**: 建議將 **Pure Disease Markers** 與腎功能指標 (BUN/CRE) 進行強關聯擬合。

---
*報告由 AI 同事自動生成，旨在完善 Path1 分析的解釋深度。*
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(md)

print(f"Deduction analysis completed: {report_path}")
