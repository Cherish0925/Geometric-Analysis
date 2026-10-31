# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 3,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/o11_cell_einstein_shadow.py",
    "Sessions/S1003A02/workspace/data/o11_cell_einstein_shadow.json",
    "Sessions/S1003A02/workspace/figures/o11_cell_einstein_shadow.png",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json",
    "Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md"
  ]
}
```

## Task

Critically read the empirical comparison between the certified X=8 subthreshold cell and the Einstein bolt flow. The profile reconstructs geodesic state, estimates a bolt anisotropy d_fit≈-0.462, and shows the same-bolt Einstein trajectory becomes singular at t≈0.297 while 99% of the positive P action of the cell is accumulated by t≈0.319 (90% by t≈0.150). State what scientific conclusion about the 'shadow Einstein separatrix then pay a late CR layer' picture is warranted. Check slot/sign conventions and whether d_fit instability invalidates the comparison. Relate this to the exact control-action identity shared by the peer: P/(8π²)=∫Σ λ_i/4 (u_i'−2H_i/λ_i)^2 dt. Suggest the strongest next mathematical object this evidence supports: local bolt action/calibration, compactness contradiction, or another formulation.

## Output

## 科学核验备忘

### 1. 这组数据不支持“先长期贴着 Einstein 分离轨道，再在外端支付 CR 修正代价”

最稳固的数值事实来自正定恒等式所给出的累计作用量：

\[
\frac{P(T)}{8\pi^2}
=\int_0^T\sum_i\frac{\lambda_i}{4}
\left(u_i'-\frac{2H_i}{\lambda_i}\right)^2dt .
\]

记录显示：

\[
\begin{array}{c|c}
P(T)/P_{\rm tot}&T\\ \hline
0.50&0.0649\\
0.75&0.1009\\
0.90&0.1496\\
0.99&0.3191
\end{array}
\qquad
t_{\rm outer}=1.7547 .
\]

因此，外段 \(0.319<t<1.755\) 只承载约 \(1\%\) 的正定 \(P\)-作用量。无论如何解释 Einstein 射线，代价都不是主要发生在靠近 \(X=8\) 的 CR 匹配层；它集中在 bolt 附近的核心区域，而且 \(90\%\) 已在 \(t\simeq0.15\) 前支付。

更符合数据的几何图像是：

> 该 cell 在核心区用 Ricci-tracefree 控制把状态从一个走向奇异区的 Ric\(=-6\) 参考流附近移开；随后很长的外段只需很小的附加作用量，就能到达标准 CH 延拓数据。

这还不能说明外段贴着哪一条精确 Einstein 轨道。小的积分作用量也不等同于逐点残差很小，但它明确排除了“主要代价位于晚期外端层”的版本。

相空间距离同样没有显示持续跟踪同一参考轨道：

\[
\begin{array}{c|cc}
t&\|\log(a/a_E)\|&\|y-y_E\|\\ \hline
0.0204&0.0385&3.59\\
0.0501&0.1889&5.97\\
0.1000&0.4841&5.54\\
0.2001&0.9274&3.77
\end{array}
\]

近 bolt 时两个 ACH deviation 都很大，主要因为 \(\kappa_2\sim t^{-1}\)；它们数量级相似并不表示两条轨道接近。

---

### 2. 槽位与 \(d\) 的符号是一致的

重构使用

\[
(a_1,a_2,a_3)
=\left(\sqrt{x},\sqrt{x e^w},\sqrt F\right).
\]

所以：

- \(a_3\) 在 bolt 塌缩，bolt fibre 是 slot \(3\)；
- 在 CH 接合端，
  \[
  (a_1,a_2,a_3)
  =\left(\sqrt x,\sqrt{x(1+x)},\sqrt x\right),
  \]
  故 CH 的快增长/Kähler 槽是 slot \(2\)；
- `ach2` 中
  \[
  \kappa_2=\frac{a_2}{a_3a_1},\qquad
  \rho_2=\frac{a_3}{a_1},
  \]
  与这个排列完全相符。

bolt 附近 \(w>0\)，于是 \(a_2>a_1\)，从而

\[
a_1-a_2=d\,t^4+\cdots,\qquad d<0.
\]

交换 \(a_1\leftrightarrow a_2\) 会把 \(d\) 变为 \(-d\)，同时交换 ACH\(_1\) 与 ACH\(_2\) 分支。因此这里的 \(d<0\) 正是 slot \(2\) 分支，不存在隐含的槽位反转。

---

### 3. \(d_{\rm fit}\) 的多项式系数很大，但四阶系数本身可直接由存储参数求出

令

\[
Q_F=\sum_{m=0}^{7}c_{F,m}(-1)^m,\qquad
C_w=\sum_{m=0}^{7}c_{w,m}(-1)^m,\qquad
\ell=\log(X/x_0).
\]

由 `cG` 的平移定义，

\[
Q_G=-Q_F.
\]

本记录给出

\[
Q_F=-0.03163478253,\qquad
C_w=0.03876429000,\qquad
A=e^{Q_G}=1.03214048.
\]

在 bolt 附近，

\[
x-x_0=A t^2+O(t^4),
\]

而 `smooth(u)=O(u^3)`，故 \(w\) 的四阶项完全来自 `wr`：

\[
w=\frac{C_wA^2}{x_0^2\ell^2}t^4+O(t^6).
\]

于是

\[
a_1-a_2
=\sqrt{x}\left(1-e^{w/2}\right)
=-\frac{bC_wA^2}{2x_0^2\ell^2}t^4+O(t^6),
\]

即

\[
d_{\rm jet}
=-\frac{bC_wA^2}{2x_0^2\ell^2}
\simeq -0.4621.
\]

这与拟合值 \(-0.462267\) 相差约 \(1.8\times10^{-4}\)，相对差约 \(4\times10^{-4}\)。因此拟合中的

\[
-1144\,t^2+2.87\times10^5\,t^4
\]

反映了有限拟合窗口内较高阶项的自然尺度，并未改变四阶分支及符号。对于固定记录，\(d\) 可以用上面的端点喷流公式代替外推拟合。

Einstein 流靠近分离结构时可能对 \(d\) 很敏感，所以精确的 \(t_s\simeq0.297\) 仍适合用 \(d_{\rm jet}\)、更高阶 bolt 展开和邻近 \(d\) 值确认；但核心作用量集中和早期相空间分离并不依赖这 \(10^{-4}\) 量级的差别。

---

### 4. “同一 bolt jet”并不准确：这里只匹配了 \(b,n,d\)，没有匹配完整喷流

由上面的展开，

\[
a_1=a_2=b+\frac{A}{2b}t^2+O(t^4),
\]

所以 cell 的共同二阶系数为

\[
p_{2,\rm cell}=q_{2,\rm cell}
=\frac{A}{2b}
=5.1607.
\]

而 Ric\(=-6\) 的 \(O(-1)\) Einstein bolt 展开给出

\[
p_{2,E}=q_{2,E}
=\frac{3b^2+2}{2b}
=10.15
\qquad (b=0.1).
\]

两者相差约 \(4.99\)。这也直接解释了为什么在 \(t\simeq0.02\) 时轴长仍较接近，而 \(y_i=a_i'/a_i\) 已有 \(O(1)\) 的差别。

因此脚本比较的是：

- 相同 bolt 半径 \(b\)；
- 相同 normal charge \(n=1\)；
- 相同四阶各向异性参数 \(d\)；
- 但 Einstein 方程重新指定了二阶及更高的各向同性系数。

它不是从 cell 的完整相空间状态启动的 Einstein 延拓。由此，奇异时间与 \(P\)-累计曲线的接近很有启发性，但尚不能视为“cell 先跟踪这条轨道，随后被控制推开”的直接动力学证明。

另一个相关点是：\(P\) 测量的是 \(\operatorname{Ric}^{\circ}\)，所有 Einstein 常数都使该密度为零。Ric\(=-6\) 是由 CH 外端归一化选出的水平。若建立纯 \(P\) 的局部控制理论，Einstein 常数应作为第一积分纳入；若使用 \(J\)，则附加的标量项把它固定到 CH 的归一化。

---

### 5. 图中 \(t>0.297\) 的橙色曲线不是 Einstein 解

输出为

```text
ein_status = -1
ein_tend   = 0.297137...
```

但代码仍执行

```python
Z = sol.sol(np.maximum(t,t0))
```

直至 \(t=1.7547\)。`solve_ivp` 的 dense interpolant 在最后积分时刻之外会继续作多项式外推。因此 \(t=0.4\) 后的 \(10^{105}\)、Infinity 和 NaN 没有几何意义，不能用作奇异爆破证据；有效比较只到 \(t\le0.297\)，表中最后一个有效采样点是 \(t\simeq0.200\)。

当前 JSON 记录的 `status=-1` 表示积分器在 \(t\simeq0.297\) 无法按指定精度继续推进。若要从这一个产物本身确认几何奇异，需要末端数据展示某些 \(a_i\) 塌缩或增长、\(y_i\) 或曲率发散，并记录 constraint 沿轨道保持的程度。Step 13 的其他 shooting 结果可为“奇异分支”提供背景，但这张图自身的外推段不能承担该结论。

这一作图问题不影响 cell 的累计 \(P\) 分布；后者完全由 cell 数据计算。

---

### 6. 与精确控制作用量恒等式的关系

定义

\[
K_i(a)=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
r_i=u_i'-\frac{2H_i}{\lambda_i}.
\]

则轨道可写成受控一阶系统

\[
a_i'=u_i+K_i(a),\qquad
u_i'=\frac{2H_i}{\lambda_i}+r_i,
\]

且

\[
\frac{P}{8\pi^2}
=\int \frac14\sum_i\lambda_i r_i^2\,dt.
\]

所以这里的数值结果有一个很清楚的控制论含义：该 cell 的控制 \(r\) 主要作用于 bolt 核心及 Ric\(=-6\) 参考流即将终止的时间窗，而不是外端 CR 匹配区。

不过，“零控制轨道走向奇异”本身并不推出正的最小作用量。一个不稳定流可以被很小的加权 \(L^2\) 控制产生有限位移；而在 bolt 处

\[
\lambda_1,\lambda_2\sim t,\qquad
\lambda_3\sim \frac{b^2}{t},
\]

控制度量本身高度各向异性。正下界必须来自一个定量的轨道分离估计，而不是仅由 Einstein 解不存在得到。

---

### 7. 最自然且最强的下一数学对象：bolt-to-escape 加权作用值及其 calibration

这组证据最直接支持的对象不是全局紧性反证，而是一个局部最优控制值：

\[
\mathcal I_{\rm core}(b,d;\Sigma_{\rm CH})
=
\inf
\left\{
\int_0^\tau
\frac14\sum_i\lambda_i r_i^2\,dt:
\begin{array}{l}
z(t)=(a(t),u(t))\text{ 有正则 }O(-1)\text{ bolt 渐近},\\
z(\tau)\in\Sigma_{\rm CH}
\end{array}
\right\}.
\]

这里 \(\Sigma_{\rm CH}\) 可取为一个位于 \(t\approx0.3\) 的横截面，其状态能够以很小附加作用量延拓到标准 CH collar。bolt 的奇异坐标可通过从 \(t=\varepsilon\) 开始并令 \(\varepsilon\downarrow0\) 处理。

定量下界对应一个状态函数 \(\Phi(a,u)\)，满足 Hamilton–Jacobi 型不等式

\[
F\cdot\nabla\Phi
+\sum_i\frac{(\partial_{u_i}\Phi)^2}{\lambda_i}
\le 0,
\]

其中

\[
F(a,u)=
\left(
u_i+K_i(a),\,
\frac{2H_i}{\lambda_i}
\right).
\]

由 Young 不等式，

\[
\frac{d}{dt}\Phi(z(t))
\le
\frac14\sum_i\lambda_i r_i^2,
\]

从而

\[
\frac{P}{8\pi^2}
\ge
\Phi(z(\tau))-\Phi(z(0)).
\]

一个可计算的局部候选可由奇异 Einstein 轨道的线性化不稳定协向量或伴随方程构造；其加权 controllability Gramian 给出二次近似的最小逃逸作用量。这比单纯比较两条数值曲线更接近可证明的正下界，也能区分：

1. cell 与 Ric\(=-6\) Einstein 二阶喷流的初始差别；
2. 避开奇异区所需的控制；
3. 进入 CH 导向状态后剩余的外端代价。

紧性反证可在此后使用：若小作用量序列在固定核心区给出足够的一致状态控制，它应收敛到零控制 Einstein 轨道；局部作用值的正性会阻止其穿过相应横截面。现有单个 \(b=0.1\) 轨道尚未提供对可变 \(b,d\)、Einstein 常数和退化权重的一致估计。

**综述：**槽位和 \(d\) 的符号正确，\(d\) 可由端点喷流稳定求得；真正显著的问题是完整二阶喷流并未匹配，以及 Einstein 曲线在积分终点后的部分只是外推。可靠的科学结论是“作用量主要是早期 bolt-core escape cost”，而不是“晚期 CR 修正 cost”。最有力的理论化对象是精确正定恒等式诱导的局部加权逃逸作用及其 Hamilton–Jacobi calibration。