# TTCS Independent Branch Record

```json
{
  "step_id": 43,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md",
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A01/workspace/scripts/step43_yamabe_lebrun_ledger.py",
    "Sessions/S1003A01/workspace/data/step43/ledger_x003_X128_N80000.json"
  ]
}
```

## Task

Check the mathematics of the new note Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md, against A02's Step-48 note (LeB_full, Theorem Y, Y0) and the script that produced the numbers. Specifically: (1) Is Proposition 43.1 correct — that maximizing LeBrun's Proposition-4 bound over the sign family a_eps=K+sum eps_i E_i gives Pi_g >= (K.c + sum|E_i.c|)^2/c^2 - A for every c in H^+_g, hence a LINEAR period term 2 sum|e_i|, e_i=E_i.K^+, improving A02's quadratic |K^-|^2+sum|E_i^+|^2; and the exact formulas K.c=A, E_i.c=sigma_i, c^2=A-|sigma|^2, e_i=sigma_i+(G sigma)_i when c=K-sum sigma_i E_i is SD-harmonic? Are the sign conventions (K.E_i=0, E_i^2=-1, monopole classes K +- E_i under the sign-family hypothesis) right? (2) Theorem 43.2 and the scalar consequence Delta V >= 4 pi^2 sum|e_i|. (3) Corollary 43.3: does the ledger really reproduce the first-order slope 6t/pi of the aligned Kahler law P=2(2pi+6t)^2+L/4 (profile Ric=-6g, sigma=3t/pi after rescaling psi=6 omega), including the Yamabe-volume upper estimate 16 hatV = Y^2 <= int s^2 and the Kahler integrals int s = -8pi^2(A+sigma), V=2pi^2(A-sigma^2)? Check c_1(M)=-(K+E) pairings. (4) Remark 43.4 smoothness/strictness argument. (5) The numerical ledger: the tail-free Yamabe-volume identity int s^2 - 576 hatV = int[e^2+48ev-1152v^3-576v^4] (profile scale, e=s+24, v=u-1, equation -6 Lap u + s u + 24u^3=0) and the conversions Ric=-g (g1=6g) giving Delta V = 36 dV_profile, D_W = deltaW + (2/3)DeltaV, Y0 in the form 8pi^2-P(hat g)=4 deltaW-(4/3)DeltaV; the LeBrun integrand (sqrt6|W+|_g - 12u^2)^2 dV_g; and the correction of A02's quoted split. (6) Theorem 43.5 (Ricci flow). Report errors with corrected formulas; do not restate correct parts at length.

## Output

# Verification memo: Step 43 (period-linear LeBrun ledger, Yamabe ledger, Ricci flow)

Most of the note is correct. There are four corrections:

- **Remark 43.4.** The derivative formula omits the Gram matrix \(G(0)\). The strictness conclusion still holds.
- **"Improving A02".** Proposition 43.1 does not dominate A02's quadratic bound for \(b^+\ge2\).
- **Volume discrepancy.** The note attributes the direct-vs-identity gap to error amplification. It is in fact a quadrature truncation, and this can be shown exactly.
- **Theorem 43.5(ii).** It rests entirely on what the adopted extension source literally proves. This needs to be confirmed.

## (1) Proposition 43.1

**Sign conventions.** With \(K_M=K+\sum E_i\), \(c_1(M)=-(K+\sum E_i)\), \(E_i^2=-1\) and \(K\cdot E_i=0\), the classes \(K+\sum\varepsilon_iE_i\) are the standard Seiberg–Witten basic classes of the blow-up. Here \(a_\varepsilon^2=A-k\). The overall sign of \(a\) is irrelevant to \((a^+)^2\).

**Main inequality.** The step \((a^+)^2\ge(a^+\cdot c)^2/c^2=(a\cdot c)^2/c^2\) is valid because \(a^-\cdot c=0\) and \(\mathcal H^+_g\) is positive definite.

