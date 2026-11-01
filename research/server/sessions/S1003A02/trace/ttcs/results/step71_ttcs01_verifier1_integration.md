# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 71,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step71_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step71_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of the Step-71 note on the Einstein-defect functional E(g)=inf_{lambda!=0} int|Ric-lambda g|^2/(lambda^2 V) on closed oriented 4-manifolds. Check with full rigor, and correct where needed: (1) Identity 71.1 E-1=(12 int|W^±|^2+L_s-24pi^2 T_±)/R, T_±=2chi±3tau, in LeBrun's conventions (compare the inherited corpus statement at Curvature_Realizability lines 1520-1543 if given in the excerpt) and the JSON example checks. (2) Theorem 71.B: strictness for T_+<0; the equality characterization E=1 iff W^+=0 and s nonzero constant when T_+=0<=T_-; the attainment criterion via Yamabe classes; the positive-scalar Betti classification (b1,b2) in {(0,4),(1,0)} (Weitzenbock with W^+=0, s>0 gives b_+=0). (3) Theorem 71.C: alpha=1 attained on S^1 x S^3/Gamma, S^1 x_phi H^3/Gamma, and #4 CPbar^2 via LeBrun's hyperbolic-ansatz self-dual classes with positive scalar representatives (source lines quoted in the note); non-existence of Einstein metrics on these; the claim that K3 and T^4 have alpha>=1 although Ricci-flat; the ASD constant-scalar formula E=1+9m/(3m+4y). (4) Theorem 71.D, the long-circle reservoir: alpha(N # (S^1 x Y))<=1 for any N and Y spherical space form or hyperbolic 3-manifold, by taking S^1 of length L -> infinity and gluing a rescaled N in a fixed ball. Scrutinize whether all junk terms (R, W^+, L_s including the mean-scalar shift, the neck) are really O(1) uniformly in L, whether scale-invariance is used correctly, and the corollary alpha(X#kCPbar^2#l(S^1xS^3)) <= min(1,4h/(1+h)), =1 iff k+4l>=A. (5) Lemma 71.T and the alpha-readings of 59.C/59.N/59.Z: especially the Gauss-Bonnet argument that E-small sequences normalized at lambda_opt=1 have V<=12pi^2 chi(1+o(1)) and cannot collapse totally with bounded curvature, and the a^4/6 EH alpha-rate on CP^2#CP^2. Also state precisely what is new versus classical (Hitchin-Thorpe, LeBrun-Nayatani-Nitta Gauss-Bonnet form, corpus) as far as the supplied sources allow, and name any knowledge_request needed for precedence. Give a direct scientific memo with corrected statements.

## Integrated Scientific Memo

# Scientific verification memo: Step 71

The functional identity, unit-wall equality characterization, the attained value on \(\#4\overline{\mathbb{CP}}^2\), and the long-circle construction are correct. The important corrections concern the scope of the Yamabe formulas, the unsupported converse in the connected-sum corollary, the exclusion of collapse, and the unverified EH rate constant.

The actual `Curvature_Realizability` passages, Ishida–LeBrun line 400, Anderson’s theorem, and the adapted EH metric construction are not supplied here. Their contents cannot be independently certified from the note’s references alone.

## 1. Exact minimization and Identity 71.1

Write
\[
V=\operatorname{Vol}(g),\quad R=\int|\operatorname{Ric}|^2,\quad
T_s=\int s,\quad P=\int|\operatorname{Ric}^{\circ}|^2,\quad
S=\int s^2,\quad L_s=S-\frac{T_s^2}{V}.
\]
For \(R>0\), setting \(x=1/\lambda\) gives
\[
\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}
=4+\frac RVx^2-\frac{2T_s}{V}x.
\]
Consequently,
\[
\boxed{\mathcal E=4-\frac{T_s^2}{RV}=\frac{4P+L_s}{R}.}
\]
If \(T_s\ne0\), the minimum occurs at
\[
\lambda_{\rm opt}=\frac{R}{T_s}.
\]
If \(T_s=0<R\), the infimum is \(4\), approached as \(|\lambda|\to\infty\), but not attained in the \(\lambda\)-optimization. If \(R=0\), the metric is Ricci-flat and the defining quotient equals \(4\) for every \(\lambda\ne0\).

