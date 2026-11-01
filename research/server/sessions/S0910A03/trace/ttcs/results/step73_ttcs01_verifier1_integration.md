# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 73,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step73_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step73_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical content of the Step 73 note and computation. Check (i) all five Ricci-defect formulas for the explicit expanding tail, including which mixed components vanish; (ii) the exact operator-norm formula, N-independence, endpoint matching, shape operator, and normal balance; (iii) the general adiabatic tail formulas for h=e^{2a}q_{(r-r0)/K}, including the rr, tangential, and mixed components and the stated C(epsilon+K^-1+K^-2+e^-2a0) estimate; (iv) the exact core decomposition equations in a volume-preserving gauge; and (v) the warning that the 3-equation conformal-gauge elliptic subsystem does not automatically solve the remaining constraints. Identify and repair any wrong sign, coefficient, norm factor, unstated regularity/geometric assumption, or conclusion whose scope is too broad. Return a direct mathematical memo with corrected formulas and what the tail result genuinely establishes for the graph-neck route.

## Integrated Scientific Memo

# Step 73 核验与修正版备忘录

取约定
\[
E:=\operatorname{Ric}_g+3g,\qquad 
g=dr^2+h_r,\qquad S=\frac12h_r^{-1}h_r',
\]
法向为 \(+\partial_r\)。核心公式基本正确，但端点光滑性、一般尾部的正则性、core 分解的适用范围，以及 core–tail 的一阶匹配需要补充。

## 1. 显式 expanding tail

令
\[
g=dr^2+e^{2r}\!\left(dz^2+N^{-2}e^v dx^2+N^{-2}e^{-v}dy^2\right),
\]
并取正交标架
\[
e_0=\partial_r,\quad e_1=e^{-r}\partial_z,\quad
e_2=Ne^{-r-v/2}\partial_x,\quad
e_3=Ne^{-r+v/2}\partial_y.
\]
记
\[
L v:=v_{rr}+3v_r+e^{-2r}v_{zz}.
\]
则五个可能非零的正交分量恰为
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
等价地，在基底
\[
B=dr^2+e^{2r}dz^2
\]
上
\[
\boxed{E|_B=-\frac12\,dv\otimes dv.}
\]

须区分两种记号：

- 坐标分量：
  \[
  E(\partial_r,\partial_z)=-\frac12v_rv_z;
  \]
- 正交分量：
  \[
  E(e_0,e_1)=-\frac12e^{-r}v_rv_z.
  \]

所有 base–fiber 分量
\[
E_{02},E_{03},E_{12},E_{13}
\]
以及 fiber–fiber 混合分量 \(E_{23}\) 均为零；\(rz\) 基底混合分量一般不为零。

基底块是秩一算子，特征值为
\[
0,\qquad-\frac12|\nabla_Bv|^2,
\]
另外两特征值为 \(\pm Lv/2\)。因此逐点精确算子范数是
\[
\boxed{
\|E\|_{\mathrm{op}}
=\frac12\max\left\{
v_r^2+e^{-2r}v_z^2,\,
\left|v_{rr}+3v_r+e^{-2r}v_{zz}\right|
\right\}.}
\]

参数 \(N\) 只在两个 warp exponent 中贡献常数 \(-\log N\)，故局部曲率和上述算子范数完全与 \(N\) 无关；但全局纤维长度、体积及 injectivity radius 仍依赖 \(N\)。

对于
\[
v(r,z)=\chi\!\left(\frac{r-r_0}{K}\right)v_0(z),
\]
有
\[
\boxed{
\|E\|_{\mathrm{op},\infty}
\le C_{v_0,\chi}
\left(K^{-1}+K^{-2}+e^{-2r_0}\right).}
\]
这是解析估计。JSON 中的 `sup_defect_exact` 是精确公式在有限网格上的最大值，不是连续 supremum 的严格区间认证。

对脚本使用的 quintic smootherstep，
\[
\max|\chi'|=\frac{15}{8},
\]
故解析地
\[
\lim_{K\to\infty}K\|E\|_{\mathrm{op},\infty}
=\frac32\max|\chi'|
=\frac{45}{16}=2.8125,
\]
与数值结果一致。

### 端点匹配修正

若 \(\chi\) 在两端邻域恒定，则两端有固定 germ；右端 \(v\equiv0\) 时确为精确平坦截面的双曲 cusp germ。左端 \(v=v_0(z)\) 时仍有 \(O(e^{-2r_0})\) 缺陷，并非一般精确 Einstein germ。

脚本中的多项式只满足前两阶导数在端点消失；将其延拓为常数只能得到 \(C^2\) 拼接，而非光滑拼接。几何构造必须改用端点邻域恒定的 \(C^\infty\) cutoff，估计不变。

### 形算子和法向平衡

