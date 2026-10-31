# 03 卷审计与新增替换引理

本笔记只审计 03 卷 I54 / I55 / X10；把已继承的 I40 / I41、全度量实际供给以及标准缩核恢复作为前提，不把交接稿当成这些前提的独立证明。

## 1. 结论

1. X10 构造的固定参数、标量为 -4 的 `N/Q<1` 序列，逻辑上可成立；它的成本严格高于 4，因此确实击破“竞争性自动给 N≥Q-o(Q)”，没有击破“真正近极小性给选择/补偿”。
2. X10 Proposition 2 的有限变分计算正确；它只排除固定 C4 紧族的正密度出现，不提供退化族的统一下降率。
3. 可把这条近极小排除加强为下述**任意退化完整单元的正超额消失引理**。它无需单元度量预紧、曲率上界、单元拓扑取有限种，甚至无需总单元体积 O(Q)。只需待考虑单元的 CH 参考帽总体积 `D=o(A)`。
4. 该引理没有建立 O11：它排除正超额，却不能排除 `P_C<8π²q_C` 的负超额。补偿式本身仍严格等价于未知的 `P≥8π²Q-o(Q)`，并未因 N/Z 分解变成较弱命题。

## 2. 新引理：任意退化单元的总正超额必须消失

设同一原始平衡族上的 `g_j` 满足

\[
s_{g_j}=-4,\qquad \mathcal E(g_j)-\alpha_j=o(h_j),\quad
\alpha_j=\inf_g\mathcal E(g),\quad h_j=Q_j/A_j\to0.
\]

继承结论给出

\[
P_j=O(Q_j),\quad V_j=2\pi^2 A_j+O(Q_j),\quad
R_j=4V_j+P_j,\quad \mathcal E(g_j)=4P_j/R_j.
\]

取任意有限个两两不交的标记完整单元

\[
C_{ij}=D_{ij}\#k_{ij}\overline{\mathbb {CP}}^2
                  \#\ell_{ij}(S^1\times S^3),
\qquad q_{ij}=k_{ij}+4\ell_{ij}>0,
\]

每个单元外侧一个开 collar 与相应 CH 帽的整个度量 germ 精确相同。允许几何、帽的半径、单元个数及其拓扑随 j 改变。记

\[
d_{ij}=\operatorname{Vol}(D_{ij}),\quad
v_{ij}=\operatorname{Vol}_{g_j}(C_{ij}),\quad
p_{ij}=\int_{C_{ij}}|\operatorname{Ric}^{\circ}|^2.
\]

假设

\[
D_j:=\sum_i d_{ij}=o(A_j).
\]

则

\[
\boxed{\sum_i(p_{ij}-8\pi^2q_{ij})_+=o(Q_j).}
\tag{A}
\]

### 2.1 单元体积条件自动得到

I54 (1.1)，03 卷约 54–68 行，在 `s=-4` 下给出精确式

\[
p_{ij}=8\pi^2q_{ij}+\frac43v_{ij}
                         +4W_{ij}-4d_{ij},
\qquad W_{ij}=\int_{C_{ij}}|W^+|^2.
\tag{B}
\]

因此对任意所选子集

\[
\sum v_{ij}\le\frac34\sum p_{ij}+3\sum d_{ij}
\le\frac34P_j+3D_j=o(A_j).
\tag{C}
\]

无需另外假设总实际单元体积小，更不需要其为 O(Q)。

### 2.2 替换比较与所有尺度

只替换 `p_{ij}>8π²q_{ij}` 的单元。对这组单元置

\[
B_j=\sum_i(p_{ij}-8\pi^2q_{ij})>0,\quad
w_j=\sum_i(d_{ij}-v_{ij}).
\]

有 `B_j≤P_j=O(Q_j)`，`Σq_{ij}≤P_j/(8π²)=O(Q_j)`，由 (C) 得 `w_j=o(A_j)`。

在每个单元内实施原稿已使用的标准缩核恢复，保留整个外 collar。对每个固定 j，单元数量及拓扑有限，可以把恢复参数取到任意小；**不需要关于 j、帽半径或 q 的统一速率**。对角选择使所有误差之和为 `o(Q_j)`。帽内极限矩为

\[
V_{\rm ref}=d,\qquad I_{\rm ref}=-4d,\qquad
R_{\rm ref}=4d+8\pi^2q.
\tag{D}
\]

于是新闭度量仍在同一光滑流形上，且

\[
V'_j=V_j+w_j+o(Q_j),\quad
I'_j=-4(V_j+w_j)+o(Q_j),
\]
\[
R'_j=4(V_j+w_j)+P_j-B_j+o(Q_j).
\tag{E}
\]

