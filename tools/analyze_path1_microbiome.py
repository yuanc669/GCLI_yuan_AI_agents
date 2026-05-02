import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# File paths
f1_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham_HS2W_HS6W_HS10W-1.xlsx'
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Load and merge on taxonomy
f1 = pd.read_excel(f1_path)
f2 = pd.read_excel(f2_path)

# Relevant samples
sham_12w = ['Sham-1', 'Sham-2', 'Sham-3']
sham_20w = ['Sham10W-4', 'Sham10W-5', 'Sham10W-6']

# Use relative abundance if available or calculate from counts
# Let's normalize counts to be safe
merged = pd.merge(f1[tax_cols + sham_12w], f2[tax_cols + sham_20w], on=tax_cols, how='outer').fillna(0)

# Normalize to Relative Abundance
all_s = sham_12w + sham_20w
merged[all_s] = merged[all_s].div(merged[all_s].sum(axis=0), axis=1)

results = []
for idx, row in merged.iterrows():
    vals_12w = row[sham_12w].values.astype(float)
    vals_20w = row[sham_20w].values.astype(float)
    
    mean_12w = np.mean(vals_12w)
    mean_20w = np.mean(vals_20w)
    
    # Avoid division by zero
    fc = (mean_20w + 1e-9) / (mean_12w + 1e-9)
    log2fc = np.log2(fc)
    
    # Statistical test
    try:
        stat, pval = ttest_ind(vals_12w, vals_20w)
    except:
        pval = 1.0
        
    if mean_12w > 0.001 or mean_20w > 0.001: # Filter low abundance
        results.append({
            'Phylum': row['Phylum'],
            'Genus': row['Genus'],
            'Species': row['Species'],
            'Mean_12W': mean_12w,
            'Mean_20W': mean_20w,
            'Log2FC(20W/12W)': log2fc,
            'P_value': pval
        })

res_df = pd.DataFrame(results).sort_values('P_value')
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path1_Microbiome_Aging_Analysis.csv', index=False)

print("Top 10 Aging-related shifts (Sham vs Sham10W):")
print(res_df.head(10).to_string())

