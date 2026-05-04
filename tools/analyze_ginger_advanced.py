import pandas as pd
import os

# Paths
processed_file = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\Ginger_Full_Analysis.csv'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\PDNV\02_Analysis\Advanced'
os.makedirs(output_dir, exist_ok=True)

try:
    df = pd.read_csv(processed_file)
    
    # Define marker groups
    marker_groups = {
        'Classic EV Markers': ['Tetraspanin', 'TET', 'Syntaxin', 'PEN1', 'HSP70', 'Annexin', 'Patellin', 'Rab'],
        'RNA-binding / Cargo': ['RNA-binding', 'Argonaute', 'AGO', 'helicase', 'ribonucleoprotein', 'polyadenylate-binding'],
        'Secondary Metabolism': ['PAL', 'C4H', '4CL', 'phenylalanine ammonia-lyase', 'cinnamate 4-hydroxylase', 'coumarate--CoA ligase', 'protease']
    }

    found_markers = []
    
    for group, keywords in marker_groups.items():
        pattern = '|'.join(keywords)
        mask = df['Description'].str.contains(pattern, case=False, na=False)
        subset = df[mask].copy()
        if not subset.empty:
            subset['Marker_Group'] = group
            # Get rank based on Mean abundance
            subset = subset.sort_values('Mean', ascending=False)
            found_markers.append(subset)

    if found_markers:
        markers_df = pd.concat(found_markers)
        # Global rank
        df_sorted = df.sort_values('Mean', ascending=False).reset_index(drop=True)
        df_sorted['Global_Rank'] = df_sorted.index + 1
        
        # Merge global rank back to markers
        markers_df = markers_df.merge(df_sorted[['Accession', 'Global_Rank']], on='Accession', how='left')
        
        markers_df.to_csv(os.path.join(output_dir, 'Ginger_Advanced_Markers_Benchmarking.csv'), index=False)
        
        print("Advanced Marker Benchmarking Complete.")
        print("\nTop Identified Markers:")
        print(markers_df[['Global_Rank', 'Description', 'Mean', 'Marker_Group']].head(15).to_string())
    else:
        print("No specific markers found with the current keyword set.")

except Exception as e:
    print(f"Error: {e}")
