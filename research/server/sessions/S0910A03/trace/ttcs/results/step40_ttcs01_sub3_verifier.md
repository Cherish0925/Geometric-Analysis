# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step27_shifted_curvature_continuation_analysis.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step37_continuation_theorem_and_first_exit.md",
    "Sessions/S0910A01/trace/ttcs/results/step37_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the independent unweighted shifted-curvature derivative ordering needed before the m=2 pair. Determine whether ∇T∈L^q for all finite q follows from the actual T equation under |U| bounded, the m=1 base pair (∇U,∇²χ) finite in all L^q, and T finite in all L^q. Explicitly inspect the Hessian-a and high-cutoff terms, remembering ∇²a=2χ∇²χ+2dχ⊗dχ and that no division by a or fictitious χ factor is allowed. Assess A01's alternative split {χ≥δ}/{χ<δ}: does small C0 metric drift on {χ<δ} imply C^k curvature control there? If not, state the valid integrated route and its exact inputs. The useful output is a rigorous order-one lemma or an exact unresolved term, not a broad summary.

## Output

# 科学核验备忘录：一阶无权 shifted-curvature 估计

## 1. 结论

设
\[
T=\operatorname{Rm}+G,\qquad U=aT,\qquad a=\chi^2,\qquad
W=\nabla U,\qquad \Theta=\nabla^2\chi,
\]
并在有限光滑时间段 \([\tau,T_0)\)、\(\tau>0\) 上假设

\[
\sup |U|\le K,
\]
以及对每个有限 \(q\),
\[
\sup_t\bigl(\|T\|_{L^q}+\|W\|_{L^q}+\|\Theta\|_{L^q}\bigr)<\infty.
\]

则对每个有限 \(q\),
\[
\boxed{\sup_{t\in[\tau,T_0)}\|\nabla T(t)\|_{L^q}<\infty.}
\]

对目标指数 \(p\ge2\)，实际只需 \(T,W,\Theta\in L^{2p}\)。证明不除以 \(a\)，不需要 \(\nabla^3\chi\) 的先验范数，也不把
\[
\nabla^2a=2\chi\Theta+2\,d\chi\otimes d\chi
\]
中的第二项伪装成带 \(\chi\) 的项。这正是 \(m=2\) 耦合对之前所需的一阶无权模块。

---

## 2. 一阶演化式

shifted tensor 的全协变方程具有穷尽导数阶数的形式
\[
(\partial_t-a\Delta)T
=a(T*T+G*T)+\nabla a*\nabla T+\nabla^2a*T. \tag{2.1}
\]
这里没有纯粹的 \((\nabla^2a)*G\) 源项；当 \(T=0\) 时 \(E=0\)，流静止，与此结构一致。

令
\[
X=\nabla T.
\]
对 (2.1) 取一阶协变导数，并计入
\[
\partial_t\Gamma=\nabla(aE)=\nabla\operatorname{Ric}(U)=W
\]
的通用收缩，可整理为
\[
\begin{aligned}
\partial_tX={}&a\Delta X
+\nabla a*\nabla X+\nabla^2a*X+\nabla^3a*T\\
&+aT*X+aG*X
+\nabla a*T*T+\nabla a*G*T+W*T. \tag{2.2}
\end{aligned}
\]
曲率与 Laplacian 的交换项也落在 \(aT*X+aG*X\) 中，因为
\(\nabla G=0\) 且 \(\nabla\operatorname{Rm}=X\)。

范数和体积元随时间的变化只增加 \(C K\int|X|^p\)，因为
\[
|aE|=|\operatorname{Ric}(U)|\le C_nK. \tag{2.3}
\]

---

## 3. 加权耗散与梯度-\(a\) 项

取
\[
P(X)=|X|^{p-2}X,\qquad
D_p=\int_M a|\nabla X|^2|X|^{p-2}\,d\mu.
\]
扩散项和所有 \(\nabla a*\nabla X\) 项满足
\[
\int P(X)*(a\Delta X+\nabla a*\nabla X)
\le -c_pD_p+
C_p\int|\nabla a|\,|\nabla X|\,|X|^{p-1}. \tag{3.1}
\]
由于
\[
\nabla a=2\chi\,d\chi,\qquad
\frac{|\nabla a|^2}{a}=4|d\chi|^2, \tag{3.2}
\]
Young 不等式给出
\[
C_p\int|\nabla a|\,|\nabla X|\,|X|^{p-1}
\le \varepsilon D_p+
C_{p,\varepsilon}\|d\chi\|_\infty^2\|X\|_p^p. \tag{3.3}
\]

