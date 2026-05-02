import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# File path
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Load data
f2 = pd.read_excel(f2_path)

# Relevant samples for Path 3 (Late Stage)
sham_20w = ['Sham10W-4', 'Sham10W-5', 'Sham10W-6']
hs10w_20w = ['HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6']

# Normalize to Relative Abundance
all_s = sham_20w + hs10w_20w
df = f2[tax_cols + all_s].fillna(0)
df[all_s] = df[all_s].div(df[all_s].sum(axis=0), axis=1)

results = []
for idx, row in df.iterrows():
    vals_sham = row[sham_20w].values.astype(float)
    vals_hs10w = row[hs10w_20w].values.astype(float)
    
    mean_sham = np.mean(vals_sham)
    mean_hs10w = np.mean(vals_hs10w)
    
    # Avoid division by zero
    fc = (mean_hs10w + 1e-9) / (mean_sham + 1e-9)
    log2fc = np.log2(fc)
    
    # Statistical test
    try:
        stat, pval = ttest_ind(vals_sham, vals_hs10w)
    except:
        pval = 1.0
        
    if mean_sham > 0.001 or mean_hs10w > 0.001: # Filter low abundance
        results.append({
            'Phylum': row['Phylum'],
            'Genus': row['Genus'],
            'Species': row['Species'],
            'Mean_Sham10W': mean_sham,
            'Mean_HS10W': mean_hs10w,
            'Log2FC(HS10W/Sham10W)': log2fc,
            'P_value': pval
        })

res_df = pd.DataFrame(results).sort_values('P_value')
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path3_Microbiome_Late_Stage.csv', index=False)

print("Top 10 Late-Stage Microbiome shifts (Sham10W vs HS10W):")
print(res_df.head(10).to_string())
