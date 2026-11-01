# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step98_full_matrix_joint_transition.py",
    "Sessions/S0910A03/workspace/scripts/step98_direct_spd_transition.py",
    "Sessions/S0910A03/workspace/data/step98_direct_spd_N16_interior.json",
    "Sessions/S0910A03/workspace/data/step98_center_residual_resolution.json",
    "Sessions/S0910A03/workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/plans/step96_route_map.md"
  ]
}
```

## Task

Given the exact charged Koiso center data and Step 98's full SPD logarithmic-matrix finite-domain formulation, develop a mathematically serious next construction/obstruction experiment that can distinguish genuine two-ended matching from low-resolution overfitting. Work directly with the supplied equations and artifacts. Seek a representation that preserves the full center q,K and both attachments, allows resolution continuation, and exposes residual projections versus inverse scales. Specify a small number of decisive computations, exact variables/boundary conditions, and what numerical scaling would reveal. Do not treat the cosh exterior as solving the inner transition and do not assume a gauge change cures elliptic Cauchy ill-posedness.

## Output

### 1. What the present Step 98 result is actually measuring

The direct nodal calculation does not yet represent a \(C^2\)-attached metric. It fixes only the endpoint values of \(X\); arbitrary interior nodal values generally change the Chebyshev first and second derivatives there. The code then replaces \(q_n,q_{nn}\) in the endpoint residual rows by the desired jets. Thus those rows are not the Ricci tensor of the polynomial metric produced by the optimizer. A large decrease after four function evaluations can therefore coexist with derivative jumps at the two attachments.

Two numerical floors in the supplied \(N_s=16\), \(R=1\) record are already identifiable:

* The final center supremum \(1.3634185384\) is precisely the Fourier momentum error at \(N_s=16\). The resolution table reduces it to \(6.76\times10^{-6}\) at \(N_s=128\), while the Hamiltonian and tangential center blocks are already at roundoff.
* For the inherited exterior \(q=e^{2r}q_0(s)\),
  \[
  E_{rr}=E_{ri}=0,\qquad E_{ij}=\operatorname{Ric}(q_0)_{ij}.
  \]
  Hence its invariant endpoint defect is exactly
  \[
  \delta_{\rm inh}(R)
  =e^{-2R}\left\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\right\|_{\rm op}.
  \tag{1}
  \]
  The reported \(R=1\) value \(1.0741905092\) is consistent with this formula. An inherited-end computation cannot pass below (1) when the endpoint itself is included.

These two effects explain the displayed final supremum without determining the continuum residual in the interior.

---

## 2. A single signed-coordinate representation with exact center and end jets

A stronger representation uses one signed normal coordinate \(n\in[-R_-,R_+]\), rather than two independently optimized half-polynomials. Let
\[
S_0(s)=q_0(s)^{1/2},\qquad
A=S_0^{-1}K_0S_0^{-1},\qquad
B=S_0^{-1}\operatorname{Ric}(q_0)S_0^{-1}+3I.
\]
Write
\[
g=dn^2+q(n,s),\qquad
q=S_0\,e^{X(n,s)}S_0.
\tag{2}
\]

The exact center conditions are
\[
X(0,s)=0,\qquad X_n(0,s)=2A(s),\qquad X_{nn}(0,s)=2B(s).
\tag{3}
\]
They imply
\[
q(0)=q_0,\qquad q_n(0)=2K_0,
\]
and, because \(D^2e^0[2A,2A]=4A^2\),
\[
q_{nn}(0)
=2\bigl(\operatorname{Ric}(q_0)+3q_0+2K_0q_0^{-1}K_0\bigr).
\tag{4}
\]
Consequently all ten components of \(E=\operatorname{Ric}+3g\) vanish at the center analytically, using the exact Hamiltonian and momentum constraints.

There are two useful terminal families.

### Inherited terminal geometry

Set
\[
X(R_+,s)=2R_+I,\quad X_n(R_+,s)=2I,\quad X_{nn}(R_+,s)=0,
\]
\[
X(-R_-,s)=2R_-I,\quad X_n(-R_-,s)=-2I,\quad X_{nn}(-R_-,s)=0.
\tag{5}
\]
This reproduces the Step 98 attachments and retains the exact floor (1).

### Exact flat horospherical terminal geometry

Choose constant flat torus metrics \(\bar q_\pm\) and define
\[
L_\pm(s)=\log\!\left(S_0(s)^{-1}\bar q_\pm S_0(s)^{-1}\right).
\]
Replace the terminal values in (5) by
\[
X(R_+,s)=2R_+I+L_+(s),\qquad
X(-R_-,s)=2R_-I+L_-(s),
\tag{6}
\]
while keeping the same first and second derivatives. Then
\[
q=e^{2n}\bar q_+\quad\text{on the right exterior},\qquad
q=e^{-2n}\bar q_-\quad\text{on the left exterior},
\]
which are exact \(\operatorname{Ric}=-3g\) metrics. This second family separates the inner matching problem from the known \(e^{-2R}\) inherited-end term.

For every matrix component, let \(H_R(n,s)\) be the degree-eight Hermite interpolant satisfying the three jets at \(-R_-,0,R_+\). The complete finite-dimensional space can then be written
\[
X=H_R+w_RY,
\qquad
w_R(n)=
\left(\frac{n}{R_*}\right)^3
\left(\frac{n+R_-}{R_*}\right)^3
\left(\frac{R_+-n}{R_*}\right)^3,
\tag{7}
\]
with
\[
Y(n,s)=
\sum_{k=0}^{N_r}\sum_{|m|\le N_s}
Y_{km}T_k(\xi(n))e^{ims},
\qquad
Y_{k,-m}=\overline{Y_{km}},
\tag{8}
\]
where every \(Y_{km}\) is a symmetric \(3\times3\) matrix. Equation (7) preserves all nine interpolation conditions for every truncation. Because it is one global function, it also removes the uncontrolled third-derivative mismatch between separately constructed halves.

For long cylinders, a \(C^p\) Fourier–spectral-element or high-order B-spline version of (7) is numerically preferable. Fixed physical element width keeps radial resolution constant as \(R\) grows. Terminal elements can be fixed exactly to the exponential exteriors, giving open collars rather than substituted endpoint rows.

The matrix exponential should remain the true exponential on accepted states. Eigenvalue clipping changes both the metric map and its linearization.

---

## 3. Three decisive computations

### A. Fixed-\(R\) continuum continuation

For a fixed \(R\), minimize the complete geometric residual
\[
\|E\|_{2,g}^2
=\int_{-R}^{R}\int_{S^1}|E^{\rm orth}|_F^2
\sqrt{\det q}\,ds\,dn
\tag{9}
\]
while separately recording
\[
\delta_\infty
=\sup_{n,s}\|E^{\rm orth}(n,s)\|_{\rm op}.
\tag{10}
\]
A \(p\)-norm continuation with \(p=4,8,16\) is useful because an \(L^2\) objective alone can hide a narrow peak.

The same candidate has three evaluations:

1. the optimization grid;
2. a Fourier–radial grid with two or three times as many points;
3. modal projection of every residual block on the enlarged grid.

No endpoint derivative replacement enters any of them. The center derivatives of the analytic \(q_0,K_0\) should be evaluated analytically or by automatic differentiation, so the \(N_s=16\) momentum artifact is absent.

Let
\[
\kappa_{km}
=\left[\left(\frac{\pi k}{R_-+R_+}\right)^2+m^2\right]^{1/2}.
\]
The shell energy
\[
\mathcal E(\kappa)^2
=\sum_{\kappa\le\kappa_{km}<2\kappa}
|\widehat E_{km}|^2
\tag{11}
\]
distinguishes a smooth residual from one moving with the numerical cutoff.

A continuum candidate exhibits stabilization of \(\delta_\infty\), agreement between all three evaluations, decay of the highest coefficient shells, and convergence of \(q\) in \(C^2\) on fixed compact subcylinders. Collocation overfitting instead appears as a small optimization-grid value accompanied by an \(O(1)\) enlarged-grid value, residual energy near \(\kappa_{\max}\), or growing \(C^2\) coefficient norms.

A fixed-\(R\) sequence with \(\delta_\infty\to0\) and \(C^2\) convergence would approximate an exact finite-cylinder connector. A fixed-\(R\) sequence converging to \(\delta(R)>0\) instead identifies a genuine finite-domain residual level for this Gaussian \(T^2\)-invariant class.

### B. Outer-scale continuation with two terminal families

Let
\[
\eta=e^{-R},\qquad R_j=R_0+j\log2,
\]
so each increment halves \(\eta\). Radial degrees of freedom grow proportionally to \(R\), keeping the physical mesh scale fixed. For every \(R_j\), compare:

* inherited terminals (5);
* exact flat terminals (6).

The inherited family has the exact benchmark
\[
\delta(R)\ge C_0\eta^2,
\qquad
C_0=\|q_0^{-1/2}\operatorname{Ric}(q_0)q_0^{-1/2}\|_{\rm op}.
\tag{12}
\]
The flat family has no such terminal contribution.

Several mechanisms have sharply different signatures:

* **Delayed charge taper:** the mixed block predicted by the fixed-charge scaling behaves as
  \[
  \|E_{\rm mix}\|=O(\eta^3/\ell),\qquad Q=O(\eta^6),
  \tag{13}
  \]
  for a taper of physical width \(\ell\) near the expanded end.
* **Intrinsic inherited-end curvature:** \(\delta\sim C_0\eta^2\).
* **A broad adiabatic transition:** radial derivatives can produce powers of \(R^{-1}\), visibly distinct from powers of \(\eta\).
* **A persistent horizontal or orbit-shape cost:** one of \(E_{nn},E_{ns},E_{TT}\) approaches a nonzero level as \(R\to\infty\).

The peak location is as important as its value. A redshift construction gives
\[
|n_{\rm peak}|=R-O(1)
\]
with bounded physical inverse scale. A center obstruction gives a residual field remaining in a fixed compact region. A peak whose inverse scale tracks \(\kappa_{\max}\) reflects discretization rather than an outer geometric layer.

The restriction of the optimized metrics to \(|n|\le r_*\), for fixed \(r_*\), should also be compared as \(R\) varies. Convergence there would indicate that the center is approaching one common charged Einstein continuation while the taper migrates outward.

### C. Scale-normalized Jacobian and adjoint projections

At each converged candidate \(X_R\), form the exact linearization
\[
J_R=D_X(\operatorname{Ric}_{g_X}+3g_X).
\tag{14}
\]
Jacobian-vector and adjoint-vector products can use automatic differentiation or the Fréchet formula
\[
D e^X[V]=\int_0^1e^{(1-t)X}Ve^{tX}\,dt,
\tag{15}
\]
rather than finite differences.

Raw Euclidean singular values depend strongly on nodal coordinates. A geometric input norm is
\[
\|V\|_{\mathcal X}^2
=\int\left|
q^{-1/2}Dq_X[V]q^{-1/2}
\right|_F^2d\mu_g,
\tag{16}
\]
and the output norm is (9). The generalized singular system
\[
J_Rv_j=\sigma_ju_j,\qquad J_R^*u_j=\sigma_jv_j
\tag{17}
\]
then has a reproducible normalization.

For every mode record
\[
\pi_j=\langle u_j,E_R\rangle,\qquad
a_j=\frac{|\pi_j|}{\sigma_j},
\tag{18}
\]
together with its physical inverse scale
\[
\kappa_j^2=
\frac{\int|\nabla(q^{-1/2}Dq[v_j]q^{-1/2})|^2d\mu_g}
{\int|q^{-1/2}Dq[v_j]q^{-1/2}|^2d\mu_g}
\tag{19}
\]
and its radial localization. Since Ricci is second order, \(\sigma_j\sim\kappa_j^2\) at high frequency; the reduced value
\[
\widetilde\sigma_j=\frac{\sigma_j}{1+\kappa_j^2}
\tag{20}
\]
isolates geometrically soft modes from ordinary high-frequency stiffness.

A useful cumulative picture is
\[
P_R(\tau)^2
=\sum_{\sigma_j\le\tau}|\pi_j|^2
+\|\Pi_{\ker J_R^*}E_R\|^2,
\qquad
A_R(\tau)^2
=\sum_{\sigma_j>\tau}\frac{|\pi_j|^2}{\sigma_j^2}.
\tag{21}
\]
It displays how much residual lies in weakly responsive left modes and how large a first-order correction would be needed at each inverse singular scale.

A construction signature is a soft right mode localized near \(|n|=R-O(1)\), with bounded \(\kappa_j\) and \(\widetilde\sigma_j\) scaling like \(\eta^3\) or \(\eta^2\), accompanied by corresponding decay of \(\pi_j\) and of the nonlinear residual. A prospective obstruction is a smooth low-\(\kappa\) left field that stabilizes under both resolution and \(R\), satisfies \(J_R^*u_R\to0\), and retains a nonzero pairing with the residual or center data. Its block decomposition would show whether it is a charge-work, horizontal TT/Hopf, or target-current mode and could lead to an integral identity.

---

## 4. Exact exterior comparison

For a flat three-torus metric \(\bar q\),
\[
g=dn^2+f(n)^2\bar q
\]
has
\[
\operatorname{Ric}_{nn}=-3\frac{f''}{f},\qquad
\operatorname{Ric}_{ij}
=-\bigl(ff''+2(f')^2\bigr)\bar q_{ij}.
\]
Thus \(\operatorname{Ric}=-3g\) requires
\[
f''=f,\qquad (f')^2=f^2,
\]
so the expanding solution is exponential. For \(f=\cosh n\),
\[
E_{ij}=2\bar q_{ij},\qquad
\|E_{TT}\|_{\rm op}=2\cosh^{-2}n.
\]
A cosh segment may provide prescribed terminal data, but its residual must remain in the complete tensor norm; it does not solve the inner transition.

This experiment is a global finite-domain residual problem, not a normal Einstein evolution. The known elliptic Cauchy instability is therefore exposed through the scale-normalized singular spectrum rather than presumed removed by a coordinate choice. A persistent residual level pertains to the represented \(T^2\)-invariant Gaussian class; a decaying, continuously verified sequence supplies an actual small-defect mechanism in that class.