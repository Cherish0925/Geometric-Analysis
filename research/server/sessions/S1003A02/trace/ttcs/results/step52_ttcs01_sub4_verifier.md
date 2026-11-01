# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step52_residual_norm_selection_absorption.md",
    "Sessions/S1003A02/workspace/notes/step51_residual_entry_link_charges_and_kahler_recovery.md",
    "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_verifier1_integration.md",
    "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_verifier2_integration.md",
    "Knowledge/objects/papers/The-long-time-behavior-of-fourth-order-curvature-flows--5b1863f1c7b9--f1cab1a2d745/object.md"
  ]
}
```

## Task

Verify Sections 1-2 of the Step-52 note on minimizing sequences of P(g)=∫|Ric°|² on closed four-manifolds. Check rigorously: (a) Proposition 52.1 — the harmonic-coordinate bootstrap from L^6 curvature, Sobolev and an L² residual of the gradient Q to W^{4,2} bounds, strong L^q convergence of curvature, and passage to an exact smooth P-critical limit (is the triangular structure Q = -ΔRic + a∇²s + b(Δs)g + Rm*Ric, tr Q = c0 Δs correct; are the Sobolev exponents in dimension four right, especially W^{2,6}⊂C^{1,1/3}, W^{2,2}⊂W^{1,4}, W^{4,2}⊂⊂W^{3,p}, p<4); (b) Proposition 52.2 — the logarithmic-cloud computation and whether it really shows that an own-scale L² residual cannot control pointwise curvature for the P-gradient (can the scalar profile be realized geometrically with small full residual?); (c) Proposition 52.4 — the contradiction proof via the L^6 curvature radius: point-picking, which integral-curvature harmonic-radius theorem is needed and whether it is true with a Sobolev bound, completeness and Euclidean volume growth of the limit, s≡0 by Yau, and the use of Tian–Viaclovsky small-energy regularity for scalar-flat Bach-flat complete metrics with a Sobolev bound; (d) Theorem 52.3 — whether (PS_ε) with the energy radius plus a uniform Sobolev bound really suffices for the orbifold/ALE structure without derivative hypotheses, and whether the remark r_ε ≥ cρ is right; (e) Section 2 — horizontality and length bound, the two warnings, the frozen-weight time-stepping construction and Theorem 52.5's deduction from Lemma 52.KS (is the deduction correct; is Lemma 52.KS a plausible true statement for this non-Willmore functional whose Weyl part is not dissipated; identify the exact obstacle or a counter-mechanism). Return a corrected statement of every item that is wrong or overstated, and distinguish proved, plausible-but-unwritten, and false.

## Output

# Verification memo: Step 52, §§1–2 (residual norm, small‑energy regularity, frozen‑weight selection)

## Summary

The elliptic core of §1 is correct. Proposition 52.1 is a valid bootstrap with the right four‑dimensional exponents. The logarithmic computation in Proposition 52.2 is correct, and it can be realized geometrically. Proposition 52.4 and Theorem 52.3 are correct modulo two items that are true but not yet written: an integral‑curvature harmonic‑radius lemma (the exponent condition the note states is the wrong one), and a modulus form of small‑energy regularity on neck annuli.

In §2 three things need correcting:

1. **Lemma 52.KS is false as stated.** Its two‑sided factor‑2 comparability at a fixed energy threshold \(\varepsilon\) cannot hold, for a purely measure‑theoretic reason.
2. **The named obstacle is the wrong one.** For \(P\) the Weyl part is parabolically smoothed, because the \(P\)-flow in dimension four is exactly Streets' \(\int|\mathrm{Rm}|^2\)-flow.
3. **The deduction of Theorem 52.5 is correct once the comparability is corrected.** For minimizing sequences it needs only two steps, not an infinite run. The genuinely open input is a step‑0 own‑scale regularization from critical (energy plus Sobolev) data.

Two identities organize much of what follows. With the full tensor norm \(|\mathrm{Rm}|^2=g^{ip}g^{jq}g^{kr}g^{ls}R_{ijkl}R_{pqrs}\), the decomposition \(|\mathrm{Rm}|^2=|W|^2+2|\mathrm{Ric}^\circ|^2+\tfrac16s^2\) and the Chern–Gauss–Bonnet density \(32\pi^2\mathrm{Pf}=|W|^2-2|\mathrm{Ric}^\circ|^2+\tfrac16s^2\) give

\[
\boxed{|\mathrm{Rm}|^2\,d\mu=32\pi^2\,\mathrm{Pf}+4|\mathrm{Ric}^\circ|^2\,d\mu\ \ \text{pointwise},\qquad \int_M|\mathrm{Rm}|^2=32\pi^2\chi(M)+4P(g).}\tag{0.1}
\]

Two consequences:

- The energy bound in Step 52 is an exact identity, not merely a bound.
- Streets' functional \(\mathcal F=\tfrac12\int|\mathrm{Rm}|^2\) equals \(16\pi^2\chi+2P\) in dimension four, so \(\operatorname{grad}\mathcal F=2Q\). The unweighted \(P\)-flow is Streets' flow (1.3) with time rescaled by 2. This matches leading terms: \(\delta d\,\mathrm{Rc}=-\Delta\mathrm{Ric}+\tfrac12\nabla^2s+\mathrm{Rm}*\mathrm{Ric}\).

---

## (a) Proposition 52.1: correct

**Structure of \(Q\).** Use \(\Delta=\operatorname{tr}\nabla^2\) and the standard first variations:

- \(\nabla\!\int|\mathrm{Ric}|^2=-\Delta\mathrm{Ric}+\nabla^2s-\tfrac12(\Delta s)g-2R_{ikjl}R^{kl}+\tfrac12|\mathrm{Ric}|^2g\);
- \(\nabla\!\int s^2=2\nabla^2s-2(\Delta s)g-2s\mathrm{Ric}+\tfrac12s^2g\).

Since \(P=\int|\mathrm{Ric}|^2-\tfrac14\int s^2\),
\[
Q=-\Delta\mathrm{Ric}+\tfrac12\nabla^2s-2R_{ikjl}R^{kl}+\tfrac12s\,\mathrm{Ric}+\tfrac12|\mathrm{Ric}|^2g-\tfrac18s^2g,\qquad \operatorname{tr}Q=-\tfrac12\Delta s .
\]
So \(a=\tfrac12\), \(b=0\) and \(c_0=-\tfrac12\). The zero‑order part is pointwise traceless, as scale invariance requires.

Two features matter for the bootstrap:

- The zero‑order term contains \(W*\mathrm{Ric}^\circ\). The full curvature, not only Ricci, must be in \(L^6\).
- \(c_0\neq0\) is what makes the system triangular: \(s\), then \(\mathrm{Ric}\), then \(g\). For \(\int|W|^2\), with \(c_0=0\), the scalar equation disappears and the bootstrap has no first rung.

**Exponents in dimension four.** All are correct:

- \(W^{1,6}\subset C^{0,1/3}\), so \(W^{2,6}\subset C^{1,1/3}\).
- \(W^{1,2}\subset L^4\), so \(W^{2,2}\subset W^{1,4}\).
- Rellich gives \(W^{1,2}\Subset L^p\) for \(p<4\), so \(W^{4,2}\Subset W^{3,p}\).
- For \(2<p<4\), \(W^{3,p}\subset W^{2,4p/(4-p)}\subset C^{1,\gamma}\). Letting \(p\uparrow4\) gives \(W^{2,q}\) for every \(q<\infty\).

**Each step of the bootstrap is valid:**

1. \(\Delta_g u=g^{kl}\partial_{kl}u\) holds exactly in harmonic coordinates. With \(g^{kl}\in C^{1,1/3}\) and \(\operatorname{tr}Q\in L^2\), this gives \(s\in W^{2,2}\).
2. The Ricci system has diagonal principal part \(g^{kl}\partial_{kl}\). Its first‑order coefficients \(\Gamma\) are in \(C^{0,1/3}\). Its zero‑order coefficients \(\partial\Gamma+\Gamma\Gamma\) are in \(L^6\), acting on \(\mathrm{Ric}\in L^6\), so they contribute in \(L^3\). The right side \(\nabla^2s-\Gamma\partial s+\mathrm{Rm}*\mathrm{Ric}+Q\) is in \(L^2\). Interior \(L^2\) theory gives \(\mathrm{Ric}\in W^{2,2}\).
3. Differentiating the harmonic‑coordinate equation once and twice gives \(W^{3,4}\) and then \(W^{4,2}\), exactly as written. In the second derivative the products \(\partial g\,\partial^3g\in L^4\) and \(\partial^2g\,\partial^2g\in L^q\) appear.
4. **Passage to the limit.** \(Q\) is linear in \(\partial^4g\) with coefficients in \(g\). The remaining terms are \(\partial^3g\,\partial g\), \((\partial^2g)^2\) and lower. So \(Q(g_i)\rightharpoonup Q(g_\infty)\) weakly in \(L^2\), and \(Q(g_\infty)=0\) a.e.

**Smoothness of the limit.** The same triangular structure bootstraps the limit with no gauge input. \(s_\infty\) solves \(g^{kl}\partial_{kl}s=0\) with \(C^{1,\gamma}\) coefficients, so \(s_\infty\in C^{2,\gamma}\). Then \(\mathrm{Ric}\in W^{2,q}\), \(g\in W^{3,q}\subset C^{2,\gamma}\), and the iteration continues. The appeal to GV Prop. 3.3 is not needed.

The constant \(C\) depends on the harmonic radius and \(C^{1,\beta}\) norm, on \(\Lambda\), and on \(\sup_i\|Q(g_i)\|_{L^2}\).

**Hypothesis wording.** "(e.g. from \(L^6\) plus Sobolev — see 52.4)" conflates two results. Proposition 52.4 yields an \(L^6\) bound. The harmonic radius is a separate lemma; see (c).

---

## (b) Proposition 52.2: correct, and realized by metrics

**The computation checks out.** Set \(L=\log(1/r)\). Then
\[
\|h_\sigma\|_2^2=2\pi^2\!\int_{L/2}^{L}\!\frac{dL'}{L'^2}=\frac{2\pi^2}{\log(1/\sigma)},\qquad
u_\sigma(0)=\tfrac12\!\int_{L/2}^{L}\!\frac{dL'}{L'}=\tfrac12\log2 .
\]
Moreover \(0\le u_\sigma\le\tfrac12\log2\) and \(u_\sigma\) is concentrated in \(|x|\lesssim\sigma^{1/2}\), so \(u_\sigma\to0\) in every \(L^q_{\rm loc}\). Here \(-\Delta u_\sigma=h_\sigma\). The example is the sharp failure of \(W^{2,2}\subset L^\infty\) in four dimensions.

**A geometric realization.** The note stops at the scalar profile. A metric realization follows. On a flat patch (or on a flat region of any metric), let \(\eta\) be a fixed cutoff and set
\[
\varphi_\sigma=\tfrac{\lambda}{6}\,\eta\,(\Gamma*u_\sigma),\qquad g_\sigma=e^{2\varphi_\sigma}\delta,\qquad s_{g_\sigma}=-6e^{-2\varphi_\sigma}\big(\Delta\varphi_\sigma+|\nabla\varphi_\sigma|^2\big).
\]
Its properties:

- \(\|\varphi_\sigma\|_{W^{4,2}}\lesssim\lambda\|u_\sigma\|_{W^{2,2}}\to0\), so \(\nabla\varphi_\sigma\to0\) uniform (since \(W^{4,2}\subset C^{1,\gamma}\)).
- \(s_{g_\sigma}(0)\to\tfrac{\lambda}{2}\log2\neq0\).
- \(Q(g_\sigma)\) is a polynomial in \(\partial^{\le4}\varphi_\sigma\). Its terms \(\partial^4\varphi\), \(\partial^3\varphi\,\partial\varphi\) and \((\partial^2\varphi)^2\) all tend to zero in \(L^2\). The last uses \(\partial^2\varphi\in W^{2,2}\subset L^q\).
- \(\Delta\varphi_\sigma\) is bounded, so Calderón–Zygmund gives uniform \(L^6\) bounds on \(\partial^2\varphi_\sigma\), hence on \(\mathrm{Rm}\).
- \(\int|\mathrm{Rm}|^2\to0\) and \(g_\sigma\to\delta\) in \(W^{4,2}\).

Because the cloud carries vanishing energy, the energy radius there equals the cap. The weight \(r_\varepsilon^4\) is therefore of order one, and \((\mathrm{PS}_\varepsilon)\) holds.

Hence, near any fixed metric (an Einstein minimizer, for instance), there are \((\mathrm{PS}_\varepsilon)\) sequences with \(P\to\alpha\) that satisfy every hypothesis of 52.1 while \(|\mathrm{Rm}|\) does not converge pointwise. Two conclusions follow:

- The convergence class \(C^{1,\beta}\cap W^{2,q}\) in Theorem 52.3 cannot be improved to \(C^2\) under \((\mathrm{PS}_\varepsilon)\).
- An \(L^{2+\eta}\) own‑scale residual does give \(L^\infty\) control, as stated. \(\Delta s\in L^{p}\) with \(p>2\) gives \(s\in W^{2,p}\subset C^0\), and similarly \(g\in W^{4,p}\subset C^{2,\gamma}\).

---

## (c) Proposition 52.4: correct modulo a harmonic‑radius lemma

**Point‑picking.** \(r^{(q)}\) is 1‑Lipschitz. The map \(r\mapsto r^{2q-4}\int_{B(x,r)}|\mathrm{Rm}|^q\) is nondecreasing and \(B(y,r-d)\subset B(x,r)\). Maximizing \(d(x,\partial B(x_0,1))/r^{(6)}(x)\) gives the stated \(y_i,\lambda_i,A_i\) with \(B(y_i,A_i\lambda_i)\) inside the ball. Hence the limit is complete.

**Normalization of the limit.** \(r^{(6)}\ge\tfrac12\) gives \(\int_{B(y,1/2)}|\mathrm{Rm}|^6\le 2^8\). Below the cap, \(\int_{B(y_i,1)}|\mathrm{Rm}|^6=1\).

**The residual condition is subcritical, so \(\eta_0\) need not be small.** After rescaling, the residual is \(\lambda_i^4\eta_0\to0\) for any finite \(\eta_0\). The proposition holds with \(C=C(C_S,\eta_0)\) for every \(\eta_0<\infty\). Only \(\varepsilon_0\) has to be small.

**The harmonic‑radius lemma has the wrong exponent condition.** The note writes "\(p=3>n/2\)". With \(\int|\mathrm{Rm}|^q\) bounded for \(n/2<q\le n\), harmonic coordinates give only \(g\in W^{2,q}\). That is \(C^{0,\alpha}\), not \(C^{1,\beta}\), and does not feed 52.1. What 52.1 needs is \(q>n=4\); \(q=6\) qualifies.

The needed statement, for fixed \(q>4\) and \(C_S\):

> If \(\rho^{2q-4}\int_{B(z,\rho)}|\mathrm{Rm}|^q\le\Lambda\) for all \(z\in B(y,2r)\) and \(\rho\le r\), and the scale‑invariant Sobolev inequality holds on these balls, then the \(W^{2,q}\) (hence \(C^{1,1-4/q}\)) harmonic radius at \(y\) is at least \(c(q,\Lambda,C_S)\,r\).

It is provable by Anderson's harmonic‑radius blow‑up:

1. Rescale to harmonic radius 1 at a point‑picked minimum.
2. The \(L^q\) quantity is subcritical and tends to zero.
3. Sobolev gives Euclidean volume growth.
4. The limit is a complete flat manifold with Euclidean volume growth, hence \(\mathbb R^4\).
5. This contradicts continuity of the harmonic radius under \(C^{1,\beta'}\) convergence with uniform \(W^{2,q}\) bounds.

Integral‑curvature compactness papers (D. Yang, Petersen–Wei) treat related settings, but their exact hypotheses differ. The lemma is most cleanly written out directly.

**Properties of the limit.**

- *Euclidean Sobolev.* Fix compactly supported \(u\) and let \(R\to\infty\) in the inequality on \(B(y,R)\); the \(R^{-2}\int u^2\) term disappears. So \(\|u\|_4\le C\|\nabla u\|_2\) on the limit, and \(\operatorname{vol}B(y,R)\ge cR^4\).
- *Scalar curvature vanishes.* \(s\) is harmonic and \(\int s^2\le C\varepsilon_0\) by lower semicontinuity. Yau's \(L^p\) Liouville theorem makes \(s\) constant, and infinite volume makes it zero.
- *Bach‑flat.* This then follows from \(B=\tfrac s3\mathrm{Ric}^\circ\).
- *Flat.* Small‑energy regularity for scalar‑flat Bach‑flat metrics with a Sobolev bound gives \(\sup_{B(y,R/2)}|\mathrm{Rm}|\le CR^{-2}\varepsilon_0^{1/2}\). Sources: Tian–Viaclovsky for Bach‑flat, scalar‑flat metrics; Anderson Prop. 3.5, with Sobolev‑dependent constants, as checked in Step 51. Letting \(R\to\infty\) makes the limit flat.
- *Contradiction.* Strong \(L^6\) convergence from 52.1 gives \(\int_{B(y_\infty,1+\delta)}|\mathrm{Rm}_\infty|^6\ge1\).

---

## (d) Theorem 52.3 and the remark on \(r_\varepsilon\)

**The remark is correct.** \(|\mathrm{Rm}|\le\rho^{-2}\) on \(B(x,\rho)\) and Bishop give \(\int_{B(x,c\rho)}|\mathrm{Rm}|^2\le Cc^4\). So \(r_\varepsilon\ge\min\{(\varepsilon/C)^{1/4}\rho,\,r_0\}\), and \((\mathrm{PS}_\varepsilon)\) implies the curvature‑radius residual. The cloud in (b) shows the converse is false.

**Entry into the theorem is correct.**

- The Lipschitz property makes \(r_\varepsilon(z)\ge\tfrac34r_\varepsilon(x)\) on \(B(x,r_\varepsilon(x)/4)\).
- Proposition 52.4 applies at every such \(z\). With the lemma in (c), the harmonic radius is \(\gtrsim r_\varepsilon\).
- The number of concentration points is at most \((32\pi^2\chi+4\sup P)/\varepsilon\), by (0.1).
- Sobolev at scales \(\le1\) gives (NC).

**Three items are true but unwritten; each is needed in place of Anderson's \(L^\infty\) curvature control.**

1. **Residual at bubble scales holds only away from deeper points.** At a bubble point \(p\) with \(r_\varepsilon(p)=\lambda\), the weight is small near deeper concentration points inside \(B(p,A\lambda)\). So \((\mathrm{PS}_\varepsilon)\) controls the rescaled residual only on compact subsets of the regular part of the rescaled limit, where \(r_\varepsilon\ge c(\delta)\lambda\). Exact criticality is obtained there. It extends across the finitely many deeper points by the removable‑singularity theorem for critical metrics with finite energy and a Sobolev bound (Tian–Viaclovsky), which produces orbifold points.
2. **Necks need a modulus form of small‑energy regularity.** On a neck, each dyadic annulus has \(r_\varepsilon\gtrsim|x|\), so its rescaled residual tends to zero. But 52.4 gives only *bounded* \(L^6\). Identifying the links as \(S^3/\Gamma\) requires *closeness* to a flat cone. This follows by contradiction from 52.1 and 52.4: energy and residual tending to zero give an exact critical limit with zero energy, which is flat, so the annuli are \(C^{1,\beta}\)-close to flat annuli. The argument is short, but it is a separate proposition.
3. **The Theorem‑G ledger.** It is applied to the smooth exact limits (bulk, bubbles), as Step 51 requires. Where APS transgression terms on slices of the approximating metrics are used, they make sense for \(\mathrm{Rm}\in W^{2,2}\) on Fubini‑generic slices.

**Attainment without concentration improves.** \(\mathrm{Ric}^\circ\) converges strongly in \(L^2\), so \(P(g_\infty)=\lim P(g_i)=\alpha\) holds with equality, not merely by lower semicontinuity. With bubbles, only (5.1)–(5.2) of Step 51 remain, since the neck energy is uncontrolled.

---

## (e) Section 2: selection

### What is correct

- **Horizontality and scale invariance.** \(\langle wQ,\mathcal L_Xg\rangle_w=DP(\mathcal L_Xg)=0\), and \(\langle\cdot,\cdot\rangle_w\) is scale invariant when \(w\sim\text{length}^4\).
- **Dimensionless time.** \(wQ\) scales like \(g\).
- **Speed and length.** The speed is \((\int w|Q|^2)^{1/2}\), and the length is at most \(\sqrt{T\delta}\) by Cauchy–Schwarz.
- **Volume renormalization.** It is free: \(DP_g(g)=\int\operatorname{tr}Q=0\) and \(\langle wQ,g\rangle_w=0\). The flow itself does change volume, at rate \(-\tfrac{c_0}{2}\int w\Delta s\neq0\).
- **The two warnings are right.** For (ii): a ripple carrying energy \(\varepsilon\) at scale \(\rho\) has amplitude \(a\sim\varepsilon^{1/2}(\nu\rho)^{-2}\) and \(w\)-length\({}^2\) \(\sim\varepsilon(\nu\rho)^{-4}\to0\).
- **Gauge.** The DeTurck background is reset at each refreeze. Steps are composed by diffeomorphisms, and \(P\), \(Q\) are equivariant. The law \(P'=-\int w_n|Q|^2\) holds exactly.

### Lemma 52.KS as stated is false

The comparability \(\tfrac12r_\varepsilon(t_n)\le r_\varepsilon(t)\le2r_\varepsilon(t_n)\) at a fixed threshold fails for any evolution that changes local energies by any amount \(\eta>0\). This is a plateau mechanism.

- *Upper inequality.* Suppose \(\int_{B(x,r)}|\mathrm{Rm}|^2\) reaches \(\varepsilon\) at \(r=\rho\) and stays within \(\eta\) of \(\varepsilon\) on \([\rho,100\rho]\). A loss of \(\eta\) in \(B(x,\rho)\) moves \(r_\varepsilon(x)\) to about \(100\rho\).
- *Lower inequality.* Suppose the energy reaches \(\varepsilon-\eta\) at \(r=\rho/100\) and stays nearly flat up to \(\rho\). A gain of \(\eta\) moves \(r_\varepsilon(x)\) to about \(\rho/100\).

The correct form uses shifted thresholds:
\[
c\,r_\varepsilon(g(t_n))\le r_{2\varepsilon}(g(t)),\qquad r_{\varepsilon/2}(g(t))\le C\,r_\varepsilon(g(t_n)).\tag{KS′}
\]
The deduction of Theorem 52.5 uses only the second inequality: \(w_n\ge c\,r_{\varepsilon/2}(g(t))^4\). It then outputs \((\mathrm{PS}_{\varepsilon/2})\), and Theorem 52.3 accepts any \(\varepsilon\le\varepsilon_0\). With (KS′) the deduction is correct.

### The obstacle named in the note is not the real one

**The Weyl part is parabolically smoothed.** Write \(L(h)\) for the leading part of \(D\mathrm{Rm}(h)\). The Ricci‑flow identity gives \(L(\mathrm{Ric})=-\tfrac12\Delta\mathrm{Rm}\). The Hessian term contributes only lower order, since \(\nabla^2s=\tfrac12\mathcal L_{\nabla s}g\) and \(D\mathrm{Rm}(\mathcal L_Xg)=\mathcal L_X\mathrm{Rm}\). Because \(b=0\), there is no \((\Delta s)g\) term. Hence
\[
\partial_t\mathrm{Rm}=-\tfrac12\Delta^2\mathrm{Rm}+P^2_2(\mathrm{Rm})+P^0_3(\mathrm{Rm})
\]
for the unweighted \(P\)-flow. This is exactly Streets' FOCF form (1.1), consistent with the identification in (0.1).

Streets' Proposition 4.3 at \(m=0\) then gives a local inequality with dissipation \(\int\gamma^s|\nabla^2\mathrm{Rm}|^2\) for the full curvature, Weyl included. The weighted flow adds \(\nabla w*\nabla^3\mathrm{Rm}\) and \(\nabla^2w*\nabla^2\mathrm{Rm}\), which are lower order at own scale given \(|\nabla^jw|\lesssim\rho^{4-j}\) for \(j\le2\).

**The localized energy identity has no separate undissipated Weyl term.** It reads exactly
\[
\frac{d}{dt}\int\gamma|\mathrm{Rm}|^2=-4\int\gamma\,w|Q|^2+\mathcal F_\gamma,\qquad
|\mathcal F_\gamma|\lesssim\int\big(|\nabla^2\gamma||\mathrm{Rm}|+|\nabla\gamma||\nabla\mathrm{Rm}|\big)\,w|Q|.
\]
After two integrations by parts in the Pfaffian transgression and in \(D|\mathrm{Ric}^\circ|^2\), the flux contains no derivative of \(w\). There is no \(s^2\) term either, with the full norm in (0.1).

**This yields an energy‑transport estimate.** Cauchy–Schwarz in \((x,t)\), together with a time‑slice elliptic estimate, gives
\[
\Big|\int\gamma|\mathrm{Rm}|^2\Big|_{t_n}^{t}\Big|\le4D+C\sqrt{D\,(D+c_1\varepsilon)},\qquad D=\int_{t_n}^{t}\!\!\int w|Q|^2 .\tag{T}
\]
The time‑slice estimate is
\[
\rho^4\int\gamma|\nabla^2\mathrm{Rm}|^2\lesssim\rho^4\int|Q|^2+\int_{\operatorname{supp}\gamma}|\mathrm{Rm}|^2 .
\]
It comes from the chain \(\operatorname{tr}Q\to\Delta s\to\Delta\mathrm{Ric}\to\Delta\mathrm{Rm}\) via Bochner integrations by parts, with the nonlinear terms absorbed by small energy and Sobolev; this is the quantitative form of 52.1.

Thus when the dissipation is small, as in minimizing sequences or late steps, local energies are nearly frozen and (KS′) follows. The estimate needs \(|\nabla\gamma|_{g(t)}\lesssim\rho^{-1}\) and \(|\nabla^2\gamma|_{g(t)}\lesssim\rho^{-2}\), that is, \(C^1\) control of \(g(t)\) relative to \(g(t_n)\) on own‑scale balls.

**The true obstacle is intrinsic localization from critical data.** From data with only small energy and Sobolev, the smoothing scale gives \(|\nabla^2\mathrm{Rm}|\lesssim\varepsilon^{1/2}t^{-1}\) in own‑scale units. Then \(|\partial_tg|=w|Q|\lesssim t^{-1}\), and the metric drift is logarithmically divergent at \(t=0\). This is the same \(W^{2,2}\not\subset L^\infty\) borderline as in (b).

KS avoid this through ambient Euclidean cutoffs. For intrinsic metrics it is exactly Streets' open Remark 1.14 (localizing Theorem 1.3; a curvature bound does not give \(C^0\) metric control), together with Remark 1.12 (noncollapsing).

From data with own‑scale \(L^6\) curvature (subcritical) the drift is integrable:

- \(\sup|\mathrm{Rm}|\lesssim t^{-1/6}\) and \(|\nabla^2\mathrm{Rm}|\lesssim t^{-2/3}\), so the \(C^0\) drift is \(O(t^{1/3})\);
- \(|\nabla(wQ)|\lesssim t^{-11/12}\) is integrable, so the \(C^1\) drift is \(O(t^{1/12})\).

### Corrected structure of the selection

- **For minimizing sequences, two steps suffice.** Each \(D_n\le\delta_i\to0\), so step 1 alone yields \(t\) with \(\int r_{\varepsilon/2}(g(t))^4|Q|^2\le C\delta_i/c_1\). The infinite run and long‑time Sobolev persistence are needed only to select from a single \(g_0\).
- **Steps \(n\ge1\) start from own‑scale smooth data.** In the rescaled picture \(\rho^{-2}g\), which has bounded geometry, existence for a uniform time \(c_1\), \(C^k\)-closeness to the initial data, Sobolev \(\le2C_S\), and (KS′) follow from standard local Schauder theory for a quasilinear fourth‑order parabolic system plus continuation. This is plausible and standard but unwritten.
- **Step 0 contains the whole open content.** From arbitrary \(g_i\) with energy and Sobolev bounds, one must reach, at \(P\)-cost \(o(1)\), a metric that is smooth at own scale with universal constants. Its weight must also have own‑scale \(C^2\) bounds relative to \(g_0\), which energy and Sobolev data do not supply. Streets' reference [15] (small initial energy) has the title of the closest global analogue for this flow; its contents are not in the supplied material.

---

## Corrected statements

- **52.1.** As written. Add the explicit formula \(Q=-\Delta\mathrm{Ric}+\tfrac12\nabla^2s+\mathrm{Rm}*\mathrm{Ric}+(s,\mathrm{Ric})\)-quadratic terms, with \(\operatorname{tr}Q=-\tfrac12\Delta s\). Note that smoothness of the limit follows from the triangular bootstrap without GV. The constants depend on the \(C^{1,\beta}\) harmonic radius, \(\Lambda\), and \(\sup\|Q\|_2\).
- **52.2.** Add the realization \(g_\sigma=e^{2\varphi_\sigma}\delta\). It shows that \((\mathrm{PS}_\varepsilon)\) minimizing sequences can have non‑convergent pointwise curvature, so the \(C^{1,\beta}\cap W^{2,q}\) convergence of 52.3 is optimal.
- **52.4.** Allow any finite \(\eta_0\), with \(C=C(C_S,\eta_0)\). Replace "\(p=3>n/2\)" by the lemma for \(q>4\) stated in (c).
- **52.3.** Add the three written ingredients from (d): residual at bubble scales on compact subsets of the regular part with removable singularities; modulus small‑energy regularity on necks; and \(\int|\mathrm{Rm}|^2=32\pi^2\chi+4P\). Without concentration, \(P(g_\infty)=\alpha\) exactly.
- **52.KS.** Replace fixed‑\(\varepsilon\) comparability by (KS′). Replace the Weyl remark by the FOCF structure and the transport estimate (T). Name the step‑0 critical localization as the open problem.
- **52.5.** Under existence of a step‑0 regularization (own‑scale smooth metrics \(h_i\) with \(P(h_i)-\alpha\to0\) and uniform Sobolev bounds), one uniform step produces a \((\mathrm{PS}_{\varepsilon/2})\) minimizing sequence with Sobolev \(\le2C_S\).

## Status table

| Item | Status |
|---|---|
| \(Q\) triangular form; \(b=0\), \(c_0=-\tfrac12\) | proved |
| 52.1 bootstrap, exponents, weak passage, smooth limit | proved |
| 52.2 computation | proved |
| 52.2 geometric realization in \((\mathrm{PS}_\varepsilon)\) sequences | proved (conformal construction above) |
| \(L^{2+\eta}\) residual gives \(L^\infty\) curvature | proved |
| Harmonic radius from \(L^q\) curvature, \(q>4\), plus Sobolev | true, unwritten (Anderson blow‑up) |
| Exponent "\(p=3>n/2\)" | wrong condition; \(q>4\) is needed |
| 52.4, including \(\eta_0\) arbitrary | proved modulo the radius lemma |
| \(r_\varepsilon\ge c(\varepsilon)\rho\) | proved |
| 52.3 orbifold/ALE structure | proved modulo radius lemma, neck modulus regularity, removable singularities |
| Horizontality, length bound, volume renormalization, warnings | proved |
| P-flow = Streets' \(\int|\mathrm{Rm}|^2\)-flow in 4D; full Rm parabolic | proved |
| "Weyl not dissipated" as the obstacle | incorrect |
| KS factor‑2 comparability at fixed \(\varepsilon\) | false (plateau) |
| (KS′) with small dissipation, via (T) | plausible; needs \(C^1\) metric control |
| Steps \(n\ge1\) from own‑scale smooth data | plausible, standard parabolic theory |
| Step 0 from energy + Sobolev data | open (critical, log‑borderline; Streets Rem. 1.12/1.14) |
| 52.5 deduction given (KS′) | proved; two steps suffice for minimizing sequences |