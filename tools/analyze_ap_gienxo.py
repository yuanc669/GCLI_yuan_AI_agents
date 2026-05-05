import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def process_l7_file(file_path, output_heatmap, output_prism_md, title_prefix):
    # Load data
    df = pd.read_excel(file_path)
    
    # Identify relative abundance columns (ending in .1) and Genus
    rel_cols = [c for c in df.columns if c.endswith('.1') and not c.startswith('Total')]
    genus_col = 'Genus'
    
    # Filter columns
    df_rel = df[[genus_col] + rel_cols].copy()
    
    # Handle duplicates by summing (sometimes the same genus appears twice)
    df_rel = df_rel.groupby(genus_col).sum().reset_index()
    
    # Calculate average abundance for sorting
    df_rel['Mean_Abundance'] = df_rel[rel_cols].mean(axis=1)
    
    # Filter Top 20
    top_20 = df_rel.nlargest(20, 'Mean_Abundance')
    top_20_genera = top_20[genus_col].tolist()
    
    # Prepare data for Heatmap
    heatmap_data = top_20.set_index(genus_col)[rel_cols]
    
    # Rename columns for heatmap readability (remove .1 and suffix)
    heatmap_data.columns = [c.replace('.1', '').split('_')[0] for c in heatmap_data.columns]
    
    # Plot Heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, annot=False, cmap='YlGnBu', robust=True)
    plt.title(f'Top 20 Genus Abundance - {title_prefix}')
    plt.tight_layout()
    plt.savefig(output_heatmap)
    plt.close()
    
    # Prepare Prism Format Markdown
    # Groups: Sham (1-6), AP (1-6), GiExo (1-6)
    # We need to map columns to these groups correctly.
    
    prism_df = top_20[[genus_col] + rel_cols].copy()
    
    # Generate the Markdown table
    md_table = prism_df.to_markdown(index=False)
    
    with open(output_prism_md, 'w', encoding='utf-8') as f:
        f.write(f"### {title_prefix} Top 20 Genus (Relative Abundance)\n\n")
        f.write(md_table)
        f.write("\n\n")

    return top_20

# Define paths
lung_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\AP_GiNV_Oral\L7_lung.xlsx'
stool_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\AP_GiNV_Oral\L7_stool.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\screens'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Process Lung
top_20_lung = process_l7_file(
    lung_file, 
    os.path.join(output_dir, 'lung_heatmap.png'), 
    os.path.join(output_dir, 'lung_prism.md'), 
    'Lung'
)

# Process Stool
top_20_stool = process_l7_file(
    stool_file, 
    os.path.join(output_dir, 'stool_heatmap.png'), 
    os.path.join(output_dir, 'stool_prism.md'), 
    'Stool'
)

# Preliminary Lung-Gut Axis Observation
lung_genera = set(top_20_lung['Genus'])
stool_genera = set(top_20_stool['Genus'])
common_genera = lung_genera.intersection(stool_genera)

observation_file = os.path.join(output_dir, 'axis_observation.md')
with open(observation_file, 'w', encoding='utf-8') as f:
    f.write("## 肺腸軸初步觀察 (Lung-Gut Axis Observations)\n\n")
    f.write(f"在肺部與腸道同時進入 Top 20 的菌屬共有 {len(common_genera)} 個：\n")
    for g in common_genera:
        f.write(f"- {g}\n")
    f.write("\n初步建議：請檢查這些共有菌屬在兩處的變化趨勢是否一致。")

print("Analysis complete. Heatmaps and Prism tables generated.")
