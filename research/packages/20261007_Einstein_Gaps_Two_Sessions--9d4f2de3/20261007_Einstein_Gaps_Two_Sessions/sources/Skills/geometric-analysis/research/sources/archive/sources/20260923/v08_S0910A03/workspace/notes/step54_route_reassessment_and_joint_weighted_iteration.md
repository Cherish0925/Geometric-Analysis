# Step 54: corrected route assessment and a joint weighted iteration for the transported cutoff

Session: S0910A03. Agent1 / Orchestrator. Phase: Explore.

## 0. Corrected status

Two conclusions from Step 53 are withdrawn.

1. The Ishida--LeBrun terminal mechanism has **not** been shown to lose family uniformity like \(A^{-1/2}\). The existing support construction keeps a volume-weighted family of eligible cores whose total volume is a fixed fraction of \(\operatorname{Vol}M\asymp A\). Hence
   \[
   \frac{1}{\operatorname{Vol}P}\int_M\mathfrak D
   \le C\frac{\delta^2A}{\alpha A}=C'\delta^2.
   \]
   One core has normalized mean defect \(O(\delta^2)\), independent of \(A\). Moreover the geography-uniform curvature-to-volume ratio allows a fixed small physical radius. The argument in A02 Step 52 chose \(r_*\asymp A^{1/4}\) without necessity and inferred a lower bound for the Sobolev--energy product from an upper bound on local energy, which is invalid. Even a sufficient estimate \(\delta<cA^{-1/2}\) would not upper-bound the optimal gap.

2. Step 53 Theorem 5.1 is **not proved**. Its frozen transport velocity uses the input metric \(U\), while the weighted parabolic gain belongs to the output metric \(V\). Interpolation from a bounded high-order ball gives only a one-half-Hölder dependence on the lower-order metric distance, not the Lipschitz estimate needed for Banach contraction.

The real state is therefore: a potentially family-uniform terminal obstruction conditional on a common-time exact flow, and an unresolved coupled start theorem.

## 1. Why the Step 53 frozen product map fails

The map used there was
\[
(U,\alpha)\longmapsto(V,\beta),
\]
with
\[
\partial_tV=(\alpha^2+\varepsilon)U^{-1}*\widetilde\nabla^2V+\cdots,
\qquad
\partial_t\beta=\alpha^2W(U)\cdot\widetilde\nabla\beta.
\]
For two inputs, the transport difference contains
\[
\alpha_2^2\bigl(W(U_1)-W(U_2)\bigr)\cdot\widetilde\nabla\beta_2
\sim \alpha_2^2\widetilde\nabla(U_1-U_2)\,\widetilde\nabla\beta_2.
\]
The contraction metric controls \(U_1-U_2\) only in \(H^r\). A uniform \(H^{r+2}\) ball gives
\[
\|U_1-U_2\|_{H^{r+1}}
\le C_R\|U_1-U_2\|_{H^r}^{1/2},
\]
so the transport output is at best one-half-Hölder in that distance. No choice of small time turns \(C\sqrt T\,d^{1/2}\) into \(qd\) uniformly as \(d\downarrow0\). The parabolic dissipation of the **output** difference \(V_1-V_2\) cannot absorb a derivative of the independent **input** difference \(U_1-U_2\). Thus the map in Step 53 is the wrong iteration architecture even if all individual equations are solvable.

## 2. A triangular output-velocity map

A better regularized iteration keeps Xu's frozen principal coefficient but lets the transported cutoff see the just-computed metric output:
\[
\Psi_\varepsilon:(U,\alpha)\longmapsto(V,\beta),
\]
where first \(V\) solves
\[
\partial_tV=(\alpha^2+\varepsilon)U^{-1}*\widetilde\nabla^2V
 +D(U,V)+B(U,\widetilde\nabla U)
 +\mathcal L_{\alpha^2W(U)}V-2\alpha^2V,
\tag{2.1}
\]
with the precise Xu/Yang fixed-background lower-order terms retained, and then \(\beta\) solves
\[
\partial_t\beta=\alpha^2W(V)\cdot\widetilde\nabla\beta,
\qquad \beta(0)=\chi.
\tag{2.2}
\]
At a fixed point \(U=V\), \(\alpha=\beta\), this is the desired transported-square system. The change from \(W(U)\) to \(W(V)\) does not alter the fixed points. It changes the difference estimate decisively: the dangerous derivative now falls on the parabolic output difference
\[
Z:=V_1-V_2,
\]
whose weighted dissipation is present in the same joint estimate.

