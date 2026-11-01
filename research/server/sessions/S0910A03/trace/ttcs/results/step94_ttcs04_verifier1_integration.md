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
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs04_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step94_ttcs04_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the proposed invariant horizontal Noether/Bianchi identity for the full two-dimensional free-T2 reduction. With horizontal residual H=Ric_B-Hess sigma-(1/2)d sigma^2-(1/2)U*h-Q gamma+3 gamma, area residual T=L sigma-6-Q, orbit residual Z=tau_sigma(U)+grad_U Q, and variable-charge work one-form m_q=D_qQ[dq]=e^{-3sigma}<M^-1q,dq>, check whether
2 div_sigma H-d tr H = -dT-T d sigma-<Z,dU>-m_q
is exactly correct in signs and coefficients. Derive it independently using contracted Bianchi, harmonic-map stress divergence, and the total differential dQ=d_UQ-3Q d sigma+D_qQ[dq]. Then specialize to gamma=dr^2+psi^2dtheta^2, H=C dr^2, T=Z=0, diagonal charge, and verify it gives C'=-2(u+h)C-wb with the Step90 physical normalization. Explain whether this identity supplies a genuinely independent two-ended constraint or is a propagation/compatibility identity, and identify the most useful global adjoint pairing or moment it yields when q and H vanish on exact end collars but T,Z and Ricci defects are only C0-small. Flag any issue arising because H,T,Z are all blocks of the same Ricci defect rather than independent sources.

## Integrated Scientific Memo

## 核验结论

采用
\[
L=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle,\qquad
\tau_\sigma(U)=\tau(U)+dU(\nabla\sigma),
\]
以及
\[
(\operatorname{div}_\sigma H)_j=\nabla^iH_{ij}
   +H(\nabla\sigma,\partial_j),
\]
则所提恒等式
\[
\boxed{
2\operatorname{div}_\sigma H-d\operatorname{tr}H
=-dT-T\,d\sigma-\langle Z,dU\rangle-m_q
}
\]
在符号和全部系数上都精确正确。这里
\[
\langle Z,dU\rangle_j=\langle Z,dU(\partial_j)\rangle_h,
\qquad
m_q=e^{-3\sigma}\langle M^{-1}q,dq\rangle .
\]

需特别注意记号转换：本题定义
\[
T=L\sigma-6-Q.
\]
而 Step 90 使用 \(L\sigma=6+Q-T_{90}\)，故 \(T=-T_{90}\)。若使用 Step 90 的 \(T_{90}\)，右端前两项应写成
\[
+dT_{90}+T_{90}d\sigma.
\]

## 张量推导

记
\[
s=d\sigma,\qquad A=U^*h,\qquad e=|dU|^2.
\]
则
\[
H=\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12s\otimes s-\frac12A-Q\gamma+3\gamma
\]
且由于 \(\dim B=2\)，
\[
\operatorname{tr}H
=R-\Delta\sigma-\frac12|s|^2-\frac12e-2Q+6.
\tag{1}
\]

使用
\[
\operatorname{div}\operatorname{Ric}=\frac12dR,
\]
\[
\operatorname{div}\operatorname{Hess}\sigma
=d\Delta\sigma+\operatorname{Ric}(\nabla\sigma,\cdot),
\]
\[
\operatorname{div}(s\otimes s)
=(\Delta\sigma)s+\operatorname{Hess}\sigma(\nabla\sigma,\cdot),
\]
以及 harmonic-map stress 恒等式
\[
\operatorname{div}(U^*h)
=\langle\tau(U),dU\rangle+\frac12de,
\]
从 (1) 直接整理得
\[
\operatorname{div}H
=\frac12d\operatorname{tr}H-\frac12d\Delta\sigma
-\operatorname{Ric}(\nabla\sigma,\cdot)
-\frac12(\Delta\sigma)d\sigma
-\frac12\langle\tau(U),dU\rangle .
\tag{2}
\]

