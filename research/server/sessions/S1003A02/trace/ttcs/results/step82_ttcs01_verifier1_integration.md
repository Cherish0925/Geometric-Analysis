# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 82,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step82_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step82_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the final section §24 (and §24.0 L1/L2, §23.6) of Sessions/S1003A02/workspace/notes/theorem_package_v1.md as a research geometer checking every statement against (a) the earlier package sections it cites (§§1, 3.3-3.7, 13-17, 20, 21.10-21.11, 22) and (b) the original problem statements in five_research_problems.tex §§1-3 (Problems 1-3: Einstein existence on X#k CPbar^2 for 1<=k<A/3; exact P_*; a smooth non-Bach-flat global P-minimizer). For each statement in §24 decide whether (i) it is correctly tagged [I]/[P]/[C]/[O], (ii) its quantifiers match the cited source (which X, which k, which metrics, which hypotheses), (iii) the derivation is correct. Specific items to check with care: the L1 equivalence Einstein <=> alpha=0 attained <=> P_*=0 attained on X#kCPbar^2 and what Seiberg-Witten/Yamabe input it needs (b+ conditions); the L2 bound D(g) >= p/(p+3T_+/4) from C_+ = T_+ + p and the derived band bound alpha >= 4(3k-A)/(3k+5A) for A/3<=k<=A; the regime summary in 24.2(4); the Problem-3 discussion: whether k>=A/3 blow-ups really satisfy both hypotheses of Prop. nonbach unconditionally, whether the real-hyperbolic blow-up scalar-flat exclusion argument (no PSC on connected sums with aspherical 4-manifolds + Cheeger-Gromoll) is sound, and whether Theorem H (conditional non-attainment) is quoted correctly; the k=1 conditional dichotomy 'negative Problem 1 => positive Problem 3' from Theorem 54.A including whether A>=9 for ball quotients is right and what configurations remain; the 'three ends' paragraph (does p->0 force approach to the Einstein end of p=q^2(1-delta)^2+L, is q bounded below, and are the aligned/cscK ends correctly described as obstacles to coercive estimates rather than escape routes); the statement that 1/3 is simultaneously the zero of LeBrun's P bound and the sign change of the fixed-Kahler Weyl deficit, and its explanation by KE saturation; and the claim that every known attained alpha-minimizer is Bach-flat. Report concrete corrections with exact replacement wording, any statement that is false or overstated, and any important inherited or proved result from the package that §24 omits but that belongs in a complete statement of Problems 1-3. Do not invent literature; if a claim needs an outside source (e.g. no-PSC for connected sums with aspherical manifolds, LeBrun's Yamabe computation for b+=1), name the exact knowledge_request needed.

## Integrated Scientific Memo

# Scientific verification memo: §24 and §23.6

The distinction between \(P_*\), \(\alpha\), Einstein existence, and attainment is sound. The principal corrections concern the explanation of the \(1/3\) threshold, the \(k=1\) attainment claim, the scope of the balanced-family theorem, and several conclusions stronger than their cited sources. In particular, **KE metrics do not saturate the combined LeBrun estimate giving \(P\ge8\pi^2(k-A/3)\)**.

Below, “proved” means proved within the supplied package, with its recorded hypotheses. The external theorems themselves are not reproduced here; the \(b^+=1\) and no-positive-scalar-curvature inputs require the precise source requests listed at the end.

## 1. Definitions and the two elementary links

### Opening conventions: correct the curvature norm

The original problem defines \(I_R\) using the curvature-operator norm and proves
\[
I_R(M)=8\pi^2\chi(M)+P_*(M).
\]
The package also uses the full tensor norm, for which
\[
\int|\mathrm{Rm}|_{\mathrm{tensor}}^2=32\pi^2\chi+4P.
\]
These are compatible but must not be conflated.

**Replace the parenthesis in the opening paragraph by:**

> The original optimal-curvature problem uses the curvature-operator norm:
> \[
> I_R(M)=\inf_g\int|\mathrm{Rm}_{\mathrm{op}}|^2
> =8\pi^2\chi(M)+P_*(M).
> \]
> Equivalently, in the full tensor norm,
> \(\int|\mathrm{Rm}|^2=32\pi^2\chi+4P\).

