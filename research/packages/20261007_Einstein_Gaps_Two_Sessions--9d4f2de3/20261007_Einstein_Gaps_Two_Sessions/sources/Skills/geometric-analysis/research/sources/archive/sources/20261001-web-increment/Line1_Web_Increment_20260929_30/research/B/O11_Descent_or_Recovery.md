# O11：保持集中尺度的实际试验与修正泛函的高频结构

2026-09-29，续研B。本文接续 `o11_field_variations_20260929.md` 和近极小弱驻点工具。未构造低于4的真实恢复序列，也未证明全局最佳系数为4。本轮增加一个能随实际曲率集中自适应的合法变分，以及修正泛函上的精确平衡式；不重复已排除的单手性共形试验。

## 1. 带实际势的resolvent保持临界集中

设g是所选标量曲率s=-4的原平衡族近极小度量。记
\[
Z=\operatorname{Ric}^{\circ},\quad P=\int|Z|^2=O(Q),\qquad
\int|Rm|^2=O(A),\quad Q=Ah,\quad h\to0.
\]

### 引理：无需几何紧性的自适应试验

设B是光滑对称无迹二张量，ξ是任意光滑张量，满足
\[
|B|\le c_*|\xi|,\qquad \int|\xi|^2=O(Q).
\]
定义光滑正势及唯一光滑解
\[
v=(1+|\xi|^2)^{1/2},\qquad
(\nabla^*\nabla+v)H=B.\tag{A1}
\]
则H仍对称无迹，并满足
\[
\|H\|_\infty\le c_*,\quad
\int\bigl(|H|^2+|\nabla H|^2+|\nabla^*\nabla H|^2\bigr)=O(Q),\tag{A2}
\]
\[
\int\bigl(|\nabla^2H|^2+|\nabla H|^4\bigr)=O(A).\tag{A3}
\]
所有常数只使用张量类型、原O(Q)/O(A)常数与c_*，不使用直径、Sobolev、单射半径或ξ的导数界。

**证明。** 正势v≥1保证可逆。rough Laplacian保持对称、无迹子丛。Kato及最大值原理给
\[
(\Delta+v)|H|\le |B|\le c_*v,
\]
故|H|≤c_*。将(A1)与H配对积分，得到
\[
\int(|\nabla H|^2+v|H|^2)=\int\langle B,H\rangle.
\]
因v≥1，\(\|H\|_2\le\|B\|_2=O(\sqrt Q)\)，并有∫|∇H|²=O(Q)。同时
\[
\int v^2|H|^2
=\int|H|^2+\int|\xi|^2|H|^2=O(Q).
\]
由∇*∇H=B−vH即得(A2)最后一项。

有界截面的Hessian分部积分估计为
\[
\int|\nabla^2H|^2
\le C\left(\int|\nabla^*\nabla H|^2
+\|H\|_\infty^2\int|Rm|^2\right).
\]
其证明先对曲率导数项分部积分，再以
\[
\int|\nabla H|^4\le C\|H\|_\infty^2\int|\nabla^2H|^2
\]
及Young吸收。此处不对v或ξ求导。结合(A2)和∫|Rm|²=O(A)得到(A3)。证毕。

固定常数缩放后，H属于既有近极小弱驻点与弱稳定性的允许测试类。

### 实际Weyl预算把(A3)进一步提升到O(Q)

上述一般引理只用了全曲率O(A)，因此其结论(A3)保留不变。原平衡族的实际输入还给出
\[
\xi=(w_3^++w_3^- -1/3)_+,\qquad \int\xi^2=O(Q).
\]
每个三维Weyl块迹为零，最大特征值非负且所有特征值的绝对值不超过其两倍。所以在s=-4上
\[
|Rm|\le C(1+\xi+|Z|).
\]
置e=ξ+|Z|，则∥e∥²₂=O(Q)。对(A1)的H，完整Hessian交换式在分部积分后受
\[
\int|\nabla^*\nabla H|^2
+C\int(1+e)|\nabla H|^2
+C\int(1+e)|H||\nabla^2H|
+C\int(1+e)^2|H|^2
\]
控制。第一项和有界系数乘|H|²、|∇H|²都是O(Q)。含e的项使用H∞≤C与
\[
\|\nabla H\|_4^2\le C\|H\|_\infty\|\nabla^2H\|_2
\]
得到\(C\sqrt Q\|\nabla^2H\|_2\)，Young吸收后也是O(Q)。因此原实际族上的强化结论为
\[
\boxed{\int(|\nabla^2H|^2+|\nabla H|^4)=O(Q).}\tag{A3+}
\]
这个加强没有对ξ、Z或v求导，也不要求选取光滑校准背景。

