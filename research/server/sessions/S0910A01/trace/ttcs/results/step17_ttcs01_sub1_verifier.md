# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step17_support_scale_li_bootstrap.md",
    "Sessions/S0910A01/workspace/scripts/step17_sobolev_energy_cancellation.py",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md"
  ]
}
```

## Task

Verify the support-scale-consistent cutoff-flow construction for the 4D negative LeBrun branch. The construction claims to resolve the quantifier mismatches from Step 16 by choosing ALL radii as fixed multiples of the Li scale r_*. The key mathematical claims to verify are: (1) The Vitali/thinning construction produces disjoint supports B_{4r_*}(p_j) whose plateaux B_{3r_*}(p_j) are separated, with a positive volume fraction of bootstrap domains B_{r_*}(p_j). (2) For every center y in B_{2r_*}(p_j), the maximal function at p_j controls the Li dimensionless quantity: epsilon_y(r_*) = r_*^4 * fint_{B_{r_*}(y)} |Rm|^2 <= C K_0 r_*^4 which is small for small r_*. (3) The Li covering argument (Theorem 3.4) works on the plateau B_{3r_*}(p_j) because all covering balls B_{r_*}(y_k) with y_k in B_{3r_*/2}(x) stay inside the plateau when x in B_{r_*}(p_j). (4) THE CRITICAL CLAIM: The 4D Sobolev-energy product C_S * ||Rm||_{L^2(support)} is O(r_*^2) and absorbs the cubic/defect reaction terms in BOTH the Rm energy inequality and the E energy inequality on the transition, even though |Rm| is not pointwise bounded there. This uses the 4D critical Sobolev embedding where the Sobolev constant C_S is dimensionless. (5) The modified Li bootstrap on the full support (including transition) closes because the transition terms add only a linear C r_*^{-2} growth rate, giving bounded exponential factor over time theta r_*^2. (6) Metric comparability holds because |partial_t g| = 2 chi^2 |E| <= 2 delta, and total drift over theta r_*^2 is O(delta r_*^2). Check all six claims for mathematical correctness. Identify any circularity, wrong exponent, missing hypothesis, or gap.

## Output

# 科学核验备忘

## 总体结论

固定所有半径为 \(r_*\) 的常数倍，确实修复了“一个好点无法控制远处大量中心”的静态尺度问题，也能保留固定比例的 \(B_{r_*}\) 区域。但当前构造仍未闭合抛物估计：

- Vitali 筛选可修正后成立，但文中的 \(7r_*\) 分离并不使 \(B_{4r_*}\) 支集互不相交。
- 最大函数给出的初始归一化曲率能量小量成立，常数比较需改写。
- Plateau 上的 Li 迭代仍有内外层错位；文中所说的所有覆盖球都留在 \(B_{3r_*}\) 内是错误的。
- 四维相对 Sobolev–能量消去机制在固定时刻是正确的，但必须使用随塌缩增大的相对 Sobolev 常数，而不是脚本中的 \(C_S=2\)。
- 从耦合 \(L^2\) 能量到整个支集上的未加权 \(|\mathrm{Rm}|\le C/t\) 没有推出；靠近 \(\chi=0\) 的区域一般只能期待加权估计。
- \(|\partial_tg|\le2\delta\) 只在初始时刻可得。将它用于度量等价性，再用度量等价性证明缺陷控制，构成循环依赖。

因此，固定尺度设计有实质价值，但尚未推出该 LeBrun 族中不存在
\(\|\operatorname{Ric}+g\|_\infty\to0\) 的序列。

---

## 1. Vitali 选择与 thinning

令 \(r=r_*\)，并记

\[
\beta_m(r)=\frac{V_{-1}(mr)}{V_{-1}(r)}.
\]

对以 \(G_i\) 中点为中心的极大互不相交球族 \(\{B_r(p_j)\}\)，极大性给出

\[
G_i\subset \bigcup_j B_{5r}(p_j),
\]

因而由 Bishop–Gromov 比较，

\[
\operatorname{Vol}(G_i)
 \le \sum_j\operatorname{Vol}B_{5r}(p_j)
 \le \beta_5(r)\sum_j\operatorname{Vol}B_r(p_j).
\]

这部分成立。

若 greedy thinning 要求中心间距至少 \(Lr\)，每个被舍去的原始球
\(B_r(q)\) 都包含在某个保留中心的 \(B_{(L+1)r}(p)\) 中。由于原始
\(B_r(q)\) 两两不交，

\[
\sum_{\text{归属于 }p}\operatorname{Vol}B_r(q)
 \le \operatorname{Vol}B_{(L+1)r}(p)
 \le \beta_{L+1}(r)\operatorname{Vol}B_r(p).
\]

于是保留的 \(B_r\) 总体积至少为原始总体积的
\(\beta_{L+1}(r)^{-1}\)。

具体而言：

- 要使 \(B_{3r}(p_j)\cap B_{4r}(p_k)=\varnothing\)，需要中心间距至少 \(7r\)。
- 要使两个 \(B_{4r}\) 支集互不相交，需要中心间距至少 \(8r\)，若还要求闭包分离，可取 \(8+\sigma\)。

因此，文中的 \(7r\) thinning 只保证每个 plateau 不遇到另一个支集；两个 transition annulus 仍可能相交，“支集互不相交、各流独立”并不随之成立。改用 \(8r\) thinning 后，固定比例仍保留，但相应分母应为 \(\beta_9(r)\)，而不是 \(\beta_8(r)\)。

数值 \(625\) 与 \(4096\) 只是 \(r\to0\) 时的渐近值：

\[
\beta_5(r)\to5^4,\qquad \beta_8(r)\to8^4.
\]

在固定正 \(r\) 上不能把它们当成精确常数。正确结果是某个只依赖固定半径与维数的正比例。

---

## 2. 最大函数对附近中心的初始控制

设 \(p\in G_i\)，即

\[
\sup_{0<\rho\le4r}
 \fint_{B_\rho(p)}|\mathrm{Rm}|^2\le K_0.
\]

若 \(y\in B_{2r}(p)\)，则

\[
B_r(y)\subset B_{3r}(p).
\]

因此可直接使用半径 \(3r\) 的最大函数估计：

\[
\begin{aligned}
\int_{B_r(y)}|\mathrm{Rm}|^2
&\le \int_{B_{3r}(p)}|\mathrm{Rm}|^2\\
&\le K_0\,\operatorname{Vol}B_{3r}(p).
\end{aligned}
\]

又因为 \(B_{3r}(p)\subset B_{5r}(y)\)，

\[
\fint_{B_r(y)}|\mathrm{Rm}|^2
 \le K_0\frac{\operatorname{Vol}B_{5r}(y)}
                  {\operatorname{Vol}B_r(y)}
 \le K_0\beta_5(r).
\]

所以

\[
r^4\fint_{B_r(y)}|\mathrm{Rm}|^2
 \le \beta_5(r)K_0r^4.
\]

这一核心估计成立。文中先用 \(B_{4r}(p)\) 再写 \(\beta_5\) 并不一致；若确实使用 \(B_{4r}(p)\)，比较常数应为 \(\beta_6\)。改用上面的 \(B_{3r}(p)\) 即可得到 \(\beta_5\)。

类似地，对 \(y\in B_{5r/2}(p)\) 仍有

\[
r^4\fint_{B_r(y)}|\mathrm{Rm}|^2
 \le \beta_6(r)K_0r^4.
\]

因此最大函数也能控制 Li 覆盖中出现的初始邻近中心。取 \(r\) 足够小可使上述量小于 Li 阈值；由于 \(\beta_5(r)\) 本身依赖 \(r\)，脚本中的显式等式应换成一个带余量的不等式。

---

## 3. Plateau 上的 Li 覆盖并未闭合

对 \(x\in B_r(p)\)，确有

\[
B_{2r}(x)\subset B_{3r}(p),
\]

所以用于局部能量微分的空间区域可以位于标准归一化 Ricci 流区域内。

但 Li 的覆盖中心满足

\[
y_k\in B_{3r/2}(x),
\]

从而最多只能推出

\[
y_k\in B_{5r/2}(p).
\]

更重要的是，

\[
B_r(y_k)\subset B_{7r/2}(p),
\]

而不是 \(B_{3r}(p)\)。所以“所有覆盖球都在 plateau 内”这一几何陈述不成立。

文中定义

\[
e_j(t)=\sup_{y\in B_{2r}(p)}
 \left(\int_{B_r(y)}|\mathrm{Rm}|^2\right)^{1/2},
\]

但对 \(x\in B_r(p)\) 的能量微分会调用中心位于
\(B_{5r/2}(p)\) 的球；这些球不受该 \(e_j(t)\) 控制。反过来，若把 supremum 扩大到 \(B_{5r/2}(p)\)，对新外层中心作时间微分又会调用更外层中心。固定半径倍数修复了初始最大函数控制，却没有产生一个在邻域扩张下封闭的有限 plateau supremum。

Ye Li 的 Theorem 3.4 明确使用全流形上的 supremum，并假设在整个时间区间内：

\[
\frac12g_0\le g(t)\le2g_0,
\]

以及每个相关球上的 Sobolev 不等式。它不能按文中的一句“覆盖留在 plateau”直接改成局部版本。这里仍需要整个 active support 上的耦合有限覆盖估计，或一个严格推导的嵌套区域估计。

另外，在 plateau 内 \(a=\chi^2=1\) 时，曲率演化在每一点就是标准归一化 Ricci 流演化，并不存在来自 transition 的额外局部项。真正的问题是热扩散估计需要邻域能量，而不是 transition 通过某个额外张量项直接耦合进 plateau 方程。

---

## 4. 四维 Sobolev–能量乘积

这一机制的正确形式如下。设

\[
U=B_{4r}(p),\qquad V=\operatorname{Vol}(U).
\]

最大函数给出

\[
\|\mathrm{Rm}\|_{L^2(U)}
 \le (K_0V)^{1/2}.
\]

Ye Li 文中使用的塌缩相容 Sobolev 常数满足

\[
A_U\le C\left(\frac{(4r)^4}{V}\right)^{1/2}.
\]

因此

\[
A_U\|\mathrm{Rm}\|_{L^2(U)}
 \le C\sqrt{K_0}\,(4r)^2
 =C\sqrt{K_0r^4}.
\]

所以体积因子确实消去，并可通过减小 \(r\) 使该乘积足够小。

但“\(C_S\) 在小球上接近欧氏常数”在塌缩情形并不成立。四维临界 Sobolev 常数在同尺度缩放下无量纲，却仍可能按

\[
A_U\asymp \frac{r^2}{\sqrt V}
\]

增大。脚本把 \(C_S=2\) 和欧氏球体积直接代入，只展示了非塌缩模型中的数值缩放，不能验证塌缩情形；其中 \(K_0\)、Li 阈值及耗散常数也只是占位数值。

吸收反应项时还必须使用与退化系数匹配的加权函数。例如

\[
\begin{aligned}
\int a\eta^2|\mathrm{Rm}|\,|E|^2
 &=\int |\mathrm{Rm}|\,|\chi\eta E|^2\\
 &\le \|\mathrm{Rm}\|_2
       \|\chi\eta E\|_4^2\\
 &\le A_U\|\mathrm{Rm}\|_2
       \int|\nabla(\chi\eta E)|^2.
\end{aligned}
\]

展开最后一项得到

\[
\int|\nabla(\chi\eta E)|^2
 \le C\int a\eta^2|\nabla E|^2
 +C\int\bigl(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2\bigr)|E|^2.
\]

这才与 \(E\)-能量中的加权耗散相匹配。文中直接写
\(\|E\|_4^2\le C_S\|\nabla E\|_2^2\) 会产生未加权
\(\int|\nabla E|^2\)，而 \(a\) 接近零处没有相应耗散。

曲率三次项同理：

\[
\int a\eta^2|\mathrm{Rm}|^3
 \le A_U\|\mathrm{Rm}\|_2
      \int|\nabla(\chi\eta|\mathrm{Rm}|)|^2.
\]

因此，第4项的代数机制是成立的，但只在以下数据同时可用时成立：

1. 当前时刻的局部 \(L^2\) 曲率仍小；
2. 当前度量仍有相同量级的相对 Sobolev 不等式；
3. cutoff 梯度仍受控；
4. \(A_U\|\mathrm{Rm}\|_2\) 小于耦合能量估计中实际出现的常数。

初始时刻可满足这些条件；整个时间区间内的保持尚未由笔记证明。

---

## 5. 整个支集上的 modified Li bootstrap

若严格得到

\[
\begin{aligned}
\dot R_\alpha+cX_\alpha
 &\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
      +\varepsilon_1Y_\alpha,\\
\dot P_\alpha+cY_\alpha
 &\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta,
\end{aligned}
\]

并有统一的邻接数，则取充分大的 \(\kappa\)，
\(H_\alpha=R_\alpha+\kappa P_\alpha\) 的确会满足有限邻域 Gronwall 估计，并在时间 \(\theta r^2\) 上产生 \(e^{C\theta}\) 因子。这个形式机制没有指数错误。

但 Step 17 并未从 cutoff 流完整推出上述系统，也没有从该系统推出点态曲率估计。主要数学问题是：

- \(a=\chi^2\) 在支集外缘趋于零，方程不是一致抛物型。标准 Li Theorem 3.4 不能直接应用。
- 初始最大函数控制 \(\int_{B_{4r}(p)}|\mathrm{Rm}|^2\)，但不能控制以 \(B_{4r}(p)\) 外缘附近点为中心、向外伸出的所有未加权 \(B_r\) 能量。
- \(\nabla^2a*E*\mathrm{Rm}\) 可在积分能量层面通过分部积分改写为含 \(\nabla a\) 的项，再用 \(X,Y\) 吸收；但点态 Moser 迭代与流的统一延拓还需要更细的 cutoff 正则性。仅有 Ricci 双侧控制并不给出统一的 \(|\nabla^2\chi|\)。
- 在 \(\chi\) 很小处，有效扩散时间约为 \(a\,t\)。因此整个 transition 上统一的未加权
  \[
  |\mathrm{Rm}|\le C/t
  \]
  一般不应成立。与局部 Ricci 流结构相容的是
  \[
  |a\,\mathrm{Rm}|\le C/t
  \]
  或在 \(\chi\ge c>0\) 的内层得到未加权估计。
- 耦合 \(L^2\) 持续性本身只给能量控制；从能量到点态估计还需要一个适用于退化系数 \(a\) 的加权 Moser 定理。

因此，“transition 项只增加 \(Cr^{-2}\) 线性增长率”在积分层面有合理推导方向，但它本身不足以得到文中所写的整个支集点态曲率结论。

---

## 6. 度量等价性

初始数据给出

\[
|E(0)|\le\delta.
\]

但不能据此写成整个时间区间上的

\[
|\partial_tg|=2a|E(t)|\le2\delta.
\]

缺陷方程虽然对 \(E\) 齐次，仍含有
\(\mathrm{Rm}*E\) 和 cutoff 导数项；齐次性保证 \(E\equiv0\) 保持为零，却不保证 \(\|E(t)\|_\infty\le\|E(0)\|_\infty\)。

此外，若仍采用 \(7r\) 分离而 transition 相交，则
\(a=\sum_j\chi_j^2\) 还可能大于 \(1\)，初始时刻的常数 \(2\delta\) 也要乘以重叠数。

度量等价性真正需要的是可积的加权点态估计，例如

\[
\|aE(t)\|_\infty
 \le C_p\delta\left(\frac{r^2}{t}\right)^{2/p},
 \qquad p>2.
\]

此时

\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
 \le C_{p,\theta}\delta r^2,
\]

从而通过

\[
\left|\partial_t\log g(t)(v,v)\right|
 \le2\|aE(t)\|_\infty
\]

得到统一度量等价性。Li 的 \(t^{-2/3}\) 指数也可积，并在标准流区域给出同类机制。

但 Ye Li 的 Theorem 3.4 与 Corollary 3.5 已经假设时间区间内的度量等价性和 Sobolev 控制。用它们先获得 \(E\) 的点态估计，再用该估计反过来建立度量等价性，必须通过一个同时推进的 continuation 论证，而当前笔记没有给出这种联合闭合。

文中另有一处同类问题：

\[
|s(t)+4|\le C\delta
\]

只在 \(t=0\) 直接成立。对 Li 的体积形式条件，可以考虑以
\(1+|\mathrm{Rm}|\) 作为标量控制函数，但不能把初始缺陷小量直接视为时间全程小量。

---

## 最终评定

六项中：

1. **可修正成立**：改为至少 \(8r_*\) 分离即可得到互不相交支集和固定比例的 bootstrap 区域。
2. **成立但常数推导需改写**：使用 \(B_{3r_*}(p)\) 可得到 \(\beta_5K_0r_*^4\)。
3. **未成立**：覆盖球可伸到 \(B_{7r_*/2}(p)\)，且 supremum 的中心集合不封闭。
4. **固定时刻的吸收代数成立**：必须使用相对 Sobolev 常数与 \(\chi\eta E\)、\(\chi\eta\mathrm{Rm}\)；脚本的塌缩处理不正确。
5. **尚缺完整抛物定理**：耦合能量的 Gronwall 形式合理，但未加权全支集 \(C/t\) 估计与退化系数不相容。
6. **存在循环依赖**：初始 \(\delta\) 不能直接控制全程 \(|E(t)|\)；需要先证明可积的加权点态缺陷估计。