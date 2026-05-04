import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load processed data
file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Proteomics_Processed.csv'
df = pd.read_csv(file_path)

# 1. Calculate Mean and SD for Prism
# Replicate columns: NormPSM_G1, NormPSM_G2, NormPSM_G3
reps = ['NormPSM_G1', 'NormPSM_G2', 'NormPSM_G3']
for col in reps:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

df['Mean'] = df[reps].mean(axis=1)
df['SD'] = df[reps].std(axis=1)
df['SEM'] = df['SD'] / np.sqrt(len(reps))

# Save Prism-ready format (Top 30)
prism_df = df.sort_values('Mean', ascending=False).head(30)[['Accession', 'Description', 'Mean', 'SD', 'SEM']]
prism_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Top30_Proteins_Prism.csv', index=False)

# 2. Visualization - Top 15 Proteins (expanded from 10)
plt.figure(figsize=(12, 8))
top_15 = df.sort_values('Mean', ascending=False).head(15)
# Clean up description for plot
top_15['Short_Desc'] = top_15['Description'].str.split(';').str[0].str[:50]

sns.barplot(x='Mean', y='Short_Desc', data=top_15, palette='viridis')
plt.errorbar(x=top_15['Mean'], y=np.arange(len(top_15)), xerr=top_15['SEM'], fmt='none', c='black', capsize=3)
plt.title('Top 15 Most Abundant Proteins in Garlic_NV')
plt.xlabel('Abundance (Normalized PSM)')
plt.ylabel('Protein Description')
plt.tight_layout()
plt.savefig(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Top15_Proteins_Bar.png')

# 3. Visualization - Functional Categories
plt.figure(figsize=(8, 8))
# Grouping by Functional_Category (from analyze_ganv_proteomics.py)
# Note: The category might be messy if not cleaned. Let's use the summary file if available or recalculate
if 'Functional_Category' in df.columns:
    cat_summary = df.groupby('Functional_Category')['Mean'].sum().sort_values(ascending=False)
    # Filter out 'Other' for better visualization of specific functions if needed, or keep it
    top_cats = cat_summary.head(8)
    if 'Other' in top_cats:
        # Move 'Other' to the end
        other_val = top_cats.pop('Other')
        top_cats['Other'] = other_val
    
    plt.pie(top_cats, labels=top_cats.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Functional Distribution of Garlic_NV Proteome')
    plt.savefig(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Functional_Pie.png')

print("Visualizations and Prism data generated.")
