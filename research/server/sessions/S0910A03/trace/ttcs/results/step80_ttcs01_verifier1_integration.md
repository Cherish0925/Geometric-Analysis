# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 80,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step80_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step80_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently read and assess the Step 80 joint reflected-core finite-mode experiment for the Yau 26 negative graph-manifold route. Check (i) the invariant base equation and physical-coordinate source/measure corrections; (ii) whether the script really enforces the scalar-minus-six reflected center and projected Koiso second jet and evaluates all five Ricci components; (iii) what the paired shape-only versus joint base/area runs actually establish about compensation, especially the persistent residual layer near physical r≈0.2 and the fact that exit data become favorable while sup residual does not; (iv) identify any formula, parameterization, optimization, sampling, or interpretation error that would invalidate or sharply narrow the result. Derive the most informative next finite-mode or analytic test aimed at the inner compensation layer rather than the already solved exterior tail. Treat all numerical failures as finite-dimensional evidence, not a theorem.

## Integrated Scientific Memo

# Step 80 核验结论

## 1. 不变量方程与物理坐标权重

对
\[
g=\gamma_B+e^\sigma M_{ab}d\xi^a d\xi^b,\qquad \det M=1,
\]
令
\[
\langle V,W\rangle_{H^2}
=\frac12\operatorname{tr}(M^{-1}VM^{-1}W).
\]
基底分量确为
\[
E_B:=\operatorname{Ric}_g|_B+3\gamma_B
=\operatorname{Ric}(\gamma_B)-\operatorname{Hess}\sigma
-\frac12d\sigma\otimes d\sigma-\frac12U^*h_{H^2}+3\gamma_B .
\]
`step80_base_identity_verify.py` 在
\[
\gamma_B=dr^2+e^{2a}dz^2,\qquad
M=\operatorname{diag}(e^v,e^{-v})
\]
下将三个正交分量逐项化简到直接 Ricci 公式，差均为零；系数与正交标架换算正确。

冻结圆尖点 \(a=r,\sigma=2r+\sigma_0\) 时，
\[
E_{rr}=-\frac12v_r^2,\qquad
E_{rz}=-\frac12e^{-r}v_rv_z,\qquad
E_{zz}=-\frac12e^{-2r}v_z^2.
\]
对角轨道无迹方程带缺陷时为
\[
\partial_r(e^{a+\sigma}v_r)+
\partial_z(e^{\sigma-a}v_z)
=-e^{a+\sigma}(E_x-E_y).
\]
因此冻结尖点上
\[
\partial_r(e^{3r}v_r)+\partial_z(e^rv_z)
=-e^{3r}(E_x-E_y).
\]
同样，从共形坐标 \(t=-e^{-r}\) 得
\[
e^{2\lambda}\rho\,dt=e^{2r}e^{2r}e^{-r}dr=e^{3r}dr.
\]
所以源和测度修正正确。需强调：\(e^{3r}\) 仅是冻结尾部 \(a=r,\sigma=2r+\mathrm{const}\) 的权重；一般内层权重是 \(e^{a+\sigma}\)，脚本并未用 \(e^{3r}\) 描述内层。

常数晶格缩放 \(G\mapsto N^{-2}G\) 确使
\(\sigma\mapsto\sigma-2\log N\)，而 \(M\) 和轨道映射能量不变。

---

## 2. 中心约束、Koiso 二阶喷流与五个分量

中心连续数据由
\[
a_0=2\log u,\quad \sigma_0=4\log u,\quad v_0=2\sin z,
\]
以及
\[
u''=\frac34u^5-\frac14\cos^2z\,u
\]
生成，符号与 Step 75 的 scalar-\(-6\) Yamabe 方程一致。

脚本随后将中心数据投影到 \(K_z=4\) Fourier 空间，再从截断中心计算切片 Ricci，并将
\[
J_2=
\left(
\operatorname{Ric}_a+3,\,
\operatorname{Ric}_b+\operatorname{Ric}_c+6,\,
\operatorname{Ric}_b-\operatorname{Ric}_c
\right)
\]
再次投影。由于
\[
C(0)=C'(0)=0,\quad C''(0)=1,
\]
且所有自由径向模式为 \(O(r^4)\)，脚本严格保证
\[
L(0)=P_{K_z}L_0,\qquad L_r(0)=0,\qquad
L_{rr}(0)=P_{K_z}J_2 .
\]
因此：

* 反射中心条件精确；
* **投影后的** Koiso 二阶喷流精确；
* 但实际离散中心不是严格 scalar-\(-6\) 中心。

后一点由图册直接显示：
\[
\|E(0)\|_{\rm op,grid}=1.0970\times10^{-2}.
\]
故脚本注释中的 “exact scalar-minus-six center” 若理解为计算中实际使用的截断场，是过强表述；准确说法是“来自精确中心的 Fourier 投影”。

