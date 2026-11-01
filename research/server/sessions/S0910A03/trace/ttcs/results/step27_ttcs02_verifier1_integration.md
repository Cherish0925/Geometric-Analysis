# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 27,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step27_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step27_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Resolve one exact derivative-index discrepancy that emerged after the prior review. Wang Proposition 4.14 assumes cutoff derivatives only through order m when proving an L^p bound for ∇^m(χ²Rm), even though its raw Γ1,Γ2,Γ3 terms contain χ∇^{m+2}χ·U, ∇χ∇^{m+1}χ·U, and χ∇^{m+1}χ·∇U. The Step 27 theorem draft instead introduced a current-order pair ∇^mU ↔ ∇^{m+1}χ after only one integration by parts. Read Wang lines 622–659 and the shifted-curvature equations. Determine which dependency is actually justified. Reconstruct the grouped integration-by-parts reduction of Γ1–Γ3 far enough to show whether all ∇^{m+1}χ terms reduce to diffusion-controlled terms plus ∇²χ·∇^mχ·U (as Wang states), or whether Wang implicitly needs ∇^{m+1}χ/current Volterra closure. Then state the correct induction order for shifted T=Rm+G, U=aT, and identify any exact coefficient/cancellation needed rather than relying only on schematic stars.

## Integrated Scientific Memo

# 核验结论

Wang Proposition 4.14 按其所写的能量论证，**不能**把 \(\nabla^m(\chi^2\mathrm{Rm})\) 对截断函数的依赖降到仅含 \(\nabla^{\le m}\chi\)。实际成立的最高阶依赖是

\[
\boxed{\nabla^mU\ \longleftrightarrow\ \nabla^{m+1}\chi},
\qquad
U=aT,\quad T=\mathrm{Rm}+G,\quad a=\chi^2.
\]

Wang 所指出的残项

\[
\nabla^2\chi*\nabla^m\chi*U
\]

确实出现，但它只是把某些 \(Z\)-层面的 \(\nabla^{m+1}\chi\) 项再次分部积分后的残项；来自真正最高项
\(\chi\nabla^{m+2}\chi*U\) 的“导数落在能量测试张量上”的项仍含
\(\nabla^{m+1}\chi\)，不能由一阶扩散能量继续降阶。因此 Step 27 引入当前阶 Volterra 配对是正确修补，Prop. 4.14 的文字性 \(m\)-阶断言过强。

---

## 1. \(\Gamma _1,\Gamma _2,\Gamma _3\) 的分组分部积分

令

\[
W=\nabla^mU,\qquad Z=|W|^{p-2}W,\qquad \Phi=\nabla^m\chi .
\]

忽略仅含 \(\nabla^{\le m}\chi\) 的交换子，三个最高截断项的固定收缩通道为

\[
\begin{aligned}
\Gamma _1&=c_1\int Z*\chi\nabla^2\Phi*U,\\
\Gamma _2&=c_2\int Z*\nabla\chi*\nabla\Phi*U,\\
\Gamma _3&=c_3\int Z*\chi\nabla\Phi*\nabla U .
\end{aligned}
\]

对 \(\Gamma _1\) 分部积分一次：

\[
\begin{aligned}
\Gamma _1={}&-c_1\int \nabla Z*\chi\nabla\Phi*U\\
&-c_1\int Z*\nabla\chi*\nabla\Phi*U\\
&-c_1\int Z*\chi\nabla\Phi*\nabla U+L_m ,
\end{aligned}
\tag{1}
\]

其中 \(L_m\) 只含 \(\nabla^{\le m}\chi\)。

即使 \(\Gamma _2,\Gamma _3\) 的精确系数恰好消去 (1) 后两项，仍留下

\[
-c_1\int \nabla Z*\chi\nabla^{m+1}\chi*U.
\tag{2}
\]

由于

\[
|\nabla Z|\le C_p|W|^{p-2}|\nabla W|,
\]

Young 不等式给出

\[
\begin{aligned}
|(2)|
\le{}&
\varepsilon\int \chi^2|\nabla W|^2|W|^{p-2}\\
&+C_{p,\varepsilon}
\int |U|^2|\nabla^{m+1}\chi|^2|W|^{p-2}.
\end{aligned}
\tag{3}
\]

