# Python Templates for Western Blot Analysis

## Stage 2 - Image Processing (OpenCV/skimage)
以下為處理 WB 影像的關鍵邏輯代碼範本。

```python
import cv2
import numpy as np
from skimage import io, color, filters, measure

def analyze_wb(image_path):
    # 1. 讀取並轉為灰階
    img = io.imread(image_path)
    gray = color.rgb2gray(img) if img.ndim == 3 else img
    
    # 2. 背景扣除 (Rolling Ball 簡化版或高斯過濾)
    background = filters.gaussian(gray, sigma=50)
    corrected = gray - background
    
    # 3. 閾值分割與 ROI 偵測
    thresh = filters.threshold_otsu(corrected)
    binary = corrected > thresh
    labels = measure.label(binary)
    
    # 4. 提取 Band 數據
    regions = measure.regionprops(labels, intensity_image=corrected)
    results = []
    for prop in regions:
        # 計算積分密度 (Integrated Density)
        int_den = prop.mean_intensity * prop.area
        results.append({
            "centroid": prop.centroid,
            "area": prop.area,
            "int_den": int_den
        })
    return results
```

## Stage 3 - Normalization Logic
```python
def normalize_results(target_data, loading_control_data):
    # Target / Loading Control
    ratios = target_data / loading_control_data
    # Fold Change (Relative to Control)
    fold_change = ratios / ratios[0] 
    return fold_change
```
