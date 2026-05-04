import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Set paths
file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\Fulltable_target_Garlic_NV.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis'
os.makedirs(output_dir, exist_ok=True)

try:
    # Read merge_countbl sheet
    df = pd.read_excel(file_path, sheet_name='merge_countbl')
    
    # Filter out 'Unaligned'
    df = df[df['Gene_id'] != 'Unaligned'].copy()
    
    # Replicate columns
    reps = ['Garlic-Exo-1_count', 'Garlic-Exo-2_count', 'Garlic-Exo-3_count']
    
    # Calculate Statistics
    df['Mean_Count'] = df[reps].mean(axis=1)
    df['SD'] = df[reps].std(axis=1)
    df['SEM'] = df['SD'] / np.sqrt(len(reps))
    
    # Sort by Mean
    df = df.sort_values('Mean_Count', ascending=False)
    
    # Top 20 for Prism
    top_20 = df.head(20).copy()
    
    # Save Prism CSV
    prism_df = top_20[['Gene_id', 'Mean_Count', 'SD', 'SEM', 'Description', 'Query_seq']]
    prism_df.to_csv(os.path.join(output_dir, 'GaNV_Garlic_miRNA_Prism.csv'), index=False)
    
    # Generate Plot
    plt.figure(figsize=(10, 8))
    top_15 = df.head(15)
    plt.barh(top_15['Gene_id'][::-1], top_15['Mean_Count'][::-1], xerr=top_15['SEM'][::-1], color='lightgreen', capsize=5)
    plt.xlabel('Mean Counts')
    plt.title('Top 15 Garlic-derived miRNAs in GaExo (NV)')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'GaNV_Garlic_miRNA_Bar.png'), dpi=300)
    
    # Print results for the report
    print("Top 10 Garlic miRNAs:")
    print(top_20[['Gene_id', 'Mean_Count', 'Description']].head(10).to_string())
    
    print("\nData processed and files saved.")

except Exception as e:
    print(f"Error: {e}")
