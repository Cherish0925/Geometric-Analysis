# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/data/berger_eta_charge.json"
  ]
}
```

## Task

Independently verify the symmetry-free chiral link-charge theorem and its applications in Step 33. Re-derive all signs and normalizations from the stated Gauss–Bonnet and APS conventions. Check especially: (i) Q_±=2E∓3H and the annular orientation; (ii) thin disk-bundle charge for self-intersection n, including tau(D(n)) and the (-1)-sphere values (1,7); (iii) round S^3/Gamma charge and exact agreement with Lemma Q/Q' including the sign of eta; (iv) the Taub–NUT adiabatic derivation and whether E=O(R^-2) is justified; (v) G1, G2, and G3, including topology, quantifiers, multi-class counting, and exactly which bubble-tree degenerations G3 excludes for the certified ball-quotient cell. Identify and repair any statement stronger than the formulas prove.

## Output

# 科学核验备忘录：Step 33 的无对称性手性链接荷

## 1. 主恒等式的符号与归一化

由约定
\[
\chi(\Omega)=\int_\Omega e+\mathcal E,\qquad
\int_\Omega L=\tau(\Omega)+\mathcal H
\]
可写成
\[
\tau(\Omega)=\int_\Omega L-\mathcal H.
\]
因此
\[
2\chi\pm3\tau
 =\int_\Omega(2e\pm3L)+2\mathcal E\mp3\mathcal H.
\]
另一方面，
\[
2e\pm3L
=\frac1{4\pi^2}
\left(2|W^\pm|^2-\frac12|\Ric^\circ|^2+\frac{s^2}{24}\right).
\]
于是
\[
2\chi\pm3\tau
=\frac1{2\pi^2}\int|W^\pm|^2
-\frac1{8\pi^2}\int|\Ric^\circ|^2
+\frac1{96\pi^2}\int s^2
+2\mathcal E\mp3\mathcal H.
\]
移项即得
\[
\boxed{
\widehat P(\Omega)
=\frac1{2\pi^2}\int_\Omega|W^\pm|^2
+\frac1{96\pi^2}\int_\Omega s^2
-(2\chi\pm3\tau)(\Omega)
+\mathcal Q_\pm
}
\]
以及
\[
\boxed{\mathcal Q_\pm=2\mathcal E\mp3\mathcal H.}
\]
所以 Step 33 中主公式的系数、手性和符号全部正确。

### 环域定向

设 \(C\cong Y\times[0,1]\)，并把 \(Y_{\rm in},Y_{\rm out}\) 的荷都定义成“作为其所包围区域的外向链接”时的值。作为 \(C\) 的定向链接，内侧出现为 \(-Y_{\rm in}\)，故
\[
\mathcal Q_\pm(\partial C)
=\mathcal Q_\pm(Y_{\rm out})-\mathcal Q_\pm(Y_{\rm in}).
\]
又因产品环域满足 \(\chi(C)=\tau(C)=0\)，
\[
\widehat P(C)
=\mathcal Q_\pm(Y_{\rm out})-\mathcal Q_\pm(Y_{\rm in})
+\frac1{2\pi^2}\int_C|W^\pm|^2
+\frac1{96\pi^2}\int_Cs^2.
\]
因此
\[
\widehat P(C)\ge
\max_{\pm}\{\mathcal Q_\pm(Y_{\rm out})-\mathcal Q_\pm(Y_{\rm in})\}.
\]
内侧荷前的减号正确。对于一般四维余维零的 cobordism，仍须保留其 \(2\chi\pm3\tau\) 项；上述简式依赖于产品环域拓扑。

这里“荷差是成本”应解释为普适下界。精确等式还含非零的 \(W^\pm\) 与 \(s\) 能量；只有相应手性 Weyl 项与标量曲率项消失时，成本才恰等于荷差。

---

## 2. 薄圆盘丛链接

令 \(D(n)\to\Sigma\) 为 Euler 数 \(n\ne0\) 的有向实二维圆盘丛。它形变收缩到 \(\Sigma\)，故
\[
\chi(D(n))=\chi(\Sigma).
\]
其相对交叉配对由零截面的自交数 \(n\) 给出，因而
\[
\tau(D(n))=\operatorname{sgn}n.
\]

在光滑四维度量中取半径趋于零的管状邻域。环境曲率有界，而四维体积为 \(O(r^2)\)，所以
\[
\int_{D_r(n)} e\longrightarrow0,\qquad
\int_{D_r(n)} L\longrightarrow0.
\]
由两条特征公式，
\[
\mathcal E\longrightarrow\chi(\Sigma),\qquad
\mathcal H\longrightarrow-\operatorname{sgn}n.
\]
从而
\[
\boxed{
\mathcal Q_+=2\chi(\Sigma)+3\operatorname{sgn}n,\qquad
\mathcal Q_-=2\chi(\Sigma)-3\operatorname{sgn}n.
}
\]
即 Step 33 写成的
\[
\mathcal Q_\pm=2\chi(\Sigma)\pm3\operatorname{sgn}n
\]
完全正确。

对自交数 \(-1\) 的球面，\(\chi(S^2)=2\)，所以
\[
(\mathcal Q_+,\mathcal Q_-)
=(4-3,4+3)=(1,7).
\]
该计算只用到管状邻域的光滑性和零截面的自交配对，不依赖 Bianchi–IX 对称性。

---

## 3. 圆球空间形式与 Lemma Q/Q′

设 \(Y=S^3/\Gamma\) 取 ALE 截断区域的外向定向。在精确平锥领圈中，或沿 ALE 截面趋向无穷远时，
\[
\mathcal E\longrightarrow\frac1{|\Gamma|},
\qquad
\mathcal H\longrightarrow\eta_\Gamma,
\]
其中 \(\eta_\Gamma\) 必须使用同一个外向定向及 Step 33 的 APS 归一化
\[
\int L=\tau+\mathcal H.
\]
于是
\[
\boxed{
\mathcal Q_\pm
=\frac2{|\Gamma|}\mp3\eta_\Gamma.
}
\]

只给定链接的内蕴圆度并不足以确定该值，因为 \(\mathcal E\) 与 \(\mathcal H\) 还含领圈及第二基本形式信息。正确表述是：

* 精确平锥领圈时为精确值；
* ALE 领圈趋于平锥时为极限值；
* 若仅有一个圆的三维诱导度量而径向导数任意，则不能据此写成上述数值。

对完备光滑标量平坦 ALE 空间 \(N\)，主恒等式分别给出
\[
\widehat P(N)\ge
\frac2{|\Gamma|}-2\chi(N)-3\bigl(\tau(N)+\eta_\Gamma\bigr),
\]
\[
\widehat P(N)\ge
\frac2{|\Gamma|}-2\chi(N)+3\bigl(\tau(N)+\eta_\Gamma\bigr).
\]
取较大者，
\[
\boxed{
\widehat P(N)\ge
\frac2{|\Gamma|}-2\chi(N)
+3\bigl|\tau(N)+\eta_\Gamma\bigr|.
}
\]
这确认了 \(\eta\) 在绝对值内部以 \(\tau+\eta\) 出现，而不是 \(\tau-\eta\)。

同一结果也可由 Lemma Q 的形式直接得到。标量平坦 Gauss–Bonnet 公式给出
\[
P(N)
=2\int_N|W|^2
-16\pi^2\left(\chi(N)-\frac1{|\Gamma|}\right),
\]
而 APS 公式给出
\[
\int_N(|W^+|^2-|W^-|^2)
=12\pi^2\bigl(\tau(N)+\eta_\Gamma\bigr).
\]
利用
\[
\int(|W^+|^2+|W^-|^2)
\ge
\left|\int(|W^+|^2-|W^-|^2)\right|
\]
正好得到
\[
P(N)\ge8\pi^2
\left[
3|\tau+\eta_\Gamma|-2\chi+\frac2{|\Gamma|}
\right].
\]
所以 Step 20 的 Lemma Q 与 Step 33 完全一致。

当 \(\Gamma=1\)、\(\eta(S^3)=0\)，且
\[
\chi(N)=1+k-2\ell,\qquad \tau(N)=-k,
\]
上述下界成为
\[
\widehat P(N)\ge k+4\ell.
\]
对于单次 blow-up，等号通道是 \(+\) 手性，等号要求 \(W^+\equiv0\)，与 Burns 度量吻合。

对于 Lemma Q′，近欧氏 \(S^3\) 领圈给出
\[
\mathcal Q_+=2+O(\varepsilon).
\]
若 \(\tau(U)=-1\)、\(\chi(U)\le2\)，则
\[
\widehat P(U)
\ge
\mathcal Q_+-(2\chi+3\tau)
\ge2-(2\chi-3)-C\varepsilon
\ge1-C\varepsilon.
\]
这正是 \(P(U)\ge8\pi^2-C\varepsilon\)。其符号和常数与 Lemma Q′ 相同。

若截断区域本身含真正的 orbifold 奇点，则还需要 orbifold 特征公式中的奇点修正；Step 33 的光滑 \(\Omega\) 公式不能直接忽略这些项。对内部光滑、仅无穷远模型为 \(S^3/\Gamma\) 的 ALE bubble 则没有此问题。

---

## 4. Taub–NUT 的绝热链接荷

取 Taub–NUT 截断区域 \(N_R\cong B^4\)，使用 Step 33 指定的定向
\[
W^-=0,\qquad \Ric=0,\qquad \chi(N_R)=1,\quad\tau(N_R)=0.
\]

在 ALF 大半径处，两个水平尺度为 \(a(R)\asymp R\)，Hopf 纤维尺度趋于常数。其主曲率和链接截面曲率满足
\[
\kappa_f=O(R^{-2}),\qquad
\kappa_{b_1},\kappa_{b_2}=O(R^{-1}),
\]
\[
K_{b_1b_2}=O(R^{-2}),\qquad
K_{fb_i}=O(R^{-4}),
\]
而三维体积为 \(O(R^2)\)。

四维 Euler transgression 的每一项在主方向标架中均为
\[
\kappa_iK_{jk}
\quad\text{或}\quad
\kappa_f\kappa_{b_1}\kappa_{b_2},
\]
其中 \(i,j,k\) 互不相同。因此可能的最大项是
\[
\kappa_fK_{b_1b_2}=O(R^{-4}),
\qquad
\kappa_f\kappa_{b_1}\kappa_{b_2}=O(R^{-4}),
\]
积分后为 \(O(R^{-2})\)；其余项积分后更小。故
\[
\boxed{\mathcal E_R=O(R^{-2})\to0.}
\]
Step 33 对该衰减的论证是充分的；关键是 Euler transgression 的指标反对称性排除了 \(\kappa_bK_{b_1b_2}\) 这类较大的组合。

由 Gauss–Bonnet，
\[
1
=\frac1{8\pi^2}\int_{N_R}|W^+|^2+\mathcal E_R,
\]
所以
\[
\frac1{8\pi^2}\int_{\rm TN}|W^+|^2=1.
\]
再由 APS 公式，
\[
\mathcal H_R
=\int_{N_R}L-\tau(N_R)
=\frac1{12\pi^2}\int_{N_R}|W^+|^2
\longrightarrow\frac23.
\]
从而
\[
\boxed{
(\mathcal Q_+,\mathcal Q_-)
=(2\mathcal E-3\mathcal H,\;2\mathcal E+3\mathcal H)
\longrightarrow(-2,2).
}
\]
`berger_eta_charge.json` 中
\[
3\mathcal H
=2(1-\lambda^2)^2+\lambda^2(U-V)^2
\]
给出同样的定向：当 \(\lambda\to0\) 且 \(U-V=O(1)\) 时，\(3\mathcal H\to2\)，故荷为 \((-2,2)\)。

有一处需要收紧。关系
\[
\mathcal H=\frac23(1-\mathcal E)
\]
并不由普通的 \(W^-=0\) 单独推出。对拓扑为球、\(\tau=0\)、\(W^-=0\) 的一般填充，精确关系是
\[
\mathcal H-\frac23(1-\mathcal E)
=
\frac1{24\pi^2}\int|\Ric^\circ|^2
-\frac1{288\pi^2}\int s^2.
\]
所以 Step 33 所写“任意 controlled self-dual filling”只有在“self-dual”同时表示 Ricci-flat gravitational instanton，或另行保证右侧为零时才成立。对 Taub–NUT 本身当然成立。

此外，\((-2,2)\) 要求有界归一化径向剪切。若
\[
U-V\sim\lambda^{-1},
\]
则 \(\lambda^2(U-V)^2\) 保留非零贡献，绝热荷不再是 \((-2,2)\)。

---

## 5. CH 球及体积重整

令 \(x=\sinh^4\tau\)。CH 球满足
\[
\frac1{2\pi^2}\int|W^+|^2=6x,\qquad
\frac1{96\pi^2}\int s^2=3x,\qquad
\chi=1,\quad\tau=0,\quad P=0.
\]
因此
\[
\boxed{
(\mathcal Q_+,\mathcal Q_-)
=(2-9x,\;2-3x).
}
\]
这与 Step 33 一致。

当 \(s=-24\) 时，
\[
\frac1{96\pi^2}\int s^2
=3\widehat V,\qquad
\widehat V=\frac{2\operatorname{Vol}}{\pi^2},
\]
故 \(\mathfrak B_\pm=\mathcal Q_\pm+3\widehat V\) 的定义正确。由受控 Hopf 塌缩链接 \((-2,2)\) 开到 CH 半径 \(\tau\) 的环域满足
\[
\widehat P\ge4-9\sinh^4\tau+3\Delta\widehat V,
\]
\[
\widehat P\ge3(\Delta\widehat V-\sinh^4\tau).
\]
这些公式要求环域内 \(s=-24\)，且内侧确实是有界剪切的 Hopf 绝热截面。若径向剪切未受控，必须用实际的 \(\mathcal Q_\pm\) 代替 \((-2,2)\)。

---

## 6. G1 的拓扑和公式

设
\[
D\cong
\left(
\#^{k_D}\overline{\mathbb{CP}}^{\,2}
\#^{\ell_D}(S^1\times S^3)
\right)\setminus B^4.
\]
闭四维连通和的 Euler 数为
\[
2+k_D-2\ell_D,
\]
去掉一个开四球后
\[
\chi(D)=1+k_D-2\ell_D.
\]
每个 \(\overline{\mathbb{CP}}^{\,2}\) 贡献 \(-1\) 到 signature，而 \(S^1\times S^3\) 贡献零，因此
\[
\tau(D)=-k_D.
\]
于是
\[
2\chi(D)+3\tau(D)
=2-k_D-4\ell_D.
\]
应用 \(+\) 手性公式，
\[
\widehat P(D)\ge
\mathcal Q_+(\partial D)-(2-k_D-4\ell_D),
\]
即
\[
\boxed{
P(g)\ge P(g;D)\ge
8\pi^2
\left[
k_D+4\ell_D-(2-\mathcal Q_+(\partial D))
\right].
}
\]
G1 的拓扑系数和所有符号正确。

---

## 7. G2 的精确量词

对两两不交的 \(D_i\)，非负密度的可加性给出
\[
\widehat P(g)
\ge
\sum_i\widehat P(D_i)
\ge
\sum_i
\left(k_i+4\ell_i-\varepsilon_i\right)
\]
只要
\[
\mathcal Q_+(\partial D_i)\ge2-\varepsilon_i.
\]
所以 G2 的有限族版本正确。

序列版应明确写成：对每个 \(g_n\)，存在两两不交的 \(D_{i,n}\)，并且
\[
\sum_i k_{i,n}=k,\qquad
\sum_i\varepsilon_{i,n}\longrightarrow0.
\]
这时
\[
\liminf_n\widehat P(g_n)\ge k.
\]
“每个 exceptional class 都有某个近圆链接”若没有两两不交性，不能直接把局部积分相加；相交或嵌套区域会重复计算同一能量。一个单独的区域包住全部 \(k\) 个类则没有此问题，因为可直接取 \(k_D=k\)。

若统一使用 \(0\le\varepsilon<1\)，设这些不交区域共携带
\[
K=\sum_i k_i
\]
个独立 exceptional classes，且每个 \(k_i\ge1\)，则
\[
\widehat P
\ge K+4\sum_i\ell_i-m\varepsilon
\ge K-m\varepsilon
\ge K(1-\varepsilon),
\]
因为区域数 \(m\le K\)。因此
\[
\boxed{
K\le
\left\lfloor\frac{\widehat P}{1-\varepsilon}\right\rfloor .
}
\]
Step 33 的多类计数是正确的，但“them”应明确指这些不交区域中所携带的类总数 \(K\)。

---

## 8. G3 真正排除的退化方式

对
\[
M=X\#\overline{\mathbb{CP}}^{\,2}
\]
以及任意嵌入区域
\[
D\cong\overline{\mathbb{CP}}^{\,2}\setminus B^4
\]
且其生成元对应所讨论的 exceptional class，G1 给出
\[
\widehat P(g)\ge\mathcal Q_+(\partial D)-1.
\]
故
\[
\boxed{
\mathcal Q_+(\partial D)\le1+\widehat P(g).
}
\]
若 \(\widehat P(g)<1-\varepsilon\)，便有
\[
\mathcal Q_+(\partial D)<2-\varepsilon.
\]
该任意量词适用于上述标准 blow-up 区域，不能自动扩展到任意“同调中含有该类”的子区域；若其拓扑不同，必须重新代入实际的 \(\chi,\tau\)。

由认证单元
\[
\alpha\bigl(X\#\overline{\mathbb{CP}}^{\,2}\bigr)
\le p_*=0.995848<1.
\]
若 \(g_n\) 是趋向该下确界的序列，并取相应标准区域 \(D_n\)，则
\[
\limsup_n\mathcal Q_+(\partial D_n)
\le1+\alpha
\le1+p_*
=1.995848<2.
\]
因此下列几何图景确实被排除：

* exceptional class 完全位于一个由圆 \(S^3\) 欧氏领圈同主体分开的 ALE 子树中；
* 更一般地，外层 \(S^3\) 领圈在重标后以 \(C^2\) 收敛到平直圆环，且其内区域拓扑为 \(\overline{\mathbb{CP}}^{\,2}\setminus B^4\)。

因为这种领圈满足
\[
\mathcal Q_+\longrightarrow2,
\]
会强迫
\[
\liminf\widehat P\ge1,
\]
与 \(p_*<1\) 冲突。内部还可含若干更深层 bubble；只要整个子树外面有上述 \(S^3\) 欧氏圆领圈，结论仍成立。

公式本身尚不能排除：

1. 外层链接为 \(S^3/\Gamma\)、\(\Gamma\ne1\) 的 orbifold bubble tree；
2. Hopf 塌缩或其他塌缩链接；
3. 非圆、非塌缩但具有显著径向剪切的领圈；
4. \(\mathcal Q_+\) 取 \(1<\mathcal Q_+<2-\varepsilon\) 的链接；
5. 不携带 exceptional 同调的纯曲率集中；
6. 无法选出两两不交标准 blow-up 区域的嵌套分解。

因此 “near-minimizers are not bubble trees” 比公式给出的内容更强。精确数学内容是：

> 次单位能量序列不能通过趋于欧氏圆 \(S^3\) 的领圈，把 exceptional 子树与主体分开。

同样，“exceptional topology 只能集中在曲率尺度链接或 \(\mathcal Q_+<1\) 的塌缩链接”也不是 G1 推出的二分。G1 只给出
\[
\mathcal Q_+\le1+\widehat P;
\]
在认证数值处，这仍允许几乎整个区间
\[
\mathcal Q_+\le1.995848.
\]
认证单元与非圆、弯曲链接相容，但公式没有证明所有其余退化都必须具有认证单元的具体几何。

最后，ball quotient 的有限覆盖说明是合理的：对固定外半径 \(R\)，紧球商只有有限多个长度不超过 \(2R\) 的闭测地线共轭类；残余有限性可取有限指数正规子群避开这些短元素，从而得到全局 injectivity radius 大于 \(R\) 的有限覆盖。认证单元的上界因此适用于 Step 33 明确指定的这类覆盖。

## 总结

核心无对称性恒等式、\(\mathcal Q_\pm=2\mathcal E\mp3\mathcal H\)、环域内外定向、薄 \((-1)\)-球面的 \((1,7)\)、ALE 荷中的 \(\tau+\eta\)、Taub–NUT 的 \((-2,2)\)、以及 G1 的 \(k+4\ell\) 系数均正确。需要改写得更精确的地方主要有：

* 圆空间形式荷需要平锥/ALE 领圈控制，不由三维内蕴圆度单独决定；
* 荷差给出下界，不是一般情形下的完整能量；
* \(\mathcal H=\frac23(1-\mathcal E)\) 需要 Ricci-flat 半共形平坦球填充，而非普通 \(W^-=0\)；
* G2 的序列推论需要两两不交区域或一个包住全部类的区域；
* G3 排除的是欧氏圆 \(S^3\) 分离的 exceptional ALE 子树，而不是所有 bubble-tree、塌缩或非圆退化。