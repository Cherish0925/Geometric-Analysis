# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/trace/ttcs/results/step64_ttcs01_generator1_integration.md",
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Independently check the new results proposed by the Step-64 Generator integration, which were not part of the original verifier task. Concentrate on: (i) the exact harmonic-ASD test identity obtained by pairing the second AAD Bianchi equation with eta_h(Z)=nabla_{h(Z)} Omega, including the algebraic contraction, signs, factors, and the constant-s assumption; (ii) the claimed global second-jet estimate ||nabla^2 Omega||_2 + ||nabla Omega||_4^2 <= C||Rm||_2 for every closed almost-Kähler four-manifold—derive it carefully and identify norm/convention dependencies; (iii) the flux inequality (4-6U)||T|| <= ... and exactly what it can establish; and (iv) the regularized Berry/Chern form ledger gamma_delta and the limiting transverse-zero formula, including line-bundle conventions, signs, smoothness through zeros, transition-term order, and Hopf transgression. Separate proved identities from attractive but unproved construction implications. Provide corrected exposable statements.

## Output

# 独立核验备忘录

## 1. 对第二条 AAD 恒等式的 harmonic-ASD 测试

设 \((M^4,g,J,\Omega)\) 为闭 almost-Kähler 四维流形，并采用 AAD 的规范
\[
V_X:=\nabla_X\Omega=a(X)\phi-(Ja)(X)J\phi,\qquad
u=|a|^2=\frac14|\nabla\Omega|^2,
\]
其中 \(|\phi|^2=|J\phi|^2=2\)。于是
\[
t^-:=-(a\wedge Ja)^-.
\]

AAD Corollary 1 的第二式在 \(\kappa-s=6u\) 后成为
\[
\begin{aligned}
0={}&(du\wedge Z^\flat)''
+\frac{\kappa}{4}V_{JZ}
-V_{\rho_0(Z)}
+2(\delta W_3^+)''_Z
+V_{\rho_*''(Z)}\\
&+(\nabla_{JZ}\rho_*'')''
+(A_Z^+)''.
\end{aligned}
\tag{1.1}
\]

令 \(h\) 为光滑 harmonic ASD 二形式，把它也视为斜对称自同态，并定义
\[
(\eta_h)_Z=V_{h(Z)}.
\]
将 (1.1) 在 \(Z=e_i\) 处与 \(V_{h(e_i)}\) 配对后求和、积分。

### 1.1 决定符号和系数的代数收缩

由 AAD 对协向量上 \(J\) 的约定
\[
(Ja)(X)=-a(JX)
\]
可得
\[
a(Je_i)=-(Ja)(e_i),\qquad (Ja)(Je_i)=a(e_i).
\]
因此
\[
\begin{aligned}
\sum_i\langle V_{Je_i},V_{h(e_i)}\rangle
&=2\sum_i\left[-(Ja)(e_i)a(h e_i)
+a(e_i)(Ja)(h e_i)\right]\\
&=4\langle a\wedge Ja,h\rangle.
\end{aligned}
\]
因为 \(h\in\Lambda^-\)，
\[
\langle a\wedge Ja,h\rangle
=\langle(a\wedge Ja)^-,h\rangle
=-\langle t^-,h\rangle.
\]
故准确公式是
\[
\boxed{
\sum_i\langle V_{Je_i},V_{h(e_i)}\rangle
=-4\langle t^-,h\rangle.
}
\tag{1.2}
\]
这里没有遗漏 \(2\) 或 \(1/2\)。例如取
\[
a=e^1,\quad Ja=e^2,\quad
h=e^{12}-e^{34},
\]
则 \(t^-=-\tfrac12(e^{12}-e^{34})\)，两侧都等于 \(4\)。

### 1.2 积分恒等式

