# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/trace/ttcs/results/step85_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Develop the strongest rigorous local comparison/regularity estimate available from the corrected forced weighted Bochner system for a reflected free-T2 orthogonally transitive connector. Work from the exact formulas in the supplied notes, but correct Step 85 as follows: use finite-dimensional Ric_f^4 = Ric_B-Hess sigma-(1/2)d sigma^2 >= -(3+delta)gamma, normalized local measure estimates only, and retain BOTH terms when testing u=(e-k)_+: integral eta^2 u div_sigma V = - integral eta^2<V,grad u> -2 integral eta u<V,grad eta>. Assume pointwise |E|<=delta and derive the precise relation between orbit forcing F=tau_sigma and the traceless orbit Ricci defect, including conformal/normalization factors. Ask whether quadratic reaction plus positive Hessian can yield an interior ceiling independent of prior local energy/volume, perhaps via nonlinear absorption, a resolvent/Green estimate, or a Bernstein transform. Explicitly identify any mathematically realizable concentration or boundary-flux escape if no such ceiling follows. Keep actual buffered-domain and exit-data hypotheses explicit. The desired output is a derivation or countermechanism, not general suggestions.

## Output

## 1. 缺陷与 orbit forcing 的精确换算

令
\[
f=-\sigma,\qquad d\mu=e^{-f}dv_{\gamma_B}
=e^\sigma dv_{\gamma_B},
\qquad
L=\Delta_{\gamma_B}-\langle\nabla f,\nabla\cdot\rangle
=\Delta_{\gamma_B}+\langle\nabla\sigma,\nabla\cdot\rangle .
\]

写
\[
G=e^\sigma M,\qquad P=M^{-1}dM.
\]
若 \(E=\operatorname{Ric}_g+3g\)，令
\[
\widehat E=G^{-1}E|_{T^2},\qquad
\widehat E_0=\widehat E-\frac12\operatorname{tr}(\widehat E)I .
\]
块对角 Ricci 公式给出
\[
\left(G^{-1}\operatorname{Ric}_g|_{T^2}\right)_0
=-\frac12e^{-\sigma}\operatorname{div}_{\gamma_B}(e^\sigma P).
\]
因为 \(3I\) 没有无迹部分，
\[
\boxed{
e^{-\sigma}\operatorname{div}_{\gamma_B}(e^\sigma P)
=-2\widehat E_0.
}
\tag{1.1}
\]

将 \(T_M\mathbb H^2\) 中的向量用矩阵 \(X=M^{-1}\dot M\) 表示，并采用
\[
|X|_{\mathbb H^2}^2=\frac12\operatorname{tr}(X^2),
\]
则
\[
\boxed{\iota_M(F)=-2\widehat E_0,\qquad F=\tau_\sigma(U).}
\tag{1.2}
\]
因此
\[
\boxed{|F|_{\mathbb H^2}^2
=2\operatorname{tr}(\widehat E_0^2).}
\tag{1.3}
\]

在共形坐标 \(\gamma_B=e^{2\lambda}(dr^2+dz^2)\) 中，(1.1) 等价于
\[
\boxed{
\partial_r(e^\sigma M^{-1}M_r)
+\partial_z(e^\sigma M^{-1}M_z)
=-2e^{2\lambda+\sigma}\widehat E_0.
}
\tag{1.4}
\]
所以 \(e^{2\lambda+\sigma}\) 只出现在平直坐标写法中；几何范数关系 (1.3) 没有额外共形因子。

若 \(\|E\|_{\mathrm{op}}\le\delta\)，则 \(\widehat E_0\) 的特征值为 \(\pm a\)，且 \(|a|\le\delta\)，从而
\[
\boxed{|F|\le2\delta.}
\tag{1.5}
\]
若 \(|E|_g\le\delta\) 指 Hilbert–Schmidt 范数，则可用更强的
\[
|F|\le\sqrt2\,\delta.
\]

---

## 2. 有限维 Bakry–Émery 张量与强迫 Bochner 不等式

