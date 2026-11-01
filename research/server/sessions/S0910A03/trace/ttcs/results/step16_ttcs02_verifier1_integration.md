# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 16,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs02_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step16_ttcs02_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently scrutinize the proposed coupled transition-inclusive cutoff-flow estimate for a=chi^2: can one plausibly prove persistence of local normalized L2 curvature energy and global L2 Einstein defect using only initial |Ric+g|<=delta, local normalized ∫|Rm|² small at all centers on a support of fixed multiple of r, a relative Sobolev inequality, and controlled cutoff derivatives? Derive or inspect the full curvature evolution under ∂_t g=-2a(Ric+g), especially terms involving derivatives of a and E. Determine whether terms like ∇²a*E*Rm and ∇a*∇E*Rm close with available dissipation, whether higher cutoff derivatives or unweighted ∇E outside a>0 cause singular losses near chi=0, and what exact coupled inequalities would suffice for continuation and metric equivalence. Do not merely repeat the schematic system; identify a valid energy architecture or a specific mathematical obstruction/new assumption.

## Integrated Scientific Memo

## 核验结论

对
\[
\partial_tg=-2aE,\qquad E=\Ric+g,\qquad a=\chi^2
\]
而言，过渡区项在**形式 \(L^2\) 能量层面没有内禀的 \(1/\chi\) 奇性**；正确结构是把曲率能量与 Einstein 缺陷能量耦合起来。然而，题设列出的初始条件本身尚不足以形成无循环的延拓定理：还缺少沿流 Sobolev 常数、固定 cutoff 的协变 Hessian，以及用于度量等价的加权点态缺陷控制。尤其不能以“抛物有限传播速度”把过渡环带从 plateau 计算中删去。

---

## 1. 完整的曲率演化结构

由 Wang 给出的局部 Ricci 流公式，加上变分 \(-2ag\)，可写成
\[
\partial_tR_{ijkl}
=a\,\mathcal N_{ijkl}(\Rm)+\mathcal D_a(E)_{ijkl},
\]
其中
\[
\begin{aligned}
\mathcal N_{ijkl}={}&
\Delta R_{ijkl}
+R_{ijpq}R_{pqkl}
+2R_{ipkq}R_{jplq}
-2R_{iplq}R_{jpkq}\\
&-\bigl(
R_{ip}R_{pjkl}+R_{jp}R_{ipkl}
+R_{kp}R_{ijpl}+R_{lp}R_{ijkp}
\bigr)-2R_{ijkl},
\end{aligned}
\]
而
\[
\begin{aligned}
\mathcal D_a(E)_{ijkl}={}&-
\bigl(a_{ik}E_{jl}+a_{jl}E_{ik}
-a_{il}E_{jk}-a_{jk}E_{il}\bigr)\\
&-\bigl[
a_i\nabla_kE_{jl}+a_k\nabla_iE_{jl}
+a_j\nabla_lE_{ik}+a_l\nabla_jE_{ik}\\
&\qquad
-a_j\nabla_kE_{il}-a_k\nabla_jE_{il}
-a_l\nabla_iE_{jk}-a_i\nabla_lE_{jk}
\bigr].
\end{aligned}
\]

因此所有 cutoff 导数项都含 \(E\) 或 \(\nabla E\)，没有与缺陷无关的源项。若 \(E=0\)，整个 cutoff 流确实静止。

对 \(a=\chi^2\)，
\[
\nabla a=2\chi\nabla\chi,\qquad
\nabla^2a=2\chi\nabla^2\chi+2\nabla\chi\otimes\nabla\chi,
\qquad
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2.
\]
最后一个恒等式正是避免支撑边缘 \(1/\chi\) 损失的机制。

---

## 2. 缺陷能量：该部分确实闭合到临界曲率项

已核验的缺陷方程为
\[
\partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E).
\]
以独立空间 cutoff \(\eta\) 测试并使用
\[
\div E=\frac12d(\tr E),
\]
可将 \(\nabla^2a\) 全部积分分部掉，得到
\[
\begin{aligned}
\frac d{dt}\int\eta^2|E|^2
+c\int\eta^2a|\nabla E|^2
\le{}&
C\int\bigl(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2a\bigr)|E|^2\\
&+C\int\eta^2a|\Rm|\,|E|^2.
\end{aligned}
\tag{E}
\]
这里无不带权 \(\nabla E\)，也无 \(E\)-无关项。脚本只核验了相应点态代数和齐次性；几何积分分部仍须由上述张量公式证明，不能把脚本本身视为完整证明。

