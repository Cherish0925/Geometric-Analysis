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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step54_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step54_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the exact synchronized-output fixed-background ledger in the new Step 54 supplement as a mathematician working on degenerate quasilinear parabolic systems. Reconstruct the frozen inner system from the exact DeTurck identity and check every top-order family in the single-solution H^s estimate and the branch-2-oriented H^{s-2} difference estimate. Focus on whether any term produces an unweighted D^{r+1}(U1-U2), an unweighted D^{r+1}omega, a missing derivative of V or beta, or an epsilon-dependent constant. Check the product estimates (4.4)-(4.5), integrations (4.8),(4.12)-(4.13), and transport (4.14)-(4.16). Also assess whether standard Galerkin/parabolic-transport construction plus the stated uniform tame hierarchy can pass epsilon to zero smoothly across the zero set, or identify the exact missing estimate. Do not accept the theorem merely because the schematic ledger looks plausible; return explicit corrected formulas and status.

## Integrated Scientific Memo

## 核验结论

Step 54 的**有限阶能量账本基本可闭合**，且 \(r=s-2\) 的两阶降阶确实消除了 Step 53 的半 Hölder 导数损失。精确 DeTurck 展开未产生遗漏的顶阶族；在正确组织 Lie 差分后，也没有不可控的

\[
D^{r+1}(U_1-U_2),\qquad D^{r+1}\omega,\qquad D^{r+1}Z
\]

或 \(\varepsilon^{-1}\) 常数。

但目前只能确认：

1. 单解 \(H^s\) 一致先验估计；
2. branch-2 定向的 \(H^{s-2}\) 差分先验估计；

尚不能确认完整启动定理。缺口是固定 \(\varepsilon\) 的耦合构造细节，以及更关键的、共同时间区间上的全阶 \(\varepsilon\)-一致 tame hierarchy；仅凭有限阶估计和“标准抛物—输运理论”不能推出跨越 \(\{\beta=0\}\) 的光滑极限。

---

# 1. 精确固定背景系统

令 \(D=\bar\nabla\)，并定义
\[
A(G)^k{}_{ab}
=\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}
=\frac12G^{k\ell}
(D_aG_{b\ell}+D_bG_{a\ell}-D_\ell G_{ab}),
\]
\[
W^k(G)=G^{ab}A(G)^k{}_{ab},
\qquad
\mathcal W_j(G):=G_{jk}W^k(G)
=\frac12G^{pq}(D_pG_{qj}+D_qG_{pj}-D_jG_{pq}).
\]

与 Xu (2.3) 完全一致的固定背景恒等式为
\[
-2\operatorname{Ric}(G)+\mathcal L_{W(G)}G
=G^{ab}D_aD_bG+\mathcal R_{\bar g}(G,G)+\mathcal Q(G,DG),
\]
其中
\[
\mathcal R_{\bar g}(U,V)_{ij}
=
-U^{ab}\left(
V_{ip}\bar g^{pq}\bar R_{jaqb}
+
V_{jp}\bar g^{pq}\bar R_{iaqb}
\right),
\]
而
\[
\begin{aligned}
\mathcal Q(U,DU)_{ij}
=\frac12U^{ab}U^{pq}\bigl(&
D_iU_{pa}D_jU_{qb}
+2D_aU_{jp}D_qU_{ib}\\
&-2D_aU_{jp}D_bU_{iq}
-2D_jU_{pa}D_bU_{iq}
-2D_iU_{pa}D_bU_{jq}
\bigr).
\end{aligned}
\]

若 \(p\odot q=p_iq_j+p_jq_i\)，则
\[
\mathcal L_{\beta^2W(G)}G
=\beta^2\mathcal L_{W(G)}G+d(\beta^2)\odot\mathcal W(G).
\]

因此精确同步输出冻结系统应写成
\[
\boxed{
\begin{cases}
V_t=(\beta^2+\varepsilon)U^{ab}D_aD_bV
+\beta^2\mathcal R_{\bar g}(U,V)
+\beta^2\mathcal Q(U,DU)-2\beta^2V\\
\hspace{24mm}+d(\beta^2)\odot\mathcal W(U),\\[1mm]
\beta_t=\beta^2W(V)\cdot D\beta.
\end{cases}}
\]

这正对应 Xu 的 \(D_{ij}(U,V),E_{ij}(U,DU),F_{ij}(U,DU,\chi,D\chi)\)。因此 \(R,Q,\) Lie-cross 三族是完整的；未漏掉额外顶阶 DeTurck 项。

