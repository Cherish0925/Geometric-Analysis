# Round 16: product propagation, cusp-core exclusion, and exterior response

22 September 2026.

This round continues the three scientific lines from [Round 15](round15.md)
on the fixed closed shear manifolds constructed in Rounds 11–14. The
central question remains whether these manifolds carry any Einstein
metric, not whether a particular symmetric ansatz has an exact solution.

The strongest new connection is between local analysis and global
topology: a hypothetical exact sequence approaching the sharp volume
must resemble the hyperbolic product on an expanding region, while an
irreducible Hilbert modular core cannot embed in the underlying shear
manifold. Reducible product limits remain possible. The construction
calculation identifies the end response that their matching problem
must supply.

## 1. Rigidity: quantitative product geometry beyond the thick part

Assume the actual monopole hypotheses in both orientations from
Round 15, with
\[
 A=2\chi(M)>0,\qquad \tau(M)=0,\qquad
 \operatorname{Ric}_g=-3g.
\]
Define the absolute excess and local volume
\[
 D=9\operatorname{Vol}_g(M)-2\pi^2 A,\qquad
 v(p)=\operatorname{Vol}_g B_1(p).
\]
Let \(f=\operatorname{dist}_{\rm HS}(\mathcal R,\mathscr P_3)\),
where \(\mathscr P_3\) is the curvature-operator orbit of
\(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\).

Round 15 supplied \(\int f^2\le(68/3)D\) and uniform curvature
derivative bounds when \(D\) is sufficiently small. The new estimate is
\[
 \boxed{\frac{D}{v(p)}\le\varepsilon_0
 \quad\Longrightarrow\quad
 \sup_{B_{1/4}(p)}\bigl(f+|\nabla\operatorname{Rm}|\bigr)
 \le C\sqrt{\frac{D}{v(p)}}.}
 \tag{1}
\]
There is no assumed volume lower bound. The denominator measures
precisely which collapsing regions the estimate still controls.

The proof uses the polynomial
\[
 N(W)=W^2+W-2I
\]
for either Weyl block. Its zero set is the product Weyl orbit with
eigenvalues \((-2,1,1)\). Its differential alone misses the tangent
directions of that orbit. The full divergence equation
\(\delta W=0\), applied to all eight tangent first-jet variables,
controls those missing directions. This gives
\[
 |\nabla W|^2\le\frac{132}{9}|\nabla N(W)|^2
\]
in a fixed neighborhood of the orbit. The exact Einstein equation
then yields a scalar differential inequality for \(|N(W)|^2\).
Integration by parts and the volume-normalized mean-value inequality
give (1). A preliminary Lipschitz/volume-comparison argument enters
the neighborhood without assuming (1).

At a thick basepoint \(x\), Bishop–Gromov gives
\(v(p)\ge c_Me^{-3d(x,p)}\). Thus for every \(0<\theta<1/3\),
\[
 \boxed{
 \sup_{B_{\theta\log(1/D)}(x)}
       \bigl(f+|\nabla\operatorname{Rm}|\bigr)
 \le C_M D^{(1-3\theta)/2}\longrightarrow0.}
 \tag{2}
\]
A point with fixed positive deviation must have \(v(p)=O(D)\)
and lie at least \(\frac13\log(1/D)-O(1)\) from \(x\). This is
conditional on the presence of that deviation; it is not an
unconditional logarithmic diameter lower bound.

The analytic argument also applies to a complete Einstein metric with
a prescribed curvature bound and finite \(\int f^2\), using that
integral in place of \(D\). The monopoles supply the energy and curvature
bounds for the present application, not the local analytic mechanism.

Proof: [product-profile propagation](round16_rigidity.md).

## 2. Global topology excludes the irreducible limit alternative

Write the shear manifold as a graph of blocks \(B_v\times F_v\),
where \(B_v\) has nonempty boundary and negative Euler characteristic,
and \(F_v\) is a closed hyperbolic surface. Its group \(G\) acts on
the Bass–Serre tree. Two distinct incident edge stabilizers intersect
in a conjugate of a surface group, hence contain no \(\mathbb Z^2\).

This gives a useful exact statement:
\[
 q:\mathbb Z^2\rtimes_A\mathbb Z\longrightarrow G,\quad
 A\in\mathrm{SL}(2,\mathbb Z),\ |\operatorname{tr}A|>2
 \quad\Longrightarrow\quad q(\mathbb Z^2)=1.
 \tag{3}
\]
The proof considers the action of the normal \(\mathbb Z^2\), not an
unsupported fixed-point assertion for all solvable groups. The
translation character and the cyclic normalizers in the vertex factors
exclude its possible nontrivial images.

