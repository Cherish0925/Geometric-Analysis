# TTCS Independent Branch Record

```json
{
  "step_id": 33,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step32_nested_moser_and_tensor_audit.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A01/workspace/scripts/step33_curvature_power_verification.py"
  ]
}
```

## Task

Verify two specific mathematical claims in the curvature power inequality for the degenerate cutoff flow d_t g = -2 chi^2(Ric+g).

**Claim 1 (Hessian IBP structure):** In the general-p energy inequality, the Hessian-of-a term contributes to d/dt K_p as C*p*integral(a^{p-2}|nabla^2 a|F^p). If one bounds the tensor contraction pointwise BEFORE testing (replacing <Rm, nabla^2 a*(Rm+I)> by |nabla^2 a|*F^2), then the IBP reduces nabla^2 a to nabla a and the derivative hits only a^{p-2}F^p, producing (p-2)a^{p-3}|nabla a|^2 F^p and p*a^{p-2}F^{p-1}|nabla F|. Neither term involves nabla Rm directly; the full-tensor dissipation D_p^Rm is NOT consumed by this specific IBP step. Check: is this correct? Is there a hidden subtlety where the pointwise bound before testing loses essential cancellation or introduces an error? Compare with the alternative of keeping the tensor contraction and IBP-ing that.

**Claim 2 (J_6 persistence by bounded Gronwall):** The defect power inequality has Gronwall coefficient Lambda(t) = C*p^N*(r^{-2} + 1 + S^2*Y(t)). The positive-time curvature seed gives S^2*Y(t) <= gamma^3/t for t > 0, with gamma = S*K_2(0)^{1/2} <= C*r^2*sqrt(K_0). The integral from 0 to T of S^2*Y(s) ds is FINITE despite the 1/t singularity because: (a) Y(0) is finite for smooth initial data, (b) S^2*Y(0) <= C*gamma^3, (c) the integrated Gronwall is gamma^3*(1 + |log(T/t_0)|) + ... which is bounded for fixed r, theta. Therefore J_6(T) <= J_6(0)*exp(C_Lambda) with C_Lambda sequence-uniform. This avoids using the pointwise curvature bound ||aF|| <= C*gamma/t (whose singularity is nonintegrable at t=0). Check: is this argument mathematically correct? Specifically, does the smoothness of initial data justify replacing the 1/t bound by the finite initial value near t=0? Is there a gap in the transition from the initial-time regime (Y bounded) to the positive-time regime (Y <= gamma*K_2/t)?

## Output

## 科学核验备忘

### 总结

1. 第一项按 Step 33 §2.6 的写法不成立。逐点取绝对值本身给出了合法上界，但此后不能再把 \(\lvert\nabla^2a\rvert\) 当作 \(\nabla^2a\) 做分部积分。若保留原张量缩并做分部积分，导数通常会落到曲率张量上，因此会使用 \(D_p^{\mathrm{Rm}}\)。

2. 第二项所述的初时刻衔接并不能由光滑性推出序列一致的 Gronwall 常数。每个初始度量的光滑性只给出各自的连续性时间尺度。所需可积性可由 A03 Step 34 (3.2) 的时空估计直接得到，而不应积分 \(t^{-1}\) 点态估计。

---

## 1. Hessian-\(a\) 项

设原来的有符号项写成
\[
T_H
=p\int a^{p-2}F^{p-2}(\nabla_i\nabla_j a)B^{ij}(\operatorname{Rm})\,d\mu,
\qquad |B|\le CF^2.
\]
逐点估计确实给出
\[
T_H\le Cp\int a^{p-2}|\nabla^2a|F^p\,d\mu.
\tag{1}
\]
但 (1) 的右端包含 Hessian 的模，而不是有符号的二阶导数。一般不存在
\[
\int |\nabla^2a|\Phi
\lesssim \int |\nabla a|\,|\nabla\Phi|
\tag{2}
\]
这样的普遍不等式。

一个直接反例是在圆周上取
\[
a_k(x)=\frac12+\frac{1}{4k}\sin(kx),\qquad \chi_k=\sqrt{a_k},
\qquad \Phi=a_k^{p-2}.
\]
此时 \(a_k\) 始终为正且 \(\|\nabla\chi_k\|_\infty=O(1)\)，但
\[
\int |a_k''|a_k^{p-2}\asymp k,
\]
而
\[
\int |a_k'|\,|\Phi'|
=(p-2)\int a_k^{p-3}|a_k'|^2=O(1).
\]
因此 Step 33 (2.6a) 到其后“schematically”分部积分的转换缺少数学依据。

