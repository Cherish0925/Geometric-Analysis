# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 8,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step8_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step8_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Review the corrected nil^3 and orbit-volume conclusions solely as mathematical model results, without extrapolating to an arbitrary collapsed sequence. Verify: v''=(3-rho/2)v; the circle maximum argument; what can and cannot be concluded on an interval when rho may diverge at endpoints; and why the CH^2 cusp shows finite total volume does not bound cusp length. Also assess the abelian parabolic-base statement's exact needed hypotheses (bounded v, polar ends, exact adapted isometric action) and whether finite total volume supplies any of them. Produce corrected model statements suitable for preserving in the research record and explicitly separate them from the cover-based route.

## Integrated Scientific Memo

# 可保存的精确模型结论

以下只涉及精确 cohomogeneity-one Einstein 模型，或具有精确自由等距阿贝尔作用的适配度量；不外推到任意塌缩序列、局部展开覆盖或近似 \(N\)-结构。

## 1. \(\mathrm{nil}^3\) 轨道体积方程

设
\[
g=ds^2+h_s,\qquad
L=\frac12h_s^{-1}h_s',\qquad
H=\operatorname{tr}L=\frac{v'}v,\qquad
v=\sqrt{\det h_s}.
\]
超曲面 Ricci 公式及 \(\operatorname{Ric}_g=-g\) 给出
\[
H'+H^2=3+\operatorname{Scal}(h_s).
\]
因此
\[
\frac{v''}{v}=3+\operatorname{Scal}(h_s).
\]

对 Heisenberg 代数，在正交标架中写
\[
[E_1,E_2]=\sqrt{\rho}\,E_3.
\]
纤维 Ricci 特征值为
\[
-\frac{\rho}{2},\quad-\frac{\rho}{2},\quad+\frac{\rho}{2},
\]
故
\[
\operatorname{Scal}(h_s)=-\frac{\rho}{2}
\]
以及
\[
\boxed{v''=\left(3-\frac{\rho}{2}\right)v.}
\]

在对角表示
\[
h_s=a_1^2(\theta^1)^2+a_2^2(\theta^2)^2+a_3^2(\theta^3)^2,
\qquad d\theta^3=\theta^1\wedge\theta^2,
\]
有
\[
\rho=\frac{a_3^2}{a_1^2a_2^2}.
\]
若使用原笔记的
\[
\mu=\frac{a_3^2}{2a_1^2a_2^2}=\frac{\rho}{2},
\]
则方程等价写为 \(v''=(3-\mu)v\)。应统一记号；圆周估计是
\[
\rho\le\frac23\quad\Longleftrightarrow\quad \mu\le\frac13.
\]

Heisenberg 的负纤维标量曲率从 \(3\) 中作减法，所以不存在不附加 \(\rho\) 控制的普遍不等式 \(v''\ge cv\), \(c>0\)。

---

## 2. 圆周基底排除

令 \(Z\) 为 Heisenberg 中心，定义
\[
z=\operatorname{tr}(L|_Z),\qquad
a=\operatorname{tr}(L|_{Z^\perp}),\qquad
D=z-a,\qquad H=z+a.
\]
完整 Einstein 方程的迹子系统为
\[
\begin{aligned}
H'&=3-\frac{\rho}{2}-H^2,\\
D'&=-1+\frac{3\rho}{2}-HD,\\
\rho'&=2\rho D.
\end{aligned}
\]
混合 Einstein 方程保证 \(L\) 保持中心线，因而该迹系统不要求水平部分对角；水平 shear 不改变上述三个标量方程。

在 \(\rho\) 的内点极值处 \(D=0\)，所以
\[
\rho''=2\rho D'=\rho(3\rho-2).
\]
因此内点最大值满足 \(\rho\le2/3\)，内点最小值满足
\(\rho\ge2/3\)。

在圆周上，全局最大值给出
\[
\rho\le\frac23,
\]
从而
\[
v''=\left(3-\frac{\rho}{2}\right)v
\ge\frac83v>0.
\]
对 compact nilmanifold mapping torus，返回映射保持 lattice，故其行列式绝对值为 \(1\)，\(v\) 和 \(\rho\) 都是圆周上的全局周期标量。于是
\[
0=\int_{S^1}v''\,ds
\ge\frac83\int_{S^1}v\,ds>0,
\]
矛盾。

故可保存：

\[
\boxed{\text{不存在以 }S^1\text{ 为基底的精确 }
\mathrm{nil}^3\text{ 型 }\operatorname{Ric}=-g\text{ 模型。}}
\]

事实上同时使用圆周上的最大值和最小值还会得到 \(\rho\equiv2/3\)，但排除只需最大值结论。

---

## 3. 区间上能够与不能够推出的结论

设 \(I=(a,b)\) 是有限长度区间，并令
\[
R_\pm=\limsup_{s\to a^+,\,b^-}\rho(s).
\]
若 \(R_\pm<\infty\)，则内点最大值判据给出
\[
\sup_I\rho\le
\max\left\{\frac23,R_-,R_+\right\}.
\]

因此，若
\[
\max\{R_-,R_+\}<6,
\]
则存在 \(c>0\) 使
\[
v''\ge cv.
\]
若只知两端 \(\limsup\rho\le6\)，仍有 \(v''\ge0\)。在任一情形，若
\[
v(s)\to0\qquad(s\to a^+,b^-),
\]
则正的凸函数不能在两个有限距离端点同时趋零。因此这种两端闭合模型不存在。特别地，这排除两个光滑中心圆塌缩端，因为此时
\[
a_3\to0,\quad a_1,a_2\to\text{正有限值},
\quad \rho\to0,\quad v\to0.
\]

但若 \(\rho\) 可在端点方向发散，则不能继续使用凸性：
\[
3-\frac{\rho}{2}
\]
可能变成任意大的负数。最大值公式只说明高于 \(2/3\) 的峰值不能在内部形成；它可以由端点输入。当前模型分析没有排除两端高 \(\rho\) 或曲率爆破端之间的解，也没有给出所有 interval/ray 解趋向 \(\mathbb{CH}^2\) fixed point 的全局分类。

确实不存在无条件正系数估计。例如 Hamiltonian 约束
\[
H^2-\operatorname{tr}(L^2)=2-\frac{\rho}{2}
\]
允许一点处取
\[
H=0,\qquad k_3=0,\qquad k_1=-k_2=t,
\qquad t^2=\frac{\rho}{4}-1.
\]
取 \(\rho>6\) 时，这给出合法局部初值且
\[
\frac{v''}{v}=3-\frac{\rho}{2}<0.
\]

---

## 4. \(\mathbb{CH}^2\) cusp：有限体积不控制长度

取 \(\alpha=1/\sqrt6\)，则
\[
g=ds^2+
e^{2\alpha s}\bigl((\theta^1)^2+(\theta^2)^2\bigr)
+\frac23e^{4\alpha s}(\theta^3)^2
\]
满足
\[
\operatorname{Ric}_g=-g,\qquad
\rho=\frac23,\qquad
v(s)=C e^{4s/\sqrt6},\qquad
\frac{v''}{v}=\frac83.
\]
对 Heisenberg lattice 取商并令
\[
s\in(-\infty,0],
\]
得到完整 nil cusp。其基底长度为
\[
\int_{-\infty}^{0}ds=\infty,
\]
而总体积为
\[
C_\Gamma\int_{-\infty}^{0}e^{4s/\sqrt6}\,ds
=\frac{\sqrt6\,C_\Gamma}{4}<\infty.
\]
更直接地，截断段 \([-L,0]\) 的长度为 \(L\)，但
\[
\operatorname{Vol}([-L,0])
=\frac{\sqrt6\,C_\Gamma}{4}
\left(1-e^{-4L/\sqrt6}\right)
\]
随 \(L\to\infty\) 仍一致有界。

因此原笔记中“固定总体积迫使 cusp 长度有界”的说法方向相反，必须删除。向 cusp 深处前进时轨道体积指数衰减，新增任意长距离只贡献越来越小的体积。

---

## 5. 阿贝尔抛物基底命题的精确假设

设
\[
\bar g=
G_{IJ}(dx^I+A^I)(dx^J+A^J)+g_B
\]
具有精确自由、恒秩、等距的局部 \(\mathbb R^N\)-作用，并假定转换映射行列式绝对值为 \(1\)，使
\[
v=\sqrt{\det G}>0
\]
成为 \(B\) 上的全局函数。若
\[
\operatorname{Ric}_{\bar g}=\lambda\bar g,\qquad\lambda<0,
\]
Lott 方程为
\[
\Delta_Bv=
\left(\frac14|F|^2-\lambda N\right)v>0.
\]
若再有：

1. \(B\) 连通且抛物；
2. \(v\) 在 \(B\) 上有界；

则 bounded-above subharmonic Liouville 性使 \(v\) 为常数，与严格正的右端矛盾。因此：

\[
\boxed{\text{精确自由等距阿贝尔模型在抛物基底且有界 }v
\text{ 时不可能有 }\lambda<0.}
\]

若基底是圆周，则 \(F=0\) 且
\[
v''=-\lambda Nv>0;
\]
周期积分即可排除，无需另加 \(v\) 有界条件。

“完备化只添加有限个点”不等于抛物性。足够的标准情形是
\[
B=K\setminus\{p_1,\ldots,p_q\},
\]
其中 \(K\) 是闭光滑流形或 orbifold、\(\dim K\ge2\)，且度量在遗漏点附近光滑或 orbifold 延拓；此时这些点为 polar（零 \(W^{1,2}\)-容量）。若端是 cusp、退化 warped end 或真实边界，则必须独立证明抛物性。Lott 的 Remark 3.15 明确表明，仅“有限个完备化点”不够。

近 Einstein 版本
\[
\operatorname{Ric}=-g+E,\qquad
\|E^\#\|_{\rm op}\le\delta<1
\]
只有在作用仍对该度量**精确等距且精确适配**时才给出
\[
\Delta_Bv
=\left(\frac14|F|^2+N-\operatorname{tr}_VE^\#\right)v
\ge N(1-\delta)v.
\]
近似等距的 CFG \(N\)-结构会产生额外误差，单凭
\(\|E\|_{L^\infty}\) 不能控制。

---

## 6. 有限总体积没有提供所需假设

在已有 compact fiber、固定 lattice 归一化和精确适配分解时，有限总体积至多给出
\[
\int_B v\,d\mu_B<\infty,
\]
而不是 \(\sup_Bv<\infty\)。无界但可积的正解可出现在 puncture 附近；例如 \(-\Delta+c\) 的正 Green 函数在删点空间上满足
\[
\Delta G=cG
\]
且可积但无界。

有限总体积也不推出：

- 精确自由等距作用；
- determinant-one monodromy 与全局 \(v\)；
- 基底抛物性；
- 端点为 polar；
- 基底长度有界。

原容量估计
\[
c\int\eta^2\le\int|\nabla\eta|^2
\]
为假，故依赖它的区域体积界、cusp 长度界和定量 deficit-transport 结论均应删除。

---

## 7. 与覆盖空间路线严格分离

上述结果的输入是已经存在的光滑精确 Einstein 模型及其精确 isometric orbit structure。它们不自动适用于任意
\[
\operatorname{Ric}(g_i)+g_i\to0
\]
的塌缩序列或展开覆盖。要作这种连接，至少还需独立建立：

1. 光滑 \(\operatorname{Ric}=-g\) groupoid 极限及足够强的正则收敛；
2. 精确等距适配作用；
3. 极限基底的抛物性或 polar 端；
4. 全局轨道体积上界；
5. 覆盖次数与局部缺陷质量的控制。

特别地，原空间缺陷积分在 \(D\)-重覆盖上通常变为
\[
\int_{\widehat U}\pi^*\mathcal F
=D\int_U\mathcal F,
\]
不能无条件得到与覆盖次数无关的均值界。

因此研究记录应仅保留：精确 nil\(^3\) 方程、圆周排除、带端点 \(\rho\) 控制的有限区间排除、\(\mathbb{CH}^2\) 有限体积无限长度 cusp，以及“抛物基底 \(+\) 有界 \(v\) \(+\) 精确适配作用”下的阿贝尔模型排除。