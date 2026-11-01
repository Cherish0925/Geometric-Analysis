# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 93,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step93_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step93_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the signed Maxwell transport argument for the free-T² two-ended connector with twist. The setup: a free-T² invariant 4-manifold with two complete outward-expanding cusp ends and ||Ric+3g||_op ≤ δ. The physical twist w = √(2Q) satisfies the invariant transport |dw + (3/2)w dσ| ≤ (1/2)w|dU| + |b|, where |b| ≤ 2√2δ from mixed Ricci (equation 5.1 of step90). Three claims to verify:

1. KOISO OT THEOREM: The Step 92 constrained Koiso germs have q=0 (no charge) initial data. Under exact Ric=-3g, Maxwell conservation gives dq=0, so q≡0 throughout the germ domain. The germ is OT and blocked by Steps 85-88. Is this reasoning correct?

2. SIGNED CUSP TRANSPORT: On the expanding cusp where σ_ν→2 and e_ν→0, the coefficient a=-(3/2)σ_ν+√e_ν/2→-3. Starting from w=0 at the cusp end, the Gronwall bound gives w ≤ 2√2δ∫ exp(-(3/2)(σ(t)-σ(r)) + (1/2)∫√e_ν dτ) dt. Using e_ν ≤ B(δ)=sup e everywhere, the exponent is -(3-√B/2)(t-r). Since B(δ)<36 for δ<δ*, this converges: w_sep ≤ 2√2δ/(3-√B/2). Is this derivation correct? What are the mathematical conditions?

3. SELF-CONSISTENT LOOP: Using B(δ,Q+,Q-) from the resolvent, Q+ = w²/2 from the transport, Q- = 0 at cusps, the iteration Q→B→w→Q converges because Q appears quadratically in w but only linearly in B. The gap function floor-ceiling = (12+2Q-8δ) - B(δ,Q,0) changes sign at δ**≈0.186 (worst-case constant e_ν) or δ**≈0.210 (decaying e_ν). Is this self-consistent closure mathematically legitimate?

Key concern: the 1D signed transport along normal rays may not capture the full 2D charge distribution on the base. Does the Hodge-theoretic structure of the Maxwell equation support a 1D reduction for bounding Q at the separator? Or are there 2D charge modes that evade the 1D damping estimate?

## Integrated Scientific Memo

# 核验结论

三个主张中：

1. **Koiso germ 保持 OT：成立，但须限定为保持自由 \(T^2\) 对称的连通精确 Einstein 延拓；只有再具备完整双外扩端等条件时，Steps 85–88 才给出阻断。**
2. **所写 cusp 积分作为某个“零齐次常数的受迫特解”是可积的，但不能由外端 \(w=0\) 反推出 separator 的上界。传播方向/边界条件使用错误，并且 \(e_\nu\le B\) 在扭曲问题中尚未证明。**
3. **自洽迭代只是径向 ansatz 的数值固定点，不是一般 free-\(T^2\) connector 的数学闭合。** 数字 \(0.185928\) 和 \(0.210028\) 不能作为通用阈值。

核心障碍并非必须存在某种神秘二维 harmonic charge mode；事实上，**零切向模式的一维方程本身已否定反向阻尼估计**。二维几何又增加了路径、切向变化、法向能量集中和全局最大值控制等缺口。

---

## 1. Koiso OT 论证

Step 92 的 Cauchy 数据为
\[
g_\Sigma=ds^2+M(U(s))_{ab}\,dx^a dx^b,
\]
且 Weingarten 张量没有混合分量 \(W_{sa}\)。在 Gaussian 法向规范 \(A_\nu=0\) 下，这给出初始连接曲率
\[
F_{\nu s}^a=0,
\]
从而 Maxwell 电荷
\[
q_a=\rho G_{ab}(*_\gamma F^b)
\]
在初始曲线上为零。

