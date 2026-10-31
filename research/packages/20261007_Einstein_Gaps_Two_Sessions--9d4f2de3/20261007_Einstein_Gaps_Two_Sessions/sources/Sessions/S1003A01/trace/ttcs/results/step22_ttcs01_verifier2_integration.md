# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 22,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step22_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step22_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the existing angular/SU(2) Hessian artifacts and formulate the smallest scientifically useful non-SU(2) construction probe on the current x0=.038, X=512 scalar-normalized/near-normalized cell. Check which claims from the SU(2) Galerkin Hessian are actually supported, how to construct globally smooth low SU(2)-isotype symmetric-2-tensor modes (rather than raw Euler trigonometric functions), and how to distinguish a geometric descent from a Lie-derivative or nonstationary-base artifact. Give explicit perturbation formulas or an executable finite-dimensional design if possible, while keeping numerical evidence distinct from a theorem.

## Integrated Scientific Memo

# Minimal non-\(\mathrm{SU}(2)\) construction probe for the \(x_0=.038,\ X=512\) cell

## 1. What the existing Hessian artifacts actually support

### Off-diagonal \(\mathrm{SU}(2)\)-invariant sector

For a diagonal Bianchi IX background
\[
g_0=\frac{dx^2}{4G(x)}+\sum_{a=1}^3 h_a(x)\sigma_a^2,
\]
the three off-diagonal channels \(\sigma_1\odot\sigma_2\), \(\sigma_1\odot\sigma_3\), and \(\sigma_2\odot\sigma_3\) carry distinct characters of the sign-flip subgroup \(\mathbb Z_2^2\). Diffeomorphism invariance therefore implies exactly that:

- the first variation vanishes in each such channel;
- mixed Hessian entries between distinct channels vanish;
- mixed entries between these channels and invariant diagonal modes vanish.

Thus the reported gradient \(\lesssim2\times10^{-11}\) and off-block entries \(\lesssim10^{-13}\) validate symmetry, differentiation, and quadrature, but **do not establish stationarity of the base in the diagonal/lapse sector**.

The converged generalized values reported in the note,
\[
80.129,\qquad 260.65,\qquad 462.25,
\]
are strong finite-dimensional evidence for positivity of the three sampled off-diagonal blocks. They are not an infinite-dimensional lower bound. Also, the visible `su2_offdiag_hessian.py` computes ordinary coefficient-space eigenvalues; the quoted generalized normalization
\[
\int_0^1 (k_{ij}/N_{ij})^2\,du
\]
belongs to an unavailable companion script. Hence the table cannot be independently reconstructed from the visible artifact alone.

### Bolt rotations

Using
\[
h(\psi)=R(\psi\chi)\,h\,R(\psi\chi)^T
\]
is essential: it remains a positive metric at the bolt, whereas the discarded affine path \(h+\psi[\Psi,h]\) can be indefinite there.

However,
\[
\frac{d^2}{d\psi^2}J_6(g(\psi))\Big|_0
=
D^2J_6(g_0)[k,k]+DJ_6(g_0)[g''(0)].
\]
Therefore \(0.6053\) is rigorously a **curve stiffness**, not automatically the affine Hessian quadratic form. Interpreting it as the latter requires control of the diagonal/lapse residual, because \(g''(0)\) is diagonal. Its positive sign and stability are nevertheless meaningful.

The \((1,2)\)-rotation value tending to zero is a strong exact-symmetry calibration: it is the \(U(1)\) isometric phase mode.

### Scope of the current conclusion

The supplied evidence supports:

> No negative second variation was found in the tested off-diagonal \(\mathrm{SU}(2)\)-invariant spaces, and the nontrivial bolt-twist curve has positive stiffness.

It does **not yet prove** strict local minimality among all \(\mathrm{SU}(2)\)-invariant metrics. That stronger claim additionally needs:

1. the diagonal/lapse block in a common geometric Gram norm;
2. radial reparametrization gauge removal;
3. invariant \(dx\,\sigma_a\) shifts, or a justified slice eliminating them;
4. an infinite-dimensional coercivity argument.

The earlier raw radial negative eigenvalues in the A02 work cannot fill this gap: they occurred with a large projected gradient, nonlinear metric parametrization, no gauge quotient, and poor convergence.

---

## 2. Why the existing angular prototypes are not evidence

Neither `o11_full_hessian.py` nor `o11_full_hessian2.py` currently gives interpretable non-\(\mathrm{SU}(2)\) spectral information.

