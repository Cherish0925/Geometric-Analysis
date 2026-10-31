# Round 15: product-boundary rigidity and global shear matching

## Main results

The three investigations meet at the same question: can the fixed closed
shear manifolds constructed in Rounds 11–14 carry a negative Einstein
metric? This round obtains a quantitative restriction on exact outputs
near the sharp volume, computes the actual linear exterior response,
and constructs integral shear data that cancel one global obstruction.
It does not decide Einstein existence on these manifolds.

### 1. Rigidity at a realizable boundary

The earlier integral obstruction concerns an unrealizable Weyl profile
at the monopole ratio \(2/3\). The shear manifolds instead have ratio
\(1\), where the equality model is a genuine hyperbolic product.
The new calculation works with that model rather than trying to reuse
the forbidden-profile contradiction.

Let \(s=-4\kappa\), \(A=2\chi>0\), \(\tau=0\), and assume actual
Seiberg–Witten solutions of square \(A\) in both orientations. Set
\[
 D=\kappa^2\operatorname{Vol}(g)-2\pi^2A,\qquad
 P=\int_M|\operatorname{Ric}^{\circ}|^2.
\]
Writing \(\mathscr P_\kappa\) for the orthogonal orbit of the curvature
operator of \(\mathbb H^2_{-\kappa}\times\mathbb H^2_{-\kappa}\), we prove
\[
 \boxed{\int_M\operatorname{dist}_{\rm HS}
       (\mathcal R_g,\mathscr P_\kappa)^2
       \leq \frac32P+\frac{68}{3}D.}
 \tag{1}
\]
The spinor identities also give
\[
 4D=\int|\nabla_{\mathfrak A}\Phi|^2
       +\kappa\int(4\kappa-|\Phi|^2)
       +2\|F_{\mathfrak A}^{-}\|_2^2.
 \tag{2}
\]
All terms on the right are nonnegative. Constant scalar curvature and
actual monopoles are hypotheses; no Sobolev, diameter, noncollapse,
or full-curvature bound is imposed.

For exact \(\operatorname{Ric}=-3g\), (1), Bishop–Gromov volume upper
bounds, and the Cheeger–Tian absolute-energy regularity theorem imply:
\[
 D\leq D_0\quad\Longrightarrow\quad
 \sup|\nabla^m\operatorname{Rm}|\leq C_m,\qquad m\geq0,
 \tag{3}
\]
with universal constants. Thus exact metrics on a fixed non-Kähler
shear manifold whose volumes approach \(V_*=2\pi^2A/9\) cannot develop
curvature bubbles, even in collapsing regions.

Their diameters must diverge. Suitable basepoints have a complete,
noncompact, finite-volume smooth pointed limit with universal cover
\(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\). The existence of those
noncollapsed basepoints uses another classical Cheeger–Tian estimate.
The proof does not identify the ends of this limit with the collars of
the chosen construction.

This is a restriction on exact sequences approaching the sharp
scalar-volume bound, not on arbitrary Einstein metrics of larger volume.
The weak-Bianchi calculation retains a source of order \(D\); it does
not produce the positive limiting contradiction from the old
\(2/3\)-boundary argument.

Proof: [product-boundary calibration](round15_rigidity.md), especially
Sections 2–4 and 8.

### 2. The throat response is singular and has a negative boundary mode