`components()` 确实计算
\[
E_{rr},\ E_{rz},\ E_{zz},\ E_x,\ E_y
\]
五个正交分量。`E_rz` 中的 \(e^{-a}\) 是坐标到正交标架的正确因子；目标函数对它乘 \(\sqrt2\) 正是对称张量 Frobenius 权重。`exact_op` 对基底 \(2\times2\) 块取精确特征值，再与 \(E_x,E_y\) 比较。对这一对角 OT 类，其他混合 Ricci 分量恒零，所以五分量是该 ansatz 内完整的 Ricci 检验。

但该 ansatz 仅有
\[
M=\operatorname{diag}(e^v,e^{-v}),
\]
没有完整 \(H^2\) 轨道映射的第二个形状变量（例如 Iwasawa \(\beta\) 或极角 \(\psi\)）。因此 Step 79 所设想的角自由度重分配并未被测试。

---

## 3. 配对实验实际证明了什么

入口阶段的主要数据为

\[
\begin{array}{c|c|ccc}
R&\text{variant}&\|E\|_{\rm op,sup}&\mathrm{RMS}&q_{95}\\\hline
2&\text{shape}&14.629&4.362&9.793\\
2&\text{joint}&15.363&3.890&9.989\\
4&\text{shape}&14.867&3.599&7.974\\
4&\text{joint}&15.047&3.290&7.350\\
6&\text{shape}&14.914&3.604&7.988\\
6&\text{joint}&15.028&3.373&7.596
\end{array}
\]

由此只能得出：

1. 联合改变 \(a,\sigma,v\) 在所有 \(R\) 上降低了采样 RMS；
2. 在 \(R=4,6\) 上也降低了 \(q_{95}\)；
3. 但在所有 \(R\) 上都略微增大采样最大值；
4. 最大值稳定钉在物理半径 \(r\simeq0.2\)，与外端长度无关。

图册显示联合自由度改善了峰值外侧，但没有消除最内层。以 \(R=4\) 为例：

* \(r=0.2\)，shape-only：
  \[
  \|E\|_{\rm op}=14.867,\quad
  |E_{zz}|_{\max}=9.373,\quad |E_{rz}|_{\max}=2.243;
  \]
* joint：
  \[
  \|E\|_{\rm op}=15.047,\quad
  |E_{zz}|_{\max}=15.047,\quad |E_{rz}|_{\max}=0.688.
  \]

所以联合响应主要压低了交叉残差，却把误差集中到由 \(E_{zz}\) 主导的窄层。到 \(r=0.4\)，joint 已把算子值从 \(4.871\) 降到 \(3.030\)。这支持“基底/面积自由度具有局部补偿能力”，但不支持“已完成内层补偿”。

外端数据在 \(R=4,6\) 很好；例如 \(R=6\)：
\[
\begin{array}{c|cc}
&\|S-I\|_\infty&\|\operatorname{Ric}(q_R)\|_\infty\\\hline
\text{shape}&0.00623&3.98\times10^{-4}\\
\text{joint}&0.00994&5.11\times10^{-4}.
\end{array}
\]
不过这主要是载体结构预置的：
\[
\log\cosh r=r-\log2+O(e^{-2r}),\qquad C',C''\to0,
\]
并且切片曲率被 \(e^{-2a}\) 红移。增加 \(R\) 延长的是已工作的外部尾部，未改善固定尺度的 \(r\simeq0.2\) 转向层。最可靠的实验结论是：**当前有限模式中的瓶颈是内层，不是外部尾部。**

这仍不能推出内层补偿不存在。

---

## 4. 显著收窄实验含义的问题

### 4.1 高阶中心喷流没有匹配 Einstein 递推

中心值、反射一阶喷流和 Koiso 二阶喷流被固定，但四阶及更高喷流由 cosh/carrier 与自由基的拟合共同决定。载体
\[
C(r)=\frac12\ell^2(1-e^{-(r/\ell)^2})
\]
满足
\[
C^{(4)}(0)=-\frac6{\ell^2},
\]
会在较小 \(\ell\) 时施加强烈的四阶弯折。自由模式虽从 \(r^4\) 开始，形式上能改变四阶喷流，但所选载体尺度仅在零系数族中预选，并未与全部系数联合优化，也没有输出最终四阶喷流。

因此 \(r\simeq0.2\) 峰值可能混合了真实几何转向负担与错误高阶 germ；不能把它直接解释为补偿障碍。

### 4.2 优化目标不针对最大范数

优化的是按 \(dr\,dz\) 加权、再除以 \(R\) 的 Frobenius \(L^2\) 残差，不是算子最大范数。固定物理宽度的内层在目标中的相对权重随 \(R\) 为 \(O(R^{-1})\)。所以“RMS 下降而窄峰不动”正是该目标容易产生的结果。

目标也没有使用物理源权重 \(e^{a+\sigma}\)。这不影响点态 Ricci 计算，但它没有直接测试 Step 79 的核心累积机制：很小的轨道无迹缺陷在巨大物理权重下能否产生有限总源。

### 4.3 所有求解均未确认收敛

