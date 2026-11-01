# TTCS Independent Branch Record

```json
{
  "step_id": 60,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md",
    "Knowledge/objects/papers/Canonical-Metrics-on-3-Manifolds-and-4-Manifolds--8d02c53d4380--0b5d0f7e0ac4/object.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md"
  ]
}
```

## Task

Verify Part B of the Step-59 note (zero-gap structure) with Part C.4. Check: (1) Prop 59.N: the O(lambda^2) estimate for gluing Ricci-flat ALE trees into Einstein orbifolds of any sign (decay rates, curvature on the annulus, tree induction, orientation compatibility). (2) Prop 59.C: alpha <= 36 Vol_{|r|} with LeBrun's normalization, and the claims that MinVol=0 forces chi=tau=0 and that alpha is never attained on S^1xY (Y hyperbolic/spherical), S^2xT^2, Kodaira surfaces. (3) Prop 59.D: the explicit warped-product interpolations: the real-hyperbolic double (curvatures -(f'^2-f''), -f'^2, volume O(e^{-3T})), the complex-hyperbolic Heisenberg-cusp double (is curvature really bounded when base scales e^{-f} and fibre e^{-2f}, including the mixed terms with f', f''?), and the T^3-cusp Dehn filling for every slope (flattening path of flat metrics on T^3 at scale e^{-T}, turnaround, exponential growth of the gamma-circle while the T^2 stays at size e^{-T}, round cap; volume O(e^{-2T})). Also whether the fillings and doubles are smooth closed manifolds with the claimed topology, and whether 'no Einstein warped T^3 x I neck' supports the stated openness for doubles. (4) Theorem 59.Z: whether Anderson's Theorem 4.10 (read the Knowledge object provided; note his case labels and hypotheses) plus lower semicontinuity of P on compact subsets of the regular set really yields the trichotomy (I) Einstein orbifold, (III) finite-volume complete Einstein domain with s<0 and F-structure complement, (II) total collapse, as stated; whether the minimizers of Z_eps = P + eps int (1+|Ric|^2)^p have P -> alpha; the arguments excluding Ricci-flat and positive Omega in (III); what extra hypotheses are silently used (e.g. local minimality, convergence class); and whether 'attainment iff Einstein' is correctly scoped. Return a direct scientific memo with corrected statements.

## Output

## Scientific memo on Step 59 Part B and C.4

### 0. Conventions and relation to Anderson’s functionals

Throughout,  
\[
P(g)=\int_M |\operatorname{Ric}^\circ_g|^2\,d\mu_g
\]
is scale invariant in dimension four. Anderson works on unit-volume metrics; since \(P\) is scale invariant, one may normalize any constructed sequence to volume \(1\) without changing \(P\).

Anderson’s perturbed functional relevant here is, up to the notation of the Step,
\[
Z_\varepsilon^{2p}(g)
=
\int_M\Bigl(|\operatorname{Ric}|^2-\frac14 s^2\Bigr)d\mu
+
\varepsilon\int_M(1+|\operatorname{Ric}|^2)^p d\mu,
\]
and
\[
|\operatorname{Ric}^\circ|^2=|\operatorname{Ric}|^2-\frac14s^2.
\]
Thus \(Z_\varepsilon=P+\varepsilon\int(1+|\operatorname{Ric}|^2)^p\). This is the functional treated in Anderson’s Corollary 4.8 and Theorem 4.10. The relation between \(\mathscr R^2\) and \(P\) is, up to a fixed normalization, topological:
\[
\mathscr R^2 = \text{constant depending on }\chi(M) + c\,P,
\]
so minimizers of \(\mathscr R^2\) and \(P\) are equivalent on a fixed manifold.

---

## 1. Proposition 59.N — gluing Ricci-flat ALE trees into Einstein orbifolds

### 1.1 Local one-point estimate

Let \((V,g_V)\) be a compact Einstein orbifold with an isolated singular point modeled on \(\mathbb R^4/\Gamma\). In orbifold normal coordinates on the regular side,
\[
g_V=\delta+O(r^2),
\]
and because \(g_V\) is Einstein,
\[
\operatorname{Ric}^\circ(g_V)=0.
\]

