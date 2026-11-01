# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md",
    "Sessions/S0910A01/workspace/data/step77_scalar_kernel_and_pairing.json",
    "Sessions/S0910A01/workspace/data/step77_slice_decomposition_verify.json",
    "Sessions/S0910A02/workspace/notes/step68_spectral_symmetry_and_multipole_gate.md",
    "Sessions/S0910A02/workspace/data/step68_orbifold_kernel_full_vs_tt.json",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Verify the Step 77 repair of the mixed-row product-orbifold obstruction problem. Please check the mathematical substance, not prose style: (i) Ozuch Definition 1.8 full L2 kernel versus TT kernel distinction; (ii) the calculation that axial first harmonics u1,u2 on S^2 descend under the half-turn and give P(u_i g_j)=0 for Ozuch P=1/2∇*∇-R°; (iii) the Bianchi/pure-gauge slice interpretation and whether it is enough to remove or must be incorporated into the finite-dimensional equations; (iv) the local raw normal-coordinate projection prototype in step77_scalar_kernel_and_pairing.json, especially whether the -pi^2/18 coefficient should be treated only as a unit test before slice/Green transport; (v) the separation of lambda, mu_1, mu_2,3, projected equations, full residual/inverse estimates, and the topology/Ozuch-Q0.8 scope corrections. Identify any remaining mathematical errors or the most useful next executable computation for the singular-subtracted Green response H_ij,2.

## Output

# Verification Memo: Step 77 Product-Orbifold Obstruction Repair

I checked the mathematical substance of the Step 77 note and the two data files against the Ozuch source and by independent recomputation. The central corrections are sound. Below I confirm each computation, flag two genuine unresolved mathematical points that sit upstream of the queued Green computation, and specify the most decisive next executable step.

## 1. Definition 1.8 kernel reading — correct

The source text of Definition 1.8 reads: "$\mathbf O(\mathbf g)$ as the kernel of $P_{\mathbf g}$ on $L^2(\mathbf g)$," with $P_g=\tfrac12\nabla^*\nabla-\mathring R$ acting on all symmetric 2‑tensors (the displayed operator has no transverse‑traceless restriction). The Step 77 insistence that Step 76 may not delete the $\nu_l$ projections by invoking only $\ker(P|_{TT})=0$ is a faithful reading. The gauged operator $P=\tfrac12\nabla^*\nabla-\mathring R$ is the full linearization of $\operatorname{Ric}-\Lambda+\delta^*B$ on all symmetric 2‑tensors (the Bianchi term cancels the gauge pieces), so the literal $L^2$ kernel is the relevant object in Def 1.8.

## 2. The identity $P(u_ig_j)=0$ — independently reproduced

Using Gauss curvature $=\Lambda$ on each factor: the $\ell=1$ eigenvalue is $\ell(\ell+1)\Lambda=2\Lambda$, and the Obata relation gives $\nabla^2 u=-\Lambda u\,g_{\text{factor}}$. For $f=u_1$ on factor 1 and $g_i$ parallel:
- $\nabla^*\nabla(f g_i)=(\Delta f)g_i=2\Lambda f g_i$ (with $\Delta f=\Delta_{S^2_1}f=2\Lambda f$).
- $\mathring R(g_1)(e_1,e_1)=\operatorname{Rm}_1(e_2,e_1,e_1,e_2)=\Lambda$; mixed terms vanish because the product curvature is block‑diagonal, giving $\mathring R(g_i)=\Lambda g_i$, hence $\mathring R(fg_i)=\Lambda f g_i$.
- $P(f g_i)=\tfrac12(2\Lambda)fg_i-\Lambda f g_i=0$. ✓

I also confirmed the enumeration is complete: $P(fg_i)=0$ forces $\Delta f=2\Lambda f$, i.e. $\ell=1$ only. On the cover there are $3\times2+3\times2=12$ such modes; under $(r_\pi,r_\pi)$ the $\ell=1$ action is $\operatorname{diag}(-1,-1,+1)$ per factor, so only the axial harmonic descends (multiplicity 1 per factor), leaving exactly 4 modes $\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}$ on the quotient. This matches both A01 and A02.

