# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 88,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step88_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step88_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Analyze the next geometric frontier after removing reflection in the complete free-T^2 orthogonally transitive connector class. First independently derive the minimal-separator mechanism and its scope. Then investigate, at equation level, the nearest genuine escape: a free T^2-invariant metric with nonzero connection curvature (failure of orthogonal transitivity), written g=gamma_ij dx^i dx^j+G_ab(dxi^a+A_i^a dx^i)(dxi^b+A_j^b dx^j). Identify how the Abelian curvature F^a=dA^a enters the base Ricci equation, orbit-shape/tension equation, scalar Gauss identity on an invariant separator, and weighted Bochner formula for e=|dU|^2. Determine whether its stress has a favorable or adverse sign for the resolvent obstruction, what end data or topology control (or fail to control) F, and propose one sharp, testable theorem or countermodel that would materially extend the obstruction. Do not assume small Ricci defect forces F small; derive the relevant Maxwell conservation law and conserved fluxes. Keep this within free T^2 symmetry and distinguish it from fully nonsymmetric graph metrics and S^3 necks.

## Integrated Scientific Memo

## 自由 \(T^2\) 类中去掉反射后的下一前沿

记
\[
g=\gamma_{ij}dx^idx^j+
G_{ab}(d\xi^a+A_i^a dx^i)(d\xi^b+A_j^b dx^j),
\]
其中基底 \(B\) 二维，\(\rho=\sqrt{\det G}=e^\sigma\)，
\[
G=\rho M,\qquad \det M=1,\qquad
U:B\to SL(2,\mathbb R)/SO(2)\cong\mathbb H^2.
\]
令
\[
F^a=dA^a=f^a\,dA_\gamma,\qquad
Q=\frac12G_{ab}f^af^b=\frac12|\Omega|_G^2.
\]
以下归一化为
\[
E=\Ric_g+3g.
\]

---

### 1. 反射并非能量下界的本质：最小分离子机制

设 \(B\) 为具有两个扩张尖端的圆柱，且自由 \(T^2\) 作用的分离类存在。任意闭基底曲线 \(C\subset B\) 的不变提升
\[
\Sigma_C=\pi^{-1}(C)
\]
满足
\[
\Vol_3(\Sigma_C)=\int_C\rho\,ds_\gamma.
\]
故不变分离子的面积泛函就是共形基底度量
\[
\widehat\gamma=\rho^2\gamma
\]
的曲线长度。标准扩张尖端上
\[
\gamma\sim dr^2+e^{2r}dz^2,\qquad \rho\sim e^{2r},
\]
而横截面长度为 \(O(e^{3r})\to\infty\)。因此在适当完备性和紧性假设下，分离同伦类取得内部最短闭曲线，其提升 \(\Sigma\) 是不变极小超曲面。

在 \(\Sigma\) 上取基底曲线弧长 \(s\)。诱导度量为
\[
q=ds^2+
G_{ab}(d\xi^a+A_s^a ds)(d\xi^b+A_s^b ds).
\]
由于限制后的连接只在一维基底上，局部可规范消去；全局仅留下平移 holonomy。因此其内禀标量公式与 OT 情形完全相同：
\[
R_q=-2h_s-\frac32h^2-\frac12e,\qquad
h=(\log\rho)_s,\qquad e=|U_s|_{\mathbb H^2}^2.
\]
以 \(d\mu=\rho\,ds\) 积分并分部积分，
\[
\langle R_q\rangle_\mu
=-\frac12\langle e-h^2\rangle_\mu.
\]

极小性给 \(H_\Sigma=0\)，Gauss 方程给
\[
R_q=-6+\tr E-2E(\nu,\nu)-|II|^2.
\]
因
\[
|\tr E-2E(\nu,\nu)|\le4\delta,
\qquad \|E\|_{\op}\le\delta,
\]
得到
\[
\boxed{\;
\langle e\rangle_\mu
\ge 12-8\delta+\langle h^2\rangle_\mu
+2\langle |II|^2\rangle_\mu .
\;}
\]
特别地，精确 Einstein 情形仍有
\[
\boxed{\langle e\rangle_\mu\ge12.}
\]

