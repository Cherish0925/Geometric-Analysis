# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 93,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step93_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step93_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify A01 Step-74 Theorems 74.B–D and assess the equality/attainment question for V_m. Check the mixed inequality transfer including bubble chirality and charge conventions, the Einstein-bulk optimization and asymptotic linear form, the Kähler Ricci-flat filler budget, and the screening interpretation. Then determine what, if anything, follows rigorously from W^-=0, constant s<0, |W^+|^2=s^2/24, P=8pi^2 k for an alpha_orb minimizer: does existing Derdzinski/LeBrun equality theory force a Kähler or almost-Kähler orbifold structure, and is such a structure topologically excluded on V_m? Distinguish a theorem from a plausible route and identify any exact source theorem needed.

## Integrated Scientific Memo

# Scientific verification memo: Step 74.B–D and attainment on \(V_m\)

**Main conclusion.** The curvature transfer, Einstein-bulk optimization, and Kähler Ricci-flat budget are correct under their stated supply, topology, and ALE-gluing hypotheses. Several screening summaries need correction. More importantly, a direct first-variation argument closes most of the attainment question:
\[
P_{*,\mathrm{orb}}(V_m)=8\pi^2k
\quad\text{is never attained},
\]
and
\[
\alpha_{\mathrm{orb}}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\}
\quad\text{is not attained if }k\ne A/3.
\]
At \(k=A/3\), attainment remains precisely a constant-negative-scalar, half-conformally-flat orbifold existence problem. Derdziński or LeBrun equality theory is not needed for these nonattainment results.

Throughout, \(k=2m>0\), and conclusions involving the transferred mixed estimate retain **(SW)**, including any required \(b^+=1\) chamber input. The smooth resolution identification and exceptional root-span statement retain **(R)** and the topology recorded in the theorem package.

## 1. Transfer and charge conventions

The source conventions imply
\[
8\pi^2T_\pm=4I_\pm+\frac S{12}-P,
\qquad T_\pm=2\chi_{\mathrm{orb}}\pm3\tau_{\mathrm{orb}}.
\]
For an ALE filler oriented by the resolved manifold,
\[
P(N)=4I_\pm(N)+\frac{S(N)}{12}+8\pi^2c_\pm(N),
\]
where
\[
c_\pm=\frac2{|\Gamma|}-2\chi(N)\mp3\tau(N)\mp3\eta_\Gamma.
\]
These agree with the supplied Burns, Eguchi–Hanson, and ADE checks.

For scalar-flat fillers, expand the smooth mixed functional:
\[
Q(g):=\int(s-\sqrt6|W^+|)^2
=S-2\sqrt6\int s|W^+|+6I_+.
\]
Under derivative-controlled ALE decay and the cutoff construction of 86.S/86.S′:

* the scalar terms on the fillers vanish;
* their self-dual Weyl contribution tends to \(6B_+\);
* annular scalar, Weyl, and cross-term integrals vanish.

Indeed, with decay order \(\tau>0\) and
\[
\rho=\varepsilon^{\tau/(\tau+2)},
\]
the annular curvature is bounded and the annular volume is \(O(\rho^4)\). Applying the smooth inequality separately to each resolved metric therefore yields
\[
\boxed{Q(g_V)+6B_+\ge72\pi^2A.}
\]
No convergence of monopole classes is needed **for this numerical transfer**.

For Ricci-flat fillers,
\[
I_\pm(N)=-2\pi^2c_\pm(N),\qquad c_\pm(N)\le0,
\]
so
\[
\boxed{Q(g_V)\ge72\pi^2A+12\pi^2C_+.}
\]
For scalar-flat non-Ricci-flat fillers,
\[
B_+=\sum_j\left(\frac{P(N_j)}4-2\pi^2c_+(N_j)\right).
\]

**Chirality is essential.** A Ricci-flat Kähler filler in its complex orientation has \(W^+=0\), hence
\[
c_+=0,\qquad c_-=-4\left(\chi(N)-\frac1{|\Gamma|}\right).
\]
Reversing orientation interchanges \(c_+\) and \(c_-\); its \(W^+\)-energy is then generally nonzero. Thus “Ricci-flat” does not mean “lossless mixed transfer.”

There is one notation correction in Step 74: for a Wahl ball of type \(1/n^2(1,na-1)\),
\[
(c_+,c_-)=\left(0,-4(1-n^{-2})\right).
\]
The expression \(-4(1-1/n)\) is correct only if \(n\) denotes the **end-group order**, not the Wahl parameter.

