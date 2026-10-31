# O10 / O11：本轮直接证明尝试的结果

日期：2026-09-30。**本轮没有解决无密度 O10，也没有决定 O11 的最佳首项。没有得到符合原始全部假设的反例或更低成本闭流形构造。** 以下记录实际推导的结果与失效点，不将辅助计算登记为两个目标的完成。

## 1. O10：保留完整径向分量后的结果

本轮没有继续优化缺陷与曲率增长之间的速率。直接保留辅助负旋量的全部导数，研究全局多项式对象
\[
\mathcal B=v\wedge\nabla v\in\Omega^1(L^3).
\]
它避免了定义时除以低幅度，且其协闭残差直接来自
\(v\wedge(\nabla^*\nabla v-2v)\)。但是相应 Weitzenböck 算子不是正势算子：完整径向分量落在负势方向。局部适配标架中的强制法向导数代价不足以消掉这个负项。

此外，\(\mathcal B\) 的强二阶测试不能仅由原先的线丛测试理论自动获得。它是线丛值一形式；若改用一般 Hessian 控制，又可能引回切丛的全曲率。形式恒等式不等于对退化序列合法的小误差恒等式。

本轮另验证了一个无反手性能量损失的转移：对有界实际扭率截断 \(u\) 和有界强迫 resolvent \(v\)，
\[
\big\||v|^2-|u|^2\big\|_{H^1}
\le C\|v-u\|_{H^1}.
\]
因此，剩余径向集中不是正则化凭空制造的误差；它可以原样转回实际场。实际幅度恒等式为
\[
|\tau|^2=2\rho^3-\rho^4-\rho^2\Delta\rho-\nu.
\]
其导数包含 \(d\Delta\rho\)。现有电流 \(H^1\) 控制尚不能把这个量作为强收敛小量。完整方程中消去相应高阶测试项的证明，本轮没有得到。

**因此没有证明**
\[
\exists c>0\quad\forall\text{原允许输入},\qquad
\kappa_\beta\ge c\frac{(\beta-2)^2}{\beta^2}.
\]
上述转移也不构成反例。

## 2. O11：直接变分与真实构造均未决定最优值

### 完整平直外领口下，扩大局部模型并不能改变首项

若完整填充为
\(B^4\#m\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\)，在完整外领口等于欧氏度量，附加欧氏外部后，由 Gauss–Bonnet 与签名公式严格得到
\[
P=8\pi^2(m+4\ell)+\frac1{12}\int s^2+4\int|W^+|^2.
\]
它不要求 Kähler、对称性或核心彼此分离。因此，普通 AE 填充中的更广三向模型也不能低于该成本。本轮的一次数值搜索回到了已经被此恒等式解释的小核心范围，未产生新构造；这是无效投入，不能算数学推进。

有限尺度的复双曲外领口存在另外的边界项，不被上式一概排除。但本轮没有构造出在原闭流形族上降低首项、并完成全部过渡成本核算的度量。

### 稳定临界方程没有提供所需负方向

在光滑闭流形、常负标量曲率、稳定的精确 \(P\)-临界度量这些额外条件下，令
\(Z=\operatorname{Ric}^{\circ}\)、\(q=|Z|^2\)、\(L=-\operatorname{div}\nabla\)。消去共形变分得到
\[
\operatorname{Hess}_P(Z,Z)
\ge\langle q,L(6L-2s)^{-1}q\rangle.
\]
它是非负 Hessian 的限制，没有强迫负方向，不能据此产生 \(Q\) 级下降。对归一化 Ricci 方向的一阶计算也发生逐点相消。该计算不能未经证明移用于不完整极限或一般近驻点序列。

核对的经典刚性定理仍有额外条件。例如 Catino 的四维结果要求非正截面曲率；Gursky–Viaclovsky 的相应稳定性理论有指定 Einstein 背景及邻域条件。原问题的 \(P/A\to0\) 不提供这些条件。

**因此没有证明**
\[
\inf_gP(g)=8\pi^2Q+o(Q),
\]
也没有得到低于这一候选值的匹配下界与真实构造。O11 的已知最优值区间本轮没有缩小。

## 3. 可复核记录

- `O10_Actual_Mass_Transfer.md`：幅度的强转移、实际场恒等式、低幅度径向集中的剩余问题。
- `O10_Radial_Matrix_Identity.md`：完整径向一形式方程、势的符号与测试限制。
- `O10_Exact_Hessian_Budget_Check.md`：正旋量 Hessian 预算与既有扭率总预算的关系。
- `O11_Critical_Stability_Attempt.md`：条件性精确临界计算及失效点。
- `O11_Constructive_Audit.md`：全部普通 AE 填充的范围核查、有限 CH 外领口的区别及未成功数值回执。

后三份文件中未成功的计算只为防止以后重复同一路径，不是新主定理。

本轮未修改原整合稿，未将任何一项未完成目标标为已证。

## 文献

- M. Anderson, *Canonical Metrics on 3-Manifolds and 4-Manifolds*, <https://arxiv.org/pdf/math/0511034>。
- M. Gursky, J. Viaclovsky, *Rigidity and Stability of Einstein Metrics for Quadratic Curvature Functionals*, <https://arxiv.org/abs/1105.4648>。
- G. Catino, *Some rigidity results on critical metrics for quadratic functionals*, Theorem 1.4, <https://arxiv.org/abs/1404.0569>。
