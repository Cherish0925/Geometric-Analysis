# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 24,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step24_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step24_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify Theorems C and H in the Step-23 note against the conventions and cited LeBrun source. Check all normalizations, conformal identities, decay/boundary requirements, the conditional sharp P and Einstein-defect values, the range 1<=k<=2 chi(Y), the Burns upper sequence, and non-attainment. Identify any false statement or missing hypothesis and give exact corrected formulations. Also assess whether Theorem C's relative RV definition is invariant under moving the compact cutoff and what is actually known about existence of u on H4 versus CH cells.

## Integrated Scientific Memo

# Verification memo: Theorems C and H

## 1. Normalizations and LeBrun identity

The curvature conventions in Step 23 are consistent with the normalization ledger:
\[
8\pi^2(2\chi+3\tau)
=4\int |W^+|^2-P+\frac{S}{12},
\qquad
P=\int|\Ric^\circ|^2,\quad S=\int s^2.
\]

For real hyperbolic curvature \(K=-2\),
\[
\Ric=-6g,\qquad s=-24,\qquad W=0.
\]
Thus
\[
8\pi^2\chi(Y)=\frac1{24}S(g_{\rm hyp}),
\]
and consequently
\[
Y_{\rm hyp}^2=S(g_{\rm hyp})
=192\pi^2\chi(Y),\qquad
\frac{Y_{\rm hyp}^2}{12}=16\pi^2\chi(Y).
\]

With \(\Delta=\operatorname{div}\nabla\), the scalar conformal law for \(\hat g=u^2g\) is
\[
\hat s\,u^3=-6\Delta u+s_gu.
\]
For \(\hat s=-24\),
\[
6\Delta u=s_gu+24u^3.
\]
The algebra in (1.2)–(1.4) is correct and gives
\[
S(g)=Y[g]^2
+36\int\left(\frac{\Delta u}{u}\right)^2d\mu_g
+288\int|\nabla u|^2d\mu_g,
\]
hence, by conformal invariance of \(|W^+|^2d\mu\),
\[
P(g)-P(\hat g)
=
3\int\left(\frac{\Delta u}{u}\right)^2d\mu_g
+24\int|\nabla u|^2d\mu_g.
\]

This is not merely a new “sharpening” of LeBrun’s inequality: the full equality already appears in the computation proving Lemma 1 of §5 of the supplied 1996 paper, after converting Laplacian conventions. Likewise, the Yamabe-maximizer-implies-Einstein statement is discussed in §5, not §2.

---

## 2. Theorem C

### 2.1 Correct relative formulation

Fix an orientation-preserving marked end identification
\[
(U\setminus K,g)\cong (M_0\setminus B_{R_0},g_0),
\]
where \(g_0\) is either \(H^4\) with \(K=-2\), or \(\mathbb{CH}^2\) with holomorphic curvature \(-4\). For matched truncations \(U_R,B_R\), define
\[
\Delta W_+
=
\lim_{R\to\infty}
\left[
\int_{U_R}|W_g^+|^2d\mu_g
-
\int_{B_R}|W_{g_0}^+|^2d\mu_{g_0}
\right]
\]
and
\[
\RV_{g_0}(\hat g)
=
\lim_{R\to\infty}
\left[
\Vol_{\hat g}(U_R)-\Vol_{g_0}(B_R)
\right].
\]

Because \(g=g_0\) on the end and \(d\mu_{\hat g}=u^4d\mu_g\),
\[
\boxed{
\RV_{g_0}(\hat g)
=
\bigl[\Vol_g(U_{\rm int})-\Vol_{g_0}(B)\bigr]
+
\int_U(u^4-1)\,d\mu_g.
}
\]

The final integral must be over the **whole cell \(U\)**. If it were only over \(U_{\rm int}\), the expression would generally change when the cutoff is moved through the model end.

With the whole-cell integral, \(\RV\) is invariant under moving the matched compact cutoff: the added \(g\)-volume and model volume cancel exactly, while the integral over \(U\) is unchanged. This invariance is relative to the fixed end marking; it is not a claim of invariance under arbitrary changes of end identification or defining function. It is best called a matched relative volume, not automatically identified with Graham’s finite-part renormalized volume.