## 2. Einstein-bulk optimization and asymptotics

For an Einstein bulk, put \(x=S/(96\pi^2)\). Chern–Weil gives
\[
I_\pm=2\pi^2(T_\pm-x).
\]
Scalar transfer and Weyl positivity give
\[
\boxed{\frac A3\le x\le\min(T_+,T_-).}
\]
The negative-Yamabe argument in 86.S also applies: a nonnegative-Einstein bulk resolved by Ricci-flat fillers would produce smooth metrics with \(\|s^-\|_2\to0\), contradicting the supplied negative Yamabe bound. Thus any such Einstein bulk has \(\lambda<0\).

The mixed estimate, followed by Cauchy–Schwarz, gives
\[
72\pi^2A+12\pi^2C_+
\le Q(g_V)
\le(\sqrt S+\sqrt{6I_+})^2,
\]
hence
\[
\boxed{
F_{T_+}(x):=
\left(\sqrt{8x}+\sqrt{T_+-x}\right)^2
\ge6A+C_+.
}
\]
Here
\[
F_T(x)=T+7x+4\sqrt{2x(T-x)}
\]
is concave, with maximum \(9T\) at \(x=8T/9\). Clipping that point to the admissible interval, exactly as the script does, is the correct optimization.

### Asymptotic expansion

Write
\[
T_+=A+e,\quad e=C_+-k,
\qquad
T_-=\frac A3+d,\quad d=C_-+5k.
\]
For fixed \(k,C_\pm\) and sufficiently large \(A\), the endpoint \(x=T_-\) binds. Expansion gives
\[
F_{T_+}(T_-)-(6A+C_+)
=
9C_-+2C_++42k
-\frac{3(e-3d)^2}{4A}+O(A^{-2}).
\]
Thus (3.2) is correct. It is a fixed-charge expansion, not a uniform expansion when charges grow proportionally to \(A\).

There is also a useful **exact strengthening of its interpretation**. Homogeneity and concavity give the tangent inequality
\[
F_T(x)\le3T+9x,
\]
with equality precisely when \(x=T/3\). Consequently every admissible Einstein bulk necessarily satisfies
\[
\boxed{9C_-+2C_++42k\ge0}
\]
at every finite \(A\), not merely asymptotically. If this linear expression is zero, feasibility additionally requires
\[
e=3d,\qquad x=T_-=T_+/3.
\]
This proves the finite-\(A\) exclusion of the marginal \(A_5,k=5\) row without relying on numerical sampling: there \(e=-5\), \(d=5/3\), so equality is impossible.

## 3. Exact Kähler Ricci-flat filler budget

For \(C_+=0\), \(T_+=A-k\). The mixed test first requires
\[
9(A-k)\ge6A,\qquad\text{equivalently }k\le A/3.
\]
Its smaller root is
\[
x_{\min}=\frac A{27}
\left(4-\sqrt{1-\frac{3k}{A}}\right)^2.
\]
Since \(x_{\min}\ge A/3\) and lies in \([0,T_+]\), existence of an admissible \(x\) is equivalent to
\[
T_-\ge x_{\min}.
\]
For \(k>0\),
\[
x_{\min}-\frac{A+k}{3}
=\frac{4A}{27}
\left(1-\sqrt{1-\frac{3k}{A}}\right)^2>0.
\]
In particular, \(C_->-14k/3\).

Put
\[
Q_{\mathrm{fill}}=\sum_j\left(\chi(N_j)-\frac1{|\Gamma_j|}\right),
\qquad C_-=-4Q_{\mathrm{fill}}.
\]
Then Corollary 74.D is exactly
\[
\boxed{
Q_{\mathrm{fill}}\le
\frac14\left(\frac A3+5k-x_{\min}\right).
}
\]
The sharper expansion is
\[
Q_{\mathrm{fill}}\le
\frac{7k}{6}-\frac{k^2}{12A}
-\frac{k^3}{8A^2}+O(k^4/A^3).
\]
The quoted JSON values agree with this formula.

For the fillers under discussion, \(\chi=1+r\), \(r=b_2\), so each contributes \(r+1-|\Gamma|^{-1}\). If \(\sum r_j=k\), the exact budget implies
\[
\sum_j(1-|\Gamma_j|^{-1})<k/6.
\]
For a single filler carrying rank \(k=r\), therefore,
\[
\boxed{r>6(1-|\Gamma|^{-1})}
\]
is necessary at finite \(A\). Calling this a “sufficient-rank-per-filler condition” is potentially misleading: it is a **necessary rank threshold for surviving this numerical test**, not a sufficient condition for an embedding or an Einstein bulk.

