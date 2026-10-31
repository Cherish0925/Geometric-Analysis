# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/paired_cross_field_algebra.py",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Knowledge/objects/papers/Algebraic-surfaces-and-Seiberg-Witten-invariants--d573804ced34--70869ee25818/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Check the mathematical correctness and normalization of the proposed paired-monopole identities and the Kähler lower theorem in the session. In particular: (i) for a Kähler metric on M=X#k CPbar^2 with X minimal general type, derive explicitly whether C_+=(2pi^2)^-1∫|W+|^2+(96pi^2)^-1∫s^2 equals ∫s^2/(32pi^2), and prove or correct C_+>=A=c1^2(X) using the Hodge index with canonical class and exceptional areas; determine what additional assumptions are needed for inf_Kähler P=8pi^2 k and nonattainment; (ii) verify the cross-line bundle classes for u=<Phi_e',Phi_e> and w=Phi_e wedge Phi_e' when the determinant classes differ by flipping exceptional signs, including factor-of-two conventions and whether c1(u)=E_i or 2E_i; (iii) verify the amplitude identity and lower inequality P>=8pi^2 Q-4 E∫(2-rho)_+ under the stated s=-4 normalization. Give exact corrected statements, not procedural advice.

## Output

# 数学核验备忘录

以下采用文件中的曲率范数约定：\(W^\pm\) 是 \(\Lambda^\pm\) 上曲率算子的 Hilbert–Schmidt 范数，\(\Ric^\circ\) 是二阶张量范数；Seiberg–Witten 二次映射满足
\[
|\sigma(\Phi)|^2=\frac{|\Phi|^4}{8}.
\]

## 1. Kähler 情形的 \(C_+\) 与 \(P\) 下界

令
\[
S(g)=\int_M s_g^2\,d\mu_g,\qquad
C_+(g)=\frac1{2\pi^2}\int_M|W_g^+|^2\,d\mu_g
+\frac1{96\pi^2}S(g).
\]

### 1.1 \(C_+=S/(32\pi^2)\) 的系数正确

Kähler 曲面上 \(W^+:\Lambda^+\to\Lambda^+\) 的三个特征值为
\[
\frac{s}{6},\qquad -\frac{s}{12},\qquad -\frac{s}{12}.
\]
因此在本文采用的算子范数下
\[
|W^+|^2=\frac{s^2}{36}+2\frac{s^2}{144}=\frac{s^2}{24}.
\]
所以
\[
\boxed{
C_+(g)=
\frac{1}{48\pi^2}S(g)+\frac{1}{96\pi^2}S(g)
=\frac{S(g)}{32\pi^2}.
}
\]

这与 LeBrun 文献中 \(|W^+|^2=s^2/24\) 的归一化一致。

---

### 1.2 固定 blow-up complex structure 上的 Hodge 指数证明

设 \(X\) 是 minimal general type complex surface，
\[
A=K_X^2=c_1^2(X)>0,
\]
并令
\[
\pi:M=\operatorname{Bl}_{p_1,\dots,p_k}X\longrightarrow X
\]
是不同点处的复 blow-up。记
\[
K_0=\pi^*K_X,\qquad
K_M=K_0+\sum_{i=1}^kE_i,
\]
其中
\[
K_0^2=A,\qquad K_0\cdot E_i=0,\qquad E_i\cdot E_j=-\delta_{ij}.
\]

对任意与此 complex structure 相容的 Kähler 度量，令
\[
\Omega=[\omega],\qquad e_i=\Omega\cdot E_i>0,
\qquad
\Omega_0=\Omega+\sum_i e_iE_i.
\]
于是
\[
\Omega=\Omega_0-\sum_i e_iE_i,\qquad
\Omega_0\cdot E_i=0,
\]
并且
\[
\Omega_0^2=\Omega^2+\sum_i e_i^2.
\]
此外
\[
K_M\cdot\Omega
=K_0\cdot\Omega_0+\sum_i e_i.
\]

