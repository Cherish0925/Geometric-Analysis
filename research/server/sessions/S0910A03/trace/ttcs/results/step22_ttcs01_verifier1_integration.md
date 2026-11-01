# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 22,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step22_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step22_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following claims about the normalized cutoff flow in 4 dimensions:

1. INVERSE-SQUARE COUNTEREXAMPLE: The Hardy potential V = κ/|x|² on R⁴ with 0 < κ < 1 satisfies the form bound ∫Vφ² ≤ κ∫|∇φ|² (small form perturbation), but the heat semigroup e^{t(Δ+V)} does NOT have a uniform L²→L∞ bound. Verify that σ = 1-√(1-κ) > 0 gives the singular ground state r^{-σ} ∈ L² \ L∞.

2. SUBCRITICAL UPGRADE: In 4D, n/2 = 2 is the critical Sobolev exponent. A potential in L² gives only a form bound (critical, possibly non-ultracontractive). A potential in L³ gives form-relative bound zero (subcritical), allowing standard Moser iteration with convergent constants. Verify that the Wang hierarchy H₃(t) ≤ Cγ³/t provides exactly this subcritical upgrade at positive time.

3. SOBOLEV VARIABLE: For v = ηχF with a=χ², check that |∇v|² = η²a|∇F|² + |∇χ|²F² + a F²|∇η|² + cross terms, and that |∇a|²/a = 4|∇χ|² is bounded. Verify that this means the gradient of the Sobolev variable is controlled by the dissipation D₂ = ∫η²a|∇F|² plus lower-order terms.

4. CAUCHY-SCHWARZ FACTORING: H₃ = ∫η²aF³ ≤ H₂^{1/2} · (∫η²a²F⁴)^{1/2}. The second factor requires an OUTER cutoff. Verify that the finite-neighbor graph system handles this, and that the critical Sobolev product β = A₀²||F||₂ = C√ε_Li controls the absorption.

5. TRANSCRIPTION: The correct quadratic form is ε_t[φ] = ∫|∇(a^{-1/2}φ)|²dμ, NOT ∫|∇(a⁻¹φ)|²dμ. The former has leading weight a⁻¹ near the gradient, the latter a⁻². Verify that the a⁻¹/² version matches the conformal Sobolev substitution u = a^{-1/2}φ.

## Integrated Scientific Memo

# 核验结论

五项主张的核心机制基本正确，但须作若干重要修正。尤其：

- Hardy 例子确实否定“相对型小扰动自动推出 \(L^2\to L^\infty\) 超收缩”；
- 真正进入正时间 Moser 闭合的是
  \[
  A_0^4H_3(t)\lesssim \frac{\gamma^3}{t},
  \]
  而非无条件省略 \(A_0^4\) 的 \(H_3\) 估计；
- 外层 cutoff 的局部代数正确，但完整有限邻居图闭合尚未由材料证明；
- 正确二次型确为 \(a^{-1/2}\)，但 Step 22 对其零阶奇异项少写了一次 \(a^{-1}\)。

## 1. 逆平方反例：成立，但“\(r^{-\sigma}\in L^2(\mathbb R^4)\)”须改为局部陈述

令
\[
L=\Delta+\frac{\kappa}{r^2},\qquad 0<\kappa<1.
\]
四维 Hardy 不等式给出
\[
\int_{\mathbb R^4}\frac{\kappa}{r^2}\phi^2
 \le \kappa\int_{\mathbb R^4}|\nabla\phi|^2,
\]
故 \(-L=-\Delta-\kappa r^{-2}\) 的相对型系数为 \(\kappa<1\)。

对 \(u=r^{-\alpha}\)，
\[
Lu=\bigl[\kappa-\alpha(2-\alpha)\bigr]r^{-\alpha-2},
\]
所以
\[
\alpha_\pm=1\pm\sqrt{1-\kappa},\qquad
\sigma:=\alpha_-=1-\sqrt{1-\kappa}\in(0,1).
\]
原点附近
\[
\int_{B_1}r^{-2\sigma}\,dx
=|\mathbb S^3|\int_0^1r^{3-2\sigma}\,dr<\infty,
\]
且
\[
\int_{B_1}|\nabla r^{-\sigma}|^2dx
\asymp\int_0^1r^{1-2\sigma}\,dr<\infty,
\]
但 \(r^{-\sigma}\to\infty\)。因此
\[
r^{-\sigma}\in L^2_{\mathrm{loc}}\setminus L^\infty_{\mathrm{loc}}.
\]

