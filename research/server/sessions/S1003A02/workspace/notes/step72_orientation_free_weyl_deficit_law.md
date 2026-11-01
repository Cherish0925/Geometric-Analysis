# Step 72 — The orientation-free Weyl-deficit law and the universal unit ceiling

Agent3, Execute. Inputs: Step 71, its TTCS verifier, Spirit #87, the exact conformal comparison in `Skills/geometric-analysis/research/Curvature_Realizability.tex` lines 5765–5871, Kobayashi subadditivity as quoted in Malchiodi–Malizia \cite{malchiodiweyla}, and ABKS's Yamabe–Weyl plane \cite{akutagawaweyl}. Exact checks: `scripts/step72_weyl_deficit_identity.py` -> `data/step72_weyl_deficit_identity.json`; warped-dumbbell check: `scripts/step72_dumbbell_numeric.py` -> `data/step72_dumbbell_numeric.json`.

## 1. Orientation-free identity

Use
\[
 8\pi^2\chi=\mathcal W+\frac{S}{24}-\frac P2,
 \quad \mathcal W=\int|W|^2,\quad
 R=P+\frac S4,\quad L_s=S-\frac{T_s^2}{V}.
\]
Eliminating \(P,S\) from \(\mathcal E=(4P+L_s)/R\) gives, for \(R>0\),
\[
 \boxed{\mathcal E(g)-1=
 \frac{6\bigl(\mathcal W(g)-8\pi^2\chi(M)\bigr)+L_s(g)}{R(g)}.}
 \tag{72.1}
\]
This is exactly Identity 71.1 after adding the signature formula, but it removes the orientation and reveals its variational content. Define the conformal Weyl deficit
\[
 d([g])=8\pi^2\chi(M)-\mathcal W([g]).
\]
Then
\[
 \mathcal E(g)=1-\frac{6d([g])-L_s(g)}{R(g)}. \tag{72.2}
\]
The symbolic script obtained zero residual and checked round \(S^4\) (\(\mathcal E=0\)) and the product cylinder \(\mathbb R\times S^3\) (\(\mathcal E=1\)). At Ricci-flat metrics \(R=0\), (72.1) is read only in denominator-free form; the definition gives \(\mathcal E=4\).

Immediate all-metric consequences:
- \(\mathcal E(g)<1\) iff \(6d([g])>L_s(g)\). Thus every sub-unit metric lies in a conformal class with \(d>0\), but positive deficit alone need not make an arbitrary representative sub-unit because scalar variance can spend the deficit.
- At any nonzero constant-scalar metric, \(L_s=0\), so \(\mathcal E<1\iff\mathcal W<8\pi^2\chi\).
- At a Yamabe representative with \(Y\ne0\),
  \[
  R=\frac{Y^2}{3}+2\mathcal W-16\pi^2\chi,
  \qquad
  \mathcal E=1-\frac{6d}{R}.
  \tag{72.3}
  \]
  Equivalently \(\mathcal E=16P/(4P+Y^2)\). The denominator is positive automatically for a metric.

## 2. Exact global variational law

Every conformal class has a Yamabe representative. Because \(\mathcal W\) is conformally invariant, if \(d([g])>0\) and \(Y([g])\ne0\), its Yamabe representative has \(L_s=0\), \(R>0\), and (72.3) gives \(\mathcal E<1\). Conversely, any metric with \(\mathcal E<1\) has \(d>0\). Its conformal class cannot have \(Y=0\): at a scalar-flat Yamabe metric, Gauss–Bonnet gives \(P=2\mathcal W-16\pi^2\chi=-2d<0\), impossible. Hence
\[
 \boxed{\alpha(M)<1\iff
 \exists[g]\text{ with }Y([g])\ne0\text{ and }\mathcal W([g])<8\pi^2\chi(M).}
 \tag{72.4}
\]
The \(Y\ne0\) condition is actually forced by positive deficit but is kept visible because (72.3) divides by the nonzero Yamabe scale and because it separates scalar-flat boundary classes.