For a nonuniform irreducible lattice
\(\Lambda<\mathrm{PSL}(2,\mathbb R)^2\), a cusp contains such a Sol
group. Equation (3), followed by the classical normal subgroup theorem,
makes every homomorphism \(\Lambda\to G\) trivial. Asphericity of the
target then makes every map from a compact cusp core nullhomotopic.

There is nevertheless a nonzero compactly supported intersection
pairing on that core. On the corresponding finite-volume quotient \(N\),
the Kähler form has a bounded primitive on every cusp:
\[
 \omega=\sum_{i=1}^2\frac{dx_i\wedge dy_i}{3y_i^2},
 \qquad
 \eta=\sum_{i=1}^2\frac{dx_i}{3y_i},\qquad d\eta=\omega.
\]
Cutting off this primitive produces a closed compactly supported
two-form \(\zeta\) with
\[
 \int_N\zeta^2=2\operatorname{Vol}(N)>0.
 \tag{4}
\]
If the core embedded in \(M\), extend \(\zeta\) by zero to \(M\).
Nullhomotopy would make its restriction exact on the core, contradicting
(4). Therefore
\[
 \boxed{\text{An irreducible noncompact product cusp core cannot
 embed as a codimension-zero submanifold of }M.}
 \tag{5}
\]
The quotient in (5) preserves the orientation of each factor, as the
Round-15 limiting forms ensure in the application. No injection of
the limit fundamental group into \(G\) is assumed.

For the specified non-Kähler shear types, any smooth finite-volume
pointed limit of an exact sequence with
\(\operatorname{Vol}\to V_*=4\pi^2\chi/9\) is noncompact and must have
a reducible lattice: a finite cover is a product of finite-area
hyperbolic surfaces, at least one noncompact.

This is a genuine elimination, but not the elimination of all limits.
The existing approximate closed family already converges to
\(B_0\times F\), where \(B_0\) is a cusped finite-area surface; for a
single block this limit retains the entire volume \(V_*\).
The remaining problem is the exact matching through reducible ends.

Proof: [Sol groups and compact-core intersection pairing](round16_global.md).

## 3. Construction: where an exact repair must get its compensation

On an optimized shear collar use
\[
 G_c=dt^2+a^2\theta^2+h_F,\qquad
 a=c\cosh(\sqrt3\,t),\qquad
 \theta=d\phi+z(t)\beta ,
\]
with the actual smoothly truncated Maxwell profile and fixed integer
shear. The previous waist test had an interior adjoint error of
order \(c^2\) in \(L^1\). It varied the radius without re-solving the
connection equation.

Set \(f=\operatorname{sech}^2(\sqrt3\,t)\) and
\[
 r_c=\int fz'\,dt,\qquad
 \zeta'=2(f-r_c)z',\qquad \zeta(-\infty)=\zeta(+\infty)=0.
\]
The corrected test tensor is
\[
 \widetilde H_c
 =\chi f(dt^2-a^2\theta^2)
       +a^2\zeta(\theta\otimes\beta+\beta\otimes\theta).
 \tag{6}
\]
It respects the linearized Maxwell equation in the core. The complete
gauged calculation, including the nonzero divergence and a surviving
cubic mixed term, gives interior \(L^1\) error \(O(c^3)\). The remaining
\(O(c^2)\) error is confined to two fixed-width end bands. The signed
source is unchanged:
\[
 \int\langle \operatorname{Ric}_{G_c}+3G_c,\widetilde H_c\rangle
 =-3\sqrt3\,\|\beta\|_2^2c^3+O(c^6).
 \tag{7}
\]

For an arbitrary tensor \(h\), let
\(\eta(h)=\sum_{j=0}^2\|\nabla^j h\|_\infty\), and let \(b(h)\)
be its corresponding \(C^1\) norm on those end bands. Closed-manifold
integration by parts, with the Bianchi term retained, gives
\[
 \left|\int\langle DE[h],\widetilde H_c\rangle\right|
 \le C\bigl(c^3\eta(h)+c^2b(h)\bigr).
 \tag{8}
\]
Thus every uniformly small full linearized repair must have
\[
 \boxed{b(h)\ge b_0c.}
 \tag{9}
\]
No imposed symmetry or gauge is used. This is an actual geometric end
response requirement, not a scalar boundary condition chosen for a
model filling.

