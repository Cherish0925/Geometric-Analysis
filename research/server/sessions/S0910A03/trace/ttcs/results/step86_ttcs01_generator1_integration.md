# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 86,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step86_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step86_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the strongest rigorous local comparison/regularity estimate available from the corrected forced weighted Bochner system for a reflected free-T2 orthogonally transitive connector. Work from the exact formulas in the supplied notes, but correct Step 85 as follows: use finite-dimensional Ric_f^4 = Ric_B-Hess sigma-(1/2)d sigma^2 >= -(3+delta)gamma, normalized local measure estimates only, and retain BOTH terms when testing u=(e-k)_+: integral eta^2 u div_sigma V = - integral eta^2<V,grad u> -2 integral eta u<V,grad eta>. Assume pointwise |E|<=delta and derive the precise relation between orbit forcing F=tau_sigma and the traceless orbit Ricci defect, including conformal/normalization factors. Ask whether quadratic reaction plus positive Hessian can yield an interior ceiling independent of prior local energy/volume, perhaps via nonlinear absorption, a resolvent/Green estimate, or a Bernstein transform. Explicitly identify any mathematically realizable concentration or boundary-flux escape if no such ceiling follows. Keep actual buffered-domain and exit-data hypotheses explicit. The desired output is a derivation or countermechanism, not general suggestions.

## Integrated Scientific Memo

## 修正后的强迫 Bochner 系统：可严格得到的最强局部结论

设
\[
g=\gamma_B+G_{ab}d\xi^ad\xi^b,\qquad
\gamma_B=e^{2\lambda}(dr^2+dz^2),\qquad
G=e^\sigma M,\quad \det M=1,
\]
并令
\[
E=\Ric_g+3g,\qquad
d\mu=e^\sigma\,dv_{\gamma_B},\qquad
L=\Delta_{\gamma_B}+\langle\nabla\sigma,\nabla\cdot\rangle .
\]
轨道形状映射记为
\[
U:(B,\gamma_B)\to \mathbb H^2,\qquad e=|dU|^2_{\gamma_B}.
\]

以下假设在所讨论的缓冲域 \(\Omega\) 上成立：

1. \(T^2\)-作用自由且正交可传递；
2. \(U,\sigma,\lambda,E\) 光滑；
3. \(|E|_{\mathrm{op}}\le \delta\)；
4. 中心反射给出光滑加倍；若使用内球估计，则
   \(B_{\gamma_B}(p,2r)\Subset\Omega^{\mathrm{dbl}}\)；
5. 若球接触出口，则另需出口迹控制或跨出口的受控延拓，详见下文。

---

### 1. 轨道 forcing 与无迹轨道 Ricci 缺陷的精确关系

令
\[
P=M^{-1}dM,\qquad
\widehat E=G^{-1}E|_{T^2},\qquad
\widehat E_0=\widehat E-\frac12\tr(\widehat E)I .
\]
轨道 Ricci 方程的无迹部分为
\[
\left(G^{-1}\Ric_g|_{T^2}\right)_0
=-\frac12e^{-\sigma}\div_{\gamma_B}(e^\sigma P).
\]
由于 \(3I\) 的无迹部分为零，
\[
\boxed{
e^{-\sigma}\div_{\gamma_B}(e^\sigma P)=-2\widehat E_0.
}
\tag{1}
\]

采用对称空间归一化
\[
|\iota_M(X)|_{\mathbb H^2}^2=\frac12\tr(X^2),
\]
加权张力 \(F=\tau_\sigma(U)\) 满足
\[
\boxed{\iota_M(F)=-2\widehat E_0},
\qquad
\boxed{|F|_{\mathbb H^2}^2=2\tr(\widehat E_0^2)}.
\tag{2}
\]
因此若 \(|E|_{\mathrm{op}}\le\delta\)，则 \(\widehat E_0\) 的特征值为
\(\pm a\)、\(|a|\le\delta\)，从而
\[
\boxed{|F|\le2\delta.}
\tag{3}
\]
若 \(|E|\le\delta\) 是四维 Hilbert–Schmidt 范数约束，则可改进为
\(|F|\le\sqrt2\,\delta\)。

