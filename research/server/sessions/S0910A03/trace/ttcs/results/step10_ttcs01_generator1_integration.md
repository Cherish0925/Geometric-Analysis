# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 10,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step10_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step10_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a rigorous multiscale route for the following specific problem. On a fixed critical Ishida–LeBrun four-manifold suppose Ric(g_i)+g_i tends to zero in operator L-infinity norm, the calibrated nonnegative deficit has total integral tending to zero, and a positive-volume maximal-function set has uniformly bounded averages of |Rm|^2 and vanishing averages of the deficit for every radius up to 1. We may choose, for each point, the buffered downstairs domain before taking its normal/universal cover, at a radius r0 depending only on the curvature-mean bound K. Generate the strongest plausible theorem or countermodel about existence of a fixed r0 and a cover with a noncollapsed harmonic chart. Explicitly analyze persistent rank failure across all radii, the distinction between covers of B_R(p) for different R, and how the calibrated Weyl profile can exclude real-hyperbolic or Taub–NUT-type escape. Give concrete lemmas and proof ideas, not a survey, and identify exactly which statement would advance the fixed-topology negative branch.

## Integrated Scientific Memo

## 结论：目前最强可信结果是“校准化固定尺度解缠二择一”，而非一般曲率均值正则性

设 \(G_i\) 是正体积好点集，满足对每个 \(p\in G_i\) 及 \(0<r\le1\),

\[
\fint_{B_r(p)}|\Rm_{g_i}|^2\le K,\qquad
\fint_{B_r(p)}F_i\le\varepsilon_i\to0,
\]

且 \(\|\Ric_{g_i}+g_i\|_{L^\infty}\to0\)。单凭第一条不能推出局部万有覆盖非塌缩；Taub–NUT–AdS 是反例。真正需要证明的是加入校准亏损后的固定尺度命题。

### 目标定理（足以推进并实际闭合固定拓扑负分支）

对每个 \(K<\infty\)，存在

\[
r_*(K)>0,\qquad v_*(K)>0,\qquad A<\infty
\]

使得对充分大的 \(i\)，可取 \(p_i\in G_i\)、\(\rho_i\in[r_*(K),1/10]\)，以及连通正规覆盖

\[
\pi_i:(\widehat U_i,\hat p_i)\longrightarrow U_i,
\qquad
B_{A\rho_i}(p_i)\Subset U_i,
\]

满足

\[
\Vol_{\hat g_i}B_{\rho_i}(\hat p_i)\ge v_*(K)\rho_i^4
\]

并有固定比例的 \(C^1\)-调和半径下界。

这比指定“\(B_1(p)\) 的局部万有覆盖”更恰当：缓冲域 \(U_i\) 必须在取覆盖前选择，且其尺度属于结论的一部分。

一旦该定理成立，正规覆盖均值传输给出

\[
\fint_{B_a(\hat p_i)}\pi_i^*F_i\le C(A)\varepsilon_i\to0,
\qquad
\fint_{B_a(\hat p_i)}|\Rm_{\hat g_i}|^2\le C(A)K
\]

（\(a\le c\rho_i\)）。调和坐标紧性和 \(\Ric+g\to0\) 产生光滑 Einstein 局部极限

\[
\Ric_{g_\infty}=-g_\infty,
\]

而亏损消失强迫

