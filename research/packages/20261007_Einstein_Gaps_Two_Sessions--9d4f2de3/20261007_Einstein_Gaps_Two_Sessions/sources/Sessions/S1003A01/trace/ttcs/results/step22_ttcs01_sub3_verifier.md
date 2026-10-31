# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Sessions/S1003A01/workspace/scripts/su2_offdiag_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian2.py",
    "Sessions/S1003A02/workspace/notes/step9_universal_cell_response_and_spectral_pressure.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Read the existing angular/SU(2) Hessian artifacts and formulate the smallest scientifically useful non-SU(2) construction probe on the current x0=.038, X=512 scalar-normalized/near-normalized cell. Check which claims from the SU(2) Galerkin Hessian are actually supported, how to construct globally smooth low SU(2)-isotype symmetric-2-tensor modes (rather than raw Euler trigonometric functions), and how to distinguish a geometric descent from a Lie-derivative or nonstationary-base artifact. Give explicit perturbation formulas or an executable finite-dimensional design if possible, while keeping numerical evidence distinct from a theorem.

## Output

# Scientific memo: minimal globally smooth non-\(\mathrm{SU}(2)\) Hessian probe

## 1. What the existing Hessian artifacts establish

### 1.1 The \(\mathrm{SU}(2)\)-invariant off-diagonal experiment

For the diagonal Bianchi IX background, the three off-diagonal channels \(h_{12},h_{13},h_{23}\) transform by distinct characters of the \(\mathbb Z_2\times \mathbb Z_2\) sign-flip subgroup. Consequently,

\[
DJ_6(g)[k_{ij}]=0,\qquad
D^2J_6(g)[k_{ij},k_{kl}]=0
\]

when the two channels have different characters. Thus the reported gradient of order \(10^{-11}\) and off-block entries of order \(10^{-13}\) verify the curvature implementation, quadrature, and discrete symmetries. They do **not** measure stationarity in the diagonal/lapse sector: the first variation in every off-diagonal channel vanishes by symmetry for any diagonal background.

The reported convergence

\[
\mu_{\min}(h_{12})\to 80.129,\quad
\mu_{\min}(h_{13})\to260.65,\quad
\mu_{\min}(h_{23})\to462.25
\]

at \(X=512\) is substantial numerical evidence that the selected radial Chebyshev spaces contain no downward off-diagonal direction. It is finite-dimensional evidence only. The visible script `su2_offdiag_hessian.py` itself computes ordinary coefficient-space eigenvalues using `np.linalg.eigh(Hb)`. The table in the note refers to a separate generalized spectrum script and the norm

\[
\int (k_{ij}/N_{ij})^2\,du,
\]

but that script and its output are not supplied here, so the numerical values in that normalization cannot be independently reconstructed from the visible file.

The exact bolt-rotation paths are materially better than the discarded affine rotations. An affine off-diagonal perturbation of a semidefinite orbit matrix at the bolt can make the coordinate orbit matrix indefinite for every nonzero parameter, whereas \(R(\psi)hR(\psi)^T\) stays within metrics. There is, however, a distinction between:

* the Fréchet Hessian along an affine path \(g+\epsilon k\); and
* the second derivative along a curved path \(g(\epsilon)\), which equals
  \[
  D^2J_6(g)[k,k]+DJ_6(g)[g''(0)].
  \]

Therefore the reported twist value \(0.6053\) is a path stiffness. It equals a Hessian quadratic form only when the first variation against the rotational acceleration is negligible. The script reports only the symmetry-forced off-diagonal gradient, not the diagonal/lapse residual needed for that conclusion. The mode tending to zero in the \((1,2)\) rotation is nevertheless an excellent diffeomorphism test, because the corresponding \(U(1)\) path is isometric.

The supplied artifact does not by itself establish strict local minimality among all \(\mathrm{SU}(2)\)-invariant metrics. Such a statement also uses:

