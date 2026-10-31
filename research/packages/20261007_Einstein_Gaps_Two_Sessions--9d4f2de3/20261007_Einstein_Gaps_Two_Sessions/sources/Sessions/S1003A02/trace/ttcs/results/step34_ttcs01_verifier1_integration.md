# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the symmetry-free chiral link-charge theorem and its applications in Step 33. Re-derive all signs and normalizations from the stated Gauss–Bonnet and APS conventions. Check especially: (i) Q_±=2E∓3H and the annular orientation; (ii) thin disk-bundle charge for self-intersection n, including tau(D(n)) and the (-1)-sphere values (1,7); (iii) round S^3/Gamma charge and exact agreement with Lemma Q/Q' including the sign of eta; (iv) the Taub–NUT adiabatic derivation and whether E=O(R^-2) is justified; (v) G1, G2, and G3, including topology, quantifiers, multi-class counting, and exactly which bubble-tree degenerations G3 excludes for the certified ball-quotient cell. Identify and repair any statement stronger than the formulas prove.

## Integrated Scientific Memo

# Step 33 核验结论与修订版陈述

## 1. 手性特征恒等式：符号和归一化正确

由
\[
\chi(\Omega)=\int_\Omega e+\mathcal E,\qquad
\int_\Omega L=\tau(\Omega)+\mathcal H
\]
得到
\[
2\chi\pm3\tau
=\int_\Omega(2e\pm3L)+2\mathcal E\mp3\mathcal H.
\]
而
\[
2e\pm3L
=\frac1{4\pi^2}\left(
2|W^\pm|^2-\frac12|\Ric^\circ|^2+\frac{s^2}{24}
\right).
\]
故
\[
\boxed{
\widehat P(\Omega)
=\frac1{2\pi^2}\int_\Omega|W^\pm|^2
+\frac1{96\pi^2}\int_\Omega s^2
-(2\chi\pm3\tau)(\Omega)
+\mathcal Q_\pm(\partial\Omega)
}
\]
且
\[
\boxed{\mathcal Q_\pm=2\mathcal E\mp3\mathcal H.}
\]
因此 Step 33 的主恒等式、手性配对及所有系数均正确。

若 \(C\cong Y\times I\)，把两端荷都定义为各自所包围区域的外边界荷，则 \(Y_{\rm in}\) 作为 \(C\) 的边界具有反向定向，所以
\[
\mathcal Q_\pm(\partial C)
=\mathcal Q_\pm(Y_{\rm out})-\mathcal Q_\pm(Y_{\rm in}).
\]
又因 \(\chi(C)=\tau(C)=0\)，
\[
\widehat P(C)=
\mathcal Q_\pm(Y_{\rm out})-\mathcal Q_\pm(Y_{\rm in})
+\frac1{2\pi^2}\int_C|W^\pm|^2
+\frac1{96\pi^2}\int_Cs^2.
\]
内链接前的负号正确。若“两链接之间的区域”携带拓扑，则必须保留
\(-(2\chi\pm3\tau)(C)\)；不能无条件使用纯荷差公式。

同样，“bubble cost = outgoing charge − incoming charge”一般只是下界；仅当所选手性的 Weyl 项和标量曲率项消失时才为精确能量等式。

---

## 2. 薄圆盘丛及 \((-1)\)-球面

对 Euler 数为 \(n\neq0\) 的有向圆盘丛 \(D(n)\to\Sigma\)，
\[
\chi(D(n))=\chi(\Sigma),\qquad
\tau(D(n))=\operatorname{sgn}n,
\]
后者来自零截面生成的交叉型 \((n)\)。

在固定光滑环境度量中令管半径趋零，四维体积为 \(O(r^2)\)，曲率有界，因此
\[
\int_{D_r(n)}e,\ \int_{D_r(n)}L\longrightarrow0.
\]
于是
\[
\mathcal E\to\chi(\Sigma),\qquad
\mathcal H\to-\operatorname{sgn}n,
\]
故
\[
\boxed{
\mathcal Q_+\to2\chi(\Sigma)+3\operatorname{sgn}n,\qquad
\mathcal Q_-\to2\chi(\Sigma)-3\operatorname{sgn}n.
}
\]
对 \(n=-1,\Sigma=S^2\)，
\[
\boxed{(\mathcal Q_+,\mathcal Q_-)=(1,7).}
\]
Step 33 此处完全正确，且确实不依赖 Bianchi–IX 对称性。