在固定点 \(U=V=G\) 时，仅多出
\[
\varepsilon G^{ab}D_aD_bG.
\]

---

# 2. 单解 \(H^s\) 估计

取 \(s>n/2+4\)，假设 \(U\) 一致正定，且 \(U,V,\beta\) 位于固定 \(H^s\) 球中。

## 2.1 主部

令 \(a=\beta^2+\varepsilon\)。顶阶积分为
\[
\begin{aligned}
\langle D^sV,D^s(aU^{ab}D_aD_bV)\rangle
={}&-\int aU^{ab}\langle D_aD^sV,D_bD^sV\rangle\\
&+O\int \bigl(|\beta D\beta|+a|DU|\bigr)
|D^{s+1}V||D^sV|+\mathrm{l.o.t.}
\end{aligned}
\]

其中
\[
|\beta D\beta|\,|D^{s+1}V|
\le C_R|\beta D^{s+1}V|,
\]
而
\[
a|DU||D^{s+1}V||D^sV|
\le \eta a|D^{s+1}V|^2+C_{\eta,R}a|D^sV|^2.
\]

特别地，\(\varepsilon DU^{-1}\) 族由
\[
\varepsilon |D^{s+1}V|^2
\]
吸收，不需要除以 \(\varepsilon\)。当至少两个导数落在 \(aU^{-1}\) 上时，另一因子至多为 \(D^sV\)，由 Moser 估计控制。Step 54 的短表没有列出这整族主系数交换子，但它是低阶可控族。

## 2.2 冻结二次项

唯一超出 \(s\) 阶的结构是
\[
D^s(\beta^2\mathcal Q(U,DU))
=
\beta^2\mathsf A(U,DU)D^{s+1}U+\mathrm{l.o.t.}
\]
配对后
\[
\begin{aligned}
\int D^sV\,\beta^2\mathsf A\,D^{s+1}U
={}&-\int \beta^2D^{s+1}V\,\mathsf A\,D^sU\\
&-\int D^sV\,D(\beta^2\mathsf A)D^sU+\cdots .
\end{aligned}
\]
故不遗留无权 \(D^{s+1}U\)。

## 2.3 Lie cross

顶阶项为
\[
\beta\,\mathcal W(U)D^{s+1}\beta,
\qquad
\beta D\beta\,\mathsf A(U)D^{s+1}U.
\]
各自积分一次：
\[
\begin{aligned}
\int D^sV\,\beta\mathcal W(U)D^{s+1}\beta
={}&-\int \beta\mathcal W(U)D^{s+1}V\,D^s\beta+\mathrm{l.o.t.},
\\
\int D^sV\,\beta D\beta\,\mathsf A D^{s+1}U
={}&-\int \beta D\beta\,\mathsf A D^{s+1}V\,D^sU+\mathrm{l.o.t.}
\end{aligned}
\]
均由 \(\beta^2|D^{s+1}V|^2\) 吸收。

## 2.4 输运

令 \(b=\beta^2W(V)\)。则
\[
\frac12\frac d{dt}\|D^s\beta\|_2^2
=
-\frac12\int(\operatorname{div}b)|D^s\beta|^2
+\int D^s\beta\,[D^s,b\cdot D]\beta.
\]
显式的 \(D^{s+1}\beta\) 对流顶项经分部积分消失。唯一顶阶度量项为
\[
\int D^s\beta\,
\beta^2\mathsf A(V)D^{s+1}V\,D\beta,
\]
满足
\[
|I_s|
\le \eta\|\beta D^{s+1}V\|_2^2
+C_{\eta,R}\|\beta\|_{H^s}^2.
\]

因此
\[
\boxed{
\frac d{dt}\left(\|V\|_{H^s}^2+A\|\beta\|_{H^s}^2\right)
+c\sum_{k\le s}\int(\beta^2+\varepsilon)|D^{k+1}V|^2
\le C_R(1+\|V\|_{H^s}^2+\|\beta\|_{H^s}^2)}
\]
成立，常数对 \(0<\varepsilon\le1\) 一致。

---

# 3. \(H^r\), \(r=s-2\), 差分估计

记
\[
Z=V_1-V_2,\qquad
\omega=\beta_1-\beta_2,\qquad
H=U_1-U_2.
\]

## 3.1 主部及 (4.4)–(4.5)

