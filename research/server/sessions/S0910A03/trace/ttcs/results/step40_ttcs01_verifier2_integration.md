# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 40,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step40_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step40_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the independent unweighted shifted-curvature derivative ordering needed before the m=2 pair. Determine whether ∇T∈L^q for all finite q follows from the actual T equation under |U| bounded, the m=1 base pair (∇U,∇²χ) finite in all L^q, and T finite in all L^q. Explicitly inspect the Hessian-a and high-cutoff terms, remembering ∇²a=2χ∇²χ+2dχ⊗dχ and that no division by a or fictitious χ factor is allowed. Assess A01's alternative split {χ≥δ}/{χ<δ}: does small C0 metric drift on {χ<δ} imply C^k curvature control there? If not, state the valid integrated route and its exact inputs. The useful output is a rigorous order-one lemma or an exact unresolved term, not a broad summary.

## Integrated Scientific Memo

## 一阶无权 shifted-curvature 引理

令
\[
a=\chi^2,\qquad T=\Rm+G,\qquad U=aT,\qquad X=\nabla T,
\]
并在有限光滑区间 \([\tau,T_0)\), \(\tau>0\), 上假设
\[
\|U\|_{L^\infty(M\times[\tau,T_0))}\le K,
\]
且对每个有限 \(q\),
\[
\sup_{t<T_0}\bigl(
\|T(t)\|_{L^q}+\|\nabla U(t)\|_{L^q}
+\|\nabla^2\chi(t)\|_{L^q}\bigr)<\infty .
\]
则对每个有限 \(q\),
\[
\boxed{\sup_{t<T_0}\|\nabla T(t)\|_{L^q}<\infty.}
\]

事实上，目标指数 \(p\ge2\) 只需 \(T,\nabla^2\chi\in L^{2p}\)；\(\nabla U\) 仅用于完整记录连接变化项，且也已由 \(m=1\) 基础对提供。证明既不除以 \(a\)，也不要求 \(\nabla^3\chi\) 的先验控制。

### 1. 实际一阶方程

shifted 曲率满足
\[
(\partial_t-a\Delta)T
=a(T*T+G*T)+\nabla a*\nabla T+\nabla^2a*T.
\]
取一阶协变导数，并计入
\[
\partial_t\Gamma=\nabla(aE)
=\nabla\Ric(U),
\]
得到安全的示意式
\[
\begin{aligned}
\partial_tX={}&a\Delta X+\nabla a*\nabla X
+\nabla^2a*X+\nabla^3a*T\\
&+aT*X+aG*X+\nabla a*T*T+\nabla a*G*T
+\nabla U*T .
\end{aligned}
\tag{1}
\]
由于 \(|aE|=|\Ric(U)|\le C_nK\)，度量、体积和有限 \(L^q\) 范数在该区间统一等价。

以
\[
P(X)=|X|^{p-2}X,\qquad
D_p=\int_M a|\nabla X|^2|X|^{p-2}
\]
测试 (1)。扩散及 \(\nabla a*\nabla X\) 项由
\[
\nabla a=2\chi\,d\chi,\qquad
\frac{|\nabla a|^2}{a}=4|d\chi|^2
\]
给出
\[
\le -c_pD_p+C_p\|d\chi\|_\infty^2\|X\|_p^p.
\]

### 2. Hessian-\(a\) 项

必须使用真实展开
\[
\boxed{\nabla^2a=2\chi\nabla^2\chi+2\,d\chi\otimes d\chi.}
\]
第二项没有 \(\chi\)，但它只乘 \(X\)，故
\[
\left|\int(d\chi\otimes d\chi)*X*P(X)\right|
\le C\|d\chi\|_\infty^2\|X\|_p^p.
\]
第一项是有符号 Hessian 收缩：
\[
J=\int\chi\nabla_i\nabla_j\chi\,B^{ij}(X),
\quad |B|\le C_p|X|^p,\quad
|\nabla B|\le C_p|X|^{p-1}|\nabla X|.
\]
一次分部积分给出
\[
|J|\le \varepsilon D_p+
C_{p,\varepsilon}\|d\chi\|_\infty^2\|X\|_p^p.
\tag{2}
\]
因此不能把 \(d\chi\otimes d\chi\) 伪装成带 \(\chi\) 的项，但也不需要这样做。

### 3. 最高 cutoff 项

