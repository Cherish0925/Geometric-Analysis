# O11：任意固定复双曲领口中的解析低成本单吹起构造

日期：2026-10-07。本文是从用户提供的两会话档案继续作出的匹配渐近推导。它不声称解决无密度 O10，也不声称确定 O11 的最优值。

## 0. 原稿输入、本轮增量与范围

原稿已有：有限尺度三轴垂直单元的严格区间证书；选定覆盖族上低于4的上界；颈部常模的二次型及其最小值 -18；完整标记单元的全局复制公式。

本轮不将这些重新计为发现。本文补出的具体内容是：给定任意固定半径 R>0，显式构造一参数光滑单元，证明其全成本具有统一的 O_R(epsilon^2) 匹配余项，而不仅是中间颈部的形式系数。由此可在任意给定的固定复双曲基底的覆盖塔上使用一个固定的低成本单元，不再先要求覆盖塔容纳先前那个较大半径的固定数值单元。

记 J_6(g)=∫|Ric_g+6g|²、P(g)=∫|Ric_g^circ|²。Weyl 范数使用原稿曲率算子规范。下面使用 SU(2) 左不变一形式 dσ_i=2σ_j∧σ_k，且 ∫_{S³}σ_1∧σ_2∧σ_3=2π²。取向 dt∧σ_1∧σ_2∧σ_3。

**构造命题。** 对任意 R>0，存在 ε_R>0 和一族 ε∈(0,ε_R) 对应的光滑普通负单吹起单元 g_ε，它在 t≥R 精确等于 Ric=-6g 的复双曲度量，且

\[
\frac{P(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2),
\]
\[
\frac{J_6(g_\epsilon)}{8\pi^2}
=1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2).
\tag{A}
\]

积分可取到任意位于精确 CH 区域的外边界；该区域的 P 和 J_6 均为零。特别是，两项成本均严格小于 8π²，对所有充分小的正 ε 成立。

(A)是本轮明确匹配构造的结论，不是任意竞争度量的下界，不是任意负 KE 背景的二阶响应定理。没有将固定半径余项常数说成与 R 无关。

## 1. 一个明确的光滑度量族

令 T=R/2。固定 χ∈C∞([0,∞))，0≤χ≤1，χ=0 于 [0,1]，χ=1 于 [2,∞)。例如在 1<x<2 可取

\[
\chi(x)=\frac{e^{-1/(x-1)}}{e^{-1/(x-1)}+e^{-1/(2-x)}}.
\]

设 ε<T²/16。写

\[
S(t)=\sinh t,\quad C(t)=\cosh t,\quad
\mathbf c_*=(9/4,3/4,1/2).
\]

三组轨道半径为

\[
\mathbf a^B=(\sqrt{t^2+\epsilon},\sqrt{t^2+\epsilon},t),
\]
\[
\mathbf a^H=(S,SC,S),
\]
\[
\mathbf a^N=
\left(\sqrt{S^2+\epsilon}e^{9\epsilon/4},
\sqrt{S^2+\epsilon}\,C e^{3\epsilon/4},
S e^{\epsilon/2}\right).
\]

上标分别表示平直端 Burns 核心、复双曲背景、所选颈部。

令 χ_in(t)=χ(t/√ε)、χ_out(t)=1-χ(t/T)。对 t>0 定义

\[
 a_i(t)=a_i^H(t)\exp\left\{
 \chi_{out}(t)\left[
 \log\frac{a_i^B(t)}{a_i^H(t)}+
 \chi_{in}(t)\log\frac{a_i^N(t)}{a_i^B(t)}
 \right]\right\},
\]
\[
 g_\epsilon=dt^2+\sum_{i=1}^3a_i(t)^2\sigma_i^2.
\tag{1.1}
\]

所有半径在 t>0 正。该公式分别给出：

- t≤√ε：精确 Burns 核心；
- 2√ε≤t≤T：精确选定颈部 a^N；
- t≥2T=R：精确复双曲背景 a^H。

在 t=0 附近，a_1=a_2=√(t²+ε)，a_3=t，是普通 Hopf bolt 的标准光滑形式。不存在 bolt 处的截断或分母问题。崩塌 σ_3 圆的全周期给普通 O(-1) 拓扑；外 CH 的 Kähler 纤维为 σ_2 方向，故是与内核 Kähler 方向正交的插入。沿用原档案已核验的普通吹起边界标记，不改变手术数。