精确分解为
\[
\begin{aligned}
&a_1U_1^{-1}D^2V_1-a_2U_2^{-1}D^2V_2\\
&\quad=a_2U_2^{-1}D^2Z
+(\beta_1^2-\beta_2^2)U_1^{-1}D^2V_1
+a_2(U_1^{-1}-U_2^{-1})D^2V_1,
\end{aligned}
\]
其中 \(a_i=\beta_i^2+\varepsilon\)。

因 \(r>n/2+2\)、\(r+2=s\)，
\[
\|\beta_1^2-\beta_2^2\|_{H^r}
\le C_R\|\omega\|_{H^r},
\]
\[
\|U_1^{-1}-U_2^{-1}\|_{H^r}
\le C_R\|H\|_{H^r},
\qquad
\|D^2V_1\|_{H^r}\le R.
\]
故正确公式是
\[
\boxed{
\|(\beta_1^2-\beta_2^2)U_1^{-1}D^2V_1\|_{H^r}
\le C_R\|\omega\|_{H^r}}
\]
及
\[
\boxed{
\|a_2(U_1^{-1}-U_2^{-1})D^2V_1\|_{H^r}
\le C_R\|H\|_{H^r}.}
\]

这两式正是两阶降阶的核心；未使用差分插值，因而没有半 Hölder 损失。主部交换子中的 \(\varepsilon DU_2^{-1}\) 仍由 branch-2 的 \(\varepsilon\)-耗散吸收。

## 3.2 \(Q\) 差分及 (4.8)

由于 \(Q\) 对 \(DU\) 二次，
\[
Q(U_1,DU_1)-Q(U_2,DU_2)
=\mathsf A^aD_aH+\mathsf B H.
\]
顶项为
\[
\int D^rZ\,\beta_2^2\mathsf A\,D^{r+1}H.
\]
正确分部积分为
\[
\begin{aligned}
\int D^rZ\,\beta_2^2\mathsf A\,D^{r+1}H
={}&-\int \beta_2^2D^{r+1}Z\,\mathsf A\,D^rH\\
&-\int D^rZ\,D(\beta_2^2\mathsf A)D^rH+\cdots,
\end{aligned}
\]
故
\[
|I_Q|
\le \eta\|\beta_2D^{r+1}Z\|_2^2
+C_{\eta,R}(\|H\|_{H^r}^2+\|Z\|_{H^r}^2).
\]
没有无权 \(D^{r+1}H\) 留下。

---

# 4. Lie 差分：需要更正账本的表述

这里两支独立核验给出了看似不同的系数 \(W(U_1)\) 与 \(W(U_2)\)。两者其实来自两种都正确的代数分解，但不能混用其余项。

最简洁的精确 branch-2 分解是
\[
\boxed{
\begin{aligned}
&d(\beta_1^2)\odot\mathcal W(U_1)
-d(\beta_2^2)\odot\mathcal W(U_2)\\
&=
\bigl(d(\beta_1^2)-d(\beta_2^2)\bigr)\odot\mathcal W(U_1)
+d(\beta_2^2)\odot\bigl(\mathcal W(U_1)-\mathcal W(U_2)\bigr),
\end{aligned}}
\]
且
\[
d(\beta_1^2)-d(\beta_2^2)
=2\beta_2d\omega+2\omega d\beta_1.
\]

在此分解下，顶阶 cutoff 项应为
\[
\boxed{
I_\omega
=\int D^rZ\,\beta_2\mathcal W(U_1)D^{r+1}\omega,}
\]
而不是 Step 54 (4.11) 中的 \(\mathcal W(U_2)\)。其分部积分为
\[
\begin{aligned}
I_\omega
={}&-\int\beta_2D^{r+1}Z\,\mathcal W(U_1)D^r\omega\\
&-\int D^rZ\,D(\beta_2\mathcal W(U_1))D^r\omega+\cdots,
\end{aligned}
\]
故由 branch-2 耗散吸收。

另一种分解
\[
\begin{aligned}
&d(\beta_1^2)\mathcal W(U_1)-d(\beta_2^2)\mathcal W(U_2)\\
&=d(\beta_2^2)\Delta\mathcal W+
\bigl(d(\beta_1^2)-d(\beta_2^2)\bigr)\mathcal W(U_2)
+\bigl(d(\beta_1^2)-d(\beta_2^2)\bigr)\Delta\mathcal W
\end{aligned}
\]
也合法，并会产生 Step 54 的 \(\mathcal W(U_2)\)，但必须保留第三个交叉项；不能把它统称为“普通 \(H^r\) 乘积”。

