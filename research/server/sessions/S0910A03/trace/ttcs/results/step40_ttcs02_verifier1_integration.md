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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step40_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step40_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the proposed arbitrary-order staggered energy induction in step40_staggered_all_order_continuation_candidate.md. The central question is whether, after the m=2 extra signed integration by parts, every current-order cutoff-jet/lower-U product at arbitrary m can be reduced without demanding a current unknown at a larger exponent. Check the structural equations for U_m, C_{m+1}, and T_m against Wang Section 4 and the shifted-curvature derivation. In particular: (i) classify all ways current U_m, current C_{m+1}, or derivatives U_{m+1}, C_{m+2}, T_{m+1} can appear; (ii) verify the extra IBP on chi C_{m+1} U_1 P(U_m), including commutators, for m>=3; (iii) verify the subsequent unweighted T_m energy when expanding nabla^{m+2}a honestly; (iv) check the finite exponent schedule and cutoff-jet evolution; (v) identify any missing term that defeats equations (2.9), (2.11), or (3.6). Do not accept a schematic appeal to Wang if a current-level multiplier is hidden. Give a direct mathematical verdict on the energy induction. The terminal restart/short-time existence may be treated separately.

## Integrated Scientific Memo

# 核验结论

**判定：Step 40 的任意阶交错能量递推在正时间光滑区间上成立。**  
在假设较低空间阶的全部有限 \(L^q\) 范数均对时间一致有界后，顺序

\[
(U_m,C_{m+1})\longrightarrow T_m
\]

对每个固定 \(m\) 和有限 \(p\ge2\) 闭合。额外一次分部积分确实消除了唯一会诱发当前截止 jet \(C_{m+1}\) 的 \(L^{2p}\) 要求的项。未发现破坏 (2.9)、(2.11) 或 (3.6) 的遗漏项。

需要修正两处表述：

1. \(\chi C_{m+1}U_1P(U_m)\) 不仅由 \(\chi C_{m+2}U\) 第一次分部积分产生；它也作为原始高截止分配直接出现。**所有同型项都必须施行第二次分部积分。**
2. (2.10) 中 \(U_0*C_{m+1}\) 不是固定标量 \(\chi\) 的协变导数演化的主要项；它主要来自 \(C_{m+1}\) 的范数、逆度量及体积元随时间变化。该记账修正不影响 (2.11)。

---

## 1. 结构方程与同阶对象的穷尽分类

Wang Lemmas 4.4–4.6 与 shifted-curvature 推导支持

\[
\partial_tU_m
=a\Delta U_m+
\sum_{\alpha+\beta+\gamma=m+2,\ \gamma\le m+1}
C_\alpha*C_\beta*U_\gamma+\cdots
\]

以及

\[
\partial_tT_m
=a\Delta T_m+
\sum_{r+k=m+2}\nabla^ra*T_k+\cdots.
\]

关键是第一式中始终只有两个截止因子。由
\(\alpha+\beta+\gamma=m+2\) 可穷尽列出：

\[
\begin{array}{c|c}
\text{当前或更高对象}&\text{唯一可能结构}\\ \hline
U_{m+1}&\chi C_1*U_{m+1}\\
U_m&\chi C_2*U_m,\quad C_1*C_1*U_m\\
C_{m+2}&\chi C_{m+2}*U\\
C_{m+1}&C_1*C_{m+1}*U,\quad \chi C_{m+1}*U_1.
\end{array}
\]

特别地，**不存在**
\[
C_{m+1}*U_j,\qquad j\ge2.
\]
这正是任意阶论证闭合的组合事实。

在第二和式
\[
\sum_{i+j+k=m,\ k\le m-1}\nabla^ia*U_j*T_k
\]
中，若 \(U_j=U_m\)，则 \(i=k=0\)，系数为
\[
aT=U,
\]
由 \(\|U\|_\infty\le K\) 控制。连接变化
\[
[\partial_t,\nabla^m]U
\]
最高只产生 \(U_m*U_0\)；不会产生未受控的 \(U_{m+1}\) 系数。归一化和 \(G\) 项也不改变排序，因为 \(\nabla G=0\)，故其导数仅为截止 jet、\(G\) 和不超过当前阶的 \(U\) 的乘积。

