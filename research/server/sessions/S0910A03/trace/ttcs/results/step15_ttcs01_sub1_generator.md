# TTCS Independent Branch Record

```json
{
  "step_id": 15,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A03/workspace/notes/step13_smoothing_bridge_and_L2_propagation.md",
    "Sessions/S0910A03/workspace/scripts/verify_L2_completion_square_chain.py"
  ]
}
```

## Task

On a fixed critical Ishida-LeBrun 4-manifold M with Einstein defect E = Ric+g and a normalized cutoff flow ∂_t g = -2χ²E, the evolution of the GLOBAL L² defect Q(t) = ∫_M |E(t)|² dμ(t) is the key quantity for the topological near-saturation argument.

The challenge: the integrated energy inequality involves terms with |Rm||E|², and |Rm| is not initially bounded (Weyl can be large). The flow produces bounded curvature only after a positive time, creating a bootstrap problem.

GENERATE a concrete mechanism to control Q(t) on a short time interval [0,T] with T = O(r₀²), specifically:

1. Can the L² estimate be SEPARATED from the curvature bootstrap? For example: (a) On the plateau (χ=1), Li's Cor 3.5 gives |E| ≤ Cδ(r²/t)^{2/3}, so ∫_plateau|E(t)|² is controlled. (b) The frozen exterior contributes ∫_frozen|E₀|² = O(δ²Vol). (c) For the transition region: explore whether the DEGENERATE parabolic structure (coefficient χ² between 0 and 1) provides enough suppression. The L² contribution from the transition has width D, and |E|² there might be controlled by interpolation between the plateau (small E) and frozen boundary (E = δ).

2. Alternatively: can the GLOBAL L² estimate be obtained directly from the fact that every term in the cutoff equation is homogeneous in E? Even without a pointwise |Rm| bound, the reaction ∫|Rm||E|² might be controlled by using the INITIAL L² bound on |Rm|² (which is O(A) from topology) combined with a 4D Sobolev inequality on a COVERING by balls. Does the bounded-overlap covering + relative Sobolev produce a collapse-independent global Sobolev constant?

3. Or: can we avoid the global Q(t) estimate entirely by using only the INTEGRAL identities? The completion-square chain gives ∫(|W⁺|-1/(2√6))² ≤ 0.41∫|E|² for any metric. If we can show that the INTEGRATED ∫∫₀ᵀ|E(t)|² dt dμ is controlled (even if Q(t) at specific times is not), this might suffice for a time-averaged topological argument.

Look for the simplest, most robust mechanism.

## Output

### 核心结论

\(Q(t)\) 可以与点态 \(C/t\) 曲率估计分离，但不能与动态的局部 \(L^2\) 曲率小性完全分离。最简洁的机制不是把流形拆成平台、过渡区和冻结区后做空间插值，而是把

\[
\int \chi^2|\mathrm{Rm}|\,|E|^2
\]

看成相对于退化扩散能量

\[
\int \chi^2|\nabla E|^2
\]

的二次型扰动。四维相对 Sobolev 不等式与每个活动球上的归一化曲率能量相乘后，体积因子逐球消去。这样可直接得到全局 \(Q(t)\) 的 Gronwall 估计；所需曲率信息只是动态局部 \(L^2\) 小性，而不是点态曲率上界。

---

## 1. 全局 \(Q\) 的局部二次型估计

令 \(a=\chi^2\)，\(U=\operatorname{supp}\chi\)。把体积元演化

\[
\partial_t d\mu=-a\,\tau\,d\mu,\qquad \tau=\operatorname{tr}E
\]

加入 Step 14 的积分公式，可写成

\[
\frac{dQ}{dt}
+c_0\int_M a|\nabla E|^2
\le
C_0(1+\|\nabla\chi\|_\infty^2)Q
+C_0\int_U a|\mathrm{Rm}|\,|E|^2 .
\tag{1}
\]

体积项不会产生新的结构，因为在四维

