# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 90,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step90_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step90_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the structured Maxwell-area-orbit-map system for an approximately Einstein free-T^2 metric after the Step 90 charge-potential cancellation. Starting from Q=(1/2)e^{-3σ}q^T M^{-1}q, S_F=-grad_H Q, the mixed Ricci law for dq, Lσ=6+Q-tr_orb E, and the base drift equation, look for a geometrically natural energy or variable-potential comparison that controls physical twist without differentiating Ricci defect. Explore combinations of orbit energy e, |∇σ|^2, Q, and the normalized physical charge amplitude, and distinguish what can be proved from what merely looks plausible. Identify either (i) a coercive inequality compatible with exact OT ends and a minimal separator, or (ii) a concrete concentration/escape mechanism consistent with all reduced equations. Provide explicit equations and the most decisive next computation or proof, not broad brainstorming.

## Integrated Scientific Memo

## 结论

Step 90 之后最自然且真正闭合一阶交换项的组合是
\[
\boxed{W=e+2Q+3|\nabla\sigma|^2.}
\]
它把所有 \(dq\) 和 defect 的导数放进一个受控散度通量中，但其零阶项对大 \(Q\) **不强制**。现有方程因此尚不能给出兼容 exact OT ends 的全局 coercive ceiling；相反，它们允许一个明确的“高 twist 核心—面积红移—低振幅放电层”机制。该机制目前是完整 reduced system 的局部形式解与匹配方案，而不是已构造出的完整两端度量。

Branch 2 提出的 \(\langle Q\rangle=O(\delta^2)\) 论证不能闭合：它预先需要 \(e\le B<36\)，而 variable-\(Q\) 情形正缺少这个 ceiling；仅有全局平均 \(\int Q\) 小也不足以控制 resolvent kernel 从某点看到的局部 \(Q\)-浓集。其 Feynman–Kac occupation 推断还需要热核/容量或 Kato 范数控制，不能由全局加权平均推出。

---

## 1. 规范化 reduced system

令
\[
p^2=|\nabla\sigma|^2,\qquad
b_i=e^{-3\sigma/2}M^{-1/2}\nabla_iq ,
\]
并写
\[
\tau_\sigma(U)=S+\Theta,\qquad S=-\nabla_{\mathbb H^2}Q,
\qquad T=\operatorname{tr}_{\rm orb}E.
\]
则
\[
L\sigma=6+Q-T,
\]
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma-\frac12d\sigma^2
=(-3+Q)\gamma+\frac12U^*h+E_B.
\]
Step 90 已验证
\[
\operatorname{Hess}_{\mathbb H^2}Q=Qh,\qquad |\nabla Q|^2=Q^2,
\]
以及
\[
|b|^2=4|E_{\rm mix}|_{\rm HS}^2.
\]
因此若 \(\|E\|_{\rm op}\le\delta\)，则在当前二维混合块规范下
\[
|b|\le2\sqrt2\,\delta,\qquad |\Theta|\le2\delta,\qquad |T|\le2\delta.
\]

定义
\[
\zeta_i=\langle\nabla Q,U_i\rangle,\quad
m_i=D_qQ[\nabla_iq],\quad
X=\langle d\sigma,\zeta\rangle,\quad
Y=\langle d\sigma,m\rangle .
\]
正确的尺度是
\[
|\zeta|\le Q\sqrt e,\qquad |X|\le pQ\sqrt e,
\]
而不是 \(p\sqrt{Qe}\)。此外
\[
|m|\le\sqrt{2Q}\,|b|,\qquad
|R_q|\le\sqrt{2Qe}\,|b|.
\]

---

## 2. Step-90 的核心 Bochner 消去

令 \(A=U^*h\)，
\[
\Phi(A)=\frac12\operatorname{tr}(A^2)+2\det A\ge\frac12e^2,
\quad
V_\Theta(X)=\langle dU(X),\Theta\rangle.
\]
由
\[
\langle dU,DS\rangle=-Qe+3X+R_q
\]
和 base drift curvature 中的 \(+Qe\)，二者精确消去：
\[
\boxed{
\begin{aligned}
\frac12Le={}&|DdU|^2+\frac12|dU(\nabla\sigma)|^2+\Phi(A)-3e\\
&+3X+R_q+E_B{:}A
+\operatorname{div}_\sigma V_\Theta
+\langle\nabla Q,\Theta\rangle-|\Theta|^2 .
\end{aligned}}
\tag{2.1}
\]
这解释了为什么 Step 89 对固定 \(Q\) 的公式不能直接用于可变 charge：固定 charge 时遗留的 \(\sigma\)-交换项在可变情形必须与 area、Maxwell 方程一起处理。

---

## 3. 不微分 Ricci defect 的 \(Q\) 方程