另一方面，由 \(H\) 的定义，
\[
\begin{aligned}
\operatorname{Ric}(\nabla\sigma,\cdot)
={}&H(\nabla\sigma,\cdot)
+\operatorname{Hess}\sigma(\nabla\sigma,\cdot)
+\frac12|\nabla\sigma|^2d\sigma\\
&+\frac12A(\nabla\sigma,\cdot)+(Q-3)d\sigma .
\end{aligned}
\]
代入 (2)，加入 \(H(\nabla\sigma,\cdot)\)，并用
\[
A(\nabla\sigma,\cdot)
=\langle dU(\nabla\sigma),dU\rangle,
\]
得到
\[
\operatorname{div}_\sigma H
=\frac12d\operatorname{tr}H-\frac12dL\sigma
-\frac12\langle\tau_\sigma(U),dU\rangle
+\left(3-Q-\frac12L\sigma\right)d\sigma .
\tag{3}
\]

由
\[
L\sigma=6+Q+T,\qquad dL\sigma=dQ+dT,
\]
式 (3) 化为
\[
\begin{aligned}
\operatorname{div}_\sigma H
={}&\frac12d\operatorname{tr}H-\frac12dT-\frac12dQ
-\frac12\langle\tau_\sigma(U),dU\rangle\\
&-\frac32Q\,d\sigma-\frac12T\,d\sigma .
\end{aligned}
\tag{4}
\]

现在使用完整链式法则
\[
\boxed{dQ=d_UQ-3Q\,d\sigma+m_q},
\qquad
d_UQ=\langle\nabla_UQ,dU\rangle,
\tag{5}
\]
和
\[
\tau_\sigma(U)=Z-\nabla_UQ.
\]
于是
\[
-\frac12dQ-\frac12\langle\tau_\sigma(U),dU\rangle
=\frac32Q\,d\sigma-\frac12m_q-\frac12\langle Z,dU\rangle .
\]
这恰好消去 (4) 中的 \(-\frac32Qd\sigma\)，从而
\[
\operatorname{div}_\sigma H
=\frac12d\operatorname{tr}H-\frac12dT-\frac12T\,d\sigma
-\frac12\langle Z,dU\rangle-\frac12m_q,
\]
即所声称恒等式。

这也说明两个敏感系数为何不可改变：\(-\frac12U^*h\) 使 \(de\) 项消去，\(-\frac12d\sigma^2\) 使 Hessian-gradient 项正确合并为 \(dL\sigma\)。

## 径向专门化与 Step 90 归一化

令
\[
\gamma=dr^2+\psi(r)^2d\theta^2,\qquad
u=\sigma',\qquad h=\frac{\psi'}{\psi},\qquad
H=C(r)\,dr^2.
\]
则
\[
\operatorname{tr}H=C,\qquad
(\operatorname{div}H)_r=C'+hC,
\]
因而
\[
(\operatorname{div}_\sigma H)_r=C'+(u+h)C.
\]
所以
\[
(2\operatorname{div}_\sigma H-d\operatorname{tr}H)_r
=C'+2(u+h)C.
\tag{6}
\]

对
\[
M=\operatorname{diag}(e^\alpha,e^{-\alpha}),\qquad q=(q(r),0),
\]
采用 Step 90 的有符号物理变量
\[
\widetilde w=e^{-(3\sigma+\alpha)/2}q,\qquad
b=e^{-(3\sigma+\alpha)/2}q',
\]
则
\[
m_q(\partial_r)=e^{-3\sigma-\alpha}qq'=\widetilde w\,b.
\]
在 Step 90 的 \(q\ge0\) taper 中，\(\widetilde w=w=\sqrt{2Q}\)。若允许 \(q\) 变号，应保留有符号的 \(\widetilde w\)，否则 \(m_q\) 是 \(\operatorname{sgn}(q)wb\)。

