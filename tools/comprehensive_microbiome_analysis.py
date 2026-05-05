import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import kruskal, mannwhitneyu
from scipy.spatial.distance import pdist, squareform
import os

# Set style
sns.set(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] # For Traditional Chinese
plt.rcParams['axes.unicode_minus'] = False

def calculate_alpha(counts_df):
    # Shannon: -sum(p * log(p))
    def shannon(x):
        p = x[x > 0] / x.sum()
        return -np.sum(p * np.log(p))
    
    # Simpson: 1 - sum(p^2)
    def simpson(x):
        p = x[x > 0] / x.sum()
        return 1 - np.sum(p**2)
    
    # Chao1: S_obs + (n1^2) / (2 * n2)
    def chao1(x):
        s_obs = np.sum(x > 0)
        n1 = np.sum(x == 1)
        n2 = np.sum(x == 2)
        if n2 == 0:
            return s_obs + n1 * (n1 - 1) / 2
        return s_obs + (n1**2) / (2 * n2)

    alpha_results = []
    for col in counts_df.columns:
        alpha_results.append({
            'Sample': col,
            'Shannon': shannon(counts_df[col]),
            'Simpson': simpson(counts_df[col]),
            'Chao1': chao1(counts_df[col])
        })
    return pd.DataFrame(alpha_results)

def perform_pcoa(rel_df, groups_map):
    # Bray-Curtis distance
    dist_matrix = pdist(rel_df.T, metric='braycurtis')
    dist_square = squareform(dist_matrix)
    
    # Manual PCoA (Classical MDS)
    n = dist_square.shape[0]
    # Double centering
    J = np.eye(n) - np.ones((n, n)) / n
    B = -0.5 * J.dot(dist_square**2).dot(J)
    
    # Eigen decomposition
    evals, evecs = np.linalg.eigh(B)
    
    # Sort eigenvalues and eigenvectors in descending order
    idx = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:, idx]
    
    # Take top 2 components
    pc1 = evecs[:, 0] * np.sqrt(np.maximum(evals[0], 0))
    pc2 = evecs[:, 1] * np.sqrt(np.maximum(evals[1], 0))
    
    pcoa_df = pd.DataFrame({'PC1': pc1, 'PC2': pc2})
    pcoa_df['Sample'] = rel_df.columns
    pcoa_df['Group'] = pcoa_df['Sample'].map(groups_map)
    return pcoa_df

