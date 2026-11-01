# TTCS Independent Branch Record

```json
{
  "step_id": 80,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step80_J_equivariant_all_order_reduction.md",
    "Sessions/S0910A01/workspace/data/step80_J_symmetry_verification.json",
    "Sessions/S0910A01/workspace/notes/step79_angular_rho_and_tilt_repair.md",
    "Sessions/S0910A01/workspace/notes/step78_equivariant_diagonal_reduction.md"
  ]
}
```

## Task

Verify the J-symmetry all-order obstruction elimination theorem for the product orbifold (S²×S²)/⟨(r_π,r_π)⟩ with EH insertion direction ω₂. The claim is: simultaneous complex conjugation J(z,w)=(z̄,w̄) acts on the SD/ASD basis at each node as diag(-1,+1,-1), fixes ω₂ (the insertion direction), and therefore a J-equivariant Eguchi-Hanson construction has zero obstruction projections onto the J-odd directions (ω₁ and ω₃) at EVERY order of the Ozuch expansion. Combined with A-symmetry (killing scalar kernel ν_l) and the rank-one determinant (μ₁=0), this eliminates all finite-dimensional Ozuch obstructions. Check: (1) Is the J-parity argument mathematically rigorous? (2) Does J genuinely extend as an isometry of the EH metric when the insertion direction is ω₂? (3) Is the 'every order' claim correct, or could higher-order gauge/normalization issues break J-invariance? (4) Is the surviving system really balanced (2 equations in 2 unknowns)? (5) What is the strongest statement about existence that this structural result supports, and what analytical gaps remain?

## Output

# Verification Memo: J-symmetry all-order obstruction elimination (Step 80)

## Independent recomputation of the parity linear algebra

I reconstructed the SD/ASD parity table from scratch to check it does not rest on the numerical script alone.

Tangent frame at a node $(N,N)$: $e_1=\partial_{x_1},e_2=\partial_{x_2}$ (factor 1), $e_3=\partial_{y_1},e_4=\partial_{y_2}$ (factor 2). In these real coordinates $J(x_1,x_2,x_3)=(x_1,-x_2,x_3)$ gives $dJ=\mathrm{diag}(1,-1,1,-1)$, $\det dJ=+1$ (orientation-preserving, so the $\Lambda^+\oplus\Lambda^-$ splitting is preserved). With the standard bases

$$\omega_1^\pm=e_{12}\pm e_{34},\quad \omega_2^\pm=e_{13}\mp e_{42},\quad \omega_3^\pm=e_{14}\pm e_{23},$$

and $dJ$ sending $e_{12}\to-e_{12}$, $e_{34}\to-e_{34}$, $e_{13}\to+e_{13}$, $e_{24}\to+e_{24}$, $e_{14}\to-e_{14}$, $e_{23}\to-e_{23}$, I get

$$J^*\omega_1^\pm=-\omega_1^\pm,\quad J^*\omega_2^\pm=+\omega_2^\pm,\quad J^*\omega_3^\pm=-\omega_3^\pm.$$

So $\mathrm{diag}(-1,+1,-1)$ on **both** chiralities. This matches the note and the JSON exactly. The $\rho_x$ transformation ($\rho_{Jx}(\omega_2)_j=\varepsilon_j^-\rho_x(\omega_2)_j$, $\varepsilon^-=(-1,+1,-1)$) and the $H^4$ invariance (each summand carries parity $\varepsilon_j^-\cdot\varepsilon_j^-=+1$) follow correctly by conjugation of endomorphisms, since $J$ orthogonal implies $J^{-1}(AB)J=(J^{-1}AJ)(J^{-1}BJ)$ and the endomorphism parity equals the 2-form parity. **Point (1): the parity layer is rigorous and independently confirmed.** The commutations $J\sigma=\sigma J$, $JA=AJ$ also check out directly (all three maps are diagonal in the $x_i,y_i$ coordinates).

## (2) J as an isometry of the Eguchi–Hanson bubble with insertion $\omega_2$

This holds, and the reason is worth stating precisely because it is what makes the insertion-direction choice special. $J$ fixes $\omega_2^+$ and negates $\omega_1^+,\omega_3^+$. Writing the hyperkähler triple $(I_1,I_2,I_3)$ with Kähler forms $(\omega_1^+,\omega_2^+,\omega_3^+)$, one checks $J$ commutes with $I_2$ (e.g. $J I_2 e_1=Je_3=e_3=I_2 e_1=I_2 J e_1$) and anticommutes with $I_1,I_3$. Hence $J$ is a **holomorphic** isometry of the flat cone $\mathbb C^2/\mathbb Z_2$ with respect to the $I_2$ structure that is used to resolve into $T^*\mathbb{CP}^1$, fixes $0$, and preserves the $I_2$-Kähler class (since $J^*\omega_2^+=+\omega_2^+$). It negates the holomorphic 2-form $\Omega=\omega_1^++i\omega_3^+$, i.e. it is anti-holomorphic for $I_1,I_3$, but that leaves the metric fixed because the EH metric is the same for the whole compatible triple. A holomorphic isometry of the cone fixing the origin and the resolution's Kähler class extends to the minimal resolution and preserves the unique ALE hyperkähler metric in that class. So $J$ is a genuine EH isometry. The note asserts this rather than proving it, but the supporting facts are standard. One requirement is implicit: the insertion must align the bubble's $I_2$-Kähler direction with $\omega_2^+$; only for a $J$-fixed insertion direction does $J$ preserve the glued bubble. Since $\ker R^+=\mathrm{span}\{\omega_2^+,\omega_3^+\}$ and $\omega_3$ is $J$-odd, **$J$-equivariance forces the insertion direction to be exactly $\omega_2$** — the previously "free" angle $\alpha$ (Step 78) is fixed to $0$ by the symmetry, not left as a gauge parameter. This is internally consistent and tightens the parameter count.