- The first script claims a Bianchi/DeTurck penalty in its docstring, but implements none.
- Constant coordinate tensors and raw Euler functions need not extend smoothly across Euler-coordinate singular sets.
- The family
  \[
  1,\cos\psi,\sin\psi,\cos\theta,\sin\theta\cos\phi,\sin\theta\sin\phi
  \]
  is not a complete Peter–Weyl isotype.
- In the geometric-coframe script, constant angular coefficients are just the \(j=0\), \(\mathrm{SU}(2)\)-invariant sector.
- Angular quadrature with \(2\) or \(3\) points per angle is inadequate for a spectral claim.
- The radial envelope \((u(1-u))^2\) does not give \(C^2\) contact with an exact collar when extended by zero.
- Both scripts compute \(P\), not the relevant
  \[
  J_6=P+\frac14\int(s+24)^2\,dV.
  \]
- No diffeomorphism quotient is performed.
- No numerical output from these scripts is supplied here.

At an exactly scalar-normalized base,
\[
D^2J_6[k,k]
=
D^2P[k,k]+\frac12\int (Ds[k])^2\,dV
\]
before division by \(8\pi^2\). Thus a negative raw \(P\)-mode need not be a negative \(J_6\)-mode.

---

## 3. Smallest robust globally smooth non-\(\mathrm{SU}(2)\) block

The safest first computation should avoid bolt regularity altogether by using a radial bump supported strictly inside the cell. This is smaller and less convention-sensitive than implementing the exact bolt charge rules immediately.

Let
\[
u(x)=\frac{\log(x/x_0)}{\log(X/x_0)}
\]
and choose \(0<u_-<u_+<1\), preferably covering the curvature-producing core while staying away from both ends. Set
\[
b(u)=
\begin{cases}
C\exp\!\left[-\dfrac{(u_+-u_-)^2}
{(u-u_-)(u_+-u)}\right],&u_-<u<u_+,\\
0,&\text{otherwise},
\end{cases}
\]
with \(\max b=1\). Every derivative vanishes at \(u_\pm\), so modes built from \(b\) extend smoothly through the bolt and exact collar.

Use the background orthonormal coframe
\[
\vartheta^0=\frac{dx}{2\sqrt G},\qquad
\vartheta^a=\sqrt{h_a}\,\sigma_a.
\]

### Recommended first block: fixed-row \(j=1\)

Represent \(q\in SU(2)\) by a unit quaternion and let
\[
R(q)=\operatorname{Ad}(q)\in SO(3).
\]
For a fixed row \(m\), define
\[
F_r(q)=\sqrt3\,R_{mr}(q),\qquad r=1,2,3.
\]
These are globally smooth, descend under \(q\mapsto -q\), and satisfy under normalized Haar measure
\[
\int F_r\,d\mu=0,\qquad
\int F_rF_s\,d\mu=\delta_{rs}.
\]

The tensor modes are
\[
B_{r,AB}
=
b(u)F_r(q)\,\vartheta^A\odot\vartheta^B,
\qquad
r=1,2,3,\quad 0\le A\le B\le3.
\]
This is a \(3\times10=30\)-dimensional real block.

It is the smallest topology-robust complete isotypic multiplicity block compatible with the current coframe/Euler machinery. By Schur symmetry, one fixed row suffices; repeating the computation with another row should reproduce the spectrum.

### Mathematically lowest isotype

If the principal orbit is confirmed to be \(S^3=SU(2)\), rather than \(SO(3)\), the first nontrivial scalar isotype is \(j=\tfrac12\). In quaternion/complex coordinates
\[
z_1=q_0+iq_1,\qquad z_2=q_2+iq_3
\]
up to the implementation’s convention, the four real functions
\[
\Re z_1,\ \Im z_1,\ \Re z_2,\ \Im z_2
\]
give a \(4\times10=40\)-dimensional block
\[
B_{\mu,AB}=b(u)f_\mu(q)\,\vartheta^A\odot\vartheta^B.
\]
This is the genuinely first isotype and may contain displacement-like modes. It should follow the \(j=1\) implementation unless the orbit topology and Euler periods are already unambiguous.

The more delicate charge-adapted bolt modes are valuable later, but are unnecessary for the first scientifically useful probe. Interior support sacrifices no validity; it only restricts the tested radial subspace.

---

## 4. Explicit coordinate realization

