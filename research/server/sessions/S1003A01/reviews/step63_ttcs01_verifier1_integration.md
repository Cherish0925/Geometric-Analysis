# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 63,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step63_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step63_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the Step-63 diagonal Bianchi-IX regular-nut calculation and its mathematical interpretation for the closed negative-scalar Goldberg problem. Read the note and exact scripts/data. Verify: (i) the u=t^2 Einstein and closure equations and regular-nut parameter count; (ii) whether the exact L1,...,L5 ideal and Singular localization really exclude all interior three-weight, genuinely triaxial branches through this order; (iii) whether the three associated components are exactly permutations of the stated complex-hyperbolic Kähler branch, including the closed-form sinh identification and q=0; (iv) what is proved versus only suggested about all-order formal or analytic branches. Identify any normalization, smoothness, ideal-theoretic, or overinterpretation errors and give corrected theorem wording.

## Integrated Scientific Memo

# Verification memo: Step-63 regular-nut calculation

## Conclusion

The supplied equations and exact algebra support the intended obstruction: **a real diagonal Bianchi-IX Einstein regular nut with an invariant closed self-dual form of constant length cannot produce a strict almost-Kähler germ.** The surviving real data are precisely the three permutations of the complex-hyperbolic Kähler data.

The note nevertheless needs four substantive corrections:

1. The normalized polynomial ideal has dimension **one**, not two. The reported second dimension is the unused localization variable \(z\).
2. Its three minimal-prime components are **affine lines**, not three points. Nonnegativity of the real squared weights cuts each line down to one point.
3. The form selects the **simple** curvature eigenline, not the repeated eigenspace.
4. Agreement through five orders alone does not establish all-order rigidity. An explicit nonresonant recurrence, derived below, supplies the missing argument.

The Singular output establishes the relevant algebraic zero-set conclusion; it does **not** establish a primary decomposition or that the original ideal is radical. Neither additional assertion is needed.

## 1. Equations, normalization, and regular-nut parameters

Fix cyclic indices and
\[
d\sigma_i=2\sigma_j\wedge\sigma_k,\qquad
g=dt^2+\sum_i a_i^2\sigma_i^2.
\]
This normalization makes \(\sum_i\sigma_i^2\) the unit round three-sphere metric, compatible with a smooth ordinary nut having \(a_i/t\to1\). A different structure-constant normalization would require different leading coefficients.

