# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md",
    "Sessions/S1003A02/workspace/scripts/scalar_normalized_constraint.py",
    "Sessions/S1003A02/workspace/scripts/chiral_two_sided_bound.py"
  ]
}
```

## Task

Independently verify Lemmas V, N, and W in the Step-31 note. Derive all constants and signs from the stated diagonal chiral and Ricci identities. In particular: (i) determine whether the pointwise conclusion dP_hat/dt = b'_pm + nonnegative density and the stronger integral max{0,b_+',b_-'} bound are valid simultaneously; (ii) check b_- normalization at the O(-1) bolt; (iii) check C identities and whether scalar -24 is legitimately without loss for the exact-ended diagonal infimum; (iv) inspect Lemma W's first-barrier proof including the case S(T)>A, and state a corrected rigorous version if needed. Distinguish exact theorem from numerical support.

## Output

# Verification memo: Lemmas V, N, W of Step 31

## Summary

- **Lemma V** is correct. Both chiral identities hold at once, so \(\widehat P'\ge\max\{0,\mathfrak b_+',\mathfrak b_-'\}\) pointwise. The dropped \(s^2\) term gives a strictly stronger exact bound (§1c).
- **The bolt charge \((1,7)\)** is correct. It requires the smoothness conditions \(a_f'(0)=a_g'(0)=0\); arbitrary triaxial jets do not give it.
- **Lemma N(1)–(4)** are correct. I re-derived them by hand, and (2) follows directly from \(\operatorname{div}G=0\).
- **The scalar \(-24\) reduction** is valid for lower bounds. It does not preserve an exact end, only an asymptotic one, which is enough. It does not preserve the bolt radius, which affects the Theorem L programme.
- **Lemma W** is true as stated, including the case \(S(T)>A\). The proof's monotonicity step needs a last-crossing argument; a rigorous version is given in §4 together with a cleaner cost form.

## 1. Lemma V

### (a) Density and simultaneity

Step 27 gives \(\mathfrak s'=\tfrac12W(B_A-B_B)\) and \(\mathfrak b_\pm=\mathfrak b\mp\mathfrak s\). It also gives
\[
\widehat P'=\mathfrak b'+\tfrac12W(B_A+B_B)+\tfrac{Ws^2}{48}.
\]
The last term is \(\frac1{96\pi^2}s^2\cdot2\pi^2W\). Subtracting the two transgressions gives
\[
\widehat P'=\mathfrak b_+'+W B_A+\tfrac{Ws^2}{48}=\mathfrak b_-'+W B_B+\tfrac{Ws^2}{48}.
\]

- So \(\omega_+=W\operatorname{tr}W_A^2+Ws^2/48\) and \(\omega_-=W\operatorname{tr}W_B^2+Ws^2/48\). Both are \(\ge0\).
- The bracket "\(|W^\pm|^2\)-density" written in the note should be read with exactly these normalizations; the prefactor \(W/(2\pi^2)\) there is not literally right.
- These are two equalities for the same \(\widehat P'=W|\mathrm{Ric}^\circ|^2/4\ge0\). Hence \(\widehat P'\ge\max\{0,\mathfrak b_+',\mathfrak b_-'\}\) pointwise. There is no conflict between the two chiralities.
- The integral inequality and the bound \(\int\max\{\cdot\}\ge\max\{V^+(\mathfrak b_+),V^+(\mathfrak b_-)\}\) follow. The sup-increment forms follow as well.
- **Regularity needed:** \(\mathfrak b_\pm\) must be absolutely continuous up to the bolt. They are polynomial in \(a_i'\) and \(\gamma_i\), and \(\gamma_f,\gamma_g\to0\) continuously at a smooth bolt (§2). So this holds.

Burns is a consistency check:
- \(+\) identity: \(2-1=1\), with \(B_A=s=0\).
- \(-\) identity: \(2-7+6=1\), using \(\int WB_B=6\).

### (b) Consequences 1–3

**Consequence 1** is a direct application.

**Consequence 2.** The value \(\mathfrak b_-=8.54957\) is an exact algebraic function evaluated at one specific Step-30 state. The bound \(\ge1.5496\) is therefore exact for every path from an \(O(-1)\) bolt through that state; interval evaluation would certify it trivially. It does not cover all high-shear escapes. A shear path that keeps \(\mathfrak b_-<7+p_*\) is not covered, which the note itself states at the end of §5.

**Consequence 3.** The threshold works out as follows:
- The condition is \(2-9\sinh^4\tau<-2+p_*\), i.e. \(\sinh^4\tau>(4-p_*)/9=0.33379\).
- This gives \(\sinh\tau>0.76010\), i.e. \(\tau>0.7012\). This matches the lower end \(0.701\) of the numerical CH radius window.
- The input \(\mathfrak b_+\approx-2\) at a "collapsed section" is the Step-27 value only for controlled near-biaxial Hopf collapse with bounded normalized jets. Step 27 states that anisotropic collapsed jets carry shear corrections.
- The reduction is exact if "collapsed section" is defined by the charge, \(\mathfrak b_+\le-2+\delta\), rather than by geometry. Otherwise the shear-collapsed states are not yet in the reduction.

### (c) Exact strengthening from the dropped \(s^2\) term

In the class \(s\equiv-24\) (legitimate by §3), \(Ws^2/48=12W\). This gives
\[
\widehat P'=\mathfrak b_\pm'+12W+W\operatorname{tr}W_{A/B}^2 .
\]
Define \(\beta_\pm(t)=\mathfrak b_\pm(t)+12\int_0^tW\). Then pointwise
\[
\widehat P'\ \ge\ \max\Big\{0,\ \beta_+',\ \beta_-',\ \tfrac{WC^2}{3}\Big\}.
\]
Hence \(\widehat P[a,b]\ge\max\{V^+_{[a,b]}(\beta_+),V^+_{[a,b]}(\beta_-)\}\). This dominates Lemma V wherever \(W\) is not small.

Hand check on CH:
- With \(a_f=sc\), \(a_g=a_h=s\), one has \(W=s^3c\) and \(12\int_0^tW=3s^4\).
- So \(\beta_-=2-3s^4+3s^4\equiv2\). Equivalently \(\mathfrak b_-'=-12W\), consistent with \(B_B=0\) on CH.
- \(\beta_-\) is therefore the exactly pinned chiral observable on the Einstein end, and \(\beta_-(\infty)-2\) is the renormalized-volume term of Step 27.

Bearing on §2:
- `charge_variation.json` evaluates Lemma V without the volume term, recovering \(1.49\) of \(6.48\).
- The control script treats \(H\) (`U[:,0]`) as a free control. Its trajectories are therefore not in the \(s\equiv-24\) class.
- For those trajectories one can still use \(\widehat P'\ge\mathfrak b_\pm'+Ws^2/48\) with their actual \(s\).
- How much of the remaining \(\sim5\) units the volume channel recovers cannot be read off the supplied data.

## 2. Bolt normalization of \(\mathfrak b_-\)

**Smoothness at the bolt.** The \(O(-1)\) bolt has \(a_h\to0\), \(a_h'(0)=1\), and \(a_f(0)=a_g(0)=b\).
- The \(\sigma\)-period of the Hopf fibre is \(2\pi\), which is why \(a_h'(0)=1\) and not some other value.
- Smoothness requires \(a_f^2+a_g^2\) even in \(t\) and \(a_f^2-a_g^2=O(t^2)\). Together these give \(a_f'(0)=a_g'(0)=0\).

**Limits of \(\gamma\).**
- \(\gamma_h=(a_f^2+a_g^2-a_h^2)/(a_fa_g)\to2\).
- \(\gamma_f=(a_g^2-a_f^2)/(a_ga_h)+a_h/a_g\to0\), and likewise \(\gamma_g\to0\).

**Charges.** So \(u=(0,0,-1)\) and \(w=(0,0,3)\):
- \(\mathfrak b_+=2-1-0=1\).
- \(\mathfrak b_-=9-0-2=7\).
- These equal \(2\chi\pm3\tau\) with \(\chi=2\), \(\tau=-1\), and \(\mathfrak b=4=2\chi\). Confirmed.

**Sensitivity to the smoothness condition.** Suppose instead \(a_f'(0)=-a_g'(0)=c\neq0\). Then \(\gamma_f\to-4c\), \(\gamma_g\to4c\), \(u=(5c,-5c,-1)\), and \(\mathfrak b_+=1-75c^2\). So "any triaxial jet" in Step 27 must be read as "any jet satisfying the smooth-bolt conditions".

**Independent checks.**
- CH by hand: \(w=(2+s^2,2c,2c)\) gives \(\mathfrak b_-=2-3s^4\). \(u=(3s^2,0,0)\) gives \(\mathfrak b_+=2-9s^4\). The numerical values \(1.00657\) at \(t=0.7\) and \(-59.667\) at \(t=1.5\) are reproduced.
- Sanity check on \(S^4\): a forward centre (\(a'=1\)) has charge \((2,2)\), and a reversed centre (\(a'=-1\), so \(u=w\)-type values \(-2,0\)) has \((-2,-2)\). The total \(-4=-(2\chi\pm3\tau)(S^4)\) comes out correctly.

## 3. Lemma N and the scalar \(-24\) reduction

### (a) Hand re-derivation of the identities

**Orbit Ricci.** With \(dσ_i=2σ_jσ_k\), the orbit Ricci components are
\[
P_i=2\big(a_i^4-(a_j^2-a_k^2)^2\big)/(a_1a_2a_3)^2 .
\]
Rewriting with \(\kappa=a_f/(a_ga_h)\), \(\zeta=1/(a_ga_h)\), \(q=\log(a_g/a_h)\) gives exactly the script's \(P_f,P_g,P_h\). The relevant substitutions are \(1/a_f^2=\zeta^2/\kappa^2\), \(4/a_g^2=4\zeta e^{-q}\), and \((a_g^2-a_h^2)^2/(a_ga_h)^2=4\sinh^2q\).

**Radial equations.** One has \(\mathrm{Ric}_{ii}=-y_i'-y_iS+P_i\) and \(\mathrm{Ric}_{00}=-\sum(y_i'+y_i^2)\). This gives the stated \(y_i'\) and \(R^{(3)}=-2\kappa^2+8\zeta\cosh q-8\zeta^2\sinh^2q/\kappa^2\), hence the closed form of \(\mathcal C\).

**(1)** From the radial equations, \(e_0=-12+2\sigma_2-R^{(3)}+\sum e_i\). Therefore \((e_0-\sum e_i)/2=\mathcal C\). Also \(s=e_0+\sum e_i-24\), which gives \(G_{00}=\mathcal C+6\).

**(2)** Contracted Bianchi for the warped diagonal metric reads
\[
G_{00}'+SG_{00}-\sum y_iG_{ii}=0 .
\]
Substituting \(G_{ii}=e_i-6-(e_0+\sum e-24)/2\) and \(e_0=2\mathcal C+\sum e\) gives \(\mathcal C'=-2S\mathcal C-\sum(S-y_i)e_i\). An equivalent exact form is
\[
(W^2\mathcal C)'=-W^2\sum_i(S-y_i)e_i .
\]
So \(W^2\mathcal C\) is conserved on Einstein orbits; this is the precise content of "zero free drift".

**(3)** If \(s\equiv-24\) then \(e_0=-\sum e_i\), so \(\mathcal C=e_0=\mathrm{Ric}^\circ_{00}\). Spot checks confirm the norm decomposition \(|\mathrm{Ric}^\circ|^2=\tfrac34H^2+\tfrac23E^2+\tfrac12D^2\), with \(H=-4\mathcal C/3\). Multiplying by \(W/4\) gives \(W(\mathcal C^2/3+E^2/6+D^2/8)\).

**(4)** \(S'=18-S^2+R^{(3)}-\sum e_i=18-S^2+R^{(3)}+\mathcal C\).

All four agree with the symbolic checks in `scalar_normalized_constraint.py`. On CH, \(\mathcal C=0\).

### (b) Is \(s\equiv-24\) without loss?

**What holds.**
- Step 23 gives existence and uniqueness of \(u\to1\) for every smooth exact-CH-ended cell, with \(u-1=O(e^{-mr})\) for \(4<m<2+2\sqrt3\).
- Theorem C then gives \(P(g)-P(\hat g)=Q\ge0\).
- Uniqueness and the left-\(SU(2)\) isometries force \(u=u(t)\). Hence \(\hat g=d\hat t^2+\sum(ua_i)^2σ_i^2\) is diagonal Bianchi IX.
- The bolt stays smooth: \(d(ua_h)/d\hat t\to1\). So the bolt charges remain \((1,7)\).
- The CR datum at infinity is unchanged, because \(u\to1\) faster than \(e^{-4t}\).

**Correction 1: the end is asymptotic, not exact.** Since \(u\neq1\) on the exterior, \(\hat g\) is not exact CH outside a compact set; the phrase "preserves the exact end" is incorrect. The correct statement, already in Step 23, has two parts:
- The exact-ended diagonal infimum is \(\ge\) the infimum over diagonal \(s\equiv-24\) metrics asymptotic to the marked CH end at rate \(m>4\).
- Equality also holds. Cut off \(\hat g\) to exact CH on \([T,T+1]\). The added cost is \(O(e^{(4-2m)T})\to0\), since second-derivative errors are \(O(e^{-mT})\) and volume is \(e^{4T}\).

For lower bounds nothing is lost. However, any statement used inside the \(s\equiv-24\) class must not assume exactness of the end; Lemmas V, N and W are local in \(t\) and do not.

**Correction 2: charges are not conformally invariant.** \(\mathfrak b_\pm\) are scale-invariant but not conformally invariant. Pathwise statements must therefore be applied to \(\hat g\) itself. This is consistent, because \(\widehat P(\hat g)\le\widehat P(g)\) makes \(\hat g\) also cheap.

**Correction 3: the bolt radius is not preserved (bears on Theorem L).**
- \(\hat b=u(0)\,b\). The Step-23 barriers bound \(u\) above via \(\max(-s)\), but give no positive lower bound uniform in \(g\).
- So \(b\to\infty\) for \(g\) does not imply \(\hat b\to\infty\).
- Step 1 of Theorem L uses the \(s\equiv-24\) structure together with \(W\gtrsim b^2t\). It must therefore either be stated in terms of \(\hat b\), or come with a separate lower bound on \(u(0)\) for cheap large-bolt cells.

## 4. Lemma W

### (a) Where the written proof is incomplete

The phrase "\(S+\int|\mathcal C|\) cannot decrease while \(S\le m\)" gives monotonicity only on sub-intervals where \(\sigma_0\le S\le A\). \(S\) may start above \(m\) (always so when \(S(T)>A\)), and it may leave and re-enter \(\{S\le m\}\). Monotonicity on that set alone does not yield \(S(t)\ge m-\int_T^t|\mathcal C|\).

The case \(S(T)>A\) is not a counterexample. There \(S'\ge A^2-S^2-|\mathcal C|\) may be very large in magnitude below zero, but only while \(S>A\ge m\).

### (b) Rigorous version

**Lemma W (repaired).** Assume:
- \(s\equiv-24\) and \(R^{(3)}\ge-\rho_0\) on \([T,T_1]\);
- \(A=\sqrt{18-\rho_0}>0\), \(m=\min\{S(T),A\}\), and \(0<\sigma<m\).

If \(S\) attains the value \(\sigma\) on \([T,T_1]\), then
\[
\widehat P_{[T,T_1]}\ \ge\ \tfrac13\,\sigma\,(m-\sigma)^2\,W(T).
\]
Equivalently, if \(m-\big(3\widehat P_{[T,T_1]}/(\sigma W(T))\big)^{1/2}\ge\sigma\), then \(S>\sigma\) on \([T,T_1]\). In that case \(W(t)\ge W(T)e^{\sigma(t-T)}\) and \(\int_T^{T_1}W^{-1}\le(1-e^{-\sigma(T_1-T)})/(\sigma W(T))\).

*Proof.*
1. Let \(t_\sigma\) be the first time with \(S=\sigma\). On \([T,t_\sigma]\) we have \(S\ge\sigma\), so \(W'=SW\) gives \(\int_T^{t}W^{-1}\le1/(\sigma W(T))\).
2. Put \(f(t)=S(t)-m+\int_T^t|\mathcal C|\). Then \(f(T)=S(T)-m\ge0\); this covers both \(S(T)\le A\) and \(S(T)>A\).
3. Suppose \(f(t)<0\) for some \(t\le t_\sigma\). Let \(t_0=\sup\{\tau<t:f(\tau)\ge0\}\).
4. On \((t_0,t]\) we have \(\sigma\le S<m\le A\). By Lemma N(4) and \(R^{(3)}\ge-\rho_0\), \(S'\ge A^2-S^2+\mathcal C\ge-|\mathcal C|\), so \(f'\ge0\). Hence \(f(t)\ge f(t_0)=0\), a contradiction.
5. Therefore \(m-\sigma\le\int_T^{t_\sigma}|\mathcal C|\).
6. By Lemma N(3) and Cauchy–Schwarz, \(\int_T^{t_\sigma}|\mathcal C|\le(3\widehat P)^{1/2}(\sigma W(T))^{-1/2}\). This gives the cost bound.
7. For the equivalent form: if \(\widehat P=0\) the hypothesis forces \(m>\sigma\) strictly, and the cost bound excludes reaching \(\sigma\). Otherwise the strict factor \((1-e^{-\sigma(t-T)})\) makes the bootstrap strict. \(\square\)

**Corollary (bounce price).** Optimize at \(\sigma=m/3\). Any path on which \(S\) drops to \(m/3\) costs at least
\[
\widehat P\ \ge\ \frac{4m^3}{81}\,W(T).
\]
This includes every volume bounce \(S\le0\). It is the exact form of the note's "\((\Delta S)^2\sigma_0W/3\)".

### (c) Where the hypothesis \(R^{(3)}\ge-\rho_0\) holds

- **CH end.** \(-R^{(3)}=2-6/\sinh^2t<2\), so \(\rho_0=2\), \(A=4\), and \(S_{CH}\downarrow4\). The lemma applies with \(m\to4\).
- **Face \(\zeta=0\).** \(R^{(3)}=-2\kappa^2\), so one needs \(\kappa\) bounded. Examples: \(A^2\approx15\) at \(\kappa(1)\approx1.21\), and \(A^2\approx4\) at \(\kappa\approx2.63\) (\(t=0.38\)). The hypothesis does not hold near the bolt corner \(\kappa=\infty\).
- **Collapsed neck.** \(8\zeta^2\sinh^2q/\kappa^2=8\sinh^2q/a_f^2\) drives \(R^{(3)}\to-\infty\) when the fibre slot is small and \(q\neq0\). This is the same \(16q/\varepsilon^2\) term that makes the collapsed \(q\)-mode unstable. The missing orbit-curvature input sits exactly in that mechanism.

## 5. Exact versus numerical

**Exact (proved by derivation or symbolic identity):**
- the pointwise form of Lemma V and the \(\beta_\pm\) strengthening;
- the bolt charges \((1,7)\) under smoothness, and the CH and Burns checks;
- Lemma N(1)–(4) and \((W^2\mathcal C)'=-W^2\sum(S-y_i)e_i\);
- the inequality \(P(g)\ge P(\hat g)\) with diagonal, radial \(\hat g\), and equality of infima over exact-ended versus rate-\(>4\) asymptotic ends;
- Lemma W in the repaired form;
- the threshold \(\tau>0.7012\);
- Consequence 2 for the single tabulated state (a floating evaluation of an exact formula).

**Numerical only:**
- all of §2 (constrained local minima from collocation);
- the face limit \(d\sim0.90535b\) and \(\rho_\infty\sim1.345b\);
- the growth \(b^2(\log b)^2\);
- the Step-27 small-\(b\) laws.

**Textual inconsistency.** §5 states (N) is "numerically \(\ge5.37\)". §2 correctly says the constrained values are local minima. Each feasible converged path is an upper bound for the constrained infimum, and no lower bound follows from a local minimum. Only exact functionals (Lemma V, the \(\beta_\pm\) variation, Lemma W, or a certified dual) give lower values, and these currently reach \(\approx1.5\).

**Open input for the (N) reduction.** The reduction also uses \(\mathfrak b_+\approx-2\) at the collapsed section, which is exact only for controlled biaxial collapse. A sheared collapsed state needs its own charge evaluation before it enters (N).