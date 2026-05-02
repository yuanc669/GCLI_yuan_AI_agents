import pandas as pd
import re
from collections import defaultdict

file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Proteomics_Full_Analysis.csv'

try:
    df = pd.read_csv(file_path)
    
    go_counts = defaultdict(int)
    go_psm = defaultdict(float)
    kegg_counts = defaultdict(int)
    kegg_psm = defaultdict(float)
    
    for _, row in df.iterrows():
        desc = str(row['Description'])
        psm = row['AVERAGE_NormPSM']
        
        # Extract GO
        # Pattern: GO=Molecular Function: catalytic activity (GO:0003824),Biological Process: ...
        go_matches = re.findall(r'GO:([^,\); ]+)', desc)
        for go_id in go_matches:
            # Try to get the term name before the ID
            # This is tricky with the current regex, let's just use IDs for now or a simpler regex
            go_counts[go_id] += 1
            go_psm[go_id] += psm
            
        # Extract KEGG
        # Pattern: KEGG=probable serine/threonine...; K11583...
        kegg_matches = re.findall(r'K(\d{5})', desc)
        for k_id in kegg_matches:
            k_id = 'K' + k_id
            kegg_counts[k_id] += 1
            kegg_psm[k_id] += psm

    # Convert to DataFrames
    go_df = pd.DataFrame([{'GO_ID': k, 'Count': v, 'PSM_Sum': go_psm[k]} for k, v in go_counts.items()]).sort_values('PSM_Sum', ascending=False)
    kegg_df = pd.DataFrame([{'KEGG_ID': k, 'Count': v, 'PSM_Sum': kegg_psm[k]} for k, v in kegg_counts.items()]).sort_values('PSM_Sum', ascending=False)
    
    # Map some common IDs to names for readability (manual top list)
    go_map = {
        '0003824': 'Catalytic activity',
        '0016491': 'Oxidoreductase activity',
        '0005515': 'Protein binding',
        '0005524': 'ATP binding',
        '0006096': 'Glycolysis',
        '0016020': 'Membrane',
        '0005737': 'Cytoplasm',
        '0003677': 'DNA binding',
        '0006412': 'Translation',
        '0006950': 'Response to stress'
    }
    
    go_df['Term'] = go_df['GO_ID'].map(go_map).fillna('Other/Unknown')
    
    go_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_GO_Enrichment_Summary.csv', index=False)
    kegg_df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_KEGG_Enrichment_Summary.csv', index=False)
    
    print("GO/KEGG Analysis Complete.")
    print("\nTop 10 GO Terms by PSM Abundance:")
    print(go_df.head(10).to_string())
    
    print("\nTop 10 KEGG Orthologs by PSM Abundance:")
    print(kegg_df.head(10).to_string())

except Exception as e:
    print(f"Error: {e}")
