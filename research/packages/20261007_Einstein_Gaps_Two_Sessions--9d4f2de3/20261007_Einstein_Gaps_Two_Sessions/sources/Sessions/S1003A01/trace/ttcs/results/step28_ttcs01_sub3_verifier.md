# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/scripts/step28_ak_nu_structure.py",
    "Sessions/S1003A01/workspace/scripts/step28_chern_stokes_check.py",
    "Sessions/S1003A01/workspace/scripts/step28_ak_gap_identity.py",
    "Sessions/S1003A01/workspace/data/step28/ak_nu_structure.json",
    "Sessions/S1003A01/workspace/data/step28/ak_hatted_structure.json",
    "Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json",
    "Knowledge/objects/papers/Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7--68f3db154d35/object.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Check the mathematical correctness and scope of Theorem A and its supporting identities in the note step28_AK_gap_identity_nijenhuis_transport.md, for smooth diagonal Bianchi-IX O(-1) cells with an exact complex-hyperbolic collar (perpendicular class), in the units P/(8pi^2) with W dt volume units. Specifically: (1) the claim that g is conformal via u^2=phi/(a_g a_h) to a diagonal almost-Kahler metric with A_f=(A_gA_h)_T/2, and the symbolic formulas for the Nijenhuis scalar nu, kappa-shat=6nu^2, the linear transport lambda=nu_T/2+beta*nu, and the Chern identity as the exact Stokes formula (shat+2nu^2)w=d/dT[4P cosh q - P P'' - P'^2/2] (scripts step28_ak_nu_structure.py and step28_chern_stokes_check.py; compare with Apostolov-Armstrong-Draghici formulas (10),(13) in the supplied paper, including normalization of Omega, kappa, W3 eigenvalue lambda); (2) the four-step proof of Theorem A, especially the U(2) splitting |W+|^2=(3/2)W_ww^2+(1/2)(W_gg-W_hh)^2, the conformal weights (Wff/u^2, |W+|^2 dV invariance), boundary terms at the conical bolt (u^2~ct, phi~ct^2) and at the CH collar, and the use of the inherited relative identity 1-Phat=D_+-36Vexc-Sexc; (3) the bolt Nijenhuis charge law and the asymptotics nu~-1/(2ut), mu~t^{3/2}, and the leading-order cancellation of the 6G and (3/2)N densities at the bolt; (4) the far-field Hardy lemma and the CH Hardy radius x_H=3+(3/4)sqrt(15), including whether the stated inequality and the condition Lambda>=4sqrt3 are correctly derived, and whether the conclusion 'all gain is generated inside sinh^2 R<~6' is supported by the data or needs qualification; (5) the section-5 claims about non-diagonal extension (uniqueness of the relative SD harmonic form when b_+=0, the modulus a=int_E omega, near-symplectic zero sets, expected a-dependence of pinning and Chern terms). Identify any error, hidden assumption, or overstatement, and state the corrected mathematics precisely. Also say what in Theorem A is genuinely new structural information versus a rewriting of the inherited relative Weyl-volume identity.

## Output

# 数学核验备忘录

## 总结

Theorem A 的盒装恒等式及其系数是正确的，前提是作如下精确定义：

1. \(\hat g=u^2g\) 只在去掉 bolt 的开集上是正定 almost-Kähler 度量；\(u\to0\) 于 bolt，故 \(\hat g\) 不延拓成该处的光滑黎曼度量。
2. 与 Apostolov–Armstrong–Drăghici（AAD）规范一致的基本形式是
   \[
   \Omega=\frac12d(\mathcal P\sigma_f),
   \qquad |\Omega|_{\hat g}^2=2,
   \]
   而笔记中的 \(d(\phi\sigma_f)\) 在 \(\mathcal P=\phi\) 时等于 \(2\Omega\)。