在共形坐标中，(1) 等价于
\[
\boxed{
\partial_r(e^\sigma M^{-1}M_r)
+\partial_z(e^\sigma M^{-1}M_z)
=-2e^{2\lambda+\sigma}\widehat E_0.
}
\tag{4}
\]
所以 \(e^{2\lambda+\sigma}\) 是平直坐标散度方程中的密度因子；它不出现在不变量范数关系 (2)–(3) 中。由此也修正了“长扩张 collar 会放大几何张力”的疑虑：被放大的是坐标源，而不是 \(F\) 的 \(\mathbb H^2\)-范数。

---

### 2. 有限维漂移曲率

取 \(f=-\sigma\)，则
\[
L=\Delta-\langle\nabla f,\nabla\cdot\rangle,\qquad
d\mu=e^{-f}dv_{\gamma_B}.
\]
基底方程为
\[
\Ric_B-\Hess\sigma
=-3\gamma_B+\frac12d\sigma^2+\frac12U^*h_{\mathbb H^2}+E_B .
\]
基底维数为 \(2\)，有效维数取 \(N=4\)，故
\[
\begin{aligned}
\Ric_f^4
&=\Ric_B+\Hess f-\frac1{4-2}df^2\\
&=\Ric_B-\Hess\sigma-\frac12d\sigma^2\\
&=-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B.
\end{aligned}
\]
于是
\[
\boxed{\Ric_f^4\ge-(3+\delta)\gamma_B.}
\tag{5}
\]
这是正确的局部几何输入；不得以 \(\Ric_f^\infty\) 或未归一化体积下界代替它。

---

### 3. 强迫 Bochner 不等式

令
\[
A_{ij}=\langle dU(e_i),dU(e_j)\rangle,\qquad
V(X)=\langle dU(X),F\rangle .
\]
由
\[
\langle dU,D\tau_\sigma\rangle
=\div_\sigma V-|F|^2
\]
及 \(K_{\mathbb H^2}=-1\)，有
\[
\begin{aligned}
\frac12Le={}&|DdU|^2+\div_\sigma V-|F|^2
+\frac12|dU(\nabla\sigma)|^2\\
&+\frac12\tr(A^2)+2\det A-3e+E_B:A .
\end{aligned}
\tag{6}
\]
注意：\(-|F|^2\) **不能被称为消失**；它只是在把
\(\langle dU,DF\rangle\) 改写成散度形式时出现。积分估计必须保留它。

由于
\[
\frac12\tr(A^2)+2\det A
=\frac12e^2+\det A\ge\frac12e^2,
\qquad E_B:A\ge-\delta e,
\]
得到
\[
\boxed{
\frac12Le\ge
|DdU|^2+\div_\sigma V-|F|^2
+\frac12e^2-(3+\delta)e.
}
\tag{7}
\]
记
\[
\kappa=6+2\delta,\qquad b=\|F\|_\infty\le2\delta.
\]

---

### 4. 正确的超能级检验

取
\[
u=(e-k)_+,\qquad k\ge\kappa,
\]
以及紧支撑于缓冲域的 \(0\le\eta\le1\)。在 \(A_k=\{e>k\}\) 上
\(\nabla e=\nabla u\)，且
\[
|V|\le b\sqrt e.
\]
关键散度项必须完整写成
\[
\boxed{
\int\eta^2u\,\div_\sigma V\,d\mu
=-\int\eta^2\langle V,\nabla u\rangle\,d\mu
-2\int\eta u\langle V,\nabla\eta\rangle\,d\mu .
}
\tag{8}
\]
第一项不能省略；它正是产生 \(b^2e\) 误差的超能级界面通量。

将 (7) 乘以 \(\eta^2u\)，分部积分并作 Young 估计，可取一组非最优但明确的常数得到
\[
\boxed{
\begin{aligned}
&\frac14\int\eta^2|\nabla u|^2\,d\mu
+\int\eta^2u|DdU|^2\,d\mu\\
&\quad+\frac12\int\eta^2
\bigl[u^3+(2k-\kappa)u^2+k(k-\kappa)u\bigr]\,d\mu\\
&\le
3\int u^2|\nabla\eta|^2\,d\mu
+4b^2\int_{A_k}\eta^2e\,d\mu .
\end{aligned}}
\tag{9}
\]
这里使用了精确展开
\[
u\,\frac12e(e-\kappa)
=\frac12\left[u^3+(2k-\kappa)u^2+k(k-\kappa)u\right].
\tag{10}
\]

