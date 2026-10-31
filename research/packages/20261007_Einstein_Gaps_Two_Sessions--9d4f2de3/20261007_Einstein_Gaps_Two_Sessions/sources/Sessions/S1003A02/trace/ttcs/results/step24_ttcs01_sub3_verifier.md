# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Skills/geometric-analysis/references/conventions-and-literature.md",
    "Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md"
  ]
}
```

## Task

Independently verify Theorems C and H in the Step-23 note against the conventions and cited LeBrun source. Check all normalizations, conformal identities, decay/boundary requirements, the conditional sharp P and Einstein-defect values, the range 1<=k<=2 chi(Y), the Burns upper sequence, and non-attainment. Identify any false statement or missing hypothesis and give exact corrected formulations. Also assess whether Theorem C's relative RV definition is invariant under moving the compact cutoff and what is actually known about existence of u on H4 versus CH cells.

## Output

# Scientific verification memo

## 1. Normalizations and the closed conformal identity

The curvature normalization is internally consistent. From
\[
8\pi^2(2\chi+3\tau)
 =4\int |W^+|^2-P+\frac{S}{12},
\]
one has
\[
P=4\int |W^+|^2+\frac{S}{12}-8\pi^2(2\chi+3\tau).
\]

For the real-hyperbolic normalization \(K=-2\),
\[
\operatorname{Ric}=-6g,\qquad s=-24,\qquad W=0.
\]
Gauss–Bonnet gives
\[
8\pi^2\chi(Y)=\frac1{24}\int_Y s^2\,d\mu
            =24\,\operatorname{Vol}(Y),
\]
hence
\[
\operatorname{Vol}(Y)=\frac{\pi^2}{3}\chi(Y),\qquad
Y_{\rm hyp}=-24\sqrt{\operatorname{Vol}(Y)},\qquad
Y_{\rm hyp}^2=192\pi^2\chi(Y).
\]
Thus \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\), exactly as used in Step 23.

With \(\Delta=\operatorname{div}\nabla\), the scalar conformal law for \(\hat g=u^2g\) is
\[
\hat s\,u^3=-6\Delta u+su.
\]
For \(\hat s=-24\), this becomes
\[
6\Delta u=su+24u^3.
\]
The algebra in (1.2)–(1.3) is correct. On a closed manifold it yields
\[
S(g)-S(\hat g)
 =36\int\left(\frac{\Delta u}{u}\right)^2d\mu_g
 +288\int|\nabla u|^2d\mu_g.
\]
Since \(S(\hat g)=576\operatorname{Vol}(\hat g)=Y[g]^2\),
\[
S(g)=Y[g]^2
 +36\int\left(\frac{\Delta u}{u}\right)^2
 +288\int|\nabla u|^2.
\]
Conformal invariance of \(|W^+|^2d\mu\) then gives
\[
P(g)-P(\hat g)
 =3\int\left(\frac{\Delta u}{u}\right)^2
 +24\int|\nabla u|^2.
\]

This is exactly LeBrun’s displayed computation in Lemma 1 of §5 of the supplied 1996 paper, after converting his Laplacian convention and setting \(\hat s=-24\). The relevant Yamabe-maximizer-implies-Einstein passage is also in §5, not §2.

---

## 2. Theorem C

### 2.1 Precise relative definitions

Let \(g_0\) be the real- or complex-hyperbolic model, and fix an orientation-preserving end identification
\[
(U\setminus K,g)\cong (M_0\setminus B_{R_0},g_0).
\]
For matched truncations \(U_R\) and \(B_R\), the natural quantities are
\[
\Delta W_+
 :=\lim_{R\to\infty}\left[
 \int_{U_R}|W_g^+|^2d\mu_g-\int_{B_R}|W_{g_0}^+|^2d\mu_{g_0}
 \right],
\]
and
\[
\operatorname{RV}_{g_0}(\hat g)
 :=\lim_{R\to\infty}
 \left[\operatorname{Vol}_{\hat g}(U_R)
       -\operatorname{Vol}_{g_0}(B_R)\right].
\]
Because \(g=g_0\) on the end and \(d\mu_{\hat g}=u^4d\mu_g\),
\[
\operatorname{RV}_{g_0}(\hat g)
 =
 \bigl[\operatorname{Vol}_{g}(U_{\rm int})
       -\operatorname{Vol}_{g_0}(B)\bigr]
 +\int_U(u^4-1)\,d\mu_g.
\]

The integral in the Step-23 definition must therefore be over all of \(U\). If it were intended only over \(U_{\rm int}\), the expression would change when the cut is moved through the model end.

With the integral over all \(U\), the expression is invariant under moving the cut through the fixed exact end: the added \(g\)-volume equals the added model volume, while the integral over \(U\) is unchanged. This invariance is relative to the fixed end marking. An unrelated change of defining function or end identification is a different renormalization convention.

### 2.2 Flux computation

On \(U_R\), integration by parts gives
\[
\int_{U_R}
 \bigl(\sigma u^2+24u^4-24u^2\bigr)
 =
 -6\int_{U_R}|\nabla u|^2
 +6\int_{\Sigma_R}u\,\partial_\nu u.
\]
Consequently, the finite-\(R\) version of (1.3) contains
\[
-24\int_{\Sigma_R}u\,\partial_\nu u
\]
in addition to the two bulk square terms. Thus (1.5) is valid once this flux tends to zero.

On the exact ends, the linearized equation is
\[
\Delta w=8w,\qquad w=u-1.
\]
The decaying indicial exponents are:

- real hyperbolic \(K=-2\):
  \[
  \alpha_{\rm H}=4\sqrt2,\qquad
  \operatorname{Area}(\Sigma_t)\asymp e^{3\sqrt2t};
  \]
- complex hyperbolic, holomorphic curvature \(-4\):
  \[
  \alpha_{\rm CH}=2+2\sqrt3,\qquad
  \operatorname{Area}(\Sigma_t)\asymp e^{4t}.
  \]

In both cases \(\alpha\) exceeds the area-growth exponent. Hence
\[
\int_{\Sigma_t}u\,\partial_\nu u\to0,\qquad
u^4-1\in L^1,
\]
and all terms in the relative identity converge. Standard elliptic asymptotics also give the derivative decay needed for the Chern–Simons transgression at infinity to vanish. Writing \(O(e^{-\alpha t})\), rather than \(w\sim e^{-\alpha t}\), allows the leading coefficient to vanish.

### 2.3 Relative Chern–Weil constant

For
\[
U_R\cong D^4\#\overline{\mathbb{CP}}^{\,2},
\]
relative to a ball,
\[
\Delta\chi=1,\qquad \Delta\tau=-1,\qquad
\Delta(2\chi+3\tau)=-1.
\]
The outer geometric transgression and eta contributions cancel for \(g\), since the two collars agree exactly. Therefore
\[
P_{\rm cell}(g)-8\pi^2
 =4\Delta W_+
  +\left[
    \int_{U_R}\frac{s_g^2}{12}\,d\mu_g
    -48\operatorname{Vol}_{g_0}(B_R)
   \right].
\]
Taking \(R\to\infty\) and inserting the conformal identity gives
\[
\boxed{
P_{\rm cell}(g)-8\pi^2
 =4\Delta W_+
 +48\,\operatorname{RV}_{g_0}(\hat g)
 +3\int_U\left(\frac{\Delta u}{u}\right)^2d\mu_g
 +24\int_U|\nabla u|^2d\mu_g .
}
\]
Since the Weyl density is conformally invariant,
\[
\boxed{
P_{\rm cell}(\hat g)-8\pi^2
 =4\Delta W_+
 +48\,\operatorname{RV}_{g_0}(\hat g).
}
\]

Thus Theorem C is correct with the following assumptions made explicit:

1. \(U\) has one marked exact model end and topology \(D^4\#\overline{\mathbb{CP}}^{\,2}\);
2. the end identification preserves the chosen orientation;
3. \(u>0\) solves the Yamabe equation and tends to \(1\) with sufficient derivative decay;
4. the integral in the displayed definition of \(\operatorname{RV}\) is over all of \(U\);
5. \(P_{\rm cell}(\hat g)\), \(\Delta W_+\), and the scalar term are interpreted through matched relative truncations.

For the real-hyperbolic model, \(W_{g_0}^+=0\), so
\[
\Delta W_+=\int_U|W_g^+|^2\ge0.
\]
Hence \(\operatorname{RV}(\hat g)\ge0\) is sufficient for \(P_{\rm cell}(g)\ge8\pi^2\). It is not necessary: the exact equivalent statement is
\[
4\Delta W_++48\operatorname{RV}(\hat g)\ge0
\]
for all constant-scalar representatives under consideration.

### 2.4 Existence of the conformal factor

**Real-hyperbolic end.**  
An exact real-hyperbolic end has a smooth conformal compactification. The singular Yamabe theorem supplies a complete conformal metric with scalar curvature \(-24\). Comparing its leading end coefficient with the already normalized hyperbolic model gives \(u\to1\). The maximum principle gives uniqueness. Thus existence for arbitrary smooth compact perturbations with an exact \(H^4\) end is supported by the Loewner–Nirenberg/Aviles–McOwen singular Yamabe theory.

**Complex-hyperbolic end.**  
The ordinary conformally compact singular Yamabe theorem does not transfer directly to the ACH geometry. The supplied Step-21 argument proves existence when
\[
s_g<0\quad\text{everywhere}.
\]
Since the compact perturbation is smooth and the exterior has \(s=-24\), this is equivalent to \(s_g\le-c<0\) for some \(c\). Constants
\[
u_-=\sqrt{c/24},\qquad
u_+=\sqrt{\max(-s_g)/24}
\]
give sub- and supersolutions, and exhaustion plus elliptic compactness gives a positive solution. The ratio maximum principle gives uniqueness.

For CH cells where \(s_g\) is zero or above zero somewhere, the supplied material contains no general existence theorem. The spectral identity
\[
6\lambda_0(\mathbb{CH}^2)+s_{\rm CH}=6\cdot4-24=0
\]
shows why the direct conformal-Laplacian coercivity argument is unavailable; it does not show that solutions are absent. Small compact perturbations are covered by an implicit-function argument because the linearization at \(u=1\) is
\[
-6\Delta+48.
\]
Newton convergence for the listed diagonal cells is numerical evidence, not an exact PDE existence proof unless accompanied by a posteriori interval enclosures.

Accordingly, Theorem C itself is valid as a conditional identity for every cell possessing such a solution. Universal existence is established for exact \(H^4\) ends and for the CH subclass with \(s_g<0\), plus sufficiently small perturbations of CH.

---

## 3. Theorem H

Let
\[
X_k=Y\#k\overline{\mathbb{CP}}^{\,2}.
\]
Then
\[
\chi(X_k)=\chi(Y)+k,\qquad
\tau(X_k)=-k,
\]
so
\[
2\chi(X_k)+3\tau(X_k)=2\chi(Y)-k.
\]
Chern–Weil therefore gives, for every metric,
\[
\boxed{
P(g)=8\pi^2k+4\int|W^+|^2
+\frac{S(g)-Y_{\rm hyp}^2}{12}.
}
\]
Under
\[
\mathcal Y(X_k)=Y_{\rm hyp}<0,
\]
every conformal class has \(Y[g]\le Y_{\rm hyp}<0\), and hence
\[
Y[g]^2\ge Y_{\rm hyp}^2.
\]
Combining the closed conformal identity with the preceding formula gives
\[
\boxed{
P(g)=8\pi^2k+4\int|W^+|^2
+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}
+3\int\left(\frac{\Delta u}{u}\right)^2
+24\int|\nabla u|^2 .
}
\]

### 3.1 Sharp \(P\)-value and strict pointwise inequality

Every term after \(8\pi^2k\) is at least zero, so
\[
P(g)\ge8\pi^2k.
\]
If equality held, then
\[
W^+=0,\qquad Y[g]=Y_{\rm hyp},\qquad \nabla u=0.
\]
Thus \(g\), up to constant rescaling, is a Yamabe metric whose conformal class realizes the Yamabe invariant. The standard variational theorem quoted by LeBrun in §5 makes such a metric Einstein. Equivalently, as a global minimizer of \(\int s^2\), its constant-scalar Euler equation is
\[
-2s\,\operatorname{Ric}+\frac12s^2g=0,
\]
hence \(\operatorname{Ric}=\frac{s}{4}g\). This gives \(P=0\), incompatible with \(P=8\pi^2k\) for \(k\ge1\). Therefore
\[
P(g)>8\pi^2k
\]
for every individual metric.

The Burns construction gives the matching upper sequence. Since
\[
\mathbf R^+=W^++\frac{s}{12}I=-2I
\]
on \(Y\), Theorem F at \(k\) disjoint points yields
\[
P(g_{x_0})
 =8\pi^2k(1+2x_0)+O(kx_0^{6/5}),
\]
and consequently
\[
\inf_{X_k}P=8\pi^2k.
\]
This infimum is not attained.

### 3.2 Einstein-defect value and the range \(1\le k\le2\chi(Y)\)

Put \(t=P/S\). Then
\[
\mathcal J=\frac{4P}{P+S/4}
          =\frac{16t}{4t+1},
\]
which is strictly increasing in \(t\). From the exact Chern–Weil formula,
\[
t\ge\frac1{12}
-\frac{8\pi^2(2\chi(Y)-k)}{S}.
\]
Under the Yamabe assumption,
\[
S\ge Y[g]^2\ge Y_{\rm hyp}^2
 =192\pi^2\chi(Y).
\]
When \(k\le2\chi(Y)\), the right-hand side increases with \(S\), giving
\[
t\ge\frac{k}{24\chi(Y)}.
\]
Therefore
\[
\mathcal E\ge\mathcal J
\ge\frac{4k}{k+6\chi(Y)}.
\]

The Burns metrics satisfy
\[
S(g_{x_0})\to Y_{\rm hyp}^2,\qquad
\operatorname{Vol}(g_{x_0})\to\operatorname{Vol}(Y).
\]
A clean justification for scalar variance is supplied by the fixed-\(\lambda=-6\) version of Theorem F:
\[
\int|\operatorname{Ric}+6g|^2
 =P+\frac14\int(s+24)^2.
\]
The fixed-\(\lambda\) defect and \(P\) have the same first-order expansion, so
\[
\int(s+24)^2\to0,
\qquad
\int(s-\bar s)^2\to0.
\]
Hence
\[
\mathcal E(g_{x_0})-\mathcal J(g_{x_0})\to0,
\]
and
\[
\boxed{
\inf\mathcal E=\inf\mathcal J
=\frac{4k}{k+6\chi(Y)},
\qquad 1\le k\le2\chi(Y).
}
\]

The upper construction is therefore valid. The note’s phrase that scalar curvature differs from \(-24\) only on cores of volume \(O(x_0^2)\) is too literal: there are also intermediate and cutoff annuli. The estimates in Theorem F still give the required \(L^2\)-decay.

The endpoint \(k=2\chi(Y)\) needs a correction concerning attainment.

- If \(1\le k<2\chi(Y)\), equality in the lower estimate forces
  \[
  S=Y_{\rm hyp}^2,\qquad W^+=0,
  \]
  and the LeBrun identity then forces the metric to be a Yamabe-invariant maximizer. The Einstein contradiction applies. Thus neither \(\mathcal J\) nor \(\mathcal E\) attains its infimum.

- If \(k=2\chi(Y)\), the strict dependence on \(S\) disappears:
  \[
  P=\frac{S}{12}+4\int|W^+|^2.
  \]
  Consequently
  \[
  \mathcal J=1
  \quad\Longleftrightarrow\quad
  W^+\equiv0,
  \]
  while
  \[
  \mathcal E=1
  \quad\Longleftrightarrow\quad
  W^+\equiv0
  \ \text{and}\ 
  s\ \text{is constant}.
  \]
  Such a metric may have \(S>Y_{\rm hyp}^2\), so it need not realize the Yamabe invariant and need not be Einstein. The Step-23 argument does not establish nonattainment at this endpoint.

Thus the corrected statement is:
\[
\inf\mathcal E=\inf\mathcal J
=\frac{4k}{k+6\chi(Y)}
\]
through the closed interval \(1\le k\le2\chi(Y)\), with nonattainment proved for \(1\le k<2\chi(Y)\). At \(k=2\chi(Y)\), attainment is exactly the half-conformally-flat/constant-scalar question above.

The endpoint is also where the range restriction becomes structurally visible. For \(k>2\chi(Y)\), the coefficient \(2\chi(Y)-k\) changes sign, so the lower estimate \(S\ge Y_{\rm hyp}^2\) no longer produces the same sharp bound.

### 3.3 Structure of \(P\)-minimizing sequences

If \(P(g_j)\to8\pi^2k\), the exact decomposition forces
\[
\int|W_{g_j}^+|^2\to0,
\]
\[
Y[g_j]^2-Y_{\rm hyp}^2\to0,
\]
and
\[
\int|\nabla u_j|^2\to0,\qquad
\int\left(\frac{\Delta u_j}{u_j}\right)^2\to0.
\]
Because every \(Y[g_j]\le Y_{\rm hyp}<0\),
\[
Y[g_j]\to Y_{\rm hyp}.
\]
The LeBrun identity also gives
\[
S(g_j)\to Y_{\rm hyp}^2.
\]

These are valid energy statements. They do not, by themselves, assign \(8\pi^2\) locally to each exceptional class. The explicit Burns sequence has \(k\) disjoint cores, each contributing \(8\pi^2+o(1)\); an arbitrary minimizing sequence requires a separate localization and compactness theorem before the same per-class allocation follows.

### 3.4 The fixed-\(k\) Yamabe assumption

Kobayashi’s connected-sum inequality gives
\[
\mathcal Y(X_k)\ge\mathcal Y(X_{k-1})
\ge\cdots\ge\mathcal Y(Y)\ge Y_{\rm hyp}.
\]
Hence equality \(\mathcal Y(X_k)=Y_{\rm hyp}\) forces equality at every preceding blow-up and on \(Y\). This part of the Step-23 discussion is correct.

For
\[
y_k=\frac{\mathcal Y(X_k)^2}{Y_{\rm hyp}^2}
\]
when \(\mathcal Y(X_k)<0\), the displayed unconditional estimates yield
\[
8\pi^2k-(1-y_k)16\pi^2\chi(Y)
\le\inf P\le8\pi^2k.
\]
When \(y_k=1\), these two values coincide. When \(y_k<1\), the inequalities alone do not determine whether the actual infimum is strictly below \(8\pi^2k\). Therefore the sentence that the gap equals the sharp value “exactly when \(y_k=1\)” is stronger than the derivation. The exact formulation is: \(y_k=1\) is sufficient, and it is precisely when the displayed Yamabe lower estimate meets the Burns upper value.

---

## 4. Corrected theorem statements

### Corrected Theorem C

For a one-ended, oriented marked cell
\[
U\cong D^4\#\overline{\mathbb{CP}}^{\,2}
\]
with an exact real- or complex-hyperbolic end, suppose \(u>0\) solves
\[
6\Delta_g u=s_gu+24u^3,\qquad u\to1,
\]
with sufficient derivative decay. Define \(\Delta W_+\) and \(\operatorname{RV}\) by matched relative truncations. Then
\[
P_{\rm cell}(g)-8\pi^2
 =4\Delta W_+
 +48\operatorname{RV}(\hat g)
 +3\int_U\left(\frac{\Delta u}{u}\right)^2
 +24\int_U|\nabla u|^2,
\]
and
\[
P_{\rm cell}(\hat g)-8\pi^2
 =4\Delta W_++48\operatorname{RV}(\hat g).
\]
The relative volume is independent of the matched compact cut and equals
\[
\bigl[\operatorname{Vol}_g(U_{\rm int})-\operatorname{Vol}_{g_0}(B)\bigr]
+\int_U(u^4-1)\,d\mu_g.
\]
Existence and uniqueness hold for every exact \(H^4\)-end cell; for CH ends they are established here when \(s_g<0\) everywhere and for sufficiently small perturbations of CH. General CH cells with \(s_g\ge0\) somewhere remain unresolved by the supplied analytic material.

### Corrected Theorem H

Assume
\[
\mathcal Y\!\left(Y\#k\overline{\mathbb{CP}}^{\,2}\right)=Y_{\rm hyp}.
\]
Then for \(k\ge1\),
\[
P(g)>8\pi^2k\quad\text{for every metric},\qquad
\inf P=8\pi^2k,
\]
and this \(P\)-infimum is not attained. For
\[
1\le k\le2\chi(Y),
\]
\[
\inf\mathcal E=\inf\mathcal J
=\frac{4k}{k+6\chi(Y)}.
\]
For \(1\le k<2\chi(Y)\), neither normalized infimum is attained. At \(k=2\chi(Y)\), attainment is equivalent to the existence of an anti-self-dual constant-scalar metric for \(\mathcal E\), and to an anti-self-dual metric for \(\mathcal J\); the Yamabe assumption alone does not decide this.

Every \(P\)-minimizing sequence satisfies the four integral convergences above and \(S(g_j)\to Y_{\rm hyp}^2\). Per-exceptional-class concentration is established for the constructed Burns sequence, not for arbitrary minimizing sequences.