### 2.2 Boundary flux and decay

On a finite truncation \(U_R\), integration by parts contributes
\[
-24\int_{\partial U_R}u\,\partial_\nu u
\]
to the right side of the relative identity. Thus (1.5) requires this flux to vanish.

Writing \(u=1+w\), the exterior linearization is
\[
\Delta w=8w.
\]
The decaying indicial rates are

- real hyperbolic:
  \[
  w=O(e^{-4\sqrt2\,t}),\qquad
  \Area(\Sigma_t)\asymp e^{3\sqrt2 t};
  \]
- complex hyperbolic:
  \[
  w=O(e^{-(2+2\sqrt3)t}),\qquad
  \Area(\Sigma_t)\asymp e^{4t}.
  \]

These rates imply
\[
u^4-1\in L^1,\qquad
\nabla u\in L^2,\qquad
\frac{\Delta u}{u}\in L^2,\qquad
\int_{\Sigma_t}u\,\partial_\nu u\to0.
\]
The notation should be \(O(e^{-\alpha t})\), rather than necessarily \(w\sim e^{-\alpha t}\), because the leading coefficient may vanish. Corresponding derivative decay is also needed to make the Chern–Simons transgression of \(\hat g\) converge to the model one.

### 2.3 Relative Chern–Weil constant

For the one-blow-up cell
\[
U\cong D^4\#\overline{\mathbb{CP}}^{\,2},
\]
relative to a ball,
\[
\Delta\chi=1,\qquad
\Delta\tau=-1,\qquad
\Delta(2\chi+3\tau)=-1.
\]
Exact agreement of the collars cancels the boundary transgressions, giving
\[
P_{\rm cell}(g)-8\pi^2
=
4\Delta W_+
+
\lim_{R\to\infty}
\left[
\int_{U_R}\frac{s_g^2}{12}\,d\mu_g
-
48\Vol_{g_0}(B_R)
\right].
\]
Combining this with the relative Yamabe identity yields
\[
\boxed{
P_{\rm cell}(g)-8\pi^2
=
4\Delta W_+
+48\RV_{g_0}(\hat g)
+3\int_U\left(\frac{\Delta u}{u}\right)^2d\mu_g
+24\int_U|\nabla u|^2d\mu_g.
}
\]
Since the Weyl density is conformally invariant,
\[
\boxed{
P_{\rm cell}(\hat g)-8\pi^2
=
4\Delta W_+
+48\RV_{g_0}(\hat g).
}
\]

Thus Theorem C is correct as a conditional identity, provided that:

