# TTCS Independent Branch Record

```json
{
  "step_id": 91,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step91_receiver_and_adjacent_green.md",
    "Sessions/S0910A01/workspace/scripts/step91_receiver_simplification.py",
    "Sessions/S0910A01/workspace/data/step91_receiver_simplification.json",
    "Sessions/S0910A01/workspace/scripts/step91_checkerboard_radial_reduction.py",
    "Sessions/S0910A01/workspace/data/step91_checkerboard_radial_reduction.json",
    "Sessions/S0910A01/workspace/scripts/step91_corrected_spectral_ledger.py",
    "Sessions/S0910A01/workspace/data/step91_corrected_spectral_ledger.json",
    "Sessions/S0910A01/workspace/scripts/step91_adjacent_ab_heat_spectral.py",
    "Sessions/S0910A01/workspace/data/step91_adjacent_ab_heat_spectral.json",
    "Sessions/S0910A01/workspace/notes/step90_K_symmetry_cross_parity_elimination.md",
    "Sessions/S0910A01/workspace/notes/step89_correction_and_relative_green.md"
  ]
}
```

## Task

Verify the Step 91 product-orbifold calculation. Read the Step 91 note and supporting scripts/data. Check: (1) whether the product-background odd receiver really reduces to the sparse second-jet formula with no V0/frame/background-curvature correction; (2) whether the checkerboard radial reduction correctly leaves only adjacent ordered pairs in the per-receiver equations; (3) whether the corrected spectral ledger repairs the Step 90 mistakes (m-parity quotient descent, factor trace-free minimum P=2, independent degrees) while preserving P>=1 on the K-odd quotient linear sector; and (4) whether the AB one-form heat computation and its normalization are mathematically plausible as a sector calculation, including any norm/factor/sign/tail caveats. State precisely what is verified and what remains unsupported for the full Ozuch coefficient and Yau-26.

## Output

# Verification Memo — Step 91 Product-Orbifold Calculation (Session S0910A01)

I read the Step 91 note, the three scripts, and their JSON outputs, together with the Step 89/90 notes that supply the conventions. Below I separate what I independently reconstructed and confirm, from what is asserted but not derived in these files, from what remains open for the full Ozuch coefficient and for Yau-26.

## 1. Product-background odd receiver → sparse second-jet formula

**Confirmed analytically, not merely by the script.** I reconstructed the receiver from the stated conventions and it reproduces the boxed formula exactly.

- Vanishing of the background operator on the radial forms: product curvature carries only the index pairs $(01)$ and $(23)$ (i.e. $R_{0101}=R_{2323}=1$). The raw two-forms $\omega_2^\pm = e_{02}\mp e_{13}$ carry only the pairs $(02),(13)$. Since $(R\Omega)_{ij}=\tfrac12 R_{ijkl}\Omega_{kl}$ needs $R_{ij,02}$ or $R_{ij,13}$, and product curvature never carries a mixed A/B antisymmetric pair, $R_0\omega_2^\pm=0$. The data (`R0_omega_..._max_abs_num = 0`) matches. This part is rigorous.
- Reduction to the sparse jet: I computed the raw contraction $\tfrac18\sum \omega^\pm_{ij}\omega^\pm_{kl}\,\delta R_{ijkl}$ by hand. Using the stated $\delta R_{abcd}=\tfrac12(H_{ad,bc}+H_{bc,ad}-H_{ac,bd}-H_{bd,ac})$, the $\omega^+$ block gives $\tfrac12(\delta R_{0202}-\delta R_{0213}-\delta R_{1302}+\delta R_{1313})$ and $\omega^-$ gives the same with $+$ on the mixed terms; the difference is $-(\delta R_{0213}+\delta R_{1302})$. Expanding, $\delta R_{0213}=\delta R_{1302}=\tfrac12(H_{03,12}+H_{12,03}-H_{01,23}-H_{23,01})$, so
$$R_{\rm odd}=\tfrac12\big(H_{01,23}-H_{03,12}-H_{12,03}+H_{23,01}\big).$$
This is precisely the boxed expression and the four nonzero basis entries $\pm\tfrac12$ in the JSON. The 100-basis check with `failures_count=0` is therefore corroborated by an independent derivation.
- No $V_0/V_1$ dependence: this is automatic, since curvature is a second-order object and the receiver is evaluated at the node center in normal coordinates; only the Hessian $H$ enters. The $\ell=1$ census confirms every $V_0$-nonzero coexact mode has zero odd receiver, and only $(*dZ_A)\odot(*dZ_B)$ carries receiver $=1$.

