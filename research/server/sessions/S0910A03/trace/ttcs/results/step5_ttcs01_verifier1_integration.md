# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 5,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the proposed local-limit route for the fixed critical Ishida–LeBrun sequence. Starting from the exact quantitative deficit decomposition and Weyl norm profile, determine precisely what convergence on a harmonic-radius patch yields for (i) the selected Seiberg–Witten 2-form/eigenline, (ii) the W+ eigenvalue multiplicities, and (iii) the limiting Einstein metric. Check whether the nonnegative eigenvalue defect plus amplitude/Hodge projection control forces the limiting spectrum (-1/6,1/12,1/12) on a regular patch. Then check the Derdzinski consequence carefully: is this spectrum locally impossible at Ric=-g, or does it give a locally conformally Kähler noncompact model? Resolve conventions, conformal factor, scalar curvature, and Bochner formula, and identify the strongest true theorem.

## Integrated Scientific Memo

# 核验结论：正则局部极限给出校准谱，但 Derdziński 不产生局部矛盾

设固定临界 Ishida–LeBrun 流形上的度量满足

\[
\delta_i=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{L^\infty}\to0 .
\]

固定拓扑意味着 \(A\) 固定，且符号 monopole 类只有有限多个；取子列可固定所选类 \(a\)。定量分解给出

\[
R_i=O(A\delta_i^2),\qquad \Delta_{a,i}=O(A\delta_i^2),
\]

所以 \(D_{\rm amp},D_{\rm Hodge},D_{\rm eig},J_A\to0\)，并且

\[
\|f_i\varphi_i+6\sqrt2\pi H_i\|_2\to0,\qquad
\left\||2\pi H_i|-\frac{q_i}{3\sqrt2}\right\|_2\to0.
\tag{1}
\]

此外

\[
s_i\to-4\quad\text{一致},\qquad
|W_i^+|\to \frac1{2\sqrt6},\qquad q_i\to\frac92
\quad\text{于 }L^2 .
\tag{2}
\]

这里 \(q_i=-s_i+\sqrt6|W_i^+|\)。

## 1. harmonic-radius patch 上真正得到什么

假设 \(x_i\) 周围存在固定尺度的 \(C^{2,\alpha}\) harmonic-radius 坐标片。缩小坐标片并拉回后，

\[
g_i\to g_\infty\quad\text{于 }C^{2,\beta}_{\rm loc},
\]

从而经 Einstein 方程 bootstrap，

\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad s_\infty=-4,
\tag{3}
\]

且 \(g_\infty\) 光滑。由曲率一致收敛和 (2)，

\[
|W_\infty^+|\equiv\frac1{2\sqrt6},\qquad |W_\infty^+|^2=\frac1{24}.
\tag{4}
\]

### (i) 所选 SW 二形式与本征线

调和形式 \(H_i\) 有统一全局 \(L^2\) 范数；局部椭圆估计给出子列

\[
H_i\to H_\infty
\]

于更小坐标片上光滑收敛，其中 \(H_\infty\) 调和、自对偶。由 (1)、(2) 及强局部收敛，

\[
|H_\infty|\equiv \frac{3}{4\sqrt2\pi}>0.
\tag{5}
\]

取正则化权重 \(f_i\to\sqrt{9/2}=3/\sqrt2\)，则

\[
\varphi_i\to -4\pi H_\infty,\qquad
\psi_i=\frac23\varphi_i\to
\psi_\infty=-\frac{8\pi}{3}H_\infty,
\tag{6}
\]

至少强 \(L^2_{\rm loc}\)；因此

\[
|\psi_\infty|=\sqrt2,\qquad d\psi_\infty=d^*\psi_\infty=0.
\tag{7}
\]

故在该正则片上，极限 SW 二形式处处非零、闭且自对偶，定义局部 almost-Kähler 结构，并张成一个光滑实线丛。

这里需要区分两点：

* 对**极限形式**，非消失由 harmonic-form 的局部椭圆紧性和 (1)–(2) 得到；
* 仅凭原序列的全局 \(L^2\) 估计，并不能断言每个 \(\psi_i\) 在该片上都点态非零，也不能直接获得全局 almost-Kähler 结构。那仍需要 \(C^0\) 型升级。

在当前重标度约定中 \(|\Phi_i|^2\to\sqrt2\)，不能与另一套未重标度方程中的“\(|\Phi|^2\to4\)”混用。

### (ii) \(W^+\) 的本征值重数

定义非负代数缺陷

\[
\mathcal E(W,v)=\langle Wv,v\rangle+
\sqrt{\frac23}|W|\,|v|^2.
\]

因为

\[
D_{{\rm eig},i}=2\int \mathcal E(W_i^+,\psi_i)\to0,
\]

而 \(W_i^+\to W_\infty^+\)、\(\psi_i\to\psi_\infty\neq0\)，极限上

\[
\mathcal E(W_\infty^+,\psi_\infty)=0.
\tag{8}
\]

所以 \(\psi_\infty\) 张成最低本征线，并且

\[
\lambda_{\min}
=-\sqrt{\frac23}|W_\infty^+|=-\frac16.
\tag{9}
\]

非负性本身来自迹零三维对称算子的尖锐估计

\[
\lambda_{\min}\ge-\sqrt{\frac23}|W|.
\]

取等当且仅当另外两个本征值相等。结合迹零与 (9)，

\[
\boxed{\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)}.
\tag{10}
\]

因此答案是肯定的：**在上述正则极限片上，非负本征值缺陷加振幅和 Hodge/调和投影控制确实强制完整谱 (10)**。最低本征值简单，最大本征值重数二。

### (iii) 极限 Einstein 度量

局部极限满足

\[
\operatorname{Ric}=-g,\quad s=-4,\quad
|W^+|^2=\frac1{24},\quad
\operatorname{Spec}(W^+)=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{11}
\]