Let \((N,g_N)\) be a Ricci-flat ALE space asymptotic to the same cone, with end coordinate \(y\). The Bando–Kasue–Nakajima decay gives, in a suitable gauge,
\[
g_N=g_{\text{cone}}+O(|y|^{-4}),
\qquad
\nabla^k g_N=O(|y|^{-4-k}),
\]
so in particular
\[
\operatorname{Rm}(g_N)=O(|y|^{-6}).
\]

Scale the ALE metric by \(\lambda^2\) and introduce the base coordinate \(x=\lambda y\). Then
\[
\lambda^2 g_N
=
\delta+O(\lambda^6 |x|^{-4}),
\]
and
\[
\operatorname{Rm}(\lambda^2 g_N)
=
O(\lambda^4 |x|^{-6}).
\]

Choose the gluing annulus
\[
t\le r\le 2t,
\qquad
t=\lambda^{1/2}.
\]
On this annulus,
\[
\lambda^4 r^{-6}=O(\lambda^4 t^{-6})=O(\lambda),
\]
while the orbifold side differs from \(\delta\) by \(O(t^2)=O(\lambda)\). The two metrics therefore differ by \(O(\lambda)\). A radial cutoff over an interval of length comparable to \(t\) introduces second derivatives of size
\[
O\!\left(\frac{\lambda}{t^2}\right)=O(1).
\]
Hence the interpolated metric has uniformly bounded curvature on the annulus:
\[
|\operatorname{Rm}| \le C,
\qquad
|\operatorname{Ric}^\circ|\le C.
\]

The annular volume is
\[
\operatorname{Vol}(\text{annulus})=O(t^4)=O(\lambda^2).
\]
Therefore
\[
\int_{\text{annulus}}|\operatorname{Ric}^\circ|^2\,d\mu
\le C\lambda^2.
\]

This gives the stated \(O(\lambda^2)\) error for one singular point.

### 1.2 Trees

For an ALE orbifold tree, one repeats the same construction at each singular point of the ALE space. If the top scale is \(\lambda\), choose lower-level scales sufficiently small relative to \(\lambda\). Since the tree is finite, the sum of annular errors can be made arbitrarily small; with a fixed geometric hierarchy it is still \(O(\lambda^2)\) up to a constant depending on the tree.

The induction uses the same estimate at each level:

* the outer orbifold or ALE piece is Einstein or Ricci-flat, hence has \(\operatorname{Ric}^\circ=0\);
* the inner scaled ALE piece is Ricci-flat;
* the error is localized in annuli of volume \(O(t_v^4)\) with bounded curvature.

Thus the total \(P\)-energy tends to zero.

### 1.3 Orientation

The ALE end must match the cone with compatible orientation. If the available ALE space has the opposite orientation, one uses its orientation reversal. Since \(P=\int|\operatorname{Ric}^\circ|^2\) is insensitive to orientation reversal, this does not affect the estimate.

### 1.4 Corrected statement

Proposition 59.N is correct as a sufficient zero-energy construction. More explicitly:

> If \(M\) is obtained from a compact Einstein orbifold \(V\) by replacing each isolated cone point by a finite Ricci-flat ALE orbifold tree with matching end group and compatible orientation, then there exist smooth metrics \(g_j\) on \(M\) with \(P(g_j)\to0\). Hence \(\alpha(M)=0\).

The \(O(\lambda^2)\) estimate rests on the standard ALE decay and the choice \(t=\lambda^{1/2}\). The exact decay rate need only ensure that the scaled ALE curvature remains bounded on the gluing annulus; the Bando–Kasue–Nakajima decay provides this.

---

## 2. Proposition 59.C — total collapse and the \(36\operatorname{Vol}_{|r|}\) estimate

### 2.1 Constant and normalization

Let \(\operatorname{Vol}_{|r|}(M)\) denote an infimum of volumes over metrics satisfying a Ricci bound. The constant \(36\) is correct if the Ricci bound is an operator norm bound
\[
|\operatorname{Ric}|_{\mathrm{op}}\le 3.
\]
Indeed, if \(\lambda_1,\dots,\lambda_4\) are the eigenvalues of the Ricci operator, then \(|\lambda_i|\le3\), and
\[
|\operatorname{Ric}^\circ|^2
=
\sum_{i=1}^4\left(\lambda_i-\frac{s}{4}\right)^2
\le
\sum_{i=1}^4\lambda_i^2
\le
4\cdot 3^2
=
36.
\]
Thus
\[
P(g)\le 36\,\operatorname{Vol}(g).
\]

