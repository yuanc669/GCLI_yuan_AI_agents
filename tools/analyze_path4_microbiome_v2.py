import pandas as pd
import numpy as np

# File path
f1_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham_HS2W_HS6W_HS10W-1.xlsx'

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Load data
f1 = pd.read_excel(f1_path)

# Sample groups
groups = {
    'Sham': ['Sham-1', 'Sham-2', 'Sham-3'],
    'HS2W': ['HS2W-1', 'HS2W-2', 'HS2W-3', 'HS2W-4', 'HS2W-5'],
    'HS6W': ['HS6W-1', 'HS6W-2', 'HS6W-3', 'HS6W-4', 'HS6W-5', 'HS6W-6'],
    'HS10W': ['HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6']
}

all_samples = groups['Sham'] + groups['HS2W'] + groups['HS6W'] + groups['HS10W']
df = f1[tax_cols + all_samples].fillna(0)
df[all_samples] = df[all_samples].div(df[all_samples].sum(axis=0), axis=1)

results = []
for idx, row in df.iterrows():
    m_sham = np.mean(row[groups['Sham']])
    m_hs2w = np.mean(row[groups['HS2W']])
    m_hs6w = np.mean(row[groups['HS6W']])
    m_hs10w = np.mean(row[groups['HS10W']])
    
    # Check for consistent trends
    is_increasing = (m_hs2w >= m_sham - 1e-5) and (m_hs6w >= m_hs2w - 1e-5) and (m_hs10w >= m_hs6w - 1e-5)
    is_decreasing = (m_hs2w <= m_sham + 1e-5) and (m_hs6w <= m_hs2w + 1e-5) and (m_hs10w <= m_hs6w + 1e-5)
    
    if m_sham > 0.001 or m_hs2w > 0.001 or m_hs6w > 0.001 or m_hs10w > 0.001:
        trend = "Fluctuating"
        if is_increasing and m_hs10w > m_sham + 0.005: trend = "Increasing"
        elif is_decreasing and m_hs10w < m_sham - 0.005: trend = "Decreasing"
        
        results.append({
            'Phylum': row['Phylum'],
            'Genus': row['Genus'],
            'Species': row['Species'],
            'Mean_Sham': m_sham,
            'Mean_HS2W': m_hs2w,
            'Mean_HS6W': m_hs6w,
            'Mean_HS10W': m_hs10w,
            'Trend': trend
        })

res_df = pd.DataFrame(results)
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path4_Microbiome_TimeCourse.csv', index=False)

print("Key Time-course Microbial Trends (Path 4):")
print(res_df[res_df['Trend'] != 'Fluctuating'].sort_values('Mean_HS10W', ascending=False).head(10).to_string())
