# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 76,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step76_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step76_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify, as a careful differential geometer, the almost-Kaehler torsion results in the Step-75 note and Section 1 of the Step-76 note, using AAD's conventions (the two Knowledge papers) and A01's Step-59 data. Context: closed negative Goldberg problem (does a closed almost-Kaehler Einstein 4-manifold with s<0 have to be Kaehler?). Check concretely: (A) eq (75.2) d_b alpha = -R(J phi + i phi) for alpha=a+iJa from AAD (26); the identification of the Lambda^- part of d_b alpha with the J-anti-invariant Ricci tensor Ric'' (Theorem 75.H(a)); injectivity of the principal symbol of the primitive (1,1) projection P (75.H(b)); the five-piece U(2) splitting of nabla^b alpha and which pieces correspond to W_2^+ (eta) and W_3^+ (75.H(c)), including whether the extra |a|^2 term really appears where claimed; the sharp refined Kato constant k^2=3/4 (75.H(d)). (B) Proposition 75.I: det_R Df = |c|^4 - |c|^2(||S||^2-||A||^2) + |det B|^2 for f = cz + B zbar with B=S+A, and the stated sign consequences; whether index is correctly the sign of this determinant with orientation conventions of E. (C) Section 3 of the Step-75 note: is the 'decay principle' argument logically valid as stated, and is the claim that weighted Bochner arguments are index-blind correct? (D) Step-76 Section 1: the claim that the Lambda^- (su(2)) part of the canonical Hermitian connection curvature equals the Levi-Civita one because [m,m] lies in R Omega; formula (76.1) db = R(Omega) - a^Ja and its sign; formula (76.2) c2(E) = (9/4) p1(Lambda^+) - (1/4) p1(Lambda^-); the density (76.3) 4pi^2 c2(E) = 42 - 27q/8 + 9|eta|^2/4 + |W^-|^2/2 at s=-12, and the transgression identity (76.4) relating it to the AAD balance |eta|^2+2|W3|^2+3q^2/16-3q/2. The script/JSON confirm (76.4) identically on A01's pair, given the stated normalizations; judge whether that confirmation actually pins down the sign in (76.1) or whether an alternative sign could also be consistent. State corrections with exact replacement formulas. Do not invent literature.

## Integrated Scientific Memo

# Verification memo: Step 75 and Step 76 §1

The principal torsion equation, elliptic symbol, refined Kato constant, zero-index determinant, and Chern–Weil densities survive verification. The necessary corrections are: a Ricci-block normalization, the four—not five—gradient summands, the placement of the quadratic torsion term, the sign of \(db\), and the scope of the claims about weighted Bochner formulas and decay. In particular, the Step-76 script **cannot determine the overall sign of \(db\)**.

Throughout, use AAD’s form norms, \(|\Omega|^2=|\phi|^2=2\), and write
\[
u=J\phi+i\phi,\qquad \alpha=a+iJa,\qquad q=4|a|^2,
\qquad \eta=W^+(\Omega)-\frac{\kappa}{6}\Omega.
\]

## A. Torsion equation and Theorem 75.H

### 1. Equation (75.2) is correct

Expanding the definition gives
\[
d_b\alpha
=(da-Ja\wedge b)+i\bigl(d(Ja)+a\wedge b\bigr).
\]
AAD-LM (23), equivalently AAD-LR (12), therefore yields
\[
\boxed{d_b\alpha=-R(u).}
\]
It is gauge covariant under
\[
\alpha'=e^{i\theta}\alpha,\qquad b'=b+d\theta,\qquad u'=e^{i\theta}u.
\]

Here \(J\alpha=-i\alpha\), so \(\alpha(JX)=i\alpha(X)\): \(\alpha\) has the usual \((1,0)\) type. Correspondingly, \(u\) has type \((0,2)\). A01’s conjugate coefficient convention leads to the same symbol and index calculations.

### 2. The \(\Lambda^-\) component detects exactly \(\operatorname{Ric}''\)

The only curvature block mapping \(\Lambda^+\) to \(\Lambda^-\) is the traceless Ricci block. Its restriction to the anti-invariant plane detects precisely the \(J\)-anti-invariant Ricci tensor; the invariant trace-free Ricci component annihilates that plane. Thus
\[
\boxed{(d_b\alpha)^-=0\iff \operatorname{Ric}''=0.}
\]

