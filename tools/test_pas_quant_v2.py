from PIL import Image
import numpy as np
import os

def process_pas_v2(img_path, output_path):
    # Load image with Pillow
    img_pil = Image.open(img_path).convert('RGB')
    img = np.array(img_pil)
    
    r = img[:,:,0].astype(np.float32)
    g = img[:,:,1].astype(np.float32)
    b = img[:,:,2].astype(np.float32)
    
    # Calculate "Magenta-ness" score: (R+B)/2 - G
    # PAS magenta is high in R and B, low in G.
    magenta_score = (r + b) / 2.0 - g
    
    # Simple thresholding based on the score
    # Values > 25 (empirically found for PAS) are likely positive
    # We can use a percentile to be more adaptive
    threshold = np.percentile(magenta_score, 90) # Top 10% is usually the target
    if threshold < 20: threshold = 20 # Minimum threshold to avoid noise in clean samples
    
    mask = magenta_score > threshold
    
    pas_area = np.sum(mask)
    total_area = mask.size
    pas_percent = (pas_area / total_area) * 100
    
    # Create visual verification image
    mask_img = np.zeros_like(img)
    mask_img[mask] = [255, 255, 255]
    
    overlay = img.copy()
    overlay[mask] = [255, 0, 255] # Mark as Magenta
    
    # Concatenate results: Original | Mask | Overlay
    combined = np.concatenate((img, mask_img, overlay), axis=1)
    Image.fromarray(combined).save(output_path)
    
    return pas_percent

# Test files
test_files = [
    r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS/Sham/20251126_sham-1_pas1.jpg",
    r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS/HS10W/20260107_hs10w-1_pas1.jpg",
    r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS/GAE10/20260121_hs10wgae10-1_pas1.jpg"
]

output_dir = "400_Data/DN/PAS_Test_Results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"{'File Name':<40} | {'PAS Area %':<10}")
print("-" * 55)

for f in test_files:
    if os.path.exists(f):
        base = os.path.basename(f)
        out = os.path.join(output_dir, f"test_v2_{base}")
        try:
            percent = process_pas_v2(f, out)
            print(f"{base:<40} | {percent:>10.2f}%")
        except Exception as e:
            print(f"Error processing {base}: {e}")
    else:
        print(f"File not found: {f}")
