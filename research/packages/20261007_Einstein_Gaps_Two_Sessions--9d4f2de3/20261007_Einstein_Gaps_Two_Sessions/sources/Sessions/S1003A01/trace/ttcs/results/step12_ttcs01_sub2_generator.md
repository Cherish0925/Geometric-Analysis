# TTCS Independent Branch Record

```json
{
  "step_id": 12,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md",
    "Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md",
    "Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/mathematics/current/round15_boundary_response.md",
    "Knowledge/objects/papers/1303.0827-Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--711e2a97c44e--5258e72d2de1/object.md"
  ]
}
```

## Task

Develop a mathematically precise two-core interaction framework for the established Einstein-defect cell problem. The functional is J(g)=∫|Ric(g)+g|² on a compact region in a complex-hyperbolic four-manifold with an exact CH outer collar. Start from two actual admissible blow-up cores, not formal curvature sources. Derive the correct small-boundary-data reduced action about the CH exterior, including gauge, the order of the Euler equation, the boundary jet variables, the Schur-complement/Dirichlet-to-Neumann form, and the cross term between the two cores. Explain how separation and relative orientation enter, what symmetry could force the orientation-averaged cross term to vanish, and what nonzero calculation would yield a strict improvement over two copies of the certified frozen witness. Distinguish an improvement over a known witness sum from strict nonadditivity relative to unknown infima. Propose one tractable calculation or numerical PDE experiment that could decisively determine the sign while using boundary data extracted from the actual frozen cell. Do not assume ordinary Einstein Dirichlet data suffice for the squared-defect functional.

## Output

# Two-core interaction theory for the exact-CH defect functional

Units: \(J(g)=\int|\operatorname{Ric}_g+g|^2\), with complex hyperbolic metric \(g_0\), \(\operatorname{Ric}_{g_0}=-g_0\). The frozen witness, stored in \(\operatorname{Ric}=-6g\) cell coordinates, is converted by \(\tilde g=6g\). This leaves \(J\) unchanged (Step 11, §2.4).

## 1. Admissible two-core competitors

Let \(C_*\) be the certified perpendicular cell (\(x_0=10^{-2}\), \(X=8\)). Fix a cut level \(x_c<X\) and let \(K_*=\{x\le x_c\}\subset C_*\), with interface \(\Sigma=\{x=x_c\}\cong S^3\).

On the overlap \(x\ge x_c\), the cell and CH share the coordinates \((x,\sigma_i)\). The perturbation
\[
h_*=g_*-g_0\qquad\text{on }x\ge x_c
\]
is therefore a definite tensor. Its 1-jet on \(\Sigma\) is the core datum
\[
y_*=\bigl(h_*|_\Sigma,\ \nabla_\nu h_*|_\Sigma\bigr).
\]

Place isometric copies \(K_1,K_2\) at \(p_1,p_2\in H^2_{\mathbb C}\), with orientations \(k_i\in U(2)_{p_i}\). Let \(\Omega\) be the complement of the two cores.

A competitor is defined as follows:
- \(g=g_*\) on each \(K_i\);
- \(g=g_0+h\) on \(\Omega\), where \(h\) has 1-jet \(y_i\) on \(\Sigma_i\);
- \(h\) vanishes identically on an outer collar, of any radius.

