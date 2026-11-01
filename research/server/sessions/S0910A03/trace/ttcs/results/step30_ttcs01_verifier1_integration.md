# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 30,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step30_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step30_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Adversarially verify the claimed smooth-extension proof for the normalized fixed-cutoff flow ∂_t g=-2χ²(Ric+g), focusing only on the high-order Wang induction. Read Wang's actual Section 4 source and the Codex/A03 shifted-curvature derivations. Determine whether the grouped Γ1–Γ4 integrations really bound ∇^m U using cutoff derivatives only through order m (not m+1 or m+2), without dividing by χ or assuming hidden pointwise bounds. Expand the dangerous terms sufficiently to expose any unmatched factor, state a valid finite Hölder-exponent schedule if it closes, and classify the new G-linear terms exactly. If the source itself has a gap, identify it precisely rather than inheriting it. The scientific output should be a rigorous lemma/proof or a concrete obstruction.

## Integrated Scientific Memo

# 核验结论：Wang 高阶归纳在 cutoff 阶数 \(m\) 处不闭合，但在 \(m+1\) 阶耦合后可闭合

令
\[
a=\chi^2,\qquad 
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\Rm+G,\qquad U=aT .
\]
按给定曲率约定，
\[
\Ric(G)=g,\qquad \nabla G=0,\qquad
a(\Ric+g)=\Ric(U),
\]
故归一化局部流可写为
\[
\partial_tg=-2\Ric(U).
\]
这一 shift 是正确的，并保持 cutoff-jet 方程的三角结构。不过，`shifted_curvature_continuation.md` §7.3 所称“估计 \(\nabla^mU\) 只需 cutoff 导数至 \(m\) 阶”是错误的；Wang Proposition 4.14 的相同表述也遗漏了一项。正确结构是
\[
\boxed{\nabla^mU\quad\text{必须与}\quad\nabla^{m+1}\chi
\text{ 同时估计}.}
\]

## 1. 精确障碍

设
\[
V=\nabla^mU,\qquad H=\nabla^{m+1}\chi,\qquad
\Phi_p(V)=|V|^{p-2}V,
\]
并记扩散耗散项
\[
D_{m,p}=\int_M\chi^2|\nabla V|^2|V|^{p-2}\,d\mu .
\]
微分后的 \(U\)-方程确实含有四类最高阶项
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]
\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\quad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U .
\]

对 \(\Gamma_1\) 的一个代表性收缩积分一次分部：
\[
\begin{aligned}
\int\Phi_p(V)*\chi\nabla H*U
={}&-\int\nabla\Phi_p(V)*\chi H*U\\
&-\int\Phi_p(V)*\nabla\chi*H*U\\
&-\int\Phi_p(V)*\chi H*\nabla U
+\text{交换子项}.
\end{aligned}
\]
第一项满足
\[
\begin{aligned}
\left|\int\nabla\Phi_p(V)*\chi H*U\right|
&\le C_p\|U\|_\infty
 \int\chi|\nabla V|\,|H|\,|V|^{p-2}\\
&\le \varepsilon D_{m,p}
 +C_{\varepsilon,p}\|U\|_\infty^2
 \int |H|^2|V|^{p-2}\\
&\le \varepsilon D_{m,p}
 +C\|H\|_{L^p}^2\|V\|_{L^p}^{p-2}.
\end{aligned}
\tag{1}
\]
因此分部仅把 \(\nabla^{m+2}\chi\) 降到
\(\nabla^{m+1}\chi\)，并没有降到 \(m\) 阶。

此外，\(\Gamma_2\) 本身直接给出
\[
\left|\int\Phi_p(V)*\nabla\chi*H*U\right|
\le C\|H\|_{L^p}\|V\|_{L^p}^{p-1}.
\tag{2}
\]
若试图再从 \(H=\nabla(\nabla^m\chi)\) 上分部，导数落到 \(V\) 时出现未加权的 \(\nabla V\)。可用耗散只有
\(\chi\nabla V\)；将其吸收需要引入
\[
\frac{|\nabla\chi|}{\chi},
\]
这在 \(\{\chi=0\}\) 附近不可控。再次分部 \((1)\) 则产生
\(\nabla^2V\)，超出当前能量控制。因此不存在既不除以 \(\chi\)、又只使用 cutoff 至 \(m\) 阶的闭合方式。

