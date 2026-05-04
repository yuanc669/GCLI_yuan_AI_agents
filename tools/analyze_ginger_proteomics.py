import pandas as pd
import numpy as np
import os

# Paths
raw_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\01_Raw_Data\25091902-Label-free Quantification Ginger NV.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis'
os.makedirs(output_dir, exist_ok=True)

try:
    # Read the data, skip the first row as it's a header duplicate (or header row is at index 1)
    df = pd.read_excel(raw_file, skiprows=1)
    
    # Map columns based on peek results
    # ['Accession', 'Description', 'MW [kDa]', 'Ginger-1', 'Ginger-2', 'Ginger-3', 
    #  'Ginger-1.1', 'Ginger-2.1', 'Ginger-3.1', 'Ginger-1.2', 'Ginger-2.2', 'Ginger-3.2', 
    #  'Unnamed: 12', 'Unnamed: 13']
    
    new_cols = [
        'Accession', 'Description', 'MW_kDa', 
        'Area_1', 'Area_2', 'Area_3', 
        'PSM_1', 'PSM_2', 'PSM_3', 
        'NormPSM_1', 'NormPSM_2', 'NormPSM_3', 
        'AVERAGE_NormPSM', 'SD_NormPSM'
    ]
    df.columns = new_cols
    
    # Filter out empty or non-protein rows
    df = df[df['Accession'].notna() & (df['Accession'] != 'Accession')].copy()
    
    # Handle "-" or NaN in numeric columns
    numeric_cols = ['MW_kDa', 'AVERAGE_NormPSM', 'SD_NormPSM', 'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col].replace('-', np.nan), errors='coerce').fillna(0)
    
    # Functional Categorization
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
    
    # Calculate SEM for Prism
    df['SEM_NormPSM'] = df['SD_NormPSM'] / np.sqrt(3) # Assuming n=3 for SEM calculation, though some might be n=2
    
    # 1. Full Analysis
    full_output = os.path.join(output_dir, 'GingerNV_Proteomics_Full_Analysis.csv')
    df.to_csv(full_output, index=False)
    
    # 2. Top 50 Proteins
    top_50 = df.sort_values('AVERAGE_NormPSM', ascending=False).head(50)
    top_50_output = os.path.join(output_dir, 'GingerNV_Top50_Proteins.csv')
    top_50.to_csv(top_50_output, index=False)
    
    # 3. Functional Summary
    summary = df.groupby('Functional_Category')['AVERAGE_NormPSM'].agg(['count', 'sum', 'mean']).sort_values('sum', ascending=False)
    summary_output = os.path.join(output_dir, 'GingerNV_Functional_Summary.csv')
    summary.to_csv(summary_output)
    
    # 4. Prism Data (Top 30)
    prism_data = df.sort_values('AVERAGE_NormPSM', ascending=False).head(30)[['Accession', 'Description', 'AVERAGE_NormPSM', 'SD_NormPSM', 'SEM_NormPSM']]
    prism_output = os.path.join(output_dir, 'GingerNV_Top30_Prism.csv')
    prism_data.to_csv(prism_output, index=False)

    print(f"Analysis Complete. Results saved to {output_dir}")
    print("\nTop 10 Functional Categories by Abundance:")
    print(summary.head(10).to_string())

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
