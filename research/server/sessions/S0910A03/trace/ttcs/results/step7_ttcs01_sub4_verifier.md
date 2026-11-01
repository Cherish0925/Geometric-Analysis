# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step6_collapsed_unwrapping_route.md"
  ]
}
```

## Task

Verify the orbit-volume obstruction argument for negative Einstein regular collapse:

1. Check that Lott's equation (2.9) Δv = (|F|²/4 - λN)v correctly specializes to Δv = (|F|²/4 + N)v for λ = -1, and that this makes v strictly subharmonic.

2. Verify the parabolicity argument: complement of finitely many points in a compact space of dim ≥ 2 is parabolic (Grigoryan), bounded-above subharmonic → constant → contradiction with positive RHS.

3. Check the circle base case: ∫v'' = 0 vs ∫Nv > 0.

4. Verify the near-Einstein error term: for Ric = -g + E with ||E||∞ ≤ δ, the coefficient becomes N(1-δ) > 0 for δ < 1.

5. Check the capacity estimate: from Δv ≥ cv with test function η²/v, one gets c∫η² ≤ ∫|∇η|².

6. Verify that the conclusion is correctly scoped: excludes free abelian collapse only (not nil³), and only on parabolic bases with bounded orbit volume. Identify any gaps or additional hypotheses needed.

7. Check whether the Cheeger-Tian framework legitimately applies to near-Einstein (not exactly Einstein) 4-manifolds to produce a groupoid limit with Ric = -g.

## Output

# Verification Memo: Orbit-Volume Obstruction for Negative Einstein Regular Collapse

Prepared on `step7_orbit_volume_negative_einstein_collapse.tex` (with supporting reading of the Step 6 notes). I worked each of the seven requested points to independent confirmation or refutation. Headline: five points hold (some with corrections to the stated justification), one point (the capacity estimate, Task 5) is mathematically incorrect, and Task 7 rests on a transfer of Cheeger–Tian machinery from exact to near-Einstein inputs that is not established by the hypotheses cited.

---

## 1. Lott's equation and the λ = −1 specialization — correct, independently confirmed

Arithmetic: $\Delta v=(|F|^2/4-\lambda N)v$ at $\lambda=-1$ gives $(|F|^2/4+N)v$, and with $|F|^2\ge0$, $N\ge1$ the coefficient is $\ge N\ge1>0$, so $v$ is strictly subharmonic where $v>0$ under the trace-of-Hessian convention $\Delta=\operatorname{tr}\nabla^2$. All correct.

I checked Lott's equation itself against the O'Neill warped-product Ricci formula rather than taking it on citation. Take the simplest instance $N=1$, $F=0$, so $\bar g=v^2dt^2+g_B$ with circle fiber, $v=\sqrt{G_{11}}$. O'Neill's formula for a 1-dimensional flat fiber gives $\operatorname{Ric}(\partial_t,\partial_t)=-v\,(\Delta_{\text{geom}}v)\,g_F$, and imposing $\operatorname{Ric}=\lambda\bar g$ yields $\Delta_{\text{geom}}v=-\lambda v$. Lott's equation at $N=1$, $F=0$ reads $\Delta v=(0-\lambda\cdot1)v=-\lambda v$ — an exact match, and it also fixes the sign convention consistently. So the specialization and the subharmonicity conclusion are sound.

## 2. Parabolicity / bounded-above-subharmonic-constant — conclusion holds, but state the correct mechanism and one hidden hypothesis

The logical shape (bounded-above subharmonic on parabolic base ⇒ constant ⇒ contradiction with strictly positive right-hand side) is valid. Two points require correction/attention.

**(a) The correct engine is removable singularity across polar points, and the dim ≥ 2 threshold is exactly the right one.** A single point in a Riemannian manifold is polar (zero capacity, removable for bounded subharmonic functions) precisely for base dimension $\ge2$; in dimension 1 points separate and the punctured-space argument does not run — which is why the note correctly switches to the ODE argument for $B^1$. So a bounded-above subharmonic $v$ on $B=(\text{compact})\setminus\{x_1,\dots,x_C\}$ extends subharmonically across the punctures, and on a closed connected manifold $\int_B\Delta v=0$ with $\Delta v\ge0$ forces $\Delta v\equiv0$, hence $v$ constant. This is cleaner and more robust than invoking a volume-growth parabolicity theorem, and it is worth writing this way because the round-vs-flat distinction below shows conformal framing can mislead.

**(b) Removability needs the base metric near the punctures to be finite-distance with controlled (non-cusp, comparable-volume) geometry — this is a genuine hypothesis, not automatic.** Parabolicity is *not* conformally invariant in dimension $\ge3$: $S^n\setminus\{p\}$ with the round metric is parabolic (point at finite distance, polar), while the conformally-equivalent flat $\mathbb R^n$ is transient for $n\ge3$. The note's phrase "metric completion adds finitely many points" asserts finite distance, but if the limiting base metric $g_B$ near a curvature-blowup point degenerates into a cusp (infinite distance) or an orbifold cone with non-polar structure, removability can break. The note itself flags this in the "what remains" section (Lott Prop. 3.19: orbifold points create base boundary, potentially non-parabolic). So the Proposition's hypotheses should explicitly include: punctures at finite distance with polar (non-cusp, controlled-volume) local geometry.

**(c) The "$v$ bounded above because 4D volume is finite" inference is an $L^1$-to-$L^\infty$ slip.** Finite $\int_B v\,(\text{lattice})\,d\mu_B$ gives $v\in L^1$, not a pointwise upper bound. The correct reason $v$ is bounded above in the intended application is that this is genuine collapse: the orbit-volume function is small ($v\to0$), hence certainly bounded. Replace the volume-finiteness justification with the collapse (small-fiber) justification; the Proposition as stated (taking "$\det G$ bounded above" as hypothesis) is fine.

## 3. Circle base case — correct and clean

On $B^1=$ circle of length $L$, $\Delta v=v''$ in arc length, and $\int_0^Lv''\,ds=v'(L)-v'(0)=0$ by periodicity, while $\Delta v\ge Nv$ (coefficient $\ge N=3$ for the stated $N=3$ instance) gives $\int_0^Lv''\ge N\int_0^Lv>0$. Contradiction. Correct. This is the same divergence-theorem contradiction as the closed higher-dimensional case and is the most airtight piece of the note.

## 4. Near-Einstein error term — arithmetic correct; one structural assumption to make explicit

Tracing the vertical Ricci: exact $\operatorname{Ric}=\lambda\bar g$ contributes vertical trace $\lambda N$; replacing $\lambda\bar g$ by $-\bar g+E$ replaces this by $-N+\operatorname{tr}_{\text{vert}}E$, so $-\lambda N\to N-\operatorname{tr}_{\text{vert}}E$, giving $\Delta v=(|F|^2/4+N-\operatorname{tr}_{\text{vert}}E)v$. With $|\operatorname{tr}_{\text{vert}}E|\le N\delta$, $\Delta v\ge(|F|^2/4+N(1-\delta))v\ge N(1-\delta)v$, positive for $\delta<1$. Arithmetic confirmed, matching \eqref{eq:nearein}.

**Structural point:** Lott's equation presumes the metric is written in the *exact* adapted form with an exact local isometric $\mathbb R^N$-action. For the perturbed $g_i$ the collapse (CFG N-structure) provides only an *approximately* isometric action; the deviation of $g_i$ from invariance under that action contributes terms beyond the Ricci defect $E_i$, and these are hidden in the "$\cdots$" of the displayed vertical-trace identity. The near-Einstein inequality applied directly to $g_i$ therefore carries an unaccounted isometry-defect term. The logically clean path avoids this: pass first to the groupoid limit $\mathcal X$, where the local $\mathbb R^N$-action is *exactly* isometric and $\operatorname{Ric}_{\mathcal X}=-g_{\mathcal X}$ exactly, then apply the exact equation \eqref{eq:negein} and the Section 2 Proposition. That route needs no near-Einstein version at all. I would route the argument through the limit rather than through \eqref{eq:nearein}.

## 5. Capacity estimate — incorrect; a concrete counterexample

The claim $c\int_\Omega\eta^2\le\int_\Omega|\nabla\eta|^2$ derived from $\Delta v\ge cv$ ($v>0$, $c>0$) via testing with $\psi=\eta^2/v$ is false, and "AM–GM gives the result" does not close.

**Where the sketch breaks.** Testing gives correctly
$$
c\int\eta^2\le\int\psi\,\Delta v=-\int\langle\nabla\psi,\nabla v\rangle=\int\frac{\eta^2}{v^2}|\nabla v|^2-\int\frac{2\eta}{v}\langle\nabla\eta,\nabla v\rangle .
$$
Writing $P=\tfrac{\eta}{v}\nabla v$, $Q=\nabla\eta$, the right side is $\int(|P|^2-2\langle P,Q\rangle)=\int(|P-Q|^2-|Q|^2)$. To reach $\int|\nabla\eta|^2=\int|Q|^2$ one would need $\int|P-Q|^2\le 2\int|Q|^2$, which is not implied by any AM–GM step because $P$ (hence $|\nabla v|/v$) is uncontrolled. The uncontrolled term $\int\frac{\eta^2}{v^2}|\nabla v|^2$ cannot be absorbed.

**Exact ground-state identity confirms the wrong sign.** Setting $\eta=vw$,
$$
\int|\nabla\eta|^2=-\int\frac{\eta^2}{v}\Delta v+\int v^2|\nabla w|^2\le -c\int\eta^2+\int v^2|\nabla w|^2,
$$
i.e. $\int|\nabla\eta|^2+c\int\eta^2\le\int v^2|\nabla w|^2$ — the opposite combination, giving no upper bound on $c\int\eta^2$.

**Counterexample.** On $\Omega=(-a,a)\subset\mathbb R$ take $v=\cosh(\sqrt c\,x)>0$, so $v''=cv$ exactly. The claimed estimate would force $c\le\lambda_1(\Omega)=(\pi/2a)^2$, which fails for $a$ large; on all of $\mathbb R$, $\lambda_1=0<c$ yet the positive supersolution $v$ exists. So the inequality is simply false. (The underlying reason: a positive function with $\Delta_{\text{geom}}v\ge cv$ is a positive *subsolution*, not a supersolution, so no Barta-type spectral lower bound follows.)

**Consequences and what survives.** The Section 3 quantitative statements built on this — the boxed "$\operatorname{Vol}(\Omega)\le L^2/c_i$," the bounded-capacity exhaustion, and the quantitative deficit-transport bridge — are not supported as written. However, the *qualitative* exclusion (Section 2 Proposition, the circle case, the closed-base $\eta\equiv1$ contradiction) does **not** use the capacity estimate: it uses only the direct divergence-theorem / parabolic-removability argument, which is valid. So the core exclusion of free abelian negative-Einstein collapse stands; only the quantitative superstructure needs replacement. If a quantitative statement is wanted, the honest route is a Dirichlet-eigenvalue comparison in the *reverse* direction, or a direct integral estimate against the actual base geometry — not this capacity inequality.

## 6. Coverage of the conclusion — stated correctly, with two corrections and a list of the assumptions that must travel with it

The note is explicit that it excludes only *free abelian* $\mathbb R^N$ collapse, on parabolic bases with $\det G$ bounded above, and lists nil³, singular fibers, the interval-endpoint case, and the positive branch as open. That coverage statement is accurate. Two corrections and the assumption inventory:

- **The $N=4$ (base = point) argument is justified incorrectly, though the conclusion is right.** The note cites "Ricci-flat locally homogeneous 4-manifold is flat; $\operatorname{Ric}=-g\ne0$ is not flat." That theorem concludes flatness *from* Ricci-flatness and is not the relevant implication here — and general locally homogeneous negative Einstein 4-manifolds do exist (real/complex hyperbolic space). The correct reason the *abelian* case is excluded is that a left-invariant metric on abelian $\mathbb R^4$ (a flat torus) is flat, hence $\operatorname{Ric}=0\ne-g$. Hyperbolic space is homogeneous but not via a free abelian isometric action, so it is not a counterexample. Restate the $N=4$ exclusion as "abelian ⇒ flat ⇒ Ricci-flat, contradicting $\operatorname{Ric}=-g$."

- **The Ricci-flat comparison remark ("K3 examples exist") deserves care.** In the $\lambda=0$ case the same argument forces $F=0$ and $v$ constant on a parabolic base; for a K3 elliptic fibration the base is $S^2$ minus the singular fibers, which is parabolic, so the remark that this "permits nontrivial semiflat collapse" is in some tension with $F=0$ on the parabolic part. This is peripheral to the main result but the parenthetical should be checked before it is relied on as intuition.

**Assumptions that must be carried explicitly with the Proposition** (beyond parabolicity and $\det G$ bounded above already stated): (i) punctures at finite distance with polar, non-cusp, volume-controlled local geometry (Task 2b); (ii) the action genuinely free with no rank drop over the region considered (rank drop is separately flagged as open); (iii) exact local isometric $\mathbb R^N$-action, which holds for the groupoid limit $\mathcal X$ but not for the pre-limit $g_i$ (Task 4); (iv) the interval-with-endpoints case is explicitly incomplete ("modulo endpoint analysis"), and the note's own table records this honestly.

## 7. Cheeger–Tian applied to near-Einstein 4-manifolds — the limit is fine; the concentration structure is not established by the hypotheses cited

Two layers here.

**The exact-Einstein groupoid limit is defensible.** On the regular region, harmonic-coordinate $W^{2,q}$ convergence with $\|E_i\|_{L^\infty}\to0$ gives a weak limit satisfying $\operatorname{Ric}(g_\infty)=-g_\infty$, bootstrapping to smooth; the limit groupoid $\mathcal X$ then carries an exact local isometric action. This part (developed more fully in Step 6) is standard and I have no objection to it. It is precisely why the argument should be run on $\mathcal X$ (Task 4).

**The step producing "at most $\mathcal N(\chi)$ curvature blowup balls" is not supported by $L^\infty$ Ricci-defect control alone.** Cheeger–Tian (JAMS 2006) and the Anderson-type $\epsilon$-regularity that yields finitely many curvature-concentration points use the *exact* Einstein equation, which turns $\operatorname{Rm}$ into an elliptic quantity ($\Delta\operatorname{Rm}=\operatorname{Rm}*\operatorname{Rm}$) and lets small $\int|\operatorname{Rm}|^2$ bootstrap to pointwise bounds. For near-Einstein $g_i$ the equation acquires source terms in $E_i$ and its derivatives; with only $\|E_i\|_{L^\infty}\le\delta_i$ (no control on $\nabla E_i$) the bootstrap that converts small energy density to a pointwise curvature bound is not automatic. The note invokes "Cheeger–Tian gives at most $\mathcal N(\chi)$ balls" and "bounded-curvature collapse applies (CFG 1992)" in one line each; both need a near-Einstein $\epsilon$-regularity statement (or an a priori bound on $\nabla E_i$, or a stronger norm on $E_i\to0$) that is not provided. Also note the stated bound "$|\operatorname{Rm}|\le C(\chi)s_i^{-2}$" diverges as $s_i\to0$, while CFG collapse needs $|\operatorname{Rm}|$ bounded on unit balls — the reconciliation is a rescaling/covering argument that is being compressed. The Chern–Gauss–Bonnet input itself (fixed $\chi$ + bounded Ricci + finite volume ⇒ $\int|\operatorname{Rm}|^2\le C(\chi)$) is correct.

Net: the groupoid limit and the exact orbit-volume exclusion on it are sound modulo the parabolicity hypotheses of Task 2/6; the reduction *to* that regular limit (finiteness of concentration balls, CFG structure) is the part that currently rests on transferring Einstein-specific regularity to near-Einstein inputs without the derivative control that transfer requires. This is the most substantive unresolved mathematical content, and it sits upstream of everything the note proves.

---

## Summary of what is solid and what needs work

| Item | Status |
|---|---|
| Lott eq. → $\lambda=-1$ specialization, subharmonicity (Task 1) | Correct; independently reconfirmed via O'Neill warped product |
| Parabolic bounded-subharmonic-constant contradiction (Task 2) | Conclusion holds; recast via removable-singularity/polar points (dim ≥ 2 exact); needs finite-distance non-cusp puncture geometry; "$v$ bounded from finite volume" should be "$v$ small from collapse" |
| Circle base integral contradiction (Task 3) | Correct and airtight |
| Near-Einstein coefficient $N(1-\delta)$ (Task 4) | Arithmetic correct; presumes exact adapted isometric decomposition — route through the exact limit groupoid instead |
| Capacity estimate $c\int\eta^2\le\int|\nabla\eta|^2$ (Task 5) | **Incorrect**; $\cosh$ counterexample; ground-state identity gives opposite sign. Qualitative exclusion does not depend on it |
| Coverage statement (Task 6) | Accurately restricted; $N=4$ justification mis-stated (should be abelian⇒flat); assumptions (i)–(iv) must travel explicitly |
| Cheeger–Tian on near-Einstein (Task 7) | Exact limit groupoid defensible; finiteness of blowup balls / CFG structure needs near-Einstein $\epsilon$-regularity beyond $\|E_i\|_{L^\infty}\le\delta_i$ — unresolved upstream content |

The central free-abelian exclusion (Sections 2, circle case, applied to the exact limit groupoid) is a genuine and correct piece of mathematics. The two things that most affect whether it becomes a convincing component of the larger negative-branch route are: proving the near-Einstein regularity that delivers the groupoid limit with finitely many concentration points (Task 7), and either discarding or replacing the incorrect capacity estimate wherever the quantitative deficit-transport discussion depends on it (Task 5). Neither of these touches the higher-dimensional statement or the positive branch, consistent with the note's own accounting.