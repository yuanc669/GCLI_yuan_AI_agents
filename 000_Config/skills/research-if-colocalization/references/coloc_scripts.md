# Python Templates for IF Colocalization

## 1. Nuclear Segmentation (Cellpose)
```python
from cellpose import models
import numpy as np
from skimage import io

def segment_nuclei(dapi_path, output_path, diameter=30):
    model = models.Cellpose(model_type='nuclei', gpu=False)
    dapi_img = io.imread(dapi_path)
    masks, flows, styles, diams = model.eval(
        dapi_img, 
        diameter=diameter, 
        channels=[0, 0]
    )
    io.imsave(output_path, masks.astype(np.uint16))
    return masks.max()
```

## 2. Colocalization Quantification (ImageJ API + NumPy)
```python
import numpy as np
import pandas as pd
from skimage import io

def quantify_coloc(ch2_path, ch3_path, mask_path):
    ch2 = io.imread(ch2_path).astype(float)
    ch3 = io.imread(ch3_path).astype(float)
    mask = io.imread(mask_path)
    
    results = {}
    for n_id in np.unique(mask)[1:]:
        roi = mask == n_id
        a, b = ch2[roi], ch3[roi]
        
        # Pearson Correlation Coefficient (PCC)
        pcc = np.corrcoef(a, b)[0, 1]
        
        # Manders Overlap Coefficients (M1, M2)
        th_a, th_b = np.mean(a), np.mean(b)
        m1 = np.sum(a[b > th_b]) / np.sum(a)
        m2 = np.sum(b[a > th_a]) / np.sum(b)
        
        results[n_id] = {"PCC": pcc, "M1": m1, "M2": m2}
    
    return pd.DataFrame(results).T
```