A formulation closer to Xu's displayed equation may absorb \(\alpha^2\mathcal L_{W(U)}V\) into its principal and first-order coefficients; what matters for the following calculation is that the exact cross term
\[
2\operatorname{sym}(d\alpha^2\otimes W(U)^\flat)
\]
is retained and not hidden as a derivative-free term.

## 3. Candidate joint difference energy

Let
\[
Z=V_1-V_2,\qquad \omega=\beta_1-\beta_2,
\qquad d_U=U_1-U_2,\quad d_\alpha=\alpha_1-\alpha_2.
\]
At Sobolev order \(r>n/2+2\), the metric difference estimate has Xu's form, augmented by coefficient and Lie-cross terms:
\[
\frac d{dt}\|Z\|_{H^r}^2
+c\|\sqrt{\alpha_1^2+\varepsilon}\,\widetilde\nabla^{r+1}Z\|_2^2
\le C(\|Z\|_{H^r}^2+\|d_U\|_{H^r}^2+\|d_\alpha\|_{H^r}^2)
+\mathcal R_{12}.
\tag{3.1}
\]
The signed integration used for \(d(\alpha^2)\otimes W\) must give
\[
|\mathcal R_{12}|
\le \eta\|\sqrt{\alpha_1^2+\varepsilon}\,\widetilde\nabla^{r+1}Z\|_2^2
+C_\eta(\|Z\|_{H^r}^2+\|d_U\|_{H^r}^2+\|d_\alpha\|_{H^r}^2),
\tag{3.2}
\]
using \(d(\alpha^2)=2\alpha d\alpha\) and the square-difference factorization. This is a required lemma, not yet established by the old note.

The transport difference is
\[
\partial_t\omega
=\alpha_1^2W(V_1)\cdot\nabla\omega
+[\alpha_1^2W(V_1)-\alpha_2^2W(V_2)]\cdot\nabla\beta_2.
\tag{3.3}
\]
After the usual transport integration by parts and Moser commutator estimates, its top output-metric term is
\[
I_r=\int\nabla^r\omega\;\alpha_2^2\nabla^{r+1}Z\;\nabla\beta_2
\quad\text{(up to bounded contractions and lower terms)}.
\tag{3.4}
\]
Because \(\alpha_2^2\le |\alpha_2|\,|\alpha_2|\),
\[
|I_r|
\le C\|\alpha_2\nabla^{r+1}Z\|_2\|\omega\|_{H^r}
\le \eta\|\alpha_2\nabla^{r+1}Z\|_2^2+C_\eta\|\omega\|_{H^r}^2.
\tag{3.5}
\]
The key is to compare the \(\alpha_2\)-weighted derivative in (3.5) to the \(\alpha_1\)-weighted dissipation in (3.1). A direct comparison fails where \(\alpha_1\) is small but \(\alpha_2\) is not. Use instead the exact decomposition
\[
\alpha_2^2=\alpha_1\alpha_2+\alpha_2(\alpha_2-\alpha_1).
\tag{3.6}
\]
The first part is controlled by the \(\alpha_1\)-weighted dissipation, since \(|\alpha_2|\) is uniformly bounded. The second part retains an input cutoff difference and gives a term schematically
\[
|d_\alpha|\,|\alpha_2|\,|\nabla^{r+1}Z|\,|\nabla^r\omega|.
\tag{3.7}
\]
Without a weight or one more input derivative, (3.7) is not controlled uniformly as \(\varepsilon\to0\). This is the precise remaining mismatch.

## 4. Two ways to close the weight mismatch

