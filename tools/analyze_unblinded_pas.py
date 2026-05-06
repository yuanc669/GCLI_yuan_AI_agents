import pandas as pd
import numpy as np
import os
import re

def extract_group(filename):
    # Pattern: YYYYMMDD_GroupName-AnimalID_pasN.jpg
    # Handle SHAM vs SHAM10W
    if 'sham' in filename.lower():
        if '(10w)' in filename.lower():
            return 'SHAM10W'
        return 'SHAM'
    
    match = re.search(r'^\d{8}_([a-zA-Z0-9]+)-', filename)
    if match:
        return match.group(1).upper()
    return "UNKNOWN"

# Load unblinded data
csv_path = r"400_Data/DN/20260506_Inbox_PAS_Analysis_Full_unblind.csv"
# The file has encoding issues (likely Big5/CP950), let's try to handle it
try:
    df = pd.read_csv(csv_path, encoding='utf-8')
except UnicodeDecodeError:
    df = pd.read_csv(csv_path, encoding='cp950')

# Extract real filename column (the second column based on read_file output)
# Columns: Index, Real_Filename, Inbox_ID, Image_ID, Area, PAS_Area, Index%, OD
# Renaming for clarity
df.columns = ['Index', 'Original_Filename', 'Inbox_ID', 'Image_ID', 'Glomerular_Area_um2', 'PAS_Area_um2', 'Mesangial_Index_Percent', 'Optical_Density']

# Map groups
df['Group'] = df['Original_Filename'].apply(extract_group)

# Fix specific group names to align with project conventions
group_map = {
    'SS10W': 'SS10W',
    'SHAM': 'Sham',
    'SHAM10W': 'Sham10W',
    'HS10W': 'HS10W',
    'GAE9': 'HS10WGAE9',
    'GAE10': 'HS10WGAE10',
    'HS10WGAE9': 'HS10WGAE9',
    'HS10WGAE10': 'HS10WGAE10',
    'HFD10W': 'HFD10W'
}
df['Group'] = df['Group'].replace(group_map)

# Statistics by Group
stats = df.groupby('Group').agg({
    'Glomerular_Area_um2': ['mean', 'std', 'sem', 'count'],
    'PAS_Area_um2': ['mean', 'std', 'sem'],
    'Mesangial_Index_Percent': ['mean', 'std', 'sem'],
    'Optical_Density': ['mean', 'std', 'sem']
})

# Flatten multi-index columns
stats.columns = ['_'.join(col).strip() for col in stats.columns.values]
stats = stats.reset_index()

# Save unblinded results
output_unblinded_full = r"400_Data/DN/20260506_PAS_Unblinded_Full_Data.csv"
output_summary = r"100_Research/02_Active/DN_GaExo/02_Analysis/06_Prism_Outputs/Path6_PAS_Unblinded_Summary.csv"
df.to_csv(output_unblinded_full, index=False)
stats.to_csv(output_summary, index=False)

# Generate Markdown Report
report_path = r"100_Research/02_Active/DN_GaExo/02_Analysis/03_Pathology/20260506_PAS_Unblinded_Analysis_Report.md"

# Order for display
groups_order = ["Sham", "Sham10W", "SS10W", "HS10W", "HS10WGAE9", "HS10WGAE10"]
stats['Group'] = pd.Categorical(stats['Group'], categories=groups_order, ordered=True)
stats = stats.sort_values('Group')

# Format statistics table for Markdown
display_stats = stats[['Group', 'Mesangial_Index_Percent_mean', 'Mesangial_Index_Percent_sem', 'Optical_Density_mean', 'Glomerular_Area_um2_count']]
display_stats.columns = ['Group', 'Mesangial Index (Mean%)', 'SEM', 'Avg OD', 'N']

report_content = f"""# PAS Staining Unblinded Analysis Report (Group Consistency Check)
**Date:** 2026-05-06
**Project:** DN_GaExo
**Analysis Level:** Group-wise Statistics (Unblinded)

## 📊 Group Summary (Mesangial Index & OD)
{display_stats.to_markdown(index=False)}

## 🧪 Pathological Interpretation
- **Mesangial Expansion:** {stats.loc[stats['Mesangial_Index_Percent_mean'].idxmax(), 'Group']} shows the highest Mesangial Index.
- **Therapeutic Candidates:** HS10WGAE9 and HS10WGAE10 are treated as distinct experimental groups for comparison.

## 📂 Data Assets
- **Unblinded Raw Data:** `{output_unblinded_full}`
- **Prism-Ready Summary:** `{output_summary}`
"""

with open(report_path, 'w', encoding='utf-8') as f:
    f.write(report_content)

print(f"Unblinded analysis complete. Report: {report_path}")
