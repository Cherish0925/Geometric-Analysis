# Technical supplement: actual topology, gauge supply, and earlier field equations

Research snapshot: 844e62f7304d9f890914a6a4370ec39291ddc26e.

Complete inputs and comparisons. The old quadratic lower bound and concentration-only status have since been strengthened by I40/I41. Pin-minus invariant-weight solvability is retained in its own scope.

Read 00_READ_FIRST.md for superseded statements. Each source below is complete and byte-preserved. Original local links remain relative to their source; locate other texts using Volume 6. Formula numbers restart in each source.


---

## Source 1: line1_two_chirality_topology.md

Original path: mathematics/current/line1_two_chirality_topology.md

SHA-256: 91eb14bc07220c6d66e2b97af97501d324bc1dad999ba7b9d2f41368217fa5a6

BEGIN COMPLETE SOURCE

# From the energy envelope to a two-chirality topological gap

23 September 2026. This note composes the existing functional-pencil
theorem with both Chern--Weil identities. Its new application is a uniform
integral Einstein obstruction on a realized family of mixed blow-ups and
handle additions lying away from the previously recorded one-third
critical band. All statements depend on the analytic theorem in
[the functional-pencil manuscript](line1_functional_pencil.md), through
[the energy-envelope theorem](line1_energy_envelope_gap.md).
The elementary Chern--Weil calculation is classical. No independent
literature-priority certification is claimed for this composition.

## 1. An upper bound that applies to every candidate

Let
\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}\#m(S^1\times S^3),\qquad
 A=c_1^2(X)>0,\quad h=\frac{k+4m}{A}\in(0,1/3),
 \tag{1}
\]
where \(X\) is a minimal complex surface of general type. Write
\[
 T_\pm=2\chi(M)\pm3\tau(M),\qquad
 U=\frac{3\min(T_+,T_-)}{A}
   =\frac{3(2\chi(M)-3|\tau(M)|)}{A},
\]
\[
 R=\int_M|\operatorname{Ric}|^2,\quad
 P=\int_M|\operatorname{Ric}^{\circ}|^2,\quad
 e=\frac{R}{8\pi^2A},\quad
 F(h)=\frac{(4-\sqrt{1-3h})^2}{9}.
 \tag{2}
\]
The Ricci norms are tensor norms; Weyl norms are Hilbert--Schmidt
endomorphism norms on two-forms. Set
\[
 \mathcal E(g)=\inf_{\lambda\ne0}
 \frac{\int|\operatorname{Ric}-\lambda g|^2}
      {\lambda^2\operatorname{Vol}(g)}.
 \tag{3}
\]
The scalar monopole estimate makes \(R>0\). Direct minimization, with
\(I=\int s\) and \(V=\operatorname{Vol}(g)\), gives
\[
 \mathcal E=4-\frac{I^2}{RV}\ge\frac{4P}{R}.
 \tag{4}
\]
For \(I=0\), the value four is an infimum as \(|\lambda|\to\infty\);
the same formula remains valid. The inequality uses
\(I^2/V\le\int s^2=4(R-P)\), not a sign assumption on \(s\).

The two Chern--Weil formulas give, separately for either sign,
\[
 \int|W^\pm|^2=2\pi^2T_\pm-\frac{R}{12}+\frac P3\ge0.
\]
Consequently
\[
 e\le U+\frac{4P}{8\pi^2A}\le U+e\mathcal E,
 \qquad\boxed{e(1-\mathcal E)\le U.}
 \tag{5}
\]
For Einstein metrics, this is the genuine upper bound \(e\le U\).
It controls all candidates, regardless of their proximity to a preferred
construction or variational minimum. No energy infimum has been used as
an upper bound. No monopole structure in the opposite orientation is
assumed: only the nonnegativity of its Weyl energy is used.

## 2. A uniform topological inequality for all smooth metrics

**Theorem 1.** There is a universal \(c>0\) such that every metric on
every manifold (1) satisfies
\[
 \boxed{\mathcal E(g)+(U-F(h))_+\ge c h^2.}
 \tag{6}
\]
One may take \(c=\varepsilon/7\), where
\(0<\varepsilon\le1\) is the constant in the energy-envelope theorem
\[
 \mathcal E(g)+(e-F(h))_+\ge\varepsilon h^2.
 \tag{7}
\]
The same argument works in the abstract actual-class setting of that
theorem: \(T_+=A(1-h)\), and for every metric an actual conformally
solvable Spin\(^c\) structure has \((a_g^+)^2\ge A\) and
\(a_g^2\ge T_+\).

**Proof.** Since \(T_+/A=1-h\), one has \(U\le3\).
If \(\mathcal E\ge1/2\), (6) is immediate because
\(c h^2\le1/63\). If \(\mathcal E<1/2\), (5) forces \(U>0\) and
\[
 e\le\frac{U}{1-\mathcal E}
 \le U+2U\mathcal E\le U+6\mathcal E.
\]
Hence
\[
 (e-F(h))_+\le(U-F(h))_++6\mathcal E.
\]
Substitute this into (7) and use
\(7\mathcal E+(U-F)_+\le7[\mathcal E+(U-F)_+]\).
This proves (6), including \(U\le0\) through the first case. \(\square\)

**Corollary 2.** If
\[
 U\le F(h)+\frac c2 h^2,
 \tag{8}
\]
then every smooth metric satisfies
\[
 \mathcal E(g)\ge\frac c2 h^2.
 \tag{9}
\]
There are no Einstein metrics of any sign on this manifold. Nonzero
Einstein constants would give \(\mathcal E=0\). For the zero constant,
the signed scalar monopole inequality
\(\int s_-^2\ge32\pi^2A>0\) excludes Ricci-flatness separately.
For either normalized pointwise branch,
\[
 \delta_\sigma(g)=\|g^{-1}\operatorname{Ric}-\sigma I\|_{\infty,\mathrm{op}},
 \qquad\sigma\in\{-1,1\},
\]
one has \(\mathcal E\le4\delta_\sigma^2\). Thus
\[
 \boxed{\delta_\sigma(g)\ge h\sqrt{c/8}.}
 \tag{10}
\]
This is an obstruction to both pointwise inputs on these types, not a
Yau26 counterexample.

The previously obtained family-uniform theorem used only
\(T_+/A=1-h\). Formula (6) adds the independent opposite-chirality
budget \(T_-\). When \(T_-\) is large it yields no new restriction;
the mixed examples below have a small enough \(T_-\) for it to matter.

## 3. Realized mixed ball-quotient examples outside the old band

Choose any compact smooth complex-hyperbolic surface \(X_0\), with
complex orientation, and a sequence of connected finite unramified
covers \(X_j\to X_0\) of unbounded degree. Such a sequence exists:
the cocompact lattice is an infinite finitely generated linear group
in characteristic zero (use its faithful adjoint representation), hence
is residually finite. A finitely generated residually finite infinite
group has finite-index subgroups of unbounded index. Otherwise it has
only finitely many finite-index subgroups, their intersection is
finite-index, and residual finiteness makes that intersection trivial,
forcing the group to be finite. All covers remain compact complex
hyperbolic and minimal of general type.

Put \(A_j=c_1^2(X_j)\to\infty\). The Chern numbers are
\[
 \chi(X_j)=A_j/3,\qquad \tau(X_j)=A_j/9.
\]
Define integers
\[
 k_j=\left\lfloor\frac{29 A_j}{2025}\right\rfloor,
 \qquad
 m_j=\left\lfloor\frac{397 A_j}{32400}\right\rfloor-2,
 \qquad
 M_j=X_j\#k_j\overline{\mathbb{CP}}^{\,2}
          \#m_j(S^1\times S^3).
 \tag{11}
\]
For sufficiently large \(j\), both integers are positive. No prescribed
divisibility of the cover degree or \(A_j\) is needed.

Let
\[
 h_0=\frac{19}{300},\quad x_0=\frac{29}{2025},\quad
 z_0=\frac{397}{32400},\quad F_0=F(h_0)=\frac{961}{900}.
\]
Then \(x_0+4z_0=h_0\), and
\[
 1+15x_0-12z_0=F_0.
 \tag{12}
\]
Write \(k_j=x_0A_j-\alpha_j\) and
\(m_j=z_0A_j-\beta_j-2\), where
\(0\le\alpha_j,\beta_j<1\). Consequently
\[
 h_j=h_0-\frac{\alpha_j+4\beta_j+8}{A_j},
\]
\[
 \frac{3T_-(M_j)}{A_j}
 =1+\frac{15k_j-12m_j}{A_j}
 =F_0+\frac{-15\alpha_j+12\beta_j+24}{A_j}.
 \tag{13}
\]
The signature is positive, since
\(\tau(M_j)/A_j=1/9-k_j/A_j\ge1/9-x_0>0\).
Thus the second expression in (13) is exactly \(U_j\).
Moreover
\[
 F'(h)=\frac{4-\sqrt{1-3h}}{3\sqrt{1-3h}},
 \qquad 0<F'(h)\le\frac{31}{27}<2
 \quad(0\le h\le h_0).
\]
For large \(j\), therefore,
\[
 0<h_j<h_0,\qquad
 \boxed{0<U_j-F(h_j)<\frac{62}{A_j}.}
 \tag{14}
\]
Indeed, the second correction in (13) lies strictly between \(9/A_j\)
and \(36/A_j\), and \(0<F_0-F(h_j)<26/A_j\).

Since \(h_j\to h_0>0\), (14) eventually implies (8). We have proved:

**Theorem 3.** The realized sequence (11), for every sufficiently large
\(j\), satisfies
\[
 \boxed{\inf_{g\in\operatorname{Met}(M_j)}\mathcal E(g)
       \ge\frac{c h_0^2}{8}>0.}
 \tag{15}
\]
In particular, none of these smooth manifolds carries any Einstein
metric. For every smooth metric on every sufficiently large member,
\[
 \delta_\sigma(g)\ge h_0\sqrt{c/32},\qquad \sigma=\pm1.
 \tag{16}
\]
The threshold index depends on the universal analytic constant and the
chosen cover sequence; no explicit numerical lower bound for that
constant is claimed. The manifolds have unbounded Euler characteristic,
so an infinite subsequence consists of pairwise distinct smooth types.

### Actual gauge input, not merely numerical Chern data

For every metric on (11), select the exceptional signs at its
polarization as in Section 2 of
[the polarized closure proof](lebrun_stability_closure.md). The actual
structure has
\[
 (a_g^+)^2\ge A_j,\qquad a_g^2=A_j-k_j\ge A_j-k_j-4m_j=T_+(M_j).
\]
Nonvanishing after handle addition includes the \(m_j\) loop insertions.
The structure is fixed throughout the conformal class; the unchanged
Hodge star on two-forms supplies the same class for every auxiliary
positive weight. This is precisely the quantifier
\(\forall g\,\exists\mathfrak s_g\,\forall f>0\)
used in the energy-envelope theorem. The classical input is LeBrun's
Proposition 3.2 and its polarized proof, not residual finiteness or the
intersection form alone. Alternatively, sufficiently high covers have
\(b_+>1\), since \(\chi(\mathcal O_{X_j})=A_j/9\to\infty\) and
\(b_+=1+2p_g\); hence these examples do not require the small-\(b_+\)
chamber extension.

## 4. Precisely which prior tests these examples pass

The following comparisons establish additional coverage relative to
the recorded first-line bounds and to the displayed classical tests.
They do not prove that every Einstein-obstruction paper has been
exhaustively searched.

1. **The recorded uniform one-third band does not detect them.**
   Its stated constant is
   \(\varepsilon_0=\min\{1/4,c_{\rm cal}/1215\}\le1/4\), whereas
   \(1/3-h_j>1/3-h_0=27/100>1/4\).
   Thus setting \(\mathcal E=0\) does not contradict that inequality.
   In particular this is not another choice of topology inside its
   stated near-one-third strip.
2. **Both strict Hitchin--Thorpe inequalities hold.**
   \(T_+/A_j\to281/300>0\) and
   \(T_-/A_j\to961/2700>0\).
3. **The classical optimized scalar--Weyl moment bounds have slack.**
   Formula (14) gives \(U_j>F(h_j)\). Choose a formal Einstein energy
   \(e_j=(U_j+F(h_j))/2\); it has positive energies for both Weyl
   halves and satisfies the scalar and all functional-pencil
   nonnegativity bounds for large \(j\). The equality case at
   \(U=F\) was already classically forbidden; the new content is the
   uniform open strip \(0<U-F\lesssim h^2\). These moment values are
   a numerical non-implication witness, not a metric construction.
