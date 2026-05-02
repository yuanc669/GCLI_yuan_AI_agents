import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import MDS
from scipy.spatial.distance import pdist, squareform

def calculate_shannon(counts):
    counts = counts[counts > 0]
    probs = counts / counts.sum()
    return -np.sum(probs * np.log(probs))

def calculate_chao1(counts):
    s_obs = np.sum(counts > 0)
    n1 = np.sum(counts == 1)
    n2 = np.sum(counts == 2)
    if n2 > 0:
        return s_obs + (n1**2) / (2 * n2)
    else:
        return s_obs + (n1 * (n1 - 1)) / 2

# File paths
f1_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham_HS2W_HS6W_HS10W-1.xlsx'
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Load data
f1 = pd.read_excel(f1_path)
f2 = pd.read_excel(f2_path)

# Taxonomy columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']

# Identify sample columns (counts)
f1_samples = ['Sham-1', 'Sham-2', 'Sham-3', 'HS2W-1', 'HS2W-2', 'HS2W-3', 'HS2W-4', 'HS2W-5', 'HS6W-1', 'HS6W-2', 'HS6W-3', 'HS6W-4', 'HS6W-5', 'HS6W-6']
f2_samples = ['Sham10W-4', 'Sham10W-5', 'Sham10W-6', 'SS10W-1', 'SS10W-2', 'SS10W-3', 'SS10W-4', 'SS10W-5', 'SS10W-6', 'HFD10W-1', 'HFD10W-2', 'HFD10W-3', 'HFD10W-4', 'HFD10W-5', 'HFD10W-6', 'HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6', 'HS10WGaE9-1', 'HS10WGaE9-2', 'HS10WGaE9-3', 'HS10WGaE9-4', 'HS10WGaE9-5', 'HS10WGaE10-1', 'HS10WGaE10-2', 'HS10WGaE10-3', 'HS10WGaE10-4', 'HS10WGaE10-5']

# Consolidate Alpha Diversity
alpha_data = []

# Process F1
for s in f1_samples:
    counts = f1[s].values
    alpha_data.append({
        'Sample': s,
        'Group': s.split('-')[0],
        'Shannon': calculate_shannon(counts),
        'Chao1': calculate_chao1(counts)
    })

# Process F2
for s in f2_samples:
    counts = f2[s].values
    # Clean group name
    group = s.split('-')[0]
    if 'GaE' in s:
        if 'GaE9' in s: group = 'HS10WGaE9'
        elif 'GaE10' in s: group = 'HS10WGaE10'
    
    alpha_data.append({
        'Sample': s,
        'Group': group,
        'Shannon': calculate_shannon(counts),
        'Chao1': calculate_chao1(counts)
    })

alpha_df = pd.DataFrame(alpha_data)
alpha_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Microbiome_Alpha_Diversity.csv', index=False)

# Beta Diversity (PCoA) - using Relative Abundance from F2 (most groups)
rel_cols = [c + '.1' for c in f2_samples]
matrix = f2[rel_cols].T
dist_matrix = pdist(matrix, metric='braycurtis')
dist_square = squareform(dist_matrix)

# MDS for PCoA
mds = MDS(n_components=2, dissimilarity='precomputed', random_state=42)
pos = mds.fit_transform(dist_square)

pcoa_df = pd.DataFrame(pos, columns=['PCoA1', 'PCoA2'])
pcoa_df['Sample'] = f2_samples
pcoa_df['Group'] = [alpha_df[alpha_df['Sample'] == s]['Group'].values[0] for s in f2_samples]
pcoa_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Microbiome_Beta_Diversity_PCoA.csv', index=False)

print("Alpha Diversity Summary:")
print(alpha_df.groupby('Group')[['Shannon', 'Chao1']].agg(['mean', 'std']))
