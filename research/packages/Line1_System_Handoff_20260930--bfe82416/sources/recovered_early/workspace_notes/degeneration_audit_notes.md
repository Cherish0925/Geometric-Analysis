# 07/08 深读审查笔记（内部）

## 最关键的量词

- 08 原稿4（round18_integral_limits，819–1007）：M_j=N_j#(S1×S3)，无任何符号Einstein，统一局部几何，体积→∞，E(g_j)→0，但δ∞固定>0。870–872显式排除“证明一个固定M上inf E=0”的解读。
- 固定E_D及剪切闭拼接则已经有点态δ−→0，固定体积，故固定M的inf E=0；但无一般Einstein不存在性。08 原稿10（2702–2739）及原稿17（5505–5527）。两种材料合并不能得固定M且无Einstein的零缺陷反例。
- 07 原稿3 I33（914–956）在cm^-2邻域控制全部张量和全部Einstein输出；原稿6 I36（2338–2350、2684–2718）固定幅度只分离fiber-preserving products。不能用后者幅度与前者输出量词拼成新定理。
- 全局E积分小不能升级为点态δ小或有限奇点C2紧性。对任一负Einstein h，局部共形扰动exp(2aρφ(x/ρ))h有积分残差平方O(aρ²)，点态残差约aρ/ρ²。可aρ→0同时后者→∞；可放置密集多小球且总能量仍→0。任何完整退化理论需保留点态Ricci假设、方程临界性、或选择改善后的规范序列。

## 最小固定候选

取F=B=Σ2，F上非分离圈α的正Dehn twist D，ρ(a1)=D，其余三个标准生成元映到1；等价ρ=D^u，其中u:π1(B)→Z本原。D支集外固定点给截面。

E_D闭、aspherical，π1=Π2⋊Π2，χ=4，τ=0，b1=7，b2=16，b2+=b2−=8。08 原稿16（5100–5160）。

08 4910–4942给实际双曲路径h_z=du²+a²(ds+zζ′du)²、端点D*h0以及固定标记闭组装；4944–5006给完整4×4 Ricci矩阵与全局δ≤C/L→0、V0=16π²、所有固定阶残差与曲率导数界。短圆圈不会生成隐藏ℓ^-1，因为系数独立角度，联络只含b′/b=tanh t。构造不是局部模型或体积稀释。

唯一决定性命题是：是否存在任意h满足Ric_h=−h？若不存在，就是负符号点态分支反例；若存在，必非Kähler、非NPC，且16π²<Vol(h)<48π²。不得以Yamabe/标量/Ricci能量不达到最优替代此问题；全曲率能量下确界达到恰等价Einstein存在。

## 原始文献核查与旧障碍的明确不足

- Kapovich–Leeb, Actions of discrete groups on nonpositively curved spaces, Theorem4.5直接使用同一循环Dehn twist曲面丛，证明无sec≤0，不是无Einstein：https://www.math.ucdavis.edu/~kapovich/EPR/KL_1996.pdf 。拓扑对象经典，不应宣称新。
- Anderson, Dehn filling and Einstein metrics in higher dimensions, math/0303260, Theorem1.1及§2.1：其充分大toral cusp填充均由2π theorem同时承载sec≤0度量，因此E_D不在该填充定理中：https://arxiv.org/pdf/math/0303260 。不排除未来双曲平面乘积端的新填充理论。
- LeBrun, Four-Manifolds, Curvature Bounds, and Convex Geometry, math/0611450, TheoremA给∫s²≥32π²β²。由已有定体积s→−4序列和canonical平方2χ，推出两取向β²=2χ。Theorem5.2的Einstein条件只是2χ≥(2/3)β²=4χ/3，有严格余量。更多基本类不会突破该β²上限：https://arxiv.org/pdf/math/0611450 。这是本次代入所得，不是原文专门研究E_D。
- Kotschick, Entropies, volumes, and Einstein metrics, math/0410215, Theorem1：χ≥3|τ|/2+λ_min^4/(108π²)。Bishop+已有序列给λ_min^4≤9V0=36π²χ；τ=0故此条件右端≤χ/3。其simplicial volume推论更弱：https://arxiv.org/pdf/math/0410215 。
- Kotschick, On regularly fibered complex surfaces, math/9911255, Theorem4：签名零+复结构等价有限monodromy，正确排除E_D复结构。Theorem3对Einstein只给3|τ|<χ，此处自动满足：https://arxiv.org/pdf/math/9911255 。
- 本次检索未找到E_D全部Einstein不存在性或非Kähler Einstein存在定理；“未找到”不等于世界范围证明不存在文献。

## 两个真正升格命题（建议研究目标，未证明）

1. 覆盖次数无关的固定小半径全模态约化及刚性。对Bm×F任意张量扰动，保留整个T_F值慢场、基底Teich核与连接变量；法向一致可逆。证明精确Einstein零点慢场必常数，从而全Einstein局部分类且固定幅度慢例远离所有Einstein。关键是多参数Teich场的非平坦水平连接、所有法向反馈、不断增长的基底核，以及微分同胚切片的一致控制。现有单标量路径精确式和cm^-2收缩球不足。
2. 跨整棵泡树的带标记核心恢复。在现有有界直径+点态Ricci误差+actual saturation假设下，建立整个核心的辛延拓或Milnor光滑类型；不能仅识别最末端ALE。先限制A1/b2=1或rational-ball类，保留全局QG smoothing独立条件。核心难题是实际调和/规范场的非零幅度跨所有尺度传递、排除中间颈零点、保持边界标记。不要把全局缺陷/rho_core^4自动趋零作为既定目标：08 188–195已有小整体缩放退化KE族的校准反例。可研究尺度优化后的量或直接相对辛延拓。

## 填充的现有最强结论和限制

07 1368–1388：实际H无零+A1/b2=1或rational ball ⇒整个填充相对实际标记是Milnor fiber。1632–1655：再有全球projective QG smoothing才得同一smooth M负KE。

07 3160–3200、3256–3291、3320–3399：实际调和幅度误差≤818(r+q)V；受控坐标尺度ρ上的零点至少耗cρ4；由比值充分小得无零和匹配。没有证明原始δ+q→0自动给比值小。

07 3409–3556：零圆反例保留实际class、全部periods、harmonicity及平均结构误差趋0，但δ∞约ρ^-2发散，不能据此否定完整点态输入下自动核心恢复。

Etnyre–Ozbagci–Tosun的原文确认球面空间若有辛rational-ball filling，只能是Wahl lens space；引文方向正确：https://etnyre.math.gatech.edu/preprints/papers/sfsfillings.pdf （Theorem1.18，搜索工具turn6view0）。没有在已深读的核心公式中发现可确认的实质算术/符号错误；上述量词限制比形式修订更重要。仍不能将手稿自称proved视为独立完整认证。
