# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Knowledge/objects/papers/Degenerating-Kähler-Einstein-cones-locally-symmetric-cusps-and-the-Tian--adb04d311c2f--499d8f08a8b4/object.md",
    "Knowledge/objects/papers/Invariants-of-some-compactified-Picard-modular-surfaces-and-applications--a2801b1afe2c--6270e445600c/object.md"
  ]
}
```

## Task

Check the proposed corrected separated-depletion theorem and the ramification-cap realization logic. Context: We study the two-parameter ramified Kähler--Einstein surgery law for Einstein-defect gaps on four-manifolds. Step 33 left a partial anti-self-dual retention argument; the current strategist note proposes that if U contains the surgery regions and N is a disjoint topology-preserving modification region with exact KE boundary matching, then retaining the global scalar variance term gives a clean lower bound: for t=theta_0 in [0,1/3], the numerator of equation (4.1) is bounded below by -16 B_U^0 - 48 t B_N^0, hence E >= 4t/(1+t)-o(h) when Delta/A -> 0 and B_U^0=o(Q), even if Delta/Q grows. Peer Step38 adds the local identity on a ramification neighbourhood with matching boundary: Delta_N B = P_N/4 - Delta_N S/48, or in scalar -4 normalization Delta_N B=P_N/4-Delta_N V/3, so flux alone has no sign. Please read the context and give a mathematical verification memo: identify exact assumptions needed, check the algebra and scale estimates, distinguish what this closes from unrestricted competitors, and assess the bridge from the exact Calabi cap model to actual ramified towers (Biquard--Guenancia only gives C0/quasi-isometric model comparison in the negative setting near D unless further elliptic/local chart work is supplied).

## Output

# 数学核验备忘录

## 1. 分离耗散估计：在明确假设下代数完全闭合

记
\[
t=\theta_0=\frac{4\ell-5k}{A}=h(1-6\theta),\qquad
a=\frac{1-3t}{3},
\]
并设
\[
\mathcal N(g)
=a(S-S_0)+16(B-B_\Delta)+(1+t)L_s .
\]
由 (4.1)，
\[
\mathcal E(g)-\frac{4t}{1+t}
=\frac{\mathcal N(g)}{(1+t)R(g)}.
\]

所提修正结论成立，但需要以下几项精确输入。

1. \(g_0\) 是 \(\bar X\) 上的 Kähler–Einstein 度量，\(\operatorname{Ric}(g_0)=-g_0\)，并且
   \[
   S_0=32\pi^2A,\qquad B(g_0)=B_\Delta=\frac{8\pi^2}{3}\Delta .
   \]

2. \(M\) 的全部拓扑手术都位于 \(U\)；在底流形中有对应的旧区域 \(U^0\)。区域 \(N\) 不承载任何拓扑改变。

3. \(U\cap N=\varnothing\)，且 \(g\) 在 \(U\cup N\) 之外等于 \(g_0\)。在 \(U,N\) 的接口环带上两度量完全相同。这个环带假设同时保证：
   - 把 \(N\) 恢复成 \(g_0\) 后得到光滑度量 \(g_1\)；
   - 把 \(N\) 中的修改放到 \(\bar X\) 上得到光滑度量 \(g'\)；
   - 曲率积分严格可加；
   - 相对 Euler、signature 公式没有额外 Chern–Simons 接口项。

4. 全度量标量预算对 \(g_1\) 仍成立：
   \[
   S(g_1)\ge S_0.
   \]
   这正是实际 monopole 输入 \(p\ge A\) 的用途。

定义
\[
\delta S_U=S_U(g)-S_{U^0}(g_0),\qquad
\delta S_N=S_N(g)-S_N(g_0),
\]
以及类似的 \(\delta B_N\)。由于 \(g_1\) 只在 \(U\) 中偏离 \(g_0\)，
\[
\delta S_U=S(g_1)-S_0\ge0. \tag{1}
\]

### \(N\) 上的相对 Chern–Weil 恒等式

令
\[
P_N=\int_N|\operatorname{Ric}^{\circ}_g|^2.
\]
相对 signature 公式给出
\[
\delta\!\int_N|W^+|^2=\delta\!\int_N|W^-|^2=\delta B_N.
\]
相对 Gauss–Bonnet 公式给出
\[
0=2\delta B_N-\frac12P_N+\frac1{24}\delta S_N.
\]
因此
\[
\boxed{\delta B_N=\frac14P_N-\frac1{48}\delta S_N}, \tag{2}
\]
即 Step 38 的局部恒等式。由 \(B_N(g)\ge0\)，还有
\[
\delta B_N\ge-B_N^0,\qquad
\delta S_N=12P_N-48\delta B_N
\le 12P_N+48B_N^0, \tag{3}
\]
其中 \(B_N^0=B_N(g_0)\)。

### 全局分解

由于外部完全不变，
\[
B-B_\Delta
=\bigl(B_U(g)-B_U^0\bigr)+\delta B_N
\ge -B_U^0+\delta B_N.
\]
于是
\[
\begin{aligned}
\mathcal N(g)
&\ge -16B_U^0
+a\delta S_U+a\delta S_N+16\delta B_N+(1+t)L_s(g)\\
&=-16B_U^0
+a\delta S_U+4P_N-t\delta S_N+(1+t)L_s(g).
\end{aligned}
\]
这里使用了 \(a-1/3=-t\)。当
\[
0\le t\le\frac13
\]
时，\(a\ge0\)。结合 (1)、\(L_s\ge0\) 和 (3)，得到
\[
\begin{aligned}
\mathcal N(g)
&\ge -16B_U^0+4P_N-t\delta S_N\\
&\ge -16B_U^0+(4-12t)P_N-48tB_N^0\\
&\ge \boxed{-16B_U^0-48tB_N^0}. \tag{4}
\end{aligned}
\]

所以提出的估计是正确的。它甚至给出稍强形式
\[
\boxed{
\mathcal N(g)\ge
-16B_U^0+(4-12t)P_N-48tB_N^0 .
}
\]

修正论证的关键不是比较 \(L_s(g)\)、\(L_s(g_1)\) 和 \(L_s(g')\)，而是始终保留全局非负项 \(L_s(g)\)，再把标量预算施用于恢复 \(N\) 后的度量 \(g_1\)。因此不需要假设 \(s\) 接近 \(-4\)，也不需要任何相对体积估计。

---

## 2. 尺度估计确实允许 \(\Delta/Q\to\infty\)

由
\[
R=P+\frac14S\ge\frac14S_0=8\pi^2A
\]
和 (4)，
\[
\mathcal E(g)\ge
\frac{4t}{1+t}
-\frac{16B_U^0+48tB_N^0}{(1+t)8\pi^2A}. \tag{5}
\]

若
\[
B_U^0=o(Q),\qquad \frac{\Delta}{A}\to0,
\]
则 \(B_N^0\le B_\Delta=(8\pi^2/3)\Delta\)。又因
\[
t=h(1-6\theta),\qquad t\ge0,
\]
有 \(t\le h=Q/A\)，从而
\[
tB_N^0
\le \frac{Q}{A}\,\frac{8\pi^2}{3}\Delta
=O\!\left(Q\frac{\Delta}{A}\right)
=o(Q).
\]
因此 (5) 化为
\[
\boxed{
\mathcal E(g)\ge \frac{4t}{1+t}-o(h).
}
\]
当 \(h\to0\) 时，
\[
\frac{4t}{1+t}
=4h(1-6\theta)+O(h^2).
\]

这里确实只使用 \(\Delta/A\to0\)，没有使用 \(\Delta=O(Q)\)。即使
\[
\frac{\Delta}{Q}\longrightarrow\infty,
\]
仍有
\[
\frac{t\Delta}{Q}\le\frac{\Delta}{A}\to0.
\]

在 CH-close 手术位置，\(B_U^0=o(Q)\) 也有直接几何来源：CH 度量满足 \(W^-=0\)，若每个固定大小手术区域上 \(g_0\) 与 CH 的 \(C^2\) 差为 \(\varepsilon_m\)，则每个区域的旧 \(W^-\) 能量为 \(O(\varepsilon_m^2)\)，总和为 \(O(Q\varepsilon_m^2)=o(Q)\)。所有计入 \(U\) 的非缩小手术区域都必须具有这一性质；缩小区域则需使旧曲率能量总和为 \(o(Q)\)。

---

## 3. 这一结果处理的度量类，与任意竞争度量的区别

式 (4) 排除了下面这一机制在 \(h\) 的首阶上改善系数：

- 手术全部放在 \(U\)；
- 在与 \(U\) 分离的 \(N\) 中任意改变度量，包括消耗原有 \(W^-\) 能量；
- \(N\) 不改变拓扑；
- 修改在接口环带上回到原 Kähler–Einstein 度量。

即使 \(N\) 含有全部 ramification 区域，并且 \(B_N^0\) 与 \(B_\Delta\) 同阶，其影响仍带有额外因子 \(t=O(Q/A)\)，所以是 \(o(Q)\)。这严格落实了“分离的耗散不改变首阶 tariff”。

它本身不能直接给出 \(\alpha(M)\) 的新全度量估计，因为一般光滑度量未必能写成上述紧支撑、精确环带匹配的形式。以下情形不由该论证处理：

- 手术区域与 ramification 修改区域重叠；
- 手术 cell 本身放在 \(W^-_{g_0}=O(1)\) 的 cap 中；
- 度量在整个流形上弥散变化，无法恢复 \(N\) 而保持接口光滑；
- 只有近似匹配而没有量化相对特征形式的接口误差。

若用近似环带代替完全相同的环带，真正需要控制的是 Euler 和 signature 的 Chern–Simons 接口项以及恢复操作产生的标量平方误差；它们的总量必须是 \(o(Q)\)。仅有点态小差异并不自动给出这一积分尺度。

因此，这个定理解决的是“与手术分离的 ramification 耗散”，而允许 \(r\)-依赖首阶系数的剩余几何机制正是手术与 cap 曲率在同一区域发生相互作用。

---

## 4. 精确 Calabi cap 模型的计算是自洽的

对
\[
g=\tau(dx^2+dy^2)+\frac{d\tau^2}{\Theta}+\Theta\eta^2,
\qquad
\Theta=\frac23\tau^2-\frac c\tau,
\qquad d\eta=dx\wedge dy,
\]
令
\[
\tau_0=\left(\frac{3c}{2}\right)^{1/3}.
\]
则
\[
\Theta(\tau_0)=0,\qquad \Theta'(\tau_0)=2\tau_0.
\]
取纤维角变量周期 \(2\pi/\tau_0\) 后，闭合端光滑。若坐标环面的面积为 \(a\)，则零截面面积及法丛次数满足
\[
\operatorname{Area}(D')=a\tau_0=2\pi e,
\qquad
e=\frac{a\tau_0}{2\pi}.
\]

给定脚本所得
\[
|W^-|^2=\frac{6c^2}{\tau^6},
\]
体积形式为
\[
d\mu=\tau\,dx\,dy\,d\tau\,d\psi.
\]
因此
\[
\begin{aligned}
\int |W^-|^2\,d\mu
&=6c^2 a\frac{2\pi}{\tau_0}
\int_{\tau_0}^{\infty}\tau^{-5}\,d\tau\\
&=\frac{4\pi}{3}a\tau_0
=\frac{8\pi^2}{3}e.
\end{aligned}
\]
在零截面上，
\[
|W^-|^2
=\frac{6c^2}{\tau_0^6}
=\frac83.
\]
这些常数彼此一致。

能量并非紧支撑于固定宽度管状区域。精确模型中，
\[
\frac{\displaystyle\int_{L\tau_0}^{\infty}|W^-|^2\,d\mu}
{\displaystyle\int_{\tau_0}^{\infty}|W^-|^2\,d\mu}
=L^{-4}.
\]
所以 \(\tau_0\le\tau\le L\tau_0\) 捕获比例 \(1-L^{-4}\)。正确表述是：能量在 cap 中指数集中，任意给定高比例可由某个固定宽度区域捕获；“全部位于单位邻域”并非精确积分陈述。

---

## 5. 从精确 cap 到真实 ramified tower：拓扑部分已落实，曲率部分还需要局部椭圆工作

### 已由所给资料支持的部分

1. Biquard–Guenancia §4.3 说明：当 cone 参数取
   \[
   \beta_{m,\lambda}=v_{m,\lambda}^{-1},
   \]
   拉回后的度量在 ramified compactification 上是光滑的 Kähler–Einstein 度量。

2. 对紧化曲线 \(D'_c\)，令
   \[
   e_c=-{D'_c}^{\,2}>0.
   \]
   Hurwitz、adjunction 和紧化 Chern 数给出
   \[
   \sum_c e_c=\Delta.
   \]

3. 对任意这样的紧致 Kähler–Einstein 曲面，全局恒等式
   \[
   B_\Delta=\int|W^-|^2=\frac{8\pi^2}{3}\Delta
   \]
   是精确的，不依赖局部模型逼近。

4. Džambić 的 Theorem 2.5、Propositions 3.3 和 3.5 支持惯性素数幂塔中的
   \[
   A_n\asymp p^{8n},\qquad
   \Delta_n\asymp p^{6n},
   \]
   因而固定 \(r>0\) 时 \(Q_n\sim\Delta_n/r=o(A_n)\)，而 \(r=0\) 时可取
   \(Q_n\asymp p^n\Delta_n=o(A_n)\)。

这些事实足以支撑全局尺度和修正后的分离耗散定理；该定理只需
\[
B_N^0\le B_\Delta,
\]
不需要知道 \(B_\Delta\) 在真实度量中的点态位置。

### 目前资料没有直接给出的部分

Biquard–Guenancia 的 Lemma 4.4 和 Theorem 4.5 在 compactification divisor 附近给出的是
\[
(1-\varepsilon_\beta)\omega_{\beta,\mathrm{model}}
\le \widehat\omega_\beta
\le(1+\varepsilon_\beta)\omega_{\beta,\mathrm{model}},
\]
即趋于一的双线性形式比较，以及相应的准等距渐近。其论文引言也明确说明，得到所有导数的估计需要额外的 gluing/椭圆分析。

这不足以推出：

- 真实度量在 \(D'\) 上满足 \(|W^-|^2\to8/3\)；
- 真实 \(W^-\) 能量在固定 cap 带内等于
  \((8\pi^2/3)e_c+o(e_c)\)；
- 真实度量在固定物理半径区域内与精确 Calabi cap \(C^2\)-接近；
- 在这些区域中插入 cell 后，Ricci-defect 成本趋于模型成本。

曲率依赖度量的二阶导数，而 \(C^0\) 准等距比较无法控制这些量。将模型结论传到真实塔需要在 ramified 局部坐标中建立至少
\[
\|\widehat g_m-g_{\mathrm{cap},m}\|_{C^{2,\alpha}(K)}
\longrightarrow0
\]
的统一估计；若还要比较 cell 的高阶光滑拼接，通常需要更高阶版本。可行的分析框架是：

- 在 ramified 坐标中解除 cone；
- 在局部覆盖上消除切向塌缩带来的 injectivity 问题；
- 利用两度量满足同一 Kähler–Einstein/Monge–Ampère 方程；
- 从 Lemma 4.4 的统一椭圆性出发建立 Evans–Krylov 与 Schauder 估计；
- 证明常数对所有 compactification 分量及 ramification 阶数统一。

若要在 \(\Delta\) 的积分尺度上定位能量，还需要误差速率。举例而言，若 thick part 上的 \(C^2\) 误差是 \(\varepsilon_v\)，其总 \(W^-\) 能量的粗略量级可能是 \(d\,\varepsilon_v^2\)，而
\[
\Delta\asymp \frac d{v^2}.
\]
要得到 \(o(\Delta)\)，需要类似 \(\varepsilon_v=o(v^{-1})\) 的量化信息；单纯 \(\varepsilon_v\to0\) 不够。当 \(\Delta/Q\to\infty\) 时，若误差需达到 \(o(Q)\)，要求还会更强。

### “\(\asymp\Delta\) 个 cap sites”还需嵌入几何

精确面积公式
\[
\sum_c\operatorname{Area}(D'_c)=2\pi\Delta
\]
给出总面积量级，但现有 cell 的外半径是
\[
7.6451\ldots
\]
再加缓冲，而不只是抽象的单位尺度。要得到 \(\asymp\Delta\) 个互不相交、可承载该 cell 的四维球，还需要：

- \(D'_c\) 在拉回度量中的切向 systole 控制；
- 法向 cap 在所需半径内保持嵌入；
- 不同 cusp/cap 区域之间具有统一分离；
- 算术覆盖的 cusp stabilizer 对切向格点的增长估计。

Džambić 的 Chern 数公式给出总次数与总面积，但不直接给出这些局部嵌入数据。面积本身可以支持许多分离点，却不能单独保证每个点周围都有半径 \(7.6451\) 的嵌入四球。

此外，现有认证 cell 具有精确 CH collar。若要研究“cell 与 ramification cap 相互作用”，还需要构造具有精确 Calabi-cap collar 的新 cell，或者量化 CH collar 到 cap collar 的过渡成本。仅把当前 CH-cell 放到 cap 中，并不能直接沿用现有的 \(J_1<8\pi^2\) 证书。

## 6. 总结

- 修正后的分离耗散估计在 \(0\le t\le1/3\) 下严格成立：
  \[
  \mathcal N(g)\ge-16B_U^0-48tB_N^0.
  \]
- 其核心是对恢复 \(N\) 后的度量 \(g_1\) 使用标量预算，并保留全局 \(L_s(g)\ge0\)；不需要标量接近 \(-4\) 或相对体积控制。
- 在 \(B_U^0=o(Q)\)、\(\Delta/A\to0\) 下，
  \[
  \mathcal E(g)\ge\frac{4t}{1+t}-o(h),
  \]
  即使 \(\Delta/Q\to\infty\) 也成立。
- 这排除了与手术分离的 ramification 耗散改变首阶系数，但没有覆盖与手术重叠的 cap-cell，也没有转化为对全部光滑度量的新估计。
- 精确 Calabi 模型、全局 \(B_\Delta\) 和 Picard 塔的算术尺度相互一致；把模型的点态 \(W^-\)、局部能量和 cell 成本传给真实 ramified Kähler–Einstein 度量，仍需统一的 ramified \(C^{2,\alpha}\) 局部收敛、相应速率以及嵌入半径估计。