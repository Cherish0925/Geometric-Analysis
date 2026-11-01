# TTCS Independent Branch Record

```json
{
  "step_id": 15,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Sessions/S0910A03/workspace/scripts/verify_L2_completion_square_chain.py"
  ]
}
```

## Task

Verify the following proposed L² completion-square chain for the Yau Problem 26 negative-branch program on a fixed critical Ishida-LeBrun 4-manifold M.

CHAIN CLAIM: For ANY Riemannian metric g on M (not just the original near-Einstein sequence), the following hold:
(a) Chern-Gauss-Bonnet: I - R = 2A/3 where I = (4pi²)⁻¹∫(s²/24 + 2|W⁺|²), R = (8pi²)⁻¹∫|Ric₀|².
(b) Seiberg-Witten monopole: K ≥ A where K = (72pi²)⁻¹∫(s - √6|W⁺|)².
(c) Completion square: ∫(s + 8√6|W⁺|)² ≤ 864pi²R ≤ 108∫|E|² where E = Ric + g.
(d) Consequence: ∫(|W⁺| - 1/(2√6))² ≤ C∫|E|² with C ≈ 0.41.

VERIFY EACH STEP. In particular:
1. Is (b) really metric-independent? The SW inequality involves metric data; check that the final bound K ≥ A uses only topological invariants after minimizing over metrics.
2. Does the chain from R → calibrated Weyl profile require volume control as an additional input? Or is the bound (d) truly volume-independent?
3. The CRITICAL QUESTION: After applying a normalized cutoff flow ∂_t g = -2χ²(Ric+g), the evolved metric g(t) is still on M. Does the chain apply to g(t) without additional hypotheses? What if the flow develops singularities or degeneracies?
4. For the forbidden-germ contradiction (Step 6), we need not just |W⁺| ≈ 1/(2√6) but the specific eigenvalue structure (-1/6, 1/12, 1/12). Does the L² Weyl modulus convergence suffice to extract eigenvalue information, or is additional compactness needed? What is the MINIMAL additional input beyond ∫|E|² → 0 to reach the contradiction?

## Output

# 科学复核备忘

## 总结

在固定定向的临界 Ishida–LeBrun 四维流形 \(M\) 上，并把 Bauer–Furuta 给出的全部符号类作为已知拓扑数据时：

- **(a) 正确**，是任意光滑 Riemann 度量的 Chern–Gauss–Bonnet 恒等式。
- **(b) 正确**，但关键不是先对度量作变分，而是对有限个 monopole 符号类作逐度量选择。最终确有 \(K_g\ge A\) 对每个 \(g\) 成立。
- **(c) 正确**，系数 \(864\pi^2\) 与 \(108\) 都正确。
- **(d) 正确且不需要预先控制体积。** 脚本给出的约 \(0.41\) 是可用但较松的常数；利用 \(E\) 的正交迹分解可改进为
  \[
  \boxed{\int_M\left(|W^+|-\frac1{2\sqrt6}\right)^2d\mu
  \le \frac7{24}\int_M|E|^2d\mu.}
  \]
- 截断流之后，只要 \(g(t)\) 仍是原闭流形上的光滑正定度量，整个静态链条逐时成立；链条本身不提供流的存在时间，也不提供 \(\int|E(t)|^2\) 从初始时刻到后来时刻的控制。
- Weyl 模长收敛不能决定三个特征值。Step 6 的局部矛盾还需要 Weyl 代数形状的极值关系，以及足以把积分关系传到光滑 Einstein 开集上的局部紧性。

---

## 1. Chern–Gauss–Bonnet 部分

固定与 monopole 类一致的定向。四维公式为

\[
(2\chi+3\tau)(M)
=\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W^+|^2-\frac{|\Ric^\circ|^2}{2}\right)d\mu .
\]

因此按题中定义，

\[
I-R=(2\chi+3\tau)(M).
\]

临界关系 \(D=A/3\) 给出

\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3},
\]

故

\[
\boxed{I-R=\frac{2A}{3}}.
\]

这是纯静态恒等式，对 \(M\) 上每个光滑度量均成立。

---

## 2. \(K_g\ge A\) 的逐度量证明

对每个 Bauer–Furuta 符号类写成

\[
a_{\varepsilon,\eta}
=\sum_j\varepsilon_jc_j+\sum_\ell\eta_\ell e_\ell ,
\]

