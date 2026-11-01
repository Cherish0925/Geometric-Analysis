# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 81,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step81_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step81_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify and extend the following analysis of the harmonic-form alignment mechanism for positive Einstein 4-manifolds.

The key result: the summed Weitzenböck chain for b_+ independent harmonic self-dual forms on a positive Einstein 4-manifold reduces, after Cauchy-Schwarz with θ=0 (rank-1 T) and κ=1 (constant trT), to EXACTLY the Gursky-LeBrun inequality ∫|W+|² ≥ ∫s²/24, independent of b_+. The margin for χ=8, τ=0 rows is exactly √(3/2) ≈ 22.5%.

Three questions to verify and check for errors or missed opportunities:

1. Is the b_+ cancellation correct? The chain is: (s/3)b_+ ≤ 2√(2/3)(∫|W+|²)^{1/2}(∫(trT)²)^{1/2}, and with Q-orthonormal forms, ∫trT = b_+, κ=1 gives (∫(trT)²)^{1/2} = b_+/√V, so b_+ cancels. Is this the sharpest possible use of the Weitzenböck formula, or is there a better way to exploit b_+ ≥ 3 that doesn't go through the crude α·trT bound?

2. The degeneracy defect: on b_+ ≥ 2 Einstein, β ≠ -α/2 somewhere (otherwise Kähler, b_+=1). Does any known result quantify the measure or depth of this deviation? Does the refined Kato |∇W+|² ≥ (5/3)|∇|W+||² (Gursky-LeBrun) combine with a Sobolev inequality to give a quantitative strict inequality for b_+ ≥ 2?

3. The CLR/spectral reformulation: the Weitzenböck operator L = ∇*∇ - 2W+ + (s/3) has b_+ zero modes. On Kähler (b_+=1): potential V = diag(0,6,6) ≥ 0, one zero mode with zero potential. For b_+ = 3: need 3 zero modes, forcing more negative potential. Does this give a b_+-dependent Weyl bound through any known spectral inequality (CLR, Li-Yau, Berezin, or other)?

## Integrated Scientific Memo

# 核验结论

核心算术正确，但原分析有四处重要修正：

1. \(b_+\) 的确从归一化后的粗链中消去；然而 \(\kappa=1\) 不是结论，而是额外的“总密度恒定”极端情形。因此该粗链只在 \(\kappa=1\) 模型中取得 Gursky–LeBrun 的数值常数，并未重新证明其一般定理。
2. \(22.47\%\) 是 Bishop 上界处的形式最小余量；对 \(\chi=8\) 流形，Bishop 等号不可能，实际余量严格更大但无统一量化。
3. \(\theta=t_2/\operatorname{tr}T\) 的最大值不是 \(1/3\)，而是 \(1/2\)。因此“\(A>18\) 时无论多各向同性都失败”是错误的。
4. 原 CLR 公式既漏掉可能的第二个负势通道，也不能计数阈值零模。必须先作 coercive shift；修正后仍只给出 \(A=\int|W^+|^2/V\) 的下界，不能单独排除这些流形。

---

## 1. 精确的 \(b_+\)-消去及其适用范围

令 \(b=b_+\)，取 \(L^2\)-正交归一调和自对偶形式 \(\{\omega_a\}_{a=1}^b\)，并定义
\[
T=\sum_a\omega_a\otimes\omega_a,\qquad
f=\operatorname{tr}T=\sum_a|\omega_a|^2,
\qquad
G=\sum_a\int|\nabla\omega_a|^2.
\]
则
\[
\int f=b
\]
且求和后的 Weitzenböck 恒等式为
\[
G+\frac{s}{3}b=2\int\langle W^+,T\rangle.
\]
若 \(\alpha\) 是 \(W^+\) 最大特征值，则
\[
\langle W^+,T\rangle\le \alpha f
 \le \sqrt{\frac23}|W^+|f.
\]
因此，记
\[
E_+=\int|W^+|^2,\qquad
\kappa^2=\frac{V\int f^2}{b^2}\ge1,
\]
有
\[
\frac Gb+\frac s3
 \le 2\sqrt{\frac23}\,\kappa\sqrt{\frac{E_+}{V}}.
\]
所以 \(b\) 确实完全消去；这是对任意 \(\kappa\) 都成立的。丢掉 \(G\) 后得到
\[
\frac{E_+}{V}\ge \frac{s^2}{24\kappa^2}.
\]

