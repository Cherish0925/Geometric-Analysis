# 第一科学主线：双取向实际类的联合间隙

日期：2026-10-07。

## 0. 结论的逻辑地位

本文证明一条**以项目有限密度 O10 定理为前置的全局推论**。新的工作是同一度量上的双取向实际类配对、定量极化控制，以及把可能的等号逼近送入一个固定密度的 O10 窗口。本文没有重新证明有限密度 O10 所引用的 R1、强流或线丛分析，也没有把该前置定理的正确性由本推论反向认证。

条件性结论为：对每一个光滑定向曲面丛

\[
\Sigma_f\longrightarrow M\stackrel\pi\longrightarrow\Sigma_b,
\qquad f,b\ge2,
\]

存在一个不依赖两个亏格、单值、总空间或度量的正数 \(\varepsilon_{\mathrm{SB}}\)，使全部光滑度量满足

\[
\boxed{\mathcal J(g)+\left(1-\frac{3|\tau(M)|}{\chi(M)}\right)_+
\ge\varepsilon_{\mathrm{SB}}.}
\tag{T}
\]

这里 \(\tau\) 表示签名，

\[
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2\,dV_g,\quad
R(g)=\int_M|\operatorname{Ric}_g|^2\,dV_g,\quad
\mathcal J(g)=4P(g)/R(g).
\]

Weyl 范数采用曲率算子在二形式上的 Hilbert–Schmidt 规范；Ricci 使用二张量范数。所有拓扑交叉积没有隐藏的 \(2\pi\) 因子。

因此，若 M 承载 Einstein 度量，则

\[
\boxed{3|\tau(M)|\le(1-\varepsilon_{\mathrm{SB}})\chi(M).}
\tag{E}
\]

这是一条从项目端点机制导出的统一定量加强。经典 Kotschick 定理已有严格不等式 \(3|\tau|<\chi\)；本文不将该经典结论、双取向辛构造或 SW 非消失重新登记为新成果。本文也不声称完成全领域的优先性核查。

**一般无密度 O10 与原平衡手术族 O11 的匹配最优值没有因此解决。**原 O11 的次四恢复保持已有状态。

---

## 1. 唯一非经典解析前置 FD2

使用项目 `O10_All_Finite_Density.md` 第1节及第4节所陈述的定理，在单个固定密度 B=2 上：

> **FD2.** 在原实际共形单极子供给下，若同一实际类 c 满足
> \[
> p_c=(c^+)^2\ge A_c>0,\quad c^2\ge T_+=2\chi+3\tau,
> \quad\chi/A_c\le2,
> \]
> 则存在 \(c_{\mathrm{FD}}(2)>0\)，对每一个允许度量及全部 \(\beta\ge2\) 有
> \[
> \fint|\operatorname{Ric}+g|^2+\frac{D_\beta(g,c)}V
> \ge c_{\mathrm{FD}}(2)\frac{(\beta-2)^2}{\beta^2},
> \]
> 其中
> \[
> D_\beta(g,c)=(1+\beta^{-1})\int s^2
> +6(\beta+1)\int|W^+|^2-72\pi^2p_c.
> \]
> 常数不依赖几何紧性、直径、非塌缩、Sobolev 常数或具体流形。

本文仅在反取向 \(\bar M\) 的 \(s=-4\) 代表上使用 FD2。固定

\[
c=\min\{1,c_{\mathrm{FD}}(2)\},\qquad
\boxed{\varepsilon_{\mathrm{SB}}=(c/200)^2.}
\tag{1.1}
\]

常数200只是便于核查的选择，没有最优性主张。

经典前置为：Thurston 曲面丛辛形式构造；Taubes 的辛典范类 SW 非消失以及 \(b^+>1\) 时实际单极子供给；SW 标量预算；Yamabe 归一化；Chern–Weil；Hodge 极化。项目 N1 继承稿已记录所需的共形比较，下面亦给出计算。

