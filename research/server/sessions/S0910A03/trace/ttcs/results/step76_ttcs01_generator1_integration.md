# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 76,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step76_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step76_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a mathematically serious next route for the unresolved reflection-core entry problem in the negative branch of Yau 26, using the integrated center anisotropy floor, exact boundary-pairing transport, the expanding-tail lemma, and the actual Li-Liu PE+cusp constructions. Explore both directions: a parameter-dependent exact or small-defect core that converts the scalar-minus-six reflected center into a nonflat expanding PE-type end, and a global inequality that would forbid this. Derive concrete equations or monotone quantities rather than broad suggestions. Pay particular attention to CMC/volume gauge evolution P'+3a'P=e^{-2a}Ric(q)^circ, constraint propagation, Fourier-mode amplification, lattice quotient scaling, and whether Li-Liu's metrics or their Toda boundary problems supply a nearby mechanism despite lacking a totally geodesic torus. Identify one or two distinguishing mathematical calculations that would genuinely decide whether the core-tail construction is viable.

## Integrated Scientific Memo

## 核心判断

目前最有力的下一路线不是再优化一个固定长度有限核，而是把问题改写为：

\[
\boxed{\text{反射标量 }-6\text{ 中心}\longrightarrow
\text{非平坦 AHE/PE 扩张端}}
\]

的参数依赖半核问题，再在远端截断并接 Step 73 的绝热平坦化尾。现有局部障碍只迫使中心出现阶一收缩；它并未排除该收缩被一个越来越长的精确 Einstein 区域“红移”为 \(O(e^{-2R})\) 的出口剪切。真正需要控制的是加权出口应力，而不是未加权的 \(S-I\)。

同时，Li–Liu 确实提供了精确、非平坦的 PE+cusp Einstein 端及其 Toda 边界映射，但不提供反射中心。它最适合作为外端机制和可计算的 Dirichlet-to-Neumann 映射，而不是直接截取成核。

---

# 1. CMC/逐点体积规范中的精确运输系统

取物理 Gaussian 距离 \(r\)，写

\[
g=dr^2+e^{2a(r)}q_r,\qquad
q_r'=2q_rP,\qquad \operatorname{tr}_{q_r}P=0,
\]

于是

\[
S=a'I+P,\qquad H=3a'.
\]

对精确 Einstein 方程 \(\operatorname{Ric}_g=-3g\)，有