In the conventions explicitly supplied by LeBrun–Nayatani–Nitta,
\[
8\pi^2T_\pm
=4\int|W^\pm|^2+\frac S{12}-P,\qquad T_\pm=2\chi\pm3\tau.
\]
Since \(R=P+S/4\), this yields
\[
\boxed{R=4P+24\pi^2T_\pm-12\int|W^\pm|^2}
\]
and, for \(R>0\),
\[
\boxed{\mathcal E-1
=\frac{12\int|W^\pm|^2+L_s-24\pi^2T_\pm}{R}.}
\tag{71.1}
\]
The coefficient \(24\pi^2\), the Weyl coefficient \(12\), and all signs are correct. This also agrees with the supplied Step-59 identity
\[
P=4\int|W^+|^2+\frac S{12}-8\pi^2T_+.
\]

The quotient identity is **undefined at Ricci-flat metrics**. Its denominator-free companion remains valid there.

### JSON and script

All displayed numerical values and residuals are correct. However:

- The K3 branch directly assigns \(4\) to `E_formula` and `E_identity`. It does not test the quotient identity at \(R=0\). That field should instead say “not applicable,” while recording \(\mathcal E=4\) from the definition.
- Every explicit metric tested has \(L_s=0\). The variable-scalar term is proved algebraically above, not exercised by these examples.
- The two symbolic checks with \(m=0\) are the same substitution, and omit the necessary exclusion of \(y=0\).

The range statements are correct:
\[
0\le\mathcal E\le4,\qquad
\mathcal E=4\iff T_s=0,
\]
including Ricci-flat metrics, and
\[
\alpha=0\text{ attained}\iff
\text{a non-Ricci-flat Einstein metric exists}.
\]
The assertion \(\alpha(M)<4\) uses the classical existence of a negative-scalar-curvature metric.

## 2. Corrected Theorem 71.B

Choose the orientation so that \(T_+=T_{\min}=2\chi-3|\tau|\).

### Unit wall and strictness

If \(T_+\le0\), then \(\mathcal E(g)\ge1\) for every metric; Ricci-flat metrics are handled separately by \(\mathcal E=4\).

If \(T_+<0\), Ricci-flat metrics cannot exist, and every metric satisfies
\[
\boxed{\mathcal E(g)\ge1+\frac{24\pi^2|T_+|}{R(g)}>1.}
\]
Thus \(\alpha=1\), if true, is not attained. More precisely,
\[
\mathcal E(g_j)\to1
\iff
\frac{12\int|W^+_{g_j}|^2+L_s(g_j)+24\pi^2|T_+|}
     {R(g_j)}\to0.
\]
In particular \(R(g_j)\to\infty\), and both Weyl energy and scalar variance are \(o(R(g_j))\). Here \(R\) is already scale invariant in dimension four; this divergence cannot be removed by homothety.

### Equality and Yamabe attainment

When \(T_+=0\),
\[
\boxed{\mathcal E(g)=1
\iff W^+_g=0\ \text{and }s_g\text{ is a nonzero constant}.}
\]
Indeed, the numerator in (71.1) is a sum of nonnegative terms. A zero constant scalar curvature cannot give equality: the functional then equals \(4\).

Since half-conformal flatness is conformally invariant, and every conformal class has a Yamabe representative,
\[
\boxed{\alpha(M)=1\text{ attained}
\iff \exists[g]\text{ with }W^+=0,\quad Y([g])\ne0.}
\]
A constant-scalar metric has the sign of its class’s Yamabe constant: its conformal Laplacian has the constant function as its positive first eigenfunction. The attaining metrics are **all** nonzero constant-scalar representatives of these classes, not just Yamabe minimizers.

No Einstein metric attains the value \(1\).

### Positive-scalar equality topology

For a self-dual harmonic two-form,
\[
0=\int\left(|\nabla\omega|^2+\frac{s}{3}|\omega|^2
             -2\langle W^+\omega,\omega\rangle\right).
\]
Thus \(W^+=0,\ s>0\) implies \(b_+=0\). Using
\[
T_+=4-4b_1+5b_+-b_-,
\]
equality gives \(b_-=4-4b_1\), hence
\[
\boxed{(b_1,b_2)\in\{(0,4),(1,0)\}.}
\]

