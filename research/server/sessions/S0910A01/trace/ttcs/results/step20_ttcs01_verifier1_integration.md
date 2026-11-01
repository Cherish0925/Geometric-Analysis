# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 20,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step20_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step20_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 20 analytic change in the Yau 26 four-dimensional negative-route cutoff-flow work. Read the Step 20 closed tensor estimate, Step 20 scripts, and Step 19 Whitney/TTCS context. Check scientifically: (1) whether E=Ric+g and nabla E=contraction(nabla Rm) legitimately allow the Hess(a) and nabla a*nabla E terms in the curvature-power energy to be absorbed into full curvature dissipation without a separate high-power defect-gradient energy; (2) whether the schematic curvature variation under h=-2aE correctly has no Einstein-independent Hess(a) source; (3) whether the q-dependent inequality and the warning about all-exponent critical absorption are mathematically sound; (4) whether the triangular unweighted defect estimate avoids the invalid +epsilon X inference and can preserve Q/A->0 under small beta; and (5) what exact gaps remain before this becomes a theorem. Be strict about hidden assumptions: evolving metric, volume form, covariant derivative convention, cutoff Hessian, finite-neighbor summation, Sobolev constants, and collapse-uniform constants.

## Integrated Scientific Memo

# Step 20 严格核验结论

## 总结判定

Step 20 的核心解析改动是正确且重要的：

\[
E=\operatorname{Ric}+g=\operatorname{contr}_{g}\operatorname{Rm}+g,
\qquad
\nabla E=\operatorname{contr}_{g}(\nabla\operatorname{Rm})
\]

在每个光滑时片上成立。因此，将 \((\nabla^2a)E\) 分部积分后产生的 \(\nabla E\) 可以由完整曲率耗散控制，高次曲率能量无需另引入高次 defect-gradient 能量。

同时，把速度保持为整体 \(h=-2aE\) 可看出：所有 cutoff 导数项都带 \(E\) 或 \(\nabla E\)，不存在在 \(E=0\) 时仍存留的 Einstein-independent \((\nabla^2a)g\) 源。三角形的未加权 defect 估计也是修复旧 \(+\varepsilon X\) 论证的正确机制。

但目前仍不是一个 PDE 定理。特别需要修正：

1. (7.1) 中的
   \[
   (\nabla a)*\operatorname{Rm}*E
   \]
   按标准 Ricci 线性化不应出现；真正的曲率项是
   \(a\,\operatorname{Rm}*E\)，可能已包含在 \(a\Delta_LE\) 中。若前者真实存在，则 (7.2)–(7.3) 并不由临界 \(L^2\) 控制闭合。
2. (2.2) 将线性 \(a\operatorname{Rm}\) 项归因于 \(a\nabla^2E\) 不准确；它来自曲率变分的代数 \(h*\operatorname{Rm}\) 部分。
3. 脚本只是结构与指数账本，不证明精确的 \(q\)-常数、有限指数增益或 Moser 定理。

---

## 1. Hessian cutoff 和 \(\nabla a\,\nabla E\) 能否闭合于曲率耗散？

可以，但有两个必要约定：

- 所有收缩、范数及 \(\nabla\) 均相对于当前度量 \(g(t)\)；
- \(\operatorname{Rm}\) 的张量型必须固定，并把度量逆矩阵的时间变化纳入能量计算。

因为 \(\nabla^{g(t)}g(t)=0\)，

\[
E_{ij}=g^{k\ell}R_{kilj}+g_{ij},
\qquad
\nabla_pE_{ij}=g^{k\ell}\nabla_pR_{kilj}.
\]

故有维数常数

\[
|\nabla E|\le C_n|\nabla\operatorname{Rm}|,\qquad
|E|\le C_nF,\qquad
F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

若 \(\nabla\) 被解释为固定的初始连接，这些公式不再成立；会多出 connection-difference 项。

对代表项

\[
I_q=q\int\eta^2F^{q-2}\operatorname{Rm}*(\nabla^2a)*E
\]

分部积分一次，所得非局部化项均可粗略化为

\[
Cq^2\int\eta^2|\nabla a|F^{q-1}|\nabla\operatorname{Rm}|.
\]

按照

\[
\sqrt a\,F^{(q-2)/2}|\nabla\operatorname{Rm}|
\cdot
\frac{|\nabla a|}{\sqrt a}F^{q/2}
\]

施行 Young 不等式，得到

\[
|I_q|
\le \varepsilon q\int\eta^2aF^{q-2}|\nabla\operatorname{Rm}|^2
 +C_\varepsilon q^3
   \int\eta^2\frac{|\nabla a|^2}{a}F^q
 +Cq\int a|\nabla\eta|^2F^q .
\]

直接的 \((\nabla a)*\nabla E\) 项同理。又因为 \(a=\chi^2\)，

\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2
\]

