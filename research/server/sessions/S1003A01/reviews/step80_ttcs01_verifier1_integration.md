# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 80,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step80_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step80_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematics in the new Step-80 note. Focus on: (i) signs and integration by parts in the regularized scalar identity (80.R) from the displayed Δq equation; (ii) signs in the equally regularized Kodaira identity (80.K); (iii) the local distributional limits for q=c rho^{2m} at an isolated four-dimensional zero versus a smooth codimension-two stratum, including constants 4π²m R² and 4πm; (iv) the exact Bianchi-VIII rational formulas and asymptotic/scaling interpretation, including whether the indefinite ∂v term really cancels half of 24|eta|² at leading order; (v) any overstatement in the conclusions about what uniform estimate remains. Return corrected formulas and a direct scientific assessment. Do not rely on numerical output as proof beyond its scope.

## Integrated Scientific Memo

## Verification result

**The signs in (80.R) and (80.K), and the local constants \(4\pi^2mR^2\) and \(4\pi m\), are correct.** The Bianchi–VIII rational formulas are mutually consistent and follow exactly from the supplied radial scalar data. Their inferred coupling cancels half of \(24|\eta|^2\) at leading order.

Necessary corrections are:

- the peak-location constant is \(1.020090\ldots\), not \(0.99+o(1)\);
- the sweep residuals are predominantly **omitted boundary flux at \(u=32\)**, not numerical cancellation error;
- Step 80’s model measure differs from Step 79’s integral normalization by \(\sqrt2\);
- the geometric coupling samples quoted in Step 79 contradict (80.2);
- the statements about isolated-zero integrability, zero curves, normalized-torsion winding, and the uniquely necessary “uniform estimate” require qualification.

### 1. Regularized scalar and Kodaira identities

Write
\[
a=\frac{3|s|}{2},\qquad b=\frac94,\qquad
\Delta q=-D+aq-bq^2,
\]
using \(\Delta=\operatorname{div}\nabla\). On a closed manifold,
\[
0=\int_M\Delta\log(q+\varepsilon)
=\int_M\left[
\frac{-D+aq-bq^2}{q+\varepsilon}
-\frac{|dq|^2}{(q+\varepsilon)^2}\right].
\]
Consequently,
\[
\boxed{\int_M\left[
\frac{|dq|^2}{(q+\varepsilon)^2}
+\frac D{q+\varepsilon}
+\frac94\frac{q^2}{q+\varepsilon}\right]
=\frac{3|s|}{2}\int_M\frac q{q+\varepsilon}.}
\]
Equivalently, integration by parts gives the useful sign check
\[
\int_M\frac{\Delta q}{q+\varepsilon}
=-\int_M\left\langle dq,d(q+\varepsilon)^{-1}\right\rangle
=\int_M\frac{|dq|^2}{(q+\varepsilon)^2}.
\]
Thus **(80.R) is valid without assumptions on \(Z\)**.

For \(F_f=\operatorname{div}j_f\),
\[
\operatorname{div}\!\left(\frac{j_f}{q+\varepsilon}\right)
=\frac{F_f}{q+\varepsilon}
-\frac{\langle dq,j_f\rangle}{(q+\varepsilon)^2},
\]
so
\[
\boxed{\int_M\frac{F_f}{q+\varepsilon}
=\int_M\frac{\langle dq,j_f\rangle}{(q+\varepsilon)^2}.}
\]
The sign in **(80.K) is also correct**.

The underlying Kodaira signs agree with Step 79 provided the current is defined unambiguously by
\[
\iota_{j_f}dV=\operatorname{Re}(i\bar f Df\wedge\omega).
\]
Indeed,
\[
d\,\operatorname{Re}(i\bar fDf\wedge\omega)
=\left(|\bar\partial_Df|^2-|\partial_Df|^2
-k\langle db,\omega\rangle |f|^2\right)dV,
\]
and
\[
\langle db,\omega\rangle=\frac{|s|}{2}-\frac q4.
\]
This yields the displayed coefficients for weights \(k=2\) and \(k=1\). No positivity follows for the weighted transport term.

### 2. Local distributional limits

#### Isolated radial zero in four dimensions