它并不属于全局 \(L^2(\mathbb R^4)\)，因为无穷远处衰减不足。全局算子反例可由 ground-state transform 得到：
\[
L(r^{-\sigma}w)
=r^{-\sigma}\left(w_{rr}+\frac{3-2\sigma}{r}w_r\right)
\]
（径向情形）。若 \(f\ge0\) 是非零光滑径向环带支撑函数，则对任意 \(t>0\)，变换后的热解在 \(r=0\) 有严格正有限极限，故
\[
e^{tL}f(r)\sim c_t r^{-\sigma},\qquad c_t>0.
\]
于是 \(e^{tL}f\in L^2\setminus L^\infty\)，所以不存在有界
\[
e^{tL}:L^2\longrightarrow L^\infty .
\]

应同时修正：

1. 不能声称“任意非零 \(L^2\) 初值”都产生该奇性；正的非零径向初值已经足够，带符号数据可能消去首项。
2. \(V=\kappa r^{-2}\) 是 weak-\(L^2\) 临界势，而非 strong \(L^2\)：
   \[
   \int_{B_1}V^2dx\asymp\int_0^1\frac{dr}{r}=\infty.
   \]
   该例严格反驳的是“型小性本身推出超收缩”，而不是“每个 strong-\(L^2\) 势都失败”。
3. 热核的尺度兼容形式应写为
   \[
   p_t(x,y)\sim t^{-2}
   \left(\frac{|x|}{\sqrt t}\right)^{-\sigma}
   \left(\frac{|y|}{\sqrt t}\right)^{-\sigma}\Phi,
   \]
   若直接提出 \(|x|^{-\sigma}|y|^{-\sigma}\)，前因子相应为 \(t^{-2+\sigma}\)。

## 2. \(L^3\) 次临界升级：条件性成立

四维势的临界指数是 \(n/2=2\)，函数 Sobolev 指数为 \(4\)。若
\[
\|\phi\|_4^2\le A_0^2\mathfrak e[\phi],
\]
则 strong-\(L^2\) 势只直接给出固定系数
\[
\int |V|\phi^2
\le A_0^2\|V\|_2\,\mathfrak e[\phi].
\]
这不足以仅凭一个统一小系数控制整个无限次幂迭代。

若 \(V\in L^3\)，则
\[
\int |V|\phi^2
\le \|V\|_3\|\phi\|_3^2
\le \|V\|_3\|\phi\|_2^{2/3}\|\phi\|_4^{4/3},
\]
故对任意 \(\varepsilon>0\)，
\[
\int |V|\phi^2
\le \varepsilon\mathfrak e[\phi]
 +C\varepsilon^{-2}A_0^4\|V\|_3^3\|\phi\|_2^2.
\tag{1}
\]
这正是 form-relative bound zero；令 \(\varepsilon\) 随 Moser 指数按多项式衰减，只产生多项式指数损失，沿几何增长的幂序列其乘积收敛。

取
\[
\mathcal K=aF,\qquad d\nu=a^{-2}d\mu.
\]
则
\[
\|\mathcal K\|_{L^3(\nu)}^3
=\int aF^3\,d\mu=H_3.
\]
但 Step 20 实际给出的正规化量是
\[
\boxed{A_0^4H_3(s)\le \frac{C\gamma^3}{s}}.
\tag{2}
\]
因此在 \(s\in[t/2,t]\) 上，由 (1)–(2)
\[
\int\mathcal K\phi^2\,d\nu_s
\le \varepsilon\mathfrak e_s[\phi]
+C\varepsilon^{-2}\frac{\gamma^3}{t}
 \|\phi\|_{L^2(\nu_s)}^2.
\]
这就是所需的正时间次临界升级。

脚本中通过
\[
\frac1{r_k}=\frac12-\frac1{q_k}
\]
论证“\(L^3\) 覆盖所有 \(r_k\)”并不正确：\(r_k\to2\) 是从上方，且从 \(q_0=2\) 开始有
\[
r_0=\infty,\quad r_1=4,\quad r_2=\frac83.
\]
在可能为无限测度的 \((\Omega,\nu)\) 上，也不能直接用 \(L^3\subset L^{r_k}\)。正确论证是上面的固定 \(L^3\) 插值估计。

