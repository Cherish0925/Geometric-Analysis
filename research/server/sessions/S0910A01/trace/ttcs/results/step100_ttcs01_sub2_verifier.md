# TTCS Independent Branch Record

```json
{
  "step_id": 100,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step100_chirality_cancellation_proof.md",
    "Sessions/S0910A01/workspace/notes/step98_trace_obstruction_theorem.md",
    "Sessions/S0910A01/workspace/data/step100_chirality_cancellation_proof.json",
    "Sessions/S0910A01/workspace/plans/route_assessment_step100.md",
    "Sessions/S0910A01/workspace/notes/step99_geometric_mode_bridge_check.md"
  ]
}
```

## Task

Verify the structural proof of same-chirality vanishing B_{++} = B_{--} = 0 in the product-orbifold Ozuch desingularization calculation. The proof claims three algebraic mechanisms: (1) tensor-pole parity giving pairwise cancellation when tensor factors have different poles; (2) scalar-mode parity where Block_D = Block_O forces c2+s2 cancellation when tensor is at the same pole; (3) cross-chirality nonzero because R_minus(O,D) = +1/2 O changes sign from R_plus(O,D) = -1/2 O. The geometric root is the definite chirality of the EH curvature (Ozuch Prop 1.16: linearized curvature d_e R^+(H^4(zeta^+)) = 0). Check: (a) Are the three mechanisms correctly stated and do they cover all cases (sector AA/BB, pairs NS/SN/SS)? (b) Does the geometric interpretation correctly connect the algebraic identities to the EH definite chirality? (c) Are there hidden assumptions or gaps in the proof? (d) Does the result extend to the AB sector? (e) What does this mean for the full Ozuch equation — can the self/deformation terms break the positive inter-node response?

## Output

## Verification memo: same-chirality vanishing $B_{++}=B_{--}=0$

I reproduced the algebra of all three mechanisms by hand from the maps as listed, checked case coverage, and traced what the identity actually rests on. The finite-dimensional identity is correct as stated for the implemented AA/BB tensor–scalar model. Below are the confirmations, the exact ingredients the result depends on, one descriptive inconsistency, and the answers to (a)–(e).

### The algebra checks out

**Case 1 (tensor factor at different poles).** With source node signs $T_{\rm src}(E,c_2)=\sigma D,\ T_{\rm src}(M,s_2)=\sigma D$ and receiver values $D,\,-D$, bilinearity of $R_+$ in its first argument gives
$$[R_+(D,S)+R_+(-D,S)]\otimes S_+(\sigma D,S)=0,$$
and the pairing $\{(E,s_2),(M,c_2)\}$ vanishes by the same argument in the source slot ($-\sigma O+\sigma O$). This holds for **every** scalar $S$ (including $S=I$) and needs no scalar sum. Correct.

**Case 2 (tensor factor at the same pole).** I recomputed both blocks:
$$\mathrm{Block}_D=2\!\left[(-\tfrac12 D)\otimes(-\tfrac14 D)+(-\tfrac12 O)\otimes(-\tfrac14 O)\right]=\tfrac14(D\otimes D+O\otimes O),$$
$$\mathrm{Block}_O=2\!\left[(-\tfrac12 O)\otimes(-\tfrac14 O)+(\tfrac12 D)\otimes(\tfrac14 D)\right]=\tfrac14(O\otimes O+D\otimes D).$$
So $\mathrm{Block}_D=\mathrm{Block}_O$ exactly. I also checked that this equality is **robust to unequal electric/magnetic weights**: summing the four polarizations gives $(w_E+w_M)[R_+(D,S)\otimes S_+(D,S)+R_+(O,S)\otimes S_+(O,S)]$, and each of $E,M$ contributes one $D$-type and one $O$-type term, so the $w_E=w_M$ degeneracy is not required here. The final vanishing is $(\eta_c w_c+\eta_s w_s)\mathrm{Block}_D$.

