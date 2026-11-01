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
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step17_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step17_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the support-scale-consistent cutoff-flow construction for the 4D negative LeBrun branch. The construction claims to resolve the quantifier mismatches from Step 16 by choosing ALL radii as fixed multiples of the Li scale r_*. The key mathematical claims to verify are: (1) The Vitali/thinning construction produces disjoint supports B_{4r_*}(p_j) whose plateaux B_{3r_*}(p_j) are separated, with a positive volume fraction of bootstrap domains B_{r_*}(p_j). (2) For every center y in B_{2r_*}(p_j), the maximal function at p_j controls the Li dimensionless quantity: epsilon_y(r_*) = r_*^4 * fint_{B_{r_*}(y)} |Rm|^2 <= C K_0 r_*^4 which is small for small r_*. (3) The Li covering argument (Theorem 3.4) works on the plateau B_{3r_*}(p_j) because all covering balls B_{r_*}(y_k) with y_k in B_{3r_*/2}(x) stay inside the plateau when x in B_{r_*}(p_j). (4) THE CRITICAL CLAIM: The 4D Sobolev-energy product C_S * ||Rm||_{L^2(support)} is O(r_*^2) and absorbs the cubic/defect reaction terms in BOTH the Rm energy inequality and the E energy inequality on the transition, even though |Rm| is not pointwise bounded there. This uses the 4D critical Sobolev embedding where the Sobolev constant C_S is dimensionless. (5) The modified Li bootstrap on the full support (including transition) closes because the transition terms add only a linear C r_*^{-2} growth rate, giving bounded exponential factor over time theta r_*^2. (6) Metric comparability holds because |partial_t g| = 2 chi^2 |E| <= 2 delta, and total drift over theta r_*^2 is O(delta r_*^2). Check all six claims for mathematical correctness. Identify any circularity, wrong exponent, missing hypothesis, or gap.

## Integrated Scientific Memo

# 核验结论

该固定支撑尺度方案**修复了初始尺度错配，但没有闭合 cutoff-flow 的过渡区分析**。六项结论如下：

1. **Vitali/稀疏化：可修正成立。**
2. **最大函数初始小能量：成立，体积比较常数需改写。**
3. **按现有 \(1,3,4\) 半径配置不成立；扩大 plateau 可修复纯几何包含，但不能单独解决过渡区。**
4. **四维吸收乘积的结论成立于某一已受控时刻，但笔记及脚本给出的非塌缩理由错误；沿流保持尚未证明。**
5. **全支撑 modified Li bootstrap 未证明；仅得到一个合理的耦合能量目标，不能推出全过渡区未加权 \(C/t\) 点态界。**
6. **度量等价性论证循环；\(|E(0)|\le\delta\) 不蕴含 \(|E(t)|\le\delta\)。**

因此 Step 17 尚不能推出该 LeBrun 临界族的反证结论，也不能推出全局终端缺陷
\(\int|E(t_0)|^2=O(\delta^2\operatorname{Vol}M)\)。

---

## 1. Vitali 与 thinning

设 \(r=r_*\)，并记

\[
\beta_m(r)=\frac{V_{-1}(mr)}{V_{-1}(r)}.
\]

从 \(G_i\) 中取极大两两不交的 \(B_r(p_j)\)，则

\[
G_i\subset\bigcup_j B_{5r}(p_j),
\qquad
\sum_j\operatorname{Vol}B_r(p_j)
\ge \beta_5(r)^{-1}\operatorname{Vol}(G_i).
\]

若 thinning 后中心间距至少 \(Lr\)，每个被舍弃的 \(B_r(q)\) 均包含在某个保留中心的 \(B_{(L+1)r}(p)\) 内。因原球两两不交，

\[
\sum_{\text{归属于 }p}\operatorname{Vol}B_r(q)
\le \operatorname{Vol}B_{(L+1)r}(p)
\le \beta_{L+1}(r)\operatorname{Vol}B_r(p).
\]

故保留的 bootstrap 球仍占固定正体积比例。

但须区分两个分离要求：

- \(d(p_j,p_k)>7r\) 只保证
  \[
  B_{3r}(p_j)\cap B_{4r}(p_k)=\varnothing;
  \]
- 若声称支撑 \(B_{4r}(p_j)\) 两两不交，则需
  \[
  d(p_j,p_k)\ge8r
  \]
  （闭包严格分离可加固定余量）。

所以原文“disjoint supports”和“plateau 不遇到其他 support”混为一谈。若需要真正独立支撑，应取 \(L=8\)，相应 thinning 损失为 \(\beta_9(r)\)。此外 \(625,4096\) 只是 \(r\to0\) 的渐近值，不是固定正 \(r\) 下的精确常数。

---

## 2. 最大函数初始控制

若 \(p\in G_i\) 且 \(y\in B_{2r}(p)\)，则

\[
B_r(y)\subset B_{3r}(p).
\]

因此直接使用半径 \(3r\) 的最大函数界：

