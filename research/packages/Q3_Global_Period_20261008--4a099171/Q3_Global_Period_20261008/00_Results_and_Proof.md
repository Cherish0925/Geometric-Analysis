# Q3：全局极化预算对带标记 ALE 退化的限制

日期：2026-10-08。

本次只推进 Q3：在固定光滑四流形上取得一个非 Bach-flat 的全局 P 极小元。新增内容是一个闭流形上的极化下界，以及它对真实带标记 ALE 退化的后果。没有证明光滑极小值已经取得。

## 1. 固定对象与输入

沿用另一会话选择的经典 Godeaux 曲面 X，K_X²=1，并在其十五条度一有理曲线之外吹起一点：

\[
 M=X\#\overline{\mathbb{CP}}^2,
 \quad K=\pi^*c_1(K_X),\quad K^2=1,\quad E^2=-1,\quad K\cdot E=0.
\]

所有交叉积在实上同调中计算，忽略扭转。记

\[
 P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2,\qquad p_* = \inf_gP(g).
\]

系统已有的严格构造与经典单极子下界给出

\[
 \frac{16\pi^2}{3}\le p_*<8\pi^2.
\]

这里严格上界是输入，不是本轮新构造。负 Yamabe 性及无 Einstein 度量也沿用原 Q3 论证。因此，一旦 p_* 由光滑度量取得，它必为非 Bach-flat。

本轮只用经典曲率估计中的一个尚未丢弃投影信息的形式：

\[
 \boxed{P(g)\ge \frac{16\pi^2}{3}\|K_g^+\|^2.}
 \tag{1}
\]

这是 LeBrun Proposition 3.1 的曲率估计与 Proposition 3.2 的实际符号类选择，在 T=2χ+3τ=0 时的后果。不调用 N1、FD2 或极限轨形上的新单极子供给。

## 2. 新连接：负定标记被送入反自对偶方向，会提高剩余典范类的正平方

取固定带标记类 C_1,…,C_r，令

\[
 Q_{ij}=C_i\cdot C_j<0\text{（矩阵负定）},\quad
 d_i=K\cdot C_i,\quad
 \beta_Q(K)=-d^{\mathsf T}Q^{-1}d.
\]

置

\[
 L=\sum_i(Q^{-1}d)_iC_i,\qquad K_\perp=K-L.
\]

精确计算为

\[
 K_\perp\cdot C_i=0,\qquad L^2=-\beta_Q(K),\qquad
 K_\perp^2=1+\beta_Q(K).
\]

对任何度量，Hodge 分解和三角不等式给

\[
 \|K_g^+\|\ge
 \left(\sqrt{1+\beta_Q(K)}-\|L_g^+\|\right)_+.
\]

结合 (1)，得到有限度量的不等式

\[
 \boxed{
 P(g)\ge\frac{16\pi^2}{3}
 \left(\sqrt{1+\beta_Q(K)}-\|L_g^+\|\right)_+^2.
 }
 \tag{2}
\]

因此，若 (C_i)^+_{g_j}→0，则

\[
 \boxed{\liminf_jP(g_j)\ge
 \frac{16\pi^2}{3}(1+\beta_Q(K)).}
 \tag{3}
\]

在极小化序列上，严格上界 p_*<8π² 于是强迫

\[
 \boxed{\beta_Q(K)\le\frac{3p_*}{16\pi^2}-1<\frac12.}
 \tag{4}
\]

这是闭流形的整体下界，不是把泡的费用另加到一个已经包含泡的全局下界上。

## 3. 为什么真实负定 ALE 泡满足所需的投影消失？

假定对应带标记区域在缩放后，于任意固定紧集光滑收敛到一个完整光滑负定 ALE 四流形 N，并保留原 C_i 的紧支撑上同调标记。

ALE 中 H_c²→H² 是同构，且每个类有唯一 L² 调和二形式。负定交叉形式使这些二形式全部反自对偶。对代表 Ω，在远端环带选取 dα_R=Ω，并用固定形状环带的椭圆估计得到

\[
 \|\alpha_R\|_{L^2(A_R)}\le CR\|\Omega\|_{L^2(A_R)}.
\]

截断成紧支撑闭形式 ω_R 后，其自对偶部分满足

\[
 \|\omega_R^+\|_2\le C\|\Omega\|_{L^2(A_R)}\to0.
\]

先固定 R，将该形式经标记映射拉回原闭流形，再令 j→∞。四维二形式的 L² 范数及 Hodge 星不受常数缩放改变，所以

\[
 \limsup_j\|(C_i)^+_{g_j}\|\le\|\omega_R^+\|_2.
\]

最后令 R→∞，得到投影消失。

