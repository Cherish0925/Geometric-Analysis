# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md",
    "Knowledge/objects/papers/Degenerating-Kähler-Einstein-cones-locally-symmetric-cusps-and-the-Tian--adb04d311c2f--499d8f08a8b4/object.md",
    "Knowledge/objects/papers/Invariants-of-some-compactified-Picard-modular-surfaces-and-applications--a2801b1afe2c--6270e445600c/object.md"
  ]
}
```

## Task

Check the proposed corrected separated-depletion theorem and the ramification-cap realization logic. Context: We study the two-parameter ramified Kähler--Einstein surgery law for Einstein-defect gaps on four-manifolds. Step 33 left a partial anti-self-dual retention argument; the current strategist note proposes that if U contains the surgery regions and N is a disjoint topology-preserving modification region with exact KE boundary matching, then retaining the global scalar variance term gives a clean lower bound: for t=theta_0 in [0,1/3], the numerator of equation (4.1) is bounded below by -16 B_U^0 - 48 t B_N^0, hence E >= 4t/(1+t)-o(h) when Delta/A -> 0 and B_U^0=o(Q), even if Delta/Q grows. Peer Step38 adds the local identity on a ramification neighbourhood with matching boundary: Delta_N B = P_N/4 - Delta_N S/48, or in scalar -4 normalization Delta_N B=P_N/4-Delta_N V/3, so flux alone has no sign. Please read the context and give a mathematical verification memo: identify exact assumptions needed, check the algebra and scale estimates, distinguish what this closes from unrestricted competitors, and assess the bridge from the exact Calabi cap model to actual ramified towers (Biquard--Guenancia only gives C0/quasi-isometric model comparison in the negative setting near D unless further elliptic/local chart work is supplied).

## Output

# Verification memo: separated anti-self-dual depletion and the ramification-cap bridge

## Summary

- **Separated theorem.** It is correct as stated. It needs one input beyond what Step 33 used: LeBrun's scalar estimate applied to the *restored* metric \(g_1\). Its error term is explicit and does not depend on \(r\). Under the same hypotheses it removes both terms Step 33 left open.
- **What it does not give.** It is a statement about one class of competitors, not about \(\alpha(M_m)\). The all-metric lower bound is still Theorem A.
- **Step 38 identity.** It is correct. In the separated setting it shows that depletion acts only through the global normalization \(R\), at rate \(t\).
- **Cap model.** The exact Calabi-cap computation checks out completely. The separated theorem does not need it. The interacting-cell problem does, and for that BG's Lemma 4.4 (uniform \(C^0\)) has to be upgraded to curvature-level closeness on bounded neighbourhoods of the ramification curves \(D'\). Section 5 gives a concrete route and shows why that upgrade is enough for \(o(\Delta)\) localization.

## 1. A closed form that organizes everything

Write \(T=\int s\). Since \(|\mathrm{Ric}-\lambda g|^2=|\mathrm{Ric}^\circ|^2+(s-4\lambda)^2/4\), minimizing over \(\mu=1/\lambda\) gives \(\mathcal E=4-T^2/(VR)\). Using \(T^2/V=S-L_s\):
\[
\boxed{\mathcal E=\frac{4P+L_s}{R}},\qquad R=P+\tfrac S4 .
\]
Hence, for any \(t\),
\[
(1+t)R\Bigl(\mathcal E-\tfrac{4t}{1+t}\Bigr)=\mathcal N:=4P-tS+(1+t)L_s .
\tag{A}
\]

**Check of (1.1).** It follows from
- \(P=4\int|W^+|^2+S/12-8\pi^2T_+\),
- \(\int|W^+|^2=B+12\pi^2\tau\),
- \(\tau(M)=(A-2\Delta)/9-k\) and \(T_+=A-k-4\ell\).

The \(A\)-terms combine to \(-(8\pi^2/3)A=-S_0/12\). The \(\Delta\)-term is \(-4B_\Delta\). The \(k,\ell\)-terms give \(8\pi^2(4\ell-5k)=8\pi^2A\theta_0\). Substituting into (A), the \(32\pi^2At\) terms cancel and (4.1) is reproduced exactly.

**Consistency checks.**
- KE normalization: \(\mathrm{Vol}=2\pi^2A\) gives \(S_0=32\pi^2A\). At \(t=0\) on \(\bar X\), \(P=0\) forces \(B=B_\Delta\).

**Correction to Step 33.** At \(t=0\), \(\mathcal N=4P+L_s\). So on \(\bar X\),
\[
S-S_0=12P-48(B-B_\Delta)
\]
is an identity, not a consequence of KE minimality. The "\(-3L_s\)" in Step 33's inequality is superfluous.

## 2. The separated-depletion theorem

### Hypotheses (exactly what the proof uses)

- **(H1) All-metric scalar budget.** \(S(g')\ge32\pi^2p\ge S_0\) for every smooth metric \(g'\) on \(M_m\). This is LeBrun's estimate with \(p\ge A\), as in Step 32.
- **(H2) Regions.** \(U\subset M\) is a union of compact regions containing all surgery topology. \(N=M\setminus U\) may be taken to be the whole complement, so no separate "exterior" is needed. \(N\) is identified with a region \(N_0\subset\bar X\), and \(U\) replaces \(U_0=\bar X\setminus N_0\).
- **(H3) Collar matching.** \(g=g_{KE}\) on an open collar of \(\partial N\). Then:
  - \(g_1\) (\(=g\) on \(U\), \(g_{KE}\) on \(N\)) is a smooth metric on \(M\);
  - \(g'\) (\(=g\) on \(N\), \(g_{KE}\) on \(U_0\)) is a smooth metric on \(\bar X\).
- **(H4)** \(0\le t=\theta_0\le1/3\), that is, \(\theta\le1/6\) and \(h(1-6\theta)\le1/3\).

### Proof

Use (A) and \(P_{\rm ext}=0\). Write \(\Delta_N S=S_N(g)-S_{N_0}(g_{KE})\) and \(\Delta_N B\) similarly. Then
\[
\mathcal N(g)=\underbrace{4P_U(g)-tS(g_1)}_{(\mathrm I)}+\underbrace{4P_N(g)-t\,\Delta_NS}_{(\mathrm{II})}+(1+t)L_s(g).
\]

**Term (I).** Since \(P(g_1)=P_U(g)\), identity (1.1) applied to \(g_1\) gives
\[
(\mathrm I)=\tfrac{1-3t}{3}\bigl(S(g_1)-S_0\bigr)+16\bigl(B_U(g)-B_U^0\bigr).
\]
By (H1) for \(g_1\), \(S(g_1)-S_0=\Delta_US\ge0\). Since \(B_U(g)\ge0\), \((\mathrm I)\ge-16B_U^0\).

**Term (II).** Compare \(g'\) with \(g_{KE}\) on \(\bar X\). They have the same topology and identical integrands off \(N_0\), so the Euler and signature integrals over \(N\) agree. This gives Step 38's identity
\[
\Delta_NB=\tfrac14P_N-\tfrac1{48}\Delta_NS .
\]
Hence \(\Delta_NS=12P_N-48\Delta_NB\le12P_N+48B_N^0\), and
\[
(\mathrm{II})\ge4(1-3t)P_N-48tB_N^0 .
\]

**Conclusion.**
\[
\mathcal N(g)\ge-16B_U^0-48tB_N^0+\tfrac{1-3t}{3}\Delta_US+4(1-3t)P_N+(1+t)L_s(g).
\]
The extra positive terms are retained here for near-extremal analysis.

### Normalization and scale

By (H1) for \(g\), \(R\ge S/4\ge8\pi^2A\). Therefore
\[
\mathcal E(g)\ \ge\ \frac{4t}{1+t}-\frac{2B_U^0+6t\,B_N^0}{\pi^2A(1+t)}
\ \ge\ \frac{4t}{1+t}-\frac{2B_U^0}{\pi^2A}-\frac{16\,t\,\Delta}{A}.
\]
The second inequality uses \(B_N^0\le B_\Delta=8\pi^2\Delta/3\).

Since \(t=h(1-6\theta)\) and \(4t/(1+t)=4h(1-6\theta)+O(h^2)\), the error is \(o(h)\) exactly when both
- \(\Delta/A\to0\), and
- \(B_U^0=o(Q)\).

The bound holds for every \(r=\Delta/Q\), including \(r\to\infty\).

For CH-close sites, \(B_U^0\le C\varepsilon_m^2Q\). This uses only BG's Theorem 1.1 (\(C^\infty_{\rm loc}\) convergence on the fixed marked compact set), not the cap model. Shrinking handles contribute \(B_U^0\to0\), given bounded KE curvature.

### Why Step 33's two leftover terms disappear

- **Scalar-variance comparison.** In form (A), \(L_s\) enters only as \((1+t)L_s(g)\ge0\). The quantities \(L_s(g_1)\) and \(L_s(g')\) never appear.
- **The \(O(h)\cdot\Delta S_N\) correction.** It is priced by the local identity at rate \(48t\).

## 3. Cross-checks and structure

- **Recovers Theorem A.** Drop the local identity and use only \(S(g)\ge S_0\) and \(B\ge0\). Then \(\mathcal N\ge-16(B_U^0+B_N^0)\ge-16B_\Delta\), so
  \[
  \mathcal E\ge4h(1-6\theta)-\tfrac{16}{3}rh=\tfrac43(3-\sigma)h ,
  \]
  which is exactly Theorem A's explicit branch. The whole gain is that background ASD energy outside \(U\) costs \(48t\) instead of \(16\).
- **Dilution interpretation.** Separated depletion changes \(\mathcal N\) by \(4(1-3t)P_N+48t\Delta_NB\). It can only enlarge \(R\) through the Weyl–volume exchange; at \(s\approx-4\), \(\Delta_NB=P_N/4-\Delta_NV/3\). Its first-order effect is \(\delta\mathcal E\approx-\mathcal E\,\delta S/(4R)\), proportional to \(\mathcal E\sim t\). It has no topological coupling to the surgery.
- **The \(48t\) term is never attained.** Equality would need \(P_N=0\), \(B_N(g)=0\) and \(L_s=0\). Then \(g\) would be Einstein on \(N\) and equal to \(g_{KE}\) on the collar, so by unique continuation \(g=g_{KE}\) on \(N\). That gives \(B_N=B_N^0\), a contradiction unless \(B_N^0=0\). This is irrelevant asymptotically.
- **Theorem B's metrics lie in the class.** The cutoff \(g_{CH}+\chi(g_m-g_{CH})\) is exactly \(g_m\) on the outer subannulus. So within the class,
  \[
  4h(1-6\theta)-o(h)\ \le\ \mathcal E_{\min}\ \le\ 4h(1-\eta\theta).
  \]
  The \(\theta\)-tariff is still open; the \(r\)-direction is now flat on both sides.
- **Approximate collars.** If \(g\) is only \(\delta\)-close to \(g_{KE}\) in \(C^2\) on uniform collars, interpolate to build \(g_1\) and \(g'\).
  - Transgression differences are \(O(\delta)\) per collar.
  - \(P\) and \(S\) collar changes are \(O(\delta^2)\) and \(O(\delta)\).

  The total extra error is \(O(\delta Q)\) in \(\mathcal N\), which is still \(o(h)\) after dividing by \(R\) if \(\delta\to0\).

## 4. What remains open for unrestricted competitors

\(\alpha(M_m)\) is an infimum over all metrics. The theorem bounds only metrics that admit collars, near the surgery, on which they are \(C^2\)-close to \(g_{KE}\). Three mechanisms are untouched.

1. **Interacting placement.** Surgery inside or overlapping ramification neighbourhoods makes \(B_U^0\) comparable to \(B_\Delta\), and the rate \(16\) returns. The local form on \(U\) is
   \[
   \Delta_US=12P_U-48\Delta_UB-96\pi^2(4\ell-5k).
   \]
   It shows that a cell depleting cap \(W^-\) by \(\delta\) at fixed \(\Delta_US\) lowers \(P_U\) by \(4\delta\). This exchange rate is exactly the open interacting question, and it is the sole remaining source of Theorem A's \(r\)-loss.
2. **No decoupling.** A near-minimizer has \(P=O(Q)\) spread over volume \(\asymp A\). It may be locally close to *some* Einstein metric without being close to \(g_{KE}\). The monopole estimate sees classes, not locations, so nothing forces the exceptional or handle charge to localize.

   A decoupling lemma would close this: every \(g\) with \(\mathcal E(g)\le Ch\) can be replaced, at cost \(o(h)\), by a metric with \(o(1)\)-KE collars. Such a lemma needs both concentration of the topological charge and identification of thick regions with \(g_{KE}\), and the second is a rigidity input not presently available.

   For \(\sigma\ge4+c_0\), Einstein metrics are not excluded at all, and an Einstein metric is in any case outside the class by unique continuation. The theorem is therefore best read as a structural necessity: any family with \(\mathcal E/h<4(1-6\theta)-o(1)\) has no approximately-KE collars around localized CH-site surgery.
3. **\(\theta>1/6\).** Here \(t<0\) and the target \(4t/(1+t)\) is \(\le0\), so the statement is vacuous.

## 5. The Calabi-cap model and its bridge to actual towers

### Model checks

All of the following verified directly.

- **Calabi ansatz.** In BG's convention \((\varphi')^{3}=a+be^{\varphi}\) with \(\tau=\varphi'\), one gets \(\Theta=2\varphi''=\tfrac23\tau^2-\tfrac{2a}{3\tau}\). So \(c=2a/3\), and \(c=0\) is the cusp of (4.5).
- **Closing.** \(\tau_0^3=3c/2\) and \(\Theta'(\tau_0)=2\tau_0\). Smoothness requires \(\eta\)-period \(2\pi/\tau_0\). The self-intersection is \(-e\) with \(e=a\tau_0/2\pi\), and the area of \(D'\) is \(2\pi e\).
- **Weyl energy.** With \(d\mu=\tau\,dx\,dy\,d\tau\,d\psi\),
  \[
  \int|W^-|^2=\frac{2\pi a}{\tau_0}\cdot\frac{6c^2}{4\tau_0^4}=\frac{8\pi^2e}{3}.
  \]
  Also \(|W^-|^2=8/3\) on \(D'\), \(|W^+|^2=2/3\), and since \(d\simeq\sqrt{3/2}\log\tau\), \(|W^-|^2\sim e^{-2\sqrt6 d}\).
- **Topology.** \(\sum_ce_c=-d\sum\beta^2D_\lambda^2=\Delta\), and from Prop. 3.2 of Džambić, \(\Delta=-T^2\).

### What BG actually supplies

- **Theorem 1.1.** \(C^\infty_{\rm loc}\) convergence on fixed compact subsets of \(X^\circ\). This is enough for CH-site placement and hence for \(B_U^0=o(Q)\).
- **Theorem 4.5.** Only quasi-isometry to explicit forms.
- **Lemma 4.4.** The sharpest statement: \((1-\varepsilon_\beta)\omega_\beta\le\hat\omega_\beta\le(1+\varepsilon_\beta)\omega_\beta\) uniformly on all of \(U^*\). Both are Kähler–Einstein forms on the same complex manifold; the cusp neighbourhood is biholomorphic to the disc bundle by (4.5). Moreover \(dd^cF=\hat\omega_\beta-\omega_\beta\) and \(\|F\|_\infty\to0\).

None of these gives curvature closeness near \(D'\).

### Upgrade route

1. On the ramified cover, \(\hat\omega=\omega_{\rm model}+dd^cF\) solves a complex Monge–Ampère equation of the form \((\omega_{\rm model}+i\partial\bar\partial F)^2=e^{F}\omega_{\rm model}^2\), up to BG's normalizations. It has a uniform \(C^0\) bound and a uniform Laplacian bound (from the quasi-isometry).
2. The model has bounded curvature (BG Lemma 3.1, flat \(D\)). Thin tori \(D'\) can be handled by passing to local universal covers of tubular neighbourhoods, which gives quasi-coordinate charts of uniform size.
3. Evans–Krylov and Schauder estimates then give uniform \(C^{k,\alpha}\) bounds on \(F\). Interpolation with \(\|F\|_\infty\to0\) gives \(\|\hat\omega-\omega_{\rm model}\|_{C^k}\to0\) on caps.
4. The points to write out are:
   - uniformity of \(\varepsilon_\beta\) for tuples \(\beta\to0\);
   - pulling Lemma 4.4 back through the \(v\)-fold branched cover;
   - chart construction near \(D'\).

### Why closeness on bounded caps suffices for localization

Fix \(R_0\) and let \(\mathcal C_{R_0}\) be the \(R_0\)-neighbourhoods of the curves \(D'_c\), whose volume is \(\lesssim e_c f(R_0)\). Curvature \(\varepsilon\)-closeness there gives
\[
\int_{\mathcal C_{R_0}}|W^-|^2\ \ge\ \tfrac{8\pi^2}{3}\Delta\,\bigl(1-\rho(R_0)\bigr)-O\bigl(\varepsilon f(R_0)\Delta\bigr),
\]
where \(\rho(R_0)\to0\). The exact topological total \(B_\Delta\) and \(|W^-|^2\ge0\) then force the energy outside \(\mathcal C_{R_0}\) to be \(o(\Delta)\) along a diagonal \(R_0\to\infty\), \(\varepsilon\to0\).

Pointwise \(o(1)\) closeness on the whole cusp region would not suffice, because it carries volume \(\asymp A\gg\Delta\). This is why closeness on bounded caps, combined with the exact total, is the right target.

### Uses of the upgrade

- Step 33's "all of \(B_\Delta\) inside unit neighbourhoods of \(D'\)" for actual towers.
- Cap-placed cells with exact-model collars: the first-order neutrality of §5 transfers with \(\kappa=g_{\rm actual}-g_{\rm model}\), giving errors \(O(\varepsilon^2)\) per site over \(\asymp\Delta\) sites.

### Tower realization

The principal congruence subgroups \(\Gamma_K(p^n)\subset\Gamma_K(p^{n_0})\) (\(p\) odd, inert) are normal. This gives Galois covers of a fixed neat base with equal ramification orders \(v\sim p^{n-n_0}\to\infty\), as BG §4.3 needs. Using \(\vartheta=p^n\) and Lemma 2.4:
- \(A\asymp p^{8n}\);
- \(\Delta=h_K\eta_K[\Gamma_K:\Gamma_K(p^n)]/\vartheta^2\asymp p^{6n}\).

So \(\Delta/A\to0\), which is the hypothesis the separated theorem needs.