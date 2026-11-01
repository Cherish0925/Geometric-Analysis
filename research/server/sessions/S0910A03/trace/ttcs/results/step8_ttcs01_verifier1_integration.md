# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 8,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step8_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step8_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify and sharpen the proposed local mean transfer bridge for the fixed-topology critical Ishida–LeBrun sequence. Read the cited working notes and the Naber–Zhang source. Focus on: (i) whether the A01 normal-cover lemma is actually correct for local normal covers, including the closest-lift measurable section, disjoint translates, domain/buffer, and whether its RHS should use B_r(p) or a larger ball; (ii) whether combining that lemma with small base-ball means and Naber–Zhang Proposition 6.4 gives a fixed-scale harmonic chart on the cover for merely bounded Ricci; (iii) whether small mean of the full calibrated deficit on the cover is enough to force the forbidden Einstein germ through finite W^{2,p} convergence, including possible mismatch between the point selected for low mean and the point/scale where Naber–Zhang produces regularity. State a precise conditional theorem that is genuinely supported, and identify the exact unresolved hypothesis needed to apply it to almost all collapsed points. Do not assume Cheeger–Tian curvature decomposition or exact symmetric collapse models.

## Integrated Scientific Memo

## 核验结论

这条桥在适当修正后成立：

\[
\text{小的基球平均亏损}
\Longrightarrow
\text{小的局部普适覆盖球平均亏损}
\Longrightarrow
\text{固定尺度调和坐标}
\Longrightarrow
\text{禁戒的 calibrated Einstein germ}.
\]

但它只能排除在**正体积比例**上满足统一 Naber–Zhang 假设的塌缩点。当前真正缺失的不是 cover 上的亏损传输，而是：几乎所有塌缩点是否都具有统一低维模型、最大纤维基本群秩及不退化模型尺度。

---

## 1. 正规覆盖平均值传输：结论正确，但 A01 的论域与可测截面论证须修正

### 修正版引理

设 \((M^n,g)\) 满足

\[
\operatorname{Ric}_g\ge -(n-1)K g,
\]

\(U\subset M\) 为开集，且 \(\overline{B_{4r}(p)}\subset U\)。令

\[
\pi:(\widehat U,\hat g)\to(U,g)
\]

为连通正规 Riemann 覆盖，\(\pi(\hat p)=p\)。则对任意非负可测函数 \(\varphi\)，

\[
\fint_{B_r(\hat p)}\pi^*\varphi\,d\hat\mu
\le
\frac{V_{-K}^{(n)}(3r)}{V_{-K}^{(n)}(r)}
\fint_{B_r(p)}\varphi\,d\mu .
\tag{1}
\]

这里所有覆盖球均取覆盖空间的内蕴长度度量。

### 证明要点

每个 \(x\in B_r(p)\) 都有一个位于 \(B_r(\hat p)\) 的 lift：提升从 \(p\) 到 \(x\) 的最短测地线即可。可选取 Borel 截面

\[
s:B_r(p)\to B_r(\hat p),\qquad \pi\circ s=\mathrm{id}.
\]

不必使用“最近 lift”。A01 关于等距集合是余维一子流形、坏集合测度零的说法未获支持：cut locus 会使等距集合更复杂。标准的 countable-fibre Borel selection 足够。令 \(S=s(B_r(p))\)，则面积公式给出

\[
\hat\mu(S)=\mu(B_r(p)).
\tag{2}
\]

设 deck 群为 \(\Gamma\)，并令

\[
N(2r)=\#\{\gamma\in\Gamma:d(\hat p,\gamma\hat p)<2r\}.
\]

若 \(\hat x,\hat x_1\in B_r(\hat p)\) 是同一点的两个 lifts，\(\hat x=\gamma\hat x_1\)，则

\[
d(\hat p,\gamma\hat p)<2r.
\]

故 \(B_r(\hat p)\to B_r(p)\) 的纤维重数不超过 \(N(2r)\)。另一方面，对所有上述 \(\gamma\)，

\[
\gamma S\subset B_{3r}(\hat p),
\]

且这些 translates 两两不交，因此

\[
N(2r)\,\mu(B_r(p))
\le \hat\mu(B_{3r}(\hat p)).
\tag{3}
\]