## 2. 曲面丛提供的两个真实类

写 \(e=\chi(M)=4(f-1)(b-1)>0\)。必要时反转基底取向，从而反转总空间取向，使 \(\tau\ge0\)。\(e,\mathcal J,|\tau|\) 不受这个选择影响。

取实定向平面丛分裂

\[
TM\simeq T_{\mathrm{vert}}M\oplus\pi^*T\Sigma_b.
\]

令 \(x=e(\pi^*T\Sigma_b)\)、\(y=e(T_{\mathrm{vert}}M)\)。在所选总空间取向上，

\[
x^2=0,\qquad x\cdot y=e,\qquad y^2=3\tau.
\tag{2.1}
\]

第一式因 x 来自二维基底；第二式为 Euler 类乘积；第三式来自 \(p_1(TM)=x^2+y^2\) 与签名公式。

Thurston 构造分别对基底面积项取正、负符号，得到两个总空间取向上的辛形式。其相容几乎复结构分别与水平/垂直块的取向选择同伦。因此可取两个实际典范或反典范类

\[
a=x+y,\qquad b=x-y.
\]

b 与反取向结构的实际典范类只可能相差整体符号，该符号不影响下文平方和绝对配对。于是

\[
\boxed{
 a^2=2e+3\tau,\quad b^2[M]=-2e+3\tau,
 \quad a\cdot b=-3\tau.
}
\tag{2.2}
\]

b 是 \(\bar M\) 上的真实辛典范类，不是从一个形式交叉向量猜出的单极子类。

由 \(\pi_1(M)\twoheadrightarrow\pi_1(\Sigma_b)\)，有 \(b_1(M)\ge2b\ge4\)。当前取向满足

\[
b_2^+(M)=\frac{e-2+2b_1+\tau}{2}>1.
\]

因此 a 具有全度量非消失供给。其正平方 \(a^2=2e+3\tau>0\) 排除了非负标量曲率的 Yamabe 代表：该代表上的未扰动 SW 方程与 Weitzenböck 恒等式会迫使旋量为零、\(a^+=0\)，与 \((a^+)^2\ge a^2>0\) 矛盾。

故 M 的每个共形类均为负 Yamabe 类，所有度量均有 R>0。本文不对 Ricci-flat 度量使用未定义的 \(4P/R\)。

反取向的 \(b_2^+\) 条件将在第4节以已有曲率预算推出，避免先假定一个待证的签名上界。

## 3. 转到同一个负 Yamabe 代表

若原度量 \(\mathcal J(g)\ge1\)，(T)直接成立。故只考虑 \(\mathcal J(g)<1\)。

令 \(\hat g\in[g]\) 为 \(s_{\hat g}=-4\) 的代表。Weyl 能量的共形不变性与 Chern–Weil 给出

\[
P(g)-P(\hat g)=\Delta S/12,\quad
R(g)-R(\hat g)=\Delta S/3,
\quad\Delta S=\int_gs^2-\int_{\hat g}s^2\ge0.
\]

因而 \(\mathcal J(g)\) 是 \(\mathcal J(\hat g)\) 与1的加权平均。原 \(\mathcal J(g)<1\) 迫使

\[
j:=\mathcal J(\hat g)\le\mathcal J(g)<1.
\tag{3.1}
\]

以下全部度量、Hodge 投影和实际解都使用同一个 \(\hat g\)。记

\[
t=3\tau/e\ge0,\quad u=V/(2\pi^2e),\quad
r=P/V=\frac{4j}{4-j},\quad
w=\fint|W^-|^2.
\tag{3.2}
\]

由于 \(\hat g\) 为常标量代表，原归一化缺陷还满足 \(\mathcal E(\hat g)=j\)，但证明不需要从这个等式推出任何极小值取得性。

## 4. 先仅使用正取向实际类和两手性 Chern–Weil

设 \(U=(a^+)^2/e\)。实际 SW 标量预算

\[
16V\ge32\pi^2(a^+)^2
\]