\[
|\tau||E|^2\le 2|E|^3
\le C(1+|\mathrm{Rm}|)|E|^2,
\]

这里使用了 \(|E|\le C(1+|\mathrm{Rm}|)\)。因此它可并入 (1) 的两个右端项。

取半径 \(\rho\asymp r_0\) 的球 \(B_\alpha\) 覆盖 \(U\)，重叠数仅依赖维数；取

\[
\sum_\alpha\psi_\alpha^2=1,\qquad
|\nabla\psi_\alpha|\le C\rho^{-1}.
\]

假设沿流有短时度量等价，并且每个加倍球满足相对 Sobolev 不等式

\[
\left(\int |v|^4\right)^{1/2}
\le
S\,V_\alpha^{-1/2}
\left(
\rho^2\int|\nabla v|^2+\int v^2
\right),
\tag{2}
\]

以及动态归一化能量小性

\[
\varepsilon_\alpha(t)
=
\frac{\rho^4}{V_\alpha(t)}
\int_{2B_\alpha}|\mathrm{Rm}(t)|^2
\le\varepsilon_* .
\tag{3}
\]

对 \(F_\alpha=\psi_\alpha\chi |E|\)，Hölder 与 (2) 给出

\[
\begin{aligned}
\int |\mathrm{Rm}|F_\alpha^2
&\le
\|\mathrm{Rm}\|_{L^2(2B_\alpha)}
\|F_\alpha\|_{L^4}^2\\
&\le
S\varepsilon_*^{1/2}
\left(
\int|\nabla F_\alpha|^2
+\rho^{-2}\int F_\alpha^2
\right).
\end{aligned}
\tag{4}
\]

关键消去正是

\[
\|\mathrm{Rm}\|_2
\le \varepsilon_*^{1/2}V_\alpha^{1/2}\rho^{-2},
\qquad
V_\alpha^{1/2}\cdot V_\alpha^{-1/2}=1.
\]

若过渡宽度为 \(D\)，则求和后

\[
\int_U \chi^2|\mathrm{Rm}|\,|E|^2
\le
CS\varepsilon_*^{1/2}
\int_U\chi^2|\nabla E|^2
+
CS\varepsilon_*^{1/2}
(\rho^{-2}+D^{-2})Q.
\tag{5}
\]

只要 \(CS\varepsilon_*^{1/2}<c_0/2\)，第一项被 (1) 左端吸收，于是

\[
\frac{dQ}{dt}
\le
C(1+\rho^{-2}+D^{-2})Q.
\tag{6}
\]

因此，当 \(D\asymp\rho\asymp r_0\) 且 \(T=\theta r_0^2\) 时，

\[
\boxed{
Q(t)\le
\exp\!\bigl(C(1+\rho^{-2}+D^{-2})t\bigr)Q(0)
\le C_\theta Q(0).
}
\tag{7}
\]

初始点态估计 \(|E(0)|\le\delta\) 给出

\[
Q(0)\le \delta^2\operatorname{Vol}(M,g_0),
\]

而临界 Ishida–LeBrun 序列的体积由既有拓扑恒等式一致控制，故

\[
Q(t)\le C_\theta\delta^2\longrightarrow0.
\tag{8}
\]

这一步不需要 Li 的点态 \(C/t\) 曲率估计，也不需要先分别估计平台与过渡区。Li 的 Corollary 3.5 可随后用于平台上的点态 \(E\) 估计。

---

## 2. 动态局部曲率小性可与局部缺陷能量组成闭合系统

真正需要建立的是 (3)，但它可以在点态平滑之前由一个较弱的耦合能量系统得到。

在活动缓冲区取嵌套截断 \(\phi_\alpha\)，以初始体积归一化定义

\[
R_\alpha(t)
=
\frac{\rho^4}{V_\alpha(0)}
\int \phi_\alpha^2|\mathrm{Rm}|^2,
\qquad
P_\alpha(t)
=
\frac{\rho^4}{V_\alpha(0)}
\int \phi_\alpha^2|E|^2,
\]

