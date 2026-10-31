# O10：同丛有界替代截面、Chern 类集中与端点范围扩展

2026-09-29。直接续接 `00_Research_Result.md` 的 R1–R2；不改变原统一积分障碍、N1 或 I40/I41。

## 0. 本轮结论与证据范围

本文推导一个新的连接：**不必先控制实际三次扭率的四次导数；可在同一个负手性扭率丛中，用有界 rough-Laplacian resolvent 截面替代它来测试第二 Chern 类。** 实际场用于证明替代截面的幅度集中，而特征类只依赖丛，不要求测试截面本身仍是原三次表达式。

在下列明示的既有 R2 结论及有界反自对偶拟合成立的前提下，本文证明：

1. 任意假想 O10 零端序列都必须携带一个普适正量的、归一化的 **高幅度反自对偶 Weyl 能量**；总量或高幅度尾部不能任意小。
2. 特别地，若 `|W^-|^2` 对归一化体积一致可积，则不能发生 O10 零端逃逸。这里不要求点态 Ricci 界、Sobolev、不塌缩或直径界。
3. 与原稿的 Euler 密度预算结合，存在普适 `delta_top>0`，使 O10 的全参数间隙在 `chi/A <= 3/8 + delta_top` 上成立。它包含此前尚未由纯预算排除的临界 `3/8`，并超过该阈值一个正量。本文不给出该正量的最佳数值。

**没有证明任意大有限 `chi/A` 下的一般 O10，也没有决定 O11 最佳首项。** 本文主命题是依赖明示前置结果的解析推导；没有声称已获外部同行认证或完成全球原创性检索。

---

## 1. 冻结输入：只继承实际同解结论

考虑一列闭、定向、连通四维流形及其度量。采用原稿已经证明的共形归约，令

\[
 s_{g_j}=-4,\qquad D_{A_j}\Phi_j=0,\qquad
 F_{A_j}^{+}=2i\sigma(\Phi_j),\qquad 0\le\rho_j=|\Phi_j|^2\le2.
\]

原实际供给与拓扑假设保持为

\[
 p_j=(a_{g_j}^{+})^2\ge A_j>0,\qquad a_j^2\ge T_{+,j}=2\chi_j+3\tau_j.
\]

下文 `tau_j` 用于三次扭率截面时写作 `\tau_j^{\mathrm{sp}}`，而签名写 `\operatorname{sign}(M_j)`，避免混淆。连接符号 `A_j` 与拓扑预算 `A_j` 在源稿中重名；正文出现 `F_A` 时指连接，单独的 `A_j` 在拓扑比值中指预算。

设

\[
 \eta_j=\fint|\operatorname{Ric}_{g_j}+g_j|^2
       +D_{\beta_j}/V_j+\beta_j^{-2}\longrightarrow0,
 \qquad\beta_j\longrightarrow\infty.
\]

所有平均均相对于概率测度 `dmu_j=dV_j/V_j`；子集积分也除以整个流形体积。

定义复秩二丛

\[
 E_j=S^-_j\otimes L_j,
\]

其 determinant 为 `L_j^3`，诱导连接记 `\nabla_j`，相应负手性 Dirac 算子记 `\mathcal D_j=D^-_{3A_j}`。实际三次扭率为

\[
 t_j:=\tau_j^{\mathrm{sp}}\in\Gamma(E_j),\quad
 m_j=|t_j|^2,\quad q_j=|\nabla_{A_j}\Phi_j|^2,
 \quad \rho_*=4/3,\quad m_*=128/81.
\]

继承最新 `01_O10_Strong_Current.md` 中的结论：

\[
 \|\mathcal D_jt_j\|_{2,\mathrm{av}}\to0,
 \qquad \|m_j-m_*\|_{2,\mathrm{av}}\to0,
 \qquad \|q_j-4/9\|_{2,\mathrm{av}}\to0,
 \qquad\rho_j\to\rho_*\text{ in normalized measure}.
 \tag{H1}
\]

还继承同一实际解的曲率拟合：令

\[
 f_j=-iF_{A_j}^-,\quad Q_j^{\mathrm{sp}}=-i q_-(t_j),\quad
 S_j=m_*+2\rho_j^2q_j,\quad
 K_j=-\frac98\frac{\rho_j^3Q_j^{\mathrm{sp}}}{S_j}.
\]

则