For a product collar with
\[
 a(t)=c\cosh(kt),\quad k=\sqrt3,\quad a(R)=A_0,
 \qquad f(t)=\operatorname{sech}^2(kt),
\]
the radial tracefree operator has the exact boundary response
\[
 D_w=-a_R\frac{a'(R)}{a_R}I+
      \frac1{2\Lambda_wf_R^2}
      \begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \qquad
 \Lambda_w=\int_{-R}^{R}\frac{dt}{a f^2}.
 \tag{4}
\]
Its common-boundary eigenvalue tends to \(-kA_0\), while its odd
eigenvalue tends to \(kA_0/2\). The response is not positive
semidefinite; dropping the Robin term changes the matching problem.

The optimized electric shear has an \(O(c^2)\) source. The projected
Bianchi-gauged waist equation with zero Dirichlet data satisfies
\[
 \boxed{c\,v_D(0)\longrightarrow
       \frac{\rho_\beta A_0^3}{4\pi},\qquad
       \rho_\beta=\frac{\|\beta\|_2^2}{\operatorname{Area}(F)}.}
 \tag{5}
\]
Small residual therefore coexists with a divergent response in this
projected boundary problem. Whether exterior feedback removes it while
satisfying the gauge constraints is a genuine equation, not a consequence
of smallness of the residual.

The calculation separates true metric modes, Bianchi-gauged modes,
and pure-gauge twist modes with nontrivial relative boundary rotation.
It gives exact matrices and affine sources, not a presumed nonlinear
Einstein Dirichlet-to-Neumann operator.

Proof: [throat response and gauge data](round15_boundary_response.md).

### 3. An actual exterior gives a global compatibility equation

For a hyperbolic product exterior \(B\times F\), the Einstein–Hilbert
action including its mean-curvature boundary term is exactly
\[
 \int_{B\times F}(s+6)+2\int_{\partial(B\times F)}H
       =4\pi\chi(B)\operatorname{Area}(F).
 \tag{6}
\]
An arbitrary infinitesimal Einstein deformation, with no imposed
symmetry, projects onto the fiber TT space as a harmonic function on
\(B\). Its total outward conormal is zero. The physical boundary
momentum contains a Robin term; that term cancels across a matched
interface and has not been discarded.

Harmonic measures of the actual compact base define its capacitance
matrix
\[
 C_{ij}=\frac12\int_B\langle d\omega_i,d\omega_j\rangle.
 \tag{7}
\]
This matrix is positive semidefinite with precisely the common-constant
kernel. Assemble it with the collar responses in a connected network
with common marked fiber and identity fiber gluing. The averaged
linear TT matching system is solvable if and only if
\[
 \boxed{\sum_e q_e
       \left(\beta_e\otimes\beta_e-\tfrac12|\beta_e|^2h_F\right)=0,
       \qquad q_e=\int a_e^3(z_e')^2\,dt.}
 \tag{8}
\]
It is then unique modulo a common fiber deformation. Nonconstant
boundary data, waist modes, normal constraints, and nonlinear exterior
response remain in the full problem. The note derives the retained
quadratic exterior remainder explicitly.

Proof: [exterior response and physical matching](round15_global.md).

### 4. Integral topology allows cancellation, but not for every pair

Equation (8) is the first variation of
\[
 \mathcal H_q(h)=\sum_e q_e\|\beta_e(h)\|_2^2
\]
on marked hyperbolic fiber metrics. Its harmonic-map interpretation
is classical: it is the vanishing of the Hopf differential of the
associated map to a flat torus.

For two nonzero integral classes,
\[
 d=(2\pi)^{-2}\int_F b_1\wedge b_2
\]
is decisive. Balance forces a holomorphic or antiholomorphic branched
cover of a torus of degree \(|d|\). Hence \(d=0\) and \(|d|=1\)
cannot balance when the fiber genus is at least two.

There is an explicit degree-two balanced example: take the genus-two
double cover of a square torus, branched at two points, and pull back
\(dx,dy\). The two forms have integral periods and are Hodge duals,
so their TT stresses cancel for equal capacities. Both are legitimate
circle-valued shear data.

Use them on two self-gluings of \(B_{r,4}\times F\), with identical
collar profiles. This gives a fixed closed near-Einstein family with
\(\chi=4r+4\). Its normalized Einstein–Hilbert functional satisfies
the exact identity
\[
 \mathcal S(G_c)=-12\sqrt{V_*}
                 -\frac{\pi}{\sqrt{V_*}}\mathcal H_q(h_F).
 \tag{9}
\]
Consequently it is stationary under every simultaneous hyperbolic
fiber variation, for every collar size. This is an actual closed
family, not a formal cancellation of nonintegral Hodge duals.
The nonzero waist forces remain on their separate collars.

Proof: [integral balancing and closed variation](round15_shear_balance.md).

## What changed relative to Round 14

| Earlier result | New step in this round |
| --- | --- |
| A small all-mode repair neighborhood is excluded by a localized waist receiver. | The full finite-collar linear response and its boundary source are computed; an actual exterior response is included in the TT sector. |
| Closed shear examples realize small Ricci defect at the product boundary. | Actual monopoles control distance from the full product curvature model; exact sharp-volume degeneration cannot develop curvature bubbles. |
| A single shear has a nonzero fiber force. | A global compatibility equation is derived. Integral rank-two data distinguish impossible degree-zero/one balance from a realizable degree-two balance. |
| Exact outputs cannot retain local continuous symmetry on the specified topology. | Near the sharp volume, any exact sequence must degenerate through bounded-curvature long geometry with a noncompact product-locally-symmetric limit. |

The new compactness consequence uses classical regularity after the new
calibration estimate. The harmonic-map and capacitance interpretations
likewise use established mathematics. No claim of literature priority
is inferred from these derivations.

## The next decisive problems

The computations identify two concrete routes, without requiring that
every future argument follow them.

1. **Complete the boundary equations on balanced data.** The degree-two
   example removes the fiber-average obstruction. Determine the actual
   exterior response in the waist and remaining tensor sectors, with
   the constraints and nonlinear remainder retained. A successful
   Einstein repair may break all continuous symmetry; a no-repair
   argument must address such corrections as well.
2. **Classify the bounded-curvature exact degeneration forced by (3).**
   Establish which finite-volume product quotients and end matchings
   can occur on the fixed shear topology. The present pointed limit
   does not supply this identification, nor does it exclude exact
   metrics whose volumes stay above \(V_*\).

These questions interact: the local matching equations describe how
ends could be joined, while the exact-output theorem controls the
geometry in which sharp-volume joining would have to occur.
Neither supplies global Einstein nonexistence yet. The separate positive
branch also remains necessary for a full fixed-dimensional disproof
of the project's Yau26 statement.

## Proofs and reproduction

Four proof notes and four runnable checks accompany this report:

| Proof | Check |
| --- | --- |
| [Rigidity](round15_rigidity.md) | [Symbolic identities](round15_rigidity_check.py) |
| [Throat response](round15_boundary_response.md) | [Exact equations and numerical asymptotics](round15_boundary_response_check.py) |
| [Exterior matching](round15_global.md) | [Boundary and capacitance identities](round15_global_check.py) |
| [Integral balance](round15_shear_balance.md) | [Energy, degree, and gluing identities](round15_shear_balance_check.py) |

See [verification](round15_verification.md) for the run scope and
independent proof reviews. The inherited Round-1–14 files remain intact.
