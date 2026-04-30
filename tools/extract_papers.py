import pandas as pd
import os

path_proteomics = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\KJA\25091902-Label-free Quantification Ginger NV.xlsx'

def analyze_proteomics():
    try:
        # 讀取 Excel，通常數據在第一個或特定 Sheet
        df = pd.read_excel(path_proteomics)
        print(f"\n=== Ginger NV Proteomics Snapshot ({os.path.basename(path_proteomics)}) ===")
        print("Columns:", df.columns.tolist())

        # 尋找蛋白名稱與丰度相關欄位 (假設包含 'Protein' 或 'Accession' 或 'Intensity/PSM')
        # 輸出前 30 行以供人工判讀關鍵蛋白
        print("\nTop 30 Detected Proteins/Peptides:")
        print(df.head(30).to_csv(index=False))

        # 嘗試篩選關鍵字 (Myrosinase, Clathrin, Annexin, RuBisCO)
        keywords = ['Thioglucosidase', 'Myrosinase', 'Clathrin', 'Annexin', 'Ribulose']
        print("\n=== Targeted Keyword Search (Key Active Components) ===")
        for kw in keywords:
            matches = df[df.apply(lambda row: row.astype(str).str.contains(kw, case=False).any(), axis=1)]
            if not matches.empty:
                print(f"Found {kw}: {len(matches)} entries")
                print(matches.iloc[:, :5].to_csv(index=False))

    except Exception as e:
        print(f"Error in Proteomics: {e}")

analyze_proteomics()

