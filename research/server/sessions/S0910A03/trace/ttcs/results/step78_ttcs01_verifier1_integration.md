# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 78,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step78_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step78_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the rotating-eigenframe Bianchi VII_0 benchmark for the negative graph-connector route. Read the Step 78 symbolic script/output and the inherited Step 75/77 notes. For g=dr^2+a(r)^2 dz^2+b(r)^2 omega_1^2+c(r)^2 omega_2^2 with omega_1=cos(kz)dx+sin(kz)dy, omega_2=-sin(kz)dx+cos(kz)dy, d=log(b/c), u=a'/a, H=a'/a+b'/b+c'/c, and K=2k^2 a^{-2}sinh^2 d, check from first principles: intrinsic Ricci/scalar formulas; exact Ric=-3g ODEs u'+Hu=3-K, d''+Hd'=2K coth d, (log K)'=-2u+2 coth(d)d'; reflected center implications; and the proposed invariant-region proof u<0, d'>0, K>=6 for r>0. Then derive the sharpest elementary small-defect persistence statement under ||Ric+3g||_op<=delta, including whether delta<3/5 is correct, what interval it covers, and what role H plays. Identify any omitted momentum/off-diagonal equation or global-periodicity issue. Explain precisely what this rules out and what it leaves open for a finite vanishing-defect connector.

## Integrated Scientific Memo

# Bianchi \(\mathrm{VII}_0\) 旋转本征标架基准：核验结论

