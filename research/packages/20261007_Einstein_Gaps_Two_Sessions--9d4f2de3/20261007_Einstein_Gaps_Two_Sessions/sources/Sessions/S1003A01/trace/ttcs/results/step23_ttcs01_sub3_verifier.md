# TTCS Independent Branch Record

```json
{
  "step_id": 23,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md",
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md",
    "Sessions/S1003A02/workspace/scripts/cr_pinning_check.py",
    "Sessions/S1003A01/workspace/scripts/arb_piece_diagnose.py",
    "Sessions/S1003A01/workspace/data/perp_tail/arb_diag_x0038_X256_p32.json"
  ]
}
```

## Task

Independently verify the mathematical synthesis joining the exact-CH conformal infimum equality, the corrected mu>2 normalized class, the peer CR-pinning identity/Lemma P, and the exact CH exterior response. Determine exactly what is proved, what still depends on decay/noncollapse/shadowing, and whether CR pinning and the exterior null-line response can be interpreted as components of one terminal map without conflating variables or normalizations. Also read the Arb diagnosis and assess the proposed local-basis certification repair.

## Output

# 科学核验备忘录

## 一、核心结论

给定材料支持以下数学结论：

1. 对单个 exact-CH 端且其补集紧的光滑四维 cell，Step 22 的共形方程存在唯一正解；无需预设 \(s_g\) 的符号。所得度量满足 \(s_{\widehat g}=-24\)，并在任意
   \[
   m< m_*:=2+2\sqrt3\approx5.4641
   \]
   的速率下趋于 CH。
2. 两个共形能量恒等式的系数、符号和衰减阈值相符。去除线性端部通量确实需要选取 \(m>4\)，而最终二次能量的可积性只需 \(m>2\)。
3. exact-ended 类中
   \[
   \inf P=\inf J_6
   \]
   已由所给论证推出。
4. 以当前衰减证明，标量归一化类之间能严格推出的是
   \[
   \boxed{\;
   \inf_{{\cal C}_{\rm exact}}P
   =\inf_{{\cal C}_{\rm exact}}J_6
   =\inf_{{\cal C}_{-24}^{\rm aCH,\mu}}P,
   \qquad 2<\mu<2+2\sqrt3 .
   \;}
   \]
   对所有 \(\mu>2\) 的版本尚未由给定论证推出。特别地，\(r e^{-4r}\) 属于每个 \(2<\mu<4\) 的类，但不属于 \(\mu=4\) 或更大的类。
5. CR-pinning 的控制恒等式和 Lemma P 的常数是正确的。写成 \(\zeta^2G\) 时，\(G\) 对一般对角度量并不是自动正则有界的函数；其有界性来自 ACH block 中对缩放变量的额外控制。
6. exact CH exterior response 是线性化对角反对称通道的精确 Dirichlet-to-Neumann 二次型。其 off-null 变量与 CR-pinning 所控制的无穷远 Rossi 数据在 CH 线性理论中是同一个几何量，差一个明确因子：
   \[
   C_{\rm int}=-\frac{\delta_-}{2}.
   \]
   因而二者可放入一个终端映射，但不能作为两个独立能量项相加。
7. Arb 数据说明当前“全局高阶 Chebyshev 多项式直接作用于复方盒”的区间表示极不适合长 cell；它没有证明真实度量在复域存在奇点。局部低阶表示加严格余项是合适的修复方式，但必须同时处理二阶导数、实轴正性、复域分母分离以及 bolt 附近的可去奇性。

---

## 二、exact-CH 共形归一化

### 1. 存在性、正性和唯一性

令
\[
F(u)=-6\Delta_g u+s_gu+24u^3.
\]
Step 22 的两个分片函数满足正确的弱次解、上解符号：

- 对
  \[
  u_-=1-e^{-a(r-R)},\qquad 0<a<4,
  \]
  CH 端上
  \[
  \Delta u_-=a(\Delta r-a)e^{-a(r-R)}\ge0,
  \]
  且 \(u_-(u_-^2-1)\le0\)，故 \(F(u_-)\le0\)。