4. **The degree-to-complex-hyperbolic entropy obstruction has slack.**
   Collapsing the added summands gives a degree-one map \(M_j\to X_j\).
   Kotschick's Corollary 3, equation (15), requires
   \(\chi(M_j)>\frac32|\tau(M_j)|+\frac{32}{81}\chi(X_j)\)
   for an Einstein metric. Here the left difference divided by \(A_j\)
   tends to \(F_0/6=961/5400>32/243\), so this test is satisfied
   strictly. Entropy supplies a lower-volume restriction, not the
   missing upper bound used in (5).
5. **The elementary Seiberg--Witten Miyaoka--Yau test has slack.**
   \((\chi-3\tau)(M_j)/A_j\to59/1800>0\).

The mechanism is now different from a bare improvement of the
\(T_+/A=2/3\) threshold: the actual class forces a quantitative lower
energy envelope while the opposite Weyl half supplies a topological
upper envelope. Their incompatibility eliminates every candidate
Einstein metric on the same smooth type. It simultaneously rules out
arbitrarily small normalized integral error on those types.

## Sources and reproducible scope

- [LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg--Witten Theory*,
  Proposition 3.2, Theorem 3.3 and Corollary 2.5](https://arxiv.org/html/math/0003068).
  These provide the classical polarized gauge input, the one-third
  obstruction, and the exact equality comparison.
- [Kotschick, *Entropies, volumes, and Einstein metrics*, Theorem 1 and
  Corollary 3](https://arxiv.org/html/math/0410215). The comparison above
  uses its explicitly stated complex-hyperbolic degree bound, not an
  uncomputed exact minimal entropy for the new manifolds.
- Mal'cev's residual-finiteness theorem for finitely generated linear
  groups in characteristic zero supplies the finite covers; see
  [Nica's account and proof](https://arxiv.org/abs/1306.2385).
  The unbounded-index deduction is given above.
- The nonclassical differential input remains the local
  [functional-pencil proof](line1_functional_pencil.md), with its
  [energy-envelope transfer](line1_energy_envelope_gap.md). This note
  does not replace that proof by the finite calculations below.

`check_line1_two_chirality_topology.py` verifies the Chern--Weil and
defect algebra, all rational ratios, the floor-error estimates, and
the displayed comparison margins; it rejects incorrect opposite-
orientation handle and trace-free-Ricci coefficients. It does not
certify the analytic pencil theorem, Seiberg--Witten gluing or
literature priority.


END COMPLETE SOURCE


---

## Source 2: line1_bauer_furuta_geography.md

Original path: mathematics/current/line1_bauer_furuta_geography.md

SHA-256: 1ef42b7981722b1ec8a4325e85e460cc5dda1805b64827def3c7d4afe07de3e9

BEGIN COMPLETE SOURCE

# Two-chirality integral rigidity beyond ordinary Seiberg--Witten type

23 September 2026. This note applies the existing quantitative functional
pencil to Bauer--Furuta detected connected sums. The new application is an
actual family with even positive and negative Betti numbers and no
almost-complex structure in either orientation. The differential estimate
is inherited; the actual gauge supply, geography, topology and application
are proved together below. No claim of exhaustive literature priority is made.

## 1. The analytic input and the distinct gauge category

Use tensor norms for Ricci and the Hilbert--Schmidt norm on the Weyl
endomorphism of two-forms.
For a closed connected oriented smooth four-manifold set

\[
 T_\pm=2\chi\pm3\tau,\qquad
 \mathcal E(g)=\inf_{\lambda\ne0}
 \frac{\int|\operatorname{Ric}_g-\lambda g|^2}
      {\lambda^2\operatorname{Vol}_g(M)}.
\]

The actual-class version of the existing
[two-chirality theorem](line1_two_chirality_topology.md), Section 2, says:
if there is a number \(A>0\) such that every metric admits an actual
conformally solvable Spin\(^c\) structure satisfying

\[
 (a_g^+)^2\ge A,\qquad a_g^2\ge T_+,
 \qquad h=1-T_+/A\in(0,1/3),
\]

then a universal constant \(c>0\) gives

\[
 \mathcal E(g)+(U-F(h))_+\ge ch^2,\qquad
 U=\frac{3\min(T_+,T_-)}A,
 \qquad F(h)=\frac{(4-\sqrt{1-3h})^2}{9}.
 \tag{1}
\]

The constant is independent of the number of ordinary basic classes,
the rank of cohomology, and the virtual dimension of the chosen structure.
The only nonclassical analytic premise in this note is (1), whose proof
uses the [functional-pencil theorem](line1_functional_pencil.md) and
[energy-envelope transfer](line1_energy_envelope_gap.md).

The following source theorem supplies actual structures where ordinary
Seiberg--Witten invariants vanish. For two or three simply connected
symplectic four-manifolds \(X_i\) with \(b_+(X_i)\equiv3\pmod4\), Bauer's
nonvanishing theorem gives nonzero Bauer--Furuta invariants for the
connected sum of their canonical structures. Adding a manifold with
negative-definite intersection form and determinant square \(-b_2\)
preserves this nonvanishing. Independent canonical and exceptional signs
give actual monopole classes. See Ishida--LeBrun, Theorem 9,
Corollary 8, Proposition 10 and Corollary 11 in
[*Curvature, Connected Sums, and Seiberg--Witten Theory*](https://arxiv.org/html/math/0111228).
For two or three positive summands no fourth-summand congruence is needed.

## 2. A quantitative theorem for decomposable symplectic building blocks

**Theorem 1.** Let \(r\in\{2,3\}\). Let \(X_1,\ldots,X_r\) be simply
connected symplectic four-manifolds with
\(b_+(X_i)\equiv3\pmod4\), and suppose

\[
 A=\sum_{i=1}^r c_1^2(X_i)>0.
\]

For nonnegative integers \(k,m\), put

\[
 M=\Bigl(\#_{i=1}^r X_i\Bigr)
       \# k\overline{\mathbb{CP}}^{\,2}
       \# m(S^1\times S^3),\qquad
 D=4(r-1)+k+4m,\qquad h=D/A.
 \tag{2}
\]

If \(0<h<1/3\), every smooth metric on \(M\) satisfies (1), with the
same universal constant as in the existing two-chirality theorem. In
particular, if

\[
 U\le F(h)+\frac c2h^2,
 \tag{3}
\]

then

\[
 \mathcal E(g)\ge\frac c2h^2,
 \qquad
 \|g^{-1}\operatorname{Ric}_g-\sigma I\|_{\infty,\mathrm{op}}
       \ge h\sqrt{c/8}\quad(\sigma=\pm1).
 \tag{4}
\]

Under condition (3), \(M\) has no Einstein metric of any sign.

**Proof.** Canonical classes on the symplectic summands have mod-two
Seiberg--Witten invariant one. Write \(c_i=c_1(X_i)\) and
\(\alpha=\sum_i c_i\), using the orthogonal connected-sum splitting.
The source theorem gives, for every exceptional sign choice, an actual
monopole class

\[
 a_{\epsilon}=\alpha+\sum_{j=1}^k\epsilon_jE_j,
 \qquad \epsilon_j\in\{\pm1\},\quad E_iE_j=-\delta_{ij}.
 \tag{5}
\]

Here \(\epsilon=(\epsilon_1,\ldots,\epsilon_k)\). These are first Chern
classes of specified Spin\(^c\) structures with
solutions for every metric, not merely formal characteristic vectors.
The handle factors are included in the negative-definite gluing theorem;
its proof allows a nontrivial Picard torus on that summand.

Topology and the almost-complex structure on each summand give

\[
 T_+(M)=A-4(r-1)-k-4m=A-D,
 \qquad a_{\epsilon}^2=A-k,
\]

\[
 a_{\epsilon}^2-T_+(M)=4(r-1+m)\ge0.
 \tag{6}
\]

In particular these are special classes, with actual virtual dimension
\(r-1+m\). For any metric, averaging (5) over the exceptional signs gives

\[
 2^{-k}\sum_{\epsilon}(a_{\epsilon,g}^+)^2
   =(\alpha_g^+)^2+\sum_j(E_{j,g}^+)^2
   \ge\alpha^2=A.
 \tag{7}
\]

Choose one maximizing structure. The choice can depend on the metric,
but the resulting structure solves the unperturbed equations on all
metrics and hence on every conformal metric. The same chosen class
therefore supplies every positive auxiliary weight in the analytic
theorem. Its square is positive here, since
\(k/A\le h<1/3\), so the negative-square cost is actually zero.
Equations (6)--(7) verify all inputs to (1), proving (1) and (4).

A nonzero Einstein constant makes \(\mathcal E=0\), contradicting (4).
Ricci-flatness is not a zero-defect case of this definition; instead
the actual class and (7) give the signed scalar estimate
\(\int s_-^2\ge32\pi^2A>0\), which rules it out separately. This proves
the final assertion. \(\square\)

This extension changes the source of the gauge information. Splitting
\(M\) into two pieces of positive \(b_+\) makes its ordinary
Seiberg--Witten invariants vanish by the standard connected-sum vanishing
theorem. Actual Bauer--Furuta classes persist nevertheless. Thus ordinary
basic classes on \(M\) cannot be silently substituted for (5).

## 3. Why low-signature building blocks do not realize the new strip

This is a useful selection calculation, not a general obstruction to
the connected-sum method. Write

\[
 \rho=\frac{\sum_i\tau(X_i)}A,\quad x=k/A,
 \qquad h=\frac{4(r-1)+k+4m}A.
\]

The exact opposite-orientation budget is

\[
 \frac{3T_-}A=3(1-6\rho)-3h+18x.
 \tag{8}
\]

For zero-signature building blocks and \(h<1/3\), the signature of
\(M\) is \(-k\); hence \(U=3T_+/A=3(1-h)>2\), while
\(F(h)<16/9\). They cannot approach \(U=F(h)\) in this range. This
explains why simply taking several product-like inputs does not realize
the desired two-chirality strip.

For positive signature, (8) instead shows what must change: the
building blocks need a sufficiently positive ratio \(\rho\), and handle
addition must supply enough of the surgery budget. Both are realized in
the following construction.

## 4. An actual infinite family with no almost-complex structure

Braungardt--Kotschick's geography theorem realizes every sufficiently
large lattice point strictly below any fixed slope less than nine by
simply connected minimal symplectic manifolds: Theorem 4 of
[*Einstein metrics and the number of smooth structures on a four-manifold*](https://arxiv.org/pdf/math/0306021).
Take its parameter \(\epsilon=1/20\). Consequently, for every sufficiently
large integer \(n\), choose such a manifold \(X_n\) with

\[
 \chi_h(X_n)=20n,\qquad c_1^2(X_n)=178n.
 \tag{9}
\]

Indeed \(178n\le(9-1/20)20n-c(1/20)=179n-c(1/20)\) for large \(n\).
Here \(\chi_h=(\chi+\tau)/4\) is the topological Todd number for a
symplectic manifold; no complex structure on \(X_n\) is assumed.
The two defining topological equations imply

\[
 \chi(X_n)=62n,\quad \tau(X_n)=18n,\quad
 b_+(X_n)=40n-1\equiv3\pmod4,\quad b_-(X_n)=22n-1.
 \tag{10}
\]

Take two copies of \(X_n\). Set

\[
 A_n=356n,\quad h_0=\frac{19}{300},\quad F_0=F(h_0)=\frac{961}{900},
 \quad u_0=\frac{105}{89},
\]

\[
 x_0=\frac{781}{180225},\qquad y_0=\frac{42533}{2883600}.
 \tag{11}
\]

These positive rational numbers satisfy

\[
 x_0+4y_0=h_0,\qquad u_0+15x_0-12y_0=F_0.
 \tag{12}
\]

Define the even nonnegative surgery counts, for sufficiently large \(n\),

\[
 k_n=2\left\lfloor\frac{x_0A_n}{2}\right\rfloor,
 \qquad m_n=2\left\lfloor\frac{y_0A_n}{2}\right\rfloor-4,
\]

\[
 M_n=X_n\#X_n\#k_n\overline{\mathbb{CP}}^{\,2}
                    \#m_n(S^1\times S^3).
 \tag{13}
\]

**Theorem 2 (realized Bauer--Furuta strip).** There exists \(n_0\) such
that, for every \(n\ge n_0\) and every smooth metric on \(M_n\),

\[
 \boxed{\mathcal E(g)\ge\frac{c h_0^2}{8}>0,\qquad
 \delta_\sigma(g)\ge h_0\sqrt{c/32}\quad(\sigma=\pm1).}
 \tag{14}
\]

The manifolds \(M_n\) are pairwise nonhomeomorphic, have vanishing ordinary
Seiberg--Witten invariants, and admit no almost-complex structure in either
orientation. Both strict Hitchin--Thorpe inequalities hold. Their numerical
data lie on the allowed side of the classical optimized energy envelope,
but inside its new quantitative exclusion strip for large \(n\).

**Proof.** Connected-sum topology gives

\[
 \chi(M_n)=124n-2+k_n-2m_n,\qquad \tau(M_n)=36n-k_n,
\]

\[
 T_+=A_n-4-k_n-4m_n,
 \quad T_-=140n-4+5k_n-4m_n.
 \tag{15}
\]

Write \(k_n=x_0A_n-\alpha_n\) and
\(m_n=y_0A_n-\beta_n-4\), with \(0\le\alpha_n,\beta_n<2\).
Since
\(\tau(M_n)/A_n\ge9/89-x_0=196/2025>0\), the smaller chirality is
\(T_-\). Thus, exactly,

\[
 h_n=h_0-\frac{\alpha_n+4\beta_n+12}{A_n},\qquad
 U_n=F_0+\frac{-15\alpha_n+12\beta_n+36}{A_n}.
 \tag{16}
\]

For large \(n\), \(0<h_n<h_0\). The numerator of the correction in
\(U_n\) lies strictly between 6 and 60. Also

\[
 F'(h)=\frac{4-\sqrt{1-3h}}{3\sqrt{1-3h}},\qquad
 0<F'(h)\le31/27<2\quad(0\le h\le h_0).
\]

Since \(\alpha_n+4\beta_n+12<22\), it follows that

\[
 \boxed{0<U_n-F(h_n)<\frac{104}{A_n},\qquad h_n\longrightarrow h_0.}
 \tag{17}
\]

Theorem 1 applies by (10). Choose \(n_0\) so that \(h_n\ge h_0/2\)
and \(104/A_n\le c h_0^2/8\). Then (1) implies
\(\mathcal E\ge ch_0^2/4-ch_0^2/8\), proving (14).

The Betti numbers are

\[
 b_1(M_n)=m_n,\qquad b_+(M_n)=80n-2,\qquad
 b_-(M_n)=44n-2+k_n.
 \tag{18}
\]

They are all even. An almost-complex four-manifold necessarily has
\((\chi+\tau)/4\in\mathbb Z\), equivalently
\(1-b_1+b_+\) even. Equation (18) makes this number odd. Reversing
orientation replaces \(b_+\) by the also-even \(b_-\), so the same
contradiction holds there. No almost-complex structure exists in either
orientation. The positive and negative summands in (18) also allow the
ordinary connected-sum vanishing argument in both orientations.
The second Betti number \(b_2=124n-4+k_n\) is strictly increasing,
which gives pairwise distinct homeomorphism types even without fixing
the orientation.

Finally \(T_+/A_n\to281/300>0\) and
\(T_-/A_n\to961/2700>0\), proving strict Hitchin--Thorpe. By (17), the
classical Einstein energy interval \([F(h_n),U_n]\) has positive length.
Both Weyl energies can be positive inside it. It is the quantitative
separation, not the classical scalar--Weyl numerical inequalities alone,
that eliminates this interval. \(\square\)

## 5. The precise increase in scope

1. These are not merely new choices of a complex general-type base in the
   earlier application. A Kähler surface has odd \(b_+=1+2p_g\), and
   blowups and \(S^1\times S^3\) additions preserve \(b_+\). Both \(b_+\)
   and \(b_-\) in (18) are even, so neither orientation of \(M_n\) can be
   diffeomorphic to any member of that former category.
2. Ordinary Seiberg--Witten invariants on the whole manifold vanish.
   The application genuinely uses actual classes retained by stable
   cohomotopy. It is not obtained by declaring arbitrary cohomology vectors
   to be monopoles. The virtual dimension is \(1+m_n\), not zero.
3. The previously recorded universal one-third estimate has
   \(\varepsilon_0\le1/4\), whereas
   \(1/3-h_n>1/3-h_0=27/100\). It does not itself force positive
   Einstein defect on this family. The classical connected-sum
   nonexistence threshold \(D\ge A/3\) likewise does not apply.
4. The new differential input is still the existing functional pencil.
   Bauer's nonvanishing and Braungardt--Kotschick geography are classical
   inputs. This note supplies a realized extension of the quantitative
   obstruction, not a new Bauer--Furuta theorem or new symplectic geography.
5. These manifolds cannot be Yau26 counterexamples: (14) forbids the
   required arbitrarily tight pointwise inputs. The result establishes a
   further category of no-Einstein smooth types on which the original
   pointwise hypotheses are uniformly impossible.

For large \(n\), \(\pi_1(M_n)\) is the infinite free group of rank
\(m_n\). Myers' theorem already excludes strictly positive Ricci
curvature on these objects. The positive-sign pointwise corollary is
therefore not a second independent discovery; the substantive extension
is the uniform all-metrics integral gap and its negative-sign pointwise
consequence, supplied by the actual Bauer--Furuta classes.

The threshold \(n_0\) depends on the inherited analytic constant and the
geography existence threshold. No explicit numerical value is claimed.
We choose one available \(X_n\) at each lattice point. Although the source
geography gives infinitely many smooth structures there, this note does
not assert that all remain pairwise distinct after the new connected sum.

`check_line1_bauer_furuta_geography.py` checks the exact topology, rational
parameters, parity obstruction, sign of the floor errors, and comparison
with the old recorded band. Those checks do not prove gauge nonvanishing,
the geography theorem or the inherited analytic theorem.


END COMPLETE SOURCE


---

## Source 3: round14_twisted_rigidity.md

Original path: mathematics/current/round14_twisted_rigidity.md

SHA-256: 77b52d2c7a8b3e8a9fd6a71f0109cbebcd825e34d428b1be30dffaf1bb505bc8

BEGIN COMPLETE SOURCE

# Twisted monopole extension and positive-b-plus connected sums

## 1. A larger analytic input than all-metric monopoles on a cover

The finite-cover criterion in `round14_rigidity.md` does not exhaust the
available gauge input. For its analytic proof, the cover equations only
need to be solvable for the **deck-invariant curvature weights actually
used by the proof**. Pin-minus monopoles supply exactly this input,
including on connected sums whose ordinary Seiberg--Witten invariants
vanish. The argument below checks that restriction explicitly.

**Invariant-weight lemma.** Let \((\widetilde X,\widetilde g)\) be a
closed oriented four-manifold with a finite group of orientation-preserving
isometries \(G\). Fix one ordinary spin-c structure with real Chern class
\(\widetilde a\). Suppose that for every smooth positive \(G\)-invariant
function \(f\), the weighted equations

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi)                 \tag{1.1}
\]

have a solution in this structure. Then the integral calibration theorem
of round 4 holds for \((\widetilde X,\widetilde g,\widetilde a)\),
with its original universal constant and square cost. Solutions are not
required to be invariant, and no solvability on non-invariant metrics
or for non-invariant weights is asserted.

**Proof.** There are only three kinds of weight in the full proof chain.

1. The signed scalar inequality uses \(f=1\).
2. The spectral inequality uses \(f_\epsilon=\sqrt{q_\epsilon}\), where
   \(q_\epsilon\) is a positive smooth majorant of
   \(h=(-2s/3-2\lambda_{\min}(W^+))_+\), converging uniformly to \(h\).
3. The bounded-spinor estimate uses positive smooth majorants of
   \(f_0=\max\{\sqrt{\max(-s+\sqrt6|W^+|,3)},(-s)_+/4\}\).

Both \(h\) and \(f_0\) are \(G\)-invariant. Start with any smooth
majorant converging uniformly and replace it by
\(|G|^{-1}\sum_{\gamma\in G}f\circ\gamma\). This preserves positivity,
the majorant property and uniform convergence. The square root in case 2
also remains invariant. Thus (1.1) supplies every solution invoked in
round 3, Section 6, and round 4, Sections 3--6.

All subsequent operations take place on the smooth ordinary spinor and
line bundles upstairs: Weitzenbock identities, the Hessian estimate,
the determinant-curvature identity, the polynomial Weyl tensor and its
weak Bianchi self-test. They impose no equivariance condition on the
spinor or test tensor. The measurable lowest-eigenline projector need
not be selected equivariantly either; it is used only for pointwise
norm estimates. No additional weighted solution is requested at that
step. Therefore the proof and all constants are unchanged. QED.

## 2. Twisted integral-gap theorem

Let \(\pi:\widetilde X\to X\) be a nontrivial double cover of a closed
oriented four-manifold, and let \(\ell\) denote the associated real
sign local system. A genuine spin-c-minus structure has an associated
\(O(2)\) characteristic bundle and a twisted Euler class
\(a\in H^2(X;\ell)\). Assume that for the metric being tested its
Pin-minus equations have solutions throughout that conformal class.
This assumption holds, in particular, for a nonzero Pin-minus basic
class with \(b_+^\ell\ge2\).

The required lifting statement is the one in
[Ishida--Matsuo--Nakamura, Section 2 and Proposition 8](https://arxiv.org/pdf/1505.05948):
the pulled-back structure is ordinary spin-c, with Chern class
\(\widetilde a=\pi^*a\), and a lifted twisted solution is an ordinary
Seiberg--Witten solution, after matching the constant spinor normalization.
Consequently conformal covariance supplies (1.1) for every positive
deck-invariant weight: the weight descends, the corresponding conformal
metric is still a metric on \(X\), and one lifts its solution before
applying the ordinary conformal transformation.

For the lifted metric, the harmonic projection and intersection form obey

\[
 \widetilde a^2=2a^2,\qquad
 (\widetilde a^+)^2=2(a^+)^2,\qquad
 \widetilde V=2V,\qquad \widetilde T=2T.                 \tag{2.1}
\]

Here products of two sign-local-system classes are untwisted. Pullback
commutes with the twisted Laplacian and with Hodge star; the factor two
in the norms is integration over the covering sheets. This verifies the
normalization rather than treating the twisted Euler class as an
ordinary Chern class downstairs.

**Theorem.** Suppose that for every metric \(g\) on \(X\) one may
select such a twisted class on a fixed double cover, with the same class
working for all weights in that conformal class, and

\[
                  (a_g^+)^2\ge A>0,\qquad a_g^2\ge T_X.
                                                               \tag{2.2}
\]

Then the existing universal constant gives

\[
 \boxed{\displaystyle
 \mathcal E_X(g)+\left(\frac{T_X}{A}-\frac23\right)_+
                  \ge c_*>0\qquad\hbox{for every }g.}           \tag{2.3}
\]

If the last square hypothesis is instead \(a_g^2\ge-C_A A\), the
corresponding constant is \(c(C_A)>0\). There is no degree loss or new
geometric condition.

**Proof.** Apply the invariant-weight lemma upstairs. The Hessian proof
uses the actual Hermitian positive-spinor bundle and its line connection
there, so there is no missing global complex structure on the downstairs
real spinor bundle. Its determinant energy remains

\[
 \int_{\widetilde X}|F_A|^2
    =2\int_{\widetilde X}|F_A^+|^2-4\pi^2\widetilde a^2.
\]

The normalized negative-square cost is
\(( -\widetilde a^2)_+/\widetilde V=(-a^2)_+/V\).
The lifted monopole quadratic form is sign-equivariant; its square
\(\psi\otimes\psi\), and hence
\(A_\psi=|\psi|^2I/24-\psi\otimes\psi/8\), is an ordinary
Weyl-operator model. Alternatively all testing may simply be performed
upstairs without descending this model. The topology-transfer algebra,
positive-sign scalar obstruction and optimization in the Einstein
constant are unchanged. Use (2.1) and exact invariance of
\(\mathcal E\) under pullback to obtain (2.3). QED.

The square hypothesis in (2.2) is explicit. It is **not** inferred from
the virtual dimension formula of arbitrary Pin-minus moduli spaces,
which differs from the ordinary SW dimension formula. The concrete
application below verifies it from the actual glued classes.

## 3. Concrete positive-b-plus surgeries

Let \(M\) be a closed oriented four-manifold with \(b_+(M)\ge2\)
and a spin-c structure with odd ordinary SW invariant and

\[
                     c^2=A=T_M=2\chi(M)+3\tau(M)>0.
\]

For example, any symplectic \(M\) with positive canonical square and
\(b_+\ge2\) supplies such a class. Let \(N\) have \(b_+(N)=0\),
set \(k=b_2(N)\), \(l=b_1(N)\), and let

\[
 Z=\mathop{\#}_{j=1}^{n}(S^2\times\Sigma_{r_j})
      \#\mathop{\#}_{i=1}^{m}(S^1\times Y_i),
 \qquad r_j\ge1,\qquad n+m\ge1,                        \tag{3.1}
\]

where the \(Y_i\) are arbitrary closed oriented three-manifolds. Put
\(X=M\#N\#Z\). The choice \(N=S^4\) simply means no \(N\) summand.
No Yamabe assumption on \(N\) or \(Y_i\) is imposed: only the
nonvanishing theorem, not the paper's Yamabe-equality conclusion, is used.

The classical input is
[Ishida--Matsuo--Nakamura, Proposition 9 and its proof](https://arxiv.org/pdf/1505.05948).
It provides actual Pin-minus basic classes, with independently selectable
exceptional signs, of the form

\[
 a=c+\sum_{j=1}^{k}\epsilon_j e_j+t,
 \qquad (a_g^+)^2\ge A,
 \qquad a^2=A-k.                                       \tag{3.2}
\]

Here the first summand is untwisted, the \(e_j\) form the negative
diagonal part, and \(t\) is the torsion twisted class on \(Z\).
The nonvanishing proof, including its local-system construction, is an
external gauge-theoretic input; the Euler-characteristic computation
alone does not produce these classes.

For connected sums, \(T(U\#V)=T(U)+T(V)-4\). Since
\(T_N=4-4l-k\), \(T_{S^2\times\Sigma_r}=8-8r\), and
\(T_{S^1\times Y}=0\), define

\[
       D=k+4l+\sum_{j=1}^{n}(8r_j-4)+4m.
\]

Then

\[
 T_X=A-D,\qquad a^2-T_X=D-k
          =4l+\sum_j(8r_j-4)+4m\ge0.                   \tag{3.3}
\]

The square condition in (2.2) is now verified. Thus

\[
 \boxed{\displaystyle
 \mathcal E_X(g)+\left(\frac13-\frac DA\right)_+\ge c_* .}
                                                               \tag{3.4}
\]

This permits positive-b-plus connected-sum summands, unlike the earlier
negative-definite connected-sum corollary. When at least one
\(S^2\times\Sigma_{r_j}\) occurs, ordinary SW and ordinary
stable-cohomotopy SW invariants vanish in this family, as noted in the
same paper's introduction. Their vanishing cannot be used to dismiss
the twisted input. Its double cover also has several positive-b-plus
connected-sum factors, so the proof must not pretend that it has an
ordinary nonzero SW invariant.

### An explicit critical family with vanishing ordinary invariants

For each \(j\ge1\), take

\[
 M_j=\Sigma_2\times\Sigma_{3j+1},\qquad
 Z_j=\mathop{\#}_{i=1}^{2j}(S^2\times T^2),\qquad
 X_j=M_j\#Z_j.
\]

The product canonical invariant is \(\pm1\), and

\[
 A_j=8(2-1)((3j+1)-1)=24j,\qquad
 D_j=4(2j)=8j,\qquad
 T_{X_j}=16j,\qquad \frac{T_{X_j}}{A_j}=\frac23.
\]

The new estimate therefore gives the uniform endpoint statement

\[
                  \boxed{\mathcal E_{X_j}(g)\ge c_*}
\]

for every \(j\) and every smooth metric. Ordinary SW and ordinary
stable-cohomotopy SW invariants vanish on these manifolds, while the
twisted classes in (3.2) remain available. This is the quantitative
critical situation: the classical strict exact inequality alone does
not supply a common positive gap for arbitrary metrics across this
infinite family.

### Application to the new closed shear manifolds

Take the smallest closed shear example from round 12:
\(\chi(M)=4\), \(\tau(M)=0\), \(b_+(M)=5\), hence \(A=8\).
The canonical invariant is \(\pm1\). For

\[
                         X=M\#(S^2\times T^2)
\]

one has \(D=4\), \(T_X=4\), and (3.4) becomes

\[
                          \mathcal E_X(g)\ge c_* .      \tag{3.5}
\]

The unmodified \(M\) admits the already constructed
\(\delta_-\to0\) metrics, but **no construction on this modified
smooth manifold can retain arbitrarily small integral Einstein defect**.
This excludes all pointwise near-Einstein constructions there as well.
It is an ansatz-independent conclusion, despite the ordinary invariants
of the modified manifold being zero. Ricci-flat metrics are separately
excluded by the positive twisted monopole scalar estimate.

This last example has \(D/A=1/2\), strictly beyond the classical
critical ratio \(1/3\). A positive defect bound there is also available
from classical twisted curvature estimates away from equality. It is
a useful application to the current construction, not the appropriate
example on which to base the novelty of the quantitative endpoint.

## 4. Position relative to the known theorem

The cited 2016 paper already proves exact Einstein obstructions on this
connected-sum family; its Theorem 16 requires \(D<A/3\) for Einstein
existence. No priority is claimed for that classical obstruction or for
Pin-minus equations. The present consequence replaces a strict exact
threshold by the uniform, all-metric relative integral inequality
(3.4), using the existing self-test theorem with genuinely verified
twisted input.

The extension does not improve the unmodified closed shear ratio. Its
near-Einstein sequence bounds twisted projection budgets just as it
bounds ordinary ones; applying a twisted scalar inequality along that
sequence cannot create a larger budget for the same manifold.
The positive result is instead a new range of surgeries and quotients
to which the integral rigidity mechanism applies.

The finite checks in `round14_rigidity_check.py` include the factors of
two, the connected-sum loss and the explicit shear application. Weighted
solvability and the invariant-weight lemma are proved above, not tested
by those finite calculations.


END COMPLETE SOURCE


---

## Source 4: 20260926_boundary_compatibility.md

Original path: continuation/20260926_boundary_compatibility.md

SHA-256: e182615cd26b7031d4275ae9c5930e244e6088cbad39ac9770c835ba7f5bca19

BEGIN COMPLETE SOURCE

# Endpoint supply, joint-class certificates, and an actual small-topology limit

26 September 2026. This is a continuation of I08, I09 and I12, not a new
independent PDE engine. It incorporates and extends the owner's two supplied
web analyses: [eight-volume synthesis](../guidance/source/20260926_web_eight_volume_synthesis.zh.md)
and [boundary proof program](../guidance/source/20260926_web_boundary_proof_program.zh.md).
The latter supplied the joint-matrix argument and the scalar-slack target;
the former supplied the varying-topology rounding construction. The exact
coercive PDE premises remain those of the inherited manuscripts. No global
priority or external certification of those premises is asserted.

The increments below are: a uniform near-closedness consequence of the actual
field construction; an explicit classical-budget dominance theorem for the
proposed joint certificate; and a same-scope small-h family with an explicit
upper bound from classical gluing. The zero-Weyl weak-gap and optimal h-order
questions remain open. No theorem of unrestricted Einstein realization is
claimed here.

## 1. Actual near-closedness at the zero-Weyl endpoint

Use tensor Ricci norms and endomorphism Weyl norms. Let an actual Spin^c
structure on a closed oriented four-manifold be monopole-solvable for every
metric conformal to g, with the structure fixed during all weight changes.
Put
\[
 V=\operatorname{Vol}(g),\quad p=(a_g^+)^2>0,\quad
 r=\fint|\operatorname{Ric}+g|^2,\quad
 D_\beta=\frac{\beta+1}{\beta}\int(s^2+6\beta|W^+|^2)-72\pi^2p,
 \quad \kappa=r+D_\beta/V.
\]
Here beta is any finite number at least two, and t=1/beta.

**Proposition 1 (the same supplied field is nearly closed).** The bounded
smooth forms used in [the compactified pencil](../mathematics/current/line1_compactified_pencil.md)
can simultaneously be chosen with arbitrarily small allowance such that
\[
 \fint|d\omega|^2\le\frac{39}{4}\kappa+o(1).                 \tag{1.1}
\]
The constant is independent of beta, volume, diameter and Sobolev constants.
This is a consequence of existing estimates, not a new regularity theorem.

**Proof.** In [the actual-field proof](../mathematics/current/line1_functional_pencil.md),
equations (11)--(13), the nonnegative quantity D_0 satisfies
\[
 2\int|d\psi|^2\le D_0\le4S_0/27+o(1),\qquad S_0\le117V\kappa.
\]
The same smooth solution supplies omega=c_beta psi, with
\(c_\beta^2=9\beta/[8(\beta+1)]\le9/8\). Multiplying proves (1.1).
The allowance tends to zero for the fixed metric and class; no uniform rate
of smoothing over a family is used. In particular, the beta=2 almost-parallel
estimate is not being applied at other beta values. QED.

The inherited bounds, on this same form, are
\[
 \|\omega\|_\infty\le3\sqrt2,\quad
 \fint\bigl(|\operatorname{Ric}+g|^2+|W^+-A_{\omega,t}|^2
                    +( |\omega|^2-2)^2\bigr)\le C\kappa+o(1),
\]
\[
 A_{\omega,t}=t(|\omega|^2I/3-\omega\otimes\omega),\qquad
 \fint|\Delta_H\omega|^2\le C(1+\kappa+(-a^2)_+/V)+o(1).    \tag{1.2}
\]
If a^2>=T_+=2chi+3tau, Chern--Weil implies
\((-a^2)_+/V\le r/(8\pi^2)\). For kappa<=1 the last budget is thus
bounded by an absolute B_0. Also
\[
 \fint|W^+|^2\le C\kappa+432t^2+o(1),                    \tag{1.3}
\]
because \(|A_{\omega,t}|^2=(2/3)t^2|\omega|^4\).

### The remaining endpoint theorem is not proved

The new report asks whether, for a smooth self-dual two-form on a closed
oriented Riemannian four-manifold and fixed K and B_0, the assumptions
\(\|\omega\|_\infty\le K\) and
\(\fint|\Delta_H\omega|^2\le B_0\) imply a positive universal lower bound
for
\[
 Z=\fint\bigl(|\operatorname{Ric}+g|^2+|W^+|^2
                     +( |\omega|^2-2)^2+|d\omega|^2\bigr). \tag{1.4}
\]
The exact zero system is impossible: it would give a negative Einstein,
anti-self-dual, almost-Kaehler four-manifold. Armstrong's local obstruction is
recorded in Apostolov--Draghici, [Corollaries 2--3](https://arxiv.org/pdf/math/0302152).
Exact impossibility is not a proof of a positive infimum in this noncompact
class of geometries.

There is also a useful non-parallelism conclusion. For a self-dual form with
Z as in (1.4), the integrated Weitzenboeck identity gives
\[
 \left|\fint|\nabla\omega|^2-\frac83\right|
 \le2Z+\left(\frac43+\frac{8K^2}{3}\right)\sqrt Z.         \tag{1.5}
\]
To see this, use
\(\fint|\nabla\omega|^2=2\fint|d\omega|^2+
2\fint\langle W^+\omega,\omega\rangle-(1/3)\fint s|\omega|^2\),
the trace bound \((\fint|s+4|^2)^{1/2}\le2\sqrt Z\), and the amplitude bound K.
Thus a hypothetical zero-defect sequence here has derivative energy tending
to 8/3, not to zero. The near-parallel KE-end mechanism is not the appropriate
endpoint argument.

There is a concrete analytical distinction. The inherited bounded-form
estimates control a Hessian in L2 and the first derivative in L4. Armstrong's
prolongation argument uses the additional structure generated by the first
derivative of the almost-complex form; repeating curvature commutation there
acts on its cotangent index as well. The original Lambda+ curvature budget
cannot simply be reused as a bound for that tensor connection. Neither a
third derivative estimate nor the corresponding opposite-Weyl contractions
has been supplied. See [Armstrong's thesis, section 3.3.3](https://johnarmstrongmaths.com/publications/resources/thesis.pdf).
This identifies an unfinished route, not a counterexample to (1.4) and not a
proof that such extra hypotheses are necessary for every possible proof.

**Conditional consequence.** If (1.4) has a lower bound eta(K,B_0)>0,
then, under the above actual input and a^2>=T_+,
\[
 r+D_\beta/V\ge c\frac{(\beta-2)^2}{\beta^2},\qquad
 r+P_t/V\ge ct(1-2t)^2,\quad P_t=tD_{1/t}.               \tag{1.6}
\]
Indeed (1.1)--(1.3) give Z<=C kappa+432t^2+o(1). Fix t_0 small
enough to absorb the t^2 term. For t<t_0 a positive kappa gap follows.
For t>=t_0 the already proved compactified estimate is at least a fixed
multiple of (1-2t)^2. The case kappa>1 is immediate. Finally
r+tD/V>=t(r+D/V). This proves only the implication (1.4)=>(1.6).
It would improve the upper-wall endpoint margin from cubic to linear in
h-1/4, since the existing optimal parameter satisfies
t_*(h)~(2/3)(h-1/4). Neither improvement is recorded as achieved.

## 2. Joint-field certificates without fixing a global sign

Assume exactly the multiple actual conformal-class inputs of
[I12](../mathematics/current/line1_period_inertia.md): classes a_1,...,a_m
are each supplied by a fixed actual structure throughout the conformal class,
p_i>0, and
\[
 \kappa=\max_i(r+D_2(g,a_i)/V)\le1/2880.
\]
Define the topological pairing matrix and the sign support function by
\[
 Q_{ij}=\frac{2\pi^2}{V}a_i\cdot a_j,\qquad
 H(Y)=\max_{\sigma\in\{\pm1\}^m}\sigma^T Y\sigma,\qquad
 A(Y)=\left(\sum_i\sqrt{Y_{ii}}\right)^2,
 \quad Y\succeq0.
\]
Let CUT_m be the convex hull of the matrices sigma sigma^T, and
K_m=CUT_m-PSD_m. The negative Hodge part is retained in this set.

**Proposition 2 (the supplied web certificate).** Under these hypotheses,
\[
 \operatorname{tr}(YQ)\le
       \bigl(\sqrt{H(Y)}+\sqrt{27000\kappa A(Y)}\bigr)^2.   \tag{2.1}
\]
No first scalar eigenvalue, common class square, or bound on the negative
Hodge Gram matrix is assumed.

**Proof.** With normalized L2 inner product, let xi_i=-sqrt(2) pi H_i,
where H_i is the self-dual harmonic representative of a_i. I12 gives bounded
u_i with
\[
 \mathbb E|u_i-\xi_i|^2\le49\kappa/2,
 \quad\mathbb E(|u_i|^2-1)^2\le180\kappa,
 \quad\mathbb E|u_i-\sigma_i u_1|^2\le6480\kappa,
\]
up to arbitrarily small simultaneous allowances; sigma_i is the measurable
sign of the inner product with u_1, with sign(0)=+1. Choose n=u_1/|u_1| away from its zero
set and any measurable unit section on that set. Then
\(\mathbb E|u_1-n|^2\le180\kappa\), and two triangle inequalities give
\[
 \mathbb E|\xi_i-\sigma_i n|^2
       \le (49+26640)\kappa=26689\kappa\le27000\kappa.    \tag{2.2}
\]
No measurable sign or normalized section is differentiated.

Let P be the Gram matrix of the xi_i, C that of sigma_i n, and E_err
that of their differences. Thus C is in CUT_m and Q=P-N for N>=0.
For the column operators into the L2 Hilbert space, the Hilbert--Schmidt
triangle inequality after multiplication by sqrt(Y) gives
\[
 \sqrt{\operatorname{tr}(YP)}\le\sqrt{\operatorname{tr}(YC)}
                                      +\sqrt{\operatorname{tr}(YE_{\rm err})}.
\]
The terms on the right are at most sqrt(H(Y)) and
sqrt(27000 kappa A(Y)), respectively; the latter follows from (2.2) and
\(|Y_{ij}|\le\sqrt{Y_{ii}Y_{jj}}\). Since tr(YN)>=0, (2.1) follows.
Letting the allowances tend to zero is done for fixed Y; no convergence
of monopole solutions or signs is required. QED.

In particular, tr(YQ)>H(Y) implies
\[
 \kappa\ge
 \frac{(\sqrt{\operatorname{tr}(YQ)}-\sqrt{H(Y)})^2}{27000A(Y)}. \tag{2.3}
\]
For fixed m, if kappa tends to zero and Q has a finite limit, that limit lies in K_m:
the column error bound gives
\(\|P-C\|_{\rm op}\le m(27000\kappa+2\sqrt{27000\kappa})+o(1)\),
and CUT_m is compact. The conclusion is not rank-one convergence.

### 2.1 A precise limitation for standard signed suppliers

**Proposition 3 (classical scalar budgets dominate these certificates).**
Suppose the actual selected classes have pairings of the form
\[
 Q=\sum_{j=1}^{n_+} w_j s_js_j^T-B,\qquad
 w_j\ge0,\ s_j\in\{\pm1\}^m,\ B\succeq0.                \tag{2.4}
\]
Write S_w=sum w_j. Assume the same metric also has an actual scalar
monopole supplier with projected square at least A_+, where
S_w=2pi^2 A_+/V. Then, with L(r)=(1+sqrt(r)/2)^2,
\[
 Q/L(r)\in K_m,\qquad
 \operatorname{tr}(YQ)\le L(r)H(Y)\quad(Y\succeq0).      \tag{2.5}
\]
This conclusion requires no common endpoint saturation.

**Proof.** The classical signed scalar estimate yields
\[
 32\pi^2 A_+\le\int s_-^2,
 \quad\|s_-\|_{L^2(d\mu/V)}\le4+\|s+4\|_2\le4+2\sqrt r.
\]
Hence S_w<=L(r). A convex combination of the sign matrices with weights
w_j/L(r), completed to total weight one with any other sign matrix, gives
C in CUT_m with C-Q/L(r)>=0. This proves both statements. QED.

For Y nonzero, H(Y)>0. A proposed separation t=tr(YQ)>H(Y) already
forces, by this classical estimate alone,
\[
 r\ge4\frac{(\sqrt t-\sqrt{H(Y)})^2}{H(Y)}.              \tag{2.6}
\]
Since H(Y)<=A(Y) and r<=kappa, this is stronger than (2.3) on this supplier
family. Thus finding such a certificate here does not demonstrate an
application beyond the scalar projection budget.

The hypotheses apply to the standard actual signed connected-sum suppliers
with positive orthogonal blocks b_j^2>0 and a negative-definite exceptional
block. Their cup matrix has (2.4), with w_j=2pi^2 b_j^2/V. Full independent
sign supply guarantees A_+=sum b_j^2: average the positive Hodge squares
over all signs; the result is the sum of the individual projected squares,
at least sum b_j^2. Some sign choice therefore supplies that budget.
Alternatively, use the already established metricwise selected supplier.
This includes the relevant [BF application](../mathematics/current/line1_bauer_furuta_geography.md)
and ordinary blow-ups. A twisted version requires one common real local
system, its actual pairing and its established scalar estimate; no cross
pairing between unrelated local systems is asserted.

For a full independent sign cube with a diagonal negative exceptional block,
the statement has an exact algebraic version: Q belongs to K_m if and only
if S_w<=1. Sufficiency is the preceding convex argument. For necessity,
let Y be the orthogonal projection onto the span of the positive sign
coordinate columns. These Walsh columns have squared norm m and are
orthogonal to all exceptional columns. Hence tr(YQ)=m S_w, while
H(Y)=m (a positive coordinate column attains the maximum). Membership in
K_m implies m S_w<=m. This necessity is not asserted for arbitrary subsets
of sign rows or arbitrary negative matrices B.

The report's higher slow-spectrum estimate is a separate conditional-field
consequence, not a new scalar-gap-free topological obstruction. Round18
already contains a spectral-cluster mechanism; the later assumptions allow
unequal squares and an uncontrolled negative Hodge part. No actual family
with a new separation beyond established budgets is supplied in this note.

### 2.2 An actual matrix realization which does not increase obstruction scope

The formal three-by-three example in the supplied report can in fact be
realized by actual BF classes, but not in its required small-error regime.
Let X be a smooth degree-eight hypersurface in CP^3. Adjunction gives
c_1^2=128 and p_g=35; Lefschetz gives b_1=0, hence b_+=71, congruent to
three modulo four. On
\(M=X\#X\#X\#128\overline{\mathbb{CP}}^2\), the established three-block
BF supply gives the independent canonical and exceptional sign classes.
Choose positive sign rows (-,+,+), (+,-,+), (+,+,-). Choose exceptional
sign rows by repeating each of the vectors (1,1,1,1), (1,1,-1,-1),
(1,-1,1,-1) thirty-two times. The three exceptional rows are orthogonal.
The resulting actual classes have diagonal square 256 and off-diagonal
pairing -128. At volume 512pi^2 their Q is exactly
\[
 Q_* = \begin{pmatrix}1&-1/2&-1/2\\-1/2&1&-1/2\\-1/2&-1/2&1\end{pmatrix}.
\]
Thus Y=I-11^T/3 has tr(YQ_*)=3>8/3=H(Y). However A_+=384 and
S_w=3/2, so (2.5) already forces r>=10-4sqrt(6)>0.202. In particular,
the common small-kappa premise cannot hold. Also h=(128+8)/384>1/3;
the classical BF Einstein obstruction already applies. The precise supplier
and obstruction are [Ishida--LeBrun, Proposition 10, Corollary 11 and Theorem D](https://arxiv.org/pdf/math/0111228).
This example separates actual realizability of the intersection matrix from
a genuinely new application of its certificate. It supplies the former only.

## 3. Small h in the actual two-chirality window

Define E(g)=inf over nonzero lambda of
\(\int|\operatorname{Ric}-\lambda g|^2/(\lambda^2 V)\).
For R=int|Ric|^2>0 and I=int s, minimization in 1/lambda gives
\[
 \mathcal E=4-I^2/(VR).                                  \tag{3.1}
\]
This includes I=0 as an infimum, not necessarily a minimum.

**Proposition 4 (explicit upper bound from classical gluing).** If X is a
compact complex-hyperbolic surface, A=c_1^2(X), and
\(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), then
\[
 \inf_g\mathcal E(g)\le\frac{4h}{1+h},\qquad h=(k+4\ell)/A. \tag{3.2}
\]
The upper bound does not assert attainment.

**Proof.** Normalize Ric=-g on X. The scalar-flat anti-self-dual
insertions in [LeBrun, Theorem 4.3 and its proof](https://arxiv.org/html/math/0003068)
give, on each fixed M, metrics with
\[
 V_\epsilon\to2\pi^2A,\quad I_\epsilon\to-8\pi^2A,
 \quad R_\epsilon\to8\pi^2A(1+h).                        \tag{3.3}
\]
For the first two limits, the exterior converges to the normalized background,
the inserted scalar-flat regions have vanishing volume, and the transition
annuli have bounded scalar curvature and vanishing volume. These are features
of that construction, not consequences of the Ricci-energy infimum alone.
Substitution in (3.1) proves (3.2). QED.

The no-handle limit 4k/(A+k) was already recorded in the project's
[Kaehler controls, section 5](../mathematics/current/line1_kahler_energy.md).
The present use includes handles and places the bound in the same numerical
window as I08; it is not a newly invented gluing construction.

**Theorem 5 (same-scope vanishing family, conditional on I08).** There are
actual ordinary-monopole manifolds M_j, with h_j tending to zero, such that
\[
 0<U_j-F(h_j)=o(h_j^2),\qquad
 c_1h_j^2\le\inf_g\mathcal E(g)\le\frac{4h_j}{1+h_j}\to0.  \tag{3.4}
\]
All sufficiently late M_j admit no Einstein metric of any sign.
Here F(h)=(4-sqrt(1-3h))^2/9 and U=3min(T_+,T_-)/A, precisely as in I08.

**Proof.** Use connected finite unramified covers X_j of a fixed compact
complex-hyperbolic surface, taking a subsequence with A_j>=j^4. Their
existence is explained in the retained [two-chirality construction, section 3](../mathematics/current/line1_two_chirality_topology.md):
the infinite finitely generated lattice is linear and residually finite.
No prescribed cover degree or divisibility is required. Put eta_j=1/j and,
eventually, 0<eta_j<=19/300. Define
\[
 x(\eta)=\frac{F(\eta)-1+3\eta}{18},\qquad
 y(\eta)=\frac{15\eta-F(\eta)+1}{72},
 \quad k_j=\lfloor A_jx(\eta_j)\rfloor,\quad
 \ell_j=\lfloor A_jy(\eta_j)\rfloor-2.                   \tag{3.5}
\]
They are nonnegative for large j, since x~2eta/9 and y~7eta/36.
Let M_j be the indicated connected sum. Write the two fractional parts as
alpha_j,beta_j in [0,1). The identities x+4y=eta and
1+15x-12y=F(eta) imply
\[
 h_j=\eta_j-(\alpha_j+4\beta_j+8)/A_j,
 \quad U_j=F(\eta_j)+(-15\alpha_j+12\beta_j+24)/A_j.       \tag{3.6}
\]
For the second identity, tau(M_j)=A_j/9-k_j>0 eventually, so the smaller
chiral budget is T_-; the absolute value in U has not been omitted.
Since 0<F'<2 on [0,19/300],
\[
 0<U_j-F(h_j)<(36+26)/A_j=62/A_j=o(h_j^2),\quad h_j\sim1/j.
\]
Ordinary polarized supply gives, for every metric, a class with
p>=A_j and a^2=A_j-k_j>=T_+=A_j-k_j-4ell_j, fixed through its
conformal weights. Handle additions do not decrease this class square;
their contribution to T_+ is a separate topological term.
I08 therefore yields E>=c h_j^2-62/A_j>=(c/2)h_j^2 for large j.
Apply Proposition 4 to each fixed M_j for the upper bound. Nonzero Einstein
constants have E=0. Ricci-flat metrics are independently excluded by
\(\int s_-^2\ge32\pi^2A_j>0\). QED.

An actual diagonal sequence can approximate (3.2) on each M_j to any chosen
o(h_j) error. Alternatively the fixed-radius surgery construction in the
supplied synthesis gives O(h_j) directly. Neither gives pointwise-small
Ricci error. Thus (3.4) disproves an h-independent positive integral gap
in this same class, but proves neither h^2 sharpness nor a Yau26 counterexample.

## 4. What is actually missing for linear h-order

Put S=int s^2, P=int|Ric^circ|^2, Sigma=S-32pi^2 p>=0 and D=D_2.
Classical Chern--Weil gives the exact identity
\[
 36\pi^2(p-T_+)=\frac92P+\frac98\Sigma-D.                \tag{4.1}
\]
The proposed strengthening Sigma<=C(P+D) would yield a linear h lower
bound on (3.4). It is not proved by the existing parameter inequalities.

A precise estimate that does follow is
\[
 \Sigma\le\frac49D+\frac{4\sqrt2}{3}\sqrt{RD}.            \tag{4.2}
\]
Indeed let z=s+2sqrt(6)|W^+|. The completed-square inequality gives
int z^2<=2D, and direct substitution gives
\(\Sigma=(4/9)D+(2/3)\int sz-(1/3)\int z^2\).
Cauchy--Schwarz and S<=4R prove (4.2). For a Kaehler metric in its complex
orientation, |W^+|^2=s^2/24 gives the stronger identity
Sigma=(4/9)D, for any p used in these definitions. The general input is
not assumed Kaehler, so this special identity cannot be transplanted.

Here is an algebraic test isolating the missing differential information.
Write C_A=8pi^2 A and, for small positive h, prescribe formal moments
\[
 T_+=A(1-h),\quad p=A,\quad
 R=C_A(1+h+2h^2),\quad P=C_Ah^2,\quad
 S=4C_A(1+h+h^2),\quad W_+:=\int|W^+|^2=C_A(1-h)^2/6.
\]
Choose constant formal scalar curvature so that I^2/V=S. These data obey
the plus Chern--Weil identity, the scalar bound and all scalar--Weyl pencil
nonnegativity tests: with x=2sqrt(1+h+h^2) and y=1-h, x>=2 and x+y>=3.
For U=F(h)+o(h^2), the minus Weyl energy is also positive for small h,
because it equals C_A[U-1-h+2h^2]/12. Yet
\[
 D=9C_Ah^2,\quad\Sigma=4C_Ah(1+h),\quad
 \mathcal E+D/R=\frac{13h^2}{1+h+2h^2},\qquad
 \frac{\Sigma}{P+D}=\frac{2(1+h)}{5h}\to\infty.           \tag{4.3}
\]
These are not actual metrics or monopole solutions, and so are not a
counterexample to the proposed inequality. They prove a narrower useful
fact: the displayed numerical identities and near-Einstein moment conditions
alone cannot prove that inequality. A proof would need additional actual-field
or differential compatibility information. The topology in (3.4) is real;
the moments in (4.3) are only a feasibility test and are not identified with
the metrics used in (3.3).

For precision, the implication of the proposed linear inequality has no
additional hidden small-deficit branch. Suppose Sigma<=C(P+D) holds for a
selected Spin^c structure whose unperturbed equations are solvable for every
metric conformal to g, fixed through all weights, with A>0, p>=A,
a^2>=T_+=A(1-h), and E+D/R<eta_0, with uniform C and eta_0.
On the family (3.4), eventually
U<=1+h+3h^2. If E<1/2, the classical lower Ricci budget and the chiral upper
budget give 1+h<=e<=U/(1-E)<=3. Since
\[
 D/C_A=\frac92\{e-(1+h)-2(p/A-1)\},\qquad P/C_A\le eE/4,
\]
one may use the loose bounds D/C_A<=27h^2+18E and P/C_A<=3E/4.
It follows that E+D/R<=19E+27h^2. If the small-deficit hypothesis fails,
small enough h forces E>=eta_0/38. If it holds, (4.1) and p-T_+>=Ah
give h<=K(E+h^2), hence E>=h/(2K) for sufficiently small h. The case
E>=1/2 is immediate. Together with (3.2), the proposed inequality would
therefore imply inf E asymptotic to h up to two fixed positive multiplicative
constants. Its unproved ingredient is exactly the scalar-slack inequality,
not the conversion from that inequality to an all-metric conclusion.

## 5. Realization and the fixed-manifold question remain separate

The supplied off-boundary identity is correct classical algebra:
\[
 D_2+72\pi^2(p-T_+)+54\int|W^-|^2
      =18P+144\pi^2(\chi-3\tau).                         \tag{5.1}
\]
At p>=T_+ and chi=3tau it supplies the saturation used in I26. It does
not remove diameter or identify the filling of a long thin end. The suggested
diameter-free numerical-boundary realization and the quantitative W^{2,p}
repair rate remain targets, not consequences established in this continuation.

The fixed Dehn-twist bundle E_D is already registered as C02/O02. Its
reported pointwise approximations, virtual non-Kaehler restrictions and
candidate Einstein volume window belong to the retained cross-line proofs.
This continuation neither reconstructs its full pointwise sequence nor
excludes all its negative Einstein outputs. Its global existence question
is not replaced by the small-h integral family above, where topology varies.
The existing elimination of nonnegative Einstein outputs is a separate
topological/scalar argument; no failure of one repair algorithm supplies the
remaining negative-output exclusion.

The current common problem is therefore stable: use actual fields to decide
which numerical boundaries are geometrically realizable. Sections 1--4 make
specific parts of that question more precise. They do not combine the
obstruction, compact realization and unrestricted Yau26 statements into an
unproved exhaustive dichotomy.


END COMPLETE SOURCE


---

## Source 5: 20260926_actual_topological_cost.md

Original path: continuation/20260926_actual_topological_cost.md

SHA-256: 5b189c3143977efe8ab65b4f22c06ef2e8d354d30faa69180a0f07eadf95772b

BEGIN COMPLETE SOURCE

# Actual spinor energy and the location of a possible topological cost

26--27 September 2026, Beijing time. Continuation of
[the boundary proof](20260926_boundary_compatibility.md), based at local
commit `f48f385`. The owner's
[parallel execution brief](../guidance/source/20260926_web_parallel_execution.zh.md)
proposes zero-Weyl rigidity and a linear small-h lower bound. Neither is
assumed proved here. The inherited actual weighted-field construction is an
explicit premise, with its original fixed-structure/conformal-solvability
quantifiers. No inherited proof or eight-volume source is replaced.

Two connections are proved below using the **same bounded weighted
solution**. First, an exact remainder identity, the localized spinor equation
and signed Chern transgression force any sublinear small-h sequence to carry
both projective first-order energy and critical transition-layer concentration.
This avoids comparing unidentified ordinary and weighted solutions. Second,
a smooth cubic torsion field satisfies an additional Dirac identity, giving
a vanishing weak residual at the hypothetical zero-Weyl endpoint. These are
necessary-structure and weak-equation results; neither the linear small-h
gap nor the zero-end exclusion is assumed or claimed.

## 1. An exact identity without differentiating the weight

Let M be a closed oriented Riemannian four-manifold. Use the spinor and
curvature conventions of [the functional pencil](../mathematics/current/line1_functional_pencil.md).
Fix an actual Spin^c structure and a smooth positive weight f, and a solution
of the corresponding rescaled Seiberg--Witten equations. Write

\[
 \rho=|\Phi|^2,\quad K_A=\int|\nabla_A\Phi|^2,\quad
 p=(a_g^+)^2,\quad \Sigma=\int s^2-32\pi^2p,
 \quad J_+=\|iF_A^+-2\pi H\|_2^2,
\]

where H is the self-dual harmonic representative of a_g^+. The sign of
the quadratic map is chosen so that the determinant curvature has harmonic
projection 2pi H. The two identities needed are

\[
 4K_A+\int s\rho+\int f\rho^2=0,\qquad
 \int f^2\rho^2=32\pi^2p+8J_+.                 \tag{1.1}
\]

**Proposition 1.** For every constant c>0, the same solution satisfies

\[
 \boxed{\Sigma+\int(f-c)^2\rho^2
 =\|s+c\rho\|_2^2+8cK_A+8J_+.}              \tag{1.2}
\]

**Proof.** Expand the square on the right and substitute (1.1). The
coefficient of rho^2 after cancelling the scalar-spinor term is
c^2-2cf+f^2=(f-c)^2. No derivative of f is taken. QED.

For f=c=1 this recovers the ordinary-solution remainder in the supplied
brief. For a variable f, it is not legitimate to omit the additional
nonnegative term on the left. In particular, replacing Phi by sqrt(f)Phi
would introduce derivatives of f; (1.2) does not make that replacement.
The equations and Weitzenboeck input are classical; retaining and using the
same weighted solution is the point of the present composition.

## 2. Uniform amplitude and potential estimates for the supplied solution

Retain the actual conformal-solvability hypotheses of the inherited pencil,
with the same structure throughout all auxiliary weights. Put

\[
 r=\fint|\operatorname{Ric}+g|^2,\quad
 \kappa=r+D_\beta/V,\quad 2\le\beta<\infty,
 \quad q_\beta=4(1+1/\beta),
 \quad c_\beta=\sqrt{q_\beta},\quad \rho_\beta=2c_\beta/3.
\]

Here c_beta denotes the reference **weight**, not the form rescaling
constant denoted similarly in some earlier manuscripts. Set
U=s+f rho and U_beta=-4+c_beta rho_beta=(4/3)(2/beta-1).
The selected smooth majorants may have an arbitrarily small total allowance
epsilon V in the following estimates. Every estimate concerns the same
actual solution; one can choose epsilon after fixing each metric and class.

**Lemma 2.** The inherited construction gives, uniformly in beta,

\[
 \rho\le4,\qquad
 \fint(\rho-\rho_\beta)^2\le40\kappa+o(1),\qquad
 \fint(f-c_\beta)^2\le\tfrac{33}{2}\kappa+o(1),
                                                        \tag{2.1}
\]
\[
 \fint|U-U_\beta|^2\le1504\kappa+o(1),\quad
 \fint|d\rho|^2\le\tfrac{26}{3}\kappa+o(1),\quad
 8J_+/V\le52\kappa+o(1).                              \tag{2.2}
\]

**Proof.** With the original notation w=sqrt(6)|W+|, q=-s+w,
Q=max(q,3), e=s+4, u=3rho/2 and f_0=max(sqrt(Q),(-s)_+/4), the exact
square completion gives

\[
 \int(q-q_\beta)^2\le18\kappa V,\quad
 \int e^2\le4\kappa V,\quad
 \int Q(u-\sqrt Q)^2\le117\kappa V+o(V).
\]

Clipping at three does not increase distance to q_beta in [4,6]. Thus
int(sqrt(Q)-c_beta)^2<=6kappa V and
int(u-sqrt(Q))^2<=39kappa V. Combining gives the first amplitude
estimate. Also (f_0-sqrt(Q))^2<=f_0^2-Q<=9e^2/16, which gives the
weight estimate. The potential difference is
e+c_beta(rho-rho_beta)+(f-c_beta)rho. First bound the first two terms
together by 488kappa V and the last by 264kappa V, and then their sum
by 1504kappa V. Finally D_0<=52kappa V/3 controls 2int|drho|^2.
The actual curvature moment C_act satisfies
C_act-72pi^2p<=117kappa V+o(V); since
8J_+=(4/9)(C_act-72pi^2p), this proves the final estimate. QED.

**Corollary 3 (same-solution scalar-slack comparison at beta=2).** Take
c=sqrt(6). Then

\[
 -540\kappa V-o(V)\le8\sqrt6 K_A-\Sigma
 \le264\kappa V+o(V).                                 \tag{2.3}
\]

Indeed rho_2=4/sqrt(6), so int(s+c rho)^2<=488kappa V+o(V),
int(f-c)^2rho^2<=264kappa V+o(V), and 8J_+<=52kappa V+o(V).
Substitute in (1.2). The little-o allowance here is freely selectable
smoothing error, not an assumed limiting solution or a rate in kappa.

## 3. Actual first-order energy cannot be hidden at spinor zeros

Use a fixed pair 0<a<b<4/3. A Lipschitz nonincreasing cutoff chi(rho)
equals one below a and zero above b, with |chi'|<=1/(b-a). Smooth
approximations give the same inequalities. Testing

\[
             4\nabla_A^*\nabla_A\Phi+U\Phi=0
\]

against chi(rho)Phi gives the exact real identity

\[
 4\int\chi|\nabla_A\Phi|^2+
 2\int\chi'|d\rho|^2+\int\chi U\rho=0.
\]

If mu_b=Vol{rho<b}/V, Cauchy--Schwarz gives

\[
 \fint_{\{\rho\le a\}}|\nabla_A\Phi|^2
 \le\frac{\fint|d\rho|^2}{2(b-a)}
 +\frac b4\left(|U_\beta|\mu_b+
      \|U-U_\beta\|_{L^2_{\rm avg}}\sqrt{\mu_b}\right). \tag{3.1}
\]

The symbol fint over a subset here and below means integral over the
subset divided by **total** V. By (2.1),
mu_b<= (40kappa+o(1))/(rho_beta-b)^2; rho_beta>=4/3 and |U_beta|<=4/3.
Consequently

\[
 \boxed{\int_{\{\rho\le a\}}|\nabla_A\Phi|^2
             \le C_{a,b}\kappa V+o(V).}                \tag{3.2}
\]

This is uniform over all finite beta>=2, and uses the actual spinor equation
and moment remainders. It is stronger than applying a generic Hessian/L4
estimate, which would give only an O(sqrt(kappa)) bound. It does not estimate
the fourth-power gradient or squared Hessian energy on the same set.

There is a further phase/radial decomposition. On {rho>0}, let Pi_Phi be
Hermitian projection onto the complex line spanned by Phi, and write
gamma=Im< Phi,nabla_A Phi >, with the pairing linear in its second entry.
For the normalized quadratic map psi used
in the original proof, direct differentiation gives

\[
 4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2=4|\gamma|^2,
 \qquad
 |\Pi_\Phi\nabla_A\Phi|^2
       =\frac{|d\rho|^2}{4\rho}+\frac{|\gamma|^2}{\rho}.
                                                        \tag{3.3}
\]

These identities can be checked in a unitary frame Phi=(sqrt(rho),0),
with an arbitrary complex two-component derivative; they are gauge
invariant. Since both remainders are summands of D_0,

\[
 \int_{\{\rho>a\}}|\Pi_\Phi\nabla_A\Phi|^2
       \le\frac{13}{2a}\kappa V+o(V).                 \tag{3.4}
\]

Thus all but O(kappa V) of K_A lies in
int_{rho>a}|(1-Pi_Phi)nabla_A Phi|^2. This is a change of direction of
the spinor line, not a gauge phase change or a change of amplitude.

For completeness, testing the spinor equation against Phi and using (2.1)
--(2.2) gives

\[
 K_A/V=-\tfrac14 U_\beta\rho_\beta+O(\sqrt\kappa)+o(1)
       =\tfrac29\sqrt{q_\beta}(1-2/\beta)
          +O(\sqrt\kappa)+o(1).                       \tag{3.5}
\]

In a putative actual zero-end sequence beta->infinity, kappa->0,
the projective-direction energy outside {rho<=a} therefore tends to 4/9.
The previously proved two-form energy limit 8/3 is consistent with this.
Neither limit is zero-Weyl rigidity: it identifies which nonparallel
energy that rigidity would have to detect.

## 4. A necessary structure theorem for any sublinear small-h sequence

Fix precisely the varying-topology family in Theorem 5 of
[the preceding continuation](20260926_boundary_compatibility.md), with
T_+=A(1-h), p>=A and U_top=F(h)+o(h^2). Its selected actual class has
a^2=A-k and c_2(S^+)[M]=ell, with ell/(Ah)->7/36. The positive budget,
actual conformal-solvability and chiral identities are unchanged.

**Theorem 4 (where a hypothetical sublinear cost must go).** Suppose
metrics g_j on this same family satisfy E(g_j)=o(h_j). After the optimal
negative rescaling, there exist the bounded beta=2 actual weighted
solutions above, with freely chosen allowances o(h_j), such that

\[
 \frac{V_j}{A_j}\to2\pi^2,\qquad
 \kappa_j=o(h_j),\qquad
 \frac{\Sigma_j}{A_jh_j}\to32\pi^2,
                                                        \tag{4.1}
\]
\[
 \boxed{\frac1{A_jh_j}
   \int_{\{\rho_j>a\}}|(1-\Pi_{\Phi_j})\nabla_{A_j}\Phi_j|^2
       \longrightarrow\frac{4\pi^2}{\sqrt6}.}           \tag{4.2}
\]

The integral on {rho_j<=a} and the line/radial/phase derivative on
{rho_j>a}, divided by A_j h_j, both tend to zero.

**Proof, including the normalization and sign.** Put R=int|Ric|^2,
I=int s, L_s=int(s-I/V)^2 and e=R/(8pi^2 A). For R>0,

\[
 E=4-I^2/(VR)=(4P+L_s)/R.
\]

If I>=0, the actual scalar estimate gives
32pi^2 A<=int s_-^2<=L_s<=RE, hence 4<=eE. On the other hand,
e(1-E)<=U_top and U_top<=2 eventually, so for E<1/2 we have e<=4
and eE<2, a contradiction. Thus I<0 for all late j.
The minimizing constant is lambda_*=R/I<0. Set g'=(-lambda_*)g.
Then r(g')=E(g), V(g')=R/(4-E), and R,P,D_2,p are invariant under
this constant rescaling. Relabel g' as g.

The exact identities are

\[
 D_2=36\pi^2A\{e-(1+h)-2(p/A-1)\},\qquad
 36\pi^2(p-T_+)=\tfrac92P+\tfrac98\Sigma-D_2.
\]

Together with p>=A, D_2>=0 and e(1-E)<=U_top=1+h+O(h^2), these
give e=1+h+o(h), p-A=o(Ah), D_2=o(Ah), P<=RE/4=o(Ah), and
Sigma/(Ah)->32pi^2. Also V/A=8pi^2e/(4-E)->2pi^2, proving (4.1).
Equation (2.3) then gives K_A/(Ah)->4pi^2/sqrt(6). Choose all
smoothing allowances o(h). Equations (3.2) and (3.4), with kappa=o(h),
leave exactly (4.2). QED.

This theorem goes beyond a formal moment model: it concerns the same
actual bounded solution used in the curvature-deficit proof. It does not
assert that (4.2) is impossible. The still-open estimate P+D_2>=c ell
would exclude the entire sequence and imply a linear lower bound; no such
estimate is assumed in Theorem 4.

### 4.1 Positive Chern charge forces critical transition concentration

The necessary condition can be strengthened using the **sign** of the
determinant curvature, not an absolute bound on all its components.
Write Theta=(kappa+epsilon)V, where epsilon is the selectable allowance.
For bundle curvature in this subsection use the two-form Hilbert--Schmidt
norm sum_{i<j}|F_ij|^2, half the double-sum convention of the inherited
Hessian lemma. Let F be the curvature of the positive spinor connection,
F=Omega+(F_A/2)I, where Omega is traceless.

**Theorem 5 (localized positive-charge bound).** For the same beta=2
supplied solutions there is a universal C such that

\[
 \boxed{c_2(S^+)[M]\le C\Theta+
               C\int_{\{1/2<\rho<1\}}|\nabla_A\Phi|^4.} \tag{4.3}
\]

No bound for W-, F_A- in L-infinity, derivatives of f, a uniform Sobolev
constant or transverse zeros is required. The inequality holds also when
c_2 is negative; its useful application here is c_2=ell>0.

**Proof.** For a unitary rank-two connection,
c_2(F)=(tr(F wedge F)-trF wedge trF)/(8pi^2). In our conventions,

\[
 16\pi^2 c_2(F)=\left(|F_A^+|^2-|F_A^-|^2
                 -2|\Omega^+|^2+2|\Omega^-|^2\right)d\mu,
 \quad |\Omega^+|^2=|W^+|^2+s^2/48,\quad
 |\Omega^-|^2=|\operatorname{Ric}^\circ|^2/4.            \tag{4.4}
\]

In particular its positive part is bounded by
(|F_A+|^2+|Ric^circ|^2/2)/(16pi^2), while the term
-|F_A-|^2/(16pi^2) must be retained for the argument below.

Let B={rho<=1} and T={1/2<rho<1}. Since (4/sqrt(6)-1)^2>2/5,
(2.1) gives Vol(B)<=100Theta. The actual equation and weight estimate give

\[
 \int_B|F_A^+|^2=\tfrac18\int_B f^2\rho^2
       \le\tfrac18(12\operatorname{Vol}(B)+33\Theta)
       \le155\Theta.                                  \tag{4.5}
\]

On B the bounded model A_{omega,1/2}, with omega=sqrt(3)psi/2, has
|A_{omega,1/2}|^2=3rho^4/32<=3/32. The inherited squared model error
is at most CTheta. Thus int_B|W+|^2<=CTheta; also int_B s^2<=CTheta
and int|Ric^circ|^2<=Theta. Consequently

\[
 \int_B G^2\le C\Theta,\qquad G^2=|\Omega|^2+|F_A^+|^2. \tag{4.6}
\]

On {rho>0}, set u=Phi/sqrt(rho), Pi=uu*, Q=1-Pi. Define a unitary
connection nabla^0 by
nabla^0(zu+w)=dz tensor u+Q nabla_A w for w perpendicular to u.
It fixes u, so c_2(F^0)=0. In a local unitary frame (u,v), write
nabla_A u=i alpha u+b v; the difference B_c=nabla_A-nabla^0 is
the matrix [[i alpha,-b*],[b,0]], with |B_c|<=sqrt(2)|nabla_A u|.
The projected-connection curvature formula gives
|F^0|<=C(|F|+|nabla_A u|^2). For nabla^t=nabla^0+tB_c,
F^t=(1-t)F^0+tF-t(1-t)B_c wedge B_c, hence the same bound holds.
The Chern--Weil transgression form

\[
 T_u=\frac1{4\pi^2}\int_0^1
       \{\operatorname{tr}(B_c\wedge F^t)
             -\operatorname{tr}B_c\wedge\operatorname{tr}F^t\}\,dt
\]

satisfies dT_u=c_2(F), and

\[
 |T_u|\le C\left(|F||\nabla_Au|+|\nabla_Au|^3\right).  \tag{4.7}
\]

Choose a smooth eta equal to zero below 1/2 and one above 1, with
|eta'|<=4, and put chi=(1-eta)^2. Then |chi'|<=8 and
(chi')^2/chi<=64 on {chi>0}. The form (1-chi(rho))T_u extends by
zero smoothly across Phi=0. Stokes' theorem therefore yields exactly

\[
 c_2(S^+)[M]=\int\chi(\rho)c_2(F)+\int d\chi(\rho)\wedge T_u.
                                                        \tag{4.8}
\]

On T, |nabla_Au|<=|nabla_A Phi|/sqrt(rho) and
|drho|<=2sqrt(rho)|nabla_A Phi|. The second integral is bounded by
C|chi'|[(G+|F_A-|)|nabla_A Phi|^2+|nabla_A Phi|^4] integrated over T.
Young's inequality bounds its F_A- part by

\[
 \frac{\chi|F_A^-|^2}{32\pi^2}
       +C\frac{(\chi')^2}{\chi}|\nabla_A\Phi|^4.
\]

The first term is absorbed by half the **negative** central contribution
in (4.4). The G term costs CG^2+C|nabla_A Phi|^4. Apply (4.5)--(4.6)
to all remaining curvature terms. This proves (4.3). QED.

**Corollary 6 (two distinct energy locations are compulsory).** Under
the hypothesis of Theorem 4, take epsilon_j=o(h_j). Then

\[
 \operatorname{Vol}(T_j)=o(A_jh_j),\qquad
 \int_{T_j}|\nabla_{A_j}\Phi_j|^2=o(A_jh_j),\qquad
 \int_{T_j}|\nabla_{A_j}\Phi_j|^4\ge cA_jh_j.            \tag{4.9}
\]

Indeed the first two statements follow from (2.1), (3.2), choosing
a=1<b<4/3. Since ell_j/(A_jh_j)->7/36, (4.3) gives the third. In
particular, with kappa including an arbitrarily small allowance,

\[
 \sup_{T_j}|\nabla_{A_j}\Phi_j|^2
       \ge\frac{c h_j}{\kappa_j+\epsilon_j}\longrightarrow\infty.
                                                        \tag{4.10}
\]

Thus a sublinear defect requires both the diffuse leading L2 projective
energy from (4.2) on normal-amplitude points and critical L4 concentration
in a small-amplitude transition layer. Neither a purely slow diffuse field
nor the negative determinant-curvature bulk term alone can account for it.
Here "diffuse leading L2" means the leading term is outside the declared
small-amplitude set; it does not assert uniform spatial equiintegrability
over every other set.

This is not yet a contradiction: the inherited global L4 budget permits
(4.9). Even ordinary equiintegrability with respect to dmu/V would give
only o(V), insufficient when the required charge is hV->0 relative to V.
Closing the linear bound needs control at the **hV scale**, or a direct
actual-equation exclusion of (4.9). No such control is silently added.

## 5. The topological quantities and the critical energy not yet controlled

For a Spin^c structure with determinant L and a=c_1(L), the splitting
principle gives

\[
 c_2(S^+)[M]=(a^2-T_+)/4,\quad
 c_2(S^-)[M]=(a^2+2\chi-3\tau)/4,
\]
\[
 c_2(S^-\otimes L)[M]
   =5\chi+6\tau+\tfrac94(a^2-T_+).                    \tag{5.1}
\]

Indeed twisting a rank-two bundle of first Chern class a by L increases
its second Chern class by 2a^2. These are identities, not energy-gap
theorems. With the manuscript curvature norms, Chern--Weil also gives

\[
 \frac{8\pi^2(5\chi+6\tau)}V
 =\fint(9|W^+|^2+|W^-|^2+5s^2/24-5|\operatorname{Ric}^\circ|^2/2)
 \ge10/3-(10/3)\sqrt r-(5/2)r.                         \tag{5.2}
\]

Armstrong's compact exact argument uses a nowhere-zero torsion section
to force the corresponding characteristic number to vanish. Equations
(5.1)--(5.2) provide the desired opposite inequality for actual inputs,
but the existence of an approximate torsion section alone does not force
vanishing. Its zeros and concentrated critical energy must be retained.
See [Armstrong, section 2.2.2](https://johnarmstrongmaths.com/publications/resources/thesis.pdf).

The actual estimates (3.2)--(3.4) remove concentration of the **first**
spinor derivative energy as an explanation for Theorem 4's leading term.
They do not prove uniform integrability of |nabla Phi|^4 or |nabla^2 Phi|^2,
nor any L4 bound for the derivative of a torsion section containing
nabla Phi. Those are different orders of information. The zero-end weak
gap and the linear small-h lower bound therefore remain open.

### 5.1 A polynomial opposite-spinor field and its weak Dirac equation

Let B=S^- tensor L, with the tensor-product connection; its determinant
connection is 3A. Define, without division by the spinor length,

\[
 t_\Phi=\sum_i c(e^i)\Phi\otimes(\Phi\wedge\nabla^A_i\Phi)
              \in\Gamma(B).                           \tag{5.3}
\]

The contraction is invariant under orthonormal-frame and unitary Spin^c
changes. It is smooth across the zero set of Phi. It is the candidate
suggested in the owner's execution brief; the following equation is a
further calculation, not an assertion supplied by the exact rigidity theorem.

**Proposition 7 (actual weak Dirac bridge at the zero endpoint).** For the
same weighted solution, put P_i=nabla_i Phi, w_i=Phi wedge P_i. In the
Clifford convention described below,

\[
 D^-_{3A}t_\Phi=-4\sum_i P_i\otimes w_i+\mathcal K,\qquad
 |\mathcal K|\le2|W^+||\Phi|^3.                       \tag{5.4}
\]

In particular, if beta_j->infinity, kappa_j->0 and a_j^2>=T_{+,j}, the
actual supplied solutions, with sufficiently small allowances, satisfy

\[
 \|t_{\Phi_j}\|_{L^4_{\rm avg}}+
 \|\nabla t_{\Phi_j}\|_{L^2_{\rm avg}}\le C,
 \quad \fint|t_{\Phi_j}|^2\longrightarrow128/81,
                                                        \tag{5.5}
\]
\[
 \boxed{\|D^-_{3A_j}t_{\Phi_j}\|_{L^q_{\rm avg}}
          \longrightarrow0\quad(1\le q<2).}            \tag{5.6}
\]

This produces an actual opposite-chirality twisted spinor with nonvanishing
mean mass and a vanishing weak Dirac residual. It is not a new monopole
solution: no curvature equation for its quadratic map has been established.

**Proof of the differential identity.** At a normal orthonormal frame,
the product rule for (5.3) splits into

\[
 Q=\sum_{ji}c_jc_i\{P_j\otimes w_i+
                       \Phi\otimes(P_j\wedge P_i)\},
 \quad H=\sum_{ji}c_jc_i\Phi\otimes(\Phi\wedge\nabla_jP_i).
\]

The two-dimensional determinant identity
Phi(P_j wedge P_i)=P_j w_i-P_i w_j and D_A Phi=0 give
Q=-4 sum_i P_i tensor w_i, using c_jc_i+c_ic_j=-2delta_ij.
The symmetric part of H is
Phi tensor(Phi wedge nabla^*nabla Phi), which vanishes because the
same weighted spinor equation makes nabla^*nabla Phi a scalar multiple
of Phi. The remaining part is exactly

\[
 \mathcal K=\tfrac12\sum_{ji}c_jc_i\Phi\otimes
                   (\Phi\wedge R^{S^+}_{ji}\Phi).       \tag{5.7}
\]

The central determinant-curvature term vanishes in the wedge. Clifford
action on S^+ annihilates the anti-self-dual first-pair component, so the
Ricci-off-diagonal block also disappears. For a real orthonormal basis
sigma_alpha of Lambda+, set J_alpha=c(sigma_alpha)/sqrt(2). The scalar
curvature term disappears by
sum_alpha J_alpha Phi tensor(Phi wedge J_alpha Phi)=0. With the convention
D_A^2=nabla^*nabla+s/4+c(F_A)/2, the remaining expression is

\[
 \mathcal K=-\sum_{\alpha\beta}W^+_{\alpha\beta}
                  J_\alpha\Phi\otimes(\Phi\wedge J_\beta\Phi).
\]

The matrix with columns J_alpha Phi has operator norm sqrt(2)|Phi|,
and the vector of wedges has norm sqrt(2)|Phi|^2. This proves (5.4).
Equivalently (5.7), whose sign does not depend on identifying a curvature
operator convention, can be used throughout.

Here are explicit pointwise checks of the remaining representation facts.
On S+->S-, take Clifford matrices

\[
 C_1=I,\quad C_2=\operatorname{diag}(i,-i),\quad
 C_3=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad
 C_4=\begin{pmatrix}0&-i\\-i&0\end{pmatrix}.
\]

On S-->S+ use -C_i^*. Thus c(e12+e34)=-2i diag(1,-1) on S+.
At a nonzero spinor use a unitary frame Phi=sqrt(rho)u and write
nabla Phi=alpha u+beta v, nabla u=i gamma u+b v. In the notation
Omega=sqrt(2)psi/rho, differentiation gives

\[
 |\nabla\Omega|^2=8|b|^2,\quad |d\Omega|^2=8|b_L|^2,
 \quad |t_\Phi|^2=2\rho^3|b_N|^2
    =\frac{\rho^3}{4}(|\nabla\Omega|^2-|d\Omega|^2).
                                                        \tag{5.8}
\]

Here b_N is the component in ker[c(.)v] and b_L its Hermitian-orthogonal
complement. For closed Omega this is precisely the non-Kaehler intrinsic
torsion component, with the appropriate conjugate-bundle convention.
Thus (5.3) is not merely an arbitrary cubic field with the same Chern class.

Let zeta=<Phi,nabla Phi>, with the Hermitian pairing linear in its second
entry. The Dirac equation implies |beta_L|<=|alpha|. Each complex
isotropic subspace has beta_N dot beta_N=beta_L dot beta_L=0. Therefore

\[
 \left|\sum_iP_i\otimes w_i\right|^2
   =\rho(|\alpha\mathbin\cdot\beta|^2+|\beta\mathbin\cdot\beta|^2)
   \le5|\zeta|^2|\nabla\Phi|^2,\qquad
 \fint|\zeta|^2\le D_0/(4V).                          \tag{5.9}
\]

The last inequality follows from (3.3) and
|zeta|^2=|drho|^2/4+|gamma_original|^2. This notation distinguishes
gamma_original=Im<Phi,nabla Phi> from the normalized-frame gamma above.
The inherited bounded-spinor Hessian and fourth-power gradient estimates
are uniform when a^2>=T+ and kappa<=1. Directly differentiating (5.3)
then gives the bounds in (5.5). Holder and (5.4), (5.9) yield

\[
 \|D^-_{3A}t_\Phi\|_{L^{4/3}_{\rm avg}}
 \le2\|\Phi\|_\infty^3\|W^+\|_{L^2_{\rm avg}}
   +4\sqrt5\|\zeta\|_{L^2_{\rm avg}}
                     \|\nabla\Phi\|_{L^4_{\rm avg}}
 \le C(\sqrt\kappa+\beta^{-1})+o(1).                  \tag{5.10}
\]

The same expression is bounded in L2, since
|zeta|<=|Phi||nabla Phi|. Interpolation proves (5.6).
For the mass limit, (5.8) also gives

\[
 |t_\Phi|^2=\frac\rho2\left(|\nabla\psi|^2-|d\rho|^2
                -|d\psi-\rho^{-1}d\rho\wedge\psi|^2\right).
\]

Its difference from (rho/2)|nabla psi|^2 has absolute value bounded
by C(|drho|^2+|dpsi|^2), also through spinor zeros by the polynomial
identity and continuity. Its average is O(kappa). Now rho->4/3 in L2,
nabla psi is bounded in L4, and the previous Hodge computation gives
avg|nabla psi|^2->64/27. The mass limit is consequently 128/81. QED.

The remaining critical quantity is particularly explicit:

\[
 \|D^-_{3A}t_\Phi\|_{L^2_{\rm avg}}^2
 \le C\left(\fint|W^+|^2+
               \fint|\zeta|^2|\nabla_A\Phi|^2\right).   \tag{5.11}
\]

Existing L2 smallness of zeta and L4 boundedness of nabla Phi do not
make the product in (5.11) small. Nor does the mean mass limit make
t_Phi nowhere zero. Thus (5.6) is a weak Dirac bridge, not the claimed
zero-end exclusion or a characteristic-number vanishing theorem.

### 5.2 What the opposite-spinor topological argument must additionally pay

Writing the curvature of B=S^- tensor L as
F_B=Omega_-spin+(3/2)F_A I, the same conventions give

\[
 16\pi^2c_2(F_B)=\bigl(2|W^-|^2+s^2/24-|\operatorname{Ric}^\circ|^2/2
                     +9|F_A^+|^2-9|F_A^-|^2\bigr)d\mu,
\]
\[
 \|F_B\|_2^2=8\pi^2c_2(B)[M]+\tfrac12P+9\|F_A^-\|_2^2. \tag{5.12}
\]

At the zero endpoint, a^2>=T+ bounds avg|F_A-|^2 above by 2/9+o(1).
It does **not** bound avg|F_B|^2 universally, because c_2(B)/V,
equivalently the opposite Weyl energy, need not be bounded above.
The uniform bound in (5.5) concerns the derivative of a particular
section, not the curvature of its whole bundle.

For any smooth section t of a Hermitian rank-two bundle, the construction
of (4.7) applied to t/|t| and a cutoff in |t|/delta gives

\[
 |c_2(B)[M]|\le C\left(
    \int_{\{|t|<2\delta\}}|F_B|^2+
    \delta^{-4}\int_{\{\delta<|t|<2\delta\}}|\nabla t|^4\right).
                                                        \tag{5.13}
\]

For clarity, |dchi|<=C|nabla t|/delta and
|nabla(t/|t|)|<=C|nabla t|/delta on the transition layer; (4.7) and
Young's inequality give exactly (5.13). The cutoff is constant near
zeros, so no zero-set transversality is assumed. Formula (5.13) isolates
the missing terms rather than discarding boundary flux.

Under a^2>=T+ and r->0, (5.1)--(5.2) give
c_2(B)/V>=5/(12pi^2)+o(1). Hence decay of both terms in (5.13), divided
by V, would close the topological contradiction. Proposition 7 by itself
supplies neither: nabla t is bounded in L2, not L4, and W- may concentrate
where t is small. These facts distinguish the actual weak Dirac bridge
from an already completed weak-error rigidity theorem.

## 6. Scope correction for the inherited harmonic-zero example

The owner's new report correctly narrows its previous interpretation of
I37. In [the original proof](20260924_harmonic_zero_scale.md), lines
422--432, the scaled zero-circle construction explicitly has divergent
pointwise Ricci error and does not establish r+q->0. It cannot refute
automatic whole-core matching from the full near-Einstein PDE input.

In fact the particular nonzero-Ricci model fixed in that construction
gives a little more. On a fixed interior open set U of the model with
int_U|Ric(g_tilde)|^2>0, its exact rescaling g_rho=rho^2 g_tilde satisfies

\[
 \int_{\rho U}|\operatorname{Ric}(g_\rho)+g_\rho|^2
 =\int_U|\operatorname{Ric}(\widetilde g)+\rho^2\widetilde g|^2
 \longrightarrow\int_U|\operatorname{Ric}(\widetilde g)|^2>0.
\]

Since total volume tends to the fixed exterior volume, liminf r_rho>0.
This calculation concerns that chosen model, not every possible harmonic
zero construction. The original sufficient scale criterion remains valid;
its automatic derivation under complete PDE input remains an open problem.


END COMPLETE SOURCE
