import pandas as pd
import numpy as np
from scipy.spatial.distance import pdist, squareform
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

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
    n = len(D)
    H = np.eye(n) - np.ones((n, n))/n
    B = -0.5 * H.dot(D**2).dot(H)
    evals, evecs = np.linalg.eigh(B)
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:,idx]
    w = np.where(evals > 0)
    L = np.diag(np.sqrt(evals[w]))
    V = evecs[:,w[0]]
    Y = V.dot(L)
    return Y, evals

# File path
file_path = r'_inbox/AP_GiNV/L7_stool.xlsx'
output_dir = r'100_Research/02_Active/AP_GiNV/02_Analysis/Microbiome_IT_Study'
os.makedirs(output_dir, exist_ok=True)

# Load data
df = pd.read_excel(file_path)

# Extract Taxonomy and Count columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
sample_cols = [c for c in df.columns if '_Stool' in c and not c.endswith('.1') and c != 'Total']

# Identify groups
groups = []
for s in sample_cols:
    if 'Sham' in s: groups.append('Sham')
    elif 'AP-GiExo' in s: groups.append('AP-GiExo')
    elif 'AP-' in s: groups.append('AP')
    else: groups.append('Unknown')

# 1. Alpha Diversity
alpha_data = []
for i, s in enumerate(sample_cols):
    counts = df[s].values
    alpha_data.append({
        'Sample': s,
        'Group': groups[i],
        'Shannon': calculate_shannon(counts),
        'Chao1': calculate_chao1(counts),
        'Observed_OTUs': np.sum(counts > 0)
    })

alpha_df = pd.DataFrame(alpha_data)
alpha_df.to_csv(os.path.join(output_dir, 'Alpha_Diversity.csv'), index=False)

# Save for Prism
for metric in ['Shannon', 'Chao1', 'Observed_OTUs']:
    prism_df = alpha_df.pivot(index='Sample', columns='Group', values=metric)
    prism_df.to_csv(os.path.join(output_dir, f'Prism_Alpha_{metric}.csv'))

# 2. Beta Diversity (PCoA)
counts_matrix = df[sample_cols].T
rel_matrix = counts_matrix.div(counts_matrix.sum(axis=1), axis=0)
dist_matrix = pdist(rel_matrix, metric='braycurtis')
dist_square = squareform(dist_matrix)

Y, evals = cmdscale(dist_square)
pcoa_df = pd.DataFrame(Y[:, :2], columns=['PCoA1', 'PCoA2'])
pcoa_df['Sample'] = sample_cols
pcoa_df['Group'] = groups
pcoa_df.to_csv(os.path.join(output_dir, 'Beta_Diversity_PCoA.csv'), index=False)

# Plot PCoA
plt.figure(figsize=(8, 6))
sns.scatterplot(data=pcoa_df, x='PCoA1', y='PCoA2', hue='Group', s=100, palette='Set1')
plt.title('PCoA of Gut Microbiome (Bray-Curtis)')
plt.savefig(os.path.join(output_dir, 'PCoA_Stool_IT.png'))
plt.close()

# 3. Phylum Composition
phylum_sum = df.groupby('Phylum')[sample_cols].sum()
phylum_rel = phylum_sum.div(phylum_sum.sum(axis=0), axis=1)
phylum_top10 = phylum_rel.mean(axis=1).sort_values(ascending=False).head(10).index
phylum_final = phylum_rel.loc[phylum_top10]
phylum_final.loc['Others'] = 1 - phylum_final.sum()
phylum_final.to_csv(os.path.join(output_dir, 'Composition_Phylum_Top10.csv'))

# 4. Genus Analysis & Differential
genus_sum = df.groupby('Genus')[sample_cols].sum()
genus_rel = genus_sum.div(genus_sum.sum(axis=0), axis=1)

# AP vs Sham
# AP-GiExo vs AP
def get_diff(df_rel, grp1_cols, grp2_cols):
    mean1 = df_rel[grp1_cols].mean(axis=1)
    mean2 = df_rel[grp2_cols].mean(axis=1)
    fc = (mean2 + 0.0001) / (mean1 + 0.0001)
    log2fc = np.log2(fc)
    return pd.DataFrame({'Mean1': mean1, 'Mean2': mean2, 'Log2FC': log2fc})

sham_cols = [s for s in sample_cols if 'Sham' in s]
ap_cols = [s for s in sample_cols if 'AP-' in s and 'GiExo' not in s]
giexo_cols = [s for s in sample_cols if 'GiExo' in s]

diff_ap_sham = get_diff(genus_rel, sham_cols, ap_cols)
diff_giexo_ap = get_diff(genus_rel, ap_cols, giexo_cols)

diff_ap_sham.to_csv(os.path.join(output_dir, 'Diff_Genus_AP_vs_Sham.csv'))
diff_giexo_ap.to_csv(os.path.join(output_dir, 'Diff_Genus_GiExo_vs_AP.csv'))

print("Analysis complete. Results saved to:", output_dir)
