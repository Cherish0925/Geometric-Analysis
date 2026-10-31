# 负 Einstein 几乎 Kähler 几何：成果与继续点

本导引依据已收录的完整数学原稿，连接 10 月 8 日的显式构造、10 月 9—14 日的零点与刚性分析，以及 10 月 15 日的两会话合并。下列结论的证明、规范和计算证书均以所列原稿为准。

## 研究对象与共同问题

在闭、连通、定向四维流形上，给定

$$
\operatorname{Ric}_g=-ag,\quad a>0,\qquad d\Omega=0,\quad |\Omega|_g^2=2,
$$

取向由 $\Omega$ 决定。负 Goldberg 问题要求证明 $\nabla\Omega=0$，或构造满足这些完整条件的非 Kähler 例子。

研究同时保留两种信息：实际 Einstein 方程对 Weyl 曲率的微分约束，以及实际闭二形式对几乎复结构、规范曲率和拓扑的约束。局部结构、闭流形的整体关系和显式非紧构造在同一问题中相互检验。

## 已形成的主要数学内容

| 内容 | 原稿中的结论 | 证明入口 |
|---|---|---|
| 完整非紧严格几乎 Kähler–Einstein 构造 | 完整 $\mathbb R^4$ 上 $\operatorname{Ric}=-3g$、$W^-=0$、$d\Omega=0$、$\vert \Omega\vert ^2=2$、$\vert \nabla\Omega\vert ^2>0$；度量非齐性 | [Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) §§1–4；[Q4_independent_cartan.py](../archive/originals/2026-10-08/Q4_independent_cartan.py) |
| 扭率零点结构 | 零点处精确 Hessian–Weyl 恒等式、复线性／反线性正规形、非负实行列式；横截零点指数为 $+1$ | [Q4_Torsion_Zero_Structure.tex](../archive/originals/2026-10-09/Q4_Torsion_Zero_Structure.tex) §§1–4；[Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) §2 |
| 规范正交关系 | 横向 Weyl 形式与全部闭实 $J$-反不变形式 $L^2$ 正交；正积分因子若存在即推出 Kähler | [Q4_Canonical_Orthogonality.tex](../archive/originals/2026-10-12/Q4_Canonical_Orthogonality.tex) §§1–3 |
| 固定度量的调和乘积表示 | 相容几乎 Kähler 形式精确对应一个线性核中的正、迹一、秩一矩阵；平行分支由经典唯一性定理处理 | [Q4_Harmonic_Product_Reduction.tex](../archive/originals/2026-10-13/Q4_Harmonic_Product_Reduction.tex) §§1–4 |
| 行列式符号刚性 | $\det(W^+-aI/3)\le0$ 处处成立时，给定相容形式平行 | [Q4_Determinant_Sign_Rigidity.tex](../archive/originals/2026-10-13/Q4_Determinant_Sign_Rigidity.tex) §§1–4 |
| Green 势刚性 | 行列式的正势逆算子像在一个扭率零点非正，即推出全局 Kähler | [Q4_Green_Potential_Rigidity.tex](../archive/originals/2026-10-14/Q4_Green_Potential_Rigidity.tex) §§1–4 |
| 零曲线与完整 Weyl 方程 | 排除紧致干净二维零分支；规则零曲线全测地；保留法向导数的非齐次方程和 Weyl 横向块的完整耦合 | [Goldberg_Global_Connections_20261015.tex](../archive/originals/2026-10-15/Goldberg_Global_Connections_20261015.tex) 与 [Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex](../archive/originals/2026-10-15/Goldberg_Torsion_Zeros_and_Weyl_Equation_20261015.tex) 正文 |
| 两会话严格回接 | 谱重根位置与二阶扭率消失等价；符合条件的闭零曲线必经过该位置；Green 配对中的全局项仍保留 | [Goldberg_Two_Conversations_Merged_20261015.tex](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex) §§3–6 |

### 1. 完整非紧构造及 Fino 问题

原研究系统 A01 给出显式度量与二形式；[Q4_Complete_Example_and_Fino_Question.tex](../archive/originals/2026-10-08/Q4_Complete_Example_and_Fino_Question.tex) 补充全曲率计算、端点光滑延拓、完整性、非齐性以及文献问句的对应。

结构方程为

$$
d\sigma_1=-2\sigma_2\wedge\sigma_3,\quad
d\sigma_2=2\sigma_3\wedge\sigma_1,\quad
d\sigma_3=2\sigma_1\wedge\sigma_2.
$$

