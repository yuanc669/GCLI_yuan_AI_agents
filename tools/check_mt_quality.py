import numpy as np
from PIL import Image
import os

def check_mt_quality(img_path):
    img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32)
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    
    # In MT: Blue (Collagen) should have high B and low R.
    # Red (Cytoplasm) should have high R and low B.
    
    # Calculate contrast between Blue and Red signal
    blue_signal = b - r
    red_signal = r - b
    
    return {
        "blue_max": np.max(blue_signal),
        "red_max": np.max(red_signal),
        "brightness_mean": np.mean((r+g+b)/3.0),
        "resolution": img.shape[:2]
    }

samples = [
    r"_inbox/DN_GaExo/MT/20251126_sham-1_mt_1.jpg",
    r"_inbox/DN_GaExo/MT/20260107_hs10w-1_mt_1.jpg"
]

print("--- MT Image Quality Diagnostic ---")
for s in samples:
    if os.path.exists(s):
        q = check_mt_quality(s)
        print(f"File: {os.path.basename(s)}")
        print(f"  Resolution: {q['resolution']}")
        print(f"  Blue Signal Strength (B-R): {q['blue_max']:.2f}")
        print(f"  Red Signal Strength (R-B): {q['red_max']:.2f}")
        print(f"  Mean Brightness: {q['brightness_mean']:.2f}")
        print("-" * 30)
