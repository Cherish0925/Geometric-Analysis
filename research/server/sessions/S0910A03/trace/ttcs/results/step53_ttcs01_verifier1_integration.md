# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 53,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step53_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step53_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the coupled transported-coefficient start theorem for the normalized cutoff flow ∂_t g = -2χ²(Ric+g). The central mathematical claim is that the coupled DeTurck system (metric equation + scalar transport for χ̂=χ∘φ⁻¹) has short-time existence through a staggered parabolic-ODE grading. Specifically verify:

1. PULLBACK IDENTITY: Does the coupled system (1.4) in the note actually pull back to give ∂_t g = -2χ²(Ric+g) with FIXED χ in geometric coordinates? Check the computation: g=φ*ĝ, â∘φ=a because χ̂=χ∘φ⁻¹.

2. PRINCIPAL STRUCTURE: The coupling matrix shows metric eq at order k needs ψ at order k (coefficient only), transport at order k needs V at order k+1 (through DeTurck vector W~∂V). Is this 'lower-triangular' description correct?

3. PARABOLIC GAIN: The note claims V∈C_t(H^s)∩L²_t(H^{s+1}) from the parabolic equation, and this extra L²_t derivative compensates the ODE for φ needing ∫||âW||_{H^s}dt, where ||W||_{H^s}≤C||V||_{H^{s+1}}. Verify this chain.

4. TRANSPORT IBP: The transport energy estimate claims ∫∂^α ψ·ψ²W·∂_k∂^α ψ = -½∫(∂^α ψ)²·∂_k(ψ²W), so the top-order ψ term is absorbed without needing ψ at order k+1. Is this correct for the SPECIFIC equation ∂_t ψ = ψ²W^k∂_kψ (note the coefficient is ψ² not just a constant)?

5. CONTRACTION: The I2 factorization â₁-â₂=(χ̂₁+χ̂₂)(χ̂₁-χ̂₂) is used to bound the coefficient difference in the contraction. Does this genuinely make the cross-terms proportional to ||χ̂₁-χ̂₂|| with bounded multipliers?

6. CRITICAL GAP: Is there any hidden derivative loss in the coupled fixed-point that the note misses? In particular, does the composition ψ=χ∘φ⁻¹ really give ψ∈H^s when φ∈H^s, for the specific Sobolev orders needed?

The flat-torus test (Step 52) permanently falsified Step 51's homogeneous energy closure. This note does NOT use energy estimates for existence; it uses Xu's fixed-point method. Confirm that these are genuinely different approaches.

## Integrated Scientific Memo

# 核验结论

耦合系统
\[
\begin{cases}
\partial_t\widehat g
=-2\widehat\chi^2(\Ric_{\widehat g}+\widehat g)
+\mathcal L_{\widehat\chi^2W}\widehat g,\\
\partial_t\widehat\chi
=\widehat\chi^2W(\widehat\chi)
\end{cases}
\]
确实是恢复几何坐标中固定 cutoff 流的正确系统。但 Step 53 **尚未证明**其短时存在定理。拉回恒等式、输运积分分部、平方差分解以及 Sobolev 复合本身成立；然而固定点论证遗漏了一个精确的一阶耦合项，并错误地使用了一个降阶 Sobolev 不等式，同时把退化抛物方程的加权导数增益写成了 \(\varepsilon\)-一致的非加权增益。

---

## 1. 拉回恒等式：正确

令
\[
Y_t=(\partial_t\varphi_t)\circ\varphi_t^{-1}
=-\widehat aW,\qquad \widehat a=\widehat\chi^2.
\]
则
\[
\frac d{dt}\varphi_t^*\widehat g
=\varphi_t^*(\partial_t\widehat g+\mathcal L_Y\widehat g),
\]
所以 Lie 导数恰好抵消：
\[
\partial_t(\varphi^*\widehat g)
=\varphi^*\!\left[-2\widehat a
(\Ric_{\widehat g}+\widehat g)\right].
\]

另一方面，
\[
\frac d{dt}(\widehat\chi\circ\varphi)
=\bigl(\partial_t\widehat\chi-\widehat aW(\widehat\chi)\bigr)\circ\varphi
=0.
\]
由初值可得
\[
\widehat\chi\circ\varphi=\chi,\qquad
\widehat a\circ\varphi=\chi^2.
\]
因此 \(g=\varphi^*\widehat g\) 满足
\[
\boxed{\partial_tg=-2\chi^2(\Ric_g+g)}.
\]