- 对
  \[
  u_+=1+(M-1)e^{-a(r-R)},
  \]
  有 \(\Delta u_+\le0\) 且 \(u_+(u_+^2-1)\ge0\)，故 \(F(u_+)\ge0\)。
- \(r=R\) 处法向导数的跃变给出的分布项符号也与上述次解、上解一致。

在穷竭域上取外端值 \(u=1\)，标准单调迭代给出 \(0\le u\le M\)。局部椭圆估计和对角子列产生全局解。由于解在 CH 端严格为正，且满足带有局部有界势的线性方程，Harnack 原理将正性传播到紧核。

若 \(u_1,u_2\) 都趋于一，令 \(w=u_1/u_2\)，则
\[
-6\Delta_{u_2^2g}w-24w+24w^3=0,\qquad w\to1.
\]
大于一的极大值与小于一的极小值均与方程符号矛盾，所以 \(w\equiv1\)。

这一部分隐含的几何假设是：指定 CH 端之外的部分为紧集；若还有其他非紧端，则还需给定那些端上的渐近数据。

### 2. 衰减指数

在 exact CH 区域写 \(v=u-1\)，有
\[
-6\Delta v+(48+72v+24v^2)v=0.
\]
对 \(e^{-mr}\)，线性主部满足
\[
(-6\Delta+48)e^{-mr}
=
6[-m^2+m(3\coth r+\tanh r)+8]e^{-mr}.
\]
无穷远处系数趋于
\[
6(-m^2+4m+8),
\]
其正根是 \(m_*=2+2\sqrt3\)。因此，初始 \(a<4\) 衰减可通过两侧比较提升到每个 \(m<m_*\)。CH 环带上的一致 Schauder 估计给出全部固定阶导数的同一速率。

端点速率 \(m=m_*\) 没有由这一比较法得到；一般 Green 函数展开也允许出现该 indicial 指数对应的首项。

### 3. 能量恒等式

在四维中，截断域上的 Chern–Gauss–Bonnet 比较和 Weyl 能量共形不变性给出
\[
P(g)-P(\widehat g)
=
\frac1{12}\int
\left[
s_g^2-\left(s_g-6\frac{\Delta u}{u}\right)^2
\right]dV_g,
\]
这里应理解为可积差的极限，而不是两个各自可能发散的标量曲率平方积分之差。

设
\[
q=\frac{\Delta u}{u}.
\]
由标量方程
\[
s_g-6q=-24u^2
\]
得到
\[
\begin{aligned}
P(g)-P(\widehat g)
&=\int(s_gq-3q^2)\,dV_g\\
&=\int(3q^2-24u\Delta u)\,dV_g\\
&=3\int q^2\,dV_g+24\int|\nabla u|^2\,dV_g.
\end{aligned}
\]
最后一步的截面通量是
\[
\int_{S_r}u\,\partial_\nu u=O(e^{(4-m)r}),
\]
所以选 \(m>4\) 即可消失。Euler 形式的 transgression 同样由连接差
\[
\nabla^{u^2g}-\nabla^g=O(e^{-mr})
\]
和 \(S_r\) 面积 \(O(e^{4r})\) 得到 \(O(e^{(4-m)r})\)。

再使用
\[
J_6(g)=P(g)+\frac14\int(s_g+24)^2dV_g,
\qquad J_6(\widehat g)=P(\widehat g),
\]
即得第二个恒等式。所有最终二次积分只需 \(m>2\) 即可收敛。

---

## 三、三个下确界的精确逻辑关系

记
\[
a=\inf_{{\cal C}_{\rm exact}}P,\qquad
b=\inf_{{\cal C}_{\rm exact}}J_6,\qquad
c_\mu=\inf_{{\cal C}_{-24}^{\rm aCH,\mu}}P.
\]

### 1. exact-ended 类中的 \(a=b\)