For \(q=cr^{2m}\), \(c>0\),
\[
\int_{B_R}\Delta\log(q+\varepsilon)
=2\pi^2R^3\,\frac{2mcR^{2m-1}}{cR^{2m}+\varepsilon}
=\boxed{\frac{4\pi^2mcR^{2m+2}}{cR^{2m}+\varepsilon}}.
\]
Its limit is \(4\pi^2mR^2\), which vanishes as \(R\downarrow0\). More explicitly,
\[
\boxed{\Delta\log(cr^{2m})=\frac{4m}{r^2}}
\]
distributionally in \(\mathbb R^4\), with **no point mass**.

The separate terms in this radial model are uniformly integrable and converge for every fixed \(m\):
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
Their difference is exactly the limiting flux.

Thus Step 80 should distinguish:

- \(1/q\in L^1_{\rm loc}\) iff \(m=1\), for integer \(m\ge1\);
- \(|d\log q|^2\in L^1_{\rm loc}\) for **every** \(m\);
- failure of \(1/q\in L^1\) does not imply failure of the combined scalar identity.

If the displayed scalar equation holds, then
\[
\frac Dq=-\frac{\Delta q}{q}+a-bq.
\]
For this radial model \(D/q\) remains locally integrable even when \(1/q\) does not. The Step-79 hypotheses are therefore sufficient, not necessary.

These conclusions concern the specified normal form. An arbitrary anisotropic isolated analytic zero requires its own integrability analysis; the radial calculations do not establish absolute integrability of its separate terms.

#### Smooth codimension-two stratum

Per unit tangential area, let \(C=cR^{2m}\). Exact normal-plane integration gives
\[
\int_{\rho<R}\frac{\Delta q}{q+\varepsilon}
=4\pi m\log\left(1+\frac C\varepsilon\right),
\]
\[
\int_{\rho<R}\frac{|dq|^2}{(q+\varepsilon)^2}
=4\pi m\left[
\log\left(1+\frac C\varepsilon\right)-\frac C{C+\varepsilon}\right].
\]
Hence
\[
\boxed{\int_{\rho<R}\Delta\log(q+\varepsilon)
=\frac{4\pi mC}{C+\varepsilon}\longrightarrow4\pi m.}
\]
For the controlled tubular normal form
\[
q=c(y)\rho^{2m}(1+O(\rho)),
\]
with corresponding derivative control,
\[
\boxed{\Delta\log q=(\Delta\log q)_{\rm off\;Z}
+4\pi m\,\delta_\Sigma.}
\]
Here \(\delta_\Sigma\) denotes **surface measure**, not a cohomological divisor class. Both separate normal-plane integrals diverge logarithmically; \(1/q\) also fails local integrability.

If the off-stratum combined expression is integrable, and these smooth strata account for all singular contributions, the resulting unregularized identity has the sign
\[
\boxed{
\int_{M\setminus Z}
\left[|d\log q|^2+\frac Dq+\frac94q\right]
=\frac{3|s|}{2}V
+4\pi\sum_i m_i\,\operatorname{Area}(\Sigma_i).}
\]
The positive surface term is absent from the limit of the *regularized integral* because the regularized combined density develops the compensating negative concentration. Passing to the limit separately would lose it.

#### Zero curves

If “zero curve” means a real one-dimensional stratum, its normal dimension is three. For the analogous radial normal form,
\[
\int_{\rho<R}\Delta\log q
=2m|S^2|R=8\pi mR\longrightarrow0.
\]
Such a curve carries no logarithmic residue. Therefore Step 80’s blanket withdrawal of “zero curves have no residue” is inappropriate under that meaning of *curve*. Its withdrawal of the unsupported assertion “the zero set has codimension at least three” is appropriate. A complex curve, being real two-dimensional, does carry the codimension-two residue.

The leading polynomial at a degenerate point does not determine the actual zero-set dimension. Neither the radial formulas nor a lowest homogeneous degree alone justify a general anisotropic residue or integrability theorem.

### 3. Exact Bianchi–VIII scalar verification

