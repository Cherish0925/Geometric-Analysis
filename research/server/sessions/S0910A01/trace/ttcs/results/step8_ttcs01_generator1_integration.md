# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 8,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step8_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step8_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Using the Step 8 measure-local theorem and the Naber-Zhang collapsed regularity framework, propose the strongest mathematically precise next route for extending the Derdziński contradiction through local unwrapping of collapsed neighborhoods. Focus on what hypotheses would let small mean LeBrun deficits transfer to noncollapsed local covers with bounded multiplicity or controlled measure distortion, how maximal nilpotency-rank assumptions enter, and what collapse mechanisms remain outside such a route. Do not claim a full collapse classification; give testable lemmas or reductions that could materially advance Yau 26.

## Integrated Scientific Memo

## 局部解卷绕路线：可严格推进的最强归约

设四维近边界 LeBrun 序列满足

\[
\|\Ric_{g_i}+g_i\|_{L^\infty}\to0,\qquad
\fint_{M_i}F_i\,d\mu_i\to0,
\]

其中

\[
F_i=|\Ric_{g_i}+g_i|^2+
(s_i+8\sqrt6|W_i^+|)^2+\xi_i(Q_i+P_i)\ge0.
\]

Step 8 已排除正体积比例的非塌缩区域。下一步不需要完整分类塌缩，而是排除下述“可解卷绕、最大秩、测度可控”的塌缩部分。

### 1. 真正需要转移的缺陷

\(\Ric+g\) 的小性是 \(L^\infty\) 的，故任意局部 Riemann 覆盖上自动保持：

\[
\|\Ric_{\hat g_i}+\hat g_i\|_{L^\infty}
=\|\pi_i^*(\Ric_{g_i}+g_i)\|_{L^\infty}\to0.
\]

因此一旦覆盖具有统一 harmonic radius，其极限自动满足

\[
\Ric_{g_\infty}=-g_\infty,\qquad s_\infty=-4.
\]

需要测度转移的仅是两个积分型量

\[
G_i:=(s_i+8\sqrt6|W_i^+|)^2+\xi_i(Q_i+P_i).
\]

这一区分很重要：Naber–Zhang 提供覆盖上的非塌缩与正则性，但并不自动把 \(G_i\) 的基空间平均小性转成覆盖平均小性。

---

## 2. 精确的覆盖测度条件

令

\[
\pi:(\widehat U,\hat g)\longrightarrow U
\]

为局部正规覆盖，\(B_r(\hat p)\Subset\widehat U\)，并定义

\[
m_{\hat p,r}(x)
=\#\bigl(\pi^{-1}(x)\cap B_r(\hat p)\bigr).
\]

则对任意非负可测函数 \(\phi\),

\[
\int_{B_r(\hat p)}\pi^*\phi\,d\hat\mu
=
\int_U \phi(x)m_{\hat p,r}(x)\,d\mu(x),
\]

所以覆盖平均是由 \(m_{\hat p,r}\) 加权的基空间平均。最自然的充分条件不是绝对有界的 sheet 数——它在塌缩中通常发散——而是以下相对密度控制：

\[
\boxed{
\frac{m_{\hat p,r}(x)}
{\Vol_{\hat g}B_r(\hat p)}
\le
\frac{L}{\Vol_g B_{\sigma r}(p)}
\,1_{B_{\sigma r}(p)}(x)
}
\tag{T}
\]

几乎处处成立，其中 \(L,\sigma\) 一致有界。由此

\[
\fint_{B_r(\hat p)}\pi^*\phi
\le
L\fint_{B_{\sigma r}(p)}\phi.
\tag{2.1}
\]

更灵活且足够的形式是

