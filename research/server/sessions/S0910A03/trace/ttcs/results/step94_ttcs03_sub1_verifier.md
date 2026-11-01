# TTCS Independent Branch Record

```json
{
  "step_id": 94,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step94_charged_koiso_separator.py",
    "Sessions/S0910A03/workspace/data/step94_charged_koiso_separator.json",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/trace/ttcs/results/step92_ttcs02_verifier1_integration.md",
    "Sessions/S0910A03/workspace/notes/step88_source_note_twist.md",
    "Sessions/S0910A03/workspace/notes/step90_structured_forced_twist_and_radial_escape.md"
  ]
}
```

## Task

Verify the proposed charged Koiso separator construction in full detail. The hypersurface metric is qSigma=ds^2+M(U(s)) on T^3, det M=1. Choose fixed charge covector q, mixed Weingarten covector m=-q/2 (orientation convention), a hyperbolic target circle U of constant speed squared 12+2S with 0<S<3, physical separator charge Q(s)=1/2 q^T M^-1q scaled so Q<S, P=S-Q, and vertical tracefree Weingarten B=sqrt(P/2) M^-1 dM(N), N target-normal to U_s. Check: (i) the full block Weingarten endomorphism and its self-adjointness; (ii) tr W=0 and tr W^2=P+Q=S, including the factor 2 in the mixed block; (iii) scalar curvature and Hamiltonian constraint for lambda=-3; (iv) every momentum component, especially whether constant covector m really makes vertical momentum vanish after all connection terms and whether s-momentum remains tr(A B)=0 despite mixed W; (v) the Gaussian-gauge relation between m and the twist charge q, including rho factors and orientation; (vi) full—not merely invariant—strict stability and whether the potential is exactly 3-S for all torus Fourier modes; (vii) analyticity/global periodicity of the wound target circle and applicability of Koiso. Identify any hidden obstruction or needed modification. State exactly what a valid construction would establish and what global two-ended work remains.

## Output

# 科学核验备忘录

## 总结

该带电 Koiso separator 构造在所给归一化下成立。取严格不等式
\[
0<S<3,\qquad \max_{S^1}Q<S,
\]
则 \((q_\Sigma,W)\) 是 \(T^3\) 上的全局解析 Cauchy 数据，精确满足四维
\(\operatorname{Ric}=-3g\) 的 Hamilton–momentum 约束。Koiso 解析 Cauchy 定理由此给出
\[
(-\varepsilon,\varepsilon)\times T^3
\]
上的局部解析 Einstein 度量。中心 \(T^3\) 极小且对所有变化严格稳定，并携带非零守恒 twist charge。

需要明确的两点是：

1. momentum 的垂直分量还包含收缩联络项
   \(\Gamma^i{}_{is}m_a=(\operatorname{tr}A)m_a\)，但因
   \(\det M=1\) 而精确为零；其余两个联络项互相抵消。
2. 所有 Fourier 模共有的 Jacobi 零阶势是 \(3-S\)；非零 torus 模的一维有效势还包含
   \(k^TM^{-1}k\ge0\)。因此最低特征值恰为 \(3-S\)。

没有发现因子、符号以外的潜在障碍。

---

## 1. 完整 Weingarten 块及自伴性

为避免与超曲面度量混淆，记固定 charge covector 为
\(\mathfrak q=(\mathfrak q_a)\)，并令
\[
m_a=-\frac12\mathfrak q_a,\qquad m^a=M^{ab}m_b.
\]
在坐标基
\[
(\partial_s,\partial_{x^1},\partial_{x^2})
\]
中定义
\[
W^i{}_j=
\begin{pmatrix}
0&m_b\\
m^a&B^a{}_b
\end{pmatrix}.
\]
等价地，
\[
W(\partial_s)=m^a\partial_{x^a},\qquad
W(\partial_{x^a})=m_a\partial_s+B^b{}_a\partial_{x^b}.
\]

设
\[
C_X:=M^{-1}dM(X),\qquad
\langle X,Y\rangle_{\mathbb H^2}
=\frac12\operatorname{tr}(C_XC_Y),
\]
以及
\[
B=\sqrt{\frac P2}\,C_N.
\]
因为 \(\det M=1\)，
\[
\operatorname{tr}C_N=N(\log\det M)=0.
\]
又因 \(N\) 是靶空间单位向量，
\[
\frac12\operatorname{tr}(C_N^2)=1.
\]

自伴性可直接从
\[
(q_\Sigma)_{ik}W^k{}_j=
\begin{pmatrix}
0&m_b\\
m_a&(MB)_{ab}
\end{pmatrix}
\]
看出。这里
\[
MB=\sqrt{\frac P2}\,dM(N)
\]
是对称矩阵，所以整个下指标形式均对称。脚本中的
`W_self_adjoint` 最大残差为 \(3.33\times10^{-16}\)，与此精确计算一致。

