import pandas as pd

def analyze_excel(file_path, name):
    try:
        df = pd.read_excel(file_path)
        print(f"--- {name} ---")
        print("Columns:", df.columns.tolist())
        print("\nFirst 5 rows:")
        print(df.head(5).to_string())
        print("-" * 30)
    except Exception as e:
        print(f"Error reading {name}: {e}")

biochem_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20260225_biochemistry.xlsx'
weight_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\20251001_body weight.xlsx'

analyze_excel(biochem_path, "Biochemistry")
analyze_excel(weight_path, "Body Weight")