此外，材料尚未完整证明 normalized cutoff flow 下的 (2)：精确张量能量式、演化测度、\(a=0\) 正则化及有限邻居组装仍是未闭合部分。因此该项是“若 Wang 层级给出 (2)，则恰好完成临界到次临界升级”。

## 3. Sobolev 变量：成立，精确恒等式须保留 \(\eta^2\)

对
\[
v=\eta\chi F,\qquad a=\chi^2,
\]
有
\[
\nabla v=\eta\chi\nabla F+\eta F\nabla\chi+\chi F\nabla\eta,
\]
从而
\[
\begin{aligned}
|\nabla v|^2={}&
\eta^2a|\nabla F|^2
+\eta^2F^2|\nabla\chi|^2
+aF^2|\nabla\eta|^2\\
&+2\eta^2\chi F\langle\nabla F,\nabla\chi\rangle
+2\eta aF\langle\nabla F,\nabla\eta\rangle\\
&+2\eta\chi F^2\langle\nabla\chi,\nabla\eta\rangle .
\end{aligned}
\]
题文第二个平方项漏了 \(\eta^2\)；若 \(0\le\eta\le1\)，去掉它仍可作为上界。

Young 不等式给出
\[
|\nabla v|^2\le C\left(
\eta^2a|\nabla F|^2
+\eta^2F^2|\nabla\chi|^2
+aF^2|\nabla\eta|^2\right).
\]
而
\[
\frac{|\nabla a|^2}{a}
=\frac{|2\chi\nabla\chi|^2}{\chi^2}
=4|\nabla\chi|^2,
\]
在零集处按该右端延拓。若 cutoff 梯度为 \(O(r^{-1})\)，则
\[
\int|\nabla v|^2
\le C D_2
+Cr^{-2}\int_{\operatorname{supp}\eta_{\rm out}}F^2,
\qquad
D_2=\int\eta^2a|\nabla F|^2.
\]
故所述 dissipation 控制成立。

## 4. Cauchy–Schwarz 与外层 cutoff：局部机制成立，完整图系统仍待证明

必须固定约定
\[
H_q=\int\eta^2a^{q-2}F^q\,d\mu
=\int\eta^2\mathcal K^q\,d\nu .
\]
于是
\[
H_2=\int\eta^2F^2,\qquad
H_3=\int\eta^2aF^3,
\]
且
\[
H_3\le
H_2^{1/2}
\left(\int\eta^2a^2F^4\right)^{1/2}.
\tag{3}
\]

不能直接对同一 \(\eta\) 使用 Sobolev，因为它只产生
\[
\int\eta^4a^2F^4,
\]
而 \(\eta^4\) 在过渡区不能控制 \(\eta^2\)。取外层 cutoff
\(\widetilde\eta\equiv1\) 于 \(\operatorname{supp}\eta\)，则
\[
\left(\int\eta^2a^2F^4\right)^{1/2}
\le \|\widetilde\eta\chi F\|_4^2
\le CA_0^2
 \left(D_{2,\widetilde\eta}
       +r^{-2}H_{2,\widetilde\eta}\right).
\]
因此
\[
H_{3,\eta}\le
C\beta_{\rm out}
\left(D_{2,\widetilde\eta}
+r^{-2}H_{2,\widetilde\eta}\right),
\qquad
\beta_{\rm out}=A_0^2\|F\|_{L^2(U_{\rm out})}.
\tag{4}
\]
在 Li 尺度上
\[
\beta_{\rm out}\lesssim r^2\sqrt{K_F}
\lesssim \sqrt{\varepsilon_{\rm Li}},
\]
故足够小时可吸收外层 dissipation。若 \(F=(1+|\mathrm{Rm}|^2)^{1/2}\)，则一般还要保留 Step 20 指出的 \(Cr^2\) 项，或用 \(K_F\) 定义 Li 尺度；初始近负 Einstein 切片上 \(F\lesssim|\mathrm{Rm}|\) 时二者可比较。

