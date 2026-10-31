# O10：实际场、局部核心、跨尺度拓扑与最新零端进展

专题汇总，2026-09-28。只依据上传的完整稿及本轮 `audit_zero.md`。下文“稿内定理”意为原稿给出了证明，不等于独立发表认证。原稿源索引编号止于 I55，**没有检出 I56**；04 卷三个新源文及本轮 fixed-outer 引理均用描述性名字，不自行追加编号。

## 目标与目前真正最强的无几何条件结论

O10 的优先实际场版本要求：在同一真实 Spin-c 类的共形可解供给、`p≥A>0`、`a²≥T_+=2χ+3τ`、`χ/A≤B` 下，不加逐点 Ricci、Sobolev、驻点、直径或非塌缩假设，证明

\[
\kappa_\beta:=r+D_\beta/V\ge c(B)(\beta-2)^2/\beta^2,
\qquad \beta\ge2.
\]

这要求 `β→∞` 时仍有正间隙。去掉 B，或只给一般近闭自对偶形式而没有实际 SW 场，是更强的不同问题。I51 已无附加几何地证明

\[
(1+b_a)\left(r+\frac{D_\beta}{\beta V}\right)
 \ge c\frac{(\beta-2)^2}{\beta^4},\quad b_a=(-a^2)_+/V;
\]

在 `a²≥T_+` 下可删去 `1+b_a`。紧化后为 `r+P_t/V≥ct²(1-2t)²`，`P_t=tD_{1/t}`；这是旧三次退化改为二次退化，**仍不是 O10 的非退化零端**。

## 节点表：已证输入、具体产出、缺失桥梁

