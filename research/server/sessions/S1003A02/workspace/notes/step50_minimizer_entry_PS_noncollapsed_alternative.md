# Step 50 — Minimizer entry: scale-adapted Palais–Smale selection, the noncollapsed gap/attainment alternative, the Kähler infimum, and the cell family in Yamabe variables

> **Status (Steps 51–52).** The analytic §§2–4 of this note (Lemma W, Theorems 50.A–C, the \(b_2-2b_1\) bubble charge, "scalar-flat bubbles never
> save", the connected-sum/SW case split) are **superseded** and kept only as history. Lemma W is not a consequence of Bour/Streets, the input-to-output
> scale comparison it needs is false, and the bubble charge is \(b_2+4b_1\). Corrections: `step51_residual_entry_link_charges_and_kahler_recovery.md`;
> reduced conditional structure theorem, frozen-weight selection and Kronheimer absorption: `step52_residual_norm_selection_absorption.md`.
> §5 (Theorem \(K_\infty\)) survives in the corrected form of the Step-51 note (total transforms, successive Arezzo–Pacard, fixed \(J\)); §7 (family ledger) survives.
Session S1003A02, Agent2, Execute.
Scripts/data: `workspace/scripts/step50_family_ledger.sh` (runs A01's `step43_yamabe_lebrun_ledger.py`, N=80000, on ten A01 `perp_area` records) → `workspace/data/step50_family/ledger_*.json`; `workspace/scripts/step50_family_and_kahler.py` → `workspace/data/step50_family_summary.json`.
Sources read this step: Arezzo–Pacard, *Blowing up and desingularizing constant scalar curvature Kähler manifolds* (Knowledge object `Blowing-up-and-desingularizing-constant-scalar-curvature--7e9bd4072728`, Thms 1.1–1.3, Cor 8.2–8.3); Bour, *Fourth order curvature flows and geometric applications* \cite{bour2010fourth} (class (E_P), Thm 1.4–1.5, §3 gradient formulas); Anderson, *Orbifold compactness for spaces of Riemannian metrics* (Knowledge object `Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159`, Thm 1.1, Thm 1.2, Remark 3.10); Gursky–Viaclovsky, *Critical metrics on connected sums of Einstein four-manifolds* (Knowledge object `Critical-metrics-on-connected-sums...--e569e9d1f954`, (1.5)–(1.8), Prop 3.3); Streets \cite{streets2013long}.

Conventions as in the theorem package: \(P(g)=\int|\mathrm{Ric}^\circ|^2d\mu\), \(\widehat P=P/8\pi^2\); \(8\pi^2\chi=\int(|W|^2-\tfrac12|\mathrm{Ric}^\circ|^2+\tfrac{s^2}{24})\), \(12\pi^2\tau=\int(|W^+|^2-|W^-|^2)\).

---

## 1. The variational structure of \(P\)

In dimension four \(P=\mathcal F_{\rm Ric}-\tfrac14\mathcal F_R\). Bour (§3, from Besse 4.H) gives
\[
\nabla P=-\delta\tilde\delta\mathrm{Rm}-\mathrm{Ric}\circ(\mathrm{Ric}-\tfrac12 Rg)-\mathring{\mathrm{Rm}}(\mathrm{Ric})+\tfrac12\bigl(|\mathrm{Ric}|^2-\tfrac14R^2\bigr)g ,
\]
so \(-\nabla P=\delta\tilde\delta\mathrm{Rm}+\mathrm{Rm}*\mathrm{Rm}\) belongs to Bour's class \((E_P)\) with \(a=b=0<\tfrac1{2(n-1)}=\tfrac16\): the DeTurck-modified flow is strongly parabolic (Bour Thm 1.4), and Bando–Bernstein–Shi estimates hold under curvature bounds (Thm 1.5). In the Gursky–Viaclovsky parametrization \(\mathcal F_\tau=16\pi^2\chi+\tfrac12\mathcal B_{2(\tau+1/3)}\), \(P=\mathcal F_{-1/4}\) corresponds to \(\mathcal B_{1/6}=\int|W|^2+\tfrac16\int R^2\) up to a topological constant. Hence:

* \(P\)-critical \(\iff\) \(B^{1/6}\)-flat \(\iff\) \(R\) constant and \(B=\tfrac13R\,\mathrm{Ric}^\circ\) (GV (1.6)–(1.8) with \(t=\tfrac16\)); the gauged linearization is elliptic since \(t\neq0\) (GV Prop 3.3).
* On a closed manifold the trace of the critical equation forces \(R\) constant; on a complete finite-energy ALE critical metric \(R\) is an \(L^2\) harmonic function, hence \(R\equiv0\) and the metric is Bach-flat and scalar-flat.
* Anderson (Remark 3.10): critical metrics of \(\int|z|^2=P\) have constant scalar curvature, satisfy an equation \(D^*D\mathrm{Ric}+\mathrm{Rm}*\mathrm{Ric}=0\), and therefore satisfy his small-curvature estimate (1.5) **provided the volume lower bound (1.4) is assumed**; Anderson Thm 1.1/1.2 then give \(C^{1,\alpha}\) orbifold compactness and ALE blow-up limits.

So exact critical points of \(P\) have a complete noncollapsed compactness theory. The obstacle identified in Steps 19–21 and 49 is that near-minimizers are not critical. The next section removes that obstacle without regularizing \(P\).

## 2. Theorem 50.A (scale-adapted Palais–Smale entry)

**Curvature scale.** For a smooth metric \(g\) on a closed \(M^4\) let \(r_g(x)=\sup\{r: r^2|\mathrm{Rm}_g|\le1\text{ on }B_g(x,r)\}\) (capped at a fixed global scale after normalizing \(\mathrm{Vol}=1\)). It is 1-Lipschitz. Fix a smoothing \(\rho\) with \(\tfrac12r_g\le\rho\le r_g\), \(|\nabla^j\log\rho|_{\rho^{-2}g}\le C_j\) (mollify \(\log r_g\) in bounded-curvature exponential charts; no injectivity bound is used — charts are pulled back to tangent balls).

**Weighted flow.** With \(w=\rho_{g_0}^4\) fixed, consider
\[
\partial_tg=-w\,\nabla P(g)+\mathcal L_{V(g)}g,\qquad g(0)=g_0,
\]
\(V\) the Bour DeTurck field multiplied by \(w\) (the extra \(dw\otimes V\) terms are of order three, so the principal symbol is \(w\) times Bour's strongly elliptic symbol).

**Lemma W (uniform local existence).** There are \(c_0,C\) depending only on the order of the estimates such that the weighted flow exists on \([0,c_0]\), and in every bounded-curvature chart of \(\tilde g_0=\rho^{-2}g_0\) (pulled back to tangent balls) the rescaled solution \(\tilde g_t=\rho^{-2}g_t\) satisfies \(\|\tilde g_t-\tilde g_0\|_{C^2}\le Ct^{\theta}\) and \(|\nabla^j\mathrm{Rm}_{g_t}|\le C_j(\rho^{-2-j}+\dots)\) with \(C_j\) uniform for \(t\in[c_0/2,c_0]\).

*Proof.* Since \(P\) is scale invariant, \(\nabla P(\lambda^2 g)=\lambda^{-2}\nabla P(g)\) as a \((0,2)\)-tensor. For the variable factor \(g=\rho^2\tilde g\),
\(\rho^2\nabla P(\rho^2\tilde g)=\nabla P(\tilde g)+\mathcal E(\tilde g,\nabla\log\rho,\dots,\nabla^4\log\rho)\), where \(\mathcal E\) is of order \(\le3\) in \(\tilde g\) with coefficients polynomial in the derivatives of \(\log\rho\). Therefore \(\partial_t\tilde g=-[\nabla P(\tilde g)+\mathcal E]+\mathcal L_{\tilde V}\tilde g\): the weighted flow for \(g\) is an unweighted Bour-class flow for \(\tilde g\) perturbed by lower-order terms with uniformly bounded coefficients, starting from a metric of uniformly bounded curvature (all derivatives, by the choice of \(\rho\) and \(t\ge c_0/2\) smoothing). Standard quasilinear strongly parabolic theory in a uniform atlas (as in Bour §2; local covers handle collapse, the equation being diffeomorphism-natural) gives a uniform existence time and the stated estimates. \(\square\)

*Status:* this is a routine adaptation of standard parabolic theory, but it is written here at proof-sketch level; its full write-up (uniform Schauder constants in pulled-back charts) is the one analytic item to expose in the final proof.

**Theorem 50.A.** For every smooth \(g_0\) there is a smooth metric \(g\) on the same manifold (isotopic through the flow) with
1. \(P(g)\le P(g_0)\);
2. \(C^{-1}g_0\le g\le Cg_0\) and \(C^{-1}\rho_{g_0}\le r_g\le C\rho_{g_0}\);
3. \(\displaystyle\int_M\rho_{g_0}^4\,|\nabla P(g)|_g^2\,d\mu_g\le\frac{2}{c_0}\bigl(P(g_0)-P(g)\bigr)\le\frac2{c_0}\bigl(P(g_0)-\alpha(M)\bigr).\)

*Proof.* The DeTurck term does not change \(P\) (diffeomorphism invariance), so \(\frac{d}{dt}P(g_t)=-\int w|\nabla P(g_t)|^2d\mu_{g_t}\). Integrate over \([c_0/2,c_0]\) and choose \(t_*\) where the integrand is at most its mean; item 2 is Lemma W. \(\square\)

**Meaning.** The quantity \(\rho^4\int_{B(x,\rho)}|\nabla P|^2\) is scale invariant (\(|\nabla P|^2d\mu\) scales like \(\lambda^{-4}\)). Item 3 says: **every minimizing sequence of \(P\) can be replaced, without leaving the infimum, without changing the manifold, and without changing the local geometry at its own curvature scale, by a minimizing sequence whose normalized \(L^2\) Euler–Lagrange residual tends to zero at every point at that point's own scale.** For the fourth-order operator in dimension four an \(L^2\) residual is subcritical (the critical space is \(L^1\)), which is why this is the right entry: an Ekeland selection in a \(C^k\) metric gives a residual in \((C^k)^*\), worse than critical and useless, while the unweighted flow gives smallness only at the smallest scale of \(g_0\). The weight \(\rho^4\) is exactly the device that makes every scale run for unit local time. This replaces the derivative-penalization route (\(P+\varepsilon\int|\nabla\mathrm{Rm}|^2\), whose comparison radius \(R_*(\delta)\) could diverge) by an infimum-preserving selection that adds no term to the functional.

## 3. Theorem 50.B (ε-regularity and orbifold compactness for noncollapsed minimizing sequences)

**Hypothesis (NC).** \(\mathrm{Vol}(g_i)=1\) and \(\mathrm{vol}\,B_{g_i}(x,r)\ge\nu_0r^4\) for all \(x\), \(r\le1\).

**Energy bound.** Gauss–Bonnet gives \(\int|W|^2+\tfrac1{24}\int s^2=8\pi^2\chi+\tfrac12P\), hence \(\int|\mathrm{Rm}|^2\le C(\chi(M)+P)\) uniformly along a minimizing sequence.

**Theorem 50.B.** Let \(g_i\) be a minimizing sequence for \(\alpha(M)\) satisfying (NC), and let \(g_i'\) be its Theorem-50.A replacement (which still satisfies (NC) with \(\nu_0/C^4\)). There exist \(\delta_0,C_0\) and \(i_0\) such that Anderson's small-curvature estimate (1.5) holds for \(g_i'\), \(i\ge i_0\). Consequently (Anderson Thm 1.1–1.2) a subsequence converges, in \(C^{1,\alpha}\) modulo diffeomorphisms and smoothly on the regular part, to a compact orbifold \((V,g_\infty)\) with finitely many singular points (number and local groups bounded by \(\chi,\alpha,\nu_0\)), and rescalings at the concentration points give complete ALE orbifold bubbles (finitely many levels). Moreover
* \(g_\infty\) is \(P\)-critical (\(B^{1/6}\)-flat) on the regular part, with constant scalar curvature;
* every bubble \(N\) is a complete noncollapsed \(P\)-critical ALE metric with \(R\equiv0\), i.e. Bach-flat and scalar-flat.

*Proof.* Suppose (1.5) fails along a subsequence: points \(x_i\), radii \(r_i\le1\) with \(\int_{B(x_i,r_i)}|\mathrm{Rm}|^2\le\delta_0\) but \(\sup_{B(x_i,r_i/2)}r_i^4|\mathrm{Rm}|^2\) not controlled, so \(r_{g_i'}\) is \(\ll r_i\) somewhere in \(B(x_i,r_i/2)\). Point-picking gives \(y_i\) with \(r_{g_i'}\ge\tfrac12r_{g_i'}(y_i)\) on \(B(y_i,A_ir_{g_i'}(y_i))\), \(A_i\to\infty\). Rescale by \(r_{g_i'}(y_i)^{-1}\): curvature \(\le4\) on balls of radius \(A_i\), (NC) at all scales up to \(\to\infty\), smoothing estimates of Lemma W for all derivatives, and by Theorem 50.A(3) the rescaled \(\|\nabla P\|_{L^2(B_{A_i})}^2\le16\int\rho^4|\nabla P|^2\to0\). A subsequence converges smoothly to a complete noncollapsed metric with \(\nabla P=0\), \(\int|\mathrm{Rm}|^2\le\delta_0\), and \(\sup_{B(y_\infty,1)}|\mathrm{Rm}|=1\). Its scalar curvature is constant; by Anderson Remark 3.10 it satisfies (1.5) with constants depending on \(\nu_0\); applying (1.5) on \(B(y_\infty,r)\) with \(r\to\infty\) gives \(\sup|\mathrm{Rm}|\le(C_0\delta_0/\nu_0)^{1/2}r^{-2}\to0\), a contradiction. Smooth convergence on the regular part and passage of \(\nabla P(g_i')\to0\) in \(L^2_{\rm loc}\) give criticality of the limits; the scalar-curvature statements are §1. \(\square\)

*Status:* rests on Lemma W and on Anderson's Remark 3.10 (stated there for critical metrics of \(\int|z|^2\) with (1.4) assumed). The proof uses only exact critical blow-up limits, so no approximate-critical ε-regularity needs to be invented.

## 4. Theorem 50.C (noncollapsed decomposition of α and the gap/attainment/Einstein alternative)

**Bubble charge.** For a scalar-flat ALE orbifold \(N\) with one end \(S^3/\Gamma\) (flat cone), the ALE Gauss–Bonnet and signature formulas give, in both orientations,
\[
\widehat P(N)=\frac1{2\pi^2}\int_N|W^{\pm}|^2-(2\chi\pm3\tau)(N)+\frac2{|\Gamma|}\mp3\eta_\Gamma
\;\ge\;\Bigl[\frac{2}{|\Gamma|}-2\chi(N)+3|\tau(N)+\eta_\Gamma|\Bigr]_+=: \mathfrak c(N)
\]
(the Step-20 bubble inequality; \(\eta_\Gamma\) in the convention of that note). For a pure blow-up bubble \(N\simeq\mathbb R^4\#k_b\overline{\mathbb{CP}}^2\) (\(\Gamma=1\), \(\chi=1+k_b\), \(\tau=-k_b\)): \(\mathfrak c(N)=k_b\), with equality iff \(W^+\equiv0\) (Burns-type). Multi-end bubbles add the end terms.

**Theorem 50.C.** Under the hypotheses of Theorem 50.B, with \((V,g_\infty)\) and bubbles \(N_1,\dots,N_m\) (all levels),
\[
\alpha(M)\;\ge\;P(g_\infty)+\sum_bP(N_b)\;\ge\;P(g_\infty)+8\pi^2\sum_b\mathfrak c(N_b),
\]
and \(M\) is diffeomorphic to the orbifold resolution of \(V\) by the bubble trees. In particular:
1. **(Attainment modulo bubbles.)** If no curvature concentrates, \(\alpha(M)\) is attained by a smooth \(P\)-critical metric on \(M\).
2. **(Zero gap.)** If \(\alpha(M)=0\), then \(g_\infty\) is an Einstein orbifold metric and every bubble is Ricci-flat ALE: the only noncollapsed zero-gap mechanism is the canonical-model one (Einstein orbifold resolved by Ricci-flat ALE spaces). If moreover \(V\) has no orbifold points, \(M\) carries an Einstein metric. Equivalently: **if \(M\) carries no Einstein metric and is not an Einstein-orbifold/Ricci-flat-ALE resolution, every minimizing sequence collapses somewhere, or \(\alpha(M)>0\).**
3. **(Blow-ups.)** Let \(M=X\#k\overline{\mathbb{CP}}^2\) with \(X\) minimal of general type and \(b^+(X)\ge2\). If \(V\) is smooth (all \(\Gamma=1\)), then \(M\cong V\#\hat N_1\#\cdots\#\hat N_m\) (\(\hat N\) the one-point compactifications). By the Seiberg–Witten connected-sum vanishing theorem, either every \(\hat N_b\) has \(b^+=0\), or \(b^+(V)=0\). In the first case each \(\hat N_b\) is negative definite, hence (Donaldson) has diagonal form with \(k_b=b_2(\hat N_b)\), \(\mathfrak c(N_b)\ge k_b-2b_1(N_b)\) (\(=k_b\) if \(b_1(N_b)=0\)), and \(V\) has the intersection form of \(X\#k'\overline{\mathbb{CP}}^2\), \(k'=k-\sum k_b\). Then \(\alpha(M)\ge P(g_\infty)+8\pi^2(k-k')\) with \(P(g_\infty)\ge\alpha(V)\) **attained** on \(V\) by the critical metric \(g_\infty\). The Burns upper bound of Theorem F (insertion cost \(\to8\pi^2\)) makes this sharp: \(\alpha(M)=P(g_\infty)+8\pi^2(k-k')\) in this branch. The second case (a bubble carrying all of \(b^+\), the bulk negative definite) is a separate alternative, not excluded here.
4. **(Where subunit saving lives.)** Scalar-flat bubbles never save: a subunit per-class coefficient cannot be carried by scale-separated noncollapsed bubbles. If \(\alpha(X\#k\overline{\mathbb{CP}}^2)<8\pi^2k\) and the minimizing sequence is noncollapsed, the saving is carried by the exact critical limit \(g_\infty\) itself (or by orbifold-type bubbles with \(\Gamma\ne1\)).

**Application to the certified cell.** Let \(X\) be a ball quotient with injectivity radius large enough that the authoritative cell (exact CH outside cell radius \(128\)) embeds. Inserting it gives a closed metric on \(X\#\overline{\mathbb{CP}}^2\) with \(\widehat P\le0.995662732771115\), so \(\alpha(X\#\overline{\mathbb{CP}}^2)<8\pi^2\). In the first branch of item 3 with \(k=1\), the option \(k'=0\) (the class carried by a negative-definite bubble with \(b_1=0\)) would force \(\alpha\ge P(g_\infty)+8\pi^2\ge8\pi^2\). Hence: **for such \(X\) (with \(b^+(X)\ge2\)), every minimizing sequence for \(\alpha(X\#\overline{\mathbb{CP}}^2)\) either collapses somewhere, or concentrates in an orbifold-type bubble with \(\Gamma\ne1\), or in a bubble with \(b^+>0\) or \(b_1>0\), or converges without concentration and \(\alpha(X\#\overline{\mathbb{CP}}^2)\) is attained by a smooth \(P\)-critical (\(B^{1/6}\)-flat, constant-scalar) metric on \(X\#\overline{\mathbb{CP}}^2\) itself.** (With \(k=1\) and \(k'=1\), \(m=0\) bubbles of blow-up type remain, so \(V\cong M\) up to homotopy-sphere summands carrying \(\mathfrak c\ge0\).) If in the last case \(\alpha=0\), that metric is Einstein. This is the first statement of the project that converts the certified local cell into a statement about the actual minimizers on a closed manifold.

**What this changes.** The density-free O10 obstruction, the Taub–NUT/Gibbons–Hawking clusters (many classes behind one lens link), and the Hopf/Berger collapse channel of Steps 28–32 are exactly the collapsed alternatives; Theorem 50.C shows that, apart from them, the problem *is* the existence and value theory of exact \(B^{1/6}\)-flat metrics plus a computable bubble tariff. The unrestricted per-class question becomes: (a) a collapse analysis for \(P\)-minimizing sequences (the remaining analytic frontier, now precisely isolated), and (b) a lower bound for \(P\) on exact critical metrics on \(X\#k'\overline{\mathbb{CP}}^2\), where the critical equation \(B=\tfrac13R\,\mathrm{Ric}^\circ\) supplies the differential information (Cotton/\(\delta W^+\) control) that was missing for arbitrary metrics in Steps 41–44: on a critical metric \(\delta W^+\) is determined by \(\mathrm{Ric}^\circ\) through the Bach equation, so the Cotton slack of Proposition 43.C is no longer free.

## 5. Theorem K∞ (the Kähler infimum is exactly \(8\pi^2k\), not attained)

Let \(X\) be a minimal compact complex surface of general type, \(A=c_1^2(X)\), and \(M\) the blow-up of \(X\) at \(k\) points (distinct or infinitely near). Then
\[
\inf\{P(g): g\text{ Kähler on }M\}=8\pi^2k,
\]
not attained for \(k\ge1\).

*Proof.* Lower bound (Step 36): for Kähler \(g\) with class \(\Omega\), \(\widehat P=\frac{(K_M\cdot\Omega)^2}{\Omega^2}+\frac1{32\pi^2}\int(s-\bar s)^2-A+k\); since \(K_M\cdot\Omega=\pi^*K_X\cdot\Omega+\sum E_i\cdot\Omega\) with \(E_i\cdot\Omega>0\), \(K_X\) nef, and Hodge index \((\pi^*K_X\cdot\Omega)^2\ge A\,\Omega^2\), one gets \(\widehat P>k\) for every Kähler metric when \(k\ge1\).
Upper bound: the pluricanonical model \(\bar X\) carries a Kähler–Einstein orbifold metric \(\omega_{KE}\) with \([\omega_{KE}]=\lambda c_1(K)\), its automorphism group is discrete (Arezzo–Pacard proof of Cor 8.3), so \((\bar X,\omega_{KE})\) is nondegenerate. Apply Arezzo–Pacard Thm 1.3 simultaneously at the singular points (Kronheimer crepant ALE resolutions, scalar-flat) and at \(k\) smooth points (Burns metrics \(a_j\eta\), \([\eta]=-PD[E]\)): for \(\varepsilon<\varepsilon_0\) there are cscK forms with \([\omega_\varepsilon]=[\omega_{KE}]+\varepsilon^2\sum[\eta_j]\) (nondegenerate case, Thm 1.3). For infinitely near points iterate Thm 1.1 (each blow-up of a general-type surface is again nondegenerate). With constant scalar curvature, \(\widehat P(\omega_\varepsilon)=\frac{(K_M\cdot\Omega_\varepsilon)^2}{\Omega_\varepsilon^2}-A+k\). The crepant classes \(c\) satisfy \(K\cdot c=0\), \(c^2\le0\); the Burns classes give \(K_M\cdot(-\varepsilon^2a_jE_j)=\varepsilon^2a_j\). Exact computation (`step50_family_and_kahler.py`):
\[
\widehat P(\omega_\varepsilon)=k+2\varepsilon^2\textstyle\sum_ja_j/\lambda+O(\varepsilon^4)\longrightarrow k.
\]
\(\square\)

This closes the open package item "exact Kähler infimum" by citation, for every minimal general-type \(X\) (ample or merely nef \(K\)). The recovery family is the clean \((D_W,\Delta V)\)-test family: \(D_W=0\) exactly (Kähler, scalar \(-4\) after scaling: \(|W^+|^2=2/3\)), \(\widehat P-k=\Delta V/2\pi^2\), \(\Delta V\to0\). It is also exactly the bubbling picture of Theorem 50.C(3) with \(k'=0\): KE bulk plus Burns bubbles, each saturating \(\mathfrak c=1\) with \(W^+\equiv0\).

## 6. Weyl-deficient volume (unconditional)

At the Yamabe representative (\(s\equiv-4\)) the Kähler value is \(|W^+|^2=2/3\), and \(D_W=\int(\tfrac23-|W^+|^2)\le\tfrac23\mathrm{Vol}\{|W^+|^2<\tfrac23\}\). From (Y0), \(8\pi^2k-P=4(D_W-\Delta V)\), so \(P\le8\pi^2ck\) forces
\[
\mathrm{Vol}_{\hat g}\{|W^+|^2<2/3\}\ \ge\ 3\pi^2(1-c)k+\tfrac32\Delta V .
\]
This is the volume form of the Step-49 weighted statement. It does not count atoms; in the noncollapsed case Theorem 50.C now tells where that volume must sit (in the critical bulk, not in scalar-flat bubbles).

## 7. The certified family in Yamabe variables

Ledger along A01's perpendicular CH family (scalar \(-4\) units, \(8\pi^2\) units, tail-free \(\Delta V\), floating; `step50_family_summary.json`):

| \(x_0\) | \(X\) | \(\widehat P(g)\) | saving \(1-\widehat P(\hat g)\) | \(\Delta V\) | \(D_W/\Delta V\) | efficiency saving\(/4\Delta V\) | \(\Delta V/x_0\) |
|---|---|---|---|---|---|---|---|
| .003 | 64 | .999795 | .000205 | .00464 | 1.0110 | .0110 | 1.55 |
| .010 | 64 | .998700 | .001300 | .01627 | 1.0200 | .0200 | 1.63 |
| .015 | 64 | .997766 | .002235 | .02518 | 1.0222 | .0222 | 1.68 |
| .020 | 256 | .996800 | .003201 | .03437 | 1.0233 | .0233 | 1.72 |
| .030 | 128 | .995663 | .004339 | .05310 | 1.0204 | .0204 | 1.77 |
| .050 | 256 | .996103 | .003899 | .09133 | 1.0107 | .0107 | 1.83 |
| .070 | 256 | 1.000885 | −.000874 | .12855 | 0.9983 | −.0017 | 1.84 |
| .100 | 128 | 1.015277 | −.015219 | .18236 | 0.9791 | −.0209 | 1.82 |
| .150 | 256 | 1.052023 | −.051819 | .26703 | 0.9515 | −.0485 | 1.78 |

(\(x_0=.015,.01,.003\) use \(X=64\) records and are not converged in \(X\); the \(x_0=.03\) row agrees with the interval certificate and with A01's ledger.)

Reading. \(\Delta V\) is linear in the bolt scale, \(\Delta V\approx1.6\)–\(1.8\,x_0\), while the saving is of second order at small \(x_0\) (Burns kernel direction; ratio to \(x_0^2\log(1/x_0)\) of order 2–4, consistent with the Bianchi-IX second-order law but not a fit of it) and turns negative beyond \(x_0\approx.065\). Hence \(D_W/\Delta V=1+\text{saving}/4\Delta V\) is pinned to \(1\) by the leading-order Gauss–Bonnet bookkeeping of the core volume, with a maximal excess \(2.33\%\) at \(x_0\approx.02\); efficiency \(\to0\) in both directions. Within this family no core size approaches the field-extremal regime \(D_W\to2\Delta V\) (efficiency \(1\)). The ratio is not set by the collar: it is the statement that the core's added volume is almost exactly paid back by its Weyl deficit, the residual being the second-order kernel saving. A construction pushing efficiency up must change the core type (not its size), e.g. cores whose added volume carries Weyl deficit at density close to \(2/3\) with less than the Gauss–Bonnet-required volume — which Theorem 50.C now says must be a non-scalar-flat, non-bubble piece of the critical bulk.

## 8. Open items, in order of consequence

1. **Collapse.** Extend Theorem 50.B without (NC): the remaining escape is collapse with bounded curvature at the own scale (local \(F\)-structures/nilpotent structures). Theorem 50.A already applies (no injectivity bound used); what is missing is the analogue of Cheeger–Tian small-energy estimates for exact \(P\)-critical metrics in the collapsed regime, plus the Taub–NUT/ALF bubble charge with lens links (many classes behind one link).
2. **Critical metrics.** A lower bound for \(P\) on \(B^{1/6}\)-flat metrics on \(X\#k'\overline{\mathbb{CP}}^2\): the Bach equation \(\delta\delta W=\tfrac13 R\,\mathrm{Ric}^\circ+\dots\) ties \(\delta W^+\) to \(\nabla\mathrm{Ric}^\circ\) and should make the Proposition-43.C Cotton pairing coercive; this is now the decisive analytic question for the noncollapsed regime.
3. **Orbifold bubbles** with \(\Gamma\ne1\) on blow-ups: classify which can occur for \(X\#k\overline{\mathbb{CP}}^2\) and compute their charge \(\mathfrak c\).
4. **Lemma W write-up.**
