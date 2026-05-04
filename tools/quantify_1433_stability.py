import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load processed proteomics data
file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Proteomics_Processed.csv'
df = pd.read_csv(file_path)

# 1. Identify all 14-3-3 isoforms
iso_1433 = df[df['Description'].str.contains('14-3-3', case=False, na=False)].copy()

# 2. Extract Replicates and Calculate Stability (CV - Coefficient of Variation)
reps = ['NormPSM_G1', 'NormPSM_G2', 'NormPSM_G3']
for col in reps:
    iso_1433[col] = pd.to_numeric(iso_1433[col], errors='coerce').fillna(0)

iso_1433['Mean'] = iso_1433[reps].mean(axis=1)
iso_1433['SD'] = iso_1433[reps].std(axis=1)
iso_1433['CV_Percent'] = (iso_1433['SD'] / iso_1433['Mean']) * 100

# Sort by abundance
iso_1433 = iso_1433.sort_values('Mean', ascending=False)

# 3. Save Prism-ready file
prism_1433 = iso_1433[['Accession', 'Description', 'NormPSM_G1', 'NormPSM_G2', 'NormPSM_G3', 'Mean', 'SD', 'CV_Percent']]
prism_1433.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_14-3-3_Stability_Prism.csv', index=False)

# 4. Visualization - Stability Bar Plot
plt.figure(figsize=(10, 6))
# Melt for seaborn
melted = iso_1433.melt(id_vars=['Accession'], value_vars=reps, var_name='Replicate', value_name='PSM')
sns.barplot(x='Accession', y='PSM', data=melted, palette='muted', capsize=.1)
plt.title('Abundance & Stability of 14-3-3 Isoforms in Garlic_NV')
plt.ylabel('Normalized PSM')
plt.xlabel('Accession')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_14-3-3_Stability_Plot.png')

print("14-3-3 targeted quantification complete.")
print(prism_1433[['Accession', 'Mean', 'CV_Percent']].head().to_string())