There is a normalization qualification. AAD-LM defines the **raw** extension by
\[
\widetilde h(\psi)=h\circ\psi+\psi\circ h,
\]
and its explicit Singer–Thorpe matrix has off-diagonal block \(\frac12\widetilde{\operatorname{Ric}_0}\). With this definition, replace 75.H(a) by
\[
\boxed{
(d_b\alpha)^-
=-\frac12\widetilde{\operatorname{Ric}''}(u).
}
\]
If Step 75’s tilde denotes the actual curvature block instead, its formula is already correct. The equivalence is unaffected.

### 3. The principal symbol is injective

For real \(\xi\ne0\),
\[
\sigma_\xi(\mathcal P)v=(\xi^{0,1}\wedge v)_0,
\qquad v\in\Lambda^{1,0}\otimes\mathcal L.
\]
For \(v\ne0\), the wedge is nonzero and decomposable. If its primitive projection vanished, it would be a multiple of \(\Omega\), which is impossible because
\[
(\xi^{0,1}\wedge v)^2=0,\qquad \Omega^2\ne0.
\]
Thus 75.H(b) is correct: this is an overdetermined elliptic operator of complex ranks \(2\to3\).

### 4. Correct gradient splitting and exact location of \(|a|^2\)

The derivative preserving the type of \(\alpha\) must be specified:
\[
D\alpha:=\bar\nabla\alpha-ib\otimes\alpha,
\qquad
\bar\nabla=\nabla-\frac12J\nabla J.
\]
It has **four** irreducible \(U(2)\)-summands:
\[
\boxed{
T^*_{\mathbb C}\otimes(\Lambda^{1,0}\otimes\mathcal L)
=
\bigl(\Lambda^{1,1}_0\oplus\mathbb C\Omega
\oplus\Lambda^{2,0}\oplus S^{2,0}\bigr)\otimes\mathcal L,
}
\]
of complex ranks \(3+1+1+3=8\).

The curvature identity itself decomposes as
\[
\boxed{
d_b\alpha
=
\frac{|a|^2}{2}u
-\frac12\langle\eta,u\rangle\Omega
-W_3^+(u)
-\frac12\widetilde{\operatorname{Ric}''}(u).
}
\tag{A.1}
\]
The inner product is extended complex bilinearly here.

Crucially, \(|a|^2u/2\) and \(W_3^+(u)\) lie in **opposite type lines**. The former is the algebraic \((0,2)\) Nijenhuis component, not part of the same-type antisymmetric gradient.

This can be checked directly. At a point choose
\[
\Omega=e^{12}+e^{34},\quad
\phi=e^{13}-e^{24},\quad J\phi=e^{14}+e^{23},\quad a=t e^1.
\]
For \(A=\bar\nabla-\nabla=-\frac12J\nabla J\), its action on \(\alpha\) gives
\[
\operatorname{Alt}(A\otimes\alpha)
=-\frac{t^2}{2}(J\phi+i\phi).
\]
Hence the exact replacement is
\[
\boxed{
\operatorname{Alt}(D\alpha)
=d_b\alpha-\frac{|a|^2}{2}u
=
-\frac12\langle\eta,u\rangle\Omega
-W_3^+(u)
-\frac12\widetilde{\operatorname{Ric}''}(u).
}
\tag{A.2}
\]

Therefore:

| Gradient summand | Exterior-derivative image |
|---|---|
| \(\Lambda^{1,1}_0\) | \(-\frac12\widetilde{\operatorname{Ric}''}(u)\) |
| \(\mathbb C\Omega\) | \(-\frac12\langle\eta,u\rangle\Omega\), i.e. \(W_2^+\) |
| \(\Lambda^{2,0}\) | \(-W_3^+(u)\), **without** a quadratic correction |
| \(S^{2,0}\) | invisible to alternation |

In AAD’s \((\lambda,\mu)\) notation,
\[
W_3^+(u)=(-\lambda+i\mu)(J\phi-i\phi).
\]
The quadratic term is instead
\[
\boxed{(d_b\alpha)^{0,2}=N(\alpha)=\frac{|a|^2}{2}u.}
\]

Thus 75.H(c) needs replacement, not merely a corrected piece count. Its spinorial interpretation can describe the symbol-level Dirac/twistor decomposition, but identifying a particular Levi-Civita twisted Dirac operator requires accounting for the connection’s zeroth-order torsion correction.

### 5. Refined Kato: \(k^2=3/4\) is correct

