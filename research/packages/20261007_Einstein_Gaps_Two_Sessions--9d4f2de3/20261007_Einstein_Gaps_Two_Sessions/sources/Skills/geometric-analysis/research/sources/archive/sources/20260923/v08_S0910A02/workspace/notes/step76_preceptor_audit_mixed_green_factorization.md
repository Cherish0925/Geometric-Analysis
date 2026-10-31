# Step 76: Preceptor audit of the mixed-row Green computation gates

Session `S0910A02`. Agent4 / Preceptor. Phase Execute.

This note audits the Step-75 executable ledger before the project invests again in the \((S^2\times S^2)/\mathbb Z_2\) mixed-row Green-response and finite-dimensional obstruction computation.  It also checks the Strategist's proposed product-Green shortcut against the actual product operator structure.  A post-TTCS/A01 correction at the end supersedes any remaining shorthand that calls the inter-node Green response simply "the second obstruction".

## 0. Scope relative to Yau--26

The active target remains the full Yau Problem 26 proposition for every closed connected smooth manifold in every dimension.  The mixed-row calculation is **not** a proof or refutation of that proposition.  Its correct role is local and diagnostic:

- If the sliced finite-dimensional obstruction system beginning with the bare local \(\mu\)-terms and the multipole-to-curvature interaction maps vanishes (and the appropriate transversality/slice hypotheses can then be proved), this supplies evidence for a nearby-orbifold Einstein construction on the product-quotient test geometry.
- If the resulting map is nonzero with no zero over the allowed scales/angles/slice variables, it rules out that local nearby-orbifold route for those rows, but it does **not** prove that the underlying PSC, finite-\(\pi_1\), strict-Hitchin--Thorpe smooth manifolds carry no Einstein metric far from the orbifold degeneration.
- Step 74's tower-impossibility result remains the guardrail: small unweighted Ricci-operator defect sees the first obstruction but is structurally blind to higher obstruction orders.  A second-obstruction computation can test tower-rigidity in this product geometry, not establish it in general.

I repaired the remaining overstatement in `workspace/notes/step74_ell_classification_tower_impossibility_and_hardness_propagation.md`: its summary row no longer says "n>=6 follows from n=4".  It now says only that specific near-pinched product families propagate to n>=6; this is a bottleneck/family test, not a universal implication \(P_4^+\Rightarrow P_n^+\).

## 1. Source-pinned audit of the Ozuch object

The relevant source is Ozuch, `Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics.../object.md`.

1. Lines 608--612 define the object: for a chosen singular point and a homogeneous asymptotic tensor \(H^4(\zeta^\pm)\), one solves
   \[
   P_o\bar h^4=\sum_l\nu_l v_l+\sum_k\lambda_k\bar o_k^4,
   \qquad
   \bar h^4=H^4+H_2^4+O(r^{-\epsilon})
   \]
   at that singular point, with orthogonality to the orbifold kernel.  Thus the singular asymptotic belongs to the **source/self node**.
2. Lines 640--646 state the multi-singularity version as a sum of these source extensions, again with kernel and obstruction projections.
3. Lines 903--905, in the torus model, state exactly the inter-node regular expansion: at a different singular point \(i\),
   \[
   \sum_{i'\ne i}\bar h^4(\zeta_{i'}^\pm)=H_0(i)+H_2(i)+O(d(i,\cdot)^4).
   \]
   This confirms that for \(j\ne i\) there is no receiver singular part to subtract; the target data are the constant part to be normalized away and the second jet \(H_2(i)\).
4. Lines 770--807 give the obstruction equation for actual nearby Einstein metrics:
   \[
   t_j\lambda_k^j+t_j^2\mu_k^j=O(t_{\max}^{5/2}).
   \]
   In the product quotient the first obstruction vanishes for EH directions in \(\ker R_\pm\), because \(R_\pm=\operatorname{diag}(\Lambda,0,0)\) has a two-dimensional kernel.  The displayed determinant formula also gives the bare radial \(\mu_1\) for the rank-one product block, but it does not by itself establish the transverse \(\mu_2,\mu_3\) or the scalar-kernel-projected equations.  Inter-node regular jets change the receiver's effective curvature block and hence its first obstruction at a later scale; the desired local diagnostic is therefore the full sliced multipole-to-curvature interaction system, not merely a \(\mu\)-coefficient.