并令

\[
\mathcal R(t)=\sup_\alpha R_\alpha(t),
\qquad
\mathcal P(t)=\sup_\alpha P_\alpha(t).
\]

所有中心及其相邻加倍球都位于同一个缓冲区。这样内球能量右端出现的外球能量，可由全中心上确界闭合，而不会重现 Step 13 的内外量不一致。

在 \(\mathcal R(t)\le\varepsilon_*\) 时，预期的精确能量系统为

\[
D^+\mathcal P
\le C\rho^{-2}\mathcal P,
\tag{9}
\]

\[
D^+\mathcal R
\le C\rho^{-2}(\mathcal R+\mathcal P),
\tag{10}
\]

其中 \(D\asymp\rho\)。其来源逐项清楚：

* 三次曲率项用
  \[
  \int \chi^2|\mathrm{Rm}|^3
  =
  \int |\mathrm{Rm}|\,|\chi\mathrm{Rm}|^2
  \]
  与 (2) 处理，在 \(\mathcal R^{1/2}\) 足够小时吸收进
  \(\int\chi^2|\nabla\mathrm{Rm}|^2\)。

* 过渡项
  \[
  \nabla a*\nabla E*\mathrm{Rm}
  \]
  使用 \(\nabla E=\nabla\operatorname{Ric}\)，因而由 \(\nabla\mathrm{Rm}\) 控制，并利用
  \[
  \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2.
  \]

* 项
  \[
  \nabla^2a*E*\mathrm{Rm}
  \]
  给出
  \[
  CD^{-2}\int(|E|^2+|\mathrm{Rm}|^2).
  \]
  它只贡献 \(\mathcal P+\mathcal R\)，没有与 \(E\) 无关的过渡源。

由 (9)–(10)，令 \(s=t/\rho^2\)，得到

\[
\mathcal P(t)\le e^{Cs}\mathcal P(0),
\tag{11}
\]

\[
\mathcal R(t)
\le
e^{Cs}\bigl(\mathcal R(0)+Cs\,\mathcal P(0)\bigr).
\tag{12}
\]

初始时

\[
\mathcal P(0)\le \delta^2\rho^4,
\qquad
\mathcal R(0)\le C K_0\rho^4.
\]

最大函数好点允许先固定一个足够小但与序列指标无关的 \(\rho>0\)，使 \(\mathcal R(0)\) 留有固定余量；随后 \(\delta\to0\)。于是 (12) 保持动态局部能量小性，(5)–(8) 同时给出全局缺陷控制。之后 Li 的 Moser 机制才负责产生平台上的 \(C/t\) 曲率估计和 \(O(\delta)\) 点态缺陷。

因此，最自然的逻辑结构是：

\[
\text{局部 }(\mathcal R,\mathcal P)\text{ 能量}
\Longrightarrow
Q(t)\le C Q(0)
\Longrightarrow
\text{Li 点态平滑}.
\]

点态曲率不必进入 \(Q\) 的第一轮估计。

---

## 3. 退化系数的作用不是空间插值

过渡区不能仅凭平台侧和冻结侧的点态值做稳健插值。若在冻结侧附近

\[
\chi(s)\sim s/D,\qquad a(s)\sim s^2/D^2,
\]

并令 \(u_\epsilon\) 在宽度 \(\epsilon\) 内变化固定振幅 \(A\)，则

\[
\int_0^\epsilon a(s)|u_\epsilon'(s)|^2\,ds
\asymp
\frac{A^2}{D^2}\epsilon
\longrightarrow0.
\]

所以加权梯度能量并不强制两侧迹值之间的定量插值。

退化结构真正有利之处是：扩散与危险反应项带有同一个 \(\chi^2\)。把 Sobolev 不等式应用于 \(\chi E\) 后，反应项正好由退化梯度能量吸收；导数落在 \(\chi\) 上时只留下

