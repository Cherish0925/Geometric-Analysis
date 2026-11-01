# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step93_signed_maxwell_self_consistent.py",
    "Sessions/S0910A03/workspace/data/step93_signed_maxwell_self_consistent.json",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md",
    "Sessions/S0910A03/workspace/notes/step88_reflection_free_minimal_separator.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md"
  ]
}
```

## Task

Verify the signed Maxwell transport argument for the free-T² two-ended connector with twist. The setup: a free-T² invariant 4-manifold with two complete outward-expanding cusp ends and ||Ric+3g||_op ≤ δ. The physical twist w = √(2Q) satisfies the invariant transport |dw + (3/2)w dσ| ≤ (1/2)w|dU| + |b|, where |b| ≤ 2√2δ from mixed Ricci (equation 5.1 of step90). Three claims to verify:

1. KOISO OT THEOREM: The Step 92 constrained Koiso germs have q=0 (no charge) initial data. Under exact Ric=-3g, Maxwell conservation gives dq=0, so q≡0 throughout the germ domain. The germ is OT and blocked by Steps 85-88. Is this reasoning correct?

2. SIGNED CUSP TRANSPORT: On the expanding cusp where σ_ν→2 and e_ν→0, the coefficient a=-(3/2)σ_ν+√e_ν/2→-3. Starting from w=0 at the cusp end, the Gronwall bound gives w ≤ 2√2δ∫ exp(-(3/2)(σ(t)-σ(r)) + (1/2)∫√e_ν dτ) dt. Using e_ν ≤ B(δ)=sup e everywhere, the exponent is -(3-√B/2)(t-r). Since B(δ)<36 for δ<δ*, this converges: w_sep ≤ 2√2δ/(3-√B/2). Is this derivation correct? What are the mathematical conditions?

3. SELF-CONSISTENT LOOP: Using B(δ,Q+,Q-) from the resolvent, Q+ = w²/2 from the transport, Q- = 0 at cusps, the iteration Q→B→w→Q converges because Q appears quadratically in w but only linearly in B. The gap function floor-ceiling = (12+2Q-8δ) - B(δ,Q,0) changes sign at δ**≈0.186 (worst-case constant e_ν) or δ**≈0.210 (decaying e_ν). Is this self-consistent closure mathematically legitimate?

Key concern: the 1D signed transport along normal rays may not capture the full 2D charge distribution on the base. Does the Hodge-theoretic structure of the Maxwell equation support a 1D reduction for bounding Q at the separator? Or are there 2D charge modes that evade the 1D damping estimate?

## Output

# 科学核验备忘录

## 总结

1. **Koiso 数据的 OT 延拓：在明确假设下成立。** Step 92 的 Cauchy 数据确实给出零 Maxwell 电荷；同一自由 \(T^2\) 对称类中的连通、精确 Einstein 延拓保持 \(q_a\equiv0\)。若该延拓进一步具有 Steps 85–88 所需的完整双外扩端和圆柱商空间，则 \(\delta=0\) 的 OT 定理排除这种完整延拓。

2. **由 cusp 端的 \(w=0\) 反推 separator 的衰减核不成立。** 衰减因子控制从内部向外端的正向传播；从外端反向估计内部值时，指数符号相反，得到放大因子。即使 \(e_\nu=0\)、\(\sigma_\nu=2\)，Maxwell 方程本身也允许有界混合 Ricci 源在 separator 产生任意大的 \(w\)。

3. **数值自洽迭代不是一般自由 \(T^2\) connector 的数学闭合。** 它同时把三个不同量
   \[
   Q_+=\sup_BQ,\qquad Q_C=\langle Q\rangle_C,\qquad Q\text{ 沿单条射线的值}
   \]
   设为同一个数，并采用未由一般几何推出的径向面积 ODE 与 \(e_\nu\) 剖面。数值 \(0.1859\) 和 \(0.2100\) 是该选定模型的交点，不是双端 connector 的通用阈值。

---

## 1. Step 92 Koiso germ 的 Maxwell 电荷

Step 92 的初始三维度量为
\[
g_\Sigma=ds^2+M(U(s))_{ab}\,dx^adx^b,
\]
Weingarten 张量满足
\[
W(\partial_s)=0,
\]
而非零部分只在竖直无迹块中。采用 Gaussian 法向坐标 \(n\) 并令 \(A_n=0\)，有
\[
F^a_{ns}=\partial_nA_s^a.
\]
初始度量没有 \(ds\,dx^a\) 项，而 \(W_{sa}=0\) 给出其法向导数也为零，因此
\[
F^a_{ns}=0,\qquad
q_a=\rho G_{ab}(*_\gamma F^b)=0
\]
在初始曲线上成立。这里需区分 Step 92 中表示诱导度量的符号 \(q\) 与 Maxwell 电荷 \(q_a\)。

精确 Einstein 情形 \(E=\operatorname{Ric}+3g=0\) 下，Step 90 的混合 Ricci 公式成为
\[
dq_a=0.
\]
在连通商空间中，\(q_a\) 是常向量；初始曲线上的零值因而推出
\[
q_a\equiv0,\qquad F^a\equiv0.
\]
解析 Cauchy 数据具有 \(T^2\) 对称性，Koiso 解析解的局部唯一性保留这一对称性。因此 germ 的水平分布可积，局部为 OT。平坦连接仍可能具有平移 holonomy，但它不产生 \(F\) 或 \(Q\)，也不改变 OT 的局部方程。

于是，**任何保持自由 \(T^2\) 对称、精确 Einstein 且连通的继续延拓仍然是 OT**。若它还是完整的、商空间为 \(S^1\times\mathbb R\)、并具有 Steps 85–88 的两个精确外扩端，则 Step 88 在 \(\delta=0\) 给出
\[
\sup e\ge12,\qquad \sup e\le6,
\]
形成矛盾。

这并不涉及随后允许 \(E\ne0\) 的拼接区域，因为此时
\[
dq_a=\pm2\rho *_\gamma E(\,\cdot\,,K_a)
\]
可以生成电荷。

---

## 2. Maxwell 传播的方向

沿一条向 cusp 外部延伸的单位速曲线 \(\gamma(t)\)，令
\[
p(t)=\frac32\sigma'(t),\qquad
c(t)=\frac12|U'(t)|,\qquad
\beta(t)=|b(\gamma'(t))|.
\]
若采用方向化的 Maxwell 估计，则
\[
|w'+pw|\le cw+\beta.
\tag{2.1}
\]
若只有 Step 90 写出的总范数形式，则右侧只能先用 \(|dU|\)；要替换为
\(\sqrt{e_\nu}=|U'|\)，还需使用其张量层面的方向化版本。

由 (2.1) 得到两个不同方向的不等式：
\[
w'+(p-c)w\le\beta,
\tag{2.2}
\]
\[
w'+(p+c)w\ge-\beta.
\tag{2.3}
\]

### 正向传播

从内部 \(r\) 向外部 \(t\) 积分 (2.2)，得到
\[
w(t)\le
e^{-\int_r^t(p-c)}w(r)
+\int_r^t
e^{-\int_s^t(p-c)}\beta(s)\,ds.
\tag{2.4}
\]
因此若 \(p-c>0\)，已有的内部电荷向外传播时衰减。这是 cusp 的物理红移。

### 从外端反推内部

若在外侧有限位置 \(R\) 已进入精确 OT 端，因而 \(w(R)=0\)，则应积分 (2.3)：
\[
w(r)\le
\int_r^R
\beta(s)\exp\!\left(
\int_r^s[p(\tau)+c(\tau)]\,d\tau
\right)ds.
\tag{2.5}
\]
这里是**增长指数**，而不是
\[
\exp\!\left(-\int_r^s(p-c)\right).
\]
所以外部零值不能借助 cusp 红移给出长度无关的内部上界。

### 一维显式反例

取精确 cusp 系数
\[
\sigma=2t,\qquad U=\mathrm{const},\qquad p=3,\qquad c=0.
\]
令 \(0\le\phi\le1\) 为支撑在远端附近的光滑平坦截断，实际有符号源为
\[
b_s(t)=-\beta_0\phi(t),\qquad |b_s|\le\beta_0.
\]
定义
\[
w(r)=e^{-3r}\int_r^R\beta_0e^{3s}\phi(s)\,ds.
\]
则
\[
w'+3w=-\beta_0\phi,
\]
而在 \(\phi\) 支撑外侧有 \(w=0\)，可与精确 OT 端光滑相接。若支撑位于 \(R-O(1)\)，则
\[
w(0)\asymp \beta_0e^{3R}.
\]
故即使
\[
e_\nu=0,\qquad B=0<36,
\]
separator 电荷仍可随过渡长度指数增长。这个一维零 Fourier 模式已经足以否定所提的反向衰减估计，无需二维振荡模式。

另一个基本区别是：若只知道
\[
w(t)\longrightarrow0,
\]
这不推出 Maxwell 电荷为零。无源解
\[
w(t)=Ce^{-3t}
\]
也趋于零，对应非零常坐标电荷。只有端部存在一个 \(F=0\) 的精确开集，才能推出那里 \(q_a=0\)。

### 所写积分何时收敛

单独考虑
\[
I(r)=\int_r^\infty
\exp\!\left[
-\frac32(\sigma(t)-\sigma(r))
+\frac12\int_r^t\sqrt{e_\nu}\,d\tau
\right]dt,
\]
若从 \(r\) 开始逐点满足
\[
\sigma'\ge2,\qquad e_\nu\le B<36,
\]
则
\[
I(r)\le\frac1{3-\sqrt B/2}.
\]
若仅有 \(\sigma'\to2\)、\(e_\nu\to0\)，尾积分仍然有限，但有限过渡段产生额外乘法常数，不能直接得到上述分母。脚本所用面积模型恰有
\[
u(0)=\sigma'(0)=0,\qquad u(t)<2
\]
于有限 \(t\)，所以该逐点估计甚至不适用于其 separator 到 cusp 的整个区间。更重要的是，\(I(r)\) 的收敛并不能把它变成由外端反推 \(w(r)\) 的 Green 核。

---

## 3. 数值自洽循环中的数学不等价

### 3.1 三个 \(Q\) 不能合并

Step 90 的 resolvent–separator 关系是
\[
12+2Q_C-8\delta
\le B(\delta,Q_+,Q_-),
\]
其中
\[
Q_C=\frac{\int_CQ\rho\,ds}{\int_C\rho\,ds},\qquad
Q_+=\sup_BQ,\qquad Q_-=\inf_BQ.
\]
精确 OT 端确实给出 \(Q_-=0\)。但脚本进一步设置
\[
Q_C=Q_+=\frac12w_{\rm sep}^2.
\]
一般情形没有这一等式：

* 一条法向曲线上的 \(w_{\rm sep}\) 不是 \(C\) 上的加权平均；
* separator 上的最大值不必等于整个二维商空间中的最大值；
* Maxwell 源可以在 collar 内产生离开 separator 的局部峰值。

Step 92 已明确说明其 Jacobi–Maxwell 结果只给出 \(\sup_CQ<\infty\)，并不控制 \(\sup_BQ\)。

而且，对 \(Q_C\) 的上界不能作为 floor 中 \(+2Q_C\) 的替代值。若只使用 \(Q_C\ge0\)，通用 floor 仍是
\[
12-8\delta.
\]

### 3.2 固定点迭代没有给出全体解的估计

脚本从 \(Q=0\) 迭代某个等式映射。即使数值序列收敛，这也只找到该映射所选中的一个固定点。若原几何只提供
\[
Q_+\le F(Q_+)
\]
之类的不等式，还需证明所有允许的 \(Q_+\) 都落在同一有限区间，并排除较大的固定点或不变分支。

“\(B\) 对 \(Q\) 仅线性依赖”也不符合脚本公式。令
\[
K=3+\delta,\qquad f=Q+2\delta.
\]
当 \(Q\) 大时，
\[
B=
\left[
\frac{2f}{\sqrt K}
+\sqrt{2K+\frac{5f^2}{K}}
\right]^2
\sim
\frac{(2+\sqrt5)^2}{K}f^2.
\]
因此 \(B\) 对大 \(Q\) 是二次增长，不能由“\(w^2\) 是二次量”推出压缩性质。

### 3.3 面积和 \(e_\nu\) 剖面是附加 ansatz

脚本采用
\[
u'=6+Q_{\rm const}-u(1+u),\qquad u(0)=0.
\]
这需要特定的共轭一维基底几何；一般二维商空间的面积方程还含有基底散度、变量 \(Q\) 和 \(T\)。代码还使用
\[
Q_{\rm const}=\min(Q_+,3)
\]
并忽略 `delta` 参数。较大的常 \(Q\) 会增强面积增长并减小计算出的输运量，因而不能代表所有允许的变量剖面。

同样，
\[
e_\nu=B e^{-2r}
\]
只是选定模型，并非由 Maxwell、Jacobi 或水平 Einstein 方程推出。

### 3.4 文件内部的可见不一致

* JSON 的 worst-case 数据在 \(\delta=0.24<\delta_*\) 已记录
  \[
  B=36.343>36,
  \]
  所以“在所研究区域总有 \(B<36\)”与该数据不一致。
* 脚本最终打印“at \(\delta=0.246\)”，但实际调用的是
  ```python
  self_consistent_obstruction(0.20, ...)
  ```
  因而该摘要行展示的是 \(\delta=0.20\) 的数值。
* `converged=True` 在循环耗尽 `max_iter` 后仍会写入；函数没有单独记录是否真正达到容差。

因此
\[
\delta^{**}_{\rm const}\approx0.185928,\qquad
\delta^{**}_{\rm decay}\approx0.210028
\]
可以视为脚本中两个径向 ansatz 的数值交点，但不提供一般 connector 的排除结果。

---

## 4. 二维 Hodge 结构

Maxwell 方程在二维商空间上是
\[
dq_a=S_a,\qquad
S_a=\pm2\rho *_\gamma E(\,\cdot\,,K_a).
\]
这里 \(q_a\) 是两个标量函数。因此对任意路径 \(\Gamma\)，
\[
q_a(x)-q_a(x_0)=\int_\Gamma S_a.
\]
Einstein–Bianchi 结构保证 \(S_a\) 是恰当的 exact 一形式；圆柱上的非零周期 harmonic 一形式不能作为独立 Maxwell 源出现。齐次解只是常向量 \(q_a\)。平坦连接的 \(H^1\) holonomy 可以非零，但 \(F=Q=0\)，与物理 twist 无关。

所以主要问题不是隐藏的 Hodge 模式：**一维路径积分在每条给定路径上是成立的。** 真正缺少的是：

1. 从每个 separator 点到精确端部的统一几何路径控制；
2. 对正确反向权重
   \[
   \int \beta(s)e^{\int(p+c)}
   \]
   的长度无关估计；
3. 把 separator 数据与全局 \(Q_+\) 联系起来的二维椭圆或单调性结果。

法向指数映射还可能出现交叉或 cut locus，因此一般商空间未必由 separator 的全局法向射线参数化。二维切向变化会使不同路径上的峰值和权重不同，但零切向 Fourier 模式已经展示了核心问题。

**最终数学结论：Koiso 的精确 Einstein germ 保持 OT；所提 signed cusp 反向输运公式符号方向错误；由此建立的自洽阈值没有闭合一般自由 \(T^2\) 双端 connector。**