# I53 精确匹配帽与首项稳定性审读；可直接加入的新推论

审读对象：第二卷 Source 3 `20260928_intrinsic_caps_and_stability.md` 全文；并对照 Source 1 的 Yamabe 连续性、Source 2 的 X09 标记中心阻碍。2026-09-28。

## 1. 结论

I53 的帽构造与其有限估计在本次独立检查中没有发现导致结论失效的缺口。它确实支持**所选恢复序列的任意收缩 C0 邻域**中首项为 4，不需要扰动幅度相对 h 的速率，也没有偷偷加入非塌缩、Sobolev 或输入导数的一致控制。其局部几何控制来自明确假设的、固定坐标环带上的 C0 欧氏接近；这当然不是从所有竞争序列中自动推出的。

其中最容易误判的量词是：平滑时间 T 与输出常数 C 不依赖输入导数，但正则化参数 eta 可以在每个固定光滑输入之后选得任意小。输出仅要求存在一个光滑帽，不要求一个对输入连续、统一复杂度或者同一 eta 的帽算子。这足以用于有限多个核心逐一封帽，再取外层 j 对角。

## 2. PDE 的逐步核查

### (a) 局域化 DeTurck 主部与继续存在

I53 (1.2) 必须保留完整 Lie 导数 `L_{qW} g`。它等于普通 q 倍 DeTurck 主部，加上 `(dq) tensor W` 的一阶漂移；因此 (1.3) 的结构正确。q=chi²+eta² 满足 `|Dq|²/q + |D²q| <= C`，由 chi 固定而与 eta 无关。

对 v=|u|²、w=q|Du|²，微分出的所有 cutoff 项分别形如 q Dq Du D²u、q D²q Du²、q Dq Du³，利用上述 cutoff 控制，分别被 q²|D²u|² 的小份额及 Cw+Cw² 控制。(1.4) 的吸收不需要原始导数界。

在 F=w/(Ka²-v) 的极大点，商函数梯度项确实消去。分母演化带来的负二次项是 `-c F²`，而正二次项为 `C(Ka²-v)F²`，故小 a 吸收后得 (1.5)。由此 `q|Du|² <= Ca²/t`。固定 eta>0 后，q 有正下界，C1 控制与小 C0 控制排除固定正时间前的经典抛物继续存在障碍。内带 chi=1 上获得 C2 大小 O(a)，支撑内插帽 Ca² 能量。

### (b) 外领口冻结：可以删去较长的指数屏障论证，换成已核实的更短证明

文中引用的 Schnürer–Schulze–Simon, *Stability of Euclidean space under Ricci flow*, arXiv:0706.0421，Theorem 4.4（PDF p.8），确实声明：小 C0 的 Euclidean DeTurck 流，在球的半球内部直到初始时刻的高阶导数，受该球内的光滑初始度量控制，不依赖边界导数。不是只有正时间 `t^{-m/2}` 估计。

因此对闭包包含于 `{chi=0}` 的每个缓冲球，改时变量 s=eta²t，所得流在 0<=s<=eta²T 上为普通 DeTurck 流。使用 Theorem 4.4（把时间上界统一取不超过固定 T0；其证明为固定上界的内部先验估计），得到

`sup_{ball/2, 0<=s<=eta²T} |D^m g_eta(s/eta²)| <= C(g0,m,ball,T0)`.

将局部方程积分后有

`||g_eta(t)-g0||_{C^m(ball/2)} <= C(g0,m) eta²T`.

覆盖所需固定领口即得 (1.10)，而且有明确 O_{g0}(eta²) 误差。这个版本使外领口回接、边界通量 B_eta=O_{g0}(eta²) 更直接。不需要声称存在跨越退化界面的光滑 eta=0 流。

原文指数屏障版本在差分方程的小 C0 吸收后也是合理的，但最终稿采用上述短证明能减少不必要技术。

原始来源：https://arxiv.org/pdf/0706.0421；本次检索 ref turn92view0/turn93view0。

### (c) 临界能量保留

Yang, *Convergence of Riemannian manifolds with integral bounds on curvature I*, Section 9, (9.7)，的局域 Ricci 曲率演化结构与原文一致。这里只借用演化恒等式，没有借用 Yang 需额外 Ricci Lp 假设的存在定理。

更清楚的版本是使用文中已经给出的直接 Hessian 控制：

`|nabla_g²q| <= C + |Gamma(g)| |Dq| <= C(1+a/sqrt(t))`.

因为 `|Gamma| <= C a/sqrt(qt)` 且 `|Dq| <= C sqrt(q)`。因此不必对 Hessian q 项分部积分，直接得到

`E_eta' <= -c D_eta + C(1+a/sqrt(t)) E_eta + C integral q|Rm|³ + B_eta`.

Lie 导数对曲率能量密度的作用恰是空间散度，因此只产生边界 transport 项；边界位于 chi=0 缓冲区，`B_eta=O_{g0}(eta²)`。

C0 度量等价足以将固定欧氏环域上的标量 Sobolev 不等式转移给 g_eta；并不需要坐标导数。对 sqrt(q)|Rm| 应用 Sobolev 和 Kato 即有 (1.13)。小 E0 与连续性 bootstrap 吸收临界立方项。系数 `1+a/sqrt(t)` 在 0 时可积，故输出能量 CE0+O_{g0}(eta²)。这个论证没有隐藏 h。

