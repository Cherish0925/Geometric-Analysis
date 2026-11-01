# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md",
    "Sessions/S0910A01/workspace/notes/step15_cutoff_smoothing_architecture.md",
    "Sessions/S0910A03/workspace/notes/step14_cutoff_smoothing_and_cor35_reconstruction.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Read the corrected smoothing-route files and assess the transition-inclusive cutoff-flow stability problem as mathematics. The goal is not final approval; determine whether the proposed weighted energy route can plausibly yield, on a support of radius comparable to the Li scale, (i) persistence of local normalized L2 curvature energy and interior |Rm|<=C/t, and (ii) global or support-summed Einstein-defect control Q(t0)/A->0 for the near-Einstein LeBrun critical sequence. Explicitly account for Ricci flow having no finite propagation speed, for Li's supremum/covering quantifiers, for cutoff transition terms in the E equation, for the difference between pointwise E control and the weaker normalized L2 target, and for what existing Li/Yang/Wang statements actually supply. Give a direct scientific memo: viable proof skeleton, obstruction terms, exact hypotheses still needed, and whether any part of Step 15's completed-chain wording survives after Step 16.

## Output

# 科学复核备忘录：过渡环参与的 cutoff-flow 稳定性

## 总体判断

在支撑半径取为 Li 尺度 \(r_*\) 的固定倍数后，weighted energy 路线具有相容的四维缩放结构。它不依赖任何有限传播性质，而是把平台、过渡环和冻结外部统一纳入支撑上的能量估计。

其中两部分的数学成熟度不同：

1. **Einstein 缺陷的 \(L^2\) 控制具有很好的闭合结构。**  
   一旦局部 \(L^2\) 曲率能量在流中保持小量，A03 已推导的 \(E=\operatorname{Ric}+g\) 齐次方程和积分恒等式可给出
   \[
   q_j(t)\le Cq_j(0)
   \]
   于每个支撑；对互不相交的支撑求和，再加上冻结外部，即得到
   \[
   Q_i(t_0)/A_i\to0.
   \]
   这里无需在过渡环证明全局逐点 \(E=O(\delta_i)\)。

2. **曲率能量保持与内区 \(|\operatorname{Rm}|\le C/t\) 需要一个尚未出现在所引文献中的局部 normalized-LRF 定理。**  
   Wang/Yang 的能量计算提供了非常接近的模型；Li 提供了临界吸收和 Moser 部分。但 Li 的全流形 supremum 不能直接截取到平台，Wang/Yang 的现成陈述也不是
   \[
   \partial_tg=-2\chi^2(\operatorname{Ric}+g)
   \]
   且未直接给出多个坍缩支撑上的求和版本。

目前未见由缩放或符号导致的根本冲突；真正需要建立的是支撑整体上的 weighted curvature theorem，而不是“过渡环在短时间内尚未影响内区”。

---

## 1. 尺度一致的静态输入是成立的

令 \(r=r_*\)。一种干净的选取方式是对好点族的球 \(B_{16r}(p)\) 使用 Vitali，得到两两不交的 \(B_{16r}(p_j)\)，并有

\[
G_i\subset\bigcup_j B_{80r}(p_j).
\]

可取

\[
\chi_j=1\quad\text{于 }B_{8r}(p_j),\qquad
\operatorname{supp}\chi_j\subset B_{12r}(p_j),
\]

再取 \(\zeta_j=1\) 于 \(B_{12r}(p_j)\)、支撑于 \(B_{16r}(p_j)\)。只需要

\[
|d\chi_j|+|d\zeta_j|\le Cr^{-1}.
\]

从仅有 Ricci 控制的数据不能推出统一的 \(|\nabla^2\chi_j|\le Cr^{-2}\)。因此所有 Hessian-cutoff 项都必须通过分部积分消去；A03 的 \(E\)-能量恒等式已经实现了这一点，Wang 的 LRF 曲率能量计算也采用同一机制。

若

\[
\mathcal M_{R_0}(|\operatorname{Rm}|^2)(p_j)\le K_0,\qquad 17r\le R_0,
\]

