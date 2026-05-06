import os
import fitz  # PyMuPDF
import re

pdf_path = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers\2022 High-FructoseHigh-Fat Diet Downregulates the Hepatic Mitochondrial Oxidative Phosphorylation Pathway in Mice Compared with High-Fat Diet Alone.pdf"

def find_oxphos_abs():
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        targets = ["NDUFS1", "SDHC", "ATP5C1", "ATP5J", "GAPDH", "actin", "Sigma", "Abcam"]
        print("--- Searching Morales 2022 ---")
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if any(t in line for t in targets):
                start = max(0, i-1)
                end = min(len(lines), i+3)
                print(f"Line {i}: {' '.join(lines[start:end])}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_oxphos_abs()