因此反射的真正作用只是提供一个全测地分离子；两端扩张几何已经可通过极小分离子恢复同一能量地板，而且 \(|II|^2\) 通常使其更强。其范围限于：

* 自由 \(T^2\) 作用；
* 基底为两端圆柱型，且不变 \(T^3\) 分离类有内部极小代表；
* 不含奇异轨道。

它不适用于一般无对称图度量，也不适用于以 \(S^3\) 为接口的连通和颈。

---

## 2. 非正交传递的约化方程

### 2.1 Maxwell 方程与守恒 twist charge

混合 Ricci 分量给 Abelian Maxwell 方程。按上述 \(Q\) 归一化，其结构形式为
\[
\boxed{\;
d\!\left(\rho\,G_{ab}*_\gamma F^b\right)
=2\rho *_\gamma E^{\rm mix}_a .
\;}
\]
精确 Einstein 时，
\[
d\!\left(\rho G_{ab}*F^b\right)=0.
\]
由于基底连通且二维，
\[
\boxed{\;
q_a:=\rho G_{ab}f^b
\quad\text{为常数}.
\;}
\]
于是
\[
f^a=\rho^{-1}G^{ab}q_b
=\rho^{-2}M^{ab}q_b,
\]
并且
\[
\boxed{\;
Q=\frac12\rho^{-3}q_aM^{ab}q_b.
\;}
\]

这立即纠正了“Ricci 缺陷小则 \(F\) 小”的错误推断。近 Einstein 情形只有
\[
dq_a=2\rho *_\gamma E_a^{\rm mix},
\]
故沿曲线 \(\Gamma\)
\[
|q(\Gamma(1))-q(\Gamma(0))|
\le 2\int_\Gamma \rho\,|E^{\rm mix}|\,ds_\gamma.
\]
真正受控量是加权 Maxwell impulse
\[
\mathcal I(\Gamma)=\int_\Gamma\rho\,|E^{\rm mix}|\,ds_\gamma,
\]
而不是单独的 \(\|E\|_\infty\)。在长且 \(\rho\) 很大的区域，任意小的点态缺陷仍可造成 \(O(1)\) 的 charge 变化。

边界与拓扑信息的强弱如下：

* 若精确尾部在某开集上 \(F=0\)，则该端 \(q=0\)，守恒律迫使整个连通精确区 \(F=0\)。
* 仅有 \(F\to0\) 不迫使 \(q=0\)，因为固定非零 \(q\) 时
  \[
  Q=\tfrac12\rho^{-3}q^TM^{-1}q\to0
  \]
  可由面积增长自动实现。
* 圆柱基底无闭二维基类，故 \(q\) 不是 Chern 数，也不被拓扑量子化。
* \(\int F^a\) 控制两端平坦连接 holonomy 的变化，但与守恒动量 \(q_a\) 是不同对象。
* \(F=0\) 但有平移 holonomy 时，水平分布局部可积；这不会产生局部 Bochner 新项。

---

### 2.2 轨道面积方程

垂直 Ricci 迹给
\[
Q-\Delta_\gamma\sigma-|\nabla\sigma|^2
=-6+E_{\rm orb},
\]
即
\[
\boxed{\;
\Delta_\gamma\rho=(6+Q-E_{\rm orb})\rho.
\;}
\]
精确情形：
\[
\boxed{\Delta_\gamma\rho=(6+Q)\rho.}
\]

所以连接曲率增加轨道面积的凸性。它不会通过减弱面积增长来逃离原障碍。

---

### 2.3 基底 Ricci 方程