在 \(\{\chi>0\}\) 上成立，并连续延拓为有界量；因此没有 \(\chi^{-1}\) 损失。Step 19 中的混合项

\[
\frac{|\nabla a|^2}{a}|E|^2|\operatorname{Rm}|^{q-2}
\]

也由 \(|E|\le C_nF\) 化为

\[
C\frac{|\nabla a|^2}{a}F^q.
\]

所以该层确实不需要独立的高次 \(\nabla E\) 能量。若保留径向耗散

\[
q(q-2)\int\eta^2aF^{q-2}|\nabla F|^2,
\]

可改善 \(q\)-损失，但并不改变闭合机制。

---

## 2. 曲率变分中是否存在 Einstein-independent \(\nabla^2a\) 源？

不存在。对固定空间函数 \(a=\chi^2\) 和

\[
h=\partial_tg=-2aE,
\]

曲率变分为

\[
D\operatorname{Rm}_g(h)=\nabla^2h+h*\operatorname{Rm}.
\]

展开

\[
\nabla^2(aE)
=a\nabla^2E+(\nabla a)*\nabla E+(\nabla^2a)*E.
\]

因此所有 cutoff 导数项都含 \(E\) 或 \(\nabla E\)。当 \(E=0\) 时 \(h=0\)，度量和曲率均静止；任何在 \(E=0\) 时仍存留的 \((\nabla^2a)g\) 都必是将

\[
-2aE=-2a\operatorname{Ric}-2ag
\]

人为拆开后未重组导致的伪源。

正确的曲率方程结构是

\[
\partial_t\operatorname{Rm}
=
a\Delta\operatorname{Rm}
+a\,\operatorname{Rm}*\operatorname{Rm}
+a\,\operatorname{Rm}
+(\nabla a)*\nabla E
+(\nabla^2a)*E
+aE*\operatorname{Rm},
\]

其中各代数项可依曲率张量型和符号约定重新分配。需要纠正的是：线性规范化项 \(a\operatorname{Rm}\) 不是由 \(a\nabla^2E\) 产生，而来自 \(h*\operatorname{Rm}\) 中的 \(-2ag\) 部分。

能量中还必须显式计入

\[
\partial_t d\mu=-a\,\operatorname{tr}E\,d\mu
\]

以及曲率范数随 \(g(t)\) 的变化。这些产生

\[
CaF^{q+1}+CaF^q
\]

型反应项，故不破坏曲率闭合。

---

## 3. \(q\)-依赖不等式和“不能全指数临界吸收”的警告

以下结构是可信的：

\[
\begin{aligned}
\frac d{dt}\int\eta^2F^q
+cq\int\eta^2aF^{q-2}|\nabla\operatorname{Rm}|^2
\le{}&
Cq\int\eta^2aF^{q+1}\\
&+Cq^3\int\eta^2
 \left(\frac{|\nabla a|^2}{a}+a\right)F^q\\
&+Cq\int a|\nabla\eta|^2F^q .
\end{aligned}
\]

但它尚是 schematic inequality，不是已完成的指标级估计。

令 \(\phi=\eta F^{q/2}\)。四维临界 Sobolev 给出

\[
\int\eta^2aF^{q+1}
\lesssim \|F\|_{L^2(W)}
\|\chi\eta F^{q/2}\|_{L^4(W)}^2.
\]

由于

\[
|\nabla(F^{q/2})|
=\frac q2 F^{q/2-1}|\nabla F|,
\]

将右侧改写为能量耗散会产生 \(q\)-因子。由当前粗糙耗散估计，吸收条件至多形如

\[
Cq^2\beta_W<c;
\]

若利用完整的 \(q(q-2)|\nabla F|^2\) 耗散，可望改善到

\[
Cq\beta_W<c.
\]

两者都随 \(q\to\infty\) 恶化。因此固定临界小量 \(\beta_W\) 不能直接支持“每个指数都重新临界吸收”的迭代。这个警告是正确的。

