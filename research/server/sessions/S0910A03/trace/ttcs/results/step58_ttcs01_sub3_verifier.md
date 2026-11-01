# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A03/workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Independently verify the curvature all-p and Moser part of Step 58, distinct from the Step 39 defect ladder. Starting from the exact weighted curvature inequality K_p'+dissipation <= C p^N(1+r^-2+S^2 Y)K_p and the positive-slab bound S^2Y<=C Gamma^3/t, check the time-slab recurrence, correct use of z_p, all powers of S,t,H(0),Gamma, and the conclusion ||a F_T(t)||_infty <= C Gamma/t. Determine whether the displayed recurrence M_{3p/2} <= C S (L M_p)^(3/2) is actually justified by the available sup K_p and integrated gradient terms, including any missing square roots or time factors. State a corrected recurrence and endpoint if needed.

## Output

## Step 58 曲率 all-\(p\) 与 Moser 部分核对备忘录

只核对曲率量 \(F_T=(1+|T|^2)^{1/2}\)、\(K_p\)、\(Y\) 与 Moser 迭代；不使用 Step 39 的 defect ladder。

### 1. 权重与 \(z_p\) 的使用是正确的

Step 58 对 \(p\ge3\) 定义
\[
K_p=\int \eta^2 a^{p-2}F^p,\qquad 
z_p=\eta a^{(p-1)/2}F^{p/2}.
\]
由于 \(\eta=1\) 在 \(\operatorname{supp}a\) 上，且 \(p\ge3\) 时 \(a^{p-2}\) 在 \(a=0\) 处消失，所以在曲率 Moser 段中
\[
K_{2p}=\int a^{2p-2}F^{2p}=\|z_p\|_4^4
\]
是成立的。插值式也正确：
\[
K_{3p/2}
=\int a^{3p/2-2}F^{3p/2}
\le K_p^{1/2}K_{2p}^{1/2}.
\]
指数核算为
\[
\frac{p-2}{2}+\frac{2p-2}{2}=\frac{3p}{2}-2,\qquad
\frac p2+p=\frac{3p}{2}.
\]

特别地，\(p=3\) 时
\[
z_3=\eta aF^{3/2},\qquad z_3^2=\eta^2a^2F^3,
\]
这正好匹配 \(K_3\) 方程中的 \(a^2\)-加权耗散。旧变量 \(\eta a^{1/2}F^{3/2}\) 的梯度只给 \(a\)-权重，不能接到 \(p=3\) 的曲率耗散上。Step 58 在这里的修正是必要且正确的。

---

### 2. 正时间 slab 上的能量输入

从给定曲率 all-\(p\) 不等式
\[
K_p'
+c\{pD_p^T+p(p-2)D_p^F\}
\le Cp^N(1+r^{-2}+\mathcal S^2Y)K_p
\tag{2.1}
\]
和 Step 58 的正时间估计
\[
\mathcal S^2Y(s)\le \frac{C\Gamma^3}{t},
\qquad s\in [t/2,t],
\tag{2.2}
\]
取
\[
I_j=[\tau_j,t],\qquad 
\tau_j=t(1-2^{-(j+1)}),\qquad 
p_j=3(3/2)^j.
\]

令 \(\zeta_j\) 为时间截断，\(\zeta_j=0\) 近 \(\tau_j\)，\(\zeta_j=1\) 在 \(I_{j+1}\)，并取
\[
|\zeta_j'|\le C\,4^j/t
\]
这个较粗但可用的估计。由 (2.1) 得
\[
\sup_{I_{j+1}}K_{p_j}
+\int_{I_{j+1}}\{p_jD_{p_j}^T+p_j(p_j-2)D_{p_j}^F\}
\le A_j\,\mathcal M_{p_j,j},
\tag{2.3}
\]
其中
\[
\mathcal M_{p,j}:=\int_{I_j}K_p(s)\,ds,
\]
且可取
\[
A_j
=Cp_j^N\left(\frac{4^j}{t}+1+r^{-2}+\frac{\Gamma^3}{t}\right).
\tag{2.4}
\]

