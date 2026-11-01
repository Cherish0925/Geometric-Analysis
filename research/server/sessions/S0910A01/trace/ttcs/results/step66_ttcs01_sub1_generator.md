# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/briefing/original_research_goal.md",
    "Sessions/S0910A01/workspace/notes/step66_route_reorientation_after_IL_bridge.md",
    "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

The active goal is the sign-unrestricted Yau Problem 26 proposition: in each dimension, decide whether some dimension-only Ricci interval forces the same closed smooth manifold to carry an Einstein metric, or rigorously refute it. Read the route reorientation note and the goal. Generate serious, high-value mathematical routes after the restricted four-dimensional Ishida--LeBrun negative-gap analytic bridge has been completed. Do not propose final writing. Focus on mechanisms that could actually solve or refute the full proposition: positive branch, arbitrary four-dimensional topology, higher dimensions, collapse, topology, calibration-free methods, or new invariants. Distinguish what evidence would make each route promising or eliminate it.

## Output

### 总体结构

记
\[
\Gamma_n^\sigma=
\inf_{\operatorname{Ein}(M)=\varnothing}\ 
\inf_g\|g^{-1}\operatorname{Ric}_g-\sigma I\|_{L^\infty,\mathrm{op}},
\qquad \sigma=\pm1.
\]
原题在维数 \(n\) 成立，只需 \(\Gamma_n^+>0\) 或 \(\Gamma_n^->0\) 其中之一；要在某个固定维数推翻原题，则必须同时构造 \(\Gamma_n^+=\Gamma_n^-=0\)。Ishida–LeBrun 路线目前给出的是某类四维光滑型上的统一负支间隙。其真正可迁移的部分，是局部流和平滑化；下一层数学核心是找到不依赖该规范理论地理的退化荷、全局刚性量，或能够产生无权逐点小残差的退化构造。

## 一、四维“熵—Euler 锁定”给出一个新的全 Einstein 排除机制

存在一个相当直接、而且不使用 Seiberg–Witten 的四维命题。

设 \(X^4\) 是闭双曲四维流形，截面曲率归一化为 \(-1\)。若闭定向四维流形 \(M\) 存在非零度映射
\[
f:M\longrightarrow X,\qquad \deg f=d\ne0,
\]
并满足
\[
\chi(M)=|d|\chi(X),
\]
且 \(M\) 不是 \(X\) 的 \(|d|\)-重双曲覆盖的光滑底空间，则 \(M\) 不承载任何 Einstein 度量。

证明分三种 Einstein 常数。

* 若 \(\lambda>0\)，Myers 定理使 \(\pi_1(M)\) 有限，因而 \(\|M\|=0\)。但映射度不等式给出
  \[
  \|M\|\ge |d|\,\|X\|>0,
  \]
  矛盾。

* 若 \(\lambda=0\)，Cheeger–Gromoll 理论给出 \(\pi_1(M)\) 虚拟阿贝尔，同样导致 \(\|M\|=0\)，仍与非零映射度矛盾。

* 若 \(\lambda<0\)，缩放至
  \[
  \operatorname{Ric}_h=-3h.
  \]
  Besson–Courtois–Gallot 与 Bishop 熵估计给出
  \[
  \operatorname{Vol}(M,h)\ge |d|\,\operatorname{Vol}(X).
  \]
  四维 Einstein Gauss–Bonnet 公式给出
  \[
  8\pi^2\chi(M)
  =\int_M\bigl(|W_h|^2+6\bigr)\,dV_h.
  \]
  因为 \(8\pi^2\chi(X)=6\operatorname{Vol}(X)\)，Euler 等式又给出
  \[
  |d|\,\operatorname{Vol}(X)
  =\operatorname{Vol}(M,h)+\frac16\int_M|W_h|^2\,dV_h
  \ge \operatorname{Vol}(M,h).
  \]
  两侧体积不等式只能同时取等号，于是 \(W_h=0\)，且 BCG 等号情形迫使 \(f\) 同伦于双曲覆盖。这与光滑型假设冲突。