在四维相对 Sobolev 不等式
\[
\|v\|_4^2\le A_B\bigl(\|\nabla v\|_2^2+r^{-2}\|v\|_2^2\bigr),
\qquad
A_B\lesssim \frac{r^2}{V(B)^{1/2}}
\]
下，若
\[
\varepsilon_B(t):=\frac{r^4}{V(B)}\int_B|\Rm|^2\le\varepsilon,
\]
则
\[
A_B\|\Rm\|_{L^2(B)}\lesssim \varepsilon_B(t)^{1/2}.
\]
故取 \(v=\eta\chi|E|\) 可吸收 (E) 中的临界项，只要沿流的 \(\varepsilon_B(t)\) 保持足够小。

---

## 3. 曲率能量必须借用缺陷耗散

由上述完整曲率演化，基本局部估计为
\[
\begin{aligned}
\frac d{dt}\int\eta^2|\Rm|^2
+c\int\eta^2a|\nabla\Rm|^2
\le{}&
C\int\bigl(a|\nabla\eta|^2+\eta^2|\nabla\chi|^2+\eta^2a\bigr)|\Rm|^2\\
&+C\int\eta^2a|\Rm|^3\\
&+C\int\eta^2|\nabla^2a|\,|E|\,|\Rm|\\
&+C\int\eta^2|\nabla a|\,|\nabla E|\,|\Rm|.
\end{aligned}
\tag{R}
\]

若过渡宽度与 \(r\) 同阶且沿流有
\[
|\nabla\chi|\le Cr^{-1},\qquad |\nabla^2\chi|\le Cr^{-2},
\]
则
\[
\int\eta^2|\nabla^2a|\,|E|\,|\Rm|
\le Cr^{-2}\int\eta^2(|E|^2+|\Rm|^2).
\]
而
\[
\begin{aligned}
\int\eta^2|\nabla a|\,|\nabla E|\,|\Rm|
&=2\int\eta^2\chi|\nabla\chi|\,|\nabla E|\,|\Rm|\\
&\le \epsilon\int\eta^2a|\nabla E|^2
+C_\epsilon r^{-2}\int\eta^2|\Rm|^2.
\end{aligned}
\]
所以这一项不能在纯曲率估计内闭合，但可由缺陷方程的加权耗散吸收。立方项则以 \(v=\eta\chi|\Rm|\) 和小的局部归一化曲率能量吸收。

因此有效架构不是单独的 \(R_\alpha\) 不等式，而是
\[
\begin{aligned}
\dot R_\alpha+cX_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta+P_\beta)
+\epsilon_1Y_\alpha,\\
\dot P_\alpha+cY_\alpha
&\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta,
\end{aligned}
\tag{C}
\]
其中
\[
\begin{aligned}
R_\alpha&=\frac{r^4}{V_\alpha(0)}
 \int\eta_\alpha^2|\Rm|^2,&
X_\alpha&=\frac{r^4}{V_\alpha(0)}
 \int\eta_\alpha^2a|\nabla\Rm|^2,\\
P_\alpha&=\frac{r^4}{V_\alpha(0)}
 \int\eta_\alpha^2|E|^2,&
Y_\alpha&=\frac{r^4}{V_\alpha(0)}
 \int\eta_\alpha^2a|\nabla E|^2.
\end{aligned}
\]
覆盖必须具有统一有限重叠，并覆盖**整个 cutoff 支撑及其缓冲邻域**；不能只对内 plateau 取 supremum。选足够大的 \(\kappa\)，
\[
H_\alpha=R_\alpha+\kappa P_\alpha
\]
应满足
\[
\dot H_\alpha+c(X_\alpha+Y_\alpha)
\le Cr^{-2}\sum_{\beta\sim\alpha}H_\beta.
\]
于是
\[
D^+\sup_\alpha H_\alpha\le Cr^{-2}\sup_\alpha H_\alpha,
\]
在 \(t\le\theta r^2\) 上给出 \(e^{C\theta}\) 控制。这是替代错误“inner/outer Gronwall”及错误有限传播论证的正确目标。

取 \(\eta\equiv1\) 并对支撑覆盖求和，同一机制给出
\[
Q(t):=\int_M|E(t)|^2,\qquad
Q'(t)\le Cr^{-2}Q(t),
\]
从而
\[
Q(t)\le e^{C\theta}Q(0).
\]
这足以保持已有的全局 \(L^2\) 小缺陷，但不会自动产生初始不存在的小量。

---

## 4. 题设初始数据尚不能独立保证上述系统