By (A.2), when \(\operatorname{Ric}''=0\), \(D\alpha\) belongs to the kernel of the full primitive-projection map. In the coefficient model this is
\[
K=\{(P,Q):P=cI,\ Q\in M_2(\mathbb C)\},
\qquad \dim_{\mathbb C}K=5.
\]
For a unit real tensor \(\xi\otimes v\), half its squared norm lies in the unrestricted same-type sector. The trace projection of the other half contributes at most \(1/4\). Consequently
\[
\sup_{|\xi|=|v|=1}|\pi_K(\xi\otimes v)|^2
=\frac12+\frac14=\frac34,
\]
with equality for the script’s aligned example. Thus
\[
\boxed{|d|\alpha||\le\frac{\sqrt3}{2}|D\alpha|.}
\]
This is sharp for the algebraic first-order kernel. The supplied computation does not establish that equality is realized by a genuine Einstein almost-Kähler germ.

## B. Proposition 75.I: determinant and orientation

For \(f(z)=cz+B\bar z\), complexification of its real derivative gives
\[
\begin{pmatrix}cI&B\\ \bar B&\bar cI\end{pmatrix}.
\]
Therefore
\[
\det_{\mathbb R}Df=\det(|c|^2I-\bar BB).
\]
Writing \(B=S+A\), with \(S^T=S\), \(A^T=-A\),
\[
\operatorname{tr}(\bar BB)=\|S\|^2-\|A\|^2,\qquad
\det(\bar BB)=|\det B|^2.
\]
Hence (75.5) is correct:
\[
\boxed{
\det_{\mathbb R}Df
=|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2.
}
\]

Set
\[
x=|c|^2,\qquad t=\|S\|^2-\|A\|^2,\qquad d=|\det B|.
\]
At a nondegenerate zero, the exact negative-index criterion is
\[
\boxed{
t>2d,\qquad
\frac{t-\sqrt{t^2-4d^2}}2
<x<
\frac{t+\sqrt{t^2-4d^2}}2.
}
\]
Thus the note’s necessary inequality \(t\ge2d\) should be sharpened to **strict** \(t>2d\). Its positive cases—\(c=0\), \(S=0\), or \(\|S\|\le\|A\|\)—are correct under the nondegeneracy assumption.

The script’s docstring nevertheless contains a separate error: for arbitrary \(B\), this determinant is **not**
\[
(|c|^2-s_1^2)(|c|^2-s_2^2)
\]
with \(s_i\) the singular values of \(B\). The eigenvalues of \(\bar BB\) need not be the squared singular values. The implemented calculation and JSON use the correct polynomial and are unaffected.

### Orientation

The source carries the orientation of \(\Omega^2/2\); \(E\) carries its complex orientation. The identifications between the torsion, \(a\), and the two complex coefficient functions are complex-linear or complex-antilinear. Both preserve real orientation in complex rank two. Thus
\[
\boxed{\operatorname{ind}_p(T)=\operatorname{sign}\det_{\mathbb R}Df.}
\]

Replace Step 76’s sentence “every complex structure on \(E\) induces the same real orientation” by:

> The prescribed complex structure on \(E\), its conjugate, and the complex-linear or complex-antilinear identifications used here induce the same real orientation in complex rank two.

Arbitrary complex structures on a real rank-four bundle need not induce the same orientation.

Both index signs occur on open subsets of this necessary jet space. Calling positive index “generic” is therefore misleading. These jets are not constructions of Einstein germs.

## C. Step 75 §3: Bochner weights and decay

### 1. The Kato exponent calculation is valid, but the asserted Dirac formula is not established

For a metric connection \(D\), \(f=|\alpha|>0\), and \(0<\gamma<2\),
\[
\Delta f^\gamma
=\gamma f^{\gamma-2}
\left[
|D\alpha|^2-(2-\gamma)|df|^2
-\operatorname{Re}\langle D^*D\alpha,\alpha\rangle
\right].
\]
The Kato bound gives the stated inequality and the critical exponent \(\gamma=2/3\). The restriction \(0<\gamma<2\), rather than merely \(\gamma<2\), is needed.

The note’s specific assertion about a \(-s/4\) coefficient and removal of the Weyl coupling “only after integration” should not be treated as proved. A source-grounded alternative is available from AAD-LM (47). For an Einstein metric and \(T=\nabla\Omega\), contraction with \(T\) gives
\[
\boxed{
\langle\nabla^*\nabla T,T\rangle
=-\frac{3s}{4}q+2\langle\nabla\eta,T\rangle.
}
\tag{C.1}
\]
The \(\Omega\)-valued terms are perpendicular to \(T\); the remaining term involving \(J\eta\) contracts to zero because \(J\eta\) is skew and the Gram tensor of \(T\) is symmetric. On a closed manifold,
\[
\int\langle\nabla\eta,T\rangle
=\int\langle\eta,\nabla^*\nabla\Omega\rangle
=2\int|\eta|^2.
\]
Thus the negative-scalar-curvature sign difficulty is real, but this does not exclude every possible weighted or Kato-based argument.

