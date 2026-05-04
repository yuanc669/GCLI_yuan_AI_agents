import pandas as pd
import numpy as np
import os

weight_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20251001_body weight.xlsx'
xl = pd.ExcelFile(weight_path)

# Try to find therapy groups in any sheet
for sheet in xl.sheet_names:
    print(f"--- Sheet: {sheet} ---")
    df = xl.parse(sheet)
    # Search for GaE
    mask = df.astype(str).apply(lambda x: x.str.contains('GaE')).any(axis=1)
    if mask.any():
        print(f"Found GaE in sheet {sheet}")
        print(df[mask].head())
    else:
        print(f"No GaE in sheet {sheet}")

# Let's also look for SS
    mask_ss = df.astype(str).apply(lambda x: x.str.contains('SS')).any(axis=1)
    if mask_ss.any():
        print(f"Found SS in sheet {sheet}")