- With \(\varepsilon_i=\operatorname{sgn}(E_i\cdot c)\) one gets \(|a\cdot c|\ge K\cdot c+\sum|E_i\cdot c|\).
- If \(K\cdot c<0\), choosing \(\varepsilon_i=\operatorname{sgn}(K\cdot c)\operatorname{sgn}(E_i\cdot c)\) gives the stronger \((|K\cdot c|+\sum|E_i\cdot c|)^2\). The stated form remains true in either case.

**The case \(c=K^+\).** We have \(K\cdot K^+=(K^+)^2=A+|K^-|^2\) and \((x+y)^2/x=x+2y+y^2/x\). This is correct.

**The case \(c=K-\sum\sigma_jE_j\).** The following are all correct:

- \(K\cdot c=A\), \(E_i\cdot c=\sigma_i\), \(c^2=A-|\sigma|_2^2\).
- \((A+s_1)^2/(A-s_2)\ge(A+2s_1)(1+s_2/A)\), which gives \(\Pi\ge 2|\sigma|_1+|\sigma|_2^2\).
- \(K^+=c+\sum\sigma_jE_j^+\), which gives \(e=(I+G)\sigma\).

Positivity of \(c\) on the exceptional curve matches the Kähler sign: \([\omega]/2\pi=K-\sigma E\) pairs to \(\sigma>0\) with \(E\).

One requirement concerns the Step-40/41 family: \([\psi]\) must be the class of a \(g\)-self-dual closed form for the metric whose \(\hat g\) is used. Self-duality is conformally invariant, so conformal rescalings are harmless.

**Correction: Proposition 43.1 does not uniformly improve A02.** The exact quantity is
\[
\Pi_g=\max_\varepsilon\Bigl[|K^-|^2+2\sum_i\varepsilon_ie_i+\Bigl|\sum_i\varepsilon_iE_i^+\Bigr|^2\Bigr].
\]
A02's bound is the average over \(\varepsilon\). The new bound is the projection onto \(\mathbb RK^+\).

- **When \(b^+=1\).** \(E_i^+=(e_i/(K^+)^2)K^+\), so \(\sum|E_i^+|^2\le(\sum|e_i|)^2/(K^+)^2\). The new bound dominates.
- **When \(b^+\ge2\).** Components of \(E_i^+\) orthogonal to \(K^+\) have \(e_i=0\) but \(|E_i^+|^2>0\). They are charged only by A02's quadratic term.

The correct combined statement is
\[
\Pi_g\ge|K^-|^2+\max\Bigl(2\sum_i|e_i|+\Bigl|\sum_i\operatorname{sgn}(e_i)E_i^+\Bigr|^2,\ \sum_i|E_i^+|^2\Bigr).
\]

## (2) Theorem 43.2

**Re-derivation of (L).**

- At \(s\equiv-4\), \((4+w)^2=3w^2+24-2(w-2)^2\).
- Gauss–Bonnet gives \(P=\tfrac23\int w^2+\tfrac43V-8\pi^2(A-k)\).
- Substituting into \(\int(4+w)^2\ge72\pi^2(A+\Pi)\) gives \(P+4\Delta V\ge8\pi^2k+16\pi^2\Pi+\tfrac49\int u^2\).

This is (L) exactly. The scalar estimate \(16\hat V\ge32\pi^2(A+\Pi)\) gives \(\Delta V\ge2\pi^2\Pi\). Both inequalities use the same maximizing \(\varepsilon\), which is legitimate.

**The rewrite.** \(4\Delta V-16\pi^2\Pi=4\Delta V_{\rm free}-8\pi^2\Pi\), combined with \(\Pi\ge2\sum|e_i|\), gives the boxed inequality and \(\Delta V\ge4\pi^2\sum|e_i|\). Both are correct.

**Recommendation for multi-cell use.** For \(k>1\) cells with \(c=K-\sum\sigma_iE_i\), use the \(c\)-form \(\Pi\ge2|\sigma|_1+|\sigma|_2^2\) directly. The reason is that \(e=(I+G)\sigma\) does not imply \(|e|_1\ge|\sigma|_1\) componentwise. Only \(\sigma\cdot e\ge|\sigma|_2^2\) holds.