| 节点与来源 | 状态 | 实质成果 | 必须保留的边界 / 下一桥梁 |
|---|---|---|---|
| I41 / I51：零端共形归一化；05 卷 Source 2，01 卷 Source 2 §1 | 稿内定理 | 可将实际 `κβ→0` 序列改到 `s=-4`；同类、投影平方和拓扑预算保留，体积比趋 1。确切共形 Ricci/Weyl 恒等式控制损失。 | 不提供共形因子的逐点/Hessian 控制；不保持原度量的逐点 Ricci 界或特定局部核心。不能把两套解直接认作同一套解。 |
| I42 / I43：精确零端模型的局部不相容、覆盖体积、平滑比较；05 卷 §8–13，06 卷 Source 1 §1–4 | 稿内条件性间隙定理 | 在受控局部几何上，近模型极限成为负 Einstein almost-Kähler；t=0 由 Armstrong 局部 ASD 障碍排除，t>0 由 Bianchi 强迫平行并推出 t=1/2，排除 t∈[0,1/4]。进一步给塌缩/曲率尺度退化的体积分数限制。 | 小积分残差本身不提供可取这种光滑极限的图册。局部展开覆盖体积与原流形体积不能混淆；比较平滑度量不是实际场所在度量。 |
| I45：有界 Ricci + Euler 密度；06 卷 Source 2 §3 | 稿内定理 | 以 Cheeger–Tian 覆盖正则性、Euler/Fubini 选点、Liouville 平均得到 `avg Z_t≥c(K,L,Λ)`，无直径/原空间非塌缩/全局 Sobolev 假设。全 pencil 为 `(1+b_a)(r+Dβ/V)≥c(β-2)²/β²`。 | 保留逐点 Ricci 界；Euler 密度可由适用拓扑比导出，不能由一般 L² Ricci 自动导出。经典 general-type 手术族的点态版本可统一，但不等于积分 O10。 |
| I45 / I46：有界 Ricci 逃逸的拓扑方向；06 卷 Source 2 §5 | 稿内推论 | 若仍有零端逃逸，则 `χ/V→∞`、`χ/T_+→∞`、`τ/χ→-2/3`；`c₂(S^+)/V→0`，而两个负手性束的 c₂ 密度及 W⁻ 能量密度发散。恒等式 `c₂(S^-⊗L)=χ+2T_++9c₂(S^+)` 精确指出所在曲率块。 | 不是 bubble 提取定理，不给单个核心数量；在固定拓扑上不能有这种有界 Ricci 逃逸。 |
| I46：实际 annular holonomy 分类；06 卷 Source 2 §4.1–4.4 | 稿内定理 | 同时容许非零平行正 spinor 与 `S^-⊗L` torsion 的自由平商恰为奇数阶 `1/n(1,-2)`，允许 determinant 标记 ±1。其余固定有限种标记付出校准/曲率/Dirac 代价；有覆盖重数条件可计数。 | 整个 Spin-c lift、物理定向与标记都要保留；不能只看未标记 lens space。常数不统一于无界 n；原弱输入不给 annuli 分解。 |
| I46 resonant 实例；06 卷 Source 2 §4.5 | **实际局部解**，不是闭反例 | 两种允许 lift 都有负双曲商颈上的实际 weighted SW 解；近常幅非零 torsion 与归一化损失在任意深内尺度上一致变小。 | n>1 时顶点仍是 orbifold 奇点，未平滑填充，未构造闭同类共形供给。它阻止用更强局部 holonomy 禁掉允许支。 |
| I47：整个 resonant core 代价；06 卷 Source 3 §1 | 稿内 sharp filling 定理 | 完整光滑填充、外向欧氏锥 collar 下，`∫(Ric°²+4W⁺²+s²/12)≥4π²(n-1)/n≥8π²/3`；经典 Calderbank–Singer scalar-flat Kähler ALE 截断逼近下确界。近锥 collar 误差 `O(δ²/n)`；小体积时成为实际缺陷 atom。 | 是整个平滑 core，不是穿孔颈、内禀圆边界或未填 orbifold。n 增大时成本仍有界、Euler 数却增大，因此不能用它线性控制全部拓扑复杂度。 |
| I47：跨尺度整核记账；06 卷 Source 3 §1.4 | 稿内精确恒等式 | 内部边界有符号消去；一子 flat neck 可零成本，整个已填充外核仍付完整 atom。二叉 resonant 分支有 `>4π²/3` 成本。 | 不能给树上每个嵌套节点重复收费；一般多叉不具有同一算术下界（out 3、三个 in 9 的小数障碍抵消），也没有因此构造零成本 cobordism。 |
| I47：faithful determinant 及全局一阶 ALE；06 卷 Source 3 §2、Source 1 §7 | 稿内条件性排除 | faithful 平坦 determinant 不能穿过非平凡光滑 Ric≥0 ALE；另在全局一阶 Spin-c 展开、完整平行正联络、`dB∈L²` 与有界物理一阶 torsion/current 下，ALE 全局导数修正为零，不能保持非零校准外场。 | 普通 L² 曲率界不保证全局一阶曲率界；校准可逃到 bubble 坐标无穷远。必须保留 determinant twist，不能拿未扭 spin frame 代替。|
| I48：积分 Ricci 的可闭合正则性子类；06 卷 Source 3 §3，Source 4 §5–6 | 稿内条件性间隙定理 | 一支为 `|∇*∇Ric|≤A|Rm||Ric|` 加固定尺度 p>2 的小负 Ricci 预算；另一支为准确二次泛函临界、受控参数、全局 Sobolev 与绝对拓扑界。可建立受控图册并排除零端。 | “小”不能改成仅“有限”；近极小不是驻点，Yamabe 归一化不是曲率椭圆方程。两支条件不可混用。 |
| I50：实际 determinant 相对电荷；01 卷 Source 1 §1–2 | 稿内定理 | 标记 ±1 下 `Q_rel∈Z-f_n`、`f_n=(n-1)/(2n)≥1/3`；可控固定比 collar 给 `|Q_rel|≤C∫whole core+collar |F_A|²`，常数可统一于 n。实际 bounded fit 给 `Σ|Q_rel|/V≤CΣVol/V+CΛ(β⁻¹+√η)`。 | 平坦联络仅比较模板，不能是正权实际 SW 的非零 spinor collar。原弱输入不给完整帽及有限重叠；归一化 o(V) 不等于绝对无核心。 |
| I50：同线 harmonic charge 与任意有限树深度；01 卷 Source 1 §2.1–2.2 | 稿内定理 | 同一个**整 determinant 线**的实际/调和联络具有相同相对电荷；Hodge 误差两手性相等，不用谱隙。内部界面先有符号消去，再对 disjoint frontier whole subtrees 求绝对值；在体积 o(V) 时 frontier 电荷 o(V)，与有限树深度无关。 | 保留 torsion 线标记，不能只剩实上同调向量；不是从弱输入构造 bubble tree；不能对无限重叠祖先作无符号求和。 |
| I50 / X07：torsion c₂ 与 determinant charge 解耦；01 卷 Source 1 §3 | 稿内拓扑反例及实际局部反例 | canonical resolution 上 `J_+=(m-j)/4=0`、`J_-=(n-1)/2→∞`，而 `|Q_rel|=f_n<1/2`。另真实平凡 determinant 局部核可 `Q_rel=0` 而 torsion index +1 或 d²。 | 因此 determinant tightness 不推出 torsion index no-loss。若要用相对 index 加和，需要 disjoint 核覆盖全部零点、实际边界 section 非零；有限重叠本身不足。 |
| X07：高指数 actual cores 与后续修正；01 卷 Source 1 §3.2，Source 2 §3–4 | 实际局部解 + 精确尺度计算 | 固定 d 后缩 r，index d²、Q_rel=0；round 固定比 collar 的方向四次能量 Θ(d⁴)。改用幅值 level shell，单项式临界成本 Θ(d³)、二次成本 Θ(r²d)。分裂为 d² 个简单零点则选中分量的临界成本仅 Θ(d²)。 | 这三者是不同区域，不能混写成统一 d³ 或 d⁴ 下界。原型允许高幅值/大外导数；没有全校准外场与闭供给。I50 的 frontier 发散要求 `H/V→0`；若 d² 个平凡界面、H/V≈1，只有有限正临界密度。 |
| I51：同一常权解的全参数平方分解；01 卷 Source 2 §2 | 稿内定理，当前无几何的最强参数加强 | s=-4 后任选实际 `D_AΦ=0,F_A⁺=2iσ(Φ)`，`ρ≤2`，直接分解 Dβ 为 harmonic remainder/current/full Weyl-fit/amplitude 四个非负项。导出二次紧化间隙和上能量墙二次 margin。 | 不依赖选择解的连续性；β 在估计里，不在此方程里。Maxwell 控制是 Hodge graph norm，不是含 W⁻ 的 covariant W¹,²，更不是二阶 Laplacian 小量。 |
| I51：局部核全局化必须付外场；01 卷 Source 2 §3.1、4.1 | 稿内必要条件 | 缩比控制延拓给 `r²d≲E_D+r²+r²√E_0`，故大 d 要么 Dirac 源要么曲率付款。闭 s=-4 同解必有 `K/V→4/9`；近乎平行 exterior 反而 `liminf Dβ/V≥32/27`。调和两手性能量必须 `8/9,2/9` 的 V 级，由外部提供。 | 缩核场在整个 seed ball 的 K、曲率都可忽略，因此裸 gluing 零点远不够；但非平行外部并未被排除。不能对另一共形代表声称原核仍原样保留。 |
| 04 卷 phase-curvature / prolongation | 精确实际恒等式 + 失败机制 | actual cubic torsion 精确决定 `(0,1)` bracket，`[Z1,Z2]^{0,1}=−2κ\bar Z1`；实际 `(2,0)` 曲率仅由 Ric° block 驱动。 | 积分测试仍留对称二阶 torsion 导数；平直 Dirac jet 给非零可变号主符号。不能凭 Dirac 收缩或交换反对称导数将其删掉；jet 不是闭实际反例。 |
| 04 卷 global signed quartic flux | 精确全局恒等式 / 条件性阈值 | 首先 `∫ϑ²k=∫(jχ+2|M|²−2|ϑW⁻−M|²)+Rχ`；实际零端左侧/V→20/3。Euler multiplier 给明确严格次阈值充分判据。继续 central Stokes + weighted Lichnerowicz 可消除 determinant/scalar 导数乘积。 | 最新消元同时消掉 **20V/3 正特征预算**。最终只剩 signed square difference 与 Ric° mixed pairing；把余项证明 o(V) 仍不自动矛盾。不能回用消元前正预算且忽略已消项。 |
| 04 卷 §7：actual simple core 对 signed separation 的检验 | 实际局部反例，针对特定中间论证 | 固定双曲核 `W⁻=Ric°=0`，最新 signed identity 两边均恰为零；quartic cutoff 范数仍有非零极限，且 `E_-−(8/9)E_+=32π²/3`。ASD fit 仅 O(ℓ⁴)，二次导数成本 O(ℓ²)。 | actual cubic bracket 本身不能强迫正 local square separation；必须用 calibrated exterior/matching 或另外完整系统信息。它仍未构造闭逃逸。 |
| 本轮 fixed-outer-extension，`audit_zero.md` | **本轮新增条件性引理**，未获原稿编号 | 固定有界几何 B₂ 上，同一常权解且 `|Φ|≤√2`，abelian Coulomb + Dirac–Maxwell 正则性给 `sup_B1|∇τ|≤C(1+||F_A||₂)^4`。简单缩核有 `|∇τ|≳ℓ⁻¹`，故固定外球 `∫|F_A|²≳ℓ⁻¹/²`，ASD fitted error 亦有同阶外部成本；有限重叠下不能以正 V 密度存在。 | 固定外半径、受控图册及重叠仍是实质假设；一般弱输入可塌缩、退化、改变尺度。计数简单核不等于控制任意高指数总和。与 I51 缩小延拓区的便宜 residual 完全相容。 |

