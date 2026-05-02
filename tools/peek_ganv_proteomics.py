import pandas as pd

file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\25091902-Label-free Quantification Garlic_NV.xlsx'

try:
    # Read first sheet to see structure
    df = pd.read_excel(file_path)
    print("Columns:", df.columns.tolist())
    print("\nFirst 10 rows:")
    print(df.head(10).to_string())
    
    # Check for multiple sheets
    xl = pd.ExcelFile(file_path)
    print("\nSheet names:", xl.sheet_names)
    
except Exception as e:
    print(f"Error: {e}")
