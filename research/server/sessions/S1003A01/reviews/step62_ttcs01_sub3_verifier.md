# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/scripts/step62_zero_prolong.py",
    "Sessions/S1003A01/workspace/scripts/step62_phi_identity.py",
    "Sessions/S1003A01/workspace/scripts/step62_det_formula.py",
    "Sessions/S1003A01/workspace/data/step62b/phi_prediction.json",
    "Sessions/S1003A01/workspace/data/step62/linear.json",
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md"
  ]
}
```

## Task

Verify Theorem 62.A and Corollaries 62.B/62.C in the attached note (closed negative Goldberg problem, four-dimensional Einstein almost-Kahler geometry). Check carefully: (1) the Weitzenbock identity for a harmonic self-dual 2-form of constant length |Omega|^2=2 and q=4<W+u,u>-2s/3; (2) the Derdzinski/Einstein Weitzenbock formula nabla^*nabla W+ = -(s/2)W+ + 6(W+)^2 - 2 tr((W+)^2) Id in the endomorphism normalization where a Kahler surface has W+ spectrum (s/6,-s/12,-s/12) (confirm by testing on Kahler and on the integrated identity int|nabla W+|^2 + (s/2)|W+|^2 - 18 det W+ = 0); (3) the computation at a torsion zero giving |nabla^2 Omega|^2 = 4 trV^2 - 12|eta|^2, including the claim that nabla^2 Omega(p) takes values in Omega^perp inside Lambda^+; (4) the translation into the first-jet parametrization f=cz+(S+A)zbar, the cone ||A||^2=8|c|^2+||S||^2 (using the numerically determined proportionalities |eta|^2=|m_c|^2/8, trV^2=|m_A|^2/4, |m|^2/2=|nabla^2 Omega|^2, Frobenius ratios 4|c|^2:2||A||^2:2||S||^2), and the index bound det_R Df >= 25|c|^4 via |det S|<=||S||^2/2. Assess whether 'every nondegenerate torsion zero has index +1' follows rigorously, and whether the numerical continuation evidence (section 3) is consistent with the cone being the complete first nonlinear compatibility. Point out any sign/normalization error or hidden assumption (e.g. orientation of E, identification of c with eta, whether the S/A split used in the determinant matches the U(2) split used numerically). Also say whether this identity or index law appears to be known (Armstrong, AAD, Kim) as far as the supplied sources show; do not invent literature.

## Output

## Scientific verification memo

### 1. Harmonic self-dual Weitzenböck identity

Use the convention
\[
\nabla^*\nabla=-\operatorname{tr}\nabla^2,\qquad
\Delta_d=d\delta+\delta d.
\]
For a self-dual two-form in dimension four,
\[
\Delta_d\Omega=\nabla^*\nabla\Omega-2W^+\Omega+\frac{s}{3}\Omega.
\]
An almost-Kähler form is closed and self-dual in the \(\Omega\)-orientation, hence also coclosed. Therefore
\[
\nabla^*\nabla\Omega=2W^+\Omega-\frac{s}{3}\Omega.
\]
Since \(|\Omega|^2=2\) is constant,
\[
0=\frac12\nabla^*\nabla|\Omega|^2
 =\langle\nabla^*\nabla\Omega,\Omega\rangle-|\nabla\Omega|^2.
\]
Writing \(u=\Omega/\sqrt2\) and \(r=\langle W^+u,u\rangle\) gives
\[
q:=|\nabla\Omega|^2
 =2\langle W^+\Omega,\Omega\rangle-\frac{s}{3}|\Omega|^2
 =4r-\frac{2s}{3}.
\]
Thus item (1) is correct. At a torsion zero \(p\), \(q(p)=0\), so
\[
r(p)=\frac{s}{6}.
\]

### 2. Einstein–Derdziński formula and normalization

In the endomorphism normalization on \(\Lambda^+\),
\[
\boxed{\;
\nabla^*\nabla W^+
=-\frac{s}{2}W^+ +6(W^+)^2
 -2\operatorname{tr}\bigl((W^+)^2\bigr)\operatorname{Id}_{\Lambda^+}.
\;}
\]
This normalization passes both requested tests.

For a Kähler–Einstein surface,
\[
\operatorname{spec}(W^+)=\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right),
\qquad
|W^+|^2=\operatorname{tr}(W^+)^2=\frac{s^2}{24}.
\]
Substitution into the right-hand side gives zero on all three eigenspaces.

Pairing the formula with \(W^+\), using \(\operatorname{tr}W^+=0\), yields
\[
\langle\nabla^*\nabla W^+,W^+\rangle
=-\frac{s}{2}|W^+|^2+6\operatorname{tr}(W^+)^3.
\]
For a traceless \(3\times3\) endomorphism,
\[
\operatorname{tr}(W^+)^3=3\det W^+.
\]
Hence on a closed manifold,
\[
\int_M\left(
|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+
\right)=0.
\]
For the Kähler spectrum, both algebraic terms equal \(s^3/48\), so they cancel pointwise. There is no sign or factor discrepancy here.

### 3. Calculation at a torsion zero

At \(p\), write
\[
W^+=
\begin{pmatrix}
r&\eta^T\\
\eta&-\frac r2 I+V
\end{pmatrix},
\qquad \operatorname{tr}V=0,
\qquad r=\frac{s}{6}.
\]
Then
\[
\langle (W^+)^2u,u\rangle=\frac{s^2}{36}+|\eta|^2
\]
and
\[
\operatorname{tr}(W^+)^2
=\frac{s^2}{24}+2|\eta|^2+\operatorname{tr}V^2.
\]
The \(uu\)-entry of the Derdziński formula is therefore
\[
\left\langle(\nabla^*\nabla W^+)u,u\right\rangle
=2|\eta|^2-2\operatorname{tr}V^2.
\]

Because \(\nabla u(p)=0\), the product formula at \(p\) has no mixed \(\nabla W^+\cdot\nabla u\) terms:
\[
\nabla^*\nabla\langle W^+u,u\rangle
=
\left\langle(\nabla^*\nabla W^+)u,u\right\rangle
+2\left\langle W^+(\nabla^*\nabla u),u\right\rangle.
\]
The harmonic-form equation gives
\[
\nabla^*\nabla u=2W^+u-\frac{s}{3}u,
\]
so
\[
2\left\langle W^+(\nabla^*\nabla u),u\right\rangle
=4\left(\frac{s^2}{36}+|\eta|^2\right)
-\frac{2s}{3}\frac{s}{6}
=4|\eta|^2.
\]
Consequently,
\[
\nabla^*\nabla r
=6|\eta|^2-2\operatorname{tr}V^2.
\]
Einstein implies that \(s\) is constant, and \(q=4r-2s/3\), hence
\[
\nabla^*\nabla q
=24|\eta|^2-8\operatorname{tr}V^2.
\]

For \(T=\nabla\Omega\),
\[
\nabla^*\nabla |T|^2
=2\langle\nabla^*\nabla T,T\rangle-2|\nabla T|^2.
\]
Since \(T(p)=0\),
\[
\nabla^*\nabla q(p)=-2|\nabla^2\Omega|^2(p).
\]
Combining the last two equations gives
\[
\boxed{\;
|\nabla^2\Omega|^2(p)
=4\operatorname{tr}V^2-12|\eta|^2.
\;}
\]
Thus Theorem 62.A is correct with the stated conventions.

#### Values of \(\nabla^2\Omega(p)\)

The additional assertion is also correct. Since the Hodge star is parallel and \(\Omega\) is self-dual,
\[
*\nabla_k\nabla_l\Omega=\nabla_k\nabla_l\Omega.
\]
Moreover,
\[
0=\nabla_k\langle\nabla_l\Omega,\Omega\rangle
=\langle\nabla_k\nabla_l\Omega,\Omega\rangle
 +\langle\nabla_l\Omega,\nabla_k\Omega\rangle.
\]
At a torsion zero, the second term vanishes. Hence
\[
\nabla_k\nabla_l\Omega(p)\in
\Lambda_p^+\cap\Omega(p)^\perp
\]
for every \(k,l\). This justifies representing the Hessian only by its \(\phi,J\phi\) components.

### 4. Exact translation to \(c,S,A\)

Let \(m=m_c+m_A+m_S\) be the orthogonal decomposition used in the note. The listed relations give
\[
|\nabla^2\Omega|^2
=\frac12\bigl(|m_c|^2+|m_A|^2+|m_S|^2\bigr),
\]
\[
|\eta|^2=\frac{|m_c|^2}{8},
\qquad
\operatorname{tr}V^2=\frac{|m_A|^2}{4}.
\]
Substitution into Theorem 62.A gives
\[
\frac12(|m_c|^2+|m_A|^2+|m_S|^2)
=|m_A|^2-\frac32|m_c|^2,
\]
or
\[
2|m_c|^2-\frac12|m_A|^2+\frac12|m_S|^2=0,
\]
equivalently
\[
|m_A|^2=4|m_c|^2+|m_S|^2.
\]

The proportionality
\[
|m_c|^2:|m_A|^2:|m_S|^2
=
4|c|^2:2\|A\|^2:2\|S\|^2
\]
then gives
\[
\boxed{\;
\|A\|^2=8|c|^2+\|S\|^2.
\;}
\]

These constants can be justified without floating-point output. At a zero, put \(M=\nabla a\). From
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi
\]
one obtains
\[
|\nabla^2\Omega|^2=4|M|^2,
\qquad |m|^2=8|M|^2.
\]
In the Step-59 representation
\[
(f_1\,d\bar z_1+f_2\,d\bar z_2)\otimes\ell,
\]
the real Frobenius norm is
\[
\|Df\|_{\mathbb R}^2
=4|c|^2+2\|S\|^2+2\|A\|^2.
\]
The \(c\)-mode gives the trace component of \(d_b\alpha\), hence \(\eta\); the antisymmetric \(A\)-mode gives \(V=W_3^+\); the symmetric \(S\)-mode is annihilated by exterior antisymmetrization. Representative computations \(f=z\) and
\[
f=(\bar z_2,-\bar z_1)
\]
give respectively
\[
|\eta|^2=\frac{|m_c|^2}{8},
\qquad
\operatorname{tr}V^2=\frac{|m_A|^2}{4}.
\]
Thus the floating eigenvalues in `phi_prediction.json` reflect exact \(U(2)\)-equivariant constants. The script `step62_det_formula.py` by itself verifies the Jacobian norm and determinant formulas, but not the curvature identification; the coframe computation above supplies that missing exact link.

### 5. Corollary 62.B

All three parts follow.

* A pure \(c\), pure \(S\), or pure \(A\) jet cannot satisfy
  \[
  \|A\|^2=8|c|^2+\|S\|^2
  \]
  unless it vanishes. Any nonzero admissible jet has \(A\ne0\), and the exact \(A\leftrightarrow V=W_3^+\) identification gives \(W_3^+(p)\ne0\).

* Theorem 62.A rearranges to
  \[
  \operatorname{tr}V^2
  =\frac14|\nabla^2\Omega|^2+3|\eta|^2.
  \]
  Hence \(V=0\) forces both \(\nabla^2\Omega=0\) and \(\eta=0\).

* At the zero,
  \[
  |W^+|^2
  =\frac{s^2}{24}+2|\eta|^2+\operatorname{tr}V^2.
  \]
  A nonzero first torsion jet forces \(V\ne0\), so
  \[
  |W^+|^2>\frac{s^2}{24}.
  \]

Here “order at least two” means that the torsion section \(T=\nabla\Omega\) and its first derivative both vanish.

### 6. Determinant and local index

For
\[
f(z)=cz+B\bar z,\qquad B=S+A,
\]
the complexified real Jacobian has block form
\[
\begin{pmatrix}
cI&B\\
\bar B&\bar cI
\end{pmatrix}.
\]
Its determinant is
\[
\det_{\mathbb R}Df
=\det\bigl(|c|^2I-\bar BB\bigr).
\]
Because \(S^T=S\) and \(A^T=-A\),
\[
\operatorname{tr}(\bar BB)=\|S\|^2-\|A\|^2,
\]
and therefore
\[
\det_{\mathbb R}Df
=|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2.
\]

Write
\[
A=\begin{pmatrix}0&a\\-a&0\end{pmatrix}.
\]
Then
\[
\det B=\det S+a^2,
\qquad |a|^2=\frac{\|A\|^2}{2}.
\]
On the cone,
\[
\det_{\mathbb R}Df=9|c|^4+|\det B|^2.
\]
Also,
\[
|\det S|\le\frac{\|S\|^2}{2},
\]
so
\[
|\det B|
\ge |a|^2-|\det S|
\ge 4|c|^2.
\]
Consequently,
\[
\boxed{\;
\det_{\mathbb R}Df\ge25|c|^4.
\;}
\]

When \(c\ne0\), positivity is immediate. When \(c=0\), the displayed lower estimate only gives \(\det_{\mathbb R}Df\ge0\); nondegeneracy supplies \(\det_{\mathbb R}Df\ne0\), and the formula
\[
\det_{\mathbb R}Df=|\det B|^2
\]
then gives strict positivity. Thus every nondegenerate zero has index \(+1\).

The orientation must be the complex orientation of
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2}
\]
over the \(\Omega\)-oriented base. This is the orientation used in Steps 59 and 75. Unitary changes of the base coordinates or of the line frame have positive real determinant, and \(f=z\) fixes the calibration at \(+1\). Transposing the real matrix \(M\) does not alter its determinant. With these identifications, the index statement is rigorous.

The degenerate nonzero first jets are exactly
\[
c=0,\qquad \det B=0,
\]
which is equivalent on the cone to
\[
|\det S|=\frac{\|S\|^2}{2},
\qquad
\det S=-a^2.
\]
Thus the equal-singular-value description is also correct.

### 7. Numerical continuation

The reported computations are consistent with the cone being the sole quadratic compatibility at degree four:

* pure \(c\), \(S\), \(A\), and the index-\(-1\) mixed target lie off the cone and retain residuals;
* residual squared scaling approximately as \(t^4\) is what a quadratic equation in the first jet produces;
* sampled cone targets reach raw residuals near \(10^{-15}\), hence squared residuals near \(10^{-30}\);
* the Gibbons–Hawking jet has \(c=0\), equal \(A\)- and \(S\)-norms, \(\eta=0\), and satisfies
  \[
  |\nabla^2\Omega|^2=4\operatorname{tr}V^2;
  \]
* both \(\lambda=0\) and \(\lambda=-1\) samples agree with the scalar-curvature cancellation in Theorem 62.A.

The numerical data do not by themselves establish solvability for every point of the cone. That stronger statement would require an exact elimination or a formal implicit-function argument showing surjectivity onto all remaining degree-four equations, separately at regular cone points and at the \(c=0\) degenerate stratum. Likewise, degree-four jets do not produce an analytic Einstein almost-Kähler germ. The unavailable degree-five output cannot be assessed here.

One wording detail: `gh_jets` converts SymPy coefficients to floating-point arrays before JAX evaluation. Its reported zero is therefore a machine-arithmetic result, although the underlying Gibbons–Hawking formulas are suitable for a separate symbolic verification.

### 8. Appearance in the supplied literature material

The supplied AAD material contains the Ricci identities, curvature splitting, and integrated torsion balance from which the zero identity is naturally derived, but no supplied passage states
\[
|\nabla^2\Omega|^2=4\operatorname{tr}V^2-12|\eta|^2
\]
at a torsion zero or the resulting positive-index theorem.

Step 75 contains the unrestricted determinant formula, allowing both index signs before the Einstein quadratic relation is imposed. The positivity on the cone is new relative to that supplied note.

Armstrong’s full text was not available in the supplied material, so no comparison with its local formulas is possible. No Kim source or quoted passage was supplied. Accordingly, the files support the derivation but do not establish bibliographic priority.

**Overall:** Theorem 62.A and Corollaries 62.B/62.C are mathematically correct under the stated endomorphism, form-norm, and complex-orientation conventions. The principal textual improvement needed is to replace reliance on numerically observed proportionalities by the exact unitary-coframe calculation connecting \(c,A,S\) to \(\eta,V\) and \(m\).