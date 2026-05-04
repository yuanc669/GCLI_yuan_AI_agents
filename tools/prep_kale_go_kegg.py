import pandas as pd
import os

prot_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\01_Raw_Data\25091902-Label-free Quantification Kale NV.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis'

def prepare_accessions():
    print("# 🧪 Preparing Accession IDs for Functional Enrichment Analysis")
    
    df = pd.read_excel(prot_file)
    data = df.iloc[1:].copy()
    
    # Standardize columns (same as previous scripts)
    new_cols = ['Accession', 'Description', 'MW_kDa', 
                'Area_1', 'Area_2', 'Area_3', 
                'PSM_1', 'PSM_2', 'PSM_3', 
                'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    data.columns = new_cols
    
    numeric_cols = ['Area_1', 'Area_2', 'Area_3']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
    
    data['Mean_Area'] = data[numeric_cols].mean(axis=1)
    
    # Sort and take Top 100
    top_100 = data.sort_values('Mean_Area', ascending=False).head(100)
    
    # Extract Accessions
    accessions = top_100['Accession'].tolist()
    
    # Save to TXT
    accession_txt_path = os.path.join(output_dir, 'Kale_NV_Top100_Accessions.txt')
    with open(accession_txt_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(accessions))
    
    print(f"\n> Extracted {len(accessions)} Accession IDs.")
    print(f"> Saved to: {accession_txt_path}")
    print("\n## Key Target Proteins for PPI (STRING):")
    targets = {
        'Myrosinase (A0A0D3AXF1)': 'Glucosinolate degradation, Cruciferae-specific defense.',
        'Nitrilase (A0A0D3AJG2)': 'Indoleacetic acid (IAA) biosynthesis, defense.',
        'Aquaporin (A0A0D3BL75)': 'Water and small molecule transport.',
        'CSC1-like ERD4 (A0A0D3BJ42)': 'Early responsive to dehydration, calcium-binding.'
    }
    for protein, desc in targets.items():
        print(f"- **{protein}**: {desc}")

if __name__ == "__main__":
    prepare_accessions()
