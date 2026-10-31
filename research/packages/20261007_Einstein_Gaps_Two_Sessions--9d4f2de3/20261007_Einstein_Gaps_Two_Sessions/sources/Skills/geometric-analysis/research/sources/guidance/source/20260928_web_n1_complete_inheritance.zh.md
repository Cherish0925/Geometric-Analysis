# 第一科学主线：单解无迹 Ricci 积分障碍与类平方短缺版

2026年9月28日。

依据：数学快照 0b1490791be560203b86a7d9834dcdc3cbc83b41 的第01、05、07、09卷，以及同日续研报告附录06的单解加强。本篇整合原 N1 的完整继承证明、四项适用范围核查，并补出保留类平方成本的短缺版。原 N1 及短缺版均为既有单解参数估计的严格推论；不以此声称全部历史证明或文献首创性已重新认证。原研究稿保持不变。

## 1. 输入与记号

设 M 为闭、连通、定向光滑四流形，g 为光滑度量。假设：

1. [g] 的 Yamabe 常数为负，记其标量曲率归一化为 -4 的代表为 ghat。
2. ghat 上有一个实际普通 Seiberg–Witten 解，采用项目规范
   \[
   D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi).
   \]
3. 该同一 Spin^c 结构的类 a 满足
   \[
   p=(a_g^+)^2=(a_{\widehat g}^+)^2\ge A>0,\qquad
   a^2\ge T,\qquad T=2\chi+3\tau.
   \]

这是逐度量命题。全度量结论须逐共形类提供上述输入，并有统一的 A；不同共形类可以选择不同的结构。

置
\[
P(g)=\int_M|\operatorname{Ric}_g^\circ|^2,\quad
R(g)=\int_M|\operatorname{Ric}_g|^2,\quad
\mathcal J(g)=\frac{4P(g)}{R(g)}.
\]
负 Yamabe 共形类内 R(g)>0。沿用
\[
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}.
\]
有 \(\mathcal E(g)\ge\mathcal J(g)\)。Weyl 范数沿用项目的曲率算子 Hilbert–Schmidt 规范。

## 2. 单解无迹 Ricci 版原积分障碍

**命题。** 在上述输入下，存在绝对常数 \(\varepsilon>0\)，使
\[
\boxed{\mathcal J(g)+\left(\frac{T}{A}-\frac23\right)_+
\ge\varepsilon.}
\tag{N1}
\]
常数不依赖直径、非塌缩、Sobolev 常数、点态曲率或驻点方程。

这将旧公式中的 \(\mathcal E\) 加强为 \(\mathcal J\)，并使用负 Yamabe 代表上的单解输入。不声称继承旧常数的数值或得到最佳常数。

**证明。** 以下中间积分均在 ghat 上，令
\[
V=\operatorname{Vol}_{\widehat g}(M),\qquad
r=\frac{P(\widehat g)}{V},\qquad
d=\left(\frac{T}{A}-\frac23\right)_+.
\]
续研报告附录06证明：I51 的有限参数估计只需这一普通实际解。I51(2.15) 在 \(a^2\ge T\) 时去掉类平方成本，给出
\[
r+\frac{D_\beta}{\beta V}
\ge c_0\frac{(\beta-2)^2}{\beta^4},\qquad
D_\beta=(1+\beta^{-1})\int s^2
       +6(\beta+1)\int|W^+|^2-72\pi^2p.
\]
取 \(\beta=8\)，记 \(c_8=9c_0/1024>0\)，则
\[
r+\frac{D_8}{8V}\ge c_8. \tag{N2}
\]
第07卷 functional pencil 的精确 Chern–Weil 恒等式为
\[
D_8=108\pi^2(T-2p/3)+\frac{27}{2}P. \tag{N3}
\]
该式也可由
\[
4\pi^2T=\frac1{24}\int s^2+2\int|W^+|^2-\frac12P
\]
乘以27直接核对。