1. the cell topology is specified—\(D^4\#\overline{\mathbb{CP}}^{\,2}\) for the displayed \(8\pi^2\);
2. the exact end and orientation-preserving marking are fixed;
3. \(u>0\) exists, tends to \(1\), and has sufficient derivative decay;
4. \(\RV,\Delta W_+\), and \(P_{\rm cell}(\hat g)\) are defined by matched relative truncations;
5. \(\int(u^4-1)\) in the cutoff formula is over all of \(U\).

For a general cell
\[
D^4\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\]
the topological constant becomes
\[
8\pi^2(k+4\ell).
\]

In the real-hyperbolic case \(W_{g_0}^+=0\), so
\[
\Delta W_+=\int_U|W_g^+|^2\ge0.
\]
Hence \(\RV(\hat g)\ge0\) is sufficient for \(P_{\rm cell}\ge8\pi^2\). It is not necessary; the exact condition at the Yamabe representative is
\[
4\Delta W_++48\RV(\hat g)\ge0.
\]

### 2.4 What is actually established about \(u\)

#### Exact \(H^4\) ends

An exact real-hyperbolic end is smoothly conformally compact. The Loewner–Nirenberg/Aviles–McOwen singular Yamabe theory supports existence of a complete conformal metric of scalar curvature \(-24\) for arbitrary smooth compact perturbations; normalization against the exact hyperbolic end gives \(u\to1\). The ratio maximum principle gives uniqueness.

Thus the Step-23 existence assertion for \(H^4\) cells is supported.

#### Exact \(\mathbb{CH}^2\) ends

Complex-hyperbolic ends are ACH, not conformally compact in the ordinary real-hyperbolic sense, so the same theorem cannot simply be cited.

The supplied Step-21 argument rigorously establishes existence when
\[
s_g<0\quad\text{everywhere},
\]
equivalently \(s_g\le-c<0\), since \(s_g=-24\) outside a compact set. Constant sub- and supersolutions then give an exhaustion construction. It also covers sufficiently small compact perturbations by an implicit-function argument.

For CH cells with \(s_g\ge0\) somewhere, no general existence theorem is established in the supplied sources. The identity
\[
6\lambda_0(\mathbb{CH}^2)+s_{\rm CH}=6\cdot4-24=0
\]
shows that the naive conformal-Laplacian coercivity argument is spectrally critical, but it neither proves existence nor nonexistence.

One branch proposed a global double-well variational argument for all compact perturbations and all signs of \(s\). That is an interesting possible extension, but the supplied sketch does not close several noncompact variational issues sufficiently to promote it to a verified theorem here: preservation of the asymptotic condition in the admissible class, exclusion of loss at infinity, regularity/positivity at critical growth, and derivation of the exact indicial asymptotics for the minimizer. Consequently, the defensible current statement is:

- universal existence and uniqueness for exact \(H^4\) ends;
- existence and uniqueness for CH ends when \(s_g<0\), and for sufficiently small perturbations;
- general CH existence when \(s_g\) becomes nonnegative somewhere remains unresolved by the supplied material.

Newton convergence in the listed diagonal examples is numerical evidence, not a rigorous existence proof unless paired with an a posteriori enclosure.

---

## 3. Theorem H

Let
\[
X_k=Y\#k\overline{\mathbb{CP}}^{\,2}.
\]
Because a closed real-hyperbolic four-manifold has \(\tau(Y)=0\),
\[
2\chi(X_k)+3\tau(X_k)=2\chi(Y)-k.
\]
Chern–Weil gives, for every metric,
\[
\boxed{
P(g)
=
8\pi^2k+4\int|W^+|^2
+\frac{S(g)-Y_{\rm hyp}^2}{12}.
}
\]

Assume
\[
\tag{H}
\mathcal Y(X_k)=Y_{\rm hyp}<0.
\]
Then every conformal class has
\[
Y[g]\le Y_{\rm hyp}<0,
\]
and therefore \(Y[g]^2\ge Y_{\rm hyp}^2\). Combining this with LeBrun’s identity gives
\[
\boxed{
P(g)
=
8\pi^2k+4\int|W^+|^2
+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}
+3\int\left(\frac{\Delta u}{u}\right)^2
+24\int|\nabla u|^2.
}
\]

### 3.1 Sharp \(P\)-value and nonattainment

All terms after \(8\pi^2k\) are nonnegative, so
\[
P(g)\ge8\pi^2k.
\]
If equality held, then
\[
W^+=0,\qquad Y[g]=Y_{\rm hyp},\qquad \nabla u=0.
\]
Thus \(g\), up to scale, would be a constant-negative-scalar metric whose conformal class attains the Yamabe invariant. Equivalently, it globally minimizes \(S=\int s^2\). At constant \(s\ne0\), the Euler–Lagrange equation is
\[
-2s\,\Ric+\frac12s^2g=0,
\]
so \(\Ric=(s/4)g\), hence \(P=0\), contradicting \(P=8\pi^2k>0\). Therefore
\[
\boxed{P(g)>8\pi^2k\quad\text{for every metric}.}
\]

On the hyperbolic bulk,
\[
\mathbf R^+=W^++\frac{s}{12}I=-2I.
\]
Applying Theorem F at \(k\) disjoint points gives
\[
P(g_{x_0})
=
8\pi^2k(1+2x_0)+O(kx_0^{6/5}),
\]
so
\[
\boxed{\inf P=8\pi^2k,}
\]
and the infimum is not attained.

