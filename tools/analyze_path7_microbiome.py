import pandas as pd
import numpy as np

# File path
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Load data
f2 = pd.read_excel(f2_path)

# Sample groups for Path 7
groups = {
    'Sham10W': ['Sham10W-4', 'Sham10W-5', 'Sham10W-6'],
    'SS10W': ['SS10W-1', 'SS10W-2', 'SS10W-3', 'SS10W-4', 'SS10W-5', 'SS10W-6'],
    'HFD10W': ['HFD10W-1', 'HFD10W-2', 'HFD10W-3', 'HFD10W-4', 'HFD10W-5', 'HFD10W-6'],
    'HS10W': ['HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6'],
    'HS10WGaE9': ['HS10WGaE9-1', 'HS10WGaE9-2', 'HS10WGaE9-3', 'HS10WGaE9-4', 'HS10WGaE9-5'],
    'HS10WGaE10': ['HS10WGaE10-1', 'HS10WGaE10-2', 'HS10WGaE10-3', 'HS10WGaE10-4', 'HS10WGaE10-5']
}

all_samples = [s for g in groups.values() for s in g]
df = f2.fillna(0)
# Normalize all samples in the dataframe
df[all_samples] = df[all_samples].div(df[all_samples].sum(axis=0), axis=1)

# Species of interest (Top markers from Path 5 & 6)
target_species = [
    'UBA7173 sp900540205',
    'Lepagella sp900547755',
    'Lawsonibacter unclassified',
    'Bacteroides_H_857956 acidifaciens',
    'Acetatifactor sp011959105',
    'Kineothrix sp000403275',
    'Duncaniella muricolitica',
    'Muribaculum gordoncarteri'
]

# Helper to find row by species name (partial match for simplicity)
heatmap_data = []

for spec in target_species:
    # Try to find the exact or partial match in df['Species']
    row = df[df['Species'].str.contains(spec.split(' ')[-1], na=False)].iloc[0] if not df[df['Species'].str.contains(spec.split(' ')[-1], na=False)].empty else None
    
    if row is not None:
        row_dict = {'Species': spec}
        for g_name, g_samples in groups.items():
            row_dict[g_name] = np.mean(row[g_samples])
        heatmap_data.append(row_dict)

res_df = pd.DataFrame(heatmap_data)
res_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Path7_Microbiome_Heatmap_Data.csv', index=False)

print("Comprehensive Microbial Signature Matrix (Path 7):")
print(res_df.to_string())
