# Step 26: nilpotent abelian-forcing audit for the positive branch

Session S0910A02. Agent3/Actuator. Phase Execute.

## 0. Scope and conclusion

This step tested the Step-25 "abelian forcing" idea for positive Ricci collapse.  The
active Yau-26 target is unchanged: decide the full all-dimensional Ricci-pinching
criterion for Einstein existence.  The work here is only a structural piece for the
positive branch; it proves no branch of Yau-26 and starts no Lean formalization.

The main correction is that a Milnor-only proof is too strong once the second
fundamental form of the collapsing fibers is allowed.  For a Heisenberg fiber with
orthonormal bracket
\[
[e_1,e_2]=b e_3,
\]
Milnor gives
\[
\operatorname{Ric}^F=(-b^2/2,-b^2/2,+b^2/2),\qquad \operatorname{scal}_F=-b^2/2.
\]
Positive two-sided pinching controls vertical anisotropy in the *total* Ricci tensor,
so the question is whether the O'Neill twist and second-fundamental/mean-curvature
terms can reproduce the opposite pattern.  The answer from the local algebraic tests
is:

- With totally geodesic fibers (\(T=0\)), the statement is clean but narrow: upper
  pinching in the center direction bounds \(b^2/2\le 1+\delta\), and exact \(\operatorname{Ric}=g\)
  requires a positive-semidefinite twist quadratic form \(Q=I-\operatorname{Ric}^F\) of
  rank at least 2--3.  In particular an \(H_3\) fiber over a 2-dimensional base is
  impossible by rank alone, but this is not the general collapse theorem.
- With \(T\ne0\), local exact \(\operatorname{Ric}=g\) equations admit large-\(b\) data.
  They force \(|T|\sim b\) and rapid relative rescaling of the fiber directions, but
  they do not give a pointwise contradiction.  Thus the valid theorem, if true, must
  be a graded/relative-rate/global statement: ungraded homothetic nonabelian collapse
  is ruled out or converted into an iterated abelian collapse, while second-fundamental
  terms carry the contested balance.

The reproducible computations are
`workspace/scripts/step26_nilpotent_submersion_balance.py` ->
`workspace/data/step26_nilpotent_submersion_balance.json`, and the independent moving
frame check `workspace/scripts/step26_heisenberg_moving_frame_ricci.py` ->
`workspace/data/step26_heisenberg_moving_frame_ricci.json`.

## 1. Source check for the lower-Ricci nilpotent input

The strategist note asked not to hide the collapse bridge behind unavailable bounded
sectional-curvature theory.  Directly read sources support the following bounded
statement.

Naber--Zhang quote Kapovitch--Wilking's generalized Margulis lemma in
`Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md`,
lines 373--389: for a complete \(n\)-manifold with
\(\operatorname{Ric}\ge -(n-1)\), the image of the short-loop group
\(\Gamma_{\epsilon_1}(p)\) is \((w(n),n)\)-nilpotent; near a \(k\)-dimensional Ricci
limit ball, the refined fibered group has rank at most \(n-k\).  Proposition 5.9,
lines 1332--1341, says that if this rank is maximal then the local universal cover is
noncollapsed.  Rong's `Collapsed Manifolds with local Ricci bounded Covering Geometry`
confirms the same landscape: lines 23--29 define local Ricci-bounded covering geometry;
lines 84--86 give an infra-nil conclusion for maximally collapsed manifolds under that
extra covering noncollapse; lines 94--114 state a smooth nilpotent fiber-bundle theorem
when the collapsed manifold is GH-close to a noncollapsed lower-dimensional manifold
with local rewinding volume lower bound; lines 132--166 recall the KW Margulis input
and the rank estimate.

Thus, under positive pinching, the **short-loop groups** are almost nilpotent by the
lower Ricci bound alone.  A smooth Riemannian submersion with controlled \(A,T,N\) still
requires additional regular-region, covering-noncollapse, or GH-base hypotheses.  The
gap is sharper than before: not "there is no nilpotent information," but "one must
turn lower-Ricci almost-nilpotent local groups plus upper Ricci pinching into a
controlled, preferably virtually-abelian, collapse model."

## 2. Short toric addendum from the strategist note

Step 25 correctly removed the false Step-20 identity \(\int K_B w=\int w\), but the
phrase "no interior curvature constraint" should be read as "no such integral
weighted-curvature identity."  The corrected individual equation is
\[
-\Delta_B p=(1-K_B)p,
\]
so equivalently
\[
(-\Delta_B+K_B)p=p
\]
with mixed boundary conditions: Dirichlet on the \(p\)-rods and Neumann behavior on
\(q\)-rods, and symmetrically for \(q\).  This mixed eigenvalue condition is real
interior variational content, stronger than \(-\Delta w=2w\).  For the formal
\(\alpha\)-family it does not obstruct collapse because the boundary-layer cancellation
is exact: along a short rod, the endpoint vanishing fixes a tangential mode of size
\(\pi^2/L^2\sim 2A\), which offsets the potential well \(K_B=-A\).  The remaining
BUILD freedom is therefore at the corner-to-interior junction and in the next order of
this cancellation, not in another global integral identity.  I did not run new toric
numerics in this step because boundary discretization noise would not test this
analytic cancellation.

