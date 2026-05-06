import os
import numpy as np
import pandas as pd
from PIL import Image

def detect_scale_px(img_path):
    img = Image.open(img_path).convert('L')
    arr = np.array(img)
    h, w = arr.shape
    roi = arr[int(h*0.8):, :int(w*0.3)]
    
    best_w = 0
    is_dark = roi < 50
    for row in is_dark:
        count = 0
        for val in row:
            if val: count += 1
            else:
                if count > best_w: best_w = count
                count = 0
        if count > best_w: best_w = count
    
    is_white = roi > 200
    best_white = 0
    for row in is_white:
        count = 0
        for val in row:
            if val: count += 1
            else:
                if count > best_white: best_white = count
                count = 0
        if count > best_white: best_white = count
        
    return max(best_w, best_white)

def process_mt_blind(img_path, scale_px_per_um):
    img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32)
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    
    # Fixed algorithm for all images
    blue_signal = b - r
    brightness = (r + g + b) / 3.0
    tissue_mask = brightness < 235
    collagen_mask = (blue_signal > 35) & tissue_mask
    
    collagen_px = np.sum(collagen_mask)
    tissue_px = np.sum(tissue_mask)
    
    cvf = (collagen_px / tissue_px) * 100 if tissue_px > 0 else 0
    
    px_to_um2 = (1.0 / scale_px_per_um)**2 if scale_px_per_um > 0 else 1.0
    return tissue_px * px_to_um2, collagen_px * px_to_um2, cvf

# MAIN
inbox_dir = r"_inbox/DN_GaExo/MT"
output_dir = r"100_Research/02_Active/DN_GaExo/02_Analysis"
results = []

# Detect scale blindly
scales = []
files = sorted([f for f in os.listdir(inbox_dir) if f.lower().endswith('.jpg')])
for f in files[:10]:
    scales.append(detect_scale_px(os.path.join(inbox_dir, f)))
median_px = np.median(scales)
scale_px_per_um = median_px / 30.0

print(f"Blind Scale Detection: {median_px} px for 30 um")

for f in files:
    img_path = os.path.join(inbox_dir, f)
    t_area, c_area, cvf = process_mt_blind(img_path, scale_px_per_um)
    results.append({
        "ID": f.split('.')[0],
        "Filename": f,
        "Tissue_Area_um2": t_area,
        "Collagen_Area_um2": c_area,
        "CVF_Percent": cvf
    })

df = pd.DataFrame(results)
# Save as a pure numeric record
blind_csv_path = os.path.join(output_dir, "MT_Blind_Analysis_Raw_Data.csv")
df.to_csv(blind_csv_path, index=False)

# Generate a blind summary (by index range or just raw)
print(f"\n--- Blind Analysis Complete ---")
print(f"Total processed: {len(df)}")
print(f"Data saved to: {blind_csv_path}")
print(df.head(10).to_string(index=False))
