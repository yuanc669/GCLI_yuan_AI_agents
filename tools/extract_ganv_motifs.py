import pandas as pd

# Load processed proteomics data
file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Proteomics_Processed.csv'
df = pd.read_csv(file_path)

# Ensure numeric and sort
df['AVERAGE_NormPSM'] = pd.to_numeric(df['AVERAGE_NormPSM'], errors='coerce')
top_100 = df.sort_values('AVERAGE_NormPSM', ascending=False).head(100).copy()

# Functional keywords for Direction 2 & 3
keywords = {
    'Chaperone/HSP': ['heat shock', 'hsp', 'chaperone', 'dnaj', 'dnak'],
    'Signaling/Hub': ['14-3-3', 'kinase', 'phosphatase', 'binding', 'annexin'],
    'Transcription Factor': ['transcription factor', 'erf', 'tiny', 'myb', 'zinc finger', 'wrky', 'bzip'],
    'Metabolism/Lipase': ['lipase', 'esterase', 'hydrolase', 'gdsl'],
    'Antioxidant/Redox': ['peroxidase', 'dismutase', 'reductase', 'thioredoxin', 'glutathione'],
    'Transport/Exosome': ['transporter', 'channel', 'porin', 'v-atpase', 'clathrin']
}

def identify_motifs(desc):
    desc = str(desc).lower()
    found = []
    for cat, keys in keywords.items():
        if any(key in desc for key in keys):
            found.append(cat)
    return ', '.join(found) if found else 'Structural/Other'

top_100['Motif_Category'] = top_100['Description'].apply(identify_motifs)

# Filter for the most interesting ones for Mechanism Storyline
regulatory_hubs = top_100[top_100['Motif_Category'].str.contains('Transcription Factor|Signaling|Chaperone')]

# Save the Top 100 with Motifs
top_100.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\GaNV_Top100_Motif_Analysis.csv', index=False)

print("Top 100 Motif Analysis Complete.")
print("\nRegulatory Hubs identified (Signaling/TF/Chaperone):")
print(regulatory_hubs[['Accession', 'Motif_Category', 'AVERAGE_NormPSM']].head(15).to_string())

# Summary of categories in Top 100
print("\nCategory Distribution in Top 100 (PSM Sum):")
summary = top_100.groupby('Motif_Category')['AVERAGE_NormPSM'].sum().sort_values(ascending=False)
print(summary.to_string())
