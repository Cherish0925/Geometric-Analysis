# TTCS Independent Branch Record

```json
{
  "step_id": 49,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step49_qg_smoothing_einstein_existence_mechanism.md",
    "Sessions/S0910A01/workspace/scripts/step49_tangent_euler_and_qg_obstruction.py"
  ]
}
```

## Task

Verify the following chain of reasoning about Einstein metric existence on product-quotient surface resolutions, checking each link for mathematical correctness:

1. HYPERKÄHLER IDENTIFICATION: For the A_1 singularity {uv-w^2=0}, the hyperkähler family of ALE metrics on the resolution T*CP^1 has three real parameters (ζ_1, ζ_2, ζ_3). The ζ_1 direction corresponds to the size of the exceptional CP^1 (Kähler/resolution direction); the (ζ_2, ζ_3) directions correspond to the complex smoothing {uv-w^2=t}. On a product Kähler-Einstein orbifold (Σ_1×Σ_2)/G with Ric=Λg, the curvature operator has R_+=diag(Λ,0,0) with the nonzero eigenvalue in the Kähler form direction and the kernel in the (2,0)+(0,2) directions. Therefore the kernel-directed Eguchi-Hanson replacement (which kills the first Ozuch obstruction) corresponds to a complex smoothing of each A_1 node, not a holomorphic resolution.

2. GLOBAL QG SMOOTHING: For a canonical model Z of a surface of general type with only rational double points (A_1 singularities), a global Q-Gorenstein smoothing exists if H^2(T_Z^0) = 0. By the Burns-Wahl result for RDPs, this equals H^2(T_S) where S is the minimal resolution. By Serre duality, H^2(T_S) = H^0(Ω^1_S ⊗ K_S). The sufficient condition fails (i.e., H^2 > 0) when χ(T_S) = 2K^2-10 > 0, which occurs for K^2 ≥ 6.

3. AMPLENESS PERSISTENCE: If the canonical model Z has a QG smoothing π:Z→Δ with K_{Z/Δ} Q-Cartier, and K_{Z_0} is ample, then K_{Z_t} is ample for small t≠0.

4. AUBIN-YAU: A smooth projective surface with ample canonical bundle carries a unique negative Kähler-Einstein metric with Ric(ω)=-ω.

5. SIMULTANEOUS RESOLUTION: For a flat family of surfaces with ADE singularities, after a finite Weyl-group base change, the family admits a simultaneous resolution. For A_1, this is a Z/2Z base change. The resolved family is smooth, so all fibers are diffeomorphic. The central fiber is the minimal resolution S.

6. CONCLUSION: S is diffeomorphic to Z_t, which carries a KE metric, so the smooth 4-manifold underlying S carries an Einstein metric.

Check each link for correctness. Are there hidden assumptions, missing hypotheses, or known counterexamples to any step?

## Output

## Verification memo: the QG‑smoothing → Aubin–Yau Einstein existence chain for $A_1$ product‑quotient surfaces

### Overall reading

Links 3–6 form a self‑contained algebro‑geometric argument that is correct as a **conditional** statement: *if* $Z$ admits a global Q‑Gorenstein smoothing, *then* the smooth 4‑manifold underlying the minimal resolution $S$ carries a smooth Einstein metric. Every step in that sub‑chain is standard and I found no error, only two places where an implicit hypothesis should be made explicit. Link 2 correctly identifies a sufficient input and correctly computes when the associated cohomology obstruction is nonzero, but the equality it uses between two candidate obstruction spaces is one‑directional, not an equivalence. Link 1 is a heuristic bridge whose curvature‑algebra content is sound but whose central assertion (the obstruction‑killing direction *equals* the smoothing direction) is stated, not derived. The decisive unestablished ingredient is exactly the one the note names: the global smoothing for a concrete family. Details follow.

### Link 1 — hyperkähler parameter identification