若保留原张量结构，则外围积分项消失后
\[
T_H
=-p\int \nabla_j a\,
\nabla_i\!\left(a^{p-2}F^{p-2}B^{ij}\right)d\mu .
\]
展开后出现三类量：
\[
\begin{aligned}
|T_H|\lesssim{}&
p(p-2)\int a^{p-3}|\nabla a|^2F^p\\
&+p(p-2)\int a^{p-2}|\nabla a|F^{p-1}|\nabla F|\\
&+p\int a^{p-2}|\nabla a|F^{p-1}|\nabla\operatorname{Rm}|.
\end{aligned}
\tag{3}
\]
第三项来自 \(\nabla B\); 对这里的曲率缩并，
\[
|\nabla B|\lesssim F|\nabla\operatorname{Rm}|.
\]
它通常要由
\[
D_p^{\mathrm{Rm}}
=\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
\]
吸收。第二项只涉及径向收缩 \(\nabla F\)，可由 \(D_p^F\) 处理。某些精确指标组合也许会与原演化式中的 \(\nabla a*\nabla\operatorname{Rm}\) 项抵消，但这必须从完整张量恒等式证明；逐点取模会丢掉这种结构。

所以准确表述是：

- 逐点取模没有产生错误；
- 取模以后不能执行 Step 33 所写的分部积分；
- 若有独立的逐点估计 \(|\nabla^2a|\lesssim r^{-2}\)，则可直接估计 (1)；
- 若没有该估计，保留张量缩并的做法通常会使用完整曲率耗散。

这与 Step 32 §5 的张量展开一致。Python 脚本中“Hessian IBP does NOT produce nabla Rm directly”一行只是 `check(..., True)`，并未验证这一分析步骤。

---

## 2. \(J_6\) 的 Gronwall 积分

仅从
\[
q(t):=\mathcal S^2Y(t)\le \frac{A}{t},\qquad q(0)\le B,
\]
以及 \(q\) 在零点连续，不能得到只依赖 \(A,B,T\) 的
\(\int_0^Tq(t)\,dt\) 上界。

例如对任意小的 \(\varepsilon>0\)，取连续函数
\[
q_\varepsilon(t)=
\begin{cases}
A t/\varepsilon^2,&0\le t\le\varepsilon,\\[2mm]
A/t,&\varepsilon\le t\le T.
\end{cases}
\]
它满足 \(q_\varepsilon(0)=0\) 和 \(q_\varepsilon(t)\le A/t\)，但
\[
\int_0^Tq_\varepsilon(t)\,dt
=\frac A2+A\log\frac{T}{\varepsilon},
\]
可以任意大。平滑连接不会改变这一结论。

因此：

- 初始光滑性保证每一个固定流的 \(Y(t)\) 在零点附近有限；
- 它不给出共同的连续性时间尺度；
- 不能用 \(\mathcal S^2Y(0)t_0\) 估计整个 \([0,t_0]\)，除非另有
  \(\sup_{[0,t_0]}Y\le CY(0)\)；
- 序列相关的 \(t_0\) 还会使 \(\log(T/t_0)\) 无法一致控制。

此外，
\[
\mathcal S^2Y(0)\le C\gamma^3
\]
也不由 \(K_2(0)\) 控制自动推出。Sobolev 插值实际给出
\[
\mathcal S^2Y(0)
\le C\mathcal S^3K_2(0)^{1/2}
\bigl(D_2(0)+r^{-2}K_2(0)\bigr),
\]
其中包含未被现有输入一致控制的 \(D_2(0)\)。

### 可成立的可积性来源

A03 Step 34 (3.2) 已记录更强且正好适用的时空估计：
\[
\int_0^T Y(s)\,ds\le C\gamma K_2(0).
\]
若在同步 first-exit 区间内
\(\mathcal S(t)\le2\mathcal S(0)\)，则
\[
\int_0^T\mathcal S(t)^2Y(t)\,dt
\le C\mathcal S(0)^2\gamma K_2(0)
=C\gamma^3.
\tag{4}
\]
这里使用
\[
\gamma=\mathcal S(0)K_2(0)^{1/2}.
\]
于是对 \(p=6\)
\[
\int_0^T\Lambda(t)\,dt
\le C6^N\bigl(r^{-2}T+T+\gamma^3\bigr),
\]
而 \(T=\theta r^2\) 时 \(r^{-2}T=\theta\)。这个推导不含对数，也不使用
\(\|aF\|_\infty\lesssim\gamma/t\)。

最后，Step 33 (4.4) 写有加性项 \(C_0'p\)。按该式直接应用 Gronwall 得到的是
\[
J_6(T)\le e^{\int_0^T\Lambda}
\left(J_6(0)+6C_0'T\right).
\]
因此 \(J_6(T)\le C\delta^6V\) 还要求 \(C_0'=0\)，或证明正则化产生的该项随 \(\varepsilon\to0\) 消失。由于 \(E=0\) 时流静止，未正则化的 defect 演化应当齐次于 \(E\)；这一点需要在 \(f_\varepsilon\) 推导中明确体现。

附带地，Step 33 使用的 Hölder 指数应为 \((3,3,3)\)，不是
\((3,3,3/2)\)：
\[
\int A^{1/3}B^{1/3}z^{4/3}
\le \left(\int A\right)^{1/3}
   \left(\int B\right)^{1/3}
   \left(\int z^4\right)^{1/3}.
\]
修正后仍然得到所需的 \(\mathcal S^2YJ_p\) 系数。