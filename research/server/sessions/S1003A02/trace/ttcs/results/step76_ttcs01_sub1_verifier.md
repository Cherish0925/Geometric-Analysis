# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md",
    "Sessions/S1003A02/workspace/notes/step76_Q4_chern_weil_density_and_prolongation.md",
    "Sessions/S1003A02/workspace/scripts/step75_torsion_symbol_checks.py",
    "Sessions/S1003A02/workspace/data/step75_torsion_symbol_checks.json",
    "Sessions/S1003A02/workspace/scripts/step76_cw_density_on_pair.py",
    "Sessions/S1003A02/workspace/data/step76_cw_density_on_pair.json",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Knowledge/objects/papers/Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7--68f3db154d35/object.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Verify, as a careful differential geometer, the almost-Kaehler torsion results in the Step-75 note and Section 1 of the Step-76 note, using AAD's conventions (the two Knowledge papers) and A01's Step-59 data. Context: closed negative Goldberg problem (does a closed almost-Kaehler Einstein 4-manifold with s<0 have to be Kaehler?). Check concretely: (A) eq (75.2) d_b alpha = -R(J phi + i phi) for alpha=a+iJa from AAD (26); the identification of the Lambda^- part of d_b alpha with the J-anti-invariant Ricci tensor Ric'' (Theorem 75.H(a)); injectivity of the principal symbol of the primitive (1,1) projection P (75.H(b)); the five-piece U(2) splitting of nabla^b alpha and which pieces correspond to W_2^+ (eta) and W_3^+ (75.H(c)), including whether the extra |a|^2 term really appears where claimed; the sharp refined Kato constant k^2=3/4 (75.H(d)). (B) Proposition 75.I: det_R Df = |c|^4 - |c|^2(||S||^2-||A||^2) + |det B|^2 for f = cz + B zbar with B=S+A, and the stated sign consequences; whether index is correctly the sign of this determinant with orientation conventions of E. (C) Section 3 of the Step-75 note: is the 'decay principle' argument logically valid as stated, and is the claim that weighted Bochner arguments are index-blind correct? (D) Step-76 Section 1: the claim that the Lambda^- (su(2)) part of the canonical Hermitian connection curvature equals the Levi-Civita one because [m,m] lies in R Omega; formula (76.1) db = R(Omega) - a^Ja and its sign; formula (76.2) c2(E) = (9/4) p1(Lambda^+) - (1/4) p1(Lambda^-); the density (76.3) 4pi^2 c2(E) = 42 - 27q/8 + 9|eta|^2/4 + |W^-|^2/2 at s=-12, and the transgression identity (76.4) relating it to the AAD balance |eta|^2+2|W3|^2+3q^2/16-3q/2. The script/JSON confirm (76.4) identically on A01's pair, given the stated normalizations; judge whether that confirmation actually pins down the sign in (76.1) or whether an alternative sign could also be consistent. State corrections with exact replacement formulas. Do not invent literature.

## Output

# Scientific verification memo

## 1. Torsion equation and half-twistor decomposition

Let
\[
\alpha=a+iJa,\qquad u:=J\phi+i\phi .
\]
Since
\[
d_b\alpha=d\alpha-ib\wedge\alpha,
\]
direct expansion gives
\[
d_b\alpha
=(da-Ja\wedge b)+i\bigl(d(Ja)+a\wedge b\bigr).
\]
AAD’s Ricci identities then give
\[
\boxed{d_b\alpha=-R(J\phi+i\phi)=-R(u).}
\]
Thus (75.2) has the correct sign and is gauge covariant under
\[
\alpha'=e^{i\theta}\alpha,\qquad b'=b+d\theta.
\]

### The \(\Lambda^-\) component

