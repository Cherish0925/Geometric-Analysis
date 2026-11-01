# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 40,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step40_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step40_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Critically verify the assembled four-dimensional negative Ishida--LeBrun defect-gap theorem and A03's claimed discharge of H1, focusing only on mathematical interfaces that could invalidate the proof. User goal is the full Yau Problem 26, but the artifact under review is the restricted negative-family theorem. Read the supplied files and give a direct scientific memo addressing: (1) whether Step39's support Lemma 3.1 proves all cutoff regularity it uses, especially Hessian/higher jets under only Ricci lower bound and mean curvature energy; (2) whether the K2 self-improvement with any additive C0*T is homogeneous enough in collapsed or tiny-support regimes; (3) whether A03 Step40/Step41 sufficiently verify the normalized weighted-U and unweighted-T evolution interfaces, including G, normalization, connection variation, and zero-order T propagation, or still leave structural equations to derive; (4) whether the transported DeTurck existence/restart proof is a complete theorem or a plausible adaptation needing detailed tame estimates; (5) whether terminal recalibration requires q>=0 and selected monopole class with (a^+)^2>=A, and whether Step39's theorem statement says this clearly; (6) whether the exponential-pullback/terminal compactness passage must use inner plateau centers, Liouville averaging on a center set, and strong finite-W^{2,p} convergence rather than weak convergence or Lipschitz-in-metric claims. Conclude what should be repaired next to turn the restricted theorem into a rigorous mathematical result, without treating it as completion of Yau 26.

## Integrated Scientific Memo

# 核验备忘录：四维负 Ishida–LeBrun 缺陷间隙定理

## 总判定

Step39 尚未给出无条件严格定理，A03 Step40/41 也尚未严格解除 H1。现有材料已经形成可信的证明架构，但以下接口仍可使证明失效：

- 支撑引理没有构造其声称的统一 Hessian 截止界；
- \(K_2\) 自改进中的裸 \(C_0T\) 不具已展示的局部齐次性；
- weighted-\(U\)、unweighted-\(T\) 的一般阶结构式及零阶 \(T\) 传播尚未完整推导；
- transported DeTurck 只是可信的 Yang 扰动方案，缺少 \(\varepsilon\)-一致 tame 估计；
- 终端 \(119Q\) 校准需要明确的 \(q\ge0\) 和终端重新选择 monopole 类；
- Step39 的弱 \(W^{2,p}\) 极限不足以传递 \(W^+\) 谱，必须采用 Step28 的内层中心、Liouville 平均和强有限 \(W^{2,p}\) 紧致性。

此外还有一个组装接口必须修正：所有 plateaux 必须来自**同一次全局 cutoff 流**，而不是分别运行互不兼容的局部流。

---

## 1. Lemma 3.1 没有证明其声称的截止正则性

### 已证明的部分

Ricci 下界、Bishop–Gromov doubling 和 maximal-function 论证足以给出：

\[
\operatorname{Vol}(G_R)\ge \eta_0\operatorname{Vol}(M),
\]

最大 \(14r\)-分离中心，\(B_{7r}(x_\alpha)\) 两两不交，以及

\[
\sum_\alpha \operatorname{Vol}B_{2r}(x_\alpha)\gtrsim A_i.
\]

中心处的曲率平均小量也成立。但要控制整个 \(\eta_\alpha\)-支撑上的初始 \(K_2^\eta\)，必须明确选择

\[
7r\le R,
\]

否则 maximal function 只控制半径不超过 \(R\) 的球，未必覆盖 \(B_{7r}(x_\alpha)\)。

### 未证明的部分

Lemma 3.1(a) 声称

\[
\|\nabla^2\chi_\alpha\|_\infty\le Cr^{-2}.
\]

该结论不能由仅有的 Ricci 下界和中心处平均 \(L^2\)-曲率小量推出。距离函数 cutoff 最多立即给出 Lipschitz 梯度控制；其 Hessian 需要更强的局部截面曲率或 harmonic-radius 控制。平均曲率小量不排除支撑内存在点状高曲率。