需补充限定：这是固定光滑度量中的薄管极限。对曲率在零截面附近集中的退化序列，必须令管半径相对于曲率尺度足够小，才能沿序列得到 \((1,7)\)。

---

## 3. 圆空间形式、APS \(\eta\) 符号及 Lemma Q/Q′

对于作为 ALE 截断区域外边界的 \(S^3/\Gamma\)，在平锥领圈或 ALE 极限中
\[
\mathcal E\to\frac1{|\Gamma|},\qquad
\mathcal H\to\eta_\Gamma,
\]
其中 \(\eta_\Gamma\) 必须采用该外向定向和
\[
\int L=\tau+\mathcal H
\]
的约定。因此
\[
\boxed{
\mathcal Q_\pm=\frac2{|\Gamma|}\mp3\eta_\Gamma.
}
\]

对完整光滑标量平坦 ALE 空间 \(N\)，两种手性给出
\[
\widehat P(N)\ge
\frac2{|\Gamma|}-2\chi(N)
\mp3\bigl(\tau(N)+\eta_\Gamma\bigr).
\]
取较大者：
\[
\boxed{
\widehat P(N)\ge
\frac2{|\Gamma|}-2\chi(N)
+3\bigl|\tau(N)+\eta_\Gamma\bigr|.
}
\]
这与 Step 20 Lemma Q 精确一致；特别是绝对值内必须是
\(\tau+\eta_\Gamma\)，而不是 \(\tau-\eta_\Gamma\)。

等价地，
\[
P(N)=2\int_N|W|^2
-16\pi^2\left(\chi(N)-\frac1{|\Gamma|}\right),
\]
且
\[
\int_N(|W^+|^2-|W^-|^2)
=12\pi^2(\tau+\eta_\Gamma).
\]
使用 \(\int(|W^+|^2+|W^-|^2)\ge
|\int(|W^+|^2-|W^-|^2)|\) 即得同一下界。

当 \(\Gamma=1\)，
\[
\chi=1+k-2\ell,\qquad \tau=-k
\]
给出
\[
\widehat P\ge k+4\ell.
\]
单 blow-up 的等号通道为 \(+\) 手性，要求 \(W^+=0\)，与 Burns 度量一致。

Lemma Q′ 也是同一公式的近欧氏 \(S^3\) 版本：若
\(\mathcal Q_+=2+O(\varepsilon)\)、\(\tau(U)=-1\)、\(\chi(U)=2\)，则
\[
\widehat P(U)\ge1-O(\varepsilon).
\]

### 必须修订的措辞

“圆 \(S^3/\Gamma\) 的荷”不能只由三维诱导度量的内蕴圆度决定。荷还依赖领圈的第二基本形式和局部 transgression。正确表述应为：

* 精确平锥领圈：上述值精确成立；
* ALE 截面趋于平锥：上述值作为极限成立；
* 仅知道三维边界是圆的、但径向 jet 任意：不能推出该荷。

若区域内部含真正的 orbifold 奇点，还必须加入 orbifold 特征公式的奇点修正；Step 33 的光滑区域公式不能直接使用。

---

## 4. Taub–NUT 绝热极限

取 blow-up 定向，使 Taub–NUT 满足
\[
\Ric=0,\qquad W^-=0,\qquad \chi=1,\quad\tau=0.
\]
ALF 大半径截面上，两条水平尺度为 \(O(R)\)，Hopf 纤维尺度趋于常数。其主曲率和三维截面曲率具有
\[
\kappa_f=O(R^{-2}),\qquad
\kappa_{b_i}=O(R^{-1}),
\]
\[
K_{b_1b_2}=O(R^{-2}),\qquad
K_{fb_i}=O(R^{-4}),
\qquad \operatorname{Area}(Y_R)=O(R^2).
\]

