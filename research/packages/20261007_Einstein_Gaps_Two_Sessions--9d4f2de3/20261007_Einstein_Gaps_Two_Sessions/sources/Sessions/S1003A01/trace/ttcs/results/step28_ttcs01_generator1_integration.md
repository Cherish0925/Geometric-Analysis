# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step28_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step28_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Research goal context: the session studies the scale-invariant Einstein defect on closed four-manifolds and, centrally, the optimal cost of an exceptional (-1)-sphere cell inserted into a complex-hyperbolic (CH) background; a certified perpendicular diagonal cell has Phat=P/(8pi^2)<1 (best floating ~0.99518), disproving universal coefficient 4, but no matching lower bound exists. Theorem A in the supplied note gives, for diagonal exact-CH perpendicular cells, the exact identity Phat-1=12H+6G+(3/2)Qdelta+(1/2)QA-(3/2)N+Sigma, where only the nonintegrability N of the canonical almost-Kahler structure (conformal factor u, ghat=u^2 g) is negative; nu is forced by the bolt (charge K, linear transport lambda=nu_T/2+beta*nu, far-field Hardy positivity beyond sinh^2 R~5.9; at the bolt the 6G and (3/2)N densities cancel). Generate the strongest mathematically concrete routes by which this structure could yield (a) a quantitative lower bound Phat>=1-kappa for diagonal cells with explicit small kappa (ideally of the observed order 0.005), e.g. a near-zone inequality coupling nu, (log 1/u)_T, lambda and the Yamabe equation 6 Lap_hat v + shat v + 24 v^3=0 (v=1/u), a Bogomolny/calibration completion, an optimal-control or Sturm-Liouville reduction with the forced charge K, or an obstruction showing why no such inequality can hold without global information; (b) a symmetry-free extension to arbitrary exact-CH cells using the closed self-dual form extending the CH Kahler form, its modulus a=int_E omega, its near-symplectic zero set, and the U(2) splitting with W2 and W3, unifying aligned Kahler cells (a>0; Kahler formula P=2(2pi+6t)^2+L/4) with perpendicular cells (a=0); derive the expected a-dependent pinning and Chern terms and test them against the known Kahler cell formula; (c) consequences for collapsed/large-bolt degenerations (where H, G, N, QA, Qdelta should be evaluated on Taub-bolt-like prefixes) and for multi-cell or mixed blow-up/handle interactions. For each route give the key equations, what would be proved, what decisive calculation would test it, and what would falsify it. Do not invent literature; name precise knowledge requests if needed.

## Integrated Scientific Memo

# Einstein-cell lower bounds and symmetry-free extension: concrete routes

Assume first the scalar-normalized diagonal perpendicular class, so \(s_g=-24\) and \(\Sigma=0\). Let
\[
v=u^{-1},\qquad r=(\log v)_T,\qquad
w=A_fA_gA_h,\qquad L=(\log w)_T .
\]
Then \(G=\int r^2w\,dT\), \(N=\int4\nu^2w\,dT\), and
\[
\lambda=\frac12\nu_T+\beta\nu .
\]
The Yamabe equation
\[
-6\widehat\Delta v+\hat s\,v+24v^3=0
\]
gives
\[
\hat s=6(r_T+r^2+Lr)-24v^2.
\]
Since \(\kappa-\hat s=6\nu^2\) and \(\widehat W^+_{\omega\omega}=\kappa/6\),
\[
\delta:=\widehat W^+_{\omega\omega}+4
=r_T+r^2+Lr+\nu^2+4(1-v^2).
\]
Thus Theorem A becomes the exact one-dimensional action
\[
\boxed{
\widehat P-1
=\int w\left[
12(v^2-1)^2+6(r^2-\nu^2)
+\frac32\delta^2
+\frac12(\nu_T+2\beta\nu)^2
\right]\,dT .}
\tag{1}
\]
This is the correct starting point: the negative \(-6\int\nu^2w\) cannot be estimated sharply while treating \(v,\nu,\beta,w\) as independent.

---

## 1. Diagonal quantitative lower bound

### 1.1 Regularize the bolt cancellation before estimating

Let
\[
\mu_T=2\beta\mu,\qquad h=\mu\nu,\qquad k=\mu r,\qquad
\rho=\frac{w}{\mu^2}.
\]
Then
\[
\frac12Q_A=\frac12\int\rho h_T^2\,dT,\qquad
6G-\frac32N=6\int\rho(k^2-h^2)\,dT.
\tag{2}
\]
Near the perpendicular bolt,
\[
r\sim\nu,\qquad h(0)=k(0)=K,
\]
while \(\rho\) is locally integrable. This represents the exact cancellation of the individually singular \(G\)- and \(N\)-densities without subtracting them numerically.