This part of Theorem H is correct.

### 3.2 The normalized defects

Put \(t=P/S\). Then
\[
\mathcal J=\frac{4P}{P+S/4}
=\frac{16t}{4t+1},
\]
which is increasing in \(t\). The exact formula above implies
\[
t\ge \frac1{12}
-\frac{8\pi^2(2\chi(Y)-k)}{S}.
\]
Under (H),
\[
S\ge Y[g]^2\ge Y_{\rm hyp}^2
=192\pi^2\chi(Y).
\]
When \(k\le2\chi(Y)\), the right side is nondecreasing in \(S\), hence
\[
t\ge\frac{k}{24\chi(Y)},
\]
and therefore
\[
\mathcal E\ge\mathcal J
\ge\frac{4k}{k+6\chi(Y)}.
\]

The Burns metrics satisfy
\[
P\to8\pi^2k,\qquad S\to Y_{\rm hyp}^2,
\qquad \int(s-\bar s)^2\to0.
\]
The last conclusion is valid, but the sentence “the scalar curvature differs from \(-24\) only on cores of volume \(O(x_0^2)\)” is inaccurate: intermediate and cutoff annuli also contribute. The estimates in Theorem F nevertheless show that their total \(L^2\) scalar defect tends to zero. Thus
\[
\boxed{
\inf\mathcal E=\inf\mathcal J
=\frac{4k}{k+6\chi(Y)}
\qquad (1\le k\le2\chi(Y)).
}
\]

### 3.3 Endpoint correction at \(k=2\chi(Y)\)

The Step-23 claim of nonattainment throughout the closed range is not proved at the endpoint.

If \(1\le k<2\chi(Y)\), equality in the normalized lower bound forces
\[
S=Y_{\rm hyp}^2,\qquad W^+=0,
\]
and then forces a Yamabe-invariant-attaining metric, hence an Einstein contradiction. Thus both \(\mathcal J\) and \(\mathcal E\) fail to attain their infima.

At
\[
k=2\chi(Y),
\]
the coefficient involving \(S^{-1}\) vanishes:
\[
P=\frac{S}{12}+4\int|W^+|^2.
\]
Therefore
\[
\mathcal J\ge1,\qquad \mathcal E\ge1,
\]
and Burns metrics give infimum \(1\). In fact this value is unconditional, independent of (H):
\[
\boxed{
\inf\mathcal J=\inf\mathcal E=1
\quad\text{on }X_{2\chi(Y)}.
}
\]

The equality conditions are
\[
\mathcal J(g)=1
\iff W^+\equiv0,
\]
and
\[
\mathcal E(g)=1
\iff W^+\equiv0
\ \text{and}\ s\ \text{is constant}.
\]
Here constant scalar curvature cannot be zero because \(2\chi+3\tau=0\) and \(W^+=0\) would then force \(P=0\), giving an Einstein metric, excluded by the entropy obstruction. Thus attainment of \(\mathcal E=1\) is equivalent to existence of an anti-self-dual constant nonzero scalar-curvature metric. The supplied material does not decide this.

Accordingly:

- nonattainment is proved for \(1\le k<2\chi(Y)\);
- at \(k=2\chi(Y)\), the value is known but attainment remains unresolved;
- \(\mathcal J\)-attainment requires only an anti-self-dual metric, while \(\mathcal E\)-attainment additionally requires constant scalar curvature.

### 3.4 Minimizing-sequence statement

If
\[
P(g_j)\to8\pi^2k,
\]
the exact nonnegative decomposition implies
\[
\int|W^+_{g_j}|^2\to0,
\]
\[
Y[g_j]\to Y_{\rm hyp},
\]
\[
\int|\nabla u_j|^2\to0,\qquad
\int\left(\frac{\Delta u_j}{u_j}\right)^2\to0,
\]
and hence
\[
S(g_j)\to Y_{\rm hyp}^2.
\]

These are correct global energy conclusions. The further phrase

> “with \(8\pi^2\) carried by each exceptional class”