Taking Yamabe representatives gives the unconditional exact law
\[
 \boxed{
 \alpha(M)=\min\left\{1,
 \inf_{[g]:Y([g])\ne0}
 \left[1-
 \frac{6d([g])}
 {\,Y([g])^2/3+2\mathcal W([g])-16\pi^2\chi(M)\,}
 \right]\right\}.}
 \tag{72.5}
\]
Equivalently, writing the denominator as \(R(\widehat g)=P(\widehat g)+Y^2/4\),
\[
 \boxed{
 \alpha(M)=1-6\max\left\{0,
 \sup_{[g]:Y([g])\ne0}
 \frac{8\pi^2\chi(M)-\mathcal W([g])}
 {P(\widehat g)+Y([g])^2/4}
 \right\}.}
 \tag{72.6}
\]
Here \(\widehat g\) is the Yamabe representative. This max-with-zero is essential: the universal dumbbell construction supplies the competing value 1 even when every conformal class has nonpositive Weyl deficit. Formula (72.6) is more general than the supply-specific scalar-\(-4\) bridge in the corpus. It follows directly from (72.1), Yamabe existence, and the fact that positive deficit itself excludes \(Y=0\); no assumption that every class is Yamabe-negative is needed.

This gives the common mechanism for the human functional. The unit wall is the vanishing of the normalized Weyl deficit. A small Einstein gap means that the conformal Weyl deficit is nearly \(R/6\), while \(\alpha=0\) requires the equality value \(d/R=1/6\) asymptotically. On a nonzero Einstein metric, Gauss–Bonnet gives exactly \(6d=R\).

## 3. Universal ceiling by a smooth dumbbell

Take a warped metric \(dr^2+f(r)^2g_{S^3}\) on \(S^4\), with two fixed smooth caps and a central cylinder \([0,L]\times S^3(1)\). A fixed cap–cylinder interpolation makes the whole metric smooth with all noncylindrical integrals independent of \(L\). Warped products with one-dimensional base and space-form fibers are conformally flat.

