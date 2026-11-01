# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step76_mixed_row_reduced_obstruction_map.md",
    "Sessions/S0910A01/workspace/data/step76_harmonic_pairing_analysis.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the reduced obstruction-map formulation for Einstein desingularization of (S^2 x S^2)/Z_2. The note claims: (1) All first obstructions lambda_k^j vanish automatically when the EH direction zeta_j lies in the 2D kernel of R^{pm} = diag(Lambda, 0, 0). (2) The second obstruction mu_1^j vanishes because the 2x2 remaining block has determinant 0 (one eigenvalue is 0, the other is Lambda). (3) The leading surviving obstruction is the global system nu_l, which pairs H^4 (the r^{-4} EH correction) against V_{l,2} (quadratic jet of orbifold kernel modes) via an L^2 integral on S^3/Z_2. (4) H^4 restricted to S^3 lives in l=2 tensor harmonics (NOT constant) because theta_1^-(x) depends on x through the quaternionic conjugation formula theta_i^-(x) = sum_j (x^T(omega_i^+ circ omega_j^-) x/|x|^2) omega_j^-, making it quadratic in x. (5) V_{l,2} also lives in l=2 tensor harmonics, so the pairing is not automatically zero by representation theory. (6) The reduced system has 4 in-kernel angle unknowns and at most 4 global equations, giving a generically solvable dimension count. Check each claim against the Ozuch source, identify any errors in the curvature calculation (R^+ on S^2 x S^2), the angular structure of lambda_k near the kernel, and the harmonic-degree argument. Does the trigonometric form sum_j (A_l^j cos alpha_j + B_l^j sin alpha_j) = 0 correctly capture the alpha-dependence of nu_l?

## Output

# Verification Memo: Reduced Obstruction Map for $(S^2\times S^2)/\mathbb{Z}_2$ Einstein Desingularization

## Summary judgment

The local curvature algebra at the nodes and the automatic vanishing of the first and second Ozuch obstructions are correct. But two structural pieces of the reduced map are not sound: (a) the deformation space $\mathbf{O}(g_o)$ that feeds the global $\nu_l$ system is, for this orbifold, zero-dimensional, so the "leading surviving system" as written does not exist; and (b) the angular dependence of $\nu_l$ is a **double-angle** trigonometric form, not the single-angle $A\cos\alpha_j+B\sin\alpha_j$ used in §4.4–4.5. I work through each item below.

---

## 1. Curvature at the nodes: $\mathbf R^\pm=\mathrm{diag}(\Lambda,0,0)$ — correct, with one numerical slip

Direct computation on $S^2\times S^2$ with each factor of Gauss curvature $K=\Lambda$: the only nonzero curvature components are $R_{1212}=R_{3434}=K$. The curvature operator on $\Lambda^2$ is diagonal with eigenvalue $K$ on $e^{12}$ and $e^{34}$ and $0$ on the four mixed 2-forms. Hence for $\omega_1^\pm=e^{12}\pm e^{34}$, $\mathcal R\,\omega_1^\pm=K\,\omega_1^\pm$ and $\mathcal R\,\omega_{2,3}^\pm=0$. So
$$
\mathbf R^+=\mathbf R^-=\mathrm{diag}(\Lambda,0,0),\qquad \operatorname{tr}\mathbf R^\pm=\Lambda=\tfrac{s}{4},\ \ s=4K,
$$
confirming rank 1 with a 2-dimensional kernel. This matches Ozuch's convention (verified against Example 2.1, where $\operatorname{tr}\mathbf R^-=s/4$). The note's rank/kernel statement is right, and this is exactly Ozuch's obstruction (3) *and* the stronger "Kähler-type" form (4) $\mathbf R^\pm=\mathrm{diag}(0,0,\Lambda)$ being satisfied at every node.

**One numerical error to fix.** The prose in §1.2 gives $W^+=W^-=\mathrm{diag}(\Lambda/3,-\Lambda/6,-\Lambda/6)$. With $s/12=\Lambda/3$,
$$
W^+=\mathbf R^+-\tfrac{s}{12}I=\mathrm{diag}\!\big(\tfrac{2\Lambda}{3},-\tfrac{\Lambda}{3},-\tfrac{\Lambda}{3}\big),
$$
i.e. the stated Weyl eigenvalues are off by a factor of 2 (both are traceless, so the mistake is only in magnitude). This does not affect the kernel structure but should be corrected.

---

## 2. Vanishing of $\lambda_k^j$ and $\mu_1^j$ — correct, and it places the route in Ozuch's "forced-Kähler" regime

