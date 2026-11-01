# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step38_continuation_repair_and_support_normalization.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Verify the proposed arbitrary-order staggered energy induction in step40_staggered_all_order_continuation_candidate.md. The central question is whether, after the m=2 extra signed integration by parts, every current-order cutoff-jet/lower-U product at arbitrary m can be reduced without demanding a current unknown at a larger exponent. Check the structural equations for U_m, C_{m+1}, and T_m against Wang Section 4 and the shifted-curvature derivation. In particular: (i) classify all ways current U_m, current C_{m+1}, or derivatives U_{m+1}, C_{m+2}, T_{m+1} can appear; (ii) verify the extra IBP on chi C_{m+1} U_1 P(U_m), including commutators, for m>=3; (iii) verify the subsequent unweighted T_m energy when expanding nabla^{m+2}a honestly; (iv) check the finite exponent schedule and cutoff-jet evolution; (v) identify any missing term that defeats equations (2.9), (2.11), or (3.6). Do not accept a schematic appeal to Wang if a current-level multiplier is hidden. Give a direct mathematical verdict on the energy induction. The terminal restart/short-time existence may be treated separately.

## Output

# 科学核验备忘录

## 结论

在闭流形的正时间光滑区间 \([\tau,T_*)\) 上，假设

\[
\sup_{M\times[\tau,T_*)}|U|<\infty
\]

并把 (1.7) 解释为各较低空间阶的 \(L^q\) 范数对时间一致有界，则 Step 40 的交错递推

\[
(U_m,C_{m+1})\longrightarrow T_m
\]

在任意固定有限指数 \(p\ge2\) 上闭合。逐项展开 Wang Lemmas 4.4–4.6 的导数结构以及 shifted-curvature 文件中的 (3.8)、(4.1) 后，没有出现迫使同一子阶段的 \(U_m\)、\(C_{m+1}\) 或 \(T_m\) 从 \(L^p\) 升到 \(L^{2p}\) 的项。

其中有两个应在正式证明中明确写出的细节：

1. 对所有出现的
   \[
   \chi C_{m+1}*U_1*P(U_m)
   \]
   都要施行 (2.6)，不仅是从 \(\chi C_{m+2}*U\) 分部积分产生的那一份；原始高截止导数和中本来就有另一份同型项。
2. (2.10) 中的 \(U_0*C_{m+1}\) 主要来自 \(L^p\) 范数和体积元随时间变化；固定标量 \(\chi\) 的原始协变导数演化本身以 \(U_j*C_{m+1-j}\) 为主。这个记账差异不改变 (2.11)。

下面给出直接分类。

---

## 1. \(U_m\) 方程中的全部同阶出现方式

Wang Lemma 4.5 和 shifted equation (4.1) 给出的高截止导数部分是

\[
\sum_{\alpha+\beta+\gamma=m+2,\ \gamma\le m+1}
C_\alpha*C_\beta*U_\gamma .
\]

由导数总数立即得到以下穷尽分类。

| 同阶对象 | 唯一可能的导数分配 |
|---|---|
| \(U_{m+1}\) | \((\alpha,\beta,\gamma)=(1,0,m+1)\) 及交换，故为 \(\chi C_1*U_{m+1}\) |
| \(U_m\) | \((2,0,m)\)、\((1,1,m)\)，故为 \(\chi C_2*U_m\)、\(C_1*C_1*U_m\) |
| \(C_{m+2}\) | \((m+2,0,0)\) 及交换，故为 \(\chi C_{m+2}*U\) |
| \(C_{m+1}\) | \((m+1,1,0)\)、\((m+1,0,1)\)，故为 \(C_1*C_{m+1}*U\)、\(\chi C_{m+1}*U_1\) |

因此不存在 \(C_{m+1}*U_j\) 且 \(j\ge2\) 的原始项；导数总数已经排除了它。

其余结构也没有隐藏同阶乘子：

* 在
  \[
  \sum_{i+j+k=m,\ k\le m-1}\nabla^ia*U_j*T_k
  \]
  中，若 \(U_j=U_m\)，则 \(i=k=0\)，系数是
  \[
  aT=U,
  \]
  已由 \(K\) 控制。
* 连接变化给出
  \[
  [\partial_t,\nabla^m]U
  =\sum_{r+s=m-1}U_{r+1}*U_s.
  \]
  唯一含 \(U_m\) 的项是 \(U_m*U_0\)，系数仍有界。
* 归一化和 \(G\) 项具有
  \[
  \sum_{i+j=m}\nabla^ia*G*U_j.
  \]
  含 \(U_m\) 时 \(i=0\)，系数 \(aG\) 有界；若 \(i>0\)，最高截止导数仅为 \(C_m\)。
* Laplacian 交换项正是 Wang 公式中 \(T_k\) 只到 \(m-1\) 的来源，没有 \(T_m\) 乘上未控制的系数。

