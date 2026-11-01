# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step54_route_reassessment_and_joint_weighted_iteration.md",
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md",
    "Sessions/S0910A02/workspace/notes/step52_negative_chain_start_and_critical_product_audit.md",
    "Sessions/S0910A03/workspace/notes/step53_coupled_transported_coefficient_start.md"
  ]
}
```

## Task

Independently verify the Step 54 strategic and mathematical corrections. First check the family-uniform normalization: from a retained disjoint core set of total volume a fixed fraction of Vol(M)~A and ∫D≤Cδ²Vol(M), does weighted averaging indeed give a core with mean O(δ²), invalidating the claimed intrinsic A^{-1/2} loss? Check also the fixed-radius Sobolev–energy upper bound gamma≤Cr²sqrt(1+kappa²) and identify any hypothesis that could still introduce A-dependence. Second, inspect the synchronized-output coupled iteration and test whether its proposed joint difference estimate is actually viable, especially the different output weights beta_1,beta_2. Return precise derivations or a counterterm, not a procedural review.

## Output

# 独立核验备忘

## 1. 体积加权平均确实消除了 \(A^{-1/2}\) 因子

令终端时刻的互不相交核心为
\[
P=\bigsqcup_{\alpha}\Omega_\alpha,\qquad
V_\alpha=\operatorname{Vol}_{g(T)}(\Omega_\alpha),\qquad
D_\alpha=\int_{\Omega_\alpha}\mathfrak D\,d\mu_{g(T)} .
\]
由于 \(\mathfrak D\ge0\)，
\[
\sum_\alpha D_\alpha
=\int_P\mathfrak D
\le \int_M\mathfrak D
\le C_D\delta^2\operatorname{Vol}_{g(0)}(M).
\]
若终端漂移给出统一双 Lipschitz 比较，并且初始核心总量满足
\[
\sum_\alpha \operatorname{Vol}_{g(0)}(\Omega_\alpha)
\ge \alpha_0\operatorname{Vol}_{g(0)}(M),
\]
则对某个统一 \(c_{\rm vol}>0\)，
\[
\sum_\alpha V_\alpha
\ge c_{\rm vol}\alpha_0\operatorname{Vol}_{g(0)}(M).
\]
于是
\[
\min_\alpha \frac{D_\alpha}{V_\alpha}
\le
\frac{\sum_\alpha D_\alpha}{\sum_\alpha V_\alpha}
\le
\frac{C_D}{c_{\rm vol}\alpha_0}\,\delta^2.
\tag{1.1}
\]
因此至少一个核心满足
\[
\fint_{\Omega_\alpha}\mathfrak D\,d\mu_{g(T)}
\le C\delta^2,
\]
其中 \(C\) 与核心数目、单个核心体积以及 \(A\) 无关。

这里甚至不需要单独使用 \(\operatorname{Vol}(M)\asymp A\)：分子和分母都直接以总流形体积归一化。若写成 \(A\)-标度，则只是
\[
\int_M\mathfrak D=O(\delta^2A),\qquad
\operatorname{Vol}(P)\ge cA,
\]
两者相除后 \(A\) 消去。此前把全局积分分配到一个预先指定的单位球，才会留下 \(A\)；体积加权地从整族核心中选择一个核心不会留下该因子。

这一推导依赖三个明确事实：

1. 核心互不相交；
2. \(\mathfrak D\ge0\)；
3. 核心总终端体积是总初始体积的固定比例。

Step 47 的 (7.3)–(7.4) 和 Step 54 的 (6.1)–(6.3) 正好提供这三个量。因而 Step 54 对所谓内生 \(A^{-1/2}\) 损失的撤回是正确的。

---

## 2. 固定半径的 Sobolev–能量乘积计算正确

设好点 \(x_\alpha\) 满足
\[
\sup_{0<\rho\le1}
\fint_{B_\rho(x_\alpha)}|\operatorname{Rm}|^2
\le\kappa^2,
\]
并固定 \(r>0\) 使 \(Cr\le1\)。若辅助截断支撑在 \(B_{Cr}(x_\alpha)\)，则
\[
K_{2,\alpha}(0)
=\int \eta_\alpha^2(1+|\operatorname{Rm}|^2)
\le
(1+\kappa^2)\operatorname{Vol}B_{Cr}(x_\alpha).
\tag{2.1}
\]
在四维、统一 Ricci 下界下，体积归一化的局部 Sobolev 不等式给出
\[
\mathcal S_\alpha
\le
C\,r^2\operatorname{Vol}B_{Cr}(x_\alpha)^{-1/2}.
\tag{2.2}
\]
故
\[
\gamma_\alpha
=\mathcal S_\alpha K_{2,\alpha}(0)^{1/2}
\le
Cr^2\sqrt{1+\kappa^2}.
\tag{2.3}
\]
塌缩体积因子完全抵消。若
\[
\kappa^2=4C_{\mathrm{HL}}\Lambda,\qquad
\Lambda=\frac{\int_M(1+|\operatorname{Rm}|^2)}
{\operatorname{Vol}(M)}
\]
有统一上界，则选择一个固定的小 \(r\) 即可使 \(\gamma_\alpha\) 低于吸收阈值，无需令 \(r\sim A^{1/4}\)。

A02 Step 52 的推理还存在一个纯逻辑问题：即使有
\[
\mathcal S_\alpha\ge c\,r^2\operatorname{Vol}(B)^{-1/2},
\]
将它与
\[
K_{2,\alpha}(0)\le C\operatorname{Vol}(B)
\]
结合，也不能推出 \(\mathcal S_\alpha K_{2,\alpha}^{1/2}\) 的下界。后一个不等式方向与所需方向相反。

### 仍可能携带 \(A\) 的具体常数

公式 (2.3) 本身不含 \(A\)。家族层面的统一性还依赖：

- \(\Lambda\) 的统一上界；否则 \(\kappa\) 随拓扑数据变化。
- Ricci 下界的统一性；它控制局部 doubling、Sobolev 常数和着色数。
- 保留核心比例 \(\alpha_0\) 的统一性；固定半径网格与有限着色可由统一 doubling 得到。
- \(Q(T)\le C_Q Q(0)\) 中 \(C_Q\) 的统一性。
- 终端双 Lipschitz 漂移和观测时刻 \(T=\theta r^2\) 的统一性。
- 高阶截断导数是否进入共同时间或终端导数常数。现有笔记只给出高阶截断导数“逐数据有限”；若某个家族层面的常数实际依赖这些导数，仍可能间接依赖 \(A\) 或塌缩几何。

因此，加权平均和临界乘积两处的 \(A\)-损失已经消失；共同时间精确流及其统一估计仍承担其余常数。

---

## 3. 同步输出权重：不同的 \(\beta_1,\beta_2\) 并非自动产生障碍

考虑主部模型
\[
\partial_tV_i
=(\beta_i^2+\varepsilon)A(U_i)D^2V_i+\cdots,
\qquad
\partial_t\beta_i
=\beta_i^2W(V_i)\cdot D\beta_i,
\]
并记
\[
Z=V_1-V_2,\qquad \omega=\beta_1-\beta_2.
\]
取
\[
s>\frac n2+2,\qquad r=s-2>\frac n2,
\]
并假定各输出在 \(H^s\) 球内统一有界。

### 3.1 应始终以第二分支组织差分

令 \(A_i=A(U_i)\)、\(a_i=\beta_i^2+\varepsilon\)。主部有精确分解
\[
a_1A_1D^2V_1-a_2A_2D^2V_2
=
a_2A_2D^2Z
+(\beta_1^2-\beta_2^2)A_1D^2V_1
+a_2(A_1-A_2)D^2V_1.
\tag{3.1}
\]
第一项产生
\[
\mathcal D_{2,r}
=
\int_M(\beta_2^2+\varepsilon)|D^{r+1}Z|^2.
\tag{3.2}
\]
因为 \(r+2\le s\)，第二项无需对 \(Z\) 做空间分部积分：
\[
\bigl\|
D^r[(\beta_1^2-\beta_2^2)A_1D^2V_1]
\bigr\|_2
\le C_R\|\omega\|_{H^r}.
\tag{3.3}
\]
这里使用
\[
\beta_1^2-\beta_2^2=(\beta_1+\beta_2)\omega
\]
以及 \(H^r\) 的代数性质。第三项同理给出
\[
\bigl\|
D^r[a_2(A_1-A_2)D^2V_1]
\bigr\|_2
\le C_R\|U_1-U_2\|_{H^r}.
\tag{3.4}
\]

这一低两阶的选择很重要：它使主系数差只需要输出的无权 \(H^s\) 上界，而不需要比较 \(\beta_1\) 与 \(\beta_2\)。

### 3.2 Lie 交叉项也可与第二分支权重对齐

对 Step 54 特别指出的项，使用
\[
d(\beta_1^2)-d(\beta_2^2)
=
2\beta_2\,d\omega+2\omega\,d\beta_1.
\tag{3.5}
\]
最高阶的 \(d\omega\) 项因此带有 \(\beta_2\)，而不是无法控制的 \(\beta_1+\beta_2\)。其能量贡献形如
\[
L_{\rm top}
=
\int D^rZ\;\beta_2W_1\,D^{r+1}\omega .
\]
一次分部积分给出
\[
L_{\rm top}
=
-\int \beta_2D^{r+1}Z\,W_1D^r\omega
+\text{较低阶项},
\]
故
\[
|L_{\rm top}|
\le
\eta\mathcal D_{2,r}
+C_{\eta,R}\|\omega\|_{H^r}^2.
\tag{3.6}
\]
这里没有使用 \(\beta_1/\beta_2\) 的比值。

### 3.3 运输方程的最高阶项恰好匹配同一权重

写
\[
v_i=\beta_i^2W(V_i).
\]
则
\[
v_1-v_2
=
(\beta_1^2-\beta_2^2)W(V_1)
+\beta_2^2\bigl(W(V_1)-W(V_2)\bigr).
\tag{3.7}
\]
第二项产生的最高阶贡献为
\[
I_{\rm top}
=
\int D^r\omega\;
\beta_2^2D^{r+1}Z\;
D\beta_2
\]
乘以统一有界的张量系数。因此
\[
|I_{\rm top}|
\le
\eta\mathcal D_{2,r}
+C_{\eta,R}\|\omega\|_{H^r}^2.
\tag{3.8}
\]
这正是同步输出结构所需要的吸收。无需比较 \(\beta_1\) 与 \(\beta_2\)；只需在度量差和运输差中都选择第二分支作为主分支。

在精确低阶项也都保留相同平方因子的前提下，所得候选能量为
\[
\frac d{dt}
\left(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2\right)
+c\mathcal D_{2,r}
\le
C_R\left(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2
+\|U_1-U_2\|_{H^r}^2\right).
\tag{3.9}
\]
相同初值下，Grönwall 给出
\[
\sup_{t\le T}
\left(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2\right)
\le
C_RT e^{C_RT}
\sup_{t\le T}\|U_1-U_2\|_{H^r}^2.
\tag{3.10}
\]
所以不同输出权重本身并不否定 Step 54 的同步输出设想。

---

## 4. 两个必须写入估计的精确条件

### 4.1 “\(r<s\)”太宽；至少需要两阶余量，除非另有新变量

若取 \(r=s-1\)，主系数差产生
\[
K_{\rm high}
=
\left\langle
D^rZ,\,
(\beta_1+\beta_2)\omega\,D^{s+1}V_1
\right\rangle .
\tag{4.1}
\]
单解能量只给出
\[
\beta_1D^{s+1}V_1\in L_t^2L_x^2,
\]
却不给出
\[
\beta_2D^{s+1}V_1\in L_t^2L_x^2.
\]
两个运输后的截断可以有不同零集，也没有
\(\beta_2\le C\beta_1\) 这样的估计。因此 (4.1) 不能由 Step 54 的 (5.2) 一致控制。取 \(r\le s-2\) 后，\(D^{r+2}V_1\) 已由无权 \(H^s\) 球控制，问题消失。

### 4.2 朴素对称化会把耗散降为 \(\beta_1\beta_2\)

若把主部写成平均系数，令
\[
P=D^{r+1}V_1,\quad Q=D^{r+1}V_2,\quad R=P-Q,
\]
则有精确恒等式
\[
\frac12(\beta_1^2-\beta_2^2)(P+Q)
=
\omega(\beta_1P+\beta_2Q)-\frac12\omega^2R.
\tag{4.2}
\]
最后一项在能量中产生
\[
+\frac12\omega^2|R|^2.
\]
它与平均主耗散
\[
-\frac12(\beta_1^2+\beta_2^2)|R|^2
\]
合并后只剩
\[
-\beta_1\beta_2|R|^2.
\tag{4.3}
\]
当其中一个截断为零时，这个量完全消失，而运输差仍可能含另一分支的平方权重。因而直接对称化不是合适的联合能量。前述“固定第二分支、主系数差按低两阶项处理”的组织方式避免了 (4.3)。

---

## 5. 对 Step 54 迭代判断的精确修正

- Step 53 使用输入度量 \(U\) 作为运输速度，确实留下
  \[
  \alpha_2^2D^{r+1}(U_1-U_2)
  \]
  这一输入高阶导数；输出 \(Z\) 的抛物耗散无法吸收它。仅靠高阶球插值只得到半 Hölder 依赖。这一撤回正确。

- Step 54 §3 中由 \(\alpha_1\) 与 \(\alpha_2\) 得到的权重错位并非内生现象。若度量差主部也按第二分支写，耗散是
  \[
  (\alpha_2^2+\varepsilon)|D^{r+1}Z|^2,
  \]
  正好吸收运输方程中的
  \(\alpha_2^2D^{r+1}Z\)。因此三角形的“输出速度”构造也可能在 \(r\le s-2\) 的分级下闭合；同步令主系数等于输出 \(\beta^2\) 不是由权重错位强制出来的。

- 同步输出系统仍然具有良好的结构。其完整成立还取决于 Step 54 未展开的精确 \(\mathcal F\)：所有含 \(D^{r+1}\omega\) 的度量项必须来自 \(d(\beta^2)\)，从而可用 (3.5) 提取 \(\beta_2\)；所有含 \(D^{r+1}(U_1-U_2)\) 的项必须带 \(\beta_2\) 或 \(\sqrt{\beta_2^2+\varepsilon}\)，以便分部积分后进入 (3.2)。若精确展开出现无权项
  \[
  \int D^rZ\,G\,D^{r+1}(U_1-U_2),
  \]
  则 \(H^r\) 输入距离不足。现有文件没有给出完整张量展开，故 (3.9)–(3.10) 目前是结构上可闭合的估计，而非已经逐项完成的证明。

总体上，Step 54 关于 IL 体积归一化的修正完全成立；关于耦合起始系统，它正确识别了“运输速度必须使用输出度量”这一核心变化，但不同平方权重可通过一致的分支取向处理。真正需要补充的是两阶 Sobolev 分级和精确 DeTurck 张量项的逐项恒等式。