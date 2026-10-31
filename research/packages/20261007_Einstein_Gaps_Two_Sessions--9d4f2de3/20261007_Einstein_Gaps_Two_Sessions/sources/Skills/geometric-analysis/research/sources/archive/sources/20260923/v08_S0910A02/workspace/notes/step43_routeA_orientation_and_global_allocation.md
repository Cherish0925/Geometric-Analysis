# Step 43: Route A orientation correction and global allocation

Session S0910A02. Agent1/Orchestrator. Phase Explore.

## 0. Scope and target fidelity

The active target remains Yau's Problem 26 in the exact session formulation: for every dimension \(n\ge2\), decide whether there are dimension-only constants \(c_n<C_n\) such that every closed connected smooth \(n\)-manifold carrying a metric with
\[
 c_n g\le \operatorname{Ric}_g\le C_n g
\]
necessarily carries some Einstein metric. The constants are not fixed in advance and the output Einstein metric is not required to be related to the input metric.

This note does **not** prove or refute the target. It corrects a route-allocation error created by Step 42: the computation \(\det R_+=0\) for Kähler--Einstein limits is real, but it is not a ceiling on the first obstruction. It is the orientation-compatible side of the obstruction being automatically satisfied; topology can force bubbles on the opposite side, where \(R_-\) is not Kähler-pinned.

The corrected logical target of the current branch is only four-dimensional, positive-sign, noncollapsed behavior; positive collapse, the negative sign, dimensions \(n\ge5\), and the Lean formalization remain separate obligations for the full problem.

## 1. Source facts checked in this step

### 1.1 Ozuch orientation dictionary

Ozuch's higher-obstruction source states the first local obstruction in the precise two-block form. For an Einstein orbifold \((M_o,g_o)\) with an \(\mathbb R^4/\mathbb Z_2\) singularity, a smooth Einstein desingularization by Eguchi--Hanson bubbles forces, depending on the gluing orientation,
\[
\det \mathbf R^+_{g_o}(p)=0 \quad\text{or}\quad \det \mathbf R^-_{g_o}(p)=0 .
\]
This is explicit in `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md`, lines 83--92.

The same source defines the usual orientation family \(\mathbf{eh}_{\zeta^+}\) and the reversed orientation family \(\mathbf{eh}_{\zeta^-}\). In the usual family, the metric is Ricci-flat, anti-self-dual, and its asymptotic term is
\[
H^4(\zeta^+)=-{\rho(\zeta)^-\circ\zeta^+\over 2r^4},
\]
while the obstruction coefficients are
\[
\lambda_k(\zeta^\pm)=c\,\langle \mathbf R^\pm(\psi_*H_2)\zeta^\pm,\zeta_{(k)}^\pm\rangle
\]
(lines 559--560). For the negative-orientation family, the source says \(\mathbf{eh}_{\zeta^-}\) is isometric to \(|\zeta|\mathbf{eh}\) but has the opposite orientation and asymptotic expansion
\[
\mathbf{eh}_{\zeta^-}=\mathbf e-{\zeta^-\circ\rho(\zeta)^+\over2r^4}+O(|\zeta|^4r^{-8})
\]
(lines 372--376). Thus the block tested by the mode projection is genuinely orientation-dependent: \(\zeta^+\) tests \(R_+\), \(\zeta^-\) tests \(R_-\).

### 1.2 Kähler--Einstein pins only the self-dual block in the complex orientation

For a positive Kähler--Einstein surface in its complex orientation, the Kähler identity gives
\[
W_+\sim\operatorname{diag}\left({2\Lambda\over3},-{\Lambda\over3},-{\Lambda\over3}\right),
\qquad
R_+=W_+ + {\Lambda\over3}I
\sim\operatorname{diag}(\Lambda,0,0).
\]
Therefore \(\det R_+=0\) everywhere and the kernel is the two-dimensional anti-Kähler subspace \(\Lambda^{2}_{+,0}\). This was computed in Step 42 and rechecked in `workspace/data/step43_orientation_obstruction_bookkeeping.json`.

But this identity says nothing general about \(W_-\). In a diagonal eigenbasis for a generic trace-free \(W_-\) with eigenvalues \((a,b,-a-b)\),
\[
\det R_- = \left(a+{\Lambda\over3}\right)
\left(b+{\Lambda\over3}\right)
\left(-a-b+{\Lambda\over3}\right),
\]
so \(\det R_-=0\) is one real pointwise condition. The source and algebra therefore support the strategist's correction: a KE limit makes orientation-compatible EH bubbles first-obstruction-compatible, but reversed EH bubbles impose a nontrivial condition on the anti-self-dual block.

