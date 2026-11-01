# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 98,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step98_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step98_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical and computational substance of Step 98's full-matrix charged-Koiso matching experiment. Focus on: (i) the Gaussian formulas for all blocks of E=Ric+3g, especially E_nn, E_ni=div K-dH, and E_ij; (ii) whether q=q0^{1/2} exp(X) q0^{1/2} with X_n(0)=±2A and X_nn(0)=2(Rhat+3I) really reproduces q_n=±2K0 and the sign-independent exact Einstein q_nn jet, including noncommutative exponential terms; (iii) invariant norm computation by Cholesky conjugation; (iv) what the low-resolution direct nodal residual decrease actually establishes and what aliasing, endpoint, regularization, underresolution, or overfitting artifacts remain; and (v) propose the most decisive convergence/cross-resolution experiment and residual-projection calculation. Read the actual scripts and JSON evidence. Return corrections with explicit equations, not generic process advice.

## Integrated Scientific Memo

# Step 98 全矩阵 charged-Koiso 实验核验结论

## 1. Gaussian 坐标中的全部 \(E=\operatorname{Ric}_g+3g\) 分块

令
\[
g=dr^2+q_{ij}(r,s)\,dy^i dy^j,\qquad
K=\frac12q_r,\qquad W=q^{-1}K,\qquad H=\operatorname{tr}W.
\]
非零混合 Christoffel 符号为
\[
\Gamma^r_{ij}=-K_{ij},\qquad
\Gamma^i_{rj}=W^i{}_j,\qquad
\Gamma^i_{jk}=\Gamma(q)^i{}_{jk}.
\]
由
\[
H_r=\operatorname{tr}(q^{-1}K_r)-2\operatorname{tr}(W^2)
\]
得到
\[
\boxed{E_{rr}
=3-\operatorname{tr}(q^{-1}K_r)+\operatorname{tr}(W^2),}
\]
\[
\boxed{E_{ri}
=q^{jk}\nabla_jK_{ki}-\partial_iH,}
\]
\[
\boxed{E_{ij}
=\operatorname{Ric}(q)_{ij}+3q_{ij}
-(K_r)_{ij}-HK_{ij}
+2(Kq^{-1}K)_{ij}.}
\]

这与 `full_residual` 中的 `Enn`、`mom`、`ET` 完全一致。特别地，只有 \(s=y^0\) 方向有导数，因此
```python
nab = ks[:,kk,i] if j == 0 else 0
```
中的导数方向 \(j\) 正确；这里没有遗漏 \(\partial q^{jk}\)，因为计算的是协变散度 \(q^{jk}\nabla_jK_{ki}\)。

测试度量 \(q=e^{2r}I\) 满足 \(K=q\)、\(K_r=2q\)、\(H=3\)、\(W=I\)，故所有分块严格为零。JSON 中 \(2.46\times10^{-11}\) 的误差验证了径向微分和符号，但这一测试本身不检验空间变化的 Codazzi 项；后者由上述张量推导及中心分辨率实验支持。

一个必须明确的建模事实是：脚本所接的
\[
q(r)=e^{2r}q_0
\]
一般不是精确 Einstein 外端。事实上
\[
E_{rr}=E_{ri}=0,\qquad E_{ij}=\operatorname{Ric}(q_0)_{ij},
\]
从而
\[
\|E\|_{\mathrm{op},g}
=e^{-2r}\left\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\right\|_{\mathrm{op}}.
\]
这解释了 \(R=1\) 时端点残差 \(1.07419\) 和 \(R=2.5\) 时 \(0.0534808\)，两者之比为 \(e^{-3}\)。因此这里是渐近变小的占位外端，不是有限 \(R\) 处的精确 Einstein 附着。

---

## 2. 矩阵指数中心 jet，包括非交换项

记
\[
S=q_0^{1/2},\qquad
A=S^{-1}K_0S^{-1},\qquad
\widehat R=S^{-1}\operatorname{Ric}(q_0)S^{-1},
\]
并令
\[
q=S e^X S,\quad X(0)=0,\quad
X_r(0)=2\varepsilon A,\quad
X_{rr}(0)=2(\widehat R+3I),\qquad \varepsilon=\pm1.
\]

