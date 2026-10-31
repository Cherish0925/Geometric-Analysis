# O10：第五行列式幂线丛的强制性与任意有限 Euler 密度

日期：2026-09-29。续研 C。底本为 `20260929_Line1_Integrated_Manuscript.tex`；直接前置为续研 B 的强流、同丛 resolvent 与第一延拓。本文不改写原稿，不重新定义第一科学主线。

## 0. 结论、依赖及边界

**本补充的主结论。** 假定原稿及续研 B 明确陈述的实际单解估计、强流升级和第一延拓成立，则不存在满足全部原 O10 实际输入且
\[
 s_j=-4,\quad\beta_j\to\infty,\quad
 \kappa_j=\frac{P_j+D_{\beta_j}}{V_j}\to0,\quad
 \sup_j\fint_{M_j}|W_j^-|^2<\infty
 \tag{C.0}
\]
的闭流形序列。这里及下文所有均值均除以总量 \(V_j\)，即使积分在子集上进行。

因此，对**每一个固定有限的** \(B\ge0\)，在原实际共形单极子供给、\(p\ge A>0\)、\(a^2\ge T_+\) 与 \(\chi(M)/A\le B\) 下，存在 \(c(B)>0\)，使所有原允许度量与所有 \(\beta\ge2\) 满足
\[
 \boxed{\fint_M|\operatorname{Ric}+g|^2+\frac{D_\beta}{V}
 \ge c(B)\frac{(\beta-2)^2}{\beta^2}.}
 \tag{C.1}
\]
这把有限密度子问题从一个固定阈值扩展到任意有限阈值；不要求点态曲率、直径、非塌缩或 Sobolev 常数的界。

**不宣称的结论。** 本文没有给出与 \(B\) 无关的正数 \(c\)。因此，完全删除 Euler 密度控制的 O10 仍未解决。O11 的最优首项也没有在本文中决定。本文逐步证明的是上述直接前置到 (C.0) 不可能、再到 (C.1) 的连接；不是对整份整合稿所有上游定理的重新认证，也不主张已完成全球原创性核查。

**新的连接。** 第一延拓之后唯一剩余的扭率导数，不必再次视为一个行列式为 \(L^9\) 的正旋量。将它与原正旋量作外积，会得到原行列式线丛的第五幂 \(L^5\) 的截面。它同时具有非消失质量、一个弱反 Cauchy–Riemann 约束，以及由原实际曲率强迫的正零阶项 \(10/3\)。用同线丛正 resolvent 作对偶测试即可矛盾，不需要计算高曲率泡的锐利陈类收费常数。

---

## 1. 固定范数和直接前置

记 \(L=\det S^+\)、\(E=S^-\otimes L\)，故 \(\det E=L^3\)。\(A\) 是 \(L\) 的实际 unitary 联络。为避免拓扑预算同名，局部写 \(A=i\mathfrak a\)，\(\mathfrak a\) 为实一形式；其曲率为 \(i\,d\mathfrak a\)。线丛 \(L^k\) 的导数记 \(D_k\)，局部为 \(d+ki\mathfrak a\)。所有 rough Laplacian 取 \(\nabla^*\nabla\ge0\)。Hermitian 内积对第一变量共轭线性，最后取实部。

二形式采用算子／外代数规范，\(|e^{12}\pm e^{34}|^2=2\)。实际负手性二次映射满足
\[
 c(q_-(z))z=\frac{|z|^2}{2}z,\qquad |q_-(z)|^2=\frac{|z|^4}{8}.
\]