\[
\int_{B_r(y)}|\mathrm{Rm}|^2
\le K_0\operatorname{Vol}B_{3r}(p).
\]

又 \(B_{3r}(p)\subset B_{5r}(y)\)，所以

\[
\fint_{B_r(y)}|\mathrm{Rm}|^2
\le K_0\beta_5(r),
\]

从而

\[
\epsilon_y(r)
=r^4\fint_{B_r(y)}|\mathrm{Rm}|^2
\le \beta_5(r)K_0r^4.
\]

故该量可通过选取足够小的固定 \(r\) 压到 Li 阈值以下。

原文若坚持先估计 \(B_{4r}(p)\)，则因 \(B_{4r}(p)\subset B_{6r}(y)\)，常数应是 \(\beta_6\)，不是 \(\beta_5\)。脚本中的显式公式也应改成带余量的不等式，因为 \(\beta_5(r)\) 本身依赖 \(r\)。

---

## 3. Plateau 上的 Li covering

现有半径配置为

\[
D=B_r(p),\qquad \Pi=B_{3r}(p),\qquad \Omega=B_{4r}(p).
\]

对 \(x\in D\)，Li 覆盖中心满足

\[
y_k\in B_{3r/2}(x)\subset B_{5r/2}(p),
\]

但其覆盖球只满足

\[
B_r(y_k)\subset B_{7r/2}(p),
\]

并不包含于 \(B_{3r}(p)\)。因此“所有 covering balls 留在 plateau”是错误的。

此外，原定义

\[
e(t)=\sup_{y\in B_{2r}(p)}
\left(\int_{B_r(y)}|\mathrm{Rm}|^2\right)^{1/2}
\]

也不能控制可能位于 \(B_{5r/2}(p)\) 的覆盖中心。扩大 supremum 后，对扩大区域外缘球求导又会调用更外层球；这正是尚未解决的内外层闭合问题。Li 定理本身使用全流形 supremum，并假设整个时间区间内度量等价和统一 Sobolev 不等式，不能仅凭中心位于 plateau 内直接局部化。

纯几何问题可以通过重新选半径修复，例如取

\[
D=B_r(p),\qquad \{\chi=1\}\supset B_{4r}(p),\qquad
\operatorname{supp}\chi\subset B_{5r}(p).
\]

这样上述 \(B_r(y_k)\subset B_{7r/2}(p)\) 确实处于 plateau 内；随后必须相应增大中心分离常数。但这只修复 plateau 内层，不证明整个 transition 的 cutoff flow。

在 plateau 上方程是局部标准 normalized Ricci flow；并不存在“transition 通过额外局部张量项耦合进入 plateau 方程”。真正困难是抛物能量传播需要邻域数据，而 Ricci flow 没有有限传播速度。

---

## 4. 四维 Sobolev–能量乘积

### 正确的塌缩相容计算

设 \(U=B_{4r}(p)\)，\(V=\operatorname{Vol}U\)。初始最大函数给出

\[
\|\mathrm{Rm}\|_{L^2(U)}\le (K_0V)^{1/2}.
\]

Li 所用的相对 Sobolev 常数满足

\[
\left(\int_U |f|^4\right)^{1/2}
\le A_U\int_U|\nabla f|^2,
\qquad
A_U\le C\left(\frac{(4r)^4}{V}\right)^{1/2}.
\]

故

\[
A_U\|\mathrm{Rm}\|_{L^2(U)}
\le C\sqrt{K_0}\,(4r)^2
=O(\sqrt{K_0}\,r^2).
\]

体积 \(V\) 在这里**精确消去**。这才是塌缩情形下正确的四维机制。

脚本将 \(C_S=2\) 并代入欧氏球体积，不能验证塌缩情形。临界 Sobolev 常数虽然在尺度缩放意义下无量纲，却可在塌缩时按 \(r^2/\sqrt V\) 墑大；它不必接近欧氏常数。

### 必须使用加权测试函数

缺陷反应项应写成

\[
\begin{aligned}
\int a\eta^2|\mathrm{Rm}|\,|E|^2
&=\int |\mathrm{Rm}|\,|\chi\eta E|^2\\
&\le \|\mathrm{Rm}\|_2\|\chi\eta E\|_4^2\\
&\le A_U\|\mathrm{Rm}\|_2
       \int|\nabla(\chi\eta E)|^2.
\end{aligned}
\]

展开得

\[
\int|\nabla(\chi\eta E)|^2
\le C\int a\eta^2|\nabla E|^2
 +C\int\!\left(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2\right)|E|^2.
\]

这与退化耗散 \(\int a|\nabla E|^2\) 匹配。直接使用
\(\|E\|_4^2\le A_U\|\nabla E\|_2^2\) 会产生未加权梯度，而 \(a\to0\) 处没有相应耗散。

曲率三次项同理：

\[
\int a\eta^2|\mathrm{Rm}|^3
\le A_U\|\mathrm{Rm}\|_2
   \int|\nabla(\chi\eta|\mathrm{Rm}|)|^2.
\]