在 \(X=0\) 处，
\[
\left.\frac{d}{dr}e^X\right|_0=X_r(0),\qquad
\left.\frac{d^2}{dr^2}e^X\right|_0=X_{rr}(0)+X_r(0)^2.
\]
这不要求 \(X_r\) 与 \(X_{rr}\) 对易。展开
\[
X=rB+\frac12r^2C+O(r^3)
\]
后，二阶项只有 \(\frac12C+\frac12B^2\)；\(BC\)、\(CB\) 等非交换项从三阶才出现。

因此
\[
q_r(0)=S(2\varepsilon A)S=2\varepsilon K_0,
\]
且
\[
\begin{aligned}
q_{rr}(0)
&=S\left(2(\widehat R+3I)+4A^2\right)S\\
&=2\operatorname{Ric}(q_0)+6q_0+4K_0q_0^{-1}K_0\\
&=2\left(\operatorname{Ric}(q_0)+3q_0+
2K_0q_0^{-1}K_0\right).
\end{aligned}
\]
中心为极小超曲面，\(H=0\)，故这正是 Einstein 演化式给出的
\[
q_{rr}=2K_r
=2\bigl(\operatorname{Ric}(q_0)+3q_0-HK_0+2K_0q_0^{-1}K_0\bigr).
\]
符号只通过 \(X_r^2=4A^2\) 进入，所以二阶 jet 对 \(\varepsilon\) 完全独立。

在 \(r=R\) 处 \(X=2RI\)，其与所有矩阵对易；由 \(X_r=2I\)、\(X_{rr}=0\) 得
\[
q_r(R)=2q(R),\qquad q_{rr}(R)=4q(R).
\]
有限模态脚本中的扰动含因子 \(t^3(1-t)^3\)，故其函数值及前两阶导数在两端均为零，确实解析地保持这些 jet。

### 直接 nodal 脚本的关键例外

上述结论不适用于 `step98_direct_spd_transition.py` 优化后的插值场。它只固定 \(X\) 的端点值，内部 nodal 值会改变插值多项式的端点导数；随后 evaluator 把端点 \(q_r,q_{rr}\) 强行替换为目标值。因此其残差评估没有证明优化后场具有真实 \(C^2\) 附着。

若 \(X^I\) 是 nodal 数据的 Chebyshev 插值，则应额外报告
\[
\Delta q_r(0)=S\bigl(X_r^I(0)-2\varepsilon A\bigr)S,
\]
\[
\Delta q_{rr}(0)=S\left(
X_{rr}^I(0)+X_r^I(0)^2
-2(\widehat R+3I)-4A^2\right)S,
\]
以及
\[
\Delta q_r(R)=e^{2R}S\bigl(X_r^I(R)-2I\bigr)S,
\]
\[
\Delta q_{rr}(R)=e^{2R}S\bigl(
X_{rr}^I(R)+X_r^I(R)^2-4I\bigr)S.
\]
当前 JSON 未保存这些量。

此外，代码用 Chebyshev 矩阵微分 nodal \(q\)，这对应“\(q\) 的多项式插值”；而连续 SPD 解释 \(q=S e^{X^I}S\) 一般有不同导数。前者在节点间也不保证正定。端点覆盖隐藏了这一区别。

---

## 3. Cholesky 共轭给出的确是不变量范数

若
\[
g=LL^T,
\]
脚本的两次线性求解得到
\[
E_{\mathrm{orth}}=L^{-1}EL^{-T}.
\]
令正交标架矩阵 \(B=L^{-T}\)，则
\[
E_{\mathrm{orth}}=B^TEB.
\]
其特征值就是广义特征值
\[
Ev=\lambda gv,
\]
因此
\[
\max_\alpha|\lambda_\alpha(E_{\mathrm{orth}})|
\]
是相对于 \(g\) 的不变算子范数，适合检验 Ricci 二次型夹逼。

