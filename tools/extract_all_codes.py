import os
import fitz  # PyMuPDF
import re

pdf_path = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers\2021 Testicular torsion–detorsion causes dysfunction of.pdf"

def find_all_codes():
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        
        # Find anything that looks like a catalog number: 
        # (e.g., A1234, #1234, ab1234, SC-1234, H000...)
        codes = re.findall(r'[A-Z0-9#]{4,20}', text)
        print("Potential codes found in Shih 2021:")
        print(set(codes))
        
        # Look for the section with antibody names
        idx = text.find("primary antibody")
        if idx != -1:
            print("\nContext around primary antibody:")
            print(text[idx-50:idx+500])
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_all_codes()