### 2. “Index-blind” is correct only for norm-only zero-localized data

The decisive observation is
\[
|OLx|=|Lx|
\]
for an orientation-reversing orthogonal target map \(O\), although
\[
\operatorname{sign}\det(OL)=-\operatorname{sign}\det L.
\]
Thus the norm profile cannot recover the signed index.

The note’s example
\[
\Delta|Lx|^{-2}=-c|\det L|^{-1}\delta_0
\]
is false for general \(L\). With spherical principal-value convention, the correct formula is
\[
\boxed{
\Delta|Lx|^{-2}
=
\operatorname{pv}\!\left(
-\frac{2\operatorname{tr}H}{(x^THx)^2}
+\frac{8x^TH^2x}{(x^THx)^3}
\right)
-2\left(\int_{S^3}|L\theta|^{-2}\,d\theta\right)\delta_0,
\quad H=L^TL.
}
\]
The delta coefficient depends on the singular values, not just \(|\det L|\), and the term away from zero generally does not vanish. For \(L=tI\), it reduces to
\[
\Delta|tx|^{-2}=-4\pi^2t^{-2}\delta_0,
\]
already disproving the claimed determinant scaling.

Nor does every singular weight necessarily produce a Dirac mass. The valid replacement is:

> Norm-only singular contributions cannot distinguish the index sign. This does not rule out a global weighted identity coupled to additional orientation-sensitive tensors.

### 3. The decay principle is conditional, not a universal no-go theorem

The rigorous statement is:

> Suppose a universal local identity on almost-Kähler Einstein solutions is
> \(\operatorname{div}V=\Phi\), where \(V\) is globally defined and smooth on A01’s completed pair. If \(\Phi\ge0\) and the end flux of \(V\) tends to zero, then exhaustion and Stokes imply \(\int\Phi=0\), hence \(\Phi\equiv0\) on that pair.

Consequently, such an identity cannot have a nonnegative integrand whose vanishing forces \(T=0\). But:

* an identity known only after integration on closed manifolds is insufficient;
* polynomial dependence on jets does not imply decaying flux;
* a gauge-dependent expression involving \(b\) requires a globalization argument;
* the sign-indefinite AAD balance is not itself an example of a coercive \(\Phi\).

A01’s four finite integrals do establish absolute integrability and zero total integral of the AAD balance. For the global Chern–Weil transgression below, this implies zero limiting **total transgression flux**. It does not establish decay of every prospective current.

The phrase “charge escapes to infinity” should not be read as a finite integral of the ordinary \(c_2\) densities: both densities tend to \(42/(4\pi^2)\), and their integrals on this infinite-volume pair diverge. Relative or section-localized representatives require a separate interpretation.

## D. Step 76 §1: canonical curvature and Chern–Weil formulas

### 1. The \(\Lambda^-\) connection is unchanged

AAD’s first canonical connection is
\[
\boxed{\bar\nabla=\nabla+A,\qquad A=-\frac12J\nabla J.}
\]
The note reverses this connection-difference convention.

Since \(A\) takes values in \(\mathfrak m\subset\Lambda^+\) and
\[
[\Lambda^+,\Lambda^-]=0,
\]
the induced connections on \(\Lambda^-\) are **identical**, not merely curvature-equivalent. Thus their \(p_1(\Lambda^-)\) densities agree. The observation
\[
[\mathfrak m,\mathfrak m]\subset\mathbb R\Omega
\]
is correct; in a curvature expansion the covariant-derivative term is \(\mathfrak m\)-valued and disappears upon \(\mathfrak u(2)\)-projection.

### 2. Equation (76.1) has the wrong overall sign

Both supplied AAD papers explicitly give
\[
\boxed{db=a\wedge Ja-R(\Omega).}
\tag{76.1 corrected}
\]
The canonical Chern form is
\[
\boxed{\gamma_J=-db=R(\Omega)-a\wedge Ja,\qquad
[\gamma_J/(2\pi)]=c_1(M,J).}
\]
Accordingly,
\[
\boxed{
\langle db,\Omega\rangle=-\frac{s+s^*}{4},
\qquad
\langle\gamma_J,\Omega\rangle=\frac{s+s^*}{4}.
}
\]
For Einstein metrics, replace the subsequent \(db\)-component formulas by
\[
\boxed{
(db)^+=-\left(\frac s4+\frac q8\right)\Omega-\eta,
\qquad
(db)^-=(a\wedge Ja)^-.
}
\]
The formulas printed in Step 76 are instead the components of \(\gamma_J=-db\).

