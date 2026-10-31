# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/scripts/step28_ak_gap_identity.py",
    "Sessions/S1003A01/workspace/scripts/step28_ak_nu_structure.py",
    "Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json",
    "Sessions/S1003A02/workspace/notes/step34_characteristic_constraint_calculus_and_N_probe.md"
  ]
}
```

## Task

Independently read the peer's canonical almost-Kähler gap identity for diagonal perpendicular exact-CH O(-1) cells. Check the conformal factor and almost-Kähler construction, the exact coefficients and signs in P_hat-1=12H+6G+(3/2)Qdelta+(1/2)QA-(3/2)N+Sigma, the transport lambda=nu_T/2+beta nu and bolt charge law, and the far-field Hardy conclusion. Use the supplied scripts/data as supporting records, but reason through the derivation. State the exact hypotheses, identify any hidden boundary or integrability assumption, and judge whether this identity genuinely supplies a stronger route to the non-round lower bound than b_++phi(q,eta). Develop the most plausible compact near-zone inequality coupling nu, lambda, and log u, or identify a structural countermechanism if the desired >=1 lower bound is implausible.

## Output

# Verification memo: canonical almost-Kähler gap identity for diagonal perpendicular exact-CH O(−1) cells

## Summary

- **Construction and coefficients.** The almost-Kähler construction, the pinning formula, the Chern–Stokes bracket and every coefficient in Theorem A check out by independent derivation.
- **Stronger form of Theorem A.** The term \(\Sigma\) combines exactly with \(12H\) into a perfect square. The identity therefore holds with every term except \(-\tfrac32N\) nonnegative, with no \(s\equiv-24\) assumption.
- **Transport law.** The algebra of the transport law and of the bolt charge law is verified. The pointwise numerical check stored in the record does not work; the integrated check does.
- **Far-field Hardy step.** It is correct and its constant \(4\sqrt3\) is sharp for exponential weights. It upgrades to a Riccati inequality with an exported endpoint term.
- **The ≥1 bound.** The identity is exact, and the records give \(\widehat P<1\) on this class. No inequality derived from it can yield \(\widehat P\ge1\) for perpendicular cells.
- **Countermechanism.** It is visible in the records: the Jacobi operator of the Nijenhuis sector oscillates in the zone \(\Lambda<4\sqrt3\), and there the conformal factor has already relaxed while \(\nu\) persists.
- **What the identity does supply.** A one-dimensional Riccati condition that is sufficient for \(\widehat P\ge1\), and a computable deficit bound otherwise. That is the correct tool for the sharp subunit constant.

---

## 1. Conformal factor and almost-Kähler construction

**Self-duality.** In the frame \(e^0=dt,\ e^i=a_i\sigma_i\),
\[
d(\phi\sigma_f)=(\phi'/a_f)\,e^{0f}+(2\phi/a_ga_h)\,e^{gh}.
\]
This is self-dual iff \(\phi'/\phi=2a_f/(a_ga_h)\). ✓

**Normalization on the collar.** On CH (\(a_f=\sinh R\cosh R,\ a_g=a_h=\sinh R\)), the solution is \(\phi=\sinh^2R\), so \(u\equiv1\) there. ✓

**Constant norm and the AK constraint.** We have \(\omega=2u^2(e^{0f}+e^{gh})=2(\hat e^{0f}+\hat e^{gh})\), so \(\omega/2\) is the unit AK form of \(\hat g=u^2g\). Matching \(d(\phi\sigma_f)=\phi_T\,dT\wedge\sigma_f+2\phi\,\sigma_g\wedge\sigma_h\) against \(2(\hat e^{0f}+\hat e^{gh})\) gives:
- \(\mathcal P=A_gA_h=\phi\),
- \(A_f=\mathcal P_T/2\). ✓

The script docstring writes "Pm = A_g A_h = 2 phi". This conflicts with \(u^2=\phi/(a_ga_h)\). It is harmless, because the SymPy code uses \(\mathcal P=A_gA_h\) directly.

**Pinning.** \(d\hat V=A_fA_gA_h\,dT=d(\mathcal P^2/4)\), and on CH \(\mathcal P^2/4=X^2/4=\sinh^4R/4=V_{\rm CH}\). ✓

**Behaviour at the bolt: \(\hat g\) is singular.** With \(a_f,a_g\to b\) and \(a_h\simeq t\):
- \(\phi\sim ct^2\), so \(u^2\sim(c/b)t\);
- \(dT=u\,dt\), so \(T\sim t^{3/2}\);
- the slots behave as \(A_f,A_g\sim T^{1/3}\) and \(A_h\sim T\).

The bolt is crushed: \(\hat g\) is an incomplete singular metric, and \(J\) does not extend. \(J\) sends the normal direction \(e^0\) to the tangential direction \(e^f\), and \(e^f,e^g\) rotate around the \(h\)-circle. The zero set of \(\omega\) is the entire bolt \(S^2\), with \(|\omega|_g\sim t\). This zero set is far from generic for near-symplectic forms, and it is forced by the symmetry.

**Smoothness requirement.** \(\phi\sim ct^2(1+O(t^2))\) needs the standard smoothness at a U(1)-isotropy orbit: \(a_f-a_g=O(t^2)\), \(a_h=t+O(t^3)\). For a \(\mathbb Z_p\)-orbifold bolt, or for \(O(-k)\), the exponents change and the relative Chern–Weil input changes as well.

## 2. Coefficients of Theorem A — rederived

**Sign convention.** \(|W^+|^2\) is the sum of squared eigenvalues on \(\Lambda^+\). On CH these are \((-4,2,2)\), giving 24.

**Relative identity.** I rederived \(1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc}\) from Gauss–Bonnet/signature:
- \(dV=2\pi^2W\,dt\);
- \(\chi(O(-1))=2\), \(\tau=-1\), so \(2\chi+3\tau=1\);
- subtract the CH ball (\(2\chi+3\tau=2\)) with the same collar. ✓

**Steps (i)–(iv) of the proof.**

(i) The traceless split gives \(\tfrac32W_{\omega\omega}^2+\tfrac12(W_{gg}-W_{hh})^2\). Writing \(\tfrac32(\delta-4)^2=\tfrac32\delta^2-12\delta+24\) gives the stated formula for \(D_+\). ✓

(ii) The relations are consistent with the AAD formulas:
- \(\kappa-\hat s=6\nu^2\) and \(\hat s^*-\hat s=2\nu^2\), in the ratio 3:1 that AAD gives;
- hence \(\kappa/6=\hat s^*/6+\tfrac23\nu^2\);
- the record checks \(\kappa-\hat s-6\nu^2\) to \(3.6\times10^{-14}\), with \(\kappa\) from the Cartan \(W^+\) and \(\hat s\) from the conformal Laplacian.

(ii′) The Stokes bracket \(B=4\mathcal P\cosh q-\mathcal P\mathcal P_{TT}-\tfrac12\mathcal P_T^2\):
- On CH, with \(x=\sinh^2R\): \(B=4x-2x(1+2x)-2x(1+x)=-6x^2\), and \(B'=-24\sinh^3R\cosh R=\hat s\,w\). ✓
- At the bolt, \(\mathcal P\cosh q\sim t\), and both \(\mathcal P\mathcal P_{TT}\) and \(\mathcal P_T^2\) scale as \(T^{2/3}\), so \(B\to0\). ✓
- Hence \(\int\delta\,d\hat V=N/6\).

(iii) Integration by parts and the volume formula:
- With the analyst's Laplacian, \(\int\hat s\,d\hat V=6G+\int su^2W\).
- The endpoint term \(uu'W\sim b^2t/2\to0\). ✓
- Combining with pinning and \(H=\int u^4W-2\int u^2W+\int W\) reproduces \(V_{\rm exc}=H+G/2+N/24+\tfrac1{12}\int(s+24)u^2W\). ✓

(iv) Using \(S_{\rm exc}=\int W[(s+24)^2/48-(s+24)]\) reproduces Theorem A exactly. ✓

**Arithmetic check of the record** (\(x_0=.038\), \(X=128\)): the six terms sum to \(-0.0047126\). ✓

**Strengthening.** \(12(u^2-1)^2+(s+24)(u^2-1)+(s+24)^2/48=(24u^2+s)^2/48\). Therefore
\[
\boxed{\widehat P-1=\mathcal S+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N,\qquad \mathcal S=\tfrac1{48}\int(s+24u^2)^2\,dV\ \ge0.}
\]
Numerically \(\mathcal S=.00074+.00003\), \(.003327\), \(.00769\) for the three records. The statement "all terms nonnegative except \(-\tfrac32N\)" is now literally true for every \(s\).

The note's "integrable ⇒ \(\widehat P\ge1+12H\)" should read \(\widehat P-1\ge\mathcal S+6G+\dots\).

In \(\hat g\)-variables, with \(\psi=\log u\),
\[
G=\int|d\psi|^2_{\hat g}\,d\hat V,\qquad \mathcal S=\tfrac1{48}\int\big(\hat s+24+6\hat\Delta\psi-6|d\psi|^2\big)^2d\hat V .
\]
The conformal sector is thus a Yamabe-type functional of \(\psi\) on the singular AK metric.

**Regrouping.** \(\nu-\ell=-v_g/(ua_g)\) with \(\ell=-\psi_T\). I verified this from \(u'/u=\tfrac12(2a_f/a_ga_h-y_g-y_h)\) and \(2\sinh q/a_f=(a_g^2-a_h^2)/W\). At the bolt, \(v_g=O(t)\), so \(\nu-\ell=O(t^{1/2})\). This is the precise content of "bolt neutrality".

## 3. Transport and bolt charge

**Algebra.** From \(\lambda=\tfrac12\nu_T+\beta\nu\) and \(\mu_T=2\beta\mu\) we get \((\mu\nu)_T=2\mu\lambda\). The explicit formula follows from \(dT/A_f=dt/a_f\):
\[
\mu=(ua_f)^{-1}\exp\int\frac{4\cosh q}{a_f}\,dt .
\]
✓

**Bolt asymptotics.** \(4\cosh q/a_f\simeq2/t\), so \(\mu\sim t^{3/2}\). Together with \(\nu\sim-1/(2ut)\sim t^{-3/2}\), this gives a finite \(K\), which is nonzero because both coefficients are positive.

**Numerical status.**
- The pointwise check `transport_rel_residual_max = 2.0e7` in the record does not test the law. It applies `np.gradient` on concatenated Gauss panels to \(\nu_T\sim T^{-2}\) near the bolt, where \(\nu_T/2\) and \(\beta\nu\) cancel to the much smaller \(\lambda\).
- The field `law_residual` is hard-coded to 0.0 by dead code.
- The genuine evidence is threefold:
  - \(\mu\nu\) is constant to about \(10^{-9}\) over the first 15 profile nodes;
  - \(\mu\nu(X)\approx5\times10^{-13}\);
  - \(\int2\mu\lambda\,dT=0.0174759\) matches \(-K\) to \(1.3\times10^{-12}\). Here \(\mu\) comes from quadrature of \(\cosh q/a_f\) and \(\lambda\) from the Cartan \(W^+\), so the two sides are independent.
- This verifies the integrated law on one interval. A pointwise test would compare cumulative \(\int2\mu\lambda\) with \(\mu\nu\) at all 40 nodes, or compute \(\nu_T\) from the jets.
- The SymPy output `ak_nu_structure.json` was not supplied, so the pointwise formula for \(\beta\) rests on that file.

**Consequence.** Normalization-free Cauchy–Schwarz gives
\[
Q_A\ \ge\ \frac{K^2}{\int\mu^2w^{-1}\,dT}.
\]

**Charge form of the Nijenhuis sector.** Set \(z=\mu\nu\) and \(m=w/\mu^2\), with \(w=A_fA_gA_h\). Then
\[
\tfrac12Q_A-\tfrac32N=\int m\Big(\tfrac12z_T^2-6z^2\Big)dT,\qquad z(0)=K,\ z(X)=0,\qquad \Lambda=(\log m)_T .
\]
The Hardy coefficient is exactly the log-derivative of the weight.

## 4. Far-field Hardy step and its sharp form

**Verification.** \((\nu^2w)_T=4\nu\lambda w+\Lambda\nu^2w\) is correct, and the bound \(16/c^2\le1/3\Leftrightarrow c\ge4\sqrt3\) follows.

On CH,
\[
\Lambda=5\coth R+3\tanh R-\frac{8}{\sinh R\cosh R}=\frac{8x-3}{\sqrt{x(1+x)}} .
\]
Setting \(\Lambda^2=48\) gives \(16x^2-96x+9=0\), so \(x_H=3+\tfrac34\sqrt{15}\). ✓

For \(m=e^{cT}\), the weighted Hardy constant \(c^2/4\) shows that \(c=4\sqrt3\) is sharp.

**Riccati upgrade.** Start from \(\tfrac12z'^2\ge-2\kappa zz'-2\kappa^2z^2\). For any \(C^1\) function \(\kappa\) on \([a,b]\),
\[
\int_a^b m\big(\tfrac12z_T^2-6z^2\big)\ \ge\ \kappa mz^2\big|_a-\kappa mz^2\big|_b+\int_a^b mz^2\big(\kappa'+\Lambda\kappa-2\kappa^2-6\big).
\]
- On a tail with \(\Lambda\ge c\), take \(\kappa=(c+\sqrt{c^2-48})/4\), which equals \(\sqrt3\) at threshold. Then the tail sector is at least \(\kappa\,\nu^2w(T_*)\). That endpoint value is exported to the near zone.
- Record check: \(\sqrt3\times0.0022385=0.00388\le0.00588\), the actual far sector. ✓
- Equality holds for \(\kappa=-z_T/(2z)=-\lambda/\nu\).

**What is rigorous.** Positivity holds on any tail where \(\Lambda\ge4\sqrt3\), or where a Riccati supersolution exists. The location \(x_*\approx5.9\)–\(6.0\) is measured on these optimizers. "All gain inside \(x\lesssim6\)" is therefore an observation about them, not a property of every cell.

## 5. Hypotheses, including hidden ones

1. **Symmetry.** Diagonal SU(2)-invariant metric, so \(\mathcal J=0\) and \(W_2^+=0\). Off-diagonal cells add \(+2|W_2^+|^2\) but also change \(\omega\).
2. **Bolt.** Smooth, non-orbifold O(−1) bolt with perpendicular collapse (\(h\ne f\)) and the smoothness orders of §1. These give \(\phi\sim ct^2\), \(u\sim t^{1/2}\), \(\nu\sim t^{-3/2}\), \(\lambda,\delta\sim t^{-1}\).
   - Every term is then separately finite: the densities of \(G\) and \(N\) are bounded, and those of \(Q_A\) and \(Q_\delta\) are \(O(t)\).
   - The Nijenhuis sector alone has divergent integration-by-parts pieces at the bolt (\(\beta w\nu^2\sim T^{-4/3}\)). Any rearrangement must keep \(6G\) together with \(N\), or use the charge form with \(\kappa mz^2\to0\), i.e. \(\kappa=o(T^{1/3})\).
3. **Exact CH collar.** It is used four times:
   - in the relative Chern–Weil step;
   - for \(\nu=0\) at \(X\);
   - for \(u'=0\);
   - for \(B(X)=-6X^2\).
4. **Bolt contributes nothing to \(\int\hat s^*\).** This is a one-dimensional limit valid because \(\omega\) vanishes to first order along the whole bolt. It is not a Chern–Weil statement for singular AK metrics. For generic closed SD forms the zero set is circles, and its contribution to \(\int s^*\) must be computed by Taubes-type analysis.
5. **Existence of \(\omega\) outside the diagonal class.** A closed SD form agreeing with the Kähler form on an open collar is unique by unique continuation, but its existence is overdetermined. The natural generalization is the APS-type problem: SD harmonic \(\omega\) with prescribed tangential data on the link. Since \(b_+=0\), it is uniquely solvable, and it introduces collar flux terms in the pinning and Chern steps.

## 6. Is \(\widehat P\ge1\) plausible on this class? No.

**The records.** Theorem A is an exact identity whose residual is about \(10^{-10}\). In the same records, \(\widehat P\) agrees with the stored \(J\) to \(3\times10^{-7}\). The deficits are:

| \(x_0\) | \(X\) | \(\widehat P-1\) |
|---|---|---|
| .015 | 256 | −0.00233 |
| .038 | 128 | −0.00471 |
| .038 | 512 | −0.00482 |

The longer collar lowers it further. No inequality deduced from the identity can therefore give \(\widehat P\ge1\) here.

**The mechanism, read off the \(x_0=.038\) profile.**

- **Decoupling of relaxation lengths.** By \(t\approx0.36\) the factor \(u\) has relaxed to 0.97, and to 0.99 by \(t=0.5\); 98% of \(6G\) is accumulated by \(t=0.5\). Meanwhile \(\nu\) is still \(-0.47\), then \(-0.20\), and \(\lambda\) passes through zero at \(t\approx0.35\).
  - In this window \(\ell\approx0\) while \(\nu\ne0\), so \(\ell^2-\nu^2\approx-\nu^2\).
  - The density \(6w(\ell^2-\nu^2)\) delivers almost its maximal gain with no conformal payment.
  - The cumulative total falls from \(+0.0007\) at \(t=0.12\) to \(-0.0161\) at \(t=0.50\).
- **Oscillatory Jacobi regime.** \(\int m(\tfrac12z_T^2-6z^2)\) has Jacobi equation \(z''+\Lambda z'+12z=0\), which oscillates when \(\Lambda^2<48\). The optimizer uses this: \(z=\mu\nu\) is \(-0.00705\) at \(t=0.73\) and \(+0.00235\) at \(t=1.08\). The sign change occurs where \(\Lambda\in(2.3,5.1)<4\sqrt3\), and there is a second small gain window for \(t\in(1.1,1.6)\).
- **\(Q_\delta\) cannot compensate.** Its forced part is quartic. With the local Chern flux \(F(T)=B+6\mathcal P^2\),
  \[
  Q_{\delta,[0,T]}\ \ge\ \frac{\big(F(T)/6+N_{[0,T]}/6\big)^2}{\hat V(T)},
  \]
  which is about \(10^{-5}\) here, against a quadratic gain of 0.06.

**Trend.** \(K=.0073,\ .0175,\ .0292\) and the deficit sequence \(-.0023,\ -.0047,\ +.0008\) over \(x_0=.015,\ .038,\ .07\) are consistent with \(\widehat P\to1^-\) in the bubble limit \(x_0\to0\). That limit recovers the Lemma Q unit \(2-4+3=1\). Three points do not fix the exponent.

## 7. The near-zone inequality in its natural form

Combine the strengthened identity, the charge form, and Riccati applied over the whole cell (with \(\kappa mz^2\to0\) at the bolt and \(z(X)=0\)):
\[
\widehat P-1\ \ge\ \mathcal S+\tfrac32Q_\delta+\int w\Big[6\ell^2+\nu^2\big(\kappa'+\Lambda\kappa-2\kappa^2-6\big)\Big]dT .
\]

**Sufficient condition for \(\widehat P\ge1\).** There exists \(\kappa\) on \((0,X]\) with \(\kappa=o(T^{1/3})\) at the bolt and
\[
\kappa'+\Lambda\kappa-2\kappa^2\ \ge\ 6\big(1-\ell^2/\nu^2\big).
\]

**Quantitative form otherwise.**
\[
\widehat P\ \ge\ 1-\inf_\kappa\int w\nu^2\big[6(1-\ell^2/\nu^2)-\kappa'-\Lambda\kappa+2\kappa^2\big]_+\,dT .
\]

**How the pieces behave.**
- Near the bolt, \(\ell/\nu\to1\), so the right side of the condition tends to 0 and \(\kappa\approx0\) works. This is bolt neutrality.
- On the tail \(\Lambda\to8\), and a constant \(\kappa\in[1,3]\) works. This is Hardy.
- The condition can only break in the middle zone, where \(\ell^2/\nu^2\ll1\) and \(\Lambda<4\sqrt3\). There the Riccati solution meets a conjugate point; the optimizer's zero of \(\nu\) at \(t\approx0.9\) is its trace.

All three ingredients — \(\Lambda=(\log m)_T\), \(\ell=-(\log u)_T\), and \(\nu\) — are computable from the existing records. \(\ell\) is `upr/uu**2` in the script.

**What a theorem needs.** A lower bound on the deficit, uniform over the class, needs geometric control of two quantities across \(x\lesssim6\):
- the length of the oscillatory zone in the \(m\)-geometry;
- the ratio \(\ell/\nu\), i.e. the conformal relaxation length set by \(\phi\) versus the Nijenhuis length set by \(\mu\).

This gives a sharp-constant statement \(\widehat P\ge1-\varepsilon_*\), with \(\varepsilon_*\gtrsim0.0048\) from the records, not \(\ge1\). Two coupling features matter:
- \(m\) depends on \(q\) through \(\mu\), so the full problem is nonlinear;
- for fixed geometry the \(z\)-problem is linear-quadratic, with Robin end value \(\kappa_*=\sqrt3\) at \(T_*\).

## 8. Relation to \(\mathfrak b_++\phi(q,\eta)\)

**HJ facts.** Equation (3.1) says the charge calibration has zero pointwise slack. Equation (3.2) rules out decorating it by \((q,\eta)\).

**Why the AK identity escapes this.** It uses a variable absent from the state \((x,z,p,\chi,\eta)\): the potential \(\Phi=\log\phi\) of the closed SD form. \(\Phi\) obeys the uncontrolled ODE \(\Phi'=2a_f/(a_ga_h)\) with its end value fixed at the collar, so it is nonlocal in the original state. The variables \(u\), \(\nu=-(\eta+4\sinh q/a_f)/(2u)\) and \(\mu\) all depend on it.

**The Riccati term as a value function.** \(\kappa\,\nu^2w=\kappa\,mz^2\) is a value-function term in the augmented state \((X,\Phi)\). It is exactly the kind of "additional geometric/jet variable" that Step 34 found necessary.

**Assessment.** The identity is a genuinely stronger structure:
- it is exact;
- it isolates one sign-reversed mechanism;
- it reduces that mechanism to a one-dimensional weighted Sturm–Liouville form with a forced charge;
- it proves sharp tail positivity.

Its correct target is the subunit infimum on the perpendicular class and the shape of near-minimizers, not a bound \(\ge1\). The bound \(\ge1\) is contradicted by the class's own records, and any non-round lower bound on this class must enter at \(1-\varepsilon_*\).