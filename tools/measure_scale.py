import numpy as np
from PIL import Image
import os

def detect_scale_bar_pixels(img_path):
    img = Image.open(img_path).convert('L')
    arr = np.array(img)
    h, w = arr.shape
    
    # Focus on the bottom-left corner (bottom 10%, left 20%)
    roi = arr[int(h*0.9):, :int(w*0.2)]
    
    # Scale bars are usually black lines (low values) on a lighter background
    # Let's find the longest horizontal black segment
    # Binary thresholding to find black pixels
    binary = roi < 50
    
    max_len = 0
    for row in binary:
        # Find continuous True segments
        current_len = 0
        for val in row:
            if val:
                current_len += 1
            else:
                if current_len > max_len:
                    max_len = current_len
                current_len = 0
        if current_len > max_len:
            max_len = current_len
            
    return max_len

inbox_dir = r"_inbox/DN_GaExo/PAS"
sample_img = os.path.join(inbox_dir, "001.jpg")
px_len = detect_scale_bar_pixels(sample_img)
print(f"Detected scale bar length: {px_len} pixels")
