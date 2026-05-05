import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import pdist, squareform

# Setup environment
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
input_path = r'_inbox/AP_GiNV_Oral/L7_lung.xlsx'
output_dir = r'100_Research/02_Active/AP_GiNV/02_Analysis/L7_Lung_Analysis'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_excel(input_path)

# Define columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
raw_samples = [
    'Sham-1_Lung', 'Sham-2_Lung', 'Sham-3_Lung', 'Sham-4_Lung', 'Sham-5_Lung', 'Sham-6_Lung',
    'AP-1_Lung', 'AP-2_Lung', 'AP-3_Lung', 'AP-4_Lung', 'AP-5_Lung', 'AP-6_Lung',
    'AP-GiExo-1_Lung', 'AP-GiExo-2_Lung', 'AP-GiExo-3_Lung', 'AP-GiExo-4_Lung', 'AP-GiExo-5_Lung', 'AP-GiExo-6_Lung'
]
rel_samples = [s + '.1' for s in raw_samples]

# 1. Alpha Diversity (using raw counts)
alpha_list = []
for i, s in enumerate(raw_samples):
    counts = df[s].values
    group = s.split('-')[0]
    if group == 'AP':
        if 'GiExo' in s:
            group = 'AP-GiExo'
        else:
            group = 'AP'
    
    alpha_list.append({
        'Sample': s,
        'Group': group,
        'Shannon': calculate_shannon(counts),
        'Chao1': calculate_chao1(counts),
        'Observed_OTUs': np.sum(counts > 0)
    })

alpha_df = pd.DataFrame(alpha_list)
alpha_df.to_csv(os.path.join(output_dir, 'Alpha_Diversity.csv'), index=False)

# Prism format for Alpha Diversity
for metric in ['Shannon', 'Chao1', 'Observed_OTUs']:
    prism_alpha = alpha_df.pivot(index='Sample', columns='Group', values=metric)
    # Reorder columns
    cols = [c for c in ['Sham', 'AP', 'AP-GiExo'] if c in prism_alpha.columns]
    prism_alpha[cols].to_csv(os.path.join(output_dir, f'Prism_Alpha_{metric}.csv'))

# 2. Beta Diversity (PCoA using relative abundance)
rel_df = df[tax_cols + rel_samples].copy()
counts_matrix = rel_df[rel_samples].T
dist_matrix = pdist(counts_matrix, metric='braycurtis')
dist_square = squareform(dist_matrix)

Y, evals = cmdscale(dist_square)
pcoa_df = pd.DataFrame(Y[:, :2], columns=['PCoA1', 'PCoA2'])
pcoa_df['Sample'] = raw_samples
pcoa_df['Group'] = alpha_df['Group'].values
pcoa_df.to_csv(os.path.join(output_dir, 'Beta_Diversity_PCoA.csv'), index=False)

# Plot PCoA
plt.figure(figsize=(10, 8))
sns.scatterplot(data=pcoa_df, x='PCoA1', y='PCoA2', hue='Group', style='Group', s=100, palette='Set1')
plt.title('PCoA Plot (Bray-Curtis Distance) - Lung Microbiome')
plt.savefig(os.path.join(output_dir, 'PCoA_Lung.png'))
plt.close()

# 3. Alpha Diversity Plots
for metric in ['Shannon', 'Chao1']:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Group', y=metric, data=alpha_df, palette='Set2', order=['Sham', 'AP', 'AP-GiExo'])
    sns.stripplot(x='Group', y=metric, data=alpha_df, color=".3", alpha=0.5, order=['Sham', 'AP', 'AP-GiExo'])
    plt.title(f'Alpha Diversity - {metric}')
    plt.savefig(os.path.join(output_dir, f'Alpha_{metric}_Lung.png'))
    plt.close()

# 4. Composition (Top 10 Phyla)
phylum_comp = df.groupby('Phylum')[rel_samples].sum()
# Normalize to 1 again just in case
phylum_comp = phylum_comp.div(phylum_comp.sum(axis=0), axis=1)
top10_phyla = phylum_comp.mean(axis=1).sort_values(ascending=False).head(10).index
phylum_summary = phylum_comp.loc[top10_phyla].T
phylum_summary['Group'] = alpha_df['Group'].values
phylum_summary.to_csv(os.path.join(output_dir, 'Composition_Phylum_Top10.csv'))

# Group Mean for Phylum
phylum_mean = phylum_summary.groupby('Group').mean()
phylum_mean.to_csv(os.path.join(output_dir, 'Prism_Phylum_Mean.csv'))

# 4. Composition (Top 30 Genera)
genus_comp = df.groupby('Genus')[rel_samples].sum()
genus_comp = genus_comp.div(genus_comp.sum(axis=0), axis=1)
top30_genera = genus_comp.mean(axis=1).sort_values(ascending=False).head(30).index
genus_summary = genus_comp.loc[top30_genera].T
genus_summary['Group'] = alpha_df['Group'].values
genus_summary.to_csv(os.path.join(output_dir, 'Composition_Genus_Top30.csv'))

# 5. Differential Abundance (Simple Fold Change / T-test for AP vs AP-GiExo)
# We will identify Genus that are significantly different
diff_list = []
for genus in top30_genera:
    ap_vals = genus_summary[genus_summary['Group'] == 'AP'][genus]
    giexo_vals = genus_summary[genus_summary['Group'] == 'AP-GiExo'][genus]
    
    mean_ap = ap_vals.mean()
    mean_giexo = giexo_vals.mean()
    
    if mean_ap > 0:
        fc = mean_giexo / mean_ap
    else:
        fc = np.inf
        
    diff_list.append({
        'Genus': genus,
        'Mean_AP': mean_ap,
        'Mean_GiExo': mean_giexo,
        'Fold_Change': fc
    })

diff_df = pd.DataFrame(diff_list)
diff_df.to_csv(os.path.join(output_dir, 'Differential_Genus_AP_vs_GiExo.csv'), index=False)

print(f"Analysis complete. Results saved in {output_dir}")
