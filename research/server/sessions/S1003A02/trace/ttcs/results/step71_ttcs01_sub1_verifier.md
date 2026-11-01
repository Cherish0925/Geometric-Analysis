# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step71_functional_split_and_unit_wall.md",
    "Sessions/S1003A02/workspace/scripts/step71_functional_split_examples.py",
    "Sessions/S1003A02/workspace/data/step71_functional_split_examples.json",
    "Knowledge/objects/papers/dg-ga-9411001-Self-Dual-Manifolds-with-Positive-Ricci-Curvature--92f685b1b31c--e3fd78dbc8b6/object.md",
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md"
  ]
}
```

## Task

Verify the mathematics of the Step-71 note on the Einstein-defect functional E(g)=inf_{lambda!=0} int|Ric-lambda g|^2/(lambda^2 V) on closed oriented 4-manifolds. Check with full rigor, and correct where needed: (1) Identity 71.1 E-1=(12 int|W^±|^2+L_s-24pi^2 T_±)/R, T_±=2chi±3tau, in LeBrun's conventions (compare the inherited corpus statement at Curvature_Realizability lines 1520-1543 if given in the excerpt) and the JSON example checks. (2) Theorem 71.B: strictness for T_+<0; the equality characterization E=1 iff W^+=0 and s nonzero constant when T_+=0<=T_-; the attainment criterion via Yamabe classes; the positive-scalar Betti classification (b1,b2) in {(0,4),(1,0)} (Weitzenbock with W^+=0, s>0 gives b_+=0). (3) Theorem 71.C: alpha=1 attained on S^1 x S^3/Gamma, S^1 x_phi H^3/Gamma, and #4 CPbar^2 via LeBrun's hyperbolic-ansatz self-dual classes with positive scalar representatives (source lines quoted in the note); non-existence of Einstein metrics on these; the claim that K3 and T^4 have alpha>=1 although Ricci-flat; the ASD constant-scalar formula E=1+9m/(3m+4y). (4) Theorem 71.D, the long-circle reservoir: alpha(N # (S^1 x Y))<=1 for any N and Y spherical space form or hyperbolic 3-manifold, by taking S^1 of length L -> infinity and gluing a rescaled N in a fixed ball. Scrutinize whether all junk terms (R, W^+, L_s including the mean-scalar shift, the neck) are really O(1) uniformly in L, whether scale-invariance is used correctly, and the corollary alpha(X#kCPbar^2#l(S^1xS^3)) <= min(1,4h/(1+h)), =1 iff k+4l>=A. (5) Lemma 71.T and the alpha-readings of 59.C/59.N/59.Z: especially the Gauss-Bonnet argument that E-small sequences normalized at lambda_opt=1 have V<=12pi^2 chi(1+o(1)) and cannot collapse totally with bounded curvature, and the a^4/6 EH alpha-rate on CP^2#CP^2. Also state precisely what is new versus classical (Hitchin-Thorpe, LeBrun-Nayatani-Nitta Gauss-Bonnet form, corpus) as far as the supplied sources allow, and name any knowledge_request needed for precedence. Give a direct scientific memo with corrected statements.

## Output

# Step 71 数学核验备忘录

## 一、结论概览

Step 71 的核心分离是正确的：

- \(\mathcal E\) 与 \(P=\int|\operatorname{Ric}^{\circ}|^{2}\) 是本质不同的泛函；
- 单位墙 \(\alpha\ge 1\)、其等号几何、\(\#4\overline{\mathbb {CP}}^{2}\) 上达到的正间隙，以及长圆周储库构造均成立；
- ASD 常标量曲率公式计算正确。

需要修订的主要点有五个：

1. Identity 71.1 只在 \(R=\int|\operatorname{Ric}|^{2}>0\) 时可写成商；Ricci-flat 情形必须单列。JSON 中 K3 的程序分支直接赋值 \(4\)，并未核验该商恒等式。
2. 正标量等号类中，Donaldson 对角化需要加入单连通假设；\(b_{1}=0\) 本身不足。
3. 一般型曲面的含柄连通和上，只证明了 \(k+4\ell\ge A\Rightarrow\alpha=1\)；反向等价在 \(1/3\le h<1\) 没有得到。
4. \(\lambda_{\rm opt}\) 的统一归一化应为 \(\lambda_{\rm opt}=\pm1\)，以涵盖趋近正、负 Einstein 几何的序列。
5. \(\mathbb {CP}^{2}\#\mathbb {CP}^{2}\) 上的 \(a^{4}/6\) 系数仍依赖
   \[
   L_s=o(a^{4}).
   \]
   现有材料没有给出这一估计，因而该系数目前是条件式结果。

---

## 二、泛函的精确最小化与 Identity 71.1

记
\[
R=\int_M|\operatorname{Ric}|^{2},\qquad
T_s=\int_M s,\qquad
P=\int_M|\operatorname{Ric}^{\circ}|^{2},\qquad
L_s=\int_M(s-\bar s)^2.
\]
对于 \(R>0\)，令 \(x=\lambda^{-1}\)，则
\[
\frac{\int|\operatorname{Ric}-\lambda g|^{2}}{\lambda^{2}V}
=4+\frac RVx^{2}-2\frac{T_s}{V}x.
\]
因此
\[
\lambda_{\rm opt}=\frac{R}{T_s}\quad(T_s\ne0),
\qquad
\mathcal E(g)=4-\frac{T_s^{2}}{RV}.
\]
当 \(T_s=0\) 时，右侧等于 \(4\)；此时关于 \(\lambda\) 的下确界在 \(|\lambda|\to\infty\) 时逼近。

又因为
\[
R=P+\frac14\int s^{2},
\qquad
L_s=\int s^{2}-\frac{T_s^{2}}{V},
\]
故
\[
\boxed{\mathcal E(g)=\frac{4P+L_s}{R}}\qquad(R>0).
\]

在 LeBrun 约定下，
\[
8\pi^{2}\chi
=\int\left(|W^+|^{2}+|W^-|^{2}+\frac{s^{2}}{24}-\frac P2\right),
\]
\[
12\pi^{2}\tau=\int\left(|W^+|^{2}-|W^-|^{2}\right).
\]
于是
\[
4\pi^{2}T_\pm
=\int\left(2|W^\pm|^{2}+\frac{s^{2}}{24}-\frac P2\right),
\qquad T_\pm=2\chi\pm3\tau.
\]
乘以 \(6\) 并使用 \(R=P+\frac14\int s^{2}\)，得到
\[
24\pi^{2}T_\pm
=12\int|W^\pm|^{2}+R-4P,
\]
即
\[
\boxed{R=4P+24\pi^{2}T_\pm-12\int|W^\pm|^{2}}.
\]
再代入 \(\mathcal E R=4P+L_s\)，得到
\[
\boxed{
\mathcal E(g)-1
=\frac{12\int|W^\pm|^{2}+L_s-24\pi^{2}T_\pm}{R}
}\qquad(R>0).
\]

### Ricci-flat 情形

若 \(R=0\)，则 \(\operatorname{Ric}=0\)、\(s=0\)，且对每个 \(\lambda\ne0\)
\[
\frac{\int|-\lambda g|^{2}}{\lambda^{2}V}=4.
\]
因此 \(\mathcal E=4\)。此时上面的商恒等式没有定义，但第二个无商恒等式仍成立。

### JSON 的实际验证内容

脚本对所有 \(R>0\) 的齐性例子正确核验了：

- 最小化定义；
- \((4P+L_s)/R\)；
- Chern–Gauss–Bonnet 与 signature 公式；
- Identity 71.1。

但这些例子均有 \(L_s=0\)，所以脚本没有数值测试变标量曲率项。K3 分支在 `R == 0` 时直接令三个 \(\mathcal E\) 表达式都等于 \(4\)，故它只核验了 Ricci-flat 的直接定义和拓扑公式，而没有核验 Identity 71.1 的商形式。

---

## 三、Theorem 71.B：单位墙和等号几何

### 1. \(T_+\le0\)

若 \(T_+<0\)，Ricci-flat 度量不可能存在，因为 Ricci-flat 时
\[
T_+=\frac1{2\pi^{2}}\int|W^+|^{2}\ge0.
\]
所以每个度量都有 \(R>0\)，而
\[
\mathcal E-1
=\frac{12\int|W^+|^{2}+L_s+24\pi^{2}|T_+|}{R}
\ge\frac{24\pi^{2}|T_+|}{R}>0.
\]
因此逐个度量都有 \(\mathcal E>1\)，但下确界仍可能等于 \(1\)。若
\(\mathcal E(g_j)\to1\)，则
\[
\frac{
12\int|W^+_{g_j}|^{2}+L_s(g_j)+24\pi^{2}|T_+|
}{R(g_j)}
\longrightarrow0,
\]
从而必有 \(R(g_j)\to\infty\)。Step 71(b) 的解释正确。

### 2. \(T_+=0\)

对于 \(R>0\)，
\[
\mathcal E-1
=\frac{12\int|W^+|^{2}+L_s}{R}.
\]
故
\[
\mathcal E=1
\iff W^+\equiv0,\quad L_s=0.
\]
这等价于 \(W^+=0\) 且 \(s\) 为常数。该常数不能为零：若 \(s=0\)，则 \(T_s=0\)，直接定义给出 \(\mathcal E=4\)；结合 \(T_+=W^+=0\) 还会推出 \(P=R=0\)。

所以精确表述是
\[
\boxed{
\mathcal E(g)=1
\iff W^+_g=0\ \text{且}\ s_g\ \text{为非零常数}.
}
\]

### 3. Yamabe 类刻画

半 Weyl 张量的消失在共形变换下保持。若某个 \(W^+=0\) 共形类满足 \(Y([g])\ne0\)，其 Yamabe 度量具有非零常标量曲率，因而达到 \(\mathcal E=1\)。

反过来，达到 \(\mathcal E=1\) 的度量本身有非零常标量曲率；其共形类的 Yamabe 常数与该标量曲率同号，因而非零。于是
\[
\boxed{
\alpha(M)=1\ \text{被达到}
\iff
M\ \text{存在}\ W^+=0,\ Y\ne0\ \text{的共形类}.
}
\]
所有达到值 \(1\) 的度量正是这些共形类中的非零常标量曲率代表，不要求它们自身一定是 Yamabe 极小代表。

Einstein 度量不可能达到值 \(1\)：非零 Einstein 度量给出 \(\mathcal E=0\)，Ricci-flat 度量给出 \(\mathcal E=4\)。

### 4. 正标量曲率等号类

若 \(W^+=0\) 且 \(s>0\)，自对偶调和二形式满足
\[
0=\int\left(|\nabla\omega|^{2}+\frac{s}{3}|\omega|^{2}
-2\langle W^+\omega,\omega\rangle\right),
\]
故 \(b_+=0\)。

又
\[
T_+=4-4b_1+5b_+-b_-.
\]
由 \(T_+=0\)、\(b_+=0\) 得
\[
b_-=4-4b_1.
\]
因此
\[
(b_1,b_2)\in\{(0,4),(1,0)\}.
\]

这里需修订 Donaldson–Freedman 句子：

- 当 \((b_1,b_2)=(0,4)\) 时，只能先得到自由部分上的交叉形式负定；
- 若再假设 \(M\) 单连通，Donaldson 定理才给出交叉形式 \(-I_4\)；
- 随后 Freedman 定理给出
  \[
  M\approx\#4\overline{\mathbb {CP}}^{2}
  \]
  的拓扑同胚。

原文从 \(b_1=0\) 直接使用 Donaldson 对角化缺少单连通假设。

---

## 四、Theorem 71.C 的例子

### 1. \(S^1\times S^3/\Gamma\)

取三维球面空间形式截面曲率 \(+1\)。乘积度量的 Ricci 特征值为
\[
(0,2,2,2),
\]
所以
\[
R=12V,\qquad P=3V,\qquad s=6,\qquad W=0.
\]
因此
\[
\mathcal E=\frac{4P}{R}=1.
\]
又 \(\chi=\tau=0\)，单位墙给出 \(\alpha\ge1\)，故
\[
\boxed{\alpha(S^1\times S^3/\Gamma)=1}
\]
且被乘积度量达到。

它不可能有 Einstein 度量。若闭四维流形满足 \(\chi=0\) 且度量 Einstein，则
\[
0=8\pi^{2}\chi=\int\left(|W|^{2}+\frac{s^{2}}{24}\right),
\]
从而度量平坦。闭平坦四维流形的基本群含有限指数的 \(\mathbb Z^4\)，而
\(\pi_1(S^1\times S^3/\Gamma)\) 仅虚拟同构于 \(\mathbb Z\)。

### 2. 双曲三流形的等距映射环面

设 \(Y=H^3/\Gamma\)，\(\phi\) 为保向等距映射。度量
\[
dt^2+h_Y
\]
在
\[
(\mathbb R\times Y)/(t,y)\sim(t+L,\phi(y))
\]
上良定义，局部 Ricci 特征值为
\[
(0,-2,-2,-2).
\]
它局部共形平坦，\(s=-6\)，同样给出 \(\mathcal E=1\)。由局部共形平坦性和 signature 公式，\(\tau=0\)；映射环面还有 \(\chi=0\)。所以
\[
\boxed{\alpha(S^1\times_\phi Y)=1}
\]
并被达到。

若存在 Einstein 度量，仍由 \(\chi=0\) 推出平坦；但其基本群包含闭双曲三流形群，不是虚拟阿贝尔群，故不可能是 Bieberbach 群。

### 3. \(\#4\overline{\mathbb {CP}}^{2}\)

这里
\[
\chi=6,\qquad \tau=-4,\qquad T_+=0.
\]
给定的 LeBrun–Nayatani–Nitta 文本明确说明：

- 对每个 \(n\)，LeBrun 的 hyperbolic ansatz 在 \(n\mathbb {CP}^{2}\) 上给出 self-dual 共形类；
- 每个所构造的共形类都含正标量曲率代表。

反向定向后，这在 \(n\overline{\mathbb {CP}}^{2}\) 上给出 \(W^+=0\) 的共形类。取 \(n=4\) 并取 Yamabe 代表，得到 \(W^+=0\)、\(s>0\)，故
\[
\mathcal E=1.
\]
结合 \(T_+=0\) 的单位墙，
\[
\boxed{
\alpha(\#4\overline{\mathbb {CP}}^{2})=1
}
\]
且被达到。

该流形满足 Hitchin–Thorpe 等号
\[
2\chi=3|\tau|=12.
\]
Einstein 等号情形只能是平坦型或有限覆盖为 K3 的 Ricci-flat 半共形平坦型；\(\#4\overline{\mathbb {CP}}^{2}\) 单连通且交叉形式为奇型 \(-I_4\)，两者均不可能。

给定论文的 Theorem 1.3 还说明：这些 \(n=4\) 的正标量 self-dual 度量不可能有非负 Ricci operator，因为该定理的非乘积分支只允许 \(n\le3\)。

### 4. K3 与 \(T^4\)

Ricci-flat 时
\[
T_\pm=\frac1{2\pi^{2}}\int|W^\pm|^{2}\ge0.
\]
对 K3 取复定向，
\[
T_+=2\cdot24+3(-16)=0.
\]
对 \(T^4\)，\(T_+=T_-=0\)。故
\[
\alpha(K3)\ge1,\qquad \alpha(T^4)\ge1,
\]
尽管它们存在 Ricci-flat Einstein 度量；这些度量的 \(\mathcal E\) 值是 \(4\)，不是 \(0\)。

对 \(T^4\)，若存在 \(W^+=0\) 的度量，则 \(\tau=0\) 的 signature 公式还推出 \(W^-=0\)，所以该度量实际局部共形平坦。关于此类共形结构是否必为平坦型，给定材料没有文献支撑。

### 5. ASD 常标量曲率公式

在
\[
M=k\overline{\mathbb {CP}}^{2}\#\ell(S^1\times S^3)
\]
上，
\[
\chi=2+k-2\ell,\qquad \tau=-k.
\]
设
\[
m=k+4\ell-4,\qquad
y=\frac{Y^2}{32\pi^2},
\]
并取 \(W^+=0\)、非零常标量曲率度量。计算给出
\[
P=\frac{8\pi^2}{3}(3m+y),
\qquad
R=\frac{8\pi^2}{3}(3m+4y).
\]
因此
\[
\boxed{
\mathcal E
=\frac{4(3m+y)}{3m+4y}
=1+\frac{9m}{3m+4y}.
}
\]
该公式正确。几何可实现的数据还满足
\[
y>0,\qquad 3m+y\ge0,\qquad 3m+4y>0.
\]
当共形类为正 Yamabe 类时，Aubin 上界给出 \(y\le12\)；对于 Yamabe 常数为负的类，不能从 Aubin 上界推出 \(y\le12\)。

---

## 五、Theorem 71.D：长圆周储库

该构造在固定连通和区域的理解下成立。

设 \(Y\) 为截面曲率 \(c=\pm1\) 的闭三流形，\(q=\operatorname{vol}(Y)\)。在
\[
Q_L=S^1_L\times Y
\]
上，
\[
s_0=6c,\qquad W=0,\qquad R(Q_L)=12Lq.
\]

在一个半径固定、与 \(L\) 无关的小球内完成与 \(N\) 的连通和。对所有充分大的 \(L\)，该球的局部几何完全相同。固定一次缩放参数和 neck 度量，使整个替换区域 \(J\) 与 \(L\) 无关。四维中
\[
\int|\operatorname{Ric}|^{2},\quad
\int|W^\pm|^{2},\quad
\int s^{2}
\]
在常数缩放下不变，因此 \(J\) 上这些量均为 \(O(1)\)。

于是
\[
V_L=Lq+O(1),\qquad
T_s=s_0Lq+O(1),
\]
从而
\[
\bar s=s_0+O(L^{-1}).
\]
乘积区域对标量方差的贡献为
\[
O(L)\cdot O(L^{-2})=O(L^{-1}),
\]
而固定区域 \(J\) 上
\[
\int_J(s-\bar s)^2=O(1).
\]
故
\[
L_s=O(1).
\]
同时
\[
R(g_L)=12Lq+O(1),\qquad
\int|W^+_{g_L}|^{2}=O(1).
\]
拓扑数 \(T_+\) 与 \(L\) 无关，因此 Identity 71.1 给出
\[
\mathcal E(g_L)=1+O(L^{-1}).
\]
所以
\[
\boxed{
\alpha\bigl(N\#(S^1\times Y)\bigr)\le1.
}
\]

这里无需让缩放参数随 \(L\) 变化；固定它即可。这样 neck 的所有曲率平方积分自动一致有界。

### 多柄结论

因为
\[
T_\pm\bigl(N\#\ell(S^1\times S^3)\bigr)
=T_\pm(N)-4\ell,
\]
若
\[
\min(T_+(N),T_-(N))\le4\ell,
\]
则结果流形的某个 Hitchin–Thorpe 数不正。单位墙给出 \(\alpha\ge1\)，储库给出 \(\alpha\le1\)，故
\[
\boxed{\alpha=1.}
\]

达到性精确为：

- 若相应的较小 \(T\) 严格小于零，则每个度量都有 \(\mathcal E>1\)，所以值 \(1\) 不被达到；
- 若该 \(T=0\)，则达到值 \(1\) 等价于存在相应半 Weyl 张量消失且 Yamabe 常数非零的共形类。

### 一般型曲面的 \(h\)-公式

设
\[
h=\frac{k+4\ell}{A},\qquad \ell\ge1.
\]
结合先前的恢复构造，
\[
\alpha\le
\min\left\{1,\frac{4h}{1+h}\right\}.
\]
若 \(h\ge1\)，则 \(T_+=A-k-4\ell\le0\)，所以
\[
\boxed{h\ge1\Longrightarrow\alpha=1.}
\]
若 \(h>1\)，该值不被达到；若 \(h=1\)，达到性仍由半共形平坦 Yamabe 类决定。

反向等价目前不能写成
\[
\alpha=1\iff h\ge1.
\]
现有估计只能进一步给出：

- \(h<1/3\) 时，\(\frac{4h}{1+h}<1\)，故 \(\alpha<1\)；
- \(1/3\le h<1\) 时，给定上下界仍允许 \(\alpha=1\) 或 \(\alpha<1\)。

---

## 六、Lemma 71.T 与 Step 59 的 \(\alpha\)-解释

### 1. \(P\) 与 \(\mathcal E\)

对于 \(R>0\)，
\[
\mathcal E=\frac{4P+L_s}{R}\ge\frac{4P}{R}.
\]
若 \(\widehat g\) 为非零 Yamabe 常数的常标量曲率度量，则
\[
R=P+\frac{Y^2}{4},
\]
故
\[
\boxed{
\mathcal E(\widehat g)
=\frac{16P}{4P+Y^2}.
}
\]
在 \(\lambda=s/4\) 处代入仅得到
\[
\frac{16P}{Y^2},
\]
它通常严格大于真正的 \(\lambda\)-下确界。

因此 Yamabe 序列上
\[
\mathcal E\to0
\iff
\frac{P}{Y^2}\to0.
\]
仅有 \(P\to0\) 不足以推出 \(\mathcal E\to0\)。

### 2. 最优 Einstein 尺度归一化

当 \(T_s\ne0\) 时，
\[
\lambda_{\rm opt}=\frac{R}{T_s}.
\]
通过常数缩放可以统一归一化为
\[
\lambda_{\rm opt}=\sigma,\qquad \sigma\in\{+1,-1\}.
\]
于是
\[
T_s=\sigma R,\qquad
R=(4-\mathcal E)V.
\]
原文只写 \(\lambda_{\rm opt}=1\)，这只覆盖总标量曲率为正的情形。

若 \(\mathcal E\le1-\eta\)，则不论是否先归一化，
\[
(1-\mathcal E)R
=24\pi^{2}T_+-12\int|W^+|^{2}-L_s
\le24\pi^{2}T_+,
\]
从而
\[
R\le\frac{24\pi^{2}T_+}{\eta}.
\]

### 3. Gauss–Bonnet 与整体有界曲率塌缩

设 \(\mathcal E(g_j)\to0\)，并归一化为
\(\lambda_{\rm opt}=\sigma=\pm1\)。则
\[
R=(4-\mathcal E)V,
\qquad
P\le\frac{\mathcal ER}{4}=o(V),
\qquad
L_s\le\mathcal ER=o(V).
\]
又
\[
\bar s=\frac{T_s}{V}
=\sigma(4-\mathcal E),
\]
所以
\[
\int s^{2}
=L_s+\bar s^{\,2}V
=16V+o(V).
\]
代入 Gauss–Bonnet：
\[
\boxed{
8\pi^{2}\chi
=\int|W|^{2}+\frac23V+o(V).
}
\]
因此
\[
V\le12\pi^{2}\chi\,(1+o(1)),
\]
并且这种序列必有 \(\chi>0\)。

若进一步在该归一化下
\[
|\operatorname{Rm}|\le\Lambda,\qquad V\to0,
\]
则 \(\int|W|^{2}=O(V)\)，上式右端趋于零，迫使 \(\chi=0\)，与 \(\chi>0\) 冲突。因此整体体积趋零且曲率一致有界的序列不可能同时满足 \(\mathcal E\to0\)。

### 4. Step 59.C

\(\operatorname{MinVol}=0\) 只推出 \(P_*=0\)。有界截面曲率塌缩还推出
\[
\chi=\tau=0,
\]
所以 \(T_+=T_-=0\)，单位墙反而给出
\[
\alpha\ge1.
\]
因此 Step 59.C 不能作为 \(\alpha=0\) 的机制。

这与显式例子一致：

- \(S^1\times S^3/\Gamma\) 和双曲三流形映射环面有 \(\alpha=1\)，且被达到；
- \(S^2\times T^2\) 目前只有 \(1\le\alpha\le2\)；
- Kodaira 曲面的给定材料只给出 \(\alpha\ge1\) 与 \(P_*=0\)。

### 5. Step 59.N

设 Einstein orbifold 的 Einstein 常数为 \(\kappa\)。

若 \(\kappa\ne0\)，标准 ALE 插入估计不仅给出 \(P\to0\)，还给出 neck 上
\[
\int|\operatorname{Rm}|^{2}\to0.
\]
Ricci-flat ALE 核心的标量曲率为零，而 orbifold 主体的标量曲率为 \(4\kappa\)。因此
\[
L_s\to0,\qquad
R\to4\kappa^{2}V_{\rm orb}>0,
\]
从而
\[
\mathcal E\to0.
\]
所以非零 Einstein orbifold 的兼容 ALE-tree 替换确实给出 \(\alpha=0\)。

若 \(\kappa=0\)，则 \(R\to0\)，\(P\to0\) 本身没有提供 \(\mathcal E\) 信息。Kummer–K3 正是这一现象。

### 6. Step 59.Z

对同一个、已按 \(\lambda_{\rm opt}=\pm1\) 归一化的 \(\mathcal E\)-小序列，上述计算证明：

- \(V\) 一致有上界；
- \(P\to0\)；
- 整体体积趋零且曲率一致有界的几何不可能出现。

但 Anderson 的给定定理选择的是 \(P\)-正则化极小序列，不是任意 \(\mathcal E\)-极小序列。由 \(\alpha=0\) 虽可推出 \(P_*=0\)，Anderson 选出的另一条 \(P\)-序列仍可能呈现不同几何。因此，除非有一个紧性定理直接作用于同一条 \(\mathcal E\)-小序列，不能仅凭 Gauss–Bonnet 就把 Anderson 的全部结构直接移植到 \(\alpha\)。

若另有紧性分解适用于该同一序列，则其非塌缩光滑极限必为 Einstein，且 Einstein 常数为非零尺度；这一结论来自
\[
\int|\operatorname{Ric}-\sigma g|^{2}
=\mathcal E\,V\to0.
\]

### 7. \(\mathbb {CP}^{2}\#\mathbb {CP}^{2}\) 的 EH 系数

对 Ozuch 型度量 \(g_a\)，应写成恒等式
\[
\mathcal E(g_a)
=\frac{4P(g_a)+L_s(g_a)}{R(g_a)},
\]
而不是“\(\le\)”。

若已有渐近量
\[
4P(g_a)=8\pi^{2}a^{4}+o(a^{4}),
\qquad
R(g_a)=48\pi^{2}+o(1),
\]
那么只有在进一步证明
\[
L_s(g_a)=o(a^{4})
\]
后，才能得到
\[
\boxed{
\mathcal E(g_a)=\frac{a^{4}}6+o(a^{4}).
}
\]
若 \(L_s=O(a^{4})\)，主系数还包含
\[
\frac{L_s}{48\pi^{2}a^{4}}.
\]
若仅知 \(L_s\to0\)，只能推出 \(\mathcal E\to0\)，不能确定 \(a^{4}/6\) 的系数。

---

## 七、文献归属与所需检索

给定材料足以支持的经典部分包括：

- 四维 Chern–Gauss–Bonnet 与 signature 公式；
- Hitchin–Thorpe 不等式及 Einstein 等号几何；
- Yamabe 代表的存在；
- 半 Weyl 消失时的调和二形式 Weitzenböck 公式；
- Donaldson–Freedman 在单连通定 definite 情形的结论；
- LeBrun hyperbolic ansatz 在每个 \(n\mathbb {CP}^{2}\) 上产生含正标量曲率代表的 self-dual 共形类；
- LeBrun–Nayatani–Nitta Theorem 1.3 关于非负 Ricci operator 的拓扑结论。

相对于给定材料，以下内容是本研究包中的新推导或新组合：

- \(\mathcal E\) 的单位墙等号类及其 Yamabe 达到刻画；
- \(\alpha(\#4\overline{\mathbb {CP}}^{2})=1\) 且被达到；
- 长圆周储库
  \[
  \alpha(N\#(S^1\times Y))\le1;
  \]
- \(P\)-小与 \(\mathcal E\)-小的系统分离；
- Ricci-flat Einstein 度量对应 \(\mathcal E=4\) 而非零点的解释。

仅凭现有材料不能确定这些推导在全部既有文献中的首次出现。适合建立以下 `knowledge_request`：

1. **精确泛函检索**：搜索
   \[
   \inf_{\lambda\ne0}
   \frac{\|\operatorname{Ric}-\lambda g\|_{L^{2}}^{2}}
        {\lambda^{2}\operatorname{Vol}(g)}
   \]
   及其四维 Chern–Weil 下界、\(\mathcal E\ge1\) 和半共形平坦等号类。
2. **长圆周连通和检索**：搜索在 \(N\#(S^1\times Y)\) 上通过 \(S^1\) 长度趋于无穷压低归一化 Ricci–Einstein 缺陷的构造。
3. **\(\#4\overline{\mathbb {CP}}^{2}\) 精确值检索**：搜索该流形上 ASD 正 Yamabe 度量与归一化 Einstein-defect 下确界等于 \(1\) 的既有表述。
4. **Hitchin–Thorpe 等号来源**：补充平坦有限覆盖或 K3 有限覆盖分类的原始定理来源。
5. **\(T^4\) 局部共形平坦结构**：核实闭四环面上的局部共形平坦度量是否必与平坦结构共形。
6. **Ozuch 标量方差**：检索或直接计算适配 EH 度量上的
   \[
   L_s=\int(s-\bar s)^2
   \]
   至 \(a^{4}\) 阶，以确定 \(1/6\) 系数。
7. **\(\mathcal E\)-序列紧性**：检索是否存在直接针对该商泛函极小序列的 Anderson 型 orbifold/cusp 分解定理。