The unconditional conclusion in the first case is that the intersection form on the free part is negative definite. The supplied materials do not settle the precise fundamental-group hypotheses of the general Donaldson diagonalization theorem. A fully justified formulation is:

> If \(M\) is additionally simply connected, Donaldson gives the form \(-I_4\), and Freedman gives a homeomorphism \(M\cong\#4\overline{\mathbb{CP}}^2\).

This does not assert that simple connectivity is necessary for every extension of Donaldson’s theorem. The quoted Pedersen–Poon statement in the supplied paper may yield a stronger differentiable classification in this geometric setting; its exact hypotheses should be retrieved before invoking that strengthening.

There is an elementary additional restriction. In the \((b_1,b_2)=(0,4)\) case, \(\chi=6\). Any connected finite cover inherits the equality geometry and the same Betti dichotomy, so its Euler characteristic is either \(6\) or \(0\). Multiplicativity gives \(6d\), forcing \(d=1\). Therefore
\[
\boxed{\pi_1(M)\text{ has no proper finite-index subgroup}.}
\]
This does not by itself imply \(\pi_1(M)=1\).

## 3. Corrected Theorem 71.C

### Products and isometric mapping tori

For \(Y\) of sectional curvature \(c=\pm1\), the locally product metric has
\[
\operatorname{Ric}\text{ eigenvalues }(0,2c,2c,2c),\quad
s=6c,\quad P=3V,\quad R=12V,\quad W=0.
\]
The metric descends to an isometric mapping torus when the monodromy is orientation preserving. Its Euler characteristic vanishes, and \(W=0\) gives \(\tau=0\). Hence
\[
\boxed{\alpha(S^1\times S^3/\Gamma)=1,\qquad
\alpha(S^1\times_\phi H^3/\Gamma)=1,}
\]
attained by these locally product metrics.

Their Einstein nonexistence needs no delicate Hitchin equality classification. For an Einstein metric,
\[
8\pi^2\chi=\int\left(|W|^2+\frac{s^2}{24}\right).
\]
Thus \(\chi=0\) forces flatness. A closed flat four-manifold has fundamental group virtually \(\mathbb Z^4\). The spherical product has group virtually \(\mathbb Z\), and the hyperbolic mapping torus contains a closed hyperbolic three-manifold group, which is not virtually abelian. Neither can be flat.

### \(\#4\overline{\mathbb{CP}}^2\)

Here
\[
\chi=6,\qquad \tau=-4,\qquad T_+=0.
\]
The supplied LeBrun–Nayatani–Nitta introduction explicitly states that the hyperbolic-ansatz classes on every \(n\mathbb{CP}^2\) contain positive-scalar representatives. Section 3 describes their compactification on \(n\mathbb{CP}^2\). Reversing orientation and choosing a Yamabe representative gives \(W^+=0,\ s>0\). Therefore
\[
\boxed{\alpha(\#4\overline{\mathbb{CP}}^2)=1\quad\text{and is attained}.}
\]

There is also a direct Einstein obstruction:

- A nonzero Einstein constant would give \(\mathcal E=0\), contradicting the unit wall.
- A Ricci-flat metric would have \(W^+=0\), since \(T_+=0\). Its induced connection on \(\Lambda^+\) is flat. Simple connectivity would then produce three global parallel self-dual two-forms, contradicting \(b_+=0\).

Thus no Einstein metric exists. The supplied paper’s Theorem 1.3 also confirms that the positive-scalar attaining metrics cannot have nonnegative **Ricci operator**.

### ASD constant-scalar formula: correct with a notation repair

On
\[
M=k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3),
\qquad m=k+4\ell-4,
\]
let \(W^+=0\), let \(s\) be a nonzero constant, and define
\[
y=\frac{s^2V}{32\pi^2}.
\]
Then
\[
P=8\pi^2m+\frac{s^2V}{12}
  =\frac{8\pi^2}{3}(3m+y),
\qquad
R=\frac{8\pi^2}{3}(3m+4y),
\]
so
\[
\boxed{\mathcal E
=\frac{4(3m+y)}{3m+4y}
=1+\frac{9m}{3m+4y}.}
\]
The geometrically admissible parameters satisfy
\[
y>0,\qquad 3m+y\ge0.
\]
One may write \(y=Y([g])^2/(32\pi^2)\) **only when the chosen metric is a Yamabe minimizer**. Constant scalar curvature alone does not imply \(s^2V=Y([g])^2\).

For positive Yamabe minimizers, the sphere bound gives \(y\le12\). This bound does not control \(Y^2\) in negative Yamabe classes. The formula is algebraic and does not itself prove the existence of ASD classes for arbitrary \((k,\ell)\); the claimed Ishida–LeBrun existence passage is absent.

### Ricci-flat examples and unresolved values

For a Ricci-flat metric,
\[
T_\pm=\frac1{2\pi^2}\int|W^\pm|^2.
\]
K3 in its complex orientation has \(T_+=0\), and \(T^4\) has \(T_+=T_-=0\). Therefore
\[
\boxed{\alpha(K3)\ge1,\qquad \alpha(T^4)\ge1,}
\]
although both admit Einstein metrics. Those Ricci-flat metrics have \(\mathcal E=4\).

For \(T^4\), the two branches disagree about half-flatness. The signature identity resolves this:
\[
\tau=0,\quad W^+=0
\ \Longrightarrow\ \int|W^-|^2=0.
\]
Thus **any half-conformally-flat metric on \(T^4\) is fully conformally flat**. Its attainment question really is about conformally flat classes with nonzero Yamabe constant. The assertion that such classes must be of flat conformal type, and the assertion that this problem is open, are not established by the supplied sources.

For K3, attainment at \(1\) requires an ASD class with nonzero Yamabe constant; using the classical psc obstruction, its sign must be negative. The supplied material does not decide existence or the value of \(\alpha\).

For \(S^2\times T^2\), the product has \(\mathcal E=2\), so
\[
1\le\alpha(S^2\times T^2)\le2.
\]
Positive-scalar attainment at \(1\) is excluded by \(b_+=b_-=1\). Negative-scalar attainment and the exact infimum remain undecided here.

## 4. Theorem 71.D: rigorous reservoir construction

The theorem is valid. Its proof becomes completely uniform by fixing the connected-sum replacement **once**, without taking its scale to zero.

Let
\[
Q_L=S^1_L\times Y,\qquad q=\operatorname{Vol}(Y),\qquad s_0=\pm6.
\]
For all sufficiently large \(L\), a fixed small ball in \(Q_L\) has identical local geometry. Replace this ball by a fixed smooth piece \(\Omega\) containing the punctured, fixed-rescaled \(N\) and a fixed neck. The resulting metric is exactly the product outside \(\Omega\).

Put \(x=Lq-v_B\), where \(v_B\) is the removed ball’s volume, and write the fixed replacement integrals as
\[
v_\Omega=\operatorname{Vol}(\Omega),\quad
t_\Omega=\int_\Omega s,\quad
r_\Omega=\int_\Omega|\operatorname{Ric}|^2.
\]
Then exactly
\[
V=x+v_\Omega,\qquad T_s=s_0x+t_\Omega,\qquad R=12x+r_\Omega.
\]
In particular, \(R=12Lq+O(1)\); writing “\(-O(1)\)” is unnecessarily restrictive.

Let
\[
a=t_\Omega-s_0v_\Omega=\int_\Omega(s-s_0),\qquad
J=\int_\Omega(s-s_0)^2.
\]
The mean-scalar shift and total variance satisfy the exact formulas
\[
\bar s=s_0+\frac aV,\qquad
\boxed{L_s=J-\frac{a^2}{V}=J+O(L^{-1}).}
\]
Thus the unchanged product region contributes \(O(L^{-1})\), while the replacement contributes \(O(1)\). Also
\[
\int|W^\pm|^2=\int_\Omega|W^\pm|^2=O(1).
\]
All neck terms are uniformly bounded because the neck is literally fixed.

Four-dimensional scale invariance correctly explains why the curvature-square integrals of a fixed-rescaled piece are unchanged. It does **not** bound an arbitrary varying neck, nor make volume or total scalar curvature scale invariant. Those latter quantities are controlled here by the fixed construction.

Equation (71.1) now gives
\[
\mathcal E(g_L)-1
=\frac{12\int_\Omega|W^+|^2+J-24\pi^2T_+(M)}
       {12Lq}+O(L^{-2}),
\]
and hence
\[
\boxed{\alpha\bigl(N\#(S^1\times Y)\bigr)\le1.}
\]

### Connected-sum consequences

For \(\ell\ge1\),
\[
T_\pm\bigl(N\#\ell(S^1\times S^3)\bigr)=T_\pm(N)-4\ell.
\]
Therefore
\[
\boxed{T_{\min}(N)\le4\ell
\ \Longrightarrow\
\alpha\bigl(N\#\ell(S^1\times S^3)\bigr)=1.}
\]
It is not attained if the resulting \(T_{\min}<0\). If \(T_{\min}=0\), attainment is exactly the half-flat, nonzero-Yamabe criterion.

For the general-type family, assuming the inherited notation \(T_+(X)=A\), one obtains
\[
k+4\ell\ge A\Longrightarrow\alpha=1.
\]
The converse is **not proved**. The claimed recovery estimate
\[
\alpha\le\min\left\{1,\frac{4h}{1+h}\right\},
\qquad h=\frac{k+4\ell}{A},
\]
also requires verification of the absent corpus passage establishing the second bound with handles. If that estimate is available, it excludes \(\alpha=1\) for \(h<1/3\), but leaves \(1/3\le h<1\) unresolved. Replace “iff” by “if.”

### A supported extension: self-covering reservoirs

If \(Z\) admits connected finite covers of unbounded degree whose total spaces are diffeomorphic to \(Z\), then
\[
\boxed{\alpha(N\#Z)\le\alpha(Z).}
\]
Indeed, lift any fixed metric with \(R>0\) to a degree-\(d\) cover. Its \(R,T_s,V\) multiply by \(d\), so \(\mathcal E\) is unchanged. A fixed-ball replacement changes these three integrals by constants independent of \(d\); the connected-sum defect converges to the original metric’s defect. Taking the metric infimum proves the claim.

This applies to \(S^1\times Y\) for every closed \(Y\), and explains the reservoir as an extensive-energy mechanism. It does not imply that every mapping torus is diffeomorphic to arbitrarily large cyclic covers. The note’s \(L/r\) argument against other reservoirs is a heuristic, not a general impossibility theorem.

## 5. Lemma 71.T and the corrected Step-59 readings

### Yamabe translation

For \(R>0\),
\[
\mathcal E\ge\frac{4P}{R}.
\]
At a Yamabe minimizer with \(Y\ne0\),
\[
\boxed{\mathcal E=\frac{16P}{4P+Y^2}.}
\]
The value at \(\lambda=s/4\) is \(16P/Y^2\), only an upper bound for the optimized defect. Thus, on Yamabe representatives,
\[
\mathcal E\to0\iff P/Y^2\to0.
\]
A sequence with \(P\to0\) and degenerating Yamabe scale need not have \(\mathcal E\to0\).

The note’s unrestricted “exact quotient”
\[
\alpha=\inf\frac{4p}{p+A+\upsilon}
\]
needs additional justification. The expression is exact **on the Yamabe representatives**. Equality with the infimum over all metrics cannot be inferred merely from the existence of those representatives.

For example, within a negative Yamabe class, Weyl energy is conformally invariant and
\[
P=q+\frac S{12},\quad R=q+\frac S3,\quad
\mathcal E=4-\frac b{q+S/3},
\quad q=4\int|W^+|^2-8\pi^2T_+,\quad b=\frac{T_s^2}{V}.
\]
For \(T_s\le0\), the Yamabe inequality gives \(b\le Y^2\), while \(S\ge Y^2\); hence the Yamabe metric minimizes \(\mathcal E\) in this restricted sector. But a negative Yamabe class can contain metrics with \(T_s>0\). The supplied materials contain no argument disposing of that sector.

A useful unconditional bound, when \(T_{\min}>0\), is
\[
\boxed{\alpha(M)\ge
\frac{\mathfrak p_*}{\mathfrak p_*+\frac34T_{\min}},
\qquad \mathfrak p_*=\frac{P_*}{8\pi^2}.}
\]
It follows from \(R\le4P+24\pi^2T_{\min}\) and monotonicity. On supply manifolds, the stated Yamabe lower bound would give the upper estimate
\[
\alpha\le\frac{4\mathfrak p_*}{A+\mathfrak p_*},
\]
because passing to the negative Yamabe representative decreases \(P\). These two bounds suffice for zero-infimum equivalence there; an unrestricted exact-quotient theorem is not needed for that conclusion.

### Einstein-scale normalization and an exact Gauss–Bonnet identity

For \(\mathcal E<4\), normalize
\[
\lambda_{\rm opt}=\sigma,\qquad \sigma\in\{+1,-1\}.
\]
Positive homothety cannot change its sign. Then
\[
T_s=\sigma R,\qquad R=(4-\mathcal E)V.
\]
The original \(\lambda_{\rm opt}=1\) statement is correct for positive total scalar curvature but does not cover negative Einstein limits.

From (71.1),
\[
\mathcal E\le1-\eta
\Longrightarrow
R\le\frac{24\pi^2T_\pm}{\eta}
\]
for either sign; in particular both \(T_\pm\) must be positive.

Substituting the normalized relations into Gauss–Bonnet gives the stronger exact identity
\[
\boxed{48\pi^2\chi
=6\int|W|^2+L_s+(4-\mathcal E)(1-\mathcal E)V.}
\tag{*}
\]
Therefore \(\mathcal E<1\) forces \(\chi>0\), and
\[
V\le\frac{48\pi^2\chi}{(4-\mathcal E)(1-\mathcal E)}.
\]
For an \(\mathcal E\)-small sequence,
\[
P=o(V),\quad L_s=o(V),\quad S=16V+o(V),
\]
so
\[
8\pi^2\chi=\int|W|^2+\frac23V+o(V),\qquad
\boxed{V\le12\pi^2\chi(1+o(1)).}
\]
In particular \(P\to0\), and \(\alpha=0\) implies \(P_*=0\).

If additionally \(V\to0\) and curvature is **globally** uniformly bounded, \(\int|W|^2=O(V)\), contradicting \(\chi>0\). This exclusion is rigorous.

It does **not** exclude collapse with finitely many shrinking curvature-concentration balls. Such balls may carry the Euler characteristic even as total volume tends to zero.

### 59.C: total bounded-curvature collapse

Replace its old \(\alpha\)-claims by
\[
P_*\le36\,\operatorname{Vol}_{|r|}\le36\,\operatorname{MinVol}.
\]
If \(\operatorname{MinVol}=0\), Chern–Weil gives \(\chi=\tau=0\), so
\[
\alpha\ge1,
\]
not \(\alpha=0\). This correctly separates the collapse mechanism for \(P\) from the human functional.

### 59.N: orbifold resolutions

For a compact Einstein orbifold with Einstein constant \(\kappa\ne0\), compatible Ricci-flat ALE replacements yield
\[
P\to0,\quad L_s\to0,\quad
R\to4\kappa^2V_{\rm orb}>0.
\]
The scalar-variance conclusion follows from the shrinking replacement volume and the derivative-controlled **Ricci/scalar** cutoff estimates. No vanishing of the ALE core’s full curvature energy is required. Thus these constructions give \(\alpha=0\).

For \(\kappa=0\), they only give \(P\to0\) and \(R\to0\). No conclusion about \(\alpha\) follows without additional information. The Kummer–K3 example has \(\alpha\ge1\) for its separate topological reason.

The corrected cusp-double and filling constructions of 59.D likewise survive as \(\alpha=0\) constructions: their bounded-curvature transition regions have vanishing volume, so \(L_s\to0\), while the nonzero negative-Einstein bulk keeps \(R\) bounded below.

### 59.Z: no established transfer of the trichotomy

Anderson’s supplied description concerns selected \(P\)-regularized minimizing sequences, not arbitrary \(\mathcal E\)-minimizing sequences. Two distinctions remain essential:

1. Passing from \(\alpha=0\) to \(P_*=0\) does not show that the selected \(P\)-sequence preserves the normalized nonzero Einstein scale of an \(\mathcal E\)-small sequence.
2. Anderson’s collapse alternative allows exceptional shrinking balls, and is not excluded by the global bounded-curvature argument.

Thus the sentence “alternative (II) is excluded” must be removed or restricted to **globally bounded-curvature, bubble-free collapse of the same normalized \(\mathcal E\)-small sequence**.

If a compactness theorem does apply to that same sequence, then
\[
\int|\operatorname{Ric}-\sigma g|^2=\mathcal EV\to0
\]
forces every smooth noncollapsed limit to have Einstein constant \(\sigma\ne0\). This is a valid conditional conclusion, not an established complete decomposition theorem.

## 6. EH rate on \(\mathbb{CP}^2\#\mathbb{CP}^2\)

The arithmetic is correct:
\[
V_{\rm orb}=\frac{4\pi^2}{3},\qquad \kappa=3,\qquad
R\to48\pi^2,\qquad T_+=14,\quad T_-=2.
\]
But the sharp \(P\)-expansion is referenced, not proved in the supplied files. Assuming
\[
P(g_a)=2\pi^2a^4+o(a^4),
\]
the exact defect is
\[
\boxed{\mathcal E(g_a)=\frac{4P(g_a)+L_s(g_a)}{R(g_a)}.}
\]
Consequently,
\[
L_s=o(a^4)
\Longrightarrow
\mathcal E(g_a)=\frac{a^4}{6}+o(a^4).
\]
If instead \(L_s/a^4\to\ell_s\), then
\[
\mathcal E(g_a)
=\left(\frac16+\frac{\ell_s}{48\pi^2}\right)a^4+o(a^4).
\]
If merely \(L_s=O(a^4)\), the assumed \(P\)-expansion gives \(\mathcal E=\Theta(a^4)\), but not coefficient \(1/6\).

An \(O(1)\) scalar mismatch on an \(O(a^4)\)-volume core makes a nonzero variance coefficient plausible. That is not a proof that \(L_s=o(a^4)\) fails: the adapted corrections could affect it. The precise remaining object is the leading scalar-curvature profile of the adapted metric, including its mean shift and cutoff contributions.

## 7. Classical content, package deductions, and required sources

The supplied paper directly supports the Chern–Weil normalization, the classical self-dual Gauss–Bonnet expression
\[
2\chi-3\tau=\frac1{8\pi^2}\int\left(\frac{s^2}{12}-|\operatorname{Ric}^{\circ}|^2\right),
\]
the hyperbolic-ansatz positive-scalar classes, and the nonnegative-Ricci-operator obstruction. Yamabe existence, the Weitzenböck vanishing, and Einstein topological obstructions are classical mechanisms.

Identity 71.1 and the wall are **reported as corpus-inherited**, but their precise prior corpus statements cannot be checked without the absent passages. The equality/attainment interpretation, exact attained \(\alpha=1\) examples, reservoir bound, self-covering extension, and identity (*) are deductions or combinations not exhibited as such in the supplied classical paper. This establishes novelty relative to the supplied text—not historical priority.

The useful `knowledge_request`s are:

- **Corpus:** lines 1520–1543, the exact conformal-comparison argument, and line 5562, especially its handle dependence.
- **Classical geometric scope:** Ishida–LeBrun’s ASD-psc connected-sum passage; Pedersen–Poon’s precise classification hypotheses; the relevant nonsimply-connected Donaldson theorem.
- **Precedence:** prior treatments of
  \[
  4-\frac{(\int s)^2}{V\int|\operatorname{Ric}|^2},
  \]
  its unit-wall equality class, and long-circle/self-covering connected-sum dilution.
- **Remaining geometry:** conformally flat structures on \(T^4\), negative-Yamabe ASD classes on K3, without presupposing their existence or openness.
- **EH rate:** the actual adapted metric expansion and its scalar variance through order \(a^4\).
- **Compactness:** a theorem controlling the same normalized \(\mathcal E\)-small sequence, including curvature-concentration balls.

The verified conclusions are therefore strong but sharply delimited: the unit wall and its attaining geometry are exact, the reservoir upper bound is rigorous, bounded-curvature total collapse cannot produce \(\alpha=0\), and the coefficient \(a^4/6\), unrestricted Yamabe quotient, reverse handle threshold, and full \(\alpha\)-sequence decomposition remain unproved by these materials.