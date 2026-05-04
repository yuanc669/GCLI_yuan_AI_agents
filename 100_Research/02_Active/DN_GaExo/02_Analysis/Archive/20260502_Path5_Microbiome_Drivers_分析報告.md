# [20260502] Path5_Microbiome_Drivers_分析報告

> [!INFO]
> 數據來源: `Path5_Microbiome_Drivers.csv`
> 分析對象: Sham vs SS (STZ only) vs HFD (Diet only) vs HS (HFD+STZ)
> 產出日期: 2026-05-02
> 狀態: [正式分析報告]

## 🔬 關鍵驅動菌屬分類 (Driver Categories)

本分析旨在區分「高脂飲食 (HFD)」與「鏈左佐菌素 (STZ)」對菌相變動的貢獻度，並識別具備協同作用的關鍵菌屬。

### 1. 🍔 HFD-Driven (由高脂飲食主導)
這些菌屬在 HFD 與 HS 組均顯著上升，是代謝紊亂的主要微生物標記。
- **Kineothrix sp000403275**: 在 HFD (0.119) 與 HS (0.107) 中均維持極高水平。
- **Lepagella sp900547755**: 穩定隨飲食肥胖而增加。
- **Romboutsia_B ilealis**: 高脂飲食誘導的急性爆發菌。
- **Parabacteroides goldsteinii**: 典型的飲食反應菌。

### 💉 STZ-Driven (由糖尿病狀態主導)
這些菌屬主要受 STZ 誘導的血糖升高與腎損傷影響。
- **Bacteroides acidifaciens**: 在 SS (0.10) 與 HS (0.10) 中表現一致，與 HFD 關聯較小。
- **Lepagella muris_A**: 傾向於對高血糖狀態產生反應。

### 🤝 Synergistic (1+1 > 2 協同作用)
最危險的類群，只有在 HFD 與 STZ 同時存在（HS 組）時才會極端變動。
- **Acetatifactor sp011959105**: Sham(0.002) -> SS(0.004) -> HFD(0.005) -> **HS(0.035)**。顯示 HS 組合對此菌有強大的正向篩選壓力。
- **Faecalibaculum rodentium**: 僅在 HS 組 (0.010) 明確增加，是 DN 病程加速的潛在指標。

### 🛡️ HFD-Inhibited (受高脂飲食抑制的益生菌)
- **Duncaniella (unclassified)**: 在 HFD/HS 中幾乎完全消失。
- **Paramuribaculum sp001689565**: 對高脂飲食極度敏感，迅速被排除。

## 💡 生物學意義解讀 (Mechanistic Insights)

1. **協同加速模型**:
   - `Acetatifactor` 與 `Faecalibaculum` 的協同增加暗示了 HFD 產生的代謝物與 STZ 導致的氧化壓力在腸道中產生了疊加效應，這可能與 HS 組觀察到的更嚴重的腎損傷 (BUN 上升) 直接相關。

2. **GaExo 的干預靶點**:
   - 未來分析應觀察 **GaExo** 是否能優先抑制 `Acetatifactor` 的異常爆發，或是恢復受 HFD 抑制的 `Duncaniella`。

3. **研究重點**:
   - `Kineothrix` 雖然被歸類為 HFD-Driven，但其豐度與腎功能指標的強相關性使其成為「代謝-腎臟軸」的核心連結者。

---
*本報告由 `/data-interpret` 自動生成，並遵循 [日期][文件名]_分析報告 命名規範。*
