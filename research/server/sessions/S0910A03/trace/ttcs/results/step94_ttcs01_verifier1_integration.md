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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the Step 94 correction and invariant full-charge derivation. In the convention L=Delta+grad sigma·grad, verify that the diagonal identity LQ=|dQ|^2/Q-18Q-4Q^2 does not exclude an interior maximum and that the scalar even solution y''=-18-4e^y is a valid sign countermodel. Then verify, for fixed nonzero q and F(U)=1/2 q^T M(U)^-1q, beta=log F, using Hess F=Fh and |grad F|^2=F^2 together with L sigma=6+Q and tau_sigma(U)=-Q grad beta, that L log Q=-18-4Q+e-|d(beta o U)|^2. Check all signs and normalizations against the supplied reduction notes/scripts. Assess precisely what remains valid from exact charge conservation and the OT Bochner/resolvent obstruction, versus what must be withdrawn. Finally analyze the proposed two-ended vector-charge flux pairing: identify the strongest derivative-free identity obtainable from Liu's mixed Ricci law, and whether separator stability plus both exact OT end collars presently provide any coercive amplitude bound or whether an additional weighted capacity/area estimate is indispensable. Give a direct mathematical memo, not procedural advice.

## Integrated Scientific Memo

# Step 94 核验备忘录

## 1. 对角恒等式与最大值原理

采用
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle,
\]
对 \(Q>0\) 有
\[
L\log Q=\frac{LQ}{Q}-\frac{|\nabla Q|^2}{Q^2}.
\]
因此
\[
LQ=\frac{|\nabla Q|^2}{Q}-18Q-4Q^2
\]
与
\[
L\log Q=-18-4Q
\]
完全等价。

若 \(p\) 是 \(Q\) 的正内点极大值，则
\[
\nabla Q(p)=0,\qquad LQ(p)=\Delta Q(p)\le0.
\]
方程在 \(p\) 给出
\[
LQ(p)=-18Q(p)-4Q(p)^2<0,
\]
这与 \(LQ(p)\le0\) 完全相容，而非矛盾。因此原先“排除正内点极大值”的推论必须撤回。相反，在对角情形，该方程排除的是正内点局部极小值，因为此时应有 \(L\log Q\ge0\)。

### 标量反例

