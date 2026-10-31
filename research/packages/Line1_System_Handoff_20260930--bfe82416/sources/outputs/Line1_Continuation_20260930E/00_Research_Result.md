# O10／O11：本轮直接研究、效率问题与准确结果

日期：2026-09-30（北京时间）。本轮仍只研究无密度 O10 与原平衡族的 O11，不改变统一积分障碍主线。原整合稿及前轮文件均保留。

**本轮没有解决这两个最终问题。** 新增内容是：O10 原缺陷的多项式下界转接；一项不依赖反手性曲率预算的双重带权测试；以及 O11 可以使用的既有理想极小序列接口。后两项分别减少了一类分析损失和一个不必要的全局前提。未闭合部分在下文明确列出，不用“突破”代替尚缺的证明。

## 1. 为什么效率低：具体的数学原因

一部分原因确实属于研究组织问题，不能全部归因于题目难。

1. **O10 多轮计算仍支付同一个未控量。** 先用负旋量 Hessian 估计引入 \(1+b\)，再改进插值和截断，通常只能改变缺陷与 \(b=\fint|W^-|^2\) 的增长关系。它们有实际含义，但无论把指数界改成多项式界多少次，只要还容许足够快的 \(b\to\infty\)，就没有完成无密度目标。
2. **O11 有一条重复计算并不产生新约束。** 已有实际场恒等式为
   \[
   P-8\pi^2Q=\mathcal A-4\mathbb E K_\epsilon.
   \]
   在固定度量上右侧的差与实际解的选择无关。沿光滑的度量—实际解支求导，只重新得到 \(DP\)；拓扑常数在求导时消失。近驻点不能凭这一恒等式恢复缺失的零阶下界。更多次求导也一样。
3. **局部模型、全部竞争度量和极限中的标记曾被混在一起。** 一个模型已经达到标准费用，并不排除其他共形类更便宜；一个 ALE 泡的出现，也不说明它承载哪一个原异常类或哪个连接柄。反复优化已经完成的模型不能补足这个量词差别。
4. **完整档案与本轮证明输入应当区分。** 本轮按新附件的具体命题读取直接依赖、核查常数和误差；不把重新整理研究历史、编译或代理间同意计作数学推进。

“还剩两个编号”不意味着“只剩两个短引理”。但也没有证据允许断言它们一定需要漫长研究。应以具体未知项、有效的新估计或真实构造判断进展。

## 2. O10：新附件的幂次估计可以接到更强的已有机制

在 \(s=-4\) 的代表上，记
\[
x=\kappa_\beta+\beta^{-2},\qquad b=\fint|W^-|^2,
\qquad \kappa_\beta=(P+D_\beta)/V.
\]
所有范数使用 \(dV/V\)。令 R1 中固定的慢梯度指数为 \(\epsilon_0\in(0,1]\)，并置
\[
\gamma=\frac{\epsilon_0}{1+\epsilon_0}.
\]

审读新附件第 5 节后，可将其中省写的高幅度扭率测试补出；也可使用 C 轮的直接 resolvent 得到同一结论。关键是核对 D 轮的**完整**误差清单，特别补入 \(\|v-\tau\|_4\)，而不是只核对新附件较短的清单。结果为
\[
\boxed{\mathfrak e_D\le Cx^{\gamma/16}.}\tag{2.1}
\]

D 轮第五线丛正势论证排除了
\[
\mathfrak e_D(1+b)^{3/2}\longrightarrow0
\]
的实际零端序列。将两项连接：若不存在普适的正下界，可选允许对象使
\[
x(1+b)^{24/\gamma}\to0;
\]
于是由 (2.1)
\[
\mathfrak e_D(1+b)^{3/2}
\le C\bigl[x(1+b)^{24/\gamma}\bigr]^{\gamma/16}\to0,
\]
矛盾。因此，在上述 R1 与 D 轮正势前置下，得到
\[
\boxed{\kappa_\beta+\beta^{-2}\ge c(1+b)^{-p},\qquad p=24/\gamma.}\tag{2.2}
\]
这是对既有结果的严格转接，不是独立重证全部上游分析。指数未声称最优。

用 Euler 预算及大小参数分割，还得到
\[
\boxed{
\frac{\chi(M)}A\le B
\ \Longrightarrow\ 
\fint|\operatorname{Ric}_g+g|^2+\frac{D_\beta(g)}{V_g}
\ge c'(1+B)^{-p}\frac{(\beta-2)^2}{\beta^2}.
}\tag{2.3}
\]
它比所贴的 \(ce^{-C(1+B)^2}\) 强，但仍非无密度结论：更快增长的 \(b\) 仍未被排除。**本轮不把调换衰减率本身作为最终攻法。**

完整速率、固定高幅度测试、直接 resolvent 复核和量词论证见 `O10_Primitive_Rate_Audit.md`。