对称矩阵打包中非对角元乘 \(\sqrt2\)，故
\[
\|\operatorname{packed}(E)\|_2^2
=\sum_iE_{ii}^2+2\sum_{i<j}E_{ij}^2
=\|E_{\mathrm{orth}}\|_{\mathrm{HS}}^2.
\]
这一实现正确。相反，`minimum_q_eigenvalue` 只是所选坐标下、采样节点上的正定性指标，不是几何不变量，也不控制节点之间。

---

## 4. 低分辨率 nodal 残差下降究竟说明什么

在 \(N_r=11,N_s=16,R=1\) 的直接 nodal 实验中，端点排除的离散几何残差为
\[
260.21\to8.90 \quad(+\text{ half}),\qquad
137.10\to8.22 \quad(-\text{ half}).
\]
沿保存的线段该离散量单调下降。因此它确实证明：在该粗网格和正则化目标下，全对称矩阵 nodal 方向能抵消基准五次插值残差的很大部分。除此之外尚不能推出连续几何结论。

主要伪影如下。

1. **最终 supremum 是中心 Fourier 离散误差。**  
   两侧最终值都精确等于
   \[
   1.36341853842137,
   \]
   峰值位于 \(r=0\)，且来自 \(E_{ri}\)。中心表显示该量随 \(N_s\) 为
   \[
   1.3634,\ 0.7084,\ 0.3289,\ 0.07121,\ 0.01212,\
   3.04\!\times10^{-4},\ 6.76\!\times10^{-6}.
   \]
   解析上中心动量约束为零。因此 \(1.36\) 是未解析的 Codazzi/Fourier 误差，不是几何残差下界。

2. **端点残差被优化目标排除。**  
   \(R=1\) 外端的 \(1.07419\) 是上述非 Einstein 外端的真实残差，但 `exclude_endpoints=true` 使其不进入 least squares。

3. **解尚未收敛。**  
   两侧均因 `max_nfev=4` 停止，`success=false`，最优性指标为 \(745.9\) 和 \(79.7\)。输出只是显著下降的中间迭代，不是驻点。

4. **正则化不可忽略。**  
   由总 cost 与几何残差可算出正则化向量范数约为 \(5.82\) 和 \(4.36\)。它只惩罚径向二阶导数，不惩罚 \(s\) 方向网格尺度振荡。

5. **严重的过参数化/拟合风险。**  
   有 \(864\) 个内部未知量，而每个内部节点只有 10 个完整 Einstein 分量；虽非严格“未知数等于残差数”，但自由度很高且 Jacobian 未保存。矩阵指数、逆矩阵、Christoffel 乘积及 \(Kq^{-1}K\) 都产生超出截断频率的模态，而脚本没有 padding/dealiasing 或独立网格验证。

6. **分辨率变化时中心数据本身也在变化。**  
   `initial_data` 用离散 Fourier 导数构造 \(K_0\)，所以不同 \(N_s\) 并非严格采样同一个冻结的解析 Cauchy 数据。

7. **JSON 不足以复验优化结果。**  
   未保存 `ls.x`、\(X\)、\(q\) 或模态系数，无法把优化场 prolong 到更细网格重新计算。

8. **\(N_r=35,N_s=64,R=2.5\) 文件没有做优化。**  
   其 `gn_steps=0`，故 \(970.66\) 和 \(99.57\) 仅是未修正 quintic 初值的残差；没有 Jacobian、SVD 或 nonlinear decrease，不能与直接 nodal 结果比较。

---

## 5. 最有判别力的交叉分辨率实验

应使用解析保持端点 jet 的嵌套模态参数化
\[
X_\varepsilon(t,s)
=X_{\varepsilon,\mathrm{Hermite}}(t,s)
+t^3(1-t)^3
\sum_{\ell=0}^{m}\sum_{|k|\le K}
C_{\ell k}^{(\varepsilon)}
T_\ell(2t-1)e^{iks},
\]
其中系数满足实性与矩阵对称条件。这样兼有全矩阵自由度和真实 \(C^2\) 附着，不需要覆盖端点导数。