3. Stokes 公式中的 \(\hat s+2\nu^2\) 是 Chern/Hermitian scalar curvature
   \[
   s^\nabla=\frac{\hat s+\hat s_{\rm star}}2,
   \]
   不是通常定义的 star scalar curvature；通常的量满足
   \[
   \hat s_{\rm star}=\hat s+4\nu^2.
   \]
4. 笔记中的
   \[
   A_gv_g=-A_hv_h
   \]
   是代数笔误；正确关系是
   \[
   \frac{v_g}{A_g}=-\frac{v_h}{A_h},
   \qquad\text{即}\qquad A_hv_g=-A_gv_h.
   \]
5. 当 \(s\not\equiv-24\) 时，\(\Sigma\) 没有固定符号。因此“除 \(-3N/2\) 外各项均为 \(\ge0\)”以及“全部低于阈值的下降都来自非可积性”只在 \(s\equiv-24\) 时成立。
6. Hardy 部分推导正确，但“所有下降都产生于 \(\sinh^2R\lesssim6\)”是常标量情形下、且实际 \(\Lambda\) 满足相应点态不等式时的结论；对给出的数值样本成立，不能仅由 CH 公式推到任意 diagonal cell。
7. 非对角推广一节目前是合理的研究框架，并非已经推出的一般恒等式。唯一性需要 collar-relative 交叉型无正特征方向；零集为一维只在横截性成立时成立；\(a\)-依赖系数还需固定基本形式及体积单位。

---

## 1. 共形 almost-Kähler 构造与 AAD 归一化

令
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
\qquad d\sigma_f=2\sigma_g\wedge\sigma_h,
\]
并取正解
\[
\frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h}.
\]
置
\[
u^2=\frac{\phi}{a_ga_h},\qquad dT=u\,dt,\qquad A_i=ua_i,
\qquad \mathcal P=A_gA_h.
\]
则
\[
\mathcal P=u^2a_ga_h=\phi
\]
且
\[
\mathcal P_T=\frac{\phi'}u=2ua_f=2A_f.
\]
所以
\[
\boxed{A_f=\frac12\mathcal P_T}
\]
完全正确。

与 AAD 的 \(|\Omega|^2=2\) 规范相配的基本形式为
\[
\Omega=A_f\,dT\wedge\sigma_f+\mathcal P\,\sigma_g\wedge\sigma_h
      =\frac12d(\mathcal P\sigma_f).
\]
因此笔记的 \(d(\phi\sigma_f)\) 是 \(2\Omega\)，不是标准归一化的基本形式。这个常数不改变 \(J\)、\(\kappa\)、\(\nu\) 或 Weyl 特征值，但在比较 AAD 公式和定义 period \(a=\int_E\Omega\) 时必须明确。

### bolt 处的几何性质

光滑 perpendicular bolt 给出
\[
a_h=t+O(t^3),\qquad a_f=b+O(t^2),\qquad a_g=b+O(t^2).
\]
由 ODE，
\[
\phi=Ct^2(1+O(t^2)),\qquad
u^2=ct(1+O(t^2)),\qquad c=C/b>0,
\]
以及
\[
T=\frac23\sqrt c\,t^{3/2}(1+O(t^2)).
\]
于是
\[
A_f,A_g\asymp T^{1/3},\qquad A_h\asymp T.
\]
这不是普通 metric cone；它是各向异性的幂次型奇异端。故“每个 diagonal cell 共形于 almost-Kähler metric”应理解为：

> 在 \(C\setminus E\) 上，\(\hat g=u^2g\) 是 almost-Kähler；其体积密度和所有 Theorem A 中的积分在 \(E\) 附近可积，并具有零端点通量。

原始 \(g\) 仍是光滑度量。

---

## 2. \(\nu,\kappa,\lambda\) 的公式

取
\[
v_i=(A_i)_T-\gamma_i,\qquad
\gamma_i=\frac{A_j^2+A_k^2-A_i^2}{A_jA_k}.
\]
AK 约束给出正确关系
\[
\boxed{\frac{v_h}{A_h}=-\frac{v_g}{A_g}}.
\]
`ak_hatted_structure.json` 中输出的
`v_g_times_Ag_plus_v_h_times_Ah`
一般不为零，直接显示笔记所写 \(A_gv_g=-A_hv_h\) 不成立。

定义
\[
\boxed{\nu=\frac{v_h}{A_h}=-\frac{v_g}{A_g}
=-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right)}.
\]
在 AAD 的表示
\[
\nabla\Omega=a\otimes\varphi-Ja\otimes J\varphi,
\qquad |\varphi|^2=2
\]
中，此对称模型满足
\[
|a|^2=\nu^2,\qquad |\nabla\Omega|^2=4\nu^2.
\]
AAD 公式 (10)
\[
\kappa-\hat s=6|a|^2
\]
遂成为
\[
\boxed{\kappa-\hat s=6\nu^2}.
\]
这与 `ak_nu_structure.json` 的符号输出完全一致。