## 3. Bianchi/gauge slice — correct, and the interpretation is the right one

With $B=\delta+\tfrac12 d\operatorname{tr}$: $\operatorname{div}(fg_1)=df$, $\operatorname{div}(fg_2)=0$ for $f$ on factor 1, and $\operatorname{tr}(af g_1+bfg_2)=2(a+b)f$. Thus $B(af g_1+bfg_2)=b\,df$, so the Bianchi‑surviving direction is $b=0$, i.e. $u_1g_1$, which is pure gauge: $\mathcal L_{\nabla u_1}g=2\nabla^2u_1=-2\Lambda u_1g_1$. The TT forcing $h=(a-c\Lambda)fg_1+bfg_2$, trace‑free $\Rightarrow(a-c\Lambda)+b=0$, divergence‑free $\Rightarrow a-c\Lambda=0$, hence $b=0$, $h=0$. All verified.

The structurally important consequence, which the note states correctly but could sharpen: **modulo gauge the 4‑dimensional kernel reduces to 2 genuine directions.** $u_1g_1,u_2g_2$ are pure gauge (Lie derivatives). $u_1g_2\equiv u_1g$ and $u_2g_1\equiv u_2g$ modulo gauge — conformal‑type directions that are *not* pure gauge on the product. So the physically meaningful non‑gauge kernel is exactly 2‑dimensional. The note's conclusion that the slice "must be derived and substituted, not imposed afterwards" is the correct position, and this refinement (4 = 2 gauge + 2 conformal) makes precise what the slice must accomplish.

## 4. Relative mode and node curvature — correct

$h_{\text{rel}}=g_1-g_2$ is parallel, trace‑free, divergence‑free; $\mathring R h_{\text{rel}}=\Lambda h_{\text{rel}}$, so $Ph_{\text{rel}}=-\Lambda h_{\text{rel}}$, eigenvalue $-\Lambda$ (Ozuch) / $-2\Lambda$ (Kröncke $\Delta_E=2P$). This is the known destabilizing direction of $S^2\times S^2$; the product is unstable yet non‑degenerate (no small TT eigenvalue). A02's convention warning (rejecting a "$-4\Lambda$" normalization) is consistent.

Node curvature: the product curvature operator gives $\mathcal R(\omega_1^\pm)=\Lambda\omega_1^\pm$, $\mathcal R(\omega_{2,3}^\pm)=0$, so $R^\pm=\operatorname{diag}(\Lambda,0,0)$ with $\operatorname{tr}R^+=R_{\text{scal}}/4=\Lambda$ ✓. Consequently:
- $\lambda_k^j(\phi_j,0)=0$ for $\phi_j\in\ker R^{\epsilon_j}=\operatorname{span}\{\omega_2,\omega_3\}$ (rank‑one $R^\pm$). ✓
- $\mu_1^j=C\det\!\begin{psmallmatrix}R_{22}&R_{23}\\R_{32}&R_{33}\end{psmallmatrix}=0$: with $\phi=\omega_2^+$, the block on $\phi^\perp$ is $\operatorname{diag}(\Lambda,0)$, determinant $0$. ✓
- The note is right that Lemma 2.14 / Biq16 Lemme 9 supplies **only** $\mu_1$; $\mu_2,\mu_3$ are not fixed by this determinant. The retraction of "all second‑order obstructions vanish" is warranted.

This places the product orbifold as one that *satisfies* the Ozuch necessary condition (rank‑one Kähler $R^\pm$), so Theorem 0.2 does not exclude it — the decision therefore lives entirely in the inter‑node coupling, exactly as the note argues.

## 5. Topology and coverage corrections — verified