---

## 2. 迹和混合块的因子 \(2\)

由 \(B\) 无迹，
\[
\operatorname{tr}W=\operatorname{tr}B=0.
\]
对块矩阵平方取迹得到
\[
\operatorname{tr}(W^2)
=\operatorname{tr}(B^2)+2m_am^a.
\]
靶空间归一化给出
\[
\operatorname{tr}(B^2)
=\frac P2\operatorname{tr}(C_N^2)=P.
\]
另一方面，
\[
2m_am^a
=2m^TM^{-1}m
=\frac12\mathfrak q^TM^{-1}\mathfrak q
=Q.
\]
因此
\[
\boxed{\operatorname{tr}W=0},\qquad
\boxed{|II|^2=\operatorname{tr}(W^2)=P+Q=S}.
\]

混合块中的因子 \(2\) 来自 \(W^2\) 的 \(ss\) 对角贡献和垂直块对角贡献各出现一次；不能只计其中一个。

---

## 3. 标量曲率和 Hamiltonian 约束

令
\[
A=\frac12M^{-1}M_s.
\]
度量
\[
q_\Sigma=ds^2+M_{ab}(s)\,dx^a dx^b
\]
的非零 Christoffel 符号为
\[
\Gamma^a{}_{sb}=\Gamma^a{}_{bs}=A^a{}_b,\qquad
\Gamma^s{}_{ab}=-(MA)_{ab}.
\]
其标量曲率为
\[
\operatorname{Scal}_{q_\Sigma}
=-2(\operatorname{tr}A)_s-(\operatorname{tr}A)^2-\operatorname{tr}(A^2).
\]
由于
\[
\operatorname{tr}A
=\frac12\partial_s\log\det M=0,
\]
可得
\[
\operatorname{Scal}_{q_\Sigma}=-\operatorname{tr}(A^2).
\]
而
\[
e_s:=|U_s|^2
=\frac12\operatorname{tr}\bigl[(M^{-1}M_s)^2\bigr]
=2\operatorname{tr}(A^2),
\]
所以
\[
\boxed{\operatorname{Scal}_{q_\Sigma}=-\frac12e_s}.
\]
取恒定速度
\[
e_s=12+2S
\]
便有
\[
\boxed{\operatorname{Scal}_{q_\Sigma}=-6-S}.
\]

四维 Einstein 常数 \(\lambda=-3\) 的 Gauss 约束为
\[
\operatorname{Scal}_{q_\Sigma}
+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2
=(3-1)\lambda=-6.
\]
代入上述量：
\[
(-6-S)+S-0=-6.
\]
Hamiltonian 约束精确成立。

---

## 4. 全部 momentum 分量

记
\[
D_j:=\nabla_iW^i{}_j.
\]
坐标公式为
\[
D_j=\partial_iW^i{}_j
+\Gamma^i{}_{i\ell}W^\ell{}_j
-\Gamma^\ell{}_{ij}W^i{}_\ell.
\]

### \(s\) 分量

平移不变性使所有 \(x^a\) 导数消失；又因 \(W^s{}_s=0\)，得到
\[
D_s=-A^b{}_aB^a{}_b=-\operatorname{tr}(AB).
\]
混合块 \(m\) 不出现在这一分量中。由
\[
A=\frac12C_{U_s},\qquad
B=\sqrt{\frac P2}C_N,
\]
可得
\[
\operatorname{tr}(AB)
=\sqrt{\frac P2}\,
\langle U_s,N\rangle_{\mathbb H^2}=0.
\]
故
\[
D_s=0.
\]

### 垂直分量

对每个 \(a\)，完整计算为
\[
D_a
=m'_a+(\operatorname{tr}A)m_a
-A^b{}_am_b+(MA)_{ba}m^b.
\]
其中
\[
(MA)_{ba}m^b=A^c{}_am_c,
\]
所以最后两项相消。又有
\[
\operatorname{tr}A=0
\]
以及固定坐标 covector 给出的
\[
m'_a=0.
\]
因此
\[
\boxed{D_a=0}.
\]