关键是 Jensen 只给出 \(\kappa\ge1\)，并不给出 \(\kappa=1\)。等号恰好要求
\[
f=\frac bV\quad\text{a.e.}
\]
当且仅当人为置 \(\kappa=1\) 时，上式变成
\[
E_+\ge \frac{s^2}{24}V.
\]
这与 Gursky–LeBrun 不等式具有完全相同的常数，但粗求和链并未对一般的非恒定 \(f\) 推导该定理。Gursky–LeBrun 的一般结论依赖 refined Kato、Bochner 和 Yamabe 论证。Kähler–Einstein \(\mathbb{CP}^2\) 中 Kähler 形式平行、长度恒定，所以正好实现 \(\kappa=1\) 并使该模型链取等。

### \(\chi=8,\tau=0\) 的余量

在 \(\operatorname{Ric}=3g,\ s=12\) 归一化下，
\[
E_+=32\pi^2-3V,\qquad
A:=\frac{E_+}{V}=\frac{32\pi^2}{V}-3.
\]
Bishop 给出 \(V\le 8\pi^2/3\)，故 \(A\ge9\)。形式上的 rank-one、\(\kappa=1\) 上界与所需左端之比为
\[
\sqrt{\frac A6}.
\]
在 Bishop 体积处，
\[
\sqrt{\frac96}=\sqrt{\frac32}=1.224744\ldots,
\]
即 \(22.474\%\)。但 Bishop 等号迫使流形为圆球；因此在 \(\chi=8\) 上实际有 \(A>9\)，余量严格大于 \(22.474\%\)，只是现有资料不给出统一严格幅度。

---

## 2. 比 \(\alpha f\) 更精确的矩阵形式

因为 \(W^+\) 无迹，真正参与配对的是
\[
T_0=T-\frac f3I:
\qquad
\langle W^+,T\rangle=\langle W^+,T_0\rangle
 \le |W^+|\,|T_0|.
\]
若 \(t_1\ge t_2\ge t_3\ge0\) 是 \(T\) 的特征值，\(r_i=t_i/f\)，则
\[
q(T)^2:=\frac{|T_0|^2}{f^2}
 =r_1^2+r_2^2+r_3^2-\frac13,
\qquad
0\le q(T)\le\sqrt{\frac23}.
\]
故有更锋利的积分链
\[
G+\frac{s}{3}b
\le
2E_+^{1/2}
\left(\int f^2q(T)^2\right)^{1/2}.
\]
典型值为
\[
\begin{array}{c|c}
(t_1,t_2,t_3)/f&q(T)\\ \hline
(1,0,0)&\sqrt{2/3}\\
(1/2,1/2,0)&1/\sqrt6\\
(1/3,1/3,1/3)&0.
\end{array}
\]
因此 \(b_+\)-敏感性只能通过以下量进入：

- \(T\) 的定量各向同性，即对 \(q(T)\) 的加权上界；
- 对浓度因子 \(\kappa\) 的上界；
- 或保留并定量利用 \(G/b\)。

仅凭 \(\int f=b\) 和点态矩阵代数无法保留 \(b\)。

### 原 \(\theta\) 分析的修正

令 \(\theta=t_2/f\)，并在给定 \(\theta\) 时取最坏情况 \(t_3=0\)。则
\[
\langle W^+,T\rangle
\le
\alpha f-(\alpha-\beta)t_2-(\alpha-\gamma)t_3,
\]
对 \(|W^+|=1\) 优化得
\[
C_\theta
=
\sqrt{\frac23-2\theta+2\theta^2}.
\]
这确实重现 \(A=9\) 时
\[
\theta_*=0.127322\ldots.
\]

但
\[
0\le\theta=\frac{t_2}{f}\le\frac12,
\]
不是 \(1/3\)。\(1/3\) 只是完全各向同性的值。因此：

- 在 rank-two 均分构型 \((1/2,1/2,0)\) 下，系数为 \(1/\sqrt6\)，形式阈值可达到 \(A=24\)；
- 完全各向同性时 \(\langle W^+,T\rangle=0\)，与 \(s>0\) 的 Weitzenböck 左端对任意 \(A\) 都矛盾。

故不存在原文声称的绝对 \(A=18\) 截止。

### 点态秩能给出什么