其中 \(e_\ell\) 表示拓扑上来自 \(N\) 的类，以免和 Einstein 缺陷 \(E=\Ric+g\) 混淆。对任意给定度量 \(g\)，取 Hodge 分解，并对所有独立符号平均：

\[
\operatorname{Av}_{\varepsilon,\eta}
\bigl\|(a_{\varepsilon,\eta})^+\bigr\|_2^2
=
\sum_j\|c_j^+\|_2^2+\sum_\ell\|e_\ell^+\|_2^2 .
\]

又因为

\[
\|c_j^+\|_2^2=c_j^2+\|c_j^-\|_2^2,
\qquad
\sum_jc_j^2=A,
\]

所以

\[
\operatorname{Av}_{\varepsilon,\eta}
\bigl\|(a_{\varepsilon,\eta})^+\bigr\|_2^2
=
A+\sum_j\|c_j^-\|_2^2+\sum_\ell\|e_\ell^+\|_2^2
\ge A.
\]

于是对每个 \(g\)，至少存在一个符号向量，使

\[
\bigl\|(a_{\varepsilon,\eta})^+\bigr\|_2^2\ge A.
\]

对这个 monopole 类应用源中的 scalar–Weyl 估计：

\[
\frac1{72\pi^2}\int_M
(s-\sqrt6|W^+|)^2d\mu
\ge \bigl\|(a_{\varepsilon,\eta})^+\bigr\|_2^2.
\]

因此

\[
\boxed{K_g\ge A\qquad\text{对每个光滑 }g.}
\]

这里被选中的符号类可以随 \(g\) 改变；并不需要它沿度量路径连续变化。因而

\[
\inf_g K_g\ge A
\]

只是上述逐度量结论的直接推论，而不是其证明来源。

这一部分确实需要“全部独立符号类均为 monopole 类”这一 Ishida–LeBrun/Bauer–Furuta 输入。只有数值关系 \(D=A/3\) 而没有这组类时，不能推出 \(K_g\ge A\)。

---

## 3. 配方恒等式与常数

令 \(w=|W^+|\)。逐点恒等式为

\[
27\left(\frac{s^2}{24}+2w^2\right)
-(s-\sqrt6w)^2
=\frac18(s+8\sqrt6w)^2.
\]

设

\[
L:=\int_M(s+8\sqrt6w)^2d\mu .
\]

积分并代入 \(I,K\)：

\[
\frac18L
=27(4\pi^2I)-72\pi^2K,
\]

亦即

\[
L=288\pi^2(3I-2K).
\]

利用 \(I=2A/3+R\) 和 \(K\ge A\)，

\[
3I-2K
\le 3\left(\frac{2A}{3}+R\right)-2A
=3R.
\]

所以

\[
\boxed{L\le864\pi^2R}.
\]

再由

\[
R=\frac1{8\pi^2}\int_M|\Ric^\circ|^2d\mu
\]

得到

\[
864\pi^2R=108\int_M|\Ric^\circ|^2d\mu.
\]

而

\[
E^\circ=(\Ric+g)^\circ=\Ric^\circ,
\qquad |E^\circ|^2\le |E|^2,
\]

故

\[
\boxed{
\int_M(s+8\sqrt6|W^+|)^2d\mu
\le108\int_M|E|^2d\mu.}
\]

这些推导不使用 \(E\) 的点态小量性。

同时还有精确公式

\[
K=A+\frac32R-\frac{L}{576\pi^2},
\]

从而

\[
0\le K-A\le\frac32R.
\]

所以若 \(\int|E|^2\to0\)，则 \(K\to A\)。

---

## 4. Weyl 模长估计无需体积输入

设

\[
q=s+4=\operatorname{tr}E,\qquad
v=w-\frac1{2\sqrt6}.
\]

则

\[
s+8\sqrt6w=q+8\sqrt6v.
\]

记

\[
P=\int|\Ric^\circ|^2,\qquad
X=\int q^2,\qquad
Q=\int|E|^2.
\]

由于迹部分与无迹部分正交，

\[
E=\Ric^\circ+\frac q4g,
\qquad
Q=P+\frac14X.
\]

由上一节

\[
\|s+8\sqrt6w\|_2\le\sqrt{108P}=6\sqrt3\,P^{1/2}.
\]

因此