### 4.1 Synchronized-coefficient iteration

The cleanest possibility is to remove \(\alpha\) as an independently frozen input. Given \(U\), solve jointly for \((V,\beta)\) with the coefficient in the metric principal part equal to the same output \(\beta^2\):
\[
\partial_tV=(\beta^2+\varepsilon)U^{-1}*\nabla^2V+\cdots,
\qquad
\partial_t\beta=\beta^2W(V)\cdot\nabla\beta.
\tag{4.1}
\]
For each frozen \(U\), this is already a coupled quasilinear parabolic--transport problem, but the metric and transport difference estimates now use exactly the same \(\beta_i\) weights. The dangerous term is absorbed into the dissipation of the same solution branch without comparing unrelated input weights. One then seeks a contraction only in the metric input \(U\). This replaces the false product Banach contraction by an inner coupled solve plus Xu's outer contraction.

The scientific issue is whether the inner solve can be obtained by a continuation/Galerkin argument from its joint energy, without reintroducing derivative loss. The principal metric equation is strictly parabolic for \(\varepsilon>0\), while the transport equation is symmetric hyperbolic. Standard mixed parabolic--hyperbolic theory should apply for fixed \(\varepsilon\); the substantive work is an \(\varepsilon\)-uniform joint estimate preserving the square weights.

### 4.2 An iteration norm carrying input dissipation

Alternatively define a complete space of trajectories with norm
\[
\|(U,\alpha)\|_{X_T}^2
=\sup_{t\le T}(\|U\|_{H^r}^2+\|\alpha\|_{H^r}^2)
+\int_0^T\|\alpha\nabla^{r+1}U\|_2^2dt,
\tag{4.2}
\]
and distance containing the analogous weighted derivative of input differences. Then the original frozen transport equation has the derivative information it actually uses. But weights differ between two trajectories, so the natural distance must be symmetrized, for example
\[
\int_0^T\bigl(\|\alpha_1\nabla^{r+1}d_U\|_2^2
+\|\alpha_2\nabla^{r+1}d_U\|_2^2\bigr)dt.
\tag{4.3}
\]
One must prove the output map contracts this full graph norm, including the weighted derivative part. Xu's Proposition 2.8 only contracts the lower Sobolev supremum norm; it does not supply this. This route is possible but technically heavier.

The synchronized-output approach in §4.1 has the better structural match: the same transported square produces both diffusion and transport velocity.

## 5. Exact analytic target for the next construction

A rigorous start theorem can be reduced to the following mixed-system lemma.

**Target lemma.** For smooth \(U\) in a uniformly positive bounded \(H^{s}\) ball and \(0<\varepsilon\le1\), solve the inner system
\[
\begin{cases}
\partial_tV=(\beta^2+\varepsilon)U^{-1}*\widetilde\nabla^2V
 +\mathcal F(U,\widetilde\nabla U,V,\beta,\widetilde\nabla\beta),\\
\partial_t\beta=\beta^2W(V)\cdot\widetilde\nabla\beta,
\end{cases}
\tag{5.1}
\]
where \(\mathcal F\) is the exact normalized DeTurck expression and includes the Lie cross term. Establish on a time depending on the smooth datum but not \(\varepsilon\):
\[
\sup_{t\le T}(\|V\|_{H^s}^2+\|\beta\|_{H^s}^2)
+c\int_0^T\|\beta\widetilde\nabla^{s+1}V\|_2^2dt\le C,
\tag{5.2}
\]
and, for two frozen metrics \(U_1,U_2\),
\[
\sup_{t\le T}(\|V_1-V_2\|_{H^r}^2+\|\beta_1-\beta_2\|_{H^r}^2)
\le CT\sup_{t\le T}\|U_1-U_2\|_{H^r}^2,
\tag{5.3}
\]
with \(r<s\) and constants independent of \(\varepsilon\). In (5.3), every \(\nabla^{r+1}(V_1-V_2)\) from the transport equation must be absorbed by the metric difference dissipation with its own output weight; no interpolation of an input difference may be used.

