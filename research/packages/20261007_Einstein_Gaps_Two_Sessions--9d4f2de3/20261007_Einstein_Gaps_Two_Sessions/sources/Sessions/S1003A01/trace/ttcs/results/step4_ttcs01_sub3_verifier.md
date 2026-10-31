# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md"
  ]
}
```

## Task

Analyze and strengthen the fixed-exterior part of the O11 cell programme in light of this precise issue. Suppose a true J-minimizing sequence converges in C^2 on compact regular regions while the CH exterior is fixed. Explain exactly how comparison minimality transfers compactly supported local stationarity/stability to the limit; what is still needed to control an interface stress at the free-interior/fixed-collar interface and justify unique continuation to a locally CH base; and prove the quantitative recovered-volume implication from F=((s+3)^2/3)+1+4|W+|^2>=0: how a deficit delta forces at least delta/4 of background CH volume to be unrecovered. Also assess whether the developing-map extension argument applies unchanged to real-hyperbolic negative Einstein / W+-flat bases relevant to the peer O10 route, making all necessary constant-curvature and completeness hypotheses explicit.

## Output

# 科学核验备忘录：固定外部极小序列、界面应力与恢复体积

设 \(C\) 是固定拓扑的 cell，\(U\) 是逐点固定为复双曲度量 \(g_{\mathrm{CH}}\) 的外部区域，\(V=C\setminus U\) 是可变内部，并令

\[
J(g)=\int_C |\operatorname{Ric}_g+g|^2\,dV_g,
\qquad m=\inf_{\mathcal A_U}J,
\]

其中 \(\mathcal A_U\) 表示在 \(U\) 上等于 \(g_{\mathrm{CH}}\) 的光滑度量。以下结论适用于 \(J(g_i)\to m\) 的真正极小序列。

## 1. 比较极小性确实传到 regular 极限

设 \((\Omega,g_\infty)\) 是极限的 regular 部分。对每个

\[
K\Subset \Omega_{\mathrm{free}},
\]

假设存在嵌入 \(\Phi_i\) 使

\[
\Phi_i^*g_i\longrightarrow g_\infty
\quad\text{in }C^2
\]

于 \(K\) 的一个邻域。取任意

\[
k\in C_c^\infty(S^2T^*\Omega_{\mathrm{free}})
\]

并令 \(g_\infty(t)=g_\infty+tk\)，其中 \(|t|\) 足够小。将 \(k\) 推到 \(\Phi_i(K)\)，得到 \(k_i\)，并定义

\[
g_i(t)=g_i+tk_i.
\]

由于 \(k_i\) 在其支集外恒为零，\(g_i(t)\) 仍属于 \(\mathcal A_U\)，且拓扑、外部标记及其他集中区域均未改变。于是

\[
J(g_i(t))-J(g_i)\ge m-J(g_i)\longrightarrow0.
\]

另一方面，\(J\) 的密度只依赖度量的二阶 jet，所以 \(C^2\) 收敛给出

\[
\begin{aligned}
\lim_i\bigl[J(g_i(t))-J(g_i)\bigr]
&=
\int_K\Bigl(
|\operatorname{Ric}_{g_\infty(t)}+g_\infty(t)|^2\,dV_{g_\infty(t)}
\\
&\hspace{35mm}
-|\operatorname{Ric}_{g_\infty}+g_\infty|^2\,dV_{g_\infty}
\Bigr).
\end{aligned}
\]

故对每个固定小 \(t\),

\[
J_K(g_\infty(t))\ge J_K(g_\infty).
\]

这比“极小序列的梯度趋零”更直接：集中于 \(K\) 之外的全部能量在差值中精确抵消。因此，在 regular 可变区上，

\[
DJ_{g_\infty}(k)=0,
\qquad
D^2J_{g_\infty}(k,k)\ge0.
\]

也就是说，紧支局部 stationarity 与 stability 都由比较极小性传递；不需要先对每个 \(g_i\) 使用 Ekeland 修正，也不需要全局能量恒等式。

这里真正需要的是：

1. \(K\) 在 \(g_i\) 中有单值的标记嵌入，使局部扰动可以推回原 cell；
2. 扰动支集与固定外部及集中点分离；
3. \(C^2\) 收敛发生在支集的一个邻域，而不只是点态收敛。

若 regular 极限最初只有 \(C^2\)，上式首先给出弱 Euler–Lagrange 方程。将其写成经典四阶方程还需要 harmonic gauge 下的局部正则性；若“regular”已经表示光滑 orbifold 度量，则这一步无需另加处理。

## 2. 内部方程与界面应力是两个不同问题

### 2.1 标量方程

对紧支共形变分 \(\dot g=2fg\)，I54 (8.1) 给出

\[
\dot J=4\int f(\Delta_+s+s+4)\,dV.
\]

因此在可变 regular 区内，令 \(u=s+4\)，有

\[
(\Delta_++1)u=0. \tag{2.1}
\]

若极限度量 \(C^2\) 地接到固定 CH 一侧，则 \(u\) 在界面 \(\Sigma\) 上的迹为零。若极限在孤立 orbifold 点的统一化图中光滑延拓，或者这些点对 (2.1) 可去，则 \(u\in H^1_0(V)\)，从而

\[
0=\int_Vu(\Delta_++1)u
  =\int_V\bigl(|du|^2+u^2\bigr).
\]

所以

\[
s\equiv-4 \quad\text{于可变 regular 部分}. \tag{2.2}
\]

这一步只使用零 Dirichlet 迹与 \(\Delta_++1\) 的强制正性；它不需要先知道法向导数。若极限存在非 orbifold 缺失点，则还需排除这些点携带标量通量，否则不能直接把 \(u\) 当作 \(H^1_0\) 测试函数。

### 2.2 张量方程

令

\[
E=\operatorname{Ric}+g.
\]

在 \(s=-4\) 后，内部 stationarity 化为 I54 (8.2)：

\[
\Delta_-E=-2\operatorname{Rm}(E)+\frac12|E|^2g. \tag{2.3}
\]

右侧可写成一个有界系数的线性作用于 \(E\)：

\[
-2\operatorname{Rm}(E)+\frac12|E|^2g
=
A_E(x)E,
\qquad
A_E(T)=-2\operatorname{Rm}(T)+\frac12\langle E,T\rangle g.
\]

所以在紧 regular 集上

\[
|\Delta_-E|\le C|E|. \tag{2.4}
\]

固定 CH 一侧满足 \(E=0\)。\(C^2\) 接合还给出

\[
E|_\Sigma=0,
\]

但这本身不能推出内部 \(E=0\)：二阶椭圆系统可以有非零的零 Dirichlet 解。

令 \(\widehat E\) 表示把内部 \(E\) 在固定一侧延拓为零。对 Laplace 型主部作分部积分可见，在 \(E|_\Sigma=0\) 时，

\[
(\Delta_-\widehat E-A_E\widehat E)_{\mathrm{dist}}
=
\pm(\nabla_\nu E)_{\mathrm{free}}\,\delta_\Sigma. \tag{2.5}
\]

符号取决于法向约定；科学内容是同一个：剩余界面应力正是自由一侧的法向一阶迹

\[
(\nabla_\nu E)_{\mathrm{free}}.
\]

若 \(E\) 的迹也不连续，还会出现 \(\nabla_\nu\delta_\Sigma\) 型项；\(C^2\) 接合已经排除了这一项。因而从度量角度看，缺少的是三阶 jet 的控制。

固定外部的可允许光滑变分在固定一侧恒为零，故在 \(\Sigma\) 上连同全部 jets 都为零。于是任何支撑于 \(\Sigma\) 的有限阶分布都不会被这些变分探测到。紧支 stationarity 和 stability 因而不能单独给出

\[
\nabla_\nu E|_\Sigma=0. \tag{2.6}
\]

这正是此前“regular base stationary，因此可直接从 CH collar 作唯一延拓”中尚未闭合的一步。

### 2.3 足以消除界面应力的解析输入

下列任一事实都能使 (2.5) 中的项消失：

- 在跨越 \(\Sigma\) 的固定坐标中有 \(C^3\) 收敛；由于每个 \(g_i\) 在固定一侧完全等于 CH，便有 \(E_i=\nabla E_i=0\)，极限满足 \(E=\nabla_\nu E=0\)。
- 极限度量在整个 regular 基底上光滑，而不是只在界面两侧分别光滑。此时 \(E\) 在 CH 开集上恒零，光滑性自动给出全部 Cauchy jets 为零。
- 已知极限的弱 Euler–Lagrange 方程在整个基底上成立且没有支撑于 \(\Sigma\) 的测度项；结合 \(E|_\Sigma=0\)，(2.5) 直接给出 (2.6)。
- 可变一侧本身含有一个 CH 开集，并且该开集属于局部 stationarity 所在区域。此时无需穿越固定界面，直接从该开集在内部使用唯一延拓。

有了这些输入之一，\(\widehat E\) 在界面两侧满足 (2.3)。由 (2.4) 和 Aronszajn 型唯一延拓，

\[
E\equiv0
\]

于相连的 regular 基底。于是 \(g_\infty\) 是 \(\operatorname{Ric}=-g\) Einstein 度量。

Einstein 度量在 harmonic 坐标中实解析。它在固定开集上是 CH，故解析张量 \(\nabla\operatorname{Rm}\) 在开集上为零，进而在相连 regular 基底上恒零；其曲率张量由 CH germ 平行延拓。因此 regular 基底局部复双曲。对 orbifold 点，该论证在有限统一化图中进行。

所以固定外部路线的精确结构是：

\[
\text{比较极小性}
\Longrightarrow
\text{内部 stationarity/stability},
\]

\[
\text{界面无应力 + orbifold 可去性}
\Longrightarrow
\operatorname{Ric}=-g,
\]

\[
\text{Einstein 解析性 + CH 开集}
\Longrightarrow
\text{局部 CH}.
\]

其中第一箭头已由 \(C^2\) 比较收敛严格成立；第二箭头需要比 \(C^2\) 多一个法向导数，或等价的跨界面弱方程。

## 3. 缺口 \(\delta\) 强迫至少 \(\delta/4\) 的 CH 体积未恢复

I54 (1.2) 给出精确相对恒等式

\[
J(g_i)-8\pi^2q
=
\int_C F(g_i)\,dV_{g_i}-4d,
\]

其中

\[
F(g)=\frac{(s+3)^2}{3}+1+4|W^+|^2\ge0. \tag{3.1}
\]

在 \(\operatorname{Ric}=-g\) 的 CH 度量上，

\[
s=-4,\qquad |W^+|^2=\frac23,
\]

故

\[
F(g_{\mathrm{CH}})
=\frac13+1+\frac83=4. \tag{3.2}
\]

设序列有能量缺口

\[
\limsup_i J(g_i)\le8\pi^2q-\delta,
\qquad \delta>0. \tag{3.3}
\]

设 \(\mathcal R\subset D\) 是被 regular 极限恢复为原 CH 度量的背景部分，恢复通过单值标记嵌入实现。对任意

\[
K\Subset\mathcal R,
\]

\(C^2\) 收敛和 (3.2) 给出

\[
\int_{\Phi_i(K)}F(g_i)\,dV_{g_i}
\longrightarrow
4\,\operatorname{Vol}_{\mathrm{CH}}(K).
\]

由于 \(F\ge0\)，其余区域不能抵消这部分积分，所以

\[
4\,\operatorname{Vol}_{\mathrm{CH}}(K)
\le
\liminf_i\int_CF(g_i)\,dV_{g_i}.
\]

另一方面，由相对恒等式与 (3.3)，

\[
\limsup_i\int_CF(g_i)\,dV_{g_i}
\le4d-\delta.
\]

令 \(K\) 穷尽 \(\mathcal R\)，得到

\[
4\,\operatorname{Vol}_{\mathrm{CH}}(\mathcal R)
\le4d-\delta,
\]

即

\[
\boxed{
d-\operatorname{Vol}_{\mathrm{CH}}(\mathcal R)
\ge\frac{\delta}{4}.
} \tag{3.4}
\]

这里左侧就是原背景球中未恢复的 CH 体积。

特别地，若一球 cell 写成

\[
j_i=\frac{J(g_i)}{2\pi^2}\le4-\varepsilon,
\]

则 \(\delta=2\pi^2\varepsilon\)，故

\[
\boxed{
d-\operatorname{Vol}_{\mathrm{CH}}(\mathcal R)
\ge\frac{\pi^2}{2}\varepsilon.
} \tag{3.5}
\]

这与 I55 Proposition 6 中固定改进需要非消失背景体积完全一致。

一个直接推论是：若 regular 基底恢复了 \(D\) 除有限点之外的全部 CH 度量，则恢复体积仍为 \(d\)，而 (3.4) 排除任何 \(\delta>0\)。因此有限点 bubbling 本身不能产生阈值以下的 \(J\)；必须有正体积的背景未被恢复，或者极限不具有这里使用的单值 CH 恢复结构。

## 4. 实双曲情形的 developing-map 论证

### 4.1 在常截面曲率假设下，论证原样成立

令

\[
X=\mathbb H^4_\kappa/\Gamma
\]

为闭实双曲四流形，\(\Gamma\) 无挠且余紧。若采用 \(\operatorname{Ric}=-g\) 归一化，则

\[
3\kappa=-1,\qquad \kappa=-\frac13. \tag{4.1}
\]

从 \(X\) 中删去一个或有限多个互不相交的嵌入闭四球，得到连通外部 \(U\)。设 \(\mathcal O\) 是紧致、连通、有效、定向且完备的局部实双曲 orbifold，并有光滑单射局部等距映射

\[
f:U\longrightarrow\mathcal O_{\mathrm{reg}}. \tag{4.2}
\]

则 \(f\) 延拓为 \(X\to\mathcal O\) 的整体等距，且 \(\mathcal O\) 实际上光滑。

证明如下。

完备局部实双曲 orbifold 可写成

\[
\mathcal O=\mathbb H^4_\kappa/\Gamma',
\]

其中 \(\Gamma'<\operatorname{Isom}^+(\mathbb H^4_\kappa)\) 离散余紧。由于四维中删去有限个球不改变基本群，

\[
\pi_1(U)=\Gamma.
\]

局部等距映射的提升是两个常曲率空间开集之间的局部等距；它由一点及其正交微分唯一决定，并延拓为 \(\mathbb H^4_\kappa\) 的整体等距。共轭 \(\Gamma'\) 后可令提升成为标准包含，并得到

\[
\Gamma<\Gamma'. \tag{4.3}
\]

设 \(\widetilde U\subset\mathbb H^4_\kappa\) 是 \(U\) 的提升。它连通且无界，其补集由局部有限个有界 lifted balls 组成。映射 \(f\) 的单射性等价于

\[
\gamma'\widetilde U\cap\widetilde U=\varnothing
\quad
\text{对每个 }\gamma'\in\Gamma'\setminus\Gamma. \tag{4.4}
\]

若存在这样的 \(\gamma'\)，则连通无界集 \(\gamma'\widetilde U\) 必须完全落入

\[
\mathbb H^4_\kappa\setminus\widetilde U
\]

的某个连通分量；但每个此类分量都是一个有界 lifted ball，矛盾。因此

\[
\Gamma'=\Gamma.
\]

由于 \(\Gamma\) 无挠，\(\mathcal O\) 光滑，所得 quotient 等距延拓 (4.2)。

所以 developing-map 刚性对实双曲空间与对 \(\mathbb{CH}^2\) 一样成立，且不需要体积小于一半的假设。

### 4.2 必不可少的几何假设

上述证明实际使用了以下事实：

1. regular 基底已经是局部常截面曲率 \(\kappa\)，而不只是 Einstein；
2. orbifold 度量完备，从而有全局 quotient
   \(\mathbb H^4_\kappa/\Gamma'\)；
3. 固定外部以光滑单射局部等距方式进入 regular locus；
4. 使用的是整个 \(U=X\setminus\bigcup D_a^\circ\)，而不只是一个球面 collar germ；
5. 各 lifted balls 有界，且 \(\widetilde U\) 连通无界；
6. 极限的尺度与原实双曲尺度相同。

若只有一个局部 collar，它通常不能携带 \(\Gamma=\pi_1(X)\)，因而无法推出 (4.3)。若 regular locus 的度量完备化不是 orbifold，也不能直接写成 \(\mathbb H^4_\kappa/\Gamma'\)。

### 4.3 \(\operatorname{Ric}=-g,\ W^+=0\) 不等同于实双曲

在四维 Einstein 情形，曲率算子分解为

\[
\mathcal R=
\begin{pmatrix}
W^+-\frac13I&0\\
0&W^--\frac13I
\end{pmatrix}
\quad\text{当 }\operatorname{Ric}=-g. \tag{4.5}
\]

所以 \(W^+=0\) 只固定了 \(\Lambda^+\) 块；要得到常截面曲率 \(-1/3\)，还必须有

\[
W^-=0. \tag{4.6}
\]

因此，单凭 Einstein 与 \(W^+=0\)，不能把基底写成实双曲空间的离散商，也不能直接使用上述 developing-map 证明。

若原固定外部本身是实双曲，并且界面应力已经消除，使整个相连 regular 基底成为光滑 Einstein 度量，那么 Einstein 解析性会把实双曲 germ 传播到整个 regular 基底：固定开集上 \(W^-=0\)，解析延拓给出全局 \(W^-=0\)，于是 (4.6) 成立。此后 developing-map 论证才可使用。

还有一个与体积估计有关的常数差异。对同一个 (3.1) 密度，实双曲归一化满足

\[
s=-4,\qquad W^+=0,
\qquad
F_{\mathrm{RH}}=\frac13+1=\frac43,
\]

而 CH 上 \(F_{\mathrm{CH}}=4\)。因此 O11 的“缺口除以 \(4\)”不能直接移到实双曲 O10。若 O10 有相对恒等式

\[
J-J_{\mathrm{top}}
=
\int(F-F_{\mathrm{RH}})\,dV,
\]

同样的非负性论证会产生背景密度 \(4/3\)，而不是 \(4\)；具体系数必须从 O10 自己的相对 Chern–Weil 恒等式确定。

## 5. 固定外部路线目前得到的精确结论

1. 真正极小序列的比较性质足以在每个紧 regular 可变区产生完整的局部 stationarity 和 stability；集中能量不会干扰这一传递。
2. \(C^2\) 接合足以给出 \(s=-4\) 的零迹，并在 orbifold 可去性成立时通过 \(\Delta_++1\) 的正性推出 \(s\equiv-4\)。
3. 对 \(E=\operatorname{Ric}+g\)，\(C^2\) 只给出 \(E|_\Sigma=0\)；跨界面唯一延拓还需要消除
   \((\nabla_\nu E)\delta_\Sigma\)。
4. 一旦该界面项消失，Aronszajn 延拓与 Einstein 解析性给出局部 CH 基底。
5. 任意绝对能量缺口 \(\delta\) 都强迫至少 \(\delta/4\) 的原 CH 球体积未恢复。恢复除有限点外的整个球已足以推出
   \(\liminf J_i\ge8\pi^2q\)。
6. developing-map 刚性原样适用于完备局部实双曲 orbifold；它不适用于仅知 \(\operatorname{Ric}=-g,\ W^+=0\) 的基底，除非再由固定实双曲 germ 和解析延拓得到 \(W^-=0\)。