# **DN_GaExo H&E 病理評分與量化計畫**

## **1. 分析背景與調整**
更正：目前影像為 **H&E 染色**，而非 PAS。
在糖尿病腎病變 (DN) 模型中，H&E 主要用於評估 **腎小球肥大 (Glomerular Hypertrophy)** 與 **腎小管間質損傷 (Tubulointerstitial Injury)**。

## **2. 定量指標 1：腎小球肥大 (Hypertrophy)**
*   **工具**：`tools/Analyze_HE_Glomerular_Area.ijm`
*   **方法**：圈選腎小球毛細血管叢 (Tuft) 並計算面積 (Area)。
*   **目的**：驗證 **GaExo** 是否能減輕因高過濾作用導致的腎小球代償性肥大。

## **3. 定量指標 2：腎小管損傷評分 (Tubular Injury Score)**
請使用以下標準進行半定量評分 (0-4 分)：

| 分數 | 損傷程度 (依受損面積比例) | 關鍵特徵 |
| :--- | :--- | :--- |
| **0** | 正常 | 腎小管結構完整，刷狀緣 (Brush Border) 明確。 |
| **1** | < 25% | 輕微空泡變性 (Vacuolation)、少量蛋白管型 (Casts)。 |
| **2** | 25% - 50% | 中度擴張、刷狀緣部分脫落。 |
| **3** | 50% - 75% | 顯著擴張、管腔內充滿蛋白物質。 |
| **4** | > 75% | 廣泛壞死、萎縮或嚴重的管腔阻塞。 |

## **4. 定量指標 3：炎症浸潤 (Inflammation)**
*   觀察間質區是否有單核細胞 (Mononuclear cells) 浸潤。
*   紀錄方式：(-) 無, (+) 輕微局部, (++) 廣泛分佈。

## **5. 執行路徑 (Path 1~7)**
已完成歸類的影像將依序進行上述評分：
*   **Path 4 (Progression)**：觀察隨時間增加的肥大與損傷趨勢。
*   **Path 6 (Efficacy)**：核心路徑，對比 `GaExo` 治療後指標是否下降。

---
*Developed by Senior Research Colleague Agent (Skill: /scoring).*