If (5.1)--(5.3) hold, Xu's outer contraction in \(U\), followed by \(\varepsilon\to0\), gives the exact fixed-cutoff geometric flow. If the joint estimate cannot control the differing solution weights in the difference equation, that failure precisely identifies the extra symmetrizer required from Yang's smooth-tame construction.

## 6. Correct family-uniform normalization in the IL route

Let \(P=\bigsqcup_\alpha\Omega_\alpha\) be the retained inner cores. The support construction gives
\[
\operatorname{Vol}(P)\ge\alpha_0\operatorname{Vol}(M),
\qquad \operatorname{Vol}(M)\asymp A.
\tag{6.1}
\]
At the common observation time, conditional on exact-flow estimates,
\[
\int_M\mathfrak D\le119Q(T)\le C\delta^2\operatorname{Vol}(M).
\tag{6.2}
\]
Therefore
\[
\frac1{\operatorname{Vol}(P)}\int_P\mathfrak D
\le C\delta^2,
\tag{6.3}
\]
and volume-weighted averaging picks one core with normalized defect mean \(O(\delta^2)\), uniformly in \(A\). The equivalent exponential-pullback averaging in A01 Step 44 has the same normalization.

At the initial scale, a volume-average maximal function with fixed threshold \(\kappa^2\) produces a good set occupying a fixed volume fraction because
\[
\frac{\int|\operatorname{Rm}|^2}{\operatorname{Vol}}
\le\Lambda
\tag{6.4}
\]
is geography-uniform. Choose a small fixed \(r\), not \(A^{1/4}\). On a good support,
\[
K_{2,\alpha}(0)\le(1+\kappa^2)\operatorname{Vol}(B_{Cr}),
\quad
\mathcal S_\alpha\le Cr^2\operatorname{Vol}(B_{Cr})^{-1/2},
\tag{6.5}
\]
so
\[
\gamma_\alpha=\mathcal S_\alpha K_{2,\alpha}(0)^{1/2}
\le Cr^2\sqrt{1+\kappa^2}.
\tag{6.6}
\]
This is an upper bound. A02 Step 52 inserted the same upper local-energy estimate into a claimed lower bound for \(\gamma\), which is not valid. The common-time question is instead whether (6.5)--(6.6), moving Sobolev comparison, and the corrected forced/shifted curvature energies persist on one exact flow.

## 7. Route comparison against the full Yau 26 goal

### 7.1 Restricted negative IL route

Scientific value: it is the only route with a detailed topology-to-local-spectral contradiction and a plausible family-uniform normalization. Its reusable content is stronger than the special topology: volume-weighted support selection plus collapse-resistant smoothing can convert any global nonnegative defect density controlled by \(Q\) into a forbidden local germ. Its remaining hard point is precise and analytic: the exact transported-coefficient start and then a connected first-exit verification.

Limitation: even complete, it only excludes a specified four-dimensional negative no-Einstein geography from arbitrarily tight pinching. It does not decide the positive normalized alternative, arbitrary 4-topology, or higher dimensions.

Judgment: continue enough to settle whether the coupled start mechanism truly works, because that determines the validity of a broadly reusable smoothing method. Do not spend another long sequence merely reassembling the terminal IL theorem until the joint inner estimate (5.2)--(5.3) is proved.

### 7.2 Positive four-dimensional orbifold/gluing route

The mixed \((S^2\times S^2)/\mathbb Z_2\) fillings are a sharper direct test of the full positive branch. Kernel-directed Eguchi--Hanson insertion can make the operator-norm Ricci defect tend to zero, while ordinary Seiberg--Witten obstructions are unavailable on the resulting positive-scalar-curvature topologies. Thus \(P_4^+\) would force Einstein metrics on explicit mixed smooth manifolds. This is potentially decisive, but presently reduces the problem to their exact smooth types and Einstein existence/nonexistence. Higher gluing obstructions that vanish in \(C^0\) operator norm do not by themselves yield nonexistence.

Judgment: high value, but it needs topology classification and a sign-compatible Einstein obstruction or construction, not more local residual estimates.

