import pandas as pd
import os

file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\19份研究論文結構化提煉表.xlsx'
try:
    df = pd.read_excel(file_path)
    # 輸出前幾行以確認結構
    print("Columns:", df.columns.tolist())
    print(df.to_csv(index=False))
except Exception as e:
    print(f"Error: {e}")
