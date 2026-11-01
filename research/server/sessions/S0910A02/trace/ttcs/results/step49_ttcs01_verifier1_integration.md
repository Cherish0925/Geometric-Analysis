# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 49,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step49_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step49_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 49 correction for the Yau-26 positive noncollapsed route. Read the Step 49 note and supporting data/sources. Check: (i) whether the scaling from MV/Ozuch refined estimates really shows that after the first obstruction term t*lambda*o is killed, the glued approximate metrics have ||Ric-Lambda g||_op = O(t^{1/2}) on the four-dimensional EH/Calabi replacement, while second/higher obstruction residuals are invisible to C^0 operator pinching; (ii) whether the H4_dual compactness obstruction must be formulated as the normalized boundary flux B/t_i^2 with quantitative two-scale matching, not the unnormalized B; (iii) whether the finite product-quotient orientation enumeration and known-Einstein/mixed-row status are stated with correct caveats. Identify any mathematical errors, hidden assumptions, or needed repairs that would change the route allocation. Do not invent external facts; if a needed source is absent, say exactly what source should be retrieved.

## Integrated Scientific Memo

## Verification of Step 49 correction

Step 49’s main scientific correction is essentially right, but it needs several caveats sharpened. The key conclusions that should drive route allocation are:

1. **For explicit refined EH/Calabi replacements, after the vector first obstruction is killed, the Ricci endomorphism defect is small in \(C^0\): at worst \(O(t^{1/2})\) in the MV notation, or \(O(t^{1/2-\beta/4})\) if one quotes Ozuch’s weighted estimate directly.** Thus second and higher Ozuch obstruction coefficients do not obstruct Yau–26-style operator pinching; they obstruct exact Einstein gluing.

2. **For compactness/necessity, the H4-dual boundary functional must be normalized by the quadratic signal size.** The unnormalized flux tends to zero for the trivial reason \(h_i\to0\). The hard lemma is a quantitative two-scale expansion/matching statement, not just an integration-by-parts identity.

3. **The product-quotient enumeration is arithmetically plausible/correct in the \(\mathbb Z_2\) case, but the endpoint Del Pezzo identification and all mixed smooth types still require explicit topology.** The mixed rows are near-pinched input families, not Yau–26 counterexamples unless one proves the actual smooth manifolds admit no Einstein metric of any sign.

---

### 1. Operator-norm scaling: mathematically correct, with source/citation repairs

The scaling argument in Step 49 is correct for the refined approximate metric.

On the bubble/core region the glued metric has the form, in MV notation,
\[
g_t \simeq t\, g_{\mathrm{cal}},
\]
and the refined estimate is
\[
\left|
\nabla^k\bigl(\operatorname{Ric}_{g_t}-\Lambda g_t
-t\lambda\chi_t o\bigr)
\right|_{g_{\mathrm{cal}}}
\le C_k t^2 \rho^{2-k}.
\]
For a \((0,2)\)-tensor \(T\), the Ricci pinching norm is an endomorphism norm:
\[
\|g_t^{-1}T\| \sim t^{-1}\|g_{\mathrm{cal}}^{-1}T\|.
\]
Therefore, after subtracting/killing the first obstruction term,
\[
\left\|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)\right\|
\le C\,t\rho^2 .
\]
Since the refined gluing region has \(\rho\le 2t^{-1/4}\), this gives
\[
\sup \|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)\|
\le C t^{1/2}.
\]
The maximum occurs in the damage/transition annulus \(\rho\asymp t^{-1/4}\); on the fixed EH core it is only \(O(t)\). On the exterior the original orbifold metric is Einstein, so away from cutoffs there is no contribution.

A nonzero first obstruction term \(t\lambda o\) is different:
\[
\|g_t^{-1}(t\lambda o)\| \sim |\lambda o|_{g_{\mathrm{cal}}}
\]
on the EH core, hence order one if the vector coefficient is nonzero. This is exactly the order visible to Yau–26’s \(C^0\) operator pinching.

By contrast, an obstruction-mode residual of order \(t^q o\), \(q>1\), has core endomorphism size
\[
t^{-1}t^q= t^{q-1}\to0.
\]
Thus a second obstruction \(t^2\mu o\) contributes only \(O(t)\) in the pinching norm. Higher Ozuch obstructions remain essential for exact Einstein desingularization, but they are invisible to the limiting \(C^0\) Ricci endomorphism condition.