精确 Einstein 情形 \(E=\operatorname{Ric}+3g=0\) 下，Step 90 (1.4) 变为
\[
dq_a=0.
\]
因此在连通商空间内 \(q_a\) 为常向量；初值 \(q_a=0\) 推出
\[
q_a\equiv0,\qquad F^a\equiv0.
\]
Koiso 解析解的局部唯一性还保证 \(T^2\) 对称性延续。因此 germ 局部 OT。平坦连接可以有平移 holonomy，但 \(F=Q=0\)，不影响局部 OT 方程。

不过，“被 Steps 85–88 阻断”只在延拓进一步满足以下条件时成立：

- 完整；
- 商空间为 \(S^1\times\mathbb R\)；
- 两个完整、向外扩张的规定 cusp 端；
- 满足相应有界性和无穷远 resolvent 条件。

Koiso germ 本身只是局部对象，不能直接称为被完整性定理排除。若确有上述完整延拓，则在 \(\delta=0\) 时 Step 88 给出
\[
\sup e\ge12,\qquad \sup e\le6,
\]
故矛盾。

**结论：Claim 1 在上述限定下正确。** 它不控制 \(E\ne0\) collar 中由混合 Ricci 源生成的 twist。

---

## 2. 正确的有向 Maxwell 传播

沿朝 cusp 外侧的单位速法向曲线，以 \(t\) 增大表示向外，令
\[
p(t)=\frac32\sigma_\nu(t),\qquad
c(t)=\frac12\sqrt{e_\nu(t)},\qquad
\beta(t)=|b_\nu(t)|.
\]
需要先有 Step 90 (5.1) 的**方向化版本**，方可写成
\[
|w'+pw|\le cw+\beta,\qquad \beta\le2\sqrt2\,\delta.
\tag{2.1}
\]
仅由总范数形式严格得到的是 \(c\le |dU|/2\)，将它直接替换为 \(\sqrt{e_\nu}/2\) 需要张量级推导。

由 (2.1) 得
\[
w'+(p-c)w\le\beta,
\tag{2.2}
\]
以及
\[
w'+(p+c)w\ge-\beta.
\tag{2.3}
\]

### 向外正向传播

从内部 \(r\) 到外部 \(t\)，(2.2) 给出
\[
w(t)\le e^{-\int_r^t(p-c)}w(r)
+\int_r^t e^{-\int_s^t(p-c)}\beta(s)\,ds.
\tag{2.4}
\]
若 \(p-c>0\)，已有内部 twist 向 cusp 外传播时衰减。这是正确的红移方向。

### 从外端反推内部

若在有限 \(R\) 后已经是精确 OT 开集，故 \(w(R)=0\)，则应使用 (2.3)：
\[
w(r)\le
\int_r^R\beta(s)
\exp\!\left(\int_r^s[p(\tau)+c(\tau)]\,d\tau\right)ds.
\tag{2.5}
\]
这是**增长核**，并非 Claim 2 所用的
\[
\exp\!\left[-\int_r^s(p-c)\right].
\]
因此 cusp 的向外阻尼不能反向变成从端部到 separator 的长度无关上界。

### 明确的一维反例

即使取理想 cusp
\[
\sigma=2t,\qquad U=\mathrm{const},\qquad p=3,\qquad c=0,
\]
并令实际有符号源满足
\[
w'+3w=-\beta_0\phi(t),\qquad 0\le\phi\le1,
\]
其中 \(\phi\) 平滑支撑于远端过渡区且外侧 \(w=0\)，解为
\[
w(r)=e^{-3r}\int_r^R\beta_0e^{3s}\phi(s)\,ds.
\]
若源支撑位于 \(R-O(1)\)，则
\[
w(0)\asymp\beta_0e^{3R}.
\]
故即使
\[
e_\nu=0,\qquad B=0<36,\qquad |b|\le\beta_0,
\]
separator 的 \(w\) 仍可随 collar 长度指数增大。这个零切向 Fourier 模式已足够推翻所提上界。

