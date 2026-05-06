import os
import fitz  # PyMuPDF
import re

pdf_dir = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers"

def search_wb_details():
    targets = ["NDUFS1", "NUDFS1", "SDHC", "ATP5C1", "ATP5J", "GAPDH", "actin"]
    for filename in os.listdir(pdf_dir):
        if filename.lower().endswith(".pdf"):
            filepath = os.path.join(pdf_dir, filename)
            try:
                doc = fitz.open(filepath)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                lower_text = text.lower()
                if any(t.lower() in lower_text for t in targets):
                    print(f"--- Checking {filename} ---")
                    for t in targets:
                        if t.lower() in lower_text:
                            # Find indices and get context
                            for m in re.finditer(t, text, re.IGNORECASE):
                                context = text[max(0, m.start()-100) : min(len(text), m.end()+200)]
                                if any(kw in context.lower() for kw in ["#", "cat", "no.", "from", "sigma", "abcam", "cell signaling"]):
                                    print(f"Target: {t}")
                                    print(f"Context: {context.replace('\n', ' ')}")
                                    print("-" * 30)
            except:
                pass

if __name__ == "__main__":
    search_wb_details()
