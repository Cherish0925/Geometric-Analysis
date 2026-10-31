# Full-core curvature cost and extremal metrics

27 September 2026. Continuation from `0c8059f`.

This proof develops the two open interfaces left in
[the preceding continuation](20260927_local_geometry_and_variational_extrema.md):
the smooth filling of its actual resonant annuli, and the all-metric sharp
coefficient. It does not reopen the already proved linear small-h order.
No web handoff package is generated.

The filling argument below is a synthesis of classical boundary curvature
formulas with the project's actual holonomy calculation. It is not a new
index theorem or a classification of all Ricci-flat ALE spaces. Its new use
here is that an entire smooth core pays a scale-independent cost even when
its exterior annulus satisfies both actual local spinor equations.

## 1. An entire resonant core has a uniform curvature cost

All orientations in this section are physical orientations, not orientations
chosen after identifying the underlying lens space. Weyl norms are the
Hilbert--Schmidt norms of the endomorphisms of two-forms,
\(|W^\pm|^2=\operatorname{tr}((W^\pm)^2)\), not their spectral operator
norms. Put

\[
 \mathscr Q(g)=|\operatorname{Ric}^{\circ}|^2
                       +4|W^+|^2+\frac{s^2}{12}.
                                                        \tag{1.1}
\]

Let \(\Gamma_n\) act on \(\mathbb C^2\), with its complex orientation, by
\((z_1,z_2)\mapsto(\zeta z_1,\zeta^{-2}z_2)\), where \(n\ge3\) is odd.
Let \(\Omega\) be any compact connected oriented smooth four-manifold with
one boundary component, identified with \(S^3/\Gamma_n\). Suppose its metric
has an outward Euclidean conical collar: near the boundary it is
\(dr^2+r^2g_{S^3/\Gamma_n}\), with \(r\) increasing outward.

There are **no** conditions on the interior fundamental group, intersection
form, complex structure, spinor zeros, or the number of smaller scales inside
\(\Omega\). Then

\[
 \boxed{\int_\Omega\mathscr Q(g)\ge
              8\pi^2\frac{n-1}{2n}\ge\frac{8\pi^2}{3}.}
                                                        \tag{1.2}
\]

### 1.1. Boundary formula, including its sign

Attach the exactly flat exterior cone to obtain a smooth complete ALE
manifold with compactly supported curvature. Its Euler characteristic and
signature are those of \(\Omega\). Use the convention

\[
 \chi=\frac1{8\pi^2}\int
       \left(|W^+|^2+|W^-|^2-\frac12|\operatorname{Ric}^{\circ}|^2
                                      +\frac{s^2}{24}\right)+\frac1n,
\]
\[
 \tau=\frac1{12\pi^2}\int(|W^+|^2-|W^-|^2)
                                      +\eta_{\rm LV}(\Gamma_n).
                                                        \tag{1.3}
\]

