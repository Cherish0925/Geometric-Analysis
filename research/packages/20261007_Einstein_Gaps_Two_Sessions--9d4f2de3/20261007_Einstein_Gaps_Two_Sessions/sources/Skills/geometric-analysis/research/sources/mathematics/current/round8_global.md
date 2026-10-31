# Two conformal ends: an exact OT exclusion and the role of boundary phases

21 September 2026.

This note concerns the actual complete Einstein connector, not a local
Einstein germ or a closed-manifold counterexample. Arbitrary smooth
asymptotically hyperbolic boundary data do not rescue the orthogonally
transitive class. Neither orientation of the selfdual toric Einstein ansatz
can supply the connector. A separate static-continuation argument excludes
every constant-frame diagonal fibre ansatz, even with nonzero charge.
A genuinely rotating-shape, charged, non-half-flat filling remains an open
case in this work.

## 1. Geometric setting

Let the interior of \(\bar M=[0,1]\times T^3\) carry a complete Einstein metric
\(\operatorname{Ric}_g=-3g\), smoothly conformally compact at both boundary
components. Assume a free isometric, marked \(T^2\) action extends freely to
the compactification, with quotient an annulus \(B\). The actual torus
lattice is fixed. The principal bundle over the annulus is trivial, but its
connection can have holonomy. Write

\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad
G=\rho M,\quad \det M=1,\quad \sigma=\log\rho.
\tag{1.1}
\]

The shape map \(U:B\to\mathbb H^2\) has target metric of curvature \(-1\),
normalized by

\[
S=U^*h,\qquad e=\operatorname{tr}_\gamma S
=\tfrac12\operatorname{tr}(M^{-1}dM\,M^{-1}dM).
\tag{1.2}
\]

Set \(dA=f\,d\mu_\gamma\), \(q=\rho^2Mf\), and
\(Q=\frac12\rho^{-3}q^{\mathsf T}M^{-1}q\).
The Einstein mixed equation makes \(q\) constant. In particular
\(q=0\), \(Q=0\), and orthogonal transitivity \(dA=0\) are equivalent.
Flat connection holonomy need not vanish in this case.

An invariant smooth defining function \(x\) can be chosen at each end.
There \(\gamma=x^{-2}\bar\gamma\), \(\rho=x^{-2}\bar\rho\), where
\(\bar\gamma\) and \(\bar\rho>0\) are smooth and nondegenerate up to the
boundary. The shape matrix \(M\) extends smoothly. Consequently

\[
e=O(x^2)\longrightarrow0.
\tag{1.3}
\]

No flatness, constancy of the boundary shape, or nonnegative Yamabe
assumption is made.

## 2. The orthogonally transitive no-connector theorem

**Theorem 2.1.** There is no metric satisfying Section 1 with \(q=0\).

**Proof, first step: a global shape-energy ceiling.** The exact reduced
equations in the charge-free case are

\[
\tau_\sigma U=0,\qquad
\operatorname{Ric}_\gamma-\nabla^2\sigma
=-3\gamma+\tfrac12d\sigma\otimes d\sigma+\tfrac12S,
\tag{2.1}
\]

where \(L=\Delta_\gamma+\nabla\sigma\cdot\nabla\) and
\(\tau_\sigma U=\tau U+dU(\nabla\sigma)\). Weighted Bochner gives

\[
\frac12Le
=|\nabla dU|^2-3e
 +\tfrac12|dU(\nabla\sigma)|^2
 +e^2-\tfrac12|S|^2
\ge -3e+\tfrac12e^2.
\tag{2.2}
\]

Here the target-curvature term is \(e^2-|S|^2\), while the \(S/2\) term
in (2.1) adds \(|S|^2/2\). Since \(S\ge0\), \(|S|^2\le e^2\).
By (1.3), if \(e\) is not identically zero its positive global maximum is
attained in the interior. The maximum principle therefore yields

