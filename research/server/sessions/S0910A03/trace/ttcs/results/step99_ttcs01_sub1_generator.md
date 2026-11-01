# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md",
    "Sessions/S0910A03/workspace/notes/step92_full_jacobi_maxwell_and_remaining_collar.md",
    "Sessions/S0910A03/workspace/plans/step98_route_map.md"
  ]
}
```

## Task

Given the cost structure of the free-T² connector for Yau Problem 26:

1. Normal cost: bounded below by Raychaudhuri floor δ_min(R) ~ 12e^{-2R}
2. Tangential cost: conformal expansion gives 9.94·sech²(r) for the charged separator orbit shape
3. The exact Einstein germ (Koiso) has zero cost but is only defined locally

The critical unknown is the continuation domain of the exact Einstein germ from the charged Koiso center. If it extends to r = r₁, the best trial metric could achieve operator norm ~ max(δ_min(R), 9.94·sech²(r₁)) for a total cylinder of length R.

PROPOSE concrete mathematical strategies for either:
(A) Establishing that the Koiso germ has finite maximal continuation radius r_max, and estimating r_max from the data (S=1, Qmax=0.5, scalar curvature -7, orbit energy concentrated with von Mises parameter 800).
(B) Proving that the tangential cost cannot be made arbitrarily small by any trial (i.e., a genuine tangential obstruction).
(C) A completely different construction strategy that bypasses the Koiso center + expanding exterior framework.

The context includes the full development history of the free-T² connector problem over 96+ steps, including the Bochner/resolvent obstruction for exact OT connectors, the flat-slice barrier, and the charged Koiso separator construction.

## Output

The free-\(T^2\) connector now has a very sharp scientific bottleneck: the charged Koiso center removes Ricci cost exactly, but only for as long as the analytic Einstein Cauchy development remains usable. The important distinction is between two possible ways the exact germ can stop helping:

\[
\text{low-mode focusing of the separator direction}
\qquad\text{versus}\qquad
\text{high-mode elliptic Cauchy growth from the concentrated orbit data.}
\]

For the stored \(S=1\), \(Q_{\max}=0.5\), \(R(q_\Sigma)=-7\) center, both mechanisms have concrete quantitative signatures.

---

## A. Finite \(r_{\max}\): mechanisms and estimators

The exact germ in Gaussian normal form satisfies

\[
\partial_r q=2K,\qquad
\partial_rK=\operatorname{Ric}(q)+3q-HK+2Kq^{-1}K,
\]

with

\[
R(q)-H^2+|W|^2=-6,\qquad \operatorname{div}K=dH.
\]

At the charged Koiso center,

\[
H=0,\qquad |W|^2=S=1,\qquad R(q_\Sigma)=-7,
\]

and Step 96 gives the decisive Taylor data

\[
H_r=3-S=2,
\]

\[
a_r=0,\qquad a_{rr}=-(3+S+Q)=-(4+Q),
\]

\[
\sigma_r=0,\qquad \sigma_{rr}=6+Q.
\]

Thus the exact germ initially expands in volume while the separator-circle factor \(a\) contracts. At the point where \(Q=Q_{\max}=0.5\),

\[
a_{rr}=-4.5.
\]

Two crude center-only extrapolations already put a geometric event at order one, not at large \(R\):

\[
a(r)\approx 1-\frac12(4+Q)r^2
\quad\Rightarrow\quad
r\approx \sqrt{\frac{2}{4+Q}},
\]

so

\[
r\approx 0.667\quad(Q=0.5),
\qquad
r\approx 0.706\quad(Q\approx0).
\]

A constant-sectional-curvature Jacobi comparison

\[
a(r)\approx \cos(\sqrt{4+Q}\,r)
\]

gives instead

\[
r\approx \frac{\pi}{2\sqrt{4+Q}},
\]

hence

\[
r\approx 0.740\quad(Q=0.5),
\qquad
r\approx 0.785\quad(Q\approx0).
\]

These are not proofs, but they set the natural low-mode focusing scale. If the true \(r_{\max}\) is near \(0.7\)–\(0.8\), then the tangential cost remains large:

\[
9.94\,\operatorname{sech}^2(0.75)\approx 5.9.
\]

By contrast, to push tangential cost below \(10^{-2}\) one needs

\[
9.94\,\operatorname{sech}^2 r<10^{-2}
\quad\Rightarrow\quad
r\gtrsim 4.14.
\]

So a proof that the exact germ cannot pass even \(r\sim1\) would make the conformal-expansion trial irrelevant for small Ricci defect.

### A1. Validated Taylor/Pade continuation of the full \(3\times3\) Cauchy system

The most direct finite-radius test is not a radial model; it must use the full \(s\)-dependent matrix system. Write

\[
q(r,s)=\sum_{m\ge0}q_m(s)r^m,\qquad
K(r,s)=\sum_{m\ge0}K_m(s)r^m.
\]

The Einstein evolution recursively determines every \(q_m,K_m\) from the frozen analytic center data. The relevant observables are

\[
a^2=q_{ss}-q_{sA}G^{AB}q_{Bs},
\]

\[
\lambda_{\min}(q),\qquad
\lambda_{\min}(G),\qquad
|W|^2,\qquad |{\rm Rm}(g)|,
\]

and the constraint residuals reconstructed from the truncated series.

A real finite event can be certified by one of the following validated outcomes:

\[
a^2(r_*,s_*)=0,
\]

or

\[
\lambda_{\min}(q(r_*,s_*))=0,
\]

or interval enclosures showing curvature blow-up along a real ray. Complex Pade poles alone only locate analytic singularities in the complexified variables; they become geometrically decisive only when tied to a real SPD loss or real curvature divergence.

The concrete computation should use the stored Step-94/96 center data, not regenerated radial substitutes. For the concentrated von Mises parameter \(800\), a Taylor order around \(60\)–\(120\) with Fourier padding is natural, because the dangerous Fourier ridge will not be visible at \(N=48\) or \(64\).

A useful figure would show, as functions of Taylor order,

\[
r_m^{(q)}=\frac{\|q_m\|}{\|q_{m+1}\|},\qquad
r_m^{(K)}=\frac{\|K_m\|}{\|K_{m+1}\|},
\]

together with Pade pole clouds and the first real zero of the Schur complement \(a^2\). A stable cluster near \(0.7\)–\(0.8\) would support low-mode focusing; a cluster near \(0.08\)–\(0.15\) would indicate high-frequency elliptic growth.

### A2. High-frequency elliptic growth from the von Mises concentration

The normal Einstein Cauchy problem is elliptic in the \(s\)-direction. For a tangential Fourier mode \(k\), the principal normal growth has the form

\[
e^{\mu |k|r},
\]

with \(\mu\) read from the principal symbol of the linearized full-matrix system; for the scalar/map blocks one expects \(\mu=1\).

For a von Mises profile

\[
B_\kappa(s)=\frac{e^{\kappa\cos s}}{I_0(\kappa)},
\qquad \kappa=800,
\]

the central Fourier envelope satisfies, for the main range of modes,

\[
|\widehat B_\kappa(k)|\approx e^{-k^2/(2\kappa)}.
\]

After normal propagation,

\[
|\widehat B_\kappa(k;r)|
\approx
\exp\!\left(\mu |k|r-\frac{k^2}{2\kappa}\right).
\]

The maximizing mode is

\[
k_*(r)\approx \mu\kappa r,
\]

and the amplification is

\[
\exp\!\left(\frac12\mu^2\kappa r^2\right).
\]

For \(\kappa=800\), even with \(\mu=1\),

\[
r=0.02:\quad e^{0.16}\approx1.17,
\]

\[
r=0.10:\quad e^{4}\approx54.6,
\]

\[
r=0.20:\quad e^{16}\approx 8.9\times10^6.
\]

Thus Step 96’s short evolution at \(r=0.02\) lies well inside the harmless regime, while continuation to \(r=0.1\) already probes a very different scale.

If the peak-normalized concentrated part has effective Fourier amplitude \(A\), the order-one growth radius is approximately

\[
r_{\rm hf}\approx
\sqrt{\frac{2\log(A^{-1})}{\kappa}}.
\]

For plausible amplitudes,

\[
A=10^{-1}\Rightarrow r_{\rm hf}\approx0.076,
\]

\[
A=4.4\times10^{-2}\Rightarrow r_{\rm hf}\approx0.088,
\]

\[
A=10^{-2}\Rightarrow r_{\rm hf}\approx0.107.
\]

This is a second, much shorter candidate scale than the \(a\)-focusing estimate. The calculation that separates the two is the projection of the actual center data onto the growing eigenvectors of the full principal symbol. If the concentrated von Mises component projects strongly onto an unstable matrix direction, \(r_{\max}\) could be \(O(\kappa^{-1/2})\), not \(O(1)\).

### A3. Riccati/Sturm focusing for the separator-circle Jacobi field

The separator direction gives a geometric scalar observable. Along a normal geodesic, the horizontal variational field associated with \(\partial_s\) satisfies a matrix Jacobi/Riccati equation. In a gauge where the horizontal part is separated,

\[
\frac{a_r}{a}
\]

is the \(s\)-direction component of the shape operator, and

\[
a_{rr}+K_{\nu s}\,a=\text{coupling terms from the mixed connection and vertical block}.
\]

At the center the effective value is

\[
K_{\nu s}(0,s)=4+Q(s),
\]

because

\[
a_{rr}=-(4+Q)a.
\]

If the exact equations force the accumulated \(\nu s\)-sectional curvature to remain comparable to \(4+Q\) until the first focal event, then a Sturm comparison gives the same scale

\[
r_{\max}\lesssim \frac{\pi}{2\sqrt{4+Q_{\rm eff}}}.
\]

The nontrivial part is proving that the connection and orbit-shape terms cannot quickly reverse the sign of the \(a\)-equation. The quantities available for such a proof are

\[
H_r=3-|W|^2,
\]

the Hamiltonian constraint,

\[
R(q)-H^2+|W|^2=-6,
\]

and the quotient equations for \(\sigma,U,q\). The center has strong area acceleration,

\[
\sigma_{rr}=6+Q,
\]

so any rebound of \(a\) must be paid for by shear and vertical deformation. A useful scalar to monitor is

\[
\mathcal F(r)=
\int_{S^1}
\left[
\left(\frac{a_r}{a}\right)^2
+
|U_r|^2
+
|U_s|^2/a^2
+
Q
\right]\,a e^\sigma ds.
\]

A monotone or almost-monotone inequality for \(\mathcal F\) would turn the Taylor focusing signal into a theorem.

---

## B. A genuine tangential obstruction

A tangential floor cannot come merely from target displacement in \(\mathbb H^2\). A loop in \(\mathbb H^2\) can be contracted across a long cylinder with small pointwise tension if the rest of the Einstein system is ignored. Therefore a real tangential obstruction must use the coupled Einstein identities: Hopf/TT moments, target Killing currents, charge potential, and the shared center/end parameters.

The correct form is duality. Let \(F(V)\) denote the full normalized residual

\[
F=(H,T,Z,\mathcal B)
\]

from the reduced system, with \(H\) the horizontal Einstein block, \(T\) the area equation, \(Z\) the target equation, and \(\mathcal B\) the charge equation. For an adjoint field \(\Psi\),

\[
\|F(V)\|_\infty
\ge
\frac{|\langle \Psi,F(V)\rangle|}
{\|\Psi\|_{L^1}}.
\]

If \(\Psi\) solves the adjoint homogeneous equation, integration by parts converts the numerator into endpoint moment data plus finite parameter terms. A tangential floor exists exactly when, after optimizing over center phase/frame, charge direction, \(S\), and end shapes, some adjoint moment remains nonzero.

### B1. Hopf/TT moment

In conformal quotient coordinates \(z=r+is\), the tracefree horizontal Einstein equation is the natural partner of the Hopf differential of the coupled fields \((\sigma,U,q)\). Schematically,

\[
\Phi
=
\sigma_z^2-\sigma_{zz}
+
\frac12\langle U_z,U_z\rangle
+
\text{charge terms}.
\]

For exact solutions, Bianchi identities make the corresponding quadratic differential holomorphic up to the explicit charge forcing. Pairing with the constant quadratic differential \(dz^2\) gives a conserved or forced TT moment.

At the center,

\[
\sigma_r=\sigma_s=0,
\]

and in the standard determinant-one orbit metric normalization,

\[
R(q_\Sigma)=-\frac12|U_s|^2.
\]

Thus \(R(q_\Sigma)=-7\) corresponds to

\[
|U_s|^2=14.
\]

The \(S=1\) vertical tracefree Weingarten block corresponds, in the Koiso normalization, to normal target energy of size

\[
|U_r|^2\sim 2.
\]

So the raw Hopf anisotropy contains a large contribution of order

\[
|U_s|^2-|U_r|^2\sim 12,
\]

before normalization and before subtracting parameter directions. This is exactly the kind of quantity that can produce the observed numerical coefficient near \(9.94\).

A theorem here would have the following shape:

\[
\|F(V)\|_\infty
\ge
\eta_{\rm Hopf}
\left|
\Pi_{\mathcal P^\perp}
\mathcal M_{\rm Hopf}(V_{\rm center},V_{\rm ends})
\right|,
\]

where \(\mathcal P\) is the finite span generated by allowed shared parameters. The important number is the smallest singular value of the matrix of Hopf moments after projecting away those parameter derivatives. If it stays \(>0\) as \(R\to\infty\), the conformal expansion cannot drive the tangential cost to zero.

### B2. Target Killing current moments

For each Killing field \(Y\) of \(\mathbb H^2\), the target equation gives a Noether identity of the form

\[
\operatorname{div}_\sigma \langle dU,Y\rangle
=
-\langle\nabla_U Q,Y\rangle
+
\langle Z,Y\rangle.
\]

Here

\[
Q=\frac12 c^T e^{-3\sigma}M^{-1}c.
\]

The potential \(Q\) breaks the full \(\mathrm{PSL}(2,\mathbb R)\) symmetry down to the stabilizer of \(c\). Thus the three Killing currents separate three effects:

1. rotation of the orbit-shape loop in \(\mathbb H^2\);
2. target phase/frame matching;
3. charge-direction matching.

For the center curve \(U_0(s)\), define

\[
J_Y(0)=\int_{S^1}\langle U_s,Y(U)\rangle\,ds.
\]

For a loop winding around a hyperbolic circle, at least one rotation-type \(Y\) typically gives a nonzero current. The end OT region has \(U_s=0\), hence no corresponding current. The charge potential can supply part of the impulse,

\[
P_Y=\int_{\Omega}
\langle\nabla_U Q,Y\rangle\,d\mu_\sigma,
\]

but this term redshifts like \(e^{-3\sigma}\). A real obstruction is the nonvanishing of

\[
J_Y(0)-P_Y
\]

after optimizing the target isometry and charge frame. Numerically this is best represented as a three-vector in \(\mathfrak{sl}(2,\mathbb R)^*\), with the target frame acting by the coadjoint representation. Its Lorentzian norm is an invariant quantity; if that norm stays separated from zero, no slow conformal expansion can erase the current mismatch.

### B3. Global horizontal Noether fields

Step 96 showed that compactly supported local vector fields \(X\) give zero numerator on the exact fixed-charge germ:

\[
\frac12c^TK_Xc
=
\operatorname{div}_\sigma(QX)-m_c(X),
\qquad m_c=0.
\]

So the useful \(X\)’s must be global adjoint fields tied to both ends. The relevant object is a solution of the adjoint horizontal problem whose pairing with the center charge source is not a pure divergence after the end data are imposed.

The pairing has the schematic form

\[
\langle \Psi_X,F(V)\rangle
=
\mathcal N_X^{\rm center}
-
\mathcal N_X^{\rm ends}
+
\text{parameter terms}.
\]

A centered adjoint field with bounded \(L^1\)-norm as \(R\to\infty\) produces a genuine floor. An adjoint field escaping into the redshifted end gives no such floor, because the numerator and denominator scale together.

This distinction is visible in the linearized matching operator: the left singular field either remains near the Koiso center or drifts to the charge-taper zone. The first behavior supports a tangential obstruction; the second behavior supports a redshift near-kernel.

### B4. Compactness-to-Liouville formulation

A strong nonperturbative route is:

Assume a sequence of full-cylinder trials has

\[
\|F(V_j)\|_\infty\to0,
\qquad
R_j\to\infty,
\]

while the center traces converge to the charged Koiso data. After conformal/Coulomb gauge fixing, local elliptic estimates give a \(C^\infty_{\rm loc}\) limit on every finite \(r\)-interval. The limit is a complete exact free-\(T^2\) Einstein solution with the same charged Koiso center.

Then a tangential floor follows from a Liouville theorem:

\[
\text{no complete exact expanding two-sided free-}T^2
\text{ solution carries this center data.}
\]

The Liouville proof would use the Hopf moment, target Killing currents, and the Hamiltonian/Raychaudhuri identities. This formulation is powerful because it converts “all possible long trials” into one exact complete object.

---

## C. Different construction strategies

### C1. Let the torus action acquire smooth circle collapses

The free-\(T^2\) framework makes charge removal expensive because the coordinate charge is transported across a free cylinder. If one circle of the torus collapses smoothly, the charge can terminate through topology rather than through a redshifted taper.

This suggests replacing the free connector by a toric connector with rod data: primitive circle subgroups collapse along smooth fixed surfaces, and the connection holonomy changes by the corresponding integer vector. Exact or near-exact local models include hyperbolic space in toric polar coordinates, AdS soliton-type caps, Taub-Bolt-AdS geometries, and more general Plebanski–Demianski/Calderbank–Singer toric Einstein pieces.

The scientific mechanism is different:

\[
\text{charge removal by smooth degeneration}
\quad\text{instead of}\quad
dq\neq0\text{ on a free cylinder}.
\]

The observables are explicit:

\[
\text{rod vectors},\qquad
\text{period smoothness},\qquad
\text{holonomy jump},\qquad
\sup\|\operatorname{Ric}+3g\|_{\rm op}.
\]

If a toric collapse region can be made exact or exponentially close to exact, the Koiso separator is no longer needed.

### C2. Branched-cover or hyperbolization metrics with sectional pinching

A route completely outside the connector ansatz is to use closed manifolds already carrying metrics with sectional curvatures close to \(-1\). Then Ricci is automatically close to \(-3g\) in dimension four:

\[
\sec\in[-1-\varepsilon,-1+\varepsilon]
\quad\Rightarrow\quad
\operatorname{Ric}\in[-3-O(\varepsilon),-3+O(\varepsilon)]g.
\]

The needed topology is a no-Einstein smooth manifold. A promising source family is:

- Gromov–Thurston branched covers with pinched sectional curvature;
- Hirzebruch signature formulas for cyclic branched covers;
- LeBrun/Seiberg–Witten Einstein obstructions;
- Ontaneda smooth hyperbolization with pinched curvature.

For a cyclic \(d\)-fold branched cover along a surface \(\Sigma\), the topological quantities are governed by formulas of the type

\[
\chi(\widehat X)=d\chi(X)-(d-1)\chi(\Sigma),
\]

\[
\tau(\widehat X)
=
d\tau(X)
-
\frac{d^2-1}{3d}\,[\Sigma]^2.
\]

If the resulting smooth manifold violates a four-dimensional Einstein topological inequality while retaining a pinched curvature metric, this bypasses the entire free-\(T^2\) gluing problem.

The exact source search here is:

\[
\text{“Gromov--Thurston branched covers pinched sectional curvature signature formula Einstein obstruction”}
\]

and

\[
\text{“Ontaneda smooth hyperbolization four-manifolds Hitchin--Thorpe Einstein obstruction”.}
\]

### C3. Quantitative Ricci-flexibility / Lohkamp-type construction

Another route is to stop trying to approximate an Einstein metric and instead exploit flexibility of Ricci curvature. Lohkamp-type theorems show enormous freedom for constructing metrics with Ricci \(<0\) on many manifolds. The missing quantitative strengthening would be:

For a no-Einstein closed manifold \(M^n\), construct \(g\) with

\[
-(n-1+\varepsilon)g
\le
\operatorname{Ric}_g
\le
-(n-1-\varepsilon)g,
\]

or at least with both Ricci eigenvalue extremes lying inside a prescribed interval after scaling.

A possible construction uses local warped-product blocks with explicitly controlled Ricci eigenvalues, glued through layers whose Ricci tensors are kept inside the same interval. The model equations are elementary:

\[
g=dt^2+f(t)^2g_{S^p}+h(t)^2g_{S^q},
\]

with

\[
\operatorname{Ric}_{tt}
=
-p\frac{f''}{f}-q\frac{h''}{h},
\]

\[
\operatorname{Ric}_{S^p}
=
\frac{(p-1)(1-(f')^2)-ff''-qf f'h'/h}{f^2},
\]

and similarly for the \(S^q\) block. A library of such blocks could be assembled into handles while keeping Ricci eigenvalues in a fixed interval.

This is not a Koiso-center problem at all; it is a quantitative Ricci-prescription problem. The relevant source family is:

\[
\text{“Lohkamp Ricci curvature h-principle quantitative Ricci prescription”}.
\]

### C4. Two-scale orbit-shape microstructure

A more speculative construction remains within \(T^2\)-invariant geometry but abandons the single charged Koiso center. The idea is to generate the required separator scalar curvature through small-amplitude, high-frequency orbit-shape oscillations.

Near a point in \(\mathbb H^2\), set roughly

\[
U(s,r)\sim \varepsilon
\bigl(\cos ks,\sin ks\bigr),
\]

so

\[
|U_s|^2\sim \varepsilon^2k^2.
\]

To obtain the scalar contribution corresponding to

\[
R(q_\Sigma)=-7
\quad\Longleftrightarrow\quad
|U_s|^2\sim14,
\]

one may take

\[
\varepsilon k\sim\sqrt{14},
\qquad
\varepsilon\sim \frac{\sqrt{14}}{k}.
\]

Then the target displacement is only \(O(k^{-1})\), so the end matching problem is no longer a large orbit-shape transition. The hard part is that

\[
U_{ss}\sim \varepsilon k^2\sim \sqrt{14}\,k
\]

is large. A successful two-scale ansatz must cancel this large tension by adding an \(r\)-dependent phase/amplitude, for example

\[
U(r,s)\sim \varepsilon e^{-kr}
(\cos ks,\sin ks),
\]

together with conformal and area correctors solving the averaged Einstein equations.

The two-scale expansion would reveal whether the residual has the structure

\[
\|\operatorname{Ric}+3g\|_{\rm op}=O(k^{-1})
\]

after homogenization, or whether an \(O(1)\) tensor remains. If the \(O(1)\) terms cancel, this gives a connector whose smallness comes from microstructure rather than from a long exact Koiso germ.