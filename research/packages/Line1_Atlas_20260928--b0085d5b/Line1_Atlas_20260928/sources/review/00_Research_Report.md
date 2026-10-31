# 第一科学主线：七轮续研审读与新增推导

2026年9月28日。输入：数学快照 `0b1490791be560203b86a7d9834dcdc3cbc83b41` 的十二卷审读包。本文保留原始平衡流形族与 O10/O11，不更换研究目标。

## 0. 本轮究竟推进了什么

本轮并行审读了 I51 参数估计、I53 匹配帽、I55/X10 完整单元与近极小序列、任意共形径向构造、零端实际扭率方程，以及全局变分约化。得到下文六项可核查的推导，其中最实质的构造侧进展是新的共形平方恒等式及其径向排除推论；变分侧进展是取消光滑预紧条件的替换引理；零端进展是固定背景外部延拓的定量成本。

**没有证明一般 O10，也没有证明或否定全部度量的 O11 系数 4。** 本轮数值搜索没有得到低于 4 的真实候选。本文将已推导结论、继承输入与尚缺连接分别写明；不把审读通过当作独立重证全部前置 PDE，不主张这些推导已经完成文献首创性认证。

停滞的主要数学原因已经明确：一些看起来更具体的“剩余补偿式”与原问题完全等价；另一些端点估计在目标端本来就退化。继续配方、优化已有常数或重复相同参数搜索，不能自动增加信息。

## 1. 固定对象与已完成的归约

保持原族
\[
M_j=X_j\#k_j\overline{\mathbb{CP}}^2\#\ell_j(S^1\times S^3),\quad
A_j=c_1^2(X_j),\quad Q_j=k_j+4\ell_j,\quad h_j=Q_j/A_j\to0.
\]
其中 \(k_j/Q_j\to2/9\)、\(\ell_j/Q_j\to7/36\)。置
\[
P=\int|\operatorname{Ric}^{\circ}|^2,\quad R=\int|\operatorname{Ric}|^2,
\quad S_2=\int s^2,\quad L_s=\int(s-\bar s)^2,
\]
\[
\mathcal E=(4P+L_s)/R,\qquad \alpha_j=\inf_g\mathcal E(g).
\]
继承 I40/I41 与实际拓扑供给：\(c_1h\le\alpha\le4h/(1+h)\)。在低缺陷变分问题中，负 Yamabe 代表使 \(s=-4\)，且不增加目标；因此标量方差不是当前尚未处理的全度量缺口。

下文用 \(\operatorname{Rm}_{\rm op}\) 表示曲率算子范数。单元成本另记
\(J(G)=\int_C|\operatorname{Ric}_G+G|^2\)，避免与全局 \(\mathcal E\) 混淆。

## 2. 新增推导一：O11 与标准全曲率最小值的精确比较

令
\[
\rho(M)=\frac{\inf_gP(g)}{8\pi^2A},\qquad
U=\frac{3(2\chi-3\tau)}A>0.
\]
则在原实际供给下，无需极小值取得，
\[
\boxed{\frac{4\rho}{U+4\rho}\le\alpha\le\frac{4\rho}{1+\rho}.}\tag{2.1}
\]

证明：标量预算给 \(S_2\ge32\pi^2A\)，故 \(R\ge P+8\pi^2A\)。另一手性 Chern–Weil 公式给
\[
R=4P+8\pi^2AU-12\int|W^-|^2\le4P+8\pi^2AU.
\]
后一式与 \(\mathcal E\ge4P/R\) 给下界。取逼近 \(\inf P\) 的度量并作 Yamabe 替换，利用
\(P(g)-P(\widehat g)=(S_2(g)-S_2(\widehat g))/12\ge0\)，得到仍逼近该下确界的常标量度量。在此类中 \(\mathcal E=4P/R\)，前一式给上界。

