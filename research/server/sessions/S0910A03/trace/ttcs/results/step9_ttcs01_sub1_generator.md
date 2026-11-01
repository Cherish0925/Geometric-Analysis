# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md"
  ]
}
```

## Task

Generate a concrete mechanism for using harmonic self-dual 2-forms to force covering noncollapse in 4D near-negative-Einstein collapse.

SETUP: On a fixed critical Ishida-LeBrun 4-manifold with δ_i = ||Ric_i + g_i||_∞ → 0:
- There exist near-harmonic self-dual forms H with nearly constant amplitude |H| ≈ const
- The Weitzenböck identity gives ∫|∇H|² = (1 + O(δ))∫|H|² (for the simple eigenform)
- On a collapsed region, the Bochner identity for nearly constant amplitude gives |∇H|² ≈ |H|² pointwise
- The eigenline direction rotates at O(1) rate in base directions (not fiber directions)

QUESTION: Can these properties of the forms (controlled amplitude, controlled gradient energy, eigenline rotation) force the local universal cover to be noncollapsed? Or can a collapsed cover accommodate all these properties?

Consider:
1. Whether the forms define a topological obstruction to collapse (e.g., through Euler class of the eigenline bundle)
2. Whether the O(1) horizontal rotation rate constrains the topology or geometry of the collapse base
3. Whether nearly constant amplitude + approximate harmonicity + controlled gradient produces a Bochner-type constraint on the covering fundamental group
4. Whether the three independent near-harmonic forms (when b₂⁺ ≥ 3) can constrain the collapse rank
5. Explicit collapsed models (torus bundles over surfaces, nilmanifolds) and whether they can support forms with these properties

Produce specific mathematical mechanisms, not general strategy.

## Output

A useful way to use the self-dual form is not just as a tensor with \(L^2\) control, but as an adiabatic variable in the collapsed directions.  On a regular collapsed chart, after passing to the torus/nilpotent cover supplied by the collapse structure, a fiber-invariant self-dual form has very rigid first-order equations.  These equations separate the possible collapse ranks.

## 1. Circle collapse: one form can survive

Assume a regular rank-one collapse
\[
U^4 \simeq S^1 \longrightarrow U \xrightarrow{\pi} B^3,
\qquad 
g=\pi^*\gamma+\theta^2,
\]
where \(\theta\) is the unit vertical coform.  Write
\[
d\theta=\kappa\wedge \theta+\tau,
\]
with \(\kappa\in\Omega^1(B)\), \(\tau\in\Omega^2(B)\).  Every invariant self-dual 2-form has the form
\[
H=\alpha\wedge\theta+*_{3}\alpha,
\qquad \alpha\in\Omega^1(B).
\]
Then
\[
|H|^2=2|\alpha|^2,
\]
and the harmonicity equation \(dH=0\) becomes
\[
d_B\alpha=\kappa\wedge\alpha,
\qquad
d_B(*_3\alpha)=\alpha\wedge\tau.
\]
If \(\theta=\ell\eta\), then \(\kappa=d\log\ell\), so the first equation is
\[
d(\ell^{-1}\alpha)=0.
\]
Thus a self-dual harmonic form on a circle-collapsed region is essentially a weighted harmonic one-form on the 3-dimensional base.

The Bochner identity on the base gives the relevant compatibility:
\[
\frac12\Delta_\gamma |\alpha|^2
=
|D\alpha|^2+\operatorname{Ric}_\gamma(\alpha,\alpha)
+\text{terms from }\kappa,\tau .
\]
If \(|\alpha|\) is nearly constant, then
\[
|D\alpha|^2
\approx
-\operatorname{Ric}_\gamma(\alpha,\alpha)
+\text{connection terms}.
\]
So the observed four-dimensional identity
\[
\fint |\nabla H|^2 \approx \fint |H|^2
\]
can be accommodated by a 3-dimensional base whose Ricci curvature in the \(\alpha\)-direction is roughly \(-|\alpha|^2\).  A single form therefore does not by itself force a circle-collapsed cover to open up.  It reduces the problem to a very concrete 3-dimensional object: a constant-length weighted harmonic one-form with prescribed Bochner energy.

The distinguishing calculation is
\[
\alpha=i_{e_\theta}H,\qquad
d(\ell^{-1}\alpha),\qquad
d*_3\alpha-\alpha\wedge\tau,\qquad
|D\alpha|^2+\operatorname{Ric}_\gamma(\alpha,\alpha).
\]
If these quantities match the equations above, rank-one collapse is compatible with the form package.

## 2. Rank-two torus collapse: constant amplitude kills rotation

Now suppose
\[
U^4\simeq T^2\longrightarrow U\xrightarrow{\pi}\Sigma^2.
\]
In an adapted oriented orthonormal coframe \(e^1,e^2,\theta^1,\theta^2\), write
\[
H
=
a(e^1\wedge e^2+\theta^1\wedge\theta^2)
+
b(e^1\wedge\theta^1-e^2\wedge\theta^2)
+
c(e^1\wedge\theta^2+e^2\wedge\theta^1).
\]
Equivalently, set \(\phi=b+ic\).  In the flat product model \(\Sigma\times T^2_\ell\),
\[
dH=0
\quad\Longleftrightarrow\quad
da=0,\qquad \bar\partial \phi=0.
\]
Thus the mixed part is a holomorphic function on the surface base.  If \(|H|\) is constant, then
\[
a^2+|\phi|^2=\text{constant}.
\]
Since \(a\) is constant, \(|\phi|\) is constant.  A holomorphic function of constant modulus is constant, so \(b,c\) are constant and
\[
\nabla H=0.
\]
This is incompatible with the Weitzenböck energy
\[
\fint |\nabla H|^2\approx \fint |H|^2.
\]

For a genuine torus bundle, the same mechanism becomes a covariant Cauchy–Riemann equation.  The mixed coefficient \(\phi\) is a section of the complex line
\[
L=\operatorname{Hom}_{\mathbb C}(T\Sigma,V),
\]
where \(V\) is the oriented vertical 2-plane bundle.  Harmonicity gives schematically
\[
\bar\partial_A\phi=a\,\mathcal T+o(1),
\]
where \(A\) is the metric connection induced by the base and vertical rotations, and \(\mathcal T\) is built from O’Neill tensors.  If the vertical-horizontal twisting is small and \(a\) is controlled, then
\[
\bar\partial_A\phi=o(1),\qquad |\phi|\approx\text{constant}.
\]
For a unit section of a Hermitian line,
\[
\bar\partial_A\phi=0,\qquad |\phi|=\text{constant}
\]
implies
\[
\nabla_A\phi=0,
\qquad
F_A=0.
\]
Hence the horizontal rotation energy must vanish.

So rank-two collapse can carry the form package only if one sees a definite source in the covariant Cauchy–Riemann equation: large O’Neill twisting, curvature of \(L\), loss of constant amplitude, or nontrivial non-invariant behavior.  In a regular torus collapse with small fiber geometry, the form equations force parallel behavior, not \(O(1)\) rotation.

## 3. Rank-three collapse: product tori give no rotation; nil twisting can fake it

For a rank-three product collapse
\[
U\simeq I\times T^3_\ell,
\]
write
\[
H=\sum_{j=1}^3 n_j(t)\,\sigma_j,
\]
where
\[
\sigma_1=dt\wedge\theta^1+\theta^2\wedge\theta^3,
\]
and cyclically.  Then
\[
dH=0
\quad\Longleftrightarrow\quad
n_1'=n_2'=n_3'=0.
\]
Thus a harmonic self-dual form of constant amplitude is parallel.  Again, no \(O(1)\) eigenline rotation is possible.

Nil fibers are different.  On
\[
I\times \mathrm{Nil}^3,
\qquad
d\theta^1=d\theta^2=0,\qquad
d\theta^3=c\,\theta^1\wedge\theta^2,
\]
one checks
\[
d\sigma_1=0,\qquad d\sigma_2=0,\qquad d\sigma_3=-c\,dt\wedge\theta^1\wedge\theta^2.
\]
Hence \(\sigma_1,\sigma_2\) are closed self-dual forms of constant length, but
\[
|\nabla \sigma_1|^2+|\nabla \sigma_2|^2\sim c^2.
\]
Choosing \(c\sim 1\) gives exactly the kind of \(O(1)\) rotation energy seen in the Weitzenböck identity.

This model is important: the tensorial properties of \(H\) alone do not rule out collapsed quotients.  Nil twisting can support constant-amplitude harmonic self-dual forms with \(O(1)\) covariant derivative.  But if \(c\sim 1\), the local universal cover with this left-invariant metric has ordinary four-dimensional volume at unit scale.  Collapse of the quotient comes from the lattice, and unwrapping the nil directions restores volume.  If one tries to keep the local universal cover itself collapsed by shrinking simply connected directions, then the structure constants scale like \(c\sim \ell^{-1}\), and \(|\operatorname{Rm}|\) becomes large at the same scale.  The maximal curvature mean would see this.

So nil models show compatibility with collapsed quotients, but they point toward covering noncollapse rather than against it.

## 4. Euler class mechanism: the line is trivial, the orthogonal plane carries topology

A nonzero self-dual form \(H\) gives a unit section
\[
\sigma=\frac{H}{|H|}
\]
of \(\Lambda^+\).  The real line \(\mathbb R\sigma\) is then already trivial.  The useful topological object is not the line itself, but the oriented rank-two bundle
\[
E=\sigma^\perp\subset \Lambda^+.
\]
Choose a local oriented frame \((\sigma_1,\sigma_2,\sigma_3)\), with \(\sigma_1=\sigma\), and write
\[
\begin{aligned}
\nabla\sigma_1&=a_2\otimes\sigma_2+a_3\otimes\sigma_3,\\
\nabla\sigma_2&=-a_2\otimes\sigma_1+a_1\otimes\sigma_3,\\
\nabla\sigma_3&=-a_3\otimes\sigma_1-a_1\otimes\sigma_2.
\end{aligned}
\]
Then
\[
|\nabla\sigma_1|^2=|a_2|^2+|a_3|^2.
\]
The Euler curvature of \(E\) is
\[
\Omega_E=da_1+a_2\wedge a_3
\]
(up to orientation convention), and
\[
e(E)=\frac{1}{2\pi}\Omega_E.
\]
Since
\[
\Lambda^+=\mathbb R\sigma\oplus E,
\]
one has
\[
p_1(\Lambda^+)=e(E)^2.
\]
Globally,
\[
\int_M p_1(\Lambda^+)=2\chi(M)+3\tau(M)=\frac{2A}{3}.
\]

This gives a sharp topological mechanism.  If collapse is purely regular and all connection forms \(a_j\) are basic over a base of dimension at most \(3\), then
\[
\Omega_E\wedge\Omega_E=0
\]
on the regular collapsed part.  Horizontal rotation energy \( |a_2|^2+|a_3|^2\sim 1 \) does not by itself create the four-form \(e(E)^2\).  The topological charge must therefore be carried by vertical connection curvature, singular/twisted regions, or genuinely four-dimensional regions.

Thus the Euler class does not automatically give a pointwise volume lower bound on every lifted ball, but it rules out an everywhere regular low-dimensional base picture in which the eigenline merely rotates horizontally.

## 5. Bochner constraint on the local fundamental group

Let \(X_1,\dots,X_r\) be short almost-Killing fields coming from a local nilpotent collapse structure.  Since \(H\) descends,
\[
\mathcal L_{X_a}H\approx 0.
\]
Using Cartan’s formula and \(dH=0\),
\[
d(i_{X_a}H)\approx 0.
\]
For two commuting vertical fields,
\[
d\bigl(H(X_a,X_b)\bigr)\approx 0.
\]
Thus vertical contractions of \(H\) become nearly constant along the base.

This is the fundamental-group mechanism: short deck directions force the components of \(H\) to descend to low-dimensional harmonic data.  Then the collapse rank dictates the PDE:

- rank \(1\): a weighted harmonic one-form on a 3-base;
- rank \(2\): a covariantly holomorphic section over a surface;
- rank \(3\): an ODE along a 1-base, with nil structure constants as forcing terms.

The Bochner identity is compatible with rank \(1\), rigid for rank \(2\), and rigid for flat rank \(3\).  Nil rank \(3\) can carry the rotation only through structure constants that also appear in curvature.

## 6. Three independent self-dual forms are far stronger

Suppose on a lifted ball there are three harmonic self-dual forms
\[
H^1,H^2,H^3
\]
whose Gram matrix
\[
G_{\alpha\beta}=\langle H^\alpha,H^\beta\rangle
\]
has eigenvalues bounded above and below, and whose entries are nearly constant.  Normalize them to an oriented orthonormal frame
\[
\omega_1,\omega_2,\omega_3
\]
of \(\Lambda^+\).  Write
\[
\nabla\omega_a=\sum_b A_{ab}\otimes \omega_b,
\qquad A_{ab}+A_{ba}=0.
\]
In dimension four, for a definite triple, the linear map
\[
A\longmapsto (d\omega_1,d\omega_2,d\omega_3)
\]
is an isomorphism.  Hence
\[
d\omega_1=d\omega_2=d\omega_3=0
\quad\Longrightarrow\quad
A=0.
\]
Quantitatively,
\[
\int |A|^2
\lesssim
\sum_{a=1}^3\int |d\omega_a|^2
+
\int |\nabla G|^2.
\]
Therefore three independent nearly harmonic self-dual forms with nearly constant Gram matrix force \(\nabla\omega_a\) small.  That is incompatible with three forms each carrying \(O(1)\) Weitzenböck rotation energy.

In collapse-rank language:

- rank \(1\): the three forms become three one-forms \(\alpha_1,\alpha_2,\alpha_3\) on the 3-base.  If their Gram matrix is controlled, they form a coframe.  Harmonicity and constant Gram force the base coframe to be parallel, so the base is locally flat.

- rank \(2\): after the self-dual decomposition above, the mixed space has only two real degrees of freedom once the scalar component is controlled.  Three independent forms cannot all live in a rank-two collapsed model with constant amplitudes.

- rank \(3\): flat torus collapse gives only constant coefficients; nil twisting gives at most the directions allowed by its structure equations and pays visible curvature.

Thus three independent forms with a well-conditioned Gram matrix would be a powerful covering-noncollapse mechanism.  If the actual Ishida–LeBrun sign forms instead show phase separation, then the Gram determinant tends to zero on most small regions, and this three-form mechanism is not the active one there.

## 7. Concrete model comparison

### Flat \(T^3\)-collapse over an interval
\[
g=dt^2+\ell^2(dx_1^2+dx_2^2+dx_3^2).
\]
Self-dual harmonic forms have constant coefficients.  They are parallel.  They cannot realize
\[
|\nabla H|^2\approx |H|^2.
\]

### Flat \(T^2\)-collapse over a surface
\[
g=g_\Sigma+\ell^2(dx^2+dy^2).
\]
The mixed coefficient is holomorphic.  Constant amplitude forces constant coefficient.  Again \(\nabla H=0\).

### Circle collapse over a 3-base
\[
g=\gamma+\ell^2 d\theta^2.
\]
Here
\[
H=\alpha\wedge(\ell d\theta)+*_3\alpha,
\]
and \(H\) is harmonic iff \(\alpha\) is harmonic on \(B^3\) in the product case.  A constant-length harmonic one-form on a curved 3-base can have \(O(1)\) gradient energy through the Bochner term.  Rank-one collapse is therefore the natural place where one form can live.

### Heisenberg nil collapse
With
\[
d\theta^3=c\,\theta^1\wedge\theta^2,
\]
the forms \(\sigma_1,\sigma_2\) above are closed self-dual, constant-length, and have
\[
|\nabla\sigma_a|^2\sim c^2.
\]
This shows that collapsed quotients can accommodate the form package.  But when \(c\sim1\), the local universal cover is not collapsed at unit scale; when the cover is also shrunk, curvature becomes large.

## Bottom line

The harmonic self-dual form mechanism strongly separates collapse types.

- One form does not rule out rank-one collapse; it becomes a constant-length weighted harmonic one-form on a 3-base, and the \(O(1)\) rotation is Bochner-compatible.

- Rank-two torus collapse is highly rigid: harmonicity becomes a covariant holomorphic equation, and constant amplitude forces parallel behavior unless twisting or curvature appears explicitly.

- Rank-three flat torus collapse cannot carry the rotation.  Nil collapse can, but then the local universal cover is naturally noncollapsed unless curvature grows at the collapsed scale.

- Three independent forms with a controlled Gram matrix would force a local hyperkähler-type frame and hence rule out collapsed covers.  The key observable is the smallest eigenvalue of \((\langle H^\alpha,H^\beta\rangle)\) on the lifted ball.

- The useful topological class is \(e(H^\perp)\), with \(p_1(\Lambda^+)=e(H^\perp)^2\).  Pure horizontal rotation over a base of dimension \(\le3\) cannot carry this four-dimensional Chern–Weil charge.