所有阶段都在
\[
\texttt{nfev}=85=\texttt{MAX\_NFEV}
\]
停止，信息为“maximum number of function evaluations exceeded”。部分 joint 最优性仍为 \(0.038,0.095,0.152\)。所以结果不是已验证的驻点，更不是给定有限空间的最优值；且只使用了单一零初值。

### 4.4 “sup”只是训练网格最大值

Pilot 仅用 \(K_z=4,N_z=24,N_r=29\)。指数非线性产生截断以上的 Fourier 谐波，局部 Gaussian 径向模式也可在节点间形成峰。所报 `operator_sup` 仅是采样最大值，连续最大值可能更大。给定材料中没有 refine 结果或独立加密网格重评估。

### 4.5 不同 \(R\) 的空间不嵌套

全局径向模式取 \(s=r/R\)，改变 \(R\) 同时改变函数空间。内层 Gaussian 模式则保持固定物理尺度。因此跨 \(R\) 的峰值稳定具有定位价值，但不能视为同一嵌套逼近序列的收敛证据。

### 4.6 补偿账本诊断无点态意义

`base_response_needed` 比较的是两个可能出现在不同 \((r,z)\) 的全局最大值：
\[
\sup\tfrac12|dv|^2\quad\text{与}\quad \sup|E|.
\]
该布尔量不能判断是否发生点态张量补偿。正确账本应保存
\[
\mathcal C_B=
\operatorname{Ric}(\gamma_B)-\operatorname{Hess}\sigma
-\frac12d\sigma^2+3\gamma_B,\qquad
\mathcal T_B=\frac12dv\otimes dv,
\]
并逐点、逐 Fourier 模式、逐特征方向比较
\[
E_B=\mathcal C_B-\mathcal T_B.
\]

---

## 5. 最有信息量的下一步：先消除内层 germ 污染

写反射偶展开
\[
l_i(r,z)=l_i^0(z)+\frac12p_i(z)r^2+
\frac1{24}w_i(z)r^4+O(r^6),\qquad i=a,b,c,
\]
其中
\[
p_i=\operatorname{Ric}(q_0)_i+3.
\]
由
\[
E_i=3+\operatorname{Ric}(q_r)_i-l_i''-Hl_i',
\qquad H=\sum_jl_j',
\]
比较 \(r^2\) 系数得到精确四阶递推
\[
\boxed{\;
w_i=\bigl(D\operatorname{Ric}_{q_0}[\,2p^\flat\,]\bigr)_i-6p_i,
\;}
\]
这里 \(D\operatorname{Ric}\) 的输入是实际切片度量变分
\(\partial_{r}^{\,2}q_r|_0=2p^\flat\)；若把 \(D\operatorname{Ric}[p]\) 记作已吸收此因子的约定，必须明确该约定。法向方程还要求
\[
\sum_iw_i=-2\sum_ip_i^2.
\]
动量方程的首个非平凡阶应由收缩 Bianchi 恒等式相容。继续展开可递推 \(L_6\)。

最有区分力的实验应为：

1. 只研究 \(0\le r\le r_*\)，取 \(r_*\approx0.6\!-\!1\)，不让长尾稀释内层目标；
2. 高精度表示连续 scalar-\(-6\) 中心及 \(L_2,L_4,L_6\)，并在投影后重新检查 Hamilton、momentum 与喷流相容式；
3. 以匹配到 \(r^6\) 的 Einstein germ 替换当前 carrier germ，后续自由模式从 \(r^8\) 开始；
4. 使用内层分片 Chebyshev/B-spline 和加密离线网格，直接压低五分量的点态算子范数，而非全区间平均 \(L^2\)；
5. 将 shape-only 残差在线性化算子
   \[
   D E_{(a,\sigma,v)}
   \]
   下投影到 \((\delta a,\delta\sigma)\) 的像空间，定量测量哪些内层模式可由基底/面积抵消，哪些属于兼容性余核；
6. 输出逐点 \(\mathcal C_B-\mathcal T_B\) 账本及物理通量
   \[
   \Phi(r)=\int_{S^1}e^{a+\sigma}v_r\,dz,\qquad
   \Phi'(r)=-\int_{S^1}e^{a+\sigma}(E_x-E_y)\,dz.
   \]

若匹配 \(L_4,L_6\) 后 \(r\simeq0.2\) 峰值按预期高阶消失，则现峰主要是 germ 截断伪影；若在分辨率、喷流阶数和优化收敛均提高后仍留下稳定的内层余核，才形成较强的有限维障碍证据。

最后应在相同内层测试中加入完整 \(H^2\) 的第二个轨道变量 \(\beta\)。否则所得结论始终只适用于对角 OT 子类，不能检验 Step 79 的角动量重分配机制。

**总评：** Ricci 公式、物理权重、投影 Koiso 二阶喷流和五分量评价均基本正确；“严格 scalar-\(-6\) 离散中心”不正确。数值明确定位了一个未解决的物理内层，并确认外尾不是当前瓶颈；它既未证明联合补偿成功，也未证明补偿不可能，更没有任何定理性非存在含义。