这准确修复了 Step 52 中固定 Eulerian 系数在拉回后变成 \(a\circ\varphi\) 的错误。

---

## 2. 主部与耦合阶数：主符号判断正确，但“lower-triangular”陈述不完整

二阶主符号确实是
\[
\widehat a\,\widehat g^{-1}*\widetilde\nabla^2\widehat g,
\]
故 \(\widehat\chi\) 在二阶主部中仅作为零阶系数出现。输运方程又因
\[
W(\widehat g,\widetilde g)\sim\widetilde\nabla V
\]
而在 \(H^k\) 估计中需要 \(V\) 的 \(k+1\) 阶信息。

但精确的 metric 方程还包含 Step 53 的 (2.1)、(4.1) 未写出的项：
\[
\mathcal L_{\widehat aW}\widehat g
=\widehat a\,\mathcal L_W\widehat g
+2\,\operatorname{sym}(d\widehat a\otimes W^\flat),
\]
即
\[
2\,\operatorname{sym}(d(\widehat\chi^2)\otimes W^\flat)
=4\widehat\chi\,\operatorname{sym}
(d\widehat\chi\otimes W^\flat)
\sim\widehat\chi\,\widetilde\nabla\widehat\chi*
\widetilde\nabla V.
\]

因此逐项微分 \(k\) 次时会出现
\[
\widehat\chi\,W*\widetilde\nabla^{k+1}\widehat\chi.
\]
所以“metric 在 \(k\) 阶只需要 \(\psi\) 的 \(k\) 阶”并非逐项成立。它只能在**能量层面**通过积分分部修复：把该导数移到 \(V\) 上，得到形如
\[
\widehat\chi\,\widetilde\nabla^{k+1}V\,
W\,\widetilde\nabla^k\widehat\chi,
\]
其最高阶 metric 因子带有 \(\widehat\chi\)，可望由加权耗散
\[
\int \widehat\chi^2
|\widetilde\nabla^{k+1}V|^2
\]
控制。

故准确表述应是：

* 主符号在 \(\widehat\chi\) 上无导数；
* metric–transport 耦合不是朴素逐项 lower-triangular；
* 经额外的 metric 能量积分分部后，存在一个可能闭合的**加权三角结构**；
* Step 53 尚未写出该估计。

---

## 3. 抛物增益：固定 \(\varepsilon\) 时正确，\(\varepsilon\to0\) 所需的一致版本不正确

对每个固定 \(\varepsilon>0\)，正则化方程严格抛物，确有
\[
V_\varepsilon\in C_tH^s\cap L^2_tH^{s+1}.
\]
因此固定 \(\varepsilon\) 下，
\[
\int_0^T\|\widehat aW\|_{H^s}\,dt
\lesssim \sqrt T\,
\|\widehat aW\|_{L^2_tH^s}
\]
是正确机制。

但退化极限中通常只有
\[
\int_0^T\!\!\int_M
(\widehat\chi^2+\varepsilon)
|\widetilde\nabla^{s+1}V_\varepsilon|^2
\le C,
\]
即
\[
\bigl\|
\sqrt{\widehat\chi^2+\varepsilon}\,
\widetilde\nabla^{s+1}V_\varepsilon
\bigr\|_{L^2_{t,x}}\le C,
\]
而非 \(\varepsilon\)-一致的
\[
\|V_\varepsilon\|_{L^2_tH^{s+1}}\le C.
\]
后者的常数一般随椭圆性下界 \(\varepsilon\) 退化。

