# 第一科学主线：统一手术端点与预定残余覆盖塔上的低成本恢复

日期：2026-10-07。

## 本文完成的内容与依赖边界

本文不修改用户的原稿。本文补出两条可逐步检查的推论：

1. 将 N1 与有限密度 O10 按拓扑参数分区，得到一项地理条件下的统一端点定理；它适用于实际供给已验证的一般型曲面吹起、添柄，以及相应的正平方多主体连通和，常数不依赖这些手术的数量，也不要求手术后 Euler 密度有界。
2. 将已认证的严格低成本完整单元复制到**任意事先给定的嵌套残余覆盖塔**，而非仅在为单元另行选择的覆盖族上复制。覆盖子群不要求正规。结合原稿的完整端共形选择，可直接使用已有 P 区间上端，得到下文的数值上界。

两项都是现有主定理和实际构造之间的推导连接，不是新证明了 SW 非消失、有限密度 PDE 或区间积分程序。本文没有证明对任意实际供给对象都成立的无密度 O10，也没有决定 O11 的锐利首项。旧目标“首项必为 4”在已被严格低成本构造覆盖的族上不能继续作为待证真命题。

---

## 1. 固定的原稿输入

对闭、连通、定向光滑四流形，记

\[
T=2\chi+3\tau,\quad
P(g)=\int|\operatorname{Ric}^{\circ}_g|^2,\quad
R(g)=\int|\operatorname{Ric}_g|^2,
\quad\mathcal J=4P/R,
\]
\[
\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}_g-\lambda g|^2}{\lambda^2V_g},
\qquad \alpha(M)=\inf_g\mathcal E(g),
\]
\[
D_\beta=(1+\beta^{-1})\int s^2
+6(\beta+1)\int|W^+|^2-72\pi^2p,
\qquad
\kappa_\beta=\fint|\operatorname{Ric}+g|^2+D_\beta/V.
\]

保留原 O10 的实际共形单极子供给和同一类的预算

\[
p=(a^+)^2\ge A>0,\qquad a^2\ge T.
\]

全度量应用须在每一个共形类内满足原供给条件；每次证明中的 p、a 与实际解来自同一结构。本文不将一个共形类上的一个解扩大成全部共形类的供给。以下引用原稿已有结论：

- **N1：**存在普适 \(\varepsilon_N>0\)，有
  \[
  \mathcal J(g)+(T/A-2/3)_+\ge\varepsilon_N.
  \]
- **有限密度端点：**每个固定有限 \(B\) 有 \(c_{\rm FD}(B)>0\)，使
  \[
  \chi/A\le B\implies
  \kappa_\beta\ge c_{\rm FD}(B)(\beta-2)^2/\beta^2,
  \quad\beta\ge2.
  \]
- **基本比较：**\(D_\beta\ge0\)，且
  \[
  \mathcal J\le\mathcal E\le\fint|\operatorname{Ric}+g|^2.
  \]
  最后一项只是取 \(\lambda=-1\)。原负 Yamabe／正实际供给使所用 \(R>0\)；不把 Ricci-flat 度量代入未定义的 \(4P/R\)。

以上三项是本文的前置定理，不由下文几行代数重新认证。

## 2. 一个地理条件足以去掉整族手术上的密度损失

### 定理 1：分区闭合

设一族原允许对象满足

\[
Q:=A-T\ge0,\qquad \chi(M)\le C A+Q
\tag{2.1}
\]

其中 \(C\) 为固定有限常数。则同一个常数

\[
c_{\rm geo}(C)=\min\{\varepsilon_N,c_{\rm FD}(C+1/3)\}>0
\]

使整族、所有原允许度量与所有 \(\beta\ge2\) 满足

\[
\boxed{\kappa_\beta(g)\ge
c_{\rm geo}(C)\frac{(\beta-2)^2}{\beta^2}.}
\tag{2.2}
\]

结论没有要求 \(\chi(M)/A\) 在这族中有统一上界。它要求的是明确的仿射地理约束 (2.1)。

**证明。**

若 \(Q/A\ge1/3\)，则 \(T/A=1-Q/A\le2/3\)。N1 直接给

\[
\kappa_\beta\ge\mathcal E\ge\mathcal J\ge\varepsilon_N.
\]

若 \(Q/A<1/3\)，则 (2.1) 给

\[
\chi/A<C+1/3.
\]

此时只需调用有限密度定理在**单个固定数** \(B=C+1/3\) 处的常数。结合 \(0\le(\beta-2)^2/\beta^2\le1\)，两个区间合并即得 (2.2)。证毕。

这里没有令 \(B\to\infty\)，也没有将 \(c_{\rm FD}(B)\) 假设成统一正数。机制是：手术过多而可能导致密度失控的部分，已被 N1 单独覆盖；只有手术较少的部分需要有限密度分析。

