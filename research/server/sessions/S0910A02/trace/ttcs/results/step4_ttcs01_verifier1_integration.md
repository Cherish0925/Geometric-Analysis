# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 4,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step4_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step4_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Step-4 Preceptor note for Yau Problem 26. Focus on the four-dimensional full-Weyl Chern--Gauss--Bonnet accounting and the route judgment. Verify the constants and inequalities: 8π²χ = ∫(|W|²+s²/24-|E|²/2), b(δ)=(2/3)(1-δ)²-2δ², volume ceiling, equivalence between volume lower bound and Weyl-energy deficit up to δ-dependent constants, and the claim that tight pinching plus bounded |Rm| forbids 4D collapse. Also check the target-fidelity/refutation logic: p→1/3+ negative LeBrun boundary alone cannot refute Q_4, positive branch obstruction statements are not overclaimed, and Anderson/Ye source gaps are stated at their real scope. Identify corrections or sharper formulations that would materially affect the next research step.

## Integrated Scientific Memo

# Step-4 核验结论

Step-4 的核心全 Weyl Chern–Gauss–Bonnet 计量、\(b(\delta)\)、体积上界、Weyl 亏量与总体积的比较，以及“统一全曲率有界时不能总体积塌缩”的结论均正确。路线判断也基本准确。不过有三项应实质性加强或限缩：

1. \(b(\delta)\) 只是粗下界；存在最优点态下界 \(\beta(\delta)\)，可把正性窗口从 \(\delta<1/(1+\sqrt3)\) 扩大到 \(\delta<1/2\)。
2. “collapse”必须明确指总体积 \(V_i\to0\)；该 CGB 论证本身不排除局部注入半径退化，尤其负号支路缺少直径控制。
3. 正号 SW 排除需要 metric-independent monopole class（或足以保证其对所有度量有效的条件），不能无条件以“nonzero SW”替代。

---

## 1. 全 Weyl CGB 与基本点态估计

令 Ricci 端同态特征值为
\[
\sigma+e_i,\qquad \sigma=\pm1,\qquad |e_i|\le\delta<1,
\]
并记
\[
E=\operatorname{Ric}-\frac{s}{4}g.
\]
则
\[
s=4\sigma+\sum_i e_i,\qquad
|E|^2=\sum_i(e_i-\bar e)^2
=\sum_i e_i^2-\frac14\Big(\sum_i e_i\Big)^2
\le4\delta^2,
\]
且
\[
4(1-\delta)\le |s|\le4(1+\delta).
\]

在 Step-4 使用的曲率范数约定下，
\[
\boxed{
8\pi^2\chi(M)
=\int_M\left(|W|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)d\mu
}
\]
正确，其中 \(|W|^2=|W^+|^2+|W^-|^2\)。

定义
\[
B:=\frac{s^2}{24}-\frac{|E|^2}{2}.
\]
粗估计给出
\[
B\ge \frac23(1-\delta)^2-2\delta^2=:b(\delta),
\]
其中
\[
b(\delta)=\frac23-\frac43\delta-\frac43\delta^2
=\frac23(1-2\delta-2\delta^2).
\]
故
\[
\boxed{
\int_M|W|^2\,d\mu+b(\delta)V
\le8\pi^2\chi(M).
}
\]
并且
\[
b(\delta)>0
\iff
\delta<\frac{\sqrt3-1}{2}
=\frac1{1+\sqrt3}.
\]
这些系数和符号全部正确。

上界
\[
B\le \frac{s^2}{24}\le a(\delta),
\qquad
a(\delta):=\frac23(1+\delta)^2
\]
也正确。

### 更强的最优下界

\(b(\delta)\) 并非由假设能得到的最佳统一下界。以 \(\sigma=1\) 为例，令
\[
S=\sum_i e_i,\qquad Q=\sum_i e_i^2.
\]
则
\[
B=\frac23+\frac S3+\frac{S^2}{6}-\frac Q2.
\]
逐变量看这是凹函数，故在立方体 \([-\delta,\delta]^4\) 上的最小值出现在顶点。枚举顶点得到
\[
\boxed{
B\ge\beta(\delta):=
\begin{cases}
\frac23(1-\delta)^2,
&0\le\delta\le\frac13,\\[1mm]
\frac23-\frac23\delta-\frac43\delta^2
=\frac23(1+\delta)(1-2\delta),
&\frac13\le\delta<1.
\end{cases}}
\]
负号支路由 \(e_i\mapsto-e_i\) 相同。因此
\[
\beta(\delta)>0\iff\delta<\frac12.
\]