结合重数面积公式、(3) 及覆盖上的 Bishop–Gromov 即得 (1)。

### 论域修正

A01 写的 \(B_{3r}(\hat p)\subset\widehat U\) 若 \(\widehat U\) 已指整个覆盖空间，形式上是空洞条件。实际需要的是：

1. \(\widehat U\) 是某个较大开基域 \(U\) 的**完整正规覆盖**，而不是任意截断的 cover patch；
2. \(B_{3r}(\hat p)\) 在该覆盖中有足够内部余量，使局部 Bishop–Gromov 和 deck translates 均合法。

若只取大覆盖中的截断子集，deck 变换未必保持它，disjoint-translate 论证会失效。假设 \(\overline{B_{4r}(p)}\subset U\) 是一个干净的充分条件。

### RHS 究竟是哪一个球？

(1) 的右端确实是

\[
\fint_{B_r(p)}\varphi,
\]

而非更大球；投影及重数公式只涉及 \(B_r(p)\)。较大半径 \(3r\) 只出现在覆盖空间的体积比较中。

若已知的只是 \(B_R(p)\) 上的平均，\(R\ge r\)，则另用 Bishop–Gromov：

\[
\fint_{B_r(p)}\varphi
\le
\frac{V_{-K}^{(n)}(R)}{V_{-K}^{(n)}(r)}
\fint_{B_R(p)}\varphi.
\tag{4}
\]

若中心移到 \(q\)，则必须保证 \(B_r(q)\subset B_R(p)\)，并再付一个固定体积比较因子。

---

## 2. Naber–Zhang 给出的正是 bounded-Ricci 情形所需的调和半径，而不是曲率界

Naber–Zhang Proposition 6.4 假设：

\[
|\operatorname{Ric}|\le n-1,
\]

局部相对紧致性，

\[
d_{GH}\!\left(B_2(p),
B_2(0^{k-\ell},z^\ell)\right)<\delta_0,
\qquad \ell\le3,
\tag{5}
\]

以及最大纤维 nilpotency rank

\[
\operatorname{rank}
\operatorname{Image}\!\left[
\pi_1(B_{\delta_0}(p))\to\pi_1(B_2(p))
\right]
=n-k.
\tag{6}
\]

其结论是：对每个 \(q\in B_1(p)\)，在 \(B_1(q)\) 的局部普适覆盖中，

\[
r_h(\tilde q)\ge h_0>0.
\tag{7}
\]

常数依赖于 \(n\) 和模型 \(B_1(z^\ell)\)，等价地依赖于模型 noncollapsing radius \(r_c(z^\ell)\)。因此要用于序列，必须有统一下界

\[
r_c(z_i^\ell)\ge r_*>0.
\tag{8}
\]

关键区别：

* 仅有 bounded Ricci 已足以得到 (7)；
* bounded Ricci 不给 approximating metrics 的点态曲率界；
* Einstein 或 \(|\nabla\operatorname{Ric}|\) 控制才给 Naber–Zhang 的曲率升级；
* Proposition 6.4 的覆盖是局部普适覆盖，不应无证明地替换成任意 intermediate normal cover。

本序列满足 \(\|\operatorname{Ric}_{g_i}+g_i\|_\infty\to0\)，故大 \(i\) 时 \(|\operatorname{Ric}_{g_i}|\le3\)，正符合四维归一化。

### 最干净的尺度对齐

取 \(q=p_i\)，并固定

\[
0<a<\frac13
\]

（例如 \(a=1/8\)）。在 \(B_1(p_i)\) 的普适覆盖上使用 (1)，则 \(3a<1\) 提供必要 buffer；同时由 (7)，在 \(\tilde p_i\) 处已有固定调和半径。缩小 \(h_0\) 后可令调和 chart 完全包含于 \(B_a(\tilde p_i)\)。

因此，只要

\[
\fint_{B_a(p_i)}F_i\to0,
\tag{9}
\]

就有

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i\to0.
\tag{10}
\]

小平均本身不产生调和 chart；(5)–(8) 才是固定尺度正则性的来源。

---

## 3. 完整 calibrated deficit 的小 cover 平均足以产生禁戒 germ

可取显式非负密度