Let \(E(q)\) convert invariant one-forms to Euler-coordinate one-forms, and define
\[
C(q)=\operatorname{diag}(1,E(q)),\qquad
L(x)=\operatorname{diag}\!\left(
\frac1{2\sqrt G},\sqrt{h_1},\sqrt{h_2},\sqrt{h_3}
\right).
\]
If \(S_{AB}\) is the symmetric unit matrix representing \(e_A\odot e_B\), then
\[
B_{r,AB}(x,q)
=
b(u)F_r(q)\,
C(q)^TL(x)S_{AB}L(x)C(q).
\]

Use the affine metric family
\[
g(a)=g_0+\sum_i a_iB_i.
\]
Affine parametrization is important: a nonlinear parametrization contributes
\[
DJ_6(g_0)\!\left[\frac{\partial^2g}{\partial a_i\partial a_j}\right]
\]
to the computed second derivative whenever the base is not exactly stationary.

The objective must be
\[
\mathcal J(a)=\frac1{8\pi^2}\int
\left(
|\operatorname{Ric}^{\circ}_{g(a)}|^2
+\frac14(s_{g(a)}+24)^2
\right)dV_{g(a)}.
\]

A direct code adaptation is:

```python
def mode_tensor(y, r, A, B):
    x, ang = y[0], y[1:]
    G, h = prof(x)
    C = block_diag(1.0, euler_E(ang))
    L = diag(1/(2*sqrt(G)),
             sqrt(h[0,0]), sqrt(h[1,1]), sqrt(h[2,2]))
    S = symmetric_unit_matrix(A, B)
    return bump(u(x)) * F[r](ang) * (C.T @ L @ S @ L @ C)

def metric(y, a):
    return g0(y) + tensordot(a, mode_stack(y), axes=1)

def density(y, a):
    s, ric0sq, _, _ = curvature_scalars(lambda z: metric(z, a), y)
    gm = metric(y, a)
    return (ric0sq + 0.25*(s+24.0)**2) * sqrt(det(gm))
```

The angular integration must be Haar-calibrated. A quaternion spherical design is preferable to low-order Euler-product quadrature:

- for \(j=1\), a \(24\)-cell design integrates the required degree-four angular products exactly in the ideal representation-level computation;
- a \(600\)-cell or refined Haar quadrature supplies an independent check;
- left-translate the design by a generic quaternion if the curvature routine has Euler-coordinate singularities.

Mandatory calibrations are
\[
\sum_\alpha w_\alpha F_r(q_\alpha)=0,\qquad
\sum_\alpha w_\alpha F_r(q_\alpha)F_s(q_\alpha)=\delta_{rs},
\]
and
\[
\mathcal J(0)\approx0.99517819
\]
for the \(X=512\) record.

---

## 5. Gauge quotient

For the same angular isotype, choose compactly supported vector fields
\[
X_{rA}=c(u)F_r(q)E_A,
\]
where \(E_A\) is dual to \(\vartheta^A\), initially with \(c=b\). Compute the exact coordinate Lie derivatives
\[
L_{rA}=\mathcal L_{X_{rA}}g_0,
\]
using
\[
(\mathcal L_Xg)_{\mu\nu}
=
X^\rho\partial_\rho g_{\mu\nu}
+g_{\rho\nu}\partial_\mu X^\rho
+g_{\mu\rho}\partial_\nu X^\rho.
\]
For fixed-row \(j=1\), this gives \(3\times4=12\) gauge tensors.

With the geometric \(L^2\) pairing, form
\[
G_{ij}=\langle B_i,B_j\rangle,\qquad
A_{ab}=\langle L_a,L_b\rangle,\qquad
C_{ai}=\langle L_a,B_i\rangle.
\]
Project by
\[
\widetilde B_i
=
B_i-\sum_{a,b}L_a(A^+)_{ab}C_{bi},
\]
where \(A^+\) is the pseudoinverse after discarding genuinely null vector fields. Solve
\[
H_{\rm slice}v=\lambda G_{\rm slice}v
\]
on the independent span of the \(\widetilde B_i\).

A second vector radial profile,
\[
c_1(u)=(2u-u_--u_+)b(u),
\]
tests whether the one-profile gauge space is too small. Ultimately, the canonical isotypic projection solves
\[
\delta_g\mathcal L_Xg=\delta_gk
\]
with \(X\) vanishing near both ends; after Peter–Weyl reduction this is a radial ODE system.

---

## 6. Distinguishing geometric descent from gauge and base-residual artifacts

### Symmetry-forced first variation

For every nontrivial isotype,
\[
DJ_6(g_0)[k]
=
DJ_6(g_0)\!\left[\int_{SU(2)}L_a^*k\,da\right]=0.
\]
This remains true even if the base is nonstationary in the invariant sector. Therefore a persistent nonzero angular-block gradient indicates an error in the mode construction, angular measure, or coordinate treatment; it is not a useful stationarity diagnostic.