---

## 4. Hessian-\(a\) 项

展开
\[
\nabla^2a=2\chi\Theta+2\,d\chi\otimes d\chi. \tag{4.1}
\]
测试 \(\nabla^2a*X\) 后，第二部分直接满足
\[
\left|\int(d\chi\otimes d\chi)*X*P(X)\right|
\le C\|d\chi\|_\infty^2\|X\|_p^p. \tag{4.2}
\]

第一部分是有符号 Hessian 收缩。若
\[
J=\int\chi\nabla_i\nabla_j\chi\,B^{ij}(X),
\]
其中
\[
|B(X)|\le C_p|X|^p,\qquad
|\nabla B(X)|\le C_p|X|^{p-1}|\nabla X|,
\]
则闭流形上的协变分部积分给出
\[
J=-\int\nabla_i\chi\nabla_j\chi\,B^{ij}
  -\int\chi\nabla_j\chi\,\nabla_iB^{ij}.
\]
因此
\[
|J|\le \varepsilon D_p+
C_{p,\varepsilon}\|d\chi\|_\infty^2\|X\|_p^p. \tag{4.3}
\]
所以 Hessian-\(a\) 项不需要 \(\Theta\in L^\infty\)，也没有给
\(d\chi\otimes d\chi\) 插入额外的 \(\chi\)。

---

## 5. 最高 cutoff 项 \(\nabla^3a*T\)

必须先展开
\[
\nabla^3a
=2\chi\nabla^3\chi+d\chi*\Theta. \tag{5.1}
\]
低阶部分直接满足
\[
\begin{aligned}
\left|\int(d\chi*\Theta*T)*P(X)\right|
&\le C\|d\chi\|_\infty
 \|\Theta\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}\\
&\le C_p(1+\|X\|_p^p). \tag{5.2}
\end{aligned}
\]

对唯一含当前三阶 cutoff jet 的积分
\[
I=\int\chi\,\nabla\Theta*T*P(X), \tag{5.3}
\]
只把 \(\nabla\Theta\) 上的一阶导数移走：
\[
\begin{aligned}
I={}&-\int d\chi*\Theta*T*P(X)
-\int\chi\Theta*X*P(X)\\
&-\int\chi\Theta*T*\nabla P(X). \tag{5.4}
\end{aligned}
\]

第一项由 (5.2) 控制。第二项再次是 (4.3) 型有符号 Hessian 收缩。对于第三项，
\[
|\nabla P(X)|\le C_p|X|^{p-2}|\nabla X|,
\]
故
\[
\begin{aligned}
\left|\int\chi\Theta*T*\nabla P(X)\right|
&\le \varepsilon D_p
+C_{p,\varepsilon}
 \int|\Theta|^2|T|^2|X|^{p-2}\\
&\le \varepsilon D_p+
C_{p,\varepsilon}
 \|\Theta\|_{2p}^2\|T\|_{2p}^2\|X\|_p^{p-2}\\
&\le \varepsilon D_p+C_p(1+\|X\|_p^p). \tag{5.5}
\end{aligned}
\]

因此
\[
\boxed{
\left|\int(\nabla^3a*T)*P(X)\right|
\le \varepsilon D_p+C_p(1+\|X\|_p^p).} \tag{5.6}
\]

这里没有使用 \(Z=\nabla^3\chi\) 的任何范数。重要的操作顺序是先用
(5.1) 分离 \(\chi\nabla^3\chi\) 与 \(d\chi*\Theta\)，然后只对前者分部积分。若把整个 \(\nabla^3a=\nabla(\nabla^2a)\) 一次性分部积分，会产生
\[
(d\chi\otimes d\chi)*T*\nabla P(X),
\]
它没有 \(\chi\) 因子，不能直接由 \(D_p\) 吸收。

---

## 6. 其余乘积