This supports the Step-68/75 correction: the coefficient is a multipole-to-second-jet Green transport, not a node-value Green matrix.  It also supports the Strategist's point that inter-node evaluations are regular.  However, regularity is not the same as factorization into one-factor Green functions.

## 2. Audit of the Step-75 ledgers

### 2.1 D8 pattern reduction

`workspace/data/step75_symmetry_selection_collapse.json` and its script correctly implement the node grid
\[
(N,N),(N,S),(S,N),(S,S)
\]
as a \(2\times2\) square.  Row flip, column flip, and factor swap generate the full orientation-preserving \(D_8\) of size 8 on the four nodes.  The pattern ledger is sound:

- \(r=1\) has no complementer by cardinality and is not self-conjugate after composing with the chirality-exchanging reflection \(c(z,w)=(\bar z,w)\).
- \(r=3\) is the complement/reflection companion of \(r=1\), not an independent computation.
- Adjacent \(r=2\) has stabilizer size 2 and complementers.
- Diagonal \(r=2\) has stabilizer size 4 and complementers, hence gives the strongest internal bug-check.

The next coefficient computation should therefore have exactly three independent pattern classes: \(r=1\sim r=3\), adjacent \(r=2\), and diagonal \(r=2\).

### 2.2 Chirality sign matrices

The local sign matrices in the Step-75 script are acceptable as **basis-convention bug checks**, not invariant numerical coefficients.  The invariant content to preserve is: row/column flips may be taken as identity after transporting oriented pole frames; factor swap is orientation-preserving and acts nontrivially on the kernel planes; \(c\) reverses orientation and exchanges \(\Lambda^+\) and \(\Lambda^-\).  Any later code may choose a different kernel basis, but it must conjugate these matrices consistently and must still make \(r=1\) and \(r=3\) agree.

### 2.3 Spin-row identification

The script's product spin-lift computation is a strong canonical-model argument.  On each \(\mathbb{CP}^1\), the half-turn has opposite spin-lift signs at north and south; multiplying the two factors gives signs
\[
(+,-,-,+)
\]
up to a global sign.  Combined with the Step-64 seam rule, this identifies the distinguished opposite-sign pair as diagonal.  Therefore the working identification is:

