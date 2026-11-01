# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step96_corrected_selection_and_determinantal.md",
    "Sessions/S0910A02/workspace/notes/step94_three_gates_and_highdim_theorem.md",
    "Sessions/S0910A02/workspace/data/step97_gradient_quartic_audit.json",
    "Sessions/S0910A01/workspace/notes/step97_ab_physical_cone_interpretation.md",
    "Knowledge/objects/papers/Smoothing-singular-extremal-Kähler-surfaces-and-minimal-Lagrangians--76bcf086d1fb--80cf6934cc4e/object.md",
    "Knowledge/objects/papers/COMPACT-MODULI-SPACES-OF-DEL-PEZZO-SURFACES--3cb2439eac00--b970fe5e4bdb/object.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md"
  ]
}
```

## Task

Critically verify the revised positive Gate-3 calibration for the Yau 26 project. The claim to assess is: for the four-A1 quotient (P^1 x P^1)/Z2 in the degree-4 del Pezzo KE compactification, the compatible Kähler smoothing directions correspond to Eguchi-Hanson periods in the kernel planes orthogonal to the local Kähler form, while the excluded holomorphic resolution direction is the Kähler exceptional-curve direction. Therefore the full Lyapunov-Schmidt reduced Einstein obstruction, viewed as the gradient of a normalized Einstein-Hilbert/scalar-curvature functional after solving the complement in a suitable slice, should have its leading quartic f4 vanish on the compatible KE smoothing locus. In particular, same-chirality self and pair coefficients should vanish in the full calibrated LS potential; partial raw spectral sectors such as the AB coefficient need not vanish alone but must cancel after all sectors and coordinate/complement/global corrections. Please check what is actually supported by the supplied sources, what assumptions about gauge/slice/coordinates/automorphisms are needed, and what should not be claimed. Also judge whether the old Gate-3 criterion |q_diag| versus |2q_adj+q_diag| must be replaced by a calibrated real quartic on physical scale/phase/global-deformation variables, and whether local obstruction can or cannot imply global no-Einstein for Yau 26.

## Output

## Verification memo: revised third-stage coefficient calibration at the four‑A₁ del Pezzo quotient

I checked the geometric identification, the variational/quartic reformulation, and the local‑versus‑global relevance against OSS (doi:10.4310/jdg/1452002879), Biquard–Rollin (arxiv:1211.6957), Ozuch (arxiv:2012.13316), and the internal files (step94/96 notes, `step97_gradient_quartic_audit.json`, A01 `step97_ab_physical_cone`). The picture separates cleanly into parts that are well grounded, one part that is stated more strongly than the sources or your own corrected framework allow, and one part (the Yau‑26 relevance) that the sources contradict.

### 1. The smoothing/resolution identification is sound and source‑grounded

The statement that the compatible Kähler smoothing directions are Eguchi–Hanson periods in the kernel planes orthogonal to the local Kähler form, while the excluded holomorphic resolution direction is the Kähler exceptional‑curve direction, is supported and internally consistent:

- **Object exists and carries KE.** OSS Theorem 4.1 (Mabuchi–Mukai) gives exactly one four‑A₁ polystable degree‑4 point, $X_{4T}=(\mathbb P^1\times\mathbb P^1)/\mathbb Z_2$, with an explicit KE metric. Biquard–Rollin §7.1 constructs KE metrics on its smoothing by gluing Eguchi–Hanson bubbles; the smoothing of the four A₁ nodes is diffeomorphic to a four‑point blow‑up of $\mathbb P^1\times\mathbb P^1$, i.e. a smooth degree‑4 del Pezzo, which is KE by Tian/OSS. So the compatible locus is not conjectural: **genuine Einstein (KE) metrics exist there.**
- **The period identification is Kronheimer/Lemma‑6 geometry, correctly read.** In the graviton $Y_\zeta$, $\zeta=(\zeta_1,\zeta_2,\zeta_3)$ with $\zeta_1=\zeta_r$ the ambient‑Kähler period (exceptional curve area) and $\zeta_c=\zeta_2+i\zeta_3$ the holomorphic‑symplectic parameter. Biquard–Rollin Lemma 6 and Lemma 37 say the vanishing cycle is Lagrangian for the ambient structure exactly when $\zeta_r=0$ (smoothing, period lives in the $(\omega_2,\omega_3)$ plane, i.e. orthogonal to the Kähler form), and holomorphic when $\zeta_r\neq0$ (resolution, the $-2$ curve carries Kähler area). This is precisely the split you describe. It matches Biquard–Rollin's introductory remark that the *resolution* with the exceptional $-2$ sphere cannot carry KE unless $c_1=0$, whereas the *smoothing* can — the KE dP4 sits on the smoothing complex structure, not the resolution one.

So the assignment "compatible = smoothing = kernel‑plane period orthogonal to $\omega_1$; excluded = resolution = Kähler curve direction" is defensible. Two points need pinning before it is airtight: (i) $R^+=R^-=\mathrm{diag}(\Lambda,0,0)$ ("bi‑Kähler") uses that $S^2\times S^2$ with equal radii is Kähler for both orientations — standard, but it should be recorded as the reason both chiralities have rank‑one curvature; (ii) the identification "all‑compatible chirality row $\leftrightarrow$ KE smoothing" (your Step 67) plus the coordinate values $\sigma=(+,-,-,+)$ rests on matching Ozuch's $\pm$ EH orientation to the ambient complex orientation and on the corrected pole‑sign bookkeeping (Step 96). Physically all four nodes inherit one orientation from the ambient; the $\sigma$ pattern is then a coordinate label, not four distinct physical orientations. Confirm that the $\sigma$‑matched pair enumeration is invariant under the pole‑sign convention before trusting the adjacent/diagonal counting.

### 2. "f₄ vanishes on the compatible locus" is a true consequence of KE existence — but only for the fully calibrated potential

Because KE metrics genuinely exist along the compatible smoothing, the *full* Lyapunov–Schmidt reduced Einstein obstruction (all spectral sectors, complement solved in the slice, automorphisms accounted for) must vanish there. For a degree‑4 homogeneous real $f_4$, Euler's identity makes $\nabla f_4(x_0)=0$ force $f_4(x_0)=\tfrac14\langle\nabla f_4(x_0),x_0\rangle=0$. So gradient‑vanishing and value‑vanishing coincide at the KE configuration. This part is correct.

The reservation is exactly the one your `step97_gradient_quartic_audit.json` already records: the partial raw sectors do **not** individually vanish on the compatible locus (the AB partial $P^{(r=0)}\approx-0.0452$ is nonzero), and this is expected because tensor‑even, self/opposite‑corner, frame/projector, complement, and global‑deformation pieces are omitted. The vanishing is a property of the assembled, normalized potential, not of any truncation. Do not let "f₄ vanishes on the compatible locus" migrate into "the computed partial coefficients vanish."

### 3. "Same‑chirality self and pair coefficients should vanish" is stated too strongly and conflicts with your own determinantal reduction

What the KE‑existence argument delivers is that the compatible configuration is a *critical point* of the calibrated $f_4$ with $f_4=0$ there — i.e. $\nabla f_4=0$ along the whole Aut$(X_{4T})$‑orbit of that configuration. It does **not** deliver vanishing of individual self/pair coefficients $c_{\mathrm{adj}},c_{\mathrm{diag}},q_{\mathrm{diag}},\dots$. This is the same content as your corrected step94/step96 statement that the compatible row is a *degeneracy* $|P|=|Q|$, explicitly "not $P=0$ or $Q=0$ or any individual coefficient vanishing." The proposition "same‑chirality self and pair coefficients should vanish in the full calibrated potential" therefore contradicts the determinantal reformulation you adopted to replace the invalid linear subtraction. Recommended precise form: *the gradient of the assembled real quartic vanishes on the compatible KE orbit (equivalently $|P|=|Q|$ there), with the individual $c,q$ generically nonzero.* The nonvanishing AB coefficient is consistent with this and is not a signal of anything wrong.

### 4. Replacing $|q_{\mathrm{diag}}|$ vs $|2q_{\mathrm{adj}}+q_{\mathrm{diag}}|$ by a calibrated real quartic on physical variables is justified

The move from the scalar comparison to a genuine variational quartic is supported on several independent grounds:

- **The old comparison is an equal‑phase special ansatz.** Your own note records that collapsing to $|q_{\mathrm{diag}}|$ vs $|2q_{\mathrm{adj}}+q_{\mathrm{diag}}|$ presupposes an equal‑phase configuration. The phase‑reachability data (`analytic_range_for_abs_of_two_terms` $=[0,0.008]$, random min $\approx3\times10^{-7}$) show the two adjacent $Q$‑terms are independently phase‑tunable, so $2q_{\mathrm{adj}}$ is not the physically forced combination.
- **Physical sources are a rank‑one positive cone.** The A01 `step97_ab_physical_cone` result — $M_j=t_j^2u_ju_j^T$, $x=t_j^2>0$, $y^2+z^2=x^2$ — means kernels of unconstrained Sym²(K) blocks need not correspond to any bubble configuration, and conversely singularity of an unconstrained block is not itself an obstruction. The decision is therefore existence of a nonzero critical point of the reduced quartic restricted to the cone (scales $t_j>0$, angles $\theta_j$) together with the global/product‑ratio deformation directions, after solving the complement in the slice.
- **Gradient structure gives the right reformulation.** $f_4=\sum c_{ij}|\xi_i|^2|\xi_j|^2+\mathrm{Re}(q_{ij}\xi_i^2\overline{\xi_j}^2)$ has $\partial f_4/\partial\overline{\xi_j}=P_j\xi_j+Q_j\overline{\xi_j}$ (cubic), which is exactly your $O(t^3)$ inter‑node response. The order bookkeeping is consistent: the quadratic ($O(t^2)$) obstruction vanishes on $K$ (Section 5 below), and the pattern‑dependence first appears in the cubic gradient = quartic potential.

Two points require care. First, reality of $f_4$ forces $q_{ji}=\overline{q_{ij}}$ and real symmetric $c_{ij}$ after common‑frame transport; these are necessary self‑consistency tests for the computed coefficients (if violated, the transport or normalization is wrong), and their validity presupposes a variationally‑compatible slice — nontrivial because Ozuch's $\Phi_g=\mathrm{Ric}-\Lambda g+\delta^*B_g g$ carries the Bianchi term and is not literally a gradient; the gradient structure comes from the Kuranishi map of the Einstein moduli under integrable deformations, so the slice/gauge must preserve it. Second, the quartic is the leading term: where the assembled response is degenerate ($|P|=|Q|$), the verdict passes to the next order/transversality, so a quartic computation gives the leading decision, not an unconditional one.

### 5. A local obstruction here cannot establish global no‑Einstein for Yau 26

This is the decisive point, and the sources point against any such implication:

- **The target manifold already has an Einstein metric.** The compatible smoothing of $X_{4T}$ is a smooth degree‑4 del Pezzo, which carries a positive KE metric (OSS/Tian, Biquard–Rollin §7.1). Whether or not a mixed‑orientation Ricci‑flat gluing is obstructed, this smooth 4‑manifold possesses an Einstein metric. So this branch cannot exhibit a manifold with no Einstein metric.
- **Locality.** An obstruction near one orbifold degeneration constrains only gluing families near that degeneration; it is silent about Einstein metrics elsewhere in moduli. A01's `step97` note states this directly: the branch "does not settle Einstein existence on the smooth resolution and does not address the all‑dimensional Ricci‑pinching proposition."
- **The Yau‑26 statement is all‑dimensional and about pinched manifolds.** Refuting Yau‑26 requires a closed pinched $M^n$ that admits no Einstein metric of any sign; a single 4‑dimensional surface degeneration does not produce such an $M$. The mechanism‑separation observation in step94 §5 is the correct framing: all known dimension‑4 obstructions to Einstein use the four‑dimensional Chern–Weil identity $8\pi^2\chi=\int|W|^2+\tfrac23\lambda^2 V$ or the $\Lambda^2=\Lambda^+\oplus\Lambda^-$ splitting (SW/BF), neither of which survives to $n\ge5$; and the Gromov simplicial‑volume theorem ($\|M\|>0\Rightarrow$ no Einstein with $\lambda\ge0$) is a correct but known result touching only the $\lambda\ge0$ direction. None of these is delivered by the local del Pezzo computation.

In short: the del Pezzo branch may yield a rigorous local desingularization result for mixed‑orientation Eguchi–Hanson gluings, which is mathematically interesting, but it does not connect to Yau‑26 either as a refutation or as support, because the smooth object is KE.

### 6. Technical consistency checks that hold

- **Vanishing of the quadratic obstruction on $K$ (step96 §1).** With $R^\pm=\mathrm{diag}(\Lambda,0,0)$, $K\cong\mathbb C$ carrying weight‑1 under the $\beta=0$ subcircle, a homogeneous quadratic $T^2$‑equivariant self‑map needs $z^a\bar z^b$ with $a+b=2,\ a-b=1$, i.e. $a=3/2$ — no integer solution. The argument is clean and correctly promotes the pointwise $\det R_\perp=0$ to full projected vanishing, provided the $|\theta|=1$ weight and the "homogeneous quadratic equivariant map $K\to K$" framing are exactly the objects at that order. This is what pushes the first pattern‑dependence to the cubic response (= quartic potential), consistent with Section 4.
- **Gromov theorem (step94 §5, step96 §6).** Correct: $\mathrm{Ric}$ is scale‑invariant as a $(0,2)$‑tensor, so $\mathrm{Ric}_g\ge0$ gives $\mathrm{Ric}_{\varepsilon^2 g}\ge-(n-1)\varepsilon^2 g$; Gromov's bound then yields $\|M\|\le C(n)\varepsilon^n\mathrm{Vol}\to0$, so $\|M\|=0$.
- **Automorphism/slice bookkeeping.** $X_{4T}$ has positive‑dimensional Aut (a 2‑torus commuting with the $\mathbb Z_2$); OSS/Biquard–Rollin work Aut‑equivariantly, and Bando–Mabuchi makes the KE metric Aut‑invariant. The reduced quartic therefore lives on (deformation space)/Aut, the compatible KE configuration is a whole Aut‑orbit, and your "global coupling filter" ($T^2$‑invariant modes feed $P$ only) is the right kind of consideration. The calibration should be performed in an Aut‑equivariant slice and $f_4$ must vanish along the orbit.

### 7. What remains unresolved and what would settle it

- Assemble the full real quartic $f_4$ (AB, AA/BB even, self/opposite‑corner finite parts, frame/projector motion, and the $T^2$‑invariant global deformation of the $R_1/R_2$ product ratio), verify $c_{ij}$ real symmetric and $q_{ji}=\overline{q_{ij}}$ after common‑frame transport, and confirm that $\nabla f_4=0$ on the compatible KE orbit. Only after this calibration does the mixed‑orientation decision reduce to existence of a nonzero critical point of $f_4$ on the physical rank‑one cone with phases and global modes.
- Confirm that the LS slice preserves the gradient structure (the Kuranishi map is a true gradient), since Ozuch's operator is not literally variational; failure of the reality/symmetry tests would indicate a slice or transport error rather than a mathematical obstruction.
- Even a nonvanishing calibrated $f_4$ on the mixed row would be a statement about that gluing family near this degeneration. It would not bear on Yau‑26, because the smooth object carries a positive KE metric. If the intent is Yau‑26, the productive object is a pinched $M^n$ lacking an Einstein metric — which the mechanism‑separation and Gromov results suggest is where the genuine unknown lives (especially $n\ge5$), and which this del Pezzo branch does not supply.