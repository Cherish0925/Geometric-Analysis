# TTCS Independent Branch Record

```json
{
  "step_id": 78,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step78_bianchi_vii0_verify.py",
    "Sessions/S0910A03/workspace/data/step78_bianchi_vii0_symbolic.json",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md"
  ]
}
```

## Task

Independently verify the rotating-eigenframe Bianchi VII_0 benchmark for the negative graph-connector route. Read the Step 78 symbolic script/output and the inherited Step 75/77 notes. For g=dr^2+a(r)^2 dz^2+b(r)^2 omega_1^2+c(r)^2 omega_2^2 with omega_1=cos(kz)dx+sin(kz)dy, omega_2=-sin(kz)dx+cos(kz)dy, d=log(b/c), u=a'/a, H=a'/a+b'/b+c'/c, and K=2k^2 a^{-2}sinh^2 d, check from first principles: intrinsic Ricci/scalar formulas; exact Ric=-3g ODEs u'+Hu=3-K, d''+Hd'=2K coth d, (log K)'=-2u+2 coth(d)d'; reflected center implications; and the proposed invariant-region proof u<0, d'>0, K>=6 for r>0. Then derive the sharpest elementary small-defect persistence statement under ||Ric+3g||_op<=delta, including whether delta<3/5 is correct, what interval it covers, and what role H plays. Identify any omitted momentum/off-diagonal equation or global-periodicity issue. Explain precisely what this rules out and what it leaves open for a finite vanishing-defect connector.

## Output

# 独立核验备忘录：旋转本征标架 Bianchi \(\mathrm{VII}_0\) 模型

## 1. 内蕴曲率：从结构方程直接计算

固定 \(r\)，取正交余标架
\[
\theta^1=a\,dz,\qquad \theta^2=b\,\omega_1,\qquad \theta^3=c\,\omega_2 .
\]
由
\[
d\omega_1=k\,dz\wedge\omega_2,\qquad
d\omega_2=-k\,dz\wedge\omega_1
\]
可得
\[
d\theta^2=\alpha\,\theta^1\wedge\theta^3,\qquad
d\theta^3=-\beta\,\theta^1\wedge\theta^2,
\]
其中
\[
\alpha=\frac{k b}{ac},\qquad \beta=\frac{k c}{ab}.
\]
对偶正交标架满足
\[
[e_1,e_2]=\beta e_3,\qquad [e_1,e_3]=-\alpha e_2,\qquad [e_2,e_3]=0.
\]
Koszul 公式给出三个截面曲率
\[
\begin{aligned}
\sec(e_1,e_2)&=\frac{(\alpha-\beta)(\alpha+3\beta)}4,\\
\sec(e_1,e_3)&=-\frac{(\alpha-\beta)(3\alpha+\beta)}4,\\
\sec(e_2,e_3)&=\frac{(\alpha-\beta)^2}{4}.
\end{aligned}
\]
因此
\[
\operatorname{Ric}_q(e_1,e_1)=-\frac{(\alpha-\beta)^2}{2},
\]
\[
\operatorname{Ric}_q(e_2,e_2)=\frac{\alpha^2-\beta^2}{2},\qquad
\operatorname{Ric}_q(e_3,e_3)=-\frac{\alpha^2-\beta^2}{2}.
\]
记
\[
d=\log\frac bc,
\]
则
\[
K:=\frac{(\alpha-\beta)^2}{2}
=\frac{k^2(b^2-c^2)^2}{2a^2b^2c^2}
=2k^2a^{-2}\sinh^2d,
\]
\[
L:=\frac{\alpha^2-\beta^2}{2}
=\frac{k^2(b^4-c^4)}{2a^2b^2c^2}
=k^2a^{-2}\sinh(2d).
\]
当 \(d\ne0\) 时，
\[
L=K\coth d.
\]
于是
\[
\boxed{\operatorname{Ric}_q=\operatorname{diag}(-K,L,-L)},\qquad
\boxed{R_q=-K}.
\]
这与 `step78_bianchi_vii0_symbolic.json` 中的三个内蕴分量及
`scalar_plus_K = 0` 完全一致。

