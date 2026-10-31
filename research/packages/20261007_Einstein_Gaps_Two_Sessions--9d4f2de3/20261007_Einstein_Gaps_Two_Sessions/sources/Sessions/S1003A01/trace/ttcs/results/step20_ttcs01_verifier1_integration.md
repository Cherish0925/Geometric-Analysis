# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 20,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step20_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step20_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-19 core–exterior result, the inherited exact conformal stationarity argument, and the new Step-20 radial-conformal scripts/results. Check the mathematics and scientific interpretation. In particular: (i) does g -> e^{2phi}g implemented as G->e^{-2phi}G, h->e^{2phi}h preserve the O(-1) bolt geometry and exact CH endpoint contact? (ii) Are the component residual sums and scalar-solve experiments meaningfully testing the Euler equation, given the fixed spectral ansatz and exact cG[0] redundancy? (iii) Is the conclusion justified that J-P tends rapidly to zero while the nonzero trace-free tail charge lambda can remain, but no smooth full critical exact-collar cell can exist? Identify any formula/sign/normalization or optimization flaw, and state the strongest supported mathematical conclusion and the most consequential next finite-interface computation.

## Integrated Scientific Memo

# Verification memo

## 1. Radial conformal implementation, bolt, and CH endpoint

For
\[
g=\frac{dx^2}{4G(x)}+h(x),
\]
the substitutions
\[
G\mapsto \widetilde G=e^{-2\phi}G,\qquad h\mapsto \widetilde h=e^{2\phi}h
\]
give
\[
\widetilde g=\frac{dx^2}{4e^{-2\phi}G}+e^{2\phi}h=e^{2\phi}g.
\]
Thus the implementation has the correct sign and radial factor.

### Bolt geometry

Suppose, with \(y=x-x_0\),
\[
F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),\qquad f_1g_1=1.
\]
Since \(\phi\) is smooth in \(x\),
\[
\widetilde F'(x_0)=e^{2\phi(x_0)}F'(x_0),\qquad
\widetilde G'(x_0)=e^{-2\phi(x_0)}G'(x_0),
\]
and therefore
\[
\widetilde F'(x_0)\widetilde G'(x_0)=1.
\]
Also \(x-x_0\sim t^2\), so \(\phi(x(t))\) is smooth and even in the geodesic radius. The collapsing radius remains odd, the noncollapsing radii remain even, and the cone angle and \(O(-1)\) normal bundle are unchanged. The round-bolt condition is preserved because both noncollapsing directions receive the same conformal factor.

However, the physical bolt area changes:
\[
A_{\rm bolt}\propto x_0e^{2\phi(x_0)}.
\]
Hence \(x_0\) is no longer itself the physical area parameter. The supplied changes are tiny,
\[
\phi(x_0)\approx-3.12\times10^{-5}\quad(X=128),\qquad
\phi(x_0)\approx-8.96\times10^{-6}\quad(X=512),
\]
but an area optimization should either vary \(x_0\) jointly or constrain \(\phi(x_0)=0\).

### Endpoint contact is finite-order, not an exact CH collar

With
\[
\phi(u)=(1-u)^3p(u),
\]
one has
\[
\phi(X)=\phi_x(X)=\phi_{xx}(X)=0.
\]
Thus the conformal deformation preserves the metric 2-jet and curvature contact at the endpoint, assuming the base profile has the stated CH contact.

It does **not** preserve an exact CH germ on an open collar. Extending \(\phi\) by zero beyond \(X\) is generally only \(C^2\), because \(\phi_{xxx}(X)\) need not vanish. Therefore the stored spectral profile is not itself a smooth exact-collar metric. For that, \(\phi\) must vanish identically on a terminal subcollar or be flat to all orders at the gluing interface. This distinction is essential when invoking the exact-collar nonexistence theorem.

A further gauge point: after conformal rescaling, \(a_1^2=e^{2\phi}x\), not \(x\). Any tail decomposition written in the original \(x\)-gauge must first re-gauge a conformal record. The effect is negligible for the supplied tiny \(\phi\), but conceptually necessary.

---

## 2. Residual objective and numerical normalization

The least-squares residual in `perp_lm.py` is correctly normalized. Writing
\[
W=a_1a_2a_3,\qquad e=s+24,\qquad dt=\frac{dx}{2\sqrt G},
\]
its squared norm approximates
\[
\int W\,dt\left(\frac{|z|^2}{4}+\frac{e^2}{16}\right)
=\frac{J_6}{8\pi^2}.
\]
Consequently,
\[
\frac{P}{8\pi^2}=\sum R_{1:3}^2,\qquad
\frac{J_6-P}{8\pi^2}=\sum R_4^2.
\]
The component splitting in `perp_conformal_lm.py` therefore has the intended meaning.