For a normalized nonlinear repair of size \(O(c)\) with \(o(c)\)
end response, its Taylor remainder \(Q_c(h)\) must instead satisfy
\[
 \boxed{\lim_{c\to0}c^{-3}
       \int\langle Q_c(h),\widetilde H_c\rangle
       =3\sqrt3\,\|\beta\|_2^2.}
 \tag{10}
\]
The calculation does not prove that this quadratic charge is impossible.
It does not enlarge the existing small-\(c\) repair-exclusion radius.
It identifies the contribution that a successful full correction must
actually produce.

The same note computes genuine closed hyperbolic length variations:
with the local connection profile held fixed,
\[
 \partial_{\log c_e}\mathscr S
 =-\frac{3\pi q_e}{\sqrt{V_*}}\|\beta_e\|_2^2<0.
 \tag{11}
\]
The exterior product blocks are included. Fiber-stress balance therefore
does not make the waist parameters stationary.

Proof: [Maxwell-compatible receiver and exterior response](round16_construction.md).

## 4. A cross-line construction: balanced isotropic integer data

The rank-two balance criterion from Round 15 requires a nonzero cup
product. That criterion cannot be extended to three forms.

Take the classical separating Schwarz P minimal surface
\(U:F_3\hookrightarrow\mathbb T^3\) and its three coordinate
differentials \(\beta_j\). In its uniformized hyperbolic conformal
class they are harmonic, have integral periods, are linearly independent,
and satisfy
\[
 \int_{F_3}\beta_i\wedge\beta_j=0,\qquad
 \sum_{j=1}^3
   \left(\beta_j\otimes\beta_j-\tfrac12|\beta_j|^2h\right)=0.
 \tag{12}
\]
Separation proves the first identity; conformal minimality proves the
second. Their span is Lagrangian in \(H^1(F_3;\mathbb R)\).
Three equal-capacity self-gluings of \(B_{r,6}\times F_3\) realize
these data in the fixed closed construction, with
\(\chi=8r+16\) and pointwise Ricci defect \(O(c^2)\).

Moreover balance is not necessarily a minimum of the fiber potential.
For any unbranched orientable minimal immersion of genus \(p\ge2\)
into a flat three-torus, the parallel normal variation and harmonic
energy minimization give
\[
 \left.\frac{d^2}{dt^2}\sum_j\|\beta_j(h_t)\|_2^2\right|_{t=0}
 \le -16\pi(p-1)<0.
 \tag{13}
\]
This differs from the nonnegative rank-two balanced Hessian.
The minimal surface and its classical variational formulas are inherited
mathematics; their role here is to provide admissible shear matching data
and distinguish two different equilibria. Neither equilibrium solves
the waist or nonsymmetric exterior equations.

Proof: [minimal surfaces and isotropic integral balance](round16_minimal_balance.md).

## 5. What the three lines now say together

The implications are more specific than “a counterexample must degenerate”:

- A near-sharp exact output has controlled product curvature throughout
  an expanding region, including balls whose volume decays more slowly
  than \(D\).
- The limiting product geometry cannot be irreducible Hilbert modular.
- Reducible limits are consistent with the topology and the actual
  approximate constructions. They cannot be discarded.
- Within the explicit shear family, fiber forces can cancel even for
  pairwise isotropic integer data, but a waist force remains.
- Every uniformly small linearized repair needs order-\(c\) end data;
  a normalized nonlinear \(O(c)\) repair with \(o(c)\) end response
  must supply the specified positive quadratic charge.

These are linked restrictions and constructions, not a proof that every
possible Einstein metric lies near the chosen family. In particular,
the analysis neither proves a positive Einstein-volume gap above \(V_*\)
nor excludes exact metrics of larger volume.

Two concrete mathematical problems emerge. The first is to identify
the actual reducible end geometry and control the region where
\(\operatorname{Vol}B_1=O(D)\). The second is to solve, or obstruct,
the real exterior response and the full quadratic compatibility
condition. A negative answer in a symmetric sector would not settle
the unrestricted problem. An exact nonsymmetric solution would be
equally decisive for the chosen smooth object.

For Yau26, these are steps toward the same-smooth-manifold
Einstein decision. No complete sign branch, full counterexample, or
dimension-uniform existence theorem is established in this round.
Literature priority for the new deductions has not been settled.

## Reading and reproduction

The four linked notes contain the arguments and their classical inputs.
[Verification](round16_verification.md) records the four programs
actually rerun, numerical versus exact scope, and cross-review.
The inherited papers and checks remain unchanged.