这会实质增强 Step-4 的 Euler、Hitchin–Thorpe、体积和有界曲率结论：凡使用 \(b\) 的地方均可在 \(\delta<1/2\) 内用 \(\beta\) 替换。特别地，原文把“小 pinching 拓扑过滤器”限制在约 \(0.366\) 并非最优。

需要注意：\(\beta(\delta)=\frac23-\frac43\delta+O(\delta^2)\) 在 \(\delta\le1/3\) 仍有真实线性项。除非另加 \(s\equiv4\sigma\) 等标量中心化条件，不能把误差笼统写成 \(O(\delta^2)\)。

---

## 2. 体积上界与 Weyl-energy deficit

由 \(B\ge b(\delta)\) 得
\[
V\le\frac{8\pi^2\chi}{b(\delta)}
=\frac{12\pi^2\chi}{1-2\delta-2\delta^2}
=12\pi^2\chi+O(\delta)\chi.
\]
在 \(\delta=0\) 时，
\[
V\le12\pi^2\chi,
\]
与 \(\operatorname{Ric}=\pm g\) 的 CGB 结论一致。

更强形式为
\[
V\le \frac{8\pi^2\chi}{\beta(\delta)}
\qquad(\delta<1/2).
\]

令
\[
D_W:=8\pi^2\chi-\int_M|W|^2\,d\mu
=\int_M B\,d\mu.
\]
则在粗窗口内
\[
b(\delta)V\le D_W\le a(\delta)V,
\]
而在最优窗口内
\[
\boxed{
\beta(\delta)V\le D_W\le a(\delta)V
\qquad(\delta<1/2).
}
\]
因此：

\[
V\ge v
\Longrightarrow
\int|W|^2\le8\pi^2\chi-\beta(\delta)v,
\]
以及
\[
\int|W|^2\le8\pi^2\chi-\eta
\Longrightarrow
V\ge\frac{\eta}{a(\delta)}.
\]

所以“总体积存在正下界”和“Weyl 能量距拓扑上限 \(8\pi^2\chi\) 有正亏量”确实等价到只依赖 \(\delta\) 的常数。对满足统一 \(\delta_i\le\delta_0<1/2\) 的序列，
\[
V_i\to0
\iff
8\pi^2\chi(M_i)-\int|W_{g_i}|^2\to0.
\]

但应把 Step-4 中的“collapse is exactly …”改成：

> **总体积塌缩** \(V_i\to0\) 恰对应 CGB Weyl 预算饱和。

这不等价于局部 injectivity-radius collapse。正号支路有 Myers 直径上界，故总体积正下界可与 Ricci 下界结合导出局部非塌缩；负号支路没有自动直径控制，总体积计量本身不控制远端细部或局部薄区。

---

## 3. 紧夹逼加统一全曲率上界

若采用与 CGB 分解一致的范数并且
\[
|\operatorname{Rm}|\le K,
\]
则 Weyl 是正交分量，所以
\[
|W|\le|\operatorname{Rm}|\le K.
\]
于是
\[
8\pi^2\chi
=\int(|W|^2+B)
\le (K^2+a(\delta))V.
\]
另一方面，\(\beta(\delta)>0\) 强制 \(\chi>0\)，故闭连通四维流形满足整数 \(\chi\ge1\)。因此
\[
\boxed{
V\ge \frac{8\pi^2}{K^2+a(\delta)}
\qquad(\delta<1/2).
}
\]
在正号、可定向情形，Bochner 给出 \(b_1=0\)，Poincaré 对偶给出 \(b_3=0\)，故
\[
\chi=2+b_2\ge2,
\]
分子可增强为 \(16\pi^2\)。

所以严格正确的结论是：

> 四维紧 Ricci 夹逼与统一 \(\|Rm\|_\infty\) 上界排除总体积趋零；任何总体积塌缩序列都必须发生全曲率爆破。