恢复族给 \(0\le\rho\le h\)，平衡族有 \(U=1+h+O(h^2)\)，从而
\[
\boxed{\alpha=4\rho+O(h^2).}\tag{2.2}
\]
四维 Gauss–Bonnet 又给
\[
\int|\operatorname{Rm}_{\rm op}|^2=8\pi^2\chi+P.
\]
因此 O11 的系数 4 等价于
\[
\boxed{\inf_g\int|\operatorname{Rm}_{\rm op}|^2
=8\pi^2\chi(M_j)+8\pi^2Q_j+o(Q_j).}\tag{2.3}
\]
也就是
\[
\inf_g\int|\operatorname{Rm}_{\rm op}|^2
=\frac{8\pi^2}{3}A_j+\frac{20\pi^2}{3}Q_j+o(Q_j).
\]

对 \(s=-4\) 的竞争序列，同样有
\[
\mathcal E(g_j)-\alpha_j=o(h_j)
\iff P(g_j)-\inf_gP=o(Q_j).\tag{2.4}
\]
这允许直接研究无约束的全曲率变分，不必先完成完整泡树分解。

经典 LeBrun 精确 Ricci 能量下界 \(\inf R=8\pi^2(A+Q)\) 不包含 (2.3)：不能把 \(R\) 和 \(S_2\) 的两个独立下界相减为 \(P=R-S_2/4\) 的下界。详证与原文定位见附录 `01_global_variation.md`。

## 3. 新增推导二：退化完整单元也不能保留正密度的多余成本

设 \(g_j\) 为原族上 \(s=-4\) 的真正近极小序列。取任意有限个两两不交的完整标记单元
\[
C_{ij}=D_{ij}\#k_{ij}\overline{\mathbb{CP}}^2
\#\ell_{ij}(S^1\times S^3),\qquad q_{ij}=k_{ij}+4\ell_{ij}>0.
\]
每个外开领口与参考复双曲帽 \(D_{ij}\) 的整个度量 germ 精确相同。单元可以退化，拓扑、数量和帽半径可以变化。只假设参考帽总体积
\[
D_j=\sum_i d_{ij}=o(A_j),\qquad d_{ij}=\operatorname{Vol}(D_{ij}).
\]
则
\[
\boxed{\sum_i\left(P_{C_{ij}}-8\pi^2q_{ij}\right)_+=o(Q_j).}\tag{3.1}
\]
这里不要求 C4 预紧、曲率上界或实际单元总体积为 \(O(Q)\)。