对输入度量顶项，
\[
\mathcal W(U_1)-\mathcal W(U_2)
=\mathsf P^aD_aH+\mathsf P_0H,
\]
且 \(d(\beta_2^2)=2\beta_2d\beta_2\)，所以
\[
\int D^rZ\,\beta_2D\beta_2\,\mathsf P D^{r+1}H
\]
分部积分为
\[
\begin{aligned}
&-\int\beta_2D\beta_2\,\mathsf P D^{r+1}Z\,D^rH\\
&\quad-\int D^rZ\,D(\beta_2D\beta_2\,\mathsf P)D^rH+\cdots .
\end{aligned}
\]
同样没有无权 \(D^{r+1}H\)。

### 必须显式采用的规则

凡出现完整分支的高阶因子，如
\[
\omega\,\mathcal W(U_2)\,D^{r+1}\beta_1,
\qquad
\omega\,D^{r+1}U_1,
\]
应直接使用单支 \(H^s\) 球：
\[
\|D^{r+1}\beta_1\|_2+\|D^{r+1}U_1\|_2\le R,
\]
而不能再写成 branch 2 加差分。例如把
\[
D^{r+1}\beta_1=D^{r+1}\beta_2+D^{r+1}\omega
\]
会制造无权 \(D^{r+1}\omega\)，继而在分部积分后制造无权 \(D^{r+1}Z\)，只能靠 \(\varepsilon\)-耗散并引入 \(\varepsilon^{-1}\)。两阶余量正是为直接控制这些完整分支高阶项而存在。

---

# 5. 输运差分及 (4.14)–(4.16)

令 \(b_i=\beta_i^2W(V_i)\)。则
\[
\omega_t=b_1\cdot D\omega+(b_1-b_2)\cdot D\beta_2,
\]
\[
b_1-b_2
=(\beta_1^2-\beta_2^2)W(V_1)
+\beta_2^2\bigl(W(V_1)-W(V_2)\bigr).
\]
并且
\[
W(V_1)-W(V_2)
=\mathsf C^aD_aZ+\mathsf C_0Z.
\]

对流项中的 \(D^{r+1}\omega\) 经分部积分消失。唯一顶阶输出度量项为
\[
I_T
=\int D^r\omega\,
\beta_2^2\mathsf C\,D^{r+1}Z\,D\beta_2,
\]
因而
\[
|I_T|
\le C_R\|\beta_2D^{r+1}Z\|_2\|\omega\|_{H^r}
\le
\eta\|\beta_2D^{r+1}Z\|_2^2
+C_{\eta,R}\|\omega\|_{H^r}^2.
\]

故 (4.14)–(4.16) 的顶阶机制正确。多个交叉项同时借用同一耗散时，只需分别选取足够小的 Young 参数，使总吸收量小于主部椭圆常数。

---

# 6. 经修正的差分结论

在上述 Lie 分解和“完整分支高阶因子不再拆分”的规则下，
\[
\boxed{
\begin{aligned}
\frac d{dt}\bigl(\|Z\|_{H^r}^2+A\|\omega\|_{H^r}^2\bigr)
&+c\sum_{k\le r}\int(\beta_2^2+\varepsilon)|D^{k+1}Z|^2\\
&\le C_R\bigl(
\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2+\|H\|_{H^r}^2
\bigr).
\end{aligned}}
\]

精确危险项清单如下：

- \(D^{r+1}H\)：只来自 \(Q\) 和 Lie-input，分别带 \(\beta_2^2\) 与 \(\beta_2D\beta_2\)；
- \(D^{r+1}\omega\)：只来自 Lie-cutoff 和输运对流；前者转移到 \(\beta_2D^{r+1}Z\)，后者由输运分部积分消失；
- \(D^{r+1}Z\)：主部提供耗散；输运顶项带 \(\beta_2^2\)；
- 主系数差分只需 \(H^r\) 的 \(H,\omega\)，因为 \(D^2V_1\in H^r\)；
- 所有 \(\varepsilon\) 项都以正耗散或有界系数出现，没有除以 \(\varepsilon\)。

因此有限阶 (4.17) 是可信的 \(\varepsilon\)-一致先验估计。

---

# 7. 构造与 \(\varepsilon\to0\)：精确状态

## 7.1 固定 \(\varepsilon\)

对每个 \(\varepsilon>0\)，\(V\)-方程严格抛物，\(\beta\)-方程是速度依赖 \(DV\) 的拟线性输运方程。Galerkin/Friedrichs 构造应可行，但不能只引用独立的“抛物方程 + 输运方程”理论，因为两者双向耦合。