### The `DualCell.costs` fields disagree with the verified residual

At \(x_0=.038,\ X=512\),
\[
\begin{aligned}
\text{stored `J'}&=0.995181162362,\\
\text{residual sum}&=0.995178186591,\\
\text{independent evaluator}&=0.995178186608.
\end{aligned}
\]
The residual and independent evaluations agree to about \(2\times10^{-11}\), while the stored `J` differs by \(2.98\times10^{-6}\). At \(X=128\), the discrepancy is about \(3.96\times10^{-7}\).

Thus the strongest supplied floating value for the ordinary \(X=512\) cell is
\[
\boxed{\frac{J_6}{8\pi^2}=0.995178186608},
\]
not \(0.9951812\). Any extrapolation or finite-\(X\) difference should consistently use the residual/independent evaluator. This shifts the extrapolated infinite-collar figure slightly, to approximately \(0.995166\), but does not materially change the claimed deficit scale.

### Exact \(cG[0]\) redundancy

Removing `cG[0]` is correct if, as stated, it cancels algebraically from `prof_factory`. It explains the exact Hessian null direction and the huge stored coefficients such as \(5.46\times10^4\) and \(-1.12\times10^9\): they are parametrization artifacts, not large geometric amplitudes.

The supplied conformal JSON files retain those old huge coordinates, despite the displayed current script resetting the redundant coordinate to zero. They were therefore generated by an earlier code version. A direct check
\[
R(z)=R(z\text{ with }cG[0]=0)
\]
should be done at machine precision, especially because a cancellation involving a \(10^9\) coefficient could otherwise amplify roundoff.

The Step-19 Hessian conclusion is correspondingly limited: it proves a strict local minimum only in the fixed finite spectral family, modulo this redundancy. It does not establish unrestricted metric stationarity.

---

## 3. What the conformal and scalar-solve experiments test

For the Ricci normalization \(\operatorname{Ric}_{CH}=-6g\), let
\[
e=s+24.
\]
The conformal first variation is
\[
\delta J_6[2fg]
=4\int f(\Delta_++6)e\,dV,
\qquad \Delta_+=-\operatorname{div}\nabla.
\]
For a radial function,
\[
(\Delta_++6)e
=-\left(e_{tt}+\frac{W_t}{W}e_t\right)+6e.
\]
Thus the sign and coefficient in `conformal_stationarity_check.py` are correct.

For the normalized objective \(j=J_6/(8\pi^2)\) and conformal basis \(q_k=\partial\phi/\partial c_k\),
\[
\boxed{
\frac{\partial j}{\partial c_k}
=\int q_k(\Delta_++6)e\,W\,dt
=\int q_k(\Delta_++6)e\,\frac{W}{2\sqrt G}\,dx .
}
\]
This identity is the clean direct test of the projected conformal Euler equation.

### Scalar-only minimization does not test the Euler equation of \(J_6\)

The `--scalar-solve` branch minimizes only
\[
\frac1{16}\int We^2\,dt
\]
with the shape frozen. Its conformal stationarity operator is proportional to
\[
(\Delta_++8)e,
\]
not \((\Delta_++6)e\). The variation of the trace-free channel \(P\) is part of the cancellation that produces the full \(J_6\) Euler equation.

Therefore:

- `grad_inf_optimized` near \(10^{-13}\) or \(10^{-10}\) means stationarity only for the scalar residual objective.
- The final full-\(J_6\) conformal gradients remain
  \[
  3.51\times10^{-5}\quad(X=128),\qquad
  2.57\times10^{-5}\quad(X=512).
  \]
- The full shape gradients are even larger,
  \[
  1.40\times10^{-3},\qquad 4.06\times10^{-4}.
  \]
- Hence neither scalar-solve record is stationary for \(J_6\), even in the enlarged finite-dimensional family.

The runs are still informative: they show that the scalar channel is already tiny and can be changed only slightly by small radial conformal factors:
\[
\begin{array}{c|c|c}
X&(J_6-P)/(8\pi^2)\text{ before}&\text{after}\\ \hline
128&3.4646\times10^{-7}&3.2969\times10^{-7}\\
512&3.3489\times10^{-8}&3.2418\times10^{-8}.
\end{array}
\]
The total decreases are only about \(2.1\times10^{-8}\) and \(1.3\times10^{-9}\). This supports insensitivity of the numerical cost to these twelve conformal modes, but not Euler stationarity.

Likewise, `--joint-outer` is not a true block-coordinate descent for one objective: every cycle ends with a scalar-only solve, which may increase \(P\), increase \(J_6\), or move away from full-\(J_6\) stationarity. A final full-\(J_6\) solve is required.

### Fixed spectral ansatz limitation

Twelve conformal coefficients test only twelve weighted moments
\[
\int q_k(\Delta_++6)e\,dV.
\]
They do not establish the pointwise equation. Because this operator differentiates the metric profiles to fourth order, degree and quadrature convergence are especially important.

Also, radial conformal variations are not fundamentally absent from the full diagonal \(a_1^2=x\) gauge: up to a radial reparametrization \(\widetilde x=e^{2\phi}x\), they are represented by changes of the shape functions and, if \(\phi(x_0)\ne0\), by a change in physical bolt area. The added conformal block primarily tests completeness and conditioning of the finite spectral truncation.

### Factor-of-two error in `conformal_stationarity_check.py`

Given
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2,
\]
the physical volume element is
\[
dV=2\pi^2W\,dt=\frac{\pi^2W}{\sqrt G}\,dx.
\]
The script uses
\[
\texttt{dv}=\frac{\pi^2W}{2\sqrt G}\,dx=\pi^2W\,dt,
\]
which is one half of the correct volume density. Consequently `scalar_energy_over_8pi2` is one half of the scalar residual channel reported by the least-squares code. Weighted RMS ratios and pointwise suprema are unaffected.

---

## 4. Exterior response: sign and asymptotics

Define
\[
m=-2k(\rho)\Theta,\qquad
\delta=m-w_0G(\rho),
\qquad
I(\rho)=\int_\rho^\infty\frac{G^2}{\mu}\,dx.
\]
For the minimizer,
\[
\mu w'=-\lambda G,\qquad
w=w_0-\lambda L(x,\rho).
\]
The moment mismatch satisfies
\[
\delta=\int_\rho^\infty f_-^2(w-w_0)\,dx=-\lambda I.
\]
Hence
\[
\boxed{\lambda=-\frac{\delta}{I}.}
\]
Step 19 uses this convention consistently: its negative \(\delta\) gives positive fitted \(\lambda\). The docstring and
```python
lam_pred = delta/Iinf
```
in `exterior_null_line.py` have the wrong sign. The tabulated positive agreement is obtained only after reversing that script output’s sign.

There is also an omitted logarithm in the asymptotic statement for \(\theta\). If
\[
w=A_\infty-2\lambda\log x+o(1),
\]
then
\[
k(x)\theta(x)=-\frac12\int_x^\infty f_-^2(s)w(s)\,ds,
\]
and therefore
\[
\boxed{
\theta(x)=
\frac{\lambda}{2}\frac{\log x}{x^2}
+\frac{\lambda-A_\infty}{4x^2}
+o(x^{-2}).
}
\]
Thus the far field is \(x^{-2}\log x\), not purely \(x^{-2}\). In an ACH defining coordinate with \(x\sim\rho^{-2}\), this is a \(\rho^4\log\rho\) term.

The interpretation of \(\lambda\) as a conserved costate is exact for the quadratic CH exterior problem. For the nonlinear numerical cells it is a fitted linearized charge; the stated \(1\)–\(2\%\) exterior agreement quantifies the approximation.

---

## 5. Compatibility of small scalar defect, nonzero \(\lambda\), and nonexistence

These statements are compatible but have different logical strengths.

### Small \(J_6-P\) and nonzero \(\lambda\)

In the antisymmetric CH linearization,
\[
\delta s=0
\]
identically. Therefore the off-null response can carry trace-free Ricci energy and a nonzero charge \(\lambda\) without producing scalar defect at quadratic order. The \(X=512\) record indeed has
\[
\frac{J_6-P}{8\pi^2}\simeq3.35\times10^{-8},
\qquad |\lambda|\simeq0.18.
\]
There is no contradiction.

The supplied values support that the scalar channel decreases rapidly from \(X=128\) to \(512\), but two collar lengths do not prove a limiting rate or even by themselves prove convergence to zero. The linear decomposition makes such decay structurally plausible.

Likewise, persistence of a limiting nonzero charge is not yet numerically established by a single \(X=512\) fit. The Step-19 \(x_0=.03\) comparison and the analytical exterior law support the mechanism, but a sequence \(\lambda_X\) for the same \(x_0=.038\) branch at \(X=128,256,512,\ldots\) is needed to demonstrate convergence.

### No smooth full critical exact-collar cell

This is a rigorous theorem, independent of the numerics. At a smooth full critical point with an exact CH collar,
\[
(\Delta_++6)e=0,\qquad e=s+24.
\]
Because \(e=0\) on the collar, testing by \(e\) gives
\[
\int\left(|\nabla e|^2+6e^2\right)dV=0,
\]
so \(e=0\) throughout. The remaining tensor Euler equation and unique continuation imply
\[
\operatorname{Ric}+6g=0
\]
throughout the cell. Gluing to the CH exterior would produce a globally locally complex-hyperbolic manifold, incompatible with the \(O(-1)\) blowup topology.

This theorem does not conflict with the numerical cells because:

1. they are stationary, at most, in a finite radial spectral family;
2. the supplied conformal runs are not stationary for full \(J_6\);
3. their endpoint matching is finite-order rather than an exact smooth CH germ;
4. in the infinite-collar interpretation, a nonzero \(\lambda\)-tail persists arbitrarily far out, so there is no open CH set from which the exact-collar unique-continuation argument begins.

The theorem is a nonattainment result. It does not imply \(J_6/(8\pi^2)\ge1\), and it does not exclude a degenerating subthreshold sequence or a critical point of a different infinite-ended variational problem.

---

## 6. Strongest supported conclusion

The supplied evidence supports the following statement:

- There is a robust finite-dimensional diagonal \(O(-1)\)-bolt construction with independently evaluated
  \[
  \boxed{\frac{J_6}{8\pi^2}=0.995178186608}
  \]
  at \(x_0=.038,\ X=512\).
- Its scalar defect is only about \(3.35\times10^{-8}\).
- Its exterior is accurately modeled by the explicit off-null antisymmetric quadratic response, with fitted charge of magnitude about \(0.18\).
- Twelve-mode radial conformal scalar adjustment changes the total objective only at the \(10^{-9}\) level at \(X=512\), but those scalar-only runs are not tests of full Euler stationarity.
- The infinite-collar value near \(0.995166\)–\(0.99517\) remains an uncertified numerical extrapolation.
- No smooth unrestricted critical cell with an exact CH collar can exist on this topology.

It is therefore justified to say that the observed branch has a rapidly diminishing scalar channel while its trace-free exterior charge remains substantial. It is not yet justified to claim a proved limit \(J_6-P\to0\), a proved limiting \(\lambda\ne0\), or a smooth critical exact-collar realization.

---

## 7. Most consequential finite-interface computation

The dominant next computation is a transparent-boundary optimization on a fixed core \([x_0,\rho]\), preferably at several values such as \(\rho=5,10,20\):
\[
j_{\rm FI}
=
j_{\rm core}
+\frac{\delta^2}{I(\rho)}
+Q_{+,\mathrm{sc}}(\text{symmetric and scalar interface data}),
\]
where
\[
\delta=-2k(\rho)\Theta-w_0G(\rho),\qquad
\lambda=-\frac{\delta}{I(\rho)}.
\]
For the antisymmetric penalty,
\[
\frac{\partial E_{\rm ext}}{\partial w_0}
=2G(\rho)\lambda,\qquad
\frac{\partial E_{\rm ext}}{\partial\Theta}
=4k(\rho)\lambda.
\]
These are the terminal costates that must match the core boundary momenta.

The optimization should jointly vary:

- core shape coefficients;
- full-\(J_6\) conformal coefficients;
- physical bolt area;
- free interface trace data.

It should report:

1. \(j_\infty\) and its stability under changing \(\rho\);
2. \(\lambda\) and its stability under changing \(\rho\);
3. the full projected conformal identities
   \[
   \partial_{c_k}j_{\rm FI}
   =
   \int_{x_0}^{\rho}q_k(\Delta_++6)e\,W\,dt
   +\partial_{c_k}E_{\rm ext};
   \]
4. agreement between autodiff terminal gradients and the explicit costates above.

At \(\rho\approx10\), the supplied data indicate that the antisymmetric penalty captures essentially the whole exterior cost. To move the interface inward toward \(\rho=5\), one should also derive and include the symmetric \(U(2)\) and scalar transparent penalties, taking account of the Calabi Einstein null line. This finite-interface computation removes the finite-\(X\) \((\log X)^2/X^2\) truncation, directly tests costate matching, and determines whether the subthreshold value survives the presently missing variational directions.