## 3. O10：一项真正避开负手性 Hessian 的估计

这一项直接针对上述效率瓶颈。设辅助截面满足已经取得的
\[
|v|+|\nabla^*\nabla v|\le C.
\]
对任意光滑系数张量 \(e\)，以 \(|e|^2v\) 测试并用 Kato 不等式、Young 不等式，有
\[
\boxed{\||e|\nabla v\|_2\le C\|e\|_{H^1}.}\tag{3.1}
\]
这里完全没有交换协变导数，因此没有 \(W^-\)、全 Riemann 曲率或 Sobolev 常数。

对既有第五线丛测试
\[
(\nabla_{5A}^*\nabla_{5A}+10/3)w=T_M(c),
\]
固定截断高度 \(M\) 后，\(w\) 及其粗 Laplacian 有界，且线丛曲率 \(5F_A\) 给出不含 \(b\) 的二阶预算。再次在 (3.1) 中取 \(e=\nabla w\)，得到
\[
\boxed{\||\nabla v||\nabla w|\|_2\le C.}\tag{3.2}
\]
反过来对 \(w\) 使用权重 \(|\nabla\Phi|\)，也得到
\[
\||\nabla\Phi||\nabla w|\|_2\le C.
\]

因此，如果 \(\zeta\to0\) 于 \(H^1\)，且 \(\mathcal C\) 是满足
\[
|\mathcal C|\le C,
\quad |\nabla\mathcal C|\le C(1+|\nabla\Phi|+|\nabla v|)
\]
的全局收缩张量，则一次分部积分给出
\[
\boxed{
\left|\fint \zeta\,\mathcal C\,\nabla^2v\,\nabla w\right|
\le C\|\zeta\|_{H^1}\to0.
}\tag{3.3}
\]
证明的三项分别由
\[
\|\nabla\zeta\|_2\|\nabla v\nabla w\|_2,
\quad \|\zeta\nabla v\|_2\|\nabla^2w\|_2,
\]
以及
\[
\|\zeta\nabla v\|_2
\bigl(\|\nabla w\|_2+\|\nabla\Phi\nabla w\|_2+
\|\nabla v\nabla w\|_2\bigr)
\]
控制。**对称 Hessian 也适用；不需要把所有指标强行反对称化。**固定幅度截断的导数要计入 \(\nabla\mathcal C\)，不能省略。

还直接有
\[
\left|\fint R\,\nabla v\,\nabla w\right|\le C\|R\|_2.
\tag{3.4}
\]
这删除了原弱测试中一类此前通过 \(\|\nabla v\|_4\) 控制、因而随 \(b\) 增长的损失。

**线性径向项也能弱消去。** 记 \(m=|v|^2\to m_*\) 于 \(L^2\)。对同类有界张量 \(\mathcal C\)，
\[
\left|\fint dm\,\mathcal C\,\nabla w\right|
\le C\|m-m_*\|_2\to0.
\tag{3.5}
\]
只需把导数移到 \(\mathcal C\nabla w\)，再用 (3.2)。

完整引理和适用条件见 `O10_Double_Weighted_Test.md`；径向式见 `O10_Global_Closure_Attempt.md` 第 5 节。

### 这之后真正仍未消去的内容

不能将 (3.5) 升格为 \(dm\to0\) 于 \(L^2\)。例如
\[
\fint dm\,\nabla v\,\nabla w,
\qquad \fint dm\,\mathcal C\,\nabla^2w
\]
分别会引入 \((m-m_*)\nabla^2v\nabla w\) 和三阶测试导数；(3.3) 不能用于只有 \(L^2\) 小、没有 \(H^1\) 小的系数 \(m-m_*\)。

此外，第五线丛截面的非消失质量及其在固定截断高度下的保留，仍需要证明。低幅度井的径向能量可能在现有弱预算里承担梯度质量；现有标量模型只证明这些预算不足，**不是实际 O10 反例**。

另须保留原稿已有的局部事实：负 Einstein、ASD、almost-Kähler 的精确零端局部模型不存在。项目已有的双曲实际 SW 核心并不满足这一完整条件，不能当作现成零端主体来拼接。Armstrong 的局部证明还使用更高阶相容性，因此也不能直接替代上述弱极限步骤。

## 4. O11：可以用已有极小序列结构，但不用先追求全部能量无损分解

目标仍是
\[
\inf_gP(g)=8\pi^2Q+o(Q),\quad Q=k+4\ell,
\]
或给出同一原族更低最优值及匹配构造。不预设系数 4。

查阅 Anderson 的原始定理后，应使用它已经提供的结构：由于
\[
\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi(M)+P,
\]
其全曲率极小序列也是 \(P\) 极小序列。紧轨形情形有包含 ALE 泡的能量等式；开放、塌缩情形至少有相应下半连续不等式。不能继续把一般变分结构说成全无现成输入，也不能把这些极限自动认作原复双曲主体。