若 \(\eta=\chi^{m/2}\)、\(m\ge6\)、\(|\nabla\chi|\le D\)，由
\[
D^2\chi^{m-2}u^2\le
\varepsilon\chi^m u^3+C_{\varepsilon,m}D^6\,1_{A_k},
\]
和
\[
b^2u\le\varepsilon u^3+C_\varepsilon b^3,
\]
可推出
\[
\boxed{
\begin{aligned}
&\int\chi^m|\nabla u|^2
+\int\chi^m u|DdU|^2
+\int\chi^m(u^3+\kappa u^2)\\
&\qquad\le
C_m(D^6+b^3+b^2k)\,
\mu(A_k\cap\supp\chi).
\end{aligned}}
\tag{11}
\]
这已经不依赖任何先验 \(\int e\) 控制。

---

### 5. 归一化局部 ceiling

由 (5) 的 \(CD(-(3+\delta),4)\) 条件，在
\[
(3+\delta)s^2\le1
\]
的球上有有效维数 \(4\) 的局部 doubling 和归一化 Sobolev 不等式，例如
\[
\frac{\mu(B_{2s})}{\mu(B_s)}\le C_4,
\]
\[
\boxed{
\left(\fint_{B_s}|\phi|^4\,d\mu\right)^{1/2}
\le C_4s^2\fint_{B_s}|\nabla\phi|^2\,d\mu
+C_4\fint_{B_s}\phi^2\,d\mu .
}
\tag{12}
\]
只使用归一化平均 \(\fint\)，因此不需要 \(\mu(B_s)\) 的绝对正下界；轨道塌缩本身不破坏该估计。

若
\[
B_{\gamma_B}(p,2r)\Subset\Omega^{\mathrm{dbl}},
\]
取
\[
s=\min\left\{\frac r8,\ \kappa^{-1/2},\ b^{-1/2}\right\},
\]
其中 \(b=0\) 时最后一项视为 \(+\infty\)。将 (11) 与 (12) 用于 De Giorgi 超能级迭代，可得
\[
\boxed{\sup_{B_s(p)}e\le\kappa+\Lambda s^{-2}}
\tag{13}
\]
其中 \(\Lambda\) 仅依赖有效维数 \(4\) 的局部 doubling–Sobolev 常数。覆盖后得到
\[
\boxed{
\sup_{B_r(p)}e
\le C\bigl(\kappa+b+r^{-2}\bigr)
\le C\bigl(1+\delta+r^{-2}\bigr).
}
\tag{14}
\]

因此，二次反应和正 Hessian 项确实给出一个不依赖下列量的内域 ceiling：

- 先验局部轨道能量；
- 加权球体积的绝对大小；
- connector 总长度；
- \(T^2\) 或中心圆的塌缩尺度。

同时 (11) 给出高能级区域上的 \(u|DdU|^2\) 控制。

---

### 6. 该论证不能推出 \(6+C\delta\)

现有输入严格支持的是 (14)，而不是
\[
\sup e\le6+C\delta.
\]
把 Keller–Osserman、Green/resolvent 或 Bernstein 论证直接宣称为
\(6+O(\delta)+Cr^{-2}\)，并进而排除小缺陷 connector，是尚未证明的。原因有三：

1. 散度 forcing 的超能级界面项
   \[
   -\int\eta^2\langle V,\nabla u\rangle
   \]
   只由 \(|F|\) 控制，并产生 \(b^2e\) 误差；它并不会自动成为接近阈值 \(6\) 的小扰动。

2. 局部无边界数据的吸收估计必然留下 \(r^{-2}\) 尺度项，其系数未被证明小于中心能隙 \(6\)。

3. 点态 Bernstein 变换仍会遇到 \(DF\)：仅有 \(C^0\) 小 forcing 时，无法在最大点控制
   \(\langle dU,DF\rangle\)。

一个接近精确阈值的 resolvent 方法至少需要额外证明实际加倍 connector 上的定量核估计，例如
\[
\sup_x\int |\nabla_yG_\kappa(x,y)|\,d\mu_y
\le C\kappa^{-1/2},
\tag{15}
\]
并控制截断超能级界面通量。有限维曲率维数条件本身没有给出这一结论。

---

### 7. 可实现的浓缩逃逸