及交叉平方给出

\[
2+t\le U\le u.
\tag{4.1}
\]

反手性 Chern–Weil 公式给出精确关系

\[
\boxed{w=\frac{2-t}{u}-\frac13+\frac{j}{4-j}\ge0.}
\tag{4.2}
\]

由于 j<1，(4.2)首先推出 t<2，并给出

\[
2+t\le u\le C(j)(2-t),\qquad
C(j)=\frac{3(4-j)}{4(1-j)}.
\tag{4.3}
\]

于是

\[
(16-7j)t\le16+2j,
\quad
\boxed{t\le1+\frac{9j}{16-7j}\le1+j.}
\tag{4.4}
\]

现在 t<2 推出

\[
b_2^-(M)=\frac{e-2+2b_1-\tau}{2}
>\frac e6+b_1-1>1.
\]

所以反取向的辛典范类 b 也具有全度量实际供给，且

\[
b^2[\bar M]=e(2-t)>0.
\]

由其实际标量预算，令 \(Z=\|b^-\|^2/e\)（负 Hodge 范数取正值），则

\[
2-t\le Z\le u.
\tag{4.5}
\]

这里不存在从同一自旋丛中任意改取向的步骤：a 和 b 分别由两个真实辛结构提供。

## 5. 同一个度量上的交叉配对补出关键极化信息

置

\[
d=j+(1-t)_+.
\]

如果 \(d\ge1/256\)，则因 \(\varepsilon_{\mathrm{SB}}\le1/40000\)，结论已成立。暂设

\[
0<d\le1/256.
\tag{5.1}
\]

设

\[
X=U-(2+t)=\|a^-\|^2/e\ge0,
\qquad Y=Z-(2-t)=\|b^+\|^2/e\ge0.
\]

由(4.3)–(4.4)可得

\[
1-d\le t\le1+d,\qquad 3-d\le u\le3+5d<4,
\]
\[
\boxed{X\le4d,\quad w\le d,\quad r\le4d/3.}
\tag{5.2}
\]

给出常数核对：当 j≤1/4 时，\(C(j)\le3+3j\)。记 \(d_-=(1-t)_+\)，则

\[
X\le4d_-+3j(1+d_-)\le4(j+d_-)=4d.
\]

(4.2)和 \(u\ge2+t\) 给

\[
w\le\frac{4(1-t)}{3(2+t)}+\frac{j}{4-j}
\le\frac12d_-+\frac13j\le d.
\]

现在使用独立于两项平方预算的真实拓扑配对。Hodge 正交分解和 Cauchy–Schwarz 使(2.2)变成

\[
\boxed{t\le\sqrt{UY}+\sqrt{XZ}.}
\tag{5.3}
\]

在 \(X\le4d,\ Z\le u<4\) 下，有 \(\sqrt{XZ}\le4\sqrt d\)。由于 \(t-4\sqrt d>0\)，

\[
\frac Zu\ge\frac{2-t}{u}
+\frac{(t-4\sqrt d)^2}{u^2}.
\tag{5.4}
\]

第一项由 \(w\ge0\) 控制：

\[
\frac{2-t}{u}\ge\frac13-\frac j{4-j}\ge\frac13-\frac d3.
\]

第二项满足

\[
\frac{(t-4\sqrt d)^2}{u^2}
\ge\frac{(1-d-4\sqrt d)^2}{(3+5d)^2}
\ge\frac19-\frac89\sqrt d-\frac{16}{27}d.
\]

最后一个不等式由

\[
(1-d-4\sqrt d)^2\ge1-2d-8\sqrt d>0,
\quad
(3+5d)^{-2}\ge\frac19-\frac{10}{27}d>0
\]

逐项相乘得到。因此

\[
\frac Zu\ge\frac49-\frac89\sqrt d-\frac{25}{27}d
\ge\boxed{\frac49-2\sqrt d.}
\tag{5.5}
\]

