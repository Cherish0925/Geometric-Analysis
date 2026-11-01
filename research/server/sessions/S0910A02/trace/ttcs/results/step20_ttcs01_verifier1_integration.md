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
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step20_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step20_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

I am testing a proposed reduction of a 4D toric volume-gap question to a 2D Dirichlet eigenvalue question, for the Yau Problem 26 positive-branch crux on #_k(S^2 x S^2). Please verify the LOGIC and CORRECTNESS of the reduction and tell me exactly what the decisive 2D computation is, catching any gap. SETUP (see step13_preceptor_toric_spectral_review.md and step12/step14 notes): A T^2-invariant 4-metric g = g_B + p^2 dtheta^2 + q^2 dphi^2 over a 2D orbit space Omega (a curved polygon, geodesic edges, right-angle corners), with w = pq the orbit-area density, vanishing on partial Omega, positive inside. For exact Einstein Ric=g: -Delta_B w = 2 w (twist-free), so w is the Dirichlet ground state with eigenvalue 2; for delta-pinched positive metrics lambda_1^Dir(Omega, g_B) in [2(1-delta), 2(1+delta)]. Volume identity: Vol_4 = 4 pi^2 int_Omega w dA_B; and 2 int w = -int_{partial Omega} partial_nu w ds = total flux = sum of rod fluxes, where on a p-rod smooth toric closure gives |grad p| = 1 so partial_nu w = q there, i.e. rod flux = int_rod q ds (area of the collapsing 2-sphere). Gauss-Bonnet with right-angle corners pins int_Omega K_B dA = 2 pi - (pi/2) m, m = number of corners = chi(M) = 2k+2. Step 19 found a formal collapsing SEED: on even polygon m=2k+2 with alternating primitive labels, each rod has edge curvature K_B|edge = -A with A = m^2, transverse profile Q'' + (1+2A) Q = 0, rod length pi/sqrt(1+2A), rod flux 2/(1+2A), total flux ~ 1/m -> 0, base perimeter -> pi/sqrt(2). QUESTIONS: (1) Is it correct that the ENTIRE volume-gap fork reduces to whether a 2D disk with the pinned Gauss-Bonnet total, geodesic edges, right-angle corners, can sustain lambda_1^Dir approx 2 while int_Omega w (equivalently total flux, equivalently 4D volume) collapses to 0 as m -> infinity? (2) CRUCIAL: is int_Omega w really free to collapse independently, or is its scale fixed by the boundary normalization partial_nu w = (surviving fiber value) at each rod, so that the question is not a normalized eigenvalue question but a question about the ground state with GEOMETRICALLY FIXED Neumann data? Clarify whether lambda_1 approx 2 plus Area(Omega) >= c > 0 (Faber-Krahn, Step 14) already forces int w >= c' > 0, or whether a thin/concentrated w can have small integral while the eigenvalue stays near 2. (3) Does the negative-curvature-near-edges seed actually RAISE lambda_1 above 2(1+delta) (spectrally forbidding the collapse, giving a chi-uniform BUILD gap), or can strongly negative boundary-localized curvature keep lambda_1 approx 2 while shrinking the volume (BREAK candidate survives)? Give the sharpest rigorous statement you can about how lambda_1^Dir of a curved polygon responds to boundary-localized very negative curvature at fixed area, and whether McKean-type or curved-Faber-Krahn / total-curvature bounds decide it. Be concrete about which inequality is the right lever. Do NOT invent literature results; if a specific theorem is needed, name precisely what statement is required.

## Integrated Scientific Memo

## Verification verdict

The determinant and flux identities are correct in the **exact twist-free toric Einstein class**, but the proposed fork is **not reducible to a scalar Dirichlet eigenvalue problem**. The decisive two-dimensional object is a **geometrically normalized Dirichlet-to-Neumann flux problem for the full coupled reduced Einstein system**.

The Step 19 configuration is a valid local rod/corner seed. It does not yet show that a curved polygon carrying those collars admits a global ground state and fiber data satisfying all horizontal Einstein equations. Conversely, neither the eigenvalue bound, Gauss–Bonnet total curvature, nor boundary-localized negative curvature currently rules it out.

---

## 1. What is correct, and what must be corrected