各区间之间的 χ 在端点平坦，故度量全局 C∞。这不是先构造 C² 度量再要求额外光滑化证书。

## 2. 完整曲率代价的精确校准

令循环指标 (i,j,k)，定义

\[
 u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
 H_i=u_i+\frac12u_ju_k,\qquad
 \lambda_i=\frac{a_ja_k}{a_i}.
\]

原稿 Cartan 公式给

\[
\frac{P}{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.
\tag{2.1}
\]

定义相对密度

\[
\begin{aligned}
\mathscr L_P={}&\frac{\lambda_1}{4}
(\dot u_1+2H_1/\lambda_1)^2\\
&+\frac{\lambda_2}{4}
(\dot u_2-(2u_2-u_1u_3)/\lambda_2)^2\\
&+\frac{\lambda_3}{4}
(\dot u_3+2H_3/\lambda_3)^2
+\frac{2u_1u_2u_3}{\lambda_2}.
\end{aligned}
\]

逐项展开得到

\[
 \mathscr L_P-\sum_i\frac{\lambda_i}{4}
 (\dot u_i-2H_i/\lambda_i)^2
 =\frac d{dt}(u_1^2+u_3^2+u_1u_2u_3).
\]

bolt 端 u=(0,0,-1)，外 CH 端 u=(0,3sinh²t,0)。故

\[
\boxed{\frac{P}{8\pi^2}=1+\int_0^R\mathscr L_P\,dt.}
\tag{2.2}
\]

这条恒等式保留了整个核心、过渡与外边界，不能以一段颈部积分代替它。

再令

\[
 \Sigma=\sum_i\left(\frac{\dot u_i}{a_i}
 +\frac{2H_i}{a_ja_k}\right),\qquad s=-2\Sigma.
\]

因为 dV=2π²a_1a_2a_3dt，且 J_6=P+∫(s+24)²/4，故

\[
 \frac{J_6}{8\pi^2}
 =1+\int_0^R\mathscr L_Jdt,\qquad
 \mathscr L_J=\mathscr L_P+
 \frac{a_1a_2a_3}{4}(\Sigma-12)^2.
\tag{2.3}
\]

## 3. 颈部的两尺度解析因子化

在 2√ε≤t≤T，置

\[
 z=\epsilon/t^2,\quad y=t^2,
 \mathfrak s(y)=\frac{\sinh\sqrt y}{\sqrt y},\quad
 \mathfrak c(y)=\cosh\sqrt y.
\]

其中 0≤z≤1/4、0≤y≤T²，且在 y=0 连续解析延拓。写 a_i=t A_i(z,y)，则

\[
 A_1=\sqrt{\mathfrak s^2+z}\,e^{zyc_1},\quad
 A_2=\sqrt{\mathfrak s^2+z}\,\mathfrak c\,e^{zyc_2},\quad
 A_3=\mathfrak s\,e^{zyc_3}.
\]

先允许任意固定 c=(c_1,c_2,c_3)。所有函数在所述实矩形附近实解析且半径为正。以固定 ε 微分时，

\[
 t\frac d{dt}=2y\partial_y-2z\partial_z.
\]

因而 u_i=U_i(z,y)、λ_i=tΛ_i(z,y) 均可在该矩形解析表示。

在 z=0 上是精确 CH，U_1=U_3=0；在 y=0 上是缩放后的平直 Burns 数据，

\[
 U_1=U_2=0,\quad U_3=-\frac z{1+z},\quad
 (\Lambda_1,\Lambda_2,\Lambda_3)=(1,1,1+z).
\]

由这两条精确边界校准：

1. U_1 可被 yz 整除；U_2 可被 y 整除；U_3 可被 z 整除。
2. 定义

\[
\begin{aligned}
B_1&=2(yU_{1,y}-zU_{1,z})+2H_1/\Lambda_1,\\
B_2&=2(yU_{2,y}-zU_{2,z})-(2U_2-U_1U_3)/\Lambda_2,\\
B_3&=2(yU_{3,y}-zU_{3,z})+2H_3/\Lambda_3.
\end{aligned}
\]

每个 B_i 在 z=0 与 y=0 都为零，故 B_i=yz b_i，b_i 解析。
3. Σ 可写为 y^{-1}B_s；B_s 在 y=0 为零，而 B_s(0,y)=12y。因此 Σ-12=z b_s(z,y)，b_s 解析。

这些因子给出**完整且无形式余项的表示**

\[
\boxed{\mathscr L_P=\frac{\epsilon^2}{t}F_P(z,y;c),\qquad
\mathscr L_J=\frac{\epsilon^2}{t}F_J(z,y;c),}
\tag{3.1}
\]

F_P,F_J 在整个所述矩形上光滑。由普通均值估计，

\[
 |F_\bullet(z,y;c)-F_\bullet(0,0;c)|\le C_{R,c}(z+y).
\tag{3.2}
\]

这一步控制的是下端 z=ε/t² 可能并不极小的整个颈部，不是把固定 t 的 ε 展开直接积分到 t≈√ε。

## 4. 角点系数与严格余项

系数可由固定 t 的一阶半径变化计算：

\[
\frac{\partial_\epsilon a_i}{a_i}\Big|_{\epsilon=0}
=\left(\frac1{2\sinh^2t}+c_1,
\frac1{2\sinh^2t}+c_2,c_3\right).
\]

本轮独立符号计算得到

\[
\begin{aligned}
F_P(0,0;c)={}&11\sum_i c_i^2
 -10(c_1c_2+c_1c_3+c_2c_3)\\
&-37c_1+11c_2+19c_3+59/4,\\
F_J(0,0;c)={}&F_P(0,0;c)+(2c_1+2c_2+2c_3-7)^2/4.
\end{aligned}
\]

令 d=c-(9/4,3/4,1/2)。它们等价于

\[
F_P=-18+16|d|^2-5(d_1+d_2+d_3)^2,
\]
\[
F_J=-18+16|d|^2-4(d_1+d_2+d_3)^2.
\]

两者唯一最小点同为 c_*，值 -18。这个常模最小值原稿已有；本轮脚本作了独立复算，不宣称第一次发现该系数。

选择 c=c_*。由(3.1)–(3.2)，

\[
\begin{aligned}
\int_{2\sqrt\epsilon}^{T}\mathscr L_\bullet dt
&=-18\epsilon^2\log\frac{T}{2\sqrt\epsilon}
 +O_R\left(\epsilon^2\int_{2\sqrt\epsilon}^{T}
 \frac{t^2+\epsilon/t^2}{t}\,dt\right)\\
&=-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2).
\end{aligned}
\]