### Diffeomorphism Ward identities

For a compactly supported vector field \(X\),
\[
J_6(\phi_t^*g_0)=J_6(g_0).
\]
Consequently, for \(k=\mathcal L_Xg_0\),
\[
D^2J_6(g_0)[k,k]
+
DJ_6(g_0)[\mathcal L_X^2g_0]=0,
\]
and more generally
\[
D^2J_6(g_0)[h,\mathcal L_Xg_0]
=
-DJ_6(g_0)[\mathcal L_Xh].
\]
These are the functional counterparts of the reparametrization identities in Ozuch’s Proposition 1.3.

They explain the central pitfall: at a nonstationary base, an **affine** Lie-derivative direction need not be a Hessian zero mode. The defect is controlled by the invariant residual because products of two modes in the same nontrivial isotype contain \(j=0\).

Accordingly, record:

1. the invariant diagonal/lapse gradient in a sufficiently rich \(j=0\) space;
2. the Hessian restricted to represented Lie derivatives;
3. the residuals in the identities above.

If the apparent negative eigenvalue scales with those residuals or disappears after re-optimizing the invariant base, it is not established as geometric.

### Direct line test

For a projected, Gram-normalized candidate \(k\), compute
\[
Q_{\rm even}(\epsilon)=
\frac{J_6(g_0+\epsilon k)+J_6(g_0-\epsilon k)-2J_6(g_0)}
{\epsilon^2},
\]
and
\[
Q_{\rm odd}(\epsilon)=
\frac{J_6(g_0+\epsilon k)-J_6(g_0-\epsilon k)}
{2\epsilon}.
\]
A genuine quadratic descent requires, over a decreasing range such as
\[
\epsilon\|g_0^{-1}k\|_\infty
\in\{10^{-3},\,5\times10^{-4},\,2.5\times10^{-4}\},
\]
that
\[
Q_{\rm even}(\epsilon)\to\lambda<0,\qquad
Q_{\rm odd}(\epsilon)\to0,
\]
while the quotient norm
\[
\inf_X\|k-\mathcal L_Xg_0\|_{L^2}
\]
stays bounded away from zero.

Also perturb the base by a small invariant residual direction \(v_0\):
\[
g_\eta=g_0+\eta v_0.
\]
A geometric eigenvalue should vary smoothly and remain separated from zero; a gauge/residual artifact commonly changes approximately linearly with \(\eta\) and crosses zero near the current base.

---

## 7. Scalar normalization and interpretation

The \(X=512\) profile is only near scalar-normalized. There are two clean options.

1. Evaluate \(J_6\) on the supplied base. A verified decrease is already useful.
2. First replace it by its Yamabe-normalized representative and recompute the Hessian there.

At an exactly normalized base, the scalar-constrained tangent correction is obtained from
\[
(-6\Delta+48)v=-Ds_{g_0}[k],
\qquad
k_Y=k+2vg_0,
\]
so that \(Ds[k_Y]=0\).

More importantly, if an explicit perturbation keeps \(s<0\), the conformal-selection identity gives its constant-scalar representative \(\widehat g\) with
\[
P(\widehat g)\le J_6(g).
\]
Thus a certified \(J_6\) descent yields a genuine constant-scalar \(P\)-upper-bound improvement after normalization. This conclusion applies to an explicit finite perturbation, not merely to an unverified negative numerical eigenvalue.

---

## 8. Minimal recommended run

The smallest useful experiment is therefore:

- the \(x_0=.038,\ X=512\) record;
- the full \(J_6/(8\pi^2)\), not \(P\);
- one \(C^\infty\) radial bump supported away from both ends;
- the fixed-row \(j=1\), \(30\)-tensor block;
- \(12\) exact compactly supported Lie-derivative modes;
- geometric \(L^2\) Gram projection;
- Haar/design angular quadrature calibrated against orthogonality and \(J_0\);
- row-independence and representation-degeneracy checks;
- the Ward identities;
- direct two-sided line tests for any negative projected eigenmode.

If the orbit is confirmed as \(S^3\), repeat with the \(40\)-dimensional \(j=\tfrac12\) block, since it is the true lowest isotype.

A stable negative quotient eigenvalue passing these tests produces an explicit smooth non-\(\mathrm{SU}(2)\) construction direction. Positivity only establishes numerical stability in that chosen radial/isotypic subspace; a theorem would still require isotype-wise coercivity or certified spectral lower bounds.