不过速度含有额外权重 \(\widehat a=\widehat\chi^2\)，因此存在可行的加权修复。展开
\[
\widetilde\nabla^s(\widehat\chi^2W)
=\widehat\chi^2\widetilde\nabla^sW
+\sum_{j=1}^s
\widetilde\nabla^j(\widehat\chi^2)
\,\widetilde\nabla^{s-j}W.
\]
只有首项含有 \(V\) 的 \(s+1\) 阶导数，并且
\[
\|\widehat\chi^2\widetilde\nabla^{s+1}V\|_2
\le \|\widehat\chi\|_\infty
\|\widehat\chi\,\widetilde\nabla^{s+1}V\|_2.
\]
其余各项最多使用 \(V\) 的 \(s\) 阶导数，可由高阶 Sobolev 乘积估计处理。因此目标应是证明
\[
\|\widehat aW\|_{L^2_tH^s}
\le C\!\left[
\|\widehat\chi\widetilde\nabla^{s+1}V\|_{L^2_{t,x}}
+\sqrt T\,P\bigl(
\|V\|_{C_tH^s},\|\widehat\chi\|_{C_tH^s}
\bigr)\right].
\]
由此才可推出
\[
\widehat aW\in L^1_tH^s
\]
并一致地构造 \(\varphi\)。

此外，Step 53 §4.3 从 \(L^2_tH^s\) 速度写成 \(CT\) 小量并不成立；若仅有 \(L^2_t\) 控制，应得到 \(\sqrt T\) 因子。

---

## 4. 输运积分分部：正确，包括系数 \(\psi^2\)

令
\[
b=\psi^2W.
\]
对 \(|\alpha|=k\)，最高阶项为
\[
\int_M \widetilde\nabla^\alpha\psi\,
b^j\widetilde\nabla_j\widetilde\nabla^\alpha\psi
=-\frac12\int_M
\operatorname{div}_{\widetilde g}b\,
|\widetilde\nabla^\alpha\psi|^2.
\]
所以表面上的 \(k+1\) 阶 \(\psi\) 导数被消去。系数为 \(\psi^2\) 不破坏这一恒等式；它只是速度 \(b\) 的一部分。

标准交换子估计给出
\[
\|[\widetilde\nabla^k,b\cdot\widetilde\nabla]\psi\|_2
\lesssim
\|\widetilde\nabla b\|_\infty\|\psi\|_{H^k}
+\|b\|_{H^k}\|\widetilde\nabla\psi\|_\infty,
\]
加上固定背景曲率产生的低阶项。因此当 \(k>n/2+1\) 时，输运方程传播 \(H^k\) 不要求 \(\psi\in H^{k+1}\)。

需要注意的是，\(\nabla^k b\) 中含
\[
\psi^2\nabla^kW\sim
\psi^2\nabla^{k+1}V,
\]
所以 metric 的额外一阶仍须由上述**加权抛物耗散**提供。

---

## 5. \(I2\) 平方差分解：正确，但不能消除 \(W\) 的导数损失

恒等式
\[
\widehat a_1-\widehat a_2
=(\widehat\chi_1+\widehat\chi_2)
(\widehat\chi_1-\widehat\chi_2)
\]
确实使系数差对 \(\widehat\chi_1-\widehat\chi_2\) Lipschitz。对 \(r>n/2\)，正确的高阶估计是
\[
\|\widehat a_1-\widehat a_2\|_{H^r}
\le C\bigl(
\|\widehat\chi_1\|_{H^r}
+\|\widehat\chi_2\|_{H^r}
\bigr)
\|\widehat\chi_1-\widehat\chi_2\|_{H^r}.
\]
因此在固定高阶球内，乘子一致有界。仅用
\[
|\widehat a_1-\widehat a_2|
\le2|\widehat\chi_1-\widehat\chi_2|
\]
则只足以控制零阶乘积，不能替代高阶 Moser 估计。

更关键的是，\(I2\) 不处理
\[
W(U_1)-W(U_2)\sim\widetilde\nabla(U_1-U_2).
\]
Step 53 §4.4 所用
\[
\|U_1-U_2\|_{H^{\widetilde p+1}}
\le C\|U_1-U_2\|_{H^{\widetilde p}}
\]
是错误的；高阶球有界也不能使该不等式成立。至多有插值
\[
\|h\|_{H^{r+1}}
\le C\|h\|_{H^r}^{1/2}
\|h\|_{H^{r+2}}^{1/2},
\]
这只给出低阶距离的 \(1/2\)-Hölder 控制，不足以得到所宣称的 Banach 收缩。

metric 差方程还遗漏了
\[
d(\alpha_1^2-\alpha_2^2)*W_1
+d(\alpha_2^2)*(W_1-W_2),
\]
它们来自精确的
\(2\operatorname{sym}(d(\alpha^2)\otimes W^\flat)\) 项。

