# 双取向配对的一般间隙与完备 Einstein 实例的全局几何

2026-10-08

本稿沿两项现有成果继续推导。第一部分以项目的固定密度端点命题 FD2 为输入，推广双取向间隙；第二部分使用系统已构造并写出曲率公式的完备 Einstein strictly almost-Kähler 度量，确定其截面曲率和全部等距商的体积性质。完整证明见同目录 `Pair_Gap_and_Pinched_Example.tex`。

## 1. 具有配对损失的双取向间隙

设 M 为闭定向四流形，e=χ(M)>0，选择取向使 τ≥0，T±=2e±3τ，J=4P/R。

令 C+ 是 M 上有限组真实单极子类：相应结构的未扰动 SW 方程对每个光滑度量有解。取

\[
 a\in\operatorname{Hull}(\mathcal C_+),\qquad a^2\ge T_+.
\]

再取反取向流形上的一个真实单极子类 b，满足

\[
 b^2[\bar M]=-b^2[M]\ge T_-.
\]

所有未注明取向的交叉积都在 [M] 上计算。记

\[
 t=\frac{3\tau}{e},\qquad z=\frac{|a\cdot b|}{e},\qquad
 \varepsilon_{\rm pair}=\left(\frac{\min\{1,c_{\rm FD}(2)\}}{200}\right)^2.
\]

在 FD2 的输入下，有

\[
 \boxed{\mathcal J(g)+(1-t)_++(t-z)_+\ge\varepsilon_{\rm pair}}
\]

对全部光滑度量成立。不要求 M 是曲面丛，也不要求 a 本身是真实单极子类；它属于真实类的凸包已经足够。实际曲率预算只在凸包一侧取凸组合，FD2 则始终作用于真实类 b。

### 证明要点

真实类的标量预算及凸性给出

\[
 \|a^+\|\le\sum_i\lambda_i\|a_i^+\|
 \le\sqrt{S/(32\pi^2)}.
\]

正平方排除非负 Yamabe 共形类。在负代表 s=-4 上，令

\[
 j=\mathcal J(\widehat g)\le\mathcal J(g)<1,\quad
 u=\frac V{2\pi^2e},\quad r=\frac PV=\frac{4j}{4-j},\quad
 w=\frac1V\int|W^-|^2,
\]

\[
 U=\frac{\|a^+\|^2}{e},\quad Z=\frac{\|b^-\|^2}{e},\quad
 X=\frac{\|a^-\|^2}{e},\quad Y=\frac{\|b^+\|^2}{e}.
\]

同一个度量上的预算给

\[
 2+t\le U\le u,\quad 2-t\le Z\le u,\quad
 w=\frac{2-t}{u}-\frac13+\frac{j}{4-j}\ge0.
\]

因此 t<2 且 t≤1+j。令 \(d=j+(1-t)_++(t-z)_+\)。若 0<d<1/256，则

\[
 1-d\le t\le1+d,\quad3-d\le u\le3+5d<4,\quad
 X\le4d,\quad w\le d,\quad r\le4d/3,\quad z\ge1-d.
\]

Hodge 分解保留了混合交叉积：

\[
 z\le\sqrt{UY}+\sqrt{XZ}
 \le\sqrt{u\{Z-(2-t)\}}+4\sqrt d.
\]

从而

\[
 \frac Zu\ge\frac49-2\sqrt d.
\]

在反取向上取 A−=e(2−t)，则 e/A−<2。取有限 β=d^(−1/2)，得到

\[
 \bar\kappa_\beta
 =r+16(1+\beta^{-1})+6(\beta+1)w-36Z/u
 <100\sqrt d.
\]

FD2 同时给出 \(\bar\kappa_\beta\ge\min\{1,c_{\rm FD}(2)\}/2\)，于是 d≥εpair。d=0 时有 \(\bar\kappa_\beta\le16/\beta\)，直接矛盾。较大 d 的分支自动成立。

### 多真实类的有限维版本

有有限组反取向实际类 C− 时，定义

\[
 z_* = \frac1e\max\left\{|a\cdot b|:
 a\in\operatorname{Hull}(\mathcal C_+),\ a^2\ge T_+,\
 b\in\mathcal C_-,\ -b^2\ge T_-\right\}.
\]

假设候选集合非空。有限凸包的紧性保证最大值存在。于是

\[
 \mathcal J(g)+(1-t)_++(t-z_*)_+\ge\varepsilon_{\rm pair}.
\]

这是一项使用真实类之间混合相交数据的有限维优化，而不是只记录各类平方。它不需要为凸组合求解 SW 方程。若存在 Einstein 度量，则 t≤1，且 min(t,z*)≤1−εpair。

### 几何特例：辛形式对

若 TM=E1⊕E2 来自辛形式对，令 x=e(E1)、y=e(E2)，则

\[
 xy=e,\quad x^2+y^2=3\tau,\quad a=x+y,\quad b=x-y.
\]

当两个取向有相应真实规范供给（例如 b2±>1 下的辛典范类）时，得到

