# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step29_collapsed_saturation_value_four.md",
    "Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py",
    "Sessions/S1003A02/workspace/data/collapse_chiral_charge_limit.json",
    "Sessions/S1003A02/workspace/scripts/beta_pinning_identity.py",
    "Sessions/S1003A02/workspace/data/beta_pinning_identity.json",
    "Sessions/S1003A02/workspace/data/beta_pinning_threshold.json",
    "Sessions/S1003A02/workspace/data/saturation_control/step30_anisotropic_summary.json"
  ]
}
```

## Task

Independently verify the new Step-30 mathematics. In particular: (i) starting from the chiral transgression, check Lemma Q'' and the exact controlled-collapse limit b_+^{end}=-2-(C+4X)^2 under x=X z^3+o(z^3), p=Pz+o(z), chi=Cz+o(z), eta=Nz+o(z); determine whether the asymptotic assumptions really represent finite-curvature/F-structure control and whether any missing first-jet term changes the formula; (ii) check the fibre/base observable B~=log(kappa/sqrt(1+zeta))+(v-kappa^{-1})/4, its CH vanishing, the derivative B~'=F_beta-E/4, tensor coefficient P_hat >= (1/6)∫WE^2, the Cauchy-Schwarz constant, CH tail integral, and mismatch threshold 0.3702 at T=.70; (iii) interpret the raw anisotropic numerical runs without treating them as regular-bolt constructions. Give explicit corrections if needed and explain what is rigorously established for the diagonal Einstein-gap programme.

## Output

# Step 30 数学核验备忘录

## 总结

1. 从手征 transgression 恒等式出发，Lemma Q″ 是直接且正确的端点通量不等式。对受控端点
   \[
   \mathfrak b_+^{\rm in}\to-2-(C+4X)^2
   \]
   和圆欧氏端点，严格得到
   \[
   \liminf \widehat P\ge 4+(C+4X)^2.
   \]
2. 受控塌缩电荷公式
   \[
   \mathfrak b_+^{\rm end}=-2-(C+4X)^2
   \]
   的代数完全正确；\(P,N\) 的消失不是漏项，而是 plus 手征通量中的精确消去。
3. 式 (4) 准确描述的是“plus 电荷有限、形算子一阶数据按 \(z\) 缩放”的端点射流族。它本身并不等价于通常意义下、在基底尺度固定后曲率一致有界的 F-structure 塌缩，也不控制径向二阶导数。非零 \(X,C\) 在基底尺度固定时一般产生发散的切向或 Codazzi 曲率。真正一致有界的 Hopf 塌缩通常迫使 \(X,C\to0\)，因而恢复标准电荷 \(-2\)。
4. \(\widetilde B\) 的 CH 消失、导数恒等式、Ricci 张量系数、Cauchy–Schwarz 常数和 CH 模型积分均正确。数值阈值的准确值是
   \[
   C_*=\sqrt{\frac{3I(0.70)}8}=0.370125324\ldots;
   \]
   四位小数应写成 \(0.3701\)。\(0.3702\) 可作为略强的充分数值，但不是通常舍入值。
5. 用 CH 的 \(I(T)\) 代替一般轨迹的 \(\int W^{-1}dt\) 需要额外的体积比较。对任意 ACH 连接段，严格公式应保留实际的
   \[
   J=\int\frac{dt}{W_g}.
   \]
6. raw \(\Delta\eta=-8\) 运行从一个不受控的一阶射流开始，未计入由正则 bolt 数据制造该射流的代价。其低费用由初始 plus 电荷已升到 \(1.4519\) 完全解释，不构成正则 bolt 竞争度量。

---

## 1. Lemma Q″ 与端点通量

手征恒等式为
\[
\widehat P(C_j)
=\mathfrak b_+^{\rm out}(j)-\mathfrak b_+^{\rm in}(j)
+\frac1{2\pi^2}\int_{C_j}|W^+|^2
+\frac1{96\pi^2}\int_{C_j}s^2 .
\]
后两项均为 \(\ge0\)，所以若两个端点的完整尺度归一化一阶射流收敛，
\[
\liminf_j\widehat P(C_j)
\ge b_+^{\rm out}-b_+^{\rm in}.
\]
令外端为圆欧氏射流，\(b_+^{\rm out}=2\)，即得
\[
\liminf_j\widehat P(C_j)\ge2-b_{\rm end}.
\]

这里要求一阶射流而不只是轨道三度量是必要的：\(\mathfrak b_+\) 同时依赖 \(a_i\) 与法向导数 \(a_i'\)。整体尺度不重要，因为通量是尺度不变的。若等号成立，则恒等式同时给出
\[
W^+\equiv0,\qquad s\equiv0
\]
在 \(L^2\) 意义下成立。Burns 度量确实精确满足这一等号结构。Step 29 的数值序列接近端点差，只能推出相应积分数值很小；若要得到一个光滑 ASD、标量平坦极限，还需要几何紧性。

对于 CH 外端，
\[
b_+^{\rm out}=2-9\sinh^4\tau,
\]
所以受控塌缩公式还给出
\[
\liminf\widehat P
\ge4+(C+4X)^2-9\sinh^4\tau. \tag{A}
\]

---

## 2. 受控塌缩电荷的独立推导

设 \(r=(A_fA_gA_h)^{1/3}\)，用体积归一化系数 \(a_i=A_i/r\)。由
\[
q=-3\log z,\qquad \beta=x+\frac q2
\]
得到
\[
a_f=e^{2x/3}z^{-1},\qquad
a_g=e^{-x/3}z^{-1},\qquad
a_h=e^{-x/3}z^2.
\]
在
\[
x=Xz^3+o(z^3),\quad
p=Pz+o(z),\quad
\chi=Cz+o(z),\quad
\eta=Nz+o(z)
\]
下，三个法向导数为
\[
\begin{aligned}
p_f&=a_f\left(p+\frac23\chi+\frac13\eta\right)
 \longrightarrow P+\frac23C+\frac13N,\\
p_g&=a_g\left(p-\frac13\chi+\frac13\eta\right)
 \longrightarrow P-\frac13C+\frac13N,\\
p_h&=a_h\left(p-\frac13\chi-\frac23\eta\right)
 \longrightarrow0.
\end{aligned}
\]
轨道连接系数
\[
\gamma_f=\frac{a_g^2+a_h^2-a_f^2}{a_ga_h},\quad
\gamma_g=\frac{a_h^2+a_f^2-a_g^2}{a_ha_f},\quad
\gamma_h=\frac{a_f^2+a_g^2-a_h^2}{a_fa_g}
\]
满足
\[
\gamma_f\to-2X,\qquad \gamma_g\to2X,\qquad \gamma_h\to2.
\]
因此，令 \(u_i=p_i-\gamma_i\)，
\[
\begin{aligned}
u_f&\to A:=P+\frac23C+\frac13N+2X,\\
u_g&\to B:=P-\frac13C+\frac13N-2X,\\
u_h&\to-2.
\end{aligned}
\]
Step 27 归一化下
\[
\mathfrak b_+=2-\sum_i u_i^2-u_fu_gu_h.
\]
代入便有
\[
\begin{aligned}
\mathfrak b_+^{\rm end}
&=2-A^2-B^2-4+2AB\\
&=-2-(A-B)^2\\
&=\boxed{-2-(C+4X)^2}.
\end{aligned}
\]

所以 \(P,N\) 不出现是精确消去：二者只改变 \(u_f,u_g\) 的共同部分，而 plus 通量在 \(u_h\to-2\) 时只保留 \(u_f-u_g\)。\(\eta\) 也没有漏掉；它已经通过 \(N\) 进入两个水平速度，并在该手征组合中消去。

### 一阶渐近相容性

若式 (4) 只是不同度量上所选轨道的一阶射流序列，则 \(X,C,P,N\) 可以独立指定。若它被解释为同一个光滑端部上可逐项求导的渐近展开，还须使用
\[
\eta=rq'=-3r\frac{z'}z,\qquad rz'=-\frac{\eta z}{3}.
\]
若 \(x=Xz^3+o(z^3)\) 的余项也具有对应的一阶控制，则
\[
\chi=rx'
=3Xz^2rz'+o(z^4)
=-X\eta z^3+o(z^4)
=-XN z^4+o(z^4).
\]
此时 \(\chi=Cz+o(z)\) 强迫 \(C=0\)。因此非零 \(C\) 更自然地表示选定截面上的独立射流扰动，或一个径向变化很快的过渡层，而不是平缓端部的逐项渐近系数。

---

## 3. “有限曲率/F-structure”解释需要改写

令物理基底半径 \(R=A_g\)，纤维比
\[
\delta=\frac{A_h}{A_g}=z^3,\qquad A_f=Re^x,\quad A_h=R\delta.
\]
式 (4) 确实使三个形算子本征值保持基底尺度下的有限量，因为
\[
y_f=\frac{p+\frac23\chi+\frac13\eta}{r},\qquad
y_g=\frac{p-\frac13\chi+\frac13\eta}{r},\qquad
y_h=\frac{p-\frac13\chi-\frac23\eta}{r},
\]
且 \(r\sim Rz\)。

但是，在 \(R\) 归一化为 \(O(1)\) 时，非零 \(X\) 并不产生一致有界的轨道曲率。用 \(d\sigma_i=2\sigma_j\wedge\sigma_k\) 的标准轨道 Ricci 公式，
\[
{\rm Ric}^{\rm orb}_{ff}
=\frac{2\left(A_f^4-(A_g^2-A_h^2)^2\right)}
 {A_f^2A_g^2A_h^2},
\]
并有
\[
{\rm Ric}^{\rm orb}_{ff}-{\rm Ric}^{\rm orb}_{gg}
=\frac{16x}{R^2\delta^2}+O(R^{-2}).
\]
若 \(x=X\delta+o(\delta)\)，则
\[
{\rm Ric}^{\rm orb}_{ff}-{\rm Ric}^{\rm orb}_{gg}
=\frac{16X}{R^2\delta}+o(\delta^{-1}),
\]
对 \(X\ne0\) 发散。固定基底尺度的曲率一致有界至少需要
\[
x=O(\delta^2)=O(z^6).
\]

同样，\(\chi=Cz\) 给出
\[
y_f-y_g=x'=\frac{\chi}{r}=\frac C R+o(1).
\]
在 Berger 塌缩中，一个 Codazzi 曲率分量的主项为
\[
R_{0fgh}
=-\frac{2}{R\delta}(y_f-y_g)+O(1)
=-\frac{2C}{R^2\delta}+O(1),
\]
故固定基底尺度下还需要 \(y_f-y_g=O(\delta/R)\)，等价于
\[
\chi=O(z^4),\qquad C\to0.
\]

另外，式 (4) 完全没有约束 \(A_i''/A_i\)，所以也不能单独控制径向截面曲率。

因此，式 (4) 最准确的名称是：

> plus 电荷有限、形算子一阶数据受控的 Berger 射流族。

它不是单凭自身就能推出通常的有界曲率 F-structure 几何。若 \(R\to\infty\)，例如 ALF 端部，绝对曲率可能因 \(R\) 的增长而保持有限，但这项信息不在尺度自由状态 \((x,z,p,\chi,\eta)\) 中，必须另外给出。对于固定基底尺度的一致有界 Hopf 塌缩，上述必要关系使 \(X,C\to0\)，从而
\[
\mathfrak b_+^{\rm end}\to-2.
\]

非零的电荷核方向 \(C+4X=0\) 只说明 plus Chern–Simons 组合保持 \(-2\)；它本身不表示曲率正则。

这些修正不削弱 Q″：在更宽的一阶射流族内仍有
\[
\mathfrak b_+^{\rm end}\le-2,
\]
所以圆化价格仍至少是 \(4\)，且非核方向给出更大的端点差。

---

## 4. fibre/base 可观测量

### 4.1 CH 上严格为零

由
\[
\kappa=\coth t,\qquad \zeta=\csch^2t,\qquad v=\tanh t
\]
以及
\[
\sqrt{1+\csch^2t}=\coth t
\]
可得
\[
\log\frac{\kappa}{\sqrt{1+\zeta}}=0,\qquad
v-\kappa^{-1}=0.
\]
故
\[
\widetilde B
=\log\frac{\kappa}{\sqrt{1+\zeta}}
+\frac14(v-\kappa^{-1})
\]
在每个标准归一化 CH 轨道上严格消失。

### 4.2 导数中的 \(E\) 系数

令 Einstein 缺陷分量为 \(e_i={\rm Ric}_{ii}+6\)。在一阶系统中，控制项对三个 \(y_i'\) 的作用是 \(-e_i\)。于是
\[
v'=y_f'-\frac{y_g'+y_h'}2
\]
的控制部分为
\[
-e_f+\frac{e_g+e_h}{2}=-E.
\]
\(\kappa',\zeta'\) 在给定状态下没有额外的 \(e_i\) 直接项，因此
\[
\boxed{\widetilde B'=F_\beta-\frac14E}.
\]
这也解释了为何 \(F_\beta\) 在 CH 上为零：CH 是零缺陷流，而 \(\widetilde B\) 沿整条 CH 曲线恒为零。

### 4.3 张量系数与 Cauchy–Schwarz 常数

正交分解
\[
|\operatorname{Ric}^{\circ}|^2
=\frac34H^2+\frac23E^2+\frac12D^2
\]
给出
\[
\widehat P
=\frac14\int W|\operatorname{Ric}^{\circ}|^2dt
\ge\frac16\int WE^2dt.
\]
另一方面，
\[
\Delta\widetilde B-\int F_\beta dt
=-\frac14\int E\,dt.
\]
所以
\[
\begin{aligned}
\left|\Delta\widetilde B-\int F_\beta dt\right|
&\le\frac14
 \left(\int WE^2dt\right)^{1/2}
 \left(\int\frac{dt}{W}\right)^{1/2}\\
&\le
\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2}.
\end{aligned}
\]
Step 30 的系数无误。

---

## 5. CH 尾积分与阈值

CH 上
\[
W=\sinh^3t\cosh t.
\]
令 \(u=\sinh t\)，则
\[
\int_T^\infty\frac{dt}{W}
=\int_{\sinh T}^{\infty}\frac{du}{u^3(1+u^2)}
=\frac1{2\sinh^2T}
-\frac12\log\!\left(1+\sinh^{-2}T\right).
\]
因此式 (10) 正确。

若实际连接段满足
\[
J:=\int_T^\infty\frac{dt}{W_g},
\]
并定义
\[
C=\left|\Delta\widetilde B-\int_T^\infty F_\beta dt\right|,
\]
则严格结论是
\[
\boxed{\widehat P_{[T,\infty)}\ge\frac{8C^2}{3J}}. \tag{B}
\]
只有在 \(W_g=W_{\rm CH}\)，或已证明 \(J\le I(T)\) 时，才能写成
\[
\widehat P\ge\frac{8C^2}{3I(T)}.
\]
一个端点具有 CH 一阶射流，并不足以自动推出整个连接段的这一体积比较。若连接段只渐近接近 CH，则常数还应带上相应的定量比较因子。

数值上
\[
I(0.70)=0.36531401499170657,
\]
所以单位费用阈值为
\[
C_*=\sqrt{\frac{3I(0.70)}8}
=0.370125324\ldots .
\]
因此：

- 写 \(0.3701\) 是通常四位小数舍入；
- 要给一个略强的充分数值，可用 \(C\ge0.3702\)。

Taylor 系数
\[
z\left(-\frac15s_2+\frac25u-\cosh q+1\right)
\]
也与给出的符号文件一致。常数项确实为零，但线性项没有统一符号；而且若 \(q\) 随 \(z\) 增长，使 \(z\cosh q\) 不小，则“靠近 ACH 曲线时漂移很小”的推论也需要额外的状态控制。

---

## 6. raw anisotropic 数值的几何含义

### 6.1 raw \(\Delta\eta=-8\)

固定 raw \(\eta=O(1)\) 时，
\[
\eta=Nz
\]
对应 \(N=\eta/z\to\infty\)，并不属于固定 \(N\) 的式 (4)。在基底尺度固定时，相关形算子分量含有
\[
\frac{\eta}{r}\sim\frac{\eta}{Rz},
\]
会变得很大。若从正则 bolt 出发，制造这种射流的前段几何及其 Ricci 费用必须计入；当前最优控制问题把该射流直接当作初始数据，因此只计算后续连接段。

在 \(\varepsilon=1/16\) 的 raw \(\eta=-8\) 数据中，
\[
\mathfrak b_+(0)=1.4519368402,
\]
到电荷 \(2\) 的差只有
\[
2-\mathfrak b_+(0)=0.5480631598.
\]
于是低费用并非绕过了手征通量，而是初始电荷已经非常接近圆值。离散费用
\[
0.5454079
\]
比端点差小约 \(2.66\times10^{-3}\)，这不可能是精确度量的 transgression 值；独立重构的实际度量费用
\[
0.57446
\]
位于端点差之上，与恒等式相容。

在 \(\varepsilon=1/32\) 时，
\[
2-\mathfrak b_+(0)=2.9421976031,
\]
而 collocation 与重构分别为
\[
2.9425036,\qquad 2.94303,
\]
再次显示费用主要由端点电荷差决定。

### 6.2 固定 \(N=-8\) 与电荷核方向

固定 \(N=-8\)、令 \(\eta=Nz\) 是一阶射流意义下的受控族。有限 \(\varepsilon\) 时它可以显著改变匹配和初始电荷，但精确极限公式仍给出
\[
\mathfrak b_+^{\rm end}\to-2,
\]
因此若后来达到圆电荷，其严格渐近下界仍趋于 \(4\)。

同理，\(X=1,C=-4\) 只保证
\[
C+4X=0,\qquad \mathfrak b_+^{\rm end}=-2.
\]
两组费用 \(3.5789,3.7783\) 与趋向 \(4\) 相符，但两个网格点尚不能构成渐近定理；而且如上所述，这个电荷核方向并不自动具有固定基底尺度下的一致有界曲率。

---

## 7. 对 Einstein-gap 计划已严格得到的内容

在当前材料中，可以严格使用的结论是：

1. **对角类端点定价：**
   \[
   \liminf\widehat P\ge b_+^{\rm out}-b_+^{\rm in}.
   \]

2. **受控一阶射流的精确 plus 电荷：**
   \[
   b_+^{\rm in}=-2-(C+4X)^2.
   \]

3. **圆化和 CH 化的条件式下界：**
   \[
   \liminf\widehat P_{\rm round}\ge4+(C+4X)^2,
   \]
   \[
   \liminf\widehat P_{\rm CH(\tau)}
   \ge4+(C+4X)^2-9\sinh^4\tau.
   \]

4. **精确 fibre/base pinning 恒等式：**
   \[
   \widetilde B'=F_\beta-\frac14E,
   \]
   以及实际体积权重下的估计 (B)。

当前文件尚未提供以下数学连接：

- 正则小 bolt 数据到某个塌缩截面时确实满足式 (4)，或更强的有界曲率渐近；
- 对一般 ACH 连接段证明 \(J\le I(T)\)；
- 证明有效漂移修正后的 mismatch 至少为 \(0.3701253\ldots\)；
- 证明 saturation 全局下确界等于 \(4\)；
- 将对角手征电荷推广为一般 F-structure 颈部上的端部 Chern–Simons 极限。

因此，Step 30 最坚实的新成果是两个精确代数结构：受控端点的 plus 电荷公式，以及 fibre/base pinning 恒等式。它们已经把小 bolt 分支转化为明确的几何问题：正则 bolt 如何进入塌缩截面、该截面的实际一阶射流为何仍具有 \(\mathfrak b_+\le-2+o(1)\)，以及 ACH 连接段的真实体积权重和自由漂移如何定量控制。