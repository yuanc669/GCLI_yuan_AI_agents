import os
import fitz  # PyMuPDF
import re

pdf_path = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers\2021 Testicular torsion–detorsion causes dysfunction of.pdf"

def search_for_codes():
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Search for primary antibody names and anything that looks like a cat number
        # Often cat numbers are after vendor name or in parentheses
        # Targets: NDUFS1, SDHC, ATP5C1, ATP5J, Actin
        patterns = [
            r"NDUFS1.*?([A-Z0-9-]+)",
            r"SDHC.*?([A-Z0-9-]+)",
            r"ATP5C1.*?([A-Z0-9-]+)",
            r"ATP5J.*?([A-Z0-9-]+)",
            r"Sigma-Aldrich.*?([A-Z0-9-]+)"
        ]
        
        print("--- Full Text Search for Cat Numbers ---")
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if any(t in line for t in ["NDUFS1", "NUDFS1", "SDHC", "ATP5C1", "ATP5J", "actin"]):
                start = max(0, i-1)
                end = min(len(lines), i+3)
                print(f"Line {i}: {' '.join(lines[start:end])}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_for_codes()
