import pandas as pd
import numpy as np

# --- 1. Process Biochemistry ---
biochem_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20260225_biochemistry.xlsx'
df_biochem = pd.read_excel(biochem_path)

# Clean CRE
df_biochem['CRE'] = df_biochem['CRE'].astype(str).str.replace('<', '').astype(float)
df_biochem.loc[df_biochem['CRE'] < 0.01, 'CRE'] = 0.01

# Map Groups
def map_group(sid):
    sid = str(sid)
    if 'Sham(10W)' in sid or 'Sham10W' in sid: return 'Sham10W'
    if 'Sham' in sid: return 'Sham'
    if 'SS10W' in sid: return 'SS10W'
    if 'HFD10W' in sid: return 'HFD10W'
    if 'HS10WGaE9' in sid: return 'HS10WGaE9'
    if 'HS10WGaE10' in sid: return 'HS10WGaE10'
    if 'HS10W' in sid: return 'HS10W'
    if 'HS2W' in sid: return 'HS2W'
    if 'HS6W' in sid: return 'HS6W'
    return 'Unknown'

df_biochem['Group'] = df_biochem['SampleID'].apply(map_group)

# Stats
biochem_summary = df_biochem.groupby('Group').agg(['mean', 'std']).reset_index()
df_biochem.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Cleaned_Data.csv', index=False)

# --- 2. Process Body Weight ---
weight_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20251001_body weight.xlsx'
# Load without header to handle the complex structure
df_w_raw = pd.read_excel(weight_path, header=None)

# Identify Week columns from row 0
# Row 0: NaN, NaN, 入室, W0, W1, NaN, W2...
weeks = df_w_raw.iloc[0].values
# Row 1: NaN, NaN, 週齡, 5W, 6W, NaN, 7W...
age = df_w_raw.iloc[1].values

# Data starts from row 3
df_w_data = df_w_raw.iloc[3:].copy()
df_w_data.columns = [f"Col_{i}" for i in range(df_w_raw.shape[1])]

# Re-map groups and format for timeline
weight_records = []
current_group = ""

for idx, row in df_w_data.iterrows():
    g_val = str(row['Col_0'])
    if g_val != 'nan' and g_val != "":
        current_group = g_val
    
    sid = str(row['Col_2'])
    if sid == 'nan' or sid == "": continue
    
    # Iterate through columns to find week weights
    for col_idx in range(3, len(weeks)):
        w_label = str(weeks[col_idx])
        if w_label.startswith('W') and ' ' not in w_label:
            val = row[f'Col_{col_idx}']
            if isinstance(val, (int, float)) and not np.isnan(val):
                weight_records.append({
                    'Group': current_group,
                    'SampleID': sid,
                    'Week': w_label,
                    'Weight': val
                })

df_weight = pd.DataFrame(weight_records)

# Fix group names in weight data to match project standard
group_fix = {
    'Sham': 'Sham',
    'HS 2W': 'HS2W',
    'HS 6W': 'HS6W',
    'HS 10W': 'HS10W',
    'SS 10W': 'SS10W',
    'HFD 10W': 'HFD10W',
    'GaE9': 'HS10WGaE9',
    'GaE10': 'HS10WGaE10',
    'Sham 10W': 'Sham10W'
}
df_weight['Group'] = df_weight['Group'].replace(group_fix)

df_weight.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Cleaned_Data.csv', index=False)

# Summary for weights
weight_summary = df_weight.groupby(['Group', 'Week'])['Weight'].agg(['mean', 'std']).reset_index()
weight_summary.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Summary.csv', index=False)

print("Biochemistry Group Counts:")
print(df_biochem['Group'].value_counts())
print("\nBody Weight Group Counts:")
print(df_weight['Group'].value_counts() // 10) # rough estimate of n per group