\[
\begin{aligned}
8\sqrt6\,\|v\|_2
&\le \|s+8\sqrt6w\|_2+\|q\|_2\\
&\le 6\sqrt3\,P^{1/2}+2\left(\frac X4\right)^{1/2}\\
&\le \sqrt{108+4}\left(P+\frac X4\right)^{1/2}\\
&=\sqrt{112}\,Q^{1/2}.
\end{aligned}
\]

平方后得到

\[
\boxed{
\int_M\left(w-\frac1{2\sqrt6}\right)^2d\mu
\le\frac{112}{384}Q
=\frac7{24}Q.}
\]

因此该估计完全不依赖体积。

`verify_L2_completion_square_chain.py` 中约 \(0.41\) 的值来自把 \(P\le Q\) 与 \(X\le4Q\) 分开使用，重复消耗了同一个 \(Q\)。此外，脚本文字中的判别式 `172416` 是算术笔误；代码实际计算的是

\[
32^2\cdot6+4\cdot384\cdot108=172032.
\]

对应的较松常数约为 \(0.4123\)，仍然有效。

---

## 5. 完整体积与能量轮廓也无需另加体积假设

设固定 \(M\) 上 \(Q_i\to0\)。于是 \(R_i\to0\) 且

\[
I_i\to\frac{2A}{3}.
\]

首先，因 scalar 项是 \(I_i\) 的一部分，

\[
\|s_i\|_2^2\le96\pi^2I_i.
\]

又有 \(\|q_i\|_2\le2Q_i^{1/2}\)，故

\[
4\operatorname{Vol}(g_i)^{1/2}
=\|4\|_2
\le\|s_i\|_2+\|q_i\|_2.
\]

右端一致有界，所以体积自动有界。于是

\[
\int s_i^2
=16\operatorname{Vol}(g_i)-8\int q_i+\int q_i^2
=16\operatorname{Vol}(g_i)+o(1),
\]

并由上一节的 \(v_i\to0\) 得到

\[
\int w_i^2
=\frac1{24}\operatorname{Vol}(g_i)+o(1).
\]

因此

\[
I_i
=\frac1{96\pi^2}\int s_i^2
+\frac1{2\pi^2}\int w_i^2
=\frac{3}{16\pi^2}\operatorname{Vol}(g_i)+o(1).
\]

结合 \(I_i\to2A/3\)：

\[
\boxed{\operatorname{Vol}(g_i)\to\frac{32\pi^2A}{9}},
\]

以及

\[
\boxed{S_i\to\frac{16A}{27},\qquad W_i\to\frac{2A}{27}}.
\]

需要区分：若只知道 \(R_i\to0\)，只能推出

\[
s_i+8\sqrt6|W_i^+|\to0
\quad\text{于 }L^2;
\]

数值 \(1/(2\sqrt6)\) 还需要 \(s_i+4=\operatorname{tr}E_i\to0\)。这正是 \(Q_i\to0\) 中的迹信息。

---

## 6. 截断流后的适用性

对任意时刻 \(t\)，只要 \(g(t)\) 是原闭流形 \(M\) 上的光滑正定度量，则：

1. Chern–Gauss–Bonnet 恒等式成立；
2. monopole 符号类仍是同一组拓扑类；
3. Hodge 正投影虽随 \(t\) 变化，符号平均论证仍逐时成立；
4. 因而 (a)–(d) 全部适用于 \(g(t)\)。

这与 \(g(t)\) 是否满足通常 Ricci 流、截断流或其他演化方程无关。即使方程在 \(\chi=0\) 处不是严格抛物型，静态链条只关心最终得到的度量是否全局光滑且正定。

若最大光滑时间为 \(T\)，链条适用于每个 \(t<T\)。在 \(T\) 时刻若曲率爆破，或度量不再正定，则经典 Chern–Weil 积分、Hodge 投影和 SW 曲率估计不能直接代入。奇异极限还需另行建立相应的测度曲率公式。

更重要的是，静态链条不推出

\[
Q(t)=\int_M|\Ric_{g(t)}+g(t)|^2d\mu_{g(t)}
\]

仍然趋于零。只有在另外得到 \(Q_i(t_i)\to0\) 后，才可对流后度量恢复完整轮廓。

脚本末尾的 `ALL DONE` 没有给出这一演化估计。截断缺陷方程虽对 \(E\) 齐次，但仍含

\[
\int\chi^2|\Rm|\,|E|^2
\]