这给出一个很强的负支反例模板：若存在一列 \(M_j\) 满足上述拓扑等式，同时承载
\[
-1-\eta_j\le \sec_{g_j}\le -1+\eta_j,\qquad \eta_j\to0,
\]
那么把 \(g_j\) 放大三倍后就有
\[
\delta_-(3g_j)\le \eta_j,
\]
而每个 \(M_j\) 都没有任何符号的 Einstein 度量，因此 \(\Gamma_4^-=0\)。

最自然的候选是双曲四维流形的异光滑结构、切向同伦等价光滑化，或带 Euler 数不变的度映射构造。决定性文献问题是：Farrell–Jones、Ontaneda 型近双曲光滑化是否真正覆盖实维四，且是否保持
\(\chi(M)=|d|\chi(X)\)。高维版本本身不能代替四维版本，因为上述体积反向不等式来自四维 Gauss–Bonnet 的正项
\(|W|^2\)。

这个机制还有定量形式。若
\[
\|g^{-1}\operatorname{Ric}_g+3I\|_{\infty,\mathrm{op}}\le\varepsilon,
\]
则
\[
\operatorname{Vol}(g)\ge
(1+\varepsilon/3)^{-2}|d|\operatorname{Vol}(X),
\]
而 Gauss–Bonnet 给出
\[
\int_M|W_g|^2\,dV_g
\le
6|d|\operatorname{Vol}(X)
-\Bigl[6(1-\varepsilon/3)^2-2\varepsilon^2\Bigr]\operatorname{Vol}(g).
\]
因此体积比趋于一且 Weyl 能量相对于双曲体积趋于零。任何近双曲异光滑构造都必须与这一精确能量关系相容。

## 二、轨形消解中“首阶荷”与“高阶荷”决定间隙还是反例

设 \((\mathcal O,\bar g)\) 是 Einstein 轨形，奇点用 Ricci-flat ALE 空间 \((Y,g_Y)\) 消解。核心区的精细近似通常具有形式
\[
g_t=t^2\left(g_Y+t^2h_2+t^4h_4+\cdots\right).
\]
在未缩放的 ALE 坐标中，Einstein 方程成为
\[
\operatorname{Ric}\left(g_Y+t^2h_2+\cdots\right)
=
\lambda t^2\left(g_Y+t^2h_2+\cdots\right).
\]

这里存在一个对原题极其重要的阶数分界。

* 若最初方程
  \[
  L_Yh_2=\lambda g_Y
  \]
  连同所需渐近项不可解，则残差在未缩放坐标中为 \(t^2K\)。由于物理度量是 \(t^2g_Y\)，其算子范数为 \(O(1)\)。这种首阶障碍直接产生逐点 Ricci 缺陷的固定下界。

* 若 \(h_2\) 可解，而最先出现的不相容项在 \(t^{2m}\)、\(m\ge2\)，则物理算子范数为
  \[
  O(t^{2m-2})\longrightarrow0.
  \]
  因而高阶障碍完全可能同时产生：
  1. 无法修正为精确 Einstein 度量；
  2. 无权逐点 Ricci 缺陷趋零。

这正是轨形路线能否触及原题的分水岭。首阶 Green 算子计算不能只回答“能否精确消解”，还要输出残差在物理度量中的阶数。Ozuch 的高阶障碍理论在这里尤其相关：若某个轨形—ALE 配对首阶荷消失而更高阶荷非零，它比普通首阶不相容更接近真正反例。

对正支而言，这可能是目前最具体的近 Einstein 构造机。它仍需与全 Einstein 排除配对。局部不相容只能排除靠近该轨形的解；真正的反例还需要以下两种全局结构之一：

* 该光滑型上全部 Einstein 度量的紧化只出现已计算的轨形退化；
* 一个与正标量曲率相容、同时排除所有 Einstein 常数的光滑不变量。

后一类工具目前非常稀少。Seiberg–Witten 型量通常已被正标量输入消去，因此正支的主要困难不是制造小残差，而是排除远离该轨形的其他 Einstein 度量。

## 三、可替代 IL 校准的“Einstein 缺陷荷”

