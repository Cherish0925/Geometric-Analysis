# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/scripts/step80_regularized_model_fast.py",
    "Sessions/S1003A01/workspace/scripts/step80_zero_models.py",
    "Sessions/S1003A01/workspace/data/step80/regularized_model_fast.json",
    "Sessions/S1003A01/workspace/data/step80/zero_model_regularization.json",
    "Sessions/S1003A01/workspace/data/step59/chiral_exact.json"
  ]
}
```

## Task

Independently verify the mathematics in the new Step-80 note. Focus on: (i) signs and integration by parts in the regularized scalar identity (80.R) from the displayed Δq equation; (ii) signs in the equally regularized Kodaira identity (80.K); (iii) the local distributional limits for q=c rho^{2m} at an isolated four-dimensional zero versus a smooth codimension-two stratum, including constants 4π²m R² and 4πm; (iv) the exact Bianchi-VIII rational formulas and asymptotic/scaling interpretation, including whether the indefinite ∂v term really cancels half of 24|eta|² at leading order; (v) any overstatement in the conclusions about what uniform estimate remains. Return corrected formulas and a direct scientific assessment. Do not rely on numerical output as proof beyond its scope.

## Output

# Scientific verification memo

## 1. Regularized scalar identity

Let
\[
a=\frac{3|s|}{2},\qquad b=\frac94,\qquad
\Delta q=-D+aq-bq^2,
\]
with \(\Delta=\operatorname{div}\nabla\). Since \(q+\varepsilon>0\),
\[
0=\int_M\Delta\log(q+\varepsilon)
 =\int_M\left(
 \frac{\Delta q}{q+\varepsilon}
 -\frac{|dq|^2}{(q+\varepsilon)^2}\right).
\]
Substitution gives
\[
0=\int_M\left[
-\frac{D}{q+\varepsilon}
+a\frac{q}{q+\varepsilon}
-b\frac{q^2}{q+\varepsilon}
-\frac{|dq|^2}{(q+\varepsilon)^2}\right],
\]
and therefore
\[
\boxed{
\int_M\left[
\frac{|dq|^2}{(q+\varepsilon)^2}
+\frac{D}{q+\varepsilon}
+\frac94\frac{q^2}{q+\varepsilon}\right]
=\frac{3|s|}{2}\int_M\frac{q}{q+\varepsilon}.}
\]
Thus every sign in (80.R) is correct.

Equivalently,
\[
\int_M\frac{\Delta q}{q+\varepsilon}
=-\int_M\left\langle dq,d\frac1{q+\varepsilon}\right\rangle
=\int_M\frac{|dq|^2}{(q+\varepsilon)^2},
\]
which provides an independent sign verification.

## 2. Weighted Kodaira identity

Given \(F_f=\operatorname{div}j_f\), put \(h=(q+\varepsilon)^{-1}\). Then
\[
0=\int_M\operatorname{div}(h j_f)
 =\int_M\left(
 \frac{F_f}{q+\varepsilon}
 -\frac{\langle dq,j_f\rangle}{(q+\varepsilon)^2}\right).
\]
Hence
\[
\boxed{
\int_M\frac{F_f}{q+\varepsilon}
=\int_M\frac{\langle dq,j_f\rangle}{(q+\varepsilon)^2}.}
\]
The plus sign on the right of (80.K) is correct. Dropping this term after weighting by \((q+\varepsilon)^{-1}\) changes the identity.

This verification uses the displayed convention \(F_f=\operatorname{div}j_f\). It is also consistent with the form calculation in Step 79 if the three-form defining \(j_f\) is identified by \(\iota_{j_f}dV=\operatorname{Re}(i\bar fDf\wedge\omega)\).

## 3. Local zero models

### 3.1 Isolated zero in \(\mathbb R^4\)

For \(q=cr^{2m}\),
\[
\partial_r\log(q+\varepsilon)
=\frac{2mc\,r^{2m-1}}{cr^{2m}+\varepsilon}.
\]
Since \(|S^3_R|=2\pi^2R^3\),
\[
\int_{B_R}\Delta\log(q+\varepsilon)
=2\pi^2R^3\partial_r\log(q+\varepsilon)\big|_{R}
=\boxed{\frac{4\pi^2mcR^{2m+2}}{cR^{2m}+\varepsilon}}.
\]
Thus
\[
\lim_{\varepsilon\downarrow0}\int_{B_R}\Delta\log(q+\varepsilon)
=4\pi^2mR^2,
\qquad
\lim_{R\downarrow0}4\pi^2mR^2=0.
\]
There is no point-supported mass. Distributionally,
\[
\Delta\log(cr^{2m})=\frac{4m}{r^2}
\]
in four dimensions.

The two separate regularized integrals satisfy
\[
\lim_{\varepsilon\downarrow0}
\int_{B_R}\frac{|dq|^2}{(q+\varepsilon)^2}
=4\pi^2m^2R^2,
\]
\[
\lim_{\varepsilon\downarrow0}
\int_{B_R}\frac{\Delta q}{q+\varepsilon}
=4\pi^2m(m+1)R^2.
\]
Their difference is \(4\pi^2mR^2\), exactly the flux above.

Also,
\[
\frac1q\in L^1_{\rm loc}(\mathbb R^4)
\iff \int_0 r^{3-2m}\,dr<\infty
\iff m=1
\]
for integral \(m\ge1\). By contrast,
\[
|d\log q|^2=\frac{4m^2}{r^2}
\]
is locally integrable in four dimensions for every fixed \(m\). Thus the Step-79 pair of hypotheses breaks at \(m\ge2\) specifically through \(1/q\).

### 3.2 Smooth codimension-two stratum

Per unit area along the stratum, let \(C=cR^{2m}\). Direct integration in the normal two-plane gives
\[
\int_{\rho<R}\frac{|dq|^2}{(q+\varepsilon)^2}
=4\pi m\left[
\log\left(1+\frac C\varepsilon\right)
-\frac{C}{C+\varepsilon}\right],
\]
and
\[
\int_{\rho<R}\frac{\Delta q}{q+\varepsilon}
=4\pi m\log\left(1+\frac C\varepsilon\right).
\]
Their difference is
\[
\boxed{\frac{4\pi m C}{C+\varepsilon}\longrightarrow4\pi m}.
\]
Consequently,
\[
\boxed{
\Delta\log q
=(\Delta\log q)_{\rm reg}+4\pi m\,\delta_\Sigma}
\]
along a smooth stratum \(\Sigma\), with the analyst Laplacian and the stated normal form. Both separate integrals diverge logarithmically:
\[
\int\frac{|dq|^2}{(q+\varepsilon)^2}
=4\pi m\log(1/\varepsilon)+O(1),
\]
and \(1/q\notin L^1_{\rm loc}\).

For \(q=c(y)\rho^{2m}(1+O(\rho))\), with corresponding derivative control, the coefficient remains \(4\pi m\); \(c(y)\), the tubular metric, and the lower-order factors contribute only the regular part. In a formal unregularized scalar identity, the surface term enters with plus sign on the side containing
\[
|d\log q|^2+\frac Dq+\frac94q.
\]
Since the separate terms generally diverge, this is properly formulated through the common regularization or through a renormalized distribution.

## 4. Exact Bianchi–VIII algebra

Set
\[
A=1-p^2,\qquad H=1+3p^2,\qquad L=9p^2-1.
\]
The displayed formulas become
\[
q=\frac{36A^3}{H^3},\qquad
|\eta|^2=\frac{18A^3L}{H^4},\qquad
\operatorname{tr}V^2=\frac{81A^4L^2}{2H^6}.
\]
Writing
\[
P=297p^6-243p^4+227p^2-25,
\]
\[
Q=135p^6+63p^4-79p^2+9,
\]
the Step-80 expressions are
\[
D=\frac{108A^3P}{H^6},
\]
\[
32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=-\frac{216A^3Q}{H^6}.
\]
These formulas are algebraically compatible because
\[
P=4LH^2-3AL^2-2Q.
\]
Indeed,
\[
24|\eta|^2-8\operatorname{tr}V^2
+32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=\frac{108A^3}{H^6}
\left(4LH^2-3AL^2-2Q\right)=D.
\]

Using the script’s radial metric data,
\[
\Delta q
=\frac1{\mathrm{vol}\sqrt G}
\frac d{dp}\left(\frac{\mathrm{vol}}{\sqrt G}q'\right),
\]
direct differentiation reproduces
\[
D=-\Delta q+18q-\frac94q^2
=\frac{108A^3P}{H^6}.
\]
Thus the rational scalar formulas are exact consequences of \(q,G,\mathrm{vol}\).

### End asymptotics

For \(t=1-p\),
\[
q=\frac92t^3+O(t^4),\qquad
dV=\left(\frac{16\sqrt2}{3}t^{-3}+O(t^{-2})\right)dt,
\]
\[
|dq|^2=\frac{729}{2}t^6+O(t^7),
\]
\[
|\eta|^2=\frac92t^3+O(t^4),\qquad
D=54t^3+O(t^4),
\]
and
\[
32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=-54t^3+O(t^4).
\]
Therefore
\[
24|\eta|^2=108t^3+O(t^4),
\]
while the \(\partial v\) coupling contributes \(-54t^3+O(t^4)\). It cancels exactly one half of the leading \(24|\eta|^2\) term. The \(V\)-term begins at order \(t^4\). The scalar equation then gives
\[
\Delta q=27t^3+O(t^4),
\]
consistent with direct radial differentiation.

The transition scale follows from \(\frac92t^3\asymp\varepsilon\):
\[
t\asymp\left(\frac{2\varepsilon}{9}\right)^{1/3}.
\]
The dominant integrated scalar terms scale as \(\varepsilon^{-2/3}\); the \(V\)-term scales as \(\varepsilon^{-1/3}\), and the \(q^2/(q+\varepsilon)\) integral has a finite limit.

For the regularized logarithmic flux,
\[
\Phi_\varepsilon(t)
=\left|\frac{\mathrm{vol}}{\sqrt G}
\frac{q'}{q+\varepsilon}\right|
\sim\frac{144\sqrt2\,t}{\varepsilon+\frac92t^3}.
\]
Its maximum occurs at
\[
t_{\rm peak}=\left(\frac{\varepsilon}{9}\right)^{1/3},
\]
and
\[
\Phi_{\rm peak}
\sim\frac{96\sqrt2}{9^{1/3}}\varepsilon^{-2/3}.
\]
Under the script’s parametrization
\[
1-p=\frac43e^{-u}-\frac23e^{-2u},
\]
this yields
\[
\boxed{
u_{\rm peak}
=\frac13\log(1/\varepsilon)
+\log\frac43+\frac13\log9+o(1)}
\]
with constant
\[
\log\frac43+\frac13\log9=1.020090\ldots .
\]
Thus the fitted \(0.99+o(1)\) should be replaced by the exact asymptotic constant \(1.020090\ldots\). For fixed \(\varepsilon\),
\[
\Phi_\varepsilon(t)\sim \frac{144\sqrt2}{\varepsilon}t\longrightarrow0,
\]
so the end flux statement is correct.

### Orbit-volume normalization

The `vol` used in `step80_regularized_model_fast.py` gives
\[
\int q\,dV=64\sqrt2,
\]
and hence
\[
\lim_{\varepsilon\downarrow0}
\frac94\int\frac{q^2}{q+\varepsilon}\,dV
=144\sqrt2=203.646752\ldots ,
\]
exactly as seen in the JSON file. Step 79 uses the convention \(\int q=64\). To compare absolute integral values with Step 79, every Step-80 model integral and level flux must therefore be divided by \(\sqrt2\). Ratios, signs, and inverse-power exponents are unchanged.

## 5. Inconsistency with the quoted Step-79 frame samples

The new script does not evaluate
\(\operatorname{Im}\langle\alpha,K\partial_Dv\rangle\) from frame components. It computes \(D\) from \(\Delta q\) and defines the coupling by subtraction:
\[
\texttt{cr}=D-24|\eta|^2+8\operatorname{tr}V^2.
\]
Accordingly, the numerical JSON cannot independently establish the identification of this scalar residual with the geometric inner product.

There is also a direct inconsistency with the Step-79 parenthetical samples. At \(p=\tfrac12\), formula (80.2) gives
\[
32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=\frac{1755432}{117649}=14.9209\ldots,
\]
so
\[
\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=0.46628\ldots,
\]
whereas Step 79 records approximately \(1.0689\). Formula (80.2) is also \(<0\) sufficiently near \(p=1\), while the Step-79 sample at \(p=0.9\) records a value \(>0\).

Thus the half-cancellation is rigorously established for the scalar residual forced by \(q,G,\mathrm{vol},|\eta|^2,\operatorname{tr}V^2\). Its identification with the frame expression under the stated \(K\), \(\alpha\), and \(Dv\) conventions still contains a textual or convention inconsistency in the supplied artifacts. A symbolic pointwise evaluation of those frame components is the concrete mathematical object that resolves the discrepancy.

## 6. Strength of the concluding interpretation

Two refinements are important.

1. A finite uniform bound on each of the three displayed transport terms is not the uniquely necessary form of new information. Codimension-two strata already produce logarithmic divergences in separate pieces, while (80.R) forces cancellation in their combined sum. Mathematically viable inputs include:
   - an \(\varepsilon\)-independent signed inequality for the combined expression;
   - subtraction of the explicit \(4\pi m[\Sigma]\) residue;
   - convergence as signed measures;
   - a global cohomological formula for the weighted current.

   For example, an inequality of the strength
   \[
   \int\left[
   \frac{|dq|^2}{(q+\varepsilon)^2}
   +\frac D{q+\varepsilon}\right]
   \ge \frac{3|s|}{2}\int\frac q{q+\varepsilon}
   \]
   would combine with (80.R) to force
   \(\int q^2/(q+\varepsilon)=0\). A mere absolute bound on the transport terms would not provide this sign and strength.

2. Equation (80.K) directly measures the component of the Kodaira current along \(dq\), hence radial transport relative to the amplitude \(|\alpha|\). It does not by itself involve the direction \(\alpha/|\alpha|\). Moreover, \(\alpha\) is a section of a complex rank-two bundle; around a normal circle the unit vector lies in an \(S^3\) fiber, whose fundamental group is trivial. An integer phase winding requires an additional complex-line factorization or trivialization. The residue \(4\pi m\) follows from the vanishing order of \(q\), not automatically from a winding of \(\hat\alpha\).

Overall, (80.R), (80.K), and the two model-zero constants are correct. The Bianchi–VIII scalar asymptotics and the one-half leading cancellation are algebraically correct, with the corrected peak-location constant and the \(\sqrt2\) normalization adjustment. The remaining substantive inconsistency is the identification of the inferred scalar coupling with the Step-79 frame inner product under the same conventions.