定义
\[
\begin{aligned}
\mathcal F_h=\int_M\sum_i\bigl[
 &\langle(du\wedge e_i^\flat)'',V_{h(e_i)}\rangle
 -\langle V_{\rho_0(e_i)},V_{h(e_i)}\rangle\\
 &+2\langle(\delta W_3^+)''_{e_i},V_{h(e_i)}\rangle
 +\langle V_{\rho_*''(e_i)},V_{h(e_i)}\rangle\\
 &+\langle(\nabla_{Je_i}\rho_*'')'',V_{h(e_i)}\rangle
 +\langle(A_{e_i}^+)'' ,V_{h(e_i)}\rangle
\bigr].
\end{aligned}
\tag{1.3}
\]
由 (1.2) 得到
\[
\int_M\kappa\langle t^-,h\rangle=\mathcal F_h.
\]
再用 \(\kappa=s+6u\)，可写成
\[
\boxed{
\int_Ms\,\langle t^-,h\rangle
=\mathcal F_h-6\int_Mu\langle t^-,h\rangle.
}
\tag{1.4}
\]

只有在 \(s\) 为常数时，才能把左侧变成 harmonic 投影：
\[
\int_Ms\,\langle t^-,h\rangle
=s\,\langle\mathsf H^-(t^-),h\rangle_{L^2}.
\]
因此恒定 \(s\) 情形的准确结论为
\[
\boxed{
s\,\langle\mathsf H^-(t^-),h\rangle
=\mathcal F_h-6\int_Mu\langle t^-,h\rangle.
}
\tag{1.5}
\]
若 \(s\) 不是常数，正确左侧是
\[
\langle\mathsf H^-(s\,t^-),h\rangle,
\]
而不是 \(s\,\langle\mathsf H^-(t^-),h\rangle\)。

在 \(s=-4\) 的归一化下，
\[
\boxed{
4\langle\mathsf H^-(t^-),h\rangle
=6\int_Mu\langle t^-,h\rangle-\mathcal F_h.
}
\tag{1.6}
\]

所以 Step-64 integration 中的代数符号、系数 \(4\)、系数 \(6\) 以及 \(s=-4\) 后的重排均正确。恒定标量曲率是提取 \(\mathsf H^-(t^-)\) 的必要前提；一般 almost-Kähler 度量不能仅靠共形改成 Yamabe 度量而仍保持原 almost-Kähler 结构。

---

## 2. 全局二阶导数估计

以下结论确实对每个闭 almost-Kähler 四维流形成立：
\[
\boxed{
\|\nabla^2\Omega\|_{L^2}
+\|\nabla\Omega\|_{L^4}^{\,2}
\le C\|\operatorname{Rm}\|_{L^2}.
}
\tag{2.1}
\]

这里 \(\nabla^2\Omega\) 表示未对称化的完整协变 Hessian，且采用 \(|\Omega|^2=2\)。常数 \(C\) 随曲率张量、二形式和 Hessian 的范数约定而变，但不依赖体积、注入半径或 Sobolev 常数。

### 2.1 一阶项

因为 \(d\Omega=0\)、\(*\Omega=\Omega\)，所以 \(\Omega\) 是 harmonic 二形式。自对偶二形式的 Weitzenböck 公式为
\[
0=\Delta_H\Omega
=\nabla^*\nabla\Omega-2W^+(\Omega)+\frac{s}{3}\Omega,
\]
即
\[
\nabla^*\nabla\Omega
=2W^+(\Omega)-\frac{s}{3}\Omega.
\tag{2.2}
\]
故点态有
\[
|\nabla^*\nabla\Omega|\le C|\operatorname{Rm}|.
\tag{2.3}
\]

由于 \(|\Omega|^2=2\) 为常数，并采用
\(\nabla^*\nabla=-\operatorname{tr}\nabla^2\)，
\[
|\nabla\Omega|^2
=\langle\nabla^*\nabla\Omega,\Omega\rangle.
\tag{2.4}
\]
结合 (2.2)，
\[
|\nabla\Omega|^2\le C|\operatorname{Rm}|.
\tag{2.5}
\]
平方积分即得
\[
\|\nabla\Omega\|_4^4
\le C\|\operatorname{Rm}\|_2^2,
\qquad
\boxed{
\|\nabla\Omega\|_4^2
\le C\|\operatorname{Rm}\|_2.
}
\tag{2.6}
\]

### 2.2 二阶项