从联络差公式估计标量平方的二阶变分，使用(A2)、(A3+)及|Ric|≤C(1+|Z|)，进一步得到
\[
|D^2S[H,H]|=O(Q),\qquad
\gamma_jD^2S[H,H]=O(hQ)=o(Q).\tag{A3++}
\]
故这些实际局部化试验上的阈值二阶修正是低阶项。它与一般bulk测试可能具有O(Q)修正并不矛盾：此处H本身的L²质量和临界导数预算都只有O(Q)，而bulk测试可以达到O(A)。

## 2. 两个具体来源

### 2.1 直接无迹Ricci试验

取
\[
\boxed{(\nabla^*\nabla+\sqrt{1+|Z|^2})H_Z=Z.}\tag{A4}
\]
满足引理且c_*=1。它使一个由Z产生的有界试验合法，避免未经证明直接使用H=Z。还具有正的能量配对
\[
\int\langle Z,H_Z\rangle
=\int\left(|\nabla H_Z|^2+\sqrt{1+|Z|^2}|H_Z|^2\right)\ge0.\tag{A5}
\]

### 2.2 实际混合手性试验

对同一未扰动SW解，置ω=iF_A^+、η=iF_A^-，取
\[
B_{ij}=\omega_i{}^k\eta_{jk}+\eta_i{}^k\omega_{jk},\qquad
(\nabla^*\nabla+\sqrt{1+|\eta|^2})H_A=B.\tag{A6}
\]
不同手性保证B对称无迹。实际最大值原理给|ω|≤√2，故|B|≤c_*|η|。原类a²=A−k以及V=2π²A+O(Q)给
\[
\int|\eta|^2
=\int|\omega|^2-4\pi^2a^2
\le2V-4\pi^2(A-k)=O(Q).
\]
于是(A2)–(A3)全部适用。没有截断B，也没有求η的导数。

### 与上轮单位平滑的严格区别

欧氏局部尺度模型中，若
\[
B_\ell(x)=\ell^{-2}\bar B(x/\ell),\qquad
\xi_\ell(x)=\ell^{-2}\bar\xi(x/\ell),
\]
代入x=ℓy，方程变成
\[
(-\Delta_y+\sqrt{\ell^4+|\bar\xi|^2})\bar H_\ell=\bar B.
\]
它没有在源前留下ℓ²因子，因此能够保留O(1)的试验幅度，临界Hessian预算也是尺度不变的。上轮先把源截断为O(1)、再单位平滑时，右侧会带ℓ²，因而压低核心幅度。

这是方程的严格尺度说明，不是新造的实际SW核心；在(A6)中若ω本身消失，B仍可能不能检测核心。直接Z版本(A4)没有这一额外幅度因子。

## 3. 修正泛函上的精确弱平衡

固定0≤α<1，令
\[
c_\alpha=\frac{\alpha}{4(4-\alpha)},\qquad
\mathscr F_\alpha=P-c_\alpha S,\quad S=\int s^2.
\]
在s=-4处，标准曲率变分给
\[
\operatorname{grad}P
=\nabla^*\nabla Z-2Rm(Z)+\tfrac12|Z|^2g,
\qquad\operatorname{grad}S=8Z.
\]
因此，对任意无迹H，有精确式
\[
D\mathscr F_\alpha[H]
=\int\langle Z,\nabla^*\nabla H-2Rm(H)-8c_\alpha H\rangle.\tag{A7}
\]
曲率作用Rm在对称二张量上的配对自伴；其迹部分与Z不配对。

