# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md",
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step13.md"
  ]
}
```

## Task

Verify the normalization-invariant rank-one reduction and the claimed accessibility bootstrap. Check: (1) The structural formulas: vertical Ric[33] = (-|C|² + 2tr(h) + 2|u|²)/2 with the correct sign, matching A03's tr(H) = 1 + ℓ²|F|²/4 (with the appropriate norm convention). (2) The static limit Spec(W+) = {1/3 - η_i} from the reduction output. (3) The bootstrap argument: is the claim that H ≥ 0 implies Ric_B ≥ -I correct? Is 3D Bishop-Gromov applicable? Does 4D cover noncollapse follow? (4) The gap: does the weighted RCD(-1,4) structure really fail to give ordinary base Ricci? Can any other route (4D arguments on the cover, Moser iteration, Bochner identities) close the gap? Assess what is rigorous and what remains conjectural.

## Output

## Verification memo: rank-one reduction and the accessibility bootstrap

I worked through the reduction independently in a moving coframe, checked the reduced Einstein equations against the standard Kaluza–Klein formulas and against the two worked examples (H²×H², Taub–NUT–AdS), and re-derived the static Weyl spectrum. The structural dictionary is largely sound, with one sign-convention matter and one genuine power discrepancy in the mixed equation. The accessibility bootstrap contains a step whose logical direction is inverted, and the "static case closed" statement is not supported by the estimates present. Details below, organized by the four requested points.

### 1. Vertical equation and its sign

Set the coframe $e^3 = v\,\theta$, $\theta = dz+B$, so $de^3 = u_a e^a\wedge e^3 + \tfrac12 C_{ab}e^a\wedge e^b$ with $u_a=\partial_a\log v$, $C_{ab}=vF_{ab}$. Solving Cartan's equations gives
$$
\omega^a_3=-u_a e^3-\tfrac12 C_{ab}e^b,\qquad \omega^a_b=\tilde\omega^a_b-\tfrac12 C_{ab}e^3,
$$
and the standard reduction then yields, with $\Delta$ the trace-of-Hessian Laplacian,
$$
\operatorname{Ric}(e_3,e_3)= -\frac{\Delta v}{v}+\frac{v^2}{4}\,F_{ab}F^{ab}
=\frac{|C|^2}{2}-\bigl(\operatorname{tr}h+|u|^2\bigr).
$$
I confirmed the $+\tfrac14|F|^2$ coefficient two ways: the $v\equiv1$ Hopf value $\operatorname{Ric}(V,V)=\tfrac14|F|^2>0$ (round $S^3$), and the warped case $F=0$ giving $\operatorname{Ric}(V,V)=-\Delta v/v$ (checked on the surface $dx^2+v^2dz^2$, $K=-v''/v$). Setting $\operatorname{Ric}(e_3,e_3)=-1$ produces exactly the note's scalar equation
$$
\operatorname{tr}h+|u|^2 = 1+\tfrac12|C|^2,\qquad \frac{\Delta v}{v}=1+\tfrac12|C|^2,
$$
which is correct.

However, the expression quoted in the task, $\operatorname{Ric}[33]=(-|C|^2+2\operatorname{tr}h+2|u|^2)/2 = \operatorname{tr}h+|u|^2-\tfrac12|C|^2$, is the **negative** of the true $\operatorname{Ric}(e_3,e_3)$; it equals $-\operatorname{Ric}(e_3,e_3)=+1$, not $-1$. The correctly signed vertical component is $\operatorname{Ric}(e_3,e_3)=\tfrac12|C|^2-\operatorname{tr}h-|u|^2$. The derived scalar identity is unaffected (it fixes only the magnitude), but the displayed component sign is inverted. This is exactly the kind of inversion produced by a negated curvature operator, and it should be reconciled with Section 9's admitted operator index-order issue (`R[a,b,d,c]` vs `R[a,b,c,d]`); a single global convention should be pinned to a known model (H⁴ or $S^4$) and Ric, W⁺ re-read from it.

### 2. Norm convention and A03 match

The bookkeeping $|C|^2=\sum_{a<b}C_{ab}^2=\tfrac12 C_{ab}C^{ab}=\tfrac{v^2}{2}F_{ab}F^{ab}$, hence $\tfrac12|C|^2=\tfrac{v^2}{4}F_{ab}F^{ab}$, matches A03's $\ell^2|F|^2/4$ term under $F_{ab}F^{ab}=2\sum_{a<b}F_{ab}^2$. Translating A03's $z=*_q Z$, $Z=\ell F$, the term $|z|^2/2 = \tfrac14 Z_{ab}Z^{ab}=\tfrac{\ell^2}{4}F_{ab}F^{ab}$ agrees. The two notes are consistent here.

### 3. Mixed equation: the weight is $v^3$, not $v^2$

This is a genuine discrepancy worth correcting. The reduced action carries the horizontal Maxwell term as $\tfrac{v^3}{4}|F|^2\,\sqrt{g_B}$ (the $\sqrt{g_4}=v\sqrt{g_B}$ factor times the $v^2/4$ vertical coefficient). Varying $B$ gives
$$
\operatorname{div}_B(v^3 F_B)=0 \iff \sum_b\bigl(\nabla_b C_{ab}+2u_b C_{ab}\bigr)=0.
$$
The dual of this in 3D is precisely A03's $dz=-2u\wedge z$ (I verified the Hodge translation $\delta C=-2\iota_uC \leftrightarrow dz=-2u\wedge z$), so A03's form and its Taub–NUT–AdS check correspond to the $v^3$ weight. The S0910A01 note instead states "$v^2 F_B$ is weighted harmonic" and builds bootstrap Step 1 on a "$v^2$-Hodge Laplacian." The correctly co-closed object is $v^3 F_B$; the elliptic estimate in Step 1 should use the $v^3$ weight. The component form written after the "$\operatorname{div}_B(v^2F_B)$" line, $\sum_b\nabla_b(vC_{ab})+2u_bC_{ab}$, is also dimensionally uneven (the last term lacks the $v$), consistent with a transcription slip toward the wrong power. The correct component identity is $\sum_b(\nabla_bC_{ab}+2u_bC_{ab})=0$.

The horizontal equation $\operatorname{Ric}^B=-I+H+\tfrac12 C^2$ (with $H=\operatorname{Hess}(v)/v$, $(C^2)_{ab}=\sum_c C_{ac}C_{bc}$) I checked and it is correct, including the sign of the $-\tfrac{v^2}{2}F\!\circ\!F$ horizontal term.

### 4. Static Weyl spectrum: correct, with a strong internal check

In the static limit ($C=0,u=0$, $\operatorname{tr}h=1$, $\operatorname{Ric}^B=h-I$), the formula $\operatorname{Spec}(W^+)=\{1/3-\eta_i\}$ passes three tests:
- **Trace-free:** $\sum(1/3-\eta_i)=1-\operatorname{tr}h=0$. ✓
- **H²×H²:** $\eta=(1,0,0)\Rightarrow(-2/3,1/3,1/3)$, matching both notes and the known product spectrum. ✓
- **Calibrated profile** $H=(1/2,1/4,1/4)$: eigenvalues $(-1/6,1/12,1/12)$, giving $|W^+|^2=1/36+2/144=1/24$. ✓ This reproduces the calibrated deficit value $|W^+|^2\to1/24$ exactly, a nontrivial consistency check tying the reduction to the calibration.

The constant $1/3$ is $\kappa/3$ with $\kappa=1$, consistent with A03's $E=(\kappa/3)q-H+(\text{twist})$. The static formula and its use are sound. The subsequent "$\ne 2/3$" contradiction is the Derdziński mechanism: a repeated $W^+$ eigenvalue on an open Einstein set forces a locally Kähler germ, whose $W^+$ for $s=-4$ must be $(-2/3,1/3,1/3)$ ($|W^+|^2=2/3$), incompatible with the calibrated $(-1/6,1/12,1/12)$. This is internally coherent but rests on Step 6 (Derdziński), which I did not have in front of me; the reduction verification does not by itself establish that a near-critical sequence approaches the specific profile $H=(1/2,1/4,1/4)$.

### 5. The bootstrap: one correct algebraic step, one inverted comparison, one missing bound

**H ≥ 0 ⟹ Ric_B ≥ −I is algebraically correct.** From $\operatorname{Ric}^B=-I+H+\tfrac12 C^2$, the twist term $\tfrac12\sum_c C_{ac}C_{bc}=\tfrac12(CC^\top)$ is positive semidefinite (C antisymmetric), so $H\succeq0$ gives $\operatorname{Ric}^B\succeq -I$. ✓

**But three things break the "static case closed" conclusion:**

(i) *$H\succeq0$ is not a consequence of the static condition.* Static fixes only $\operatorname{tr}H=\operatorname{tr}h=1$ (via $\Delta\log v=1$, a subharmonicity of $\log v$), which controls the trace, not the individual eigenvalues. The listed profiles happen to be nonnegative, but the route assessment's parenthetical "(true in the static case $C=0$)" is stronger than what is shown; the note's own Section 6 correctly states this "requires analysis of the constrained system." These two statements are in tension and the general $H\succeq0$ assertion is unsupported.

(ii) *3D Bishop–Gromov runs the wrong way for what is needed.* Relative volume comparison from $\operatorname{Ric}^B\ge -I$ gives volume **upper** bounds ($\operatorname{vol}(B_r)\le$ model), i.e., non-increasing volume ratios. It does **not** produce a volume lower bound, and a Ricci lower bound alone never prevents collapse (Berger spheres, thin flat tori collapse with $\operatorname{Ric}$ bounded below). The note's Section 6 sentence "$\operatorname{Ric}^B\ge -I$, giving a 3D Bishop–Gromov volume **lower** bound … 4D noncollapse" inverts the comparison. Noncollapse of the base requires an independent volume lower bound input; it is not delivered by $\operatorname{Ric}^B\ge -I$.

(iii) *Harmonic radius needs an upper Ricci bound too.* Even granting base noncollapse, a 3D harmonic radius bound (bootstrap Step 3) needs $|\operatorname{Ric}^B|$ bounded on both sides. Section 12(c) itself states $\operatorname{Ric}^B=-I+H+\tfrac12 C^2$ is not bounded above (H and $C^2$ can be large). So the harmonic-radius step is not available even in the static sub-case unless $\operatorname{Hess}(\log v)$ is separately bounded above.

Consequently Layer 2 ("static rank-one closed") is not rigorously established as written; it is closer to a target than a theorem. The conditional final step — base noncollapse plus fiber extent $\Theta(r)$ on the cover with $v$ bounded ⟹ 4D noncollapse — is fine as an implication; only its antecedent is unproven.

The static case does have appealing special structure worth stating exactly: $C=0,u=0$ forces $\Delta v=v$ and $\operatorname{Ric}^B=-I+\operatorname{Hess}(v)/v$ — a positive Laplace eigenfunction driving the base metric. Whether this rigidity forces the two-sided bounds is an open question, not a consequence of the material present.

### 6. Weighted RCD(−1,4) and ordinary base Ricci

The identity $\operatorname{Ric}^4_{q,\ell}=\operatorname{Ric}_B-\operatorname{Hess}(\ell)/\ell=\operatorname{Ric}_B-H$ is the $N=4$ Bakry–Émery Ricci for the fiber-weighted measure $\ell\,dvol_q$; I verified it via $f=-\log\ell$, $\operatorname{Ric}_f^4=\operatorname{Ric}_B+\operatorname{Hess}f-df\otimes df=\operatorname{Ric}_B-H$. The 4D lower bound descends to $\operatorname{Ric}_B-H\succeq -I$. Since $\operatorname{Ric}_B=(\operatorname{Ric}_B-H)+H\succeq -I+H_{\min}$, the weighted bound controls ordinary $\operatorname{Ric}_B$ from below only up to $H$'s most negative eigenvalue, and not at all from above. So the note is right: RCD(−1,4) genuinely does **not** deliver ordinary base Ricci control. A03's hyperbolic-cusp remark is a legitimate obstruction — excellent weighted quotient geometry coexists with arbitrarily short surviving fibers — so synthetic regularity plus doubling/Poincaré cannot by itself force a smooth chart or keep $\ell$ away from zero.

### 7. Can another route close the gap? Assessment of the three proposals

**Route (c) (maximum principle for v) does not close for uniform constants.** Subharmonicity $\Delta v=v(1+\tfrac12|C|^2)>0$ gives that $v$ attains its maximum on the outer sphere, hence $v(p)=1\le \sup_{\partial}v$ — an interior-vs-boundary comparison, not an a priori two-sided bound on a fixed inner ball. The Harnack step needs $q=1+\tfrac12 v^2|F_B|^2\in L^\infty$, which is the very quantity being sought. The note's rescue ("$v>0$ continuous $\Rightarrow v\ge c_3$ on compacts") produces a constant depending on the individual metric; for a collapsing sequence one needs constants independent of the index, and pointwise positivity of each $v_i$ gives no uniform lower bound. This is the central circularity and route (c) as stated does not break it.

**Route (b) (Moser iteration on $\Delta_4\ell=(1+\tfrac14\ell^2|F|^2)\ell$)** needs Sobolev/doubling constants (degenerate under collapse; one must first pass to the cover) and control of the potential $\tfrac14\ell^2|F|^2=\tfrac12|C|^2$. That potential is exactly the twist A03 shows is not controlled by the calibrated deficit (derivative twisting keeps $\nabla z$ order-one while $|C|$ small). So Moser meets the same twist-control obstruction.

**Route (a) (direct $L^2$ from 4D energy) identifies the correct controlled quantities but stops at the open analytic core.** The component $\operatorname{Rm}(e_a,e_3,e_b,e_3)=-H^{A03}_{ab}$ and $\operatorname{Rm}(e_a,e_b,e_c,e_3)=-\tfrac12[(\nabla z)+\dots]$ mean that a bounded $\int|\operatorname{Rm}|^2$ on a cover ball yields $L^2$ bounds on both $H$ and on the derivative-twist block $\nabla z$ (equivalently on both chiral Weyl energies $|W^\pm|^2$). This is genuinely available and is the right target. But this is exactly A03's identified interface: $L^2$ is scale-invariant in 4D, and bounded $|W^+|^2,|W^-|^2$ energies plus a calibrated $W^+$ do **not** control pointwise geometry or a reconstruction radius — derivative twisting can concentrate at critical scaling. So route (a) delivers the correct hypotheses of the missing theorem but not the theorem.

**Weighted Bochner for $a_\pm$** (A03 §7) is a reasonable program; the obstruction is real: the trace mode carries $|z|^2$ and $\langle u,z\rangle$, which is not sign-definite, so a coercive inequality bounding $|\nabla a_\pm|^2+|a_+\wedge a_-|^2$ by the two Weyl energies is not yet in hand.

I did not find, in the supplied material or the standard reduction, any route that presently closes the passage from bounded $L^2$ curvature energy to a fixed-scale reconstruction on the cover under nonzero twist. A03's formulation of the needed statement — compactness/reconstruction for the coupled chiral Riccati–Maurer–Cartan system on an RCD(−1,4) quotient with both Weyl means bounded — is the accurate description of the open mathematical object, and it is not an established result.

### 8. The chiral factorization is sound and is the sharper structure

$W^\pm=-[\operatorname{sym}\nabla a_\pm+a_\pm\otimes a_\pm]_0$ with $a_\pm=u\mp z/2$, $da_+=a_+\wedge a_-$, $da_-=-a_+\wedge a_-$, is verified by A03's script and checked on H²×H² ($\operatorname{Spec}W^+=(-2/3,1/3,1/3)$) and Taub–NUT–AdS ($E+B=0$, $\operatorname{Spec}(E-B)=(-4c,2c,2c)$). The essential structural point is correct and important: the derivative twist $\nabla z$ enters the magnetic block $B$ at order one and is not suppressed as $\ell\to0$, so the "high scaled-twist amplitude" division of Step 11 is too coarse. A03's refutation of "constant static spectrum $\Rightarrow W^+=0$" via H²×H², and its Taub–NUT–AdS demonstration that derivative twisting cancels an order-one electric anisotropy, are solid and remove two simplifications that would have pointed subsequent work at a false rigidity.

### 9. What is rigorous, what is conjectural

Rigorous / verified: the vertical, horizontal, and closure identities (vertical up to the displayed overall sign); the norm reconciliation with A03; the static $\operatorname{Spec}(W^+)=\{1/3-\eta_i\}$ with its trace-free, H²×H², and $|W^+|^2=1/24$ checks; the algebraic implication $H\succeq0\Rightarrow\operatorname{Ric}_B\succeq -I$; the weighted identity $\operatorname{Ric}^4_{q,\ell}=\operatorname{Ric}_B-H$ and the statement that it does not control ordinary $\operatorname{Ric}_B$; the chiral factorization.

To be corrected: the mixed-equation weight ($v^3$, not $v^2$ — A03's dual form is the correct one) and the associated "weighted harmonic" object in bootstrap Step 1; the displayed sign of $\operatorname{Ric}(e_3,e_3)$, to be made consistent with a single verified curvature convention (linked to the Section 9 operator index issue).

Conjectural / not established: $H\succeq0$ on the calibrated bulk in general; base noncollapse from $\operatorname{Ric}_B\succeq -I$ (the Bishop–Gromov direction is inverted, and no volume lower bound is supplied); the 3D harmonic radius (needs a two-sided base Ricci bound that is absent); therefore Layer 2 ("static rank-one closed") and Layer 3 (twisted) both remain open. The decisive missing object is a coercive weighted compactness/reconstruction theorem for the chiral $(u,z)$ system with bounded $|W^\pm|^2$ means and calibrated $W^+$ — an $L^2$-to-reconstruction passage at critical scaling — for which no source or self-contained argument is currently present.