令
\[
F_\sigma=\operatorname{Ric}-\sigma g,\qquad
\mathcal T_\sigma
=
F_\sigma-\frac12(\operatorname{tr}_gF_\sigma)g.
\]
由收缩 Bianchi 恒等式，
\[
\operatorname{div}_g\mathcal T_\sigma=0.
\]
故对任意向量场 \(X\) 和光滑区域 \(\Omega\)，
\[
\int_{\partial\Omega}\mathcal T_\sigma(X,\nu)
=
\frac12\int_\Omega
\langle\mathcal T_\sigma,\mathcal L_Xg\rangle\,dV.
\]
若 \(\|F_\sigma\|_{\infty}\le\varepsilon\)，右侧由
\[
C_n\varepsilon\int_\Omega|\mathcal L_Xg|\,dV
\]
控制。

这个恒等式提供一种不依赖规范理论的局部荷：

* 在 ALE 区域，取近似径向伸缩场，通量可恢复质量、重整化体积或首阶消解系数。
* 在长颈中，取近似轴向平移场，通量测量两端 Einstein Hamiltonian 数据的差。
* 在塌缩纤维化中，取近似纤维 Killing 场，通量测量 O’Neill 张量与纤维曲率的补偿量。
* 对轨形高阶项，向量场荷还不够，需要把它扩展为与伴随 Einstein Jacobi 张量的 Green 配对：
  \[
  \int_\Omega\langle \Phi(g),k\rangle
  =
  \int_{\partial\Omega}\mathcal B(g,k)
  +\text{高阶项},
  \qquad L^*k=0.
  \]

由此可以定义一族尺度归一化缺陷荷 \(\mathcal Q_\alpha\)。精确 Einstein 度量使所有荷为零；首个非零荷的缩放阶数决定逐点缺陷是否能够趋零。已完成的截断流正适合把仅有 \(C^0\) 缺陷的环带或核心区平滑到足以计算这些通量，而不需要先有全局 Weyl 控制。

有力信号是：该荷体系能重新导出 Biquard 首阶障碍、Ozuch 高阶项以及余齐性一 Einstein 方程的守恒量。若所有非可积退化都携带维数统一的首阶非零荷，就会导向某一支的维数统一间隙。若存在首阶荷全消失、首个非零项出现在更高阶的闭光滑消解，则它给出反例构造所需的局部核心。

## 四、四维一般拓扑可组织为“临界点在无穷远”的完整问题

在四维固定光滑型上，紧 Ricci 夹逼已提供相当强的总能量信息。写
\[
E=\operatorname{Ric}-\frac{s}{4}g.
\]
若 \(\delta_\sigma(g)\le\varepsilon\)，则 \(s\) 接近 \(4\sigma\)，且
\[
|E|\le C\varepsilon.
\]
Gauss–Bonnet 给出
\[
8\pi^2\chi(M)
=
\int_M\left(|W|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)dV.
\]
对固定 \(M\)，这同时控制体积和 \(\int|W|^2\)。因此非塌缩序列应具有以下结构：

1. 光滑 Einstein 核心；
2. 有限个轨形点；
3. Ricci-flat ALE 泡；
4. 每个拼接参数对应有限维障碍映射。

高曲率尺度 \(r_i\to0\) 上，归一化项变成 \(r_i^2\sigma g_i\)，所以任何良好吹起极限必为 Ricci-flat。这一事实不依赖正负支，也不依赖 IL 地理。

由此原题的四维核心可以重写为：所有 Einstein 空集分支上的临界序列，是否必然携带一个尺度不衰减的缺陷荷？若答案为是，得到统一间隙；若某个退化层的障碍映射满足
\[
\mathcal O(t)\ne0,\qquad |\mathcal O(t)|=O(t^\alpha),\quad \alpha>0,
\]
并且其光滑消解型上没有其他 Einstein 度量，就得到逐点缺陷趋零的反例。

真正的新定理形状应当同时覆盖三种退化：

* 非塌缩 ALE 泡树；
* ALF、ALG 或更深层局部塌缩；
* 长颈或 cusp 型分裂。

IL 路线处理的是第一类结构中带有特殊全局校准的一部分。一般四维拓扑所需的是“泡树加荷”的统一表述，而不是另找一个只对某个地理成立的曲率积分。

