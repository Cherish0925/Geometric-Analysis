# TTCS Independent Branch Record

```json
{
  "step_id": 41,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step41_continuation_criterion_and_first_exit_assembly.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step37_transported_deturck_existence.md",
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md"
  ]
}
```

## Task

Verify the continuation criterion (Theorem 3.1) and its application to the first-exit bootstrap, as stated in the Step 41 note. The key claims are:

1. Given a smooth solution of dt g = -2a(Ric+g) on [0,T*) with |U| = |a(Rm+G)| ≤ K and T* < ∞, the solution extends smoothly past T*. The proof uses: (a) metric equivalence from bounded velocity, (b) the Step 40 staggered L^p induction giving all derivative bounds, (c) Sobolev + Kato for pointwise bounds, (d) Arzelà-Ascoli for terminal convergence, (e) restart from the Step 37 DeTurck existence.

2. The first-exit bootstrap closes on the actual maximal interval. The curvature Moser gives |U(t)| ≤ Cγ/t + C for t > 0, which combined with the smooth initial data gives sup_{[0,T*)} |U| < ∞ when T* < ∞, hence T_max = ∞ by the continuation criterion.

Check carefully: (i) Is the argument from L^p bounds to pointwise bounds (Step C) correct for all m? Does the Kato inequality handle tensor norms properly? (ii) Is the terminal convergence (Step E) correct for this degenerate equation where the diffusion degenerates at χ=0? (iii) In the first-exit closure, the curvature endpoint |aF(t)| ≤ Cγ/t gives |U(t)| bounded only for t > 0 — does the argument properly handle the initial time t=0? (iv) Is there a gap between the per-datum continuation (which uses constants depending on the specific smooth solution) and the sequence-uniform estimates needed for the gap theorem?

## Output

## 科学核验备忘

### 总体结论

Theorem 3.1 的核心蕴含关系成立：

\[
\sup_{M\times[0,T_*)}|U|<\infty
\quad+\quad
\text{Step 40 的全阶一致 }L^p\text{ 估计}
\quad+\quad
\text{Step 37 的重启定理}
\]

确实推出 \(g(t)\) 在有限 \(T_*\) 处具有光滑极限并可向后延拓。退化系数 \(a=\chi^2\) 在这一终端步骤中不会造成新的困难，因为此时依赖的是速度张量及其全部空间导数，而不是统一抛物性。

不过，Step 41 的文字还略过了固定坐标导数转换、时间方向拼接和非线性唯一性；Step 40 的任意阶部分仍以示意演化式记载。因此，当前材料严格证明的是“在 Step 40 全阶估计与 Step 37 重启/唯一性成立的前提下”的续流结果。

第一退出论证中，从 \(|aF(t)|\le C\gamma_0/t\) 处理 \(t=0\) 没有问题；真正未闭合的是：所列改善只在 \(t\le\theta\) 上控制度量漂移，并且 (5.3) 尚未给出 H3、H4 所需的严格改善。因此，“到达任意给定有限观察时刻 \(\theta\)”与“\(T_{\max}=\infty\)”目前没有被同一组估计连接起来。

---

## 1. 有界 \(U\) 推出度量等价

Lemma 2.1 的结论正确，但证明中的“有界速度积分得到加法估计，因而双 Lipschitz”等表述应改为乘法估计。令 \(v=\partial_tg\)。由于

\[
v=-2\operatorname{Ric}(U),\qquad |v|_{g(t)}\le C_nK,
\]

对任意固定切向量 \(X\neq0\),

\[
\left|\frac{d}{dt}\log g(t)(X,X)\right|
 =\frac{|v(X,X)|}{g(X,X)}
 \le C_nK.
\]

故

\[
e^{-C_nKt}g_0\le g(t)\le e^{C_nKt}g_0.
\]

这直接给出正定性、体积比较以及标量 Sobolev 常数的统一控制。后者的常数还依赖 \((M,g_0)\) 的 Sobolev 常数；不能只写成 \(C(n,K,T_*)\)。

---

## 2. 从全阶 \(L^p\) 到逐点导数估计

这一步正确。对任意随 \(t\) 变化的光滑张量 \(S\)，弱 Kato 不等式成立：

\[
|d|S||\le |\nabla S|
\]

在 \(S=0\) 处按弱导数理解。取 \(q>n\)，在闭流形上使用统一的标量嵌入 \(W^{1,q}\hookrightarrow C^0\)，得到

\[
\|S\|_\infty
\le C\bigl(\|S\|_{L^q}+\|\nabla S\|_{L^q}\bigr).
\]

分别取

\[
S=U_m,\qquad S=C_{m+1},\qquad S=T_m
\]