则

\[
\int_{B_{16r}(p_j)}|\operatorname{Rm}|^2
\le K_0\operatorname{Vol}(B_{16r}(p_j)).
\]

对任意 \(y\in B_{12r}(p_j)\)，球包含关系和 Bishop–Gromov 给出

\[
r^4\fint_{B_r(y)}|\operatorname{Rm}|^2
\le C(12)K_0r^4.
\]

这修复了 Step 15 中 \(r\ll\rho\) 时的量词错配。另一方面，

\[
\sum_j\operatorname{Vol}(B_{8r}(p_j))
\ge c\,\operatorname{Vol}(G_i)
\]

由 \(G_i\subset\bigcup B_{80r}(p_j)\) 和同心球体积比较得到。因此平台仍占固定体积比例，只是所有半径都必须是 \(r\) 的固定倍数。

---

## 2. 支撑整体曲率能量是正确的闭合对象

对第 \(j\) 个支撑定义

\[
F_j(t)=\int \zeta_j^2|\operatorname{Rm}|^2\,d\mu_t,
\qquad
q_j(t)=\int \zeta_j^2|E|^2\,d\mu_t.
\]

相对 Sobolev 不等式可写成

\[
\|u\|_4^2
\le S_j\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\qquad
S_j\le C\frac{r^2}{\operatorname{Vol}(B_{16r}(p_j))^{1/2}}.
\]

初始曲率能量满足

\[
S_jF_j(0)^{1/2}
\le Cr^2K_0^{1/2}.
\]

因此选择固定小 \(r\) 后，这个量可低于临界吸收常数，与球体积多小无关。这正是四维坍缩消去机制。

### 预期的曲率能量不等式

对 normalized cutoff flow

\[
\partial_tg=-2aE,\qquad a=\chi_j^2,
\]

曲率变分包含

\[
a\Delta\operatorname{Rm},\quad
a\,\operatorname{Rm}*\operatorname{Rm},\quad
da*\nabla E,\quad
\nabla^2a*E,
\]

以及归一化产生的低阶项。由于 \(\nabla E=\nabla\operatorname{Ric}\) 是 \(\nabla\operatorname{Rm}\) 的收缩，且

\[
da=2\chi\,d\chi,
\]

Hessian 项分部积分后应得到如下形式：

\[
\begin{aligned}
\frac d{dt}F_j
+c\int\zeta_j^2a|\nabla\operatorname{Rm}|^2
\le{}&
Cr^{-2}(F_j+q_j)\\
&+C\int\zeta_j^2a|\operatorname{Rm}|^3 .
\end{aligned}
\tag{2.1}
\]

是否出现 \(Cr^{-2}q_j\) 取决于曲率张量的具体型别和归一化整理；它对当前序列无害。关键是不能出现与 \(E\) 无关的体积源，而且不能留下依赖 \(\|\nabla^2\chi\|_\infty\) 的常数。

临界项满足

\[
\begin{aligned}
\int\zeta_j^2a|\operatorname{Rm}|^3
&\le F_j^{1/2}\|\zeta_j\chi_j\operatorname{Rm}\|_4^2\\
&\le S_jF_j^{1/2}
\left[
C\int\zeta_j^2a|\nabla\operatorname{Rm}|^2
+Cr^{-2}F_j
\right].
\end{aligned}
\]

若 \(S_jF_j^{1/2}\le\varepsilon_0\)，梯度项可被吸收，故

\[
F_j'(t)\le Cr^{-2}(F_j+q_j).
\]

这说明支撑整体而不是内区 supremum 是自然的闭合量。

### 与 Li supremum 的关系

Li Theorem 3.4 使用

\[
e_0(t)=\sup_{x\in M}\left(\int_{B_r(x)}f^2\right)^{1/2}
\]

并在估计 \(B_r(x)\) 时用 \(B_{2r}(x)\) 的覆盖中心。若 supremum 只取内区，覆盖中心会落入更外层；有限次增加缓冲层仍会在最外层重新遇到同一问题。

