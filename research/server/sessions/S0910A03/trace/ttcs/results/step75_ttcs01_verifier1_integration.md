# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 75,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step75_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step75_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

For the Yau-26 negative graph-neck program, independently check the mathematical results in the Step-75 note. Verify from first principles: (i) for q=ds^2+G(s) on T^3 with flat T^2 orbits and R_q=-6, the formula R_q=-2h'-|A|^2-h^2 and the downward-zero argument forcing an orbit-plane sectional curvature >=3; (ii) the equivalence to an eigenvalue <=-3 of Ric_q+3I and to reflected Einstein shape acceleration; (iii) under |Ric_4+3g|_op<=delta at a reflected center, the stated quantitative constant lambda_min S'(0)<=-3+5delta, including every trace and sign; (iv) the finite-cylinder anisotropy integration showing reflection plus exact equal orbit normal derivatives at the exit forces d=b-c constant and makes the scalar-minus-six center impossible; (v) the normal weighted identity and physical-length inequality. Report corrected formulas if anything is wrong, and distinguish exact results from statements requiring extra regularity, orientation, coordinates, or boundary assumptions.

## Integrated Scientific Memo

# Step‑75 核验结论

五项核心结论在其声明的对称性、反射和边界条件下均成立；所有主要符号正确。需要两处修正/加强：