\[
 \boxed{\mathcal J(g)+\left(1-\frac{3\tau}{e}\right)_+
 +\frac2e\bigl(\min\{x^2,y^2\}\bigr)_+
 \ge\varepsilon_{\rm pair}.}
\]

一个 Euler 类平方非正时，最后一项消失，恢复曲面丛形式的间隙，不要求叶空间本身是光滑曲面。这里没有假定所有辛形式对都满足这个符号条件。

## 2. 系统完备模型的锐截面曲率范围

系统已经构造 (N,g,Ω)，N≅R4，Ric=−3g，W−=0，dΩ=0，|Ω|²=2，且 |∇Ω|²>0；下述计算不使用 FD2。

源稿给出的曲率算子为

\[
 \mathcal R^-=-I,\qquad\mathcal R^+=\operatorname{diag}(r_1,r_2,r_3),\qquad
 D=1+3x^2,\quad1/3\le x<1,
\]

\[
 r_1=-\frac{3(x-1)^2(21x^4+18x^3+12x^2-2x-1)}{D^3},
\]
\[
 r_2=-\frac{3(x+1)^2(21x^4-18x^3+12x^2+2x-1)}{D^3},\qquad
 r_3=\frac{9(x-1)^2(x+1)^2(5x^2-1)}{D^3}.
\]

直接因子化得

\[
 r_1-r_2=48x^3/D^2>0,
\]
\[
 r_3-r_2=12(x+1)^2(3x-1)(3x^3-3x^2+x+1)/D^3\ge0,
\]
\[
 r_2'=72x(x-1)^2(x+1)(3x^2-3x-2)/D^4<0,
\]
\[
 \frac13-r_3=\frac{4(7-3x^2)(3x^2-1)^2}{3D^3}\ge0.
\]

另有 r1≤0，r2(1/3)=−4/3，r2→−3。单位简单二向量的两手性部分模平方各为1/2，所以

\[
 \sec(\sigma)=\tfrac12\langle\mathcal R^+u,u\rangle-\tfrac12,
 \qquad|u|=1.
\]

因此

\[
 \boxed{-2<\sec_g\le-1/3.}
\]

上端在 x=1/√3 的平面上取得，下端为无穷端的极限，两个常数均锐。这个完备 Einstein strictly almost-Kähler 例子不仅 Ricci 为负，而且全部截面曲率被统一夹在两个负数之间，锐全局夹逼比为1/6。

## 3. 度量的任何等距商都不可能有有限体积

完整曲率算子的最小特征值是严格单调的 r2(x)。因而 x 可以从度量本身恢复，所有等距变换都保持 x；不必要求它们保持 Ω。

令 dr=√G dx。等距变换保持 r 和 ∇r，故在正则区域具有 (r,p)↦(r,φ(p)) 的形式，φ 与 r 无关。任意自由、正常不连续的离散等距群所给的每个正则层，都是同一个商 Y。源稿的体积密度是

\[
 dV=\frac{64x(1+3x^2)}{3(1-x^2)^3}\,dx\,|\sigma_{123}|.
\]

商层的轨道密度总质量为某个正数 v（允许无穷），于是

\[
 \operatorname{Vol}(N/\Gamma)
 =v\int_{1/3}^1\frac{64x(1+3x^2)}{3(1-x^2)^3}\,dx=\infty.
\]

这比只排除保持 Ω 的紧商更强。

进一步，Einstein 度量在谐和坐标中实解析；完备单连通实解析黎曼流形之间的局部等距可以延拓为整体等距。因此不存在完备有限体积 Einstein 四流形含有与该模型局部等距的非空开集。特别不能在保留该模型一个精确开片的同时修改外部，得到闭 Einstein 度量。这不排除处处改变度量的构造，也不排除近似拼接。

## 4. 本轮与原主线的关系

- 双取向间隙：从曲面丛的精确交叉关系推广到允许配对短缺、允许一侧凸包输入的命题，仍以 FD2 为前置。没有凭空提供非极小一般型曲面的反取向单极子类。
- Fino 实例：构造归系统；本轮新增锐截面夹逼、只依赖度量的等距商排除和精确 Einstein 开片的有限体积延拓障碍。
- Q3 的光滑极小值取得、一般无密度 O10、闭负 Goldberg、全度量锐最优值，均不由这些推论自动解决。

## 5. 来源

项目原稿：`Line1_Two_Orientation_Global_Gap.md`（FD2 与原同度量证明）；`Q4_Complete_Example_and_Fino_Question.tex`（系统完整模型和曲率块）；`03_Subsequent_Mathematical_Developments.tex`（体积公式）。

经典文献：LeBrun, *Four-Manifolds, Curvature Bounds, and Convex Geometry*, arXiv:math/0611450；Bande–Kotschick, *The geometry of symplectic pairs*, arXiv:math/0407441；DeTurck–Kazdan, *Some regularity theorems in Riemannian geometry*, Theorems 5.2, 5.4；Kobayashi–Nomizu, *Foundations of Differential Geometry*, Vol. I, Chapter VI, Corollary 6.4。

`check_identities.py` 以精确有理式检验所列有限代数，`exact_checks.json` 保存结果。它不替代 FD2、原模型完整性及经典定理的证明。
