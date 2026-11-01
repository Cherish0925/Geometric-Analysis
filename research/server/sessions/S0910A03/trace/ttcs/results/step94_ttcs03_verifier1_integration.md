# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 94,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs03_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs03_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the proposed charged Koiso separator construction in full detail. The hypersurface metric is qSigma=ds^2+M(U(s)) on T^3, det M=1. Choose fixed charge covector q, mixed Weingarten covector m=-q/2 (orientation convention), a hyperbolic target circle U of constant speed squared 12+2S with 0<S<3, physical separator charge Q(s)=1/2 q^T M^-1q scaled so Q<S, P=S-Q, and vertical tracefree Weingarten B=sqrt(P/2) M^-1 dM(N), N target-normal to U_s. Check: (i) the full block Weingarten endomorphism and its self-adjointness; (ii) tr W=0 and tr W^2=P+Q=S, including the factor 2 in the mixed block; (iii) scalar curvature and Hamiltonian constraint for lambda=-3; (iv) every momentum component, especially whether constant covector m really makes vertical momentum vanish after all connection terms and whether s-momentum remains tr(A B)=0 despite mixed W; (v) the Gaussian-gauge relation between m and the twist charge q, including rho factors and orientation; (vi) full—not merely invariant—strict stability and whether the potential is exactly 3-S for all torus Fourier modes; (vii) analyticity/global periodicity of the wound target circle and applicability of Koiso. Identify any hidden obstruction or needed modification. State exactly what a valid construction would establish and what global two-ended work remains.

## Integrated Scientific Memo

# 核验结论

该带电 Koiso separator 构造在给定归一化及定向约定下成立。若
\[
0<S<3,\qquad 
Q(s):=\frac12\mathfrak q^TM(s)^{-1}\mathfrak q<S,
\qquad P=S-Q,
\]
并取
\[
m=-\frac12\mathfrak q,\qquad
B=\sqrt{\frac P2}\,M^{-1}dM(N),
\]
则 \((q_\Sigma,W)\) 是 \(T^3\) 上全局解析、完整满足 \(\operatorname{Ric}=-3g\) Cauchy 约束的数据。Koiso 解析 Cauchy 定理给出局部解析 Einstein germ。中心 \(T^3\) 极小并对任意变化严格稳定，且具有非零守恒 twist charge。

没有发现隐藏的代数、联络、解析或周期性障碍。需要精确表述的是：

* 垂直 momentum 除两个互消项外还有 \((\operatorname{tr}A)m_a\)，它因 \(\det M=1\) 消失；
* Jacobi 的共同几何零阶势是 \(3-S\)，但非零 torus Fourier 模的有效一维势还含 \(k^TM^{-1}k\)；
* \(m=-\mathfrak q/2\) 只适用于中心处 \(\rho=1\) 及所选定向；一般关系是 \(m=-\mathfrak q/(2\rho)\)；
* Koiso 只产生局部 germ，不产生完整两端 connector。

---

## 1. 完整 Weingarten 块与自伴性

为避免符号冲突，以 \(\mathfrak q\) 表示固定 charge covector。相对于
\[
q_\Sigma=ds^2+M_{ab}(s)\,dx^adx^b
\]
和基 \((\partial_s,\partial_{x^1},\partial_{x^2})\)，应取
\[
W^i{}_j=
\begin{pmatrix}
0&m_b\\
m^a&B^a{}_b
\end{pmatrix},
\qquad m^a=M^{ab}m_b.
\]
即
\[
W(\partial_s)=m^a\partial_{x^a},\qquad
W(\partial_{x^a})=m_a\partial_s+B^b{}_a\partial_{x^b}.
\]

令
\[
C_X=M^{-1}dM(X),\qquad
\langle X,Y\rangle_{\mathbb H^2}
=\frac12\operatorname{tr}(C_XC_Y).
\]
由于 \(M\) 对称，
\[
MB=\sqrt{\frac P2}\,dM(N)
\]
也是对称矩阵。降低 \(W\) 的上指标得
\[
(q_\Sigma W)_{ij}=
\begin{pmatrix}
0&m_b\\
m_a&(MB)_{ab}
\end{pmatrix},
\]
故 \(W\) 对 \(q_\Sigma\) 自伴。

