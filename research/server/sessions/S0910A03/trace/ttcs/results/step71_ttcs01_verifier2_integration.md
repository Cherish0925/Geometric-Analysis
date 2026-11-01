# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 71,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step71_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step71_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the Li–Liu Type-I equation relevant to T^2-compatible anisotropic quotients. The source equation is (e^v)_{xi xi}+Delta_{T^2}v=0, with W=1-(xi/2)v_xi. For a one-angular-variable reduction v(xi,theta), derive the correct nonlinear PDE, its linearization around a constant bounded AH-cusp solution, Fourier radial branches, the slice-average conservation law, and the reflection/totally-geodesic condition translated into the Li–Liu metric variables if possible. Decide whether their BVP1 family can contain a totally geodesic T^3 level or whether Proposition 6.6/global geometry rules it out. Identify a mathematically meaningful finite-cylinder approximate matching experiment that preserves the nonlinear equation and quotient symmetry, without claiming it solves the full graph gluing.

## Integrated Scientific Memo

## Li–Liu Type-I 方程的核验结论

取平坦坐标
\[
g_{T^2}=d\theta^2+dy^2,\qquad v=v(\xi,\theta),
\]
且 \(v\) 与 \(y\) 无关。Type-I 方程化为
\[
\boxed{(e^v)_{\xi\xi}+v_{\theta\theta}=0}
\]
即
\[
\boxed{e^v(v_{\xi\xi}+v_\xi^2)+v_{\theta\theta}=0.}
\]
遗漏 \(v_\xi^2\) 会把非线性方程写错。由于主部系数为 \(e^v>0\) 与 \(1\)，这是 \((\xi,\theta)\) 上的椭圆方程，不是演化方程。若角向度量为 \(a^2d\theta^2\)，则第二项应为 \(a^{-2}v_{\theta\theta}\)。

### 1. 常数 AH-cusp 解、线性化与 Fourier 支

常数解 \(v\equiv v_0\) 满足
\[
W=1-\frac{\xi}{2}v_\xi=1,
\]
并给出平坦截面的实双曲 cusp
\[
h_0=\xi^{-2}\!\left(d\xi^2+d\tau^2+e^{v_0}(d\theta^2+dy^2)\right).
\]

令 \(v=v_0+\varepsilon u+O(\varepsilon^2)\)，线性化为
\[
\boxed{e^{v_0}u_{\xi\xi}+u_{\theta\theta}=0.}
\]
若 \(\theta\) 的周期为 \(P\)，写
\[
u=a_m(\xi)e^{i\kappa_m\theta},\qquad \kappa_m=\frac{2\pi m}{P},
\]
则
\[
a_m''-\mu_m^2a_m=0,\qquad
\mu_m=e^{-v_0/2}|\kappa_m|.
\]
因此
\[
a_m=A_me^{\mu_m\xi}+B_me^{-\mu_m\xi}\quad(m\neq0),
\qquad
a_0=A_0+B_0\xi.
\]
BVP1 的有界条件排除增长支和零模线性斜率。因此非零角向模按 \(e^{-\mu_m\xi}\) 衰减。若将该角向周期缩短 \(N\) 倍，则相应 \(\mu_m\) 增大 \(N\) 倍；不过这只描述给定商格上的频谱，不改变局部几何。

同时
\[
\delta W=-\frac{\xi}{2}u_\xi.
\]
对衰减模 \(u=Ce^{-\mu\xi}\cos(\kappa\theta)\)，
\[
\delta W=\frac{\mu\xi}{2}Ce^{-\mu\xi}\cos(\kappa\theta).
\]
非线性乘积会生成零模及高次谐波，故单 Fourier 模截断不保持精确方程。

### 2. 切片平均守恒律与 bundle degree

设
\[
F(\xi)=\int_{S^1}e^{v(\xi,\theta)}\,d\theta .
\]
积分方程得到
\[
\boxed{F''=0,\qquad F(\xi)=c_0+c_1\xi.}
\]
守恒对象是 \(e^v\) 的平均，而不是 \(v\) 的平均。BVP1 中 \(v\) 有界，故 \(F\) 有界，从而
\[
\boxed{c_1=0,\qquad F(\xi)\equiv F(0).}
\]

又由 \(W=1-\frac12\xi v_\xi\)，
\[
We^v=e^v-\frac{\xi}{2}(e^v)_\xi,
\]
所以
\[
\int We^v\,d\theta=c_0+\frac{c_1}{2}\xi,\qquad
\frac d{d\xi}\int We^v\,d\theta=\frac{c_1}{2}.
\]
因此 BVP1 中该导数为零。结合 Li–Liu 的 Chern 类公式，这正对应 degree \(0\)，故 link 是 \(T^3\)。这不要求连接曲率逐点为零。

### 3. \(\xi\)-level 的第二基本形式

在一角变量情形，可取径向规范
\[
\eta=d\tau+A(\xi,\theta)\,dy,
\]
其中
\[
A_\theta=(We^v)_\xi,\qquad A_\xi=-W_\theta.
\]
切片度量和单位法向量为
\[
q_\xi=\xi^{-2}\!\left(W^{-1}\eta^2+We^v(d\theta^2+dy^2)\right),
\qquad
N=\frac{\xi}{\sqrt W}\partial_\xi.
\]

