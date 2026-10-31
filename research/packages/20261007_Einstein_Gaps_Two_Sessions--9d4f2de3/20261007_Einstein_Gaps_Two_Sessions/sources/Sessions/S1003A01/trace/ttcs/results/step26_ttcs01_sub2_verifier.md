# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md",
    "Sessions/S1003A01/workspace/notes/step25_degeneration_matching_and_charge.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py"
  ]
}
```

## Task

Read the proposed Step-26 action-budget matching note together with the peer's chiral transgression note as a mathematical verifier. Check every normalization, the dimension-four rescaling of P and scalar curvature, the passage from the two chiral identities to the max lower bound, the controlled collapsed charge substitution, and the bound on the kernel C+4X=0. Identify hidden hypotheses needed for limits of charges and for applying a whole-cell budget to a prefix. Then propose the sharpest theorem statement that is actually supported, including how to formulate the missing high-shear alternative without silently assuming Einstein equations or bounded geometry. Focus on substantive mathematical corrections, not presentation.

## Output

# Verification memo: Step 26 action-budget matching against the chiral transgression identities (Steps 25, 27, 30)

## 1. Normalizations and the dimension-four rescaling

**Normalization of the functional.** With \(\int_{S^3}\sigma_{123}=2\pi^2\), the definition \(\widehat P=\frac1{8\pi^2}\int|\mathrm{Ric}^\circ|^2dV\) equals \(\frac14\int W|\mathrm{Ric}^\circ|^2dt\). Step 26 and Step 27 therefore use the same functional.

**Closed-manifold form of (1.1).** Combine
- \(8\pi^2\chi=\int(|W|^2-\tfrac12|\mathrm{Ric}^\circ|^2+\tfrac1{24}s^2)\), and
- \(12\pi^2\tau=\int(|W^+|^2-|W^-|^2)\).

This gives exactly
\[
\widehat P=\tfrac1{2\pi^2}\int|W^\pm|^2+\tfrac1{96\pi^2}\int s^2-(2\chi\pm3\tau),
\]
with no stray factor 2. The parenthetical "up to the factor 2" in Step 27 §1 is unnecessary. The reference values are consistent: bolt \(2\cdot2\pm3(-1)=1,7\); smooth centre \(2\).

**Rescaling.** For \(g^\#=b^{-2}g\) in dimension four:
- \(|\mathrm{Ric}^\circ|^2dV\) is invariant, and \(s(g^\#)=b^2s(g)=-24b^2\). Both statements are correct.
- \(\int s^2dV\) is also invariant. With \(s\equiv-24\), \(\frac1{96\pi^2}\int_Is^2dV=12\int_IW\,dt\) in either picture. Step 26 drops this term from (2.1), and it should be retained (§2).

**Hidden hypothesis in the rescaled-limit paragraph.** A limit of \(b_j^{-1}a_i\) exists only if the rescaled 1-jets \((b_j^{-1}a_i,a_i')\) stay bounded on compact \(t/b_j\)-sets.
- The energy bound plus constant \(s\) controls Ricci in weighted \(L^2\), hence \(a_i''\) in \(L^2_{\rm loc}\), *provided* the first derivatives are bounded.
- The diagonal Ricci components contain the quadratic terms \((a_i'/a_i)(a_j'/a_j)\). An \(L^2\) bound alone does not exclude Riccati-type growth of the logarithmic rates.
- Once \(C^1_{\rm loc}\) convergence holds, Ricci converges weakly in \(L^2\). Then \(s\to0\) a.e. and \(\widehat P(\lim)\le\liminf\widehat P\) by lower semicontinuity, so "scalar-flat, not necessarily Ricci-flat" is correct.

Uniform 1-jet control in scale-normalized variables is the same hypothesis as entering a controlled class. The small-bolt compactness question and the high-shear branch therefore have one common cause: loss of normalized \(C^1\) compactness.

## 2. Passage from the two chiral identities to the max bound

The bound \(\widehat P(C)\ge\max\{0,\Delta\mathfrak b_+,\Delta\mathfrak b_-\}\) is correct. Each identity bounds the same energy, and averaging only recovers the weaker Euler bound \(\Delta\mathfrak b\). The supported statement is stronger in three ways.

**(a) Keep the scalar term.**
\[
\widehat P(C)\ge\max_\pm\Delta\mathfrak b_\pm+\tfrac1{96\pi^2}\int_Cs^2 .
\]
This term is exact, and it is order one wherever the prefix reaches volume of order one.

**(b) Disjoint intervals add, with a free chirality choice on each.** For \(0=t_0<\dots<t_n\),
\[
\widehat P[t_0,t_n]\ \ge\ \sum_k\Big(\max\{\Delta_k\mathfrak b_+,\Delta_k\mathfrak b_-,0\}+S_k\Big).
\]
This exceeds both "total upward variation of \(\mathfrak b_+\)" and that of \(\mathfrak b_-\) separately, which is all Step 27 (2.1) records.

**(c) An independent jet-only density from the Hamiltonian constraint.**
- The Gauss equation gives \(G_{tt}=\mathrm{Ric}_{tt}-s/2=\sum_{i<j}\frac{a_i'a_j'}{a_ia_j}-\frac12R_\Sigma\). This is first order.
- Hence \(\mathrm{Ric}^\circ_{tt}=G_{tt}+s/4\) pointwise.
- Tracelessness gives \(|\mathrm{Ric}^\circ|^2\ge\frac43(\mathrm{Ric}^\circ_{tt})^2\). This is consistent with the Step-30 decomposition, since \(H=\frac43\mathrm{Ric}^\circ_{tt}\).

Therefore, when \(s\equiv-24\),
\[
\widehat P[I]\ \ge\ \tfrac13\int_IW\,(G_{tt}(J)-6)^2\,dt, \tag{2.c}
\]
a density depending only on the 1-jet \(J\). It enters the per-interval max, not the sum, because it bounds the same energy.

**Telescoping consequence.** Charges alone can never give more than the path's mixed upward variation. Take a path bolt \(\to\Sigma\to\) (an orbit with \(\mathfrak b_+=2-9\sinh^4\tau\)). Minimizing \(\max(0,\mathfrak b_+(\Sigma)-1)+\max(0,2-9\sinh^4\tau-\mathfrak b_+(\Sigma))\) over \(\mathfrak b_+(\Sigma)\) gives exactly \(1-9\sinh^4\tau\), whatever the collapse data. This is Corollary X2/X3. Any additional pricing of the high-shear branch must come from \(\int|W^\pm|^2\), from \(S\), or from (2.c).

## 3. Controlled collapsed charge substitution

I rederived the limits by hand with \(r=1\) normalization. Then
\[
a_f=z^{-1}e^{2x/3},\qquad a_g=z^{-1}e^{-x/3},\qquad a_h=z^2e^{-x/3}.
\]

**Orbit coefficients.**
- \(\gamma_f=z^{-3}(e^{-x/3}-e^{5x/3})e^{\dots}\to-2X\), \(\gamma_g\to2X\).
- \(\gamma_h=2\cosh x-z^6e^{-x}\to2\).

**Derivatives.**
- \(p_f=z^{-1}e^{2x/3}(p+\tfrac23\chi+\tfrac13\eta)\to P+\tfrac23C+\tfrac13N\).
- \(p_g\to P-\tfrac13C+\tfrac13N\).
- \(p_h=z^2e^{-x/3}(p-\tfrac13\chi-\tfrac23\eta)\to0\).

**Charges.** These reproduce the script's \(u_i\). With \(w_i=p_i+\gamma_i\),
\[
\mathfrak b_+=2-\textstyle\sum u_i^2-\prod u_i=-2-(u_f-u_g)^2\to-2-(C+4X)^2,
\]
\[
\mathfrak b_-=\textstyle\sum w_i^2-\prod w_i-2=2+(w_f-w_g)^2\to2+(C-4X)^2 .
\]
The \(o(z^3)\) and \(o(z)\) remainders contribute \(o(1)\), so they suffice. The reference checks pass:
- round centre \(u=0\), \(w=(2,2,2)\) gives \((2,2)\);
- bolt \(u=(0,0,-1)\), \(w=(0,0,3)\) gives \((1,7)\);
- biaxial Berger gives \((-2,2)\).

The formula is symmetric under \(f\leftrightarrow g\) (\(C+4X\mapsto-(C+4X)\)), so the slot relabeling issue of Step 25 does not affect it. However, \((X,C)\) must be defined relative to the two non-collapsing slots at \(\Sigma\).

**Hidden hypothesis: exactness of the polynomial charges.** The script *defines* \(\mathfrak b_\pm\) by the \(u\)- and \(w\)-polynomials. Theorem X defines them as \(\mathfrak b\mp\mathfrak s\) with the 84-term \(\mathfrak s\). Agreement at three reference configurations is evidence, not proof. A symbolic identity
\[
\mathfrak b_+-(2-\textstyle\sum u^2-\prod u)\equiv0,\qquad \mathfrak b_--(\textstyle\sum w^2-\prod w-2)\equiv0
\]
on general 1-jets would settle it. Both are plausible as Chern–Simons functionals of the two chiral \(SU(2)\) connections.

**Consequence if exact.** Inequality (2.1) holds at every finite section with the exact 1-jet charge, and no limit is needed. The device "first section at which the sequence enters a controlled class" is then superfluous. It is also ill-defined: the controlled class is a property of sequences of sections, namely
\[
z_j\to0,\quad x_j/z_j^3\to X,\quad (p_j,\chi_j,\eta_j)/z_j\to(P,C,N),
\]
not of a single section.

**Scale interpretation.** \(z=(a_h/a_g)^{1/3}=e^{-x/3}r/a_g\approx r/L\), where \(L\) is the base size. The controlled class is therefore exactly "logarithmic rates bounded at the base scale \(L\)": \(L(\log a_f)'=P+N/3+\dots\). The raw class is "rates bounded at the collapsed scale \(r\)".

## 4. The kernel bound, and where P and N reappear

**Numerical constant.** On \(C+4X=0\), the minus channel gives \(64X^2\le c+5\). For \(c=0.99585\), \(\sqrt{5.99585}/8=0.30608\). The statement should read \(|X|\le0.30608\); "\(|X|<0.306\)" is slightly false. The exclusion of \((X,C)=(1,-4)\) is correct by a wide margin: the prefix costs at least \(59\) in the limit.

**Hidden hypothesis.** The bound uses \(p,\eta=O(z)\). Now repeat §3 in the collapsed-scale chart: keep \(x=Xz^3\) and \(\chi=Cz\), but let \(p\to P_0\) and \(\eta\to N_0\) be of order one. Put
\[
\lambda_i=r(\log a_i)',\qquad \lambda_f,\lambda_g\to B=P_0+\tfrac13N_0,\qquad \lambda_h\to A=P_0-\tfrac23N_0 .
\]
Then:
- \(u_f-u_g\to C+4X\) and \(w_f-w_g\to C-4X\), as before;
- \(\delta=u_h+2\approx a_h'=z^2A+O(z^3)\), and \(u_fu_g\approx w_fw_g\approx z^{-2}B^2\).

The Step-30 identity \(\mathfrak b_+=-2-(u_f-u_g)^2+\delta(4-u_fu_g)-\delta^2\), and its \(w\)-analogue \(\mathfrak b_-=2+(w_f-w_g)^2+\epsilon(4-w_fw_g)+\epsilon^2\) with \(\epsilon=w_h-2\approx\delta\), give
\[
\boxed{\ \mathfrak b_+\to-2-(C+4X)^2-Q,\qquad \mathfrak b_-\to2+(C-4X)^2-Q,\qquad Q=\lambda_f\lambda_g\lambda_h=AB^2.\ }
\]
This should be confirmed symbolically: replacing `p=P*z, eta=N*z` by `p=P, eta=N` in `collapse_chiral_charge_limit.py` is the computation.

**What the formula shows.**
- P and N cancel only in the base-scale chart. At the collapsed scale they enter both chiralities equally, through the scale-free Kasner product, i.e. through the Euler flux (\(\mathfrak b\to-8CX-Q\)), while \(\mathfrak s\) is unchanged.
- The kernel bound becomes \(64X^2\le c+5+Q\). It is invalid for collapsed-scale entries with \(Q>0\).
- Raw \(\chi\) (\(\chi/z\to\infty\) with \(x/z^3\) bounded) sends \(\mathfrak b_-\to+\infty\) and is priced. Raw \(x\) gives \(\gamma_{f,g}\sim z^{-3}\) and is priced unless compensated (§5).
- The genuinely dangerous raw coordinates are \((p,\eta)\), in agreement with Step 30.

**Constraint pricing of the collapsed-scale chart.** In this chart \(G_{tt}=\sigma_2(\lambda)/r^2-\frac12R_\Sigma\), with \(r^2R_\Sigma\approx8z^2\to0\). By (2.c), an interval of length \(\theta r\) on which the rates stay near \(\lambda\) costs about \(\frac\theta3\sigma_2(\lambda)^2\). Cheap raw sections must therefore lie near the Kasner cone
\[
\sigma_2=B(B+2A)=0 .
\]
- On the branch \(A=-B/2\), i.e. \(N_0=3P_0\), the normalized exponents are \((\tfrac23,\tfrac23,-\tfrac13)\). This is the Ricci-flat Kasner with base expanding and circle shrinking, and \(-Q=B^3/2\).
- On \(B=0\), the circle opens with constant base, as at a smooth bolt, and \(Q=0\).

The "volume bounce" that raises \(\mathfrak b_+\) above \(-2\) is therefore precisely a \((\tfrac23,\tfrac23,-\tfrac13)\) Kasner epoch with \(B>0\). On it the prefix budget allows
\[
B^3/2\le\min\{3+c+(C+4X)^2,\ 5+c-(C-4X)^2\},
\]
i.e. \(B\lesssim2\) at \(X=C=0\). Such entries are not excluded by charges. The raw \(\varepsilon=1/16\) entry with \(\mathfrak b_+=1.452\) is compatible with this mechanism. Its total bound \(0.45194+0.57446=1.0264\) correctly adds disjoint intervals.

## 5. Directions not priced by any charge

Let \(K_c=\{J:\ \mathfrak b_+(J)\le1+c,\ \mathfrak b_-(J)\le7+c\}\). This set is unbounded in normalized jet space along:

1. **The minus-kernel ray.** Here \(w_f-w_g\) is bounded while \(u_f-u_g\to\infty\) (e.g. \(C-4X=0\) with \(X\to\infty\), or raw \(x\) compensated by \(\chi\)). Then \(\mathfrak b_+\to-\infty\) at no prefix cost. Since the exact CH tail also has \(\mathfrak b_+=2-9\sinh^4T\to-\infty\), suffix charges do not price it either. The plus-kernel \(C+4X=0\) singled out in Step 26 is the *opposite*, priced direction.
2. **Collapsed-scale jets with \(Q\ge0\) large.** On the cone this means \(B<0\): base contracting outward with the circle opening at rate \(1/r\).
3. **Jets with \(Q\) bounded but individual rates diverging off the cone.** These are priced only by (2.c), and only if the rates persist over an \(r\)-length interval.

The \(\beta\)-pinning estimate (10) is weakest exactly here. Near the bolt \(W\approx b^2t\), so \(\int dt/W\) diverges logarithmically and is of size \(b^{-2}\log\) on collapsed intervals. Pinning cannot be applied on intervals touching the bolt. The constraint density (2.c), of order \(W/r^4\sim1/r\), is strongest exactly where pinning is weakest. The two tools are complementary.

## 6. Supported theorem statements

**Theorem A (exact prefix budget).** *Hypotheses:*
- \(g\) is an \(SU(2)\)-diagonal metric on the \(O(-1)\) disc bundle with \(a_i\in C^{1,1}\);
- the bolt at \(t=0\) is regular (\(a_f(0)=a_g(0)\), \(a_h\sim t\));
- \(\mathfrak b_\pm\) are given by the exact polynomials of §3, subject to the identity check there.

Then for every partition \(0=t_0<\dots<t_n\),
\[
\widehat P[0,t_n]\ge\sum_k\max\Big\{\Delta_k\mathfrak b_++S_k,\ \Delta_k\mathfrak b_-+S_k,\ K_k\Big\},
\]
where \(\mathfrak b_\pm(0)=(1,7)\), \(S_k=\frac1{96\pi^2}\int_{I_k}s^2\), and, when \(s\equiv-24\), \(K_k=\frac13\int_{I_k}W(G_{tt}-6)^2dt\).

*Application to a whole cell.* For an exact-CH-ended cell, \(\widehat P_{\rm cell}\) is an unrenormalized integral of a density \(\ge0\), because \(\mathrm{Ric}^\circ\equiv0\) on the tail. Hence \(\widehat P[\text{prefix}]\le\widehat P_{\rm cell}\). This is the only fact needed to transfer a whole-cell budget to a prefix. The number \(c=0.99585\) bounds \(\alpha\) over the *diagonal* class only, so the conclusions concern diagonal near-minimizers.

**Corollary B (limits).** Let \(\widehat P(g_j)\le c+o(1)\), and let \(\Sigma_j\) be sections whose jets converge in the base-scale chart (\(Q=0\)) or in the collapsed-scale chart (\(Q=AB^2\)). Then
\[
(C-4X)^2-Q\le5+c,\qquad -3-(C+4X)^2-Q\le c .
\]
In the base-scale chart on \(C+4X=0\), this gives \(|X|\le\sqrt{c+5}/8\).

Suppose additionally that a later section \(\Sigma'_j\) has convergent charge \(\beta_\pm\). Then the parallelogram bound
\[
(C+4X)^2\le c-2-\beta_+-\max(0,(C-4X)^2-5)-Q
\]
follows. For a CH-like \(\Sigma'\) at radius \(\tau\), the pair \((X,C)\) is confined to a compact set when \(9\sinh^4\tau\ge4-c\).

**Target D (high-shear alternative without Einstein or bounded-geometry input).** Write the diagonal problem as a control system on 1-jets,
\[
J'=F_E(J)+G(J)\,\mathrm{Ric}^\circ,
\]
with \(\mathrm{Ric}^\circ_{tt}=G_{tt}(J)-6\) and running cost \(\frac W4|\mathrm{Ric}^\circ|^2\). Define the prefix and suffix value functions \(V_{\rm pre}(J)\) (from the bolt) and \(V_{\rm suf}(J)\) (to the CH end). Then:
- \(\alpha^{\rm diag}_{\rm cell}=\inf_J[V_{\rm pre}+V_{\rm suf}]\), since \(C^1\) gluing preserves \(s\equiv-24\) a.e. and \(L^2\) Ricci.
- Every \(\Phi\) satisfying \(\Phi'\le\frac W4|\mathrm{Ric}^\circ|^2\) along all admissible trajectories gives \(V\ge\Delta\Phi\). The charges \(\mathfrak b_\pm\) are such subsolutions, and the value function is the maximal one.

The missing statement is a dichotomy for small-bolt near-minimizers:
- **(i)** the normalized jets remain in a compact subset of the union of the two charts up to the opening region; then Corollary B and the rescaled-limit argument of §1 apply; or
- **(ii)** jets diverge inside \(K_c\) along directions 1–3 of §5, and \(V_{\rm suf}\) (or \(V_{\rm pre}\)) has an explicit positive lower bound there.

The natural route to (ii) is a one-dimensional shadowing lemma. On an interval of length \(\theta r\),
\[
\int|\mathrm{Ric}^\circ|\,dt\le\sqrt{\widehat P}\,(\textstyle\int dt/W)^{1/2}\sim\sqrt{\widehat P}/r,
\]
so the normalized rates move by \(O(\sqrt{\widehat P})\) relative to the Einstein drift. Grönwall then makes low-action raw segments shadow Ricci-flat Bianchi I/II solutions: Kasner epochs and their curvature-mediated transitions. The Weyl energies \(\frac1{2\pi^2}\int|W^\pm|^2\) of those exact solutions are computable, and they supply the term \(\Psi\) that charges cannot see. Two points remain unproved and are what this route has to establish:
- the shadowing estimate near the Kasner singular directions, where the drift's Lipschitz constant grows like \(|\lambda|\);
- a lower bound for \(V_{\rm suf}\) on the minus-kernel ray, where both the entry and the CH tail have \(\mathfrak b_+\to-\infty\).

The exact-Einstein branch (Taub-bolt core, collapsed \(\Lambda\)-Taub–NUT neck, unstable \(q\)-mode) is the zero-cost trajectory of this same control system. It is the case \(\mathrm{Ric}^\circ\equiv0\) of Target D, not a separate theory.