# TTCS Independent Branch Record

```json
{
  "step_id": 69,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step69_P_form_upper_law_balanced_towers.md",
    "Sessions/S1003A02/workspace/data/step69_balanced_upper_law.json",
    "Sessions/S1003A02/workspace/scripts/step69_balanced_upper_law.py",
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md",
    "Sessions/S1003A02/workspace/notes/step59_rigorous_burns_expansion_and_zero_gap_structure.md",
    "Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md"
  ]
}
```

## Task

Verify, as a careful geometric analyst, the note Sessions/S1003A02/workspace/notes/step69_P_form_upper_law_balanced_towers.md. It claims: (1) Lemma 69.Y: for Y[g]<0 and the Yamabe metric ĝ in [g], E(ĝ)=16P(ĝ)/Y^2 and P(g)-P(ĝ)=|ŝ|∫|∇φ|^2+3∫(Δφ/φ)^2, hence alpha(M) <= 16 P(g)/Y[g]^2 for the scale-invariant defect E(g)=inf_λ ∫|Ric-λg|^2/(λ^2 V); (2) Corollary 69.Y': on X#k CP2bar#l(S1xS3), X minimal general type, LeBrun's polarized supply gives Y^2>=32π^2 c1^2(X), so alpha <= P(g)/(2π^2 A) for all g, alpha <= 4 p_*/A; (3) Theorem 69.B: exact non-asymptotic balanced bound alpha/h <= 28/9+(8/9)p_c = 3.99614465... on X#8n CP2bar#7n(S1xS3) for every finite cover X of a preliminary ball-quotient cover with large injectivity radius; (4) handle model (H'): the Green-function blow-up of round S1xS3 at a point is AE, conformally flat, scalar flat, with P=32π^2, and its small-scale gluing into any background changes P by 32π^2+o(1); (5) Theorem 69.KE(a): alpha(X#kCP2bar) < 4k/c1^2(X) for every minimal surface of general type and k>=1, via Corollary 59.KE; (b) cover version; (c) the claim that for non-ball-quotient KE hosts unramified covers force slope sigma->infinity as h->0, so the balanced small-h slice is unreachable there. Check each argument: conventions (Weyl norms, Gauss-Bonnet with AE end, P formula with F_+=4|W+|^2+s^2/12), whether LeBrun's Lemma 1 and Prop 3.2 are used correctly (the supply on manifolds with S1xS3 summands and b+=1 chambers), whether the certified cell P-enclosure (A01 step33 JSON values quoted in the note) can legitimately replace the J value in the coefficient, the topology arithmetic (T+, T-, sigma for Delta=0), the injectivity-radius/ball-count argument, uniformity of 59.R constants on covers, the handle gluing estimate, and the scope corrections in §4(c). Identify any error, missing hypothesis, or overstatement, and say precisely how to repair it. Also say whether Lemma 69.Y / alpha<=4p_*/A is standard (do not invent references; name a knowledge_request if needed).

## Output

# Verification memo: Step 69, the P-form upper law

## Summary

Every upper bound in the note holds, with one exception in form. The central formula of Lemma 69.Y is wrong as an equality. The correct value at a Yamabe metric is smaller, so every downstream upper bound survives and becomes slightly sharper.

The same algebra also gives a reverse inequality between \(\alpha\) and \(p_*\). The note's final paragraph says no such inequality is known; this memo derives one. It shows that \(\alpha\) and \(4p_*/A\) are comparable up to a factor of 3 for small \(p_*/A\), and the bound is exact on the real-hyperbolic Theorem H family.

All other components check out:
- the topology arithmetic,
- the coefficient arithmetic,
- the use of the P enclosure,
- the injectivity-radius construction,
- the locality of the 59.R constants,
- the \(S^1\times S^3\) Green-function handle,
- the slope analysis of §4(c).

Each of these needs at most a small repair, listed below. One input rests on material not supplied here: the LeBrun supply on manifolds with \(S^1\times S^3\) summands.

---

## 1. Lemma 69.Y: the equality is false; the bound survives in sharper form

**The defect at a constant-scalar metric.** Use the pointwise identity \(|\mathrm{Ric}-\lambda g|^2=|\mathrm{Ric}^\circ|^2+4(s/4-\lambda)^2\), which is correct. At constant \(s\), put \(\mu=1/\lambda\). Then
\[
\mathcal E=\inf_\mu\Big[\tfrac{P}{V}\mu^2+4\big(\tfrac{s}{4}\mu-1\big)^2\Big].
\]
The derivative in \(\mu\) at \(\mu=4/s\) (that is, \(\lambda=s/4\)) equals \(8P/(sV)\). This is nonzero unless \(P=0\), so \(\lambda=s/4\) is not the minimizer. The true minimum is
\[
\boxed{\ \mathcal E(\hat g)=\frac{16P(\hat g)}{4P(\hat g)+\hat s^2\hat V}=\frac{16P(\hat g)}{4P(\hat g)+Y[g]^2}=\frac{4P(\hat g)}{\int|\mathrm{Ric}_{\hat g}|^2}\ <\ \frac{16P(\hat g)}{Y^2}.\ }
\]

