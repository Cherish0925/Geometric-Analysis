# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step38_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step38_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the mathematical correctness and normalization of the proposed paired-monopole identities and the Kähler lower theorem in the session. In particular: (i) for a Kähler metric on M=X#k CPbar^2 with X minimal general type, derive explicitly whether C_+=(2pi^2)^-1∫|W+|^2+(96pi^2)^-1∫s^2 equals ∫s^2/(32pi^2), and prove or correct C_+>=A=c1^2(X) using the Hodge index with canonical class and exceptional areas; determine what additional assumptions are needed for inf_Kähler P=8pi^2 k and nonattainment; (ii) verify the cross-line bundle classes for u=<Phi_e',Phi_e> and w=Phi_e wedge Phi_e' when the determinant classes differ by flipping exceptional signs, including factor-of-two conventions and whether c1(u)=E_i or 2E_i; (iii) verify the amplitude identity and lower inequality P>=8pi^2 Q-4 E∫(2-rho)_+ under the stated s=-4 normalization. Give exact corrected statements, not procedural advice.

## Integrated Scientific Memo

# 核验结论

以下采用会话中的约定：

- \(W^\pm\) 是 \(\Lambda^\pm\) 上曲率算子的 Hilbert–Schmidt 范数；
- \(\Ric^\circ\) 是二阶张量范数；
- \(|\sigma(\Phi)|^2=|\Phi|^4/8\)；
- monopole 方程归一化为
  \[
  D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi);
  \]
- \(P(g)=\int|\Ric^\circ|^2\,d\mu\)，且
  \[
  C_+(g)=\frac1{2\pi^2}\int|W^+|^2\,d\mu
         +\frac1{96\pi^2}\int s^2\,d\mu .
  \]

---

## 1. Kähler 情形

### 1.1 \(C_+=\int s^2/(32\pi^2)\) 完全正确

对按给定方向定向的 Kähler 曲面，
\[
W^+:\Lambda^+\to\Lambda^+
\]
的特征值为
\[
\frac{s}{6},\qquad-\frac{s}{12},\qquad-\frac{s}{12}.
\]
因此
\[
|W^+|^2=\frac{s^2}{36}+2\frac{s^2}{144}=\frac{s^2}{24},
\]
从而
\[
\boxed{
C_+(g)=\frac1{32\pi^2}\int_Ms^2\,d\mu .
}
\]
若 Kähler 方向与预先选定方向相反，应交换 \(W^+\) 与 \(W^-\)。

四维 Chern–Weil 公式同时给出
\[
\frac{P(g)}{8\pi^2}=C_+(g)-(2\chi+3\tau)(M).
\]
对
\[
M=X\#k\overline{\mathbb {CP}}^{\,2},\qquad A=K_X^2=c_1^2(X),
\]
有
\[
2\chi(M)+3\tau(M)=A-k,
\]
故
\[
\boxed{
P(g)=8\pi^2\bigl(C_+(g)-A+k\bigr).
}
\]

---

### 1.2 固定 blow-up complex structure 上的正确 Hodge-index 论证

设
\[
\pi:M\to X,\qquad K_0=\pi^*K_X,\qquad
K_M=K_0+\sum_{i=1}^kE_i,
\]
其中
\[
K_0^2=A,\qquad K_0\cdot E_i=0,\qquad E_i\cdot E_j=-\delta_{ij}.
\]
令
\[
\Omega=[\omega],\qquad e_i=\Omega\cdot E_i>0.
\]
于是
\[
K_M\cdot\Omega=K_0\cdot\Omega+\sum_i e_i.
\]