The transport law immediately yields the capacitary bound
\[
\boxed{
\frac12Q_A\ge
\frac{K^2}
{2\displaystyle\int_0^{T_c}\mu^2/w\,dT}.}
\tag{3}
\]
This quotient, not the normalization-dependent value of \(K\), is the invariant transport cost.

A bound based only on (3), however, will not be sharp: the geometry imposes a second global constraint.

---

### 1.2 Contact closure forces a sign change and a second transport moment

Set
\[
y=\tanh(q/2).
\]
From
\[
\nu=-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right)
\]
one obtains
\[
\boxed{
y_T+\frac4{A_f}y=-\nu(1-y^2).}
\tag{4}
\]
If \(\eta_T=(4/A_f)\eta\), then
\[
(\eta y)_T=-\eta\nu(1-y^2).
\]
Since \(y(0)=1\) at a perpendicular bolt and \(y(T_c)=0\) on the CH collar,
\[
\boxed{
\int_0^{T_c}\eta\,\nu(1-y^2)\,dT=\eta(0)>0.}
\tag{5}
\]
Because \(\nu<0\) near the bolt, \(\nu\) must become positive somewhere. The sign change seen in the numerical profiles is therefore compulsory.

For fixed coefficients, minimizing
\[
\frac12\int\rho h_T^2\,dT
\]
subject to

* \(h(0)=K,\ h(T_c)=0\);
* the contact moment (5), linearized or retained nonlinearly,

is a two-constraint capacity problem. In the linearized problem its value is an explicit quadratic form obtained by inverting the \(2\times2\) Gram matrix of the Green representers.

**Potential theorem.** If the corresponding capacity matrix admits a uniform lower bound over the admissible near-zone geometry, then \(Q_A\) controls both bolt-charge removal and the forced positive lobe of \(\nu\). Combined with the Yamabe equation, this can bound the entire negative sector in (1).

**Decisive calculation.** On the existing \(x_0=.015,.038,.07\) profiles, compute:

1. the one-constraint minimum from (3);
2. the two-constraint minimum including (5);
3. the observed \(Q_A/2\).

If the two-constraint value nearly saturates \(Q_A/2\), the problem has effectively reduced to a finite-dimensional capacity estimate. A large remaining discrepancy means that the structural evolution of \((A_f,\mathcal P,q,v)\) must be retained.

**Falsification.** A sequence of admissible cells with bounded geometry, fixed nonzero normalized charge and contact moment, but vanishing transport action would disprove such a uniform capacity estimate.

---

### 1.3 The tail must enter through its impedance, not merely Hardy positivity

For fixed \(w,\beta\), define
\[
\mathcal Q_\nu
=\frac12\int w(\nu_T+2\beta\nu)^2\,dT
-6\int w\nu^2\,dT.
\tag{6}
\]
Its Euler equation is
\[
-\frac1w(w\nu_T)_T+
\left(4\beta^2-2\beta_T-2\beta L-12\right)\nu=0.
\tag{7}
\]
For a minimizing tail terminating with \(\nu(T_c)=0\), its on-shell action is the Dirichlet-to-Neumann form
\[
\boxed{
\mathcal Q_{\nu,\mathrm{tail}}
=-\frac12w(T_*)\nu(T_*)
\bigl(\nu_T(T_*)+2\beta(T_*)\nu(T_*)\bigr).}
\tag{8}
\]
The impedance can be computed rigorously by the Riccati equation associated with (7).

One must also impose contact closure. In the linear CH tail,
\[
q_T+\frac4{A_f}q=-2\nu,
\]
hence
\[
\eta(T_*)q(T_*)
=2\int_{T_*}^{T_c}\eta\nu\,dT.
\tag{9}
\]
The correct tail action is therefore a quadratic form in
\[
\bigl(q(T_*),\nu(T_*)\bigr),
\]
not a scalar form in \(\nu(T_*)\).

This is numerically essential. For the supplied \(x_0=.038\) profile, the near-zone conformal plus Nijenhuis sectors contribute approximately
\[
0.06009-0.07068=-0.01059,
\]
while the far sector returns
\[
+0.00588.
\]
Discarding the tail after proving only nonnegativity loses a term of the same scale as the final saving \(0.00471\). A sharp estimate near \(0.005\) must retain the tail impedance.