决定性测试应同时包含：

- 从 Step 94 解析公式冻结同一组 \(q_0,K_0\)，避免中心数据随 \(N_s\) 改变；
- 嵌套 \((m,K)\) 空间，并分别增加径向与 Fourier 截断；
- 在独立、相移且至少高 \(3\)–\(4\) 倍的网格上重算未正则化残差；
- 至少覆盖 \(N_s=96,128\)，因为中心表明低分辨率尚未解析动量约束；
- 不覆盖端点导数，并报告上述四个 jet 误差；
- 分别报告 \(rr,ri,ij\) 分块、密集网格不变算子 supremum、带体积元和正交基系数尾部的 \(L^2\) 范数；
- 报告 fine-grid 最小 \(q\) 特征值以及指数特征值 clipping 是否触发；
- 逐级减小正则化，并单独报告纯几何目标；
- 固定高分辨率后再比较多个 \(R\)，将中心、严格内部、外端残差分开。

若粗网格优化场在独立细网格上残差反弹，即为 aliasing/过拟合；若细网格范数稳定下降且模态尾部衰减，才构成连续近似匹配的证据。对 \(R\) 的测试还应核对外端项的 \(e^{-2R}\) 衰减，并观察内部残差是否趋于正下界。

---

## 6. 正确的残差投影与跨分辨率 Jacobian 检验

使用体积元与求积权重 \(W\)，定义
\[
\widehat F=W^{1/2}F,\qquad
\widehat J=W^{1/2}J.
\]
若
\[
\widehat J=U\Sigma V^T,\qquad
p_j=u_j^T\widehat F,
\]
则在数值阈值 \(\tau\) 下
\[
P_\tau\widehat F
=\sum_{\sigma_j>\tau}p_j u_j,\qquad
\widehat F_\perp
=\widehat F-P_\tau\widehat F.
\]
应报告
\[
\sigma_j,\qquad p_j,\qquad |p_j|/\sigma_j,
\]
并把重要左奇异场按 \(rr,ri,ij\) 分块、径向位置和 Fourier 模态分解。

现有 ridge 步
\[
\Delta x
=-\sum_j\frac{\sigma_jp_j}{\sigma_j^2+\rho^2}v_j
\]
是正确的；其 ridge 有效可消除部分为
\[
-J\Delta x
=\sum_j\frac{\sigma_j^2}{\sigma_j^2+\rho^2}p_j u_j.
\]
但脚本中的
```python
accessible = U @ (U.T @ F)
```
无阈值地纳入全部返回奇异向量，包括数值零奇异值方向，也不等于 ridge 有效投影。应使用阈值投影或上述 ridge 因子。

最关键的跨分辨率对象是
\[
J_{m\to M}
=D\mathcal F_M(Px_m)\,P,
\]
即在细网格上对 prolong 后的粗模态系数求 Jacobian。先把 fine-grid 残差投影到 \(\operatorname{ran}J_{m\to M}\)，再投影到新增模态壳层，可区分：

- 粗空间本已可调但优化未收敛的残差；
- 只有加密后才可见/可调的欠分辨率残差；
- 对全部已解析方向近乎正交的候选障碍。

同时追踪最小奇异值及其左奇异场：中心局域化通常表示 Codazzi 分辨率伪影，外端局域化表示非 Einstein 附着，稳定分布于内部且与精确中心数据非零配对，才可能是有限维障碍的数值迹象。

**最终核验结论：** Gaussian 分块公式、矩阵指数中心 jet（包括非交换二阶项）和 Cholesky 不变量范数均正确。当前直接 nodal 下降仅是粗网格、未收敛、受正则化稳定的离散下降；其最终 supremum 被中心 Fourier 误差控制，而且优化场没有验证真实端点 jet。尚未确定的科学对象是：冻结同一解析中心数据后，独立细网格上的内部未正则化残差及其全分块 Jacobian 正交余量，随模态分辨率和 \(R\) 的极限行为。