式 (2.1) 若成立，就不再需要用有限传播来解决这个量词链：整个活动支撑的能量已经受控。之后在 \(B_{8r}(p_j)\) 内使用 Li 的 Moser 部分时，所需的动态 \(L^2\) 输入由 \(F_j(t)\) 提供，而不是由一个未闭合的内区 supremum 提供。

---

## 3. Ricci flow 没有有限传播速度

即使 \(\chi=1\) 于平台，平台与过渡环在任意正时间都已通过抛物方程耦合。平台上的方程与标准 normalized Ricci flow 相同，仅表示局部微分算子相同；它不表示解只由平台初始数据决定。

精确 cutoff flow 确实使 \(\{\chi=0\}\) 上的度量冻结，但其科学作用是：

- 外部能量不随时间变化；
- 活动支撑之间若彼此不交，积分可以分别求和；
- 过渡项只出现于固定环带，并显式带有 \(d\chi\)。

它不使过渡环对平台不可见。上述支撑整体估计正是对这种即时耦合的处理。

以 \(\chi_\varepsilon\ge\varepsilon\) 正则化也不能自动提供所需统一常数：此时外部不再冻结，高曲率区域通过正扩散系数参与流动。除非有与 \(\varepsilon\) 一致的 weighted estimates，否则该正则化不足以替代 Yang 型退化 LRF 存在理论。

---

## 4. Einstein 缺陷能量具有三角闭合结构

A03 已验证

\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]

且 \(\mathcal C_a(E)\) 每项都含 \(E\)、\(\nabla E\) 或其迹。积分后有

\[
\begin{aligned}
\frac d{dt}q_j
+c\int\zeta_j^2a|\nabla E|^2
\le{}&
Cr^{-2}q_j\\
&+C\int\zeta_j^2a|\operatorname{Rm}|\,|E|^2.
\end{aligned}
\tag{4.1}
\]

这里最重要的事实是右侧没有仅依赖曲率而与 \(E\) 无关的加性项。恒等式

\[
\frac{|da|^2}{a}=4|d\chi|^2
\]

消除了 \(1/\chi\) 型奇异系数。

曲率势能项满足

\[
\begin{aligned}
\int\zeta_j^2a|\operatorname{Rm}|\,|E|^2
&\le F_j^{1/2}\|\zeta_j\chi_jE\|_4^2\\
&\le S_jF_j^{1/2}
\left[
C\int\zeta_j^2a|\nabla E|^2
+Cr^{-2}q_j
\right].
\end{aligned}
\]

因此，一旦曲率 bootstrap 给出 \(S_jF_j^{1/2}\le\varepsilon_0\)，式 (4.1) 化为

\[
q_j'(t)\le Cr^{-2}q_j(t),
\]

从而在 \(0\le t\le\theta r^2\) 上

\[
q_j(t)\le e^{C\theta}q_j(0).
\tag{4.2}
\]

这比把 \(F_j+\gamma q_j\) 粗略合并更合适，因为粗略合并会丢掉 \(q_j(0)\) 中的 \(\delta_i^2\) 小因子。

---

## 5. 支撑求和足以得到 \(Q_i(t_0)/A_i\to0\)

初始逐点条件给出

\[
q_j(0)\le \delta_i^2\operatorname{Vol}(B_{16r}(p_j)).
\]

由于扩大的支撑两两不交，式 (4.2) 求和后得到

\[
\sum_j q_j(t_0)
\le C\delta_i^2\operatorname{Vol}(M_i,g_i).
\]

活动支撑外度量完全冻结，故那里 \(E\) 不变。因此

\[
Q_i(t_0)
=\int_{M_i}|E_i(t_0)|^2
\le C\delta_i^2\operatorname{Vol}(M_i,g_i).
\]

利用临界 LeBrun 序列中 \(\operatorname{Vol}(M_i)/A_i=O(1)\)，可得

\[
\boxed{\frac{Q_i(t_0)}{A_i}\to0.}
\]

又因为