Writing \(h_i=\dot a_i/a_i\), the spatial Ricci components are
\[
\operatorname{Ric}_{ii}
=-\frac{\ddot a_i}{a_i}-h_i(h_j+h_k)
+2\frac{a_i^4-(a_j^2-a_k^2)^2}{a_i^2a_j^2a_k^2}.
\]
Set
\[
u=t^2,\qquad a_i=tf_i(u),\qquad
H_i=1+2u\frac{f_i'}{f_i},\qquad
Z_i=\frac{f_i}{f_jf_k}.
\]
Multiplying the Einstein equation by \(t^2\) gives
\[
2uH_i'-H_i+H_i\sum_\ell H_\ell
-2\bigl[Z_i^2-(Z_j-Z_k)^2\bigr]+\lambda u=0.
\]
The Hamiltonian constraint is
\[
C=\sum_{i<j}H_iH_j+\sum_iZ_i^2
-2\sum_{i<j}Z_iZ_j+\lambda u=0.
\]
Thus the signs and coefficients in `step63_bianchiIX_nut_series.py` are correct for \(\lambda=-3\), with scalar curvature \(s=-12\).

### Lowest-order data

For \(f_i=1+A_i u+O(u^2)\), the coefficient of \(u\) in each Einstein equation and in \(C\) is
\[
6\sum_i A_i+\lambda.
\]
Consequently
\[
\sum_iA_i=\frac12,\qquad
A_i=\frac16+d_i,\qquad \sum_i d_i=0.
\]
There are exactly two free cubic metric coefficients in the fixed diagonal gauge. The script assumes this order-one relation rather than checking it; the relation is correct.

### All-order recurrence

Add a new coefficient \(b_i u^n\) to each \(f_i\), and write \(B=\sum_i b_i\). Its contribution to the order-\(u^n\) Einstein equations is
\[
\delta E_i=2(n+2)\bigl(2(n-1)b_i+B\bigr).
\]
The coefficient matrix has eigenvalues
\[
4(n+2)(n-1)\quad\text{on the trace-free subspace},
\]
and
\[
2(n+2)(2n+1)\quad\text{on the trace direction}.
\]
The trace-free resonance at \(n=1\) accounts for the two nut parameters. For every \(n\ge2\), the matrix is invertible, independently of \(d\). Hence the higher formal coefficients are uniquely determined by those parameters.

The Hamiltonian is also consistent at all orders, rather than merely in the recorded checks. Let \(S=\sum_i h_i\). If the spatial Einstein equations hold, the contracted Bianchi identity implies, for
\(e=\operatorname{Ric}_{tt}-\lambda\),
\[
\dot e=-2Se.
\]
The Gauss identity gives \(e=2C/t^2\), so
\[
2uC'=2\bigl(1-\sum_iH_i\bigr)C.
\]
Since \(\sum_iH_i(0)=3\), a nonzero leading formal coefficient \(C\sim c u^m\) would require \(m=-2\). Thus an analytic or formal regular-nut solution of the spatial equations has \(C\equiv0\).

### Closure and length

Use the orthogonal self-dual basis
\[
\omega_i=dt\wedge(a_i\sigma_i)+a_ja_k\,\sigma_j\wedge\sigma_k,
\qquad |\omega_i|^2=2.
\]
For \(\Omega=\sum_i x_i\omega_i\), direct differentiation gives
\[
d\Omega=0
\iff
\frac{d}{dt}(x_i a_ja_k)=2x_i a_i.
\]
Equivalently,
\[
2u x_i'=M_i x_i,\qquad M_i=2Z_i-H_j-H_k.
\]
For \(X_i=x_i^2\),
\[
uX_i'=M_iX_i,\qquad |\Omega|^2=2\sum_iX_i.
\]
These are exactly the script’s equations.

Here \(M_i(0)=0\), and in fact
\[
M_i=(6d_i-1)u+O(u^2),
\]
matching the stored first coefficients. The apparent singular transport equation is regular after dividing \(M_i\) by \(u\):
\[
X_i(u)=R_i\exp\left(\int_0^u\frac{M_i(v)}v\,dv\right).
\]
For a real form,
\[
R_i=x_i(0)^2\ge0,\qquad \sum_iR_i=1.
\]
In particular, a zero initial component remains identically zero. No extra component can first appear at a higher order.

For an actual smooth nut, the parity and extension conditions matter: the scalar coefficients are smooth functions of \(t^2\), with \(f_i(0)=1\). Merely imposing a leading slope on a punctured-orbit solution would not by itself justify smooth extension. The stated regular-nut ansatz supplies the required setting.

## 2. What the exact ideal proves

Let
\[
I=\langle L_1,\ldots,L_5\rangle
\subset\mathbb Q[R_1,R_2,d_1,d_2],
\qquad R_3=1-R_1-R_2.
\]
All denominators in the supplied length conditions are nonzero rational constants, so clearing them does not change the ideal’s zero set.

The localization polynomial is
\[
P=R_1R_2R_3(d_1-d_2)(2d_1+d_2)(d_1+2d_2).
\]
Since \(d_3=-d_1-d_2\), the final two factors are \(d_1-d_3\) and \(d_2-d_3\).

The supplied Singular output reports
\[
\operatorname{std}\bigl(I+\langle1-zP\rangle\bigr)=\langle1\rangle.
\]
This is the correct Rabinowitsch test. It excludes, even over the complex numbers, every common zero of the five constraints with all weights nonzero and all three cubic eigenvalues distinct. It establishes an empty localized **zero set**, not merely a failure of numerical solving.

### Correct reading of the minimal primes

Simplifying the printed generators gives the three lines
\[
\begin{aligned}
\ell_1:\;&d=(1/6,-1/12,-1/12),&
R&=(1,r,-r),\\
\ell_2:\;&d=(-1/12,1/6,-1/12),&
R&=(r,1,-r),\\
\ell_3:\;&d=(-1/12,-1/12,1/6),&
R&=(r,-r,1).
\end{aligned}
\]
For example, in the third printed prime, substituting \(d_2=-1/12\) reduces the remaining two generators to
\[
1728d_1-288,\qquad 432R_1-432.
\]
Thus \(d_1=1/6\), \(R_1=1\), but \(R_2\) remains free.

The output therefore supports
\[
V_{\mathbb C}(I)=\ell_1\cup\ell_2\cup\ell_3.
\]
These rational linear primes also settle the geometric components over \(\mathbb C\). The result is stronger than the interior localization: **all** complex solutions have the stated biaxial cubic metric data, including solutions with zero weights.

The lines arise because the two repeated directions have identical closure transport. Opposite algebraic weights cancel in the length sum. Such cancellation is unavailable for real squared coefficients. Indeed,
\[
R_i\ge0
\]
forces \(r=0\) on every line. The real geometric feasible set is exactly the three stated vertices.

Two distinctions must be retained:

- The algebraic components have complexified, signed-weight points that are not real almost-Kähler data. The components themselves are not “exactly the three real Kähler branches.”
- `minAssGTZ` reports minimal associated primes. It determines the support needed here, but says nothing by itself about embedded primes, multiplicities, or radicality of \(I\).

### Dimension error

The Singular ring is
\[
\mathbb Q[R_1,R_2,d_1,d_2,z].
\]
The full ideal does not involve \(z\). Accordingly,
\[
\dim\bigl(\mathbb Q[R_1,R_2,d_1,d_2,z]/I\bigr)=2
\]
means that the geometric four-variable quotient has dimension **one**. The note’s dimension-two statement omits this auxiliary-variable distinction.

The supplied materials do not contain the trajectories behind the “119 least-squares solutions.” The algebra rules out 119 distinct exact real normalized solutions; it does not verify where each numerical trajectory converged.

## 3. Closed-form identification and exact \(q=0\)

At the first real vertex,
\[
A_1=\frac13,\qquad A_2=A_3=\frac1{12}.
\]
The closed form is
\[
a_1=\frac{\sinh(\sqrt2\,t)}{\sqrt2},
\qquad
a_2=a_3=\sqrt2\sinh(t/\sqrt2).
\]
Its coefficients are
\[
f_1=\sum_{n\ge0}\frac{(2u)^n}{(2n+1)!},
\qquad
f_2=f_3=\sum_{n\ge0}\frac{(u/2)^n}{(2n+1)!},
\]
which reproduce all five listed orders.

Put \(\rho=t/\sqrt2\). Then
\[
g=2\left[
d\rho^2+\sinh^2\rho
\bigl(\sigma_2^2+\sigma_3^2+\cosh^2\rho\,\sigma_1^2\bigr)
\right].
\]
This is the complex-hyperbolic polar metric, with \(\operatorname{Ric}=-3g\) and holomorphic sectional curvature \(-2\), in the fixed structure-constant normalization.

Exact substitution can be made without relying on truncated series:
\[
\begin{aligned}
H_1&=\rho(\coth\rho+\tanh\rho),&
H_2=H_3&=\rho\coth\rho,\\
Z_1&=\rho\coth\rho,&
Z_2=Z_3&=\rho(\coth\rho-\tanh\rho).
\end{aligned}
\]
These satisfy the Einstein equations and Hamiltonian constraint identically. They also give
\[
M_1=0,\qquad
b_2=H_2-Z_1+Z_2-Z_3=0,\qquad
b_3=H_3-Z_1-Z_2+Z_3=0.
\]
For \(X=(1,0,0)\), all terms in the supplied torsion formula vanish:
\[
q=\frac2u\left[
\sum_iX_iM_i^2
+(X_1+X_2)b_3^2
+(X_1+X_3)b_2^2
+(X_2+X_3)b_1^2
\right]=0.
\]
Thus \(\Omega=\pm\omega_1\) is parallel, exactly, not just to finite order. Closure is also visible directly from
\[
(a_2a_3)'=2a_1.
\]

The algebraic lines have an exact transport explanation:
\[
M_2=M_3=-3\rho\tanh\rho,\qquad
X_2=R_2\cosh^{-6}\rho,\quad
X_3=R_3\cosh^{-6}\rho.
\]
Hence
\[
\sum_iX_i=R_1+(R_2+R_3)\cosh^{-6}\rho.
\]
This confirms the cancellation mechanism on \(\ell_1\) at all orders, while showing why positivity is essential to its real interpretation.

### Scope of the \(q\) script

`step63_nut_q.py` is a finite-series check, not an exact proof of parallelism. In its branch-output loop, `series(Qnum,...,0,5)` retains the numerator through \(u^4\), then divides by \(u\). Thus the printed branch result checks \(q\) through \(u^3\), i.e. \(q=O(u^4)\). The earlier generic variable `q` is not used in that output. Exact \(q=0\) follows from the closed-form identities above.

### Eigenline correction

On the Kähler branch,
\[
\operatorname{spec}(W^+)=(-2,1,1),
\]
since \(s=-12\). The selected form spans the simple eigenline with eigenvalue \(s/6=-2\); the repeated eigenspace is its orthogonal complement. The note’s “align with a repeated metric-curvature eigenspace” is reversed.

## 4. All-order rigidity and corrected theorem

Five computed orders alone would not identify an arbitrary infinite series. Here the missing implication is supplied by the recurrence:

1. Every all-order real solution satisfies the first five length conditions.
2. Their real nonnegative zero set fixes \(d\) and the form’s initial direction to one of the three vertices.
3. The Einstein recurrence is invertible at every subsequent order.
4. The explicit complex-hyperbolic solution has exactly those initial data, so it is the unique formal metric.
5. Closure transport uniquely fixes the form: the two zero components stay zero, and the remaining component is \(\pm1\).

No convergence theorem for the entire two-parameter Einstein family is needed to conclude this rigidity: the only surviving formal solution is explicitly convergent.

**Corrected theorem.**  
Fix \(d\sigma_i=2\sigma_j\wedge\sigma_k\). Let
\[
g=dt^2+\sum_i a_i(t)^2\sigma_i^2,\qquad
a_i=t f_i(t^2),\qquad f_i(0)=1,
\]
be a real formal regular-nut metric satisfying \(\operatorname{Ric}=-3g\). Let
\[
\Omega=\sum_i x_i(t^2)\omega_i
\]
be a real invariant self-dual formal form satisfying \(d\Omega=0\) and \(|\Omega|^2=2\). Then, after permuting axes,
\[
a_1=\frac{\sinh(\sqrt2\,t)}{\sqrt2},\qquad
a_2=a_3=\sqrt2\sinh(t/\sqrt2),\qquad
(x_1,x_2,x_3)=(\pm1,0,0).
\]
In particular, the unique formal solution is convergent and Kähler.

The same conclusion holds for analytic germs. For smooth genuine Einstein regular-nut germs it also follows using Einstein analytic regularity: the metric is analytic in an appropriate coordinate atlas, and the closed self-dual form is harmonic and therefore analytic there. Geodesic radial coordinates and the regular-nut parity identify the corresponding convergent radial series. Formal uniqueness then gives equality of germs. Smooth Taylor agreement alone, without this analytic-regularity input or another uniqueness argument, would not suffice.

The theorem should explicitly assume **self-duality/almost-Kähler compatibility**. Closedness and constant length alone, for a general two-form, are not the hypotheses used by the calculation.

## 5. Interpretation and remaining boundary

This proves local rigidity in the specified diagonal, fully invariant class. It excludes the proposed strict isolated torsion-zero nut construction: the sole admissible model has torsion zero throughout a neighborhood.

It does not resolve the closed negative-scalar Goldberg problem, or the existence of unrestricted strict analytic germs with isolated torsion zeros. Step 62’s necessary cone relation and index theorem remain compatible with this result; its finite-order numerical tests are not existence proofs.

There is a plausible enlargement beyond diagonal metrics, but it is not established by the supplied scripts. For a general orbit matrix
\[
h=t^2(I+uB+u^2B_2+\cdots),
\]
the order-by-order equations at the round leading orbit are \(SO(3)\)-equivariant. The trace-free symmetric representation is irreducible, suggesting the same nonresonance mechanism. If a unique full matrix recurrence is established, diagonalizing \(B\) and using its diagonal sign-change stabilizer would force every \(B_n\) to be diagonal. What remains to verify is the full matrix Einstein recurrence together with the mixed/momentum constraints. This argument is a concrete possible extension, not permission to remove “diagonal” from the present theorem.

Finally, the separate clean-zero-surface argument is consistent with the supplied Step-62 cone and curvature dictionary:
\[
2\pi c_1(M,J)[C]=\frac{s}{4}\operatorname{Area}(C),\qquad
\deg(K_J^{-2}|_C)=\frac{s}{4\pi}\operatorname{Area}(C).
\]
It excludes a closed torsion-zero surface with nonzero first torsion derivative everywhere. If the rank-two locus is merely dense, writing the degree as a sum of local winding numbers requires **isolated zeros** of the restricted section \(W_3^+\). Density alone does not ensure that. Without isolated zeros, the degree remains a valid characteristic-class statement, but not the claimed pointwise localization formula.