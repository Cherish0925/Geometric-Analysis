# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 17,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step17_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step17_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following claim about the normalized cutoff flow ∂_t g = -2χ²(Ric + g) on a closed 4-manifold. The Einstein defect E = Ric + g satisfies ∂_t E = a(Δ_L E - 2E) + C_a(E) where a = χ². The claim is that |E|² satisfies a scalar parabolic inequality where the reaction term has NO quadratic-in-|E|² loss independent of δ. Specifically: (1) In the Lichnerowicz contribution to ∂_t|E|², the -4a·Ric(E,E) - 4a|E|² terms combine to -4a·tr(E³), because Ric = E - g gives Ric(E,E) = tr(E³) - |E|², and the ±4a|E|² cancel exactly. (2) Therefore the full reaction at a maximum point is bounded by C(|Rm| + δ + r⁻²)|E|², where δ = ||E||_∞. (3) The resulting Gronwall gives ||E(t)||_∞ ≤ √2·δ for t ≤ θr² with θ = O(1/(K₀r² + 1)), which is an a priori bound requiring NO curvature-bootstrap output. (4) This breaks the continuation circle because metric equivalence follows directly from the defect bound: |∂_t log|v|²| ≤ 2|E| ≤ 2√2·δ. Check each step for mathematical correctness, paying special attention to: the sign of the Lichnerowicz Laplacian convention, whether the maximum principle applies to the degenerate equation (a = 0 boundary), and whether the cubic term 4a|tr(E³)| ≤ 4a|E|³ ≤ 8aδ|E|² is correctly bounded.

## Integrated Scientific Memo

## 核验结论

该主张**不能按原文成立**。关键修正有两点：

1. Step 17 漏掉了随时间变化的逆度量对 \(\partial_t|E|^2\) 的贡献。加入后，所谓残余三次项 \(-4a\operatorname{tr}(E^3)\) **完全消失**。
2. 最大值原理仍含有演化时刻的 \(a|\Rm(g(t))|\) 和 \(|\nabla^2_{g(t)}a|\)。它们不能由初始曲率 \(K_0\) 和双线性度量等价自动控制。因此声称无需任何曲率 bootstrap 即得到给定生存时间，是不成立的。

### 1. 正确的标量演化式

采用
\[
\Delta=\nabla^k\nabla_k,\qquad
(\Delta_LE)_{ij}
=\Delta E_{ij}+2R_{ikjl}E_{kl}
-\Ric_i{}^kE_{kj}-\Ric_j{}^kE_{ki}.
\]
此时标量函数在空间最大点满足 \(\Delta f\le0\)，并且
\[
2\langle E,\Delta_LE\rangle
=\Delta|E|^2-2|\nabla E|^2
+4\Rm(E,E)-4\Ric(E,E).
\]

在
\[
\partial_tg=-2aE,\qquad
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
\]
下，不能只写
\[
\partial_t|E|^2=2\langle E,\partial_tE\rangle.
\]
因为
\[
\partial_tg^{ij}=2aE^{ij},
\]
两个逆度量因子的变化额外贡献
\[
\left.\partial_t|E|^2\right|_{g^{-1}}
=4a\tr(E^3).
\]

另一方面，
\[
\Ric=E-g,\qquad
\Ric(E,E)=\tr(E^3)-|E|^2,
\]
所以来自 \(2\langle E,\partial_tE\rangle\) 的相关项为
\[
-4a\Ric(E,E)-4a|E|^2=-4a\tr(E^3).
\]
它与逆度量贡献 \(+4a\tr(E^3)\) 完全抵消。因此正确恒等式是
\[
\boxed{
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2
+4a\Rm(E,E)
+2\langle E,\mathcal C_a(E)\rangle .
}
\]
这正是 Step 14 已记录的恒等式；Step 17 与脚本中的残余三次项来自遗漏逆度量变化。

故问题中的第 (1) 步：

- \(\pm4a|E|^2\) 的确抵消；
- 但最终并不剩下 \(-4a\tr(E^3)\)；
- 完整标量演化中的三次项为零。

独立地，
\[
|\tr(E^3)|\le |E|^3
\]
以及在 \(|E|\le2\delta\) 时
\[
4a|\tr(E^3)|\le8a\delta |E|^2
\]
本身都正确，但对正确的完整演化式没有必要。

### 2. 截断项和实际反应界

由给出的 \(\mathcal C_a(E)\) 公式及四维估计
\[
|\tr E|\le2|E|,\qquad |\nabla\tr E|\le2|\nabla E|,
\]
对任意 \(\varepsilon>0\)，在 \(a>0\) 上有
\[
|2\langle E,\mathcal C_a(E)\rangle|
\le
\varepsilon a|\nabla E|^2+
C_\varepsilon\left(
|\nabla^2a|+\frac{|\nabla a|^2}{a}
\right)|E|^2.
\]
对 \(a=\chi^2\)，
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,\qquad
\nabla^2a=2\chi\nabla^2\chi+2\,d\chi\otimes d\chi.
\]
吸收梯度项后，
\[
\boxed{
(\partial_t-a\Delta)|E|^2
\le
C\left(
a|\Rm|
+|\nabla^2a|
+\frac{|\nabla a|^2}{a}
\right)|E|^2 .
}
\]
若在整个时间区间另有
\[
|\nabla\chi|_{g(t)}\le Cr^{-1},\qquad
|\nabla^2_{g(t)}\chi|\le Cr^{-2},
\]
才可简化为
\[
(\partial_t-a\Delta)|E|^2
\le C(a|\Rm|+r^{-2})|E|^2.
\]