## 五、正支塌缩可化为 Einstein–Yang–Mills 的积分格逼近

正支最具体的塌缩模型来自主 \(S^1\)-丛
\[
S^1\longrightarrow P\overset{\pi}{\longrightarrow}B
\]
及连接度量
\[
g_t=\pi^*g_B+t^2\theta^2,\qquad d\theta=F.
\]
在纤维全测地的常用约定下，若 \(U\) 是单位竖直向量，
\[
\begin{aligned}
\operatorname{Ric}_{g_t}(X,Y)
&=\operatorname{Ric}_{g_B}(X,Y)
-\frac{t^2}{2}\langle\iota_XF,\iota_YF\rangle,\\
\operatorname{Ric}_{g_t}(U,U)
&=\frac{t^2}{4}|F|^2,\\
\operatorname{Ric}_{g_t}(X,U)
&=-\frac t2(d^*F)(X).
\end{aligned}
\]
所以 \(g_t\) 接近 \(\operatorname{Ric}=g\) 等价于一个 Einstein–Yang–Mills 系统：
\[
d^*F\approx0,\qquad
\frac{t^2}{4}|F|^2\approx1,\qquad
\operatorname{Ric}_{B}
-\frac{t^2}{2}F\circ F\approx g_B.
\]

这产生一个此前路线中没有充分利用的反例机制。若 \(b_2(B)\ge2\)，积分格方向在实射影上稠密。取一个实二形式 \(\alpha\) 精确解
\[
d^*\alpha=0,\qquad
\frac{t_0^2}{4}|\alpha|^2=1,\qquad
\operatorname{Ric}_B-\frac{t_0^2}{2}\alpha\circ\alpha=g_B,
\]
而 \([\alpha]/2\pi\) 的方向不是有理方向。可选原始积分类 \(c_k\) 与 \(t_k\to0\)，使调和曲率 \(F_k\) 满足
\[
t_kF_k\longrightarrow t_0\alpha.
\]
相应圆丛度量便有
\[
\delta_+(g_{t_k})\longrightarrow0.
\]

在 \(B\) 为多个二球乘积时，上述实方程可化为显式代数方程。若
\[
\alpha=\sum_i a_i\omega_i,\qquad
\operatorname{Ric}_{B}|_{B_i}=\kappa_i g_i,
\]
则要求大致为
\[
\kappa_i-\frac{t_0^2a_i^2}{2}=1,\qquad
\frac{t_0^2}{4}\sum_i a_i^2=1,
\]
允许连续且通常无理的方向。

这一机制对正支有双重意义：

* 若某些总空间 \(P_{c_k}\) 可由独立拓扑定理证明没有任何 Einstein 度量，它直接产生正支反例。
* 若 Wang–Ziller、Sasaki–Einstein 或更一般连接度量理论总能在同一总空间上通过改变基底尺度而找到精确 Einstein 度量，则它解释了为何塌缩近解仍满足原题结论。

经典 \(S^1\)-丛例子中，很多总空间确实已经承载 Wang–Ziller 或 Sasaki 型 Einstein 度量，所以它们是重要对照，而不是反例。真正有辨识力的是：积分 Chern 向量的近 EYM 解是否总可在同一总空间上完成为某个精确 Einstein 度量。该问题可以先在主环面丛和齐性基底上化为有限代数系统。

## 六、正四维支的高价值目标是“小拓扑 + 全模空间紧化”

正 Ricci 输入已经排除了所有依赖正标量曲率不存在性的规范理论工具。因而正四维反例最可能来自：

1. 一个严格满足 Hitchin–Thorpe 的正标量光滑型；
2. 一个正 Einstein 轨形的高阶近似消解；
3. 对该光滑型全部 Einstein 度量的整体排除。

