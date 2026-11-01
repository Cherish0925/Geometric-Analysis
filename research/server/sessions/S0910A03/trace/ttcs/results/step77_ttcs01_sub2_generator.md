# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md"
  ]
}
```

## Task

Consider the following mathematical problem arising in the negative branch of Yau Problem 26.

We seek a complete, non-ASD Einstein metric on ℝ × T³ with Ric = -3g that has two Poincaré-Einstein (PE) ends and a totally geodesic T³ center (equivalently, a reflected half-core on [0,∞) × T³ with S(0)=0 and PE at infinity). The ASD obstruction rules out Li-Liu-type fillings. The conformal infinity satisfies R_γ < -12.

Generate concrete mathematical mechanisms or structural arguments addressing:

(A) EXISTENCE/NON-EXISTENCE: Are there known results about non-ASD PE Einstein metrics on (0,∞) × T³? Anderson's boundary theory gives Fredholm index 0 for the PE boundary map. For the Li-Liu ASD sector, the Toda equation uniquely determines the filling. What is the dimension of the non-ASD moduli? Is there a parity or topological argument for/against non-ASD fillings?

(B) FORWARD EVOLUTION: From center data (q₀, S=0) with R(q₀)=-6 on T³, the Einstein evolution is well-posed after DeTurck gauge-fixing. Under what conditions does the forward evolution produce a PE end (rather than a singularity)? The pure cosh warped product requires Ric(q₀) = -2q₀, impossible on T³ by Preissmann. So the evolution is genuinely anisotropic. What structural conditions on q₀ control the long-time behavior?

(C) OBSTRUCTION MECHANISMS: Could a Bochner-type, index-theory, or topological argument prove that NO reflected Einstein core exists on ℝ × T³? The Witten-Yau one-endedness doesn't apply (negative Yamabe). The integrated shear identity R_γ = -12 - 4∫e^{2r}|S-I|²dr provides quantitative constraints. Is there a global monotonicity or Pohozaev-type identity that separates reflected centers from PE ends?

(D) DEFECT-BASED ALTERNATIVE: If no exact reflected core exists, could a family of approximate Einstein metrics with defect → 0 still work for the graph construction? The tail mechanism can flatten anisotropy at vanishing cost. If an exact obstruction exists, it might not extend to approximate metrics (analogous to how nearby Einstein metrics don't exist but the manifold might carry a distant Einstein metric).

Develop the most promising ideas with concrete mathematical content, equations, and testable predictions.

## Output

## Generator memo — the two‑ended Einstein core on ℝ×T³

I want to reopen this problem structurally before it hardens into "hunt for a non‑ASD filling." Several of the pieces already in the notes combine into sharper statements, and the geometry points to a concrete integrable arena plus two genuinely different ways the question could resolve.

### 1. Reframing (A): on this topology every filling is already non‑ASD — the dichotomy is a red herring

The orientation‑reversing reflection is the cleanest tool here, and it does more than exclude ASD. A reflection across a totally geodesic T³ is an isometry that reverses orientation, so it interchanges the self‑dual and anti‑self‑dual Weyl pieces: it maps \(W^+\leftrightarrow W^-\) pointwise on the fixed T³ and globally as an involution. Consequently, for **any** reflection‑symmetric Einstein metric on ℝ×T³,
\[
\int_M |W^+|^2\,dV=\int_M |W^-|^2\,dV .
\]
If such a metric were ASD (\(W^+\equiv0\)) it would then also be SD, hence conformally flat; with Ric\(=-3g\) that forces constant sectional curvature \(-1\), and a flat T³ cannot sit as a totally geodesic slice of \(\mathbb H^4\) (Preissmann). So ASD is impossible not as an accident of Li–Liu but as a consequence of the reflection itself. The practical conclusion: **on the two‑PE ℝ×T³ topology every filling is non‑ASD, so "find a non‑ASD filling" is not a special search — it is the only search.** The Li–Liu ASD sector lives on the *different* one‑PE‑plus‑one‑cusp topology; the Toda uniqueness there says nothing about a moduli dimension here.

For the moduli question itself, Anderson's index‑zero theorem says the map (Einstein fillings) → (conformal‑infinity data) is Fredholm of index 0, so at a nondegenerate metric the fillings of a fixed \([\gamma]\) form a discrete set and the fillable \([\gamma]\) form an open set of conformal classes. There is no continuous "non‑ASD modulus" to count; the object to produce is an isolated solution, and existence is a degree/continuation problem, not a dimension count.

### 2. A Gauss–Bonnet / renormalized‑volume reduction, and why a Weyl‑integral obstruction is unlikely

Because \(\chi(\mathbb R\times T^3)=0\), the four‑dimensional AH‑Einstein Chern–Gauss–Bonnet identity (Anderson, *L² curvature and volume renormalization*, normalization Ric\(=-3g\)),
\[
8\pi^2\chi(M)=\int_M |W|^2\,dV+6\,V_{\mathrm{ren}},
\]
collapses to the exact relation
\[
\boxed{\;\int_M |W|^2\,dV=-6\,V_{\mathrm{ren}}\;}
\]
for every complete such metric on ℝ×T³. Since the left side is \(\ge0\) and \(>0\) unless conformally flat (excluded), **any admissible core has \(V_{\mathrm{ren}}<0\).** Combined with the reflection swap, \(\int|W^+|^2=\int|W^-|^2=-3V_{\mathrm{ren}}\).

This makes the whole existence question equivalent, up to sign, to the achievability of \(V_{\mathrm{ren}}<0\). One tempting route to *non‑existence* is to prove \(V_{\mathrm{ren}}\ge0\) for reflection‑symmetric wormholes with a minimal (H=0) throat, which would force \(W\equiv0\) and kill the metric. I think this route is unpromising, and it is worth saying why so effort is not spent there: the Horowitz–Myers AdS soliton and toroidal AdS black holes are honest Ric\(=-3g\) metrics with toroidal conformal infinity and \(V_{\mathrm{ren}}<0\) (the soliton is even the energy‑minimizer in its class, proven in several cases by Galloway–Woolgar and Barzegar–Chruściel–et al.). So sub‑zero renormalized volume is not exotic; it is the ground‑state behavior for T³ infinity. A pure \(V_{\mathrm{ren}}\ge0\) statement would contradict the spirit of these examples. The value of the identity is therefore not as an obstruction but as a **bookkeeping equivalence**: any construction must arrange \(V_{\mathrm{ren}}<0\), and any purported non‑existence must explain why the soliton‑type mechanism producing \(V_{\mathrm{ren}}<0\) cannot coexist with a totally geodesic (rather than bolt) throat. That contrast — codimension‑one fixed T³ versus codimension‑two degenerating circle — is where a real obstruction, if one exists, must be located, not in a Weyl integral.

### 3. The concrete integrable arena: T²‑reduction to 2D dilaton gravity coupled to an H² sigma model

The right symmetry to impose is a T² of translations (two of the three torus directions), leaving a two‑dimensional quotient \((r,z)\), \(z\in S^1\). This is exactly the Ernst/Gowdy reduction with \(\Lambda=-3\). Write
\[
g=e^{2\nu(r,z)}\bigl(dr^2+dz^2\bigr)+\rho(r,z)\,M(r,z),\qquad M\in \mathrm{SL}(2,\mathbb R)/\mathrm{SO}(2)=\mathbb H^2,\ \det M=1 .
\]
Here \(\rho=\sqrt{\det(\text{T²-block})}\) is the fiber‑area "dilaton," and \(M\) is the unit‑determinant orbit shape (for the diagonal case \(M=\mathrm{diag}(e^{\omega},e^{-\omega})\)). The Einstein equations Ric\(=-3g\) become three coupled pieces:

- **Sigma model (matches the notes' \( \mathrm{div}(\rho\nabla\omega)=0\)):**
\[
\partial_r(\rho\,M^{-1}\partial_rM)+\partial_z(\rho\,M^{-1}\partial_zM)=0,
\]
a \(\rho\)-weighted harmonic map into the Hadamard surface \(\mathbb H^2\). Its \(\rho\)-weighted Dirichlet energy is precisely the center energy \(\langle d_s^2\rangle_\rho\) of Step 76 — the orbit anisotropy is a harmonic map, and the floor \(\langle d_s^2\rangle_\rho\ge12\) is the statement that this map cannot be trivial.
- **Dilaton:** \(\Delta_{(r,z)}\rho\) is driven by the \(\Lambda\)-source and the sigma‑model stress; schematically \(\Delta_{(r,z)}\rho = +6\,e^{2\nu}\rho\) (subharmonic — an interior minimum is allowed, which is exactly the throat). The reflection center is a critical slice \(\partial_r\rho(0,z)=0\); the two PE ends are \(\rho\to\infty\).
- **Conformal factor \(\nu\):** determined by first‑order constraints (the Hamilton/momentum pair) from \(\rho\) and \(M\).

Two things make this the arena of choice. First, at \(\Lambda=0\) this is the fully integrable vacuum system (Belinski–Zakharov inverse scattering / Weyl canonical coordinates with \(\rho\) harmonic), so one has an exact solvable seed to deform in \(\Lambda\). Second, the warped‑product degeneration is transparent here: a warped product needs \(M\equiv\)const, and the fiber equation then forces the cross‑section to have Ric\(=-2\) — impossible on the flat orbit. I verified this cleanly: \(g=dr^2+a(r)^2\gamma_0\) with Ric\(=-3g\) gives \(a''=a\) (so \(a=\cosh r\), totally geodesic at \(r=0\)) and the fiber equation reduces to the \(r\)-independent condition \(\mathrm{Ric}(\gamma_0)=-2\gamma_0\). This is the **Fuchsian wormhole** \(dr^2+\cosh^2r\,\gamma_{\mathrm{hyp}}\) whenever the cross‑section carries a metric of Ric\(=-2\) (hyperbolic 3‑manifolds), and it is unavailable on T³ solely because T³ has no such metric. So the T³ core must be genuinely off‑diagonal/anisotropic: \(M\) must be nonconstant, and the sigma‑model energy is forced. This turns "does a T³ core exist" into "does the \(\Lambda=-3\) \(\rho\)-weighted \(\mathbb H^2\) harmonic map admit a reflection‑symmetric configuration with a critical‑\(\rho\) throat and two \(\rho\to\infty\) PE ends." That is a sharply posed 2D elliptic problem, far more tractable than the five‑field fits that stalled.

### 4. Forward evolution (B): the PE‑versus‑cusp dichotomy is decided by a fiber eigenvalue, and the forced‑contraction direction is the one at risk

Two structural points. (i) Riemannian Einstein evolution in \(r\) is elliptic, so "evolving from center data" is analytic continuation, not a well‑posed initial‑value march; the linearized mode map amplifies like \(\sinh k/k\) (Step 74–76), i.e. it is exponentially bad in frequency and needs analytic/Gevrey center data. DeTurck makes it an elliptic two‑point problem, not a stable forward flow. (ii) Granting analytic data, the long‑\(r\) alternative is clean in the reduced picture: either all three torus circle‑lengths grow (\(\rho\to\infty\) with \(M\) bounded ⇒ PE end) or one circle collapses (an eigenvalue of the fiber metric \(\to0\) at finite \(r\) ⇒ a cusp end, the Li–Liu behavior). The single quantity to monitor is \(\lambda_{\min}(q_r)\) along the flow.

Here the center theorem becomes a *prediction*, not just a burden. The forced initial contraction \(\lambda_{\min}(S'(0))\le-3\) picks out one orbit direction whose circle length has strictly negative acceleration at the throat — precisely the direction that, left alone, drives \(\lambda_{\min}(q_r)\to0\) and a cusp. So the conjecture is: **the direction the center theorem forces to contract is the direction that generically collapses into a Li–Liu cusp; a PE end at both sides requires the expansion to "recapture" that direction before collapse.** This is directly testable by shooting in the reduced (r,z) system: parametrize \(q_0=e^{2\psi(z)}dz^2\oplus G(z)\) with \(R(q_0)=-6\) and \(S(0)=0\), integrate the elliptic system (or a DeTurck‑Ricci relaxation) and record whether \(\lambda_{\min}(q_r)\) turns around. Prediction consistent with Anderson index 0: generic \(q_0\) collapse (cusp), and only a discrete/codimension set re‑expand to two PE ends.

### 5. Obstruction candidates (C): what could actually work, and a new second identity

The exact shear identity you already have,
\[
R_\gamma=-12-4\int_0^\infty e^{2r}|S-I|^2\,dr,\qquad \tfrac{d}{dr}\!\left[e^{2r}(3-H)\right]=e^{2r}|S-I|^2,
\]
is a Pohozaev relation with weight \(e^{2r}\). It is worth generating the companion identities that isolate the *anisotropic* part, because the Weyl content lives there, not in \(H\). Split \(|S-I|^2=|S_0|^2+\tfrac13(H-3)^2\) into traceless shear plus mean‑curvature deficit. The traceless Riccati (Einstein) is
\[
S_0'+\tfrac{2H}{3}S_0=-(S_0^2)_0-\mathcal W_n,\qquad \mathcal W_n:=W(\cdot\,,n,\cdot\,,n)_{0},
\]
so anisotropy is sourced exactly by the electric Weyl \(\mathcal W_n\); \(W\equiv0\Rightarrow S_0\equiv0\Rightarrow\) umbilic ⇒ warped product ⇒ Ric\((q_0)=-2q_0\), impossible. This is the pointwise counterpart of \(\int|W|^2=-6V_{\mathrm{ren}}\) and links the two. Pairing with \(S_0\):
\[
\tfrac12(|S_0|^2)'=-\tfrac{2H}{3}|S_0|^2-\mathrm{tr}(S_0^3)-\langle \mathcal W_n,S_0\rangle .
\]
A monotonicity or Pohozaev argument that bounds \(\int e^{\alpha r}\langle\mathcal W_n,S_0\rangle\) from one side would separate reflected cores (which must generate \(S_0\) immediately from \((\mathrm{Ric}\,q_0)_0\neq0\)) from PE ends (where \(S_0\sim e^{-2r}\)). The most likely place for a true obstruction is a **global sign incompatibility between the throat‑generated shear stress and the stress a Yamabe‑sub‑zero PE end can absorb**, expressed through the \(\rho\)-weighted \(\mathbb H^2\) energy balance rather than through any curvature integral. Concretely: integrate the sigma‑model conservation law \(\mathrm{div}(\rho\,\nabla d)=0\) against well‑chosen weights over the half‑strip with the throat (Neumann, \(d_r=0\)) and the PE end (prescribed decay), and ask whether the forced throat energy \(\langle d_s^2\rangle_\rho\ge12\) can be radiated to infinity consistently with the momentum constraint \(\mathrm{div}_{q_r}P=0\). Index theory and Bochner on the *ambient* side look weak here: with \(R=-12<0\) there are no L² harmonic spinors (so Dirac index and the \(\eta\)-invariant of flat T³ give nothing), and the stable‑minimal structure of the throat is favorable, not obstructive — the stability operator of the totally geodesic T³ is \(-\Delta+3>0\), so the throat is strictly stable, i.e. nondegenerate. That strict stability is actually an argument *for* existence/robustness, not against it.

### 6. Defect route (D): the center theorem does not obstruct defect families, and the target is a uniform operator‑norm statement

The center theorem \(\lambda_{\min}(S'(0))\le-3+3\delta\) and the energy floor \(\langle d_s^2\rangle_\rho\ge12-8\delta\) survive for small‑defect cores, so one might fear they block the defect construction. They do not, and Step 76 already shows the escape: the throat energy can be diluted, \(F/V\sim e^{-2t}\to0\), so an order‑one throat contraction can be spread over a long expanding region at vanishing cost per unit physical volume. The exact identities (shear, energy) are throat‑exact; for defect cores they acquire \(O(\delta)\) corrections that do not prevent \(\delta\to0\). So the correct target for the minus branch is not an exact wormhole but a family
\[
S_j(0)=0,\quad R(q_0^{\,j})=-6,\quad \|\mathrm{Ric}_{G_j}+3G_j\|_{\mathrm{op},\infty}\to0,
\]
reaching an almost‑umbilic expanding slice that the adiabatic tail lemma then flattens to a flat‑cusp germ. The rigidity/existence analogy is apt: exact Einstein metrics near a given one may be absent while a distant Einstein metric exists — and likewise an exact reflected core may be absent while a defect‑vanishing family exists, because the pointwise Weyl obstruction \((W\equiv0\Rightarrow\) impossible) does not carry a positive lower bound on the *defect*. The concrete deliverable is to run the reduced (r,z) sigma‑model shooting with the throat fixed (\(S=0\), \(R(q_0)=-6\)) and the far data free, minimizing the operator‑norm defect over an *analytic* (not merely truncated‑Fourier) family, and to check whether \(\|\mathrm{Ric}+3g\|_{\mathrm{op}}\) descends toward 0 as the transition length grows — the earlier stall near residual \(\approx16\) is a finite‑basis artifact of the elliptic instability, not information about the infimum.

### 7. What I would compute to move the needle decisively

Three items, each of which changes the route rather than fitting tolerances:

1. **Reduced integrable seed.** Solve the \(\Lambda=0\) T²‑reduced vacuum system (Belinski–Zakharov / \(\rho\) harmonic) on ℝ×T³ for a reflection‑symmetric two‑soliton configuration with a critical‑\(\rho\) throat, then deform in \(\Lambda=-3\) by continuation. A persistent throat with two \(\rho\to\infty\) ends after turning on \(\Lambda\) would be the first genuine T³ core; obstruction to the deformation would be the first structural reason it cannot exist.
2. **Fiber‑eigenvalue shooting.** Integrate from analytic throat data with \(R(q_0)=-6\), \(S(0)=0\), monitoring \(\lambda_{\min}(q_r)\); map, in the two‑parameter anisotropy family, the set that re‑expands (PE) versus collapses (cusp). Test the prediction that the center‑theorem contraction direction is the collapsing one and that PE data are codimension \(\ge1\), matching index 0.
3. **Renormalized‑volume sign check on the soliton family.** Compute \(V_{\mathrm{ren}}\) (equivalently \(\int|W|^2\)) along a family interpolating from the AdS soliton/toroidal‑black‑hole geometry toward a would‑be totally geodesic throat, to see whether the transition from a codimension‑two bolt to a codimension‑one fixed T³ forces \(V_{\mathrm{ren}}\) across zero — the only quantitative place a non‑existence statement could originate.

The honest state of play (in ordinary terms): the pointwise Weyl/warped‑product argument explains *why the core must be anisotropic and non‑ASD*, the Gauss–Bonnet identity turns existence into the sign of \(V_{\mathrm{ren}}\), and the AdS‑soliton evidence makes a Weyl‑integral non‑existence unlikely — so the decisive battleground is the \(\Lambda=-3\) \(\rho\)-weighted \(\mathbb H^2\) harmonic‑map problem with a critical‑\(\rho\) throat, either as an exact solution or as a defect‑vanishing family.