基底方程为
\[
\operatorname{Ric}_B-\nabla^2\sigma
=-3\gamma_B+\frac12d\sigma^2+\frac12U^*h_{\mathbb H^2}+E_B,
\qquad E_B=E|_{TB}.
\]
基底实维为 \(2\)，故
\[
\begin{aligned}
\operatorname{Ric}^{\,4}_f
&=\operatorname{Ric}_B+\nabla^2f-\frac1{4-2}df^2\\
&=\operatorname{Ric}_B-\nabla^2\sigma-\frac12d\sigma^2\\
&=-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B.
\end{aligned}
\tag{2.1}
\]
若 \(\|E_B\|_{\mathrm{op}}\le\delta\)，则
\[
\boxed{\operatorname{Ric}^{\,4}_f\ge-(3+\delta)\gamma_B.}
\tag{2.2}
\]

令
\[
e=|dU|^2,\qquad
A_{ij}=\langle U_i,U_j\rangle,\qquad
V(X)=\langle dU(X),F\rangle.
\]
强迫 Bochner 公式是
\[
\frac12Le
=|DdU|^2+\operatorname{div}_\sigma V-|F|^2
+\frac12|dU(\nabla\sigma)|^2
+\frac12\operatorname{tr}(A^2)+2\det A-3e+E_B:A.
\tag{2.3}
\]
利用
\[
\frac12\operatorname{tr}(A^2)+2\det A
=\frac12e^2+\det A\ge\frac12e^2
\]
以及 \(E_B:A\ge-\delta e\)，得到
\[
\boxed{
\frac12Le\ge
|DdU|^2+\operatorname{div}_\sigma V-|F|^2
+\frac12e^2-(3+\delta)e.
}
\tag{2.4}
\]
记
\[
a=3+\delta,\qquad \kappa=2a=6+2\delta,\qquad
b=\|F\|_{L^\infty}.
\]
则反应项写成
\[
\frac12e(e-\kappa).
\]

---

## 3. 正确的截断检验恒等式

令
\[
u=(e-k)_+,\qquad k\ge\kappa,
\]
并取紧支撑 Lipschitz 函数 \(0\le\eta\le1\)。在集合 \(A_k=\{e>k\}\) 上有
\(\nabla e=\nabla u\)。对 (2.4) 乘以 \(\eta^2u\) 后积分，必须保留
\[
\boxed{
\int\eta^2u\,\operatorname{div}_\sigma V\,d\mu
=
-\int\eta^2\langle V,\nabla u\rangle\,d\mu
-2\int\eta u\langle V,\nabla\eta\rangle\,d\mu.
}
\tag{3.1}
\]
同时
\[
|V|\le b\sqrt e.
\tag{3.2}
\]

逐项分部积分与 Young 不等式给出
\[
\boxed{
\begin{aligned}
&\frac14\int\eta^2|\nabla u|^2\,d\mu
+\int\eta^2u|DdU|^2\,d\mu
+\int\eta^2u\,\frac12e(e-\kappa)\,d\mu\\
&\qquad\le
3\int u^2|\nabla\eta|^2\,d\mu
+4b^2\int_{A_k}\eta^2e\,d\mu .
\end{aligned}}
\tag{3.3}
\]
这里第一项 \(-\int\eta^2\langle V,\nabla u\rangle\) 产生
\(b^2\int\eta^2e\)，不能丢弃。

反应项还有精确展开
\[
\boxed{
u\,\frac12e(e-\kappa)
=\frac12\left[
u^3+(2k-\kappa)u^2+k(k-\kappa)u
\right].
}
\tag{3.4}
\]
特别地，\(k\ge\kappa\) 时同时控制 \(u^3\) 与 \(\kappa u^2\)。

---

## 4. 归一化局部估计

取 \(\eta=\chi^{m/2}\)，其中 \(m\ge6\)，\(0\le\chi\le1\)，且
\(|\nabla\chi|\le D\)。由
\[
\chi^{m-2}D^2u^2
\le \varepsilon\chi^m u^3+C_{\varepsilon,m}D^6\,1_{A_k},
\]
以及
\[
b^2u\le\varepsilon u^3+C_\varepsilon b^3,
\]
可从 (3.3) 得到
\[
\boxed{
\begin{aligned}
&\int\chi^m|\nabla u|^2\,d\mu
+\int\chi^m u|DdU|^2\,d\mu
+\int\chi^m(u^3+\kappa u^2)\,d\mu\\
&\qquad\le
C_m\bigl(D^6+b^3+b^2k\bigr)
\,\mu(A_k\cap\operatorname{supp}\chi).
\end{aligned}}
\tag{4.1}
\]
这已经是一条不依赖先验 orbit 能量的局部正则估计。