第一项由扩散控制；第二项仍需要当前截断阶
\(\nabla^{m+1}\chi\)。若再对 (2) 分部积分，就会产生
\(\nabla^2Z\)，而能量只控制 \(\nabla W\)，故该方法不能继续降阶。

相比之下，对剩余的 \(Z\)-层面项再分部积分确实得到 Wang 所说的残项。例如

\[
\begin{aligned}
\int Z*\nabla\chi*\nabla\Phi*U
={}&-\int\nabla Z*\nabla\chi*\Phi*U\\
&-\int Z*\nabla^2\chi*\Phi*U\\
&-\int Z*\nabla\chi*\Phi*\nabla U+L_m ,
\end{aligned}
\]

其中第二项正是

\[
-\int Z*\nabla^2\chi*\nabla^m\chi*U.
\]

所以 Wang 的残项并非错误，而是**不完整**：它没有处理 (2)。不存在仅靠 \(\Gamma _1,\Gamma _2,\Gamma _3\) 的系数匹配消去 (2) 的机制；要消去它，必须另有精确项

\[
+c_1\int\nabla Z*\chi\nabla^{m+1}\chi*U,
\]

而所列演化项、扩散积分、\(\Gamma _4\) 和 \(G\)-反应项都不产生这一项。

---

## 2. 最高 Hessian 通道不是可消去的 schematic artifact

定义

\[
\mathcal K(H,S)_{ijkl}
=
H_{ik}S_{jl}+H_{jl}S_{ik}
-H_{il}S_{jk}-H_{jk}S_{il}.
\]

在给定曲率约定下，\(T\) 方程中 Hessian-\(a\) 部分为

\[
[(\partial_t-a\Delta)T]_{\nabla^2a}
=
-\mathcal K(\nabla^2a,\operatorname{Ric}T).
\]

因为 \(U=aT\)，重写扩散后 \(U\) 方程的完整 Hessian 通道是

\[
\boxed{
[(\partial_t-a\Delta)U]_{\nabla^2a}
=
-\mathcal K(\nabla^2a,\operatorname{Ric}U)
-(\Delta a)U.
}
\tag{4}
\]

这说明两件事：

1. 所有这些项均含 \(U\)，故 shift 后没有独立的
   \(\nabla^2a*G\) 强迫源；
2. 该线性算子并不恒为零，故不能依赖未写出的代数消去来移除最高截断导数。

又因为

\[
\nabla^{m+2}(\chi^2)
=
2\chi\nabla^{m+2}\chi
+2(m+2)\operatorname{Sym}
  (\nabla\chi\otimes\nabla^{m+1}\chi)
+\{\nabla^{\le m}\chi\},
\tag{5}
\]

真正最高通道中的 \(\chi\nabla^{m+2}\chi\) 系数来自精确因子 \(2\)，并通过 (4) 的非零算子作用于 \(U\)。这里单个 \(\chi=\sqrt a\) 正是 (3) 中匹配扩散权重 \(a=\chi^2\) 的关键，而不是可忽略的 schematic 系数。

---

## 3. 当前阶 Volterra 闭合

有精确恒等式

\[
aE=a(\operatorname{Ric}+g)=\operatorname{Ric}(U).
\]

若 \(S=\operatorname{Ric}(U)\)，则 \(\partial_tg=-2S\)，连接变分为

\[
\partial_t\Gamma^k_{ij}
=
-g^{k\ell}
\bigl(
\nabla_iS_{j\ell}
+\nabla_jS_{i\ell}
-\nabla_\ell S_{ij}
\bigr).
\tag{6}
\]

因此 \(\partial_t\nabla^{m+1}\chi\) 的最高项是

\[
\nabla^mS*\nabla\chi
=
\operatorname{Ric}(\nabla^mU)*\nabla\chi,
\]

从而在低阶量已控制后，

\[
\|\nabla^{m+1}\chi(t)\|_{L^p}
\le C+C\int_0^t
\bigl(1+\|\nabla^mU(s)\|_{L^{p_1}}\bigr)\,ds.
\tag{7}
\]