**Case coverage is complete.** The pole bookkeeping is right: for AA the tensor lives on factor A, so Case 1 = {SN, SS}, Case 2 = {NS}; for BB, Case 1 = {NS, SS}, Case 2 = {SN}. All six (sector × pair) combinations are hit. Within each case, every scalar mode is covered because the covariant Hessian of any scalar harmonic at a pole lies in $\mathrm{Sym}^2(\mathbb R^2)=\{I,D,O\}$: $m=0\to I$, $m=2\to D,O$, and $m=1$ has vanishing 2-jet at the pole (the function is $\sim x\cdot h(r^2)$, Hessian $=0$ at the origin in normal coordinates), while $m\ge3$ content does not reach the 2-jet. So $\{I,D,O\}$ is genuinely complete and the identity is degree-independent — the 12 sampled $(\ell_t,\ell_s)$ pairs are a confirmation, not the substance.

### The single most load-bearing ingredient: the scalar node-sign relation

The Case 2 cancellation is *not* forced by $\mathrm{Block}_D=\mathrm{Block}_O$ alone. It also needs the $c_2$ and $s_2$ scalar modes to enter the source pole with **opposite** node signs, $\eta_c=-\eta_s$, together with equal degeneracy weights $w_c=w_s$. Then $(\eta_c w_c+\eta_s w_s)=0$.

This is where a substantive geometric input hides. Under the pure antipodal map $\theta\to\pi-\theta,\ \phi\to\phi+\pi$, both $m=2$ harmonics $\cos2\phi,\sin2\phi$ pick up the **same** sign $(-1)^{\ell}$ — which would give $\eta_c=\eta_s$ and a **nonzero** Case-2 block, contradicting the theorem. The opposite-sign relation $\eta_c=-\eta_s$ requires the node-frame transport / $\mathbb Z_2$ identification to include a $\phi$-reflection (cos even, sin odd). The tensor node signs already listed ($T_{\rm src}(E,c_2)=+\sigma D$ vs $T_{\rm src}(E,s_2)=-\sigma O$) carry exactly this opposite relative sign, so the convention is internally consistent between the tensor and scalar sides. But the reflection is a **transport convention inherited from the orbifold geometry**, not derived inside Step 100. The identity is only as reliable as that convention. This is precisely the "node-frame transport and quotient normalization" the Step 99 note lists as still-assumed; it deserves to be stated as the pivot of Case 2 rather than folded into the notation, because the theorem's truth flips if that reflection is absent.

### One descriptive inconsistency (does not affect the theorem)

The note says the minus-chirality maps "differ only in the K-odd cross terms," then lists $R_-(O,O)=-\tfrac12 D$ — a change to a diagonal $(O,O)$ entry, not a cross term. The rule that makes the cross-chirality algebra work is cleaner: **flip sign of every map whose tensor argument is $O$** (K-odd tensor polarization). Under this rule I confirm
$$\mathrm{Block}_D^{+-}=\tfrac14(D\otimes D-O\otimes O),\qquad \mathrm{Block}_O^{+-}=-\tfrac14(D\otimes D-O\otimes O)=-\mathrm{Block}_D^{+-},$$
so $c_2+s_2$ reinforces and $B_{+-}\ne0$. Note that if instead one flips *both* cross terms $(O,D)$ and $(D,O)$ (a literal reading of "K-odd cross terms"), then $\mathrm{Block}_O^{+-}=-\tfrac14(D\otimes D+O\otimes O)\ne-\mathrm{Block}_D^{+-}$ and the stated $B_{+-}$ structure changes (though it stays nonzero). The nonvanishing conclusion survives either reading; the exact channel structure quoted for $B_{+-}$ holds only under the "tensor-$O$" flip rule. Since the same-chirality theorem uses only $R_+,S_+$, this ambiguity touches only the secondary "why nonzero" explanation, not the main result.

### (b) Geometric interpretation — consistent, but stated more firmly than derived

The picture is coherent and attractive. EH is anti-self-dual, $R^+(\mathbf{eh})=0$, and $d_{\mathbf e}R^+(H^4(\zeta^+))=0$: a $+$-chirality EH source produces no self-dual linearized curvature, so the self-dual receiver $R_+$ is blind to it, giving $B_{++}=0$; a $-$ source carries the opposite duality, is visible, and $B_{+-}\ne0$. The four sign assignments ($B_{++}=B_{--}=0$, $B_{+-},B_{-+}\ne0$) are mutually consistent with this reading.

