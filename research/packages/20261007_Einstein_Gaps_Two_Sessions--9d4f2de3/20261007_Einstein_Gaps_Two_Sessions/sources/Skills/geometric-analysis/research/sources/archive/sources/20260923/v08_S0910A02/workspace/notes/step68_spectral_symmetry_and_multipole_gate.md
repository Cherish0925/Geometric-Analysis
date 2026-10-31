# Step 68: spectral, symmetry, and multipole gates for the mixed A1 obstruction computation

## Purpose

The previous Step-67 handoff proposed computing the finite-dimensional Ozuch obstruction for mixed Eguchi--Hanson (EH) patterns on
\[(S^2\times S^2)/\mathbb Z_2,\]
with four isolated \(A_1\) points.  The current step does **not** compute the final mixed obstruction coefficients.  It fixes the gates that must be correct before such a computation can mean anything:

1. local orientation-independence must be proved by an actual isometry, not inferred from the quadratic jet;
2. the global reflection symmetry must be used as a bug detector for sign-pattern computations;
3. the product Einstein operator convention and kernel must be settled before using any Green operator;
4. the distant-bubble coupling is a second-jet/multipole object, not a value Green's-function sum.

These are still intermediate facts for the Yau--26 target.  A nonzero mixed obstruction would only rule out Einstein metrics near this degeneration and would not refute \(P_4^+\).  A vanishing obstruction plus transversality would be the valuable branch, because it could produce positive Einstein metrics on mixed rows.

## 1. Orientation-independence: reflection proof

Let the product orbifold be formed using the specified order-two rotation on each \(S^2\) factor, with fixed points \((N,N),(N,S),(S,N),(S,S)\).  In complex coordinates on each \(\mathbb P^1\), write the quotient rotation as
\[\rho(z,w)=(-z,-w).\]
The map
\[c(z,w)=(\overline z,w)\]
is an isometry of the product metric, reverses the orientation of the first \(S^2\) factor and hence of the product, and commutes with the quotient rotation because
\[c\rho(z,w)=(-\overline z,-w)=\rho c(z,w).\]
It fixes \(0\) and \(\infty\) on the first factor, and the identity fixes the second factor, so it fixes all four orbifold nodes.

Thus \(c\) descends to an orientation-reversing isometry of the orbifold which fixes every node and exchanges \(\Lambda^+\) and \(\Lambda^-\) at each node (up to harmless basis signs).  Pulling back a compatible EH datum by \(c\) gives the reversed EH datum for the same metric germ.  Because the whole germ, not just \(H_2\), is carried isometrically, the single-node obstruction tower is orientation-independent at every order.  This is the rigorous replacement for Step 67's weaker inference from the equality of the ambient quadratic tensor.

Consequence: local obstruction functions for one isolated node cannot distinguish compatible from reversed.  Any mixed-pattern difference must come from inter-node coupling.

## 2. Global sign-pattern symmetry

The same reflection sends the set \(S\) of reversed nodes to its complement \(S^c\).  Therefore:

- \(r=0\) and \(r=4\) are isometric/conjugate cases and are solvable by the known del Pezzo/Kähler--Einstein control row;
- \(r=1\) and \(r=3\) are equivalent cases;
- \(r=2\) maps to \(r=2\) with \(S\leftrightarrow S^c\), while adjacent/diagonal seam classes may still have to be distinguished by the gluing-map/spin ledger rather than by node count alone.

Any coefficient computation that gives different solvability for \(r=1\) and \(r=3\) has a symmetry bug.  The node-level orbit ledger is recorded in `workspace/data/step68_product_spectrum_and_symmetry.json`.

## 3. Einstein-operator convention and kernel

The source convention matters.  Ozuch defines, for an Einstein background \(\mathrm{Ric}=\Lambda g\), the gauged linear operator
\[P_g=\frac12\nabla^*\nabla-\mathring R,\]
where \(\mathring R\) acts on symmetric two-tensors; see Ozuch arXiv:2012.13316, lines 243--250.  LeBrun--Ozuch similarly state that on TT tensors the linearization reduces to
\[P_g=\frac12\nabla^*\nabla-\mathring{\mathcal R}\]
(lines 254--263 of arXiv:2601.19215 in the local Knowledge representation).  Kröncke's Einstein operator is
\[\Delta_E=\nabla^*\nabla-2\mathring R=2P_g\]
with product-spectrum formulas in Proposition 4.1 and positive-product formulas in Proposition 4.8/Remark 4.9.

For \(S^2(\Lambda)\times S^2(\Lambda)\), the parallel relative factor-scaling tensor
\[h_{\rm rel}=g_1-g_2\]
is trace-free, divergence-free, and quotient-invariant.  Since \(\mathring R h_{\rm rel}=\Lambda h_{\rm rel}\),
\[P_g h_{\rm rel}=-\Lambda h_{\rm rel},\qquad \Delta_E h_{\rm rel}=-2\Lambda h_{\rm rel}.\]
Thus the product is a saddle, but the unstable mode is bounded away from zero.  In the Ozuch convention the unit-test eigenvalue is \(-\Lambda\), not \(-4\Lambda\); a \(-4\Lambda\) statement is a different normalization and should not be used to test Ozuch-code coefficients.