## 4. What the screening does—and does not—establish

The script implements the intended necessary test correctly. Its interpretation needs the following repairs.

### Numerical summaries

* The eight large-\(A\) cyclic rank-one survivors and their charge pairs agree with the supplied JSON.
* “From \(A\ge90\)” in a sparsely sampled table means **first passing sampled value**, not exact threshold among multiples of nine. For example, the single Kronheimer \(D_6\), \(k=6\), already passes at \(A=63\), but fails at \(54\).
* The claim that every rank-plus-one row passes from \(A=9\)–\(18\) contradicts the JSON. For example, \(A_{10}\), \(k=11\), first passes in the supplied sample at \(A=36\).
* All 98 Ricci-flat-charge-compatible rational-ball rows survive **eventually**, not at every sampled \(A\). The row \(L(4,3)\), \((c_+,c_-)=(-3,0)\), fails at \(A=9\) and passes at \(18\).
* Reversed-orientation Wahl metrics are actual Ricci-flat fillers, not merely hypothetical charge rows. They cease to be Kähler in the ambient orientation but still exist as Ricci-flat metrics.

“Charge-compatible” means only \(I_\pm=-2\pi^2c_\pm\ge0\). Passing the screen establishes only an admissible integrated scalar/Weyl budget. Actual filler existence, oriented embedding, identification of the smooth resolution, and Einstein-bulk existence remain separate questions.

### Additional topology beyond the screen

For a simply connected Kronheimer region embedded in \(M_k\), the classifying map to the aspherical \(X\) is null on that region. Its root lattice must therefore embed in the exceptional lattice \(-I_k\). This is stronger than charge arithmetic.

The standard root-subsystem classification of \(D_k\) would remove \(E_6,E_7,E_8\) embeddings into any \(\mathbb Z^k\), and remove full-rank \(A_n\subset\mathbb Z^n\) for \(n\ge4\). Thus many numerical “survivors” are not topologically viable. This refinement needs the precise lattice-classification input if used as a theorem; it is not established by the screening script itself. Likewise, eliminating hypothetical Ricci-flat rank-one ADE-end fillers by a hyperkähler criterion requires the exact criterion and its spin, group, and decay hypotheses—not just its informal name.

## 5. A direct nonattainment theorem on \(V_m\)

This is the decisive advancement.

For every orbifold metric on \(V_m\), the supplied identities give
\[
\boxed{
P=8\pi^2k+\frac{S-32\pi^2A}{12}+4I_-.
}
\]
Thus a metric attaining \(P=8\pi^2k\) would satisfy
\[
S=32\pi^2A>0,\qquad W^-=0.
\]

On a fixed compact four-orbifold,
\[
P=\frac S{12}+2\mathcal W-16\pi^2\chi_{\mathrm{orb}},
\qquad
\mathcal W=12\pi^2\tau_{\mathrm{orb}}+2I_-.
\]
At \(W^-=0\), the first variation of \(I_-\), hence of \(\mathcal W\), vanishes. Therefore a \(P\)-minimizer would be critical for \(S=\int s^2\).

The scalar-square Euler equation, after division by two, is
\[
\nabla^2s-(\Delta s)g-s\,\operatorname{Ric}
+\frac14s^2g=0.
\]
Its trace gives \(\Delta s=0\). Compact orbifold integration implies \(s\) is constant, and the remaining equation is
\[
s\,\operatorname{Ric}^\circ=0.
\]
Since \(S>0\), \(s\ne0\), so \(P=0\), contradicting \(P=8\pi^2k>0\).

All variations may initially be supported in the regular locus; the equation extends across isolated points because the metric is smooth in orbifold charts. No special equality-rigidity theorem is involved.

Hence
\[
\boxed{P_{*,\mathrm{orb}}(V_m)=8\pi^2k\text{ is never attained}.}
\]
The same Euler argument shows that the scalar-square infimum \(32\pi^2A\), approached by the Green-cap family, is not attained either.

### Consequences for \(\alpha_{\mathrm{orb}}\)

