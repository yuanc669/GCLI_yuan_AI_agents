import pandas as pd
import re
import os

prot_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\01_Raw_Data\25091902-Label-free Quantification Kale NV.xlsx'
srna_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\01_Raw_Data\Fulltable_target_Kale.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis'

def clean_desc(desc):
    if not isinstance(desc, str): return 'Uncharacterized protein'
    clean = desc.split(' OS=')[0]
    clean = clean.split(' GN=')[0]
    clean = clean.split('|')[-1].strip()
    return clean

def analyze_kale_proteomics():
    print("# 🥬 Kale NV Proteomics Data Analysis Report")
    df = pd.read_excel(prot_file)
    data = df.iloc[1:].copy()
    
    new_cols = ['Accession', 'Description', 'MW_kDa', 
                'Area_1', 'Area_2', 'Area_3', 
                'PSM_1', 'PSM_2', 'PSM_3', 
                'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    data.columns = new_cols
    
    numeric_cols = ['MW_kDa', 'Area_1', 'Area_2', 'Area_3', 'PSM_1', 'PSM_2', 'PSM_3', 'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
    
    data['Mean_Area'] = data[['Area_1', 'Area_2', 'Area_3']].mean(axis=1)
    data['CV_Area'] = data[['Area_1', 'Area_2', 'Area_3']].std(axis=1) / data['Mean_Area']
    data['Mean_PSM'] = data[['PSM_1', 'PSM_2', 'PSM_3']].mean(axis=1)
    data['Clean_Name'] = data['Description'].apply(clean_desc)
    
    top_20 = data.sort_values('Mean_Area', ascending=False).head(20)
    
    print("\n## Top 20 Most Abundant Proteins (by Area)")
    print("| Rank | Accession | Protein Name | Mean Area | CV (%) | Mean PSM |")
    print("|---|---|---|---|---|---|")
    for i, r in enumerate(top_20.itertuples(), 1):
        cv_str = f"{r.CV_Area*100:.1f}" if not pd.isna(r.CV_Area) else "N/A"
        print(f"| {i} | {r.Accession} | {r.Clean_Name} | {r.Mean_Area:,.0f} | {cv_str} | {r.Mean_PSM:.1f} |")
    
    categories = {
        'Ribosomal': ['ribosomal', '40S', '60S'],
        'Metabolism/Enzyme': ['dehydrogenase', 'kinase', 'synthase', 'phosphatase', 'protease', 'peptidase', 'reductase'],
        'Cytoskeleton': ['actin', 'tubulin', 'myosin'],
        'Chaperone/Stress': ['heat shock', 'chaperone', 'thioredoxin', 'peroxiredoxin'],
        'Signaling': ['GTP-binding', '14-3-3', 'annexin'],
        'Histone': ['histone']
    }
    
    cat_counts = {}
    for cat, keywords in categories.items():
        mask = data['Description'].str.contains('|'.join(keywords), case=False, na=False)
        cat_counts[cat] = mask.sum()
        
    print("\n## Functional Category Distribution (by keyword match)")
    print("| Category | Count |")
    print("|---|---|")
    for cat, count in cat_counts.items():
        print(f"| {cat} | {count} |")
        
    data.to_excel(os.path.join(output_dir, 'Kale_NV_Proteomics_Analysis.xlsx'), index=False)

def analyze_kale_srna():
    print("\n# 🧬 Kale NV small RNA-seq Analysis")
    df = pd.read_excel(srna_file, header=None)
    data = df.iloc[7:].copy()
    
    # Correct indices: 0: Human Match, 7: Query_seq, 8: Mean, 9: Gene_id
    sub = data[[0, 7, 8, 9]].copy()
    sub.columns = ['Human_miRNA_Match', 'Query_seq', 'Mean_Count', 'Gene_id']
    sub['Mean_Count'] = pd.to_numeric(sub['Mean_Count'], errors='coerce').fillna(0)
    
    kale_mirna = sub[sub['Gene_id'].str.contains('Brassica', case=False, na=False)].copy()
    top_mirna = kale_mirna.sort_values('Mean_Count', ascending=False).head(20)
    
    print("\n## Top 20 Most Abundant Kale miRNAs")
    print("| Rank | miRNA ID | Mean Count | Sequence | Human Match |")
    print("|---|---|---|---|---|")
    for i, r in enumerate(top_mirna.itertuples(), 1):
        seq = str(r.Query_seq).replace('\n', '')
        print(f"| {i} | {r.Gene_id} | {r.Mean_Count:,.0f} | {seq} | {r.Human_miRNA_Match} |")
    
    kale_mirna.to_excel(os.path.join(output_dir, 'Kale_NV_sRNA_Analysis.xlsx'), index=False)

if __name__ == "__main__":
    analyze_kale_proteomics()
    analyze_kale_srna()
    print(f"\n> Full analysis results saved to {output_dir}")
