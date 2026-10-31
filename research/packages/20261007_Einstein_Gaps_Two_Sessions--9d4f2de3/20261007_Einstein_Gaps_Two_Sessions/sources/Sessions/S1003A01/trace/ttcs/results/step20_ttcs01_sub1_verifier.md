# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md",
    "Sessions/S1003A01/workspace/scripts/perp_conformal_lm.py",
    "Sessions/S1003A01/workspace/scripts/conformal_stationarity_check.py",
    "Sessions/S1003A01/workspace/scripts/perp_lm.py",
    "Sessions/S1003A01/workspace/scripts/exterior_null_line.py",
    "Sessions/S1003A01/workspace/data/perp_tail/area/lm_x00.038_X128_d24.json",
    "Sessions/S1003A01/workspace/data/perp_tail/area/lm_x00.038_X512_d28.json",
    "Sessions/S1003A01/workspace/data/perp_conformal/scalar_solve_x00.038_X128_d24_p12.json",
    "Sessions/S1003A01/workspace/data/perp_conformal/scalar_solve_x00.038_X512_d28_p12.json",
    "Sessions/S1003A01/workspace/data/perp_tail/independent_x00.038_X512_d28.json",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Read the Step-19 core–exterior result, the inherited exact conformal stationarity argument, and the new Step-20 radial-conformal scripts/results. Check the mathematics and scientific interpretation. In particular: (i) does g -> e^{2phi}g implemented as G->e^{-2phi}G, h->e^{2phi}h preserve the O(-1) bolt geometry and exact CH endpoint contact? (ii) Are the component residual sums and scalar-solve experiments meaningfully testing the Euler equation, given the fixed spectral ansatz and exact cG[0] redundancy? (iii) Is the conclusion justified that J-P tends rapidly to zero while the nonzero trace-free tail charge lambda can remain, but no smooth full critical exact-collar cell can exist? Identify any formula/sign/normalization or optimization flaw, and state the strongest supported mathematical conclusion and the most consequential next finite-interface computation.

## Output

# Scientific verification memo

## 1. Radial conformal transformation

For
\[
g=\frac{dx^{2}}{4G(x)}+h_{ij}(x)\sigma_i\sigma_j,
\]
the replacement
\[
G\longmapsto \widetilde G=e^{-2\phi}G,\qquad
h\longmapsto \widetilde h=e^{2\phi}h
\]
gives exactly
\[
\widetilde g
=\frac{dx^{2}}{4e^{-2\phi}G}+e^{2\phi}h
=e^{2\phi}g.
\]
Thus `ConformalCell.prof_factory` implements the intended conformal change without a sign or radial-factor error.

### O\((-1)\) bolt

Write \(y=x-x_0\), and suppose the collapsing coefficient and radial coefficient have expansions
\[
F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),
\qquad f_1g_1=1.
\]
Since \(u=\log(x/x_0)/\ell\) is smooth in \(y\), the implemented \(\phi\) has
\[
\phi=\phi_0+\phi_1y+O(y^2),
\]
which is an even smooth function of the true radial coordinate because \(y\sim t^2\). Moreover,
\[
\widetilde F'=e^{2\phi_0}F',\qquad
\widetilde G'=e^{-2\phi_0}G',
\]
at the bolt, so
\[
\widetilde F'(x_0)\widetilde G'(x_0)=F'(x_0)G'(x_0)=1.
\]
The cone angle, circle period, and O\((-1)\) normal topology are therefore unchanged.

The induced bolt metric is rescaled by \(e^{2\phi_0}\). Consequently, after adding conformal coefficients, \(x_0\) is no longer literally the physical bolt-area parameter: the latter is proportional to
\[
x_0e^{2\phi(x_0)}.
\]
For the supplied scalar solves this correction is tiny:
\[
\phi(x_0)\simeq-3.12\times10^{-5}\quad(X=128),\qquad
\phi(x_0)\simeq-8.96\times10^{-6}\quad(X=512),
\]
but it matters when locating an optimum in \(x_0\).

### CH endpoint contact

Because
\[
\phi(u)=(1-u)^3p(u),
\]
one has
\[
\phi(X)=\phi_x(X)=\phi_{xx}(X)=0.
\]
Thus the conformal deformation preserves the metric 2-jet at \(x=X\), including curvature values there, provided the base profile already has the corresponding CH contact.