There are important caveats. Fubini--Study \(\mathbb CP^2\), with the complex orientation, is self-dual, so \(R_-=(\Lambda/3)I\) and reversed EH insertion is first-order obstructed everywhere. The product Einstein metric on \(S^2\times S^2\), however, is Kähler for both orientations: both blocks have eigenvalues \((\Lambda,0,0)\). Hence \(\det R_-=0\) is not automatically a universal obstruction in the natural product-like stress limit. Any use of the \(R_-\) lever must therefore analyze actual KE/orbifold models, not rely on a slogan that all reversed bubbles are forbidden.

### 1.3 Expected topology is exactly the orientation-compatible case

LeBrun--Ozuch defines expected topology for conformally Kähler Einstein orbifold desingularizations as the case where all Ricci-flat ALE spaces are Kähler in an orientation-compatible manner (`Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--...`, lines 326--328). Under an admissible sequence with Hermitian positive Einstein limit, they prove \(M\) is Del Pezzo, hence \(b_+(M)=1\) (lines 155--168). This is why Step 33's “Hermitian/admissible input unavailable” should not be read as a failure to supply a helpful hypothesis; for spin stress topologies \(\#_k(S^2\times S^2)\), \(k\ge2\), topology forces expected topology to fail.

The failure is structured. In the simplest \(A_1\)/Eguchi--Hanson bookkeeping, an orientation-compatible EH replacement contributes one negative class \((b_+,b_-)=(0,1)\), while reversing the orientation contributes \((1,0)\). If a KE orbifold limit has \(b_+(O)=1\) (true for smooth Fano surfaces and expected for the corresponding rational orbifold setting; exact orbifold cohomology hypotheses still need source-level statement before being used as theorem), and if the smooth target is \(\#_k(S^2\times S^2)\), then
\[
 b_+(M)=k=1+N_- ,
\]
so at least \(k-1\) reversed EH bubbles are required. Those bubbles test \(R_-\), not the Kähler-pinned \(R_+\). The finite table in `workspace/data/step43_orientation_obstruction_bookkeeping.json` records this calculation for sample \(k\) and \(b_-(O)\).

This supplies a mechanism behind the recurring empirical pattern “positive Einstein examples with these extra hypotheses have \(b_+\le1\)”: admissible/Hermitian sequences keep all EH bubbles on the Kähler-compatible side, while \(b_+>1\) demands the reversed side and therefore loses the Hermitian classification shortcut.

## 2. Correction to Step 42

Step 42's algebraic computation \(\det R_+=0\) for all positive KE surfaces is correct. The phrase in its JSON/data saying that the obstruction is “trivial” for KE limits or that desingularization is “possible in principle” is too strong. The correct statement is:

> A positive KE limit automatically satisfies the first obstruction for orientation-compatible EH bubbles. For any reversed EH bubble, the first obstruction is instead \(\det R_-=0\), which is not imposed by the Kähler identity and may be a genuine local condition. Thus KE limits are not harmless; their non-admissible/reversed bubbles are the promising obstruction lever.

This also means the next expensive step should **not** be a broad higher-order \(\Lambda>0\) Ozuch deformation program. Higher-order obstructions remain important later, but the cheap decisive work is the first-order orientation-pair problem: make the pair \((\det R_+,\det R_-)\) obstruction rigorous for merely \(C^0\)-Ricci-pinched noncollapsed sequences using the Step-42 mode projection, and test which side each necessary bubble occupies.

## 3. Noncollapsed family versus fixed-manifold regimes

A second correction concerns the stress-family question.

For the family \(M_k=\#_k(S^2\times S^2)\), \(k\to\infty\), Step 9 already gives a strong dichotomy: if \(\|\operatorname{Ric}-g\|_{op}\to0\) and volumes stay uniformly positive in the normalization \(\operatorname{Ric}\approx g\), Cheeger--Naber finite diffeomorphism type contradicts unbounded \(b_2(M_k)=2k\). Therefore any large-\(k\) positive-sign counterexample family must collapse. Noncollapsed Route A is not needed to settle the large-family noncollapse case.

For a fixed smooth manifold \(M\), however, noncollapsed bubbling remains live. The bubble count is bounded by the \(L^2\) curvature budget and each nontrivial ALE bubble has a positive energy quantum (Eguchi--Hanson is the minimal \(A_1\) case). The bounded count makes the first-order pair obstruction potentially manageable, but it does not by itself rule out bubbling. Route A should therefore be reframed as a fixed-\(M\), noncollapsed compactness/obstruction theorem, not as the solution of the Sha--Yang large-\(k\) family.

Positive collapse is still the required other half of any proof of \(P_4^+\). The toric diagonal route is now a narrow stress lab, not a proof route; the cheaper dimension-flexible collapse line remains the Bochner central almost-Killing/volume-gap bridge.

## 4. Derdziński/Wu/LeBrun instruments and their gap

Derdziński-type rigidity is relevant but cannot currently be invoked from finite singular-point data. The source package says:

- LeBrun--Ozuch Theorem 3.1: for a compact oriented simply-connected \(\Lambda>0\) Einstein orbifold, Hermitian/conformally Kähler is equivalent to \(W^+\) having two equal negative eigenvalues almost everywhere, a global harmonic self-dual form with positivity, or \(\det W^+>0\) everywhere (lines 136--151).
- Catino--Dameno/LeBrun--Derdziński: for a compact oriented Einstein 4-manifold, if the largest eigenvalue of \(W^+\) is everywhere simple (or uniformly simple under additional hypotheses), then the metric is conformally Kähler after a double cover (`Conformal-Kähler-rigidity...`, lines 23--24, 42--61, 91--120).

The honest gap is exactly “everywhere/dense spectral condition” versus “\(\det R_\pm=0\) at finitely many bubble points.” The latter does not imply Hermitian geometry. A plausible way to use the Derdziński/Wu machinery would require upgrading local bubble-point spectral constraints to an open or dense spectral condition, or producing a global harmonic self-dual form whose positivity survives the degeneration. No such upgrade is currently established.

Thus the near-term route should bypass global Kähler classification unless such an upgrade becomes visible: work directly with the pair obstruction and topology/orientation bookkeeping.

## 5. Status of the peer negative-flow route

The new A01 Step 40 review (#358) is important. A01 no longer accepts its own Step 39 theorem or A03 #355 as a theorem. It records concrete remaining proof interfaces: gradient-only support cutoffs, homogeneous \(K_2\) self-improvement, full normalized shifted evolution identities with \(G,T,U,a\), epsilon-uniform transported Yang--DeTurck tame estimates and restart, terminal sign/topology calibration, and strong terminal \(W^{2,p}\) convergence.

This reinforces A02's earlier caution. The negative-flow architecture is valuable, but A02 must not import it as an established conclusion. If it becomes relevant to A02's own proof state, the next action is to verify one load-bearing interface directly, not to accept the whole theorem conditionally. Its ceiling is still a restricted four-dimensional Ishida--LeBrun negative-family gap; it does not prove \(P_4^-\), and proving one sign branch per dimension suffices for Yau--26 whereas a refutation in one dimension must defeat both signs.

## 6. Global route allocation after this step

The current allocation should be:

1. **Primary four-dimensional positive noncollapsed fixed-\(M\) task:** convert Step 42's mode projection into a rigorous first-order pair-obstruction lemma. The receiving agent should prove or sharply test the precise statement:
   \[
   \text{an EH bubble of orientation }\pm\text{ in a }C^0\text{-Ricci-pinched noncollapsed sequence forces }\det R_\pm(p)=0.
   \]
   This requires a Bianchi-gauge angular projection/weak integration-by-parts derivation, not higher-order deformation theory.

2. **Topology/orientation application:** for \(M=\#_k(S^2\times S^2)\) and KE-like orbifold limits, use the intersection-form splitting to force reversed bubbles and then test \(R_-\). Begin with finite model checks (CP2, product \(S^2\times S^2\), toric KE del Pezzo/orbifold points) to see whether \(R_-\)-degeneracy is generic, impossible, or model-dependent.

3. **Cheap positive-collapse line to keep alive:** revisit the Bochner central almost-Killing/volume-gap bridge as the dimension-flexible route. The exact Einstein Kaluza--Klein collapse examples in \(n\ge5\) show collapse is not forbidden, so the question is whether collapse can occur on topologies that lack Einstein metrics or whether collapse itself supplies an Einstein structure. The toric diagonal BVP is lower priority unless it attacks the full variable-curvature determinant/horizontal compatibility problem.

4. **Negative-flow peer work:** keep external unless a specific interface is verified by A02. A01 #358 supplies a repair checklist if A02 chooses to verify it later.

5. **High dimensions:** no current four-dimensional EH/bubble machinery transfers directly to \(n\ge5\). The next high-dimensional exploration should search for either a no-Einstein reservoir with tight Ricci pinching (for refutation) or a dimension-flexible compactness/collapse mechanism (for proof). The Bochner center bound is the only current dimension-flexible analytic object.

## 7. Files from this step

- Algebra/topology data: `Sessions/S0910A02/workspace/data/step43_orientation_obstruction_bookkeeping.json`
- Script: `Sessions/S0910A02/workspace/scripts/step43_orientation_obstruction_bookkeeping.py`

No Lean formalization was attempted in this step; the full proposition remains far from formalization.