The TT kernel on the quotient is zero.  The reason is specific to the \(S^2\times S^2\) case and should not be read directly from positive-product formulas that assume non-spherical decompositions.  On a round \(S^2\), the scalar eigenvalue \(2\Lambda\) is the \(l=1\) eigenspace and satisfies
\[\nabla^2 f=-\Lambda f g_{S^2}.\]
For a scalar-sector candidate with \(f\) on one factor,
\[h=A f g_1+B f g_2+C\nabla^2 f=(A-C\Lambda)f g_1+B f g_2.
\]
Trace-free gives \((A-C\Lambda)+B=0\), while divergence-free gives \(A-C\Lambda=0\), hence \(B=0\).  The scalar \(l=1\) full-kernel modes therefore do not contribute TT tensors.  Each factor has no TT Einstein deformations, and the mixed one-form sector is positive.  Therefore a quotient TT kernel would lift to zero on the cover, so
\[\ker(P|_{TT})=0\quad\text{on }(S^2\times S^2)/\mathbb Z_2.
\]

There is, however, an important full-gauged-kernel nuance.  On the orbifold quotient, the \(\lambda=2\Lambda\) invariant scalar multiplicity is two (the axial first harmonic on either factor), and the full operator \(P\) kills both \(f g_1\) and \(f g_2\) for each such invariant \(f\).  Thus the **full** \(P\)-kernel has a four-dimensional scalar/conformal/automorphism-type sector, while the TT infinitesimal Einstein deformation space is zero.  A faithful Ozuch implementation must either fix these non-TT directions by a slice/normalization or include the corresponding \(v_l\) and projection terms until they are proved harmless.  The spectral facts are recorded in `workspace/data/step68_orbifold_kernel_full_vs_tt.json`.

This is favorable for the analytic near-pinching/certificate track: there is no small TT eigenvalue amplification.  But it is not yet the full compact inverse theorem, because the finite-dimensional non-TT gauged kernel has to be handled correctly.

## 4. Correct distant-bubble coupling object

The Step-67 placeholder coupling matrix based on node distances and a bare Green value is not the Ozuch obstruction coefficient.  The source makes the correct object explicit in the torus model.  Ozuch constructs, for a source node \(i\), a tensor \(\bar h^4(\zeta_i)\) satisfying
\[P_{g_\infty}\bar h^4=0,\quad B_{g_\infty}\bar h^4=0,\quad \bar h^4\sim H^4(\zeta_i)\]
near \(p_i\), with singular-part subtraction/orthogonality; see especially lines 888--905 of arXiv:2012.13316.  At a different node \(p_j\), the expansion is
\[\bar h^4(\zeta_i)=H_{ij,0}+H_{ij,2}+O(r_j^4),\]
and the curvature modification at \(p_j\) is determined by the second jet \(H_{ij,2}\), after removing the constant term by the appropriate linear map \(\phi_j\).

Therefore the desired coefficient is schematically
\[H_{ij,2}=\frac12 D_{p_j}^2\left[G_P^{\perp}(\text{TT quadrupole }H^4(\zeta_i)\text{ at }p_i)\right],\]
not
\[\sum_\alpha \frac{\psi_\alpha(p_i)\psi_\alpha(p_j)}{\lambda_\alpha}.
\]
A spectral implementation must contract the source multipole at \(p_i\) with the eigenfunction/tensor derivatives representing that multipole, and then take the second derivatives at \(p_j\), with kernel projection and Bianchi gauge.  A value-only harmonic sum computes a different Green object and would produce numbers that should not be interpreted as obstruction coefficients.

## 5. What this step changes

The Step-67 line is not abandoned, but it is narrowed and made safer:

- The local orientation-independence claim is now a proof by the orientation-reversing product reflection, not a jet-truncation inference.
- Mixed obstruction computations have two independent sign counts, not three: \(r=1\sim r=3\), and \(r=2\) possibly split by adjacent/diagonal seam data.
- The TT kernel/invertibility gate is favorable: \(\ker(P|_{TT})=0\) and the relative product mode is a bounded negative eigenvalue, not a small one.
- The full gauged operator still has a scalar sector that a rigorous Ozuch computation must slice away or include.
- The queued finite computation must be reformulated as a multipole-to-second-jet calculation.  The old distance/value coupling matrix remains only a qualitative symmetry ledger.

No branch of Yau--26 is proved or refuted here.  The most valuable next execution is either (a) implement the correct multipole-to-second-jet Green calculation in a symmetry-reduced tensor harmonic basis, using the above unit tests; or (b) turn the invertibility/slice statement into a compact analytic lemma adapting Biquard/Ozuch Section 4 to four isolated \(A_1\) points with mixed first-obstruction-killed inserts.  A nonzero mixed coefficient would be only a local degeneration obstruction; a zero coefficient would justify pushing toward transversality and genuine positive-Einstein existence on a mixed row.