### 推论 1：一般型主体上的任意吹起和添柄

设 X 为光滑紧致极小复一般型曲面，\(A=c_1^2(X)>0\)。令

\[
M=X\#k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3),\qquad k,\ell\ge0.
\]

限定在原文献／项目已经验证其实际共形供给的范围内（例如原稿使用的 \(p_g(X)\ge1\) 范畴），保留相应的腔室、极化及手柄输入。对所供给的类有

\[
T=A-k-4\ell,\qquad a^2=A-k,\qquad Q=k+4\ell.
\]

存在一个不依赖 X、k、\(\ell\)、度量和 \(\beta\) 的常数 \(c_*>0\)，使

\[
\boxed{\kappa_\beta(g)\ge
c_*\frac{(\beta-2)^2}{\beta^2}.}
\tag{2.3}
\]

**地理估计。**经典 Noether 不等式及曲面 Noether 公式为

\[
p_g(X)\le A/2+2,
\qquad
\chi(X)=12\{1-q_{\rm hol}(X)+p_g(X)\}-A.
\]

它们推出 \(\chi(X)\le35A\)：若 \(A=1\)，整数性给 \(p_g\le2\)，故 \(\chi\le35\)；若 \(A\ge2\)，则 \(\chi\le5A+36\le23A\le35A\)。这只是一个方便的统一界，不主张 35 最佳。

因而

\[
\chi(M)=\chi(X)+k-2\ell\le35A+Q.
\]

由定理 1，可取

\[
c_* =\min\{\varepsilon_N,c_{\rm FD}(106/3)\}.
\]

纯吹起 \(\ell=0\) 已是源稿 Corollary K 的结论；这里将同一逻辑明确接到混合吹起—添柄范畴。不能把这个纯吹起特例重新登记为首次获得。

### 推论 2：实际供给已验证的多一般型主体

令

\[
M=(\#_{i=1}^{r}X_i)\#k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3),
\quad A=\sum_i A_i,\quad A_i=c_1^2(X_i)>0.
\]

**明确附加前置：**该具体连通和须已由普通／BF 等原理论供给所需的实际类，满足 \(p\ge A\) 及 \(a^2=A-k\)。本文不宣称任意 r、任意连通和自动有这个供给。

准确的特征数是

\[
T=A-k-4\ell-4(r-1),\qquad
Q=k+4\ell+4(r-1),
\]
\[
\chi(M)=\sum_i\chi(X_i)+k-2\ell-2(r-1).
\]

于是 \(a^2-T=4\ell+4(r-1)\ge0\)，且

\[
\chi(M)\le35A+Q.
\]

同一个 \(c_*\) 仍然有效。新分析不承担 BF 非消失证明；其准确同余、\(b^+\) 和连接条件仍由供给文献承担。平方为零的主体、任意辛一般型或任意实际单极子流形没有被上述 Noether 论证覆盖，不能删去这些范围限制。

## 3. 任意预定嵌套残余覆盖塔上的低成本恢复

### 引理 2：固定几何块在残余塔中拥有正比例的互不相交位置

设 \(X=\Gamma\backslash\mathbb{CH}^2\) 为紧致光滑复双曲曲面。设

\[
\Gamma\supseteq\Gamma_1\supseteq\Gamma_2\supseteq\cdots,
\qquad [\Gamma:\Gamma_j]<\infty,
\qquad \bigcap_j\Gamma_j=\{1\}.
\tag{3.1}
\]

不要求各子群正规。记 \(X_j=\Gamma_j\backslash\mathbb{CH}^2\)，
\(A_j=c_1^2(X_j)\)。给定任意固定半径 R 和标记球，存在 \(j_0\)，使每个 \(j\ge j_0\) 都含有至少

\[
[\Gamma_{j_0}:\Gamma_j]=A_j/A_{j_0}
\]

个互不相交、等距的该标记球。

**证明。**在普遍覆盖中固定中心 p。由作用的适当不连续性，集合

\[
\mathcal F_R=\{\gamma\in\Gamma\setminus\{1\}:d(p,\gamma p)\le2R\}
\]

有限。嵌套性和交集为平凡群保证存在 \(j_0\) 使
\(\Gamma_{j_0}\cap\mathcal F_R=\varnothing\)。故所选球在 \(X_{j_0}\) 中嵌入。对任意 \(j\ge j_0\)，取这个球在覆盖映射 \(X_j\to X_{j_0}\) 下的全部提升。因球单连通且局部等距，这些提升互不相交、均等距于原球，数量正是覆盖度数。证毕。

这不要求覆盖塔包含某个另行挑选的有限指数正规子群；只需要在它自己某一级嵌入一个固定球。也不需要整个覆盖的单射半径处处趋于无穷。

### 定理 2：严格次四恢复适用于每一条满足 (3.1) 的覆盖塔

在上述预先给定的塔上，取任意符合原平衡条件的整数序列

\[
Q_j=k_j+4\ell_j\to\infty,\qquad h_j=Q_j/A_j\to0,
\]
\[
k_j/Q_j\to2/9,\qquad \ell_j/Q_j\to7/36,
\]
\[
M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}
\#\ell_j(S^1\times S^3).
\]