便得到所需逐点估计。指标上没有循环：

- \(U_m\) 使用 \(U_{m+1}\)；
- \(C_{m+1}\) 使用 \(C_{m+2}\)；
- \(T_m\) 使用 \(T_{m+1}\)；

这些都由下一空间阶的 Step 40 结果提供。由于先取得所有阶的有限 \(L^q\) 估计，再逐阶应用 Sobolev，因此逻辑顺序是三角形的。

需要保留的依赖是：Step 40 的 (1.4)、(1.5) 中 \(\mathcal G_m,\mathcal N_m\) 目前只被描述为具有合适的最高阶结构，尚未逐项导出。因而 (3.2) 在现有文件中仍是任意阶示意张量演算，而不是完全展开的独立证明。低阶 \(m=2\) 的修复是具体的，任意阶结论还依赖该结构描述确实覆盖所有交换子与联络变分项。

---

## 3. 固定坐标中的光滑终端极限

由

\[
\nabla^m v=-2\nabla^m\operatorname{Ric}(U)
\]

以及 \(\nabla g^{-1}=0\)，实际上有

\[
|\nabla^m v|\le C_{n,m}|U_m|,
\]

所以移动联络下的全部速度导数一致有界。Step E 还需补入从移动联络到固定坐标的标准归纳。

令

\[
A(t)=\nabla^{g(t)}-\nabla^{g_0}.
\]

联络变分公式为

\[
(\partial_tA)^k{}_{ij}
=\frac12g^{k\ell}
\left(\nabla_i v_{j\ell}
+\nabla_j v_{i\ell}
-\nabla_\ell v_{ij}\right).
\]

因此 \(A\) 一致有界。对该公式施加 \((\nabla^{g_0})^r\)，并利用

\[
\nabla^{g_0}=\nabla^{g(t)}+A*
\]

作归纳，可得所有 \((\nabla^{g_0})^rA\) 一致有界，继而得到

\[
\sup_{t<T_*}\|v(t)\|_{C^r(g_0)}<\infty
\qquad\text{对每个 }r.
\]

于是

\[
\|g(t)-g(s)\|_{C^r(g_0)}
\le C_r|t-s|,
\]

所以整个族而不只是某个子列在 \(C^\infty\) 中收敛到唯一的 \(g_*\)。前述指数型度量比较保证 \(g_*\) 正定。

退化扩散在这里无影响：终端收敛只使用 \(v\) 的全阶控制。特别地，在 \(\chi=0\) 的开集上速度本来就是零；在支集过渡区，全阶控制已经由 \(U=aT\) 的估计承担。

Step E 中“所有空间和时间导数直接由 (3.4) 有界”略强于已写出的论证。空间导数需要上述 \(A(t)\) 归纳；高阶时间导数则可由自治方程

\[
\partial_tg=\mathcal F(g):=-2a(\operatorname{Ric}_g+g)
\]

反复对时间求导获得。由于 \(g(t)\to g_*\) 于 \(C^\infty\)，左侧各时间 jet 收敛到由 \(\mathcal F\) 确定的相应 jet，因此与从 \(g_*\) 出发的新解相匹配。

Step F 所说的“在重叠区间上由唯一性拼接”并不准确：旧解与新解只在 \(t=T_*\) 相接，没有非空的时间重叠。正确拼接依赖上述时间 jet 匹配。若还要得到 Corollary 4.1 中“唯一最大光滑解”，则需一个明确的非线性局部唯一性命题；Step 37 记载了线性化唯一性和存在性，但没有完整写出该非线性命题。

Step 37 另有一个不影响主部但应修正的公式：对

\[
\hat a=\chi^2\circ\varphi^{-1},
\]

其变分是

\[
\delta\hat a=-d\hat a(\psi)
=-2\hat\chi\,d\hat\chi(\psi),
\]

一般只有一个 \(\chi\) 因子，而不是 \(\chi^2\) 因子。它仍是有界低阶项，故“归入 Yang 线性系统的低阶矩阵”这一结论仍然成立。

---

## 4. \(t=0\) 处的 \(C\gamma_0/t\) 奇性

这不妨碍有限终止时间处使用续流结论。若假设 \(T_{\max}<\infty\)，取

\[
\tau=\frac12T_{\max}>0.
\]

光滑性和 \(M\times[0,\tau]\) 的紧致性给出

\[
\sup_{M\times[0,\tau]}|U|<\infty.
\]

而对 \(t\in[\tau,T_{\max})\),

\[
|U(t)|\le \frac{C\gamma_0}{t}+C
\le \frac{C\gamma_0}{\tau}+C.
\]

故

