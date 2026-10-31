# Step 58: Biquard estimate located, Cheeger--Tian transfer ceiling, and collapse energy pinning

Session `S0910A02`, Agent3 / Explore.

This note records source-grade and computational checks that change route allocation for Yau--26. It is not a proof or counterexample.

## 1. Biquard estimate: the useful estimate is Section 4, not Section 14

The human scientist supplied the missing Biquard source (`arXiv:1105.4904`). I downloaded it to

- `workspace/data/source_text/biquard_1105_4904.pdf`
- `workspace/data/source_text/biquard_1105_4904_pdftotext.txt`

and checked the relevant text directly. The earlier inherited phrase "Biquard §14 estimate" is wrong for the local Ricci residual used in our Yau--26 near-pinching construction: in the arXiv version §14 is a transversality argument. The needed estimates are in **§4, Lemmas 4.1--4.2**.

Source anchors in the extracted text:

- lines 96--112: Theorem 0.1 is an AH, nondegenerate, exact-desingularization theorem; it also states that if there are several \(\mathbb R^4/\mathbb Z_2\) singularities, they may be desingularized simultaneously or on a subset. This is stronger than what we need but carries AH/global hypotheses.
- lines 146--153: if \(\det R^-\) vanishes, one glues the opposite-orientation Eguchi--Hanson metric; the actual parameter is a kernel line in \(O(4)/U(2)\). This supports the compatible/reversed orientation dictionary.
- lines 1264--1269: §4 constructs metrics satisfying the Einstein equation approximately modulo Eguchi--Hanson obstructions; up to §8 the orbifold may be compact or noncompact. This matters because the raw approximate estimate is not tied to AH boundary transversality.
- lines 1331--1358: Lemma 4.1 gives, on the EH region,
  \[
  \left|\nabla^k\left(\operatorname{Ric}_{h_{t,\phi}}-t\Lambda h_{t,\phi}-t\sum_{j=1}^3\lambda_j o_j\right)\right|_{eh}
  \le c_k t^2\rho^{2-k}.
  \]
- lines 1361--1399: the matching uses \(\beta=1/4\), \(\rho\lesssim t^{-1/4}\), and a cutoff \(\chi_t\) with \(|\partial_r^k\chi_t|\le c_k t^{k/4}\).
- lines 1408--1429: Lemma 4.2 gives the same estimate for the glued approximate metric,
  \[
  \left|\nabla^k\left(\operatorname{Ric}_{g_{t,\phi}}-\Lambda g_{t,\phi}-t\sum_{j=1}^3\lambda_j\chi_t o_j\right)\right|_{eh}
  \le c_k t^2\rho^{2-k}.
  \]
  The warning at lines 1425--1429 says the norm is in the EH metric and the error from truncating \(o_j\) is absorbed in \(t^2\rho^2\).
- lines 1430--1453: the naive gluing estimate is only \(O(t)\) in the EH norm, hence order one in the scaled operator norm; the refined matching is not optional.

## 2. Operator-norm scaling for the Yau--26 input metric

On the inserted core the compact metric is \(g_t\sim t\,eh\). Thus a \((0,2)\)-tensor that has EH norm \(A\) has \(g_t\)-operator size \(t^{-1}A\).

From Biquard Lemma 4.2 with \(k=0\):
\[
|\operatorname{Ric}_{g_t}-\Lambda g_t-t\sum\lambda_j\chi_t o_j|_{eh}\le C t^2\rho^2,
\qquad \rho\le C t^{-1/4}.
\]
Therefore
\[
\|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t-t\sum\lambda_j\chi_t o_j)\|
\le C t\rho^2 \le C t^{1/2}.
\]
In the core \(\rho=O(1)\) this is \(O(t)\). The obstruction term is different:
\[
\|g_t^{-1}(t\lambda_j o_j)\|\sim |\lambda_j|\,|o_j|_{eh},
\]
which is order one near the EH core if any \(\lambda_j\ne0\). Hence:

- the refined approximate metric gives a genuine Yau--26 input sequence **only after the first vector obstruction is killed at each inserted node**;
- higher obstruction terms \(t^q o\) with \(q>1\) have core operator size \(t^{q-1}\to0\), so they obstruct exact Einstein gluing but not \(C^0\) Ricci pinching;
- the simple gluing in Biquard Remark 4.3 is insufficient for our purpose.