---

## 3. 所写积分何时只是一个可积特解

Claim 2 中的积分
\[
I(r)=\int_r^\infty
\exp\!\left[
-\frac32(\sigma(t)-\sigma(r))
+\frac12\int_r^t\sqrt{e_\nu}\,d\tau
\right]dt
\tag{3.1}
\]
确实是正向阻尼算子的核。若对所有 \(t\ge r\) 有
\[
\sigma_\nu(t)\ge2,\qquad e_\nu(t)\le B<36,
\tag{3.2}
\]
则
\[
I(r)\le
\int_r^\infty e^{-(3-\sqrt B/2)(t-r)}dt
=\frac1{3-\sqrt B/2}.
\tag{3.3}
\]
因而设齐次常数为零时，受迫特解满足
\[
w_{\rm forced}(r)
\le\frac{2\sqrt2\,\delta}{3-\sqrt B/2}.
\tag{3.4}
\]

但这不是实际 \(w(r)\) 的端值估计，原因有三：

1. **齐次模式未被端部衰减条件消除。**  
   齐次解为
   \[
   w_h(t)=C\exp\!\left[
   -\frac32\sigma(t)
   +\frac12\int^t\sqrt{e_\nu}\,d\tau
   \right].
   \]
   当指数趋于 \(-\infty\) 时，每个 \(C\) 都满足 \(w_h(t)\to0\)。因此仅有 \(w\to0\) 不确定 \(C\)。在精确 cusp 上 \(w=Ce^{-3t}\) 正对应非零常坐标电荷 \(q_a\)。

2. **“\(w=0\) at the cusp end”含义必须区分。**  
   \(w\to0\) 不等于 \(q_a=0\)。只有端上存在 \(F=0\) 的精确 OT **开集**，才能推出那里 \(q_a=0\)；即便如此，从该有限边界反向传播仍得到 (2.5) 的增长核。

3. **全射线上的假设 (3.2) 未建立。**  
   仅有
   \[
   \sigma_\nu\to2,\qquad e_\nu\to0
   \]
   只保证足够远尾部可积；有限 collar 会产生依赖其几何的乘法常数。脚本自身采用的面积模型满足 \(\sigma_\nu(0)=0\) 且有限距离内 \(\sigma_\nu<2\)，所以不能从 separator 起使用 (3.3)。

此外，Step 92 已构造精确 Einstein Koiso germs，使 \(e_\nu\) 可形成任意高的窄峰。因此，在一般 twisted connector 中并无已证明的点态
\[
e_\nu\le B.
\]
Step 88 的 \(B\) 是 OT Bochner ceiling；不能未经新的变量势 resolvent 定理就用于 twisted 的 \(e_\nu\)。

**结论：Claim 2 的积分收敛计算在强附加假设及零齐次常数选择下正确，但作为 cusp 到 separator 的通用上界错误。**

---

## 4. 自洽循环没有形成数学闭合

Step 90 的必要比较涉及三个不同量：
\[
Q_+=\sup_BQ,\qquad
Q_-=\inf_BQ,\qquad
Q_C=\frac{\int_CQ\rho\,ds}{\int_C\rho\,ds},
\]
并为
\[
12+2Q_C-8\delta
\le B(\delta,Q_+,Q_-).
\tag{4.1}
\]
精确 OT 端可以给出 \(Q_-=0\)，但脚本额外设置
\[
Q_C=Q_+=\frac12w_{\rm sep}^2.
\tag{4.2}
\]
一般没有依据：

- 单条射线到达 separator 的值不等于 \(C\) 上加权平均；
- separator 上的最大值不等于整个二维基底上的 supremum；
- twist 可在 collar 内、离开 separator 处达到更大值；
- Step 92 仅证明一个很粗的 \(\sup_CQ<\infty\)，明确未控制 \(Q_+\)。