由于 \(K_X\) nef 且 big，\(K_0\cdot\Omega_0>0\)。在实 \((1,1)\)-上同调上使用 Hodge 指数定理，
\[
(K_0\cdot\Omega_0)^2
\ge K_0^2\Omega_0^2
=A\left(\Omega^2+\sum_i e_i^2\right).
\]
因此
\[
K_M\cdot\Omega
\ge
\sqrt{A\left(\Omega^2+\sum_i e_i^2\right)}
+\sum_i e_i.
\]

另一方面，
\[
\int_Ms\,d\mu
=4\pi c_1(M)\cdot\Omega
=-4\pi K_M\cdot\Omega,
\qquad
\operatorname{Vol}(M,g)=\frac{\Omega^2}{2}.
\]
Cauchy–Schwarz 给出
\[
S(g)\ge
\frac{\left(\int s\,d\mu\right)^2}{\operatorname{Vol}}
=
32\pi^2\frac{(K_M\cdot\Omega)^2}{\Omega^2}.
\]
结合前式得到精确的强化形式
\[
\boxed{
C_+(g)\ge
\frac{(K_M\cdot\Omega)^2}{\Omega^2}
\ge
\frac{
\left[
\sqrt{A\left(\Omega^2+\sum_i e_i^2\right)}
+\sum_i e_i
\right]^2
}{\Omega^2}
\ge A.
}
\]
若 \(k>0\)，则所有 \(e_i>0\)，故实际上
\[
\boxed{C_+(g)>A.}
\]

这也显示：若某 Kähler 序列满足 \(C_+(g_j)\to A\)，则在固定总体积归一化后必须有
\[
e_{i,j}\to0,
\]
且 \((\Omega_0)_j\) 渐近于 \(K_0\) 的正倍数；同时标量曲率在 \(L^2\) 意义下渐近常数。

---

### 1.3 与 \(P=\int|\Ric^\circ|^2\) 的关系