令
\[
P_a=\partial_{q_a}Q=e^{-3\sigma}(M^{-1}q)^a,\qquad
Z_Q=\sum_aP_a\nabla q_a .
\]
把所有二阶 \(q\) 项保留为加权散度，可得
\[
\boxed{
\begin{aligned}
LQ={}&\operatorname{div}_\sigma Z_Q
+Qe-4Q^2-18Q+3QT+9Qp^2\\
&-6X-R_q-3Y+\langle\nabla Q,\Theta\rangle .
\end{aligned}}
\tag{3.1}
\]
这里
\[
|Z_Q|\le\sqrt{2Q}\,|b|.
\]
同时，area-gradient Bochner 式为
\[
\boxed{
\begin{aligned}
\frac12Lp^2={}&|\operatorname{Hess}\sigma|^2-3p^2-2Qp^2+\frac12p^4
+\frac12|dU(\nabla\sigma)|^2\\
&+E_B(\nabla\sigma,\nabla\sigma)+X+Y\\
&-\operatorname{div}_\sigma(T\nabla\sigma)+T(6+Q-T).
\end{aligned}}
\tag{3.2}
\]

---

## 4. 唯一的同时消去组合

取
\[
\boxed{W=e+2Q+3p^2.}
\]
因为
\[
\frac12LW=\frac12Le+LQ+\frac32Lp^2,
\]
所以
\[
3X-6X+3X=0,\qquad R_q-R_q=0,\qquad -3Y+3Y=0.
\]
于是
\[
\boxed{
\begin{aligned}
\frac12LW={}&\operatorname{div}_\sigma\mathcal J
+|DdU|^2+3|\operatorname{Hess}\sigma|^2
+2|dU(\nabla\sigma)|^2+\Phi(A)\\
&+\frac32p^4+3Qp^2+Qe
-3e-9p^2-18Q-4Q^2\\
&+E_B{:}A+3E_B(\nabla\sigma,\nabla\sigma)
+2\langle\nabla Q,\Theta\rangle-|\Theta|^2\\
&+18T+6QT-3T^2 ,
\end{aligned}}
\tag{4.1}
\]
其中
\[
\boxed{\mathcal J=V_\Theta+Z_Q-3T\nabla\sigma.}
\tag{4.2}
\]
并且
\[
|\mathcal J|
\le |\Theta|\sqrt e+\sqrt{2Q}|b|+3|T|p
\le (2+2\sqrt2+2\sqrt3)\delta\sqrt W .
\tag{4.3}
\]

这是当前最强的无 \(\nabla E\) 结构式。系数 \(1,2,3\) 不是任意调参：同时消去 \(X,R_q,Y\) 强制给出该比例。

---

## 5. 为什么它不是 coercive ceiling

在一点令
\[
d\sigma=dU=dq=0,\qquad E_B=T=\Theta=0,\qquad Q=Q_0.
\]
可选择二阶 jet 满足精确 reduced equations：
\[
\operatorname{Hess}\sigma=\frac{6+Q_0}{2}\gamma,\qquad
DdU=\frac{Q_0}{2}\gamma\otimes\partial_\alpha,\qquad
K_\gamma=\frac32Q_0,
\]
其中 \(\alpha\) 沿 charge 选定的目标测地线。此时
\[
W=2Q_0
\]
且 (4.1) 的非散度右端为
\[
3|\operatorname{Hess}\sigma|^2+|DdU|^2-18Q_0-4Q_0^2
=54-2Q_0^2.
\]
因此仅从 \((e,Q,p^2)\) 不能推出统一的
\[
\frac12LW\ge\operatorname{div}_\sigma\mathcal J+aW^2-bW-C,
\qquad a>0.
\]
大 \(Q\) 的共同临界点是实质性退化，不是 Young 不等式损失。

这也否定了把 \(Q\) 简单看作“有利势”的做法：其在 \(e\)-Bochner 中消去 \(Qe\) 后，\(Q\)-自身方程仍含 \(-4Q^2\)。

---

## 6. 物理 twist 的一阶输运及逃逸机制

令
\[
w=\sqrt{2Q}=e^{-3\sigma/2}|M^{-1/2}q|.
\]
由 \(dQ\) 的精确分解，
\[
\boxed{
\left|dw+\frac32w\,d\sigma\right|
\le \frac12w\,|dU|+|b|.
}
\tag{6.1}
\]
在
\[
M=\operatorname{diag}(e^\alpha,e^{-\alpha}),\qquad q=(q(r),0)
\]
的 charge 方向上，
\[
\boxed{
w'+\frac12(3\sigma'+\alpha')w=b,\qquad
w=e^{-(3\sigma+\alpha)/2}q.
}
\tag{6.2}
\]
round cusp 上 \(\sigma'=2,\alpha'=0\)，故
\[
w'+3w=b.
\]
因此小 \(b\) 只保证向外的物理振幅趋于 \(O(\delta)\)，并不控制向内反演；向内会指数放大。一个大 coordinate charge 可以在核心很大，但在面积增长后其物理振幅已被红移到 \(O(\delta)\)，随后以 \(|b|=O(\delta)\) 将 \(q\) taper 到零，从而接上 exact OT open end。

