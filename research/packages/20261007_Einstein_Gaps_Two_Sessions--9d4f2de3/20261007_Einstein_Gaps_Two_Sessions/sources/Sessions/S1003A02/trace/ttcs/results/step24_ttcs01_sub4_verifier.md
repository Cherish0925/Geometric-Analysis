# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Skills/geometric-analysis/references/conventions-and-literature.md",
    "Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md"
  ]
}
```

## Task

Independently verify Theorems C and H in the Step-23 note against the conventions and cited LeBrun source. Check all normalizations, conformal identities, decay/boundary requirements, the conditional sharp P and Einstein-defect values, the range 1<=k<=2 chi(Y), the Burns upper sequence, and non-attainment. Identify any false statement or missing hypothesis and give exact corrected formulations. Also assess whether Theorem C's relative RV definition is invariant under moving the compact cutoff and what is actually known about existence of u on H4 versus CH cells.

## Output

# Verification of Theorems C and H (Step-23 note)

## Summary

- **Algebra and normalizations.** All of the algebra checks against the ledger and LeBrun's paper. This covers (1.1)–(1.6), (3.1), (3.2), the value \(Y_{\rm hyp}^2=192\pi^2\chi(Y)\), the \(t=P/S\) bound and the value \(4k/(k+6\chi)\).
- **Theorem C.** It is correct as stated. Its hypothesis "for which (1.1) has the complete solution" can be removed in both bulks. A double-well variational argument (§4 below) gives existence, uniqueness, decay, and the explicit bound \(Q\le\frac{13}{12}\int(s+24)^2\).
- **Theorem H** contains four false or unsupported statements:
  1. At the endpoint \(k=2\chi(Y)\), the value \(\alpha=1\) holds unconditionally, but non-attainment does not follow from the given argument.
  2. "The gap equals its sharp value exactly when \(y_k=1\)" is only sufficiency.
  3. The clause "\(8\pi^2\) carried by each exceptional class" in (3) does not follow from (3.2).
  4. The justification of \(\int(s-\bar s)^2\to0\) omits the transition regions. The conclusion still holds.
- **Attributions.** The attaining-implies-Einstein statement is in LeBrun §5, not §2. Identity (1.4) is already the equality line of LeBrun's Lemma 1, not a sharpening of it.

---

## 1. Normalizations

- **Chern–Weil.** The ledger's \(4\pi^2T_+=S/24+2\int|W^+|^2-P/2\), times 2, gives the note's \(8\pi^2(2\chi+3\tau)=\int(4|W^+|^2-|\mathrm{Ric}^\circ|^2+s^2/12)\). LeBrun's §3 formula is the same identity.
- **Laplacian convention.** The note uses \(\Delta=\operatorname{div}\nabla\); LeBrun's \(\Delta\) is the positive Laplacian. So LeBrun's \(\hat s\phi^3=6\Delta_{\rm L}\phi+s\phi\) is the note's (1.1) with \(\hat s=-24\).
- **Model normalizations.**
  - \(H^4\) with \(K=-2\): \(\mathrm{Ric}=-6\), \(s=-24\), volume growth \(e^{3\sqrt2t}\).
  - \(\mathbb{CH}^2\) with holomorphic curvature \(-4\): Jacobi factors \(\sinh t,\sinh t,\tfrac12\sinh2t\), so volume growth \(e^{4t}\) and \(\mathrm{Ric}=-6\).
  - Both bulks use the same \(\hat s=-24\).
- **Burns first-order slopes.**
  - \(H^4\): \(\mathbf R^+=\tfrac s{12}I=-2I\).
  - CH: \(W^+=\mathrm{diag}(-4,2,2)\), so the perpendicular direction has \(W^+(\zeta,\zeta)=2\).
  - These give the first-order slopes \(48\mathrm{RV}/x_0\to2\) in both bulks, \(4\Delta W_+/x_0\to0\) for \(H^4\), and \(4\Delta W_+/x_0\to-2\) for CH.
- **Hyperbolic Gauss–Bonnet.** \(8\pi^2\chi(Y)=S/24\), so \(Y_{\rm hyp}^2=S(g_{\rm hyp})=192\pi^2\chi(Y)\) and \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\). With \(\tau(Y)=0\), \((2\chi+3\tau)(X_k)=2\chi(Y)-k\).

## 2. Closed identity (1.2)–(1.4)

- **Pointwise identity.** Expanding both sides of the quadratic identity gives \(\sigma^2/12+4\sigma u^2-4\sigma+48u^4-96u^2+48\) on each side.
- **Integration.** \(\int u\cdot(1.1)\) gives \(I=-6\int|\nabla u|^2\). Then \(\sigma+24(u^2-1)=6\Delta u/u\), and \(\int(\sigma^2/12-4\sigma)=S/12-48V\). These yield (1.4) with \(Y[g]^2=576\,\mathrm{Vol}(\hat g)\).
- **Attribution.** This is literally LeBrun's Lemma 1 computation: \(\int s^2=\int\hat s^2d\hat\mu+12|\hat s|\int|\nabla\phi|^2+36\int(\Delta\phi/\phi)^2\), before the final "\(\ge\)". The equivalent form \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\) also matches S1003A01 (1.3) with \(\kappa=24\) and the ledger's \(P(g)=P(\hat g)+\delta/12\).

## 3. Relative identity (1.5) and RV

- **Algebra.** On \(U_{\rm int}\), \(\int(\sigma^2/12-4\sigma)=\int_{U_{\rm int}}s^2/12-48\mathrm{Vol}_g(U_{\rm int})\). On the exterior \(\sigma=0\). Regrouping gives (1.5) exactly.
- **Decay.** The linearization is \(6\Delta w=48w\).
  - \(H^4\): in AH language the indicial equation is \(s(s-3)=4\), so \(s=4\). Hence \(w=O(\rho^4)=O(e^{-4\sqrt2t})\) for every angular mode, not only radial ones.
  - CH: \(\mu^2-4\mu-8=0\) gives \(\mu=2+2\sqrt3>4\).
  - In both bulks \(\int|u^4-1|\,d\mu_g<\infty\), and the flux \(\oint u\partial_\nu u\) is \(O(e^{-\sqrt2t})\) for \(H^4\) and \(O(e^{(2-2\sqrt3)t})\) for CH.
- **Cutoff invariance of RV.** Replace \(U_{\rm int}\) by \(U_{\rm int}\cup A\), where \(A\) is an exterior annulus on which \(g\) equals the model, and replace \(B\) by \(B\cup A\).
  - \(\mathrm{Vol}_g(U_{\rm int}\cup A)-\mathrm{Vol}(B\cup A)\) is unchanged.
  - \(\int(u^4-1)\) is over the whole cell and does not depend on the cutoff.
  - The left side of (1.5) changes by \(\int_A(576/12-48)=0\).
  - Because \(u^4-1\) is absolutely integrable, RV equals \(\lim[\mathrm{Vol}_{\hat g}(\Omega_j)-\mathrm{Vol}_{\rm model}(\Omega_j')]\) for any exhaustion compatible with the marking.
- **Marking.** RV depends on the marking only through \(\mathrm{Vol}(B)\). An isometry between connected exterior regions of \(H^4\) or \(\mathbb{CH}^2\) extends to a global isometry, because these are complete, simply connected and analytic. So \(\mathrm{Vol}(B)\) is well defined.
- **Nature of RV.** RV is a relative volume against an exact collar. It is not Graham's finite-part renormalized volume, and the two should not be conflated.
- **The \(\hat g\) statement in Theorem C.** \(P_{\rm cell}(\hat g)-8\pi^2=4\Delta W_++48\mathrm{RV}\) uses Chern–Weil for a metric whose collar is only asymptotic to the model. The Pfaffian and signature transgressions on \(S_t\) differ from the model by \(O(|w|+|\nabla w|+|\nabla^2w|)\times\mathrm{area}(S_t)\to0\) at the rates above, so this needs no further hypothesis.

## 4. Existence and uniqueness of u: what is known, and a general theorem

**\(H^4\) cells.** Exact \(H^4\) exteriors are smoothly conformally compact with round \(S^3\) at infinity. The Loewner–Nirenberg / Aviles–McOwen theorem gives a complete constant-\(\hat s\) conformal metric with no sign condition on \(s\). Uniqueness and \(u\to1\) follow from the normalization at infinity. This reading in the note is correct.

**CH cells.** \(\mathbb{CH}^2\) is not conformally compact (its infinity is CR), so Aviles–McOwen does not apply. S1003A01's Theorem 2 covers \(s\le-c<0\) through constant sub- and supersolutions. The criticality \(6\lambda_0+s_{\rm CH}=0\) has a concrete meaning. Any Dirichlet eigenvalue satisfies \(\lambda_1(\Omega)>4\), so no compactly supported exterior subsolution of \(-6\Delta v\le24v(1-v^2)\) exists. Positivity cannot come from local barriers.

**General theorem (derived here).** It covers both bulks and every sign of \(s\). Write \(\sigma=s+24\), supported in the compact set \(K\), and set
\[
\tilde E(u)=\int\Big[3|\nabla u|^2+6(u^2-1)^2+\tfrac12\sigma(u^2-1)\Big]d\mu_g .
\]
Its Euler–Lagrange equation is \(-6\Delta u+24u(u^2-1)+\sigma u=0\), which is (1.1). On the model end the potential is the double well \(6(u^2-1)^2\).

- *Lower bound.* \(\tilde E\ge\int3|\nabla u|^2+3(u^2-1)^2-\int\sigma^2/48\), and \(\tilde E(1)=0\).
- *Minimizer.* Take a minimizing sequence and replace each \(u_j\) by \(|u_j|\). This gives local \(H^1\) bounds, since \(\int_\Omega u^4\le2\int(u^2-1)^2+2|\Omega|\).
  - The \(\sigma\)-term converges by Rellich into \(L^p(K)\), \(p<4\).
  - The other terms are lower semicontinuous.
  - The minimizer \(u\ge0\) is smooth by Trudinger/Brezis–Kato regularity, since \(u^2\in L^2_{\rm loc}=L^{n/2}\).
- *Positivity.* The strong maximum principle gives \(u>0\) or \(u\equiv0\). Here \(\tilde E(0)=+\infty\) because the end has infinite volume, so \(u>0\).
- *Decay.* On the end, \(w=u-1\ge-1\) solves \(-6\Delta w+24(w+1)(w+2)w=0\), with a bounded potential \(\ge0\). Moser iteration in bounded geometry gives \(\sup_{B_{1/2}(x)}|w|\le C\|w\|_{L^2(B_1(x))}\to0\), because \(\int_{\rm end}w^2\le\int(u^2-1)^2<\infty\). The exact model exterior then gives the indicial rate.
- *Uniqueness.* For two solutions \(u_1,u_2\to1\), the ratio \(v=u_2/u_1\) satisfies \(6\Delta_{g_1}v=24v(v^2-1)\). An interior maximum with \(v>1\) or minimum with \(v<1\) is impossible, so \(v\equiv1\).
- *Explicit bound.* Since the solution is the minimizer, \(\tilde E(u)\le0\). This gives \(\|u^2-1\|_2\le\|\sigma\|_2/12\) and \(\int|\nabla u|^2\le\|\sigma\|_2^2/72\), hence
\[
Q=\tfrac1{12}\!\int(\sigma+24(u^2-1))^2+24\!\int|\nabla u|^2\le\tfrac{13}{12}\int(s+24)^2 .
\]

The closed analogue holds when \(\tilde E(0)=6V-\tfrac12\int\sigma>0\). Then the minimizer is nonzero and equals the unique Yamabe factor.

**Consequences.**
- *Finding 3 becomes a theorem.* For Burns-glued metrics, \(\int\sigma^2\) has three contributions: core \(O(x_0^2)\), intermediate region \(O(x_0^2\log(1/x_0))\), and cut annulus \(O(x_0^{6/5})\). So \(Q=O(x_0^{6/5})=o(x_0)\), and \(48\mathrm{RV}(\hat g)=\Delta S/12-Q=-8\pi^2x_0s_p/12+O(x_0^{6/5})\). The note's statement that an "\(L^2\) bound on \(\nabla w\) at core scale" is needed is superseded.
- *Closed first-order Yamabe response.* For a bulk with \(s\equiv-24\) and \(k\) Burns points,
\[
Y[\hat g_{x_0}]^2=Y[g]^2+192\pi^2kx_0+O(x_0^{6/5}).
\]
  The Burns minimizing sequences on \(H^4\) bulk therefore have \(Y[g_j]\uparrow\)… more precisely \(Y[g_j]\to Y_{\rm hyp}\) **from below** (\(|Y[g_j]|>|Y_{\rm hyp}|\)). Their entire first-order excess \(16\pi^2kx_0\) sits in the Yamabe term of (3.2). This is consistent with (H) and gives no information about \(\mathcal Y(X_k)\).

## 5. Theorem C, exact formulation

Setup:
- \((U,g)\) is complete and oriented, with \(U\cong D\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\).
- \(g\) equals \(H^4\) (\(K=-2\)) or \(\mathbb{CH}^2\) (holomorphic curvature \(-4\), complex orientation) outside a compact set, with a fixed marking.

Statement:
- There is a unique positive \(u\) with \(\hat s\equiv-24\) and \(u\to1\) at the rates of §3.
- With \(\Delta W_+=\int_{U_{\rm int}}|W^+|^2-\int_B|W^+_{\rm model}|^2\),
\[
P_{\rm cell}(g)-8\pi^2(k+4\ell)=4\Delta W_++48\mathrm{RV}(\hat g)+Q,\qquad 0\le Q\le\tfrac{13}{12}\textstyle\int(s+24)^2,
\]
\[
P_{\rm cell}(\hat g)-8\pi^2(k+4\ell)=4\Delta W_++48\mathrm{RV}(\hat g).
\]

\(H^4\) consequences:
- \(\mathrm{RV}\ge0\) implies \(P_{\rm cell}\ge8\pi^2(k+4\ell)\).
- The note's equivalence with \(\inf(4\int|W^+|^2+48\mathrm{RV})\ge0\) needs, in the forward direction, an \(H^4\) truncation lemma. That lemma says \(\hat g\) is a limit of exact-collar cells with \(P\to P(\hat g)\), which is the analogue of S1003A01's CH truncation at rate \(e^{(4-2\mu)R}\).

What remains open is the sign of RV. Mass positivity for \(\hat g\) (AH, \(\hat s\equiv-24\), nonhyperbolic topology) would give the decay coefficient \(c>0\). That is a different quantity, and no RV–mass comparison in dimension four is in the supplied material.

## 6. Table consistency

Row closure \((P-1)-(4\Delta W_++48\mathrm{RV}+Q)\):
- \(H^4\) rows: between \(10^{-6}\) and \(3\times10^{-5}\), growing with \(x_0\).
- CH rows at \(x_0=.003\) and \(x_0=.01\): \(-6\times10^{-7}\) and \(-1.7\times10^{-6}\).
- CH certified witness (\(x_0=.03\)): \(-0.0041516\) against \(-0.0041001\), a residual of \(5.2\times10^{-5}\).
- CH row \(x_0=.05\): residual \(3.3\times10^{-5}\).

The witness residual is about \(1.2\%\) of \(|P-1|\) and an order of magnitude above the neighbouring rows. That is inconsistent with the stated \(O(h^2)\) closure. It fits a mismatch between the Arb-certified metric, whose \(P\) is quoted, and the metric the finite-volume script rebuilds. It does not affect any channel sign.

The ratios \(-4\Delta W_+/48\mathrm{RV}\) are \(1.033, 1.060, 1.058, 1.030\), confirming the range \([1.03,1.06]\). \(Q/x_0^2\) depends on the family: about 3–4 for the \(H^4\) \(X=64\) cells, about \(10^{-2}\) for the scalar-optimized CH cells. So "\(Q\sim x_0^2\)" is family-specific. The family-independent statement is \(Q\le\frac{13}{12}\int\sigma^2\).

## 7. Theorem H

**Verified.**
- (3.1) and (3.2) hold.
- Kobayashi's inequality gives \(\mathcal Y(X_k)\ge\mathcal Y(Y)\ge Y_{\rm hyp}\), using \(Y(\overline{\mathbb{CP}}^2)>0\). Hence (H) at \(k\) implies (H) at every \(k'\le k\).
- Part (1) holds, including strictness. Equality forces \(W^+=0\), \(\nabla u=0\) and \(Y[g]=\mathcal Y\). Then \(g\) globally minimizes \(S\), since \(S(h)\ge Y[h]^2\ge Y_{\rm hyp}^2\). The Euler–Lagrange equation at constant \(s\ne0\) gives \(\mathrm{Ric}=\tfrac s4g\), so \(P=0\), a contradiction.
- The Burns upper bound \(8\pi^2k(1+2x_0)+O(kx_0^{6/5})\) needs no (H).
- The \(t\)-bound holds: \(t\ge\frac1{12}-8\pi^2(2\chi-k)/S\ge k/(24\chi)\), which gives \(\mathcal J\ge4k/(k+6\chi)\).
- Burns sequences have \(S\to Y_{\rm hyp}^2\) (\(\Delta S=192\pi^2kx_0\)) and \(\int(s+24)^2\to0\). The latter needs all three regions of §4, not only the core.

**Corrections.**

(a) *Endpoint \(k=2\chi(Y)\).* Here \(2\chi+3\tau=0\), so \(P-S/12=4\int|W^+|^2\ge0\) for every metric. This gives \(\mathcal E\ge\mathcal J\ge1\) **without (H)**, and Burns gives \(\mathcal E\to1\). So \(\alpha(X_{2\chi})=1\) unconditionally. The 1/S coefficient vanishes, so equality does not force \(S=Y_{\rm hyp}^2\), and the non-attainment argument does not apply. Exactly:
- \(\mathcal E(g)=1\) iff \(W^+\equiv0\) and \(s\) is a nonzero constant;
- \(\mathcal J(g)=1\) iff \(W^+\equiv0\);
- attainment is equivalent to an anti-self-dual metric of constant nonzero scalar curvature on \(Y\#2\chi(Y)\overline{\mathbb{CP}}^2\), which is unresolved.

Non-attainment in (2) is proved for \(1\le k\le2\chi(Y)-1\). There, strict monotonicity in \(S\) forces \(S=Y_{\rm hyp}^2\), hence a Yamabe-attaining, hence Einstein, metric.

(b) *\(k>2\chi(Y)\).* Each metric has \(\mathcal J>1\). But conformal inflation keeps \(W^+\) fixed and has \(\Delta P=\Delta S/12\) exactly, with \(S\) unbounded, so \(\mathcal J\to1\). This is the ledger's "convex combination of \(J(\hat g)\) and 1". So \(\inf\mathcal J=1\) is not attained, while \(1\le\inf\mathcal E\le4k/(k+6\chi)\) is undetermined. The two normalizations separate here.

(c) *"Sharp value exactly when \(y_k=1\)".* Only sufficiency is proved. With \(y_k<1\), \(\inf P\) could still equal \(8\pi^2k\) through the \(W^+\) and \(Q\) terms.

(d) *Part (3).* \(\int|W^+|^2\to0\), \(Y[g_j]\to Y_{\rm hyp}\), \(S\to Y_{\rm hyp}^2\) and \(Q_j\to0\) follow. "\(8\pi^2\) carried by each exceptional class" is a localization statement that (3.2), a global identity, does not provide.

(e) *Citations.* LeBrun's attaining-implies-Einstein remark is in §5 of the supplied paper and is stated without proof. The self-contained Euler–Lagrange argument above replaces it. (H) remains the sole unproved input for parts (1), (2) with \(k<2\chi\), and (3).

**Exact corrected statement.**
- Under (H) at \(k\ge1\): (1) holds as written.
- For \(1\le k<2\chi(Y)\): \(\alpha=\inf\mathcal E=\inf\mathcal J=4k/(k+6\chi(Y))\), not attained.
- Unconditionally, at \(k=2\chi(Y)\): \(\alpha=\inf\mathcal E=\inf\mathcal J=1\), with attainment equivalent to the existence of a constant-scalar anti-self-dual metric.
- For \(k>2\chi(Y)\): \(\inf\mathcal J=1\), not attained, and \(\inf\mathcal E\in[1,4k/(k+6\chi)]\).
- Without (H), the unconditional bounds of the note hold, and \(y_k>1-k/(2\chi)\) is a sufficient condition for \(\alpha>0\).