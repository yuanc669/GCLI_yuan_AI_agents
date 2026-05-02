import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# File path
f1_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham_HS2W_HS6W_HS10W-1.xlsx'

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Load data
f1 = pd.read_excel(f1_path)

# Relevant samples for Path 2
sham_12w = ['Sham-1', 'Sham-2', 'Sham-3']
hs2w_12w = ['HS2W-1', 'HS2W-2', 'HS2W-3', 'HS2W-4', 'HS2W-5']

# Normalize to Relative Abundance
all_s = sham_12w + hs2w_12w
df = f1[tax_cols + all_s].fillna(0)
df[all_s] = df[all_s].div(df[all_s].sum(axis=0), axis=1)

results = []
for idx, row in df.iterrows():
    vals_sham = row[sham_12w].values.astype(float)
    vals_hs2w = row[hs2w_12w].values.astype(float)
    
    mean_sham = np.mean(vals_sham)
    mean_hs2w = np.mean(vals_hs2w)
    
    # Avoid division by zero
    fc = (mean_hs2w + 1e-9) / (mean_sham + 1e-9)
    log2fc = np.log2(fc)
    
    # Statistical test
    try:
        stat, pval = ttest_ind(vals_sham, vals_hs2w)
    except:
        pval = 1.0
        
    if mean_sham > 0.001 or mean_hs2w > 0.001: # Filter low abundance
        results.append({
            'Phylum': row['Phylum'],
            'Genus': row['Genus'],
            'Species': row['Species'],
            'Mean_Sham': mean_sham,
            'Mean_HS2W': mean_hs2w,
            'Log2FC(HS2W/Sham)': log2fc,
            'P_value': pval
        })

res_df = pd.DataFrame(results).sort_values('P_value')
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path2_Microbiome_Acute_Induction.csv', index=False)

print("Top 10 Acute Microbiome shifts (Sham vs HS2W):")
print(res_df.head(10).to_string())
