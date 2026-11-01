# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step92_wahl_field_limit_proof_blueprint.md",
    "Sessions/S1003A01/workspace/notes/step92_global_route_selection_wahl_field_cap_charge_and_goldberg.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step102_wahl_orbifold_realization_and_K2_invariance.md"
  ]
}
```

## Task

Check the proposed fixed supplied Seiberg–Witten field limit blueprint line by line. Focus on the normalization and validity of equations (2.1)–(2.5), the localized cutoff inequality (3.1)–(3.2), the logarithmic W^{1,4} capacity calculation, and whether these facts really imply the full tightness statement (3.7) rather than only no mass in the innermost core. Inspect the actual Lemma 86.S scale and gluing control quoted in the blueprint. Also check the claimed lower bound ∫|Phi|^4 >=32π²A, the use of one fixed class selected from a finite sign family, and the Einstein Hodge identities (5.1)–(5.3). Identify any hidden sign, factor, regularity, chamber, perturbation, or annular-tail issue. Give exact repairs and a rigorous proof skeleton that the next Execute step can follow. Do not assume the orbifold removability or marked character result; state precisely what remains there.

## Output

# 科学核验备忘录：Wahl 填充收缩下的固定 Seiberg–Witten 场

## 1. 几何尺度与标量曲率控制

对 \(\tau=4\)，Lemma 86.S 的平衡尺度确为
\[
\rho=\varepsilon^{4/(4+2)}=\varepsilon^{2/3},
\qquad
(\varepsilon/\rho)^4=\varepsilon^{4/3}=\rho^2.
\]
因此过渡区的尺度化 \(C^2\) 偏差满足
\[
\delta_\varepsilon
=O\!\left(\rho^2+(\varepsilon/\rho)^4\right)
=O(\rho^2).
\]
Ricci 曲率包含两个导数，故
\[
|\operatorname{Ric}(g_\varepsilon)|
\le C\rho^{-2}\delta_\varepsilon\le C
\]
在过渡区一致成立；填充内部 Ricci-flat，外部等于固定 orbifold 度量。于是这个显式族实际上满足更强的点态估计
\[
\sup_\varepsilon\|s_{g_\varepsilon}^-\|_{L^\infty}<\infty. \tag{1.3'}
\]
变化区体积为 \(O(\rho^4)=O(\varepsilon^{8/3})\)，从而
\[
\int_{\{r<2\rho\}}(s_\varepsilon^-)^2=O(\rho^4).
\]
对于固定 \(R\) 和充分小的 \(\varepsilon\)，
\[
\int_{\{r<R\}}(s_\varepsilon^-)^2
\le
\int_{\{2\rho<r<R\}}(s_g^-)^2+C\rho^4.
\]
固定 orbifold 度量在 uniformizer 上光滑，故右端先令 \(\varepsilon\to0\)、再令 \(R\to0\) 即趋于零。这严格给出 (1.2)。

若把对数截止的内半径取成 \(r_\varepsilon=2\rho\)，则其导数完全位于 \(g_\varepsilon=g\) 的区域；这样无需在临界 \(L^4\) 计算中使用过渡区的精细 \(C^2\) 比较。若取 \(r_\varepsilon\asymp\rho\) 穿过过渡区，Lemma 86.S 仍给出一致双 Lipschitz 比较，足够控制该积分。

---

## 2. 固定 supplied spin\(^c\) 结构与全局恒等式

### 2.1 固定结构的量词

正确表述是：对任意给定序列 \(\varepsilon_j\downarrow0\)，每个 \(g_{\varepsilon_j}\) 从一个**有限的实际供给 spin\(^c\) 结构族**中选取一个携带无扰动解且满足
\[
(a_{j,g_{\varepsilon_j}}^+)^2\ge A
\]
的结构；有限性给出一个子列，使整个 spin\(^c\) 结构固定，而不只是其 determinant class 固定。

对 blow-up 符号族 \(a_\sigma=c+\sum_i\sigma_iE_i\)，投影平均为
\[
2^{-k}\sum_\sigma (a_\sigma^+)^2
=(c^+)^2+\sum_i(E_i^+)^2\ge c^2=A.
\]
因此若所用供应定理保证这些符号类在相应度量上确实给出实际无扰动解，就能选到所需结构。

这里有两个必要假设：

* 若 \(b^+=1\)，必须有与 \(g_\varepsilon\) 相容的 chamber 供应；“SW basic”本身不自动给出每个度量上的无扰动解。
* 方程必须是无扰动方程。若
  \[
  F_A^+=q(\Phi)+i\eta,
  \]
  则 \(|F_A^+|^2=|\Phi|^4/8\)、(2.1) 以及后续下界都会出现额外项。

### 2.2 (2.1)–(2.5) 的系数

令 \(U=|\Phi|^2\)，并采用
\[
|F_A^+|^2=|q(\Phi)|^2=\frac{U^2}{8}.
\]
点态 Weitzenböck 方程是
\[
4\nabla_A^*\nabla_A\Phi+s\Phi+U\Phi=0.
\]
在闭流形上积分得到
\[
4\int|\nabla_A\Phi|^2+\int sU+\int U^2=0, \tag{2.1}
\]
系数正确。于是
\[
\int U^2\le\int s^-U
\le\|s^-\|_2\|U\|_2,
\]
故
\[
\|U\|_2\le\|s^-\|_2, \tag{2.2}
\]
并且
\[
4\int|\nabla_A\Phi|^2
=-\int sU-\int U^2
\le\|s^-\|_2\|U\|_2. \tag{2.3}
\]

采用
\[
a=\left[\frac{iF_A}{2\pi}\right],
\]
调和投影给出
\[
\int|F_A^+|^2\ge4\pi^2(a_g^+)^2.
\]
因此
\[
\boxed{\int|\Phi|^4=\int U^2
=8\int|F_A^+|^2
\ge32\pi^2(a_g^+)^2
\ge32\pi^2A.} \tag{2.4}
\]
这个 \(32\pi^2\) 系数正确。

同一规范下，
\[
4\pi^2a^2
=\int|F_A^+|^2-\int|F_A^-|^2,
\]
故
\[
\int|F_A^-|^2
=\int|F_A^+|^2-4\pi^2a^2. \tag{2.5}
\]
所以固定类以后，\(\|F_A\|_2\)、\(\|\Phi\|_4\) 和
\(\|\nabla_A\Phi\|_2\) 一致有界。

---

## 3. 局部化 Weitzenböck 估计

对实值 \(\eta\in W^{1,4}\cap L^\infty\)，直接配方可得精确恒等式
\[
4\int|\nabla_A(\eta\Phi)|^2
+\int\eta^2sU+\int\eta^2U^2
=
4\int|d\eta|^2U. \tag{3.A}
\]
因此
\[
\boxed{
\int\eta^2U^2
\le
\int\eta^2s^-U
+4\int|d\eta|^2U.} \tag{3.B}
\]
再用 Hölder，
\[
\int\eta^2U^2
\le
\|s^-\|_{L^2(\operatorname{supp}\eta)}\|U\|_2
+4\|d\eta\|_4^2\|U\|_2. \tag{3.C}
\]
所以 (3.1)–(3.2) 正确；常数可取第一项为 \(1\)、第二项为 \(4\)。

不必实际光滑化对数截止：因为 \(\Phi\in L^4\)，
\(d\eta\in L^4\)，故 \(d\eta\,\Phi\in L^2\)，分段 Lipschitz 截止已经能代入弱恒等式。若采用光滑近似，在对数坐标中以固定宽度平滑两个拐角即可保持同一阶估计。

---

## 4. 临界 \(W^{1,4}\) 容量

在圆锥
\[
dr^2+r^2g_{S^3/\Gamma}
\]
上，令 \(L=\log(R/r_\varepsilon)\)。对
\[
\eta(r)=\frac{\log(R/r)}{L},
\qquad r_\varepsilon<r<R,
\]
有
\[
|d\eta|=\frac1{rL}.
\]
因此
\[
\int|d\eta|^4
=
\frac{\operatorname{Vol}(S^3/\Gamma)}{L^4}
\int_{r_\varepsilon}^{R}\frac{dr}{r}
=
\frac{2\pi^2/|\Gamma|}{L^3}. \tag{4.1}
\]
对 Wahl 群，\(|\Gamma|=n^2\)。由此
\[
\|d\eta\|_4^2
=
\left(\int|d\eta|^4\right)^{1/2}
=O(L^{-3/2}). \tag{4.2}
\]
蓝图中的指数与系数正确。

---

## 5. 原有截止只控制最内核，不直接给出 (3.7)

蓝图的 \(\eta_\varepsilon\) 等于 \(1\) 仅在 \(r\le r_\varepsilon\)。由 (3.C) 可严格推出
\[
\lim_{R\downarrow0}\limsup_{\varepsilon\downarrow0}
\int_{\{r<r_\varepsilon\}}U_\varepsilon^2=0.
\]
但这并不自动控制 \(r_\varepsilon<r<R\)：在靠近外端 \(r=R\) 的对数薄层上，\(\eta_\varepsilon\) 可以任意小，而未加权的 \(U_\varepsilon^2\) 仍可能携带固定质量。“互补截止”若直接取 \(1-\eta_\varepsilon\)，其标量曲率项遍及流形，不能趋于零。因此蓝图中从 (3.6) 到 (3.7) 的那一句尚缺推导。

这里有两种完整修复。

### 5.1 对当前显式族，最大值原理直接给出全紧性

由点态方程，
\[
2\Delta U+4|\nabla_A\Phi|^2+sU+U^2=0
\]
（\(\Delta=d^*d\)）。在 \(U\) 的最大点，
\[
U\le \|s^-\|_\infty.
\]
结合 (1.3')，
\[
\sup_\varepsilon\|U_\varepsilon\|_\infty\le C.
\]
而 Lemma 86.S 的体积比较给出
\[
\operatorname{Vol}_{g_\varepsilon}\{r<R\}\le CR^4
\]
对充分小的 \(\varepsilon\) 一致成立。因此
\[
\boxed{
\limsup_{\varepsilon\downarrow0}
\int_{\{r<R\}}|\Phi_\varepsilon|^4
=
\limsup_{\varepsilon\downarrow0}
\int_{\{r<R\}}U_\varepsilon^2
\le CR^4,}
\]
随 \(R\downarrow0\) 趋于零。这比 (3.7) 更强，也完全覆盖过渡环和填充核心。

### 5.2 仅依赖局部 \(L^2\) 标量控制时的外向对数截止

取固定 chart 半径 \(r_*\)，令
\[
R_0=\sqrt{Rr_*},\qquad
L_R=\log(R_0/R)=\frac12\log(r_*/R),
\]
并定义
\[
\zeta_R=
\begin{cases}
1,&r\le R,\\
\log(R_0/r)/L_R,&R<r<R_0,\\
0,&r\ge R_0.
\end{cases}
\]
对固定 \(R\)，当 \(\varepsilon\) 足够小时有 \(2\rho<R\)，故
\(d\zeta_R\) 完全位于 \(g_\varepsilon=g\) 的 orbifold 区。于是
\[
\int|d\zeta_R|^4\le C L_R^{-3}.
\]
由 (3.C)，若 \(C_U=\sup_\varepsilon\|U_\varepsilon\|_2\)，则
\[
\limsup_{\varepsilon\to0}\int_{\{r<R\}}U_\varepsilon^2
\le
C_U
\left(
\limsup_{\varepsilon\to0}
\int_{\{r<R_0\}}(s_\varepsilon^-)^2
\right)^{1/2}
+
C C_U L_R^{-3/2}.
\]
这里 \(R_0\to0\) 且 \(L_R\to\infty\)，结合 (1.2) 即得完整的 (3.7)。

---

## 6. 正则部分极限与非零性

在任意 \(K\Subset V^{\mathrm{reg}}\) 上，度量一致光滑，固定 determinant bundle 上的阿贝尔 Coulomb gauge 与标准 SW 紧致性给出子列光滑收敛
\[
(A_{\varepsilon_j},\Phi_{\varepsilon_j})
\longrightarrow
(A_\infty,\Phi_\infty).
\]
全紧性意味着没有 \(L^4\) spinor 质量落入 Wahl 点。因而
\[
\int_{V^{\mathrm{reg}}}|\Phi_\infty|^4
=
\lim_{j\to\infty}\int_M|\Phi_{\varepsilon_j}|^4
\ge32\pi^2A. \tag{6.1}
\]
所以 \(\Phi_\infty\not\equiv0\)。

这一步只排除了 spinor 质量集中；它没有排除 \(F_A^-\) 的曲率能量集中。后者与点处延拓及 link holonomy 的识别仍需单独处理。

---

## 7. Einstein 情形的恒等式

以下均以完成 orbifold 延拓为前提，或等价地已有足够正则性使点处不产生 link 项。

### 7.1 (5.1)

明确令
\[
s=-\lambda,\qquad \lambda>0,
\]
其中 \(\lambda\) 是标量曲率绝对值，不是 \(\operatorname{Ric}=cg\) 中的 \(c\)。最大值原理给出
\[
0\le U\le\lambda,
\]
而 (2.1) 变成
\[
\boxed{
4\int|\nabla_A\Phi|^2
=\int U(\lambda-U).} \tag{7.1}
\]
系数正确。

### 7.2 (5.2)

令 \(\mathcal F=iF_A\)，并取
\[
\mathcal F=2\pi h_a+d\alpha,
\]
其中 \(h_a\) 是代表实 determinant class 的 orbifold 调和二形式。调和项与精确项正交。又因
\[
\int d\alpha\wedge d\alpha=0,
\]
有
\[
\|(d\alpha)^+\|_2^2
=
\|(d\alpha)^-\|_2^2
=
\frac12\|d\alpha\|_2^2.
\]
因此
\[
\boxed{
\frac18\int U^2-4\pi^2\|h_a^+\|_2^2
=
\int|F_A^-|^2-4\pi^2\|h_a^-\|_2^2
=
\frac12\|d\alpha\|_2^2.} \tag{7.2}
\]
蓝图中的因子正确；最好把 \(\|a_g^\pm\|^2\) 明确定义为
\(\|h_a^\pm\|_2^2\)。

### 7.3 (5.3)

对任意实自对偶二形式 \(\psi\)，Hodge–Weitzenböck 公式为
\[
\|d\psi\|_2^2+\|d^*\psi\|_2^2
=
\|\nabla\psi\|_2^2+\frac{s}{3}\|\psi\|_2^2
-2\int\langle W^+\psi,\psi\rangle.
\]
故
\[
\boxed{
2\int\langle W^+\psi,\psi\rangle
=
\int|\nabla\psi|^2+\frac{s}{3}\int|\psi|^2
-\int(|d\psi|^2+|d^*\psi|^2).} \tag{7.3}
\]
取 \(\psi=iF_A^+\) 即为 (5.3)。

需要修正的是术语：\(F_A^+\) 一般并不闭合。由 \(dF_A=0\) 不能推出
\(dF_A^+=0\)。对自对偶 \(\psi\)，仅有
\[
d^*\psi=-*d\psi,\qquad \|d^*\psi\|_2=\|d\psi\|_2.
\]
Einstein 条件给出的 \(\delta W^+=0\) 也没有参与 (7.3) 的推导；它是后续耦合恒等式的额外输入。

---

## 8. Wahl 点处仍待建立的解析与拓扑内容

现有估计产生的是 punctured uniformizer 上的有限能量解：
\[
F_{A_\infty}\in L^2,\qquad
\Phi_\infty\in L^4,\qquad
\nabla_{A_\infty}\Phi_\infty\in L^2.
\]
这尚未自行给出所需 orbifold 延拓。完整论证还包含：

1. 在 \(B^4\setminus\{0\}\) 上构造临界 Sobolev Coulomb gauge，使连接一形式具有足以弱延拓的 \(W^{1,2}\) 控制。
2. 证明弱延拓后的方程没有点质量，并由椭圆正则性提升为光滑解。
3. 保持 \(\Gamma\)-等变性；规范变换后出现的 \(\Gamma\)-cocycle 必须化为一个固定表示，而不能直接消去。
4. 区分 spin\(^c\) lift、determinant 表示和 line twist。line twist 作用到 determinant character 时有乘二。
5. 将这个表示与固定 smooth spin\(^c\) 结构在
   \(L(n^2,n-1)\) 上的标记限制相比较。

Feehan–Leness 的光滑穿点结果可提供分析模板，但不能替代上述阿贝尔、等变和标记版本。有限 \(L^2\) 曲率本身也不识别具体 isotropy character。

---

## 9. 可直接采用的证明骨架

严密版本可按以下逻辑组织：

1. 任取 \(\varepsilon_j\downarrow0\)，由有限实际供应族选子列，使 smooth spin\(^c\) 结构固定，并保留 \((a_{g_{\varepsilon_j}}^+)^2\ge A\)。
2. 用 (2.1)–(2.5) 得到全局 \(F\)、\(\Phi\)、\(\nabla_A\Phi\) 能量控制及
   \(\int|\Phi|^4\ge32\pi^2A\)。
3. 用 Lemma 86.S 的一致标量点态下界与最大值原理得到
   \(\|U_\varepsilon\|_\infty\le C\)。
4. 用 \(\operatorname{Vol}\{r<R\}\le CR^4\) 直接证明完整的 (3.7)；外向对数截止作为只使用局部 \(L^2\) 标量控制的替代推导。
5. 在 \(V^{\mathrm{reg}}\) 上作局部 Coulomb gauge 并光滑收敛；全紧性和 (2.4) 给出非零极限。
6. 点处等变延拓与标记 character 识别作为独立定理证明；在此之前不把极限称为全局 orbifold monopole。
7. 完成延拓后，(5.1)–(5.3) 与 \(\delta W^+=0\) 成为同一 Einstein 度量上的精确场恒等式。

核心修正是：原对数截止计算本身正确，但原来的内向截止只控制 \(r<r_\varepsilon\)；完整紧性应由当前显式族上的最大值原理，或由“内平坦、向外对数衰减”的新截止来完成。