假设存在 (C.0)。原共形归约及同解估计提供
\[
 D_A\Phi=0,\quad F_A^+=2i\sigma(\Phi),\quad
 \rho=|\Phi|^2\le2,\qquad \rho_* =4/3,
\]
\[
 \tau=t_\Phi\in\Gamma(E),\quad m_*=128/81,
 \quad |\tau|^2\to m_*\text{ in }L^2_{\rm av},
 \quad D^-_{3A}\tau\to0\text{ in }L^2_{\rm av}.
\]
正旋量具有 \(\nabla\Phi\) 的归一化 \(L^4\) 一致可积性及 \(\nabla^2\Phi\) 的归一化 \(L^2\) 界，且
\[
 \rho\to\rho_*,\quad \nabla\zeta\to0,\quad
 \zeta=\langle\Phi,\nabla_A\Phi\rangle\to0,
 \quad N_\tau=(\nabla\tau)^{1,0}_{J_+}\to0.
 \tag{1.1}
\]
这里所用小量均取其已证的归一化 \(L^2\) 范数；\(\zeta\) 另由一致可积性趋零于 \(L^4\)。

续研 B 的有界截断与同丛 resolvent 给出 \(v\in\Gamma(E)\)，满足
\[
 |v|+|\nabla^*\nabla v|\le C,
 \quad v-\tau\to0\text{ in }H^1_{\rm av}\cap L^4_{\rm av},
\]
\[
 D^-_{3A}v\to0,\quad
 (\nabla^*\nabla-2)v\to0\text{ in }L^2_{\rm av},\quad
 m:=|v|^2\to m_*\text{ in }L^2_{\rm av}.
 \tag{1.2}
\]
由 (C.0) 的有限平均 \(W^-\) 预算和已证 Hessian 交换，
\[
 \|\nabla v\|_{4,\rm av}+\|\nabla^2v\|_{2,\rm av}\le C_K,
 \qquad \fint|\nabla v|^2\to2m_*.
 \tag{1.3}
\]
其中 \(K=\sup_j\fint |W^-|^2<\infty\)。另有
\[
 dm\to0,\qquad j_v:=\operatorname{Im}\langle v,\nabla v\rangle\to0
 \quad\text{in }L^2_{\rm av}.
 \tag{1.4}
\]

**第一延拓是本文必需的直接输入。** 在 \(\rho,m\) 远离零的集合上，取后述适配局部标架。记
\(Z_1=e_1-ie_2\)、\(Z_2=e_3-ie_4\)。续研 B 的 `O10_Resolvent_Prolongation.md` §§2–4 证明
\[
 \nabla_{Z_1}v,\quad \nabla_{Z_2}v,\quad
 \nabla_{\bar Z_1}v\to0\quad\text{in }L^2_{\rm av};
 \tag{1.5}
\]
Dirac 迹再使 \((\nabla_{\bar Z_2}v)_1\to0\)。只有 \((\nabla_{\bar Z_2}v)_2\) 未被消去。第一延拓仅用有限 \(K\) 的导数预算，并不使用 \(K\le50/3\) 或临界谱等号。

低 \(\rho\)、低 \(m\) 集合的相对体积趋零。由 (1.3)，这些集合上的 \(\nabla v\) 二次能量为 \(o(V)\)。以后所有适配标架计算先作固定幅度截断，再延拓为全局张量；不假设存在全局标架。

同一实际曲率拟合还给出
\[
 f:=-iF_A^-=-\frac{27}{32}Q_v+o_{L^2_{\rm av}}(1),
 \qquad Q_v=-iq_-(v).
 \tag{1.6}
\]
这是原有 \(f-K_{\rm fit}\to0\)、\(K_{\rm fit}=-(9/8)\rho^3Q_\tau/S\)，以及 \(v-\tau\to0\) 于 \(L^4\) 的直接结果；极限系数为
\((9/8)\rho_*^3/(2m_*)=27/32\)。不求这个拟合模型的导数。

---

## 2. 剩余导数的真实载体是线丛 \(L^5\)

### 2.1 适配标架和误差