所以同阶 \(U_m\) 只以三种可处理形式出现：加权梯度 \(U_{m+1}\)、有符号 Hessian 系数 \(\chi C_2\)、有界零阶系数。

---

## 2. 第二次分部积分在任意 \(m\) 上成立

第一次从 \(\chi C_{m+2}*U\) 移走一个导数后，以及原方程中的直接分配，都会产生

\[
J_m=\int_M \chi\,C_{m+1}*U_1*P(V),\qquad V=U_m.
\]

逐个张量收缩处理即可。对有序协变导数可直接写

\[
C_{m+1}=\nabla C_m,
\]

从而闭流形上的散度积分给出

\[
\begin{aligned}
J_m={}&-\int d\chi*C_m*U_1*P(V)\\
&-\int\chi C_m*U_2*P(V)\\
&-\int\chi C_m*U_1*\nabla P(V).
\end{aligned}
\tag{A}
\]

若为了统一指标次序需要交换协变导数，则

\[
C_{m+1}-\nabla C_m
=
\sum_{r=0}^{m-2}\nabla^r\operatorname{Rm}*C_{m-1-r}
\tag{B}
\]

在示意张量意义下成立。这里曲率阶数至多 \(m-2\)，截止导数阶数至多 \(m-1\)；全部属于已经完成的空间层。把 \(\operatorname{Rm}=T-G\) 代入也不会产生新分支，因为 \(\nabla G=0\)。

式 (A) 的三项分别如下。

### 2.1 导数落在 \(\chi\)

\[
\int |d\chi|\,|C_m|\,|U_1|\,|V|^{p-1}
\le
C\|C_m\|_{2p}\|U_1\|_{2p}\|V\|_p^{p-1}.
\]

\(C_m\) 是第 \(m-1\) 阶截止对象，\(U_1\) 也是较低层，因而右端是
\(C(1+\|V\|_p^p)\)。

### 2.2 导数落在 \(U_1\)

当 \(m\ge3\) 时，\(C_m\) 和 \(U_2\) 均已在前面空间层得到任意有限指数控制：

\[
\left|\int\chi C_m*U_2*P(V)\right|
\le
\|C_m\|_{2p}\|U_2\|_{2p}\|V\|_p^{p-1}.
\]

当 \(m=2\) 时，\(U_2=V\)，于是该项为

\[
\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V),
\]

其中

\[
|B(V)|\le C_p|V|^p,\qquad
|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|.
\]

Step 38 的有符号 Hessian 分部积分精确给出

\[
\left|\int\chi C_2*V*P(V)\right|
\le
\varepsilon D^U_{m,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.
\]

指标次序不同至多再产生 \(\operatorname{Rm}*U\) 型较低项。

### 2.3 导数落在 \(P(V)\)

利用

\[
|\nabla P(V)|\le C_p|V|^{p-2}|\nabla V|,
\]

有

\[
\begin{aligned}
\int\chi|C_m||U_1||V|^{p-2}|\nabla V|
&\le \varepsilon D^U_{m,p}
+C_{p,\varepsilon}\int |C_m|^2|U_1|^2|V|^{p-2}\\
&\le \varepsilon D^U_{m,p}
+C_{m,p}\|C_m\|_{2p}^2\|U_1\|_{2p}^2\|V\|_p^{p-2}.
\end{aligned}
\]

这里 \(L^{2p}\) 已经足够；原笔记使用 \(L^{4p}\) 也成立。整个过程中从未使用 \(C_{m+1}\) 的较大指数。

这证明了任意 \(m\) 上唯一棘手的
\(\chi C_{m+1}U_1P(U_m)\) 类确实被移到较低空间层。

---

## 3. 截止导数方程

对固定标量 \(\chi\)，直接变化公式是

\[
\partial_t C_{m+1}
=
\sum_{j=1}^{m}U_j*C_{m+1-j}
+\text{由指标重排产生的较低曲率项}.
\tag{C}
\]

原因是

\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\]

而 \(\nabla^{j-1}\partial_t\Gamma\) 的最高部分正是 \(U_j\)。

式 (C) 中：

* 唯一含 \(U_m=V\) 的项是 \(V*C_1\)，且 \(C_1=d\chi\) 一致有界；
* 对 \(1\le j<m\)，\(U_j\) 和 \(C_{m+1-j}\) 都是较低层；
* 原始张量演化不含“较低但非有界系数乘 \(C_{m+1}\)”；
* \(L^p\) 范数和体积元的时间变化产生 \(U_0*|C_{m+1}|^p\)，而 \(U_0\in L^\infty\)。

因此

\[
\frac d{dt}\|C_{m+1}\|_p^p
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
\]

没有较大指数的同阶对象。与 \(U_m\) 能量相加即得到 (2.9)–(2.11)。

---

## 4. \(T_m\) 子阶段