\(\#_4\mathbb{CP}^2\) 位于 Hitchin–Thorpe 等号处，不能承载任意紧的正支夹逼；\(\#_3\mathbb{CP}^2\) 则满足
\[
2\chi-3\tau=1,
\]
是最小的严格余量之一。其一般 Einstein 存在状态必须由原始来源确认。若该状态仍未定，它本身就是一个高度集中的测试对象，而不是可直接使用的反例。

对这类小 \((\chi,\tau)\) 光滑型，固定拓扑使 Einstein 曲率能量有限，因而“所有 Einstein 度量都进入有限轨形—泡树紧化”比任意拓扑上的全局分类更有希望。数学上需要同时处理：

* \(\lambda>0\) 的 Myers 紧性与轨形退化；
* \(\lambda=0\) 的四维 Ricci-flat 覆盖分类；
* \(\lambda<0\) 的体积、长颈及塌缩；
* 每个紧化层的消解荷；
* 不接近任何退化层的光滑 Einstein 分支。

A02 所研究的 \((S^2\times S^2)/\mathbb Z_2\) 与 Eguchi–Hanson 配对，只有在这一完整紧化中才能贡献全局不存在性。若首阶荷为零且高阶荷非零，它可制造正支近解；若首阶荷非零，则它更可能产生正支局部间隙。

## 七、高维可寻找“特征数—体积”代数校准

四维熵—Euler 机制依赖 Einstein 曲率分解
\[
\operatorname{Rm}=-I+W
\]
下的恒等式
\[
\operatorname{Pf}(\operatorname{Rm})
=
\operatorname{Pf}(-I)+c|W|^2.
\]
在更高偶维，可研究是否存在 Euler 与 Pontryagin 形式的线性组合 \(\mathcal P\)，使所有归一化 Einstein 代数曲率张量满足
\[
\mathcal P(-I+W)-\mathcal P(-I)
=
\sum_\alpha |Q_\alpha(W)|^2
\]
或至少具有固定符号。若存在，则对映射到局部对称目标的流形：

* BCG 型度定理给出体积下界；
* 特征数等式给出体积上界；
* 等号迫使 \(W\) 落入局部对称代数轨道；
* 非标准光滑型因此没有 Einstein 度量。

这会把四维的近双曲反例机扩展到 Ontaneda、Farrell–Jones 等更高维构造真正活跃的维数。

这里有一个低成本而决定性的有限维计算：在满足代数 Bianchi 恒等式和 Einstein 收缩的 Weyl 张量空间上，计算 Pfaffian及 Pontryagin 组合的符号。六维的三次 Weyl 项很可能出现双符号；八维则可能存在非平凡平方和组合。随机精确代数样本、对称空间曲率张量和半正定平方和分解可以迅速区分“普遍代数恒等式”与“只对特殊 holonomy 成立的恒等式”。

若普遍固定符号不存在，仍可在复双曲、四元数双曲或特定 holonomy 类中寻找表示论投影；此时还需要证明任意 Einstein 度量被拓扑或度映射强迫进入该表示类型。

## 八、最具分辨力的三组观察

1. **首阶还是高阶不相容。**  
   轨形消解中，首阶不相容给 \(O(1)\) 的无权 Ricci 缺陷；首次不相容若出现在 \(t^4\) 或更高阶，则无权缺陷可以趋零。这一阶数计算直接区分“统一间隙”与“反例核心”。

2. **塌缩是否归约为可完成的 EYM 系统。**  
   若所有正支塌缩近解都能在同一总空间上完成为精确连接 Einstein 度量，塌缩支持正支成立；若积分格逼近实 EYM 解产生没有任何 Einstein 度量的总空间族，则正支被推翻。

3. **是否存在维数统一的退化荷量子。**  
   四维固定拓扑上的能量紧化只给拓扑相关常数。原题需要更强的局部事实：每个不能完成为 Einstein 的退化模型，都携带只依赖维数的非零尺度荷。若这些荷可沿轨形群、Chern 类或泡树复杂度趋于零，则它们自然生成维数固定的反例序列。

目前最接近完整反例机器的组合是：四维熵—Euler 拓扑包提供全 Einstein 排除，近双曲光滑化提供负支输入；高阶轨形消解或 EYM 积分格逼近提供正支输入。最接近完整存在机器的组合则是：缺陷荷量子化、四维临界序列紧化、以及塌缩 EYM 完成定理。两种方向最终都汇聚到同一个数学对象——Einstein 方程在退化层上的首个非零尺度荷。