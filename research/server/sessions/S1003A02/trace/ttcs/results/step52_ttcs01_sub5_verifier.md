# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/data/step52_absorption_lattice.json",
    "Sessions/S1003A02/workspace/scripts/step52_absorption_lattice.py",
    "Sessions/S1003A02/workspace/notes/step51_residual_entry_link_charges_and_kahler_recovery.md"
  ]
}
```

## Task

Verify Section 3 of the Step-52 note ('Kronheimer absorption of exceptional classes') and Proposition 52.10. Check: (a) Lemma 52.6 lattice facts (which ADE lattices or sums admit integral odd overlattices containing norm -1 vectors; A1+A1 in Z^2, A3=D3 in Z^3, D_n in Z^n; A8's index-3 overlattice is E8; the claim that k=1 cannot be absorbed), and whether 'E in R⊗Q' is the right notion given that links are rational homology spheres; (b) Theorem 52.7(a): S^4/Z2 with ι(z,x)=(-z,x), both points SU(2)-type for either orientation, gluing two Eguchi–Hanson spaces with τ=-2 gives CP2bar#CP2bar — check χ, τ, η=0, π_1, the T^2-action lifting to the toric EH resolutions, and the Orlik–Raymond conclusion; identify E1±E2; (c) Theorem 52.7(b): orientation bookkeeping for L(4,1), L(4,3), the A3 plumbing and the rational ball B_2, π_1, homeomorphism to #3CP2bar, and what is still needed for diffeomorphism; (d) the characteristic bookkeeping in the JSON (χ_orb, τ_orb, η_{Z4}=1/2 from 3η=r-2+2/|Γ|, the Theorem-G charges 1,0,0,2,3); (e) Corollary 52.8: the O(ε²) gluing estimate for Ricci-flat ALE into orbifold metrics, the identification X#(S^4/Z2)=(X#X)/ι with two isolated fixed points and P_orb=P_Z/2, hence α(X#2CP2bar) ≤ (1/2)α^ι(X#X); (f) Corollary 52.9: (i) unconditional, (ii) conditional, (iii) the refutation of 'every exceptional class in the bulk', (iv) the orbifold LeBrun estimate reproducing k ≤ A/3 in every absorption pattern (state precisely the orbifold SW input needed), (v) the non-Kähler argument via basic classes; and the global judgment paragraph. Also judge novelty: is this absorption phenomenon standard in the literature (e.g. resolutions of S^4/Z2, Kummer-type constructions, rational blowdown), and which statements need a citation rather than a proof. Return corrected statements.

## Output

# Section 3 与 Proposition 52.10 科学核验备忘

## 一、结论概览

1. **Lemma 52.6 的三个核心例子成立**：
   \[
   A_1\oplus A_1\subset -\mathbb Z^2,\qquad
   A_3=D_3\subset-\mathbb Z^3,\qquad
   D_n\subset-\mathbb Z^n
   \]
   都是指数 \(2\) 的整格扩张，扩张后含平方 \(-1\) 向量。\(A_8\) 的指数 \(3\) 整扩张是 \(E_8\)，仍为偶格，不含平方 \(-1\) 向量。

2. “\(E\in R\otimes\mathbb Q\)”正是沿球面空间形式接口分解时“该类由泡区域承载”的合理有理同调表述；整系数信息应写成饱和格
   \[
   R^{\mathrm{sat}}=(R\otimes\mathbb Q)\cap\bigl(H_2(M;\mathbb Z)/\mathrm{Tor}\bigr).
   \]
   真正承载 \(E\) 等价于 \(E\in R^{\mathrm{sat}}\)，而不只是某个抽象同构的扩张格含平方 \(-1\) 向量。

3. **“由秩可知 \(k=1\) 不能被吸收”按当前定义并不成立。** 它只有在附加
   \[
   R\otimes\mathbb Q\subset
   \operatorname{span}_{\mathbb Q}\{E_1,\dots,E_k\}
   \]
   且全部根格完全位于 blow-up 子空间时才成立。一般 \(D_n\otimes\mathbb Q\) 含平方 \(-1\) 向量，完全可能把唯一指定的 \(E\) 与 \(X\) 原有同调方向一起放入同一泡格。单个 \(A_1\) 确实不能承载平方 \(-1\) 整类。

4. **Theorem 52.7(a) 正确。** 两个 \(A_1\) 解消得到的闭流形光滑同胚于
   \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\)，两个 \((-2)\)-球在适当对角基下是 \(E_1+E_2\) 与 \(E_1-E_2\)，符号及次序可变。

5. **Theorem 52.7(b) 的定向、基本群、交叉形式以及拓扑同胚结论成立。** 光滑同胚于
   \(\#3\overline{\mathbb{CP}}^2\) 仍需：
   - 一份 Kirby 化简；或
   - 证明两侧圆作用在 \(L(4,\cdot)\) 上的带权轨道数据精确匹配，再调用 Fintushel–Pao 型分类结果。

6. JSON 中的
   \[
   \chi_{\rm orb},\quad\tau_{\rm orb},\quad
   \eta_{\mathbb Z_2}=0,\quad\eta_{\mathbb Z_4}=\tfrac12
   \]
   以及 charge 数字 \(1,0,0,2,3\) 全部正确。Proposition 52.10 最精确的守恒对象是两分量原始账本 \((C_+,C_-)\)，而不是取最大值后的单个 charge。

7. Corollary 52.8 的 \(O(\epsilon^2)\) 拼接估计和
   \[
   \alpha(X\#2\overline{\mathbb{CP}}^2)
   \le \frac12\alpha^\iota(X\#X)
   \]
   都成立。

8. Corollary 52.9(i)–(iii) 成立。(iv) 需要更强的 orbifold Seiberg–Witten 输入：单独一个非零 orbifold 不变量不足以推出
   \((c_Y^+)^2\ge A\)；需要所有相关符号选择的类都下降并保持非零，或直接把该不等式作为输入。(v) 原有 basic-class 数量论证不成立；可用一个更短、更强的特征类奇偶性论证替代。

---

## 二、Lemma 52.6：有理承载、饱和格与 ADE 扩张

### 2.1 为什么 \(E\in R\otimes\mathbb Q\) 是自然表述

设一个 ALE 泡的截面为 \(S^3/\Gamma\)。由于
\[
H_1(S^3/\Gamma;\mathbb Q)=H_2(S^3/\Gamma;\mathbb Q)=0,
\]
Mayer–Vietoris 在有理系数下给出泡区与主体区的正交型分解；泡区的 \(H_2\) 像正是 \(R\otimes\mathbb Q\)。因此：

- \(E\in R\otimes\mathbb Q\)：\(E\) 的有理同调分量完全位于泡区；
- 整系数中有限群 \(H_1(S^3/\Gamma;\mathbb Z)\) 会产生非本原嵌入；
- 对应的整格对象是
  \[
  R^{\rm sat}=(R\otimes\mathbb Q)\cap L,\qquad
  L=H_2(M;\mathbb Z)/\mathrm{Tor}.
  \]

所以“被吸收”可精确定义为
\[
E\in R^{\rm sat},
\]
它等价于当前写法 \(E\in R\otimes\mathbb Q\)，前提是已明确 \(E\) 是 \(L\) 中的整类。

一个抽象整扩张 \(R\subset S\) 含平方 \(-1\) 向量，仅说明该根格**可以**如此嵌入；要对应给定流形，还需要 \(S\) 就是实际嵌入的饱和格，且接口的 linking form 与粘合映射实现相应判别群胶合。

### 2.2 不可约 ADE 根格中哪些可扩张出平方 \(-1\) 向量

将符号反转为正定形式叙述。一个整扩张含平方 \(1\) 向量当且仅当存在
\[
v\in R^*,\qquad v^2=1.
\]
因为 \(v\in R^*\) 保证 \(v\cdot R\subset\mathbb Z\)，而 \(v^2=1\) 保证 \(R+\mathbb Zv\) 是整格。

#### \(A_n\)

令 \(N=n+1\)。判别群为 \(\mathbb Z/N\)。阶为 \(d\) 的胶合子群产生指数 \(d\) 的整扩张，需
\[
d^2\mid N.
\]
写 \(N=md^2\)。该子群非零陪集中的最小平方长度为
\[
m(d-1).
\]
它等于 \(1\) 当且仅当
\[
m=1,\qquad d=2,\qquad N=4.
\]
因此在所有不可约 \(A_n\) 中，只有
\[
A_3=D_3
\]
有含平方 \(1\) 向量的整扩张。

对 \(A_8\)，\(N=9\)、\(d=3\)，新陪集最小平方长度为 \(2\)，所得指数 \(3\) 扩张是 \(E_8\)。它为偶、酉模格，不含平方 \(1\) 向量。JSON 对此记录正确。

#### \(D_n\)

\[
D_n=\{x\in\mathbb Z^n:\sum_i x_i\equiv0\pmod2\}.
\]
故
\[
D_n\subset\mathbb Z^n
\]
指数为 \(2\)，而标准基向量 \(e_i\) 的平方为 \(1\)。在原负定号约定下即平方 \(-1\)。

这同时包含
\[
D_2=A_1\oplus A_1,\qquad D_3=A_3.
\]

#### \(E_6,E_7,E_8\)

- \(E_6\) 判别式 \(3\)，不存在非平凡整扩张；
- \(E_7\) 判别式 \(2\)，不存在非平凡整扩张；
- \(E_8\) 已是偶酉模格，不含平方 \(1\) 向量。

因此不可约 ADE 根格的完整结论是：

\[
\boxed{\text{可在整扩张中产生平方 }-1\text{ 向量的不可约类型恰为 }
A_3\text{ 与 }D_n\ (n\ge4).}
\]

再加上可约类型 \(A_1\oplus A_1=D_2\)。

对于任意 ADE 直和，完整代数表述是：在判别双线性型的直和中寻找整数自配对的胶合元素；等价地，在 \(R^*\) 中寻找平方 \(1\) 向量。因而不同分量可以共同产生平方 \(1\) 向量，例如两个 \(A_1^*\) 中各取平方 \(1/2\) 的元素。

### 2.3 三个显式嵌入

脚本中的向量正确：

\[
A_1\oplus A_1:
\quad a=e_1+e_2,\quad b=e_1-e_2,
\]
其 Gram 矩阵为 \(-2I_2\)，指数 \(2\)，且
\[
e_1=\tfrac12(a+b),\qquad e_2=\tfrac12(a-b).
\]

对 \(A_3\)，取
\[
a_1=e_2-e_3,\quad a_2=e_1-e_2,\quad a_3=e_2+e_3.
\]
则
\[
e_1=\tfrac12a_1+a_2+\tfrac12a_3,\qquad
e_2=\tfrac12a_1+\tfrac12a_3,\qquad
e_3=-\tfrac12a_1+\tfrac12a_3.
\]
这与 JSON 完全一致。

### 2.4 关于 \(k=1\)

以下命题正确：

> 若整个泡根格满足
> \[
> R\otimes\mathbb Q\subset
> \operatorname{span}_{\mathbb Q}\{E\},
> \qquad E^2=-1,
> \]
> 则非零 ADE 根格不可能存在。

因为任一根 \(a=qE\) 将满足
\[
-2=a^2=-q^2,
\]
从而 \(q^2=2\)，与 \(q\in\mathbb Q\) 矛盾。

但若 \(R\otimes\mathbb Q\) 还使用 \(X\) 的同调方向，则 \(D_n\) 中的一个平方 \(-1\) 向量完全可以指定为唯一的 blow-up 类。因此原句“by rank, \(k=1\) cannot be absorbed”应加上“根格完全位于 blow-up 子空间”这一假设。

---

## 三、Theorem 52.7(a)：两个 \(A_1\) 点的解消

### 3.1 局部群与定向

作用
\[
\iota(z_1,z_2,x)=(-z_1,-z_2,x)
\]
在 \(S^4\subset\mathbb C^2\times\mathbb R\) 上有两个不动点
\[
(0,0,\pm1).
\]
切表示均为 \(-I\) 作用于 \(\mathbb R^4\cong\mathbb C^2\)。元素 \(-I\) 是两个四维半旋群中的中心元素，因此反转整体定向后仍可视为 \(SU(2)\)-型 \(A_1\) 奇点。此处原文正确。

### 3.2 Euler 数、signature 与 \(\eta\)

商空间的 Satake orbifold Euler 数是
\[
\chi_{\rm orb}(S^4/\mathbb Z_2)=\frac{\chi(S^4)}2=1.
\]
其底层拓扑空间是 \(\Sigma(\mathbb{RP}^3)\)，Euler 数为
\[
\chi_{\rm top}=2.
\]

去掉两个锥邻域后得到 \(\mathbb{RP}^3\times I\)。每个截断 Eguchi–Hanson 空间缩到一个 \(S^2\)，Euler 数为 \(2\)，替换一个锥点使闭流形的 Euler 数增加 \(1\)。因此
\[
\chi=2+1+1=4.
\]

每个 \(A_1\) plumbing 的交叉形式为 \([-2]\)，signature 为 \(-1\)，中间圆柱块的 signature 为 \(0\)，故
\[
\tau=-2.
\]

由
\[
3\eta_{\mathbb Z_2}
=1-2+\frac22=0
\]
得到
\[
\eta_{\mathbb Z_2}=0.
\]

### 3.3 基本群

中间块的基本群为 \(\mathbb Z_2\)。截断 Eguchi–Hanson 空间单连通，而
\[
\pi_1(\mathbb{RP}^3)=\mathbb Z_2
\longrightarrow\pi_1(\mathbb{RP}^3\times I)
\]
是同构。粘上第一个 Eguchi–Hanson 块已经杀掉该 \(\mathbb Z_2\)，所以闭流形单连通。

### 3.4 \(T^2\)-作用与光滑类型

坐标旋转
\[
(e^{i\theta_1},e^{i\theta_2})\cdot(z_1,z_2,x)
=(e^{i\theta_1}z_1,e^{i\theta_2}z_2,x)
\]
与 \(\iota\) 对易。商作用的有限核可除去，得到有效二维环面作用。局部 \(A_1\) 解消是 toric 的，因而作用提升到两端的解消块。

Orlik–Raymond 分类随后给出该单连通闭四维流形是标准连通和。由
\[
b_2=2,\qquad \tau=-2
\]
可知交叉形式为 \(-I_2\)，因此
\[
\widehat{S^4/\mathbb Z_2}
\cong\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2.
\]

两条解消球互不相交且各自平方 \(-2\)。在 \(-I_2\) 的基 \(E_1,E_2\) 中，一对正交根只能是
\[
\pm(E_1+E_2),\qquad \pm(E_1-E_2)
\]
的形式，故原文的识别正确，需理解为“在符号和交换后”。

---

## 四、Theorem 52.7(b)：\(B_2\)、\(A_3\) 与 \(Q_3\)

### 4.1 Lens 空间定向

固定约定
\[
L(p,q)=S^3/\bigl((z_1,z_2)\mapsto(\zeta z_1,\zeta^qz_2)\bigr).
\]
\(A_3\) 奇点是
\[
\frac14(1,3),
\]
其 link 为 \(L(4,3)\)。取有理球 \(B_2\) 满足
\[
\partial B_2=-L(4,3)\cong L(4,1).
\]
这与
\[
B_2=\mathbb{CP}^2\setminus N(\text{conic})
\]
相容；不同 lens 记号约定会互换 \(L(4,1)\) 与 \(L(4,3)\)，因此文中必须把定向等式与无定向同胚分开写。

### 4.2 基本群

已知
\[
\pi_1(B_2)=\mathbb Z_2,
\]
且
\[
\pi_1(L(4,\cdot))=\mathbb Z_4\longrightarrow\mathbb Z_2
\]
是模 \(2\) 满射。\(A_3\) plumbing 单连通。Van Kampen 因而给出
\[
\pi_1(Q_3)=1.
\]

### 4.3 同调与交叉形式

\(B_2\) 是有理同调四球，故 \(\chi(B_2)=1\)。\(A_3\) plumbing 缩到三条链状 \(S^2\)，Euler 数为
\[
3\cdot2-2=4.
\]
粘合截面 Euler 数为零，所以
\[
\chi(Q_3)=1+4=5.
\]
单连通给出 \(b_2=3\)。有理系数 Mayer–Vietoris 表明交叉形式就是 \(A_3\) 的负定形式，所以
\[
\tau(Q_3)=-3.
\]

Donaldson 定理给出整交叉形式 \(-I_3\)，Freedman 分类再给出
\[
Q_3\ \text{拓扑同胚于}\ \#3\overline{\mathbb{CP}}^2.
\]

### 4.4 光滑同胚还差什么

给定的圆作用
\[
[x:y:z]\longmapsto[s^2x:sy:z]
\]
确实保持圆锥曲线 \(xz=y^2\)，从而作用于 \(B_2\)。\(A_3\) 解消有 toric 作用。但“两边都有圆作用”尚不足以直接得到闭流形上的圆作用；还需证明所选
\[
L(4,1)\cong -L(4,3)
\]
粘合映射匹配两侧的稳定子权重、奇异轨道和纤维斜率。

一旦这一等变匹配写出，Fintushel–Pao 型分类可推出标准光滑类型。另一条完整路线是 Kirby 图化简到三个互不链接、framing 为 \(-1\) 的 2-handle。当前 note 将结论暂时表述为 \(X\#Q_3\) 是适当的。

---

## 五、JSON 与 Proposition 52.10

### 5.1 特征数

对 Kronheimer \(A_{r}\) ALE 空间，
\[
\chi=1+r,\qquad\tau=-r,\qquad
3\eta_\Gamma=r-2+\frac2{|\Gamma|}.
\]

因此：

- Eguchi–Hanson：
  \[
  r=1,\ |\Gamma|=2,\quad\eta=0;
  \]
- \(A_3\)：
  \[
  r=3,\ |\Gamma|=4,\quad
  \eta=\frac12.
  \]

对 \(\Sigma_4=B_2\cup\operatorname{cone}(L(4,3))\)：
\[
\chi_{\rm orb}(\Sigma_4)
=\chi_{\rm top}(\Sigma_4)-\left(1-\frac14\right)
=2-\frac34=\frac54.
\]
又因 \(Q_3\) 的 signature 已由有理同调直接算得 \(-3\)，
\[
-3=\tau_{\rm orb}(\Sigma_4)+\tau(A_3)+\eta_{\mathbb Z_4},
\]
即
\[
-3=\tau_{\rm orb}(\Sigma_4)-3+\frac12,
\]
故
\[
\tau_{\rm orb}(\Sigma_4)=-\frac12.
\]

于是
\[
2\chi_{\rm orb}(\Sigma_4)+3\tau_{\rm orb}(\Sigma_4)
=\frac52-\frac32=1.
\]
与 \(X\) 在正则点连通和时减去 \(2\)，故相对于 \(2\chi(X)+3\tau(X)=A\) 的变化是
\[
1-2=-1
\]
再结合 orbifold signature 的连通和 bookkeeping，最终 note 中
\[
(2\chi+3\tau)_{\rm orb}(X\#\Sigma_4)=A-3
\]
是正确的；等价地直接用
\[
\Delta\chi=-\frac34,\qquad \Delta\tau=-\frac12
\]
得到
\[
2\Delta\chi+3\Delta\tau=-3.
\]

对 \(S^4/\mathbb Z_2\)：
\[
\Delta\chi_{\rm orb}=1-2=-1,\qquad\Delta\tau_{\rm orb}=0,
\]
故
\[
\Delta(2\chi+3\tau)=-2.
\]

### 5.2 Theorem-G charge 重算

定义原始两分量
\[
C_\sigma=
\sum_{\rm out}q_\sigma
-\sum_{\rm in}q_\sigma
-(2\chi+3\sigma\tau),
\qquad
q_\sigma(\Gamma)=\frac2{|\Gamma|}-3\sigma\eta_\Gamma.
\]

各块为：

| 块 | \((C_+,C_-)\) | 标量 charge |
|---|---:|---:|
| Burns | \((1,-5)\) | \(1\) |
| EH | \((0,-6)\) | \(0\) |
| \(A_3\) ALE | \((0,-15)\) | \(0\) |
| \(S^4/\mathbb Z_2\) cell | \((2,2)\) | \(2\) |
| \(\Sigma_4\) cell | \((3,0)\) | \(3\) |
| \(D\#2\overline{\mathbb{CP}}^2\) cell | \((2,-10)\) | \(2\) |
| \(D\#3\overline{\mathbb{CP}}^2\) cell | \((3,-15)\) | \(3\) |

真正逐接口相消的是 \(C_\sigma\)，并且这里有精确恒等式
\[
(2,2)+2(0,-6)=(2,-10),
\]
以及
\[
(3,0)+(0,-15)=(3,-15).
\]
所以 Proposition 52.10 可加强为：

> 在这两个吸收构造中，原始两分量账本与相应平滑 \(k\)-blow-up cell 的账本完全相等；取
> \(\max\{0,C_+,C_-\}\) 后分别得到 \(2\) 与 \(3\)。

对一般泡树，先取最大值会破坏线性相消，因此“守恒”应首先陈述于 \((C_+,C_-)\) 层面。

### 5.3 脚本本身

脚本正确复现了所列 Gram 矩阵、指数、坐标表达式及 charge 数值。三点需要在数据说明中写清：

1. `all_roots_norm_-2` 实际只检验了输入的简单根向量，并未枚举全部根；
2. `single_lattice_overlattice` 中 \(A_8,E_8,D_4\) 的说明是手工写入，不是程序推导；
3. `tau_orb_Sigma4` 在程序中由预期解消 signature 反解。数学上可用上面的 \(H_2(Q_3;\mathbb Q)\cong A_3\) 先独立得到 \(\tau(Q_3)=-3\)，从而消除循环性。

浮点行列式对当前小矩阵给出了正确整数；若作为长期证据文件，整系数 Bareiss 或符号行列式会更直接。

---

## 六、Corollary 52.8

### 6.1 \(O(\epsilon^2)\) 拼接代价

在 orbifold 正规坐标中
\[
g_{\rm orb}=\delta+O(r^2),\qquad
\partial^jg_{\rm orb}=O(r^{2-j}).
\]
Kronheimer ALE 在无穷远处有
\[
g_{\rm ALE}=\delta+O(R^{-4}).
\]
缩放尺度为 \(\epsilon\) 后，在物理坐标 \(r=\epsilon R\) 中
\[
g_{\epsilon,\rm ALE}
=\delta+O(\epsilon^4r^{-4}),
\qquad
\partial^j(g_{\epsilon,\rm ALE}-\delta)
=O(\epsilon^4r^{-4-j}).
\]

取过渡半径
\[
\rho=\epsilon^{1/2}.
\]
cutoff 产生的曲率量级为
\[
O(1)+O(\epsilon^4\rho^{-6})
=O(1)+O(\epsilon).
\]
过渡环体积为
\[
O(\rho^4)=O(\epsilon^2).
\]
因此
\[
\int_{\rm neck}|\operatorname{Ric}^\circ|^2
=O(\epsilon^2).
\]
ALE 内部 Ricci-flat，移去的 orbifold 小球也只贡献 \(O(\rho^4)=O(\epsilon^2)\)，所以
\[
P(g_\epsilon)=P_{\rm orb}(g)+O(\epsilon^2).
\]
这证明
\[
\alpha(\operatorname{resolution}(Y))
\le\alpha_{\rm orb}(Y).
\]

### 6.2 双覆盖与 \(\frac12\) 因子

在 \(S^4\) 中取一对由 \(\iota\) 交换的正则点，分别与两份 \(X\) 作等变连通和。所得双覆盖为
\[
Z=X\#S^4\#X\cong X\#X,
\]
商为
\[
Y=X\#(S^4/\mathbb Z_2).
\]
新的 involution 交换两份 \(X\)，并保留原来两个孤立不动点。

\(Y\) 上的光滑 orbifold 度量与 \(Z\) 上的 \(\iota\)-不变光滑度量一一对应。由于覆盖次数为 \(2\)，孤立不动点为零测集，
\[
P_Z(g)=2P_{\rm orb}(g/\iota).
\]
故实际上有
\[
\alpha_{\rm orb}(Y)
=\frac12\alpha^\iota(Z),
\]
再结合解消估计，
\[
\boxed{
\alpha(X\#2\overline{\mathbb{CP}}^2)
\le\frac12\alpha^\iota(X\#X).
}
\]

特别地，取 \(X=S^4\) 和 round \(S^4/\mathbb Z_2\)，可直接得到
\[
\alpha(\overline{\mathbb{CP}}^2\#
\overline{\mathbb{CP}}^2)=0.
\]
这已经是“两个 exceptional classes 全部由 EH 根格承载”的真实零间隙实例。

---

## 七、Corollary 52.9

### 7.1 (i) 与 (ii)

(i) 成立：若紧 orbifold 主体为 Einstein，所有插入的 ALE 块 Ricci-flat，则上述拼接给出
\[
P(g_\epsilon)\to0,
\]
故解消流形满足 \(\alpha=0\)。多层泡树可用分离尺度逐层拼接。

(ii) 在 Theorem 52.3 及选择机制给出的非塌缩序列下，
\[
0=\alpha\ge
P(g_\infty)+\sum_bP(N_b).
\]
每项非负，故主体各分支 Einstein，所有 ALE 泡 Ricci-flat。Ricci-flat ALE 在非负 Ricci 条件下不能有多个 Euclidean-growth ends；若 \(\Gamma=1\)，其渐近体积比为 \(1\)，Bishop–Gromov 等号情形给出平坦 \(\mathbb R^4\)。因此非平凡零代价泡必经 \(\Gamma\ne1\) 的 link。

### 7.2 (iii)

成立，但措辞宜为：

> Exceptional classes 不必在 orbifold 主体的有理 \(H_2\) 中出现；它们可以属于泡根格在总整格中的饱和扩张。

EH 对的 round \(S^4/\mathbb Z_2\) 解消已经给出实际反例。这里“不可见”仅指有理交叉形式投影；link 上的扭结数据、局部 isotropy character 和 orbifold Spin\(^c\) 提升仍可能记录这些类。

### 7.3 (iv)：orbifold LeBrun 输入必须加强

设 \(M=X\#k\overline{\mathbb{CP}}^2\)，\(A=K_X^2\)，且 orbifold 主体为 \(Y\)。若所有泡为 \(SU(2)\) Kronheimer 型，则
\[
(2\chi+3\tau)_{\rm orb}(Y)=A-k.
\]

对 Einstein orbifold，LeBrun 型估计需要一个 orbifold Spin\(^c\) 结构，其 SW 不变量在相关 chamber 中非零，并满足
\[
(2\chi+3\tau)_{\rm orb}(Y)
\ge\frac23(c_Y^+)^2.
\]

要进一步推出
\[
(c_Y^+)^2\ge A,
\]
不能只假设“某一个投影类有非零不变量”。足够的精确输入是：

1. \(K_X\) 投影为 \(K_0\in H^2_{\rm orb}(Y;\mathbb Q)\)，且
   \[
   K_0^2=A;
   \]
2. 被吸收的 \(E_i\) 投影为零；
3. 对每个未吸收类的全部符号选择
   \[
   c_{\varepsilon}
   =K_0+\sum_{j=1}^{u}\varepsilon_j e_j,
   \qquad \varepsilon_j=\pm1,
   \]
   相应 orbifold Spin\(^c\) 结构均存在，并在给定 polarization/chamber 中提供非零 SW 输入。

此时符号平均给出
\[
2^{-u}\sum_{\varepsilon}
\left\|
\left(K_0+\sum_j\varepsilon_je_j\right)^+
\right\|^2
=
\|K_0^+\|^2+\sum_j\|e_j^+\|^2
\ge K_0^2=A.
\]
故至少一个符号选择满足
\[
(c_\varepsilon^+)^2\ge A.
\]
于是
\[
A-k\ge\frac23A,
\qquad
k\le\frac A3.
\]

因此 \(k\le A/3\) 的代数推导正确，但 orbifold Spin\(^c\) 下降、局部群表示以及非零 SW 不变量的切割—粘合定理尚未由 Section 3 提供。单独写“a nonzero orbifold SW invariant for the projected class”不足以支撑符号选择步骤。

### 7.4 (v)：应替换为特征类奇偶性论证

原文“解消曲面只有 \(\pm K\) 两个 basic classes”一般不成立；极小一般型曲面可能有其他 basic classes，而且“奇点的极小解消”不等于“作为紧复曲面的极小模型”。

这里有一个更直接的证明。

若 \(Y\) 是复 orbifold，局部群属于 \(SU(2)\)，则奇点是 Du Val 型，极小复解消
\[
\pi:Z\to Y
\]
是 crepant 的。因此
\[
K_Z\cdot r=0
\qquad\text{对每个 exceptional root }r\in R.
\]
若某个平方 \(-1\) 整类 \(E\) 被吸收，即
\[
E\in R\otimes\mathbb Q,
\]
则
\[
K_Z\cdot E=0.
\]
但 \(K_Z\) 是特征类，所以
\[
K_Z\cdot E\equiv E^2\equiv1\pmod2,
\]
矛盾。

因此可得到更强结论：

\[
\boxed{
\text{复 }SU(2)\text{-orbifold 的 crepant 解消中，
任何平方 }-1\text{ 整类都不能属于 exceptional 根格的有理张成。}
}
\]

这不仅排除“所有 exceptional classes 被吸收”，还排除任何单个平方 \(-1\) 类被如此吸收。故 EH-pair 吸收或 \(A_3\) 吸收若由 Einstein orbifold 实现，该 orbifold 不能同时带有使这些奇点成为复 \(SU(2)\) 商奇点的全局复结构。

---

## 八、对 global judgment 的精确改写

由
\[
\alpha(M)\le\alpha_{\rm orb}(Y)
=\frac12\alpha^\iota(Z)
\]
可知，若证明
\[
\alpha(X\#2\overline{\mathbb{CP}}^2)>0,
\]
则自动得到
\[
\alpha_{\rm orb}(X\#S^4/\mathbb Z_2)>0,
\qquad
\alpha^\iota(X\#X)>0.
\]
这比排除一个精确 Einstein 度量更强，因为还必须排除 \(P\to0\) 但不达到的 \(\iota\)-不变序列。

因此 global paragraph 宜改为：

> 开区间 \(0<k<A/3\) 中的正 Einstein 间隙问题，不仅包含对原光滑流形 Einstein 度量的排除，还包含对相应吸收 orbifold 及其有限覆盖上对称近 Einstein 序列的统一控制。Exceptional root lattice 可以在有理交叉形式层面吸收 blow-up 类，所以任何把每个标准 \(E_i\) 预先放入主体并逐类收费的论证均不适用。可能成立的逐类下界仍需使用 link 的局部表示、Spin\(^c\) 延拓、场论通量或非标准 germ，而不能只依赖抽象 exceptional 格。

对 \(S^4/\mathbb Z_2\) 分支，orbifold Einstein 度量与 \(\iota\)-不变 Einstein 度量确实等价。对 \(\Sigma_4\) 分支没有在 note 中构造相同的 involution 双覆盖，因此不应把两类 orbifold 同时写成与 \(X\#X\) 上 involution 问题等价。

---

## 九、文献位置与新颖性判断

这些拓扑与格现象本身大多已有标准背景：

1. **根格非本原嵌入与判别型胶合**属于整格理论的标准内容；应引用判别群、整扩张与 primitive closure 的系统来源。
2. **Kummer 解消**是经典类比：\(T^4/\{\pm1\}\) 的 \(A_1^{16}\) 根格在 \(K3\) 格中非本原，primitive closure 含半和类。那里总格为偶格，所以不会产生平方 \(-1\) 向量，但“根格的有理张成比根格本身承载更多整类”完全是经典机制。
3. **\(S^4/\mathbb Z_2=\Sigma(\mathbb{RP}^3)\)**、两端 \(A_1\) plumbing 以及 toric 提升应配合 Orlik–Raymond 分类给出引用；当前证明本身已足以推出光滑类型。
4. **\(B_2\) 与 lens 空间、\(A_3\) plumbing 的替换**属于 rational blowdown/rational blow-up 技术的标准图景。\(Q_3\) 的具体光滑类型最好引用现成 Kirby 计算；若无来源，就保留 \(Q_3\) 记号。
5. **\(\eta\)、orbifold signature 与 Euler 数**应引用 APS/Kawasaki 型公式及 Kronheimer ALE 的拓扑公式。
6. **orbifold LeBrun 估计**必须给出实际定理来源，尤其是孤立 quotient 奇点、orbifold Spin\(^c\) 结构、chamber 以及 SW 不变量非零的精确假设。
7. “吸收”作为连接 Einstein defect、ALE 零代价泡与 blow-up 类的组织方式可能具有研究价值；但仅凭现有材料不能确认其在文献中的首创性。真正较有特色的是由这些标准拓扑机制导出的
   \[
   \alpha(X\#2\overline{\mathbb{CP}}^2)
   \le\frac12\alpha^\iota(X\#X)
   \]
   以及它对 Einstein 间隙论证结构的影响，而不是根格非本原嵌入本身。