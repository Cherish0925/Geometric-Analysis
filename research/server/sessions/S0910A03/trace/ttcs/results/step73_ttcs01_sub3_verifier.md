# TTCS Independent Branch Record

```json
{
  "step_id": 73,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/scripts/step73_expanding_tail_verify.py",
    "Sessions/S0910A03/workspace/data/step73_expanding_tail.json",
    "Sessions/S0910A03/workspace/data/step72_conformal_gauge_system.json",
    "Sessions/S0910A03/trace/ttcs/results/step72_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Independently verify the mathematical content of the Step 73 note and computation. Check (i) all five Ricci-defect formulas for the explicit expanding tail, including which mixed components vanish; (ii) the exact operator-norm formula, N-independence, endpoint matching, shape operator, and normal balance; (iii) the general adiabatic tail formulas for h=e^{2a}q_{(r-r0)/K}, including the rr, tangential, and mixed components and the stated C(epsilon+K^-1+K^-2+e^-2a0) estimate; (iv) the exact core decomposition equations in a volume-preserving gauge; and (v) the warning that the 3-equation conformal-gauge elliptic subsystem does not automatically solve the remaining constraints. Identify and repair any wrong sign, coefficient, norm factor, unstated regularity/geometric assumption, or conclusion whose scope is too broad. Return a direct mathematical memo with corrected formulas and what the tail result genuinely establishes for the graph-neck route.

## Output

# Step 73 数学核验备忘录

## 总体结论

显式 expanding tail 的 Ricci 张量、算子范数、\(N\)-无关性、形算子与法向平衡均正确。一般绝热尾部的 \(rr\)、切向与混合公式也正确，但须明确：

1. \(rz\) 分量在坐标标架与正交标架中相差 \(e^{-r}\)；
2. 一般尾部公式中的 \(E_T\) 是以 \(h=e^{2a}q_s\) 升指标后的切向算子，不是直接以 \(q_s\) 升指标；
3. 混合项需要对 \(\nabla Q\) 的控制，原文列出的正则性表述没有清楚包含这一量；
4. 精确 cusp germ 要求 cutoff 在端点邻域恒定。脚本中的五次 smootherstep 若向外接常数，仅为 \(C^2\)，不能直接产生光滑拼接；
5. 精确 core 分解要求 \(a=a(r)\) 且 \(q_r\) 的点态体积形式不随 \(r\) 变化，等价于等距切片具有空间常数平均曲率；它不是任意 Gaussian foliation 的恒等分解；
6. 原文给出的 core-entry 数据只有 \(P_j\to0\)，而尾部引理的左端实际给出 \(P=0\)。两者之间还需要一个定量受控的插值段或更强的端点匹配；
7. 三方程椭圆子系统不能仅由 Bianchi 恒等式自动推出剩余两个分量为零。原文对此的警示正确。

---

## 1. 显式 expanding tail

令
\[
B=dr^2+e^{2r}dz^2,\qquad
u=r-\log N+\frac v2,\qquad
w=r-\log N-\frac v2,
\]
于是
\[
g=B+e^{2u}dx^2+e^{2w}dy^2.
\]
对 \(B\) 有
\[
\operatorname{Ric}_B=-B,\qquad
\operatorname{Hess}_B r=B-dr^2.
\]
双重 warped-product 公式给出
\[
\operatorname{Ric}_g|_B
=\operatorname{Ric}_B-\operatorname{Hess}u-du\otimes du
-\operatorname{Hess}w-dw\otimes dw
=-3B-\frac12\,dv\otimes dv.
\]
因此
\[
\boxed{E|_B=-\frac12\,dv\otimes dv},
\qquad E=\operatorname{Ric}_g+3g.
\]

取正交标架
\[
e_0=\partial_r,\quad e_1=e^{-r}\partial_z,\quad
e_2=Ne^{-r-v/2}\partial_x,\quad
e_3=Ne^{-r+v/2}\partial_y.
\]
记
\[
Lv=v_{rr}+3v_r+e^{-2r}v_{zz}.
\]
五个非平凡分量为
\[
\boxed{
\begin{aligned}
E_{00}&=-\frac12v_r^2,\\
E_{01}&=-\frac12e^{-r}v_rv_z,\\
E_{11}&=-\frac12e^{-2r}v_z^2,\\
E_{22}&=-\frac12Lv,\\
E_{33}&=+\frac12Lv.
\end{aligned}}
\]
所有 base–fiber 分量
\[
E_{0\,2},E_{0\,3},E_{1\,2},E_{1\,3}
\]
以及 \(E_{23}\) 都为零。原文所写
\[
E_{rz}=-\frac12v_rv_z
\]
是坐标分量 \(E(\partial_r,\partial_z)\)；正交分量须乘 \(e^{-r}\)。

### 算子范数

基底上的 \(2\times2\) 块是秩一算子
\[
-\frac12(\nabla_Bv)\otimes(\nabla_Bv),
\]
其特征值为
\[
0,\qquad -\frac12|\nabla_Bv|^2.
\]
另外两个特征值为 \(\pm Lv/2\)。故
\[
\boxed{
\|E\|_{\mathrm{op}}
=\frac12\max\left\{
v_r^2+e^{-2r}v_z^2,\,
|v_{rr}+3v_r+e^{-2r}v_{zz}|
\right\}.}
\]
这是逐点精确公式。

### \(N\)-无关性

\(N\) 只给 \(u,w\) 加常数，所有导数均消去，所以局部曲率、正交分量及上述算子范数都与 \(N\) 无关。全局的纤维长度、体积与 injectivity radius 仍依赖 \(N\)。

### cutoff 估计

对
\[
v(r,z)=\chi(s)v_0(z),\qquad s=\frac{r-r_0}{K},
\]
有
\[
v_r=K^{-1}\chi'v_0,\qquad
v_{rr}=K^{-2}\chi''v_0,
\]
从而
\[
\|E\|_{\mathrm{op},\infty}
\le C_{v_0,\chi}
\left(K^{-1}+K^{-2}+e^{-2r_0}\right).
\]
该估计正确。要使两端成为真正的光滑固定 germ，应取 \(\chi\) 在端点邻域恒定。脚本中的
\[
\chi=1-10s^3+15s^4-6s^5
\]
满足前两阶导数在端点消失，但接常数后只有 \(C^2\)；可换成标准 \(C^\infty\) cutoff，估计不变。

右端若 \(\chi\equiv0\) 于某邻域，则
\[
g=dr^2+e^{2r}
\left(dz^2+N^{-2}dx^2+N^{-2}dy^2\right)
\]
在该邻域精确满足 \(\operatorname{Ric}=-3g\)。左端若 \(\chi\equiv1\)，则 \(v=v_0(z)\)、\(v_r=0\)，其剩余 Ricci 缺陷为 \(O(e^{-2r_0})\)。

### 形算子与法向平衡

相对于 \(+\partial_r\)，
\[
S=\frac12h^{-1}h'
=\operatorname{diag}
\left(1,1+\frac12v_r,1-\frac12v_r\right),
\]
故
\[
H=3,\qquad
|S-I|^2=\frac12v_r^2,\qquad
E_{rr}=-\frac12v_r^2.
\]
因此
\[
(H-3)'+2(H-3)+|S-I|^2=-E_{rr}
\]
逐点成立。这个尾部中的法向 Ricci 缺陷恰好补偿它自身产生的 shear，不改变此前累积的 \(H-3\)。

### 脚本与数值文件

`step73_expanding_tail_verify.py` 的符号代入与上述独立推导一致。数据文件中的 `sup_defect_exact` 实际是精确逐点公式在 \(1001\times1024\) 网格上的最大值，不是经过区间算术证明的连续 supremum。

对于 smootherstep，
\[
\max|\chi'|=\frac{15}{8},
\]
因此解析地
\[
\lim_{K\to\infty}K\|E\|_{\mathrm{op},\infty}
=\frac32\max|\chi'|
=\frac{45}{16}=2.8125,
\]
与 JSON 中的数据吻合。

---

## 2. 一般绝热尾部

令
\[
g=dr^2+h_r,\qquad h_r=e^{2a(r)}q_s,\qquad
s=\frac{r-r_0}{K},
\]
并定义
\[
Q=q_s^{-1}\dot q_s,\qquad T=\operatorname{tr}Q.
\]
这里 \(\dot{}\) 表示 \(s\)-导数。Gaussian 公式在约定
\[
S=\frac12h^{-1}h'
\]
下为
\[
\operatorname{Ric}_{rr}=-H'-\operatorname{tr}(S^2),
\]
\[
\operatorname{Ric}_{r\cdot}=\operatorname{div}_hS-dH,
\]
\[
(\operatorname{Ric}_T)^\sharp_h
=e^{-2a}\operatorname{Ric}(q_s)^\sharp_q-S'-HS.
\]
由
\[
S=a'I+\frac1{2K}Q,\qquad
H=3a'+\frac1{2K}T
\]
得到：

\[
\boxed{
\begin{aligned}
E_{rr}={}&3-3a''-3(a')^2
-\frac{a'}K T
-\frac1{2K^2}\dot T
-\frac1{4K^2}\operatorname{tr}(Q^2).
\end{aligned}}
\]

\[
\boxed{
\begin{aligned}
(E_T)^\sharp_h={}&e^{-2a}\operatorname{Ric}(q_s)^\sharp_q\\
&+\left(3-a''-3(a')^2-\frac{a'}{2K}T\right)I\\
&-\frac{3a'}{2K}Q
-\frac1{2K^2}\dot Q
-\frac1{4K^2}TQ .
\end{aligned}}
\]

\[
\boxed{
E_{r\cdot}
=\frac1{2K}\left(\operatorname{div}_{q_s}Q-dT\right).}
\]
若反转法向，混合坐标分量随之变号。以当前 \(+\partial_r\) 约定，上式符号确定为正。其 \(g\)-范数为
\[
\boxed{
|E_{r\cdot}|_g
=\frac{e^{-a}}{2K}
\left|\operatorname{div}_{q_s}Q-dT\right|_{q_s}.}
\]

原文公式本身正确，但“所有切向张量均以 \(q_s\) 视作 endomorphism”容易造成误解：上面的 \(E_T\) 是 \(h^{-1}E|_{T}\)，而 Ricci 项写成 \(e^{-2a}\operatorname{Ric}(q_s)^\sharp_q\)。

### 估计所需的几何控制

对一个随参数变化的路径，足够直接的统一假设是
\[
\|\operatorname{Ric}(q_s)\|_{q_s}
+\|Q\|_{q_s}
+\|\dot Q\|_{q_s}
+|\dot T|
+\|\operatorname{div}Q-dT\|_{q_s}
\le M.
\]
这要求 \(q_s\) 在空间变量上至少有控制 Ricci 所需的二阶正则性，并要求 \(Q\) 有一阶空间导数。仅控制 \(q_s\) 的空间一阶导数不能控制混合项。

设
\[
a'=1-\varepsilon\eta(s),\qquad
0\le\varepsilon\le1,\qquad 0\le\eta\le1,\qquad K\ge1.
\]
则 \(a(r)\ge a_0\)，且
\[
a''=-\frac{\varepsilon}{K}\dot\eta.
\]
上述精确公式给出
\[
\boxed{
\|E\|_{\mathrm{op},\infty}
\le C_M\left(
\varepsilon+K^{-1}+K^{-2}+e^{-2a_0}
\right).}
\]
混合项中的 \(e^{-a_0}/K\) 可由
\[
\frac{e^{-a_0}}K
\le \frac12e^{-2a_0}+\frac1{2K^2}
\]
吸收。若不假设 \(a\) 单调，应把 \(a_0\) 换成区间上的 \(\inf a\)。

若 \(T=0\)，则 \(rr\) 分量中由路径引起的一阶项消失，只剩
\[
-\frac1{4K^2}\operatorname{tr}(Q^2).
\]
这一改善只针对法向路径项；切向的 \(-3a'Q/(2K)\) 和混合项通常仍是一阶量。

若 \(q_s,\eta\) 在右端邻域恒定、\(q_1\) 平坦且 \(\eta=0\)，右端确为精确平坦 cusp germ。左端若 \(q_s\) 恒定且 \(\eta=1\)，则
\[
h_0=e^{2a_0}q_0,\qquad S_0=(1-\varepsilon)I.
\]

---

## 3. core 的点态体积保持分解

设
\[
h_r=e^{2a(r)}q_r,\qquad
S=a'I+P,\qquad \operatorname{tr}P=0,\qquad
q_r'=2q_rP.
\]
由于 \(a\) 只依赖 \(r\)，这同时表示：

- \(H=3a'(r)\) 在每个切片上为空间常数；
- \(q_r\) 的点态体积形式不随 \(r\) 改变。

因此这是 CMC Gaussian ansatz，而不是任意 core 的自动分解。若 \(a\) 依赖切片坐标，原文公式会出现额外的空间导数项。

在该 ansatz 下，精确方程 \(\operatorname{Ric}=-3g\) 等价于相应的演化式与约束：
\[
\boxed{
a''=1-(a')^2-\frac13|P|^2,
}
\]
\[
\boxed{
P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ,
}
\]
\[
\boxed{
e^{-2a}R(q_r)+6\bigl(1-(a')^2\bigr)+|P|^2=0,
}
\]
\[
\boxed{
\operatorname{div}_{q_r}P=0.
}
\]
这里
\[
|P|^2=\operatorname{tr}(P^2).
\]
所有符号和系数均正确。

在反射中心 \(S(0)=0\) 时，
\[
a'(0)=0,\qquad P(0)=0,
\]
Hamilton 方程给出
\[
\boxed{R(q_0)=-6e^{2a(0)}.}
\]

“\(3a'P\) 提供阻尼、曲率源被 \(e^{-2a}\) 压低”这一解释还需要
\[
\|\operatorname{Ric}(q_r)\|_{q_r}
\]
不以 \(e^{2a}\) 或更快速度增长。单凭 \(a\to\infty\) 不能推出源项趋零。

### core-entry 拼接还需补充的量

引理中的固定路径在左端满足 \(Q(0)=0\)，故其
\[
P_{\mathrm{tail}}(0)=0.
\]
原文允许 core 末端
\[
S=(1-\varepsilon)I+P,\qquad P\to0,
\]
但 \(P\neq0\) 时两侧一阶 jet 不相同，不能直接拼接。

更一般的插值路径应满足
\[
Q(0)=2KP
\]
并直接控制精确公式中出现的缩放量，例如
\[
\frac{\|Q\|}{K},\quad
\frac{\|\dot Q\|+\|Q\|^2}{K^2},\quad
\frac{e^{-a}}K\|\operatorname{div}Q-dT\|,\quad
e^{-2a}\|\operatorname{Ric}(q_s)\|.
\]
这些量趋零，再配合 \(a\) 的相应 jet，才足以推出光滑低缺陷拼接。仅有
\[
\varepsilon+\|P\|+e^{-2a}\|\operatorname{Ric}(q)\|\to0
\]
尚未包含完整的插值控制。

---

## 4. 三方程椭圆子系统与剩余约束

主符号行列式
\[
2(\tau^2+\xi^2)^3
\]
确实说明
\[
(E_{tt}+E_{zz},E_x,E_y)=0
\]
在内部是三未知量的椭圆系统。但它没有代数地给出
\[
E_{tt}-E_{zz}=0,\qquad E_{tz}=0.
\]

若前三式成立，则 \(\operatorname{tr}_gE=0\)。 contracted Bianchi 恒等式只推出
\[
\nabla^\mu E_{\mu\nu}=0.
\]
剩余的 base trace-free 张量因而满足一阶散度方程；散度为零的 trace-free 二阶张量在圆柱上可以非零。因此仍需：

- 由相容的端面数据证明这两个分量消失；或
- 解完整 Einstein–DeTurck 系统，并另证 DeTurck 向量场为零。

此外，内部主符号非退化本身并不建立给定端面条件下的适定性。

---

## 5. 该尾部对 graph-neck 路线实际建立的内容

该计算严格建立了一个局部机制：

> 在已进入大尺度膨胀区、径向形算子已接近 \(I\)、且横截面度量可沿几何量受控的路径变到平坦度量时，横截面中幅度为 \(O(1)\) 的各向异性或非平坦变形，可以在长度 \(K\) 的尾部中以
> \[
> O\!\left(\varepsilon+K^{-1}+K^{-2}+e^{-2a_0}\right)
> \]
> 的最大 Ricci 缺陷消除。

显式模型还说明，这一机制对 lattice 参数 \(N\) 完全一致，并且精确有限圆柱上的漂移-Laplace 刚性不能转化为对长退化圆柱的一致逆估计。

它没有构造从全测地反射中心 \(S=0\) 到近脐 expanding slice 的 core。法向平衡显示显式尾部只补偿自身 shear；中心处 \(H-3=-3\) 的初始差额仍须在此前的 core 中处理。因而 Step 73 成功解决的是“进入膨胀区之后如何消除横截面变形”，而尚未给出完整 graph connector。