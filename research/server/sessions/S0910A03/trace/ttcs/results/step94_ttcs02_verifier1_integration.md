# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 94,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the new Step 94 two-ended redshift-taper benchmark and its exact output. Check the ODE normalization rho''=(6+Q)rho, Q=q^2/(2rho^3), the identity b=rho^-3/2 q' and w'+(3/2)sigma'w=b, the two-end q=0 construction, weighted integrals, and fitted exponential rates. Determine rigorously what this benchmark rules out: does it establish that Maxwell conservation/source control plus both OT end values, the exact area equation, and a finite separator Q bound cannot by themselves imply Q small or a length-independent matrix-weighted Poincare estimate? Confirm that it is not a full reduced Einstein connector because orbit-shape and horizontal equations are omitted. Identify the sharp remaining coupled equation or energy mechanism that any obstruction/construction must now confront. Give a concise mathematical memo.

## Integrated Scientific Memo

## Step 94 核验备忘录

### 1. 归一化与恒等式

令 \(\rho=e^\sigma\)。在一维模型中
\[
L\sigma=\sigma''+(\sigma')^2=\frac{\rho''}{\rho},
\]
故
\[
L\sigma=6+Q,\qquad Q=\frac{q^2}{2\rho^3}
\]
严格等价于
\[
\boxed{\rho''=(6+Q)\rho=6\rho+\frac{q^2}{2\rho^2}}.
\]

再令
\[
w=\rho^{-3/2}q=\sqrt{2Q},\qquad b=\rho^{-3/2}q'.
\]
直接求导即得
\[
\boxed{w'+\frac32\sigma'w=b}.
\]
因此 Maxwell 源归一化、面积方程及其系数均正确。

构造中的 \(q_R\) 为偶函数：在 \(|r|\le R\) 上 \(q_R=1\)，在固定宽度 \(R<|r|<R+1\) 上下降，在两侧外 collar 上严格为零。于是
\[
\int q_R'\,dr=0,
\]
但两半轴分别产生 \(+1\) 与 \(-1\) 的坐标电荷变化；两端条件只强制源通量抵消，不控制中间电荷高度。

由 \(\rho''>0,\rho(0)=1,\rho'(0)=0\) 得 \(\rho\ge1\)，故
\[
0\le Q_R\le\frac12,\qquad Q_R(0)=\frac12.
\]
这不是数值观察，而是解析事实。当前 smootherstep 仅给出 \(C^2\) 的 \(q_R\)；若任务要求光滑模型，应换成端点平坦的 \(C^\infty\) cutoff。该替换不改变以下反例机制和指数率。

### 2. 加权积分与指数率

漂移测度为 \(d\mu_\sigma=\rho\,dr\)，所以脚本计算的是
\[
\int w^2\,d\mu_\sigma=\int q^2\rho^{-2}\,dr,\qquad
\int b^2\,d\mu_\sigma=\int (q')^2\rho^{-2}\,dr,
\]
因子 \(2\) 正确计入左右两半。

中央平台上
\[
\rho''=6\rho+\frac1{2\rho^2},
\]
其第一积分为
\[
(\rho')^2=6\rho^2-\rho^{-1}-5.
\]
因此
\[
\rho(r)=Ae^{\sqrt6\,r}(1+o(1)).
\]
固定宽度 taper 上遂有
\[
\|b_R\|_\infty\asymp e^{-3\sqrt6 R/2},\qquad
\int b_R^2\,d\mu_\sigma\asymp e^{-2\sqrt6R},
\]
而
\[
\int w_R^2\,d\mu_\sigma\longrightarrow
2\int_0^\infty \rho_*^{-2}\,dr>0.
\]
故
\[
\boxed{\frac{\int w_R^2\,d\mu_\sigma}
{\int b_R^2\,d\mu_\sigma}\asymp e^{2\sqrt6R}}.
\]

数值拟合
\[
-3.6742318\approx-\frac32\sqrt6,\qquad
4.8989804\approx2\sqrt6
\]
与解析率吻合。程序报告的 transport/area residual 则主要是代数回代的一致性检查，并非独立的 ODE 误差估计。

### 3. 它严格排除了什么

该族满足：

- 两端开 collar 上 \(q_R=0\)；
- Maxwell transport 精确成立；
- 一维面积方程精确成立；
- 总坐标电荷通量为零；
- 分隔处及全局 \(Q_R\) 均有固定有限界，且 \(Q_R(0)=1/2\)；
- \(\|b_R\|_\infty\to0\)，加权源能量也趋于零。

因此，仅凭这些条件不可能推出
\[
\sup Q\le F(\|b\|_\infty),\qquad F(t)\to0,
\]
特别不能推出 \(Q=o(1)\) 或 \(Q=O(\delta^2)\)。面积方程并未恢复强制性；它产生的指数面积膨胀恰好使坐标变化
\[
\Delta q=\int b\,\rho^{3/2}dr
\]
在 \(b\to0\) 时仍可保持 \(O(1)\)。

同样，取
\[
A_R=\rho_R^{-3}I,\qquad \mathbf q_R=(q_R,0),
\]
矩阵加权不等式退化为上述标量商，故不存在只由这些资料推出、且与长度和面积膨胀无关的 \(C\)，使
\[
\int \mathbf q^TA_R\mathbf q\,d\mu_\sigma
\le C\int(d\mathbf q)^TA_R(d\mathbf q)\,d\mu_\sigma.
\]
所需常数至少按 \(e^{2\sqrt6R}\) 增长。

但该模型**不反驳含未缩小分隔迹项的估计**
\[
\int \mathbf q^TA\mathbf q
\le C\int(d\mathbf q)^TA(d\mathbf q)+C_0|\mathbf q(0)|^2,
\]
因为 \(|\mathbf q(0)|=1\) 始终固定。它证明的是：仅有有限的 separator bound 最多给出 \(O(1)\) 控制，不能随源趋零而得到小量。

### 4. 为什么它不是完整 Einstein connector

模型冻结 \(M=I\)，即 \(U\) 为常值，却没有施加 orbit-shape 方程
\[
\boxed{\tau_\sigma(U)=-Q\nabla\beta+Z}.
\]
在无 orbit 缺陷 \(Z=0\) 时，常值 \(U\) 与 \(Q>0\) 不相容。等价地，在 \(q\) 常值的平台上，该模型给出
\[
L\log Q=-3L\sigma=-18-3Q,
\]
而完整的对角、定电荷 Einstein 系统还利用 orbit 方程，给出
\[
L\log Q=-18-4Q.
\]
因此 orbit 方程不是被自动满足，而是确实被省略了。

水平方程也未施加：
\[
\boxed{
\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma\otimes d\sigma
=(-3+Q)\gamma_B+\frac12U^*h+E_B.}
\]
所以该 benchmark 不是两端约化 Einstein 解，更不是 connector 或 Yau 第26题的反例。

### 5. 剩余的尖锐耦合对象

不能只说“补上 orbit 方程”即可：Step 90 的径向核表明，面积与 orbit 方程同时精确成立时，有限的中央 \(Q\) 仍可被红移到近零。真正尚未支付的全局代价主要位于：

\[
\boxed{\text{水平 Einstein/约束方程}
+\text{orbit 能量}
+\text{两端拓扑与 separator 稳定性}}
\]

的二维耦合中。其一维径向表现是水平约束残差传播
\[
C'=-2(u+H)C-wb,
\]
说明 \(\int q'=0\) 不足以完成精确两端匹配；还需满足由 \(wb\) 加权的水平矩条件或提供相应几何补偿。

因此，任何 obstruction 必须从完整水平方程、Codazzi–Bianchi 结构及
\[
\int_C\mathcal Wy^2\le\int_C(y_s^2+a_\delta y^2),
\qquad \mathcal W\ge\frac34Q,
\]
提取一个不被 \(\rho^{-3/2}\) 红移消除、与 connector 长度无关的能量或通量代价。反过来，任何 construction 都必须同时解出 \(U\) 与 \(\gamma_B\)，控制 orbit 能量及水平残差，并在自由 \(T^2\) 圆柱的两个 OT ends 完成精确匹配。

**结论：** Step 94 严格击破了“Maxwell 源控制 + 两端 \(q=0\) + 精确面积方程 + 有限 separator \(Q\)”单独蕴含 \(Q\) 小或长度无关加权 Poincaré 强制性的方案；尚未解决的是完整水平—orbit—稳定性耦合是否阻止或允许该红移逃逸。