这里 \(\kappa=6p\)，其中
\[
p=\frac{\langle\widehat W^+(\Omega),\Omega\rangle}{|\Omega|^2}
\]
是基本形式方向的 Weyl 特征值。若用未归一化的 \(d(\mathcal P\sigma_f)=2\Omega\)，必须仍按 Rayleigh quotient 理解 \(W_{\omega\omega}\)。

### \(W_3^+\) 的归一化

AAD 公式
\[
W_3^+=\frac{\lambda}{2}
\bigl(\varphi\otimes\varphi-J\varphi\otimes J\varphi\bigr)
\]
使 \(W_3^+\) 在归一化二维子空间上的特征值为 \(\lambda,-\lambda\)。因此在 diagonal SD 基下
\[
\boxed{\lambda=\frac{\widehat W^+_{gg}-\widehat W^+_{hh}}2}
\]
与 AAD 的 \(\lambda\) 一致。

符号化输出给出
\[
\boxed{
\lambda=\frac12\nu_T+
\left(-\frac{(A_f)_T}{2A_f}
+\frac{2\cosh q}{A_f}\right)\nu
}
\]
即
\[
\lambda=\frac12\nu_T+\beta\nu.
\]
AAD 公式 (13) 中显式的 \(|a|^2\) 项与 \(da,b\) 中的二次项在这个 diagonal gauge 中相消，故所得公式线性于 \(\nu,\nu_T\)；这与 AAD 并不矛盾。

由 diagonal 曲率算子无 off-block 项，\(W_2^+=0\)。

### \(J\)-反不变 Ricci 的“当且仅当”

脚本给出的两个分量是
\[
\widehat D=2\nu_T+\nu\left(
\frac{2(A_f)_T}{A_f}
-\frac{8\cosh q}{A_f}
+\frac{4A_f}{\mathcal P}\right),
\]
\[
\widehat{\rm Ric}_{00}-\widehat{\rm Ric}_{ff}
=-2\nu^2-\frac{8\nu\sinh q}{A_f}.
\]
若这两个张量分量在一个开区间上恒为零，则确可推出 \(\nu=0\)：第二式的另一支
\(\nu=-4\sinh q/A_f\) 连同 \(\nu\) 的定义给出
\(q_T=4\sinh q/A_f\)，代回第一式得到
\[
\widehat D=-\frac{16\sinh q}{\mathcal P},
\]
故 \(q=0\) 且 \(\nu=0\)。

不过，在单独一个点上同时为零不能仅由这两个代数式推出 \(\nu=0\)，因为 \(\nu_T\) 可独立调节。因此“iff”应表述为局部张量场恒等消失，而不是逐点代数等价。

---

## 3. Chern–Stokes 公式

通常的 star scalar curvature 满足
\[
\hat s_{\rm star}-\hat s=|\nabla\Omega|^2=4\nu^2.
\]
代表 Chern 配对的标量是
\[
s^\nabla=\frac{\hat s+\hat s_{\rm star}}2
=\hat s+2\nu^2.
\]
因此脚本验证的是
\[
\boxed{
s^\nabla\,\hat w
=
\frac d{dT}\left[
4\mathcal P\cosh q
-\mathcal P\mathcal P_{TT}
-\frac12\mathcal P_T^2
\right],
\qquad
\hat w=A_fA_gA_h.
}
\]
`step28_chern_stokes_check.py` 同时给出：

