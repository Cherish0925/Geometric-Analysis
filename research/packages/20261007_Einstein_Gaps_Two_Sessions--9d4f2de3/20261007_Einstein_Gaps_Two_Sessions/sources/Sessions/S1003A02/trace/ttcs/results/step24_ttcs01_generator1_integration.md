# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 24,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step24_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step24_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop mathematically serious possible routes from Theorem C to an absolute lower bound for the complete constant-scalar ACH O(-1) cell energy 4 Delta W_+ + 48 RV > -8 pi^2. Use the fact that CH has |W+|^2=24, first-order Weyl and volume channels cancel in kernel directions, and zero cost would require a definite Weyl deletion. Explore whether a two-scale localization through a half-conformally-flat region and a localized hyperbolic renormalized-volume comparison is coherent, what exact lemma would be needed, and what counter-mechanisms (oscillation, concentration, curved neck, collapse) defeat naive versions. Compare this route with the global bulk-to-cell passage and identify the most load-bearing theorem worth constructing, without treating a Lambda>1 trade-off as sufficient.

## Integrated Scientific Memo

## 从 Theorem C 到绝对 ACH 单胞间隙：可行路线与关键缺口

令
\[
X=\mathcal O(-1)\to \mathbb {CP}^{1},
\]
固定标准球面 CR 无穷远，并在复双曲归一化
\[
\Ric_{\mathrm{CH}}=-6g_{\mathrm{CH}},\qquad s=-24,\qquad |W^+_{\mathrm{CH}}|^2=24
\]
下考虑完整 ACH 度量。对已经 Yamabe 归一化的 \(g\)，Theorem C 给出
\[
P(g):=\int_X|\Ric_g^\circ|^2\,d\mu_g
   =8\pi^2+\mathcal A(g),\qquad
\mathcal A(g):=4\Delta W_+(g)+48\,\RV_{\mathrm{CH}}(g). \tag{1}
\]
因此目标
\[
4\Delta W_++48\RV>-8\pi^2
\]
等价于逐点 \(P(g)>0\)；真正的“绝对间隙”则是更强的
\[
\inf_gP(g)=:\varepsilon_*>0,
\qquad
\mathcal A(g)\ge-8\pi^2+\varepsilon_* . \tag{2}
\]

逐点严格性可由“标准无穷远不存在 Einstein 填充”推出；(2) 还必须排除 \(P(g_j)\to0\) 的退化序列。后者才是核心困难。

### 1. 零成本要求有限量的 Weyl 删除

在固定相对边界规范下，相对签名公式应写成
\[
\Delta W_+(g)-\int_X|W^-_g|^2=-12\pi^2. \tag{3}
\]
记
\[
B_-(g)=\int_X|W^-_g|^2.
\]
由 (1)、(3) 得
\[
P(g)=4B_-(g)+48\RV(g)-40\pi^2, \tag{4}
\]
以及
\[
\Delta W_+(g)
=-12\pi^2+B_-(g)
=-2\pi^2-12\RV(g)+\frac14P(g). \tag{5}
\]
所以若 \(P(g_j)\to0\) 且至少有
\[
\RV(g_j)\ge-o(1),
\]
则
\[
-\Delta W_+(g_j)
=2\pi^2+12\RV(g_j)+o(1)
\ge2\pi^2-o(1). \tag{6}
\]
这不是无穷小效应：由于 CH 的 \(W^+\) 密度为 \(24\)，最小的 \(2\pi^2\) 删除量相当于完全删除体积
\[
\frac{2\pi^2}{24}=\frac{\pi^2}{12}
\]
的 CH Weyl 能量。同时
\[
B_-(g_j)+12\RV(g_j)=10\pi^2+o(1). \tag{7}
\]
故零成本序列必须把一部分 CH 的自对偶 Weyl 背景删除，并生成携带 \((-1)\)-拓扑的反自对偶曲率；它不能只是一个趋零的小扰动。

公式 (3)–(7) 的使用依赖相对签名边界项及定向约定，构造正式证明时必须把它作为独立相对 Chern–Weil 引理核实。它与 \(\Delta W_+=-12\pi^2+B_-\) 一致；不能把 \(-2\pi^2\) 误写成该拓扑恒等式的常数项。

### 2. 为什么 \(\Lambda>1\) 的通道贸易不够

估计
\[
4\Delta W_+\ge-\Lambda\,48\RV-\eta,\qquad \Lambda>1,
\]
只给出
\[
P-8\pi^2\ge-(\Lambda-1)48\RV-\eta,
\]
除非另有 \(\RV\) 上界，否则没有绝对下界。

