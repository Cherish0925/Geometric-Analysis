# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 41,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step41_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step41_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the continuation criterion (Theorem 3.1) and its application to the first-exit bootstrap, as stated in the Step 41 note. The key claims are:

1. Given a smooth solution of dt g = -2a(Ric+g) on [0,T*) with |U| = |a(Rm+G)| ≤ K and T* < ∞, the solution extends smoothly past T*. The proof uses: (a) metric equivalence from bounded velocity, (b) the Step 40 staggered L^p induction giving all derivative bounds, (c) Sobolev + Kato for pointwise bounds, (d) Arzelà-Ascoli for terminal convergence, (e) restart from the Step 37 DeTurck existence.

2. The first-exit bootstrap closes on the actual maximal interval. The curvature Moser gives |U(t)| ≤ Cγ/t + C for t > 0, which combined with the smooth initial data gives sup_{[0,T*)} |U| < ∞ when T* < ∞, hence T_max = ∞ by the continuation criterion.

Check carefully: (i) Is the argument from L^p bounds to pointwise bounds (Step C) correct for all m? Does the Kato inequality handle tensor norms properly? (ii) Is the terminal convergence (Step E) correct for this degenerate equation where the diffusion degenerates at χ=0? (iii) In the first-exit closure, the curvature endpoint |aF(t)| ≤ Cγ/t gives |U(t)| bounded only for t > 0 — does the argument properly handle the initial time t=0? (iv) Is there a gap between the per-datum continuation (which uses constants depending on the specific smooth solution) and the sequence-uniform estimates needed for the gap theorem?

## Integrated Scientific Memo

## 核验结论

### 1. Theorem 3.1：条件性成立，但现稿不是完全闭合的独立证明

在以下两项确已成立的前提下，

1. Step 40 的任意阶、任意有限 \(L^p\) 一致估计；
2. Step 37 对同一退化固定截断方程的短时存在与非线性唯一性，

有限时间内
\[
\sup_{M\times[0,T_*)}|U|<\infty
\]
确实推出光滑延拓。退化系数 \(a=\chi^2\) 不妨碍终端收敛，因为终端论证只使用速度
\[
v=\partial_tg=-2\operatorname{Ric}(U)
\]
及其所有空间导数，而不需要统一抛物性。

但现有材料中，Step 40 的全阶交换子枚举仍是示意性的，Step 37 也没有完整写出非线性唯一性。因此严格表述应是：

> **条件性续流定理。** 假设 Step 40 的全阶估计和 Step 37 的短时存在/唯一性成立，则有界 \(U\) 排除有限时间奇点。

---

## 2. 度量等价：结论正确，证明应改成乘法 ODE 比较

Step 41 的加法论证
\[
|g(t)-g(0)|\le CKT_*
\]
本身不能直接保证双 Lipschitz 等价。正确证明是：对固定 \(X\neq0\)，
\[
\left|\frac{d}{dt}\log g(t)(X,X)\right|
\le |\partial_tg|_{g(t)}
\le C_nK,
\]
故
\[
e^{-C_nKt}g_0\le g(t)\le e^{C_nKt}g_0.
\]
这给出体积、\(|d\chi|\) 和 Sobolev 常数的统一控制。Sobolev 常数还依赖初始数据 \((M,g_0)\)，不能仅记为 \(C(n,K,T_*)\)。

---

## 3. 问题 (i)：\(L^p\to L^\infty\) 正确，Kato 对张量适用

对任意张量丛截面 \(S\)，弱 Kato 不等式
\[
|d|S||\le |\nabla S|
\]
成立；在 \(S=0\) 处按弱导数理解。取固定 \(q>n\)，由统一的标量 Sobolev 嵌入，
\[
\|S\|_\infty
\le C\bigl(\|S\|_{L^q}+\|\nabla S\|_{L^q}\bigr).
\]
因此分别取
\[
S=U_m,\qquad C_{m+1},\qquad T_m
\]
得到
\[
\begin{aligned}
\|U_m\|_\infty
&\le C(\|U_m\|_q+\|U_{m+1}\|_q),\\
\|C_{m+1}\|_\infty
&\le C(\|C_{m+1}\|_q+\|C_{m+2}\|_q),\\
\|T_m\|_\infty
&\le C(\|T_m\|_q+\|T_{m+1}\|_q).
\end{aligned}
\]
不存在指标循环：先由全阶归纳取得每一阶有限 \(L^q\) 控制，再逐阶应用 Sobolev。