由 (2.2)，加权空间满足有限维曲率维数条件
\[
CD(-(3+\delta),4).
\]
因而在半径 \(s\) 满足 \((3+\delta)s^2\le1\) 的球上，有仅依赖有效维数 \(4\) 的：

\[
\frac{\mu(B_{2s})}{\mu(B_s)}\le C_4,
\tag{4.2}
\]
以及归一化 Sobolev 不等式
\[
\boxed{
\left(\fint_{B_s}|\phi|^4\,d\mu\right)^{1/2}
\le C_4s^2\fint_{B_s}|\nabla\phi|^2\,d\mu
+C_4\fint_{B_s}\phi^2\,d\mu .
}
\tag{4.3}
\]
这里始终使用 \(\fint=\mu(B)^{-1}\int\)，完全不需要 \(\mu(B)\) 的统一正下界。

---

## 5. 无先验能量与体积输入的内域 ceiling

设 \(B_{\gamma_B}(p,2r)\) 紧含于反射加倍后的基底，并且不接触出口端面。定义
\[
s=\min\left\{\frac r8,\ \kappa^{-1/2},\ b^{-1/2}\right\},
\]
其中 \(b=0\) 时把 \(b^{-1/2}\) 解释为 \(+\infty\)。

在 \(B_{2s}\) 上取递减球列与递增能级
\[
k_j=\kappa+\Lambda s^{-2}(1-2^{-j}).
\]
由 (4.1)–(4.3)，对归一化超能级测度
\[
\Theta_j=
\frac{\mu(\{e>k_j\}\cap B_{s_j})}{\mu(B_{2s})}
\]
得到
\[
\boxed{
\Theta_{j+1}
\le C_4\,2^{20j}\Lambda^{-4}\Theta_j^2.
}
\tag{5.1}
\]
取一个仅依赖 \(C_4\) 的固定大常数 \(\Lambda\)，迭代给出
\(\Theta_j\to0\)。于是
\[
\boxed{
\sup_{B_s(p)}e
\le\kappa+\Lambda s^{-2}.
}
\tag{5.2}
\]

逐点应用于 \(B_r(p)\) 得到：

\[
\boxed{
\sup_{B_r(p)}e
\le C\bigl(\kappa+b+r^{-2}\bigr)
=C\bigl(6+2\delta+b+r^{-2}\bigr),
}
\tag{5.3}
\]
其中 \(C\) 只来自有效维数 \(4\) 的归一化 doubling–Sobolev 常数。结合 (1.5)，
\[
\boxed{
\sup_{B_r(p)}e
\le C\bigl(1+\delta+r^{-2}\bigr).
}
\tag{5.4}
\]

这是真正独立于以下量的内域上界：

* \(\int e\,d\mu\)；
* \(\mu(B_r)\) 的绝对大小；
* connector 的总长度；
* \(T^2\) 或 \(S^1\) 的塌缩尺度。

正的 \(u|DdU|^2\) 项还给出超能级上的加权 Hessian 控制 (4.1)。

---

## 6. 反射中心与出口端面的假设

### 反射中心

若中心反射给出光滑加倍，则中心圆在加倍基底中是普通内点集；对跨越中心的球可直接使用 (5.3)，没有额外通量项。

对 \(\|E\|_{\mathrm{op}}\le\delta\) 的全测地中心切片，
\[
R(q_0)=-6+\operatorname{tr}E-2E_{nn}.
\]
因此
\[
K(0)=12-2\left\langle \operatorname{tr}E-2E_{nn}\right\rangle,
\]
并且
\[
\boxed{
\langle e(0,\cdot)\rangle_\mu
=K(0)+\langle h^2\rangle_\mu
\ge12-8\delta.
}
\tag{6.1}
\]
估计 (5.3) 的常数目前不足以把右端压到 \(12-8\delta\) 以下；它给出几何一致的有界性，但不是
\[
e\le6+C\delta
\]
这种接近精确阈值的估计。