\(\Gamma_3\) 同样保留 \(H=\nabla^{m+1}\chi\)；\(\Gamma_4\) 则是唯一可直接由耗散吸收的最高 \(U\)-导数项：
\[
\left|\int\Phi_p(V)*\chi\nabla\chi*\nabla V\right|
\le \varepsilon D_{m,p}+C\|V\|_p^p.
\tag{3}
\]

所以 Wang Proposition 4.14 中“分部后仅剩
\(\nabla^2\chi*\nabla^m\chi*\cdots\)”的句子不完整：至少遗漏了
\[
\nabla\Phi_p(V)*\chi\nabla^{m+1}\chi*U .
\]
Wang 自己的 Lemma 4.11 在 \(m=1\) 时实际上保留了
\(\nabla^2\chi\)，并把它与 \(\nabla U\) 联立估计；这正是一般阶的正确机制。

## 2. 修正后的高阶耦合引理

### 引理

假设在有限区间 \([0,T)\) 上：

1. \(g(t)\) 一致等价于 \(g(0)\)；
2. \(\|U\|_\infty\) 与 \(\|\nabla\chi\|_\infty\) 一致有界；
3. 所有低于当前阶的 \(U,T\) 导数，以及 \(\chi\) 至 \(m\) 阶的导数，已在所需有限 \(L^q\) 空间一致有界。

固定 \(p>\max\{n,2\}\)，令
\[
X_p=\|\nabla^mU\|_p^p,\qquad
Z_p=\|\nabla^{m+1}\chi\|_p^p.
\]
则有
\[
\boxed{
\frac d{dt}(X_p+Z_p)+c_{m,p}D_{m,p}
\le C_{m,p}(1+X_p+Z_p).}
\tag{4}
\]

### 证明要点

由上面的 \(\Gamma_i\) 展开及 Young 不等式，
\[
\frac d{dt}X_p+cD_{m,p}
\le C(1+X_p+Z_p).
\tag{5}
\]
其中：

- \(\Gamma_1\) 用式 \((1)\)；
- \(\Gamma_2\) 用式 \((2)\)；
- \(\Gamma_3\) 分部后，导数落在 \(V\) 上的项由 \(D_{m,p}\) 吸收，其余用低阶有限 \(L^q\) 范数；
- \(\Gamma_4\) 用式 \((3)\)。

由于
\[
\partial_t\Gamma=g^{-1}*\nabla\Ric(U)
\]
且 \(\chi\) 是固定标量，最高阶 cutoff 演化具有形式
\[
\partial_t\nabla^{m+1}\chi
=U*\nabla^{m+1}\chi
 +\nabla^mU*\nabla\chi+L_m,
\tag{6}
\]
其中 \(L_m\) 只含已知低阶量。于是
\[
\frac d{dt}Z_p\le C(1+Z_p+X_p).
\tag{7}
\]
将 \((5)\)、\((7)\) 相加即得 \((4)\)，再由 Grönwall 闭合。全程不出现 \(1/\chi\)，也不假设高阶 cutoff 的点态界。

正确归纳顺序因此是
\[
\boxed{
B_{m-1}
\longrightarrow
\bigl(A_m,C_{m+1}\bigr)
\longrightarrow B_m,
}
\]
即
\[
(\nabla^mU,\nabla^{m+1}\chi)
\quad\text{联立估计，随后估计}\quad \nabla^mT.
\]
这与 `step27...md` 的 Move A/Move B 一致，而与
`shifted_curvature_continuation.md` §7.3 的
\(C_m\to A_m\) 断言不一致。

## 3. 一个有限 Hölder 指数方案