当 \(b_+\ge2\) 时，两独立调和自对偶形式不能在开集上处处共线。若 \(\eta=u\omega\) 且 \(\omega\ne0\)，则 \(\omega\) 是非退化自对偶二形式；由
\[
d\omega=d\eta=0
\]
得 \(du\wedge\omega=0\)，从而 \(du=0\)，再由唯一延拓得到全局线性相关。结合解析性可得
\[
\operatorname{rank}T\ge2\quad\text{a.e.},
\]
从而 \(q(T)<\sqrt{2/3}\) 几乎处处，但没有统一差距。

不能仅因有三个全局独立截面就断言 \(T\) 几乎处处满秩；其楔式行列式可能恒为零而截面的常系数线性关系仍不存在。因此这一更强断言不成立于现有论证层面。

---

## 3. 退化缺陷与 refined Kato

写成
\[
\beta=-\frac{\alpha}{2}+u,\qquad
\gamma=-\frac{\alpha}{2}-u.
\]
则精确退化缺陷为
\[
D:=|W^+|^2-\frac32\alpha^2
 =2u^2
 =\frac12(\beta-\gamma)^2.
\]
所以 \(D=0\) 当且仅当两个较小特征值相等，即 Kähler 型谱
\[
(\alpha,-\alpha/2,-\alpha/2).
\]

原材料中“该谱型处处成立当且仅当 \(\nabla W^+=0\)”过强。对 Einstein 四流形，\(\delta W^+=0\)；重复特征值结构通常导向 \(W^+\ne0\) 区域上的局部共形 Kähler 结构，并不要求 \(W^+\) 平行。Page 和 Chen–LeBrun–Weber 型现象正说明“共形 Kähler”不能替换为“局部对称”。

在适用的紧致正 Einstein 刚性结论下，全局退化型最终迫使 \(b_+=1\)。所以 \(b_+\ge2\) 至少给出 \(D>0\) 于某非空开集，并由此排除等号。然而所给来源均不提供
\[
\operatorname{Vol}\{D>0\}\ge c>0
\quad\text{或}\quad
\int D\ge c>0
\]
这样的维数统一下界。

refined Kato
\[
|\nabla W^+|^2\ge\frac53|\nabla|W^+||^2
\]
本身测量的是 \(W^+\) 的变化而非特征值分裂 \(D\)。甚至 \(D=0\) 的共形 Kähler Einstein 度量也可有 \(\nabla W^+\ne0\)。它与 Bochner、Yamabe 不等式结合可以得到等号刚性及
\[
E_+>\frac{s^2}{24}V\qquad(b_+\ge2),
\]
但现有输入不足以推出
\[
E_+\ge(1+\varepsilon)\frac{s^2}{24}V
\]
其中 \(\varepsilon>0\) 仅依赖维数或 \(b_+\)。

尤其
\[
Y([g])=s\sqrt V
\]
在归一化 Einstein 度量体积塌缩时趋于零，故 Sobolev 控制会退化。要量化严格性，至少需要额外的非塌缩、曲率或注入半径控制。

---

## 4. 谱重述：原 CLR 公式不成立，修正版仍不足

令 \(s=12\)。原算子为
\[
L=\nabla^*\nabla+4I-2W^+,
\qquad
\dim\ker L=b_+.
\]
势的特征值为
\[
4-2\alpha,\quad4-2\beta,\quad4-2\gamma.
\]

### 两项修正

第一，不一定只有一个负势方向。可能同时有
\[
\alpha>2,\qquad\beta>2,
\]
故原始负部应为
\[
(2W^+-4I)_+,
\]
且
\[
\operatorname{tr}(2W^+-4I)_+^2
=(2\alpha-4)_+^2+(2\beta-4)_+^2.
\]

第二，更根本地，普通 CLR 计数的是严格负特征值，不能直接计数阈值零模。Kähler–Einstein \(\mathbb{CP}^2\) 上
\[
4I-2W^+=\operatorname{diag}(0,6,6)
\]
没有负势，却有一个平行 Kähler 零模。因此
\[
b_+\le \frac{C}{Y^2}\int(2\alpha-4)_+^2
\]
不可能作为一般紧流形零模计数成立。

### 正确的 coercive shift