### 3. Formula (76.2) is correct

The roots of \(E\) give
\[
c_2(E)=c_2(TM,J)+2c_1(TM,J)^2.
\]
Using
\[
e(TM)=\frac14\bigl(p_1(\Lambda^+)-p_1(\Lambda^-)\bigr),
\qquad c_1^2=p_1(\Lambda^+),
\]
one obtains
\[
\boxed{
c_2(E)=\frac94p_1(\Lambda^+)-\frac14p_1(\Lambda^-).
}
\]
For the canonical connection,
\[
p_1(\Lambda^+)=\frac1{4\pi^2}db\wedge db.
\]
The sign correction therefore leaves all the degree-four densities unchanged.

Strictly speaking, the “Levi-Civita representative of \(c_2(E)\)” below is the Levi-Civita characteristic polynomial
\(\frac94p_1(\Lambda^+)-\frac14p_1(\Lambda^-)\). Levi-Civita does not itself preserve the \(J\)-defined bundle \(E\).

### 4. Formulas (76.3) and (76.4) are correct

At \(s=-12\),
\[
4\pi^2p_1(\Lambda^+,\bar\nabla)
=(18-\tfrac32q+|\eta|^2)d\mu,
\]
because the \(q^2\) terms in \(|\gamma_J^+|^2-|\gamma_J^-|^2\) cancel. Also,
\[
4\pi^2p_1(\Lambda^-,\bar\nabla)
=(-6-2|W^-|^2)d\mu.
\]
Thus
\[
\boxed{
4\pi^2c_2(E)_{\bar\nabla}
=
\left(42-\frac{27}{8}q+\frac94|\eta|^2+\frac12|W^-|^2\right)d\mu.
}
\]

The Levi-Civita polynomial is
\[
4\pi^2c_2(E)_{\mathrm{LC}}
=\left(15+\frac92|W^+|^2+\frac12|W^-|^2\right)d\mu.
\]
Using \(\kappa=-12+\frac32q\) and
\[
|W^+|^2=\frac{\kappa^2}{24}+|\eta|^2+|W_3^+|^2
\]
gives
\[
\boxed{
4\pi^2(c_2(E)_{\mathrm{LC}}-c_2(E)_{\bar\nabla})
=
\frac94\left(
|\eta|^2+2|W_3^+|^2+\frac3{16}q^2-\frac32q
\right)d\mu.
}
\]

The script verifies these algebraic substitutions on A01’s exact functions. Its canonical density
\[
D(p)=\frac{6(567p^8+783p^6+297p^4+165p^2-20)}
{(3p^2+1)^4}
\]
indeed increases from \(6\) to \(42\): setting \(x=p^2\),
\[
\frac{dD}{dx}
=\frac{486(1-x)^2(5-x)}{(3x+1)^5}>0
\quad(1/9\le x<1).
\]

### 5. What the script says about signs

It **does not fix the overall sign** in (76.1). Both
\[
db=a\wedge Ja-R(\Omega)
\quad\text{and}\quad
-db=R(\Omega)-a\wedge Ja
\]
produce identical squares and therefore identical (76.3)–(76.4). AAD’s connection and Ricci identities, not this script, fix which one is \(db\).

Changing the **relative** sign is different. Replacing \(\gamma_J=R(\Omega)-a\wedge Ja\) by \(R(\Omega)+a\wedge Ja\) would instead give
\[
4\pi^2c_{2,\mathrm{alt}}
=
\left(
42-\frac{81}{8}q+\frac9{16}q^2
+\frac94|\eta|^2+\frac12|W^-|^2
\right)d\mu,
\]
and the difference bracket would become
\[
|\eta|^2+2|W_3^+|^2-\frac1{16}q^2+\frac32q.
\]
Its A01 integral is \(448/3\) per unit orbit volume, not zero. Nevertheless, the supplied script does not independently compute the connection curvature or its flux; its successful substitution is not an independent geometric sign determination.

**Remaining scientific limitation.** These corrected identities allow both signs of nondegenerate torsion-zero index and do not establish the existence or impossibility of a negative Einstein almost-Kähler germ with a torsion zero. That is a nonlinear compatibility/existence question beyond the verified first-order kernel and characteristic-density calculations.