及梯度、截断函数导数项。齐次性排除了与 \(E\) 无关的加性源，却不能单独推出 \(Q(t)\le C Q(0)\)；还需要局部曲率能量吸收、Sobolev 控制或点态曲率估计。这与 Step 14 所述尚待建立的截断流曲率 bootstrap 一致。

---

## 7. Weyl 模长不能决定特征值

\(W^+\) 是 \(\Lambda^+\) 上迹为零的对称 \(3\times3\) 算子。下面两个谱具有同样的模长平方 \(1/24\)：

\[
\left(-\frac16,\frac1{12},\frac1{12}\right),
\]

以及

\[
\left(\frac1{4\sqrt3},-\frac1{4\sqrt3},0\right).
\]

因此即使 \(|W_i^+|\to1/(2\sqrt6)\) 点态成立，也不能仅由此选出 Step 6 所需谱。

代数上最少还需要最低特征值达到迹零矩阵的极值。若

\[
\lambda_1\le\lambda_2\le\lambda_3,\qquad
\lambda_1+\lambda_2+\lambda_3=0,
\]

则

\[
|W|^2
=\lambda_1^2+\lambda_2^2+\lambda_3^2
\ge\frac32\lambda_1^2,
\]

故

\[
\lambda_1\ge-\sqrt{\frac23}|W|.
\]

等号恰好对应 \(\lambda_2=\lambda_3=-\lambda_1/2\)。在

\[
|W|=\frac1{2\sqrt6}
\]

时即得到

\[
\lambda_1=-\frac16,\qquad
\lambda_2=\lambda_3=\frac1{12}.
\]

等价的单个标量关系是

\[
\det W^+=-\frac{|W^+|^3}{3\sqrt6}.
\]

---

## 8. 到达 Step 6 局部矛盾所需的最少额外数学输入

除 \(Q_i\to0\) 外，需要两类信息，二者缺一不可。

### 8.1 Weyl 代数形状的局部极值信息

一种具体实现是存在自对偶形式 \(H_i\)，在所研究开集上有非零极限，并满足

\[
\frac{\langle W_i^+H_i,H_i\rangle}{|H_i|^2}
+\sqrt{\frac23}|W_i^+|\longrightarrow0.
\]

左端大于等于零；趋于零同时迫使 \(H_i\) 落入最低特征线，并迫使另外两个特征值相等。

这正是 scalar–Weyl 估计证明内部的最低特征值步骤。数值结论 \(K_i\to A\) 本身没有记录 \(H_i\)、其零点集或其局部质量。需要保留选定 monopole 类、SW 解或 harmonic 正投影，并把对应的积分差传到局部。

固定 \(M\) 时符号类只有有限多个，因此可取子列使选定类固定；但 Step 6 中

\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0
\]

这一局部振幅并不是由 (a)–(d) 单独推出的。

### 8.2 一个可传递曲率和形式的光滑正体积开集

一个充分而接近最少的局部输入是：存在固定开集 \(U\) 与坐标拉回，使

\[
g_i\longrightarrow g_\infty
\]

光滑收敛，并且上述 \(H_i\to H_\infty\)、\(|H_\infty|>0\)。此时全局 \(L^2\) 残差在 \(U\) 上也趋于零，从而

\[
\Ric_{g_\infty}=-g_\infty,\qquad
s_\infty=-4,\qquad
|W_\infty^+|=\frac1{2\sqrt6},
\]

而代数极值关系给出

\[
\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Einstein 条件给出 \(\delta W_\infty^+=0\)。Step 6 的常谱投影引理于是给出

\[
\nabla W_\infty^+=0.
\]

另一方面 Einstein–Weyl 恒等式在该谱下为

\[
0=2|\nabla W_\infty^+|^2
+(-4)\frac1{24}
-36\left(-\frac1{864}\right),
\]

即

\[
|\nabla W_\infty^+|^2=\frac1{16},
\]

形成矛盾。

因此，**仅有局部光滑紧性仍不够**，因为同模长可有不同谱；**仅有全局 SW 数值饱和也不够**，因为形式质量可以集中或迁移。真正所需的是“正体积光滑开集 + 非消失 monopole/harmonic 形式 + 最低特征值极值关系”这一局部组合。原始点态 \(\|E_i\|_\infty\to0\) 序列中，带固定体积下界的球与 Cheeger–Naber 正则开集可提供前一部分；流后只有 \(L^2\) 缺陷时，还需平滑曲率估计与局部形式紧性。