On the cylinder,
\[
 \operatorname{Ric}=(0,2,2,2),\quad s=6,\quad
 |\operatorname{Ric}^{\circ}|^2=3,\quad |\operatorname{Ric}|^2=12,
\]
so
\[
 P=6\pi^2L+O(1),\quad R=24\pi^2L+O(1),\quad L_s=O(1).
\]
Replace a fixed ball in one cap by a fixed punctured/rescaled metric on any closed \(M\), through a fixed neck. Since \(M\#S^4\cong M\), the replacement changes \(P,R,S,T_s,V\) by \(O(1)\) independent of \(L\). Thus
\[
 \mathcal E(g_L)=1+O(L^{-1})
 \quad\Longrightarrow\quad
 \boxed{0\le\alpha(M)\le1\text{ for every closed four-manifold}.}
 \tag{72.7}
\]
The numerical warped model used \(f=\sin r\) near the poles, a quintic \(C^2\) blend to \(f=1\), and a cylinder. Its Gauss–Bonnet residual was below \(4\times10^{-13}\); \(\mathcal E\) decreased from \(1.1600\) at \(L=5\) to \(1.011685\) at \(L=200\), with \(L(\mathcal E-1)\to\) a finite constant. This model checks the curvature formulas and asymptotics but is not itself the smooth proof metric: replace the quintic by an endpoint-flat \(C^\infty\) cutoff, which changes only the fixed cap constants.

Combining (72.7) with the unit-wall lower bound gives the exact topological region
\[
 \boxed{2\chi(M)\le3|\tau(M)|\Longrightarrow\alpha(M)=1.}
 \tag{72.8}
\]
If the inequality is strict, the infimum is not attained. At equality, attainment is exactly the half-conformally-flat, nonzero-constant-scalar class of Theorem 71.B. This settles the values (not always attainment) for K3, \(T^4\), \(k\overline{\mathbb{CP}}^2\) for \(k\ge4\), general-type blow-ups for \(k\ge A\), and the real-hyperbolic blow-ups beyond their Hitchin–Thorpe wall.

## 4. Connected-sum calculus for the Weyl deficit

Let
\[
 \mathcal W_*(M)=\inf_g\int_M|W_g|^2,
 \qquad d_*(M)=8\pi^2\chi(M)-\mathcal W_*(M).
\]
Kobayashi's connected-sum subadditivity is quoted explicitly in Malchiodi–Malizia \cite{malchiodiweyla}:
\[
 \mathcal W_*(M\#N)\le\mathcal W_*(M)+\mathcal W_*(N).
\]
Since \(\chi(M\#N)=\chi(M)+\chi(N)-2\),
\[
 \boxed{d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.}
 \tag{72.9}
\]
This is the correct global bookkeeping: the \(16\pi^2\) loss is the Euler charge of the neck.

Examples in the present curvature normalization:
- \(d_*(S^4)=16\pi^2\), so an \(S^4\) summand is neutral, as topology requires.
- Reversed Fubini–Study on \(\overline{\mathbb{CP}}^2\) is Einstein with \(\mathcal E=0\), hence \(d/R=1/6\); directly \(\mathcal W=12\pi^2\), \(\chi=3\), so \(d_*=12\pi^2\) (the signature lower bound forces equality).
- Iterating (72.9) yields
  \[
  d_*(\#_n\overline{\mathbb{CP}}^2)\ge(16-4n)\pi^2.
  \]
  The signature lower bound supplies the matching upper bound, so in fact
  \[
  d_*(\#_n\overline{\mathbb{CP}}^2)=4\pi^2(4-n),
  \qquad \mathcal W_*=12n\pi^2.
  \]
  It is positive for \(n\le3\), zero for \(n=4\), and topology gives \(\alpha=1\) for \(n\ge4\). Therefore
  \[
  \alpha(\#_n\overline{\mathbb{CP}}^2)<1\ (n\le3),
  \qquad \alpha(\#_n\overline{\mathbb{CP}}^2)=1\ (n\ge4).
  \]
  This recovers the Poon/LeBrun side without choosing an ASD metric and explains the exact threshold by Euler loss.
- If a minimal general-type surface has a nonzero Kähler–Einstein metric, its Weyl deficit is \(d_*(X)\ge4\pi^2A/3\) (equality for the KE class at the starting point). Each \(\overline{\mathbb{CP}}^2\) insertion changes the lower bound by \(-4\pi^2\), so
  \[
  d_*(X\#k\overline{\mathbb{CP}}^2)\ge4\pi^2(A/3-k).
  \]
  Consequently \(k<A/3\Rightarrow\alpha<1\), reproducing the threshold of the strict construction \(\alpha<4k/(A+k)\). This is an existence statement, not the sharp value.

In the intermediate band \(A/3\le k<A\), topology permits either \(\alpha<1\) or \(\alpha=1\). By (72.4), the exact question is
\[
 \boxed{
 \inf_{[g]}\mathcal W([g])<8\pi^2\chi(X\#k\overline{\mathbb{CP}}^2)
 \quad\text{or not}.}
 \tag{72.10}
\]
Using signature to eliminate \(W^-\), and the corrected topology
\[
 \tau(X\#k\overline{\mathbb{CP}}^2)=\frac{A-2\chi(X)}3-k,
 \qquad 2\chi(M)+3\tau(M)=A-k,
\]
this is equivalently
\[
 \inf_g\int|W^+|^2<2\pi^2(A-k)
\]
in the session's endomorphism norm. Thus \(\alpha=1\) in this band is exactly the all-class lower bound \(\int|W^+|^2\ge2\pi^2(A-k)\). It belongs to the classical Weyl-functional problem, not to a new local-tariff programme. ABKS \cite{akutagawaweyl} already organize Yamabe and Weyl conformal invariants jointly and explicitly note that the relation between their Yamabe-line invariant and the global Weyl infimum is unclear on general-type surfaces. LeBrun's later work \cite{lebrun2023weyl} shows that positive-Yamabe lower bounds need not control the global infimum because negative-Yamabe classes can have much smaller Weyl energy.

## 5. Reinterpretation of the open range

For \(0<k<A/3\), the value is now rigorously in \([0,1)\); the unsolved issue is not whether it lies below the unit wall but how close it is to zero. Formula (72.6) says that every local construction must be scored by
\[
 \frac{d([g])}{R(\widehat g)},
\]
not by \(P\) alone. The certified cell, Burns response and exceptional-flux ledger measure how a topology insertion changes both the conformal Weyl deficit and the Yamabe/Ricci denominator. A universal P tariff is neither necessary nor sufficient to determine \(\alpha\) unless the Yamabe scale is controlled.

This changes the ranking of unfinished computations:
1. **Burns isotropic boundary.** It is directly relevant: when the logarithmic P response vanishes, the regular second-order term may decide the change in \(d/R\).
2. **EH/A_n/Wahl rates.** They matter for \(\alpha\) only over a nonzero-scale Einstein orbifold, where \(R\) has a stable bulk denominator; Ricci-flat bulk rates remain P-only.
3. **O10 density-free fields.** They can contribute a genuine lower bound only if they control the same normalized Weyl-deficit ratio, rather than merely harmonic twist or P.
4. **Collapse.** The universal identity already excludes sub-unit values outside strict Hitchin–Thorpe and globally bounded-curvature total collapse at \(\alpha=0\), but concentration balls and noncollapsed orbifold channels remain.

## 6. Binding corrections from the Step-71 verifier

The Step-71 TTCS integration is authoritative for the material it read (`trace/ttcs/results/step71_ttcs01_verifier1_integration.md`). Apply these corrections:
- The exact scalar-\(-4\) conformal comparison is supported by the actual corpus lines 5765–5871; its supply assumptions must remain explicit. Formula (72.5), derived independently, is the unconditional all-class replacement at the level of the human functional.
- At a constant-scalar ASD metric set \(y=s^2V/(32\pi^2)\); write \(y=Y^2/(32\pi^2)\) only for a Yamabe minimizer.
- On \(X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), \(k+4\ell\ge A\) implies \(\alpha=1\) once the reservoir is combined with the wall; the converse was not proved by Step 71. The universal dumbbell now proves \(\alpha\le1\), while \(h<1/3\) is independently sub-unit by the strict Burns construction.
- The old statement that Anderson's collapse alternative is excluded must be narrowed to globally bounded-curvature, bubble-free collapse of the same normalized \(\mathcal E\)-small sequence.
- The EH coefficient \(a^4/6\) remains conditional on \(L_s=o(a^4)\).
- The long-circle theorem is correct; the universal dumbbell supersedes its need for handle topology.

## 7. Status

Closed in this step:
- the orientation-free identity (72.1);
- the exact sub-unit characterization (72.4) and variational law (72.5)–(72.6);
- the universal ceiling \(\alpha\le1\), hence exact value at and beyond the Hitchin–Thorpe wall;
- the connected-sum Weyl-deficit law (72.9) and the exact \(n=4\) threshold for \(\#_n\overline{\mathbb{CP}}^2\);
- the reduction of the intermediate general-type band to the classical all-class Weyl-energy inequality.

Still open: the value in \(0<k<A/3\), the intermediate band's Weyl infimum, attainment at the topological wall beyond the known half-flat examples, and quantitative degeneration of maximizing deficit-to-Ricci ratios.


## 8. Independent verification (binding)

The focused two-branch verifier is `trace/ttcs/results/step72_ttcs02_verifier1_integration.md`; it confirms (72.1)–(72.10), the universal dumbbell, connected-sum law, and all final constants, with these refinements binding over §§1–7:

- At \(R=0\), use the original definition \(\mathcal E=4\); ratios with denominator \(R\) are not evaluated.
- Formula (72.6) is justified by a conformal-class minimization lemma. For every metric in a class, \(S\ge Y^2\), including \(Y<0\) via \(|Y|\le\|s_-\|_2\). In a positive-deficit class, the Yamabe representative minimizes \(\mathcal E\), since \(R=S/3-2d\ge Y^2/3-2d=R(\widehat g)\). An unambiguous form is
  \[
  \alpha=1-6\sup\left(\{0\}\cup
  \left\{\frac{d([g])}{Y([g])^2/3-2d([g])}:d([g])>0\right\}\right).
  \]
  Positive deficit automatically forces \(Y\ne0\).
- The smooth proof uses an endpoint-flat \(C^\infty\) cap interpolation. The numerical quintic is only \(C^2\) and is evidence for the formulas, not the smooth construction.
- At \(T_{\min}=0\), equality of the signature bound selects \(W^-=0\) when \(\tau>0\), \(W^+=0\) when \(\tau<0\), and \(W=0\) when \(\tau=0\); attainment also requires \(Y\ne0\).
- The \(\#_n\overline{\mathbb{CP}}^2\) Weyl deficit is exact, not just bounded below: \(d_*=4\pi^2(4-n)\), \(\mathcal W_*=12n\pi^2\).
- The general-type connected-sum calculation assumes an actual smooth negative Kähler–Einstein metric on the starting surface. Canonical models with \((-2)\)-curves require their separate orbifold/ALE transfer already used elsewhere in the package; do not silently enlarge the hypothesis.
- The corrected signature is \(\tau(X\#k\overline{\mathbb{CP}}^2)=(A-2\chi(X))/3-k\). The final threshold \(\inf\int|W^+|^2<2\pi^2(A-k)\) is correct in the session endomorphism norm (four times this right side in the corresponding \((0,4)\)-tensor convention).
