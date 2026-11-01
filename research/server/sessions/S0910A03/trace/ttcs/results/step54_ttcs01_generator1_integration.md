# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 54,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step54_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step54_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop or falsify the synchronized-output construction in Step 54 for short-time existence of the exact fixed-cutoff normalized local Ricci flow. The goal is a rigorous mixed parabolic–transport iteration for the transported square coefficient, not a generic literature discussion. Starting from the proposed inner system with frozen metric U but output coefficient beta^2 and transport velocity beta^2 W(V), derive the exact joint high-order and difference energies. Determine whether every top derivative of V appearing in beta's transport equation can be absorbed by the beta-weighted parabolic dissipation of the same output, including when comparing two solutions with different beta weights. If a direct contraction fails, seek a good unknown, relative-flow/Lagrangian reformulation, symmetrizer, or graph norm that fixes the mismatch. State the exact remaining term if no closure works. Do not assume interpolation turns Hölder-1/2 into Lipschitz.

## Integrated Scientific Memo

## 结论

“同步输出系数”确实消除了 Step 54 中最初指出的**不同 \(\beta\)-权重失配**，但现有分支给出的完整闭合证明仍不成立。其算术平均主算子是正确且重要的对称化：

\[
P_1D^2V_1-P_2D^2V_2
=\bar P D^2Z+\delta P D^2V_*,
\qquad
\bar P=\frac{P_1+P_2}{2},
\]

其中

\[
P_i=(\beta_i^2+\varepsilon)U_i^{-1},\quad
Z=V_1-V_2,\quad V_*=\frac{V_1+V_2}{2}.
\]

\(\bar P\) 给出双边耗散

\[
\bar P(\xi,\xi)\ge c\,
(\beta_1^2+\beta_2^2+2\varepsilon)|\xi|^2,
\]

所以 transport 差分中所有 \(D^{r+1}Z\) 项都能被同一输出的对称耗散吸收。**真正尚未闭合的对象不是 transport 顶阶项，而是主系数差源**
\[
\boxed{\delta P\,D^2V_*}.
\]

在所要求的低阶 \(H^r\) 收缩范数内，现有论证无法对该项取得 \(\varepsilon\)-一致 Lipschitz 估计。

---

## 1. 应使用的精确内系统

相对于固定背景 \(\bar g\) 和 \(D=\bar\nabla\)，令

\[
W^k(G)=\frac12G^{kj}G^{pq}
(D_pG_{qj}+D_qG_{pj}-D_jG_{pq}).
\]

对给定冻结路径 \(U\)，同步系统可写为

\[
\begin{aligned}
\partial_tV_{ij}
={}&(\beta^2+\varepsilon)U^{ab}D_aD_bV_{ij}
+\beta^2\mathcal R_{ij}(U,V)
+\beta^2\mathcal Q_{ij}(U,DU)\\
&+2\beta\bigl(D_i\beta\,W_j(U)+D_j\beta\,W_i(U)\bigr)
-2\beta^2V_{ij},\\
\partial_t\beta
={}&\beta^2W(V)^kD_k\beta ,
\end{aligned}
\tag{1}
\]

初值为 \(V(0)=g_0,\ \beta(0)=\chi\)。这里 \(\mathcal R,\mathcal Q\) 是 Xu 固定背景展开中的曲率和一阶二次项。

在固定点 \(U=V\) 时，

\[
\partial_tV
=-2\beta^2(\operatorname{Ric}_V+V)
+\mathcal L_{\beta^2W(V)}V
+\varepsilon V^{ab}D_aD_bV.
\tag{2}
\]

因此 \(\varepsilon\to0\) 后确为正确的 transported-cutoff DeTurck 系统。

---

## 2. 单解高阶能量确实闭合

取 \(m>n/2+4\)，定义

\[
E_m=\frac12\bigl(\|V\|_{H^m}^2+\|\beta\|_{H^m}^2\bigr),
\]

\[
\mathcal D_m
=\sum_{k\le m}\int_M(\beta^2+\varepsilon)
|D^{k+1}V|^2\,d\mu_{\bar g}.
\]

### Metric 主项

分部积分给出

\[
\left\langle D^mV,
D^m\bigl((\beta^2+\varepsilon)U^{-1}D^2V\bigr)\right\rangle
\le -c\mathcal D_m+\text{commutators}.
\]

因为

\[
D(\beta^2)=2\beta D\beta,
\]

所有由系数导数产生的顶阶项都带一个 \(\beta\)，故可用
\(\|\beta D^{m+1}V\|_2\) 吸收，不需要除以 \(\beta\)。

Lie 交叉项

\[
2\beta\,\operatorname{sym}(D\beta\otimes W(U)^\flat)
\]