梯度变量满足
\[
\|\nabla z_p\|_2^2
\le Cp^2(D_p^T+D_p^F+r^{-2}K_p).
\tag{2.5}
\]
结合 (2.3)，可将系数放大为
\[
L_j
=Cp_j^{N+2}\left(\frac{4^j}{t}+1+r^{-2}+\frac{\Gamma^3}{t}\right)
\tag{2.6}
\]
并得到
\[
\boxed{
\sup_{I_{j+1}}K_{p_j}
+\int_{I_{j+1}}\|\nabla z_{p_j}\|_2^2
\le L_j\,\mathcal M_{p_j,j}.}
\tag{2.7}
\]

如果沿用 Step 58 的简化式
\[
L_j\le Cp_j^{N+2}4^j(t^{-1}+r^{-2}),
\]
则这里已经把 \(1\)、\(\Gamma^3/t\) 吸收到常数中。这需要正在使用的 first-exit 上界 \(\Gamma\le \Gamma_*\)，以及 \(t\le r^2\le1\)。若不作这个吸收，应保留 (2.6)。

---

### 3. Moser recurrence 的精确形式

每个时间片上有
\[
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}.
\tag{3.1}
\]
而 Sobolev 给出的是
\[
K_{2p}^{1/2}
=\|z_p\|_4^2
\le \mathcal S\bigl(\|\nabla z_p\|_2^2+r^{-2}\|z_p\|_2^2\bigr)
\le \mathcal S\bigl(\|\nabla z_p\|_2^2+r^{-2}K_p\bigr).
\tag{3.2}
\]
因此
\[
\begin{aligned}
\mathcal M_{3p/2,j+1}
&=\int_{I_{j+1}}K_{3p/2}\\
&\le 
\bigl(\sup_{I_{j+1}}K_p\bigr)^{1/2}
\int_{I_{j+1}}K_{2p}^{1/2}\\
&\le 
\mathcal S
\bigl(\sup_{I_{j+1}}K_p\bigr)^{1/2}
\left(
\int_{I_{j+1}}\|\nabla z_p\|_2^2
+r^{-2}\int_{I_{j+1}}K_p
\right).
\end{aligned}
\tag{3.3}
\]

代入 (2.7) 得到更精确的 recurrence：
\[
\boxed{
\mathcal M_{3p/2,j+1}
\le
C\mathcal S\,(L_j\mathcal M_{p,j})^{1/2}
(L_j+r^{-2})\mathcal M_{p,j}.}
\tag{3.4}
\]
若 \(L_j\) 已按 (2.6) 放大，使 \(L_j\ge r^{-2}\)，则 (3.4) 化为
\[
\boxed{
\mathcal M_{3p/2,j+1}
\le C\mathcal S\,(L_j\mathcal M_{p,j})^{3/2}.}
\tag{3.5}
\]

所以 Step 58 显示的
\[
\mathcal M_{p_{j+1},j+1}
\le C\mathcal S\bigl(L_j\mathcal M_{p_j,j}\bigr)^{3/2}
\tag{3.6}
\]
是可推出的，但要把 \(L_j\) 理解为已经同时支配时间截断项、反应项、\(\|\nabla z_p\|_2\) 转换中的 \(p\)-损耗，以及 Sobolev 中的 \(r^{-2}K_p\) 项。

这里没有少一个平方根；关键是使用
\[
\int K_{2p}^{1/2},
\]
而不是 \(\int K_{2p}\)。每一步只引入一个 Sobolev 因子 \(\mathcal S\)。

---

### 4. 指数与端点核算

设
\[
m_j:=\mathcal M_{p_j,j}^{1/p_j},\qquad p_{j+1}=\frac32p_j.
\]
由 (3.5) 得
\[
m_{j+1}
\le
(C\mathcal S)^{2/(3p_j)}
L_j^{1/p_j}
m_j.
\tag{4.1}
\]

