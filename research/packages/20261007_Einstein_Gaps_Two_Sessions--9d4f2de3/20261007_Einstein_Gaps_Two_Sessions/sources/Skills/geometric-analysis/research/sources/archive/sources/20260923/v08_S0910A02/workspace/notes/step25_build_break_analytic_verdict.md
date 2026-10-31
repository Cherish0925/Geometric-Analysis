# Step 25: Toric BUILD/BREAK analytic verdict and individual-equation sign correction

Session S0910A02. Agent2/Constructor. Phase Execute.

## 0. Scope

This note delivers one analytic verdict for the four-dimensional positive-branch
toric \(\#_k(S^2\times S^2)\) BUILD/BREAK question, as requested by the Step-24
handoff and strategist note. It also records a consequential sign correction in
the individual warping equations that was verified by TTCS (Step 25 verifier
task, `trace/ttcs/results/step25_ttcs01_verifier1_integration.md`).

No branch of Yau-26 is resolved. The verdict concerns only the T²-invariant
toric subproblem in dimension 4.

## 1. Sign correction in the individual warping equations

**The Step-14 note recorded:**
\[
-\Delta_B p = (K_B - 1)p, \qquad -\Delta_B q = (K_B - 1)q.
\]

**The correct equations are:**
\[
\boxed{-\Delta_B p = (1 - K_B)p, \qquad -\Delta_B q = (1 - K_B)q.}
\]

**Derivation.** For a twist-free doubly-warped product
\(g = g_B + p^2 d\theta^2 + q^2 d\phi^2\) over a 2D base, Besse's Ricci formula
gives:
\[
\operatorname{Ric}(\partial_\theta,\partial_\theta)/p^2
= -\frac{\Delta_B p}{p} - \frac{\langle\nabla p,\nabla q\rangle}{pq} = 1.
\]
The horizontal trace equation gives, after denoting
\(\gamma = \Delta p/p = \Delta q/q\):
\[
2K_B - 2\gamma = 2, \qquad \gamma = K_B - 1.
\]
So \(-\Delta p/p = 1 - K_B\), and substituting back:
\(\langle\nabla p,\nabla q\rangle/(pq) = -\gamma - 1 = -K_B\).

**Anchor verification:**
- \(S^2\times S^2\): \(K_B=0\), \(p=\sin x\). \(-\Delta(\sin x) = \sin x = (1-0)\sin x\). ✓
- Eigenvalue cross-check: \(\Delta(pq) = -(1-K_B)pq - (1-K_B)pq - 2K_B pq = -2pq\).
  Hence \(-\Delta_B w = 2w\). ✓

## 2. Corrected Green identity: flux equi-partition only

The Step-20 energy script derived from the wrong-sign equations an identity
\(\int_\Omega K_B w\,dA = \int_\Omega w\,dA\). This identity is **FALSE**.

**Correction:** Apply Green's formula with the correct equations:
\[
\int_\Omega\langle\nabla p,\nabla q\rangle\,dA + \int_\Omega q\,\Delta p\,dA
= \int_{\partial\Omega} q\,\partial_\nu p\,ds.
\]
Substituting \(\langle\nabla p,\nabla q\rangle = -K_B w\) and \(\Delta p = -(1-K_B)p\):
\[
-\int K_B w - \int(1-K_B)w = -\int w.
\]
So:
\[
\boxed{\Phi_p = \int_\Omega w\,dA, \qquad \Phi_q = \int_\Omega w\,dA.}
\]
The \(K_B\) terms cancel completely. There is **no interior weighted-curvature
identity**. The only content is the flux equi-partition: p-rod flux = q-rod flux
= \(\int w\), and total flux \(= 2\int w\).

**Anchor:** For \(S^2\times S^2\) with \(K_B=0\), \(\int w = 4\) and each pair of
p-rods (at \(x=0\) and \(x=\pi\)) gives flux \(\int\sin y\,dy = 2\) each, total
\(\Phi_p=4=\int w\). ✓

## 3. Rod saturation: G_i → 1 is possible

Define the Q-weighted negative-curvature charge of rod \(i\):
\[
G_i := \int_{\mathrm{rod}_i} (-K_{\mathrm{edge}}) Q_i\,ds, \qquad
\Phi_i = 2 - 2G_i.
\]

For a constant-curvature rod \(K_{\mathrm{edge}} = -A\), \(A > 0\):
\[
G_i = \int_0^L A\,Q\,ds = A\cdot\Phi_i = \frac{2A}{1+2A}, \qquad
\Phi_i = \frac{2}{1+2A}.
\]

**Limits as \(A\to\infty\):** \(G_i \to 1\), \(\Phi_i \to 0\). ✓ (SymPy-verified.)

So a single constant-curvature rod can drive its flux to zero while its
Q-weighted negative charge saturates at the maximum value 1.

## 4. The alpha-family passes all tested constraints

For \(m = 2k+2\) rods with \(A_m = m^\alpha\), \(\alpha > 1\):
\[
\Phi_i = \frac{2}{1+2m^\alpha}, \qquad
\text{total }\Phi = \frac{2m}{1+2m^\alpha} \sim m^{1-\alpha} \to 0.
\]

By the (corrected) TTCS-derived summed identity:
\[
\int_\Omega w\,dA = m + \sum_{i=1}^m \int_{\mathrm{rod}_i} K_{\mathrm{edge}} Q_i\,ds
= m - \sum_i G_i = m\cdot\frac{1}{1+2A_m} \to 0.
\]

The alpha-family simultaneously satisfies:
| Constraint | Status |
|---|---|
| Rod ODE \(Q''+(\ldots)Q=0\), unit slopes | ✓ |
| Local corner Ricci matching (Step 19) | ✓ through first nontrivial order |
| Signed Gauss–Bonnet scale | ✓ |
| Bishop volume ceiling | ✓ |
| Eigenvalue equation \(-\Delta w = 2w\) | Compatible (∫w → 0 allowed) |
| Flux equi-partition | ✓ (\(\Phi_p = \Phi_q = \int w\)) |
| Traceless horizontal (Step 20) | No additional collar obstruction |
| Rod saturation \(G_i \to 1\) | ✓ |

## 5. Traceless equation on the collar-to-interior transition

The traceless horizontal equation in conformal \(z\) of \(g_B\):
\[
(\log w)_{zz} + \tfrac12[(\log w)_z^2 + v_z^2] = 0.
\]

Step 20 checked this in flat rod-collar coordinates: residual = \((1+2A)/4\),
which equals the base curvature effect \(-K_B/2 + 1/4\). This is not a new
constraint — it is already included in the curved-base Ricci equations that
the Step-19 corner matching solves. Step 19 checked the full Ricci tensor
(all 4 components) in Fermi coordinates of the curved base through the first
nontrivial formal order. Result: compatible with \(A\) free.

**Conclusion.** The traceless equation does not produce a separate obstruction
on the collar or at the collar-to-interior transition. Any BUILD obstruction
must involve the full coupled system globally, not a local or integral identity.

## 6. VERDICT

**BREAK-compatible at the level of all tested integral identities.**

No integral identity among the four verified reduced equations (eigenvalue,
v-equation, traceless horizontal, horizontal trace) forces \(\int w\) — equivalently
the total 4-volume — bounded below independently of \(m\). The previous candidate
constraint \(\int K_B w = \int w\) was an artifact of a sign error in the
individual warping equations; the correct Green identity yields only the flux
equi-partition \(\Phi_p = \Phi_q = \int w\), with no interior curvature pinning.

### What BUILD needs

A global PDE solvability obstruction for the full coupled system on periodic-label
polygons. No integral, spectral, or local identity tested in this session provides
this. The missing object would be either:
- A nonlinear Pohozaev-type identity that forces \(\int w \ge c_0\), or
- A global regularity/smoothing argument showing the boundary-normalized
  eigenfunction on a domain of fixed area cannot have arbitrarily small
  boundary gradient.

### What BREAK needs

An actual smooth global metric with \(\int w \to 0\) satisfying all four equations.
The alpha-family is formal rod/corner-compatible data, not a global smooth solution.

### Impact on Yau 26

This analysis concerns only the \(T^2\)-invariant toric subproblem in dimension 4.
Even a full BREAK (constructing the global metric) only shows that
\(\#_k(S^2\times S^2)\) admits tight positive pinching with collapse; it does **not**
refute Yau-26 because Einstein existence on \(\#_k(S^2\times S^2)\) for large \(k\) is
an independent open problem (positive scalar curvature kills the SW obstruction).

## 7. The entanglement structure of Yau 26

Following the strategist note and Step 24, the correct organizing principle is:
\[
P_n^+ \text{ holds} \quad\Longleftrightarrow\quad
\{\text{closed }n\text{-manifolds admitting tight positive pinching}\}
\subseteq \{\text{closed }n\text{-manifolds admitting Einstein metrics}\}.
\]

The toric alpha-family tests whether \(\#_k(S^2\times S^2)\) lies in the LEFT set.
The Einstein-existence question asks whether it lies in the RIGHT set. Both are open.
The BREAK/BUILD verdict determines which horn of the entanglement we are on:
- **BUILD:** the left set is smaller than expected (tight pinching forces a
  volume gap), which, combined with Cheeger–Naber compactness, could give
  a positive-branch proof in dim 4.
- **BREAK:** the left set is large (tight pinching allows collapse on
  \(\#_k(S^2\times S^2)\)), and P₄⁺ reduces to Einstein existence on that family.

The current evidence tilts toward BREAK at the integral level, but neither
conclusion is established.

## 8. Files

| File | Content |
|------|---------|
| `scripts/step25_weighted_curvature_identity_test.py` | Initial WCI derivation and S²×S² falsification |
| `data/step25_weighted_curvature_identity_test.json` | WCI test output with anchor contradiction |
| `scripts/step25_build_break_analytic_verdict.py` | Complete corrected analysis |
| `data/step25_build_break_analytic_verdict.json` | Full verdict with alpha-family data |
| `trace/ttcs/results/step25_ttcs01_verifier1_integration.md` | TTCS verification of sign correction |
| `trace/ttcs/results/step25_ttcs01_sub1_verifier.md` | Branch 1 record |
| `trace/ttcs/results/step25_ttcs01_sub2_verifier.md` | Branch 2 record |

**Erratum to Step 14:** Table row "1" should read
\(-\Delta_B p = (1-K_B)p\), not \((K_B-1)p\). The corrected horizontal equation
and the identity \(K_B = \frac14(|\nabla v|^2 - |\nabla\log w|^2)\) are unaffected
because they were derived from the eigenvalue equation and the cross-gradient,
not from the wrong individual equations. The Step-14 Faber–Krahn area lower
bound, Euler non-uniformity, and the qualitative fork (BUILD vs BREAK) are
unaffected. The Step-14 "uniform-K_B stabilization" (Section 8) used the correct
eigenvalue equation and rod identity, not the individual equations, so its
content is also unaffected.

**Erratum to Step 20:** The identity `int K_B w = int w` in the script
`step20_global_energy_identity.py` and its JSON output is wrong. Correct: only
\(\Phi_p = \Phi_q = \int w\) holds. The stream function energy identity
\(\int|\nabla\psi|^2 = 2\int w^2 + 4\int K_B w^2\) is derived from the horizontal
trace equation and is unaffected.