\[
F_i=
|\operatorname{Ric}_{g_i}+g_i|^2
+(s_i+8\sqrt6\,|W_i^+|)^2
+\mathcal G_i,
\tag{11}
\]

其中

\[
\alpha=\sqrt{\frac23},\quad
u_i=|W_i^+|,\quad
w_i=\lambda_{\min}(W_i^+),
\]

\[
f_i=\frac23s_i-2\alpha u_i,\qquad
b_i=\frac23s_i+2w_i,
\]

\[
\mathcal G_i=f_i^2-\bigl(\min\{b_i,0\}\bigr)^2\ge0.
\tag{12}
\]

固定临界 Ishida–LeBrun 拓扑下，已有绝对小量

\[
\int_M F_i\,d\mu_i\to0.
\tag{13}
\]

这些量在定向局部等距覆盖下逐点拉回。由 (10) 及覆盖球的统一体积上界，

\[
\int_{B_a(\tilde p_i)}\pi_i^*F_i\to0,
\tag{14}
\]

故其任意固定较小调和 chart 上的积分也趋于零。

### 有限 \(W^{2,p}\) 极限足够

在调和坐标中，

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=
-2(\operatorname{Ric}_{g_i})_{jk}
+Q_{jk}(g_i^{-1},\partial g_i).
\tag{15}
\]

调和半径给出统一椭圆性和一阶控制；bounded Ricci 给有限任意 \(p\) 的 \(W^{2,p}\) 控制。取 \(p>4\)，缩小 chart 后可得

\[
g_i\to g_\infty
\quad\text{strongly in }C^{1,\beta},
\qquad
g_i\rightharpoonup g_\infty
\quad\text{in }W^{2,p}.
\]

又因

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,\qquad
\|e_i\|_\infty\to0,
\]

对差分方程使用 interior \(L^p\) estimates，得到更小 chart 上的强 \(W^{2,p}\) 收敛。极限弱满足

\[
\operatorname{Ric}_{g_\infty}=-g_\infty,
\]

并由调和坐标 Einstein 方程 bootstrap 为光滑度量。

因此曲率在有限 \(L^p\) 中强收敛；\(s\)、\(|W^+|\)、最低特征值及 \(\mathcal G\) 都可在 \(L^1\) 中传递。由 (14)：

\[
s_\infty=-4,\qquad
|W_\infty^+|=\frac1{2\sqrt6},\qquad
\mathcal G_\infty=0.
\tag{16}
\]

在这些值上，令

\[
\xi=w_\infty+\sqrt{\frac23}|W_\infty^+|
=w_\infty+\frac16,
\]

则

\[
\mathcal G_\infty=4\xi(3-\xi).
\]

自对偶 Weyl 的最低特征值估计给 \(\xi\ge0\)，而 \(w_\infty\le0\) 给 \(\xi\le1/6\)，故

\[
\xi=0,\qquad w_\infty=-\frac16.
\]

再由 trace-free 条件和 \(|W^+|^2=1/24\) 得

\[
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\tag{17}
\]

因此若把完整的 \(\mathcal G_i\) 放入 \(F_i\)，不需要额外提升 monopole 场来识别极限特征线。

### germ 的局部矛盾

Einstein 性给 \(\delta W_\infty^+=0\)。常数二特征值 projector 引理给

\[
\nabla W_\infty^+=0.
\tag{18}
\]

但 Einstein–Weyl 标量恒等式

\[
\Delta|W^+|^2
=
2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]

代入

\[
s=-4,\quad |W^+|^2=\frac1{24},\quad
\det W^+=-\frac1{864}
\]

得

\[
|\nabla W_\infty^+|^2=\frac1{16},
\tag{19}
\]

与 (18) 矛盾。这是纯局部矛盾，不需完备性。

---

## 4. 点与尺度错配如何严格处理

最优处理是完全避免错配：

1. 只在满足统一 Naber–Zhang 假设的点集上做平均；
2. 选出的低平均点记为 \(p_i\)；
3. 在 Proposition 6.4 中直接取 \(q=p_i\)；
4. 在 \(B_1(p_i)\) 的普适覆盖上以固定 \(a<1/3\) 应用传输引理；
5. 使用以 \(\tilde p_i\) 为中心的调和 chart。

