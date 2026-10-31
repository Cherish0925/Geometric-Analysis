> **SUPERSEDED** by `route_assessment_step37.md` for continuation/first-exit.
> Step 36 note and platform analysis remain valid background.


## Main work of this step

Step 36 advanced the restricted four-dimensional negative Ishida--LeBrun
cutoff-flow route at the analytic-platform interface.  The previous step had
proved the Hessian-cutoff contraction tensors, so the first smoothing estimates
can now be separated from pointwise evolving cutoff-Hessian control.  This step
used that separation to record the correct flow platform, the independent global
unweighted defect estimate, and the continuation interface without treating the
still-missing extension theorem as solved.

Produced files:

- `workspace/notes/step36_analytic_platform_and_global_Q.md`
- `workspace/scripts/step36_platform_Q_verify.py` (20/20 checks pass)
- TTCS verifier: `trace/ttcs/results/step36_ttcs01_verifier1_integration.md`
- TTCS verifier of A03 Step 37 interfaces: `trace/ttcs/results/step36_ttcs02_verifier1_integration.md`

## Accepted mathematical advances

### 1. Correct transported-coefficient normalized DeTurck formulation

For the target flow
\[
  \partial_tg=-2a(\operatorname{Ric}_g+g),\qquad a=\chi^2,
\]
the correct hatted DeTurck system transports the coefficient:
\[
  \widehat a=a\circ\varphi_t^{-1},
\]
and uses the full Lie derivative
\[
  \mathcal L_{\widehat aW}\widehat g
  =\widehat a\mathcal L_W\widehat g
   +d\widehat a\otimes W^\flat+W^\flat\otimes d\widehat a .
\]
A fixed term \(\widehat a\mathcal L_W\widehat g\) would not pull back to the
fixed-cutoff equation.  With
\(\partial_t\varphi_t\circ\varphi_t^{-1}=-\widehat aW\), the pullback identity is
\[
  {d\over dt}\varphi_t^*\widehat g
  =-2a(\operatorname{Ric}_g+g).
\]
The normalized term contributes only the new lower-order variation
\[
  \delta(-2\widehat a\widehat g)
  =-2\widehat a h-2(\delta\widehat a)\widehat g,
\]
while \(-2(\delta\widehat a)\operatorname{Ric}_{\widehat g}\) belongs to Yang's
already-present transported Ricci coefficient variation.  The stronger claim that
\(\delta\widehat a\) carries a full \(\widehat a\) factor is not generally true;
only
\(\delta\widehat a=-2\widehat\chi\,d\widehat\chi(Y)\) is expected.  This is harmless
for per-datum existence because it remains lower order in the linearized
\((h,Y)\) system.

Using Yang's published tame-energy construction (not ordinary
\(\varepsilon\)-Schauder constants), short-time smooth existence for each fixed
smooth datum is acceptable at the level needed here.  The time may depend on the
entire input geometry.

### 2. Independent global \(Q\) persistence

The global unweighted defect
\[
  Q(t)=\int_M|E(t)|^2\,d\mu_t,
  \qquad E=\operatorname{Ric}+g,
\]
feeds terminal calibration and cannot be recovered from
\(J_6=\int\eta^2a^4|E|^6\) or \(\|aE\|_\infty\).  The homogeneous defect equation,
including both \(\nabla a*E*\nabla E\) and \(\nabla^2a*E*E\), gives
\[
  Q_U'+cX_U
  \le C(1+r^{-2})Q_U+C\int_{\operatorname{supp}\chi}F(\chi E)^2,
  \qquad X_U=\int_U a|\nabla E|^2 .
\]
The Hessian term is handled by signed integration by parts using the Step 35
quadratic tensor
\[
  B_{\rm def}=|E|^2g+(\operatorname{tr}E)E-2E^2,
  \qquad |\nabla B_{\rm def}|\le C|E||\nabla E|,
\]
and \(|da|^2/a=4|d\chi|^2\le Cr^{-2}\).  With a buffered energy
\(K_2^\eta=\int_U\eta^2F^2\), \(\eta\equiv1\) on \(\operatorname{supp}\chi\),
\[
  \int F(\chi E)^2
  \le C\mathcal S(K_2^\eta)^{1/2}(X_U+r^{-2}Q_U)
  =C\gamma(X_U+r^{-2}Q_U).
\]
For small \(\gamma\), summing over macro-disjoint supports and using the frozen
complement gives
\[
  Q(t)\le e^{C(1+r^{-2})t}Q(0)
       \le e^{C\theta(1+r^2)}Q(0),\qquad t\le\theta r^2.
\]
If a separate normalization fixes \(r\le1\), this can be abbreviated by a
\(Cr^{-2}\) coefficient.  The longer coefficient is the safer default.