The glued metric is \(C^{1,1}\), and only second derivatives may jump. Mollifying across a width-\(\delta\) layer changes \(J\) by \(O(\delta)\), since curvature stays bounded on a region of volume \(O(\delta)\). Hence \(J\) of the glued metric is a limit of costs of smooth exact-collar metrics on \(D\#2\overline{\mathbb{CP}}^2\). The cost splits exactly:
\[
J=J_{\rm in}(K_1)+J_{\rm in}(K_2)+J_\Omega(g_0+h).
\]
Nothing in this construction is a formal source; the cores are the actual frozen metric.

## 2. Exterior expansion and the Euler system

### 2.1 Quadratic expansion

Since \(E(g_0)=0\), every term that varies the norm or the volume multiplies \(E\). Therefore
\[
J_\Omega(g_0+h)=\int_\Omega|Lh|^2\,dV_0+\mathcal C_3(h)+\dots,
\qquad
L h=\tfrac12\nabla^*\nabla h-\mathring R h-\delta^*\beta h.
\]
Here \(\beta=\delta+\tfrac12 d\operatorname{tr}\), \(\delta=-\operatorname{div}\), \(\delta^*\omega=\operatorname{sym}\nabla\omega\), and \(L=E'_{g_0}\). This uses \(\operatorname{Ric}'=\tfrac12\Delta_L-\delta^*\beta\) with \(\Delta_L=\nabla^*\nabla-2-2\mathring R\) on \(\operatorname{Ric}=-g\).

The adjoint is
\[
L^*e=\tfrac12\nabla^*\nabla e-\mathring R e-\delta^*\delta e-\tfrac12(\delta\delta e)g .
\]

### 2.2 The fourth-order Euler equation as a coupled pair

The exterior Euler equation is \(L^*Lh=0\), which is fourth order. It is best read as the pair
\[
Lh=e,\qquad L^*e=0 .
\]
Put \(\sigma=\operatorname{tr}e\), the linearized \(s+4\). The linearized contracted Bianchi identity gives \(\delta e=-\tfrac12 d\sigma\) exactly. Hence
\[
L^*e=\tfrac12\nabla^*\nabla e-\mathring Re+\tfrac12\nabla^2\sigma+\tfrac14(\nabla^*\nabla\sigma)g=0 .
\]

Its trace is \((\nabla^*\nabla+1)\sigma=0\), using \(\operatorname{tr}\mathring Re=-\sigma\). This is the linearization of (8.1) in `relative_cell_cost`. The trace-free part is the Einstein operator \(P=\nabla^*\nabla-2\mathring R\), forced by \(\nabla^2\sigma\).

Consequences:
- **The defect is itself a field.** The far defect field \(e\) is a solution of the adjoint linearized Einstein system. It is the exact analogue of the Gursky–Viaclovsky cokernel element \(o_1\).
- **Doubled indicial roots.** The indicial roots of \(L^*L\) are those of \(P\) and of \(\nabla^*\nabla+1\), each doubled. Defect-carrying tails therefore decay like \(r\,e^{-\kappa r}\).
- **Scalar rate.** In cell units (\(\operatorname{Ric}=-6g\), volume entropy \(4\)), the scalar channel has \(\kappa_\sigma=2+\sqrt{10}\).
- **Tensor rates.** The tensor-channel rates in each \(U(1)_R\) weight still have to be computed. They come from the radial ODE of §7(ii).

### 2.3 Gauge

Diffeomorphism invariance gives \(L(\mathcal L_Xg_0)=0\). So \(\int|Lh|^2\) is degenerate along every \(X\) whose 2-jet vanishes on \(\Sigma\).

Two equivalent fixes are available:
- the Gursky–Viaclovsky device: add \(\mathcal K\delta\mathcal K\delta\mathring h\), and recover genuine critical points because the gradient of a Riemannian functional is divergence-free (their Prop. 3.5);
- reduction to gauge-invariant interface data, as in §3.

In the symmetric sectors used below, gauge becomes trivial (§7).

## 3. Interface variables and the Dirichlet-to-Neumann operator

### 3.1 Data count

The Dirichlet variables of a second-order energy in \(h\) are its 1-jet \((h,\nabla_\nu h)\): 20 functions on \(S^3\). Gauge acts through the 2-jet of \(X\) (\(X\), \(\partial_\nu X\), \(\partial_\nu^2X\)): 12 functions.

This leaves 8 invariant functions. Equivalently, take \((\gamma,\mathrm{II})\) modulo \(\operatorname{Diff}(\Sigma)\) and normal displacement. These 8 split as:
- 4 Gauss–Codazzi constraint values, i.e. \(e(\nu,\nu)\) and \(e(\nu,\cdot)\) on \(\Sigma\);
- 4 constraint-satisfying Einstein Cauchy data, i.e. transverse-traceless \(\gamma\) and \(\mathrm{II}\).

The Einstein Dirichlet problem sees only half of the second group. The \(J\)-problem sees all 8.

### 3.2 Green's form

With \(\nu\) outward from \(U\),
\[
\int_U\bigl(\langle e,Lk\rangle-\langle L^*e,k\rangle\bigr)=\oint_{\partial U}\mathfrak B(e,k),
\]
\[
\mathfrak B(e,k)=\tfrac12\bigl(\langle\nabla_\nu e,k\rangle-\langle e,\nabla_\nu k\rangle\bigr)-e(\nu,\beta k)+k(\nu,\delta e)-\tfrac12(\operatorname{tr}k)\,(\delta e)(\nu).
\]
The Neumann variables dual to the 1-jet are the interface components of \(e\) (paired with \(\nabla_\nu k\)) and the traction built from \(\nabla e\) and \(d\sigma\) (paired with \(k\)). These are third derivatives of \(h\).

### 3.3 Natural matching at an optimum

When both sides are re-optimized, the natural conditions are continuity of \(e\)'s interface components and of the traction. The optimal glued metric is therefore matched to third order. This is Cauchy matching for a fourth-order system, not the \(C^1\) matching of Einstein gluing. It is the precise sense in which ordinary Einstein Dirichlet data do not suffice.

### 3.4 The DtN operator and its kernel

\(\Lambda_\Omega\) is defined by \(Q_\Omega(y)=\langle y,\Lambda_\Omega y\rangle=\min\int_\Omega|Lh|^2\). It is \(\ge0\).

Define the exterior problem on all of \(H^2_{\mathbb C}\) as the monotone limit of exact-collar problems of increasing radius. A collar at radius \(R\) is admissible for every \(R'>R\), so this limit exists without any truncation estimate.

- **Finite exact collar.** Here \(\ker\Lambda\) is trivial modulo gauge. A solution of \(Lh=0\) vanishing on an open collar is pure gauge, by unique continuation in Bianchi gauge.
- **Limit operator.** Its kernel is the space of Cauchy data of decaying Einstein deformations that lie in the energy closure. This is a Lagrangian half of the constraint-satisfying data.
- **What decides membership.** Whether slowly decaying Einstein tails belong to the closure depends on the CH indicial rates compared with \(\rho\), the half-entropy. This must be checked weight by weight.

## 4. Two-core Schur complement and the exact first-order cross term

### 4.1 Single-core fields

Let \(h_i\) minimize \(\int_{H^2_{\mathbb C}\setminus B_i}|Lh|^2\) with datum \(y_i\), and put \(e_i=Lh_i\). Each \(h_i\) is smooth through the other core's ball.

### 4.2 Expansion of the two-core minimizer

Write the two-core minimizer as \(h=h_1+h_2+r\). The correction \(r\) carries the 1-jet \(-a_1\) on \(\Sigma_1\), with \(a_1=j^1h_2|_{\Sigma_1}\), and similarly \(-a_2\) on \(\Sigma_2\).

Expand \(\int_\Omega|e_1+e_2+Lr|^2\) using \(L^*e_i=0\) in \(\Omega\):
- \(2\int_\Omega\langle e_1,e_2\rangle=2\oint_{\Sigma_1\cup\Sigma_2}\mathfrak B(e_1,h_2)\). Its \(\Sigma_1\) part equals \(2\langle N_1,a_1\rangle\), where \(N_1\) is the Neumann datum of \(h_1\).
- \(2\int_\Omega\langle e_1+e_2,Lr\rangle=-2\langle N_1,a_1\rangle-2\langle N_2,a_2\rangle+O(\text{cross}^2)\).

The \(\Sigma_1\) terms cancel. What remains is
\[
\boxed{Q_\Omega(y_1,y_2)=Q_1(y_1)+Q_2(y_2)+I_{12}+O(\text{cross}^2),\qquad
I_{12}=2\oint_{\Sigma_2}\mathcal W(h_1,h_2),}
\]
\[
\mathcal W(u,v)=\mathfrak B(Lu,v)-\mathfrak B(Lv,u),
\]
with \(\nu\) pointing into core 2.

### 4.3 Properties of the cross term

- **Conservation.** For two solutions of \(L^*L=0\), \(\mathcal W\) is a closed 3-form. So \(\Sigma_2\) may be replaced by any sphere enclosing core 2 but not core 1, and \(I_{12}=-2\oint_{\Sigma_1}\mathcal W\).
- **Gauge invariance.** \(\oint\mathfrak B(Lh_1,\mathcal L_Xg_0)=\int\langle L^*Lh_1,\mathcal L_Xg_0\rangle=0\).
- **Einstein parts do not interact.** \(\mathcal W(h^E,h'^E)=0\) whenever both fields satisfy \(Lh=0\). Interaction is always carried by at least one defect field \(e_i\). This is the second structural reason the Einstein Dirichlet theory cannot see it.
- **Charge-times-potential form.** Expand \(h_2\) in its decaying modes ("charges" \(q_2\)) and \(h_1\) near \(p_2\) in regular modes ("potentials" \(\Phi_1(p_2)\)). Then \(I_{12}=-2\langle q_2,\Phi_1(p_2)\rangle_{\mathcal W}\). This is the same Green-identity flux that produces \(\tfrac23W\circledast W+4tR\,\mathrm{mass}\) in Gursky–Viaclovsky §8.
- **Laplace analogue.** Two conductors held at equal potential have mutual capacitance below zero, so like Dirichlet data screen each other and lower the total energy. A fourth-order multi-channel \(\mathcal W\) has no maximum principle. The sign is therefore channel-dependent and must be computed.

### 4.4 Second order and core stiffness

The second-order remainder has two pieces:
- the excised energies \(-\int_{B_2}|e_1|^2-\int_{B_1}|e_2|^2\), which lower the cost;
- the relaxed mismatch energy for absorbing the incoming jets \(a_i\). For a core whose reduced interior cost has Hessian \(H\), this term lies between \(0\) (soft core) and \(\langle a,\Lambda a\rangle\) (stiff core).

By the envelope theorem, re-optimizing the core interiors does not change \(I_{12}\) at first order when the single-core data are stationary. Core stiffness enters only at second order, as a van der Waals-type balance between polarization and blocking.

For a frozen competitor (interiors held fixed), the formula is exact at first order whether or not \(y_*\) is stationary.

### 4.5 Size estimates

With \(\varepsilon=|y_*|\) on \(\Sigma\), the two-core cost minus twice the relaxed single-core cost (same interiors) is
\[
I_{12}+O\!\bigl(\varepsilon^2e^{-2\kappa d}\bigr)+O\!\bigl(\varepsilon^3e^{-\kappa d}\bigr).
\]
Single-core cubic terms cancel in this difference.

## 5. Separation, orientation, and symmetry

### 5.1 The configuration space

The witness is invariant under \(SU(2)_L\subset U(2)\), the left translations preserving the \(\sigma_i\). This group acts simply transitively on unit vectors at the core center. The direction from \(p_1\) to \(p_2\) is therefore immaterial. The relative orientation is the single angle \(\psi\) between core 2's \((\sigma_1,\sigma_2)\) frame and the frame transported from core 1, since \(U(2)/SU(2)_L=U(1)_R\).

By Schur's lemma, only the \(SU(2)_{L,p_2}\)-invariant part of \(h_1\) near \(p_2\) pairs with \(h_2\). The diagonal cell contains only:
- the \(U(1)_R\)-invariant biaxial ("monopole") part: lapse, \(\tfrac12(F+x)(\sigma_1^2+\sigma_2^2)\), and \(xe^w\sigma_3^2\);
- the quadrupole \(\tfrac12(F-x)(\sigma_1^2-\sigma_2^2)\).

Because only the \(\sigma_1\) slot collapses, the two have equal amplitude in that block. Hence
\[
I_{12}(d,\psi)=A_0(d)+|A_2(d)|\cos\bigl(2\psi-\phi(d)\bigr),
\qquad \min_\psi I_{12}=A_0-|A_2|,
\qquad \langle I_{12}\rangle_\psi=A_0 .
\]

### 5.2 Decay in \(d\)

Each \(A\) behaves like a polynomial in \(d\) (degree \(\le1\), from the doubled roots) times \(e^{-\kappa d}\), with \(\kappa\) the slowest coupled rate in its weight. If a coupled tensor channel had complex indicial roots, \(A(d)\) would alternate in sign with \(d\). The radial ODE decides whether this happens.

### 5.3 When the orientation average vanishes

Weight-0 data are fixed by all of \(U(2)\), and complex conjugation preserves the biaxial sector. So no isometry of CH forces \(A_0=0\).

Since \(\mathcal W(h^E,h^E)=0\), the average vanishes exactly when the \(\psi\)-averaged far field of each core is Einstein outside the core, i.e. it carries no weight-0 defect charge. The mechanism that would force this is integrability of the averaged tail, not symmetry.

### 5.4 The small-core law at separations of order the curvature radius

For \(t_2=\pi x_0\ll d\), core 2 sits in core 1's tail, which is a small non-Einstein perturbation of CH. Linear \(U(2)_{\hat\zeta}\) invariant theory fixes the response, exactly as in Step 8 §6:
- \(\Lambda^+\otimes\Lambda^-\) has no invariants, so traceless Ricci does not couple;
- odd jets have no invariants, since \(-1\in U(2)\);
- the scalar coupling of \(\int\!\tfrac14(s+4)^2\) uses \(\Delta\!\int s\,dV=-4\pi t+O(t^2)\) (Step 8 §5).

The result is
\[
\delta J_2=-8\pi t_2\Bigl[\delta W^+_1(\hat\zeta_2,\hat\zeta_2)+\tfrac{\delta s_1}{12}\Bigr](p_2)-2\pi t_2\,\delta s_1(p_2)+o(t_2).
\]

Averaging \(\hat\zeta_2\) over \(\omega^\perp\) replaces \(\hat\zeta\otimes\hat\zeta\) by \(\tfrac12(I-\hat\omega\hat\omega)\). This gives
\[
\langle\delta J_2\rangle_\psi=4\pi t_2\Bigl[\delta W^+_1(\hat\omega,\hat\omega)-\tfrac{\delta s_1}{6}\Bigr]-2\pi t_2\,\delta s_1 .
\]
- The \(P\)-part vanishes for any tail that is Kähler for \(J_{CH}\) to first order, because \(W^+(\hat\omega,\hat\omega)=s/6\) on Kähler metrics.
- What remains is the scalar coupling.
- The \(\psi\)-amplitude is \(8\pi t_2\) times the quadrupole of \(\delta W^+_1|_{\omega^\perp}\).
- The cell with \(\hat\zeta_2\) along the top eigenvector of \(\delta R^+_1(p_2)|_{\omega^\perp}\) gains whenever that eigenvalue exceeds the scalar coupling term.

The coefficient \(-2\pi t\) of the scalar coupling, and the validity of the response law in non-Einstein backgrounds, are derived here, not yet tested. They are fixed or refuted by the comparison in §7(iv).

### 5.5 Coulomb-gas form at second order

Combined with Step 8 §7.4, the cost of \(n\) small cores has the form
\[
J=8\pi^2 n-\sum_{i,j}t_it_j\,\langle\hat s_i,\mathcal G(p_i,p_j)\hat s_j\rangle+o(t^2),
\]
where \(\mathcal G\) is the Green operator of CH's background response. The diagonal entries are the self-margins: \(\eta\approx8.8\,x_0^2\) for the witness. The off-diagonal entries are the pair interactions.

Two consequences:
- Because the CH critical direction makes the single gain second order, the pair term is of the **same order** as the self-margin when \(d\sim1\).
- In the far-separation regime with fixed cut cores (\(x_c\sim2\), \(\kappa\) of order the volume entropy), the interaction is suppressed like \(\varepsilon^2e^{-\kappa d}\), roughly \(10^{-9}\). Meaningful nonadditivity lives at \(d=O(1)\) with small cores.

For clusters, the number of neighbours grows like \(e^{2\rho d}\) against pair decay \(e^{-\kappa_h d}\). If \(\kappa_h<2\rho\), the large-block limit \(\mathfrak J_{k,0}/k\) is governed by a homogenized orientation-density functional rather than by pairs. This is a distinct, unexplored regime.

## 6. Three different comparisons

1. **Beating twice the frozen witness: \(J<2J_*\).** This carries no information about interaction. Proposition 2 already shows the witness is non-stationary, and the monotone-in-\(X\) scan shows single-cell tail relaxation improves it. Any two-core competitor beats \(2J_*\) by \(2\delta_{\rm tail}\) plus \(I_{12}\), where \(\delta_{\rm tail}=J_{\rm tail}(y_*)-\min_{\rm ext}(y_*)\). It does improve the explicit coefficient \(\tfrac{28}9+J/(9\pi^2)\), with \(J\) replaced by the per-core pair cost.

2. **Nonadditivity at fixed cores.** Compare \(J_{\rm two}(d,\psi)\) with \(2J_{\rm one,relaxed}\), using identical interiors and optimally relaxed exteriors. The difference is \(I_{12}+\text{remainder}\). This is the quantity the computation in §7 measures.

3. **Nonadditivity relative to infima: \(\mathfrak J_{2,0}<2\mathfrak J_{1,0}\).** Subadditivity is automatic, using distant copies with exact collars. Strict inequality follows if all of the following hold for some minimizing sequence \(g_n\) of \(\mathfrak J_{1,0}\):
   - its tails stay uniformly in the linear regime beyond a fixed radius;
   - its charges \(q_n\) converge;
   - \(\min_\psi I(q_\infty;d,\psi)<0\) for some \(d\).

   Then one fixes \(d\) first and takes \(n\) large. If minimizing sequences instead spread their tails (\(X_n\to\infty\)) or degenerate in a way that sends the charges to zero, the statement becomes an overlapping-tail problem. Proposition 2 shows degeneration is unavoidable somewhere. The \(X\)-scan data in `perp_collar` tell which kind occurs.

## 7. A decisive computation from the frozen cell

**(i) Interface data.** From the exact dyadic profile, form at \(x_c\in\{0.1,0.2,0.4\}\) the 1-jet of \((G,F,xe^w)\) minus \(\bigl(x(1+x),x,x(1+x)\bigr)\). Split it into weight 0 (biaxial average) and weight 2 in \(\psi\) (\(\tfrac12(F-x)\)). The scalar charge is the Wronskian of \(\sigma\) at \(\Sigma\) against the regular radial solution of \(\nabla^*\nabla\sigma+6\sigma=0\).

**(ii) Linear exterior, weight by weight.** Expand the Cartan-verified diagonal Bianchi-IX density (`perp_cartan_verify.py`) to second order about CH. This gives two decoupled radial fourth-order boundary-value problems on \([t_c,\infty)\) with decay.
- The weight-2 sector has no gauge: \(SU(2)_L\)-invariant vector fields carry weights 0 and 1 only.
- The weight-0 sector has only the radial gauge. Geodesic gauge leaves one normal-displacement constant.
- Collocation with an exponential map gives \(h_1,e_1\), their indicial exponents, and \(Q^{\rm lin}(y_*)\).
- The comparison \(Q^{\rm lin}(y_*)\) versus the frozen tail cost separates \(\delta_{\rm tail}\) from interaction.

**(iii) Pairing.** In the Bergman ball model, each field is an explicit radial profile times tensors built from \(dr_i\), \(Jdr_i\), \(g_0\) and the transported \(SU(2)_L\) frame about \(p_i\). The Hessian of \(r_i\) is explicit on CH. Then \(I_{12}(d,\psi)=2\oint_S\mathcal W\) is a 3-dimensional quadrature over a geodesic sphere about \(p_2\), for \(d\in[0.7,2]\). No 4-dimensional solve is needed. Built-in consistency relations:
- the values on spheres about \(p_2\) and about \(p_1\) must be equal and opposite;
- the value must be independent of the sphere radius;
- the \(d\)-dependence must match the exponents found in (ii).

**(iv) Small-core cross-relation.** Repeat (i)–(iii) on the stored \(x_0\in\{0.003,0.01,0.03\}\) cells. The ratios \(A_0/t^2\) and \(A_2/t^2\) must converge to the transported response law of §5.4 evaluated on core 1's tail. The same Green kernel must reproduce \(\eta/x_0^2\approx8.8\) on the diagonal.

**(v) Reading the outcome.**
- \(A_0<0\) at some \(d\): generic-orientation attraction.
- \(0\le A_0<|A_2|\): attraction only near \(\psi^*=\phi/2\).
- \(A_0\ge|A_2|\) for all \(d\) in the window: no first-order gain. The question then moves to the second-order polarization/blocking balance or to the merged regime.

In the attractive case, the competitor of §1 with \(h=h_1+h_2+r\) is an actual 4-dimensional metric with only finite symmetry. Its excess over \(2J_{\rm one,relaxed}\) equals \(I_{12}\) (computable by Arb as a validated 3-dimensional integral of ODE-validated profiles) plus remainders \(O(\varepsilon^2e^{-2\kappa d}+\varepsilon^3e^{-\kappa d})\). These need an explicit coercivity bound for \(\Lambda\) on the complement of its kernel.

## 8. What remains open

- The tensor indicial rates of \(P\) on CH in weights 0 and 2, and whether any are complex.
- Whether slow Einstein tails lie in the energy closure, which determines \(\ker\Lambda\).
- The non-Einstein validity and the scalar coefficient of the transported response law.
- The coercivity constant needed to certify the remainders.
- The degeneration mode of minimizing sequences for \(\mathfrak J_{1,0}\).

Literature to consult:
- Biquard on Einstein desingularization and the \(\det\mathbf R^+=0\) obstruction, and on asymptotically complex-hyperbolic Einstein deformation theory;
- Ozuch on higher-order obstructions for trees of Einstein bubbles;
- Camporesi-type \(\tau\)-spherical functions on \(SU(2,1)/U(2)\), which would give the transport coefficients behind \(A_0(d)\) in closed form.