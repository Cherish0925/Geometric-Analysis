# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 85,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step85_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step85_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check, line by line, the mathematics of the Step-85 note on closed negative Goldberg near Kahler-Einstein (KE) metrics and A1 orbifolds. Focus on: (1) Proposition 85.1 (exact identity |a omega + beta|^2 = 2a^2+|beta|^2 for beta in Re H^{2,0}; constant |theta| forces K trivial; orbifold validity; quadratic estimate). (2) Theorem 85.A: does Nagy's Theorem 1.6 normal form apply to formal second-order Einstein jets; correctness of the pointwise algebra A1-A5 in the script (conventions g^{-1}g_t = 1 + tH1 + t^2/2 H2, Hodge star, ASD projection); the holomorphic-transport construction of beta' (J' = J H1, g_s = omega(., J_s .), first-order integrability from dbar H1 = 0, ddbar-lemma step, why <omega,beta'>=0 pointwise); whether admissible length corrections compatible with the other second-order equations are exactly the constants; any missing second-order term. (3) Theorem 85.B: indicial classification of closed self-dual forms on flat R^4 minus 0 (degrees >=0 and <=-4; -2,-3 empty; no logs), Gamma-parity; neck argument that the constant mode drifts only by the integrated metric error; whether the metric-error hypothesis is plausibly supplied by Ozuch's weighted closeness; Liouville statements; uniform L^infty bound; b+(M)=b+(V). (4) 85.D: at a KE point R^+ = (s/4) I(x)I, Biquard/Ozuch first obstruction forces the EH period direction into I-perp; is the conclusion (bubble's parallel form orthogonal to zeta, smoothing rather than resolution, vanishing cycle asymptotically Lagrangian) correct? EH potential expansion and anti-self-duality of i ddbar(1/r^2). (5) T_+(M)=T_+(V) for EH with W+=0 and D(g)=(S_hat^2(g)-S_hat^2(V))/16. (6) Conditional Theorem 85.M: is hypothesis (b) correctly scaled, does the mean-value argument work, is the Kahler smoothing locus of codimension one. Give corrections with explicit formulas and state which statements are fully proved, which need repair, and any counterexample.

## Integrated Scientific Memo

# Verification memo: Step 85

The exact length obstruction and the second-order coupled calculation survive verification. The main repairs concern the neck statement, the normalization of the Eguchi–Hanson tail, and the reduced obstruction in 85.M. The supplied Nagy paper supports the formal-jet argument; the Ozuch and Biquard texts themselves are not present, so their quoted consequences must remain identified as inputs.

## 1. Proposition 85.1: proved, including compact orbifolds

With complex orientation and the stated form norm,
\[
\Lambda_g^+=\mathbb R\omega\oplus\operatorname{Re}\Lambda^{2,0},
\qquad |\omega|^2=2.
\]
Thus
\[
|a\omega+\beta|^2=2a^2+|\beta|^2
\]
is an exact pointwise identity. For the usual complexified form norm,
\[
|\operatorname{Re}\theta|^2=\tfrac12|\theta|^2.
\]

If \(|\theta|\) is a positive constant, the holomorphic section \(\theta\) has no zeros and trivializes the canonical bundle. The orbifold statement is equally valid: a nowhere-zero **orbifold** section trivializes the orbifold line bundle. But
\[
c_1^{\mathrm{orb}}(V)=\frac{E}{2\pi}[\omega]\ne0,
\]
because pairing with \([\omega]\) gives \(E\int_V\omega^2/(2\pi)\ne0\). This contradicts canonical triviality.

There is also a local verification. Wherever \(\theta\ne0\),
\[
i\partial\bar\partial\log|\theta|^2=\rho=E\omega.
\]
Consequently a nonzero holomorphic canonical section cannot have constant norm even on an open set when \(E\ne0\).

The quadratic estimate follows exactly as written:
\[
c_V=\min_{\|\beta\|_{L^2}=1}
 \bigl\||\beta|^2-\fint_V|\beta|^2\bigr\|_{L^2}>0.
\]
Homogeneity gives
\[
\|Q_0(\beta)\|_{L^2}\ge c_V\|\beta\|_{L^2}^2.
\]
If \(H^{2,0}=0\), the estimate is vacuous and any positive constant works.