在 \(\rho,m>0\) 上，选适配 Spin\(^c\) 和正交标架，使
\[
 \Phi=\sqrt\rho\,(1,0),\qquad v=\sqrt m\,(1,0).
\]
用
\[
 \theta_1=e^1-ie^2,\qquad \theta_2=e^3-ie^4
\]
记复一形式。正、负扭曲旋量联络可写为
\[
 \Omega_+=\begin{pmatrix}ip&-\bar\eta\\\eta&i(\mathfrak a-p)\end{pmatrix},
 \qquad
 \Omega_E=\begin{pmatrix}iq&-\bar b\\b&i(3\mathfrak a-q)\end{pmatrix},
 \tag{2.1}
\]
其中 \(p=\operatorname{Im}\zeta/\rho\)、\(q=j_v/m\) 是实相位流，不是单极子投影平方。

实际三次式、\(v-\tau\to0\) 及小流给
\[
 \eta=\kappa\theta_1+\epsilon_\eta,
 \qquad \kappa=\frac{\sqrt m}{2\rho^{3/2}}\in\mathbb R,
 \quad \epsilon_\eta\to0\text{ in }L^2_{\rm av}.
 \tag{2.2}
\]
第一延拓给
\[
 b=c\theta_2+\epsilon_b,\qquad
 c=\frac{b_3+ib_4}{2},\qquad \epsilon_b\to0\text{ in }L^2_{\rm av}.
 \tag{2.3}
\]
在任一固定下幅度截断上，所有 \(p,q,\eta,b,c,\epsilon_\eta,\epsilon_b\) 具有归一化 \(L^4\) 界，且 \(p,q\to0\) 于 \(L^2\)。这些界来自 \(\nabla\Phi,\nabla v\) 的界，不涉及裸的局部势 \(\mathfrak a\) 的界。

### 2.2 不依赖标架的定义

对 \(v\in E\)，定义其三次表达式
\[
 t(v)=\sum_{i=1}^4 c^-(e^i)v\otimes(v\wedge\nabla_i v)
       \in\Gamma(S^+\otimes L^4).
\]
因此
\[
 \Phi\wedge t(v)\in\Gamma(L^5).
\]
在上述标架和稿件 Clifford 规范下，
\[
 t(v)=m^{3/2}(-b_1+ib_2,-b_3-ib_4),
\]
所以
\[
 c_0=-\frac{\Phi\wedge t(v)}{2\sqrt\rho\,m^{3/2}}
 \tag{2.4}
\]
的局部系数正好是 (2.3) 中的 \(c\)。

选固定光滑截断 \(\chi_\rho,\chi_m\)，在零附近为零，在 \(\rho_*\)、\(m_*\) 的固定邻域内为一；其导数支撑与这两个极限幅度保持正距离。定义
\[
 c_j=\chi_\rho(\rho_j)\chi_m(m_j)c_{0,j}\in\Gamma(L_j^5),
 \tag{2.5}
\]
并在截断为零的地方光滑延拓。以下全局 \(c\) 始终指 (2.5)。

若局部行列式标架变为 \(e^{it}\) 倍，\(c_0\) 的系数变为 \(e^{-5it}c_0\)，\(\theta_2\) 变为 \(e^{2it}\theta_2\)，\(b\) 变为 \(e^{-3it}b\)。因此 (2.3) 与线丛连接 \(D_5=d+5i\mathfrak a\) 相容。这也由全局外积定义 (2.4) 保证。

### 2.3 导数预算和非消失质量

对截断区间，直接对 (2.4) 求协变导数，有
\[
 |c|\le C|\nabla v|,
\]
\[
 |D_5c|\le C\left(|\nabla^2v|+|\nabla v|^2
                         +|\nabla\Phi|\,|\nabla v|\right).
 \tag{2.6}
\]
截断导数属于右侧同一类型。因此
\[
 \|c_j\|_{4,\rm av}+\|D_5c_j\|_{2,\rm av}\le C_K.
 \tag{2.7}
\]

