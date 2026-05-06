import os
import fitz  # PyMuPDF

pdf_path = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\03_Library\01_Personal_Publications\01_Papers\2021 Testicular torsion–detorsion causes dysfunction of.pdf"

def read_wb_section():
    try:
        doc = fitz.open(pdf_path)
        for i in range(doc.page_count):
            page = doc.load_page(i)
            text = page.get_text()
            if "Immunoblotting assay" in text or "Western blotting" in text:
                print(f"--- Page {i+1} ---")
                print(text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    read_wb_section()