---

## 2. 迹与混合块的因子 \(2\)

由 \(\det M=1\)，
\[
\operatorname{tr}C_N=N(\log\det M)=0.
\]
因此
\[
\operatorname{tr}W=\operatorname{tr}B=0.
\]
单位靶法向满足
\[
\frac12\operatorname{tr}(C_N^2)=1,
\]
所以
\[
\operatorname{tr}(B^2)
=\frac P2\operatorname{tr}(C_N^2)=P.
\]

对块矩阵平方取迹：
\[
\operatorname{tr}(W^2)
=\operatorname{tr}(B^2)+2m^TM^{-1}m.
\]
这里的 \(2\) 是必需的：\(ss\) 对角项和垂直对角块各贡献一份混合范数。由于
\[
m=-\frac12\mathfrak q,
\]
有
\[
2m^TM^{-1}m
=\frac12\mathfrak q^TM^{-1}\mathfrak q=Q.
\]
故
\[
\boxed{\operatorname{tr}W=0},\qquad
\boxed{|II|^2=\operatorname{tr}(W^2)=P+Q=S}.
\]

---

## 3. 标量曲率与 Hamiltonian 约束

置
\[
A=\frac12M^{-1}M_s.
\]
相关 Christoffel 符号为
\[
\Gamma^a{}_{sb}=\Gamma^a{}_{bs}=A^a{}_b,\qquad
\Gamma^s{}_{ab}=-(MA)_{ab}.
\]
一般标量曲率公式为
\[
R_{q_\Sigma}
=-2(\operatorname{tr}A)_s-(\operatorname{tr}A)^2-\operatorname{tr}(A^2).
\]
而
\[
\operatorname{tr}A=\frac12\partial_s\log\det M=0,
\]
故
\[
R_{q_\Sigma}=-\operatorname{tr}(A^2).
\]
靶速度归一化为
\[
e_s=|U_s|^2
=\frac12\operatorname{tr}\!\left[(M^{-1}M_s)^2\right]
=2\operatorname{tr}(A^2),
\]
所以
\[
\boxed{R_{q_\Sigma}=-\frac12e_s}.
\]
取 \(e_s=12+2S\) 得
\[
\boxed{R_{q_\Sigma}=-6-S}.
\]

三维超曲面位于四维 \(\operatorname{Ric}=-3g\) 中时，Hamiltonian 约束为
\[
R_{q_\Sigma}+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2=-6.
\]
代入即为
\[
(-6-S)+S=-6.
\]

---

## 4. 全部 momentum 分量

令
\[
D_j:=\nabla_iW^i{}_j.
\]
因 \(\operatorname{tr}W=0\)，momentum 约束等价于 \(D=0\)，不受散度整体符号约定影响。

### \(s\)-分量

直接计算得
\[
D_s=-\operatorname{tr}(AB).
\]
混合块 \(m\) 不贡献这一分量。又
\[
A=\frac12C_{U_s},\qquad
B=\sqrt{\frac P2}C_N,
\]
所以
\[
\operatorname{tr}(AB)
=\sqrt{\frac P2}\,
\frac12\operatorname{tr}(C_{U_s}C_N)
=\sqrt{\frac P2}\,\langle U_s,N\rangle_{\mathbb H^2}=0.
\]
因此
\[
\boxed{D_s=0}.
\]

### 垂直分量

完整公式是
\[
D_a
=m'_a+(\operatorname{tr}A)m_a
-A^b{}_am_b+(MA)_{ba}m^b.
\]
最后两项满足
\[
(MA)_{ba}m^b=A^c{}_am_c,
\]
故精确相消。又
\[
\operatorname{tr}A=0,\qquad m'_a=0,
\]
于是
\[
\boxed{D_a=0}.
\]