展开
\[
\nabla^3a=2\chi\nabla^3\chi+C\,d\chi*\nabla^2\chi.
\]
后者直接由 Hölder 控制。唯一含三阶 cutoff jet 的积分为
\[
I=\int\chi\,\nabla(\nabla^2\chi)*T*P(X).
\]
只将该导数移走：
\[
\begin{aligned}
I={}&-\int d\chi*\nabla^2\chi*T*P(X)\\
&-\int\chi\nabla^2\chi*X*P(X)\\
&-\int\chi\nabla^2\chi*T*\nabla P(X).
\end{aligned}
\tag{3}
\]
第一项由 \(T,\nabla^2\chi\in L^{2p}\) 控制；第二项再用 (2)。第三项满足
\[
\begin{aligned}
\left|\int\chi\nabla^2\chi*T*\nabla P(X)\right|
&\le \varepsilon D_p+
C_{p,\varepsilon}
\int|\nabla^2\chi|^2|T|^2|X|^{p-2}\\
&\le \varepsilon D_p+
C_{p,\varepsilon}
\|\nabla^2\chi\|_{2p}^2\|T\|_{2p}^2\|X\|_p^{p-2}\\
&\le \varepsilon D_p+C_p(1+\|X\|_p^p).
\end{aligned}
\tag{4}
\]
这一步不使用 \(\nabla^3\chi\) 的范数。

需注意：不能把整个 \(\nabla^3a=\nabla(\nabla^2a)\) 不加区分地分部积分；否则会产生
\[
(d\chi\otimes d\chi)*T*\nabla P(X),
\]
其上没有供退化耗散吸收的 \(\chi\)。正确顺序正是先展开 \(\nabla^3a\)，只对 \(\chi\nabla^3\chi\) 分部积分。

### 4. 其余项

代表性估计为
\[
\int a|T||X|^p=\int |U|\,|X|^p\le K\|X\|_p^p,
\]
\[
\int|\nabla a|\,|T|^2|X|^{p-1}
\le C\|T\|_{2p}^2\|X\|_p^{p-1},
\]
以及
\[
\int|\nabla U|\,|T|\,|X|^{p-1}
\le \|\nabla U\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}.
\]
\(G\)-项仅使用 \(|G|=C_n\) 与 \(\nabla G=0\)。

综合后，选择小 \(\varepsilon\) 吸收耗散：
\[
\boxed{
\frac d{dt}\|X\|_p^p+c_pD_p
\le C_p(1+\|X\|_p^p).
}
\tag{5}
\]
由 \(X(\tau)\) 光滑和 Gronwall，
\[
\sup_{t<T_0}\|\nabla T(t)\|_{L^p}<\infty.
\]
逐个取 \(p\ge2\)，再用有限体积 Hölder，得到所有有限 \(q\)。因此该一阶无权模块确实在 \(m=2\) 对
\[
(\nabla^2U,\nabla^3\chi)
\]
之前闭合。

## A01 分区法无效

\(\{\chi\ge\delta\}/\{\chi<\delta\}\) 的替代论证有两个独立错误。

第一，
\[
|aE|=|\Ric(U)|\le C_nK
\]
并不含额外的 \(\chi^2\)。因此在 \(\{\chi<\delta\}\) 上不能推出
\[
|g(t)-g(\tau)|\lesssim \delta^2K(t-\tau).
\]
这里 \(T\) 可具有 \(a^{-1}\) 量级而 \(U=aT\) 仍有界。

第二，即使另有小的 \(C^0\) 度量漂移，也不能推出曲率的 \(C^k\) 控制。曲率依赖度量的二阶空间导数，\(\nabla^k\Rm\) 依赖 \(k+2\) 阶导数。比如平坦二维环面上的
\[
g_N=e^{2f_N}g_{\rm flat},\qquad f_N=N^{-1}\sin(Nx_1)
\]
满足 \(g_N\to g_{\rm flat}\) 于 \(C^0\)，但
\[
K_{g_N}=-e^{-2f_N}\Delta f_N
=e^{-2f_N}N\sin(Nx_1)
\]
无界。故“小 \(C^0\) 漂移 \(\Rightarrow C^k\) 曲率控制”是错误推断。

## 有效顺序与精确输入

正确路线是全流形积分估计，不分区、不除以 \(a\)：
\[
\boxed{
\begin{gathered}
\sup|U|<\infty,\\
T\in L^q\quad(\forall q<\infty),\\
\nabla U,\ \nabla^2\chi\in L^q\quad(\forall q<\infty)
\end{gathered}
\Longrightarrow
\nabla T\in L^q\quad(\forall q<\infty).
}
\]
对固定目标 \(p\)，上述证明具体只调用 \(T,\nabla U,\nabla^2\chi\) 的若干有限指数范数（取 \(2p\) 足够），加上 \(\|d\chi\|_\infty\)、度量等价和光滑初值。没有使用 \(a^{-1}\)、无权曲率点态界或 \(\nabla^3\chi\) 的先验控制。