考虑
\[
y''=-18-4e^y,\qquad y(0)=\log Q_0,\qquad y'(0)=0,\qquad Q_0>0.
\]
乘以 \(2y'\) 并积分得到
\[
(y')^2=36(\log Q_0-y)+8(Q_0-e^y).
\]
解由唯一性为偶函数。又因
\[
y''<-18,
\]
在 \(x>0\) 上有 \(y'(x)<0\)，且
\[
y(x)\le \log Q_0-9x^2.
\]
故解全局存在并满足
\[
y(x)\to-\infty,\qquad e^{y(x)}\to0
\quad(|x|\to\infty).
\]
令 \(Q=e^y\)，则
\[
Q''(0)=Q_0(-18-4Q_0)<0,
\]
所以 \(Q\) 在原点有严格正内点极大值 \(Q_0\)，同时两端趋于零。脚本中的约 \(10^{-9}\) 第一积分残差与此解析结论一致。它只是符号反例，不是耦合约化 Einstein 解。

---

## 2. 固定非零全电荷的 invariant 恒等式

为避免符号混淆，将 Iwasawa 第二坐标记为 \(\zeta\)：
\[
M=
\begin{pmatrix}
e^\alpha+\zeta^2e^{-\alpha}&\zeta e^{-\alpha}\\
\zeta e^{-\alpha}&e^{-\alpha}
\end{pmatrix},
\qquad
h=d\alpha^2+e^{-2\alpha}d\zeta^2.
\]
对固定 \(q=(q_1,q_2)\ne0\)，
\[
F=\frac12q^TM^{-1}q
=\frac12\left[e^{-\alpha}(q_1-\zeta q_2)^2+e^\alpha q_2^2\right]>0.
\]
非零 Christoffel 符号为
\[
\Gamma^\alpha_{\zeta\zeta}=e^{-2\alpha},
\qquad
\Gamma^\zeta_{\alpha\zeta}
=\Gamma^\zeta_{\zeta\alpha}=-1.
\]
直接计算及所给 SymPy 零残差均验证
\[
\operatorname{Hess}F=Fh,\qquad |\nabla F|_h^2=F^2.
\]
令
\[
\beta=\log F,
\]
则
\[
\operatorname{Hess}\beta
=\frac{\operatorname{Hess}F}{F}
-\frac{dF\otimes dF}{F^2}
=h-d\beta\otimes d\beta,
\qquad
|\nabla\beta|^2=1.
\]

现在
\[
Q=e^{-3\sigma}F(U).
\]
在目标变量中
\[
\nabla_{\mathbb H^2}Q
=e^{-3\sigma}\nabla F
=Q\nabla\beta,
\]
故给定的轨道方程
\[
\tau_\sigma(U)=-Q\nabla\beta
\]
与 Step 90 的 \(\tau_\sigma(U)=-\nabla_UQ\) 一致。

加权映射链式法则给出
\[
\begin{aligned}
L(\beta\circ U)
&=\operatorname{Hess}\beta:dU\otimes dU
+d\beta(\tau_\sigma U)\\
&=e-|d(\beta\circ U)|^2-Q,
\end{aligned}
\]
其中 \(e=|dU|^2\)。再由
\[
\log Q=-3\sigma+\beta\circ U,\qquad L\sigma=6+Q,
\]
得到
\[
\boxed{
L\log Q=-18-4Q+e-|d(\beta\circ U)|^2.}
\]
所有符号和归一化均正确：

- \(-18=-3\cdot6\)；
- 面积方程贡献 \(-3Q\)；
- 轨道张力贡献 \(-Q\)；
- 总计 \(-4Q\)。

定义
\[
e_\perp:=e-|d(\beta\circ U)|^2.
\]
由于 \(|\nabla\beta|=1\)，若 \(\{E_i\}\) 是底空间正交标架，则
\[
e_\perp
=\sum_i\langle dU(E_i),J\nabla\beta\rangle^2\ge0.
\]
故一般公式是
\[
L\log Q=-18-4Q+e_\perp.
\]
相应地，
\[
LQ=\frac{|\nabla Q|^2}{Q}-18Q-4Q^2+Qe_\perp.
\]

对角电荷对齐情形 \(q=(q_0,0),\zeta=0\) 下，
\[
\beta=\mathrm{const}-\alpha,\qquad L\alpha=Q,
\]
于是 \(e_\perp=0\)，恢复
\[
L\log Q=-3(6+Q)-Q=-18-4Q.
\]
这独立核验了符号。

在 \(Q\) 的内点极大值处，一般公式只给
\[
-18-4Q+e_\perp=L\log Q\le0,
\quad\text{即}\quad e_\perp\le18+4Q,
\]
仍不产生 \(Q\) 的上界；没有横向能量估计时，反应项本身的符号也不可预先确定。

---

## 3. 精确电荷守恒与 OT 障碍：保留与撤回

Liu 的混合 Ricci 公式为
\[
\operatorname{Ric}(Z,K_a)
=-\frac1{2\rho}\langle dq_a,JZ\rangle,
\qquad \rho=\sqrt{\det G}=e^\sigma.
\]
由于 \(g(Z,K_a)=0\)，对
\[
E=\operatorname{Ric}+3g
\]
有同样的混合分量。等价地，在选定取向下
\[
\boxed{dq_a(W)=2\rho\,E(JW,K_a),}
\]
或写成带 \(*_\gamma\) 的公式时带取向依赖的整体符号。

结合 \(G=e^\sigma M\)，最强的 invariant 范数等式是
\[
\boxed{
e^{-3\sigma}M^{ab}\langle dq_a,dq_b\rangle
=4\,G^{ab}
\langle E(\cdot,K_a),E(\cdot,K_b)\rangle
=4|E_{\rm mix}|_{\rm HS}^2.}
\]
因此 Step 90 所定义的 \(b\) 满足
\[
|b|=2|E_{\rm mix}|_{\rm HS}\le2\sqrt2\,\delta
\]
（四维中由算子范数控制混合 Hilbert–Schmidt 范数）。

### 仍然成立

1. 精确 Einstein 区域中 \(E_{\rm mix}=0\)，故
   \[
   dq=0.
   \]
2. 若一个连通的精确 Einstein principal region 含有精确 OT 开邻域，则该邻域中 \(q=0\)，由常值性得到整个区域
   \[
   q\equiv0.
   \]
   因 \(q=\rho Gf\) 且 \(G\) 可逆，遂有 \(f=0\)，即全局 OT。
3. Koiso 初值若给出 \(q=0\)，其精确 Einstein 延拓保持 OT。
4. Steps 85–88 中对**全局 OT 类**建立的独立 Bochner/resolvent 障碍不受此次符号修正影响。所给材料不足以重新核算其中 \(\delta_*\approx0.246\) 的数值，但 Step 94 不推翻其机制。
5. 前向 cusp 阻尼仍成立；它只由 separator 数据控制 cusp 侧，而不能反向控制 separator。

### 必须撤回

1. 由对角 \(LQ\) 方程排除正内点极大值；
2. 由 \(Q\to0\) 于两端推出 \(Q\equiv0\)；
3. 将对角公式无修改地用于一般轨道映射；
4. 由 \(Q\) 方程独立重证 OT connector 障碍；
5. 仅靠弱积分分部或 \(C^0\) 混合 Ricci 控制推出 \(Q=O(\delta^2)\)；
6. Step 93 中把前向衰减核反向使用所得的 \(\delta^{**}=0.186,0.210\) 阈值。

必须保持物理电荷与坐标电荷的区别：
\[
Q=\frac12e^{-3\sigma}q^TM^{-1}q\to0
\]
并不蕴含 \(q\to0\)。非零守恒 \(q\) 可因面积及轨道因子的增长而被 redshift 到 \(Q\to0\)。

---

## 4. 两端 vector-charge flux pairing

由 Liu 定律，对任意跨越路径 \(\gamma\)，
\[
q_a(\gamma_+)-q_a(\gamma_-)
=\int_\gamma dq_a
=2\int_\gamma \rho\,E(J\dot\gamma,K_a)\,dt.
\]
若两端均有精确 OT collar，则两端 \(q=0\)，从而
\[
\int_\gamma dq=0.
\]
又因 \(dq\) 是 exact vector-valued one-form，
\[
\oint_\Gamma dq=0
\]
对所有闭路成立。这些是严格的产生—湮灭通量抵消条件，但不是振幅控制。

为写成标量弱配对，先固定 \(\ell\in\mathbb R^2\)，令
\[
q_\ell=\ell^aq_a,\qquad K_\ell=\ell^aK_a.
\]
在边界位于两个 OT collars 内的区域 \(\Omega\) 上，
\[
\int_\Omega\langle dq_\ell,du\rangle\,d\mu
=-\int_\Omega q_\ell\Delta u\,d\mu,
\]
因为边界项由 \(q_\ell=0\) 消失；同时
\[
\int_\Omega\langle dq_\ell,du\rangle\,d\mu
=2\int_\Omega\rho\,
\langle E(J\cdot,K_\ell),du\rangle\,d\mu.
\]
漂移权重形式是
\[
\int_\Omega \rho\langle dq_\ell,du\rangle\,d\mu
=-\int_\Omega \rho q_\ell Lu\,d\mu.
\]

原 Step 94 式 (4.6) 的 \(d^*\) 号需澄清：若采用标准约定
\[
d^*du=-\Delta u,
\]
则
\[
-\int q\,\Delta u=+\int q\,d^*du,
\]
而不是 \(-\int q\,d^*du\)。此外，不先与 \(\ell\) 收缩时，该等式应理解为逐分量或向量值等式。

若 \(u\) 只是两端取相反常数的调和函数，上述配对可退化为零，不能控制 \(q\)。加入质量项至多给出某个加权矩，若无谱隙或容量下界仍不具 coercivity。

---

## 5. 现有数据不能给出两端振幅界

两端 \(q=0\) 加
\[
|dq|\lesssim\delta\rho
\]
只给
\[
|q(x)|\lesssim \delta\inf_\gamma\int_\gamma\rho\,ds,
\]
其常数可随 connector 的加权长度增长。最简单的一维模型
\[
q(0)=q(L)=0,\qquad |q'|\le\delta
\]
允许三角形轮廓
\[
\max|q|=\frac{\delta L}{2}.
\]
因此端点抵消及一阶源界本身没有长度无关的振幅控制。

separator 稳定性与切向 Maxwell 输运确实给出
\[
\sup_CQ\le C_Q(\delta),
\]
但：

- 该界只在 separator 曲线上成立；
- 它是有限界而非随 \(\delta\to0\) 消失的小量界；
- 正常输运还涉及
  \[
  |h_\nu|+\sqrt{e_\nu};
  \]
- Step 92 的精确 Koiso germs 表明，即使有完整稳定性、Einstein 约束和局部精确 Einstein 解，\(e_\nu\) 仍可任意大。

故现有 separator 稳定性、两个精确 OT collars 与 exact flux cancellation 尚不能控制
\[
Q_+=\sup_BQ
\]
或内部 \(q\) 的振幅。

真正缺失的是对矩阵权
\[
A=e^{-3\sigma}M^{-1}
\]
的长度/面积不退化 coercive 不等式，例如某种
\[
\int_\Omega q^TAq\,d\mu_\sigma
\le C\int_\Omega(dq)^TA(dq)\,d\mu_\sigma
+\text{separator trace term},
\]
其中 \(C\) 必须在任意 connector 长度及轨道面积增长下保持受控。普通无权两端容量不够：长度 \(L\) 区间上连接 \(-1\) 与 \(1\) 的线性函数，其 Dirichlet 能量是 \(4/L\to0\)。

因此额外的**加权容量/面积估计是不可缺少的**。它必须把通量 exactness 与
\[
L\sigma=6+Q-T,
\]
separator Jacobi 形式及水平/轨道方程耦合起来。现有结果只提供：

- 精确区域内的电荷守恒；
- 两端总通量抵消；
- separator 上有限但不小的 \(Q\) 界；
- 前向 cusp 阻尼；
- 全局 OT 子类的独立 Bochner/resolvent 障碍。

它们尚未形成被迫两端 twisted connector 的 coercive 振幅估计。