**下界所需的是足够的拓扑收费，未必是全部能量等式。** 若取得互不重复的完整 AE 核心，负定交叉形式、\(e\) 个 Euclidean ends、\(r=b_1\)、\(m=b_2\)，相对 Gauss–Bonnet 与 signature 给
\[
\boxed{P_N\ge8\pi^2m+32\pi^2(r+e-1)+\frac1{12}\int_Ns^2.}\tag{4.1}
\]
这正是吹起与连接柄的标准费用。若从一个真正的极小序列中，取得承载足够多原标记的完整核心及主体预算，误差总计 \(o(Q)\)，已有下半连续性便足够推出目标下界。额外遗漏的非负能量有利于下界；**没有计入费用的拓扑标记**才是问题。

一般 ALE 泡不能直接套用 (4.1)。保留无穷端群与谱修正后，实际公式为
\[
P_N\ge8\pi^2m+32\pi^2r
+16\pi^2\left(e-2+\sum_a|\Gamma_a|^{-1}\right)
-24\pi^2\eta_\infty+\frac1{12}\int_Ns^2.
\]
Eguchi–Hanson 的一个二周期就可由 Weyl 能量承担，而 \(P=0\)。这说明不能对所有 terminal ALE bubbles 简单按每个周期 \(8\pi^2\) 收费。

所以，本轮没有得到 O11 的新系数。减少的是一个多余目标：“先证明普遍无能量损失”。保留下来的确切缺口是：对可选的真正极小序列，哪些标记留在主体、哪些进入完整核心或塌缩区，它们怎样合计支付 \(8\pi^2Q-o(Q)\)。详见 `O11_Ideal_Minimizer.md`。

### 两条检查后应停止重复的捷径

- 同一实际场恒等式反复求导不能补回拓扑常数，见 `O11_Closure_Attempt.md`。
- 原族的两类手术不改变最小体积熵：经典定理给 \(\lambda(M)=\lambda(X)\)。因此，未加权的熵积缺陷下确界为零，不能直接支付正的 \(ck\) 或 \(cQ\)。这不是 O11 反例，因为熵近极小序列不必是 \(P\) 近极小序列。见 `O11_BCG_Test.md`。

## 5. 本轮状态，不移动终点

| 内容 | 状态 | 是否完成原问题 |
|---|---|---|
| 新附件的原误差幂次、完整 D 误差清单转接 | 在列明前置下补全 | 否 |
| 多项式 O10 缺陷—密度下界 | 上述前置的推论 | 否 |
| 双重带权测试、对称 Hessian 配对及线性弱径向消去 | 给出独立证明 | 否；删除一类无密度测试障碍 |
| O10 剩余径向项与截面质量保留 | 未闭合 | 无密度 O10 未解 |
| Anderson 极小序列接口、完整 AE 相对费用及条件推导 | 既有定理的准确应用与计算 | 未证明原族必有所需标记结构 |
| 全部竞争度量的锐利 O11 下界／更低匹配构造 | 未取得 | O11 未解 |

后续不能把重复求导、改进衰减指数、重算标准帽子当作这两项目标的替代。已有统一主定理、有限密度结果及线性阶保持原状态；本轮也没有把这些已证内容撤回。

## 6. 本次实际使用的材料与边界

- 用户本轮附件：`upload/O10_Quantitative_Escape_and_O11_Boundary(1).md`，本地读取。
- 原整合稿：`upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex`，按直接依赖定位；未宣称本轮重新逐式审读全部文件。
- C 轮强流和直接 resolvent；D 轮第五线丛与增长条件证明。本轮没有重命名为新增结果。
- J. Armstrong, *Almost-Kähler Geometry*, §§3.3.1–3.3.3, Theorem 3.3.5：<https://johnarmstrongmaths.com/publications/resources/thesis.pdf>。
- M. Anderson, *Canonical Metrics on 3-Manifolds and 4-Manifolds*, Theorem 4.10, (4.43), (4.45), Remark 4.12：<https://arxiv.org/pdf/math/0511034>。
- M. Brunnbauer, M. Ishida, P. Suárez-Serrato, *An Essential Relation between Einstein Metrics, Volume Entropy, and Exotic Smooth Structures*, Theorem 1.1：<https://arxiv.org/pdf/0807.1187>。
- C. LeBrun, *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*, §11：<https://arxiv.org/pdf/math/0404251>。该文历史上已明确区分可计算的标量／Ricci 下确界与尚未精确决定的全曲率下确界；此处不将 2004 年的开放状态冒充完整的 2026 年查新结论。

各证明文件分别列出适用条件和依赖。有限代数核验、交叉阅读和文件保存均不等于对整个研究计划的独立证明认证。