这是新接通的关键：若正取向接近复双曲拓扑边界且无迹 Ricci 很小，正取向实际类几乎完全自对偶；它与反取向实际类的固定交叉积，迫使后者的正投影（在反取向下）进入原禁止端点的数值范围。单独知道两个类的平方无法得到(5.3)。

## 6. 反取向端点矛盾；常数对全部曲面丛统一

在 \(\bar M\) 上使用 b，选取预算

\[
A_-=e(2-t)=b^2[\bar M]=T_+(\bar M)>0.
\]

投影 \(p_b=Ze\ge A_-\)，同一类平方条件恰取等号。而且

\[
\frac{\chi(\bar M)}{A_-}=\frac1{2-t}
\le\frac1{1-d}<2.
\tag{6.1}
\]

所以无论两个亏格和单值怎样变化，FD2都在**同一个固定密度2**上使用。

反取向参数缺陷为

\[
\bar\kappa_\beta
=r+16(1+\beta^{-1})+6(\beta+1)w-36\frac Zu.
\tag{6.2}
\]

取有限参数 \(\beta=d^{-1/2}\ge16\)。由(5.2)、(5.5)，

\[
\bar\kappa_\beta
\le\frac43d+16\sqrt d+6(\sqrt d+d)+72\sqrt d
=94\sqrt d+\frac{22}{3}d
<100\sqrt d.
\tag{6.3}
\]

FD2同时给出

\[
\bar\kappa_\beta\ge c(1-2\sqrt d)^2
\ge\frac{49}{64}c\ge\frac12c.
\tag{6.4}
\]

于是 \(d\ge(c/200)^2\)。

还须处理 d=0，而不能除以零：此时 j=0,t=1,u=3,X=0,w=0；(5.3)直接给 \(Z\ge4/3\)。因此对每个有限 \(\beta\ge2\)，

\[
\bar\kappa_\beta\le16/\beta.
\]

这与FD2在 \(\beta\to\infty\) 时的正下界矛盾。没有把 \(\beta=\infty\) 当成一个原定理参数。

所有分支合并得到

\[
j+(1-t)_+\ge(c/200)^2.
\]

再用 \(j\le\mathcal J(g)\) 和取向可反转，证明(T)。证毕。

## 7. Einstein、Kodaira与全度量含义

### 7.1 Einstein与非Einstein度量

实际正预算排除了非负标量曲率，因此这里的Einstein度量必具有负Einstein常数，\(R>0\)、\(\mathcal J=0\)。将其代入(T)，得到(E)。

对固定流形，若 \(d_{\mathrm{top}}=(1-3|\tau|/e)_+<\varepsilon_{\mathrm{SB}}\)，则所有度量都有

\[
\mathcal J(g)\ge\varepsilon_{\mathrm{SB}}-d_{\mathrm{top}}>0.
\]

利用正取向实际标量预算还给出

\[
P(g)\ge2\pi^2 e(2+t)
\bigl(\varepsilon_{\mathrm{SB}}-d_{\mathrm{top}}\bigr).
\]

这不是仅判断一个局部修复是否成功，而是约束所有光滑竞争度量。

### 7.2 Kodaira纤维化

对紧复曲面的光滑Kodaira纤维化，基底和纤维亏格均至少2，总空间无有理曲线。它是极小一般型曲面；其规范丛为ample，因而具有负Kähler–Einstein度量。这里使用经典曲面论与Aubin–Yau存在定理，不将其作为新证明。

在复取向，\(c_1^2=2e+3\tau\)、\(c_2=e\)。由(E)得到

\[
\boxed{c_1^2(M)\le(3-\varepsilon_{\mathrm{SB}})c_2(M).}
\tag{7.1}
\]

也可仅把(7.1)陈述为对已知承载负KE度量的Kodaira纤维化的推论，从而不需在本稿中展开规范丛amplicity的经典证明。

