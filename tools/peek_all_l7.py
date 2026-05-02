import pandas as pd

def peek(file_path):
    try:
        df = pd.read_excel(file_path)
        print(f"File: {file_path}")
        print("Columns:", df.columns.tolist())
        print("-" * 50)
    except Exception as e:
        print(f"Error {file_path}: {e}")

files = [
    r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham_HS2W_HS6W_HS10W-1.xlsx',
    r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\L7_Sham10W_SS10W_HFD10W_HS10W_GaE9W_GaE10W-1.xlsx'
]

for f in files:
    peek(f)