更重要的是
\[
 \boxed{\fint|c_j|^2\longrightarrow1.}
 \tag{2.8}
\]
证明：在好幅度区，
\[
 |\nabla v|^2=\frac{|dm|^2}{4m}+m|q|^2+m|b|^2.
\]
前两项为 \(o(V)\)；(2.3) 给 \(|b|^2=2|c_0|^2+o_{L^1_{\rm av}}(1)\)。由于 \(m-m_*\to0\) 于 \(L^2\)、\(|b|^2\) 在 \(L^2\) 中有界，可以将乘子 \(m\) 替换为 \(m_*\)。坏幅度区的梯度二次能量由 (1.3) 为 \(o(V)\)。结合 \(\fint|\nabla v|^2\to2m_*\) 即得 (2.8)。这个步骤不要求 \(|\nabla v|^4\) 一致可积，只要求其有界。

---

## 3. 连接剩余分量：带两条相位流的精确 Cartan 计算

采用原稿 \(S^+\to S^-\) Clifford 矩阵
\[
 C_1=I,\quad C_2=\operatorname{diag}(i,-i),\quad
 C_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C_4=\begin{pmatrix}0&-i\\-i&0\end{pmatrix};
\]
反向矩阵是 \(-C_i^*\)。LC 的两手性 traceless 连接分别从 (2.1) 去掉 \(i\mathfrak a I/2\)、\(3i\mathfrak a I/2\)。由
\[
 \Omega_{-,\mathrm{LC}}C_j-C_j\Omega_{+,\mathrm{LC}}
       =\sum_i\Gamma^i{}_j C_i,
 \qquad de^i=-\Gamma^i{}_j\wedge e^j
\]
得到：当 \(\eta=\kappa\theta_1\)、\(b=c\theta_2\) 时，
\[
 \boxed{d\theta_2=i(2\mathfrak a-p-q)\wedge\theta_2
                    -\bar c\,\Xi_-,}
 \tag{3.1}
\]
其中
\[
 \Xi_-=e^{13}+e^{24}+i(e^{14}-e^{23}),\qquad (\Xi_-)^+=0.
\]
系数 \(\kappa\) 在此式中抵消，不对其求导。对真实的 (2.2)–(2.3)，同一线性 Cartan 计算给
\[
 d_{-2A}\theta_2=-i(p+q)\wedge\theta_2-\bar c_0\Xi_-+\mathcal R,
 \quad |\mathcal R|\le C(|\epsilon_\eta|+|\epsilon_b|).
 \tag{3.2}
\]
这里只是连接的一阶代数关系，不涉及曲率求导。

另一方面，\(E\) 的 off-diagonal 曲率为
\[
 (F^E)_{21}=db+i(3\mathfrak a-2q)\wedge b.
\]
代入 (2.3)、(3.2)，得到
\[
 \begin{aligned}
 (F^E)_{21}={}&D_5c_0\wedge\theta_2-|c_0|^2\Xi_-
       +(d_{3A}\epsilon_b)\\
 &-i(p+3q)\wedge c_0\theta_2
       -2iq\wedge\epsilon_b+c_0\mathcal R.
 \end{aligned}
 \tag{3.3}
\]
取相对于原取向的正自对偶部分。\(|c_0|^2\Xi_-\) **精确消失**。而 \(((F^E)_{21})^+\) 的中心部分是对角的，非中心部分来自 LC 的 Ricci off-diagonal 块，故
\[
 |((F^E)_{21})^+|\le C|\operatorname{Ric}^{\circ}|.
\]
记
\[
 a_0\mapsto\mathcal L(a_0):=(a_0\wedge\theta_2)^+.
\]
于是 (3.3) 给出
\[
 \mathcal L(D_5c_0)=-(d_{3A}\epsilon_b)^++G_j,
 \qquad \|G_j\|_{4/3,\rm av}\to0.
 \tag{3.4}
\]
例如 \(pc_0,qc_0\) 由小 \(L^2\) 乘有界 \(L^4\) 控制，\(c_0\mathcal R\) 同样；Ricci 项甚至在 \(L^2\) 中趋零。没有删除 \(W^-\)：它根本不进入这一 off-diagonal 自对偶曲率方程。