## (3) The "every order" statement

This is the strongest and most valuable part of the note, and it is legitimately an exact (not Taylor) argument, subject to one requirement.

The mechanism: if the approximate family $g_t$ is $J$-invariant, then the full nonlinear residual $\mathrm{Ric}(g_t)-\Lambda g_t$ is a $J$-invariant section of $\mathrm{Sym}^2 T^*M$; since $J$ acts trivially on the scale $t$, each order-$t^n$ coefficient is separately $J$-invariant; pairing against a $J$-odd cokernel mode $\bar{\mathbf o}_k$ ($\varepsilon_k=-1$) gives $c_k^{(n)}=\varepsilon_k c_k^{(n)}=-c_k^{(n)}=0$. This is order-independent by construction, and the note correctly emphasizes that no truncation is used. The Lyapunov–Schmidt solve does not disturb this: $J$ commutes with the linearized operator, so the kernel/cokernel split into $J$-even and $J$-odd invariant subspaces, the complementary correction $w$ can be chosen $J$-invariant, and the $J$-odd projections are automatically zero.

The one requirement carrying the whole argument is that **$g_t$ and the DeTurck reference are exactly $J$-invariant**. This needs: (a) $J$-invariant EH bubbles (established in (2)); (b) $J$-invariant cutoffs — radial cutoffs in the neck are automatically $J$-invariant, so this is fine; (c) a $J$-invariant background/reference metric, which the product orbifold metric is. There is no hidden obstruction here provided the gluing uses $J$-symmetric data, which the fixed insertion $\omega_2$ and radial gluing supply. So the "all orders" statement is sound. What it kills is precisely the $\omega_1$ and $\omega_3$ ($J$-odd) projections at every order.

## Internal inconsistency in the conclusion phrasing

The JSON `combined_theorem.conclusion` reads "**ALL** finite-dimensional Ozuch obstructions vanish," while the adjacent `surviving_system` field states "one $\omega_2$-projection per orbit at order $\ge t^3$," and §7 of the note describes a surviving $2\times2$ system $F_1=F_2=0$. These cannot both hold literally: the surviving $\omega_2$-projections at order $t^3$ **are** finite-dimensional obstructions and they do not vanish by symmetry. $J$ is even on $\omega_2$, so it provides no cancellation there; and the shape mode $g_1-g_2$ is both $A$-even and $J$-even, so it too is untouched. The accurate statement is: the symmetry removes the $\nu_l$ scalar-kernel equations (via $A$) and the $\omega_1,\omega_3$ transverse projections at all orders (via $J$), and the rank-one determinant gives $\mu_1=0$ at order $t^2$; what remains is the $\omega_2$-projected system at order $\ge t^3$ plus an indefinite mode. The §8 text is correct; the JSON `conclusion` string and the §6 header "ALL finite-dimensional obstruction equations are satisfied" overstate relative to §7/§8 and should be reconciled to the "$J$-odd + $t^2$-radial" content.

## (4) Is the surviving system genuinely balanced $2\times 2$?

The counting is plausible. Per node the cokernel has three SD directions; $A$ removes the $\nu_l$, $J$ removes $\omega_1,\omega_3$, leaving one $\omega_2$ equation per node; $A$ identifies the two nodes inside each of the two orbits, giving 2 equations. Parameters: one EH scale $t_j$ per node, reduced by $A$ to $(t_1,t_2)$; the insertion angle is fixed by $J$. So 2 equations in 2 unknowns. This matches the classical picture in Biquard/Ozuch gluing, where the leading condition per EH bubble is a single scalar scale-balancing equation. That structural expectation supports the count.

Two concrete problems with the reduction to a single equation:

1. **Misattributed orbit exchange.** §7 states "by the diagonal $A$-symmetry (which exchanges the two orbits) $F_1$ and $F_2$ have the same functional form." But Step 78 §1.2 defines $A(x,y)=(-x,-y)$ with orbits $\{(N,N),(S,S)\}$ and $\{(N,S),(S,N)\}$, and $A$ acts **within** each orbit — it does not exchange orbit 1 with orbit 2. So the stated justification contradicts the note's own definition of $A$. The two orbits also carry **opposite** chirality ($+$ vs $-$), so an exchange symmetry must reverse orientation. A single-factor involution such as $(p,q)\mapsto(p,-q)$ (antipodal on one $S^2$ only, or a $z$-reflection on one factor) sends $(N,N)\leftrightarrow(N,S)$ and $(S,S)\leftrightarrow(S,N)$, i.e. it exchanges the two orbits, and it reverses the 4D orientation, hence swaps chirality $+\leftrightarrow-$ consistently. Combined with $R^+=R^-=\mathrm{diag}(\Lambda,0,0)$ on the product, this is the actual reason $F_1$ and $F_2$ can share a functional form. To reduce to a single $F(t)=0$, the note needs this chirality-reversing single-factor involution to commute with $J$ and $\sigma$ and to be imposable equivariantly — that compatibility is not checked. As written, the single-equation reduction is not yet justified by the symmetry that is actually named.

