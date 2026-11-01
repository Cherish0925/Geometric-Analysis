# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 2,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step2_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step2_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Yau Problem 26 asks whether for each dimension n, there exist dimension-only constants c_n < C_n such that any closed connected smooth Riemannian n-manifold (M,g) with c_n g ≤ Ric_g ≤ C_n g admits an Einstein metric h on M. The problem decomposes into positive and negative branches P_n^+ and P_n^-. Through quantitative Chern-Weil analysis combined with Seiberg-Witten theory, the positive branch in dimension 4 is strongly protected: all known no-Einstein 4-manifolds have δ_+ bounded away from 0 (HT-violating: δ_+ ≥ 0.366; LeBrun SW-obstructed: δ_+ ≥ 1 since no positive scalar curvature). The NEGATIVE branch is the live territory. For LeBrun manifolds M = X#k CPbar² with A = c₁²(X), combining LeBrun's ∫s²dV ≥ 32π²A with CGB volume bounds gives δ_- ≥ C/√A for varying manifolds with A→∞, which tends to 0. So varying-manifold counterexamples are not ruled out by current integral bounds. The central unsolved problems are: (A) Can tight two-sided negative Ricci pinching (Ric ≈ -g in operator norm) be constructed on manifolds with no Einstein metric? Lohkamp gives one-sided Ric < 0 flexibility and h-principle for open relations, but not two-sided bounds. DeTurck prescribed-Ricci is local. Min-Oo/Jäckel need additional conditions (d²max|K| bounded or sec < 0). (B) Alternatively, can a new existence theorem work with ONLY Ricci pinching, without full curvature/derivative/diameter control? All known existence theorems require more than Ricci. Propose genuinely new mathematical mechanisms, constructions, or proof strategies that could resolve either direction. For a counterexample mechanism: how could one construct a metric with all Ricci eigenvalues in (-1-ε, -1+ε) on a LeBrun manifold with the Weyl curvature free? For an existence mechanism: what new analytic, variational, or topological principle could extract Einstein existence from pure Ricci pinching, possibly through a new flow, functional, or topological constraint?

## Integrated Scientific Memo

# 科学整合备忘：负支的可检验构造机制与纯 Ricci 存在机制

## 1. 先校正两个决定路线的事实

### 1.1 原题只需一支成立

已有严格归约是
\[
Q_n\Longleftrightarrow P_n^+\vee P_n^-.
\]
因此：

- 证明任意一支即可证明该维数的原题；
- 否定原题必须在同一固定维数同时否定正、负两支；
- 构造 LeBrun 型负支反例只会否定 \(P_4^-\)，不会否定 \(Q_4\)。

### 1.2 LeBrun 临界尺度是 \(\sqrt{\eta}\)，不是 \(\eta\)

令
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad
A=c_1^2(X),\qquad
k=\Bigl(\frac23+\eta\Bigr)A.
\]
给定材料中的组合不等式为
\[
8\pi^2\Bigl(k-\frac{2A}{3}\Bigr)
\le
4\delta^2\,
\frac{4\pi^2(A-k)}
{\frac23(1-\delta)^2-2\delta^2}.
\]
当 \(\delta\to0\) 时，
\[
\delta^2\ge
\frac{k-2A/3}{3(A-k)}+o(1)
=
\frac{\eta}{1-3\eta}+o(1),
\]
故
\[
\boxed{\delta\gtrsim\sqrt{\eta}}.
\]
所以目标误差为 \(\varepsilon\) 时必须选
\[
k-\frac{2A}{3}=O(\varepsilon^2A),
\]
这支持第一分支的参数尺度，否定了第二分支提出的线性估计
\(\delta\gtrsim \frac32\eta\)。

最靠近临界值的整数选择使 \(k-2A/3=O(1)\)，于是
\[
\delta\gtrsim A^{-1/2}.
\]
这只是必要下界，不是可达性定理。

---

## 2. 四维纯 Ricci 夹逼确有拓扑体积上界，但不能推出跨流形紧性

由
\[
2\chi\pm3\tau
=\frac1{4\pi^2}\int
\left(2|W^\pm|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)dV
\]
和 \(\delta_\sigma(g)\le\varepsilon\)，有
\[
|s|\ge4(1-\varepsilon),\qquad |E|^2\le4\varepsilon^2.
\]
因此
\[
2\chi\pm3\tau\ge
\frac{\Vol(M,g)}{4\pi^2}
\left[\frac23(1-\varepsilon)^2-2\varepsilon^2\right],
\]
从而在括号为正时
\[
\boxed{
\Vol(M,g)\le
\frac{4\pi^2(2\chi\pm3\tau)}
{\frac23(1-\varepsilon)^2-2\varepsilon^2}
}.
\]
所以“负支没有 Bishop–Gromov 体积上界”是对的，但四维固定拓扑下仍有 Chern–Weil 体积上界。