这里“固定 \(m\)”必须理解为 \(m_a\) 在全局 torus 共标架 \(dx^a\) 中为常数。若 \(m=m(s)\)，垂直 momentum 会留下 \(m'_a\)。

脚本中的 `conn1+conn2` 是预先编码的代数抵消，而不是独立计算完整散度；不过上述完整 Christoffel 推导证明该抵消确实正确，并补上了脚本未显示的 \((\operatorname{tr}A)m_a\) 项。

---

## 5. Gaussian gauge、\(\rho\) 因子与定向

采用
\[
g=dt^2+q_t,\qquad \nu=\partial_t,\qquad
q_t(WX,Y)=-\frac12\dot q_t(X,Y).
\]
中心处选
\[
A_s=A_t=0,\qquad G=M,\qquad
\rho=\sqrt{\det G}=1.
\]
由
\[
g_{sa}=G_{ab}A_s^b
\]
以及
\[
\dot g_{sa}=-2W_{sa}=-2m_a
\]
可得
\[
G_{ab}F^b_{ts}=-2m_a.
\]

若基底定向为
\[
\operatorname{vol}_\gamma(\nu,\partial_s)=+1,
\qquad F^a=f^a\operatorname{vol}_\gamma,
\]
且 charge 定义为
\[
\mathfrak q_a=\rho G_{ab}f^b,
\]
则
\[
\boxed{\mathfrak q_a=-2\rho m_a}.
\]
中心处 \(\rho=1\)，故
\[
\boxed{m=-\frac12\mathfrak q}.
\]
反转 \(\nu\)、基底定向或 Weingarten 符号约定会反转此符号，但不改变能量。

一般物理 twist 能量为
\[
Q_{\rm phys}
=\frac{1}{2\rho^2}\mathfrak q^TG^{-1}\mathfrak q
=2m^TG^{-1}m.
\]
在中心 \(G=M,\rho=1\) 时恰为题设的
\[
Q=\frac12\mathfrak q^TM^{-1}\mathfrak q.
\]

垂直块还给出
\[
M^{-1}M_\nu=-2B,\qquad
e_\nu=\frac12\operatorname{tr}\!\left[(M^{-1}M_\nu)^2\right]=2P,
\]
所以
\[
|II|^2=\frac12e_\nu+Q=P+Q=S.
\]

---

## 6. 完整严格稳定性

中心极小，因为
\[
H=\operatorname{tr}W=0.
\]
Jacobi 二次型为
\[
\mathcal J[\phi]
=\int_{T^3}\left(
|\nabla\phi|^2-
[\operatorname{Ric}(\nu,\nu)+|II|^2]\phi^2
\right)d\mu.
\]
这里
\[
\operatorname{Ric}(\nu,\nu)=-3,\qquad |II|^2=S,
\]
故
\[
\boxed{
\mathcal J[\phi]
=\int_{T^3}\bigl(|\nabla\phi|^2+(3-S)\phi^2\bigr)d\mu }.
\]
由于 \(0<S<3\)，这对所有 \(\phi(s,x^1,x^2)\) 严格正定，而非仅对不变函数成立。

更精确地，作 torus Fourier 展开
\[
\phi=\sum_{k\in\mathbb Z^2}y_k(s)e^{ik\cdot x},
\]
因为 \(\det M=1\)，
\[
\mathcal J[\phi]
=\sum_k\int
\left(
|y_k'|^2+
[3-S+k^TM^{-1}(s)k]|y_k|^2
\right)ds.
\]
因此：

* 所有模共有的几何零阶势是 \(3-S\)；
* 非零模的有效势不是“恰好 \(3-S\)”，而是
  \[
  3-S+k^TM^{-1}k;
  \]
* \(k=0\) 的常函数达到 Rayleigh 商 \(3-S\)。

所以完整 Jacobi 算子的最低特征值恰为
\[
\boxed{\lambda_1=3-S}.
\]

---

## 7. 双曲圆的周期性与解析性

对 \(L=2\pi\)，取整数 winding \(\ell\ge1\)，令
\[
v=\sqrt{12+2S},\qquad
R=\operatorname{arsinh}\frac v\ell,\qquad
\theta=\ell s.
\]
上半平面坐标中的圆可写为
\[
D=\cosh R-\sinh R\sin\theta,
\]
\[
e^\alpha=D^{-1},\qquad
\beta=\frac{\sinh R\cos\theta}{D}.
\]
由于
\[
D\ge \cosh R-\sinh R=e^{-R}>0,
\]
故 \(U=(\alpha,\beta)\) 在整个圆周上实解析。整数 \(\ell\) 保证周期性，而
\[
|U_s|^2=\ell^2\sinh^2R=12+2S.
\]
多重绕行不妨碍其作为解析浸入。

利用 \(\mathbb H^2\) 的定向，
\[
N=J\frac{U_s}{|U_s|}
\]
给出全局周期解析单位法向，不存在 normal monodromy。

固定任意非零 charge 方向后，将其整体缩小即可使
\[
0<Q(s)<S.
\]
于是 \(P=S-Q\) 是严格正的解析周期函数，\(\sqrt P\) 也全局解析。这一严格不等式不可随意削弱为 \(P\ge0\)，因为零点处 \(\sqrt P\) 未必解析。

---

## 8. Koiso 的确切结论

数据 \(q_\Sigma\) 与 \(W\) 均解析，且满足
\[
R_{q_\Sigma}+\operatorname{tr}(W^2)-(\operatorname{tr}W)^2=-6,
\qquad
d(\operatorname{tr}W)+\delta W=0.
\]
因此 Koiso 解析 Cauchy 定理给出某个 \(\varepsilon>0\) 及
\[
g=dt^2+q_t
\quad\text{on}\quad
(-\varepsilon,\varepsilon)\times T^3
\]
使
\[
\operatorname{Ric}_g=-3g,\qquad q_0=q_\Sigma,\qquad W_0=W.
\]
解析唯一性使初值的 \(T^2\)-平移对称性延续到 germ；混合 Einstein 方程使相应 twist charge 在连通基底上守恒。由于 \(m\ne0\)，该 germ 在中心具有非零 twist curvature，故不是 OT germ。

---

## 9. 此构造建立及未建立的内容

它严格建立了一个同时具有以下性质的局部例子：

1. 精确 \(\operatorname{Ric}=-3g\)；
2. 自由 \(T^2\) 对称；
3. 非零守恒 twist charge；
4. 极小中心 \(T^3\)；
5. 完整严格稳定性；
6. 完整 Hamilton–momentum Cauchy 约束。

因此，separator 层面的极小性、完整稳定性和完整 Einstein 约束并不迫使 twist 消失。非零 charge 与这些局部条件完全相容。

它没有建立：

* 完备或两端 Einstein/近 Einstein connector；
* 与指定 OT 或柱状端的匹配；
* 参数族上一致的 Koiso collar 宽度；
* 中心 \(T^3\) 在其同调类中的全局面积最小性；
* 闭流形上的 Ricci 夹逼反例；
* Yau 第26题的证明或证伪。

此外，精确 Einstein 方程令 charge 守恒，因此非零-charge germ 不可能精确接到一个 exact OT 开集：后者的 charge 为零。它可以接近“物理 twist 能量趋零但坐标 charge 非零”的膨胀端；若要把 charge 真正消去，就必须允许混合 Ricci defect，并同时满足其余水平匹配方程。

仍未解决的精确全局对象是：构造一个具有统一 collar 控制的两变量延拓/拼接，使两侧满足所需端部条件、完备性及全部 Ricci 夹逼；或者证明两端拓扑和完整 reduced Einstein–Codazzi–Bianchi 系统排除这种延拓。该局部 Koiso 构造本身不决定二者。