### 出口端面

若球接触出口，有两种可直接使用的情形：

1. 几何与方程可光滑延拓穿过出口，且延拓区域仍满足同样的 \(E\)、\(F\)、\(\operatorname{Ric}_f^4\) 控制；
2. 出口迹满足 \(e\le E_{\mathrm{out}}\)，出口 collar 具有相对型 doubling–Sobolev 不等式。

第二种情形取
\[
k\ge\max\{\kappa,E_{\mathrm{out}}\}
\]
后，\(u=(e-k)_+\) 在出口迹上为零，分部积分没有端面项，并得到
\[
\boxed{
\sup_{\text{半 collar}}e
\le C\left(\max\{\kappa,E_{\mathrm{out}}\}+b+r^{-2}\right).
}
\tag{6.2}
\]

若没有出口能量迹，也没有延拓，则会出现
\[
\int_{\Sigma_{\rm out}}\eta^2u\langle V,\nu\rangle\,d\mu_\Sigma,
\qquad
\frac12\int_{\Sigma_{\rm out}}\eta^2u\,\partial_\nu e\,d\mu_\Sigma .
\tag{6.3}
\]
即使 \(|F|\le b\)，第一项也只有
\[
|u\langle V,\nu\rangle|
\le b\,u\sqrt e,
\]
所以出口处的大 \(e\) 可携带任意大的通量。

---

## 7. 为什么点态 Bernstein 法不能给出 \(6+C\delta\)

仅控制 \(F\)，不控制 \(DF\)，在一个点上无法控制
\(\langle dU,DF\rangle\)。这一现象可由完全显式的光滑 jet 看出。

令 \(U\) 沿 \(\mathbb H^2\) 中一条测地线运动，局部写作
\[
U(x)=\Gamma(\psi(x)),
\]
并令
\[
\psi'(0)=A,\qquad
\psi''(0)=0,\qquad
\psi'''(0)=-\frac12A^3.
\]
则在 \(x=0\)
\[
e=A^2,\qquad \nabla e=0,\qquad F=\psi''=0,\qquad |DdU|=0,
\]
但
\[
\langle dU,DF\rangle
=A\psi'''=-\frac12A^4=-\frac12e^2.
\]
它恰好抵消二次反应。并且在宽度
\[
|x|\lesssim \delta A^{-3}
\]
的条带上仍可保持 \(|F|\lesssim\delta\)。所以任意大的点态能量可由越来越窄的强迫变化层支撑；固定半径的估计 (5.3) 通过积分吸收排除了这种层在固定缓冲球中独立存在。

同样，标量比较系统具有显式端面层
\[
q_\varepsilon(d)=\frac6{(d+\varepsilon)^2},
\]
满足
\[
q_\varepsilon''=q_\varepsilon^2
\ge q_\varepsilon(q_\varepsilon-\kappa).
\]
其端面值 \(6/\varepsilon^2\) 可任意大，而距端面 \(r\) 处仅降到 \(O(r^{-2})\)。这说明没有出口迹时，\(r^{-2}\) 项具有真实的比较机制，不是截断计算的纯技术产物。

---

## 8. 最强可得结论

修正后的强迫系统确实通过二次反应、正 Hessian 项以及有限维 \(CD(-(3+\delta),4)\) 的归一化 Sobolev 理论给出：

\[
\boxed{
\sup_{B_r}e\le C(1+\delta+r^{-2}),
}
\]
不需要先验局部能量、非塌缩体积或 connector 长度控制。

但由这些输入尚不能得到接近精确常数的
\[
\sup e\le6+C\delta.
\]
阻碍来自超能级界面上的
\(-\int\eta^2\langle V,\nabla u\rangle\)、出口通量，以及 \(DF\) 可在尺度
\(\delta e^{-3/2}\) 上剧烈变化。一个接近 \(6\) 的 resolvent 论证需要对实际 doubled connector 的 massive Green 核建立类似
\[
\sup_x\int |\nabla_yG_\kappa(x,y)|\,d\mu_y
\le C\kappa^{-1/2},
\]
并同时处理截断产生的超能级界面通量；归一化局部曲率维数估计本身只给出上述 \(C(1+\delta+r^{-2})\) ceiling。