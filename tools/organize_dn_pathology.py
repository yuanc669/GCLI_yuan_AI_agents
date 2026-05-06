import os
import shutil

# Source and target directories
src_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\01_Raw_Data\04_Pathology_Images'
base_out_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\DN_GaExo\02_Analysis\03_Pathology'

# Path definitions (based on Working Notes)
paths = {
    "Path1_Aging": ["sham-1", "sham-2", "sham-3", "sham-4(10w)", "sham-5(10w)", "sham-6(10w)"],
    "Path2_Acute": ["sham-1", "sham-2", "sham-3", "hs2w"],
    "Path3_Establishment": ["sham-4(10w)", "sham-5(10w)", "sham-6(10w)", "hs10w"],
    "Path4_Progression": ["sham-1", "sham-2", "sham-3", "hs2w", "hs6w", "hs10w"],
    "Path5_Driver": ["sham-4(10w)", "sham-5(10w)", "sham-6(10w)", "ss10w", "hfd10w", "hs10w"],
    "Path6_Efficacy": ["sham-4(10w)", "sham-5(10w)", "sham-6(10w)", "hs10w", "hs10wgae9", "hs10wgae10"],
    "Path7_Global": ["sham-4(10w)", "sham-5(10w)", "sham-6(10w)", "ss10w", "hfd10w", "hs10w", "hs10wgae9", "hs10wgae10"]
}

# Create directories and symlink/copy files
for path_name, groups in paths.items():
    path_dir = os.path.join(base_out_dir, path_name, "01_Images")
    os.makedirs(path_dir, exist_ok=True)
    print(f"Organizing {path_name}...")
    
    files = [f for f in os.listdir(src_dir) if f.lower().endswith(('.jpg', '.png', '.tif'))]
    
    count = 0
    for filename in files:
        # Match group name in filename (e.g., 'sham-1' in '20251126_sham-1_he_1.jpg')
        for group in groups:
            if group in filename.lower():
                # For compatibility across OS, we use copy instead of symlink if needed, 
                # but here we'll just report. 
                # Actually, creating a mapping file is more token-efficient than copying thousands of files.
                # But the user asked for "separate presentation", so we will create organized folders.
                shutil.copy2(os.path.join(src_dir, filename), os.path.join(path_dir, filename))
                count += 1
                break
    print(f"  Done. {count} images assigned to {path_name}.")

print("\nPath-specific image organization complete.")
