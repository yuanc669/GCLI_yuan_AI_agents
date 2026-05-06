import os
import numpy as np
import pandas as pd
from PIL import Image
import json

# Mapping generated previously
mapping = {
  "001.jpg": "HS2W", "002.jpg": "HS2W", "003.jpg": "HS2W", "004.jpg": "HS2W", "005.jpg": "HS2W",
  "006.jpg": "HS2W", "007.jpg": "HS2W", "008.jpg": "HS2W", "009.jpg": "HS2W", "010.jpg": "HS2W",
  "011.jpg": "HS2W", "012.jpg": "HS2W", "013.jpg": "HS2W", "014.jpg": "HS2W", "015.jpg": "HS2W",
  "016.jpg": "HS2W", "017.jpg": "HS2W", "018.jpg": "HS2W", "019.jpg": "HS2W", "020.jpg": "HS2W",
  "021.jpg": "HS2W", "022.jpg": "HS2W", "023.jpg": "HS2W", "024.jpg": "Sham", "025.jpg": "Sham",
  "026.jpg": "Sham", "027.jpg": "Sham", "028.jpg": "Sham", "029.jpg": "Sham", "030.jpg": "Sham",
  "031.jpg": "Sham", "032.jpg": "Sham", "033.jpg": "Sham", "034.jpg": "Sham", "035.jpg": "Sham",
  "036.jpg": "Sham", "037.jpg": "Sham", "038.jpg": "Sham", "039.jpg": "Sham", "040.jpg": "Sham",
  "041.jpg": "Sham", "042.jpg": "HS6W", "043.jpg": "HS6W", "044.jpg": "HS6W", "045.jpg": "HS6W",
  "046.jpg": "HS6W", "047.jpg": "HS6W", "048.jpg": "HS6W", "049.jpg": "HS6W", "050.jpg": "HS6W",
  "051.jpg": "HS6W", "052.jpg": "HS6W", "053.jpg": "HS6W", "054.jpg": "HS6W", "055.jpg": "HS6W",
  "056.jpg": "HS6W", "057.jpg": "HS6W", "058.jpg": "HS6W", "059.jpg": "HS6W", "060.jpg": "HS6W",
  "061.jpg": "HS6W", "062.jpg": "HS6W", "063.jpg": "HS6W", "064.jpg": "HS6W", "065.jpg": "HS6W",
  "066.jpg": "HS6W", "067.jpg": "HS6W", "068.jpg": "HS6W", "069.jpg": "HS6W", "070.jpg": "HS6W",
  "071.jpg": "HS6W", "072.jpg": "HS6W", "073.jpg": "HS6W", "074.jpg": "HS6W", "075.jpg": "HS6W",
  "076.jpg": "HS6W", "077.jpg": "HS6W", "078.jpg": "HFD10W", "079.jpg": "HFD10W", "080.jpg": "HFD10W",
  "081.jpg": "HFD10W", "082.jpg": "HFD10W", "083.jpg": "HFD10W", "084.jpg": "HFD10W", "085.jpg": "HFD10W",
  "086.jpg": "HFD10W", "087.jpg": "HFD10W", "088.jpg": "HFD10W", "089.jpg": "HFD10W", "090.jpg": "HFD10W",
  "091.jpg": "HFD10W", "092.jpg": "HFD10W", "093.jpg": "HFD10W", "094.jpg": "HFD10W", "095.jpg": "HFD10W",
  "096.jpg": "HFD10W", "097.jpg": "HFD10W", "098.jpg": "HFD10W", "099.jpg": "HFD10W", "100.jpg": "HFD10W",
  "101.jpg": "HFD10W", "102.jpg": "HFD10W", "103.jpg": "HFD10W", "104.jpg": "HFD10W", "105.jpg": "HFD10W",
  "106.jpg": "HFD10W", "107.jpg": "HFD10W", "108.jpg": "HFD10W", "109.jpg": "HFD10W", "110.jpg": "HFD10W",
  "111.jpg": "HFD10W", "112.jpg": "HFD10W", "113.jpg": "HFD10W", "114.jpg": "HS10W", "115.jpg": "HS10W",
  "116.jpg": "HS10W", "117.jpg": "HS10W", "118.jpg": "HS10W", "119.jpg": "HS10W", "120.jpg": "HS10W",
  "121.jpg": "HS10W", "122.jpg": "HS10W", "123.jpg": "HS10W", "124.jpg": "HS10W", "125.jpg": "HS10W",
  "126.jpg": "HS10W", "127.jpg": "HS10W", "128.jpg": "HS10W", "129.jpg": "HS10W", "130.jpg": "HS10W",
  "131.jpg": "HS10W", "132.jpg": "HS10W", "133.jpg": "HS10W", "134.jpg": "HS10W", "135.jpg": "HS10W",
  "136.jpg": "HS10W", "137.jpg": "HS10W", "138.jpg": "HS10W", "139.jpg": "HS10W", "140.jpg": "HS10W",
  "141.jpg": "HS10W", "142.jpg": "HS10W", "143.jpg": "HS10W", "144.jpg": "HS10W", "145.jpg": "HS10W",
  "146.jpg": "HS10W", "147.jpg": "HS10W", "148.jpg": "HS10W", "149.jpg": "HS10W", "150.jpg": "Sham10W",
  "151.jpg": "Sham10W", "152.jpg": "Sham10W", "153.jpg": "Sham10W", "154.jpg": "Sham10W", "155.jpg": "Sham10W",
  "156.jpg": "Sham10W", "157.jpg": "Sham10W", "158.jpg": "Sham10W", "159.jpg": "Sham10W", "160.jpg": "Sham10W",
  "161.jpg": "Sham10W", "162.jpg": "Sham10W", "163.jpg": "Sham10W", "164.jpg": "Sham10W", "165.jpg": "Sham10W",
  "166.jpg": "Sham10W", "167.jpg": "Sham10W", "168.jpg": "GAE9", "169.jpg": "GAE9", "170.jpg": "GAE9",
  "171.jpg": "GAE9", "172.jpg": "GAE9", "173.jpg": "GAE9", "174.jpg": "GAE9", "175.jpg": "GAE9",
  "176.jpg": "GAE9", "177.jpg": "GAE9", "178.jpg": "GAE9", "179.jpg": "GAE9", "180.jpg": "GAE9",
  "181.jpg": "GAE9", "182.jpg": "GAE9", "183.jpg": "GAE9", "184.jpg": "GAE9", "185.jpg": "GAE9",
  "186.jpg": "GAE9", "187.jpg": "GAE9", "188.jpg": "GAE9", "189.jpg": "GAE9", "190.jpg": "GAE9",
  "191.jpg": "GAE9", "192.jpg": "GAE9", "193.jpg": "GAE9", "194.jpg": "GAE9", "195.jpg": "GAE9",
  "196.jpg": "GAE9", "197.jpg": "GAE9", "198.jpg": "GAE10", "199.jpg": "GAE10", "200.jpg": "GAE10",
  "201.jpg": "GAE10", "202.jpg": "GAE10", "203.jpg": "GAE10", "204.jpg": "GAE10", "205.jpg": "GAE10",
  "206.jpg": "GAE10", "207.jpg": "GAE10", "208.jpg": "GAE10", "209.jpg": "GAE10", "210.jpg": "GAE10",
  "211.jpg": "GAE10", "212.jpg": "GAE10", "213.jpg": "GAE10", "214.jpg": "GAE10", "215.jpg": "GAE10",
  "216.jpg": "GAE10", "217.jpg": "GAE10", "218.jpg": "GAE10", "219.jpg": "GAE10", "220.jpg": "GAE10",
  "221.jpg": "GAE10", "222.jpg": "GAE10", "223.jpg": "GAE10", "224.jpg": "GAE10", "225.jpg": "GAE10",
  "226.jpg": "GAE10", "227.jpg": "GAE10", "228.jpg": "SS10W", "229.jpg": "SS10W", "230.jpg": "SS10W",
  "231.jpg": "SS10W", "232.jpg": "SS10W", "233.jpg": "SS10W", "234.jpg": "SS10W", "235.jpg": "SS10W",
  "236.jpg": "SS10W", "237.jpg": "SS10W", "238.jpg": "SS10W", "239.jpg": "SS10W", "240.jpg": "SS10W",
  "241.jpg": "SS10W", "242.jpg": "SS10W", "243.jpg": "SS10W", "244.jpg": "SS10W", "245.jpg": "SS10W",
  "246.jpg": "SS10W", "247.jpg": "SS10W", "248.jpg": "SS10W", "249.jpg": "SS10W", "250.jpg": "SS10W",
  "251.jpg": "SS10W", "252.jpg": "SS10W", "253.jpg": "SS10W", "254.jpg": "SS10W", "255.jpg": "SS10W",
  "256.jpg": "SS10W", "257.jpg": "SS10W", "258.jpg": "SS10W", "259.jpg": "SS10W", "260.jpg": "SS10W",
  "261.jpg": "SS10W", "262.jpg": "SS10W", "263.jpg": "SS10W", "264.jpg": "HS2W", "265.jpg": "HS2W",
  "266.jpg": "HS2W", "267.jpg": "HS2W", "268.jpg": "HS2W", "269.jpg": "HS2W", "270.jpg": "HS2W"
}

