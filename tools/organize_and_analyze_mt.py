import os
import shutil
import re
from PIL import Image
import numpy as np
import pandas as pd

source_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\DN_GaExo\MT"
dest_root = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\MT"

# 1. Organize Images
patterns = {
    "Sham10W": r"sham-[4-6]\(10w\)",
    "Sham": r"sham-[1-3]_",
    "HS2W": r"hs2w-[1-6]_",
    "HS6W": r"hs6w-[1-6]_",
    "HS10W": r"hs10w-[1-6]_",
    "HFD10W": r"hfd10w-[1-6]_",
    "SS10W": r"ss10w-[1-6]_",
    "GAE9": r"hs10wgae9-[1-5]_",
    "GAE10": r"hs10wgae10-[1-5]_"
}

if not os.path.exists(dest_root):
    os.makedirs(dest_root)

files = [f for f in os.listdir(source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.tif'))]
count = 0
for file_name in files:
    for group, pattern in patterns.items():
        if re.search(pattern, file_name, re.IGNORECASE):
            group_dir = os.path.join(dest_root, group)
            if not os.path.exists(group_dir):
                os.makedirs(group_dir)
            shutil.copy(os.path.join(source_dir, file_name), os.path.join(group_dir, file_name))
            count += 1
            break
print(f"Organized {count} MT images.")

# 2. Detect Scale
def detect_scale_bar(img_path):
    img = Image.open(img_path)
    arr = np.array(img)
    h, w, c = arr.shape
    roi = arr[int(h*0.8):, :int(w*0.3)]
    
    # Scale bar in MT seems to be red (high R, low G/B)
    r, g, b = roi[:,:,0].astype(int), roi[:,:,1].astype(int), roi[:,:,2].astype(int)
    is_red = (r > 150) & (g < 100) & (b < 100)
    
    best_width = 0
    for row in is_red:
        count = 0
        for val in row:
            if val:
                count += 1
            else:
                if count > best_width: best_width = count
                count = 0
        if count > best_width: best_width = count
    return best_width

sample_img = os.path.join(dest_root, "Sham", "20251126_sham-1_mt_1.jpg")
px_length = detect_scale_bar(sample_img)
if px_length < 10: 
    # Fallback to simple black/white detection if red fails
    img_gray = Image.open(sample_img).convert('L')
    arr_gray = np.array(img_gray)
    h, w = arr_gray.shape
    roi_gray = arr_gray[int(h*0.8):, :int(w*0.3)]
    best_width = 0
    for row in (roi_gray < 50):
        count = 0
        for val in row:
            if val: count += 1
            else:
                if count > best_width: best_width = count
                count = 0
        if count > best_width: best_width = count
    px_length = best_width

print(f"Detected scale bar length: {px_length} pixels for 30 um.")
scale_px_per_um = px_length / 30.0 if px_length > 0 else 1.0
print(f"Scale: {scale_px_per_um:.3f} px/um")

# 3. Quantify MT CVF%
def process_mt(img_path, scale=scale_px_per_um):
    img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32)
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    
    # Blue signal for collagen: B - R
    blue_signal = b - r
    
    # Filter background (white spaces)
    brightness = (r + g + b) / 3.0
    tissue_mask = brightness < 230
    
    # Threshold for blue collagen
    collagen_mask = (blue_signal > 30) & tissue_mask
    
    collagen_px = np.sum(collagen_mask)
    tissue_px = np.sum(tissue_mask)
    
    px_to_um2 = (1.0 / scale) ** 2 if scale > 0 else 1.0
    collagen_um2 = collagen_px * px_to_um2
    tissue_um2 = tissue_px * px_to_um2
    
    cvf = (collagen_px / tissue_px) * 100 if tissue_px > 0 else 0
    return tissue_um2, collagen_um2, cvf

results = []
groups = ["Sham", "Sham10W", "HS2W", "HS6W", "HS10W", "HFD10W", "SS10W", "GAE9", "GAE10"]

print("Starting MT quantification...")
for group in groups:
    group_dir = os.path.join(dest_root, group)
    if not os.path.exists(group_dir): continue
    files = [f for f in os.listdir(group_dir) if f.lower().endswith(('.jpg', '.png'))]
    for file_name in files:
        try:
            t_um2, c_um2, cvf = process_mt(os.path.join(group_dir, file_name))
            results.append({
                "Group": group,
                "Sample": file_name,
                "Tissue_Area_um2": t_um2,
                "Collagen_Area_um2": c_um2,
                "CVF_Percent": cvf
            })
        except Exception as e:
            print(f"Error on {file_name}: {e}")

output_csv = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\MT_Fibrosis_Results.csv"
df = pd.DataFrame(results)
df.to_csv(output_csv, index=False)

summary = df.groupby("Group")["CVF_Percent"].agg(['mean', 'std', 'count']).reset_index()
print("\n--- MT Analysis Summary (CVF %) ---")
print(summary.to_string(index=False))
print(f"Saved to {output_csv}")