令
\[
V=\nabla\Omega\in\Omega^1(\Lambda^2).
\]
对 \(\Lambda^2\)-值一形式使用 bundle-valued Hodge–Weitzenböck 公式：
\[
\|d^\nabla V\|_2^2+\|\delta^\nabla V\|_2^2
=\|\nabla V\|_2^2+
\int_M\langle\mathcal R V,V\rangle,
\tag{2.7}
\]
其中
\[
|\langle\mathcal R V,V\rangle|
\le C|\operatorname{Rm}|\,|V|^2.
\]

Ricci 恒等式给出
\[
(d^\nabla V)_{X,Y}
=R^{\Lambda^2}_{X,Y}\Omega,
\qquad
|d^\nabla V|\le C|\operatorname{Rm}|.
\tag{2.8}
\]
另一方面，
\[
\delta^\nabla V=\nabla^*\nabla\Omega
\]
至多相差由 codifferential 约定产生的符号，故由 (2.3)
\[
|\delta^\nabla V|\le C|\operatorname{Rm}|.
\tag{2.9}
\]
于是
\[
\begin{aligned}
\|\nabla V\|_2^2
&\le C\|\operatorname{Rm}\|_2^2
+C\int_M|\operatorname{Rm}|\,|V|^2\\
&\le C\|\operatorname{Rm}\|_2^2,
\end{aligned}
\]
最后一步直接使用点态估计 (2.5)。由于
\(\nabla V=\nabla^2\Omega\)，
\[
\boxed{
\|\nabla^2\Omega\|_2
\le C\|\operatorname{Rm}\|_2.
}
\tag{2.10}
\]

此证明不需要 Gray 曲率条件，也不需要非塌缩或标量曲率恒定。它依赖两个关键事实：\(\Omega\) 全局光滑、长度恒定，并且 \(\Omega\) harmonic。因此它不能直接用于在 spinor 零点处奇异的归一化 Bloch 场。

---

## 3. \(\mathcal F_h\) 的估计及 harmonic flux 不等式

设 \(\|h\|_2=1\)。利用分部积分、AAD 第一条恒等式以及 (2.1)，可以得到
\[
\boxed{
|\mathcal F_h|
\le C E_{\mathrm{AAD}}B_h,
}
\tag{3.1}
\]
其中
\[
E_{\mathrm{AAD}}
=\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P,
\tag{3.2}
\]
以及
\[
B_h
=\|h\|_\infty\|\operatorname{Rm}\|_2
+\|\nabla h\|_4\|\operatorname{Rm}\|_2^{1/2}.
\tag{3.3}
\]

估计的结构如下：

* \(\delta W_3^+\)、\(\nabla\rho_*''\) 和
  \(A=d^\nabla\operatorname{Ric}''+\iota_Jd\rho\)
  中的曲率导数经分部积分落到 \(V\)、\(h\) 和 \(J\) 上；
* \(d\rho=*J\delta\operatorname{Ric}''\) 消除了额外曲率导数；
* 出现的测试张量满足
  \[
  |\eta_h|\le C|h||V|,
  \]
  以及
  \[
  |\nabla\eta_h|
  \le C\bigl(
  |h||\nabla V|+|\nabla h||V|+|h||V|^2
  \bigr);
  \]
* AAD 第一式处理 \(du\) 项时，测试一形式 \(\xi_h\) 也满足同样类型的估计；
* (2.1) 给出
  \[
  \|\nabla V\|_2+\|V\|_4^2
  \le C\|\operatorname{Rm}\|_2.
  \]
* \(\rho_0\) 和 \(\operatorname{Ric}''\) 的 \(L^2\) 范数均由
  \(\sqrt P=\|\operatorname{Ric}^\circ\|_2\) 控制。

因此 (3.1) 不含曲率导数。另一方面，\(B_h\) 仍记录所选 harmonic 代表元的点态集中和一阶变化；单凭拓扑交叉型不能给出统一的 \(B_h\) 上估计。

### 3.1 精确的加权形式

