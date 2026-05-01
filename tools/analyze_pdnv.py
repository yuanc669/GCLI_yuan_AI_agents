import pandas as pd
import numpy as np
import os

files = {
    "Garlic": r"G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\PDNV\25091902-Label-free Quantification Garlic_NV.xlsx",
    "Ginger": r"G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\PDNV\25091902-Label-free Quantification Ginger NV.xlsx",
    "Kale": r"G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\PDNV\25091902-Label-free Quantification Kale NV.xlsx"
}

# Define GO categories by keywords
go_categories = {
    "Stress Response": ["heat shock", "hsp", "chaperone", "stress", "oxidative", "peroxidase", "superoxide"],
    "Vesicle Trafficking/Cytoskeleton": ["clathrin", "syntaxin", "annexin", "rab", "vesicle", "tubulin", "actin", "dynein", "v-type p-type h+-transporting atp synthase"],
    "Protein Synthesis/Ribosome": ["ribosomal", "translation", "elongation factor", "initiation factor"],
    "Metabolism/Energy": ["dehydrogenase", "reductase", "kinase", "synthase", "carboxylase", "rubisco", "atp synthase", "glycolysis", "mitochondrial"],
    "Defense/Signaling": ["myrosinase", "thioglucosidase", "defensin", "pathogenesis", "leucine-rich repeat", "kinase", "signal"]
}

# Established PDNV Markers to search for
markers = [
    "HSP70", "Annexin", "Actin", "GAPDH", "Tubulin", "Clathrin", "V-ATPase", "Syntaxin", "PEN1"
]

results = {}

for name, path in files.items():
    df = pd.read_excel(path)
    data = df.drop(0).reset_index(drop=True)
    norm_psm_cols = [9, 10, 11]
    for col in norm_psm_cols:
        data.iloc[:, col] = pd.to_numeric(data.iloc[:, col], errors='coerce')
    data['Calc_Average'] = data.iloc[:, norm_psm_cols].mean(axis=1)
    
    # Keyword-based GO Profiling
    go_counts = {cat: 0 for cat in go_categories}
    descriptions = data.iloc[:, 1].fillna("").str.lower()
    
    for cat, keywords in go_categories.items():
        mask = descriptions.apply(lambda x: any(kw in x for kw in keywords))
        go_counts[cat] = mask.sum()
        
    # Marker Check
    marker_hits = []
    for m in markers:
        m_lower = m.lower()
        m_mask = descriptions.str.contains(m_lower, regex=False)
        if m_mask.any():
            top_hit = data[m_mask].sort_values(by='Calc_Average', ascending=False).iloc[0]
            marker_hits.append({
                "Marker": m,
                "Accession": top_hit.iloc[0],
                "Average": top_hit['Calc_Average']
            })
    
    results[name] = {
        "count": len(data[data.iloc[:, 0].notna()]),
        "go_profile": go_counts,
        "markers": marker_hits
    }

print("--- GO Profiling (Keyword-based) ---")
for name, data in results.items():
    print(f"\n[{name}] (Total: {data['count']})")
    for cat, count in data['go_profile'].items():
        percentage = (count / data['count']) * 100
        print(f"- {cat}: {count} ({percentage:.1f}%)")

print("\n--- Exosome Marker Comparison ---")
marker_table = []
for name, data in results.items():
    for hit in data['markers']:
        marker_table.append({"Source": name, **hit})

df_markers = pd.DataFrame(marker_table)
if not df_markers.empty:
    pivot_markers = df_markers.pivot(index='Marker', columns='Source', values='Average')
    print(pivot_markers.to_string())
else:
    print("No markers found.")