好消息是 Step34–35 的能量估计不需要这个统一 Hessian 界。它们将

\[
(\nabla^2a)*B
\]

作为有符号张量分部积分，最终只使用

\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2}.
\]

因此严密的支撑引理应删除统一 Hessian 断言，只保留：

1. \(\chi_\alpha,\eta_\alpha\) 光滑；
2. \(|d\chi_\alpha|\le C/r\)；
3. plateau 和 stationary collar；
4. 每个固定数据上所有高阶 jets 有限，但不声称沿序列统一。

原始距离 cutoff 在 cut locus 不光滑，还需引用或构造保持梯度控制的光滑逼近。Step40 所用高阶 \(\nabla^m\chi\) 只需 per-datum 有限，因此不需要统一高阶几何控制。

### 单一全局流问题

Step39 §4 按单个 \(\chi_\alpha\) 写流，但 §5 和 §7 使用一个同时包含所有 plateaux 的终端度量。应定义一个全局 cutoff，例如在互不相交的支撑下

\[
a_i=\sum_\alpha \chi_\alpha^2
\]

并只运行一次流

\[
\partial_tg=-2a_i(\operatorname{Ric}+g).
\]

若分别运行局部流，所得终端度量不同，无法进行全局 \(Q\) 求和或从所有 plateaux 中选择同一个终端中心。

---

## 2. \(K_2^\eta\) 自改进必须是齐次的

Step39 使用

\[
(K_2^\eta)'
 \le C(1+r^{-2}+\mathcal S^2Y)K_2^\eta+C_0
\]

并在终端得到裸加项 \(C_0\theta r^2\)。按当前写法，无法统一推出

\[
C_0\theta r^2<K_2^\eta(0)
\]

因为 Ricci 下界不保证固定半径球的体积下界，塌缩支撑上 \(K_2^\eta(0)\) 可以任意小。

有两种合法修复。

### 最佳修复：使用 Step34 的齐次不等式

Step34 已给出

\[
(K_2^\eta)'+cD_2^\eta
 \le CY+Cr^{-2}K_2^\eta,
\]

及

\[
Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta).
\]

吸收后直接得到

\[
(K_2^\eta)'\le C(1+r^{-2})K_2^\eta,
\]

从而

\[
K_2^\eta(t)\le e^{C(1+r^{-2})t}K_2^\eta(0).
\]

这是对塌缩和任意小支撑真正齐次的版本，应替换 Step39 的 (4.4)、(4.13)。

### 另一可能修复：识别 \(C_0\) 的体积因子

若该项实际来自 \(F^2=1+|\mathrm{Rm}|^2\) 中的常数，则必须写成

\[
C_0(t)\le C\,\operatorname{Vol}_{g(t)}(\operatorname{supp}\eta).
\]

又因 \(F\ge1\)，并在 \(\eta=1\) 的固定内层区域上有体积比较，

\[
K_2^\eta(0)\ge c\,\operatorname{Vol}(\operatorname{supp}\eta)
\]

才可把加项吸收到种子能量中。现有 Step39 没有展示这一点，不能把符号 \(C_0\) 当作已自动齐次。

因此应优先采用已经存在的纯乘法 Step34 估计。

---

## 3. Step40/41 尚未完整验证 weighted-\(U\) 与 unweighted-\(T\) 接口

令

\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad U=aT.
\]

代数恒等式

\[
\operatorname{Ric}(T)=E,\qquad
\operatorname{Ric}(U)=aE,\qquad
\partial_tg=-2\operatorname{Ric}(U)
\]

是正确的；\(\nabla G=0\) 也说明 \(G\) 本身不产生独立空间导数分支。

但 Step40 的一般阶式

\[
\partial_tU_m=\cdots+\mathcal G_m,\qquad
\partial_tT_m=\cdots+\mathcal N_m
\]

