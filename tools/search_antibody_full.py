import os
import fitz  # PyMuPDF
import re

pdf_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers"

def search_pdfs():
    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(pdf_dir, filename)
            try:
                doc = fitz.open(filepath)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                if "primary antibody" in text.lower() or "secondary antibody" in text.lower():
                    print(f"--- Found in {filename} ---")
                    lines = text.split('\n')
                    for i, line in enumerate(lines):
                        if "primary antibody" in line.lower() or "secondary antibody" in line.lower():
                            start = max(0, i-2)
                            end = min(len(lines), i+5)
                            print("Context:", " ".join(lines[start:end]))
            except Exception as e:
                pass

if __name__ == "__main__":
    search_pdfs()
