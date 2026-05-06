import cv2
import numpy as np
import os
from skimage import io, color, morphology

def process_pas(img_path, output_path):
    # Read image
    img = io.imread(img_path)
    if img.shape[2] == 4: # Handle RGBA
        img = color.rgba2rgb(img)
        img = (img * 255).astype(np.uint8)
    
    # Convert to LAB
    img_lab = color.rgb2lab(img)
    a_channel = img_lab[:,:,1]
    
    # Normalize a_channel for thresholding
    a_min, a_max = a_channel.min(), a_channel.max()
    a_norm = ((a_channel - a_min) / (a_max - a_min) * 255).astype(np.uint8)
    
    # Use Otsu's thresholding on 'a' channel to find pink/red areas
    _, mask = cv2.threshold(a_norm, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    # Morphological cleaning: Remove small objects
    mask_bool = mask > 0
    cleaned_mask = morphology.remove_small_objects(mask_bool, min_size=50)
    final_mask = (cleaned_mask.astype(np.uint8) * 255)
    
    # Calculate PAS %
    pas_area = np.sum(cleaned_mask)
    total_area = cleaned_mask.size
    pas_percent = (pas_area / total_area) * 100
    
    # Create overlay for visual check (Magenta overlay)
    overlay = img.copy()
    overlay[final_mask > 0] = [255, 0, 255] # Mark detected area as bright magenta
    combined = np.hstack((img, cv2.cvtColor(final_mask, cv2.COLOR_GRAY2RGB), cv2.addWeighted(img, 0.7, overlay, 0.3, 0)))
    
    # Save result
    cv2.imwrite(output_path, cv2.cvtColor(combined, cv2.COLOR_RGB2BGR))
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
        out = os.path.join(output_dir, f"test_{base}")
        try:
            percent = process_pas(f, out)
            print(f"{base:<40} | {percent:>10.2f}%")
        except Exception as e:
            print(f"Error processing {base}: {e}")
    else:
        print(f"File not found: {f}")
