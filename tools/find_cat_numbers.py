import os
import fitz  # PyMuPDF
import re

pdf_path = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers\2021 Testicular torsion–detorsion causes dysfunction of.pdf"

def find_catalog_numbers():
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Look for the proteins and any alphanumeric codes near them
        targets = ["NDUFS1", "NUDFS1", "SDHC", "ATP5C1", "ATP5J", "GAPDH", "actin", "secondary antibody"]
        for target in targets:
            print(f"=== {target} ===")
            matches = [m.start() for m in re.finditer(target, text, re.IGNORECASE)]
            for m in matches:
                start = max(0, m - 50)
                end = min(len(text), m + 150)
                print(text[start:end].replace('\n', ' '))
                print("-" * 10)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_catalog_numbers()