脚本中的 \(\beta_{\max}\sim q^{-1}\) 只是改善版的示意；它并非从脚本所打印的粗糙 \(q^3\) 账本严格推出。

还需修正 \(F\) 的 Sobolev乘积。因为 \(F=(1+|\operatorname{Rm}|^2)^{1/2}\)，

\[
S_W\|F\|_2
\le S_W\|\operatorname{Rm}\|_2
 +S_W\operatorname{Vol}(W)^{1/2}
\le C\sqrt{K_0}\,r^2+C\ell^2.
\]

所以 (6.2) 应写成 \(C\sqrt{1+K_0}\,r^2\) 型估计，或另列 \(Cr^2\) 项。

“先到固定 \(q_0>2\)，再做 mean-value”是合理方向，但尚未实现：仅把 (5.1) 用于 \(q=q_0\) 需要初始 \(L^{q_0}\) 输入，而初始临界 \(L^2\) 小并不控制它。缺少的关键步骤是从 \(q=2\) 能量持续性出发，在正时间产生超临界可积性。Li 的来源材料也是先由临界能量产生 \(L^3\) 势估计，再使用线性 Moser 定理，而不是在无穷指数上反复临界吸收。

---

## 4. 三角形未加权 defect 估计

旧形式

\[
Q'\le Cr^{-2}Q+\varepsilon X,
\qquad
X=\int a|\nabla\operatorname{Rm}|^2
\]

确实无效。若

\[
\int_0^TX\,dt=O(\mathcal A),
\]

则 Gronwall 后保留 \(O(\varepsilon\mathcal A)\)，固定 \(\varepsilon\) 时不能从
\(Q(0)/\mathcal A\to0\) 推出 \(Q(T)/\mathcal A\to0\)。

### 必须修正的 \(E\)-方程

标准 Ricci 线性化表明其结构应为

\[
\partial_tE
=
a\Delta_LE-2aE
+(\nabla a)*\nabla E
+(\nabla^2a)*E,
\]

其中 \(a\,\operatorname{Rm}*E\) 可包含在 \(\Delta_L\) 内，也可单独写出。Step 20 的

\[
(\nabla a)*\operatorname{Rm}*E
\]

没有由 \(D\operatorname{Ric}(-2aE)\) 产生的明显来源，应删除，除非完整指标计算证明其存在。它与随后 (7.2) 也不一致：若该项存在，会产生

\[
|\nabla a|\,|\operatorname{Rm}|\,|E|^2
\]

势，而不能由所写的 \(a|\operatorname{Rm}||E|^2\) 代替。

修正后，将方程乘以 \(\eta^2E\)，分部积分 \((\nabla^2a)E\)，并加入范数和体积变化，得到

\[
\begin{aligned}
\frac d{dt}\int\eta^2|E|^2
+c\int\eta^2a|\nabla E|^2
\le{}&
C\int\eta^2
\left(
\frac{|\nabla a|^2}{a}
+a+a|\operatorname{Rm}|
\right)|E|^2\\
&+C\int a|\nabla\eta|^2|E|^2 .
\end{aligned}
\]

其中 \(a|E|^3\) 可由

\[
a|E|^3\le C a(1+|\operatorname{Rm}|)|E|^2
\]

处理。

曲率势满足

\[
\begin{aligned}
\int a|\operatorname{Rm}|\,|\eta E|^2
&=\int|\operatorname{Rm}|\,|\chi\eta E|^2\\
&\le \|\operatorname{Rm}\|_2
 \|\chi\eta E\|_4^2\\
&\le C\beta_W\int\eta^2a|\nabla E|^2\\
&\quad+C\beta_W(c^{-2}+L^2)r^{-2}
 \int_{\widetilde W}|E|^2 .
\end{aligned}
\]

这里使用 tensor Kato、相对 Sobolev 以及

\[
a|\nabla\eta|^2\lesssim c^{-2}r^{-2},\qquad
|\nabla\chi|^2\lesssim L^2r^{-2}.
\]

因此在时间一致的小 \(\beta_W\) 下，曲率势可被 defect 耗散吸收，不产生任何 curvature-only 加性源。这正是保持 \(Q/\mathcal A\to0\) 所需的三角结构。

若 Whitney 扩大球具有统一有限图度数和重叠数，并使用未归一化能量，则

\[
Q_\alpha'
\le C(c,L)r^{-2}
\sum_{\beta\sim\alpha}Q_\beta.
\]

经有限截断后求和并取单调极限，可得