事实上
\[
\|W\|_\infty^2
\ge \frac{8\pi^2\chi}{V}-a(\delta)
\ge \frac{8\pi^2}{V}-a(\delta),
\]
故 \(V_i\to0\) 直接推出
\[
\|W_{g_i}\|_\infty\to\infty.
\]

这不是“所有四维 collapse 被排除”。它没有单独排除固定总体积下的局部注入半径退化。

### 正号支路的进一步结果

若
\[
\delta_i\to0,\qquad
\|\operatorname{Ric}_{g_i}-g_i\|_{\mathrm{op}}\le\delta_i,
\qquad
\|\operatorname{Rm}_{g_i}\|_\infty\le K,
\]
则 Myers 自动给出统一直径上界；上述 CGB 估计给出统一总体积下界。结合 Ricci 下界、Bishop–Gromov、曲率上界与标准紧致性，可取固定微分拓扑后的极限，并在谐和坐标中把
\[
\operatorname{Ric}_{g_i}-g_i\to0
\]
传递为
\[
\operatorname{Ric}_{g_\infty}=g_\infty.
\]
椭圆正则性使极限光滑。因此：

> 任一四维正号 \(\delta_i\to0\) 的 Einstein-free 序列必有  
> \(\|\operatorname{Rm}_{g_i}\|_\infty\to\infty\)。

负号支路若另有统一直径上界也成立；否则还可能出现直径发散。

---

## 4. 曲率范数需固定

Step-4 的“full curvature energy approaches \(8\pi^2\chi\)”应声明采用何种 \(Rm\) 范数。若 \(\mathcal R:\Lambda^2\to\Lambda^2\) 采用 Hilbert–Schmidt 范数，则
\[
|\mathcal R|^2
=|W|^2+\frac{|E|^2}{2}+\frac{s^2}{24},
\]
因而
\[
\int|\mathcal R|^2
=8\pi^2\chi+\int|E|^2.
\]
又
\[
\int|E|^2
\le4\delta^2V
\le\frac{32\pi^2\delta^2}{\beta(\delta)}\chi,
\]
所以
\[
\int|\mathcal R|^2
=8\pi^2\chi+O(\delta^2\chi).
\]
若 \(Rm\) 指完整 \((0,4)\)-张量范数，通常会有整体因子差异。后续计算必须固定这一约定，避免重现 Step-2 的因子错误。

---

## 5. Hitchin–Thorpe 与正号 obstruction 的精确范围

由
\[
4\pi^2(2\chi\pm3\tau)
=\int\left(2|W^\pm|^2+B\right)d\mu
\]
和 \(\beta(\delta)>0\)，可加强为
\[
2\chi\pm3\tau>0,\qquad
2\chi>3|\tau|
\qquad(\delta<1/2).
\]
因此以 Hitchin–Thorpe 数值违反来排除 Einstein 度量的拓扑，也不能承载任一符号的任意紧 Ricci 夹逼。

对
\[
M=\#_k\mathbb{CP}^2,\qquad
\chi=k+2,\quad\tau=k,
\]
有
\[
2\chi-3\tau=4-k.
\]
故该过滤器直接排除 \(k=4\) 的等号情形以及 \(k\ge5\) 的违反情形；不应笼统暗示它处理 \(k=2,3\)。

LeBrun/SW 正号句子应改为带假设的表述：

> 若流形具有对所有度量有效的非零 monopole class（例如已验证的相应 metric-independent 情形），则 \(\delta_+<1\) 强制 \(s>0\)，与 monopole Weitzenböck obstruction 冲突。

在 \(b_2^+=1\) 时普通 SW 不变量有 chamber 依赖；“nonzero SW”本身不足以无条件推出所有度量都无正标量曲率。Step-4 前文的“relevant polarization/monopole-class input”应在正号结论处重复保留。

---

## 6. 目标忠实性与反驳逻辑

Step-4 关于两条符号支路的判断正确。

证明任一支路，例如
\[
\|\operatorname{Ric}-g\|_{\mathrm{op}}\le\varepsilon
\Longrightarrow M\text{ 承载 Einstein 度量},
\]
即给出原命题所需区间
\[
[1-\varepsilon,1+\varepsilon].
\]
负号支路同理。因此任一支路成立已足以证明 \(Q_4\)。