另一方面，(3) 及其余能量项给出有限 staggered 指数族上的

\[
X_m'(t)\le C(1+X_m(t)+H_m(t)),
\]

其中可取

\[
X_m\sim \sum_p\|\nabla^mU\|_{L^p}^2,
\qquad
H_m\sim \sum_p\|\nabla^{m+1}\chi\|_{L^p}^2.
\]

由 (7) 和时间方向 Cauchy–Schwarz，

\[
H_m(t)\le C+C\int_0^tX_m(s)\,ds,
\]

故

\[
\boxed{
X_m'(t)\le
C\left(1+X_m(t)+\int_0^tX_m(s)\,ds\right).
}
\tag{8}
\]

这正是所需的当前阶 Volterra 闭合。Wang 的 \(m=1\) 基础情形实际上已经展示了同一机制：\(\nabla U\) 与 \(\nabla^2\chi\) 联立估计；高阶没有新的消去使这一配对消失。

---

## 4. 正确的 shifted induction 顺序

在第 \(m\) 层开始时，应已有

\[
\nabla^jU\ (j\le m-1),\qquad
\nabla^r\chi\ (r\le m),\qquad
\nabla^jT\ (j\le m-1)
\]

的所需有限 \(L^p\) 估计。等价地，可把
\(\nabla^{m-1}T\) 看作上一层结束时已经取得；若单独列出当前层操作，则顺序为：

1. **先确保 \(\nabla^{m-1}T\)**：其原始最高项为
   \(\chi\nabla^{m+1}\chi*T\)，一次分部积分后只需要
   \(\nabla^m\chi\)。

2. **联合估计当前 weighted pair**
   \[
   \boxed{\nabla^mU\quad\text{与}\quad\nabla^{m+1}\chi}
   \]
   使用 (3)、(7)、(8)。

3. **再估计当前 unweighted curvature**
   \[
   \nabla^mT.
   \]
   它的最高项一次分部积分后需要
   \(\nabla^{m+1}\chi\)，此时已由第 2 步得到。

4. **Sobolev 升级**：利用相邻导数阶及 \(p>n\) 的估计得到所需
   \(L^\infty\) 控制。

因此 Step 27 中应保留的依赖图是

\[
\boxed{
\nabla^mU\leftrightarrow\nabla^{m+1}\chi,
\qquad
\nabla^{m-1}T\ \text{只需}\ \nabla^m\chi.
}
\]

---

## 5. shift 中必须明确保留的精确事实

不能只写成无系数的星号而寄望于未知消去：

- \(\nabla G=0\)，故 \(r\ge1\) 时
  \(\nabla^rT=\nabla^r\mathrm{Rm}\)；
- \(\operatorname{Ric}(G)=g\)，故
  \(aE=\operatorname{Ric}(U)\)；
- \(\partial_tG\) 仅代数依赖于 \(U,g\)，不产生截断导数；
- \(T=0\) 时 \(E=0\)，反应项在 \(T=0\) 消失，因此没有独立常数源；
- \(a=\chi^2\) 给出 (5) 的最高系数 \(2\)，以及
  \[
  \frac{da\otimes da}{a}=4\,d\chi\otimes d\chi
  \]
  的跨越 \(\{a=0\}\) 的光滑延拓；
- \(aG*U\) 的 \(m\) 次微分至多含 \(\nabla^m\chi\) 和当前
  \(\nabla^mU\)，不会引入 \(\nabla^{m+1}\chi\) 以上的新阶数。

**最终判定：** Wang Proposition 4.14 的 printed \(m\)-only cutoff dependency 未由其 lines 622–659 证明；高阶证明必须隐式补入与基础情形相同的
\(\nabla^mU\leftrightarrow\nabla^{m+1}\chi\) Volterra 联立闭合。Step 27 的当前阶配对在机制上正确，但其正文中“分部积分后不再留下该阶截断导数”之类表述应改为：最高 \(m+2\) 阶降到 \(m+1\) 阶，而 \(m+1\) 阶由当前 Volterra 配对控制。