单解标量预算与 \(s_{\widehat g}=-4\) 给
\[
16V\ge32\pi^2p\ge32\pi^2A,\qquad
\frac{A}{V}\le\frac1{2\pi^2}.
\]
又 \(T-2p/3\le Ad\)，所以
\[
\frac{D_8}{8V}\le\frac{27}{4}d+\frac{27}{16}r.
\]
与(N2)合并：
\[
\frac{43}{16}r+\frac{27}{4}d\ge c_8. \tag{N4}
\]

在 ghat 上 \(R=P+4V\)，因此
\[
\mathcal J(\widehat g)=\frac{4r}{r+4}.
\]
I41 精确共形比较给
\[
\mathcal J(g)\ge\min\{\mathcal J(\widehat g),1\}. \tag{N5}
\]
具体地，令
\[
\delta=\int_gs_g^2-\int_{\widehat g}s_{\widehat g}^2\ge0.
\]
则 \(P(g)-P(\widehat g)=\delta/12\)，
\(R(g)-R(\widehat g)=\delta/3\)，故 \(\mathcal J(g)\) 是
\(\mathcal J(\widehat g)\) 与1的加权平均。

若 \(\mathcal J(g)\ge1\)，结论直接成立。否则
\[
\mathcal J(\widehat g)\le\mathcal J(g)<1,\qquad
r=\frac{4\mathcal J(\widehat g)}{4-\mathcal J(\widehat g)}
\le\frac43\mathcal J(g).
\]
由(N4)，
\[
c_8\le\frac{43}{12}\mathcal J(g)+\frac{27}{4}d
\le\frac{27}{4}\bigl(\mathcal J(g)+d\bigr).
\]
取 \(\varepsilon=\min\{1,4c_8/27\}\)，即得(N1)。证毕。

## 3. 严格继承及统一的范围

- \(\mathcal E\ge\mathcal J\)，故(N1)恢复原统一积分障碍，并将支付落实到无迹 Ricci。
- 一般型手术应用有 \(T=A-k-4\ell\)，因此在原对应实际供给下
  \[
  \mathcal J(g)+\left(\frac13-\frac{k+4\ell}{A}\right)_+
  \ge\varepsilon.
  \]
- 原稿四类对应应用继续通过其实际供给代入：LeBrun 相关手术障碍、Kotschick special monopole 条件、Ishida–LeBrun 的 BF 连通和供给、Ishida–Matsuo–Nakamura 的 Pin-minus 供给。经典非消失和预算仍是输入。
- Pin-minus 的既有双覆盖提升使 p、a²、T、A、P、R、V 同乘2，归一化 J、E 不变。提升后的负 Yamabe 代表上有普通实际解，故证明可在覆盖上进行再下降，常数不损失。不要求覆盖上的所有非不变度量都有供给。
- I40/I41 的另一共同核心仍是
  \[
  \Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\quad
  (p-T)_+\le C_T\{\Pi+\sqrt{\Pi Y}\},
  \]
  \[
  \Sigma=\int s^2-32\pi^2p,\quad
  \Pi=P+D_2,\quad Y=(T-a^2)_+.
  \]
  类平方条件已能按 Y 量化放宽。这与另一手性预算给小 h 线性窗口。

统一核心因此可以同时包含：单解有限参数机制、beta=8 的原临界拓扑障碍，以及 beta=2 附近的精细线性强制。这里证明的是明确继承，不是宣称所有历史公式均已由一条最短定理推出。

## 4. 四项适用范围与继承核查

### 4.1 旧供给确实推出负 Yamabe 和新单解输入

旧供给要求所选同一实际结构在整个待测共形类上可解，并且 \(p\ge A>0\)。若该类的 Yamabe 代表有非负常标量曲率，实际普通解的 Weitzenböck 恒等式使自旋子为零，进而 \(F_A^+=0\)；其非零调和投影与 \(p>0\) 矛盾。因此旧供给的每一个待测共形类必为负。将唯一负 Yamabe 代表常数缩放至 \(s=-4\)，旧供给仍给实际解；再常数缩放自旋子即可使用本文权重2规范。\(p,a^2,T\) 不变。

所以新输入真正兼容全部所列旧应用，不是把旧适用范围偷偷缩小。不同共形类可以选择不同的结构，仍须分别验证 \(p\ge A>0\) 并共用应用所需的统一 \(A\)。本论证不从某一共形类的一个解自动产生其他共形类上的解。