反过来，严格否定 \(Q_4\) 必须排除所有候选区间。正 Ricci 的紧夹逼反例经缩放只能覆盖带正上端的区间；它不能处理完全非正区间。负号反例也不能代替正号反例。因此同一维数中需要两条符号的 Einstein-free 紧夹逼序列。

所以即使成功构造
\[
p=k/A\to1/3^+,\qquad \delta_-\to0
\]
的 LeBrun 负号序列，也只能否定 \(P_4^-\)，不能单独否定 \(Q_4\)。这部分判断无误。

现有正号 statement 没有被过度声称：SW 型流形在适用的 monopole 假设下根本不承载 \(\delta_+<1\) 输入；Hitchin–Thorpe 违反拓扑又被上述 sign-blind 过滤器排除。它们都没有产生正号反例。

---

## 7. Anderson、Cheeger–Naber、Ozuch、Min-Oo、Ye 的真实作用域

现有材料支持 Step-4 的谨慎判断：

- Ozuch 所引 Anderson–BKN 紧化定理假设输入是**精确 Einstein** 四维流形，并要求非塌缩、直径和 \(L^2\) 曲率控制；结论为 Einstein orbifold 极限及 Ricci-flat ALE bubbles。
- Ozuch Theorem 0.2 同样从精确 Einstein 输入出发，只描述 GH 接近 orbifold 时的 gluing–perturbation 结构，不是任意 almost-Ricci-pinched 度量的 Einstein 存在定理。
- Cheeger–Naber 在非塌缩、双侧 Ricci 有界条件下给出 codimension-4 正则性、四维 \(L^2\) 曲率估计及有限微分同胚型；这些都是正则性/有限性结论，不产生 Einstein 度量。
- Min-Oo 原文要求 \(n>3\)、负平均标量曲率以及
  \[
  d^2\max|K|<\Lambda^2,
  \]
  pinching 常数依赖 \((n,\Lambda)\)。它不是仅依赖维数的 Ricci pinching 定理。
- 当前材料没有 Ye 1993 原始定理正文。仅由二手引用最多可把它当作现有 Einstein 度量附近、带稳定性假设的局部结果，不能用于全局 Yau-26。
- Anderson 1989 Corollary B(4) 的准确正文仍未出现；不应赋予超出现有二手材料的作用。

此外，Ozuch Example 1 是当前正号方向最接近目标的实际对象，但它只给出
\[
\operatorname{Ric}(g_i)\ge3g_i,\qquad
\|\operatorname{Ric}(g_i)-3g_i\|_{L^p}\to0,
\]
以及不存在 GH 收敛到该 orbifold 的 Einstein 序列。这既不是点态双侧 operator pinching，也不等于底层光滑流形完全没有任何 Einstein 度量。因此它目前不能作为 \(P_4^+\) 反例；其关键未决对象是：

1. 这些 neck/gluing 度量是否有全局点态 Ricci 上界使 pinching ratio \(\to1\)；
2. 底层光滑流形是否完全 Einstein-free，而非仅无特定 GH 退化的 Einstein 序列。

---

## 对 Step-4 文本的建议替换

最重要的修订版结论可写为：

\[
\beta(\delta)V
\le
8\pi^2\chi-\int|W|^2
\le
a(\delta)V,
\qquad \delta<\frac12,
\]
其中
\[
\beta(\delta)=
\begin{cases}
\frac23(1-\delta)^2,&\delta\le1/3,\\
\frac23(1+\delta)(1-2\delta),&1/3\le\delta<1/2,
\end{cases}
\quad
a(\delta)=\frac23(1+\delta)^2.
\]

并将路线缺口表述为：

> 正号支路中 Myers 已给直径控制；若全曲率也有统一上界，则 CGB 强制非塌缩并由紧致性产生 Einstein 极限。因此任何潜在正号反例必须进入 Weyl 曲率集中、\(\|Rm\|_\infty\to\infty\) 的 regime。Cheeger–Naber 处理的是给定局部非塌缩后的正则性与有限性，Ozuch 处理的是精确 Einstein 退化；二者均未解决从点态 Ricci 紧夹逼到同一光滑流形上 Einstein 存在的缺失步骤。