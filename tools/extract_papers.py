import pandas as pd
import numpy as np

path_biochem = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\DN_GaExo\20260225.xlsx'
path_weight = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\DN_GaExo\20251001.xlsx'

def map_group(sid):
    sid = str(sid)
    if 'Sham' in sid: return 'Sham'
    if 'SS' in sid: return 'SS'
    if 'HFD' in sid: return 'HFD'
    if 'HS' in sid and 'Ga' not in sid: return 'HS'
    if 'Ga' in sid: return 'GaE'
    return 'Other'

def analyze():
    # 1. 血清生化分析
    try:
        df_bio = pd.read_excel(path_biochem)
        df_bio['Group'] = df_bio['SampleID'].apply(map_group)
        
        metrics = ['BUN', 'CRE', 'AC', 'TG', 'CHOL', 'SGOT', 'SGPT', 'HDL', 'LDL']
        # 強制轉換為數值
        for m in metrics:
            if m in df_bio.columns:
                df_bio[m] = pd.to_numeric(df_bio[m], errors='coerce')
        
        biochem_summary = df_bio.groupby('Group')[metrics].mean()
        print("\n=== Serum Biochemistry Grouped Means ===")
        print(biochem_summary.to_csv())
        
        if 'HS' in biochem_summary.index and 'GaE' in biochem_summary.index:
            diff = biochem_summary.loc['GaE'] - biochem_summary.loc['HS']
            print("\n=== Therapeutic Effect (GaE - HS) ===")
            print(diff.to_csv())
    except Exception as e:
        print(f"Error in Biochem: {e}")

    # 2. 體重趨勢分析
    try:
        df_w = pd.read_excel(path_weight, header=None)
        # 修正 ffill
        df_w[0] = df_w[0].ffill()
        df_w['Group'] = df_w[0].apply(map_group)
        
        # 提取第 3 到第 15 欄 (W0-W12 區間)
        weight_matrix = df_w.groupby('Group').apply(lambda x: x.iloc[:, 3:16].apply(pd.to_numeric, errors='coerce').mean(numeric_only=True))
        print("\n=== Body Weight Trend (W0 - W12) ===")
        print(weight_matrix.to_csv())
    except Exception as e:
        print(f"Error in Weight: {e}")

analyze()
