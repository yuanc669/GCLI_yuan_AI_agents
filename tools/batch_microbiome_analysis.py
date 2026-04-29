import pandas as pd
import numpy as np
import os
import re

inbox_dir = 'G:/我的雲端硬碟/GCLI_yuan_AI agents/_inbox'
output_dir = 'G:/我的雲端硬碟/GCLI_yuan_AI agents/secondgrain/100_Research/02_Active/DN_GaExo'
files = [f for f in os.listdir(inbox_dir) if f.endswith('.xlsx')]

def get_group_data(df):
    cols = [c for c in df.columns if not c.endswith('.1') and c not in ['Kingdom', 'Phylum', 'Class', 'Order', 'Family', 'Genus', 'Species', 'Total']]
    groups = {}
    for c in cols:
        prefix = re.split(r'[-_]\d', c)[0]
        if prefix not in groups: groups[prefix] = []
        groups[prefix].append(c + '.1')
    return groups

for f_name in files:
    try:
        path = os.path.join(inbox_dir, f_name)
        df = pd.read_excel(path)
        groups = get_group_data(df)
        if not groups: continue
        
        sorted_group_names = sorted(groups.keys())
        group_str = '_'.join(sorted_group_names).replace(' ', '_')
        
        for gn in sorted_group_names:
            df[f'Mean_{gn}'] = df[groups[gn]].mean(axis=1)
        
        base = sorted_group_names[0]
        comp = sorted_group_names[-1]
        df['Abs_Change'] = abs(df[f'Mean_{comp}'] - df[f'Mean_{base}'])
        top_30 = df.sort_values(by='Abs_Change', ascending=False).head(30)
        
        # Save Report
        report_path = os.path.join(output_dir, f'20260429_Microbiome_Report_{group_str}.md')
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(f'# Microbiome Analysis Report: {group_str}\n\n')
            f.write('| Species | ' + ' | '.join(sorted_group_names) + ' | Abs_Change |\n')
            f.write('| --- | ' + ' | '.join(['---'] * len(sorted_group_names)) + ' | --- |\n')
            for _, row in top_30.iterrows():
                vals = [f'{row[f"Mean_{gn}"]*100:.4f}%' for gn in sorted_group_names]
                f.write(f'| {row["Species"]} | ' + ' | '.join(vals) + f' | {row["Abs_Change"]*100:.4f}% |\n')
                
        # Save Prism Data
        prism_path = os.path.join(output_dir, f'20260429_Microbiome_Prism_{group_str}.md')
        with open(prism_path, 'w', encoding='utf-8') as f:
            f.write(f'# Prism Data: {group_str}\n\n')
            for _, row in top_30.iterrows():
                name = row['Species']
                f.write(f'### {name}\n')
                f.write('\t'.join(sorted_group_names) + '\n')
                max_reps = max(len(groups[gn]) for gn in sorted_group_names)
                for i in range(max_reps):
                    line = []
                    for gn in sorted_group_names:
                        cols = groups[gn]
                        if i < len(cols): line.append(f'{row[cols[i]]*100:.4f}')
                        else: line.append('')
                    f.write('\t'.join(line) + '\n')
                f.write('\n')
        print(f'Processed: {f_name}')
    except Exception as e:
        print(f'Error processing {f_name}: {e}')
