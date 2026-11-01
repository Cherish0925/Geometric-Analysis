# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 81,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step81_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step81_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

On a compact oriented positive Einstein 4-manifold (M⁴, g) with Ric = 3g, s = 12, the Weitzenböck operator L = ∇*∇ - 2W⁺ + (s/3) on self-dual 2-forms has kernel of dimension b_+(M). Every known compact positive Einstein 4-manifold has min(b_+, b_-) ≤ 1. The crude summed-Weitzenböck chain gives Gursky-LeBrun (independent of b_+) with a 22.5% margin for χ=8, τ=0.

Generate mathematically precise conjectures and possible proof strategies for a b_+-DEPENDENT Weyl energy inequality. Specifically:

(A) Is there a spectral-theoretic argument (CLR, heat kernel, zeta function, Selberg-type) that bounds N_0(L) in terms of the negative-part integral ∫(2α-4)_+^n for appropriate n, with constants that depend on the Yamabe constant Y = 12√V, leading to ∫|W+|² ≥ f(b_+)·V with f(3) > 9?

(B) Is there an argument using the determinant of the Gram matrix G_ab(x) = ⟨ω_a(x), ω_b(x)⟩ of three harmonic SD forms? On a non-symplectic manifold, no form can be everywhere nonzero. The determinant det G measures the 'volume' of the harmonic forms in Λ⁺. Does Einstein rigidity constrain det G in a way that forces ∫|W+|² to be large?

(C) Is there a Bochner/Berger-type argument using the tensor T = Σ ω_a ⊗ ω_a directly? For b_+=3, T is a symmetric endomorphism of Λ⁺ with ∫trT = 3. Does T satisfy a useful PDE (from the individual Weitzenböck equations) that constrains its pointwise eigenvalue distribution?

(D) Is there an obstruction from mod-2 or integral characteristic classes, spin structures, or index theory that prevents positive Einstein metrics with b_+ ≥ 2 more directly?

For each direction, give the precise mathematical formulation and identify the decisive step that would need to be proved. Do not fabricate literature references.

## Integrated Scientific Memo

## 结论与统一记号

令
\[
L=\nabla^*\nabla-2W^++4I,\qquad B=2W^+-4I,
\]
其中 \(W^+\) 的特征值记为
\[
\alpha\ge \beta\ge \gamma,\qquad \alpha+\beta+\gamma=0,
\]
并置
\[
q=(2\alpha-4)_+.
\]
则
\[
\ker L=\mathcal H_g^+,\qquad \dim\ker L=b_+(M).
\]

目标是得到
\[
\int_M|W^+|^2\,dV\ge f(b_+)V,\qquad f(3)>9.
\]
对 \((\chi,\tau)=(8,0)\)，Chern–Gauss–Bonnet 给出
\[
\int|W^+|^2=32\pi^2-3V,\qquad V\le \frac{8\pi^2}{3},
\]
所以任何严格的 \(f(3)>9\) 都排除这类正 Einstein 度量。现有求和 Weitzenböck 链只给出
\[
\int|W^+|^2\ge 6V,
\]
且 \(b_+\) 完全消去；因此必须加入真正控制多个零模相互作用的新信息。

以下给出四条精确的研究命题，并纠正若干容易误用之处。

---

# A. 谱论路线

## A.1 必须计数的是非正谱，而不只是负谱

标准 CLR 通常控制负特征值数
\[
N_-(L)=\#\{\lambda_j(L)<0\},
\]
但本题需要控制
\[
N_{\le0}(L)=N_-(L)+\dim\ker L=b_+,
\]
因为 \(L\ge0\) 且所有相关态恰好位于阈值 \(0\)。

因此所需定理不能只是普通 CLR；它必须是下列之一：

1. 一个直接的阈值估计；
2. 对 \(L-\varepsilon\) 应用 CLR，并证明 \(\varepsilon\downarrow0\) 时常数和右端稳定；
3. Birman–Schwinger 算子在阈值 \(1\) 处的计数估计。

这是该路线的第一个决定性技术点。

## A.2 标量阱猜想

最直接的定理形状是：

> **Einstein 阈值-CLR 猜想。** 对所有 \(b_+\ge2\) 的闭正 Einstein 四流形，
> \[
> b_+(M)\le C_{\rm E}\,Y^{-2}\int_M(2\alpha-4)_+^2\,dV,
> \qquad Y=12\sqrt V.
> \tag{A-CLR}
> \]