\[
\sup_B e\le6.
\tag{2.3}
\]

This step is why smooth AH ends suffice: compact support of \(dU\), used
for exact flat ends in the earlier analysis, is unnecessary.

**Second step: an invariant minimal separator.** Equip the annulus with
the auxiliary metric \(\widehat\gamma=\rho^2\gamma\). Near each boundary
it is uniformly comparable to \(x^{-6}(dx^2+d\theta^2)\). Essential loops
escaping into either end have length tending to infinity; a bounded-length
essential loop cannot make an unbounded excursion into an end because the
radial distance also diverges. A minimizing sequence in the primitive
essential free homotopy class thus stays in a compact annulus. The direct
curve-shortening/minimization argument gives a smooth embedded closed
\(\widehat\gamma\)-geodesic \(c\).

The lift \(\Sigma=\pi^{-1}(c)\cong T^3\) has area equal to the fixed fibre
period area times \(\int_c\rho\,ds_\gamma\). It is therefore minimal.
Equivalently its mean curvature is invariant along each fibre and its
vanishing follows already from invariant normal variations. This argument
does not require a globally trivial flat connection.

**Third step: a contradictory shape-energy floor.** Parametrize \(c\) by
\(\gamma\)-arclength \(s\). Locally gauge away the pulled-back connection;
the intrinsic metric of \(\Sigma\) is \(ds^2+G(s)_{ab}d\xi^a d\xi^b\).
Its scalar curvature is