\[
 |K_j|\le C,\qquad
 \|f_j-K_j\|_{2,\mathrm{av}}\to0,
 \qquad \|\operatorname{Ric}_{g_j}+g_j\|_{2,\mathrm{av}}\to0.
 \tag{H2}
\]

原稿 Clifford 规范是

\[
 c(q_-(t))t=\frac{|t|^2}{2}t.
 \tag{H3}
\]

这里没有增加 `W^-` 的界。后面需要有界总能量时会明确说明；若尾能量为无穷，相应必要下界自动成立。

---

## 2. 新的替代截面：不微分实际 Dirac 误差

### 命题 2.1：存在有界截面和有界 rough Laplacian 的同丛替代

在 (H1)–(H3) 下，存在光滑 `u_j in Gamma(E_j)`，满足

\[
 \|u_j\|_\infty+\|\nabla_j^*\nabla_j u_j\|_\infty\le C,
 \tag{2.1}
\]

以及

\[
 \|u_j-t_j\|_{2,\mathrm{av}}+
 \|\nabla_j(u_j-t_j)\|_{2,\mathrm{av}}\longrightarrow0.
 \tag{2.2}
\]

特别地，`|u_j|^2 -> m_*` 在归一化测度意义成立。`u_j` 不是另一个 SW 解，也不被宣称等于原来的三次扭率；它只作为同一丛的特征类测试截面使用。

### 证明

负手性 twisted Lichnerowicz 恒等式为

\[
 \mathcal D_j^*\mathcal D_j
 =\nabla_j^*\nabla_j-1+\frac32c(F_{A_j}^-).
\]

由 (H3) 及 K 的定义，点态有

\[
 \frac32c(iK_j)t_j=-\gamma_jt_j,
 \qquad\gamma_j=\frac{27}{32}\frac{\rho_j^3m_j}{S_j}.
 \tag{2.3}
\]

因为 `m_j <= 2 rho_j^2 q_j <= S_j`，所以 `0 <= gamma_j <= 27/4`。由 (H1)，

\[
 \gamma_j\longrightarrow1\text{ in measure}.
\]

置 `e_j=(3/2)c(F_{A_j}^- - iK_j)`，则 `||e_j||_{2,av}->0`，且

\[
 (\nabla_j^*\nabla_j-2)t_j
 =\mathcal D_j^*\mathcal D_jt_j+(\gamma_j-1)t_j-e_jt_j.
 \tag{2.4}
\]

取一个固定、光滑、纤维径向的截断 `T`，在 `|t|<=2` 上恒等，且 `|T(t)|<=4`。它由 Hermitian 范数定义，所以与丛的酉转移函数兼容。记 `z_j=T(t_j)`。由于 `m_*<4`、`m_j -> m_*` in L2av，

\[
 \|z_j-t_j\|_{2,\mathrm{av}}\longrightarrow0,
 \qquad \sup_j\|t_j\|_{4,\mathrm{av}}<\infty.
 \tag{2.5}
\]

在每个闭流形上精确求解

\[
 \boxed{(4+\nabla_j^*\nabla_j)u_j=6z_j.}
 \tag{2.6}
\]

正零阶项保证算子可逆；光滑性来自每个固定 j 上的椭圆理论。这里不需要几何一致的 Schauder 常数。点态最大值论证给

\[
 |u_j|\le6,\qquad
 |\nabla_j^*\nabla_j u_j|=|6z_j-4u_j|\le48.
\]

更具体地，在 `|u|^2` 的最大点，采用非负 rough Laplacian 的规范，

\[
 0\le\Delta|u|^2
 =2\operatorname{Re}\langle6z-4u,u\rangle-2|\nabla u|^2,
\]

从而 `4|u| <= 6|z|`（最大值非零时）。

令 `w_j=u_j-t_j`、`d_j=\mathcal D_jt_j`。由 (2.4)、(2.6)，

\[
 (4+\nabla_j^*\nabla_j)w_j
 =6(z_j-t_j)-\mathcal D_j^*d_j-(\gamma_j-1)t_j+e_jt_j.
 \tag{2.7}
\]

用 `w_j` 测试，在归一化体积下积分：

\[
 4\|w_j\|_2^2+\|\nabla_jw_j\|_2^2
 =6\langle z_j-t_j,w_j\rangle
 -\langle d_j,\mathcal D_jw_j\rangle
 -\langle(\gamma_j-1)t_j,w_j\rangle
 +\langle e_jt_j,w_j\rangle.
\]

