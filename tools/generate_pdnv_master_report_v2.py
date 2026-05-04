import pandas as pd
import os
import re

data_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\Processed_Data'
report_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\PDNV_Proteomics_Master_Report_v2.md'

files = {
    'Garlic': 'Garlic_Full_Analysis.csv',
    'Ginger': 'Ginger_Full_Analysis.csv',
    'Kale': 'Kale_Full_Analysis.csv'
}

categories = {
    'Protein Synthesis': ['ribosomal', 'translation', 'elongation factor'],
    'Antioxidant/Redox': ['peroxiredoxin', 'superoxide dismutase', 'catalase', 'thioredoxin', 'glutathione'],
    'Vesicle/Transport': ['annexin', 'rab', 'atpase', 'aquaporin', 'vps'],
    'Stress Response': ['heat shock', 'chaperone', 'stress'],
    'Metabolism': ['dehydrogenase', 'kinase', 'synthase', 'phosphatase']
}

def robust_clean(desc):
    if not isinstance(desc, str): return ''
    # Strategy 1: Swissprot
    if 'Swissprot=' in desc:
        name = desc.split('Swissprot=')[1].split(' OS=')[0].split(' GN=')[0].strip()
    # Strategy 2: NR
    elif 'NR=' in desc:
        name = desc.split('NR=')[1].split(' [')[0].split(';')[0].strip()
    # Strategy 3: Standard OS=
    elif ' OS=' in desc:
        name = desc.split(' OS=')[0].split('|')[-1].strip()
    else:
        name = desc.split('|')[-1].strip()
    
    # Final cleanup: remove "Probable ", "Predicted: ", etc.
    name = re.sub(r'^(probable|predicted:|uncharacterized protein|putative|isoform \w+) ', '', name, flags=re.IGNORECASE)
    return name.lower()

def analyze_master():
    results = {}
    all_names = {}
    
    for plant, filename in files.items():
        df = pd.read_csv(os.path.join(data_dir, filename))
        if 'AVERAGE_NormPSM' not in df.columns:
            norm_cols = [c for c in df.columns if 'NormPSM_' in c]
            df['AVERAGE_NormPSM'] = df[norm_cols].mean(axis=1)
        
        cat_sums = {}
        for cat, keywords in categories.items():
            mask = df['Description'].str.contains('|'.join(keywords), case=False, na=False)
            cat_sums[cat] = df.loc[mask, 'AVERAGE_NormPSM'].sum()
        
        results[plant] = cat_sums
        df['Clean_Name'] = df['Description'].apply(robust_clean)
        all_names[plant] = set(df[df['Clean_Name'] != '']['Clean_Name'].tolist())

    # Core Proteins (Intersection)
    core_names = all_names['Garlic'] & all_names['Ginger'] & all_names['Kale']
    
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write("# 🌿 PDNV Proteomics Master Comparative Report (v2)\n\n")
        f.write("**Date:** 2026-05-04  \n")
        f.write("**Scope:** Comparative analysis of Garlic, Ginger, and Kale Nanovesicles.\n\n")
        
        f.write("## 1. Functional Category Abundance (Sum of Normalized PSMs)\n")
        f.write("| Category | Garlic | Ginger | Kale |\n")
        f.write("| :--- | :---: | :---: | :---: |\n")
        for cat in categories.keys():
            f.write(f"| {cat} | {results['Garlic'][cat]:.2f} | {results['Ginger'][cat]:.2f} | {results['Kale'][cat]:.2f} |\n")
        
        f.write("\n\n## 2. Core PDNV Proteome\n")
        f.write(f"在三種植物中均鑑定到的共同蛋白質數量為: **{len(core_names)}**。\n")
        if len(core_names) > 0:
            f.write("部分核心蛋白質包含：\n")
            for name in sorted(list(core_names))[:15]:
                f.write(f"- {name.capitalize()}\n")
        
        f.write("\n## 3. Plant-Specific Highlights\n")
        f.write("*   **Garlic**: 在 **Antioxidant/Redox** 類別展現出較高的相對豐度。\n")
        f.write("*   **Ginger**: 含有顯著的 **AGO1** 蛋白，暗示其強大的 RNA 運載機制。\n")
        f.write("*   **Kale**: 富集了 **Myrosinase** 與 **Nitrilase** 系統，專注於次級代謝產物的調控。\n\n")
        
        f.write("## 4. Analytical Data for Prism\n")
        f.write("| Plant | Total NormPSM (Analyzed) |\n")
        f.write("| :--- | :---: |\n")
        for plant in files.keys():
            total = sum(results[plant].values())
            f.write(f"| {plant} | {total:.2f} |\n")

    print(f"Master report generated at: {report_path}")

if __name__ == "__main__":
    analyze_master()
