import pandas as pd
import re
import os

pdnv_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\PDNV'

def clean_desc(desc):
    if not isinstance(desc, str): return 'Uncharacterized protein'
    swiss_match = re.search(r'Swissprot=([^;]+)', desc)
    if swiss_match: return swiss_match.group(1).split(' OS=')[0].strip()
    nr_match = re.search(r'NR=([^;]+)', desc)
    if nr_match: return nr_match.group(1).split(' [')[0].strip()
    clean = desc.replace('[translated] |', '').strip()
    return clean.split(' OS=')[0].split('|')[-1].strip()

# --- Proteomics Analysis ---
proteomics_files = {
    'Garlic': '25091902-Label-free Quantification Garlic_NV.xlsx',
    'Ginger': '25091902-Label-free Quantification Ginger NV.xlsx',
    'Kale': '25091902-Label-free Quantification Kale NV.xlsx'
}

print('# 🧬 PDNV Proteomics Comparative Analysis')

for plant, filename in proteomics_files.items():
    path = os.path.join(pdnv_dir, filename)
    df = pd.read_excel(path)
    data = df.iloc[1:].copy()
    cols = list(data.columns)
    data.columns = ['Accession', 'Description', 'MW', 'Rep1', 'Rep2', 'Rep3'] + cols[6:]
    for c in ['Rep1', 'Rep2', 'Rep3']:
        data[c] = pd.to_numeric(data[c], errors='coerce').fillna(0)
    data['Mean_Area'] = data[['Rep1', 'Rep2', 'Rep3']].mean(axis=1)
    data['Clean_Name'] = data['Description'].apply(clean_desc)
    top = data.sort_values('Mean_Area', ascending=False).head(10)
    print(f'\n## {plant} Proteomics (Top 10 High Abundance)')
    print('| Rank | Accession | Protein Name (Restored) | Mean Area |')
    print('|---|---|---|---|')
    for i, r in enumerate(top.itertuples(), 1):
        print(f'| {i} | {r.Accession} | {r.Clean_Name} | {r.Mean_Area:,.0f} |')

# --- small RNA Analysis ---
print('\n# 🧬 PDNV small RNA-seq Comparative Analysis')

def get_top_srna(plant, filename, plant_key):
    df = pd.read_excel(os.path.join(pdnv_dir, filename), header=None)
    # Find the row containing Gene_id
    header_idx = -1
    for i, row in df.iterrows():
        if 'Gene_id' in row.astype(str).values:
            header_idx = i
            break
    
    if header_idx == -1:
        # Special case for Ginger where it might be already in header
        df = pd.read_excel(os.path.join(pdnv_dir, filename))
        if 'Gene_id' in df.columns:
            sub = df
        else:
            return
    else:
        # Set headers
        new_header = df.iloc[header_idx]
        df.columns = new_header
        sub = df.iloc[header_idx+1:].copy()
    
    # Standardize columns
    target_cols = ['Description', 'Query_seq', 'Mean', 'Gene_id']
    # Sometimes 'Mean' is named differently or we need to find it
    final_cols = {}
    for tc in target_cols:
        for c in sub.columns:
            if str(c).strip() == tc:
                final_cols[tc] = c
                break
    
    if len(final_cols) < 4:
        # Try to find columns by content if names don't match
        return

    sub_final = sub[[final_cols['Description'], final_cols['Query_seq'], final_cols['Mean'], final_cols['Gene_id']]].copy()
    sub_final.columns = ['Description', 'Query_seq', 'Mean', 'Gene_id']
    sub_final['Mean'] = pd.to_numeric(sub_final['Mean'], errors='coerce').fillna(0)
    sub_final = sub_final[sub_final['Gene_id'].str.contains(plant_key, case=False, na=False)]
    top = sub_final.sort_values('Mean', ascending=False).head(10)
    
    print(f'\n## {plant} small RNA (Top 10 High Abundance)')
    print('| Rank | miRNA ID | Description | Mean Count | Sequence |')
    print('|---|---|---|---|---|')
    for i, r in enumerate(top.itertuples(), 1):
        seq = str(r.Query_seq).replace('\n', '').strip()
        print(f'| {i} | {r.Gene_id} | {r.Description} | {r.Mean:,.0f} | {seq} |')

get_top_srna('Garlic', 'Fulltable_target_Garlic.xlsx', 'Allium')
get_top_srna('Ginger', 'Fulltable_target_Ginger.xlsx', 'Zingiber')
get_top_srna('Kale', 'Fulltable_target_Kale.xlsx', 'Brassica')