The parameter picture is standard and correct. The $A_1$ ALE space carries a hyperkähler triple; the three real periods $(\zeta_1,\zeta_2,\zeta_3)$ of $(\omega_1,\omega_2,\omega_3)$ over the generator of $H_2$ control it. For a fixed complex structure $I$, $\zeta_1$ is the Kähler area of the holomorphic $(-2)$‑curve (resolution), and $\zeta_2+i\zeta_3$ is the period of the holomorphic $(2,0)$‑form, whose nonvanishing removes the holomorphic curve and biholomorphically produces the affine quadric $\{uv-w^2=t\}$ (smoothing). A feature that makes this especially clean and that the argument silently relies on: for $A_1$ the minimal resolution and the Milnor fiber are the *same* smooth 4‑manifold $T^*S^2$, so both parameter regimes glue in diffeomorphic bubbles. This is what later lets Link 6 conclude a diffeomorphism.

The curvature computation is also correct. For a Kähler–Einstein 4‑manifold with $\mathrm{Ric}=\Lambda g$ one has $s=4\Lambda$, and the full self‑dual curvature operator $\mathcal R^+ = W_+ + \tfrac{s}{12}\mathrm{Id}$ has eigenvalue $\tfrac{s}{4}=\Lambda$ on $\mathbb R\omega$ and eigenvalue $0$ on $\Lambda^{2,0}\oplus\Lambda^{0,2}$. So $R_+=\mathrm{diag}(\Lambda,0,0)$ with $\ker R_+$ the $(2,0)+(0,2)$ plane, exactly as written.

Two things need care before this is a proof rather than a picture:

