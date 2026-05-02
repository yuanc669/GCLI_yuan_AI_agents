# [20260502] Path3_Microbiome_Late_Stage_分析報告

> [!INFO]
> 數據來源: `Path3_Microbiome_Late_Stage.csv`
> 分析對象: Sham (20W/10W-post) vs HS10W (末期病情 10 週)
> 產出日期: 2026-05-02
> 狀態: [正式分析報告]

## 🔬 顯著差異菌屬摘要 (Top 10)

以下為根據 P-value 排序最顯著的末期病情 (Late Stage) 相關菌相變動：

| Phylum | Genus | Species | Mean (Sham10W) | Mean (HS10W) | Log2FC | P-value | 趨勢 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Bacillota_A_368345 | unclassified | unclassified | 0.0036 | 0.0000 | -21.79 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Duncaniella | D. dubosii | 0.0013 | 0.0000 | -20.30 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Muribaculum | M. gordoncarteri | 0.0322 | 0.0010 | -4.99 | < 0.0001 | ⬇️ 顯著減少 |
| Bacillota_A_368345 | CAG-314 | sp900551395 | 0.0065 | 0.0000 | -22.62 | < 0.0001 | ⬇️ 顯著減少 |
| Bacteroidota | Duncaniella | D. muricolitica | 0.0575 | 0.0001 | -9.26 | < 0.0001 | ⬇️ 顯著減少 |
| Bacillota_A_368345 | unclassified | unclassified | 0.0020 | 0.0000 | -20.94 | < 0.0001 | ⬇️ 顯著減少 |
| Pseudomonadota | Parasutterella_564865 | unclassified | 0.0062 | 0.0000 | -22.57 | < 0.0001 | ⬇️ 顯著減少 |
| Pseudomonadota | Escherichia | unclassified | 0.0032 | 0.0004 | -2.96 | < 0.0001 | ⬇️ 顯著減少 |
| Bacillota_A_368345 | CAG-273 | sp003507395 | 0.0037 | 0.0000 | -21.83 | < 0.0001 | ⬇️ 顯著減少 |
| Pseudomonadota | Parasutterella_564865 | P. excrementihominis | 0.0027 | 0.0000 | -21.34 | < 0.0001 | ⬇️ 顯著減少 |

## 💡 生物學意義解讀

1. **末期特徵：多樣性與恆定性喪失**:
   - 與 Path2 (急性) 相比，Path3 顯示了 **Muribaculum** 與 **Duncaniella** 的持續性缺失。這代表腸道微環境已進入慢性的失調狀態，難以自發性恢復。
   - **Parasutterella** 的完全消失值得注意，該菌屬通常被認為與膽汁酸代謝有關，其缺失可能暗示末期大鼠的膽汁酸循環受損。

2. **慢性期關鍵驅動菌 (Late-stage Drivers)**:
   - 雖然前 10 名均為減少，但數據深處顯示 **Lepagella sp900547755** (Log2FC +2.76, P=0.0006) 與 **Romboutsia_B ilealis** (Log2FC +24.94) 持續顯著增加。
   - **Kineothrix sp000403275** 在末期依然保持高倍數增加 (Log2FC +2.16, P=0.0079)，這進一步鞏固了其作為 **慢性腎損傷驅動者** 的地位。

3. **轉譯思維**:
   - 末期菌相的變動更接近臨床慢性腎病 (CKD) 的表現。若 **GaExo** 能在末期逆轉這些菌相變動，將具備極高的臨床轉譯價值。

---
*本報告由 `/data-interpret` 自動生成，並遵循 [日期][文件名]_分析報告 命名規範。*
