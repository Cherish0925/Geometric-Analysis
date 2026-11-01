# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step37_base_pair_continuation.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently verify the proposed m=2 coupled continuation mechanism in step40_m2_coupled_continuation_mechanism.md for the normalized cutoff flow. Focus on the exact hard residual: V=∇²U, Z=∇³χ, W=∇U, Θ=∇²χ, and I=∫χ Z*W*|V|^{p-2}V. Check whether integrating once more off Z really yields only (i) a signed χΘ*V*P(V) term amenable to the Step 38 Hessian lemma, (ii) a weighted-dissipation term with coefficient ΘW controlled from the m=1 base pair at finite exponents, and (iii) lower products—without hidden current-level Z at 2p or W in L∞. Check tensor/covariant-derivative commutators and whether the Γ1, Γ2, Γ3 coefficients/contractions can be grouped this way rather than merely schematically. Also verify the Z evolution derivative count and same-p closure. Identify precisely any remaining term that invalidates the displayed m=2 Grönwall inequality. Treat the note as a mathematical proposal, not as established.

## Output

# 独立复核备忘：\(m=2\) 耦合延拓机制

## 结论摘要

在以下量均为时间一致的有限上界时，

\[
\|U\|_\infty,\qquad
\|W\|_{L^q},\qquad
\|\Theta\|_{L^q},\qquad
\|T\|_{L^q},\qquad
\|\nabla T\|_{L^q},
\]

其中所需 \(q\) 至少包含 \(2p,4p\)，Step 40 对硬项

\[
I=\int_M \chi\,Z*W*P(V)\,d\mu,
\qquad
P(V)=|V|^{p-2}V
\]

的二次分部积分是正确的。它逐个张量收缩地产生：

1. \(\chi\Theta*V*P(V)\)，可直接应用 Step 38 的 Hessian 分部积分；
2. \(\chi\Theta*W*\nabla P(V)\)，由 \(D_{2,p}\) 与 \(W,\Theta\) 的有限高指数范数控制；
3. \(d\chi*\Theta*W*P(V)\)，仅含前一级量。

此过程不需要 \(Z\in L^{2p}\)，也不需要 \(W\in L^\infty\)。\(Z=\nabla^3\chi\) 的演化确实只含当前项 \(V*d\chi\)、\(W*\Theta\)，再加上度量范数变化给出的 \(U*Z\)，因而在同一个指数 \(p\) 闭合。

在 Step 40 已明确假定 \(\nabla T\) 的时间一致有限 \(L^q\) 上界时，没有发现额外项破坏

\[
Y_{2,p}'\le C_p(1+Y_{2,p}).
\]

若只从 \(\sup|U|\) 和 \(m=1\) 对 \((W,\Theta)\) 的估计出发，则尚不能得到该式；具体剩余量是 \(V\)-方程中的

\[
aW*\nabla T,\qquad
\nabla a*U*\nabla T,
\]

以及采用导数换序时可能出现的 \(\nabla T*d\chi*U\)。这正是文中假设 (1.1) 所承担的内容。

---

## 1. 硬项的逐收缩分部积分

固定任意一个由 \(g,g^{-1}\) 构成的平行收缩 \(\mathcal C\)。不需要把 \(Z\) 看成完全对称张量；取实际迭代次序

\[
Z_{abc}=\nabla_a\Theta_{bc},
\qquad
\Theta_{bc}=\nabla_b\nabla_c\chi .
\]

相应积分可写成

\[
I_{\mathcal C}
=\int_M\chi\,(\nabla_a\Theta_{bc})
 \,\mathcal C^{abc}(W,P(V))\,d\mu .
\]

由于 \(\nabla g=\nabla g^{-1}=0\)，导数不会产生收缩系数的空间导数。散度积分给出

\[
\begin{aligned}
I_{\mathcal C}
={}&-\int_M(\nabla_a\chi)\Theta_{bc}
       \mathcal C^{abc}(W,P(V))\,d\mu\\
&-\int_M\chi\Theta_{bc}
       \mathcal C^{abc}(\nabla_aW,P(V))\,d\mu\\
&-\int_M\chi\Theta_{bc}
       \mathcal C^{abc}(W,\nabla_aP(V))\,d\mu .
\end{aligned}
\tag{1}
\]

这对每个实际收缩分别成立，不依赖不同 \(\Gamma_i\) 之间的系数抵消。

### 1.1 导数落在 \(W\) 上

按照有序协变导数定义，\(\nabla W\) 就是 \(V=\nabla^2U\)。因此第二项具有形式

\[
J=\int_M\chi\,\Theta_{bc}B^{bc}(V)\,d\mu ,
\]

其中

\[
|B(V)|\le C_p|V|^p,\qquad
|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]

即使 \(B^{bc}\) 不对称也没有影响，因为 \(\Theta_{bc}\) 自动只收缩其对称部分。Step 38 的计算逐字适用：

