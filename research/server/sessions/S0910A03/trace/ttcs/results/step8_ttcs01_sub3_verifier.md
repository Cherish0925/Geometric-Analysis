# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex",
    "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_generator1_integration.md",
    "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/scripts/verify_nil3_sign_check.py",
    "Knowledge/objects/papers/The-collapsing-geometry-of-almost-Ricci-flat-4-manifolds--a6608f08b3f8--f94b3ef0dffe/object.md"
  ]
}
```

## Task

Review the corrected nil^3 and orbit-volume conclusions solely as mathematical model results, without extrapolating to an arbitrary collapsed sequence. Verify: v''=(3-rho/2)v; the circle maximum argument; what can and cannot be concluded on an interval when rho may diverge at endpoints; and why the CH^2 cusp shows finite total volume does not bound cusp length. Also assess the abelian parabolic-base statement's exact needed hypotheses (bounded v, polar ends, exact adapted isometric action) and whether finite total volume supplies any of them. Produce corrected model statements suitable for preserving in the research record and explicitly separate them from the cover-based route.

## Output

# 数学模型复核备忘录

## 摘要

作为精确对称 Einstein 模型，以下结果成立：

1. 对一维基底上的 Heisenberg 轨道，
   \[
   \boxed{v''=\left(3-\frac{\rho}{2}\right)v},
   \qquad
   \rho=\frac{a_3^2}{a_1^2a_2^2}.
   \]
2. 圆周基底上的完整 Einstein ODE 没有周期解。
3. 有限区间上，若两端的 \(\rho\) 有统一上界且不超过 \(6\)，并且 \(v\to0\) 于两端，则不存在正解。若 \(\rho\) 在端点方向发散，现有凸性论证不再适用。
4. \(\mathbb{CH}^2\) 的 nil cusp 是真实的 \(\operatorname{Ric}=-g\) 解；其总体积有限，但基底方向长度无限。
5. 阿贝尔抛物基底结论需要全局有界的 \(v\)、精确等距适配作用，以及真正的抛物性。有限总体积至多给出某种加权 \(L^1\) 信息，不能给出这些条件。

这些都是精确模型命题，不能直接转化为任意塌缩序列或其局部覆盖空间上的结论。

---

## 1. nil\(^3\) 轨道体积方程

写
\[
g=ds^2+h_s,\qquad
L=\frac12h_s^{-1}\dot h_s,\qquad
H=\operatorname{tr}L=\frac{v'}v,
\qquad v=\sqrt{\det h_s}.
\]
超曲面 Ricci 公式为
\[
\operatorname{Ric}_{ss}=-H'-\operatorname{tr}(L^2),
\]
\[
\operatorname{Ric}_{T}^{\#}
=\operatorname{Ric}_{h_s}^{\#}-L'-HL.
\]
因此 \(\operatorname{Ric}_g=-g\) 给出
\[
L'+HL=\operatorname{Ric}_{h_s}^{\#}+I.
\]
取迹，
\[
H'+H^2=3+\operatorname{Scal}(h_s).
\]
由于 \(v''/v=H'+H^2\)，只需代入 Heisenberg 轨道的标量曲率。

在 \(h_s\)-正交标架中令
\[
[E_1,E_2]=\sqrt{\rho}\,E_3,
\]
其中 \(E_3\) 张成中心。Milnor Ricci 特征值为
\[
-\frac{\rho}{2},\qquad
-\frac{\rho}{2},\qquad
+\frac{\rho}{2},
\]
故
\[
\operatorname{Scal}(h_s)=-\frac{\rho}{2}.
\]
于是
\[
\boxed{\frac{v''}{v}=3-\frac{\rho}{2}}.
\]

在对角表示
\[
h_s=a_1^2(\theta^1)^2+a_2^2(\theta^2)^2+a_3^2(\theta^3)^2
\]
中，
\[
\rho=\frac{a_3^2}{a_1^2a_2^2}.
\]
若沿用 Step 7 中的
\[
\mu=\frac{a_3^2}{2a_1^2a_2^2}=\frac{\rho}{2},
\]
则同一方程写成
\[
v''=(3-\mu)v.
\]

`verify_nil3_sign_check.py` 用 \(\mathbb{CH}^2\) 模型直接核算了该符号。脚本末尾文字中的“\(\mu\le2/3\)”是变量笔误；正确关系是
\[
\rho\le\frac23,\qquad \mu\le\frac13.
\]

---

## 2. 圆周基底的最大值论证

混合 Einstein 方程 \(\operatorname{Ric}(\partial_s,\cdot)=0\) 在 Heisenberg 正交标架中给出
\[
\operatorname{div}L
=\sqrt{\rho}\,(L_{23}E_1-L_{13}E_2)=0.
\]
因此 \(L\) 保持中心线及其正交补。令
\[
z=\operatorname{tr}(L|_Z),\qquad
a=\operatorname{tr}(L|_{Z^\perp}),\qquad
D=z-a,\qquad H=z+a.
\]
中心与水平部分取迹得到
\[
z'+Hz=1+\frac{\rho}{2},
\qquad
a'+Ha=2-\rho.
\]
另一方面，Heisenberg bracket 范数满足
\[
\rho'=2\rho D.
\]
故闭合标量系统为
\[
\begin{aligned}
H'&=3-\frac{\rho}{2}-H^2,\\
D'&=-1+\frac{3\rho}{2}-HD,\\
\rho'&=2\rho D.
\end{aligned}
\]

在 \(\rho\) 的内点极值处，\(D=0\)，从而
\[
\rho''=2\rho D'
=\rho(3\rho-2).
\]
于是：

- 在局部最大点，\(\rho\le2/3\)；
- 在局部最小点，\(\rho\ge2/3\)。

圆周上 \(\rho\) 同时取得最大值和最小值，因此实际上
\[
\rho\equiv\frac23.
\]
较弱的最大值结论已经足够，因为
\[
v''=\left(3-\frac{\rho}{2}\right)v
\ge\frac83v.
\]

对于 compact nilmanifold mapping torus，返回映射保持 lattice，因而其 Lie 代数行列式的绝对值为 \(1\)。所以 \(\rho\) 与轨道体积 \(v\) 都是圆周上的全局周期标量。积分得到
\[
0=\int_{S^1}v''\,ds
\ge\frac83\int_{S^1}v\,ds>0,
\]
矛盾。因此：

\[
\boxed{\text{不存在圆周基底上的 Heisenberg 轨道 }\operatorname{Ric}=-g\text{ 周期解。}}
\]

该论证不要求水平度量保持对角形式；水平 shear 不进入上述迹系统。

---

## 3. 有限区间上能够推出的结果

设 \(I=(a,b)\)，其中 \(b-a<\infty\)，并令
\[
R_-=\limsup_{s\to a^+}\rho(s),\qquad
R_+=\limsup_{s\to b^-}\rho(s).
\]
若二者有限，则内点最大值公式给出
\[
\sup_I\rho
\le
R:=\max\left\{\frac23,R_-,R_+\right\}.
\]

因此：

- 若 \(R<6\)，则
  \[
  v''\ge\left(3-\frac R2\right)v=:cv,\qquad c>0.
  \]
- 若 \(R\le6\)，至少有
  \[
  v''\ge0.
  \]

若再有
\[
v(s)\longrightarrow0
\quad\text{当 }s\to a^+,b^-,
\]
则 \(v\) 是非负凸函数且两端趋零，故 \(v\le0\)，与内部 \(v>0\) 矛盾。特别地，两个光滑中心圆塌缩端不能由有限区间连接，因为这种端点满足
\[
a_3\to0,\qquad a_1,a_2\to\text{正有限值},
\qquad
\rho\to0,\qquad v\to0.
\]

### 当 \(\rho\) 在端点方向发散时

此时最大值公式只说明高 \(\rho\) 不能形成数值大于 \(2/3\) 的内部峰值；它可以由端点方向输入。由于
\[
3-\frac{\rho}{2}
\]
可能变成任意大的负数，\(v\) 不再具有凸性。

这不是纯粹形式上的可能性。Hamiltonian 约束为
\[
H^2-\operatorname{tr}(L^2)=2-\frac{\rho}{2}.
\]
在一点取对角数据
\[
H=0,\qquad k_3=0,\qquad k_1=-k_2=t,
\]
则约束要求
\[
t^2=\frac{\rho}{4}-1.
\]
任取 \(\rho>6\) 都得到实初值，并且
\[
\frac{v''}{v}=3-\frac{\rho}{2}<0.
\]
标准 ODE 局部存在性和约束保持给出局部 Einstein 解。因此不存在无附加端点控制的统一不等式 \(v''\ge cv\)、\(c>0\)。

现有标量系统没有给出所有高 \(\rho\) 有限端点解的全局分类，也没有排除两端 \(\rho\to\infty\) 时的所有连接解。

---

## 4. \(\mathbb{CH}^2\) cusp 与长度计算

取
\[
\alpha=\frac1{\sqrt6},
\]
以及
\[
g=ds^2
+e^{2\alpha s}\bigl((\theta^1)^2+(\theta^2)^2\bigr)
+\frac23e^{4\alpha s}(\theta^3)^2.
\]
此时
\[
k_1=k_2=\alpha,\qquad k_3=2\alpha,
\qquad
\rho=\frac23,
\]
并且直接代入得到
\[
\operatorname{Ric}_g=-g.
\]
轨道体积为
\[
v(s)=C e^{4\alpha s},
\qquad
\frac{v''}{v}=16\alpha^2=\frac83.
\]

对 Heisenberg lattice 取商，并令 cusp 方向为
\[
s\in(-\infty,s_0],
\]
则
\[
\operatorname{Vol}
=C_\Gamma\int_{-\infty}^{s_0}e^{4\alpha s}\,ds
=\frac{C_\Gamma}{4\alpha}e^{4\alpha s_0}<\infty.
\]
但基底方向长度为
\[
\int_{-\infty}^{s_0}ds=\infty.
\]

更明确地，固定 \(s_0=0\) 后，截断段 \([-L,0]\) 满足
\[
\operatorname{Length}=L,
\]
而
\[
\operatorname{Vol}([-L,0])
=\frac{C_\Gamma}{4\alpha}
\left(1-e^{-4\alpha L}\right)
\le\frac{C_\Gamma}{4\alpha}.
\]
所以 \(L\to\infty\) 时体积仍一致有界。Step 7 中“指数体积增长迫使 cusp 长度有界”的句子方向相反：朝 cusp 深处，轨道体积指数衰减，新增长度贡献越来越小。

---

## 5. 阿贝尔抛物基底命题的精确形式

设
\[
\bar g=G_{IJ}(dx^I+A^I)(dx^J+A^J)+g_B
\]
是一个精确适配度量。下列条件共同给出 Lott 方程的 Liouville 论证：

1. 局部 \(\mathbb R^N\) 作用自由、等距且轨道维数恒为 \(N\)；
2. 转换映射的行列式绝对值为 \(1\)，从而
   \[
   v=\sqrt{\det G}
   \]
   是 \(B\) 上的全局正函数；
3. \(\operatorname{Ric}_{\bar g}=\lambda\bar g\)，其中 \(\lambda<0\)；
4. \(B\) 连通且抛物；
5. \(\sup_Bv<\infty\)。

Lott 方程为
\[
\Delta_Bv
=\left(\frac14|F|^2-\lambda N\right)v.
\]
于是 \(v\) 是有界上方的次调和函数，抛物性使其为常数；但右端严格为正，产生矛盾。因此不存在这样的精确阿贝尔模型。

对于
\[
\operatorname{Ric}_{\bar g}=-\bar g+E,
\qquad
\|E^\#\|_{\mathrm{op}}\le\delta<1,
\]
若作用对该度量仍然精确等距，则竖直迹公式给出
\[
\Delta_Bv
=\left(\frac14|F|^2+N-\operatorname{tr}_VE^\#\right)v
\ge N(1-\delta)v.
\]
在同样的抛物性和有界 \(v\) 条件下，结论相同。

### 零容量端与抛物性

若
\[
B=K\setminus\{p_1,\dots,p_q\},
\]
其中 \(K\) 是闭光滑 Riemann 流形或 orbifold，\(\dim K\ge2\)，且度量在这些点附近按光滑或 orbifold 方式延拓，则每个遗漏点具有零 \(W^{1,2}\)-容量。此时 bounded-above 次调和函数可跨点延拓，故 \(B\) 抛物。

但是“度量完备化只增加有限个点”本身不够。Lott 文中的 Remark 3.15 明确给出一个 annulus 度量：完备化只增加两个点，但该曲面并不抛物。因此需要零容量端或直接的抛物性证明，而不能只使用点数和维数。

---

## 6. 有限总体积实际提供的信息

在已经具有 compact fiber、固定 lattice 归一化和精确适配分解时，
\[
d\mu_M=v\,d\mu_B\,d\mu_{\mathrm{fiber}},
\]
所以有限总体积至多给出
\[
\int_Bv\,d\mu_B<\infty.
\]
它不推出
\[
\sup_Bv<\infty.
\]

即使同时知道
\[
\Delta v=cv,\qquad c>0,
\]
加权 \(L^1\) 也不能替代点态上界。具体地，在闭流形 \(K\) 上取算子 \(-\Delta+c\) 的正 Green 函数 \(G_p\)。在
\[
B=K\setminus\{p\}
\]
上，
\[
\Delta G_p=cG_p,
\]
而 \(G_p\) 在 \(p\) 附近无界但局部可积：维数大于二时行为为 \(r^{2-m}\)，二维时为 \(-\log r\)。

有限总体积同样不产生：

- 精确等距 \(\mathbb R^N\) 作用；
- 全局 determinant-one 轨道体积函数；
- 基底抛物性；
- 零容量端；
- 基底方向长度上界。

对于 unwrapped groupoid 的相对轨道体积，若 lattice 归一化尚未固定，原流形总体积甚至未必直接给出统一的 \(L^1\) 控制。

---

## 7. 与覆盖空间路线的分离

上述命题的输入是一个已经存在的光滑 Einstein 度量及其精确 isometric orbit structure。局部正常覆盖只展开短轨道，并不自动产生：

- 对原度量精确等距的作用；
- 可跨图粘合的全局 \(v\)；
- 抛物商空间；
- 端点处的 \(\rho\) 控制；
- 足以把 Ricci 方程传到光滑极限的正则收敛。

Step 7 的 deck-averaged deficit 段落也不能由轨道体积方程直接得到。若某区域是 \(D\)-重覆盖，则
\[
\int_{\widehat U}\pi^*\mathcal F
=D\int_U\mathcal F.
\]
因此原空间上的 \(O(\delta_i^2)\) 总积分通常只给出覆盖空间上的 \(D\,O(\delta_i^2)\) 上界；文中 degree-independent 的平均值估计少了覆盖次数或局部质量分配信息。

此外，已经撤回的
\[
c\int\eta^2\le\int|\nabla\eta|^2
\]
仍在后文被用于
\[
\operatorname{Vol}(\Omega)\le L^2/c
\]
及 cusp 长度推论。反例 \(v=e^{\sqrt c\,x}\) 表明该容量不等式为假，因而这些定量句子不属于可保存的模型结果。

综上，研究记录中可稳定保留的是：精确 nil\(^3\) 体积恒等式、圆周排除、带端点 \(\rho\) 控制的有限区间结果、\(\mathbb{CH}^2\) 有限体积无限长度 cusp，以及带有界 \(v\) 和抛物基底的精确阿贝尔命题。