The executable ledger `workspace/scripts/step58_biquard_ct_collapse_ledger.py` saves this in `workspace/data/step58_biquard_ct_collapse_ledger.json`. Sample exponents:

| \(t\) | worst operator residual after first obstruction killed |
|---:|---:|
| \(10^{-1}\) | \(3.16\cdot10^{-1}\) |
| \(10^{-2}\) | \(10^{-1}\) |
| \(10^{-4}\) | \(10^{-2}\) |
| \(10^{-8}\) | \(10^{-4}\) |

## 3. Minimal genuinely mixed pattern check

The same ledger includes two minimal mixed checks:

1. positive mirror \((S^2\times S^2)/\mathbb Z_2\), one reversed node among four;
2. negative mirror \((\Sigma_2\times\Sigma_2)/\langle\iota\times\iota\rangle\), one reversed node among thirty-six.

At every node in both mirrors,
\[
R_+=R_- = \operatorname{diag}(\Lambda,0,0),
\]
with \(\Lambda=+1\) in the positive schematic and \(\Lambda=-1\) in the negative schematic. Choosing \(\zeta=(0,1,0)\) kills the correct vector condition for both chiralities:
\[
R_+\zeta=0,\qquad R_-\zeta=0.
\]
Choosing \(\zeta=(1,0,0)\) gives \(R_\pm\zeta=(\Lambda,0,0)\ne0\), showing that this is the actual vector condition, not determinant shorthand.

For near-pinched input metrics this is enough: because the chosen \(\zeta\) kills every first obstruction and Biquard's Lemma 4.2 gives an unprojected raw Ricci estimate for the glued approximate metric, a finite disjoint mixed pattern has
\[
\|\operatorname{Ric}_{g_t}-\Lambda g_t\|_{op,g_t}=O(t^{1/2})\to0.
\]
No global inverse, transversality, AH boundary deformation, or small eigenvalue statement is needed for this weaker approximate construction. Those belong to the exact Einstein gluing problem, not to constructing Yau--26 input metrics.

Remaining limitations are equally important: this still does **not** prove that any mixed filling lacks some distant Einstein metric, and it does **not** prove H4-dual necessity for arbitrary \(C^0\)-Ricci-pinched degenerations.

## 4. Cheeger--Tian is the exact Einstein theorem; Step 11 blocks the \(C^0\)-Ricci analogue

I attempted to retrieve the original Cheeger--Tian JAMS PDF. AMS returned 403 and several public URL guesses failed; the final knowledge request also misfired. I therefore do **not** claim to have read the original CT paper in this step.

The theorem statement was read from a secondary paper (`Knowledge/objects/papers/1707.05511-ε-regularity-for-shrinking-Ricci-solitons-and-Ricci-flows--.../object.md`, lines 29--36): there are universal \(\epsilon,C\) such that if \((M,g,p)\) is a four-dimensional Einstein manifold with \(\operatorname{Ric}=\lambda g\), \(|\lambda|\le3\), and
\[
\int_{B_r(p)} |\operatorname{Rm}|^2\le\epsilon,
\qquad r\le1,
\]
then
\[
\sup_{B_{r/2}(p)} |\operatorname{Rm}|\le C r^{-2},
\]
with no volume assumption.

This is exactly the theorem the collapse branch would like to transfer to Yau--26, but Step 11 structurally falsifies the transfer. On fixed \(S^2\times S^2\), the opposite-warping spike has
\[
\|\operatorname{Ric}_{g_\Lambda}-g_\Lambda\|_{op}=O(\Lambda^{-2/3})\to0,
\]
local added Hessian/curvature \(L^2\) energy \(O(\Lambda^{-4/3})\to0\), but
\[
|\operatorname{Rm}_{g_\Lambda}|(p)\gtrsim \Lambda^{1/3}\to\infty.
\]
The saved data confirms slopes close to \(-2/3\) for the Ricci defect and \(-4/3\) for the local Hessian energy; at \(\Lambda=500\), the recorded defect is about \(0.0322\), the center curvature lower bound about \(24.45\), and the Hessian-energy proxy about \(0.00489\).

