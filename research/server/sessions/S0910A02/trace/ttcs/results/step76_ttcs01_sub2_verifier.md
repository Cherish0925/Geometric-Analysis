# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step76_preceptor_audit_mixed_green_factorization.md",
    "Sessions/S0910A02/workspace/data/step76_product_green_factorization_audit.json",
    "Sessions/S0910A02/workspace/data/step75_symmetry_selection_collapse.json",
    "Sessions/S0910A02/workspace/notes/step68_spectral_symmetry_and_multipole_gate.md",
    "Sessions/S0910A02/workspace/notes/step64_positive_mirror_homeomorphism_and_allocation.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/On-infinitesimal-Einstein-deformations--3392b31fc0b0--66ff3e854e20/object.md"
  ]
}
```

## Task

Verify the Step-76 Preceptor audit before the next mixed-row Green computation is built. Focus on the scientific correctness of four gates: (1) Ozuch's \bar h^4 singular asymptotic is a source/self-node issue and inter-node expansions at other A1 points are regular second-jet extractions; (2) on a product background the P-Green/resolvent separates with additive spectral denominators (or heat-kernel integral) and is not a literal product of two static S^2 Green functions, so adjacent coincident-in-one-factor pairs must be treated in the full product resolvent or a justified massive one-factor reduction; (3) the T^2 pole selection rule restricts characters but does not truncate spherical degree l; (4) the D8 reduction, working diagonal=spin identification caveat, scalar full-gauged kernel slice requirement, and Yau-26 scope statements are faithful. Identify any overclaims, missing tensor/operator convention issues, or a better completion criterion for the next diagonal r=2 calibration computation.

## Output

# Verification Memo: Step-76 Preceptor Audit of the Mixed-Row Green Computation

## 1. Gate 1 — Ozuch source singularity and inter-node regularity

**Verdict: Correct and source-pinned.**

The audit's key assertion — that the $H^4 + H_2^4$ singular asymptotic belongs to the source/self node while inter-node evaluations are smooth second-jet extractions — is faithfully grounded in the Ozuch paper.

*Source verification.* Proposition 2.10 (equation (35)) constructs $\bar{h}^4$ on the orbifold satisfying $P_o\bar{h}^4 = \sum_l\nu_l\mathbf{v}_l + \sum_k\lambda_k\bar{\mathbf{o}}_k^4$ with the singular asymptotic $\bar{h}^4 = H^4(\zeta_j^\pm) + H_2^4 + O(r_o^{-\epsilon})$ only at the source point $j$. The multi-singularity version (equation (39)) sums $\bar{h}_j^4$ over all singular points. At a *different* singular point $i \neq j$, the contribution $\bar{h}_j^4$ has the regular expansion $H_0(i) + H_2(i) + O(d(i,\cdot)^4)$ — stated explicitly in Section 3.2.2, equation context near (62)–(63). This regularity is a consequence of the Green kernel being smooth away from the diagonal, a property that holds for the gauged operator $P_{\mathbf{g}_o}$ on any compact Einstein orbifold, including $(S^2 \times S^2)/\mathbb{Z}_2$ (the general framework of Section 2 handles arbitrary $\Lambda$).

*One clarification the audit should carry.* The explicit periodized sum formula (62) is specific to the flat torus $\mathbb{T}^4/\mathbb{Z}_2$ (convergence ensured by $|\nabla^l H^4| = O(r^{-4-l})$ summability on $\mathbb{Z}^4\setminus\{0\}$ for $l > 0$). On the positive-curvature product orbifold $(S^2\times S^2)/\mathbb{Z}_2$, the analogous extension uses Fredholm theory on a compact manifold (Proposition 2.10 applies in full generality, without periodization). The regularity principle transfers, but the explicit computational form differs.

---

## 2. Gate 2 — Product resolvent algebra

**Verdict: Correct. The factorization obstruction is real and the unit tests are verified.**

On $S^2(\Lambda)\times S^2(\Lambda)$, the Einstein operator's eigenvalues on product eigentensors are *sums* from the two factors (Kröncke, Proposition 4.1):

$$\operatorname{spec}(\Delta_E^{M\times N}) = \bigl(\operatorname{spec}(\Delta_E^M) + \operatorname{spec}(\Delta_0^N)\bigr) \cup \bigl(\operatorname{spec}(\Delta_E^N) + \operatorname{spec}(\Delta_0^M)\bigr) \cup \bigl(\operatorname{spec}(\Delta_1^M) + \operatorname{spec}(\Delta_1^N)\bigr).$$

The resolvent therefore has denominators $1/(\lambda_1 + \lambda_2 + \kappa_{\text{tensor}})$, not $C/[(\lambda_1+a)(\lambda_2+b)]$.

**Scalar unit tests verified.** Using $\lambda_l = l(l+1)$ on unit $S^2$ and additive shift $\kappa=1$:

| $(l_1,l_2)$ | Additive $1/(l_1(l_1+1)+l_2(l_2+1)+1)$ | Product $1/((l_1(l_1+1)+1)(l_2(l_2+1)+1))$ | Equal? |
|:---:|:---:|:---:|:---:|
| $(1,0)$ | $1/3$ | $1/3$ | ✓ |
| $(1,1)$ | $1/5$ | $1/9$ | ✗ |
| $(2,3)$ | $1/19$ | $1/91$ | ✗ |

Equality holds precisely when one factor sits in eigenvalue 0 (the $l=0$ constant mode), confirming the audit's statement that a "massive one-factor reduction" is legitimate only after proving one factor is restricted to a fixed eigenmode.

**Heat-kernel representation verified.** $(A\otimes1+1\otimes B+\kappa)^{-1} = \int_0^\infty e^{-t\kappa}e^{-tA}\otimes e^{-tB}\,dt$ correctly factorizes the integrand but gives a non-factored resolvent after $t$-integration.

**Adjacent-pair subtlety well-identified.** For $(N,N)\to(N,S)$, the first factor is at the *same* pole. In the full 4D product the points are separated by geodesic distance $\pi$, and the product Green kernel is smooth there. Multiplying a singular 2D Green function (at the coincident pole) by a regular 2D antipodal Green function would produce a spurious singularity. The audit correctly warns against this.

---

## 3. Gate 3 — $T^2$ pole selection rule

**Verdict: Correct. Character restriction is real; $l$-truncation does not occur.**

*Character restriction.* At a pole of $S^2$, a (scalar) spherical harmonic $Y_{lm}$ and its derivatives up to order $k$ probe only $|m|\le k$. The quotient parity $\rho(z,w)=(-z,-w)$ imposes $(-1)^{m_1+m_2}=+1$, i.e. $m_1+m_2$ even. Combined with the EH kernel-product $T^2$-characters $(\pm2,0),(0,\pm2)$, this selects a finite number of character channels.

*Non-truncation of $l$ verified.* The formula $P_l''(1)=\tfrac{(l+2)(l+1)l(l-1)}{8}$ is confirmed by direct computation (standard Legendre identity). It is nonzero for every $l\ge2$, so every $l\ge2$ contributes to the $|m|=2$ second-jet channel. Spot checks against the JSON data:

- $l=2$: $4\cdot3\cdot2\cdot1/8=3$ ✓  
- $l=4$: $6\cdot5\cdot4\cdot3/8=45$ ✓  
- $l=12$: $14\cdot13\cdot12\cdot11/8=3003$ ✓

Antipodal sign $P_l''(-1)=(-1)^l P_l''(1)$ follows from $P_l(-x)=(-1)^l P_l(x)$ and double differentiation. ✓

The computation is therefore an infinite sum in $l$ (for each allowed character), requiring either a closed-form evaluation or a certified tail bound. The audit's completion criterion item 6 correctly requires this.

---

## 4. Gate 4 — D8 reduction, diagonal–spin identification, kernel, scope

### 4a. D8 reduction: Correct

The four nodes form a $2\times2$ grid. Row flip, column flip, and factor swap generate a group of order 8 acting on the four nodes. The orbit analysis:

- $r=1$: orbit size 4, stabilizer size 2. Complement $r=3$ is equivalent via $c$ (orientation-reversing).
- Adjacent $r=2$: orbit size 4, stabilizer size 2. Self-conjugate.
- Diagonal $r=2$: orbit size 2, stabilizer size 4. Self-conjugate. Strongest internal consistency check.

The three independent pattern classes and the $r=1\sim r=3$ equivalence are sound.

### 4b. Diagonal = spin: working identification with appropriate caveat

The product spin-lift computation (signs $(+1,-1,-1,+1)$ at the four nodes) identifies the *diagonal* pair as the distinguished opposite-sign pair. The audit appropriately notes this depends on the canonical product lift and the Step-64 seam convention and is not yet an independently source-pinned topological theorem. For guiding the computation order and internal consistency tests, this is sufficient.

### 4c. TT kernel and full-gauged kernel: scientifically correct, with a Kröncke formula anomaly to note

The audit's central assertion $\ker(P|_{TT})=0$ on $(S^2\times S^2)/\mathbb{Z}_2$ is **correct**, verified by two independent arguments:

**Argument 1 (direct spectral computation on the cover).** On $S^2(\Lambda)\times S^2(\Lambda)$, TT deformations from the $l=1$ scalar sector vanish identically because the conformal Killing equation $\nabla^2 f = -\Lambda fg_{S^2}$ causes the TT construction (Kröncke, Remark 4.10) to give $h = \alpha fg_1 + 0\cdot fg_2 + (\alpha/\Lambda)\nabla^2f = \alpha fg_1 - \alpha fg_1 = 0$ when $n_1=n_2=2$. Since each factor separately has no TT deformations ($\ker\Delta_E^{S^2}|_{TT}=0$), and the mixed 1-form sector is positive (Lemma 4.4), the cover has $\ker\Delta_E^{S^2\times S^2}|_{TT}=0$. Any TT kernel element on the quotient would lift to the cover, so the quotient TT kernel is also zero.

**Argument 2 (dimension count).** On $S^2\times S^2$, direct enumeration gives $\dim(\ker\Delta_E^{S^2\times S^2})=12$ (6 from each case of the product formula). By Lemma 4.7 applied to the product (which is not a sphere): $\dim(\ker\Delta_E|_{TT}) = 12 - 2\times 6 = 0$.

**Anomaly in Kröncke's Proposition 4.8.** The formula $\dim(\ker\Delta_E^{M\times N}|_{TT}) = \dim(\ker\Delta_E^M|_{TT})+\dim(\ker\Delta_E^N|_{TT})+\operatorname{mult}_{\Delta_0^M}(2\mu)+\operatorname{mult}_{\Delta_0^N}(2\mu)$ gives $0+0+3+3=6$ for $S^2\times S^2$, contradicting the correct value 0. The discrepancy arises because the proof's intermediate formula uses $\dim(\ker\Delta_E^{S^2})=2\times\operatorname{mult}_{\Delta_0}(2\Lambda)=6$, but on the round sphere the $fg$ and $\nabla^2 f$ eigentensors for $l=1$ coincide (conformal Killing equation), so the true dimension is $\operatorname{mult}_{\Delta_0}(2\Lambda)=3$. This is a known subtlety of the sphere decomposition acknowledged in Lemma 4.3's proof. The anomaly does not affect the audit's conclusions (which correctly identify $\ker P|_{TT}=0$), but any future computation that directly invokes Proposition 4.8 for sphere factors must apply the correction.

**Full-gauged kernel.** On the quotient, the $\mathbb{Z}_2$-invariant part of $\ker\Delta_E^{S^2\times S^2}$ is 4-dimensional: only the $m=0$ modes from each factor survive ($Y_{10}^{(1)}g_1$, $Y_{10}^{(2)}g_2$, $Y_{10}^{(1)}g_2$, $Y_{10}^{(2)}g_1$). These are non-TT (conformal/automorphism type). The audit's identification of this 4-dimensional sector and the requirement that the Ozuch computation must slice or include it is correct.

### 4d. Relative product mode

Step 68 states $P_g h_{\rm rel}=-\Lambda h_{\rm rel}$ where $h_{\rm rel}=g_1-g_2$. Verified: $\Delta_E h_{\rm rel} = (\nabla^*\nabla - 2\mathring{R})h_{\rm rel}$. Since $h_{\rm rel}$ is parallel ($\nabla h_{\rm rel}=0$) and $\mathring{R}h_{\rm rel}=\Lambda h_{\rm rel}$ (direct computation using product curvature), we get $\Delta_E h_{\rm rel}=-2\Lambda h_{\rm rel}$, hence $P h_{\rm rel}=-\Lambda h_{\rm rel}$. ✓

### 4e. Scope: faithful

The scope statements correctly describe the mixed-row computation as a *diagnostic* for the local nearby-orbifold desingularization route on the specific product geometry, not as a proof or refutation of $P_4^+$ or Yau-26.

---

## 5. Additional scientific substance for the next computation

### 5a. Cosmological term

The Ozuch equations (20)–(23) include the $\Lambda\,\mathbf{eh}$ source term. On $\mathbb{T}^4/\mathbb{Z}_2$ this vanishes ($\Lambda=0$), greatly simplifying the periodized-sum construction. On $(S^2\times S^2)/\mathbb{Z}_2$ with $\Lambda>0$, the equation for $\underline{h}_2$ is $P_{\mathbf{eh}_{\zeta^\pm}}\underline{h}_2 = \Lambda\,\mathbf{eh}_{\zeta^\pm} + \sum_k\lambda_k\mathbf{o}_k$, and the cosmological source produces a nonzero $\underline{h}_2$ even before any ambient curvature interaction. The next computation must include this term; omitting it would produce the wrong $H_2^4$ and hence the wrong inter-node transport coefficients.

### 5b. Integrability of $\mathbf{O}(\mathbf{g}_o)$

The Ozuch framework (Definition 1.10) requires the orbifold's Einstein deformations to be integrable. On $(S^2\times S^2)/\mathbb{Z}_2$, the kernel $\mathbf{O}(\mathbf{g}_o)$ is 4-dimensional (scalar/conformal type). The two "same-factor" modes ($Y_{10}^{(a)}g_a$) are infinitesimal conformal rescalings integrated by rescaling each factor. The two "cross" modes ($Y_{10}^{(a)}g_b$, $a\ne b$) deform the metric on one factor by a function of the other. Their integrability must be verified explicitly (it is not automatic) for the Ozuch machinery to apply rigorously. If these modes are gauge-equivalent to automorphism directions (as they appear to be for $S^2$ isometries), the issue is benign; this should be stated.

### 5c. Strengthened completion criterion

The audit's 6-item completion list is substantive. Two additions would improve it:

**Item 7.** The $\Lambda>0$ cosmological source in equations (20)–(23) must be included, with the $\Lambda\,\mathbf{eh}$ contribution to $\underline{h}_2$ computed or bounded before inter-node transport. A computation setting $\Lambda=0$ by analogy with $\mathbb{T}^4/\mathbb{Z}_2$ would produce quantitatively different (and physically wrong) obstruction coefficients.

**Item 8.** The computation should identify which of Kröncke's three spectral sectors (symmetric 2-tensor lifts from each factor, mixed 1-form products) contributes to the Ozuch second-jet coefficient. On the product orbifold, all three sectors are present in the resolvent. The $T^2$-character selection reduces the number of active channels, but the spectral sum mixes sectors, and the tensor contractions with the EH kernel $O_k^4$ (equation (14)) must be tracked per-sector.

---

## Summary assessment

The Step-76 Preceptor audit is scientifically sound on all four gates. The Ozuch source anchoring, product resolvent algebra, $T^2$ selection rule, and D8/kernel/scope analysis are correctly described and well-grounded. The identified factorization obstruction (additive vs. product denominators) is real and verified by explicit counterexample. The $l$-non-truncation is confirmed numerically.

The main items to strengthen before the diagonal $r=2$ calibration computation: (a) include the $\Lambda>0$ cosmological source explicitly, (b) verify integrability of $\mathbf{O}(\mathbf{g}_o)$ for the product orbifold, (c) note the Kröncke Proposition 4.8 sphere anomaly (already consistent with the audit's $\ker P|_{TT}=0$ conclusion but relevant if that formula is cited elsewhere), and (d) add spectral-sector tracking to the completion criterion.