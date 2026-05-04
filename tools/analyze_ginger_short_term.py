import pandas as pd
import os

# Paths
processed_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\Ginger_Full_Analysis.csv'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\Short_Term'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(processed_file)
    
    # 1. Extract Top 100 Accessions for external tools (STRING/g:Profiler)
    top_100 = df.sort_values('Mean', ascending=False).head(100)
    top_100_list = top_100['Accession'].tolist()
    
    with open(os.path.join(output_dir, 'Ginger_Top100_Accessions.txt'), 'w') as f:
        f.write('\n'.join(top_100_list))
    
    # 2. Keyword-based "Pseudo-Enrichment"
    # Define functional categories and their keywords
    keyword_map = {
        'Translation/Ribosome': ['ribosomal', 'translation', 'elongation factor'],
        'Carbohydrate Metabolism': ['phosphorylase', 'kinase', 'dehydrogenase', 'aldolase', 'isomerase', 'glucosidase'],
        'Protein Folding/Stress': ['heat shock', 'hsp', 'chaperone', 'disulfide', 'folding'],
        'Redox/Antioxidant': ['peroxidase', 'dismutase', 'reductase', 'catalase', 'thioredoxin', 'oxidoreductase'],
        'Proteolysis': ['protease', 'peptidase', 'ubiquitin', 'cathepsin'],
        'Transport/Vesicle': ['transporter', 'channel', 'aquaporin', 'clathrin', 'rab', 'annexin'],
        'Cytoskeleton': ['actin', 'tubulin', 'profilin', 'myosin'],
        'Defense/Signaling': ['defense', '14-3-3', 'lipoxygenase', 'chitinase', 'pathogenesis']
    }

    results = []
    for category, keywords in keyword_map.items():
        # Case insensitive match
        pattern = '|'.join(keywords)
        mask = df['Description'].str.contains(pattern, case=False, na=False)
        subset = df[mask]
        results.append({
            'Category': category,
            'Protein_Count': len(subset),
            'Abundance_Sum': subset['Mean'].sum(),
            'Top_Proteins': '; '.join(subset.sort_values('Mean', ascending=False).head(3)['Description'].str.split(';').str[0].tolist())
        })
    
    enrich_df = pd.DataFrame(results).sort_values('Abundance_Sum', ascending=False)
    enrich_df.to_csv(os.path.join(output_dir, 'Ginger_Keyword_Enrichment.csv'), index=False)
    
    # 3. Identify Hub Candidates (High abundance + Signaling/Transport)
    hubs = df[df['Description'].str.contains('14-3-3|Rab|Annexin|Clathrin|HSP70', case=False, na=False)]
    hubs = hubs.sort_values('Mean', ascending=False).head(10)
    hubs.to_csv(os.path.join(output_dir, 'Ginger_Hub_Candidates.csv'), index=False)

    print(f"Short-term analysis files generated in {output_dir}")
    print("\nSimulated Enrichment Summary:")
    print(enrich_df[['Category', 'Protein_Count', 'Abundance_Sum']].to_string())

except Exception as e:
    print(f"Error: {e}")