它既不是复双曲型 Kähler–Einstein bulk（后者在 \(s=-4\) 时
\(|W^+|^2=2/3\)），也不是实双曲型（后者 \(W^+=0\)）。

## 2. Derdziński 的正确后果

谱 (10) 位于

\[
\alpha=\beta=\frac1{12},\qquad \gamma=-\frac16,
\]

即**最大本征值二重、负的最低本征值简单**。因此 Catino–Dameno 关于“最大本征值一致简单”的定理不适用：这里恰为其尖锐边界

\[
\frac{\det W^+}{|W^+|^3}=-\frac1{3\sqrt6},\qquad \rho=\beta/\alpha=1.
\]

适用的是原始 Derdziński 两本征值结论：在简单最低本征线可定向的局部双覆盖上，存在正函数 \(f\)，使

\[
\widetilde g=f^2g_\infty
\]

为 Kähler 度量。其 Kähler 标量曲率 \(\widetilde s\) 为负，并由 Weyl 本征值的共形权重满足

\[
f^2\widetilde s=-1.
\tag{12}
\]

注意：不能因为 \(|W_g^+|\) 恒定，就断言这个负分支的 \(f\) 恒定。文献中常见的
\(\alpha_h^{2/3}h\) 归一化针对的是**最大简单正本征值**分支；本题处在最大本征值二重的相反分支。将该公式直接移用到这里，是导致“局部不可能”错误结论的根源。

采用几何学家的非负 Laplacian

\[
\nabla^*\nabla=d^*d=-\operatorname{div}\nabla,
\]

标量曲率共形变换与 (12)、\(s_g=-4\) 给出

\[
\boxed{\nabla^*\nabla f=\frac12 f}.
\tag{13}
\]

等价地，若 \(\Delta=\operatorname{div}\nabla\)，则

\[
\Delta f=-\frac12f.
\]

这在开集或非紧流形上完全可能有正解。因此：

\[
\boxed{\text{谱 (10) 在 }\operatorname{Ric}=-g\text{ 下并非局部不可能。}}
\]

它给出的是负标量 Kähler 度量的局部共形 Einstein 模型。

## 3. 紧致性为何产生矛盾

若同一结构存在于闭流形上，(13) 与 \(f>0\) 导致

\[
0=\int_M\nabla^*\nabla f\,d\mu
=\frac12\int_M f\,d\mu>0,
\]

矛盾。等价地，闭流形上正本征值对应的 Laplace 本征函数不可能保持正号。

这与 LeBrun–Armstrong 的全局结论一致：闭 Einstein 度量若饱和相应 monopole 不等式，则必须为 Kähler–Einstein；但 \(s=-4\) 的 Kähler 度量具有

\[
\operatorname{Spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right),\qquad
|W^+|^2=\frac23,
\]

而非 (10)。所以矛盾是**紧致/全局的**，不是纯局部的。

非紧时不能无条件使用 Stokes；所需边界衰减或容量条件并未从当前局部极限推出。现有共形 Kähler–Einstein、Poincaré–Einstein 构造说明这种非紧机制本身是合理的，但供应材料尚未给出一个同时满足 (11) 全部常数条件的完整显式模型。

## 4. Bochner 公式与数值修正

Einstein 四流形上，按上述 Laplacian 约定，

\[
\frac12\Delta |W^+|^2
=
|\nabla W^+|^2+\frac{s}{2}|W^+|^2
-6\operatorname{tr}\bigl((W^+)^3\bigr).
\tag{14}
\]

对 (10)，

\[
|W^+|^2=\frac1{24},\qquad
\operatorname{tr}\bigl((W^+)^3\bigr)=-\frac1{288}.
\]

因范数恒定，(14) 给出

\[
\boxed{|\nabla W^+|^2=\frac1{16}}.
\tag{15}
\]

所以该假想局部模型的 \(W^+\) 非平行，并非局部对称。先前使用系数
\((s/3,-4)\) 得到的 \(1/24\) 不符合 Catino–Dameno 的 Einstein–Weyl Weitzenböck 方程，应改为 (14)–(15)。Bochner 公式没有产生矛盾，反而与非平行的局部共形 Kähler 模型相容。

## 5. 最强成立的定理

当前材料支持的最强结论是：

> **正则局部极限定理。**  
> 固定临界 Ishida–LeBrun 流形上的近 Einstein 序列，若在某些未缩放固定尺度 harmonic-radius 片上收敛，则任何光滑极限片都满足 (11)，其选定 SW 极限二形式是处处非零的最低 Weyl 本征形式，并局部定义 almost-Kähler 结构。该片由 Derdziński 局部共形于负标量 Kähler 度量，其共形因子满足 (13)。这些条件局部并不矛盾。

相应的全局结论仍是：

> 若另有统一全局 harmonic-radius 下界和直径上界，则得到同一闭流形上的光滑 Einstein 极限；紧致 Stokes 或 LeBrun–Armstrong 刚性随后排除该极限。因此任何假想序列必须发生 harmonic-radius 退化或直径逃逸。

不能由现有论证推出

\[
\sup_x r_h(x,g_i)\to0,
\]

因为单个正则片只产生非紧/有边界局部模型，而该模型没有局部矛盾。可推出的仍只是全局有界几何排斥，或等价的

\[
\inf_x r_h(x,g_i)\to0
\quad\text{或}\quad
\operatorname{diam}(M,g_i)\to\infty
\]

这一退化二分。

精确剩余对象是：是否存在完整非紧 Einstein 四流形满足 (11)，以及能否从原紧流形序列获得足以对其共形因子应用全局积分的衰减、有限体积或零容量条件。没有这些附加信息，Derdziński 路线不能单独排除局部正则极限。