相对于 \(+\partial_r\)，
\[
\boxed{
S=\operatorname{diag}\left(1,1+\frac12v_r,1-\frac12v_r\right),\qquad H=3,
}
\]
且
\[
|S-I|^2=\frac12v_r^2,\qquad
E_{rr}=-\frac12v_r^2.
\]
因此
\[
(H-3)'+2(H-3)+|S-I|^2=-E_{rr}
\]
逐点成立。该尾部的负法向缺陷只补偿尾部自身产生的 shear，不能支付从反射中心 \(H=0\) 到 entry slice 之前积累的法向不平衡。

---

## 2. 一般绝热尾部

设
\[
g=dr^2+h_r,\qquad h_r=e^{2a(r)}q_s,\qquad
s=\frac{r-r_0}{K},
\]
并定义
\[
Q=q_s^{-1}\dot q_s,\qquad T=\operatorname{tr}_{q_s}Q.
\]
则
\[
\boxed{
S=a'I+\frac1{2K}Q,\qquad
H=3a'+\frac1{2K}T.}
\]

以 \(h_r\) 升指标理解切向 \(E\)，有
\[
\boxed{
E_{rr}
=3-3a''-3(a')^2
-\frac{a'}K T
-\frac1{2K^2}\dot T
-\frac1{4K^2}\operatorname{tr}(Q^2).
}
\]

\[
\boxed{
\begin{aligned}
(E_T)^\sharp_h={}&
e^{-2a}\operatorname{Ric}(q_s)^\sharp_q\\
&+\left(3-a''-3(a')^2-\frac{a'}{2K}T\right)I\\
&-\frac{3a'}{2K}Q
-\frac1{2K^2}\dot Q
-\frac1{4K^2}TQ .
\end{aligned}}
\]

由 contracted Codazzi 方程，
\[
\boxed{
E_{r\cdot}
=\frac1{2K}\left(\operatorname{div}_{q_s}Q-dT\right).}
\]
反转法向会改变该混合分量的符号；在当前约定下符号为正。其范数包含缩放因子
\[
\boxed{
|E_{r\cdot}|_g
=\frac{e^{-a}}{2K}
\left|\operatorname{div}_{q_s}Q-dT\right|_{q_s}.}
\]

原注“切向张量都作为 \(q_s\)-endomorphism”不够准确：左侧实际是 \(h^{-1}E|_T\)，而 Ricci 项表示为
\[
e^{-2a}\operatorname{Ric}(q_s)^\sharp_q.
\]

### 估计及必要假设

取
\[
a'=1-\varepsilon\eta(s),\qquad
0\le\varepsilon\le1,\quad 0\le\eta\le1,\quad K\ge1.
\]
则 \(a\ge a_0\)，并且
\[
a''=-\frac{\varepsilon}{K}\dot\eta.
\]
若沿路径统一控制
\[
\|\operatorname{Ric}(q_s)\|,\quad
\|Q\|,\quad\|\dot Q\|,\quad|\dot T|,\quad
\|\operatorname{div}Q-dT\|,
\]
并有统一正定性/椭圆性下界，则
\[
\boxed{
\|E\|_{\mathrm{op},\infty}
\le C\left(
\varepsilon+K^{-1}+K^{-2}+e^{-2a_0}
\right).}
\]
其中混合项可由
\[
\frac{e^{-a_0}}K
\le\frac12e^{-2a_0}+\frac1{2K^2}
\]
吸收。

原正则性陈述需明确加入：

1. \(q_s\) 的统一正定性及逆度量控制；
2. 控制 Ricci 所需的空间二阶正则性；
3. 至少一个 \(\dot q_s\) 的空间导数，以控制 \(\operatorname{div}Q\)；
4. 足够的参数正则性以控制 \(\dot Q,\dot T\)。

若不能保证 \(a\ge a_0\)，估计中的 \(a_0\) 应改为 \(\inf a\)。

若 \(T=0\)，则只有 \(E_{rr}\) 中的路径贡献由 \(O(K^{-1})\) 改进为 \(O(K^{-2})\)。总算子范数一般仍为 \(O(K^{-1})\)，因为切向项
\[
-\frac{3a'}{2K}Q
\]
仍存在；显式 tail 正是一个反例，虽 \(T=0\)，但缺陷主阶为 \(2.8125/K\)。

若 \(q_s,\eta\) 在端点邻域恒定、\(q_1\) 平坦且右端 \(\eta=0\)，则右端是精确平坦 cusp germ；左端有
\[
h_0=e^{2a_0}q_0,\qquad S_0=(1-\varepsilon)I.
\]

---

## 3. core 的 volume-preserving/CMC 分解

设
\[
h_r=e^{2a(r)}q_r,\qquad
S=a'I+P,\qquad
\operatorname{tr}_{q_r}P=0,\qquad
q_r'=2q_rP.
\]
这一分解附带实质性假设：

- \(a\) 只依赖 \(r\)；
- \(H=3a'(r)\) 在每个 slice 上为空间常数；
- \(q_r\) 的点态体积形式不随 \(r\) 变化。

因此它是 CMC、点态体积保持 gauge，不是任意 Gaussian foliation 自动满足的恒等分解。

在此 gauge 下，精确方程 \(\operatorname{Ric}=-3g\) 分解为
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
以及 Hamilton、momentum 约束
\[
\boxed{
e^{-2a}R(q_r)+6\left(1-(a')^2\right)+|P|^2=0,
}
\]
\[
\boxed{
\operatorname{div}_{q_r}P=0.
}
\]
这里 \(|P|^2=\operatorname{tr}(P^2)\)。符号和系数均正确。

在反射中心 \(S(0)=0\) 时，
\[
a'(0)=0,\qquad P(0)=0,
\]
并由 Hamilton 约束得到
\[
\boxed{R(q_0)=-6e^{2a(0)}.}
\]

“\(3a'P\) 是阻尼且曲率源被 \(e^{-2a}\) 压低”只是条件性机制：还需
\[
e^{-2a}\|\operatorname{Ric}(q_r)\|\to0.
\]
单凭 \(a\to\infty\) 不排除 \(\operatorname{Ric}(q_r)\) 同速或更快增长。

---

## 4. core–tail 接口尚有一阶 jet 缺口

原 tail 引理若要求 \(q_s\) 在左端邻域恒定，则
\[
Q(0)=0,
\]
故 tail 左端的无迹形算子部分为零。原 core-entry 条件却只要求
\[
S_{\rm core}=(1-\varepsilon)I+P,\qquad P\to0,
\]
并允许每个有限阶段 \(P\neq0\)。这不足以直接光滑拼接：两侧一阶 jet 不完全相同。

有两种严格修复：

1. 加强 entry 条件为 \(P=0\) 并匹配更高阶 jet；
2. 加入受控插值段，使
   \[
   Q(0)=2KP
   \]
   并直接验证
   \[
   \frac{\|Q\|}{K},\quad
   \frac{\|\dot Q\|+\|Q\|^2}{K^2},\quad
   \frac{e^{-a}}K\|\operatorname{div}Q-dT\|,\quad
   e^{-2a}\|\operatorname{Ric}(q_s)\|
   \]
   都趋于零，同时匹配 \(a\) 和路径的所需高阶 jet。

因此仅有
\[
\varepsilon+\|P\|+e^{-2a}\|\operatorname{Ric}(q)\|\to0
\]
尚不是完整的光滑 attachment theorem。

---

## 5. 三方程椭圆子系统不能自动补齐约束

主符号行列式
\[
2(\tau^2+\xi^2)^3
\]
只证明
\[
(E_{tt}+E_{zz},E_x,E_y)=0
\]
作为三个未知量的内部主系统是椭圆的。它既不证明给定边界条件下适定，也不推出
\[
E_{tt}-E_{zz}=0,\qquad E_{tz}=0.
\]

即使前三式成立，contracted Bianchi 只给出剩余无迹基底张量满足一阶散度方程；圆柱上散度为零的无迹二阶张量可以非零。因此必须额外：

- 从相容边界数据证明 Hamilton/momentum 分量传播为零；或
- 解完整 Einstein–DeTurck 系统，再证明 DeTurck 向量场消失。

只监测三个椭圆方程的数值收敛不足以证明 Einstein 或小全 Ricci 缺陷；必须记录全部五个独立分量。

## 6. 对 graph-neck 路线真正建立的结论

该 tail 结果严格建立的是一个条件性局部延拓机制：

> 若 core 已到达大尺度、近脐的 expanding slice，并且截面度量可沿几何量统一受控的路径变到平坦度量，同时解决一阶及更高 jet 匹配，则可在足够长的尾部中以
> \[
> O\!\left(\varepsilon+K^{-1}+K^{-2}+e^{-2a_0}\right)
> \]
> 的最大 Ricci 缺陷消除幅度 \(O(1)\) 的截面各向异性或非平坦性，并得到精确平坦 cusp germ。局部估计对 lattice 参数 \(N\) 一致。

它说明 finite-cylinder 的精确 drift-Laplacian 刚性不能升级为长、膨胀、退化圆柱上的统一小缺陷障碍。

它没有建立：

1. 从全测地反射中心 \(S=0\) 到近脐 expanding entry slice 的 core；
2. core–tail 的完整光滑 jet 匹配；
3. 剩余 Einstein 约束的自动传播；
4. 闭流形上的完整 graph connector；
5. Yau 第 26 题的证伪。

精确未解决对象仍是：构造一个 \(z\)-非齐次 core 或全五分量受控的近似 core，使其从
\[
S(0)=0,\qquad R(q_0)=-6e^{2a(0)}
\]
到达 \(a\to\infty\)、\(S\to I\) 且
\[
e^{-2a}\|\operatorname{Ric}(q)\|\to0
\]
的可拼接 entry 数据，并同时满足 Hamilton、momentum 约束及所需 jet 控制。