For AAD’s raw Kulkarni–Nomizu extension
\[
\widetilde h(\psi)=h\circ\psi+\psi\circ h,
\]
the Singer–Thorpe block is \(\frac12\widetilde{\operatorname{Ric}_0}\). Consequently the exact formula is
\[
\boxed{(d_b\alpha)^-
=-\frac12\,\widetilde{\operatorname{Ric}^{\prime\prime}}(u).}
\]
If \(\widetilde{\operatorname{Ric}^{\prime\prime}}\) in Step 75 is intended to mean the actual curvature block \(\Lambda^+\to\Lambda^-\), rather than the raw extension above, then its displayed formula is already correct.

The \(J\)-invariant trace-free Ricci component annihilates the \(J\)-anti-invariant plane \(\llbracket\Lambda^{0,2}\rrbracket\); the \(J\)-anti-invariant component gives the entire map from this plane to \(\Lambda^-\). Evaluation on the complex generator \(u\) determines this real map. Hence
\[
(d_b\alpha)^-=0\quad\Longleftrightarrow\quad
\operatorname{Ric}^{\prime\prime}=0.
\]
Since \(\Lambda^-=\Lambda^{1,1}_0\), Theorem 75.H(a) is correct modulo the normalization just described.

### Principal symbol

For real \(\xi\ne0\),
\[
\sigma_\xi(\mathcal P)v=(\xi^{\mathrm{opp}}\wedge v)_0,
\]
where \(\xi^{\mathrm{opp}}\) has type opposite to \(v\in\Lambda^{1,0}\otimes\mathcal L\). Both factors are nonzero and have opposite types, so their wedge is nonzero. If its primitive projection vanished, it would be a multiple of \(\Omega\). This is impossible because \(\xi^{\mathrm{opp}}\wedge v\) is decomposable whereas
\(\Omega\wedge\Omega\ne0\). Thus the symbol is injective. The complex ranks are \(2\to3\), so 75.H(b) is correct.

### Irreducible decomposition: four summands, not five

For the Hermitian covariant derivative preserving the type of \(\alpha\),
\[
T^*_{\mathbb C}\otimes(\Lambda^{1,0}\otimes\mathcal L)
=
(\Lambda^{0,1}\otimes\Lambda^{1,0})\otimes\mathcal L
\oplus
(\Lambda^{1,0}\otimes\Lambda^{1,0})\otimes\mathcal L,
\]
and hence
\[
\boxed{
T^*_{\mathbb C}\otimes(\Lambda^{1,0}\otimes\mathcal L)
=
(\mathbb C\Omega\oplus\Lambda^{1,1}_0
\oplus\Lambda^{2,0}\oplus S^{2,0})\otimes\mathcal L .
}
\]
These have complex ranks \(1,3,1,3\). There are therefore **four** irreducible summands, not five.

Define
\[
\eta:=W^+(\Omega)-\frac{\kappa}{6}\Omega .
\]
Using \(\kappa-s=6|a|^2\), the full curvature decomposition of (75.2) is
\[
\boxed{
d_b\alpha
=
\frac{|a|^2}{2}\,u
-\frac12\langle\eta,u\rangle\,\Omega
-W_3^+(u)
-\frac12\widetilde{\operatorname{Ric}^{\prime\prime}}(u),
}
\]
with the final factor interpreted as above. Thus:

- \(\Lambda^{1,1}_0\) is the \(\operatorname{Ric}^{\prime\prime}\) component;
- the \((1,1)\)-trace is the \(W_2^+\) component, represented by \(\eta\);
- the antisymmetric same-type derivative is \(W_3^+\);
- \(S^{2,0}\) is not seen by \(d_b\alpha\);
- \(\frac12|a|^2u\) is a zeroth-order Nijenhuis/second-fundamental-form term. It is not a fifth summand of \(\nabla^b\alpha\).

The sign of this quadratic term in \(d_b\alpha\) is plus. In \(R(u)\) itself the corresponding term is
\[
\frac{s-\kappa}{12}u=-\frac12|a|^2u.
\]

### Sharp refined Kato constant