With $\phi_j\in\ker\mathbf R^\pm=\operatorname{span}(\omega_2^\pm,\omega_3^\pm)$, Ozuch eq. (28) gives $\lambda_k^j=c\langle\mathbf R^\pm\phi_j^\pm,\phi_{j,(k)}^\pm\rangle=0$. In the basis $(\phi_j,\phi_{(2)},\phi_{(3)}=\omega_1^\pm)$ one has $\mathbf R^\pm=\mathrm{diag}(0,0,\Lambda)$, so the $2\times2$ block orthogonal to $\phi_j$ is $\mathrm{diag}(0,\Lambda)$ and Lemma 2.14 gives $\mu_1^j=C\det\mathrm{diag}(0,\Lambda)=0$. Both are correct, and the $\phi^0_j$ (in-kernel angle) is genuinely a free parameter as claimed. The linear/quadratic split of $\lambda_1,\lambda_2,\lambda_3$ in $\epsilon_3$ in §3.2 is also consistent with $\mathbf R^\pm\phi^+\propto\epsilon_3\,\omega_1^+$.

A scientific point the note underplays: because $\mathbf R^\pm=\mathrm{diag}(\Lambda,0,0)$ *is* the Kähler-Einstein curvature form (the product is Kähler–Einstein), the mixed-chirality gluing is precisely the situation Ozuch's Theorem 0.2 / Question 0.8 identifies as pushing toward "the desingularization must be Kähler." The automatic vanishing here is not an opening; it is the signature that the first two orders cannot distinguish the mixed-orientation route, exactly as in Ozuch's $\mathbb T^4/\mathbb Z_2$ analysis. The note's framing ("leading surviving obstruction") should be read against this: vanishing of $\lambda,\mu$ is generic to this Kähler-type node, not special to the configuration.

---

## 3. Central problem: $\mathbf O(g_o)=0$, so the $\nu_l$ system is empty

Ozuch's $\nu_l$ (eq. 39) pairs $H^4$ against $V_{l,2}$, the quadratic jet of $\mathbf v_l\in\mathbf O(g_o)=\ker P_{g_o}$, where $\mathbf O(g_o)$ is the space of genuine infinitesimal Einstein deformations. The note's §1.3 is internally contradictory: it states $\dim\mathbf O_{\rm TT}(g_o)=0$, then asserts a 4-dimensional $\ker P_{g_o}$ of "scalar/gauge/conformal directions," and then calls these "the genuine integrable Einstein deformations." Gauge (Lie-derivative) and conformal directions are not Einstein deformations and do not enter $\nu_l$; they are divided out in Bianchi gauge.

The genuine space is zero. $S^2\times S^2$ is infinitesimally Einstein-rigid. Concretely, the candidate "shape" mode $h_0=g_1-g_2$ (traceless, parallel, hence TT) satisfies
$$
\nabla^*\nabla h_0=0,\qquad \mathring R\,h_0=\Lambda h_0,
$$
so the Einstein-deformation equation $\nabla^*\nabla h=2\mathring R\,h$ reads $0=2\Lambda h_0\neq0$. Thus $h_0$ is a *destabilizing* direction (negative eigenvalue of $\tfrac12\nabla^*\nabla-\mathring R$), not a zero mode. It is not in $\mathbf O(g_o)$. The $\mathbb Z_2$ quotient only restricts to invariant modes, so $\dim\mathbf O(g_o)=0$ on the orbifold as well.

Consequences:
- The "shape deformation $\delta g=\delta\rho_1 g_1-\delta\rho_2 g_2$" the note places in the kernel is not an infinitesimal Einstein deformation; the reasoning that led to $d\le4$ is not valid.
- With $d=0$, the reduced map is $\mathcal F:(S^1)^4\to\mathbb R^0$, and there is no $\nu_l$ obstruction at all. All of Ozuch's *computed* obstructions ($\lambda,\mu,\nu$) then vanish, vacuously for $\nu$.
- The statement "$\nu_l$ is the leading surviving obstruction" is therefore incorrect for this orbifold. If the first two orders vanish and $\nu$ is empty, the leading nontrivial obstruction sits at an order Ozuch does not compute in closed form (a third-order term, cf. the unresolved higher obstructions Ozuch alludes to in Question 0.8 and Conjecture 2.22).

This is the item most in need of resolution. Either (i) accept $d=0$ and recognize that the reduced map cannot be the operative obstruction, or (ii) the strategy is actually a *partial* resolution (glue some nodes first, then treat the resulting hyperkähler/Kähler partial desingularization $\mathbf g_\pm$ as the new $M_o$, whose moduli $\mathbf O(\mathbf g_\pm)$ are the bubble parameters — this is the $3|S_\pm|+9$-dimensional space in Ozuch §3.2–3.3). If (ii) is intended (the "mixed-row" language suggests it), then $\mathbf v_l$ are deformations of already-glued bubbles, not deformations of the product, and §1.3 must be rewritten accordingly; the "$\dim\ker P_{g_o}=4$ on the product orbifold" statement is then irrelevant.

