# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 2,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step2_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step2_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following quantitative analysis for Yau Problem 26:

1. MIN-OO CORRECTION: The condition in Min-Oo 1990 (JDG 32, 457-472) is d²·max|K| < Λ² (diameter-curvature product, scale-invariant), NOT r⁻²·max|K|. Check this against the OCR source: §3 normalization reads 'max|K(0)| = 1, d(0) < Λ'. Under g→λg: d²K → d²K (invariant) vs r⁻²K → λ(r⁻²K) (not invariant).

2. POSITIVE BRANCH BOUND: For M = X#k CP̄² (LeBrun no-Einstein, 2A/3 < k < A, A=c₁²(X)), combining: (i) LeBrun ∫s²dV ≥ 32π²A, (ii) CGB(+): 4π²(A-k) = ∫[2|W⁺|² + s²/24 - |E|²/2]dV, (iii) Bishop-Gromov V ≤ 24π²/(1-δ)² for σ=+1 gives 12δ²/(1-δ)² ≥ k-2A/3, hence δ_+ ≥ 1/7 uniformly. But stronger: non-trivial SW on LeBrun manifolds prevents s > 0, so δ_+ ≥ 1.

3. NEGATIVE BRANCH: Same integral bound gives δ² ≥ (k-2A/3)/(3(A-k)) using V ≤ 4π²(A-k)/f(δ) from CGB. For varying manifolds with A→∞, this → 0. Check the derivation chain and whether the constants are correct.

4. Verify that the structural asymmetry (positive has Myers+BG+SW control, negative has none) is correctly stated and that no additional constraint on the negative branch has been overlooked.

## Integrated Scientific Memo

# 核验结论

四项中，第 1、2、4 项基本正确；第 3 项的常数链在取 \(\delta\to0\) 的渐近意义下正确，但
\[
\delta^2\ge \frac{k-2A/3}{3(A-k)}
\]
**不是由所列不等式推出的精确有限-\(\delta\) 下界**。精确下界如下。

设
\[
A=c_1^2(X),\qquad B=A-k>0,\qquad q=k-\frac{2A}{3}>0,
\]
并定义四维 Ricci 夹逼量
\[
\delta_\sigma(g)=\sup_{x,i}|\rho_i(x)-\sigma|.
\]
若 \(E=\operatorname{Ric}-\frac{s}{4}g\)，则两种符号下均有
\[
|E|^2\le \sum_{i=1}^4(\rho_i-\sigma)^2\le4\delta_\sigma^2. \tag{1}
\]

## 1. Min-Oo 条件：修正成立

原文 OCR 中定义 \(J^-(n,\Lambda)\) 的字符串损坏，但 §3 的归一化明确为
\[
\max |K(0)|=1,\qquad d(0)<\Lambda.
\]
因此原条件只能是
\[
\boxed{d^2\max|K|<\Lambda^2}.
\]

确实，若 \(L=\max|K_g|>0\)，令 \(\widehat g=Lg\)，则
\[
\max|K_{\widehat g}|=1,\qquad d_{\widehat g}=\sqrt L\,d_g,
\]
故 \(d_{\widehat g}<\Lambda\) 等价于 \(d_g^2L<\Lambda^2\)。

尺度检验也完全一致：
\[
g\mapsto\lambda g:\qquad d\mapsto\sqrt\lambda\,d,\quad
K\mapsto\lambda^{-1}K,\quad r\mapsto\lambda^{-1}r,
\]
所以
\[
d^2\max|K|\mapsto d^2\max|K|,
\]
而
\[
r^{-2}\max|K|\mapsto
\lambda\,r^{-2}\max|K|,
\]
并不尺度不变。这里 \(r\) 是平均标量曲率，不是半径。

