# [20260502] Path 5: 小鼠 DN 驅動因子 (Drivers) 拆解分析完整報告

> [!IMPORTANT]
> **分析對象**: C57BL/6 小鼠 (Sham10W, SS10W, HFD10W, HS10W)
> **分析核心**: 區分「高脂飲食 (HFD)」與「高血糖 (STZ)」對腸道菌相失調的各自貢獻。
> **狀態**: [正式版整合報告 - 已修正為小鼠模型]

---

## 📈 一、 驅動因子對多樣性的衝擊 (Diversity Drivers)

### 1. Alpha 多樣性比較
![Alpha Plots](20260502_Drivers_Alpha_Plot.png)

| 組別 | Chao1 (豐富度) | Shannon (均勻度) |
| :--- | :--- | :--- |
| **Sham (20W)** | 122.00 | 3.7286 |
| **STZ Only (SS)** | 111.78 | 3.4227 |
| **HFD Only (HFD)** | 98.19 | 3.4648 |
| **DN (HFD+STZ)** | 96.61 | 3.2673 |
| **P-value (ANOVA)** | **1.5367e-04** | **0.0026** |

- **關鍵發現**: **HFD (高脂飲食)** 是導致豐富度下降的主要驅動者，其影響力顯著高於單純的 STZ 誘導。

### 2. Beta 多樣性：群落結構的漂移方向
![Beta PCoA Plot](20260502_Drivers_Beta_PCoA_Plot.png)
- **觀察**: HFD 組與 HS10W (DN) 組在 PCoA 圖上位置極為接近，顯示高脂飲食主導了菌相結構的病理轉向。

---

## 🔬 二、 菌屬水平的驅動因子拆解 (Taxonomic Attribution)

![Driver Comparison](20260502_Path5_Driver_Comparison_Plot.png)

### 1. HFD 驅動菌 (Diet-driven)
- **Lepagella**: 在 HFD 與 HS10W 中同步上升，但在單純 STZ 組中無明顯變動。
- **Kineothrix**: 同樣表現出明顯的高脂依賴性。

### 2. STZ/血糖敏感菌 (Glucose-driven)
- **B. acidifaciens**: 在單純 STZ 組中呈現下降趨勢，顯示其受血糖/氧化壓力環境影響。

### 3. 協同效應菌 (Synergistic Markers)
- **Acetatifactor** / **Faecalibaculum**: 呈現 **1+1 > 2** 的趨勢。僅在「肥胖+糖尿病」同時存在時（HS10W）發生爆發性增長，標誌著病程的惡性加速。

---

## 💡 整合科學洞察

1. **飲食是根源**: 腸道菌相的失調主要源於 HFD 的長期壓力。
2. **疾病是放大器**: STZ 產生的代謝紊亂進一步放大了 HFD 誘導的特定有害菌（如 Acetatifactor）。
3. **治療啟示**: **GaExo (大蒜外泌體)** 若要展現療效，必須能同時對抗 HFD 誘導的基礎失調，並切斷與 STZ 產生的協同毒性。

---
*本 Master Report 由 AI 同事整合碎片文件生成。原始數據已封存。*