若正则点不得不选在 \(q_i\ne p_i\)，则需要预先保证 \(B_\rho(q_i)\subset B_R(p_i)\)，用 (4) 把低平均转移到 \(q_i\)，或直接在包含该 chart 的较大 cover ball 上传输。仅知道 \(B_R(p_i)\) 的小积分、却没有 chart 体积下界，不足以推出 chart 平均小；Naber–Zhang 的统一调和半径正好补足这一点。

---

## 5. 真正支持的条件定理

**条件排除定理。**  
设 \(M^4\) 为固定闭定向光滑流形，\(g_i\) 为固定临界 Ishida–LeBrun 序列，满足

\[
\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty}\to0,
\qquad
\int_MF_i\,d\mu_i\to0,
\]

其中 \(F_i\) 如 (11)。固定 \(r_*>0\)。令 \(S_i\) 为所有满足下列条件的点 \(p\)：

1. 对某些 \(k,\ell\)（\(\ell\le3\)）和 \(\ell\)-维 Ricci-limit model \((Z^\ell,z^\ell)\)，
   \[
   d_{GH}\!\left(B_2(p),
   B_2(0^{k-\ell},z^\ell)\right)
   <\delta_*(4,r_*);
   \]
2. 模型尺度不退化：
   \[
   r_c(z^\ell)\ge r_*;
   \]
3. 纤维基本群秩最大：
   \[
   \operatorname{rank}
   \operatorname{Image}\!\left[
   \pi_1(B_{\delta_*}(p))
   \to\pi_1(B_2(p))
   \right]
   =4-k.
   \]

则

\[
\frac{\operatorname{Vol}_{g_i}(S_i)}
{\operatorname{Vol}_{g_i}(M)}
\longrightarrow0.
\tag{20}
\]

证明：若沿子列该比例至少为 \(\eta>0\)，在 \(S_i\) 上应用 Fubini–Bishop–Gromov 局部平均，引出 \(p_i\in S_i\) 使固定 \(a<1/3\) 下

\[
\fint_{B_a(p_i)}F_i\to0.
\]

Proposition 6.4 在 \(\tilde p_i\) 给统一调和半径；修正版覆盖传输给 cover 上小平均；有限 \(W^{2,p}\) 极限产生 (17)，再由 (18)–(19) 矛盾。

该定理不使用 Cheeger–Tian 曲率分解，也不假设精确对称塌缩模型。

---

## 6. 对“几乎所有塌缩点”应用时唯一实质未解的输入

所需的精确假设是：

> 在某个固定几何尺度上，除去 \(o(\operatorname{Vol}M)\) 的点之外，每个塌缩点都具有一个 \(\ell\le3\) 的 Naber–Zhang 低维 GH 模型，模型 noncollapsing radius 有统一正下界，并且纤维基本群具有最大 nilpotency rank。

等价地，至少要先证明存在 \(\rho,\eta>0\)，使沿某子列

\[
\operatorname{Vol}\left\{
p:
r_h\!\left(\tilde p;\widetilde{B_1(p)}\right)\ge\rho
\right\}
\ge \eta\,\operatorname{Vol}(M,g_i).
\tag{21}
\]

若要覆盖几乎所有点，则 (21) 中比例应趋于 \(1\)。

现有 Ishida–LeBrun 亏损估计和单位尺度处处基空间塌缩，并不推出这一点。仍可能失败于：

* 最大秩下降；
* 奇异纤维或奇异 strata；
* 模型 noncollapsing radius \(r_c\to0\)；
* 残余四维因子或四维 bubble（Naber–Zhang 的 \(\ell\le3\) 限制在此是尖锐的）；
* 仅在 \(r_i\to0\) 的尺度上才能 unwrap。

最后一种不能直接救回论证：按 \(r_i^{-2}\) 重标后 Einstein 常数趋于零，固定尺度的 calibrated profile \(\operatorname{Ric}=-g\)、\(|W^+|^2=1/24\) 不再保留。

因此，deck multiplicity/亏损传输已不是剩余障碍；剩余的精确科学对象是 **Naber–Zhang-good maximal-rank、uniform-model points 的体积占比定理**。