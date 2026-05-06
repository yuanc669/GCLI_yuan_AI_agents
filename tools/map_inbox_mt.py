import os
import json

def get_mapping():
    mapping = {}
    root = r"100_Research/02_Active/DN_GaExo/01_Raw_Data/MT"
    if not os.path.exists(root):
        return {}
    
    for g in os.listdir(root):
        gp = os.path.join(root, g)
        if os.path.isdir(gp):
            for f in os.listdir(gp):
                full_path = os.path.join(gp, f)
                if os.path.isfile(full_path):
                    size = os.path.getsize(full_path)
                    mapping[size] = g
    
    inbox = r"_inbox/DN_GaExo/MT"
    final_map = {}
    if not os.path.exists(inbox):
        return {}
        
    for f in os.listdir(inbox):
        full_path = os.path.join(inbox, f)
        if os.path.isfile(full_path):
            size = os.path.getsize(full_path)
            if size in mapping:
                final_map[f] = mapping[size]
            else:
                # Try to find the closest size or just log it
                pass
    return final_map

if __name__ == "__main__":
    m = get_mapping()
    print(json.dumps(m, indent=2))