At an \(A_1\) point, \((-1)^*(dz_1\wedge dz_2)=dz_1\wedge dz_2\); nonvanishing there is allowed. No assumption \(p_g=0\) is needed.

**Boundary counterexample.** At \(E=0\), a flat complex torus or hyperkähler K3 has nonzero constant-length elements of \(\operatorname{Re}H^{2,0}\). Thus the nonzero-Ricci assumption cannot simply be dropped.

Lemma 85.0 is correct. The definition of \(\lambda(g)\) needs \(b^+>0\); when \(b^+=0\), its constraint set is empty.

---

## 2. Theorem 85.A: correct after specifying Einstein jets and volume normalization

The precise statement should be:

> A first-order coupled pair
> \[
> H_1\in\mathscr E(V,g),\qquad
> \beta_1\in\operatorname{Re}H^{2,0}(V)
> \]
> extends to a second-order Einstein, closed, self-dual, constant-length jet if and only if \(\beta_1=0\).

Calling the initial object a “formal second-order AKE jet” is circular: such an object already solves the second-order equations.

### 2.1 Nagy’s normal form does apply to formal second-order jets

Although Theorem 1.6 is stated for actual Einstein families, its supplied proof uses only:

* first- and second-order Einstein equations;
* second-order volume and diffeomorphism normalization;
* elliptic inversion and complex-type decomposition.

In particular, Theorems 3.9 and 4.21 yield, for formal jets,
\[
H_1\in\mathscr E(V,g),\qquad H_2^+=H_1^2,
\]
and
\[
H_2^-=\mathbf h_2-\tfrac12\mathcal L_{J\operatorname{grad}f}J,
\]
where
\[
\Delta_E\mathbf h_2=-2\delta[H_1,H_1]^c,\qquad
(\Delta-2E)f=-\tfrac12\operatorname{tr}(H_1^2).
\]
The anti-\(J\) component is **not arbitrary**: it satisfies this inhomogeneous equation and is determined modulo \(\mathscr E\).

One omitted step is the volume normalization. For a fixed-\(E\) Einstein jet,
\[
\operatorname{Ric}_{g_t}-Eg_t=O(t^3),
\]
consider
\[
\mathcal A_E(g)=\int_V(s_g-2E)\,d\mu_g.
\]
In dimension four its Euler–Lagrange tensor vanishes at \(\operatorname{Ric}=Eg\). Hence
\[
\frac d{dt}\mathcal A_E(g_t)=O(t^3),\qquad
\mathcal A_E(g_t)=2E\,\operatorname{Vol}(g_t)+O(t^3).
\]
Therefore
\[
\operatorname{Vol}(g_t)=\operatorname{Vol}(g)+O(t^3).
\]
Formal Moser normalization makes the volume form fixed through order two, as required by Nagy. It does not introduce an admissible homothetic Einstein correction.

The jet should satisfy the actual Einstein equation. If the displayed gauge-fixed \(F\) is retained, its Bianchi gauge must be defined and the implication from gauge-fixed solutions to Einstein jets justified. In the usual negative-Einstein Bianchi slice this follows from the invertible gauge operator \(\Delta-2E\), order by order. It is not a consequence of diffeomorphism covariance of the gauge-fixed expression itself.

Nagy proves the result for manifolds. On compact orbifolds, invariant local tensor identities, orbifold elliptic/Hodge theory, formal Moser normalization, and the same negative-\(E\) inversions give the extension. This is an adaptation of the proof, not literally a cited orbifold theorem.

### 2.2 A1–A5: correct algebra, with one qualification to A5

The script’s norm, orientation, Hodge star and
\[
P^-=\tfrac12(1-*)
\]
are consistent. For a symmetric endomorphism \(H\), let
\[
(H\sharp F)(X,Y)=F(HX,Y)+F(X,HY).
\]
The universal variation formulas are
\[
D* [H]F=*\bigl(\tfrac12\operatorname{tr}H\,F-H\sharp F\bigr),
\]
\[
DP^-[H]F=-\tfrac12*
 \bigl(\tfrac12\operatorname{tr}H\,F-H\sharp F\bigr).
\]
They verify:

