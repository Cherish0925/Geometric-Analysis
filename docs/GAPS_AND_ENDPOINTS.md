# 积分 Einstein 间隙、端点与双取向应用：研究导航

本导航连接原积分障碍、N1、I40/I41、有限密度 O10、无密度续研及双取向应用。依据下列原稿中的定理陈述、证明依赖和后续修订整理；状态指归档原稿实际写出的数学内容。原始证明与修订稿均应保留。本文件不替代证明正文，也不构成对全部前置分析的独立认证。

## 1. 共同对象与实际输入

设 $M$ 为闭、连通、定向光滑四流形。统一记号为


$$
T_+=2\chi(M)+3\tau(M),\quad
P(g)=\int_M|\operatorname{Ric}^{\circ}_g|^2,\quad
R(g)=\int_M|\operatorname{Ric}_g|^2,
$$


$$
\mathcal J(g)=\frac{4P(g)}{R(g)},\qquad
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|^2}
{\lambda^2\operatorname{Vol}_g(M)}.
$$


项目 Weyl 范数是二形式曲率算子的 Hilbert–Schmidt 范数；Ricci 使用二张量范数。不同规范之间的常数不得直接拼接。

共同分析使用负 Yamabe 共形类中归一化为 $s_{\widehat g}=-4$ 的代表，以及该代表上的一个实际普通 Seiberg–Witten 解


$$
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi).
$$


其同一 Spin$^c$ 结构的类 $a=c_1(L)$ 满足投影预算


$$
p=(a_g^+)^2=(a_{\widehat g}^+)^2\ge A>0.
$$


这是逐共形类输入。全度量结论需要每个共形类都有所需供给及统一预算；不同共形类可选择不同结构，每次推导中的实际解、$p$ 和 $a^2$ 必须属于同一结构。

原供给若在整个待测共形类上成立，正投影预算与 SW–Weitzenböck 恒等式排除非负 Yamabe 代表。普通、special monopole、BF、Pin$^{-}$ 是不同实际供给来源，不以形式特征类替代非消失定理。Pin$^{-}$ 分支使用真实双覆盖上的普通解；提升底空间负 Yamabe 代表、按覆盖次数缩放各积分与拓扑平方后下降，归一化量不变。无需覆盖上所有非不变度量都有供给。

在 $R>0$ 时有 $\mathcal E\ge\mathcal J$。Ricci-flat 度量满足 $R=0$，此时 $\mathcal J$ 不定义，而原 $\mathcal E$ 定义给出 $4$。有关 Einstein 非存在性的应用以正实际标量预算另行排除 Ricci-flat，不将其代入 $\mathcal J=0$。

入口：[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1、4；较早版本为 [Qiushi_Line1_Unified_Gap_20260928.md](../archive/originals/2026-09-28/Qiushi_Line1_Unified_Gap_20260928.md)。两版均在归档中保留，后者不是类平方短缺问题的最后状态。

## 2. 原积分障碍、N1 与 I40/I41 的连续关系

### 2.1 N1 是原积分障碍的严格加强

参数泛函为


$$
D_\beta=(1+\beta^{-1})\int s^2
 +6(\beta+1)\int|W^+|^2-72\pi^2p.
$$


在上述单解输入及 $a^2\ge T_+$ 下，I51 有限参数估计给出


$$
\frac{P(\widehat g)}V+\frac{D_\beta(\widehat g)}{\beta V}
\ge c_0\frac{(\beta-2)^2}{\beta^4}.
$$


$\beta=8$ 处 Chern–Weil 的精确连接是


$$
D_8=108\pi^2(T_+-2p/3)+\frac{27}{2}P.
$$


配合实际标量预算及精确共形转移，原稿得到


$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\varepsilon_N>0.}
\tag{N1}
$$


按该有限参数常数可取 $\varepsilon_N=\min\{1,c_0/768\}$，不是最佳常数。

共形转移不是小扰动估计。若


$$
\Delta S=\int_gs_g^2-\int_{\widehat g}s_{\widehat g}^2\ge0,
$$


