# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step74_neck_and_screen.py",
    "Sessions/S1003A01/workspace/data/step74/neck_and_screen.json",
    "Sessions/S1003A02/workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md"
  ]
}
```

## Task

Independently verify A01 Step-74 Theorems 74.B–D and assess the equality/attainment question for V_m. Check the mixed inequality transfer including bubble chirality and charge conventions, the Einstein-bulk optimization and asymptotic linear form, the Kähler Ricci-flat filler budget, and the screening interpretation. Then determine what, if anything, follows rigorously from W^-=0, constant s<0, |W^+|^2=s^2/24, P=8pi^2 k for an alpha_orb minimizer: does existing Derdzinski/LeBrun equality theory force a Kähler or almost-Kähler orbifold structure, and is such a structure topologically excluded on V_m? Distinguish a theorem from a plausible route and identify any exact source theorem needed.

## Output

# Verification memo: Step 74.B–D and equality on \(V_m\)

## 1. Mixed-curvature transfer, including chirality

The transfer formula in Theorem 74.B is correct under the stated scalar-flat ALE gluing hypotheses.

For the smooth resolved metrics \(g_\varepsilon\) on \(M_k\), LeBrun’s estimate gives
\[
\int_{M_k}(s_{g_\varepsilon}-\sqrt6\,|W^+_{g_\varepsilon}|)^2
\ge 72\pi^2A.
\]
On a scalar-flat filler \(N_j\), the scalar and mixed terms vanish, while the self-dual Weyl term contributes
\[
6\int_{N_j}|W^+|^2=6B_{+,j}.
\]
On the gluing annuli, the construction used in Lemma 86.S gives bounded curvature on volume \(O(\rho^4)\), so
\[
\int_{\rm annulus}s^2,\quad
\int_{\rm annulus}|W^+|^2,\quad
\int_{\rm annulus}|s|\,|W^+|
=o(1).
\]
Consequently,
\[
\int_V(s-\sqrt6|W^+|)^2+6B_+\ge72\pi^2A.
\]

The orientation dependence is essential and is recorded correctly. From
\[
P(N)=4I_+(N)+\frac{S(N)}{12}+8\pi^2c_+(N)
\]
one obtains, for a Ricci-flat filler,
\[
I_+(N)=-2\pi^2c_+(N),\qquad c_+(N)\le0.
\]
Thus
\[
\int_V(s-\sqrt6|W^+|)^2
\ge72\pi^2A+12\pi^2C_+.
\]
For a Ricci-flat Kähler filler in its complex orientation, \(W^+=0\), hence \(c_+=0\), and the smooth estimate transfers without loss. Reversing the orientation interchanges the two chiral ledgers: the same Ricci-flat metric generally has \(c_-=0\), \(c_+<0\), and contributes nonzero \(B_+\).

For a scalar-flat filler that is not Ricci-flat,
\[
B_+=I_+=\frac{P(N)}4-2\pi^2c_+(N),
\]
also as stated.

Two qualifications belong explicitly with this theorem:

1. The result remains conditional on the monopole supply (SW), including the chamber input in the fake-projective-plane case.
2. For scalar-flat fillers beyond the order-four examples, the ALE decay and derivative estimates used to make the annular integrals vanish are part of the hypotheses.

## 2. Einstein-bulk optimization

Let
\[
x=\frac{S}{96\pi^2},\qquad
T_\pm=2\chi_{\rm orb}\pm3\tau_{\rm orb}.
\]
For an Einstein orbifold, \(P=0\), and the orbifold Chern–Weil identities give
\[
I_\pm=2\pi^2(T_\pm-x).
\]
Indeed,
\[
4\pi^2T_+=\frac{S}{24}+2I_+,
\qquad
4\pi^2T_-=\frac{S}{24}+2I_-.
\]
The scalar transfer and \(I_\pm\ge0\) therefore give
\[
\frac A3\le x\le \min(T_+,T_-).
\]

Using Theorem 74.B for Ricci-flat fillers,
\[
72\pi^2A+12\pi^2C_+
\le \int_V(s-\sqrt6|W^+|)^2.
\]
The elementary estimates
\[
(s-\sqrt6|W^+|)^2\le(|s|+\sqrt6|W^+|)^2
\]
and Cauchy–Schwarz yield
\[
\int_V(s-\sqrt6|W^+|)^2
\le \left(\sqrt S+\sqrt{6I_+}\right)^2.
\]
Substituting \(S=96\pi^2x\) and \(I_+=2\pi^2(T_+-x)\) gives precisely
\[
\boxed{\left[\sqrt{8x}+\sqrt{T_+-x}\right]^2\ge6A+C_+.}
\]

Write
\[
F_T(x)=\left[\sqrt{8x}+\sqrt{T-x}\right]^2
      =T+7x+4\sqrt{2x(T-x)}.
\]
This is concave on \(0\le x\le T\), with maximum \(9T\) at \(x=8T/9\). Hence the code’s clipping of \(8T_+/9\) to
\[
\left[\frac A3,\min(T_+,T_-)\right]
\]
is the correct finite-dimensional optimization.

The conclusion \(\lambda<0\) is also valid here: resolving by Ricci-flat fillers to \(M_k\), a bulk with \(\lambda\ge0\) would produce smooth metrics whose \(L^2\)-norm of \(s^-\) tends to zero, contrary to
\[
\int_{M_k}(s^-)^2\ge32\pi^2A.
\]

## 3. Large-\(A\) expansion

Set
\[
T_+=A+e,\qquad e=C_+-k,
\]
and
\[
T_-=\frac A3+d,\qquad d=C_-+5k.
\]
For fixed \(k,C_\pm\) and \(A\to\infty\), the upper endpoint \(x=T_-\) lies below \(8T_+/9\), provided the scalar interval is nonempty. Direct expansion gives
\[
F_{T_+}(T_-)
=
6A+3e+9d-\frac{3(e-3d)^2}{4A}+O(A^{-2}).
\]
After subtracting \(6A+C_+\),
\[
F_{T_+}(T_-)-(6A+C_+)
=
9C_-+2C_++42k
-\frac{3(e-3d)^2}{4A}
+O(A^{-2}).
\]
Thus both linear forms in (3.2) are correct:
\[
C_-+5k\ge0,
\qquad
9C_-+2C_++42k\ge0
\]
at leading order. The displayed expansion applies when \(k,C_\pm\) remain fixed relative to \(A\); for proportional growth the exact formula should be used.

The subtractive \(A^{-1}\) term also correctly explains the \(A_5\) row: its linear term is zero, while \(e-3d\ne0\), so the exact margin remains below zero for every finite \(A\).

## 4. The \(C_+=0\) formula and the Kähler Ricci-flat budget

For \(C_+=0\), one has \(T_+=A-k\), and the lower root of
\[
F_{A-k}(x)=6A
\]
is
\[
x_{\min}
=\frac A{27}\left(4-\sqrt{1-\frac{3k}{A}}\right)^2.
\]
A real root with the required maximum exists only for \(k\le A/3\). Moreover,
\[
x_{\min}-\frac{A+k}{3}
=
\frac{4A}{27}\left(1-\sqrt{1-\frac{3k}{A}}\right)^2>0
\]
for \(k>0\), as stated.

For complex-oriented Ricci-flat Kähler fillers,
\[
C_-=-4Q,\qquad
Q=\sum_j\left(\chi(N_j)-\frac1{|\Gamma_j|}\right).
\]
The condition \(T_-\ge x_{\min}\) becomes
\[
\boxed{
Q\le
\frac14\left(\frac A3+5k-x_{\min}\right).
}
\]
Expanding at \(k/A\to0\),
\[
x_{\min}
=\frac A3+\frac k3+\frac{k^2}{3A}
+\frac{k^3}{2A^2}+O(k^4/A^3),
\]
and hence
\[
Q\le
\frac{7k}{6}-\frac{k^2}{12A}
-\frac{k^3}{8A^2}+O(k^4/A^3).
\]
The numerical values in the JSON agree with the exact expression.

For a connected Ricci-flat Kähler ALE filler with \(b_2=r\),
\[
\chi(N)=1+r,
\qquad
\chi(N)-\frac1{|\Gamma|}
=r+1-\frac1{|\Gamma|}.
\]
Thus, if the fillers collectively carry all \(k\) exceptional directions,
\[
\sum_j r_j=k
\quad\Longrightarrow\quad
\sum_j\left(1-\frac1{|\Gamma_j|}\right)
\le \frac k6-\frac{k^2}{12A}+O(k^3/A^2).
\]
The “roughly six ranks per filler correction” interpretation is therefore correct.

## 5. Reading the screening tables

The script implements the exact test correctly, but several prose summaries need a more precise reading.

- The labels \(c_\pm\le0\) mean only that Ricci-flatness is compatible with the two integrated chiral energies:
  \[
  I_\pm=-2\pi^2c_\pm\ge0.
  \]
  They do not produce a Ricci-flat ALE metric.

- Passing the scalar and mixed tests gives only the existence of an admissible number \(x\). It does not produce an embedding, an orbifold bulk, or an Einstein metric.

- Thresholds inferred from
  \[
  A\in\{9,18,27,36,45,90,\ldots\}
  \]
  are “first passing sampled values,” not exact thresholds among all multiples of \(9\). For example, the single \(D_6\) Kronheimer filler with \(k=6\) already passes at \(A=63\):
  \[
  Q=\frac{111}{16}=6.9375
  <
  \frac14\left(21+30-x_{\min}(63,6)\right)
  \approx6.94405.
  \]
  It does not pass at \(A=54\). Thus the exact first multiple of \(9\) is \(63\), rather than \(90\).

- The sentence that all rank-plus-one Kronheimer rows pass from \(A=9\)–\(18\) is inconsistent with the JSON. For instance, \(A_{10}\) with \(k=11\) cannot even satisfy \(k\le A/3\) before \(A=33\); its first allowed multiple in the table is \(A=36\).

- “All 98 rational-ball rows survive both tests” is correct only in the eventual, large-\(A\) sense. For example \(L(4,3)\), with \((c_+,c_-)=(-3,0)\), does not pass the mixed test at \(A=9\), but does from \(A=18\) onward.

- The orientation reversals of the T-type Ricci-flat metrics should not be grouped with wholly hypothetical rows. A T-type metric with \((c_+,c_-)=(0,-q)\) becomes an actual Ricci-flat metric with \((-q,0)\) after orientation reversal, although it is no longer Kähler in the orientation used for \(W^+\). Rows with both entries strictly below zero generally still require a separate existence theorem.

The large-\(A\) count of eight cyclic \(b_2=1\) survivors is consistent with the JSON. The paired-\(A_1\) row has
\[
C_+=0,\qquad C_-=-6k,
\]
so \(C_-+5k=-k<0\); it is excluded already by the scalar interval.

## 6. Equality equations and a direct nonattainment theorem

Suppose \(g\) attains
\[
P_{*,\rm orb}(V_m)=8\pi^2k.
\]
Then the proof of Theorem 74.A forces
\[
S=32\pi^2A,\qquad I_-=0,\qquad I_+=\frac{4\pi^2A}{3}.
\]
Therefore \(W^-=0\). Since the EH fillers have \(B_+=0\), the transferred mixed estimate and its upper Cauchy–Schwarz estimate both become equalities:
\[
72\pi^2A
\le\int(s-\sqrt6|W^+|)^2
\le\left(\sqrt S+\sqrt{6I_+}\right)^2
=72\pi^2A.
\]
Equality gives
\[
s\le0,\qquad
\sqrt6\,|W^+|=\frac{|s|}{2},
\qquad
|W^+|^2=\frac{s^2}{24}.
\]

There is, however, a simpler variational obstruction that was not used in Step 74.

On a fixed compact orbifold,
\[
P=\frac{S}{12}+2\mathcal W-16\pi^2\chi_{\rm orb}.
\]
If \(W^-=0\), the orbifold signature formula writes \(\mathcal W\) as a topological constant plus \(2I_-\). Hence the first variation of \(\mathcal W\) vanishes at \(W^-=0\). At a \(P\)-minimizer,
\[
0=\delta P=\frac1{12}\delta S.
\]
Thus \(g\) is a critical metric of \(\int s^2\). Its Euler equation is
\[
\nabla^2s-(\Delta s)g-s\,\operatorname{Ric}
+\frac14s^2g=0.
\]
Taking the trace gives \(\Delta s=0\), so \(s\) is constant on the compact orbifold. Since \(S>0\), \(s\ne0\), and the remaining equation gives
\[
\operatorname{Ric}^\circ=0.
\]
This implies \(P=0\), contradicting \(P=8\pi^2k>0\).

Therefore:

\[
\boxed{\inf_{\mathscr G_{\rm orb}(V_m)}P=8\pi^2k
\text{ is never attained for }k\ge1.}
\]

For the human functional this yields:

- If \(k<A/3\), an \(\alpha_{\rm orb}\)-minimizer would necessarily have \(P=8\pi^2k\) and \(L_s=0\). Hence it cannot exist.
- If \(k>A/3\), the strict inequality \(4P/R>1\) already gives nonattainment.
- If \(k=A/3\), an attainer would satisfy
  \[
  W^-=0,\qquad s\equiv{\rm const}<0,
  \]
  but it cannot also have \(S=32\pi^2A\). Thus any such metric must have
  \[
  S>32\pi^2A,\qquad P>8\pi^2k.
  \]
  The supplied results do not exclude this remaining constant-scalar half-conformally-flat possibility.

So the only unsettled attainment case is the wall \(k=A/3\), and there the stronger relation
\[
|W^+|^2=s^2/24,\qquad P=8\pi^2k
\]
cannot occur.

## 7. Derdziński and LeBrun equality theory

The displayed tensor conditions alone do not force a Kähler or almost-Kähler structure.

The relevant Derdziński theorem requires two additional inputs:

1. \(\delta W^+=0\);
2. \(W^+\) has at most two eigenvalues on the set where it is nonzero.

It then makes a conformal rescaling Kähler. Since \(|W^+|\) is constant in the present equality configuration, that conformal factor would be constant, so the original metric would be Kähler. But neither missing input follows here:

- \(W^-=0\) implies Bach-flatness, not \(\delta W^+=0\);
- with \(s\) constant,
  \[
  \delta W^+\ \text{is controlled by }d^\nabla\operatorname{Ric}^\circ,
  \]
  which need not vanish;
- the scalar identity \(|W^+|^2=s^2/24\) fixes only the norm of a trace-free symmetric \(3\times3\) operator and does not fix its eigenvalue multiplicities.

The exact Derdziński result relevant to such a route is the harmonic-self-dual-Weyl, two-eigenvalue conformally Kähler theorem from *Self-dual Kähler manifolds and Einstein manifolds of dimension four*, Compositio Math. 49 (1983). Its hypotheses are absent here.

LeBrun’s smooth equality theory also cannot presently be applied directly. Theorem 74.B transfers only the numerical inequality. The smooth metrics \(g_\varepsilon\) may use different monopole classes, and no convergence of the corresponding monopole solutions to an orbifold solution on \(V_m\) has been established. Even if the smooth equality clause for the mixed estimate produces an almost-Kähler form, one still needs:

- a fixed monopole class along the degeneration, or compactness for the varying solutions;
- a nonzero limiting self-dual form on the regular locus;
- orbifold extension across the \(A_1\) points;
- the exact equality clause from the cited source, not only Proposition 3.8’s numerical inequality.

Thus an orbifold equality theorem for the transferred LeBrun estimate is additional mathematics, rather than a consequence of (2.1).

## 8. Topology of a hypothetical Kähler or almost-Kähler structure

A Kähler orbifold structure in the orientation used here is excluded by the supplied parity lemma. Resolving the \(2m=k\) \(A_1\) points gives \(M_k\) with disjoint \((-2)\)-classes \(C_j\). By the topological input (R), their rational span contains all the odd-square exceptional classes \(E_i\). Crepancy gives
\[
K\cdot C_j=0.
\]
Hence \(K\cdot E_i=0\), while a canonical class is characteristic and must satisfy
\[
K\cdot E_i\equiv E_i^2\equiv1\pmod2,
\]
a contradiction.

The same argument would exclude an almost-Kähler orbifold once one has the local symplectic \(A_1\)-resolution lemma: an orbifold symplectic form can be resolved to a symplectic form on \(M_k\) for which every exceptional \((-2)\)-sphere is symplectic. Adjunction then again gives \(K_\omega\cdot C_j=0\), followed by the same characteristic-class contradiction.

The complex crepant version is already present in the theorem package. For the almost-Kähler version, the remaining item is an explicit proof or citation for the local symplectic resolution that preserves the ambient orientation and makes the \(A_1\) spheres symplectic. Once that lemma is supplied, the topological exclusion is complete.

## Conclusion

- Theorems 74.B and 74.C, including chirality, charge signs, optimization, and the asymptotic form, are mathematically consistent.
- Corollary 74.D and its exact budget are correct.
- The screening code evaluates the intended necessary test, but several prose thresholds are only sampled thresholds; the \(D_6\) and rank-plus-one summaries need correction.
- Passing the screen supplies no metric, embedding, or Einstein bulk.
- The tensor equalities do not activate Derdziński’s theorem, and the transferred LeBrun estimate does not by itself produce an orbifold almost-Kähler form.
- A direct first-variation argument proves that the \(P\)-infimum on \(V_m\) is never attained and that \(\alpha_{\rm orb}\) is not attained whenever \(k\ne A/3\).
- At \(k=A/3\), only a constant-\(s<0\), \(W^-=0\), strictly-above-\(P\)-infimum metric remains possible from the present equations.