This is finite-order endpoint contact, not an exact CH germ. Extending \(\phi\) by zero for \(x\ge X\) is generally only \(C^2\), since \(\phi_{xxx}(X)\) need not vanish. If the base metric was CH on an open outer collar, this polynomial conformal factor destroys that property except at \(X\). A smooth exact-collar version requires a conformal factor that is identically zero on a subcollar or flat to all orders at the joining interface. Since \(\phi=O((X-x)^3)\), flattening it in a shrinking layer changes the curvature energy by a quantity tending to zero; hence the numerical metric can still be converted into smooth exact-collar competitors with asymptotically the same \(J_6\), but the stored spectral profile itself is not such a metric.

---

## 2. Residual normalization and numerical objective

The residual construction in `perp_lm.py` is correctly normalized. With \(W=a_1a_2a_3\), \(e=s+24\), and \(dt=dx/(2\sqrt G)\),
\[
\sum_q |R_q|^2
\approx
\int W\,dt\left(\frac{|z|^2}{4}+\frac{e^2}{16}\right)
=\frac{J_6}{8\pi^2}.
\]
Likewise,
\[
P/(8\pi^2)=\sum R_{1:3}^2,\qquad
(J_6-P)/(8\pi^2)=\sum R_4^2.
\]
Therefore `component_costs` in `perp_conformal_lm.py` is the appropriate positive-square evaluation of the two channels.

