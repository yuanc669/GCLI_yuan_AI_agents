import os
import numpy as np
import pandas as pd
from PIL import Image
import math

def calculate_od(mean_intensity):
    # OD = log10(Max/Mean)
    if mean_intensity <= 0: return 0
    return math.log10(255.0 / max(mean_intensity, 1.0))

def process_pas_image(img_path, scale_px_per_um=3.7, magenta_threshold=80):
    """
    Quantifies PAS area, tissue area, and optical density.
    """
    img_pil = Image.open(img_path).convert('RGB')
    img = np.array(img_pil)
    
    r = img[:,:,0].astype(np.float32)
    g = img[:,:,1].astype(np.float32)
    b = img[:,:,2].astype(np.float32)
    
    # Calculate Magenta-ness using R - G (PAS staining is pink/magenta)
    # We use (R - G) as a simple proxy for PAS positivity
    magenta_score = r - g
    
    # Brightness filter to exclude white background/empty spaces
    brightness = (r + g + b) / 3.0
    tissue_mask = brightness < 240
    
    # PAS mask
    pas_mask = (magenta_score > magenta_threshold) & tissue_mask
    
    # Area calculation
    px_to_um2 = (1.0 / scale_px_per_um) ** 2
    tissue_area_um2 = np.sum(tissue_mask) * px_to_um2
    pas_area_um2 = np.sum(pas_mask) * px_to_um2
    
    # Mesangial Index (%)
    mesangial_index = (pas_area_um2 / tissue_area_um2 * 100) if tissue_area_um2 > 0 else 0
    
    # Optical Density (OD) of PAS area
    # We use the Green channel for OD as it's the complementary color to magenta
    if np.sum(pas_mask) > 0:
        mean_g_pas = np.mean(g[pas_mask])
        od = calculate_od(mean_g_pas)
    else:
        od = 0
        
    return tissue_area_um2, pas_area_um2, mesangial_index, od

# Main execution
inbox_dir = r"_inbox/DN_GaExo/PAS"
output_csv = r"400_Data/DN/20260506_Inbox_PAS_Analysis_Full.csv"
output_md = r"100_Research/02_Active/DN_GaExo/02_Analysis/03_Pathology/20260506_Inbox_PAS_Analysis_Report.md"

results = []
files = sorted([f for f in os.listdir(inbox_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

print(f"Analyzing {len(files)} images...")

for file_name in files:
    img_path = os.path.join(inbox_dir, file_name)
    try:
        tissue_area, pas_area, m_index, od = process_pas_image(img_path)
        results.append({
            "Image_ID": file_name,
            "Glomerular_Area_um2": tissue_area,
            "PAS_Area_um2": pas_area,
            "Mesangial_Index_Percent": m_index,
            "Optical_Density": od
        })
    except Exception as e:
        print(f"Error processing {file_name}: {e}")

df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)

# Prepare Markdown Report
report_content = f"""# PAS Staining Analysis Report - Inbox Batch
**Date:** 2026-05-06
**Project:** DN_GaExo
**Scope:** Inbox Images (001.jpg - 168.jpg)

## 📊 Summary Statistics
- **Total Images Processed:** {len(df)}
- **Avg Glomerular Area:** {df['Glomerular_Area_um2'].mean():.2f} um²
- **Avg PAS Area:** {df['PAS_Area_um2'].mean():.2f} um²
- **Avg Mesangial Index:** {df['Mesangial_Index_Percent'].mean():.2f}%
- **Avg Optical Density:** {df['Optical_Density'].mean():.4f}

## 🔍 Top 10 Highest Mesangial Index
{df.nlargest(10, 'Mesangial_Index_Percent')[['Image_ID', 'Mesangial_Index_Percent', 'Optical_Density']].to_markdown(index=False)}

## 📂 Data Export
- Detailed results saved to: `{output_csv}`
"""

with open(output_md, 'w', encoding='utf-8') as f:
    f.write(report_content)

print("Analysis complete.")
print(f"Report saved to: {output_md}")
