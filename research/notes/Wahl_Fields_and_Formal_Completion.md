# Wahl 退化中的实际规范场与形式延拓

*Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen, Yihao Yang · Qiushi Engine Team, Zhejiang University. [Authors and correspondence](../../AUTHORS.md).*

本节研究光滑四流形上的实际 Seiberg–Witten 解在有理球收缩中的极限，以及奇点处的等变字符能够强迫什么。结论分为场与能量的转移、局部指标、强迫零点和形式延拓。最后的形式结论针对给定度量上的辅助场方程。

## 1. 几何、规范与供给条件

设 $V$ 是紧定向四维轨形，唯一奇点的局部群为
$$
\Gamma=\frac1{n^2}(1,n-1)\subset U(2),\qquad n\ge2.
$$
以 Wahl 有理球 $B_{n,1}$ 替换锥邻域，得到光滑流形 $M$。取该球上的 Ricci-flat Kähler ALE 度量 $h$，在外部固定轨形度量 $g$ 上插入 $\epsilon^2h$。以 $\rho=\epsilon^{2/3}$ 为过渡半径，可使恢复度量 $g_\epsilon$ 满足
$$
g_\epsilon=g\quad(r\ge2\rho),\qquad
\sup|s_{g_\epsilon}|\le C_g,\qquad
\operatorname{Vol}_{g_\epsilon}\{r<R\}\le C_g(\rho^4+R^4).
\tag{1}
$$
曲率界来自过渡区的
$\rho^{-2}[\rho^2+(\epsilon/\rho)^4]=O(1)$。常数允许依赖固定背景。

设有限个 Spin$^c$ 结构组成集合 $\mathcal S$。对每个恢复度量，至少一个结构提供未扰动解，且
$$
p_\epsilon=(a^+_{g_\epsilon})^2\ge A_0>0.
\tag{2}
$$
这里 $a$ 是该结构行列式线丛的第一 Chern 类。本节使用行列式联络 $A$，规范为
$$
D_A\Phi=0,\quad F_A^+=q(\Phi),\quad
|q(\Phi)|^2=\tfrac18|\Phi|^4,
\quad4\nabla_A^*\nabla_A\Phi+s\Phi+|\Phi|^2\Phi=0.
\tag{3}
$$
这一旋量规范与间隙专题的规范相差常数重标 $\Phi_{\mathrm W}=\sqrt2\,\Phi_{\mathrm G}$；行列式联络和拓扑类不变。
若要对 $V$ 的每个轨形度量应用以下结论，条件（2）必须对各自恢复族成立。例如，光滑 $M$ 上对全部度量有效的有限单极子类集合提供这种输入。单独一族上的供给不蕴含其他度量上的供给。

## 2. 场极限与能量转移

**命题 1.** 在（1）—（3）下，任意 $\epsilon_j\to0$ 的序列存在子列，使所选 Spin$^c$ 结构固定，解经规范变换在 $V^{\rm reg}$ 上光滑局部收敛，并延拓为 $V$ 上的光滑轨形解。若 $a_V$ 是其行列式类，则
$$
a_V^2=a_M^2,\qquad
\int_M|\Phi_j|^4\longrightarrow\int_V|\Phi_\infty|^4
\ge32\pi^2A_0,
\tag{4}
$$
$$
\int_M|F_{A_j}|^2\longrightarrow\int_V|F_{A_\infty}|^2,
\qquad
\int_M|\nabla_{A_j}\Phi_j|^2
\longrightarrow\int_V|\nabla_{A_\infty}\Phi_\infty|^2.
\tag{5}
$$

**证明。** 有限性先固定结构。对 $U=|\Phi|^2$，（3）的最大值原理给 $0\le U\le C_g$。因而
$$
\limsup_{j\to\infty}\int_{r<R}U_j^2\le C_gR^4.
\tag{6}
$$
同时，调和投影与 Chern–Weil 公式给
$$
\int U_j^2=8\int|F_{A_j}^+|^2\ge32\pi^2p_j,
\quad
\int|F_{A_j}^-|^2=\int|F_{A_j}^+|^2-4\pi^2a_M^2.
\tag{7}
$$
积分 Weitzenböck 恒等式控制 $\nabla_A\Phi$。在正规部分使用局部 Coulomb 规范及椭圆正则性得到光滑子列；（6）排除旋量质量在奇点丢失。