## 3. Twist-only test: clean but narrow

For a totally geodesic submersion model, the vertical Ricci equation has the schematic
form
\[
\operatorname{Ric}_M^V(U,U)=\operatorname{Ric}^F(U,U)+Q(U,U),\qquad
Q(U)=\sum_i |A_{X_i}U|^2\ge0,
\]
where \(Q\) is generated by the vertical-valued curvature/twist vectors
\(\omega_{ij}=A_{X_i}X_j\).  Hence
\(\operatorname{rank}Q\le {d\choose2}\), where \(d\) is the base dimension.

For \(H_3\), exact \(\operatorname{Ric}=g\) would require
\[
Q=\operatorname{diag}(1+b^2/2,\ 1+b^2/2,\ 1-b^2/2).
\]
Consequences checked in `step26_nilpotent_submersion_balance.json`:

- The center direction gives the immediate upper-pinching bound
  \(b^2/2\le 1+\\delta\) in a \([1-\delta,1+\delta]\)-pinched model with \(T=0\).
- If \(b<\sqrt2\), the required \(Q\) is positive definite, rank 3, so at least
  \({d\choose2}\ge3\), i.e. \(d\ge3\), is needed by rank alone.
- At \(b=\sqrt2\), the center component of \(Q\) vanishes and rank drops to 2;
  a 2-dimensional base still has only rank 1 twist and cannot realize it.
- If \(b>\sqrt{2(1+\delta)}\), even positive-semidefinite twist cannot repair the
  center upper bound.

This confirms the strategist's warning: the test case \(H_3\) over a 2-base is too
easy if \(T=0\); it validates the rank obstruction but not the desired all-dimensional
abelian-forcing theorem.

## 4. T-active Heisenberg model: pointwise Milnor forcing fails

