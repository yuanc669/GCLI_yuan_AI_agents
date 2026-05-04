import pandas as pd
import re
import os

prot_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\01_Raw_Data\25091902-Label-free Quantification Kale NV.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis'

def clean_desc(desc):
    if not isinstance(desc, str): return 'Uncharacterized protein'
    clean = desc.split(' OS=')[0]
    clean = clean.split(' GN=')[0]
    clean = clean.split('|')[-1].strip()
    return clean

def generate_top_30_report():
    df = pd.read_excel(prot_file)
    data = df.iloc[1:].copy()
    
    # Standardize columns
    new_cols = ['Accession', 'Description', 'MW_kDa', 
                'Area_1', 'Area_2', 'Area_3', 
                'PSM_1', 'PSM_2', 'PSM_3', 
                'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    data.columns = new_cols
    
    numeric_cols = ['Area_1', 'Area_2', 'Area_3', 'PSM_1', 'PSM_2', 'PSM_3']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
    
    data['Mean_Area'] = data[['Area_1', 'Area_2', 'Area_3']].mean(axis=1)
    data['Mean_PSM'] = data[['PSM_1', 'PSM_2', 'PSM_3']].mean(axis=1)
    data['Clean_Name'] = data['Description'].apply(clean_desc)
    
    # Extract Top 30
    top_30 = data.sort_values('Mean_Area', ascending=False).head(30)
    
    # Save to CSV for Prism
    prism_data = top_30[['Clean_Name', 'Area_1', 'Area_2', 'Area_3']].copy()
    prism_csv_path = os.path.join(output_dir, 'Kale_NV_Top30_Area_Prism.csv')
    prism_data.to_csv(prism_csv_path, index=False)
    
    # Output MD Table
    print("# 🥬 Kale NV Proteomics: Top 30 High Abundance Proteins")
    print("\n| Rank | Protein Name | Accession | Mean Area | Mean PSM | MW (kDa) |")
    print("|:---:|:---|:---:|:---:|:---:|:---:|")
    for i, r in enumerate(top_30.itertuples(), 1):
        print(f"| {i} | {r.Clean_Name} | {r.Accession} | {r.Mean_Area:,.0f} | {r.Mean_PSM:.1f} | {r.MW_kDa} |")

    # Update the full report file as well
    md_report_path = os.path.join(output_dir, 'Kale_NV_Proteomics_Top30_Report.md')
    with open(md_report_path, 'w', encoding='utf-8') as f:
        f.write("# 🥬 Kale NV Proteomics: Top 30 High Abundance Proteins\n\n")
        f.write("| Rank | Protein Name | Accession | Mean Area | Area-1 | Area-2 | Area-3 | MW (kDa) |\n")
        f.write("|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|\n")
        for i, r in enumerate(top_30.itertuples(), 1):
            f.write(f"| {i} | {r.Clean_Name} | {r.Accession} | {r.Mean_Area:,.0f} | {r.Area_1:,.0f} | {r.Area_2:,.0f} | {r.Area_3:,.0f} | {r.MW_kDa} |\n")
    
    print(f"\n> Top 30 report and CSV generated in: {output_dir}")

if __name__ == "__main__":
    generate_top_30_report()