Here \(\eta_{\rm LV}\) is the positive cotangent-sum convention of
[Lock--Viaclovsky, equations (1-5), (3-1), and (3-5)](https://msp.org/gt/2016/20-3/gt-v20-n3-p13-s.pdf).
It is the negative of the boundary eta convention in which the signature
formula has a minus sign. The convention is fixed by (1.3), not by an
unqualified occurrence of the word eta.

For odd \(n\), the negative continued fraction is

\[
 \frac{n}{n-2}=[\underbrace{2,\ldots,2}_{(n-3)/2},3],
 \qquad (n-2)^{-1}\equiv\frac{n-1}{2}\pmod n.
\]

Substitution into the cyclic eta formula gives

\[
 \eta_{\rm LV}(\Gamma_n)
       =-\frac{(n-1)(n-5)}{6n},\qquad
 B_n:=\frac2n+3\eta_{\rm LV}(\Gamma_n)
       =3-\frac n2-\frac1{2n}.
                                                        \tag{1.4}
\]

Consequently the exact signed relation is

\[
 2\chi(\Omega)+3\tau(\Omega)-B_n
 =\frac1{4\pi^2}\int_\Omega
       \left(2|W^+|^2+\frac{s^2}{24}
                                  -\frac{|\operatorname{Ric}^{\circ}|^2}{2}\right).
                                                        \tag{1.5}
\]

This formula loses the whole \(W^-\) term. No upper bound for that term
has been inserted. Since the boundary is a rational homology sphere,
\(\tau(\Omega)\) is the integer signature of the relative intersection
pairing. Also

\[
 B_n=\frac{5-n}{2}+\frac{n-1}{2n},\qquad
 \operatorname{dist}(B_n,\mathbb Z)=\frac{n-1}{2n}\ge\frac13.
                                                        \tag{1.6}
\]

The absolute value of the integral in (1.5) is at most
\(\tfrac12\int\mathscr Q\). This proves (1.2).

For a sign check, \(n=3\) gives \(B_3=4/3\); \(n=5\) gives \(B_5=2/5\).
Reversing the cone orientation changes the calculation. In particular the
orientation reversal at \(n=3\) is an \(A_2\) cone and does have a Ricci-flat
hyperkähler filling. It is not covered by (1.2).

### 1.2. Actual approximately conical collars

The assertion is stable under the collar hypothesis used in the preceding
annular theorem. More precisely, suppose an inner collar of \(\Omega\)
is identified with \(\{1/2<|y|\le1\}/\Gamma_n\), and the **lift** of
\(r^{-2}g\) has Euclidean \(C^2\) distance at most \(\delta\). Then

\[
 \boxed{\int_\Omega\mathscr Q(g)
          \ge 8\pi^2\frac{n-1}{2n}-C\delta^2/n.}
                                                        \tag{1.7}
\]

The constant is independent of odd \(n\) and of the physical scale \(r\).
To prove this, leave the metric unchanged below radius \(3/4\), and on
the fixed annulus interpolate, with a fixed radial cutoff, to the flat cone
metric before reaching radius 1. The lifted interpolated metric is positive
definite for small universal \(\delta\), and its curvature is
\(O(\delta)\) in the rescaled coordinates. Its volume is \(O(1/n)\).
Thus the added integral of (1.1) is at most \(C\delta^2/n\). Extend by
the flat cone and apply (1.2). The unchanged interior contributes its
original integral; the nonnegative original collar contribution can simply
be retained in the upper bound. Four-dimensional curvature-square integrals
are invariant under the homothety, proving (1.7) at every \(r\).

Fixing a sufficiently small universal \(\delta_0\), (1.7) in particular
gives the order-independent lower bound

\[
                  \int_\Omega\mathscr Q\ge q_0,
                  \qquad q_0=4\pi^2/3.              \tag{1.8}
\]

Unlike the finite-family constants in the spinor annular compactness
argument, this constant does not deteriorate as the quotient order grows.
The lifted metric control is essential; a bare diffeomorphism of the
intrinsic boundary to a lens space does not give (1.7).

### 1.3. Consequence for the original integral defect

Let \(M\) be closed and oriented, let \(\omega\) be a smooth self-dual
two-form with \(|\omega|\le L\), and \(0\le t\le1/4\). As before set

\[
 A_{\omega,t}=t\left(\frac{|\omega|^2}{3}I-\omega\otimes\omega\right),
\]
\[
 Z_t=|\operatorname{Ric}+g|^2+|W^+-A_{\omega,t}|^2
                         +( |\omega|^2-2)^2+|d\omega|^2,
 \qquad z=V^{-1}\int_M Z_t.                         \tag{1.9}
\]

Suppose \(\Omega_1,\ldots,\Omega_N\subset M\) are embedded smooth
one-boundary cores of the kind in Section 1.2, with overlap at most
\(\Lambda\). Their odd orders may vary without bound. If

\[
 \operatorname{Vol}(\Omega_i)\le v_0(L),\qquad
 v_0(L)=\frac{q_0}{2(8+L^4/3)},
                                                        \tag{1.10}
\]

then

\[
                    \boxed{\frac NV\le\frac{16\Lambda}{q_0}\,z.}
                                                        \tag{1.11}
\]

Indeed, \(|A_{\omega,t}|^2=(2/3)t^2|\omega|^4\le L^4/24\), so

\[
 \mathscr Q\le |\operatorname{Ric}|^2+4|W^+|^2
          \le8Z_t+8+L^4/3.                         \tag{1.12}
\]

Sum (1.8), use the overlap for the defect term, and absorb the sum of
core volumes using (1.10). This proves (1.11). No pointwise Ricci bound,
noncollapse, diameter, Sobolev constant, first-order expansion, or
control of \(W^-\) is used.

For the actual weighted forms of the previous proof, their uniform
amplitude bound and \(\int Z_{1/\beta}\le C\eta V\) give

\[
                         N/V\le C\Lambda\eta.       \tag{1.13}
\]

Thus a positive density of small-volume smoothly filled resonant cores
cannot occur in a zero-defect sequence, however small their individual
radii and however long the inner scale separation. The local resonant
annuli from the preceding construction remain valid: they did not fill
their quotient apex. Equations (1.7)--(1.13) concern the **whole** smooth
filling, not an isolated terminal bubble or an unmarked cap.

The original averaged hypotheses have not been proved to produce these
embedded cores, their overlap bound, or their small volumes. This result
therefore removes an actual smooth-filling alternative when present; it
does not itself prove the unrestricted integral zero-end theorem.

### 1.4. Intermediate cores and cancellation across scales

For a smooth region \(W\) with one outgoing conical boundary of type
\(\Gamma_{n_0}\) and \(r\) incoming conical boundaries of types
\(\Gamma_{n_1},\ldots,\Gamma_{n_r}\), the same calculation gives

\[
 2\chi(W)+3\tau(W)-B_{n_0}+\sum_{i=1}^r B_{n_i}
   =\frac1{4\pi^2}\int_W
     \left(2|W^+|^2+\frac{s^2}{24}
                         -\frac{|\operatorname{Ric}^{\circ}|^2}{2}\right).
                                                        \tag{1.14}
\]

This is the boundary transgression formula with the incoming shape
operators and boundary orientations reversed. It can also be verified
by gluing arbitrary smooth caps and subtracting (1.5); signature and
Euler characteristic are additive across rational homology three-spheres.

In particular a one-child flat neck has no cost: identical boundary
terms cancel. It is wrong to apply (1.2) independently to every vertex
of a bubble tree. When the entire core is smoothly filled, all internal
terms in (1.14) cancel and (1.5) for its outer boundary survives. A
multiscale decomposition cannot remove the full-core cost.

There is also a uniform intermediate restriction. With two incoming
resonant boundaries, write \(f_n=(n-1)/(2n)\in[1/3,1/2)\). Then

\[
 f_{n_0}-f_{n_1}-f_{n_2}\in(-2/3,-1/6),\qquad
 \operatorname{dist}(B_{n_0}-B_{n_1}-B_{n_2},\mathbb Z)>1/6.
\]

Consequently an exactly conical binary branching region pays
\(\int_W\mathscr Q>4\pi^2/3\). This is not an arbitrary-valence
rule: with outgoing order 3 and three incoming orders 9 the fractional
terms differ by \(1/3-3(4/9)=-1\). The numerical obstruction then
vanishes. That arithmetic example asserts neither existence of a
zero-cost cobordism nor a solution of the actual field equations.

### 1.5. The full-core cost is sharp, and its sign has content

The boundary value in (1.2) is the exact infimum, not only a convenient
lower bound:

\[
 \boxed{\inf_{\text{smooth conically collared fillings of }\Gamma_n}
                   \int\mathscr Q=4\pi^2\frac{n-1}{n}.}        \tag{1.15}
\]

The same infimum is obtained if the smooth topology is fixed to a compact
truncation of the minimal complex resolution. Indeed, its exceptional
chain is the negative definite chain
\([2,\ldots,2,3]\) of length \((n-1)/2\). Hence

\[
 \chi=(n+1)/2,\qquad \tau=-(n-1)/2,\qquad
                 2\chi+3\tau=(5-n)/2=\lfloor B_n\rfloor.
\]

[Calderbank--Singer, Theorem A](https://arxiv.org/pdf/math/0206229)
provides a complete scalar-flat Kähler ALE metric on this resolution.
In the complex orientation \(W^+=s=0\), so (1.5), now taken on its
complete ALE end, gives

\[
 \int|\operatorname{Ric}^{\circ}|^2
                 =8\pi^2\frac{n-1}{2n}.             \tag{1.16}
\]

Truncate at radius \(R\to\infty\). The ALE estimates make the lifted
rescaled metric \(C^2\)-close to the flat cone on the truncation collar.
Flatten that collar by the construction of Section 1.2. The change in
the curvature-square integral tends to zero. Rescale the truncation to
a fixed boundary radius; the energy is unchanged. This gives the upper
bound in (1.15); (1.2) gives the lower bound. Further homotheties make
the core volume as small as desired without changing this cost. No
attainment assertion for the exactly conical compact problem is needed.

This uses a classical existence theorem to calibrate the new full-core
inequality; it is not a new scalar-flat ALE construction.

More precisely, put \(f_n=(n-1)/(2n)\) and
\(j=2\chi+3\tau-\lfloor B_n\rfloor\in\mathbb Z\). The signed identity
is

\[
 P=4W_++S_2/12+8\pi^2(f_n-j),                       \tag{1.17}
\]

where the integrals are over the core. Thus \(j\le0\) forces
\(P\ge8\pi^2f_n\), whereas \(j\ge1\) forces
\(4W_++S_2/12\ge8\pi^2(1-f_n)\). The integer topology decides which
side pays. For a complete Ricci-flat ALE filling this implies
\(W_+\ge2\pi^2(1-f_n)=\pi^2(1+1/n)\); it does not rule out every
non-ASD Ricci-flat filling.

The sharp examples also delimit what this argument can control. On their
complete scalar-flat Kähler models,

\[
 \int|W^-|^2=4\pi^2n+6\pi^2-10\pi^2/n,
 \qquad \int\mathscr Q=4\pi^2(1-1/n).
                                                        \tag{1.18}
\]

Thus Euler number and opposite-chiral energy can grow without bound
while the full-core cost stays bounded. There can be no order-independent
estimate of core Euler number by this cost alone. These are actual metrics
on noncompact resolutions, not a closed zero-end sequence with actual
monopole supply. In particular (1.18) does not contradict (1.11), which
counts cores rather than their Euler numbers.

### 1.6. A defect atom, not only a curvature atom

The sign in (1.17) improves the translation to the actual defect. Write
\(e=\int_\Omega Z_t\), \(v=\operatorname{Vol}(\Omega)\), and
\(b_L=2/3+L^4/12\). The collar-flattening construction also controls
the **signed** error in (1.5): if its error in the unnormalized integral
is at most \(\epsilon=C\delta^2/n\), then

\[
 j\le0\quad\Longrightarrow\quad
 \int_\Omega|\operatorname{Ric}+g|^2
              \ge8\pi^2(f_n-j)-2\epsilon;                       \tag{1.19}
\]
\[
 j\ge1\quad\Longrightarrow\quad
 e\ge\frac12\left[
       \sqrt{(4\pi^2(j-f_n)-\epsilon)_+}-\sqrt{b_Lv}
                         \right]_+^2.                          \tag{1.20}
\]

For (1.19), \(P\le\int|\operatorname{Ric}+g|^2\le e\) and (1.17)
suffice; no small-volume assumption is needed. For (1.20), apply the Hilbert-space triangle inequality to
\((\sqrt2W^+,s/\sqrt{24})\), splitting it into the error
\((\sqrt2(W^+-A_{\omega,t}),(s+4)/\sqrt{24})\) and the bounded model
\((\sqrt2A_{\omega,t},-4/\sqrt{24})\). Since
\(|s+4|^2\le4|\operatorname{Ric}+g|^2\), this gives

\[
 \int_\Omega(2|W^+|^2+s^2/24)
                 \le(\sqrt{2e}+\sqrt{b_Lv})^2.
\]

Its left side is at least \(4\pi^2(j-f_n)-\epsilon\) by the signed
formula and \(P\ge0\). Thus (1.20) follows.

For any sequence of such smooth cores with \(v\to0\) and
\(\delta\to0\), possibly with unbounded odd orders,

\[
                       \boxed{\liminf\int_\Omega Z_t\ge\pi^2.} \tag{1.21}
\]

For fixed order the lower bound is \(\pi^2(1+1/n)\), or the stronger
\(4\pi^2(1-1/n)\) on the branch \(j\le0\). Unlike the sharp
\(\mathscr Q\) infimum, sharpness of (1.20)--(1.21) for an actual
monopole field is not asserted. An orbifold core with an unfilled apex
is not smooth and may have zero cost; its missing boundary contribution
must not be discarded.

There is an immediate pure-Ricci application: a bounded-overlap collection
of minimal-resolution cores (or any of the \(j\le0\) topologies), with
the prescribed small collar error, satisfies

\[
 \sum_i(f_{n_i}-j_i)\le C\Lambda
                         \int_M|\operatorname{Ric}+g|^2.        \tag{1.22}
\]

Absorb the collar errors into \(f_{n_i}-j_i\ge1/3\). This needs no
volume bound on the cores and no gauge field. Extra interior blow-ups
decrease \(j_i\) and incur additional linear cost, even if hidden at
smaller scales. The Calderbank--Singer truncations followed by shrinking
homotheties make \(\int|\operatorname{Ric}+g|^2\to8\pi^2f_n\):
the scalar cross term and the volume term vanish under that last
homothety. Thus the minimal-resolution pure-Ricci cost is also
asymptotically sharp as a metric-cap statement.

## 2. A second obstruction: a faithful determinant cannot extend flatly

The curvature cost has an independent global interpretation which avoids
the classification of Ricci-flat ALE spaces.

**Proposition.** Let \(X^m\), \(m\ge3\), be a smooth connected complete
ALE manifold with \(\operatorname{Ric}\ge0\) and nontrivial infinity
group \(\Gamma\). No flat unitary line bundle on \(X\) restricts to a
faithful holonomy character of \(\Gamma\).

**Proof.** Put \(N=|\Gamma|\); the asymptotic volume ratio is \(1/N\).
Choose a lift \(\tilde p\) of \(p\) in the universal cover and a
Dirichlet fundamental domain \(D\). The subset
\(D\cap B(\tilde p,R)\) projects, up to measure-zero cut loci, onto
\(B_X(p,R)\). For a finite subset \(S\) of deck transformations, let
\(a\) be the largest displacement of \(\tilde p\). The translates of
this subset have disjoint interiors and lie in \(B(\tilde p,R+a)\),
so Bishop--Gromov gives

\[
 |S|\operatorname{Vol}B_X(p,R)
     \le\operatorname{Vol}B_{\widetilde X}(\tilde p,R+a)
     \le\omega_m(R+a)^m.
\]

Letting \(R\) tend to infinity proves \(|S|\le N\). Thus the deck
group is finite of order \(d\le N\). A global flat character whose
restriction to \(\Gamma\) is faithful makes the inclusion-induced map
\(\Gamma\to\pi_1(X)\) injective. Hence \(d\ge N\) and \(d=N\).

For a finite cover the asymptotic volume ratio multiplies by its degree:
one may see this directly by taking the preimage of large balls, whose
distances from a fixed lift differ by a uniformly bounded amount because
there are finitely many deck transformations. Therefore
\(\operatorname{AVR}(\widetilde X)=d/N=1\). Equality in Bishop--Gromov
forces \(\widetilde X=\mathbb R^m\). A finite group of Euclidean
isometries fixes the average of any orbit and cannot act freely unless
it is trivial. This contradicts \(N>1\). QED.

The ALE covering facts can alternatively be obtained from
[Șuvaina, Lemmas 4.1--4.2 and Remark 4.3](https://arxiv.org/pdf/1102.2672).
The argument above displays the volume reason, not merely an appeal to
the Kähler ALE classification.

### 2.1. Application to the actual positive spinor alone

There is no smooth complete Ricci-flat ALE four-manifold with oriented
infinity \(1/n(1,-2)\), odd \(n>1\), carrying a nonzero global parallel
positive Spin-c spinor. The opposite twisted spinor need not extend.

First, flatness of the determinant is automatic. For a parallel spinor
\(\Phi\) with determinant curvature \(F_A=i\Omega\), the local
curvature identity is

\[
 \operatorname{Ric}(v)\cdot\Phi
                      =i(v\mathbin{\lrcorner}\Omega)\cdot\Phi.
                                                        \tag{2.1}
\]

See [Moroianu, Lemma 3.1](https://moroianu.perso.math.cnrs.fr/tex/1997cmp.pdf).
For Ricci-flat metrics the right side vanishes. Clifford multiplication
by a nonzero real covector is invertible, and \(\Phi\ne0\); hence
\(\Omega=0\).

At infinity the parallel spinor gives an invariant vector of the limiting
positive representation. In the stated marking the canonical positive
weights are \((1,\zeta^{-1})\). A character twist permits an invariant
vector only for twists \(1\) and \(\zeta\); its determinant character
is respectively \(\zeta^{-1}\) and \(\zeta\). Both are faithful. The
proposition applies. A Ricci-flat Kähler ALE metric in this orientation
has such a parallel canonical Spin-c spinor, so it is excluded as well.
For trivial infinity group, Bishop--Gromov already gives flat Euclidean
space.

This deduction removes the first-order expansion, first-order curvature
energy, same-scale derivative bound, and global parallel-frame premises
from this particular resonant-filling exclusion. It still requires a
**genuine smooth complete ALE limit** and a positive spinor that extends
parallel over that same limit. Neither follows just by inspecting an
exterior annulus.

An independent consequence of Section 1 is the nonexistence of any smooth
Ricci-flat anti-self-dual ALE filling of this oriented cone, even without
spinor data. This agrees with, but does not require, the Ricci-flat Kähler
classification: its nontrivial cyclic types have
\(N=dk^2\), \(q=dkm-1\), whose determinant character has order \(k\),
not the order \(N\) demanded by \(q=-2\).

## 3. An integral lower-Ricci bridge in an elliptic class

There is a second way to extend the endpoint theorem. Here the additional
information is an elliptic equation for Ricci, not a marked core. The
statement is not a claim that arbitrary small integral Ricci error has
the following regularity.

Fix \(p>2\), \(r_0\in(0,1]\), \(A,L<\infty\), and \(\Lambda_0\).
Define the negative part of the least Ricci eigenvalue by

\[
 \rho_-(x)=\max\{0,-\lambda_{\min}(\operatorname{Ric}^{\sharp}(x))\},
 \qquad k_p(r)=r^2\sup_x
                  \left(\fint_{B_r(x)}\rho_-^p\right)^{1/p}.
                                                        \tag{3.1}
\]

There is \(\delta_p>0\) such that the hypotheses

\[
 |\nabla^*\nabla\operatorname{Ric}|
              \le A|\operatorname{Rm}|\,|\operatorname{Ric}|,
 \quad k_p(r_0)\le\delta_p,
 \quad |\omega|\le L,
 \quad 8\pi^2\chi/V\le\Lambda_0                       \tag{3.2}
\]

on a closed connected smooth oriented four-manifold imply

\[
                  \boxed{\fint_M Z_t\ge c(p,r_0,A,L,\Lambda_0)>0,}
                  \qquad 0\le t\le1/4.             \tag{3.3}
\]

In this section \(|\operatorname{Rm}|\) is the full four-index tensor
norm. No diameter, pointwise Ricci, or noncollapse bound is assumed.
Both the elliptic condition and the **small** normalized local lower-Ricci
budget in (3.2) are genuine inputs.

### 3.1. The normalized local estimate

[Dai--Wei--Zhang, Theorem 1.1, Corollary 1.5, and (2.5)--(2.6)](https://web.math.ucsb.edu/~wei/paper/Dai-Wei-Zhang.pdf)
give, after choosing \(\delta_p\) small enough and rescaling,

\[
 \frac{\operatorname{Vol}B_a(x)}{\operatorname{Vol}B_b(x)}
                 \ge\frac12(a/b)^4,
                 \qquad 0<a\le b\le r_0.           \tag{3.4}
\]

The propagation to every smaller scale uses their (2.6); decrease the
initial threshold by the factor needed there. In particular

\[
 \operatorname{Vol}B_r\le2\omega_4r^4,
 \qquad \operatorname{Vol}B_{2r}\le32\operatorname{Vol}B_r.
                                                        \tag{3.5}
\]

When \(2r\le r_0\) and \(B_{2r}(x)\) is proper, apply their Dirichlet
Sobolev estimate at reference scale \(2r\), to \(|f|^3\), and then use
Cauchy--Schwarz. It yields

\[
 \left(\fint_{B_r}|f|^4\right)^{1/2}
            \le S(p)r^2\fint_{B_r}|\nabla f|^2,
                         \qquad f\in C_c^\infty(B_r).           \tag{3.6}
\]

This is a normalized Sobolev estimate. No uniformly bounded
unnormalized Sobolev constant has been introduced.

Under (3.2)'s elliptic inequality, (3.6) implies the following local
lemma, for constants \(e_0,C_R>0\) depending only on \(p,A\):

\[
 r^4\fint_{B_r}|\operatorname{Rm}|^2\le e_0
 \quad\Longrightarrow\quad
 \sup_{B_{r/8}}|\operatorname{Ric}|
                  \le C_R\left(\fint_{B_r}|\operatorname{Ric}|^2\right)^{1/2}.
                                                        \tag{3.7}
\]

Here are the normalization and proof, rather than an invocation of a
collapsed harmonic-radius theorem. Work with \(h=r^{-2}g\) and the
probability measure \(d\nu=dV_g/\operatorname{Vol}_g(B_r)\). A constant
multiple of Riemannian measure preserves integration by parts. With
\(U=\operatorname{Ric}_h\), \(B=\operatorname{Rm}_h\), all norms below
use this same measure on nested subballs of \(B_1^h\). The rescaled
Sobolev inequality is \(\|f\|_4^2\le S\|\nabla_hf\|_2^2\).

Kato's inequality, the tensor energy identity, and a cutoff yield

\[
 \|U\|_{4;B_{3/4}}^2+\|\nabla U\|_{2;B_{3/4}}^2
                              \le C\|U\|_{2;B_1}^2,             \tag{3.8}
\]

after absorbing \(C\|B\|_2\|\phi U\|_4^2\). Next use the universal
curvature identity \(\Delta B=\mathcal L(\nabla^2U)+B*B\). One
integration by parts and Young's inequality give

\[
 \int\psi^2|\nabla B|^2\le
 C\int(|\nabla\psi|^2|B|^2+\psi^2|\nabla U|^2)
                                      +C\int\psi^2|B|^3.
\]

Sobolev and (3.8) absorb the cubic term, because
\(\int\psi^2|B|^3\le\|B\|_2\|\psi B\|_4^2\). Thus

\[
                         \|B\|_{4;B_{1/2}}^2\le C\|B\|_{2;B_1}^2.
                                                        \tag{3.9}
\]

Finally \(u=|U|\) obeys \(\Delta u\ge-A|B|u\), where here
\(\Delta=\operatorname{tr}\nabla^2\) has nonpositive spectrum.
For the Moser test function \(v=\psi u^{m/2}\),

\[
 \int|B|v^2\le\|B\|_4\|v\|_{8/3}^2
                   \le\|B\|_4\|v\|_2\|v\|_4.
\]

Young's inequality and (3.6) give, on nested balls,
\(\|u\|_{2m,B_a}\le[C\{m^4+m^2(b-a)^{-2}\}]^{1/m}
\|u\|_{m,B_b}\). Iteration proves (3.7). These are the early
integration-by-parts estimates of
[Tian--Viaclovsky, Section 3, Lemmas 3.2--3.5](https://arxiv.org/pdf/math/0310302),
written with the normalized measure; no later volume-comparison premise
from that paper is being transplanted.

### 3.2. Euler density selects enough good centers

Assume \(z\le1\), since otherwise (3.3) is immediate. Then

\[
 \fint|\operatorname{Ric}|^2\le10,\qquad
 \fint|\operatorname{Rm}|^2
       =32\pi^2\chi/V+4\fint|\operatorname{Ric}^{\circ}|^2
       \le H:=4(1+\max\{\Lambda_0,0\}).             \tag{3.10}
\]

For any nonnegative \(F\), doubling and Fubini imply

\[
                     \fint_M\fint_{B_r(x)}F\le32\fint_M F.      \tag{3.11}
\]

Indeed, if \(x\in B_r(y)\), then
\(\operatorname{Vol}B_r(y)\le\operatorname{Vol}B_{2r}(x)
\le32\operatorname{Vol}B_r(x)\).

Decrease \(e_0\le1\) so that \(2\omega_4e_0\) is below the
Cheeger--Tian local covering energy threshold for dimensionless Ricci
bound \(C_R+1\), allowing for the fixed norm conversion. Choose

\[
 R=\min\{r_0/64,1,(e_0/(2^{20}H))^{1/4}\}.           \tag{3.12}
\]

If \(D=\operatorname{diam}M\ge8R\), all \(B_{2R}(x)\) are proper.
At least half the centers satisfy
\(R^4\fint_{B_R(x)}|\operatorname{Rm}|^2\le e_0\), by (3.10)--(3.11).
On each such center (3.7) gives a pointwise Ricci bound
\(C_R\sqrt{e_0}R^{-2}\) on \(B_{R/8}\), while (3.5) gives
\(\int_{B_R}|\operatorname{Rm}|^2\le2\omega_4e_0\).

Apply the original bounded-Ricci local covering result of
Cheeger--Tian on the buffered ball \(B_{R/16}\), exactly as verified
in [I45, Section 3](20260927_local_geometry_and_variational_extrema.md).
This gives fixed-size uniformly regular covering charts over a positive
volume fraction of centers. I45's local coercivity for \(Z_t\) and its
Liouville-measure averaging now give (3.3). Radial Jacobian comparison
is used only inside these good neighborhoods, where Ricci has just been
bounded; extension of a nonnegative angular integral to all centers
does not require a global Ricci bound.

If \(D<8R\), set \(u=D/16\). Every \(B_{2u}(x)\) is proper and
\(B_{2D}(x)=M\). Since \(2D<r_0\), (3.4) gives
\(\operatorname{Vol}B_u(x)\ge V/(2\cdot32^4)\). Therefore every center
satisfies

\[
 u^4\fint_{B_u(x)}|\operatorname{Rm}|^2
              \le32D^4H\le2^{17}R^4H\le e_0/8.
\]

By (3.7) and (3.10),
\(|\operatorname{Ric}|(x)\le C_R\sqrt{20\cdot32^4}\) everywhere.
I45 now applies directly, with a bound independent of the small
diameter. This completes the proof of (3.3).

### 3.3. Actual and variational interfaces

The actual form supply gives \(\int Z_{1/\beta}\le C\eta V\), hence
(3.3) yields the uniform actual endpoint gap for all \(\beta\ge4\)
under (3.2). The earlier small-defect identity that makes \(V\) comparable
to \(T_+\) is purely algebraic, so a bounded \(\chi/T_+\) may replace
the Euler-density premise here as well.

For a constant-scalar-curvature critical point of
\(Q_\tau=\int|\operatorname{Ric}|^2+\tau\int s^2\), the equation is

\[
 \Delta\operatorname{Ric}
 =-2\operatorname{Rm}(\operatorname{Ric})
   -2\tau s\operatorname{Ric}
                   +\tfrac12(|\operatorname{Ric}|^2+\tau s^2)g.
                                                        \tag{3.13}
\]

Thus (3.2)'s elliptic inequality holds with \(A\le C(1+|\tau|)\).
See [Catino, Proposition 2.1](https://arxiv.org/abs/1404.0569).
The sharp-functional parameter \(\tau=-1/(4-\alpha)\) for
\(0\le\alpha<1\) lies in a fixed bounded interval. This establishes
an actual connection with the extremal problem, not an extra PDE
silently imposed on arbitrary near-Einstein metrics. A Yamabe
representative only has constant scalar curvature; it need not satisfy
(3.13), and a minimizing sequence need not be a critical sequence.

The small local quantity \(k_p(r_0)\) is not supplied by the global
\(L^2\) defect. Indeed, the comparison theorem itself requires
smallness, not merely a finite bound; Dai--Wei--Zhang's Remark 1.2
explicitly records this distinction. For an elliptic actual endpoint
sequence escaping (3.3), for every fixed \(p>2\) and \(0<r\le1\),

\[
                         \liminf_j k_p^{g_j}(r)\ge\delta_p.      \tag{3.14}
\]

A diagonal subsequence therefore has radii \(r_j\downarrow0\) and
centers \(x_j\) with
\(r_j^{2p}\fint_{B_{r_j}(x_j)}\rho_{-,j}^p
\ge(\delta_p/2)^p\). This is normalized local Ricci concentration,
not an unnormalized energy atom or an automatically existing ALE bubble.

## 4. Actual spinor remainders and concentration of smooth extrema

This section concerns the remaining **coefficient**, not the already
settled linear order. All metrics here have constant scalar curvature
\(s=-4\). Ordinary SW solvability is required for the one solution used
below. It follows from the project's conformal-weight supply by taking
weight 1; no comparison of two different solutions is made.

### 4.1. An exact nonnegative decomposition at the ordinary solution

Let \(D_{\mathcal A}\Phi=0\), \(-iF_{\mathcal A}^+=\sigma(\Phi)\),
with \(|\sigma(\Phi)|^2=|\Phi|^4/8\). Put \(\rho=|\Phi|^2\),
\(x=\rho/4\), \(\omega=\sigma(\Phi)\), and
\(\gamma=\operatorname{Im}\langle\Phi,\nabla_{\mathcal A}\Phi\rangle\).
The maximum principle gives \(0\le x\le1\). Define

\[
 \begin{split}
 K&=\int|\nabla_{\mathcal A}\Phi|^2,&Q&=\int(4-\rho)^2,\\
 \Gamma&=\int(|d\rho|^2/4+|\gamma|^2),&
 J&=\|F_{\mathcal A}^+-(F_{\mathcal A}^+)_H\|_2^2,\\
 W_0&=\tfrac12(|\omega|^2I/3-\omega\otimes\omega),&
 F&=\int|W^+-W_0|^2,\\
 H&=\tfrac23\int(1-x)^2(2+4x-x^2).&&
 \end{split}                                                   \tag{4.1}
\]

The harmonic projection uses the same curvature/Chern sign as the
solution; its squared norm is \(4\pi^2p\). For
\(D=D_2=24V+18\int|W^+|^2-72\pi^2p\), one has the exact identity

\[
                  \boxed{D/18=F+\Gamma/2+J+H.}                  \tag{4.2}
\]

In particular \(F,J\le D/18\), \(\Gamma\le D/9\), and
\(Q\le2D/3\). This is a retention of the remainders at one actual
ordinary solution, not a new nonvanishing theorem. The underlying
equations and Weitzenböck conventions are those of
[LeBrun, equations (5)--(7)](https://arxiv.org/pdf/math/0003068).

For completeness, the Hopf differential and Dirac equation give

\[
 |\nabla\omega|^2=\frac\rho2|\nabla_{\mathcal A}\Phi|^2
                                      -\frac12|\gamma|^2,
 \qquad |d\omega|^2=|\gamma|^2/4.                  \tag{4.3}
\]

These factors can be checked in the Clifford frame
\(C_1=I\), \(C_2=\operatorname{diag}(i,-i)\),
\(C_3=((0,1),(-1,0))\), \(C_4=((0,-i),(-i,0))\).
At \(\Phi=\sqrt\rho\,e_1\), write
\(\nabla_i\Phi=(u_i+iv_i,w_i+iz_i)\). Differentiating in the self-dual
basis \((e^{12}+e^{34},e^{13}-e^{24},e^{14}+e^{23})\) gives
\(\nabla_i\omega=(\sqrt\rho/2)(u_i\Sigma_1+z_i\Sigma_2-w_i\Sigma_3)\).
The two Dirac equations give \(d^*\omega=-\gamma/2\), with an
irrelevant simultaneous sign change if the opposite curvature convention
is used. The squared statements extend across zeros polynomially.

Pair the scalar spinor equation with \(\rho\) and integrate to obtain

\[
 2\int|d\rho|^2+4\int\rho|\nabla_{\mathcal A}\Phi|^2
                              =\int(4-\rho)\rho^2.
\]

Thus, writing \(T_\omega=\int(|\nabla\omega|^2-2|d\omega|^2)\),

\[
 T_\omega=8\int x^2(1-x)-\Gamma,
 \qquad
 F=\int|W^+|^2+\tfrac23\int x^4+T_\omega/2-\tfrac43\int x^2.
                                                        \tag{4.4}
\]

Also \(J=2\int x^2-4\pi^2p\). Substitution reduces (4.2) to
\((1-x)^2(2+4x-x^2)=2-7x^2+6x^3-x^4\). Finally
\(Q/12\le H\le5Q/24\), proving the stated inequalities.

### 4.2. The exact critical equation and Cotton identity

Write \(Z=\operatorname{Ric}^{\circ}\), \(P=\int|Z|^2>0\), and
\(\alpha=\mathcal E(g)=4P/(P+4V)\). Set

\[
 \tau_*=-1/(4-\alpha),\qquad
 b=\alpha/(4-\alpha)=P/(4V),\qquad q=1/3-2b.
\]

Here \(\Delta=\operatorname{tr}\nabla^2\) has nonpositive spectrum;
this is the opposite sign to the positive Laplacian used for the earlier
conformal variation. Use \(R_{ikjl}g^{kl}=\operatorname{Ric}_{ij}\),
\(\sec(e_i,e_j)=R_{ijij}\). The genuine \(L^2\) metric gradient of
\(Q_{\tau_*}\), holding its parameter fixed while varying the metric, is

\[
 \mathcal G=-\Delta Z-2\operatorname{Rm}(Z)-2bZ
                                      +\tfrac12|Z|^2g.          \tag{4.5}
\]

This follows from the classical first variation (3.13). In particular,
a smooth attained positive minimum of \(\mathcal E\) has \(\mathcal G=0\)
by the preceding variational reduction. Formula (4.5) itself is valid
without stationarity.

Define the Ricci-normalized Cotton tensor by
\(C_{ijk}=\nabla_kZ_{ij}-\nabla_jZ_{ik}\), with its full ordered
tensor norm; it is not divided by a Schouten factor. Integration by
parts, using \(\operatorname{div}Z=0\), gives

\[
 \tfrac12\int|C|^2
   =\int\langle\mathcal G,Z\rangle
     +\int\sum_{i<j}(\lambda_i+\lambda_j)^2\sec_{ij}+2bP,       \tag{4.6}
\]

where \(\lambda_i\) are the eigenvalues of \(Z\). Indeed the usual
Cotton identity is
\(\int|\nabla Z|^2-\tfrac12\int|C|^2
=\int(\operatorname{Rm}(Z,Z)-\operatorname{tr}Z^3-s|Z|^2/4)\);
pair (4.5) with \(Z\) and use

\[
 \operatorname{Rm}(Z,Z)+\operatorname{tr}Z^3+s|Z|^2/4
                  =\sum_{i<j}(\lambda_i+\lambda_j)^2\sec_{ij}.
\]

The source formulas are
[Catino, Propositions 2.1 and 4.1](https://arxiv.org/pdf/1404.0569),
not his pinching theorem for a different parameter interval.

Define \(K^\perp(\Pi)=(\sec\Pi+\sec\Pi^\perp)/2\) and
\(k_\perp=\max_\Pi K^\perp(\Pi)\). The complementary weights in
(4.6) are equal and their total is \(2|Z|^2\). For a stationary metric,
for every \(k>b\),

\[
 \int(k_\perp+k)_+|Z|^2
                  \ge(k-b)P+\tfrac14\int|C|^2.                 \tag{4.7}
\]

In particular a positive smooth extremizer cannot have
\(k_\perp<-b\) everywhere. No strict conclusion at the equality
threshold is inferred without additional information about Cotton.

### 4.3. Joint use of the actual field and the full variational equation

Let \(w_3^\pm\) be the largest Weyl eigenvalues. Decomposition into a
unit self-dual and anti-self-dual form, followed by complementary-plane
averaging, cancels the Ricci off-diagonal block and gives

\[
 k_\perp=-1/3+(w_3^++w_3^-)/2.
\]

Set \(\xi=(w_3^++w_3^--1/3)_+\). Equations (4.6)--(4.7) imply

\[
 qP+\tfrac12\int|C|^2
             \le\int\langle\mathcal G,Z\rangle+\int\xi|Z|^2.
                                                        \tag{4.8}
\]

The top eigenvalue of the actual \(W_0\) is \(x^2/3\le1/3\).
For a traceless symmetric three-by-three matrix,
\(\lambda_{\max}\le\sqrt{2/3}|\cdot|\). Therefore

\[
 \int\xi^2\le\tfrac89(F+3B)
            \le\tfrac89(D/18+3B),\qquad B=\int|W^-|^2,          \tag{4.9}
\]

using \((a+b)^2\le(4/3)(a^2+3b^2)\). The weighting matters here.
Assume the actual budget \(p\ge A>0\), \(T_+=A(1-h)\), and write
\(u_-=3T_-/A\), \(z_a=p/A-1\), \(e=R/(8\pi^2A)\). Chern--Weil
gives the exact identities

\[
 D/18=2\pi^2A(e-1-h-2z_a),\qquad
 B=P/3+(2\pi^2A/3)(u_--e).
\]

Consequently

\[
 \boxed{\mathcal H:=D/18+3B
             =P+2\pi^2A(u_--1-h-2z_a).}             \tag{4.10}
\]

Only when \(T_-\le T_+\) is \(u_-\) the earlier two-sided \(U\).
This holds eventually on the balanced small-h family; it is not assumed
for arbitrary orientations.

For a stationary metric with \(0<\alpha<4/7\), \(q>0\) and (4.8)
forces \(\mathcal H>0\). Hölder and (4.9) prove

\[
 \boxed{\int|Z|^4\ge\frac98q^2\frac{P^2}{\mathcal H},
 \qquad \|Z\|_\infty^2\ge\frac98q^2\frac P{\mathcal H}.}       \tag{4.11}
\]

More generally, without assuming stationarity, one has

\[
 \boxed{
 \frac{\|\mathcal G\|_2}{\sqrt P}
       +\sqrt{\frac{8\mathcal H}{9P}}\,\|Z\|_\infty
               \ge q+\frac{\int|C|^2}{2P}.}         \tag{4.12}
\]

One may replace \(\|Z\|_\infty\) by
\((\int|Z|^4/P)^{1/2}\). This is obtained directly from (4.8) by
Cauchy--Schwarz; it remains valid when \(\mathcal H=0\).

### 4.4. Explicit consequence on the realized balanced family

Use the same actual family as I38--I41, with
\(h_j\to0\) and \(U_j=F(h_j)+o(h_j^2)=1+h_j+O(h_j^2)\).
For any scalar \(-4\) competitor satisfying
\(0<\alpha_j=\mathcal E(g_j)\le4h_j/(1+h_j)\), the existing actual
linear theorem and \(e_j\ge1+h_j\) give \(P_j\ge cA_jh_j\).
Also \(b_j\le h_j\), and the favorable sign of \(z_a\ge0\) in (4.10)
gives \(\mathcal H_j/P_j\le1+O(h_j)\).

Thus if these competitors are stationary, in particular if they are
smooth attained minima,

\[
 \boxed{
 \liminf_j\frac{\int|\operatorname{Ric}^{\circ}_{g_j}|^4}{P_j}\ge\frac18,
 \qquad
 \liminf_j\|\operatorname{Ric}^{\circ}_{g_j}\|_{\infty,\rm HS}^2\ge\frac18.}
                                                        \tag{4.13}
\]

Since \(s=-4\), \(\operatorname{Ric}+g=Z\), and four-dimensional
Hilbert--Schmidt norm is at most twice the spectral norm. Consequently

\[
                         \liminf_j\delta_-(g_j)\ge\frac1{4\sqrt2}.
                                                        \tag{4.14}
\]

If instead these scalar \(-4\) competitors have \(\delta_-(g_j)\to0\),
then (4.12) forces the explicit variational residual

\[
                   \boxed{\liminf_j
                       \|\mathcal G_j\|_2/\sqrt{P_j}\ge1/3.}   \tag{4.15}
\]

They cannot be relatively almost critical for this quadratic-curvature
problem. This is an unrestricted metric variation, not a variation confined
to constant-scalar metrics. With \(R=\int|\operatorname{Ric}|^2\) and
\(S_2=\int s^2\), the scalar-variance term has zero first variation at a
constant-scalar metric. Hence
\(\nabla\mathcal E=\nabla\mathcal J=(S_2/R^2)\mathcal G
=((4-\alpha)/R)\mathcal G\). In computing \(\mathcal G\), the
parameter \(\tau\) is selected at the metric and then held fixed;
differentiating \(\tau(g)\) inside \(Q_{\tau(g)}(g)\) would instead
differentiate an identically zero expression.

No existence of either sequence is asserted. These conclusions
do not prove nonattainment, determine the all-metric coefficient, or
apply to general nonconstant-scalar input after an uncontrolled conformal
change. They identify an actual obstruction to treating weak integral
minimization as a uniformly pointwise near-Einstein deformation problem.

### 4.5. The signed term still needed for coefficient four

The ordinary solution also makes the unclosed estimate explicit. Define
\(L_0=2H-Q/8=(2/3)\int(1-x)^2(1+8x-2x^2)\ge0\).
Retaining \(\Sigma=8K+Q+8J\) and using (4.2) gives

\[
 \boxed{P-8\pi^2Ah
        =2[2F+\Gamma+J+L_0+4\pi^2(p-A)-K].}          \tag{4.16}
\]

The same actual solution supplies every term. Its only negative payment
on the right is the spinor gradient energy \(K\); nonnegative losses
must not be discarded before asking whether they compensate it.
On \(V-2\pi^2A=O(Ah)\), the estimate
\([K-\Gamma-J-L_0-4\pi^2(p-A)]_+=o(Ah)\) would suffice for leading
coefficient four, even if the earlier unsigned directional cost is only
\(O(Ah)\). This estimate is **not** proved here. Equations (4.13)--(4.15)
give information about extremal geometry instead of pretending that the
remaining signed balance has already closed.

## 5. What this closes, and what still requires mathematics

The preceding local annulus theorem has two actual exceptional lifts.
Neither lift has been discarded. The new distinction is that both solve
the local field equations while their **entire smooth filling** must pay
the curvature cost (1.7). This is stronger than ruling out one proposed
first-order correction, and applies to arbitrary topology inside a core
with the specified outer collar.

It does not yet supply a decomposition of every weak-error sequence into
such cores. Hyperkähler-type, nonresonant annuli are still governed by the
actual-field estimates, not by (1.2); reversing orientations is prohibited.
No conclusion about all Einstein metrics on the fixed Dehn-twist manifold
is inferred here. The balanced family's sharp coefficient and the pure
integral-Ricci endpoint remain separate problems.

The elliptic bridge in Section 3 replaces pointwise Ricci control by a
specific curvature equation and a small local normalized lower-Ricci
budget. It does not hide these additional hypotheses inside an admissibility
definition. Section 4 keeps the ordinary actual solution's full remainders,
then links them to the variational equation: small total defect does not
make a smooth low-energy extremum uniformly pointwise near Einstein.

The next sufficient statements are now precise: obtain the marked complete
core structure from weaker original inputs, or estimate the signed ordinary
spinor balance in (4.16). Neither requires redoing linear sharpness or
repeating the local holonomy classification. The proof above does not assume
either missing statement.