For
\[
g=g_B+p^2d\theta^2+q^2d\phi^2,\qquad w=pq,
\]
with \(\operatorname{Ric}_g=g\), the supplied reduction gives
\[
-\Delta_Bw=2w,\qquad w>0\ \text{in }\Omega,\qquad w=0\ \text{on }\partial\Omega.
\]
Thus \(w\) is the Dirichlet ground state and
\[
\lambda_1^D(\Omega,g_B)=2.
\]

With outward normal \(\nu\),
\[
2\int_\Omega w\,dA
=-\int_{\partial\Omega}\partial_\nu w\,ds
=\sum_i\Phi_i,
\]
and
\[
\operatorname{Vol}_4
=4\pi^2\int_\Omega w\,dA
=2\pi^2\sum_i\Phi_i.
\]
On a \(p\)-rod, smooth primitive closure gives
\[
-\partial_\nu p=1,\qquad
-\partial_\nu w=q,
\]
so \(\Phi_i=\int_{\mathrm{rod}_i}q\,ds\). These identities are sound.

### Pinched case

In the **twist-free diagonal** setting, put
\[
a(x)=-\frac{\Delta w}{w}.
\]
Vertical Ricci pinching gives pointwise
\[
2(1-\delta)\le a(x)\le 2(1+\delta).
\]
The ground-state/Barta principle then yields
\[
2(1-\delta)\le\lambda_1^D(\Omega,g_B)
\le2(1+\delta).
\]
This is stronger than the Rayleigh upper-bound argument alone.

For a general invariant metric with twist,
\[
\left(-\Delta_B+\frac12|F|_h^2\right)w
=\bigl(\operatorname{tr}_V\operatorname{Ric}\bigr)w.
\]
The two-sided bracket applies to the ground eigenvalue of this Schrödinger operator. For the ordinary Laplacian one obtains directly only
\[
\lambda_1^D(-\Delta_B)\le2(1+\delta).
\]
Thus the clean scalar Dirichlet formulation requires twist-free/polar reduction. Exact simply connected toric Einstein metrics satisfy this; an arbitrary pinched metric does not automatically do so.

---

## 2. The fork is not “pinned Gauss–Bonnet plus \(\lambda_1\approx2\)”

The exact polar Einstein reduction includes
\[
-\Delta_Bw=2w,
\]
\[
\operatorname{div}_B(w\nabla v)=0,
\qquad v=\log(p/q),
\]
the horizontal traceless equation
\[
(\log w)_{zz}
+\frac12\left((\log w)_z^2+v_z^2\right)=0
\]
in conformal coordinates, and
\[
K_B=\frac14\left(|\nabla v|^2-|\nabla\log w|^2\right).
\]
These must be supplemented by primitive unit closure and the alternating rod singularities of \(v\).

Accordingly,
\[
\int_\Omega K_B\,dA
=2\pi-\frac{\pi}{2}m
\]
is a necessary compatibility identity, not an independently adjustable curvature prescription. A genuine solution must produce its own \(K_B\) from the fields and the base metric.

Therefore the correct invariant-class fork is:

> Do the full coupled reduced equations and smooth rod/corner closure admit \(m\to\infty\) solutions with
> \[
> -\int_{\partial\Omega}\partial_\nu w\,ds\to0,
> \]
> or do they force a positive lower bound independent of \(m\)?

Resolving this would settle the stated **polar toric subproblem**, not the general positive branch: reduction of arbitrary pinched collapse to invariant toric data remains separate.

---

## 3. The eigenfunction scale is free analytically but fixed geometrically

The scalar equation is homogeneous:
\[
w\mapsto cw
\]
preserves \(-\Delta w=2w\). In fact the displayed coupled interior equations are also unchanged if \(w\mapsto cw\) while \(v,g_B\) remain fixed, since they involve \(w\) linearly or only through derivatives of \(\log w\).

Hence \(\lambda_1=2\) alone cannot bound \(\int w\).

Smooth toric closure removes this global scaling freedom. Since
\[
p=\sqrt{w}\,e^{v/2},\qquad q=\sqrt{w}\,e^{-v/2},
\]
the replacement \(w\mapsto cw\) scales both fibers by \(\sqrt c\), changing the slope of every collapsing circle from \(1\) to \(\sqrt c\). Except at \(c=1\), this introduces a cone singularity.