令
\[
T=\mathsf H^-(t^-),\qquad
N=\|T\|_2,\qquad
h=T/N
\]
（若 \(N=0\)，以下不等式为空泛成立），并置
\[
r=t^--T,\qquad
m_h=\int_Mu|h|^2,\qquad
U=\|u\|_\infty.
\]
由 (1.6)，
\[
4N
=6\int_Mu\langle Nh+r,h\rangle-\mathcal F_h.
\]
所以有更精确的等式
\[
\boxed{
(4-6m_h)N
=6\int_Mu\langle r,h\rangle-\mathcal F_h.
}
\tag{3.4}
\]
进而
\[
(4-6m_h)N
\le 6U\|r\|_2+|\mathcal F_h|.
\tag{3.5}
\]
因为 \(m_h\le U\)，当 \(U<2/3\) 时，
\[
\boxed{
(4-6U)\|T\|_2
\le CE_{\mathrm{AAD}}B_h+6U\|r\|_2.
}
\tag{3.6}
\]
Step-64 integration 的该式正确；(3.4) 是更强、也更适合展示的版本。

一般地，若 \(s=-\sigma<0\) 为常数，则
\[
(\sigma-6m_h)N
=6\int u\langle r,h\rangle-\mathcal F_h,
\]
而有效的点态幅度条件变为 \(U<\sigma/6\)。

### 3.2 它实际给出的信息

结合
\[
T=2\pi h_a^--\mathsf H^-(\rho_0^J)
\]
以及
\[
\|T\|_2
\ge 2\pi\|h_a^-\|_2-\sqrt{P/2},
\]
可得
\[
\begin{aligned}
CE_{\mathrm{AAD}}B_h
\ge{}&(4-6U)
\left(2\pi\sqrt{k+\Pi}-\sqrt{P/2}\right)\\
&-6U\|t^--T\|_2.
\end{aligned}
\tag{3.7}
\]

因此它排除了这样一种同时出现的状态：

* \(U\) 与 \(2/3\) 保持固定距离；
* \(t^-\) 在 \(L^2\) 中接近 harmonic；
* harmonic 代表元具有受控的 \(B_h\)；
* \(W_3^+\)、\(\rho_*''\) 和 \(\operatorname{Ric}^\circ\) 同时过小。

但 (3.6) 本身不是纯 \(P\) 下界，因为 \(E_{\mathrm{AAD}}\) 还含
\(\|W_3^+\|_2\) 和 \(\|\rho_*''\|_2\)，而 \(B_h\) 可随塌缩或 harmonic 集中而增大。它精确探测的是由 harmonic flux 选出的 AAD 分量，而不是仅由 Ricci defect 决定的量。

---

## 4. Berry/Chern 正则化账本

令 \(S^+\) 为秩二正 spinor 丛，
\[
L=\det S^+,\qquad a=c_1(L).
\]
采用如下约定：

* Hermitian 内积对第二变量复线性；
* determinant connection 的复曲率为 \(F_{\mathcal A}\in i\Omega^2\)；
* 实曲率定义为
  \[
  f_{\mathcal A}=iF_{\mathcal A},
  \qquad [f_{\mathcal A}]=2\pi a.
  \]

在 \(\{\Phi\ne0\}\) 上写
\[
v=\frac{\Phi}{|\Phi|},\qquad \ell=\mathbb Cv\subset S^+.
\]
定义实 Berry 一形式
\[
\beta_B=i\langle v,\nabla_{\mathcal A}v\rangle.
\tag{4.1}
\]
于是 \(\ell\) 的实曲率为 \(d\beta_B\)。商线
\(\ell^\perp\) 满足
\[
f_{\ell^\perp}=f_{\mathcal A}-d\beta_B,
\]
故
\[
\operatorname{Hom}(\ell,\ell^\perp)
\]
的实曲率是
\[
f_{\ell^\perp}-f_\ell
=f_{\mathcal A}-2d\beta_B.
\tag{4.2}
\]

若 Bloch identification 取为
\[
\operatorname{Hom}(\ell,\ell^\perp)\cong K_J^{-1}
\cong\Omega^\perp,
\]
并与 Step 63 的 frame orientation 一致，则
\[
\boxed{
\gamma_J=f_{\mathcal A}-2d\beta_B
=R(\Omega)+t_J.
}
\tag{4.3}
\]
若把 \(K_J^{-1}\) 换成其对偶，或者把实曲率定义成 \(-iF\)，相应符号会一起改变；(4.3) 在上述明确约定下是正确的。