另有
\[
\sec_q(e_2,e_3)=\frac K2.
\]
在精确反射端 \(K(0)=6\) 时，该轨道平面曲率恰为 \(3\)，正好达到 Step 75 中心定理中的数值 \(3\)。

---

## 2. 四维 Ricci 张量与 Einstein 方程

设
\[
u=\frac{a'}a,\qquad v=\frac{b'}b,\qquad w=\frac{c'}c,\qquad
H=u+v+w,\qquad p=d'=v-w.
\]
切片形算子的三个本征值为 \(u,v,w\)。协同一维公式给出
\[
\begin{aligned}
\operatorname{Ric}_{rr}
  &=-H'-(u^2+v^2+w^2),\\
\operatorname{Ric}_{z}
  &=-K-u'-Hu,\\
\operatorname{Ric}_{b}
  &=L-v'-Hv,\\
\operatorname{Ric}_{c}
  &=-L-w'-Hw.
\end{aligned}
\]
这些就是脚本在 \(z=0\) 得到的四个单位标架分量。

令 \(\operatorname{Ric}=-3g\)。则
\[
u'+Hu=3-K,
\]
而 \(b,c\) 两式之差给出
\[
p'+Hp=2L=2K\coth d,
\]
即
\[
\boxed{d''+Hd'=2K\coth d}.
\]
由
\[
K=2k^2a^{-2}\sinh^2d
\]
直接微分，在 \(K>0\) 时得到
\[
\boxed{(\log K)'=-2u+2\coth(d)d'}.
\]
因此 Step 78 列出的三个方程符号均正确。\(K\coth d\) 在 \(d=0\) 应理解为光滑表达式
\[
k^2a^{-2}\sinh(2d),
\]
但反射端会有 \(K(0)=6\)，故这里不会遇到 \(d=0\)。

这三个方程只是 Einstein 系统的必要子系统。其余对角方程为
\[
v'+Hv=3+L,\qquad w'+Hw=3-L,
\]
以及
\[
H'=3-(u^2+v^2+w^2).
\]
若记 \(s=v+w\)，也可写成
\[
s'+Hs=6,\qquad H=u+s.
\]
精确 Hamilton 恒等式是
\[
\boxed{K=6-H^2+(u^2+v^2+w^2)}.
\]
因此仅演化 \(u,d,K\) 而不给出 \(H\) 或 \(v+w\)，并不是闭合的 Einstein 构造系统；不过以下不变区论证只需这三个必要方程。

---

## 3. 反射端的精确含义

反射延拓要求 \(a,b,c\) 关于 \(r\) 为偶函数，所以
\[
u(0)=v(0)=w(0)=0,\qquad H(0)=0,\qquad d'(0)=0.
\]
精确 Einstein 情形在此给出
\[
R_{q_0}=-6.
\]
由于 \(R_{q_0}=-K(0)\)，
\[
\boxed{K(0)=6}.
\]
所以 \(d_0=d(0)\ne0\)。交换两个轨道本征方向后可取
\[
d_0>0.
\]
中心二阶数据为
\[
u'(0)=-3,
\]
\[
d''(0)=12\coth d_0>12,
\]
并且
\[
L_0=6\coth d_0,
\]
\[
v'(0)=3+6\coth d_0,\qquad
w'(0)=3-6\coth d_0<-3,
\]
\[
H'(0)=3.
\]
这也直接验证
\[
S'(0)=\operatorname{Ric}_{q_0}^{\sharp}+3I.
\]
特别地，\(z\) 方向的本征值正好为 \(-3\)，另一个轨道方向更小。与 Step 75 的中心收缩结论一致。

此外
\[
K'(0)=0,
\]
但
\[
(\log K)''(0)=6+24\coth^2d_0>0.
\]

若原始标号满足 \(d_0<0\)，则相应结论是 \(d'(r)<0\)，且 \(|d|\) 增长；不能在不交换 \(b,c\) 的情况下直接写 \(d'>0\)。

---

## 4. 精确不变区

取从 \(r=0\) 出发、\(a,b,c>0\) 的任意连通光滑径向区间。由中心导数，
\[
u<0,\qquad p=d'>0
\]
在充分小的正 \(r\) 上成立。

只要这两个符号保持且 \(d>0\)，便有
\[
(\log K)'=-2u+2\coth d\,p>0,
\]
所以 \(K\) 严格增长。

若 \(u\) 首次从下方接触 \(0\)，则在接触点
\[
u'=3-K\le -3<0,
\]
与首次向上接触不相容。

若 \(p\) 首次从上方接触 \(0\)，则
\[
p'=2K\coth d>0,
\]
与首次向下接触不相容。

因此，在整个上述光滑区间内，
\[
\boxed{u(r)<0,\qquad d'(r)>0,\qquad K(r)>6\quad(r>0)}.
\]
\(H\) 无需具有任何符号：在 \(u=0\) 或 \(p=0\) 的接触面上，\(Hu\) 与 \(Hp\) 自动消失。\(H\) 会影响增长速率和径向延拓，但不影响这两个接触方向。

---

## 5. 小缺陷持续性与 \(\delta=3/5\)

令
\[
E=\operatorname{Ric}+3g,\qquad \|E\|_{\mathrm{op}}\le\delta,
\]
并用 \(E_r,E_z,E_b,E_c\) 表示不变正交标架中的对角分量。则
\[
u'+Hu=3-K-E_z,
\]
\[
p'+Hp=2K\coth d-(E_b-E_c).
\]

### 5.1 反射端数据

在反射端，Gauss 恒等式给出
\[
K_0:=K(0)
 =6-\bigl(E_z+E_b+E_c-E_r\bigr)_0.
\]
因此
\[
\boxed{K_0\ge6-4\delta}.
\]
中心导数还具有更好的分量消去：
\[
u'(0)=-3+E_b+E_c-E_r,
\]
所以
\[
u'(0)\le-3+3\delta.
\]
同时
\[
p'(0)=2K_0\coth d_0-(E_b-E_c),
\]
故
\[
p'(0)>2K_0-2\delta\ge12-10\delta.
\]

### 5.2 统一常数

若
\[
\boxed{\delta\le\frac35},
\]
则
\[
K_0\ge6-4\delta\ge3+\delta,
\]
而
\[
u'(0)\le-\frac65<0,\qquad p'(0)>6>0.
\]
所以局部仍有 \(u<0,p>0\)，并随即有 \(K'>0\)。

在任意后续 \(u=0\) 接触点，由于此时 \(K>K_0\)，
\[
u'=3-K-E_z\le3-K+\delta
   <3-K_0+\delta\le0.
\]
在任意 \(p=0\) 接触点，
\[
p'=2K\coth d-(E_b-E_c)
   >2K_0-2\delta>0.
\]
于是
\[
\boxed{
u(r)<0,\quad d'(r)>0,\quad
K(r)>K_0\ge6-4\delta
}
\]
在缺陷估计持续成立的整个连通光滑径向区间内成立。

因此，\(\delta<3/5\) 确实充分，但端点也可以包含：

\[
\boxed{\delta\le3/5\ \text{同样成立}.}
\]

数值 \(3/5\) 恰来自
\[
6-4\delta\ge3+\delta.
\]
更精确的按中心数据表述是：若实际 \(K_0>3+\delta\)，则同一论证对更大的 \(\delta\) 仍可使用；等号情形还需中心导数严格指向内部。仅从四个分量的点态估计出发，\(\delta>3/5\) 时下界 \(6-4\delta\) 已不足以保证 \(K_0\ge3+\delta\)，因而上述统一推导不再给出结论。

这里没有获得 \(u,p\) 离零的统一定量距离，也没有获得径向区间的全局存在性；这些问题会用到 \(H\) 的演化
\[
H'=3-(u^2+v^2+w^2)-E_r.
\]

---

## 6. 动量分量、非对角分量与脚本的 \(z=0\) 处理

这个模型没有额外的非平凡动量方程。切片上
\[
S=\operatorname{diag}(u,v,w)
\]
在不变标架中各本征值为空间常数，而且由上述连接系数可见
\[
\nabla_{e_i}e_i=0.
\]
故
\[
\operatorname{div}S=0,\qquad dH=0,
\]
Codazzi 公式给出
\[
\operatorname{Ric}_{ri}=0.
\]
切向 Ricci 与径向演化项在不变标架中也都为对角形，所以不存在另一个独立的非对角 Einstein 方程。

不过脚本只输出了 \(z=0\) 的坐标非对角分量。一般 \(z\) 上，坐标张量 \(\operatorname{Ric}_{xy}\) 不必为零，因为 \((x,y)\) 坐标标架相对 \((\omega_1,\omega_2)\) 正在旋转；真正为零的是不变标架中的非对角分量。切片齐性与上述结构方程补足了脚本未直接打印的一步。

---

## 7. 周期性

若 \(z\) 的周期为 \(2\pi\)，并要求 \(\omega_1,\omega_2\) 本身成为 \(T^3\) 上的全局一形式，则必须有
\[
\boxed{k\in\mathbb Z}.
\]
脚本中的局部符号计算允许任意非零实数 \(k\)，但紧致模型需要此量子化条件。更一般地，若 \(z\) 周长为 \(L\)，则需
\[
kL\in2\pi\mathbb Z.
\]

若只要求二次型 \(b^2\omega_1^2+c^2\omega_2^2\) 周期，而不要求两条 \(\omega_i\) 分别下降为全局一形式，则同时变号也不改变度量，因而在 \(2\pi\)-周期坐标中还可出现 \(2k\in\mathbb Z\) 的写法；这已不是题设所写的全局余标架版本。

---

## 8. 对图连接构造的数学含义

Step 77 的 PE 端要求
\[
S\longrightarrow I,
\]
特别是
\[
u=\frac{a'}a\longrightarrow1.
\]
但上述精确或小缺陷结论始终给出 \(u<0\)。事实上任意正径向端点都有
\[
\|S-I\|_{\mathrm{op}}\ge |u-1|>1.
\]
同时
\[
\|\operatorname{Ric}(q_r)\|_{\mathrm{op}}
 =\max\{K,|L|\}>K\ge6-4\delta,
\]
因为 \(d>0\) 时 \(L=K\coth d>K\)。因此切片也不能进入内蕴近乎平坦的扩张界面。

具体地说，若有一列该 Bianchi \(\mathrm{VII}_0\) 形式的有限连接段，均从反射 \(T^3\) 出发，并在整个连接段满足
\[
\sup\|\operatorname{Ric}+3g\|_{\mathrm{op}}=\delta_j\to0,
\]
那么对充分大的 \(j\)，每个正长度出口都满足
\[
u_j<0,\qquad
K_j\ge6-4\delta_j,
\]
因而既不能有 \(S_j-I\to0\)，也不能有切片内蕴 Ricci 趋零。这排除了该固定旋转标架、对角协同一维模型作为 Step 73 型扩张尾部的有限小缺陷入口；精确情形也不可能从反射端发展成 \(S\to I\) 的 PE 端。

仍未涉及的几何包括：具有 \(r,z\) 依赖的轨道矩阵、随 \(r\) 旋转的本征标架、非对角形算子、非零动量输运、更低对称性的中心，以及含有点态阶一缺陷层的连接。上述结论也不提供光滑区间的无限延拓；若解先发生尺度退化，它只说明该退化之前始终处于同一符号区。