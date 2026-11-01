# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step9_noncollapsed_finiteness_and_all_dim_structure.md",
    "Sessions/S0910A02/workspace/data/step9_finiteness_constants.json",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md"
  ]
}
```

## Task

Verify the following claims for the positive branch of Yau Problem 26, checking the chain of implications against the actual source statements.

1. THEOREM A (Noncollapsed Positive Finiteness, dim 4): If |Ric_g - g|_op ≤ δ < 1/2 and Vol(M,g) ≥ v > 0 on a closed oriented 4-manifold, then M is one of at most C(δ,v) diffeomorphism types. The proof chain is: |Ric| ≤ 1+δ < 3; Myers diam ≤ π√(3/(1-δ)); Bishop-Gromov Vol(B₁(p)) ≥ c(δ)v for ALL p; Cheeger-Naber Theorem 1.12 applies. Check: does CN 1.12 require uniform noncollapse at every point or at one point? Is the Bishop-Gromov argument for uniform noncollapse correct when diam ≤ D?

2. THEOREM B (All-dimensional structure): For n ≥ 4, a sequence with |Ric_{g_i}-g_i|_op → 0, Vol ≥ v converges (up to subsequence) in GH to a space smooth away from a set of codim ≤ n-4, with Ric = g on the regular part. Check: is the bootstrap from C^{1,α} ∩ W^{2,q} convergence to smooth Einstein on the regular set correct?

3. SHA-YANG DICHOTOMY: The claim that for #_k(S²×S²), either δ_+ is bounded below for all large k, or collapse must occur. Check: is the logical chain from Theorem A + b₂ = 2k → ∞ to the dichotomy correct? Is there a gap in the argument (e.g., could δ₀ depend on k in a way that breaks the dichotomy)?

4. ε-REGULARITY CORRECTION: The claim that CN Theorem 6.1 is an ε-regularity for bounded Ricci (not Einstein), and what genuinely fails without Einstein is pointwise regularity scale r_x, not harmonic radius r_h. Check against the CN source.

5. BLOW-UP RICCI FLATNESS: The claim that at bubble scale t, |Ric_ĝ| = t²|Ric_g| ≤ t²(1+δ) → 0, so blow-ups are Ricci-flat independent of δ. Is this scaling correct for the operator norm?

## Output

# 科学核验备忘录

## 总结

1. **四维非塌缩有限性定理成立。** Cheeger–Naber 定理 1.12 只要求某一个基点的 \(B_1\) 体积下界；本文由 Myers 与 Bishop–Gromov 得到的逐点下界也是正确的。需补上算子范数到 CN 所用张量范数的维数因子。
2. **全维结构定理的核心部分成立。** 正则部分上的 \(C^{1,\alpha}\cap W^{2,q}\) 收敛足以把 \(\operatorname{Ric}_{g_i}-g_i\to0\) 传入调和坐标方程，并由 Schauder 理论得到光滑 Einstein 极限。不需要 \(\nabla\operatorname{Ric}_{g_i}\) 的估计。
3. **Sha–Yang 表述必须采用“所有充分大的 \(k\)”版本。** 原笔记中“对所有 \(k\)”的第一种情形不成立，因为 \(S^2\times S^2\) 本身有 \(\operatorname{Ric}=g\) 的乘积度量。尾部版本的逻辑完整，且可固定 \(\delta_0=1/4\)，不依赖 \(k\)。
4. **关于 CN 定理 6.1 的修正与源文一致。** 仅有双侧 Ricci 控制时得到的是调和半径 \(r_h\)；曲率正则尺度 \(r_x\) 还需要 Einstein 方程或 \(|\nabla\operatorname{Ric}|\) 控制。
5. **吹起缩放公式正确。** 若 \(\hat g=t^{-2}g\)，则
   \[
   \|\operatorname{Ric}_{\hat g}\|_{\mathrm{op},\hat g}
   =t^2\|\operatorname{Ric}_g\|_{\mathrm{op},g}.
   \]
   但 Step 9 第 6 节把同一 \(t\) 同时当作长度尺度和度量倍数，导致测试张量的幂次记号不一致。

---

## 1. 四维非塌缩有限性

设
\[
\|\operatorname{Ric}_g-g\|_{\mathrm{op},g}\le \delta<\frac12.
\]
则 Ricci 端同态的四个特征值 \(\rho_a\) 满足
\[
1-\delta\le \rho_a\le 1+\delta.
\]

### CN 的 Ricci 范数归一化

Cheeger–Naber 定理 1.12 写的是
\[
|\operatorname{Ric}|\le3.
\]
若这里采用通常的 Hilbert–Schmidt 张量范数，则
\[
|\operatorname{Ric}|^2=\sum_{a=1}^4\rho_a^2
\le4(1+\delta)^2<9.
\]
所以确有 \(|\operatorname{Ric}|<3\)。若按算子范数解释则更加直接。

因此 Step 9 中“\(\delta<2\) 即可推出 CN 归一化”只对算子范数成立；在通常张量范数下需要
\[
2(1+\delta)<3,
\]
恰好由 \(\delta<1/2\) 保证。`step9_finiteness_constants.json` 中的布尔值仍然正确，但其中 `ric_upper` 记录的是算子范数上界，而不是 CN 源文通常使用的张量范数。

### Myers 直径估计

有
\[
\operatorname{Ric}_g\ge(1-\delta)g=3K_\delta g,
\qquad
K_\delta=\frac{1-\delta}{3}.
\]
Myers 定理给出
\[
\operatorname{diam}(M,g)
\le D_\delta:=\frac{\pi}{\sqrt{K_\delta}}
=\pi\sqrt{\frac3{1-\delta}}.
\]

### Bishop–Gromov 逐点体积下界

对任意 \(p\in M\)，由于 \(D_\delta\ge\operatorname{diam}M\)，有
\[
B_{D_\delta}(p)=M
\]
（忽略可能的测度零最远点不影响体积）。正曲率模型的 Bishop–Gromov 比较给出
\[
\frac{\operatorname{Vol}B_1(p)}{V_{K_\delta}(1)}
\ge
\frac{\operatorname{Vol}B_{D_\delta}(p)}
     {V_{K_\delta}(D_\delta)}.
\]
故
\[
\operatorname{Vol}B_1(p)
\ge
\frac{V_{K_\delta}(1)}{V_{K_\delta}(D_\delta)}
\operatorname{Vol}M
\ge a_\delta v,
\]
其中
\[
a_\delta:=\frac{V_{K_\delta}(1)}{V_{K_\delta}(D_\delta)}>0.
\]
这个推导对每个 \(p\) 都成立。数据文件中的数值，例如 \(\delta=0.1\) 时的 \(a_\delta\approx0.01526734\)，与该公式一致。

### CN 定理 1.12 的基点要求

源文定理 1.12 的条件是
\[
|\operatorname{Ric}|\le3,\qquad
\operatorname{Vol}(B_1(p))>\mathrm v,\qquad
\operatorname{diam}M\le D,
\]
其中只出现一个基点 \(p\)。因此逐点非塌缩比源文需要的更强。由于上面得到的是“\(\ge a_\delta v\)”，可向 CN 输入
\[
\mathrm v_{\rm CN}=\frac12a_\delta v
\]
以满足严格不等号。

于是 CN 定理给出至多
\[
C\!\left(\tfrac12a_\delta v,D_\delta\right)
\]
个光滑微分同胚型。源文不区分定向；固定底层连通流形至多产生两个定向微分同胚型，所以定向版本仍然有限。

### Betti 数表述中的一处数值错误

有限多个微分同胚型确实推出存在
\[
B(\delta,v)=\max b_2(M_j),\qquad
X(\delta,v)=\max\chi(M_j).
\]
但 Step 9 的句子
\[
b_2\le N-2
\]
不能由“至多 \(N\) 个微分同胚型”推出；类型数量 \(N\) 与这些类型的 Betti 数大小没有这种数值关系。

正 Ricci 通过 Bochner 给出 \(b_1=0\)，定向四维 Poincaré 对偶给出
\[
\chi=2+b_2,
\]
所以 \(b_2\) 与 \(\chi\) 的有限上界成立，只应写成上述最大值形式。

---

## 2. 全维非塌缩结构与正则部分的 Einstein 方程

设 \(n\ge4\)，
\[
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\le\delta_i\to0,
\qquad
\operatorname{Vol}(M_i,g_i)\ge v.
\]

舍去有限项后可取 \(\delta_i\le1/2\)，于是
\[
\operatorname{Ric}_{g_i}\ge\frac12g_i.
\]
取
\[
K_0=\frac1{2(n-1)},\qquad
D_0=\pi\sqrt{2(n-1)},
\]
Myers 与 Bishop–Gromov 如上一节给出统一直径上界及所有基点的统一 \(B_1\) 体积下界。

若 CN 的 \(|\operatorname{Ric}|\) 是张量范数，则应使用
\[
|\operatorname{Ric}_{g_i}|
\le\sqrt n\,(1+\delta_i).
\]
因为 \(n\ge4\) 且 \(\sqrt n<n-1\)，对充分大的 \(i\) 有
\[
|\operatorname{Ric}_{g_i}|\le n-1.
\]
Step 9 中写成“\(|\operatorname{Ric}|\le2<n-1\)”只适用于算子范数；改用上式即可完全匹配 CN 定理 1.4。

由 Gromov 紧致性和 CN 定理 1.4，可取子列收敛到紧度量空间 \(X\)，其奇异集 \(\mathcal S\) 闭且
\[
\dim_{\mathrm H}\mathcal S\le n-4,
\]
源文也给出相应 Minkowski 维数估计。

### 正则部分上的极限方程

设 \(K\Subset X\setminus\mathcal S\)。正则性理论给出 \(K\) 上统一正的调和半径；经局部微分同胚拉回后，
\[
g_i\longrightarrow g_\infty
\quad\text{于 }C^{1,\alpha}\cap W^{2,q}
\]
中成立，适当取子列可对任意 \(\alpha<1,\ q<\infty\) 使用。

写
\[
\operatorname{Ric}_{g_i}=g_i+E_i,
\qquad
\|E_i\|_{\mathrm{op},g_i}\le\delta_i.
\]
调和坐标中度量满足
\[
-\frac12g_i^{ab}\partial_a\partial_b(g_i)_{jk}
+Q_{jk}(g_i,\partial g_i)
=(g_i)_{jk}+(E_i)_{jk}.
\]
调和坐标内 \(g_i\) 与欧氏度量一致等价，因此
\[
(E_i)_{jk}\to0
\quad\text{于 }L^\infty.
\]
同时 \(C^{1,\alpha}\) 收敛使
\[
Q(g_i,\partial g_i)\to Q(g_\infty,\partial g_\infty)
\]
局部一致。故极限在分布意义下满足
\[
-\frac12g_\infty^{ab}\partial_a\partial_b(g_\infty)_{jk}
+Q_{jk}(g_\infty,\partial g_\infty)
=(g_\infty)_{jk}.
\]
由于 \(g_\infty\in C^{1,\alpha}\)，系数和右端具有 Hölder 正则性，内部 Schauder 理论给出
\[
g_\infty\in C^{2,\alpha}.
\]
随后对同一拟线性椭圆系统反复使用 Schauder 估计得到 \(g_\infty\in C^\infty\)，且
\[
\operatorname{Ric}_{g_\infty}=g_\infty.
\]

这一过程不使用 \(\nabla E_i\) 或 \(\nabla\operatorname{Ric}_{g_i}\)：各个 \(g_i\) 未必具有高阶统一估计，但 \(E_i\to0\) 的 \(L^\infty\) 收敛足以使极限满足光滑 Einstein 方程。

### 关于切锥横截面

Step 9 的 Theorem B(d) 中“每个切锥 \(C(Y)\) 的 \(Y\) 都是光滑流形”没有由 CN 定理 1.4 推出。源文支持的是：

- 切锥是非塌缩度量锥；
- 吹起后的 Ricci 范数趋于零；
- 切锥的正则部分 Ricci-flat；
- 在 \(Y\) 的正则部分，
  \[
  \operatorname{Ric}_{Y}=(n-2)g_Y.
  \]

在一般 \(n\) 中，\(Y\) 自身仍可带有奇异子集。四维情形可结合 CN 第 8 节及 Corollary 8.85 得到孤立 orbifold 点和
\[
C(Y)=\mathbb R^4/\Gamma.
\]

---

## 3. Sha–Yang 尾部二分

记
\[
M_k=\#_k(S^2\times S^2),\qquad
d_k:=\delta_+(M_k).
\]

### 原“对所有 \(k\)”版本不成立

当 \(k=1\) 时，
\[
M_1=S^2\times S^2.
\]
两个单位二球的乘积度量满足
\[
\operatorname{Ric}=g,
\]
所以
\[
d_1=0.
\]
因此不存在 \(c>0\) 使 \(d_k\ge c\) 对所有 \(k\ge1\) 成立。

### 正确的尾部版本

以下两种情形恰好互斥且穷尽：

1. 存在 \(K\) 和 \(c>0\)，使
   \[
   d_k\ge c\qquad(k\ge K);
   \]
2. 存在 \(k_j\to\infty\) 及 \(M_{k_j}\) 上的度量 \(g_j\)，使
   \[
   \|\operatorname{Ric}_{g_j}-g_j\|_{\mathrm{op}}\to0,
   \qquad
   \operatorname{Vol}(M_{k_j},g_j)\to0.
   \]

若第一种情形不成立，可选 \(k_j\ge j\) 使 \(d_{k_j}<1/(2j)\)，再按下确界定义选 \(g_j\) 使
\[
\|\operatorname{Ric}_{g_j}-g_j\|_{\mathrm{op}}<\frac1j.
\]
若体积不趋于零，则存在 \(v_0>0\) 和子列满足
\[
\operatorname{Vol}(M_{k_j},g_j)\ge v_0.
\]
对充分大的 \(j\)，Ricci 误差小于固定常数
\[
\delta_0=\frac14.
\]
Theorem A 因而给出有限多个微分同胚型。但
\[
b_2(M_{k_j})=2k_j\to\infty,
\]
所以这些流形两两不可能属于有限多个微分同胚型，矛盾。

这里 \(\delta_0=1/4\) 从头到尾固定，不依赖 \(k\)，不存在随 \(k\) 变化而破坏推理的问题。塌缩结论只涉及 Ricci 误差趋于零的度量序列，并不涉及任意 Sha–Yang 正 Ricci 度量。

### ALE 区域数量的附带修正

Step 9 第 3 节从
\[
\int|W|^2\gtrsim k
\]
以及“每个 ALE 泡具有一个能量下界”推到“至少 \(O(k)\) 个 ALE 区域”，这个方向不能成立。每个泡的能量下界结合总能量上界可以控制泡的数量上界；要从总能量下界推出数量下界，还需要每个泡的统一能量上界或统一拓扑复杂度上界。单个 ALE 泡原则上可以承载随 \(k\) 墈长的能量。

---

## 4. CN 定理 6.1 的实际内容

源文 Theorem 6.1 明确假设
\[
|\operatorname{Ric}|\le\epsilon(n,v),\qquad
\operatorname{Vol}(B_1(p))>v,
\]
并且
\[
d_{\mathrm{GH}}\!\left(
B_2(p),B_2(0\in\mathbb R^{n-3}\times C(Y))
\right)<\epsilon.
\]
其结论是
\[
r_h(p)\ge1.
\]
这确实是不要求 Einstein 方程的调和半径 \(\epsilon\)-正则性定理。

源文随后写明：若 \(M\) 还是 Einstein，则可推出
\[
\sup_{B_1(p)}|\operatorname{Rm}|\le1.
\]
相同区分还出现在：

- Theorem 1.8：仅有双侧 Ricci 控制时估计调和半径；Einstein 时估计曲率正则尺度；
- Remark 1.11：加入 \(|\nabla\operatorname{Ric}|\) 上界也可估计曲率正则尺度；
- Theorem 1.13：四维一般双侧 Ricci 情形给出调和半径弱 \(L^2\) 型估计，Einstein 情形才可替换为 \(r_x\)。

因此 Step 9 的修正与源文一致。需要保留 Theorem 6.1 的非塌缩、锥近似和缩放后小 Ricci 三项假设；它不是单由 \(|\operatorname{Ric}|\le C\) 得到任意点的 \(r_h\) 下界。

---

## 5. 吹起后的 Ricci 缩放

令
\[
\hat g=t^{-2}g,
\]
其中 \(t\) 是长度尺度。常数倍缩放不改变 Levi–Civita 联络，也不改变作为 \((0,2)\)-张量的 Ricci：
\[
\operatorname{Ric}_{\hat g}=\operatorname{Ric}_g.
\]
但
\[
\hat g^{-1}=t^2g^{-1},
\]
所以
\[
\|\operatorname{Ric}_{\hat g}\|_{\mathrm{op},\hat g}
=t^2\|\operatorname{Ric}_g\|_{\mathrm{op},g}.
\]
Hilbert–Schmidt 范数也具有同样的 \(t^2\) 因子。

若
\[
\operatorname{Ric}_g=g+E,\qquad
\|E\|_{\mathrm{op},g}\le\delta,
\]
则
\[
\operatorname{Ric}_{\hat g}
=t^2\hat g+E,
\qquad
\|E\|_{\mathrm{op},\hat g}
=t^2\|E\|_{\mathrm{op},g}.
\]
从而
\[
\|\operatorname{Ric}_{\hat g}\|_{\mathrm{op},\hat g}
\le t^2(1+\delta)\to0.
\]
所以任何具有充分局部正则收敛的吹起极限都是 Ricci-flat；仅有 GH 收敛时，相应结论首先作用于极限正则部分。

### Step 9 投影桥中的尺度记号

Step 9 第 4 节使用
\[
\hat g=t^{-2}g,
\]
此时 \(t\) 是长度尺度。但第 6 节又写
\[
g\simeq t\,g_{\rm flat},\qquad
d\mu_g\simeq t^2d\mu_{\rm flat},\qquad
|\phi|_g\simeq t^{-1}|\phi|_{\rm flat}.
\]
后三式把 \(t\) 当作度量倍数。若 \(t\) 仍是长度尺度，正确公式应为
\[
g\simeq t^2g_{\rm flat},\qquad
d\mu_g\simeq t^4d\mu_{\rm flat},\qquad
|\phi|_g\simeq t^{-2}|\phi|_{\rm flat}
\]
（这里 \(\phi\) 是未额外重标度的协变二张量），因而
\[
\|\phi\|_{L^1(g)}\simeq t^2.
\]
原第 6 节公式在令
\[
\tau=t^2
\]
后才一致：
\[
g\simeq\tau g_{\rm flat},\quad
d\mu\simeq\tau^2d\mu_{\rm flat},\quad
|\phi|\simeq\tau^{-1},\quad
\|\phi\|_{L^1}\simeq\tau.
\]
因此投影恒等式中的主项和 \(O(\delta t)\) 误差必须统一采用长度尺度 \(t\) 或度量尺度 \(\tau\)。

此外，orbifold 切锥尺度可能收敛到 \(\mathbb R^4/\Gamma\)，而真正解析 ALE 核心的吹起尺度通常收敛到非平坦 Ricci-flat ALE 空间，例如 Eguchi–Hanson。Step 9 把“inner bubble scale”直接写成收敛到 \(\mathbb R^4/\Gamma\)，应区分锥颈尺度与 ALE 核心尺度。