四维 Chern–Weil 公式给出
\[
\frac{P(g)}{8\pi^2}
=
C_+(g)-(2\chi+3\tau)(M).
\]
对于 \(M=X\#k\overline{\mathbb{CP}}^{\,2}\)，
\[
(2\chi+3\tau)(M)=A-k.
\]
故
\[
\boxed{
P(g)=8\pi^2\bigl(C_+(g)-A+k\bigr).
}
\]
由上面的 Kähler 下界，
\[
\boxed{
P(g)\ge8\pi^2k,
}
\]
而且固定 blow-up complex structure 下，若 \(k>0\)，
\[
\boxed{
P(g)>8\pi^2k
\quad\text{对每个光滑 Kähler 度量成立。}
}
\]

---

### 1.4 何时可写 \(\inf_{\mathrm{K\ddot ahler}}P=8\pi^2k\)

下界本身只给出
\[
\inf_{g\ {\rm K\ddot ahler}}P(g)\ge8\pi^2k.
\]
精确等号等价于存在固定 complex structure 上的 Kähler recovery sequence：
\[
\boxed{
\inf_{g\ {\rm K\ddot ahler}}P(g)=8\pi^2k
\iff
\inf_{g\ {\rm K\ddot ahler}}C_+(g)=A
\iff
\inf_{g\ {\rm K\ddot ahler}}S(g)=32\pi^2A.
}
\]

所给 `variational_selection_and_global_cost.tex` 中的 recovery metrics 只被陈述为光滑 Riemannian metrics；该段没有陈述它们与固定 blow-up complex structure 相容。因此该 recovery 不能单独推出 Kähler 下确界的等号。

一个干净的充分假设包是：

1. \(K_X\) ample，因而 \(X\) 有 \(\Ric=-\lambda g\)、\(\lambda>0\) 的 Kähler–Einstein 度量；
2. 在给定 blow-up 点上使用小 exceptional sizes 的 cscK blow-up existence theorem。

此时存在 cscK 度量，其 Kähler 类形如
\[
\Omega_\varepsilon
=tK_0-\varepsilon^2\sum_i\lambda_iE_i,
\qquad t,\lambda_i>0.
\]
由于标量曲率为常数，
\[
C_+(g_\varepsilon)
=
\frac{(K_M\cdot\Omega_\varepsilon)^2}
{\Omega_\varepsilon^2}
=
\frac{
\left(tA+\varepsilon^2\sum_i\lambda_i\right)^2
}{
t^2A-\varepsilon^4\sum_i\lambda_i^2
}
\longrightarrow A.
\]
于是
\[
\inf_{\mathrm{K\ddot ahler}}P=8\pi^2k.
\]

若 \(k>0\)，前面的严格不等式说明此下确界不被任何光滑 Kähler 度量取到。

若 \(k=0\)，则 \(P=0\) 被取到当且仅当 \(X\) 有 \(\Ric=-\lambda g\) 的 Kähler–Einstein 度量。事实上，\(C_+=A\) 强迫：

- \(s\) 为常数；
- \([\omega]\) 是 \(K_X\) 的正倍数；
- Ricci form 与 \(\omega\) 成比例，从而度量是 Kähler–Einstein。

若 \(K_X\) 非 ample，而另有 Kähler recovery sequence 使 \(P\to0\)，则该下确界不被取到。

若“所有 Kähler metrics”还允许改变同一光滑 \(M\) 上的 complex structure，则还需识别每个 complex structure 的 minimal model、canonical class 与 holomorphic exceptional classes。所给 Friedman–Morgan 文献在其 stated hypotheses 下提供了这种 canonical/exceptional class 的识别；仅由光滑分解式本身不能直接把固定的 \(E_i\) 当作每个 complex structure 的有效 exceptional curves。

---

## 2. Cross-line bundles：因子 \(2\) 的精确位置

设
\[
a_\epsilon=c+\sum_{i=1}^k\epsilon_iE_i
\]
是 determinant line \(L_\epsilon\) 的第一 Chern 类，并令
\[
\Phi_\epsilon\in\Gamma(S^+_\epsilon),\qquad
\det S^+_\epsilon=L_\epsilon.
\]

固定两组符号 \(\epsilon,\epsilon'\)。选择相对 twisting line
\[
N_{\epsilon'\epsilon}
\]
使得
\[
S^+_{\epsilon'}\cong S^+_\epsilon\otimes N_{\epsilon'\epsilon}.
\]
Spin\(^c\) twisting 的 determinant 是平方，因此
\[
L_{\epsilon'}\cong
L_\epsilon\otimes N_{\epsilon'\epsilon}^{\,2},
\]
从而
\[
\boxed{
c_1(N_{\epsilon'\epsilon})
=\frac{a_{\epsilon'}-a_\epsilon}{2}.
}
\]

这正是 determinant classes 的差出现因子 \(2\)、而 cross-line class 只取其一半的原因。

### 2.1 \(u=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle\)

采用脚本中的 Hermitian 约定，即内积对第一变量共轭线性，则
\[
u_{\epsilon\epsilon'}
=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle
\in\Gamma(N_{\epsilon'\epsilon}^{\,*}).
\]
因此
\[
\boxed{
c_1(u_{\epsilon\epsilon'})
=
\frac{a_\epsilon-a_{\epsilon'}}{2}
=
\sum_i\frac{\epsilon_i-\epsilon_i'}{2}E_i.
}
\]

若仅第 \(i\) 个符号翻转，则
\[
c_1(u_{\epsilon\epsilon'})=\epsilon_iE_i.
\]
特别地，若 \(\epsilon_i=+1,\epsilon_i'=-1\)，则
\[
\boxed{c_1(u)=E_i,\quad\text{不是 }2E_i.}
\]

若改用对第一变量线性的 Hermitian 约定，符号反转，但绝对的因子仍是一半而不是全部 determinant difference。

### 2.2 \(w=\Phi_\epsilon\wedge\Phi_{\epsilon'}\)

利用
\[
S^+_{\epsilon'}=S^+_\epsilon\otimes N_{\epsilon'\epsilon},
\]
外积是
\[
w_{\epsilon\epsilon'}
\in
\Gamma\!\left(
\det S^+_\epsilon\otimes N_{\epsilon'\epsilon}
\right).
\]
故
\[
\boxed{
c_1(w_{\epsilon\epsilon'})
=
a_\epsilon+\frac{a_{\epsilon'}-a_\epsilon}{2}
=
\frac{a_\epsilon+a_{\epsilon'}}2.
}
\]
若只翻转第 \(i\) 个符号，则
\[
c_1(w)
=
c+\sum_{j\ne i}\epsilon_jE_j;
\]
该 exceptional component 被消去。

若全部 exceptional signs 同时翻转，则 \(c_1(w)=c\)。即使 \(c\) 在 blow-up 上不是 characteristic class，它仍可是一条普通复线丛的第一 Chern 类；它只不能自动充当 Spin\(^c\) determinant class。

若只知道 determinant Chern classes，而未固定相对 Spin\(^c\) twisting，则 \(2\)-torsion 数据也需一并固定。这里的 blow-up sign family 由 exceptional line bundles 的自然 twisting 给出，因而上述等式是积分上同调中的等式。

### 2.3 相对连接的曲率

若 \(B\) 是 \(N_{\epsilon'\epsilon}\) 上的连接，则
\[
A_{\epsilon'}=A_\epsilon+2B.
\]
写 \(f_\epsilon=-iF_{A_\epsilon}\)，则 \(u\) 与 \(w\) 的诱导实曲率分别为
\[
\boxed{
f_u=\frac{f_\epsilon-f_{\epsilon'}}2,
\qquad
f_w=\frac{f_\epsilon+f_{\epsilon'}}2.
}
\]
直接使用 \(f_\epsilon-f_{\epsilon'}\) 作为 \(u\) 的曲率会把 \(c_1(u)\) 错写成 \(2E_i\)。

---

## 3. Paired Fierz/Walsh 恒等式

在
\[
F_{A_\epsilon}^+=2i\sigma(\Phi_\epsilon)
\]
的归一化下，
\[
f_\epsilon^+=-iF_{A_\epsilon}^+
=2\sigma(\Phi_\epsilon),
\qquad
|f_\epsilon^+|^2=\frac{\rho_\epsilon^2}{2},
\qquad
\rho_\epsilon=|\Phi_\epsilon|^2.
\]
在 \(\rho_\epsilon>0\) 处定义单位 Bloch vector
\[
n_\epsilon=\frac{\sqrt2\,f_\epsilon^+}{\rho_\epsilon}.
\]

选取 \(N_{\epsilon'\epsilon}\) 的局部单位 frame 后，两 spinors 可局部写为 \(\mathbb C^2\) 向量。frame 改变只改变 \(u,w\) 的相位，不改变其范数。于是脚本中的 Fierz 公式全都成立：
\[
\boxed{
|u_{\epsilon\epsilon'}|^2
=
\rho_\epsilon\rho_{\epsilon'}
\frac{1+n_\epsilon\cdot n_{\epsilon'}}2,
}
\]
\[
\boxed{
|w_{\epsilon\epsilon'}|^2
=
\rho_\epsilon\rho_{\epsilon'}
\frac{1-n_\epsilon\cdot n_{\epsilon'}}2,
}
\]
以及
\[
|u|^2+|w|^2=\rho_\epsilon\rho_{\epsilon'}.
\]
因此
\[
\boxed{
|f_\epsilon^+-f_{\epsilon'}^+|^2
=
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
}
\]
和
\[
\boxed{
|f_\epsilon^+-f_{\epsilon'}^+|^2
=
\frac{(\rho_\epsilon+\rho_{\epsilon'})^2
-4|u_{\epsilon\epsilon'}|^2}{2}.
}
\]
这些式子在 spinor 零点处连续延拓。

对 Walsh coefficients
\[
f_I=\mathbb E_\epsilon
\left[\left(\prod_{i\in I}\epsilon_i\right)f_\epsilon\right],
\]
Parseval 恒等式给出
\[
\boxed{
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=
\mathbb E_{\epsilon,\epsilon'}
\|f_\epsilon^+-f_{\epsilon'}^+\|_2^2.
}
\]
这里 \(\epsilon,\epsilon'\) 是独立均匀符号变量。因此
\[
\boxed{
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=
\mathbb E_{\epsilon,\epsilon'}\int_M
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right]d\mu.
}
\]
无额外的 \(2^k\) 因子。

脚本中的 kinetic decomposition 也正确：
\[
\boxed{
|\nabla_{A_\epsilon}\Phi_\epsilon|^2
=
\frac{|\zeta_\epsilon|^2}{\rho_\epsilon}
+\frac{\rho_\epsilon}{4}|\nabla n_\epsilon|^2,
\qquad
\zeta_\epsilon=
\langle\Phi_\epsilon,\nabla_{A_\epsilon}\Phi_\epsilon\rangle,
}
\]
在 \(\{\rho_\epsilon>0\}\) 上成立，并可按积分意义延拓。这里 \(U(1)\) connection 从 \(n_\epsilon\) 中消去。

\(u,w\) 是 line-valued fields，而不是全局复函数；它们也不由原始 monopole equations 自动满足新的 Dirac–curvature system。Fierz 与 Walsh 公式只使用其范数，故不受此影响。

---

## 4. \(s=-4\) 下的 amplitude 恒等式

### 4.1 \(\rho\le2\) 与 \(K\) 的精确公式

Weitzenböck 公式为
\[
0=
\frac12\Delta\rho_\epsilon
+|\nabla_{A_\epsilon}\Phi_\epsilon|^2
+\frac{s}{4}\rho_\epsilon
+2\langle-iF_{A_\epsilon}^+,\sigma(\Phi_\epsilon)\rangle.
\]
由于
\[
-iF_{A_\epsilon}^+=2\sigma(\Phi_\epsilon),
\qquad
|\sigma(\Phi_\epsilon)|^2=\frac{\rho_\epsilon^2}{8},
\]
在 \(s=-4\) 时得到
\[
\boxed{
0=
\frac12\Delta\rho_\epsilon
+|\nabla_{A_\epsilon}\Phi_\epsilon|^2
-\rho_\epsilon+\frac{\rho_\epsilon^2}{2}.
}
\]
最大值原理给出
\[
\boxed{0\le\rho_\epsilon\le2.}
\]
积分后，
\[
\boxed{
K_\epsilon
=
\int_M|\nabla_{A_\epsilon}\Phi_\epsilon|^2\,d\mu
=
\frac12\int_M\rho_\epsilon(2-\rho_\epsilon)\,d\mu.
}
\]
这与脚本中的
\[
K=I_1-\frac12I_2
\]
完全一致。

令
\[
\delta_\epsilon=2-\rho_\epsilon
=(2-\rho_\epsilon)_+.
\]
则
\[
-4K_\epsilon
=-2\int\rho_\epsilon\delta_\epsilon
=
-4\int\delta_\epsilon
+2\int\delta_\epsilon^2.
\]

---

### 4.2 精确的 paired-amplitude 恒等式

由 `webvar:field-cost` 与 `webvar:positive-field-cost`，
\[
P-8\pi^2Q
=
2\|f_\varnothing^-\|_2^2
+2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
+\mathbb E_\epsilon
\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int b(\rho_\epsilon)\delta_\epsilon^2
-4K_\epsilon
\right],
\]
其中
\[
b(t)=\frac{-t^2+8t+2}{6}.
\]
在 \(0\le t\le2\) 上，
\[
b(t)\ge b(0)=\frac13.
\]

代入 \(K_\epsilon\) 公式，并使用 paired Walsh identity，得到完整的精确形式
\[
\boxed{
\begin{aligned}
&P(g)-8\pi^2Q
+4\mathbb E_\epsilon\int_M\delta_\epsilon\,d\mu\\
={}&
2\|f_\varnothing^-\|_2^2\\
&+\mathbb E_{\epsilon,\epsilon'}\int_M
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right]d\mu\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int_M\bigl(b(\rho_\epsilon)+2\bigr)
\delta_\epsilon^2\,d\mu
\right].
\end{aligned}
}
\]
也可将 pair integrand 写成
\[
\frac{(\rho_\epsilon+\rho_{\epsilon'})^2
-4|u_{\epsilon\epsilon'}|^2}{2}.
\]

右端每一项都非负，因为
\[
b(\rho)+2\ge\frac73.
\]
所以所问下界的系数完全正确：
\[
\boxed{
P(g)\ge
8\pi^2Q
-4\mathbb E_\epsilon
\int_M(2-\rho_\epsilon)_+\,d\mu.
}
\]
在当前归一化中 \(\rho_\epsilon\le2\)，故正部符号可以删去。

数字 \(2\) 和系数 \(4\) 都依赖 \(s=-4\) 以及
\[
F_A^+=2i\sigma(\Phi)
\]
这两个归一化；若改变其中任意一个，公式中的振幅阈值和系数也随之改变。

---

### 4.3 脚本中的 residual polynomial

每个 field 的 amplitude–kinetic 差还可写为
\[
4K_\epsilon-\int b(\rho_\epsilon)(2-\rho_\epsilon)^2
=
\int m(\rho_\epsilon),
\]
其中
\[
\boxed{
m(\rho)
=
2\rho(2-\rho)-b(\rho)(2-\rho)^2
=
\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6.
}
\]
此因式分解正确。但 \(m\) 在 \([0,2]\) 上具有两种符号，例如
\[
m(0)=-\frac43,\qquad m(1)=\frac12.
\]
因此不能由 \(m\) 推出
\[
4K\le\int b(\rho)(2-\rho)^2
\]
或 \(P\ge8\pi^2Q\)。可用的无条件结论正是上面的 amplitude-error inequality；其更强的精确版本是 paired-amplitude 恒等式。

## 汇总

1. Kähler 归一化
   \[
   C_+=\frac1{32\pi^2}\int s^2
   \]
   正确。

2. 对固定 blow-up complex structure，
   \[
   C_+\ge A,\qquad P\ge8\pi^2k,
   \]
   且 \(k>0\) 时两式均严格。要得到
   \[
   \inf_{\mathrm{K\ddot ahler}}P=8\pi^2k
   \]
   还需固定 complex structure 上的 Kähler recovery sequence；\(K_X\) ample 加小尺寸 cscK blow-up metrics 是一个充分包。若 \(k>0\)，该下确界不被取到。

3. 若一个 exceptional sign 从 \(+E_i\) 翻到 \(-E_i\)，determinant classes 相差 \(2E_i\)，但
   \[
   c_1\!\left(\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle\right)
   =E_i
   \]
   （按脚本的内积顺序）；不是 \(2E_i\)。

4. \(u,w\) 的正确 line classes 分别是 half-difference 与 half-sum：
   \[
   c_1(u)=\frac{a_\epsilon-a_{\epsilon'}}2,\qquad
   c_1(w)=\frac{a_\epsilon+a_{\epsilon'}}2.
   \]

5. Fierz、Walsh、kinetic split、\(K=\frac12\int\rho(2-\rho)\) 均与脚本一致。最终的精确 paired-amplitude 恒等式如上，并严格推出
   \[
   P\ge8\pi^2Q-4\mathbb E\int(2-\rho)_+.
   \]