def detect_scale_px(img_path):
    img = Image.open(img_path).convert('L')
    arr = np.array(img)
    h, w = arr.shape
    # User said bottom-left. Focus on bottom 20%, left 30%
    roi = arr[int(h*0.8):, :int(w*0.3)]
    
    # Scale bar in MT is often dark or red. Let's look for dark horizontal lines.
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
    
    # Also check if it's white (sometimes it's a white bar on dark background)
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

def process_mt(img_path, scale_px_per_um):
    img = np.array(Image.open(img_path).convert('RGB')).astype(np.float32)
    r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
    
    # Blue signal: B - R
    blue_signal = b - r
    
    # Tissue mask: non-white
    brightness = (r + g + b) / 3.0
    tissue_mask = brightness < 235
    
    # Threshold for collagen (adjust based on manual check if needed)
    collagen_mask = (blue_signal > 35) & tissue_mask
    
    collagen_px = np.sum(collagen_mask)
    tissue_px = np.sum(tissue_mask)
    
    cvf = (collagen_px / tissue_px) * 100 if tissue_px > 0 else 0
    
    # um2 conversion
    px_to_um2 = (1.0 / scale_px_per_um)**2 if scale_px_per_um > 0 else 1.0
    collagen_um2 = collagen_px * px_to_um2
    tissue_um2 = tissue_px * px_to_um2
    
    return tissue_um2, collagen_um2, cvf