To test whether second fundamental form can reverse Milnor anisotropy, I used the
cohomogeneity-one diagonal metric
\[
g=dt^2+a(t)^2(\theta_1^2+\theta_2^2)+c(t)^2\theta_3^2,
\qquad [E_1,E_2]=E_3,
\]
with orthonormal bracket
\[
b=c/a^2,
\qquad k_1=a'/a,
\qquad k_3=c'/c,
\qquad H=2k_1+k_3.
\]
The moving-frame computation from the brackets
\([e_0,e_1]=-k_1e_1\), \([e_0,e_2]=-k_1e_2\),
\([e_0,e_3]=-k_3e_3\), \([e_1,e_2]=be_3\) gives
\[
\begin{aligned}
\operatorname{Ric}_{00}&=-2(k_1'+k_1^2)-(k_3'+k_3^2),\\
\operatorname{Ric}_{11}=\operatorname{Ric}_{22}&=-\frac{b^2}{2}-k_1'-Hk_1,\\
\operatorname{Ric}_{33}&=+\frac{b^2}{2}-k_3'-Hk_3.
\end{aligned}
\]
The independent script `step26_heisenberg_moving_frame_ricci.py` verifies these
formulas exactly from Koszul/anholonomic curvature.  Imposing vertical
\(\operatorname{Ric}_{ii}=1\) yields
\[
k_1'=-1-\frac{b^2}{2}-Hk_1,
\qquad
k_3'=-1+\frac{b^2}{2}-Hk_3,
\qquad
\frac{b'}b=k_3-2k_1.
\]
The \(00\)-equation is the Hamiltonian constraint
\[
4k_1^2+8k_1k_3+b^2+4=0.
\]
The corrected moving-frame output records
\(\operatorname{Ric}_{00}-1=\tfrac12(4k_1^2+8k_1k_3+b^2+4)\) after the vertical
substitution, so this constraint is exactly equivalent to \(\operatorname{Ric}_{00}=1\).

The numerical ODE sample starts at
\[
b_0=20,
\qquad k_1=10,
\qquad k_3=-10.05,
\]
which satisfies the constraint.  Integration over \(t\in[0,0.01]\) succeeds with
sampled constraint error \(<7\times10^{-13}\) and Ricci error \(<3\times10^{-13}\).
Thus large bracket is locally compatible with exact positive Einstein equations, but
only with large, anisotropic fiber second fundamental form:
\[
2k_1^2+k_3^2\approx 301\quad\text{at }t=0,
\]
and rapid bracket evolution \(b'\approx -601\).  The local model is not compact and is
not a Yau-26 counterexample; its role is to falsify a naive pointwise theorem that
ignores \(T\).

## 5. Scaling interpretation and a corrected theorem target

For a Heisenberg nilmanifold with generator scale \(a=\varepsilon^\alpha\) and center
scale \(c=\varepsilon^\gamma\), the orthonormal bracket is
\[
b=c/a^2=\varepsilon^{\gamma-2\alpha}.
\]
The audit records three regimes:

- **Homothetic collapse** \((\gamma=\alpha)\): \(b\sim\varepsilon^{-\alpha}\to\infty\).
  This is impossible in the \(T=0\) model and in the \(T\ne0\) local model requires
  \(|T|\sim b\), i.e. very rapid relative variation.
- **Graded collapse** \((\gamma=2\alpha)\): \(b=O(1)\), while at the first visible
  diameter scale the bracket is small.  The commutator direction has already collapsed
  to the next scale.
- **Super-graded collapse** \((\gamma>2\alpha)\): \(b\to0\), genuinely abelian at the
  fiber metric scale.

The corrected all-dimensional theorem target is therefore not "positive pinching makes
the nilpotent fiber topologically abelian."  A plausible sharp statement is closer to:

> Under a regular nilpotent-submersion model with \(\operatorname{Ric}\in[1-\delta,1+\delta]\),
> nonabelian brackets cannot persist at the first collapse scale unless compensated by
> second-fundamental/mean-curvature terms of the same size.  If those terms are
> uniformly controlled in the scale supplied by the lower-Ricci covering/fibration
> theorem, then the first collapse stage is virtually abelian.  Nonabelian collapse, if
> present, must be graded and decomposes into iterated abelian stages.

This would fit the Step-24 KK picture: the first stage supplies circle/torus equations
(determinant trace, Yang--Mills/twist conservation, and lower-dimensional positive
Einstein--Maxwell data), while any nilpotent commutator directions are relegated to
smaller scales.  However, the required hypotheses are still substantial: one needs a
regular or local-covering nilpotent fibration, control of \(T\) or an integrated scalar
identity strong enough to control it, and treatment of singular/fixed strata.

## 6. Scalar identity status

The strategist suggested using the integrated O'Neill scalar identity.  I did not
certify the full general coefficient convention in this step.  The accessible source
`Ricci-positive-metrics-on-connected-sums-of-projective-spaces` lines 179--183 states
that O'Neill formulas relate total curvature to base/fiber curvature through \(A\) and
\(T\), and cites Besse/O'Neill; lines 183--196 give a reliable totally-geodesic warped
submersion formula used for comparison.  A direct O'Neill/Besse formula source was not
successfully ingested by `knowledge_request`, which returned irrelevant tensor files.

For the cohomogeneity-one model, the scalar identity derived from the verified Ricci
components is
\[
\operatorname{scal}_M=-\frac{b^2}{2}-4k_1'-2k_3'-6k_1^2-4k_1k_3-2k_3^2.
\]
The negative intrinsic scalar \(-b^2/2\) is offset locally by derivative/mean-curvature
terms when exact \(\operatorname{Ric}=g\) holds.  On a closed fibration, divergence terms
and boundary/fixed-stratum flux accounting become decisive, just as in the toric rod
system.  This remains a good next verification target, but this step's established
result is the local T-active obstruction to a pointwise Milnor argument.

## 7. Peer-message assimilation

A03 message #309 corrected the negative-branch curvature-flow normalization: the
fully lowered curvature tensor acquires a physical conformal scaling term, but the
corresponding contribution to \(|\mathrm{Rm}|^2d\mu\) cancels after inverse-metric and
volume variations; plateau regularity is standard, transition \(L^\infty\) is still not
closed.  A01 message #310 reports a schematic tensor derivation of the buffered
support energy inequalities and adopts the same normalization correction.  These
sharpen the four-dimensional negative side branch but do not change the positive
nilpotent-collapse audit above.  I did not verify A01's tensor derivation because it
was not a direct request and the positive abelian-forcing target was higher priority.

## 8. What this changes for Yau-26

This step strengthens the positive-branch architecture while narrowing its theorem
claim.  Lower Ricci already gives almost-nilpotent local fundamental groups via
Kapovitch--Wilking/Naber--Zhang.  The upper Ricci bound should now be used not to
forbid all nonabelian nilpotent collapse pointwise, but to force a graded filtration:
first-stage visible collapse should be abelian unless large \(T/N\) terms are present;
large \(T/N\) terms require global scalar/divergence or singular-stratum accounting.

Thus the best continuation is a verifier/critical-review step on whether the proposed
regular nilpotent-submersion theorem can be made mathematically true with explicit
hypotheses, using the Step-26 files and exact O'Neill formulas.  If it survives, Agent2
can try to formalize the theorem statement and proof in the regular case.  If it fails,
Agent1/Agent4 should redirect the positive branch toward toric fixed-strata/global PDE
or toward a different characterization of the left-hand pinching class.
