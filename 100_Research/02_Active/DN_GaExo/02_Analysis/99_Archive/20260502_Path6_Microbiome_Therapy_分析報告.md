# [20260502] Path6_Microbiome_Therapy_分析報告

> [!INFO]
> 數據來源: `Path6_Microbiome_Therapy.csv`
> 分析對象: Sham vs HS (HFD+STZ) vs GaE9 (Low Dose) vs GaE10 (High Dose)
> 產出日期: 2026-05-02
> 狀態: [正式分析報告]

## 🔬 治療效果摘要 (Therapeutic Effects)

本分析重點評估 **GaExo (生薑外泌體樣奈米顆粒)** 對於 DN 腸道菌相失調的逆轉能力。

### 1. 🟢 Rescued Taxa (成功修復的益生菌屬)
這些菌屬在 HS 組中被顯著抑制，但隨 GaExo 劑量增加而顯著回升。
- **Lawsonibacter (unclassified)**: Sham(0.009) -> HS(0.002) -> GaE9(0.005) -> **GaE10(0.008)**。成功回復至接近健康水平。
- **Helicobacter_C hepaticus**: 呈現明顯的劑量依賴性回升 (Dose-dependent Rescue)。

### 2. 🛑 Inhibited Taxa (被有效抑制的致病/驅動菌)
這些菌屬在 HS 組中異常擴張，經 GaExo 處理後被顯著壓制。
- **Lepagella sp900547755**: HS(0.053) -> GaE9(0.026) -> **GaE10(0.024)**。被壓制超過 50%，該菌在 Path4/5 中被識別為病程驅動者。
- **UBA7173 sp900540205**: HS(0.061) -> GaE9(0.042) -> **GaE10(0.036)**。呈現穩定的劑量相關性下降。
- **Bacteroides_H_857956 acidifaciens**: 在高劑量組 (GaE10) 中顯示出明顯的抑制效果。
- **unclassified Bacteroidota**: HS(0.136) -> **GaE10(0.030)**。展現了極其強大的廣譜抑制能力。

## 💡 治療機制洞察 (Therapeutic Insights)

1. **劑量依賴性 (Dose-dependency)**:
   - 數據清楚顯示 **GaE10 (高劑量)** 在多數關鍵菌屬的回復/抑制上均優於 GaE9。這為後續臨床轉譯的劑量設定提供了強力的實驗數據支持。

2. **逆轉「疾病穩定態」**:
   - GaExo 成功打斷了 Path4 中觀察到的「疾病穩定態」。特別是針對 `Lepagella` 的抑制，可能與整體腎功能指標 (BUN/CRE) 的改善有直接因果關係。

3. **核心價值**:
   - GaExo 不僅是補充益生菌，更重要的是它具備「清除有害驅動菌」的重塑能力 (Microbiome Remodeling)。

---
*本報告由 `/data-interpret` 自動生成，並遵循 [日期][文件名]_分析報告 命名規範。*