可去奇点只需如下阿贝尔论证。将极限拉回穿孔球，令 $F=-iF_A\in L^2$。在半径 $\delta$ 的截断上，$\|d\chi_\delta\|_2=O(\delta)$，所以 $dF=0$ 分布成立于整个球。由球的 $H^1=H^2=0$，存在
$$
a'\in W^{1,2},\qquad da'=F,\quad d^*a'=0,\quad\iota_\nu a'=0.
$$
原联络与 $A_0+ia'$ 相差恰当形式。若差为 $i\,df$，行列式规范变换 $u=e^{if/2}$ 消去它。旋量仍有界，故 Dirac 方程右端属于 $L^4$。依次有
$$
\Phi\in W^{1,4},\quad a'\in W^{2,4}
\subset C^{0,\alpha}\cap W^{1,p}\quad(p<\infty),
$$
再取 $p>4$ 迭代，得到光滑延拓。Coulomb 解的唯一性使其保持 $\Gamma$-等变性；实原函数在有限群作用下的常数差构成 $\Gamma\to\mathbb R$ 的同态，故为零。延拓保持原 Spin$^c$ 提升，偶数 $n$ 时也保留完整提升而非仅行列式字符。

有理球和锥都没有实二阶上同调，球面空间形式边界没有实一、二阶上同调。因此正规部分的配对确定 $a_V$，且平方不变。（6）与局部收敛先转移 $F_A^+$ 能量；再由（7）转移全曲率能量。最后使用
$$
4\int|\nabla_A\Phi|^2=-\int sU-\int U^2
$$
及过渡区体积趋零，得到（5）。$\square$

这里转移的是实际解及指定能量。对每个共形代表重新使用实际供给，才可进一步应用共形曲率估计；未扰动 SW 方程本身没有所需的简单共形协变性。

## 3. 手性、指标与可延拓字符

令 $d=1-n^{-2}$，以曲率积分定义轨形 Euler 数和签名。替换有理球后
$$
\chi_{\rm orb}(V)=\chi(M)-d,
\quad\tau_{\rm CW}(V)=\tau(M)+\tfrac23d.
$$
因此
$$
T_+^{\rm orb}=T_+(M),\qquad
T_-^{\rm orb}=T_-(M)-4d.
\tag{8}
$$
多个奇点时各项求和。正手性拓扑预算不变，反手性预算发生变化。

相对于典范提升，边界 Spin$^c$ 结构由 $m\in\mathbb Z/n^2\mathbb Z$ 标记。能延拓过有理球的扭转为 $m=nj$。对这些结构，光滑与轨形 Dirac 指标相等。可由 APS 分解证明：边界为正标量曲率的球面空间形式，其平坦扭转 Dirac 算子无核；有理球上的平坦行列式联络与 Ricci-flat 度量使 $D^2=\nabla^*\nabla$。端部指标根在所用权重区间中没有穿越，衰减核与余核均为零。锥帽采用正标量曲率填充，得到相同的零相对指标。

局部固定点项给出独立的代数表达。取 $p=n^2$、$\zeta=e^{2\pi i/p}$，令
$$
\delta(m)=\frac1p\sum_{r=1}^{p-1}
\frac{\zeta^{rm}}{(1-\zeta^{-r})(1-\zeta^{-r(n-1)})}.
$$
用有限 Fourier 恒等式
$$
H(a)=\frac1p\sum_{r=1}^{p-1}\frac{\zeta^{ra}}{1-\zeta^{-r}}
=\frac{p-1-2a}{2p}\quad(0\le a<p)
$$
可得 $\delta(m)-\delta(m-1)=H([-(n+1)m]_p)$。写 $m=an+b$、$0\le a,b<n$、$c=n-a-1$，求和后
$$
2n^2[\delta(an+b)-\delta(0)]=
\begin{cases}
b[(n+1)b+2na-n(n-1)],&b\le c,\\
(b-n)[(n+1)b-2nc],&b>c.
\end{cases}
\tag{9}
$$
对奇数 $n$，可能的非零根须使 $n+1$ 整除 $2(a+1)$ 或 $2c$；唯一内部候选落在相反的分支。对偶数 $n$，$\gcd(n,n+1)=1$ 同样排除内部根。于是
$$
\delta(m)=\delta(0)\iff m\in n\mathbb Z/n^2\mathbb Z,
\qquad\delta(0)=\frac{1-n^{-2}}{12}.
\tag{10}
$$
指标相等不等于完整 SW 不变量、模空间或局部字符均相同；这些对象还涉及全局粘合。