因此当前 \(U_m\) 只以以下方式出现：

* 加权梯度 \(U_{m+1}\)，由耗散吸收；
* \(\chi C_2 U_m\)，由有符号 Hessian 分部积分处理；
* 有界零阶系数乘 \(U_m\)。

---

## 2. 额外分部积分及其交换项

令
\[
V=U_m,\qquad Z=C_{m+1},\qquad P(V)=|V|^{p-2}V.
\]
所有
\[
J_m=\int_M\chi\,C_{m+1}*U_1*P(V)
\]
必须统一处理。选取实际有序协变导数，使 \(C_{m+1}=\nabla C_m\)，则

\[
\begin{aligned}
J_m={}&-\int d\chi*C_m*U_1*P(V)\\
&-\int\chi C_m*U_2*P(V)\\
&-\int\chi C_m*U_1*\nabla P(V)
+\mathcal R_{\rm com}.
\end{aligned}
\tag{A}
\]

若为匹配收缩而交换导数，标量的一阶导数之后的交换产生

\[
\mathcal R_{\rm com}
=
\sum \nabla^r\operatorname{Rm}*C_s*U_1*P(V),
\qquad r\le m-2
\]
（采用不同的有序表示时可作更宽松的上界 \(r\le m-1\)）。无论采用哪种安全记账，均只涉及已完成的 \(T_{<m}\) 与较低截止阶；\(\operatorname{Rm}=T-G\) 且 \(\nabla G=0\) 不产生新分支。

式 (A) 三项分别闭合：

\[
\int |d\chi|\,|C_m|\,|U_1|\,|V|^{p-1}
\le
C\|C_m\|_{2p}\|U_1\|_{2p}\|V\|_p^{p-1}.
\]

当 \(m\ge3\) 时，\(C_m,U_2\) 均为较低空间阶，故

\[
\int|\chi C_mU_2P(V)|
\le
\|C_m\|_{2p}\|U_2\|_{2p}\|V\|_p^{p-1}.
\]

当 \(m=2\) 时 \(C_m=C_2,\ U_2=V\)，该项具有真实的有符号结构

\[
\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V),
\]

因而由 Step 38 的 Hessian 引理估计为

\[
\varepsilon D^U_{m,p}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.
\]

最后，

\[
\begin{aligned}
\int\chi|C_m||U_1||V|^{p-2}|\nabla V|
&\le \varepsilon D^U_{m,p}\\
&\quad+C_{p,\varepsilon}
\int |C_m|^2|U_1|^2|V|^{p-2},
\end{aligned}
\]

而右侧剩余积只调用较低层的有限指数范数；例如 \(C_m,U_1\in L^{4p}\) 足够。于是 \(C_{m+1}\) 已完全从该困难项中移除。

第一次处理 \(\chi C_{m+2}U\) 后留下的其他当前耦合只有

\[
|Z|^2|V|^{p-2},
\qquad |Z||V|^{p-1},
\]

均由 \(Z,V\in L^p\) 直接控制。因此得到

\[
\frac d{dt}\|U_m\|_p^p+cD^U_{m,p}
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\]

---

## 3. 截止 jet 演化

对固定标量 \(\chi\)，因为

\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\]

真实最高阶结构为

\[
\partial_t C_{m+1}
=
\sum_{j=1}^{m}U_j*C_{m+1-j}
+\text{较低曲率交换项}.
\]

最高项仅为

\[
U_m*C_1,
\]

而不是 \(U_{m+1}\)。其余乘积含两个较低空间阶对象。对
\(\|C_{m+1}\|_p^p\) 求导时，逆度量和体积元变化另给出有界的
\(U_0|C_{m+1}|^p\) 型项。因此

\[
\frac d{dt}\|C_{m+1}\|_p^p
\le
C_{m,p}\bigl(
1+\|U_m\|_p^p+\|C_{m+1}\|_p^p
\bigr).
\]

与前式相加即闭合当前 pair，没有当前量的指数升级。

---

## 4. 诚实展开 \(\nabla^{m+2}a\) 后的 \(T_m\) 能量

令 \(X=T_m\)。必须使用完整展开