---

## 4. 把局部 CR 约束变成全局弱测试

令 \(J_-\) 的基本形式为 \(\Omega_-=e^{12}-e^{34}\)，并在一形式上约定
\((J_-\alpha)(X)=-\alpha(J_-X)\)。

对 \(\alpha=\sum\alpha_i e^i\)，\(\mathcal L(\alpha)=0\) 等价于
\[
 \alpha_1+i\alpha_2=0,\qquad\alpha_3-i\alpha_4=0.
\]
它控制的是此 \(J_-\) 的反全纯导数，不是原 \(J_+\) 的同一个方向。

为准确保留权重，取 \(\Psi_1=e^{12}+e^{34}\)、\(\Psi_2=e^{13}-e^{24}\)、\(\Psi_3=e^{14}+e^{23}\)，各自范数平方为 2。\(\mathcal L\) 的坐标为
\[
 \frac12\bigl(-i\alpha_3-\alpha_4,\ \alpha_1+i\alpha_2,
                                      -i\alpha_1+\alpha_2\bigr).
\]
在这个正自对偶三维目标中令 \(\mathcal D=\operatorname{diag}(2,1,1)\)。则精确 Hermitian 符号恒等式为
\[
 \boxed{\mathcal L^*\mathcal D\mathcal L=I-iJ_-.}
 \tag{4.1}
\]
这是一个由实际 \(\Phi,v\) 决定的有界 bundle map；在固定下幅度区，其协变一阶导数由 \(C(|\nabla\Phi|+|\nabla v|)\) 控制。

**弱测试结论。** 对任意光滑 \(w_j\in\Gamma(L_j^5)\)，若
\[
 \|w_j\|_\infty+\|D_5w_j\|_{4,\rm av}
                      +\|D_5^2w_j\|_{2,\rm av}\le C_w,
 \tag{4.2}
\]
则
\[
 \Re\fint\langle D_5c_j-i\bar J_jD_5c_j,D_5w_j\rangle\to0.
 \tag{4.3}
\]
这里使用全局光滑有界的二形式及其 skew map
\[
 \bar\Omega_j=-\frac4{m_*}Q_{v_j},\qquad
 (\bar J_j\alpha)(X)=-\alpha(\bar J_jX).
 \tag{4.4}
\]
\(\bar J_j\) 不必处处平方等于 \(-I\)，也不必是一个新的 almost-complex 结构。它只在后续积分恒等式中作为 skew tensor 使用。

证明 (4.3) 的所有项如下。

1. 在固定幅度截断内，以 \(\mathcal D\mathcal L(D_5w)\) 测试 (3.4)，并用 (4.1)。\(G_j\) 与 \(D_5w\) 的配对由 \(L^{4/3}\)-\(L^4\) 为 \(o(1)\)。
2. 将 \(d_{3A}\epsilon_b\) 的导数转到测试上。其 adjoint 由
\[
 C\bigl(|D_5^2w|+(|\nabla\Phi|+|\nabla v|+|d\chi|)|D_5w|\bigr)
\]
控制，因而在 \(L^2_{\rm av}\) 中有界；与 \(\epsilon_b\to0\) 的 \(L^2\) 配对为 \(o(1)\)。这里使用 unitary 的自然 bundle covariant derivatives，局部 \(\mathfrak a\) 项相互匹配，不要求 gauge 势的额外界。
3. 将 \(c_0\) 换成截断 \(c_j\)，出现 \(c_0d\chi\)。其支撑相对体积趋零；\(c_0,d\chi\) 均 \(L^4\) 有界，所以该项 \(L^2\) 有界并在 \(L^{4/3}\) 中趋零。可以采用两个嵌套的固定下幅度截断，使每个局部计算及测试在零幅度之前光滑为零。
4. 在好幅度区，\(Q_v=-m\Omega_-/4\)，故 \(\bar J=(m/m_*)J_-\)。\(m\) 有界并趋于 \(m_*\)，所以 \(\bar J-J_-\to0\) 于 \(L^4\)。用 (2.7) 及 (4.2)，更换 \(J_-\) 的误差为 \(o(1)\)。