\[
\sup_{M\times[0,T_{\max})}|U|<\infty.
\]

所以，只要 Moser 端点估计确实持续成立到 \(T_{\max}\)，初始时刻的 \(1/t\) 项不会阻止续流。Step 41 在 §5.2 使用“\(t\le\tau\) 由光滑性处理”的思路是正确的。

---

## 5. 第一退出闭合中尚未连接的部分

### 5.1 有限观察时刻与无限时间

度量漂移估计是

\[
|g(t)-g(0)|
\le C\delta\,t^{2/3}r^{2/3}.
\]

文件只在 \(t\le\theta\) 且

\[
C\delta\,\theta^{2/3}r^{2/3}\ll1
\]

时得到 H1 的严格改善。因此该计算自然证明的是：在给定 \(\theta\) 上，若小量条件依赖 \(\theta\)，则解至少存在到 \(\theta\)。

它不能直接维持 H1 到所有 \(t\)，因为右端随 \(t^{2/3}\) 增长。相应地，(5.5) 也只在 H1–H4 已保持的时间段上导出。于是下列推理链尚缺一个全时间估计：

\[
\text{有限 }\theta\text{ 上闭合}
\;\not\Rightarrow\;
T_{\rm ex}=T_{\max}\text{ 在所有时间成立}
\;\not\Rightarrow\;
T_{\max}=\infty.
\]

若把第一退出时间定义在 \([0,\min\{T_{\max},\theta\}]\)，现有漂移估计可以支持“\(T_{\max}>\theta\)”。要得到无限时间，还需要与 \(\theta\) 无关的小量、可反复重置的区间估计，或可积的长期速度衰减。当前的 \(t^{-1/3}\) 速度上界并不可积于 \([1,\infty)\)。

### 5.2 H2、H3、H4 的严格改善

显示出的公式尚不足以逐项得到 §5.2 所用的严格改善：

- (5.6) 在零附近发散，因此自身不能改善固定的 H2。对单个初值可用短时间光滑性分段处理，但相应的短时间长度和 \(K_*\) 依赖该初值。
- (5.3) 只有
  \[
  K_2(t)\le C K_2^{(0)},
  \]
  这并不推出
  \[
  K_2(t)<2K_2^{(0)}
  \]
  ，除非另有 \(C<2\) 或 \(1+o(1)\) 型估计。
- H4 同时依赖 Sobolev 常数与 \(K_2^{1/2}\)；度量接近只控制前者，后者仍需要上述 \(1+o(1)\) 型能量公式。

因此，“严格改善 H1–H4”需要一条定量能量式，而不能只从 (5.3) 的固定倍数估计推出。

---

## 6. 单个初值与度量序列的量词差异

单个初值的续流定理允许所有常数依赖 \(g_0,\chi\)。这对排除某个具体解的有限奇异时间完全足够。

但 Conditional Theorem 7.1 考察同一 \(M\) 上变化的度量 \(g_i\)。其所需量词是

\[
\exists\,\delta_0(M)>0\quad
\forall\,g\text{ on }M.
\]

当前估计提供的形式更接近

\[
\forall\,g\quad
\exists\,\varepsilon(g,\chi,K_2,\mathcal S,\ldots)>0.
\]

二者不能交换。即使 \(\delta_i\to0\)，也不能推出

\[
\delta_i<\varepsilon(g_i)
\]

最终成立；例如可能有 \(\varepsilon(g_i)=\delta_i^2\)。同样，\(\gamma_{0,i}\) 的小性并没有由 \(\delta_i\to0\) 推出。

所以，Step 41 §7 中“对充分大的 \(i\)，初始数据满足 bootstrap hypotheses”尚无所给材料支持。需要的是沿整个度量序列对 Sobolev 常数、\(K_2^{(0)}\)、支集几何、短时间分段参数以及各 Moser 常数的共同控制。Terminal Layer E 即使成立，也不会自动补出这些序列估计，除非其中明确包含相应的紧性与定量几何结论。

---

## 对四个指定问题的直接回答

1. **Step C：正确。** 弱 Kato 不等式适用于张量模长；每一阶逐点估计使用下一阶有限 \(L^q\) 估计。
2. **Step E：实质正确，但文字省略了联络差张量归纳和时间 jet 拼接。** 退化扩散不影响这一终端论证。
3. **初始时刻：处理正确。** 有限 \(T_{\max}\) 时，将时间分成 \([0,T_{\max}/2]\) 与 \([T_{\max}/2,T_{\max})\) 即可。
4. **度量序列：确有量词不一致。** 单个初值的常数不足以推出固定流形上的统一 Ricci 缺陷下界，更不足以产生仅依赖维数的常数。