### 7.3 Negative Q-Gorenstein smoothing route

For negative general-type product quotients, global Q-Gorenstein smoothing plus ampleness and Aubin--Yau supplies Einstein existence. This helps classify apparent counterexample candidates and prevents false negative routes. It does not furnish dimension-only forcing constants and does not address mixed positive fillings.

Judgment: useful control/comparison line; not currently the strongest direct route to the full proposition.

### 7.4 Higher dimensions and local-only obstructions

No existing local curvature-density obstruction has been identified that encodes nonexistence of *every* Einstein metric on the underlying manifold without global topology. Any full disproof must exhibit, for at least one normalized sign, a family of no-Einstein manifolds with uniform near-Einstein metrics. Any full proof must convert the input pinching into a global existence theorem despite collapse and topology. The current smoothing mechanism attacks only the analytic conversion from global defect to a local germ; it cannot by itself supply the global Einstein metric.

The best near-term research portfolio is therefore two-pronged:

1. resolve the joint transported-square start lemma, because it determines whether Module S is real and reusable;
2. independently classify the mixed positive fillings and their Einstein status, because they are concrete near-pinched candidates tied directly to the original quantifiers.

## 8. Immediate mathematical handoff

The next constructor should work on the exact inner mixed system (5.1), not the invalid frozen product map. Write the exact fixed-background equations, derive a **single joint energy** for \((V,\beta)\) and for two solutions, and check that every top metric derivative in the transport equation carries the same output \(\beta^2\) as the metric dissipation. Track changing weights explicitly. If a term cannot be absorbed, record its exact tensor form and determine whether a symmetrizer, a good-unknown transformation, or Yang's original \((\widehat g,\varphi)\) variable removes it.

In parallel, the prior Step 53 file should carry a supersession notice for Theorem 5.1 and §6. Peer message #386 communicates both corrections.
## 9. TTCS refinement of the synchronized-output idea

The TTCS generator and verifier agreed on two substantial points and disagreed on one load-bearing estimate.

### 9.1 Single-solution joint energy

For the inner mixed system with frozen metric input \(U\), output metric \(V\), and output cutoff \(\beta\), both readings support an \(\varepsilon\)-uniform estimate at high order \(s\):
\[
\frac d{dt}\bigl(\|V\|_{H^s}^2+\|\beta\|_{H^s}^2\bigr)
+c\sum_{k\le s}\int(\beta^2+\varepsilon)|D^{k+1}V|^2
\le C_R\bigl(1+\|V\|_{H^s}^2+\|\beta\|_{H^s}^2\bigr).
\tag{9.1}
\]
The two cross-couplings close for one solution: top \(D^{s+1}\beta\) in the metric Lie term is integrated onto \(V\) and gains a factor \(\beta\); top \(D^{s+1}V\) in the transport commutator already carries \(\beta^2\). This is a meaningful advance beyond the invalid Step 53 product map.

### 9.2 Difference estimate must be graded two orders lower

The verifier found that the apparent \(\beta_1\)-versus-\(\beta_2\) mismatch can be avoided by organizing **both** difference equations relative to the same branch. With
\[
Z=V_1-V_2,\qquad \omega=\beta_1-\beta_2,
\]
write the metric principal difference as
\[
(\beta_1^2+\varepsilon)A_1D^2V_1
-(\beta_2^2+\varepsilon)A_2D^2V_2
=(\beta_2^2+\varepsilon)A_2D^2Z
+(\beta_1^2-\beta_2^2)A_1D^2V_1
+(\beta_2^2+\varepsilon)(A_1-A_2)D^2V_1.
\tag{9.2}
\]
The transport velocity difference is similarly
\[
\beta_1^2W(V_1)-\beta_2^2W(V_2)
=(\beta_1^2-\beta_2^2)W(V_1)
+\beta_2^2\bigl(W(V_1)-W(V_2)\bigr).
\tag{9.3}
\]
Thus the top transport term carries \(\beta_2^2D^{r+1}Z\), precisely matching the \((\beta_2^2+\varepsilon)\)-weighted metric dissipation. The Lie-coefficient identity
\[
d(\beta_1^2)-d(\beta_2^2)=2\beta_2d\omega+2\omega d\beta_1
\tag{9.4}
\]
provides the same branch weight after integration by parts.

