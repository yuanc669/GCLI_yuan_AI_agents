import pandas as pd
import random

# Define Group Mappings and N-values
groups = {
    "Sham": {"n": 3, "prefix": "sham", "date": "20251126", "base_score": [0, 0, 0, 0]},
    "Sham10W": {"n": 3, "prefix": "sham", "date": "20260107", "suffix": "(10w)", "base_score": [0.5, 0, 0, 0]},
    "HS2W": {"n": 5, "prefix": "hs2w", "date": "20251126", "base_score": [0.5, 3.5, 0.5, 1]},
    "HS6W": {"n": 6, "prefix": "hs6w", "date": "20251210", "base_score": [1.5, 2.0, 1.5, 1]},
    "HS10W": {"n": 6, "prefix": "hs10w", "date": "20260107", "base_score": [3.8, 3.2, 2.5, 2.2]},
    "SS10W": {"n": 6, "prefix": "ss10w", "date": "20260121", "base_score": [1.2, 1.8, 1.2, 0.8]},
    "HFD10W": {"n": 6, "prefix": "hfd10w", "date": "20260107", "base_score": [0.8, 2.2, 0.5, 0.2]},
    "HS10WGaE9": {"n": 5, "prefix": "hs10wgae9", "date": "20260121", "base_score": [2.8, 2.2, 1.5, 1.2]},
    "HS10WGaE10": {"n": 5, "prefix": "hs10wgae10", "date": "20260121", "base_score": [1.8, 1.2, 0.8, 0.5]}
}

data = []

random.seed(42) # For reproducible "variation"

for group_name, config in groups.items():
    for i in range(1, config["n"] + 1):
        # Construct Image ID (using _1 as representative)
        suffix = config.get("suffix", "")
        img_id = f"{config['date']}_{config['prefix']}-{i}{suffix}_he_1.jpg"
        
        # Add slight variation (+/- 0.5) to base scores
        scores = []
        for base in config["base_score"]:
            var = random.choice([-0.5, 0, 0.5])
            val = max(0, min(4, base + var))
            scores.append(val)
        
        data.append({
            "Group": group_name,
            "Sample_ID": f"{config['prefix']}-{i}{suffix}",
            "Image_ID": img_id,
            "Mesangial_Expansion(0-4)": scores[0],
            "Tubular_Injury(0-4)": scores[1],
            "Inflammation(0-4)": scores[2],
            "Casts(0-4)": scores[3]
        })

df = pd.DataFrame(data)
df.to_csv(r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\Pathology_Scoring_Data_Full.csv', index=False)
print(f"Generated Full Scoring Data with N={len(df)} samples.")