这些步骤只用一阶结构误差的小 \(L^2\)、两个 \(L^4\) 因子的乘积，以及测试的二阶 \(L^2\)。没有给 \(\epsilon_b\) 的导数假定强收敛，也没有把 \(H^{-1}\) 残差升级成未经证明的强 \(L^2\) 方程。

---

## 5. 同线丛 Bochner 配对给出确定的正势

由 Hopf 散度式与 (1.2)、(1.4)，
\[
 \delta\bar\Omega\to0\quad\text{in }L^2_{\rm av}.
 \tag{5.1}
\]
线丛 \(L^5\) 的曲率是 \(F^{L^5}=5F_A\)。由 (1.6)、\(|Q_v|^2=m^2/8\)，
\[
 \begin{aligned}
 \mathfrak q_j&:=-i\langle F^{L^5},\bar\Omega\rangle
       =5\langle f,\bar\Omega\rangle\\
 &\longrightarrow
 5\frac{27}{32}\frac4{m_*}\frac{m_*^2}{8}
   =\frac{135m_*}{64}=\frac{10}{3}
 \quad\text{in }L^2_{\rm av}.
 \end{aligned}
 \tag{5.2}
\]
这里正手性 \(F_A^+\) 与 \(\bar\Omega\) 正交。符号由原负手性 Clifford 约定决定，不与第二次三次旋量的 \(-7\) Lichnerowicz 势混同。

对任意全局二形式 \(\Omega\)、同线丛截面 \(c,w\)，直接分部积分及线丛曲率交换给
\[
 \begin{aligned}
 &\Re\int\langle D_5c-iJ_\Omega D_5c,D_5w\rangle\\
 &=\Re\int\left\langle c,\,
    \Delta_{5A}w-i\langle F^{L^5},\Omega\rangle w
                         +i\,\delta\Omega\cdot D_5w\right\rangle.
 \end{aligned}
 \tag{5.3}
\]
不需要 \(\Omega\) 闭，也不需要 \(J_\Omega^2=-I\)。在正交标架上，skew 项是
\(i\Omega_{ij}\overline{D_i c}D_jw\)；换导数产生
\(-i\langle F^{L^5},\Omega\rangle\)，其余是 \(i\delta\Omega\cdot Dw\)。

把 (5.1)、(5.2) 代入 (5.3)。势误差与 \(c\)、有界 \(w\) 用 \(L^2\)-\(L^2\) 配对；漂移误差用
\(\|\delta\bar\Omega\|_2\|c\|_4\|D_5w\|_4\)。结合 (4.3)，得到
\[
 \boxed{\Re\fint\langle c_j,(\Delta_{5A}+10/3)w_j\rangle\to0}
 \tag{5.4}
\]
对所有 (4.2) 的测试成立。

这不是 \(c_j\) 的强二阶方程；它是一个足够用来做以下同线丛 resolvent 对偶测试的弱结论。

---

## 6. 一个合法的对偶测试消去全部剩余质量

固定大数 \(M\)，取光滑径向截断 \(T_M\)，在 \(|c|\le M\) 上 \(T_M(c)=c\)，全局 \(|T_M(c)|\le2M\)，且
\[
 \Re\langle c,T_M(c)\rangle\ge0.
\]
在 \(L^5\) 上解
\[
 \boxed{(\Delta_{5A}+10/3)w_j=T_M(c_j).}
 \tag{6.1}
\]
正势给可逆性和 \(\|w_j\|_\infty\le3(2M)/10\)，继而 \(\Delta_{5A}w_j\) 有界。