Pin 型供给按真实双覆盖提升先变成普通解；归一化负 Yamabe 代表由唯一性保持 deck invariance。前述证明在覆盖上进行后下降，不要求覆盖上的所有非不变度量或任意非不变权重均有解。详见第07卷Source8 §§1–2、第05卷Source2 Part I §5。

### 4.2 正预算、Ricci-flat 和零预算边界

本文始终要求 \(p\ge A>0\)。普通一般型、BF与Pin应用必须使用各自实际供应链验证该条件，不能凭一个形式特征类或拓扑平方替代实际解。

在 Ricci-flat 度量上 \(R=0\)，所以 \(\mathcal J=4P/R\) 不定义；原定义却给 \(\mathcal E=4\)，不是零。因此排除 Ricci-flat 不能通过把它代入 \(\mathcal J=0\) 或 \(\mathcal E=0\) 完成。旧实际正投影供给独立给
\[
\int s_-^2\ge32\pi^2p\ge32\pi^2A>0,
\]
故排除 Ricci-flat。新逐共形类版本明确要求负 Yamabe 类，同样不包含一个 Ricci-flat 度量所在的零 Yamabe 类。本文的全度量应用必须保留这项逐类假设及其来源。

LeBrun 手术应用的 \(T_X>0\) 范围已经严格回接。\(T_X=D=0\) 的零预算、零手术角点不能冒称一般 Einstein 非存在；K3 可承载 Ricci-flat 度量。\(T_M<0\) 的排除则由 Chern–Weil 独立给出，不依赖本文正预算规范输入。来源：第07卷Source1 §8、Source9 “Theorem 3.3: the positive budget and the zero corner”。

### 4.3 类平方短缺范围已经有定量扩展

第2节 N1 使用 \(a^2\ge T\)。这不是任意实际解自动满足的条件。第5节现证明，在相同负 Yamabe 单解与 \(p\ge A>0\) 条件下，允许
\[
y=\frac{(T-a^2)_+}{A}\ge0
\]
并得到
\[
\mathcal J(g)+(T/A-2/3)_+\ge\frac{c}{1+y}.
\]
因此 \(y\le L\) 的统一 \(c/(1+L)\) gap 已完成，不再列作开放问题。该常数依赖及 \(y\to\infty\) 时的退化保留在结论里，不宣称任意短缺下无损常数，也不宣称这个依赖最优。

I40/I41 已有的另一短缺式
\[
\Sigma,(p-T)_+\le C\{P+D_2+\sqrt{(P+D_2)(T-a^2)_+}\}
\]
继续保留，其小 \(h\) 后果为 \(c h^2/(h+y)\)。它与第5节的原临界阈值短缺版是互补输出，不能混用误差尺度。

### 4.4 BF 完整经典预算的缺口不影响本文证明

第09卷原审读§五已对明确供给的符号集合
\[
\mathcal C_0=\{\pm c_1(X_1)\pm c_1(X_2)+\sum_i\pm E_i\}
\]
核得经典凸包及正子空间优化预算均为 \(A\)。I41 真实 BF 线性窗口因此严格超出这整组已知类给出的所列经典预算，而不只是超出单个粗预算。

但 \(\mathcal C_0\) 不一定是所有实际 monopole 类。若完整预算为 \(B=A(1+\delta)\)，经典 Einstein 必要条件可能已经提高为 \(1+h+2\delta\le U\)。尚未上控的 \(O(Ah)\) 增量可能影响“这些具体光滑类型首次被排除 Einstein”的历史优先性判断。精确到 \(o(Ah)\) 的完整预算上控仍未完成。

这不影响 N1、短缺版或 I40/I41 的证明：它们只要求供给一个满足展示预算的实际解，而不要求已经列尽所有解或所有 monopole 类。本文定位为实际参数机制对原积分障碍的严格加强，不以未知完整类预算宣称独立历史首创性。

## 5. 类平方短缺版：完整证明

**带 \(1/(1+y)\) 损失的N1已经由保留类平方成本的I51直接推出；其最佳短缺依赖仍未确定。** 不声称任意短缺下都保持无损绝对gap。