But this does **not** imply a uniform flux lower bound. On a \(p\)-rod,
\[
-\partial_\nu w=q_{\rm surviving}.
\]
Unit closure normalizes the derivative of the collapsing fiber \(p\), not the size of the surviving fiber \(q\). The latter can in principle be small along all rods.

This is exactly what the Step 19 local profile demonstrates:
\[
Q(s)=\frac{\sin(\omega s)}{\omega},\qquad
\omega^2=1+2A,
\]
has endpoint slopes \(Q'(0)=1\), \(Q'(L)=-1\), but
\[
\int_0^LQ\,ds=\frac{2}{1+2A}.
\]
For \(A=m^2\), \(m\) rods have total formal flux
\[
\frac{2m}{1+2m^2}\sim\frac1m.
\]
Thus unit endpoint slopes alone do not prevent collapse.

The proper formulation is therefore a **corner-normalized Dirichlet-to-Neumann problem**, not a conventionally normalized eigenfunction problem:
\[
\mathcal F(w):=-\int_{\partial\Omega}\partial_\nu w\,ds,
\]
where normalization is imposed indirectly through simultaneous no-cone closure of \(p,q\) on every rod.

---

## 4. Area does not control \(\int w\)

Even if one knew
\[
\operatorname{Area}(\Omega)\ge c>0,
\]
it would not follow that
\[
\int_\Omega w\ge c'>0.
\]
Eigenvalues fix a base length scale, while \(\int w\) depends on the geometrically normalized amplitude of the fiber determinant. Without a Harnack, boundary-Harnack, Dirichlet-to-Neumann, or isoperimetric estimate tied to unit rod closure, these quantities are not comparable.

There is also a gap in the stated Step 14 Faber–Krahn constant. The Euclidean formula
\[
\lambda_1A\ge \pi j_{0,1}^2
\]
does not hold for an arbitrary curved polygon merely from the signed identity for \(\int K_B\). A valid area conclusion requires a uniform isoperimetric/Faber–Krahn theorem for the admissible base metrics. No such theorem is supplied.

Thus neither
\[
\lambda_1\approx2
\]
nor “\(\lambda_1\approx2\) plus base area bounded below” forces \(\int w\) away from zero.

---

## 5. What the Step 19 seed proves—and does not prove

The seed correctly passes:

- primitive alternating rod labels;
- right-angle local corner smoothness;
- the rod ODE
  \[
  Q''+(1-2K_B|_{\rm edge})Q=0;
  \]
- endpoint unit slopes;
- low-order corner Einstein matching;
- vanishing formal total rod flux.

It does **not** yet provide:

1. a global disk metric \(g_B\) containing all collars;
2. a positive global \(w\) satisfying \(-\Delta_Bw=2w\);
3. matching Neumann data
   \[
   -\partial_\nu w=Q_i
   \]
   on every rod;
4. a global solution \(v\) of \(\operatorname{div}(w\nabla v)=0\);
5. satisfaction of the horizontal traceless equation;
6. a global smooth four-metric with \(\|\operatorname{Ric}-g\|_{\rm op}\to0\).

Prescribing \(K_B|_{\rm edge}=-m^2\) is only local seed data. In a true solution this boundary curvature must arise self-consistently from \(w,v,g_B\).

---

## 6. Boundary-localized negative curvature does not by itself force \(\lambda_1\) upward

No supplied theorem implies that very negative curvature near the rods raises the first Dirichlet eigenvalue above \(2(1+\delta)\).

A simple rigorous reason is domain monotonicity. If an interior subdomain \(U\Subset\Omega\), disjoint from the bad collars, satisfies
\[
\lambda_1^D(U)\le2+\varepsilon,
\]
then
\[
\lambda_1^D(\Omega)\le\lambda_1^D(U)\le2+\varepsilon.
\]
Thus arbitrarily negative curvature confined near the boundary cannot force the full eigenvalue high when the interior retains an admissible low-Rayleigh-quotient region.