Euler transgression 中各项不是任意的 \(|A||\Rm_Y|\)，而是
\[
\kappa_iK_{jk}\quad(i,j,k\ \text{互异}),\qquad
\kappa_f\kappa_{b_1}\kappa_{b_2}.
\]
故主项
\[
\kappa_fK_{b_1b_2},\quad
\kappa_f\kappa_{b_1}\kappa_{b_2}
=O(R^{-4}),
\]
积分后
\[
\boxed{\mathcal E_R=O(R^{-2}).}
\]
因此 Step 33 的 \(O(R^{-2})\) 结论有充分依据；关键是反对称指标结构排除了较大的 \(\kappa_bK_{b_1b_2}\) 型项。即使只作粗略估计得到 \(o(1)\)，也足以计算极限荷，但精确的 \(O(R^{-2})\) 需要上述结构。

Gauss–Bonnet 给出
\[
1=\frac1{8\pi^2}\int_{\rm TN}|W^+|^2,
\]
故
\[
\int_{\rm TN}L
=\frac1{12\pi^2}\int|W^+|^2=\frac23.
\]
又 \(\tau=0\)，所以
\[
\mathcal H_R\to\frac23,
\qquad
\boxed{(\mathcal Q_+,\mathcal Q_-)\to(-2,2).}
\]

这与 Berger 数据
\[
3\mathcal H
=2(1-\lambda^2)^2+\lambda^2(U-V)^2
\]
一致：若 \(\lambda\to0\) 且归一化剪切 \(U-V\) 有界，则
\(3\mathcal H\to2\)。

### 两处必要修订

1. Step 33 所称
   \[
   \mathcal H=\frac23(1-\mathcal E)
   \]
   “对任意 controlled self-dual filling”成立，过强。对拓扑为球、\(\tau=0\)、\(W^-=0\) 的一般填充，实际为
   \[
   \boxed{
   \mathcal H-\frac23(1-\mathcal E)
   =
   \frac1{24\pi^2}\int|\Ric^\circ|^2
   -\frac1{288\pi^2}\int s^2.
   }
   \]
   因此原关系需要 Ricci-flat，或至少要求右端恰为零。对 Taub–NUT 本身成立。

2. “Hopf-adiabatic 荷为 \((-2,2)\)”必须指定 Hopf 手性。反转四维定向会使 \(\mathcal H\) 变号并交换两荷；相反 Hopf 手性的受控塌缩链接具有
   \[
   (\mathcal Q_+,\mathcal Q_-)=(2,-2).
   \]
   此外若 \(U-V\sim\lambda^{-1}\)，剪切项保留有限贡献，极限不再是 \((-2,2)\)。因此必须明确“blow-up 定向、Taub–NUT 手性、受控径向剪切”。

---

## 5. CH 球与体积重整

记 \(x=\sinh^4\tau\)。CH 球满足
\[
\frac1{2\pi^2}\int|W^+|^2=6x,\qquad
\frac1{96\pi^2}\int s^2=3x,\qquad
\chi=1,\quad\tau=0,\quad\widehat P=0.
\]
故
\[
\boxed{
(\mathcal Q_+,\mathcal Q_-)
=(2-9x,\ 2-3x).
}
\]
Step 33 正确。

当 \(s=-24\) 时，
\[
\frac1{96\pi^2}\int s^2=3\widehat V,\qquad
\widehat V=\frac{2\operatorname{Vol}}{\pi^2}.
\]
因此
\[
\mathfrak B_\pm=\mathcal Q_\pm+3\widehat V
\]
及从受控 Taub–NUT 手性塌缩端 \((-2,2)\) 开到 CH 球的两个下界
\[
\widehat P\ge4-9\sinh^4\tau+3\Delta\widehat V,
\]
\[
\widehat P\ge3(\Delta\widehat V-\sinh^4\tau)
\]
均正确。它们要求中间区域为产品拓扑、\(s\equiv-24\)，并使用实际受控塌缩荷；剪切失控时必须用真实 \(\mathcal Q_\pm\) 替换 \((-2,2)\)。

---

## 6. G1：拓扑和不等式正确

若
\[
D\cong
\left(
\#^{k_D}\overline{\mathbb{CP}}^{\,2}
\#^{\ell_D}(S^1\times S^3)
\right)\setminus B^4,
\]
则
\[
\chi(D)=1+k_D-2\ell_D,\qquad
\tau(D)=-k_D,
\]
所以
\[
2\chi(D)+3\tau(D)=2-k_D-4\ell_D.
\]
应用 \(+\) 手性公式：
\[
\boxed{
P(g)\ge P(g;D)\ge
8\pi^2\left[
k_D+4\ell_D-(2-\mathcal Q_+(\partial D))
\right].
}
\]
G1 的所有符号和系数均正确。