**Potential theorem.** Split at a controlled section \(T_*\):
\[
\widehat P-1\ge
\mathcal A_{\mathrm{inner}}(z(T_*))
+\langle \mathcal Z_{\mathrm{tail}} z(T_*),z(T_*)\rangle,
\qquad z=(q,\nu,\text{possibly }v-1),
\]
and minimize the finite-interval inner action plus the certified CH impedance.

**Decisive calculation.** Compute interval enclosures for the Riccati matrix of the coupled \((q,\nu)\) CH system, then compare its boundary action with the measured far contributions for all three profiles.

**Falsification.** If admissible tails can carry fixed \((q(T_*),\nu(T_*))\) to the CH collar with action tending to zero, no lower bound of the desired scale can follow from a finite near/far split.

---

### 1.4 A Bogomolny completion identifies where gain cannot occur

Let
\[
\ell=\frac{A_f}{A_gA_h},\qquad B=2\beta-\ell.
\]
The supplied anti-invariant Ricci component can be written
\[
\widehat D=2\nu_T+(-4\beta+4\ell)\nu .
\]
Integration by parts gives
\[
\boxed{
\mathcal Q_\nu
=\frac18\int w\widehat D^2\,dT
+[wB\nu^2]
+\int w\Xi\nu^2\,dT,}
\tag{10}
\]
where
\[
\Xi=4\beta\ell-2\ell^2-6-B_T-LB.
\tag{11}
\]
On exact CH,
\[
A_f=\sqrt{x(1+x)},\qquad A_gA_h=x,\qquad
\beta=\frac{3-2x}{2\sqrt{x(1+x)}},
\]
and
\[
B=\frac{2-3x}{\sqrt{x(1+x)}}.
\]
These obey \(\Xi=0\). For compactly supported variations of the CH geometry,
\[
\boxed{
\mathcal Q_\nu=\frac18\int w\widehat D^2\,dT\ge0.}
\tag{12}
\]
Thus arbitrary CH-supported squashing cannot create saving: gain requires coupled deformation of the radial geometry, conformal factor, and bolt data.

Equation (10) cannot be integrated naively through the conical almost-Kähler bolt because its separated pieces diverge. The regular original-metric square is
\[
\boxed{
v^2D_g=\widehat D-2rq_T,\qquad
\frac18\int D_g^2\,dV_g
=\frac18\int(\widehat D-2rq_T)^2\,d\hat V.}
\tag{13}
\]
This is the appropriate square for a global completion.

**Potential theorem.** Complete (1) using (13), leaving a deformation remainder involving \(\Xi\), \(\delta\), and \(v-1\). If that remainder is bounded below on the compact near zone and the tail is replaced by its impedance, one obtains an explicit
\[
\widehat P\ge1-\kappa .
\]

**Decisive calculation.** Symbolically expand
\[
12(v^2-1)^2+\frac32\delta^2
+\frac18(\widehat D-2rq_T)^2
\]
against the original integrand and determine whether the residual is a low-rank quadratic form plus an exact derivative. Its smallest generalized eigenvalue along the supplied profiles is the immediate test.

**Falsification.** A negative direction in the residual quadratic form, compatible with all structural equations and carrying no compensating boundary action, would rule out this completion.

---

### 1.5 Global Hamilton–Jacobi calibration

