# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 24,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step24_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step24_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following two claims for the 4D normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed Riemannian 4-manifold.

CLAIM 1 (Normalization reaction): Under h = -2a·g with a = χ², the linearized Riemann curvature variation has ZERO lower-order R·h contribution. The conformal piece contributes only the Kulkarni-Nomizu Hessian source -(∇²a ∧ g) to ∂_t R_{ijkl}. Consequently, the full flow h = -2a(Ric+g) has curvature evolution ∂_t Rm = a·ΔRm + a·(Rm*Rm) + (∇a)*(∇Ric) + (∇²a ∧ E), where the quadratic reaction is EXACTLY the same as Wang's unnormalized local Ricci flow, and the normalization produces no linear Rm reaction.

CLAIM 2 (Subcritical downstream chain): Conditional on the q=2,3 integrated energy inequalities holding for the normalized cutoff flow, the complete chain from H₃(t) ≤ Cγ³/t to the gap theorem on critical Ishida-LeBrun 4-manifolds is logically sound:
(a) The subcritical Moser iteration from L³ to L^∞ converges because 3 > n/2 = 2 in 4D. The exponent sequence q_k = 3·(3/2)^k and the per-step constant product converge.
(b) The defect iteration from J₆ to |aE| ≤ Cδ(r²/t)^{1/3} uses the same subcritical potential.
(c) The metric drift ∫₀^{θr²} |aE| dt is integrable (proportional to δ), hence self-improving.
(d) All five first-exit conditions (Sobolev, energy, curvature, defect, metric) are self-improving.

Please verify these using the general linearized curvature variation formula (Chow-Lu-Ni Lemma 2.27) and the standard subcritical Moser theory. Identify any errors, missing hypotheses, or gaps in the chain.

## Integrated Scientific Memo

# 核验结论

## 1. Claim 1 为假：归一化项确实产生线性曲率反应

必须先区分 Riemann 张量的指标类型。对全降指标张量 \(R_{ijkl}\)，由一般曲率线性化公式，若

\[
h=\varphi g,
\]

则在给定 Kulkarni–Nomizu 约定下

\[
(D\operatorname{Rm})_g(\varphi g)_{ijkl}
=
\varphi R_{ijkl}
+\frac12(\nabla^2\varphi\owedge g)_{ijkl},
\]

其中 Hessian 项的符号会随曲率号约定改变，但代数项 \(\varphi R_{ijkl}\) 不会消失。因此令 \(\varphi=-2a\)，得到

\[
\boxed{
(D\operatorname{Rm})_g(-2ag)
=
-2a\,\operatorname{Rm}
-(\nabla^2a\owedge g)
}
\]

（后一项的整体符号按约定可能相反）。

### 决定性的常数缩放检验

若 \(a\equiv1\)，且只考虑

\[
\partial_tg=-2g,
\]

则 \(g(t)=e^{-2t}g(0)\)。Levi-Civita 联络以及 \(R^l{}_{ijk}\) 不变，但降低最后一个指标后

\[
R_{ijkl}(t)=e^{-2t}R_{ijkl}(0),
\]

所以

\[
\partial_tR_{ijkl}=-2R_{ijkl}.
\]

故“全降指标曲率没有 \(R\cdot h\) 低阶项”的断言不可能成立。

零代数反应只对混合型张量 \(R^l{}_{ijk}\) 成立。将最后一个指标降低时，会额外产生

\[
h_{lm}R^m{}_{ijk}=\varphi R_{ijkl}.
\]

这正是 `verify_step24_downstream_chain.py` 所遗漏的项。该脚本的“相消”实际上混用了 \((1,3)\) 与 \((0,4)\) 张量。

### 正确的完整结构

Wang 的局部 Ricci 部分可写为

\[
D\operatorname{Rm}(-2a\operatorname{Ric})
=
a\Delta\operatorname{Rm}
+aQ(\operatorname{Rm})
+\mathcal C(\nabla a,\nabla\operatorname{Ric})
-(\nabla^2a\owedge\operatorname{Ric}),
\]

因此归一化流

\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}+g
\]

满足