真正尚未完全形式化的是 Step C 的输入。Step 40 的任意阶文件只以
\(\mathcal G_m,\mathcal N_m\) 的“正确最高阶结构”概括所有交换子和联络变分项；完整展开的计算仅做到低阶。已写出的最高截断阶分类和额外分部积分机制是相容的，但仍需任意 \(m\) 的穷尽性证明。

---

## 4. 问题 (ii)：终端收敛成立，但 Step E 省略了关键转换

由度量相容性，
\[
\nabla^m v=-2\operatorname{Ric}(\nabla^mU),
\qquad
|\nabla^mv|\le C_{n,m}|U_m|.
\]
这给出移动联络 \(\nabla^{g(t)}\) 下的速度导数界。要推出固定坐标中的 \(C^\infty\) 收敛，需补入联络差归纳。

令
\[
A(t)=\nabla^{g(t)}-\nabla^{g_0}.
\]
联络变分公式为
\[
(\partial_tA)^k{}_{ij}
=\frac12g^{k\ell}
\left(\nabla_iv_{j\ell}+\nabla_jv_{i\ell}-\nabla_\ell v_{ij}\right).
\]
由 \(v\) 的协变导数界和
\[
\nabla^{g_0}=\nabla^{g(t)}+A*
\]
归纳得到所有 \((\nabla^{g_0})^rA\) 有界，进而
\[
\sup_{t<T_*}\|v(t)\|_{C^r(g_0)}<\infty .
\]
于是
\[
\|g(t)-g(s)\|_{C^r(g_0)}\le C_r|t-s|,
\]
故整个族在每个 \(C^r\) 中为 Cauchy，并唯一收敛到光滑正定度量 \(g_*\)。

退化性没有额外障碍：

- 在 \(\{\chi=0\}\) 上，\(v=0\)，度量冻结；
- 在过渡区，所需信息已包含在 \(U=aT\) 的全阶控制中；
- 此处不使用正的统一扩散下界。

### 拼接修正

Step F 所谓“在 overlap 上唯一性”不准确：旧解和从 \(g_*\) 出发的新解仅在 \(T_*\) 相接，没有非空重叠。应证明所有时间 jet 匹配。由于方程自治，
\[
\partial_tg=\mathcal F(g),
\]
而 \(g(t)\to g_*\) 于 \(C^\infty\)，递归求时间导数可知旧解左侧 jets 与从 \(g_*\) 出发的新解右侧 jets 都由 \(\mathcal F\) 的相同递归公式决定，因此拼接光滑。若要声明唯一最大解，还需明确引用或证明退化方程的非线性局部唯一性。

Step 37 中另有一处权重表述应修正：
\[
\hat a=\hat\chi^2,\qquad
\delta\hat a=-2\hat\chi\,d\hat\chi(\psi),
\]
一般只有一个显式 \(\hat\chi\) 因子，而非 \(\hat\chi^2\)。它仍是有界的一阶低阶项，所以“不改变主部”的结论不因此失效，但不能按原文宣称具有 \(\chi^2\) 权重。

---

## 5. 问题 (iii)：\(1/t\) 不妨碍续流，但第一退出闭合本身仍有缺口

若假设 \(T_{\max}<\infty\)，取
\[
\tau=T_{\max}/2.
\]
光滑性给出
\[
\sup_{M\times[0,\tau]}|U|<\infty,
\]
而对 \(t\ge\tau\)，
\[
|U(t)|\le C\gamma_0/t+C
\le C\gamma_0/\tau+C.
\]
因此
\[
\sup_{M\times[0,T_{\max})}|U|<\infty.
\]
所以，只要 Moser 端点确实在整个最大区间上成立，\(t=0\) 的形式奇性不影响应用续流准则。

然而，Step 41 所声称的“第一退出严格改善 H1–H4”尚未证明。

### H2 的初始层问题

H2 是固定常数界
\[
\sup_M|U(t)|\le K_*,
\]
但
\[
|U(t)|\le C\gamma_0/t+C
\]
不能在 \(t\downarrow0\) 时严格改善它。短时光滑性仅说明对每个初值存在某个依赖初值的初始层，现稿没有把该层与 Moser 区间定量拼接。