There is, however, a reporting inconsistency in the ordinary LM records. At \(x_0=.038,X=512\),
\[
\begin{aligned}
\text{stored `J'}&=0.995181162362,\\
\text{`J_resid'}&=0.995178186591,\\
\text{independent Cartan evaluation}&=0.995178186608.
\end{aligned}
\]
The positive residual and independent calculation agree to about \(2\times10^{-11}\), while the stored `DualCell.costs` value differs by \(2.98\times10^{-6}\). At \(X=128\) the analogous discrepancy is \(3.96\times10^{-7}\). Thus the scientifically relevant Step-19 values are the residual/independent ones, not the `P,J` fields produced by `c.costs`. In particular, the strongest supplied floating value for the \(X=512\) ordinary cell is
\[
\boxed{J_6/(8\pi^2)=0.995178186608}
\]
before the very small conformal scalar adjustment.

### Exact redundant coordinate

The coordinate `cG[0]` is identically absent from the physical profile. Leaving it in `perp_lm.py` explains the enormous stored coefficients such as \(5.46\times10^4\) and \(-1.12\times10^9\); these numbers do not represent large geometry. They produce a zero Jacobian column and a zero Hessian eigenvalue. Removing this coordinate in `perp_conformal_lm.py` is mathematically correct and improves numerical conditioning. It does not alter the represented metric.

The old local-minimum statement therefore refers only to the fixed-gauge spectral family modulo this exact null coordinate. It does not include all radial conformal directions, variation of the physical bolt area, or arbitrary compactly supported tensor variations.

---

## 3. What the scalar-solve experiments test

For
\[
J_6(g)=\int |\operatorname{Ric}+6g|^2\,dV,
\]
the conformal variation \(\dot g=2fg\) is
\[
\delta J_6
=4\int f\,(\Delta_++6)(s+24)\,dV,
\qquad \Delta_+=-\operatorname{div}\nabla.
\]
Thus the full conformal Euler expression is
\[
L e:=-(e_{tt}+(W_t/W)e_t)+6e,\qquad e=s+24.
\]
The sign and the coefficient \(6\) in `conformal_stationarity_check.py` are correct.

For the normalized numerical objective \(j=J_6/(8\pi^2)\), a basis function
\[
q_k(x)=\frac{\partial\phi}{\partial c_k}
\]
must satisfy the exact directional identity
\[
\boxed{
\frac{\partial j}{\partial c_k}
=\int q_k\,L e\,W\,dt
=\int q_k\,L e\,\frac{W}{2\sqrt G}\,dx .
}
\]
This provides a direct comparison between autodiff gradients and the independently evaluated Euler expression.

The supplied `--scalar-solve` records do something different: they minimize only
\[
\frac1{16}\int W e^2\,dt.
\]
Its Euler equation under conformal changes is not \(Le=0\); the cancellation with the conformal variation of \(P\) is essential in deriving \(Le\). Accordingly:

- `grad_inf_optimized` near \(10^{-13}\) or \(10^{-10}\) measures stationarity of the scalar channel alone.
- The full conformal gradients remain
  \[
  3.51\times10^{-5}\quad(X=128),\qquad
  2.57\times10^{-5}\quad(X=512),
  \]
  and the full shape gradients are \(1.40\times10^{-3}\) and \(4.06\times10^{-4}\), respectively.
- These scalar-solve outputs are not stationary points of \(J_6\), even inside the enlarged finite spectral family.

The experiments are nevertheless informative: they show that the scalar channel can be reduced with extremely small conformal factors while changing \(P\) very little. Numerically,
\[
\begin{array}{c|c|c}
X&J_6-P\text{ before}&J_6-P\text{ after scalar solve}\\ \hline
128&3.4646\times10^{-7}&3.2969\times10^{-7}\\
512&3.3489\times10^{-8}&3.2418\times10^{-8}.
\end{array}
\]
The total reductions in \(J_6/(8\pi^2)\) are only
\[
2.11\times10^{-8}\quad\text{and}\quad1.34\times10^{-9}.
\]
No supplied run yet measures the result of a full-\(J_6\) `--phi-only` or default joint optimization.

The `--joint-outer` implementation also ends each cycle with a scalar-only conformal solve. Since that last substep does not minimize the same full objective, its final output need not be stationary for \(J_6\), nor need \(J_6\) decrease in every such scalar substep.

### Normalization defect in `conformal_stationarity_check.py`

With the stated one-form normalization,
\[
\int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi^2,
\]
the physical volume density in the \(x\)-coordinate is
\[
dV=\frac{\pi^2W}{\sqrt G}\,dx.
\]
The script uses
\[
\texttt{dv}=\frac{\pi^2W}{2\sqrt G},
\]
which is smaller by a factor of two. Therefore its field
`scalar_energy_over_8pi2` is one half of the scalar residual energy used by `perp_lm.py`. The weighted RMS ratios and pointwise suprema are unaffected by this common factor.

Because \(Le\) contains four derivatives of the metric profiles, degree and quadrature convergence are especially important for this test. A fixed twelve-dimensional Chebyshev family only tests twelve moments of \(Le\), not the pointwise equation.

---

## 4. Exterior charge and sign convention

Let
\[
\delta=-2k(\rho)\Theta-w_0G(\rho),\qquad
I(\rho)=\int_\rho^\infty\frac{G^2}{\mu}\,dx.
\]
For
\[
E=\int_\rho^\infty\mu(w')^2dx
\]
with the moment constraint, the minimizer satisfies
\[
\mu w'=-\lambda G,\qquad
w=w_0-\lambda L(x,\rho).
\]
Since
\[
\delta=\int f_-^2(w-w_0)\,dx=-\lambda I,
\]
the correct relation is
\[
\boxed{\lambda=-\frac{\delta}{I}.}
\]
Step 19 uses this sign consistently with its table: the reported \(\delta<0\) gives \(\lambda>0\). In `exterior_null_line.py`, both the docstring and
```python
lam_pred = delta/Iinf
```
have the opposite sign. The finite-interval linear system itself uses a convention that approaches \(-\delta/I\).

There is also a logarithm in the asymptotic \(\theta\). If
\[
w=A_\infty-2\lambda\log x+o(1),
\]
then the torsion relation gives
\[
k(x)\theta(x)=-\frac12\int_x^\infty f_-^2w\,ds,
\]
hence
\[
\boxed{
\theta(x)=
\frac{\lambda}{2}\frac{\log x}{x^2}
+\frac{\lambda-A_\infty}{4x^2}
+o(x^{-2}).
}
\]
Thus the description \(\theta\sim x^{-2}\) suppresses an essential logarithm. In an ACH defining coordinate with \(x\sim\rho^{-2}\), this is a \(\rho^4\log\rho\) term.

The interpretation of \(\lambda\) as a conserved costate is exact for the quadratic CH exterior problem. For the full nonlinear cell it is a fitted linear exterior charge, with the supplied \(1\)–\(2\%\) agreement quantifying the nonlinear remainder near the computed branch.

---

## 5. Small scalar channel, persistent trace-free tail, and nonexistence of a smooth full critical cell

These three facts are compatible.

1. In the antisymmetric CH linearization, \(\delta s=0\) identically.
2. The off-null response with \(\lambda\ne0\) contributes to the trace-free Ricci energy \(P\), while contributing nothing to \(J_6-P\) at quadratic order.
3. The \(X=512\) record simultaneously has
   \[
   (J_6-P)/(8\pi^2)\simeq3.35\times10^{-8}
   \]
   and fitted \(\lambda\simeq0.183\).

Thus a nonzero trace-free tail charge does not force a comparable scalar channel. The data support rapid decrease of the computed scalar channel between \(X=128\) and \(512\), but they do not by themselves establish a limiting rate or an exact scalar-flat limit.

The inherited nonexistence theorem transfers exactly to the current normalization. If \(\widehat g=6g\), then
\[
\operatorname{Ric}(\widehat g)=-\widehat g,\qquad
J_1(\widehat g)=J_6(g).
\]
For a smooth full critical metric that is exactly CH on a nonempty outer collar, conformal stationarity gives
\[
(\Delta_++6)e=0,\qquad e=s+24.
\]
Since \(e=0\) on the CH collar, testing with \(e\) yields
\[
\int\bigl(|\nabla e|^2+6e^2\bigr)=0,
\]
so \(e=0\) everywhere. The remaining tensor Euler equation and unique continuation force
\[
\operatorname{Ric}+6g=0
\]
throughout the cell. Gluing back the CH exterior would produce a global locally complex-hyperbolic metric, incompatible with the O\((-1)\) blowup topology.

There is no contradiction with the numerical cells:

- They are stationary only in a finite radial spectral family.
- The supplied scalar solves are not stationary for full \(J_6\).
- Their stored endpoint contact is finite order rather than an exact smooth CH germ.
- In the \(X\to\infty\) picture, the \(\lambda\)-tail remains nonzero arbitrarily far out, so there is no open CH region from which unique continuation could begin.

## Strongest supported mathematical conclusion

The supplied calculations establish a robust finite-dimensional subthreshold construction with
\[
J_6/(8\pi^2)\approx0.99517819
\]
at \(x_0=.038,X=512\), a far field accurately described by the explicit off-null antisymmetric response with \(|\lambda|\approx0.18\), and a scalar channel of order \(3\times10^{-8}\). Radial conformal scalar adjustment changes the value only at the \(10^{-9}\) level in the \(X=512\) record. The infinite-collar value near \(0.99517\) remains a numerical extrapolation. No supplied result establishes a smooth unrestricted critical metric, and the exact-collar theorem rules out such a metric on this topology.

## Most consequential finite-interface computation

The natural compact objective at \(\rho\simeq10\) is
\[
j_{\mathrm{FI}}
=
j_{\mathrm{core}}[x_0,\rho]
+\frac{\delta^2}{I(\rho)}
+Q_{+,\mathrm{sc}}(\text{interface trace}),
\qquad
\delta=-2k(\rho)\Theta-w_0G(\rho),
\]
where \(Q_{+,\mathrm{sc}}\) is the symmetric/scalar exterior response. The antisymmetric terminal derivatives are explicit:
\[
\frac{\partial E_{\rm ext}}{\partial w_0}=2G(\rho)\lambda,\qquad
\frac{\partial E_{\rm ext}}{\partial\Theta}=4k(\rho)\lambda,
\qquad
\lambda=-\delta/I.
\]
A full-\(J_6\) optimization of this finite-interface functional over the core shape, radial conformal coefficients, physical bolt area, and interface trace would simultaneously:

- remove finite-\(X\) truncation from the dominant tail channel;
- test the full projected conformal Euler equation rather than the scalar residual alone;
- enforce the correct costate matching through \(\lambda\);
- determine whether the \(0.99517\) value survives the missing conformal and interface directions.

The independent identity
\[
\partial_{c_k}j_{\mathrm{FI}}
=
\int_{x_0}^{\rho}q_kLe\,W\,dt
+\partial_{c_k}E_{\rm ext}
\]
would then provide a direct scientific verification of the autodiff gradient and the transparent terminal term.