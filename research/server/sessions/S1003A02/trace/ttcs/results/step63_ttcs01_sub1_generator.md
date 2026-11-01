# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md"
  ]
}
```

## Task

Research question for the open-range Einstein-gap lower bound on M = X#kCP̄² (X minimal general type, k < A/3). Step 63 (file attached) shows: (i) for every metric and every orthogonal almost complex structure J, the exceptional flux 2π|c1(J)^-| ≥ 2π√k must be carried by J-invariant tracefree Ricci (costing P) or by the ASD frame twist (α∧β)^-; (ii) all rational-cohomology/SW/Chern–Weil constraints are saturated at p = 0 only by configurations made of W⁺ = 0 negative Einstein patches with the Chern numbers of an orientation-reversed fake projective plane, so what is unpriced is the joining / transition between W⁺-carrying Kähler-type regions and twist-carrying W⁺≈0 regions. Develop concrete, provable mechanisms for a 'domain-wall' lower bound: a quantitative estimate showing that a region where the frame twist carries flux 2π, bordered by a region where J is nearly parallel and W⁺ is of Kähler type with s<0, costs P ≥ c·8π² with explicit c>0 (or explain why no such bound can hold, with a construction sketch of a cheap fat transition). Consider: localized Chern–Weil/Gauss–Bonnet on the wall with boundary transgression terms; monotonicity or capacity arguments for the twist energy ∫|(α∧β)^-|² ≤ ∫|∇Ω|⁴/32; the role of the zeros of the Nijenhuis tensor (c2 = 5χ+6τ); comparison with the 2-ended AE neck bound P ≥ 32π²; and whether the competitor X#k\overline{FPP} could have α < 8π²k. State precise inequalities with quantifiers and name what would need to be proved or computed to decide.

## Output

这里有一个相当清楚的分层结论：

1. **若 wall 退化为一个单端 AE 的 \(\#_m\overline{\mathbf{CP}}^{\,2}\) 型泡，则局部 Chern–Weil 公式已经给出精确的单位 tariff**
   \[
   \int |\Ric^\circ|^2\ge 8\pi^2m.
   \]
2. **若 joining 退化为两端 AE neck，则精确代价是**
   \[
   \int |\Ric^\circ|^2\ge 32\pi^2,
   \]
   标量平坦、共形平坦的 Schwarzschild neck 达到等号。
3. **仅凭 \(2\pi\) frame-twist flux、\(J\) 的旋转或 Nijenhuis 零点，不能推出任何正的 \(P\)-代价。** 对任意正下界，必须额外控制端面上的 Euler–signature transgression，或把 \(J\) 与 SW 旋量/调和自对偶形式绑定，使 twist 满足一个椭圆强制估计。
4. **真正尚未定下的是 fat wall：** 它既不产生 AE 泡，也不产生 AE neck，而是让端面 transgression 在一个宏观或塌缩 collar 中变化。这个通道确实可能很便宜；cusp joining 给出一个明确的异拓扑模型。

下面给出可直接使用的精确公式与候选定理。

---

## 1. 局部 Euler–signature 公式：AE 泡自动给出 \(c=1\)

设 \(U\) 是紧致定向四维区域，端面为 \(Y=\partial U\)。记标准 Euler 与 signature transgression 为 \(\mathcal E_Y,\mathcal S_Y\)，归一化为

\[
8\pi^2\chi(U)
=
\int_U\left(|W^+|^2+|W^-|^2-\frac12|\Ric^\circ|^2+\frac{s^2}{24}\right)
+\mathcal E_Y,
\]

\[
12\pi^2\tau(U)
=
\int_U\left(|W^+|^2-|W^-|^2\right)+\mathcal S_Y.
\]

于是有精确局部恒等式

\[
\boxed{
P(U)
=
4\int_U|W^+|^2+\frac1{12}\int_U s^2
-8\pi^2\bigl(2\chi(U)+3\tau(U)\bigr)
+2\bigl(\mathcal E_Y+\mathcal S_Y\bigr).
}
\tag{1}
\]

这里 \(\mathcal E_Y\) 是第二基本形式与 \(Y\) 内蕴曲率的显式三次多项式积分；\(\mathcal S_Y\) 可写成 Levi-Civita Chern–Simons 项，若采用 APS 形式则等价地出现 \(\eta(Y)\)。

### 单端 AE 泡

若 \(U_\infty\) 是完整单端 AE 四流形，端为 \(S^3\)，且

\[
U_\infty\simeq
\left(\#_{j=1}^m\overline{\mathbf{CP}}^{\,2}\right)\setminus\{\mathrm{pt}\},
\]

则

\[
\chi(U_\infty)=m+1,\qquad \tau(U_\infty)=-m.
\]

AE 端满足

\[
\mathcal E_{S_R^3}\longrightarrow 8\pi^2,\qquad
\mathcal S_{S_R^3}\longrightarrow 0.
\]

代入 (1) 得到

\[
\boxed{
P(U_\infty)
=
8\pi^2m
+4\int_{U_\infty}|W^+|^2
+\frac1{12}\int_{U_\infty}s^2
\ge 8\pi^2m.
}
\tag{2}
\]

因此，只要一列度量把 \(m\) 个 exceptional classes 隔离成一个 \(S^3\)-端 AE 泡，就有缺陷测度量化

\[
\liminf_i\int_{U_i}|\Ric^\circ_{g_i}|^2\ge 8\pi^2m.
\tag{3}
\]

这正是所求的 \(c=1\)，而且与 Burns 泡一致：\(m=1\)、标量平坦、\(W^+=0\) 时达到 \(8\pi^2\)。

### 有限尺度版本

若

\[
U\cong
\left(\#_{j=1}^m\overline{\mathbf{CP}}^{\,2}\right)\setminus B^4
\]

且端面满足

\[
\mathfrak b(Y):=\mathcal E_Y+\mathcal S_Y\ge 8\pi^2-\delta,
\]

则 (1) 直接给出

\[
\boxed{
P(U)\ge 8\pi^2m-2\delta.
}
\tag{4}
\]

若端面经尺度归一后在 \(C^2\) 中与欧氏大球面相差 \(\varepsilon\)，第二基本形式也相差 \(\varepsilon\)，那么

\[
\delta\le C\varepsilon,
\]

其中 \(C\) 可由 Euler transgression 的显式多项式逐项算出。于是

\[
P(U)\ge 8\pi^2m-C'\varepsilon.
\tag{5}
\]

这是一条已经可证明的 domain-wall 定理：它所需的几何输入不是 \(J\) 本身，而是承载 exceptional topology 的区域具有近 AE 的 \(S^3\) 端。

---

## 2. 两端 AE neck：\(32\pi^2\) 是精确值，不是启发式数值

对有 \(n\) 个平凡球面端的完整 AE 四流形，

\[
P
=
2\int|W|^2+\frac1{12}\int s^2
+16\pi^2\bigl(n-\chi\bigr).
\tag{6}
\]

若 neck 拓扑为 \(S^3\times\mathbb R\)，则 \(n=2,\chi=0,\tau=0\)，故

\[
\boxed{
P_{\mathrm{neck}}
=
32\pi^2
+2\int|W|^2+\frac1{12}\int s^2
\ge32\pi^2.
}
\tag{7}
\]

标量平坦、共形平坦的 Riemannian Schwarzschild neck 达到等号。

有限 annulus 版本同样来自 (1)：若 \(U\simeq S^3\times I\) 且两个端面的总 transgression 满足

\[
\mathfrak b(\partial U)\ge 16\pi^2-\delta,
\]

则

\[
\boxed{
P(U)\ge32\pi^2-2\delta.
}
\tag{8}
\]

在旋转对称类

\[
g=dt^2+f(t)^2g_{S^3}
\]

中可直接看到这一点。设

\[
A=-\frac{f''}{f},\qquad
B=\frac{1-f'^2}{f^2}.
\]

则

\[
|\Ric^\circ|^2=3(A-B)^2
\]

以及

\[
\boxed{
P
=
6\pi^2\int
\frac{\bigl(f'^2-ff''-1\bigr)^2}{f}\,dt.
}
\tag{9}
\]

两端欧氏条件 \(f(t)\sim |t|\) 将 (9) 的下确界固定为 \(32\pi^2\)。所以 shrinking neck 绝不会给出低于单位 tariff 的 joining；它甚至支付四个单位。

---

## 3. fat wall 的核心量是端面 transgression，而不是单独的 flux

公式 (4) 表明，低于 \(8\pi^2m\) 的唯一局部通道是

\[
\mathfrak b(Y)<8\pi^2.
\]

因此适合证明的定量命题不是笼统的“twist 有代价”，而是下面的 **transgression susceptibility**：

设 \(U\) 承载 \(m\) 个负定生成元，\(A\) 是其外侧 wall。若存在统一的 \(q<\infty\) 与误差 \(\varepsilon\)，使

\[
\boxed{
\bigl(8\pi^2-\mathfrak b(Y)\bigr)_+
\le
q\int_{U\cup A}|\Ric^\circ|^2+\varepsilon,
}
\tag{10}
\]

则由 (4)

\[
(1+2q)P(U\cup A)\ge8\pi^2m-2\varepsilon,
\]

即

\[
\boxed{
P(U\cup A)
\ge
\frac{8\pi^2m-2\varepsilon}{1+2q}.
}
\tag{11}
\]

所以显式常数为

\[
c=\frac{1}{1+2q}
\]

至端面误差。若能证明 \(q=0\)，恢复 \(c=1\)；任意有限 \(q\) 已给出正 tariff。

几何上，(10) 需要把 Kähler-type 外相

\[
W^+\approx W_K(s,\Omega)
:=
\frac{s}{4}P_\Omega-\frac{s}{12}I_{\Lambda^+},
\qquad \nabla\Omega\approx0,
\]

与内侧 \(W^+\approx0\)、\(u\approx|s|/6\) 的相通过一个 collar 联系起来。仅有两端的代数相型并不控制 \(\mathfrak b(Y)\)；还需要非塌缩、受控 Sobolev 常数，或者由某个椭圆方程导出的 collar 紧致性。

---

## 4. twist capacity 给出固定的 \(L^4\) 扭转量，但本身不产生 \(P\)

记

\[
T_U:=\|(\alpha\wedge\beta)^-\|_{L^2(U)}.
\]

Step 63 的点态估计给出

\[
T_U^2
\le
\frac1{32}\int_U|\nabla\Omega|^4.
\tag{12}
\]

若 wall 内 twist 承担至少 \(2\pi(1-\delta)\) 的一单位 flux，则

\[
\boxed{
\int_U|\nabla\Omega|^4
\ge128\pi^2(1-\delta)^2.
}
\tag{13}
\]

这是真正的临界维 capacity 量化。但要转成 \(P\)，必须再有某种 coercivity，例如

\[
\boxed{
T_U^2
\le
C_{\mathrm{tw}}\,P(U)
+\mathcal R_{\partial U}
+\mathcal S_{\mathrm{phase}},
}
\tag{14}
\]

其中 \(\mathcal R_{\partial U}\) 是端面数据，\(\mathcal S_{\mathrm{phase}}\) 测量 \(W^+\) 偏离两相模型以及 SW/LeBrun slack。

若误差为零，(14) 与局部 flux 分解

\[
\sqrt{\frac{P(U)}2}+T_U\ge2\pi
\]

合并为

\[
\boxed{
P(U)\ge
\frac{4\pi^2}
{\bigl(\sqrt{C_{\mathrm{tw}}}+1/\sqrt2\bigr)^2}
=
8\pi^2\,
\frac{1}
{2\bigl(\sqrt{C_{\mathrm{tw}}}+1/\sqrt2\bigr)^2}.
}
\tag{15}
\]

这是一个完全显式的 \(c>0\)。

### 为什么 (14) 对任意 \(J\) 不成立

取

\[
M=\Sigma_{m+1}\times\Sigma_{n+1}
\]

配同 Einstein 常数的双曲乘积度量。设 \(a,b\) 为两个因子的整数二阶类。对任何

\[
c=2r\,a+2s\,b,\qquad rs=mn,
\]

都有

\[
c^2=2\chi(M)+3\tau(M),
\]

且 \(c\equiv w_2(M)\pmod2\)。Hirzebruch–Hopf 理论给出相应几乎复结构；把它正交化不改变 \(c_1\)。当 \(r:s\ne m:n\) 时，

\[
c^-_g\ne0.
\]

然而乘积度量是 Einstein，所以

\[
P(g)=0.
\]

此时全部 ASD Chern flux 必须由 \((\alpha\wedge\beta)^-\) 承担。因而任何不把 \(J\) 与 SW 旋量、调和自对偶形式或 LeBrun 近等号结构绑定的

\[
T_U^2\le C P(U)
\]

都不可能成立。

更强地，临界四维 annulus 的旋转本身可以任意便宜。令

\[
\Omega(r)=\cos\theta(r)\Omega_0+\sin\theta(r)\Omega_1,\qquad
\theta(r)=\frac{\log(r/r_0)}{\log(R/r_0)}\Delta\theta .
\]

在欧氏 annulus 上，

\[
\int|\nabla\Omega|^4
=
\frac{8\pi^2(\Delta\theta)^4}
{\bigl(\log(R/r_0)\bigr)^3}.
\tag{16}
\]

当 conformal modulus 趋于无穷时该量趋于零。这个一维旋转还可选取使 \(\alpha\wedge\beta=0\)。因此 wall 的“换 frame”本身没有固定 tension；真正的 \(2\pi\) flux 留在内侧拓扑核心中。

对 SW 产生的 \(J\)，(14) 的实质是控制

\[
\frac{\nabla\psi}{|\psi|}
\]

的非加权 \(L^4\) 范数。SW Weitzenböck 公式天然控制的是

\[
\int |\psi|^2\left|\nabla\frac{\psi}{|\psi|}\right|^2,
\]

所以还需要关于旋量零集的频率函数或可移除奇性估计。这个缺口可以精确表述为：证明

\[
\int_U\left|\nabla\frac{\psi}{|\psi|}\right|^4
\le C\,P(U)+C\,(\text{SW slack})+C\,(\text{端面项}).
\tag{17}
\]

---

## 5. Nijenhuis 零点只提供相对指标，不自动产生每类一个单位的能量

对几乎 Kähler四流形，Nijenhuis 张量可视作

\[
N\in\Gamma\bigl(T^{1,0}\otimes K^{-1}\bigr),
\]

并且

\[
c_2\bigl(T^{1,0}\otimes K^{-1}\bigr)
=
c_2+2c_1^2
=
5\chi+6\tau.
\tag{18}
\]

在

\[
M=X\#k\overline{\mathbf{CP}}^{\,2}
\]

上，

\[
5\chi(M)+6\tau(M)=c_2(X)+2A-k.
\tag{19}
\]

这个数随一次 blow-up 减少一，而不是增加一。因此它不能直接给出“每个 exceptional class 至少一个零点”的正计数。外侧 Kähler 区域又有 \(N\equiv0\)，使零集不是横截的孤立点。

若某个内端面上 \(|N|\ge\nu>0\)，则归一化

\[
\widehat N=\frac{N}{|N|}:Y^3\longrightarrow S^3
\]

有相对次数 \(d\)。Hadamard 不等式给出显式三维能量量化

\[
\boxed{
\int_Y|d\widehat N|^3
\ge6\sqrt3\,\pi^2|d|.
}
\tag{20}
\]

要把 (20) 变成四维 \(P\)-下界，需要 AAD 结构方程导出的估计，例如

\[
\boxed{
\int_U|\nabla N|^2
\le
C\int_U|\Ric^\circ|^2
+C\int_U\bigl(|W_2^+|^2+|W_3^+|^2\bigr)
+C\,\mathcal R_{\partial U}.
}
\tag{21}
\]

再结合 trace Sobolev 与 \(|N|\ge\nu\)，才可能把次数变成固定代价。几乎 Kähler恒等式 63.AK 已经把 \(W_2,W_3\) 放进 \(P\)，所以 (21) 是自然目标；其核心是从 AAD 的一阶结构方程中提取 \(\nabla N\)，并处理规范 1-形式 \(b\)。

---

## 6. chiral Levi-Civita connection 是更自然的 wall 表示

令 \(A^+\) 为 \(\Lambda^+\) 上的 Levi-Civita \(SU(2)_+\) connection。取标准迹归一化后，

\[
\boxed{
P(g)=4\|F_{A^+}^-\|_{L^2}^2.
}
\tag{22}
\]

这就是 Atiyah–Hitchin–Singer 表示：\(g\) Einstein 当且仅当 \(A^+\) 的曲率是自对偶的。

因此 domain-wall 问题可改写为：

> 在承载一个负定生成元的四维 cobordism 上，连接 \(A^+(g)\) 从 Kähler-reducible 状态过渡到 \(W^+\simeq0\) 的 definite 状态时，其反自对偶曲率是否具有统一能隙？

端面 Chern–Simons 公式给出

\[
\frac1{8\pi^2}\int_U\operatorname{tr}(F_{A^+}\wedge F_{A^+})
=
\operatorname{CS}(A^+|_Y)+n.
\tag{23}
\]

但对一般 \(SU(2)\) connection，非零拓扑荷可完全由自对偶 instanton 承担，使 \(F^-=0\)。所以仅计算 Chern–Simons 跳跃还不够；必须利用

\[
A^+=A^+(g)
\]

这一 metricity 条件，以及 \(s=-4\)、外侧 Kähler 特征值

\[
\left(-\frac23,\frac13,\frac13\right)
\]

和内侧 \(W^+=0\) 的相结构。纯 connection 表述中，这对应对 \(F_i\wedge F_j\) 的 algebraic “perfectness”方程施加拓扑与端面数据。

一个可计算的对称模型是 biaxial Bianchi IX：

\[
g=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+c(t)^2\sigma_3^2.
\]

CP̄² puncture 的 bolt 条件是 \(c=0\)、\(a>0\) 及相应光滑导数关系；外端数据取 CH Kähler collar 的 Berger 球面数据。泛函为

\[
\mathcal P[a,c]
=
\operatorname{Vol}(SU(2))
\int a^2c\,
\sum_{j=0}^3\bigl(\lambda_j-\bar\lambda\bigr)^2\,dt,
\tag{24}
\]

其中 \(\lambda_j\) 是该 ansatz 的四个 Ricci 特征值。若此变分问题的下确界是 \(8\pi^2\)，且唯一退化极限为 Burns 型 AE 泡，就得到对称类中的 \(c=1\)。若出现 \(<8\pi^2\) 的光滑轨道，则它会直接给出 cheap fat transition，并同时给出端面 transgression 如何跌破 \(8\pi^2\)。

---

## 7. phase 描述本身不能排除 cheap fat wall

存在一个清楚的 cusp 模型。取两块具有同型 cusp 截面的有限体积复双曲四流形；一块取复定向，另一块取相反定向。第一块满足 Kähler-type \(W^+\ne0\)，第二块在全局定向下满足 \(W^+=0\)。在深度 \(T\) 截断 cusp 并平滑拼接。

cusp 截面体积按

\[
\operatorname{Vol}(Y_T)=O(e^{-QT})
\]

衰减。反射造成的第二基本形式跳跃可在固定长度 collar 内平滑，使 \(|\Ric^\circ|=O(1)\)，从而

\[
\boxed{
P_{\mathrm{wall}}=O(e^{-QT})\longrightarrow0.
}
\tag{25}
\]

这个模型的端面是 infranil 三流形，而不是 exceptional summand 的 \(S^3\)。它说明：

- Kähler-type \(W^+\) 与 \(W^+=0\) 两相本身并不产生固定 tension；
- 塌缩截面可以让 transgression 在极小体积内变化；
- \(Y\simeq S^3\) 的拓扑、负定填充、非塌缩或相应 Floer 数据必须进入定理。

甚至 \(S^3\) 也可用 Berger 度量沿 Hopf 纤维塌缩且保持截面曲率受控，所以仅写 \(Y\cong S^3\) 仍不够；需要控制归一化 injectivity radius、Sobolev 常数，或直接控制 \(\mathfrak b(Y)\)。

---

## 8. \(\overline{\mathrm{FPP}}\) competitor：AE 通道不能低于 \(8\pi^2\)，fat 通道仍开放

反向 fake projective plane 满足

\[
\chi=3,\qquad \tau=-1,
\]

与 \(\overline{\mathbf{CP}}^{\,2}\) 有相同的有理交叉型和 Chern 数值。其 puncture \(U=\overline{\mathrm{FPP}}\setminus\{\mathrm{pt}\}\) 有

\[
\chi(U)=2,\qquad \tau(U)=-1.
\]

因此任何具有平凡 \(S^3\) 单 AE 端的完整度量都满足

\[
\boxed{
P(U)
=
8\pi^2
+4\int_U|W^+|^2
+\frac1{12}\int_U s^2
\ge8\pi^2.
}
\tag{26}
\]

所以：

- 通过把每个 \(\overline{\mathrm{FPP}}\) 缩成单端 AE 泡来构造 \(X\#k\overline{\mathrm{FPP}}\)，不可能得到 \(P<8\pi^2k\)；
- 通过两端 AE neck joining，模型代价反而是 \(32\pi^2k\)；
- 若
  \[
  \alpha\bigl(X\#k\overline{\mathrm{FPP}}\bigr)<8\pi^2k,
  \]
  则近极值序列必须采用宏观 fat joining、塌缩且带非平凡 \(\eta\)-修正的 joining，或者趋近一个真正的 Einstein metric。

特别地，若 \(X\#k\overline{\mathrm{FPP}}\) 存在 Einstein metric，则其 \(\alpha=0\)。现有 SW/Chern–Weil 数值在 \(k<A/3\) 时并不排除这种可能。

还有一个拓扑细节：闭的反向 FPP 本身不能承载诱导该反向定向的几乎复结构，因为其交叉型为 \(\langle-1\rangle\)，而几乎复结构要求

\[
c_1^2=2\chi+3\tau=3,
\]

这在负定秩一格上不可能。Step 63 的 FPP 是局部 Chern 数值模型，不是闭的几乎 Kähler相。连接到 \(X\) 后，全局正方向来自 \(X\)，总流形仍可能有相应 \(c_1\)。

---

## 9. 最锋利的可证命题形状

综合上述，最有希望的定理可以写成：

> **量化 wall 命题。** 给定 \(\iota>0\) 与 Sobolev 常数 \(C_S\)，存在
> \[
> c(\iota,C_S)>0,\qquad \varepsilon_0>0,
> \]
> 使得对每个 Yamabe 度量 \(s\equiv-4\)，若 \(U\cong\overline{\mathbf{CP}}^{\,2}\setminus B^4\) 承担一单位 \(c_1^-\)-flux，外 collar 满足
> \[
> \|\nabla\Omega\|_{L^4}
> +\|W^+-W_K(-4,\Omega)\|_{L^2}
> \le\varepsilon_0,
> \]
> 内侧满足
> \[
> \|W^+\|_{L^2}
> +\|u-2/3\|_{L^2}
> \le\varepsilon_0,
> \]
> 且 collar 在所有相关尺度上具有体积比下限 \(\iota\) 与 Sobolev 常数上界 \(C_S\)，则
> \[
> \int_{U\cup A}|\Ric^\circ|^2
> \ge c(\iota,C_S)\,8\pi^2.
> \]

这个命题可由下面两种实质不同的估计之一推出：

\[
(8\pi^2-\mathfrak b(Y))_+
\le q(\iota,C_S)\,P(U\cup A)+O(\varepsilon_0),
\tag{27}
\]

或

\[
\|(\alpha\wedge\beta)^-\|_2^2
\le C(\iota,C_S)P(U\cup A)+O(\varepsilon_0).
\tag{28}
\]

(27) 是局部 Chern–Weil/APS 路线；(28) 是 AAD–SW 椭圆路线。前者在 AE 极限给出 \(c=1\)，后者通过 (15) 给出显式较小常数。

决定 fat wall 是否真实便宜的三个计算量是：

\[
\inf \mathcal P[a,c]
\quad\text{在 CP̄² bolt–CH collar 的 Bianchi IX 类中},
\]

\[
\inf\bigl(\mathcal E_Y+\mathcal S_Y\bigr)
\quad\text{在满足两相数据与非塌缩条件的端面上},
\]

以及

\[
\inf P\bigl(\overline{\mathrm{FPP}}\setminus B^4\bigr)
\quad\text{在给定 CH 型外端数据、非 AE 的 fat fillings 中}.
\]

若第一个量等于 \(8\pi^2\)，第二个量保持在 \(8\pi^2\) 附近，并且第三个量不低于 \(8\pi^2\)，则单位 tariff 机制基本闭合。若其中任一量严格低于 \(8\pi^2\)，相应极值度量会给出具体的 cheap fat transition，并说明 \(\alpha(X\#k\overline{\mathrm{FPP}})\) 乃至 \(\alpha(X\#k\overline{\mathbf{CP}}^{\,2})\) 在 open range 中可能趋向零。