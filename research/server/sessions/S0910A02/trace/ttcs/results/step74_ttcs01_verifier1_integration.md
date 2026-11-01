# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 74,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step74_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step74_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify three structural results that reshape the noncollapsed P₄⁺ proof architecture for Yau Problem 26.

1. ELL-CLASSIFICATION: The claim is that among homogeneous degree-ℓ TT/radial-null modes on a cone R^d/Gamma (d≥4), the unweighted nuclear-norm mass integral ∫r^{1-ℓ}dr gives H₂=log(R/b) for ℓ=2 (logarithmic) and H_ℓ=b^{2-ℓ}/(ℓ-2)→∞ power-scale for ℓ>2. Check the radial integral, the resulting lower bound on operator-norm defect, and the conclusion that ℓ=2 is the unique unweighted log-critical mode.

2. STRUCTURAL IMPOSSIBILITY: The argument combines two inputs: (a) Ozuch's scaling hierarchy showing the k-th Biquard obstruction creates O(t^k) error in the (0,2)-form on the ALE core, hence O(t^{k-1}) in operator norm after raising index; and (b) the near-pinched construction FND:A1construction with dominant error O(1/|log a|). Since t~a^2 and O(a^{2(k-1)}) << O(1/|log a|) for k≥2, the claim is that no C⁰ Ricci-endomorphism pinching theorem can force higher obstructions to vanish. Check whether this argument is valid, whether there is a logical gap or hidden assumption, and whether any additional sequence-level mechanism could circumvent it.

3. PRODUCT PROPAGATION: If (O⁴,g_O) is a positive Einstein 4-orbifold with Ric=σg and isolated A₁ points, and M⁴ carries near-pinched metrics g_a with δ(g_a)≤C/|log a|, then for n≥6, the product M⁴×S^{n-4}(Ric=σg) has δ(product)=δ(g_a) because Ric is block-diagonal on a product. Check the product Ricci formula, the operator-norm equality, and the gap at n=5 (S¹ has Ric=0, incompatible with σ>0).

## Integrated Scientific Memo

# 核验结论

三项结果的核心计算分别如下：

1. **ELL-CLASSIFICATION：成立。**  
   对所述纯齐次 TT/radial-null 模，径向质量确为
   \[
   H_\ell(b,R)=
   \begin{cases}
   \log(R/b),&\ell=2,\\[1mm]
   \dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell>2,
   \end{cases}
   \]
   因而 \(\ell=2\) 是该类纯多项式模中唯一的无权对数临界次数。

2. **STRUCTURAL IMPOSSIBILITY：应作带限定的肯定。**  
   幂次与对数的比较正确，并确实说明：仅由无权 \(C^0\) Ricci-endomorphism 缺陷 \(\delta_i\to0\)，不能推出高阶障碍系数消失。不过，当前材料尚未直接证明某个具体 mixed-row 配置确有非零高阶障碍；此外，一般“第 \(k\) 个障碍给出 \(O(t^k)\) 残差”须核准 Ozuch 的归一化。故已证明的是**这种推理机制不可能成立**，不是已构造出具体非零高阶障碍反例。

3. **PRODUCT PROPAGATION：度量计算成立，但不能推出普遍维数归约。**  
   对特定乘积流形，
   \[
   \delta_\sigma(g_a\oplus g_N)=\delta_\sigma(g_a)
   \]
   在 \(n\ge6\) 时完全正确，\(n=5\) 的 \(S^1\) 障碍也正确。但这不证明
   \(P_4^+\Rightarrow P_n^+\)，也不证明任意高维证明都必须解决四维因子问题。

---

## 1. 齐次模与唯一对数临界次数

写
\[
K_\ell(r\theta)=r^\ell Y_\ell(\theta),\qquad
o_\ell=r^{-(d+2\ell-2)}K_\ell
      =r^{-(d+\ell-2)}Y_\ell(\theta).
\]
这里齐次性必须解释为**笛卡尔分量齐次性**。于是
\[
\|o_\ell(r,\theta)\|_*
=r^{-(d+\ell-2)}\|Y_\ell(\theta)\|_*.
\]
结合
\[
dV=r^{d-1}\,dr\,d\theta
\]
得到
\[
\int_A\|o_\ell\|_*\,dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr,
\]
其中
\[
J_{K_\ell}
=\int_{S^{d-1}/\Gamma}\|K_\ell\|_{*,r=1}\,d\theta.
\]
因此
\[
H_\ell(b,R)=
\begin{cases}
\log(R/b),&\ell=2,\\[1mm]
\dfrac{b^{2-\ell}-R^{2-\ell}}{\ell-2},&\ell>2.
\end{cases}
\]