1. positivity in the diagonal and lapse sector;
2. treatment of invariant \(dx\,\sigma_i\) shifts, or an explicit radial gauge reduction;
3. endpoint relative rotations;
4. an infinite-dimensional coercive estimate rather than increasing finite Chebyshev spaces.

Mixed diagonal/off-diagonal Hessian entries vanish by the same sign-flip symmetry, so a separately verified diagonal block would combine cleanly with the present off-diagonal blocks.

### 1.2 The two angular prototypes

`o11_full_hessian.py` and `o11_full_hessian2.py` do not yet provide interpretable non-\(\mathrm{SU}(2)\) spectral evidence.

* The first script states that a DeTurck/Bianchi penalty is added, but no such term is present in the source. It returns the raw Hessian of \(P\).
* Constant coordinate-component tensors in Euler coordinates are generally not smooth tensor fields through the Euler polar sets.
* The raw functions \(\cos\psi,\sin\psi,\cos\theta,\sin\theta\cos\phi,\sin\theta\sin\phi\) do not form a complete Peter–Weyl block and some depend on the Euler seam conventions.
* In `o11_full_hessian2.py`, constant coefficients in the invariant coframe are globally defined, but they are precisely the \(j=0\), hence \(\mathrm{SU}(2)\)-invariant, sector.
* Its `basic` angular family is still not a complete irreducible block.
* The radial factor \((u(1-u))^2\) has a nonzero second derivative at the end faces. When concatenated with the exact collar, it does not give \(C^2\) contact.
* Both angular scripts compute \(P\), not \(J_6\).
* The angular quadratures \(nqa=2\) or \(3\) are too small for a spectral conclusion, and no numerical output was supplied.

The distinction between \(P\) and \(J_6\) is essential. At an exactly scalar-normalized background \(s=-24\),

\[
D^2\!\left(\frac{J_6}{8\pi^2}\right)[k,k]
=
D^2\!\left(\frac{P}{8\pi^2}\right)[k,k]
+\frac{1}{16\pi^2}\int (D s_g[k])^2\,dV_g.
\]

Thus a downward direction for the raw \(P\)-Hessian may disappear once the scalar square is included.

---

## 2. Globally smooth low-isotype tensor modes

Write the diagonal background as

\[
g_0=\frac{dx^2}{4G(x)}+\sum_{a=1}^3 h_a(x)\sigma_a^2,
\]

and use the orthonormal coframe on the principal-orbit region

\[
\vartheta^0=\frac{dx}{2\sqrt G},\qquad
\vartheta^a=\sqrt{h_a}\,\sigma_a.
\]

The \(\sigma_a\) are globally defined left-invariant forms. Hence, if \(F(q)\) is a globally defined scalar matrix coefficient on \(\mathrm{SU}(2)\), then

\[
F(q)\,\vartheta^A\odot\vartheta^B
\]

is a globally defined symmetric tensor away from the bolt. Taking a radial coefficient identically zero in neighborhoods of both ends makes the tensor smooth on the entire cell without any bolt isotropy calculation.

Let

\[
u=\frac{\log(x/x_0)}{\log(X/x_0)}
\]

and choose \(0<u_-<u_+<1\). A useful smooth radial bubble is

\[
b(u)=
\begin{cases}
C\exp\!\left[-\dfrac{(u_+-u_-)^2}
{(u-u_-)(u_+-u)}\right],&u_-<u<u_+,\\[1.2ex]
0,&\text{otherwise},
\end{cases}
\]

where \(C\) normalizes \(\max b=1\). All derivatives vanish at \(u_\pm\).

### 2.1 The first isotype for a Burns \(O(-1)\) cell

For the Burns cell the principal orbit is \(S^3\simeq\mathrm{SU}(2)\), so the first scalar Peter–Weyl isotype is \(j=\tfrac12\). In standard Euler variables,

\[
z_1=e^{i(\alpha+\gamma)/2}\cos(\beta/2),\qquad
z_2=e^{i(\alpha-\gamma)/2}\sin(\beta/2),
\]

and the four real functions

\[
f_\mu\in
\{\Re z_1,\Im z_1,\Re z_2,\Im z_2\}
\]

