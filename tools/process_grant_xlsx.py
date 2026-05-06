import pandas as pd
import os

file_path = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\_inbox\研究計畫申請案結構化提煉表.xlsx'
output_dir = r'G:\我的雲端硬碟\GCLI_yuan_AI agents\400_Data\研究計畫申請案'
assets_dir = os.path.join(output_dir, '_assets')

if not os.path.exists(assets_dir):
    os.makedirs(assets_dir)

df_dict = pd.read_excel(file_path, sheet_name=None)
df = df_dict['Table 1']

md_content = """---
title: "研究計畫申請案結構化提煉表"
author: "Multiple Authors"
year: 2026
category: "研究計畫申請案"
original_file: "./_assets/研究計畫申請案結構化提煉表.xlsx"
processed_date: 2026-05-02
---

# 研究計畫申請案結構化提煉表

## 📋 總覽
本表整理了 111 年至 115 年間各項研究計畫申請案的核心摘要，包含背景、研究缺口、研究問題、方法學及預期貢獻。

"""

for index, row in df.iterrows():
    md_content += f"""
### {index + 1}. {row['標題']}
- **申請時間**: {row['申請時間']}
- **申請單位**: {row['申請單位']}
- **Source Index**: {row['Source']}

#### 🔬 AI 精華層 (Executive Summary)
- **GAP (Research Gap)**: {row['GAP (Research Gap)']}
- **METH (Methodology)**: {row['METH (Methodology)']}
- **Key Finding/Goal**: {row['CONTRI (Contribution)']}

#### 🧬 學術五力分析 (Academic Extraction)
- **BG (Background)**: {row['BG (Background)']}
- **GAP (Research Gap)**: {row['GAP (Research Gap)']}
- **RQ (Research Question)**: {row['RQ (Research Question)']}
- **METH (Methodology)**: {row['METH (Methodology)']}
- **CONTRI (Contribution)**: {row['CONTRI (Contribution)']}

---
"""

md_path = os.path.join(output_dir, '研究計畫申請案結構化提煉表.md')
with open(md_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(f'Markdown saved to {md_path}')