因此吸收代数在某个受控时刻成立，但沿时间区间使用它还需同时保证：

- 当前局部 \(L^2\) 曲率仍小；
- 当前相对 Sobolev 不等式保持；
- 当前度量等价及覆盖常数保持；
- \(|\nabla\chi|\) 及所需 cutoff 正则性保持。

这些正是未证明的 continuation package。

另一个尺度修正是 Corollary 3.5 中

\[
A_U^{2/3}\operatorname{Vol}(U)^{1/3}=O(r^{4/3}),
\]

不是简单的 \(O(1)\)。在 \(t=\theta r^2\) 时，它与 \(t^{-2/3}\) 抵消，最终仍给出 \(O(\delta)\)，所以终端尺度结论本身可保留。

---

## 5. 全支撑 modified Li bootstrap

若能严格证明有限重叠覆盖上的耦合系统

\[
\begin{aligned}
\dot R_\alpha+cX_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
+\varepsilon_1Y_\alpha,\\
\dot P_\alpha+cY_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta,
\end{aligned}
\]

则对适当 \(\kappa\)，\(H_\alpha=R_\alpha+\kappa P_\alpha\) 确实满足线性有限邻域 Gronwall 界。时间为 \(\theta r^2\) 时指数因子为

\[
\exp(Cr^{-2}\theta r^2)=e^{C\theta},
\]

所以这里没有指数或尺度错误。

但 Step 17 没有证明上述系统在整个存在区间有效，也没有从该 \(L^2\) 系统推出点态曲率界。关键缺口为：

1. \(a=\chi^2\) 在外缘趋于零，方程非一致抛物；
2. Li Theorem 3.4 不直接适用于该退化 cutoff 方程；
3. \(\nabla^2a*E\) 项虽可能通过分部积分在能量层面改写，但点态 Moser 迭代和延拓还需 cutoff Hessian/导数控制；
4. \(L^2\) 能量持续性本身不蕴含点态 \(C/t\)；
5. 在 \(a\ll1\) 区域，有效扩散时间约为 \(at\)，因此整个 transition 上统一未加权
   \[
   |\mathrm{Rm}|\le C/t
   \]
   一般不应期待。自然目标是
   \[
   |a\,\mathrm{Rm}|\le C/t,
   \]
   或仅在 \(\chi\ge c>0\) 的内层得到未加权界。

故“transition 只加入 \(Cr^{-2}\) 线性增长率”至多是耦合积分估计的合理目标，尚不足以证明全支撑 smoothing。

---

## 6. 度量等价性与循环依赖

初始条件只给出

\[
|E(0)|\le\delta.
\]

它不能推出时间区间上

\[
|\partial_tg|=2a|E(t)|\le2\delta.
\]

缺陷方程对 \(E\) 齐次只意味着 \(E\equiv0\) 是保持解；它不提供
\(\|E(t)\|_\infty\le\|E(0)\|_\infty\) 的最大值原理，因为存在
\(\mathrm{Rm}*E\) 及 cutoff 导数反应项。若 transition 支撑还相交，则 \(a=\sum\chi_j^2\) 甚至可能大于 \(1\)。

真正足够的输入是可积的加权点态界，例如

\[
\|aE(t)\|_\infty
\le C_p\delta\left(\frac{r^2}{t}\right)^{2/p},
\qquad p>2.
\]

于是

\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C_{p,\theta}\delta r^2,
\]

并由

\[
\left|\partial_t\log g(t)(v,v)\right|
\le2\|aE(t)\|_\infty
\]

得到度量漂移 \(O(\delta r^2)\)。

当前论证的循环是：

\[
\text{Sobolev/吸收}
\Rightarrow \text{曲率与缺陷点态界}
\Rightarrow \text{度量等价}
\Rightarrow \text{Sobolev/覆盖保持}.
\]

Li 的定理已经把度量等价和随时间有效的 Sobolev 不等式作为假设，不能用其结论反过来无条件建立这些假设。需要一个联合 continuation 论证或新的 transition-inclusive 加权 Moser 定理。

---

## 精确剩余对象

需要证明一个塌缩相容、有限重叠、相对 Sobolev 的 cutoff-flow continuation 定理，它从实际初始数据同时推出：

\[
\sup_\alpha R_\alpha(t)\le2\varepsilon,\qquad
|a\,\mathrm{Rm}(t)|\le C/t,
\]

\[
\|aE(t)\|_\infty
\le C_p\delta(r^2/t)^{2/p},\quad p>2,
\]

以及度量等价、相对 Sobolev/覆盖常数和 cutoff 导数控制。现有 Li 来源处理标准 Ricci flow，并明确依赖时间区间内的度量等价与 Sobolev 假设；它不提供该退化 cutoff continuation theorem。

所以六项中只有 (1)、(2) 可直接修正完成，(3) 可通过扩大 plateau 修复其几何部分，(4) 的静态吸收机制正确；(5)、(6) 仍是决定性的未解分析缺口。