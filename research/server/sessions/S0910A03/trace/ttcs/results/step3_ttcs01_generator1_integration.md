# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 3,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step3_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step3_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

We study Yau Problem 26 in dimension 4. For Ishida–LeBrun boundary manifolds M=(#_{j=1}^m X_j)#N with m=2 or 3, A=sum c1^2(X_j), and D=4m-(2χ+3τ)(N)=A/3, published Proposition 4 is strict for every metric but gives no uniform normalized gap. Assume a sequence g_i has ||Ric(g_i)+g_i||_op=δ_i→0. Derive the strongest consequences you can from the genuine scalar–Weyl inequality, Chern–Gauss–Bonnet, monopole sign choices/convex hull, and equality structure. Identify exactly what normalized energies, periods, spinors/forms, and concentration measures must converge; distinguish conclusions needing volume/noncollapse/Sobolev bounds. Explore whether there is a route to force a forbidden symplectic structure, or instead a plausible degeneration geometry. Do not use the false Weyl-only lower bound. Seek new rigorous lemmas or a sharp research formulation useful for resolving the negative branch.

## Integrated Scientific Memo

## 1. 规范化及无条件结论

设
\[
M=\Big(\#_{j=1}^mX_j\Big)\#N,\qquad m=2,3,
\]
\[
A=\sum_{j=1}^m c_1^2(X_j),\qquad
D=4m-(2\chi+3\tau)(N)=A/3.
\]
则
\[
T:=(2\chi+3\tau)(M)=A-D=\frac{2A}{3}.
\]

令
\[
S_i=\frac1{4\pi^2}\int_M\frac{s_i^2}{24}\,d\mu_i,\quad
W_i=\frac1{4\pi^2}\int_M2|W_{+,i}|^2\,d\mu_i,
\]
\[
R_i=\frac1{4\pi^2}\int_M\frac{|\Ric_i^\circ|^2}{2}\,d\mu_i,\quad
I_i=S_i+W_i.
\]
Chern–Gauss–Bonnet恒等式给出
\[
I_i-R_i=T=\frac{2A}{3}. \tag{1}
\]

若
\[
\delta_i=\|\Ric_{g_i}+g_i\|_{\rm op}\to0,
\]
则逐点
\[
|s_i+4|\le4\delta_i,\qquad
|\Ric_i^\circ|^2\le4\delta_i^2.
\]
由于 \(s_i^2\ge16(1-\delta_i)^2\)，有
\[
R_i\le q_iS_i,\qquad
q_i=\frac{3\delta_i^2}{(1-\delta_i)^2}\to0.
\]
结合 \(S_i\le I_i\) 与 (1)，
\[
I_i\le \frac{2A/3}{1-q_i},
\]
故
\[
R_i\to0,\qquad I_i\to\frac{2A}{3}. \tag{2}
\]

这是完全无条件的：体积上下界、非塌缩及 Sobolev 控制均不需要。

---

## 2. 正确使用真正的 scalar–Weyl 不等式

定义
\[
K_i=\frac1{72\pi^2}\int_M
\bigl(s_i-\sqrt6|W_{+,i}|\bigr)^2\,d\mu_i .
\]
LeBrun 的真正不等式是
\[
K_i\ge(a_i^+)^2 \tag{3}
\]
对每个 monopole class \(a\) 成立。另有纯代数不等式
\[
I_i\ge\frac23K_i. \tag{4}
\]
这里绝不能代之以任何 Weyl-only 下界。

当 \(s_i<0\)，置 \(x_i=-s_i\)、\(w_i=|W_{+,i}|\)，直接配方得到
\[
I_i-\frac23K_i
=\frac1{864\pi^2}
\int_M(x_i-8\sqrt6\,w_i)^2\,d\mu_i. \tag{5}
\]

---

## 3. 符号族与周期平面的定量收敛

Bauer–Furuta 给出的类为
\[
a_{\varepsilon,\eta}
=\sum_{j=1}^m\varepsilon_jc_j+\sum_{\ell=1}^k\eta_\ell E_\ell,
\qquad \varepsilon_j,\eta_\ell=\pm1,
\]
其中 \(c_j=c_1(X_j)\)，而 \(E_\ell\) 是 \(N\) 的负定对角基。对所有符号平均，自对偶投影平方中的交叉项消失：
\[
\operatorname{Av}_{\varepsilon,\eta}(a_{\varepsilon,\eta,i}^+)^2
=
A+\sum_j\|c_{j,i}^-\|_{L^2}^2
+\sum_\ell\|E_{\ell,i}^+\|_{L^2}^2. \tag{6}
\]
另一方面，由 (3)–(4)，
\[
(a_{\varepsilon,\eta,i}^+)^2
\le\frac32I_i=A+\frac32R_i.
\]
所以
\[
0\le
\sum_j\|c_{j,i}^-\|_{2}^2+
\sum_\ell\|E_{\ell,i}^+\|_{2}^2
\le\frac32R_i\to0. \tag{7}
\]
因此
\[
c_{j,i}^-\to0,\qquad E_{\ell,i}^+\to0, \tag{8}
\]
并且每个顶点都满足
\[
(a_{\varepsilon,\eta,i}^+)^2\to A. \tag{9}
\]

更一般地，
\[
a_{\varepsilon,\eta,i}^+\cdot
a_{\varepsilon',\eta',i}^+
\longrightarrow
\sum_j\varepsilon_j\varepsilon_j'c_1^2(X_j). \tag{10}
\]

因此周期平面沿这些指定类收敛到：包含所有 \(c_j\) 的正方向，并渐近正交于 \(N\) 的负方向。不能仅由此声称整个 period plane 在 Grassmannian 中收敛；其余方向仍可能漂移。

---

## 4. 尖锐能量与体积极限

由 (2)、(3)、(4)、(9)，对每个固定 monopole 顶点，
\[
K_i\to A,\qquad
I_i-\frac23K_i\to0,\qquad
K_i-(a_i^+)^2\to0. \tag{11}
\]
于是 (5) 给出
\[
\int_M\bigl(-s_i-8\sqrt6|W_{+,i}|\bigr)^2\,d\mu_i\to0. \tag{12}
\]
因为 \(s_i\to-4\) 一致，且体积由 \(S_i\le I_i\) 有一致上界，
\[
|W_{+,i}|\to\frac1{2\sqrt6}
\quad\text{于 }L^2(d\mu_i). \tag{13}
\]
从而
\[
W_i=\frac18S_i+o(1).
\]
结合 \(S_i+W_i\to2A/3\)，得到唯一可能的能量轮廓
\[
\boxed{
R_i\to0,\quad
S_i\to\frac{16A}{27},\quad
W_i\to\frac{2A}{27},\quad
K_i\to A.
} \tag{14}
\]
又因 \(s_i^2\to16\) 一致，
\[
\boxed{\Vol(M,g_i)\to\frac{32\pi^2A}{9}.} \tag{15}
\]

反向定向的 CGB 还给出
\[
\frac1{4\pi^2}\int2|W_{-,i}|^2\,d\mu_i
\longrightarrow
(2\chi-3\tau)(M)-\frac{16A}{27}, \tag{16}
\]
故全曲率的 \(L^2\) 范数一致有界。

这些结论仍不需要非塌缩、直径或 Sobolev 假设。特别地，体积有正极限并不排除局部塌缩或曲率集中。

---

## 5. 曲率测度

有总变差收敛
\[
\frac{s_i^2}{96\pi^2}\,d\mu_i
-\frac1{6\pi^2}\,d\mu_i\longrightarrow0, \tag{17}
\]
\[
\frac{2|W_{+,i}|^2}{4\pi^2}\,d\mu_i
-\frac1{48\pi^2}\,d\mu_i\longrightarrow0, \tag{18}
\]
以及
\[
\frac{|\Ric_i^\circ|^2}{8\pi^2}\,d\mu_i\longrightarrow0. \tag{19}
\]
因此在把所有测度放入某个共同紧致极限空间的前提下，若
\(d\mu_i\rightharpoonup\mu\)，则 scalar 与 \(W_+\) 能量测度分别趋于
\[
\frac1{6\pi^2}\mu,\qquad \frac1{48\pi^2}\mu,
\]
而无迹 Ricci 测度消失。

不过 \(W_-\) 只有总质量控制；其能量可在颈部、奇点或塌缩区集中，这正是 \(N\) 的拓扑可能隐藏之处。

---

## 6. 近等号的 spinor/form 结论：哪些是严格的，哪些尚需证明

对固定顶点 \(a\)，采用 Proposition 3.8 证明中的 rescaled Seiberg–Witten 方程，取
\[
f_i^2=-s_i+\sqrt6|W_{+,i}|,
\]
以及
\[
D_{A_i}\Phi_i=0,\qquad -iF_{A_i}^+=f_i\sigma(\Phi_i).
\]
由 (12)–(13)，
\[
f_i\to\frac3{\sqrt2}\quad\text{于 }L^4(d\mu_i). \tag{20}
\]

无条件可确定的是：

* scalar–Weyl 总缺陷趋零；
* harmonic projection 的能量缺陷趋零，即在选取实现上述链条的解后，
  \[
  \|\,iF_{A_i}^+-2\pi h_i^a\,\|_{L^2}\to0, \tag{21}
  \]
  其中 \(h_i^a\) 是 \(a_i^+\) 的 harmonic self-dual representative；
* 证明链条中所有非负积分缺陷的**总和**趋零。

但仅凭文献中陈述的不等式，不能不经稳定性分析便逐项断言
\[
\||\psi_i|-\sqrt2\|_2\to0,\qquad
\|d\psi_i\|_2\to0,
\]
或
\[
|h_i^a|^2\to \frac{9}{32\pi^2}\quad\text{于 }L^1.
\]
这些结论是合理且关键的候选稳定性结论，但需要对 Proposition 3.8 的两次 Hölder、Weitzenböck、Kato/二次映射以及 \(f_i\) 正下界逐项追踪。源文献只刻画**精确等号**，并未提供定量近等号定理。

因此最有用的新引理应表述为：

> **scalar–Weyl 稳定性引理。** 若 \(f_i\) 在 \(L^4\) 中趋于正常数，且 Proposition 3.8 的总缺陷趋零，则适当规范下，spinor 二次型 \(\psi_i\) 渐近闭合、渐近定长，\(F_{A_i}^+\) 渐近 harmonic，并且 \(\psi_i\) 渐近处于 \(W_{+,i}\) 的最低特征线，而其余两个特征值渐近重合。

该引理应能在当前已有能量界下证明，但目前材料尚未完整给出其定量推导。

---

## 7. 多顶点、相分离及浓度测度

设 \(u_{j,i}\) 为 \(c_{j,i}^+\) 的 harmonic representative。由 (8)，顶点 harmonic form 满足
\[
h_i^{\varepsilon,\eta}
=\sum_j\varepsilon_j u_{j,i}+o_{L^2}(1). \tag{22}
\]

若上述稳定性引理证明了所有顶点的渐近定长，则符号平均和 Walsh 极化将给出
\[
\sum_j|u_{j,i}|^2\to\frac{9}{32\pi^2}
\quad\text{于 }L^1, \tag{23}
\]
\[
\langle u_{p,i},u_{q,i}\rangle\to0
\quad\text{于 }L^1,\qquad p\ne q. \tag{24}
\]
此时定义
\[
\theta_{j,i}
=\frac{|u_{j,i}|^2}{9/(32\pi^2)},
\]
则
\[
\sum_j\theta_{j,i}\to1,\qquad
\int_M\theta_{j,i}\,d\mu_i
\to\frac{32\pi^2c_1^2(X_j)}9. \tag{25}
\]
在共同极限空间中可抽取 phase measures
\[
\theta_{j,i}d\mu_i\rightharpoonup\mu_j,\qquad
\sum_j\mu_j=\mu,\qquad
\mu_j(M)=\frac{32\pi^2c_1^2(X_j)}9. \tag{26}
\]

这些相测度是极具解释力的候选结构，但其严格成立依赖上面的近等号稳定性引理，而非仅依赖总能量极限。

---

## 8. 禁止 symplectic 结构的可能路线

若能把 harmonic form 的 \(L^1\) 定长结论提升为
\[
|h_i^a|\ge c>0
\]
的逐点下界，则 \(h_i^a\) 是闭、自对偶、处处非退化的 2-form，故定义 symplectic 结构。近等号 spinor 结构应进一步识别其第一 Chern 类为 \(a\)。

对 \(m>1\) 的该 connected sum，普通 Seiberg–Witten 不变量因非平凡 connected sum 而消失；但 \(b_+>1\) 的 symplectic 四流形由 Taubes 定理有非零 canonical SW invariant，产生矛盾。

真正缺失的是从积分近等号到无零点的升级。可充分的附加条件包括：

* 一致 Sobolev 常数与适合 harmonic 2-form 的椭圆/Moser 估计；
* 一致 harmonic radius 或曲率半径下界；
* 非塌缩的 Einstein-orbifold 紧性，并能在正体积正则区传递 spinor/form 结构。

只有体积正下界或 Ricci 双边夹逼本身不够。

---

## 9. 光滑极限路线的修正

若某个正体积区域有足够强的光滑非塌缩收敛，则极限满足
\[
\Ric=-g,\qquad s=-4,\qquad |W_+|=\frac1{2\sqrt6}.
\]
若近等号稳定性还能传递最低特征线结构，则
\[
\Spec(W_+)=\left\{-\frac16,\frac1{12},\frac1{12}\right\}. \tag{27}
\]

必须注意：仅由“Einstein、\(W_+\) 两重特征值且范数常数”推出局部 Kähler，再与 Kähler 的
\[
\Spec(W_+)=\left\{-\frac23,\frac13,\frac13\right\}
\]
比较，需要额外的 Derdziński 型定理；该定理不在给定来源中，故不能作为此材料内已验证的闭合论证。

更直接且完全源内的办法是：若极限同时保留 scalar–Weyl **精确等号**及相应 monopole/equality data，则 LeBrun 2006 Theorem 4.10 直接推出极限 Kähler–Einstein；随后其标量–Weyl能量比例与当前比例不相容。难点仍是 monopole 类和全局等号结构是否能穿过非紧或奇异极限。

---

## 10. 最可信的退化图景与精确剩余问题

若这样的 \(g_i\) 存在，它不可能是普通意义下收敛到 \(M\) 上光滑 Einstein 度量的序列。所有允许的退化都必须同时满足：

\[
s_i\to-4\ \text{一致},\quad
\Ric_i^\circ\to0\text{ 于 }L^2,\quad
|W_{+,i}|\to\frac1{2\sqrt6}\text{ 于 }L^2,
\]
\[
\Vol_i\to\frac{32\pi^2A}{9},\quad
c_{j,i}^-\to0,\quad E_{\ell,i}^+\to0,
\]
以及固定的总曲率能量轮廓 (14)、(16)。

几何上最合理的是：

* 各 \(X_j\) 形成不同的正体积“相”；
* connected-sum 颈部、\(N\) 及其负定拓扑进入塌缩区或奇异区；
* \(W_-\) 能量在这些区域集中；
* harmonic self-dual forms 在退化区失去逐点下界，因而避免生成全局 symplectic form。

因此负分支的尖锐研究问题可表述为：

> 是否存在满足 (2)、(7)、(11)–(16) 的 almost-\(\Ric=-g\) 序列，而其所有正体积部分均逃避能够传递 Seiberg–Witten 近等号结构的四维非塌缩光滑紧性？

解决它的两个具体数学对象是：

1. Proposition 3.8 的**定量近等号稳定性定理**；
2. 对 Ricci \(C^0\)-近 \(-g\)、总 \(L^2\)-曲率有界且体积固定的四维序列，带 harmonic monopole forms 的**塌缩/奇异紧性定理**。

前者若结合足够非塌缩控制，可能强迫 forbidden symplectic structure；若非塌缩不可得，则后者应精确描述相分离、颈部和 \(W_-\) 浓度如何承载 connected-sum 拓扑。