方程为
\[
\boxed{\;
\Ric_\gamma-\Hess\sigma
=-3\gamma+Q\gamma
+\frac12d\sigma\otimes d\sigma
+\frac12U^*h_{\mathbb H^2}+E_B.
\;}
\]
等价地，有限维 Bakry–Émery 张量满足
\[
\boxed{\;
\Ric_\sigma^4
:=\Ric_\gamma-\Hess\sigma-\frac12d\sigma^2
=-3\gamma+Q\gamma+\frac12U^*h_{\mathbb H^2}+E_B.
\;}
\]
因此 \(Q\gamma\) 对热核和 resolvent 比较具有有利符号：它提高加权 Ricci 下界。特别地，若 \(E_B\ge-\delta\gamma\)，仍有
\[
\Ric_\sigma^4\ge-(3+\delta)\gamma,
\]
无需把 \(Q\) 当成负误差。

---

### 2.4 轨道形状方程

定义垂直无迹 Maxwell stress
\[
\mathcal S_F{}^a{}_b
=f^af_b-Q\delta^a_b,\qquad f_b=G_{bc}f^c.
\]
这是 \(SL(2)/SO(2)\) 切空间中的无迹自伴端同态。矩阵约化给
\[
\boxed{\;
\div_\gamma(\rho M^{-1}dM)
=\rho\,\mathcal S_F-2\rho\,E_V^0,
\;}
\]
其中 \(E_V^0\) 是垂直 Ricci 缺陷的无迹部分。故精确 Einstein 时
\[
\boxed{\tau_\sigma(U)=\mathcal S_F.}
\]
这与 OT 方程 \(\tau_\sigma(U)=0\) 有本质差别：twist 并非小缺陷，而是精确方程中的真实强迫。

在 charge 变量中令
\[
W(M)=q^TM^{-1}q,
\qquad Q=\frac12\rho^{-3}W.
\]
则该强迫是 charge potential 的双曲梯度，具体符号取决于张量—目标空间的识别约定。Iwasawa 坐标下
\[
W=e^{-\alpha}(q_1-\beta q_2)^2+e^\alpha q_2^2,
\]
因而可直接计算强迫方向；关键不变量是其大小与 \(Q\) 同阶，而不是梯度符号本身。

---

## 3. 分离子上的 \(F\) 项

\(F\) 不显式进入 \(R_q\)，但进入外第二基本形式。沿极小基底曲线取单位切向 \(T\) 和法向 \(\nu\)，在 \(A_\nu=0\) 规范中
\[
II_{sa}=\frac12G_{ab}F^b(\nu,T).
\]
所以
\[
2G^{ab}II_{sa}II_{sb}
=\frac12G_{ab}f^af^b=Q.
\]
因此至少有
\[
|II|^2\ge Q
\]
（还可能有来自基底曲线和 \(G\) 法向变化的其他非负分量）。于是 separator floor 可加强为
\[
\boxed{\;
\langle e\rangle_\mu
\ge12-8\delta+\langle h^2\rangle_\mu+2\langle Q\rangle_\mu.
\;}
\]
所以 twist 对下界不是逃逸项，而是强化项。

---

## 4. 加权 Bochner 方程与 resolvent 符号

令
\[
A_{ij}=\langle U_i,U_j\rangle_{\mathbb H^2},
\qquad e=\tr_\gamma A,
\qquad
L=\Delta_\gamma+\langle\nabla\sigma,\nabla\cdot\rangle.
\]
对任意加权 tension \(F_U=\tau_\sigma(U)\)，
\[
V(X)=\langle dU(X),F_U\rangle,
\]
有
\[
\frac12Le
=|DU|^2+(\Ric_\gamma-\Hess\sigma):A
+2\det A+\div_\sigma V-|F_U|^2.
\]
代入基底方程：
\[
\boxed{
\begin{aligned}
\frac12Le={}&|DU|^2
+\frac12|dU(\nabla\sigma)|^2
+\frac12\tr(A^2)+2\det A\\
&+(Q-3)e+E_B:A
+\div_\sigma V-|F_U|^2.
\end{aligned}}
\]
使用
\[
\frac12\tr(A^2)+2\det A\ge\frac12e^2
\]
得精确情形的基本不等式
\[
\boxed{\;
\frac12Le\ge
\frac12e^2+(Q-3)e+\div_\sigma V_F-|\mathcal S_F|^2.
\;}
\]

