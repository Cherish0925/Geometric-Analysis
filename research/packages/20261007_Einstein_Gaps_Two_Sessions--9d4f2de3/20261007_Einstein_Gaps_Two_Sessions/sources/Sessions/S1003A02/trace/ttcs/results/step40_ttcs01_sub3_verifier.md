# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/scripts/step40_nijenhuis_tariff_check.py",
    "Sessions/S1003A02/workspace/data/step40_nijenhuis_tariff_check.json",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Skills/geometric-analysis/research/paper/sections/single_solution_coercivity.tex",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md"
  ]
}
```

## Task

Verify the new Step-40 theorems in workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md against the simultaneous signed-cost identity (Prop. 'Simultaneous signed cost identity', lines 319-447 of variational_selection_and_global_cost.tex) in its normalization s=-4, F^+=2i sigma(Phi), rho=|Phi|^2 in [0,2], psi=2sqrt2 sigma(Phi), W_0=(1/4)(rho^2 I/3 - psi psi). Check in detail: (1) Lemma 1: that the Clifford contraction of the u^perp-valued part of the first jet has kernel exactly the Gray-Hervella W_2 (almost-Kaehler / Nijenhuis) component, that cc*=2, hence rho|v_4|^2=|a+J'b|^2/2 under D_A Phi=0, and that this is correct in the presence of the U(1) connection; (2) the pointwise Weitzenboeck formula (1/2)Delta rho + |nabla Phi|^2 = rho(2-rho)/2 in this normalization (the integrated version K=(1/2)int rho(2-rho) follows from the paper's slack identities); (3) Theorem N as an exact equality, including the polynomial m-rho^2(2-rho) and the (a,b) quadratic form, and the Hermitian corollary P>=8pi^2 Q; (4) Theorem W: the self-dual Weitzenboeck convention (Delta_H = nabla*nabla - 2W^+ + s/3 with W_0 having Kaehler eigenvalue s/6), |d psi|^2 = 2 rho |b|^2 under the Dirac equation, and the collapse of the (a,b) form to -4|zeta|^2; (5) Theorem E: the pointwise envelope g_{t,lambda}, the use of |W^+|^2 = rho^4/24 - rho^2 x/2 + |M|^2 and |M|^2 >= (3/2) x^2, and the exact conclusion that the threshold is t=2/3 binding at rho=3/2. Report any sign, factor, convention, or quantifier error and its repair, and say precisely which statements are proved. Also assess whether Theorem E really shows that no pointwise/algebraic compensation inequality can give k-dependence, and what global terms remain.

## Output

# Scientific verification memo

## 1. Overall result

In the normalization
\[
s=-4,\qquad F_{\mathcal A}^{+}=2i\sigma(\Phi),\qquad
\rho=|\Phi|^{2}\in[0,2],\qquad
\psi=2\sqrt2\,\sigma(\Phi),\quad |\psi|=\rho,
\]
the principal formulas in Lemma 1 and Theorems N, W, and E are algebraically consistent with Proposition `Simultaneous signed cost identity`.

The exact identities have the correct signs and constants. The following textual points need more precise formulation:

1. Theorem E establishes exhaustion for a specified family of constant affine combinations of the displayed field identities, followed by pointwise positivity and
   \(|M|^{2}\ge\frac32x^{2}\). It does not establish impossibility for every conceivable pointwise relation coupling the entire sign family.
2. The Hermitian corollary recovers the tariff for scalar-\(-4\) metrics admitting a simultaneous choice of integrable monopole Bloch structures. It does not subsume the full Step-38 theorem for arbitrary Kähler metrics, since passage to a scalar-\(-4\) Yamabe representative generally destroys the Kähler property.
3. The Nijenhuis lower estimate is asymptotic and its displayed numerical value is slightly inaccurate: the coefficient is approximately \(0.684914\), rather than \(0.68488\).
4. The scale-law conclusions require controlled geometry and controlled multiplicity of rotating regions.
5. In Theorem W, \(W^{+}(n,n)\) is a Rayleigh component, not necessarily an eigenvalue.

---

## 2. Lemma 1: first-jet decomposition and the \(U(1)\) connection

### 2.1 Clifford contraction

At a point with \(\rho>0\), write
\[
\Phi=\sqrt\rho\,u,\qquad |u|=1,
\]
and choose a unit spinor \(u^\perp\) Hermitian-orthogonal to \(u\). The coupled derivative has the form
\[
\nabla_{\mathcal A}u=i\beta\otimes u+v\otimes u^\perp,
\qquad
\beta\in T^*,\quad v\in T^*\otimes\mathbb C.
\]
The Clifford contraction
\[
c:T^*\otimes_{\mathbb R}\mathbb C\longrightarrow S^-,
\qquad
c(v)=\sum_i e_i\cdot(v_i u^\perp)
\]
is a real-linear map from an \(8\)-dimensional real space to a \(4\)-dimensional real space.

Its real Hilbert–Schmidt norm is \(8\): the eight real basis vectors
\[
e^i\otimes u^\perp,\qquad e^i\otimes i u^\perp
\]
all have images of norm one. Equivariance under the \(U(2)\) stabilizer of the unit positive spinor gives
\[
cc^*=\mu\,\operatorname{Id}_{S^-}.
\]
Taking real traces gives \(4\mu=8\), hence
\[
\boxed{cc^*=2\,\operatorname{Id}_{S^-}}.
\]
This also proves surjectivity and \(\dim_{\mathbb R}\ker c=4\).

### 2.2 Identification of \(\ker c\) with \(\mathcal W_2\)

The quadratic spinor \(u\) defines a unit self-dual Bloch form \(n\), or equivalently a fundamental form \(\omega\) of norm \(\sqrt2\). The phase component \(i\beta u\) does not change \(n\); only \(v\) contributes to \(\nabla n\).

In real dimension four, the intrinsic torsion of a compatible almost-complex structure has the decomposition
\[
\mathcal W_2\oplus\mathcal W_4.
\]
The alternation map
\[
v\longmapsto d\omega
\]
has real rank four. Its kernel is the \(\mathcal W_2\) component, characterized pointwise by \(d\omega=0\). Since \(\omega\) is self-dual, \(d\omega=0\) and \(d^*\omega=0\) are equivalent at the point.

For the canonical determinant connection chosen so that the phase component of \(\nabla u\) vanishes at the point, the standard spinorial almost-Hermitian identity gives
\[
d\omega=0\quad\Longrightarrow\quad D_{\mathcal A}u=c(v)=0.
\]
Thus \(\ker(d\omega)\subseteq\ker c\). Both kernels have real dimension four, so
\[
\boxed{\ker c=\mathcal W_2=\ker(v\mapsto d\omega)}.
\]
Its orthogonal complement is the \(\mathcal W_4\), or Lee-form, component. In complex dimension two, \(\mathcal W_2=0\) is equivalent to integrability. Consequently the terminology “Nijenhuis component” is valid, although the displayed norm is a chosen normalization of intrinsic torsion and should not be identified with a conventionally normalized \(|N_J|^2\) without an explicit constant.

The random-spinor computations in `step40_nijenhuis_tariff_check.json` corroborate this: both maps have rank four and the principal cosines of their kernels equal one to machine precision.

### 2.3 Dirac equation and the Lee component

Put
\[
a=d\sqrt\rho,\qquad b=\sqrt\rho\,\beta.
\]
Then
\[
\nabla_{\mathcal A}\Phi
=(a+ib)\otimes u+\sqrt\rho\,v\otimes u^\perp,
\]
so
\[
D_{\mathcal A}\Phi=(a+ib)\cdot u+\sqrt\rho\,c(v).
\]
There is an orthogonal complex structure \(J'\) on \(T^*\) such that
\[
(ib)\cdot u=(J'b)\cdot u,
\qquad
|(a+ib)\cdot u|=|a+J'b|.
\]
Write \(v=v_2+v_4\), with \(v_2\in\ker c\) and
\(v_4\perp\ker c\). Since \(cc^*=2I\),
\[
v_4=-\frac1{2\sqrt\rho}\,
c^*\bigl((a+ib)\cdot u\bigr),
\]
and therefore
\[
\rho|v_4|^2
=\frac14\left\langle c^*\gamma,c^*\gamma\right\rangle
=\frac14\langle\gamma,cc^*\gamma\rangle
=\frac12|\gamma|^2
=\frac12|a+J'b|^2.
\]
Thus
\[
\boxed{\rho|v_4|^2=\frac12|a+J'b|^2}.
\]

The \(U(1)\) connection has not been omitted: its contribution is exactly the phase one-form \(\beta\), hence \(b\). Gauge changes rotate \(u\) and \(u^\perp\), but the norms, the Bloch form, and the \(\mathcal W_2\oplus\mathcal W_4\) decomposition are unchanged. The phrase “Dirac does not see the Nijenhuis component” is therefore correct at the first-jet algebraic level; the remaining SW equations can still constrain that component differentially.

Finally,
\[
|\nabla\Phi|^2=|a|^2+|b|^2+\rho|v|^2,
\]
\[
\zeta=\langle\Phi,\nabla_{\mathcal A}\Phi\rangle
=\sqrt\rho\,(a+ib),
\qquad
|\zeta|^2=\rho(|a|^2+|b|^2),
\]
and
\[
|\nabla n|^2=4|v|^2.
\]
All these identities are correct.

---

## 3. Scalar spinor Weitzenböck formula

Undoing the constant spinor rescaling in
`single_solution_coercivity.tex` gives
\[
4\nabla_{\mathcal A}^*\nabla_{\mathcal A}\Phi
+(-4+2\rho)\Phi=0.
\]
Hence
\[
\nabla_{\mathcal A}^*\nabla_{\mathcal A}\Phi
=\left(1-\frac\rho2\right)\Phi.
\]
With \(\Delta=d^*d\), the norm identity is
\[
\frac12\Delta|\Phi|^2
=\left\langle\nabla^*\nabla\Phi,\Phi\right\rangle
-|\nabla\Phi|^2.
\]
Therefore
\[
\boxed{\frac12\Delta\rho+|\nabla_{\mathcal A}\Phi|^2
=\frac12\rho(2-\rho)}.
\]
Integration gives
\[
K=\frac12\int\rho(2-\rho),
\]
as used in Step 40.

Multiplication by \(2\rho\) and integration gives
\[
\int\rho\,\Delta\rho+2\int\rho|\nabla\Phi|^2
=\int\rho^2(2-\rho).
\]
Since
\[
d\rho=2\sqrt\rho\,a,\qquad
\int\rho\Delta\rho=\int|d\rho|^2=4\int\rho|a|^2,
\]
the exact zero identity is
\[
\boxed{
\int\left[
2\rho|\nabla\Phi|^2+4\rho|a|^2-\rho^2(2-\rho)
\right]=0.}
\]
The sign used in Theorem N is correct.

---

## 4. Theorem N

From Proposition `Simultaneous signed cost identity`,
\[
\mathfrak S:=8\pi^2Q-P
=4\mathbb E K-\mathcal W
-\mathbb E\!\left[
8\|\zeta\|^2+4\|M\|^2
+\int B(\rho)(2-\rho)^2
\right],
\]
where
\[
B(\rho)=\frac{-\rho^2+8\rho+2}{6}.
\]
Using \(4K=2\int\rho(2-\rho)\), define
\[
m(\rho)=2\rho(2-\rho)-B(\rho)(2-\rho)^2
=\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6.
\]
Thus the amplitude form is exactly
\[
\mathfrak S
=\mathbb E\int m(\rho)
-8\mathbb E\|\zeta\|^2
-4\mathbb E\|M\|^2-\mathcal W.
\]

Add the zero identity from the preceding section. Using
\[
2\rho|\nabla\Phi|^2+4\rho|a|^2
=6\rho|a|^2+2\rho|b|^2
+2\rho^2|v_2|^2+2\rho^2|v_4|^2
\]
and
\[
2\rho^2|v_4|^2=\rho|a+J'b|^2,
\]
the derivative terms become
\[
\begin{aligned}
&-8\rho(|a|^2+|b|^2)
+6\rho|a|^2+2\rho|b|^2+\rho|a+J'b|^2\\
&\qquad
=-\rho\bigl(|a|^2+5|b|^2-2\langle a,J'b\rangle\bigr).
\end{aligned}
\]
Also
\[
2\rho^2|v_2|^2
=\frac12\rho^2|\nabla n|_{\mathcal W_2}^2.
\]
The polynomial is
\[
m(\rho)-\rho^2(2-\rho)
=-\frac{(2-\rho)^2(2+2\rho-\rho^2)}6.
\]
Consequently Theorem N is the exact equality
\[
\boxed{
\begin{aligned}
\mathfrak S={}&
\frac12\mathbb E\int\rho^2|\nabla n|_{\mathcal W_2}^2\\
&-\mathbb E\int
\frac{(2-\rho)^2(2+2\rho-\rho^2)}6\\
&-\mathbb E\int
\rho\bigl(|a|^2+5|b|^2-2\langle a,J'b\rangle\bigr)\\
&-4\mathbb E\|M\|^2-\mathcal W .
\end{aligned}}
\]

On \(0\le\rho\le2\),
\[
2+2\rho-\rho^2>0,
\]
and
\[
|a|^2+5|b|^2-2\langle a,J'b\rangle
\]
has coefficient matrix
\[
\begin{pmatrix}1&-1\\-1&5\end{pmatrix},
\qquad \det=4,\quad \operatorname{tr}=6.
\]
Thus every term after the \(\mathcal W_2\) energy has the asserted sign.

### Hermitian tariff

If one can choose the simultaneous solutions so that every associated \(J_\epsilon\) is integrable on \(\{\Phi_\epsilon\ne0\}\), then
\[
|\nabla n_\epsilon|_{\mathcal W_2}=0
\]
there. The weighted term also vanishes on the spinor zero set, and Theorem N gives
\[
\mathfrak S\le0,\qquad
\boxed{P\ge8\pi^2Q}.
\]

The exact quantifier is existence of a simultaneous chosen family with integrable Bloch structures; requiring every possible solution to have this property is stronger than needed.

This recovers the scalar-\(-4\) Kähler or Hermitian instance. It does not by itself prove the Step-38 result for every Kähler metric, because a general Kähler metric does not have constant scalar curvature and its scalar-\(-4\) Yamabe representative need not be Kähler.

### Near-minimizer estimate

For pure blow-ups, if
\[
\frac{P}{8\pi^2k}\longrightarrow c<1,
\]
then the exact asymptotic statement is
\[
\boxed{
\liminf\frac1k\,
\mathbb E_\epsilon\int
\rho_\epsilon^2|\nabla n_\epsilon|_{\mathcal W_2}^2
\ge16\pi^2(1-c).}
\]
Equivalently, at finite \(k\),
\[
\mathbb E\int\rho^2|\nabla n|_{\mathcal W_2}^2
\ge16\pi^2(1-c)k+o(k).
\]
For
\[
1-c\in[0.0043372672289,0.0043372672468],
\]
the coefficient is approximately
\[
16\pi^2(1-c)\in[0.68491378,0.68491379].
\]
The value \(0.68488\) in Step 40 is a small arithmetic discrepancy.

The scale statement \(O(r^2)\) is correct for a controlled fixed-angle rotation on one four-dimensional region of diameter \(r\):
\[
|\nabla n|^2=O(r^{-2}),\qquad \operatorname{Vol}=O(r^4).
\]
The stronger phrase that unit-sized regions are required additionally presumes controlled geometry and a bounded number of rotating regions per exceptional class. Many shrinking regions or anisotropic tubes are not excluded by the displayed energy estimate alone.

---

## 5. Theorem W

### 5.1 Self-dual Weitzenböck convention

For a self-dual two-form,
\[
\Delta_H
=\nabla^*\nabla-2W^++\frac{s}{3},
\]
so
\[
\nabla^*\nabla\psi
=\Delta_H\psi+2W^+\psi-\frac{s}{3}\psi.
\]
At \(s=-4\),
\[
\int|\nabla\psi|^2
=\|d\psi\|^2+\|d^*\psi\|^2
+2\int W^+(\psi,\psi)+\frac43\int\rho^2.
\]
Since \(\psi\) is self-dual,
\[
|d^*\psi|=|d\psi|,
\]
and hence
\[
\int|\nabla\psi|^2
=2\|d\psi\|^2
+2\int W^+(\psi,\psi)+\frac43\int\rho^2.
\]

Now
\[
W_0\psi=-\frac{\rho^2}{6}\psi,
\]
because
\[
W_0=\frac14\left(\frac{\rho^2}{3}I-\psi\otimes\psi\right),
\qquad |\psi|^2=\rho^2.
\]
Thus, writing \(M=W^+-W_0\) and \(x=M(n,n)\),
\[
2W^+(\psi,\psi)
=2\rho^2x-\frac{\rho^4}{3}.
\]
Therefore
\[
\boxed{
\int|\nabla\psi|^2
=2\|d\psi\|^2
+2\int\rho^2x
+\int\frac{\rho^2}{3}(4-\rho^2).}
\]

At \(\rho=2\), the \(n\)-direction eigenvalue of \(W_0\) is
\[
-\frac{\rho^2}{6}=-\frac23=\frac{s}{6},
\]
so the Kähler sign convention is correct.

### 5.2 The \(d\psi\) identity

The quadratic-spinor Fierz identity, followed by the Dirac equation, gives
\[
|d\psi|^2=|d^*\psi|^2
=2|\operatorname{Im}\zeta|^2.
\]
Since
\[
\operatorname{Im}\zeta=\sqrt\rho\,b,
\]
this is
\[
\boxed{|d\psi|^2=2\rho|b|^2}.
\]
The \(\mathcal W_2\) component lies in the kernel of the alternation map and therefore contributes nothing to \(d\psi\).

The JSON output records eigenvalues \(\{0^4,2^4\}\) for the quadratic form, which is compatible with this identity, but those eigenvalues alone do not identify the kernel with the \(a\)-subspace. The same script’s combined matrix \(G\) has all eigenvalues equal to \(-4\); because \(G\) is symmetric and
\[
G=Q_d-4I_a-6I_b,
\]
this numerically implies \(Q_d=2I_b\). Recording the direct residual
\(\|Q_d-2I_b\|\) would make the computational artifact more transparent. The spinorial derivation above supplies the exact mathematical identification.

### 5.3 Collapse to \(-4|\zeta|^2\)

Since \(\psi=\rho n\),
\[
|\nabla\psi|^2
=|d\rho|^2+\rho^2|\nabla n|^2
=4\rho|a|^2+4\rho^2|v_2|^2
+2\rho|a+J'b|^2.
\]
Substitution into the self-dual Weitzenböck identity gives
\[
\begin{aligned}
2\rho^2|v_2|^2={}&
2\rho|b|^2+\rho^2x
+\frac{\rho^2}{6}(4-\rho^2)\\
&-2\rho|a|^2-\rho|a+J'b|^2.
\end{aligned}
\]
Inserting this into Theorem N, the \((a,b)\) terms are
\[
\begin{aligned}
&2\rho|b|^2-2\rho|a|^2-\rho|a+J'b|^2\\
&\qquad
-\rho\bigl(|a|^2+5|b|^2-2\langle a,J'b\rangle\bigr)\\
&=-4\rho(|a|^2+|b|^2)=-4|\zeta|^2.
\end{aligned}
\]
The polynomial identity is
\[
\frac{\rho^2}{6}(4-\rho^2)
-\frac{(2-\rho)^2(2+2\rho-\rho^2)}6
=\frac{(2-\rho)(\rho-1)(3\rho+2)}3.
\]
Hence Theorem W is exact:
\[
\boxed{
\begin{aligned}
\mathfrak S={}&
\mathbb E\int\bigl[\rho^2x-4|M|^2\bigr]\\
&+\mathbb E\int
\frac{(2-\rho)(\rho-1)(3\rho+2)}3
-4\mathbb E\|\zeta\|^2-\mathcal W.
\end{aligned}}
\]

Here
\[
x=M(n,n)=W^+(n,n)+\frac{\rho^2}{6}
\]
is the excess Rayleigh component along \(n\). Unless \(n\) is an eigenvector of \(W^+\), it should not be called an eigenvalue. Also \(x>0\) alone does not imply that \(|W^+|\) is smaller than \(|W_0|\), because transverse and off-diagonal components of \(M\) may be large. The exact saving channel is
\[
\rho^2x-4|M|^2.
\]

---

## 6. Theorem E

Assume now \(\ell=0\), so \(Q=k\), and retain \(A-k>0\).

### 6.1 Affine field combination

Combining the amplitude and Weyl forms with a constant \(\lambda\) gives the exact identity
\[
\begin{aligned}
\mathfrak S
={}&\mathbb E\int\Big[
\lambda\rho^2x+\lambda p_2(\rho)
+(1-\lambda)m(\rho)-4|M|^2\\
&\hspace{35mm}-(8-4\lambda)|\zeta|^2
\Big]-\mathcal W,
\end{aligned}
\]
where
\[
p_2(\rho)=\frac{(2-\rho)(\rho-1)(3\rho+2)}3.
\]
For
\[
\lambda\le2,
\]
the \(\zeta\)-coefficient has the useful sign, and dropping the
\(\zeta\) and Walsh terms yields an upper estimate for \(\mathfrak S\).

The closed Weyl–volume identity is
\[
P=-8\pi^2(A-k)
+\mathbb E\int\left(
\frac{\rho^4}{6}+\frac43-2\rho^2x+4|M|^2
\right),
\]
because
\[
|W^+|^2
=|W_0+M|^2
=\frac{\rho^4}{24}-\frac{\rho^2x}{2}+|M|^2.
\]
This formula has the correct cross-term sign.

For \(t\ge0\), use the field lower estimate for \(tP\) and the closed identity for \((1-t)P\). The \(M\)-dependent expression is
\[
4|M|^2-\bigl(t\lambda+2-2t\bigr)\rho^2x.
\]
For a trace-free symmetric endomorphism of a three-dimensional space,
\[
|M|^2\ge\frac32\,M(n,n)^2=\frac32x^2.
\]
Equality occurs at
\[
M=\operatorname{diag}\left(x,-\frac x2,-\frac x2\right)
\]
in a basis beginning with \(n\). Consequently,
\[
4|M|^2-c\rho^2x
\ge6x^2-c\rho^2x
\ge-\frac{c^2\rho^4}{24},
\qquad c=t\lambda+2-2t.
\]
This yields
\[
\boxed{
P\ge8\pi^2[k-(1-t)A]
+\mathbb E\int g_{t,\lambda}(\rho)}
\]
with
\[
\boxed{
\begin{aligned}
g_{t,\lambda}(\rho)
={}&(1-t)\left(\frac{\rho^4}{6}+\frac43\right)\\
&-t\left[\lambda p_2(\rho)+(1-\lambda)m(\rho)\right]\\
&-\frac{(t\lambda+2-2t)^2\rho^4}{24}.
\end{aligned}}
\]
Thus the formula in Step 40 is correct. The natural parameter domain accompanying the displayed derivation is
\[
t\ge0,\qquad \lambda\le2.
\]
Using only convex weights \(0\le\lambda\le1\) is also sufficient for the threshold calculation.

### 6.2 Exact threshold

At
\[
t=\lambda=\frac23,
\]
symbolic factorization gives
\[
g_{2/3,2/3}(\rho)
=-\frac2{243}(2\rho-3)^2(\rho^2-24\rho-18).
\]
Since
\[
\rho^2-24\rho-18<0
\qquad(0\le\rho\le2),
\]
one has
\[
g_{2/3,2/3}(\rho)\ge0,
\]
with equality only at \(\rho=3/2\). Hence
\[
P\ge8\pi^2\left(k-\frac A3\right).
\]
Using
\[
C_+=\frac{P}{8\pi^2}+A-k,
\]
this is precisely
\[
\boxed{C_+\ge\frac23A}.
\]

At \(\rho=3/2\),
\[
\max_\lambda g_{t,\lambda}(3/2)
=-\frac34(3t-2),
\qquad
\lambda_{\rm opt}=2-\frac8{9t}.
\]
For \(t>2/3\), this maximum is \(<0\). Moreover
\(\lambda_{\rm opt}<2\), so it lies in the parameter domain above. Thus no constant choice of \(\lambda\) makes \(g_{t,\lambda}\ge0\) throughout \([0,2]\) when \(t>2/3\).

This proves that \(t=2/3\) is the exact threshold for this affine envelope. At the threshold the pointwise contact occurs at \(\rho=3/2\), while
\[
g_{2/3,2/3}(2)=\frac{124}{243}.
\]

### 6.3 Inclusion of the Nijenhuis form

The Nijenhuis identity does not improve this threshold within the same affine sign-discarding method. Give it coefficient \(\beta\), the Weyl form coefficient \(\gamma\), and the amplitude form coefficient \(1-\beta-\gamma\). A pointwise upper estimate for the saving can discard the term
\[
2\beta\rho^2|v_2|^2
\]
only when \(\beta\le0\), unless the self-dual Weitzenböck relation is used to convert it back into the Weyl form.

At \(\rho=3/2\),
\[
m=\frac{97}{96},\qquad
q:=\frac{(2-\rho)^2(2+2\rho-\rho^2)}6=\frac{11}{96},
\qquad
p_2=\frac{13}{24}.
\]
The scalar part of the affine field expression is
\[
(1-\beta-\gamma)m-\beta q+\gamma p_2
=\frac{97}{96}-\frac98\beta-\frac{15}{32}\gamma.
\]
In the resulting \(g\)-function, the \(\beta\)-contribution is
\[
\frac98\,t\beta\le0.
\]
Thus the best useful choice is \(\beta=0\). The Nijenhuis form does not move the \(2/3\) contact point in this enlarged affine family.

---

## 7. What Theorem E establishes about pointwise compensation

The mathematically precise result is:

> Constant affine combinations of the amplitude identity, the Nijenhuis/Weyl identities, and the closed Weyl–volume identity, followed only by positivity of the discarded field terms and the sharp algebraic estimate \(|M|^2\ge\frac32x^2\), cannot produce \(C_+\ge tA\) with \(t>2/3\).

Since a lower estimate \(P\ge ck\) for \(k/A\ll1\) would require
\[
C_+\ge A-(1-c)k=tA
\]
with \(t>2/3\), this affine pointwise mechanism cannot supply such a tariff.

A stronger sentence excluding every possible pointwise or algebraic compensation mechanism is not established by the calculation. In particular, the calculation does not use:

- algebraic correlations among the \(2^k\) fields sharing the same \(W^+\);
- the full pointwise Walsh tensors before their norms are discarded;
- additional Fierz relations between different sign spinors;
- global integral constraints that may prevent an actual solution from remaining near \(\rho=3/2\);
- elliptic estimates, unique continuation, or localization of exceptional curvature.

The \(\rho=3/2\) contact is an algebraic witness for the envelope; Step 40 does not construct a closed metric and a simultaneous SW family realizing that state.

The remaining substantive quantities are exactly those identified in the note:

1. the Walsh energy
   \[
   \mathcal W
   =2\|f_\varnothing^-\|^2
   +2\sum_{I\ne\varnothing}\|f_I^+\|^2;
   \]
2. the gradient/Lee/amplitude term
   \[
   \mathbb E\|\zeta_\epsilon\|^2;
   \]
3. the harmonic projection terms \(J_\epsilon\), related to \(\mathcal W\) by
   \[
   \mathcal W
   =8\pi^2(\mathbb E p_\epsilon-A)+2\mathbb E J_\epsilon;
   \]
4. differential control of the \(\mathcal W_2\) energy and its localization near exceptional topology;
5. multi-field elliptic relations and common-Weyl correlations.

Finally, the \(F_{3/4}\) computation is consistent:
\[
F_{3/4}(\rho)\le\frac45,
\qquad
F_{3/4}(8/5)=\frac45.
\]
It yields an averaged saving-support volume estimate
\[
\mathbb E_\epsilon\operatorname{Vol}
\{F_{3/4}(\rho_\epsilon)>0\}
\ge10\pi^2(1-c)k+o(k).
\]
It does not imply that every individual sign class has that much support.

In summary, the exact mathematical core of Step 40 is sound; the principal repairs concern quantifiers, interpretation of the affine exhaustion theorem, the general-Kähler comparison, the asymptotic wording, and one small numerical value.