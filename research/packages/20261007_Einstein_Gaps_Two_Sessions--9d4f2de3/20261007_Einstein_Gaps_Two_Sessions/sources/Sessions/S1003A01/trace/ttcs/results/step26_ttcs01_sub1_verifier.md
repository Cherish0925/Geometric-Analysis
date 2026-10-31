# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md",
    "Sessions/S1003A01/workspace/notes/step25_degeneration_matching_and_charge.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py"
  ]
}
```

## Task

Read the proposed Step-26 action-budget matching note together with the peer's chiral transgression note as a mathematical verifier. Check every normalization, the dimension-four rescaling of P and scalar curvature, the passage from the two chiral identities to the max lower bound, the controlled collapsed charge substitution, and the bound on the kernel C+4X=0. Identify hidden hypotheses needed for limits of charges and for applying a whole-cell budget to a prefix. Then propose the sharpest theorem statement that is actually supported, including how to formulate the missing high-shear alternative without silently assuming Einstein equations or bounded geometry. Focus on substantive mathematical corrections, not presentation.

## Output

# 数学核验备忘

## 1. 四维缩放归一化正确，但标量曲率结论需要明确前提

令
\[
\widetilde g=b^{-2}g.
\]
在常数倍缩放下，Levi-Civita 联络不变；把 Ricci 张量看作 \((0,2)\)-张量，有
\[
\operatorname{Ric}_{\widetilde g}=\operatorname{Ric}_g,\qquad
s_{\widetilde g}=b^2s_g.
\]
并且
\[
\operatorname{Ric}^{\circ}_{\widetilde g}
=\operatorname{Ric}^{\circ}_g,
\qquad
|\operatorname{Ric}^{\circ}_{\widetilde g}|_{\widetilde g}^{2}
=b^4|\operatorname{Ric}^{\circ}_g|_g^2,
\qquad
dV_{\widetilde g}=b^{-4}dV_g.
\]
因此在四维
\[
\widehat P(\widetilde g)
=\frac1{8\pi^2}\int |\operatorname{Ric}^{\circ}_{\widetilde g}|^2\,dV_{\widetilde g}
=\widehat P(g).
\]
这一部分完全正确。Bianchi–IX 归一化
\[
\int_{S^3}\sigma_{123}=2\pi^2
\]
也给出
\[
\widehat P=\frac14\int W|\operatorname{Ric}^{\circ}|^2\,dt,
\]
与 peer note 一致。

若
\[
\operatorname{Ric}_g=-6g,
\]
则
\[
\operatorname{Ric}_{\widetilde g}=-6b^2\widetilde g,
\]
所以任何 \(C^2_{\mathrm{loc}}\) 光滑 pointed 极限均为 Ricci-flat。

对于一般单元，结论
\[
s_{\widetilde g}=-24b^2\to0
\]
需要每个 \(g_j\) 本身满足逐点恒等式 \(s_{g_j}\equiv-24\)。单纯把无穷远端缩放成标准 CH，或者只指定某种总体标量归一化，都不能把一个变动的标量曲率函数变成常数。若单元类确实由常标量曲率代表组成，这一结论成立；否则必须另加
\[
b_j^2s_{g_j}\longrightarrow0
\quad\text{in }C^0_{\mathrm{loc}}
\]
之类的假设。

在常标量曲率假设下，若 \(\widetilde g_j\to g_\infty\) 光滑，则
\[
s_{g_\infty}=0.
\]
若只有 \(\widehat P(g_j)\le c\)，则在每个紧子集上
\[
\frac1{8\pi^2}\int|\operatorname{Ric}_{g_\infty}|^2
\le c,
\]
但不能推出 \(\operatorname{Ric}_{g_\infty}=0\)。若这些紧子集穷尽一个完整极限，则得到一个标量平坦、有限 Ricci action 的核心。若 \(\widehat P(g_j)\to0\)，或者原序列本来就是 Einstein，则 Ricci-flat 结论才随之成立。

---

## 2. Chiral 归一化与 bolt 电荷一致

Hitchin–Thorpe 密度给出
\[
4\pi^2(2\chi\pm3\tau)
=
\int\left(
2|W^\pm|^2-\frac12|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{24}
\right)dV.
\]
解出 \(\widehat P\) 后正是
\[
\widehat P
=
\frac1{2\pi^2}\int|W^\pm|^2
+\frac1{96\pi^2}\int s^2
-(2\chi\pm3\tau).
\]
因此 peer note 中两个系数
\[
\frac1{2\pi^2},\qquad \frac1{96\pi^2}
\]
均正确。

对于 \(O(-1)\) 盘丛，
\[
\chi=2,\qquad \tau=-1,
\]
所以
\[
2\chi+3\tau=1,\qquad 2\chi-3\tau=7.
\]
这与所用取向下的 bolt 电荷
\[
\mathfrak b_+=1,\qquad \mathfrak b_-=7
\]
吻合。这里必须固定为“CH 的 Kähler Weyl 张量属于 \(W^+\)”的取向；若使用改变取向的槽位置置换，两个 chirality 会交换。

---

## 3. 从两条 chiral 恒等式得到的精确 prefix 结论

令 \(C_T\) 为从光滑 \(O(-1)\) bolt 到主轨道 \(\Sigma_T\) 的前缀，并设
\[
S_T:=\frac1{96\pi^2}\int_{C_T}s^2\,dV,
\qquad
Q_{\pm,T}:=\frac1{2\pi^2}\int_{C_T}|W^\pm|^2\,dV.
\]
先在 \([\varepsilon,T]\) 上积分，再令 \(\varepsilon\to0\)。光滑 bolt 给出
\[
\boxed{
\widehat P(C_T)
=
\mathfrak b_+(\Sigma_T)-1+Q_{+,T}+S_T
=
\mathfrak b_-(\Sigma_T)-7+Q_{-,T}+S_T.
}
\]
因为 \(Q_{\pm,T}\ge0\)，最强的直接推论是
\[
\boxed{
\widehat P(C_T)\ge
\max\left\{
0,\,
\mathfrak b_+(\Sigma_T)-1+S_T,\,
\mathfrak b_-(\Sigma_T)-7+S_T
\right\}.
}
\tag{A}
\]
Step 26 的
\[
\widehat P(C_T)\ge
\max\{0,\mathfrak b_+(\Sigma_T)-1,\mathfrak b_-(\Sigma_T)-7\}
\]
是正确的较粗版本，只是丢掉了公共的 \(S_T\) 项。

两条 chiral 下界不能相加：它们的左端是同一个 \(\widehat P(C_T)\)。对两条式子作任意凸组合，最多恢复两者之中的较大者，而不是二者之和。

若整个单元满足
\[
\widehat P(g_j)\le c_j,
\]
则由于 \(|\operatorname{Ric}^{\circ}|^2dV\ge0\)，每个前缀满足
\[
\widehat P(C_{T,j})\le\widehat P(g_j)\le c_j.
\]
结合 (A)，得到对任意主轨道都成立的精确原始电荷约束
\[
\boxed{
\mathfrak b_+(\Sigma_{T,j})+S_{T,j}\le1+c_j,
\qquad
\mathfrak b_-(\Sigma_{T,j})+S_{T,j}\le7+c_j.
}
\tag{B}
\]
这一结论不需要 collapsed 渐近式，也不需要 Einstein 方程。

把 whole-cell 预算用于前缀时，需要的是实际积分
\[
\widehat P=\frac1{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2dV,
\]
而不能直接使用尚未证明等价的 renormalized Weyl–volume 表达式。对于 exact-CH tail，\(\operatorname{Ric}^{\circ}=0\)，所以实际 action 的可加性没有问题；但 \(s^2\) 和 \(|W^\pm|^2\) 的单独积分在无穷端可能发散，不应把有限前缀恒等式逐项直接送到无穷远。

---

## 4. Controlled collapsed charge 的代数完全正确

应把 little-\(o\) 写成轨道序列上的一阶喷射收敛。令 \(z_j\to0\)，并假设
\[
\frac{x_j}{z_j^3}\to X,\qquad
\frac{p_j}{z_j}\to P,\qquad
\frac{\chi_j}{z_j}\to C,\qquad
\frac{\eta_j}{z_j}\to N.
\tag{C}
\]
这比“单个 section 满足 \(o(z^k)\)”更精确。

脚本中的 spin 变量给出
\[
\begin{aligned}
u_f&\to P+\frac23C+\frac13N+2X,\\
u_g&\to P-\frac13C+\frac13N-2X,\\
u_h&\to-2,
\end{aligned}
\]
而另一 chirality 为
\[
\begin{aligned}
w_f&\to P+\frac23C+\frac13N-2X,\\
w_g&\to P-\frac13C+\frac13N+2X,\\
w_h&\to2.
\end{aligned}
\]
使用
\[
\mathfrak b_+
=2-\sum_i u_i^2-u_fu_gu_h,
\qquad
\mathfrak b_-
=\sum_iw_i^2-w_fw_gw_h-2,
\]
得到
\[
\boxed{
\mathfrak b_+\to-2-(C+4X)^2,
\qquad
\mathfrak b_-\to2+(C-4X)^2.
}
\tag{D}
\]
\(P,N\) 的消去是精确代数事实。

条件 (C) 足以使带 remainder 的电荷也收敛到 (D)：电荷只依赖轨道尺度归一化的一阶喷射，不需要二阶导数，也不需要任何场方程。不过这些是逐点序列条件；若把 \(x=Xz^3+o(z^3)\) 解释成同一 collar 上可微的函数渐近式，再对它求导，就会引入额外的运动学关系，不能与这里的独立首喷射参数混用。

将 (D) 代入 (A)，若
\[
S_*:=\liminf_jS_{T,j},
\]
则
\[
\boxed{
\liminf_j\widehat P(C_{T,j})
\ge
\max\left\{
0,\,
S_*-3-(C+4X)^2,\,
S_*+(C-4X)^2-5
\right\}.
}
\tag{E}
\]
丢掉 \(S_*\) 后正是 Step 26 的
\[
\boxed{
\liminf_j\widehat P(C_{T,j})
\ge\max\{0,(C-4X)^2-5\}.
}
\]
因此 (2.2) 正确。plus 通道的电荷差是
\[
-3-(C+4X)^2,
\]
而 opposite 通道给出
\[
(C-4X)^2-5.
\]

---

## 5. Whole-cell 预算与 kernel 数值

若
\[
\widehat P(g_j)\le c+o(1),
\]
由 (B) 和 (D) 有更精确的
\[
\boxed{
(C-4X)^2+\limsup_jS_{T,j}\le c+5.
}
\tag{F}
\]
特别地，
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
64X^2+\limsup_jS_{T,j}\le c+5,
\qquad
|X|\le\frac{\sqrt{c+5}}8.
}
\tag{G}
\]

若使用显示值 \(c\le0.99585\)，则
\[
\frac{\sqrt{5.99585}}8=0.3060803\ldots.
\]
所以正确数值应为
\[
|X|\le0.306081,
\]
而不是严格的 \(|X|<0.306\)。

对 \((X,C)=(1,-4)\)，有
\[
\mathfrak b_+\to-2,\qquad
\mathfrak b_-\to2+64=66.
\]
从 bolt 的 \(\mathfrak b_-=7\) 上升到 \(66\)，故
\[
\liminf_j\widehat P(C_{T,j})\ge59+S_*.
\]
因此该 kernel entry 不只是与 action \(<1\) 不相容；其渐近 prefix 代价至少为 \(59\)。这一结论是渐近序列结论，不能在未给出误差估计时直接赋给某个固定的有限 \(z\) section。

---

## 6. 可直接立为定理的版本

**定理（对角 \(O(-1)\) bolt 的 chiral action budget）。**  
设
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2
\]
是光滑对角 Bianchi–IX 度量，固定 CH 为 \(W^+\)-Kähler 的取向，并在 \(t=0\) 光滑延拓到 \(O(-1)\) bolt。则对任意主轨道 \(\Sigma_T\)，有
\[
\widehat P([0,T])
=
\mathfrak b_+(\Sigma_T)-1
+\frac1{2\pi^2}\int_{[0,T]}|W^+|^2dV
+\frac1{96\pi^2}\int_{[0,T]}s^2dV,
\]
以及相应的 minus 公式，其中 bolt 电荷为 \(7\)。从而 (A) 成立。

若 \(g_j\) 是此类度量，\(\widehat P(g_j)\le c+o(1)\)，且存在主轨道序列 \(\Sigma_j\) 满足 (C)，则 (D)、(E)、(F) 成立。该结论不使用 Einstein 方程，也不假设曲率一致有界。

该定理所需的具体前提是：

1. bolt 真正光滑，具有 \(O(-1)\) 的 Hopf 周期，而不是 orbifold bolt；
2. 槽位置和取向在整个序列中固定；若 collapsing slot 改变，需先作保持取向的循环重标；
3. 电荷极限是归一化一阶喷射的逐点序列极限；
4. bolt 到 \(\Sigma_j\) 的曲率积分有限，以便从 \([\varepsilon,T_j]\) 令 \(\varepsilon\to0\)；
5. whole-cell 预算是实际的 \(\int|\operatorname{Ric}^{\circ}|^2\)，且 prefix 是其可测子区域；
6. 标量平坦 blow-up 的结论另需 \(s\equiv-24\) 或 \(b_j^2s_{g_j}\to0\)。

---

## 7. High-shear 分支应如何精确定义

“第一次进入 controlled finite-charge class”目前不是单条曲线上的数学定义，因为 little-\(o\) 描述的是一个序列。可先固定 \(L<\infty\)，定义首喷射管
\[
\mathcal K_L(z)=
\left\{
|x|\le Lz^3,\quad
|p|\le Lz,\quad
|\chi|\le Lz,\quad
|\eta|\le Lz
\right\}.
\]
再把进入 \(\mathcal K_L\) 作为单条轨道曲线上的事件。对任意选定的 collapsed sections \(z_j\to0\)，令
\[
\mathcal D_j=
\max\left\{
\frac{|x_j|}{z_j^3},
\frac{|p_j|}{z_j},
\frac{|\chi_j|}{z_j},
\frac{|\eta_j|}{z_j}
\right\}.
\]
取子序列后只有两种情形：

1. \(\mathcal D_j\) 有界。四个归一化量可再取收敛子序列，因而定理中的 controlled charge 公式适用；
2. \(\mathcal D_j\to\infty\)。这时当前 transgression 理论仍给出原始电荷约束
   \[
   \mathfrak b_+(\Sigma_j)+S_j\le1+c+o(1),\qquad
   \mathfrak b_-(\Sigma_j)+S_j\le7+c+o(1),
   \]
   但不能把电荷写成 (D)。

这是目前已有材料支持的精确 high-shear alternative。需要注意，离开 \(\mathcal K_L\) 不等于电荷发散，也不等于曲率发散；它只表示该 \(z^3/z\) 首喷射 chart 不再紧致。

### 为什么不能直接写成 \(\widehat P\ge\Psi(\mathcal D_\Sigma,W_\Sigma)\)

一个只依赖终端 \(\mathcal D_\Sigma,W_\Sigma\) 且随 \(\mathcal D_\Sigma\) 增长而产生正代价的普遍公式并不由现有恒等式推出：

* 在光滑 Einstein bolt 附近，
  \[
  p\sim\frac1{3z^2},\qquad \eta\sim-\frac1{z^2},
  \]
  因而 \(\mathcal D\sim z^{-3}\)，但 \(\operatorname{Ric}^{\circ}=0\)，任意该类 prefix 的 \(\widehat P\) 都是零。任何普遍的 \(\Psi\) 都必须沿这些 Einstein bolt 状态取零或更小。
* controlled charge 极限完全看不到 \(P,N\)，所以 chiral 端点电荷不能单独控制 radial/volume directions。
* fibre/base pinning 依赖整条路径上的
  \[
  \int\frac{dt}{W}
  \]
  和 drift \(\int F_\beta dt\)，终端值 \(W_\Sigma\) 不能代替该路径积分。

因此，high-shear 的恰当对象应是一个带外端数据的路径变分值。固定由几何尺度定义的内外 sections、标准 CH 终端数据，以及避免 \(\mathcal K_L\) 的条件，可定义
\[
V_{\mathrm{hs}}
=
\inf
\frac14\int
W\left(
\frac34H^2+\frac23E^2+\frac12D^2
\right)dt,
\]
其中：

* 路径来自光滑 regular bolt，并在外端接到 exact standard CH；
* 若单元类是常标量曲率类，则施加 \(s=-24\)；
* \(H,E,D\) 是 trace-free Ricci 的三个对角分量，被当作自由 controls；
* 使用完整的对角 Ricci 演化恒等式，但不把 \(H,E,D\) 设为零；
* 在明确指定的 collapsed transition interval 上，路径不进入 \(\mathcal K_L\)；
* 权重始终使用实际的 \(W(t)\)。

每个 high-shear 路径按定义满足 \(\widehat P\ge V_{\mathrm{hs}}\)。真正尚缺的是对 \(V_{\mathrm{hs}}\) 的正定量估计，而不是 Einstein separatrix 的分类。若不固定 transition interval 的几何尺度，局部 Einstein bolt collar 会使这类变分值退化到零。

---

## 8. Fibre/base pinning 系数核对

peer note 使用
\[
|\operatorname{Ric}^{\circ}|^2
=
\frac34H^2+\frac23E^2+\frac12D^2,
\qquad
\widehat P=\frac14\int W|\operatorname{Ric}^{\circ}|^2dt.
\]
故
\[
\widehat P\ge\frac16\int WE^2dt.
\]
由
\[
\widetilde B'=F_\beta-\frac14E
\]
和 Cauchy–Schwarz，
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le
\frac14
\left(\int WE^2dt\right)^{1/2}
\left(\int\frac{dt}{W}\right)^{1/2}
\le
\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2}.
\]
系数完全正确，因而
\[
\widehat P\ge\frac{8C^2}{3I}
\]
也正确。CH 上
\[
I(T)
=
\int_T^\infty\frac{dt}{\sinh^3t\cosh t}
=
\frac1{2\sinh^2T}
-\frac12\log(1+\sinh^{-2}T).
\]
但该 \(I(T)\) 只能用于 exact CH 区间，或已有
\[
\int W_g^{-1}dt\le I(T)
\]
的独立比较。实际 high-shear connector 必须保留自身的 \(\int W^{-1}dt\)。

---

## 9. 代码注释中的一个实质不一致

`collapse_chiral_charge_limit.py` 的电荷代数正确，输出的
\[
-2-(C+4X)^2,\qquad 2+(C-4X)^2
\]
也正确。但脚本开头注释称 \(x=Xz^3\) 对应 finite orbit curvature，这与两份研究笔记中的曲率计算不一致。固定 base scale 时：

\[
\text{orbit curvature 一致有界通常需要 }x=O(z^6),
\]
而 mixed curvature 还要求类似
\[
\chi=O(z^4)
\]
及径向二阶导数控制。\(x=O(z^3)\)、\(\chi=O(z)\) 应称为 finite-charge normalized first-jet class，不能据此推断曲率一致有界。该注释应修正，但不影响脚本的电荷计算。

最后，peer 的 raw \(\Delta\eta=-8\) 数据与精确 prefix 定理一致：在 \(\varepsilon=1/16\) 时
\[
\mathfrak b_+=1.45193684
\]
已强制 regular bolt prefix 支付至少
\[
0.45193684.
\]
加上实际 metric reconstruction 的 connector action \(0.57446\)，总量至少
\[
1.02639684.
\]
这正说明 raw connector 的低 collocation 数值不能单独代表一个 regular-cell action。