Set
\[
A=1-p^2,\qquad H=1+3p^2,\qquad L=9p^2-1.
\]
The supplied formulas are
\[
q=\frac{36A^3}{H^3},\quad
|\eta|^2=\frac{18A^3L}{H^4},\quad
\operatorname{tr}V^2=\frac{81A^4L^2}{2H^6},
\]
\[
G=\frac{4H}{A^2L},\qquad
\mathrm{vol}=\frac{32pH}{3A^2}.
\]
In particular,
\[
q'=-\frac{864pA^2}{H^4}.
\]
Direct differentiation of
\[
\Delta q=
\frac1{\mathrm{vol}\sqrt G}
\frac d{dp}\left(\frac{\mathrm{vol}}{\sqrt G}q'\right)
\]
gives
\[
\boxed{\Delta q=
\frac{432A^3(1-23p^2+81p^4-27p^6)}{H^6}.}
\]
Therefore
\[
-\Delta q+18q-\frac94q^2
=\boxed{\frac{108A^3P}{H^6}},
\qquad
P=297p^6-243p^4+227p^2-25.
\]
This is exactly Step 80’s \(D\).

Writing
\[
Q=135p^6+63p^4-79p^2+9,
\]
the inferred coupling is
\[
\boxed{C_{\partial v}:=D-24|\eta|^2+8\operatorname{tr}V^2
=-\frac{216A^3Q}{H^6}.}
\]
The polynomial identity verifying the decomposition is
\[
P=4LH^2-3AL^2-2Q.
\]
These are exact algebraic checks, independent of quadrature.

**Important geometric qualification.** The fast script computes \(C_{\partial v}\) by this subtraction; it does not independently evaluate \(32\operatorname{Im}\langle\alpha,K\partial_Dv\rangle\). Its identification with that geometric expression is conditional on the supplied torsion equation—and the Step-79 frame samples are inconsistent with it.

For example, at \(p=1/2\), (80.2) gives
\[
C_{\partial v}=\frac{1755432}{117649}=14.9209\ldots,
\qquad
\operatorname{Im}\langle\alpha,K\partial_Dv\rangle
=0.46628\ldots,
\]
whereas Step 79 quotes \(1.0689\). Near \(p=1\), (80.2) is negative, while Step 79 quotes a positive value at \(p=0.9\). These cannot be simultaneous checks under identical conventions.

Thus the scalar residual and its half-cancellation are verified exactly. **An independent symbolic evaluation of the frame coupling is still needed to resolve whether Step 79’s samples, conventions, or general torsion equation contain the error.**

### 4. End asymptotics, scaling, and sweep corrections

For \(t=1-p\downarrow0\), in the script’s measure,
\[
q=\frac92t^3+O(t^4),\qquad
dV=\left(\frac{16\sqrt2}{3}t^{-3}+O(t^{-2})\right)|dt|,
\]
\[
|dq|^2=\frac{729}{2}t^6+O(t^7),\qquad
|\eta|^2=\frac92t^3+O(t^4),
\]
\[
D=54t^3+O(t^4),\qquad
C_{\partial v}=-54t^3+O(t^4),\qquad
\operatorname{tr}V^2=\frac{81}{8}t^4+O(t^5).
\]
Hence
\[
24|\eta|^2=108t^3+O(t^4),
\]
and the inferred coupling cancels **exactly half** of this leading term.

This also repairs Step 79’s end-density statement:
\[
|d\log q|^2\to18,\qquad
\frac{24|\eta|^2}{q}\to24,\qquad
\frac{C_{\partial v}}q\to-12,\qquad
\frac{-8\operatorname{tr}V^2}{q}\to0.
\]
Thus \(\Delta\log q\to-12=s\), and \(B\to30=5|s|/2\). The statement that \(24|\eta|^2/q\to12\) and all other terms decay is false.

The transition scale is
\[
t\asymp(2\varepsilon/9)^{1/3}.
\]
An exact leading-order integral calculation yields
\[
R_\varepsilon:=18\int\frac q{q+\varepsilon}\,dV
\sim C_R\varepsilon^{-2/3},
\qquad
C_R=64\pi\sqrt{\frac23}\left(\frac92\right)^{2/3}.
\]
The gradient, \(D\), eta, and coupling integrals have respective leading ratios
\[
\boxed{\frac13,\quad\frac23,\quad\frac43,\quad-\frac23}
\]
to \(R_\varepsilon\). The \(V\)-term is lower order, \(O(\varepsilon^{-1/3})\), and the \(q^2/(q+\varepsilon)\) integral has a finite limit.

The absolute logarithmic flux is
\[
\Phi_\varepsilon(t)\sim
\frac{144\sqrt2\,t}{\varepsilon+\frac92t^3}.
\]
Its maximum occurs at
\[
t_{\rm peak}=(\varepsilon/9)^{1/3},
\qquad
\Phi_{\rm peak}\sim
\frac{96\sqrt2}{9^{1/3}}\varepsilon^{-2/3}.
\]
Since
\[
t=\frac43e^{-u}-\frac23e^{-2u},
\]
the corrected peak location is
\[
\boxed{
u_{\rm peak}=\frac13\log(1/\varepsilon)
+\log\frac43+\frac13\log9+o(1)
=\frac13\log(1/\varepsilon)+1.020090\ldots+o(1).}
\]
The reported node-grid fit does not establish a different asymptotic constant.

For every fixed \(\varepsilon>0\), the end flux vanishes. At the finite cutoff \(U=32\), however,
\[
\Phi_\varepsilon(U)\sim
\frac{192\sqrt2\,e^{-32}}{\varepsilon}
=\frac{3.438688\ldots\times10^{-12}}{\varepsilon}.
\]
This matches the JSON residuals across the sweep. On the truncated domain,
\[
\boxed{\mathrm{LHS}-\mathrm{RHS}
=-\Phi^{\rm signed}_\varepsilon(U)
=\Phi_\varepsilon(U),}
\]
the bolt flux being zero. The large residuals therefore primarily represent **the omitted boundary/tail**, not cancellation error. Boundary correction is necessary before interpreting them as quadrature errors.

Finally, the normalization mismatch can be checked exactly:
\[
q\,dV
=\frac{768p}{H^{3/2}\sqrt L}\,dp
=64\,d\sqrt{\frac LH}.
\]
Thus
\[
\int q\,dV=64\sqrt2,
\qquad
\lim_{\varepsilon\downarrow0}\frac94\int\frac{q^2}{q+\varepsilon}\,dV
=144\sqrt2.
\]
To compare with Step 79’s \(Q=64\), divide Step 80’s integrals and level fluxes by \(\sqrt2\).

### 5. What remains scientifically unresolved

The note overstates the necessity and interpretation of the proposed uniform transport estimate.

On any closed candidate, (80.R) already gives an exact uniform bound on the **signed scalar combination**
\[
S_\varepsilon:=
\int_M\left[
\frac{|dq|^2}{(q+\varepsilon)^2}+\frac D{q+\varepsilon}\right]
=a\int_M\frac q{q+\varepsilon}
-b\int_M\frac{q^2}{q+\varepsilon}.
\]
In particular,
\[
-b\int_Mq\le S_\varepsilon\le aV.
\]
For a nontrivial analytic \(q\), whose zero set has volume zero,
\[
S_\varepsilon\longrightarrow aV-b\int_Mq.
\]
Separate pieces can nevertheless diverge, especially at surface strata. **The missing input is not mere boundedness; it is a new global signed/coercive relation strong enough to contradict this balance.** It could involve weighted Kodaira transport, residue subtraction, or another genuinely compact geometric input. The displayed identities do not show that the three listed transport quantities are the unique remaining route.

The complete model demonstrates that fixed-\(\varepsilon\) identities and local estimates compatible with its integrability cannot alone distinguish compactness. Its moving layer is at infinity, where \(q>0\), not at a torsion zero. It does not prove that every pointwise Young estimate has nonuniform constants or that closed-zero behavior is exhausted by the smooth surface models.

Also, (80.K) directly measures current transport along \(dq\); interpreting it through \(\hat\alpha\) requires additional structure. Locally \(\alpha\) is a complex rank-two bundle section, so its unit vector takes values in \(S^3\), with \(\pi_1(S^3)=0\). There is no automatic integer normal winding. A phase winding would require a justified complex-line reduction. The \(4\pi m\) residue follows from amplitude vanishing order, not from such a winding.

One useful conditional consequence of the scalar equation is available at every torsion zero:
\[
\alpha=0,\qquad
\Delta q=8\operatorname{tr}V^2-24|\eta|^2\ge0,
\]
hence
\[
\boxed{\operatorname{tr}V^2\ge3|\eta|^2\quad\text{on }Z.}
\]
This is strict when \(\Delta q>0\), including nondegenerate zeros. It supplies genuine zero-set information, but not the needed global contradiction.

**Direct assessment:** Step 80 successfully establishes the regularized integration framework and the two stated radial residue calculations. Its scalar model algebra and asymptotic half-cancellation are correct. It does not independently verify the geometric coupling, resolve general anisotropic zero limits or weighted Kodaira residues, or establish a coercive compact inequality. The immediate exact discrepancy is the Step-79 frame coupling versus (80.2); resolving that discrepancy is necessary before treating the half-cancellation as an independently checked geometric fact.