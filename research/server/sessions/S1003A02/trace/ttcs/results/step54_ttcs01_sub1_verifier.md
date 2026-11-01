# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/workspace/data/step54_charge_and_entropy_checks.json",
    "Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md",
    "Sessions/S1003A02/trace/ttcs/results/step53_ttcs01_verifier1_integration.md",
    "Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/web_research_collected.tex"
  ]
}
```

## Task

Verify, adversarially and constructively, Theorem 54.A and Lemmas 54.1-54.3 in step54_k1_ball_quotient_attainment_theorem.md. The setting: X compact ball quotient other than a fake projective plane, M = X # CPbar^2, P = int |Ric°|^2; an Anderson case-(I) minimizing configuration with only trivial-group cone points. Check in particular: (1) Lemma 54.1 two-orientation cost formula c(N)=4(e-1)+4b1+b^- - 5b^+ for multi-ended AE bubbles with Gamma=1, including the boundary-term hypotheses; (2) Lemma 54.2: is each capped bubble really a connected summand of M, including multi-ended bubbles and graph loops; (3) Lemma 54.3: M=Z#R, b+(M)>=2, Z PSC with b+(Z)>=1 implies SW_M=0 even when b+(R)=0 -- is the neck-stretching argument correct (reducibles on Z side avoided by generic perturbation; irreducibles by PSC)? Is there a known counterexample or a cleaner citation? (4) the pi_1 argument: freely indecomposable PD4 lattice, Hopf surjection H2(Y)->H2(pi1 Y), conclusion that each bubble compactification is a homotopy sphere; (5) part (iii): SW_{V#Sigma}=SW_V for a PSC homotopy sphere; constant negative scalar curvature; Einstein-or-non-Bach-flat; the 'no bubbles if all hat N_k are standard S^4' step via Bishop-Gromov; (6) whether the upper bound (U) p_*(M)<8 pi^2 legitimately follows from the analytic CH-collar cell of web_research_collected.tex Ch.5 for EVERY non-fake-plane ball quotient (collar radius issue); (7) the general-k extension inequality sum[4(e-1)+4b1+beta] < k and its use of Lemma 54.3; (8) the collapse lemma (free circle action region is spin, so cannot carry E) and the orbifold parity remark (absorbing E needs a in H2(X) with a^2=-1 when m=1); (9) the BCG+Bishop computation in data JSON and Remark 4; (10) the answer to A01 on Koiso local rigidity near ball quotients (TT gap 2 from Rcirc eigenvalues -2,+4). Give corrected statements where something fails, and say precisely which hypotheses (H_sm, H_lsc, H_dec, H_eq, H_rem) each conclusion needs. Also assess whether the 'gate economy' paragraph's analysis of the rescaled perturbation coefficient eps*ell^{4-4p} is right and whether a better choice of p(eps) or a different argument gives bubble-scale P-criticality.

## Output

# Scientific verification memo: Step 54

## 1. Main assessment

The central conclusion of Theorem 54.A can be retained under the stated hypotheses, but the proof of part (i) must be reordered. The sentence following Lemma 54.1 asserting that every bubble with \(e\ge2\) or \(b_1\ge1\) costs at least \(8\pi^2\) is false for an indefinite compactification. Consequently, the deduction
\[
c(N)\le0,\quad c(\bar N)\le0
\quad\Longrightarrow\quad
e=1,\ b_1=0
\]
is also false.

The theorem is repaired as follows:

1. Lemma 54.2 makes every capped bubble \(\widehat N\) a connected summand of \(M\) and gives it a PSC metric.
2. Lemma 54.3 and \(SW_M\neq0\) then imply \(b^+(\widehat N)=0\).
3. Only after this step does Lemma 54.1 give
   \[
   P(N)\ge8\pi^2\bigl[4(e-1)+4b_1+b^-\bigr].
   \]
4. Since every \(P(N)<8\pi^2\), the bracket vanishes, yielding
   \[
   e=1,\qquad b_1=0,\qquad b^-=0.
   \]

With this repair, the homology and \(\pi_1\) arguments lead to homotopy-sphere compactifications as stated.

---

## 2. Lemma 54.1: the two-orientation formula

Let \(N\) have \(e\) AE ends, all modeled on \(\mathbb R^4\setminus B\), and let \(\widehat N\) be obtained by adding one point at each end. Assume in every end chart
\[
g_{ij}-\delta_{ij}=O(r^{-\tau}),\qquad
\partial^j g=O(r^{-\tau-j})
\]
for some \(\tau>0\) and enough derivatives to pass the Chern–Gauss–Bonnet and signature transgressions to the limit; derivatives through order two give curvature integrability, while a formulation through order three is preferable when invoking the full Chern–Simons convergence directly. Then
\[
\chi(N)=\chi(\widehat N)-e,
\]
and the Euclidean end correction contributes one further unit per end. Thus the effective Euler quantity appearing in Chern–Gauss–Bonnet is
\[
\chi(N)-e=\chi(\widehat N)-2e.
\]
The signature is unchanged by deleting finitely many points:
\[
\tau(N)=\tau(\widehat N).
\]

Therefore
\[
\begin{aligned}
2(\chi(N)-e)+3\tau(N)
&=2\chi(\widehat N)-4e+3\tau(\widehat N)\\
&=4-4e-4b_1+5b^+-b^-\\
&=-\bigl[4(e-1)+4b_1+b^--5b^+\bigr].
\end{aligned}
\]
Inserting this into the noncompact Chern–Weil identity gives
\[
P(N)
=
4\int_N|W^+|^2+\frac1{12}\int_Ns^2
+8\pi^2c(N),
\]
where
\[
c(N)=4(e-1)+4b_1+b^--5b^+.
\]
Reversing orientation exchanges \(b^+\) and \(b^-\), so
\[
P(N)
=
4\int_N|W^-|^2+\frac1{12}\int_Ns^2
+8\pi^2c(\bar N),
\]
with
\[
c(\bar N)=4(e-1)+4b_1+b^+-5b^-.
\]
Hence
\[
P(N)\ge8\pi^2\max\{c(N),c(\bar N),0\}.
\]

This part of Lemma 54.1 is correct.

### The incorrect consequence after the lemma

The formula does not imply a cost of \(8\pi^2\) whenever \(e\ge2\). For example,
\[
e=2,\quad b_1=0,\quad b^+=b^-=1
\]
gives
\[
c(N)=c(\bar N)=0.
\]
This topology is realized by a scalar-flat two-ended AE metric: start with a PSC metric on \(S^2\times S^2\), take the sum of two positive Green functions for its conformal Laplacian, and conformally blow up at the two poles. The resulting metric on
\[
(S^2\times S^2)\setminus\{p,q\}
\]
is complete, scalar-flat and AE at both ends.

Likewise, \(b_1\ge1\) alone does not force the stated cost. Algebraically,
\[
e=1,\quad b_1=1,\quad b^+=b^-=1
\]
again gives \(c(N)=c(\bar N)=0\); a one-pole Green construction on
\[
(S^1\times S^3)\#(S^2\times S^2)
\]
provides the corresponding scalar-flat AE geometry.

The semidefinite nonzero case is different: if exactly one of \(b^\pm\) is nonzero, one of the two orientation formulas produces a positive integral charge. That portion of the discussion is correct.

---

## 3. Lemma 54.2: connected-summand topology

For a connected gluing graph \(\mathcal G\) whose links are all \(S^3\), cap every incident \(S^3\) by a standard \(4\)-ball. If the resulting closed vertex manifolds are \(Y_v\), then successive \(S^3\)-gluings give
\[
M\cong
\#_{v}Y_v\ \#\
\#^{\,b_1(\mathcal G)}(S^1\times S^3).
\]
A spanning tree of \(\mathcal G\) produces the ordinary connected sum of the vertex caps; every remaining graph edge adds one \(S^1\times S^3\) factor. Thus every capped bubble is individually a connected summand of \(M\), even when:

- the bubble has several AE ends;
- the gluing graph has multiple edges;
- an edge joins two already connected portions;
- graph cycles occur.

This proves the topological content of Lemma 54.2, provided every spherical attachment is recorded in \(\mathcal G\). For a multiscale bubble tree, one should either record every resolved puncture as an incident edge or aggregate each rooted subtree before applying this formula. The statement “a second bulk component requires a multi-ended bridge” uses this rooted-tree convention.

The PSC statement also follows from the corrected Lemma 53.Y: scalar-flat AE geometry with derivative-controlled order \(\tau>0\) makes the compactification admit a smooth PSC metric. For several ends, all ends are compactified simultaneously. No metric removability at the original cone points is needed for the connected-sum topology; trivial links are already topological \(4\)-balls.

---

## 4. Lemma 54.3: PSC summand with \(b^+>0\)

The lemma is mathematically consistent, including the case \(b^+(R)=0\).

Let
\[
M=Z\#R,\qquad b^+(M)>1,
\]
where \(Z\) admits a PSC metric and \(b^+(Z)\ge1\). Put the PSC metric on \(Z\setminus B^4\) into product form near its cylindrical end and stretch the \(S^3\)-neck.

For any fixed Spin\(^c\) structure on \(M\), choose a sufficiently small self-dual perturbation \(\eta\) supported in the \(Z\)-piece.

### Irreducible solutions on \(Z\)

The perturbed Weitzenböck identity excludes irreducibles if \(\|\eta\|_\infty\) is small compared with the positive scalar minimum. This remains valid on the cylindrical completion because the cylindrical region also has positive scalar curvature.

### Reducible solutions on \(Z\)

A reducible would require
\[
2\pi\,\mathcal H^+\bigl(c_1(L)|_Z\bigr)
=
\mathcal H^+(\eta)
\]
in the \(L^2\) harmonic self-dual space. That space has dimension \(b^+(Z)\). Compactly supported perturbations have enough harmonic projections to avoid this one prescribed value. Thus a small generic \(\eta\) removes reducibles as well.

### Neck stretching

A sequence of monopoles on longer and longer necks would converge to finite-energy monopoles on the two cylindrical pieces. The round \(S^3\) has only its flat reducible critical point, and it is nondegenerate after the usual gauge fixing. Since the \(Z\)-piece has no limiting monopole, the moduli space on \(M\) is empty for sufficiently long neck.

Because \(b^+(M)>1\), the ordinary Seiberg–Witten invariant is independent of metric and generic perturbation. Hence every ordinary invariant vanishes.

When \(b^+(R)=0\), additivity gives
\[
b^+(Z)=b^+(M)>1,
\]
so the argument is no weaker; in fact the harmonic space on the PSC side has dimension at least two.

The supplied materials do not give a theorem number for this precise one-sided PSC connected-sum formulation. A precise source request would be: a Seiberg–Witten neck-stretching theorem across \(S^3\) proving vanishing when one summand has PSC and \(b^+>0\), while the total manifold has \(b^+>1\). The proof written in Step 54 is a correct outline of that theorem.

---

## 5. Corrected proof of Theorem 54.A(i)–(ii)

The analytic CH cell gives
\[
p_*(M)<8\pi^2.
\]
Under \(\mathrm H_{\mathrm{lsc}}\),
\[
p_*(M)\ge P(V,g_0)+\sum_kP(N_k).
\]
Since all terms are at least zero,
\[
P(N_k)<8\pi^2
\]
for every bubble.

By \(\mathrm H_{\mathrm{dec}}\), every \(\widehat N_k\) admits a PSC metric. By Lemma 54.2 it is a connected summand of \(M\). If \(b^+(\widehat N_k)\ge1\), Lemma 54.3 would make all Seiberg–Witten invariants of \(M\) vanish. But
\[
M=X\#\overline{\mathbb{CP}}^2
\]
has nonzero invariants by Taubes’ theorem for the ball quotient and the blow-up formula. Therefore
\[
b^+(\widehat N_k)=0.
\]

Now Lemma 54.1 becomes
\[
P(N_k)\ge
8\pi^2\bigl[
4(e_k-1)+4b_1(\widehat N_k)+b^-(\widehat N_k)
\bigr].
\]
The bracket is an integer at least zero. Since \(P(N_k)<8\pi^2\), it must vanish:
\[
e_k=1,\qquad
b_1(\widehat N_k)=0,\qquad
b^-(\widehat N_k)=0.
\]
Together with \(b^+=0\), every \(\widehat N_k\) is a rational homology \(4\)-sphere.

Once all bubbles are one-ended, the rooted case-(I) graph has one bulk component and no bridging bubble between distinct bulk components. Thus
\[
M\cong V\#\Sigma,\qquad
\Sigma=\#_k\widehat N_k.
\]

### Fundamental group

Since \(X\) is aspherical,
\[
\pi_1(M)=\pi_1(X)=\Gamma.
\]
The connected-sum decomposition gives
\[
\Gamma
\cong
\pi_1(V)*
\pi_1(\widehat N_1)*
\cdots.
\]
A torsion-free cocompact complex-hyperbolic lattice is a \(PD_4\) group and is one-ended, hence freely indecomposable. Therefore at most one factor in this free product is nontrivial. If a bubble factor were nontrivial, it would be isomorphic to \(\Gamma\).

For any connected CW complex \(Y\), the Hopf exact sequence contains
\[
H_2(Y;\mathbb Q)\longrightarrow
H_2(\pi_1Y;\mathbb Q)\longrightarrow0.
\]
Taking \(Y=\widehat N_k\), its rational \(H_2\) is zero, while
\[
H_2(\Gamma;\mathbb Q)
=
H_2(X;\mathbb Q)\neq0
\]
because \(X\) is aspherical and \(b_2(X)\ge1\). This is impossible. Hence
\[
\pi_1(\widehat N_k)=1.
\]

For a closed simply connected oriented \(4\)-manifold, \(H_2\) is torsion-free by universal coefficients and Poincaré duality. Thus each \(\widehat N_k\) is an integral homology sphere. Hurewicz and Whitehead then make it a homotopy \(4\)-sphere, and Freedman gives
\[
\widehat N_k\approx S^4.
\]

This proves parts (i) and (ii) after the proof-order correction. Since the bubble summands have \(H_2=0\), the exceptional class \(E\) lies in the bulk summand.

For such a bubble,
\[
e=1,\quad b_1=b_2=0,\quad s=0,
\]
so both orientation formulas reduce to
\[
P(N_k)=4\int|W^+|^2
      =4\int|W^-|^2,
\]
and every individual value is below \(8\pi^2\).

---

## 6. Part (iii)

Under \(\mathrm H_{\mathrm{eq}}\) and \(\mathrm H_{\mathrm{rem}}\), the bulk metric extends smoothly across all trivial-link points, and the attainment-transfer argument gives
\[
P(g_0)=p_*(V),\qquad
p_*(M)=p_*(V)+\sum_kP(N_k).
\]

### Standard \(S^4\) compactifications

If every \(\widehat N_k\) is diffeomorphic to \(S^4\), then
\[
V\cong M,
\]
so \(p_*(V)=p_*(M)\). The energy identity forces
\[
\sum_kP(N_k)=0.
\]
Every bubble is scalar-flat, hence \(P(N_k)=0\) gives \(\operatorname{Ric}=0\). A complete Ricci-flat one-ended AE manifold with trivial group is Euclidean: the Bishop–Gromov ratio starts at \(1\), tends to \(1\) at infinity, and is monotone, so equality holds at every radius. Its rigidity case gives
\[
N_k\cong\mathbb R^4
\]
isometrically. Such a flat intermediate scale carries no curvature concentration and is removed from the bubble tree. Thus no nontrivial bubbles remain.

### Seiberg–Witten invariant under a PSC homotopy sphere

Let \(\Sigma\) be the connected sum of the bubble compactifications. It is a homotopy sphere and has a PSC metric. Its unique Spin\(^c\) structure has a single reducible solution; PSC removes the Dirac kernel, while
\[
H^1(\Sigma)=H^+(\Sigma)=0
\]
removes the remaining deformation and obstruction spaces. Standard connected-sum gluing therefore gives, up to the orientation sign,
\[
SW_{V\#\Sigma}(\mathfrak s\#\mathfrak s_0)
=
\pm SW_V(\mathfrak s).
\]
Since \(V\#\Sigma\cong M\) and \(SW_M\neq0\), one gets \(SW_V\neq0\). The corresponding basic class has square
\[
c^2=A-1>0.
\]

### Scalar curvature and Bach tensor

A smooth global \(P\)-minimizer is \(P\)-critical. The trace of its Euler equation gives
\[
\Delta s=0,
\]
so \(s\) is constant on connected \(V\).

- \(s>0\) would give a PSC metric and annihilate the nonzero Seiberg–Witten invariant.
- \(s=0\) contradicts the monopole estimate
  \[
  \int_Vs^2\ge32\pi^2c^2>0.
  \]

Therefore
\[
s_{g_0}<0.
\]

If \(g_0\) is also Bach-flat, use
\[
P=2\int|W|^2+\frac1{12}\int s^2-16\pi^2\chi.
\]
Since both \(P\) and \(\int|W|^2\) are stationary, \(\int s^2\) is stationary. At constant \(s\),
\[
\nabla\!\int s^2=-2s\,\operatorname{Ric}^{\circ}.
\]
Because \(s\neq0\), one obtains \(\operatorname{Ric}^{\circ}=0\). Hence the minimizer is Einstein; otherwise its Bach tensor is nonzero. This dichotomy is correct.

---

## 7. The analytic CH-cell upper estimate

Chapter 5 gives, for every fixed \(R>0\), a smooth ordinary blow-up cell that is exactly complex hyperbolic for \(t\ge R\) and satisfies
\[
\frac{P(g_\epsilon)}{8\pi^2}
=
1-9\epsilon^2\log(1/\epsilon)+O_R(\epsilon^2).
\]
Every fixed compact ball quotient has positive injectivity radius. Choose any
\[
0<R<\operatorname{inj}(X)
\]
small enough that the required radial cell and its matching collar lie in an embedded ball. The construction explicitly allows arbitrary fixed \(R>0\). For that fixed \(R\), choose \(\epsilon\) so small that
\[
9\log(1/\epsilon)
\]
dominates the constant hidden in \(O_R(1)\). Then the cell cost is strictly below \(8\pi^2\).

The exterior complex-hyperbolic metric is Einstein and contributes no \(P\)-energy. Exact matching gives a smooth metric on
\[
X\#\overline{\mathbb{CP}}^2.
\]
Therefore
\[
p_*(M)\le P(g_\epsilon)<8\pi^2.
\]

This works for every individual compact ball quotient. The admissible \(R\) and \(\epsilon\) may depend on \(X\); no uniform injectivity radius over all ball quotients is needed. The fixed numerical cell mentioned separately may not fit every quotient, but the arbitrary-collar analytic family does.

---

## 8. General \(k\)

For every fixed \(k\), one can choose \(k\) disjoint embedded complex-hyperbolic balls and insert \(k\) cells, giving
\[
p_*(M_k)<8\pi^2k.
\]

The displayed estimate
\[
\sum_i\bigl[4(e_i-1)+4b_1(\widehat N_i)+\beta(\widehat N_i)\bigr]<k
\]
is valid only after applying Lemma 54.3.

Indeed, before showing \(b^+(\widehat N_i)=0\), Lemma 54.1 supplies
\[
P(N_i)\ge8\pi^2
\max\{D_i+b_i^--5b_i^+,\,
      D_i+b_i^+-5b_i^-,\,0\},
\]
where
\[
D_i=4(e_i-1)+4b_1(\widehat N_i).
\]
This maximum is not generally equal to
\[
D_i+\max\{b_i^--5b_i^+,\ b_i^+-5b_i^-,0\}.
\]
For example \(D_i=4\) and \(b_i^+=b_i^-=1\) give zero in the first expression but \(4\) in the second.

For \(M_k\), however, the blow-up formula gives \(SW_{M_k}\neq0\), and \(b^+(M_k)=b^+(X)\ge3\). Lemmas 54.2–54.3 then yield
\[
b^+(\widehat N_i)=0.
\]
Consequently
\[
\beta(\widehat N_i)=b^-(\widehat N_i)=b_2(\widehat N_i),
\]
and
\[
P(N_i)\ge8\pi^2
\bigl[
4(e_i-1)+4b_1(\widehat N_i)+b_2(\widehat N_i)
\bigr].
\]
Summing proves
\[
\sum_i
\bigl[
4(e_i-1)+4b_1(\widehat N_i)+b_2(\widehat N_i)
\bigr]<k.
\]
In particular,
\[
\sum_i b_2(\widehat N_i)<k.
\]

If \(p_*(M_k)<32\pi^2\), every bubble must have \(e_i=1\), because \(e_i\ge2\) would contribute at least \(32\pi^2\) after \(b^+=0\). Thus the connectedness statement is correct with this order of argument.

---

## 9. Collapse and orbifold arithmetic

### Free circle action region

For a free orientation-preserving circle action
\[
S^1\longrightarrow C\stackrel{\pi}{\longrightarrow}B,
\]
the vertical tangent line is trivial and a connection splits
\[
TC\cong\pi^*TB\oplus\underline{\mathbb R}.
\]
Every orientable \(3\)-manifold is parallelizable, so \(TC\) is trivial and
\[
w_2(C)=0.
\]

If \(y\in H_2(C;\mathbb Z)\) maps to \(x\in H_2(M;\mathbb Z)\), Wu’s formula and naturality give
\[
x^2\equiv\langle w_2(M),x\rangle
=\langle w_2(C),y\rangle
=0\pmod2.
\]
Hence the class \(E\), with \(E^2=-1\), cannot be entirely carried by such a region. This argument does not extend automatically to locally free actions with finite isotropy.

### Orbifold root calculation

If the absorbed root has the form
\[
a+mE,\qquad a\in H_2(X),
\]
and square \(-2\), then
\[
a^2-m^2=-2,
\qquad\text{so}\qquad
a^2=m^2-2.
\]
If the local homology argument forces \(m\) odd, then \(a^2\) is odd. For \(m=1\),
\[
a^2=-1.
\]

The final sentence in Step 54 should not infer the existence of a square-\(-1\) class from odd \(m\) alone. For \(m=3,5,\ldots\), the required square is \(7,23,\ldots\). Thus:

- odd \(m\) implies that the intersection form of \(X\) represents an odd square;
- a square-\(-1\) class is required only when the orbifold mechanism separately forces \(m=1\).

The supplied Step 54 text does not rederive why absorption forces odd \(m\); that input belongs to the earlier local lattice calculation.

---

## 10. BCG, Bishop and the Einstein volume calculations

For an Einstein metric normalized by
\[
\operatorname{Ric}_g=-6g
\]
in dimension four, Bishop comparison gives
\[
h(g)\le3\sqrt2.
\]
The complex-hyperbolic metric in the same normalization has entropy
\[
h_{\mathrm{CH}}=4.
\]
The degree-one collapse map
\[
X\#\overline{\mathbb{CP}}^2\longrightarrow X
\]
and Besson–Courtois–Gallot give
\[
h(g)^4\operatorname{Vol}(g)
\ge4^4\operatorname{Vol}(X).
\]
Therefore
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
\ge
\left(\frac4{3\sqrt2}\right)^4
=
\frac{64}{81}.
\]
The JSON value is correct.

LeBrun’s scalar estimate gives
\[
\int s_g^2\ge32\pi^2A.
\]
Since \(s_g=-24\),
\[
576\operatorname{Vol}(g)\ge32\pi^2A.
\]
For the complex-hyperbolic metric on \(X\),
\[
576\operatorname{Vol}(X)=32\pi^2A.
\]
Hence
\[
\operatorname{Vol}(g)\ge\operatorname{Vol}(X),
\]
which is stronger than \(64/81\).

The topological upper estimates are also correct:
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
\le3-\frac1{c_2(X)}
\]
from \(T_+\), and
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
\le2+\frac2{c_2(X)}
\]
from \(\chi\).

### Sign correction in Remark 4

If an Einstein metric had the Kähler algebraic relation
\[
\int|W^+|^2=\frac1{24}\int s^2,
\]
then
\[
\frac{\operatorname{Vol}(g)}{\operatorname{Vol}(X)}
=
1-\frac1{3c_2(X)}.
\]
This contradicts the LeBrun estimate.

For a general Einstein metric on \(M\),
\[
\int|W^+|^2
=
2\pi^2(A-1)-\frac1{48}\int s^2.
\]
Therefore
\[
\int|W^+|^2-\frac1{24}\int s^2
=
2\pi^2(A-1)-\frac1{16}\int s^2
\le-2\pi^2.
\]
Thus the actual \(W^+\)-energy must lie strictly **below**, not above, the Kähler-type value \(\int s^2/24\). The direction in Remark 4 is reversed.

---

## 11. Koiso rigidity near a ball quotient

With \(\operatorname{Ric}=-6g\), the curvature action on trace-free symmetric tensors has eigenvalues
\[
-2\quad\text{on the \(J\)-invariant part},\qquad
4\quad\text{on the \(J\)-anti-invariant part}.
\]
The dimensions \(3\) and \(6\) are correct.

For a TT tensor \(h\), the Codazzi–Koiso identity gives
\[
\langle(\nabla^*\nabla-2\mathring R)h,h\rangle
=
\|d^\nabla h\|_2^2
+6\|h\|_2^2
-\langle\mathring Rh,h\rangle.
\]
Since the largest eigenvalue of \(\mathring R\) is \(4\),
\[
\langle(\nabla^*\nabla-2\mathring R)h,h\rangle
\ge2\|h\|_2^2.
\]
Thus the TT Einstein operator has no kernel, and the spectral gap \(2\) is independent of the lattice. Koiso’s gauge-fixed implicit-function theorem then gives local Einstein rigidity up to diffeomorphism and scale.

The individual \(C^{2,\alpha}\) and \(H^s\), \(s>4\), local rigidity statements are correct. Raw \(H^2\) smallness does not provide \(L^\infty\) control in dimension four.

The additional statement that the neighborhood size is uniform over all finite covers requires a uniformly-local Hölder inverse estimate for the gauge-fixed Einstein operator. Finite covers of a fixed quotient do have uniform local geometry and preserve the TT \(L^2\) gap, but the full \(C^{2,\alpha}\leftarrow C^{0,\alpha}\) inverse estimate is a separate analytic theorem. The referenced “Lemma M” is not among the supplied files, so this uniform strengthening is not independently established here.

---

## 12. Exact use of the five hypotheses

| Conclusion | Required inputs |
|---|---|
| \(p_*(M)<8\pi^2\) | Analytic CH-cell only; none of the five hypotheses |
| Every capped bubble is a connected summand | Case-(I) topology and \(\mathrm H_{\mathrm{sm}}\) |
| Every capped bubble admits PSC | \(\mathrm H_{\mathrm{dec}}\), including scalar-flatness and derivative-controlled AE decay |
| \(\sum P(N_k)<8\pi^2\) | Upper estimate and \(\mathrm H_{\mathrm{lsc}}\) |
| \(b^+(\widehat N_k)=0\) | Previous two rows, Lemma 54.3, and \(SW_M\neq0\) |
| \(e=1,\ b_1=b_2=0\) | Lemma 54.1 after \(b^+=0\) |
| Homotopy-sphere compactifications | Previous row, connected-sum topology and the \(\pi_1\)/Hopf argument |
| Parts (i)–(ii) | \(\mathrm H_{\mathrm{sm}},\mathrm H_{\mathrm{lsc}},\mathrm H_{\mathrm{dec}}\) |
| Smooth bulk metric and \(P(g_0)=p_*(V)\) | Add \(\mathrm H_{\mathrm{eq}},\mathrm H_{\mathrm{rem}}\), together with reassembly |
| \(s_{g_0}<0\) and Einstein/Bach alternative | Smooth attained bulk minimizer plus the Seiberg–Witten gluing argument |
| No nontrivial bubbles when every cap is standard \(S^4\) | All assumptions used in part (iii), plus Bishop–Gromov rigidity |

---

## 13. Rescaled perturbation coefficient and bubble-scale criticality

The rescaling formula is correct. If
\[
\widehat g=\ell^{-2}g,
\]
then
\[
\varepsilon\int(1+|\operatorname{Ric}_g|^2)^p\,dV_g
=
\varepsilon\ell^{4-4p}
\int(\ell^4+|\operatorname{Ric}_{\widehat g}|^2)^p\,dV_{\widehat g}.
\]
Thus the effective coefficient is
\[
\kappa_\varepsilon=\varepsilon\ell^{4-4p}.
\]

The \(L^{2p}\) energy estimate yields only
\[
\kappa_\varepsilon\le C.
\]
Indeed, if the curvature radius is normalized by
\[
\ell^{4p-4}\int_{B_\ell}|\operatorname{Ric}|^{2p}\ge c,
\]
while
\[
\int|\operatorname{Ric}|^{2p}\le C/\varepsilon,
\]
then
\[
\varepsilon\ell^{4-4p}\le C/c.
\]
The Step 54 paragraph correctly observes that this does not imply \(\kappa_\varepsilon\to0\).

Choosing \(p=p(\varepsilon)\downarrow1\) does not improve this estimate by itself, because the smallest curvature scale also depends on \(p\). Moreover, letting the supercritical margin \(p-1\) tend rapidly to zero weakens the uniform Morrey and elliptic estimates used to produce smooth bubbles.

There are two better mechanisms.

### A. Compact replacement on the bubble

The original closed metrics satisfy
\[
P(g_i)\longrightarrow p_*(M).
\]
If a smooth bubble \(N\) admitted a compactly supported variation lowering \(P\) by a fixed amount \(\delta>0\), transplant that variation into \(g_i\) at the bubble scale. Smooth convergence on the chosen compact subset gives
\[
P(\widetilde g_i)
=
P(g_i)-\delta+o(1),
\]
which is below \(p_*(M)\) for large \(i\). Therefore every smooth bubble is locally minimizing for \(P\) under compactly supported variations, hence \(P\)-critical.

This argument does not use \(\kappa_\varepsilon\to0\), \(\mathrm H_{\mathrm{eq}}\), or the no-neck identity. It uses:

- \(P(g_i)\to p_*(M)\);
- smooth convergence on compact bubble subsets;
- the ability to transplant a compactly supported metric variation.

The trace equation then gives \(\Delta s=0\). Since an AE scalar function arising from the curvature tends to zero at infinity, the maximum principle gives \(s=0\). Thus bubble-scale \(P\)-criticality and scalar-flatness can be obtained directly once smooth bubble convergence is available.

### B. Letting \(p_i\to1\) with bounded \(\kappa_i\)

Formally, if \(p_i\to1\) and \(\kappa_i\to\kappa<\infty\), the rescaled perturbation tends to
\[
\kappa\int|\operatorname{Ric}|^2.
\]
At a scalar-flat limit,
\[
\nabla\!\int|\operatorname{Ric}|^2
=
\nabla P,
\]
because the first variation of \(\int s^2\) vanishes at \(s=0\). The limiting equation would therefore be
\[
(1+\kappa)\nabla P=0.
\]
This also yields \(P\)-criticality without requiring \(\kappa=0\). Making this passage rigorous requires uniform convergence of the weighted Euler operators as \(p_i\to1\), especially near the zero set of \(\operatorname{Ric}\), together with compactness estimates uniform in \(p_i\).

The compact-replacement argument is cleaner and avoids those weighted-operator issues. The remaining analytic work is then improved AE decay with derivative control, not vanishing of \(\varepsilon\ell^{4-4p}\).