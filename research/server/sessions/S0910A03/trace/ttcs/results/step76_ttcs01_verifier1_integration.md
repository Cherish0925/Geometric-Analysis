# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 76,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step76_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step76_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

For the Yau-26 negative graph-manifold route, verify and sharpen the new center-energy/transport synthesis from first principles. In the diagonal orthogonally-transitive class, derive with correct physical measures: (i) the periodic center identity for q=ds^2+G(s), rho=sqrt(det G), h=rho'/rho, A0=A-(h/2)I, including the approximate scalar error e=R_q+6; (ii) the diagonal d=b-c specialization and its normalization under lattice quotients; (iii) the invariant exact and forced equations div_gamma(rho grad d)=-rho(E_x-E_y), total signed flux, boundary covariance pairing with arbitrary constant c, and all signs; (iv) the slice evolution F'(r) in Gaussian distance; and (v) for one Fourier mode on an expanding flat-cusp background, the reflection-normalized solution, asymptotic derivative, weighted pairing, and normalized decay. State exactly whether these identities imply a positive Ricci-defect cost or instead exhibit a feasible energy-dilution mechanism, and identify assumptions needed for either conclusion.

## Integrated Scientific Memo

# 核验结论：中心能量、通量输运与膨胀稀释

以下均限于对角、正交传递类。所有积分都使用物理测度；设轨道格点 \(\Lambda\subset\mathbb R^2\) 的坐标余体积为 \(\mathcal A_\Lambda\)。

## 1. 周期中心恒等式

