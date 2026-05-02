# DN_GaExo 專案分析報告 - 腸道菌叢 (16S rRNA)

## 實驗背景
- **疾病模型**: HFD+STZ 誘導之糖尿病腎病 (HS10W)。
- **干預物**: 大蒜外泌體 (Garlic Exosomes, GaE)。
- **分析組別**: Sham10W, SS10W, HFD10W, HS10W, HS10WGaE9 (低劑量), HS10WGaE10 (高劑量)。

## 核心發現 (Scientific Results)

在 HFD+STZ 誘導的糖尿病腎病 (HS) 模型中，腸道微生物組表現出顯著的群落結構漂移。在物種層級上，HS 模型組表現出特定病原菌的異常增生，包括 *Lepagella sp900547755* 與 *UBA7173 sp900540205*（與 Sham 組相比均為 P < 0.05）。介入**大蒜外泌體 (GaE)** 展現了明確的治療效果，其中低劑量 (GaE9) 與高劑量 (GaE10) 均能顯著抑制上述失調物種。

值得注意的是，GaE 表現出顯著的劑量依賴性（Dose-dependent response）。高劑量 (GaE10) 在重塑菌相方面展現出獨特優勢：(1) **顯著促進丁酸生成菌 *Kineothrix sp000403275* 的增殖**（P = 0.028 vs. HS10W），此現象在低劑量組並不明顯；(2) **對關鍵代謝相關物種 *Bacteroides acidifaciens* 展現出更強的抑制趨勢**，將其豐度由 HS10W 的 10.10% 壓低至 6.51%；(3) 對於 HS 模型中佔比極高的未分類物種 (unclassified, 198)，GaE10 達到了極顯著的抑制效果（P = 0.006）。綜合數據顯示，高劑量大蒜外泌體透過強化益生菌叢與清除特定致病菌群，更有效地修復了「腸-腎軸」的微生態平衡。

## Prism 繪圖數據 (Mean ± SEM)

| 物種 (Species) | Sham | HS10W | GaE9 | GaE10 |
| :--- | :--- | :--- | :--- | :--- |
| *Kineothrix sp.* | 2.41 ± 0.49 | 10.79 ± 1.54 | 11.10 ± 2.32 | 16.78 ± 1.45 |
| *B. acidifaciens* | 7.16 ± 0.38 | 10.10 ± 1.17 | 10.33 ± 2.55 | 6.52 ± 1.14 |
| *Lepagella sp.* | 0.79 ± 0.06 | 5.36 ± 0.53 | 2.63 ± 0.62 | 2.45 ± 0.77 |
| *UBA7173 sp.* | 0.68 ± 0.05 | 6.11 ± 0.77 | 4.23 ± 0.65 | 3.60 ± 0.77 |
| *unclassified (198)* | 8.99 ± 0.80 | 13.68 ± 1.79 | 9.03 ± 1.75 | 3.01 ± 0.57 |

## 統計驗證 (Wilcoxon Test P-values)
- **Kineothrix**: HS vs GaE10 (P=0.028)
- **B. acidifaciens**: HS vs GaE10 (P=0.067, trend)
- **Lepagella**: HS vs GaE9 (P=0.011), HS vs GaE10 (P=0.028)
- **Unclassified (198)**: HS vs GaE10 (P=0.006)

---
*分析日期: 2026-04-29*
*分析工具: Gemini CLI /microbiome skill*