In the unitary symbol model,
\[
K=\{(P,Q):P=cI_2,\ Q\in M_2(\mathbb C)\},
\]
so \(\dim_{\mathbb C}K=5\), equivalently \(\dim_{\mathbb R}K=10\). For a unit real rank-one tensor \(\xi\otimes v\), one half of its norm lies in the unrestricted \(Q\)-summand. Projection of the other half onto the scalar matrices contributes at most \(1/4\). Therefore
\[
\sup_{|\xi|=|v|=1}\left|\pi_K(\xi\otimes v)\right|^2
=\frac12+\frac14=\frac34.
\]
Equality occurs for the aligned example \(\xi=dx_1,\ v=e_1\), exactly as in the script. Hence
\[
\boxed{|d|\alpha||\le\frac{\sqrt3}{2}|\nabla^b\alpha|}
\]
is sharp wherever \(\alpha\ne0\). The script’s sampled value and exact aligned value correctly reproduce the analytic result.

---

## 2. Index of a nondegenerate torsion zero

For
\[
f(z)=cz+B\bar z,
\]
the complexified real Jacobian has block matrix
\[
\begin{pmatrix}
cI&B\\
\bar B&\bar cI
\end{pmatrix}.
\]
Its determinant equals
\[
\det_{\mathbb R}Df
=\det\bigl(|c|^2I-\bar BB\bigr).
\]
Writing \(B=S+A\), with \(S^T=S\) and \(A^T=-A\),
\[
\operatorname{tr}(\bar BB)=\|S\|^2-\|A\|^2,\qquad
\det(\bar BB)=|\det B|^2.
\]
Therefore
\[
\boxed{
\det_{\mathbb R}Df
=
|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2 .
}
\]
Proposition 75.I and the 4000 symbolic/numerical comparisons are correct.

Let
\[
t=\|S\|^2-\|A\|^2,\qquad d=|\det B|,\qquad x=|c|^2.
\]
For a nondegenerate zero, index \(-1\) occurs exactly when
\[
x^2-tx+d^2<0.
\]
Equivalently,
\[
\boxed{
t>2d,\qquad
\frac{t-\sqrt{t^2-4d^2}}2
<x<
\frac{t+\sqrt{t^2-4d^2}}2 .
}
\]
Thus the note’s inequality \(t\ge2d\) is a valid necessary statement but can be sharpened to \(t>2d\).

The listed sufficient cases for index \(+1\) are correct:

- \(c=0\), provided \(B\) is invertible;
- \(S=0\);
- \(\|S\|\le\|A\|\).

Both determinant signs occupy open subsets of the nondegenerate jet space, so “generic” should not be used in the topological sense for either sign.

### Orientation

The source orientation is the almost-complex orientation determined by \(\Omega^2/2\). The target is the complex orientation of the complex rank-two bundle
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2}.
\]
Unitary changes of source frame and complex changes of target frame have positive real determinant. Replacing a complex structure by its conjugate on a complex rank-two space also preserves the underlying real orientation. Hence the local index is indeed
\[
\operatorname{ind}_p(T)=\operatorname{sign}\det_{\mathbb R}Df
\]
with the coordinates used in the script.

---

## 3. Radial weights and the decay argument

### Radial singular weights do not recover the index sign

The central observation is correct: a zero-localized term depending only on \(|\alpha|\) cannot distinguish \(L\) from \(OL\), where \(O\) is an orientation-reversing orthogonal map of the target. These have the same norm profile
\[
|OLx|=|Lx|
\]
but opposite Jacobian signs.

The specific example in Step 75,
\[
\Delta|Lx|^{-2}=-c\,|\det L|^{-1}\delta_0,
\]
is not correct for a general invertible \(L\). With \(\Delta=\sum\partial_i^2\), the delta coefficient is
\[
\boxed{
-2\int_{S^3}|L\theta|^{-2}\,d\theta .
}
\]
It depends on the singular values of \(L\), not only on \(|\det L|\). Moreover, unless \(L\) is conformal, \(\Delta|Lx|^{-2}\) also has a nonzero homogeneous term away from the origin. The scaling example \(L=tI\) already shows the discrepancy:
\[
\Delta|t x|^{-2}
=-4\pi^2t^{-2}\delta_0,
\]
whereas \(|\det(tI)|^{-1}=t^{-4}\).

