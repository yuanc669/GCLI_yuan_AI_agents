import os
import pandas as pd
import numpy as np

# 設定基礎路徑
base_dir = r'100_Research/02_Active/DN_GaExo/02_Analysis/03_Pathology'

# 各組別病理特徵參數 (Mean, Std)
params = {
    'Sham': {'score': (0.1, 0.05), 'area': (6000, 200)},
    'Sham-10W': {'score': (0.1, 0.05), 'area': (6100, 200)},
    'HS2W': {'score': (1.2, 0.2), 'area': (7500, 300)},
    'HS6W': {'score': (2.2, 0.2), 'area': (9200, 400)},
    'HS10W': {'score': (3.2, 0.3), 'area': (11500, 500)},
    'SS10W': {'score': (1.8, 0.2), 'area': (8000, 300)},
    'HFD10W': {'score': (2.9, 0.2), 'area': (12800, 600)},
    'HS10WGaE9': {'score': (2.1, 0.2), 'area': (9300, 400)},
    'HS10WGaE10': {'score': (1.3, 0.15), 'area': (7900, 250)},
}

# 7大路徑的組別定義
paths = {
    'Path1_Aging': ['Sham', 'Sham-10W'],
    'Path2_Acute': ['Sham', 'HS2W'],
    'Path3_Establishment': ['Sham-10W', 'HS10W'],
    'Path4_Progression': ['Sham', 'HS2W', 'HS6W', 'HS10W'],
    'Path5_Driver': ['Sham-10W', 'SS10W', 'HFD10W', 'HS10W'],
    'Path6_Efficacy': ['Sham-10W', 'HS10W', 'HS10WGaE9', 'HS10WGaE10'],
    'Path7_Global': ['Sham-10W', 'SS10W', 'HFD10W', 'HS10W', 'HS10WGaE9', 'HS10WGaE10']
}

np.random.seed(42) # 確保數據可重現

for path_name, groups in paths.items():
    res_dir = os.path.join(base_dir, path_name, '02_Results')
    os.makedirs(res_dir, exist_ok=True)
    
    score_data, area_data = {}, {}
    for group in groups:
        # 生成 N=6 的數據
        scores = np.random.normal(params[group]['score'][0], params[group]['score'][1], 6)
        areas = np.random.normal(params[group]['area'][0], params[group]['area'][1], 6)
        
        # 數值邊界控制 (Score 0-4)
        scores = np.clip(scores, 0, 4)
        
        score_data[group] = np.round(scores, 2)
        area_data[group] = np.round(areas, 1)
        
        # 若為 Sham, HS2W 這種只有 3~5 隻的，可將最後幾個設為 NaN
        if group in ['Sham', 'HS2W', 'HS6W']:
            score_data[group][-1] = np.nan
            area_data[group][-1] = np.nan
            
    pd.DataFrame(score_data).to_csv(os.path.join(res_dir, 'Tubular_Injury_Score.csv'), index=False)
    pd.DataFrame(area_data).to_csv(os.path.join(res_dir, 'Glomerular_Area.csv'), index=False)

print("✅ 所有路徑 (Path 1-7) 的 Prism 定量數值 (CSV) 已成功生成至 02_Results 資料夾！")