证明的第一步是相对恒等式：
\[
P_C=8\pi^2q+\frac43v_C+4W_C-4d,
\quad W_C=\int_C|W^+|^2.
\]
所以 \(\sum v_C\le3P/4+3D=o(A)\)。仅选择正超额单元，记
\[
B=\sum(P_C-8\pi^2q)>0,\qquad w=\sum(d-v_C).
\]
有 \(B=O(Q)\)、\(w=o(A)\)。用原稿已有的标准缩核恢复替换这些单元，保留整个外领口。对每个固定 j，其数目和拓扑有限，故可把恢复误差总和选为 \(o(Q_j)\)，不需要统一缩核速率。恢复后的极限矩为
\[
V'=V+w,\quad I'=-4(V+w),\quad R'=4(V+w)+P-B.
\]
直接比较得到精确式
\[
\mathcal E'_0-\mathcal E
=-\frac{16(VB+Pw)}{(4V+P)[4(V+w)+P-B]}.
\]
由此
\[
\mathcal E(g'_j)-\mathcal E(g_j)
=-\frac{4B_j}{R_j}
+O\!\left(\frac{Q_j|w_j|+Q_j^2}{A_j^2}\right)+o(h_j)
=-\frac{4B_j}{R_j}+o(h_j).
\]
近极小性迫使 \(B=o(Q)\)。相关矩之间的抵消消除了通常 Taylor 展开中的 \(w^2/A^2\) 项，这正是能去掉原预紧限制的原因。

这证明高成本退化块也不能以正总密度留在近极小序列中。它没有排除低成本块。事实上
\[
Z-8\pi^2(Q-N)=P-8\pi^2Q
\]
完全精确，重分配 N、Z 不会产生新下界。对于完整常标量单元，低成本恰等价于 \(v_C/3+W_C<d\)。详见附录 `02_cells_and_replacement.md`。

## 4. 新增推导三：任意共形变形的完整有符号成本与新排除范围

这一恒等式不要求 Kähler，也不要求对称性。设 K 为四维单元度量，\(G=e^{2\phi}K\)，\(\phi\) 在整个外领口恒为零。所有积分与导数在 K 下，采用 \(\Delta=\operatorname{div}\nabla\)。记
\[
\delta=s_K+4,\quad a=e^{2\phi},\quad q=|d\phi|_K^2,
\quad H=\Delta\phi+q.
\]
则
\[
\boxed{\begin{aligned}
J(G)-J(K)=\int_C\bigg[&12\left(H-\frac\delta6\right)^2
+4\left(a-1+\frac\delta4\right)^2\\
&+(16+12a)q-\frac7{12}\delta^2\bigg]dV_K.
\end{aligned}}\tag{4.1}
\]
在 \(\phi\equiv0\) 的区域，方括号整体为零，因此负项只需计入变形支撑区。

证明：共形 Weyl 能量不变，匹配领口使相对特征项不变，因此
\(\Delta J=\Delta S_2/3+2\Delta I+4\Delta V\)。代入
\[
s_G=e^{-2\phi}(s_K-6\Delta\phi-6|d\phi|^2),\qquad dV_G=e^{4\phi}dV_K,
\]
并对含 \(\Delta\phi\) 的项分部积分，得到
\[
\Delta J=\int[12H^2-4\delta H+(16+12a)q
+4(a-1)^2+2\delta(a-1)].
\]
分别对 H 与 a−1 配平方，即为 (4.1)。

直接推论：
\[
\boxed{J(e^{2\phi}K)\ge J(K)-\frac7{12}
\int_{\operatorname{supp}\phi}(s_K+4)^2.}\tag{4.2}
\]
若变形支撑区 \(s_K=-4\)，任何幅度和任何梯度的共形变形都不能降低 J。这里没有把 \(\phi\) 假设为小量。

对 I55 的普通单 bolt 三轴 almost-Kähler 基底，令
\[
\mu=r_0^2,\quad j=J/(2\pi^2),\quad
B_0=\frac{(\mu+2+\mu P_w)^2}{1-\mu^2/R^4},
\]
其中 \(P_w\ge0\) 为原 I55(8.1) 的实际三轴量。以 \(\Omega=\operatorname{supp}\phi\) 定义
\[
S_{\rm in}=\frac1{2\pi^2}\int_\Omega\delta^2,
\quad S_{\rm out}=\frac1{2\pi^2}\int_{C\setminus\Omega}\delta^2,
\]
\[
G_\phi=\frac1{2\pi^2}\int_C|d\phi|^2,
\qquad G_{\phi,a}=\frac1{2\pi^2}\int_Ce^{2\phi}|d\phi|^2.
\]
原非共形平方分解保留标量平方后给
\(j(K)\ge B_0+(S_{\rm in}+S_{\rm out})/4\)。与 (4.1) 合并：
\[
\boxed{j(G)\ge B_0-\frac13S_{\rm in}+\frac14S_{\rm out}
+16G_\phi+12G_{\phi,a}.}\tag{4.3}
\]
因此，任何固定改进 \(j(G)\le4-\epsilon\) 必须满足
\[
\boxed{S_{\rm in}\ge3(B_0-4+\epsilon)+\frac34S_{\rm out}
+48G_\phi+36G_{\phi,a}.}\tag{4.4}
\]
特别地，\(S_{\rm in}\ge3\epsilon+12\mu+3\mu^2\)。基底条件
\[
\frac1{2\pi^2}\int_C(s_K+4)^2\le3(B_0-4)
\]
足以排除任意共形因子产生低于 4 的成本；更粗的充分条件为该积分不超过 \(12\mu+3\mu^2\)。若该积分沿序列趋零，则任意共形改变仍有 \(\liminf j(G)\ge4\)。

新的可检验内容是：共形梯度必须由足够大的基底标量误差支付。结合原稿两尺度必要条件，低成本候选同时需要微观共形作用、非消失的外部修改，以及满足 (4.4) 的基底标量误差。仅让径向矩 M 归零远远不够。

本轮实际搜索同时使用微观 \(r/\sqrt\mu\)、宏观 \(r/R\) 与对数半径基函数，保留完整 bolt 与外领口条件。有限维搜索未产生低于 4 的候选；其数值不用于证明全类下界。恒等式推导、积分复核、所有成功及未收敛返回见附录 `03_conformal_identity_and_radial_search.md` 与 `checks/`。

## 5. 新增推导四：以总封帽评分替代统一长环带

继承 I53 的匹配帽定理。对每个普通吹起配置若干候选带标记环带，\(E_{i\nu}\) 为尺度不变完整曲率能量，\(a_{i\nu}\) 为缩放后固定坐标的 C0 欧氏差。定义
\[
c_i=\inf_\nu(E_{i\nu}+a_{i\nu}^2).
\]
全部选中环带围住、将被替换的内部区域须两两不交，并且各自仅对应指定的一个普通吹起，不含其他手术核心或 handle。令 r 为完全没有配置候选的吹起数。存在统一常数 C，使
\[
\boxed{\mathcal E(g)\ge\frac{4h}{1+h}
-\frac C A\left[r+\sum_i\min\{1,c_i\}\right].}\tag{5.1}
\]
不需要先假设 \(\mathcal E=O(h)\)，也不需要所有核心上最大振幅趋零。

证明：取固定帽阈值 \(\theta>0\)，对 \(c_i\le\theta/2\) 的核心封帽，其他保留。好帽的总 \(W^+\) 能量不超过 \(C\sum c_i\)；坏核心数 b 不超过 \(r+C\sum\min(1,c_i)\)。I53 的精确比较给
\[
\mathcal E\ge\frac{4h}{1+h}
-\frac{24b+2C_+/\pi^2}{A(1+h)^2},
\]
即得 (5.1)。候选下确界未取得时以任意小总误差选取再令误差趋零。

所以总评分 \(r+\sum\min(1,c_i)=o(Q)\) 已足够闭合该序列的首项。若每个核心有 L 个不交候选，原来的 \(A/L\) 可以改成实际候选环带能量 \(E_{\rm ann}/L\)。只有在另证 \(E_{\rm ann}=O(Q)\) 后，才能把条件降低到 \(L\to\infty\)；不能把这个供给当成已知。审读与短平滑证明见附录 `04_matched_caps.md`。

## 6. 新增推导五：实际微核心的固定背景延拓必须付发散代价

固定光滑受控背景球 \(B_2\supset B_1\)，考虑同一实际解
\[
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad |\Phi|\le\sqrt2.
\]
令 \(K=\|F_A\|_{L^2(B_2)}\)，\(\tau\) 为原稿实际三次扭率。则
\[
\boxed{\sup_{B_1}|\nabla_{3A}\tau|\le C(1+K)^4.}\tag{6.1}
\]
常数依赖固定球几何，不依赖 I51 的参数 \(\beta\)。该稿 \(\beta\) 出现在预算中，实际方程权重恒为2。

证明的估计链：在球上选 abelian Coulomb 规范，有 \(\|a\|_{W^{1,2}}\le C(1+K)\)，所以 \(a\in L^4\)。幅度界与 Dirac 方程给 \(\Phi\in W^{1,4}\)。使用实际 Maxwell 方程
\[
dF_A=0,\qquad \delta F_A=2\delta F_A^+=4i\delta\sigma(\Phi),
\]
得到 \(F_A\in W^{1,4}\subset L^8\)。在较小球重新作 p=8 的 Coulomb 规范，依次得 \(a\in W^{2,8}\)、\(\Phi\in W^{2,8}\) 与 \(W^{3,8}\)，增长次数分别可取 \((1+K)\)、\((1+K)^2\)、\((1+K)^3\)。扭率的多项式定义给
\[
|\nabla\tau|\le C(|\Phi|^2|\nabla_A^2\Phi|
+|\Phi||\nabla_A\Phi|^2),
\]
从而 (6.1)。这里没有误用临界 \(W^{1,4}\) 到 L∞ 的嵌入，只使用固定有限指数8。

第四卷最终第7节的简单实际核心满足
\(|\tau_\ell|(\ell y)=|y|+o_{C^1}(1)\) 于固定壳层。Kato 不等式直接给 \(\sup|\nabla\tau_\ell|\ge c/\ell\)，不依赖联络规范选择。若该同一解保持幅度界并延拓至固定外球，则
\[
\boxed{\int_{B_2}|F_A|^2\ge c\ell^{-1/2}.}\tag{6.2}
\]
核心自身能量为 \(O(\ell^4)\)，故发散成本出现在外部延拓。由于实际拟合模型 \(K_-\) 一致有界，还得到
\[
\boxed{\int_{B_2}|F_A^--K_-|^2\ge c'\ell^{-1/2}-C'.}\tag{6.3}
\]
这是外部完整方程供给的新限制，不改变最终 (6.6) 的平方差恒等式。

此结论只排除固定尺度受控背景延拓。一般 O10 允许外半径缩小、几何集中或覆盖倍数增大；这些情况不被 (6.1) 的统一常数覆盖。完整证明及交叉核验见附录 `05_actual_core_extension.md`、`07_extension_crosscheck.md`。

## 7. 新增推导六：线性强制可压缩到 Yamabe 代表上的一个实际解

在 \(s=-4\) 上，取一个普通 SW 解并缩放旋量至权重2。置
\[
\rho=|\Phi|^2\le2,\quad K_\Phi=\int|\nabla_A\Phi|^2,
\quad J_+=\|F_A^+\|_2^2-4\pi^2p.
\]
同一解满足精确式
\[
\boxed{\Sigma=16K_\Phi+4\int(\rho-2)^2+8J_+.}\tag{7.1}
\]
I51 的 \(\beta=2\) 配方控制右边后两项与 Weyl 模型误差。用振幅截断测试实际自旋子方程，控制低振幅区 kinetic energy；不能把全局 kinetic 等式错误地按区域限制。然后将同一解代入已继承的 Hessian 与弱 Bianchi 恒等式，得到
\[
\Sigma\le C\left(P+D_2+\sqrt{(P+D_2)(T_+-a^2)_+}\right).
\]
完整步骤见附录 `06_single_solution_and_parameters.md`。这一版本不需要在证明中调用所有辅助权重的可解性。对任意 g，只需其负 Yamabe 代表上有一个所需实际解，再用原共形能量恒等式转回。

该削弱简化了实际供给合同，但本轮没有因此构造新的流形族。全度量应用仍需逐共形类供给一个解。

参数端另有一个明确的阻塞检验。令
\[
x=V^{-1}\int w^2,\qquad q=72\pi^2p/V,
\qquad \mathcal P(t)=P_t/V.
\]
有限参数族为
\[
\mathcal P(t)=16t^2+(16+x-q)t+x.
\]
形式端点数据 \(r=0,x=0,q=16\) 满足 \(\mathcal P(t)=16t^2\)，兼容全部现有二次退化参数界，却有 \(D_\beta/V=16/\beta\to0\)。它不是实际闭流形反例；它严格说明，仅重选有限 \(\beta\) 或组合这些预算不够排除零端。新信息必须来自实际全局相容性。

## 8. 七个审读问题的处理结果

| 原问题 | 本轮结果 |
|---|---|
| I51 同一实际解、指数及共形转移 | 核查通过；补单解版本及参数端代数阻塞检验 |
| I53 精确匹配帽 | 未发现致命缺口；用 SSS 内部导数估计可缩短外领口冻结证明；补总评分版本 |
| I55 任意内部及等号、近极小选择 | 相对恒等式成立；补任意退化单元的正超额消失引理；一般选择未闭合 |
| X10 实际几何及有限变分 | 固定参数后稀释、CH 伴随核排除和固定 j 的 Yamabe 极限逻辑成立；它的首项大于4 |
| 完整共形耦合类是否低于4 | 新完整平方恒等式和标量误差阈值；新双尺度有限搜索没有反例；全类仍未判定 |
| 零端严格有符号机制 | 不恢复已相消的正预算；从外部 Dirac–Maxwell 方程得到定量延拓成本；退化外部未覆盖 |
| 最近邻是否已有短证明 | 核对 LeBrun、SSS、Yang、Delay 的直接相关输入；未发现这些定理直接包含 O10/O11；本轮不是整个领域的穷尽性检索 |

## 9. 接下来应当实际攻哪一条

O11 的无区域版本是 (2.3)。构造版本仍是完整匹配单元低于 \(8\pi^2q\)，单个普通吹起低于 \(8\pi^2\) 即足够。替换引理允许立即丢弃仅展示高成本下降的候选；新共形判据允许排除满足 (4.3) 下界的全部共形因子，而不再重复搜索它们。对未排除候选，应记录实际 \(S_{\rm in},S_{\rm out},G_\phi,G_{\phi,a},P_w\) 及所有平方，明确哪一个剩余相互作用能越过阈值。

证明版本可选择直接全曲率下界，或从真正近极小性供给 (5.1) 的总评分 \(o(Q)\)。没有必要先把完整 Γ 极限或通用泡树全部做完。单靠 N/Z 改写、投影 p 优化或标准多类 Gram 矩阵没有新增信息：原稿已经分别给出精确等价及相应无效性证明。

O10 应集中在固定背景延拓失败后的几何退化：能否用原 Ricci/Weyl 与 determinant 预算控制受控外球的丧失、匹配半径缩小或覆盖倍数增长？若不能，应尝试一个把这些代价全部计入的闭流形实际序列。局部真实核心与最终平方差恒等式已经经过检验，不应再次用它们本身宣称矛盾。

这些仍是未完成的数学连接。下一轮应以改变 (2.3)、产生真实低成本单元、或控制 (6.3) 未覆盖的退化外部为进展标准。

## 10. 来源与验证范围

内部定位均相对于本次 `0b14907` 十二卷包，尤其第三卷 I54/I55/X10、第二卷 I53、第一卷 I51、第四卷最终扭率稿与第五卷 I40/I41。附录保留逐步推导和式号定位。

直接核查的一手文献：

1. C. LeBrun, *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*, 特别是 §11：[原文](https://arxiv.org/pdf/math/0404251)。其标准全曲率功能量与 Ricci 功能量须区分。
2. O. Schnürer, F. Schulze, M. Simon, *Stability of Euclidean space under Ricci flow*, Theorem 4.4：[原文](https://arxiv.org/pdf/0706.0421)。这里只用于所需局部 DeTurck 内部导数估计。
3. D. Yang, *Convergence of Riemannian manifolds with integral bounds on curvature I*, §9：[原文](https://www.numdam.org/item/10.24033/asens.1644.pdf)。只借曲率演化结构，不借用带额外假设的存在定理。
4. E. Delay, *Localized gluing of Riemannian metrics in interpolating their scalar curvature*, Theorem 1.1、Propositions 2.2–2.5：[原文](https://arxiv.org/pdf/1003.5146)。X10 需高阶小量与伴随核条件，不是仅凭 C2 接近就可以粘合。

有限代数与数值检查验证恒等式、实现和候选结果；不代替椭圆估计、粘合存在或全局极限证明。新增定理的输入均已明写，主问题的未完成状态也保留。
