import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Config
base_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV'
raw_dir = os.path.join(base_dir, '01_Raw_Data')
analysis_dir = os.path.join(base_dir, '02_Analysis')
figure_dir = os.path.join(base_dir, '03_Figures_Tables')

os.makedirs(analysis_dir, exist_ok=True)
os.makedirs(figure_dir, exist_ok=True)

samples = {
    'Ginger': '25091902-Label-free Quantification Ginger NV.xlsx',
    'Garlic': '25091902-Label-free Quantification Garlic_NV.xlsx',
    'Kale': '25091902-Label-free Quantification Kale NV.xlsx'
}

categories_map = {
    'Antioxidant': ['peroxidase', 'dismutase', 'reductase', 'glutathione', 'catalase', 'thioredoxin'],
    'Anti-stress/HSP': ['heat shock', 'hsp', 'chaperone'],
    'Lipid Metabolism': ['lipase', 'esterase', 'lipid', 'fatty acid'],
    'Defense/Immunity': ['defense', 'chitinase', 'pathogenesis', 'antimicrobial'],
    'Transport': ['transporter', 'channel', 'aquaporin', 'carrier'],
    'Protein Synthesis': ['ribosomal', 'translation', 'elongation factor'],
    'Exosome Marker': ['annexin', 'rab', 'tetraspanin', 'hsp70']
}

def categorize(desc):
    desc = str(desc).lower()
    found = []
    for cat, keywords in categories_map.items():
        if any(k in desc for k in keywords):
            found.append(cat)
    return ', '.join(found) if found else 'Other'

summary_list = []

for name, filename in samples.items():
    print(f"Processing {name}...")
    file_path = os.path.join(raw_dir, filename)
    
    # Read data
    df = pd.read_excel(file_path, skiprows=1)
    
    # Standardize columns (Targeting NormPSM columns which are .2 or similar)
    # Most files have 3 sets of 3 columns (Area, PSM, NormPSM)
    # We identify NormPSM as columns 9, 10, 11 (0-indexed)
    cols = df.columns.tolist()
    new_cols = ['Accession', 'Description', 'MW_kDa']
    # Dynamic renaming based on index
    norm_psm_indices = [9, 10, 11]
    
    df_clean = df.iloc[:, [0, 1, 2, 9, 10, 11]].copy()
    df_clean.columns = ['Accession', 'Description', 'MW_kDa', 'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    
    # Filter
    df_clean = df_clean[df_clean['Accession'].notna() & (df_clean['Accession'] != 'Accession')].copy()
    
    # Numeric
    for col in ['MW_kDa', 'NormPSM_1', 'NormPSM_2', 'NormPSM_3']:
        df_clean[col] = pd.to_numeric(df_clean[col].replace('-', np.nan), errors='coerce').fillna(0)
    
    df_clean['Mean'] = df_clean[['NormPSM_1', 'NormPSM_2', 'NormPSM_3']].mean(axis=1)
    df_clean['SD'] = df_clean[['NormPSM_1', 'NormPSM_2', 'NormPSM_3']].std(axis=1)
    df_clean['SEM'] = df_clean['SD'] / np.sqrt(3)
    
    df_clean['Functional_Category'] = df_clean['Description'].apply(categorize)
    
    # Save Individual
    df_clean.to_csv(os.path.join(analysis_dir, f'{name}_Full_Analysis.csv'), index=False)
    
    # Collect for Comparison
    cat_sum = df_clean.groupby('Functional_Category')['Mean'].sum().reset_index()
    cat_sum['Sample'] = name
    summary_list.append(cat_sum)
    
    # Individual Top 15 Plot
    plt.figure(figsize=(10, 6))
    top_15 = df_clean.sort_values('Mean', ascending=False).head(15)
    top_15['Short_Desc'] = top_15['Description'].str.split(';').str[0].str[:40]
    sns.barplot(x='Mean', y='Short_Desc', data=top_15, palette='viridis')
    plt.title(f'Top 15 Proteins - {name}')
    plt.tight_layout()
    plt.savefig(os.path.join(figure_dir, f'{name}_Top15_Bar.png'))
    plt.close()

# Comparison Plot
comp_df = pd.concat(summary_list)
plt.figure(figsize=(12, 7))
sns.barplot(x='Mean', y='Functional_Category', hue='Sample', data=comp_df)
plt.title('Functional Comparison across PDNV Samples')
plt.xlabel('Cumulative Abundance (NormPSM Sum)')
plt.tight_layout()
plt.savefig(os.path.join(figure_dir, 'PDNV_Functional_Comparison.png'))
plt.close()

print("Multi-sample Analysis Complete.")
