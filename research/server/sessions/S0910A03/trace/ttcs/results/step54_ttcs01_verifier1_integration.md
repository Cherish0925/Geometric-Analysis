# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 54,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step54_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step54_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the Step 54 strategic and mathematical corrections. First check the family-uniform normalization: from a retained disjoint core set of total volume a fixed fraction of Vol(M)~A and ∫D≤Cδ²Vol(M), does weighted averaging indeed give a core with mean O(δ²), invalidating the claimed intrinsic A^{-1/2} loss? Check also the fixed-radius Sobolev–energy upper bound gamma≤Cr²sqrt(1+kappa²) and identify any hypothesis that could still introduce A-dependence. Second, inspect the synchronized-output coupled iteration and test whether its proposed joint difference estimate is actually viable, especially the different output weights beta_1,beta_2. Return precise derivations or a counterterm, not a procedural review.

## Integrated Scientific Memo

## 核验结论

### 1. 家族统一归一化：Step 54 的修正成立

设终端互不相交核心
\[
P=\bigsqcup_\alpha \Omega_\alpha,\qquad
D_\alpha=\int_{\Omega_\alpha}\mathfrak D\,d\mu_{g(T)},\qquad
V_\alpha=\operatorname{Vol}_{g(T)}(\Omega_\alpha).
\]
若
\[
\int_M\mathfrak D\,d\mu_{g(T)}
\le C_D\delta^2\operatorname{Vol}_{g(0)}(M)
\]
且初始核心总量满足
\[
\sum_\alpha\operatorname{Vol}_{g(0)}(\Omega_\alpha)
\ge \alpha_0\operatorname{Vol}_{g(0)}(M),
\]
终端双 Lipschitz 比较又给出
\[
\sum_\alpha V_\alpha
\ge c_{\rm vol}\alpha_0\operatorname{Vol}_{g(0)}(M),
\]
则由 \(\mathfrak D\ge0\) 和核心不交，
\[
\min_\alpha\frac{D_\alpha}{V_\alpha}
\le
\frac{\sum_\alpha D_\alpha}{\sum_\alpha V_\alpha}
\le
\frac{C_D}{c_{\rm vol}\alpha_0}\delta^2.
\]
所以某个核心满足
\[
\fint_{\Omega_\alpha}\mathfrak D\le C\delta^2,
\]
常数与 \(A\) 无关。

事实上不必先写 \(\operatorname{Vol}(M)\asymp A\)：分子、分母都直接按总流形体积归一化。若写成 \(A\)-标度，也只是
\[
\int_M\mathfrak D=O(\delta^2A),\qquad
\operatorname{Vol}(P)\ge cA,
\]
相除后 \(A\) 消失。此前的 \(A^{-1/2}\) 损失来自把全局缺陷分配给一个预先指定的固定球，而不是从总量占固定比例的整族核心中作体积加权选择。

因此，Step 53/A02 Step 52 所称的内生 \(A^{-1/2}\) 损失不成立。

---

### 2. 固定半径 Sobolev–能量乘积：上界正确

若好点 \(x_\alpha\) 满足
\[
\sup_{0<\rho\le1}
\fint_{B_\rho(x_\alpha)}|\operatorname{Rm}|^2\le\kappa^2
\]
并固定 \(r>0\)、\(Cr\le1\)，则
\[
K_{2,\alpha}(0)
=\int\eta_\alpha^2(1+|\operatorname{Rm}|^2)
\le(1+\kappa^2)\operatorname{Vol}B_{Cr}(x_\alpha).
\]
四维局部体积归一化 Sobolev 不等式给出
\[
\mathcal S_\alpha
\le Cr^2\operatorname{Vol}B_{Cr}(x_\alpha)^{-1/2}.
\]
故
\[
\gamma_\alpha
=\mathcal S_\alpha K_{2,\alpha}(0)^{1/2}
\le Cr^2\sqrt{1+\kappa^2}.
\]
塌缩体积严格抵消。若
\[
\kappa^2=4C_{\rm HL}\Lambda,\qquad
\Lambda=\frac{\int_M(1+|\operatorname{Rm}|^2)}
{\operatorname{Vol}(M)}
\]
有家族统一上界，则可选一个固定的小 \(r\)，无需 \(r\asymp A^{1/4}\)。