在上述二维垂直归一化中 \(|\mathcal S_F|=Q\)，故
\[
Le\ge e^2+2(Q-3)e+2\div_\sigma V_F-2Q^2.
\]
重写为 massive resolvent 形式：
\[
\boxed{\;
(-L+6)e
\le36-(e-6)^2-2Qe+2Q^2-2\div_\sigma V_F.
\;}
\]

符号结论是混合的：

* \(+Qe\) 在 Bochner 方程中有利；
* \(Q\) 提高 \(\Ric_\sigma^4\)，有利于热核比较；
* \(Q\) 也提高 separator floor；
* 但 \(-|\tau_\sigma(U)|^2=-Q^2\) 经移到 resolvent 上界后变成 \(+2Q^2\)，不利；
* \(\div_\sigma V_F\) 需要 resolvent 梯度估计，而
  \[
  |V_F|\le Q\sqrt e,
  \]
  若无 \(Q\) 上界则同样失控。

因此 twist 的各向同性 base stress 是有利的，而其无迹垂直 stress 对原 resolvent ceiling 是不利的。它是最近的真正逃逸机制。

---

## 5. 一个可直接检验的定量扩展

假设完整两端延拓满足：

1. 自由 \(T^2\) 不变；
2. 两端为精确扩张尖端，\(e\to0\)；
3. 存在上述不变最小分离子；
4. 精确 Einstein；
5. \(Q\le q_0\) 全局。

由
\[
(-L+6)e
\le36+2q_0^2-2\div_\sigma V_F
\]
及原 resolvent 梯度常数
\[
\sup_x\int|\nabla_yG_6(x,y)|\,d\mu(y)
\le\frac2{\sqrt3},
\]
得到，记 \(B=\sup e\)，
\[
B\le6+\frac{q_0^2}{3}
+\frac4{\sqrt3}q_0\sqrt B.
\]
解二次不等式：
\[
\boxed{\;
B\le
\left[
\frac{2q_0}{\sqrt3}
+\sqrt{6+\frac53q_0^2}
\right]^2.
\;}
\]
而最小分离子给 \(B\ge12\)。故当
\[
\left[
\frac{2q_0}{\sqrt3}
+\sqrt{6+\frac53q_0^2}
\right]^2<12
\]
时矛盾。解得
\[
\boxed{\;q_0<9\sqrt2-12\approx0.7279.\;}
\]

由此得到最尖锐且可测试的候选定理：

> **带 twist 的最小分离子障碍。**  
> 不存在具有两个精确扩张尖端、内部不变最小分离子并满足
> \[
> \Ric_g=-3g,\qquad
> \sup_B\frac12|F|_G^2<9\sqrt2-12
> \]
> 的完整自由 \(T^2\)-不变四维连接器。

证明只差对约化常数、\(|\mathcal S_F|=Q\) 的目标范数约定以及非紧 resolvent 分部积分作一次统一张量核验；逻辑链已经闭合。由于精确尖端若在开尾上 \(F=0\)，Maxwell 守恒实际上给 \(F\equiv0\)，该定理最有意义的版本应允许仅渐近 cusp、但非零守恒 charge 的端。

与之互补的明确反模型目标是：求解带非零常 charge \(q_a\) 的完整约化 Einstein 系统，使

\[
e\to0,\qquad Q\to0
\]
于两端，但内部
\[
\sup Q\ge 9\sqrt2-12.
\]
若存在，它将是自由 \(T^2\) 对称类中首次真正绕过 OT resolvent ceiling 的模型；若不存在，则需要证明 charge potential 与面积方程联合给出更强的全局 \(Q\) 控制。无论哪种结果，都严格位于自由 \(T^2\) 前沿，不能外推到一般图流形度量或 \(S^3\) 颈。