具体径向系统为
\[
\gamma=dr^2+\psi(r)^2d\theta^2,\quad
Q=\frac12e^{-3\sigma-\alpha}q^2,
\]
\[
\sigma''+\Big(\frac{\psi'}{\psi}+\sigma'\Big)\sigma'=6+Q-T,
\]
\[
\alpha''+\Big(\frac{\psi'}{\psi}+\sigma'\Big)\alpha'=Q+\Theta_\alpha,
\]
以及两个水平 defect：
\[
E_{rr}=K-\sigma''+3-Q-\frac12(\sigma')^2-\frac12(\alpha')^2,
\]
\[
E_{\theta\theta}=K-\frac{\psi'}{\psi}\sigma'+3-Q,\qquad
K=-\frac{\psi''}{\psi}.
\]
精确核心 jet 满足
\[
\sigma=\sigma_0+\frac{6+Q_0}{4}r^2+O(r^4),\qquad
\alpha=\alpha_0+\frac{Q_0}{4}r^2+O(r^4),
\]
\[
\psi=r-\frac{Q_0}{4}r^3+O(r^5).
\]
于是
\[
\frac12(3\sigma'+\alpha')
=\left(Q_0+\frac92\right)r+O(r^3),
\]
故
\[
w(r)\sim w_0
\exp\!\left[-\frac12\left(Q_0+\frac92\right)r^2\right].
\]
当
\[
r\asymp\sqrt{\frac{\log(w_0/\delta)}{Q_0}}
\]
时可把 \(w\) 降至 \(O(\delta)\)，然后在物理规范
\[
b=e^{-(3\sigma+\alpha)/2}q'
\]
下以 \(O(\delta)\) 代价令 \(q\to0\)。

这与 exact OT ends 不矛盾：exact Einstein 时 charge 常数且 OT open end 强制全局 \(q=0\)；approximate Einstein 时 \(dq\) 虽在物理范数中小，却可在红移区累计消除 coordinate charge。

---

## 7. 关于平均 \(Q\) 估计的准确地位

由
\[
dQ=-3Q\,d\sigma+\zeta+m
\]
乘 \(\nabla\sigma\) 并积分，确有
\[
\begin{aligned}
\int_\Omega\!\left[3Qp^2+Q(6+Q-T)\right]d\mu
={}&\int_\Omega\!\left[
\langle\nabla Q,dU(\nabla\sigma)\rangle
+\langle w,b\rangle\cdot\nabla\sigma\right]d\mu\\
&+\int_{\partial\Omega}Q\,\partial_\nu\sigma\,d\mu_\partial .
\end{aligned}
\]
Young 不等式给出条件式
\[
(6-2\delta)\int Q+\int Q^2
\le\frac16\int Qe+\frac83\delta^2\mu(\Omega)
+\text{boundary flux}.
\tag{7.1}
\]
若已知 \(e\le B<36-12\delta\)，则它确实推出平均 \(Q=O(\delta^2)\)。但目前 variable twist 情形并无该先验 ceiling；使用 Step 89 的 fixed-\(Q\) ceiling 会循环论证。此外：

* 平均 \(Q\) 小允许高且极薄的 twist 核；
* resolvent/Feynman–Kac 需要的是 kernel-weighted occupation、容量或 Kato 控制；
* \(\mu\{Q>a\}\) 的全局估计不能单独给出从任意起点出发的 occupation bound。

所以 (7.1) 是有价值的条件性 coercive average identity，而不是已完成的方案 (i)。

---

## 8. 最决定性的下一计算

应直接积分上述径向 core–taper 边值问题，并监测
\[
|b|,\quad |T|,\quad |\Theta_\alpha|,\quad
|E_{rr}|,\quad |E_{\theta\theta}|
\]
是否能同时保持 \(\le C\delta\)，同时满足：

1. 中心光滑性；
2. 核心 \(Q_0\gg1\)；
3. 红移后 \(q\) 在有限 collar 内降至零；
4. 外部精确 OT expanding cusp；
5. 两端和最小 separator 所需的全局拓扑/完备性。

这项计算会直接区分两种可能：

* 若可完成匹配，则得到与全部 reduced equations 相容的具体 twist escape；
* 若匹配必然失败，失败项将揭示所缺的全局 coercive 恒等式，最可能来自水平 Einstein 两分量与 Maxwell 输运的联合，而不是单独的 \(e\)-Bochner 或平均 \(Q\) 估计。

目前证据支持的最强结论是：\(W=e+2Q+3|\nabla\sigma|^2\) 是正确的结构能量，但大 \(Q\) 使其失去点态强制性；高 twist 核心经面积红移后以小 mixed defect 放电，是尚未被现有方程排除的具体逃逸机制。