are globally smooth coordinate functions on \(S^3\). The complete one-radial-bubble tensor space is

\[
k_{\mu,AB}
=
b(u)f_\mu(q)\,\vartheta^A\odot\vartheta^B,
\qquad
0\leq A\leq B\leq3.
\]

It has \(4\times10=40\) real dimensions. Because the coframe is left invariant, this is a complete \(j=\tfrac12\) coefficient block, including the radial-angular components absent from the previous \(h_{ij}\)-only experiment.

If the actual Euler implementation has imposed \(q\sim -q\), these functions do not descend. That topology can be settled by the angle ranges and the base-volume calibration.

### 2.2 A topology-robust \(j=1\) block

A robust alternative uses the adjoint matrix \(R(q)=\operatorname{Ad}(q)\in SO(3)\), which is invariant under \(q\mapsto -q\). For \(q=(q_0,q_1,q_2,q_3)\),

\[
R(q)=
\begin{pmatrix}
1-2(q_2^2+q_3^2)&2(q_1q_2-q_0q_3)&2(q_1q_3+q_0q_2)\\
2(q_1q_2+q_0q_3)&1-2(q_1^2+q_3^2)&2(q_2q_3-q_0q_1)\\
2(q_1q_3-q_0q_2)&2(q_2q_3+q_0q_1)&1-2(q_1^2+q_2^2)
\end{pmatrix}.
\]

For a fixed row \(m\), define

\[
F_b(q)=\sqrt3\,R_{mb}(q),\qquad b=1,2,3.
\]

Normalized Haar integration gives

\[
\int F_bF_c\,d\mu=\delta_{bc},\qquad
\int F_b\,d\mu=0.
\]

