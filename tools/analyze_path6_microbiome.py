import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# File path
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Load data
f2 = pd.read_excel(f2_path)

# Sample groups for Path 6
groups = {
    'Sham10W': ['Sham10W-4', 'Sham10W-5', 'Sham10W-6'],
    'HS10W': ['HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6'],
    'GaE9': ['HS10WGaE9-1', 'HS10WGaE9-2', 'HS10WGaE9-3', 'HS10WGaE9-4', 'HS10WGaE9-5'],
    'GaE10': ['HS10WGaE10-1', 'HS10WGaE10-2', 'HS10WGaE10-3', 'HS10WGaE10-4', 'HS10WGaE10-5']
}

all_samples = groups['Sham10W'] + groups['HS10W'] + groups['GaE9'] + groups['GaE10']
df = f2[tax_cols + all_samples].fillna(0)
df[all_samples] = df[all_samples].div(df[all_samples].sum(axis=0), axis=1)

results = []
for idx, row in df.iterrows():
    m_sham = np.mean(row[groups['Sham10W']])
    m_hs = np.mean(row[groups['HS10W']])
    m_gae9 = np.mean(row[groups['GaE9']])
    m_gae10 = np.mean(row[groups['GaE10']])
    
    # Statistical test (HS10W vs GaE10)
    try:
        stat, pval = ttest_ind(row[groups['HS10W']], row[groups['GaE10']])
    except:
        pval = 1.0

    # Therapy type
    therapy = "None"
    # Rescue: Decreased in HS, saved by GaE
    if m_hs < m_sham - 0.005:
        if m_gae10 > m_hs + 0.005:
            therapy = "Rescued (Dose-dependent)" if m_gae10 >= m_gae9 else "Rescued"
    # Inhibition: Increased in HS, blocked by GaE
    elif m_hs > m_sham + 0.005:
        if m_gae10 < m_hs - 0.005:
            therapy = "Inhibited (Dose-dependent)" if m_gae10 <= m_gae9 else "Inhibited"

    if therapy != "None":
        results.append({
            'Phylum': row['Phylum'],
            'Genus': row['Genus'],
            'Species': row['Species'],
            'Mean_Sham': m_sham,
            'Mean_HS': m_hs,
            'Mean_GaE9': m_gae9,
            'Mean_GaE10': m_gae10,
            'Therapy_Effect': therapy,
            'P_value(HS_vs_GaE10)': pval
        })

res_df = pd.DataFrame(results).sort_values('P_value(HS_vs_GaE10)')
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path6_Microbiome_Therapy.csv', index=False)

print("Top 10 Therapeutic Microbial Shifts (Path 6):")
print(res_df.head(10).to_string())
