import os
import numpy as np
import pandas as pd
from PIL import Image

def process_pas_corrected(img_path, scale_px_per_um=1.2, fixed_threshold=80):
    """
    Corrected PAS quantification logic:
    - Uses R - G for better specificity.
    - Higher threshold to filter background.
    - Brightness filter to exclude empty spaces.
    """
    img_pil = Image.open(img_path).convert('RGB')
    img = np.array(img_pil)
    
    r = img[:,:,0].astype(np.float32)
    g = img[:,:,1].astype(np.float32)
    b = img[:,:,2].astype(np.float32)
    
    # Calculate Magenta-ness using R - G
    magenta_score = r - g
    
    # Brightness filter: Exclude very bright pixels (white background)
    brightness = (r + g + b) / 3.0
    valid_tissue_mask = brightness < 240
    
    # Final mask: Magenta score > threshold AND not empty white space
    mask = (magenta_score > fixed_threshold) & valid_tissue_mask
    
    # Area in pixels
    pas_area_px = np.sum(mask)
    total_area_px = np.sum(valid_tissue_mask) # Calculate relative to total tissue area, not full field
    
    # Unit conversion (um^2)
    px_to_um2 = (1.0 / scale_px_per_um) ** 2
    
    pas_area_um2 = pas_area_px * px_to_um2
    total_tissue_um2 = total_area_px * px_to_um2
    mesangial_index = (pas_area_px / total_area_px) * 100 if total_area_px > 0 else 0
    
    return total_tissue_um2, pas_area_um2, mesangial_index

# Configuration
data_root = r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS"
groups = ["Sham", "Sham10W", "HS10W", "SS10W", "GAE9", "GAE10"]
output_csv = r"400_Data/DN/PAS_Master_Results_Corrected.csv"

results = []

for group in groups:
    group_dir = os.path.join(data_root, group)
    if not os.path.exists(group_dir): continue
    
    files = [f for f in os.listdir(group_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.tif'))]
    
    for file_name in files:
        img_path = os.path.join(group_dir, file_name)
        try:
            total_um2, pas_um2, m_index = process_pas_corrected(img_path)
            results.append({
                "Group": group,
                "Sample": file_name,
                "Tissue_Area_um2": total_um2,
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
print("\n--- Corrected PAS Analysis Summary (Threshold=80) ---")
print(summary.to_string(index=False))