Since the Hessian commutes with the left \(\mathrm{SU}(2)\) action, its matrix has the form \(\delta_{mm'}A\). One fixed row therefore gives the complete multiplicity matrix. The minimal block is

\[
k_{b,AB}=b(u)F_b(q)\,\vartheta^A\odot\vartheta^B,
\]

with \(3\times10=30\) dimensions. Repeating one eigenvector with another row is a direct numerical test of the expected threefold degeneracy.

This \(30\)-dimensional \(j=1\) block is the smallest immediately robust construction using the current Euler/coframe machinery. The \(40\)-dimensional \(j=\tfrac12\) block is the mathematically first isotype for the Burns topology.

---

## 3. Minimal executable design

In the coordinate notation of `o11_full_hessian2.py`, let

\[
C(q)=\operatorname{diag}(1,E(q)),\qquad
A(x)=\operatorname{diag}\!\left(
\frac1{2\sqrt G},\sqrt{h_1},\sqrt{h_2},\sqrt{h_3}
\right).
\]

If \(S_{AB}\) is the constant symmetric matrix representing
\(e_A\odot e_B\), the coordinate components of a mode are

\[
B_{r,AB}(x,q)
=
b(u)F_r(q)\,
C(q)^T A(x)S_{AB}A(x)C(q).
\]

The affine family is

\[
g(a)=g_0+\sum_i a_iB_i.
\]

For sufficiently small \(a\), positivity follows directly from the background-orthonormal normalization. The functional used in the Hessian is

\[
\frac{1}{8\pi^2}\int
\left(
|\operatorname{Ric}^{\circ}|^2
+\frac14(s+24)^2
\right)dV.
\]

A direct adaptation of the existing JAX code is schematically:

```python
def mode_tensor(y, r, Aidx, Bidx):
    x, ang = y[0], y[1:]
    G, h = prof(x)
    C = block_diag(1.0, euler_E(ang))
    L = diag(1/(2*sqrt(G)), sqrt(h[0,0]), sqrt(h[1,1]), sqrt(h[2,2]))
    S = symmetric_unit_matrix(Aidx, Bidx)
    return bump(u(x)) * F[r](ang) * (C.T @ L @ S @ L @ C)

def metric(y, a):
    return g0(y) + tensordot(a, B(y), axes=1)

def density(y, a):
    s, ric0sq, _, _ = curvature_scalars(lambda z: metric(z, a), y)
    gm = metric(y, a)
    return (ric0sq + 0.25*(s+24.0)**2) * sqrt(det(gm))
```

The angular integration should use normalized Haar measure. For standard Euler coordinates this is proportional to

\[
\sin\beta\,d\alpha\,d\beta\,d\gamma,
\]

with the \(\gamma\)-period chosen according to the actual \(S^3\) parametrization. Gauss–Legendre quadrature in \(z=\cos\beta\) and periodic trapezoidal rules in \(\alpha,\gamma\) are natural. Before reading any spectrum, the same quadrature should reproduce:

\[
\int F_r\,d\mu=0,\qquad
\int F_rF_s\,d\mu=\delta_{rs},
\]

and the angular integral of \(J_6(g_0)\) should agree with the radial code value near \(0.99517814\). Repetition at larger angular and radial orders distinguishes a stable eigenvalue from quadrature structure.

---

## 4. Removing Lie-derivative contamination

Let \(E_A\) denote the frame dual to \(\vartheta^A\). In the same isotype, compactly supported vector fields are

\[
X_{rA}=c(u)F_r(q)E_A,
\]

with \(c=b\) in the smallest experiment. Their exact metric tangents are

\[
L_{rA}=\mathcal L_{X_{rA}}g_0,
\]

computed in coordinates by

\[
(\mathcal L_Xg)_{\mu\nu}
=
X^\rho\partial_\rho g_{\mu\nu}
+g_{\rho\nu}\partial_\mu X^\rho
+g_{\mu\rho}\partial_\nu X^\rho.
\]

This gives \(16\) gauge tensors for the \(j=\tfrac12\) block or \(12\) for a fixed-row \(j=1\) block.

Let

\[
A_{ab}=\langle L_a,L_b\rangle_{L^2},\qquad
C_{ai}=\langle L_a,B_i\rangle_{L^2}.
\]

The finite-dimensional slice tensors are

\[
\widetilde B_i
=
B_i-\sum_{a,b}L_a(A^+)_{ab}C_{bi},
\]

where \(A^+\) is the pseudoinverse after removing numerical null vectors. The Hessian and Gram matrices restricted to the \(\widetilde B_i\) then measure directions orthogonal to the represented Lie derivatives. A second vector radial shape, such as

\[
c_1(u)=(2u-u_--u_+)b(u),
\]

tests whether the first gauge space was too small.

A stronger realization solves, within the chosen isotype,

\[
\delta_g\mathcal L_Xg=\delta_g k,\qquad X=0
\ \text{near both ends},
\]

and replaces \(k\) by \(k-\mathcal L_Xg\). Since the background is cohomogeneity one, this is a finite system of radial ODEs after Peter–Weyl decomposition.

---

## 5. Separating a genuine descent from base residual and reparametrization

### 5.1 First variation in a nontrivial isotype

For any nontrivial \(\mathrm{SU}(2)\) isotype,

\[
DJ_6(g_0)[k]
=
DJ_6(g_0)\!\left[\int_{\mathrm{SU}(2)}L_a^*k\,da\right]
=0.
\]

This holds even if \(g_0\) is not stationary in the invariant sector. A computed first derivative that persists with angular refinement therefore indicates an angular-mode, Haar-measure, or coordinate-seam inconsistency.

The same representation argument makes the Hessian block diagonal in \(j\). It also makes the mixed \(j=0\)–\(j>0\) Hessian vanish.

### 5.2 Diffeomorphism Ward identity

For the flow \(\phi_t\) of a compactly supported vector field \(X\),

\[
J_6(\phi_t^*g_0)=J_6(g_0).
\]

Writing \(k=\mathcal L_Xg_0\), differentiation twice gives

\[
D^2J_6(g_0)[k,k]
+
DJ_6(g_0)[\mathcal L_X^2g_0]
=0.
\]

This follows from the Ricci reparametrization identities recorded in Proposition 1.3 of the supplied Ozuch paper. It explains why a raw affine Hessian along a Lie derivative need not vanish when the background still has an invariant-sector gradient: \(\mathcal L_X^2g_0\) contains a \(j=0\) component.

Numerically, the residual in this identity directly measures the combined curvature, differentiation, and quadrature error. It also quantifies how much of an apparent below-zero gauge eigenvalue is generated by the invariant residual.

The relevant invariant residual is obtained from compactly supported \(j=0\) modes in:

\[
\vartheta^0\!{}^2,\quad
\vartheta^1\!{}^2,\quad
\vartheta^2\!{}^2,\quad
\vartheta^3\!{}^2,
\]

together with any invariant shift modes retained by the parametrization. The \(10^{-11}\) off-diagonal gradient from `su2_offdiag_hessian.py` contains no information about this quantity.

### 5.3 Direct two-sided metric evaluation

For a normalized projected eigenmode \(k\), define

\[
Q_{\mathrm{even}}(\epsilon)
=
\frac{J_6(g_0+\epsilon k)+J_6(g_0-\epsilon k)-2J_6(g_0)}
{\epsilon^2},
\]

and

\[
Q_{\mathrm{odd}}(\epsilon)
=
\frac{J_6(g_0+\epsilon k)-J_6(g_0-\epsilon k)}
{2\epsilon}.
\]

As \(\epsilon\to0\),

\[
Q_{\mathrm{even}}(\epsilon)\to D^2J_6(g_0)[k,k],
\qquad
Q_{\mathrm{odd}}(\epsilon)\to0.
\]

A stable value \(Q_{\mathrm{even}}<0\), together with a positive quotient norm

\[
\inf_X\|k-\mathcal L_Xg_0\|_{L^2}>0,
\]

is an explicit metric descent rather than an exact diffeomorphism path. Evaluating several decreasing values of
\(\epsilon\|g_0^{-1}k\|_\infty\) separates the quadratic term from cubic and floating-point effects.

### 5.4 Scalar normalization

For an exactly normalized base, the linear conformal correction \(u=1+\epsilon v\) satisfies

\[
(-6\Delta+48)v=-D s_{g_0}[k].
\]

Thus

\[
k_{\mathrm Y}=k+2vg_0
\]

is tangent to \(s=-24\). This supplies a direct scalar-constrained version of the same isotype block.

More simply, a verified \(J_6\) descent already has the desired geometric consequence. For sufficiently small perturbations the scalar curvature remains \(<0\), and the conformal-selection identity gives a constant-scalar metric \(\widehat g_\epsilon\) with

\[
P(\widehat g_\epsilon)\leq J_6(g_0+\epsilon k).
\]

If the starting cell is only near normalized, the comparison should be made against its normalized representative rather than against the unnormalized \(J_6(g_0)\).

---

## 6. Smallest useful experiment and its interpretation

The smallest complete construction compatible with the present code is:

* current \(x_0=.038,\ X=512\) scalar-normalized profile;
* one smooth radial bubble supported away from the bolt and collar;
* the fixed-row \(j=1\) block: \(30\) tensor modes;
* \(12\) exact Lie-derivative modes;
* the full \(J_6\) functional;
* an \(L^2\) projection away from those Lie derivatives;
* Haar quadrature calibrated by Peter–Weyl orthogonality and the known radial value;
* direct two-sided evaluation of the lowest projected mode;
* the diffeomorphism Ward identity and the invariant-sector gradient recorded alongside the eigenvalue.

For the Burns \(S^3\) topology, the analogous \(j=\tfrac12\) experiment has \(40\) tensor modes and \(16\) Lie-derivative modes and probes the genuinely first nontrivial isotype.

A stable projected eigenvalue below zero would provide an explicit finite-dimensional non-\(\mathrm{SU}(2)\) construction lowering \(J_6\), and after Yamabe normalization, lowering \(P\). Eigenvalues above zero would establish stability only in the selected isotype and radial space. An all-mode theorem would additionally require radial completeness, every allowed \(j\), and a coercive estimate for the gauge-fixed Hessian.