McKean-type bounds are not applicable here. Their relevant form requires global pointwise curvature control such as
\[
K\le-\kappa^2<0
\]
on a complete simply connected ambient surface. Large negative curvature only on rods or thin collars, possibly with sign-changing curvature elsewhere, does not meet that hypothesis.

Likewise, Gauss–Bonnet gives only
\[
\int_\Omega K_B\,dA
=2\pi-\frac{\pi}{2}m.
\]
It does not control the Cheeger constant, the isoperimetric profile of all subdomains, or \(\int K_B^\pm\) separately. Hence it cannot determine \(\lambda_1\).

A valid spectral obstruction would require, for example, a theorem deriving a uniform lower bound
\[
h(\Omega)^2/4>2(1+\delta)
\]
from the full admissible geometry, where \(h(\Omega)\) is the Cheeger constant. The currently known signed curvature total is insufficient to derive this.

The quantitative \(O(m^{-3})\) eigenvalue perturbation claimed in one branch is **not justified by the supplied data**. It assumes collar widths, ground-state bulk amplitude, and controlled metric perturbations not established by the seed. The rigorous conclusion is only that boundary-localized negative curvature is not, by itself, spectrally coercive; its actual eigenvalue effect requires construction of the global base metric and a controlled Rayleigh comparison.

A useful conditional obstruction remains: if the whole base had \(K_B\le0\) and supported the corresponding Cartan–Hadamard isoperimetric inequality, then the seed perimeter
\[
P_m\to\frac{\pi}{\sqrt2}
\]
would force small area. Combined with a valid Euclidean-type Faber–Krahn inequality, this would conflict with \(\lambda_1\approx2\). But the seed does not establish global \(K_B\le0\), and the many corner turnings and sign-changing curvature must be included explicitly.

---

## 7. The decisive 2D computation

For each even \(m=2k+2\), define the admissible class \(\mathcal A_m\) of polygonal disks and smooth reduced data
\[
(\Omega,g_B,w,v)
\]
satisfying:

\[
-\Delta_Bw=2w \quad\text{(or the precise pinched residual)},
\]
\[
\operatorname{div}_B(w\nabla v)=0,
\]
\[
(\log w)_{zz}
+\frac12\bigl((\log w)_z^2+v_z^2\bigr)=0,
\]
\[
K_B=\frac14\bigl(|\nabla v|^2-|\nabla\log w|^2\bigr),
\]
with \(w>0\) inside, \(w=0\) on the boundary, alternating primitive rod behavior, right-angle corners, and unit no-cone slopes for every collapsing circle.

The decisive number is
\[
I_m
=
\inf_{(\Omega,g_B,w,v)\in\mathcal A_m}
\left(
-\int_{\partial\Omega}\partial_\nu w\,ds
\right).
\]

Since
\[
\operatorname{Vol}_4=2\pi^2\mathcal F,\qquad
\mathcal F=-\int_{\partial\Omega}\partial_\nu w\,ds,
\]
the fork is exactly
\[
\inf_m I_m>0
\]
versus the existence of admissible data with
\[
I_m\to0.
\]

Equivalently, one must determine whether the Step 19 rod Neumann profiles belong to the Dirichlet-to-Neumann image of a global corner-normalized ground state that also satisfies the \(v\)-equation and horizontal traceless constraint.

For a numerical attack, the decisive outputs are not merely \(\lambda_1\), but:

- the residual of the horizontal traceless equation;
- the consistency residual between \(K(g_B)\) and
  \[
  \tfrac14(|\nabla v|^2-|\nabla\log w|^2);
  \]
- the spread of collapsing-circle slopes across all rods after one global scaling;
- the Neumann mismatch between \(-\partial_\nu w\) and the surviving-fiber rod profiles;
- the total normalized flux \(\mathcal F_m\).

The exact BUILD statement needed is a new uniform estimate:
\[
-\int_{\partial\Omega}\partial_\nu w\,ds\ge c_0>0
\]
for every solution of the full unit-closure reduced system, independently of \(m\). Neither Faber–Krahn, McKean, nor Gauss–Bonnet alone is this estimate.

Thus the seed survives all presently justified **local and purely spectral** tests, but its decisive global Dirichlet-to-Neumann/horizontal-Einstein compatibility remains unresolved.