由于 \(P\le J_6\)，有
\[
a\le b.
\]
对任意 exact-ended \(g\)，共形归一化得到 \(\widehat g=u^2g\)，且
\[
P(\widehat g)\le P(g),\qquad J_6(\widehat g)=P(\widehat g).
\]
把 \(u\) 在远端截断到一，得到 exact-ended \(g_R\)，并有
\[
J_6(g_R)\longrightarrow P(\widehat g).
\]
因此
\[
b\le P(\widehat g)\le P(g).
\]
对 \(g\) 取下确界得到 \(b\le a\)，故
\[
\boxed{a=b}.
\]

### 2. 从标量归一化类向 exact 类拼接

若
\[
h-g_{\rm CH}=O(e^{-\mu r})
\]
连同所需导数成立，且 \(\mu>2\)，在宽度固定的环带上拼接到 exact CH 后，Einstein 残差为 \(O(e^{-\mu R})\)，体积为 \(O(e^{4R})\)，故新增平方能量为
\[
O(e^{(4-2\mu)R})\to0.
\]
因此对每个 \(\mu>2\)，
\[
a=b\le c_\mu.
\]

### 3. 反向不等式只在 \(2<\mu<m_*\) 由当前衰减推出

exact-ended \(g\) 的归一化像满足每个 \(m<m_*\) 的衰减。给定
\[
2<\mu<m_*,
\]
可选 \(\mu<m<m_*\)，于是归一化像属于 \({\cal C}_{-24}^{\rm aCH,\mu}\)，从而
\[
c_\mu\le a.
\]
合并得到
\[
a=b=c_\mu,\qquad 2<\mu<m_*.
\]

若 \(\mu_1<\mu_2\)，则
\[
{\cal C}_{-24}^{\rm aCH,\mu_2}
\subset
{\cal C}_{-24}^{\rm aCH,\mu_1},
\qquad
c_{\mu_1}\le c_{\mu_2}.
\]
这种包含关系只能给出较快衰减类的下确界不小于较慢衰减类，不能提供 \(c_{\mu_2}\le a\)。所以“包含关系加直接拼接”不能推出所有 \(\mu>2\) 的相等性。

对 \(\mu\ge m_*\)，需要额外的标量曲率保持拼接定理，或证明 exact-ended 竞争度量可在几乎不改变 \(P\) 的情况下变成 \(s=-24\) 且具有任意快衰减。给定材料中没有这样的结果。

此外，
\[
r e^{-4r}=O(e^{-\mu r})
\quad\Longleftrightarrow\quad \mu<4.
\]
因此若希望归一化类直接容纳观察到的 \(r e^{-4r}\) 尾部，应明确固定
\[
2<\mu<4.
\]

---

## 四、CR-pinning 恒等式与 Lemma P

令
\[
d=y_g-y_h,\qquad A=y_g+y_h,\qquad S=y_f+A,
\]
以及
\[
\widetilde\Phi=q+\frac14d-\zeta\sinh q.
\]
由所给受控方程直接计算可得
\[
\widetilde\Phi'
=
\mathcal D
-\frac14(e_g-e_h),
\]
其中
\[
\boxed{
\mathcal D=
d\left(1-\frac S4\right)
+\zeta\bigl[(A-2)\sinh q-d\cosh q\bigr]
+\frac{2\zeta^2\sinh(2q)}{\kappa^2}.
}
\]
脚本 `cr_pinning_check.py` 对控制部分的符号验证是正确的：
\[
\mathcal D_{\rm control}=-\frac14(e_g-e_h).
\]
随机受迫积分达到 \(6.97\times10^{-16}\) 的一致性，也与该恒等式相符。

若写
\[
\mathcal D=\zeta^2\mathcal G_{\rm CR},
\]
则对一般状态
\[
\mathcal G_{\rm CR}
=
\frac{d(1-S/4)}{\zeta^2}
+
\frac{(A-2)\sinh q-d\cosh q}{\zeta}
+
\frac{2\sinh(2q)}{\kappa^2}.
\]
所以 \(\mathcal G_{\rm CR}\) 对任意对角度量并不自动在 \(\zeta=0\) 正则。ACH block 必须控制
\[
d(1-S/4)=O(\zeta^2),\qquad
(A-2)\sinh q-d\cosh q=O(\zeta)
\]
才能获得统一的 \(\sup|\mathcal G_{\rm CR}|\)。

