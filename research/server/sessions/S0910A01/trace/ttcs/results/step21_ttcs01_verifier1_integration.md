# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 21,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step21_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step21_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

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

## Integrated Scientific Memo

# 核验结论

当前四步方案的**指数结构是可行的**，但 `step21_finite_exponent_smoothing_lemma.md` 所声明的结论尚未证明。主要问题不是 \(q=2,3\) 的指数，而是：

1. 初始局部临界小量没有被严密传播为当前时刻的小量；
2. 抛物缩放中遗漏了曲率的长度维数；
3. Step D 最多自然给出 \(\ell ^2F\) 的界，而非与 \(\chi _0\) 无关的 \(F\) 界；
4. 曲率方程尚未被写成可直接应用 Stampacchia/Moser 的弱次解形式；
5. Section 13 的 bootstrap 因而没有闭合。

可保留的正确目标应是
\[
\ell ^2F\le C
\qquad\Longleftrightarrow\qquad
a|\Rm|\le Cr^{-2},
\]
而不是 \(F\le C\) 且常数与 \(\chi _0\) 无关。

---

## (a) Bishop–Gromov 转移

核心结论正确，但原文直接比较不同球心的 \(B_\ell(y)\) 与 \(B_{5r}(p)\) 不严密。

由 \(d(p,y)<4r\) 得
\[
B_{5r}(p)\subset B_{9r}(y).
\]
在固定上界 \(r\le \bar r\) 下，利用以 \(y\) 为球心的 Bishop–Gromov 比较，
\[
\frac{\Vol B_\ell(y)}{\Vol B_{9r}(y)}
\ge c(\bar r)\left(\frac{\ell}{9r}\right)^4.
\]
结合 H1，
\[
\begin{aligned}
\ell ^4\fint_{B_\ell(y)}|\Rm_0|^2
&\le
\ell ^4K_0
  \frac{\Vol B_{5r}(p)}{\Vol B_\ell(y)}\\
&\le CK_0r^4 .
\end{aligned}
\]
因此 \(\ell=cr\chi _0\) 中的 \(\chi _0^4\) 与体积比中的
\(\ell^{-4}\) **精确消去**。对 \(F_0^2=1+|\Rm_0|^2\)，
\[
\ell^4\fint_{B_\ell(y)}F_0^2\le Cr^4(1+K_0).
\]

但这只控制尺度不变量，并不推出原文 (5.2) 所需的
\[
\int_WF_0^2\le C(1+K_0)\Vol(W).
\]
事实上 H1 仅给出
\[
\int_W|\Rm_0|^2\le K_0\Vol B_{5r}(p),
\]
右侧与 \(\Vol(W)\) 的比可能是 \(O(\chi _0^{-4})\)。

**结论：(a) 成立，但 BG 证明和后续未归一化能量界必须修正。**

---

## (b) \(q=2\) 吸收中的 \(a_0\)

在 Whitney 球上 \(a\simeq a_0=\chi _0^2\)，故
\[
\begin{aligned}
\int \eta^2aF^3
&\le Ca_0\|F(t)\|_{L^2(W)}
              \|\eta F\|_{L^4(W)}^2\\
&\le Ca_0 A_W^2\|F(t)\|_2
 \left(\int|\nabla(\eta F)|^2
       +\ell^{-2}\int(\eta F)^2\right).
\end{aligned}
\]
而
\[
a_0\int|\nabla(\eta F)|^2
\lesssim \int a|\nabla(\eta F)|^2.
\]
因此吸收参数确为
\[
\gamma_W(t)=A_W^2\|F(t)\|_{L^2(W)},
\]
其中不含 \(a_0\)：**\(a_0\) 的代数消去正确，阈值与
\(\chi _0\) 无关。**

但原文错误地声称 H2–H3 可将初始 \(\gamma_W(0)\) 的界传到任意
\(t\)。双 Lipschitz 度量比较和 Sobolev 持续性不控制曲率，因为曲率含度量二阶导数。必须把
\[
\sup_{s\le t}A_W^2\|F(s)\|_2\le 2\varepsilon_0
\]
纳入首次越出假设，再由 \(q=2\) 能量不等式改进它；否则 Step A 的临界吸收是循环的。

**结论：(b) 的消去成立，但当前时刻小量尚未得到证明。**