\[
\boxed{
\fint_{B_r(\hat p)}\pi^*\phi
\le L\,\mathcal M_R\phi(p),
\qquad
\mathcal M_R\phi(p):=
\sup_{0<t\le R}\fint_{B_t(p)}\phi
}
\tag{T'}
\]

其中 \(r\asymp R\)。因为 Ricci 下界给出局部 doubling，Hardy–Littlewood 弱型估计给出

\[
\Vol\{p:\mathcal M_RF_i(p)>\alpha\}
\le
\frac{C}{\alpha}\int_{M_i}F_i.
\]

故任何占固定总体积比例的候选点集都含有 \(p_i\)，使

\[
\mathcal M_RF_i(p_i)\to0.
\]

条件 (T′) 随即推出覆盖球上的平均缺陷趋零。

仅有 pushforward 测度的弱收敛不足以处理可能集中的 \(L^1\) 密度 \(G_i\)；必须有类似 (T)、(T′) 的一致绝对连续性或最大函数支配。

---

## 3. 可直接证明的条件性排除定理

固定 \(R_0,\rho,L>0\)。称 \(p_i\) 为 **NZ-可访问点**，若存在尺度 \(R_i\in[R_0,1]\)、整数 \(k_i\le3\) 及 \(\ell_i\le3\)，使：

1. **低维模型逼近**
   \[
   d_{GH}\!\left(
   B_{2R_i}(p_i),
   B_{2R_i}(0^{k_i-\ell_i},z_i^{\ell_i})
   \right)<\delta_iR_i,\qquad \delta_i\to0,
   \]
   且模型的 noncollapsing radius 满足
   \[
   r_c(z_i^{\ell_i})\ge\rho.
   \]

2. **纤维基本群达到最大 nilpotency rank**
   \[
   \rank\Image\!\left[
   \pi_1(B_{\delta_iR_i}(p_i))
   \to\pi_1(B_{2R_i}(p_i))
   \right]
   =4-k_i.
   \tag{3.1}
   \]

3. **局部覆盖上的测度转移**
   对某个局部 universal 或 normal cover 及某个
   \(a=a(\rho)>0\)，条件 (T′) 在 \(B_{aR_i}(\hat p_i)\) 上成立，常数不依赖 \(i\)。

则这些点的集合在 Step 8 序列中只能占消失的体积比例：

\[
\frac{\Vol\{p_i:\ p_i\text{ 为 NZ-可访问点}\}}
{\Vol M_i}\longrightarrow0.
\tag{3.2}
\]

### 证明机制

若反之有固定正体积比例，可选取其中的 \(p_i\) 满足

\[
\mathcal M_{R_i}F_i(p_i)\to0.
\]

由测度转移，

\[
\fint_{B_{aR_i}(\hat p_i)}\pi_i^*F_i\to0.
\tag{3.3}
\]

Naber–Zhang Theorem 5.1 与 Proposition 6.4 在 (3.1)、\(\ell_i\le3\) 及 \(r_c\ge\rho\) 下给出覆盖上的统一非塌缩与 harmonic-radius 下界：

\[
r_h(\hat p_i)\ge h_0(4,\rho)R_i
\ge h_0(4,\rho)R_0>0.
\tag{3.4}
\]

在较小 harmonic chart 上，Step 8 的有限 \(W^{2,p}\) 论证适用于拉回度量。取 \(p>2\)，得到强 \(W^{2,p}\) 收敛到光滑极限 \(g_\infty\)，且

\[
\Ric_{g_\infty}=-g_\infty.
\]

由 (3.3) 传递另外两个非负缺陷，得到

\[
s_\infty=-4,\qquad
|W_\infty^+|^2=\frac1{24},\qquad
\spec(W_\infty^+)
=
\left(\frac1{12},\frac1{12},-\frac16\right).
\]

Einstein 性给出 \(\delta W_\infty^+=0\)。Derdziński Proposition 5 适用，且

\[
(24|W_\infty^+|^2)^{1/3}
\]

为常数，所以 \(g_\infty\) 局部 Kähler。可是四维 Kähler–Einstein 度量若 \(\Ric=-g\)，则在相应定向下

\[
|W^+|^2=\frac23,
\]

与 \(1/24\) 矛盾，证明 (3.2)。

---

## 4. 最大秩的准确作用

最大秩有两个已由 Naber–Zhang 支持的作用：

1. **恢复覆盖上的缺失维数。**  
   若基极限维数为 \(k\)，则广义 Margulis 结论仅给出
   \[
   \rank\Gamma_\delta(p)\le4-k.
   \]
   等号使 graded short generators 在 equivariant limit 中产生总维数 \(4-k\) 的 nilpotent orbit；Theorem 5.1 因而给出 universal cover 的统一非塌缩。

2. **导出 harmonic radius。**  
   当残余模型维数 \(\ell\le3\) 时，覆盖上的非塌缩与 quantitative splitting 可接入非塌缩 \(\epsilon\)-regularity，得到 Proposition 6.4 的 harmonic-radius 下界。

但来源材料**没有直接证明**最大秩还蕴含 (T) 或有界 multiplicity oscillation。把极限群轨道的传递性直接等同于有限尺度、对所有 \(L^1\) 函数有效的均匀测度解体，是尚未完成的步骤。因此不能声称“仅最大秩已闭合整个链”。

---

## 5. 核心待证引理：nilpotent deck-orbit counting

最有价值的下一引理是：

### Deck-orbit counting lemma

在上述模型逼近、\(r_c\ge\rho\) 和最大秩条件下，对局部 universal cover 存在固定 \(a,a',C>0\)，使任意 \(\phi\ge0\) 满足

\[
\fint_{B_{aR}(\hat p)}\pi^*\phi
\le
C(4,\rho,a)\,
\mathcal M_R\phi(p),
\tag{5.1}
\]

或更强地，

\[
\pi_*\!\left(
\frac{1_{B_{aR}(\hat p)}d\hat\mu}
{\Vol B_{aR}(\hat p)}
\right)
\le
C\,
\frac{1_{B_{a'R}(p)}d\mu}
{\Vol B_{a'R}(p)}.
\tag{5.2}
\]

证明应使用 Naber–Zhang 的：

- 有界指数 almost-nilpotent subgroup；
- 与 lower central series 相容的 graded short generators；
- 每个无限循环因子的受控位移；
- 最大秩时极限轨道恰好填满全部 \(4-k\) 个塌缩方向。

在平坦模型

\[
B^k\times(\mathbb R^{4-k}/\varepsilon\mathbb Z^{4-k})
\]

中，覆盖球投影的重数约为晶格点计数；其绝对值随
\(\varepsilon^{-(4-k)}\) 发散，但除以自然平均重数后保持一致有界。一般 nilpotent 情形应以 graded/Mal’cev 坐标中的晶格计数及 Haar 体积比较取代欧氏格点计数。有限指数 \(w_0\) 仅应改变常数。

一个较弱、也足够的版本是 dyadic 环带控制：

\[
\frac{m_{\hat p,aR}(x)}{\Vol B_{aR}(\hat p)}
\le
C\sum_{j=0}^{J}
\frac{1_{B_{2^{-j}R}(p)}(x)}
{\Vol B_{2^{-j}R}(p)},
\]

它同样推出 (5.1)。

---

## 6. 正则塌缩层上的归约

在 measured Ricci-limit 的 \(m\)-regular 点，几乎处处切锥为 \(\mathbb R^m\)。在可统一选择的正尺度上，这对应

\[
k=m,\qquad \ell=0.
\]

因此可得到以下严格归约：

> 若在占固定体积比例的 \(m\)-regular 塌缩点上，存在统一正尺度的欧氏模型逼近、纤维基本群秩 \(4-m\)，并且 deck-orbit counting lemma 成立，则该体积比例不可能存在。

要从“极限测度几乎处处 regular”推出“某个统一 \(R_0>0\) 上占固定比例”仍需定量分层或 Egorov 型尺度选择；单点 regularity 本身只给出依点而变的尺度，可能趋零。

---

## 7. 此路线之外的真实残余机制

1. **秩下降与奇异纤维。**
   \[
   \rank\Gamma_\delta(p)<4-k.
   \]
   覆盖未恢复所有维数，Naber–Zhang 非塌缩结论不能使用。K3 的 pinched-torus 奇异纤维正是这种机制；它未必伴随大的 LeBrun 缺陷。

2. **可用尺度趋零。**  
   若 \(R_i\to0\)，按 \(R_i^{-2}\) 重标后
   \[
   \Ric_{R_i^{-2}g_i}\approx -R_i^2(R_i^{-2}g_i)\to0.
   \]
   极限变为 Ricci-flat，原尺度上的
   \(s=-4\)、\(|W^+|^2=1/24\) 标定不再保留，因此不能直接复用同一 Derdziński 矛盾。

3. **模型退化。**  
   \(r_c(z_i)\to0\) 时，Naber–Zhang 常数退化。这包括基空间奇异层及不断变化的低维模型。

4. **残余四维核心。**  
   Naber–Zhang 的 \(\ell\le3\) 是尖锐条件；四维 Eguchi–Hanson 型因子不受该正则性定理控制。它们可存在于 \(o(\Vol M_i)\) 的非塌缩岛或 bubble core 中，并承载 Euler/signature。

5. **测度畸变。**  
   最大秩已知能给覆盖非塌缩，但在 (5.1) 证明之前，覆盖球仍可能过度加权基空间中的极小缺陷集中集。这正是 deck-counting 引理要排除的对象。

6. **有界曲率但秩不足的塌缩。**  
   这种塌缩既无覆盖非塌缩，也不必产生 Weyl 能量集中，故不能仅靠曲率能量预算排除。

---

## 8. 可验证的近期目标

最关键的两个可独立检验对象是：

\[
\boxed{\text{最大秩}+\text{统一模型几何}
\Longrightarrow \text{相对重数/最大函数控制}}
\]

以及

\[
\boxed{\text{在正体积比例的 regular 塌缩层上出现统一正尺度和最大秩}}
\]

前者可先在平坦 torus bundles 与 Heisenberg nilmanifold collapse 上证明，再利用 Naber–Zhang graded generators 推广；后者把整个剩余问题精确归约为 rank-deficient stratum 的体积控制。两者结合即把 Step 8 的 Derdziński 矛盾严格扩展到所有固定尺度、低维模型正则、最大 nilpotency-rank 且测度可控的塌缩邻域，而不需要也不声称完整塌缩分类。