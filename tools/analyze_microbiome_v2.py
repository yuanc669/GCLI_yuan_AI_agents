import pandas as pd
import numpy as np
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

def cmdscale(D):
    """
    Classical multidimensional scaling (MDS) / PCoA
    """
    # Number of points
    n = len(D)
    # Centering matrix
    H = np.eye(n) - np.ones((n, n))/n
    # YY^T
    B = -0.5 * H.dot(D**2).dot(H)
    # Diagonalize
    evals, evecs = np.linalg.eigh(B)
    # Sort by eigenvalue in descending order
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:,idx]
    # Compute coordinates
    w = np.where(evals > 0)
    L = np.diag(np.sqrt(evals[w]))
    V = evecs[:,w[0]]
    Y = V.dot(L)
    return Y, evals

# File paths
f1_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham_HS2W_HS6W_HS10W-1.xlsx'
f2_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'

# Load data
f1 = pd.read_excel(f1_path)
f2 = pd.read_excel(f2_path)

# Sample columns (counts)
f1_samples = ['Sham-1', 'Sham-2', 'Sham-3', 'HS2W-1', 'HS2W-2', 'HS2W-3', 'HS2W-4', 'HS2W-5', 'HS6W-1', 'HS6W-2', 'HS6W-3', 'HS6W-4', 'HS6W-5', 'HS6W-6']
f2_samples = ['Sham10W-4', 'Sham10W-5', 'Sham10W-6', 'SS10W-1', 'SS10W-2', 'SS10W-3', 'SS10W-4', 'SS10W-5', 'SS10W-6', 'HFD10W-1', 'HFD10W-2', 'HFD10W-3', 'HFD10W-4', 'HFD10W-5', 'HFD10W-6', 'HS10W-1', 'HS10W-2', 'HS10W-3', 'HS10W-4', 'HS10W-5', 'HS10W-6', 'HS10WGaE9-1', 'HS10WGaE9-2', 'HS10WGaE9-3', 'HS10WGaE9-4', 'HS10WGaE9-5', 'HS10WGaE10-1', 'HS10WGaE10-2', 'HS10WGaE10-3', 'HS10WGaE10-4', 'HS10WGaE10-5']

# Alpha Diversity
alpha_data = []
for s in f1_samples:
    alpha_data.append({'Sample': s, 'Group': s.split('-')[0], 'Shannon': calculate_shannon(f1[s].values), 'Chao1': calculate_chao1(f1[s].values)})
for s in f2_samples:
    group = s.split('-')[0]
    if 'GaE' in s: group = 'HS10WGaE9' if 'GaE9' in s else 'HS10WGaE10'
    alpha_data.append({'Sample': s, 'Group': group, 'Shannon': calculate_shannon(f2[s].values), 'Chao1': calculate_chao1(f2[s].values)})

alpha_df = pd.DataFrame(alpha_data)
alpha_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Microbiome_Alpha_Diversity.csv', index=False)

# Beta Diversity (PCoA) - use all samples from both files (if possible)
# Merging files on Taxonomy
merged = pd.merge(f1, f2, on=['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species'], how='outer').fillna(0)
all_samples = f1_samples + f2_samples
rel_cols = [c + '.1_x' if c in f1_samples else c + '.1_y' for c in all_samples]

# Wait, let's just use the count columns and normalize
counts_matrix = merged[all_samples].T
rel_matrix = counts_matrix.div(counts_matrix.sum(axis=1), axis=0)

dist_matrix = pdist(rel_matrix, metric='braycurtis')
dist_square = squareform(dist_matrix)

Y, evals = cmdscale(dist_square)
pcoa_df = pd.DataFrame(Y[:, :2], columns=['PCoA1', 'PCoA2'])
pcoa_df['Sample'] = all_samples
pcoa_df['Group'] = alpha_df['Group'].values
pcoa_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Microbiome_Beta_Diversity_PCoA.csv', index=False)

print("Alpha Diversity Summary (Mean ± STD):")
summary = alpha_df.groupby('Group')[['Shannon', 'Chao1']].agg(['mean', 'std'])
print(summary)
