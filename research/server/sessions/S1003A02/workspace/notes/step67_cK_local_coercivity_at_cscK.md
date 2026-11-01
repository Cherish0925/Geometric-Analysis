# Step 67 — Local coercivity of the exceptional-flux ledger at cscK metrics (Theorem 67.K)

Agent2, Execute. This continues `step66_rank_one_exceptional_ricci_rigidity.md` §§7–9, where the local
constant was defined as c_K = inf_{d₂>0} ℓ₂/(q²d₂). Symbol check:
`workspace/scripts/step67_cK_symbol_check.py` → `workspace/data/step67_cK_symbol_check.json`.

Notation, as in step66 §7.1:
- a = c₁(J₀);
- h_a⁻ is the g-harmonic ASD part of a;
- ĥ = h_a⁻/‖h_a⁻‖ and q = ‖h_a⁻‖ = |a⁻|_g;
- 𝔉 = √2∫|B^*ĥ| and δ = 1 − 𝔉/(2πq);
- L = (P/2 − 𝔉²)/(4π²), so that p = q²(1−δ)² + L holds exactly.

g₀ is a cscK metric with Kähler structure (J₀, ω) and primitive Ricci form ρ₀ = 2πh_a⁻ ≠ 0 (non-KE). Then B_{g₀} = ½ω⊗ρ₀ is rank one and aligned with constant amplitude, so δ(g₀) = 0 and L(g₀) = 0.

The slice 𝒮 is the space of first-order deformations ġ of constant-scalar metrics (the constant may vary) in harmonic (Bianchi) gauge with respect to g₀. By 66.Y this is no loss for α. For a smooth curve g_t with ġ = ∂_t g_t|₀ put
d₂(ġ) = ½∂²_tδ(g_t)|₀ and ℓ₂(ġ) = ½∂²_tL(g_t)|₀.
These are well defined quadratic forms because the first derivatives vanish (Lemma 67.1).

## 1. The first variation, and a classical reformulation

**Lemma 67.1.** At every cscK metric g₀ as above, Dδ(g₀) = 0 and DL(g₀) = 0. Consequently

  D(P − 8π²|c₁⁻|²_g)(g₀) = 0,  equivalently  D(C₊(g) − |c₁⁺|²_g)(g₀) = 0,

where C₊ = (2π²)⁻¹∫|W⁺|² + (96π²)⁻¹∫s² is LeBrun's functional. *Every cscK metric is a critical point of P − 8π²|c₁⁻|²_g on the space of all Riemannian metrics.*

*Proof.*
1. L ≥ 0 and L(g₀) = 0, so DL = 0.
2. For every orientation-compatible J with c₁(J) = a, identity 65.1 gives (t_J⁻, ĥ) = 2πq − ∫⟨Ω_J, B^*ĥ⟩. Since |Ω_J| = √2 we have ∫⟨Ω_J,B^*ĥ⟩ ≤ 𝔉. Hence

  2πq_g δ(g) ≤ τ_J(g) := (t_J⁻, ĥ)_g   for every class-a structure J.   (67.1)

3. Take J = Ĵ_t, the g_t-orthogonalization of J₀. Its intrinsic torsion is O(t). The twist t⁻ = (α∧β)⁻ is quadratic in the torsion, so τ_{Ĵ_t} = O(t²). Then (67.1) gives δ(g_t) ≤ Ct² for t of both signs, so the first-order coefficient vanishes.
4. The identity p − q² = q²(δ² − 2δ) + L then gives D(p − q²) = 0.
5. Finally p − q² = C₊ − |c₁⁺|²_g, because p = C₊ − c₁² (the chiral Chern–Weil identity) and |c₁⁻|² = |c₁⁺|² − c₁². ∎

Checks.
- Along Kähler directions: C₊ − |c₁⁺|² = (32π²)⁻¹∫s² − |c₁⁺|² ≥ 0 on Kähler metrics, with equality at cscK.
- Along conformal directions: the Weyl energy and |c₁⁺|² are conformally invariant, and ∫s² is stationary at any constant-scalar metric; Yamabe minimizing is unnecessary.
- We have not located Lemma 67.1 in the literature. LeBrun's sharp Seiberg–Witten estimate gives only C₊ ≥ (2/3)|c₁⁺|², and the Burns construction (Cor. 59.KE) shows that C₊ − |c₁⁺|² < 0 occurs on KE blow-ups. So cscK metrics are critical points but not global minimizers.