\[
\boxed{
\partial_t\operatorname{Rm}
=
a\Delta\operatorname{Rm}
+aQ(\operatorname{Rm})
-2a\operatorname{Rm}
+\mathcal C(\nabla a,\nabla E)
-(\nabla^2a\owedge E).
}
\]

精确结论是：

- 二次项 \(Q(\operatorname{Rm})\) 与 Wang 的未归一化局部 Ricci 流相同；
- 归一化项额外产生线性反应 \(-2a\operatorname{Rm}\)；
- cutoff Hessian 项确实合并成对 \(E\) 齐次的
  \[
  -(\nabla^2a\owedge E);
  \]
- \(\nabla a\) 项可写成 \(\mathcal C(\nabla a,\nabla E)\)，因为 \(\nabla g=0\)。

当 \(E=0\) 时，整个速度为零。右侧逐项相消依赖 Einstein 曲率恒等式

\[
\Delta\operatorname{Rm}+Q(\operatorname{Rm})
=2\operatorname{Rm}
\qquad (\operatorname{Ric}=-g),
\]

而不是因为归一化线性项不存在。

该线性项对能量论证不是致命的。它至多贡献

\[
C_q\int\eta^2a^{q-1}F^q
\le C_qH_q,
\]

当 \(r\le1\) 时可并入 \(C_qr^{-2}H_q\)。因此 Step 23 的能量框架可修复，但其曲率演化必须显式保留线性项。

---

## 2. Claim 2 只有部分成立；由 \(q=2,3\) 不等式不能推出“完整链”

### 必须先恢复正确的 \(H_3\) 归一化

按 Step 23 的 Sobolev 记号

\[
\|u\|_4^2\le \mathsf S
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\]

实际得到的是

\[
\boxed{
\mathsf S^2H_3(t)\le \frac{C\gamma^3}{t},
}
\]

而不是无条件的 \(H_3(t)\le C\gamma^3/t\)。在塌缩情形中 \(\mathsf S\) 可能依赖局部体积，不能省略。

该归一化正好给出势项形式估计：

\[
\int Fv^2
\le
\varepsilon\mathcal E[v]
+
C\varepsilon^{-2}\mathsf S^2H_3\,\|v\|_2^2.
\]

在 \([t/2,t]\) 上，

\[
\int_{t/2}^{t}\mathsf S^2H_3(s)\,ds
\le C\gamma^3\log2,
\]

这是正时间 Moser 迭代真正需要的无量纲输入。

### (a) 指数与常数乘积：正确，但不足以构成证明

令

\[
q_k=3\left(\frac32\right)^k.
\]

若第 \(k\) 步常数至多按 \(Cq_k^A\) 增长，则

\[
\prod_k(Cq_k^A)^{1/q_k}<\infty,
\]

因为

\[
\sum_k\frac1{q_k}<\infty,
\qquad
\sum_k\frac{\log q_k}{q_k}<\infty.
\]

正时间 slab 上，势属于 \(L^\infty_tL^3_x\)，满足

\[
\frac{2}{\infty}+\frac{4}{3}<2,
\]

所以在正确的混合时空意义下确为抛物次临界。

但 \(q=2,3\) 两个能量不等式本身并不提供：

1. 所有 \(q\ge3\) 的加权能量不等式及可控的 \(q\)-依赖；
2. 或一个可直接应用标准 Moser 定理的标量弱不等式。

此外 \(a=\chi^2\) 在过渡环带退化。普通一致抛物 Moser 只能直接用于 \(a=1\) 的内平台；若要求全支撑上的 \(|aF|\) 控制，必须证明相应加权退化 Moser 理论或完整的 all-\(q\) 层级。

形式上，若这些额外输入成立，则标准尺度计算给出

\[
\|aF(t)\|_\infty
\lesssim
\mathsf S^{2/3}t^{-2/3}H_3(t/2)^{1/3}
\lesssim \frac{C(\gamma)\gamma}{t},
\]

其中 \(\mathsf S^2H_3\) 的归一化恰好消去塌缩相关 Sobolev 因子。供应的 downstream 脚本没有完成这一计算；其注释中出现残余体积因子后直接“接受标准结果”，因此不能视为证明。

### (b) 缺陷迭代：条件成立，但需要独立输入

若对所有 \(m\ge6\) 已证明齐次缺陷不等式，并有