仍将最关键的正规化、\(G\)、连接交换子和 Bianchi 余项封装在未展开符号中。要使交错归纳成为证明，至少须逐阶证明以下最高导数分类：

1. \(G\) 的时间变化
   \[
   \partial_tG=
   \frac{(\partial_tg)\owedge g+g\owedge(\partial_tg)}
        {2(n-1)}
   \]
   在 \(\nabla^m\) 后最高只含 \(U_m\) 的代数收缩；

2. 连接变化
   \[
   \partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)
   \]
   在 \([\partial_t,\nabla^m]U\)、\([\partial_t,\nabla^m]T\) 中不产生无法吸收的裸 \(U_{m+1}\) 或 \(T_{m+1}\)；

3. 将 \(\nabla^2\operatorname{Ric}(U)\) 转成扩散项时，因 \(U=aT\) 不满足普通曲率 Bianchi 恒等式而产生的
   \[
   \nabla a*\nabla T,\qquad \nabla^2a*T
   \]
   必须精确落入 Step40 已处理的权重类别；

4. 所有 \(\nabla^ra\) 必须按
   \[
   \nabla^ra=\sum_{s=0}^r C_s*C_{r-s}
   \]
   展开，不能给每一项虚构一个 \(\chi\) 因子。

Step40 的第二次分部积分确实修复了“当前 cutoff jet 必须先在 \(L^{2p}\) 中已知”的循环问题，但它验证的是**给定结构式之后**的指数调度，不等于推导了结构式。

### H2 并未由 Step35 直接解除

Step39 (4.12) 所需的是无权全流形估计

\[
\frac d{dt}\|T\|_p^p+
 c\int a|\nabla T|^2|T|^{p-2}
\le C(K+1+r^{-2})\|T\|_p^p+C_p.
\]

Step35 推导的是带 \(a^{p-2}\) 权的 \(\operatorname{Rm}\) 能量，不是这个无权 \(T\) 估计。Step41 又把无权 \(T_0\in L^q\) 当作 stage-zero 输入，并仅称其为 Wang Lemma 4.10 的正规化适配。

其机制可信：二次反应含 \(aT*T\)，在 \(|U|=|aT|\le K\) 下线性化为 \(K|T|\)；\(a=0\) 区域度量静止。但完整的正规化、Hessian-\(a\) 分部积分和常数源项尚未写出。因此 H2 当前只是“有可信证明方案”，不是已解除的引理。

Step41 另一个版本从 \(t=0\) 把固定 \(|U|\le K_*\) 放入 bootstrap，而 Moser 只导出 \(C\gamma/t+C\)。用于序列统一论证时应保留 Step39 的三角链：先由 \(K_2\to Y\to\) Moser 得到正时间 \(|U|\) 界，再只在 \([\tau,T_*)\) 用 continuation；不能让数据相关的初始 \(K_*\) 污染统一常数。

---

## 4. transported DeTurck 是可信适配，不是已完成定理

Step37 正确修复了 gauge。必须使用 transported coefficient

\[
\widehat a=(\chi\circ\varphi_t^{-1})^2
\]

以及相匹配的 gauge，而不是固定 \(a\mathcal L_Wg\)。其 pullback 代数基本正确。新增正规化项的线性化

\[
\delta(-2\widehat a\,\widehat g)
=-2\widehat a\,h-2(\delta\widehat a)\widehat g
\]

不含 \(h\) 的二阶导数，因而不改变退化抛物主符号。这充分说明 Yang 的构造应当可以适配。

但退化问题不能仅靠“低阶扰动不改变主符号”完成。还需要实际写出：

- 正则化线性系统的 \(\varepsilon\)-一致高阶能量/tame 估计；
- 对交换任意阶导数后新增两项的估计；
- 线性右逆对 \((\widehat g,\varphi)\) 的 smooth tame 依赖；
- Nash–Moser 邻域内统一的存在时间和正定性；
- \(\varepsilon\to0\) 后极限的光滑性；
- 非线性局部唯一性，以定义唯一极大解并无歧义地拼接 restart。