在约定
\[
D\Ric_e u=-\frac12\Delta u+\text{规范项}
\]
下，测试张量 \(o_\ell\) 的无迹、无散和 radial-null 性质使规范项的体积分及边界项消失。由于
\[
\partial_rK_\ell=\frac{\ell}{r}K_\ell,\qquad
\partial_ro_\ell=-\frac{d+\ell-2}{r}o_\ell,
\]
Green–Wronskian 公式给出
\[
\int_A\langle D\Ric_eu,o_\ell\rangle
=-\frac{d+2\ell-2}{2}I_{K_\ell},
\]
其中
\[
I_{K_\ell}
=\int_{S^{d-1}/\Gamma}|K_\ell|_{r=1}^2\,d\theta .
\]

由算子范数与核范数对偶，
\[
\boxed{
\|D\Ric_eu\|_{\mathrm{op},\infty}
\ge
\frac{(d+2\ell-2)I_{K_\ell}}
{2J_{K_\ell}H_\ell(b,R)}.
}
\]

故：

- \(\ell=2\)：
  \[
  \|D\Ric_eu\|_{\mathrm{op},\infty}
  \ge
  \frac{(d+2)I_K}{2J_K\log(R/b)}.
  \]
- \(\ell>2\)，固定 \(R\) 且 \(b/R\to0\)：
  \[
  H_\ell(b,R)\sim\frac{b^{2-\ell}}{\ell-2},
  \qquad
  \|D\Ric_eu\|_{\mathrm{op},\infty}
  \gtrsim b^{\ell-2}\to0.
  \]

因此，**在纯齐次整数多项式模范围内，\(\ell=2\) 是唯一的无权对数临界模。**

必须保留三个边界条件：

- 结论目前属于线性化 Ricci；非线性度量需另控端点 \(C^1\) 误差和非线性余项。
- \(r^\ell\log r\) 共振项不在此分类内。
- 即使 \(\ell=2\)，也只有
  \[
  \delta_iL_i\gtrsim1,
  \]
  并非尺度无关的正下界；若 \(L_i\to\infty\)，仍可有 \(\delta_i\to0\)。

---

## 2. 高阶障碍为何不能由 \(\delta\to0\) 单独消去

若 ALE 核心尺度满足
\[
g_t\sim t\,g_{\mathrm{ALE}},
\]
而第 \(k\) 阶残差作为协变二张量为
\[
E_t=O(t^k)
\]
（相对于未缩放 ALE 背景测量），则升一个指标后
\[
E_t^{\sharp_{g_t}}
=g_t^{-1}E_t
=O(t^{k-1}).
\]
所以第一阶残差产生 \(O(1)\) Ricci-endomorphism 缺陷，而 \(k\ge2\) 时产生
\[
O(t^{k-1})\to0.
\]

若 \(t\asymp a^q\)，其中任意固定 \(q>0\)，则
\[
a^{q(k-1)}|\log a|\to0\qquad(k\ge2),
\]
从而
\[
t^{k-1}=o\!\left(\frac1{|\log a|}\right).
\]
因此，在 FND:A1construction 的
\[
\delta(g_a)\le \frac C{|\log a|}
\]
背景下，高阶障碍的幂次贡献可完全落在主导对数误差之下。

严格可得的逻辑结论是：

> 若 pinching 信息仅为无权 \(\delta_i\to0\)，且没有 \(\delta_i\) 与 \(t_i\) 的额外速率关系，那么任何形如
> \[
> \delta_i\ge c|\mathcal O_k|t_i^{k-1}
> \]
> 的估计都不能推出 \(\mathcal O_k=0\)。

但需修正两处过强表述：