Use \(p=P/(8\pi^2)\) for a metric value and \(\mathfrak p_*=P_*/(8\pi^2)\) for the infimum, consistently with §1.

### L1: correct, but distinguish the inherited input from the deduction

On any closed connected manifold,
\[
P(g)=0\iff g\text{ is Einstein},
\]
by the contracted Bianchi identity. For the human functional,
\[
\mathscr D(g)=0\iff g\text{ is Einstein with }\lambda\ne0.
\]
Ricci-flat metrics instead have \(\mathscr D=4\). Thus the equivalence in L1 needs exclusion of Ricci-flat metrics; negative Yamabe invariant supplies this and additionally excludes all nonnegative constant-scalar metrics.

The exact Yamabe value is stronger than necessary for L1. Its negativity suffices. The package’s chamber-independent sign-family arguments explicitly cover \(b^+\ge2\); they do **not**, without the separate chamber argument, establish the stated all-\(X\) quantifier for \(b^+=1\).

**Replacement:**

> **L1 [I]+[P].** Adopt LeBrun’s Yamabe theorem, with its \(b^+=1\) chamber treatment where needed,
> \[
> \mathcal Y(X\#k\overline{\mathbb{CP}}^2)
> =-4\pi\sqrt{2A}<0.
> \]
> This excludes scalar-flat metrics and forces every Einstein metric to have negative Einstein constant. Consequently
> \[
> M\text{ admits an Einstein metric}
> \iff P_*(M)=0\text{ and the infimum is attained}
> \iff \alpha(M)=0\text{ and the infimum is attained}.
> \]
> The Yamabe theorem is inherited; the equivalence is an elementary deduction. The \(b^+=1\) application must cite the chamber-inclusive theorem, rather than only §§3.6–3.7.

The corresponding statements in §24.3 about \(k\ge A/3\) are mathematically correct **once this inherited all-\(X\) theorem and the classical nonexistence theorem are supplied**. They need no extra hypothesis on minimizing sequences.

### L2: the algebra and band constant are correct

Write \(S=\int s^2\). From
\[
C_+=T_++p,\qquad
C_+=\frac{1}{2\pi^2}\int|W^+|^2+\frac{S}{96\pi^2},
\]
one obtains
\[
S\le96\pi^2(T_++p),\qquad
R=P+\frac S4\le8\pi^2(4p+3T_+).
\]
Hence
\[
\mathscr D=\frac{4P+L_s}{R}
\ge\frac{p}{p+\frac34T_+}.
\]
For \(T_+>0\), the right side is increasing in \(p\), so the infimum comparison follows.

Substituting \(\mathfrak p_*\ge k-A/3\) and \(T_+=A-k\) gives
\[
\frac{k-A/3}{k-A/3+\frac34(A-k)}
=\frac{4(3k-A)}{3k+5A}.
\]
This proves the displayed bound for \(A/3\le k<A\). At \(k=A\), \(T_+=0\) and the inherited lower bound gives \(p>0\), so the same calculation yields \(\mathscr D\ge1\); the universal ceiling yields \(\alpha=1\).

**Tag correction:** the chiral comparison is [P], requiring no monopoles. Its application with LeBrun’s lower bound is [I]+[P]. The endpoint \(k=A\) should be explained separately, rather than included under a heading assuming \(T_+>0\).

An important omitted consequence is:
\[
\boxed{
P_*(M)=0\iff\alpha(M)=0,\qquad
P_*(M)>0\iff\alpha(M)>0
\quad(1\le k<A).
}
\]
Indeed, combine L2 with the supply-dependent upper comparison
\[
\alpha\le\frac{4\mathfrak p_*}{A+\mathfrak p_*}.
\]
This is an equivalence of zero versus positive values, not equality of the functionals or their minimizing sequences.

## 2. Problem 1: correct conclusions and scope repairs

### Status paragraph and N1

The classical \(k\ge A/3\) exclusion is correctly tagged [I]. The N1 window is also correctly inherited, **only on the metric-wise actual-supply class specified in the original problem**.

The original problem gives more than nonexistence. If
\[
j_0=\varepsilon-(1/3-k/A)_+>0,
\]
then
\[
\mathcal J\ge j_0,\qquad
P\ge\frac{8\pi^2j_0}{4-j_0}A,\qquad
\alpha\ge j_0.
\]
These quantitative consequences belong in §24. They contradict the later blanket statement that no positive lower bound is known anywhere in \(0<k<A/3\).

The hypersurface examples and their \(A_d\ge2/\varepsilon\) condition match the original problem.

### §24.1(1): remove the unnecessary ADE qualification

Theorem 69.KE already includes canonical-model/ADE localization.

**Replacement:**

> For every minimal general-type \(X\) and \(1\le k<A/3\),
> \[
> 0\le\alpha(M)<\frac{4k}{A+k}<1
> \]
> by Theorem 69.KE, including its canonical-model and Kronheimer localization.

### §24.1(2): “No topology-only obstruction can work” is false

Strict sub-\(8\pi^2k\) constructions refute a particular tariff, not every topology-based Einstein obstruction.

**Replacement:**

> **The unit per-class tariff is false [P].** Corollary 59.KE gives \(P_*<8\pi^2k\) for every fixed minimal general-type \(X\) and every fixed \(k\ge1\). Thus an unrestricted inequality \(P(g)\ge8\pi^2k\) cannot hold. The explicit enclosure \(P_{\rm cell}/(8\pi^2)\in[0.99566273275,0.99566273278]\) concerns CH-collared cells, not arbitrary hosts. Other topological, gauge-theoretic, or entropy obstructions are not excluded.

Likewise, the concluding reference to “\(C_+\ge A\) that would suffice” needs clarification:
\[
C_+\ge A\iff p\ge k.
\]
It would certainly imply nonexistence, but **it is already false for unrestricted metrics** by 59.KE. It is not an open target.

> The fixed-complex Kähler inequality \(C_+\ge A\) does not extend to arbitrary metrics. Nonexistence requires \(C_+>A-k\) at each metric; a positive gap requires uniform separation from \(A-k\).

This also corrects the obsolete open target in §20.7.

### §24.1(3): separate Chern classes from individual exceptional classes

The twist identity applies to an almost-complex Chern class \(a=c_1(J)\), not directly to \(E_i\). At an Einstein metric the stronger exact statement is available:
\[
\mathsf H^-(t_J^-)=2\pi h_a^-.
\]

**Replacement:**

> For any realizable best-sign class \(a\) and any orthogonal \(J\) with \(c_1(J)=a\), an Einstein metric satisfies
> \[
> \mathsf H^-(t_J^-)=2\pi h_a^-,
> \qquad
> \|\mathsf H^-(t_J^-)\|_2=2\pi|a^-|.
> \]
> Separately, \(E_i^2=-1\) implies
> \(|E_i^-|^2=1+|E_i^+|^2\ge1\).
> The latter does not identify \(E_i\) as an almost-complex Chern class.

### §24.1(4): absorption does not prove nonattainment

The topology and comparison of Corollary 52.8 are correctly reported. A nonzero-scale Einstein orbifold, with the recorded vanishing scalar-variance gluing error, gives \(\alpha(M)=0\). It does **not** exclude an unrelated smooth Einstein metric on \(M\).

**Replace “would give \(\alpha=0\) without an Einstein metric on \(M\)” by:**

> would give \(\alpha(M)=0\) by ALE resolution, without itself supplying a smooth Einstein metric on \(M\). Nonattainment would require a separate exclusion of all such metrics.

The “necessarily non-Kähler” assertion should remain confined to the absorption patterns and orbifold gauge hypotheses established in §13.

### §24.1(5): entropy comparison

The real-hyperbolic nonexistence conclusion for every \(k\ge1\) follows correctly from §3.3. The \(64/81\) comparison, however, is for **complex-hyperbolic ball-quotient hosts with the stated Einstein normalization**, not all general-type \(X\).

## 3. Problem 2: exact values, regimes, and capacity

### §24.2(1): strict upper bound is correct; the local formula needs hypotheses

59.KE proves strictness for every fixed \(X,k\), not a topology-uniform saving constant.

The first-order law of Theorem F is valid on arbitrary smooth backgrounds. The eigenvalue-only second-order expression needs local \(P\)-criticality, the pointwise Einstein condition used by §20.1, an eigenvector, and optimized corrector.

**Replacement:**

> For every smooth bulk, Theorem F gives
> \[
> \frac{P(\widetilde g_{x_0})-P(g)}{8\pi^2}
> =1-x_0R_p^+(\zeta,\zeta)+O(x_0^{6/5}).
> \]
> If the bulk is \(P\)-critical throughout the insertion support, \(\operatorname{Ric}^\circ_p=0\), and \(\zeta\) is an \(R_p^+\)-eigenvector, optimization over the allowed degree-zero corrector gives
> \[
> 1-x_0\mu_1+\frac{\Phi_{\rm opt}}2x_0^2\log(1/x_0)+O(x_0^2),
> \]
> \[
> \Phi_{\rm opt}
> =-\frac12\mu_1(\mu_1-\mu_2-\mu_3)
> -\frac12(\mu_2-\mu_3)^2.
> \]
> Without these hypotheses the coefficient is
> \(\Phi(\mathrm{Rm}_p,\zeta,K)\), not the displayed eigenvalue formula.

### §24.2(2): fixed-complex Kähler infimum

Theorem \(K_\infty\), including successive and infinitely near blow-ups, correctly gives
\[
\inf_{\mathrm{Kähler\ for}\ J}P=8\pi^2k,
\]
not attained for \(k>0\).

**Replace the final sentence by:**

> Every metric with \(P<8\pi^2k\), and hence any smooth unrestricted minimizer if one exists, is non-Kähler for the prescribed blow-up complex structure \(J\). The theorem neither proves unrestricted attainment nor excludes Kählerness for an unexamined different complex structure.

### §24.2(3): balanced-family quantifiers are overstated

The numerical constant \(C_c\) is proved for the specific balance
\[
k=8n,\qquad \ell=7n,\qquad Q=36n,
\]
on the preliminary deep cover and subsequent covers satisfying the packing condition. It is not stated for arbitrary \(k_j,\ell_j\) merely because \(h_j\to0\).

**Replacement:**

> On the ball-quotient cover families of Theorem 69.B, with
> \[
> M=X_m\#8n\overline{\mathbb{CP}}^2\#7n(S^1\times S^3),
> \quad h=36n/A_m,
> \]
> and the stated preliminary-cover and packing hypotheses,
> \[
> \alpha/h\le C_c/(1+C_ch/4),
> \qquad C_c=3.99614465135\ldots.
> \]
> This refutes the project’s standard-leading-coefficient expectation \(4\) on these families. The inherited linear lower bound applies under its original balanced-family hypotheses.

### §24.2(4): regime summary is correct; repair the exact ratio formula

For the stated supply manifolds the three regime bounds are correct:
\[
h\ge1:\ \alpha=1;
\]
\[
1/3\le h<1:\quad
\frac{4(3h-1)}{3h+5}\le\alpha\le1;
\]
\[
0<h<1/3:\quad
0\le\alpha<\frac{4h}{1+h}.
\]

But the all-class formula must retain the truncation in §1:
\[
\boxed{
\alpha
=1-6\max\left\{0,\sup_{[g]:Y([g])\ne0}
\frac{8\pi^2\chi-\mathcal W([g])}
{P(\widehat g)+Y([g])^2/4}\right\}.
}
\]
Dropping \(\max\{0,\cdot\}\) is especially wrong in the unit-wall regime.

The band equivalence
\[
\alpha<1\iff
\inf_g\int|W_g^+|^2<2\pi^2(A-k)
\]
is correct here because all conformal classes have negative Yamabe constant.

### §24.2(5): a single capacity does not decide both questions

Define capacity for a specified manifold,
\[
\Theta_*(M)=\sup_{\widehat g}\frac{2\kappa(\widehat g)}A.
\]
It is not known to depend only on \(h\).

**Replacement:**

> The band question is determined by
> \[
> \alpha(M)<1\iff\Theta_*(M)>(3h-1)/2.
> \]
> Open-range positivity is instead a joint realizability problem for \((\kappa,\upsilon)\), since
> \[
> p=k-\frac43\kappa+\frac13\upsilon.
> \]
> A capacity upper bound can imply positivity under additional control, but the scalar supremum \(\Theta_*\) alone does not encode separation from the Einstein-ratio end.

### §24.2(6) and open list

The joint-set support formula is correctly inherited. Distinct \(P\)- and \(\alpha\)-minimizing classes are a legitimate consequence of their different objectives.

The general exact-\(P_*\) problem remains open. Add that **at the boundary \(k=A/3\), Einstein nonexistence does not establish \(P_*>0\)**: the classical lower bound is zero.

Theorem H’s conditional values are quoted correctly. Its \(\alpha\)-nonattainment applies only to \(k<2\chi(Y)\); the endpoint \(k=2\chi(Y)\) is an unresolved attainment problem at \(\alpha=1\).

## 4. Problem 3 and the \(k=1\) dichotomy

### Proposition nonbach is correct

At a smooth global \(P\)-minimizer,
\[
DP=0.
\]
If it is Bach-flat, then \(D\mathcal W=0\), so the identity
\(P=2\mathcal W+S/12-16\pi^2\chi\) gives \(DS=0\). Tracing the scalar-square gradient gives \(\Delta s=0\); hence
\[
s\,\operatorname{Ric}^\circ=0.
\]
Thus it is scalar-flat or Einstein. The reduction is correctly inherited.

Problem 3 is **existential over all closed four-manifolds**. These blow-up families are candidate sources, not the original problem’s entire quantifier.

### “Where exclusions hold unconditionally”

For \(k\ge A/3\), both exclusions hold with the classical all-\(X\), chamber-inclusive inputs. The heading is inappropriate for the real-hyperbolic bullet, whose scalar-flat exclusion is still source-dependent.

The smooth-bubble rank statement is cited in §15 for non-fake-plane ball quotients. Its numerical budget can be extended, using the displayed proof, to \(b^+\ge2\) general-type hosts under case-(I), trivial-group, lower-semicontinuity, PSC-cap/decay hypotheses:
\[
\sum_b[4(e_b-1)+4b_1(\widehat N_b)+b_2(\widehat N_b)]<k.
\]
This follows by eliminating \(b^+\) with SW first, then applying the nonnegative charge bound. However, identifying the bubbles’ homology image specifically with the exceptional span uses the ball-quotient degree-one argument.

**Safe replacement:**

> For non-fake-plane ball quotients, the hypotheses of §15 imply that fewer than \(k\) exceptional ranks can escape into smooth bubbles. For more general \(b^+\ge2\) hosts, the same charge/SW argument bounds total smooth-bubble \(b_2\), but the exceptional-span identification requires additional topology.

### Real-hyperbolic scalar-flat exclusion: sound chain, missing inputs

The required chain is:
\[
\text{no PSC}
\Longrightarrow
\text{every scalar-flat metric is Ricci-flat}
\Longrightarrow
\pi_1\text{ virtually abelian}.
\]
The first implication uses the scalar-flat deformation theorem, commonly attributed to Bourguignon, and is not supplied by Cheeger–Gromoll alone. The second uses the compact nonnegative-Ricci structure theorem. A cocompact real-hyperbolic lattice is not virtually abelian.

Thus the argument is sound **provided a no-PSC theorem covers \(Y\#k\overline{\mathbb{CP}}^2\), including non-spin cases**. Under Theorem H’s stronger negative-Yamabe identity, scalar-flat exclusion is immediate.

**Replace the final concentration sentence by:**

> Under \(\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}\), Theorem H gives \(P_*=8\pi^2k\), not attained, so these manifolds are not Problem-3 examples. Burns sequences approach this value. The theorem does not show that every minimizing sequence concentrates into Burns bubbles; for arbitrary sequences it establishes asymptotic half-conformal flatness and Yamabe extremality.

### \(A\ge9\) is correct; the attainment statement omits exotic caps

For a ball quotient,
\[
A=3c_2,\qquad
A+c_2=12\chi(\mathcal O_X),
\]
so
\[
A=9\chi(\mathcal O_X)\ge9.
\]
The non-fake-plane condition supplies \(b^+\ge3\); fake planes remain outside 54.A even though the strict upper construction applies to them.

Theorem 54.A gives a smooth minimizer on \(V\), with
\[
M\cong V\#\Sigma,\qquad V\approx M,
\]
where \(\Sigma\) is a homotopy sphere. It gives a minimizer on **\(M\)** only after excluding exotic homotopy-sphere caps.

**Replacement for the dichotomy paragraph:**

> Under case (I), trivial local groups, and
> \(\mathrm H_{\rm sm},\mathrm H_{\rm lsc},\mathrm H_{\rm dec},
> \mathrm H_{\rm eq},\mathrm H_{\rm rem}\),
> Theorem 54.A produces a smooth constant-negative-scalar global \(P\)-minimizer on \(V\), where \(M\cong V\#\Sigma\) and \(V\) is homeomorphic to \(M\). It is Einstein or non-Bach-flat. If all bubble caps are diffeomorphic to \(S^4\), then there are no bubbles, \(V\cong M\), and \(P_*(M)\) is attained. Under this additional condition, a negative answer to Problem 1 on \(M\) gives a positive answer to Problem 3.
> Without it, nonexistence on \(M\) does not exclude an Einstein metric on the different smooth manifold \(V\).

The remaining geometries must include:
- collapse, including finite isotropy and classes split across interfaces;
- nontrivial-group orbifold configurations;
- exotic homotopy-sphere bubbles.

For orbifold configurations, use the **§17 repairs**, not the unrepaired §16 classification: Prop. 55.3 needs simply connected regions, the fine trichotomy was weakened, and the coarse charge budget is conditional on the stated \(L\)-space splitting input. The threshold \(C_+(V)+w\ge A\) is an open exclusion target, not an established reduction covering every configuration.

### The \(\alpha\)-attainment list

The listed zero and unit-wall statements are correct. “Every known attained minimizer” is an unsupported literature-exhaustiveness claim.

**Replacement:**

> Every attained \(\alpha\)-minimizer explicitly identified in this package is Bach-flat: either Einstein with nonzero Einstein constant, or half-conformally-flat with constant nonzero scalar curvature. The supplied materials contain no attained example with \(0<\alpha<1\), and no non-Bach-flat global \(\mathscr D\)-minimizer.

## 5. Common mechanism: substantial corrections

### The \(1/3\) coincidence is real; its proposed KE explanation is false

At a KE metric on the minimal model,
\[
|W^+|^2=s^2/24,\qquad S=32\pi^2A.
\]
Therefore
\[
\int(s^2/24+2|W^+|^2)=S/8=4\pi^2A,
\]
not \(8\pi^2A/3\). This agrees with §3.6’s “contact at \(\rho=3/2\), not at KE.”

The two thresholds have different derivations:

- LeBrun gives \(C_+\ge2A/3\), hence
  \[
  p=C_+-(A-k)\ge k-A/3.
  \]
- Fixed-complex Kähler geometry gives
  \[
  I_+\ge4\pi^2A/3,\qquad
  d=4\pi^2(A-k)-2I_+
  \le4\pi^2(A/3-k).
  \]

KE saturates the scalar and stronger monopole estimates on the minimal model; Kähler recovery approaches the second frontier. It does **not** saturate the derived \(C_+\ge2A/3\) estimate. The latter’s formal equality profile is the almost-Kähler \(\theta=1/3,\ s^*=s/2\) profile of §3.7, not a proved closed equality metric on these blow-ups.

**Replacement:**

> The value \(h=1/3\) is both the zero of the classical LeBrun \(P\)-bound and the sign frontier of the prescribed-complex Kähler Weyl-deficit supremum. These arise respectively from \(C_+\ge2A/3\) and \(I_+\ge4\pi^2A/3\). KE geometry saturates the minimal-model scalar estimate underlying the Kähler frontier, but not the combined estimate giving the \(P\)-bound. N1’s differential actual-field input already advances positive separation below \(1/3\) on its supply class; certified non-Kähler cells advance the \(\alpha<1\) frontier above \(1/3\).

For \(k>0\), the Kähler inequality is strict at every individual smooth metric; “sign change” refers to the supremal/recovery frontier.

### Yamabe excess: the claimed monotonicity is reversed

At fixed \(\kappa\), set
\[
F_\kappa(\upsilon)=
\frac{4(k-\frac43\kappa+\frac13\upsilon)}
{A+k-\frac43\kappa+\frac43\upsilon}.
\]
Then
\[
F_\kappa'(\upsilon)
=\frac{4(A-3k+4\kappa)}
{3(A+k-\frac43\kappa+\frac43\upsilon)^2}.
\]
Moreover \(F_\kappa<1\iff A-3k+4\kappa>0\). Thus on the subunit region, increasing \(\upsilon\) **raises** the ratio toward \(1\).

**Replacement:**

> At fixed \(p\), increasing the denominator would lower the ratio, but \(p\) and \(\upsilon\) are not independent. At fixed Weyl capacity, increasing Yamabe excess raises \(p\) and raises the subunit \(\alpha\)-ratio toward \(1\). Different minimizing classes remain possible because the two objectives weight the joint data differently.

Globally the supply-coordinate formula must be capped:
\[
\alpha=\min\left\{1,\inf_{[g]}
\frac{4p(\widehat g)}{A+p(\widehat g)+\upsilon([g])}\right\},
\]
with the uncapped formula used when \(\alpha<1\).

### Local models

The Burns/EH invariant relation is correctly inherited from §20.6, but:
- EH’s quantitative price is a result on the specified weighted gluing neighborhoods, not arbitrary degeneration sequences.
- §17 proves absence of the linear-tail logarithm at Wahl points. It does **not** prove “interaction only at \(O(\lambda^4)\).”

**Replacement:**

> At Wahl points the linear-tail interaction has no logarithmic term. The proposed \(\lambda^4\) polarizability form remains uncomputed; §17’s established smoothing upper error is \(O(\lambda^2)\).

### Three ends: correct implication, conditional geometry

For a best-sign class,
\[
q^2=|a^-|^2\ge k.
\]
This lower bound follows algebraically: the sign average gives
\[
\max_\epsilon|a_\epsilon^+|^2
\ge |K^+|^2+\sum|E_i^+|^2
=A+|K^-|^2+\sum|E_i^+|^2.
\]
Subtract \(a_\epsilon^2=A-k\). The availability of actual fields or a \(J\) realizing the chosen class is a separate issue.

Thus
\[
p\to0\Longrightarrow L\to0,\qquad
|1-\delta|\le\sqrt{p/k}\to0.
\]
No upper bound on \(q\) is needed. Conversely, \(\delta\to1,L\to0\) alone need not give \(p\to0\) if \(q\) diverges.

**Replacement:**

> Any \(p\to0\) sequence approaches the Einstein end in the integrated ledger sense. This is a necessary algebraic description, not a compactness or nonexistence theorem. An aligned sequence can participate only by also approaching \(\delta=1\); the cscK end itself has \(p=q^2\ge k\).
> Under the bounded-extension hypothesis, 66.R characterizes the non-Einstein aligned equality structure. Its existence on the target blow-ups is not established. Such structures would obstruct a universal \(L\ge c\delta\) estimate. Product saddles prove failure of uniform Kähler-end coercivity across products of curves, not a zero-gap escape construction on \(X\#k\overline{\mathbb{CP}}^2\).

A positivity proof need not exclude every aligned structure; it must prevent approach to \(p=0\). “Must exclude the aligned end” is too strong.

### Degeneration and the final open centre

Replace “every known minimizing sequence … degenerates” by a statement about the particular nonattained constructions and quoted limiting theorems. Constant sequences at known attained minima are immediate counterexamples to the literal wording.

Replace the blanket open-centre assertion by:

> The complete \(0<k<A/3\) problem remains unresolved. N1 already gives positive \(P_*\) and \(\alpha\) on its actual-supply window near \(1/3\). For the remaining low-ratio cases, no general positive-gap theorem or fixed-topology zero-gap construction is supplied here.

Also, a “family with \(\alpha\to0\)” is not itself unknown if topology varies: whenever admissible examples have \(k/A\to0\), 69.KE already gives \(\alpha\to0\). The genuinely open object is **zero infimum on a fixed blow-up**, or matching rates below the known upper scale.

Diffuse multiclass geometry is a proposed upper mechanism, not a necessary form of every possible solution.

## 6. §23.6 and important omissions

The [N], undecided tag for the order-8 test is appropriate, although [N] should be added to §24’s tag legend if used nearby. Residuals \(0.13\)–\(0.15\), decreasing iterations, and rank \(91/119\) establish neither solvability nor obstruction. Likewise, 80.R is numerical evidence for order-6 solvability, not an exact or interval-certified formal solution. None of these tests supplies a theorem for Problems 1–3.

The following additions materially complete §24:

1. **N1’s quantitative positive-gap window** and the zero/positive equivalence of \(P_*\) and \(\alpha\) established above.
2. **Known independent optima** from the original Problem 2:
   \[
   \inf R=8\pi^2(A+k),\qquad \inf S=32\pi^2A.
   \]
   Their infima cannot be subtracted to compute \(P_*\).
3. **Zero-\(P_*\) structure, §20.5 [P*]:** Anderson’s selected sequence yields compact Einstein orbifold, componentwise complete Einstein domains with exterior collapse, or total collapse. This has not been transferred to arbitrary normalized \(\alpha\)-small sequences.
4. **Near-subunit necessary conditions**, under their sign-family hypotheses: Theorems N, K, Y and 63.T force torsion, Weyl departure, Yamabe excess, and twist. These are constraints, not tariff theorems. The conditional 62.B quadratic lower law must remain [C].
5. **Attainment beyond 54.A:** 53.D–E give smooth negative-Yamabe bulk minimizers under the Anderson ledger; 56.A gives conditional orbifold-category attainment. Neither alone proves attainment on the original smooth \(M\).
6. **Compact replacement:** smooth bubble convergence of an actual \(P\)-minimizing sequence implies local \(P\)-minimality and criticality of the bubble. The remaining analytical input is convergence/decay, not merely cancellation of the rescaled perturbation coefficient.

## 7. Exact external knowledge requests

- **LeBrun, chamber-inclusive general-type results:** obtain the theorem numbers, pages, and proofs covering \(b^+=1\) for the Yamabe computation, all-metric scalar-negative-part budget, classical \(P\)-bound, and \(k\ge A/3\) Einstein exclusion, for every \(k\).
- **No PSC on real-hyperbolic connected sums:** obtain a theorem proving that every closed oriented real-hyperbolic four-manifold \(Y\) has \(Y\#k\overline{\mathbb{CP}}^2\) without PSC, explicitly covering non-spin manifolds and specifying whether the degree-one map is sufficient.
- **Scalar-flat deformation and compact Ricci structure:** obtain the exact scalar-flat-non-Ricci-flat \(\Rightarrow\) PSC theorem and the compact nonnegative-Ricci theorem giving virtually abelian \(\pi_1\).
- **One-sided PSC SW vanishing:** register the exact neck-stretching citation for Lemma 54.3 when \(b^+(Z)\ge1\), \(Z\) admits PSC, and \(b^+(R)=0\).
- Only if Kähler exclusion is to extend beyond the prescribed \(J\): obtain the precise smooth-topological/minimal-model theorem controlling all orientation-compatible complex structures on \(M\). Without it, retain the fixed-\(J\) statement.

These repairs preserve the package’s substantive advances while separating established inequalities, conditional limiting structures, and the exact unresolved attainment and existence objects.