在 $1/3<x<1$ 上的显式系数延拓到
$\mathrm{SL}(2,\mathbb R)\times_{\mathrm{SO}(2)}\mathbb R^2\to\mathbb H^2$，总空间微分同胚于 $\mathbb R^4$。其中

$$
|\nabla\Omega|^2=\frac{36(1-x^2)^3}{(1+3x^2)^3}>0.
$$

零截面处该值为 $32/3$；另一端距离无限。完整性并非只由正规开区间上的公式推断。

该例回答原稿所引 Fino 2005 年论文 Corollary 2.1 之后的问句：实四维 Lie 群是否承载非不变、非 Ricci-flat、严格几乎 Kähler 的 Einstein 度量。这里使用 $(\mathbb R^4,+)$ 的光滑流形结构，度量不要求平移不变。原稿分别说明：这是该问句的肯定例子；完整性是额外性质；不据此宣称历史首创；它是非紧无限体积例，未回答闭负 Goldberg。

此例还检验了方法的真实边界：负 Einstein 与非可积性可以在完整非紧几何中共存，纯局部消失论证不能由方程本身推出。

### 2. 扭率零点与拓扑

令

$$
q=|\nabla\Omega|^2,\quad n=\Omega/\sqrt2,\quad
W^+=\begin{pmatrix}t&v^*\\v&-tI/2+B\end{pmatrix},
\quad t=s/6+q/4,\quad \eta=\sqrt2v,\quad \operatorname{tr}B=0.
$$

在 $Z=\{q=0\}$ 上，原稿得到

$$
|\nabla^2\Omega|^2=4|B|^2-6|\eta|^2.
$$

局部写 $\nabla\Omega=\vartheta\otimes\phi-J\vartheta\otimes J\phi$，则 $q=4|\vartheta|^2$。在扭率零点，导数正规形为

$$
D\vartheta(z)=cz+Q\bar z,\qquad
\operatorname{tr}(Q\bar Q)=-8|c|^2,
$$


$$
\det_{\mathbb R}D\vartheta=9|c|^4+|\det_{\mathbb C}Q|^2\ge0.
$$

这里 $\bar Q$ 为逐项共轭，不是 Hermitian 伴随。横截零点指数为 $+1$；全部零点横截时，数量为 $5\chi+6\tau$。奇异导数的实秩只可能为 $0$ 或 $2$。

Armstrong 的经典拓扑论证保证闭、非零标量 Einstein 情形 $Z\ne\varnothing$：Nijenhuis 丛的第二陈数为 $5\chi+6\tau>0$。正指数与该正陈数相容，不能据此产生矛盾。

10 月 15 日原稿进一步排除紧致干净二维零分支。若闭光滑零曲线的秩二点稠密，则它全测地，其法向扭率导数是 $\bar K^{\otimes2}|_C$ 的截面，度数为

$$
\frac{s}{4\pi}\operatorname{Area}(C)<0.
$$

因此法向导数必在某处消失。其实际方程仍为非齐次关系 $D^{1,0}\zeta=r$，其中 $r$ 来自法向曲率导数；在规定条件下 $D^{1,0}r=0$。这不使 $\zeta$ 自动成为全流形上的闭反不变二形式。

### 3. 两会话合并后的关键恒等式

统一取

$$
\mathcal R_+=W^+-aI/3,\quad A=-\mathcal R_+,\quad
U=\sigma_2(A)=a^2/3-|W^+|^2/2,
$$


$$
L_a=\Delta+2a,\quad
\Psi=L_a^{-1}\det\mathcal R_+,\quad
\mathcal D=L_a^{-1}|\nabla A|^2,
$$

其中 $\Delta=-\operatorname{div}\nabla$。Einstein Weyl 方程给出

$$
L_aU=|\nabla A|^2-18\det\mathcal R_+,\qquad U=\mathcal D-18\Psi.
$$

连接零点局部恒等式后，对每个 $p\in Z$，

$$
\boxed{18\Psi(p)=\mathcal D(p)+\frac18|\nabla^2\Omega(p)|^2+\frac54|\eta(p)|^2.}
$$

由于 $L_a^{-1}$ 的 Green 核严格为正，若一个零点满足 $\Psi(p)\le0$，则 $\nabla A\equiv0$，继而 $A=a\,n\otimes n$、$\nabla\Omega=0$。全局条件 $\det\mathcal R_+\le0$ 蕴含该条件。

设 $\Sigma$ 是 $W^+$ 最大两个特征值相等的位置，则

$$
Z\cap\Sigma=\{\nabla\Omega=0,\ \nabla^2\Omega=0\}.
$$

上述闭光滑零曲线必经过该交集；但在交点仍有

