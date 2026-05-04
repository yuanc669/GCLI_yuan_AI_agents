# [20260502] 老化 vs. 疾病特異性菌相排除分析 (Deduction Analysis)

> [!IMPORTANT]
> **分析目的**: 在評估生薑外泌體 (GaExo) 療效前，區分哪些變動是「自然老化」引起的，哪些是「疾病誘導」的。
> **排除邏輯**: 
> - **Pure Aging**: 僅在 Sham 12W vs 20W 顯著，不應視為治療標靶。
> - **Pure Disease**: 僅在 HS2W 誘導後出現，為核心病理菌。
> - **Synergistic**: 兩者皆顯著且趨勢一致，代表疾病加速了老化過程（或老化使腸道更易受疾病影響）。

---

## 📊 集合統計 (Overlapping Summary)

- **老化相關菌 (P < 0.05)**: 30
- **疾病特異菌 (P < 0.05)**: 57
- **交集 (Common)**: 20

![Counts Plot](20260502_Aging_Disease_Counts.png)

---

## 🦠 核心菌屬分類清單

### 1. 疾病特異性標記 (Pure Disease Markers) - **GaExo 重點標靶**
以下菌屬在老化過程中穩定，但在誘導後劇烈變動：

| Taxon | Log2FC | P-value | 趨勢 |
| :--- | :--- | :--- | :--- |
| Duncaniella unclassified | -24.49 | 2.9401e-08 | ⬇️ |
| UBA946 unclassified | -19.95 | 1.7830e-05 | ⬇️ |
| Romboutsia_B Romboutsia_B ilealis | 24.77 | 5.3044e-05 | ⬆️ |
| Kineothrix Kineothrix sp000403275 | 2.54 | 7.6837e-05 | ⬆️ |
| CAG-873 CAG-873 sp011959565 | -3.94 | 6.1222e-04 | ⬇️ |
| Borkfalkia unclassified | -5.06 | 1.0594e-03 | ⬇️ |
| Eubacterium_F unclassified | -21.53 | 1.3759e-03 | ⬇️ |
| Avispirillum Avispirillum sp011957885 | 21.03 | 1.6409e-03 | ⬆️ |
| UBA3282 UBA3282 sp003611805 | -4.47 | 1.7920e-03 | ⬇️ |
| Roseburia_B Roseburia_B sp009911505 | 6.10 | 3.1318e-03 | ⬆️ |

### 2. 協同加速標記 (Synergistic Markers) - **老化與疾病的交會點**

| Taxon | Aging Trend | Disease Trend | 性質 |
| :--- | :--- | :--- | :--- |
| Photobacterium Photobacterium damselae | Down | Down | Synergistic |
| Duncaniella Duncaniella muricolitica | Down | Down | Synergistic |
| CAG-314 CAG-314 sp900551395 | Up | Down | Antagonistic |
| Bacteroides_H_857956 Bacteroides_H_857956 acidifaciens | Down | Down | Synergistic |
| Eubacterium_R unclassified | Down | Down | Synergistic |
| unclassified unclassified | Down | Down | Synergistic |
| Acetitomaculum unclassified | Down | Down | Synergistic |
| Anaerotignum_189125 unclassified | Up | Up | Synergistic |
| UBA7173 UBA7173 sp002491305 | Down | Down | Synergistic |
| Alistipes_A_871400 Alistipes_A_871400 finegoldii | Down | Up | Antagonistic |

---

## 💡 深度解讀與建議 (Insights)

1. **排除偽陽性**: `Spongiimonas` 與 `Duncaniella` 在老化與疾病中皆顯著下降。若 GaExo 提升了這些菌，我們需判斷它是「抗老化」還是「抗病」。
2. **精準治療論證**: 報告中的 **Pure Disease Markers**（如 Kineothrix 的特定亞種或 Lepagella）應作為論文撰寫的核心，因為它們與老化背景無關，更能體現 GaExo 的疾病特異性療效。
3. **後續驗證**: 建議將 **Pure Disease Markers** 與腎功能指標 (BUN/CRE) 進行強關聯擬合。

---
*報告由 AI 同事自動生成，旨在完善 Path1 分析的解釋深度。*