\[
Q_{\rm active}(T)
\le
\exp\!\left(C(c,L,N)\frac{T}{r^2}\right)
Q_{\rm active}(0).
\]

常数实际含 \(c^{-2}\)；若 \(T=\theta r^2\) 且 \(\theta\lesssim c^2\)，指数因子统一有界。补集上 \(a=0\)，度量静止，故全局 \(Q\) 同样被初值乘法控制。

---

## 5. 成为定理前尚缺的精确对象

1. **完整指标级演化公式。**  
   固定 \(\operatorname{Rm}\) 的张量型、Laplacian 符号和 Lichnerowicz 约定，逐项推导 \(\partial_t\operatorname{Rm}\) 与 \(\partial_tE\)，确认所有 \(a,\nabla a,\nabla^2a\) 项；尤其删除或证明 (7.1) 中争议的
   \((\nabla a)*\operatorname{Rm}*E\)。

2. **完整能量恒等式。**  
   纳入 evolving metric、逆度量、曲率范数和
   \(\partial_td\mu=-a\operatorname{tr}E\,d\mu\)，证明精确 \(q\)-依赖，而非只给 schematic ledger。

3. **正时间超临界增益。**  
   从初始临界 \(L^2\) 曲率和时间一致的小局部能量，推出某个固定 \(q_0>2\) 的嵌套 Whitney-cylinder 控制；不能假设初始 \(L^{q_0}\)。

4. **适用的 mean-value/\(\varepsilon\)-regularity 定理。**  
   需要处理 tensor equation、变系数 \(a\Delta\)、仅在弱能量中消除的 \(\nabla^2a\) 项及有限邻居边界项，最终推出
   \[
   |a\operatorname{Rm}|\le C/t.
   \]
   现有 Li 定理的来源材料不直接覆盖这一局部 cutoff-flow 系统。

5. **时间一致的局部临界小量。**  
   必须在每个所需扩大 Whitney 球上保持
   \[
   S_W\|\operatorname{Rm}(t)\|_2\ll1.
   \]
   任意支持并集上的总能量界不足以排除单个分量能量集中；需要逐支持分量/有限邻域的局部预算与持续性。

6. **Whitney 图的严格求和。**  
   证明扩大相交球半径可比、统一有限图度数和 overlap；只对未归一化积分直接求和。对可数 cover 应通过有限截断和极限完成论证。

7. **evolving geometry 与 cutoff 约定。**  
   Whitney 球和空间 cutoff 最好固定于 \(g_0\)；必须用 provisional metric comparability 控制其在 \(g(t)\) 下的梯度、体积、球包含关系和 Sobolev 常数。若 \(\chi\) 固定为光滑函数，则 \(\partial_ta=0\)，但 \(|\nabla a|_{g(t)}\) 和 \(\nabla_{g(t)}^2a\) 仍演化。

8. **collapse-uniform 常数审计。**  
   BG/Sobolev 体积消去本身正确，但最终常数还依赖局部能量分布、metric comparability、Sobolev 常数、扩大倍数、\(c,L\)、邻居数及张量 Kato 常数；完成迭代前不能宣称最终估计 collapse-uniform。

9. **存在与 bootstrap 闭合。**  
   需要 cutoff Ricci–DeTurck 的光滑短时存在与延拓，并将 metric/Sobolev 持续性、局部曲率能量、加权 defect 和点态曲率组织为真正严格改善的 first-exit 系统。

10. **后续导数估计仍独立缺失。**  
    若下游需要 connection 或 cutoff-Hessian drift，则还须证明
    \[
    |\chi\nabla(aE)|
    \le C_p\delta\,t^{-1/2}(r^2/t)^{2/p},
    \]
    且时间可积性要求 \(p>4\)。

## 最终评价

Step 20 已正确解决两个结构问题：

- 高次曲率能量中的 \(\nabla E\) 不是独立未知量，可由完整 \(\nabla\operatorname{Rm}\) 耗散吸收；
- 未加权 defect 必须通过乘法型三角估计，而不是 \(+\varepsilon\) curvature-dissipation 源来传播。

但它尚未证明局部 cutoff-flow \(\varepsilon\)-regularity，也未证明
\(|a\operatorname{Rm}|\le C/t\)。当前最关键的直接缺口是：修正后的精确 \(E\)-方程，以及从临界 \(L^2\) 到正时间超临界可积性再到 pointwise bound 的局部、有限邻居、collapse-uniform 抛物定理。