* **A1:** \(D_g|\omega|^2[H]=-\operatorname{tr}H\).
* **A2:** \(D_g\langle\omega,b\rangle[H]=0\) for every symmetric \(H\) and \(b\in\operatorname{Re}\Lambda^{2,0}\). The anticommuting skew endomorphisms associated with \(\omega,b\) have skew product.
* **A3:** \(DP^-[H]\omega=0\) for anti-\(J\) \(H\) and for conformal \(H\). The map on primitive \(J\)-invariant symmetric tensors is nonzero and injective.
* **A4:** \(DP^-[H]b\) is generally nonzero for anti-\(J\) \(H\).

For **A5**, a universal proof replaces the script’s single rational sample. Put
\[
A(t)=1+tH_1+\tfrac12t^2H_2,\qquad
K=H_2^+-H_1^2.
\]
When \(H_1J=-JH_1\),
\[
(A(t)^{-1}J)^2=-1+t^2K+O(t^3).
\]
Equivalently, \(g\,e^{tH_1}\) is exactly compatible with the fixed \(\omega\), and an additional anti-\(J\) second-order tensor preserves compatibility through order two. Thus \(K=0\) implies
\[
P^-_{g_t}\omega=O(t^3),\qquad
|\omega|_{g_t}^2=2+O(t^3).
\]

More explicitly,
\[
[P^-_{g_t}\omega]_{t^2}=\tfrac12DP^-[K]\omega,\qquad
[|\omega|_{g_t}^2]_{t^2}=-\tfrac12\operatorname{tr}K.
\]
Accordingly, “a \(J\)-invariant change of \(H_2\) destroys the first property” is too broad. A scalar change preserves self-duality, by conformal invariance, but destroys the length condition. A nonzero primitive \(J\)-invariant change destroys self-duality.

### 2.3 Holomorphic transport: valid to first order

With \(\omega(X,Y)=g(JX,Y)\),
\[
J'=JH_1,\qquad J_s=J+sJ',\qquad
\omega(\,\cdot\,,J_s\,\cdot\,)=g+s\,gH_1.
\]
These are compatible Hermitian data **to first order**, not an exact complex/Hermitian family for nonzero \(s\).

Nagy’s Remark 4.9 identifies the linearized integrability equation with \(\bar\partial H_1=0\). Indeed its parametrization
\[
J_h=(1-h)^{-1}J(1-h)
\]
has derivative \(-2Jh\); take \(h=-H_1/2\).

