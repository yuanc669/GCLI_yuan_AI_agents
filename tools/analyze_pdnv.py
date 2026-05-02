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
    # Fallback for simple names or [translated]
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
    
    # Standardize columns
    cols = list(data.columns)
    # The first 3 are Accession, Description, MW. The next 3 are Area replicates.
    data.columns = ['Accession', 'Description', 'MW', 'Rep1', 'Rep2', 'Rep3'] + cols[6:]
    
    # Numeric conversion
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

# Ginger is straightforward
df_ginger = pd.read_excel(os.path.join(pdnv_dir, 'Fulltable_target_Ginger.xlsx'))
ginger_top = df_ginger[df_ginger['Gene_id'] != 'Unaligned'].sort_values('Mean', ascending=False).head(10)
print('\n## Ginger small RNA (Top 10 High Abundance)')
print('| Rank | miRNA ID | Description | Mean Count | Sequence |')
print('|---|---|---|---|---|')
for i, r in enumerate(ginger_top.itertuples(), 1):
    seq = str(r.Query_seq).replace('\n', '')
    print(f'| {i} | {r.Gene_id} | {r.Description} | {r.Mean:,.0f} | {seq} |')

# Garlic and Kale need header offset
def analyze_srna_offset(plant, filename, start_row, plant_cols):
    df = pd.read_excel(os.path.join(pdnv_dir, filename), header=start_row)
    # Filter for plant miRNAs (usually the columns on the right)
    # Col indices for plant part: Description, Query_seq, Mean, Gene_id
    sub = df.iloc[:, plant_cols].copy()
    sub.columns = ['Description', 'Query_seq', 'Mean', 'Gene_id']
    sub['Mean'] = pd.to_numeric(sub['Mean'], errors='coerce').fillna(0)
    # Gene_id like Allium_sativum... or Brassica_oleracea...
    sub = sub[sub['Gene_id'].str.contains(plant, case=False, na=False)]
    top = sub.sort_values('Mean', ascending=False).head(10)
    print(f'\n## {plant} small RNA (Top 10 High Abundance)')
    print('| Rank | miRNA ID | Description | Mean Count | Sequence |')
    print('|---|---|---|---|---|')
    for i, r in enumerate(top.itertuples(), 1):
        seq = str(r.Query_seq).replace('\n', '')
        print(f'| {i} | {r.Gene_id} | {r.Description} | {r.Mean:,.0f} | {seq} |')

analyze_srna_offset('Garlic', 'Fulltable_target_Garlic.xlsx', 4, [8, 9, 10, 11])
analyze_srna_offset('Kale', 'Fulltable_target_Kale.xlsx', 6, [6, 7, 8, 9])