更一般地，对 \(\partial D\cong S^3\)，若 \(b_3=b_1\)，则
\[
2\chi+3\tau
=2-4b_1+5b_2^+-b_2^-,
\]
从而
\[
\widehat P(D)\ge
b_2^-+4b_1-5b_2^+-(2-\mathcal Q_+).
\]
所以 G1 实际只需 \(b_2^+=0,\ b_2^-=k_D,\ b_1=\ell_D\)，未必需要给定完整连通和微分同胚型。

---

## 7. G2：有限族结论正确，但量词必须补全

若 \(D_i\) 两两不交，且
\[
\mathcal Q_+(\partial D_i)\ge2-\varepsilon_i,
\]
则
\[
\boxed{
\widehat P(g)\ge
\sum_i(k_i+4\ell_i-\varepsilon_i).
}
\]
这是非负能量密度的可加性，正确。

序列版本应表述为：对每个 \(g_n\)，存在两两不交的 \(D_{i,n}\)，满足
\[
\sum_i k_{i,n}=k,\qquad
\sum_i\varepsilon_{i,n}\to0.
\]
此时才有
\[
\liminf_n\widehat P(g_n)\ge k.
\]
仅称“每个 exceptional class 都被某个近圆链接包住”不够；这些区域若相交或嵌套，不能直接相加。另一种充分条件是存在单个区域包住全部 \(k\) 个类。

“近圆近平”还须明确：

* \(D_i\) 位于平直模型链接的球侧；
* 链接为 \(S^3\)，而非 \(S^3/\Gamma\)；
* 至少有足以控制边界曲率与第二基本形式的 \(C^2\) collar 收敛。

Step 33 后文声称非塌缩链接的 \(C^1\) collar 收敛已足以控制 \(\mathcal H\)，依据不足。Euler 和 signature transgression 都涉及四维连接/曲率 jet；安全且与 G2 一致的条件是 \(C^2\) collar 收敛，或相应的高阶 Sobolev 控制。

### 多类计数

若这些不交区域共携带 \(K=\sum_i k_i\) 个类，每个非空区域有 \(k_i\ge1\)，且统一
\(\mathcal Q_+\ge2-\varepsilon\)，则区域数 \(m\le K\)，故
\[
\widehat P\ge K-m\varepsilon\ge K(1-\varepsilon),
\]
于是
\[
\boxed{
K\le
\left\lfloor\frac{\widehat P}{1-\varepsilon}\right\rfloor.
}
\]
该计数正确，但 \(K\) 是“两两不交的这些区域中所携带的类总数”，不是任意意义下所有可被某个链接包围的类数。

若 \(k\) 个认证单元只给出
\(\widehat P\lesssim kp_*\)，该计数并不说明所有 \(k\) 个类都不能圆分离；它只保证至少
\[
k-\left\lfloor\frac{kp_*+\delta}{1-\varepsilon}\right\rfloor
\]
个类不能属于这种不交圆分离族。要排除全部 \(k\) 类的圆分离，需要对其余未分离类另有正下界。

---

## 8. G3：正确的不等式与真正排除的 bubble-tree 退化

对 \(k=1\)，若
\[
D\cong\overline{\mathbb{CP}}^{\,2}\setminus B^4
\]
且生成元为所讨论的 exceptional class，则 G1 给出
\[
\widehat P(D)\ge \mathcal Q_+(\partial D)-1.
\]
因此
\[
\boxed{
\mathcal Q_+(\partial D)
\le1+\widehat P(D)
\le1+\widehat P(g).
}
\]
若 \(\widehat P(g)<1-\varepsilon\)，则确有
\[
\mathcal Q_+(\partial D)<2-\varepsilon.
\]
所以 Step 33 在严格能量假设下写出的严格结论正确；无该严格假设时基本关系应写作“\(\le\)”。

