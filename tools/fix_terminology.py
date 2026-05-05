import os
import re

dirs_to_process = [
    r"100_Research/02_Active/AP_GiNV",
    r"100_Research/02_Active/AP_GiNV_Oral",
    r"_inbox"
]

def replace_in_file(file_path):
    if not os.path.isfile(file_path):
        return
    if not (file_path.endswith('.md') or file_path.endswith('.csv') or file_path.endswith('.txt')):
        return
    
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = re.sub(r'GaExo', 'GiNV', content)
    new_content = re.sub(r'GiExo', 'GiNV', new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {file_path}")

for d in dirs_to_process:
    for root, _, files in os.walk(d):
        for file in files:
            replace_in_file(os.path.join(root, file))