## 最新全局精确继续点

04 卷最终式 (6.6) 为

\[
\|\vartheta W^- -\widetilde H\|_2^2-\|\widetilde H\|_2^2
=\|\vartheta\mathsf R\|_2^2
  -2\int\vartheta\langle\mathsf R,H^+\rangle,
\qquad |\mathsf R|^2=|\operatorname{Ric}^{\circ}|^2/4.
\]

`H⁺` 是两个不同手性空间之间的完整 3×3 矩阵，**不能投影成对称无迹块**；它含单位 torsion 的二次导数乘积，已有预算不给统一归一化 L² 界。原稿提出的下一充分命题必须同时控制 signed separation 与 mixed pairing，且使用 cubic provenance、actual bracket 和外部校准。仅 Cauchy、仅 Ric° 小、仅测试未归一化 τ 的 scalar Lichnerowicz 都不够：最后一种测试的径向梯度项恰在两边抵消。

## 被否定／不可重复推进的路线清单

1. **“形式理想模型是局部解”不成立。** 精确理想 actual 系统在开集上若收缩 N=0，actual bracket 与曲率交换迫使额外 barred derivative 为零，继而 dm=0。单点矩阵自由度不能直接延拓。但弱 N 小只给导数交叉项，不能由精确 no-go 自动推出稳定间隙。
2. **“torsion 零点全正”被实际局部负号 seed 否定。** 04 卷 Source 1 §4 给实际 hyperbolic 常权解，局部 index −1；必须保留 signed index，不得替换成零点个数。
3. **“Dirac null-form 会自动杀掉临界乘积”已被早期 actual positive core 与后续 symmetric jet 检验否定。** 不同层面分别是代数、局部实际解、全局积分；不能互换。
4. **“每个 bubble-tree 节点收同一 quantum”错误。** neck 有零成本，内部边界消去；只能给完整填充 / disjoint frontier 收费。高阶 quotient 还可把 Euler 复杂度藏在有界 atom 中。
5. **“determinant no-loss 等于 c₂ no-loss”错误。** 同样有全真实局部 Q=0、正 index，及 resolution 的有界 Q、无界 index。
6. **“高指数必超线性 quartic cost”错误。** monomial d³ 非普适；分裂简单核 Θ(index)。frontier 结论需说明 H/V 是否趋零。
7. **“图范数小会给 covariant regularity／二阶小”错误。** W⁻ 与临界 source 仍在；signed Maxwell test 主项可恰相消。
8. **“最终全局化已保留正拓扑预算”错误。** 最新 square cancellation 恰把该预算用完；actual local hyperbolic core 直接让最终差为零。
9. **“本轮 fixed-outer no-go 已解决 O10”错误。** 新量化成果只排固定有界几何外扩展；当前剩余问题可准确改写为：退化图册／缩小外匹配尺度／覆盖重数的失败，能否由实际拓扑与曲率预算统一收费？

## 三条真正还未被覆盖的研究桥梁

- **几何桥梁：** 从一般积分实际输入提取够多的受控物理外扩展区，或量化图册失败的实际成本；需同时追踪 base 与 cover 能量倍数。这里可以直接接本轮 fixed-outer 引理和 I45/I48，不能假设结论式 bubble 分解。
- **拓扑桥梁：** 在标记 whole-frontier 电荷 tightness 之外，控制实际 signed torsion index/flux，尤其平凡 determinant 的 split simple cores 与无界 quotient 的高 c₂；统一 quantum 本身不够。
- **全系统桥梁：** 在最后 signed curvature identity 中加入真正来自 calibrated exterior 的约束，形成严格 signed separation 或其与 Ricci mixed pairing 的联合估计。局部 cubic bracket 已被用过，不能再把它当尚未使用的新正项。


来源对应：本轮 `audit_zero.md` 的正式结果并入 `sources/review/appendices/05_actual_core_extension.md` 与独立核查 `07_extension_crosscheck.md`。原工作稿也保留在 `sources/worknotes/`。