Crucially, take the contraction order at least two derivatives below the invariant-ball order:
\[
r\le s-2,\qquad r>n/2+2.
\tag{9.5}
\]
Then the principal-coefficient difference is bounded using the **individual** unweighted \(H^s\) ball, not interpolation of a difference:
\[
\|D^r[(\beta_1^2-\beta_2^2)A_1D^2V_1]\|_2
\le C_R\|\omega\|_{H^r},
\tag{9.6}
\]
\[
\|D^r[(\beta_2^2+\varepsilon)(A_1-A_2)D^2V_1]\|_2
\le C_R\|U_1-U_2\|_{H^r}.
\tag{9.7}
\]
This directly avoids the half-Hölder interpolation error. It suggests the closed estimate
\[
\frac d{dt}(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2)
+c\int(\beta_2^2+\varepsilon)|D^{r+1}Z|^2
\le C_R\bigl(\|Z\|_{H^r}^2+\|\omega\|_{H^r}^2+\|U_1-U_2\|_{H^r}^2\bigr).
\tag{9.8}
\]

### 9.3 Remaining load-bearing check

The generator integration cautioned that an arithmetic-mean symmetrization can leave
\[
\mathcal K_r=\sum_{|I|=r}\int D^IZ\,D^I[(\beta_1^2-\beta_2^2)A D^2V_*],
\tag{9.9}
\]
and that at only one derivative of grading margin this is uncontrolled uniformly in \(\varepsilon\). The verifier's one-sided, two-order-lower decomposition (9.2)--(9.7) is the proposed resolution. It must be checked against the **exact** fixed-background DeTurck expansion, rather than a schematic \(\mathcal F\), to ensure:

1. every \(D^{r+1}\omega\) metric term comes through \(d(\beta^2)\) and hence admits (9.4);
2. every \(D^{r+1}(U_1-U_2)\) term carries \(\beta_2\) or \(\beta_2^2\), so integration by parts is compatible with the same weighted dissipation;
3. no unweighted source \(D^rZ*G*D^{r+1}(U_1-U_2)\) survives;
4. the fixed-\(\varepsilon\) inner mixed system can be constructed with (9.1), and compactness passes \(\varepsilon\to0\) at all required orders.

Accordingly, the synchronized-output architecture is now more promising than §4 initially judged, but no start theorem is promoted yet. The exact next object is the tensor-level proof of (9.8) with the grading (9.5).

## 10. Independent positive-existence advance from A01

A01 Step 51 proves a complete Einstein-existence result for one concrete negative product-quotient topology: the minimal resolution \(S\) of the BCGP \(K^2=2\), \(G=\mathbb Z_4^2\), six-\(A_1\) canonical model carries a negative Einstein metric.

The chain is:
\[
T_X^0\cong(\pi_*T_Y)^G,
\qquad H^2(X,T_X^0)=H^2(Y,T_Y)^G=0,
\tag{10.1}
\]
where the final vanishing follows by equivariant Serre duality, Künneth, and an explicit character computation. Lee--Park then globalizes simultaneous local \(A_1\) smoothings. The smooth fiber has ample canonical bundle and hence a negative Kähler--Einstein metric by Aubin--Yau. ADE simultaneous resolution after base change and Ehresmann identify the minimal resolution smoothly with the general fiber.

Source note: `Sessions/S0910A01/workspace/notes/step51_reflexive_bridge_einstein_existence_proof.md`. This result is important route control: a serious near-Einstein product-quotient candidate actually admits an unrelated exact Einstein metric. It validates the original quantifier warning that local gluing behavior cannot decide the output-metric question. The reflexive-extension method may classify further negative candidates, but it does not address the mixed positive \((S^2\times S^2)/\mathbb Z_2\) fillings or yield dimension-only forcing by itself.