固定点论证本身也不充分。数值迭代某个等式映射并收敛，只说明找到该 ansatz 的一个固定点；它不证明所有满足几何不等式的 \(Q_+\) 都位于该分支，更未排除大固定点。

“\(B\) 对 \(Q\) 仅线性”亦不正确。令
\[
K=3+\delta,\qquad f=Q+2\delta.
\]
脚本使用
\[
B=
\left[
\frac{2f}{\sqrt K}
+\sqrt{2K+\frac{5f^2}{K}}
\right]^2,
\]
故当 \(Q\to\infty\) 时
\[
B\sim\frac{(2+\sqrt5)^2}{K}Q^2.
\tag{4.3}
\]
右侧二次增长，而 floor 至多随 \(Q_C\) 线性增长。因此大 \(Q\) 区域并不会由 (4.1) 自动排除。

脚本还有未证明的模型输入：

- 面积 ODE
  \[
  u'=6+Q_{\rm const}-u(1+u),\qquad u(0)=0
  \]
  是特定共轭径向模型，不是一般二维商空间的方程；
- 代码取 \(Q_{\rm const}=\min(Q_+,3)\)，且面积求解中实际忽略传入的 \(\delta\)；
- \(e_\nu=B\) 或 \(e_\nu=Be^{-2r}\) 都只是 ansatz；
- 修改后的 \(B(\delta,Q_+,Q_-)\) 尚无变量 \(Q\) 的全局 resolvent 定理支撑。

因此
\[
\delta^{**}_{\rm const}=0.185928\ldots,\qquad
\delta^{**}_{\rm decay}=0.210028\ldots
\]
只是两个选定径向模型的数值交点。

可复核的代码问题还包括：

- JSON 在 \(\delta=0.24\) 已给出 \(B=36.343>36\)，与“所研究区间总有 \(B<36\)”冲突；
- 最后标注“at \(\delta=0.246\)”的输出实际调用 \(\delta=0.20\)；
- 循环耗尽 `max_iter` 后仍可能记录 `converged=True`。

---

## 5. 二维 Hodge 结构究竟说明什么

在二维商空间中，
\[
dq_a=S_a,\qquad
S_a=\pm2\rho *_\gamma E(\,\cdot\,,K_a),
\tag{5.1}
\]
其中每个 \(q_a\) 是标量。故沿任一路径 \(\Gamma\)
\[
q_a(x)-q_a(x_0)=\int_\Gamma S_a.
\tag{5.2}
\]
Bianchi/可积条件要求 \(S_a\) 为 exact 一形式。圆柱上的非零周期 harmonic 一形式不能作为额外的 \(dq_a\)；齐次自由度是每个分量的加法常数。平坦连接的 \(H^1\) holonomy 可存在，但 \(F=Q=0\)，不属于物理 twist charge。

所以：

- 一维路径限制本身是合法的；
- 但它只控制选定路径上的变化，不能自动给出全基底 \(Q_+\)；
- 从外端反向传播的权重是增长权重；
- 法向坐标可能遇到 cut locus，separator 未必给出全局射线参数化；
- 切向变化允许不同路径上出现不同峰值；
- \(U\) 的二维二阶方程只控制 Hessian 的迹，允许 Step 92 所示的高窄 \(e_\nu\) 集中。

准确缺失的科学对象是一个真正的 collar 定理，例如控制
\[
\sup_{\Gamma}\int_\Gamma
\bigl(|\sigma_\nu|+\sqrt{e_\nu}\bigr)\,dn
\]
及正确反向 Maxwell 权重，并把 separator 信息转化为全局 \(Q_+\) 控制；还需一个变量 \(Q\) 的 resolvent 定理，始终区分 \(Q_+,Q_C,Q_-\)。

**最终判定：Claim 1 有条件成立；Claim 2 的反向 separator 上界不成立；Claim 3 不构成一般 connector 的自洽闭合。二维 Hodge 结构没有救回该论证，而一维零模已经暴露其根本符号与边界条件问题。**