The most robust diagonal route works directly with the scalar-normalized Ricci controls. Let
\[
y_i=\frac{a_i'}{a_i},\qquad S=y_f+y_g+y_h.
\]
With \(P_i\) the intrinsic Ricci eigenvalues of the orbit metric,
\[
C=\frac12\left(S^2-\sum_i y_i^2-R^{(3)}-12\right),
\tag{14}
\]
and
\[
\begin{aligned}
y_f'&=P_f-Sy_f+6+C/3-2E/3,\\
y_g'&=P_g-Sy_g+6+C/3+E/3-D/2,\\
y_h'&=P_h-Sy_h+6+C/3+E/3+D/2.
\end{aligned}
\tag{15}
\]
The action is
\[
\mathcal L=W\left(C^2/3+E^2/6+D^2/8\right).
\]
Write the controlled evolution as
\[
z'=f(z)+E B_E+D B_D.
\]
For a potential \(V(z)\), set
\[
p_E=dV(B_E),\qquad p_D=dV(B_D).
\]
Then
\[
\begin{aligned}
\mathcal L-\frac{dV}{dt}
={}&\frac W6\left(E-\frac{3p_E}{W}\right)^2
+\frac W8\left(D-\frac{4p_D}{W}\right)^2\\
&+\frac W3C^2-dV(f)
-\frac{3p_E^2}{2W}-\frac{2p_D^2}{W}.
\end{aligned}
\tag{16}
\]
Hence the Hamilton–Jacobi subsolution inequality
\[
\boxed{
\frac W3C^2-dV(f)
-\frac{3p_E^2}{2W}-\frac{2p_D^2}{W}\ge0}
\tag{17}
\]
implies
\[
\widehat P\ge V(z_{\rm CH})-V(z_{\rm bolt}).
\tag{18}
\]

This framework naturally incorporates the chiral charges, the \(D\)-channel Green estimates from Step 26, and regularized variables \((h,k,y)\).

**Potential theorem.** Produce a certified \(V\) whose endpoint difference is \(1-\kappa\), uniformly in bolt and collar parameters.

**Decisive calculation.** Use an approximate optimal trajectory to infer \(dV\) from
\[
E\approx3p_E/W,\qquad D\approx4p_D/W,
\]
fit \(V\) in a controlled basis, and verify (17) by interval arithmetic on a compactified state domain.

**Falsification.** Failure of every candidate calibration near a specific admissible state identifies either a genuine lower-action escape or a missing state variable. In particular, inherited anisotropy momentum must be included; exact Einstein arcs can carry it at zero defect cost.

---

### 1.6 What can and cannot currently be claimed

The data support an optimum of order \(1-0.005\), but do not certify a universal \(\kappa\). Hardy positivity alone is too lossy. The most realistic sharp proof is:

1. regularized inner action in \((h,k,y,v)\);
2. two constraints: bolt charge and contact closure;
3. matrix-valued CH tail impedance;
4. certified minimization or a Hamilton–Jacobi calibration.

A universal near-zone inequality depending only on \(\nu,r,\lambda\) but not on contact closure, tail boundary data, or global state evolution is unlikely to recover the observed scale.

---

## 2. Symmetry-free extension

Let \(\omega\) be a closed self-dual form asymptotic to the CH Kähler form. On \(C\setminus Z(\omega)\), choose
\[
\hat g=u^2g,\qquad |\omega|_{\hat g}^2=2,
\]
and define
\[
\tau=\frac14|\hat\nabla\omega|^2.
\]
Then
\[
\kappa-\hat s=6\tau,\qquad
\hat s^*=\hat s+2\tau.
\tag{19}
\]
The diagonal \(N\) becomes
\[
N=\frac1{2\pi^2}\int4\tau\,d\hat V
\]
when using full geometric volume.

### 2.1 Period-dependent pinning

Let
\[
a=\int_E\omega,\qquad E^2=-1.
\]
Relative intersection theory predicts
\[
\int_C\omega^2-\int_{\rm CH}\omega_{\rm CH}^2=-a^2.
\]
Since \(\omega^2=2\,d\hat V\),
\[
\boxed{
V_{\hat g}-V_{\rm CH}=-\frac{a^2}{2}.}
\tag{20}
\]
For \(a=0\), this recovers perpendicular pinning; \(a>0\) gives the aligned sector.

If the determinant line of \(J\) extends and
\[
k=\langle c_1(J),E\rangle,
\]
the expected relative Chern formula is
\[
\boxed{
\int_C\hat s^*\,d\hat V+24V_{\rm CH}=-4\pi k a.}
\tag{21}
\]
For the aligned exceptional Kähler sphere, \(k=1\).

### 2.2 Full \(U(2)\) Weyl splitting

With
\[
\Lambda^+=\mathbb R\omega\oplus\llbracket\Lambda^{0,2}\rrbracket
\]
and \(B\) the off-diagonal \(W_2^+\) block,
\[
|W^+|^2
=\frac32W_{\omega\omega}^2+2|B|^2+|W_3^+|^2.
\tag{22}
\]
Thus the expected symmetry-free extension of Theorem A is
\[
\boxed{
\begin{aligned}
\widehat P-1={}&
\frac{9a^2}{\pi^2}+\frac{6ka}{\pi}
+12H+6G+\frac32Q_\delta\\
&+\frac1{2\pi^2}\int
\left(2|B|^2+|W_3^+|^2\right)d\hat V
-\frac32N+\Sigma ,
\end{aligned}}
\tag{23}
\]
provided there are no additional zero-set or end transgressions. In the diagonal perpendicular class, \(a=0\), \(B=0\), and the \(W_3^+\) term is exactly \(Q_A/2\).

### 2.3 Exact check against the aligned Kähler formula

For an aligned Kähler cell,
\[
u=1,\quad N=H=G=0,\quad B=W_3^+=0,\quad
\delta=(s+24)/6,\quad k=1.
\]
The two scalar-square terms combine to
\[
\frac1{2\pi^2}\int\frac{(s+24)^2}{16}\,dV
=\frac{L}{32\pi^2},
\qquad L=\int(s+24)^2\,dV.
\]
Multiplying (23) by \(8\pi^2\) yields
\[
\boxed{
P=8\pi^2+48\pi a+72a^2+\frac L4
=2(2\pi+6a)^2+\frac L4,}
\tag{24}
\]
which exactly reproduces the known Kähler formula with \(t=a\). This fixes the coefficients in (20)–(23).

---

### 2.4 Near-symplectic zero circles add Chern-flux data beyond \(a\)

For a generic self-dual harmonic form, \(Z(\omega)\) is a union of circles. The normalized almost-complex structure exists only off \(Z\), and its determinant line need not extend.

Excising tubes \(U_\varepsilon(Z_j)\), the relative Chern formula acquires
\[
\boxed{
\int\hat s^*\,d\hat V+24V_{\rm CH}
=-4\pi ka+\mathcal R_Z,}
\tag{25}
\]
where
\[
\mathcal R_Z
=-2\sum_j\lim_{\varepsilon\to0}
\int_{\partial U_\varepsilon(Z_j)}\rho_J\wedge\theta,
\qquad d\theta=\omega+a\chi,
\tag{26}
\]
with \(\chi\) representing \(\operatorname{PD}(E)\) according to the chosen sign convention. Formally, if
\[
m_j=\frac1{2\pi}\int_{S_j^2}\rho_J
\]
is the linking Chern number, then
\[
\mathcal R_Z=-4\pi\sum_jm_j\oint_{Z_j}\theta.
\tag{27}
\]
The corresponding addition to (23) is
\[
-\frac{3\mathcal R_Z}{2\pi^2}.
\tag{28}
\]

Therefore an \(a\)-only theory is generally insufficient: even when \(a=0\), zero-circle circulations may contribute. The diagonal perpendicular cell is special because its primitive has vanishing bolt contribution.

The local energies remain plausibly integrable. At a transverse zero,
\[
u^2\asymp r,\qquad \tau\asymp r^{-3},\qquad
d\hat V\asymp r^4\,dr\,ds,
\]
so \(\tau\,d\hat V\asymp r\,dr\,ds\).

**What must be proved.**

1. Existence of a harmonic self-dual form with prescribed CH leading term.
2. Its decay and end transgression.
3. The relative Chern–Weil formula on the complement of near-symplectic zeros.
4. The precise linking Chern number and sign of each standard zero-circle model.

Uniqueness from \(b_+=0\) applies only after existence has been established; exact agreement with the CH Kähler form on an exterior open set is stronger than merely prescribing asymptotic data.

**Decisive test.** Deform a cell while holding \(a\) fixed but moving or creating zero circles. The variation of \(\int\hat s^*\) should equal the change in (26). If it does not, either the local zero term or the end transgression is incomplete.

---

## 3. Collapsed and large-bolt degenerations

For \(b_j\to0\), rescale
\[
g_j^\#=b_j^{-2}g_j.
\]
Then \(s(g_j^\#)=-24b_j^2\to0\). A smooth limit need only be scalar flat, not Ricci flat; Taub-bolt matching applies automatically only to an exact-Einstein or defect-to-zero branch.

For \(a=0\), Theorem A gives immediately
\[
\widehat P\ge1-\frac32N.
\tag{29}
\]
Hence
\[
\boxed{
N_j\to0\quad\Longrightarrow\quad
\liminf_j\widehat P_j\ge1.}
\tag{30}
\]
A uniformly subthreshold collapsed sequence must therefore retain nonzero transported nonintegrability energy.

On a genuinely \(O(b_j)\)-sized core with uniformly controlled rescaled profiles,
\[
G_{\rm core},N_{\rm core}=O(b_j^2),\qquad
H_{\rm core}=O(b_j^4),
\]
while Weyl-square terms may remain order one. Thus persistent subthreshold saving requires at least one of:

* \(N\)-energy transported to scales larger than the bolt;
* loss of uniform control of the canonical conformal factor;
* an extended collapsed region with nonvanishing \(N\);
* a singular transition whose cost must be detected by chiral charges or the \(D\)-channel.

A collapsed prefix should therefore be evaluated simultaneously by:

1. the Step-26 chiral action budget;
2. the cumulative \(H,G,N,Q_A,Q_\delta\);
3. the regularized charge \(h=\mu\nu\);
4. the contact moment (5);
5. the endpoint tail impedance.

This distinguishes a harmless Taub-bolt-like core from a prefix that stores the finite action needed for subthreshold saving.

For large bolts, the isolated conformal Dirichlet energy is not coercive:
\[
W\sim b^2t,\qquad
\int_0^\varepsilon W^{-1}dt=\infty.
\]
Thus merely imposing \(u=0\) at the bolt cannot force a fixed \(G\)-cost. Any large-bolt lower bound must use contact closure, \(W_3^+\) transport, and/or the Ricci-control action. A logarithmically slow conformal transition is the basic obstruction to an \(H+G\)-only estimate.

**Decisive degeneration calculation.** For a sequence of candidate shrinking or expanding bolts, rescale cumulative profiles by the bolt scale and determine whether the negative near-zone contribution converges to:

* zero;
* a finite core action;
* a mesoscopic transported \(N\)-action.

This identifies which compactness theorem is actually needed.

---

## 4. Multiple cells and mixed blow-up/handle configurations

Let the exceptional classes have intersection matrix \(Q\), period vector \(\mathbf a\), and Chern evaluations \(\mathbf k\). Relative intersection theory gives
\[
\Delta V_{\hat g}
=\frac12\mathbf a^TQ^{-1}\mathbf a,
\tag{31}
\]
and, when the determinant line extends,
\[
\Delta\int\hat s^*d\hat V
=4\pi\,\mathbf k^TQ^{-1}\mathbf a.
\tag{32}
\]
Their contribution to the normalized gap identity is therefore
\[
\boxed{
-\frac9{\pi^2}\mathbf a^TQ^{-1}\mathbf a
-\frac6\pi\mathbf k^TQ^{-1}\mathbf a,}
\tag{33}
\]
plus zero-circle and end transgressions. For disjoint exceptional spheres \(Q=-I\), this becomes the sum of the single-cell positive area/Chern terms; plumbed configurations produce genuine cross terms.

The topological baseline follows from
\[
P=4\int\left(|W^+|^2+\frac{s^2}{48}\right)dV
-8\pi^2(2\chi+3\tau).
\tag{34}
\]
A blow-up changes the normalized baseline by \(1\). A connected sum with \(S^1\times S^3\) changes \(2\chi+3\tau\) by \(-4\), hence the normalized baseline by \(4\).

Even for disjoint cells, analytic costs need not add: the Yamabe factor and harmonic self-dual form are global. At large separation, eliminating those fields should produce Green-operator interactions between:

* bolt charges;
* contact moments and orientations;
* periods \(\mathbf a\);
* zero-circle circulations.

**Decisive experiment.** For two cells, vary separation and relative contact-slot orientation. Subtract the known topological and intersection-matrix terms. The residual detects transported-field interaction. A mixed handle/blow-up family is especially useful because a handle changes the topological constant and available circulations without adding an exceptional period; it tests whether the correct variables are periods plus Chern flux rather than independent local cell costs.

---

## Main conclusion

The observed saving is generated by a tightly constrained global mechanism:

\[
\text{bolt Nijenhuis charge}
\;\longrightarrow\;
\text{forced sign change from contact closure}
\;\longrightarrow\;
W_3^+\text{ transport cost}
\;\longrightarrow\;
\text{positive CH tail impedance},
\]
coupled to the Yamabe response of \(u\).

The most credible route to an explicit \(\kappa\sim0.005\) is not a bare Hardy inequality. It is a certified finite-interval variational problem using regularized bolt variables, the two global transport constraints, and a matrix Dirichlet-to-Neumann tail action—or equivalently a Hamilton–Jacobi calibration of the full scalar-normalized Ricci-control system.

Without symmetry, the same mechanism should persist, but the governing global data enlarge from the perpendicular charge to:

\[
(a,\;c_1\!\cdot E,\;\text{zero-circle Chern circulations},\;W_2^+,\;W_3^+).
\]
The \(a\)-dependent coefficients are fixed by the aligned Kähler test, while generic near-symplectic zeros show why period data alone cannot determine the gap.