### 4.1 穿过 spinor 零点的光滑正则化

令
\[
\rho=|\Phi|^2.
\]
由
\[
d\rho=2\operatorname{Re}\langle\Phi,\nabla_{\mathcal A}\Phi\rangle
\]
可得
\[
\lambda:=\rho\beta_B
=i\left(
\langle\Phi,\nabla_{\mathcal A}\Phi\rangle-\frac12d\rho
\right)
=-\operatorname{Im}\langle\Phi,\nabla_{\mathcal A}\Phi\rangle.
\tag{4.4}
\]
所以 \(\lambda\) 是穿过零点仍光滑的实一形式，并在零点消失。

对每个 \(\delta>0\)，定义
\[
\beta_\delta
=\frac{\lambda}{\rho+\delta}
=\frac{\rho}{\rho+\delta}\beta_B,
\qquad
w_\delta=\frac{\rho}{\rho+\delta},
\]
以及
\[
\gamma_\delta=f_{\mathcal A}-2d\beta_\delta.
\tag{4.5}
\]
此时 \(\beta_\delta,\gamma_\delta\) 都在整个 \(M\) 上光滑，并且
\[
d\gamma_\delta=0,\qquad
[\gamma_\delta]=2\pi a.
\tag{4.6}
\]

在非零点集上，
\[
\begin{aligned}
\gamma_\delta
&=f_{\mathcal A}-2d(w_\delta\beta_B)\\
&=w_\delta(f_{\mathcal A}-2d\beta_B)
 +(1-w_\delta)f_{\mathcal A}
 -2dw_\delta\wedge\beta_B.
\end{aligned}
\]
因此
\[
\boxed{
\gamma_\delta^-=
w_\delta(R(\Omega)^-+t_J^-)
+(1-w_\delta)f_{\mathcal A}^-
-2(dw_\delta\wedge\beta_B)^-.
}
\tag{4.7}
\]

若 \(h\) 为光滑 harmonic ASD 二形式，且 \(h_a^-\) 是 \(a\) 的 harmonic ASD 代表元，则
\[
\boxed{
\begin{aligned}
2\pi\langle h_a^-,h\rangle
={}&\int_Mw_\delta
 \langle R(\Omega)^-+t_J^-,h\rangle\\
&+\int_M(1-w_\delta)
 \langle f_{\mathcal A}^-,h\rangle\\
&-2\int_M
 \langle(dw_\delta\wedge\beta_B)^-,h\rangle .
\end{aligned}
}
\tag{4.8}
\]
这是一个全局光滑且完全准确的 degree-two flux 公式。

### 4.2 横截孤立零点

设零点 \(z\) 横截。取 \(r=d(x,z)\)，则
\[
c r^2\le\rho\le Cr^2,\qquad
|d\rho|\le Cr,
\]
并且
\[
|\beta_B|\le Cr^{-1},\qquad
|d\beta_B|\le Cr^{-2}.
\]
由 (4.3)，
\[
|t_J|\le Cr^{-2}.
\]
所以 \(t_J\in L^1_{\mathrm{loc}}\)，但一般不在 \(L^2_{\mathrm{loc}}\)。

连接球面上的端项满足
\[
\left|\int_{S_\varepsilon^3(z)}\beta_B\wedge h\right|
\le C\varepsilon^2.
\tag{4.9}
\]
正则化过渡项的主积分为
\[
\int_0^{r_0}
\frac{\delta r^3}{(r^2+\delta)^2}\,dr
=
\frac{\delta}{2}
\left[
\log\frac{r_0^2+\delta}{\delta}
+\frac{\delta}{r_0^2+\delta}-1
\right],
\]
故
\[
\boxed{
\left|
\int_M\langle
(dw_\delta\wedge\beta_B)^-,h\rangle
\right|
\le C_h\,\delta\bigl(1+|\log\delta|\bigr).
}
\tag{4.10}
\]
同时，
\[
\int(1-w_\delta)|f_{\mathcal A}|=O(\delta),
\]
而
\[
\int(1-w_\delta)|t_J|
=O\!\left(\delta|\log\delta|\right).
\]
因此 (4.8) 可令 \(\delta\to0\)，得到绝对收敛的 improper integral：
\[
\boxed{
\int_{M\setminus Z(\Phi)}
\langle t_J^-,h\rangle
=
2\pi\langle h_a^-,h\rangle
-
\int_{M\setminus Z(\Phi)}
\langle R(\Omega)^-,h\rangle.
}
\tag{4.11}
\]
孤立的余维四零点不产生额外 degree-two 项；其拓扑信息出现在 degree four。

