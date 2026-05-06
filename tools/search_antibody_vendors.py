import os
import fitz  # PyMuPDF
import re

pdf_path = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers\2021 Testicular torsion–detorsion causes dysfunction of.pdf"

def search_pdf_for_antibodies():
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Look for the protein names and vendor info
        targets = ["NDUFS1", "NUDFS1", "SDHC", "ATP5C1", "ATP5J", "GAPDH", "actin"]
        for target in targets:
            print(f"--- Searching for {target} ---")
            # Find occurrences and get 200 characters around it
            matches = [m.start() for m in re.finditer(target, text, re.IGNORECASE)]
            for m in matches:
                start = max(0, m - 100)
                end = min(len(text), m + 200)
                print(text[start:end].replace('\n', ' '))
                print("-" * 20)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_pdf_for_antibodies()
