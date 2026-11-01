# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step35_unregularized_J6_persistence_lemma.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step32_nested_moser_and_tensor_audit.md",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md"
  ]
}
```

## Task

Independently verify the conditional K2–Y–Moser smoothing layer in the Step 38 note against A01's fixed-exponent and index-level notes and A03's restored state. Check exact Sobolev convention, weights, q=2 absorption, q=3 good-slice propagation, the coefficient S^2Y on dyadic slabs, the p→3p/2 spacetime recurrence, and endpoint scalings ||aF||∞≲γ/t and ||aE||∞≲δ(r²/t)^(1/3). Determine which estimates are genuinely established conditional PDE lemmas and which still depend on unproved moving first-exit, regularized defect general-p, or continuation inputs. Pay special attention to whether the defect high-p inequality follows from the fixed unregularized J6 lemma, and whether any additive regularization source would destroy the δ scaling.

## Output

# 独立科学核验备忘录

## 一、总结果

Step 38 的曲率链
\[
K_2\Longrightarrow Y\Longrightarrow \|aF\|_\infty
\]
在一个预先存在的光滑 first-exit 时间区间上是自洽的。其 Sobolev 系数、权重、\(q=2\) 吸收、\(q=3\) 时间切片传播、\(\mathcal S^2Y\) 系数以及 \(p\mapsto 3p/2\) 迭代都与 A01 Step 34–35、A01 Step 32 和 A03 Step 34 相符。短时间条件应写成
\[
t\lesssim \min\{r^2,1\},
\]
或者在所有公式中保留 \(t^{-1}+r^{-2}+1\)。

缺陷链中，
\[
J_6(t)\lesssim \delta^6V
\]
已经由 A03 Step 35 的无正则化估计和 A01 Step 35 的 Hessian-\(a\) 张量计算支撑；但是它只提供 Moser 迭代的初始指数 \(p_0=6\)。Step 38 的缺陷端点
\[
\|aE(t)\|_\infty\lesssim
\delta (r^2/t)^{1/3}
\]
还需要每个 \(p=6(3/2)^k\) 的缺陷能量不等式。所给文件尚未逐项推导这一一般 \(p\) 公式。Step 38 已经用 “Assume” 明确将其作为额外前提，这是正确的数学定位。

所有这些估计仍依赖移动 Sobolev 比较、支撑域几何和 \(\gamma(t)\) 小量在 first-exit 区间内成立。到指定正时间的流存在性还需要高阶 shifted-curvature/cutoff-jet 延拓论证；Step 38 的 \(m=2\) 修复尚未给出一般 \(m\) 归纳。

---

## 二、Sobolev 约定与吸收参数

正确约定是
\[
\boxed{
\|u\|_4^2\le \mathcal S(t)
\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad
\mathcal S\simeq \frac{r^2}{\sqrt V}.}
\]
因此吸收参数是
\[
\boxed{\gamma(t)=\mathcal S(t)K_2(t)^{1/2},}
\qquad
K_2(t)=\int\eta^2F^2\,d\mu_t.
\]
曲率反应在高指数能量中产生的系数是
\[
\boxed{\mathcal S^2Y,}
\qquad
Y=\int\eta^2aF^3,
\]
而不是再多一个 Sobolev 平方。若采用未平方嵌入常数 \(S\)，则 \(S^2=\mathcal S\)，此时同一系数写成 \(S^4Y\)。

有一个需要精确改写的支撑域问题。A03 Step 35 §5 中若
\(\|F\|_{2,U}^2\le K_2\) 的 \(U\) 表示整个辅助域，这个不等式方向不对，因为 \(\eta\le1\)。实际使用的是
\[
\Omega_a=\operatorname{supp}a,\qquad \eta=1\ \text{于 }\Omega_a,
\]
从而
\[
\|F\|_{L^2(\Omega_a)}^2
=\int_{\Omega_a}\eta^2F^2
\le K_2.
\]
严格缓冲条件因此足以修复所有 \(K_2\)-吸收步骤。

---

## 三、\(q=2\) 吸收与积分 \(Y\) 控制

令
\[
D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2.
\]
A01 Step 35 的 signed Hessian-\(a\) 张量
\[
B_{\mathrm{curv}}^{pq}
=R^p{}_j{}^q{}_lE^{jl},
\quad
|B_{\mathrm{curv}}|\le CF^2,
\quad
|\nabla B_{\mathrm{curv}}|
\le CF|\nabla\operatorname{Rm}|
\]
正好提供 \(q=2\) 能量所需的积分分部结构。原始不等式应写成
\[
K_2'+cD_2
\le CY+C(r^{-2}+1)K_2.
\]
当 \(r\le1\) 时，常数项可并入 \(r^{-2}\)。

取
\[
v=\chi F.
\]
由于 \(\eta=1\) 于活跃支撑域，
\[
Y=\int Fv^2
\le \|F\|_{L^2(\Omega_a)}\|v\|_4^2.
\]
而
\[
\|\nabla(\chi F)\|_2^2
\le C D_2+Cr^{-2}K_2.
\]
所以
\[
\boxed{
Y\le C\gamma(t)(D_2+r^{-2}K_2).}
\]
若 first-exit 假设给出
\(\gamma(t)\le\gamma_0\) 且 \(C\gamma_0<c/2\)，则
\[
K_2'+\frac c2D_2
\le C(r^{-2}+1)K_2.
\]
在 \(t\lesssim\min\{r^2,1\}\) 上，
\[
\sup_{s\le t}K_2(s)+\int_0^tD_2(s)\,ds
\le CK_2(0),
\]
并进一步得到
\[
\boxed{
\int_0^tY(s)\,ds
\le C\gamma_*K_2(0),}
\]
其中 \(\gamma_*=\sup_{s\le t}\mathcal S(s)K_2(s)^{1/2}\)。这与 Step 38 (4.3)–(4.5) 一致。

---

## 四、\(q=3\) 时间切片传播

令
\[
D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2.
\]
未经反应吸收的固定 \(q=3\) 公式为
\[
Y'+cD_3
\le C(r^{-2}+1)Y
+C\int\eta^2a^2F^4.
\]
取
\[
u=aF^{3/2}.
\]
则
\[
\int a^2F^4=\int Fu^2
\le \|F\|_{L^2(\Omega_a)}\|u\|_4^2.
\]
同时
\[
|\nabla(aF^{3/2})|^2
\le Ca^2F|\nabla F|^2+C|da|^2F^3
\le C\,D_3+Cr^{-2}aF^3.
\]
故
\[
\boxed{
\int a^2F^4
\le C\gamma_*(D_3+r^{-2}Y).}
\]
在同一小量条件下，
\[
Y'\le C(r^{-2}+1)Y.
\]

由 \(\int_0^tY\le C\gamma_*K_2(0)\)，存在
\(s\in[t/4,t/2]\) 使
\[
Y(s)\le \frac{C\gamma_*K_2(0)}t.
\]
传播到 \(t\) 得
\[
\boxed{
Y(t)\le\frac{C\gamma_*K_2(0)}t.}
\]
若
\[
\mathcal S_*=\sup_{[0,t]}\mathcal S(s),\qquad
K_{2,*}=\sup_{[0,t]}K_2(s),\qquad
\gamma_*=\mathcal S_*K_{2,*}^{1/2},
\]
则 \(K_2(0)\le K_{2,*}\)，从而
\[
\boxed{
\mathcal S(t)^2Y(t)
\le\frac{C\gamma_*^3}{t}.}
\]
Step 38 中不带星号的 \(\gamma\) 应理解为这个 first-exit 上确界，或与初始 \(\gamma(0)\) 可比的统一参数。

A01 Step 34 还给出了另一种传播：
\[
Y'\le C(r^{-2}+1+\mathcal S^2Y)Y
\]
配合
\(\int\mathcal S^2Y\le C\gamma^3\) 做 Gronwall。它与上述两因子 \(q=3\) 吸收兼容；Step 38 使用的是更直接的一种。

---

## 五、高指数曲率不等式与 \(p\mapsto3p/2\)

A01 Step 35 已逐项给出曲率 Hessian-\(a\) 张量及其导数估计，并得到
\[
\boxed{
K_p'
+c\{pD_p^{\mathrm{Rm}}+p(p-2)D_p^F\}
\le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p,
\quad p\ge3.}
\]
这里保留两种耗散是必要的：

- \(\nabla B_{\mathrm{curv}}\) 由 \(D_p^{\mathrm{Rm}}\) 支付；
- \(\nabla F^{p-2}\) 由 \(D_p^F\) 支付。

这也确认 Step 38 (4.2) 使用 \(p(p-2)\)，而不是旧稿中的 \(p(p-3)\)。

定义
\[
H_p(f)=\int\eta^2a^{p-2}f^p,
\qquad
z_p=\eta a^{(p-1)/2}f^{p/2}.
\]
因为 \(\eta=1\) 于 \(a>0\) 的区域，权重恒等式严格成立：
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2.
\]
于是
\[
\boxed{
H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2.}
\]

在嵌套时间区间上，令
\[
A_k=\int_{I_k}H_{p_k},\qquad
p_{k+1}=\frac32p_k.
\]
由时间截断能量和 Sobolev 不等式，
\[
A_{k+1}
\le Cp_k^N\mathcal S_*
\bigl(L_kA_k\bigr)^{3/2},
\]
其中更精确地
\[
L_k\le Cp_k^N
\left(\frac{4^k}{t}+r^{-2}+1+\frac{\gamma_*^3}{t}\right).
\]
若 \(\gamma_*\le\gamma_0\) 且
\(t\lesssim\min\{r^2,1\}\)，则
\[
L_k\le Cp_k^N4^kt^{-1}.
\]
指数和为
\[
\sum_{k\ge0}\frac1{p_{k+1}}=\frac2{p_0},
\qquad
\frac32\sum_{k\ge0}\frac1{p_{k+1}}=\frac3{p_0}.
\]
因此
\[
\boxed{
\|af(t)\|_\infty
\le C\mathcal S_*^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^tH_{p_0}(f,s)\,ds\right)^{1/p_0}.}
\]
不采用短时间简化时，\(t^{-3/p_0}\) 应替换为
\[
(t^{-1}+r^{-2}+1)^{3/p_0}.
\]

---

## 六、两个端点的尺度计算

### 1. 曲率

取 \(p_0=3\)，并使用
\[
\int_{t/2}^tY(s)\,ds
\le C\gamma_*K_2(0).
\]
则
\[
\|aF(t)\|_\infty
\le C\mathcal S_*^{2/3}t^{-1}
(\gamma_*K_2(0))^{1/3}.
\]
在 first-exit 比较下，
\[
\mathcal S_*^{2/3}
(\gamma_*K_2(0))^{1/3}
\le C\mathcal S_*K_{2,*}^{1/2}
=C\gamma_*.
\]
所以
\[
\boxed{\|aF(t)\|_\infty\le C\gamma_*/t.}
\]
该尺度与 Step 38 (5.5) 完全一致。

### 2. 缺陷

若一般 \(p\) 缺陷能量公式可用，取 \(p_0=6\)。固定指数引理给出
\[
J_6(s)\le C\delta^6V,
\]
故
\[
\int_{t/2}^tJ_6(s)\,ds
\le Ct\delta^6V.
\]
代入 Moser 公式：
\[
\begin{aligned}
\|aE(t)\|_\infty
&\le C\mathcal S_*^{1/3}t^{-1/2}
(t\delta^6V)^{1/6}\\
&=C\delta\,\mathcal S_*^{1/3}V^{1/6}t^{-1/3}\\
&\le C\delta(r^2/t)^{1/3}.
\end{aligned}
\]
这里使用
\(\mathcal S_*\lesssim r^2V^{-1/2}\)，其移动版本依赖体积和度量比较。时间积分为
\[
\boxed{
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.}
\]

---

## 七、固定 \(J_6\) 与一般 \(p\) 缺陷公式不是同一件事

A03 Step 35 与 A01 Step 35 已支撑
\[
J_6'+cX_6
\le C(1+r^{-2})J_6+CP_6,
\]
以及
\[
P_6\le C\gamma(X_6+r^{-2}J_6),
\]
从而
\[
\boxed{
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).}
\]
这是可靠的固定指数引理。A03 Step 35 (3.6a) 中的 \(s^{3/2}\) 是文字幂次不一致；其前后计算和 A01 Step 34 均使用正确的
\[
a^4|da|s^{5/2}|\nabla E|.
\]

但是 Moser 迭代还需要 \(p=9,13.5,\ldots\) 的能量公式。\(p=6\) 的 Gronwall 估计本身不能产生这些公式。所需形式是
\[
(H_p^E)'
+c\|\nabla z_p^E\|_2^2
\le Cp^N(r^{-2}+1+\mathcal S^2Y)H_p^E,
\]
且右端没有与 \(E\) 无关的加法项。

一个自然的无正则化路线是
\[
H_p^E=\int\eta^2a^{p-2}s^{p/2},
\qquad
z_p^E=\eta a^{(p-1)/2}s^{p/4},
\qquad s=|E|^2.
\]
沿 Moser 指数列始终有 \(p\ge6\)，所以
\(E\mapsto |E|^p\) 至少为 \(C^2\)，而 \(z_p^E\) 至少为 \(C^1\)。链式法则
\[
(\partial_t-a\Delta)s^{p/2}
=\frac p2s^{p/2-1}(\partial_t-a\Delta)s
-a\frac p2\left(\frac p2-1\right)
s^{p/2-2}|\nabla s|^2
\]
在 \(E=0\) 处没有奇性。A01 Step 35 的
\[
B_{\mathrm{def}}^{ij}
=s g^{ij}+(\operatorname{tr}E)E^{ij}
-2(E^2)^{ij}
\]
满足
\[
|B_{\mathrm{def}}|\le Cs,\qquad
|\nabla B_{\mathrm{def}}|
\le Cs^{1/2}|\nabla E|,
\]
所以一般 \(p\) 的 Hessian-\(a\) 项也具有正确的齐次权重。反应项则可用
\[
a^{p-1}F|E|^p
=(aF^3)^{1/3}
(a^{p-2}|E|^p)^{1/3}
(z_p^E)^{4/3}
\]
产生 \(\mathcal S^2Y\) 系数。这个路线在结构上完整，但所给文件尚未把所有一阶 cutoff、移动张量范数和体积项逐项写成一般 \(p\) 证明。

---

## 八、加法正则化源对 \(\delta\) 尺度的影响

A01 Step 33 曾显示带 \(C_0'p\) 的正则化公式；后续文件已将固定 \(J_6\) 改成无正则化证明。该旧公式不能直接用于缺陷端点。

若
\[
J_{6,\varepsilon}'\le LJ_{6,\varepsilon}
+A_{6,\varepsilon}
\]
中的 \(A_{6,\varepsilon}\) 在 \(\varepsilon\to0\) 后仍留下与 \(\delta\) 无关的量，则
\[
J_6(t)\lesssim
\delta^6V+\int_0^tA_6(s)\,ds.
\]
Moser 端点相应包含
\[
\mathcal S^{1/3}t^{-1/2}
\left[t\delta^6V+
t\int_0^tA_6(s)\,ds\right]^{1/6},
\]
第二项不与 \(\delta\) 成正比。因此
\(\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}\)
不再随 \(\delta\to0\) 消失。

这也与精确模型一致：\(E=0\) 时流速度为零，缺陷能量应保持为零。任何在正则化极限后仍存在的加法源都是正则化产物。一般 \(p\) 证明需要无加法源，或者证明所有 \(\varepsilon\)-项在每个迭代指数上以足够统一的估计趋于零。

---

## 九、各数学对象的当前支撑程度

| 数学对象 | 所给材料中的支撑 |
|---|---|
| Sobolev 约定、\(\gamma=\mathcal SK_2^{1/2}\)、体积消去 | 已逐项成立 |
| 曲率 Hessian-\(a\) 张量和一般 \(p\) 曲率能量 | A01 Step 35 已给出 index-level 推导 |
| \(q=2\) 吸收、\(K_2\) 持续、\(\int Y\) 控制 | 在光滑 first-exit 区间上成立 |
| \(q=3\) good-slice 传播与 \(\mathcal S^2Y\lesssim\gamma^3/t\) | 在同一区间上成立；需保留 \(+1\) 或假设 \(r,t\) 小 |
| \(p\mapsto3p/2\) 时空迭代及时间幂 | A01 Step 32 与 Step 38 一致 |
| \(\|aF\|_\infty\lesssim\gamma/t\) | 条件性曲率 PDE 结论 |
| 无正则化 \(J_6\lesssim\delta^6V\) | A03 Step 35 与 A01 Step 35 支撑 |
| 一般 \(p\) 缺陷能量 | Step 38 中仍是额外假设 |
| \(\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}\) | 依赖上一行的一般 \(p\) 公式 |
| 移动 first-exit 自我改进 | 尚无完整组合证明 |
| 到指定时间的光滑存在与延拓 | 一般高阶 cutoff-jet 归纳尚未完成 |

因此，Step 38 的曲率 K2–Y–Moser 层已经构成可靠的条件性 PDE 模块；缺陷端点的尺度代数正确，但其一般 \(p\) 能量输入仍需独立张量推导。即使这些局部流公式全部补齐，它们处理的仍是四维 \(E=\operatorname{Ric}+g\) 的 Ishida–LeBrun 实验模型，而不是原题的全维结论。