记
\[
\alpha=\frac{\xi W_\xi}{W},\qquad
p=\xi v_\xi=2(1-W),\qquad
\beta=-\frac{\xi W_\theta}{2W^{3/2}e^{v/2}}.
\]
在适配于 \(\eta,\theta,y\) 的正交标架中，除法向方向的整体符号外，
\[
S=
\begin{pmatrix}
\dfrac{-2-\alpha}{2\sqrt W}&0&\beta\\[2mm]
0&\dfrac{-2+\alpha+p}{2\sqrt W}&0\\[2mm]
\beta&0&\dfrac{-2+\alpha+p}{2\sqrt W}
\end{pmatrix}.
\]
即使不使用非对角项，\(S=0\) 已要求
\[
-2-\alpha=0,\qquad -2+\alpha+p=0.
\]
两式推出 \(p=4\)，于是
\[
W=1-\frac p2=-1,
\]
与 Riemannian 条件 \(W>0\) 矛盾。因此
\[
\boxed{\text{任何 Riemannian Type-I 解都没有 totally geodesic 的 }\xi\text{-level}.}
\]

更强地，
\[
|S|^2
=\frac{(\alpha+2)^2+2(\alpha-2W)^2}{4W}+2\beta^2
\ge \frac23\frac{(1+W)^2}{W}
\ge \boxed{\frac83}.
\]
所以格点商虽可缩小截面体积，却不能令这些 coordinate levels 在局部范数中趋于 totally geodesic。

### 4. 是否可能有倾斜的 totally geodesic \(T^3\)

仅仅说“所有不变超曲面都是 \(\xi\)-level”不足以排除非不变、倾斜的嵌入 \(T^3\)。但 Type-I 度量是 ASD，这给出全局排除。

若某紧致 \(T^3\subset M\) totally geodesic，Codazzi 方程给出
\[
R(\nu,X,Y,Z)=0.
\]
由于环境度量满足 \(\operatorname{Ric}=-3h\)，常曲率部分在这一指标型中为零，故 Weyl 张量的磁部分 \(B\) 沿该超曲面为零。四维 ASD 条件 \(W^+=0\) 将 Weyl 的电、磁部分联系起来，因而电部分也为零，遂 \(W=0\) 沿超曲面。Gauss 方程随后表明诱导三维度量具有常截面曲率 \(-1\)。紧致 \(T^3\) 不可能承载这种度量。

故
\[
\boxed{\text{BVP1 家族中不存在任何 totally geodesic }T^3,}
\]
不仅限于 coordinate levels。

### 5. Proposition 6.6 的准确作用

Proposition 6.6 不是一般性排除理由；它要求 PE conformal infinity 的 Yamabe 常数非负。

* 非平坦 BVP1 边界由 Lemma 6.8 有 \(Y<0\)，故 Proposition 6.6 不适用。
* 平坦 \(T^3\) 边界有 \(Y=0\)，Proposition 6.6 强制刚性 warped product
  \[
  h=ds^2+e^{-2s}g_{T^3},
  \]
  即常数 \(v\) 的双曲 cusp 解；其 levels 满足 \(S=\pm I\)，仍非 totally geodesic。

所以一般 BVP1 的排除来自上面的 \(W=-1\) 局部矛盾及 ASD/Codazzi–Gauss 论证，而不是 Proposition 6.6。

### 6. 保持精确非线性方程的有限柱匹配实验

一个有数学意义的实验是：先规范化下端数据
\[
\phi_\varepsilon(\theta)
=v_0+\varepsilon\cos(m\theta)-\log I_0(\varepsilon),
\]
使
\[
\frac1{2\pi}\int_0^{2\pi}e^{\phi_\varepsilon}\,d\theta=e^{v_0}.
\]
然后在 \(0<\xi<L\) 解精确 Dirichlet 问题
\[
\begin{cases}
(e^v)_{\xi\xi}+v_{\theta\theta}=0,\\
v(0,\theta)=\phi_\varepsilon(\theta),\\
v(L,\theta)=v_0.
\end{cases}
\]
两端 \(e^v\) 平均相同，因此
\[
\int e^v\,d\theta\equiv2\pi e^{v_0},
\]
即严格处在 AH-compatible、degree-zero 分支。小 \(\varepsilon\) 时由椭圆扰动理论可保持 \(W>0\)，再由上式构造 \(\eta\)，所得柱体内部是精确 Einstein，而不是只满足某个截断的 tangential 方程。

一阶解为
\[
v-v_0
=\varepsilon\frac{\sinh(\mu(L-\xi))}{\sinh(\mu L)}
 \cos(m\theta)+O(\varepsilon^2),
\qquad
\mu=|m|e^{-v_0/2},
\]
故
\[
v_\xi(L,\theta)
=-\varepsilon\frac{\mu}{\sinh(\mu L)}\cos(m\theta)+O(\varepsilon^2),
\]
\[
W(L,\theta)-1
=\varepsilon\frac{L\mu}{2\sinh(\mu L)}
 \cos(m\theta)+O(\varepsilon^2).
\]
这定量检验各向异性数据向标准 cusp terminal data 的指数衰减。

实验应记录：

\[
\min W,
\quad
\|q_L-q_L^{\rm cusp}\|_{C^2},
\quad
\|S_L\mp I\|_{C^1},
\quad
\|d\eta_L\|_{C^1},
\]
并在用 cutoff 接到标准 cusp 后直接计算
\[
\|\operatorname{Ric}+3h\|_{\mathrm{op},\infty},
\]
包括法向一、二阶 jet。应同时核对 \(\eta\) 的 holonomy 和 quotient lattice。沿 \(\tau,y\) 的整数格点商保持 PDE、连接方程和所有局部曲率量，只改变界面总体积；若商作用于 \(\theta\)，则必须按实际新周期重算 Fourier 频率。

这个实验能产生“精确 Einstein 内部柱体 + 可量化 terminal attachment defect”，并检验 quotient symmetry 下的各向异性衰减；它不产生 totally geodesic wall，也不解决完整 graph gluing、约束相容性或闭流形装配。特别地，直接沿任意 \(\xi\)-level 反射加倍必有第二基本形式跳跃，因而在墙上产生非零分布曲率。