---

## 4. Harmonic degree of $H^4$: $\ell=2$ — correct

$H^4(\zeta^+)=-\dfrac{\rho(\zeta)^-\circ\zeta^+}{2r^4}$ with $\rho_x(\zeta)_j=\dfrac{x^\top(\zeta^+\circ\omega_j^-)x}{|x|^2}$. The coefficients are degree-2 harmonic polynomials in $x/|x|$, i.e. $\ell=2$ tensor harmonics on $S^3$ (the "second eigenvalue," fourth on $S^3$, as Ozuch notes in the Lemma 3.15 proof), living in $\Omega^+\otimes\Omega^-\cong(1,1)$ of $SU(2)_+\times SU(2)_-$ (dimension $9$). This is correct and consistent with Ozuch's orthogonality argument in the Prop. 2.10 proof (pairing with the constant term $V_{l,0}$ vanishes by eigenvalue mismatch; only $V_{l,2}$ survives). The note's "not constant on $S^3$" conclusion is right, and there is no automatic representation-theoretic vanishing of the pairing per se.

---

## 5. Angular form of $\nu_l$: the single-angle expression is wrong; it is double-angle

This is a concrete calculational error. $H^4(\zeta^+)=-\dfrac{\rho(\zeta)^-\circ\zeta^+}{2r^4}$ is **bilinear** in $\zeta$: both $\rho(\zeta)^-$ and $\zeta^+$ are linear in $\zeta$, so $H^4$ scales as $|\zeta|^2$ (consistent with the note's own order ledger $\nu_l=O(|\zeta|^2)$). Writing the in-kernel unit direction as $\phi_j=\cos\alpha_j\,\omega_2^\pm+\sin\alpha_j\,\omega_3^\pm$,
$$
H^4(\phi_j)=-\frac{1}{2r^4}\big[\cos^2\!\alpha_j\,\rho(e_2)^-\!\circ\omega_2^+ +\cos\alpha_j\sin\alpha_j\,(\rho(e_2)^-\!\circ\omega_3^+ +\rho(e_3)^-\!\circ\omega_2^+)+\sin^2\!\alpha_j\,\rho(e_3)^-\!\circ\omega_3^+\big].
$$
Because $\cos^2,\ \sin^2,\ \cos\sin$ collapse to $\{1,\cos2\alpha_j,\sin2\alpha_j\}$, the correct reduced system is
$$
\boxed{\;\nu_l=\sum_{j}\big(\tilde A_l^{\,j}+\tilde B_l^{\,j}\cos 2\alpha_j+\tilde C_l^{\,j}\sin 2\alpha_j\big)=0\;}
$$
not $\sum_j(A_l^j\cos\alpha_j+B_l^j\sin\alpha_j)$. The error in §4.2 is that $\theta_1^-$ was held fixed (its $\zeta=(1,0,0)$ value) while only the $\omega^+$ factor was rotated; in fact $\rho(\zeta)^-$ rotates with $\zeta$ too. Ozuch eq. (11)–(13) and Prop. 1.16 make the bilinearity explicit ($H^4=\tfrac{|\zeta|}{2}O_1^4$, with $O_1^4=\zeta^+_{(1)}\circ\rho(\zeta)^-/r^4$).

The important structural difference from the note's version: the corrected form has an $\alpha$-**independent** term $\sum_j\tilde A_l^{\,j}$. A pure $A\cos\alpha+B\sin\alpha$ system passes through the origin of its image ellipse; the double-angle system does not — its image is an offset ellipsoidal sum, and whether $0$ lies in it depends on the magnitudes of the constants versus the oscillating amplitudes. So even the dimension-count solvability heuristic in §4.5/§6.2 does not follow "generically"; the constant offset can obstruct or force solutions independent of the $4$-vs-$d$ count.

---

## 6. Dimension count and "generic solvability"

Given §3 ($d=0$) and §5 (double-angle plus constant), the "4 unknowns, $\le4$ equations, generically solvable" statement is not established. If $d=0$ the map is trivial (no equations); if instead the partial-resolution reading is intended, then both the number of equations and the coefficients $\tilde A,\tilde B,\tilde C$ must be recomputed from the corrected $H^4$ and from the actual $\mathbf O(\mathbf g_\pm)$. The degree-theory argument sketched in §6.2 should be redone for the offset double-angle system.

---

## 7. Necessity versus construction

Ozuch's Proposition 2.19 and the cited [Ozu20t/Ozu19b, Prop. 5.1] are used in the source to bound the obstructions and $\|g^A-\mathbf g_{\zeta,v}\|$ **assuming an Einstein metric already exists nearby** — i.e. they run in the necessity direction. The provided material does not contain a self-contained existence/construction theorem stating that vanishing $(\lambda,\mu,\nu)$ plus surjective $D\mathcal F$ *produces* an Einstein metric, in particular for $\Lambda>0$ with anti-self-dual (Ricci-flat) EH bubbles glued onto a positive Einstein orbifold. The note's §0/§4.1 phrase "combined with the Ozuch quantitative inverse would construct" is therefore an assertion that the given source does not underwrite. The construction half is the substantive [Ozu19a,b] gluing-perturbation machinery, whose applicability to the $\Lambda>0$ mixed-orientation setting is exactly what Ozuch's paper suggests is heavily obstructed at higher order (Question 0.8, Conjecture 2.22). This tension — the note reaching for existence in the regime Ozuch flags as forced-Kähler / obstructed — is the main scientific point to weigh before investing in the $A_l^j,B_l^j$ computation of §6–7.

---

## 8. Topology of the target and the Yau-26 relevance

The 4-point resolution has a fixed topological Euler characteristic. Underlying space of $(S^2\times S^2)/\mathbb Z_2$: $\chi=\tfrac12(\chi(S^2\times S^2)+\#\text{fixed pts})=\tfrac12(4+4)=4$; resolving each of the 4 nodes by $T^*S^2$ raises $\chi$ by 1 each, giving $\chi(M)=8$, hence $b_2=6$ for the simply connected resolution. This is independent of the chirality pattern (only the signature changes). Therefore the note's family "$M=\#_r(S^2\times S^2)$ for $r\in\{1,2,3,4\}$" is not consistent: $\#_r(S^2\times S^2)$ has $\chi=2r+2$, which equals $8$ only at $r=3$. The correct picture is a single $\chi=8,\ b_2=6$ smooth type per chirality pattern, with signature $\tau$ ranging over the EH-orientation count (e.g. $\#_3(S^2\times S^2)$, $\tau=0$, all-mixed; through $\mathbb{CP}^2\#5\overline{\mathbb{CP}^2}$-type, $\tau=-4$, same orientation). The topology bookkeeping, and the derived Hitchin–Thorpe/spin statements in §8, should be redone from $\chi=8$.

This also bears on novelty. Several of these $\chi=8,\ b_2=6$ surfaces are del Pezzo type ($\mathbb{CP}^2\#5\overline{\mathbb{CP}^2}$ is a degree-4 del Pezzo) and already carry Kähler–Einstein metrics by known complex-geometry results; a positive Einstein metric there would not be new. The genuinely open target is the $\tau=0$ type $\#_3(S^2\times S^2)$, which is precisely the non-Kähler orientation pattern that Ozuch's higher obstructions most strongly resist. So the "removes the only known potential counterexample family" language in §8 overstates what a single construction would deliver, and the honest relation to Yau 26 (a forcing statement over *all* near-pinched metrics) is, as the note itself grants in §8, indirect.

---

## What would resolve the open items

1. State $\dim\mathbf O(g_o)$ unambiguously: for the product orbifold it is $0$ (rigidity, shown in §3). If the intended base is a partial (hyperkähler/Kähler) desingularization $\mathbf g_\pm$, recompute $\mathbf O(\mathbf g_\pm)$ and its $V_{l,2}$ jets there, and rewrite §1.3.
2. Recompute the coefficients with the correct bilinear $H^4$: the reduced system is $\sum_j(\tilde A_l^{\,j}+\tilde B_l^{\,j}\cos2\alpha_j+\tilde C_l^{\,j}\sin2\alpha_j)=0$, and the solvability analysis must account for the constant offset $\sum_j\tilde A_l^{\,j}$.
3. Separate necessity from construction: identify the exact theorem (and its hypotheses for $\Lambda>0$, mixed orientation) that would turn a transverse zero of $\mathcal F$ into an actual Einstein metric, rather than citing the a-priori estimate Prop. 2.19.
4. Fix the topology to $\chi=8,\ b_2=6$ and redo the signature/Hitchin–Thorpe/novelty discussion, distinguishing the known-KE del Pezzo types from the open $\tau=0$ type.

The pieces that stand as verified: the node curvature $\mathbf R^\pm=\mathrm{diag}(\Lambda,0,0)$, the automatic vanishing of $\lambda_k^j$ and $\mu_1^j$, and the $\ell=2$ harmonic character of $H^4$.