产生的 \(D^{m+1}\beta\) 项，可将一阶导数从 \(\beta\) 移到 \(V\)，得到

\[
\int D^{m+1}V*\beta W(U)*D^m\beta,
\]

从而由 \(\mathcal D_m\) 吸收。

### Transport 顶阶项

对

\[
\partial_t\beta=\beta^2W(V)\cdot D\beta
\]

做 \(H^m\) 能量，唯一含 \(D^{m+1}V\) 的项为

\[
\int D^m\beta\,
\beta^2\,\mathsf L_V(D^{m+1}V)*D\beta.
\]

于是

\[
|\cdot|
\le C_R\|\beta D^{m+1}V\|_2\|\beta\|_{H^m}
\le \eta\mathcal D_m+C_{\eta,R}\|\beta\|_{H^m}^2.
\]

故可严格得到

\[
\boxed{
\frac d{dt}E_m+c\mathcal D_m
\le C_R(1+E_m),
}
\tag{3}
\]

且常数对 \(0<\varepsilon\le1\) 一致。这个结论与 Yang 所述 mixed parabolic–transport tame-energy 机制一致；Xu 的原固定 \(\chi\) 证明本身没有处理这一动态 transport 变量，但提供了 metric 侧的加权分部积分结构。

---

## 3. 差分中 transport 权重失配由算术平均消除

令两组解对应 \(U_i\)：

\[
Z=V_1-V_2,\qquad \omega=\beta_1-\beta_2.
\]

定义

\[
S=\beta_1^2+\beta_2^2+2\varepsilon.
\]

主算子精确满足

\[
P_1D^2V_1-P_2D^2V_2
=\bar P D^2Z+\delta P D^2V_*,
\tag{4}
\]

并有

\[
\bar P\ge cS\bar g^{-1}.
\tag{5}
\]

因此 metric 差分耗散为

\[
\mathcal D_r^\Delta
=\sum_{k\le r}\int_M S|D^{k+1}Z|^2.
\tag{6}
\]

transport 速度 \(v_i=\beta_i^2W(V_i)\) 的差可沿线段
\((V_\theta,\beta_\theta)\) 写成

\[
\delta v
=\int_0^1\left[
2\beta_\theta\omega W(V_\theta)
+\beta_\theta^2DW_{V_\theta}[Z]
\right]\,d\theta.
\]

由于

\[
|\beta_\theta|^2
\le 2(\beta_1^2+\beta_2^2)\le 2S,
\tag{7}
\]

transport 能量中的顶阶项

\[
I_r=\int_0^1\!\!\int
D^r\omega\,
\beta_\theta^2\mathsf L_{V_\theta}(D^{r+1}Z)
*D\beta_*\,d\theta
\]

满足

\[
|I_r|
\le \eta\mathcal D_r^\Delta
+C_{\eta,R}\|\omega\|_{H^r}^2.
\tag{8}
\]

同理，metric 方程中由 \(D^{r+1}\omega\) 引起的项分部积分后成为

\[
\int D^{r+1}Z*\beta_\theta W(U_\theta)*D^r\omega,
\]

也由 (6) 吸收。

因此，Step 54 中具体的项

\[
|\beta_2(\beta_2-\beta_1)|
\,|D^{r+1}Z|\,|D^r\omega|
\]

不再是最终障碍；算术平均确实提供了所缺少的双边权重。

---

## 4. 分支证明中的致命缺口：\(\delta P D^2V_*\)

分支声称

\[
\|\delta P\,D^2V_*\|_{H^r}
\le C_R(\|\omega\|_{H^r}+\|U_1-U_2\|_{H^r}),
\tag{9}
\]

理由是 \(V_*\) 在 \(H^{r+2}\) 高阶球内。该估计一般是假的。

展开最高 Leibniz 项：

\[
D^r(\delta P\,D^2V_*)
\supset
\delta P\,D^{r+2}V_*.
\tag{10}
\]

于是通常只能得到

\[
\|\delta P\,D^2V_*\|_{H^r}
\lesssim
\|\delta P\|_{H^r}\|D^2V_*\|_{L^\infty}
+
\|\delta P\|_{L^\infty}\|V_*\|_{H^{r+2}}.
\tag{11}
\]

第二项为

\[
C_R\|\delta P\|_{L^\infty},
\]

而不是 \(C_R\|\delta P\|_{H^r}\) 的小倍数问题；虽有
\(\|\delta P\|_{L^\infty}\lesssim\|\delta P\|_{H^r}\)，乘上 \(D^rZ\) 后确实给出线性差分，但关键是 \(\delta P\) 的 \(\omega\)-部分没有 \(S\) 因子：

\[
\delta P
=(\beta_1^2-\beta_2^2)A
+\frac S2(U_1^{-1}-U_2^{-1}),
\tag{12}
\]

