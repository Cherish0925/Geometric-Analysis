# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Sessions/S1003A01/workspace/notes/step60_kahler_rigidity_weyl_pinching_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md"
  ]
}
```

## Task

Closed negative Goldberg problem (closed 4-manifold, Einstein Ric=lambda g with lambda<0, almost-Kahler Omega; does Omega have to be Kahler?). New local result (attached note): at every torsion zero, |nabla^2 Omega|^2 = 4trV^2 - 12|eta|^2, so the first torsion jet lies on the cone ||A||^2=8|c|^2+||S||^2 and every nondegenerate zero has index +1; W3+ != 0 at every zero with nonzero first jet; the identity is lambda-independent and Ricci-flat Gibbons-Hawking degenerate zeros lie on it. Topology forces total torsion charge 5chi+6tau>0. Propose the strongest concrete next mathematical mechanisms that could turn this into a global obstruction or, conversely, into a construction of a negative-scalar closed or local counterexample germ with an isolated zero. Candidates to evaluate rigorously, not just list: (a) a next-order (cubic/third-jet) identity obtained from Delta^2 of the Weitzenbock identity or from Bianchi relations between nabla^2 W+ and nabla^3 Omega, and whether lambda can enter there; (b) a pointwise elliptic inequality for q or for |nabla Omega| near zeros (e.g. Delta q >= ... using the global AAD Weitzenbock), giving a maximum-principle or Morse/Poincare-Hopf argument tied to the forced positive charge; (c) combining index +1 with the localization of zeros in {lambda_min(W+)<=s/6} and the Hopf/linking-sphere picture; (d) a model local negative AKE germ with an isolated nondegenerate zero (e.g. a cohomogeneity-one or toric ansatz with a fixed point) that would show the local theory cannot close Goldberg. For each, state precisely what would have to be computed and what result would change the global judgment.

## Output

The new cone relation is strong enough to reorganize the problem around three sharply testable mechanisms: an even-order prolongation where \(s\) first contributes coercively, a Morse-theoretic consequence for \(q=|\nabla\Omega|^{2}\), and a Hopf/Chern–Simons localization of the now-positive zero charge. A symmetric local model with a nut gives a particularly economical realization test.

Throughout, put
\[
u=\frac{\Omega}{\sqrt2},\qquad T=\nabla\Omega,\qquad q=|T|^{2},
\qquad r=\langle W^{+}u,u\rangle=\frac{s}{6}+\frac q4,
\]
and write \(K=\nabla T=\nabla^{2}\Omega\) at a torsion zero.

## 1. The next prolongation: the first realistic place for an \(s<0\) local obstruction

At \(T(p)=0\),
\[
q_{;ij}(p)=2\langle K_i,K_j\rangle,\qquad
\Delta q(p)=2|K|^{2},
\]
for \(\Delta=\operatorname{tr}\nabla^{2}\). The established identity gives
\[
|K|^{2}=4\operatorname{tr}V^{2}-12|\eta|^{2},
\]
equivalently
\[
\|A\|^{2}=8|c|^{2}+\|S\|^{2}.
\]

The relevant Einstein equation for the next prolongation is
\[
\nabla^{*}\nabla W^{+}
=P_s(W^{+})
:=-\frac{s}{2}W^{+}+6(W^{+})^{2}
-2\operatorname{tr}\bigl((W^{+})^{2}\bigr)I. \tag{1.1}
\]
Differentiating (1.1) introduces
\[
DP_s(W^{+})[\nabla W^{+}],
\]
which contains \(-\frac{s}{2}\nabla W^{+}\). Thus the cancellation seen in the zero identity does not persist automatically: \(s\) already occurs in the degree-five equations. It may, however, multiply freely adjustable components of \(\nabla W^{+}\), so its mere appearance need not produce a relation on \(c,S,A\).

A clean invariant prolongation uses the following unknowns at \(p\):

\[
K=\nabla T,\qquad L=\nabla K=\nabla^{3}\Omega,\qquad
U=\nabla W^{+},
\]
subject to

\[
L_{aij}-L_{aji}=(\nabla_aR_{ij})\cdot\Omega,
\]
the differentiated harmonic-form equation, \(\delta W^{+}=0\), the differentiated Ricci identities, and the derivative of (1.1). The finite-dimensional question is whether the projection
\[
\{(K,L,U):\text{all degree-five equations}\}
\longrightarrow
\{K:\|A\|^{2}=8|c|^{2}+\|S\|^{2}\}
\]
is onto after requiring \(\det_{\mathbb R}Df\ne0\).

There is a structural reason to expect degree five to solve for \(L,U\) rather than produce a new scalar equation: it is an odd prolongation, and the differentiated scalar identity is linear in the next jets. The first especially promising scalar relation is therefore the even prolongation obtained from \(\Delta^{2}q=4\Delta^{2}r\). After replacing traced derivatives by the harmonic-form and harmonic-Weyl equations, its expected invariant shape is
\[
\mathcal Q_1(L,U)+s\,\mathcal Q_2(K)
+\mathcal Q_3(W^{+},K)=0, \tag{1.2}
\]
where \(\mathcal Q_1\) contains quadratic expressions in third jets. The decisive issue is the signature of \(\mathcal Q_1\) after all Bianchi and Ricci-commutator relations have been imposed.

The \(s\)-dependence can be seen explicitly by linearizing (1.1) at the Kähler-type operator
\[
W_0=\operatorname{diag}\left(\frac s6,-\frac{s}{12},-\frac{s}{12}\right).
\]
On the three \(U(2)\)-pieces of a trace-free perturbation, \(DP_s(W_0)\) has eigenvalues
\[
\frac s2\quad\text{on the scalar Kähler ray},\qquad
0\quad\text{on the \(W_2^{+}\) piece},\qquad
-\frac{3s}{2}\quad\text{on the \(W_3^{+}\) piece}. \tag{1.3}
\]
Thus the \(V=W_3^{+}\) mode acquires a strictly positive mass for \(s<0\), while the \(\eta=W_2^{+}\) mode remains massless at this linearized level. This makes a sum-of-squares identity involving \(V\) substantially more plausible than one involving \(\eta\) alone.

Three low-dimensional sectors expose all qualitatively different outcomes:

\[
S=0,\qquad |a|=2|c|;
\]
\[
c=0,\qquad \|A\|=\|S\|,\quad \det B\ne0;
\]
and a generic Takagi-normalized \(S\) with \(c,A\ne0\).

A relation of the form
\[
0=(-s)C|K|^{2}
+\sum_\rho |\mathcal L_\rho(L,U,K)|^{2},
\qquad C>0, \tag{1.4}
\]
would force \(K=0\) when \(s<0\). To reach the closed Goldberg theorem one would then need the analogous leading-homogeneous identity for every finite vanishing order of \(T\). Since Einstein metrics and harmonic forms are analytic, exclusion of every finite order would imply local Kählerness at each torsion zero, and the positive total charge would finish the argument.

At the other extreme, if the degree-five and degree-six systems are onto over an open subset of the cone, with no further polynomial relation on \(K\), then first-order nondegenerate zeros survive all currently visible local equations. An analytic ODE model realizing one such jet would then show that the torsion-zero analysis alone cannot settle the closed problem.

For zeros with \(K=0\), the most efficient formulation is a homogeneous indicial problem. If
\[
T=P_m+O(|x|^{m+1}),\qquad m\ge2,
\]
then \(W^{+}(p)=W_0\), and \(P_m\) satisfies the half-twistor symbol equation. Substituting \(P_m\) into the linearization governed by (1.3) produces a finite-dimensional problem on degree-\(m\) spherical harmonics. A coercive identity there would treat all higher-order zeros at once, rather than repeating the full jet calculation separately for each \(m\).

## 2. What a \(q\)-inequality can actually accomplish

A direct scalar maximum principle has a fundamental local obstacle. At a nondegenerate torsion zero,
\[
\Delta q(p)=2|K|^{2}>0.
\]
Consequently an estimate such as
\[
\Delta q\le Cq
\]
would immediately exclude such a zero, but it cannot follow from the already established zero equations: the forced source \(2|K|^{2}\) has the opposite behavior. The Bochner equation for \(q\) necessarily contains
\[
2|\nabla T|^{2}
\]
as well as curvature terms quadratic in \(T\) and terms involving \(\nabla W^{+}\ast T\). At the zero the latter terms vanish, leaving precisely the positive source.

The much stronger global consequence comes from Morse theory. Suppose all torsion zeros are nondegenerate and all critical points of \(q\) are isolated and Morse. Every torsion zero is a strict minimum of \(q\), hence contributes \(+1\) to the Poincaré–Hopf index of \(\nabla q\). Since every torsion zero also has torsion index \(+1\),
\[
N=\#Z=5\chi+6\tau
=\chi+2(2\chi+3\tau).
\]
Therefore
\[
\sum_{\substack{\nabla q=0\\q>0}}
\operatorname{ind}(\nabla q)
=\chi-N=-2(2\chi+3\tau)<0. \tag{2.1}
\]
If \(O\) is the number of positive-\(q\) critical points with odd Morse index and \(E\) the number with even Morse index, then
\[
O-E=2(2\chi+3\tau),\qquad
O\ge2(2\chi+3\tau). \tag{2.2}
\]
Thus every closed strict example with simple torsion zeros must contain many saddle points of \(q\) of Morse index \(1\) or \(3\).

This gives a precise tensorial target: it would suffice to prove
\[
\det\bigl(\operatorname{Hess}q\bigr)>0
\]
at every nondegenerate critical point with \(q>0\), or more geometrically that the Morse index of \(q\) is always even. Equation (2.1) would then be impossible.

A scalar Laplacian estimate controls only \(\operatorname{tr}\operatorname{Hess}q\), not its determinant or parity. In AAD gauge, \(q=4|a|^{2}\), so at a critical point
\[
\operatorname{Hess}q(X,Y)
=
8\langle\nabla_Xa,\nabla_Ya\rangle
+8\langle a,\nabla^2_{X,Y}a\rangle. \tag{2.3}
\]
The first term is positive semidefinite, while the trace-free part of the second term is the potential source of odd Morse index. The decisive point-jet computation is therefore the image of the Einstein–almost-Kähler jet equations in
\[
\operatorname{Sym}^{2}_{0}T_p^{*}M
\]
through (2.3), under \(q>0\) and \(dq=0\). If that image is all of \(\operatorname{Sym}^{2}_{0}\), then no pointwise \(q\)-inequality can control the Morse parity; some global or curvature-coupled input is required. If the image is Hermitian or has positive determinant, (2.1) gives a complete global obstruction.

A better scalar candidate couples \(q\) to Weyl curvature. The Einstein identity
\[
\frac12\Delta|W^{+}|^{2}
=
|\nabla W^{+}|^{2}
+\frac{s}{2}|W^{+}|^{2}
-18\det W^{+} \tag{2.4}
\]
can be combined with the exact Bochner equation for \(q\). For
\[
F=q+\gamma\left(|W^{+}|^{2}-\frac{s^{2}}{24}\right),
\]
one can decompose the gradient terms into \(U(2)\)-irreducibles and optimize \(\gamma\) so that the \(\nabla W^{+}\ast T\) term is absorbed into
\[
|\nabla T|^{2}+\gamma|\nabla W^{+}|^{2}.
\]
A zeroth-order polynomial with one sign at an extremum of \(F\) would give a genuine compact maximum-principle theorem. The exact complete \(s<0\) model suggests that any such \(F\) must exploit compact attainment of an extremum: its Kähler-type value is approached only at the infinite end.

## 3. Positive local degree, Weyl localization, and the Hopf class

The cone strengthens the Weyl localization considerably. At a zero with \(K\ne0\),
\[
|W^{+}|^{2}-\frac{s^{2}}{24}
=
2|\eta|^{2}+\operatorname{tr}V^{2}
=
\frac14|K|^{2}+5|\eta|^{2}>0. \tag{3.1}
\]
Hence every such zero lies in
\[
\mathcal U=\left\{|W^{+}|^{2}>\frac{s^{2}}{24}\right\},
\]
not merely in \(\{\lambda_{\min}(W^{+})\le s/6\}\). If \(c\ne0\), then \(\eta\ne0\) and in fact
\[
\lambda_{\min}(W^{+})<\frac s6.
\]

Topology alone permits the charge to sit in disjoint small balls contained in \(\mathcal U\). To extract more, the appropriate object is the global angular form of the torsion bundle \(E\). Let \(\Psi_\nabla\) be normalized by
\[
\int_{S(E_x)}\Psi_\nabla=1,\qquad
d\Psi_\nabla=-\pi^{*}e(E).
\]
On \(M\setminus Z\), let \(\widehat T=T/|T|\). For every smooth weight \(h\),
\[
\sum_{p\in Z}h(p)\operatorname{ind}_p(T)
=
\int_M h\,e(E)
-\int_{M\setminus Z}dh\wedge\widehat T^{*}\Psi_\nabla. \tag{3.2}
\]
Choosing \(h\) as a smooth function of
\[
|W^{+}|^{2}-s^{2}/24
\quad\text{or}\quad
\lambda_{\min}(W^{+})-s/6
\]
turns the Weyl localization into an exact weighted charge identity. The concrete calculation is to express the second term in (3.2) through \(a,b,\eta,V\) and then use \(\delta W^{+}=0\) and the AAD equations. Either of the following outcomes would be decisive:

* the right-hand side has a sign incompatible with the positive left-hand side when \(h\) is supported in \(\mathcal U\);
* each unit of local charge forces a uniform amount of normalized Weyl energy. Combined with Chern–Weil formulas, this becomes a numerical inequality involving \(\chi,\tau\).

The linking-sphere formulation is even sharper. Around a nondegenerate zero,
\[
\widehat T:S^{3}\longrightarrow S^{3}
\]
has degree \(+1\). Projectivizing the twisted spinor \(\alpha\) gives
\[
[\alpha]:S^{3}\longrightarrow\mathbb{CP}^{1}\cong S^{2},
\]
and
\[
\operatorname{Hopf}([\alpha])=+1. \tag{3.3}
\]
Because \(W_3^{+}(p)\ne0\), any curvature construction producing a complex line
\[
\mathcal D(W^{+},\nabla W^{+},\ldots)\subset T^{1,0}M
\]
which

1. extends continuously across \(p\), and  
2. is homotopic on the punctured ball to \([\alpha]\),

would contradict (3.3): an extendible map from the ball has Hopf invariant zero. The computation is thus very concrete: search the differentiated Bianchi equations for a rank-one relation recovering \([\alpha]\) from an eigenspace, image, or kernel of a smooth curvature-derived tensor. The cone supplies the key input \(W_3^{+}(p)\ne0\), which permits division by the \(W_3^{+}\) coefficient in such a formula.

The eigenvalue equation offers a related route. If \(\mu=\lambda_{\min}(W^{+})\) is simple with unit eigenvector \(v\), then
\[
\Delta\mu
=
\frac{s}{2}\mu-6\mu^{2}+2|W^{+}|^{2}
+
2\sum_{a,j>1}
\frac{|\langle(\nabla_aW^{+})v,v_j\rangle|^{2}}
{\mu-\mu_j},
\]
hence
\[
\Delta\mu\le
\frac{s}{2}\mu-6\mu^{2}+2|W^{+}|^{2}. \tag{3.4}
\]
An AKE relation forcing the right-hand side of (3.4) to be \(<0\) on \(\{\mu<s/6\}\) would rule out a spatial minimum there and hence rule out the \(c\ne0\) zeros. The cone alone does not control \(|W^{+}|\) relative to \(s\), so the missing substance is an additional algebraic relation from the next prolongation or a global pinching estimate.

## 4. A local \(s<0\) germ with a nut: the most economical construction test

A toric fixed point is poorly suited to a nondegenerate torsion zero. If the tangent \(T^{2}\)-weights are \(\xi_1,\xi_2\), the complex weights of
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2}
\]
are
\[
2\xi_1+\xi_2,\qquad \xi_1+2\xi_2.
\]
For an effective fixed point these do not match the tangent weights, so an invariant linear map
\[
T_pM\longrightarrow E_p
\]
vanishes. An invariant toric torsion zero therefore has order at least two.

An \(SU(2)\)-nut has the opposite representation theory: the tangent and torsion representations are equivalent, so an equivariant \(DT(p)\) can be an isomorphism. Take
\[
d\sigma_i=2\sigma_j\wedge\sigma_k,\qquad
g=dt^{2}+\sum_{i=1}^{3}a_i(t)^{2}\sigma_i^{2},
\]
and
\[
e^0=dt,\qquad e^i=a_i\sigma_i,\qquad
\omega_i=e^{0i}+e^{jk},
\]
with
\[
\Omega=\sum_{i=1}^{3}x_i(t)\omega_i,\qquad
\sum_i x_i^{2}=1.
\]
Closedness is exactly
\[
\bigl(x_i a_j a_k\bigr)'=2x_i a_i,
\]
or
\[
\frac{x_i'}{x_i}
=
\frac{2a_i}{a_ja_k}
-\frac{a_j'}{a_j}
-\frac{a_k'}{a_k}. \tag{4.1}
\]

The diagonal Einstein equations are
\[
-\sum_i\frac{a_i''}{a_i}=\lambda,
\]
and cyclically
\[
-\frac{a_i''}{a_i}
-\frac{a_i'}{a_i}
 \left(\frac{a_j'}{a_j}+\frac{a_k'}{a_k}\right)
+
\frac{2\bigl(a_i^{4}-(a_j^{2}-a_k^{2})^{2}\bigr)}
{a_i^{2}a_j^{2}a_k^{2}}
=\lambda. \tag{4.2}
\]

Smoothness at the nut gives
\[
a_i(t)=t\bigl(1+A_it^{2}+B_it^{4}+\cdots\bigr),
\qquad
x_i(t)=x_i^{0}+X_it^{2}+Y_it^{4}+\cdots,
\]
with
\[
\sum_iA_i=-\frac{\lambda}{6},\qquad
\sum_i(x_i^{0})^{2}=1.
\]
From (4.1),
\[
\frac{x_i'}{x_i}
=
\kappa_i t+O(t^{3}),
\qquad
\kappa_i=2(A_i-2A_j-2A_k)=6A_i-4\sum_\ell A_\ell,
\]
so
\[
X_i=\frac{\kappa_i}{2}x_i^{0},\qquad
\sum_i\kappa_i(x_i^{0})^{2}=0. \tag{4.3}
\]
Equation (4.3) is the nut version of the zero Rayleigh identity \(r=s/6\). Solving (4.2) for the \(B_i\) and imposing the \(t^{4}\)-coefficient of \(\sum x_i^{2}=1\) should reproduce the cone
\[
\|A\|^{2}=8|c|^{2}+\|S\|^{2}.
\]
The \(t^{6}\)-coefficient is then the symmetric-ansatz realization of the degree-six prolongation discussed above, and it is the first place where a genuine \(\lambda\)-dependent amplitude relation can appear.

The essential computation is to convert the expansion from \((t,\sigma_i)\) to smooth quaternionic Cartesian coordinates and calculate
\[
DT(0):T_0\mathbb R^{4}\longrightarrow E_0.
\]
Its determinant is an explicit polynomial in \(A_i\) and \(x_i^{0}\). A branch satisfying

\[
\det DT(0)>0,\qquad
T(t)\ne0\quad(0<t<\varepsilon),
\]
together with all coefficient equations, gives an isolated nondegenerate zero. Writing \(\rho=t^{2}\) converts the regular-singular system to an analytic ODE–algebraic system; a branch with nonsingular algebraic Jacobian then converges by the analytic implicit-function and ODE theorems. This would be an actual local strict Einstein almost-Kähler germ, not merely a finite jet.

Conversely, if the \(t^{6}\) equation reduces to
\[
(-\lambda)\,\det(DT(0))^{1/2}
+\sum |\text{higher-mode coefficients}|^{2}=0
\]
or an equivalent positive expression, then no \(SU(2)\)-nut model with \(\lambda<0\) exists. Such an outcome would strongly support the all-order prolongation route, though it would not by itself treat nonsymmetric germs.

No compact \(\lambda<0\) example can retain this continuous symmetry. For a Killing field \(X\) on a closed Einstein manifold,
\[
\int_M|\nabla X|^{2}
=
\lambda\int_M|X|^{2},
\]
so \(\lambda<0\) forces \(X=0\). The nut ansatz is therefore a local realization device; a closed construction would require symmetry breaking and a global elliptic gluing or deformation argument.

## Overall mathematical separation

The even prolongation and the \(SU(2)\)-nut series are two representations of the same central question. A coercive \(s\)-dependent identity at degree six, extended to every finite vanishing order, would combine with \(5\chi+6\tau>0\) to settle the closed problem. An analytic nut branch with \(\det DT(0)>0\) would instead establish that strict \(s<0\) geometry can pass smoothly through an isolated charged zero.

Independently, the global \(q\)-identity (2.1) gives a strong necessary signature: a closed strict example with simple zeros must contain at least \(2(2\chi+3\tau)\) odd-index saddles of \(q\). A tensorial Hessian theorem excluding those saddles would settle the compact problem even if local charged germs exist.

Finally, the Hopf formulation isolates the most geometric local obstruction: the cone forces Hopf invariant \(+1\) while \(W_3^{+}(p)\ne0\). Any Bianchi-derived curvature line extending across the zero and matching the torsion line on the linking sphere would make these two facts incompatible.