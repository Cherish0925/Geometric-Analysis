# Charged torus separators and the limits of a topology-only obstruction

21 September 2026.

The calculations below give the full separator stability operator,
including charge and both normal deformation terms, and explain why local
stability and amenable coverings alone do not exclude the target cylinder.
The subsequent proof in `round9_connector.md` **does exclude** the complete
two-ended, free-\(T^2\), smoothly AH Einstein cylinder in the marked
annular class. An auxiliary static spacetime built from circle quotient
data has null convergence and invokes boundary noncommunication. The local and spectral
results below remain valid and identify why that global step is needed.

## 1. The exact one-dimensional stability operator

Assume \(\operatorname{Ric}_g=-3g\) on the interior of
\([0,1]\times T^3\), with two smooth AH ends and the free marked torus
action of `round8_global.md`. Use

\[
g=\gamma+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\quad
G=\rho M,\quad\det M=1,\quad\sigma=\log\rho,
\quad Q=\tfrac12 f^{\mathsf T}Gf,
\quad dA=f\,d\mu_\gamma.
\tag{1.1}
\]

A shortest essential loop for \(\rho^2\gamma\) exists in the quotient
annulus: AH end growth prevents a bounded-length minimizing sequence from
escaping. Its lift is an invariant minimal \(T^3\), denoted \(\Sigma\).
Let \(s\) be quotient arclength on its base loop, \(n\) its horizontal
unit normal, and put

\[
\sigma_s=d\sigma(\partial_s),\quad \sigma_n=d\sigma(n),\qquad
e_s=|dU(\partial_s)|^2,\quad e_n=|dU(n)|^2.
\tag{1.2}
\]

**Proposition 1.1.** The lifted hypersurface is stable for all normal
variations, not only invariant ones. Its lowest Jacobi eigenvalue is the
lowest eigenvalue of the periodic scalar operator