A useful point Step 49 should state explicitly: the refined correction \(h\) is what cancels the apparent fatal defect of gluing a Ricci-flat bubble into a positive-Einstein orbifold. Naively, on \(t g_{\mathrm{EH}}\),
\[
\operatorname{Ric}(t g_{\mathrm{EH}})-\Lambda t g_{\mathrm{EH}}
= -\Lambda t g_{\mathrm{EH}},
\]
whose endomorphism norm is \(O(1)\). But the refined metric is \(t(g_{\mathrm{EH}}+t h)\), with
\[
d\operatorname{Ric}_{g_{\mathrm{EH}}}(h)=\Lambda g_{\mathrm{EH}}+\sum_k\lambda_k o_k.
\]
Hence
\[
\operatorname{Ric}\bigl(t(g_{\mathrm{EH}}+t h)\bigr)-\Lambda\,t(g_{\mathrm{EH}}+t h)
=
t\sum_k\lambda_k o_k+O(t^2\rho^2),
\]
so if the first obstruction vector vanishes the remaining defect is small. This cancellation is the real mechanism behind the near-pinched construction.

#### Source precision

There is one citation caveat. MV’s displayed Lemma 4.2 in the supplied source is for the Calabi metric in complex dimension \(n\ge3\), where the obstruction space is one-dimensional. The four-dimensional \(A_1\)/Eguchi–Hanson case has three EH deformation modes and rotational parameters. The scale structure is the same, but the four-dimensional vector statement should be sourced from Ozuch/Biquard rather than MV alone.

The supplied Ozuch excerpts do give the correct EH obstruction structure:
\[
\lambda_k(\zeta^\pm)
=
c\left\langle \mathbf R^\pm(H_2)\zeta^\pm,\zeta_{(k)}^\pm\right\rangle
\]
and the obstruction equation for exact Einstein desingularization:
\[
t_j\lambda_k^j+t_j^2\mu_k^j=O(t_{\max}^{5/2}).
\]
Ozuch Proposition 2.19 gives a weighted estimate
\[
\left\|\pi_{\tilde{\mathbf O}^{\perp}}\Phi(g^A)\right\|
\le C|\zeta|^{3/2-\beta/4}.
\]
Converting to \(C^0\) operator norm by the \(t^{-1}\) scale factor gives an exponent
\[
O(t^{1/2-\beta/4})
\]
rather than the clean \(O(t^{1/2})\), if quoting Ozuch directly. MV gives the clean model exponent. A rigorously sourced four-dimensional statement should retrieve Biquard 2013, *Désingularisation de métriques d’Einstein I*, especially the refined EH construction and Section 14 estimates, or the corresponding full four-dimensional estimate in Ozuch’s earlier work.

This does not change the scientific conclusion: once the vector first obstruction is killed, the explicit approximate metrics are \(C^0\)-Ricci-pinched.

#### “Complete local condition” caveat

Step 49’s phrase that \(R_\varepsilon(p)\zeta=0\) is the “complete local condition” is too strong unless qualified. It is complete for the **explicit first-refined approximate gluing construction**. Its necessity for every possible \(C^0\)-pinched EH degeneration still depends on the normalized H4-dual compactness lemma discussed below.

---

### 2. H4-dual flux: Step 49’s normalization correction is necessary

Step 49 is correct that the compactness obstruction must be formulated using the normalized boundary flux, not the raw \(\mathcal B_k\).

Let \(\epsilon_i\) be the EH length scale and set
\[
\tilde g_i=\epsilon_i^{-2}g_i=g_{\mathrm{EH}}+h_i .
\]
In the bubble frame, the ambient orbifold expansion contributes
\[
h_i\sim \epsilon_i^2 H_2
\]
on fixed large EH annuli. The Wronskian/boundary functional is linear in \(h_i\):
\[
\mathcal B_k(R,i)
=
\frac12\int_{\{\rho=R\}}
\left(
\langle\nabla_\nu h_i,o_k\rangle
-\langle h_i,\nabla_\nu o_k\rangle
\right)d\sigma .
\]
Since \(H_2=O(R^2)\), \(\nabla H_2=O(R)\), \(o_k=O(R^{-4})\), \(\nabla o_k=O(R^{-5})\), and \(d\sigma=O(R^3)\), the signal is of size
\[
\mathcal B_k(R,i)=O(\epsilon_i^2).
\]
Thus the meaningful quantity is
\[
\epsilon_i^{-2}\mathcal B_k(R,i).
\]
Without this normalization, \(h_i\to0\) gives \(\mathcal B_k(R,i)\to0\) for every fixed \(R\), which contains no curvature information. This is exactly the flaw in the Step 48 unnormalized argument.