“固定点或 Nash–Moser”不能互换地略过：如果 Yang 系统存在导数损失，普通 Banach 固定点并不自动适用。文件中的 Yang 定理编号也不一致（Step39 的 Theorem 4.1 与 Step37 的 Theorem 8.2），必须核准同一准确来源和假设。

一旦归一化短时存在定理完成，从任意光滑终端度量 restart 的确是直接推论。因此 H1 的困难集中在归一化退化 tame 理论本身，而不在 restart 的逻辑形式。

---

## 5. 终端 recalibration 的拓扑条件必须写清楚

设

\[
q=k-\frac A3,\qquad e=(a^+)^2-A.
\]

终端度量上的恒等式为

\[
D_a=J-q-\frac23e.
\]

要得到 Step39 使用的纯粹控制

\[
0\le D_a\le J
\]

必须有

\[
q\ge0,\qquad (a^+)^2\ge A.
\]

Theorem 1.1 只写 \(k_i/A_i\to1/3\)，没有写 \(q_i\ge0\)，因此 §6 的

\[
\int\mathfrak D(T)\le119Q(T)
\]

并非按当前定理陈述自动成立。

有两种修复：

- 在定理中加入 \(k_i\ge A_i/3\)；
- 或允许 \(q_i<0\)，使用
  \[
  D_a\le J+q_-,
  \qquad q_-=\max\{-q,0\},
  \]
  从而
  \[
  \int\mathfrak D
  \le119Q+912\pi^2q_-.
  \]
  因 \(k_i/A_i\to1/3\)，有 \(q_-/A_i\to0\)，这仍足以支持渐近矛盾，只是常数不再是纯 \(119Q\)。

monopole 符号类必须针对**终端度量重新选择**，因为 \(a^+\) 依赖终端 Hodge 分解。平均恒等式应安全地写为

\[
2^{-k}\sum_\varepsilon(a_\varepsilon^+)^2
=(c_1(X)^+)^2+\sum_j(E_j^+)^2
\ge A+\sum_j(E_j^+)^2,
\]

除非另有证明 \((c_1(X)^-)^2=0\)。这个不等式仍保证终端度量上存在某个符号类满足 \((a_\varepsilon^+)^2\ge A\)。同时需明确所有这些符号类均具有所用 monopole 性质。

---

## 6. 终端 pullback 必须采用 Step28 的强版本

Step39 §7.2 当前不能推出所需谱结论。

### 中心必须位于内层 plateau

把整个 \(B_{2r}(x_\alpha)\) 当作中心集不够：位于边缘的中心发出的长度 \(\rho\) 测地线可能立即离开有曲率界的区域。应选更小的内层中心集，例如

\[
P_i=\bigcup_\alpha B_r(x_\alpha),
\]

并通过 Bishop–Gromov 保持

\[
\operatorname{Vol}(P_i)\ge cA_i.
\]

结合终端与初始度量的双 Lipschitz 比较，选固定 \(\rho\ll r\)，使所有终端径向测地线留在 bounded-curvature plateau buffer 内。

### 平均必须使用 Jacobian 和 Liouville 不变性

正确对象是

\[
A_\rho D(p)=
\frac{\displaystyle
 \int_{S_pM}\int_0^\rho D(\exp_p(t\xi))J_p(t,\xi)\,dt\,d\xi}
{\displaystyle
 \int_{S_pM}\int_0^\rho J_p(t,\xi)\,dt\,d\xi}.
\]

Rauch 比较和测地流的 Liouville 不变性给出

\[
\int_{P_i}A_\rho D(p)\,d\mu(p)
\le C(4,K,\rho)\int_MD\,d\mu.
\]