\[
\mathring{\operatorname{Ric}}=E^\circ,\qquad
J_i(t_0)
=\frac1{8\pi^2}\int|\mathring{\operatorname{Ric}}|^2
\le\frac{Q_i(t_0)}{8\pi^2},
\]

这正好提供 Step 16 所需的拓扑重新标定输入。

### 逐点控制与 \(L^2\) 目标的区别

Li Corollary 3.5 在内平台、并已有完整动态曲率包时，可给出

\[
|E(x,t)|\le
C\delta_i\left(\frac{r^2}{t}\right)^{2/3}.
\]

但该结论适用于普通热算子形式；它没有处理过渡环中的退化系数和 \(d\chi\) 项。因此它不能直接产生全局逐点 \(E=O(\delta_i)\)。

对于拓扑重新标定，这种全局逐点结论并非必需；式 (4.2) 已足够。不过，仅有 \(Q(t)\) 也不能自行保证度量一致性，因为

\[
\partial_tg=-2aE
\]

需要时间可积的逐点速度估计。这是另一个输入。

---

## 6. 度量一致性可望由 Wang 型 weighted Ricci 估计提供

设 Wang 记号中的 Sobolev 常数满足

\[
\|u\|_4\le A_{0,j}\|\nabla u\|_2,\qquad
A_{0,j}^2\asymp S_j.
\]

则

\[
A_{0,j}\lesssim
\frac{r}{\operatorname{Vol}(B_{16r}(p_j))^{1/4}}.
\]

初始 \(|\operatorname{Ric}|\le C\)，故任取 \(p>2\),

\[
\|\operatorname{Ric}(0)\|_{L^p(B_{16r})}
\le C\operatorname{Vol}(B_{16r})^{1/p}.
\]

Wang Theorem 6.3 的形式给出

\[
\|\chi^2\operatorname{Ric}(t)\|_\infty
\lesssim
A_0^{4/p}t^{-2/p}\|\operatorname{Ric}(0)\|_p
\lesssim r^{4/p}t^{-2/p}.
\]

体积因子再次消去，于是

\[
\int_0^{\theta r^2}
\|\chi^2\operatorname{Ric}(t)\|_\infty\,dt
\le Cr^2\theta^{1-2/p}.
\]

归一化项 \(\chi^2g\) 贡献也是 \(O(r^2)\)。因此可得到与坍缩无关的固定倍数度量一致性。这个估计不带 \(\delta_i\)，但它只承担 Sobolev 和固定球结构的保持；\(\delta_i\) 小量由齐次 \(q_j\) 方程保存。

Wang 的现成定理针对 \(-2\chi^2\operatorname{Ric}\)，所以把上述估计用于 \(-2\chi^2E\) 仍需验证低阶项不会改变指数和 lifespan。其缩放完全相容，但这一步不在已供应的原文中。

---

## 7. 从动态 \(L^2\) 能量到内平台 \(C/t\)

若已经具有：

\[
F_j(t)\le CF_j(0),\qquad
S_jF_j(t)^{1/2}\le\varepsilon_0,
\]

并且度量一致、Dirichlet Sobolev 常数保持，那么在 \(\chi=1\) 的内平台上

\[
(\partial_t-\Delta)|\operatorname{Rm}|
\le C(|\operatorname{Rm}|^2+|\operatorname{Rm}|).
\]

Li Theorem 3.4 的临界吸收与 Moser 迭代可局部运行，得到

\[
|\operatorname{Rm}|(x,t)
\le C\left(t^{-1}+r^{-2}\right)
\le \frac{C_\theta}{t},
\qquad
x\in B_{4r}(p_j),\quad0<t\le\theta r^2.
\]

这里 Li 的作用是从已保持的动态能量提升至逐点曲率，而不是负责过渡环和支撑外部的能量保持。Wang Theorem 6.3 的 \(|\chi^2\operatorname{Rm}|\le C/t\) 也可承担同一提升，但同样需要局部支撑版本和归一化适配。

---

## 8. 现有来源实际提供的内容

### Ye Li