令
\[
q=ds^2+G(s)_{ab}dx^a dx^b,\qquad s\in\mathbb R/L\mathbb Z,
\]
并定义
\[
\rho=\sqrt{\det G},\qquad
A=\frac12G^{-1}G',\qquad
h=\operatorname{tr}A=\frac{\rho'}{\rho},\qquad
A_0=A-\frac h2I.
\]
由于 \(T^2\) 轨道内蕴平坦，
\[
R_q=-2h'-|A|^2-h^2
    =-2h'-|A_0|^2-\frac32h^2.
\tag{1}
\]
写
\[
e=R_q+6.
\]
利用周期性及 \(\rho'=\rho h\)，
\[
\int_0^L\rho h'\,ds=-\int_0^L\rho h^2\,ds.
\]
因此
\[
\boxed{
\int_0^L\rho |A_0|^2\,ds
=
6\int_0^L\rho\,ds
+\frac12\int_0^L\rho h^2\,ds
-\int_0^L\rho e\,ds.
}
\tag{2}
\]
脚本中以 \(h'\mapsto-h^2\) 表示的只是这个**积分后**替换，不是点态等式。

若该切片是四维高斯度量 \(g=dr^2+q_r\) 的全测地反射面，且
\[
E=\operatorname{Ric}_g+3g,
\]
则 Gauss 标量公式给出
\[
e=\operatorname{tr}_{Tq}E-E_{nn}.
\tag{3}
\]
故 \(\|E\|_{\rm op}\le\delta\) 时
\[
|e|\le4\delta.
\tag{4}
\]

## 2. 对角特化及格点商归一化

若
\[
G=\operatorname{diag}(e^{2b},e^{2c}),\qquad
d=b-c,\qquad \sigma=b+c,
\]
则
\[
\rho=e^\sigma,\qquad h=b_s+c_s,\qquad
A_0=\frac{d_s}{2}\operatorname{diag}(1,-1),
\qquad |A_0|^2=\frac12d_s^2.
\]
于是
\[
\boxed{
\int_0^L\rho d_s^2\,ds
=
12\int_0^L\rho\,ds
+\int_0^L\rho h^2\,ds
-2\int_0^L\rho e\,ds.
}
\tag{5}
\]
以
\[
\langle f\rangle_\rho=
\frac{\int\rho f}{\int\rho}
\]
归一化，
\[
\boxed{
\langle d_s^2\rangle_\rho
=12+\langle h^2\rangle_\rho-2\langle e\rangle_\rho.
}
\tag{6}
\]
特别地，
\[
e=0\implies \langle d_s^2\rangle_\rho\ge12,
\qquad
\|E\|_{\rm op}\le\delta
\implies \langle d_s^2\rangle_\rho\ge12-8\delta.
\tag{7}
\]

物理体积元为
\[
d\mu_q=\mathcal A_\Lambda\,\rho\,ds,\qquad
\operatorname{Vol}(q)=\mathcal A_\Lambda\int\rho\,ds.
\]
有限格点商或共同轨道缩放使能量与体积乘上同一常数，故 (6)–(7) 不变。各向异性常数缩放只令 \(d\) 加常数，不改变 \(d_s\)。因此格点塌缩不能降低归一化中心能量。

## 3. 不变强迫方程、符号通量与协方差配对

对
\[
g=\gamma+e^{2b}dx^2+e^{2c}dy^2
\]
定义
\[
d=b-c,\qquad \rho=e^{b+c},\qquad X=E_x-E_y,
\]
其中 \(E_x,E_y\) 是正交归一轨道方向上的分量。轨道 Ricci 分量之差为
\[
\operatorname{Ric}_x-\operatorname{Ric}_y
=-\rho^{-1}\operatorname{div}_\gamma(\rho\nabla_\gamma d).
\]
所以正确符号是
\[
\boxed{
\operatorname{div}_\gamma(\rho\nabla_\gamma d)=-\rho X.
}
\tag{8}
\]

令 \(\Omega=[r_0,r_1]\times S^1\)，\(r\) 向外增加，并在高斯距离中写
\[
\gamma=dr^2+\alpha(r,z)^2dz^2,\qquad d\ell_r=\alpha\,dz.
\]
物理总符号通量为
\[
Q(r)=\mathcal A_\Lambda\int_{C_r}\rho d_r\,d\ell_r.
\tag{9}
\]
由 (8)，
\[
\boxed{
Q(r_1)-Q(r_0)
=-\mathcal A_\Lambda\int_\Omega\rho X\,d\mu_\gamma.
}
\tag{10}
\]
精确 Einstein 情形 \(X=0\) 时 \(Q\) 守恒；反射条件 \(d_r(r_0)=0\) 给出
\[
Q(r)\equiv0.
\tag{11}
\]
这只是**总符号通量为零**，不意味着通量密度逐点为零。

对任意常数 \(c\)，定义
\[
F_c(r)=\mathcal A_\Lambda
\int_{C_r}(d-c)\rho d_r\,d\ell_r.
\tag{12}
\]
乘 (8) 以 \(d-c\) 并分部积分，得到
\[
\boxed{
F_c(r_1)-F_c(r_0)
=
\mathcal A_\Lambda\int_\Omega\rho|\nabla d|^2\,d\mu_\gamma
-\mathcal A_\Lambda\int_\Omega(d-c)\rho X\,d\mu_\gamma.
}
\tag{13}
\]
等价地，
\[
\int_\Omega\rho|\nabla d|^2
=
\mathcal A_\Lambda^{-1}\!\left(F_c(r_1)-F_c(r_0)\right)
+\int_\Omega(d-c)\rho X.
\tag{14}
\]
精确反射情形中
\[
\boxed{
F_c(R)=\mathcal A_\Lambda\int_{\Omega_R}\rho|\nabla d|^2\,d\mu_\gamma,
}
\tag{15}
\]
且因 \(Q=0\)，它与 \(c\) 无关。这正是零总质量的符号测度
\[
\rho d_r\,d\ell_r
\]
和非常数 \(d\) 的协方差配对。

若精确外界面满足 \(d_r(R)\equiv0\)，则 \(F_c(R)=0\)，从而 \(d\) 为常数。故非恒定精确解不能在有限距离达到两轨道方向完全脐；但强迫情形可由体源 \(X\) 支付能量，不能推出同一结论。

## 4. 高斯距离中的切片演化

方程 (8) 的坐标形式是
\[
\partial_r(\alpha\rho d_r)
+\partial_z(\rho\alpha^{-1}d_z)
=-\alpha\rho X.
\tag{16}
\]
于是
\[
Q'(r)=-\mathcal A_\Lambda\int_{C_r}\rho X\,d\ell_r,
\tag{17}
\]
以及
\[
\boxed{
F_c'(r)=\mathcal A_\Lambda\int_{C_r}\rho
\left(d_r^2+|\nabla_{C_r}d|^2-(d-c)X\right)d\ell_r.
}
\tag{18}
\]
没有遗漏额外的平均曲率项；它已包含在
\(\partial_r(\alpha\rho)\) 中。

精确情形：
\[
F_c'(r)=N(r)+Z(r),
\tag{19}
\]
其中
\[
N(r)=\mathcal A_\Lambda\int_{C_r}\rho d_r^2\,d\ell_r,\qquad
Z(r)=\mathcal A_\Lambda\int_{C_r}\rho|\nabla_{C_r}d|^2\,d\ell_r.
\]
二者均非负。反射中心处 \(d_r(0)=0\)，且中心切向弧长为 \(ds=d\ell_0\)，故
\[
F_c'(0)=\mathcal A_\Lambda\int\rho d_s^2\,ds.
\tag{20}
\]
结合 (5)，
\[
F_c'(0)=12V_0+
\mathcal A_\Lambda\int\rho h^2ds
-2\mathcal A_\Lambda\int\rho e\,ds,
\tag{21}
\]
其中 \(V_0=\mathcal A_\Lambda\int\rho ds\)。精确标量 \(-6\) 时
\[
F_c'(0)\ge12V_0.
\tag{22}
\]

在强迫情形，(18) 还含有
\[
-\mathcal A_\Lambda\int\rho(d-c)X\,ds.
\]
即使 \(|X|\le2\delta\)，也只有
\[
\left|\int\rho(d-c)X\right|
\le2\delta\int\rho|d-c|,
\tag{23}
\]
故没有振幅、Poincaré 或振荡控制时，不能仅由 \(\delta\) 控制该项。

此外，单点斜率下界 (22) 不自动给出固定厚度的能量下界；那需要统一的径向正则性、椭圆性及体积比较。

## 5. 膨胀平坦尖端上的单 Fourier 模式

取
\[
g_d=dt^2+e^{2t}dz^2
+\ell_x^2e^{2t+d}dx^2
+\ell_y^2e^{2t-d}dy^2.
\tag{24}
\]
这里
\[
\gamma=dt^2+e^{2t}dz^2,\qquad
\rho=\ell_x\ell_y e^{2t}.
\]
齐次各向异性方程为
\[
\partial_t(e^{3t}d_t)+\partial_z(e^td_z)=0.
\tag{25}
\]
令
\[
d(t,z)=A\psi_k(t)\cos(kz),
\]
则
\[
\psi_k''+3\psi_k'-k^2e^{-2t}\psi_k=0.
\tag{26}
\]
对反射归一条件
\[
\psi_k(0)=1,\qquad \psi_k'(0)=0,
\]
设 \(x=ke^{-t}\)，精确解为
\[
\boxed{
\psi_k(t)=
\frac{e^{x-k}(x-1)+e^{k-x}(x+1)}{2k}.
}
\tag{27}
\]
其导数为
\[
\boxed{
\psi_k'(t)=\frac{x^2}{k}\sinh(k-x).
}
\tag{28}
\]
故
\[
\psi_k(\infty)=\frac{\sinh k}{k},
\tag{29}
\]
且固定 \(k\) 时
\[
\psi_k'(t)
=k\sinh k\,e^{-2t}
-k^2\cosh k\,e^{-3t}
+O_k(e^{-4t}),
\tag{30}
\]
特别是
\[
e^{2t}\psi_k'(t)\longrightarrow k\sinh k.
\tag{31}
\]
因此固定频率下法向导数衰减，但传递因子随 \(k\) 指数增长，不存在由此得到的频率一致逆估计。

若 \(z\)-周期为 \(L\)，且 \(\int_0^L\cos^2(kz)\,dz=L/2\)，记
\[
V_0=\mathcal A_\Lambda\ell_x\ell_yL,\qquad
V(t)=V_0e^{3t}.
\]
总符号通量因 \(\int\cos(kz)=0\) 而为零，但配对为
\[
\boxed{
F(t)=\frac{A^2V_0}{2}e^{3t}\psi_k\psi_k'.
}
\tag{32}
\]
ODE 给出
\[
\boxed{
F'(t)=\frac{A^2V_0}{2}
\left(e^{3t}\psi_k'^2+k^2e^t\psi_k^2\right).
}
\tag{33}
\]
于是
\[
F(t)\sim \frac{A^2V_0}{2}\sinh^2(k)e^t,
\tag{34}
\]
但归一化后
\[
\boxed{
\frac{F(t)}{V(t)}
=\frac{A^2}{2}\psi_k\psi_k'
\sim\frac{A^2}{2}\sinh^2(k)e^{-2t},
}
\tag{35}
\]
以及
\[
\boxed{
\frac{F'(t)}{V(t)}
=\frac{A^2}{2}\left(\psi_k'^2+k^2e^{-2t}\psi_k^2\right)
\sim\frac{A^2}{2}\sinh^2(k)e^{-2t}.
}
\tag{36}
\]
这里未归一化的协方差可增长，而强度量（每单位物理体积）衰减。

该度量满足 \(E_x=E_y=0\)，但剩余基底缺陷为
\[
E|_\gamma=-\frac12\,dd\otimes dd.
\tag{37}
\]
故它不是完整的精确 Einstein 解；对固定 \(k\)，
\[
\|E\|_{\rm op,\infty}
\sim\frac{A^2}{2}\sinh^2(k)e^{-2t}.
\tag{38}
\]
此外 \(t=0\) 处完整形算子不是 \(S=0\)，所以这是膨胀区输运模型，不是反射 Einstein 核。若频率变化，出口归一化稀释至少要求
\[
A_j e^{-R_j}\sinh k_j\to0.
\tag{39}
\]

## 6. 科学含义：目前是稀释机制，不是正缺陷代价

这些恒等式严格推出：

1. 反射中心存在格点归一化不变的阶一能量：
   \[
   \langle d_s^2\rangle_\rho\ge12
   \quad(e=0).
   \]
2. 精确输运的总符号通量为零，但 Dirichlet 能量由边界协方差承担。
3. 非恒定精确解不能在有限出口满足 \(d_r\equiv0\)。
4. 膨胀尖端允许 \(d_r\to0\)、总配对增长，而每体积配对和能量密度趋零。

因此，这条恒等式链**不推出维数一致的正 Ricci 缺陷下界**；它反而展示了一个相容的能量稀释机制。值得纠正的是：单 Fourier 模式本身并非 \(E\equiv0\) 的四维模型——它只消除了轨道差分方程 \(E_x-E_y\)，仍有二次基底缺陷 (37)。

要从这些公式得到正缺陷代价，至少需要与退化及物理长度无关的统一估计，例如：

- 中心切向能量在固定物理厚度内持续存在；
- 统一椭圆性、径向正则性和切片体积控制；
- 对 \(d-c\) 的统一 Poincaré/振荡界；
- 出口面积与 \(d_r\) 的联合控制；
- 足以压制 \(\sinh k\) 放大的频率或 Sobolev 控制；
- 对全部 Ricci 分量及 Hamilton–momentum 约束的控制，而非仅 \(E_x-E_y\)。

反之，要把稀释机制升级成负图流形构造，还缺少：从全测地标量 \(-6\) 中心到大尺度近脐膨胀切片的全非线性小缺陷连接、沿途的
\[
e^{-2a}\|\operatorname{Ric}(q_r)\|
\]
控制、全部端点 jets 的匹配，以及完整约束传播。现有恒等式既不排除也不构造这个核心连接；这正是尚未解决的科学对象。