- diagonal balanced \(r=2\): spin row, homeomorphic to \(\#_3(S^2\times S^2)\);
- adjacent balanced \(r=2\): nonspin row, homeomorphic to \(3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2\).

This is not yet a source-pinned topological theorem: it depends on the canonical product lift and the Step-64 boundary-spin convention.  It is safe for choosing which computation to prioritize and for internal consistency checks, but a final theorem should still audit it by an independent Kirby/boundary-spin or source-pinned argument.

### 2.4 \(T^2\)-selection rule

The Step-75 \(T^2\)-selection rule is sound but should not be oversold.  A value/first/second jet at a pole only sees weights \(|m_a|\le2\), the quotient half-turn imposes \(m_1+m_2\) even, and the EH kernel-product block has the four characters
\[
(\pm2,0),\qquad (0,\pm2).
\]
This removes irrelevant tensor channels.  It does **not** truncate the spherical degree \(l_a\).  For example the one-factor pole second derivative in the \(|m|=2\) scalar analogue has
\[
P_l''(1)=\frac{(l+2)(l+1)l(l-1)}{8}\ne0\qquad(l\ge2),
\]
so every \(l\ge2\) remains present in that character channel.  This is recorded in `workspace/data/step76_product_green_factorization_audit.json`.

## 3. Product Green factorization audit

The Strategist is right about one important simplification and too optimistic about another.

### 3.1 What is correct

Adjacent and diagonal inter-node transport is regular in the full four-dimensional product:

- diagonal example \((N,N)\to(S,S)\): antipodal in both factors, regular in both factors, parity schematic \((-1)^{l_1+l_2}\);
- adjacent example \((N,N)\to(N,S)\): coincident in the first factor and antipodal in the second, but the full product points are still separated by distance \(\pi\), so the four-dimensional Green kernel is smooth at the receiver.

Thus singular subtraction is a source/self-node issue, not an inter-node issue.  The diagonal spin case is indeed the cleanest first calibration because it is regular in both factors and has the larger \(D_8\) stabilizer.

### 3.2 What is not justified

The inverse of a product Einstein operator does not literally equal a product of two ordinary \(S^2\) Green functions.  After separation of variables, a product-type operator has coefficients of the form
\[
\frac{1}{\lambda_{l_1}+\lambda_{l_2}+\kappa_{\text{tensor}}},
\]
not
\[
\frac{C}{(\lambda_{l_1}+a)(\lambda_{l_2}+b)}.
\]
The symbolic obstruction is the unavoidable \(xy\) term in
\[
(x+a)(y+b)-C(x+y+\kappa),
\]
whose coefficient is 1.  The scalar unit tests in `workspace/data/step76_product_green_factorization_audit.json` show equality only when one factor has the zero mode; for example with shift 1,
\[
(l_1,l_2)=(1,1):\quad 1/(2+2+1)=1/5\ne1/9=(1/(2+1))^2.
\]
Tensor curvature terms change the finite algebraic shifts and mix a finite number of tensor components; they do not turn the inverse of a sum into a product inverse.

A legitimate factor reduction is narrower: if the source/receiver contraction projects one factor to a fixed eigenspace/eigenvalue, then the other factor solves a **massive one-factor Green problem** with shift \(\lambda_{\rm fixed}+\kappa_{\rm tensor}\).  Equivalently, on the positive spectral part a heat-kernel representation factorizes before integrating in time, but the current Ozuch operator has negative and zero modes.  The safe formula is a projected pseudo-inverse: negative modes are added as \(\sigma^{-1}\Pi_\sigma\), zero modes are removed or retained as finite-dimensional \(\nu_l\) equations, and only the strictly positive spectral part is integrated.  The final resolvent is not a pointwise product of two static Green functions.

### 3.3 Consequence for the next computation

The closed-form strategy is still promising, but it must be formulated as one of:

1. a separated spectral/resolvent sum with additive denominators, followed by exact Legendre/parity summation or certified tail bounds;
2. a heat-kernel integral using the product heat kernel and then evaluating pole jets;
3. a finite matrix of massive one-factor Green functions after proving one factor is restricted to fixed eigenmodes by the tensor/source contraction.

It should **not** multiply a singular one-factor Green at a coincident pole by an antipodal one-factor Green.  In the adjacent case, the coincident factor is harmless only in the full product resolvent; treated separately it creates a fake singularity.

## 4. Completion standard before the next construction

A Step 77/78 computation should be treated as complete only if it outputs the following, or explicitly proves why a listed item is unnecessary:

1. For each independent pattern class \(r=1\sim r=3\), adjacent \(r=2\), and diagonal \(r=2\), coefficient and interaction maps at every node and for every \(\zeta\in\ker(R_\pm)\) in a fixed kernel basis, with the expansion order explicitly identified.
2. The inter-node contribution computed from the full product \(P\)-Green/resolvent, heat-kernel formula, or a proved equivalent massive one-factor reduction, not from a naive product of two massless \(S^2\) Green functions.
3. Source singular renormalization at the source/self node only; no receiver singular subtraction for \(j\ne i\).  At receivers, extract \(H_0\), apply the \(\phi_j\) normalization, then extract \(H_{ij,2}\).
4. The four non-TT scalar full-gauged kernel directions from Step 68 must be sliced by an explicitly derived Bianchi/diffeomorphism normalization or included as Ozuch \(v_l\) variables/projections.  Orthogonality of the solution fixes a pseudo-inverse; it does not by itself prove the source projection coefficients \(\nu_l\) vanish.  A TT-only computation is not a faithful Ozuch coefficient.
5. Symmetry tests must pass: \(r=1\) equals \(r=3\) under complement/reflection; both balanced patterns satisfy their self-conjugacy constraints; diagonal \(r=2\) obeys the larger stabilizer.
6. If no closed form is achieved, a certified tail bound for the remaining alternating/resolvent series is part of the result.  A raw truncated spectral sum is not enough to decide vanishing/nonvanishing.

## 5. Collapse correction

Step 75's collapse correction is sound.  Positive pinching with \(\chi>0\) and \(\operatorname{Vol}\to0\) forces curvature concentration, but it does not rule out inner ALE bubbles: at a curvature scale \(r_i=|\mathrm{Rm}(x_i)|^{-1/2}\), fixed-radius rescaled ALE balls have positive Euclidean volume ratio while their original volumes are \(O(r_i^4)\).  Bishop--Gromov allows the ratio to drop on larger scales.  Therefore the collapse branch needs an outermost concentration/transition theorem or a controlled annulus carrying Euclidean volume ratio to ambient scale.  ALF/ALG/ALH/APS accounting is central; ADE arithmetic remains only an inner-bubble diagnostic.

## 6. Resulting route judgment

The Step-75 D8 reduction, spin working identification, and \(T^2\) character rule are reliable enough to guide the next construction.  The Strategist's regularity simplification should be used, but the proposed "closed-form factor Green functions" must be interpreted through the additive product resolvent or heat-kernel representation.  The next highest-value execution is not another generic Green-program note: it is a reduced diagonal \(r=2\) calibration calculation for the spin pattern, because it has two antipodal factors, no receiver singularity, the larger stabilizer, and the strongest topology link to \(\#_3(S^2\times S^2)\).  If the diagonal calibration exposes unresolved tensor-block/gauge issues, those should be repaired before adjacent and \(r=1\) cases are attempted.

No branch of Yau--26 is proved, refuted, or Lean-formalized by this audit.


## 7. Post-TTCS and A01 Step-77 correction: do not call the inter-node map `mu`

After the first version of this note, TTCS verification (`trace/ttcs/results/step76_ttcs01_verifier1_integration.md`) and A01's corrected Step-77 note (`Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md`) identified a material naming and order issue.

### 7.1 Full kernel versus TT kernel

A01's first Step-76 peer message briefly claimed `O(g_o)=0` and `nu_l` empty, but A01 withdrew that in message #521.  The corrected statement agrees with A02/TTCS:
\[
\ker(P|_{TT})=0,
\qquad
\ker_{L^2}P\supset \operatorname{span}\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}.
\]
Here \(u_a\) are axial first harmonics on the two round factors and descend under the half-turn.  The Bianchi calculation in A01's `step77_slice_decomposition_verify.json` records
\[
B(a u_1g_1+b u_1g_2)=b\,du_1,
\qquad
B(c u_2g_1+d u_2g_2)=c\,du_2,
\]
and the Bianchi-surviving same-factor modes are pure gauge via \(\mathcal L_{\nabla u_a}g=-2\Lambda u_ag_a\).  This explains why there is no genuine TT Einstein deformation while also confirming that Ozuch's full \(\nu_l\) projections cannot be deleted unless a reduced slice and its compatibility equations are explicitly derived.