这里指数 \(2=n/2\) 是四维临界指数。由
\[
q^2\le 4\alpha^2\le \frac83|W^+|^2
\]
可得
\[
\int|W^+|^2
\ge \frac38\,\frac{b_+Y^2}{C_{\rm E}}
=\frac{54}{C_{\rm E}}\,b_+V.
\]
所以
\[
f(b_+)=\frac{54}{C_{\rm E}}b_+,
\]
而 \(b_+=3\) 时只需
\[
\boxed{C_{\rm E}<18.}
\]

若证明只能控制 \(b_+-1\)，则
\[
\int|W^+|^2\ge \frac{54}{C_{\rm E}}(b_+-1)V,
\]
在 \(b_+=3\) 时需 \(C_{\rm E}<12\)。

不能简单声称 \(b_+\ge2\) “消除了 CP\(^2\) 的自由 Kähler 零模”，从而自动得到 \(b_+\) 而非 \(b_+-1\)：无平行 SD 形式只排除了平行阈值态，并未排除一般的非平行零模。阈值计数仍需单独证明。

## A.3 矩阵势版本

令 \(B_+\) 为 \(B\) 的正谱部分。更内禀的猜想为
\[
b_+\le C_{\rm mat}Y^{-2}\int\operatorname{tr}(B_+^2)\,dV.
\tag{A-mat}
\]
由于
\[
\operatorname{tr}(B_+^2)
=\sum_{\mu\in\{\alpha,\beta,\gamma\}}(2\mu-4)_+^2
\le 4|W^+|^2,
\]
得到
\[
\int|W^+|^2\ge \frac{36}{C_{\rm mat}}\,b_+V.
\]
因此 \(b_+=3\) 时充分条件是
\[
\boxed{C_{\rm mat}<12.}
\]

矩阵版本可能比用最大特征值 \(q\) 更自然，但通常带有秩损失，常数门槛更苛刻。

## A.4 可行证明框架及其瓶颈

### Birman–Schwinger

由二次型比较
\[
L=\nabla^*\nabla-B\ge \nabla^*\nabla-qI
\]
可把零模子空间视为标量 Schrödinger 二次型的非正子空间。所需关键结论是一个紧流形临界 CLR：
\[
N_{\le0}(\nabla^*\nabla-q)
\le C_{\rm E}Y^{-2}\int q^2,
\]
且 \(C_{\rm E}<18\)。

难点是常数函数导致 \(\nabla^*\nabla\) 本身有零模；必须利用 \(+4\)、无平行 SD 截面、均值零条件或正移位的 Green 核，而不能直接套用无质量逆算子。

### 热核

Yamabe–Sobolev 不等式
\[
Y\|u\|_4^2\le 6\int|\nabla u|^2+12\int u^2
\]
可导出带质量热核估计，再配合 Kato 支配。决定性问题不是是否能得到某个有限常数，而是：

\[
\boxed{\text{能否在阈值计数后仍保持 }C_{\rm E}<18\text{ 或 }C_{\rm mat}<12?}
\]

普通热核/CLR 常数很可能过大，因此真正有希望的版本必须利用 Einstein 势并非任意势，而满足
\[
\delta W^+=0
\]
及相应的 Einstein–Weyl 椭圆方程。

### ζ 函数

形式上
\[
\zeta_L(0)+b_+=a_4(L),
\]
但这本身不是计数不等式。\(a_4(L)\) 可写成局部曲率积分；真正缺少的是统一的下界
\[
\zeta_L(0)\ge -\Psi\!\left(Y^{-2}\int|W^+|^2\right).
\]
谱 ζ 在 \(0\) 处没有显然符号，因此这条路线只有在建立这种 Einstein 类统一估计后才有效。

### Selberg 型方法

一般闭 Einstein 四流形没有可用的轨道迹公式；除非额外假设局部对称或算术商结构，Selberg 方法并非普适路线。它更适合作为对对称模型计算最佳常数的校准工具，而非一般证明。

## A.5 “超额能量”强化