因为 \(K_X\) 对 minimal general-type surface 是 nef 且 \(K_X^2=A>0\)，Hodge 指数定理给出
\[
K_0\cdot\Omega\ge\sqrt{A\,\Omega^2}.
\]
这里 \(K_0,\Omega\) 位于同一正锥闭包中，所以取正号。又有
\[
\int_Ms\,d\mu=4\pi c_1(M)\cdot\Omega
=-4\pi K_M\cdot\Omega,
\qquad
\Vol(g)=\frac{\Omega^2}{2}.
\]
因此
\[
\int s^2\,d\mu
=
\frac{\left(\int s\,d\mu\right)^2}{\Vol}
+\int(s-\bar s)^2\,d\mu
\]
给出精确恒等式
\[
\boxed{
C_+(g)=
\frac{(K_M\cdot\Omega)^2}{\Omega^2}
+\frac1{32\pi^2}\int_M(s-\bar s)^2\,d\mu .
}
\]
从而
\[
\begin{aligned}
C_+(g)-A
&=
\left[\frac{(K_0\cdot\Omega)^2}{\Omega^2}-A\right]
+\frac{2(K_0\cdot\Omega)\sum_i e_i}{\Omega^2}
+\frac{(\sum_i e_i)^2}{\Omega^2}\\
&\qquad
+\frac1{32\pi^2}\int(s-\bar s)^2\,d\mu\\
&\ge
\frac{2\sqrt A\,\sum_i e_i}{\sqrt{\Omega^2}}
+\frac{(\sum_i e_i)^2}{\Omega^2}
+\frac1{32\pi^2}\int(s-\bar s)^2\,d\mu .
\end{aligned}
\]
故
\[
\boxed{C_+(g)\ge A,\qquad P(g)\ge8\pi^2k.}
\]
而且若 \(k>0\)，所有 exceptional curve 都有正面积，故
\[
\boxed{C_+(g)>A,\qquad P(g)>8\pi^2k}
\]
对每个光滑 Kähler 度量成立。

也可作更细的正交分解。令
\[
\Omega_0=\Omega+\sum_i e_iE_i;
\]
则 \(\Omega_0\cdot E_i=0\) 且
\[
\Omega_0^2=\Omega^2+\sum_i e_i^2,
\]
所以
\[
K_0\cdot\Omega
=K_0\cdot\Omega_0
\ge\sqrt{A\left(\Omega^2+\sum_i e_i^2\right)}.
\]
由此得到更强的
\[
C_+(g)\ge
\frac{\left[
\sqrt{A(\Omega^2+\sum_i e_i^2)}+\sum_i e_i
\right]^2}{\Omega^2}.
\]

---

### 1.3 \(\inf_{\mathrm{K\ddot ahler}}P=8\pi^2k\) 需要额外上界输入

上面的论证只证明
\[
\inf_{\mathrm{K\ddot ahler}}P\ge8\pi^2k.
\]
精确等号等价于存在 Kähler recovery sequence \(g_j\)，使
\[
C_+(g_j)\to A,
\]
亦即
\[
\boxed{
\inf_{\mathrm{K\ddot ahler}}P=8\pi^2k
\iff
\inf_{\mathrm{K\ddot ahler}}\int s^2\,d\mu=32\pi^2A.
}
\]

必要的渐近条件包括
\[
\frac{\sum_i e_{i,j}}{\sqrt{\Omega_j^2}}\to0,\qquad
\frac{(K_0\cdot\Omega_j)^2}{\Omega_j^2}\to A,\qquad
\int(s_j-\bar s_j)^2\,d\mu_j\to0.
\]
也就是说，exceptional areas 相对整体尺度趋零，Kähler 类投影趋向 canonical ray，且标量曲率的 \(L^2\)-振荡趋零。

所给 `variational_selection_and_global_cost.tex` 中的 recovery metrics 仅被陈述为 Riemannian metrics，并未证明与固定 blow-up complex structure 相容，所以不能据此推出 Kähler 下确界等号。

一个足够的假设包是：

1. \(K_X\) ample，从而 \(X\) 有负 Kähler–Einstein 度量；
2. 对给定 blow-up 点存在 exceptional sizes 趋零的 Kähler（例如 cscK）blow-up metrics，或任何满足上述 \(C_+\to A\) 的 Kähler recovery family。

在此假设下
\[
\boxed{\inf_{\mathrm{K\ddot ahler}}P=8\pi^2k.}
\]
若 \(k>0\)，严格不等式说明该下确界不被任何光滑 Kähler 度量达到。

对 \(K_X\) nef 但非 ample 的情形，也可望由 canonical-model orbifold Kähler–Einstein 度量加 Kähler ALE resolution 得到同样的 Kähler recovery；但这一 Kähler gluing 定理未包含在给定材料中，不能当作已由材料证明的结论。

若所谓 “所有 Kähler 度量” 允许改变 \(M\) 上的 complex structure，还必须知道每个相关 complex structure 都是某个 minimal general-type surface 的恰好 \(k\) 次 blow-up，且 minimal canonical square 为 \(A\)。固定 complex structure 时无此额外问题；改变 complex structure 时需使用 Friedman–Morgan 型的 canonical/exceptional class 识别，并满足其相应假设。