所给脚本验证了 \(\mathcal D\) 和控制项，但没有把它与 `ach_phi_drift.py` 中具体的 \(\mathcal G_{\rm CR}\) 表达式逐项比较；它也只在平衡曲线 \(E(q)\) 上检查了自由部分为零。因而 \(\sup|\mathcal G_{\rm CR}|\le7.354\) 等数值依赖所引用的 block 区间文件及其中的缩放坐标包络。

### Lemma P 的常数

因为
\[
e_g-e_h=\operatorname{Ric}^\circ_{gg}-\operatorname{Ric}^\circ_{hh},
\]
且
\[
P
=2\pi^2\int W|\operatorname{Ric}^\circ|^2dt
\ge
\pi^2\int W(e_g-e_h)^2dt,
\]
归一化 \(P=8\pi^2\widehat P\) 后，
\[
\begin{aligned}
\frac14\left|\int(e_g-e_h)dt\right|
&\le
\frac14
\left(\int W(e_g-e_h)^2dt\right)^{1/2}
\left(\int\frac{dt}{W}\right)^{1/2}\\
&\le
\left(\frac{\widehat P}{2}\right)^{1/2}
\left(\int\frac{dt}{W}\right)^{1/2}.
\end{aligned}
\]
这正是 Lemma P。

若
\[
W\ge \frac c{16}e^{4t},
\]
则
\[
\int_T^\infty\frac{dt}{W}
\le\frac4c e^{-4T}.
\]
配合漂移积分包络即得
\[
\widehat P_{[T,\infty)}
\ge
\frac c2e^{4T}
\bigl(|\widetilde\Phi(T)|-\varepsilon_{\rm drift}(T)\bigr)_+^2.
\]

这个结论严格依赖两个几何输入：

- 轨道体积满足上述下界；
- 整条尾部留在使 \(\mathcal G_{\rm CR}\) 有界的 ACH block 内。

仅有 \(\zeta\ll1\) 或 \(q\) 落在一个数值区间并不足以控制漂移。

---

## 五、exact CH exterior response 与 CR-pinning 的统一解释

为避免符号重叠，可将 Step 19 的量重命名为
\[
\omega_-=\frac{v_-}{f_-},\qquad
\Gamma_-(x)=\int_x^\infty f_-^2\,ds,\qquad
\varpi(x)=\frac{x^3}{4(1+x)^4}.
\]
这里
\[
x=\sinh^2t,\qquad
k(x)=\left(\frac{x}{1+x}\right)^2.
\]