由于
\[
p_j=3(3/2)^j,\qquad
\sum_{j=0}^\infty \frac1{p_j}=1,
\]
并且
\[
\sum_j\frac{j+\log p_j}{p_j}<\infty,
\]
所有 \(p_j^{N+2}\) 与 \(4^j\) 的乘积只改变常数。保留主参数，得到
\[
m_\infty
\le
C\mathcal S^{2/3}
\left(1+r^{-2}+\frac{1+\Gamma^3}{t}\right)
\mathcal M_{3,0}^{1/3}.
\tag{4.2}
\]

Step 58 的 seed 是
\[
\mathcal M_{3,0}
=\int_{t/2}^tY(s)\,ds
\le C\Gamma H(0).
\tag{4.3}
\]
因此一般形式为
\[
\boxed{
\|aF_T(t)\|_\infty
\le
C\mathcal S^{2/3}
\left(1+r^{-2}+\frac{1+\Gamma^3}{t}\right)
\bigl(\Gamma H(0)\bigr)^{1/3}.}
\tag{4.4}
\]

在 Step 58 使用的 first-exit 场景中，\(\Gamma\le\Gamma_*\)，\(t\le r^2\le1\)，于是
\[
1+r^{-2}+\frac{1+\Gamma^3}{t}\le \frac{C}{t}.
\]
于是
\[
\|aF_T(t)\|_\infty
\le
\frac{C}{t}\,
\mathcal S^{2/3}
\bigl(\Gamma H(0)\bigr)^{1/3}.
\tag{4.5}
\]
若 \(\Gamma\) 与 \(\mathcal S H(0)^{1/2}\) 可比较，或至少
\[
\mathcal S H(0)^{1/2}\le C\Gamma,
\]
则
\[
\mathcal S^{2/3}\bigl(\Gamma H(0)\bigr)^{1/3}
=
\Gamma^{1/3}\bigl(\mathcal S H(0)^{1/2}\bigr)^{2/3}
\le C\Gamma.
\]
因此
\[
\boxed{
\|aF_T(t)\|_\infty\le \frac{C\Gamma}{t}.}
\tag{4.6}
\]

若不把 \(\Gamma^3/t\) 吸收到常数中，则端点自然读作
\[
\|aF_T(t)\|_\infty
\le
C(1+\Gamma^3)\frac{\Gamma}{t}
\]
在 \(t\le r^2\le1\) 下成立。Step 58 的 displayed endpoint 对应的是 \(\Gamma\) 已由 first-exit 小参数控制的版本。

---

### 5. 核对结论

- \(z_p=\eta a^{(p-1)/2}F^{p/2}\) 的使用正确；\(p=3\) 时必须是 \(z_3=\eta aF^{3/2}\)。
- \(K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}\) 与 \(K_{2p}^{1/2}=\|z_p\|_4^2\) 的组合给出一个 \(\mathcal S\) 因子，不是 \(\mathcal S^2\)。
- Step 58 的 recurrence
  \[
  \mathcal M_{p_{j+1},j+1}
  \le C\mathcal S(L_j\mathcal M_{p_j,j})^{3/2}
  \]
  可由已有的 \(\sup K_p\) 与 \(\int\|\nabla z_p\|_2^2\) 推出，但 \(L_j\) 必须包含 Sobolev 的 \(r^{-2}\) 项；未放大 \(L_j\) 时应写成 (3.4)。
- 端点幂次核算正确：
  \[
  \mathcal S^{2/3}(\Gamma H(0))^{1/3}
  \sim \Gamma,
  \]
  所以在 Step 58 的 first-exit 小参数环境下确实得到
  \[
  \|aF_T(t)\|_\infty\le C\Gamma/t.
  \]
- 此曲率分支不使用 \(Y(0)\)，也不调用 defect ladder；种子完全来自 \(\int_{t/2}^tY\le C\Gamma H(0)\)。