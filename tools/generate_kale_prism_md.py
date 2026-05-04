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

def generate_prism_and_md():
    df = pd.read_excel(prot_file)
    data = df.iloc[1:].copy()
    
    # Standardize columns
    new_cols = ['Accession', 'Description', 'MW_kDa', 
                'Area_1', 'Area_2', 'Area_3', 
                'PSM_1', 'PSM_2', 'PSM_3', 
                'NormPSM_1', 'NormPSM_2', 'NormPSM_3']
    data.columns = new_cols
    
    numeric_cols = ['Area_1', 'Area_2', 'Area_3']
    for col in numeric_cols:
        data[col] = pd.to_numeric(data[col], errors='coerce').fillna(0)
    
    data['Mean_Area'] = data[numeric_cols].mean(axis=1)
    data['Clean_Name'] = data['Description'].apply(clean_desc)
    
    # 1. Top 10 Proteins for Prism (Replicates)
    top_10 = data.sort_values('Mean_Area', ascending=False).head(10)
    prism_data = top_10[['Clean_Name', 'Area_1', 'Area_2', 'Area_3']].copy()
    prism_csv_path = os.path.join(output_dir, 'Kale_NV_Top10_Area_Prism.csv')
    prism_data.to_csv(prism_csv_path, index=False)
    
    # 2. Functional Categories for Prism
    categories = {
        'Ribosomal': ['ribosomal', '40S', '60S'],
        'Metabolism/Enzyme': ['dehydrogenase', 'kinase', 'synthase', 'phosphatase', 'protease', 'peptidase', 'reductase'],
        'Cytoskeleton': ['actin', 'tubulin', 'myosin'],
        'Chaperone/Stress': ['heat shock', 'chaperone', 'thioredoxin', 'peroxiredoxin'],
        'Signaling': ['GTP-binding', '14-3-3', 'annexin'],
        'Histone': ['histone']
    }
    
    cat_counts = []
    for cat, keywords in categories.items():
        mask = data['Description'].str.contains('|'.join(keywords), case=False, na=False)
        cat_counts.append({'Category': cat, 'Count': mask.sum()})
    
    cat_df = pd.DataFrame(cat_counts)
    cat_csv_path = os.path.join(output_dir, 'Kale_NV_Functional_Distribution_Prism.csv')
    cat_df.to_csv(cat_csv_path, index=False)

    # 3. Generate MD Report
    md_report_path = os.path.join(output_dir, 'Kale_NV_Proteomics_Report.md')
    with open(md_report_path, 'w', encoding='utf-8') as f:
        f.write("# 🥬 Kale NV Proteomics Data Report\n\n")
        
        f.write("## 1. Top 10 High Abundance Proteins\n")
        f.write("| Rank | Protein Name | Accession | Mean Area | Area-1 | Area-2 | Area-3 |\n")
        f.write("|:---:|:---|:---:|:---:|:---:|:---:|:---:|\n")
        for i, r in enumerate(top_10.itertuples(), 1):
            f.write(f"| {i} | {r.Clean_Name} | {r.Accession} | {r.Mean_Area:,.0f} | {r.Area_1:,.0f} | {r.Area_2:,.0f} | {r.Area_3:,.0f} |\n")
        
        f.write("\n\n## 2. Functional Distribution\n")
        f.write("| Category | Count | Percentage (%) |\n")
        f.write("|:---|:---:|:---:|\n")
        total_matched = cat_df['Count'].sum()
        for r in cat_df.itertuples():
            pct = (r.Count / total_matched * 100) if total_matched > 0 else 0
            f.write(f"| {r.Category} | {r.Count} | {pct:.1f}% |\n")
        
        f.write("\n\n## 3. Data for Prism\n")
        f.write(f"- [Top 10 Replicates CSV](./Kale_NV_Top10_Area_Prism.csv)\n")
        f.write(f"- [Functional Distribution CSV](./Kale_NV_Functional_Distribution_Prism.csv)\n")

    print(f"Prism data and MD report generated in: {output_dir}")

if __name__ == "__main__":
    generate_prism_and_md()
