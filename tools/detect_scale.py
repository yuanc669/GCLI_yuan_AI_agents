from PIL import Image
import numpy as np

def detect_scale_bar(img_path):
    img = Image.open(img_path).convert('L') # Gray
    arr = np.array(img)
    h, w = arr.shape
    
    # Focus on the bottom-left corner (bottom 20%, left 30%)
    roi = arr[int(h*0.8):, :int(w*0.3)]
    
    # Scale bars are usually solid black (0) or white (255)
    # Let's check for a horizontal line of similar pixels
    # We'll look for the longest horizontal continuous segment of very dark or very light pixels
    
    best_width = 0
    # Check for black bar (low values)
    binary_black = (roi < 10).astype(np.uint8)
    for row in binary_black:
        # Find continuous segments of 1s
        count = 0
        for val in row:
            if val == 1:
                count += 1
            else:
                if count > best_width: best_width = count
                count = 0
        if count > best_width: best_width = count

    # Check for white bar (high values)
    best_width_white = 0
    binary_white = (roi > 245).astype(np.uint8)
    for row in binary_white:
        count = 0
        for val in row:
            if val == 1:
                count += 1
            else:
                if count > best_width_white: best_width_white = count
                count = 0
        if count > best_width_white: best_width_white = count

    return max(best_width, best_width_white)

test_img = r"100_Research/02_Active/DN_GaExo/01_Raw_Data/PAS/Sham/20251126_sham-1_pas1.jpg"
width = detect_scale_bar(test_img)
print(f"Detected potential scale bar width in pixels: {width}")