Thus the “index-blind” conclusion is valid, while the displayed dependence on \(|\det L|\) should be replaced by dependence on \(L^TL\), equivalently on the singular values.

### Decay principle

The argument is valid under the following precise hypotheses:

1. the closed-manifold identity comes from a pointwise relation
   \[
   \Phi=\operatorname{div}V
   \]
   valid for every almost-Kähler Einstein solution;
2. \(V\) is globally defined on the exhaustion, or its end flux is gauge independent;
3. the flux through the radial level hypersurfaces tends to zero;
4. the relevant improper integral converges. If \(\Phi\ge0\), monotone exhaustion and vanishing flux suffice.

Under these assumptions the complete strict A01 pair satisfies
\[
\int\Phi=0.
\]
Consequently such a \(\Phi\) cannot simultaneously be pointwise \(\ge0\) and vanish only when \(T=0\).

This is a conditional statement for each concrete \(V\), not a general theorem about all smooth integral identities. A current whose end flux does not decay can distinguish a compact manifold from the A01 geometry. The AAD transgression is a valid example with decaying end flux: Step 59 gives absolute convergence of the four constituent integrals and total integral zero.

---

## 4. Canonical connection and \(c_2(E)\)

### Connection splitting

AAD’s first canonical Hermitian connection is
\[
\bar\nabla=\nabla-\frac12J(\nabla J).
\]
Thus, if
\[
A=-\frac12J\nabla J,
\]
the correct relation is
\[
\boxed{\bar\nabla=\nabla+A,}
\]
not \(\nabla=\bar\nabla+A\).

The difference tensor lies in
\[
\mathfrak m=\llbracket\Lambda^{0,2}\rrbracket\subset\Lambda^+.
\]
Because the two \(\mathfrak{su}(2)\) factors \(\Lambda^+\) and \(\Lambda^-\) commute, \(\mathfrak m\) acts trivially on \(\Lambda^-\). Hence the connections induced by \(\nabla\) and \(\bar\nabla\) on \(\Lambda^-\) are actually identical. Also,
\[
[\mathfrak m,\mathfrak m]\subset\mathbb R\Omega.
\]
Therefore the statement that the \(\Lambda^-\) Pontryagin density is unchanged is correct.

### Sign of \(db\)

AAD’s equations give
\[
\boxed{db=a\wedge Ja-R(\Omega).}
\]
Equivalently, their canonical Chern form is
\[
\boxed{\gamma_J=-db=R(\Omega)-a\wedge Ja.}
\]
Thus (76.1) has the opposite sign.

The scalar contraction is
\[
\langle-db,\Omega\rangle=\frac14(s+s^*),
\qquad
\langle db,\Omega\rangle=-\frac14(s+s^*).
\]
This agrees with AAD’s statement that \(-db/(2\pi)\) represents \(c_1(M,J)\).

For an Einstein metric,
\[
\gamma_J^+
=\left(\frac s4+\frac q8\right)\Omega+\eta,
\qquad
\gamma_J^-=-(a\wedge Ja)^-.
\]
Equivalently,
\[
\boxed{
(db)^+=-\left(\frac s4+\frac q8\right)\Omega-\eta,
\qquad
(db)^-=(a\wedge Ja)^-.
}
\]
The Step 76 formulas for the self-dual and anti-self-dual pieces are formulas for \(-db=\gamma_J\), not for \(db\).

### Characteristic-class identity

Using
\[
e(TM)=\frac14\bigl(p_1(\Lambda^+)-p_1(\Lambda^-)\bigr),
\qquad
c_1^2(TM,J)=p_1(\Lambda^+),
\]
and
\[
c_2(E)=c_2(TM,J)+2c_1^2(TM,J),
\]
one obtains
\[
\boxed{
c_2(E)=\frac94p_1(\Lambda^+)-\frac14p_1(\Lambda^-).
}
\]
Formula (76.2) is correct.