若能证明
\[
\int q^2\le c_0\left(\int|W^+|^2-6V\right),
\tag{A-excess}
\]
则与 (A-CLR) 联立得到
\[
\int|W^+|^2
\ge\left(6+\frac{144}{c_0C_{\rm E}}b_+\right)V.
\]
不过现有逐点代数至多控制正部：
\[
q^2\lesssim (|W^+|^2-6)_+,
\]
而不能把它替换成全局有符号超额。因此决定性新定理是 Einstein–Weyl 的非振荡估计
\[
\int(|W^+|^2-6)_+
\le \Lambda\left(\int|W^+|^2-6V\right).
\]

---

# B. Gram 行列式路线

取 \(L^2\)-正交归一基 \(\{\omega_a\}_{a=1}^3\)，定义
\[
\Omega_x:\mathbb R^3\to\Lambda_x^+,\qquad
\Omega_xe_a=\omega_a(x),
\]
\[
G=\Omega^*\Omega,\qquad T=\Omega\Omega^*.
\]
于是
\[
\det G=\det T=(\det\Omega)^2.
\]

若 \(\det G>0\) 处处成立，则每个非零 \(u\in\mathbb R^3\) 对应的
\[
\omega_u=\sum u_a\omega_a
\]
都是处处非零的闭自对偶二形式，因而是辛形式。因此在“不承载辛形式”的假设下，每个方向 \(u\in\mathbb RP^2\) 必须至少有一个零点。

但“每个方向有零点”本身只是定性事实，不能给出 Weyl 能量下界；零集可能很细，也可能形成三团集中极限。

## B.1 Gram 方程

取函数 Laplacian 约定使
\[
\frac12\Delta |\omega|^2
=\langle\nabla^*\nabla\omega,\omega\rangle-|\nabla\omega|^2.
\]
令
\[
K_{ab}=\langle\nabla\omega_a,\nabla\omega_b\rangle.
\]
由 \(\nabla^*\nabla\omega_a=B\omega_a\) 得
\[
\boxed{\frac12\Delta G=\Omega^*B\Omega-K.}
\tag{B-G}
\]

在 \(G>0\) 区域，
\[
\frac12\Delta\log\det G
=
\operatorname{tr}B-\operatorname{tr}(G^{-1}K)
+\frac12\sum_i
\operatorname{tr}\!\left(
G^{-1}\nabla_iG\,G^{-1}\nabla_iG
\right).
\]
因 \(\operatorname{tr}B=-12\)，
\[
\boxed{
\frac12\Delta\log\det G
=-12-\operatorname{tr}(G^{-1}K)+\frac12|\nabla G|_G^2.
}
\tag{B-det}
\]

最后两个导数项没有固定相对符号；故不能仅对 \(\log\det G\) 使用最大值原理便得到矛盾。此外 \(\log\det G\) 在退化集趋于 \(-\infty\)，积分分部必须控制其奇性边界项。

## B.2 正确的定量猜想

置
\[
\delta=\frac{3(\det G)^{1/3}}{\operatorname{tr}G}\in[0,1].
\]
\(\delta=1\) 表示点态各向同性，\(\delta=0\) 表示评价映射降秩。

所需定理应是：

> **Gram 退化代价猜想。** 对 \(b_+=3\) 且无辛调和方向的正 Einstein 四流形，Gram 方程 (B-G) 与所有方向零点条件共同蕴含一个统一正下界
> \[
> \mathcal E_{\rm deg}(G)\ge c_0>0,
> \]
> 其中 \(\mathcal E_{\rm deg}\) 能进一步控制
> \[
> K=\int|\nabla\Omega|^2
> \quad\text{或}\quad
> \int (\operatorname{tr}T)^2
> \operatorname{tr}\!\left(\frac{T}{\operatorname{tr}T}-\frac I3\right)^2.
> \]

决定性步骤是证明“全方向零点”具有定量容量或拓扑电荷，足以排除三团近秩一配置；只证明 \(\det G\) 在某处为零远远不够。

## B.3 特征类输入及其限制

有
\[
p_1(\Lambda^+)[M]=2\chi+3\tau.
\]
若 \(\Omega\) 处处可逆，则 \(\Lambda^+\) 平凡，所以该数必须为零。对 \((\chi,\tau)=(8,0)\)，
\[
p_1(\Lambda^+)[M]=16,
\]
故退化必然发生。