设一个固定光滑普通吹起单元 C 在完整领口精确匹配 \(\operatorname{Ric}=-g\) 的复双曲球，完整成本为

\[
J_C=\int_C|\operatorname{Ric}+g|^2.
\]

则

\[
\boxed{\limsup_j\frac{\alpha(M_j)}{h_j}
\le\frac{28}{9}+\frac{J_C}{9\pi^2}.}
\tag{3.2}
\]

**证明。**选 R 使单元的整个外领口和缓冲区位于固定球内。引理 2 提供 \(A_j/A_{j_0}\) 个位置。由于

\[
k_j+\ell_j=O(Q_j)=o(A_j),
\]

对充分大 j，可以在互不相交位置放入所有固定吹起块与标准收缩手柄。手柄尺度可逐 j 选择，使总过渡误差为 \(o(Q_j)\)。每个固定单元的体积和总标量改变量有限；因此

\[
V_j=2\pi^2A_j+O(Q_j),\quad
T_j:=\int s_{g_j}+4V_j=O(Q_j),
\]
\[
D_j:=\int|\operatorname{Ric}_{g_j}+g_j|^2
=k_jJ_C+32\pi^2\ell_j+o(Q_j).
\]

对这些真实光滑闭度量，精确恒等式为

\[
\mathcal E(g_j)=
\frac{4D_j-T_j^2/V_j}{4V_j+D_j-2T_j}.
\tag{3.3}
\]

因为 \(Q_j=o(A_j)\)，有 \(T_j^2/V_j=O(Q_j^2/A_j)=o(Q_j)\)，故

\[
\frac{\mathcal E(g_j)}{h_j}
=\frac{k_jJ_C+32\pi^2\ell_j}{2\pi^2Q_j}+o(1).
\]

代入原比例即得 (3.2)。闭流形的实际供给继承原项目／经典理论，不需要把预指定的局部 SW 解逐个拼起来。证毕。

这是对已有单元复制公式的量词加强，不是新的廉价单元构造。它覆盖嵌套且交集平凡的事先指定覆盖塔，不覆盖任意不嵌套覆盖序列，也不覆盖交集非平凡的任意塔。

## 4. 把现有 P 证书接入恢复：不必继续使用稍大的原始 J 证书

源稿 A01 Step22 已证明：每个光滑 exact-CH-ended 单元，在 \(\operatorname{Ric}=-6g\) 规范下有正共形因子 u，满足 \(u\to1\)、\(s_{u^2g}=-24\)，且

\[
P(g)-P(u^2g)
=24\int|du|^2+3\int(\Delta u/u)^2\ge0.
\]

同时 \(J_6(u^2g)=P(u^2g)\)。衰减率与远端截断恢复说明：对任意固定 \(\epsilon>0\)，存在另一个 smooth exact-CH-ended 单元，成本

\[
J_6\le P(g)+\epsilon.
\tag{4.1}
\]

这是源稿的分析前置；本轮没有独立重证全部非紧 Yamabe 分析。

Step33 的原区间文件记录规范化 P 的精确二进有理上端

\[
p_{\rm cert}=
\frac{338806471362324583565914367157197246841}
{340282366920938463463374607431768211456}
<1.
\]

原轮廓还须经过已证明的任意小能量损失光滑化；在 (4.1) 中一起计入 \(\epsilon\) 即可。再将度量乘6，转换为 \(\operatorname{Ric}=-g\) 的领口。四维中的 P 与相应原始残差积分保持所需尺度不变。

对每个固定 \(\epsilon\) 先应用定理 2，再令 \(\epsilon\downarrow0\)，便得

\[
\boxed{
\limsup_j\frac{\alpha(M_j)}{h_j}
\le\frac{28}{9}+\frac89p_{\rm cert}
=3.996144651352101510817871499\ldots
<3.996144652<4.
}
\tag{4.2}
\]

这个数值比直接使用原始 J 证书稍小，原因是利用已证的共形选择消除了可降低的标量残差。这里没有重新做浮点优化或 Arb 积分；数值不是本轮的主要理论增量。它仍是上界，不是新最优值。

