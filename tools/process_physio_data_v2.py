import pandas as pd
import numpy as np

# --- 1. Process Biochemistry ---
biochem_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20260225_biochemistry.xlsx'
df_biochem = pd.read_excel(biochem_path)

# Handle special values in all columns
numeric_cols = ['BodyWeight (g)', 'BIT', 'SGOT', 'SGPT', 'BUN', 'CRE', 'AC', 'TG', 'CHOL', 'HDL', 'LDL']

for col in numeric_cols:
    if col in df_biochem.columns:
        # First convert to string, replace '<' with empty, then to numeric
        df_biochem[col] = pd.to_numeric(df_biochem[col].astype(str).str.replace('<', '').replace('取消不做', np.nan), errors='coerce')

# Apply the 0.01 floor for CRE specifically as requested
if 'CRE' in df_biochem.columns:
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

# Stats (Mean, Std) - excluding NaNs automatically
biochem_summary = df_biochem.groupby('Group')[numeric_cols].agg(['mean', 'std']).reset_index()
df_biochem.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Cleaned_Data.csv', index=False)
biochem_summary.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Summary.csv', index=False)

# --- 2. Process Body Weight ---
weight_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20251001_body weight.xlsx'
df_w_raw = pd.read_excel(weight_path, header=None)

weeks = df_w_raw.iloc[0].values
df_w_data = df_w_raw.iloc[3:].copy()
df_w_data.columns = [f"Col_{i}" for i in range(df_w_raw.shape[1])]

weight_records = []
current_group = ""

for idx, row in df_w_data.iterrows():
    g_val = str(row['Col_0'])
    if g_val != 'nan' and g_val != "":
        current_group = g_val
    
    sid = str(row['Col_2'])
    if sid == 'nan' or sid == "": continue
    
    for col_idx in range(3, len(weeks)):
        w_label = str(weeks[col_idx])
        if w_label.startswith('W') and ' ' not in w_label:
            val = pd.to_numeric(row[f'Col_{col_idx}'], errors='coerce')
            if not np.isnan(val):
                weight_records.append({
                    'Group': current_group,
                    'SampleID': sid,
                    'Week': w_label,
                    'Weight': val
                })

df_weight = pd.DataFrame(weight_records)
group_fix = {
    'Sham': 'Sham', 'HS 2W': 'HS2W', 'HS 6W': 'HS6W', 'HS 10W': 'HS10W',
    'SS 10W': 'SS10W', 'HFD 10W': 'HFD10W', 'GaE9': 'HS10WGaE9',
    'GaE10': 'HS10WGaE10', 'Sham 10W': 'Sham10W'
}
df_weight['Group'] = df_weight['Group'].replace(group_fix)

df_weight.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Cleaned_Data.csv', index=False)
weight_summary = df_weight.groupby(['Group', 'Week'])['Weight'].agg(['mean', 'std']).reset_index()
weight_summary.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Summary.csv', index=False)

print("Analysis Complete. Summaries saved to 02_Analysis folder.")
