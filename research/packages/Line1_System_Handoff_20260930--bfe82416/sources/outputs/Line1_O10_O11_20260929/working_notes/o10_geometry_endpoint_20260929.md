# O10：弱零端的低阶正则化传递

日期：2026-09-29。底本：upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex。

本次没有证明原假设下的 O10，也没有构造全局实际反例。下面给出完整可检查的附加推论：将零端的实际有界形式移到辅助度量时，无需在辅助度量重新求解 SW，也无需传递整个 Weyl 张量。在真正的零端，正手性 Weyl 能量由同一拓扑的 Chern–Weil 公式自动控制。剩余正则化要求仅涉及零阶度量改变、二次连接改变、Einstein 残差与体积。

这削减了一个可能证明方法所需的桥梁，并给出任何真实逃逸序列必须满足的限制；不能登记为 O10 已闭合。

## 1. 底本中已经完成的事实

以下不重新计为本次进展。

1. sec:single-parameter，式 e1.2–e1.6：原实际零端序列存在，当且仅当标量曲率为 −4 的序列存在；同一类、平方条件和 Euler 比保留，体积比趋于一。
2. sec:bounded-ricci-endpoint，式 e3.2：有界自对偶形式、点态 Ricci 界与 Euler 密度上界已经给出统一相容性间隙。该形式结论不要求实际供给；实际供给的作用是产生形式。
3. 同节 e3.7–e3.12 已完成有界 Ricci–Euler 比下整个有限参数族的端点强化。
4. sec:curvature-spikes 已有点态小 Ricci 缺陷而全曲率尖峰的真实度量。这里不再把同类尖峰计为新成果。

## 2. 记号

在闭定向四流形上令

\[
Z_t(g,\omega)=|\operatorname{Ric}_g+g|_g^2+
\left|W_g^+-t\left(\frac{|\omega|_g^2}{3}I-\omega\otimes\omega\right)\right|_g^2
+(|\omega|_g^2-2)^2+|d\omega|_g^2,\qquad 0\le t\le\tfrac14.
\]

其中 \(*_g\omega=\omega\)、\(|\omega|_g\le L\)。记

\[
z=V_g^{-1}\int Z_t,\quad r_g=V_g^{-1}\int|\operatorname{Ric}_g+g|^2,\quad
P_g=\int|\operatorname{Ric}_g^\circ|^2,\quad S_g=\int s_g^2,\quad C_g=\int|W_g^+|^2.
\]

Weyl 使用二形式算子的 Hilbert–Schmidt 范数。底本已证：给定 \(K,L,\Lambda\)，若 \(|\operatorname{Ric}_g|\le K\)、\(8\pi^2\chi/V_g\le\Lambda\)，则 \(z\ge c(K,L,\Lambda)>0\)。此结论允许 \(t=0\)。下面只使用它，没有将它默默推广到弱 Ricci。

## 3. 原缺陷给出一阶二次预算

若 \(z\le1\)，则

\[
\boxed{V_g^{-1}\int|\nabla^g\omega|^2\le C_L.}\tag{3.1}
\]

由自对偶性及 Hodge–Weitzenböck 恒等式，

\[
\int|\nabla\omega|^2=2\int|d\omega|^2-\frac13\int s_g|\omega|^2
+2\int\langle W_g^+\omega,\omega\rangle.
\]

又由 \(r_g\le z\)，有 \(\fint|s_g|\le4+2\sqrt z\)。模型算子有界，故
\(\fint|W_g^+|\le C_Lt+\sqrt z\)。结合 \(|\omega|\le L\) 即得 (3.1)。不使用 Sobolev 常数、\(W^-\) 或近平行假设。

## 4. 自对偶投影的低阶传递

令 \(h\) 是同一光滑流形上的另一度量，满足
\(\delta=\|h-g\|_{L^\infty(g)}\le\delta_0\)，其中 \(\delta_0>0\) 是固定充分小的维数常数。于是 \(g,h\) 一致等价，且 \(V_h/V_g=1+O(\delta)\)。定义

