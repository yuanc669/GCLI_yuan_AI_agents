import os
import fitz  # PyMuPDF
import re

pdf_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers"

zoletil_pattern = re.compile(r'zoletil.*?(\d+\s*mg/kg)', re.IGNORECASE)
xylazine_pattern = re.compile(r'xylazine.*?(\d+\s*mg/kg)', re.IGNORECASE)

def search_pdfs():
    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(pdf_dir, filename)
            try:
                doc = fitz.open(filepath)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                z_matches = zoletil_pattern.findall(text)
                x_matches = xylazine_pattern.findall(text)
                
                # Also just look for the words and surrounding text if specific pattern fails
                if "zoletil" in text.lower() or "xylazine" in text.lower():
                    print(f"--- Found in {filename} ---")
                    lines = text.split('\n')
                    for i, line in enumerate(lines):
                        if "zoletil" in line.lower() or "xylazine" in line.lower():
                            start = max(0, i-1)
                            end = min(len(lines), i+2)
                            print("Context:", " ".join(lines[start:end]))
                            print(f"Regex matches: Zoletil: {z_matches}, Xylazine: {x_matches}")
            except Exception as e:
                pass

if __name__ == "__main__":
    search_pdfs()