其中 \(A=(U_1^{-1}+U_2^{-1})/2\)。第一部分为

\[
(\beta_1+\beta_2)\omega\,A,
\]

只含一个输出权重。对应能量项为

\[
\boxed{
\int_M
D^rZ*
(\beta_1+\beta_2)\omega\,A*
D^{r+2}V_*.
}
\tag{13}
\]

现有单解估计只控制

\[
\beta_iD^{r+1}V_i\in L_t^2L_x^2,
\]

并不控制 \(D^{r+2}V_*\)，也不控制
\(\sqrt S\,D^{r+2}V_*\)。若直接使用严格抛物正则性，则常数通常含
\(\varepsilon^{-1/2}\) 或更坏，不能用于 \(\varepsilon\)-一致收缩。

即使把 (13) 空间分部积分一次，也会出现

\[
\int D^{r+1}Z*
(\beta_1+\beta_2)\omega*
D^{r+1}V_*,
\tag{14}
\]

以及

\[
\int D^rZ*D[(\beta_1+\beta_2)\omega]*
D^{r+1}V_*.
\tag{15}
\]

(14) 可望由 \(S\)-耗散和各分支的 \(\beta_iD^{r+1}V_i\) 控制；但 (15) 含

\[
D\omega\,(\beta_1+\beta_2)D^{r+1}V_*,
\]

其中当导数落在 \(\omega\) 上时不再保证足够的 \(\beta_i\) 配对。标准 Cauchy–Schwarz 会要求 transport 差分具有加权导数控制，或要求对单解有更高阶加权耗散。

所以当前能严格写出的差分能量是

\[
\frac d{dt}E_r^\Delta
+c\mathcal D_r^\Delta
\le
C_RE_r^\Delta+C_R\|dU\|_{H^r}^2
+\mathcal K_r,
\tag{16}
\]

其中精确未闭合项可取为

\[
\boxed{
\mathcal K_r
=
\sum_{|I|=r}
\int_M
D^IZ*
D^I\!\left[
(\beta_1^2-\beta_2^2)
A\,D^2V_*
\right]\,d\mu_{\bar g}.
}
\tag{17}
\]

其最高未决成分就是 (13)，或分部积分后的 (15)。

---

## 5. 可行的修复对象

算术平均已经是正确的 metric 对称化；剩余修复必须针对 (17)，而不是 transport 顶阶项。

### A. 加权高一阶差分图范数

加入

\[
\int_0^T\!\!\int S|D^{r+2}V_*|^2
\quad\text{或相应的各分支高阶耗散},
\]

并为 \(D\omega\) 配置与 \(\beta_iD^{r+1}V_i\) 相容的交叉能量。这需要在 \(m=r+1\) 或更高层同时运行差分估计，不能仅依靠一个固定 \(H^{r+2}\) 球。

### B. 主系数相对流/Lagrangian 变量

沿各自 transport 流保持

\[
\beta_i\circ\varphi_i=\chi.
\]

若先把两解拉回同一相对流坐标，\(\beta_1^2-\beta_2^2\) 的主系数差可能转化为相对 diffeomorphism 差，从而与 Yang 的 \((\widehat g,\varphi)\) 线性系统中的 \(\psi\)-变量配对。Yang 的原文确实采用 metric–diffeomorphism 的 smooth-tame 能量，而不是声称简单低阶 Banach 收缩。

### C. Good unknown

需要构造类似

\[
\mathcal Z
=Z-\mathcal A(V_*,\beta_*)\,\omega
\]

使主符号中

\[
(\beta_1^2-\beta_2^2)D^2V_*
\]

被 \(\partial_t\omega\) 或 transport 导数抵消。仅以 \(Z,\omega\) 的对角能量不产生这种抵消；具体 \(\mathcal A\) 必须由完整线性化主符号求出。

---

## 最终判定

1. **单解同步 mixed parabolic–transport 高阶能量闭合，且可做到 \(\varepsilon\)-一致。**
2. **算术平均主算子完全修复了不同输出权重导致的 transport 顶阶失配。**
3. **但现有直接 \(C_TH^r\) Banach 收缩仍未证明。**
4. 未闭合的精确对象是
   \[
   D^rZ\cdot D^r\!\left[(\beta_1^2-\beta_2^2)A D^2V_*\right],
   \]
   尤其是
   \[
   D^rZ\,(\beta_1+\beta_2)\omega\,D^{r+2}V_*.
   \]
5. 因而目前不能从所给论证推出完整的 exact fixed-cutoff normalized local Ricci flow 短时存在定理；需要一个高阶加权图范数、Yang 式相对流变量，或能消去该主系数变化项的 good unknown。