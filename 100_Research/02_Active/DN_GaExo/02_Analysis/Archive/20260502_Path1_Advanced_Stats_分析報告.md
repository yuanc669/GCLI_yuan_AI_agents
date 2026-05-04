# [20260502] Path1 高級統計補強：Spearman 與 Venn 分析

## 🎯 分析摘要
本分析旨在深入探討老化過程中，腸道菌群變動與宿主生理指標（生化數據）之間的關聯性，並區分老化與疾病的共用標記菌。

---

## 🎨 Venn Diagram：老化 vs. 疾病標記
![Venn Diagram](20260502_Path1_Venn_Diagram.png)

- **老化特異菌 (Aging Only)**: 10 屬
- **共有菌屬 (Common)**: 20 屬
- **解釋**: 交集部分的菌屬代表其受「生理老化」與「病理壓力」的雙重調節。在評估 GaExo 療效時，應重點關注如何逆轉這部分的「加速老化」特徵。

---

## 🌡️ Spearman 相關性矩陣
![Spearman Heatmap](20260502_Path1_Spearman_Heatmap.png)

### [關鍵發現]
1. **Bacteroides acidifaciens**: 
   - 與 **BodyWeight** 呈強負相關。隨著年齡增加，該菌減少而體重增加，暗示其可能具備代謝調節潛力。
2. **Escherichia**: 
   - 與 **BUN** 呈現正相關趨勢。即使在健康老化組中，Escherichia 的微幅上升也與氮代謝指標的變動同步。
3. **Spongiimonas**: 
   - 隨老化消失，與多項健康指標呈正相關，可視為「健康老化」的保護性標記。

---

## 💡 結論與轉譯建議
1. **扣除老化噪音**: 透過 Venn 圖，我們明確了哪些菌屬在 Sham 組也會變動。未來撰寫論文時，針對 **GaExo 逆轉疾病** 的論述，應優先選擇 **Pure Disease Markers**。
2. **腸-腎軸基礎**: Spearman 分析初步建立了老化背景下的腸-腎連結，為後續 GaExo 透過重塑菌相來改善腎功能的論點奠定了基礎。

---
*報告由 AI 同事自動生成，資產存於 DN_GaExo/02_Analysis。*