误差积分确实有与 ε 无关的上界：

\[
\int_{2\sqrt\epsilon}^{T}t\,dt\le T^2/2,\qquad
\int_{2\sqrt\epsilon}^{T}\epsilon t^{-3}dt\le1/8.
\]

因此负对数项不是被一个 O(ε²log(1/ε)) 的未知余项掩盖。

## 5. 内核与外过渡都只支付 O_R(ε²)

**内核。** t≤√ε 上精确 Burns，L_P=0。标量项的归一化积分恰为 27ε²。

在 √ε≤t≤2√ε 上令 t=√ε r。缩放后度量 ε^{-1}g_ε 是固定 Burns 核心在 1≤r≤2 上的 C² 扰动，大小 O(ε)。其 u_1,u_2=O(ε)，而 Burns 的三个校准平方都为零。于是校准平方与三次项的积分全部为 O(ε²)。标量曲率在原尺度为 O(1)，该区域体积为 O(ε²)，故 J_6-P 也为 O(ε²)。内区临界处没有裸的一阶 ε 费用。

**外过渡。** T≤t≤2T 是固定紧环带。g_ε-g_H=O_R(ε) 于 C²，g_H 为 Ric=-6g。故 |Ric+6g|=O_R(ε)，其积分费用 O_R(ε²)。同样 P=O_R(ε²)。也可以直接在(2.2)中看到：u_1,u_3=O_R(ε)，每个校准平方为 O_R(ε²)，三次项 u_1u_2u_3 也为 O_R(ε²)。

