# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step71_functional_split_and_unit_wall.md",
    "Sessions/S1003A02/workspace/scripts/step71_functional_split_examples.py",
    "Sessions/S1003A02/workspace/data/step71_functional_split_examples.json",
    "Knowledge/objects/papers/dg-ga-9411001-Self-Dual-Manifolds-with-Positive-Ricci-Curvature--92f685b1b31c--e3fd78dbc8b6/object.md",
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md"
  ]
}
```

## Task

Verify the mathematics of the Step-71 note on the Einstein-defect functional E(g)=inf_{lambda!=0} int|Ric-lambda g|^2/(lambda^2 V) on closed oriented 4-manifolds. Check with full rigor, and correct where needed: (1) Identity 71.1 E-1=(12 int|W^±|^2+L_s-24pi^2 T_±)/R, T_±=2chi±3tau, in LeBrun's conventions (compare the inherited corpus statement at Curvature_Realizability lines 1520-1543 if given in the excerpt) and the JSON example checks. (2) Theorem 71.B: strictness for T_+<0; the equality characterization E=1 iff W^+=0 and s nonzero constant when T_+=0<=T_-; the attainment criterion via Yamabe classes; the positive-scalar Betti classification (b1,b2) in {(0,4),(1,0)} (Weitzenbock with W^+=0, s>0 gives b_+=0). (3) Theorem 71.C: alpha=1 attained on S^1 x S^3/Gamma, S^1 x_phi H^3/Gamma, and #4 CPbar^2 via LeBrun's hyperbolic-ansatz self-dual classes with positive scalar representatives (source lines quoted in the note); non-existence of Einstein metrics on these; the claim that K3 and T^4 have alpha>=1 although Ricci-flat; the ASD constant-scalar formula E=1+9m/(3m+4y). (4) Theorem 71.D, the long-circle reservoir: alpha(N # (S^1 x Y))<=1 for any N and Y spherical space form or hyperbolic 3-manifold, by taking S^1 of length L -> infinity and gluing a rescaled N in a fixed ball. Scrutinize whether all junk terms (R, W^+, L_s including the mean-scalar shift, the neck) are really O(1) uniformly in L, whether scale-invariance is used correctly, and the corollary alpha(X#kCPbar^2#l(S^1xS^3)) <= min(1,4h/(1+h)), =1 iff k+4l>=A. (5) Lemma 71.T and the alpha-readings of 59.C/59.N/59.Z: especially the Gauss-Bonnet argument that E-small sequences normalized at lambda_opt=1 have V<=12pi^2 chi(1+o(1)) and cannot collapse totally with bounded curvature, and the a^4/6 EH alpha-rate on CP^2#CP^2. Also state precisely what is new versus classical (Hitchin-Thorpe, LeBrun-Nayatani-Nitta Gauss-Bonnet form, corpus) as far as the supplied sources allow, and name any knowledge_request needed for precedence. Give a direct scientific memo with corrected statements.

## Output

# Verification memo: Step 71 (functional split, unit wall, attained gaps, long-circle reservoir)

**Summary.**
- The algebra of Identity 71.1, the JSON values, the unit wall (71.B), the ASD formula and the reservoir bound (71.D) all check out.
- Six statements need correction or sharpening:
  1. The "iff" in the 71.D corollary is only an "if".
  2. The "exact quotient" on supply manifolds is exact only on part of each conformal class.
  3. The Gauss–Bonnet exclusion in 71.T covers collapse without bubble balls only.
  4. The EH rate \(a^4/6\) rests on an assumption, \(L_s=o(a^4)\), that is probably false.
  5. The T⁴ attainment question is misstated (conformally flat versus half-flat).
  6. 71.B(e) can be strengthened by a covering argument.
- Two new structural facts emerge. The reservoir mechanism is a self-covering principle, \(\alpha(N\#Z)\le\alpha(Z)\). There is also an exact companion Gauss–Bonnet identity at the Einstein normalisation.

---

## 1. The functional and Identity 71.1

**Closed form of \(\mathcal E\).**
- Expanding gives \(\int|\mathrm{Ric}-\lambda g|^2=R-2\lambda T_s+4\lambda^2V\).
- With \(u=1/\lambda\), the quotient \(Ru^2/V-2T_su/V+4\) is minimised at \(u=T_s/R\). Hence
  - \(\mathcal E=4-T_s^2/(RV)\), and \(\lambda_{\rm opt}=R/T_s\);
  - when \(T_s=0\), \(u=0\) is excluded and the infimum is 4, not attained.
- Writing \(V\int s^2-T_s^2=VL_s\) gives \(\mathcal E=(4P+L_s)/R\).
- This formula holds for **every** metric with \(R>0\), including \(T_s=0\). In that case \(4R=4P+\int s^2=4P+L_s\), which gives 4.
- Scale invariance is correct: the numerator tensor \(\mathrm{Ric}-\lambda g\) is unchanged under \(g\to cg,\ \lambda\to\lambda/c\), and \(\lambda^2V\) is invariant.

**Identity 71.1.**
- In LeBrun's conventions,
  \(8\pi^2T_\pm=2\int(|W|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)\pm2\int(|W^+|^2-|W^-|^2)=\int(4|W^\pm|^2+s^2/12)-P.\)
- So \(\int s^2=96\pi^2T_\pm+12P-48\int|W^\pm|^2\), and \(R=P+\int s^2/4=4P+24\pi^2T_\pm-12\int|W^\pm|^2\). This is exactly the note's formula.
- Then \(\mathcal E-1=(4P+L_s-R)/R\) is the stated identity. It also agrees with Step 59's \(P=\int F_+-16\pi^2\chi-24\pi^2\tau\).
- The corpus lines 1520–1543 were not in the supplied excerpt, so the comparison with the inherited statement could not be made directly. The derivation above is self-contained.

**Companion identity (new; worth recording).**
- Normalise \(|\lambda_{\rm opt}|=1\). This is possible whenever \(T_s\ne0\); the sign of \(T_s\) is scale invariant.
- Then \(R=(4-\mathcal E)V\) and \(\int s^2=L_s+(4-\mathcal E)^2V\).
- Substituting into Gauss–Bonnet gives
\[
48\pi^2\chi=6\!\int|W|^2+L_s+(4-\mathcal E)(1-\mathcal E)\,V .
\]
- Hence \(\mathcal E<1\) forces \(\chi>0\), with \(V\le 48\pi^2\chi/((4-\mathcal E)(1-\mathcal E))\).
- As \(\mathcal E\to0\) this gives \(V\le12\pi^2\chi(1+o(1))\), which is the Lemma 71.T statement, now as an equality with explicit remainder.
- It also re-derives "\(\chi\le0\Rightarrow\alpha\ge1\)", which is already contained in the wall because \(T_{\min}=2\chi-3|\tau|\).

**JSON checks.** All values were recomputed by hand and are correct (S⁴: \(R=96\pi^2\); FS: \(\int|W^+|^2=12\pi^2\); S¹×S³: \(P=6\pi^2L\), \(R=24\pi^2L\); Σ×S²: \(\mathcal E=4\); hyperbolic: \(\chi=3V/4\pi^2\); ASD family). Three points about the script:
- The K3 entry sets both `E_formula` and `E_identity` to 4 by the \(R=0\) branch. The identity, which has \(R\) in the denominator, is therefore not tested there. The entry checks only Gauss–Bonnet and signature.
- Every example is homogeneous with \(L_s=0\), so the \(L_s\) term is never exercised. It is purely algebraic, so this is harmless.
- `four_CPbar2_any_y` and `S1xS3_any_y` are the same substitution \(m=0\). They are one check, not two.

## 2. Theorem 71.B

**(a), (b): correct.**
- If \(R=0\) the metric is Ricci-flat and \(\mathcal E=4\).
- If \(R>0\) and \(T_+<0\), then \(\mathcal E-1\ge24\pi^2|T_+|/R>0\).
- The approximating-sequence sentence should read: \(\mathcal E(g_j)\to1\) iff \((12\int|W^+|^2+L_s+24\pi^2|T_+|)/R_j\to0\). In particular \(R_j\to\infty\), \(\int|W^+|^2=o(R_j)\) and \(L_s=o(R_j)\). Here \(R\) is scale invariant in dimension 4.

**(c): correct.**
- Equality forces \(R>0\), \(W^+=0\) and \(s\equiv c\). The case \(c=0\) gives \(\mathcal E=4\).
- Conversely, \(W^+=0\) with constant \(s\neq0\) gives \(R\ge\int s^2/4>0\) and \(\mathcal E=1\).
- Attainment: \(W^+=0\) is conformally invariant. A constant-\(s\) metric in a class has the sign of \(Y\), since the conformal Laplacian's first eigenvalue is then \(s/6\) with constant eigenfunction. Classes with \(Y=0\) contain only \(s=0\) constant-scalar metrics.
- The attaining set is therefore all constant-scalar metrics in \(W^+=0\) classes with \(Y\neq0\). When \(Y>0\) these may include non-minimising Yamabe metrics, and they all attain.

**(d): correct.** Einstein metrics have \(\mathcal E\in\{0,4\}\).

**(e): correct.**
- The Weitzenböck formula \((d+d^*)^2|_{\Lambda^+}=\nabla^*\nabla-2W^++s/3\) gives \(b_+=0\).
- Then \(4-4b_1-b_-=0\), so \((b_1,b_2)\in\{(0,4),(1,0)\}\).

Two sharpenings:
- *Covering argument (new).* A \(d\)-fold cover inherits \(W^+=0\) and constant \(s>0\), hence \(\mathcal E=1\) and the same dichotomy. Since \(T_+\) is multiplicative and \(\chi(\tilde M)=6d\), the case \((0,4)\) forces \(d=1\); the case \((1,0)\) has \(\chi=0\neq 6d\). So in the \((0,4)\) case \(\pi_1\) has **no proper finite-index subgroup**. This parallels the \(\chi-\tau\) argument in LeBrun–Nayatani–Nitta (LNN), Prop. 1.1.
- Donaldson's diagonalisation holds for arbitrary \(\pi_1\) (Donaldson 1987), so "diagonal" is correct without simple connectivity. Freedman is needed only for the homeomorphism type.

## 3. Theorem 71.C

**C.1 (\(S^1\times S^3/\Gamma\), \(S^1\times_\phi H^3/\Gamma\)): correct.**
- \(\mathbb R\times S^3\) and \(\mathbb R\times H^3\) are conformally flat, so \(W\equiv0\) gives \(\tau=0\). Also \(\chi=0\), \(s=\pm6\) and \(\mathcal E=1\).
- Every mapping torus of a hyperbolic \(Y\) has isometric monodromy up to isotopy by Mostow rigidity. Including this widens the family at no cost.
- Non-existence of Einstein metrics is shorter than citing Hitchin's equality case. For Einstein metrics, \(8\pi^2\chi=\int(|W|^2+s^2/24)\), so \(\chi=0\) forces flatness. Bieberbach then requires \(\pi_1\) to be virtually \(\mathbb Z^4\), and \(\mathbb Z\times\Gamma\) and \(\pi_1(Y)\rtimes\mathbb Z\) are not.

**C.2 (\(\#4\overline{\mathbb{CP}}^2\)): correct, given the source.**
- Topology: \(\chi=6\), \(\tau=-4\), \(T_+=0\).
- The LNN passage ("each of the conformal classes so constructed can be seen to contain a representative of positive scalar curvature") supports \(Y>0\).
- LNN's display \((2\chi-3\tau)=\tfrac1{8\pi^2}\int(s^2/12-|\mathrm{Ric}^\circ|^2)\) for self-dual metrics is exactly Identity 71.1 at \(W^\mp=0\). In the reversed orientation, 4CP² has \(2\chi-3\tau=0\), so \(P=\int s^2/12\), \(R=4P\) and \(\mathcal E=1\). The attainment is therefore a direct reading of LNN's Gauss–Bonnet form.
- The diffeomorphism type rests on LeBrun 1991 (the source's "\(M\approx n\mathbf{CP}_2\)") and on Pedersen–Poon for \(n\le4\) (LNN Prop. 1.1).
- The Theorem 1.3 consequence is correct. The attaining metrics are self-dual (in the CP² orientation) with \(s>0\), on a manifold that is neither \(n\mathbf{CP}_2\) with \(n\le3\) nor covered by \(\mathbb R\times S^3\).
- Non-existence of Einstein metrics: \(\lambda\neq0\) contradicts \(\mathcal E\ge1\). Ricci-flat metrics are excluded by Hitchin's equality case, because \(\chi=6\notin\{0,12,24\}\).
- The Ishida–LeBrun line 400 was **not** among the supplied files and was not checked.

**ASD formula: verified.**
- Gauss–Bonnet and signature give \(P=8\pi^2m+Y^2/12\) and \(R=P+Y^2/4\), so \(\mathcal E=4(3m+y)/(3m+4y)=1+9m/(3m+4y)\).
- The S⁴ value is \(y=12\) (\(Y^2=384\pi^2\)) and the \(\overline{\mathbb{CP}}^2\) value is \(y=9\) (\(Y^2=288\pi^2\)).
- Three points to add:
  - \(Y^2\) must mean \(\int s^2\) of the chosen constant-\(s\) metric. This equals \(Y^2\) only at a Yamabe minimiser.
  - The formula applies on the admissible set \(3m+y\ge0\) (\(P\ge0\)), with \(3m+4y>0\) automatic there for \(y>0\).
  - For \(\ell>0\), the existence of the ASD classes rests on the unverified Ishida–LeBrun passage.

**C.3 (Ricci-flat).**
- \(T_\pm=\int|W^\pm|^2/2\pi^2\) is correct. So K3, Enriques and flat manifolds have \(T_{\min}=0\) and \(\alpha\ge1\), and Ricci-flat metrics are the global maxima \(\mathcal E=4\).
- For **K3**, a W⁺=0 class containing a Kähler metric is scalar-flat Kähler, so \(Y=0\). Attainment would need a non-Kähler ASD class with \(Y<0\). Nothing supplied decides this.
- For **T⁴** the note mixes two conditions. Attainment needs a *half*-flat class with \(Y<0\), since \(Y>0\) is excluded by Schoen–Yau/Gromov–Lawson. "Conformally flat classes are believed flat" addresses only the fully flat subcase. The relevant literature is on conformally flat manifolds with nilpotent holonomy (Goldman) plus whatever is known about ASD structures on T⁴.

**C.4 (\(S^2\times T^2\)).**
- The product value \(\mathcal E=2\) is checked: Ric \(=(1,1,0,0)\), \(P=V\), \(R=2V\).
- The \(Y>0\) half-flat case is excluded since \(b_\pm=1\).
- The value of \(\alpha\) in \([1,2]\) is unresolved.

## 4. Theorem 71.D: verified, with an exact rate and a generalisation

**Direct proof without the identity.**
- Let the glued region \(\Omega\) (fixed ball, neck and rescaled \(N\)) be literally isometric for all \(L\) larger than a fixed size. Then \(R_\Omega\), \(V_\Omega\), \(T_\Omega=\int_\Omega s\), \(\int_\Omega s^2\) and \(\int_\Omega|W^\pm|^2\) are **constants**.
- No scale invariance is needed, and \(V_\Omega\) and \(T_\Omega\) are not scale invariant anyway. The note's list of "scale-invariant" quantities omits the two that \(L_s\) actually uses.
- With \(x=L\,\mathrm{vol}(Y)-|B|\):
\[
\frac{T_s^2}{RV}=\frac{(\pm6x+T_\Omega)^2}{(12x+R_\Omega)(x+V_\Omega)}=3+O(1/x).
\]
- Also \(L_s=\int_\Omega(s\mp6)^2+O(1/x)\), so the mean-scalar shift contributes \(O(1/x)\), as stated.
- The rate is
\[
\mathcal E(g_L)-1=\frac{12\int_\Omega|W^+|^2+\int_\Omega(s\mp6)^2-24\pi^2T_+(M)}{12L\,\mathrm{vol}(Y)}+O(L^{-2}).
\]
- \(T_\pm(N\#(S^1\times Y))=T_\pm(N)-4\) holds for every \(Y\).

**Generalisation (new): self-covering reservoirs.**
- \(\mathcal E\) is invariant under finite coverings: \(T_s^2/(RV)\) has degree \(2-1-1=0\) in the degree \(d\).
- \(S^1\times Y\) is diffeomorphic to its own \(d\)-fold cyclic covers.
- Hence, for any closed \(Z\) diffeomorphic to finite covers of itself of unbounded degree (\(S^1\times Y\) for any \(Y\), \(T^4\), \(S^2\times T^2\), nilmanifolds, torus bundles, mapping tori), gluing \(N\) into one ball of the lifted metric gives
\[
\alpha(N\#Z)\le\alpha(Z)\qquad\text{for every closed }N .
\]
- For products this yields \(\alpha(N\#(S^1\times Y))\le\inf_{g_Y}\bigl[4-(\int s_Y)^2/(\mathrm{vol}\int|\mathrm{Ric}_Y|^2)\bigr]\). Since \(|\mathrm{Ric}_Y|^2\ge s_Y^2/3\), the bracket is \(\ge1\), with equality iff \(Y\) is Einstein with \(s\neq0\). This is why exactly spherical and hyperbolic \(Y\) give 1.
- This explains the remark about the four-dimensional neck. The mechanism is unbounded self-covering degree, not the circle as such. The \(L/r\) cost estimate for three-dimensional necks is a heuristic and has no proof in the note.

**Corollary.**
- On \(X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) with \(\ell\ge1\): \(k+4\ell\ge A\) gives \(T_+\le0\) and \(\alpha\ge1\), and the reservoir gives \(\alpha\le1\). So \(\alpha=1\), not attained when \(k+4\ell>A\).
- The **converse is not proved**. For \(1/3<h<1\) the available bounds are \((3h-1)/(h+1)\le\alpha\le1\). "\(=1\) iff \(k+4\ell\ge A\)" should read "if".
- The bound \(4h/(1+h)\) with \(h=(k+4\ell)/A\) is attributed to corpus line 5562, which was not supplied. The note's own §5 states it only for \(\ell=0\), as \(4k/(A+k)\). Whether it extends to \(\ell>0\) with \(k\) replaced by \(k+4\ell\) needs that source.

## 5. Lemma 71.T and the α-readings

**Verified.**
- \(\mathcal E\ge4P/R\).
- At a constant-\(s\) metric, \(\mathcal E=16P/(4P+\int s^2)\), and \(16P/Y^2\) is the value at \(\lambda=s/4\).
- The normalisation bound \(R\le24\pi^2T_+/\eta\) holds for either orientation.
- The general lower bound \(\alpha\ge\mathfrak p_*/(\mathfrak p_*+\tfrac34T_{\min})\) for \(T_{\min}>0\) follows from \(R\le4P+24\pi^2T_\pm\) and monotonicity in \(P\). It needs no supply hypothesis, so \(P_*>0\Rightarrow\alpha>0\) on every manifold.

**Upper bound on supply manifolds.**
- \(\alpha\le4\mathfrak p_*/(A+\mathfrak p_*)\) holds by the following chain.
- Every class has \(Y<0\). In such a class \(\int s^2\ge Y^2\), with equality at the Yamabe metric.
- Since \(P=4\int|W^+|^2+\int s^2/12-8\pi^2T_+\), we get \(P(\hat g)\le P(g)\).
- Then \(\mathcal E(\hat g)=16\hat P/(4\hat P+\hat Y^2)\le4p/(p+A)\), using \(\hat Y^2\ge32\pi^2A\), which is inherited from LeBrun.

**Correction to the "exact quotient".**
- Within a \(Y<0\) class one has \(\mathcal E(g)\ge4-b/(c/4+b/3)\) with \(b=T_s^2/V\) and \(c=4(4\int|W^+|^2-8\pi^2T_+)\).
- This lower bound increases in \(b\). Using \(T_s\ge YV^{1/2}\) gives \(b\le Y^2\) whenever \(T_s\le0\), so the Yamabe metric minimises \(\mathcal E\) over the metrics in its class with \(T_s\le0\).
- Metrics in a \(Y<0\) class can have \(T_s>0\), via \(T_s(u^2g)=\int(6|\nabla u|^2+su^2)\), and then \(b\) can exceed \(Y^2\).
- So "\(\alpha=\inf4p/(p+A+\upsilon)\)" is established as an upper bound, and as an equality among \(T_s\le0\) metrics. Equality over all metrics needs an argument for \(T_s>0\) metrics.

**Collapse.**
- The companion identity excludes total collapse with **globally** bounded curvature, i.e. \(V\sup|\mathrm{Rm}|^2\to0\), for \(\mathcal E\)-small sequences. Such collapse forces \(\chi=0\) by Chern–Weil, while \(\mathcal E<1\) forces \(\chi>0\).
- Step 59.Z's alternative (II) allows finitely many shrinking bubble balls, which can carry all of \(\chi\). Gauss–Bonnet then only gives \(6\int|W|^2+L_s\to48\pi^2\chi\) and \(12\int|W^+|^2+L_s\to24\pi^2T_+\) as \(V\to0\).
- So the sentence "alternative (II) is excluded" holds only for bubble-free collapse.

**59.C, 59.D: correct.**
- 59.C: \(\mathrm{MinVol}=0\Rightarrow\chi=\tau=0\Rightarrow\alpha\ge1\).
- 59.D: the neck region has \(L_s=O(e^{-3T})\), and \(R\to36V_H\).

**59.N.**
- The α-zero for \(\lambda\neq0\) is correct. On the annulus \(\int s^2\le Ct^4(1+\lambda_b^8t^{-12})\to0\), so \(L_s\to0\).
- The note uses \(\lambda\) for both the Einstein constant and the bubble scale; these must be separated.
- "Ricci-flat orbifolds give \(\alpha\ge1\)" is a topological fact about the specific resolutions (K3: \(T_+=0\)). It is not a consequence of the gluing, which only gives \(R\to0\) and a quotient of the form 0/0.

**EH rate on \(\mathbb{CP}^2\#\mathbb{CP}^2\).**
- Arithmetic: \(R\to48\pi^2\) (\(\lambda=3\), \(V_{\rm orb}=4\pi^2/3\)), \(T_+=14\), \(T_-=2\), and \(8\pi^2a^4/48\pi^2=a^4/6\). The input \(P=2\pi^2a^4(1+o(1))\) is inherited from Step 61 and was not re-derived here.
- The hypothesis \(L_s=o(a^4)\) is doubtful. The \(\mathrm{Ric}^\circ\) responsible for \(P=\Theta(a^4)\) comes from an \(O(1)\) mismatch between the EH core and the orbifold 2-jet on a region of volume \(\sim a^4\). The scalar curvature on that core has an \(O(1)\) deviation from 12 on the same volume, so \(L_s=O(a^4)\) generically, with an unknown constant.
- The defensible statement is \(\mathcal E(g_a)=\Theta(a^4)\), provided \(L_s=O(a^4)\), with constant \((8\pi^2+\ell)/48\pi^2\), where \(\ell=\lim L_s/a^4\) is to be computed.

## 6. What is new versus classical, and sources needed

**Classical:**
- The combination \(\int(4|W^\pm|^2+s^2/12-|\mathrm{Ric}^\circ|^2)=8\pi^2T_\pm\) (Hitchin–Thorpe; LNN's displayed form in the self-dual case).
- The Weitzenböck vanishing \(b_+=0\) for ASD metrics with \(s>0\).
- Hitchin's equality case.
- Conformal flatness of \(\mathbb R\times S^3\) and \(\mathbb R\times H^3\).
- LeBrun's hyperbolic-ansatz classes.

**Corpus-inherited:** Identity 71.1 in \(\mathcal E\)-form, and the wall (a).

**New as far as the supplied sources show:**
- 71.B(b)–(e), including the covering refinement.
- The value \(\alpha=1\), attained, on \(\#4\overline{\mathbb{CP}}^2\) and on the \(S^1\times Y\) mapping tori.
- The ASD formula as an \(\mathcal E\)-statement.
- 71.D, with its rate and the self-covering principle.
- The companion Gauss–Bonnet identity.
- The unconditional lower bound \(\alpha\ge\mathfrak p_*/(\mathfrak p_*+\tfrac34T_{\min})\).

**knowledge_request:**
1. LeBrun 1991, *Explicit self-dual metrics on \(\mathbf{CP}_2\#\cdots\#\mathbf{CP}_2\)* (JDG 34): positive-scalar representatives and the diffeomorphism type.
2. The Ishida–LeBrun passage at line 400: ASD metrics with \(s>0\) on \(k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\).
3. Hitchin 1974: the equality case.
4. Literature on ASD and half-flat conformal structures with \(Y<0\) on K3 and T⁴, and Goldman on conformally flat manifolds with nilpotent holonomy.
5. Prior occurrences of the λ-optimised Einstein-deviation functional \(4-(\int s)^2/(V\int|\mathrm{Ric}|^2)\), or of the reservoir/self-covering bound, to settle precedence.
6. Ozuch/Biquard adapted EH metrics, for the scalar-variance constant \(\ell\).
7. Corpus line 5562, to check whether the recovery bound extends to \(\ell>0\).