其意义是把经典严格 \(c_1^2<3c_2\) 改为独立于亏格和单值的正宽度。本文没有证明最佳宽度，更没有证明 \(8/3\) 是Kodaira Chern斜率的最优上界。

### 7.3 一个精确校准

在负KE的Kodaira情形，记 \(r_K=c_1^2/e\)。其反取向典范类是原复结构的(1,1)类，故

\[
p_b=\frac{4e^2}{c_1^2},\quad
V=2\pi^2 c_1^2,\quad
\fint|W^-|^2=\frac{4(3-r_K)}{3r_K}.
\]

由此(6.2)化为

\[
\bar\kappa_\beta
=16(1+\beta^{-1})
+8(\beta+1)\frac{3-r_K}{r_K}
-\frac{144}{r_K^2}.
\tag{7.2}
\]

当 \(r_K=2,\beta=2\) 时，右侧为0，符合允许的乘积KE端；当形式上 \(r_K=3\) 时，它等于 \(16/\beta\)，恰好进入FD2排除的极限。这只是符号与常数校准，不假定存在斜率3的光滑Kodaira纤维化。

## 8. 为什么不等于两个原问题已解

1. 一般 O10 不要求存在满足(2.2)的反取向实际类。本文用到的全局配对是额外的真实信息，不能从一条正取向SW解无条件制造出来。
2. 原 O11 平衡族含普通负吹起及连接柄，不能默认仍是本稿的曲面丛，也不能默认其两取向有本稿同样的实际类。本文没有提高该原族的最佳首项下界。
3. 原有严格次四恢复仍然成立于其已验证范围；本文不恢复已被否定的“所有度量成本至少为4”的目标。
4. 外部openai/math文献没有被形式上插入本证明。本文使用的是项目已给出的FD2以及经典实际供给；新的证明信息来自两个实际类的同度量交叉配对。无需把不适配的外部定理硬接入来装饰结论。
5. 若FD2上游分析之后发现错误，本文作为其条件推论需同步调整。本文不能作为FD2的独立验证。

## 9. 文献与文件来源

### 项目来源

- `O10_All_Finite_Density.md`：§1结论、§4参数与共形转移、§5依赖边界。本文只调用B=2这一固定值。
- `03_N1_Complete_Inheritance.md`：负Yamabe输入、SW标量预算以及式N5的精确共形比较。本文没有使用N1的最终拓扑阈值替代FD2。
- 最新两会话包：仅用于保持O11严格次四构造与当前状态，不参与本新证明。

### 经典原始文献

- D. Kotschick, *On regularly fibered complex surfaces*, Geometry & Topology Monographs 2 (1999), 291–298, Theorem 3. https://arxiv.org/abs/math/9911255 。原定理给出复结构或Einstein存在时的严格 \(3|\tau|<e\)，没有在该定理中陈述本稿的统一余量。
- C. LeBrun, *Diffeomorphisms, symplectic forms and Kodaira fibrations*, Geometry & Topology 4 (2000), 451–456. https://arxiv.org/abs/math/0005195 。用于核对反取向辛形式、典范类与签名的交叉关系。
- W. P. Thurston, *Some simple examples of symplectic manifolds*, Proc. Amer. Math. Soc. 55 (1976), 467–468. 曲面丛辛形式的经典构造。
- C. H. Taubes, *The Seiberg–Witten invariants and symplectic forms*, Math. Res. Lett. 1 (1994), 809–822. 辛典范类的SW非消失。本文未重新证明该经典结果；反取向供给还显式检查了 \(b^+>1\)。
- F. Catanese and S. Rollenske, *Double Kodaira fibrations*, https://arxiv.org/abs/math/0611428 。用于Chern斜率研究背景，非本证明前置。

有限代数脚本 `verify_two_orientation.py` 验证本稿的有理恒等式、维数常数与两个KE校准；它不认证SW非消失、Yamabe理论、FD2或完整几何分析。全文的新增证明在§§2–6列出；没有把数值计算或文件保存当成数学认证。