\[
R_\Sigma=-2\sigma''-\tfrac32(\sigma')^2-\tfrac12e_{\rm tan},
\qquad e_{\rm tan}=|dU(\dot c)|^2.
\tag{2.4}
\]

For completeness, the fibre second fundamental form in this three-metric
is \(K=\frac12G^{-1}G'\), so
\(\operatorname{tr}K=\sigma'\) and
\(|K|^2=\frac12(\sigma')^2+\frac12e_{\rm tan}\); the flat-fibre scalar
formula gives (2.4). The minimal-hypersurface Gauss equation, in contrast,
is

\[
R_\Sigma=-6-|\mathrm{II}_\Sigma|^2.
\tag{2.5}
\]

At a maximum of the periodic function \(\sigma|_c\), equations (2.4)--(2.5)
give

\[
e_{\rm tan}=12+2|\mathrm{II}_\Sigma|^2-4\sigma''\ge12.
\tag{2.6}
\]

This contradicts (2.3). The theorem follows. \(\square\)

The conclusion excludes an entire geometric class. It is not a claim
that a charged connector cannot exist, or that the underlying closed
graph-manifold construction has been completed.

## 3. Exclusion of half-conformally-flat candidates

**Corollary 3.1.** A metric satisfying Section 1 cannot have either
\(W^+=0\) or \(W^-=0\).

**Proof.** Calderbank--Pedersen, Proposition 3.2, proves that on a
selfdual Einstein four-manifold of nonzero scalar curvature, the orthogonal
distribution to two independent commuting Killing fields is integrable.
Their assertion is local and needs no compactness hypothesis. Applying it
to the free torus action gives \(dA=0\), contradicting Theorem 2.1.
Reverse orientation for the other Weyl half. \(\square\)

Thus the explicit selfdual toric Einstein families do not supply the
missing global continuation of the charged local neck. The prior local
charged construction is not contradicted: it necessarily lies outside
this integrable half-flat class. This is an application of an established
classification ingredient, not a new classification theorem.

Primary reference: D. Calderbank and H. Pedersen, *Selfdual Einstein metrics
with torus symmetry*, Proposition 3.2, printed p. 4 in the preprint:
[arXiv:math/0105263](https://arxiv.org/pdf/math/0105263).

## 4. A second exclusion: a hypersurface-orthogonal circle

This exclusion does not require orthogonal transitivity of the entire
\(T^2\) action. In particular it can rule out some charged ansatz classes.

**Theorem 4.1.** A metric satisfying Section 1 cannot admit a free
hypersurface-orthogonal circle subgroup of its marked torus action.

**Proof.** Quotient by that circle. Its base \(N\) is the interior of
\([0,1]\times T^2\). The circle bundle is trivial: it is induced from the
trivial marked torus bundle over the annulus. Write

\[
g=V^2(d\phi+\alpha)^2+h,\qquad V>0.
\tag{4.1}
\]

Hypersurface orthogonality is \(d\alpha=0\). Dropping this flat connection
produces the globally defined metric \(g_0=V^2d\phi^2+h\), locally isometric
to \(g\) and thus still Einstein. This operation changes any flat holonomy;
it is used to produce a contradiction, not asserted to be a global isometry.
At both infinities \(xV\) extends smoothly and positively, and \(x^2h\)
extends to a smooth metric on \(\bar N\). The Einstein equations are

\[
\operatorname{Ric}_h-V^{-1}\nabla_h^2V=-3h,
\qquad \Delta_hV=3V.
\tag{4.2}
\]

They also imply that the Lorentzian metric
\(g_L=-V^2dt^2+h\) on \(\mathbb R\times N\) is Einstein with constant
\(-3\). This is a real static continuation; no complex continuation of
a non-flat connection is used.

The optical metric \(k=V^{-2}h\) extends smoothly and nondegenerately to
the compact connected manifold with boundary \(\bar N\). Hence the
conformal spacetime \(-dt^2+k\) on \(\mathbb R\times\bar N\) is globally
hyperbolic with timelike boundary: time slices are Cauchy, and causal
diamonds are closed subsets of a compact time interval times \(\bar N\).
Each boundary component has a compact spacelike cut \(T^2\). The physical
Einstein metric obeys the averaged null energy condition, since its null
Ricci contractions vanish identically.

Galloway--Schleich--Witt--Woolgar's boundary noncommunication theorem now
forbids a causal curve between the two conformal boundary components.
But a finite-length path for \(k\) joins these components, and traversing
it sufficiently slowly while increasing \(t\) gives a timelike curve
between them. Contradiction. \(\square\)

The relevant primary theorem is Theorem 2 in Section II of the preprint
*The AdS/CFT Correspondence Conjecture and Topological Censorship*:
[arXiv:hep-th/9912119](https://arxiv.org/pdf/hep-th/9912119).
Its compact-spacelike-cut alternative is used, not an unverified null
genericity assumption. There is no boundary scalar-curvature sign condition.

For example, in a constant torus basis the charged block ansatz

\[
g=\gamma+V_1^2(d\xi^1+A^1)^2+V_2^2(d\xi^2)^2
\tag{4.3}
\]

cannot reach two smooth AH ends, even when \(dA^1\ne0\). It retains a
static second circle. The general rotating-shape, charged metric (1.1)
has no such circle forced by its hypotheses, so Theorem 4.1 does not settle
the remaining general problem.

**Corollary 4.2.** The fibre matrices \(G(p)\), \(p\in B\), of a putative
connector cannot all be diagonal in one fixed real torus basis.

**Proof.** In such a basis, all derivative contributions to the off-diagonal
vertical Ricci component vanish. The remaining connection-curvature term is

\[
\operatorname{Ric}_{12}=\tfrac12G_{11}G_{22}f^1f^2.
\tag{4.4}
\]

Since \(g_{12}=0\), the Einstein equation gives \(f^1f^2=0\).
The charge is constant and \(G\) is diagonal, so at least one component
of \(q\), say \(q_2\), vanishes everywhere. Hence \(dA^2=0\), and the
second torus generator is hypersurface-orthogonal. If the fixed real basis
is integral, Theorem 4.1 applies directly. For an arbitrary fixed real
basis, replace the torus lattice by the lattice generated by that basis.
All coefficients remain well-defined on the same annular base and the new
compact torus fibres; the metric is locally unchanged and still has two
smooth AH ends. The second generator is now a genuine circle, again
contradicting Theorem 4.1. \(\square\)

This is not a choice-of-coordinates condition at one point. Every positive
matrix can be diagonalized individually; the excluded restriction is a
single basis valid throughout the base. Spatial variation of the fibre
eigendirections is therefore indispensable to any possible connector.

### 4.1. A boundary-data obstruction from the exact shear current

**Theorem 4.3.** Align a fixed real torus frame with the nonzero charge,
so \(q=(q_0,0)\), and define the charge-adapted shear
\(a=M_{12}/M_{22}=G_{12}/G_{22}\). If its two conformal boundary values
are the same constant, a metric as in Section 1 does not exist.

**Proof.** Write the shape matrix globally as

\[
M=\begin{pmatrix}
e^{-u}+e^u a^2&e^ua\\ e^ua&e^u
\end{pmatrix},\qquad
h_{\mathbb H^2}=du^2+e^{2u}da^2.
\tag{4.5}
\]

The exact reduced shape equation and charge potential are

\[
\tau_\sigma U+\nabla_UQ=0,\qquad
Q=\tfrac12q_0^2\rho^{-3}e^u.
\tag{4.6}
\]

In particular the shear component has no potential forcing. With the
target Christoffel coefficient \(\Gamma^a_{ua}=1\), it is exactly

\[
\Delta_\gamma a+
\langle\nabla\sigma+2\nabla u,\nabla a\rangle=0,
\qquad
\operatorname{div}_\gamma(\rho e^{2u}\nabla a)=0.
\tag{4.7}
\]

Both \(u\) and \(a\) are smooth on the compactified annulus. If
\(a|_{\partial_-B}=a|_{\partial_+B}=a_0\), a nonconstant \(a\) would
have either a maximum larger than \(a_0\) or a minimum smaller than
\(a_0\) at an interior point. The strong maximum principle applied to
(4.7) excludes either possibility. Uniform ellipticity at the compactified
boundary is not being assumed: the extremum is interior, where all
coefficients are smooth and the operator is elliptic. Thus \(a=a_0\)
throughout \(B\).

The constant covectors \(d\xi^1\) and \(d\xi^2+a_0d\xi^1\) then
diagonalize every fibre metric, since its quadratic form is
\(\rho[e^{-u}(d\xi^1)^2+e^u(d\xi^2+a_0d\xi^1)^2]\).
Corollary 4.2 gives the contradiction. \(\square\)

This is a restriction on actual boundary data for the specified charge
direction, not only an interior ansatz exclusion. The boundary shapes may
vary through arbitrary nonconstant functions \(u_\pm(\theta)\), so their
conformal classes can both have negative Yamabe sign; that variation does
not evade the theorem. In invariant target language, both shape loops
cannot lie in the same vertical geodesic whose ideal endpoint is selected
by the charge potential. In particular a possible filling requires a
nonzero range of charge-adapted shear across the union of its boundaries.
Different constants at the two ends are not excluded by this argument.

## 5. Boundary translations and the correct deformation quotient

This section describes a degeneracy of a *marked* boundary problem, not
an instability or a family of non-isometric geometries.

Suppose a metric as in Section 1 exists. Let \(X_1,X_2\) generate its
torus action, and choose an invariant smooth cutoff \(\chi\) equal to zero
near the first infinity and one near the second. For a small constant
\(v\in\mathbb R^2\), let \(\Phi_v\) be the diffeomorphism obtained by fibre
translation through \(\chi v\). Then

\[
g_v=\Phi_v^*g
\tag{5.1}
\]

is Einstein and is exactly equal to \(g\) near both ends. All these metrics
have the same conformal boundary and all the same asymptotic coefficients.
They are isometric as unmarked metrics. Nevertheless they give two local
relative-phase directions when quotienting only by diffeomorphisms which
are pointwise the identity on *both* conformal boundaries.

To see the last assertion, a boundary-identity equivalence between two
such pullbacks would produce an isometry of \(g\) equal to the identity on
one conformal boundary and to a nontrivial small torus translation on the
other. An isometry fixing one conformal boundary pointwise is the identity:
it preserves the geodesic defining function attached to a fixed boundary
representative and its inward normal lines, hence fixes a collar and then
the connected interior. This is a contradiction.

The infinitesimal tensors \(h_v^0=\mathcal L_{\chi X_v}g\) are compactly
supported. In the usual AH Bianchi slice, solve the coercive vector equation

\[
(\nabla^*\nabla+3)Y_v^\flat=\beta h_v^0,\qquad
\beta h=\delta h+\tfrac12d\operatorname{tr}h,
\tag{5.2}
\]

with the \(L^2\) solution. Then
\(h_v=h_v^0-\mathcal L_{Y_v}g\) is an \(L^2\) gauged Jacobi field.
The Einstein trace equation and coercivity make it trace-free, hence
divergence-free. The nontrivial relative boundary values prevent these
two phase directions from being removed by a boundary-identity gauge.
They disappear if the quotient also allows the corresponding independent
boundary translations. In particular they cannot justify a claim of
geometric instability or of additional physical Einstein moduli.

There is also a useful solvability distinction. Put
\(W_v=\chi X_v-Y_v\), so \(h_v=\mathcal L_{W_v}g\) and
\(\operatorname{div}W_v=0\). For any compactly supported symmetric source
\(F\) satisfying the linearized conservation condition \(\beta F=0\),

\[
\int_M\langle F,h_v\rangle\,dV
=-2\int_M\langle\operatorname{div}F,W_v\rangle\,dV
=-\int_M\langle d\operatorname{tr}F,W_v\rangle\,dV=0.
\tag{5.3}
\]

Thus these marking modes do not themselves add a new force-balancing
obstruction for a compactly supported conserved gluing source. A claimed
inverse must still fix or quotient their phases; a source meeting infinity
requires retention of the boundary flux rather than use of (5.3) without
a boundary term.

Anderson's general isometry-extension theorem does not supply independent
bulk extensions of arbitrary isometries prescribed separately on these two
ends. Theorem 5.4 assumes \(\pi_1(\bar M,\partial\bar M)=0\), which fails
for a cylinder with two boundary components. Surjectivity from each
individual boundary component on fundamental groups is a different
condition. See M. Anderson, *Extension of symmetries on Einstein manifolds
with boundary*, Theorem 5.4 and the discussion of disconnected boundary:
[author's text](https://www.math.stonybrook.edu/~anderson/isomext2.pdf).

## 6. What is now reduced, and what remains

Together with the boundary charge identity in `round8_boundary.md`, a
putative connector must carry nonzero charge, a nonzero real relative
holonomy difference, two nonconstant boundary shape loops, both Weyl
halves, and no hypersurface-orthogonal torus circle. Its fibre matrices
cannot be diagonalized in one constant real frame. It also satisfies the strict spectral restriction in
`round7_spectral.md`. None of these necessary conditions is yet an
existence theorem or a contradiction for the fully charged system.

The no-go arguments remove three complete ansatz classes from the global
search. The relative-phase analysis specifies the correct elliptic
quotient and shows why those gauge directions alone cannot close the
remaining problem. No closed-manifold Yau26 branch is settled here.

## 7. Reproduction

`round8_global_check.py` checks (2.4) directly from coordinate Christoffel
symbols for a general positive symmetric two-by-two fibre matrix, verifies
the target metric normalization and the algebra in the Bochner ceiling,
checks the maximum-point floor, and reproduces the vertical twist
coefficient in (4.4) from a four-dimensional coordinate metric. It tests local identities, not the
global variational or classification arguments above.
