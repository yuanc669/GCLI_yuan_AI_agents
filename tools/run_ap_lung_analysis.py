import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.spatial.distance import pdist, squareform

# Setup environment
sns.set_theme(style="whitegrid")
# Use a common font or default to avoid Windows-specific errors if not present, 
# but sticking to JhengHei as it was in the source.
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei', 'Arial']
plt.rcParams['axes.unicode_minus'] = False

def calculate_shannon(counts):
    counts = counts[counts > 0]
    if len(counts) == 0: return 0
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

# File path - using the one provided by user
input_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\AP_GiNV\L7_lung.xlsx'
output_dir = r'100_Research/02_Active/AP_GiNV/02_Analysis/L7_Lung_Analysis'
os.makedirs(output_dir, exist_ok=True)

df = pd.read_excel(input_path)

# Define columns
tax_cols = ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species']
# Original headers in Excel: Sham-1_Lung ... AP-1_Lung ... AP-GiExo-1_Lung
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
    # Fix terminology: GiExo -> GiNV
    group = s.split('-')[0]
    if 'GiExo' in s:
        group = 'AP-GiNV'
    elif group == 'AP':
        group = 'AP'
    else:
        group = 'Sham'
    
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
    # Group by Group and create columns for Prism
    prism_data = {}
    for g in ['Sham', 'AP', 'AP-GiNV']:
        vals = alpha_df[alpha_df['Group'] == g][metric].values
        prism_data[g] = vals
    
    # Ensure all columns have same length for DataFrame (pad with NaN)
    max_len = max(len(v) for v in prism_data.values())
    for g in prism_data:
        if len(prism_data[g]) < max_len:
            prism_data[g] = np.append(prism_data[g], [np.nan] * (max_len - len(prism_data[g])))
            
    pd.DataFrame(prism_data).to_csv(os.path.join(output_dir, f'Prism_Alpha_{metric}.csv'), index=False)

# 2. Beta Diversity (PCoA using relative abundance)
counts_matrix = df[rel_samples].T
dist_matrix = pdist(counts_matrix, metric='braycurtis')
dist_square = squareform(dist_matrix)

Y, evals = cmdscale(dist_square)
pcoa_df = pd.DataFrame(Y[:, :2], columns=['PCoA1', 'PCoA2'])
pcoa_df['Sample'] = raw_samples
pcoa_df['Group'] = alpha_df['Group'].values
pcoa_df.to_csv(os.path.join(output_dir, 'Beta_Diversity_PCoA.csv'), index=False)

# Plot PCoA
plt.figure(figsize=(10, 8))
sns.scatterplot(data=pcoa_df, x='PCoA1', y='PCoA2', hue='Group', style='Group', s=150, palette='Set1')
# Calculate variance explained
total_var = np.sum(evals[evals > 0])
pc1_var = evals[0] / total_var * 100
pc2_var = evals[1] / total_var * 100
plt.xlabel(f'PCoA1 ({pc1_var:.1f}%)')
plt.ylabel(f'PCoA2 ({pc2_var:.1f}%)')
plt.title('PCoA Plot (Bray-Curtis Distance) - Lung Microbiome')
plt.savefig(os.path.join(output_dir, 'PCoA_Lung.png'), dpi=300, bbox_inches='tight')
plt.close()

# 3. Alpha Diversity Plots
for metric in ['Shannon', 'Chao1']:
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='Group', y=metric, data=alpha_df, palette='Set2', order=['Sham', 'AP', 'AP-GiNV'])
    sns.stripplot(x='Group', y=metric, data=alpha_df, color=".3", alpha=0.5, order=['Sham', 'AP', 'AP-GiNV'])
    plt.title(f'Alpha Diversity - {metric}')
    plt.savefig(os.path.join(output_dir, f'Alpha_{metric}_Lung.png'), dpi=300, bbox_inches='tight')
    plt.close()

# 4. Composition (Top 10 Phyla)
phylum_comp = df.groupby('Phylum')[rel_samples].sum()
phylum_comp = phylum_comp.div(phylum_comp.sum(axis=0), axis=1)
top10_phyla = phylum_comp.mean(axis=1).sort_values(ascending=False).head(10).index
phylum_summary = phylum_comp.loc[top10_phyla].T
phylum_summary['Group'] = alpha_df['Group'].values
phylum_summary.to_csv(os.path.join(output_dir, 'Composition_Phylum_Top10.csv'))

# Group Mean for Phylum
phylum_mean = phylum_summary.groupby('Group').mean().reindex(['Sham', 'AP', 'AP-GiNV'])
phylum_mean.to_csv(os.path.join(output_dir, 'Prism_Phylum_Mean.csv'))

# 5. Composition (Top 30 Genera)
genus_comp = df.groupby('Genus')[rel_samples].sum()
genus_comp = genus_comp.div(genus_comp.sum(axis=0), axis=1)
top30_genera = genus_comp.mean(axis=1).sort_values(ascending=False).head(30).index
genus_summary = genus_comp.loc[top30_genera].T
genus_summary['Group'] = alpha_df['Group'].values
genus_summary.to_csv(os.path.join(output_dir, 'Composition_Genus_Top30.csv'))

# 6. Differential Abundance (AP vs AP-GiNV)
diff_list = []
for genus in top30_genera:
    ap_vals = genus_summary[genus_summary['Group'] == 'AP'][genus]
    ginv_vals = genus_summary[genus_summary['Group'] == 'AP-GiNV'][genus]
    
    mean_ap = ap_vals.mean()
    mean_ginv = ginv_vals.mean()
    
    if mean_ap > 0:
        fc = mean_ginv / mean_ap
    else:
        fc = np.inf if mean_ginv > 0 else 1.0
        
    diff_list.append({
        'Genus': genus,
        'Mean_AP': mean_ap,
        'Mean_AP_GiNV': mean_ginv,
        'Fold_Change': fc,
        'Log2FC': np.log2(fc) if fc > 0 else -np.inf
    })

diff_df = pd.DataFrame(diff_list)
diff_df.to_csv(os.path.join(output_dir, 'Differential_Genus_AP_vs_GiNV.csv'), index=False)

print(f"Analysis complete. Results saved in {output_dir}")