The mechanism is not a technical failure of proof. Einstein metrics satisfy an elliptic curvature system whose source does not contain arbitrary \(\nabla^2\operatorname{Ric}\); mere \(L^\infty\) Ricci pinching leaves the trace-free Hessian channel free. Step 11 was engineered exactly in that channel: opposite warping cancels Hessian in Ricci but not in Riemann.

Conclusion for allocation: do not spend work trying to recover collapse-tolerant pointwise \(\epsilon\)-regularity from \(C^0\) Ricci pinching. If regularity is used, it must be weaker (finite \(L^p\)/BMO, harmonic-radius on controlled covers, smoothing with changed metric, or distributional/test-field pairings).

## 5. Collapse Chern--Weil pinning: no counting slack

For any oriented four-metric, write \(E=\operatorname{Ric}^0\) and \(A_\pm=\int |W^\pm|^2\). The identities are
\[
A_+ + A_- + \int\left(\frac{s^2}{24}-\frac{|E|^2}{2}\right)=8\pi^2\chi,
\]
\[
A_+ - A_- = 12\pi^2\tau.
\]
Hence
\[
A_\pm =2\pi^2(2\chi\pm3\tau)
-\frac12\int\left(\frac{s^2}{24}-\frac{|E|^2}{2}\right).
\]
If \(\|\operatorname{Ric}-\sigma g\|_{op}\to0\) and \(\operatorname{Vol}\to0\), then the integral term is \(o(1)\). Thus both chiral Weyl energies are asymptotically pinned by topology:
\[
\int |W^\pm|^2 \to 2\pi^2(2\chi\pm3\tau).
\]

This is stronger route information than an ordinary energy bound. It explains why the toric/rod adversary survives energy counting. For \(M_k=\#_k(S^2\times S^2)\),
\[
\chi=2k+2,
\qquad \tau=0,
\]
so the total Weyl energy limit is
\[
8\pi^2\chi = 8\pi^2(2k+2).
\]
A rod model with \(m=2k+2\) rods each carrying approximately \(8\pi^2\) gives exactly the same total:
\[
(2k+2)\cdot 8\pi^2=8\pi^2(2k+2).
\]
There is no missing topological budget. A positive-collapse obstruction must find a **defect**: energy that collapse or transition regions are forced to lose to the lower-dimensional limit, nonmaximal nilpotent topology, bad collars, or some global closure condition, preventing delivery of the topologically required chiral energies.

## 6. Updated route consequences

1. **Mixed-bubble construction conditional is partially discharged.** The local raw Ricci estimate needed to build near-pinched input metrics is now directly anchored in Biquard §4. The remaining conditionality is not this local estimate, but the topology/smooth-type bookkeeping, finite disjoint chart compatibility, and above all the absence/presence of a far-away Einstein metric on the same smooth filling.

2. **The H4-dual necessity bridge remains theorem-level and high value.** If proved, it classifies noncollapsed positive counterexamples by forcing all bubble points into finite chiral degeneracy loci. This would be a theorem about arbitrary pinched degenerations, unlike the mixed-wall construction.

3. **Positive collapse should be attacked adversarially, not with symmetric examples.** Lens spaces and principal bundles with built-in symmetries only re-confirm exact/almost Killing fields. The useful action is to try globalizing the Step-29 local twist-spike/fast-fibre-variation mechanism into a closed collapsing near-pinched family; if it fails, the obstruction encountered may be the proof.

4. **Higher-dimensional refutation is not a near-term route.** The session already recorded that no closed \(n\ge5\) manifold is known here to admit no Einstein metric of any sign. A refutation in \(n\ge5\) would first require producing such a manifold, a major open prerequisite; higher dimensions should be approached from proof-side mechanisms unless a genuinely new non-Einstein source appears.

5. **A03 flow update is separate.** Peer #402 says the direct start has a per-datum tame hierarchy and asks peers to attack exact unweighted H2/Y/J6/Q inequalities. I did not audit those inequalities in this step. The negative cutoff-flow route remains conditional from A02's perspective.
