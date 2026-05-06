import numpy as np
from PIL import Image
import os

def get_stats(img_path):
    img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32)
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    
    # Try different formulas
    magenta_1 = (r + b) / 2.0 - g
    magenta_2 = r - g
    magenta_3 = (r - g) / (r + g + b + 1e-5)
    
    return {
        "m1_mean": np.mean(magenta_1),
        "m1_max": np.max(magenta_1),
        "m2_mean": np.mean(magenta_2),
        "m2_max": np.max(magenta_2),
        "m3_mean": np.mean(magenta_3),
        "m3_max": np.max(magenta_3)
    }

sham_img = r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS/Sham/20251126_sham-1_pas1.jpg"
hs_img = r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS/HS10W/20260107_hs10w-1_pas1.jpg"

print("--- Color Stats Diagnostic ---")
if os.path.exists(sham_img) and os.path.exists(hs_img):
    sham_stats = get_stats(sham_img)
    hs_stats = get_stats(hs_img)
    
    for key in sham_stats:
        print(f"{key:<10} | Sham: {sham_stats[key]:>8.2f} | HS10W: {hs_stats[key]:>8.2f}")
else:
    print("Test images not found.")