This matters for §3 "Rotations": the conversion \(|e|\to3|p|/\pi\) is valid as written for one cell (\(e=\sigma(1+G)\), \(G\ge0\)). For several cells, use \(|\sigma|_1\).

The arithmetic in §3 is correct:

- \(4\Delta V\ge\text{saving}+\text{LeB}+32\pi^2|e|\), i.e. \(12|p|/\pi\) in \(8\pi^2\) units.
- \(|p|\le0.204\pi/12=0.0534\).

## (3) Corollary 43.3

**Scale and period.**

- With \(g_1=6g\), exceptional area \(6t\), and \([\omega_1]/2\pi=K\) on the KE host, we get \(\sigma=6t/2\pi=3t/\pi\). Correct.
- Since \(G\ge0\), \(e=\sigma(1+G)\ge\sigma\), so the ledger slope \(2\sigma=6t/\pi\) is legitimate.

**Kähler integrals.**

- \(\int s\,d\mu=2\int\rho\wedge\omega=8\pi^2c_1\cdot c\).
- \(c_1\cdot c=-(K+E)\cdot(K-\sigma E)=-(A+\sigma)\).
- \(V=2\pi^2c^2=2\pi^2(A-\sigma^2)\).

All correct.

**Yamabe estimate.** For \(Y<0\), \(Y[g]^2\le\int s_g^2\) is valid (LeBrun), and \(Y^2=16\hat V\) at \(s=-4\). Then \(\int s^2=(\int s)^2/V+L_s=32\pi^2(A+\sigma)^2/(A-\sigma^2)+L_s\), which gives \(4\Delta V_{\rm free}\le L_s/4+O(\sigma^2)\). Correct.

**Cross-check against the exact Kähler identity.** The Kähler identity \(4\pi^2c_1^2=\int s^2/8-P/2\) gives exactly
\[
P_{\rm K}=8\pi^2\Bigl[1+\frac{2A\sigma+\sigma^2+A\sigma^2}{A-\sigma^2}\Bigr]+\frac{L_s}{4}.
\]
- As \(A\to\infty\) this tends to \(8\pi^2(1+\sigma)^2+L_s/4=2(2\pi+6t)^2+L/4\). This identifies the Step-8 law as the large-host limit.
- The first-order slope matches the ledger's \(8\pi^2(1+2\sigma)-L_s/4\).
- The ledger sits \(L_s/2\) below the law.

So "exactly the first-order slope" is correct. The \(L\)-terms enter with opposite signs, which should be stated.

## (4) Remark 43.4

The ingredients are correct:

- Nonnegativity of each \(F_\varepsilon\) (LeBrun applied to each monopole class \(a_\varepsilon\)).
- Smoothness (uniqueness of the Yamabe metric for \(Y<0\) plus the implicit function theorem; smooth harmonic projections).
- \(F_\varepsilon(0)=F_{-\varepsilon}(0)\). This holds because \(e(0)=0\) and \(|\sum\varepsilon_iE_i^+|^2\) is even in \(\varepsilon\).