来源：https://www.numdam.org/item/10.24033/asens.1644.pdf；本次 ref turn92view1/turn93view1。

### (d) 匹配与末尾量词

内插带位于 chi=1 的 C2 控制区域；外插带 27/8<r<7/2 与 supp chi 保持正距离，故可以回接原来的 g。原始外领口 7/2<r<4 保持逐点相等。其能量本来就属于 E0。

每个输入最后选择 eta，使 `C_g0 eta² + o_eta(1) <= E0+a²`；允许 eta 依赖所有导数没有破坏普适输出常数。E0+a²=0 时 g=e，单独用平帽。由此 Theorem 1 的存在量词闭合。

## 3. 全局代数与坏核心收费

原式 (3.5) 可独立由 signature 与 Gauss–Bonnet 重算：

- tau(M)-tau(N)=-(k-b)，因此 `B_M = 12pi²(k-b)+B_N+K_+-C_+`。
- `T_-(M)=A/3+5k-4ell`。
- `P=4 B_M+S/12-8pi²T_-`。

代入恰得

`P=8pi²(Q-6b)+(S-S0)/12+4(B_N+K_+-C_+)`。

进而原式 (3.6) 中的负代价确实为 `192pi² b`，不是漏掉了坏核心的费用。保留原 M 上的实际 scalar/projection budget 即足够，辅助封帽后的 N 不需要新 monopole supplier。

最小环带选取的 `sum E_i <= C A/L` 正确；坏环带数 `b <= C A/(L epsilon0)`。`ka²=o(Q)` 只用 k<=Q 和 a->0，没有 a=o(h) 要求。条件 Lh->infty 恰用于把粗糙全流形 A 级曲率预算稀释到 Q 级以下。

## 4. 可直接添加的加强：截断封帽评分，而非统一长环带

这是原始 I53 没有以此形式写出的直接定理，可完整证明，不是假设其余开放结构已经成立。

设 M 为 I53 同一实际平衡族成员，0<h<=1/3。任选若干带指定 blowdown 标记的候选环带组。每个选中环带围住、将被替换的整个内部区域必须两两不交，各自恰好是一个指定普通吹起的区域，不能含其他核心或 handle；仅环带本身不交不够。令 r 为完全没有使用候选环带的吹起数。对其余每个吹起 i 定义

`c_i = inf_nu {E_{i,nu}+a_{i,nu}²}`,

其中 E 是尺度不变的完整曲率能量，a 是缩放后固定标记坐标中的 C0 欧氏差。取 theta=min(epsilon0,a0²,1)>0。若 c_i<=theta/2，选取得分<=theta且任意接近 c_i 的环带并封帽；其他吹起原样保留。由 (3.6)–(3.7)，存在固定 C，使

`Edefect(g) >= 4h/(1+h) - (C/A) [r + sum_i min{1,c_i}]`.

证明：好核心封帽费 <=C c_i。坏核心个数 b 满足

`b <= r + theta^{-1} * C sum_i min{1,c_i}`,

因为坏评分至少 theta/2；(3.7) 除去 h 后分母为 A。小 h 时非负剩余项可丢掉。此论证直接使用 scalar budget，并不需要先假设 Edefect=O(h) 或先建立总曲率预算。

于是，只要

`r + sum_i min{1,c_i} = o(Q)`,

就得到最优首项下界 4。这里不需要统一 L，不需要 Lh->infty，不需要所有核心上的最大振幅趋零；这些只是给出评分小的一种具体方式。

对于有限 L_i 个不交候选环带，

`c_i <= (1/L_i) sum_nu (E_{i,nu}+a_{i,nu}²)`.

尤其统一 L 时，可把 I53 的粗项 A/L 换成**实际环带并集的能量** E_ann/L。若能另证 E_ann=O(Q)，所需长度从 Lh->infty 降为 L->infty。当前材料没有自动供给 E_ann=O(Q)，不能擅自使用。

反过来，如果有低于 4-delta 的首项序列，那么对每一种这样的不交标记封帽系统，必有

`liminf [r + sum_i min{1,c_i}]/Q >= c delta`.

这比只说“远离选定恢复族的 C0 轨道”给出了局部可收费的必要条件。它还不是全度量 O11 的证明，因为 arbitrary near-minimizer 能否给出足够多这样的 marked bands 仍然未闭合。

## 5. 对剩余研究的具体影响

不应继续将 I53 当作“可能还差平滑技术”的开放任务。适当将 1.2 改写为上面的 SSS 内部估计证明、1.3 采用可积 Hessian 误差后，它可以成为可靠的局部工具。

接下来真正会改变 O11 的是：从实际近极小序列证明上述截断评分总量 o(Q)，或者证明评分的不可消去部分被其余全局正预算补偿。仅仅加长手工恢复族的 annuli 或重复更弱平滑不会改变全度量结论。

另一个有潜在价值但尚未证实的局部升级，是以比全 Rm 更小的实际缺陷预算控制封帽 W+ 费用。必须警惕：只控制单手性 Weyl 或 Ricci 的临界积分时，局部 RF 演化会遇到对向手性与 Ricci 的耦合；现有 Theorem 1 并未给出这种升级。
