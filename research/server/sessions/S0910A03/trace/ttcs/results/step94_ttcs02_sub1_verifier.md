# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step94_two_ended_redshift_taper.py",
    "Sessions/S0910A03/workspace/data/step94_two_ended_redshift_taper.json",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/workspace/notes/step93_signed_transport_and_koiso_ot.md"
  ]
}
```

## Task

Read the new Step 94 two-ended redshift-taper benchmark and its exact output. Check the ODE normalization rho''=(6+Q)rho, Q=q^2/(2rho^3), the identity b=rho^-3/2 q' and w'+(3/2)sigma'w=b, the two-end q=0 construction, weighted integrals, and fitted exponential rates. Determine rigorously what this benchmark rules out: does it establish that Maxwell conservation/source control plus both OT end values, the exact area equation, and a finite separator Q bound cannot by themselves imply Q small or a length-independent matrix-weighted Poincare estimate? Confirm that it is not a full reduced Einstein connector because orbit-shape and horizontal equations are omitted. Identify the sharp remaining coupled equation or energy mechanism that any obstruction/construction must now confront. Give a concise mathematical memo.

## Output

## 数学核验备忘录

### 1. 方程归一化与两端构造

在一维基底、\(M=I\) 的标量对齐模型中，
\[
L\sigma=\sigma''+(\sigma')^2=\frac{\rho''}{\rho},
\qquad \rho=e^\sigma.
\]
因此
\[
L\sigma=6+Q,\qquad Q=\frac{q^2}{2\rho^3}
\]
确实等价于
\[
\boxed{\rho''=(6+Q)\rho=6\rho+\frac{q^2}{2\rho^2}}.
\]

又令
\[
w=\rho^{-3/2}q=\sqrt{2Q},\qquad b=\rho^{-3/2}q',
\]
直接求导得到
\[
w'=\rho^{-3/2}q'-\frac32\frac{\rho'}{\rho}w,
\]
故
\[
\boxed{w'+\frac32\sigma'w=b}
\]
逐点成立，系数与 Step 90 的 Maxwell 归一化一致。

程序中的 \(q_R\) 为偶函数：

- \(|r|\le R\) 时 \(q_R=1\)；
- \(R<|r|<R+1\) 上固定宽度下降；
- \(R+1\le |r|\le R+2\) 时 \(q_R=0\)。

所以两侧各有长度 \(1\) 的开 collar，且在电荷—扭率通道中严格 OT。由于 \(q_R'\) 为奇函数，
\[
\int_{-R-2}^{R+2}q_R'\,dr
=q_R(R+2)-q_R(-R-2)=0.
\]
正半轴上的变化为 \(-1\)，左半轴为 \(+1\)；两端零值只强制源的符号抵消，并不控制中间振幅。

由 \(\rho''>0,\rho'(0)=0,\rho(0)=1\)，在 \(r\ge0\) 有 \(\rho\ge1\)。又 \(0\le q_R\le1\)，所以
\[
0\le Q\le\frac12,\qquad Q(0)=\frac12.
\]
数据中的 `separator_Q=max_Q=0.5` 因而是严格解析事实，不只是数值现象。

程序采用的 smootherstep 在接点处一、二阶导数为零，故当前 \(q_R\) 是 \(C^2\) 而非 \(C^\infty\)。以
\[
\eta(t)=
\begin{cases}e^{-1/t},&t>0,\\0,&t\le0,\end{cases}
\qquad
p(t)=\frac{\eta(1-t)}{\eta(t)+\eta(1-t)}
\]
替代多项式下降函数即可得到 \(C^\infty\) 版本，以下指数率保持不变。

### 2. 加权积分与指数率

自然漂移测度为 \(d\mu_\sigma=\rho\,dr\)，因此
\[
\int w^2\,d\mu_\sigma=\int q^2\rho^{-2}\,dr,
\qquad
\int b^2\,d\mu_\sigma=\int (q')^2\rho^{-2}\,dr.
\]
脚本中的两项及其前面的因子 \(2\) 正确地计入左右两半。

在中央区 \(q=1\)，\(\rho\) 满足
\[
\rho''=6\rho+\frac1{2\rho^2}.
\]
乘以 \(2\rho'\) 可得第一积分
\[
\boxed{(\rho')^2=6\rho^2-\rho^{-1}-5}.
\]
从而对某个 \(A>0\)，
\[
\rho(r)=Ae^{\sqrt6\,r}(1+o(1)).
\]
固定宽度的 taper 上也有一致渐近
\[
\rho(R+t)=Ae^{\sqrt6(R+t)}(1+o(1)),\qquad 0\le t\le1.
\]
于是
\[
\|b\|_\infty
\sim C_b e^{-3\sqrt6 R/2},
\]
而
\[
\int b^2\,d\mu_\sigma
\sim C_S e^{-2\sqrt6 R}.
\]
另一方面，
\[
\int w^2\,d\mu_\sigma
\longrightarrow
2\int_0^\infty \rho_*(r)^{-2}\,dr>0.
\]
故
\[
\boxed{
\frac{\int w^2\,d\mu_\sigma}
{\int b^2\,d\mu_\sigma}
\sim C\,e^{2\sqrt6 R}}.
\]

输出与这些解析率高度吻合：

\[
-3.6742317557
\quad\text{对比}\quad
-\frac32\sqrt6=-3.6742346142,
\]
\[
4.8989804143
\quad\text{对比}\quad
2\sqrt6=4.8989794856.
\]
在 \(R=6\) 时，
\[
\|b\|_\infty=3.0945\times10^{-10},\quad
\int b^2d\mu_\sigma=2.0183\times10^{-13},
\]
而
\[
\int w^2d\mu_\sigma=0.79343223,\quad
\text{比值}=3.9311\times10^{12}.
\]

报告的 transport 与 area residual 是将解析表达式 \(w'\) 和
\(\rho''=(6+Q)\rho\) 回代后得到的代数残差，因此机器精度数值主要说明实现内部一致。上述第一积分和渐近推导提供了独立的数学验证。

### 3. 该族严格排除的推论

令
\[
\varepsilon_R=\|b_R\|_\infty\longrightarrow0.
\]
该族同时满足：

- 两端开 collar 上 \(q_R=0\)；
- 强迫 Maxwell 方程精确成立；
- 面积方程精确成立；
- 总坐标电荷通量为零；
- \(\sup Q_R=Q_R(0)=1/2\)；
- 分隔处 \(Q\) 有固定有限值。

因此，仅由这些资料不能得到
\[
\sup Q\le F(\|b\|_\infty),\qquad F(t)\to0,
\]
也不能得到以加权 \(L^2\) 源趋零为前提的 \(Q=o(1)\) 或 \(Q=O(\delta^2)\)。任给固定正数 \(B\)，取 \(q_0^2/2\le B\) 可得到同样现象，所以“分隔处仅有一个有限上界”本身不产生小量。

取
\[
A_R=\rho_R^{-3}I,\qquad \mathbf q_R=(q_R,0),
\]
则矩阵加权商正好退化为脚本中的标量商。因此不存在与 \(R\)、总长度及面积膨胀无关的常数 \(C\)，使这些资料单独推出
\[
\int \mathbf q^TA\mathbf q\,d\mu_\sigma
\le C\int (d\mathbf q)^TA(d\mathbf q)\,d\mu_\sigma .
\]

这里需区分带分隔曲线迹项的形式。该族并不反驳
\[
\int \mathbf q^TA\mathbf q\,d\mu_\sigma
\le C\int(d\mathbf q)^TA(d\mathbf q)\,d\mu_\sigma
+C_0|\mathbf q(0)|^2,
\]
因为 \(|\mathbf q(0)|=1\) 始终不变。它说明的是：这种迹项若只有固定有限控制，所得结论仍是 \(O(1)\)，不能随源趋零而得到 \(Q\to0\)。

### 4. 尚未纳入的耦合机制

该模型不是完整的约化 Einstein connector。它取 \(M=I\)，因而 orbit map \(U\) 为常值，却未施加
\[
\boxed{\tau_\sigma(U)=-Q\nabla\beta+Z}.
\]
由于 \(|\nabla\beta|=1\)，常值 \(U\) 会要求
\[
Z=Q\nabla\beta,
\]
在分隔处有 \(|Z|=1/2\)。所以即使 Maxwell 源趋于零，当前模型的 orbit-traceless Ricci 分量仍为固定量级。

若让 \(U\) 演化以吸收该项，就会产生
\[
e=|dU|^2,
\]
并进入水平 Einstein 方程
\[
\boxed{
\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma\otimes d\sigma
=(-3+Q)\gamma_B+\frac12U^*h+E_B.}
\]
这正是红移机制尚未支付的几何代价。在先前径向系统中，同一耦合表现为水平残差传播式
\[
C'=-2(u+H)C-wb,
\]
它要求比 \(\int q'=0\) 更强的加权矩条件才能同时匹配两侧精确区域。

因此，真正剩余的数学对象是 **orbit tension、orbit energy 与水平曲率/分隔稳定性之间的整体耦合估计**。构造需要同时解出 \(U\) 与 \(\gamma_B\) 并匹配两端；阻碍论证则需从这些方程提取一个不被 \(\rho^{-3/2}\) 红移消除的、与 connector 长度无关的能量代价。Maxwell、两端零值和面积增长本身没有这种代价。