这个步骤不要求完整泡树的能量等式、外部紧性，或轨形上的规范理论。它要求的是已识别的光滑 ALE 区域与正确标记；没有声称任意未知退化都已经具备这些结构。

## 4. 对 Godeaux 的直接后果

### 单个 (-3) 类

若 C²=-3、K·C=1，则 β_Q=1/3。因此该带标记退化若存在，必有

\[
 \boxed{p_*\ge64\pi^2/9=(8/9)(8\pi^2).}
 \tag{5}
\]

这仍允许 p_* 位于该阈值与 8π² 之间，故不是单泡的排除。

### 两个 (-3) 类

若两个度一 (-3) 类互不相交，则 β_Q=2/3，所以

\[
 \liminf_jP(g_j)\ge80\pi^2/9>8\pi^2.
\]

因此它们不可能同时成为极小化序列中的这类 ALE 标记。该排除不要求局部曲率特征值 μ 非零。

更一般地，两条不同度一曲线若交数为 s<3，则

\[
 Q=\begin{pmatrix}-3&s\\s&-3\end{pmatrix},\quad
 \beta_Q=\frac2{3-s}.
\]

经典十五条曲线的不同交数只有 0、1、2、5。前三种对应的整体下界 P/(8π²) 分别为 10/9、4/3、2，全部超过现有上界。交数为 5 时，(C+D)²=4，二者的自对偶投影也不可能同时趋零。

**结论：在这个固定标记的 Godeaux 单吹起上，十五条原度一有理曲线中，最多一条能沿同一极小化子序列具有消失的自对偶投影，因而最多一条能进入上述负定 ALE 退化。**

这里没有将十五条曲线说成全部光滑球面。

## 5. 对有正确典范标记的循环链，得到更窄的允许类型

对于负定链 [-n_1,…,-n_r]，n_i≥2，附加明确标记

\[
 K\cdot C_i=n_i-2,\qquad E\cdot C_i=0.
\]

若它沿极小化序列满足投影消失，则 (4) 强迫：含非零 K 配对的连通链只能是

\[
 [-3,-2,\ldots,-2]
\]

或其反序，且互相正交的分支中最多有一个这样的带电分支。

证明：令 A=-Q、d_i=n_i-2≥0。变分公式

\[
 d^TA^{-1}d=\max_z(2d^Tz-z^TAz)
\]

用 z_i=d_i/n_i 测试，得 β≥∑(n_i−2)²/n_i。故任何 n_i≥4，或至少两个 n_i≥3，均违反 β<1/2。剩下的唯一 (-3) 若位于内部，两侧 (-2) 尾长分别为 l,r'≥1，Schur 补给

\[
 \beta=\frac1{3-l/(l+1)-r'/(r'+1)}\ge\frac12,
\]

仍被排除。因此 (-3) 必在端点。总长 r 时

\[
 \beta=\frac r{2r+1},\qquad
 \boxed{\liminf\frac{P}{8\pi^2}\ge1-\frac1{6r+3}.}
\]

典范配对全为零的 (-2) 链不被排除；未知标记不能擅自指定成 n_i−2。

## 6. 与最新质量替换结果的结合

另一会话已经在其临界轨形与匹配条件下证明

\[
 P(g_{\lambda,t})=P(g_{\mathrm{orb}})+8\pi^2/3
 -24\pi^2m(g_t)\mu\lambda^2+o(\lambda^2),
\]

故 O(-3) 最小退化要求 μ=0。本轮不重复这项推导，而将同一带标记退化继续限制为

\[
 \boxed{\mu=0\quad\text{且}\quad p_*\ge64\pi^2/9.}
\]

同时，两个原度一 (-3) 类的共同退化已经整体排除，不需要先决定它们各自的四阶匹配系数。

Q3 仍缺光滑取得性。当前结果不能排除一个符合上述预算的零模式 O(-3) 分支、K 正交的 ADE 分支、无实二阶上同调的填充或一般部分塌缩。相关零模式续稿的负内区系数还未成为完整闭流形替换的负系数，不能据此跳过这些分支。

## 7. 本轮文件

- `Q3_Global_Period_Constraints.tex`：独立英文证明，含有限度量式、ALE 连接、十五曲线结论、循环链证明及完整符号类扩展。
- `Q3_Global_Period_Constraints.pdf`：七页阅读本。
- `check_lattices.py`：精确有理数复算。
- `exact_lattice_values.json`：各矩阵的逆、配对费用与阈值。

一手文献：LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, Propositions 3.1–3.2（math/0003068）；Hein–LeBrun, *Mass in Kähler Geometry*, Lemma 1.7（1507.08885）；Böhning–Graf von Bothmer–Sosna, *On the derived category of the classical Godeaux surface*, Proposition 4.3（1206.1830）。