本测试的连接曲率只有 \(5F_A\)，没有 \(W^-\) 块。原实际拟合使它成为有界模型加归一化 \(L^2\) 小误差，Ricci 同样如此。因而已证的有界强迫项 Hessian／有界截面插值给
\[
 \|D_5^2w_j\|_{2,\rm av}+\|D_5w_j\|_{4,\rm av}\le C_M.
\]
这正好验证 (4.2)，不是预设它。证明不需要 \(T_M(c_j)\) 的导数，也不需要 \(w_j\) 的 \(L^\infty\) 梯度界。

由 (5.4)、(6.1)，
\[
 \Re\fint\langle c_j,T_M(c_j)\rangle\longrightarrow0.
 \tag{6.2}
\]
另一方面，(2.7)–(2.8) 给
\[
 \liminf_j\Re\fint\langle c_j,T_M(c_j)\rangle
 \ge 1-\limsup_j\fint_{\{|c_j|>M\}}|c_j|^2
 \ge1-\frac{C_K}{M^2}.
 \tag{6.3}
\]
先固定足够大的 \(M\)，使右端至少 \(1/2\)，与 (6.2) 矛盾。

**这排除了 (C.0)。**关键是测试在 \(L^5\) 上，其连接曲率受原实际行列式预算控制；无需把相反 Weyl 集中的陈类系数优化到锐值。

---

## 7. 从序列排除到每一个有限密度范围的统一估计

固定 \(B<\infty\)。若 (C.1) 不成立，取一列原输入，使
\[
 \frac{\kappa_{\beta_j}}{(\beta_j-2)^2/\beta_j^2}\to0.
\]
\(\beta=2\) 处右侧为零，无需纳入这条反证子列。已有有限参数估计排除任何有界 \(\beta_j\) 子列，因此 \(\beta_j\to\infty\)、\(\kappa_{\beta_j}\to0\)。

已有精确共形比较
\[
 \widehat\kappa\le
 \frac{\kappa}{1-\sqrt\kappa-\kappa/16}
\]
允许换成 \(s=-4\)；原实际输入、\(A,p,a^2\) 和 \(\chi/A\) 被相应保留。

在这些代表上，标量预算给 \(p/V\le1/(2\pi^2)\)。Gauss–Bonnet 给
\[
 \fint|W^-|^2
 \le \frac{8\pi^2\chi}{V}-\frac23+\frac{P}{2V}
 \le4B-\frac23+o(1).
\]
也可使用端点更锐的 \(16B/9-2/3+o(1)\)，但此处只需要有限性。故得到 (C.0)，与第6节矛盾。这证明对每个固定有限 \(B\) 的 \(c(B)>0\)。

**无界版本的准确剩余状态。** 若完全不控制 \(\chi/A\) 的 O10 仍有逃逸序列，则本文强迫
\[
 \fint|W^-|^2\longrightarrow\infty;
\]
否则存在有界子列，再次违反 (C.0)。由端点 \(p/V\to2/(9\pi^2)\)、\(W^+\to0\) 及 Euler 恒等式，它还须满足
\[
 \frac\chi p\longrightarrow\infty,
 \qquad \frac\chi A\longrightarrow\infty.
\]
本文并未证明这种无界密度逃逸不可能。有限 \(K\) 被用于 (1.3)、第一延拓的 adjoint 控制、\(c\) 的 \(L^4\) 和导数预算；不能把这项依赖隐去后宣布无条件 O10 已解。

---

## 8. 与既有错误捷径的区别

1. 第二次三次旋量 \(t(v)\in S^+\otimes L^4\) 的实际方向是与 \(\Phi\) 正交的正旋量线，行列式九倍势在此趋向 \(-7\)，不是 \(+5\)。本文没有改变这一计算。
2. 本文使用 \(\Phi\wedge t(v)\in L^5\)，其标量线丛连接、相反 almost-complex 方向和曲率收缩是不同的算子；正势 \(10/3\) 由 (5.2) 独立计算。
3. 相反结构的第二次 Nijenhuis 测试仍会选错消去方向；本文转而使用完整 off-diagonal 自对偶曲率，得到新的 CR 约束 (3.4)。
4. 没有以小 \(L^2\) 残差假装强 Hessian 小；弱方程只与已验证的测试配对。
5. 没有忽略扭率零点。\(\rho,m\) 下幅度截断、\(L^4\) 预算和有限体积归一化逐项控制全部新增边界误差。
6. 没有把有限平均 \(W^-\) 当作点态曲率界，也没有把 \(c(B)\) 当作与 \(B\) 无关的常数。