沿用N1的负Yamabe单解输入与 \(p\ge A>0\)，但不要求 \(a^2\ge T\)。在标量 \(-4\) 的代表上置
\[
Y=(T-a^2)_+,\quad y=Y/A,\quad b=(-a^2)_+/V,\quad
r=P/V,\quad d=(T/A-2/3)_+.
\]
第01卷Source2§2.3式(2.15)的保留成本版本及单解附录06给
\[
(1+b)\left(r+\frac{D_8}{8V}\right)\ge c_{8,\mathrm{raw}}>0.
\]
Chern–Weil与单解标量预算分别给
\[
\frac{(-T)_+}{V}\le\frac{r}{8\pi^2},\qquad
\frac AV\le\frac1{2\pi^2}.
\]
故
\[
b\le\frac{(-T)_++Y}{V}
\le\frac r{8\pi^2}+\frac y{2\pi^2}.
\]
若原度量 \(\mathcal J(g)<1\)，精确共形比较使
\(r\le4\mathcal J(g)/3<4/3\)，从而
\[
1+b\le1+\frac1{6\pi^2}+\frac y{2\pi^2}.
\]
N1中不依赖类平方条件的 \(D_8\) 上界仍为
\[
r+\frac{D_8}{8V}
\le\frac{43}{16}r+\frac{27}{4}d
\le\frac{27}{4}(\mathcal J(g)+d).
\]
因此
\[
\boxed{
\left(1+\frac1{6\pi^2}+\frac y{2\pi^2}\right)
(\mathcal J(g)+d)\ge\frac{4c_{8,\mathrm{raw}}}{27}.}
\]
对 \(\mathcal J(g)\ge1\) 分支直接取较小常数。置
\[
c=\min\left\{1,
\frac{4c_{8,\mathrm{raw}}}{27(1+1/(6\pi^2))}\right\},
\]
即在所有上述输入下得到
\[
\boxed{
\mathcal J(g)+\left(\frac TA-\frac23\right)_+
\ge\frac{c}{1+y},\qquad y=\frac{(T-a^2)_+}{A}.}
\]
若逐共形类供给可统一保证 \(y\le L\)，便有统一下界 \(c/(1+L)\)。\(\mathcal E\ge\mathcal J\) 给对应积分障碍；Pin提升使 \(Y,A\) 同倍缩放，\(y\) 不变，故同式下降。该推论只使用已写出的I51成本式、单解输入、Chern–Weil及共形恒等式；不使用新的供给定理，不宣称短缺依赖最优。

## 6. 证明依赖与完成状态

- 第07卷Source1 Theorem1.2与§§8–10：旧积分障碍、全部Einstein符号与Ricci-flat独立排除、实际极化应用。
- 第07卷Source3 §8：\(D_8\) 的精确 Chern–Weil 恒等式，旧临界校准是参数族的 \(\beta=8\) 成员。
- 第01卷Source2 §2.3式(2.15)：保留 \(b_a\) 成本的有限参数估计及 \(a^2\ge T\) 下的去成本版本。
- 第05卷Source2 Part I §§1–3：负 Yamabe 归约、精确共形比较及 I41 线性强制；§5：cover-compatible 与 Pin 下降。
- 同日续研报告附录06 §§1–4：一个负 Yamabe 代表上的实际解足够证明有限参数与线性估计。
- 第09卷原审读§五：已知 BF 符号集合优化及完整类预算的精确比较缺口。

第2节原 N1 已在先前统一补充稿中由主会话及独立核查检查过常数、恒等式、共形比较与量词。第5节短缺版在本轮另行核对了保留成本式、\((-T)_+/V\) 界、两条 \(\mathcal J\) 分支及覆盖缩放。有限代数复核不替代上述参数估计的 PDE 证明。

本文完成的是：在原实际供给范围及更弱单解合同下，保留原临界积分障碍、加强为无迹 Ricci 支付，并允许明确的有界类平方短缺。一般零 Weyl 端点 O10、原平衡族最佳首项 O11、完整 BF 类预算及严格超出旧供应链的新实际对象，均不是本文已完成的结论。