\[
\nabla^{m+2}a
=
2\chi C_{m+2}
+
\sum_{\substack{s+t=m+2\\s,t\ge1}}C_s*C_t.
\]

后一个和式的最高单个截止阶是 \(C_{m+1}\)，而它已在当前 pair 子阶段获得全部有限指数控制。唯一更高项为 \(2\chi C_{m+2}T\)。分部积分给出

\[
\begin{aligned}
\int\chi C_{m+2}*T*P(X)
={}&-\int d\chi*C_{m+1}*T*P(X)\\
&-\int\chi C_{m+1}*T_1*P(X)\\
&-\int\chi C_{m+1}*T*\nabla P(X)
+\mathcal R_{\rm com}^T.
\end{aligned}
\]

最后一项满足

\[
\le \varepsilon D^T_{m,p}
+C\int |C_{m+1}|^2|T|^2|X|^{p-2},
\]

这里只调用已经获得的 \(C_{m+1}\) 与零阶 \(T\) 的较大但有限指数。第二项：

* \(m=1\) 时 \(T_1=X\)，成为 \(\chi C_2B(X)\) 的有符号 Hessian 项；
* \(m\ge2\) 时 \(T_1\) 是较低空间阶。

交换项也只含 \(T_{<m}\) 和不超过 \(C_{m+1}\) 的截止 jet。

其余所有当前阶出现方式同样可控：

\[
\nabla a*T_{m+1}=2\chi C_1*\nabla X
\]
由耗散吸收；

\[
\nabla^2a*T_m=(2\chi C_2+2C_1*C_1)X
\]
分别由有符号 Hessian 引理和有界系数处理；

二次项若含 \(T_m\)，另一个曲率因子与 \(a\) 结合为有界的 \(aT=U\)；

连接变化最高产生 \(U_m*T_0\)，而 \(U_m\) 已在当前 pair 阶段得到全部有限指数；不会出现 \(U_{m+1}\)。

故

\[
\frac d{dt}\|T_m\|_p^p+cD^T_{m,p}
\le C_{m,p}\bigl(1+\|T_m\|_p^p\bigr).
\]

---

## 5. 有限指数日程

对 \(N\) 个较低层因子，

\[
\int |A_1\cdots A_N|\,|V|^{p-1}
\le
\prod_{\nu=1}^N\|A_\nu\|_{Np}\,\|V\|_p^{p-1}.
\]

Young 后的平方积可用足够大的有限指数，例如

\[
\int \prod_{\nu=1}^N|A_\nu|^2|V|^{p-2}
\le
C\prod_{\nu=1}^N\|A_\nu\|_{Np}^{2}\|V\|_p^{p-2},
\]

必要时加入有限体积余量。每个固定 \((m,p)\) 只要求有限多个较低层指数。逻辑上先证明较低空间阶“对所有有限 \(q\)”成立，再处理下一空间阶的任意目标 \(p\)；这不是当前层的无限指数爬升。

严格张量记号下，\(\nabla^ra\) 应理解为所有有序 Leibniz shuffle 的和，而非单个普通二项式项，但每项仍含两个截止因子且总阶为 \(r\)，不改变以上分类。

---

## 最终判定

在正时间光滑 slab 上，Step 40 的导数能量部分通过核验：

\[
T_0\;\to\;(U_1,C_2)\to T_1
\to(U_2,C_3)\to T_2\to\cdots
\]

对所有空间阶和所有有限 \(L^p\) 闭合。唯一危险结构

\[
\chi C_{m+1}U_1P(U_m)
\]

经第二次分部积分后只产生较低层有限指数因子、当前耗散，以及 \(m=2\) 的有符号 Hessian 项；没有任何当前未知量被要求处于更大指数。

因此没有发现击败 (2.9)、(2.11) 或 (3.6) 的项。归一化/\(G\) 项虽未逐收缩完全展示，但由 \(\nabla G=0\) 及
\(\partial_tg=-2\operatorname{Ric}(U)\) 可直接确认它们不引入更高 derivative branch 或隐藏的当前阶非有界乘子。

该判定仅覆盖全阶能量递推。终端重启所需的 transported-coefficient 退化短时存在性仍是独立问题。