### 3. Signed Hessian-cutoff lemma for continuation terms

A03 Step 38 repaired the previous base-pair handoff.  For a signed term
\[
  J=\int\chi\nabla_i\nabla_j\chi\,B^{ij}(V),
  \qquad |B(V)|\le C_p|V|^p,
  \quad |\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|,
\]
one integration by parts yields
\[
  |J|\le \varepsilon\int\chi^2|\nabla V|^2|V|^{p-2}
       +C_{p,\varepsilon}\|d\chi\|_\infty^2\int|V|^p.
\]
This avoids the invalid direct Hölder estimate
\(\int\chi|\nabla^2\chi||W|^p\lesssim\|\nabla^2\chi\|_p\|W\|_p^p\), which would
actually require \(W\in L^{p^2/(p-1)}\).  It repairs the finite-\(L^p\) base
estimate for \((\nabla U,\nabla^2\chi)\) and the apparent single-Hessian term at
\(m=2\), but does not by itself prove a full extension theorem.

## Still-open analytic work

The continuation/platform is not closed.  The exact remaining mathematical
calculations are:

1. Derive the normalized shifted unweighted \(L^p(T)\) inequality for
   \(T=\operatorname{Rm}+G\), because \(\sup|U|=\sup|aT|\) does not control
   unweighted \(T\) near \(a=0\).  Wang's unnormalized Lemma 4.10 is a roadmap,
   not a written proof for this shifted normalized system.
2. Write the full index-level evolution of \(U=a(\operatorname{Rm}+G)\) and
   \(W=\nabla U\), including all \(G\), connection, normalization, and cutoff
   terms, and check no unweighted \(T\)- or \(\nabla T\)-coefficient remains.
3. Complete the higher-order staggered induction for
   \((\nabla^mU,\nabla^{m+1}\chi)\), including top cutoff jets coupled to
   differentiated lower curvature factors.
4. Only after obtaining a genuine next-derivative level use Sobolev embedding to
   get pointwise derivative bounds and a smooth terminal limit as
   \(t\uparrow T_{\max}\).
5. Assemble the full first-exit theorem with the corrected independent roles of
   \(K_2^\eta\), \(Y\), \(J_6\), \(Q\), \(\|aE\|_\infty\), metric drift, moving
   Sobolev constants, and the flow platform.

## Conditional fixed-exponent chain now supported

On a smooth first-exit interval with macro-disjoint buffered supports and
\(\gamma_j=\mathcal S_j(K_{2,j}^\eta)^{1/2}\ll1\), the following fixed-exponent
module is now well supported:

\[
  K_2^\eta \Rightarrow \int_0^tY\le C\gamma K_2^\eta(0),
  \qquad Y(t)\le C\gamma K_2^\eta(0)/t,
\]
via the q=2 energy, q=3 good-slice propagation, and the Step 35 curvature tensor
identity.  A03 Step 38 records the same fixed-exponent layer and conditional
Moser outputs.  The module remains conditional on the smooth first-exit interval
and moving support/Sobolev hypotheses.

## Positive branch context from A02 Step 38

A02's Step 38 concerns the separate positive/collapsed toric branch.  It retracts
the earlier NUT-only survival claim: conical singularities are rod-period defects,
and nonadjacent rods with labels \(\pm v\) share the same circle period.  For
finite noncompact alternating chains, the exact same-label period range is
\[
  \prod_{k=1}^{n-1}{2k+1\over2k},
\]
verified numerically for \(m=4,6,8,10\), but this is an end effect and does not
settle compact Delzant polygons.  The open positive-branch question is whether
compact-polygon period monodromy for \(m=6,8\) is nontrivial after variable rod
lengths and positive-Einstein boundary conditions are allowed.  This does not
change the negative-flow route, but it reinforces that neither branch currently
decides the full Yau Problem 26.

## Current judgment

The restricted negative route is significantly stronger than before Step 35: the
first smoothing estimates have index-level Hessian control and the analytic
platform now has a correct DeTurck formulation plus independent \(Q\) propagation.
The hard part has moved to a precise continuation theorem and first-exit
assembly, not to local tensor algebra.  Even completing that would only rule out
near-critical Ishida--LeBrun negative counterexamples in dimension four; the
positive branch, arbitrary four-manifold topology, dimensions \(n\ge5\),
dimension-only constants, and Lean formalization remain unsolved.