\[
q=V_g^{-1}\int|\nabla^h-\nabla^g|_g^2\,d\mu_g,\qquad
\omega_h=\frac12(\omega+*_h\omega).
\]

则 \(*_h\omega_h=\omega_h\)、\(|\omega_h|_h\le CL\)，并有

\[
\boxed{\fint_h\left[(|\omega_h|_h^2-2)^2+|d\omega_h|_h^2\right]
\le C_L(z+\delta^2+q).}\tag{4.1}
\]

证明：写 \(A=\tfrac12(*_h-*_g)\)，则 \(\omega_h=\omega+A\omega\)，且

\[
|A|\le C\delta,\qquad |\nabla^gA|\le C|\nabla^h-\nabla^g|.
\]

后一估计由 \(\nabla^h*_h=0\)、\(\nabla^g*_g=0\) 和两个连接在二形式上的诱导作用得到。因此

\[
|d\omega_h|_g\le |d\omega|_g+C\delta|\nabla^g\omega|_g
+CL|\nabla^h-\nabla^g|_g.
\]

平方积分后用 (3.1)。幅度误差则由
\(\big||\omega_h|_h^2-2\big|\le\big||\omega|_g^2-2\big|+C_L\delta\)
得到。所有范数、体积比较常数一致。这一步没有在 \(h\) 上调用新的实际解。

## 5. 零端正手性能量自动转移

同一 \(T_+=2\chi+3\tau\) 的 Chern–Weil 恒等式为

\[
4\pi^2T_+=2C_g+\frac{S_g}{24}-\frac{P_g}{2}.
\]

分别用于 \(g,h\) 后相减，得到精确关系

\[
\boxed{C_h-C_g=\frac{S_g-S_h}{48}+\frac{P_h-P_g}{4}.}\tag{5.1}
\]

令 \(r_h=V_h^{-1}\int|\operatorname{Ric}_h+h|_h^2\)。当 \(z,r_h\le1\) 时，

\[
S_g\le(4+2\sqrt{r_g})^2V_g,\qquad
S_h\ge(4-2\sqrt{r_h})^2V_h,\qquad P_h\le r_hV_h.
\]

同时 \(C_g/V_g\le C_Lt^2+2z\)。代入 (5.1)，舍去有利的 \(-P_g/4\)，得到

\[
\boxed{\frac{C_h}{V_h}\le C_L(t^2+\sqrt z+\delta+\sqrt{r_h}).}\tag{5.2}
\]

因此 \(t,z,\delta,r_h\to0\) 时，辅助度量的正手性 Weyl 能量自动趋零。无需估计张量差 \(W_h^+-W_g^+\)，更无需控制 \(W_h^-\) 的变化。这只用于零端：一般非零 \(t\) 下，总能量不代替模型方向。

## 6. 正则化代价下界

**命题。** 给定 \(K,L,\Lambda\)，存在 \(c>0\)。若 \(g,\omega,t\) 如前，\(z\le1\)、\(8\pi^2\chi/V_g\le\Lambda\)；且 \(h\) 满足 \(|\operatorname{Ric}_h|_h\le K\)、\(\delta\le\delta_0\)，则

\[
\boxed{t^2+\sqrt z+\delta+q+\sqrt{r_h}\ge c(K,L,\Lambda).}\tag{6.1}
\]

证明：\(r_h\ge1\) 时显然。否则由 (4.1)、(5.2)，

\[
\fint_h Z_0(h,\omega_h)\le C_L(t^2+\sqrt z+\delta+q+\sqrt{r_h}).
\]

体积比较给 \(8\pi^2\chi/V_h\le C\max\{\Lambda,0\}\)。对 \((h,\omega_h,0)\) 应用底本已证的有界 Ricci–Euler 密度形式间隙即可。

若 \(s_g=s_h=-4\)，设 \(v=|V_h/V_g-1|\)，同样证明给出更精确版本

\[
\boxed{t^2+z+v+\delta^2+q+r_h\ge c(K,L,\Lambda).}\tag{6.2}
\]

此时 \(S_g-S_h=16(V_g-V_h)\)，不需要标量迹的平方根误差。