式 (D) 是需要继承标准恢复的唯一构造输入。混合 `k` 个 blowups 与 `ℓ` 个 handles 时，曲率成本为 `8π²(k+4ℓ)`，不是只对纯 blowup 使用。

暂忽略可任意缩小的恢复误差。定义

\[
\mathcal E'_0=\frac{4(P-B)}{4(V+w)+P-B}.
\]

直接相减，而不进行一般三变量 Taylor 展开，得到

\[
\boxed{\mathcal E'_0-\mathcal E
=-\frac{16(VB+Pw)}{(4V+P)[4(V+w)+P-B]}.}
\tag{F}
\]

特别地，令 `R'_0=4(V+w)+P-B`，则有第二个精确式

\[
\boxed{\mathcal E'_0-\mathcal E+\frac{4B}{R}
=\frac{4(4Bw+BP-B^2-4Pw)}{R R'_0}.}
\tag{G}
\]

由于 `P,B=O(Q)`、`w=o(A)`、`R,R'_0∼8π²A`，

\[
\mathcal E(g'_j)-\mathcal E(g_j)
=-\frac{4B_j}{R_j}
+O\!\left(\frac{Q_j|w_j|+Q_j^2}{A_j^2}\right)+o(h_j)
=-\frac{4B_j}{R_j}+o(h_j).
\tag{H}
\]

`o(Q)` 恢复矩误差造成 `o(Q/A)=o(h)` 的泛函误差，因为新旧 V、R 仍都与 A 可比。

近极小性和 `α_j≤E(g'_j)` 推出 `4B_j/R_j≤o(h_j)`，故 `B_j=o(Q_j)`，即 (A)。

### 2.3 为什么这里不需要平方根尺度

若仅知道不相关的矩变化绝对值 `O(m_j)`，则通用 Taylor 余项确为

\[
O\!\left(\frac{h_jm_j}{A_j}+\frac{m_j^2}{A_j^2}\right),
\]

要求其为 `o(h)` 的简单充分条件是 `m_j=o(√(A_jQ_j))`。

标准恢复的矩却满足 `ΔI=-4ΔV+o(Q)`、`ΔR=4ΔV-B+o(Q)`。这些相关性使纯 `w²/A²` 项消掉，精确余项只有 `(Q|w|+Q²)/A²`。因此 (A) 只需 `w=o(A)`，由 `D=o(A)` 自动保证。不要把通用 Taylor 的平方根阈值当成本引理的限制。

### 2.4 一个不需 w=o(A) 的校正版本

若 `V+w` 仍与 A 可比但 w 可以达到 A 级，(F) 表明真正被近极小性排除的是

\[
\left[B_j+\frac{P_j}{V_j}w_j\right]_+=o(Q_j).
\tag{I}
\]

对具体一组可替换单元，这是精确的“曲率超额加体积校正”量。若 w=o(A)，第二项自动为 o(Q)，恢复 (A)。宏观体积变化不能无条件丢弃。

## 3. X10 实际构造核查

### 3.1 径向核心的成本可独立算出

03 卷约 2000–2096、2104–2162 行。记

\[
F_\mu=1+\frac{r^2}{6}-\frac{c}{2r^2}+\frac{\mu^3}{3r^4},
\quad c=\mu(\mu+2),\quad r_0=\sqrt\mu.
\]

代入原稿 Ricci 特征值式得

\[
r_v=-1-c/r^4,\qquad r_h=-1+c/r^4,
\qquad s=2r_v+2r_h=-4.
\]

于是 `|Ric+g|²=4c²/r⁸`，用 `dV=2π²r³dr`，在固定 R 处截断：

\[
J_{[r_0,R]}=2\pi^2c^2(\mu^{-2}-R^{-4})
=8\pi^2+8\pi^2\mu
 +2\pi^2\mu^2\{1-(\mu+2)^2/R^4\}.
\tag{J}
\]

所以固定足够小 μ 时，内核已严格高于 `8π²`。再取足够小扰动幅 a 可保持此严格差；外面增加非负 J 能量不会破坏它。这独立验证了 X10 的 `J_C>8π²`。

负特征质量的原函数为

\[
\mathcal B=q^2+(2+q)r^2F\phi'^2,
\quad q=2F+rF'/2+rF\phi'-2.
\]

未扰动时 `q_0=(r²-c/r²)/2`，简单零点 `r_*=c^{1/4}`。扰动 `φ=a v+O(a²)` 后，极小点的一阶平移消去 `q²` 的二阶项，剩下

\[
\min\mathcal B=2r_*^2F(r_*)v'(r_*)^2a^2+O_\mu(a^3)>0.
\]

bolt 处 B 恒为 1，固定 μ 下小扰动保持两侧单调性，所以 `N_inner=1-min B<1`。关键是先固定 μ；此 Taylor 展开没有给出 `μ→0` 的统一亏损比例。

### 3.2 标量 gluing 的实际条件

X10 使用 Delay 的局部标量粘合不是单靠二阶接近：其定理要求固定环带上足够高阶的邻近性与伴随标量算子无核。当前 Fμ 在固定环带上随 μ→0 为光滑各阶接近，固定 μ 后 a→0 同样如此，因此可满足高阶邻近性；文中随后仅用 C2 小量确保 f>0，并非把定理弱化到 C2。

CH 的伴随核满足

\[
\operatorname{Hess}f-(\Delta f)g+fg=0
\quad\Longrightarrow\quad \operatorname{Hess}f=(f/3)g.
\]

若 `∇f≠0`，对任一包含 ∇f 的 2 平面交换导数会强迫截面曲率为 `-1/3`。CH 的同点 holomorphic 与 totally real 平面曲率不同，故 ∇f=0，再由 Hess 方程得 f=0。此处固定环带非退化确实成立。粘合保持内区不动，外环 f>0，故不会暗中加回负质量。

核验的一手来源：Erwann Delay, *Localized gluing of Riemannian metrics in interpolating their scalar curvature*, Theorem 1.1 与 Propositions 2.2–2.5，https://arxiv.org/pdf/1003.5146 。

### 3.3 细柄后负 Yamabe 归一化

03 卷约 2164–2254 行的固定 j 顺序合理。关键输入必须全保留：

- 缩柄及过渡的标量有独立于柄尺度的下界，给 Yamabe 因子的统一上界；
- 固定 j 只有有限个嘴，离开嘴的椭圆紧性与有界可去奇点适用；
- 实际标量预算给 `Vol(ĝ)≥2π²A_j`，排除 Yamabe 因子整体趋零；
- 负标量常数代表唯一性迫使离嘴极限为 1；
- 再由标量能量及共形 Weyl 不变量控制 Ricci/P 能量，不能直接假设颈部不损失。

因此 `limsup N≤k(1-δ)+4ℓ` 可由余下 P 能量 `32π²ℓ` 与逐点 `8π²f_-≤|Ric°|²` 得到。对角选择只在每个固定 j 的上述论证之后进行。

最后

\[
\mathcal E/h\to28/9+J_C/(9\pi^2)>4.
\]

新引理 (A) 也直接排除这些固定细胞在真正近极小序列中占正 Q 密度，因为每个细胞的 `p_C-8π²` 是固定正数，帽总体积 O(Q)=o(A)。

## 4. 有限变分计算与 N/Z 的真实剩余内容

### 4.1 Proposition 2 的 Taylor 式正确

03 卷约 2300–2386 行。`I=-4V`、`R=4V+P` 时，对有限矩变化 `(v,i,r)` 的一阶导数是

\[
D\mathcal E(v,i,r)
=\frac{8i+16v}{R}+\frac{16Vr}{R^2}
=\frac{4(r+2i+4v)}{R}-\frac{4Pr}{R^2}.
\]

所以稿中的精确线性余项 `-4Pr/R²` 没有漏项。固定紧族给一致的有限下降和 O(n) 矩控制，连同 `n=O(Q)` 足以得到结论。问题只在于这种一致下降没有沿所有退化族得到证明。

### 4.2 补偿式严格等价于原问题

03 卷约 2256–2298 行：

\[
P=8\pi^2N+Z
\quad\Longrightarrow\quad
Z-8\pi^2(Q-N)=P-8\pi^2Q.
\tag{K}
\]

这比渐近写法更短，是完全精确的等价式。因而任何试图证明补偿而只重新分配 N、Z 的论证都没有产生新不等式。必须有实际几何/场方程贡献正下界。

对一个完整 `s=-4` CH collar 单元，(B) 进一步化为

\[
p_C-8\pi^2q=\frac43v_C+4W_C-4d.
\tag{L}
\]

因此完整单元的真正 subthreshold 目标等价于

\[
v_C/3+W_C<d.
\]

新替换引理控制的是 (L) 的正部；要完成 O11，仍需排除其可积累的负部，或从近极小性提取足以应用 I55 的 bulk/单元描述。不能把“正超额消失”读成“每单元成本下界成立”。

在 `D=o(Q)` 的完整 CH 外部情形，I55 已给阈值下界；新的 (A) 允许 `D` 远大于 Q 而仍为 o(A)，但只得上述选择排除，不填平 Q 级负超额的缺口。