# MAIN
inbox_dir = r"_inbox/DN_GaExo/MT"
results = []

# Detect scale on a few samples to be sure
scales = []
for i in range(1, 11):
    f = f"{i:03d}.jpg"
    scales.append(detect_scale_px(os.path.join(inbox_dir, f)))
median_px = np.median(scales)
# User says 30 um.
scale_px_per_um = median_px / 30.0 if median_px > 0 else 1.0
print(f"Detected Median Scale Bar: {median_px} px for 30 um ({scale_px_per_um:.4f} px/um)")

for f, group in mapping.items():
    img_path = os.path.join(inbox_dir, f)
    if os.path.exists(img_path):
        t_um2, c_um2, cvf = process_mt(img_path, scale_px_per_um)
        results.append({
            "Group": group,
            "File": f,
            "Tissue_Area_um2": t_um2,
            "Collagen_Area_um2": c_um2,
            "CVF_Percent": cvf
        })

df = pd.DataFrame(results)
output_path = r"100_Research/02_Active/DN_GaExo/02_Analysis/MT_Inbox_Analysis_Results.csv"
df.to_csv(output_path, index=False)

summary = df.groupby("Group")["CVF_Percent"].agg(['mean', 'std', 'count']).reset_index()
print("\n--- MT Inbox Analysis Summary ---")
print(summary.to_string(index=False))
