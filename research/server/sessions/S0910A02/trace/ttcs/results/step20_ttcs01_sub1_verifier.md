# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step13_preceptor_toric_spectral_review.md",
    "Sessions/S0910A02/workspace/notes/step14_faberkrahn_reduced_system_and_fork.md",
    "Sessions/S0910A02/workspace/notes/step19_toric_rod_corner_matching_execute.md",
    "Sessions/S0910A02/workspace/notes/step12_toric_determinant_volume_gap_probes.md"
  ]
}
```

## Task

I am testing a proposed reduction of a 4D toric volume-gap question to a 2D Dirichlet eigenvalue question, for the Yau Problem 26 positive-branch crux on #_k(S^2 x S^2). Please verify the LOGIC and CORRECTNESS of the reduction and tell me exactly what the decisive 2D computation is, catching any gap. SETUP (see step13_preceptor_toric_spectral_review.md and step12/step14 notes): A T^2-invariant 4-metric g = g_B + p^2 dtheta^2 + q^2 dphi^2 over a 2D orbit space Omega (a curved polygon, geodesic edges, right-angle corners), with w = pq the orbit-area density, vanishing on partial Omega, positive inside. For exact Einstein Ric=g: -Delta_B w = 2 w (twist-free), so w is the Dirichlet ground state with eigenvalue 2; for delta-pinched positive metrics lambda_1^Dir(Omega, g_B) in [2(1-delta), 2(1+delta)]. Volume identity: Vol_4 = 4 pi^2 int_Omega w dA_B; and 2 int w = -int_{partial Omega} partial_nu w ds = total flux = sum of rod fluxes, where on a p-rod smooth toric closure gives |grad p| = 1 so partial_nu w = q there, i.e. rod flux = int_rod q ds (area of the collapsing 2-sphere). Gauss-Bonnet with right-angle corners pins int_Omega K_B dA = 2 pi - (pi/2) m, m = number of corners = chi(M) = 2k+2. Step 19 found a formal collapsing SEED: on even polygon m=2k+2 with alternating primitive labels, each rod has edge curvature K_B|edge = -A with A = m^2, transverse profile Q'' + (1+2A) Q = 0, rod length pi/sqrt(1+2A), rod flux 2/(1+2A), total flux ~ 1/m -> 0, base perimeter -> pi/sqrt(2). QUESTIONS: (1) Is it correct that the ENTIRE volume-gap fork reduces to whether a 2D disk with the pinned Gauss-Bonnet total, geodesic edges, right-angle corners, can sustain lambda_1^Dir approx 2 while int_Omega w (equivalently total flux, equivalently 4D volume) collapses to 0 as m -> infinity? (2) CRUCIAL: is int_Omega w really free to collapse independently, or is its scale fixed by the boundary normalization partial_nu w = (surviving fiber value) at each rod, so that the question is not a normalized eigenvalue question but a question about the ground state with GEOMETRICALLY FIXED Neumann data? Clarify whether lambda_1 approx 2 plus Area(Omega) >= c > 0 (Faber-Krahn, Step 14) already forces int w >= c' > 0, or whether a thin/concentrated w can have small integral while the eigenvalue stays near 2. (3) Does the negative-curvature-near-edges seed actually RAISE lambda_1 above 2(1+delta) (spectrally forbidding the collapse, giving a chi-uniform BUILD gap), or can strongly negative boundary-localized curvature keep lambda_1 approx 2 while shrinking the volume (BREAK candidate survives)? Give the sharpest rigorous statement you can about how lambda_1^Dir of a curved polygon responds to boundary-localized very negative curvature at fixed area, and whether McKean-type or curved-Faber-Krahn / total-curvature bounds decide it. Be concrete about which inequality is the right lever. Do NOT invent literature results; if a specific theorem is needed, name precisely what statement is required.

## Output

## Verification memo: toric volume gap vs. 2D eigenvalue data

### 1. Algebraic reduction: mostly correct, with two important qualifications

For a **polar/diagonal** \(T^2\)-invariant metric
\[
g=g_B+p^2d\theta^2+q^2d\phi^2,\qquad w=pq,
\]
the exact Einstein normalization \(\operatorname{Ric}=g\) gives
\[
-\Delta_B w=2w,\qquad w>0\text{ in }\Omega,\qquad w=0\text{ on }\partial\Omega.
\]
Since \(w\) is positive, \(2=\lambda_1^D(\Omega,g_B)\).

The flux/volume identities are also correct:
\[
\operatorname{Vol}_4=4\pi^2\int_\Omega w\,dA_B,
\]
and
\[
2\int_\Omega w\,dA_B
=
-\int_{\partial\Omega}\partial_\nu w\,ds
=
\sum_i \Phi_i,
\]
where on a \(p\)-rod,
\[
-\partial_\nu w=q,
\qquad 
\Phi_i=\int_{\text{rod }i} q\,ds.
\]
Thus
\[
\operatorname{Vol}_4=2\pi^2\sum_i\Phi_i.
\]

For a diagonal \(\delta\)-pinched metric, writing
\[
a(x):=-\frac{\Delta_B w}{w}=\operatorname{tr}_{\mathrm{vertical}}\operatorname{Ric},
\]
one has
\[
2(1-\delta)\le a(x)\le 2(1+\delta).
\]
Because \(w>0\), the ground-state transform gives
\[
2(1-\delta)\le \lambda_1^D(\Omega,g_B)\le 2(1+\delta).
\]
So the interval statement is valid in the diagonal/twist-free setting.

However, for a general \(T^2\)-invariant metric with twist,
\[
\left(-\Delta_B+\frac12|F|_h^2\right)w
=
\operatorname{tr}_{\mathrm{vertical}}\operatorname{Ric}\, w.
\]
Then the bracket applies naturally to the Schrödinger operator
\[
-\Delta_B+\frac12|F|_h^2,
\]
while the ordinary Dirichlet eigenvalue of \(-\Delta_B\) only has the easy upper estimate
\[
\lambda_1^D(\Omega,g_B)\le 2(1+\delta).
\]
So the clean Dirichlet formulation is correct only after polar/diagonal reduction or exact twist-vanishing.

---

### 2. The volume-gap problem is not a plain normalized eigenvalue problem

The statement

\[
\lambda_1^D(\Omega,g_B)\approx 2
\]

fixes a **base length scale**. It does not fix the amplitude of the eigenfunction \(w\). As an abstract Dirichlet eigenfunction, if \(w\) solves
\[
-\Delta_B w=2w,
\]
then so does \(\varepsilon w\), and
\[
\int_\Omega \varepsilon w=\varepsilon\int_\Omega w
\]
can be made arbitrarily small.

The toric metric removes this scalar freedom through smooth rod/corner normalization:

- near a \(p\)-rod, \(p\sim r\), so \(|\nabla p|=1\);
- hence
  \[
  -\partial_\nu w=q;
  \]
- near a right-angle fixed point with adjacent rods \(p=0\), \(q=0\),
  \[
  p\sim x,\qquad q\sim y,\qquad w\sim xy.
  \]

Thus the relevant 2D problem is not:

\[
\lambda_1^D\approx 2
\quad\text{plus some normalization such as }\|w\|_{L^2}=1.
\]

It is instead a **corner-normalized Dirichlet-to-Neumann flux problem**:

\[
-\Delta_B w=2w,\qquad 
w|_{\partial\Omega}=0,\qquad 
w\sim xy\text{ at every right-angle corner},
\]
with
\[
\mathcal F(\Omega,g_B,w)
:=
-\int_{\partial\Omega}\partial_\nu w\,ds
=
\sum_i\Phi_i.
\]

The volume gap in the polar toric class is equivalent to asking whether
\[
\mathcal F\ge c>0
\]
uniformly over the admissible reduced systems, or whether one can find
\[
\mathcal F_m\to0
\]
as \(m=\chi\to\infty\).

So the amplitude of \(w\) is not freely scalable inside the toric metric, but it is also not fixed by \(\lambda_1^D\) alone. It is fixed by the rod/corner geometry.

---

### 3. Faber–Krahn area pinning does not by itself give a volume lower bound

Even if one had
\[
\operatorname{Area}(\Omega,g_B)\ge c>0,
\]
this would not imply
\[
\int_\Omega w\,dA_B\ge c'>0
\]
without further geometric input.

Reason: \(\lambda_1^D\) and area concern the base metric. The volume uses the **corner-normalized ground state amplitude**. A lower area estimate does not prevent the ground state from being small on most of the area unless one also has uniform Harnack/Carleson-type control, an isoperimetric profile, or a Dirichlet-to-Neumann lower estimate tied to the rod data.

There is also a separate issue: the Step 14 numerical Faber–Krahn constant
\[
\operatorname{Area}(\Omega)\ge \frac{\pi j_{0,1}^2}{2(1+\delta)}
\]
does not follow for an arbitrary curved polygon. The Euclidean Faber–Krahn inequality, or its curved analogues, require an isoperimetric theorem for the metric \(g_B\). The supplied hypotheses give
\[
\int_\Omega K_B\,dA
=
2\pi-\frac{\pi}{2}m,
\]
but that single Gauss–Bonnet number is not an isoperimetric profile.

A usable replacement would be a statement of the form:

\[
\operatorname{Length}(\partial D)^2
\ge I_0\,\operatorname{Area}(D)
\quad\text{for every regular }D\Subset\Omega,
\]
with \(I_0>0\) independent of \(m\). From such an estimate one can derive a Faber–Krahn lower estimate. Without it, \(\lambda_1^D\le 2(1+\delta)\) does not supply a robust area lower bound.

---

### 4. The Step 19 rod seed passes only local one-dimensional tests

The local rod model
\[
K_B|_{\text{rod}}=-A,\qquad A=m^2,
\]
gives
\[
Q''+(1+2A)Q=0,
\]
with
\[
L_m=\frac{\pi}{\sqrt{1+2m^2}},
\qquad
\Phi_i=\int_0^{L_m}Q(s)\,ds=\frac{2}{1+2m^2}.
\]
Hence
\[
\sum_{i=1}^m\Phi_i
=
\frac{2m}{1+2m^2}
\sim \frac1m.
\]

This correctly shows that **unit endpoint slopes do not alone force a rod-flux lower bound**. Short rods with large \(|K_B|\) can have small flux while satisfying
\[
Q(0)=Q(L)=0,\qquad Q'(0)=1,\qquad Q'(L)=-1.
\]

But this is not yet a global reduced Einstein construction. The missing compatibility is:

1. a global \(g_B\) on the polygon;
2. a positive \(w\) satisfying \(-\Delta_B w=2w\);
3. rod normal data
   \[
   -\partial_\nu w=Q_i
   \]
   matching the one-dimensional rod profiles;
4. the horizontal/traceless equations, equivalently the coupled \(p,q\) system:
   \[
   \Delta_Bp=(K_B-1)p,\qquad
   \Delta_Bq=(K_B-1)q,\qquad
   \langle\nabla p,\nabla q\rangle=-K_Bpq.
   \]

So the Step 19 seed is a strong local certificate, but not yet a global toric metric or even a global 2D reduced solution.

---

### 5. Does \(K_B\ll0\) near rods force \(\lambda_1^D\) above \(2\)?

Not from the supplied data.

There are three relevant spectral facts.

#### 5.1. Domain monotonicity gives an immediate upper mechanism

If \(\Omega\) contains a subdomain \(U\) with
\[
\lambda_1^D(U,g_B)\le 2+\varepsilon,
\]
then
\[
\lambda_1^D(\Omega,g_B)\le 2+\varepsilon.
\]
A region with \(K_B\ll0\) confined near \(\partial\Omega\) cannot by itself force the full \(\lambda_1^D(\Omega)\) above \(2+\varepsilon\), because test functions may live in the interior subdomain \(U\).

Thus localized curvature below zero is not spectrally fatal unless it changes the global isoperimetric geometry seen by all test functions.

#### 5.2. McKean-type estimates require pointwise global curvature control

A McKean estimate has the form:

If a complete simply connected surface satisfies
\[
K\le -\kappa^2<0
\]
everywhere, then
\[
\lambda_1^D(\Omega)\ge \frac{\kappa^2}{4}
\]
for every compact domain \(\Omega\).

If one had \(K_B\le -cm^2\) throughout the whole base, then \(\lambda_1^D\) would grow like \(m^2\), contradicting \(\lambda_1^D\approx2\). But Step 19 only prescribes large \(|K_B|\) along rods/local collars. McKean does not apply to curvature concentrated near \(\partial\Omega\) or to sign-changing metrics.

#### 5.3. Gauss–Bonnet total curvature does not decide the spectrum

The identity
\[
\int_\Omega K_B\,dA
=
2\pi-\frac{\pi}{2}m
\]
forces the total curvature integral to become large in magnitude as \(m\to\infty\). But \(\lambda_1^D\) is controlled by Rayleigh quotients and isoperimetric geometry, not by \(\int K_B\) alone.

To turn curvature information into a spectral lower estimate one needs something like:

\[
h(\Omega)^2/4>2(1+\delta),
\]
where
\[
h(\Omega)
=
\inf_D
\frac{\operatorname{Length}(\partial D)}{\operatorname{Area}(D)}
\]
is the Cheeger constant, or a stronger Faber–Krahn profile for all subdomains \(D\).

The Gauss–Bonnet number alone does not provide such an \(h(\Omega)\) estimate.

---

### 6. A useful conditional observation about the Step 19 perimeter

The Step 19 model has total rod perimeter
\[
P_m=mL_m\to \frac{\pi}{\sqrt2}.
\]

If, in addition, the base satisfied a uniform Cartan–Hadamard-type isoperimetric inequality
\[
P^2\ge 4\pi A,
\]
then
\[
A\le \frac{P_m^2}{4\pi}\to \frac{\pi}{8}\approx0.393.
\]
That is incompatible with the Euclidean Faber–Krahn consequence of \(\lambda_1^D\approx2\), which would require area of order \(9\).

So an all-\(K_B\le0\) version of the Step 19 seed with small perimeter would be spectrally obstructed if the needed isoperimetric theorem applied.

But the supplied reduced data do not prove such an isoperimetric inequality. A collapsing construction could try to place the large curvature-below-zero contribution in thin collars while using other regions to tune \(\lambda_1^D\). Whether the full horizontal system permits that is exactly the unresolved 2D issue.

---

### 7. The decisive 2D computation

The decisive computation is **not** simply computing \(\lambda_1^D(\Omega,g_B)\).

It is the following corner-normalized flux minimization problem over the full reduced toric system.

For \(m=2k+2\), consider admissible polygonal disks with alternating primitive labels and right-angle corners. Find whether there exist smooth reduced data
\[
(\Omega_m,g_{B,m},p_m,q_m)
\]
such that

\[
w_m=p_mq_m>0,\qquad w_m|_{\partial\Omega_m}=0,
\]
\[
-\Delta_{B,m} w_m=2w_m+o(1),
\]
\[
p_m,q_m \text{ satisfy unit rod closure at every edge},
\]
\[
K_{B,m}=\frac14\left(|\nabla v_m|^2-|\nabla\log w_m|^2\right),
\qquad v_m=\log(p_m/q_m),
\]
or equivalently
\[
\Delta p_m=(K_{B,m}-1)p_m+o(1),
\]
\[
\Delta q_m=(K_{B,m}-1)q_m+o(1),
\]
\[
\langle\nabla p_m,\nabla q_m\rangle=-K_{B,m}p_mq_m+o(1),
\]
with
\[
\int_{\Omega_m}K_{B,m}\,dA
=
2\pi-\frac{\pi}{2}m+o(1).
\]

Then compute the geometrically normalized flux
\[
\mathcal F_m
=
-\int_{\partial\Omega_m}\partial_\nu w_m\,ds
=
\sum_i\int_{\text{rod }i}Q_i\,ds.
\]

The fork is exactly:

\[
\inf_m \mathcal F_m>0
\]
versus
\[
\mathcal F_m\to0.
\]

In the first case, the polar toric volume satisfies
\[
\operatorname{Vol}_4=2\pi^2\mathcal F_m\ge c>0.
\]
In the second case, the Step 19 collapsing rod mechanism survives the global 2D reduced equations.

The main missing scientific object is therefore the **Dirichlet-to-Neumann compatibility of the corner-normalized ground state with the rod ODE and horizontal traceless equation**. The local rod/corner jets do not settle that compatibility; the scalar eigenvalue alone also does not.