Wang Lemma 4.4 和 shifted equation (3.8) 给出

\[
\partial_tT_m
=
a\Delta T_m
+\sum_{r+k=m+2}\nabla^ra*T_k
+\sum_{i+j+k=m}\nabla^ia*T_j*T_k
+\mathcal N_m.
\]

令 \(X=T_m\)。同阶对象的全部出现方式是：

* \(T_{m+1}\)：只能来自 \(r=1\)，即
  \[
  \nabla a*T_{m+1}=2\chi C_1*\nabla X,
  \]
  可由 \(D^T_{m,p}\) 吸收。
* \(T_m\)：在线性部分只能来自 \(r=2\)，即
  \[
  \nabla^2a*X=(2\chi C_2+2C_1*C_1)*X.
  \]
  第一项使用有符号 Hessian 分部积分，第二项是有界系数。
* 二次项若含 \(T_m\)，则另一个因子与 \(a\) 合并成
  \[
  aT=U,
  \]
  因而是有界系数乘 \(X\)。
* 连接变化为
  \[
  [\partial_t,\nabla^m]T
  =
  \sum_{r+s=m-1}U_{r+1}*T_s.
  \]
  最高项为 \(U_m*T_0\)，而 \(U_m\) 已在前一子阶段获得所有有限指数。
* \(\partial_tG\) 及其导数给出 \(G*U_m\) 和较低项，不含 \(U_{m+1}\)。

完整展开最高截止导数为

\[
\nabla^{m+2}a
=
2\chi C_{m+2}
+\sum_{\substack{s+t=m+2\\s,t\ge1}}C_s*C_t.
\]

后一个和式中最高对象仅为 \(C_1*C_{m+1}\)，已由前一子阶段得到任意有限指数。对第一项分部积分：

\[
\begin{aligned}
\int\chi C_{m+2}*T*P(X)
={}&-\int d\chi*C_{m+1}*T*P(X)\\
&-\int\chi C_{m+1}*T_1*P(X)\\
&-\int\chi C_{m+1}*T*\nabla P(X).
\end{aligned}
\]

最后一项给出

\[
\varepsilon D^T_{m,p}
+C\int |C_{m+1}|^2|T|^2|X|^{p-2},
\]

而 \(C_{m+1}\) 和 \(T\) 已具有所有所需有限指数。

第二项在 \(m=1\) 时是

\[
\chi C_2*X*P(X),
\]

仍是有符号 Hessian 项；在 \(m\ge2\) 时 \(T_1\) 属于较低层。若需调整 \(C_{m+2}\) 的指标次序，额外项形如

\[
\nabla^r\operatorname{Rm}*C_{m-r}*T*P(X),
\qquad 0\le r\le m-1,
\]

同样只含较低的 \(T\) 导数和截止导数。

所以 \(T_m\) 方程中也没有未控制系数乘 \(|X|^p\) 的情形；唯一非有界的同阶系数 \(\chi C_2\) 已由有符号 Hessian公式处理。这建立了 (3.6)。

---

## 5. 有限指数安排

若 \(A_1,\dots,A_N\) 都来自较低空间层，则

\[
\int |A_1\cdots A_N|\,|V|^{p-1}
\le
\prod_{\nu=1}^N\|A_\nu\|_{Np}\,\|V\|_p^{p-1}.
\]

Young 后出现平方乘积时，

\[
\int\prod_{\nu=1}^N|A_\nu|^2\,|V|^{p-2}
\le
\prod_{\nu=1}^N\|A_\nu\|_{Np}^{2}\,\|V\|_p^{p-2}.
\]

因此每个固定 \(m,p\) 只调用有限多个较低层指数。逻辑顺序是先得到某一空间层对所有有限 \(q\) 的陈述，再令下一层的目标 \(p\) 任意；这不是指数上的无限递升。

公式 (1.8) 在严格张量书写中应改成“所有有序 shuffle 的和”，而不是只写一个普通二项式项；但每项仍由两个截止导数组成，且两者阶数之和为 \(r\)，以上分类完全不变。

## 最终数学判定

在正时间光滑区间上，Step 40 的任意阶交错能量递推成立。唯一可能把同阶截止对象与较低 \(U\) 导数相乘的结构是

\[
\chi C_{m+1}*U_1*P(U_m),
\]

而第二次分部积分把它化为：

* 较低层 \(C_m,U_1,U_2\) 的有限指数乘积；
* \(m=2\) 时的有符号 Hessian 项；
* 可由 \(D^U_{m,p}\) 吸收的 \(\nabla P(U_m)\) 项；
* 至多含 \(T_{m-2}\) 的指标交换项。

逐项展开后，没有遗漏的项破坏 (2.9)、(2.11) 或 (3.6)。这一结论验证的是延拓论证中的全阶导数能量部分；终端度量后的 transported-coefficient 构造是另一项独立的 PDE 内容。