此处及下一段的范数均为归一化范数。第一项用 (2.5) 和 Young；第二项用 `|D w| <= 2|nabla w|` 和 `||d_j||_2->0` 吸收。第三项趋零，因为

\[
 \|(\gamma_j-1)t_j\|_{4/3}
 \le\|\gamma_j-1\|_2\|t_j\|_4\to0.
\]

第四项满足

\[
 |\langle e_jt_j,w_j\rangle|
 \le\|e_j\|_2\|t_j\|_4\|w_j\|_4\to0.
\]

**这里的 `w_j` 的 L4 界不是由 Sobolev 得到：它直接来自 `u_j` 的点态界和 `t_j` 的已知 L4 界。** 因而没有偷加 Sobolev 或不塌缩条件。吸收得到 (2.2)。证毕。

---

## 3. 有界 rough-Laplacian 版本的慢梯度截断

这是对所给 R1 证明结构的扩展。原 R1 用 `Delta u=f(|u|^2)u`；此处只要求 `|u|+|Delta u|` 有界，不要求微分右端。

### 引理 3.1：梯度高幅度能量由连接曲率的高幅度能量控制

设 `E_j` 是闭四流形上的固定秩 Hermitian 丛，连接曲率为 `F_j`，且

\[
 |u_j|+|\nabla_j^*\nabla_j u_j|\le C_0,\qquad
 \operatorname{Ric}_{g_j}=R_{0,j}+r_j,\quad |R_{0,j}|\le C_0,\quad
 \|r_j\|_{2,\mathrm{av}}\to0.
 \tag{3.1}
\]

先假设 `sup_j fint |F_j|^2 < infinity`。定义

\[
 q=|\nabla u|^2,\quad H=\nabla^2u,\quad
 w_L=\left(\frac q{L^2+q}\right)^\epsilon.
\]

存在只依赖维数、秩与 `C_0` 的固定 `epsilon>0` 和常数 C，使对任意曲率截断值 `T>=1`，

\[
 \boxed{
 \fint w_L(|H|^2+q^2)
 \le C_T\,L^{-2\epsilon}
 +C\fint_{\{|F_j|>T\}}|F_j|^2
 +C\fint|r_j|^2.}
 \tag{3.2}
\]

`C_T` 可依赖总连接曲率平均的上界；**乘在尾部能量前的 C 不依赖 T 或这个总能量上界。** 这一区别用于后面的普适浓缩门槛。

### 证明

令 `h=\nabla^*\nabla u`，使用光滑权重

\[
 w_{L,\delta}=\left(\frac{q+\delta}{L^2+q+\delta}\right)^\epsilon,
 \qquad |dw|\sqrt q\le2\epsilon w|H|.
\]

设 `P_i=\nabla_i u`，`H_{ij}=\nabla_iP_j`。保留曲率作用的 Hessian 换指标恒等式：

\[
 \int w|H|^2=
 \int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
 +\frac12\int w\sum_{i,j}|F_{ij}u|^2.
 \tag{3.3}
\]

对交换项先积分掉一个导数，再交换 `\nabla_j\nabla_iP_j`。协向量槽的曲率只给 Ricci 收缩，丛槽给 `F*P`。出现的 `\nabla h` 项**再积分一次**，改写为 `\int w|h|^2` 以及 `dw*h*P`，因此不需要 `\nabla h` 或曲率导数。取 epsilon 充分小，权重项吸收到左边，得到

\[
 I:=\int w|H|^2
 \le C\int w|h|^2
 +C\int w(|\operatorname{Ric}|+|F|)q
 +C\int w|F|^2|u|^2.
 \tag{3.4}
\]

有界截面的加权插值来自
`div(w q Re< u,nabla u >)` 的积分：

\[
 J:=\int wq^2
 \le C\int wq+C\sqrt{IJ}
 \le C_1\left(I+\int wq\right).
 \tag{3.5}
\]

将 `F` 分成幅度不超过 T 的点态部分和尾部，将 Ricci 分成 `R_0+r`；这些分解不被微分，不需要它们光滑。对尾部与 q 的乘积用

\[
 \int w(|F|1_{|F|>T}+|r|)q
 \le aJ+C_a\int(|F|^2 1_{|F|>T}+|r|^2).
\]

先固定 `C_1`，再选 a 并吸收，得

\[
 I+J\le C_T\int w(1+q)
 +C\int(|F|^2 1_{|F|>T}+|r|^2).
 \tag{3.6}
\]

这里尾部系数 C 的选择不依赖 T。用 `w=1` 及