当 \(k=0\) 时，
\[
P\ge0,
\]
且等号正好要求 Kähler–Einstein；因此 nonattainment 不能由上述 exceptional-area 严格性推出。

---

## 2. Cross-line bundles：determinant difference 必须除以 \(2\)

设
\[
a_\epsilon=c+\sum_i\epsilon_iE_i=c_1(L_\epsilon),
\qquad
\Phi_\epsilon\in\Gamma(S^+_\epsilon),
\qquad
\det S^+_\epsilon=L_\epsilon.
\]
选取相对 twisting line \(N_{\epsilon'\epsilon}\)，使
\[
S^+_{\epsilon'}\cong S^+_\epsilon\otimes N_{\epsilon'\epsilon}.
\]
Spin\(^c\) twisting 会使 determinant line 平方扭曲：
\[
L_{\epsilon'}\cong L_\epsilon\otimes N_{\epsilon'\epsilon}^{\,2}.
\]
故
\[
\boxed{
c_1(N_{\epsilon'\epsilon})
=\frac{a_{\epsilon'}-a_\epsilon}{2}.
}
\]
这正是 factor \(2\) 的来源。

### 2.1 内积场 \(u\)

按脚本的 Hermitian 约定，内积对第一变量共轭线性：
\[
u_{\epsilon\epsilon'}=\langle\Phi_{\epsilon'},\Phi_\epsilon\rangle
\in\Gamma(N_{\epsilon'\epsilon}^*).
\]
因此
\[
\boxed{
c_1(u_{\epsilon\epsilon'})
=\frac{a_\epsilon-a_{\epsilon'}}2
=\sum_i\frac{\epsilon_i-\epsilon_i'}2E_i.
}
\]
若只把第 \(i\) 个符号从 \(\epsilon_i\) 翻成 \(-\epsilon_i\)，则
\[
\boxed{c_1(u)=\epsilon_iE_i,}
\]
而不是 \(2\epsilon_iE_i\)。类 \(2\epsilon_iE_i\) 是 determinant-line difference
\[
a_\epsilon-a_{\epsilon'}
\]
或 \(u^2\) 的类。

若交换内积线性变量的约定，只会改变符号，不会改变“取 determinant difference 的一半”这一事实。

### 2.2 外积场 \(w\)

\[
w_{\epsilon\epsilon'}=\Phi_\epsilon\wedge\Phi_{\epsilon'}
\in\Gamma(\det S^+_\epsilon\otimes N_{\epsilon'\epsilon}),
\]
故
\[
\boxed{
c_1(w_{\epsilon\epsilon'})
=\frac{a_\epsilon+a_{\epsilon'}}2.
}
\]
若翻转指标集合 \(F\)，则
\[
\boxed{
c_1(u)=\sum_{i\in F}\epsilon_iE_i,\qquad
c_1(w)=c+\sum_{j\notin F}\epsilon_jE_j.
}
\]
若所有 exceptional signs 都翻转，则 \(c_1(w)=c\)。这并不使 \(c\) 成为 blow-up 上的 Spin\(^c\) determinant class；它仅说明 \(w\) 可取值于普通复线丛。

若存在 \(2\)-torsion，则仅由 determinant Chern classes 不能唯一确定相对 twisting line；需要固定相对 Spin\(^c\) structure。自然 blow-up sign family 给出了该选择，实上同调公式不受 torsion 影响。

### 2.3 诱导连接

若 \(B\) 是 \(N_{\epsilon'\epsilon}\) 上的相对连接，则
\[
A_{\epsilon'}=A_\epsilon+2B.
\]
写 \(f_\epsilon=-iF_{A_\epsilon}\)，则
\[
\boxed{
f_u=\frac{f_\epsilon-f_{\epsilon'}}2,\qquad
f_w=\frac{f_\epsilon+f_{\epsilon'}}2.
}
\]
因此直接把 \(f_\epsilon-f_{\epsilon'}\) 当成 \(u\)-bundle 的曲率，正会造成 \(c_1(u)=2E_i\) 的错误。

---

## 3. Paired Fierz–Walsh 恒等式

由
\[
f_\epsilon^+=-iF_{A_\epsilon}^+=2\sigma(\Phi_\epsilon),
\qquad
\rho_\epsilon=|\Phi_\epsilon|^2,
\]
有
\[
|f_\epsilon^+|^2=\frac{\rho_\epsilon^2}{2}.
\]
在 \(\rho_\epsilon>0\) 处写
\[
f_\epsilon^+=\frac{\rho_\epsilon}{\sqrt2}n_\epsilon,
\qquad |n_\epsilon|=1.
\]
局部平凡化 cross line 后，标准 \(\mathbb C^2\) Fierz 恒等式给出
\[
\boxed{
|u_{\epsilon\epsilon'}|^2
=\rho_\epsilon\rho_{\epsilon'}
\frac{1+n_\epsilon\cdot n_{\epsilon'}}2,
}
\]
\[
\boxed{
|w_{\epsilon\epsilon'}|^2
=\rho_\epsilon\rho_{\epsilon'}
\frac{1-n_\epsilon\cdot n_{\epsilon'}}2,
}
\]
故
\[
|u|^2+|w|^2=\rho_\epsilon\rho_{\epsilon'}.
\]
于是
\[
\boxed{
|f_\epsilon^+-f_{\epsilon'}^+|^2
=
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
}
\]
以及
\[
\boxed{
|f_\epsilon^+-f_{\epsilon'}^+|^2
=
\frac{(\rho_\epsilon+\rho_{\epsilon'})^2
-4|u_{\epsilon\epsilon'}|^2}{2}.
}
\]
这些式子在 spinor 零点连续延拓。

对 Walsh coefficients
\[
f_I=\mathbb E_\epsilon\!\left[
\Bigl(\prod_{i\in I}\epsilon_i\Bigr)f_\epsilon
\right],
\]
若 \(\epsilon,\epsilon'\) 独立均匀，则 Parseval 给出
\[
\boxed{
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=
\mathbb E_{\epsilon,\epsilon'}
\|f_\epsilon^+-f_{\epsilon'}^+\|_2^2.
}
\]
因此
\[
\boxed{
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=
\mathbb E_{\epsilon,\epsilon'}\int
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right]d\mu .
}
\]
不存在额外的 \(2^k\) 因子。

同时，脚本中的 kinetic split 正确：
\[
\boxed{
|\nabla_{A_\epsilon}\Phi_\epsilon|^2
=
\frac{|\zeta_\epsilon|^2}{\rho_\epsilon}
+\frac{\rho_\epsilon}{4}|\nabla n_\epsilon|^2,
\qquad
\zeta_\epsilon=
\langle\Phi_\epsilon,\nabla_{A_\epsilon}\Phi_\epsilon\rangle ,
}
\]
先在 \(\{\rho_\epsilon>0\}\) 成立，再作积分延拓。

---

## 4. \(s=-4\) 下的 amplitude 恒等式与下界

### 4.1 Weitzenböck 归一化

由
\[
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),
\qquad |\sigma(\Phi)|^2=\frac{\rho^2}{8},
\]
且 \(s=-4\)，得到
\[
\boxed{
0=\frac12\Delta\rho+|\nabla_A\Phi|^2-\rho+\frac{\rho^2}{2}.
}
\]
最大值原理给出
\[
\boxed{0\le\rho\le2.}
\]
积分后
\[
\boxed{
K:=\int|\nabla_A\Phi|^2\,d\mu
=\frac12\int\rho(2-\rho)\,d\mu.
}
\]
这与脚本得到的 \(K=I_1-I_2/2\) 一致。

令
\[
\delta_\epsilon=2-\rho_\epsilon=(2-\rho_\epsilon)_+.
\]
则
\[
-4K_\epsilon
=-2\int\rho_\epsilon\delta_\epsilon
=-4\int\delta_\epsilon+2\int\delta_\epsilon^2.
\]

---

### 4.2 精确 paired-amplitude 恒等式

会话中的 exact field-cost identity 是
\[
P-8\pi^2Q=\mathscr A-4\mathbb E_\epsilon K_\epsilon,
\]
其中
\[
\begin{aligned}
\mathscr A={}&
2\|f_\varnothing^-\|_2^2
+2\sum_{I\ne\varnothing}\|f_I^+\|_2^2\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int b(\rho_\epsilon)(2-\rho_\epsilon)^2\,d\mu
\right],
\end{aligned}
\]
且
\[
b(t)=\frac{-t^2+8t+2}{6}\ge\frac13
\qquad(0\le t\le2).
\]

代入 \(K_\epsilon\) 公式及 Walsh–Fierz identity，得到最直接的精确 amplitude 形式：
\[
\boxed{
\begin{aligned}
&P(g)-8\pi^2Q
+4\mathbb E_\epsilon\int_M(2-\rho_\epsilon)\,d\mu\\
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
(2-\rho_\epsilon)^2\,d\mu
\right].
\end{aligned}
}
\]
右端逐项非负；事实上 \(b+2\ge7/3\)。因此
\[
\boxed{
P(g)\ge
8\pi^2Q
-4\mathbb E_\epsilon
\int_M(2-\rho_\epsilon)_+\,d\mu .
}
\]
在当前 \(s=-4\) 归一化中 \(\rho_\epsilon\le2\)，所以正部可删除。

系数 \(4\) 与阈值 \(2\) 都依赖于 \(s=-4\) 和
\[
F_A^+=2i\sigma(\Phi)
\]
这两个归一化。

---

### 4.3 等价的 residual-polynomial 形式

定义
\[
m(\rho)
=
2\rho(2-\rho)-b(\rho)(2-\rho)^2.
\]
则
\[
\boxed{
m(\rho)
=
\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6.
}
\]
精确恒等式也可写成
\[
\boxed{
\begin{aligned}
P-8\pi^2Q+\mathbb E_\epsilon\int m(\rho_\epsilon)\,d\mu
={}&2\|f_\varnothing^-\|_2^2\\
&+\mathbb E_{\epsilon,\epsilon'}\int
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right]d\mu\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
\right]\ge0.
\end{aligned}
}
\]
这里必须注意
\[
m(0)=-\frac43,\qquad m(1)=\frac12;
\]
所以 \(m\) 在 \([0,2]\) 上变号，不能由它推出 \(P\ge8\pi^2Q\)。

另一方面，若只取正部，则
\[
m_+(\rho)\le4(2-\rho),\qquad 0\le\rho\le2,
\]
因为写
\[
m(\rho)=(2-\rho)q(\rho),\qquad
q(\rho)=\frac{-\rho^3+10\rho^2-2\rho-4}{6},
\]
并有 \(q(\rho)\le q(2)=4\)。故 residual 形式也推出
\[
P\ge8\pi^2Q-\mathbb E\int m_+(\rho)
\ge8\pi^2Q-4\mathbb E\int(2-\rho).
\]
该线性常数 \(4\) 是最优的，因为
\[
m(\rho)=4(2-\rho)+O((2-\rho)^2)
\qquad(\rho\to2).
\]

---

## 5. 适用范围

上述 paired identity 需要在同一个固定度量上，对每个
\[
a_\epsilon=c+\sum_i\epsilon_iE_i
\]
都有实际 monopole solution。对 \(b_+\ge2\) 的 chamber-independent ordinary monopole supply，这正是会话正文中的假设。若 \(b_+=1\)，不能无条件声称所有 sign classes 对任意度量同时有解；必须限定在提供这些类的共同 chamber，或另行证明 metric-wise simultaneous supply。

因此，最终经过核验的陈述是：

\[
\boxed{
\begin{gathered}
C_+=\frac1{32\pi^2}\int s^2,\qquad
C_+\ge A,\qquad
P\ge8\pi^2k
\quad\text{对固定 blow-up Kähler structure};\\[2mm]
k>0\Longrightarrow P>8\pi^2k
\quad\text{对每个光滑 Kähler metric};\\[2mm]
c_1(u)=\frac{a_\epsilon-a_{\epsilon'}}2,\qquad
c_1(w)=\frac{a_\epsilon+a_{\epsilon'}}2,
\end{gathered}
}
\]
所以单次 exceptional sign flip 给出 \(c_1(u)=\pm E_i\)，不是 \(\pm2E_i\)；并且在 \(s=-4\) 的给定 monopole 归一化下，
\[
\boxed{
P(g)\ge8\pi^2Q
-4\mathbb E_\epsilon\int(2-\rho_\epsilon)_+\,d\mu,
}
\]
其上方的 paired-amplitude 等式是准确的精确版本。