因此 (4.3)–(4.4) 尚未成立。修复必须在差分范数中保留加权抛物导数，例如
\[
\sup_{t\le T}\|\delta U(t)\|_{H^r}^2
+\int_0^T\!\!\int_M
(\alpha^2+\varepsilon)
|\widetilde\nabla^{r+1}\delta U|^2,
\]
并利用输运速度中的 \(\alpha^2\) 控制
\(\alpha^2\nabla^{r+1}\delta U\)。同时应对上述 \(d\alpha\)-交叉项积分分部并吸收到该耗散中。

---

## 6. 复合 \(\psi=\chi\circ\varphi^{-1}\)：没有独立的导数损失

若
\[
s>\frac n2+1,
\]
且 \(\varphi\) 是 \(H^s\) 微分同胚、Jacobian 有正下界，则
\[
\varphi^{-1}\in H^s,\qquad
\chi\circ\varphi^{-1}\in H^s
\]
对固定光滑 \(\chi\) 成立。定量常数实际依赖于
\[
\|\varphi\|_{H^s},\quad
\|\varphi^{-1}\|_{H^s},\quad
\inf_M\det D\varphi,
\]
而不只是 Step 53 所写的 \(\|\varphi\|_{H^s}\)。

若
\[
\widehat aW\in L^1([0,T];H^s),
\]
则短时间流保持为 \(H^s\) 微分同胚，且
\[
\int_0^T\|\nabla(\widehat aW)\|_\infty\,dt
\]
控制 Jacobian。故真正未解决的是 \(\varepsilon\)-一致的
\[
\widehat aW\in L^1_tH^s
\]
估计，而不是已知 \(H^s\) 微分同胚下的复合定理。

---

## 7. 与 Step 51 齐次曲率能量方法：确为不同方法

Step 51 试图证明
\[
E'(t)\le CE(t)
\]
型的非移位临界曲率能量闭合。平坦四维环面检验给出
\[
E(t)=48\pi^4t^2+O(t^3),\qquad
\frac{E'(t)}{E(t)}=\frac2t+O(1),
\]
因此该齐次不等式不可能成立。空间变化的 cutoff 通过
\(g\owedge\nabla^2a\) 从平坦初值产生真实曲率。

Xu 型路线则使用：

* \(\varepsilon\)-正则化的 DeTurck 方程；
* 冻结系数的线性抛物问题；
* 高阶 Sobolev 球与低阶差分估计；
* 输运交换子估计；
* \(\varepsilon\to0\) 紧性。

它不需要 \(E'\le CE\)，所以环面反例不否定该存在性路线。不过它也不能弥补上述耦合固定点中的缺失估计。JSON 的 19 项检查仅验证了代数和形式导数计数，其免责声明正确：它没有验证完整 PDE 存在性、Sobolev 乘积、收缩或紧性。

---

# 最终状态

可确认：

1. 耦合系统及其固定-cutoff 拉回完全正确；
2. 输运最高阶项可由积分分部消去，不需要 \(\psi\) 的额外一阶；
3. \(I2\) 给出系数关于 \(\psi\) 的高阶 Sobolev-Lipschitz 控制；
4. \(s>n/2+1\) 时，已知 \(H^s\) 微分同胚下的复合没有导数损失；
5. Xu 固定点路线与已被环面反例否定的齐次曲率能量路线确实不同。

但 **Theorem 5.1 尚未由 Step 53 证明**。精确缺口是构造一个 \(\varepsilon\)-一致的联合加权 metric–transport 差分估计，它必须同时处理：

\[
2\operatorname{sym}(d(\psi^2)\otimes W^\flat),
\]
\[
\psi^2\nabla^{r+1}\delta U
\quad\text{在输运差方程中的贡献},
\]
以及
\[
d(\psi_1^2-\psi_2^2)*W_1
+d(\psi_2^2)*(W_1-W_2).
\]

所需核心控制应是
\[
\sup_t\bigl(
\|\delta V\|_{H^r}^2+\|\delta\psi\|_{H^r}^2
\bigr)
+
\int_0^T
\|\psi\,\nabla^{r+1}\delta V\|_2^2\,dt
\]
型的加权范数，而不是 Step 53 所用的纯
\(C_tH^r\) 收缩范数。只有证明该估计并建立相应的 \(\varepsilon\)-一致紧性后，耦合短时存在定理才得到验证。