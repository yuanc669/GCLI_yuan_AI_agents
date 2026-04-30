import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

csv_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\KJA\GiNV_heatmap.csv'

def run_viz():
    # 1. 讀取並處理 Top 30 Heatmap 數據 (CSV 源)
    # 跳過第一行 Label 列
    df = pd.read_csv(csv_path, skiprows=[1])
    
    # 計算平均值並取 Top 30
    df['Mean_Exp'] = df[['GiNV-1', 'GiNV-2', 'GiNV-3']].apply(pd.to_numeric, errors='coerce').mean(axis=1)
    top30 = df.sort_values('Mean_Exp', ascending=False).head(30)
    
    heatmap_data = top30.set_index('Sample')[['GiNV-1', 'GiNV-2', 'GiNV-3']]
    heatmap_data = heatmap_data.apply(pd.to_numeric, errors='coerce').fillna(0)

    # 繪製 Heatmap
    plt.figure(figsize=(10, 12))
    sns.heatmap(heatmap_data, annot=True, cmap="YlOrRd", fmt=".1f", cbar_kws={'label': 'Normalized Intensity'})
    plt.title('Top 30 Proteins in Ginger NV (Source: GiNV_heatmap.csv)')
    plt.ylabel('Accession')
    plt.tight_layout()
    plt.savefig(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\AP_GiNV\AP_GiNV_Top30_Heatmap_v2.png', dpi=300)
    
    # 儲存對應的 CSV
    top30.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\400_Data\Methodology\AP_GiNV_Top30_Proteins_Heatmap_v2.csv', index=False)
    print("New Heatmap and CSV saved (v2).")

run_viz()