However, Step 100 asserts the algebraic identities are "traced to" the EH definite chirality, while Steps 98/99 state — correctly — that "no full representation-theoretic or Kähler-geometric proof has yet been written" and that membership of the Ozuch singular field in the linearized Kähler sector "is not yet proved." The rigorous content is the finite algebra for the *implemented* maps; the Ozuch/Kähler statement is a compatible interpretation, not a derivation of the identity from the geometric fact. The two levels should not be merged: the algebra is explained by, but has not been re-derived from, $d_{\mathbf e}R^+=0$.

### (d) AB sector — not covered

The proof and its 72 verified cases are $2\ (\text{AA,BB})\times3\ (\text{NS,SN,SS})\times12$ degree pairs; AB is absent. The three mechanisms are intrinsically spin-2: they use the four $\{D,O,O,-D\}$ tensor polarizations and the $\{I,D,O\}$ scalar Hessian decomposition. The AB one-form sector has vector representation content and, per the Step 98 table, contributes an **isotropic trace channel** $c_0=4a$ — and that AB trace channel is exactly what supplies the positive inter-node margin ($8a\,t^2\approx0.2515\,t^2$, after the $16a$ double-count was corrected). So the sector that carries the positive response is the one *not* addressed by this vanishing theorem; AB same-chirality behavior needs its own argument.

### (e) Meaning for the full Ozuch equation

The vanishing concerns only the inter-node blocks $B_{ij}$. In
$$F_i^\varepsilon=F_i^{\rm self}+F_i^{\rm deform,\varepsilon}+\sum_{j\ne i}B_{ij}^{\varepsilon_i\varepsilon_j}+F_i^{\rm complement}+R_i,$$
the self, deformation, complement, and remainder terms are not touched by $B_{++}=0$. Chirality-independence of the self term does not make it vanish, and any of these can carry same-chirality content that shifts or overrides the positive inter-node response. The notes state this correctly. The result is one exact term inside an equation whose other terms remain uncomputed, so it does not on its own establish a positive-direction obstruction.

### Additional items worth carrying forward

1. **Low scalar degree required repair.** An earlier fixed-degree run produced `nan` at $\ell_s=1$ through a nonexistent $m=2$ normalization; the $\ell_s=0$ constant slice and $\ell_s=1$ slice were then treated as separate cases in `step99_exact_coeff_lowmode_audit.json`. The current statement is sound, but the low-degree slices are genuinely special (constant scalar has zero Hessian, $m=1$ has zero 2-jet) and are the fragile part of any generalization.

2. **Bilinearity is an input.** Both cases lean on $R_\pm,S_\pm$ being exactly bilinear (linear response). This is the leading-order/linearized structure by construction; nonlinear source dependence would not be captured, which matters when the same identity is asked to speak about the full gluing equation.

3. **Exactness of the maps.** The whole identity is downstream of the numerical values of $R_\pm,S_\pm$. `step99_exact_coeff_lowmode_audit.json` regenerating these from the self-dual/anti-self-dual form definitions in exact rationals (max difference $0.0$ against the Step 96 floats), plus A02's independent reproduction (#675), is the right support; the identity should always be quoted together with that exact-coefficient regeneration, since a wrong sign in one map entry would silently change the conclusion.

### Net reading

The theorem is a correct, degree-independent finite algebraic identity for the implemented AA/BB tensor–scalar model, resting on: the exact map values, the $\phi$-reflection transport that yields $\eta_c=-\eta_s$, $m=2$ scalar degeneracy $w_c=w_s$, bilinearity, and completeness of the $\{D,O,O,-D\}$/$\{I,D,O\}$ bases. The transport-sign relation is the pivot most worth exhibiting explicitly and pinning to the orbifold geometry. The geometric EH-duality reading is compatible and illuminating but is interpretation rather than a second proof. The AB sector — carrier of the positive response — is outside these three mechanisms, and the self/deformation/complement/remainder terms of the full equation remain uncomputed, so the identity is a clean piece rather than a statement about the complete desingularization response.