\[
\Spec(W^+_{g_\infty})
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

这与既有常谱投影子恒等式及 Einstein–Weyl 方程矛盾。因此上述固定尺度解缠定理本身就会排除假设序列。

---

## 1. 不同缓冲半径的覆盖不能混同

定义带缓冲参数的纤维基本群

\[
\Gamma(p;\rho,A,\delta)
=
\Image\!\left[
\pi_1(B_{\delta\rho}(p))
\longrightarrow
\pi_1(B_{A\rho}(p))
\right].
\]

若 \(R_1<R_2\)，则 \(B_{R_2}(p)\) 的万有覆盖限制到 \(B_{R_1}(p)\)，对应于

\[
\ker\!\left[\pi_1(B_{R_1}(p))
\to\pi_1(B_{R_2}(p))\right],
\]

一般并不是 \(B_{R_1}(p)\) 的万有覆盖。扩大缓冲域可让更多短环在外部奇异核中收缩，故

\[
\rank\Image[\pi_1(B_\delta)\to\pi_1(B_R)]
\]

随 \(R\) 増大只能不增。

Taub–NUT 中尤其如此：小 Hopf 圆在不含 NUT 的小环域中不可缩，从而可被解缠；一旦缓冲球包含 NUT，它便可沿径向收缩，较大球的万有覆盖不再解缠该方向。这正解释了为何允许逐点选择缓冲域具有实质意义。

同时，均值传输只能用于缓冲域的真正正规覆盖，并要求所用覆盖球位于内部；不能对任意截断覆盖片套用：

\[
\fint_{B_r(\hat p)}\pi^*\phi
\le
\frac{V_{-K}^{(4)}(3r)}{V_{-K}^{(4)}(r)}
\fint_{B_r(p)}\phi .
\]

---

## 2. 最大秩情形已经可处理

若在某个固定尺度 \(\rho\) 上

\[
B_{A\rho}(p)\simeq
\mathbb R^{k-\ell}\times Z^\ell,\qquad \ell\le3,
\]

残余模型非塌缩半径有统一正下界，且

\[
\rank\Gamma(p;\rho,A,\delta)=4-k,
\]

则 Naber–Zhang 的覆盖非塌缩与调和半径定理适用，直接得到目标覆盖图表。

因此真正的障碍不是一般塌缩，而是：

\[
\boxed{\text{在每个宏观尺度、对每个合适缓冲域都持续秩亏。}}
\]

若点位于有界曲率的正规 infranil 纤维区，且较小缓冲域中没有纤维收缩核，则在可缩底球上纤维子群注入，故

\[
\rank\Gamma=4-k.
\]

所以持续秩亏意味着：每个候选尺度都必须在可比较距离内遇到奇异纤维、可缩纤维核、残余模型退化，或真正四维核。

这给出应证明的局部拓扑引理：

> **秩恢复引理。** 在有界曲率 infranil 塌缩区域中，若 \(B_{c\rho}(p)\) 不遇到奇异纤维或可缩纤维核，则存在固定 \(A',\delta\) 使  
> \[
> \rank\Image[\pi_1(B_{\delta\rho}(p))
> \to\pi_1(B_{A'\rho}(p))]=4-k.
> \]

---

## 3. 校准 Weyl 剖面排除实双曲逃逸

由于 \(\Ric+g\to0\)，有 \(s_i=-4+o(1)\)，而

\[
F_i\ge (s_i+8\sqrt6\,|W_i^+|)^2.
\]

故好球上

\[
\fint_{B_r(p)}
\left(-4+8\sqrt6|W_i^+|\right)^2\to0
\]

对所有 \(r\le1\) 一致成立。特别地，

\[
\frac{
\Vol\!\left(
\{|W_i^+|\le 1/(4\sqrt6)\}\cap B_r(p)
\right)}
{\Vol B_r(p)}
\le C\varepsilon_i\to0.
\]

因此几乎整个好球都必须满足

\[
|W_i^+|^2\approx\frac1{24}.
\]

实双曲四维空间或其实双曲 cusp 满足 \(W^+=0\)、\(s=-4\)，从而

\[
(s+8\sqrt6|W^+|)^2=16.
\]

所以它可以是有界曲率、最大秩塌缩模型，却绝不可能承载正比例的校准好集。校准亏损而非单纯曲率控制排除了它。

---

## 4. Taub–NUT–AdS 反驳弱命题，但不反驳校准命题

小参数 \(\nu\) 的 Taub–NUT–AdS 满足精确

\[
\Ric=-g,
\]

并且在距 NUT 固定距离的环带上有统一曲率界，同时总体积按 \(O(\nu)\) 塌缩。若大缓冲球包含 NUT，短 Hopf 圆在其中可缩，因此其局部万有覆盖仍塌缩。这严格反驳：

\[
\sup_{r\le1}\fint_{B_r}|\Rm|^2\le K
\quad\Longrightarrow\quad
\text{覆盖在某固定尺度非塌缩}.
\]

但其 Weyl 模长为

\[
|W|^2=
\frac{32\nu^2(4\nu^2-3)^2}{3(r+\nu)^6}.
\]

由此：

- 固定物理半径 \(r>0\) 上，\(|W|^2\to0\)，校准平方趋于 \(16\)；
- NUT 尺度 \(r=\nu x\) 上，\(|W|^2\asymp\nu^{-4}\)，远大于校准值；
- \(|W|^2=1/24\) 仅出现在
  \[
  r\asymp \nu^{1/3}
  \]
  的过渡层，而非任何固定比例的多尺度体积区域。

因此不存在 Taub–NUT–AdS 点满足

\[
\sup_{0<r\le1}\fint_{B_r(p)}F_\nu\to0.
\]

这排除了标准 NUT 剖面作为校准好点的反模型，但尚未排除所有可能的“异型校准秩亏帽”。

一个需谨慎之处是：不能仅凭小的绝对 \(\int|\Rm|^2\) 断言所有秩亏核都携带统一能量量子；来源没有提供适用于当前近 Einstein 度量的这种量子化定理。

---

## 5. 持续秩亏的精确剩余对象

若固定尺度覆盖定理失败，则在某个正体积好集上，对每个

\[
\rho\in[r_*(K),1]
\]

都发生以下至少一项：

1. \(\rank\Gamma(p;\rho,A,\delta)<4-k\)；
2. 残余 \(Z^\ell\) 的非塌缩半径趋于零；
3. 四维核或奇异纤维在距离 \(O(\rho)\) 内出现；
4. 只能在 \(\rho_i\to0\) 后解缠。

第四种情形不足以产生原有矛盾，因为重标后

\[
\Ric_{\rho_i^{-2}g_i}\approx-\rho_i^2(\rho_i^{-2}g_i)\to0,
\]

校准负 Einstein 投影子障碍随 \(\rho_i\to0\) 退化。因此必须得到依赖 \(K\) 的正下界 \(r_*(K)\)。

持续秩亏的潜在模型可进一步分为：

- **秩一可缩圆帽；**
- **nil/solvable 扭曲区；**
- **非基本自对偶联络曲率区；**
- **曲率集中奇异层。**

标准实双曲和 Taub–NUT 剖面已由校准 Weyl 条件排除；平坦高秩塌缩还受到自对偶本征线 \(O(1)\) 旋转能量的限制，但这尚未形成覆盖所有 nil 扭曲情形的定理。

---

## 6. 秩一情形的具体约化

在有界曲率正规秩一塌缩区写

\[
g_i=g_{B,i}+\ell_i^2\phi_i^2(d\psi+A_i)^2,
\qquad \ell_i\to0.
\]

忽略高阶纤维曲率项后，负 Einstein 方程给出三维静态系统

\[
\Ric_B-\phi^{-1}\nabla^2\phi=-g_B,
\qquad
\Delta_B\phi=\phi.
\tag{S}
\]

若 \(r_j\) 是 \(\Ric_B\) 的本征值，则相应四维自对偶 Weyl 本征值为

\[
w_j=-\frac23-r_j,
\qquad \sum r_j=-2.
\]

校准谱要求

\[
\Spec(\Ric_B)=
\left(-\frac12,-\frac34,-\frac34\right),
\tag{C}
\]

即

\[
\Spec(\nabla^2\phi)
=
\left(\frac12\phi,\frac14\phi,\frac14\phi\right).
\]

所以秩一持续逃逸必须在正体积区域近似满足过定系统

\[
(S)+(C).
\]

一个足以推进负分支、且远比一般塌缩正则性更集中的定理是：

> **无校准静态 NUT 帽定理。** 不存在带光滑可缩 \(S^1\) 核、统一曲率均值控制，并在某固定比例环带上满足 \(F\to0\) 的秩一近 Einstein 塌缩帽。

证明应比较光滑 Hopf 收缩核的各向同性渐近与 \((C)\) 强迫的各向异性底 Ricci 谱，并证明两者过渡必在某个居中球上产生统一正的 \(F\)-均值。

---

## 7. 不应采用的更强断言

近 Einstein 的无塌缩假设 \(L^2\)-正则性尚未由来源建立。尤其，分支中提出的

\[
\int|\Rm|^2\ll1,\quad
\Ric=-g+o_{L^\infty}(1)
\Longrightarrow
\sup|\Rm|\le C
\]

在无体积下界且仅有 \(L^\infty\) Ricci 误差时并非现成的 Cheeger–Tian 定理。曲率方程含 \(\nabla^2(\Ric+g)\)，而现有假设不给 \(\nabla h\) 或 \(\nabla^2h\) 控制。校准亏损也没有在给定材料中被证明可控制这些导数。因此不能以此宣称负分支已经闭合。

同样地，“有界截面曲率塌缩自动使指定局部万有覆盖非塌缩”也不成立；Taub–NUT 的可缩圆正是反例。必须先排除缓冲域内的收缩核或证明最大纤维秩。

---

## 8. 最精确的推进命题

当前最值得证明的是以下等价形式之一：

### 校准固定尺度覆盖定理
对每个 \(K\)，存在 \(r_*(K),v_*(K)>0\)，使任一正体积多尺度好集包含一点及尺度 \(\rho\ge r_*(K)\)，其适当缓冲正规覆盖含体积比至少 \(v_*(K)\) 的球，并具有统一调和半径。

### 校准秩亏核打包定理
对每个 \(K\)，存在 \(r_*(K),\eta_*(K)>0\)，使任何在所有 \(\rho\in[r_*(K),1]\) 上造成秩亏的核，都在某个与该核相交的好点居中球上强迫

\[
\fint F\ge\eta_*
\]

或携带可定量控制的曲率/拓扑电荷；这些核因全局能量预算和 \(\mathcal M_1F\to0\) 不能覆盖正体积好集。

第一条直接结合 Naber–Zhang 与均值传输产生禁阻 Einstein germ；第二条是处理“所有尺度持续秩亏”的具体多尺度机制。真正未决的科学对象正是：**能否存在既保持校准 Weyl 谱、又通过可缩纤维或 nil 扭曲在所有固定尺度破坏最大秩的局部帽模型。** 标准实双曲和 Taub–NUT–AdS 均不是这种模型。