- Theorem 3.1 明确要求所有中心 \(x\in M\) 的初始临界小能量。
- Theorem 3.6 继承这一全中心量词。
- Theorem 3.4 通过全流形 supremum、覆盖和 continuation 保持动态 \(L^2\) 能量。
- Corollary 3.5 可在普通 Ricci flow 的动态包已建立后传播线性曲率势能方程。
- 原文 Corollary 3.5 中未定义的 \(\phi^2\) 与 Theorem 2.5 及后续应用不一致；A03 对其按普通热方程读取是有依据的，但它不是 cutoff-transition 定理。

因此 Li 不直接提供当前所需的 normalized cutoff-flow stability theorem。

### Yang/Wang

- Yang 的 LRF 给出退化方程 \(\partial_tg=-2\chi^2\operatorname{Ric}\) 的存在理论。
- Wang 的能量式
  \[
  \frac d{dt}\int|\operatorname{Rm}|^2
  +c\int|\nabla(\chi|\operatorname{Rm}|)|^2
  \le C|d\chi|_\infty^2\int|\operatorname{Rm}|^2
  \]
  正是过渡环参与而不依赖有限传播的模型。
- Wang Theorem 6.3 还给出 weighted Ricci、weighted curvature 的逐点估计。

但其书面假设使用活动域上的统一 Sobolev 与整体 \(L^{n/2}\) 能量，并处理 unnormalized LRF。把它用于当前多个坍缩球，需要一个明确的 Dirichlet 支撑版本；把 Ricci 替换为 \(E\) 还需要低阶项计算。文献目前提供证明机制，而非可原样引用的最终定理。

---

## 9. 所需定理的精确数学内容

能够闭合上述路线的局部定理需包含：

1. 嵌套区域 \(B_{4r}\subset B_{8r}\subset\operatorname{supp}\chi\subset B_{12r}\subset B_{16r}\)；
2. 仅依赖 \(|d\chi|\le Cr^{-1}\) 的 normalized LRF 存在时间 \(T\ge\theta r^2\)；
3. Dirichlet Sobolev 常数与固定初始球在流中的可比性；
4. 支撑整体曲率能量不等式 (2.1)，所有 \(\nabla^2\chi\) 项均经分部积分化为 \(r^{-2}\) 项；
5. \(S_jF_j(0)^{1/2}\le\varepsilon_0\) 推出 \(F_j(t)\le CF_j(0)\)；
6. 时间可积的 \(\|\chi^2E\|_\infty\) 估计，以保证度量一致；
7. 内平台 \(|\operatorname{Rm}|\le C/t\)；
8. 齐次缺陷估计 \(q_j(t)\le Cq_j(0)\)，常数与坍缩体积及支撑数目无关。

这些陈述一旦成立，曲率部分和 \(Q/A\) 部分在数学上可以组成完整的 smoothing bridge。

---

## 10. Step 15 完成性语言的复核结果

以下成分继续成立：

- 好点附近、同尺度所有中心的初始小能量；
- 四维 Sobolev–energy 体积消去；
- cutoff \(E\) 方程的精确齐次性；
- 条件于 \(Q_i(t_0)/A_i\to0\) 的拓扑重新标定；
- 条件于受控 cover 极限的 Derdziński 局部矛盾。

以下 Step 15 表述没有得到现有推导支持：

- “平台上的标准流不受过渡环影响”；
- 直接把 Li 的全中心 supremum 截取到平台；
- 由冻结外部推出全局逐点 \(E=O(\delta_i)\)；
- 以 \(\chi_\varepsilon\) 正则化自动获得与 \(\varepsilon\) 一致的局部估计；
- 由平台有界曲率直接得到所需固定体积比例的 buffered normal covers；
- 四维 Ric\(=-g\) LeBrun 临界序列的完整反证链已经完成。

即使 weighted cutoff theorem 建立，bounded-curvature 到 normal-cover accessibility 仍是独立的几何命题。因而 Step 15 中可保留的是若干严密组件和一个条件性架构，而不是完成性表述。