**One point to weigh.** The statement "there is *no* background-curvature-times-$h_0$ correction to the odd receiver" rests on two ingredients of unequal strength. The vanishing $R_0\omega_2^\pm=0$ (which kills first-order frame/normalization variations $\langle\delta\omega,R_0\omega_2^\pm\rangle$) is exact. The additional "one-index replacement" support argument in §`background_curvature_times_h0_support` is a schematic model of possible $h_0$ corrections, not a derivation of the actual curved-parametrix correction terms (which are specific double contractions, not literally single-index substitutions). The robust content is: at the product center, the receiver is exactly the second-jet functional. Whether the *gluing* receiver picks up integrated/curved corrections away from the center is exactly what the note itself defers. So item (1) is solid as a statement about the pointwise principal receiver, and the note does not overreach on it.

## 2. Checkerboard radial reduction

**Confirmed.** With $\varepsilon=(+,-,-,+)$ in order $(NN,NS,SN,SS)$ and factor $\varepsilon_i\varepsilon_j-1$:
- self terms: $\varepsilon_i^2-1=0$;
- Hamming-distance-2 pairs $(NN,SS)$ and $(NS,SN)$: $\varepsilon_i\varepsilon_j=+1$, factor $0$;
- Hamming-distance-1 (adjacent) pairs: $\varepsilon_i\varepsilon_j=-1$, factor $-2$.

The eight surviving ordered pairs in the JSON are exactly the adjacent ones, and the per-receiver equations $\Delta_{NN}=-2t_{NN}(t_{NS}^2K_{NN,NS}+t_{SN}^2K_{NN,SN})$, etc., are correct. The note's insistence that the per-receiver system — not a single sum over receivers — is the geometric object is the right posture; the reduction to one number $K_{\rm adj}$ is correctly presented as contingent on frame-normalized exchange symmetries, not as established.

Minor wording only: the phrase "same-orbit diagonal companion" is loose. Under the quotient generator $(r_\pi,r_\pi)$ the four fixed points are genuinely distinct orbifold points (each is fixed, not identified). The vanishing of $(NN,SS)$ and $(NS,SN)$ comes purely from $\varepsilon_i\varepsilon_j=1$, not from any orbit identification. The arithmetic is right; the label is cosmetic.

## 3. Corrected spectral ledger vs. the Step 90 enumeration