但是 \(p_1\) 是四维 Chern–Weil 类，而 \(\det\Omega\) 是实线丛值标量，其零集本身一般不直接代表 \(p_1\)。因此不能把“\(\det\Omega\) 的零点数”等同于 16。所需的新构造应在
\[
M_\varepsilon=\{|\det\Omega|\ge\varepsilon\}
\]
上用 \(\Omega\) 产生 \(\Lambda^+\) 的规范标架，写出连接的 Chern–Simons 边界项，并证明
\[
\lim_{\varepsilon\downarrow0}
\int_{\partial M_\varepsilon}\mathrm{CS}(\Omega)
\]
存在且具有可控符号或下界。没有这一 transgression 定理，特征类只保证退化存在，不提供能量增益。

---

# C. 直接研究 \(T\)

\(T\) 是与调和基选择无关的自然对象。令
\[
u=\operatorname{tr}T=\sum_a|\omega_a|^2,\qquad
P=T/u
\]
（在 \(u>0\) 的区域）。并定义
\[
S=\sum_i(\nabla_i\Omega)(\nabla_i\Omega)^*\ge0.
\]

## C.1 精确 PDE

由各 \(\omega_a\) 的方程得到
\[
\boxed{\nabla^*\nabla T=BT+TB-2S.}
\tag{C-T}
\]
取迹：
\[
\boxed{\frac12\Delta u=\operatorname{tr}(BT)-|\nabla\Omega|^2.}
\tag{C-u}
\]
积分后
\[
K+12=2\int\langle W^+,T\rangle,\qquad
K:=\int|\nabla\Omega|^2,
\]
因为 \(\int u=3\)。

将 \(T=uP\) 代入可得漂移–反应方程
\[
\nabla^*\nabla P-2\nabla_{\nabla\log u}P
=
BP+PB-2\operatorname{tr}(BP)P
-2u^{-1}\bigl(S-\operatorname{tr}S\,P\bigr).
\tag{C-P}
\]
真正困难的项是最后的无迹部分；它没有先验有利符号，不能未经证明便声称它“把 \(P\) 推离秩一边界”。

## C.2 精确的各向异性归约

置
\[
\psi^2=\operatorname{tr}(P-I/3)^2
=\operatorname{tr}(P^2)-\frac13,\qquad
0\le\psi^2\le\frac23.
\]
因 \(W^+\) 无迹，
\[
\langle W^+,T\rangle
=u\langle W^+,P-I/3\rangle
\le u|W^+|\psi.
\]
因此
\[
K+12
\le
2\left(\int|W^+|^2\right)^{1/2}
\left(\int u^2\psi^2\right)^{1/2}.
\]
定义
\[
\Theta_T=\frac{V}{9}\int u^2\psi^2\,dV.
\]
则
\[
\boxed{
\frac1V\int|W^+|^2
\ge \frac{(K+12)^2}{36\Theta_T}.
}
\tag{C-energy}
\]

这给出了最精确的 \(T\)-路线目标：

> **张量各向异性猜想。**
> \[
> \boxed{\frac{(K+12)^2}{36\Theta_T}>9}
> \]
> 对所有 \(b_+=3\) 的正 Einstein 四流形成立。

等价地，
\[
K>18\sqrt{\Theta_T}-12.
\tag{C-target}
\]

必须注意：\(\Theta_T\) 不只测量 \(P\) 的各向异性，也包含 \(u\) 的 \(L^2\) 集中。由 Jensen 只能得到 \(\int u^2\ge 9/V\)，没有统一上界；因此 \(\Theta_T\) 并不以 \(2/3\) 为全局上界。所谓“最坏秩一值 \(\Theta_T=2/3\)”只在 \(u\equiv3/V\) 时成立。三团集中恰好可使 \(P\) 近秩一且 \(\int u^2\) 很大，是现有链条的核心障碍。

因此一个充分且正确的定理必须同时控制：

1. **集中度**
   \[
   \kappa^2=\frac{V\int u^2}{9};
   \]
2. **各向异性**
   \[
   \frac{\int u^2\psi^2}{\int u^2};
   \]
3. **梯度能**
   \[
   K.
   \]

可精确表述为
\[
\boxed{
K+12>6\sqrt{A_0\,V\int u^2\psi^2}
}
\]
并取 \(A_0=9\)；或直接证明 (C-target)。

## C.3 最大值信息