合并三段证明(A)。光滑性、正定性、普通吹起拓扑与完整标记领口均已在构造中满足。

## 6. 归一化与每个预定覆盖塔

缩放 \(\widetilde g=6g\) 后，背景 Ric=-\widetilde g，且 J_1(\widetilde g)=J_6(g)。若用几何异常面积 x=Area(E)/π 作为参数，则 x=6ε，故

\[
\frac{J_1}{8\pi^2}
=1-\frac{x^2}{4}\log(1/x)+O_R(x^2).
\]

考虑一个固定紧复双曲曲面 X_0，以及任意有限非分歧覆盖序列 X_j→X_0，度数 d_j→∞。选定 X_0 上一个小嵌入球并留足缓冲；(A)提供适合这个球的固定光滑单元 C，满足

\[
 J_1(C)=8\pi^2(1-\delta_{X_0}),\qquad\delta_{X_0}>0.
\]

每个覆盖含 d_j 个互不相交的提升球。对原比例

\[
 Q_j=k_j+4\ell_j,\quad h_j=Q_j/A_j\to0,\quad
 k_j/Q_j\to2/9,\quad \ell_j/Q_j\to7/36,
\]

因 A_j=d_jA_0，k_j+2ℓ_j=o(d_j)，所以充分大指标下有足够的提升球放置所有固定吹起单元和缩小的手柄部分。使用原供给及复制公式，得到

\[
\boxed{
\limsup_j\frac{\alpha(M_j)}{h_j}
\le\frac{28}{9}+\frac{J_1(C)}{9\pi^2}
=4-\frac89\delta_{X_0}<4.
}
\tag{6.1}
\]

此处不要求先将给定覆盖塔替换为容纳大半径数值单元的特殊覆盖塔。常数 δ_{X0} 可依赖固定基底和选定球；没有证明它对所有不同基底统一。

**极限次序至关重要。** 先固定球，再选取一个足够小但固定的 ε，然后令 j→∞。若让 ε_j→0，节省也趋零，便不能据此获得严格小于4的固定首项界。

## 7. 本轮没有解决的两项终点

- 本文没有给 O11 全体竞争度量的匹配下界，没有确定真实最优首项，也没有证明单元最优值等于闭流形最优值。只是完成了明确的一参数解析构造、全成本余项及其覆盖塔范围。
- 本文没有新增 O10 的无密度排除或合法反例。新档案的 L′ 与有限密度定理已覆盖各自范围；一般共同退化仍需新的实际微分相容性信息。
- 没有在一般 KE 背景上将 Rplus 的一阶响应余项改成所需的二阶小量，也没有直接调用 openai/math 的 Ricci-flat 树定理代替这件事。

## 8. 核查、来源与归属

输入压缩包：`20261007_Einstein_Gaps_Two_Sessions(1).zip`。

直接源文件（相对于解压包）：

1. `sources/Sessions/S1003A02/workspace/notes/step11_subthreshold_perpendicular_cell.md`，§§2、5、6：校准、复制和颈部解释。
2. `sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md`，§4.2：常模二次型和 reduced calculation 的范围；§5：此前复制对覆盖塔的限制。
3. `sources/Sessions/S1003A02/workspace/scripts/o11_neck_density_sympy.py`：原颈部系数计算。
4. `sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md`：普通吹起标记及数值单元光滑匹配。
5. `01_Mathematical_Synthesis.md`：最新选定覆盖族上界与未决最优性。

本轮新脚本 `neck_coefficient.py` 从轨道半径的一阶变化独立计算两种系数多项式。`validate_explicit_family.py` 对完整上述显式族作高精度数值积分，只作一致性检查，不是区间证明。它确认除去 -9ε²log 后的 ε²系数趋于有限数；直接截止族的这一常数可很大，所以没有用该族声称刷新现有的最佳数值3.9961512。

证明的关键是§3的两轴因子化与§5的完整匹配界，而不是数值收敛。

外部方法对照：openai/math, *Path selection and an elliptic inequality on degenerating Ricci-flat trees*，引言强调形式幂—对数展开不能自行当成可积分的统一渐近。这里对我们自己的显式族直接证明相应余项；没有声称满足该文主定理的固定 Ricci-flat 树假设，亦未将其定理作为本命题前提。