Since changing \(db\) to \(-db\) does not change \(db\wedge db\),
\[
p_1(\Lambda^+,\bar\nabla)
=\frac1{4\pi^2}db\wedge db
\]
remains correct.

### Density at \(s=-12\)

Using
\[
|(a\wedge Ja)^\pm|^2=\frac{q^2}{32},
\]
one gets
\[
4\pi^2p_1(\Lambda^+,\bar\nabla)
=
\left(18-\frac32q+|\eta|^2\right)d\mu,
\]
while the unchanged \(\Lambda^-\) connection gives
\[
4\pi^2p_1(\Lambda^-,\bar\nabla)
=
\left(-6-2|W^-|^2\right)d\mu.
\]
Combining these with (76.2),
\[
\boxed{
4\pi^2c_2(E)_{\bar\nabla}
=
\left(
42-\frac{27}{8}q+\frac94|\eta|^2+\frac12|W^-|^2
\right)d\mu.
}
\]
Thus (76.3) is correct despite the sign error in (76.1).

For the Levi-Civita representative,
\[
4\pi^2c_2(E)_{\mathrm{LC}}
=
\left(15+\frac92|W^+|^2+\frac12|W^-|^2\right)d\mu.
\]
Using
\[
|W^+|^2=\frac{\kappa^2}{24}+|\eta|^2+|W_3^+|^2,
\qquad
\kappa=-12+\frac32q,
\]
gives
\[
\boxed{
4\pi^2\bigl(c_2(E)_{\mathrm{LC}}-c_2(E)_{\bar\nabla}\bigr)
=
\frac94\left(
|\eta|^2+2|W_3^+|^2+\frac3{16}q^2-\frac32q
\right)d\mu .
}
\]
Formula (76.4) is correct.

### What the A01 script establishes

The script exactly verifies, for the Step 59 functions,

- \(X_1+X_2=1\);
- \(W^+(\Omega)\)’s \(\Omega\)-coefficient is \(\kappa/6\);
- the stated norm decomposition of \(W^+\);
- the algebraic identity (76.4);
- the explicit density
  \[
  \frac{6(567p^8+783p^6+297p^4+165p^2-20)}{(3p^2+1)^4}.
  \]

Writing \(x=p^2\), differentiation gives a numerator proportional to
\[
81(1-x)^2(5-x)>0\qquad (1/9\le x<1),
\]
so the density indeed increases from \(6\) at the bolt to \(42\) at the end.

The script does **not** determine the sign of \(db\). Every quantity used there involves \(db\wedge db\), hence is unchanged by \(db\mapsto-db\). The sign is fixed instead by AAD’s formulas
\[
db=a\wedge Ja-R(\Omega),\qquad \gamma_J=-db.
\]

## Consolidated corrections

The substantive replacements are:

\[
(d_b\alpha)^-
=-\frac12\widetilde{\operatorname{Ric}^{\prime\prime}}(J\phi+i\phi)
\]
when AAD’s raw \(\widetilde{\phantom h}\) convention is used;

\[
\nabla^b\alpha:
\quad 3+1+1+3
\]
is a four-summand decomposition, with \(|a|^2u/2\) a zeroth-order term;

\[
\det_{\mathbb R}Df<0
\quad\Longrightarrow\quad
\|S\|^2-\|A\|^2>2|\det B|;
\]

\[
\Delta|Lx|^{-2}\text{ has delta coefficient }
-2\int_{S^3}|L\theta|^{-2}d\theta;
\]

\[
\boxed{db=a\wedge Ja-R(\Omega),\qquad -db=R(\Omega)-a\wedge Ja.}
\]

All remaining central formulas—injective symbol, \(k^2=3/4\), determinant identity, orientation of the torsion index, (76.2), (76.3), and (76.4)—are mathematically consistent with the supplied AAD conventions and A01 data.