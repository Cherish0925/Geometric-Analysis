# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step26_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step26_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the proposed Step-26 action-budget matching note together with the peer's chiral transgression note as a mathematical verifier. Check every normalization, the dimension-four rescaling of P and scalar curvature, the passage from the two chiral identities to the max lower bound, the controlled collapsed charge substitution, and the bound on the kernel C+4X=0. Identify hidden hypotheses needed for limits of charges and for applying a whole-cell budget to a prefix. Then propose the sharpest theorem statement that is actually supported, including how to formulate the missing high-shear alternative without silently assuming Einstein equations or bounded geometry. Focus on substantive mathematical corrections, not presentation.

## Integrated Scientific Memo

# 核验结论与可支持的最强定理

## 1. 四维缩放：正确，但极限论断需补假设

令
\[
g_j^\#=b_j^{-2}g_j .
\]
常数缩放下，作为 \((0,2)\)-张量，
\[
\Ric_{g_j^\#}=\Ric_{g_j},\qquad s_{g_j^\#}=b_j^2s_{g_j},
\]
且
\[
\Ric^\circ_{g_j^\#}=\Ric^\circ_{g_j},\qquad
|\Ric^\circ_{g_j^\#}|_{g_j^\#}^2=b_j^4|\Ric^\circ_{g_j}|_{g_j}^2,\qquad
dV_{g_j^\#}=b_j^{-4}dV_{g_j}.
\]
因此四维中
\[
\widehat P(g_j^\#)=\frac1{8\pi^2}\int|\Ric^\circ_{g_j^\#}|^2\,dV_{g_j^\#}
=\widehat P(g_j).
\]
同样，\(\int s^2dV\) 也是尺度不变的。

若 \(\Ric_{g_j}=-6g_j\)，则
\[
\Ric_{g_j^\#}=-6b_j^2g_j^\#,
\]
故任何 \(C^2_{\rm loc}\) pointed 光滑极限均 Ricci-flat。

一般竞争度量的结论
\[
s(g_j^\#)=-24b_j^2\to0
\]
只在每个 \(g_j\) 都满足逐点常标量曲率条件 \(s_{g_j}\equiv-24\) 时成立。仅有 exact-CH end 或无穷远归一化不足以推出这一点。若不限定为常标量曲率类，必须另假设
\[
b_j^2s_{g_j}\to0
\quad\text{于 rescaled 紧集上，例如在 }C^0_{\rm loc}.
\]

此外，能量有界本身不给出 rescaled pointed 极限；至少需要尺度归一化的一阶紧性以及足够的二阶弱紧性。若已有 \(C^1_{\rm loc}\) 收敛和 \(W^{2,2}_{\rm loc}\) 控制，则可用弱下半连续性得到标量平坦、局部有限 Ricci action 的极限。仅有
\[
\widehat P(g_j)\le c
\]
不能推出该极限 Ricci-flat；后者需要原序列 Einstein，或局部 defect 趋零。

---

## 2. Chiral 归一化和 bolt 电荷

在
\[
\int_{S^3}\sigma_{123}=2\pi^2
\]
的约定下，
\[
\widehat P=\frac1{8\pi^2}\int|\Ric^\circ|^2dV
=\frac14\int W|\Ric^\circ|^2dt.
\]
Hitchin–Thorpe 密度精确给出
\[
\widehat P
=
\frac1{2\pi^2}\int|W^\pm|^2dV
+\frac1{96\pi^2}\int s^2dV
-(2\chi\pm3\tau).
\]
因此 chiral 恒等式中的系数
\[
\frac1{2\pi^2},\qquad \frac1{96\pi^2}
\]
均正确，没有额外因子 \(2\)。

在“CH 的 Kähler Weyl 曲率属于 \(W^+\)”的固定取向下，\(O(-1)\) 盘丛满足
\[
\chi=2,\qquad \tau=-1,
\]
故 bolt 电荷为
\[
\mathfrak b_+=2\chi+3\tau=1,\qquad
\mathfrak b_-=2\chi-3\tau=7.
\]
若反转取向或使用非保向槽置换，两种 chirality 会交换；因此 collapsing slot 和取向必须在序列中固定，或先作保向循环重标。

---

## 3. 两条 chiral 恒等式给出的精确前缀预算

设 \(C_T=[\mathrm{bolt},\Sigma_T]\)，并记
\[
S_T=\frac1{96\pi^2}\int_{C_T}s^2dV,\qquad
Q_{\pm,T}=\frac1{2\pi^2}\int_{C_T}|W^\pm|^2dV.
\]
从 \([\varepsilon,T]\) 积分再令 \(\varepsilon\downarrow0\)，光滑 \(O(-1)\) bolt 给出
\[
\widehat P(C_T)
=\mathfrak b_+(\Sigma_T)-1+Q_{+,T}+S_T
=\mathfrak b_-(\Sigma_T)-7+Q_{-,T}+S_T.
\]
故最强的直接端点推论是
\[
\boxed{
\widehat P(C_T)\ge
\max\left\{
0,\,
\mathfrak b_+(\Sigma_T)-1+S_T,\,
\mathfrak b_-(\Sigma_T)-7+S_T
\right\}.}
\tag{3.1}
\]
Step 26 的
\[
\widehat P(C_T)\ge
\max\{0,\mathfrak b_+-1,\mathfrak b_--7\}
\]
是正确但较弱的版本，因其丢弃了公共的 \(S_T\) 项。两种 chiral 下界不能相加，因为它们控制的是同一个 \(\widehat P(C_T)\)。

对分割 \(0=t_0<\cdots<t_m=T\)，每段可以独立选择较强 chirality，得到进一步的路径型估计
\[
\widehat P[0,T]\ge
\sum_{k=1}^m
\left[
S_k+\max\{0,\Delta_k\mathfrak b_+,\Delta_k\mathfrak b_-\}
\right].
\tag{3.2}
\]
这是端点总差所不能捕捉的混合向上变差。

### whole-cell 预算何时可用于 prefix

若 whole-cell action 是实际非负积分
\[
\widehat P(g_j)=\frac1{8\pi^2}\int_{M_j}|\Ric^\circ|^2dV,
\]
且 \(C_{T,j}\subset M_j\) 是可测前缀，则
\[
\widehat P(C_{T,j})\le\widehat P(g_j)
\]
仅由非负性成立；不需要 Einstein 方程。exact-CH tail 上 \(\Ric^\circ=0\)，亦无额外代价。

不能未经证明把 renormalized Weyl-volume 表达式当作有单调性的局部预算；其各项可有符号或在无穷端分别发散。前缀论证必须使用实际 \(\int|\Ric^\circ|^2\)。

---

## 4. Controlled collapse 电荷：代数正确，收敛假设需按序列表述

取 sections \(\Sigma_j\)，令 \(z_j\to0\)，并假设归一化一阶喷射收敛
\[
\frac{x_j}{z_j^3}\to X,\qquad
\frac{p_j}{z_j}\to P,\qquad
\frac{\chi_j}{z_j}\to C,\qquad
\frac{\eta_j}{z_j}\to N.
\tag{4.1}
\]
这比在“单个 section”上写 little-\(o\) 更精确。对应的 chiral connection 变量满足
\[
\begin{aligned}
u_f&\to P+\frac23C+\frac13N+2X,\\
u_g&\to P-\frac13C+\frac13N-2X,\\
u_h&\to-2,
\end{aligned}
\]
以及
\[
\begin{aligned}
w_f&\to P+\frac23C+\frac13N-2X,\\
w_g&\to P-\frac13C+\frac13N+2X,\\
w_h&\to2.
\end{aligned}
\]
代入
\[
\mathfrak b_+=2-\sum_i u_i^2-u_fu_gu_h,\qquad
\mathfrak b_-=\sum_i w_i^2-w_fw_gw_h-2
\]
得到
\[
\boxed{
\mathfrak b_+\to-2-(C+4X)^2,\qquad
\mathfrak b_-\to2+(C-4X)^2.}
\tag{4.2}
\]
\(P,N\) 的消去在该 base-scale first-jet chart 中是精确代数事实。

这里需要明确：

* 电荷只依赖归一化一阶喷射；无需二阶导数、Einstein 方程或曲率有界。
* 若把 \(x=Xz^3+o(z^3)\) 当作整个 collar 上的可微函数渐近式，再对其求导，会额外产生运动学关系；这不能与独立的一阶喷射参数 \(C\) 混用。
* \(x=O(z^3),\chi=O(z)\) 仅是 finite-charge first-jet 条件，不是 bounded-geometry 条件。固定 base scale 时，orbit curvature 有界通常至少要求 \(x=O(z^6)\)，mixed curvature 还要求类似 \(\chi=O(z^4)\) 及二阶径向控制。因此脚本中“finite orbit curvature”的注释应改为“finite-charge normalized first-jet”。

令
\[
S_j=\frac1{96\pi^2}\int_{[\mathrm{bolt},\Sigma_j]}s_j^2dV_j.
\]
由 (3.1) 与 (4.2)，更强的极限形式为
\[
\liminf_j\widehat P([\mathrm{bolt},\Sigma_j])
\ge
\max\left\{
0,\,
\liminf_j\!\left[S_j-3-(C+4X)^2\right],
\,
\liminf_j\!\left[S_j+(C-4X)^2-5\right]
\right\}.
\tag{4.3}
\]
特别地，丢掉 \(S_j\ge0\) 后，
\[
\boxed{
\liminf_j\widehat P([\mathrm{bolt},\Sigma_j])
\ge \max\{0,(C-4X)^2-5\}.}
\tag{4.4}
\]
所以 Step 26 的 controlled charge substitution 正确；plus channel 在该端点给出负差
\[
-3-(C+4X)^2,
\]
有用的是 minus channel。

---

## 5. kernel \(C+4X=0\) 的界及数值修正

若
\[
\widehat P(g_j)\le c+o(1),
\]
由前缀单调性和 minus 恒等式，
\[
\limsup_j\bigl((C-4X)^2+S_j\bigr)\le c+5.
\tag{5.1}
\]
因而
\[
(C-4X)^2\le c+5.
\]
在 plus-charge kernel
\[
C+4X=0
\]
上，\(C=-4X\)，故
\[
\boxed{
64X^2+\limsup_jS_j\le c+5,\qquad
|X|\le\frac{\sqrt{c+5}}8.}
\tag{5.2}
\]
对 \(c=0.99585\)，
\[
\frac{\sqrt{5.99585}}8=0.3060803\ldots.
\]
因此应写
\[
|X|\le0.306081
\]
或近似 \(|X|\lesssim0.30608\)，不能写严格的 \(|X|<0.306\)。

对 \((X,C)=(1,-4)\)，
\[
\mathfrak b_-\to2+64=66,
\]
相对 bolt 值 \(7\)，故
\[
\liminf_j\widehat P([\mathrm{bolt},\Sigma_j])\ge59+\liminf_jS_j.
\]
这比“不能在 action \(<1\) 内达到”强得多。它是 \(z_j\to0\) 的渐近结论；若要赋予固定有限 \(z\) section，需另有定量 remainder 估计。

---

## 6. 当前材料真正支持的定理

### 定理（对角 \(O(-1)\) bolt 的 chiral prefix budget）

设
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2
\]
是 \(O(-1)\) 盘丛上的光滑对角 Bianchi–IX 度量，在 \(t=0\) 具有正确 Hopf 周期的光滑 bolt。固定 CH 为 \(W^+\)-Kähler 的取向，并保持槽标号一致。则对任意主轨道 \(\Sigma_T\)，
\[
\begin{aligned}
\widehat P([0,T])
&=\mathfrak b_+(\Sigma_T)-1
+\frac1{2\pi^2}\int_{[0,T]}|W^+|^2dV
+\frac1{96\pi^2}\int_{[0,T]}s^2dV,\\
&=\mathfrak b_-(\Sigma_T)-7
+\frac1{2\pi^2}\int_{[0,T]}|W^-|^2dV
+\frac1{96\pi^2}\int_{[0,T]}s^2dV.
\end{aligned}
\tag{6.1}
\]
故 (3.1) 成立。

若 \(g_j\) 是此类度量，
\[
\widehat P(g_j)\le c+o(1),
\]
且存在 collapsed sections \(\Sigma_j\) 满足 (4.1)，则电荷极限 (4.2)、前缀下界 (4.3) 及预算约束 (5.1) 成立。特别地，在 \(C+4X=0\) 上有 (5.2)。

该定理不使用 Einstein 方程，也不要求曲率一致有界。

### 必须显式列出的假设

1. bolt 是光滑 \(O(-1)\) bolt，而非 orbifold bolt；
2. 取向、Hopf 周期及 collapsing slot 在序列中一致；
3. charges 的使用基于其精确一阶喷射多项式，而不是仅凭几个模型值；
4. 电荷极限要求归一化一阶喷射逐项收敛；
5. bolt 到 section 的曲率积分有限，以便令内截断趋向 bolt；
6. whole-cell 数值控制的是实际非负 Ricci-defect action；
7. 若主张 rescaled 极限 scalar-flat，需 \(s_j\equiv-24\) 或 \(b_j^2s_j\to0\)；
8. 若主张存在 rescaled 几何极限，需另加 normalized \(C^1\)/\(W^{2,2}\) 紧性。

---

## 7. high-shear alternative 的正确表述

“第一次进入 controlled class”目前并非良定义：little-\(o\) 或归一化喷射收敛是 sections 序列的性质，不是单条轨道上的闭条件。可固定 \(L\) 并定义有限尺度管
\[
\mathcal K_L(z)=
\left\{
|x|\le Lz^3,\quad
|p|\le Lz,\quad
|\chi|\le Lz,\quad
|\eta|\le Lz
\right\}.
\]
对任意 \(z_j\to0\) 的 sections，令
\[
\mathcal D_j=
\max\left\{
\frac{|x_j|}{z_j^3},
\frac{|p_j|}{z_j},
\frac{|\chi_j|}{z_j},
\frac{|\eta_j|}{z_j}
\right\}.
\]
取子序列后，现有理论只支持如下二分：

1. **受控喷射分支：** \(\mathcal D_j\) 有界。再取子序列后四个归一化量收敛，适用 (4.2)–(5.2)。
2. **非紧/high-shear 分支：** \(\mathcal D_j\to\infty\)。此时仍有精确原始电荷约束
   \[
   \mathfrak b_+(\Sigma_j)+S_j\le1+c+o(1),\qquad
   \mathfrak b_-(\Sigma_j)+S_j\le7+c+o(1),
   \tag{7.1}
   \]
   但不能代入 controlled 公式 (4.2)。

离开 \(\mathcal K_L\) 不等于电荷发散、曲率发散或 action 有正下界。尤其光滑 Einstein bolt collar 附近可有
\[
p\sim \frac1{3z^2},\qquad \eta\sim-\frac1{z^2},
\]
而 \(\Ric^\circ=0\)。因此不存在由现有材料支持的、只依赖终端 \((\mathcal D_\Sigma,W_\Sigma)\) 且随 shear 增长的普遍正函数
\[
\widehat P\ge\Psi(\mathcal D_\Sigma,W_\Sigma).
\]
Step 26 中这类公式只能作为研究目标，不能陈述为定理。

正确的缺失对象是路径值函数，而非终端罚函数。例如在固定的、与 bolt collar 分离的 collapsed transition interval 上定义
\[
V_{\rm hs}
=
\inf
\frac14\int W
\left(
\frac34H^2+\frac23E^2+\frac12D^2
\right)dt,
\tag{7.2}
\]
其中路径：

* 从光滑 regular bolt 数据出发并最终接到指定 exact-CH 数据；
* 满足完整的对角 Ricci 运动学/演化恒等式；
* 将 \(H,E,D\) 视为 trace-free Ricci controls，而不设为零；
* 若 admissible class 是常标量曲率类，则另施加 \(s=-24\)；
* 在指定 transition interval 上避开 \(\mathcal K_L\)；
* 使用实际 \(W(t)\)，而非 CH 模型权重。

每条 high-shear 路径按定义支付至少 \(V_{\rm hs}\)。尚未证明的核心是
\[
V_{\rm hs}>0
\]
或其显式定量下界。若不固定 transition interval 的几何尺度并排除纯 bolt collar，该值可因局部 Einstein 轨道而退化为零。

---

## 8. Fibre/base pinning：系数正确，但不能替代 high-shear 定理

由
\[
|\Ric^\circ|^2
=\frac34H^2+\frac23E^2+\frac12D^2,\qquad
\widehat P=\frac14\int W|\Ric^\circ|^2dt,
\]
有
\[
\widehat P\ge\frac16\int WE^2dt.
\]
结合
\[
\widetilde B'=F_\beta-\frac14E
\]
和 Cauchy–Schwarz，
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le
\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2}.
\tag{8.1}
\]
所以
\[
\widehat P\ge \frac{8C^2}{3I}
\]
的系数正确，其中 \(C\) 是 drift-corrected mismatch，\(I=\int W^{-1}dt\)。

对 exact CH tail，
\[
I(T)=
\frac1{2\sinh^2T}
-\frac12\log(1+\sinh^{-2}T).
\]
但该表达式只能用于 exact CH 区间，或已有独立比较
\[
\int W_g^{-1}dt\le I(T).
\]
一般 connector 必须保留实际的 \(\int W^{-1}dt\)，并控制 \(\int F_\beta dt\)。终端体积 \(W_\Sigma\) 不能替代路径积分。

---

## 9. 最终修正判断

Step 26 的核心受控分支是正确的：

* 四维 \(\widehat P\) 尺度不变；
* 两条 chiral 下界应取最大值而非相加；
* controlled charge 极限及 \(P,N\) 消去正确；
* \((C-4X)^2\le c+5\) 和 kernel 约束正确。

必须修正或限定之处是：

1. 保留可用的 scalar term \(S_T\)；
2. 将 \(|X|<0.306\) 改为 \(|X|\le0.306081\)；
3. 明确 \((1,-4)\) 的渐近 prefix 代价至少为 \(59\)；
4. scalar-flat blow-up 需常标量曲率或相应缩放收敛假设；
5. rescaled 极限存在需额外紧性；
6. “first controlled section”需改为有限 \(L\) 的喷射管或 sections 序列二分；
7. \(x=O(z^3),\chi=O(z)\) 是 finite-charge，不是 bounded-curvature；
8. high-shear 分支目前只有“喷射非紧但仍满足原始 charge budget”的严格结论；任何正的额外价格都必须来自路径型控制、Hamiltonian/标量约束、Weyl 项或 pinning，并需另行证明，不能从 Einstein matching 或终端 shear 大小静默推出。