主要缺口有三项。

### (i) 沿流 cutoff Hessian 不是初始控制的直接结果

固定标量函数 \(\chi\) 的协变 Hessian随 \(g(t)\) 改变：
\[
\partial_t(\nabla^2\chi)
=(\partial_t\Gamma)*d\chi
\sim \nabla(aE)*d\chi
=a\nabla E*d\chi+\nabla a*E*d\chi.
\]
能量只控制
\[
a^{1/2}\nabla E=\chi\nabla E\in L^2,
\]
并不推出
\[
\|\nabla^2_{g(t)}\chi\|_\infty\lesssim r^{-2}.
\]
Wang 的高阶延拓论证也明确显示 \(\nabla^2\chi\) 与 \(\nabla(\chi^2\Rm)\) 相互耦合。因此“controlled cutoff derivatives”若仅指 \(t=0\)，不够；必须作为沿流假设，或由单独的局部流正则性定理导出。

### (ii) \(L^2\) 缺陷不能给出度量等价

因为
\[
\partial_tg=-2aE,
\]
所需的是
\[
\int_0^T\|aE(t)\|_\infty\,dt<\infty,
\]
而非仅 \(Q(t)\) 有界。一个足够条件是
\[
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^\gamma,
\qquad \gamma<1,
\tag{M}
\]
于是
\[
\left|\log\frac{g(t)(v,v)}{g(0)(v,v)}\right|
\le 2\int_0^t\|aE(s)\|_\infty ds
\le C_{\gamma,\theta}\delta r^2.
\]
Li 的 \(2/3\) 指数估计可在已建立普通 Ricci 流动态条件的 plateau 上提供这种积分控制，但不能在未控制过渡区时循环地用来先证明全支撑度量等价。

### (iii) 沿流 Sobolev 保持仍有循环

临界吸收在每个时刻都需要
\[
A_\alpha(t)\lesssim A_\alpha(0)
\]
及球、体积、覆盖的可比性。通常这由度量等价导出；但度量等价又需要 (M)，而 (M) 一般依赖曲率 bootstrap/Moser。故仅有初始相对 Sobolev 不等式，尚未解除这个循环。

此外，初始“小能量对所有中心成立”的量词必须覆盖支撑的固定倍数邻域。最干净的修复是令支撑半径本身为 \(Lr\)，其中 \(L\) 固定，并假设或推出
\[
\sup_{y\in U'}r^4\fint_{B_r(y)}|\Rm(g_0)|^2\le\varepsilon.
\]
单个 good point 只控制其固定 \(O(r)\) 邻域，不能控制尺度远大于 \(r\) 的 plateau。

---

## 5. 可成立的精确附加假设／延拓包

若在 bootstrap 区间上补充

\[
\begin{gathered}
\Lambda^{-1}g_0\le g(t)\le\Lambda g_0,\\
A_\alpha(t)\le C A_\alpha(0),\\
|\nabla\chi|_{g(t)}\le Cr^{-1},
\qquad
|\nabla^2\chi|_{g(t)}\le Cr^{-2},
\end{gathered}
\]
并有固定重叠数的全支撑缓冲覆盖，则系统 (C) 严格可行；小初始 \(H(0)\) 给出局部归一化曲率能量的持续性以及全局 \(L^2\) 缺陷保持。

要从原始初始数据自行推出这些条件，还需要一个真正的 transition-inclusive 局部流定理，例如同时证明
\[
\sup_\alpha R_\alpha(t)\le 2\varepsilon,\qquad
\|\chi^2\Rm(t)\|_\infty\le C/t,\qquad
\|\chi^2E(t)\|_\infty
\le C\delta(r^2/t)^\gamma,\ \gamma<1,
\]
以及 cutoff 几何和 Sobolev 常数的保持。Wang 的现有定理提供强结构支持，但其所述版本使用全局 Sobolev、全支撑临界能量及额外 \(L^p\Ric\) 条件，不能直接由当前塌缩相对球数据调用。

**最终判断：** \(\nabla^2a*E*\Rm\) 与 \(\nabla a*\nabla E*\Rm\) 在 \(a=\chi^2\) 时并非数学障碍；它们由低阶估计和耦合缺陷耗散处理，且基本 \(L^2\) 层面不需高于二阶的 cutoff 导数。真正未闭合之处是从给定初始资料推出沿流 cutoff Hessian、Sobolev 保持和可积的加权点态缺陷控制。故当前方案是可信的条件性能量架构，而不是已由所列假设证明的持续性定理。