# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step82_goldberg_levelset_SW_and_symmetric_closures.md",
    "Sessions/S1003A01/workspace/notes/step81_normalized_sections_and_ddc_canonical_pairing.md",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/notes/step79_second_tier_dWplus_kodaira_and_log_torsion_identity.md",
    "Sessions/S1003A01/workspace/notes/step77_goldberg_first_tier_collapse_and_canonical_curve_identity.md"
  ]
}
```

## Task

The research programme is attacking the closed negative-scalar Goldberg problem in dimension four: prove that a closed almost-Kähler Einstein 4-manifold (M,g,ω) with s<0 is Kähler, or construct a closed strictly almost-Kähler Einstein counterexample.

The attached notes record the established state.
- A complete noncompact strict AKE model exists (Bianchi VIII, W⁻=0, q>0 at finite points, ACH-type end). It satisfies every integral identity built from decaying local densities: the AAD balance, Kodaira identities, the W⁺ Bochner identity and the regularized identities. It also satisfies the Seiberg–Witten Weyl integrand estimate, with a large margin.
- Torsion zeros are forced on a closed candidate, carrying c₂(E)=5χ+6τ. Nondegenerate zeros have index +1. Finite-order jets give no local obstruction.
- The amplitude-level flux identity reduces to the coarea densities of |Y|² and |η|², and the remaining freedom is the trace-free ∇Y driven by ∂_Dv.
- Symmetric (cohomogeneity-one) closures are excluded.

Produce two or three genuinely different, mathematically concrete global arguments, or a constructive route, that could change the closed-manifold conclusion. These must not be another local integral identity or rewriting of the known balance. Each should exploit something the model provably lacks: finite volume, compactness of the zero set, the Euler class, harmonic ASD classes (b⁻≥1 is forced), canonical J-currents, or the twistor or harmonic-section viewpoint (η is the tension of J as a section of the twistor bundle). Spectral or unique-continuation input is also admissible.

For each argument:
- state the precise conjectural statement;
- explain why the model does not already satisfy its premises, or why it uses compactness essentially;
- identify the first decisive calculation, with the exact objects and formulas;
- say what result would kill it.

Partial theorems of real value, such as Goldberg under a natural weak hypothesis not covered by Sekigawa, Apostolov–Armstrong–Drăghici (W₂⁺=0, Gray conditions) or Kim (b⁻=0), are welcome if precisely formulated with a proof route. Do not invent literature; name a precise knowledge_request if a source is needed.

## Output

The complete Bianchi-VIII solution shows that any compact proof must use an input that cannot be pushed out the ACH end: a discrete spectrum, a compact zero current, or a compact harmonic ASD form. The following three routes are separated by the global object they use.

---

## 1. Twistor tension and a compact Jacobi test for the section \(J\)

### Conjectural statement

Let  
\[
u=\frac{\omega}{\sqrt2}\in \Gamma(S(\Lambda^+))
\]
be the unit self-dual section determined by the almost-Kähler structure. The Hodge harmonicity of \(\omega\) gives
\[
\Delta_H u=0,
\]
and the Einstein Weitzenböck formula gives
\[
\Delta_H u=\nabla^*\nabla u+\frac{s}{3}u-2W^+u.
\]
With
\[
W^+u=r u+\eta,\qquad r=\frac{s}{6}+\frac{q}{4},\qquad |\nabla u|^2=\frac q2,
\]
this becomes
\[
\nabla^*\nabla u=\frac q2\,u+2\eta.
\]
For a unit section, the tension as a section of the twistor sphere bundle is
\[
\tau(u)=\nabla^*\nabla u-|\nabla u|^2u=2\eta.
\]
Thus \(\eta\) is exactly the vertical tension of the twistor section.

The conjecture is:

> On a closed almost-Kähler Einstein four-manifold with \(s<0\), the vertical Jacobi operator of the twistor section \(u\) has a compact spectral gap, and the equation \(\tau(u)=2\eta\) forces \(\eta\equiv0\). Equivalently, Goldberg holds under the weak additional hypothesis that the twistor section \(u\) is stable for the natural twistor-section functional.

A partial theorem of immediate value would be:

> If the Jacobi quadratic form of \(u\) is semipositive on sections of \(u^\perp\), then \(\eta=0\), hence the metric is Kähler.

This is not a restatement of the known integral balances. It uses the compactness of the spectrum of a second-order elliptic operator on a closed manifold.

### Why the Bianchi-VIII model does not satisfy the premise

The model has no compact twistor-section spectrum. Its end allows the tension field \(\eta\) to decay and the divergence terms in the section Bochner formula to escape as end flux. On a closed manifold, those divergence terms integrate to zero; on the model they are absorbed by the infinite-volume end. The model also has no finite-volume stability condition for the twistor section.

### First decisive calculation

Work in the vertical bundle \(V=u^\perp\cong \operatorname{span}\{\Re\psi,\Im\psi\}\). The decisive computation is the exact twistor-section Bochner identity for the tension:
\[
\frac12\Delta|\eta|^2
=
|\nabla\eta|^2
+
\text{vertical curvature term}
+
\text{algebraic terms in }(q,\eta,v,\partial_Dv).
\]
In the Atiyah–Hitchin–Singer convention, the vertical curvature term over an Einstein base with \(s<0\) should contribute a favourable zero-order term proportional to \(|s||\eta|^2\). The exact object to compute is
\[
L\eta := \text{vertical part of } \delta d\,\eta + \frac{|s|}{6}\eta,
\]
with \(L\eta\) expressed through the second-tier system
\[
\partial_D\eta = v\alpha+iK(\partial r),\qquad
\overline{\partial_D\eta}= -\frac{3r}{2}\alpha-2iK(\partial_Dv).
\]
After integration over a closed manifold, the divergence term disappears. The remaining algebraic terms should be compared with the exact second-tier budget
\[
10\int|\partial_Dv|^2+2\int|\bar\partial_Dv+\eta\bar\alpha|^2
=
\int\left[
\frac{5|s|}{2}\operatorname{tr}V^2
+18\eta^TV\eta
+q|\eta|^2
-q\operatorname{tr}V^2
-\frac{|s|q^2}{8}
+\frac{3q^3}{16}
\right],
\]
which is identity (82.B).

The critical test is whether the integrated twistor Bochner identity gives
\[
\int\left(|\nabla\eta|^2+c|s||\eta|^2\right)
\le
\int \text{algebraic terms}
\]
with the algebraic terms forced below the left-hand side unless \(T_{AK}=0\). If so, \(\eta=0\).

### What would terminate this route

A decisive termination signal would be an exact algebraic calculation on the Step-62 cone jets showing that the twistor Bochner integrand can vanish, or become arbitrarily small, with \(\eta\neq0\), while all second-tier equations hold. Equivalently, if the Jacobi quadratic form evaluated on the model fields, after compactly supported truncation, tends to zero without forcing \(\eta\to0\), then compact stability alone cannot prove Goldberg.

---

## 2. Euler transgression of the normalized torsion section and logarithmic charge

### Conjectural statement

Let \(\alpha\) be the torsion one-form, viewed as a section of the complex rank-two bundle carrying Euler number
\[
\int_M e(E)=5\chi+6\tau.
\]
On the complement of the zero set \(Z=\{\alpha=0\}\), define the normalized section
\[
\sigma_\varepsilon=\frac{\alpha}{\sqrt{q+\varepsilon}}.
\]
Let \(\Psi(\sigma_\varepsilon)\) be the Euler–Chern–Simons transgression form of the unit sphere bundle, so that
\[
d\Psi(\sigma_\varepsilon)=e(E,\nabla^\sim)-R_\varepsilon,
\]
where \(R_\varepsilon\) is a regularization remainder supported where \(q\) is small.

The conjectural global mechanism is:

> The Euler charge \(5\chi+6\tau\) forces a definite amount of renormalized logarithmic torsion curvature. On a closed manifold, the compactness-sensitive term
> \[
> \int_M\frac{\varepsilon}{q+\varepsilon}\,dV
> \]
> tends to zero as \(\varepsilon\to0\), while the transgression integral over linking three-spheres around the zeros remains equal to \(5\chi+6\tau\). The AK Einstein equations then force a quantitative inequality between \(5\chi+6\tau\), \(T_{AK}\), and \(c_1^2\). For topologies where this inequality is violated, no strict almost-Kähler Einstein metric exists.

A sharp form would be a universal estimate of the type
\[
|5\chi+6\tau|
\le
C\,|s|^{-2}
\int_M\left(|\nabla W^+|^2+|s|^2q\right)dV,
\]
with the right-hand side then expressed through the known topological identities and (82.B). Such an estimate would be genuinely global: it uses the compact zero set and the Euler class, not a new local density identity.

### Why the Bianchi-VIII model does not satisfy the premise

The model has no compact zero set and no Euler charge. Its normalized torsion section is globally defined, and the transgression integral is carried away by the end rather than localized on linking spheres. Also,
\[
\int_M\frac{\varepsilon}{q+\varepsilon}\,dV
\]
diverges on the model for fixed \(\varepsilon>0\), whereas on a closed manifold it tends to zero. This is exactly the compactness-sensitive term identified in Step 81.

### First decisive calculation

The first calculation is to write the Euler transgression explicitly in the AK variables. For a unit section \(\sigma\) of the oriented real four-plane bundle \(E\), the standard transgression form is
\[
\Psi(\sigma)
=
\frac{1}{2\pi^2}
\sigma^*(\text{fiber volume}),
\]
or, in connection form,
\[
\Psi(\sigma)
=
\frac{1}{8\pi^2}
\epsilon_{abcd}\,
\sigma^a D\sigma^b\wedge D\sigma^c\wedge D\sigma^d,
\]
where \(D\) is the canonical connection on \(E\). One must express this in terms of
\[
\alpha,\quad D\alpha,\quad b,\quad K,\quad v,\quad \eta.
\]
The curvature identity already known from Step 77 is
\[
4\pi^2 e(E,\nabla^\sim)
=
\frac94\gamma\wedge\gamma
+
\frac14\left(2|W^-|^2+\frac{s^2}{24}\right)dV.
\]
The decisive step is to integrate
\[
d\Psi(\sigma_\varepsilon)=e(E,\nabla^\sim)-R_\varepsilon
\]
over \(M\) and take \(\varepsilon\to0\). The left-hand side gives the sum of local indices over the zero set, i.e. \(5\chi+6\tau\). The remainder \(R_\varepsilon\) must be controlled by the regularized identities such as (80.S) and by the second-tier algebra (82.B).

A refined version pairs the zero charge with the closed form
\[
\beta=\gamma-\frac{s}{4}\omega.
\]
When zero strata contain \(J\)-curves, the \(\beta\)-pairing connects directly to the canonical-cycle identity
\[
T_{AK}-\int_M|\eta|^2
=
2\pi\int_T |a^\perp|^2\,dA.
\]
When the zeros are isolated, the same information is carried by the secondary Euler form on the linking three-spheres.

### What would terminate this route

The route would be terminated by a cone-jet construction showing that the Euler charge can be carried with arbitrarily small renormalized energy. Concretely, if one can produce Step-62-type finite-order jets with index \(+1\) for which
\[
\int \left(|d\log q|^2+\frac{|\nabla^\perp\alpha|^2}{|\alpha|^2}\right)dV
\]
is arbitrarily small while the local Euler index remains fixed, then no universal inequality of the above type can hold. Another termination signal would be an explicit compact local model in which the transgression remainder \(R_\varepsilon\) absorbs the entire Euler charge without forcing \(T_{AK}=0\).

---

## 3. Constructive bifurcation from Kähler-Einstein surfaces using harmonic ASD forms

### Conjectural construction

Every closed strict candidate must have \(b^-\ge1\). This can be turned into a construction mechanism rather than merely an obstruction.

Let \((X,g_0,J_0,\omega_0)\) be a closed Kähler-Einstein surface with
\[
\operatorname{Ric}(g_0)=\lambda g_0,\qquad \lambda<0.
\]
Suppose there exists a nonzero primitive harmonic \((1,1)\)-form
\[
\varphi\in H^-(X)
\]
such that the associated symmetric trace-free tensor
\[
h_\varphi(X,Y)=\varphi(J_0X,Y)
\]
is an infinitesimal Einstein deformation of \(g_0\).

The conjectural construction is:

> If \(h_\varphi\) lies in the kernel of the Lichnerowicz Einstein operator and the first nontrivial Einstein obstruction in that direction vanishes or changes sign, then there exists a branch of Einstein metrics
> \[
> g_t=g_0+t h_\varphi+O(t^2)
> \]
> together with closed two-forms
> \[
> \Omega_t=\omega_0+t\varphi+O(t^2)
> \]
> such that \(\Omega_t\) is self-dual and of constant norm for \(g_t\). For generic \(\varphi\), the associated almost-complex structure is not integrable, producing a closed strict almost-Kähler Einstein metric with \(s<0\).

This would give a genuine counterexample route, not merely an exclusion theorem.

### Why the Bianchi-VIII model does not satisfy the premise

The model has \(W^-=0\) and no compact harmonic ASD forms. The construction uses the finite-dimensional space \(H^-(X)\), the Fredholm property of the Einstein operator on a closed manifold, and the existence of actual harmonic representatives. None of these objects exists on the noncompact model.

### First decisive calculations

There are three exact first calculations.

#### 3.1 Linearized Einstein equation

Compute the Lichnerowicz operator on \(h_\varphi\):
\[
(\Delta_E h_\varphi)_{ij}
=
\nabla^*\nabla h_{\varphi,ij}
+
2R_{ikjl}h_\varphi^{kl}
-
2\lambda h_{\varphi,ij}.
\]
For a Kähler-Einstein metric, the curvature decomposition should allow this to be rewritten in terms of the Hodge Laplacian on \(\varphi\) and the \(W^-\)-action. The decisive identity to verify is
\[
\Delta_E(\varphi\circ J_0)
=
(\Delta_H\varphi)\circ J_0
+
\text{explicit }W^-\text{ term}.
\]
If \(\varphi\) is harmonic ASD, this determines whether \(h_\varphi\) is an infinitesimal Einstein deformation.

#### 3.2 Self-duality and constant norm of \(\Omega_t\)

The two-form
\[
\Omega_t=\omega_0+t\varphi
\]
is closed to first order because both \(\omega_0\) and \(\varphi\) are closed. One must solve the coupled first-order system
\[
d^+_{g_t}\Omega_t=0,\qquad |\Omega_t|^2_{g_t}=2.
\]
The linearization of the self-duality equation is a map
\[
\varphi\mapsto \left.\frac{d}{dt}\right|_{t=0} d^+_{g_t}(\omega_0+t\varphi).
\]
The calculation should show whether the choice \(h_\varphi=\varphi\circ J_0\) makes this derivative vanish. If it does, then the Einstein deformation and the symplectic self-duality deformation are compatible to first order.

#### 3.3 First variation of the Nijenhuis tensor

To ensure the resulting almost-Kähler structure is strict, compute the first variation of the Nijenhuis tensor. In Kähler coordinates, the relevant component should be expressible schematically as
\[
\delta N^{0,2}
=
(\bar\partial \varphi)^{0,2}
\]
or an equivalent covariant expression involving the \((0,2)\)-part of \(\nabla\varphi\). If this is nonzero for a generic harmonic ASD \(\varphi\), then the deformed almost-complex structure is not integrable.

### What would terminate this route

The route is terminated if the linear calculation shows that no nonzero harmonic ASD form \(\varphi\) produces an infinitesimal Einstein deformation satisfying the self-duality condition. Equivalently, if
\[
\Delta_E(\varphi\circ J_0)
\]
never vanishes for harmonic primitive \((1,1)\) forms on Kähler-Einstein surfaces with \(\lambda<0\), the construction cannot start.

A second termination signal is a second-order obstruction with a fixed sign. If the quadratic Einstein obstruction
\[
\operatorname{Ob}(\varphi)
=
\int_X \langle Q(h_\varphi),h_\varphi\rangle\,dV_{g_0}
\]
is nonzero and has the same sign for every allowable \(\varphi\), then no bifurcating Einstein branch exists in that direction.

A third termination signal would be a proof that every such branch preserves integrability of the compatible almost-complex structure. In that case the construction only moves within Kähler-Einstein metrics and cannot produce a strict almost-Kähler Einstein example.

---

## Precise knowledge requests

1. **Twistor-section Jacobi operator.** The exact form of the Jacobi operator for the unit self-dual section \(u=\omega/\sqrt2\) over an Einstein four-manifold with \(s<0\), in conventions matching Steps 77–82, especially the vertical curvature coefficient and the algebraic action of \(W^+\) on \(u^\perp\).

2. **Koiso-type Einstein deformation theory.** The precise statement identifying primitive harmonic \((1,1)\) forms on a Kähler-Einstein surface with \(\lambda<0\) as infinitesimal Einstein deformations, together with the explicit second-order obstruction formula for the Einstein equation in that direction.