当 \(T=Z=0\) 时，(6) 给出
\[
C'+2(u+h)C=-wb,
\]
即
\[
\boxed{C'=-2(u+h)C-wb,}
\]
与 Step 90 完全一致；没有额外的 \(1/2\)。Step 90 中混合 Ricci 分量为 \(b/2\)，但 charge-work 一形式本身确为 \(wb\)。

## 性质：兼容性/传播恒等式，而非额外场方程

这是四维 contracted Bianchi 恒等式在自由 \(T^2\) 约化中的水平分量。它不是一条独立局部方程，也不额外提供一个可自由指定的两端边界条件。

但当只强制部分约化方程时，它变成非平凡的可解性条件。例如径向情形
\[
C(r)=-\frac1{\mu(r)}
\int_{r_-}^{r}\mu(s)\,w(s)b(s)\,ds,\qquad
\mu=e^{2\sigma}\psi^2.
\]
故同时要求 \(C(r_-)=C(r_+)=0\) 强制第二个加权矩
\[
\boxed{\int_{r_-}^{r_+}e^{2\sigma}\psi^2wb\,dr=0.}
\tag{7}
\]
它不同于普通 charge-flux 条件 \(\int q'\,dr=0\)。因此 Step 90 的单调放电 \(w\ge0,b\le0\) 必然留下非零终端 \(C\)，正是传播而非独立约束的体现。

更一般地，径向恒等式为
\[
C'+2(u+h)C=-T'-uT-\langle Z,U'\rangle-m_q(\partial_r).
\]
乘以 \(\mu=e^{2\sigma}\psi^2\) 并积分得
\[
\boxed{
[\mu(C+T)]_{r_-}^{r_+}
+\int_{r_-}^{r_+}\mu
\bigl[m_q(\partial_r)+\langle Z,U'\rangle-(u+2h)T\bigr]\,dr=0.
}
\tag{8}
\]
若端点 \(C=T=0\)，这就是最直接的两端兼容矩。

## 最有用的全局 adjoint 配对

令
\[
d\mu_\sigma=e^\sigma d\mu_\gamma.
\]
取在精确端 collar 内截断为零的向量场 \(X\)，加权分部积分给出
\[
\boxed{
\begin{aligned}
\int_Bm_q(X)\,d\mu_\sigma
=\int_B\Big[
&2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X\\
&+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\Big]d\mu_\sigma .
\end{aligned}}
\tag{9}
\]
这条弱形式不含 \(dH,dT,dZ\)，因而正适合 Ricci defect 只有 \(C^0\) 控制的情形。特别取 \(X=\nabla\phi\)，
\[
\boxed{
\begin{aligned}
\int_Bm_q(\nabla\phi)\,d\mu_\sigma
=\int_B\Big[
&2H:\operatorname{Hess}\phi-(\operatorname{tr}H)L\phi\\
&+T\Delta\phi-\langle Z,dU(\nabla\phi)\rangle
\Big]d\mu_\sigma .
\end{aligned}}
\tag{10}
\]
最有用的 \(\phi\) 是两端分离的 drift-adjoint potential：在深端 collar 上常值，并使其 Hessian/漂移 Laplacian 与水平算子的形式伴随核尽量匹配。径向选择 \(\phi'=e^\sigma\psi\) 恰好消去 \(H\) 项并恢复 (8)。

若不将 \(X\) 截断为零，仅有 \(H=0\) 并不足以消灭所有端项：边界还含 \(T\) 项。因此在题设“\(H,q\) 于端 collar 消失但 \(T,Z\) 仅小”的条件下，应在 collar 内把 \(X\) 截断，而不能仅依赖 \(H=0\)。

## 同一 Ricci defect 的结构性警告

\(H,T,Z\) 和 \(dq\) 并非独立源，而是同一个
\[
E=\operatorname{Ric}_g+3g
\]
的水平、垂直迹、垂直无迹和混合块；在相应约定下
\[
H=E_B,\qquad T=-\operatorname{tr}_{\rm orb}E,\qquad
Z=-2\widehat E_{\rm orb,0},
\]
且 \(dq\) 由 \(E_{\rm mix}\) 决定。因此不能任意指定 \(b\) 后再独立令 \(H=T=Z=0\)：Bianchi 恒等式正会传播出非零 \(H\)。

同理，(9)–(10) 虽提供精确的有符号全局矩，并把导数从 \(C^0\)-小 defect 上移走，却不自动产生统一 coercivity。其右端仍带有 \(\operatorname{Hess}\phi\)、\(dU\,d\phi\) 和可能很大的加权体积；Step 94 的 redshift benchmark 已表明朴素 weighted-capacity 常数可严重退化。因此该恒等式给出了正确的两端伴随/矩对象，但本身不是独立障碍；要获得真正两端排除结论，还需由水平—轨道耦合或 separator stability 提供统一伴随范数控制或可用的符号机制。