**Cross-check with the corpus formula.** A01 Step 33, Theorem B, gives \(\mathcal E=(4D-T^2/V)/(4V+D-2T)\) with \(D=\int|\mathrm{Ric}+g|^2\) and \(T=\int s+4V\). At constant \(s\):
- \(D=P+(s+4)^2V/4\) and \(T=(s+4)V\);
- the numerator is \(4P\);
- the denominator is \(P+s^2V/4\).

So \(\mathcal E=16P/(4P+s^2V)\), confirming the formula above.

**What the script actually checked.** Script check (1) substitutes \(\lambda=s/4\) into the quotient. It therefore verifies the value of one competitor, not the infimum. The JSON key `lemmaY_equals_16P_over_s2V` should be read in that sense.

**Repaired statement.** Use \(P(g)\ge P(\hat g)\), which follows from the correct Yamabe identity below. The function \(x\mapsto16x/(4x+Y^2)\) increases in \(x\) and decreases in \(Y^2\). Hence:
- \(\alpha(M)\le 16P(g)/(4P(g)+Y[g]^2)\) for every \(g\) with \(Y[g]<0\).
- On supply manifolds, using \(Y^2\ge32\pi^2A\),
\[
\alpha(M)\le\frac{4p(g)}{A+p(g)}\quad\forall g,\qquad \alpha(M)\le\frac{4p_*}{A+p_*}.
\]
- Theorem 69.B becomes the non-asymptotic bound \(\alpha/h\le c/(1+ch/4)\), where \(c=28/9+(8/9)p_c\). This implies the printed \(\alpha/h\le c\).
- Theorem 69.KE(a) becomes \(\alpha(X\#k\overline{\mathbb{CP}}^2)<4k/(A+k)\), which is stronger than \(4k/A\).

**The Yamabe comparison is correct.** The note uses \(P=\int(4|W^+|^2+s^2/12)\,d\mu-8\pi^2(2\chi+3\tau)\) in LeBrun's norm convention, where Kähler metrics have \(|W^+|^2=s^2/24\). This follows from LeBrun's Gauss–Bonnet formula \(2\chi+3\tau=(4\pi^2)^{-1}\int(2|W^+|^2+s^2/24-|\mathring r|^2/2)\). The Weyl term is conformally invariant. LeBrun's Lemma 1 (LeBrun 1996, §5) gives \(\int s^2d\mu-\hat s^2\hat V=12|\hat s|\int|\nabla\phi|^2+36\int(\Delta\phi/\phi)^2\), with \(\Delta=d^*d\) and integrals in \(d\mu_g\). Dividing by 12 gives the stated identity, and its \(\hat s=-24\) specialisation matches the package formula.

---

## 2. A reverse inequality that answers the note's final open sentence

**Jensen gives a lower bound for every metric.** Jensen's inequality in \(\lambda\) gives \(\int(s/4-\lambda)^2\ge V(\bar s/4-\lambda)^2\). Running the same minimization as in §1 yields
\[
\mathcal E(g)\ \ge\ \frac{16P}{4P+(\int s)^2/V}\ \ge\ \frac{16P}{4P+\int s^2}=\frac{4P}{R},\qquad R=\int|\mathrm{Ric}|^2 .
\]
Equality holds if and only if \(s\) is constant.

**Chern–Weil bounds \(R\).** From the P formula, \(\int s^2\le12P+96\pi^2T_+-48\int|W^+|^2\). Hence \(R\le4P+24\pi^2T_+\), where \(T_+=2\chi+3\tau\). Therefore
\[
\boxed{\ \mathcal E(g)\ge\frac{P(g)}{P(g)+6\pi^2T_+}\ \ \forall g,\qquad
\alpha(M)\ \ge\ \frac{p_*}{p_*+\tfrac34T_+}\quad (T_+>0).\ }
\]
This uses no Seiberg–Witten input and no Yamabe metric.

**Check against Theorem H.** For \(Y\#k\overline{\mathbb{CP}}^2\) with \(Y\) real hyperbolic:
- \(T_+=2\chi(Y)-k\);
- \(p_*=k\), which is the conditional input of Theorem H;
- the lower bound becomes \(4k/(k+6\chi(Y))\).

This is exactly the Theorem H value. The inequality is therefore exact there; equality forces \(W^+\to0\) and constant \(s\).

**The two-sided window on supply manifolds.** With \(T_+=A-Q\),
\[
\frac{p_*}{p_*+\tfrac34(A-Q)}\ \le\ \alpha(M)\ \le\ \frac{4p_*}{A+p_*}.
\]
For \(p_*\ll A\), this reads \(\tfrac43p_*/A\lesssim\alpha\lesssim4p_*/A\).

**Where the factor 3 comes from.** It is exactly the term \(48\int|W^+|^2\). On Kähler-type states, \(\int|W^+|^2=\int s^2/24\), so \(\int s^2/12+4\int|W^+|^2=\int s^2/4\). Then \(R\approx P+8\pi^2A\) and the lower bound rises to the upper one.

So the open sentence "a reverse inequality is not known" should be replaced by this window. The remaining question becomes precise: do \(\alpha\)-near-minimizers carry Kähler-level self-dual Weyl energy, \(\int|W^+|^2\approx\int s^2/24\)?

**What is not proved.** It is not shown that \(\alpha=\inf_g4P/R\). The upper side holds over Yamabe metrics only, and \(P/R\) is not monotone under the Yamabe change, because both \(P\) and \(\int s^2\) decrease.

---

## 3. Corollary 69.Y′: the Seiberg–Witten supply

**Pure blow-ups.** For \(\ell=0\), LeBrun 1996 Theorem 2 gives \(\int s^2>32\pi^2c_1^2(X)\) for every metric on \(X\#k\overline{\mathbb{CP}}^2\). The \(b^+=1\) chamber choice in its proof needs \(b_1=0\). This holds automatically: \(b^+=1\) forces \(p_g=0\), and \(\chi(\mathcal O)>0\) for general type then forces \(q=0\). The step "\(Y<0\)" also holds: a metric with \(Y\ge0\) has a constant-scalar representative with \(s\ge0\), which contradicts \(\int s^2\ge32\pi^2A>0\) together with the existence of Seiberg–Witten solutions. Theorem 69.KE(a) is therefore fully supported by the supplied LeBrun text.

**With handles (\(\ell>0\)).** The supplied LeBrun 1996 paper does not cover \(\#\ell(S^1\times S^3)\). The note relies on \cite{lebrun2001ricci} Prop. 3.2 and on corpus lines that were not supplied.

When \(\ell>0\), \(b_1(M)=\ell>0\). The \(b^+=1\) wall structure is then not the one in LeBrun 1996. This case is avoidable in every application of the note:
- **Ball-quotient covers (69.B).** Noether gives \(\chi(\mathcal O)=c_2/3\). So \(p_g\ge c_2/3-1\ge1\), hence \(b^+\ge3\), as soon as \(c_2(X)\ge6\). Every cover of degree at least 2 of a ball quotient, and in particular every large-injectivity cover \(X'\), satisfies this.
- **Covers in 69.KE(b).** \(\chi(\mathcal O)\) scales with the covering degree, so \(b^+\ge2\) for all large degrees.

Repair: state \(b^+(X)\ge2\) as a hypothesis whenever \(\ell>0\), and note that it is automatic in both families.

The remaining supply input is the statement that the scalar estimate \(\int s^2\ge32\pi^2c_1^2(X)\) persists after \(\#\ell(S^1\times S^3)\) for \(b^+\ge2\). This needs the source text.

---

## 4. Theorem 69.B: arithmetic, the P versus J substitution, and placement

**Topology.** For a ball quotient, \(\chi=A/3\) and \(\tau=A/9\). Each \(\overline{\mathbb{CP}}^2\) summand adds \(+1\) to \(\chi\) and \(-1\) to \(\tau\); each \(S^1\times S^3\) summand adds \(-2\) to \(\chi\).
- \(T_+=A-k-4\ell=A-Q\).
- \(T_-=A/3+5k-4\ell=A/3+12n\) at \(k=8n\), \(\ell=7n\), so \(3T_-/A=1+h\).
- \(\sigma=18\theta=4\).

All three agree with the general A01 formula \(3T_-/A=1+(\sigma-3)h\).

**Coefficient.**
- \(\tfrac89\times0.995662732771114\ldots+\tfrac{28}9=3.996144651352\ldots\).
- The J route gives \(3.996151138\ldots\).
- The difference, \(6.4867\times10^{-6}\), equals \(\tfrac89\times\) the scalar-variance enclosure \(7.2976\times10^{-6}\).
- \(\eta_P=1-p_c=0.0043372672\ldots\).

All four values match the JSON.

**Using the P enclosure in place of J is legitimate.** In the P route, only \(P\) of the closed glued metric enters. By Lemma 69.A it is the sum of the cell \(P\)-values. No \(8\pi^2\) offset arises, because the enclosure is the full \(\int_{\rm cell}|\mathrm{Ric}^\circ|^2\) and \(P\) is scale invariant.

One step needs to be written out. The inherited "arbitrarily small smoothing loss" was proved for \(J\). It transfers to \(P\) because \(|\mathrm{Ric}^\circ|^2\le|\mathrm{Ric}-\lambda g|^2\) pointwise for every \(\lambda\). So the \(P\)-change on the smoothing region is bounded by the J-density integral there. Add this one line.

**Injectivity radius.** Excluding elements that displace the base point by less than \(4R_c\) suffices for a **normal** subgroup \(\Gamma'\). Suppose \(\gamma\in\Gamma'\) moves some point \(\delta x_0\) by less than \(4R_c\). Then \(\delta^{-1}\gamma\delta\in\Gamma'\) moves \(x_0\) by less than \(4R_c\). Hence \(\mathrm{inj}>2R_c\) everywhere. State this normality argument explicitly. Covers inherit the bound.

**Ball count.** A maximal \(2R_c\)-separated set has \(2R_c\)-balls covering \(X\). Geodesic balls in a quotient of \(\mathbb{CH}^2\) have volume at most \(v_{CH}(r)\). Hence \(N\ge2\pi^2A/v_{CH}(2R_c)\). The printed \(v_{CH}(4R_c)\) is valid but weaker. The \(R_c\)-balls are disjoint and isometric to complex-hyperbolic balls, and the blow-up orientation matches the complex orientation.

**Handle cells.** Approach to \(32\pi^2\) at the fixed outer radius \(R_c\) follows directly from (H′) in an exact complex-hyperbolic ball.

**Quantifiers.** The quantifier statement is correct: existential only in \(X'\), universal over further covers and over \(n\le N/15\).

**Ramified towers in P form.** Both \(g_{CH}\) and \(g_m\) satisfy \(\mathrm{Ric}=-g\). So the interpolated metric has \(\mathrm{Ric}^\circ=O(\varepsilon_m)\), giving \(O(\varepsilon_m^2)\) per site and \(O(\varepsilon_m^2)\) relative to \(hA\). The surfaces \(\bar X_m\) are minimal of general type, so the supply applies. The volume and total-scalar ledger is genuinely gone. With the §1 correction the bound reads \(\alpha/h\le c_m/(1+c_mh/4)\), where \(c_m=4-4\theta_m(1-p_c)+O(\varepsilon_m^2)\).

---

## 5. The handle model (H′)

**Topology and P value.** \(N=(S^1\times S^3\setminus p,\,G_p^2g_0)\) is scalar flat and conformally flat. Since \(g_0\) can be taken locally flat near \(p\), \(G=|x|^{-2}+m+O(|x|)\). Inversion then gives \(\delta+O(|y|^{-2})\), so \(N\) is AE of order two.

For a single AE end, the Chern–Gauss–Bonnet end transgression tends to the Euclidean value 1, with corrections \(O(r^{-2})\). Therefore \(\int(|W|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)=8\pi^2(\chi(N)-1)=-16\pi^2\). Since \(\chi(N)=-1\), \(W=0\) and \(s=0\), this gives \(P(N)=32\pi^2\) exactly. This is correct and agrees with \(\mathfrak P_{0,1}\).

**Gluing.** The exact identity \(P(\tilde g)-P(g)=32\pi^2+\int(F_+(\tilde g)-F_+(g))\) holds, since \(\chi\) drops by 2 and \(\tau\) is unchanged. Two corrections are needed.

1. **The construction must be a superposition.** It should be \(\tilde g=g+\chi\cdot(\text{scaled }N-\delta)\), or equivalently scaled \(N\) carrying the background jets, as in 59.R. A literal replacement of \(g\) by scaled \(N\) on \(|x|<\rho_1\) at fixed \(\rho_1\) would delete \(\int_{B_{\rho_1}}F_+(g)\), which is \(O(\rho_1^4)\) and not small.
2. **The rate is \(O(\delta^2)\), not \(O(\delta^2\log\delta^{-1})\).** On \(R\delta<|x|<\rho_1\), the cross term is \(e=O(\delta^2|x|^{-2})\). Its linear part \(\int2\langle\mathcal C(g),e\rangle\) is of size \(\int\delta^2|x|\,d|x|=O(\delta^2)\). The quadratic part is \(O(\delta^4\log)\), and the core and annulus contribute \(O(\delta^4)\) and \(O(\delta^2)\).

For Einstein backgrounds the 59.R argument identifies the \(O(\delta^2)\) term. The conformal tail \((1+m\delta^2|x|^{-2})^2\delta\) has a Green-flux scalar component and no \(W^+\) component. So the linear term is a multiple of \(m\,s(p)\,\delta^2\). This is an Einstein-background analogue of \(-8\pi^2\varepsilon R^+(\zeta,\zeta)\): its sign is fixed by \(s(p)<0\) and \(m>0\) (positive mass). It is irrelevant for the limit used in the note.

---

## 6. Theorem 69.KE

**(a)** The chain is correct: Corollary 59.KE with the Part D, D.5 order of limits (\(\varepsilon\) fixed, then \(\lambda\to0\); the insertion difference is independent of \(\lambda\)), followed by Corollary 69.Y′. The coefficient \(\Phi/2=-s^2/64=-\tfrac14\) at \(s=-4\) is right.

With §1, the conclusion strengthens to \(\alpha<4k/(A+k)\). The comparison with LeBrun's bound \(p\ge k-A/3\) should now use both sides of the §2 window.

**(b)** Theorem 59.R's \(I(\varepsilon)\) depends only on \(g|_{B_{2\rho}(p)}\):
- the inner, far and outer regions all lie in that ball;
- \(E_1\) is the limit of \(\int\ell_g(\chi_\eta B)\), which is local because \(E_P=0\) on the support;
- identity (A.1) is additive over disjoint balls.

Fix \(N_X\) points in \(X\) with disjoint embedded \(2\rho_X\)-balls. Their lifts are isometric and disjoint, so \(\eta_X\) is uniform in \(m\), \(k\) and \(\ell\). The handles use (H′). This gives \(4p/A=h(4-4\theta\eta_X)+o\), so the stated bound holds; with §1 it becomes \(c/(1+ch/4)\). The supply needs \(b^+\ge2\) when \(\ell>0\), which is automatic for large covering degree (§3). The finite-\(\pi_1\) remark is correct.

**(c)** For unramified covers, \(\Delta_m/A_m=\Delta_X/A_X\), which is positive unless \(X\) is a ball quotient (equality case of Bogomolov–Miyaoka–Yau). Hence \(r=\Delta_X/(hA_X)\to\infty\) as \(h\to0\), and \(\sigma\to\infty\). The balanced slice \(\sigma=4\) needs \(r=1-\tfrac92\theta\le1\), that is, \(h\ge\Delta_X/A_X\). This analysis is correct.

The fixed-\(h\) two-sided window, with lower bound \(4\theta_\Delta/(1+\theta_\Delta)\) for \(\sigma<3\), is non-asymptotic as stated. It should carry \(0\le\theta_\Delta\le\tfrac13\) explicitly; \(\theta_\Delta\le h\) suffices for \(h\le\tfrac13\).

---

## 7. Remaining items

**Reference computation (item 4).** The script result \(s_1=0\) at the P-optimal corrector and \(\Phi_D=\Phi=-s^2/32\) lies on the eigenvector locus \(w_{12}=w_{13}=0\). There, Part D.3 states that the projector artifact vanishes, so the computation is admissible. It concerns only the logarithmic coefficient of \(D\). The \(D\)-route quotient still involves \(T^2/V\), so "the \(D\) route would give the same saving" holds only at that order. The note's "reference" label is apt.

**Wording in §5.** "The equality \(\alpha\le4p_*/A\)" is an inequality. Its corrected form is \(\alpha\le4p_*/(A+p_*)\), paired with the reverse bound of §2.

**Literature position.**
- Lemma 69.Y, in its corrected form, is two lines of algebra on top of LeBrun's Lemma 1 (LeBrun 1996) and Theorem 2/Prop. 3.2. It should be presented as an elementary observation.
- The bounds \(\alpha\le4p_*/(A+p_*)\) and \(\alpha\ge p_*/(p_*+\tfrac34T_+)\) are not located in the supplied sources. The corpus "vg-handle identity", with its \(R\)-denominator, suggests the \(4P/R\) structure may already be implicit there.
- **knowledge_request 1:** the text of \cite{lebrun2001ricci}, Prop. 3.2 and the theorem treating \(X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), including its \(b^+\) hypotheses and the mechanism by which monopole classes persist under \(\#S^1\times S^3\).
- **knowledge_request 2:** the corpus definition of \(\mathcal J\), to determine whether \(\mathcal J=4P/R\) and hence whether §2 is already recorded.