If instead \(|\operatorname{Ric}|\) denotes the tensor/Frobenius norm and the condition is \(|\operatorname{Ric}|_{\mathrm{Frob}}\le3\), then the constant should be \(9\), not \(36\). The mechanism is unchanged; only the numerical coefficient depends on the norm convention.

For comparison with Gromov’s minimal volume,
\[
\operatorname{MinVol}(M)=\inf\{\operatorname{Vol}(g): |K_g|\le1\},
\]
a metric with \(|K|\le1\) satisfies
\[
|\operatorname{Ric}|_{\mathrm{op}}\le3,
\]
because for a unit vector \(e\),
\[
\operatorname{Ric}(e,e)=\sum_{j\ne i} K(e,e_j),
\]
and there are three sectional terms. Hence the class \(|K|\le1\) is contained in the class \(|\operatorname{Ric}|_{\mathrm{op}}\le3\), and therefore
\[
\operatorname{Vol}_{|r|}(M)\le \operatorname{MinVol}(M).
\]
Consequently,
\[
\alpha(M)\le 36\,\operatorname{Vol}_{|r|}(M)\le 36\,\operatorname{MinVol}(M),
\]
under the operator-norm convention.

### 2.2 \(\operatorname{MinVol}=0\) forces \(\chi=\tau=0\)

Suppose \(g_j\) satisfies \(|K_{g_j}|\le1\) and \(\operatorname{Vol}(g_j)\to0\). The curvature tensors are uniformly bounded. The Chern–Gauss–Bonnet and Hirzebruch signature integrands are polynomial in curvature and hence uniformly bounded:
\[
8\pi^2\chi(M)
=
\int_M\left(|W|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24}\right)d\mu,
\]
\[
12\pi^2\tau(M)
=
\int_M\left(|W^+|^2-|W^-|^2\right)d\mu.
\]
Both integrals tend to zero as \(\operatorname{Vol}(g_j)\to0\). Hence
\[
\chi(M)=0,
\qquad
\tau(M)=0.
\]

### 2.3 Non-attainment on the listed manifolds

If \(\alpha(M)=0\) is attained by a smooth metric \(g\), then
\[
P(g)=0,
\]
so
\[
\operatorname{Ric}^\circ_g=0,
\]
and \(g\) is Einstein.

If also \(\chi(M)=\tau(M)=0\), then an Einstein metric must be flat. Indeed, for Einstein metrics \(\operatorname{Ric}^\circ=0\), and Chern–Gauss–Bonnet gives
\[
8\pi^2\chi(M)
=
\int_M\left(|W|^2+\frac{s^2}{24}\right)d\mu.
\]
When \(\chi(M)=0\), the integrand is pointwise nonnegative, so
\[
W=0,
\qquad
s=0.
\]
Thus the metric is flat.

The manifolds listed do not carry flat metrics:

* \(S^1\times Y^3\) with \(Y\) hyperbolic or spherical is not flat;
* \(S^2\times T^2\) is not flat;
* Kodaira surfaces are not flat; their fundamental groups are not virtually abelian in the required Bieberbach sense.

Therefore, for these examples,
\[
\alpha(M)=0
\]
but the infimum is not attained.

### 2.4 Corrected statement

Proposition 59.C should be stated with the Ricci norm convention explicit:

> If \(\operatorname{Vol}_{|r|}\) uses the operator Ricci bound \(|\operatorname{Ric}|_{\mathrm{op}}\le3\), then
> \[
> \alpha(M)\le36\,\operatorname{Vol}_{|r|}(M)\le36\,\operatorname{MinVol}(M).
> \]
> If \(|\operatorname{Ric}|\) is the tensor norm, replace \(36\) by \(9\). In either convention, \(\operatorname{MinVol}=0\) implies \(\alpha=0\). Moreover \(\operatorname{MinVol}=0\) forces \(\chi=\tau=0\), and on nonflat manifolds with \(\chi=\tau=0\) the value \(\alpha=0\) is not attained.

---

## 3. Proposition 59.D — partial-collapse constructions

### 3.1 Real-hyperbolic double

Let \(H\) be a finite-volume real-hyperbolic 4-manifold with a cusp. A cusp end has metric
\[
dt^2+e^{-2t}g_N,
\]
where \(N\) is a compact flat 3-manifold.