可行修正是：

- 将 H2 改成适合 Moser 端点的抛物加权条件，如对 \(aF\) 使用
  \[
  \sup_{0<t<T}t\,\|aF(t)\|_\infty\le K;
  \]
  或
- 明确构造 \([0,t_0]\) 初始层，在该层由短时光滑解保留 H2 的严格余量，并证明在 \(t_0\) 后 Moser 界接管。

注意 \(\|\operatorname{Ric}+g\|_\infty\) 小并不控制 \(U(0)\)，因为 Weyl 曲率可很大。

### H3、H4 的严格改善未由现有公式推出

(5.3) 只给出
\[
K_2(t)\le C K_2^{(0)},
\]
并不能推出 bootstrap 所需的
\[
K_2(t)<2K_2^{(0)}
\]
或 \(1+O(\delta)\) 改善。H4 又依赖
\[
\gamma(t)=\mathcal S(t)K_2(t)^{1/2};
\]
度量接近只控制 \(\mathcal S(t)\)，不能自动改善 \(K_2(t)\)。需要一条明确的 \(1+o(1)\) 型能量估计，而不是固定倍数估计。

### 有限观察时间不能直接推出永恒存在

漂移界
\[
|g(t)-g_0|\le C\delta\,t^{2/3}r^{2/3}
\]
只在预先固定的 \(t\le\theta\) 且
\[
C\delta\theta^{2/3}r^{2/3}\ll1
\]
时改善 H1。它随时间增长，不能用同一固定小量维持 H1 到无穷时间。因此现有论证至多支持：

> 对每个预先固定的有限 \(\theta\)，在依赖 \(\theta\) 的小量条件下，解可延伸到 \(\theta\)。

它尚不能推出一个固定初值的 \(T_{\max}=\infty\)。要得到后者，需要与 \(\theta\) 无关的长期估计、可重置的分段 bootstrap，或时间可积的长期速度衰减；当前 \(t^{-1/3}\) 速度界在 \([1,\infty)\) 不可积。

---

## 6. 问题 (iv)：per-datum 与序列统一估计之间存在实质量词缺口

续流准则本身可以完全是 per-datum 的：对某一固定 \((g_0,\chi)\)，所有常数依赖该数据并不妨碍排除该解的有限时间奇点。

但 gap theorem 考察变化的序列 \(g_i\)，其目标量词是
\[
\exists\delta_0(M)>0\quad\forall g.
\]
当前材料只提供类似
\[
\forall g\quad\exists\varepsilon(g,\chi,K_2,\mathcal S,\ldots)>0.
\]
不能交换这两个量词；即使 \(\delta_i\to0\)，也不能推出最终有
\[
\delta_i<\varepsilon(g_i).
\]

尤其，\(\delta_i=\|\operatorname{Ric}_{g_i}+g_i\|_\infty\to0\) 本身不控制：

- 局部或整体 Weyl 曲率能量；
- \(K_{2,i}^{(0)}\)；
- Sobolev 常数 \(\mathcal S_i\)；
- 非塌缩、支集几何和初始层长度；
- Moser 与高阶能量常数。

因此 §7 中“对充分大的 \(i\)，bootstrap hypotheses 成立”没有由所给材料证明。这不仅是“拓扑统一常数”问题；它已影响所声称的 per-manifold gap statement。需要沿所有 near-Einstein 序列建立统一的曲率能量、体积/非塌缩、Sobolev 和截断几何控制。

---

## 最终判定

1. **Step C 正确**；Kato 正确处理任意张量，但依赖尚未完全展开证明的 Step 40 全阶输入。
2. **Step E 实质正确**；退化不构成障碍，但需补联络差归纳、时间 jets 拼接和非线性唯一性。
3. **\(t=0\) 的 \(1/t\) 奇性不妨碍有限时续流判据**；但它确实暴露了 H2 第一退出改善中未写出的初始层。
4. **序列统一性存在严格量词缺口**，且当前不足以推出 §7 的 per-manifold gap。
5. 此外，第一退出到永恒存在的推导还有两个独立缺口：H3/H4 未证明严格改善，以及只对有限观察时间有效的漂移估计不能直接维持全时间 bootstrap。