\[
|\nabla\chi|^2|E|^2,
\]

这是对 \(Q\) 的乘法型贡献。过渡区因而由全局能量式本身控制，而不是由一维空间插值控制。

---

## 4. 总曲率 \(L^2\) 有界不能替代逐球小性

即使已知

\[
\int_M|\mathrm{Rm}|^2\le C(A),
\]

有界重叠覆盖也不会自动产生与塌缩无关的全局 Sobolev 常数。相对 Sobolev 系数含有 \(V_\alpha^{-1/2}\)；它仅在与同一球上的

\[
\|\mathrm{Rm}\|_{L^2(B_\alpha)}
\]

配对后，通过归一化能量 \(\varepsilon_\alpha\) 消去。总能量有界既不控制每个 \(\varepsilon_\alpha\)，也不排除曲率集中于体积极小的球。

抽象模型也显示“方程关于 \(E\) 齐次”本身不够。对

\[
\partial_tu=\Delta u+V_\epsilon u
\]

取四维势

\[
V_\epsilon=c\epsilon^{-2}\mathbf 1_{B_\epsilon},
\qquad
\|V_\epsilon\|_{L^2}\asymp c.
\]

其 Rayleigh 商可具有 \(O(\epsilon^{-2})\) 的正增长率，尽管势的全局 \(L^2\) 范数保持不变。真正决定统一 \(L^2\) 演化的是局部二次型小性，恰好对应 (3)–(5)。

因此，拓扑给出的全局曲率能量适合控制总量；活动缓冲区的最大函数好点则提供吸收反应项所需的逐球小性。

---

## 5. 时间平均在逻辑上足够，但没有绕开过渡区

令

\[
Z(t)=
\int_M\bigl(s+8\sqrt6\,|W^+|\bigr)^2\,d\mu_t.
\]

每个时刻都有

\[
Z(t)\le108Q(t).
\]

若能得到

\[
\int_{T/2}^{T}Q(t)\,dt=o(T),
\tag{13}
\]

则存在 \(t_*\in[T/2,T]\) 满足

\[
Q(t_*)\le
\frac2T\int_{T/2}^{T}Q(t)\,dt=o(1),
\]

从而 \(Z(t_*)=o(1)\)，足以在该时刻恢复拓扑校准轮廓。

但 Corollary 3.5 单独不能给出从 \(0\) 开始的时空 \(L^2\) 控制，因为

\[
|E(t)|^2\lesssim
\delta^2r^{8/3}t^{-4/3},
\qquad
\int_0^Tt^{-4/3}\,dt=\infty.
\]

在晚时段 \([T/2,T]\)，它确实给出平台上的 \(O(\delta^2)\) 控制；冻结区也保持初始 \(O(\delta^2)\)。尚余的仍是过渡区。仅控制

\[
\int\!\!\int \chi^2|E|^2
\]

不能控制 \(\chi\) 很小区域中的无权 \(L^2\) 质量。因此时间平均路线最终仍需 (5) 所表达的局部二次型吸收，或者一个数学上等价的退化半群估计。

---

### 最简洁的分析对象

最有力的局部命题形态是：在活动缓冲区所有中心的初始归一化 \(L^2\) 曲率能量足够小、过渡宽度与球半径可比、短时度量等价成立时，归一化截断流满足耦合估计 (9)–(10)，并进而满足全局估计 (7)。

其中最需要完整张量推导的是局部曲率能量式 (10)：必须把  
\(\nabla a*\nabla E*\mathrm{Rm}\) 与 \(\nabla^2a*E*\mathrm{Rm}\) 精确归入 \(\rho^{-2}(\mathcal R+\mathcal P)\)，再以全中心上确界闭合嵌套球项。这个命题一旦成立，全局 \(Q(t)\)、拓扑近饱和以及平台上的 Li 平滑便形成一条直接链路。