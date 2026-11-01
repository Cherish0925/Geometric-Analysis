# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/five_research_problems.tex",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md"
  ]
}
```

## Task

Read the final section §24 (and §24.0 L1/L2, §23.6) of Sessions/S1003A02/workspace/notes/theorem_package_v1.md as a research geometer checking every statement against (a) the earlier package sections it cites (§§1, 3.3-3.7, 13-17, 20, 21.10-21.11, 22) and (b) the original problem statements in five_research_problems.tex §§1-3 (Problems 1-3: Einstein existence on X#k CPbar^2 for 1<=k<A/3; exact P_*; a smooth non-Bach-flat global P-minimizer). For each statement in §24 decide whether (i) it is correctly tagged [I]/[P]/[C]/[O], (ii) its quantifiers match the cited source (which X, which k, which metrics, which hypotheses), (iii) the derivation is correct. Specific items to check with care: the L1 equivalence Einstein <=> alpha=0 attained <=> P_*=0 attained on X#kCPbar^2 and what Seiberg-Witten/Yamabe input it needs (b+ conditions); the L2 bound D(g) >= p/(p+3T_+/4) from C_+ = T_+ + p and the derived band bound alpha >= 4(3k-A)/(3k+5A) for A/3<=k<=A; the regime summary in 24.2(4); the Problem-3 discussion: whether k>=A/3 blow-ups really satisfy both hypotheses of Prop. nonbach unconditionally, whether the real-hyperbolic blow-up scalar-flat exclusion argument (no PSC on connected sums with aspherical 4-manifolds + Cheeger-Gromoll) is sound, and whether Theorem H (conditional non-attainment) is quoted correctly; the k=1 conditional dichotomy 'negative Problem 1 => positive Problem 3' from Theorem 54.A including whether A>=9 for ball quotients is right and what configurations remain; the 'three ends' paragraph (does p->0 force approach to the Einstein end of p=q^2(1-delta)^2+L, is q bounded below, and are the aligned/cscK ends correctly described as obstacles to coercive estimates rather than escape routes); the statement that 1/3 is simultaneously the zero of LeBrun's P bound and the sign change of the fixed-Kahler Weyl deficit, and its explanation by KE saturation; and the claim that every known attained alpha-minimizer is Bach-flat. Report concrete corrections with exact replacement wording, any statement that is false or overstated, and any important inherited or proved result from the package that §24 omits but that belongs in a complete statement of Problems 1-3. Do not invent literature; if a claim needs an outside source (e.g. no-PSC for connected sums with aspherical manifolds, LeBrun's Yamabe computation for b+=1), name the exact knowledge_request needed.

## Output

# 科学核查备忘录

## 一、总评

§24 的主线基本正确：它准确区分了 \(P_*(M)\) 与 \(\alpha(M)\)，正确识别了 \(k<A/3\) 中 Einstein 存在、零间隙、退化与光滑实现之间的关系，也正确汇总了严格次 \(8\pi^2k\) 构造、固定复结构的 Kähler 最优值、球商 \(k=1\) 的条件性实现结果以及中间带的 Weyl 容量问题。

需要实质修改的地方主要有：

1. §24.0 的 L1、L2 都混合了继承定理与本会话代数推导，不宜单独标成 `[P]`。
2. “不存在纯拓扑障碍”远强于已有结果；现有结果只排除了 \(P\ge8\pi^2k\) 这种逐异常类费用。
3. Einstein 轨形吸收只能推出 \(\alpha=0\)，不能推出原光滑流形没有别的 Einstein 度量。
4. 第二阶 Burns 公式缺少“局部 \(P\)-临界、点处 Einstein、\(\zeta\) 为特征向量、对零次修正优化”等前提。
5. 固定复结构上的 Kähler 结果不能写成“真实极小值只能由非 Kähler 几何实现”，因为极小值可能根本不实现，且别的复结构未被排除。
6. 实双曲吹起的标量平坦排除尚未由所给材料闭合；需要无正标量曲率定理、Bourguignon 变形定理和 Cheeger–Gromoll 结构定理的连续证明链。
7. Theorem 54.A 的 \(k=1\) 推论漏掉了 exotic homotopy-sphere 泡；没有这一附加输入时，极小元只在与 \(M\) 同胚的光滑流形 \(V\) 上得到。
8. “大 Yamabe 能量降低 \(\alpha\)”方向相反：在 \(\mathscr D<1\) 的区域，增加 \(\upsilon\) 会提高比值并趋向 \(1\)。
9. “所有下界都停在 \(1/3\)”与 N1 在 \(1/3\) 以下给出的正分离矛盾。正确说法只适用于经典 LeBrun 下界与固定复结构 Kähler 比较。
10. Wahl 点“只在 \(\lambda^4\) 阶相互作用”尚未证明；已证明的是对数项消失，\(\lambda^4\) 极化型仍未确定。
11. 最后“整个 \(0<k<A/3\) 都没有正下界”忽略了 N1 已覆盖的窄窗口，应改成“尚未被 N1 或其他特殊输入覆盖的低 \(k/A\) 区域”。

---

## 二、§24.0：L1 与 L2

### 1. L1：Einstein、\(\alpha=0\) 的实现、\(P_*=0\) 的实现

数学推导本身正确，但标签应拆成 `[I]+[P]`：

- `[I]`：LeBrun 的 Yamabe 结论
  \[
  \mathcal Y\!\left(X\#k\overline{\mathbb{CP}}^{\,2}\right)
  =-4\pi\sqrt{2A}<0.
  \]
- `[P]`：由该结论与泛函定义推出三者等价。

具体推导是：

- \(P(g)=0\iff \operatorname{Ric}^\circ_g=0\iff g\) 为 Einstein。
- \(\mathscr D(g)=0\iff g\) 为 Einstein 且 Einstein 常数非零。
- 若 \(\mathcal Y(M)<0\)，则不存在正标量或零标量 Einstein 度量，所以任何 Einstein 度量都满足 \(\lambda<0\)。
- 因而
  \[
  M\text{ 有 Einstein 度量}
  \iff P_*(M)=0\text{ 且实现}
  \iff\alpha(M)=0\text{ 且实现}.
  \]

这里确实需要排除 Ricci-flat 度量，因为 Ricci-flat 度量有 \(P=0\)，但按本项目定义 \(\mathscr D=4\)，而不是 \(0\)。

#### \(b^+=1\) 的问题

§§3.6–3.7 的“每个度量都有未扰动解”论证直接覆盖 \(b^+\ge2\)；\(b^+=1\) 需要腔结构或一个独立的 Yamabe 定理。§24 不能仅从这些章节推出所有极小一般型曲面的 L1。

精确替换文本可写为：

> **L1 `[I]+[P]`.** 假设采用 LeBrun 对该 \(X\) 及其吹起的 Yamabe 定理
> \[
> \mathcal Y(M)=-4\pi\sqrt{2A}<0.
> \]
> 则 \(M\) 不承载标量平坦或 Ricci-flat度量，所有 Einstein 度量均有负 Einstein 常数，并且
> \[
> M\text{ 承载 Einstein 度量}
> \iff \alpha(M)=0\text{ 且下确界实现}
> \iff P_*(M)=0\text{ 且下确界实现}.
> \]
> 对 \(b^+=1\) 的曲面，需引用包含腔问题的 Yamabe 定理，而不能只引用 \(b^+\ge2\) 的全度量单极子供给。

### 2. L2：\(\mathscr D\) 与 \(P\) 的比较

推导正确。令 \(p=P/(8\pi^2)\)。由
\[
C_+=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2=T_++p
\]
得到
\[
S=\int s^2\le96\pi^2(T_++p),
\]
因此
\[
R=P+\frac14S\le8\pi^2(4p+3T_+).
\]
又
\[
\mathscr D(g)=\frac{4P+L_s}{R}\ge\frac{4P}{R},
\]
故
\[
\boxed{\mathscr D(g)\ge
\frac{p(g)}{p(g)+\frac34T_+}}.
\]
右端关于 \(p\) 单调增加，所以
\[
\boxed{\alpha(M)\ge
\frac{\mathfrak p_*(M)}
{\mathfrak p_*(M)+\frac34T_+}}.
\]

将继承的 LeBrun 下界
\[
\mathfrak p_*\ge k-\frac A3
\]
与 \(T_+=A-k\) 代入，得到
\[
\alpha\ge
\frac{k-A/3}{k-A/3+\frac34(A-k)}
=\boxed{\frac{4(3k-A)}{3k+5A}}.
\]

这在 \(A/3\le k<A\) 直接成立。\(k=A\) 时 \(T_+=0\)，而 \(\mathfrak p_*\ge2A/3>0\)，同一计算给出 \(\mathscr D\ge1\)，再结合通用上界得到 \(\alpha=1\)。

这里也宜标成 `[I]+[P]`：LeBrun 下界是 `[I]`，代数推导是 `[P]`。

### 3. 一个 §24 未写出的重要推论

当 \(0<k<A\) 时，两侧比较给出
\[
\boxed{P_*(M)>0\iff\alpha(M)>0},
\qquad
\boxed{P_*(M)=0\iff\alpha(M)=0}.
\]

一向由 L2 得出；另一向使用 §22.1 的上比较
\[
\alpha\le\frac{4\mathfrak p}{A+\mathfrak p}
\]
并令 \(\mathfrak p\to\mathfrak p_*\)。这使 Problems 1–2 在“零值还是正值”这一层面精确对应；二者的极小序列仍可能不同。

---

## 三、§24.1：Problem 1

### 1. 公开状态与量词

- \(k\ge A/3\) 的 Einstein 非存在：`[I]`，正确。
- N1 给出的 \((1/3-\varepsilon)A<k<A/3\) 窗口：`[I]`，但只对具有所述逐共形类实际供给的 \(X\) 成立。
- 超曲面 \(X_d\subset\mathbb{CP}^3\) 的真实例子：`[I]`，量词正确，且这些例子有 \(b^+>1\)。
- 其余低 \(k/A\) 区域：`[O]`，但应写成“所给材料中没有覆盖所有 \(X\) 的一般定理”；个别 \(X\) 可能有额外障碍。

### 2. §24.1(1)：重述为零值实现问题

正确，标签 `[P]`。在 \(k<A/3\) 时，Theorem 69.KE 给出
\[
\alpha(M)<\frac{4k}{A+k}<1.
\]
不必再分“光滑 KE 典范模型”和 ADE 情形，因为 59.KE/69.KE 已将典范模型与 Kronheimer 局部化写入定理。

### 3. §24.1(2)：“不存在纯拓扑障碍”不成立

严格次 \(8\pi^2k\) 构造只排除了如下类型的论证：
\[
P(g)\ge8\pi^2 k
\]
或“每个异常类固定支付 \(8\pi^2\)”的逐类费用。它并不排除由其他拓扑量、规范场、熵或交叉形式导出的 Einstein 非存在定理。

精确替换文本：

> 59.KE 证明，任何以
> \[
> P(g)\ge8\pi^2k
> \]
> 为核心的逐异常类费用不等式都不成立；CH 背景上的认证单元还给出显式值
> \[
> P_{\rm cell}/(8\pi^2)<0.995663.
> \]
> 因而 Einstein 非存在不能由固定的 \(8\pi^2\)-每类费用推出。其他拓扑或场论障碍并未被排除。

还应区分：

- “每个极小一般型 \(X\)”的严格性来自解析的 59.KE；
- 数值区间 \(0.9956627\ldots\) 只来自 CH 单元。

### 4. §24.1(3)：Einstein 端的 twist 描述

方向正确，但原句将异常类 \(E_i\) 与 almost-complex 第一 Chern 类混在一起。

更准确的版本是：

> 对任意可由正交 almost-complex 结构 \(J\) 实现的最佳符号类 \(a\)，Einstein 条件 \(B_g=0\) 使 Step 64 的恒等式化为
> \[
> \mathsf H^-(t_J^-)=2\pi h_a^-.
> \]
> 因而
> \[
> \|\mathsf H^-(t_J^-)\|_2=2\pi|a^-|,
> \qquad |a^-|^2\ge k+\Pi.
> \]
> 单独地，每个异常类满足
> \[
> |E_i^-|^2=1+|E_i^+|^2\ge1,
> \]
> 但 \(E_i\) 本身通常不是 \(c_1(J)\)，所以不能把该式直接写成“每个 \(E_i\) 都产生一个 \(J\)-twist 方程”。

Einstein 端
\[
\delta=1,\qquad L=p=0
\]
的描述正确。

### 5. §24.1(4)：轨形吸收

Corollary 52.8 的不等式
\[
\alpha(X\#2m\overline{\mathbb{CP}}^2)
\le
\alpha_{\rm orb}(X\#m(S^4/\mathbb Z_2))
\]
是 `[P]`。若右侧轨形具有非零 Einstein 尺度，则得到光滑解消的 \(\alpha=0\)。

但原句“会给出 \(\alpha=0\) 而 \(M\) 没有 Einstein 度量”并未得到证明。轨形退化只排除了由该轨形收敛而来的 Einstein 解消；\(M\) 仍可能承载与该退化无关的 Einstein 度量。

精确替换文本：

> 若相应吸收轨形承载非零尺度 Einstein 度量，则 Corollary 52.8 给出解消流形的 \(\alpha=0\)。除非另有论证排除 \(M\) 上的所有光滑 Einstein 度量，否则不能由该轨形退化推出此零值不实现。Ozuch 型结果排除的是收敛到指定轨形的 Einstein 解消族，而不是所有可能的 Einstein 度量。

“这些轨形必为非 Kähler”也只应在 52.9 所列吸收模式及其 orbifold LeBrun 输入下陈述，不能无条件扩展到所有 Einstein 轨形。

### 6. §24.1(5)：实双曲类比

实双曲 \(Y\#k\overline{\mathbb{CP}}^2\) 对所有 \(k\ge1\) 不承载 Einstein 度量，标签 `[P]`，正确。

后一句应只指复双曲球商：
\[
\operatorname{Vol}(g)\ge\frac{64}{81}\operatorname{Vol}(X)
\]
是 §15 对球商吹起及特定 Einstein 归一化的 BCG–Bishop 估计，不是一般极小一般型曲面的结论。

---

## 四、§24.2：Problem 2

### 1. 经典区间

\[
8\pi^2\max\{0,k-A/3\}\le P_*(M)\le8\pi^2k
\]
标成 `[I]` 正确。对 \(b^+=1\) 的完整量词仍依赖 LeBrun 原定理的腔处理。

### 2. 严格次 \(8\pi^2k\) 上界

59.KE 的标签 `[P]` 与量词正确：对每个固定极小一般型 \(X\) 和每个固定 \(k\ge1\)，存在严格小于 \(8\pi^2k\) 的度量。

但 Burns 二阶公式需补全前提。精确版本为：

> 若 \(g\) 在插入支撑的邻域内是 \(P\)-临界，点 \(p\) 处 \(\operatorname{Ric}^\circ_p=0\)，\(\zeta\) 是 \(\mathbf R_p^+\) 的特征向量，并对允许的零次修正 \(K\) 作优化，则
> \[
> \frac{P(\widetilde g_\varepsilon)-P(g)}{8\pi^2}
> =
> 1-\varepsilon\mu_1
> +\frac{\Phi_{\rm opt}}2\varepsilon^2\log(1/\varepsilon)
> +O(\varepsilon^2),
> \]
> \[
> \Phi_{\rm opt}
> =
> -\frac12\mu_1(\mu_1-\mu_2-\mu_3)
> -\frac12(\mu_2-\mu_3)^2.
> \]
> 对一般背景或未优化的修正，二阶系数是 \(\Phi(\operatorname{Rm}_p,\zeta,K)\)，不能只写成三个特征值的函数。

### 3. 固定复结构 Kähler 最优值

Theorem \(K_\infty\) 的标签 `[P]` 正确：
\[
\inf_{\text{Kähler for fixed }J}P=8\pi^2k,
\]
且 \(k\ge1\) 时不实现。

“真实 \(P_*\) 只能由非 Kähler 几何实现”需改为：

> 由于 \(P_*<8\pi^2k\)，任何进入严格次 \(8\pi^2k\) 区域的序列都必须离开给定吹起复结构 \(J\) 的 Kähler 度量类。若 \(P_*\) 由光滑度量实现，则该度量不可能是关于这个固定 \(J\) 的 Kähler 度量。其他复结构并未由 Theorem \(K_\infty\) 排除。

### 4. 平衡族

Theorem 69.B 的标签 `[P]`、覆盖量词和
\[
\frac{\alpha}{h}\le\frac{C_c}{1+C_ch/4},
\qquad C_c=3.99614465135\ldots
\]
均正确。它是含 \(7n(S^1\times S^3)\) 的平衡族结论，不是纯吹起 \(P_*(X\#k\overline{\mathbb{CP}}^2)\) 的精确值。

### 5. §24.2(4) 的分区总结

在采用 LeBrun 的全体共形类负 Yamabe 输入后，分区公式正确：

\[
h\ge1\quad\Longrightarrow\quad\alpha=1;
\]
\[
\frac13\le h<1
\quad\Longrightarrow\quad
\frac{4(3h-1)}{3h+5}\le\alpha\le1;
\]
\[
0<h<\frac13
\quad\Longrightarrow\quad
0\le\alpha<\frac{4h}{1+h}.
\]

并且对 \(k<A\)，
\[
\alpha<1
\iff
\inf_g\int|W_g^+|^2<2\pi^2(A-k).
\]

这里最后的等价还需要“每个共形类的 Yamabe 常数非零”；\(\mathcal Y(M)<0\) 足以保证这一点，因为所有类的 Yamabe 常数均不超过全局 Yamabe 不变量。

### 6. Weyl 容量

\[
\alpha<1
\iff
\kappa>\frac{3k-A}{4}
\]
以及归一化形式
\[
\Theta>\frac{3h-1}{2}
\]
正确。

但 \(\Theta_*(h)\) 不能在未指定 \(X\) 或流形族时只依赖 \(h\)。应先定义
\[
\Theta_*(M)
=
\sup_{\widehat g}
\frac{2\kappa(\widehat g)}A,
\]
或明确是在某个球商塔上取统一容量函数。

另外，中间带的 \(\alpha<1\) 与低 \(h\) 的 \(\alpha>0\) 不是单个标量容量值完全等价的两个问题：

- 前者由 \(\sup\kappa\) 与阈值比较决定；
- 后者需要 \((\kappa,\upsilon)\) 的联合可实现性，或等价地需要远离 Einstein 比率端的定量分离。

因此“两个问题就是同一个未知量”应改成“它们受同一 Weyl 容量方向控制，但低 \(h\) 的正间隙还需要 Yamabe 超额与 \(\kappa\) 的联合信息”。

### 7. 实双曲类比

在条件
\[
\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}
\]
下，
\[
\inf P=8\pi^2k
\]
且 \(P\) 不实现；对 \(k\le2\chi(Y)\)，
\[
\alpha=\frac{4k}{k+6\chi(Y)}.
\]
这些引用正确。

对 \(\alpha\) 的不实现只在 \(k<2\chi(Y)\) 得到；在 \(k=2\chi(Y)\) 时 \(\alpha=1\)，其实现等价于适当的半共形平坦常标量度量，材料没有排除这种可能。

---

## 五、§24.3：Problem 3

### 1. Proposition nonbach

推导正确。标签可以记作 `[I]`，因为它已在项目补充材料中完整证明；若按本会话新结果分类，也可拆成标准变分公式加 `[P]` 推论。

原 Problem 3 是存在性问题：找到一个闭四流形和一个非 Bach 平坦的光滑全局 \(P\)-极小元即可，并不要求对所有一般型吹起证明实现。

### 2. \(k\ge A/3\) 的吹起

在采用 LeBrun 的 Yamabe 定理后：

- Einstein 度量由 LeBrun 排除；
- \(\mathcal Y(M)<0\) 排除标量平坦度量。

所以对这些 \(M\)，Problem 3 确实化为“\(P_*(M)\) 是否由光滑度量实现”。

原文关于 Anderson ledger 的句子必须收窄。§15 的
\[
\sum_b\bigl[4(e_b-1)+4b_1+b_2\bigr]<k
\]
是在球商宿主、非 fake plane、平滑锥点、下半连续性以及相应泡正则输入下得到的，不适用于任意极小一般型 \(X\)。

精确替换文本：

> 对非 fake-plane 球商 \(X\)，在 Theorem 54.A 的平滑点配置及其分析前提下，光滑泡所携带的总异常秩严格小于 \(k\)，所以并非所有异常类都能逃入光滑泡。该结论尚未对任意极小一般型宿主证明。

“Burns concentration 不是最优”也应具体说成“标准 KE bulk 加独立 Burns 泡的总费用 \(8\pi^2k\) 不是极小值”。

### 3. 实双曲吹起的标量平坦问题

Einstein 非存在是无条件 `[P]`。标量平坦排除在所给材料中尚未闭合。

所需逻辑链应为：

1. \(Y\#k\overline{\mathbb{CP}}^2\) 不承载正标量曲率度量；
2. Bourguignon 定理：闭流形上的标量平坦度量若不是 Ricci-flat，可变形为正标量曲率度量；
3. Ricci-flat 度量有 \(\operatorname{Ric}\ge0\)，由 Cheeger–Gromoll，基本群虚阿贝尔；
4. 但
   \[
   \pi_1(Y\#k\overline{\mathbb{CP}}^2)=\pi_1(Y)
   \]
   是实双曲格子，不虚阿贝尔。

因此，只要第 1 步有适用于所有定向实双曲四流形、包括非 spin 情形的来源，标量平坦即可排除。原句只写“无 PSC + Cheeger–Gromoll”，漏掉了 Bourguignon。

在 Theorem H 的 Yamabe 恒等式前提下则更简单：
\[
\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}<0
\]
直接排除标量平坦，同时 \(P_*=8\pi^2k\) 不实现，所以这些流形在该前提下不能给出 Problem 3 的例子。这一引用正确。

### 4. \(k=1\) 球商的条件性二分

\(A\ge9\) 正确。对球商，
\[
A=c_1^2=3c_2,\qquad
\chi(\mathcal O_X)=\frac{c_2}{3}\in\mathbb Z_{>0},
\]
所以 \(c_2\ge3\)、\(A\ge9\)，从而 \(1<A/3\)。

但 Theorem 54.A 的原文没有直接给出 \(M\) 上的极小元。准确结果是：

- 在无非平凡局部群、无塌缩并满足
  \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec},
  \mathrm H_{\rm eq},\mathrm H_{\rm rem}\)
  时，得到一个在 \(V\) 上实现 \(p_*(V)\) 的光滑常负标量度量；
- \(V\) 与 \(M\) 同胚；
- 泡的紧化是 homotopy 4-sphere；
- 只有再假设这些紧化都微分同胚于 \(S^4\)，才能得到 \(V\cong M\)、无泡以及 \(M\) 上的全局极小元。

因此精确替换文本应为：

> 在 Theorem 54.A 的全部分析前提下，并再排除 exotic homotopy-sphere 泡时，\(P_*(M)\) 由一个常负标量的光滑度量实现；该度量或者 Einstein，或者是非 Bach 平坦的全局 \(P\)-极小元。于是，在这些前提下，对 \(M\) 的 Problem 1 给出否定答案便产生 Problem 3 的一个例子。

原文列出的剩余配置还漏了 exotic homotopy-sphere 泡。应列为：

1. 塌缩；
2. 非平凡局部群与轨形吸收；
3. exotic homotopy-sphere 泡。

### 5. \(\alpha\) 的实现段

以下内容正确：

- \(\alpha=0\) 实现当且仅当存在非零 Einstein 常数的 Einstein 度量；
- 在 \(2\chi=3|\tau|\) 时，\(\alpha=1\) 的实现等价于半共形平坦且标量为非零常数；
- \(X\#A\overline{\mathbb{CP}}^2\) 上实现 \(\alpha=1\) 等价于相应取向的 ASD 常负标量度量；
- 实双曲吹起在 Theorem H 前提下、\(k<2\chi(Y)\) 时不实现 \(\alpha\)。

“所有已知实现的 \(\alpha\)-极小元都是 Bach-flat”是文献穷尽式表述，所给材料无法证明“所有已知”。更稳固的替换是：

> 本项目明确列出的已实现 \(\alpha\)-极小元只有两类：非零 Einstein 度量，以及半共形平坦的常非零标量度量；这两类都 Bach-flat。所给材料中没有一个 \(0<\alpha<1\) 的光滑实现例子，也没有非 Bach 平坦的 \(\mathscr D\)-全局极小元。

---

## 六、§24.4：共同机制中的实质修正

### 1. \(1/3\) 临界值

以下两式都正确：
\[
\mathfrak p\ge k-\frac A3,
\]
以及固定吹起复结构上的
\[
d\le4\pi^2\left(\frac A3-k\right).
\]

第二式来自
\[
I_+\ge\frac{4\pi^2A}{3},
\qquad
d=4\pi^2(A-k)-2I_+.
\]

负 Kähler–Einstein 度量在极小模型 \(k=0\) 上使
\[
I_+=\frac{4\pi^2A}{3},
\]
而小面积 Kähler 吹起序列逼近相应 Kähler 前沿。因此 \(1/3\) 同时是：

- 经典 LeBrun \(P\)-下界变为零的位置；
- 固定复结构 Kähler Weyl deficit 改变符号的位置。

但“所有已知下界都停在 \(1/3\)”不正确，因为 N1 已在 \(1/3\) 以下的窗口给出正分离。应改成：

> 经典 LeBrun 曲率估计与固定复结构 Kähler 比较都在 \(h=1/3\) 失去正性；N1 的实际场微分输入已经把 Einstein 排除和正间隙推进到该值以下的一段窗口。

### 2. Yamabe 超额的方向写反了

令
\[
p=k-\frac43\kappa+\frac13\upsilon.
\]
固定 \(\kappa\) 时，
\[
F_\kappa(\upsilon)
=
\frac{4p}{A+p+\upsilon}
=
\frac{4(k-\frac43\kappa+\frac13\upsilon)}
{A+k-\frac43\kappa+\frac43\upsilon}.
\]
直接求导得
\[
F_\kappa'(\upsilon)
=
\frac{4(A-3k+4\kappa)}
{3\left(A+k-\frac43\kappa+\frac43\upsilon\right)^2}.
\]
而
\[
F_\kappa(\upsilon)<1
\iff
A-3k+4\kappa>0.
\]
所以在所有真正产生 \(\mathscr D<1\) 的状态上，
\[
\boxed{F_\kappa'(\upsilon)>0}.
\]
增加 Yamabe 超额会提高 \(\mathscr D\)，并在 \(\upsilon\to\infty\) 时趋向 \(1\)，不是降低它。

精确替换文本：

> 在固定 Weyl 容量 \(\kappa\) 时，Yamabe 超额 \(\upsilon\) 同时提高 \(p\) 与归一化比值；在 \(\mathscr D<1\) 的区域该比值关于 \(\upsilon\) 严格增加并趋向 \(1\)。\(P\)-极小序列与 \(\alpha\)-极小序列仍可能选择不同共形类，因为二者对 \((\kappa,\upsilon)\) 的权重不同，而不是因为大 \(\upsilon\) 本身提供节省。

### 3. Wahl 点相互作用

原句“Wahl 点只在 \(O(\lambda^4)\) 相互作用且无对数项”强于 §17。

已证明的是：

- 线性尾项的球面平均为零；
- 不出现对应的对数项。

尚未计算的是
\[
\lambda^4\mathcal Q_\Gamma(\nabla\operatorname{Rm}_p,R_p).
\]

替换为：

> Wahl 点的线性尾配对没有对数项；预期的首个非零极化项位于 \(\lambda^4\) 阶，但其二次型 \(\mathcal Q_\Gamma\) 尚未确定。

Eguchi–Hanson 的
\[
P=\pi^2a^4|\mathbf R^+\zeta|^2+O(a^6)
\]
也只是在 Theorem 61.EH 的加权 gluing 邻域中有匹配上下估计，不能写成所有退化序列的无条件费用。

### 4. “三端”段落

在最佳符号类的 harmonic-flux ledger 中，
\[
p=q^2(1-\delta)^2+L,\qquad L\ge0,
\]
并且
\[
q^2=|a^-|^2\ge k+\Pi\ge k.
\]
因此固定拓扑 \(k\ge1\) 上
\[
p_j\to0
\quad\Longrightarrow\quad
\delta_j\to1,\qquad L_j\to0.
\]
这一点正确：任何零 \(P\)-序列都在积分意义上逼近 Einstein 端。

但后续措辞需细化：

- aligned 类 \(L=0,\ 0<\delta<1\) 在固定离开 \(\delta=1\) 时有
  \[
  p=q^2(1-\delta)^2>0;
  \]
  它也可能通过 \(\delta\uparrow1\) 逼近 Einstein 端。
- cscK 端 \(\delta=L=0\) 满足 \(p=q^2\ge k\)，不能直接产生 \(p\to0\)。
- aligned 几何说明 \(L\ge c\delta\) 这种普适估计若成立，就必须同时排除相应 Blair–Ianus/Einstein–Maxwell 结构；现有材料没有证明这些结构在目标流形上实际存在。
- product saddle 只表明跨所有 cscK 曲面不存在统一的 Kähler 端 Hessian 常数；它不是 \(X\#k\overline{\mathbb{CP}}^2\) 上的零间隙构造。

精确替换文本：

> 由于 \(q^2\ge k\)，任何 \(p\to0\) 序列都满足 \(\delta\to1\)、\(L\to0\)，即逼近 Einstein 端。aligned 序列只有在同时满足 \(\delta\to1\) 时才可能参与这一过程；cscK 端本身有 \(p\ge k\)。aligned 与 cscK 几何的作用，是说明若干自然 coercivity 形式不能仅由 ledger 的非负分解推出，而不是提供已构造的零间隙逃逸序列。

### 5. 最后“未解中心”的量词

原句覆盖整个 \(0<k<A/3\)，与 N1 窗口冲突。应改为：

> 对尚未被 N1 实际供给窗口或其他特殊输入覆盖的低 \(k/A\) 区域，目前既没有统一的 \(P_*>0\) 定理，也没有纯吹起族上 \(\alpha\to0\) 的闭流形构造。完整的 \(0<k<A/3\) 问题仍未解决，但其中靠近 \(1/3\) 的一段已有正分离结果。

---

## 七、§23.6 的状态

§23.6 标成 `[N]` 是正确的。

能够从给出的计算中读取的只有：

- Kähler control 收敛到 \(3\times10^{-10}\)，说明实现对 Kähler 精确解的处理一致；
- strict jet 的残差从约 \(5\times10^3\) 降至 \(0.13\)–\(0.15\)，但仍非零；
- 投影 Jacobian 秩为 \(91\)，非平凡行数为 \(119\)。

这些数值既不建立八阶形式解，也不建立八阶矛盾。因而：

- 79.C 已在六阶被反例数值推翻；
- 六阶只给出半代数条件 \(\Phi_6\le0\)；
- 八阶是否可解仍未决定；
- §24 关于 Problems 1–3 的任何结论都不应依赖 §23.6；
- §24.4 对 almost-Kähler torsion 的共同机制只能使用已证明的强迫零点、非退化零点指数 \(+1\) 和二阶锥关系，不能把高阶延拓写成已知障碍。

---

## 八、§24 对 Problems 1–3 还应补入的结果

### 1. 零值层面 \(P_*\) 与 \(\alpha\) 的等价

如上所述，对 \(0<k<A\)，应明确加入
\[
P_*=0\iff\alpha=0,\qquad
P_*>0\iff\alpha>0.
\]
这比只讨论“零值是否实现”更完整。

### 2. N1 给出的定量 \(P\)-下界

若 N1 给出 \(\mathcal J\ge\delta>0\)，且
\[
\int(s^-)^2\ge32\pi^2A,
\]
则
\[
P\ge\frac{8\pi^2\delta}{4-\delta}A.
\]
这说明 N1 不只是 Einstein 非存在，也给出真正的未归一化正间隙。

### 3. Anderson 的零 \(P\) 结构定理

§20.5 的 Theorem 59.Z 与 Problems 1–2 直接相关，应在 §24 中出现：

在引用 Anderson Theorem 4.10 及 removability 后，若 \(P_*(M)=0\)，某个选定极小序列产生以下之一：

- 紧 Einstein 轨形；
- 分片完整 Einstein 域加外部塌缩；
- 总塌缩。

这给出了“\(P_*=0\) 但不实现”必须通过何种几何发生，正是 Problem 1 与 Problem 2 之间缺失的结构连接。

### 4. \(k=1\) 的轨形细分

§§16–17 已将非平凡局部群的 \(k=1\) 情形细分为：

- 带 \(b_2=1\) 的 charge-allowed 泡；
- rational-ball/Wahl 通道；
- 若干非循环端；
- 条件性 orbifold attainment 定理 56.A。

这些结果尚未给出 \(M\) 上的光滑极小元，但它们比 §24 中“orbifold absorption”一句更具体，且直接描述 Theorem 54.A 之外的剩余几何。

### 5. Problem 3 的 existential 量词

应明确写一句：

> Problem 3 只需一个闭四流形上的一个非 Bach 平坦全局极小元。一般型吹起提供的是一条系统性候选路线，而不是原问题要求的唯一流形类别。

### 6. 第二阶 Burns 结果与实现问题的关系

Theorem 59.R 说明标准 Burns 分裂并非极小；Theorem 53 的未闭部分说明，要从这一局部严格改进推出全局实现，还需处理：

- 塌缩；
- 轨形吸收；
- exotic homotopy-sphere 泡；
- 一般 \(P\)-临界 bulk 上的严格次可加性。

这应与 Problem 3 的实现讨论并列，而不只作为 Problem 2 的上界。

---

## 九、所需外部知识请求

1. **LeBrun Yamabe 定理的精确假设。**  
   请求原文中证明
   \[
   \mathcal Y(X\#k\overline{\mathbb{CP}}^2)
   =-4\pi\sqrt{2c_1^2(X)}
   \]
   的定理编号、页码及完整假设，特别说明：
   - 是否覆盖 \(p_g=0\)、\(b^+=1\) 的极小一般型曲面；
   - 腔依赖怎样消除；
   - 是否覆盖所有 \(k\ge0\)。

2. **LeBrun 的 \(P\)-下界在 \(b^+=1\) 时的版本。**  
   请求
   \[
   P_*(X\#k\overline{\mathbb{CP}}^2)
   \ge8\pi^2\max\{0,k-A/3\}
   \]
   对 \(b^+=1\) 的原始定理、腔选择和全度量量词。

3. **实双曲四流形吹起无正标量曲率的精确来源。**  
   请求一个明确覆盖所有闭定向实双曲四流形 \(Y\)、包括非 spin 情形的定理，证明
   \[
   Y\#k\overline{\mathbb{CP}}^2
   \]
   不承载正标量曲率度量；并说明 degree-one pinch map 是否足够。

4. **Bourguignon 标量平坦变形定理。**  
   请求“闭流形上的标量平坦度量若非 Ricci-flat，则存在正标量曲率度量”的原始定理与精确表述。

5. **PSC summand 消灭 Seiberg–Witten 不变量的 one-sided neck 版本。**  
   请求 Lemma 54.3 所需的精确引用，特别覆盖
   \[
   M=Z\#R,\qquad b^+(Z)\ge1,\quad Z\text{ 有 PSC},\quad b^+(R)=0
   \]
   的情形。

以上修正后，§24 可以成为 Problems 1–3 的可靠综合：已证明部分、继承输入、条件性紧致性结果和真正未定的几何机制会彼此清楚分开。