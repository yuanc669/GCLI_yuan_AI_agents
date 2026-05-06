import os
import shutil
import re

source_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\04_Pathology_Images"
dest_root = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\HE"

# Define expanded group mapping
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
    moved = False
    for group, pattern in patterns.items():
        if re.search(pattern, file_name, re.IGNORECASE):
            group_dir = os.path.join(dest_root, group)
            if not os.path.exists(group_dir):
                os.makedirs(group_dir)
            
            shutil.copy(os.path.join(source_dir, file_name), os.path.join(group_dir, file_name))
            moved = True
            count += 1
            break
    
    if not moved:
        print(f"Still unknown group for file: {file_name}")

print(f"Successfully organized {count} HE images (including HS2W, HS6W, HFD10W).")