1. **尚未得到具体非零障碍实例。**  
   supplied material 中 mixed rows 的二阶障碍仍未计算。因此不能据尺度比较直接断言“存在第一障碍为零而第二障碍非零的具体配置”；只能断言即便其非零，\(\delta\to0\) 也无法排除它。

2. **Ozuch 一般 \(k\) 阶层级需核准。**  
   已给材料明确支持前两阶的层级性描述，但一般
   \[
   E_t=O(t^k)
   \]
   是否指 Einstein 残差本身、度量展开误差，及其使用何种缩放范数，仍应由原文形式展开确认。第一阶 \(O(t)\mapsto O(1)\) 的一致性支持该解释，但不能替代归一化核查。

此外，齐次次数 \(\ell\) 与 Biquard–Ozuch 障碍阶数 \(k\) 尚无一般识别定理。因此：

- “\(\ell=2\) 是唯一无权对数临界齐次模”已经证明；
- “第一 Biquard 障碍是唯一可检测障碍”应主要依赖经核准的 \(t\)-层级，而不能仅从 \(\ell\)-分类推出。

额外序列信息可以绕过上述不可能性，例如
\[
\delta_i=o(t_i^{k-1}),
\]
相应加权缺陷控制、归一化残差
\(t_i^{1-k}(\Ric-\sigma g)\) 的收敛、固定非退化尺度，或“第一障碍消失蕴含整个塔消失”的代数刚性。它们都严格强于单独的 \(\delta_i\to0\)。

---

## 3. 乘积传播及其准确范围

令 \(m=n-4\)，并在
\[
M^4\times S^m
\]
上取
\[
G_a=g_a\oplus g_N.
\]
乘积 Levi-Civita 联络分裂，故
\[
\Ric_{G_a}=\Ric_{g_a}\oplus\Ric_{g_N}.
\]
若
\[
\Ric_{g_N}=\sigma g_N,
\]
则
\[
(\Ric_{G_a}-\sigma G_a)^{\sharp_{G_a}}
=
(\Ric_{g_a}-\sigma g_a)^{\sharp_{g_a}}\oplus0.
\]
对自伴块对角算子，
\[
\|A\oplus B\|_{\mathrm{op}}
=\max\{\|A\|_{\mathrm{op}},\|B\|_{\mathrm{op}}\},
\]
所以逐点及取全局上确界后均有
\[
\boxed{\delta_\sigma(G_a)=\delta_\sigma(g_a).}
\]

单位圆球 \(S^m\) 满足
\[
\Ric_{g_{\rm round}}=(m-1)g_{\rm round}.
\]
取
\[
g_N=\frac{m-1}{\sigma}g_{\rm round}
=\frac{n-5}{\sigma}g_{\rm round}
\]
即可令 \(\Ric_{g_N}=\sigma g_N\)，这要求 \(m\ge2\)，即 \(n\ge6\)。

当 \(n=5\) 时，辅助因子是一维的，而所有一维 Riemann 度量都有
\[
\Ric=0.
\]
因此其缺陷块为
\[
(0-\sigma g_{S^1})^\sharp=-\sigma I,
\]
范数为 \(\sigma\)，不会趋于零。正 Einstein 情形下的直接乘积传播确实在 \(n=5\) 失败。

### 能够严格宣称的传播结论

- 对每个 \(n\ge6\)，四维 near-pinched family 产生特定流形
  \[
  M^4\times S^{n-4}
  \]
  上具有完全相同缺陷的 near-pinched family。
- 孤立 \(A_1\) 点在极限乘积中变为 \(A_1\times S^{n-4}\) 型余维四奇异层，因此高维非塌缩分析必须允许此类模型。
- 若 \(M^4\) 已有 Einstein 度量且其常数可与球因子匹配，则相应乘积度量是 Einstein。

不能由此宣称：

\[
P_4^+\Longrightarrow P_n^+
\]
对所有 \(n\ge6\) 成立，因为 \(P_n^+\) 量化所有闭 \(n\)-流形，而乘积只覆盖特殊子类。反方向的“高维证明必然解决四维 crux”也不成立：即使
\(M^4\times S^{n-4}\) 有 Einstein 度量，该度量未必分裂，因而不能反推出 \(M^4\) 有 Einstein 度量。

综上，产品结果是**特定乘积家族上的 near-pinching 与存在性传播**，不是普遍的维数归约定理。