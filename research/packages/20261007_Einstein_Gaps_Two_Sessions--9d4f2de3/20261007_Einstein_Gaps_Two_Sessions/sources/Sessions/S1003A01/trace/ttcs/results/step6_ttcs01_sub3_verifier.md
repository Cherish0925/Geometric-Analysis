# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md"
  ]
}
```

## Task

Independently examine the corrected perpendicular O11 branch and our new dual-cost/transgression computation. Check: (i) the normalization relation J=P+(1/4)∫(s+24)^2 in the peer's Ric=-6g normalization; (ii) the axis relabeling (new a,b,c)=(old s2,old s3,old s1) and the reported bolt/collar values Y=-1 at the bolt, Y=0 and Pi=X^4? here X=1 gives Pi=9 because CH h=(x,x,x+x^2) and radial normalization; identify the exact general formula in these coordinates; (iii) what the profile x0=.01, P≈1.001996, J≈1.002453, Tmin≈0.0516 says mathematically; and (iv) whether there is a sharper localized boundary/interior identity or inequality that could prove P≥8π² or J≥8π² in the perpendicular diagonal class. Distinguish established algebra from numerical indication and surface any normalization or smoothness errors. Give a direct technical memo with explicit equations and a proposed theorem target.

## Output

# 技术核验备忘录：垂直固定槽 O11 单元

以下记
\[
g=\frac{dx^2}{4G(x)}+F(x)\sigma_1^2+x\sigma_2^2+x e^{\omega(x)}\sigma_3^2,
\qquad x_0\le x\le X,
\]
其中塌缩方向是旧 \(\sigma _1\)，CH 纤维是旧 \(\sigma _3\)。脚本输出的 \(P,J\) 均已除以 \(8\pi^2\)。

## 1. \(P\) 与 \(J\) 的归一化

四维中
\[
\operatorname{Ric}
 =\operatorname{Ric}^{\circ}+\frac{s}{4}g,\qquad
|g|^2=4,
\]
故逐点正交分解给出
\[
\begin{aligned}
|\operatorname{Ric}+6g|^2
&=\left|\operatorname{Ric}^{\circ}
       +\frac{s+24}{4}g\right|^2  \\
&=|\operatorname{Ric}^{\circ}|^2+\frac{(s+24)^2}{4}.
\end{aligned}
\]
因此
\[
\boxed{\;
J_6(g):=\int|\operatorname{Ric}+6g|^2
=P+\frac14\int(s+24)^2 .
\;}
\]
`DualCell.costs` 中
\[
p=\frac{P}{8\pi^2},\qquad
q=\frac1{32\pi^2}\int(s+24)^2,\qquad
j=p+q
\]
与此完全一致。

需修正脚本说明中的一句话：\(P\) 在 \(g\mapsto cg\) 下确实不变，但固定系数 \(6\) 的 \(J_6\) 并不单独具有这种不变性。正确的协变关系是
\[
J_a(g)=J_{a/c}(cg).
\]
特别地令 \(\widetilde g=6g\)，则
\[
J_6(g)=J_1(\widetilde g),
\]
而 \(\operatorname{Ric}_{\widetilde g}=-\widetilde g\) 对应
\(\operatorname{Ric}_g=-6g\)。所以“缩放到 \(\operatorname{Ric}=-g\) 后费用相同”正确，“固定 \(6\) 时 \(J\) 本身尺度不变”不正确。

---

## 2. 轴重排与精确端点值

采用偶循环置换
\[
(\widetilde\sigma_1,\widetilde\sigma_2,\widetilde\sigma_3)
=(\sigma_2,\sigma_3,\sigma_1),
\]
它保持轨道取向及 \(d\sigma_i=2\sigma_j\wedge\sigma_k\) 的循环形式。相应长度为
\[
\boxed{\quad
a=\sqrt{x},\qquad b=\sqrt{x e^\omega},\qquad c=\sqrt F ,
\quad}
\]
正是代码中的
`(old[1],old[2],old[0])`。若 \(t\) 是弧长径向坐标，则
\[
dt=\frac{dx}{2\sqrt G},\qquad
\dot f=\frac{df}{dt}=2\sqrt G\,\frac{df}{dx},
\]
所以 `dots = 2*sqrt(G)*dabc_dx` 也正确。

### 2.1 光滑 bolt

普通 \(\mathcal O(-1)\) bolt 条件为
\[
F(x_0)=G(x_0)=0,\qquad F'(x_0)G'(x_0)=1.
\]
对真正光滑的 charge–4 模式还需
\[
\omega=O((x-x_0)^2)=O(t^4).
\]
于是
\[
a=b=\sqrt{x_0},\quad c=0,\quad
\dot a=\dot b=0,\quad\dot c=1,
\]
并且
\[
e^{2w_s}=\frac ab\to1,\qquad z=\frac c{\sqrt{ab}}\to0,
\qquad p_\pm\to0.
\]
因此
\[
\boxed{\quad Y_{\rm bolt}=-1,\qquad
\Pi_{\rm bolt}=0,\qquad
\frac{\mathcal T_{\rm bolt}}{8\pi^2}=1.\quad}
\]

这里 \(w_s\) 是转gression公式中的切片变量，不是度量中的 \(\omega\)。

### 2.2 CH collar

在 CH 区域，
\[
F=x,\qquad G=x(1+x),\qquad e^\omega=1+x.
\]
重排后
\[
a=\sqrt x,\qquad b=\sqrt{x(1+x)},\qquad c=\sqrt x,
\]
且
\[
\dot a=\dot c=\sqrt{1+x},\qquad \dot b=1+2x.
\]
代入切片变量得到
\[
e^{2w_s}=(1+x)^{-1/2},\qquad
z=(1+x)^{-1/4},
\]
\[
p_+=0,\qquad
p_-=3x(1+x)^{-1/4}.
\]
从而
\[
\boxed{\quad
Y_{\rm CH}=0,\qquad
\Pi_{\rm CH}=9x^2,\qquad
\frac{\mathcal T_{\rm CH}(x)}{8\pi^2}=9x^2.\quad}
\]
所以外端点 \(x=X\) 的精确值是
\[
\boxed{\quad \Pi(X)=9X^2,\qquad
\mathcal T(X)=72\pi^2X^2.\quad}
\]
它不是代码坐标 \(X\) 的 \(X^4\)。若改用轨道半径
\(\rho=\sqrt x\)，则 \(\Pi=9\rho^4\)；若改到
\(\widetilde g=6g\) 的半径 \(R^2=6x\)，则
\[
\Pi=\frac{R^4}{4},
\]
这正与早先 Ric\(=-g\) 归一化中的
\(\mathcal T/(8\pi^2)=R^4/4\) 相符。

另一个直接核对是
\[
\frac{dV_g}{dx}=\pi^2x,\qquad
\operatorname{Vol}_g\{0<y<x\}=\frac{\pi^2x^2}{2},
\]
故
\[
\mathcal T_{\rm CH}(x)=144\,\operatorname{Vol}_g\{0<y<x\}.
\]

这里的几何含义很重要：CH 度量仍是 Kähler，但 CH 纤维位于新 \(b\)-槽，而切片公式把新 \(c\)-槽当作参考纤维。因此 \(p_-\ne0\) 与 \(\Pi=9x^2\) 不是 CH 度量本身的非 Kähler 性；它们度量的是相对于 bolt 适配自对偶方向的错位。转gression电荷从 bolt 的 \(Y^2=1\) 转移到 collar 的 \(\Pi=9X^2\)。

`expected_T_collar=9.0` 只对当前固定的 \(X=1\) 正确；若类构造器使用一般 \(X\)，应为 \(9X^2\)。

---

## 3. 精确的切片—内部恒等式

采用复取向的 \(W^+\)，四维 Chern–Weil 密度满足
\[
d\mathcal T
=\left(
4|W^+|^2+\frac{s^2}{12}
-|\operatorname{Ric}^{\circ}|^2
\right)dV .
\]
定义
\[
\mathcal A(\rho)
=\frac1{8\pi^2}\int_{x_0}^{\rho}
\left(\frac{s^2}{12}+4|W^+|^2\right)dV,
\]
\[
\mathcal B(\rho)
=\frac1{8\pi^2}\int_{x_0}^{\rho}
\left[
\frac{s^2}{12}+4|W^+|^2+\frac{(s+24)^2}{4}
\right]dV,
\]
以及
\[
\tau(\rho)=\frac{\mathcal T(\rho)}{8\pi^2}=Y(\rho)^2+\Pi(\rho).
\]
则对 bolt 到切片 \(\rho\) 的区域，有精确公式
\[
\boxed{
\frac{P_{\rm in}(\rho)}{8\pi^2}
=1+\mathcal A(\rho)-\tau(\rho),
}
\]
\[
\boxed{
\frac{J_{\rm in}(\rho)}{8\pi^2}
=1+\mathcal B(\rho)-\tau(\rho).
}
\]
外部部分则为
\[
\frac{P_{\rm out}(\rho)}{8\pi^2}
=\mathcal A(X)-\mathcal A(\rho)-9X^2+\tau(\rho),
\]
\[
\frac{J_{\rm out}(\rho)}{8\pi^2}
=\mathcal B(X)-\mathcal B(\rho)-9X^2+\tau(\rho).
\]
因此整个单元满足
\[
\boxed{
\frac P{8\pi^2}=1+\mathcal A(X)-9X^2,\qquad
\frac J{8\pi^2}=1+\mathcal B(X)-9X^2.
}
\]

\(J\) 的内部密度还可精确化为
\[
\begin{aligned}
\frac{s^2}{12}+4|W^+|^2+\frac{(s+24)^2}{4}
&=\frac{(s+18)^2}{3}+36+4|W^+|^2\\
&\ge36.
\end{aligned}
\]
故每个切片都给出
\[
\boxed{
J\ge8\pi^2+36\,\operatorname{Vol}(C_\rho)-\mathcal T(\rho).
}
\]
这是垂直槽中比单纯使用 \(\mathcal T\) 更强、而且只需体积和一阶切片数据的局部下估计。

---

## 4. \(x_0=0.01\) 数值的数学含义

报告值应读作
\[
p:=\frac P{8\pi^2}\approx1.001996,\qquad
j:=\frac J{8\pi^2}\approx1.002453.
\]
因此
\[
j-p\approx0.000457,
\]
即
\[
\frac14\int(s+24)^2
\approx8\pi^2(0.000457)\approx0.03608,
\]
\[
\int(s+24)^2\approx0.1443.
\]
绝对费用为
\[
P-8\pi^2\approx0.1576,\qquad
J-8\pi^2\approx0.1937.
\]

在 \(X=1\) 时，完整 Chern–Weil关系要求
\[
\mathcal A(1)=p-1+9\approx9.001996,
\]
\[
\mathcal B(1)=j-1+9\approx9.002453.
\]
这是直接曲率积分与转gression计算之间应满足的精确一致关系。

若网格给出的
\[
\tau_{\min}\approx0.0516
\]
接近真实最小值，则相应切片有
\[
\mathcal T_{\min}
\approx8\pi^2(0.0516)\approx4.0742.
\]
在该切片
\[
\frac{P_{\rm in}}{8\pi^2}
=0.9484+\mathcal A_*,
\qquad
\frac{J_{\rm in}}{8\pi^2}
=0.9484+\mathcal B_*.
\]
所以即使丢掉所有正曲率项，内部已经承担至少 \(94.84\%\) 的一个 \(8\pi^2\) 单位。要在该切片直接得到 \(P\ge8\pi^2\)，只需
\[
\mathcal A_*\ge0.0516;
\]
要得到 \(J\ge8\pi^2\)，只需
\[
\mathcal B_*\ge0.0516.
\]

利用总费用和外部费用非小于零，还可推出
\[
0\le\mathcal A_*\le
p-1+\tau_{\min}\approx0.053596,
\]
\[
0\le\mathcal B_*\le
j-1+\tau_{\min}\approx0.054053.
\]
因此该数值剖面真正需要辨别的是很窄的区间：
\[
0.0516\le\mathcal A_*\le0.053596
\]
是否成立。仅有 \(\tau_{\min}\) 还不能回答这一点。

### 两个可直接计算的充分条件

由 \(\mathcal B\) 的点态下估计，
\[
36V_*\ge\mathcal T_{\min}
\]
即可推出 \(J\ge8\pi^2\)。当前数值对应
\[
\boxed{\quad V_*\ge0.1132\quad}
\]
即可。

对 \(P\)，令
\[
Q_s=\int_C(s+24)^2\approx0.1443.
\]
反三角不等式给出
\[
\int_{C_\rho}\frac{s^2}{12}
\ge
\frac1{12}
\left(24\sqrt{V_\rho}-\sqrt{Q_s}\right)_+^2.
\]
因此
\[
P\ge8\pi^2-\mathcal T(\rho)
+\frac1{12}
\left(24\sqrt{V_\rho}-\sqrt{Q_s}\right)_+^2.
\]
在最小转gression切片，忽略 \(W^+\) 的正贡献后，
\[
\boxed{\quad V_*\ge0.0944\quad}
\]
已足以推出 \(P\ge8\pi^2\)。

当前提供的数据没有该切片的累积体积或
\(\mathcal A_*,\mathcal B_*\)，所以这两个局部估计尚不能据现有数字完成证明。`profile_lines` 中的 `P_cum,J_cum` 能直接恢复
\[
\mathcal A_*=P_{\rm cum}-1+\tau_{\min},\qquad
\mathcal B_*=J_{\rm cum}-1+\tau_{\min}.
\]

这些数值说明当前找到的候选度量位于阈值之上，并给出垂直对角族的近阈值上界。单个 \(x_0=0.01\) 数据还不能确定渐近阶；数值上
\[
p-1=19.96\,x_0^2,\qquad
j-1=24.53\,x_0^2,
\]
与其他小 \(x_0\) 运行所示的一阶抵消相容。

---

## 5. 光滑性与数值实现中的具体问题

1. **bolt 的 charge–4 模式。**  
   `wpow=2` 给出
   \[
   \omega=O(u^2)=O((x-x_0)^2)=O(t^4),
   \]
   符合光滑普通 bolt。`wpow=1` 只有 \(O(t^2)\)；按同行记录，它只是 \(C^{1,1}\) 型模式，不能作为光滑单元本身。\(P\approx1.001996\) 对应的是 `--smooth` 数值，因而 bolt 端没有这个问题。

2. **外端匹配只有二阶。**  
   `(1-u)^3` 与五次 `smooth(u)` 使度量及前两阶导数在 \(u=1\) 与 CH 匹配，但直接向外接 CH 一般只有 \(C^2\)，并非 \(C^\infty\) 的完整 collar。由于偏差三阶消失，可在很薄的终端子区间用平坦截断平滑，并使曲率平方积分收敛到打印值；不过打印出的有限参数函数本身并未在开区间上完全等于 CH。

3. **转gression代码只适用于固定槽对角分支。**  
   `adapted_slice` 取 `sqrt(diag(h))`。若启用非平凡 `beta` 旋转，\(h\) 有非对角元，这一提取不再表示主轴长度。当前 `DualCell` 的固定垂直分支仍是对角的，所以这里没有冲突。

4. **\(\tau_{\min}\) 是网格值。**  
   `profile_report` 用 401 个对数聚集点，并略去 bolt 的极薄层；因此 \(0.0516\) 是采样最小值，不是连续函数最小值的封闭区间。端点值 \(1\) 与 \(9\) 则由上面的代数精确确定。

5. **`min_intF_minus_T` 的含义。**  
   代码中
   \[
   \texttt{intF}=H_J-1+\tau=\mathcal B,
   \]
   因而
   \[
   \texttt{intF}-\tau=H_J-1.
   \]
   取它的最小值通常只会被 bolt 附近的 \(H_J\approx0\) 支配。与局部阈值真正相关的是某切片上的
   \[
   \mathcal B-\tau=H_J-1
   \]
   是否非小于零，或等价地 `J_cum >= 1`；对 \(P\) 则是 `P_cum >= 1`。

---

## 6. 推荐的定理目标

最直接的全单元形式是：

> **垂直固定槽对角单元定理。**  
> 对每个光滑普通 \(\mathcal O(-1)\) bolt、在终端开区间上精确等于
> \[
> G=x(1+x),\qquad h=\operatorname{diag}(x,x,x+x^2)
> \]
> 的固定槽对角单元，
> \[
> \boxed{
> \int_C\left(\frac{s^2}{12}+4|W^+|^2\right)dV
> \ge72\pi^2X^2.
> }
> \]
> 等价地，
> \[
> P\ge8\pi^2,
> \]
> 从而自动有 \(J\ge8\pi^2\).

与数值剖面更贴近的局部强化形式是：存在一张切片 \(\rho\)，最好取 \(\tau\) 的内部最小点，使
\[
\boxed{
\int_{C_\rho}
\left(\frac{s^2}{12}+4|W^+|^2\right)dV
\ge8\pi^2\bigl(Y(\rho)^2+\Pi(\rho)\bigr).
}
\]
它与精确切片恒等式合并后立即推出 \(P\ge8\pi^2\)。对 \(J\) 的较弱版本把左侧换成
\[
\frac{(s+18)^2}{3}+36+4|W^+|^2;
\]
体积条件 \(36V_\rho\ge\mathcal T(\rho)\) 是其最简单推论。

真正缺少的是把切片量 \(Y,p_\pm\) 控制于内部 \(s\) 与 \(W^+\) 能量的一个一维迹型估计。这里不能沿用对齐槽的“\(Y=0,\Pi=0\)”机制：垂直 CH collar 精确满足 \(Y=0,\Pi=9X^2\)。同样，已有几乎 Kähler径向矩恒等式把塌缩槽和 CH 纤维放在同一位置，不能直接移植到当前槽排列。当前剖面把所需内部能量压缩到约 \(0.0516\cdot8\pi^2\)，说明上述局部定理是比直接估计整个 \(72\pi^2\) collar 电荷更贴近数值几何的目标。