$\chi\big((S^2\times S^2)/\mathbb Z_2\ \text{resolved}\big)=8$: quotient of $S^2\times S^2$ ($\chi=4$) by an involution with 4 fixed points gives $\chi=4$ as a space, and blowing up 4 $A_1$ points adds $+4$; the resolution is simply connected, so $b_2=\chi-2=6$. ✓ The row assignments follow $\tau=2k-4$ (checked at $k=0,\dots,4$: $-4,-2,0,+2,+4$), and the two $k=2$ classes ($3\mathbb{CP}^2\#3\overline{\mathbb{CP}}^2$ odd vs. $\#3(S^2\times S^2)$ even) are distinguished only by intersection‑form parity, which is what the adjacent/opposite gluing and the reflection symmetry must decide. Q0.8 in the source is indeed a Ricci‑flat statement about trees of Kähler Ricci‑flat ALE metrics, so a flat $T^4/\mathbb Z_2$ computation is a control unless a transfer to the positive product is supplied. All correct.

The reflection $c(z,w)=(\bar z,w)$ is orientation‑reversing, commutes with $\rho=(-z,-w)$ (both sides equal $(-\bar z,-w)$), fixes all four nodes, and exchanges $\Lambda^\pm$; hence $r=1\sim r=3$ and $r=2$ self‑paired. This is a valid consistency test for any sign‑pattern computation.

## 6. The $-\pi^2/18$ prototype — right kind of object, but two things are missing

The pairing $\nu_l=3\int_{S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle$ (Prop 2.10) is a multipole‑to‑second‑jet contraction, not a value‑Green sum, and the prototype computes this kind of integral. So the object is correctly targeted. Two substantive points, however, mean $-\pi^2/18$ cannot yet be read as an obstruction coefficient:

**(a) It returns equal nonzero values on the pure‑gauge modes.** For $u_1g_1,u_2g_2$ (Lie derivatives) the genuine obstruction must vanish, since a diffeomorphism direction cannot obstruct. A raw pairing that gives $-\pi^2/18$ for all four modes therefore is *not* gauge‑invariant, and the entire discriminating content — separating the 2 gauge modes from the 2 conformal modes — lives in the slice/gauge projection that has not been performed. The "unit test" status is not merely cautious; the equal‑across‑gauge value is direct evidence that the projection is mandatory before any number is physical.

**(b) It uses raw product‑coordinate quadratic jets**, whereas Prop 2.10 assumes $H^4$ and $\mathbf v_l$ in Bianchi gauge with respect to the flat model and the eigenspace‑orthogonality that makes only $V_{l,2}$ (not $V_{l,0}$) contribute. Until $V_{l,2}$ is the Bianchi‑gauged normal‑coordinate jet, the coefficient is convention‑bound.

The equal‑scale node‑sign cancellation ($\sum u_i$ signs $=0$) is a genuine and useful feature, correctly identified as fragile under unequal scales, mixed chirality, the slice, and Green transport.

## 7. Two upstream mathematical points not yet settled

**(i) Integrability of the two non‑gauge conformal modes.** Ozuch's finite‑dimensional reduction is built for orbifolds with *integrable* Einstein deformations (Def 1.10): each $v\in\mathbf O(g_o)$ integrates to an actual Einstein metric $g_v$. The gauge modes trivially integrate (pullbacks). But $u_1g_2,u_2g_1$ are conformal directions, and the product is TT‑rigid, so it is not established that these integrate to Einstein metrics. If the second‑order Kuranishi obstruction $\pi_{\mathbf O}Q^{(2)}(v,v)$ is nonzero for these, then Def 1.10 does not hold as stated and the Kuranishi obstruction among kernel modes must enter the finite‑dimensional system directly. This is upstream of the $H_{ij,2}$ computation and should be settled first, because it decides whether the orbifold‑side variables are $\{$node parameters$\}$ alone or $\{$node parameters $+$ conformal moduli$\}$.

**(ii) Whether the TT quadrupole excites the conformal kernel at all.** Prop 2.10's mechanism is eigenspace orthogonality on $S^3/\mathbb Z_2$: $H^4$ (a quadrupole) is orthogonal to $V_{l,0}$ (which sits in the $\ell=1$ Laplace eigenspace). The natural analogue here is that the EH TT quadrupole may be orthogonal to the *genuine* (Bianchi‑gauged, non‑gauge) conformal modes by parity/representation type. If it is, the orbifold‑side $\nu_l$ obstruction is absent and the whole question collapses onto the node‑side $\lambda,\mu$ with the $H_{ij,2}$ correction. If it is not, there is a genuine conformal obstruction. **This single pairing — TT quadrupole against the Bianchi‑gauged jets of the 2 non‑gauge modes — is the cheapest computation that would resolve the gauge worry in (a) and largely settle (i)–(ii).** It is far cheaper than the full Green transport and would change the judgment about what the coupled system contains.

## 8. Most useful next executable computation for $H_{ij,2}$

$S^2\times S^2$ is homogeneous ($SO(3)\times SO(3)$ transitive), so $G_P^\perp$ diagonalizes in factorized tensor spherical harmonics. Concretely:

1. Assemble the spectrum of $P_o=\tfrac12\nabla^*\nabla-\mathring R$ on $\mathbb Z_2$‑invariant $\operatorname{Sym}^2$ from the factor tensor/vector/scalar harmonics (Kröncke Prop 4.1/4.8 give the product formulas; A02 already fixed the convention). Verify against the unit test $P h_{\text{rel}}=-\Lambda h_{\text{rel}}$ and the four zero modes.
2. Represent the EH quadrupole source $H^4(\zeta_j)=-\dfrac{\rho(\zeta)^-\circ\zeta^+}{2r^4}$, localized at $p_j$, in this basis.
3. Apply $G_P^\perp$: invert $P_o$ off the 4‑dimensional scalar kernel, imposing $B_o\bar h_j^4=0$ (as in Ozuch's flat‑case eq. (60)–(62), where the periodized extension is divergence‑ and trace‑free and orthogonal to $\mathbf O$).
4. Expand the regular part at each other node $p_i$ and extract the quadratic Hessian jet $H_{ij,2}=\tfrac12 D^2_{p_i}[\bar h_j^4]$.
5. Form the corrected block $R^+\!\big(H_{j,2}+\sum_{i\neq j}H_{ij,2}\big)$ and test whether the rank‑one Kähler structure survives, i.e. whether $\mu_1$ of the corrected block stays zero as a function of scales $t_j$ and in‑kernel angles.

By homogeneity plus the reflection, only **two** independent inter‑node relations exist — adjacent (nodes differing in one factor) and opposite (differing in both) — so the decisive data is a small finite set of second‑jet coefficients between polar fixed points, obtainable in nearly closed form from the factorized spectrum. Anchors: the reflection must yield $r=1\sim r=3$; equal‑scale symmetric sums must reproduce the node‑sign cancellation; the $-\Lambda$ eigenvalue must appear in the spectrum.

## 9. Net assessment of correctness

I found no computational error in the Step 77 note or the two data files. Every checked identity ($P(u_ig_j)=0$, the Bianchi coefficients, the TT‑vanishing forcing, $Ph_{\text{rel}}=-\Lambda h_{\text{rel}}$, $R^\pm=\operatorname{diag}(\Lambda,0,0)$, $\lambda_k=0$, $\mu_1=0$, $b_2=6$, $\tau=2k-4$, Q0.8 being Ricci‑flat) is correct. The two items that remain genuinely open and are logically prior to the Green transport are the integrability status of the two non‑gauge conformal kernel modes and whether the TT quadrupole pairs nontrivially with them after Bianchi gauge‑fixing; the cheap pairing test in §7 resolves both and should precede the full $H_{ij,2}$ evaluation in §8.