仅控制 \(|F|\le\delta\) 而不控制 \(DF\)，可以支撑任意大的窄能量层。令 \(U\) 沿 \(\mathbb H^2\) 中一条测地线：
\[
U(x)=\Gamma(\psi(x)).
\]
在一点取 jet
\[
\psi'(0)=A,\qquad
\psi''(0)=0,\qquad
\psi'''(0)=-\frac12A^3.
\]
则
\[
e(0)=A^2,\qquad
\nabla e(0)=0,\qquad
F(0)=0,\qquad
|DdU|(0)=0,
\]
但
\[
\langle dU,DF\rangle(0)
=A\psi'''(0)=-\frac12A^4=-\frac12e(0)^2,
\]
恰可抵消二次反应。在宽度
\[
|x|\lesssim\delta A^{-3}
\]
的条带中仍可保持 \(|F|\lesssim\delta\)。这说明不存在仅依赖 \(\delta\) 的点态 Bernstein ceiling；高能量可以通过越来越薄的 \(C^0\)-小、\(C^1\)-大 forcing 层逃逸。

这只是局部 jet/层机制，并未证明其可嵌入满足全部耦合 OT 方程及约束的 connector；但现有假设也没有排除它。

---

### 8. 出口边界通量与必需假设

若估计球完全位于加倍后的缓冲域内部，则不存在边界通量。光滑反射使中心圆成为普通内点集。

若球接触出口，需要以下二者之一：

1. 几何、方程及 \(|E|,|F|,\Ric_f^4\) 控制可光滑延拓穿过出口；或
2. 出口能量迹满足 \(e\le E_{\rm out}\)，且出口 collar 具有相应的相对 doubling–Sobolev 不等式。

第二种情况下取
\[
k\ge\max\{\kappa,E_{\rm out}\},
\]
则 \(u\) 在出口迹为零，并可得半 collar 估计
\[
\boxed{
\sup_{\text{half collar}}e
\le C\left(\max\{\kappa,E_{\rm out}\}+b+r^{-2}\right).
}
\tag{16}
\]

若既无出口迹，也无延拓，分部积分产生
\[
\frac12\int_{\Sigma_{\rm out}}\eta^2u\,\partial_\nu e\,d\mu_\Sigma,
\qquad
\int_{\Sigma_{\rm out}}\eta^2u\,\langle V,\nu\rangle\,d\mu_\Sigma .
\tag{17}
\]
即使 \(|F|\le b\)，后者也只有
\[
|u\langle V,\nu\rangle|\le b\,u\sqrt e,
\]
故大出口能量可以携带无统一上界的通量。

相应的标量边界层
\[
q_\varepsilon(d)=\frac6{(d+\varepsilon)^2},
\qquad
q_\varepsilon''=q_\varepsilon^2
\ge q_\varepsilon(q_\varepsilon-\kappa),
\tag{18}
\]
其端面值 \(6/\varepsilon^2\to\infty\)，而距端面 \(r\) 处仍为
\(O(r^{-2})\)。因此 (14)、(16) 中的 \(r^{-2}\) 是真实的边界层尺度，不只是证明伪影。

---

### 9. 与反射中心能量的关系

对全测地反射中心，近 Einstein 情形满足
\[
R(q_0)=-6+\tr E-2E_{nn}.
\]
由 Step 82 的切片恒等式，
\[
K(0)=12-2\langle\tr E-2E_{nn}\rangle,
\]
且
\[
\langle e(0,\cdot)\rangle_\mu
=K(0)+\langle h^2\rangle_\mu,\qquad
h=(\log\rho)_s.
\]
在 \(|E|_{\mathrm{op}}\le\delta\) 下，
\[
\boxed{
\langle e(0,\cdot)\rangle_\mu\ge12-8\delta.
}
\tag{19}
\]
然而 (14) 的常数并不足以与 (19) 矛盾。因此当前严格结论是：

\[
\boxed{
\sup_{B_r}e\le C(1+\delta+r^{-2})
}
\]
这一无先验能量、无非塌缩假设、无长度依赖的局部正则性估计成立；但由给定假设尚不能推出 \(6+C\delta\) 的近精确 ceiling，也尚不能据此排除全部小缺陷强迫 connector。剩余的精确数学对象是：对散度 forcing 的超能级界面项建立接近阈值的 resolvent/Green 控制，或从完整耦合 OT 方程推出足以排除上述窄层的额外 \(DF\) 正则性。