\[
 \int q=\int\operatorname{Re}\langle h,u\rangle\le C V
\]

先取得

\[
 \fint(|H|^2+q^2)\le C\left(1+\fint|F|^2+\fint|r|^2\right).
\]

再用 `w_{L,delta} <= L^{-2epsilon}(q+delta)^epsilon`、`0<epsilon<=1` 控制 (3.6) 中的加权低阶项。令 delta 降至零，得到 (3.2)。证毕。

### 推论 3.2：任意小体积集合上的集中控制

对满足 `Vol(Z_j)/V_j ->0` 的任意可测集合，定义

\[
 \mathfrak C_F:=\lim_{T\to\infty}\limsup_j
 \fint_{\{|F_j|>T\}}|F_j|^2.
\]

则

\[
 \boxed{
 \limsup_j\fint_{Z_j}|\nabla u_j|^4\le C\mathfrak C_F.}
 \tag{3.7}
\]

证明中先固定 T,L。低梯度集合的贡献不超过 `L^4 Vol(Z_j)/V_j`；高梯度集合上 `w_L>=2^{-epsilon}`。先令 j 趋无穷，再令 L 趋无穷，最后令 T 趋无穷。此极限顺序消除 `C_T`，而保留 T 无关的尾部系数。特别地，连接曲率平方的一致可积性推出这些小集合上的梯度四次能量趋零。

---

## 4. 同丛特征类：把未估计的实际扭率通量换成可控制的测试

### 命题 4.1：几乎定长的有界替代截面只能在曲率尾部承载第二 Chern 类

在引理 3.1 的条件下，设丛为复秩二，且

\[
 |u_j|^2\longrightarrow m_*>0\text{ in normalized measure}.
\]

则

\[
 \boxed{
 \limsup_j\frac{|c_2(E_j)[M_j]|}{V_j}
 \le C\mathfrak C_F.}
 \tag{4.1}
\]

### 证明

固定 `0<a<b<m_*`，取光滑标量 cutoff `chi`，在 `[0,a]` 上为1，在 `[b,infinity)` 上为0。令

\[
 Z_j=\{|u_j|^2\le b\},\qquad \operatorname{Vol}(Z_j)/V_j\to0.
\]

在 `u_j !=0` 区域设 `n_j=u_j/|u_j|`。用酉连接修正使 `n_j` 平行，得到分裂为平凡复线与复线的连接 `nabla^0`，其 `c_2(F^0)=0`。连接差 C 满足

\[
 |C|\le C|\nabla n_j|,\quad
 |F^t|\le C(|F_j|+|\nabla n_j|^2),
\]

于是通常的 Chern–Weil transgression 形式满足

\[
 dT_{n_j}=c_2(F_j),\qquad
 |T_{n_j}|\le C\left(|F_j||\nabla n_j|+|\nabla n_j|^3\right).
 \tag{4.2}
\]

这是原整合稿已经使用的单位截面 transgression 构造，现用于 E 而非仅 S+。`(1-chi(|u_j|^2))T_{n_j}` 在零点附近恒零，可光滑延拓。Stokes 给出

\[
 c_2(E_j)[M_j]
 =\int\chi(|u_j|^2)c_2(F_j)
 +\int d\chi(|u_j|^2)\wedge T_{n_j}.
 \tag{4.3}
\]

在过渡区 `a<=|u_j|^2<=b`，所有分母一致离零；`|u_j|` 有界。因此

\[
 \frac{|c_2(E_j)[M_j]|}{V_j}
 \le C\fint_{Z_j}\left(|F_j|^2+|\nabla u_j|^4\right).
 \tag{4.4}
\]

曲率项可按任意固定 T 分成 `T^2 Vol(Z_j)/V_j` 与尾部。梯度项由 (3.7) 控制，得到 (4.1)。没有假定零点横截，也没有把实际三次扭率的四次导数估计偷偷代入。证毕。

---

## 5. O10 的必要结论：一个普适正量的反自对偶 Weyl 集中

定义

\[
 \mathfrak C_-:=\lim_{T\to\infty}\limsup_j
 \frac1{V_j}\int_{\{|W^-_{g_j}|>T\}}|W^-_{g_j}|^2\,dV_j.
 \tag{5.1}
\]

幅度与范数都用 O10 的 `s=-4` 规范。这个量不是某个任选局部气泡的能量；它在原闭流形上计量，自动除以原总体积。

### 定理 5.1

