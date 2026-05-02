import pandas as pd
import numpy as np

# File path
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Load data
f2 = pd.read_excel(f2_path)

# Sample groups for Path 5
groups = {
    'Sham10W': ['Sham10W-4', 'Sham10W-5', 'Sham10W-6'],
    'SS10W': ['SS10W-1', 'SS10W-2', 'SS10W-3', 'SS10W-4', 'SS10W-5', 'SS10W-6'],
    'HFD10W': ['HFD10W-1', 'HFD10W-2', 'HFD10W-3', 'HFD10W-4', 'HFD10W-5', 'HFD10W-6'],
    'HS10W': ['HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6']
}

all_samples = groups['Sham10W'] + groups['SS10W'] + groups['HFD10W'] + groups['HS10W']
df = f2[tax_cols + all_samples].fillna(0)
df[all_samples] = df[all_samples].div(df[all_samples].sum(axis=0), axis=1)

results = []
for idx, row in df.iterrows():
    m_sham = np.mean(row[groups['Sham10W']])
    m_ss = np.mean(row[groups['SS10W']])
    m_hfd = np.mean(row[groups['HFD10W']])
    m_hs = np.mean(row[groups['HS10W']])
    
    # Identify driver type
    driver = "None"
    if m_hs > m_sham + 0.005:
        if m_ss > m_sham + 0.005 and m_hfd < m_sham + 0.005: driver = "STZ-Driven"
        elif m_hfd > m_sham + 0.005 and m_ss < m_sham + 0.005: driver = "HFD-Driven"
        elif m_hs > max(m_ss, m_hfd) + 0.005: driver = "Synergistic (1+1>2)"
    elif m_hs < m_sham - 0.005:
        if m_ss < m_sham - 0.005 and m_hfd > m_sham - 0.005: driver = "STZ-Inhibited"
        elif m_hfd < m_sham - 0.005 and m_ss > m_sham - 0.005: driver = "HFD-Inhibited"
        elif m_hs < min(m_ss, m_hfd) - 0.005: driver = "Synergistic Inhibition"

    if driver != "None":
        results.append({
            'Phylum': row['Phylum'],
            'Genus': row['Genus'],
            'Species': row['Species'],
            'Mean_Sham': m_sham,
            'Mean_SS': m_ss,
            'Mean_HFD': m_hfd,
            'Mean_HS': m_hs,
            'Driver_Category': driver
        })

res_df = pd.DataFrame(results)
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path5_Microbiome_Drivers.csv', index=False)

print("Key Driver Analysis (Path 5):")
print(res_df.sort_values('Mean_HS', ascending=False).head(10).to_string())