## 4. 强迫零点与正预算的同时保留

对奇数 $n\ge3$，正旋量在奇点的两个权为 $nj,n(j-1)$。若 $2\le j\le n-1$，则没有不变常旋量；余切权 $\pm1,\pm(n-1)$ 也不能抵消这些权。因此实际解满足
$$
\Phi(p_0)=0,\qquad\nabla_A\Phi(p_0)=0.
\tag{11}
$$

局部群还限制曲率的代数形式。对 $n\ge3$，$\Lambda^+_0$ 分成权为 $0,\pm n$ 的实线与复线；$\operatorname{Sym}^2_0\Lambda^+_0$ 的非零权为 $\pm n,\pm2n$。因此在适配基下
$$
W^+(p_0)=\mu\,\operatorname{diag}(2,-1,-1),
$$
所有不变自对偶二形式均沿零权方向。这个点态结论没有规定 $\mu$ 与标量曲率的关系，也不蕴含邻域可积性。$n=2$ 时权 $2n$ 已为零，不适用该一维不变子空间结论。

在具有标记 $(-4)$-球 $E_1-E_2-E_3-E_4$ 的指定光滑构造中，取保持相对典范提升的有理球嵌入。设 $h=2^{-1}\pmod n$。符号类 $-K_M+2\sum_{i\in F}E_i$ 的局部扭转为
$$
j_F=h\bigl(-1_{1\in F}+1_{2\in F}+1_{3\in F}+1_{4\in F}\bigr)\pmod n.
\tag{12}
$$
强迫零点的子集在取补集下保持不变，符号向量的平均为零。因而在这些类同时实际供给时，投影平方平均仍至少为主体预算 $A_0$，可以只在强迫零点的子集中选择满足（2）的类。

对每个固定轨形度量，遂有严格标量估计
$$
\int_V(s^-)^2>32\pi^2A_0.
\tag{13}
$$
否则经典标量估计链的等号迫使旋量平行；（11）又迫使其恒为零，与（4）矛盾。这个严格性没有自动给出与度量无关的正改进量。

若另有负 Einstein 度量，写 $s=-\lambda$、$U=|\Phi|^2$。由（3），
$$
0\le U\le\lambda,\qquad
\lambda^2V-\int U^2
=8\int|\nabla_A\Phi|^2+\int(\lambda-U)^2.
\tag{14}
$$
在受控坐标半径 $r_0$ 上，（11）与椭圆估计给出的局部代价具有量纲
$c\lambda^2r_0^4/n^2$。全局统一估计需要控制无量纲尺度 $\lambda r_0^2$，并将这个代价与同一场的 Weyl 和调和投影预算结合。

## 5. 等变 Dirac 首项与任意阶形式延拓

固定一个光滑 $\Gamma$-不变度量，取正则坐标与同步标架。与上述权相容的平坦 Dirac 算子为
$$
D_0^+=\begin{pmatrix}
\partial_{z_1}&\partial_{\bar z_2}\\
-\partial_{z_2}&\partial_{\bar z_1}
\end{pmatrix}.
\tag{15}
$$
对奇数 $n\ge3$ 和强迫扭转 $2\le j\le n-1$，非零等变齐次单调和旋量的最低次数为
$$
\ell_{\min}=2\min\{j-1,n-j\}.
\tag{16}
$$
事实上，单项式 $z_1^az_2^b\bar z_1^c\bar z_2^d$ 的权为 $P-Q+nQ$，其中 $P=a-c,Q=b-d$。若次数小于 $n$ 且权被 $n$ 整除，则 $P=Q=r$，次数至少 $2|r|$。两个分量分别要求 $r\equiv j,j-1\pmod n$。下界由
$$
\bigl(0,(z_1z_2)^{j-1}\bigr)
\quad\text{或}\quad
\bigl((\bar z_1\bar z_2)^{n-j},0\bigr)
$$
达到，它们都被（15）消去。这给出次数限制，不决定实际解的首项幅度。

