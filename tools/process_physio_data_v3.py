import pandas as pd
import numpy as np

# --- 1. Biochemistry ---
biochem_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20260225_biochemistry.xlsx'
df_biochem = pd.read_excel(biochem_path)

numeric_cols = ['BodyWeight (g)', 'BIT', 'SGOT', 'SGPT', 'BUN', 'CRE', 'AC', 'TG', 'CHOL', 'HDL', 'LDL']
for col in numeric_cols:
    if col in df_biochem.columns:
        df_biochem[col] = pd.to_numeric(df_biochem[col].astype(str).str.replace('<', '').replace('取消不做', np.nan), errors='coerce')
if 'CRE' in df_biochem.columns:
    df_biochem.loc[df_biochem['CRE'] < 0.01, 'CRE'] = 0.01

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
df_biochem.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Cleaned_Data.csv', index=False)
# Group stats
summary = df_biochem.groupby('Group')[numeric_cols].mean()
summary_std = df_biochem.groupby('Group')[numeric_cols].std()
summary.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Biochem_Summary_Mean.csv')

# --- 2. Body Weight (Simplified) ---
# Just read and save as is for now if the structure is too complex to auto-parse perfectly, 
# or use a more surgical approach.
weight_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20251001_body weight.xlsx'
# Let's try to extract at least Sham vs HS10W for now
df_w_raw = pd.read_excel(weight_path)
df_w_raw.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Raw_Export.csv', index=False)

print("Biochemistry processing complete.")
