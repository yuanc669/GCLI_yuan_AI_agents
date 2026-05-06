import os
import fitz  # PyMuPDF
import re

pdf_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers"

def search_dilutions_and_cats():
    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(pdf_dir, filename)
            try:
                doc = fitz.open(filepath)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                # Search for dilutions
                if "1:1000" in text or "1:5000" in text:
                    print(f"--- Found Dilution in {filename} ---")
                    for match in re.finditer(r'1:\d+', text):
                        start = max(0, match.start() - 50)
                        end = min(len(text), match.end() + 50)
                        print(text[start:end].replace('\n', ' '))
                
                # Search for OXPHOS targets and potential catalog numbers (often starts with letter followed by numbers)
                targets = ["NDUFS1", "NUDFS1", "SDHC", "ATP5C1", "ATP5J", "GAPDH"]
                for target in targets:
                    if target.lower() in text.lower():
                        print(f"--- Found {target} in {filename} ---")
                        # Look for alphanumeric patterns like AB1234 or H000...
                        cat_matches = re.findall(r'[A-Z]+\d+[-\w]*', text)
                        # This might be too broad, so let's just get context
                        m = re.search(target, text, re.IGNORECASE)
                        if m:
                            start = max(0, m.start() - 100)
                            end = min(len(text), m.end() + 200)
                            print(text[start:end].replace('\n', ' '))

            except Exception as e:
                pass

if __name__ == "__main__":
    search_dilutions_and_cats()