在 \(u\) 的最大点，由 (C-u)
\[
\operatorname{tr}(BT)\ge |\nabla\Omega|^2\ge0,
\]
从而
\[
\langle W^+,P\rangle\ge2.
\]
这说明最大密度处必须向 \(W^+\) 的高特征方向对齐，但只是单点信息。决定性 Berger 型定理应将其传播为正测度结论，例如：

\[
\operatorname{Vol}\bigl\{x:
\alpha(x)\ge2+\eta,\ 
\operatorname{tr}P(x)^2\le1-\eta
\bigr\}
\ge cV,
\]
或等价的加权积分估计。证明需要对耦合系统 (C-u)、(C-P) 建立 Harnack、频率函数或矩阵最大值原理。

---

# D. 特征类、spin 与指标理论

## D.1 现有标准障碍不够

正 Einstein 蕴含正标量曲率。

- 若 \(M\) spin，Lichnerowicz 给出
  \[
  \hat A(M)=-\tau/8=0,
  \]
  即 \(\tau=0\)，但这允许 \(b_+=b_-\ge2\)。

- Hitchin–Thorpe
  \[
  2\chi\ge3|\tau|
  \]
  对 \((8,0)\) 没有排除作用。

- 普通 Seiberg–Witten 不变量在正标量曲率下消失，也不能区分正 Einstein 与一般正标量度量。

- 
  \[
  p_1(\Lambda^+)[M]=2\chi+3\tau
  \]
  强迫调和评价框架退化，却不直接提供 Weyl 能量增益。

因此目前没有纯粹的 mod-2、spin 或标准指标障碍能直接排除 \(b_+\ge2\)。

## D.2 合理的新指标命题

所需对象应是自然椭圆算子 \(\mathcal D\)，满足：

\[
\mathcal D^*\mathcal D
=\nabla^*\nabla+\mathcal R_0+\mathcal R(W^+),
\]
其核或指标真正检测 \(H_g^+\)，并有
\[
\operatorname{ind}\mathcal D
=c_1b_++c_2\chi+c_3\tau.
\]
若其曲率项可在 \(\int|W^+|^2\) 小于某阈值时证明正定，就会产生所需不等式。

在 spin 情形可研究
\[
\Lambda^+\cong \operatorname{Sym}^2S^+
\]
相关的 twisted Dirac 或 Rarita–Schwinger 型算子。但决定性步骤不是计算一个新指标公式，而是证明：

1. \(H_g^+\) 自然注入该算子的核，或迫使其核维数增长；
2. Weitzenböck 曲率项只由 \(W^+\) 的“吸引部分”控制；
3. 指标下界不是被余核抵消。

没有这三点，指标只重述 \(\chi,\tau\)，不会得到 \(b_+\)-依赖的新信息。

---

# 最值得检验的三个核心命题

## 1. 阈值 Einstein–CLR

\[
b_+\le C_{\rm E}Y^{-2}\int(2\alpha-4)_+^2,\qquad C_{\rm E}<18.
\]

**决定性步骤：** 对非正谱而非仅负谱建立紧 Einstein 四流形临界 CLR，并保持门槛常数。

## 2. \(T\) 的浓度–各向异性不等式

\[
\frac{(K+12)^2}{36\Theta_T}>9,\qquad
\Theta_T=\frac V9\int u^2\operatorname{tr}(P-I/3)^2.
\]

**决定性步骤：** 从 (C-P) 证明三团、近秩一、高浓度配置必然付出足够大的 \(K\)，或不能满足 Einstein 耦合方程。

## 3. 调和框架退化的定量 transgression

利用
\[
p_1(\Lambda^+)[M]=2\chi+3\tau
\]
和 \(\Omega\) 在 \(\{\det\Omega\ne0\}\) 上给出的规范标架，证明退化集携带可量化的 Chern–Simons 边界能，并将其转化为对 \(K\)、\(\Theta_T\) 或 \(\int|W^+|^2-6V\) 的正下界。

**决定性步骤：** 控制 \(\det\Omega\to0\) 时的奇性边界项，并证明其不能通过三团集中无代价实现。

总体上，谱路线给出了最清晰的数值门槛；\(T\)-方程给出了最精确的几何未知量；Gram/特征类路线最可能解释为何三团配置在精确 Einstein 方程下不可能，但目前缺少的正是定量退化电荷定理。