此外，若 \(\operatorname{Ric}\) 的本征值属于
\([-1-\delta,-1+\delta]\)，令 \(a=-r/n\in[1-\delta,1+\delta]\)，则
\[
\max_{SM}\left|\frac{n\rho}{r}-1\right|
\le \frac{2\delta}{1-\delta}.
\]
因此，无 Einstein 度量且 \(\delta_-\to0\) 的序列若有
\(d^2\max|K|\) 的统一上界，最终将落入 Min-Oo 定理；故必有
\[
d^2\max|K|\longrightarrow\infty.
\]
逃逸既可来自 Weyl/截面曲率爆破，也可来自直径增长。

## 2. 正分支：常数正确，SW 给出更强结论

LeBrun 的原始结论实际上是严格不等式
\[
\int_Ms^2\,dV>32\pi^2A.
\]
结合
\[
4\pi^2B
=\int_M\left(2|W^+|^2+\frac{s^2}{24}
-\frac{|E|^2}{2}\right)dV
\]
并舍去 \(2|W^+|^2\)，得到
\[
\int_M|E|^2\,dV>8\pi^2q. \tag{2}
\]

若 \(\delta=\delta_+(g)<1\)，则
\[
\operatorname{Ric}\ge(1-\delta)g.
\]
Myers 与 Bishop 比较给出
\[
\operatorname{diam}M\le\pi\sqrt{\frac3{1-\delta}},
\qquad
V\le\operatorname{Vol}
\left(S^4_{\sqrt{3/(1-\delta)}}\right)
=\frac{24\pi^2}{(1-\delta)^2}. \tag{3}
\]
由 (1)–(3)，
\[
8\pi^2q<4\delta^2V
\le\frac{96\pi^2\delta^2}{(1-\delta)^2},
\]
即
\[
\boxed{\quad
q<12\frac{\delta^2}{(1-\delta)^2}.
\quad} \tag{4}
\]

由于 \(A,k\in\mathbb Z\) 且 \(k>2A/3\)，有
\[
q=\frac{3k-2A}{3}\ge\frac13.
\]
故严格版本给出 \(\delta>1/7\)；若把 LeBrun 不等式弱化为非严格形式，则可写
\[
\boxed{\delta_+\ge\frac17}.
\]

更强的结论
\[
\boxed{\delta_+(g)\ge1}
\]
也是正确的，但其依据是 **Seiberg–Witten 非消失对正标量曲率的障碍**，而不是单独由 \(\int s^2\) 下界得到。若 \(\delta_+<1\)，则
\[
s\ge4(1-\delta_+)>0,
\]
而 LeBrun 针对给定 \(H^+(g)\) 选出的非零 SW 类，经 Weitzenböck 消失论排除这种度量。对 \(b^+=1\) 必须采用 LeBrun 的极化／腔室表述，不能无条件引用一个与极化无关的 SW 不变量。

## 3. 负分支：体积估计正确，但所述 \(\delta^2\) 式仅是渐近式

若 \(\delta=\delta_-(g)<1\)，则
\[
s\le-4(1-\delta),\qquad
s^2\ge16(1-\delta)^2.
\]
由 CGB、\(|E|^2\le4\delta^2\) 及 \(W^+\ge0\)，
\[
4\pi^2B\ge f(\delta)V,
\]
其中
\[
f(\delta)=\frac23(1-\delta)^2-2\delta^2
=\frac23(1-2\delta-2\delta^2). \tag{5}
\]
因此只有当
\[
f(\delta)>0
\iff
\delta<\frac{\sqrt3-1}{2}
=\frac1{1+\sqrt3} \tag{6}
\]
时，才能除以 \(f(\delta)\) 得
\[
V\le\frac{4\pi^2B}{f(\delta)}. \tag{7}
\]

