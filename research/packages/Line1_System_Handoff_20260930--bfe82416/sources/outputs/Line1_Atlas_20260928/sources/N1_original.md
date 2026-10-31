# 第一科学主线：单解参数理论对原积分障碍的严格回接

2026年9月28日。

依据：数学快照 0b1490791be560203b86a7d9834dcdc3cbc83b41 的第01、05、07、09卷，以及同日续研报告附录06的单解加强。本篇补出既有证明之间的一条完整推论链；不以此声称全部历史证明或文献首创性已重新认证。

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

## 4. 未完成研究与完成标准

| 问题 | 真正未闭合之处 | 完成标准 |
|---|---|---|
| O10 一般弱积分零端 | 只用原实际方程控制外部也退化时的临界扭率集中；beta趋无穷时现有自测退化 | 原假设下非退化端点间隙，或满足全部原输入的闭流形逃逸序列。先保留chi/A界并删除点态Ricci，已是真实扩大范围 |
| O11 原平衡族最佳首项 | 全部竞争共形类中是否存在比标准手术更低的P成本 | 决定固定原族alpha/h极限或精确上下极限。答案4需inf P=8pi²Q+o(Q)，更低值需同族全局真实构造 |
| 更广实际输入 | 单解已兼容旧SW/BF/Pin应用，但尚未由此给出严格超出旧供给的新拓扑实例 | 一个旧范围未覆盖的自然对象和完整新结论，而非只改抽象名称 |
| 近极小几何与精确实现 | 目标所需的收敛、稳定性或拼接；固定E_D全部Einstein判定仍开放 | 对明确流形或边界证明实现或排除；不能由gap消失自动推出 |

O10和O11是现有理论的加强目标，不是I40/I41成立所欠缺的证明。若直接下界与恢复构造决定O11，则数值问题已经完成；无需把全部近极小几何分类再追加为该问题的完成条件。

两者误差尺度不同：O10排除体积V尺度的归一化缺陷趋零；O11要求误差为o(Q)，其中Q=Ah可能远小于V。普通o(V)不能自动决定首项。

## 5. 已排除的低收益路线

1. 所有现有有限参数预算兼容形式零端数据。换beta、线性组合或优化这些预算不能自行闭合O10；须新增实际微分信息。形式数据不是实际反例。
2. 零端不是近平行端：现有归一化中平均二形式导数能量趋8/3。不能复制beta=2的近平行闭合。
3. 固定受控外部的延拓成本尚未覆盖外部也退化的情况。
4. O11替换引理排除过贵单元，尚不排除过便宜单元。
5. I41通用常数优化不足以到系数4；X06否定普遍删除Weyl支付的策略。必须使用原平衡族的额外结构。
6. 带标记分解、泡树、Gamma极限均是可选方法，不是必须先完成的理论形态。

## 6. 来源定位与核查

- 第07卷，Source 1 Theorem 1.2：原积分障碍；functional pencil Source 3 §8：beta=8精确式。
- 第01卷，Source 2 §2.3：I51(2.15)及去类平方成本。
- 第05卷，I41 Part I §§1–3：曲率强制、共形比较；§5：cover-compatible及Pin下降。
- 续研报告附录06 §§1–4：单解参数估计和线性机制；§5：有限参数预算在零端的局限。
- 第09卷最后任务书 §§3、6、7：O10/O11原目标及精确实现。

本次由主会话和两条独立核查分别检查(N1)的常数、Chern–Weil恒等式、共形比较和供给量词；新增推论依赖上述已写出的前置证明。