则 $P(g)=P(\widehat g)+\Delta S/12$、$R(g)=R(\widehat g)+\Delta S/3$，故 $\mathcal J(g)$ 是 $\mathcal J(\widehat g)$ 与 $1$ 的加权平均，特别


$$
\mathcal J(g)\ge\min\{\mathcal J(\widehat g),1\}.
$$


$\mathcal E\ge\mathcal J$ 随即恢复旧的


$$
\mathcal E(g)+\left(\frac{T_+}{A}-\frac23\right)_+\ge\varepsilon_N.
$$


这里的连续关系是“共同参数分析 → 无迹 Ricci 间隙 → 原积分间隙”，不再仅仅将新旧公式并列。四类经典应用在各自实际供给、正预算和符号范围内代入；经典非消失理论仍是输入。

### 2.2 后续 N1 已允许有界类平方短缺

[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §5 保留 I51 中的类平方成本，删除 $a^2\ge T_+$，令


$$
y=\frac{(T_+-a^2)_+}{A}.
$$


得到


$$
\boxed{\mathcal J(g)+\left(\frac{T_+}{A}-\frac23\right)_+
\ge\frac{c}{1+y}.}
\tag{N1-Y}
$$


其输入仍是负 Yamabe 代表上的同一实际解及 $p\ge A>0$。因此 $y\le L$ 范畴的统一间隙 $c/(1+L)$ 已有原稿证明。早期“短缺控制尚不能接到 N1”的文字应作为历史状态保留；它已被这一推论更新。无界短缺下是否存在无损常数、最优短缺依赖，仍未由此确定。

### 2.3 I40/I41 保留精细线性作用

置


$$
\Sigma=\int s^2-32\pi^2p,\quad
\Pi=P+D_2,\quad Y=(T_+-a^2)_+.
$$


原稿的强制估计为


$$
\Sigma\le C\{\Pi+\sqrt{\Pi Y}\},\qquad
(p-T_+)_+\le C_T\{\Pi+\sqrt{\Pi Y}\}.
\tag{I41}
$$


它来自相容背景作用的消去、有界场的 Hessian 控制、剩余联络能量和同场弱 Bianchi 测试。$Y=0$ 时 $\Sigma\le C(P+D_2)$；拓扑偏离不能仅由标量超额承担而使其余缺陷降到二阶。

与所列另一手性预算结合，在相应窗口得到


$$
\mathcal J+(U-1-h)_+\ge ch.
$$


原平衡族正确线性阶由此成立。N1 的 $\beta=8$ 输出与 I40/I41 的 $\beta=2$ 精细输出共享分析，但不能互相省略。I41 的小 $h$ 短缺后果 $ch^2/(h+y)$ 与 N1-Y 的原临界阈值结论也是不同输出。

原稿定位：[00_Line1_Research_Atlas_20260928.md](../archive/originals/2026-09-28/00_Line1_Research_Atlas_20260928.md) §§1、3.1–3.4；[03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§2–6；[Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md)；旧卷定位见上述继承稿末节。

## 3. O10：从有限参数到任意固定有限密度

O10 的目标量是


$$
\kappa_\beta(g)=\fint_M|\operatorname{Ric}_g+g|^2
 +\frac{D_\beta(g)}{V_g}.
$$


它不同于前节有限参数估计的 $P/V+D_\beta/(\beta V)$。在 $s=-4$ 代表上，第一项才化为 $P/V$。

### 3.1 现有有限密度结论

[O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§1–4 陈述并给出证明链：在原实际共形供给、$p\ge A>0$、$a^2\ge T_+$ 下，任意固定有限 $B$ 存在 $c_{\rm FD}(B)>0$，使


$$
\boxed{\frac{\chi(M)}A\le B\quad\Longrightarrow\quad
\kappa_\beta(g)\ge c_{\rm FD}(B)
\frac{(\beta-2)^2}{\beta^2},\qquad\beta\ge2.}
\tag{FD}
$$


该结论不另加点态 Ricci、直径、非塌缩、注入半径或统一 Sobolev 控制。[O10_Finite_Density_Complete_Proof.tex](../archive/originals/2026-09-29/O10_Finite_Density_Complete_Proof.tex) 汇集主证明与直接前置，适合沿完整依赖阅读。

### 3.2 证明中的新连接

1. **实际正旋量的强流输入。** [O10_Strong_Current_Prerequisite.md](../archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md) 的慢梯度截断建立正旋量四次梯度的一致可积性，继而升级实际三次扭率 $\tau\in S^-\otimes L$、Dirac 残差、同场曲率拟合及首阶类型投影。此层不要求 Euler 密度界；它没有同时证明负旋量所有高阶临界量一致可积。
2. **同丛有界辅助截面。** [O10_Direct_Resolvent_Prerequisite.md](../archive/originals/2026-09-29/O10_Direct_Resolvent_Prerequisite.md) 用固定幅度截断 $T(\tau)$ 及
   
$$
(4+\nabla^*\nabla)v=6T(\tau)
$$

   得到有界 $v$、有界粗 Laplacian、$v-\tau\to0$ 于归一化 $H^1$，以及 $(\nabla^*\nabla-2)v\to0$。它是同一丛中的辅助截面，不是另一个 SW 解。
3. **有限密度所提供的导数预算。** $b=\fint|W^-|^2\le C_B$ 给 $\|\nabla v\|_4+\|\nabla^2v\|_2\le C_B$。质量—相位—Dirac 的直接约化只留下一个复导数分量；协方差测试给 $q=|\nabla v|^2\to2m_*$ 于测度，$m_*=128/81$。见 [O10_Weak_Bianchi.md](../archive/originals/2026-09-29/O10_Weak_Bianchi.md)。这条直接证明避免了早期 Nijenhuis 括号的伴随测试，保留早期 [O10_Resolvent_Prolongation.md](../archive/originals/2026-09-29/O10_Resolvent_Prolongation.md) 作为另一条推导记录。
4. **第五幂线丛。** 构造
   
$$
\sigma=\Phi\wedge t(v)\in\Gamma(L^5),\qquad
   |\sigma|^2\to4\rho_*m_*^3>0,\quad\rho_*=4/3.
$$

   同时得到 $\sigma$ 的归一化 Dirichlet 预算。线丛次数来自 $t(v)\in S^+\otimes L^4$ 和 $\det S^+=L$。
5. **全局矛盾。** 秩一线丛的对数 resolvent 正则化与 transgression 给
   
$$
c_1(L^5)^2[M]/V\to0,
$$

   而同一实际曲率预算给
   
$$
c_1(L^5)^2[M]/V=25a^2[M]/V\to25/(6\pi^2)>0.
$$

   线丛引理及更一般闭二形式配对见 [O10_Topological_Escape.md](../archive/originals/2026-09-29/O10_Topological_Escape.md)；实际应用见 [O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) §§2–3。

另一终端路线保留完整相位，取得 $L^5$ 上的弱 CR 关系及 $\nabla^*\nabla+10/3$ 的正势对偶矛盾，见 [O10_Finite_Density_Fifth_Line.md](../archive/originals/2026-09-29/O10_Finite_Density_Fifth_Line.md)。两条路线共享强流和实际场前置，是同一有限密度定理的不同完成方式。

有限参数估计排除有界 $\beta$ 的反例子列；原稿共形比较


$$
\widehat\kappa_\beta\le
\frac{\kappa_\beta}{1-\sqrt{\kappa_\beta}-\kappa_\beta/16}
$$


将小缺陷反例转到 $s=-4$ 代表，从而接回全部原允许度量。

### 3.3 阈值与常数的版本关系

| 原稿阶段 | 获得内容 | 后续使用 |
|---|---|---|
| [O10_Critical_Density.md](../archive/originals/2026-09-29/O10_Critical_Density.md) | $\chi/A<3/8$ 的较短端点论证 | 保留短证明，不再作为最大已知范围 |
| [O10_Strengthened_Endpoint.md](../archive/originals/2026-09-29/O10_Strengthened_Endpoint.md) | 谱超额、$39/4$ 临界密度及正宽度 | 历史加强，已被任意有限 $B$ 范围覆盖 |
| [O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md) | 每个固定有限 $B$ 的 FD | 当前有限密度主入口 |
| [O10_Quantitative_Escape_and_O11_Boundary.md](../archive/originals/2026-09-29/O10_Quantitative_Escape_and_O11_Boundary.md) | 增长能量的对数陈数约束及指数型密度依赖 | 保留独立引理与速率推导 |
| [O10_Primitive_Rate_Audit.md](../archive/originals/2026-09-29/O10_Primitive_Rate_Audit.md) | 原始缺陷与实际误差之间的幂次转接，结合 D 轮正势排除给多项式依赖 | 使用全部所列前置及准确误差定义 |

最后一项令 $x=\kappa_\beta+\beta^{-2}$、$\gamma=\epsilon_0/(1+\epsilon_0)$，将 D 轮完整实际误差（含 $H^1$ 与 $L^4$ 转移）控制为


$$
\mathfrak e_D\le Cx^{\gamma/16}.
$$


结合 [O10_Alternative_Global.md](../archive/originals/2026-09-29/O10_Alternative_Global.md) 的


$$
\mathfrak e_D(1+b)^{3/2}\to0\quad\Longrightarrow\quad
\text{不存在该端点序列},
$$


得到 $x\ge c(1+b)^{-24/\gamma}$，并接出某个普适有限指数 $N$ 的


$$
c_{\rm FD}(B)\ge c_0(1+B)^{-N}.
$$


这项速率转接以 R1 和 D 轮第五线丛排除为前置；$x$、不同原稿中的 $\eta$ 与 $\mathfrak e_D$ 不得仅凭符号相近视为同一误差。

## 4. N1 与 FD 的地理分区：已扩展到若干无界密度族

[Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §2（亦见 [04_Uniform_Endpoints_and_Tower_Recovery.tex](../archive/originals/2026-10-07/04_Uniform_Endpoints_and_Tower_Recovery.tex)）给出后续整合，不应遗漏。

若原允许对象构成的族满足


$$
Q:=A-T_+\ge0,\qquad \chi(M)\le CA+Q,
$$


其中 $C<\infty$ 固定，则


$$
\kappa_\beta\ge c_{\rm geo}(C)\frac{(\beta-2)^2}{\beta^2},\quad
c_{\rm geo}(C)=\min\{\varepsilon_N,c_{\rm FD}(C+1/3)\}>0.
\tag{GEO}
$$


证明分区：$Q/A\ge1/3$ 时 N1 直接给正间隙；$Q/A<1/3$ 时只需固定密度 $C+1/3$ 的 FD。整族可以有无界 $\chi/A$，但其地理关系是实质输入。

对供给已验证的极小复一般型主体 $X$，$A=c_1^2(X)>0$，Noether 估计给 $\chi(X)\le35A$。因此


$$
M=X\#k\overline{\mathbb{CP}}^{,2}\#\ell(S^1\times S^3),\quad
Q=k+4\ell,\quad \chi(M)\le35A+Q
$$


有与主体、手术数、度量、参数无关的常数


$$
c_* =\min\{\varepsilon_N,c_{\rm FD}(106/3)\}.
$$


多主体版本使用 $A=\sum_i c_1^2(X_i)$、$Q=k+4\ell+4(r-1)$，同样成立于实际普通/BF 供给已验证的具体连通和。此推导没有新建任意连通和的非消失定理，也未覆盖所有辛一般型或零平方主体。

原平衡族本来已有 $\chi/A\le1/3+h$；其端点不再是开放事项。GEO 进一步处理手术数不限的所列地理范畴，但不等于一般无密度 O10。

## 5. 无密度 O10：保留的结果、确切剩余与更正

一般目标仍是原全部实际输入下，存在不依赖 $\chi/A$ 的绝对 $c>0$。FD、速率排除和 GEO 没有共同覆盖所有允许对象。

### 已取得的无密度信息

[O10_Unbounded_Density.md](../archive/originals/2026-09-29/O10_Unbounded_Density.md) 与 [O10_Double_Weighted_Test.md](../archive/originals/2026-09-29/O10_Double_Weighted_Test.md) 处理原正旋量低幅度区、容量和合法带权测试。[O10_Low_Amplitude_Energy_and_O11_Scope.md](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md) 进一步只用有界 $v$、有界粗 Laplacian、近特征截面及小首阶类型投影，证明：令 $m=|v|^2\to m_*$、$q=|\nabla v|^2$，则固定 $0<\theta<1$、$\varepsilon>0$ 时


$$
\limsup_j\fint\frac{q_j}{(m_j+\varepsilon)^\theta}
\le\frac{2m_*}{(1-\theta)(m_*+\varepsilon)^\theta},
$$


$$
\limsup_j\fint_{\{m_j\le t\}}q_j
\le2et\log(m_*/t),\qquad0<t<m_*/e.
$$


它排除最深低幅度区承载固定梯度能量，不要求 $W^-$ 预算。极限顺序先固定权重参数，再令 $j\to\infty$；它不自动给任意选择的 $\varepsilon_j\downarrow0$ 的统一误差估计。

### 仍未闭合的连接

中间幅度层 $0<a<m_j<b<m_*$ 可在体积趋零时保留径向能量。现有结论不推出 $dm_j\to0$，也未在无密度范畴同时取得第五线丛截面的固定截断正质量和完整弱方程。这两者缺一不能组成端点矛盾。

[O10_Alternative_Global.md](../archive/originals/2026-09-29/O10_Alternative_Global.md) §8 保留完整径向项后给出


$$
b=d\,\theta_1+c\,\theta_2,\qquad
d=-\frac{m_3+i m_4}{2m},
$$


正手性非对角曲率中的相关径向项精确相消；不能以该投影另行控制径向导数。整族标量矩与形式能量测度 $d\nu_q=2dt$、$d\nu_R=4t\,dt$ 相容；此形式模型也满足逆幅度矩估计。因此重复标量权重不足以排除它。该模型不是满足全部实际方程的闭流形反例。

[O10_Local_Model_And_Prolongation_Audit.md](../archive/originals/2026-09-29/O10_Local_Model_And_Prolongation_Audit.md) 另行修正构造入口：不能使用同时满足 $\operatorname{Ric}=-g$、$W^+=0$、$d\omega=0$、$|\omega|^2=2$ 的局部 almost-Kähler 主体；其经典局部障碍与缩小双曲球上的实际 SW 核心是不同陈述。后者没有提供固定正体积的完整端点主体或闭流形匹配。

保留的开放项是完整实际径向—相位—曲率系统对集中缺陷的约束，或满足原全部供给、拓扑与过渡条件的真实闭流形逃逸。不能从“每个有限 $B$ 有 $c(B)>0$”直接取出跨全部 $B$ 的统一常数。

## 6. 双取向、Kodaira 斜率与后续配对推广

### 6.1 FD2 是不可省略的解析前置

[Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md)（2026-10-07）与 [06_Two_Orientation_Global_Gap.tex](../archive/originals/2026-10-07/06_Two_Orientation_Global_Gap.tex) 调用 FD 在固定 $B=2$ 的特例，记为 **FD2**。其同一实际类 $c$ 必须满足


$$
(c^+)^2\ge A_c>0,\quad c^2\ge T_+,\quad\chi/A_c\le2.
$$


下游双取向推论不重新证明 FD2 的 R1、强流、辅助截面或线丛分析；也不能反向作为这些前置的证明。

### 6.2 全曲面丛范畴的间隙

对光滑定向曲面丛 $\Sigma_f\to M\to\Sigma_b$，$f,b\ge2$，原稿在 FD2 前置下证明


$$
\boxed{\mathcal J(g)+\left(1-\frac{3|\tau(M)|}{\chi(M)}\right)_+
\ge\varepsilon_{\rm SB},\qquad
\varepsilon_{\rm SB}=\left(\frac{\min\{1,c_{\rm FD}(2)\}}{200}\right)^2.}
\tag{SB}
$$


常数统一于亏格、单值、总空间及全部光滑度量。

连接来自同一 Hodge 极化中的两个真实类。写 $e=\chi$，取 $x=e(\pi^*T\Sigma_b)$、$y=e(T_{\rm vert}M)$，则


$$
x^2=0,\quad xy=e,\quad y^2=3\tau,
\quad a=x+y,\quad b=x-y,
$$


$$
a^2=2e+3\tau,\quad b^2[M]=-2e+3\tau,\quad ab=-3\tau.
$$


Thurston 与 Taubes 提供相应双取向实际类；反取向 $b^+>1$ 在近临界分支内另有检查。若 $d=\mathcal J(\widehat g)+(1-3\tau/e)_+$ 很小，交叉配对使反取向投影足够大，并给


$$
A_-=e(2-3\tau/e)>0,\quad e/A_-<2,\quad
\bar\kappa_{d^{-1/2}}<100\sqrt d.
$$


FD2 给同一量至少为 $\min\{1,c_{\rm FD}(2)\}/2$，从而推出 SB。这里不需要一般无密度 O10，也不使用 O11 最优值。

Einstein 情形给 $3|\tau|\le(1-\varepsilon_{\rm SB})\chi$。对具有经典负 KE 度量的光滑 Kodaira 纤维化，$c_1^2=2\chi+3\tau$、$c_2=\chi$，得到


$$
\boxed{c_1^2/c_2\le3-\varepsilon_{\rm SB}.}
$$


这是 FD2 依赖下对统一上端分离问题的推导；不是最佳斜率计算，也不证明 $8/3$ 最优。经典背景及问题出处在原稿末节：Kotschick `math/9911255`、LeBrun `math/0005195`、Catanese–Rollenske `math/0611428`；[00_All_Recent_Research.tex](../archive/originals/2026-10-07/00_All_Recent_Research.tex) 的相关章另列 Catanese `1611.06617` §1.3 与 Polizzi `2002.01363` Remark 4.10。

### 6.3 10 月 8 日一般双取向配对定理

[00_Results_and_Proof.md](../archive/originals/2026-10-08/00_Results_and_Proof.md) §1 与 [Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) 将 SB 推广到一般闭四流形。令 $e=\chi>0$，选取 $\tau\ge0$。设 $\mathcal C_+$ 是正取向有限组真实全度量单极子类，


$$
a\in\operatorname{Hull}(\mathcal C_+),\quad a^2\ge T_+;
$$


反取向有真实类 $b$，满足 $b^2[\bar M]\ge T_-=2e-3\tau$。记 $t=3\tau/e$、$z=|ab|/e$。在 FD2 前置下，


$$
\boxed{\mathcal J(g)+(1-t)_++(t-z)_+\ge\varepsilon_{\rm pair},}
$$


其中 $\varepsilon_{\rm pair}=\varepsilon_{\rm SB}$。正取向一侧仅通过凸性使用标量预算，不需凸组合本身有 SW 解；FD2 始终作用于真实反取向类 $b$。

有限反取向实际类集合可对允许的 $(a,b)$ 最大化 $|ab|/e$，得到有限维配对优化。辛形式对 $TM=E_1\oplus E_2$ 的特例附加项为


$$
\frac{2}{e}\bigl(\min\{e(E_1)^2,e(E_2)^2\}\bigr)_+.
$$


这项推广依赖双取向真实供给及混合相交数据，未凭空给一般吹起流形制造反取向单极子类。

## 7. 后续阅读与不可混用的状态

| 阅读目的 | 原始文件及定位 |
|---|---|
| 原 gap、N1、单解与短缺继承 | [03_N1_Complete_Inheritance.md](../archive/originals/2026-09-28/03_N1_Complete_Inheritance.md) §§1–6；[00_Line1_Research_Atlas_20260928.md](../archive/originals/2026-09-28/00_Line1_Research_Atlas_20260928.md) §3 |
| I40/I41 与旧卷来源 | [Yau26_Line1_External_Review_20260927.md](../archive/originals/2026-09-27/Yau26_Line1_External_Review_20260927.md)；上述 Atlas 及继承稿的精确卷、Source、节号 |
| 强流前置 | [01_O10_Strong_Current.md](../archive/originals/2026-09-29/01_O10_Strong_Current.md)；[O10_Strong_Current_Prerequisite.md](../archive/originals/2026-09-29/O10_Strong_Current_Prerequisite.md) |
| 有界同丛 resolvent | [O10_Direct_Resolvent_Prerequisite.md](../archive/originals/2026-09-29/O10_Direct_Resolvent_Prerequisite.md) |
| 质量、相位、Dirac 与第五幂截面 | [O10_Weak_Bianchi.md](../archive/originals/2026-09-29/O10_Weak_Bianchi.md)；历史第一延拓 [O10_Resolvent_Prolongation.md](../archive/originals/2026-09-29/O10_Resolvent_Prolongation.md) |
| 有限密度主证明及附录 | [O10_All_Finite_Density.md](../archive/originals/2026-09-29/O10_All_Finite_Density.md)；[O10_Finite_Density_Complete_Proof.tex](../archive/originals/2026-09-29/O10_Finite_Density_Complete_Proof.tex) |
| 第五线正势路线 | [O10_Finite_Density_Fifth_Line.md](../archive/originals/2026-09-29/O10_Finite_Density_Fifth_Line.md)；[O10_Alternative_Global.md](../archive/originals/2026-09-29/O10_Alternative_Global.md) |
| 对数陈数与原误差速率 | [O10_Topological_Escape.md](../archive/originals/2026-09-29/O10_Topological_Escape.md)；[O10_Quantitative_Escape_and_O11_Boundary.md](../archive/originals/2026-09-29/O10_Quantitative_Escape_and_O11_Boundary.md)；[O10_Primitive_Rate_Audit.md](../archive/originals/2026-09-29/O10_Primitive_Rate_Audit.md) |
| 无密度集中与有效更正 | [O10_Unbounded_Density.md](../archive/originals/2026-09-29/O10_Unbounded_Density.md)；[O10_Double_Weighted_Test.md](../archive/originals/2026-09-29/O10_Double_Weighted_Test.md)；[O10_Low_Amplitude_Energy_and_O11_Scope.md](../archive/originals/2026-09-29/O10_Low_Amplitude_Energy_and_O11_Scope.md)；[O10_Local_Model_And_Prolongation_Audit.md](../archive/originals/2026-09-29/O10_Local_Model_And_Prolongation_Audit.md) |
| 地理分区与统一手术族 | [Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md](../archive/originals/2026-10-07/Line1_Uniform_Endpoint_and_Residual_Tower_Recovery.md) §2；[04_Uniform_Endpoints_and_Tower_Recovery.tex](../archive/originals/2026-10-07/04_Uniform_Endpoints_and_Tower_Recovery.tex) |
| 双取向与 Kodaira | [Line1_Two_Orientation_Global_Gap.md](../archive/originals/2026-10-07/Line1_Two_Orientation_Global_Gap.md)；[06_Two_Orientation_Global_Gap.tex](../archive/originals/2026-10-07/06_Two_Orientation_Global_Gap.tex) |
| 一侧凸包、配对短缺及辛形式对推广 | [00_Results_and_Proof.md](../archive/originals/2026-10-08/00_Results_and_Proof.md) §1；[Pair_Gap_and_Pinched_Example.tex](../archive/originals/2026-10-08/Pair_Gap_and_Pinched_Example.tex) |
| 连续汇编入口 | [00_Collected_Research.tex](../archive/originals/2026-10-07/00_Collected_Research.tex)；[00_All_Recent_Research.tex](../archive/originals/2026-10-07/00_All_Recent_Research.tex) 及其同名版本 |

阅读时须保留四个层次：经典实际供给；项目核心 PDE 估计；依赖这些估计的应用；未完成的全局连接。N1、I40/I41、FD、GEO、SB 与一般配对定理属于相互衔接但不相互替代的节点。

完整 BF 类预算仍与“所供给符号类的预算”分开；普通手术族后续预算计算不自动完成所有 BF 应用族的比较。O11 已在相应构造族上获得严格低于标准系数 $4$ 的上界，故旧档案中的“证明首项必为 $4$”不能当作这些族的现行目标。无密度 O10、O11 匹配最优值及精确 Einstein 实现仍是不同问题，不能由 FD2 或 Kodaira 推论互相代替。