结合 (2)、(1)、(7)：
\[
8\pi^2q<\frac{16\pi^2B\delta^2}{f(\delta)},
\]
等价于
\[
q(1-2\delta-2\delta^2)<3B\delta^2. \tag{8}
\]
整理后为
\[
(A-q)\delta^2+2q\delta-q>0.
\]
其正根是
\[
\delta_0
=\frac{\sqrt{Aq}-q}{A-q}
=\frac{\sqrt q}{\sqrt A+\sqrt q}. \tag{9}
\]
故这一推导链给出的严格全局结论是
\[
\boxed{\quad
\delta_-(g)>
\frac{\sqrt{k-2A/3}}
{\sqrt A+\sqrt{k-2A/3}}.
\quad} \tag{10}
\]
即使 \(\delta\) 不满足 (6)，(10) 仍自动成立，因为
\(0<q<A/3\) 蕴含
\[
\delta_0<\frac1{1+\sqrt3}.
\]

因此
\[
\delta^2\ge\frac{q}{3B}
\]
不能作为精确有限-\(\delta\) 推论：它把 (5) 中的
\(f(\delta)\) 替换成了 \(f(0)=2/3\)。正确陈述是
\[
\delta_0^2\sim\frac{q}{3B}
\qquad(q/B\to0). \tag{11}
\]

例如：

- \(A=100,\ k=67,\ q=1/3\)：
  \[
  \delta_0\approx0.0546,
  \]
  而 \(0.058\) 是首阶近似；
- \(A=10000,\ k=6668,\ q=4/3\)：
  \[
  \delta_0\approx0.01142.
  \]

满足 \(k>2A/3\) 的最小整数应写为
\[
k_{\min}=\left\lfloor\frac{2A}{3}\right\rfloor+1,
\]
而不是普遍写成 \(\lceil2A/3\rceil+1\)。此时 \(q=O(1)\)，所以
\[
\delta_0=O(A^{-1/2})\to0.
\]
这仅表明这些拓扑／积分估计没有产生统一正下界，**不构造** 实现 \(\delta_-\to0\) 的度量。

还有一个一致性检验：LeBrun 下界与
\(s^2\le16(1+\delta)^2\) 给出
\[
V>\frac{2\pi^2A}{(1+\delta)^2}.
\]
这与 (7) 给出的 \(V=O(A-k)\) 上界在 \(k\approx2A/3\) 时相容，并未隐藏矛盾。

## 4. 结构不对称：核心判断成立，但“负分支无约束”不宜作绝对表述

核心不对称确实存在：

- 正分支 \(\delta_+<1\)：正 Ricci 触发 Myers 和 Bishop，产生与拓扑复杂度 \(A\) 无关的总直径、总体积上界；正标量曲率又触发 SW 消失。
- 负分支：Ricci 接近 \(-g\) 不给出总体积或直径上界；SW 非消失不排除负标量曲率；纯 Ricci 夹逼也不控制四维 Weyl 曲率。

甚至精确 Einstein 负曲率也没有统一总体积或直径控制：闭双曲流形的有限覆盖经归一化满足
\(\operatorname{Ric}=-g\)，而体积随覆盖次数增长，直径也不能统一有界。

但负分支并非“毫无约束”。现有材料仍给出：

1. Min-Oo：若 \(d^2\max|K|\) 有界且 Ricci 偏差充分小，则存在负 Einstein 度量；
2. 四维 CGB/Hitchin–Thorpe 型拓扑约束；
3. LeBrun 的 \(L^2\) 标量曲率约束及精确下界 (10)；
4. Ricci 下界产生局部 Bishop 球体积比较，但没有无直径假设的总体积上界；
5. 在 \(n\ge4\) 中，未受控制的关键对象是 \(W\)；在三维 \(W=0\)，Ricci 夹逼控制全曲率，但直径增长仍可使 Min-Oo 条件失效。

因此准确结论是：**在所给工具范围内没有遗漏一个能在变化的 LeBrun 流形族上产生统一负分支夹逼间隙的约束。** 尚未解决的数学对象仍是：能否在这些无 Einstein 流形上实际构造
\[
\delta_-(g_j)\to0
\]
的度量。正分支的保护也仅针对当前这些已知无 Einstein 构造，并非所有闭四维流形上的一般定理。