更本质地，在 CH Kähler–Einstein 的 Burns 核方向，
\[
4\Delta W_+=-a x_0+o(x_0),\qquad
48\RV=a x_0+o(x_0).
\]
一阶项相消，组合能量由二阶颈相互作用决定；约化计算给出
\[
\frac{P}{8\pi^2}
=1-9x_0^2\log(1/x_0)+O(x_0^2).
\]
因此任何纯线性锥形不等式都既看不到这一负二阶效应，也看不到 \(P\) 的拓扑正下界。数值上
\[
-\frac{4\Delta W_+}{48\RV}\approx1.03\text{--}1.06
\]
也已排除系数小于 \(1\) 的普遍贸易。

### 3. 两尺度双曲局部化何时成立

一个相干的分尺度图景是：

1. 外部标准 CH 区域；
2. 删除 CH \(W^+\) 的第一过渡层；
3. 一个介观实双曲平台，接近曲率 \(-2\) 的 \(H^4\)；
4. 内层生成异常类及 \(W^-\) 电荷的拓扑核。

因为标量曲率均为 \(-24\)，
\[
\mathcal R_g-\mathcal R_{H}
=
\begin{pmatrix}
W^+&(\Ric^\circ)^\#\\
((\Ric^\circ)^\#)^*&W^-
\end{pmatrix}. \tag{8}
\]
所以“半共形平坦区”本身不够：\(W^+\approx0\) 与 \(P\approx0\) 只可能给出反自对偶 Einstein 区域；要得到 \(H^4\) 平台，还必须有
\[
W^-\approx0,\qquad \Ric^\circ\approx0. \tag{9}
\]

若存在包围异常类的长环带
\[
A_j\simeq S^3\times[-L_j,L_j],\qquad L_j\to\infty,
\]
且在固定规范下
\[
g_j\to g_H\quad\text{于 }C^{2,\alpha}_{\mathrm{loc}}(A_j), \tag{10}
\]
则可在环带中部切割，把外侧替换成精确 \(H^4\)，得到 \(D\#\overline{\CP}^{\,2}\) 上的精确 \(H^4\)-外部度量 \(\widetilde g_j\)，并期望
\[
P(\widetilde g_j)
\le P(g_j;\text{内侧})+o(1). \tag{11}
\]
Yamabe 归一化为 \(q_j=u_j^2\widetilde g_j\)、\(s_{q_j}=-24\) 后，由共形选择恒等式
\[
P(q_j)\le P(\widetilde g_j). \tag{12}
\]
实双曲端比 CH 端更有利：\(H^4_{K=-2}\) 的对应共形线性化有严格谱间隙，而 CH 端处在临界谱位置。

对所得实双曲单胞，
\[
P(q_j)
=8\pi^2+4\int_X|W^+_{q_j}|^2
 +48\RV_H(q_j). \tag{13}
\]
因此为排除 \(P(q_j)\to0\)，不必一开始证明完整的
\[
\RV_H(q)\ge0. \tag{14}
\]
如下序列版已经足够：
\[
\boxed{\quad
\RV_H(q)\ge-\omega(P(q)),\qquad
\omega(t)\to0\quad(t\downarrow0).
\quad} \tag{15}
\]
由 (13) 即有
\[
P(q)\ge8\pi^2-48\omega(P(q)),
\]
这与 \(P(q)\to0\) 矛盾。

因此两尺度路线所需的精确局部引理是：

> **双曲包围—切割引理。**  
> 若标准 ACH、\(s=-24\) 的 \(g_j\) 满足 \(P(g_j)\to0\)，且存在如 (10) 的长 \(H^4\)-环带包围异常类，则可切割、修补并 Yamabe 归一化，构造精确 \(H^4\)-外部的 \(q_j\)，满足
> \[
> P(q_j)\le P(g_j)+o(1).
> \]
> 若实双曲相对体积满足 (15)，则这种包围不可能出现在零成本序列中。

切割部分需要控制：

* 环带上的 \(C^{2,\alpha}\) 误差及插值曲率；
* 相对 Chern–Weil 边界项；
* Yamabe 因子的能量与衰减；
* \(P\) 在切割和共形归一化中的 \(o(1)\) 损失。

但最困难的并不是切割，而是从 \(P(g_j)\to0\) 推出长环带 (10)。

### 4. 为什么通道删除不自动产生双曲平台

\(\Delta W_+\) 是带符号的相对积分，而不是正测度。有限量删除可以通过以下方式实现：

* 在较大区域轻微降低 \(|W^+|^2\)；
* 在小区域完全删除；
* 在不同区域让低于和高于 CH 背景的贡献互相抵消；
* 让 \(W^+\) 删除和 \(W^-\) 生成发生在同一尺度。

最后一种情形正是“弯曲颈”：CH 的自对偶曲率状态直接转换为携带异常拓扑的反自对偶状态，中间没有 \(W^+\approx W^-\approx0\) 的平台。已知非标准 Rossi 无穷远上的完整 ACH Einstein 填充说明这种连接器机制确实存在；因此标准球面 CR 边界必须进入刚性定理，局部曲率代数不足以排除它。

### 5. 四类反机制

#### (a) 振荡、弥散和向无穷远漂移

CH 半径 \(R\) 的固定宽度壳层体积约为 \(e^{4R}\)。振幅为 \(a_R\) 的扰动，其各通道的一阶响应可为
\[
a_Re^{4R},
\]
而二次 Einstein 缺陷为
\[
a_R^2e^{4R}.
\]
取 \(a_R\sim e^{-4R}\)，可能使各相对通道发生 \(O(1)\) 改变，而二次成本趋零。拓扑中性的壳层在总组合 \(\mathcal A=P-8\pi^2\) 中必须一阶相消，但它可以把“删除发生的位置”任意推向外部。

故必须固定加权渐近规范并证明通道的加权紧性，或把近极小序列替换为满足近似 Euler–Lagrange 方程的序列；仅凭积分恒等式无法局部化。

#### (b) 曲率集中

四维 \(P\) 尺度不变，所以缩小拓扑核不会自动降低成本。若出现近欧氏 \(S^3\) 颈，缩放极限是标量平坦 ALE 泡。Lemma Q/Q′ 对一个 \((-1)\)-类给出
\[
P_{\mathrm{bubble}}\ge8\pi^2
\quad\text{或}\quad
P(U)\ge8\pi^2-C\varepsilon. \tag{16}
\]
这不仅排除 \(P\to0\) 的普通 Burns 集中，而且因为已认证 CH 单胞低于 \(8\pi^2\)，也表明其近极小序列不能经过任意精确的平坦颈。

非平凡端群的多层 orbifold 泡树则需要把每层的签名 \(\eta\)-项、端群和紧支撑交叉形式统一记账；单个泡的估计不足以证明原始平方 \(-1\) 类无法分裂或逃逸。

#### (c) 弯曲 Einstein 颈

若两种手性过渡不分尺度，\(P\to0\) 可能产生完整 \(s=-24\) Einstein 连接器。真正需要的是：

\[
\text{标准球面 CR 无穷远上不存在 }
\mathcal O(-1)\text{ 的完整 ACH Einstein 填充}, \tag{17}
\]
最好加强为模空间在该边界值处的 properness。精确 CH collar 的解析延拓非存在结论不能直接用于仅渐近 CH 的度量。

#### (d) 塌缩

注入半径趋零时未必存在可切割的 \(S^3\) 环带。拓扑可进入圆或环面纤维化的小体积区，而 \(L^2\) 曲率仍保持临界尺度。需要在局部覆盖上描述极限，并证明原始 \((-1)\)-类不能在 ALE/ALF/ALG 或低维塌缩模型中零成本消失。

### 6. 把 \(L^2\)-小量提升为几何平台的分析机制

裸条件 \(P=\|\Ric^\circ\|_2^2\ll1\) 不控制曲率导数；Bianchi 恒等式只给出
\[
\delta W\sim\nabla\Ric^\circ.
\]
可行做法是先作变分选择：在 \(s=-24\)、固定标准 CR 无穷远下，用小的曲率导数惩罚项选取近极小度量，使其满足近似四阶临界方程
\[
\nabla^*\nabla\Ric^\circ
+\Rm*\Ric^\circ
+\Ric^\circ*\Ric^\circ
=\text{小残差}. \tag{18}
\]
配合统一 Sobolev／harmonic-radius 控制，可得到 \(\varepsilon\)-正则性，把 \(L^2\)-小的 \(\Ric^\circ\) 提升为环带上的光滑近 Einstein 性。

等价的手性连接观点是考虑 \(\Lambda^+\) 上 Levi-Civita 联络 \(A^+\)：
\[
(F_{A^+})^+=W^++\frac{s}{12}I,\qquad
(F_{A^+})^-=(\Ric^\circ)^\#. \tag{19}
\]
于是 \(P\) 是 \(A^+\) 的反自对偶曲率能量。\(P\to0\) 使 \(A^+\) 近似自对偶，但只有在获得近 Yang–Mills 方程和规范紧性后，才能证明：

* 两次手性过渡分离，产生 \(H^4\) 平台；或
* 过渡保持耦合，收敛到完整 Einstein 连接器。

这正是两尺度路线与弯曲颈路线之间应有的严格二分。

### 7. 最承重的定理

最值得构造的不是另一个 \(\Lambda>1\) 通道估计，而是下述拓扑保持的 ACH 近 Einstein 紧致性定理。

> **标准 ACH 平方 \(-1\) 类承载定理。**  
> 设 \(g_j\) 是 \(X=\mathcal O(-1)\) 上完整 \(s=-24\) 度量，具有固定标准球面 CR 无穷远和统一加权规范，且
> \[
> P(g_j)\to0.
> \]
> 经不增加 \(P\) 超过 \(o(1)\) 的变分替换后，序列分解为：
> 1. 厚部完整 ACH Einstein 分量；
> 2. 有限个缩放 Ricci-flat 集中分量；
> 3. 不携带二阶同调的颈；
> 4. 在局部覆盖上可分类的塌缩分量；
> 并且紧支撑交叉形式
> \[
> [-1]
> \]
> 等于各承载分量交叉形式的正交和，原始平方 \(-1\) 类不能通过颈或塌缩奇集消失。
>
> 此外，在非塌缩厚部，手性过渡要么分尺度并产生长 \(H^4\) 包围环带，要么产生具有同一标准 CR 无穷远的完整 ACH Einstein 连接器。

结合以下三个输入即可得到绝对间隙：

1. 双曲包围情形由切割引理和 (15) 排除；
2. 标准 CR Einstein 连接器由 (17) 排除；
3. Ricci-flat 泡树和塌缩模型不能零成本承载原始 \((-1)\)-类。

于是不存在 \(P(g_j)\to0\)，从而存在 \(\varepsilon_*>0\) 使
\[
P(g)\ge\varepsilon_*,
\qquad
4\Delta W_+(g)+48\RV(g)
\ge-8\pi^2+\varepsilon_* . \tag{20}
\]

这一定理最承重，因为它同时处理振荡、集中、弯曲颈和塌缩，并把局部双曲体积比较放在其真正适用的“分尺度”分支中。

### 8. 与全局 bulk-to-cell 通路的关系

全局闭流形问题还多出若干层：

* 用实际规范场或等价微分对象识别 CH bulk；
* 将每个异常拓扑类分配给具体单胞或泡树；
* 区分非塌缩与塌缩区；
* 将渐近 CH 分量截断为精确 collar，且控制相互作用误差；
* 证明各单胞能量的近似可加性。

因此局部单胞间隙不会自动解决全局下界。反方向也不宜把完整单胞植入越来越大的紧 CH 覆盖来反推单胞间隙：截断半径 \(R\) 的单胞占据约 \(e^{4R}\) 的 CH 体积，允许的打包密度约 \(e^{-4R}\)，现有只在正密度上有效的全局拓扑估计会失去逐单胞强度。

但上述承载定理正是两条路线的公共核心：它既给出孤立 \((-1)\)-类的正成本，也为全局分解提供“拓扑不会从颈、泡树或塌缩区无代价消失”的缺失环节。

### 9. 最直接的判别计算

现有对角单胞可计算累积量
\[
D_+(r)=-\Delta W_+(r),\qquad
B_-(r)=\int_{t\le r}|W^-|^2,\qquad
P(r),\qquad \RV(r).
\]
若存在两尺度 \(H^4\) 平台，应看到 \(D_+\) 基本完成后 \(B_-\) 才开始增长，并有一段
\[
|W^+|+|W^-|+|\Ric^\circ|\ll1.
\]
若两条曲线在同一径向尺度同步变化，则当前低能单胞采用的是弯曲连接器，而非双曲平台。该计算不会证明一般定理，但能决定双曲局部化是描述已知近优构造的主机制，还是只处理紧致性定理中的一个退化分支。

综上，两尺度半共形平坦／实双曲局部化是严格相干的，但只覆盖手性过渡分离的情形。最关键的新结果应是带拓扑记账、变分正则化和塌缩分析的标准 ACH 近 Einstein 紧致性定理；局部双曲重整化体积估计 \(\RV_H\ge-\omega(P)\) 是其中强有力但非独立完备的一环。