### 4.3 Hopf transgression

在 \(\{\Phi\ne0\}\) 上，由
\(\gamma_J=f_{\mathcal A}-2d\beta_B\) 直接展开：
\[
\begin{aligned}
\gamma_J\wedge\gamma_J
-f_{\mathcal A}\wedge f_{\mathcal A}
&=4d\beta_B\wedge d\beta_B
-4f_{\mathcal A}\wedge d\beta_B\\
&=4d\bigl(
\beta_B\wedge d\beta_B
-\beta_B\wedge f_{\mathcal A}
\bigr).
\end{aligned}
\]
故
\[
\boxed{
\gamma_J^2-f_{\mathcal A}^2
=
4d\bigl(
\beta_B\wedge d\beta_B
-\beta_B\wedge f_{\mathcal A}
\bigr).
}
\tag{4.12}
\]

对连接球面的定向作一致选择，
\[
\boxed{
q_z=\frac1{4\pi^2}
\lim_{\varepsilon\to0}
\int_{S_\varepsilon^3(z)}
\beta_B\wedge d\beta_B
}
\tag{4.13}
\]
是整数 Hopf 指数。归一化 \(1/(4\pi^2)\) 正确：标准 Hopf connection 满足
\[
\left|\int_{S^3}\beta_B\wedge d\beta_B\right|=4\pi^2.
\]
此外
\[
\int_{S_\varepsilon^3}\beta_B\wedge f_{\mathcal A}
=O(\varepsilon^2),
\]
所以该平滑曲率项不改变局部 Hopf 数。

若 spinor 截面横截，则这些局部指数之和等于
\[
\left\langle c_2(S^+),[M]\right\rangle
=
\frac{a^2-(2\chi+3\tau)}4.
\tag{4.14}
\]
对 best-sign 类 \(a^2=2\chi+3\tau\)，总带符号和为零；这允许不同零点的指数互相抵消，但各零点附近的无权 \(L^2\) twist 对数发散仍分别存在。

值得明确的是：\(\gamma_\delta\) 是同一 determinant line 上经全局一形式修改所得的曲率账本，并不是某个穿过零点的光滑单位 Bloch 场之 frame Chern form。Hopf 信息也不显式出现在 (4.8)；它由未正则化公式 (4.12) 的连接球面积分保留。

---

## 5. 已证数学内容与尚未得到的构造结论

现有材料支持以下结果：

1. harmonic-ASD 配对公式 (1.5)，包括符号、系数及恒定 \(s\) 前提；
2. 对任意闭 almost-Kähler 四维流形成立的尺度不变二阶估计 (2.1)；
3. 无曲率导数的 \(\mathcal F_h\) 估计 (3.1)，以及精确加权恒等式 (3.4)；
4. 全局光滑的 Berry/Chern 账本 (4.8)、横截零点极限 (4.11) 和 Hopf transgression (4.12)。

这些公式尚未给出以下几何对象：

* 仅由 \(P=\int|\operatorname{Ric}^\circ|^2\) 决定的全局正下界；
* 从 \(\gamma_\delta\) 产生的全局光滑 orthogonal almost-complex structure；
* 具有正确 \(c_1\)、近 harmonic twist、缩小零核且 \(P=o(k)\) 的闭度量序列；
* 对 \(B_h\) 的拓扑型统一估计；
* 将 \(W_3^+\) 与 \(\rho_*''\) 的 harmonic-flux 测试分量直接压到 \(P\) 中的估计。

因此，Step-64 integration 中四项新结果在适当约定下均可作为严格命题使用；它们把未决部分集中到了 harmonic 代表元的几何控制、AAD financing 分量与 Ricci defect 的联系，以及奇异 Bloch 数据向真实 Levi-Civita frame twist 的实现问题。