需要在逼近层证明联合能量，并取得足够强的紧性，例如
\[
V_N\to V \quad\text{于 }C_tH^{s-1},
\qquad
\beta_N\to\beta \quad\text{于 }C_tH^{s-1},
\]
以通过
\[
\beta_N^2W(V_N)\cdot D\beta_N.
\]
这是标准但尚未写出的实质步骤。

## 7.2 \(\varepsilon\to0\)

单个有限 \(H^s\) 估计最多给出有限正则度极限；它不推出跨越 \(\{\beta=0\}\) 的 \(C^\infty\) 光滑性。真正缺少的是共同时间区间上、所有 \(m\ge s\) 的一致 tame hierarchy：
\[
\boxed{
\frac d{dt}E_m+cD_m
\le C(E_s)E_m+C_m(E_{m-1}),}
\]
其中
\[
E_m=\|V_\varepsilon\|_{H^m}^2+\|\beta_\varepsilon\|_{H^m}^2,
\]
\[
D_m=\sum_{k\le m}\int(\beta_\varepsilon^2+\varepsilon)
|D^{k+1}V_\varepsilon|^2,
\]
且所有常数均与 \(\varepsilon\) 无关。还需相应时间导数界
\[
\|\partial_tV_\varepsilon\|_{H^{m-2}}
+\|\partial_t\beta_\varepsilon\|_{H^{m-1}}
\le C_m.
\]

若这些估计成立，则可对每个 \(m\) 作 Rellich–对角紧化，并有
\[
\varepsilon U^{-1}D^2V_\varepsilon\to0
\]
于任意固定低阶 Sobolev 空间。此时方程中没有除以 \(\beta\) 的项，零集本身不会产生代数奇性。

但 Xu 的最终“\(\chi>0\) 区域抛物正则性，加上 \(\chi=0\) 区域解固定”不能直接移植，因为这里 \(\beta\) 也是未知量。虽然
\[
\beta_t=\beta^2W(V)\cdot D\beta
\]
暗示零集上的速度消失，且 \(\beta=0\) 处所有 \(\beta^2\) 项及 \(\beta D\beta\) Lie 项消失，但仍需证明：

1. \(\beta_\varepsilon\) 在退化界面附近全阶一致光滑；
2. 内部抛物解与外部静止解 \(V=g_0\) 在界面处全阶匹配。

因此，**“标准 Galerkin/抛物—输运构造 + 当前有限阶账本”不足以证明光滑过零集**。可闭合问题的精确缺失对象，就是上述全阶 \(\varepsilon\)-一致 tame hierarchy，或一个等价的退化界面全阶拼接定理。

---

# 8. 几何回拉核对

若
\[
\partial_t\varphi=-\beta^2W(G)\circ\varphi,
\]
则
\[
\frac d{dt}(\beta\circ\varphi)
=(\beta_t-\beta^2W(G)\cdot D\beta)\circ\varphi=0,
\]
故
\[
\beta\circ\varphi=\chi.
\]
这部分符号一致。回拉后 DeTurck Lie 项消除，得到固定 cutoff 的几何方程；若保留 \(-2\beta^2G\)，回拉方程相应包含 \(-2\chi^2g\) 的归一化项。后续使用时应明确目标到底是未归一化 local Ricci flow 还是这一归一化版本。

---

## 最终状态

- 精确冻结系统：已核对，与 Xu 的固定背景展开一致。
- 单解 \(H^s\) 估计：成立且 \(\varepsilon\)-一致。
- \(H^{s-2}\) 差分估计：经 Lie 差分表述修正后成立且 \(\varepsilon\)-一致。
- Step 54 (4.11)：若采用两项分解，应将 \(\mathcal W(U_2)\) 改为 \(\mathcal W(U_1)\)；若保留 \(\mathcal W(U_2)\)，则必须显式保留额外交叉项。
- 未出现不可控无权 \(D^{r+1}H,D^{r+1}\omega,D^{r+1}Z\)，也未出现 \(\varepsilon^{-1}\) 常数。
- 固定 \(\varepsilon\) 耦合解：合理但尚未完成构造证明。
- \(\varepsilon\to0\) 光滑过零集：尚未证明；精确缺口是共同时间上的全阶 \(\varepsilon\)-一致 tame hierarchy，或等价的 transported-cutoff 退化界面正则性定理。