同样，由
\[
\int|W^\pm|^2
=
2\pi^2(2\chi\pm3\tau)
-\frac1{48}\int s^2
+\frac14\int|E|^2
\]
得到固定拓扑下的 Weyl \(L^2\) 上界。

但这不能支持“若 \(P_4^+\) 失败，则自动得到统一曲率能量和轨形紧性”。反例序列允许 \(M_j\) 改变，\(\chi(M_j)\) 可以无界；即使拓扑固定，现有有界-Ricci正则性通常还需非塌缩等条件。Myers 只给直径上界和有限基本群，不给体积或注入半径正下界。

此外，所给来源中的 LeBrun–Ozuch 定理仅适用于**输入本身已经是正 Einstein 度量**、极限具有真奇点且 ALE 泡满足特定反自对偶条件的序列。它不能用于一般“近 Einstein”输入的分类，更不能推出所有可能的光滑消解都是 del Pezzo 或都承载 Einstein 度量。因此正支“非塌缩部分几乎由现有结果完成”的说法目前没有依据。

---

## 3. 负支反例最具体的构造目标：有限尺度 \(\overline{\mathbb{CP}}^2\) 负 Einstein 插件

一个可复算的基底是
\[
X_{p,q}=\Sigma_p\times\Sigma_q,
\]
两因子取曲率 \(-1\)。乘积度量满足 \(\Ric=-g\)，并且
\[
A=c_1^2(X_{p,q})=8(p-1)(q-1),\qquad
\Vol(X_{p,q})=2\pi^2A.
\]
取
\[
k=\left\lceil \frac23A+c\varepsilon^2A\right\rceil,
\]
则 \(X\#k\overline{\mathbb{CP}}^{\,2}\) 位于 LeBrun 无 Einstein 区域，并与上述必要尺度相容。

真正需要构造的是
\[
P=\overline{\mathbb{CP}}^{\,2}\setminus B^4
\]
上的一族度量 \(p_\varepsilon\)，满足：

1. **全插件双边夹逼**
   \[
   \|\Ric_{p_\varepsilon}+p_\varepsilon\|_{\op}\le\varepsilon;
   \]

2. **边界 Cauchy 数据匹配**
   \[
   \|\gamma_\varepsilon-\gamma_{\rm bg}\|_{C^2}
   +\|K_\varepsilon-K_{\rm bg}\|_{C^1}
   \le C\varepsilon,
   \]
   其中背景数据来自基底中待删除球面的边界；

3. **插值环仍满足**
   \[
   \|\Ric+g\|_{\op}\le C\varepsilon;
   \]

4. **每个插件的净体积代价受控**，不能靠长度趋于无穷的负曲率漏斗获得边界匹配，否则 \(k\asymp A\) 个插件会破坏 Chern–Weil/Seiberg–Witten 体积账本。

Ricci-flat ALE 泡不是直接插件：相对于目标 \(\Ric=-g\)，其缺陷为数量级 \(1\)。更合适的候选是拓扑为负线丛盘丛、内部精确满足负 Einstein 方程的 bolt 型模型。可在双轴 Bianchi IX ansatz
\[
p=dt^2+a(t)^2(\sigma_1^2+\sigma_2^2)+b(t)^2\sigma_3^2
\]
中做有限维检验。bolt 光滑条件为
\[
a(0)=a_0>0,\quad a'(0)=0,\quad b(t)=t+O(t^3),
\]
外边界 \(t=T\) 的 Berger 数据为
\[
\gamma_T=a(T)^2(\sigma_1^2+\sigma_2^2)+b(T)^2\sigma_3^2,
\]
主曲率为
\[
a'(T)/a(T),\qquad b'(T)/b(T).
\]
最小判别问题是能否在有限 \(T\) 达到
\[
\frac{b(T)}{a(T)}=1+O(\varepsilon),\qquad
\frac{a'}a-\frac{b'}b=O(\varepsilon),
\]
同时匹配平均曲率、尺度和净体积。若相空间中存在与目标圆球 Cauchy 数据保持正距离的障碍，则这一最简单插件机制被排除；若误差可趋零且体积有界，则它几乎直接给出 \(P_4^-\) 的反例框架。

这里不应把具体 AdS/Pedersen 模型的拓扑和参数范围当作已经核准的事实；给定来源未提供这些定理。它们目前只是需要逐一验证的候选 ODE 家族。

---

## 4. 插件必须满足近反自对偶的能量账本

在 LeBrun 临界族上，若 \(\delta_-\to0\)，则
\[
\int s^2\ge32\pi^2A,\qquad s^2=16+O(\delta)
\]
迫使
\[
\Vol(M,g)\ge2\pi^2A(1-O(\delta)).
\]
另一方面
\[
\int|W^+|^2
=
2\pi^2(A-k)-\frac1{48}\int s^2
+\frac14\int|E|^2.
\]
取 \(k=2A/3+d\)，可见右端由几个数量级为 \(A\) 的项近乎抵消。任何成功构造都必须使
\[
\int|W^+|^2
\]
落在很小的剩余预算内；换言之，按相应定向它必须是**近反自对偶**的，而不仅仅是 Ricci 近各向同性。

这给插件搜索增加了一个可计算筛选条件：除逐点 Ricci 特征值外，必须同时追踪

\[
\Vol,\quad \int|E|^2,\quad \int|W^+|^2,
\quad 2\chi\pm3\tau.
\]

仅证明每个局部插件的 Ricci 误差小，而不验证这些全局抵消，可能与 Chern–Weil 恒等式不相容。

---

## 5. “相对双边 Lohkamp 原理”的精确版本

最有价值的新构造定理不是笼统的 h-principle，而应具有以下相对形式：

> 对给定紧余维零区域 \(P\)、指定边界 collar 数据及 Chern–Weil 相容的拓扑，存在度量 \(g_\varepsilon\)，在 collar 上保持指定背景，并满足  
> \[
> (-1-\varepsilon)g_\varepsilon
> <\Ric_{g_\varepsilon}<
> (-1+\varepsilon)g_\varepsilon.
> \]

关键不是某个固定背景范数中的
\(\Ric_g-T\) 小，而是误差相对于**输出度量 \(g\)** 的算子范数小。还必须有：

- 输出度量不在局部修正中失去正定或发生不可控各向异性；
- collar 完全固定或有足够高阶匹配；
- 在四维允许 Weyl 承载所需特征数；
- 体积代价不会随 \(\varepsilon^{-1}\) 发散。

现有材料只支持 Lohkamp 的一侧 \(\Ric<0\) 灵活性，不支持上述双侧、相对和统一可比性结论。因而任何“Lohkamp 已近似规定 Ricci，故负支可解”的推断都尚未成立。

---

## 6. 高频“Ricci corrugation”：先做符号层否证测试

设
\[
h_\rho=\rho^2a(x)\cos(\phi(x)/\rho),
\]
则度量的 \(C^0\) 扰动小而二阶曲率效应为 \(O(1)\)。线性化 Ricci 的主符号为
\[
2\sigma_\xi(D\Ric)(h)_{ij}
=
|\xi|^2h_{ij}+\xi_i\xi_j\tr h
-\xi_i\xi^ah_{aj}-\xi_j\xi^ah_{ai}.
\]

不过固定 \(\xi\) 时，该符号的核包含规范方向
\[
h=\xi\odot v,
\]
而在规范商上它本质上是椭圆的。因此“把 Ricci 修正倾倒进 Weyl”并不像 Nash 一阶欠定关系那样自动具有凸积分自由度；高频波首先产生可控的 Ricci 主项，非线性交互和 Bianchi 恒等式才是可能的自由度来源。

可行性必须经过三层检验：

1. 多个波向的符号像能否覆盖所需的 trace-free Ricci 缺陷；
2. 二阶平均应力是否有足够秩，同时不产生不可消除的标量误差；
3. 迭代中能否控制正定性、边界 collar 和无权 \(C^0\) Ricci 误差。

即使成功，预期输出是
\[
\|\Ric+g\|_{\op}\to0,\qquad
|W|\to\infty \ \text{或高频振荡},
\]
这正好通过 Min-Oo 的曲率–直径条件逃逸。失败的核心对象则是一个符号/平均应力的不可达锥；先求出这个有限维代数对象，比直接设计无限迭代更有效。

---

## 7. 对抗性保护机制：全部 monopole classes 是否产生统一间隙

经典单一基本类估计只给出 \(\delta\gtrsim A^{-1/2}\)。吹起后存在符号族
\[
a_\sigma=K_X+\sum_{i=1}^k\sigma_iE_i.
\]
对固定度量的自对偶投影，
\[
2^{-k}\sum_\sigma (a_\sigma^+)^2
=
(K_X^+)^2+\sum_i(E_i^+)^2,
\]
故至少有一个符号满足
\[
(a_\sigma^+)^2\ge
(K_X^+)^2+\sum_i(E_i^+)^2.
\]

真正缺失的引理是：

> 纯点态 Ricci 夹逼是否迫使右侧在所有允许的 Hodge 正子空间上具有比经典估计更大的统一下界？

仅靠交叉形式代数不够，因为度量的 \(H^+\) 子空间可以旋转，许多 \(E_i^+\) 可能同时很小；Ricci 夹逼是否限制这种旋转完全未知。若能证明限制，结合全部 monopole inequalities 可能把 \(A^{-1/2}\) 提升为统一正间隙；若有限维优化仍允许 \(O(A^{-1/2})\)，则说明现有规范理论账本与插件构造相容。

这比未经证明地调用“近等号刚性”更精确：需要的是把点态 Ricci 信息连接到 harmonic projection 的新 Weitzenböck 或定量 Hodge 理论。

---

## 8. 存在方向：普通 Ricci 流的 Weyl 项不会自动消失

令 \(E=\Ric-\frac{s}{n}g\)。归一化 Ricci 流下示意地有
\[
(\partial_t-\Delta)E=2W*E+\text{低阶项}.
\]
虽然 \(W*g=0\)，但 \(W*E\) 对谱宽一般没有符号。必须先做局部代数极值问题：
\[
\sup_{|E|=1,\;W\ {\rm Weyl}}
\big\langle W*E,E\big\rangle .
\]
由于 \(W\) 可任意放大，除非谱宽处发生特殊恒等消去，否则不可能有只依赖维数的最大值原理
\[
(\partial_t-\Delta)\operatorname{osc}(\Ric^\#)
\le-c\,\operatorname{osc}(\Ric^\#)+C\operatorname{osc}^2.
\]
一般曲率作用对 trace-free 对称张量是非零的，因此应预期存在 \(O(|W||E|)\) 的增长例；这需要通过四维代数曲率张量的显式矩阵例子最终核验。若该例子成立，普通 Ricci 流不能仅凭 Ricci pinching 闭合估计。

更合理但仍高度非平凡的候选是规范化四阶流，例如
\[
\mathcal J(g)=\int_M
\left|\Ric_g-\frac{\bar s_g}{n}g\right|^2\,dV_g
\]
或尺度不变版本的梯度流。相较于
\(\int|\Ric+g|^2\)，这一泛函不会错误地把“常数为 \(-1\)”固定为唯一目标，并且其零点是 Einstein 度量。所需新定理必须同时解决：

- diffeomorphism 与尺度规范；
- Weyl 集中导致的有限时间奇性；
- 塌缩和长直径；
- 临界点序列逃逸；
- 从小的 \(L^\infty\) Ricci 缺陷推出流所需的高阶初始控制。

所以四阶流的核心不只是短时抛物性，而是一个只由 Ricci pinching 导出的**全局无能量逃逸原理**。

---

## 9. 泡分析能区分两种负支几何，但目前不能给出全局存在性

若 \(|\Rm|=Q_j\to\infty\) 且按 \(Q_jg_j\) 重标度，则
\[
|\Ric_{Q_jg_j}|_{Q_jg_j}=Q_j^{-1}|\Ric_{g_j}|_{g_j}\to0.
\]
非塌缩光滑吹起极限因此是 Ricci-flat。四维中其 Euler、signature 和边界 \(\eta\)-不变量可形成泡的“电荷账本”。

这将候选构造分成：

1. **有限尺度负 Einstein bolt cells**：拓扑在 \(O(1)\) 曲率尺度承载；
2. **高曲率 Ricci-flat bubbles**：拓扑由 ALE/ALF 型泡树承载。

两者受完全不同的匹配条件控制。ADE \((-2)\)-配置不能直接代表单个 \((-1)\)-吹起，但当前来源不足以证明所有可能 Ricci-flat 泡都排除 \((-1)\)-电荷，更不能由局部泡算术排除远处的 Einstein 度量。要把它变成存在定理，尚需证明纯 Ricci 夹逼序列具有适用的非塌缩、能量量化和完整泡树紧性；这些都不是现有假设的后果。

---

## 10. 最明确的科学分叉

目前最具决定性的两个新数学对象是：

### 构造对象
一个有限体积的相对插件
\[
\left(\overline{\mathbb{CP}}^{\,2}\setminus B^4,p_\varepsilon\right)
\]
满足双边负 Ricci 夹逼、近圆边界 Cauchy 数据、可控净体积和近反自对偶能量预算。它若存在，配合
\[
A\to\infty,\qquad
k=\frac23A+O(\varepsilon^2A)
\]
将给出严格的负支反例机制。

### 保护对象
一个把 Ricci 夹逼连接到全部 monopole classes、Hodge 正子空间或泡电荷的统一不等式，从而证明
\[
\delta_-(g)\ge\varepsilon_0>0
\]
而 \(\varepsilon_0\) 与 \(A\) 无关。现有单类积分估计无法做到这一点。

与此同时，正支的可行存在机制不能建立在尚不存在的近 Einstein 轨形分类上。其真正缺口仍是：如何仅从 Ricci 夹逼处理变化拓扑、塌缩和 Weyl 集中，或发明一个不需要这些紧性输入的全局流/变分原理。Min-Oo 的正确逃逸量是
\[
d^2\max|K|\to\infty,
\]
其中既包括 Weyl 爆破，也包括有界曲率下的直径增长；任何负支理论都必须同时覆盖这两类退化。