Let \(\phi\) be the corresponding Beltrami differential. With a consistent sign convention, first-order type preservation prescribes
\[
(\theta')^{1,1}=\iota_\phi\theta,\qquad
(\theta')^{0,2}=0.
\]
Since \(\bar\partial\phi=0\) and \(\theta\) is holomorphic,
\[
\bar\partial(\iota_\phi\theta)=0.
\]
The \((2,1)\)-form \(\partial(\iota_\phi\theta)\) is \(\partial\)-exact and \(\bar\partial\)-closed. The compact Kähler \(\partial\bar\partial\)-lemma gives a \((1,0)\)-form \(\xi\) with
\[
\partial(\iota_\phi\theta)=\partial\bar\partial\xi.
\]
Choosing \((\theta')^{2,0}=\partial\xi\) gives
\[
d(\theta+s\theta')=O(s^2).
\]
The same argument works in orbifold forms.

For \(\beta_s=\operatorname{Re}(\theta+s\theta')\),
\[
d\beta'=0,\qquad
(\beta')^-=-DP^-[H_1]\beta_1.
\]
Pointwise orthogonality is also genuine:
\[
0=\left.\frac d{ds}\right|_0
 \langle\omega,\beta_s\rangle_{g_s}
=\langle\omega,\beta'\rangle+
 D_g\langle\omega,\beta_1\rangle[H_1].
\]
A2 kills the last term, so
\[
\boxed{\langle\omega,\beta'\rangle\equiv0.}
\]
No actual integrable complex deformation is required.

### 2.4 All second-order terms and admissible corrections

The full self-duality coefficient is
\[
\tfrac12P^-\beta_2+
DP^-[H_1]\beta_1+
\tfrac12\bigl(DP^-[H_2]+D^2P^-[H_1,H_1]\bigr)\omega.
\]
The last term vanishes in Nagy normal form. Hence
\[
d\beta_2=0,\qquad
\beta_2^-=-2DP^-[H_1]\beta_1.
\]
Every solution is
\[
\beta_2=2\beta'+\gamma,\qquad \gamma\in H_g^+.
\]
Writing \(\gamma=c\omega+\eta\), \(\eta\in\operatorname{Re}H^{2,0}\), gives
\[
\langle\omega,\beta_2\rangle=2c.
\]
These corrections are exactly all constants. Metric-kernel additions are anti-\(J\) and trace-free; simultaneous gauge contributes \(\mathcal L_X|\omega|^2=0\); fixed \(E\) excludes scaling.

The complete norm coefficient is
\[
[|\omega|_{g_t}^2]_{t^2}
+2D_g\langle\omega,\beta_1\rangle[H_1]
+|\beta_1|^2+\langle\omega,\beta_2\rangle.
\]
The first two terms vanish. Therefore the obstruction, using the **\(t^2\)-coefficient convention**, is
\[
\boxed{\operatorname{Ob}_2=Q_0(\beta_1).}
\]
Using second derivatives instead would multiply it by \(2\). No second-order term is missing.

The higher-order comments do not follow from this theorem: it excludes tangent form rotation, not every higher-order rotation or a uniformly controlled expansion at a degenerating orbifold.

---

## 3. Theorem 85.B: correct under explicit neck hypotheses, but not literally on fixed-end necks

### 3.1 Flat indicial classification and parity

Write
\[
\alpha=\sum_{i=1}^3 f_i\omega_i
\]
in a parallel self-dual frame. Closedness and self-duality imply harmonicity, so each coefficient has scalar harmonic expansion
\[
r^\ell Y_\ell,\qquad r^{-\ell-2}Y_\ell,\qquad \ell\ge0.
\]
There are no logarithms: the roots \(\ell,-\ell-2\) never coincide.

For coefficient homogeneity \(d=-2\), one has \(\alpha=r^{-2}F\) with constant SD \(F\). Closedness forces
\[
dr\wedge F=0,
\]
and hence \(F=0\).

A useful all-degree argument uses inversion composed with an orthogonal reflection. This is orientation-preserving and conformal, so it preserves closed SD two-forms and transforms coefficient degree
\[
d\longmapsto-d-4.
\]
It maps degree \(-3\) to degree \(-1\), which is absent from scalar harmonic expansions. Thus degree \(-3\) is empty. Nonzero forms in every degree \(d\ge0\) are supplied by
\[
\operatorname{Re}(z_1^d\,dz_1\wedge dz_2);
\]
conformal inversion supplies every degree \(d\le-4\). Therefore the claimed all-degree set is proved:
\[
\boxed{d\ge0\quad\text{or}\quad d\le-4.}
\]

The script correctly verifies the listed finite-dimensional kernels, but its finite loop alone does not prove the all-degree statement.

For the specified \(SU(2)\) action, \(\Lambda^+\) is fixed. A nontrivial element has no fixed vectors in the standard real representation, so invariant degree-one coefficients vanish. If \(-1\in\Gamma\), all odd degrees vanish. For \(A_1\),
\[
\boxed{\{\ldots,-6,-4\}\cup\{0,2,4,\ldots\}.}
\]

### 3.2 A rigorous replacement for the constant-mode argument

“Nonconstant modes have sphere average zero” does not by itself justify projection of the perturbed first-order equation. An exact flux supplies the missing argument.

Let \(X=x^a\partial_a\), and define
\[
\vartheta_i=r^{-4}\iota_X\omega_i.
\]
Then
\[
d\vartheta_i
=2r^{-4}\omega_i-4r^{-6}X^\flat\wedge\iota_X\omega_i
\]
is flat-ASD. For a closed form \(\alpha\), define
\[
F_i(r)=\int_{S_r/\Gamma}\alpha\wedge\vartheta_i.
\]
Stokes’ theorem gives
\[
F_i(r_2)-F_i(r_1)
=\int_{A(r_1,r_2)/\Gamma}\alpha^{-,0}\wedge d\vartheta_i.
\]
If \(g=g_0+e\) and \(\alpha\) is \(g\)-SD, then
\[
|\alpha^{-,0}|_{g_0}\le C|e|\,|\alpha|_{g_0}.
\]
For flat-SD \(\alpha=\sum f_j\omega_j\), \(F_i\) is the sphere average of \(f_i\), multiplied by \(\operatorname{Vol}(S^3/\Gamma)\). Thus, for the corresponding coefficient \(c_i(r)\),
\[
\boxed{
|c_i(r_2)-c_i(r_1)|
\le C\|\alpha\|_\infty
\left(
\int_{r_1}^{r_2}\sup_{S_r}|e|\,\frac{dr}{r}
+\sup_{S_{r_1}\cup S_{r_2}}|e|
\right).}
\]
This proves that drift is controlled by integrated metric error. It needs only \(C^0\) metric error for the flux estimate; local elliptic compactness needs the derivative control already included in (H).

### 3.3 Neck truncation is essential

Let \(a_n\) be the bubble length scale. The common-trace assertion must use
\[
A(a_nR_n,\rho_n),\qquad
R_n\to\infty,\quad \rho_n\to0,\quad a_nR_n<\rho_n.
\]
For the naive model error,
\[
|e_{\rm model}|\lesssim r^2+a_n^4r^{-4},
\]
one obtains
\[
\int_{a_nR_n}^{\rho_n}|e_{\rm model}|\,\frac{dr}{r}
\lesssim \rho_n^2+R_n^{-4}\to0.
\]

**Literal counterexample to the fixed-end formulation.** If the outer neck radius is fixed, an orbifold harmonic form with a nonzero Taylor term differs there from its value at \(p\) by a fixed amount. In an \(A_1\)-invariant normal chart the first possible term is typically quadratic. Hence “one constant plus \(o(1)\) uniformly on the entire neck” is false without moving endpoints.

### 3.4 Liouville, uniform bounds and trace matching

Under (H), including its global hyperkähler frame and the indicated topological filling:

* A bounded harmonic SD form on the bubble has bounded harmonic scalar coefficients in the parallel triple. Complete Ricci-flat Liouville implies those coefficients are constant.
* A bounded closed SD form on the entire punctured flat cone is constant, by the two-sided indicial classification.

The flux estimate allows a noncircular proof of the uniform \(L^\infty\) bound. Suppose
\[
\|\alpha_n\|_\infty=1,\qquad \|\alpha_n\|_{L^2}\to0.
\]
An exterior maximum contradicts smooth local convergence to zero. A bubble maximum gives a nonzero parallel bubble limit; a neck maximum gives a nonzero constant cone limit. Its nonzero flux propagates outward. Choose first a small fixed \(\rho\) and a large fixed \(R\), so the integrated error is small, then let \(n\to\infty\). The flux on \(S_\rho\) must remain nonzero, whereas exterior \(L^2\)-vanishing forces it to zero. Contradiction.

With this uniform bound established, flux comparison with the exterior limit identifies every neck constant with \(\alpha_V(p)\). Uniformity on moving necks follows by contradiction: any sequence of offending points has \(r_n\to0\), \(r_n/a_n\to\infty\), and its rescaled limit is a constant cone form with precisely that flux. Bubble Liouville identifies the bubble limit with the same trace.

Thus the flux law plus elementary blow-up compactness repairs the proof of (i) and (iii); a separate full long-cylinder mode estimate is not indispensable.

### 3.5 Topology and the Ozuch input

Because \(S^3/\Gamma\) is a real homology sphere, gluing adds the ALE intersection lattice orthogonally. In the matched hyperkähler orientation this lattice is negative definite. Hence
\[
b^+(M)=b^+_{\mathrm{orb}}(V).
\]
Together with uniform bounds, vanishing core volume and removable singularities, this proves convergence of the harmonic SD spaces.

The quoted weighted closeness is **plausibly sufficient**, but cannot be checked against Ozuch’s actual definition from this input. The needed conversion is
\[
|e_{\rm perturb}|+r|\nabla e_{\rm perturb}|
\lesssim \varepsilon_n r_D^\beta,\qquad \beta>0,
\]
or another estimate with vanishing logarithmic integral. A bound involving \(r_D^{-\beta}\) is not sufficient without an additional scale-dependent estimate. The naive model error must also be included, rather than silently absorbed into a globally vanishing error on a fixed neck.

Corollary 85.B′ then follows. More generally, its quadratic estimate holds on any subspaces converging to \(\operatorname{Re}H^{2,0}_{\rm orb}(V)\) in the resulting \(L^4\) sense; actual Kählerness of \(g_n\) is not needed for that formulation.

---

## 4. 85.D: correct asymptotic geometry; repair the tail normalization

With \(\mathcal R^+=W^++s/12\),
\[
W^+I=\frac{s}{6}I,\qquad
W^+|_{I^\perp}=-\frac{s}{12},
\qquad I=\omega_V(p)/\sqrt2.
\]
Therefore
\[
\boxed{\mathcal R^+(p)=\frac{s}{4}I\otimes I,\qquad
\ker\mathcal R^+(p)=I^\perp.}
\]

Taking the quoted first obstruction as an input,
\[
\mathcal R^+(p)\widehat\zeta_n\to0
\]
forces \(\langle I,\widehat\zeta_n\rangle\to0\). The repaired trace theorem identifies the bubble form direction with \(I\). Hence its period direction is orthogonal to \(\zeta\).

For the hyperkähler triple \(\omega_i\),
\[
\int_S\omega_i=C\zeta_i.
\]
Consequently
\[
\boxed{\int_{S_n}\omega_n=o(|\zeta_n|),\qquad
\operatorname{Area}(S_n)\asymp|\zeta_n|.}
\]
In the limiting EH geometry the distinguished sphere is actually Lagrangian for the selected form—not merely zero-period. Relative to the complex structure \(\widehat\zeta\) it is holomorphic; relative to \(I\perp\widehat\zeta\) it is the special-Lagrangian vanishing sphere in the smoothing picture. “Never a resolution” should mean this **limiting, selected complex structure**, not an exact finite-\(n\) statement.

Proposition 85.1 identifies the exterior AK limit as \(\pm\omega_V\) without a holonomy argument. It does **not** alone identify the bubble direction; that still needs the trace theorem.

The potential expansion is correct:
\[
\phi(u)=u-\frac{a^4}{2u}+O(u^{-3}).
\]
But the coefficient of the form tail must match the flat normalization. In the script’s coordinates,
\[
\omega_1^0=\frac i2\partial\bar\partial u
=dx_1\wedge dx_2+dx_3\wedge dx_4,
\]
so the compatible convention is
\[
\boxed{
\omega_1=\frac i2\partial\bar\partial\phi
=\omega_1^0-\frac{a^4}{4}i\partial\bar\partial(r^{-2})
+O(r^{-8}).}
\]
The note’s coefficient \(-a^4/2\) instead uses \(\omega_1=i\partial\bar\partial\phi\), whose flat form is twice this \(\omega_1^0\). These conventions should not be mixed with \(\omega_2+i\omega_3=dz_1\wedge dz_2\).

The substantive tail claim is correct:
\[
\Delta_{\mathbb R^4}r^{-2}=0
\quad\Longrightarrow\quad
i\partial\bar\partial(r^{-2})
\text{ is primitive }(1,1)\text{ and flat-ASD}.
\]
The transverse holomorphic-symplectic forms are tail-free in the standard asymptotic gauge.

---

## 5. Topological charge and action identity: correct with orbifold invariants

Write
\[
T_+=2\chi+3\tau
\]
using orbifold Chern–Weil invariants on \(V\). For Einstein metrics,
\[
4\pi^2T_+
=\int\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu.
\]
An orientation-matched hyperkähler ALE bubble has \(W^+=s=0\), so its relative \(+\)-charge is zero.

For EH explicitly,
\[
\Delta\chi_{\rm orb}=2-\tfrac12=\tfrac32,\qquad
\Delta\tau_{\rm orb}=-1,
\]
and
\[
2\Delta\chi_{\rm orb}+3\Delta\tau_{\rm orb}=0.
\]
Thus \(T_+(M)=T_+(V)\). It is false with ordinary invariants of the underlying singular space: replacing an \(A_1\) point adds \(\Delta\chi=1,\Delta\tau=-1\), changing \(2\chi+3\tau\) by \(-1\).

For the normalization implicit in Step 85,
\[
D(g)=\int\left(\frac{s^2}{24}-|W^+|^2\right)d\mu
=\frac{\widehat S^2(g)}{16}-2\pi^2T_+.
\]
At a KE orbifold,
\[
\widehat S^2(V)=32\pi^2T_+(V),
\]
so
\[
\boxed{D(g)=\frac{\widehat S^2(g)-\widehat S^2(V)}{16}.}
\]

The additional identification \(D=T_{\rm AK}\) relies on Step 83, absent here. The identity above does not imply that every non-Kähler Einstein metric carries an AK form.

---

## 6. Conditional 85.M: normalize the obstruction and strengthen the graph hypothesis

### 6.1 Correct derivative scaling

Distinguish the raw obstruction \(\Lambda_I\) from its angular normalization:
\[
\Lambda_I(\zeta,y)
=A\zeta_I+O(|\zeta|^{1+\delta}),\qquad
A=c_0s/4\ne0,
\]
\[
\lambda_I=\Lambda_I/|\zeta|.
\]
The natural missing \(C^1\) estimate for the raw obstruction is
\[
\boxed{\partial_{\zeta_I}\Lambda_I=A+o(1).}
\]
For the normalized leading term,
\[
\boxed{
\partial_{\zeta_I}\left(A\frac{\zeta_I}{|\zeta|}\right)
=A\frac{|\zeta_\perp|^2}{|\zeta|^3}.}
\]
It equals \(A/|\zeta|+o(1/|\zeta|)\) only in a shrinking conic tube with \(\zeta_I/|\zeta|\to0\). On the pure normal ray its derivative is zero. Thus the note’s hypothesis (b) is not the derivative of its leading angular obstruction on a full neighborhood.

Value errors \(O(|\zeta|^{1+\delta})\) alone give no such derivative control.

### 6.2 Mean-value argument

Assume explicitly that
\[
\mathcal K=\{\zeta_I=\kappa(\zeta_\perp,y)\}
\]
consists of KE critical points and that the raw derivative has a fixed nonzero sign on every normal segment under consideration. Then
\[
\Lambda_I(\zeta,y)
=(\zeta_I-\kappa)
\int_0^1
\partial_{\zeta_I}\Lambda_I
\bigl(\kappa+t(\zeta_I-\kappa),\zeta_\perp,y\bigr)\,dt.
\]
The integral is nonzero; hence any Einstein zero in that tube lies on \(\mathcal K\).

To conclude for **all** GH-close Einstein metrics, one additionally uses the angular first obstruction to place their parameter points in this tube. The factor in the note’s mean-value formula cannot automatically be evaluated at the endpoint \(|\zeta|\).

### 6.3 Codimension one is conditional on the period parametrization

For a single \(A_1\) site, a full smoothing family has two real local parameters versus three real EH period parameters. A graph over \((\zeta_\perp,y)\) therefore has real codimension one.

However, global \(\mathbb Q\)-Gorenstein smoothability and an unobstructed global deformation base do not themselves supply the asserted graph for every pair \((\zeta_\perp,y)\). One needs the appropriate local-to-global smoothing map, period coordinates and compatibility with the \(y\)-directions.

There is also a coordinate correction: the algebraic parameter in
\[
xy=z^2+c
\]
is not generally linear in \(\zeta_\perp\). On a marked period cover,
\[
q\sim\zeta_2+i\zeta_3,\qquad c\sim q^2,
\]
with the Weyl identification \(q\sim-q\). The graph should be formulated on this period cover, or its quotient structure stated.

Failure of smoothability or unobstructedness does not by itself prove that the Kähler locus has higher codimension. It may be singular or absent. Such failure leaves possibilities unresolved; it is not a construction of a strict AKE branch.

---

## Final mathematical status

* **Proved from the supplied material:** Lemma 85.0; Proposition 85.1; the manifold formal-jet version of 85.A after the volume/gauge clarification; the flat indicial classification; the EH potential and ASD-tail mechanism; the orbifold charge/action identity.
* **Repaired under explicit hypotheses:** 85.B and its uniform quadratic corollary, using the flux law and moving necks; 85.C; the asymptotic geometric conclusion of 85.D.
* **Extensions requiring stated analytic machinery:** Nagy/Koiso on compact orbifolds; derivation of (H) from Ozuch’s precise weighted norm; the quoted desingularization obstruction.
* **Still conditional:** 85.M’s scale-uniform normal \(C^1\) estimate and full Kähler-smoothing graph.
* **Not established:** a uniform higher-order slaving statement at the orbifold endpoint, or exclusion/existence of strict closed negative AKE metrics.

In 85.E, the exact inequality also retains factors \(a_n^2\) and \(2|a_n|\) on its two right-hand terms. Since \(a_n\to\pm1\), these can be absorbed into asymptotic constants. Its finite-dimensional coercivity is justified; its asserted higher-order comparison across degeneration requires additional uniform differentiability estimates and does not follow from 85.A alone.