def main():
    file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\AP_GiNV_Oral\L7_stool.xlsx'
    output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\screens'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    df = pd.read_excel(file_path)
    
    # Define samples and groups
    sham_cols = [f'Sham-{i}_Stool' for i in range(1, 7)]
    ap_cols = [f'AP-{i}_Stool' for i in range(1, 7)]
    gienxo_cols = [f'AP-GiExo-{i}_Stool' for i in range(1, 7)]
    
    all_count_cols = sham_cols + ap_cols + gienxo_cols
    all_rel_cols = [c + '.1' for c in all_count_cols]
    
    groups_map = {}
    for c in sham_cols: groups_map[c] = 'Sham'; groups_map[c+'.1'] = 'Sham'
    for c in ap_cols: groups_map[c] = 'AP'; groups_map[c+'.1'] = 'AP'
    for c in gienxo_cols: groups_map[c] = 'AP-GiExo'; groups_map[c+'.1'] = 'AP-GiExo'

    # 1. Alpha Diversity
    alpha_df = calculate_alpha(df[all_count_cols])
    alpha_df['Group'] = alpha_df['Sample'].map(groups_map)
    
    # Statistics for Alpha
    alpha_summary = alpha_df.drop(columns='Sample').groupby('Group').agg(['mean', 'std']).reset_index()
    
    # Kruskal-Wallis
    stats_results = {}
    for metric in ['Shannon', 'Simpson', 'Chao1']:
        g1 = alpha_df[alpha_df['Group'] == 'Sham'][metric]
        g2 = alpha_df[alpha_df['Group'] == 'AP'][metric]
        g3 = alpha_df[alpha_df['Group'] == 'AP-GiExo'][metric]
        stat, p = kruskal(g1, g2, g3)
        stats_results[metric] = p

    # 2. Beta Diversity (PCoA)
    pcoa_res = perform_pcoa(df[all_rel_cols], groups_map)
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=pcoa_res, x='PC1', y='PC2', hue='Group', style='Group', s=100)
    plt.title('PCoA (Bray-Curtis) - Stool Microbiome')
    plt.savefig(os.path.join(output_dir, 'stool_pcoa.png'), dpi=300)
    plt.close()

    # 3. Difference Analysis (AP vs AP-GiExo)
    # Ensure relative abundance columns are numeric
    for col in all_rel_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    
    df_gen = df.groupby('Genus')[all_rel_cols].sum().reset_index()
    ap_rel = [c + '.1' for c in ap_cols]
    gienxo_rel = [c + '.1' for c in gienxo_cols]
    
    df_gen['Mean_AP'] = df_gen[ap_rel].mean(axis=1)
    df_gen['Mean_GiExo'] = df_gen[gienxo_rel].mean(axis=1)
    df_gen['Diff'] = df_gen['Mean_GiExo'] - df_gen['Mean_AP']
    df_gen['FoldChange'] = df_gen['Mean_GiExo'] / (df_gen['Mean_AP'] + 1e-9)
    
    # Calculate p-values for all Genus (AP vs AP-GiExo)
    p_vals = []
    for idx, row in df_gen.iterrows():
        g1 = row[ap_rel].values.astype(float)
        g2 = row[gienxo_rel].values.astype(float)
        if np.all(g1 == g2):
            p_vals.append(1.0)
            continue
        try:
            _, p = mannwhitneyu(g1, g2)
            p_vals.append(p)
        except Exception as e:
            p_vals.append(1.0)
    df_gen['p_value'] = p_vals
    
    top_10_diff = df_gen.sort_values(by='Diff', key=abs, ascending=False).head(10)
    
    # Specific Taxa
    specific_taxa = df_gen[df_gen['Genus'].isin(['Lachnospiraceae_NK4A136_group', 'Muribaculaceae'])]

    # 4. Stacked Bar Plots
    # Genus level
    df_gen_avg = pd.DataFrame()
    df_gen_avg['Sham'] = df.groupby('Genus')[[c+'.1' for c in sham_cols]].mean().mean(axis=1)
    df_gen_avg['AP'] = df.groupby('Genus')[ap_rel].mean().mean(axis=1)
    df_gen_avg['AP-GiExo'] = df.groupby('Genus')[gienxo_rel].mean().mean(axis=1)
    
    # Keep Top 10 and group others
    top_genus = df_gen_avg.mean(axis=1).sort_values(ascending=False).head(10).index
    df_gen_plot = df_gen_avg.loc[top_genus]
    df_gen_plot.loc['Others'] = df_gen_avg.drop(top_genus).sum()
    
    # Phylum level
    df_phy_avg = pd.DataFrame()
    df_phy_avg['Sham'] = df.groupby('Phylum')[[c+'.1' for c in sham_cols]].mean().mean(axis=1)
    df_phy_avg['AP'] = df.groupby('Phylum')[ap_rel].mean().mean(axis=1)
    df_phy_avg['AP-GiExo'] = df.groupby('Phylum')[gienxo_rel].mean().mean(axis=1)
    
    top_phylum = df_phy_avg.mean(axis=1).sort_values(ascending=False).head(5).index
    df_phy_plot = df_phy_avg.loc[top_phylum]
    df_phy_plot.loc['Others'] = df_phy_avg.drop(top_phylum).sum()

    # Plotting Stacked Bar
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    df_phy_plot.T.plot(kind='bar', stacked=True, ax=axes[0], colormap='tab20')
    axes[0].set_title('Phylum Composition')
    axes[0].set_ylabel('Relative Abundance')
    
    df_gen_plot.T.plot(kind='bar', stacked=True, ax=axes[1], colormap='tab20')
    axes[1].set_title('Genus Composition (Top 10)')
    axes[1].set_ylabel('Relative Abundance')
    
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'stool_taxa_bar.png'), dpi=300)
    plt.close()

    # 5. Output Results to Markdown
    report_path = os.path.join(output_dir, 'microbiome_report.md')
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# 腸道菌相深度分析報告 (Stool Microbiome Analysis Report)\n\n")
        
        f.write("## 1. Alpha Diversity\n")
        f.write(alpha_summary.to_markdown())
        f.write("\n\n**Statistics (Kruskal-Wallis p-value):**\n")
        for m, p in stats_results.items():
            f.write(f"- {m}: {p:.4f}\n")
        
        f.write("\n## 2. Beta Diversity\n")
        f.write("PCoA 分析圖已存至 `stool_pcoa.png`。觀察各組樣本的群聚情況。\n\n")
        
        f.write("## 3. Difference Analysis (AP vs AP-GiExo)\n")
        f.write("### Top 10 Genus Differences\n")
        f.write(top_10_diff[['Genus', 'Mean_AP', 'Mean_GiExo', 'Diff', 'p_value']].to_markdown(index=False))
        
        f.write("\n### 關鍵菌屬統計\n")
        f.write(specific_taxa[['Genus', 'Mean_AP', 'Mean_GiExo', 'FoldChange', 'p_value']].to_markdown(index=False))
        
        f.write("\n## 4. 物種組成堆疊圖\n")
        f.write("堆疊圖已存至 `stool_taxa_bar.png`。\n")

    print(f"Analysis complete. Report and images saved to {output_dir}")

if __name__ == "__main__":
    main()
