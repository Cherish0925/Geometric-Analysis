# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/data/step28/ak_nu_structure.json",
    "Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json",
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md",
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Knowledge/objects/papers/Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7--68f3db154d35/object.md"
  ]
}
```

## Task

Research goal context: the session studies the scale-invariant Einstein defect on closed four-manifolds and, centrally, the optimal cost of an exceptional (-1)-sphere cell inserted into a complex-hyperbolic (CH) background; a certified perpendicular diagonal cell has Phat=P/(8pi^2)<1 (best floating ~0.99518), disproving universal coefficient 4, but no matching lower bound exists. Theorem A in the supplied note gives, for diagonal exact-CH perpendicular cells, the exact identity Phat-1=12H+6G+(3/2)Qdelta+(1/2)QA-(3/2)N+Sigma, where only the nonintegrability N of the canonical almost-Kahler structure (conformal factor u, ghat=u^2 g) is negative; nu is forced by the bolt (charge K, linear transport lambda=nu_T/2+beta*nu, far-field Hardy positivity beyond sinh^2 R~5.9; at the bolt the 6G and (3/2)N densities cancel). Generate the strongest mathematically concrete routes by which this structure could yield (a) a quantitative lower bound Phat>=1-kappa for diagonal cells with explicit small kappa (ideally of the observed order 0.005), e.g. a near-zone inequality coupling nu, (log 1/u)_T, lambda and the Yamabe equation 6 Lap_hat v + shat v + 24 v^3=0 (v=1/u), a Bogomolny/calibration completion, an optimal-control or Sturm-Liouville reduction with the forced charge K, or an obstruction showing why no such inequality can hold without global information; (b) a symmetry-free extension to arbitrary exact-CH cells using the closed self-dual form extending the CH Kahler form, its modulus a=int_E omega, its near-symplectic zero set, and the U(2) splitting with W2 and W3, unifying aligned Kahler cells (a>0; Kahler formula P=2(2pi+6t)^2+L/4) with perpendicular cells (a=0); derive the expected a-dependent pinning and Chern terms and test them against the known Kahler cell formula; (c) consequences for collapsed/large-bolt degenerations (where H, G, N, QA, Qdelta should be evaluated on Taub-bolt-like prefixes) and for multi-cell or mixed blow-up/handle interactions. For each route give the key equations, what would be proved, what decisive calculation would test it, and what would falsify it. Do not invent literature; name precise knowledge requests if needed.

## Output

## 1. The sharp diagonal problem retains two global transport constraints, not just the bolt charge

There is a useful form of Theorem A in which the Yamabe coupling and the bolt cancellation are explicit. Write
\[
v=u^{-1},\qquad r=(\log v)_T,\qquad
w=A_fA_gA_h,\qquad L=(\log w)_T.
\]
All integrals in this section use the radial normalization \(d\hat V=w\,dT\). Then
\[
H=\int (v^2-1)^2w\,dT,\qquad G=\int r^2w\,dT.
\]
With \(\Delta_0=\operatorname{div}\nabla\), the scalar-normalization equation is
\[
-6\Delta_0v+\hat s v+24v^3=0.
\]
Thus, for \(s_g=-24\),
\[
\hat s=6(r_T+r^2+Lr)-24v^2,
\]
and
\[
\delta=\widehat W^+_{\omega\omega}+4
=r_T+r^2+Lr+\nu^2+4(1-v^2).
\]
The exact functional becomes
\[
\boxed{
\widehat P-1
=\int w\left[
12(v^2-1)^2+6(r^2-\nu^2)
+\frac32\delta^2
+\frac12(\nu_T+2\beta\nu)^2
\right]dT.}
\tag{1}
\]
This is a coupled scalar–transport problem. Treating \(r,\nu,\beta,w\) as independent functions discards much of its geometry.

### A regular charge representation

Let
\[
\mu_T=2\beta\mu,\qquad h=\mu\nu,\qquad k=\mu r,\qquad
\rho=\frac{w}{\mu^2}.
\]
Then
\[
\frac12Q_A=\frac12\int \rho h_T^2\,dT,\qquad
6G-\frac32N=6\int\rho(k^2-h^2)\,dT.
\]
At the perpendicular bolt,
\[
r\sim\nu\sim-\frac1{3T},\qquad
w\asymp T^{5/3},\qquad \mu\asymp T,
\]
so
\[
h(0)=k(0)=K,\qquad \rho\asymp T^{-1/3}.
\]
These variables preserve the cancellation without subtracting two singular pointwise expressions.

The transport energy alone has the capacitary estimate
\[
\boxed{
\frac12Q_A\ge
\frac{K^2}{2\displaystyle\int_0^{T_c}\mu^2/w\,dT}.}
\tag{2}
\]
The quotient is unchanged by multiplying \(\mu\) by a constant. Consequently, the numerical size of \(K\) alone is not the relevant invariant; its capacitary quotient is.

### A second exact constraint forces \(\nu\) to change sign

The contact-slot equation contains information independent of (2). Set
\[
y=\tanh(q/2),\qquad
\eta_T=\frac4{A_f}\eta.
\]
The formula for \(\nu\) gives
\[
\boxed{
y_T+\frac4{A_f}y=-\nu(1-y^2).}
\tag{3}
\]
Since \(y(0)=1\) at the perpendicular bolt and \(y(T_c)=0\) on the CH collar,
\[
\boxed{
\int_0^{T_c}\eta\nu(1-y^2)\,dT=\eta(0)>0.}
\tag{4}
\]
Because \(\nu<0\) near the bolt, every such cell has a region where \(\nu>0\). This sign change is not an optional feature of the numerical profile: it follows from the exact contact-slot transport.

Equations (2) and (4) explain why a one-charge estimate can miss the sharp cost. The \(W_3^+\) transport must both remove the bolt value of \(h\) and create sufficient oppositely signed \(\nu\) to bring \(q\) to zero.

For frozen geometric coefficients, minimizing
\[
\frac12\int\rho h_T^2
\]
with prescribed \(h(0)\), \(h(T_c)\), and the linearized version of (4) is an explicit two-constraint problem. Its minimum is a quadratic form obtained from the Gram matrix of the corresponding Green representers. The nonlinear problem retains the factor \(1-y^2\), together with
\[
v_T/v=k/\mu,\qquad
y_T+4y/A_f=-(h/\mu)(1-y^2),
\]
and the almost-Kähler structural equations for \(\mathcal P\).

**What this could prove.** A uniform estimate for the coupled capacity matrix, plus the Yamabe relation, could bound the total gain in (1) rather than merely bounding \(N\).

**Decisive calculation.** The two-constraint transport minimum on the supplied profiles would reveal how much of their \(Q_A\) is already forced by bolt charge and contact closure. A large discrepancy would identify additional geometric coupling that the sharp estimate must retain.

---

## 2. Sharpness requires the tail impedance, not just its positivity

The supplied \(x_0=.038\) profile is particularly informative. Its inner contribution is approximately
\[
0.06009-0.07068=-0.01059,
\]
whereas the outer Nijenhuis sector returns approximately
\[
+0.00588.
\]
Thus an argument that discards the outer contribution after proving it is \(\ge0\) loses a quantity comparable to the entire observed saving. Even for this one profile, such an argument naturally gives a number near \(0.0106\), not \(0.005\).

The stronger object is an effective tail action.

### Sturm–Liouville tail reduction

For fixed \(w,\beta\), define
\[
\mathcal Q_\nu
=\frac12\int w(\nu_T+2\beta\nu)^2\,dT
-6\int w\nu^2\,dT.
\]
Its Euler equation is
\[
-\frac1w(w\nu_T)_T+
\left(4\beta^2-2\beta_T-2\beta L-12\right)\nu=0.
\tag{5}
\]
For a minimizing tail with \(\nu(T_c)=0\), its action is
\[
\mathcal Q_{\nu,\mathrm{tail}}
=-\frac12w(T_*)\nu(T_*)
\bigl[\nu_T(T_*)+2\beta(T_*)\nu(T_*)\bigr].
\tag{6}
\]
This is a Dirichlet-to-Neumann quadratic form. Its impedance can be computed through the Riccati equation associated with (5).

However, prescribing only \(\nu(T_*)\) is still incomplete. Equation (3) also requires the tail to remove \(q(T_*)\). In the linear CH model,
\[
q_T+\frac4{A_f}q=-2\nu,
\]
and hence
\[
\eta(T_*)q(T_*)=
2\int_{T_*}^{T_c}\eta\nu\,dT.
\tag{7}
\]
The natural tail action is therefore a \(2\times2\) quadratic form in
\[
\bigl(q(T_*),\nu(T_*)\bigr),
\]
with additional entries when the scalar and radial geometry are allowed to vary.

### An exact CH square completion

There is a useful factorization that distinguishes geometric transport from an arbitrary weighted Hardy problem. Put
\[
\ell=\frac{A_f}{A_gA_h},\qquad B=2\beta-\ell.
\]
The supplied formula for \(\widehat D\) is
\[
\widehat D=2\nu_T+(-4\beta+4\ell)\nu.
\]
Direct integration by parts gives
\[
\boxed{
\mathcal Q_\nu
=\frac18\int w\widehat D^2\,dT
+[wB\nu^2]
+\int w\Xi\nu^2\,dT,}
\tag{8}
\]
where
\[
\Xi=4\beta\ell-2\ell^2-6-B_T-LB.
\tag{9}
\]
On CH,
\[
A_f=\sqrt{x(1+x)},\quad A_gA_h=x,\quad
\beta=\frac{3-2x}{2\sqrt{x(1+x)}},
\]
and
\[
B=\frac{2-3x}{\sqrt{x(1+x)}}.
\]
These coefficients satisfy exactly
\[
B_T+LB=4\beta\ell-2\ell^2-6,
\]
so \(\Xi=0\). Thus, for compactly supported variations on the CH geometry,
\[
\boxed{\mathcal Q_\nu=\frac18\int w\widehat D^2\,dT.}
\tag{10}
\]
The apparently attractive \(-6\nu^2\) term does not create gain from an arbitrary CH-supported squashing variation. Gain requires the coupled deformation of the radial geometry, conformal factor, and bolt data.

Formula (8) cannot simply be integrated through the conical almost-Kähler bolt: its displayed pieces separately diverge there. The original-metric combination is regular:
\[
\boxed{
v^2D_g=\widehat D-2r q_T,\qquad
\frac18\int D_g^2\,dV_g
=\frac18\int(\widehat D-2rq_T)^2\,d\hat V.}
\tag{11}
\]
This is a promising square for a full completion, because the conformal Hessian term removes the bolt singularity.

**What this could prove.** A completion retaining (11), a controlled deformation remainder \(\Xi\), and the coupled tail impedance could yield
\[
\widehat P\ge1-\kappa
\]
with a small \(\kappa\) derived from an inner variational problem.

**Distinguishing observation.** A family with increasing inner gain but vanishing tail impedance would contradict this mechanism as a source of an order-\(0.005\) estimate. Conversely, a uniformly positive two-variable impedance would explain why the observed saving is much smaller than the inner gain.

---

## 3. A global calibration can be formulated directly in the scalar-normalized Ricci controls

The almost-Kähler identity explains the mechanism; a Hamilton–Jacobi calibration could supply a rigorous numerical constant without assuming compactness of near-minimizers in advance.

Let
\[
y_i=a_i'/a_i,\qquad S=y_f+y_g+y_h,
\]
and let \(P_i\) denote the intrinsic Ricci eigenvalues of the orbit metric. For scalar curvature \(-24\),
\[
C=\frac12\left(S^2-\sum_i y_i^2-R^{(3)}-12\right).
\tag{12}
\]
Thus \(C\) is a state function, not an independent control. The two independent controls are \(E,D\), with
\[
\begin{aligned}
y_f'&=P_f-Sy_f+6+C/3-2E/3,\\
y_g'&=P_g-Sy_g+6+C/3+E/3-D/2,\\
y_h'&=P_h-Sy_h+6+C/3+E/3+D/2.
\end{aligned}
\tag{13}
\]
The action density is
\[
\mathcal L=W\left(C^2/3+E^2/6+D^2/8\right).
\]

Write the state equation as
\[
z'=f(z)+E B_E+D B_D,
\]
and take a calibration potential \(V(z)\). With
\[
p_E=dV(B_E),\qquad p_D=dV(B_D),
\]
one has the exact completion
\[
\begin{aligned}
\mathcal L-\frac{dV}{dt}
={}&\frac W6\left(E-\frac{3p_E}{W}\right)^2
+\frac W8\left(D-\frac{4p_D}{W}\right)^2\\
&+\frac W3C^2-dV(f)
-\frac{3p_E^2}{2W}-\frac{2p_D^2}{W}.
\end{aligned}
\tag{14}
\]
Therefore the pointwise inequality
\[
\boxed{
\frac W3C^2-dV(f)
-\frac{3p_E^2}{2W}-\frac{2p_D^2}{W}\ge0}
\tag{15}
\]
implies
\[
\widehat P\ge V(z_{\rm CH})-V(z_{\rm bolt}).
\tag{16}
\]

A calibration giving an endpoint difference at least \(1-\kappa\) for every bolt scale and every allowed collar would prove the desired diagonal estimate. The chiral charges provide natural leading pieces of \(V\); the almost-Kähler cancellation suggests corrections depending on regularized \(h,k,y\).

This formulation also identifies exactly what an approximate optimizer supplies: along it,
\[
E\approx 3p_E/W,\qquad D\approx4p_D/W,
\]
while the last line of (14) is approximately zero. Numerical optimal-control data can therefore determine derivatives of a candidate \(V\), rather than only another competitor.

The supplied material does not determine an explicit universal \(\kappa\). A number near \(0.005\) would require either a global calibration satisfying (15), or a proved reduction to a compact inner variational problem together with its tail action. A weighted spectral calculation with freely varying coefficients is not equivalent to that theorem.

---

## 4. The symmetry-free identity has a computable area term—and potentially a zero-circle term

For this section it is clearest to use full geometric volume and divide energies by \(2\pi^2\) when comparing with Theorem A.

Suppose a closed self-dual form \(\omega\) extends the CH Kähler form, and normalize
\[
|\omega|_{\hat g}^2=2,\qquad \hat g=u^2g.
\]
On the complement of its zero set, put
\[
\tau=\frac14|\hat\nabla\omega|^2,\qquad
\kappa-\hat s=6\tau,\qquad
\hat s^*=\hat s+2\tau.
\]
Then \(N=(2\pi^2)^{-1}\int4\tau\,d\hat V\) agrees with the diagonal definition.

### Volume pinning depends only on the exceptional period

Let
\[
a=\int_E\omega,\qquad E^2=-1.
\]
Relative intersection theory gives
\[
\int_C\omega^2-\int_{\rm CH}\omega_{\rm CH}^2=-a^2,
\]
so
\[
\boxed{
V_{\hat g}-V_{\rm CH}=-\frac{a^2}{2}.}
\tag{17}
\]
This identity does not depend on whether \(\omega\) is integrable, or on the geometry of its zero set.

### The Chern term when the determinant line extends

If the almost-complex determinant line extends across the zero set and
\[
k=\langle c_1(J),E\rangle,
\]
then, with the CH end contribution fixed,
\[
\boxed{
\int_C\hat s^*\,d\hat V+24V_{\rm CH}=-4\pi k a.}
\tag{18}
\]
For an aligned Kähler exceptional sphere, \(k=1\).

Writing
\[
d=\frac{V_{\hat g}-V_{\rm CH}}{2\pi^2}
=-\frac{a^2}{4\pi^2},\qquad
c=\frac{\int\hat s^*+24V_{\rm CH}}{2\pi^2},
\]
the derivation of Theorem A gives
\[
\begin{aligned}
V_g-V_{\rm CH}
={}&2\pi^2\left[
H+\frac G2+\frac N{24}-d-\frac c{12}
+\frac1{12}\int(s_g+24)u^2\,\frac{dV_g}{2\pi^2}
\right].
\end{aligned}
\tag{19}
\]

For the Weyl decomposition, let \(B:\mathbb R\omega\to
\llbracket\Lambda^{0,2}\rrbracket\) be the off-diagonal block. Then
\[
|W^+|^2=\frac32W_{\omega\omega}^2+2|B|^2+|W_3^+|^2.
\]
Consequently the expected symmetry-free formula is
\[
\boxed{
\begin{aligned}
\widehat P-1={}&
\frac{9a^2}{\pi^2}+\frac{6ka}{\pi}
+12H+6G+\frac32Q_\delta\\
&+\frac1{2\pi^2}\int\bigl(2|B|^2+|W_3^+|^2\bigr)d\hat V
-\frac32N+\Sigma.
\end{aligned}}
\tag{20}
\]
Here the diagonal \(\frac12Q_A\) is precisely the \(W_3^+\) integral. If \(W_2^+\) is defined as the complete off-diagonal operator, its squared norm is \(2|B|^2\).

### The Kähler formula is an exact normalization test

For an aligned Kähler metric,
\[
u=1,\quad N=H=G=0,\quad B=W_3^+=0,\quad
\delta=(s+24)/6,\quad k=1.
\]
Thus the two scalar-square contributions in (20) total
\[
\frac1{2\pi^2}\int\frac{(s+24)^2}{16}\,dV
=\frac{L}{32\pi^2},
\qquad L=\int(s+24)^2\,dV.
\]
Multiplying by \(8\pi^2\) yields
\[
\boxed{
P=8\pi^2+48\pi a+72a^2+\frac L4
=2(2\pi+6a)^2+\frac L4.}
\tag{21}
\]
This reproduces the supplied Kähler formula with \(t=a\).

It also explains why a scalar-normalized aligned cell cannot remain Kähler with \(a>0\). Equations (17) and (18), together with \(\hat s=-24\), would require
\[
12a^2=-4\pi a,
\]
which is incompatible with \(a>0\). Conformal scalar normalization therefore changes the compatible structure in an essential way.

---

## 5. Generic near-symplectic zeros introduce information beyond \(a\)

For a generic closed self-dual form, the zero set consists of circles. The determinant line on their complement need not extend over them.

A local transverse-zero model is
\[
\omega=ds\wedge(Bx\cdot dx)+*_{\mathbb R^3}(Bx\cdot dx),
\]
with \(B\) symmetric, trace free, and invertible. The normalized compatible complex structure on a linking \(S^2\) is described by
\[
x\longmapsto Bx/|Bx|.
\]
Its determinant line has linking Chern number of magnitude \(2\), with sign fixed by the orientation conventions. This is genuine Chern flux.

Choose a closed representative \(\chi=\operatorname{PD}(E)\), supported away from the zero circles, and write
\[
\omega=d\theta-a\chi,
\]
with \(\theta\) equal to the CH primitive on the end. Let \(\rho_J\) be the Chern form, normalized by \([\rho_J/(2\pi)]=c_1(J)\). On excising tubes around the zero circles \(Z_j\), Stokes gives
\[
\boxed{
\int\hat s^*\,d\hat V+24V_{\rm CH}
=-4\pi k a+\mathcal R_Z,}
\tag{22}
\]
where
\[
\mathcal R_Z
=-2\sum_j\lim_{\varepsilon\to0}
\int_{\partial U_\varepsilon(Z_j)}\rho_J\wedge\theta.
\tag{23}
\]
With product orientations and linking number
\[
m_j=\frac1{2\pi}\int_{S_j^2}\rho_J,
\]
the expected local expression is
\[
\mathcal R_Z=-4\pi\sum_jm_j\oint_{Z_j}\theta.
\tag{24}
\]
The invariant object is the total in (22); choices of cycles and potentials can redistribute its displayed pieces.

The corresponding addition to (20) is
\[
\boxed{-\frac{3\mathcal R_Z}{2\pi^2}.}
\tag{25}
\]

This supplies a concrete obstruction to an extension depending only on \(a\). Even when \(a=0\) and \(\omega\) is exact, the circulation
\[
\oint_Z\theta=\int_S\omega,\qquad \partial S=Z,
\]
need not vanish. The diagonal perpendicular bolt has a particularly special primitive that vanishes at its zero surface, explaining its zero inner Chern contribution. Generic zero circles need not share that property.

The local analytic integrals are nevertheless plausible. At a transverse zero,
\[
u^2\asymp r,\qquad
\tau\asymp r^{-3},\qquad
d\hat V\asymp r^4\,dr\,ds,
\]
so \(\tau\,d\hat V\asymp r\,dr\,ds\) is integrable. The conformal scalar integration term also tends to zero. The Chern circulation is therefore the principal extra term to understand, rather than a divergence of \(N\).

**What this could prove.** A symmetry-free identity with explicit zero-circle flux would unify aligned and perpendicular cells and identify the additional geometric quantities governing their cost.

**Decisive comparison.** A deformation moving or creating zero circles while keeping \(a\) fixed would distinguish an \(a\)-only theory from a period-and-flux theory. The change in \(\int\hat s^*\) must match (23).

### Existence of the extending form is itself substantive

The statement “\(b_+=0\), therefore the extending form is unique” addresses uniqueness when the form exists. It does not provide existence with exact agreement on an exterior open set. Closed self-duality is a harmonic equation, and exact exterior agreement prescribes more than asymptotic leading data.

For arbitrary cells, the natural object may be a harmonic self-dual form asymptotic to the CH Kähler form, with a scattered decaying component. The volume and Chern formulas then require its end transgressions to be evaluated. Rates sufficient for squared curvature integrals need not remove linear end terms, just as in the supplied conformal-reduction theorem.

Precise source needs here are:

* ACH Hodge theory for harmonic self-dual two-forms with prescribed CH leading term;
* relative Chern–Weil formulas on near-symplectic complements;
* the determinant-line topology of the standard near-symplectic zero-circle models.

---

## 6. Degeneration is measured by the transported nonintegrability energy, not by Einstein bolt jets alone

For a shrinking bolt \(b_j\to0\), the rescaled scalar-normalized metric
\[
g_j^\#=b_j^{-2}g_j
\]
has scalar curvature \(-24b_j^2\). A smooth core limit can therefore be scalar flat while retaining trace-free Ricci action, exactly as emphasized in Step 26.

The almost-Kähler identity supplies a useful additional theorem shape:
\[
\widehat P\ge1-\frac32N
\qquad(s_g=-24,\ a=0).
\tag{26}
\]
Hence
\[
\boxed{N_j\longrightarrow0\quad\Longrightarrow\quad
\liminf_j\widehat P_j\ge1.}
\tag{27}
\]
This would rule out a uniformly subthreshold shrinking-bolt sequence without classifying its scalar-flat core.

On a core of radius \(O(b_j)\), if \(u_j\) and the rescaled almost-Kähler geometry have uniformly controlled profiles,
\[
G_{\rm core},N_{\rm core}=O(b_j^2),\qquad
H_{\rm core}=O(b_j^4).
\]
The Weyl-square terms can remain order one. Thus persistence of a saving bounded away from zero requires at least one of:

* transported \(N\)-energy at scales larger than the bolt;
* a canonical conformal factor whose rescaled behavior is not uniformly controlled;
* an extended collapsed region carrying nonvanishing \(N\).

These are concrete alternatives visible in cumulative profiles.

A Taub-bolt-like prefix therefore has two complementary evaluations:

1. the chiral action budget from Step 26, pricing its characteristic flux;
2. \(H,G,N,Q_A,Q_\delta\), with \(\mu\nu\) and the contact moment tracking how the prefix connects to CH.

Ricci-flatness of a rescaled core does not by itself determine its contribution to the second evaluation.

For large bolts, a simple estimate based only on \(u=0\) at the bolt cannot supply coercivity. Since \(W\sim b^2t\),
\[
\int_0^\varepsilon W^{-1}\,dt=\infty.
\]
A logarithmic transition illustrates the zero radial capacity of the bolt for the isolated Dirichlet energy. The canonical-form equation, contact closure, and \(W_3^+\) transport are indispensable. A large-bolt estimate would need to show that avoiding conformal cost creates either substantial transport action or a priced Ricci-control trajectory.

---

## 7. Multiple cells have an intersection-matrix term and a geometric interaction term

For several exceptional classes with intersection matrix \(Q\), period vector \(\mathbf a\), and Chern evaluations \(\mathbf k\), the cohomological formulas become
\[
\Delta V_{\hat g}
=\frac12\mathbf a^TQ^{-1}\mathbf a,
\]
and, when the determinant line extends,
\[
\Delta\int\hat s^*\,d\hat V
=4\pi\,\mathbf k^TQ^{-1}\mathbf a.
\]
Thus their contribution to the normalized identity is
\[
\boxed{
-\frac9{\pi^2}\mathbf a^TQ^{-1}\mathbf a
-\frac6\pi\mathbf k^TQ^{-1}\mathbf a,}
\tag{28}
\]
plus the zero-set term (25). Disjoint exceptional spheres have \(Q=-I\), recovering the sum of the single-cell area terms. Plumbed configurations can have genuine cross terms already at this cohomological level.

The topological constant follows from
\[
P=4\int\left(|W^+|^2+\frac{s^2}{48}\right)dV
-8\pi^2(2\chi+3\tau).
\tag{29}
\]
Each blow-up contributes \(1\) to the normalized relative constant. A connected sum with \(S^1\times S^3\) changes \(2\chi+3\tau\) by \(-4\), hence contributes \(4\). The curvature and canonical-form terms determine how much of these constants is recovered.

Even for disjoint cells, the rest of the identity need not split. The Yamabe factor and the harmonic self-dual form are global fields. For well-separated insertions their leading interaction should be represented by off-diagonal entries of the scalar and self-dual-form Green operators. Eliminating those fields produces a coupled quadratic form in the cell charges and orientations.

**Distinguishing experiment.** A two-cell family varying separation and relative contact-slot orientation would separate three effects:

* the additive topological constant;
* the intersection-matrix contribution;
* the transported-field interaction.

A mixed handle/blow-up construction is especially informative: a handle changes the topological constant and the available circulations without introducing an exceptional period. It directly tests whether periods and zero-circle flux, rather than independent local cell costs, are the correct global variables.

The central opportunity is therefore a combined theory of **bolt charge, contact closure, Yamabe response, and Chern flux**. The supplied identity already separates these mechanisms. Retaining their coupling—particularly the compulsory sign change and the tail impedance—is what could turn a qualitative explanation of the observed saving into a sharp quantitative Einstein-gap theorem.