**Consequence: the meaning of the number \(c_K\).** At second order,
\[
 (p-q^2)_2=\ell_2-2q^2d_2.
\]
Hence \(c_K\ge2\) is equivalent to second-order minimality on the *linear* constant-scalar/Bianchi constraint space. It does not by itself imply nonlinear local minimality. The remainder established below is cubic in metric displacement (generically \(O(\delta^{3/2})\) along a ray), not \(O(\delta^2)\).

## 2. Theorem 67.K′ (corrected after verification)

Let \(g_0\) be a cscK metric on a compact complex surface with \(\rho_0=2\pi h_a^-\ne0\). Put
\[
 \mathcal S=\{k:\beta_{g_0}k=0,\ s'_0(k)\text{ is spatially constant}\},
 \qquad K=\ker\ell_2\cap\mathcal S.
\]
The space \(\mathcal S\) is a linear constraint space; no unobstructed parametrization of the nonlinear constant-scalar locus is asserted.

### (A) Moving-line null structure and the finite-dimensional obstruction

Assume \(Z(\widehat h)\) is empty or transverse. If \(k\in\mathcal S\) and \(\ell_2(k)=0\), the null equation follows the moving harmonic ASD line:
\[
 B'_0=\dot\Phi\otimes h_0+\Phi_0\otimes\dot h.
\tag{67.2}
\]
After subtracting this moving aligned comparison, row-wise Hadamard division at a transverse zero and linearized Lemma 66.D give a first-order almost-Kähler aligned pair
\[
 \operatorname{Ric}^\circ_t=\Phi_t\circ h_t+O(t^2),\qquad
 d\Omega_t=O(t^2),\qquad (\operatorname{Ric}'')'_0=0.
\tag{67.3}
\]
This conclusion is unconditional under the stated zero-set hypothesis.

First-order Kählerness has an additional cohomological obstruction. Define
\[
 \mathcal P_\omega:H^{0,1}(T^{1,0}M)\to H^{0,2}(M),
 \qquad [\mu]\mapsto[\mu\lrcorner\omega],
\]
and
\[
 \Xi(k)=[\dot\Omega_k]^{0,2}\pmod{\operatorname{im}\mathcal P_\omega}.
\tag{67.4}
\]
A prescribed \((0,2)\) class variation is realized by a first-order Kähler pair precisely when it lies in \(\operatorname{im}\mathcal P_\omega\). The earlier automatic construction from a holomorphic two-form was false: \(d\theta=0\) does not imply the vector-valued equation \(\bar\partial\mu=0\).

If \(\Xi(k)=0\), subtract a reference first-order Kähler pair, remove its remaining exact form variation by Moser, and use Blair--Ianus. In the present form norms the constants are
\[
 s^*-s=|\nabla\omega|^2,\quad
 \int s=4\pi c_1\cdot[\omega]-\frac12E,\quad
 DE(k)=2\int\langle\operatorname{Ric}'',k\rangle,
\]
\[
 \operatorname{Hess}E(k,k)=2\int| (\nabla\omega)'_k|^2.
\tag{67.5}
\]
Therefore \(\Xi(k)=0\) implies that \(k\) is first-order Kähler and lies in \(\operatorname{rad}d_2\). On products of curves of genera at least two, \(\mathcal P_\omega=0\); this makes the obstruction real, but does not prove that the constrained nullspace contains a mode with \(\Xi\ne0\).

### (B) Ellipticity and conditional coercivity

Assume \(Z(\widehat h)=\varnothing\). The augmented system \((DF,s',\beta)\) has injective principal symbol. The actual Ricci symbol is
\[
 \sigma_\xi(\operatorname{Ric}')(k)=\frac12\bigl(|\xi|^2k+\xi\otimes\xi\,\operatorname{tr}k-
 \xi\otimes k(\xi)-k(\xi)\otimes\xi\bigr),
\]
and reduces to \(\frac12|\xi|^2k\) on the Bianchi-symbol kernel. Thus the Step-67 numerical matrix checks an equivalent *gauge-reduced* symbol, not the unrestricted Ricci symbol. Algebraically, vanishing of the augmented symbol gives
\[
 k^\circ=\sigma\circ\widehat h,\quad \sigma\perp\omega,\quad \operatorname{tr}k=0,
 \quad (\sigma\circ\widehat h)\xi=0,
\]
and \((\sigma\circ\widehat h)^2=|\sigma|^2|\widehat h|^2\operatorname{Id}/4\) forces \(k=0\). Hence
\[
 \|k\|_{H^2}\le C\bigl(\sqrt{\ell_2(k)}+\|k\|_{L^2}\bigr),
 \qquad \ell_2(k)\ge c_1\|k-\pi_Kk\|_{H^2}^2,
\tag{67.6}
\]
and \(K\) is finite-dimensional. The sampled singular value \(0.148\) is a numerical check, not a universal constant.

If, additionally,
\[
 \Xi|_K=0,
\tag{67.7}
\]
choose first-order Kähler companions linearly on \(K\). For \(\eta=k-\pi_Kk\), the reference twist gives
\[
 d_2(k)\le C\|\eta\|_{H^1}^2\le C'\ell_2(k).
\tag{67.8}
\]
Thus \(c_K>0\) conditionally on (67.7), and for \(0<c<c_K\),
\[
 L(g_0+k)\ge cq_0^2\delta(g_0+k)-C\|k\|_{C^{2,\alpha}}^3
\tag{67.9}
\]
on \(\mathcal S\). Here \(\delta,L\) are smooth but nonlocal metric functionals near a zero-free background. A corresponding statement for exactly constant-scalar metrics needs a justified slice and quadratic projection to \(\mathcal S\). No nonlinear isolation or bifurcation conclusion follows.

The exact deficit formula is
\[
 2\pi qd_2=\tau_{\mathrm{ref},2}-\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|},
 \qquad
 w_1=P_{e_0^\perp}v'_0-|v_0|e'_0,
\tag{67.10}
\]
where the moving reference direction \(e_t\) is essential. Under (67.7), the operator representing \(q^2d_2\) on \(K^\perp\), with the \(\ell_2\)-Hilbert norm, is \(T-N\), with \(T\) compact self-adjoint and \(N\ge0\) bounded. Its positive spectrum is discrete; the whole operator need not be compact.

## 3. Product saddle (Step 68 correction)

For \(M=\Sigma_1(K_1)\times\Sigma_2(K_2)\), take a real holomorphic quadratic differential \(Q\) on \(\Sigma_1\), \(\Delta_2f=\mu f\), and \(k=fQ\). The fixed-symplectic exponential family has
\[
 8\pi^2(p-q^2)_2(k)=\frac\mu4(\mu+K_1-K_2)\|k\|_2^2.
\tag{67.11}
\]
The Step-67 generator's curvature-difference coefficient was twice too large because it mixed tensor and form norms for \(|\nabla\omega|\). In the corrected normalization,
\[
 \int u_2=\frac\mu8\|k\|_2^2,
 \quad (\rho_0,t_2^-)=-\frac{(K_1-K_2)\mu}{16}\|k\|_2^2,
 \quad (\operatorname{Ric}'')_1=\frac\mu2k.
\]
If \(K_1<K_2\), descent occurs exactly for \(0<\mu<K_2-K_1\), and
\[
 c_K\le\frac{2\lambda_1(\Sigma_2)}{K_2-K_1}.
\tag{67.12}
\]
Pinching makes this upper bound tend to zero. The mode has \(\ell_2>0\), so it bypasses rather than resolves \(\Xi\). An \(O(t^2)\) conformal correction to exact constant scalar curvature leaves the coefficient unchanged by Lemma 67.1. The proof and direct-curvature derivation are in `step68_product_cscK_saddle_verification.md`.

## 4. Final scope

The Kähler end now has four precise facts: unconditional stationarity (67.1); unconditional moving-line AK structure for null directions; finite-dimensional obstruction \(\Xi\) to Kähler rigidity and positive coercivity; and explicit non-aligned product saddles showing that \(c_K\ge2\) is false in general. Weighted ellipticity across zeros, \(\Xi|_K\), remaining product tensor blocks, and the blow-up analogue remain open.
