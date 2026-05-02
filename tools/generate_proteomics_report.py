import pandas as pd
import numpy as np

file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\25091902-Label-free Quantification Garlic_NV.xlsx'

try:
    df = pd.read_excel(file_path, skiprows=1)
    new_cols = [
        'Accession', 'Description', 'MW_kDa', 
        'Area_G1', 'Area_G2', 'Area_G3', 
        'PSM_G1', 'PSM_G2', 'PSM_G3', 
        'NormPSM_G1', 'NormPSM_G2', 'NormPSM_G3', 'AVERAGE_NormPSM'
    ]
    df.columns = new_cols
    df = df[df['Accession'].notna() & (df['Accession'] != 'Accession')].copy()
    
    # Define keywords for functional categorization
    categories = {
        'Antioxidant': ['peroxidase', 'dismutase', 'reductase', 'glutathione', 'catalase', 'thioredoxin'],
        'Anti-stress/HSP': ['heat shock', 'hsp', 'chaperone'],
        'Lipid Metabolism': ['lipase', 'esterase', 'lipid', 'fatty acid'],
        'Defense/Immunity': ['defense', 'chitinase', 'pathogenesis', 'antimicrobial'],
        'Transport': ['transporter', 'channel', 'aquaporin', 'carrier'],
        'Protein Synthesis': ['ribosomal', 'translation', 'elongation factor'],
        'Exosome Marker': ['annexin', 'rab', 'tetraspanin', 'hsp70']
    }

    def categorize(desc):
        desc = str(desc).lower()
        found = []
        for cat, keywords in categories.items():
            if any(k in desc for k in keywords):
                found.append(cat)
        return ', '.join(found) if found else 'Other'

    df['Functional_Category'] = df['Description'].apply(categorize)
    
    # Abundance ranking
    df['AVERAGE_NormPSM'] = pd.to_numeric(df['AVERAGE_NormPSM'], errors='coerce')
    top_proteins = df.sort_values('AVERAGE_NormPSM', ascending=False)
    
    # Save the full analysis
    df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Proteomics_Full_Analysis.csv', index=False)
    
    # Generate a report table for the user
    summary_table = top_proteins[['Accession', 'AVERAGE_NormPSM', 'Functional_Category', 'Description']].head(20)
    summary_table.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Top20_Proteins_Report.csv', index=False)
    
    print("Report Table Generated.")
    print(summary_table.to_string())

except Exception as e:
    print(f"Error: {e}")