- Stokes residual \(=0\)；
- pinning residual \(=0\)；
- CH bracket \(=-6\sinh^4T\)。

pinning 是
\[
\hat w=A_f\mathcal P
=\frac12\mathcal P\mathcal P_T
=\frac d{dT}\frac{\mathcal P^2}{4}.
\]
在 CH collar 上
\[
\mathcal P=\sinh^2T,\qquad X=\sinh^2R,
\]
所以
\[
\int d\hat V=\frac{X^2}{4}=V_{\rm CH},
\]
而 Stokes bracket 的外端值为 \(-6X^2\)，从而
\[
\boxed{\int s^\nabla\,d\hat V=-6X^2=-24V_{\rm CH}}.
\]

在 bolt 处，
\[
\mathcal P=O(t^2),\quad
\cosh q=O(t^{-1}),\quad
\mathcal P_T=O(t^{1/2}),\quad
\mathcal P_{TT}=O(t^{-1}),
\]
故 bracket 的三项均为 \(O(t)\)，趋于零。因而奇异端没有残余 Stokes 通量。

脚本注释中的“\(\mathcal P=2\phi\)”只有在 \(\phi\) 指 \(\Omega=\phi' dT\wedge\sigma_f+\cdots\) 的半势函数时才正确；按笔记正文 \(d(\phi\sigma_f)\) 的定义，则 \(\mathcal P=\phi\)。符号计算本身只使用 \(\mathcal P\)，未受此注释影响。

---

## 4. Theorem A 的四步推导

令
\[
p=\widehat W^+_{\Omega\Omega},\qquad
\delta=p+4,\qquad
2\lambda=\widehat W^+_{gg}-\widehat W^+_{hh}.
\]
由于 diagonal \(W^+\) 无 off-diagonal 项且迹为零，
\[
\boxed{
|\widehat W^+|^2
=\frac32p^2+\frac12
(\widehat W^+_{gg}-\widehat W^+_{hh})^2
}.
\]
于是
\[
|\widehat W^+|^2
=\frac32(\delta-4)^2+2\lambda^2
=24-12\delta+\frac32\delta^2+2\lambda^2.
\]

### 第一步：\(D_+\)

四维共形变换下，Weyl 曲率作为二形式上的算子缩放为
\[
\widehat W^+=u^{-2}W^+,
\]
且
\[
|W^+|_g^2\,dV_g
=|\widehat W^+|_{\hat g}^2\,dV_{\hat g}.
\]
同时
\[
dV_{\hat g}=u^4W\,dt.
\]
因此
\[
\begin{aligned}
D_+
&=24V_g-\int|\widehat W^+|^2d\hat V\\
&=24(V_g-\hat V)+12\int\delta\,d\hat V
-\frac32Q_\delta-\frac12Q_A.
\end{aligned}
\]
由 \(\hat V=V_{\rm CH}\)，
\[
\boxed{
D_+=24V_{\rm exc}+12\int\delta\,d\hat V
-\frac32Q_\delta-\frac12Q_A.
}
\]

### 第二步：\(\int\delta=N/6\)

由
\[
\kappa=\hat s+6\nu^2=s^\nabla+4\nu^2
\]
及 \(\delta=\kappa/6+4\)，
\[
\begin{aligned}
\int\delta\,d\hat V
&=\frac16\int s^\nabla d\hat V
+\frac23\int\nu^2d\hat V+4V_{\rm CH}\\
&=-4V_{\rm CH}+\frac{N}{6}+4V_{\rm CH}.
\end{aligned}
\]
故
\[
\boxed{\int\delta\,d\hat V=\frac N6}.
\]

### 第三步：体积恒等式

四维标量曲率共形公式给出
\[
\hat s=u^{-3}(-6\Delta_gu+su).
\]
积分后
\[
\int\hat s\,d\hat V
=6G+\int su^2W\,dt,
\]
因为内端
\[
uu'W=O(t)\to0,
\]
而 CH collar 上 \(u\equiv1\)，故 \(u'=0\)。

另一方面，
\[
\int\hat s\,d\hat V
=\int s^\nabla d\hat V-2\int\nu^2d\hat V
=-24V_{\rm CH}-\frac N2.
\]
再由
\[
H=\int(u^2-1)^2W
=V_{\rm CH}-2\int u^2W+V_g
\]
整理得到
\[
\boxed{
V_{\rm exc}
=H+\frac G2+\frac N{24}
+\frac1{12}\int(s+24)u^2W.
}
\]

### 第四步：代入 inherited identity

由
\[
1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc},
\qquad
S_{\rm exc}=\int W\left(\frac{s^2}{48}-12\right),
\]
代入前述两式得
\[
\widehat P-1
=12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N
+L+S_{\rm exc},
\]
其中
\[
L=\int(s+24)u^2W.
\]
令 \(r=s+24\)，则
\[
\frac{s^2}{48}-12=\frac{r^2}{48}-r,
\]
所以
\[
L+S_{\rm exc}
=\int r(u^2-1)W+\int\frac{r^2}{48}W
=\Sigma.
\]
因此
\[
\boxed{
\widehat P-1
=12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N+\Sigma
}
\]
完全成立。

### 关于符号解释

- \(H,G,Q_\delta,Q_A,N\) 均为 \(\ge0\)；
- \(\Sigma\) 没有固定符号；
- 当 \(s\equiv-24\) 时，\(\Sigma=0\)，此时唯一带减号的部分是 \(-3N/2\)。

故“canonical structure 若可积则 \(\widehat P>1\)”应写成：

> 若 \(s\equiv-24\) 且 \(\nu\equiv0\)，则
> \[
> \widehat P-1
> =12H+\frac32Q_\delta+\frac12Q_A>0,
> \]
> 其中 perpendicular bolt 强制 \(H>0\)。

对一般标量曲率，\(\Sigma\) 也可影响阈值。

---

## 5. bolt charge 与局部抵消

由 bolt 展开，
\[
q=\log(b/t)+O(t^2),\qquad
q'+\frac{4\sinh q}{a_f}
=\frac1t+O(t).
\]
由于 \(q_T=q'/u\)、\(A_f=ua_f\)，
\[
\boxed{\nu=-\frac1{2ut}+O(t^{-1/2})}
\]
并且 \(\nu\asymp t^{-3/2}\)。

输运方程等价于
\[
\nu_T+2\beta\nu=2\lambda.
\]
取
\[
\mu_T/\mu=2\beta,
\]
则
\[
\mu=\frac{C}{ua_f}
\exp\left(\int\frac{4\cosh q}{a_f}\,dt\right).
\]
bolt 附近积分项给出 \(t^2\)，而 \(ua_f\asymp t^{1/2}\)，故
\[
\boxed{\mu\asymp t^{3/2}}.
\]
从而
\[
K=\lim_{t\to0}\mu\nu
\]
有限且非零。由于 CH collar 上 \(\nu=0\)，
\[
\boxed{
K=-2\int\mu\lambda\,dT.
}
\]
\(K\) 随 \(\mu\) 的整体常数一起缩放；只有固定外端归一化后，其数值才有确定含义。

局部密度方面，若 \(u^2=ct+O(t^3)\)，则
\[
6u'^2W\longrightarrow\frac32cb^2,
\]
且
\[
6\nu^2u^4W\longrightarrow\frac32cb^2.
\]
因此 \(6G-\frac32N\) 的逐 \(dt\) 主阶恰好相消。该结论正确。

数值脚本有两点需要区分：

- `law_residual_from_i30=1.257...e-12` 是实际计算的积分输运误差；
- `law_residual` 因 `if False` 分支被直接置为 `0.0`，不能用作数值证据；
- 同一 JSON 中 `transport_rel_residual_max=2.0\times10^7`，原因是 `tt=np.cumsum(dtdx*wxs)` 并非各 Gauss 节点的真实 \(t\)-坐标，而后续用 `np.gradient` 对其求导。点态输运公式的依据是 SymPy 恒等式，不是这个字段。

---

## 6. Hardy 引理与 \(x_H\)

从
\[
\nu_T=2\lambda-2\beta\nu
\]
得到
\[
(\nu^2w)_T=4\nu\lambda w+\Lambda\nu^2w,
\qquad
\Lambda=\frac{w_T}{w}-4\beta.
\]
若右端位于 \(\nu=0\) 的 CH collar 内，并且区间上 \(\Lambda\ge c>0\)，积分给出
\[
cI+\nu(T_0)^2w(T_0)
\le4\sqrt{IJ},
\]
其中
\[
I=\int_{T_0}^{T_1}\nu^2w,\qquad
J=\int_{T_0}^{T_1}\lambda^2w.
\]
故
\[
I\le\frac{16}{c^2}J.
\]
Nijenhuis–\(W_3\) 扇区为
\[
2J-6I,
\]
所以当
\[
c^2\ge48,\qquad c\ge4\sqrt3
\]
时该扇区为 \(\ge0\)。系数正确。

在 CH 上，
\[
\mathcal P=x=\sinh^2R,\qquad
A_f=\sqrt{x(1+x)},\qquad q=0,
\]
直接计算
\[
\boxed{
\Lambda_{\rm CH}
=\frac{8x-3}{\sqrt{x(1+x)}}.
}
\]
方程 \(\Lambda_{\rm CH}=4\sqrt3\) 平方后有两个代数根，但较小根使 \(8x-3<0\)，不满足原方程。唯一有效根是
\[
\boxed{
x_H=3+\frac34\sqrt{15}\approx5.90474.
}
\]

对于所给 \(x_0=.038\) 数据：

- \(x_*=5.948799\)；
- far Nijenhuis sector \(=0.0058777>0\)；
- near Nijenhuis sector \(=-0.0706781\)；
- far ratio \(=0.174939<1/3\)；
- far conformal sector \(=9.31\times10^{-7}\)。

所以该样本确实把产生下降的 Nijenhuis 区域定位在 \(x\lesssim6\)。但一般陈述应写成：

> 在实际 \(\Lambda\ge4\sqrt3\) 的尾段，Nijenhuis–\(W_3\) 组合不能继续降低泛函。对记录中的三个优化 cell，最后一次 crossing 位于 \(x\approx5.94\)–\(5.99\)。

若 \(s\not\equiv-24\)，还需同时分段计算 \(\Sigma\)；当前 `hardy` 字段没有给出 far/near 的 \(\Sigma\) 分解，因此它单独不能证明完整 gap density 在尾段处处增加。

---

## 7. 非对角推广

### 相对 SD 形式的唯一性

若两个闭 SD 形式具有相同 CH collar germ，则其差 \(\alpha\) 在 collar 上为零，并定义
\[
[\alpha]\in H^2(C,\partial C).
\]
同时
\[
\int_C\alpha\wedge\alpha=\int_C|\alpha|^2\,dV.
\]
若 collar-relative 交叉型没有正特征方向，例如单个 \(O(-1)\) cell 的矩阵为 \((-1)\)，上式迫使 \(\alpha=0\)。因此唯一性成立。

这里真正使用的是 relative 交叉型，而不是未加说明的绝对 \(b_+=0\)。存在性仍是独立问题；任意非对角度量未必都有满足指定 CH germ 的闭 SD 延拓。

### period \(a\)

对标准归一化基本形式 \(\Omega\)，定义
\[
a=\int_E\Omega.
\]
perpendicular diagonal 形式在 \(E\) 上消失，故 \(a=0\)。aligned Kähler 情形通常有 \(a>0\)。

若相对类为
\[
[\Omega]=[\Omega_{\rm CH}]-a\,e,\qquad e^2=-1,
\]
则在通常实际体积单位下
\[
\operatorname{Vol}(\hat g)
=\frac12\int\Omega^2
=V_{\rm CH}-\frac{a^2}{2},
\]
而 Chern 配对满足
\[
\int s^\nabla dV=4\pi c_1\!\cdot[\Omega],
\]
相对于 \(a=0\) 情形出现线性改变量 \(-4\pi a\)。

若继续使用笔记中的未归一化形式 \(\omega=2\Omega\)，令
\(a_\omega=\int_E\omega=2a\)，则对应改变量为
\[
-\frac{a_\omega^2}{8}
\quad\text{和}\quad
-2\pi a_\omega,
\]
之后还需除以笔记采用的 orbit-volume 因子。故 section 5 所说的 \(a\)-dependent pinning/Chern terms 方向正确，但归一化必须先固定。

### 零集

闭 SD 形式若作为 \(\Lambda^+\) 的截面横截零截面，则其零集是一维光滑子流形，这正是 near-symplectic 情形。仅有“generic”一词还不足以推出该性质；需要对受固定 CH germ 约束的解空间建立横截性。当前 perpendicular diagonal 模型的零集是整个 exceptional sphere，维数为二，属于非横截模型。

在零集外可以取
\[
u^2=\frac{|\Omega|_g}{\sqrt2}
\]
并得到 almost-Kähler 共形度量；在零集处 \(u=0\)，Stokes 通量与 Chern 积分需通过零集管状邻域极限处理。因而 Taubes/near-symplectic 型分析是合理方向，但尚未由当前公式推出。

### \(W_2^+\) 的系数

一般 U(2) 分解可写成
\[
W^+=
\begin{pmatrix}
p&\zeta^T\\
\zeta&-\frac p2I+W_3
\end{pmatrix},
\]
于是
\[
|W^+|^2=\frac32p^2+2|\zeta|^2+|W_3|^2.
\]
若 \(W_3\) 的特征值为 \(\pm\lambda\)，则
\[
|W_3|^2=2\lambda^2.
\]
因此：

- 若“\(W_2^+\)”表示 off-block 向量 \(\zeta\)，附加项是 \(2|W_2^+|^2\)；
- 若“\(W_2^+\)”表示完整的 U(2) 曲率分量，则其 Hilbert–Schmidt 范数已经等于 \(2|\zeta|^2\)，附加项应写成 \(|W_2^+|^2\)。

section 5 需要注明采用哪一种记号。

---

## 8. Theorem A 中新增的结构与代数重组部分

相对于 inherited identity
\[
1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc},
\]
盒装公式本身是通过以下三条精确关系代入所得：

1. U(2) Weyl 分解；
2. \(\int\delta=N/6\)；
3. \(V_{\rm exc}\) 的共形标量曲率公式。

因此它不是一个独立的新下界，也没有消除 \(-3N/2\) 所带来的竞争。

真正增加的结构信息是：

- 每个 perpendicular diagonal cell 在去掉 bolt 后都有 canonical AK 表示；
- pinning \(\hat V=V_{\rm CH}\)；
- Chern–Stokes 公式把 \(\delta\) 的均值精确识别为 \(N/6\)；
- \(\lambda\) 与 \(\nu\) 满足一阶线性输运；
- bolt 强制一个非零 Nijenhuis charge；
- \(6G\) 与 \(3N/2\) 在 bolt 主阶抵消；
- Hardy 不等式把可产生下降的 Nijenhuis 区域定位到有限的中间区；
- 对 \(s\equiv-24\)，低于阈值必须由 canonical almost-complex structure 的非可积性提供。

这些内容给出了此前 relative Weyl-volume identity 所没有的几何机制解释；但近区耦合不等式仍未从现有公式中推出，因此 Theorem A 本身不产生统一的 sharp lower bound。