极限次序尤其重要：共形尾部截断所需半径可以依赖 \(\epsilon\)，但固定 \(\epsilon\) 后半径固定；残余塔引理给出其后全部足够高层的安放位置。因此不需要未经证明的、关于 \(\epsilon\) 的统一非紧椭圆常数。

## 5. 已有稳定单元能量与全部残余塔的关系

A02 theorem_package_v1 §5.1 已经证明构造层面的次可加性及

\[
\gamma_{\rm bal}
=\lim_{n\to\infty}\frac{\mathfrak P_{8n,7n}}{72\pi^2n}
=\inf_n\frac{\mathfrak P_{8n,7n}}{72\pi^2n}.
\]

**不将这个 Fekete 结论重新登记为本轮发现。**结合引理 2，可以增加下面的覆盖范围陈述：对每条满足 (3.1) 的预定覆盖塔，

\[
\boxed{\limsup_j\alpha(M_j)/h_j\le\gamma_{\rm bal}.}
\tag{5.1}
\]

证明只需先固定 n 和一个近最优完整 \((8n,7n)\)-单元，在原塔上复制

\[
N_j=\min\{\lfloor k_j/(8n)\rfloor,\lfloor\ell_j/(7n)\rfloor\}
\]

次。原比例保证 \(36nN_j/Q_j\to1\)，剩余手术为 \(o(Q_j)\)。按 (3.3) 得上界 \(J_C/(72\pi^2n)\)，随后分别对单元取下确界、对 n 取下确界。每一步均先固定单元再令 j 趋于无穷；无需同时增长的树形紧性定理。

不能反向写成 \(\lim\alpha/h=\gamma_{\rm bal}\)：任意全局竞争度量是否能够以足够小的损失局部化到这些标记单元，仍没有证明。即使局部比能量已存在，其数值本身和是否等于全局极值也尚未确定。

## 6. 原目标现在还缺什么

- **无条件 O10：**定理 1 不包含违反任何固定 (2.1) 的实际供给序列。例如，不能把复一般型的 Noether 界直接应用于任意辛／almost-complex 主体。它因此没有证明全部原实际输入都拥有同一个无密度常数。
- **O11：**定理 2 和 (5.1) 加强了已证竞争构造的覆盖量词；没有给出与 (4.2) 或 \(\gamma_{\rm bal}\) 匹配的下界。严格次四机制已成立，最终最优首项仍待决定。
- 本文未将 openai/math 的固定背景正流分裂或 Ricci-flat 树定理未经输入转换用于原问题。那些方法的迁移仍须独立证明；本文两条结论实际依靠的是已写出的项目定理及下列明确组合。

## 7. 来源与可复核记录

用户底本：`20261007_Einstein_Gaps_Two_Sessions(1).zip`，原文件未修改。

原包内路径：

1. `01_Mathematical_Synthesis.md`：最新结论和修正范围；严格廉价单元、L′／K、供给条件与尚未闭合事项。
2. `sources/Sessions/S1003A02/workspace/notes/step6_theorems_and_O11_rotation.md` §§1–3：L′、纯吹起 Corollary K；后面的旧数值推断不得覆盖更新的廉价单元结果。
3. `sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md`：完整普通吹起单元的正定性、bolt、拓扑、领口及光滑化。
4. `sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md`：无额外标量符号限制的完整端共形选择与精确领口恢复。
5. `sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md` §6：固定 degree-20 轮廓的区间证书。
6. `sources/Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json`：本文使用的原 P 二进上端。
7. `sources/Sessions/S1003A02/workspace/notes/theorem_package_v1.md` §§5.1–5.3：已有次可加性、稳定单元能量与原先的存在型覆盖恢复。
8. 前置：`03_N1_Complete_Inheritance.md` N1 与 `O10_All_Finite_Density.md`；其实际供给、归一化及证明依赖沿用原文，不由本文替代。

外部一手资料：

- C. LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, arXiv:math/0003068, Proposition 3.2 与 Theorem 4.3。普通吹起／柄供给及标准恢复的经典来源。https://arxiv.org/html/math/0003068
- M. Ishida and C. LeBrun, *Curvature, Connected Sums, and Seiberg–Witten Theory*, arXiv:math/0111228, Corollary 11 与 Theorem D 及其明确假设。本文不扩大其 BF 非消失范围。https://arxiv.org/html/math/0111228
- F. Catanese, M. Chen, D.-Q. Zhang, *The Noether inequality for smooth minimal 3-folds*, arXiv:math/0507606, introduction：回顾曲面经典 Noether 不等式；本文只使用二维曲面的经典公式，不使用该文三维新定理。https://arxiv.org/html/math/0507606

`verify_algebra.py` 只检查特征数代数、缺陷比值恒等式、整数地理界和有理上界转换；不验证前置 PDE 或重新运行原区间积分。
