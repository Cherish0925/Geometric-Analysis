# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step80_base_identity_verify.py",
    "Sessions/S0910A03/workspace/data/step80_base_identity.json",
    "Sessions/S0910A03/workspace/scripts/step80_joint_base_response.py",
    "Sessions/S0910A03/workspace/data/step80_joint_base_response_summary.json",
    "Sessions/S0910A03/workspace/data/step80_residual_atlas.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md"
  ]
}
```

## Task

Independently read and assess the Step 80 joint reflected-core finite-mode experiment for the Yau 26 negative graph-manifold route. Check (i) the invariant base equation and physical-coordinate source/measure corrections; (ii) whether the script really enforces the scalar-minus-six reflected center and projected Koiso second jet and evaluates all five Ricci components; (iii) what the paired shape-only versus joint base/area runs actually establish about compensation, especially the persistent residual layer near physical r≈0.2 and the fact that exit data become favorable while sup residual does not; (iv) identify any formula, parameterization, optimization, sampling, or interpretation error that would invalidate or sharply narrow the result. Derive the most informative next finite-mode or analytic test aimed at the inner compensation layer rather than the already solved exterior tail. Treat all numerical failures as finite-dimensional evidence, not a theorem.

## Output

# Step 80 科学核验备忘录

## 一、核心结论

1. `step80_base_identity_verify.py` 中的基底 Ricci 恒等式、冻结双曲尖点上的
   \(-\frac12\,dv\otimes dv\) 应力，以及物理高斯坐标中的权重 \(e^{3r}\) 都是正确的。
2. 联合搜索脚本确实固定反射中心值与一阶法向导数，并在所选 Fourier 空间内精确固定投影后的 Koiso 二阶喷流；它也计算了该对角 OT 度量中全部五个非恒零正交分量。
3. 实际使用的中心度量是 \(K_z=4\) Fourier 截断，不再严格满足 \(R=-6\)；Koiso 喷流又被单独投影。因此“严格 scalar-minus-six 中心”并未在离散模型中实现。残差图册在 \(r=0\) 给出算子范数 \(1.097\times10^{-2}\)，直接显示这一点。
4. 联合改变 \(a,\sigma,v\) 在三个长度上都降低了算子范数的 RMS，但没有降低最大采样值。最大值持续位于物理半径 \(r\simeq0.2\)，并且联合变化主要把残差从轨道方程转移到 \(E_{zz}\)，而不是同时消除五个分量。
5. \(R=4,6\) 的良好外端数据大部分由载体的渐近形式预先保证：\(a_r\to1,\sigma_r\to2,v_r\to0\)，而切片曲率项被 \(e^{-2a}\) 红移。它说明外部段工作正常，但没有解决内层峰值。
6. 现有计算只覆盖对角 \(M=\operatorname{diag}(e^v,e^{-v})\)。完整 \(H^2\) 轨道映射的第二个自由度，即 Iwasawa 变量 \(\beta\) 或极坐标角变量 \(\psi\)，没有进入 Step 80。

---

## 二、基底恒等式与物理权重

令
\[
g=\gamma_B+G_{ab}d\xi^a d\xi^b,\qquad
G=e^\sigma M,\qquad \det M=1,
\]
并记 \(P_i=M^{-1}\nabla_iM\)。标准分块 Ricci 公式化为
\[
\operatorname{Ric}^g_{ij}
=\operatorname{Ric}^{\gamma_B}_{ij}
-\nabla_i\nabla_j\sigma
-\frac12\sigma_i\sigma_j
-\frac14\operatorname{tr}(P_iP_j).
\]
在
\[
\langle V,W\rangle_{H^2}
=\frac12\operatorname{tr}(M^{-1}VM^{-1}W)
\]
的归一化下，最后一项正是
\[
-\frac12(U^*h_{H^2})_{ij}.
\]
因此脚本使用的
\[
E_B=\operatorname{Ric}(\gamma_B)-\operatorname{Hess}\sigma
-\frac12d\sigma^2-\frac12U^*h_{H^2}+3\gamma_B
\]
系数无误。

对角情形 \(M=\operatorname{diag}(e^v,e^{-v})\) 给出
\[
U^*h_{H^2}=dv\otimes dv.
\]
冻结尖点
\[
\gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r+\sigma_0
\]
中，不含 \(v\) 的各项恰好相消，故
\[
E_{rr}=-\frac12v_r^2,\quad
E_{rz}=-\frac12e^{-r}v_rv_z,\quad
E_{zz}=-\frac12e^{-2r}v_z^2
\]
均指正交标架分量，与 JSON 一致。

轨道无迹方程为
\[
\partial_r(e^{a+\sigma}v_r)
+\partial_z(e^{\sigma-a}v_z)
=-e^{a+\sigma}(E_x-E_y).
\]
代入 \(a=r,\sigma=2r+\sigma_0\)：
\[
\partial_r(e^{3r}v_r)+\partial_z(e^rv_z)
=-e^{3r}(E_x-E_y),
\]
其中整体常数 \(e^{\sigma_0}\) 已约去。在共形坐标
\(t=-e^{-r}\) 中，
\[
e^{2\lambda}\rho\,dt
=e^{2r}e^{2r}e^{-r}dr=e^{3r}dr,
\]
所以物理测度修正确实是 \(e^{3r}dr\,dz\)。

常数晶格缩放 \(G\mapsto N^{-2}G\) 使
\(\sigma\mapsto\sigma-2\log N\)，而 \(M\) 与轨道映射能量不变；通量和源测度同时乘以 \(N^{-2}\)。

---

## 三、中心数据、Koiso 喷流和五个 Ricci 分量

中心原始数据为
\[
a_0=2\log u,\qquad \sigma_0=4\log u,\qquad
v_0=2\sin z,
\]
其中
\[
u''=\frac34u^5-\frac14\cos^2z\,u.
\]
这对应
\[
q_0=u^4\bigl(dz^2+e^{2\sin z}dx^2+e^{-2\sin z}dy^2\bigr),
\]
符号与 Step 75 的 Yamabe 方程一致。

但脚本随后执行
\[
(a_0,\sigma_0,v_0)\longmapsto P_{K_z=4}(a_0,\sigma_0,v_0).
\]
内在 Ricci 是从这个截断中心重新计算的，再将 Koiso 数据
\[
J_2=
\bigl(\operatorname{Ric}_a+3,\,
\operatorname{Ric}_b+\operatorname{Ric}_c+6,\,
\operatorname{Ric}_b-\operatorname{Ric}_c\bigr)
\]
再次投影到相同 Fourier 空间。由载体和自由基函数在 \(r=0\) 的阶数可直接得到
\[
L_r(0,z)=0,\qquad L_{rr}(0,z)=P_{K_z=4}J_2(z).
\]
所以反射和“投影 Koiso 二阶喷流”在离散表示内确实精确；它们不等于未投影中心的精确几何喷流。

图册在所有六组解的中心都给出
\[
\|E\|_{\mathrm{op,grid}}=0.0109700,\quad
\|E_{zz}\|_\infty=0.0029583,\quad
\|E_{rr}\|_\infty=6.94\times10^{-5}.
\]
这不是优化产生的，因为所有自由模式在中心消失；它来自 Fourier 截断与 Ricci 喷流再次投影。

对于 \(l=(a,b,c)\)，代码中的切向公式可统一写成
\[
E_i=3+\operatorname{Ric}(q_r)_i-l_i''-Hl_i',
\qquad H=a_r+b_r+c_r,
\]
而
\[
E_{rr}=3-\sum_i\bigl(l_i''+(l_i')^2\bigr).
\]
`E1` 是正交标架中的 \(E_{rz}\)，目标函数给它乘 \(\sqrt2\)，正好对应对称张量 Frobenius 权重。`exact_op` 对基底 \(2\times2\) 块取精确特征值，再与 \(E_x,E_y\) 比较。对角 OT 类中其余 Ricci 分量恒为零，因此五分量计算是完整的。

---

## 四、配对运行究竟显示了什么

采样结果为：

| \(R\) | 模型 | 最大值 | RMS | q95 |
|---|---|---:|---:|---:|
| 2 | shape-only | 14.629 | 4.362 | 9.793 |
| 2 | joint | 15.363 | 3.890 | 9.989 |
| 4 | shape-only | 14.867 | 3.599 | 7.974 |
| 4 | joint | 15.047 | 3.290 | 7.350 |
| 6 | shape-only | 14.914 | 3.604 | 7.988 |
| 6 | joint | 15.028 | 3.373 | 7.596 |

因此联合基底/面积响应：

- 在三个 \(R\) 上都减少了 RMS；
- 在 \(R=4,6\) 上也减少 q95；
- 在三个 \(R\) 上都略微增大最大采样值。

\(R=4\)、\(r=0.2\) 的分量最能说明残差转移：

- shape-only：
  \[
  \|E\|_{\rm op}=14.867,\quad
  |E_{zz}|_{\max}=9.373,\quad |E_{rz}|_{\max}=2.243;
  \]
- joint：
  \[
  \|E\|_{\rm op}=15.047,\quad
  |E_{zz}|_{\max}=15.047,\quad |E_{rz}|_{\max}=0.688.
  \]

联合变化显著减小交叉分量，却使峰值由 \(E_{zz}\) 主导。到 \(r=0.4\)，联合值已经由 shape-only 的 \(4.871\) 降至 \(3.030\)。这表明基底自由度能改善峰值外侧的平均响应，但当前参数化没有完成最内层的同步抵消。

外端改善非常明显，例如 \(R=6\)：

\[
\begin{array}{c|cc}
&\|S-I\|_\infty&\|\operatorname{Ric}(q_R)\|_\infty\\ \hline
\text{shape-only}&0.00623&3.98\times10^{-4}\\
\text{joint}&0.00994&5.11\times10^{-4}.
\end{array}
\]

不过载体本身满足
\[
\log\cosh r=r-\log2+O(e^{-2r}),\qquad C'(r),C''(r)\to0,
\]
故这些外端量随 \(R\) 改善是结构上预置的。增加长外部段没有改变 \(r\simeq0.2\) 的峰值。

`base_response_needed` 只比较两个全局最大值：轨道应力最大值与总残差最大值通常位于不同 \((r,z)\)，因此该布尔量没有点态几何含义。真正的抵消账目应逐点分解为
\[
\mathcal C_B
=\operatorname{Ric}(\gamma_B)-\operatorname{Hess}\sigma
-\frac12d\sigma^2+3\gamma_B,\qquad
\mathcal T_B=\frac12dv\otimes dv,
\]
再比较 \(E_B=\mathcal C_B-\mathcal T_B\) 的特征方向和 Fourier 模式。现有 JSON 没有保存这组分解。

---

## 五、会显著收窄数值含义的因素

### 1. 固定载体很可能参与制造 \(r\simeq0.2\) 层

载体
\[
C(r)=\frac12\ell^2(1-e^{-(r/\ell)^2})
\]
满足
\[
C^{(4)}(0)=-\frac6{\ell^2}.
\]
在 \((a,\sigma,v)\) 变量中，未计自由修正时的四阶喷流为
\[
(-2,-4,0)-\frac6{\ell^2}\bigl(J_2-(1,2,0)\bigr).
\]
当 \(\ell\) 较小时，这是很强的四阶弯折。自由模式从 \(r^4\) 开始，理论上可以修正它，但输出没有记录拟合后的四阶喷流。载体参数只在零系数族中预选，之后没有与全部系数共同变化。

### 2. 目标函数不是最大范数

核心目标是按 \(dr\,dz\) 加权的 Frobenius \(L^2\)，并且径向权重除以 \(R\)。固定宽度的内层在 \(R\) 增大时只占 \(O(R^{-1})\) 的目标权重。因此 RMS 改善与峰值不动完全相容，也解释了联合解把误差集中到较窄的 \(E_{zz}\) 层。

该目标也没有使用物理权重 \(e^{a+\sigma}\)。这不影响点态 Ricci 的定义，却意味着它没有直接检验“小 \(E_x-E_y\) 经巨大物理测度累计成有限轨道源”的机制。

### 3. 所有运行都在函数评估上限处终止

每次两阶段求解都用了全部 85 次评估。若干联合运行的一阶最优量仍为 \(0.038\)、\(0.095\)、\(0.152\)。这些点不是已确认的驻点；单一零初值也没有检验其他局部极小点。

### 4. 最大值只在训练节点上计算

Pilot 使用 \(K_z=4,N_z=24,N_r=29\)。日志变量只有低 Fourier 模式，但指数和 Ricci 非线性产生更高谐波；径向 Gaussian 局部模式也可能在节点之间形成尖峰。脚本具备 refine 模式，但所给材料没有相应结果。现有“operator_sup”是采样最大值，连续最大值至少不小于它。

### 5. 各个 \(R\) 的函数空间不是嵌套序列

全局径向模式使用 \(s=r/R\)，因此改变 \(R\) 同时改变基函数。内层 Gaussian 模式保持物理尺度不变，所以三个长度得到几乎相同的 \(r\simeq0.2\) 轮廓并不意外，不能单独产生一个与函数空间无关的几何结论。

### 6. 完整 OT 轨道角自由度未测试

Step 80 只含一个 \(H^2\) 坐标 \(v\)。Step 79 所讨论的角动量重新分配需要第二个轨道形状变量。当前结果只说明“对角轨道形状加基底/面积响应”的有限模式表现。

---

## 六、最有信息量的内层测试

最直接的解析对象是精确四阶 Koiso 喷流。写
\[
l_i(r,z)=l_i^0(z)+\frac12p_i(z)r^2+\frac1{24}w_i(z)r^4+O(r^6),
\qquad i=a,b,c,
\]
其中
\[
p_i=\operatorname{Ric}(q_0)_i+3.
\]
将切向 Einstein 方程展开到 \(r^2\) 得
\[
\boxed{
w_i=\bigl(D\operatorname{Ric}_{q_0}[p]\bigr)_i-6p_i.
}
\]
法向方程给出相容恒等式
\[
\sum_iw_i=-2\sum_ip_i^2.
\]
其原因是 \(R(q_0)=-6\)、\(\sum p_i=3\)，而沿度量变化
\(\dot q=2p^\flat\) 有
\[
\dot R=36-2|\operatorname{Ric}|^2.
\]
动量分量的 \(O(r)\) 项由收缩 Bianchi 恒等式消失。单独 Fourier 投影 \(p_i\) 会破坏这一点，因此也能解释某些早期 \(E_{rz}\) 增长。

由此得到一个高度区分性的有限模式实验：

- 只取 \(0\le r\le r_*\)，其中 \(r_*\约0.6\!-\!1\)，不再把已工作的长外部段放入同一平均目标；
- 用更高 Fourier 分辨率表示中心、\(p_i\) 和上述 \(w_i\)，使中心标量、动量相容式及四阶喷流同时达到谱精度；
- 后续自由模式从 \(r^6\) 开始，并采用支撑在内层的分片 Chebyshev 或 B-spline，而不是由单一 \(C(r)\) 决定转折尺度；
- 对五个分量求局部线性极小化
  \[
  \mu(\eta)=
  \min_{\|\delta L\|\le\eta}
  \max_{\text{加密节点},\,A}
  |E_A+D E_A[\delta L]|,
  \]
  其中 \(\delta L=(\delta a,\delta\sigma,\delta v)\) 支撑在内层。该线性问题能直接量化 shape-only 残差中有多少位于基底/面积响应的像空间内；
- 同时保存 \(\mathcal C_B\)、\(\mathcal T_B\) 的逐点分解，以及物理轨道通量
  \[
  \Phi(r)=\int_{S^1}e^{a+\sigma}v_r\,dz,\qquad
  \Phi'(r)=-\int_{S^1}e^{a+\sigma}(E_x-E_y)\,dz.
  \]

这一测试把三种来源分开：中心投影误差、载体四阶弯折、以及五个 Einstein 分量之间真正的耦合。加入第二个轨道变量 \(\beta\) 后重复同一内层像空间计算，还可精确衡量 Step 79 的完整 \(H^2\) 机制是否提供了对角模型中不存在的补偿方向。现有 Step 80 数据本身仍是有限维 pilot 证据，不产生存在性或不可存在性定理。