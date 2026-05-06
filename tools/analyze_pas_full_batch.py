import os
import numpy as np
import pandas as pd
from PIL import Image

def process_pas_final(img_path, scale_px_per_um=1.2, fixed_threshold=25):
    """
    Final optimized PAS quantification logic.
    """
    img_pil = Image.open(img_path).convert('RGB')
    img = np.array(img_pil)
    
    r = img[:,:,0].astype(np.float32)
    g = img[:,:,1].astype(np.float32)
    b = img[:,:,2].astype(np.float32)
    
    # Calculate "Magenta-ness" score: (R+B)/2 - G
    magenta_score = (r + b) / 2.0 - g
    
    # Use fixed threshold for consistency across groups
    mask = magenta_score > fixed_threshold
    
    # Area in pixels
    pas_area_px = np.sum(mask)
    total_area_px = mask.size
    
    # Unit conversion (um^2)
    # 1 pixel = (1/scale_px_per_um) um
    # 1 pixel^2 = (1/scale_px_per_um)^2 um^2
    px_to_um2 = (1.0 / scale_px_per_um) ** 2
    
    pas_area_um2 = pas_area_px * px_to_um2
    total_area_um2 = total_area_px * px_to_um2
    mesangial_index = (pas_area_px / total_area_px) * 100
    
    return total_area_um2, pas_area_um2, mesangial_index

# Configuration
data_root = r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS"
groups = ["Sham", "Sham10W", "HS10W", "SS10W", "GAE9", "GAE10"]
output_csv = r"400_Data/DN/PAS_Master_Results.csv"

results = []

print(f"Starting batch analysis for {len(groups)} groups...")

for group in groups:
    group_dir = os.path.join(data_root, group)
    if not os.path.exists(group_dir):
        print(f"Warning: Directory not found for group {group}")
        continue
    
    files = [f for f in os.listdir(group_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.tif'))]
    print(f"Processing group {group}: {len(files)} images")
    
    for file_name in files:
        img_path = os.path.join(group_dir, file_name)
        try:
            total_um2, pas_um2, m_index = process_pas_final(img_path)
            results.append({
                "Group": group,
                "Sample": file_name,
                "Glomerular_Area_um2": total_um2,
                "PAS_Area_um2": pas_um2,
                "Mesangial_Index_Percent": m_index
            })
        except Exception as e:
            print(f"Error processing {file_name}: {e}")

# Save to CSV
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)

# Generate Summary
summary = df.groupby("Group")["Mesangial_Index_Percent"].agg(['mean', 'std', 'count']).reset_index()
print("\n--- PAS Analysis Summary (Mesangial Index %) ---")
print(summary.to_string(index=False))
print(f"\nFull results saved to: {output_csv}")