2. **The indefinite shape mode.** $g_1-g_2$ survives both symmetries and has $P$-eigenvalue $-\Lambda$. Because this eigenvalue is nonzero it is not an additional obstruction equation — it lies in the invertible range — but its sign makes the linearized operator on the $A{+}J$-invariant complement **indefinite**. This directly undercuts the earlier Step 78 §7 statement that the relevant sector has a clean positive spectral gap ($3\Lambda/2$, or $\Lambda$ after the Corollary 3.2 correction) supplying a bounded positive inverse and contraction. With an eigenvalue of sign $-\Lambda$ present, the inverse exists but there is no automatic contraction; a Banach fixed-point closure must control this indefinite direction explicitly. The note acknowledges the mode "must remain" but the consequence for the inverse estimate deserves to be stated plainly: the positive-operator argument does not apply on the full invariant complement.

## (5) Strongest supported existence statement, and what is unresolved

**Supported.** On $(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle$ with $J$-fixed insertion $\omega_2$, the exact discrete symmetries $A$ and $J$ collapse the infinite family of transverse Ozuch necessary conditions to a finite structure: the $\nu_l$ vanish, the $\omega_1,\omega_3$ projections vanish at every order, and $\mu_1$ vanishes at order $t^2$ (rank-one degeneracy). What is left is a finite $\omega_2$-projected scale system at order $\ge t^3$ together with an indefinite finite-dimensional analytical inverse problem. This is a real structural reduction: it converts "infinitely many conditions" into "a small finite set plus one analytic estimate," and the all-order vanishing is by exact symmetry rather than coefficient-by-coefficient computation. That is a genuine advance for this one construction.

**Unresolved, in order of decisiveness.**

1. **The order-$t^3$ $\omega_2$ coefficient sign.** This is the whole existence question and it has not been computed. The rank-one structure makes $\mu_1$ ($t^2$) vanish, which pushes the leading obstruction to the higher-order $\omega_2$ term — exactly where Biquard–Ozuch type obstructions are known to carry a definite sign that can prevent EH desingularization of a positively-curved Einstein orbifold. Since $R^+=\mathrm{diag}(\Lambda,0,0)\ne0$ at the nodes, this is not a case where the ambient self-dual curvature vanishes; the surviving scalar function $F(t)$ (or the pair $F_1,F_2$) may have a definite sign and no small positive root. Determining the leading nonzero coefficient of $F$ and its sign is the calculation that would decide the construction. Nothing in the symmetry argument bears on this sign.

2. **The indefinite inverse/contraction.** Even granting a zero of $F$ with transversality, the nonlinear closure requires a bounded inverse and contraction on the $A{+}J$-invariant complement, which now contains the $-\Lambda$ shape direction. The clean positive-gap argument does not cover it.

3. **Enumeration of orbifold deformation parameters $v$.** The note handles the four scalar-kernel $\nu_l$ but does not fully enumerate whether the product Einstein orbifold carries additional integrable deformations $v$ entering Ozuch's reduced map; if present they change the parameter/equation count from the assumed $2\times2$.

4. **Relation to the full Yau-26 proposition.** The note is explicit and correct that even a completed positive-Einstein metric on $\#_3(S^2\times S^2)$ would be one construction on one topology in one dimension, sign-restricted (positive $\lambda$), and would not decide the dimension-independent, sign-unrestricted pinching statement. This framing is accurate.

## Net assessment

The parity linear algebra (1) is correct and I confirmed it independently. The EH isometry extension (2) is sound with standard resolution facts and correctly forces the insertion direction to $\omega_2$. The all-order argument (3) is valid as an exact symmetry argument and is the note's real contribution; it rests only on $J$-invariant gluing data, which radial cutoffs and the fixed $\omega_2$ insertion supply. The reservations are: the "all obstructions vanish" phrasing contradicts the surviving $\omega_2$ system in the same document and should be reconciled; the reduction to a single $F(t)=0$ is attributed to $A$, which by the note's own definition does not exchange the two opposite-chirality orbits — the correct justification uses a chirality-reversing single-factor involution together with $R^+=R^-$, whose equivariant compatibility with $J$ is unchecked; and the indefinite $g_1-g_2$ mode removes the positive-inverse shortcut. The decisive open computation is the sign of the leading order-$t^3$ $\omega_2$ obstruction coefficient, which is precisely where a Biquard/Ozuch definite-sign obstruction would live and which the symmetry argument does not touch.