**Correction: the derivative formula.** Since \((a_\varepsilon^+)^2-(a_{-\varepsilon}^+)^2=4\sum\varepsilon_ie_i\) and \(e'(0)=(I+G(0))\sigma'(0)\) (the \(G'\) term multiplies \(\sigma(0)=0\)),
\[
F_\varepsilon'(0)-F_{-\varepsilon}'(0)=-64\pi^2\sum_i\varepsilon_i\big[(I+G(0))\sigma'(0)\big]_i .
\]
- The note's formula holds only if \(E_i^+=0\) at \(\psi=0\). That is automatic when \(b^+=1\) but not in general.
- Because \(I+G(0)\) is positive definite, the qualitative conclusion (\(\sigma'(0)\ne0\Rightarrow F_\varepsilon(0)>0\) for suitable \(\varepsilon\)) survives.

**The quantitative bound needs restating.**

- With \(S=\tfrac12(F_\varepsilon+F_{-\varepsilon})\) and \(D=\tfrac12(F_\varepsilon-F_{-\varepsilon})\), the bound \(S\ge|D|\) holds.
- \(S'(0)\) need not vanish, but choosing the sign of \(\psi\) with \(S'(0)\psi\le0\) removes it.
- The remainder is \(O(\psi^2)\), not \(o(\psi^2)\). Both \(S''\) and \(D''\) must be absorbed into \(\Lambda\).

The correct statement is
\[
\max_\varepsilon F_\varepsilon(0)\ge\frac{(32\pi^2|(I+G(0))\sigma'(0)|_1)^2}{2\Lambda},
\qquad \Lambda\ge\sup|S''|+\sup|D''|
\]
on an interval containing \(\psi_*=a/\Lambda\). Also, \(F_\varepsilon(0)\) depends on \(\varepsilon\) through \(|\sum\varepsilon_iE_i^+|^2\) when \(G(0)\ne0\).

## (5) Numerical ledger

**Identity.** Write \(s=e-24\), \(u=1+v\). Then
\[
s^2-576u^4-[e^2+48ev-1152v^3-576v^4]=-48\bigl[e(1+v)+48v+72v^2+24v^3\bigr]=-48(su+24u^3).
\]
Its integral vanishes by the integrated equation \(\int(su+24u^3)=6\int\Delta u=0\). The identity is exact.

The code's `dV6_id=(S24rel−Xpos)/24` equals \(\hat V-V_{CH}\). The exterior integrand is \(O(v^3)\), so truncating it is harmless.

Gauss–Bonnet plus conformal invariance of \(\int|W^+|^2\) gives \(P(g)-P(\hat g)=(\int s^2-576\hat V)/12=2X_{\rm pos}\). The conformal formula \(24\int|\nabla u|^2+3\int(\Delta u/u)^2\) reduces to the same expression after integration by parts and use of the equation.

**Correction: the cause of the direct-vs-identity gap.** The gap is not error amplification of \(v(X)\). It is exactly
\[
\Delta V_{\rm direct}-\Delta V_{\rm id}=36\cdot\frac{48R}{576}=3R_{\rm trap},
\]
where \(R_{\rm trap}\) is the trapezoid integral of the equation.

- Numerically, \(0.0532417-0.0530963=1.4540\times10^{-4}=3\times4.8468\times10^{-5}\).
- \(R_{\rm trap}\ne0\) because `I()` stops the exterior at \(x=100X\) (index `k`), while the solve extends to \(10^4X\). \(R_{\rm trap}\) is \(6\times\) the flux of \(u\) through \(x=100X\).
- The physical tail accounts for the gap. With \(v=v_X(x/X)^{-1-\sqrt3}\) and \(\rho\simeq x/2\),
\[
36\cdot\tfrac14\int_{100X}^\infty4v\rho\,dx=36\,v_Xx^2\big|_{X}\cdot\frac{100^{1-\sqrt3}}{2(\sqrt3-1)}\approx-1.44\times10^{-4}.
\]
- The direct volume omitted a genuine \(O(v_XX^2)\) tail. That tail is real, not error.
- Independent confirmation: `Yamabe_ineq_S24_minus_24dV = −9.6e−5` with the direct volume violates \(\int s^2\ge Y^2\). With the identity volume the corresponding quantity is \(X_{\rm pos}=9.4\times10^{-7}\ge0\).

**Remaining uncertainty.** The finite-volume integrated residual `int_equation_fv = 2.1e−6` should vanish for a converged conservative scheme. Newton stalled at \(|dv|=2.5\times10^{-14}\) after the full 60 iterations, and `residual_max = 0.24` is a roundoff-dominated row residual at the bolt. Through \(3R\), this puts an uncertainty of about \(6\times10^{-6}\) on \(\Delta V\) and about \(2.5\times10^{-5}\) on \(4\Delta V\). That is irrelevant to the conclusions, but the sixth digits in the table are not significant.

**JSON headline fields.** The fields `DeltaV`, `D_W`, `Y0_residual=1.9e−4` and `F_LeB=0.20433` are direct-volume values superseded by the `*_identity` fields. With identity values, (Y0) closes:
\[
4(0.0187836+\tfrac23\cdot0.0530963)-4\cdot0.0530963=0.0043391 .
\]

**Conversions.** These are all correct:

- \(D_W=\delta W+\tfrac23\Delta V\), because \(|W^+|^2=\tfrac23\) on the CH ball and \(\int|W^+|^2\) is conformally invariant.
- (Y0) relative to the CH ball is \(4\delta W-\tfrac43\Delta V\).
- In the code, \(24u^4-|W^+|_g^2\) is correct, using \(36\cdot\tfrac23=24\) and \(|W|^2_{\hat g_1}d\mu_{\hat g_1}=|W|_g^2d\mu_g\).
- The LeBrun integrand: \((\sqrt6|W|_g/(6u^2)-2)^2\cdot36u^4=(\sqrt6|W|_g-12u^2)^2\), which vanishes on CH.
- \(\int|W^-|^2=\tfrac32-\delta W\) holds by relative signature.

The A02 correction is right:

- \(0.07513=4\delta W\) and \(0.07080=\tfrac43\Delta V=48\,\Delta V_{\rm profile}\).
- The ratio \(0.2124/0.00434\approx49\) and the efficiencies \(0.0204\) and \(0.0172\) check.

The x₀ = .038 column is internally consistent: \(4\delta W-\tfrac43\Delta V=0.0047129\) against a saving of \(0.0047127\). F_LeB and F_Y reproduce to \(10^{-6}\).

**Minor discrepancy.** The JSON Gauss–Bonnet residual is \(-5.9\times10^{-9}\), whereas the note says \(2\times10^{-8}\). The note's "stable in \(N\)" statement does not cover the exterior extent `--ext`, which is the parameter that controls the tail.

## (6) Theorem 43.5

**Part (i): flow identities.** Under \(\partial_tg=-2\operatorname{Ric}+\tfrac12\bar sg\), direct differentiation gives \(d\!\int s=2P+\tfrac12\bar s^2V-\tfrac12\int s^2\). So \(\bar s'=(2P-L_s/2)/V\). Correct.

**Part (i): the rest of the argument.**

- Bounded \(s\) gives bounded \(\bar s\). Then \(2\int_0^TP=V\Delta\bar s+\tfrac12\int L_s\), which is finite once \(\int L_s<\infty\).
- The bound \(\int_0^\infty L_s<\infty\) is the imported Ishida / Fang–Zhang–Zhang-type input. It is consistent with the maximum-principle behaviour of \(s_{\min}\) (nondecreasing while \(s_{\min}<0\)), but I cannot check it from the supplied files.
- \(S\ge Y[g]^2\ge Y(M)^2>0\) is correct, because \(Y[g]\le Y(M)<0\).
- The step \(E(g(t_j))\to0\) is correct provided \(\mathscr D=E=(4P+L_s)/(P+S/4)\). That definition is not in the supplied files.

**Part (ii): the extension input.** The normalized-to-unnormalized reparametrization with bounded \(\bar s\) on a finite interval is correct. The conclusion, however, needs a theorem stating that a Ricci flow on a closed 4-manifold with bounded scalar curvature on \([0,T)\), \(T<\infty\), extends past \(T\).

The 4D bounded-scalar results I know (Bamler–Zhang; Simon) give \(L^2\) curvature control and \(C^0\) orbifold limits at \(T\). Those do not exclude a singular time. If "family 351, Thm 1.1" proves only orbifold convergence, part (ii) does not follow, and the theorem then has to allow a finite-time singularity with bounded \(s\). The literal statement of that source decides part (ii); it is the one external dependence of the theorem. Part (i) is independent of it.