(2.2) 的代数项逐项满足：

\[
\int a|T||X|^p
=\int|U||X|^p
\le K\|X\|_p^p, \tag{6.1}
\]

\[
\int|\nabla a|\,|T|^2|X|^{p-1}
\le C\|d\chi\|_\infty\|T\|_{2p}^2\|X\|_p^{p-1}, \tag{6.2}
\]

\[
\int|W|\,|T|\,|X|^{p-1}
\le \|W\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}. \tag{6.3}
\]

所有 \(G\)-线性项只需 \(|G|=C_n\)、\(\nabla G=0\)，因而也由
\(T,W\) 的 \(L^p\) 范数和 \(\|X\|_p^p\) 控制。

综合 (3.3)、(4.2)–(4.3)、(5.6) 和 (6.1)–(6.3)，选取有限多个
\(\varepsilon\) 后得到
\[
\boxed{
\frac d{dt}\|X\|_p^p+c_pD_p
\le C_p\bigl(1+\|X\|_p^p\bigr),} \tag{6.4}
\]
其中 \(C_p\) 依赖于
\[
n,p,K,\ \sup|d\chi|,\ 
\sup_t\bigl(\|T\|_{2p}+\|W\|_{2p}+\|\Theta\|_{2p}\bigr),
\]
以及该光滑数据的体积和度量等价常数。

由于 \(X(\tau)\) 光滑，Gronwall 给出
\[
\sup_{t<T_0}\|\nabla T(t)\|_p<\infty. \tag{6.5}
\]
对每个 \(p\ge2\) 分别应用该估计，再由有限体积上的 Hölder 得到
\(1\le q<2\) 的结果。零点处可用
\[
(|X|^2+\varepsilon^2)^{(p-2)/2}X
\]
测试后令 \(\varepsilon\downarrow0\)。

这与 Wang Proposition 4.13 在 \(m=1\) 时的顺序一致：其输入只包含
二阶 cutoff jet 和零阶曲率的高有限指数范数；原文中的
\(\chi\nabla^3\chi*\operatorname{Rm}\) 正是通过一次分部积分降到
\(\nabla^2\chi\)。归一化后的新增量是 \(W*T\) 与 \(G\)-线性项，分别由
m=1 基础对和 \(\nabla G=0\) 处理。

---

## 7. \(\{\chi\ge\delta\}/\{\chi<\delta\}\) 分区论证

A01 的小-\(\chi\) 漂移估计
\[
|g(t)-g(\tau)|
\le 2\chi^2K(t-\tau)
\]
不能由 \(\sup|U|\le K\) 推出。实际只有
\[
|aE|=|\operatorname{Ric}(U)|\le C_nK, \tag{7.1}
\]
而不是 \(|aE|\le C\chi^2K\)。在 \(0<\chi<\delta\) 的过渡区，\(T\) 可以具有
\(a^{-1}\) 量级，同时 \(U=aT\) 仍保持有界。

即使另有一个很小的 \(C^0\) 度量漂移，也不能推出曲率及其导数控制。具体地，在平坦二维环面上取
\[
g_N=e^{2f_N}g_{\rm flat},\qquad
f_N=N^{-1}\sin(Nx_1).
\]
则
\[
\|g_N-g_{\rm flat}\|_{C^0}\longrightarrow0,
\]
但 Gaussian 曲率为
\[
K_{g_N}=-e^{-2f_N}\Delta f_N
=e^{-2f_N}N\sin(Nx_1),
\]
其上确界随 \(N\) 发散；更高曲率导数具有更高的 \(N\) 次幂。与额外平坦因子作乘积即可得到任意 \(n\ge2\) 的同类例子。

因此小-\(\chi\) 区域上的 \(C^0\) 漂移不能替代空间二阶及更高阶估计。有效顺序是全流形上的积分估计：
\[
(T\text{ 的全部有限 }L^q)
+\bigl(W,\Theta\bigr)\text{ 的全部有限 }L^q
\Longrightarrow
\nabla T\text{ 的全部有限 }L^q,
\]
随后才进入
\[
(V,Z)=(\nabla^2U,\nabla^3\chi)
\]
的 \(m=2\) 同指数耦合估计。