**命题 2.** 对任意上述固定度量的允许 Taylor 展开，以及任一允许的非零首项 $P_\ell\in\ker D_0^+$，辅助 SW 方程在等变 Coulomb 规范中存在以 $P_\ell$ 开始的形式解。每阶的齐次 Dirac 核和反自对偶联络核可以自由指定。

**证明。** 写 $A=A_0+a$、$\Phi=\sum\Phi_k$、$a=\sum_{k\ge1}a_k$。度量的正则坐标展开为 $g=e+O(r^2)$，连接零阶系数为 $O(r)$，且群作用没有不变常一形式。在次数 $k-1$ 上，未知的 $k$ 次项仅通过
$$
\mathcal L_0(\Phi_k,a_k)=
\bigl(D_0^+\Phi_k,\ d_0^*a_k\oplus\sqrt2d_0^+a_k\bigr)
\tag{17}
$$
出现；度量修正、$a\cdot\Phi$ 和 $q(\Phi)$ 都由较低次数决定。

取非负平坦 Laplacian $\Delta_0=-\sum\partial_i^2$。有
$$
D_0^+(D_0^+)^*=\tfrac14\Delta_0,
\qquad
(d^*\oplus\sqrt2d^+)(d^*\oplus\sqrt2d^+)^*=\Delta_0.
$$
Fischer 分解给齐次多项式上 $\Delta_0:\mathcal P_{k+1}\to\mathcal P_{k-1}$ 的右逆 $G$。故（17）有右逆
$$
\mathcal L_0^*\operatorname{diag}(4G,G,G).
$$
在有限群上平均可使其等变，保留实联络条件。逐阶施加右逆并加入自由核，便完成递归。Borel 引理再给出使方程残差在原点无限阶消失的光滑等变场。$\square$

命题 2 排除了这套辅助系统的有限阶可解性障碍。它没有证明级数收敛、邻域中的精确解或全局实际类中的延拓。Einstein–almost-Kähler 的联立变形方程另有度量与二形式的耦合条件，不能由本命题替代。

## 6. 与 Einstein 存在性问题的连接

以下复实现采用奇数 $n\ge3$ 的标记 $(-4)$-球分支，或 $n=2$ 的标记 $(-3)$-球分支。其收缩链为 $[n+2,2,\ldots,2]$，差异系数为 $a_i=-(n-i)/n$。若一条 $(-1)$-曲线横截第 $i$ 个分量一次，则其像满足
$$
K_V\cdot C=-1-a_i=-i/n<0.
$$
所以这一复结构的典范类不 nef。实际场转移还将正手性的标量和 Weyl 障碍传给 $V$；反手性量则必须按（8）重新计算。

这些结果把一个退化候选约束为：有指定实际场、指定局部字符与指标的负 Einstein 轨形。要排除该候选，仍须将局部零点或填充信息转化成超过剩余曲率预算的全局估计。形式首项的可解性、逐度量的严格标量不等式和统一正间隙在这里具有不同的数学内容。

## 文献

- I. Şuvaina, [*ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities*](https://arxiv.org/abs/1102.2672)：有理平滑的 Ricci-flat Kähler ALE 模型及有限商结构。
- H. Park, J. Park and D. Shin, [*Smoothly embedded rational homology balls*](https://arxiv.org/abs/1508.03724)：指定有理球嵌入、相对标记及复模型。
- 本节的实际类供给、归一化曲率估计及其共形量词见[间隙与端点](../../docs/GAPS_AND_ENDPOINTS.md)；曲率积分在解消中的手性变化及全局极值见[曲率变分](../../docs/CURVATURE_VARIATION.md)。