1. **The obstruction‑vanishing assertion is not derived here.** The statement that the Biquard/Ozuch first obstruction to the Eguchi–Hanson gluing is annihilated *precisely* when the bubble parameter sits in $\ker R_+$ is asserted. Neither the note nor the script writes the obstruction bilinear/quadratic form in the ambient curvature and shows it vanishes on $\ker R_+$. This is the one genuinely load‑bearing computation in Link 1 and it is currently a citation‑free assertion. It should be reduced to the explicit Biquard obstruction (the quadratic pairing of $R_+$ at the orbifold point with the bubble's distinguished 2‑form) and checked directly.

2. **The claim $R_-=\mathrm{diag}(\Lambda,0,0)$ deserves an explicit check, and it controls chirality.** For a product of two constant‑curvature surfaces with equal Gauss curvature the $W_-$ block is special by symmetry, but the exact equality of the two chiral blocks is what decides whether a same‑chirality (holomorphic‑compatible) or mixed‑chirality bubble is forced. The note's §6 already isolates the mixed‑chirality regime as one where the smoothing identification breaks and Aubin–Yau does not apply. That is the correct place for this concern, but the $R_-$ equality that separates the two regimes is stated rather than computed. I recommend writing out $W_\pm$ for $\mathbb H^2(k)\times\mathbb H^2(k)$ (and $S^2\times S^2$) explicitly.

Crucially: **Links 3–6 do not depend on Link 1.** The existence conclusion rests entirely on the algebraic smoothing plus Aubin–Yau. Link 1 only supplies an interpretation of why an approximate near‑Einstein gluing lives in the smoothing rather than the resolution direction. So imprecision in Link 1's obstruction identification does not weaken the conditional existence result; it only weakens the narrative connecting the two constructions.

### Link 2 — sufficient condition for global smoothing

The Riemann–Roch arithmetic is correct. $\chi(T_S)=\tfrac16(7c_1^2-5c_2)$, and with $\chi(\mathcal O_S)=1$ so $c_2=12-K^2$, this gives $\chi(T_S)=2K^2-10$. Hence for $K^2\ge 6$, $\chi(T_S)\ge 2$, so $h^2(T_S)=h^1+\chi>0$: the vanishing $H^2(T_S)=0$ cannot hold for $K^2\ge6$. Serre duality $h^2(T_S)=h^0(\Omega^1_S\otimes K_S)$ is correct.

Points requiring precision:

- **Which obstruction space?** For a smoothing of the singular model $Z$ (not a deformation of the pair $(S,E)$), the obstructions to deforming $Z$ with only rational double points live in $H^2(\Theta_Z)$, and for RDPs the local $T^2$ vanishes (hypersurface singularities), so $H^2(\Theta_Z)\cong H^2(S,T_S)$. In the pure‑RDP setting the note's use of $H^2(T_S)$ is the correct obstruction. The parenthetical "$H^2(T_S(-\log E))=0$ (equivalently $H^2(T_S)=0$)" is looser than stated: the sequence $0\to T_S(-\log E)\to T_S\to Q\to 0$ with $Q$ supported on the $(-2)$‑curves gives only a surjection $H^2(T_S(-\log E))\twoheadrightarrow H^2(T_S)$ (since $H^2(Q)=0$ for a sheaf on a curve), not an isomorphism. So the log space is potentially larger. This does not affect the "$K^2\ge6$" conclusion (if $H^2(T_S)>0$ then the log space is too), but it does mean that for $K^2=2,4$ the "numerically possible" optimism about $H^2(T_S)=0$ is weaker than the log‑vanishing that Lee–Park's general theorem invokes. For the pure‑RDP smoothing question, using $H^2(\Theta_Z)=H^2(T_S)$ directly is the cleaner and correct framing.

- **Sufficiency vs. necessity.** The note correctly states the condition is sufficient, not necessary, and does not conclude non‑existence for $K^2=6$. That restraint is right: $H^2\ne0$ leaves smoothability open, and it might genuinely be obstructed for some $K^2=6$ families (which would itself be a substantive finding worth stating as a distinct outcome).

- **Global simultaneity.** $H^2(\Theta_Z)=0$ gives smoothness of the deformation space and surjectivity of $T^1_Z\to\bigoplus_p T^1_p$, so a single family can smooth all nodes at once. This is used implicitly and is correct.

So Link 2's arithmetic and its logical status are correct; the only repair is to state the obstruction space as $H^2(\Theta_Z)\cong H^2(T_S)$ for the RDP case rather than equating it with the log tangent space.

### Links 3 and 4 — ampleness persistence and Aubin–Yau

Both are standard and correct. Openness of relative ampleness in a proper flat family applies to a Cartier multiple $mK_{\mathcal Z/\Delta}$ that is ample on the central fiber, so $K_{Z_t}$ is ample for small $t$. Requires the family to be projective (or the relative canonical to be relatively ample), which QG‑smoothing constructions provide. Aubin–Yau then gives the unique Kähler–Einstein metric with $\mathrm{Ric}(\omega_t)=-\omega_t$ on the smooth projective surface $Z_t$ with ample $K$. No issues.

### Links 5 and 6 — simultaneous resolution and diffeomorphism

Correct, and correct for the RDP‑only setting specifically. Near a node the total space of the smoothing is $\{uv-w^2-t=0\}$, which is smooth (the $\partial_t$ component of the gradient is $-1$). Brieskorn/Atiyah: after the $W(A_1)=\mathbb Z/2$ base change $t=s^2$, the family acquires a threefold ordinary double point admitting a simultaneous (small) resolution, yielding a smooth proper family whose central fiber is the minimal resolution $S$ (unique for $A_1$) and whose other fibers are the smooth $Z_t$. Ehresmann then gives $S\cong_{\mathrm{diff}}Z_t$. Pulling back $\omega_t$'s metric along the diffeomorphism produces a smooth Einstein metric on the smooth 4‑manifold underlying $S$. The conclusion is stated at the right level (smooth 4‑manifold, not the complex structure of $S$), which is important because $S$ itself has $K_S$ nef and big but not ample — the orbifold KE on $Z$ is singular at the nodes, so the smooth Einstein metric on $S$ genuinely comes from the smoothing and is not available by applying Aubin–Yau to $S$ directly. This is real content.

Essential dependence on RDP‑only: the diffeomorphism $S\cong Z_t$ holds because the $A_1$ Milnor fiber and minimal resolution are both $T^*S^2$. For non‑RDP (Wahl / T‑singularity) nodes the Milnor fiber and the resolution are not diffeomorphic (rational‑blowdown regime), and the smooth type of $Z_t$ would differ from $S$. The argument is therefore tied to the $A_1$‑only rows and cannot be extended to general T‑singularities without a different smooth‑topology input. This restriction is respected in the note but should be stated as a structural hypothesis of the theorem, not an incidental feature.

### The decisive unestablished input

The whole chain is conditional on global Q‑Gorenstein smoothability of a concrete $Z$. For $K^2=6$ the sufficient vanishing does not hold, and no alternative smoothing has been produced. For $K^2=2,4$ the vanishing is "numerically possible" but unverified. The single most decision‑relevant computation is therefore $h^2(T_S)=h^0(\Omega^1_S\otimes K_S)$ for the named $K^2=2$ families (Bauer's 7 families), using the $G$‑equivariant structure on $C_1\times C_2$: decompose $H^0(\Omega^1_{C_1\times C_2}\otimes K_{C_1\times C_2})$ into $G$‑isotypic pieces and take invariants, then account for the $(-2)$‑curves. This is a finite equivariant computation on curves of known genus and known $G$‑action; it converts the conditional theorem into an unconditional statement for those families (if the invariant space is $0$) or forces the alternative route (if not). Until it is done, the note establishes a mechanism, not an existence result.

### Bearing on Yau 26 — a structural point the memo should surface

The note's §7 framing ("consistent with, not a counterexample") is logically correct but understates a sharper fact worth making explicit. A Kähler–Einstein metric *is* an Einstein metric, so any manifold produced by this chain already satisfies $\mathrm{Ric}=\lambda h$ with $\lambda<0$, hence trivially satisfies the two‑sided pinching $c_n h\le \mathrm{Ric}\le C_n h$ with $c_n=C_n=\lambda$. Establishing Einstein existence on these manifolds therefore places them among the *trivial positive instances* of the proposition and removes them from the counterexample pool — but it does not bear on the core implication, which concerns whether an *arbitrary* pinched metric on a possibly different manifold forces an Einstein metric. To move toward a refutation one would need a smooth manifold that carries a pinched metric yet carries *no* Einstein metric; product‑quotient resolutions that admit a KE metric are the opposite kind of object. To move toward a proof one needs the implication itself, which this construction does not touch. The value here is genuine but is confined to shrinking the counterexample search among these specific 4‑manifolds, and even that requires the smoothing to be established.

A secondary consistency check that supports (does not prove) the picture: all three rows satisfy Hitchin–Thorpe $2e\ge 3|\tau|$ ($K^2=2$: $20\ge18$; $K^2=4$: $16\ge12$; $K^2=6$: $12\ge6$), so the necessary 4‑dimensional Einstein condition does not exclude these manifolds — consistent with the existence conclusion but carrying no independent force.

### What would strengthen the work

- Compute $h^0(\Omega^1_S\otimes K_S)$ equivariantly for the $K^2=2$ (and $4$) families; this is the pivotal number and it is tractable.
- Write the Biquard/Ozuch first obstruction explicitly as a pairing with $R_+$ and verify vanishing on $\ker R_+$, so that Link 1's "obstruction direction = smoothing direction" becomes a computation rather than an assertion; and compute $W_\pm$ for the product model to settle the chirality point in §6.
- For $K^2=6$, determine whether a smoothing exists by an independent method or whether the model is smoothing‑rigid; a rigidity result would be a distinct and informative outcome.
- State the theorem with its structural hypotheses explicit: RDP‑only (so that Milnor fiber ≅ resolution), projective smoothing family, same‑chirality gluing, and the smoothing existence input.

I found no mathematical error in the conditional chain and no counterexample to any individual step. The gaps are (i) the unproven global smoothing input, (ii) the asserted‑not‑derived obstruction identification in Link 1, and (iii) the one‑directional cohomology equivalence in Link 2, none of which invalidate the conditional statement but all of which stand between the present note and an unconditional existence result for a named family.