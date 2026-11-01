# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step62_preceptor_correction_rate_limited_flux_and_model_replacement.md",
    "Sessions/S0910A02/workspace/data/step62_step61_model_audit.json",
    "Sessions/S0910A02/workspace/data/step62_ade_invariant_reachability.json",
    "Sessions/S0910A02/workspace/notes/step61_toric_cone_weyl_and_bianchi_theorem.md",
    "Sessions/S0910A02/workspace/data/step61_weyl_eigenvalues.json",
    "Sessions/S0910A02/workspace/notes/step47_preceptor_review_mode_projection.md",
    "Sessions/S0910A02/workspace/data/step47_curvature_invariant_degeneracy.json"
  ]
}
```

## Task

Verify the Step-62 Preceptor correction to the Step-61 toric-cone drift model for Yau Problem 26. Read the corrected note, the algebra/data ledgers, and the prior Step-61/Step-47 context. Check: (i) whether the toric T^2-invariant warped ansatz is indeed invalid as a near-Ricci-pinched realizability model because of non-Einstein Ricci and axis smoothness; (ii) whether the replacement by full normal-coordinate Einstein-compatible quadratic jets legitimately gives local A1 Weyl freedom while preserving Ricci to first order; (iii) whether the corrected rate-limited flux alternative is stated at the right strength, with H_flux clearly unproved and the exponential channel correctly interpreted; (iv) whether the ADE invariant reachability refinement is accurate and not overclaimed; and (v) what concrete next research branch should be prioritized without turning this conditional result into a proof of Yau-26.

## Output

## Verifier memo — Step‑62 correction of the Step‑61 toric drift model

I read Step 62, the two ledgers (`step62_step61_model_audit.json`, `step62_ade_invariant_reachability.json`), Step 61 with `step61_weyl_eigenvalues.json`, and the Step‑47 review with its curvature‑invariance data. Below is what checks out, what is asserted but not yet computed, and what mathematical substance the five questions turn on.

---

### (i) Is the toric T²‑warped ansatz invalid as a near‑pinched realizability model?

Yes, for two independent reasons, and both hold up under recomputation.

**Non‑Einstein static Ricci.** From `step61_weyl_eigenvalues.json`, the linearized orthonormal Ricci of
$g=dr_1^2+dr_2^2+r_1^2e^{2\varepsilon A(r_1^2-r_2^2)}d\phi^2+r_2^2e^{-2\varepsilon A(r_1^2-r_2^2)}d\psi^2$
at $r_1=r_2=1$ is the base block $\varepsilon A\begin{psmallmatrix}-4&4\\4&-4\end{psmallmatrix}$ with zero fiber block. Its eigenvalues are $0$ and $-8\varepsilon A$, scalar $-8\varepsilon A$, and the traceless part is order $\varepsilon A$ — nonzero. The drift mode $v=\varepsilon A(r_1^2-r_2^2)$ is harmonic ($\mathcal Dv=0$), which kills the *fiber* $\pm\mathcal Dv$ Ricci but leaves the *base* traceless Ricci intact. This is a genuine order‑$\varepsilon A$ traceless Ricci, not an artifact.

The decisive arithmetic is the frame mismatch. Weyl degeneracy $W_\pm+(\Lambda/3)I$ acquiring a zero eigenvalue needs $\varepsilon A=\Lambda/16$, an amplitude tied to the *orbifold‑frame* Einstein constant $\Lambda=O(1)$. At that amplitude the recorded defect $\operatorname{Ric}-\Lambda g$ is
$\begin{psmallmatrix}-5\Lambda/4&\Lambda/4\\\Lambda/4&-5\Lambda/4\end{psmallmatrix}\oplus(-\Lambda)\oplus(-\Lambda)$,
of norm $O(\Lambda)$. So the single static mode can only rotate an $O(1)$ orbifold‑frame Weyl object by an $O(1)$ amount at the price of an $O(1)$ departure from Einstein. Step 61's own §1.2 wanted $v=O(t)$ (near‑pinched), while its §2.4 used $\varepsilon A=\Lambda/16=O(1)$ (degeneracy); these two amplitudes are incompatible, and Step 62 correctly locates the fault there. The near‑pinched target admits $O(1)$ total Weyl rotation only by accumulation over a long neck at $O(\delta)$ per scale, never from one static mode.

**Axis smoothness.** Near $r_1=0$ the $\phi$‑circle has proper circumference $2\pi r_1 e^{v(0,r_2)}$; smoothness of the collapsing circle forces $v(0,r_2)=0$, and symmetrically $v(r_1,0)=0$. The unique T²‑invariant degree‑2 harmonic $r_1^2-r_2^2$ restricts to $-r_2^2$ and $r_1^2$, neither vanishing, so it manufactures cone‑angle defects along both axes. This is correct, and the remark that angular cutoffs reintroduce large second angular derivatives into $\mathcal Dv$ (destroying the harmonic cancellation) is also correct. Together these two points settle (i): the specific ansatz is not a smooth near‑Einstein model.

**Energy paragraph.** Step 61's "$O(t^{-2})\ll 8\pi^2\chi$" compares a divergent quantity ($t^{-2}\to\infty$) against an $O(1)$ topological total, so the inequality points the wrong way; Step 62 is right to strike it. The replacement (with $r=e^{-u}$, $\int u^2e^{-4u}\,du=O(1)$, giving $\int|\delta W|^2 r^3\,dr=O(\delta^2)$) is a coherent volume‑weighted heuristic. Note that it silently switches from a bubble‑frame $|W|=O(1)$ description to a $\delta$‑scaled $|\delta W|\le C\delta u$ description; the two exponent bookkeepings should be reconciled in one fixed frame before this is used as more than motivation.

### (ii) Is the Einstein‑compatible quadratic‑jet replacement legitimate?

The algebra is correct. In $n=4$ the algebraic curvature space has dimension $n^2(n^2-1)/12=20$; the Ricci contraction onto $\operatorname{Sym}^2(\mathbb R^4)$ (dimension 10) is surjective, so its kernel is $20-10=10=\operatorname{Sym}^2_0(\Lambda^+)\oplus\operatorname{Sym}^2_0(\Lambda^-)$ ($5+5$). The ledger reproduces this from a symmetric $6\times6$ operator (21 free entries) with the single first‑Bianchi relation ($20$), Ricci rank $10$, kernel $10$. Hence $\mathcal E_\Lambda=\{H:\delta\operatorname{Ric}_e(H)=\Lambda e\}$ is an affine space whose tangent is the full $10$‑dimensional Weyl space, and a path $s\mapsto H(s)$ moves $W^\pm$ freely while pinning first‑order Ricci. For an $A_1$ point the isotropy is $\{\pm1\}$, which acts trivially on even (quadratic) jets, so no axis condition arises and the full block is available. This genuinely repairs both faults of (i) at the algebraic level.

One check is missing and is exactly the one that exposed the toric fault. The proposed neck metric is $g=e+H(A(\log r))$ — a quadratic‑in‑$x$ tensor whose coefficients vary radially through $A(\log r)$. That is **not** a single algebraic jet; it is a radial family of jets, and its Ricci is a nonlinear functional that must be computed. The claim "same mechanism… hence $O(\delta)$ when $|A'|+|A''|\le C\delta$" is an analogy to the toric $\mathcal Dv=\cos2\alpha\,(A''+6A')$ computation, not a computation. The toric case is the cautionary precedent: a harmonic ansatz that looked Ricci‑neutral hid an $O(1)$ base‑block traceless Ricci. The direct calculation of $\operatorname{Ric}(e+H(A(\log r)))-\Lambda(e+H)$, decomposed into a static part and the $A',A''$ parts, is what would confirm there is no analogous hidden static defect and that the leading correction is truly $O(A')+O(A'')$. Until that script exists, "full A₁ Weyl freedom under exponential drift" is established as a pointwise algebraic statement and conjectured as a neck statement.

### (iii) Is the rate‑limited flux alternative at the right strength?

The strength is stated correctly. $H_{\text{flux}}$ is explicitly the unproved input, and the derived dichotomy follows from it by elementary algebra: from $|\langle R_\pm(p)\zeta,\zeta_k\rangle|\le C\delta_i\log(1/t_i)+o(1)$, either $\delta_i\log(1/t_i)\to0$ forces $\Pi_\Gamma(R_\pm(p)\zeta)=0$, or a persistent obstruction $\ge\kappa$ forces $\log(1/t_i)\ge\kappa/(C\delta_i)$, i.e. $t_i\le e^{-c\kappa/\delta_i}$. Both branches are live; the exponential channel is not swept away. The local sharpness remark — that the $A_1$ jet space can be traversed with Ricci pinned over log‑length $\sim1/\delta$ — is the natural saturation of the same inequality, and Step 62 correctly marks that global capping, EH matching, and closed‑topology preservation are not constructed.

$H_{\text{flux}}$ is the single load‑bearing lemma, and it is the tensor version of the $H4_{\text{dual}}$ target from Step 47: a TT/Bianchi‑gauge weak pairing, ambient $H_2/H_4$ tower subtraction, nonlinear/gauge error control, and inner/outer ALE flux normalization. The re‑invocation of the Step‑11 spike — that $C^0$ Ricci pinching does not license a pointwise differentiated metric ODE, so the proof must be weak/flux‑based — is consistent across Steps 11, 47, 61, 62 and is the correct reason Step 61's "Theorem C" is now demoted to a hypothesis rather than kept as a theorem. Two items to pin: the normalization must keep the bubble‑frame signal $t_i\langle R_\pm(p)\zeta,\zeta_k\rangle$ and the orbifold‑frame obstruction $R_\pm(p)$ in one consistent rescaling (this is precisely the frame mixing that broke the toric model in (i)); and the identification of the inner ALE flux with $R_\pm=W_\pm+\tfrac\Lambda3 I$ needs the orientation convention fixed, not left convention‑free, once one actually computes.

### (iv) Is the ADE invariant reachability table accurate and not overreaching?

I checked every entry against the isotropy representations and they are correct.

- $A_1$: $\Gamma/\{\pm1\}$ trivial, $W$ arbitrary traceless symmetric ($\dim5$); $\det(aI+W)=0$; sample $\operatorname{diag}(-a,a/2,a/2)$ has eigenvalues $0,\tfrac{3a}2,\tfrac{3a}2$. ✓
- cyclic $A_k$ ($k\ge2$, image order $\ge3$): only axisymmetric $\operatorname{diag}(-u/2,-u/2,u)$ survives ($\dim1$); $(a-u/2)^2(a+u)=0$, roots $u=2a$ (double kernel), $u=-a$ (single). ✓ Image orders in the Step‑47 ledger are right: $A_2\!\to\!3,\ A_3\!\to\!2,\ A_5\!\to\!3,\ A_7\!\to\!4$.
- $A_3$ (image $\mathbb Z_2$, $\pi$‑rotation): $x_z,y_z$ entries flip and vanish, leaving $[[x,y,0],[y,z,0],[0,0,-x-z]]$ ($\dim3$); $(a-x-z)((a+x)(a+z)-y^2)=0$. ✓
- $D_4$ (image Klein four): $\operatorname{diag}(x,y,-x-y)$ ($\dim2$); $(a+x)(a+y)(a-x-y)=0$. ✓
- higher $D_k$: axisymmetric $\dim1$, same equation as cyclic. ✓
- $E_6,E_7,E_8$: no invariant $l=2$ harmonic (classical for $T,O,I$), $W=0$, $R=aI$, $\det=a^3>0$, no kernel for $\Lambda>0$. ✓

The table is scoped as *local algebraic* reachability ("not a global construction and not an $H_{\text{flux}}$ proof"), which is the right strength. One reading point to keep visible: $\det(aI+W)=0$ is the *existence‑of‑kernel* condition, i.e. whether *some* $\zeta$ can satisfy the obstruction, whereas the actual Biquard–Ozuch obstruction is the direction‑specific $R_\pm(p)\zeta=0$ for the $\zeta$ dictated by the bubble. Step 47 already insisted on the vectorial form, and §2.2 keeps $\Pi_\Gamma(R_\pm(p)\zeta)=0$, so the two are used consistently; the table entries are necessary conditions for killing the obstruction, not the obstruction itself. The product‑quotient check in §4 is internally consistent: $R_\pm=\operatorname{diag}(\Lambda,0,0)$ gives $W_\pm$ ratio $2\!:\!-1\!:\!-1$ and a genuine 2‑dimensional kernel, and the Step‑61 drift‑mode ratio $1\!:\!-2\!:\!1$ mismatch is indeed irrelevant once the ansatz is dropped and the full jet block is available.

### (v) Which branch can actually decide Yau‑26, and how not to inflate this conditional result

A structural point about the problem controls this. The pinching hypothesis $c_ng\le\operatorname{Ric}_g\le C_ng$ is scale‑covariant: $\operatorname{Ric}$ is invariant under $g\mapsto s^2g$, so the condition reads $c_ns^2\le \operatorname{Ric}(v,v)/g(v,v)\le C_ns^2$ pointwise. If $c_n<0<C_n$, large $s$ makes both sides trivial for any metric with bounded Ricci — every closed manifold would qualify, and the proposition would be immediately refuted by any 4‑manifold with no Einstein metric. So a non‑vacuous (potentially true) reading requires same‑sign constants: $0<c_n<C_n$ (a universal *positive* Ricci pinching ratio $C_n/c_n$) or $c_n<C_n<0$. In the positive case the real content is: does a universal bound on the positive‑Ricci eigenvalue ratio force existence of an Einstein metric? This is exactly why the noncollapsed positive bubbling degeneration (Cheeger–Naber orbifold limits, ADE bubbles, first obstruction) is the pertinent tool — it studies sequences pushed toward the pinching edge.

Given this:

1. **The reversed‑sign / LeBrun–Ishida arc is the branch most able to produce an actual decision (a disproof) in dimension four.** A disproof needs a closed 4‑manifold with no Einstein metric (Hitchin–Thorpe $2\chi\ge3|\tau|$, or the stronger Seiberg–Witten obstructions of LeBrun) that nonetheless carries a metric inside the universal pinching ratio. The stated open piece — per‑datum smooth existence of the pinched metric and the terminal‑metric spectral contradiction — is precisely the decisive verification: one must exhibit, on the no‑Einstein manifold, a concrete metric realizing $c_ng\le\operatorname{Ric}\le C_ng$ for constants that a putative positive theorem would have to allow, and confirm the topology genuinely forbids any Einstein metric. Independent reconstruction of the A01/A03 chain should center on that existence construction and on whether the SW/Hitchin–Thorpe obstruction is airtight for the chosen manifold.

2. **The noncollapsed positive bubbling arc, even with $H_{\text{flux}}$ proved, does not decide the full proposition.** It yields a necessary first‑order obstruction (or exponential bubble scale) for Kleinian/hyperkähler‑ALE bubbles in the positive four‑dimensional noncollapsed regime only. Step 47 already recorded that it leaves positive collapse, the reversed‑sign branch, non‑Kleinian $\Gamma\subset SO(4)$ bubbles, general Ricci‑flat ALE ends, and $n\ge5$ untouched, and gives no Lean object. Treating the conditional dichotomy as a resolution of Yau‑26 would be unsupported. Its correct use is as an obstruction instrument feeding branch (1): if the first obstruction forbids the degeneration that a candidate counterexample requires, that supports a restricted positive answer; if it permits it, the candidate survives.

3. **$n\ge5$ is where a disproof is hardest because the known no‑Einstein reservoir is essentially empty.** Hitchin–Thorpe and SW obstructions are four‑dimensional; in dimension $\ge5$ few closed manifolds are known to admit no Einstein metric, and many admit them. A disproof there would require a genuinely new no‑Einstein obstruction compatible with universal Ricci pinching — a large open target, worth keeping in view precisely because its emptiness may itself be evidence about the answer in high dimensions.

The positive collapse route (toric/ALG rod machinery) is worth pursuing only with the actual rod smoothness conditions and the saturated energy budget, not the discarded cone‑axis ansatz; Step 62's redirection away from patching the toric model is well‑founded.

### Load‑bearing items still unresolved

- The explicit Ricci computation of the jet‑neck metric $g=e+H(A(\log r))$, decomposed into static and $A',A''$ parts — the direct analog of the toric $\mathcal Dv$ calculation that revealed the fault, not yet performed.
- $H_{\text{flux}}$ ($=H4_{\text{dual}}$ in tensor form): TT/Bianchi gauge, ambient tower subtraction, nonlinear/gauge errors, inner/outer ALE flux normalization, with the bubble‑frame signal and orbifold‑frame obstruction kept in one consistent rescaling.
- A global smooth capping/EH matching realizing the exponential drift on a closed manifold — currently only a local jet mechanism.
- On the reversed‑sign 4‑manifold route: the concrete pinched‑metric existence construction and the terminal spectral contradiction that would turn it into a decision.
- Orientation ($\pm$ chiral block) conventions fixed once, rather than left convention‑free, before any construction that identifies the inner flux with $W_\pm+\tfrac\Lambda3 I$.

Net reading: Step 62's correction of Step 61 is mathematically sound on all five points I could recompute — the toric model is correctly set aside, the jet replacement is algebraically valid, the flux dichotomy is at the right strength with $H_{\text{flux}}$ marked open, and the ADE table is accurate and properly conditional. The one place where the correction rests on analogy rather than computation is the jet‑neck Ricci, which is exactly the computation whose omission produced the error being corrected.