**对 O10 的具体意义。** 假设原实际零端序列存在且 \(\chi/A\le B\)。作底本已证的 Yamabe 归约，取得 \(s_{g_j}=-4\)。实际形式给出 \(t_j\to0,z_j\to0\)，标量供给给出 Euler 密度界。因此，不可能同时构造辅助度量 \(h_j\) 满足：

- 同一 \(M_j\) 上，\(|\operatorname{Ric}_{h_j}|\le K\) 一致；
- \(\|h_j-g_j\|_\infty\to0\)；
- \(V_{g_j}^{-1}\int|\nabla^{h_j}-\nabla^{g_j}|^2\to0\)；
- \(\fint_{h_j}|\operatorname{Ric}_{h_j}+h_j|^2\to0\)。

若从原假设构造出这样的辅助度量，O10 的有界 Euler 比版本即成立。现在证明的是这条充分连接及反例的必要限制，没有证明辅助度量存在。

## 7. 实际 Bianchi 条件下的连接成本

下面是可选的条件强化，不能去掉规范条件。令 \(u=h-g\)，在共同恒等识别下假设

\[
B_gu=\delta_gu+\tfrac12d\operatorname{tr}_gu=0.
\]

若 \(\|u\|_\infty=\delta\) 足够小，则 Ricci 差公式与 \(u\) 配对，分部积分和吸收后得到

\[
\int|\nabla^gu|^2\le
C\delta\int|\operatorname{Ric}_h-\operatorname{Ric}_g|
+C\delta^2\int|\operatorname{Rm}_g|.\tag{7.1}
\]

具体地，线性化主项是 \(\frac12\nabla^*\nabla u\)，其余线性项为背景曲率乘 \(u\) 及 Bianchi 散度项。后者因 \(B_gu=0\) 消失。非线性余项为 \(O(u\nabla^2u)+O(|\nabla u|^2)\)；与 \(u\) 配对后，前者一次分部积分与后者都被 \(C\delta\int|\nabla u|^2\) 控制，可吸收。背景曲率项被 \(C\delta^2\int|\operatorname{Rm}_g|\) 控制。这给出 (7.1)。

写 \(E_g=\operatorname{Ric}_g+g\)、\(E_h=\operatorname{Ric}_h+h\)，则 Ricci 差为 \(E_h-E_g-u\)。由全曲率恒等式和 Cauchy–Schwarz，

\[
\fint|\operatorname{Rm}_g|\le C\sqrt{\max\{\Lambda,0\}+r_g}.
\]

连接差与 \(\nabla^gu\) 一致可比，故

\[
\boxed{q\le C\delta(\sqrt{r_g}+\sqrt{r_h})+
C\delta^2\left(1+\sqrt{\max\{\Lambda,0\}+r_g}\right).}\tag{7.2}
\]

没有使用 Sobolev 常数或 \(W^-\) 点态界。但是，这不产生共同 Bianchi 识别的存在性。底本 X09 已否定若干过强固定基底规范要求，不能为了 (7.2) 假设任意平滑都可以小代价进入这种规范。

## 8. 一手文献核查

1. Norman Zergänge, *Convergence of Riemannian 4-manifolds with L²-curvature bounds*, Theorem 1.2, https://arxiv.org/pdf/1710.09324 。第4页要求全曲率总 \(L^2\) 界、无迹 Ricci 的未归一化 \(L^2\) 趋零、直径上下界，以及全部小球的体积下界 \(\operatorname{Vol}B_r(x)\ge\delta\omega_4r^4\)，其中 \(\delta\) 接近一。它不能直接覆盖 O10 的塌缩、总量随体积增长范畴。仅有 GH 收敛也不自动给出上面形式传递所需连接成本。
2. Li 的 Ricci-flow smoothing II, Theorem 1.1, https://arxiv.org/pdf/0911.3104 ：要求初始点态 Ricci 界，并对每个中心要求固定半径球全曲率积分小。不能以平均 Euler 密度和弱 \(L^2\) Ricci 残差替换。
3. Cheeger–Naber, *Regularity of Einstein manifolds and the codimension 4 conjecture*, https://arxiv.org/pdf/1406.6534 ：相关正则性及曲率估计含点态 Ricci 与非塌缩假设。不能反向解释成这里所需的弱 Ricci 正则化。

