# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/workspace/notes/step72_orientation_free_weyl_deficit_law.md",
    "Sessions/S1003A02/workspace/notes/step74_packing_weyl_theorem_and_scope.md"
  ]
}
```

## Task

Read the repaired theorem package as a mathematical referee with emphasis on the Step-70 P versus human-defect split: Corollary 52.8 and covering factors, §§13–20 degeneration/attainment statements, Lemma 54.3's one-sided PSC neck argument and status, and §§24.0–24.4. Test the proposed new synthesis that an S^4/Z2 orbifold summand cannot move the Weyl-deficit frontier beyond h=1/3: use orbifold Euler characteristic, d=8pi^2 chi_orb-W, the connected-sum correction -16pi^2, and conservation of d under Ricci-flat ALE resolution. Identify mathematically consequential remaining errors or scope changes and give precise replacement text, while keeping the hard range 0<k<A/3 explicit.

## Output

# 数学核验备忘录

## 一、总体判断

Step-70 之后对 \(P_*=\inf\int|\operatorname{Ric}^{\circ}|^2\) 与人类泛函
\[
\alpha(M)=\inf_g\mathscr D(g),\qquad
\mathscr D(g)=\inf_{\lambda\ne0}
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V},
\]
的分离在主定理包中基本正确。特别是：

- \(P\) 在有限覆盖下乘覆盖次数，而 \(\mathscr D\) 不变；
- Ricci-flat ALE 消解总给出 \(P_*=0\)，但只有非零 Einstein 尺度的 orbifold bulk 才由该构造给出 \(\alpha=0\)；
- Anderson 型极限理论目前是 \(P\)-极小序列的理论，不能直接移作 \(\alpha\)-极小序列的结构定理；
- 在一般型吹起流形上、\(1\le k<A\) 时，
  \[
  P_*=0\iff\alpha=0,\qquad P_*>0\iff\alpha>0,
  \]
  但这只是两个下确界是否为零的等价，不等同于极小序列或达到性的等价。

仍有四处需要实质修订：

1. `step52_residual_norm_selection_absorption.md` 本身仍保留 Step-70 以前的 \(\alpha\) 记号和错误的覆盖因子；主定理包虽已修正，但源文件仍会造成后续误引。
2. §17 中“Ricci-flat Einstein bulk 当且仅当不给出 \(\alpha=0\)”被写成了一个双向结论；现有论证只给出一个方向。
3. Lemma 54.3 的 \(S^3\)-neck 单侧 PSC 论证在数学上可完成，但当前材料没有登记精确文献定理，适宜保持为“依赖标准圆柱端紧致性”的结果；它不能自动扩展到 \(S^3/\Gamma\) 链接。
4. \(S^4/\mathbb Z_2\) 通道确实在 orbifold 加和—缩小 Eguchi–Hanson 消解这一特定构造中止于 \(h=1/3\)，但不能表述为光滑流形全部度量的 Weyl 前沿，因为 Theorem 74.W 已经在某些深覆盖上越过 \(1/3\)。

---

## 二、Corollary 52.8：覆盖因子

设 \(\pi:\widetilde V\to V\) 是次数 \(q\) 的 orbifold 覆盖，\(g\) 是 \(V\) 上的 orbifold 度量。则
\[
P(\pi^*g)=qP(g),\qquad
R(\pi^*g)=qR(g),\qquad
L_s(\pi^*g)=qL_s(g),
\]
因为
\[
\int_{\widetilde V}s=q\int_Vs,\qquad
\operatorname{Vol}(\widetilde V)=q\operatorname{Vol}(V).
\]
因此
\[
\boxed{\mathscr D(\pi^*g)=\mathscr D(g)}.
\]
同理，Weyl deficit 本身乘次数：
\[
d(\pi^*g)=q\,d_{\rm orb}(g),
\]
但归一化比值 \(d/R\) 不变。

对
\[
V=X\#(S^4/\mathbb Z_2),\qquad
Z=X\#X,\qquad V=Z/\iota,
\]
正确关系是
\[
P_{*,\rm orb}(V)=\frac12P_*^\iota(Z),
\qquad
\boxed{\alpha_{\rm orb}(V)=\alpha^\iota(Z)}.
\]
因而 Ricci-flat ALE 消解给出
\[
P_*(X\#2\overline{\mathbb{CP}}^2)
\le\frac12P_*^\iota(X\#X),
\]
而人类泛函满足
\[
\boxed{
\alpha(X\#2\overline{\mathbb{CP}}^2)
\le\alpha^\iota(X\#X),
}
\]
没有 \(\tfrac12\)。

### 可直接替换 Corollary 52.8 的文本

> 记 \(P_*^\iota(Z)\) 与 \(\alpha^\iota(Z)\) 分别为 \(\iota\)-不变度量上的 \(P\) 与 \(\mathscr D\) 下确界。若 \(V=(X\#X)/\iota=X\#(S^4/\mathbb Z_2)\)，则
> \[
> P_{*,\mathrm{orb}}(V)=\frac12P_*^\iota(X\#X),
> \qquad
> \alpha_{\mathrm{orb}}(V)=\alpha^\iota(X\#X).
> \]
> Ricci-flat Eguchi–Hanson 消解进一步给出
> \[
> P_*(X\#2\overline{\mathbb{CP}}^2)
> \le\frac12P_*^\iota(X\#X),
> \]
> \[
> \alpha(X\#2\overline{\mathbb{CP}}^2)
> \le\alpha^\iota(X\#X).
> \]
> 任意 \(\iota\)-不变 Einstein 度量都给出 \(P_*=0\)；只有当其 Einstein 常数非零时，Lemma 86.S 才进一步给出 \(\alpha=0\).

`step52_residual_norm_selection_absorption.md` 中 Theorem 52.3、Theorem 52.5、Corollary 52.9(ii) 凡是从 \(P(g_i)\to\cdots\) 出发的 \(\alpha(M)\)，均应写成 \(P_*(M)\)。这些段落描述的是 \(P\)-Palais–Smale 序列，而不是 \(\mathscr D\)-极小序列。

---

## 三、§§13–20：退化与达到性的正确字典

几类构造对两个泛函的作用如下。

| 几何过程 | \(P\) 的行为 | \(\mathscr D\) 的行为 |
|---|---:|---:|
| Einstein orbifold，\(\Lambda\ne0\)，Ricci-flat ALE 消解 | \(P\to0\) | \(\mathscr D\to0\) |
| Ricci-flat orbifold，Ricci-flat ALE 消解 | \(P\to0\) | 该消解族有 \(\mathscr D\to4\) |
| bulk 加入标量平坦、\(P(N)>0\) 的 ALE/AE bubble | \(P\) 增加 \(P(N)\) | 数值向 \(4\) 移动 |
| 有限覆盖 | 乘覆盖次数 | 不变 |
| \(P_*=0\) 且达到 | 存在 Einstein 度量，允许 Ricci-flat | 不自动推出 \(\alpha=0\) |
| \(\alpha=0\) 且达到 | — | 存在 \(\Lambda\ne0\) 的 Einstein 度量 |

Lemma 86.S′ 的精确公式
\[
\mathscr D(g_\varepsilon)\longrightarrow
\frac{4P(g)+L_s(g)+4B}{R(g)+B},
\qquad
B=\sum_jP(N_j),
\]
说明标量平坦且 \(P(N_j)>0\) 的 bubble 不是 \(\alpha\)-零间隙通道。事实上
\[
4-
\frac{4P+L_s+4B}{R+B}
=
\frac{4R-(4P+L_s)}{R+B}
=
\frac{\bigl(\int s\bigr)^2}{V(R+B)}.
\]
因此 \(B\) 增大时该值趋向 \(4\)。只有 Ricci-flat bubble 的 \(B=0\) 才在极限中保持 bulk 的 \(\mathscr D\)。

对 Ricci-flat orbifold bulk，朴素消解满足
\[
R(g_\varepsilon)=O(\rho^4),\qquad
\int s_{g_\varepsilon}=O(\rho^4),
\]
所以
\[
\mathscr D(g_\varepsilon)
=
4-\frac{O(\rho^8)}{V\,O(\rho^4)}
=4-O(\rho^4).
\]
这并不决定光滑消解流形的 \(\alpha\)，因为它还可能存在完全不同的度量族。

### §17 中需要更换的句子

现有文字：

> an Einstein bulk implies \(\alpha(M)=0\) exactly when its Einstein constant is nonzero.

应替换为：

> 若 \(g_0\) 是 Einstein orbifold 度量且 Einstein 常数 \(\Lambda\ne0\)，则 Lemma 86.S 给出其 Ricci-flat ALE 或 Wahl smoothing 满足 \(\alpha(M)=0\)。若 \(\Lambda=0\)，同一构造只给出 \(P_*(M)=0\)，并且所构造的度量族满足 \(\mathscr D\to4\)；它不决定 \(\alpha(M)\) 的值。

Corollary 56.B 已采用后一种表述，故 §17 的 Theorem 56.A 概述需要与之统一。

### Anderson 极限理论的读法

§20.5 的处理是正确的：Theorem 59.Z 是 \(P_*=0\) 的结构定理。即使已有一个 \(\mathscr D\to0\) 序列，也不能假定 Anderson 选出的 \(P\)-序列保持归一化后的非零 Einstein 尺度。因此目前只能说：

- 若同一个 \(\mathscr D\)-小序列具有所需非塌缩紧致性，则其光滑极限为 \(\operatorname{Ric}=\pm g\)；
- 已有 \(P\)-极限三分结构不能直接推出完整的 \(\alpha\)-三分结构；
- \(P_*=0\) 与 \(\alpha=0\) 在一般型吹起且 \(k<A\) 时数值上等价，但其极小序列仍可能不同。

---

## 四、Lemma 54.3：单侧 PSC neck 论证

该引理的核心数学机制成立。对固定 Spin\(^c\) 结构：

1. 在 PSC summand \(Z\setminus B^4\) 上选取圆柱型 \(S^3\) 末端的 torpedo 度量；
2. 选取支撑在 \(Z\) 内部的小扰动 \(\eta\)；
3. Weitzenböck 公式排除不可约有限能量解；
4. 可约解要求
   \[
   \mathcal H^+(\eta)=2\pi\,c_1(L|_Z)^+
   \]
   在 \(L^2\) 调和自对偶空间中成立；
5. 因 \(b^+(Z)\ge1\)，泛型 \(\eta\) 避开该仿射子空间；
6. 标准长颈紧致性于是推出充分长的 neck 上模空间为空；
7. \(b^+(M)\ge2\) 保证闭流形 SW 不变量不依赖所选度量和扰动。

这确实覆盖 \(b^+(R)=0\) 的情形，而普通的“两侧 \(b^+>0\)”连通和定理不覆盖它。

提供的材料中尚未登记与此完全同量词的文献陈述；Frøyshov 材料支持长颈紧致性，但不是该单侧消失定理本身。因此主定理包把它标为 `[P*]` 是合适的。其正式文本可写成：

> **Lemma 54.3 [P\(^*\)].** 假设采用圆柱端 Seiberg–Witten 解的标准长颈紧致性定理。若
> \[
> M=Z\#R,\qquad b^+(M)\ge2,
> \]
> 且 \(Z\) 有 PSC 度量、\(b^+(Z)\ge1\)，则 \(M\) 的所有 Seiberg–Witten 不变量为零。

两个适用对象必须保持分开：

- 此论证使用圆 \(S^3\) 上唯一平坦可约点；
- 对 \(S^3/\Gamma\) 链接，Floer 修正项、多个可约点及 orbifold Spin\(^c\) 数据会进入，不能由 Lemma 54.3 自动推出。§16 的 SW\(_L\) 仍是额外输入。

Theorem 54.A 因而仍依赖其列出的光滑收敛、能量等式、可去奇点和 AE 衰减输入；Lemma 54.3 本身并未解决 orbifold concentration 或 collapse。

---

## 五、\(S^4/\mathbb Z_2\) 与 \(h=1/3\) 的 Weyl-deficit 计算

这里必须使用 Chern–Gauss–Bonnet 所对应的 Satake orbifold Euler 数，而不是 stringy Euler 数。令
\[
\mathcal O=S^4/\mathbb Z_2
\]
为有两个 \(A_1\) 点的 round quotient。则
\[
\chi_{\rm orb}(\mathcal O)=\frac{\chi(S^4)}2=1,\qquad
\tau_{\rm orb}(\mathcal O)=0,\qquad
\mathcal W_*(\mathcal O)=0,
\]
所以
\[
d_{*,\rm orb}(\mathcal O)=8\pi^2.
\]

设 \(X\) 是球商，\(A=c_1^2(X)\)。于是
\[
\chi(X)=\frac A3,\qquad
\tau(X)=\frac A9.
\]
复双曲度量满足
\[
\mathcal W_*(X)=12\pi^2\tau(X)=\frac{4\pi^2A}{3},
\qquad
d_*(X)=\frac{4\pi^2A}{3}.
\]

令
\[
V_m=X\#m\mathcal O,
\]
连通和都在光滑点进行。则
\[
\chi_{\rm orb}(V_m)=\frac A3-m,\qquad
\tau_{\rm orb}(V_m)=\frac A9.
\]

### 1. 连通和给出的下界

每次连通和有 \(-16\pi^2\) 的 Euler 修正，故
\[
d_{*,\rm orb}(V_m)
\ge
d_*(X)+m\,d_{*,\rm orb}(\mathcal O)-16\pi^2m,
\]
即
\[
d_{*,\rm orb}(V_m)
\ge
\frac{4\pi^2A}{3}-8\pi^2m.
\]

### 2. orbifold signature 给出的反向估计

在本会话的曲率算子范数下，
\[
I_+-I_-=12\pi^2\tau_{\rm orb}.
\]
因此
\[
\mathcal W=I_++I_-\ge12\pi^2|\tau_{\rm orb}|
=\frac{4\pi^2A}{3}.
\]
于是
\[
d_{\rm orb}(g)
\le
8\pi^2\Bigl(\frac A3-m\Bigr)-\frac{4\pi^2A}{3}
=
\frac{4\pi^2A}{3}-8\pi^2m.
\]
上下两式相合：
\[
\boxed{
d_{*,\rm orb}(V_m)
=
4\pi^2\left(\frac A3-2m\right).
}
\]

### 3. Eguchi–Hanson 消解保持 \(d\) 的极限值

\(V_m\) 有 \(2m\) 个 \(A_1\) 点。每个 Eguchi–Hanson 空间满足
\[
\int_{\rm EH}|W|^2
=
8\pi^2\left(\chi({\rm EH})-\frac12\right)
=12\pi^2.
\]
消解后
\[
M=X\#2m\overline{\mathbb{CP}}^2,
\qquad
\chi(M)-\chi_{\rm orb}(V_m)=3m,
\]
而 EH 总 Weyl 能量为
\[
2m\cdot12\pi^2=24\pi^2m=8\pi^2\cdot3m.
\]
两项正好抵消，故对任何固定 orbifold 度量 \(g\)，缩小 EH 消解满足
\[
\boxed{
d(M,g_\varepsilon)\longrightarrow d_{\rm orb}(V_m,g).
}
\]
同一结论也直接来自
\[
d=\frac1{24}\int s^2-\frac12P:
\]
Ricci-flat ALE 部分对这两项均无主阶贡献。

令 \(k=2m\)、\(h=k/A\)，便得到
\[
d_{*,\rm orb}(V_m)=4\pi^2\left(\frac A3-k\right).
\]
因此该 orbifold-summand 加缩小 EH 的通道具有正 Weyl deficit 恰好在
\[
k<\frac A3.
\]

### 正确的综合表述

> 对球商 \(X\)，round \(S^4/\mathbb Z_2\) orbifold summand 与缩小 Eguchi–Hanson 消解这一特定通道的最优 orbifold Weyl deficit 为
> \[
> 4\pi^2(A/3-k),\qquad k=2m.
> \]
> 所以该零尺度吸收通道不能把正 Weyl deficit 延伸到 \(h>1/3\)。在 \(h=1/3\) 时主阶值为零，有限尺度高阶项仍需单独计算。

这不能改写成“\(X\#2m\overline{\mathbb{CP}}^2\) 的全部光滑度量均不能越过 \(1/3\)”。Theorem 74.W 已在适当深覆盖上用有限尺度 CH-collared blow-up cells 构造出
\[
d>0,\qquad h>\frac13.
\]
所以 \(S^4/\mathbb Z_2\) 结论只属于 orbifold-summand/EH 消解通道，而不是光滑流形的全局 Weyl 泛函定理。

此外，`step74_packing_weyl_theorem_and_scope.md` 的证明中有一个因子三的文字错误：

> “signature formula with \(\tau=A_Y/3\)”

应为

\[
\boxed{\tau(Y)=A_Y/9.}
\]
最终数值
\[
I_+=12\pi^2\tau=\frac{4\pi^2A_Y}{3}
\]
是正确的。

---

## 六、§§24.0–24.4 的核验

### 已正确闭合的部分

1. **L1** 正确：一般型吹起流形的 Yamabe 不变量严格小于零，所以任何 Einstein 度量都满足 \(\Lambda<0\)，从而
   \[
   \text{Einstein}
   \iff \alpha=0\text{ 且达到}
   \iff P_*=0\text{ 且达到}.
   \]

2. **L2** 的常数正确。由
   \[
   C_+=T_++\mathfrak p,\qquad
   R\le8\pi^2(4\mathfrak p+3T_+)
   \]
   得
   \[
   \mathscr D(g)\ge
   \frac{\mathfrak p}{\mathfrak p+\frac34T_+}.
   \]
   代入
   \[
   \mathfrak p_*\ge k-\frac A3,\qquad T_+=A-k
   \]
   恰得
   \[
   \alpha\ge\frac{4(3k-A)}{3k+5A}.
   \]

3. **L3** 正确，但只涉及是否为零：
   \[
   P_*=0\iff\alpha=0,\qquad 1\le k<A.
   \]
   这里不包含极小序列相同、极限相同或达到性相同。

4. §24.3 对 k=1 球商的条件性结论已正确区分：
   - 光滑 bulk \(V\) 与原流形 \(M\) 可能相差 exotic homotopy sphere；
   - 只有这些 bubble cap 都微分同胚于 \(S^4\) 时，才得到 \(M\) 上的光滑极小度量；
   - Einstein 分支与 non-Bach-flat 分支仍由 Problem 1 的未解部分分开。

### 需要改名的一处

§24.1(4) 的标题

> “The one realized zero-gap architecture on a fixed blow-up”

不宜使用 “realized”，因为同段末尾明确写着：对一般型 \(X\) 尚无这样的 Einstein orbifold 实例。可替换为：

> **A sufficient zero-gap architecture whose existence is presently open for these blow-ups.**

中文正文可写：

> 若存在 Einstein 常数非零、且其 Ricci-flat ALE 消解或 Wahl smoothing 微分同胚于 \(M\) 的紧 orbifold \(V\)，则 \(\alpha(M)=0\)。对当前的一般型吹起族，尚无这样的 \(V\) 被构造出来。

---

## 七、硬区间 \(0<k<A/3\) 的最终数学状态

修订后，核心未知仍然完整保留：

\[
\boxed{0<k<A/3.}
\]

在此区间已经知道：

\[
0\le\alpha(M)<\frac{4k}{A+k}<1,
\]
\[
P_*(M)=0\iff\alpha(M)=0,
\]
\[
\alpha(M)=0\text{ 且达到}
\iff M\text{ 有 Einstein 度量}.
\]

尚未确定的是：

- 对任意固定 \(M=X\#k\overline{\mathbb{CP}}^2\)，是否 \(P_*(M)>0\)；
- 是否存在未达到的 \(P_*=\alpha=0\) 序列；
- 是否存在光滑 Einstein 度量；
- 是否存在 Einstein 常数非零的吸收型 orbifold，其消解或 smoothing 为 \(M\)；
- collapse、Wahl 通道及非平凡 orbifold link 是否能实现零间隙。

上面的 \(S^4/\mathbb Z_2\) 计算只说明：round orbifold summand 与缩小 EH 消解不会把该特定通道推到 \(h>1/3\)。它在 \(0<k<A/3\) 内仍允许非零尺度 Einstein orbifold，并未给出正下界。因此它没有化解该硬区间，反而精确定位了一个结论：若该吸收架构产生 \(\alpha=0\)，它只能发生在现有未解区间之内。