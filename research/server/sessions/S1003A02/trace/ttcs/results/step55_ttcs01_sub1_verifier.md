# TTCS Independent Branch Record

```json
{
  "step_id": 55,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/workspace/scripts/step55_orbifold_bubble_charges.py",
    "Sessions/S1003A02/workspace/scripts/step55_Tchain_embeddings.py",
    "Sessions/S1003A02/workspace/scripts/step55_Tchain_discriminants.py",
    "Sessions/S1003A02/workspace/data/step55_Tchain_embeddings.json"
  ]
}
```

## Task

Verify the mathematics of the Step-55 note (k=1 orbifold gate for P=int|Ric°|^2 on M = X # CP2bar, X a compact ball quotient). Check carefully and report concrete errors with corrections: (1) the two-orientation ALE charge formula (1.1) c_± = 2/|Γ| − 2χ ∓ 3τ ∓ 3η with η = −4 s(q,n) (Dedekind sum), its sign conventions as fixed by Burns, Eguchi–Hanson, A_{n−1}, and the numerically verified LeBrun O(−n) value P = 8π²(n−2)²/n; (2) the ledger identities (1.2) T_+^orb(V) = T_+(M) + c_+(N) and (1.3); (3) Lemma 55.1 (degree-one/free-indecomposability argument that orbifold bubble regions have H_2 ⊂ ZE, including whether the one-sided SW vanishing with a PSC orbifold cap is a correct/standard input); (4) Prop 55.3: the claim that m=1,2 cyclic-end b2=1 bubbles have c_+=1 (linking-form restriction q a unit square mod m^2), the surviving lists, and the noncyclic D_5, D_9, E_8 analysis (orientation and linking-form compatibility, the trefoil-trace realization); (5) Prop 55.4 (T-singularity Milnor fibres have charge 0 in complex orientation and −4(1−1/n²) reversed; Ricci-flat Kähler ALE on them); (6) Theorem 55.5: π1 pushout, degree one, K unimodular negative definite of rank r+1, the H_1-torsion argument forcing primitivity (gcd(o,n)=1 ⇒ o=1), and the discriminant criterion 1−na unit square mod n² ⇔ n odd or 8|n — including whether the discriminant form of the T-chain is ⟨(1−na)/n²⟩ and whether the anti-isometry condition is stated with the right sign; (7) Prop 55.6 blow-up counting argument (Σ(−D_j²) ≤ 3r+1 over r+1 exceptional components; T-chains have Σb_i = 3r+1) and its use of SW/general type; (8) Lemma 55.8 and the collapse discussion, especially the claim that a collapsed region with τ(C) = −1 would make the ledger favorable to absorption. Also say whether the n=3 example ([5,2] chain realized by 2E1+E2 and E2+E3 in #3CP2bar) is correct as a lattice/topology statement, and whether Theorem 55.7's trichotomy follows. Write a direct mathematical memo.

## Output

# Step 55 数学核验备忘

## 总结

以下部分是正确的：

1. ALE 两种取向的电荷公式 (1.1)，包括 \(\eta(n,q)=-4s(q,n)\) 的符号；
2. Burns、Eguchi–Hanson、\(A_{n-1}\) 以及 LeBrun \(\mathcal O(-n)\) 的数值；
3. 拼接恒等式 (1.2)、(1.3)；
4. 在额外的单侧 Seiberg–Witten 消失输入成立时，Lemma 55.1 的度数一与自由积论证；
5. 单连通、\(b_2=1\) 的循环端情形中 \(m=1,2\) 的电荷，以及 \(D_5,D_9,E_8\) 的 ADE 算术；
6. T-奇点 Milnor 纤维的两种取向电荷；
7. Theorem 55.5 的基本群、度数一、核格、原始嵌入和判别群计算；
8. \(n=3\) 的 \([5,2]\) 格嵌入；
9. Lemma 55.8。

需要实质修正的地方有四处：

- Prop. 55.3 的枚举只覆盖**单连通且端群为循环群或纯 ADE 群**的 \(b_2=1\) 区域，不能作为全部 orbifold bubble 的枚举。
- “零电荷有理球恰好都是 T-奇点 Milnor 纤维”尚未由文中计算证明；文中严格得到的是 T 型 \(\Rightarrow\) 零电荷。
- Prop. 55.6 原有的 SW/极小模型论证缺少关键推理；不过其结论可由 Kähler 性、Eells–Sampson–Siu 刚性和双有理分解完整修复。
- Theorem 55.7 的详细三分法、所有 bulk 均非 Kähler、以及零能量 bubble 时的等式，需要附加拓扑枚举和重组分析；现有材料只支持按 \(b_2=1\) 或 \(b_2=0\) 的粗分。

---

## 1. ALE 电荷公式与符号

设 \(N\) 是单端 ALE 四流形，端群为 \(\Gamma\)。所用 Gauss–Bonnet 与 APS 符号应写成

\[
8\pi^2\left(\chi(N)-\frac1{|\Gamma|}\right)
=
\int_N\left(
|W^+|^2+|W^-|^2-\frac12|\Ric^\circ|^2+\frac{s^2}{24}
\right),
\]

\[
\tau(N)
=
\frac1{12\pi^2}\int_N\left(|W^+|^2-|W^-|^2\right)-\eta_\Gamma.
\]

因此

\[
\int_N|\Ric^\circ|^2
=
4\int_N|W^+|^2+\frac1{12}\int_Ns^2
+8\pi^2
\left(
\frac2{|\Gamma|}-2\chi-3\tau-3\eta_\Gamma
\right),
\]

以及

\[
\int_N|\Ric^\circ|^2
=
4\int_N|W^-|^2+\frac1{12}\int_Ns^2
+8\pi^2
\left(
\frac2{|\Gamma|}-2\chi+3\tau+3\eta_\Gamma
\right).
\]

故 (1.1)

\[
c_\pm=\frac2{|\Gamma|}-2\chi\mp3\tau\mp3\eta_\Gamma
\]

正确。

对循环作用
\[
(z_1,z_2)\longmapsto (\zeta z_1,\zeta^qz_2),
\qquad \zeta=e^{2\pi i/n},
\]
采用
\[
\eta(n,q)=-4s(q,n)
\]
与上述 APS 公式相容。

### 标准模型

- Burns：\(n=1,\chi=2,\tau=-1,\eta=0\)，故
  \[
  (c_+,c_-)=(1,-5).
  \]

- Eguchi–Hanson：\(n=2,q=1,\eta=0\)，故
  \[
  (c_+,c_-)=(0,-6).
  \]

- \(A_{n-1}\) Kronheimer 空间：\(q=-1\pmod n\)，
  \[
  \eta(n,-1)=\frac{(n-1)(n-2)}{3n},
  \]
  且 \(\chi=n,\tau=-(n-1)\)，代入得到 \(c_+=0\)。

- \(\mathcal O(-n)\) 的端作用为 \(q=1\)，
  \[
  \eta(n,1)=-\frac{(n-1)(n-2)}{3n}.
  \]
  因此
  \[
  c_+=\frac2n-1-3\eta(n,1)=\frac{(n-2)^2}{n}.
  \]

LeBrun 度量是标量平坦 Kähler 度量；按复取向 \(W^+=0\)，于是无需数值积分也已严格得到

\[
P(g_{\rm LeB})=8\pi^2\frac{(n-2)^2}{n}.
\]

`step55_orbifold_bubble_charges.py` 的积分是对这一精确恒等式的独立数值一致性测试。脚本中的 Dedekind 和精确分数运算没有发现符号错误。

---

## 2. 拼接账本 (1.2)、(1.3)

设 \(M=V^\circ\cup_LN\)，其中 \(L=S^3/\Gamma\)。有

\[
\chi(M)=\chi(V^\circ)+\chi(N),
\]
而 orbifold Euler 数为
\[
\chi_{\rm orb}(V)=\chi(V^\circ)+\frac1{|\Gamma|}.
\]

取 \(L\) 的取向为 ALE 端的取向，则

\[
\tau_{\rm orb}(V)=\tau(V^\circ)-\eta_\Gamma.
\]

由 Novikov 可加性，
\[
\tau(M)=\tau(V^\circ)+\tau(N).
\]

所以

\[
\begin{aligned}
T_+^{\rm orb}(V)-T_+(M)
&=
\frac2{|\Gamma|}-2\chi(N)-3\tau(N)-3\eta_\Gamma\\
&=c_+(N).
\end{aligned}
\]

这正是

\[
T_+^{\rm orb}(V)=T_+(M)+c_+(N).
\]

若 \(N\) 标量平坦，并定义

\[
C_+(V)=\frac1{2\pi^2}\int_V|W^+|^2+
\frac1{96\pi^2}\int_Vs^2,
\qquad
w(N)=\frac1{2\pi^2}\int_N|W^+|^2,
\]

则

\[
\frac{P(V)}{8\pi^2}=C_+(V)-T_+^{\rm orb}(V),
\qquad
\frac{P(N)}{8\pi^2}=w(N)+c_+(N).
\]

相加即得

\[
\frac{P(V)+P(N)}{8\pi^2}
=
C_+(V)+w(N)-T_+(M).
\]

因此 (1.3) 也正确。

对于多层 bubble tree，“\(N_{\rm eff}\)”应理解为拓扑重组后的区域，而 \(P,w\) 是各层积分之和。内部端截面的 \(\eta\)-项逐对抵消。它不必是一张单独的完备 ALE 度量，但加法公式仍成立。

---

## 3. Lemma 55.1

### 自由积部分

设
\[
A=\pi_1(V^\circ),\qquad B=\pi_1(N),\qquad H=\pi_1(L).
\]
Van Kampen 给出
\[
\Gamma=A*_HB.
\]

\(H\) 有限，而 \(\Gamma\) 无挠，所以 \(H\) 在 \(\Gamma\) 中的像为平凡群。因此

\[
\Gamma\cong
\bigl(A/\langle\!\langle H\rangle\!\rangle\bigr)
*
\bigl(B/\langle\!\langle H\rangle\!\rangle\bigr).
\]

\(\Gamma\) 单端且自由不可分，故两个因子中恰有一个承载 \(\Gamma\)，另一个为平凡群。这一步正确。

若承载 \(\Gamma\) 的是 bubble 因子，则 classifying map \(c:M\to X\) 在 \(V^\circ\) 上零伦，因而经

\[
M/V^\circ\simeq \widehat N
\]

分解。该分解仍有度数一，因此

\[
Q_X\hookrightarrow Q_N,
\qquad b^+(N)\ge b^+(X)\ge3.
\]

这也正确。

若承载 \(\Gamma\) 的是 bulk 因子，则 \(c|_N\) 的基本群像为平凡群，故提升到可缩的 \(\widetilde X\)，从而

\[
H_2(N;\mathbb Q)\longrightarrow H_2(X;\mathbb Q)
\]

为零。Mayer–Vietoris 给出

\[
H_2(M;\mathbb Q)
\cong
H_2(V^\circ;\mathbb Q)\oplus
\bigoplus_jH_2(N_j;\mathbb Q),
\]

且各项关于交叉形式正交。于是每个 \(H_2(N_j;\mathbb Q)\) 嵌入

\[
\ker(c_*)=\mathbb QE,
\]

所以 \(b_2(N_j)\le1\)，并且至多一个 \(N_j\) 有 \(b_2=1\)。

### 单侧 SW 消失输入

当分割两侧都有 \(b^+>0\) 时，沿正标量曲率有理同调三球的通常 SW 消失定理可以直接使用。

当 \(b^+(V^\circ)=0\)、\(b^+(N)>0\) 时，文中的“PSC orbifold cap 单侧版本”不是仅凭一句“\(\widehat N\) 有 PSC orbifold 度量”就自动得到的。完整论证需要：

1. 将 orbifold 点删去后构造带圆柱端的 PSC 度量；
2. 处理 \(L\) 上有限多个平坦可约解；
3. 用 \(b^+(N)>0\) 的自对偶扰动避开所有可约壁；
4. 使用沿 \(L\) 拉长的 monopole 紧致性与粘合。

这一论证与 Lemma 54.3 的思路一致，数学上是可信的，但精确的 orbifold-cap 形式应保留为明确假设，或补出上述相对 SW 论证。只要接受这一输入，Lemma 55.1 的其余部分成立。

---

## 4. Prop. 55.3：循环端与 ADE 端

### 4.1 循环端的正确部分

对 \(b_2(N)=1\) 的区域，有限端群正常生成 \(\pi_1(N)\)，故 \(b_1(N;\mathbb Q)=0\)，并有

\[
\chi(N)=2,\qquad \tau(N)=-1.
\]

若进一步假设 \(N\) 单连通，设生成元映到 \(mE\)，则交叉格为

\[
\langle -m^2\rangle,
\]

端截面的一级同调阶为 \(m^2\)。按本文的 lens-space 取向约定，其链接形式必须与

\[
\left\langle \frac1{m^2}\right\rangle
\]

同构，因而 \(q\) 是模 \(m^2\) 的单位平方。

于是

\[
c_+=\frac2{m^2}-1-3\eta(m^2,q),
\qquad
c_-=\frac2{m^2}-7+3\eta(m^2,q).
\]

- \(m=1\)：\(c_+=1\)；
- \(m=2\)：模 \(4\) 的唯一单位平方是 \(q=1\)，且
  \[
  \eta(4,1)=-\frac12,\qquad c_+=1.
  \]

所以单连通循环端的 \(E\) 或 \(2E\) bubble 确实至少耗费 \(8\pi^2\)。

脚本给出的首批剩余算术也正确：

\[
m=3,\quad q=4,7:
\qquad
(c_+,c_-)=\left(-\frac{23}{9},-5\right),
\]

以及 \(m=4,q=9\) 时 \(c_+=1/4\)。

### 4.2 关键缺口：Lemma 55.1 没有推出 \(\pi_1(N)=1\)

自由积分解只给出

\[
\pi_1(N)/\langle\!\langle\pi_1(L)\rangle\!\rangle=1,
\]

即 \(\pi_1(N)\) 由端群正常生成，不等于单连通。

一般情形中，\(|H_1(L)|=m^2\) 不再成立；公式还会出现
\(\operatorname{Tor}H_1(N)\) 和可能的
\(\operatorname{Tor}H_2(N)\) 因子。因此：

- \(n=m^2\)；
- \(q\) 必须为单位平方；
- Prop. 55.3 的循环端枚举；

都只对单连通 \(N\) 成立。

此外，自由作用于 \(S^3\) 的有限群并不只有循环群与纯 ADE 群。一般还存在由左右乘作用产生的其他 spherical space-form 群。现有 ADE 计算不能覆盖这些端群。

因此 Prop. 55.3 应改写为：

> 对单连通、\(b_2=1\)，且端群为循环群或 \(\Gamma\subset SU(2)\) 的 bubble，电荷与链接形式留下文中所列情形。

不能据此得到全部 \(b_2=1\) orbifold bubble 的枚举。

### 4.3 ADE 部分

在 Kronheimer 取向下，

\[
\eta_\Gamma=\frac{2/|\Gamma|+r-2}{3}.
\]

对 \(\chi=2,\tau=-1\) 的 rank-one 区域，

\[
c_+=1-r,\qquad
c_-=\frac4{|\Gamma|}+r-9.
\]

这两个公式正确。

对 \(D_r\)，\(|\Gamma|=4(r-2)\)。奇数 \(r\) 时端截面的 \(H_1\cong\mathbb Z_4\)，其链接形式与
\(\langle1/4\rangle\) 相容恰当于

\[
r\equiv1\pmod4.
\]

结合电荷 \(r\le9\)，得到 \(D_5,D_9\)。偶数 \(D_r\) 的一级同调为
\(\mathbb Z_2\oplus\mathbb Z_2\)，不能来自单连通 rank-one 格。\(E_6,E_7\) 的一级同调阶分别为 \(3,2\)，也不合适；\(E_8\) 是整同调球，允许 \(m=1\)。

对 \(E_8\)：

\[
c_+=-7,\qquad c_-=-\frac{29}{30}.
\]

若 \(\Sigma(2,3,5)\) 取为负 \(E_8\) plumbing 的端取向，则左手 trefoil 的 \((-1)\)-trace 确实给出交叉格 \(\langle-1\rangle\) 和相同取向的 Poincaré 同调球。这一拓扑模型正确。

不过 \(D_5,D_9\) 目前只是链接形式和电荷允许的情形；文中没有构造相应的标量平坦 \(P\)-临界 ALE 度量。类似地，循环端表格中的每个 \(q\) 也不因链接形式相容就自动存在 rank-one 光滑 filling。`step55_orbifold_bubble_charges.py` 计算的是必要的算术数据，不是存在性证明。

---

## 5. Prop. 55.4：T-奇点 Milnor 纤维

对
\[
\frac1{n^2}(1,na-1),\qquad (n,a)=1,
\]
其 Milnor 纤维 \(B_{n,a}\) 满足

\[
\chi(B_{n,a})=1,\qquad \tau(B_{n,a})=0,\qquad
\pi_1(B_{n,a})\cong\mathbb Z_n.
\]

Dedekind 和恒等式给出

\[
\eta(n^2,na-1)
=
-\frac23\left(1-\frac1{n^2}\right).
\]

因此按复取向

\[
c_+
=
\frac2{n^2}-2-3\eta
=0,
\]

\[
c_-
=
\frac2{n^2}-2+3\eta
=
-4\left(1-\frac1{n^2}\right).
\]

反向取向交换 \(c_+\) 与 \(c_-\)。这部分完全正确。

这类 Milnor 纤维确有 ALE Ricci-flat Kähler 度量，可视为合适的
\(\mathbb Z_n\)-自由商；复取向下 \(W^+=0\)，且 \(\Ric=0\)，所以 \(P=0\)。

需要修改的是“零电荷有理球恰好是 T 型”这句话。当前材料只证明了

\[
\text{T 型 Milnor 纤维}\quad\Longrightarrow\quad c_+=0.
\]

`step55_orbifold_bubble_charges.py` 只对 \(n\le10\) 的 lens 参数进行枚举，而且脚本中标为 `rational_ball_lens` 的条目只是满足 \(\chi=1,\tau=0\) 的假想电荷表；它没有证明每个 \(q\) 实际界住有理球。反向结论需要一个完整的 Dedekind 方程分类，再与 lens-space 有理球 filling 的拓扑分类结合。

---

## 6. Theorem 55.5

这一部分整体上是 Step 55 最牢固的结果。

### 6.1 基本群与度数一

令 \(A=\pi_1(V^\circ)\)，\(H=\pi_1(L)=\mathbb Z_{n^2}\)。由于

\[
H\longrightarrow\pi_1(B_{n,a})=\mathbb Z_n
\]

满射，而 \(H\) 在无挠群 \(\Gamma\) 中像为平凡群，

\[
\pi_1(M)
=
A*_H\mathbb Z_n
=
A/\langle\!\langle H\rangle\!\rangle
=
\Gamma.
\]

resolution plumbing \(C\) 单连通，所以

\[
\pi_1(Y)
=
A*_H1
=
A/\langle\!\langle H\rangle\!\rangle
=
\Gamma.
\]

\(M\to X\) 与 \(Y\to X\) 在 \(V^\circ\) 上来自同一个 classifying map，并分别在 \(B\) 和 \(C\) 上零伦，故都经
\(V^\circ/L\) 分解；度数相同，等于一。

### 6.2 核格

度数一映射给出正交分解

\[
H_2(Y)/{\rm tors}
=
c^!H_2(X)\oplus K,
\qquad
K=\ker c_*.
\]

两侧闭定向四流形的自由交叉格均为 unimodular，且 \(c_*c^!=1\)，所以 \(K\) unimodular。

由 rational blow-up，

\[
b_2(Y)=b_2(M)+r=b_2(X)+1+r,
\]

\[
\tau(Y)=\tau(M)-r=\tau(X)-1-r.
\]

故 \(K\) 为秩 \(r+1\) 的负定 unimodular 格。每个 plumbing 球映到 \(X=K(\Gamma,1)\) 后零伦，因此 \(C_{n,a}\subset K\)。

当 \(r+1\le7\) 时不存在该秩的偶 unimodular 定格，低秩奇 unimodular 定格同构于 \(-I_{r+1}\)。这一点正确。

### 6.3 原始性

配对 \((Y,V^\circ)\) 的长正合列给出

\[
\operatorname{coker}\bigl(K\to C^*\bigr)
\hookrightarrow H_1(V^\circ)
\longrightarrow H_1(Y)\longrightarrow0.
\]

记该 cokernel 为 \(G_c\)，阶为 \(o\)。它是 \(H_1(L)=\mathbb Z_{n^2}\) 在 \(H_1(V^\circ)\) 中的像，所以 \(o\mid n^2\)。

另一方面，

\[
H_1(M)
=
\frac{H_1(V^\circ)\oplus\mathbb Z_n}
{\operatorname{im}H_1(L)}.
\]

消去 \(\mathbb Z_n\) 后得到

\[
\frac{|\operatorname{Tor}H_1(M)|}
{|\operatorname{Tor}H_1(Y)|}
=
\gcd(o,n).
\]

由于 \(\pi_1(M)\cong\pi_1(Y)\cong\Gamma\)，两边的 \(H_1\) 同构，故

\[
\gcd(o,n)=1.
\]

再由 \(o\mid n^2\)，得到 \(o=1\)。因此

\[
K\longrightarrow C^*
\]

满射，即 \(C\subset K\) 是原始嵌入。这一论证正确。

### 6.4 判别形式与模平方条件

T-chain 的负定矩阵为 \(G_C\)。若用第一颗球的对偶类作为判别群生成元，则

\[
A_C\cong\mathbb Z_{n^2},
\qquad
b_C=
\left\langle\frac{1-na}{n^2}\right\rangle
\quad\text{in }\mathbb Q/\mathbb Z.
\]

例如 \(n=3,a=1\)，链为 \([5,2]\)，

\[
G_C=
\begin{pmatrix}
-5&1\\
1&-2
\end{pmatrix},
\qquad
(G_C^{-1})_{11}=-\frac29,
\]

而 \(1-na=-2\equiv7\pmod9\)，完全吻合。

原始嵌入进 unimodular \(K\) 后，正交补为

\[
C^\perp=\langle -n^2\rangle.
\]

其判别形式为 \(\langle-1/n^2\rangle\)。构造 unimodular overlattice 需要 \(A_C\) 与 \(A_{C^\perp}\) 之间的 anti-isometry，因此

\[
b_C\cong -b_{C^\perp}
=
\left\langle\frac1{n^2}\right\rangle.
\]

故条件是

\[
1-na\equiv u^2\pmod{n^2}
\]

对某个单位 \(u\) 成立。文中的符号是正确的；若误用相反符号，\(n=2\) 会错误地允许
\(\langle-4\rangle\subset-I_2\)。

数论等价也正确：

\[
1-na\text{ 是模 }n^2\text{ 的单位平方}
\iff
n\text{ 为奇数，或 }8\mid n.
\]

奇素数部分由平方映射在 \(1+p\mathbb Z_p\) 上的 Hensel 提升得到。二进部分中：

- \(v_2(n)=1\)：右侧模 \(4\) 为 \(3\)；
- \(v_2(n)=2\)：右侧模 \(8\) 为 \(5\)；
- \(v_2(n)\ge3\)：右侧模 \(8\) 为 \(1\)，因而是所有更高 \(2\)-幂模数下的奇单位平方。

### 6.5 计算文件的一处文字修正

`step55_Tchain_embeddings.py` 在找到 \(4000\) 个嵌入后停止。数据中 \(n=7,a=6\) 恰好显示

```json
"n_embeddings_found": 4000
```

所以“对所有 \(n\le7\) 穷尽搜索”并不准确。该截断不影响存在性：它已经找到原始嵌入；也不影响 \(n=2,4,6\) 的不允许结果，因为这些运行没有触及截断值。更准确的表述是：

> 对 \(n\le7\) 的所有情形都获得了与理论一致的存在或不存在结果；其中 \(n=7,a=6\) 的嵌入总数未穷尽。

---

## 7. \(n=3\)、\([5,2]\) 例子

格论部分正确。取

\[
v_1=2E_1+E_2,\qquad
v_2=-E_2-E_3.
\]

在 \(-I_3\) 中，

\[
v_1^2=-5,\qquad v_2^2=-2,\qquad v_1\cdot v_2=1.
\]

其 \(2\times2\) 最大子式的最大公因数为 \(1\)，所以嵌入原始；正交补由

\[
w=E_1-2E_2+2E_3,\qquad w^2=-9
\]

生成。

文中后面写成 \(E_2+E_3\) 时，交数是

\[
(2E_1+E_2)\cdot(E_2+E_3)=-1.
\]

把第二个球反向定向，即使用 \(-E_2-E_3\)，就恢复 plumbing 约定中的 \(+1\)。底层无向嵌入球没有问题。

\(2E_1+E_2\) 可由第一份 \(\overline{\mathbb{CP}}^2\) 中的 conic 与第二份中的 line 作连通和得到；第二个球可由第二、第三份中的 line 作管接得到。该光滑球配置是可信且与格计算相符的。

但 rational blowdown 后的 \(Z\) 即使被证明单连通，也只能立即推出

\[
Z\ \text{homeomorphic to }\overline{\mathbb{CP}}^2,
\]

不能直接推出微分同胚。因而这个例子目前给出：

- 原始格嵌入；
- 可见的光滑 plumbing；
- 一个可能的 rational blowdown 模型；

尚未给出 \(Z\cong\overline{\mathbb{CP}}^2\) 的微分同胚证明，也未给出相应 orbifold \(P\)-临界度量。

---

## 8. Prop. 55.6

### 原证明中的缺失推理

“\(b^+\ge3\) 且 SW 非零，所以是一般型”本身不成立。K3 曲面和某些椭圆曲面已经说明 SW 非零并不强制 Kodaira 维数为 \(2\)。

即使已知 \(Y\) 是一般型，也不能据此推出：

- 极小化恰好吹下 \(r+1\) 个类；
- \(K=\ker c_*\) 全部由吹上类生成；
- T-chain 的每个球都属于极小化的 exceptional locus。

极小一般型曲面完全可能含有 \((-2)\)-曲线或 Wahl 链。因此当前 SW/极小模型段落不足以支撑计数。

### 可行的完整修复

Prop. 55.6 的结论可以用更强而直接的复几何论证得到。

1. \(\pi_1(Y)=\Gamma=\pi_1(X)\)，所以
   \[
   b_1(Y)=b_1(X)
   \]
   为偶数。

2. 紧复曲面 \(b_1\) 为偶数，因此 \(Y\) 是 Kähler 曲面。

3. 度数一 classifying map
   \[
   c:Y\to X
   \]
   可取调和代表。目标 \(X\) 是具有强负曲率的复双曲曲面。

4. 度数非零保证调和映射某处实秩为 \(4\)。Siu 刚性于是给出：该映射为全纯或反全纯。

5. 度数一的全纯或反全纯映射是双有理映射。于是 \(Y\) 由 \(X\) 经点吹上得到。

6. 因
   \[
   b_2(Y)-b_2(X)=r+1,
   \]
   总吹上次数恰为 \(r+1\)。

7. \(X\) 不含有理曲线，所以 T-chain 中每个 \(\mathbb{CP}^1\) 都被映到一点，因而属于该双有理映射的 exceptional locus。

此时文中的计数严格成立。令 \(N=r+1\) 为吹上次数。每个新 exceptional 曲线初始自交数为 \(-1\)；以后每个吹上中心至多落在两个已有 exceptional 分支上，因此

\[
\sum_{j=1}^{N}(-D_j^2)
\le N+2(N-1)=3r+1.
\]

T-chain 自身有

\[
\sum_{i=1}^rb_i=3r+1.
\]

还剩至少一个 exceptional 分支，其 \(-D^2\ge1\)，故总和至少为

\[
3r+2,
\]

矛盾。

所以 Prop. 55.6 的结论可保留，但证明应换成“Kähler性 + Siu 刚性 + 双有理分解 + 吹上计数”。SW 在这里不是必要输入。

---

## 9. Lemma 55.8 与 collapse 讨论

### Lemma 55.8

若 \(c\circ f:\Sigma\to X=K(\Gamma,1)\) 的基本群像为循环群，由于 \(\Gamma\) 无挠，该像为平凡群或 \(\mathbb Z\)。相应映射在同伦意义下经

\[
K(\mathbb Z,1)=S^1
\]

分解，所以

\[
(c\circ f)_*[\Sigma]=0.
\]

因此

\[
f_*[\Sigma]\in\ker c_*=\operatorname{span}\{E_i\}.
\]

对一般区域 \(C\)，只要 \(\pi_1(C)\) 在 \(\Gamma\) 中的像是循环群，同一 classifying-space 论证说明

\[
H_2(C)\longrightarrow H_2(X)
\]

为零。Lemma 55.8 正确。

自由 \(S^1\)-作用时，商空间是可定向三流形，且

\[
TC\cong \pi^*TB\oplus\underline{\mathbb R}.
\]

可定向三流形可平行化，故 \(w_2(C)=0\)，从 \(C\) 推入 \(M\) 的二维类自交数为偶数。因此它不能承载 \(E^2=-1\)。这一部分也正确。

### \(\tau(C)=-1\) 的账本解释需要重写

拓扑上，若

\[
M=\Omega\cup C,\qquad \chi(C)=0,
\]

则由 Euler 数和 Novikov 可加性，

\[
T_+^{\rm top}(\Omega)
=
T_+(M)-3\tau(C).
\]

若 \(\tau(C)=-1\)，确有

\[
T_+^{\rm top}(\Omega)=A+2.
\]

但这个纯拓扑量不能直接代入带分割三流形的 \(P\)-公式。APS 表达中还有端截面的 \(\eta\)-项和 Gauss–Bonnet 端部项。对 \(\Omega\) 与 \(C\)，这些项相反并在总和中抵消。

若 \(C\) 在全曲率一致有界下体积塌缩，则

\[
\int_C|\Ric^\circ|^2\to0,\qquad
\int_C|W^+|^2\to0,\qquad
\int_Cs^2\to0.
\]

因此 \(C\) 的 APS 有效拓扑项也必须趋于零；这意味着端截面谱项会抵消由 \(\tau(C)=-1\) 产生的 \(3\) 个单位。于是不能从

\[
T_+^{\rm top}(\Omega)=A+2
\]

单独推出

\[
C_+(\Omega)\ge A+2
\]

作为无端部修正的积分不等式。

正确的科学内容是：

- 若确有一个携带奇自交类的 \(F\)-collapse 区域，则该区域自身的 \(P\)-能量可以趋于零；
- \(\tau(C)=-1\) 所产生的拓扑变化必须由端截面的 \(\eta\)-项和 Chern–Simons 型项补偿；
- 是否可实现这种拓扑、谱项和 thick-part 几何的共同匹配，仍未解决。

所以“collapse 可以零能量吸收 \(E\)”目前是一个条件性机制，不是由 \(\chi(C)=0,\tau(C)=-1\) 两个等式已经推出的构造。

---

## 10. Theorem 55.7

由 Lemma 55.1 真正推出的结构是：

1. 所有端群平凡；或
2. 恰有一个 bubble 区域满足 \(b_2=1\)，其余非平凡端群区域均为有理同调球；或
3. 所有非平凡端群区域均为有理同调球。

这个按有理 \(b_2\) 的三分成立。

文中更细的版本尚不能从已有结果推出，原因如下。

### 10.1 rank-one 枚举不完整

Prop. 55.3 没有处理：

- 非单连通的 \(b_2=1\) 区域；
- 一般自由有限 \(SO(4)\) 端群；
- 循环端或 \(D_5,D_9\) 端的实际 filling 与 ALE \(P\)-临界度量存在性。

因此不能把 \((m,\Gamma)\) 缩减为当前脚本中的全部可能项。

### 10.2 rational-ball 枚举不完整

`step55_orbifold_bubble_charges.py` 的 rational-ball 部分只到 \(m\le10\)，并且枚举的是假定 \(\chi=1,\tau=0\) 后的 lens 电荷，不是实际有理球 filling 的完整拓扑分类。非循环 spherical space-form 端也没有进入脚本。

### 10.3 “bulk 非 Kähler”只对零电荷 T 型已得到

Prop. 55.6 经上述 Siu 修复后，可以排除复 orbifold 的零电荷 T 型 bulk。它没有处理：

- rank-one 的 \(mE\) 情形；
- \(D_5,D_9,E_8\) 情形；
- 非 T 型有理球；
- 反取向 T 型有理球。

因此 Theorem 55.7 中“(B)、(C) 的 bulk 都是非 Kähler”应改为：

> 零电荷、复取向的 T 型通道之 bulk 不能是具有该复商奇点结构的复 orbifold。

### 10.4 \(P=0\) bubble 时的等式还需要重组估计

若所有 bubble 都 Ricci-flat，形式上希望得到

\[
p_*(M)=\alpha_{\rm orb}(V)=P(V,g_0).
\]

要严格推出这一点，还需证明：任意接近 \(\alpha_{\rm orb}(V)\) 的 orbifold 度量都能与缩放后的 ALE bubble 重组为 \(M\) 上的光滑度量，且过渡区的 \(P\)-误差趋于零。仅有 \(\mathrm H_{\rm lsc}\) 给出一个方向，不能替代这一重组估计。

---

## 最终评价

Step 55 的核心技术成果是可靠的：

- 两取向 ALE 电荷；
- orbifold/bubble 账本；
- 度数一把 bubble 格压入 \(\mathbb ZE\)；
- T 型 rational ball 的零电荷；
- 原始嵌入与
  \[
  1-na\equiv u^2\pmod{n^2}
  \iff n\text{ 奇或 }8\mid n
  \]
  的完整格论；
- \(n=2\) 被排除而 \(n=3\) 首次格论允许。

文稿应把更强的总体结论改成以下精确形式：

1. 当前电荷表给出必要的能量与链接形式约束，不是全部 ALE bubble 的存在分类。
2. Prop. 55.3 应显式加入“\(N\) 单连通，端群为循环或纯 ADE”。
3. Prop. 55.4 保留 T 型 \(\Rightarrow\) 零电荷，删除尚未证明的反向等价。
4. Prop. 55.6 用 Siu 双有理论证替换 SW/一般型段落。
5. collapse 部分必须保留 APS 端截面项，不能只凭 \(\tau(C)=-1\) 推出 bulk 的积分基线。
6. Theorem 55.7 目前成立的是按 \(b_2=1\) 与 \(b_2=0\) 的结构分解；详细群枚举、普遍非 Kähler 性和零能量重组等式还需要额外定理。