**The three repairs are correct.**
- *m-parity descent.* The quotient generator $r_\pi$ sends $\phi\mapsto\phi+\pi$, so $Y_{\ell m}$ transforms by $(-1)^m$; descent requires $m_A+m_B$ even. The earlier $(-1)^\ell$ rule was wrong; this fix is right, and it is correctly kept distinct from the reflection $K$ (which is $\phi\mapsto-\phi$, giving the sin/cos = odd/even split used for chirality parity).
- *Factor trace-free minimum $P=2$.* The two descriptions in the text (rough eigenvalue $\ell(\ell+1)-4$ with $-\mathring R=+1$, versus the code's $\tfrac12\ell(\ell+1)-1$) are algebraically identical: $\tfrac12(\ell(\ell+1)-4)+1=\tfrac12\ell(\ell+1)-1$. The first K-odd descending factor-TF mode is $(\ell_F,m_F,\ell_O)=(2,2,0)$ with $P=2$ ($m_F=2$ even descends, $\sin 2\phi$ supplies the K-odd part). Correct.
- *Independent $\ell_A,\ell_B$.* The AB one-form minimum $P=1$ at $(1,1)$ is correct with $P=\tfrac12(\lambda_A+\lambda_B)-1$; factor interchange relates coefficients rather than restricting $\ell_A=\ell_B$.

**Where the $P\ge1$ conclusion is strong, and where it leans on assumption.** The durable support for "$P\ge1$ on the K-odd descending sector" is the *geometric* argument from Step 90 §5: the shape mode $q=g_A-g_B$ (with $Pq=-q$) and the four scalar zero modes are all K-even (K preserves each factor metric and fixes $Z_A=\cos\theta_A$), hence orthogonal to any K-odd source. That is a clean statement and it is the real reason the sign-reversing and zero directions do not enter.

The ledger's numerics are a *supporting enumeration under assumed $P$-formulas*, not an independent proof that no other K-odd mode has $P\le0$. Two points to hold in view:
- The `scalar_trace_block_candidate` formula $P=\tfrac12(\lambda_A+\lambda_B)-1$ is labeled "candidate" for good reason: pure-trace / conformal directions of $P=\tfrac12\nabla^*\nabla-\mathring R$ do not obey the same formula as TT tensors (the trace direction mixes with the scalar Laplacian). At $(\ell_A,\ell_B)=(0,0)$ this formula returns $P=-1$; that entry is a $m=0$, K-even direction and is correctly excluded from the K-odd rows, but it signals that the trace-block $P$-values in the ledger are heuristic. This does not disturb the geometric K-evenness argument for the known nonpositive modes; it does mean the ledger alone does not certify completeness of the spectrum.
- Completeness — that the *entire* K-odd descending TT spectrum on $S^2\times S^2$ starts at $P\ge1$ — is not exhaustively proven in these files. It is plausible (the product Einstein metric's destabilizing content is classically concentrated in $g_A-g_B$ and conformal/gauge directions, all K-even), but the note's own hedging ("only a spectral lower bound on the linear sector") is the appropriate register.

## 4. AB one-form heat computation and its normalization

**The receiver reduction used in the instrument is correct.** For $h=\alpha_A\odot\beta_B$ (with $\alpha$ on factor A, indices $0,1$; $\beta$ on factor B, indices $2,3$), the only surviving pieces of the sparse 4D formula are $-\tfrac12(H_{03,12}+H_{12,03})=-\tfrac12\big((\partial_1\alpha_0)(\partial_2\beta_3)+(\partial_0\alpha_1)(\partial_3\beta_2)\big)$, which in the code's local-frame matrices is exactly `-0.5*(A[0,1]*B[1,0]+A[1,0]*B[0,1])`. I verified this map by hand; it is consistent with §1.

**The restriction to $m\in\{0,2\}$ is justified.** The receiver depends on the scalar Hessian at the pole. Only $m=0$ (Hessian $\propto I$) and $m=2$ (traceless part) have nonzero Hessian there; $m=1$ is linear and $m\ge3$ vanish to order $\ge3$. Both $m=0,2$ are even, so descent is automatic. The $m=0$ coexact one-form $*dZ$ is genuinely K-odd because the azimuthal one-form flips under $\phi\mapsto-\phi$; this resolves the apparent tension that a $m=0$ scalar has no sin component. The ledger lists this correctly.

**The stable value is real but rests on an exact cancellation.** Reading `by_oneform_type` and `largest_mode_pair_contributions` across the ladder: the $c2/s2$ contributions grow as $\tau\downarrow0$ (from $\sim0.39$ at $\tau=0.01$ to $\sim1.30$ at $\tau=0.003$) and sum to zero in pairs (c2-c2 $+$ s2-s2 $+$ c2-s2 $+$ s2-c2 $=0$ to displayed precision). What survives is the $m0$-$m0$ coexact–coexact double series, which is independently stable at $-0.0314424973$ across all $\tau$. So the finite adjacent value is essentially the $m=0$ (axial-type) channel; the $m=2$ channels contribute a block that diverges as $\tau\to0$ and cancels internally. This is delicate: the finiteness of the off-diagonal value in this sector is contingent on that exact cancellation, and it would collapse if the true geometric source did not inherit the same pairing. The note flags this ("individual polarization subseries can have strong short-time behavior, while the complete AB block has cancellations"), so it is not oversold, but it is the most fragile numerical feature and deserves an analytic proof of the cancellation rather than reliance on displayed digits.

**Internal sign consistency checks pass.** The $\ell=1$ $m0$ coexact–coexact term tends to $-9/128=-0.0703125$ (`axial_l1_contribution` $\to-0.0701$ at $\tau=0.003$), and for the adjacent pair $s_{NN}s_{NS}=(+)(-)=-1$, so this matches Step 89's $K^{11,\rm axial}=\tfrac{9}{128}s_is_j$. The opposite-corner $SS$ pair gives $+0.0177$ (positive, and killed by the checkerboard factor anyway). The heat tails (`last_10_ellA_shell_abs_sum`$\sim10^{-200}$) show the regularization suppresses high modes as intended.

**Normalization pieces that are asserted, not derived here.** Three inputs are taken from the ledger/Step 89 rather than re-derived in this script: (i) that $\alpha_A\odot\beta_B$ is a genuine $P$-eigentensor (TT) with eigenvalue $\tfrac12(\lambda_A+\lambda_B)-1$; (ii) the product norm $\|\alpha_A\odot\beta_B\|^2_{\mathcal O}=\lambda_A\lambda_B$, where a factor-2 from symmetrization is stated to cancel a factor-$\tfrac12$ from quotient volume (plausible but not shown step by step); (iii) the source normalization $S=(\pi^2/2)R$. Items (i)–(iii) are consistent with the earlier steps but are load-bearing for the *absolute value and sign* of the reported number.

## What is established vs. what remains open

**Established (within the stated conventions):**
- The product-center odd receiver equals the sparse second-jet functional, with no $V_0/V_1$ dependence — confirmed by independent hand derivation and the 100-basis check.
- The checkerboard combinatorial reduction retaining exactly the eight adjacent ordered pairs.
- The three enumeration repairs (m-parity descent, factor-TF minimum $P=2$, independent degrees), and $P\ge1$ for the *known* nonpositive/zero modes via their K-evenness.
- A convergent, heat-regularized AB one-form sector value $\approx-0.03144$ dominated by the $m=0$ coexact channel, with correct internal sign consistency to the $-9/128$ axial anchor.

**Open / not addressed in these files:**
- The single-sector number is *not* the Ozuch adjacent coefficient. Missing: matching of the singular source normalization to the actual ALE-end (asymptotic $S^3/\mathbb Z_2$) multipole data; inclusion of the AA/BB factor trace-free sectors (which enter at $P=2$ and could add finite pieces); the Bianchi/gauge projection induced by the full source; an analytic proof (not numerical digits) of both the $m=2$ block cancellation and the differentiated-pairing tail control; and the match to Ozuch's $t_i\lambda_i+t_i^2\mu_i$ radial expansion at order $t_it_j^2$.
- Completeness of the K-odd spectrum $P\ge1$ (no other descending K-odd $P\le0$ mode) rests on the geometric K-evenness of $q$ and the scalar zero modes plus a candidate enumeration; the trace-block $P$-formula is heuristic.
- Even a nonzero, correctly-signed $K_{\rm adj}$ would constrain only the symmetric desingularization branch of this one product orbifold. It does not by itself exclude Einstein metrics on the smooth $\#_3(S^2\times S^2)$ arising from other degenerations or unrelated constructions, and it has no bearing on the dimension-general, all-manifolds statement that Yau-26 asks for (existence of dimensional constants $c_n<C_n$). The note's own final section states this correctly.

The Step 91 material is internally consistent and the two "reliable" items (receiver reduction, adjacent-only radial reduction) hold up under independent checking. The AB one-form number is a legitimate one-sector experimental quantity whose finiteness leans on an exact but currently only numerically-observed cancellation, and it is several derivations away from an object that could speak to Einstein existence on the underlying smooth four-manifold.