这些来源支持“已查定理不能直接补上该连接”，不支持“所有正则化方法不可能成功”。

## 9. 小容量区域替换：允许内部发生任意大的度量改变

上一方案要求全局 \(C^0\) 小变化。以下版本只在保留区要求度量一致，因而允许小区域内部发生任意大的改变。

令 \(0\le\chi\le1\) 为光滑函数，\(\Omega=\{\chi<1\}\)，并假设新度量 \(h\) 在 \(\{\chi>0\}\) 的邻域与 \(g\) 一致。\(h\) 可以在 \(\{\chi=0\}\) 任意变化，但仍定义在同一光滑定向 \(M\) 上。假设 \(|\operatorname{Ric}_h|\le K\)，记

\[
\alpha_g=\frac{\operatorname{Vol}_g\Omega}{V_g},\qquad
\alpha_h=\frac{\operatorname{Vol}_h\Omega}{V_g},\qquad
c_\chi=\frac1{V_g}\int|d\chi|_g^2.
\]

在 \(\alpha_g+\alpha_h\le1/2\) 时，

\[
\boxed{t^2+\sqrt z+\alpha_g+\sqrt{\alpha_h}+c_\chi
\ge c(K,L,\Lambda)>0.}\tag{9.1}
\]

**证明。** 定义 \(\omega_h=\chi\omega\)，在 \(\chi=0\) 处取零。它是全局光滑 \(h\)-自对偶形式且幅度不超过 \(L\)：在非零区 \(h=g\)，零区结论显然。由于 \(h=g\) 在所有乘积求导项的支撑上，

\[
\frac1{V_h}\int|d\omega_h|_h^2
\le C(z+L^2c_\chi),\qquad
\frac1{V_h}\int(|\omega_h|_h^2-2)^2
\le C_L(z+\alpha_h).
\]

在 \(\Omega\) 外 \(h=g\)，故
\(|V_h/V_g-1|\le\alpha_g+\alpha_h\)，且

\[
r_h\le C\left(z+(K+2)^2\alpha_h\right).
\]

正手性能量仍由精确恒等式 (5.1) 控制，得到

\[
\frac{C_h}{V_h}
\le C_{K,L}(t^2+\sqrt z+\alpha_g+\sqrt{\alpha_h}).
\]

于是 \(\fint_hZ_0(h,\omega_h)\) 不超过 (9.1) 左侧的常数倍。Euler 密度因体积可比而保持上控，应用底本已有形式间隙即得 (9.1)。

**含义。** 一个真正的有界 Euler 密度 O10 逃逸序列，不能把所有无界 Ricci 区域置于归一化体积与二次容量均趋零的区域，并在其中以新体积 \(o(V)\) 的代价改造成统一有界 Ricci 度量。这个结论不要求新旧度量全局 \(C^0\) 接近，不要求内部曲率能量小，不需要给新内部延拓实际旋量或扭率，也不要求重新计算内部 \(W^-\)。

但**小体积本身不推出小二次容量，也不保证保留完整外部度量时存在有界 Ricci 的内部替换**。二者均不能从 \(\fint|\operatorname{Ric}+g|^2\to0\) 直接宣称。这是本方法尚需证明的实际几何步骤，不是已经解决的事项。

## 10. 研究状态

- 已证：同一实际形式的低阶度量传递 (4.1)。
- 已证：零端正手性能量通过拓扑恒等式自动传递 (5.1)–(5.2)。
- 已证，依赖底本形式间隙：正则化代价下界 (6.1)–(6.2)。
- 已证条件引理：实际 Bianchi 规范下的连接误差控制 (7.2)。
- 已证：允许内部任意度量改变的小容量区域替换代价下界 (9.1)。
- 未证：从原 O10 输入产生所需低成本辅助度量。

这一方法减少了需要保留的结构：只需同一个有界形式及低阶误差；完整实际旋量、指定 \(W^-\)、完整泡树与每个核心标记都不是该方法的必需前置条件。低成本正则化的存在性仍是实质性的全局问题。