$$
18\Psi(p)=\int_MG_a(p,y)|\nabla A(y)|^2\,dV_y.
$$

因此“零集与谱重根集相交”尚不等于“Green 势刚性条件成立”。任何闭非 Kähler 候选都必须在每个扭率零点具有 $\Psi>0$，并在某个开集具有 $\det\mathcal R_+>0$。

### 4. 其他可用的整体联系

**规范正交。** 对每个闭实 $J$-反不变二形式 $\alpha$，

$$
\int_M\langle\eta,\alpha\rangle\,dV=0.
$$

若存在全局光滑 $f>0$ 使 $d(f\eta)=0$，则 $\eta=0$，再由经典紧致第三 Gray 定理得到 Kähler。原稿的显式非紧例满足 $d\vartheta_\eta\ne0$，所以这种积分因子不能仅从局部方程获得。

**调和乘积。** 对固定闭度量，在平均正交规范的自对偶调和基中，令 $G_{ab}(x)=\langle\psi_a,\psi_b\rangle$、$B_g=G-I$，定义

$$
\mathsf C_g(X)=\fint\langle B_g,X\rangle B_g.
$$

相容形式精确对应 $\ker\mathsf C_g$ 中正、迹一、秩一矩阵；不能删去秩一条件。若已有平行自对偶形式，di Scala–Nagy 的经典唯一性定理处理该分支。一般 Einstein 度量所实现的调和乘积核仍须研究。

**Einstein 变形。** 在闭几乎 Kähler–Einstein 情形，令 $u=|\nabla\Omega|^2$，有

$$
s^2\operatorname{Vol}-32\pi^2(2\chi+3\tau)
=\frac32\int u^2+16\int|B|^2.
$$

归一化 Einstein 光滑路径的体积不变，故从同取向 Kähler–Einstein 度量出发的路径上，任何相容几乎 Kähler 成员仍为 Kähler。没有据此识别所有 Einstein 模空间连通分支。

**联络变分。** 固定 $\Lambda^+$ 分裂，$A=D_0+C$ 时，$A_t=D_0+tC$ 满足

$$
\operatorname{YM}(A_t)=\operatorname{YM}(A)+2(1-t^2)^2\|F_{D_0}^-\|_2^2.
$$

这说明 Yang–Mills 极小性容许非零非对角项；该路径未被证明是实际度量的 Levi-Civita 联络路径。

## 必须保留的订正与范围

- 非紧完整例与闭负 Goldberg 是不同命题。构造及其 Fino 对应保留，闭问题仍未完成。
- 一点扭率消失、二阶消失、有限阶 Einstein jet 相容，都不等于无限阶消失或唯一延拓。10 月 15 日程序构造的是 $\operatorname{Ric}+g=O(|x|^6)$ 的相容度量，不是精确 Einstein germ。
- Weyl 横向块满足完整耦合方程
  
$$
D^*DB+(3s/2+2u)B
  =2\sum_i[p_i(D_i\zeta)^T+(D_i\zeta)p_i^T]_0+2(\zeta\zeta^T)_0.
$$

  不能删去右端后改用齐次正势消失论证；$s<0$ 时零点处势本身为负。
- 调和范数方差在 Kähler 方向附近是四阶，导数能量是二阶；原稿已否定相应线性强制估计。正半定矩阵可行性也不等于秩一可行性。
- 零曲线的法向截面不自动是全纯截面；其指数可为负。紧致干净零曲线被排除，但秩下降曲线及孤立零点仍可能存在。
- Watson 的几乎 Hermitian 浸没刚性、di Scala–Nagy 唯一性、第三 Gray 定理、Armstrong 零点存在性、经典 Weyl–Weitzenböck 与 Sekigawa 公式均作为既有输入署名，不能重复登记为新结论。

## 当前继续研究的精确问题

在原始闭负 Einstein 与几乎 Kähler 假设下，取得能排除以下共同情形的新整体约束：扭率有零点，但每个零点的行列式 Green 势严格为正；局部零点结构、规范曲率、完整 Weyl 耦合和调和乘积仍全部相容。当前原稿给出多种充分刚性条件和显式构造，尚未证明这些条件对任意闭候选自动成立，也未构造闭反例。

最新直接入口为 [Goldberg_Two_Conversations_Merged_20261015.tex](../research/packages/Goldberg_Two_Conversations_Merged_20261015--5a0ab1f2/Goldberg_Two_Conversations_Merged_20261015.tex)；查局部与曲线证明分别读两份 10 月 15 日正文；查 Green 正性读 10 月 14 日稿；查存在性构造与 Fino 问句读 10 月 8 日完整例子稿。各份源文件及程序应共同保留。
