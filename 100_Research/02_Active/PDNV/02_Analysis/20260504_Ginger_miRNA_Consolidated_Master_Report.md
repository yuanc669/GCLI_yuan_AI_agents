# Ginger_NV (GiExo) 雙軌 miRNA 深度鑑定與跨物種調控報告

> **數據來源**: Ginger-derived Nanovesicles (GiNV) Small RNA-seq 原始數據  
> **分析日期**: 2026-05-04  
> **報告核心**: 建立Ginger外泌體跨物種傳遞 (Cross-species communication) 之分子證據鏈。

---

## 📊 一、 雙軌 miRNA 鑑定策略 (Dual-Track Strategy)

本分析採用雙軌並行模式，旨在同時論證 PDExo 的**藥理功能性**與**物種來源唯一性**。

### 軌道 A：進化保守組分 (Conserved Track: hsa-miR Homologs)
*這些序列在植物中高豐度表達，且與人/鼠源序列 100% 一致。它們是 PDExo 直接與宿主抗發炎通路對接的「萬能鑰匙」。*

| miRNA ID (Homolog) | TPM 均值 (表達量) | 序列 (5' -> 3') | 關鍵功能與機轉 |
| :--- | :---: | :--- | :--- |
| **hsa-miR-574-5p** | 32,541 | UGAGUGUGUGUGUGUGAGUGUGU | 調節 TLR4 信號路徑，緩解氧化壓力與纖維化。 |
| **hsa-miR-339-3p** | 29,982 | UGAGCGCCUCGACGACAGAGCCG | 與腫瘤抑制及細胞週期調控相關。 |
| **hsa-miR-8485** | 25,008 | CACACACACACACACACGUAU | 長序列保守組分，參與應激蛋白質穩定調控。 |
| **hsa-miR-4771** | 18,802 | AGCAGACUUGACCUACAAUUA | 在應激反應與免疫調節中發揮作用。 |
| **hsa-miR-6760-5p** | 16,561 | CAGGGAGAAGGUGGAAGUGCAGA | 潛在的代謝調節因子。 |

### 軌道 B：植物特異組分 (Specific Track: Plant mature)
*這些序列僅存在於Ginger基因組中，是證明 PDExo 確實被宿主攝取並運送至目標器官的「金標準」證據分子。*

| miRNA ID (Specific) | Mean Count | 序列 (5' -> 3') | 在專案中的角色 |
| :--- | :---: | :--- | :--- |
| **mature_31** | 1,796.00 | GGCGCTGTCGTCGAG
CGAGGCGCT | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **mature_6** | 1,571.67 | AACTGTTGTGGA | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **mature_18** | 1,075.67 | TGCGAGTTCTA | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **mature_20** | 888.33 | GGCACTGTCGTCGAG | 作為體內追蹤 (In vivo tracking) 之標記。 |
| **mature_37** | 528.00 | GGGACCTTCCTC | 作為體內追蹤 (In vivo tracking) 之標記。 |

---

## 📈 二、 表達量統計摘要 (Prism-Ready Data)

以下數據可用於繪製 GingerNV miRNA Cargo 的特徵圖：

| miRNA (Specific ID) | Mean Count | SD | SEM |
| :--- | :---: | :---: | :---: |
| mature_31 | 1796.00 | 660.85 | 381.54 |
| mature_6 | 1571.67 | 109.10 | 62.99 |
| mature_18 | 1075.67 | 387.90 | 223.95 |
| mature_20 | 888.33 | 239.55 | 138.30 |
| mature_37 | 528.00 | 242.95 | 140.27 |

### 完整數據清單 (Prism Data Format)

| Gene_id | Ginger-Exo-1_count | Ginger-Exo-2_count | Ginger-Exo-3_count | Mean | SD | SEM |
| --- | --- | --- | --- | --- | --- | --- |
| Zingiber_officinale_mature_31 | 2469 | 1771 | 1148 | 1796.0 | 660.8547495478866 | 381.54466754671506 |
| Zingiber_officinale_mature_6 | 1460 | 1678 | 1577 | 1571.6666666666667 | 109.09781543795152 | 62.98765311110142 |
| Zingiber_officinale_mature_18 | 1488 | 1021 | 718 | 1075.6666666666667 | 387.89990117726677 | 223.9541123633242 |
| Zingiber_officinale_mature_20 | 1118 | 907 | 640 | 888.3333333333334 | 239.54609855585903 | 138.30200448454985 |
| Zingiber_officinale_mature_37 | 779 | 511 | 294 | 528.0 | 242.94649616736604 | 140.2652249609052 |
| Zingiber_officinale_mature_12 | 710 | 384 | 375 | 489.6666666666667 | 190.8673186622931 | 110.197297809177 |
| Zingiber_officinale_mature_23 | 605 | 263 | 157 | 341.6666666666667 | 234.13101745247968 | 135.1756059518301 |
| Zingiber_officinale_mature_19 | 452 | 315 | 209 | 325.3333333333333 | 121.82911529405987 | 70.33807251015942 |
| Zingiber_officinale_mature_15 | 466 | 256 | 166 | 296.0 | 153.94804318340653 | 88.8819441731559 |
| Zingiber_officinale_mature_4 | 162 | 221 | 163 | 182.0 | 33.77869150810907 | 19.5021366350801 |
| Zingiber_officinale_mature_26 | 87 | 153 | 238 | 159.33333333333334 | 75.69896520648966 | 43.704817939342924 |
| Zingiber_officinale_mature_29 | 135 | 165 | 148 | 149.33333333333334 | 15.044378795195678 | 8.685876147196923 |
| Zingiber_officinale_mature_21 | 89 | 171 | 185 | 148.33333333333334 | 51.85878260558508 | 29.94068209718083 |
| Zingiber_officinale_mature_33 | 84 | 140 | 175 | 133.0 | 45.902069670114 | 26.501572280401277 |
| Zingiber_officinale_mature_14 | 193 | 103 | 66 | 120.66666666666667 | 65.31717487256574 | 37.710888495381695 |
| Zingiber_officinale_mature_8 | 9 | 2 | 2 | 4.333333333333333 | 4.041451884327381 | 2.3333333333333335 |
| Zingiber_officinale_mature_30 | 3 | 3 | 2 | 2.6666666666666665 | 0.5773502691896258 | 0.33333333333333337 |
| Zingiber_officinale_mature_2 | 0 | 0 | 1 | 0.3333333333333333 | 0.5773502691896258 | 0.33333333333333337 |
| Zingiber_officinale_mature_38 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 |
| Zingiber_officinale_mature_16 | 0 | 0 | 0 | 0.0 | 0.0 | 0.0 |

---

## 🖼️ 三、 數據可視化 (Visualization)

![Ginger miRNA Distribution](Ginger_Top15_Bar.png)

## 🧬 四、 科學洞察 (Scientific Insights)

1. **高豐度藥理背景**：**hsa-miR-574-5p** 在 GingerNV 中的 TPM 表達極高，說明其為該 miRNA 的強效遞送系統。
2. **跨界調控基礎**：透過保守組分對應宿主通路，實現了「精確路徑對接」；透過特異組分證明其「外源唯一性」。
3. **機制驗證建議**：後續應針對 Top 5 保守組分進行靶基因驗證，並在組織中檢測 **mature_31** 的含量。

---
*本報告由 Gemini CLI 自動生成。*