这才允许利用 \(\operatorname{Vol}P_i\gtrsim A_i\) 选取 \(p_i\)。Step39 的平坦 \(dv\) 表达式必须通过 Jacobian 比较来证明，不能直接作为 Fubini 公式使用。

### 弱 \(W^{2,p}\) 收敛不足

曲率依赖 \(g\) 的二阶导数。\(C^{1,\alpha}\) 加弱 \(W^{2,p}\) 收敛不能保证

\[
|W_i^+|\to |W_\infty^+|
\]

或最小特征值及 \(G_i\) 的强收敛。“这些曲率量对度量系数 Lipschitz”是错误接口；只有在曲率张量本身强收敛后，有限维自伴算子的特征值才是 Lipschitz 的。

可行的严格路径是：

1. Rauch 下 Jacobian 界在 tangent-space pullback 域制造中心非塌缩；
2. 缩小一次半径，取得统一 harmonic radius；
3. 先有 \(C^{1,\beta}\) 紧致性；
4. plateau 上
   \[
   \|E_i(T)\|_\infty\le C\delta_i\to0;
   \]
5. harmonic 坐标方程
   \[
   g_i^{ab}\partial_a\partial_b(g_i)_{jk}
   =-2(\operatorname{Ric}_{g_i})_{jk}
     +Q_{jk}(g_i,\partial g_i)
   \]
   及 \(\operatorname{Ric}_{g_i}=-g_i+E_i\) 给出较小球上的强有限
   \[
   g_i\to g_\infty\quad\text{于 }W^{2,p},\qquad p>4;
   \]
6. 因而
   \[
   \operatorname{Rm}_{g_i}\to\operatorname{Rm}_{g_\infty}
   \quad\text{于 }L^p,
   \]
   从而传递 \(s,W^+\)、最小特征值及 \(G\)；
7. Einstein 方程再把极限提升为光滑度量，以合法应用 Derdziński。

另一途径是利用正时间 plateau 内部曲率导数估计得到更小球上的光滑收敛。无论采用哪一种，都不能只用弱 \(W^{2,p}\)。

---

## 建议的严格修复顺序

1. **重写支撑定理**：加入 \(7r\le R\)、光滑梯度 cutoff、stationary collar、内层中心集和单一全局 cutoff；删除统一 Hessian/高阶 jet 断言。
2. **替换 \(K_2\) 不等式**：使用 Step34 的纯乘法齐次传播，彻底删除裸 \(C_0T\)，或明确证明该项按局部体积缩放。
3. **补出零阶无权 \(T\) 引理**：完整展开正规化、\(G\)、Hessian-\(a\) 项，严格证明 (4.12)。
4. **证明一般阶结构命题**：对 \(\mathcal G_m,\mathcal N_m\)、连接变化及 Bianchi 余项给出归纳式，而非仅用星号分类。
5. **完成归一化 Yang 适配**：写出 \(\varepsilon\)-一致 tame estimates、极限、唯一性；之后 restart 才真正解除 H1。
6. **修正终端校准陈述**：明确 \(q\ge0\)，或保留 \(q_-\) 误差；每个终端度量重新选择满足 \((a^+)^2\ge A\) 的 monopole 类。
7. **用 Step28 替换 Step39 §7**：内层中心、Liouville–Rauch 平均、半径缩小、强有限 \(W^{2,p}\) 和 Einstein 正则性。
8. **补验未提供的 Moser recurrence**：现有材料不能独立重验
   \[
   \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
   \]
   的精确指数；给定该端点，\(t^{-1/3}\) 可积及 metric drift 计算是正确的。

这些补充完成后，路线有望证明的是：近临界 Ishida–LeBrun 四流形族在 \(\operatorname{Ric}\approx-g\) 归一化下存在统一缺陷间隙。它仍不是 Yau 第26题的完成：正曲率支、任意四维拓扑、\(n\ge5\)、仅依赖维数的常数及 Lean 4 形式化均未覆盖。