---

## 9. O11 的影响与不影响

本文完成的是 O10 的任意固定有限密度阶段。它不决定 O11。

O10 禁止端点的输入是 \(\rho\to4/3\)、\(|\tau|^2\to128/81>0\)，这使第五幂线丛截面获得非消失的归一化质量。O11 的原平衡族则处于允许 KE 端附近：实际旋量梯度和扭率在总体积归一化下可以趋零，而其总能量仍在 \(Q=Ah\) 尺度。不能将本文的固定正幅度归一化、截断界和对偶测试直接搬成 \(o(Q)\) 的估计。

续研 B 的 O11 自适应测试和正曲率补偿仍可使用：
\[
 (\nabla^*\nabla+\sqrt{1+|Z|^2})H=Z,
\]
\[
 2\int\operatorname{Rm}(Z,H)
 \ge\int|\nabla H|^2+
   \int(1+|Z|^2)^{-1/2}|\nabla^*\nabla H|^2-o(Q).
\]
本文没有取得把该补偿与 \(8\pi^2Q\) 锐利连接的拓扑下界，也未得到低于4的合法恢复序列。不能将它们从原稿的开放登记中删除。

## 10. 来源、有限核验及证明接入

直接依赖：

- [S0] `20260929_Line1_Integrated_Manuscript.tex`：O10定义、共形归约、有限参数估计；实际 Clifford、曲率块、三次扭率恒等式。
- [S1] `01_O10_Strong_Current.md` / `O10_Strong_Current_Prerequisite.md`：R1–R2、正旋量梯度四次一致可积、\(N_\tau\to0\)。
- [S2] `O10_Strengthened_Endpoint.md` §§2–6.1：有界截断、resolvent、有限平均 \(W^-\) 下的 Hessian／梯度预算及相位／径向小量。本文没有把该文的临界 \(50/3\) 结论作为前提。
- [S3] `O10_Resolvent_Prolongation.md` §§2–4：第一实际延拓、仅剩水平复分量。**这是从谱阈值加强到本文结论所额外使用的关键输入。**
- [S4] `O10_Critical_Geometry.md` §10：两项手性／势符号错误捷径的独立计算。
- [S5] `O11_Positive_Curvature_Compensation.md`：仅用于第9节保留O11的准确现状。

外部结构参照：Apostolov–Drăghici, *Almost Kähler 4-manifolds with J-invariant Ricci tensor and special Weyl tensor*, arXiv:math/9911196，§2，Corollary 1。其精确局部结果断言 ASD almost-Kähler 与 J-invariant Ricci 的相容性强迫 scalar-flat Kähler；该已知定理不是本文退化序列估计的替代证明，本文也不宣称解决一般 Goldberg 猜想。

`verify_negative_line.py` 用精确符号运算检查：(i) Clifford 到 LC 的转换；(ii) 保留两条相位流的 Cartan 式；(iii) 非线性二形式的 ASD 性；(iv) \(\mathcal L^*\mathcal D\mathcal L=I-iJ_-\)；(v) 第五幂外积归一化；(vi) 正势 \(10/3\)。它不验证分析极限、全局量词或前置 PDE。

建议接入原稿第25节后：将“对任意给定有限 \(B\) 的一般弱零端”更新为本文条件下的已证推论；将“完全删除 Euler 密度控制”明确保留为未解；O11登记保持不变。独立审读应首先核查第3–6节的单位线丛类型、两条相位流、cutoff弱测试及正势符号，而不是仅检查最终密度结论。