扭率关系为
\[
(k\theta)'=\frac12f_-^2\omega_-.
\]
设入口数据
\[
\theta(\rho)=\Theta,\qquad \omega_-(\rho)=\omega_0,
\]
并要求 \(\theta(\infty)=0\)。积分并交换积分次序得到
\[
\int_\rho^\infty\Gamma_-(x)\omega_-'(x)\,dx
=
-2k(\rho)\Theta-\omega_0\Gamma_-(\rho)
=:\delta_-.
\]
于是 Cauchy–Schwarz 给出
\[
E_{\rm ext}
=
\int_\rho^\infty\varpi(\omega_-')^2dx
\ge
\frac{\delta_-^2}{\mathcal I_-(\rho)},
\qquad
\mathcal I_-(\rho)=
\int_\rho^\infty\frac{\Gamma_-^2}{\varpi}\,dx.
\]
取
\[
\varpi\omega_-'=\frac{\delta_-}{\mathcal I_-}\Gamma_-
\]
达到等号。Step 19 的
\[
\lambda=-\frac{\delta_-}{\mathcal I_-}
\]
只是该二次优化问题的共轭代价变量，并不是 Rossi 参数，也不是 Einstein 常数。

### 1. null line 的几何量

将入口数据沿零代价 Einstein 模式延拓，\(\omega_-\equiv\omega_0\)，则其无穷远接触平面 squashing 是
\[
C_{\rm int}
=
k(\rho)\Theta+\frac12\omega_0\Gamma_-(\rho)
=
-\frac{\delta_-}{2}.
\]
因此
\[
\delta_-=0
\]
恰好表示内部 Einstein 延拓具有标准 CR 无穷远。该零线仍携带 Einstein mass 振幅；它在纯外部问题中不耗费二次能量，但向内延拓通常在中心奇异，所以不能单独产生全局光滑 cell。

### 2. 与 CR-pinning 常数的吻合

无穷远处
\[
\Gamma_-(x)\sim\frac1{2x^2},
\qquad
\mathcal I_-(x)\sim\frac1{2x^2},
\qquad
x\sim\frac14e^{2T}.
\]
故
\[
E_{\rm ext}
=
\frac{4C_{\rm int}^2}{\mathcal I_-}
\sim
8C_{\rm int}^2x^2
\sim
\frac12e^{4T}C_{\rm int}^2.
\]
这与 Lemma P 在 CH 体积
\[
W=\sinh^3t\cosh t,\qquad We^{-4t}\to\frac1{16}
\]
下给出的系数完全一致。

对无控制 Einstein 延拓，
\[
C_{\rm int}
=
\widetilde\Phi(T)+
\int_T^\infty\mathcal D_{\rm Ein}\,dt.
\]
在线性 CH 反对称通道中，这个量正是 \(-\delta_-/2\)。因此：

- exterior response 给出该 Rossi/CR 错配在近 CH 线性理论中的完整二次值函数；
- CR-pinning 给出同一几何错配的非线性积分估计，只要尾部保持在相应 block 中。

二者不是两个独立惩罚。若把
\[
\frac{\delta_-^2}{\mathcal I_-}
\quad\text{和}\quad
\frac12e^{4T}C_{\rm int}^2
\]
直接相加，就会重复计算同一个反对称控制通道。

### 3. 合适的终端映射

完整一阶端口可写成
\[
{\cal T}_T(g)=
\bigl(g|_{S_T},\nabla_\nu g|_{S_T}\bigr).
\]
在线性对角反对称扇区，它可压缩为 \((\Theta,\omega_0)\)。\(\widetilde\Phi(T)\) 是该一阶端口的一个几何投影，不是额外自由变量。较自然的组织是：

- 保留 \((\Theta,\omega_0)\) 或等价的 metric/first-jet 端口；
- 记录
  \[
  C_{\rm CR}(T)=\widetilde\Phi(T)+\int_T^\infty\mathcal D_{\rm Ein}dt
  \]
  作为标准 CR 错配；
- 在线性近 CH 区域使用
  \[
  C_{\rm CR}=-\delta_-/2,\qquad
  V_T^{(2)}=\delta_-^2/\mathcal I_-;
  \]
- 非线性远离 CH 时，使用 Lemma P 控制 \(C_{\rm CR}\)，而不是把线性值函数继续当作精确公式。

符号上还应区分：

- 径向度量系数 \(G_{\rm rad}\)；
- CR 漂移 \(\mathcal G_{\rm CR}\)；
- exterior moment \(\Gamma_-\)；
- exterior 权重 \(\varpi\)；
- 衰减指数 \(\mu_{\rm dec}\)；
- exterior 代价变量 \(\lambda\)。

另外，A01 的 \(a_2\) 是 Reeb slot，而 A02 记为 \(a_f\)；在
\[
x=\sinh^2t
\]
下对应
\[
a_f=\sqrt{x(1+x)},\qquad a_g=a_h=\sqrt x.
\]

---

## 六、依赖衰减、非塌缩和 shadowing 的部分

### 已由给定推导建立

- exact-CH 输入的共形归一化、唯一性及 \(m<m_*\) 衰减；
- 两个能量恒等式；
- exact-ended 类中的 \(\inf P=\inf J_6\)；
- \(2<\mu<m_*\) 的标量归一化下确界相等；
- 对任意对角度量的 CR 控制恒等式；
- Lemma P 及其常数；
- 线性 CH 反对称通道的 exterior 值函数和 null line。

### 仍依赖额外几何输入

1. **任意 \(\mu>2\) 的归一化类等式**  
   需要标量曲率保持的快速拼接或更强的共形尾部消失定理。

2. **任意有限 \(P\) 的标量 \(-24\) 尾部截断**  
   加权 \(L^2\) 有限本身不给出 \(C^2\) 的 \(e^{-\mu r}\) 点态衰减。Step 25 的 truncation 论证还需证明 rate-\(2\) 径向平移模式的匹配，以及受迫稳定模态的点态衰减。

3. **大体积状态离开 ACH 曲线后再返回**  
   Lemma P 只控制一个 Rossi 投影。排除多分量 excursion 还需要：
   - 对全部状态分量的加权控制；
   - shadowing 定理；
   - face flow 无返回链的严格证明。  
   当前 face unstable fates 来自数值积分；所给材料没有区间流证明或 Lyapunov 函数。

4. **最小化序列的取得**  
   仍依赖 bolt 半径双侧控制、紧集上的轨道非塌缩以及尾部统一进入 ACH block。collapsed connector、大 bolt 和其他退化轨道尚未被 CR-pinning 单独处理。

5. **exterior 二次型的使用区域**  
   \(\delta_-^2/\mathcal I_-\) 是 CH 附近的线性值函数。它不处理远离 CH 的入口状态，也不控制非对角角向模态。全局下界仍需把远端状态拉入线性邻域，或建立非线性 exterior 值函数。

---

## 七、Arb 区间数据与局部表示方案

文件 `data/perp_tail/arb_diag_x0038_X256_p32.json` 显示：

- 32 个复方盒全部有 `vol_finite=false` 和 `ric_finite=false`；
- \(GH\) 与 \(G\) 的包络在许多盒中极大并同时含零两侧；
- 问题并未集中在某个物理子区间；
- 增大浮点精度不会自动缩小由输入盒宽和全局表达式依赖性产生的包络。

但该脚本把每个实区间扩张为实部、虚部半径均为 \(1/64\) 的复方盒，并直接计算全局高阶表达式。由这些输出不能认定真实解析延拓存在零点或奇点；它们只表明当前区间表达式无法分离分母。尤其是对复值函数检查实部下端是否大于零，只是证明无零点的一种充分方式，并非必要方式。

### 局部低阶表示是合适的，但需包含以下数学内容

1. **保持同一个全局度量**  
   若目的是验证已有 LM profile，应把全局 Chebyshev 多项式严格重表达或严格逼近于局部坐标，而不是把各子区间改成彼此独立的新 profile。否则接缝处必须额外证明至少二阶匹配。

2. **同时包络到二阶导数**  
   Ricci 曲率涉及 profile 的一阶、二阶导数；只包络函数值不能给出曲率积分证书。

3. **局部变量应适应几何尺度**  
   从 \(x_0=0.038\) 到 \(X=256\) 跨越约 \(6.7\times10^3\)。按几何级数划分 \(x\)，或使用 \(t=\operatorname{arsinh}\sqrt x\) 后局部多项式化，通常比统一的 \(x\)-宽度更稳定。

4. **bolt 邻域应先因子化**  
   将已知消失因子和可去奇项显式提出，再对剩余光滑函数作区间展开，可避免 \(0/0\) 型依赖放大。

5. **实轴正性与复域无零分开处理**  
   - 对度量成立，只需在实轴证明 \(F,G,e^w\) 等严格为正；
   - 若使用复解析积分器，则还需在每个局部复圆盘或 Bernstein 椭圆上用模长下界或圆盘排零证明分母不为零。

6. **余项必须严格传递到曲率平方积分**  
   可采用局部 Taylor model、局部 Chebyshev 尾和，或实变量 Gauss 积分加高阶导数余项。后者可完全绕开过宽的复方盒。

7. **区分“重表达”和“重新优化”**  
   对已有 profile 的局部重表达不会改变几何对象；若改用局部基重新优化，则需重新证明接缝光滑性、metric positivity、bolt smoothness 和 exact-CH collar。

因此，Step 23 提出的“物理半径子域、局部低阶 Chebyshev/Taylor、区间余项、实轴正性”方向在数学上合适。当前 Arb 文件只解释了为何原表示产生巨大包络，尚未给出 \(X=256\) profile 的严格能量上界。