A02 Step 52 另有方向错误：即使
\[
\mathcal S_\alpha\ge cr^2\operatorname{Vol}(B)^{-1/2},
\qquad
K_{2,\alpha}\le C\operatorname{Vol}(B),
\]
也不能推出 \(\mathcal S_\alpha K_{2,\alpha}^{1/2}\) 的下界，因为第二个不等式方向不支持该结论。

这里仍可能间接引入 \(A\)-依赖的假设是：

- 曲率—体积比 \(\Lambda\) 是否统一；
- Ricci 下界，从而 doubling、局部 Sobolev 常数及着色数是否统一；
- 保留核心比例 \(\alpha_0\) 是否统一；
- \(Q(T)\le C_QQ(0)\)、共同观察时间及终端双 Lipschitz 漂移是否统一；
- 高阶截断导数、精确流构造及终端导数估计是否仅逐数据有界而非家族统一。

故归一化与临界乘积本身没有 \(A\)-损失；共同时间精确流仍是可能携带家族依赖的接口。

---

## 3. 同步输出迭代：不同的 \(\beta_1,\beta_2\) 不构成本质反例

考虑主部
\[
\partial_tV_i=(\beta_i^2+\varepsilon)A(U_i)D^2V_i+\cdots,
\qquad
\partial_t\beta_i=\beta_i^2W(V_i)\cdot D\beta_i,
\]
记
\[
Z=V_1-V_2,\qquad \omega=\beta_1-\beta_2.
\]

Step 54 担忧度量差耗散带 \(\beta_1\)，而运输差最高项带 \(\beta_2\)。但差分可以一致地以第二分支为主分支组织：
\[
\begin{aligned}
&(\beta_1^2+\varepsilon)A_1D^2V_1
-(\beta_2^2+\varepsilon)A_2D^2V_2\\
&\quad=(\beta_2^2+\varepsilon)A_2D^2Z
+(\beta_1^2-\beta_2^2)A_1D^2V_1
+(\beta_2^2+\varepsilon)(A_1-A_2)D^2V_1.
\end{aligned}
\]
第一项产生耗散
\[
\mathcal D_{2,r}
=\int(\beta_2^2+\varepsilon)|D^{r+1}Z|^2.
\]

同时，运输速度差按
\[
\beta_1^2W(V_1)-\beta_2^2W(V_2)
=
(\beta_1^2-\beta_2^2)W(V_1)
+\beta_2^2\bigl(W(V_1)-W(V_2)\bigr)
\]
展开。最高阶项为
\[
I_{\rm top}
\sim
\int D^r\omega\,
\beta_2^2D^{r+1}Z\,D\beta_2,
\]
从而
\[
|I_{\rm top}|
\le
\eta\mathcal D_{2,r}
+C_{\eta,R}\|\omega\|_{H^r}^2.
\]
所以不需要比较 \(\beta_1/\beta_2\)，也不需要把 \(\beta_2\)-权重转换成 \(\beta_1\)-权重。Step 54 的分解
\[
\alpha_2^2=\alpha_1\alpha_2+\alpha_2(\alpha_2-\alpha_1)
\]
制造的权重错配不是内生的；它来自度量差方程与运输差方程选用了不同的参考分支。

Lie 交叉项也可同样对齐。使用精确恒等式
\[
d(\beta_1^2)-d(\beta_2^2)
=2\beta_2\,d\omega+2\omega\,d\beta_1,
\]
其最高阶 \(d\omega\) 项带 \(\beta_2\)。一次分部积分后得到
\[
\int D^rZ\,\beta_2W_1D^{r+1}\omega
=
-\int \beta_2D^{r+1}Z\,W_1D^r\omega+\text{低阶项},
\]
故也可由 \(\mathcal D_{2,r}\) 吸收。