令
\[
e^0=dr,\qquad e^1=a\,dz,\qquad e^2=b\,\omega_1,\qquad e^3=c\,\omega_2,
\]
并记
\[
u=\frac{a'}a,\quad v=\frac{b'}b,\quad w=\frac{c'}c,\quad
H=u+v+w,\quad d=\log\frac bc,\quad p=d'=v-w.
\]

## 1. 切片内蕴曲率

由
\[
d\omega_1=k\,dz\wedge\omega_2,\qquad
d\omega_2=-k\,dz\wedge\omega_1
\]
得到
\[
de^2=\alpha\,e^1\wedge e^3,\qquad
de^3=-\beta\,e^1\wedge e^2,
\quad
\alpha=\frac{kb}{ac},\quad \beta=\frac{kc}{ab}.
\]
Koszul/Cartan 计算给出
\[
\begin{aligned}
\sec(e_1,e_2)&=\frac{(\alpha-\beta)(\alpha+3\beta)}4,\\
\sec(e_1,e_3)&=-\frac{(\alpha-\beta)(3\alpha+\beta)}4,\\
\sec(e_2,e_3)&=\frac{(\alpha-\beta)^2}{4}.
\end{aligned}
\]
定义
\[
K=\frac{(\alpha-\beta)^2}{2}
=\frac{k^2(b^2-c^2)^2}{2a^2b^2c^2}
=2k^2a^{-2}\sinh^2d,
\]
\[
L=\frac{\alpha^2-\beta^2}{2}
=\frac{k^2(b^4-c^4)}{2a^2b^2c^2}
=k^2a^{-2}\sinh(2d).
\]
则
\[
\boxed{\Ric_q=\operatorname{diag}(-K,L,-L)},\qquad
\boxed{R_q=-K}.
\]
当 \(d\neq0\) 时，
\[
L=K\coth d.
\]
在 \(d=0\) 处应使用光滑表达式 \(L=k^2a^{-2}\sinh(2d)\)，而不是分别解释 \(K\coth d\)。

此外
\[
\sec_q(e_2,e_3)=\frac K2.
\]
精确反射中心满足 \(K(0)=6\)，故该轨道平面曲率为 \(3\)，恰好达到 Step 75 中心定理的下界。

## 2. 四维 Ricci 与完整对角 Einstein 系统

协同一维公式为
\[
\begin{aligned}
\Ric_{rr}&=-H'-(u^2+v^2+w^2),\\
\Ric_{11}&=-K-u'-Hu,\\
\Ric_{22}&=L-v'-Hv,\\
\Ric_{33}&=-L-w'-Hw.
\end{aligned}
\]
因此 \(\Ric=-3g\) 等价于
\[
u'+Hu=3-K,\qquad
v'+Hv=3+L,\qquad
w'+Hw=3-L,
\]
加上径向方程。相减即得
\[
\boxed{d''+Hd'=2K\coth d}.
\]
从 \(K=2k^2a^{-2}\sinh^2d\) 直接微分得到纯运动学恒等式
\[
\boxed{(\log K)'=-2u+2\coth(d)d'}.
\]
所以 Step 78 的三个方程及符号均正确。

脚本没有显式列出的约束为
\[
\boxed{H^2-(u^2+v^2+w^2)=6-K},
\]
等价地
\[
K=6-H^2+u^2+v^2+w^2.
\]
还有
\[
H'=3-(u^2+v^2+w^2)=9-H^2-K.
\]
这说明 \((u,d,K)\) 本身不是闭合的 Einstein 构造系统；需要 \(H\) 或 \(v+w\)。但下述符号不变区只使用那三个必要方程。

## 3. 反射中心数据

反射要求 \(a,b,c\) 为 \(r\) 的偶函数，故
\[
u(0)=v(0)=w(0)=H(0)=d'(0)=0.
\]
Hamilton 约束或 \(R_{q_0}=-6\) 给出
\[
\boxed{K(0)=6}.
\]
因此 \(d_0=d(0)\neq0\)。交换 \(b,c\) 后可设 \(d_0>0\)。此时
\[
u'(0)=-3,\qquad
d''(0)=12\coth d_0>0,
\]
\[
v'(0)=3+6\coth d_0,\qquad
w'(0)=3-6\coth d_0,\qquad H'(0)=3.
\]
此外
\[
K'(0)=0,\qquad
(\log K)''(0)=6+24\coth^2d_0>0.
\]
若不交换标号且 \(d_0<0\)，正确结论是 \(d'<0\) 且 \(|d|\) 增长。

## 4. 精确不变区

中心二阶数据首先给出小正 \(r\) 上
\[
u<0,\qquad p=d'>0.
\]
只要 \(u<0,p>0,d>0\)，就有
\[
(\log K)'=-2u+2\coth(d)p>0,
\]
故 \(K>6\)。

若 \(u\) 首次从负侧接触 \(0\)，则
\[
u'=3-K\le -3<0,
\]
不可能向上越过。若 \(p\) 首次从正侧接触 \(0\)，则
\[
p'=2K\coth d>0,
\]
不可能向下越过。因此在由中心出发、\(a,b,c>0\) 的整个最大光滑前向区间上，
\[
\boxed{u(r)<0,\qquad d'(r)>0,\qquad K(r)>6\quad(r>0)}.
\]

这里完全不要求 \(H\) 有确定符号：在接触面 \(u=0\) 或 \(p=0\) 上，阻尼项 \(Hu,Hp\) 自动消失；等价地可用正积分因子
\[
\mu(r)=\exp\!\int_0^rH(s)\,ds.
\]
\(H\) 仍控制增长速率及解能否延拓，但不影响该不变区的符号。

## 5. 小缺陷持久性及 \(3/5\) 阈值

设
\[
E=\Ric+3g,\qquad \|E\|_{\mathrm{op}}\le\delta.
\]
在不变正交标架中，
\[
u'+Hu=3-K-E_z,
\]
\[
p'+Hp=2K\coth d-(E_b-E_c).
\]
反射中心的 Gauss 约束给出
\[
K_0:=K(0)
=6-\bigl(E_z+E_b+E_c-E_r\bigr)_0,
\]
故
\[
\boxed{K_0\ge6-4\delta}.
\]
中心导数有更强的分量消去：
\[
u'(0)=-3+E_b+E_c-E_r\le-3+3\delta,
\]
而
\[
p'(0)=2K_0\coth d_0-(E_b-E_c)
>2K_0-2\delta\ge12-10\delta.
\]

保持 \(u<0,p>0\) 后，\(K\) 严格增加。后续 \(u=0\) 接触点满足
\[
u'\le 3-K+\delta.
\]
因此统一充分条件是
\[
K_0\ge3+\delta.
\]
由最坏情形下界 \(K_0\ge6-4\delta\)，这等价于
\[
6-4\delta\ge3+\delta
\quad\Longleftrightarrow\quad
\boxed{\delta\le\frac35}.
\]

端点 \(\delta=3/5\) 也可包括：此时中心仍有严格指向内部的数据
\[
u'(0)\le-\frac65<0,\qquad p'(0)>6,
\]
而任意正时刻都有 \(K>K_0\)，所以后续 \(u=0\) 接触处实际仍有 \(u'<0\)。故最强的这一初等统一陈述为：

> 若反射中心满足 \(d_0>0\)，并且在由中心出发的某个连通光滑径向区间 \(I=[0,R)\) 上
> \[
> \|\Ric+3g\|_{\mathrm{op}}\le\delta\le\frac35,
> \]
> 则对所有 \(r\in(0,R)\),
> \[
> \boxed{
> u(r)<0,\qquad d'(r)>0,\qquad
> K(r)>K_0\ge6-4\delta.
> }
> \]

这里 \(R\) 可以是任意有限出口，也可以是最大光滑存在时间；结论不证明 \(R=\infty\)，也不给出 \(u,d'\) 与零之间的统一定量间隙。

\(3/5\) 是仅使用 \(\|E\|_{\rm op}\le\delta\) 和中心最坏情形下界时的自然阈值，不是已证明的几何最优阈值。若实际中心数据满足 \(K_0>3+\delta\)，同一证明可覆盖更大的 \(\delta\)。

## 6. 动量、非对角方程与周期性

在不变标架中
\[
S=\operatorname{diag}(u,v,w),
\]
且本征值在每个齐性切片上为空间常数。直接 Cartan 计算给出
\[
\Ric_{ri}=0,\qquad \Ric_{ij}=0\quad(i\neq j)
\]
恒等成立，因此没有遗漏的非平凡动量或非对角 Einstein 方程。脚本只在 \(z=0\) 打印坐标非对角分量；一般 \(z\) 的坐标 \(\Ric_{xy}\) 未必为零，因为坐标标架在旋转，但不变标架中的 Ricci 始终对角。

全局性方面，若 \(z\sim z+2\pi\) 且要求 \(\omega_1,\omega_2\) 各自成为全局一形式，则必须
\[
\boxed{k\in\mathbb Z}.
\]
更一般地，\(z\) 周长为 \(L\) 时要求 \(kL\in2\pi\mathbb Z\)。若只要求二次型下降而容许 \((\omega_1,\omega_2)\) 同时变号，则还可出现半整数转角；这不是脚本声明的“全局余标架”版本。还必须有 \(k\neq0\)，否则 \(K\equiv0\)，与反射中心 \(K_0\approx6\) 不相容。

## 7. 对有限消失缺陷连接器的精确含义

Step 73/77 型扩张尾部入口要求至少
\[
S\to I,\qquad\text{特别是 }u\to1,
\]
并要求适当缩放后的切片内蕴曲率趋零。但本模型在 \(\delta\le3/5\) 时始终满足
\[
u<0,\qquad K\ge6-4\delta.
\]
因而任意正长度出口都有
\[
\|S-I\|_{\mathrm{op}}\ge |u-1|>1.
\]
同时
\[
\|\Ric(q_r)\|_{\mathrm{op}}
=\max\{K,|L|\}=|L|>K\ge6-4\delta
\]
（这里 \(d>0\)，故 \(\coth d>1\)）。因此它不能到达“小 \(S-I\)、小切片内蕴曲率”的扩张接口。

特别地，不存在一列保持该固定 Bianchi \(\mathrm{VII}_0\) 旋转标架、对角协同一维形式的反射连接段，使
\[
\sup\|\Ric+3g\|_{\mathrm{op}}\to0
\]
并在有限出口逼近 Step 73 所需的扩张入口。精确 Einstein 情形同样不可能演化到 \(u\to1\) 的 PE 端。

这并不证明必然发生有限距离 pinch 或曲率奇性；符号论证只排除所需扩张行为。仍然开放的是：

- \(r\)-依赖本征标架旋转或一般非对角轨道矩阵；
- 非对角形算子及非平凡动量输运；
- 更低对称性中心；
- 非反射起点；
- 含阶一缺陷层、或不在全段满足小缺陷界的连接；
- \(\delta>3/5\) 的几何行为；
- 该解的完整性、最大延拓及最终奇性类型。

因此这是对负图连接路线中一个自然但严格受限的 benchmark ansatz 的稳健否定，而不是对所有有限消失缺陷连接器的否定。