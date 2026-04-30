import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pptx import Presentation
from pptx.util import Inches, Pt
import os

def save_bar_chart(title, groups, means, stds, p_val, filename):
    plt.figure(figsize=(6, 4))
    x = np.arange(len(groups))
    bars = plt.bar(x, means, yerr=stds, capsize=10, color=['#3498db', '#e74c3c'], alpha=0.7)
    plt.xticks(x, groups)
    plt.ylabel('Abundance (%)' if '%' in title or 'Species' in title else 'Value')
    plt.title(title)
    
    # Add significance marker
    if p_val < 0.05:
        max_y = max(means) + max(stds) if any(stds) else max(means)
        plt.text(0.5, max_y * 1.05, '*', ha='center', va='bottom', fontsize=20, color='red')
        plt.plot([0, 0, 1, 1], [max_y * 1.02, max_y * 1.05, max_y * 1.05, max_y * 1.02], lw=1.5, c='black')

    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

def create_ppt():
    prs = Presentation()
    temp_images = []

    # Slide 1: Title
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = "Microbiome Analysis: Sham vs Sham10W"
    slide.placeholders[1].text = "DN_GaExo Project\nVisualized Abundance & Significance Markers"

    groups = ['Sham', 'Sham10W']

    # Slide 2: Alpha Diversity (Observed Species - Significant)
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Alpha Diversity: Observed Species"
    # Data: Sham [156, 169, 151], Sham10W [120, 125, 117]
    means = [158.67, 120.67]
    stds = [9.29, 4.04]
    img_path = "temp_observed.png"
    save_bar_chart("Observed Species (Richness)", groups, means, stds, 0.01, img_path)
    slide.shapes.add_picture(img_path, Inches(1), Inches(1.5), height=Inches(4.5))
    temp_images.append(img_path)
    
    # Slide 3: Significant Decreases (B. acidifaciens)
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Significant Decrease: B. acidifaciens"
    # Data: Sham [15.28, 15.10, 16.84], Sham10W [7.82, 7.15, 6.52]
    means = [15.74, 7.16]
    stds = [0.95, 0.65]
    img_path = "temp_b_acid.png"
    save_bar_chart("B. acidifaciens Abundance (%)", groups, means, stds, 0.04, img_path)
    slide.shapes.add_picture(img_path, Inches(1), Inches(1.5), height=Inches(4.5))
    temp_images.append(img_path)

    # Slide 4: Significant Increases (Suilimivivens)
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Significant Increase: Suilimivivens sp000403495"
    means = [0.00, 2.77]
    stds = [0.00, 1.80]
    img_path = "temp_suili.png"
    save_bar_chart("Suilimivivens Abundance (%)", groups, means, stds, 0.03, img_path)
    slide.shapes.add_picture(img_path, Inches(1), Inches(1.5), height=Inches(4.5))
    temp_images.append(img_path)

    # Slide 5: Significant Increases (B. thetaiotaomicron)
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Significant Increase: B. thetaiotaomicron"
    means = [0.23, 2.15]
    stds = [0.15, 1.70]
    img_path = "temp_b_theta.png"
    save_bar_chart("B. thetaiotaomicron Abundance (%)", groups, means, stds, 0.04, img_path)
    slide.shapes.add_picture(img_path, Inches(1), Inches(1.5), height=Inches(4.5))
    temp_images.append(img_path)

    # Slide 6: Summary
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "Summary of Significant Changes"
    content = slide.placeholders[1].text_frame
    content.text = "Key Findings (p < 0.05):"
    for text in [
        "Significant loss of microbial richness (Observed species)",
        "Major reduction in core commensal B. acidifaciens",
        "Emergence/Proliferation of B. thetaiotaomicron & Suilimivivens",
        "Markers (*) indicate p < 0.05 via Kruskal-Wallis"
    ]:
        p = content.add_paragraph()
        p.text = "- " + text

    output_path = "100_Research/02_Active/DN_GaExo/Sham_Sham10W_Analysis_Visualized.pptx"
    prs.save(output_path)
    
    # Cleanup
    for img in temp_images:
        if os.path.exists(img):
            os.remove(img)
    print(f"Visualized presentation saved to: {output_path}")

if __name__ == "__main__":
    create_ppt()