若外层邻居图的度数至多为 \(N\)，则
\[
E_\alpha'+cD_\alpha
\le C\beta_*\sum_{\rho\sim\alpha}D_\rho+\mathrm{LOT}
\]
求和后成为
\[
\sum_\alpha E_\alpha'
+(c-CN\beta_*)\sum_\alpha D_\alpha
\le\mathrm{LOT}.
\]
因此 \(CN\beta_*<c/2\) 时，图吸收的代数机制正确。

但现有材料尚未共同构造完整的 nested cutoff family、邻接权重及精确 normalized-flow 张量不等式。因此“有限邻居系统处理了它”只能核验为可行机制，不能核验为已经完成的证明。

另须区分
\[
\|v\|_2^2=\int\eta^2aF^2
\quad\text{和}\quad
H_2=\int\eta^2F^2.
\]
前者不等于后者；仅因 \(0\le a\le1\) 才有 \(\|v\|_2^2\le H_2\)。

## 5. 二次型转录：\(a^{-1/2}\) 正确，但展开式需修正

由于
\[
d\nu=a^{-2}d\mu,
\]
有
\[
\|\phi\|_{L^4(\nu)}^2
=\left(\int a^{-2}\phi^4\,d\mu\right)^{1/2}
=\|a^{-1/2}\phi\|_{L^4(\mu)}^2.
\]
故 Sobolev 代换必为
\[
u=a^{-1/2}\phi,
\]
相应梯度型为
\[
\int\left|\nabla(a^{-1/2}\phi)\right|^2d\mu,
\]
而不是 \(\int|\nabla(a^{-1}\phi)|^2\)。

精确展开为
\[
\begin{aligned}
|\nabla(a^{-1/2}\phi)|^2
={}&a^{-1}|\nabla\phi|^2
-a^{-2}\phi\langle\nabla a,\nabla\phi\rangle
+\frac14a^{-3}|\nabla a|^2\phi^2,\\
|\nabla(a^{-1}\phi)|^2
={}&a^{-2}|\nabla\phi|^2
-2a^{-3}\phi\langle\nabla a,\nabla\phi\rangle
+a^{-4}|\nabla a|^2\phi^2.
\end{aligned}
\]
因此领先梯度权分别为 \(a^{-1}\) 与 \(a^{-2}\)，主结论正确；但 Step 22 把第一式零阶项写成 \(O(a^{-2}|da|^2\phi^2)\)，少了一次 \(a^{-1}\)。利用
\[
|\nabla a|^2=4a|\nabla\chi|^2,
\]
正确零阶项是
\[
\frac14a^{-3}|\nabla a|^2\phi^2
=a^{-2}|\nabla\chi|^2\phi^2.
\]
它是真实的 conformal-Hardy 奇异项，并非完全“无隐藏奇性”。不过当
\[
\phi=\eta\mathcal K=\eta aF
\]
时，
\[
a^{-1/2}\phi=\eta\chi F=v,
\]
该项退化为正常的 cutoff 下阶项，正好与第 3 项的估计一致。

最后，原始 Sobolev 下阶质量项精确变为
\[
r^{-2}\int a^{-1}\phi^2\,d\mu
=r^{-2}\int a\phi^2\,d\nu
\le r^{-2}\|\phi\|_{L^2(\nu)}^2.
\]
所以 Step 22 所写 \(L^2(\nu)\) 项是合法放大，不是精确恒等式。

## 总体判定

- **第 1、3、5 项：** 经上述精确修正后成立。
- **第 2 项：** \(A_0^4H_3\lesssim\gamma^3/t\) 确实给出所需 \(L^3\) 次临界势估计；但该 \(H_3\) 界在 supplied materials 中仍是条件性输入。
- **第 4 项：** Cauchy–Schwarz、外层 cutoff 和 bounded-degree 图吸收代数成立；完整 normalized cutoff flow 的有限邻居实现尚未完成。

由此可严格确认的结构结论是：临界型小性不能替代 \(H_2\to H_3\) 步骤；一旦该步骤以正规化形式
\[
A_0^4H_3(t)\lesssim\gamma^3/t
\]
建立，正时间 \(L^3\) 次临界 Moser 闭合具有收敛常数。当前真正未决对象仍是产生此界的精确局部张量能量不等式及其有限邻居、演化测度和 \(a=0\) 正则化组装。