因此第 (2) 步在形式上可加强为“不含 \(\delta\) 项”，但必须保留：

- 演化时刻的 \(a|\Rm(g(t))|\)；
- 演化联络下的 \(|\nabla^2_{g(t)}a|\)。

仅有 \(g(t)\) 与 \(g_0\) 的双线性等价并不能控制后二者，因为曲率依赖二阶空间导数，而 \(\nabla^2_{g(t)}a\) 依赖 Christoffel 符号。

### 3. 退化最大值原理

对已存在的光滑解，令
\[
U(t)=\max_M|E(\cdot,t)|^2.
\]
一致抛物性不是这个点态最大值论证所必需的：在最大点，
\[
\Delta|E|^2\le0,\qquad a\ge0,
\]
故 \(a\Delta|E|^2\le0\)。上 Dini 导数满足
\[
D^+U(t)\le B(t)U(t),
\]
其中
\[
B(t)=C\left[
\|a\Rm(g(t))\|_\infty+
\left\|
|\nabla^2a|+\frac{|\nabla a|^2}{a}
\right\|_\infty
\right].
\]
商 \(|\nabla a|^2/a\) 对 \(a=\chi^2\) 以 \(4|\nabla\chi|^2\) 有界延拓至零集。

若采用标准非负光滑截断 \(0\le\chi\le1\)，则 \(\chi=0\) 处 \(d\chi=0\)，从而
\[
a=da=\nabla^2a=0,
\]
故该处度量及 \(E\) 均冻结。即使不单独使用“冻结”论证，上述 Dini 最大值论证仍适用于 \(a\ge0\) 的退化标量不等式。这里的结论是**给定光滑解后的先验估计**；它本身不证明退化流的短时存在和所需正则性。

### 4. Gronwall 步骤的准确范围

正确结论是
\[
\|E(t)\|_\infty^2
\le \|E(0)\|_\infty^2
\exp\!\left(\int_0^tB(s)\,ds\right).
\]
若额外已知整个时间区间内
\[
\|a\Rm(g(t))\|_\infty\le K,\qquad
|\nabla^2a|+\frac{|\nabla a|^2}{a}\le Cr^{-2},
\]
则
\[
t\le \frac{r^2\log2}{C(Kr^2+1)}
\]
确实给出
\[
\|E(t)\|_\infty\le\sqrt2\,\|E(0)\|_\infty.
\]

但不能直接把 \(K\) 换成
\[
K_0=\sup_{\operatorname{supp}\chi}|\Rm(g_0)|.
\]
“小的度量漂移”只控制零阶双线性形式，不控制 \(\Rm(g(t))\) 或 \(\nabla^2_{g(t)}a\)。而且最大函数给出的局部归一化 \(L^2\) 曲率小量也不自动给出截断支集上的点态 \(K_0\)。

故第 (3) 步原文错误：该 \(\sqrt2\delta\) 界仍需要时空曲率及演化截断 Hessian 的控制。最大值原理消除了人为的 \(O(\delta)\) 三次反应，却没有消除 \(a|\Rm|\) 势项。尚未闭合的精确对象仍是 transition region 的曲率传播，以及由此获得的
\[
\int_0^T\bigl(\|a\Rm\|_\infty+\|\nabla^2a\|_\infty\bigr)\,dt
\]
控制。

### 5. 度量等价

一旦缺陷界已经获得，第 (4) 步正确。对固定 \(v\neq0\)，
\[
\left|\partial_t\log g_t(v,v)\right|
=
2a\,\frac{|E(v,v)|}{g_t(v,v)}
\le2\|E(t)\|_\infty.
\]
于是若 \(\|E(t)\|_\infty\le\sqrt2\,\delta\)，则
\[
e^{-2\sqrt2\delta t}g_0
\le g(t)\le
e^{2\sqrt2\delta t}g_0.
\]
这确实仅由缺陷界推出，不再需要曲率输出；但缺陷界本身尚未在无曲率输入的条件下证明。

## 最终判定

- **(1) 错误但可加强修正**：完整计算中三次项完全抵消，而非残留 \(-4a\tr(E^3)\)。
- **(2) 条件正确且更强**：无 \(\delta\) 反应损失，但仍含 \(a|\Rm(g(t))|\) 和 \(|\nabla^2_{g(t)}a|\)。
- **退化最大值原理可用**：前提是已有足够光滑的解；退化不妨碍点态 Dini 最大值论证。
- **(3) 原文不成立**：仅凭初始 \(K_0\) 和度量小漂移不能得到所宣称时间；仍需 transition-region 曲率/Hessian 控制。
- **(4) 正确但有条件**：给定缺陷界后，度量等价直接成立。

因此，该机制只打破了“缺陷界 \(\Rightarrow\) 度量等价”这一环中的反向依赖，并未消除最大值估计对演化曲率控制的依赖，故尚未真正闭合 continuation circle。