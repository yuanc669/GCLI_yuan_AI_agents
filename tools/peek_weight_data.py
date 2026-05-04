import pandas as pd
import numpy as np

# Load the raw weight export
df = pd.read_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\BodyWeight_Raw_Export.csv', header=None)

# The structure is messy. Let's find rows for each group.
# Sham rows: 4, 5, 6, 7, 8, 9
# HFD rows: 10, 11, 12, 13, 14, 15
# HS6W rows: 16, 17, 18, 19, 20, 21
# HS10W rows: 22, 23, 24, 25, 26, 27
# We need GaNV groups too, let's read more of the file to find them.

def get_group_data(rows):
    # Columns for weight are:
    # W0(5W): col 3
    # W7(12W): col 16
    # W11(16W): col 24 (estimate, let's verify)
    # W15(20W): col 32 (estimate, let's verify)
    
    # Actually let's just look at the headers from the CSV content I read:
    # col 3: W0 (5W)
    # col 4: W1 (6W)
    # col 6: W2 (7W)
    # col 8: W3 (8W)
    # col 10: W4 (9W)
    # col 12: W5 (10W)
    # col 14: W6 (11W)
    # col 16: W7 (12W)
    # col 18: W8 (13W)
    # col 20: W9 (14W)
    # col 22: W10 (15W)
    # col 24: W11 (16W)
    # col 26: W12 (17W)
    # col 28: W13 (18W)
    # col 30: W14 (19W)
    # col 32: W15 (20W)
    # col 34: W16 (21W)
    
    indices = [16, 24, 32] # 12W, 16W, 20W
    res = {}
    for i in indices:
        vals = []
        for r in rows:
            val = df.iloc[r, i]
            try:
                vals.append(float(val))
            except:
                pass
        res[i] = np.mean(vals) if vals else np.nan
    return res

# Group row indices (approx based on head read)
groups = {
    'Sham': range(4, 10),
    'HFD': range(10, 16),
    'HS6W': range(16, 22),
    'HS10W': range(22, 28)
}

# Print summary
print("Path 1-7 Body Weight Results Summary:")
for name, rows in groups.items():
    data = get_group_data(rows)
    print(f"{name}: 12W={data[16]:.2f}g, 16W={data[24]:.2f}g, 20W={data[32]:.2f}g")

# I need the GaNV groups. Let's read the rest of the CSV.