\[
a''=1-(a')^2-\frac13|P|^2,
\tag{1}
\]

\[
P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ,
\tag{2}
\]

以及约束

\[
e^{-2a}R(q_r)+6(1-(a')^2)+|P|^2=0,
\tag{3}
\]

\[
\operatorname{div}_{q_r}P=0.
\tag{4}
\]

带缺陷 \(E=\operatorname{Ric}+3g\) 时，按 Step 73 的符号约定，

\[
a''=1-(a')^2-\frac13|P|^2-\frac13E_{rr},
\tag{5}
\]

\[
P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ-E_T^\circ,
\tag{6}
\]

且

\[
e^{-2a}R(q_r)+6(1-(a')^2)+|P|^2
=\operatorname{tr}_T E-E_{rr},
\tag{7}
\]

\[
\operatorname{div}_{q_r}P=E_{r\cdot}.
\tag{8}
\]

关键积分因子为

\[
\boxed{(e^{3a}P)'=
e^a\operatorname{Ric}(q_r)^\circ-e^{3a}E_T^\circ.}
\tag{9}
\]

因此精确区间上

\[
P(R)=e^{-3a(R)}
\int_0^R e^{a(s)}\operatorname{Ric}(q_s)^\circ\,ds.
\tag{10}
\]

若进入扩张区后 \(a(s)=s+O(1)\)，且
\(\|\operatorname{Ric}(q_s)^\circ\|\le C\)，则

\[
P(R)=O(e^{-2R}).
\tag{11}
\]

这给出了中心阶一冲击变成远端小剪切的具体机制。需要强调的是：扩张本身不够；必须控制

\[
e^{-2a}\|\operatorname{Ric}(q_r)\|,
\]

否则 (2) 中的曲率源仍可能是阶一。

反射中心满足

\[
a'(0)=0,\qquad P(0)=0,\qquad
R(q_0)=-6e^{2a(0)}.
\tag{12}
\]

可令 \(a(0)=0\) 归一化，于是 \(R(q_0)=-6\)。

---

# 2. 中心障碍究竟强迫什么

对

\[
q_0=ds^2+G(s)_{ab}dx^a dx^b,
\qquad
A=\frac12G^{-1}G',\quad h=\operatorname{tr}A,
\]

有

\[
R(q_0)=-2h'-|A|^2-h^2.
\tag{13}
\]

利用周期性和二维分解

\[
|A|^2=|A^\circ|^2+\frac12h^2
\]

可得

\[
\boxed{
\int_{S^1}
\left(|A^\circ|^2+\frac32h^2\right)\,ds
=6\,\operatorname{Length}(S^1).
}
\tag{14}
\]

更强的逐点结论是：某个 \(T^2\) 轨道平面满足

\[
K_{\rm orb}\ge3,
\tag{15}
\]

故反射中心的形算子初始加速度至少在一个方向上满足

\[
\lambda_{\min}(S'(0))\le-3.
\tag{16}
\]

若 \(\|E\|_{\rm op}\le\delta\)，Step 75 给出稳定版本

\[
\lambda_{\min}(S'(0))\le-3+3\delta.
\tag{17}
\]

所以在这一中心类中，更换 scalar-\(-6\) 种子不能使初始收缩趋零。可行构造必须在长核中重新分配这份阶一收缩，而不是消除它。

法向平衡进一步给出

\[
\boxed{
e^{2R}(3-H(R))
=
3+\int_0^R e^{2r}
\bigl(|S-I|^2+E_{rr}\bigr)\,dr.
}
\tag{18}
\]

这排除了固定物理长度上同时令 \(H(R)\to3\) 与
\(\|E\|_\infty\to0\)，但允许 \(R\to\infty\)。因此任何参数族都应预期

\[
R_\delta\gtrsim \tfrac12\log(1/\delta)
\]

量级或更长，而不能继续用固定 \(R\) 的有限基优化判定可行性。

---

# 3. 精确边界配对是正确的出口量

在对角正交传递类中，

\[
g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,
\quad d=b-c,\quad \sigma=b+c,
\]

满足

\[
\operatorname{div}(e^\sigma\nabla d)
=
-e^{\sigma+2\phi}(E_x-E_y).
\tag{19}
\]

反射内边界上 \(d_n=0\)。对任意常数 \(c\)，积分得

\[
\boxed{
\int_D e^\sigma|\nabla d|^2
=
\int_{\Gamma_R}(d-c)e^\sigma d_n
+
\int_D(d-c)e^{\sigma+2\phi}(E_x-E_y).
}
\tag{20}
\]

精确 Einstein 情形中第二项消失。总有符号通量

\[
\int_{\Gamma_R}e^\sigma d_n=0,
\tag{21}
\]

但协方差型边界配对

\[
\int_{\Gamma_R}(d-c)e^\sigma d_n
\tag{22}
\]

可以非零并承载全部 Dirichlet 能量。因此：

* 有限出口若 \(d_n\equiv0\)，精确非平凡核不可能存在；
* \(d_n\to0\) 并不构成障碍，因为面积权和 \(d\) 的配对可保持阶一；
* 小缺陷核中还可由 (20) 的体源承担能量。

这也说明任何只用 \(\|S-I\|_\infty\to0\) 推导全局禁阻的不等式都会遗漏真正的运输量。

---

# 4. Fourier 放大与 PE 加权应力

扩张背景上的单模方程为

\[
\psi''+3\psi'-k^2e^{-2r}\psi=0,
\qquad \psi(0)=1,\quad \psi'(0)=0.
\tag{23}
\]

精确解的远端振幅是

\[
\psi_\infty=\frac{\sinh k}{k},
\tag{24}
\]

而渐近导数为

\[
\psi'(R)=k\sinh(k)e^{-2R}+O(e^{-3R}).
\tag{25}
\]

故

\[
\boxed{
e^{2R}\psi'(R)\longrightarrow k\sinh k.
}
\tag{26}
\]

这同时揭示两点：

1. 固定模在远端剪切趋零；
2. 反射到远端的映射在高频上按 \(\sinh k\) 放大，不存在频率一致稳定性。

因此，若做参数依赖构造，中心数据必须位于解析/Gevrey 型权重空间，或证明非线性 Toda/Einstein 映射产生足够高频衰减。仅在有限 Fourier 截断中求得小残差不能控制极限。

标准 PE 展开同样给出这种加权残留。若

\[
g=dr^2+e^{2r}
\left(
\gamma+e^{-2r}\gamma_{(2)}
+e^{-3r}\gamma_{(3)}+\cdots
\right),
\]

则形式上

\[
\gamma_{(2)}=-\operatorname{Sch}_\gamma,\qquad
\operatorname{tr}_\gamma\gamma_{(3)}
=\operatorname{div}_\gamma\gamma_{(3)}=0,
\]

并且

\[
(S-I)^\circ
=
e^{-2r}\operatorname{Sch}_\gamma^\circ
-\frac32e^{-3r}\gamma_{(3)}^\sharp+\cdots.
\tag{27}
\]

所以

\[
e^{2r}(S-I)^\circ
\longrightarrow \operatorname{Sch}_\gamma^\circ.
\tag{28}
\]

这正是可以与中心能量配对的有限 PE 应力。

---

# 5. Li–Liu 提供什么，以及不提供什么

Li–Liu 的 Type I 度量是

\[
h=\xi^{-2}\left(
W\,d\xi^2+W^{-1}\eta^2+We^v g_{T^2}
\right),
\qquad
W=1-\frac12\xi v_\xi,
\tag{29}
\]

其中

\[
(e^v)_{\xi\xi}+\Delta_{T^2}v=0.
\tag{30}
\]

若 \(v=v(\xi,z)\)，令 \(u=e^v\)，正确方程是

\[
\boxed{u_{\xi\xi}+(\log u)_{zz}=0,}
\tag{31}
\]

不是 \(u_{\xi\xi}+u_{zz}=0\)。Step 70 中将其称为线性 Laplace 方程是不正确的。

Li–Liu 证明了 BVP1：

\[
v|_{\xi=0}=\varphi,\qquad v\in L^\infty,
\]

有唯一解，且趋于其常数模型，并证明 \(W>0\)。这产生一端 PE、一端 AH cusp 的精确 \(\operatorname{Ric}=-3h\) 度量。其作用是：

* 给出非平坦 PE 外端的精确非线性 Dirichlet-to-Neumann 映射；
* 给出稳定性和指数衰减；
* 给出可用于截断的精确扩张端。

它不直接给出反射面。事实上 \(\xi=\) 常数切片的单位法向为

\[
n=\xi W^{-1/2}\partial_\xi.
\]

其纤维方向和基面方向主曲率分别为

\[
\kappa_\eta
=
-W^{-1/2}
-\frac{\xi W_\xi}{2W^{3/2}},
\tag{32}
\]

\[
\kappa_B
=
-W^{-1/2}
+\frac{\xi}{2W^{1/2}}
\left(\frac{W_\xi}{W}+v_\xi\right).
\tag{33}
\]

若二者同时为零，则

\[
\frac{\xi W_\xi}{W}=-2,\qquad
\xi\left(\frac{W_\xi}{W}+v_\xi\right)=2,
\]

从而 \(\xi v_\xi=4\)，于是

\[
W=1-\frac12\xi v_\xi=-1,
\]

与正定性矛盾。故 Li–Liu 的 moment-map 切片不能成为 totally geodesic \(T^3\)。

不过这只排除了 \(\xi\)-水平反射面；并未排除该度量中存在非水平的 totally geodesic 图形，也未排除对 Li–Liu 外端做非 ASD Einstein 变形后生成反射面。这两者是不同且尚未解决的问题。

---

# 6. 一个具体的构造问题

最清晰的精确目标是寻找

\[
([0,\infty)\times T^3,g),\qquad
\operatorname{Ric}_g=-3g,
\]

满足

\[
S(0)=0,\qquad R(q_0)=-6,
\tag{34}
\]

并在 \(r\to\infty\) 有非平坦负 Yamabe 型 PE 展开。负 Yamabe 外边界避开 Witten–Yau/Cai–Galloway 的非负 Yamabe 端约束。

这可视为两个非线性流形的交：

* 中心数据流形：
  \[
  \mathcal C=\{(q_0,P_0,\alpha_0):R(q_0)=-6,\ P_0=0,\ \alpha_0=0\};
  \]
* Li–Liu 型 PE 稳定流形：
  \[
  \mathcal S_{\rm PE}=
  \{q_r\to\gamma,\ P_r=O(e^{-2r}),\ \alpha_r\to1\}.
  \]

方程 (9) 表明这并非由中心阶一收缩立即否定；核心问题是约束兼容的稳定流形交是否为空。

若精确交过于刚性，可求小缺陷族

\[
\|E_j\|_\infty\to0,\qquad R_j\to\infty,
\]

并要求出口

\[
\|S_j-I\|_\infty\to0,\qquad
e^{-2a_j(R_j)}
\|\operatorname{Ric}(q_{j,R_j})\|_\infty\to0.
\tag{35}
\]

随后由 Step 73 的绝热尾将非平坦出口变成平坦 cusp germ，附加缺陷为

\[
O\!\left(
\varepsilon_j+K_j^{-1}+K_j^{-2}+e^{-2a_j(R_j)}
\right).
\tag{36}
\]

---

# 7. 可能的全局禁阻形式

任何有效禁阻必须控制加权出口数据。自然候选不是
\(\|P(R)\|_\infty\)，而是

\[
\mathcal T_R:=e^{2a(R)}P(R)
\tag{37}
\]

或边界配对 (22)。

由 (9)，

\[
\mathcal T_R
=
e^{-a(R)}
\int_0^R e^{a(s)}
\operatorname{Ric}(q_s)^\circ\,ds
\quad(E=0).
\tag{38}
\]

若 \(a(R)\sim R\)，其极限可以非零。禁阻定理必须证明：由 scalar-\(-6\) 反射中心产生的加权应力不可能属于允许的 PE/Toda 应力集合。所需形式应类似

\[
\mathcal I(q_0)
\le
\liminf_{R\to\infty}
\int_{\Gamma_R}(d-c_R)e^\sigma d_n
+\text{bulk defect}
+\text{constraint residue},
\tag{39}
\]

并进一步证明右侧对所有 Li–Liu 兼容外端严格小于中心下界。现有资料没有这种严格不等式；而 Fourier 计算表明右侧完全可能保持阶一。

---

# 8. 两个真正具有判别力的计算

## A. 二阶零模匹配：反射散射映射 vs. Li–Liu Toda 映射

在 Type I 平坦模型附近取

\[
v(0,z)=\varepsilon\cos(kz).
\]

一阶线性化满足

\[
w_{\xi\xi}+w_{zz}=0,\qquad
w(0,z)=\cos(kz),\quad w(\infty,z)=0,
\]

故

\[
w=e^{-k\xi}\cos(kz),\qquad
w_\xi(0,z)=-k\cos(kz).
\tag{40}
\]

反射扩张侧则给出

\[
\psi_\infty=\frac{\sinh k}{k},\qquad
e^{2R}\psi'(R)\to k\sinh k.
\tag{41}
\]

一阶只决定非零模；真正决定可行性的是二阶产生的零模：

1. 由法向平衡 (18) 计算
   \[
   e^{2R}(3-H_R)
   \]
   的 \(\varepsilon^2\) 系数；
2. 从 Toda 方程和
   \[
   W=1-\frac12\xi v_\xi
   \]
   计算 Li–Liu PE 端对应的平均二阶应力；
3. 强制 Hamilton、momentum 约束后比较二者。

若一个长度/尺度参数能匹配零模系数，则存在真实的微扰机制；若所有可调参数消除后仍有符号不匹配，则该对称路线在二阶即被阻断。

## B. 精确非线性通量极限

对精确反射核，

\[
\int_{D_R}e^\sigma|\nabla d|^2
=
\int_{\Gamma_R}(d-c_R)e^\sigma d_n.
\tag{42}
\]

将 PE 展开代入

\[
d_n(R)=2(P_x-P_y)(R)
=
2e^{-2R}
\bigl(\operatorname{Sch}_\gamma^\circ\bigr)_{x-y}
+O(e^{-3R})
\tag{43}
\]

并同时展开 \(e^\sigma\) 与 \(d\)，得到边界配对的有限极限

\[
\mathcal F(\gamma,\gamma_{(3)}).
\]

然后利用 Li–Liu 解把
\(\mathcal F\) 明确表示为边值 \(\varphi\) 的泛函。需要判定的是：

\[
\boxed{
\mathcal F(\varphi)
\stackrel{?}{=}
\int_{D_\infty}e^\sigma|\nabla d|^2
}
\tag{44}
\]

能否对某个满足中心 scalar-\(-6\) 约束的数据成立。

* 若可成立，并且线性化无核/余核障碍，则支持精确半核；
* 若能证明对所有 Li–Liu 可实现 \(\varphi\) 存在严格间隙，则排除当前 \(T^2\)-对称机制。

---

# 9. 商格缩放

若所有系数仅依赖 \((r,z)\)，改变 \(x,y\) 周期或取相应有限覆盖不改变局部 Ricci、形算子或 CMC 方程。积分恒等式仅乘以基本域面积；归一化后不变。因此 \(T^2\)-不变构造与 lattice quotient 兼容。

反之，若引入周期 \(1/N\) 的 \(x,y\)-依赖，非零 Fourier 模的导数带来 \(N^2\) 因子。除非振幅和高阶导数按 \(N^{-2}\) 或更强缩放，否则 Ricci 缺陷不再一致。因此现阶段最安全的机制仍是商兼容的 \(T^2\)-不变类。

---

## 结论

现有证据没有给出全局禁阻。中心定理只确定了必须运输的阶一各向异性能量；方程

\[
(e^{3a}P)'=e^a\operatorname{Ric}(q)^\circ
\]

和

\[
e^{2R}\psi'(R)\to k\sinh k
\]

则给出其变为小出口剪切、但保留有限加权应力的明确机制。Li–Liu 度量精确实现了所需外端稳定区，却不能由其 \(\xi\)-水平面直接反射。

当前最尖锐的未决数学对象是：**反射中心的约束保持散射映射与 Li–Liu Toda PE 应力映射是否相交**。二阶零模系数比较和精确边界配对极限是最可能真正决定该核—尾构造生死的两项计算。