### 7.2 Order bookkeeping

The inter-node regular jet from source \(i\) at receiver \(j\) has size \(O(t_i^2)\), since \(H^4(t_i\phi_i)=t_i^2H^4(\phi_i)\).  It changes the receiver first obstruction by
\[
\delta\lambda_{j,k}=t_i^2\mathcal I_{ji,k}+o(t_i^2),
\]
so in Ozuch's finite-dimensional equation it appears as
\[
 t_j\delta\lambda_{j,k}=t_jt_i^2\mathcal I_{ji,k}+\cdots .
\]
For equal scales this is order \(t^3\), not the local order-\(t^2\) coefficient \(\mu_{j,k}\) in Ozuch's notation.  The next computation should therefore be named a **sliced multipole-to-curvature interaction map** (or Green-response map), not simply "the second obstruction".  The bare local determinant formula gives \(\mu^{(0)}_{j,1}=0\) for the rank-one product block; it does not establish \(\mu_{2,3}\) after effective jets, scalar projections, and normalization.

### 7.3 Strengthened next-computation requirements

Add to the completion standard:

7. Include the \(\Lambda>0\) cosmological source in Ozuch equations (20)--(23), especially the \(\Lambda\,\mathrm{eh}\) contribution to the local \(\underline h_2\).  Do not import the \(\Lambda=0\) torus simplifications into the positive product quotient.
8. Track Kröncke/Ozuch spectral sectors separately: symmetric 2-tensor lifts from each factor, mixed one-form sectors, scalar/gauge blocks, negative modes, and the four full-kernel projections.  The product resolvent denominator is additive in every sector, but the finite tensor matrices and curvature shifts differ.
9. Output the actual obstruction expansion being tested, for example
\[
F_{j,k}=t_j\lambda^{(0)}_{j,k}+t_j^2\mu^{(0)}_{j,k}
 +\sum_{i\ne j}t_jt_i^2\mathcal I_{ji,k}+\cdots,
\]
and state which coefficient the code computes.  A raw value for \(\mathcal I\) at a symmetric parameter point is not a proof that a row has no local Einstein desingularization; one must solve or exclude zeros over the allowed scales, kernel angles, chirality pattern, and slice variables.

This correction strengthens, rather than weakens, the route judgment: the D8/diagonal-spin/regular-inter-node gates remain useful, but the next diagonal calculation must compute the **full sliced Green-response system with order bookkeeping**, not a misnamed finite `mu` table.