---

## (c) \(q=3\) 链式法则

\[
\nabla(F^{3/2})=\frac32F^{1/2}\nabla F,
\qquad
|\nabla(F^{3/2})|^2=\frac94F|\nabla F|^2.
\]
所以 \(9/4\) 正确。\(q=2,3\) 可以共用一个充分小阈值，但应定义为
\[
\varepsilon_0\le
\min\{\varepsilon_{q=2},\varepsilon_{q=3}\},
\]
而不是将脚本中任意选择的 \(0.1\) 当作已证明阈值。

此外，非加权 \(q=3\) 计算在 Whitney 球上原则上可用，因为
\(a/a_0\) 一致可控；A03 的加权量
\[
H_3=\int \eta^2aF^3
\]
则更直接保持过渡区缩放。

**结论：(c) 成立，但仍依赖当前临界小量的首次越出闭合。**

---

## (d) 四维抛物插值

指数正确：
\[
p_*=\frac{2(n+2)}n=3\qquad(n=4).
\]
带相对 Sobolev 常数的正确局部形式是
\[
\int_0^T\!\!\int |u|^3
\le
CA_W^2
\left(\sup_t\int u^2\right)^{1/2}
\int_0^T
\left(\int|\nabla u|^2+\ell^{-2}\int u^2\right)dt.
\]
在塌缩球上不能省略 \(A_W\) 或改称“uniform geometry”；H2 本身并不提供非塌缩性。

原文 (6.2) 即使接受其 Step A 输入，体积幂也应是
\[
\Vol(W)^{3/2},
\]
而非 \(\Vol(W)^2\)。

**结论：(d) 成立；原文使用的局部 Sobolev常数及体积幂需修正。**

---

## 缩放审计：Step B–D 的决定性错误

自然的几何抛物缩放是
\[
\widetilde g=\ell^{-2}g,\qquad
\widetilde t=\frac{a_0t}{\ell^2},
\qquad
\mathcal F=\ell^2F.
\]
曲率不是无量纲量；原文“\(F\) does not change”与
\(d\widetilde\mu=\ell^{-4}d\mu\) 不能同时成立。正确关系为
\[
d\widetilde\mu=\ell^{-4}d\mu,\qquad
d\widetilde t=\frac{a_0}{\ell^2}dt,
\]
以及
\[
\int\mathcal F^3\,d\widetilde\mu\,d\widetilde t
=a_0\int F^3\,d\mu\,dt,
\]
\[
\int\mathcal F^3\,d\widetilde\mu
=\ell^2\int F^3\,d\mu.
\]

原文 Section 6 还把时间 Jacobian 方向算反；因此 (6.3)、Section 7 的反缩放以及最终未加权曲率界均不能由所写公式推出。

若正确的 Step C 给出
\[
\sup_{\widetilde t\ge2\widetilde\delta}
\int_{\widetilde B}\mathcal F^3\,d\widetilde\mu
\le \frac C{\widetilde\delta},
\]
则
\[
\sup_{t\ge2\delta}\int_BF^3\,d\mu
\le\frac{C}{\ell^2\widetilde\delta}
=\frac{C}{a_0\delta},
\qquad
\widetilde\delta=\frac{a_0\delta}{\ell^2}.
\]
这与 A03 的加权估计
\[
H_3(t)=\int aF^3\lesssim t^{-1}
\]
一致，而与 Step 21 中声称的未加权、\(\chi _0\)-一致 \(L^3\) 界不一致。

---

## (e) Stampacchia/Moser 步骤

抽象临界条件正确。若
\[
u_t-\operatorname{div}(A\nabla u)\le Vu,\qquad
V\in L^\infty_tL^p_x,
\]
则 \(p>n/2\) 是空间势的超临界条件；四维中
\[
3>\frac n2=2.
\]

但缩放后的曲率势不是 \(C\widetilde aF\)，而是
\[
\widetilde V
=C\ell^2\frac a{a_0}F
=C\frac a{a_0}\mathcal F.
\]
因此正确输入应是 \(\mathcal F=\ell^2F\) 的一致空间
\(L^3\) 控制，所得输出也是
\[
\boxed{\ell^2F\le C}.
\]
反缩放后
\[
F\le \frac C{\ell^2}
=\frac{C}{c^2r^2\chi _0^2},
\qquad
aF\le \frac C{c^2r^2}.
\]
所以 Step D 不能推出与 \(\chi _0\) 无关的 \(F\le C\)，也不能推出
\(a|\Rm|\to0\) 当 \(\chi _0\to0\)。

