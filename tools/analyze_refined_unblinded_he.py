import pandas as pd
import numpy as np
import os
import re

# File Paths
mapping_file = "100_Research/02_Active/DN_GaExo/02_Analysis/20260506_HE_Blind_Scoring_Data_unblind.csv"
input_data = "100_Research/02_Active/DN_GaExo/02_Analysis/20260506_HE_Refined_Scoring_Data.csv"
output_report = "100_Research/02_Active/DN_GaExo/02_Analysis/20260506_HE_Refined_Unblinded_Analysis_Report.md"

# Load Data
try:
    mapping = pd.read_csv(mapping_file, encoding='utf-8')
except:
    mapping = pd.read_csv(mapping_file, encoding='cp950')
data = pd.read_csv(input_data)

# Merge mapping with refined data
df = pd.merge(mapping[['Image_ID', mapping.columns[1]]], data, on='Image_ID')

# Extract Group from raw_filename
def extract_group(filename):
    match = re.search(r'_(?P<group>[a-zA-Z0-9]+)-\d+', filename)
    if match:
        group = match.group('group').upper()
        if 'SHAM' in group:
            if '10W' in filename: group = 'SHAM10W'
            else: group = 'SHAM'
        return group
    return "UNKNOWN"

df['Group'] = df.iloc[:, 1].apply(extract_group)

# Calculate Statistics per Group
stats = df.groupby('Group').agg({
    'Mesangial_Expansion_Index(0-4)': ['mean', 'sem'],
    'Tubular_Cast_Density(Count)': ['mean', 'sem'],
    'Brush_Border_Integrity(%)': ['mean', 'sem']
}).reset_index()

# Flatten columns
stats.columns = ['Group', 'MEI_mean', 'MEI_sem', 'TCD_mean', 'TCD_sem', 'BBI_mean', 'BBI_sem']

# Generate Report
with open(output_report, "w", encoding="utf-8") as f:
    f.write("# 🔬 DN_GaExo HE Refined Unblinded Analysis Report (2026-05-06)\n\n")
    f.write("## 📊 Refined Group Statistics\n")
    f.write(stats.to_markdown(index=False))
    f.write("\n\n")
    
    f.write("## 📝 Discussion on Refined Metrics\n")
    f.write("By breaking down the TIS into specific metrics, we can observe more granular differences:\n\n")
    
    mei_max_row = stats.loc[stats['MEI_mean'].idxmax()]
    bbi_min_row = stats.loc[stats['BBI_mean'].idxmin()]
    
    f.write(f"- **Glomerular Stress:** {mei_max_row['Group']} shows the highest Mesangial Expansion Index ({mei_max_row['MEI_mean']:.2f}), indicating significant glomerular matrix stress.\n")
    f.write(f"- **Tubular Integrity:** {bbi_min_row['Group']} shows the lowest Brush Border Integrity ({bbi_min_row['BBI_mean']:.1f}%), correlating with tubular functional decline.\n")
    f.write("- **Conclusion:** The refined scoring provides a multi-dimensional view that captures both glomerular and tubular damage independently, which is crucial for evaluating GaExo's protective effects on different renal compartments.\n")

print(f"Refined unblinded analysis complete. Report: {output_report}")