对任意目标指数
\[
p>\max\{n,2\},
\]
在低阶归纳中同时保留
\[
p,\qquad 2p,\qquad 4p
\]
即可：

- 当前量 \(\nabla^mU,\nabla^{m+1}\chi\) 使用 \(L^p\)；
- 如
  \[
  \int |Q|^2|\nabla U|^2|V|^{p-2}
  \]
  的项取 \(Q,\nabla U\in L^{2p}\)；
- 展开
  \[
  \nabla^ia=\sum_{r=0}^i\nabla^r\chi*
                         \nabla^{i-r}\chi
  \]
  后，一个反应项至多含两个 cutoff 因子、一个低阶 \(U\) 因子和一个低阶 \(T\) 因子；把这些低阶因子置于 \(L^{4p}\)，其乘积在 \(L^p\)；
- \(m=2\) 时出现的加权项可用一致 Sobolev 不等式及
  \(\nabla^2\chi\in L^n\) 处理；因 \(p>n\)，该范数已包含在归纳库存中。二维时取任意固定 \(q>2\) 的相应 Sobolev 指数。

因此每个目标 \(p\) 只调用有限个更高指数，不形成无限指数回溯。

## 4. 新的 \(G\)-线性项的精确分类

因为 \(\nabla G=0\)，归一化在 \(U\)-方程中新增的全部项恰为
\[
\boxed{
\mathcal G_m
=\sum_{i+j=m}\nabla^ia*G*\nabla^jU.}
\tag{8}
\]
其分类为：

- \(i=0,j=m\)：
  \[
  aG*\nabla^mU,
  \]
  是作用于当前导数的有界零阶线性系数；
- \(j<m\)：
  \[
  \nabla^ia*G*\nabla^jU,
  \]
  只含 cutoff 至 \(i\le m\) 阶及低阶 \(U\)-导数。

故
\[
\left|\int\Phi_p(V)*\mathcal G_m\right|
\le C(1+X_p).
\tag{9}
\]
它们不含 \(\nabla^{m+1}\chi\)、\(\nabla^{m+1}U\)，也不需要扩散吸收。

相应地，未加权 shifted curvature 方程中的新项为
\[
\boxed{
\widetilde{\mathcal G}_m
=\sum_{i+j=m}\nabla^ia*G*\nabla^jT.}
\tag{10}
\]
同样，\(j=m\) 是有界线性当前阶项，\(j<m\) 是已知低阶项。

这里不存在独立的
\((\nabla^2a)*G\) 源项：shifted 方程右端每项都含 \(T\) 或其导数。这也由 \(T=0\) 对应 \(\Ric=-g\)、且该状态对任意 cutoff 都静止所强制。

## 5. 最终判定

- **被核验的原断言不成立：** grouped \(\Gamma_1\)–\(\Gamma_4\) 分部不能只依赖 cutoff 导数至 \(m\) 阶。
- **精确遗漏项：**
  \[
  \nabla\Phi_p(\nabla^mU)*
  \chi\nabla^{m+1}\chi*U,
  \]
  以及原始 \(\Gamma_2,\Gamma_3\) 中的裸
  \(\nabla^{m+1}\chi\)。
- **不能合法消去它们：** 再分部会要求 \(\nabla^2V\)，或通过吸收未加权 \(\nabla V\) 强迫除以 \(\chi\)。
- **但高阶延拓归纳仍可修复：**
  \[
  \nabla^mU\leftrightarrow\nabla^{m+1}\chi
  \]
  联立 Grönwall 后，再估计 \(\nabla^mT\)。
- **所需最高 cutoff 阶数是 \(m+1\)，不是 \(m\)，但不需要 \(m+2\) 阶作为先验输入。**
- 新 \(G\)-项严格属于有界零阶线性项或已知低阶项，不改变耦合结构。

因此，Wang Section 4 的 Proposition 4.14 按其书面表述存在一个明确的高阶 bookkeeping gap；该 gap 可由上述同阶耦合引理补上。