---

## 4. 可行估计需要两阶 Sobolev 余量

取
\[
s>\frac n2+2,\qquad r\le s-2.
\]
在统一 \(H^s\) 输出球内，因 \(H^r\) 为代数，
\[
\left\|
D^r\bigl[(\beta_1^2-\beta_2^2)A_1D^2V_1\bigr]
\right\|_2
\le C_R\|\omega\|_{H^r},
\]
以及
\[
\left\|
D^r\bigl[(\beta_2^2+\varepsilon)(A_1-A_2)D^2V_1\bigr]
\right\|_2
\le C_R\|U_1-U_2\|_{H^r},
\]
因为 \(D^{r+2}V_1\) 已由无权 \(H^s\) 上界控制。这样候选联合差分估计为
\[
\frac d{dt}
\bigl(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2\bigr)
+c\mathcal D_{2,r}
\le
C_R\bigl(
\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2
+\|U_1-U_2\|_{H^r}^2
\bigr).
\]
相同初值下，
\[
\sup_{t\le T}
\bigl(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2\bigr)
\le
C_RT e^{C_RT}
\sup_{t\le T}\|U_1-U_2\|_{H^r}^2.
\]

但 Step 54 的宽泛条件“\(r<s\)”不足。若 \(r=s-1\)，主系数差包含
\[
\left\langle
D^rZ,\,
(\beta_1+\beta_2)\omega\,D^{s+1}V_1
\right\rangle.
\]
单解估计只控制
\[
\beta_1D^{s+1}V_1\in L_t^2L_x^2,
\]
并不控制
\[
\beta_2D^{s+1}V_1.
\]
由于两输出截断可能有不同零集，通常没有 \(\beta_2\le C\beta_1\)。这是真正的反项。因此，朴素方案至少需要 \(r\le s-2\)，除非引入额外权重比较、图范数或好未知量。

同样不宜把两主系数直接对称化。设
\[
P=D^{r+1}V_1,\quad Q=D^{r+1}V_2,\quad R=P-Q,
\]
则
\[
\frac12(\beta_1^2-\beta_2^2)(P+Q)
=
\omega(\beta_1P+\beta_2Q)-\frac12\omega^2R.
\]
后项会把平均耗散
\[
-\frac12(\beta_1^2+\beta_2^2)|R|^2
\]
降为
\[
-\beta_1\beta_2|R|^2,
\]
当任一权重消失时退化过强。固定同一参考分支更合适。

---

## 5. 最终判定

1. **家族归一化修正成立**：体积加权核心选择给出 \(O(\delta^2)\) 平均缺陷，没有内生 \(A^{-1/2}\) 损失。
2. **固定半径临界乘积上界成立**：
   \[
   \gamma\le Cr^2\sqrt{1+\kappa^2}.
   \]
   A02 的 \(A^{1/2}\) 下界推导既使用了不必要的半径选择，也混用了上下界方向。
3. **Step 53 的冻结输入速度收缩确实失败**：它要求控制 \(D^{r+1}(U_1-U_2)\)，输出耗散不能吸收输入差；插值只给半 Hölder。
4. **Step 54 对同步输出方案的悲观权重判断需修正**：不同 \(\beta_i\) 可通过统一选择第二分支来匹配，不是自动障碍。
5. **联合估计尚未成为完整证明**：必须取至少两阶余量 \(r\le s-2\)，并逐项展开精确 DeTurck 下阶项。若出现无权反项
   \[
   \int D^rZ\,G\,D^{r+1}(U_1-U_2),
   \]
   或不由 \(d(\beta^2)\) 提供 \(\beta_2\) 因子的
   \(D^{r+1}\omega\) 项，则现有 \(H^r\) 输入距离仍不足。现有材料未提供完整张量展开，故上述结果证明了权重机制“可行”，尚未证明完整的目标引理 (5.3)。