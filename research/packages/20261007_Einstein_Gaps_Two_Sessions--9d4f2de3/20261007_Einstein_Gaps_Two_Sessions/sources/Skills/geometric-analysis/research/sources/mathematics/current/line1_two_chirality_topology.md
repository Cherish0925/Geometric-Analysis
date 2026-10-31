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