在 (H1)–(H3) 及原 O10 拓扑输入下，存在普适 `epsilon_W>0`，使任意假想零端序列满足

\[
 \boxed{\mathfrak C_-\ge\epsilon_W>0.}
 \tag{5.2}
\]

因此 `|W^-|^2` 一致可积的 O10 零端序列不存在。

### 证明

在 `E_j=S^-_j\otimes L_j` 上，曲率分解写成

\[
 F^{E_j}=F_{0,j}+\mathscr L(W^-_{g_j})+\mathcal E_j,
 \qquad |F_{0,j}|\le C,
 \qquad\|\mathcal E_j\|_{2,\mathrm{av}}\to0.
 \tag{5.3}
\]

这里 `F_0` 保留标量块、实际有界 `F_A^+` 和有界 `F_A^-` 模型。`mathscr L` 是四维固定的曲率表示映射。错误项包含无迹 Ricci 块及 `F_A^- - iK`，均由原实际预算控制。这只是 Levi-Civita 手性曲率分解；不对模型求导。

若 `mathfrak C_-` 有限，则对某一固定 T，尾部 limsup 有限，因而 `sup_j fint |W^-|^2`（去掉有限多个指标后）有限。由 (5.3)，引理3.1对命题2.1的 u_j 可用。若 `mathfrak C_-` 为无穷，(5.2)自动成立。

点态由 (5.3) 可证明，对充分大 T，

\[
 \fint_{\{|F^{E_j}|>T\}}|F^{E_j}|^2
 \le C\fint_{\{|W^-|>T/C\}}|W^-|^2
       +C\fint|\mathcal E_j|^2.
\]

因而 `mathfrak C_{F^E}<=C mathfrak C_-`，其中 C 不依赖 Euler 密度上界。由命题4.1，

\[
 \limsup_j\frac{|c_2(E_j)[M_j]|}{V_j}
 \le C_*\mathfrak C_-.
 \tag{5.4}
\]

另一方面，原稿的特征数恒等式为

\[
 c_2(E_j)[M_j]
 =5\chi(M_j)+6\operatorname{sign}(M_j)
 +\frac94(a_j^2-T_{+,j}).
 \tag{5.5}
\]

Chern–Gauss–Bonnet 与 signature 给

\[
 \frac{8\pi^2(5\chi+6\operatorname{sign})}{V}
 =9\fint|W^+|^2+\fint|W^-|^2
       +\frac{10}{3}-\frac52\fint|\operatorname{Ric}^\circ|^2.
\]

由于 `a_j^2>=T_{+,j}`，

\[
 \liminf_j\frac{c_2(E_j)[M_j]}{V_j}
 \ge d_*:=\frac{5}{12\pi^2}>0.
 \tag{5.6}
\]

(5.4)–(5.6) 给出 `mathfrak C_- >= d_*/C_*`。例如取

\[
 \epsilon_W:=\frac{d_*}{2C_*}>0
\]

即可得到 (5.2)。所有进入尾部系数 `C_*` 的常数，只依赖维数、秩、固定幅度及 cutoff，故门槛是普适的。没有计算或声称它的最佳值。证毕。

### 解释

最新 R2 使实际扭率接近一个非零常长度，并接近一个粗 Laplacian 特征截面。我们利用它构造同丛的有界 u_j。**若相反手性曲率不集中，则 u_j 的小值区不能承载正密度的 c2。** 而原拓扑与曲率恒等式强迫 c2 有正密度。因此高幅度 W- 集中是逃逸不可缺少的结构。

这里没有重新加入原有有符号恒等式中已经相消的 `20V/3`，也没有证明旧的平方差本身为正。使用的是同一丛的独立 Chern-class 测试，依赖关系完全展开在上文。

---

## 6. 真正扩大 O10 范围：包含临界 3/8，并越过它一个普适正量

原稿已经证明：若 `chi(M_j)/A_j<=B`，则沿零端序列

\[
 \limsup_j\fint|W^-|^2\le\frac{16B}{9}-\frac23.
 \tag{6.1}
\]

原来仅由非负性只能排除 `B<3/8`。现在用定理5.1，

\[
 \epsilon_W\le\mathfrak C_-
 \le\limsup_j\fint|W^-|^2
 \le\frac{16B}{9}-\frac23.
 \tag{6.2}
\]

取

\[
 \boxed{\delta_{\rm top}=\frac9{32}\epsilon_W>0.}
 \tag{6.3}
\]

