import pandas as pd
import numpy as np
import re

file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\25091902-Label-free Quantification Garlic_NV.xlsx'

try:
    # Read the data, skip the first row as it's a header duplicate
    df = pd.read_excel(file_path, skiprows=1)
    
    # Standardize column names based on the peek output
    # Looking at the peek, the columns are: 
    # Accession, Description, MW, Area1, Area2, Area3, PSM1, PSM2, PSM3, NormPSM1, NormPSM2, NormPSM3, AVERAGE
    
    # Since column names in the file are messy, let's rename them systematically
    new_cols = [
        'Accession', 'Description', 'MW_kDa', 
        'Area_G1', 'Area_G2', 'Area_G3', 
        'PSM_G1', 'PSM_G2', 'PSM_G3', 
        'NormPSM_G1', 'NormPSM_G2', 'NormPSM_G3', 'AVERAGE_NormPSM'
    ]
    df.columns = new_cols
    
    # Filter out empty or non-protein rows
    df = df[df['Accession'].notna() & (df['Accession'] != 'Accession')].copy()
    
    # Convert numeric columns
    numeric_cols = ['MW_kDa', 'AVERAGE_NormPSM', 'Area_G1', 'Area_G2', 'Area_G3']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # 1. Top 50 Abundant Proteins
    top_50 = df.sort_values('AVERAGE_NormPSM', ascending=False).head(50)
    
    # 2. Functional Extraction
    def categorize_protein(desc):
        desc = str(desc).lower()
        categories = []
        if 'heat shock' in desc or 'hsp' in desc: categories.append('Anti-stress/HSP')
        if 'lipase' in desc or 'esterase' in desc: categories.append('Lipid Metabolism')
        if 'peroxidase' in desc or 'dismutase' in desc or 'reductase' in desc: categories.append('Antioxidant')
        if 'defense' in desc or 'chitinase' in desc or 'pathogenesis' in desc: categories.append('Defense/Immunity')
        if 'transporter' in desc or 'channel' in desc: categories.append('Transport')
        if 'ribosomal' in desc or 'translation' in desc: categories.append('Protein Synthesis')
        return ', '.join(categories) if categories else 'Other'

    df['Functional_Category'] = df['Description'].apply(categorize_protein)
    
    # 3. Targeted Family Summary
    summary = df.groupby('Functional_Category')['AVERAGE_NormPSM'].agg(['count', 'sum', 'mean']).sort_values('sum', ascending=False)
    
    # Save Results
    df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Proteomics_Processed.csv', index=False)
    top_50.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Top50_Proteins.csv', index=False)
    summary.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Functional_Summary.csv')

    print("Proteomics Analysis Complete.")
    print("\nTop 10 Functional Categories by Total Abundance (PSM Sum):")
    print(summary.head(10).to_string())
    
    print("\nTop 5 Specific Proteins:")
    print(top_50[['Accession', 'AVERAGE_NormPSM', 'Functional_Category']].head(5).to_string())

except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
