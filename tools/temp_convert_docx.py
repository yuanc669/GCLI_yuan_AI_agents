import docx
import os

def convert_docx_to_md(docx_path, md_path):
    doc = docx.Document(docx_path)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(full_text))

if __name__ == "__main__":
    docx_file = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\UUO_rat\method revision .docx"
    md_file = r"G:\我的雲端硬碟\GCLI_yuan_AI agents\100_Research\02_Active\UUO_rat\method_revision.md"
    if os.path.exists(docx_file):
        convert_docx_to_md(docx_file, md_file)
        print(f"Successfully converted {docx_file} to {md_file}")
    else:
        print(f"File not found: {docx_file}")