does not follow from (3.2). It holds for the explicitly constructed \(k\)-center Burns sequence, but proving it for an arbitrary minimizing sequence requires a localization/bubble compactness theorem assigning topological charge to individual concentration regions.

### 3.5 Fixed-\(k\) Yamabe hypothesis

Kobayashi’s connected-sum inequality gives
\[
\mathcal Y(X_k)\ge\mathcal Y(X_{k-1})
\ge\cdots\ge\mathcal Y(Y)\ge Y_{\rm hyp}.
\]
Thus equality at \(k\) indeed forces equality for every \(k'\le k\), including \(Y\).

The sentence that the sharp \(P\)-gap occurs “exactly when \(y_k=1\)” is stronger than the argument. The bounds show only that \(y_k=1\) is sufficient, and precisely the condition under which the displayed Yamabe lower bound meets the Burns upper bound. They do not exclude
\[
\inf P=8\pi^2k
\]
when \(y_k<1\), because the remaining Weyl and conformal-square terms could compensate.

---

## 4. Corrected formulations

### Corrected Theorem C

Let \(U\cong D^4\#\overline{\mathbb{CP}}^{\,2}\) be an oriented one-ended marked cell whose metric \(g\) equals the normalized real- or complex-hyperbolic model outside a compact set. Suppose there exists \(u>0\) satisfying
\[
6\Delta_gu=s_gu+24u^3,\qquad u\to1,
\]
with sufficient derivative decay, and set \(\hat g=u^2g\). Define all relative quantities by matched truncations. Then
\[
P_{\rm cell}(g)-8\pi^2
=
4\Delta W_+
+48\RV(\hat g)
+3\int_U\left(\frac{\Delta u}{u}\right)^2
+24\int_U|\nabla u|^2,
\]
and
\[
P_{\rm cell}(\hat g)-8\pi^2
=
4\Delta W_++48\RV(\hat g).
\]
Moreover,
\[
\RV(\hat g)
=
[\Vol_g(U_{\rm int})-\Vol_{g_0}(B)]
+\int_U(u^4-1)\,d\mu_g,
\]
which is independent of moving the matched cutoff through the exact end.

Existence and uniqueness are established for arbitrary exact \(H^4\)-end cells; for CH ends they are established in the supplied material when \(s_g<0\) everywhere and for sufficiently small compact perturbations. General CH existence with \(s_g\ge0\) somewhere remains open here.

### Corrected Theorem H

Assume
\[
\mathcal Y\!\left(Y\#k\overline{\mathbb{CP}}^{\,2}\right)=Y_{\rm hyp}.
\]
Then, for every \(k\ge1\),
\[
P(g)>8\pi^2k\quad\text{for every metric},\qquad
\inf P=8\pi^2k,
\]
and the \(P\)-infimum is not attained.

For
\[
1\le k\le2\chi(Y),
\]
\[
\inf\mathcal E=\inf\mathcal J
=\frac{4k}{k+6\chi(Y)}.
\]
For
\[
1\le k<2\chi(Y),
\]
neither infimum is attained. At \(k=2\chi(Y)\), the common value \(1\) is unconditional, but nonattainment is not established: \(\mathcal J\)-attainment is equivalent to existence of an anti-self-dual metric, and \(\mathcal E\)-attainment to existence of an anti-self-dual constant-scalar metric.

Every \(P\)-minimizing sequence has the global energy convergences listed above. Per-exceptional-class \(8\pi^2\) concentration is proved for the Burns construction, not for arbitrary minimizing sequences.

## 5. Additional correction beyond the stated range

For \(k>2\chi(Y)\), Chern–Weil gives \(\mathcal J(g)>1\) for every metric, but the claim should not be phrased as a uniform gap above \(1\). Conformal inflation within a negative Yamabe class makes \(S\to\infty\), with
\[
P=\frac{S}{12}+O(1),
\]
so
\[
\inf\mathcal J=1,
\]
not attained. The corresponding \(\inf\mathcal E\) is not determined by this argument; only
\[
1\le\inf\mathcal E
\le \frac{4k}{k+6\chi(Y)}
\]
is supplied by the present bounds and Burns upper sequence.