* **\(k<A/3\).** Equality in the weighted-mean argument forces \(S=32\pi^2A\), \(I_-=0\), and \(L_s=0\), hence \(P=8\pi^2k\). It is impossible.
* **\(k>A/3\).** The strict pointwise inequality \(4P/R>1\) already excludes attainment of \(\alpha_{\mathrm{orb}}=1\).
* **\(k=A/3\).** The exact identity becomes
  \[
  \boxed{\mathscr D-1=\frac{12I_-+L_s}{R}.}
  \]
  Thus attainment is equivalent to existence of an orbifold metric with
  \[
  W^-=0,\qquad s\equiv\text{constant}<0.
  \]
  The sign follows from the negative-scalar transfer. Any such attainer necessarily has
  \[
  S>32\pi^2A,\qquad P>8\pi^2k.
  \]
  It is an \(\mathscr D\)-minimizer, not a \(P\)-minimizer, so the preceding Euler argument does not exclude it.

This wall exists only when \(m=A/6\) is integral. An equivalence with existence of a half-conformally-flat **conformal class** additionally uses the compact negative orbifold Yamabe theorem. A deformation/gluing approach would need an appropriate orbifold self-dual connected-sum theorem and control of the obstruction space of the ball quotient’s self-dual deformation complex; neither is supplied here.

## 6. Equality theory: what is rigorous, what is missing

The equations
\[
W^-=0,\quad s<0\text{ constant},\quad
|W^+|^2=s^2/24,\quad P=8\pi^2k
\]
cannot describe an \(\alpha_{\mathrm{orb}}\)-minimizer: below the wall they force the impossible \(P\)-minimum; at the wall the same \(P\)-minimum is impossible; above the wall there is no attainer at all.

Independently of that contradiction, these equations do **not** supply the hypotheses of the usual Derdziński theorem:

* the norm of a trace-free symmetric operator on \(\Lambda^+\) does not determine its eigenvalue multiplicities;
* \(W^-=0\) gives Bach-flatness, not \(\delta W^+=0\);
* constant scalar curvature does not eliminate the Cotton source arising from \(\nabla\operatorname{Ric}^\circ\).

The relevant exact source is Derdziński’s harmonic-\(W^+\), two-eigenvalue conformally Kähler theorem in *Self-dual Kähler manifolds and Einstein manifolds of dimension four*, Compositio Math. 49 (1983). Its differential and spectral hypotheses must actually be established. Local conformal Kählerness would also need the usual global eigenline/descent qualification.

LeBrun equality rigidity likewise does not transfer merely because the **number** \(Q(g_V)\) transfers. The supplied material does not contain the full equality clause of the cited Proposition 3.8. A limiting proof would need:

1. the exact smooth equality statement and its hypotheses;
2. compactness of the relevant monopole solutions on the regular locus;
3. a nonzero limiting self-dual form;
4. orbifold removability and extension across the \(A_1\) points.

Thus “equality forces an orbifold almost-Kähler structure” remains an additional theorem to prove, not a consequence of 74.B.

## 7. Topological exclusion of compatible structures

The supplied root-span topology gives a stronger obstruction than merely non-Kählerness.

Suppose \(V_m\) carried an orbifold almost-complex structure inducing the orientation of \(X\). Near an \(A_1\) point, the local group is \(-I\), which commutes with every complex structure. Radial contraction in the local chart homotopes the structure to its constant value near the point. It can then be extended over the complex Eguchi–Hanson resolution, whose first Chern class evaluates to zero on the core \((-2)\)-sphere.

Resolving all points gives an almost-complex structure on \(M_k\) with
\[
c_1\cdot C_j=0
\]
for every resolution sphere. By the supplied paired-\(A_1\) topology, all odd-square exceptional classes lie in their rational span. Therefore
\[
c_1\cdot E_i=0.
\]
But \(c_1\) is characteristic:
\[
c_1\cdot E_i\equiv E_i^2\equiv1\pmod2,
\]
a contradiction.

Consequently, under the stated resolution/root-span identification,
\[
\boxed{V_m\text{ has no compatible orbifold almost-complex structure}.}
\]
In particular it has no compatible Kähler or almost-Kähler orbifold structure. This does not prohibit a half-conformally-flat constant-scalar metric at the wall: such a metric need not supply any global almost-complex structure.

**Remaining scientific object.** The only unresolved attainment case is therefore the existence of a smooth orbifold metric on \(V_{A/6}\) satisfying \(W^-=0\) and constant \(s<0\), necessarily non-almost-Kähler and strictly above the \(P\)- and scalar-square infima. The transferred inequalities do not decide that existence problem.