\[
J_{\rm inv}\phi
=-\rho^{-1}(\rho\phi')'
 +\left(3-Q-\tfrac32\sigma_n^2-\tfrac12e_n\right)\phi.
\tag{1.3}
\]

After the unitary substitution \(\phi=\rho^{-1/2}\psi\), this becomes

\[
-\psi''+\mathcal V\psi,\qquad
\boxed{\quad
\mathcal V=
\frac{36-6Q-9\sigma_n^2-3e_n-\sigma_s^2-e_s}{8}.
\quad}
\tag{1.4}
\]

All functions and the period in this operator are the actual separator
data. Neither connection holonomy nor nonconstant fibre shape has been
discarded.

**Proof.** In horizontal/vertical blocks the second fundamental form has
horizontal entry \(-\sigma_n\), vertical entry
\(\frac12G^{-1}\partial_nG\), and mixed entry determined by
\(\frac12F(n,\partial_s)\). The first follows from minimality. Their
squared contributions are respectively
\(\sigma_n^2\), \(\frac12\sigma_n^2+\frac12e_n\), and \(Q\), whence

\[
|\mathrm{II}|^2=Q+\tfrac32\sigma_n^2+\tfrac12e_n.
\tag{1.5}
\]

The ordinary hypersurface second variation is
\(\int_\Sigma(|\nabla\phi|^2+(3-|\mathrm{II}|^2)\phi^2)\).
For invariant functions the volume element is a fixed fibre period area
times \(\rho\,ds\), giving (1.3). The lowest eigenfunction on the compact
connected hypersurface is positive and unique up to scale. Every torus
translation preserves the Jacobi operator and its normalized positive
eigenfunction; the latter is therefore invariant. Thus the full and
invariant lowest eigenvalues agree. The minimizing-loop construction
gives nonnegativity on invariant variations, hence on all variations.

The intrinsic fibre scalar formula and the Einstein Gauss equation give

\[
-2\sigma_{ss}-\tfrac32\sigma_s^2-\tfrac12e_s
=-6-Q-\tfrac32\sigma_n^2-\tfrac12e_n.
\tag{1.6}
\]

Conjugating (1.3) adds \(\sigma_{ss}/2+\sigma_s^2/4\) to its potential.
Substituting (1.6) gives exactly (1.4). \(\square\)

This is a full Sturm--Liouville test for proposed charged throat data.
For example stability implies
\[
\int_c(6Q+9\sigma_n^2+3e_n+\sigma_s^2+e_s)\,ds
\le36\operatorname{Length}_\gamma(c).
\tag{1.7}
\]
It does not imply \(Q=0\). The pointwise Gauss relation at a maximum of
\(\sigma|_c\) instead gives
\(e_s\ge12+2Q+3\sigma_n^2+e_n\), which is compatible with (1.7).

## 2. Strictly stable charged Einstein throat data satisfy the test

The actual analytic germ from `round6_global.md` supplies the relevant
counterexample to a *local* separator obstruction. With \(\theta\) modulo
\(\pi\), set

\[
M=\tfrac14\begin{pmatrix}
5+3\cos2\theta&3\sin2\theta\\
3\sin2\theta&5-3\cos2\theta
\end{pmatrix},\qquad q=(1,0),
\quad Q=\frac{5-3\cos2\theta}{8},
\quad b^2=\frac9{53-3\cos2\theta}.
\tag{2.1}
\]

The hypersurface metric is \(h=b^2d\theta^2+M_{ab}d\xi^ad\xi^b\).
Prescribe only the mixed second fundamental entries
\(K_{\theta a}=bq_a/2\). Then

\[
H=0,\quad |K|^2=Q,\quad R_h=-6-Q,\quad
\operatorname{div}K=0.
\tag{2.2}
\]

These are the analytic Einstein Cauchy constraints. The analytic Cauchy
theorem gives a genuine Einstein germ, not just a formal jet; see
Ammann--Moroianu--Moroianu, Theorem 2.1
([primary text](https://moroianu.perso.math.cnrs.fr/tex/2013cmp.pdf)).
On its central separator \(\sigma_s=\sigma_n=e_n=0\) and
\(e_s=12+2Q\). Both forms of the stability potential reduce to

\[
\mathcal V=3-Q\ge2,
\tag{2.3}
\]

since \(1/4\le Q\le1\). Thus its incompressible torus is strictly stable
in a genuine charged Einstein neighborhood. Any contradiction for a
complete filling must use information that reaches beyond such a
neighborhood, for example an estimate coupling it to both conformal ends.

## 3. A complete countermodel to weaker topological hypotheses

There is also an explicit complete countermodel if the exact Einstein
equation is weakened to its Ricci lower bound. On \(T^3\), with all
coordinates periodic, define

\[
h=d\theta^2+e^{\sin\theta}dx^2+e^{-\sin\theta}dy^2,
\qquad
g=dt^2+\cosh^2t\,h\quad\hbox{on }\mathbb R\times T^3.
\tag{3.1}
\]

The eigenvalues of \(h^{-1}\operatorname{Ric}_h\) are

\[
-\tfrac12\cos^2\theta,\quad
\tfrac12\sin\theta,\quad-\tfrac12\sin\theta.
\tag{3.2}
\]

Hence \(\operatorname{Ric}_h\ge-h/2\). Warped-product curvature gives
\(\operatorname{Ric}_g(\partial_t,\partial_t)=-3\), and on tangential
endomorphisms

\[
g^{-1}\operatorname{Ric}_g
=-3I+\cosh^{-2}t\,(h^{-1}\operatorname{Ric}_h+2I)\ge-3I.
\tag{3.3}
\]

The metric is complete and smoothly AH at both ends. Indeed with
\(z=2e^{-|t|}\) near either end,
\[
g=z^{-2}\left[dz^2+(1+z^2/4)^2h\right].
\tag{3.4}
\]
Both conformal classes are strictly negative Yamabe: the constant test
function has negative Yamabe numerator because
\(R_h=-\cos^2\theta/2\) and \(\int R_h<0\).
The central incompressible \(T^3\) is totally geodesic and its Jacobi
operator is \(-\Delta_h+3>0\). The two ends, free torus action,
\(\pi_1=\mathbb Z^3\), spin topology, and essential \(H_3\) all have the
same types as in the target problem.

Moreover \(v(t)=\operatorname{sech}^2t\) is a positive \(L^2\) eigenfunction
with \(-\Delta_gv=2v\). The ground-state transform proves \(\lambda_0=2\).
Thus amenability does not itself provide the strict spectral lower bound
needed in a connectedness argument. This is a specialization of the
classical cosh-warped spectral borderline geometry, not a new Einstein
construction. In particular (3.3) is **not** equality: the countermodel
does not solve the target Einstein equation.

## 4. Amenable covers preserve, rather than repair, the spectral deficit

If the target charged Einstein cylinder exists, `round7_spectral.md` gives
\(\lambda_0(M)<2\). Every subgroup of \(\pi_1(M)=\mathbb Z^3\) is normal
and its quotient is amenable. The amenable-cover equality therefore gives

\[
\lambda_0(\widehat M)=\lambda_0(M)<2
\tag{4.1}
\]

for **every** connected Riemannian covering, including the universal
cover. For an infinite covering the bottom is also in the essential
spectrum. These statements follow from Ballmann--Matthiesen--Polymerakis,
equation (1.2) and Proposition 1.13(1), respectively
([primary text](https://archive.mpim-bonn.mpg.de/1767/1/preprint_2018_19.pdf)).
They do not require an unsupported lower spectral bound on a simply
connected negative Einstein manifold. Passing to larger torus covers
cannot turn this particular spectral deficit into a contradiction.

Two nearby theorems do not supply the missing obstruction. Wang's torus
spin nonexistence theorem requires **flat conformal infinity**; the
connectedness theorem requires a **nonnegative Yamabe conformal class**.
The original statements are Theorems 1.3 and 2.2 in
[Wang's paper](https://www.intlpress.com/site/pub/files/_fulltext/journals/mrl/2001/0008/0005/MRL-2001-0008-0005-a009.pdf).
Neither hypothesis follows from the underlying boundary being a torus.

## 5. Exact outcome

The charged separator has a complete, reproducible scalar stability
criterion, and strictly stable Einstein throat data pass it. A concrete
complete negative-Yamabe model disproves the corresponding claim based
only on Ricci lower bounds and topology. Amenable covering cannot supply
the missing spectral improvement. These methods alone do not upgrade the
OT/static exclusions. The distinct proof in `round9_connector.md` does
make that upgrade for the full marked free-torus class, including nonzero
charge. Nonsymmetric exact Einstein fillings and uniform near-Einstein
connector gaps remain separate questions.

`round9_global_check.py` verifies the local curvature, Jacobi conjugation,
potential coefficients, spectral eigenfunction, and charged-germ algebra.
It does not certify a global Einstein continuation.