取
\[
H=\nabla^*\nabla+\frac{s}{6}I,\qquad
Q=2W^+-\frac{s}{6}I,
\]
则
\[
L=H-Q.
\]
Yamabe 与 diamagnetic 不等式给出 coercive Sobolev 控制
\[
\langle H\phi,\phi\rangle
\ge \frac{Y}{6}\|\phi\|_{L^4}^2.
\]
因此可以原则上应用 Birman–Schwinger/CLR 于 \(H-Q_+\)，得到形如
\[
b_+
\le
\frac{C_{\mathrm{CLR}}}{Y^2}
\int
\operatorname{tr}\left(2W^+-\frac{s}{6}I\right)_+^2.
\]
在 \(s=12\) 时吸引通道是
\[
(2\alpha-2)_+,\qquad(2\beta-2)_+.
\]
这会正确看到 Kähler 阈值模：在 \(\mathbb{CP}^2\) 上
\[
Q=\operatorname{diag}(2,-4,-4),\qquad
\int\operatorname{tr}Q_+^2=4V,\qquad
Y^2=144V.
\]
若采用上述归一化，则必须有
\[
C_{\mathrm{CLR}}\ge36
\]
才能容纳 \(b_+=1\)。因此资料中的 Euclidean 常数 \(0.019\) 和“临界常数约 \(5.9\)”并不能直接用于该紧流形阈值问题。

又因为
\[
\operatorname{tr}Q_+^2\le4|W^+|^2,
\]
修正 CLR 至多推出
\[
\frac{E_+}{V}\ge\frac{36b_+}{C_{\mathrm{CLR}}}.
\]
这确实显式依赖 \(b_+\)，但仍只是 \(A=E_+/V\) 的下界。对于
\[
A=\frac{32\pi^2}{V}-3,
\]
当 \(V\to0\) 时 \(A\to\infty\)，故任何固定下界 \(A\ge f(b_+)\) 都只产生体积上界，不能排除正 Einstein 度量。

同理，Li–Yau、Berezin 和 heat-kernel 路线面临阈值零模及曲率浓度问题；有限时间热迹会涉及类似 \(\int e^{2t\alpha}\) 的量，不能由 Weyl 的 \(L^2\) 能量单独控制。

---

## 5. 真正尚未利用的耦合量

三个方向的共同缺口不是简单地“常数不够好”，而是现有拓扑/CGB 数据只控制 \(W^+\) 的 \(L^2\) 能量，却不控制：

- 调和形式密度 \(f\) 的空间浓度；
- \(T\) 的定量各向同性；
- 重复特征值缺陷 \(D\) 的积分尺度；
- 粗 Laplacian 在非 Kähler 区间的谱隙；
- 阈值零模。

最具体的未用杠杆是被丢弃的
\[
G=\sum_a\int|\nabla\omega_a|^2.
\]
若多个 \(L^2\)-正交形式在不同区域形成近 rank-one “多团块”，其转移区必然产生梯度能量。因而自然的目标不是单独估计 \(\theta\) 或 \(\kappa\)，而是证明耦合稳定性不等式，例如
\[
\frac Gb+
2\left(\int |W^+|^2\right)^{1/2}
\left[
\sqrt{\frac23}\left(\int f^2\right)^{1/2}
-\left(\int|T_0|^2\right)^{1/2}
\right]
\ge \varepsilon,
\]
或某个尺度一致、量纲正确的变体。现有 Ricci 下界与 Myers 直径上界本身不足以给出统一 Faber–Krahn/Sobolev 常数，因为体积仍可塌缩；任何成功版本都必须内含塌缩尺度或 Yamabe 常数。

等价的谱目标是对非 Kähler 正 Einstein 四流形建立定量粗 Laplacian 间隙，或更现实地建立把该间隙与 \(V\)、\(Y\) 或 Weyl 浓度耦合的估计。单纯声称存在维数统一
\[
\lambda_1(\nabla^*\nabla|_{\Lambda^+})\ge c>0
\]
目前没有依据，且在趋近 Kähler/塌缩退化序列下未必成立。

## 最终判定

- \(b_+\) 消去：正确。
- \(\kappa=1\) 时所得常数：确为 Gursky–LeBrun 常数，但只是恒密度极端模型，不是其一般证明。
- \(22.47\%\)：正确的 Bishop-ceiling 基准，且在 \(\chi=8\) 上不取到。
- \(b_+\ge2\)：保证矩阵和曲率等号被严格排除，但没有已知维数统一余量。
- 原 \(\theta_{\max}=1/3\) 与 \(A=18\) 绝对截止：错误。
- 原 CLR 零模计数及单负通道：错误；coercive-shift 修正后仍不足以形成排除。
- 最有实质价值的下一数学对象是“梯度能量—浓度—各向同性”的耦合不等式，而不是另一个只给 \(A\) 固定下界的 Weyl 能量估计。