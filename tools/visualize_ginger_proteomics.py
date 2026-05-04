import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Paths
processed_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\GingerNV_Proteomics_Full_Analysis.csv'
figure_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\03_Figures_Tables'
os.makedirs(figure_dir, exist_ok=True)

try:
    df = pd.read_csv(processed_file)

    # 1. Top 15 Proteins Bar Chart
    plt.figure(figsize=(12, 8))
    top_15 = df.sort_values('AVERAGE_NormPSM', ascending=False).head(15)
    top_15['Short_Desc'] = top_15['Description'].str.split(';').str[0].str[:50]

    sns.barplot(x='AVERAGE_NormPSM', y='Short_Desc', data=top_15, palette='magma')
    plt.errorbar(x=top_15['AVERAGE_NormPSM'], y=np.arange(len(top_15)), xerr=top_15['SEM_NormPSM'], fmt='none', c='black', capsize=3)
    plt.title('Top 15 Most Abundant Proteins in Ginger_NV')
    plt.xlabel('Abundance (Normalized PSM)')
    plt.ylabel('Protein Description')
    plt.tight_layout()
    plt.savefig(os.path.join(figure_dir, 'GingerNV_Top15_Proteins_Bar.png'))
    plt.close()

    # 2. Functional Distribution Pie Chart
    plt.figure(figsize=(10, 8))
    cat_summary = df.groupby('Functional_Category')['AVERAGE_NormPSM'].sum().sort_values(ascending=False)
    top_cats = cat_summary.head(8)
    
    # Move 'Other' to end if present
    if 'Other' in top_cats:
        other_val = top_cats.pop('Other')
        top_cats['Other'] = other_val
    
    plt.pie(top_cats, labels=top_cats.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('Set3'))
    plt.title('Functional Distribution of Ginger_NV Proteome')
    plt.savefig(os.path.join(figure_dir, 'GingerNV_Functional_Pie.png'))
    plt.close()

    print(f"Visualizations saved to {figure_dir}")

except Exception as e:
    print(f"Error: {e}")
