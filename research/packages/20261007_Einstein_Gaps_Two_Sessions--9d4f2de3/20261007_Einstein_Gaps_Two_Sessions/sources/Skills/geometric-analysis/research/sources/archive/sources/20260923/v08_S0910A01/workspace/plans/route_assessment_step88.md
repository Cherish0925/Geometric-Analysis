# Route assessment: Step 88 corrected by Step 89

The valid Step 88 advance is the **axial four-node source structure** for the product orbifold
\((S^2\times S^2)/\mathbb Z_2\).  For the axial mode
\(h=(*dZ_A)\odot(*dZ_B)\), the node sign vector is
\[
s=(+1,-1,-1,+1)
\]
in node order \((NN,NS,SN,SS)\), matching the diagonal mixed chirality assignment.  Thus the axial \(\lambda=1\), \(V_2\)-boundary source reinforces for the mixed assignment and cancels for the equal-scale all-same assignment.  This is a real structural distinction between the two fillings.

The Step 88 conclusion that the full chirality-odd Green interaction is unconditionally positive is **withdrawn**.  Two corrections are load-bearing:

1. The product Lichnerowicz operator is not positive on all TT tensors: the parallel shape tensor
\[
q=g_A-g_B
\]
is TT and satisfies \(Pq=-q\) in the unit-sphere normalization.  The Step 89 computation shows the principal odd source annihilates this mode, but the complete geometric source still requires a slice-level proof.

2. Point-supported quadrupole source pairings have singular self-terms.  A regularized self-pairing matrix may be nonnegative before singular subtraction, but deleting the diagonal/self-parametrix does not preserve positivity.  The finite odd--odd object should be a relative mixed--all-same comparison using the same regularization, local normalization, and scale variables.  In Ozuch radial weights it has the form
\[
\Delta^{11}(\tau)=\sum_{i,j}a_i b_j(\epsilon_i\epsilon_j-1)K_{ij}^{11}(\tau),
\qquad a_i=t_i,\quad b_j=t_j^2,
\]
not the symmetric energy weight \(w_iw_j\) if one wants the radial \(O(t^3)\) order.  Its odd--odd diagonal terms vanish identically because \(\epsilon_i^2=1\).  The sign and value of the off-diagonal limit must be derived; they are not inherited from a sum-of-squares formula, and even--odd diagonal terms require separate symmetry or matched subtraction.

Step 89 also corrects the flat principal source--receiver normalization.  With
\(H_{ijpq}=\partial_p\partial_qh_{ij}(0)\) and \(V_2=\frac12H_{ijpq}x_px_q\), the exact identity is
\[
S_{\rm odd}(V_2)=\frac{\pi^2}{2}R_{\rm odd}(H),
\qquad D:H=-16R_{\rm odd}(H),
\]
verified symbolically on the full 100-dimensional basis in
`workspace/scripts/step89_identity_and_spectral_support.py` and
`workspace/data/step89_identity_and_spectral_support.json`.  This supports a leading adjoint-source/receiver formulation, but it does not incorporate curved-parametrix terms, constant-jet/frame corrections, gauge projection, or Ozuch radial normalization.

## Current route status

### Positive mixed-row desingularization
- Valid: axial low mode distinguishes mixed from equal-scale all-same at the source-projection level.
- Valid: flat principal source--receiver identity with corrected factor \(\pi^2/2\).
- Open: complete spectral support of the full geometric source, including negative shape and scalar zero modes after Bianchi/cutoff/radial normalization.
- Open: finite regularized relative mixed--all-same interaction, including even--odd cross terms unless symmetry removes them.
- Open: relation to the actual radial equation.  The inter-node layer is \(O(t^3)\), which is smaller than Ozuch Proposition 2.19's \(O(t_{\max}^{5/2})\) necessary estimate; a sharper projected expansion is needed.

### Restricted IL negative branch
- Still the strongest scope-relevant Yau--26 asset: a repaired but not publication-certified negative-branch gap for the restricted Ishida--LeBrun geography.
- It remains separate from the product-orbifold local desingularization calculation and from the full sign-unrestricted, all-dimensional Yau--26 proposition.

### Graph and higher-dimensional routes
- No current branch supplies a full proof or disproof of Yau--26.
- A03's graph work remains a negative-sign laboratory with unresolved full OT/connector behavior.
- Product propagation to higher dimensions remains conditional on resolving a four-dimensional positive branch and does not cover dimension five.

## Strongest next work

1. Turn the Step 89 flat identity into a clean analytic derivation, including the exact factor and conventions.
2. Prove or disprove that the **full geometric** chirality-odd source annihilates the negative shape mode and scalar zero modes after Bianchi correction and cutoff/source subtraction.
3. Derive the matched finite relative interaction \(\Delta\) for mixed minus all-same configurations with Ozuch radial weights \(a_i=t_i,b_j=t_j^2\), preserving even/odd cross terms and taking the same regularization before the limit.
4. Match any resulting coefficient to Ozuch's radial variables only after the scale, EH direction, gauge, and local normalizations are fixed.
