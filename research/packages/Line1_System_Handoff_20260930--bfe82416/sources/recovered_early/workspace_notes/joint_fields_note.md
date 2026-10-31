# 内部工作笔记：03/04 的联合相容性与严格增量（非用户交付稿）

## 已有最强结果

- 03: `line1_composed_application.md`, L1282–1652：从固定实际 conformally solvable Spin^c 结构供应有界光滑自对偶形式，κ=r+δ/V 小时谐和 Chern 代表 ξ_i 近该场，协变能量 O(G(κ)), G=13κ+4√(2κ)。全标量范围，不需 Hodge 逆、谱隙或非塌缩。二阶预算才需要 (-a²)_+/V。允许 Weyl 根 t=1/2，不能作新不可能性。
- 03: `round18_periods.md`, L3380–4133：同平方 a_i²=A>0≥T 的更强输入给全交叉矩阵近 CUT_m；光滑配对观测量 covariance 给多标量低模；m=2,3,4 BF 连通和有实际应用。强于仅两两 Cauchy，但不是任意平方。
- 03: `line1_period_inertia.md`, L4526–4898：任意平方、无负部预算，正周期矩阵 P≈q ssᵀ，Q=P−N，N≥0 不受控；ν₂(Q)≤(m−1)J。不能删N，不能把整数格当统一正周期下界。
- 04: `line1_signed_harmonic_weyl.md`, L1067–1357：负最低特征值的 signed balance，把 harmonic W 的实际方程变为允许分支结构估计，无 W− 或二阶预算；正能量在等式两边，不能推出小 splitting 必为零。
- 04: `line1_aspherical_no_bubbles.md`, L1529–1767：aspherical 的拓扑把非平坦 ASD Ricci-flat ALE compact core（包括 rational ball）排除，进而半 Weyl 控制→全曲率；实际 shear 族小 splitting 的 exact Einstein 输出必须 diameter→∞。这是实质结构排除，仍非无条件 Einstein 不存在。

## 本轮可推导 A：任意平方的无谱联合证书

沿用 I12 假设、记号：κ≤1/2880，Q_ij=(2π²/V)a_i·a_j，P_ij=E〈ξ_i,ξ_j〉，Q=P−N、N≥0。全部类别固定后分别对全部所需权重可解。

结论：对任意实对称 PSD 矩阵 Y，记 M(Y)=max_{σ∈{±1}^m}σᵀYσ，

    tr(YQ) ≤ ( sqrt(M(Y)) + sqrt(27000 m κ tr(Y)) )².

更精确可把 m trY 替换为 (∑√Y_ii)²。因而若 tr(YQ)>M(Y)，则

    κ ≥ (√tr(YQ)−√M(Y))²/(27000 m trY).

这是本轮由现有 endpoint 引理直接推导的候选定理，原八卷未见此式，未做发表优先权判断。无需 λ₁ 下界，亦不需要同平方或控制 N。解释为 Q 近 CUT_m−PSD_m；不是 Q 近 CUT_m。

证明：I12(16)给 E|ξ_i−u_i|²≤49κ/2，E(|u_i|²−1)²≤180κ；(17)、phase lemma给可测σ_i=sign〈u_i,u₁〉，E|u_i−σ_i u₁|²≤6480κ。取可测单位 n=u₁/|u₁|，零点任取，E|u₁−n|²≤180κ，于是 E|u_i−σ_i n|²≤13320κ。e_i=ξ_i−σ_i n 满足 E|e_i|²≤2(49/2+13320)κ≤27000κ。C=Eσσᵀ∈CUT_m，E_error=Gram(e_i) PSD。对 Y 的平方根在 Hilbert–Schmidt Hilbert 空间用三角不等式，√tr(YP)≤√tr(YC)+√tr(YE_error)。tr(YC)≤M(Y)，|E_error,ij|≤27000κ，以及 |Y_ij|≤√Y_iiY_jj，给出误差项。Q≤P 完成。光滑 allowance→0通过有限维紧性或直接不等式取极限。

该结论高秩 Y 比仅 rank-one Y 的单方向投影有额外信息。代数分离例 G* 的 diagonal 1, offdiagonal −1/2，Q=G*−εI；Y=I−11ᵀ/3，有 tr(YQ)=3−2ε，M(Y)=8/3。因此 ε<1/6 就有无谱间隙。此仅代数例，尚无真实 monopole 实现。

重大瓶颈：标准 BF signed-sum 类的正 Gram本来就是分块权重 sign-matrix 凸组合；blow-up 类又是共同正方向减 exceptional 负 Gram。因此现有实际族常自动属于 CUT−PSD，不会由本式产生新判定。需要非正交 sign-cube 的真实 monopole 配置，或者新的跨类微分信息。否则只是有用的联合定理，不是旗舰突破。

## 本轮可推导 B：全正惯性强制标量低模簇

同上，1≤r≤m−1，若 ν_{r+1}(Q)>102000mκ，则

    λ_r(g) ≤ 24m G(κ)/(ν_{r+1}(Q)−102000mκ).

证明：h_i=〈u_i,u₁〉。I12 phase lemma给 E|h_i−σ_i|²≤3600κ，故 E|ξ_i−h_i n|²≤3(49/2+13320+3600)κ≤51000κ。令H=Ehhᵀ，Γ=Cov(h)，μ=Eh；则 Q≤P≤2H+102000mκI=2Γ+2μμᵀ+102000mκI。秩一交错→Γ至少r个特征值≥(ν_{r+1}Q−102000mκ)/2；Dirichlet矩阵D_ij=E〈dh_i,dh_j〉有 trD≤12mG。min-max完证。无需微分 n 或 σ。

它将I12的ν₂/λ₁推广为任意正惯性，解除Round18同平方与负部条件。但是仍是低模分支，不宜当改变主问题判定的大突破。

## 经典范围核查

LeBrun, Four-Manifolds, Curvature Bounds, and Convex Geometry, arXiv:math/0611450, Def4.3、Prop4.5、Def5.6 已有 β²=max_{Hull C}a² 及 α²=inf_H max_{a∈C}(a_H⁺)²。‘全体类/凸包/极化优化’不能独占为新思想；新增应是同一几何上同时近饱和的微分相容性。原文已通过 web 打开。

Wright arXiv:1102.2442 Theorem A、Remark3核实了 nonflat ASD Ricci-flat ALE 为 hyperkahler 或 GH 的 cyclic quotient，负定性及有限π₁。因此04 core排除论证的外部关键分类基本吻合。Suvaina边界镜空间细节尚未逐行核完。Catino–Dameno arXiv:2607.21538 的官方摘要核实 largest-simple 分支；03/04负lowest不能由其结论直接代换。

## 检查状态

本轮对上述代数、相位、不控N、minmax、core Mayer–Vietoris、半Weyl Hessian交换顺序做推理审读，未发现可断言的实质性缺口。没有运行原工程 check.py（附件无原程序），没有外部认证全文PDE。04 signed conformal source 的全量系数仍应独立逐行审校；有限代数check不能替代。原稿对 allowed root、负部、line cover、zero W、orbifold signature修正的限定总体谨慎。
