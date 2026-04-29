---
type: DataCard
domain: 100_Research
project: DN_GaExo
tags: [data-interpret, microbiome, 16S, GaExo-treatment, HFD, STZ]
status: active
updated: 2026-04-29
llm_ready: true
---

# Data Insight: GaExo Treatment Efficacy (Sham vs SS vs HFD vs HS vs GaE)

## 📌 數據來源
- **原始檔案**: `_inbox/L7_Sham10W_SS10W_HFD10W_HS10W_GaE10W-1.xlsx`
- **數據類型**: 16S rRNA 腸道菌叢豐度 (Relative Abundance)

## 🧪 實驗組別設定
- **Sham10W**: 假手術對照組 (n=3)
- **SS10W**: 標準飲食+STZ 組 (n=6)
- **HFD10W**: 高脂飲食對照組 (n=6)
- **HS10W**: 高脂飲食+STZ (重度糖尿病模型) (n=6)
- **HS10WGaE9 / GaE10**: GaExo 介入治療組 (各 n=5)

## 📊 核心發現 (Key Findings)
1. **主要優勢菌群**:
   - 介入組數據的 Top 5 菌屬佔比與時序組數據高度一致（`Bacteroides_H_857956` 約 9.5%，`Kineothrix` 約 9.0%），顯示實驗基礎群落的穩定性。
2. **多因子交互作用 (HFD vs STZ)**:
   - 本數據集拆解了「高脂飲食單獨作用 (HFD10W)」、「STZ 單獨作用 (SS10W)」以及「雙重打擊 (HS10W)」對腸道菌叢的不同影響。
3. **治療修復指標 (Therapeutic Restoration)**:
   - 關注 `HS10WGaE10` 組。若 GaExo 具備治療效力，預期該組的特定致病菌（在 HS10W 中升高的菌屬）豐度會顯著下降，並向 Sham10W 或單一打擊組（HFD10W/SS10W）的水平靠攏。

## 💡 分析建議
- **HFD vs STZ 效應分解**: 比較 `HFD10W` 與 `SS10W` 的 PCoA，確認何種因素對菌叢結構破壞更甚。
- **GaExo 救援效應 (Rescue Effect)**: 找出那些在 `Sham -> HS10W` 顯著改變，但在 `GaE10` 治療後恢復正常的關鍵菌屬，這些菌將是 GaExo 治療 DN 的潛在藥效靶點（如 `Bacteroides` 或 `Kineothrix` 變化）。