Truncate at height \(T\). To form the double, join two truncated copies by a collar of \(t\)-length \(O(1)\). Choose a smooth function \(f\) on the collar such that at the two ends it matches the cusp functions:
\[
f=T,\qquad f'=1
\]
on the first side, and
\[
f=T,\qquad f'=-1
\]
on the second side. Choose also
\[
f\ge T,
\qquad
|f'|\le1,
\qquad
|f''|\le C.
\]
The collar metric is
\[
g=dt^2+e^{-2f(t)}g_N.
\]

For a warped product \(dt^2+\phi(t)^2 g_N\) with \(\phi=e^{-f}\) and \(g_N\) flat, the sectional curvatures are:

* fiber–fiber planes:
  \[
  K_{NN}= -\left(\frac{\phi'}{\phi}\right)^2 = -f'^2;
  \]
* mixed time–fiber planes:
  \[
  K_{tN}= -\frac{\phi''}{\phi}
  =-(f'^2-f'').
  \]

Since \(|f'|\le1\) and \(|f''|\le C\), all sectional curvatures on the collar are bounded. Hence \(|\operatorname{Ric}^\circ|\) is bounded there.

The volume element is
\[
d\mu=e^{-3f}dt\,d\mu_N.
\]
Because \(f\ge T\) and the collar has \(t\)-length \(O(1)\),
\[
\operatorname{Vol}(\text{collar})=O(e^{-3T}).
\]
Outside the collar the metric is hyperbolic, hence Einstein, so \(P=0\) there. Therefore
\[
P(g)\le C e^{-3T}\to0.
\]

Topologically, the double
\[
D(H)=H_T\cup_N \overline{H_T}
\]
is a smooth closed 4-manifold, provided the two truncation hypersurfaces are identified by an orientation-reversing diffeomorphism.

The statement in the Step is correct, with the understanding that the piecewise definition of \(f\) is shorthand for a smooth interpolation satisfying the derivative matching above.

---

### 3.2 Complex-hyperbolic Heisenberg-cusp double

A complex-hyperbolic cusp has the form
\[
dt^2+e^{-2t}g_B+e^{-4t}\theta^2,
\]
where \(g_B\) is a flat metric on a 2-torus base and \(\theta\) is a contact form on the Heisenberg nilmanifold satisfying
\[
d\theta=\Omega_B,
\]
with \(\Omega_B\) the constant area form of the base.

For the interpolated double, use
\[
g=dt^2+e^{-2f(t)}g_B+e^{-4f(t)}\theta^2,
\]
with the same type of smooth \(f\) as above.

The crucial point is that the fiber length is the square of the base length:
\[
e^{-2f}=(e^{-f})^2.
\]
Because of this, the nilpotent curvature contribution from \(d\theta\) remains of constant size in an orthonormal frame.

Take the orthonormal coframe
\[
\omega^0=dt,
\qquad
\omega^\alpha=e^{-f}e^\alpha,\quad \alpha=1,2,
\qquad
\omega^3=e^{-2f}\theta,
\]
where \(e^\alpha\) is an orthonormal coframe for \(g_B\). Then
\[
d\omega^\alpha=-f'\omega^0\wedge\omega^\alpha,
\]
and
\[
d\omega^3=-2f'\omega^0\wedge\omega^3+c\,\omega^1\wedge\omega^2,
\]
where \(c\) is a constant determined by \(d\theta\).

The connection coefficients in this frame involve only \(f'\), \(f''\), and the constant \(c\). Schematically, the curvature components have the form
\[
K_{0\alpha}=-(f'^2-f''),
\]
\[
K_{03}=-(4f'^2-2f''),
\]
\[
K_{12}=-f'^2+C_{12},
\]
\[
K_{\alpha3}=-2f'^2+C_{\alpha3},
\]
where the \(C_{ij}\) are constants coming from \(d\theta\). No exponential factor appears because the ratio
\[
\frac{\text{fiber length}^2}{\text{base length}^4}
\]
is fixed.

Thus, if \(|f'|\le1\) and \(|f''|\le C\), all sectional curvatures are uniformly bounded.

The volume element is
\[
d\mu=e^{-4f}dt\,d\mu_N.
\]
Since \(f\ge T\) on the collar,
\[
\operatorname{Vol}(\text{collar})=O(e^{-4T}).
\]
The complex-hyperbolic pieces are Einstein, so their \(P\)-energy vanishes. Hence
\[
P(g)\le C e^{-4T}\to0.
\]

The doubled manifold is again a smooth closed 4-manifold after identifying the two truncation hypersurfaces with opposite orientations.

The Step’s assertion that the ratio fiber/base\(^2\) stays fixed is exactly the reason curvature remains bounded. If that ratio were altered, the \(d\theta\)-curvature term would acquire exponential factors and boundedness would no longer follow.

---

### 3.3 \(T^3\)-cusp Dehn filling for an arbitrary primitive slope

Let \(H\) be a finite-volume real-hyperbolic 4-manifold with a \(T^3\) cusp. Fix a primitive slope
\[
\gamma\in H_1(T^3;\mathbb Z).
\]
Because \(\gamma\) is primitive, it can be completed to an integral basis
\[
(\gamma,u,v)
\]
of \(H_1(T^3;\mathbb Z)\). Thus
\[
T^3\cong S^1_\gamma\times T^2_{u,v}
\]
by a diffeomorphism. The Dehn filling
\[
M_\gamma=H_T\cup_{T^3}(D^2\times T^2)
\]
is obtained by attaching \(D^2\times T^2\) so that \(\partial D^2\) represents \(\gamma\). This is a smooth closed 4-manifold.

The metric construction can be described in four stages.

#### Stage 1: continue the cusp shrinking

Starting from the truncation hypersurface, use a product metric
\[
dr^2+a(r)^2d\gamma^2+e^{-2T}g_{T^2},
\]
with
\[
a(r)=e^{-T-r}
\]
for a bounded interval. The \((r,\gamma)\)-part is a hyperbolic cusp with curvature \(-1\). The \(T^2\) factor is flat and has fixed size \(e^{-T}\). The volume contribution is \(O(e^{-3T})\).

#### Stage 2: turn the circle around

Choose a smooth positive function \(a(r)\) that changes from decreasing to increasing, with
\[
\left|\frac{a''}{a}\right|\le C.
\]
The \((r,\gamma)\)-curvature is
\[
K_{r\gamma}=-\frac{a''}{a},
\]
so it remains bounded. The volume remains \(O(e^{-3T})\).

#### Stage 3: grow the \(\gamma\)-circle while keeping \(T^2\) tiny

Let
\[
a(r)=e^{r-T}
\]
for \(0\le r\le T\), while keeping the \(T^2\)-metric fixed at size \(e^{-T}\). Then the \((r,\gamma)\)-part is again a 2-dimensional hyperbolic cusp, with curvature \(-1\), and the full metric is locally a product with a tiny flat \(T^2\). Curvature is uniformly bounded.

The volume element is
\[
a(r)e^{-2T}\,dr\,d\gamma\,d\mu_{T^2}.
\]
Thus
\[
\int_0^T e^{r-T}e^{-2T}\,dr
=
e^{-3T}(e^T-1)
=
O(e^{-2T}).
\]

#### Stage 4: cap the \(\gamma\)-circle by a round disk

Finally cap the \(S^1_\gamma\) factor by a disk. Use a smooth warping function \(a(r)\) with
\[
a(0)=0,
\qquad
a'(0)=1,
\]
and \(a\) reaching size \(O(1)\). The product with the tiny \(T^2\) gives a smooth metric on \(D^2\times T^2\). The curvature of the disk part is bounded if \(a''/a\) is bounded, and the volume is
\[
O(1)\cdot e^{-2T}=O(e^{-2T}).
\]

Combining all stages,
\[
P(g_T)\le C e^{-2T}\to0.
\]
Therefore
\[
\alpha(M_\gamma)=0
\]
for every primitive slope \(\gamma\).

This construction does not require the slope to be long. The long-slope condition appears only in the Anderson–Bamler Einstein existence theorem.

---

### 3.4 Relation to Anderson–Bamler Dehn filling

Anderson and Bamler construct Einstein metrics with \(s<0\) on Dehn fillings of a \(T^3\) cusp for all but finitely many slopes. For those long slopes, the zero value \(\alpha=0\) is attained by an actual Einstein metric.

For the finitely many remaining short slopes, the explicit collapsing construction above still gives \(\alpha=0\), but attainment is equivalent to the existence of an Einstein metric on that particular filled manifold. The filling theorem does not decide those finitely many cases.

Thus Part C.4 is consistent with Proposition 59.D(b): the analytic collapsing construction applies to every primitive slope, while known Einstein existence theorems apply only to all but finitely many slopes.

---

### 3.5 Doubles and absence of a warped Einstein \(T^3\times I\) neck

For a warped flat \(T^3\)-neck
\[
g=dt^2+\phi(t)^2 g_{T^3},
\]
with \(g_{T^3}\) flat, the Ricci tensor is
\[
\operatorname{Ric}_{00}=-3\frac{\phi''}{\phi},
\]
and, on the \(T^3\) directions,
\[
\operatorname{Ric}_{ij}
=
-\bigl(\phi\phi''+2(\phi')^2\bigr)(g_{T^3})_{ij}.
\]
If this metric is Einstein with constant \(\Lambda\), then
\[
-3\frac{\phi''}{\phi}=\Lambda,
\]
and
\[
-\frac{\phi\phi''+2(\phi')^2}{\phi^2}=\Lambda.
\]
Equating the two expressions gives
\[
\phi\phi''=(\phi')^2.
\]
The nonconstant solutions are exponential:
\[
\phi(t)=Ae^{ct}.
\]
These are cusp-type metrics, not finite necks with a minimum or maximum. A double neck would need \(\phi\) to decrease and then increase, or vice versa, which is incompatible with the exponential solution unless \(\phi\) is constant. The constant solution gives a flat product and cannot match the hyperbolic cusp ends.

Therefore there is no Einstein warped \(T^3\times I\) neck of this simple rotationally symmetric form. This does not prove that no Einstein metric exists on the double; it shows that the natural warped-neck Ansatz is unavailable and that the known Dehn-filling theorems do not apply directly to the double. Thus the Einstein existence question for \(D(H)\) remains open.

---

## 4. Theorem 59.Z — zero-gap structure from Anderson’s idealized minimizers

### 4.1 Anderson’s case labels

Anderson’s Theorem 1.1 uses three behaviors:

* (I) compact orbifold limit;
* (II) total collapse;
* (III) noncompact maximal open orbifold domain with collapsing complement.

Anderson’s Theorem 4.10 labels the noncompact case as (II) and allows \(\Omega=\emptyset\). Step 59 uses the Theorem 1.1 labels:

* Step 59 (I) = Anderson (I);
* Step 59 (III) = Anderson (III) / Theorem 4.10 nonempty \(\Omega\);
* Step 59 (II) = Anderson total collapse / \(\Omega=\emptyset\).

This distinction should be made explicit when citing Anderson.

---

### 4.2 Why minimizers of \(Z_\varepsilon\) have \(P\to\alpha\)

Let
\[
\alpha=\inf P.
\]
Define
\[
m_\varepsilon=\inf Z_\varepsilon.
\]
Since
\[
Z_\varepsilon(g)\ge P(g),
\]
we have
\[
m_\varepsilon\ge\alpha.
\]
For any fixed smooth metric \(g\),
\[
Z_\varepsilon(g)=P(g)+\varepsilon\int(1+|\operatorname{Ric}|^2)^p\,d\mu
\to P(g)
\]
as \(\varepsilon\to0\). Hence
\[
\limsup_{\varepsilon\to0}m_\varepsilon\le\alpha.
\]
Therefore
\[
m_\varepsilon\to\alpha.
\]

If \(g_\varepsilon\) minimizes \(Z_\varepsilon\), then
\[
\alpha\le P(g_\varepsilon)\le Z_\varepsilon(g_\varepsilon)=m_\varepsilon\to\alpha.
\]
Thus
\[
P(g_\varepsilon)\to\alpha.
\]
In particular, if \(\alpha=0\), then
\[
P(g_\varepsilon)\to0.
\]

This part of the Step is correct.

---

### 4.3 Einstein nature of the limiting regular part

Anderson’s theorem gives smooth convergence on compact subsets of the regular part of the limiting domain, after using the elliptic regularity theory for local minimizers of \(Z_\varepsilon\). On any compact regular set \(K\),
\[
\int_K|\operatorname{Ric}^\circ(g_0)|^2\,d\mu_{g_0}
=
\lim_{\varepsilon\to0}
\int_K|\operatorname{Ric}^\circ(g_\varepsilon)|^2\,d\mu_{g_\varepsilon}.
\]
Since the total \(P(g_\varepsilon)\to0\), the right-hand side is zero. Hence
\[
\operatorname{Ric}^\circ(g_0)=0
\]
on the regular part. Thus \(g_0\) is Einstein there.

The same reasoning, applied after rescaling near concentration points, shows that any ALE bubble carrying a nonzero amount of energy must have zero \(P\)-energy, hence is Ricci-flat.

---

### 4.4 What Anderson’s theorem directly gives

Assuming Anderson’s idealized-minimizer theorem for the relevant functional, and assuming \(\alpha(M)=0\), one obtains the following:

1. **Compact orbifold case.**  
   A subsequence converges to a compact oriented orbifold \((V,g_0)\), possibly reducible, with \(g_0\) Einstein on the regular part. Bubble trees may appear at singular points. Since the total \(P\)-energy tends to zero, the bubbles are Ricci-flat ALE spaces or Ricci-flat ALE orbifold trees.

2. **Noncompact domain case.**  
   A subsequence converges to a nonempty maximal orbifold domain \((\Omega,g_0)\), weakly embedded in \(M\), with
   \[
   0<\operatorname{Vol}(\Omega,g_0)\le1,
   \]
   \(g_0\) Einstein on the regular part, and an \(F\)-structure collapsing region outside large compact sets.

3. **Total collapse case.**  
   If \(\Omega=\emptyset\), the sequence collapses everywhere with locally bounded curvature along \(F\)-structures, away from finitely many shrinking balls.

This is the core trichotomy.

---

### 4.5 Completeness and the sign of scalar curvature in case (III)

The Step states that in case (III), \(\Omega\) is complete, finite-volume, and has \(s<0\). The finite-volume part is supplied by Anderson:
\[
\operatorname{Vol}(\Omega,g_0)\le1.
\]

The sign argument is:

* If \(g_0\) is complete, noncompact, finite-volume, and Ricci-flat, then it has infinite volume; this is incompatible with \(\operatorname{Vol}(\Omega)<\infty\).
* If \(s>0\) and \(g_0\) is complete Einstein, Myers’ theorem forces compactness.
* Therefore a complete noncompact finite-volume Einstein domain must have
  \[
  s<0.
  \]

However, Anderson’s Theorem 4.10, as written in the supplied Knowledge object, does not explicitly prove completeness of \(g_0\) on \(\Omega\). In Remark 4.12, Anderson states that completeness and finite topological type for \(\Omega\) are expected but not established in full generality. He notes that completeness follows if the curvature is pointwise bounded or under suitable Ricci lower bounds.

Therefore the sign conclusion \(s<0\) is valid under the additional completeness property for the noncompact Einstein domain. Without that extra input, Anderson’s theorem alone gives an Einstein domain \(\Omega\) with finite volume and collapsing ends, but does not by itself exclude an incomplete finite-volume domain with \(s\ge0\).

A precise formulation is:

> In the noncompact case, Anderson gives a maximal Einstein orbifold domain \((\Omega,g_0)\) with \(0<\operatorname{Vol}(\Omega)\le1\) and collapsing \(F\)-structure complement. If, in addition, \((\Omega,g_0)\) is complete—as in the explicit cusp examples and in the complete Einstein cusp picture—then \(s<0\).

The Step’s explicit examples in Proposition 59.D do produce complete Einstein limiting domains: cusped hyperbolic or complex-hyperbolic metrics. Thus the mechanism satisfies the stronger version.

---

### 4.6 Extra hypotheses implicitly used

The following inputs are needed for the theorem as stated:

1. **Use of Anderson’s special minimizing sequence.**  
   The smooth convergence and regularity come from Anderson’s perturbed minimizers and his elliptic regularity theory, not from an arbitrary minimizing sequence for \(P\).

2. **Local minimizing property.**  
   Anderson’s regularity theory applies to minimizers, or local minimizers, of the perturbed fourth-order functional. This is part of the machinery behind Proposition 4.6 and Theorem 4.10.

3. **Unit-volume normalization.**  
   Anderson’s theorem is formulated for unit-volume metrics. Since \(P\) is scale invariant, this is harmless, but constructed metrics must be rescaled to volume \(1\) before invoking Anderson.

4. **Completeness of \(\Omega\) for the \(s<0\) conclusion.**  
   As above, this is not automatically supplied by Theorem 4.10 in full generality.

5. **Topology of bubble trees.**  
   The statement that \(V\) is obtained from \(M\) by collapsing cycles and that the ALE tree exactly reconstructs the topology of \(M\) requires additional no-neck/topological input, such as the Step 58 ledger. Anderson’s theorem gives the geometric decomposition but not the full topological reconstruction by itself.

---

### 4.7 Attainment

The assertion

\[
\alpha(M)=0 \text{ is attained iff } M \text{ carries an Einstein metric}
\]

is correct for smooth metrics on \(M\).

Indeed, if \(g\) attains \(\alpha=0\), then
\[
P(g)=0,
\]
so
\[
\operatorname{Ric}^\circ_g=0,
\]
and \(g\) is Einstein. Conversely, an Einstein metric has \(P=0\), so it attains \(\alpha=0\).

This should be read as smooth attainment on \(M\). An Einstein orbifold metric on a singular limit gives \(\alpha=0\) through approximating smooth metrics, but it does not by itself give a smooth Einstein metric on \(M\).

For the mechanisms:

* In Proposition 59.N, attainment occurs exactly when the resolved manifold \(M\) carries an Einstein metric.
* In Proposition 59.C, when \(\chi=\tau=0\), attainment would require a flat metric; the listed nonflat examples do not attain.
* In Proposition 59.D(b), long-slope fillings attain by Anderson–Bamler Einstein metrics; the remaining finite set attains iff an Einstein metric exists.
* For doubles \(D(H)\), Einstein existence is open, so attainment is open.

---

## 5. Summary of corrected statements

### Proposition 59.N

Correct as a zero-energy gluing construction. The \(O(\lambda^2)\) estimate follows from standard ALE decay, the choice \(t=\lambda^{1/2}\), bounded curvature on the annulus, and annular volume \(O(t^4)=O(\lambda^2)\). Finite ALE trees are handled by hierarchical induction. Orientation compatibility is required, but orientation reversal does not affect \(P\).

### Proposition 59.C

The collapse estimate is correct once the Ricci norm convention is specified. With \(|\operatorname{Ric}|_{\mathrm{op}}\le3\),
\[
\alpha(M)\le36\,\operatorname{Vol}_{|r|}(M)\le36\,\operatorname{MinVol}(M).
\]
With a tensor norm bound \(|\operatorname{Ric}|_{\mathrm{Frob}}\le3\), the constant is \(9\). \(\operatorname{MinVol}=0\) forces \(\chi=\tau=0\). On nonflat manifolds with \(\chi=\tau=0\), \(\alpha=0\) is not attained because any attaining Einstein metric would be flat.

### Proposition 59.D

The real-hyperbolic double, complex-hyperbolic double, and \(T^3\)-cusp Dehn filling constructions are analytically sound.

* The real double uses a smooth \(f\) with \(f\ge T\), \(|f'|\le1\), \(|f''|\le C\), giving bounded curvature and transition volume \(O(e^{-3T})\).
* The complex-hyperbolic double remains bounded because the fiber length is the square of the base length; the nilpotent curvature term stays constant in an orthonormal frame. Transition volume is \(O(e^{-4T})\).
* The \(T^3\)-filling works for every primitive slope. The staged metric has bounded curvature and total \(P\)-energy \(O(e^{-2T})\).
* Anderson–Bamler gives Einstein metrics for all but finitely many long slopes, so those fillings attain \(\alpha=0\). The remaining finitely many slopes have \(\alpha=0\) by construction, with attainment equivalent to Einstein existence.
* For doubles, the warped Einstein neck equation forces \(\phi=Ae^{ct}\), so no finite warped \(T^3\times I\) Einstein neck exists. This supports the openness of Einstein existence on doubles but does not itself exclude non-warped Einstein metrics.

### Theorem 59.Z

Anderson’s Theorem 4.10, together with \(P(g_\varepsilon)\to0\), gives the trichotomy:

1. compact Einstein orbifold plus Ricci-flat ALE bubble tree;
2. nonempty Einstein orbifold domain with collapsing \(F\)-structure complement;
3. total collapse.

The regular part is Einstein because \(P(g_\varepsilon)\to0\) and convergence is smooth on compact regular subsets.

The additional description of case (III) as complete finite-volume with \(s<0\) requires completeness of the limiting Einstein domain. Anderson’s theorem gives finite volume and the collapsing \(F\)-structure, but completeness is an extra input or a conjectural part of the general theory. With completeness, the exclusion of Ricci-flat and positive-scalar cases gives \(s<0\).

The attainment statement is correct in the smooth category: for \(\alpha=0\), smooth attainment is equivalent to the existence of a smooth Einstein metric on \(M\).