\[
J_6(t/2)\le C\delta^6V,
\qquad
\mathsf S\lesssim r^2V^{-1/2},
\]

则标准 \(L^6\to L^\infty\) 尺度给出

\[
\|aE(t)\|_\infty
\lesssim
\mathsf S^{1/3}t^{-1/3}J_6(t/2)^{1/6}
\lesssim
C(\gamma)\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

体积确实消去：

\[
\mathsf S^{1/3}V^{1/6}
\lesssim r^{2/3}.
\]

但这不从曲率的 \(q=2,3\) 不等式自动推出。还需要：

- 从 \(t=0\) 开始的独立 \(J_6\) 持久性；
- 所有 \(m\ge6\) 的缺陷层级或相应标量定理；
- 对退化过渡区的加权处理。

必须在 \([t/2,t]\) 上启动迭代，不能从 \(0\) 积分 \(H_3(s)\sim s^{-1}\) 的系数。

### (c) 度量漂移：条件正确

给定上述缺陷点态估计，

\[
\begin{aligned}
\int_0^{\theta r^2}|aE(t)|\,dt
&\le
C\delta r^{2/3}\int_0^{\theta r^2}t^{-1/3}\,dt\\
&=
\frac32C\delta\theta^{2/3}r^2.
\end{aligned}
\]

由于

\[
\left|\frac d{dt}\log g_t(v,v)\right|
\le2|aE|_{g(t)},
\]

这给出与 \(\delta\) 成正比的双 Lipschitz 漂移。该积分步骤没有问题。

### (d) 五个 first-exit 条件：尚未全部验证

- **Sobolev 条件**：在预设双 Lipschitz 区间内稳定，但需要明确阈值和严格余量。
- **\(H_2\) 能量条件**：由吸收后的 \(q=2\) 不等式得到。
- **曲率条件**：依赖尚未证明的 all-\(q\)/加权 Moser 步骤。
- **缺陷条件**：依赖独立的 \(J_m\) 层级。
- **度量条件**：一旦缺陷点态估计成立即可自改善。

正确的 first-exit 逻辑应是：假设在首次退出前双 Lipschitz 因子至多为 \(2\)，在此假设下推导漂移严格小于 \(\log2\)，从而排除退出。不能把“从 \(1+\varepsilon\) 到 \(2\)”称为改善。

---

## 3. 仍缺少的关键数学对象

即便接受 \(q=2,3\) 曲率能量不等式，完整 gap theorem 仍需：

1. 带可控 \(q\)-增长的 all-\(q\) 曲率不等式，或适用于 \(a=\chi^2\) 退化算子的加权标量 Moser 定理；
2. 保持 \(\mathsf S\)、局部体积和时间尺度精确幂次的塌缩无关点态估计；
3. 独立证明 \(J_6\) 持久性以及 all-\(m\) 缺陷迭代；
4. 归一化退化 cutoff flow 的 DeTurck/Yang–Wang 型光滑延拓；
5. 明确的 first-exit 参数选择与严格余量；
6. 从平滑化到 Ishida–LeBrun 矛盾的紧致性、校准密度、\(W^+\) 谱和投影论证。现有文件只列出这些步骤，未提供可核验证明。

## 最终判定

- **Claim 1：错误。** 对 \(R_{ijkl}\)，归一化贡献
  \[
  -2aR_{ijkl}-(\nabla^2a\owedge g)_{ijkl}.
  \]
  只有混合型 \(R^l{}_{ijk}\) 没有代数缩放项。正确说法是“二次反应与 Wang 相同，但另有无害的线性 \(-2a\operatorname{Rm}\) 反应”。

- **Claim 2(a)：指数次临界性及常数乘积收敛正确；但完整迭代未由所给假设证明。**
- **Claim 2(b)：目标指数 \(1/3\) 与尺度一致，但需要独立的全缺陷层级和塌缩无关加权迭代。**
- **Claim 2(c)：在 (b) 条件下正确。**
- **Claim 2(d)：只有 Sobolev、能量和条件性的度量部分已闭合；曲率与缺陷条件仍是实质缺口。**

因此，“仅条件于 \(q=2,3\) 曲率积分不等式，整个下游 gap theorem 链逻辑完备”这一总断言不成立。