还有一个独立缺口：曲率方程含
\[
(\nabla a)*\nabla E,\qquad(\nabla^2a)*E.
\]
Step 20 只在积分能量中通过分部积分处理了这些项。要调用局部有界性定理，必须进一步证明一个弱次解不等式，例如把 Hessian 项改写为散度项，并验证缩放后的一阶系数一致有界。仅写“\(+\mathrm{lower}\)”不足以应用标准定理。Young 不等式可以吸收部分一阶项，但 \(\nabla^2a\) 没有在当前假设中被点态控制，且其弱形式需要明确陈述。

**结论：(e) 的指数判据正确，但 Step D 的具体应用和输出尺度错误。**

---

## (f) Section 13 的 bootstrap

目前不闭合。

### 1. Sobolev 持续性

若 H2 已经成立，则固定区域上的相对 Sobolev不等式可定量传递。这一箭头合理，但不能用来证明 H2。

### 2. 度量漂移

需要控制
\[
\int_0^T\|aE(t)\|_\infty\,dt.
\]
正确缩放输出仅给
\[
|aE|\lesssim r^{-2}
\]
（在正时间内），所以在 \(T=\theta r^2\) 上漂移为 \(O(\theta)\)，而不是原文的 \(O(r^2)\)。这可以通过选小 \(\theta\) 改善，但不会因 \(r\to0\) 自动变小。

同时 Step D 不覆盖 \([0,3\delta]\)，该初始时间层必须由独立短时间估计或首次越出假设处理。

### 3. 临界 \(L^2\) 小量

必须由 \(q=2\) 连续性/首次越出论证维持，不能先依赖由该小量推出的点态曲率界。原 Section 13 的“曲率界反馈到能量”会形成循环。

### 4. 调和坐标

在塌缩情形中，仅有曲率一致界并不能给出一致调和半径；还需要体积半径、注入半径，或在适当覆盖空间上的替代论证。

### 5. 后续导数估计

即使零阶修正完成，A03 指出的
\[
\chi a\,\nabla\Rm*U
\]
仍是独立的正时间 Bernstein 障碍。Whitney 缩放表明它不产生负的
\(\chi _0\) 幂，但系数按时间是临界的，不能从 \(t=0\) 直接 Gronwall。

---

# 可严格保留的修正版命题形态

在补充以下条件后：

1. 当前时刻局部临界量被纳入首次越出体系并由 \(q=2\) 估计改进；
2. 所有 Sobolev估计以相对常数或归一化平均书写；
3. 曲率方程被证明满足适合 Moser/Stampacchia 的弱次解不等式；
4. 正确使用 \(\mathcal F=\ell^2F\)；

固定指数路线应产生
\[
\sup_{\widetilde t\ge 2\widetilde\delta}
\|\mathcal F(\widetilde t)\|_{L^3(\widetilde B)}
\le C(\widetilde\delta),
\]
继而
\[
\boxed{
\sup_{\widetilde B'\times[3\widetilde\delta,\widetilde T]}
\mathcal F\le C(\widetilde\delta)
}
\]
，即
\[
\boxed{
\ell^2F\le C
\quad\text{或等价地}\quad
a|\Rm|\le Cr^{-2}.
}
\]

因此六问的最终判定为：

- **(a)** 是，修正非同心 BG 比较后成立；
- **(b)** 是，\(a_0\) 消去，但必须控制当前而非仅初始 \(\gamma_W\)；
- **(c)** 是，系数 \(9/4\)，共同阈值取两固定指数阈值之最小值；
- **(d)** 是，指数为 \(3\)；
- **(e)** 抽象超临界判据是，但原 Step D 的缩放、弱次解论证及结论不成立；
- **(f)** 否，当前 Section 13 尚未闭合。

随附 Python 脚本只验证了指数、形式上的 \(\chi _0\) 消去和时间比；它没有验证曲率的几何缩放、当前能量传播、塌缩 Sobolev常数或弱次解结构。