这也说明“\(m\) 固定”应理解为它在全局 torus 共标架
\(dx^a\) 中的分量固定。若取随 \(s\) 变化的 \(m_a(s)\)，垂直 momentum 就留下 \(m'_a\)。

因此无论采用
\(\delta W=-\nabla_iW^i{}_j\) 还是相反散度符号，
\[
d(\operatorname{tr}W)+\delta W=0
\]
均成立。脚本中的 `momentum_s` 为
\(6.66\times10^{-16}\)，两个显式联络项的抵消残差为零。

---

## 5. Gaussian gauge 中 \(m\) 与 twist charge 的关系

取 Koiso Gaussian 坐标
\[
g=dt^2+q_t,\qquad \nu=\partial_t,
\]
并采用文件中的约定
\[
II(X,Y)=q_\Sigma(WX,Y)=-\frac12\dot q_t(X,Y).
\]
在 Kaluza–Klein 分解中写
\[
g=\gamma_{ij}dy^i dy^j+
G_{ab}(dx^a+A_i^a dy^i)(dx^b+A_j^bdy^j).
\]
中心处
\[
A_s=0,\qquad A_t=0,\qquad G=M,\qquad
\gamma=dt^2+ds^2,\qquad \rho=\sqrt{\det G}=1.
\]
于是
\[
g_{sa}=G_{ab}A_s^b
\]
给出
\[
G_{ab}F^b_{ts}
=G_{ab}\partial_tA_s^b
=\partial_tg_{sa}
=-2II_{sa}
=-2m_a.
\]

若定向取
\[
\operatorname{vol}_\gamma(\nu,\partial_s)=+1,\qquad
F^a=f^a\operatorname{vol}_\gamma,
\]
且定义守恒 charge
\[
\mathfrak q_a^{\rm tw}=\rho G_{ab}f^b,
\]
则中心处
\[
\boxed{\mathfrak q_a^{\rm tw}=-2\rho m_a=-2m_a}.
\]
故选择
\[
m=-\frac12\mathfrak q
\]
正好重建给定 charge。反转 \(\nu\)、基底定向或采用相反的 Weingarten 号约定，都会同时改变这个等式的符号，但不会改变能量。

更一般地，
\[
m=-\frac{\mathfrak q}{2\rho},
\qquad
Q_{\rm phys}
=\frac{1}{2\rho^2}\mathfrak q^TG^{-1}\mathfrak q
=2m^TG^{-1}m.
\]
中心处 \(\rho=1,G=M\)，故
\[
Q_{\rm phys}
=\frac12\mathfrak q^TM^{-1}\mathfrak q
=Q.
\]

垂直块同时给出
\[
M^{-1}M_\nu=-2B,\qquad
e_\nu=\frac12\operatorname{tr}\bigl[(M^{-1}M_\nu)^2\bigr]
=2P.
\]
因此中心几何的精确分解是
\[
|II|^2=\frac12e_\nu+Q=P+Q=S.
\]

---

## 6. 完整严格稳定性

Koiso germ 中
\[
\operatorname{Ric}_g(\nu,\nu)=-3,\qquad |II|^2=S.
\]
极小超曲面的 Jacobi 二次型因此为
\[
\mathcal J[\phi]
=\int_{T^3}
\left(
|\nabla\phi|_{q_\Sigma}^2+
(3-S)\phi^2
\right)d\mu_{q_\Sigma}.
\]
由于 \(0<S<3\)，
\[
\mathcal J[\phi]\ge(3-S)\|\phi\|_{L^2}^2
\]
对任意依赖全部三个坐标的光滑函数成立。这直接给出完整严格稳定性，无需只考察 \(T^2\)-不变变化。

因 \(\det M=1\)，体积元为常数倍的 \(ds\,dx\)。对 torus Fourier 展开
\[
\phi(s,x)=\sum_{k}y_k(s)e^{ik\cdot x}
\]
有
\[
\mathcal J[\phi]
=\sum_k\int_{S^1}
\left(
|y'_k|^2+
\bigl[k^TM^{-1}(s)k+3-S\bigr]|y_k|^2
\right)ds.
\]
所以：

- 几何 Jacobi 零阶势对所有模都是精确的 \(3-S\)；
- 非零 torus 模的一维有效势是
  \[
  3-S+k^TM^{-1}k;
  \]
- \(k=0\) 的常函数达到 Rayleigh 商 \(3-S\)。

因此完整 Jacobi 算子的最低特征值不是仅有下界，而是
\[
\boxed{\lambda_1=3-S}.
\]

---

## 7. 绕行双曲圆的解析性与周期性

在上半平面坐标
\[
y=e^\alpha,\qquad x=\beta,\qquad
h_{\mathbb H^2}=d\alpha^2+e^{-2\alpha}d\beta^2
=\frac{dx^2+dy^2}{y^2},
\]
令
\[
v=\sqrt{12+2S}.
\]
对脚本采用的 \(L=2\pi\)，取整数绕行数 \(\ell\ge1\)，
\[
R=\operatorname{arsinh}\frac v\ell,\qquad
\theta=\ell s.
\]
定义
\[
D=\cosh R-\sinh R\sin\theta,
\]
\[
y=D^{-1},\qquad
\beta=\frac{\sinh R\cos\theta}{D}.
\]
因为
\[
D\ge\cosh R-\sinh R=e^{-R}>0,
\]
这些函数在整个圆周上实解析。它们描述半径 \(R\) 的双曲圆，并满足
\[
|U_s|^2=\ell^2\sinh^2R=v^2=12+2S.
\]
整数 \(\ell\) 保证
\[
U(s+2\pi)=U(s).
\]
即使 \(\ell>1\) 导致多重绕行，\(U\) 仍是处处浸入的全局解析周期映射。

全局单位法向可取
\[
N^\alpha=-e^{-\alpha}T^\beta,\qquad
N^\beta=e^\alpha T^\alpha,
\qquad T=\frac{U_s}{|U_s|}.
\]
它与 \(U\) 同周期且解析。

对任意固定非零方向 \(\widehat{\mathfrak q}\)，写
\[
\mathfrak q=a\widehat{\mathfrak q}.
\]
由于
\[
\widehat{\mathfrak q}^{\,T}M^{-1}(s)\widehat{\mathfrak q}>0
\]
且在圆周上有有限最大值，可选足够小的 \(a>0\) 使
\[
0<Q(s)<S.
\]
于是
\[
P=S-Q>0
\]
是全局解析周期函数，正平方根 \(\sqrt P\) 也全局解析。严格的 \(Q<S\) 在这里很重要；若 \(P\) 在某点为零，\(\sqrt P\) 未必保持解析。

---

## 8. Koiso 定理的适用性

现有数据满足：

\[
q_\Sigma\ \text{解析且正定},\qquad
W\ \text{解析且自伴},
\]
\[
\operatorname{Scal}_{q_\Sigma}
+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2=-6,
\]
\[
d(\operatorname{tr}W)+\delta W=0.
\]

因此 supplied 文件
`step92_ttcs02_verifier1_integration.md` 中所述 Koiso 解析 Cauchy 定理给出某个
\(\varepsilon>0\) 以及
\[
g=dt^2+q_t
\]
定义在
\[
(-\varepsilon,\varepsilon)\times T^3
\]
上，使
\[
\operatorname{Ric}_g=-3g,\qquad
q_0=q_\Sigma,\qquad W_0=W.
\]

初值在 \(T^2\) 平移下不变；Gaussian gauge 中的解析唯一性使该对称性延续到 germ。由 exact mixed Einstein 方程，重建的 charge covector 在连通的二维基底上守恒。

---

## 9. 数值文件与精确推导的一致性

`step94_charged_koiso_separator.json` 记录：

- 速度平方残差：\(1.24\times10^{-14}\)；
- \(|II|^2-S\)：\(8.88\times10^{-16}\)；
- 自伴性：\(3.33\times10^{-16}\)；
- \(s\)-momentum：\(6.66\times10^{-16}\)；
- 垂直联络抵消：\(0\)；
- Hamiltonian：\(6.22\times10^{-15}\)；
- charge 重建：\(0\)。

这些数值与上述解析恒等式逐项吻合；它们用于归一化验证，而解析证明来自矩阵、曲率和散度计算。

---

## 10. 该构造实际建立的数学内容

它给出了真实的局部例子，兼具：

1. \(\operatorname{Ric}=-3g\)；
2. 自由 \(T^2\) 对称性；
3. 非零守恒 twist charge；
4. 极小中心 \(T^3\)；
5. 完整严格稳定性；
6. 完整 Hamilton–momentum Cauchy 数据。

因此，“Einstein Cauchy 约束、极小性和完整严格稳定性联合起来必然迫使 separator 上 twist 为零”这一局部推理不成立。带电 separator 与所有这些结构完全相容。

它尚未提供：

- 完备的两端 Einstein 或近 Einstein connector；
- 与指定两端几何的匹配；
- 参数变化时统一的 Koiso collar 宽度；
- 中心 \(T^3\) 在其同调类中的全局面积最小性；
- 从中心向两侧延拓时对 \(M,\rho,A\) 的统一控制；
- 闭流形上的 Ricci 夹逼反例或 Yau 第26题的证明。

还有一个明确的全局现象：exact Einstein 方程使 charge 守恒，所以非零 charge germ 不能在保持 exact Einstein 的同时接到某个 exact OT 开集，因为后者给出 charge \(=0\)。它仍可能接到物理 twist 能量趋零但守恒坐标 charge 非零的膨胀端；若要把 charge 真正消去，则混合 Ricci 块必须非零，并需同时控制全部 Ricci 块。两端延拓、端部匹配、完备性和统一 Ricci 夹逼正是尚缺的全局数学内容。