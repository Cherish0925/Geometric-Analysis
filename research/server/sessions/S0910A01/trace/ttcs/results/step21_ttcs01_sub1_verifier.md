# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step21_finite_exponent_smoothing_lemma.md",
    "Sessions/S0910A01/workspace/scripts/step21_finite_exponent_smoothing.py",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md"
  ]
}
```

## Task

Verify the conditional finite-exponent smoothing lemma for the four-dimensional normalized cutoff flow ∂_t g = -2χ²(Ric+g). The construction claims four steps on each Whitney ball B_ℓ(y) with ℓ=crχ₀:

1. q=2 energy estimate with critical absorption (γ = Cr²√(1+K₀) small) giving time-uniform L² and integrated gradient L².
2. Parabolic Sobolev embedding in n=4 spatial dimensions: p* = 2(n+2)/n = 3, converting L^∞_t L² ∩ L²_t H¹ to spacetime L³.
3. q=3 power inequality with a time cutoff φ(t)=0 for t<δ, φ=1 for t≥2δ: the time-cutoff source is controlled by the spacetime L³ from Step 2, producing time-uniform spatial L³ on [2δ,T].
4. Stampacchia/Moser local boundedness: since L³_spatial is supercritical (3 > n/2 = 2 for n=4), the standard parabolic regularity gives F = (1+|Rm|²)^{1/2} ≤ C on an inner ball.

Specific questions to check:
(a) Is the BG energy transfer in Section 3 correct: ℓ⁴ fint|Rm|² ≤ CK₀r⁴ with χ₀ canceling exactly?
(b) In the Sobolev absorption at q=2, does the factor a₀ cancel on both sides, making the threshold γ-independent of χ₀?
(c) For q=3, is the chain-rule coefficient (3/2)² = 9/4, and does the same γ threshold work?
(d) Is the parabolic interpolation exponent 2(n+2)/n = 3 correct for n=4?
(e) For Step D, is L³_spatial supercritical for the Stampacchia theory? The standard condition is V ∈ L^p with p > n/2 = 2 for spatial dimension n=4. Since the potential V = CaF has F ∈ L³ uniformly in time, V ∈ L³ with 3 > 2.
(f) Is the bootstrap closure in Section 13 logically consistent: does the curvature bound feed back to preserve metric comparability, Sobolev persistence, and energy bounds?

## Output

# 科学核验备忘录

## 总结

六个问题中：

- **(a)** \(\chi _0\) 的幂次消去是正确的，但不同球心之间的 Bishop–Gromov 比较需改写，且常数依赖所用尺度的统一上界。
- **(b)** \(a_0\) 在 \(q=2\) 吸收中确实消去；不过所需的是当前时刻的局部 \(L^2\) 曲率量，而非仅初始时刻的 \(\gamma\)。
- **(c)** \((3/2)^2=9/4\) 正确；\(q=2,3\) 可共用同一个充分小的初始参数，但数值阈值应取两个固定指数所需阈值的较小者。
- **(d)** 四维抛物 Sobolev 指数 \(2(n+2)/n=3\) 正确。
- **(e)** \(p>n/2\) 以及 \(3>2\) 正确；但文稿的抛物缩放漏掉了 \(\ell^2\)，所以 Step D 实际控制的是 \(\ell^2F\)，并不能得到与 \(\chi _0\) 无关的 \(F\) 本身。
- **(f)** Section 13 尚未形成闭合推导。度量漂移、当前 \(L^2\) 小量和最初短时间段仍需额外估计。

因此，固定指数路线本身具有可行结构，但当前 Lemma 的第 3、4 项及其 \(\chi _0\)-无关结论没有由所写计算推出。

---

## 1. Bishop–Gromov 转移

设 \(d(p,y)<4r\)、\(\ell=cr\chi _0<r\)。则
\[
B_\ell(y)\subset B_{5r}(p),\qquad B_{5r}(p)\subset B_{9r}(y).
\]
若 \(\operatorname{Ric}_{g_0}\ge-3g_0\)，Bishop–Gromov 在球心 \(y\) 给出
\[
\frac{\operatorname{Vol}B_\ell(y)}
     {\operatorname{Vol}B_{9r}(y)}
\ge
\frac{v_{-1}(\ell)}{v_{-1}(9r)}.
\]
在 \(r\le \bar r\) 的固定小尺度上，
\[
\frac{v_{-1}(\ell)}{v_{-1}(9r)}
\ge C(\bar r)\left(\frac{\ell}{9r}\right)^4.
\]
结合 \(B_{5r}(p)\subset B_{9r}(y)\) 与 H1，
\[
\begin{aligned}
\ell^4\fint_{B_\ell(y)}|\operatorname{Rm}_0|^2
&\le
\ell^4K_0\frac{\operatorname{Vol}B_{5r}(p)}
                  {\operatorname{Vol}B_\ell(y)}  \\
&\le CK_0r^4.
\end{aligned}
\]
因此 \(\ell^4=(cr\chi _0)^4\) 与体积比中的 \(\ell^{-4}\) 精确消去，**(a) 的核心结论成立**。文稿中直接写成
\[
\operatorname{Vol}B_\ell(y)\ge c_{\rm BG}
(\ell/5r)^4\operatorname{Vol}B_{5r}(p)
\]
并非同球心的直接公式；用 \(9r\) 即可严密补全。

对 \(F_0^2=1+|\operatorname{Rm}_0|^2\)，相应地
\[
\ell^4\fint_WF_0^2\le Cr^4(1+K_0).
\]
若相对 Sobolev 常数满足
\[
A_W^2\le C\ell^2\operatorname{Vol}(W)^{-1/2},
\]
则
\[
A_W^2\|F_0\|_{L^2(W)}
\le C\bigl(\ell^4\fint_WF_0^2\bigr)^{1/2}
\le Cr^2\sqrt{1+K_0}.
\]

不过 H1 只给出
\[
\int_WF_0^2\le \operatorname{Vol}(W)+K_0\operatorname{Vol}B_{5r}(p),
\]
不能推出文稿 (5.2) 所写的
\[
\int_WF_0^2\le C(1+K_0)\operatorname{Vol}(W).
\]
当 \(\chi _0\to0\) 时，两球体积之比可为 \(O(\chi _0^{-4})\)。

---

## 2. \(q=2\) 与 \(q=3\) 的吸收

在 Whitney 球上 \(a\simeq a_0\)，故
\[
\begin{aligned}
\int \eta^2aF^3
&\le Ca_0\|F(t)\|_2\|\eta F\|_4^2\\
&\le C\gamma_W(t)\left[
 \int a|\nabla(\eta F)|^2+
 \ell^{-2}\int a(\eta F)^2\right],
\end{aligned}
\]
其中
\[
\gamma_W(t)=A_W^2\|F(t)\|_{L^2(W)}.
\]
主耗散同样含 \(a\simeq a_0\)，所以吸收阈值中不出现 \(a_0\)。**(b) 的代数消去正确。**

关键缺口是：H2 的双 Lipschitz 度量比较和 H3 的 Sobolev 持续性都不能控制 \(\operatorname{Rm}(t)\)，因为曲率涉及度量的二阶导数。因此文稿中

> “By (H2)–(H3), the same bound holds at time \(t\)”

不成立。吸收需要一个关于当前
\(\gamma_W(t)\) 的首次越出假设，再由 \(q=2\) 能量不等式改进该假设。对应输出应形如
\[
Y_{\rm inner}(t)+D(t)
\le Ce^{Ct/r^2}Y_{\rm outer}(0),
\]
而不是直接使用 \(C(1+K_0)\operatorname{Vol}(W)\)。

在 \(q=3\) 时，
\[
\nabla(F^{3/2})=\frac32F^{1/2}\nabla F,\qquad
|\nabla(F^{3/2})|^2=\frac94F|\nabla F|^2.
\]
所以 **(c) 中 \(9/4\) 正确**。实际吸收常数还含 Sobolev 常数、张量能量常数和空间截断常数；可取
\[
\varepsilon_0\le \min\{\varepsilon_{q=2},\varepsilon_{q=3}\}.
\]
脚本中人为选取的 \(0.1\) 不能确定这一数值。

---

## 3. 抛物 Sobolev 指数与正确缩放

四维中
\[
\frac{2(n+2)}n=3,
\]
且
\[
\int_0^T\!\!\int |u|^3
\le
CA_W^2
\left(\sup_t\int u^2\right)^{1/2}
\int_0^T\left(\int|\nabla u|^2+\ell^{-2}\int u^2\right)dt.
\]
所以 **(d) 正确**。在可能塌缩的球上，不能省略 \(A_W^2\) 或其等价的归一化平均形式；“uniform geometry”并不由 H2 单独给出。

更严重的是 Sections 4、6、7 的缩放不一致。自然的抛物缩放为
\[
\widetilde g=\ell^{-2}g,\qquad
\widetilde t=\frac{a_0t}{\ell^2},\qquad
\mathcal F=\ell^2F.
\]
于是
\[
d\widetilde\mu=\ell^{-4}d\mu,\qquad
d\widetilde t=\frac{a_0}{\ell^2}dt,
\]
以及
\[
\int\mathcal F^3\,d\widetilde\mu\,d\widetilde t
=a_0\int F^3\,d\mu\,dt,
\qquad
\int\mathcal F^3\,d\widetilde\mu
=\ell^2\int F^3\,d\mu.
\]
文稿同时使用“\(F\) 不变”和 \(d\widetilde\mu=\ell^{-4}d\mu\)，并在 Section 6 将
\(d\widetilde t=(a_0/\ell^2)dt\) 反向算成 \(\ell^2/a_0\)。因此 (6.3) 及其向原变量的转换不正确。

例如，若正确的缩放后估计是
\[
\sup_{\widetilde t}\int\mathcal F^3d\widetilde\mu
\le \frac C{\widetilde\delta},
\]
则
\[
\sup_t\int F^3d\mu
\le\frac{C}{\ell^2\widetilde\delta}
=\frac{C}{a_0\delta},
\]
而不是 Section 7 中的
\[
\frac{Cc^2r^2}{\delta}\,\ell^4.
\]

---

## 4. Stampacchia/Moser 步骤

对
\[
u_t-\operatorname{div}(A\nabla u)\le Vu
\]
且 \(V\in L^\infty_tL^p_x\)，条件 \(p>n/2\) 确实允许局部有界性。四维中 \(3>2\)，所以 **(e) 的抽象正则性事实成立**。

但原曲率不等式缩放后，其势项是
\[
\widetilde V
=C\ell^2\frac a{a_0}F
=C\frac a{a_0}\mathcal F,
\]
不是文稿写的 \(C\widetilde aF\)。所需输入是
\[
\sup_{\widetilde t}
\left(\fint_{\widetilde B}|\ell^2F|^3d\widetilde\mu\right)^{1/3}
\le C,
\]
尤其在塌缩情形中应使用归一化平均与 H3 的相对 Sobolev 常数。

由此得到的自然结论是
\[
\ell^2F\le C,
\]
即
\[
F\le\frac C{\ell^2}
=\frac{C}{c^2r^2\chi _0^2},
\qquad
aF\le\frac C{c^2r^2}.
\]
因此 Step D 不能推出与 \(\chi _0\) 无关的未加权曲率界。Section 10 中
\[
a|\operatorname{Rm}|=\chi _0^2C_4\to0
\]
也随之失去依据；正确缩放只给出 \(a|\operatorname{Rm}|\) 对 \(\chi _0\) 一致有界。

此外，曲率方程还含
\[
(\nabla a)*\nabla E,\qquad (\nabla^2a)*E.
\]
Step 20 通过分部积分处理了这些项，但 Section 8 的“\(+\text{lower}\)”尚未写成适用于截断函数的弱次解不等式。应用 Stampacchia 理论还需要把这些项写成散度形式，并验证缩放后的一阶系数一致有界。

---

## 5. Section 13 的闭合关系

**(f) 目前不成立。**

1. **Sobolev 持续性**：若 H2 已知，则固定局部区域上的相对 Sobolev不等式可定量传递；这一点合理。

2. **度量比较**：真正需要的是
   \[
   \int_0^T\|aE(t)\|_\infty\,dt<\infty,
   \qquad
   |\partial_tg|_g\le C|aE|.
   \]
   修正后的曲率结论在 \(t\gtrsim r^2\) 只给
   \[
   |aE|\lesssim r^{-2},
   \]
   在长度 \(O(r^2)\) 的区间上产生 \(O(1)\) 漂移，或在较小 \(\theta\) 下产生 \(O(\theta)\)，并非文稿所写的 \(O(r^2)\)。而且 Step D 不覆盖 \([0,3\delta]\)。

3. **当前 \(L^2\) 小量**：它应由 \(q=2\) 的连续性论证直接维持，不能先依赖由该小量推导出的点态曲率界。

4. **能量持续性**：正时间点态界可处理后半段时间，但最初短时间段仍需 \(q=2\) 临界吸收。仅说“曲率界反馈到平均能量”会形成循环。

5. **调和坐标**：一致曲率界本身不能在塌缩情形中给出一致调和半径；还需要体积半径、注入半径或适当覆盖空间上的替代输入。

一个与缩放相容的条件性结论应以
\[
\boxed{\ell^2F\le C}
\quad\text{或}\quad
\boxed{a|\operatorname{Rm}|\le Cr^{-2}}
\]
为最终输出，并把当前局部 \(L^2\) 小量纳入首次越出体系。随附 Python 脚本正确验证了指数 \(3\)、不等式 \(3>2\)、Whitney 时间比以及形式上的 \(\chi _0^4\) 消去，但没有编码上述曲率缩放、当前能量持续性、相对 Sobolev 体积因子或弱次解结构。