1. \(K_{\rm orb}\ge3\) 精确等价于**轨道法向方向**是 \(\operatorname{Ric}_q+3I\) 的一个特征方向且对应特征值 \(\le-3\)。它只蕴含“某个特征值 \(\le-3\)”；后者作为不指明方向的陈述并不反向等价。
2. 原文的
   \[
   \lambda_{\min}S'(0)\le-3+5\delta
   \]
   确实正确，但同一假设下可利用误差分量消去改进为
   \[
   \boxed{\lambda_{\min}S'(0)\le-3+3\delta.}
   \]

---

## 1. \(T^2\) 轨道的标量曲率与下降零点

设
\[
q=ds^2+G(s)_{ab}dx^a dx^b,\qquad
A=\frac12G^{-1}G',\qquad h=\operatorname{tr}A.
\]
其中 \(s\) 是单位弧长，\(G\) 是周期正定矩阵。混合 Christoffel 符号为
\[
\Gamma^s_{ab}=-\frac12G'_{ab},\qquad
\Gamma^a_{sb}=A^a{}_b.
\]
因此
\[
\operatorname{Ric}_q(\partial_s,\partial_s)=-h'-|A|^2.
\]
每个 \(T^2\) 轨道的内蕴度量系数不依赖 \(x^a\)，故轨道内蕴平坦，而 Gauss 方程给出
\[
K_{\rm orb}=-\det A.
\]
又因
\[
h^2=|A|^2+2\det A,
\]
三维标量曲率满足
\[
\begin{aligned}
R_q
&=2\bigl(\operatorname{Ric}_q(\partial_s,\partial_s)+K_{\rm orb}\bigr)\\
&=-2h'-|A|^2-h^2.
\end{aligned}
\]
故原式
\[
\boxed{R_q=-2h'-|A|^2-h^2}
\]
正确，也适用于非对角 \(G(s)\)。

此外
\[
h=(\log\sqrt{\det G})',
\qquad \int_{S^1}h\,ds=0.
\]
若 \(h\not\equiv0\)，存在下降零点 \(s_0\)，满足
\[
h(s_0)=0,\qquad h'(s_0)\le0.
\]
在该点 \(A\) 迹零，特征值为 \(\alpha,-\alpha\)，从而
\[
-\det A=\alpha^2=\frac12|A|^2.
\]
若 \(R_q=-6\)，则
\[
-6=-2h'-|A|^2,
\]
所以
\[
K_{\rm orb}=-\det A=\frac12|A|^2=3-h'\ge3.
\]
若 \(h\equiv0\)，则处处
\[
|A|^2=6,\qquad K_{\rm orb}=3.
\]

该证明至少要求 \(G\in C^2\)、正定且周期；它要求全局正交形式 \(ds^2+G(s)\)，不适用于带轨道连接项的一般 \(T^2\)-不变度量。

---

## 2. Ricci 特征值与反射中心的形状加速度

令 \(v=\partial_s\)。在三维，
\[
\operatorname{Ric}_q(v,v)=\frac{R_q}{2}-K_{\rm orb}.
\]
因此当 \(R_q=-6\) 时，
\[
(\operatorname{Ric}_q+3q)(v,v)=-K_{\rm orb}.
\]
而在当前系数只依赖 \(s\) 的模型中，
\[
\operatorname{Ric}_q(v,T^2)=0,
\]
故 \(v\) 确为特征向量。于是精确等价关系是
\[
\boxed{
K_{\rm orb}\ge3
\iff
\text{\(v\) 对应的 \(\operatorname{Ric}_q+3I\) 特征值不大于 \(-3\)}.
}
\]
这当然推出
\[
\lambda_{\min}(\operatorname{Ric}_q+3I)\le-3,
\]
但不指明方向的最后一句本身并不与 \(K_{\rm orb}\ge3\) 逻辑等价。

对四维 Gaussian 度量
\[
\bar g=dr^2+q_r,\qquad
S=\frac12q_r^{-1}\partial_rq_r,
\]
采用“膨胀双曲端有 \(S=I\)”的约定。切向 Ricci 方程为
\[
(\operatorname{Ric}_{\bar g})_T^\sharp
=\operatorname{Ric}_{q_r}^\sharp-S'-HS.
\]
反射中心有 \(S(0)=0\)。若 \(\operatorname{Ric}_{\bar g}=-3\bar g\)，则
\[
\boxed{S'(0)=\operatorname{Ric}_{q_0}^\sharp+3I.}
\]
故选出的轨道法向方向满足
\[
\langle S'(0)v,v\rangle=-K_{\rm orb}\le-3.
\]
这里“加速度”是此形状算子约定下的量；若反转单位法向或改用负的形状算子，相关形状符号须同步改变。并且
\[
q_r''(0)=2q_0S'(0),
\]
所以该结论也确实表示诱导度量相应方向的二阶收缩。

---

## 3. 小四维缺陷：\(5\delta\) 正确，但可改进为 \(3\delta\)

设
\[
E=\operatorname{Ric}_{\bar g}+3\bar g,\qquad
\|E\|_{\rm op}\le\delta,
\]
且中心反射，所以 \(S=0\)。记
\[
e=R_q+6.
\]
由中心 Gauss/切向与法向 Ricci 方程，
\[
\boxed{e=\operatorname{tr}_T E-E_{nn}.}
\]
因此
\[
|e|\le3\delta+\delta=4\delta.
\]

在 \(h\) 的下降零点，
\[
-6+e=-2h'-|A|^2,
\]
故
\[
K_{\rm orb}=\frac12|A|^2
=3-\frac e2-h'
\ge3-\frac e2.
\]
对轨道法向单位向量 \(v\)，
\[
(\operatorname{Ric}_q+3q)(v,v)
=\frac e2-K_{\rm orb}
\le e-3.
\]
同时
\[
S'(0)=\operatorname{Ric}_q^\sharp+3I-E_T^\sharp,
\]
所以
\[
\langle S'v,v\rangle\le e-3-E_{vv}.
\]
若分别使用 \(e\le4\delta\) 和 \(-E_{vv}\le\delta\)，即得原文正确的
\[
\lambda_{\min}S'(0)\le-3+5\delta.
\]

但此估计重复计算了 \(E_{vv}\)。在正交标架
\[
(v,e_1,e_2,n)
\]
中，
\[
e=E_{vv}+E_{11}+E_{22}-E_{nn},
\]
故
\[
e-E_{vv}=E_{11}+E_{22}-E_{nn}\le3\delta.
\]
因此同一假设直接给出更强结论
\[
\boxed{\lambda_{\min}S'(0)\le-3+3\delta.}
\]
所以 Step‑75 的 \(5\delta\) 不是错误常数，而是非最优常数；JSON/脚本只验证了较粗的分步估计。

若 \(h\equiv0\)，上述近似计算可在任一点进行。

---

## 4. 有限柱上的各向异性刚性与中心矛盾

对
\[
g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,
\qquad d=b-c,\quad \sigma=b+c,
\]
精确 Einstein 方程的两个归一化轨道分量之差给出
\[
\boxed{\operatorname{div}_{t,z}(e^\sigma\nabla d)=0.}
\]
等价地，以基底度量 \(\gamma=e^{2\phi}(dt^2+dz^2)\) 表示，
\[
\operatorname{div}_{\gamma}(e^\sigma\nabla_\gamma d)=0;
\]
二维共形因子消去后即为上式。

在 \(D=[0,T]\times S^1\) 上乘以 \(d\) 并积分：
\[
0=\int_{\partial D}d\,e^\sigma\partial_nd
-\int_D e^\sigma|\nabla d|^2.
\]
中心反射给出 \(d_n=0\)。外端只需两个轨道主曲率相同，即
\[
b_n=c_n,\qquad d_n=0;
\]
无需完整脐性。\(z\)-方向边界项由周期性抵消。因此
\[
\int_D e^\sigma|\nabla d|^2=0,
\]
在连通柱上推出
\[
\boxed{d\equiv d_0.}
\]

中心诱导度量遂为
\[
q=e^{2\phi(z)}dz^2
 +e^{\sigma(z)+d_0}dx^2
 +e^{\sigma(z)-d_0}dy^2.
\]
定义圆周坐标
\[
d\tau=e^{\phi-\sigma/2}\,dz.
\]
因乘子光滑、正且周期，该坐标具有某个正周期，并且
\[
q=e^\sigma\bigl(d\tau^2+e^{d_0}dx^2+e^{-d_0}dy^2\bigr)
=u^4q_{\rm flat},
\qquad u=e^{\sigma/4}>0.
\]
精确反射 Einstein 中心满足 \(R_q=-6\)，故三维共形标量曲率公式给出
\[
-8\Delta_{q_{\rm flat}}u=-6u^5.
\]
在 \(T^3\) 上积分得到
\[
0=-6\int_{T^3}u^5\,d\mu_{q_{\rm flat}},
\]
矛盾。

因此不存在同时满足以下条件的精确解：

- 上述对角、正交传递的 \(T^2\) 模型；
- \(\operatorname{Ric}_g=-3g\)；
- 中心反射；
- \(z\) 周期；
- 有限外端两个轨道方向的法向导数严格相等。

这不是小缺陷非存在定理。若 \(E=\operatorname{Ric}+3g\neq0\)，方程变为
\[
\operatorname{div}_{t,z}(e^\sigma\nabla d)
=-e^{\sigma+2\phi}(E_x-E_y),
\]
故能量积分不再迫使 \(d\) 为常数。

---

## 5. 法向加权恒等式与物理长度

对 Gaussian 度量
\[
g=dr^2+h_r
\]
定义
\[
S=\frac12h_r^{-1}h_r',\quad H=\operatorname{tr}S,\quad
B=S-I,\quad b=H-3.
\]
法向 Ricci 方程为
\[
E_{rr}=-H'-|S|^2+3.
\]
又
\[
|S|^2=|I+B|^2=3+2b+|B|^2,
\]
故
\[
\boxed{b'+2b+|B|^2=-E_{rr}}
\]
以及
\[
\boxed{(e^{2r}b)'=-e^{2r}(|B|^2+E_{rr}).}
\]

反射中心满足 \(S(0)=0\)，因而 \(b(0)=-3\)。令
\[
\eta=3-H(R)=-b(R),
\]
逐条法向测地线积分得
\[
\boxed{
e^{2R}\eta
=3+\int_0^R e^{2r}\bigl(|S-I|^2+E_{rr}\bigr)\,dr.
}
\]
若 \(\|E\|_{\rm op}\le\delta\)，则 \(E_{rr}\ge-\delta\)，从而
\[
\boxed{
e^{2R}\eta+\frac{\delta}{2}(e^{2R}-1)
\ge
3+\int_0^Re^{2r}|S-I|^2\,dr
\ge3.
}
\]

若 \(\eta\) 可能有符号，则
\[
R\ge\frac12\log\frac{3}{|\eta|+\delta/2}
\]
（当右侧为正时）。若 \(\eta\ge0\)，可保留常数项得到较强形式
\[
\boxed{
R\ge\frac12\log\frac{3+\delta/2}{\eta+\delta/2}.
}
\]
因此当 \(\delta\to0\) 且出口 \(H(R)\to3\) 时，Gaussian 物理长度必须趋于无穷。

该恒等式沿每条单位速 Gaussian 法向测地线逐点成立；若出口 \(H\) 随横向位置变化，则 \(\eta\) 也是该位置的函数。这里 \(R\) 必须是 \(dr^2+h_r\) 中的物理弧长，且出口为常 \(r\) 切片。一般共形坐标
\[
e^{2\phi(t,z)}(dt^2+dz^2)
\]
中的 \(t\)-区间不能替代 \(R\)，尤其当 \(\phi_z\neq0\) 时，\(t\)-坐标线甚至未必是法向测地线。

## 总结

Step‑75 的结构性中心障碍、有限柱刚性及法向加权恒等式均成立，但都严格受其对称性和边界假设限制。最重要的校正是：

\[
K_{\rm orb}\ge3
\iff
\text{轨道法向特征值}\le-3,
\]
而非与“任意某个特征值 \(\le-3\)”无条件双向等价；并且小缺陷中心估计可由
\[
-3+5\delta
\]
加强为
\[
\boxed{-3+3\delta}.
\]