将(A4)代入，得
\[
\boxed{D\mathscr F_\alpha[H_Z]
=P-\int(v_Z+8c_\alpha)\langle Z,H_Z\rangle
-2\int Rm(Z,H_Z),\quad v_Z=\sqrt{1+|Z|^2}.}\tag{A8}
\]
若使用修正泛函的Q尺度弱驻点，则
\[
P=\int v_Z\langle Z,H_Z\rangle
+2\int Rm(Z,H_Z)+o(Q).\tag{A9}
\]
因为α=O(h)且(A5)=O(Q)，额外项8c_α∫⟨Z,H_Z⟩=O(hQ)=o(Q)。所以在这一实际局部化试验的一阶式中，修正泛函与P的差别不产生新的Q主项。

对混合实际试验(A6)，相应精确式为
\[
\boxed{D\mathscr F_\alpha[H_A]
=\int\langle Z,B\rangle
-\int(v_A+8c_\alpha)\langle Z,H_A\rangle
-2\int Rm(Z,H_A).}\tag{A10}
\]
该式把实际场曲率相关量∫⟨Z,B⟩与一个全局微分试验连接起来。所有项定义在同一实际解和同一度量上。这是一阶固定方向公式：先在g上解出H，再沿g+tH求导。不能直接对(A8)或(A10)再次求g导数并当作固定方向二阶变分，因为那样会产生H(g)和v(g)的额外导数。

**尚未取得的内容。** (A9)、(A10)的曲率耦合项没有确定符号。仅用全曲率O(A)会得到过粗的O(√(AQ))；加入(A3+)使用的实际Weyl预算，可以将其控制为O(Q)，但仍不能作为o(Q)删除。因此不能删除这些项后宣称P=o(Q)或得到阈值。直接Z版本还有独立审读中得到的单调性正项，见同批审读文件；它约束曲率配对而尚未决定最佳首项。

## 4. 修正标量项不会制造任意高频负方向

这是一项新的明确否定：\(\mathscr F_\alpha\) 虽比P多一项O(h)标量平方修正，但当α<1时，其四阶主符号在模去微分同胚方向后仍一致正。

取一点的正交标架，非零频率ξ=|ξ|e⁰，选取横向规范h_{0i}=0。令空间3×3块
\[
h_{ab}=k_{ab}+\tfrac t3\delta_{ab},\qquad \operatorname{tr}k=0.
\]
线性化Ricci与标量的主符号给
\[
|\sigma(DRic^\circ)(\xi)h|^2
=|\xi|^4\left(\tfrac14|k|^2+\tfrac1{12}t^2\right),
\qquad |\sigma(Ds)(\xi)h|^2=|\xi|^4t^2.
\]
故二阶变分的四阶主符号为
\[
\boxed{|\xi|^4\left\{\frac12|k|^2
+\frac{2(1-\alpha)}{3(4-\alpha)}t^2\right\}.}\tag{A11}
\]
α→0时它一致正定。对每个固定光滑背景，在频率远高于背景曲率与变化尺度的振荡试验上，四阶正项支配低阶项，不能得到负二阶方向。

这不排除与曲率集中尺度相同的试验：(A4)与(A6)正是为保留这种尺度构造的。也不排除宏观或低频几何方向。但“通过任意提高频率放大−c_αD²S”不是可行的闭合方法，因为D²P同时具有更强的正主项。

## 5. 当前真正缩小到的判定

本轮没有低成本cell。新增自适应试验已去掉上轮最明显的单位平滑尺度损失，并给出(A8)、(A10)的精确一阶式。若要由此证明系数4，还必须从实际场相容性、弱稳定性或另一条全局恒等式，控制其中的Rm–Z–H相关项，使任意次阈值近极小序列产生Q尺度的下降/负方向。

仅有测试合法性不是符号控制；仅有(A9)也不是拓扑补偿下界。O11仍保持开放状态。