认证 ball-quotient 单元提供
\[
\alpha(X\#\overline{\mathbb{CP}}^2)\le p_*=0.995848<1.
\]
故任一趋向该上界以下下确界的序列，都不可能把 exceptional class 放在一个外边界满足
\(\mathcal Q_+\to2\) 的标准 blow-up 区域中。

### G3 确实排除

它排除的是：

> exceptional class 所在的整个子树，通过一个位于球侧、重标后 \(C^2\) 趋于欧氏平直 \(S^3\) collar 的外层链接，与 ball-quotient bulk 分离。

内部允许继续有多层 bubble；只要整个 exceptional 子树外面存在上述圆 \(S^3\) neck，便有
\(\mathcal Q_+\to2\)，从而强迫
\(\liminf\widehat P\ge1\)，与 \(p_*<1\) 冲突。

同一不等式也排除任何其他已知满足 \(\mathcal Q_+>1+\widehat P\) 的链接，例如：

* CH 球若
  \[
  2-9\sinh^4\tau>1+\widehat P;
  \]
* 在已固定相反 Hopf 手性且受控的情形，\(\mathcal Q_+=2\) 的 collapsed germ。

### G3 不排除

公式本身不排除：

1. 外链接为 \(S^3/\Gamma,\ \Gamma\ne1\) 的 orbifold bubble tree；
2. Taub-bolt/Taub–NUT 手性的 Hopf 塌缩链接，因其 \(\mathcal Q_+\approx-2\)；
3. 非圆、非塌缩且有明显 collar shear 的链接；
4. 任意满足 \(\mathcal Q_+\le1+\widehat P\) 的弯曲链接，包括大量 \(1<\mathcal Q_+<2\) 的情形；
5. 不携带 exceptional 同调的纯 bulk 曲率 bubbling；
6. \(D\) 同时含有 bulk 的 \(b_2^+>0\) 的分解；
7. 无法选择成两两不交标准 blow-up 区域的嵌套多类分解。

因此标题“near-minimizers … are not bubble trees”过强。应改为：

> **Subunit near-minimizers admit no Euclidean-round \(S^3\) separation of the exceptional subtree.**

同样，原文所称“exceptional topology only at curvature-scale links (or collapsed links with \(\mathcal Q_+<1\))”也未由 G1 证明。所得唯一普适约束是
\[
\mathcal Q_+\le1+\widehat P;
\]
在认证数值处仍允许
\[
\mathcal Q_+\le1.995848.
\]
所以不能把所有剩余退化强行归类为“曲率尺度”或“认证单元型”退化。

对于“每个 region \(D\) carrying the exceptional class”，量词也应收紧为：每个具有所用拓扑数据的标准负定 blow-up 区域，或更一般地满足 \(b_2^-=1,b_2^+=b_1=0\) 的区域。仅仅在同调中包含该类、但拓扑还含其他部分的任意区域，必须代入实际 \(\chi,\tau\)。

---

## 9. 建议直接替换的结论版

Step 33 的核心无对称性定理及模型计算成立：

\[
\mathcal Q_\pm=2\mathcal E\mp3\mathcal H,
\]
annulus 的内链接取负号；薄 \((-1)\)-球面的荷为 \((1,7)\)；ALE 端的荷为
\[
\frac2{|\Gamma|}\mp3\eta_\Gamma
\]
并产生 \(\tau+\eta_\Gamma\)；Taub–NUT 在指定 blow-up 定向和受控剪切下具有绝热荷 \((-2,2)\)；G1 的 \(k+4\ell\) 系数正确。

需要正式修订的是：

1. 圆空间形式荷要求平锥/ALE collar 控制，不由三维内蕴圆度单独决定。
2. 荷差一般是下界，不是完整能量等式。
3. \(\mathcal H=\frac23(1-\mathcal E)\) 只在相应 Ricci-flat 半共形平坦球填充中成立。
4. Hopf 绝热荷必须注明手性和剪切控制；反手性给 \((2,-2)\)。
5. G2 的序列推论要求两两不交区域，或单个区域包住全部类，并要求 \(C^2\) collar 级控制。
6. G3 只排除 exceptional 子树经欧氏圆 \(S^3\) germ 与 bulk 分离，以及其他明确具有过大 \(\mathcal Q_+\) 的链接；它不排除一般 bubble tree、orbifold neck、塌缩 neck、弯曲/sheared neck 或 bulk bubbling。