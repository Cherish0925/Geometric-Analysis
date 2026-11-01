# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step10_accessible_cover_reassessment.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step10.md",
    "Sessions/S0910A01/workspace/notes/step9_general_cover_transport.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/sources/lott_1708_06780_collapsing_almost_ricci_flat_4_manifolds.txt",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Read the corrected Step 10 reassessment and route plan for the Yau 26 Ricci-pinching project. Check the mathematical scope and consistency of the fixed-scale accessible-cover theorem, the use of the normal-cover mean lemma, Naber--Zhang Proposition 6.4, Lott's orbit-volume formula, Cheeger--Naber positive-branch statements, and the four-dimensional energy bookkeeping. Identify any remaining overstatement, missing hypothesis, coefficient/sign issue, or stronger next mathematical target. Treat the goal as rigorous progress toward proving or refuting the full proposition, not final exposition.

## Output

# Verifier Memo: Step 10 Reassessment and Route Plan (Yau 26, Ricci pinching)

## 1. What I verified directly, what rests on external inputs

I re-derived the algebra and cross-checked every internal computation against the supplied Lott (1708.06780), Naber–Zhang, and Cheeger–Naber (1406.6534) texts. The internal mathematics of the four-dimensional local rigidity mechanism and the transport lemma is correct and, in the crucial place, robust. Several load-bearing inputs (LeBrun's mixed Seiberg–Witten estimate, the $D_i/A_i\to0$ bookkeeping, the volume calibration $\mathrm{Vol}\sim\frac{32}{9}\pi^2 A$) are external to the three supplied papers and cannot be checked here; I flag them as the true foundation on which the $\lambda<0$ route stands.

## 2. Normal-cover transport lemma (Step 9) — correct

The four-step proof is valid. Geodesic lifting gives at least one lift in $B_r(\hat p)$; the multiplicity bound $m_r(x)\le N(2r)$ follows from the free deck action; the disjoint-translate estimate $N(2r)\,\mathrm{Vol}(B_r(p))\le \mathrm{Vol}(B_{3r}(\hat p))$ uses the buffer; and Bishop–Gromov on the cover (which inherits $\mathrm{Ric}\ge -(n-1)K$) closes it. The sheet count genuinely cancels. The numerical constants are right: I computed $\int_0^{r}\sinh^3=\frac{\cosh^3 r}{3}-\cosh r$ and obtained $V_{-1}^{(4)}(3)/V_{-1}^{(4)}(1)\approx 948$ (note: $949.5$) and $\approx 148$ at $r=1/2$ (note: $156$). This lemma is a clean, reusable object; the earlier lattice-counting proofs are correctly subsumed as corollaries.

One point to write explicitly: the buffer $B_{3r}(\hat p)\subset\widehat U$ is automatic for the universal cover of $B_{4r}(p)$ only because $B_{3r}(p)\Subset B_{4r}(p)$; geodesics of length $\le 3r$ from $\hat p$ project into $B_{3r}(p)$, so completeness of the covering domain is used and is satisfied when $B_{4r}(p)\Subset M$.

## 3. The forbidden calibrated Einstein germ — correct and robustly so

Every number checks:

- Completion identity (Step 8): I expanded $\frac{1}{12}f^2+\frac{1}{216}(s+8\sqrt6\,u)^2$ with $f=\frac23 s-2\sqrt{2/3}\,u$. The $s^2$ coefficients sum to $\frac{1}{27}+\frac{1}{216}=\frac{1}{24}$, the $u^2$ coefficients to $\frac29+\frac{16}{9}=2$, and the $su$ cross terms cancel exactly because $\sqrt{2/3}=\sqrt6/3$ forces $-\frac{2\alpha}{9}+\frac{2\sqrt6}{27}=0$. The identity $\frac{s^2}{24}+2u^2=\frac1{12}f^2+\frac1{216}(s+8\sqrt6 u)^2$ is exact. This is what makes the coefficient $8\sqrt6$ forced rather than arbitrary.
- Calibrated spectrum: $(s+8\sqrt6|W^+|)^2=0$ at $s=-4$ gives $|W^+|=1/(2\sqrt6)$, $|W^+|^2=1/24$. The spectrum $(-1/6,1/12,1/12)$ is trace-free ($-\frac16+\frac16=0$) with $|W^+|^2=\frac{1}{36}+\frac{2}{144}=\frac{1}{24}$. From $s=-4$, $u=1/(2\sqrt6)$ one gets $f=-3$ and $\mathcal G=4\xi(3-\xi)$; $\mathcal G=0$ with $0\le\xi\le1/6$ forces $\xi=0$, hence the simple eigenvalue $-1/6$. All consistent.
- The Derdziński route is the strong one and is convention-independent. Two distinct constant eigenvalues plus $\delta W^+=0$ (from the Einstein germ) give conformal factor $(24|W^+|^2)^{1/3}=1$, so the germ is locally Kähler; a Kähler–Einstein four-metric has $|W^+|^2=s^2/24=2/3$, contradicting $1/24$. This does not depend on any sign in a Weitzenböck formula.
- The Einstein–Weyl route: solving the stated identity with $\Delta|W^+|^2=0$ gives $2|\nabla W^+|^2=-s|W^+|^2+36\det W^+$. With $-s|W^+|^2=\frac16$, $36\det W^+=36\cdot(-\frac{1}{864})=-\frac1{24}$, this is $\frac16-\frac1{24}=\frac18$, so $|\nabla W^+|^2=1/16$, contradicting $\nabla W^+=0$. Even under the opposite sign convention one gets $|\nabla W^+|^2<0$, an immediate impossibility. The contradiction survives either convention; only the reported value $1/16$ is convention-dependent and should be pinned to a fixed sign for the Laplacian and $\det$.

This is the most solid part of the work and is genuine progress.

## 4. Lott orbit-volume material — matches source; interval models correctly restored

Equation (2.9) as quoted, $\Delta_B\sqrt{\det G}=(\tfrac14|F|^2-\lambda N)\sqrt{\det G}$, matches the source. Proposition 2.10's three hypotheses (parabolic base, $\lambda\le0$, $\sqrt{\det G}$ bounded above) are correctly reported, and the observation that $\lambda=-1$ makes the right side positive—yielding a contradiction only with a periodic/endpoint/Liouville input—is correct.

I verified the real-hyperbolic torus cusp: $dt^2+e^{2ct}g_{T^3}$ has sectional curvatures $-c^2$ and $\mathrm{Ric}=-3c^2 g$; $\mathrm{Ric}=-g$ forces $c=1/\sqrt3$, i.e. $e^{2t/\sqrt3}g_{T^3}$, as stated. For this model $v=\sqrt{\det G}=e^{\sqrt3\,t}$ and $v''=3v$, matching the abelian formula with $N=3$, $F=0$, $\lambda=-1$. So the abelian interval model is fully consistent with Lott, and the conclusion—circle base excluded by periodic integration, interval not excluded—is correct.

The non-abelian coefficient $v''=(3-\mu)v$ (versus $(3+\mu)v$), with $\mu=a_3^2/(2a_1^2a_2^2)$, cannot be checked from the supplied Lott extract, which only records the $N=1$, $\lambda=0$ case (Prop 2.21). This is a group-internal computation, and the sign matters: $3-\mu$ can turn $v$ concave when $\mu>3$, which changes the maximum-principle reasoning. It deserves its own derivation. The note's treatment of these as model calibrations rather than a classification is appropriate; Lott's Theorem 1.1(3) itself confirms that interval-base Kasner/Bianchi-II geometries exist, so a classification via orbit volume alone is not available.

## 5. Naber–Zhang Prop 6.4 and the accessible-cover theorem

The usage is faithful: Prop 6.4 supplies a lower harmonic radius on the local universal cover from bounded Ricci plus maximal nilpotency rank $n-k$, with constants depending on $n$ and the model noncollapsing radius $r_c(z^\ell)$ (Remark 2.7 / (1.12)). The note correctly declines to use Prop 6.5's curvature bound, which needs Einstein or a $|\nabla\mathrm{Ric}|$ bound not available for the approximating metrics, and instead uses only harmonic radius plus finite $W^{2,p}$ compactness. In dimension four the residual condition $\ell\le3$ is essentially automatic for genuine collapse; the case $\ell=4$ is exactly the Eguchi–Hanson-type residual four-dimensional core, which is one of the listed escape modes—so the enumeration is internally coherent (Remark 1.3 and Example 3.3 support this).

The proof sketch of $\mathrm{Vol}\,S_i(r_*)/\mathrm{Vol}\,M_i\to0$ is structurally sound: conditional averaging inside $S_i(r_*)$ (proportion $\ge\eta$) selects $p_i$ with $\fint_{B_R(p_i)}F_i\le\frac{C}{\eta}\fint_M F_i\to0$; transport carries the small mean upstairs; Prop 6.4 gives a fixed-radius harmonic chart; bounded Ricci gives $C^{1,\alpha}\cap W^{2,q}$ with $q>2$; the equation $\mathrm{Ric}_{g_i}=-g_i+o(1)$ passes to a smooth Einstein germ; and $F_i\to0$ in $L^1$ on the chart (since $q>2$ passes $|W^+|^2$, $s$ in $L^1$) forces the forbidden calibrated germ.

Two things to make explicit rather than assert:

- **Scale bookkeeping.** The averaging radius $R$, the transport radius $r$ with buffer $3r$, the NZ closeness scale $\delta_0(n,r_*)$, and the harmonic radius $h_0(n,r_*)$ are all fixed positive numbers depending only on $n,r_*$, but the argument only closes once they are chosen in a definite order (e.g. $R$ and $r$ small relative to $\delta_0$, and $h_0$ exceeding the chart size inside $B_{r/2}(\hat p)$). This chain should be written out.
- **Compatibility of hypothesis (4).** NZ works on the universal cover of $B_1(q)$; the transport lemma works on a buffered normal cover of $B_{4r}(p)$. Taking $q=p$ and using the universal cover of $B_1(p)$ makes these the same cover, and $B_{3r}(p)\Subset B_1(p)$ makes the buffer hold. So hypothesis (4) is satisfiable and is closer to settled than the prose suggests; I recommend recording this identification explicitly, together with the check that $h_0\ge$ the chart scale used, so that (4) is not carried as an open assumption.

The reach of this theorem is exactly as strong as accessibility is common. The theorem removes the accessible part; the entire remaining question is whether inaccessible collapse (rank drop, degenerating model scale $r_c\to0$, residual four-dimensional cores, singular fibers, or only shrinking-radius unwrapping) can occupy positive volume proportion. The rescaling observation is the sharpest obstacle and is correctly identified: at radius $r_i\to0$, rescaling by $r_i^{-2}$ sends the Einstein constant to $0$, so the germ becomes Ricci-flat and the calibration $|W^+|^2=1/24$ (which came from $s=-4$) is lost, together with its Seiberg–Witten support. The mechanism therefore genuinely requires fixed physical scale, and this is the crux, not a side detail.

## 6. Cheeger–Naber positive branch — correctly read and correctly bounded in reach

Theorem 1.12 is quoted exactly (dimension four; $|\mathrm{Ric}|\le3$, $\mathrm{Vol}(B_1)>v$, $\mathrm{diam}\le D$ imply finitely many diffeomorphism types). Positive pinching $|\mathrm{Ric}-g|\le\delta<1$ gives $\mathrm{Ric}\ge(1-\delta)g>0$, hence a Myers diameter bound; a lower total-volume bound plus Bishop–Gromov gives unit-ball noncollapse (this is exactly the mechanism used inside CN's own (8.66)). The statement that finitely many diffeomorphism types do not by themselves produce an Einstein metric is correct, and the distinction between the all-dimensional Theorem 1.4 (codimension-four regularity for noncollapsed bounded-Ricci limits) and the four-dimensional Theorem 1.12 (finiteness) is read correctly: the source does not supply an all-dimensional finiteness statement, so narrowing S0910A02's use to dimension four is right. The genuinely open positive-branch object—the passage from near-Einstein (possibly orbifold) limits to an actual Einstein metric on the original smooth manifold via an approximate-to-exact obstruction projection or desingularization—is correctly identified as unresolved.

## 7. Four-dimensional energy bookkeeping — signature correction verified

$12\pi^2\tau(M)=\int(|W^+|^2-|W^-|^2)$ is standard; $\tau(M)=\tau(X)-k$ follows from $\tau(\overline{\mathbb{CP}}^2)=-1$ and additivity, so $\int|W^-|^2=\int|W^+|^2-12\pi^2(\tau(X)-k)$. The corrected $k$-coefficient is $+12\pi^2$, not $+32\pi^2$, and the $\tau(X)$ term is not droppable—both corrections are right. The calibrated energies are internally consistent: with $s^2/24=2/3$ and $|W^+|^2=1/24$ pointwise and $\mathrm{Vol}\sim\frac{32}{9}\pi^2 A$, one gets $\int s^2/24=\frac{64}{27}\pi^2 A$ and $\int|W^+|^2=\frac{4}{27}\pi^2 A$, matching the script's values. The statement that a normalized $O(A)$ full-curvature energy budget needs $\chi(X)/A$, $k/A$, $J/A$ bounded (from algebraic-surface geography, not from pinching alone) is the correct qualification. The Weyl-divergence remark—that an $L^\infty$ Ricci defect yields integrated identities after moving derivatives onto test tensors, not a pointwise curvature estimate—is also correct, and prevents a common overreach.

## 8. The paramount connective question

Above every technical point: the entire $\lambda<0$ route operates on near-critical sequences with $\delta_i=\|g_i^{-1}(\mathrm{Ric}_{g_i}+g_i)\|\to0$, i.e. asymptotically Einstein metrics. Yau 26's hypothesis is a **fixed two-sided pinching** $c_n g\le\mathrm{Ric}\le C_n g$ with $c_n,C_n$ independent of the metric and *not* tending to Einstein. A metric that is pinched with fixed constants need not be anywhere near Einstein. The supplied notes do not establish the reduction from "a pinched metric exists on $M$" to "a near-critical ($\delta_i\to0$) LeBrun sequence on $M$ is the relevant object," nor to the LeBrun/Seiberg–Witten Einstein-obstruction picture on $X\#k\overline{\mathbb{CP}}^2$. This connective step determines whether the (correct, hard-won) local rigidity and accessible-cover analysis actually bears on Yau 26 or on a related-but-distinct Einstein-obstruction question. Making this bridge explicit—or recording precisely what part of Yau 26 the near-Einstein framework addresses—is the single most valuable thing to settle, because it fixes the meaning of all the downstream analysis. The route notes' repeated statements that none of this yet resolves the four-dimensional $\lambda<0$ case or the full proposition are accurate; the missing item is the forward link, not a correction to existing arguments.

## 9. Stronger next mathematical targets

- **Turn the conditional accessible-cover theorem into an unconditional one** by showing near-critical LeBrun energy/topology forces the NZ package (residual dimension $\le3$, maximal rank, uniform model scale $r_c\ge r_*$) on a positive volume proportion. Concrete subquestion: does the normalized $O(A)$ full-curvature mean, transported to a normal cover, yield a weak harmonic-radius lower bound on a positive-volume set under bounded Ricci alone?
- **Characterize inaccessible collapse quantitatively.** Either show each inaccessible mode (rank drop, $r_c\to0$, residual four-dimensional cores, singular fibers, shrinking-radius unwrapping) forces curvature or Euler-density concentration detectable by the normalized energy, contradicting the budget; or construct an explicit inaccessible model, which would itself be decisive information about whether this route can close.
- **Localize the Chern–Gauss–Bonnet representative of $\chi$.** Near saturation $2\chi+3\tau=A-k\approx 2A/3$; a global free circle action forces $\chi=0$, so the Euler density must concentrate on exceptional strata. Connecting that concentration to the absence of controlled unwrapping is a sharp, computable target.
- **Positive branch:** construct or refute the near-Einstein-to-Einstein bridge (approximate-to-exact obstruction projection / desingularization) for noncollapsed orbifold limits, and treat total collapse with large Weyl energy in the Sha–Yang family $\#_k(S^2\times S^2)$ as a substantive construction/obstruction problem rather than a technical input.
- **Small verifications to close:** the nil³ coefficient $v''=(3-\mu)v$ (independent derivation, since the sign controls concavity); a fixed sign convention for the Einstein–Weyl identity so the value $|\nabla W^+|^2=1/16$ is unambiguous; and, from external sources, the LeBrun mixed estimate integrand $\frac{s^2}{24}+2|W^+|^2$ with coefficient $8\sqrt6$ and the calibration $\mathrm{Vol}\sim\frac{32}{9}\pi^2 A$, all of which the internal algebra is consistent with but which are not checkable from the three supplied papers.

The withdrawal of the earlier "all regular collapse excluded" statement, the corrected nil³ sign, the corrected signature coefficient, and the restoration of interval/cusp models are all correct and improve the reliability of the accumulated picture.