若 `B<=3/8+delta_top`，(6.2)右端不超过 `epsilon_W/2`，矛盾。

### 推论 6.1：全参数版本

在原实际供给、`p>=A>0`、`a^2>=T_+` 及

\[
 \frac{\chi(M)}A\le\frac38+\delta_{\rm top}
\]

下，存在正的统一 c，使

\[
 \boxed{\fint|\operatorname{Ric}+g|^2+D_\beta/V
 \ge c\frac{(\beta-2)^2}{\beta^2},\qquad\beta\ge2.}
 \tag{6.4}
\]

**证明全参数与原度量范围。** 若不存在 c，可选比值趋零的序列。对于 beta 在任意固定紧区间内且 beta>2，既有有限参数估计排除该比值趋零；beta=2的目标右端为零。因此 beta 必须趋无穷，且 kappa 趋零。由原稿的精确共形比较，转成 `s=-4` 的零端序列，类平方、p、A和chi/A不变。定理5.1与(6.1)排除它。证毕。

这将此前的严格低密度范围扩展到临界点及一个正邻域。**不是证明任意B的完整O10。** 在更大的B范围，(6.2)允许足够多的相反手性集中，仍需更强的集中限制或真实闭流形构造。

原O11平衡族在充分大指标本来已经满足 `chi/A<1/3`，所以不能把本文新阈值当作首次解决该族端点。新增范围是临界 `3/8` 及其正邻域；新增机制是实际场到同丛辅助截面的转移和曲率尾部的拓扑检测。

---

## 7. O11：本轮不重复登记已经取得的 R3

已读取 `02_O11_Variational_Selection.md` 的完整证明。其高精度近极小选择与临界预算测试给出弱驻点和弱稳定性，但没有给出次阈值几何必有下降方向。本文没有补出所缺的统一符号，因此没有获得 O11 新的最优系数结论。

目前应保留的最短条件是：对所选真正近极小序列，若

\[
 P(g_j)\le8\pi^2(1-\epsilon)Q_j,
\]

是否能够从实际场与变分方程构造允许的 H_j，使

\[
 |DP_{g_j}[H_j]|\ge c_\epsilon Q_j
 \quad\text{或}\quad
 D^2P_{g_j}[H_j,H_j]\le-c_\epsilon Q_j?
\]

这依然没有证明。也没有实际找到低于4的恢复序列。本文的 O10 辅助截面不能不经额外推导就当作 O11 的下降张量；后者还要求正确符号及 Q 尺度，而不是只要求测试张量可构造。

普通 O11 手术族的完整单极子凸包/period-minimax预算等于A，已经由最新报告证明；不能再次把寻找遗漏普通单极子类作为关闭O11的纯预算路径。另一BF连通和族的完整预算仍单独保留。

---

## 8. 来源、接入位置和独立性边界

- `01_O10_Strong_Current.md` §§2–3：同一个实际解的有界ASD拟合、R2强Dirac/幅度/梯度结论、Lichnerowicz规范。
- `20260929_Line1_Integrated_Manuscript.tex`，`proof:mixed-current:s3`：`c(q_-(t))t=(|t|^2/2)t`。
- 同稿 `proof:actual-topological:e4.7`–`e4.8`：单位截面的Chern transgression与cutoff Stokes式。
- 同稿 `proof:actual-topological:e5.1`–`e5.2`：负手性扭率丛的c2与曲率下界。
- 同稿 `proof:quartic-flux:e3.4`：`16B/9-2/3` 的相反Weyl能量密度上界。
- 同稿 `proof:single-parameter:e1.4`：O10原度量与负Yamabe代表的比较。
- `02_O11_Variational_Selection.md`：继承R3，不作为本轮新发现。

本轮新增的是 §§2–6 的完整推导。关键可核验点：

1. resolvent比较不微分 Dirac 误差；它在能量对偶中处理。
2. L4控制来自有界u和已知t的L4，不使用Sobolev。
3. 有界rough Laplacian版本通过第二次分部积分消去其右端导数。
4. 梯度尾部估计中的系数不依赖曲率截断值或总曲率上界；这些依赖只在先被极限消去的项中出现。
5. Chern测试使用同一个丛但允许不同截面，不冒称辅助截面仍满足原SW方程。
6. 仅得到普适正量的高幅度Weyl集中，不得到其不可能性；所以一般O10保持开放。
7. 有限代数检查只能核对Clifford系数、极限常数及密度阈值，不能替代上述PDE估计。
