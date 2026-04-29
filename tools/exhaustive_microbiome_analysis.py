import pandas as pd
import numpy as np
import os
import re
from scipy import stats

inbox_dir = 'G:/我的雲端硬碟/GCLI_yuan_AI agents/_inbox'
output_dir = 'G:/我的雲端硬碟/GCLI_yuan_AI agents/secondgrain/100_Research/02_Active/DN_GaExo'
files = [f for f in os.listdir(inbox_dir) if f.endswith('.xlsx')]

def get_group_data(df):
    cols = [c for c in df.columns if not c.endswith('.1') and c not in ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species', 'Total']]
    groups = {}
    for c in cols:
        prefix = re.split(r'[-_]\d', c)[0]
        if prefix not in groups:
            groups[prefix] = {'counts': [], 'rel': []}
        groups[prefix]['counts'].append(c)
        groups[prefix]['rel'].append(c + '.1')
    return groups

def calculate_shannon(counts):
    counts = np.array(counts, dtype=float)
    counts = counts[counts > 0]
    if len(counts) == 0: return 0
    probs = counts / np.sum(counts)
    return -np.sum(probs * np.log(probs))

for f_name in files:
    try:
        path = os.path.join(inbox_dir, f_name)
        df = pd.read_excel(path)
        groups = get_group_data(df)
        if not groups: continue
        
        group_names = sorted(groups.keys())
        group_str = '_'.join(group_names).replace(' ', '_')
        
        # Alpha Diversity
        alpha_lines = ["| Sample | Group | Shannon | Observed |", "| --- | --- | --- | --- |"]
        for gn in group_names:
            for c_col in groups[gn]['counts']:
                cnts = df[c_col].values
                shannon = calculate_shannon(cnts)
                observed = np.count_nonzero(cnts)
                alpha_lines.append(f"| {c_col} | {gn} | {shannon:.4f} | {observed} |")
        
        # Statistics
        stat_lines = ["| Species | " + " | ".join(group_names) + " | Kruskal_p |", "| --- | " + " | ".join(["---"]*len(group_names)) + " | --- |"]
        for _, row in df.iterrows():
            group_vals = [row[groups[gn]['rel']].values.astype(float) * 100 for gn in group_names]
            try:
                stat, p_val = stats.kruskal(*group_vals)
            except:
                p_val = 1.0
            
            means = [f"{np.mean(v):.4f}%" for v in group_vals]
            stat_lines.append(f"| {row['Species']} | " + " | ".join(means) + f" | {p_val:.6f} |")
        
        # Save Report
        report_path = os.path.join(output_dir, f'20260429_Full_Analysis_{group_str}.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f'# Full Microbiome Analysis: {group_str}\n\n')
            f.write('## Alpha Diversity\n' + "\n".join(alpha_lines) + '\n\n')
            f.write('## All Species Abundance & Stats\n' + "\n".join(stat_lines) + '\n')

        # Save Prism
        prism_path = os.path.join(output_dir, f'20260429_Full_Prism_{group_str}.md')
        with open(prism_path, 'w', encoding='utf-8') as f:
            f.write(f'# Full Prism Data: {group_str}\n\n')
            for _, row in df.iterrows():
                f.write(f'### {row["Species"]}\n')
                f.write('\t'.join(group_names) + '\n')
                max_reps = max(len(groups[gn]['rel']) for gn in group_names)
                for i in range(max_reps):
                    line = []
                    for gn in group_names:
                        rel_cols = groups[gn]['rel']
                        line.append(f'{row[rel_cols[i]]*100:.4f}' if i < len(rel_cols) else '')
                    f.write('\t'.join(line) + '\n')
                f.write('\n')
        print(f'Fully Processed: {f_name}')
    except Exception as e:
        print(f'Error processing {f_name}: {e}')
