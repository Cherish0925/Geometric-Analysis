# Standard positive resolutions and an exotic Kähler–Einstein comparison

22 September 2026. No previously undecided standard smooth type receives an
Einstein metric in this note. The proposed transfer from a complex surface is
more sharply settled: for the mixed product resolutions and standard
\(M_r=\#_r(S^2\times S^2)\), \(r\ge2\), it is impossible, not an unknown
smooth-identification problem. This does not exclude a real, non-Kähler
Einstein metric on these manifolds.

## 1. An obstruction to the proposed identification

**Proposition.** None of the following standard smooth manifolds admits a
symplectic structure, or an integrable complex structure, in either orientation:
\[
 M_r\ (r\ge2),\qquad
 2\mathbb{CP}^2\#4\overline{\mathbb{CP}}{}^2,
 \qquad3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2.
\tag{1}
\]
The reversed \(4\mathbb{CP}^2\#2\overline{\mathbb{CP}}{}^2\) row is included.

**Proof.** In either orientation, each manifold splits into two summands
having positive \(b_2^+\). Its ordinary Seiberg–Witten invariants vanish.
This is the connected-sum argument in
[Witten, pp. 12–13 of the preprint](https://arxiv.org/pdf/hep-th/9411102).
A symplectic structure would have a canonical Spin\(^c\) class with invariant
\(\pm1\), by
[Taubes, Main Theorem, p. 809](https://www.intlpress.com/site/pub/files/_fulltext/journals/mrl/1994/0001/0006/MRL-1994-0001-0006-a015.pdf).
Here \(b_2^+>1\), so there is no chamber qualification. Finally \(b_1=0\);
an integrable complex structure would be Kähler by
[Buchdahl, Theorem 12](https://www.numdam.org/article/AIF_1999__49_1_287_0.pdf),
and hence symplectic. This is a contradiction. \(\square\)

Consequently, a homeomorphic projective surface cannot supply a pullback
Einstein metric on (1). The same obstruction applies to any projective smooth
fibre proposed as the result of a simultaneous resolution or algebraic
smoothing: a claimed diffeomorphism to (1) would pull back its Kähler form.
Neither changing complex structure nor reversing orientation removes this
obstruction. It leaves the underlying real Einstein equation open.

For \(M_r\), the elementary data are
\[
 Q=rH,\quad \chi=2+2r,\quad\tau=0,\quad\widehat A=0,
 \quad (\chi+\tau)/4=(r+1)/2.
\tag{2}
\]
Even \(r\) already fails almost-complex index integrality. Odd \(r\) passes
that test; the vanishing versus nonvanishing Seiberg–Witten invariant is the
additional obstruction. Rank, signature, spin parity and Dirac index alone
do not distinguish the standard structure from the complex example below.

## 2. One actual exotic Einstein control, with its exact rank

Take the classical Galois closure
\[
 X=Y_0(7,4)=(\mathbb{CP}^1\times\mathbb{CP}^1,\mathcal O(7,4))_{\rm Gal}
\]
of a generic projection to \(\mathbb{CP}^2\).
[Teicher, Theorem 5.8(a)(i)](https://arxiv.org/pdf/math/9904090)
asserts that this is simply connected, spin, of general type, and has zero
signature. Section 5 explicitly establishes smoothness of the Galois closure
and the canonical-bundle formula; Lemma 6.1 gives the branch degree. They yield
\[
 n=56,\qquad m=146,\qquad
 K_X=(m/2-3)f^*H=70f^*H.
\tag{3}
\]
The map \(f:X\to\mathbb{CP}^2\) is finite of degree \(56!\), so this canonical
bundle is ample. Substitution in Teicher's Theorem 5.2 gives
\[
 K_X^2=4900\cdot56!,\qquad c_2(X)=2450\cdot56!,\qquad
 r_*=1225\cdot56!-1.
\tag{4}
\]
These substitutions are independently checked by
[round20_global_check.py](round20_global_check.py); they are arithmetic
verification, not a reproof of the Galois-cover theorem.

The Aubin–Yau existence theorem gives a smooth negative Kähler–Einstein metric
on \(X\); see
[Yau, Theorem 4 and its consequence, pp. 383–384](https://doi.org/10.1002/cpa.3160310304).
Its even indefinite unimodular form is \(r_*H\). The classification theorem
of [Freedman](https://doi.org/10.4310/jdg/1214437136) therefore makes \(X\)
homeomorphic to \(M_{r_*}\), while Proposition 1 proves they are not
diffeomorphic, even without prescribing orientation. Thus this known exact
Einstein metric does not determine Einstein existence on the standard
connected sum. No counterpart at every odd rank, particularly rank three,
is asserted.

## 3. The positive Ricci defect records the smooth distinction

Use the existing convention
\[
 e_+(N)=\inf_g\|g^{-1}\operatorname{Ric}_g-I\|_{L^\infty,\rm op}.
\]
An elementary scaling observation gives
\[
 0\le e_+(N)\le1,\qquad
 e_+(N)<1\ \Longleftrightarrow\ N\text{ admits }\operatorname{Ric}>0.
\tag{5}
\]
Indeed \((tg)^{-1}\operatorname{Ric}_{tg}=t^{-1}g^{-1}\operatorname{Ric}_g\),
so \(t\to\infty\) proves the upper bound. A defect below one makes every
Ricci eigenvalue positive. Conversely, if all eigenvalues lie in
\([a,b]\), \(0<a\le b\), rescale by \(t=(a+b)/2\); the defect becomes
\((b-a)/(b+a)<1\).

The canonical invariant of \(X\) obstructs positive scalar curvature
([Witten, Section 3](https://arxiv.org/pdf/hep-th/9411102)), hence positive
Ricci curvature. In particular
\[
                  e_+(X)=1,\qquad e_-(X)=0.                 \tag{6}
\]
Classical Sha–Yang positive-Ricci metrics give \(e_+(M_r)<1\) for every
finite \(r\); their exact dimension and rank quantifiers are reproduced in
[Burdick, Theorem 1.4](https://doi.org/10.1016/j.difgeo.2018.11.005).
Thus (6) distinguishes the two smooth structures independently of the
inherited near-Einstein construction. Positive Ricci curvature itself does
not imply \(e_+=0\) or Einstein existence.

There is a relevant inherited qualification. The all-rank spherical
\(A_r\)-double proposition in
[20260912.tex, standard smooth models](skill/research/20260912.tex)
identifies the **standard smooth** \(M_r\) by its extended torus action.
But it explicitly retains a pending independent-review qualification for
the general ADE analytic approximation. It is not an all-rank A1 theorem.
Accordingly, the strengthened comparison \(e_+(M_{r_*})=0\) is conditional
on that analytic extension. The concrete A1 football and four-node product
results of [Round 17](round17_positive.md), including \(M_1\) and \(M_3\),
retain their own stated proof chains.

## 4. Why the other inspected Einstein construction does not bridge the gap

Anderson's sufficiently long toral Einstein Dehn fillings are aspherical:
his [Section 2.1, (2.4)–(2.5)](https://www.math.stonybrook.edu/~anderson/dehn.pdf)
constructs a separate nonpositively curved metric when the filling slopes
have length at least \(2\pi\). In dimension four the core torus injects
\(\mathbb Z^2\) into the fundamental group. These outputs therefore cannot
be homeomorphic to the simply connected manifolds (1). This argument does
not require the constructed Einstein metric itself to have nonpositive
sectional curvature.

The similarly titled
[Gursky–Viaclovsky connected-sum construction](https://arxiv.org/pdf/1303.0827)
constructs critical metrics for a quadratic curvature functional; the paper
explicitly explains on p. 8 why its connected-sum metrics are not Einstein.
It does not provide the missing exact output either.

The construction of \(X\), the gauge-theoretic obstructions, and (5) are
classical or elementary. The present contribution is their explicit
comparison with the actual marked standard resolutions, including the
all-rank analytic qualification. No new Einstein existence or all-sign
nonexistence theorem on an undecided standard type is claimed.