The defect estimate also scales as Step 49 says. If
\[
\|\operatorname{Ric}_{g_i}-\Lambda g_i\|_{\mathrm{op},g_i}\le \delta_i\to0,
\]
then in the rescaled bubble metric
\[
\left|
\operatorname{Ric}_{\tilde g_i}-\Lambda\epsilon_i^2\tilde g_i
\right|_{\tilde g_i}
\le \epsilon_i^2\delta_i.
\]
Pairing against \(o_k\sim \rho^{-4}\) over \(\rho\le R\) gives
\[
O(\epsilon_i^2\delta_i(1+\log R)).
\]
After dividing by \(\epsilon_i^2\), the relative error is
\[
O(\delta_i(1+\log R)),
\]
which vanishes for fixed \(R\), then one can attempt \(R\to\infty\).

Also correct: the cutoff commutator is not discardable after normalization. For \(h_i\sim \epsilon_i^2 R^2\) on \(\rho\sim R\), the commutator/Wronskian contribution is also \(O(\epsilon_i^2)\), hence order one after division by \(\epsilon_i^2\). It must be included in the limiting flux calculation.

The unresolved hard analytic object is therefore:

\[
\epsilon_i^{-2}h_i \longrightarrow H_2
\]
with enough \(C^1\) control on fixed large bubble annuli, in compatible gauges, so that
\[
\lim_{R\to\infty}\lim_{i\to\infty}
\epsilon_i^{-2}\mathcal B_k(R,i)
=
c\left\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\right\rangle .
\]
Cheeger–Naber-type \(C^{1,\alpha}_{\mathrm{loc}}\) convergence to EH gives only \(h_i=o(1)\), not the \(\epsilon_i^2H_2\)-scale expansion. Ozuch’s exact-Einstein degeneration theory supplies such weighted matching in the Einstein setting; for merely \(C^0\)-Ricci-pinched sequences this remains unproved in the supplied sources.

A notation repair is needed: Step 49 uses \(t\) as the metric scale in the gluing estimate, but the H4 discussion sometimes uses \(t_i^2\) as the signal size. The clean convention is:
\[
\text{length scale } \epsilon,\qquad \text{metric scale } t=\epsilon^2.
\]
Then the ambient quadratic signal in the bubble frame is \(tH_2=\epsilon^2H_2\), and the normalized flux is \(t^{-1}\mathcal B\), equivalently \(\epsilon^{-2}\mathcal B\).

---

### 3. Product quotient orientation enumeration: mostly correct, but topology caveats matter

#### Diagonal \(\mathbb Z_2\) quotient

The arithmetic in Step 49 and the JSON for
\[
(S^2\times S^2)/\mathbb Z_2
\]
with the diagonal half-turn is correct.

There are four fixed points, each locally \(A_1=\mathbb C^2/\{\pm1\}\). Resolving four \(A_1\) points gives
\[
\chi=8.
\]
If \(r\) of the four EH insertions are reversed, and the convention is that compatible insertions contribute negative exceptional classes while reversed insertions contribute positive classes, then
\[
(b_+,b_-)=(1+r,5-r),\qquad \tau=2r-4.
\]
Thus the five rows are:
\[
r=0:(1,5),\quad
r=1:(2,4),\quad
r=2:(3,3),\quad
r=3:(4,2),\quad
r=4:(5,1).
\]

The caveats are essential:

- \(r=0\) is the all-compatible/crepant side and is expected to have the degree-4 Del Pezzo diffeotype \(\mathbb{CP}^2\#5\overline{\mathbb{CP}}^2\). Such a smooth manifold admits positive Einstein metrics. However, the supplied sources do not themselves perform the quotient-resolution topology computation. One should not claim the minimal resolution’s particular weak Del Pezzo complex structure is Kähler–Einstein; the Yau–26-relevant statement is only that the **smooth diffeotype** carries some positive Einstein metric.

- \(r=4\) is harmless for Yau–26 as the orientation reversal of the same smooth unoriented Einstein-existence class.

- \(r=1,2,3\) are mixed-chirality targets. No supplied source proves they admit Einstein metrics, and no supplied source proves they do not. They are therefore unresolved stress targets, not counterexamples.

- For \(r=2\), \((b_+,b_-)=(3,3)\) and \(\tau=0\). It is not yet proved that the intersection form is even/spin, so it is not yet proved to be \(3H\). It could be odd \(I_{3,3}\). Even if Freedman gives a homeomorphism type after parity is settled, that is not a smooth diffeomorphism classification.

- For \(r=1,3\), even unimodular intersection forms are impossible because the signature is \(\mp2\), so the form is odd; but exact smooth type still remains to be computed.

The notation \(M_{\varepsilon,t}\) should be avoided or clarified: for a fixed orientation assignment and attaching data, varying \(t\) gives metrics on one fixed smooth manifold, not a topology varying with \(t\).

#### Diagonal \(V_4\) product quotient

The formula recorded in Step 49,
\[
(b_+,b_-)=(1+r,7-r),\qquad \chi=10,
\]
for six \(A_1\) points is arithmetically consistent: resolving six \(A_1\) singularities adds six exceptional classes to the quotient’s two invariant classes. The balanced row \(r=3\) has \((4,4)\), conditionally \(4H\) only if evenness/spin and smooth type are proved.

But this \(V_4\) row remains more weakly sourced than the \(\mathbb Z_2\) row. Step 49 correctly says the group-action/smooth-type details need independent validation. Also, the LeBrun–Ozuch remark about cyclic quotients with \(k\ne2,4\) concerns cyclic \(\mathbb Z_k\) diagonal rotations, not the Klein four \(V_4\). The \(V_4\) enumeration is Step 49’s own finite group computation, not directly that cited cyclic statement.

#### Product graph-action ADE finiteness

The endpoint-weight argument is correct within its stated scope. For a cyclic stabilizer of order \(m\), the two endpoint choices give weights
\[
(1,a),\qquad (1,-a).
\]
Requiring both to be \(SU(2)\)/ADE imposes
\[
1+a\equiv0\pmod m,\qquad 1-a\equiv0\pmod m,
\]
hence \(m\mid2\). Therefore, among orientation-preserving graph actions with injective projections, the only all-\(A_1\)/ADE possibilities are \(C_2\) and \(D_2=V_4\). Step 49 correctly excludes factor-swap subgroups and other non-graph actions from this conclusion.

---

### 4. Consequence for route allocation

The Step 49 route correction is scientifically justified.

The positive noncollapsed product-quotient wall is not repaired by second or higher Ozuch obstructions. Once at each \(A_1\) point one chooses an EH direction
\[
\zeta_j\in\ker R_{\varepsilon_j}(p_j),
\]
the explicit refined approximate metrics already satisfy
\[
\|\operatorname{Ric}_{g_t}-\Lambda g_t\|_{\mathrm{op},g_t}\to0
\]
on the corresponding fixed smooth desingularization. At the bi-Kähler product quotient,
\[
R_+=R_-=\operatorname{diag}(\Lambda,0,0),
\]
so both chiralities have a two-dimensional kernel. Therefore every orientation assignment has local directions killing the vector first obstruction. Step 48’s observation that the second obstruction also vanishes at the rank-one locus is mathematically compatible, but it is not load-bearing for Yau–26 pinching.

What remains for a Yau–26 counterexample from this route is not higher-order exact gluing; it is:

1. identify the exact smooth diffeomorphism types of the mixed resolutions;
2. prove at least one such smooth manifold admits no Einstein metric of any sign.

No supplied material establishes either.

Conversely, the compactness/obstruction theorem
\[
\text{\(C^0\)-Ricci-pinched EH bubble}
\Longrightarrow
R_\varepsilon(p)\zeta=0
\]
is not yet proved. Its bottleneck is precisely the normalized two-scale flux lemma.

---

### 5. Needed source retrievals / repairs

To make Step 49 independently robust:

1. **Retrieve correct four-dimensional refined EH estimate.**  
   MV supplies the right scale but in complex dimension \(n\ge3\). Need Biquard, *Désingularisation de métriques d’Einstein I*, Invent. Math. 192 (2013), especially the refined EH construction and Section 14 estimates, or the corresponding full Ozuch local estimate.

2. **Retrieve exact weighted matching sources for the compactness flux lemma.**  
   Need Ozuch, *Noncollapsed degeneration of Einstein 4-manifolds I/II* and/or Ozuch thesis passages proving weighted Hölder approximation for exact Einstein degenerations, to isolate which parts use \(\Phi=0\) and what must be replaced under only \(C^0\)-Ricci pinching.

3. **Compute topology of mixed product resolutions.**  
   Need an explicit equivariant/toric/Kirby calculation for the diagonal \(\mathbb Z_2\) and \(V_4\) mixed resolutions: fundamental group after filling, parity/spin, intersection form, and smooth diffeomorphism type.

4. **Endpoint Del Pezzo identification should be sourced directly.**  
   The fact Del Pezzo diffeotypes admit positive Einstein metrics is supported in the supplied LeBrun–Ozuch source, but the identification of the all-compatible quotient resolution with the appropriate Del Pezzo diffeotype still needs a direct quotient-resolution computation.

5. **Einstein nonexistence/existence for mixed rows remains open.**  
   Need actual nonexistence obstructions or constructions for the specific smooth manifolds produced. Without this, Step 49 produces near-pinched families but not a Yau–26 refutation.