\[
\begin{aligned}
J
={}&-\int_M\nabla_b\chi\,\nabla_c\chi\,B^{bc}\,d\mu
-\int_M\chi\,\nabla_c\chi\,\nabla_bB^{bc}\,d\mu ,
\end{aligned}
\]

从而

\[
|J|
\le \varepsilon D_{2,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p .
\tag{2}
\]

若为了统一下标次序而交换 \(\nabla_aW\) 的导数，则会增加
\(\operatorname{Rm}*U\)。对应积分至多为

\[
C\int |\Theta|\,|T|\,|U|\,|V|^{p-1},
\]

由 \(U\in L^\infty\)、\(\Theta,T\in L^{2p}\) 控制，不产生新的 \(Z\)。

### 1.2 导数落在 \(P(V)\) 上

正则化为

\[
P_\epsilon(V)
=(|V|^2+\epsilon^2)^{(p-2)/2}V
\]

后，有一致估计

\[
|\nabla P_\epsilon(V)|
\le C_p(|V|^2+\epsilon^2)^{(p-2)/2}|\nabla V|.
\]

令 \(\epsilon\downarrow0\) 即得

\[
\begin{aligned}
\int\chi|\Theta||W||V|^{p-2}|\nabla V|
&\le \varepsilon D_{2,p}
+C_{p,\varepsilon}
 \int|\Theta|^2|W|^2|V|^{p-2}.
\end{aligned}
\tag{3}
\]

Hölder 指数完全匹配：

\[
\begin{aligned}
\int|\Theta|^2|W|^2|V|^{p-2}
&\le
\operatorname{Vol}(M,g(t))^{1/p}
\|\Theta\|_{4p}^2\|W\|_{4p}^2
\|V\|_p^{p-2}\\
&\le C_{p,W,\Theta}(1+\|V\|_p^p).
\end{aligned}
\tag{4}
\]

这里倒数指数之和为

\[
\frac1{2p}+\frac1{2p}+\frac{p-2}{p}
=\frac{p-1}{p},
\]

剩余 \(1/p\) 由体积因子承担。该估计与维数无关，只需体积一致有界。

### 1.3 导数落在显式 \(\chi\) 上

第一项满足

\[
\begin{aligned}
\int |d\chi|\,|\Theta|\,|W|\,|V|^{p-1}
&\le
\|d\chi\|_\infty
\|\Theta\|_{2p}\|W\|_{2p}\|V\|_p^{p-1}\\
&\le C_p(1+\|V\|_p^p).
\end{aligned}
\tag{5}
\]

因此对每个收缩都有

\[
|I_{\mathcal C}|
\le \varepsilon D_{2,p}
+C_p(1+\|V\|_p^p),
\tag{6}
\]

且右侧不含任何 \(Z\) 范数。

---

## 2. \(\Gamma_1,\Gamma_2,\Gamma_3\) 的张量结构

由所给 \(U\)-方程的高 cutoff 行

\[
\nabla^\alpha\chi*\nabla^\beta\chi*
\nabla^\gamma U,
\qquad
\alpha+\beta+\gamma=4,\quad \gamma\le3,
\]

在 \(m=2\) 时所有不同导数分配恰为

\[
\begin{gathered}
\chi\nabla^4\chi*U,\quad
d\chi*Z*U,\quad
\chi Z*W,\\
\Theta*\Theta*U,\quad
d\chi*\Theta*W,\quad
\chi\Theta*V,\\
d\chi*d\chi*V,\quad
\chi d\chi*\nabla V .
\end{gathered}
\tag{7}
\]

这与 Wang 论文 Proposition 4.14 所列四个最高阶项及其唯一残余
\(\nabla^2\chi*\nabla^m\chi*U\) 一致；当 \(m=2\) 时该残余就是
\(\Theta*\Theta*U\)。

对 \(\Gamma_1\)，逐收缩写成

\[
\int\chi\,\mathcal D(\nabla Z,U,P(V)).
\]

一次分部积分严格产生

\[
d\chi*Z*U*P(V),\qquad
\chi Z*W*P(V),\qquad
\chi Z*U*\nabla P(V).
\tag{8}
\]

因此：

- 第一类与原始 \(\Gamma_2\) 同型，以 \(Z\in L^p\) 控制；
- 第二类正是上节处理的硬项；
- 第三类由
  \[
  \varepsilon D_{2,p}
  +C K^2\int |Z|^2|V|^{p-2}
  \]
  控制，而
  \[
  |Z|^2|V|^{p-2}
  \le C_p(|Z|^p+|V|^p).
  \]

这里同样不使用不同项之间的消去。数值系数只改变 \(C_p\)。

其余四类由

\[
\|\Theta\|_{2p},\quad \|W\|_{2p},\quad \|U\|_\infty
\]

与式 (2) 控制。例如

\[
\int |\Theta|^2|U||V|^{p-1}
\le K\|\Theta\|_{2p}^2\|V\|_p^{p-1}.
\]

所以高 cutoff 行确实给出

\[
\left|\int P(V)*\mathcal H_2\right|
\le \varepsilon D_{2,p}
+C_p(1+\|V\|_p^p+\|Z\|_p^p).
\tag{9}
\]

---

## 3. 协变导数换序

该论证无需把 \(\nabla^3\chi\) 或 \(\nabla^4\chi\) 完全对称化。直接保留实际迭代次序即可避免换序项。

若书写过程中进行换序，则有

\[
[\nabla_i,\nabla_j]\,d\chi
=\operatorname{Rm}*d\chi,
\]

而四阶导数换序产生

\[
\operatorname{Rm}*\Theta,
\qquad
\nabla\operatorname{Rm}*d\chi .
\]

由于

\[
\operatorname{Rm}=T-G,\qquad \nabla\operatorname{Rm}=\nabla T,
\]

这些项只要求 \(T,\nabla T\) 的有限 \(L^q\) 上界。典型被积式为

\[
|T|\,|\Theta|\,|U|\,|V|^{p-1},
\qquad
|\nabla T|\,|d\chi|\,|U|\,|V|^{p-1},
\]

仍然没有 \(Z\in L^{2p}\) 或 \(W\in L^\infty\) 的需求。

---

## 4. \(Z\) 演化的精确导数计数

令

\[
C^k{}_{ij}=\partial_t\Gamma^k{}_{ij}.
\]

由于

\[
\Theta_{ij}=\nabla_i\nabla_j\chi,
\qquad
\partial_t\Theta_{ij}=-C^k{}_{ij}\nabla_k\chi,
\]

以及 \(Z_{\ell ij}=\nabla_\ell\Theta_{ij}\)，直接计算得

\[
\begin{aligned}
\partial_tZ_{\ell ij}
={}&-(\nabla_\ell C^k{}_{ij})\nabla_k\chi
-C^k{}_{ij}\Theta_{\ell k}\\
&-C^k{}_{\ell i}\Theta_{kj}
-C^k{}_{\ell j}\Theta_{ik}.
\end{aligned}
\tag{10}
\]

另一方面，

\[
\partial_tg=-2\operatorname{Ric}(U)
\]

给出

\[
C=g^{-1}*\nabla\operatorname{Ric}(U),
\]

故

\[
|C|\le C|W|,
\qquad
|\nabla C|\le C|V|.
\tag{11}
\]

因此张量演化本身满足

\[
|\partial_tZ|
\le C\bigl(|V||d\chi|+|W||\Theta|\bigr).
\tag{12}
\]

度量范数和体积形式的时间变化由 \(|U|\le K\) 控制，贡献
\(CK\int|Z|^p\)。于是

\[
\begin{aligned}
\frac d{dt}\|Z\|_p^p
\le{}& C_pK\|Z\|_p^p
+C_p\|V\|_p\|Z\|_p^{p-1}\\
&+C_p\|W\|_{2p}\|\Theta\|_{2p}\|Z\|_p^{p-1},
\end{aligned}
\]

从而

\[
\frac d{dt}\|Z\|_p^p
\le C_p(1+\|V\|_p^p+\|Z\|_p^p).
\tag{13}
\]

导数计数与同指数闭合均正确。

---

## 5. \(V\)-方程中真正依赖 \(\nabla T\) 的项

除高 cutoff 行外，\(m=2\) 方程中的混合项具有

\[
\nabla^i a*\nabla^jU*\nabla^kT,
\qquad i+j+k=2,\quad k\le1.
\]

其中含 \(\nabla T\) 的两种分配是

\[
aW*\nabla T,\qquad
\nabla a*U*\nabla T.
\tag{14}
\]

测试后分别产生

\[
\int a|\nabla T||W||V|^{p-1},
\qquad
\int |\nabla a||U||\nabla T||V|^{p-1}.
\tag{15}
\]

在

\[
\sup_{t<T}\|\nabla T(t)\|_{2p}<\infty
\]

时，它们由 Hölder–Young 给出 \(C(1+\|V\|_p^p)\)。其余混合项只含
\(T,W,\Theta,U\)，而可能乘在 \(V\) 上的 \(aT\) 正好等于 \(U\)，所以不会形成未加权 \(T|V|^p\)。

故在 Step 40 的全部先验输入均为时间一致上界时，

\[
\frac d{dt}\|V\|_p^p+cD_{2,p}
\le C_p(1+\|V\|_p^p+\|Z\|_p^p)
\tag{16}
\]

与式 (13) 相加，确实得到

\[
Y_{2,p}'\le C_p(1+Y_{2,p}).
\tag{17}
\]

## 科学状态

硬残余 \(I\) 的机制成立，而且比直接 Hölder 路线更强：二次分部积分后 \(Z\) 从该项中完全消失。当前尚缺的数学内容不是另一个 \(m=2\) 高 cutoff 项，而是归一化流下 \(\nabla T\) 的独立积分估计及其时间一致常数。Wang Proposition 4.13 提供了未归一化情形的结构依据；所给材料尚未写出其归一化 shifted-curvature 版本的完整推导。