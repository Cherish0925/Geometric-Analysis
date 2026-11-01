# Step 93 — The fixed-supplied-field limit across a Wahl filler: complete proof, index transfer, explicit characters, and the self-similarity of the Wahl channel

Session S1003A01, Agent2, Execute. Inputs: `step92_wahl_field_limit_proof_blueprint.md`, `spirit_step92_fixed_filler_field_shortcut.md`, the verifier `trace/ttcs/results/step92_ttcs02_verifier1_integration.md` (its sign/factor conventions are adopted verbatim), A02 Step 102 (Theorem 102.R, PPS Cor. 4.3 / Prop. 4.4 proof structure), and A01 Step 89 isotropy data.

Scripts and data:
- `workspace/scripts/step93_wahl_index_transfer.py` → `workspace/data/step93/wahl_index_transfer.json`
  (exact cyclotomic Kawasaki terms, signature defect, Riemann–Roch consistency, discrepancies, n = 2…8);
- `workspace/scripts/step93_wahl_supplied_characters.py` → `workspace/data/step93/wahl_supplied_characters.json`
  (local twist characters of the 16 sign classes meeting the V₋₄ summand, odd n = 3…15).
- `workspace/scripts/step93_removability_check.py` is a withdrawn placeholder (no computation) and must not be cited.

What changes. The Wahl field-limit (WFL) theorem, previously a blueprint with an unsourced removability step, is proved below for the explicit Lemma 86.S recovery family (Theorem 93.A). Removability is elementary in the abelian case and needs only bounded spinor and finite curvature energy; the equivariant lift is canonically the restriction class res(s). An index-transfer lemma shows that the orbifold Dirac index of res(s) equals the smooth index for every spinᶜ structure, and an exact Kawasaki computation confirms that the extendible characters are precisely those for which the local fixed-point term equals the canonical one. The Wahl orbifolds of Theorem 102.R are, after choosing the PPS spheres holomorphically, complex orbifolds Y that are themselves non-minimal of general type. Consequently the Wahl alternative in the Q1 trichotomy is the orbifold form of Q1 itself, and every obstruction built from supplied Seiberg–Witten fields, Chern–Weil integrals and index counts applies to V and M identically. The only new local datum is a forced spinor zero at p for an explicit fraction of the supplied classes when n ≥ 3, and a Kähler-type algebraic form of W⁺(p).

---

## 1. Setting and statement

Let \((V,g)\) be a compact oriented Riemannian orbifold with one singular point \(p\) of type
\(\Gamma=\frac1{n^2}(1,n-1)\subset U(2)\), and let \(M=V^{\rm reg}\cup B_{n,1}\) be the smooth manifold
obtained by replacing a cone neighbourhood of \(p\) with the Wahl rational ball, carrying Şuvaina's
Ricci-flat Kähler ALE metric \(h\) (a free \(\mathbb Z_n\) quotient of an \(A_{n-1}\) hyperkähler ALE metric).
The metrics \(g_\varepsilon\) are those of Lemma 86.S: \(g_\varepsilon=g\) for \(r\ge2\rho\), \(g_\varepsilon=\varepsilon^2h\)
on the filler, cut off at \(\rho=\varepsilon^{2/3}\). Several Wahl points are handled identically.

**Supply hypothesis (S).** There is a finite set \(\mathcal S\) of spinᶜ structures on \(M\) such that for
every \(\varepsilon\) some \(\mathfrak s\in\mathcal S\) carries an unperturbed solution of
\[
D_A\Phi=0,\qquad F_A^+=q(\Phi),\qquad |q(\Phi)|^2=\tfrac18|\Phi|^4,\qquad \tfrac12c(q(\Phi))\Phi=\tfrac14|\Phi|^2\Phi
\]
for \(g_\varepsilon\), with \((a^+_{g_\varepsilon})^2\ge A>0\), where \(a=c_1(\det\mathfrak s)\).
For \(M=X\#k\overline{\mathbb{CP}}^2\), \(b^+>1\), the \(2^{k+1}\) classes \(\pm K_X\pm E_1\cdots\pm E_k\) are
simultaneously supplied for every metric, and the averaging identity
\(2^{-k}\sum_\sigma(a_\sigma^+)^2=(c^+)^2+\sum(E_i^+)^2\ge A\) supplies the selection. For \(b^+=1\) the
chamber/selection input must be stated separately; nothing below uses \(b^+>1\) beyond (S).

**Theorem 93.A (Wahl field limit).** Assume (S). For every sequence \(\varepsilon_j\to0\) there are a subsequence, one
\(\mathfrak s\in\mathcal S\), and gauge transformations such that \((A_j,\Phi_j)\) converges in \(C^\infty_{\rm loc}(V^{\rm reg})\)
to a solution \((A_\infty,\Phi_\infty)\) which extends to a smooth orbifold Seiberg–Witten solution on \((V,g)\) for the
unique orbifold spinᶜ structure \(\operatorname{res}(\mathfrak s)\) whose restriction to \(V^{\rm reg}\) is \(\mathfrak s|_{V^{\rm reg}}\).
Moreover

1. \(\int_M|\Phi_j|^4\to\int_V|\Phi_\infty|^4\ge32\pi^2A\); in particular \(\Phi_\infty\not\equiv0\) and the solution is irreducible;
2. the real class of \(\det\operatorname{res}(\mathfrak s)\) is the image of \(a\) under \(H^2(M;\mathbb R)\cong H^2(V;\mathbb R)\), and \(a_V^2=a_M^2\);
3. \(\int_M|F_{A_j}|^2\to\int_V|F_{A_\infty}|^2\), \(\int_M|\nabla_{A_j}\Phi_j|^2\to\int_V|\nabla_{A_\infty}\Phi_\infty|^2\), \(\int s_jU_j\to\int sU\);
4. if the same finite family is metric-wise supplied on \(M\) for all smooth metrics, the theorem applies separately to the recovery family of every orbifold metric on \(V\) (quantifier repaired in §8).

No assumption on \(g\) (Einstein or otherwise) is used.

## 2. Proof

**(i) Selection.** Finite pigeonhole on \(\mathcal S\) fixes \(\mathfrak s\) along a subsequence, retaining \((a^+)^2\ge A\).

**(ii) Uniform scalar bound and tightness.** Lemma 86.S gives \(|\operatorname{Ric}(g_\varepsilon)|\le C\rho^{-2}[\rho^2+(\varepsilon/\rho)^4]=O(1)\) on the transition annulus, \(\operatorname{Ric}=0\) on the filler, and \(g_\varepsilon=g\) outside. Hence \(\sup|s_\varepsilon|\le C_g\). With \(U=|\Phi|^2\), the Weitzenböck formula
\[
4\nabla_A^*\nabla_A\Phi+s\Phi+U\Phi=0,\qquad 2\Delta U+4|\nabla_A\Phi|^2+sU+U^2=0
\]
and the maximum principle give \(0\le U_\varepsilon\le C_g\). Since \(\operatorname{Vol}_{g_\varepsilon}\{r<R\}\le C(\rho^4+R^4)\),
\[
\limsup_{\varepsilon\to0}\int_{\{r<R\}}|\Phi_\varepsilon|^4\le C_gR^4. \tag{2.1}
\]
Integrating the Weitzenböck formula, \(\|U\|_2\le\|s^-\|_2\) and \(4\|\nabla_A\Phi\|_2^2\le\|s^-\|_2\|U\|_2\); harmonic projection gives \(\int U^2=8\int|F_A^+|^2\ge32\pi^2(a^+)^2\ge32\pi^2A\); Chern–Weil for the fixed class gives \(\int|F_A^-|^2=\int|F_A^+|^2-4\pi^2a^2\). All energies are uniformly bounded.

**(iii) Regular-part convergence.** On each compact \(K\subset V^{\rm reg}\) the metric is eventually \(g\) and the spinᶜ structure is the fixed \(\mathfrak s|_K\). Local Coulomb gauges, elliptic estimates for \(D_A\) and \(d^*+d^+\), the uniform \(L^\infty\) bound on \(\Phi\) and the \(L^2\) bound on \(F_A\), and a diagonal argument over an exhaustion give \(C^\infty_{\rm loc}\) convergence modulo gauge (the abelian gauge patching is standard; \(H^1\) obstructions to patching are absorbed in the limiting bundle, which is \(\mathfrak s|_{V^{\rm reg}}\)). By (2.1) and lower semicontinuity, \(\Phi_\infty\in L^\infty\), \(F_{A_\infty}\in L^2\), \(\nabla_{A_\infty}\Phi_\infty\in L^2\), and \(\int_{V^{\rm reg}}|\Phi_\infty|^4=\lim\int_M|\Phi_j|^4\ge32\pi^2A\).

**(iv) Lemma 93.R (abelian point removability).** *Let \(B\subset\mathbb R^4\) be the unit ball with a smooth metric, \(B^*=B\setminus\{0\}\), \(S\) the spinᶜ structure of \(B\), and \((A,\Phi)\) an unperturbed solution on \(B^*\) with \(\sup|\Phi|<\infty\) and \(F_A\in L^2(B^*)\). Then \((A,\Phi)\) is gauge-equivalent on \(B^*\) to the restriction of a smooth solution on \(B\).*

*Proof.* Trivialize \(\det S\) with product connection \(A_0\); write \(F=-iF_A\), a real closed 2-form on \(B^*\) in \(L^2(B)\). Let \(\chi_\delta\) vanish on \(B_\delta\), equal \(1\) off \(B_{2\delta}\), with \(|d\chi_\delta|\le2/\delta\); then \(\|d\chi_\delta\|_{L^2}=O(\delta)\) and \(\|d\chi_\delta\|_{L^1}=O(\delta^3)\). For a test 1-form \(\beta\in C^\infty_c(B)\),
\(0=\int F\wedge d(\chi_\delta\beta)=\int\chi_\delta F\wedge d\beta+\int F\wedge d\chi_\delta\wedge\beta\), and the last term is at most \(\|F\|_{L^2(B_{2\delta})}\,O(\delta)\to0\). Thus \(dF=0\) on \(B\) distributionally. Let \(a'\in W^{1,2}(B)\) solve \(da'=F\), \(d^*a'=0\), \(\iota_\nu a'|_{\partial B}=0\); it exists and is unique because \(H^1(B)=H^2(B)=0\). On \(B^*\), \(A=A_0+ia\) and \(d(a-a')=0\); since \(H^1(B^*)=0\), \(a-a'=df\) with \(f\in W^{2,2}_{\rm loc}(B^*)\). After the gauge transformation \(e^{if/2}\) (determinant connection; corrected in §8), \(A=A_0+ia'\) and \(\Phi'=e^{-if}\Phi\) is still bounded. On \(B^*\), \(D_{A_0}\Phi'=-\tfrac i2c(a')\Phi'=:\phi\in L^4(B)\) because \(a'\in W^{1,2}\subset L^4\). The same cutoff, with error \(\|\Phi'\|_\infty\|d\chi_\delta\|_{L^1}\|\psi\|_\infty=O(\delta^3)\), shows \(D_{A_0}\Phi'=\phi\) on all of \(B\). Elliptic regularity gives \(\Phi'\in W^{1,4}_{\rm loc}\). Then \(d^+a'=q(\Phi')\in W^{1,4}\) and \(d^*a'=0\) give \(a'\in W^{2,4}_{\rm loc}\subset C^{0,\alpha}\cap W^{1,p}\) (not \(C^{1,\alpha}\) in dimension four), and the system bootstraps to \(C^\infty\) via \(W^{1,p}\), \(p>4\) (§8). ∎

Only \(\Phi\in L^\infty\) and \(F_A\in L^2\) are used. The Uhlenbeck-type machinery needed for nonabelian removability (Feehan–Leness) is unnecessary because the abelian curvature equation is linear in the connection form.

**(v) Lemma 93.Q (equivariant extension and the lift).** Let \(\pi:B\to B/\Gamma\) be an orbifold chart at \(p\). Γ-equivariant spinᶜ structures on \(B\) are classified by the lift of the isotropy representation at \(0\), i.e. by characters \(\chi\in\widehat\Gamma\cong\mathbb Z_{n^2}\) relative to the canonical lift \(S_0=\Lambda^{0,0}\oplus\Lambda^{0,2}\) (\(B\) contracts equivariantly to \(0\)). Equivariant structures on \(B^*\) are spinᶜ structures on \(L=S^3/\Gamma\), an \(H^2(L;\mathbb Z)\cong\mathbb Z_{n^2}\)-torsor. Restriction is the affine bijection induced by the isomorphism \(H^2(B\Gamma)\to H^2(L)\). Hence the pullback of \(\mathfrak s|_{V^{\rm reg}}\) is \(S_\chi|_{B^*}\) for a unique \(\chi\); by definition \(\operatorname{res}(\mathfrak s)=\chi\).

Write \(A=A_0+ia\) in the equivariant trivialization \(S_\chi=B\times\mathbb C^4\) with action \(\gamma_0\otimes\chi\). Then \(A_0\) is invariant and Γ-invariance of \(A\) is \(\gamma^*a=a\). The Coulomb solution \(a'\) of (iv) is unique, hence Γ-invariant. Then \(d(f\circ\gamma-f)=0\), so \(f\circ\gamma-f=c_\gamma\) is constant, and \(\gamma\mapsto c_\gamma\) is a homomorphism \(\Gamma\to\mathbb R\), hence zero. The gauge \(e^{-if}\) is invariant, the gauge-fixed pair is invariant, and its smooth extension is invariant by continuity. It descends to a smooth orbifold solution for \(\operatorname{res}(\mathfrak s)\). ∎

The relevant gauge-theoretic datum is therefore the torsion lift \(\chi\), not a disconnected gauge sector: \(\pi_0\operatorname{Map}(L,U(1))=H^1(L;\mathbb Z)=0\), as the Step-92 verifier noted. For even \(n\) the lift \(\chi\) is retained, not only \(\chi^2=\det\).

**(vi) Energy and class transfer.** \(H^2(V;\mathbb R)\to H^2(V^{\rm reg};\mathbb R)\) is an isomorphism because \(H^*(L;\mathbb R)\) is that of \(S^3\). Pairing \(iF_{A_j}/2\pi\) with closed forms compactly supported in \(V^{\rm reg}\) and using smooth convergence identifies the real class, and the cup squares agree because the rational ball and the cone carry no rational \(H^2\). Tightness (2.1) plus local convergence gives \(\int|F^+_{A_j}|^2\to\int|F^+_{A_\infty}|^2\). Chern–Weil on \(M\) and on \(V\) with equal \(a^2\) then gives convergence of \(\int|F_A|^2\). Since \(s_j\) and \(U_j\) are bounded and the filled volume shrinks, \(\int s_jU_j\to\int sU\), and the integrated Weitzenböck identity transfers \(\int|\nabla_A\Phi|^2\). Item 4 holds because nothing in (i)–(vi) depended on \(g\) beyond smoothness. ∎

**Consequence (orbifold LeBrun estimates).** On every orbifold metric on \(V\): \(\int s^2\ge\int U^2\ge32\pi^2A\). Applying the theorem to \(f^{-2}g\) reproduces LeBrun's conformal-rescaling argument, so \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2A\) holds on \(V\). Supply on \(V\) for every orbifold metric is now a theorem, not a filler-transfer heuristic.

## 3. Index transfer

**Lemma 93.I.** For every spinᶜ structure \(\mathfrak s\) on \(M\), \(\operatorname{ind}D^{\rm orb}_{\operatorname{res}(\mathfrak s)}(V)=\operatorname{ind}D_{\mathfrak s}(M)\). Hence the orbifold Seiberg–Witten expected dimension of \(\operatorname{res}(\mathfrak s)\) equals that of \(\mathfrak s\) (zero for the basic classes of \(X\#k\overline{\mathbb{CP}}^2\)).

*Proof.* Decompose along \(L\), whose round metric has positive scalar curvature; the spinᶜ Dirac operator on \(L\) with flat twist is invertible (\(|\mu|\ge3/2\)), so APS gluing has no boundary-kernel correction:
\(\operatorname{ind}(M)=\operatorname{ind}_{\rm APS}(V^{\rm reg}_{\rm tr})+\operatorname{ind}_{\rm APS}(B_{n,1},\mathfrak s|_B)\) and
\(\operatorname{ind}(V)=\operatorname{ind}_{\rm APS}(V^{\rm reg}_{\rm tr})+\operatorname{ind}_{\rm APS}(C(L),\chi)\).
(a) *Filler.* \(H^2(B_{n,1};\mathbb Z)=\mathbb Z_n\) is torsion, so every spinᶜ structure has a flat determinant connection, and Şuvaina's metric is Ricci-flat; \(D^2=\nabla^*\nabla\). Solutions in the weight window between the indicial roots (which contains \(L^2\) and the APS weight) decay like \(r^{-3}\) and are therefore parallel, hence zero, in both chiralities. The weighted index equals the APS index after the conformal change \(r^2(dt^2+g_L)\), and Dirac conformal covariance preserves the window. Thus \(\operatorname{ind}_{\rm APS}(B,\mathfrak s|_B)=0\).
(b) *Cone.* Replace the flat cone by a Γ-invariant positive-scalar-curvature cap, the quotient of a round hemisphere with a cylindrical collar, and argue on Γ-invariant sections. With a flat twist, Lichnerowicz gives zero kernel in both chiralities, so \(\operatorname{ind}_{\rm APS}(C(L),\chi)=0\) for every χ.
The boundary operators agree because \(\chi|_L=\mathfrak s|_L\). ∎

**Exact local check** (`wahl_index_transfer.json`). Kawasaki's formula writes the orbifold index as the Chern–Weil integral plus
\[
\delta(m)=\frac1{n^2}\sum_{k=1}^{n^2-1}\frac{\zeta^{km}}{(1-\zeta^{-k})(1-\zeta^{-k(n-1)})},\qquad \zeta=e^{2\pi i/n^2},
\]
for the line twist \(\zeta^m\) of the canonical lift. For \(n=2,\dots,8\), exact evaluation gives:
- \(\delta(0)=(1-1/n^2)/12\), the value forced by \(\chi(\mathcal O)\)-invariance and Noether's formula with \(e_{\rm orb}=e-(1-1/n^2)\);
- the signature defect \(\tau_{CW}-\tau_{\rm top}=\frac1{n^2}\sum\cot\frac{\pi k}{n^2}\cot\frac{\pi k(n-1)}{n^2}=\frac23(1-\frac1{n^2})\) (for example \(1/2,16/27,5/8,16/25\)), so \(2e_{\rm orb}+3\tau_{CW}=2e+3\tau\). This is the curvature-level K²-invariance used by A02. (The first sign convention tried failed with the same magnitude; the sign is fixed by the Kähler identity.)
- \(\{m:\delta(m)=\delta(0)\}=\{0,n,2n,\dots,(n-1)n\}\) **exactly**, for both inversion conventions. These are the characters extending over \(B_{n,1}\). Since twisting by a line extending over \(B\) changes the Chern–Weil term identically on both sides, this is the local content of Lemma 93.I. The computation is an independent confirmation, and it also shows that a non-extendible lift would change the index.

## 4. Complex realization of the Wahl orbifolds: self-similarity

**Proposition 93.Y.** In Theorem 102.R choose each PPS sphere holomorphic: for odd \(n\ge3\), the \((-4)\)-curve \(S=E_1-E_2-E_3-E_4\) obtained by blowing up a point of \(X\) and then three points of its exceptional curve; for \(n=2\), the analogous \((-3)\)-curve. The class \(E_1+\dots+E_4\) is carried to \(S\) by reflections \(E_i\mapsto-E_i\), which complex conjugation on the \(\overline{\mathbb{CP}}^2\) summands realizes as diffeomorphisms. Then the resulting Wahl orbifold \(V\) is orbifold-diffeomorphic to a projective complex orbifold \(Y=\widehat X/C_{n,1}\). Here \(\widehat X\) is \(X\) blown up at \(k+n-1\) points, some infinitely near, and \(C_{n,1}=[n+2,2,\dots,2]\) is a contracted chain. \(Y\) is of general type and \(K_Y\) is **not nef**.

*Proof.* By Grauert's linearization (\(H^1\) of \(T_{\mathbb P^1}\otimes N^{-\nu}\) and of \(N^{1-\nu}\) vanish for \(N=\mathcal O(-m)\), \(m\ge1\)), a neighbourhood of the holomorphic \((-m)\)-curve is biholomorphic to PPS's complex model, so their \(n-1\) blow-ups and the chain sit inside \(\widehat X\). In the PPS family, the general fibre \(W_t\cong V_{-4}\) and the central fibre \(W_0=U/C_{n,1}\) satisfy \(W_t\setminus B_{n,1}\cong W_0\setminus(\text{cone})\). Hence \(V=(M\setminus V_{-4})\cup(W_0)\cong Y\). For the minimal resolution chain the discrepancies are \(a_i=-(n-i)/n\), \(i=1,\dots,n-1\) (data file). Any \((-1)\)-curve \(C\) meeting component \(i\) transversally once has \(K_Y\cdot C=-1-a_i=-i/n<0\). Such a curve exists, either PPS's curve \(C\) in \(U\) or any remaining generic exceptional curve. ∎

**Consequences.**
1. \(K_Y\) is not ample, so the orbifold Aubin–Yau theorem supplies no KE metric. Any Einstein orbifold metric on \(V\) is a **non-Kähler** negative Einstein metric on a non-minimal general-type orbifold. The Wahl branch of the Q1 trichotomy is Q1 posed on a singular member of the same smoothing family.
2. **Transfer principle (superseded by §8.7: only the \(+\)-chirality package transfers; \(T_-^{\rm orb}\), local characters and point-sensitive data do not; the converse sentence below is withdrawn).** WFL (Theorem 93.A, all orbifold metrics), Lemma 93.I (equal expected dimensions), and K²-invariance (\(2e_{\rm orb}+3\tau_{CW}=2e+3\tau\), \(a_V^2=a_M^2\)) show that every obstruction derived from supplied unperturbed Seiberg–Witten fields, Chern–Weil/Gauss–Bonnet/signature integrals, and index counts has identical hypotheses and conclusions on \(V\) and on \(M\). In particular WFL reproduces exactly LeBrun's obstruction \(k\ge A/3\) on \(V\) and no stronger one. Conversely, a proof of Q1 nonexistence on \(M\) by such methods would automatically exclude the Wahl channel. Separating the smooth and orbifold alternatives requires data invisible to these methods, namely the local geometry at \(p\) (§5–§6) or a genuinely Einstein-differential argument.

## 5. Explicit characters of the supplied classes and forced zeros

**Proposition 93.C** (odd \(n\ge3\), under Prop. 93.Y). For \(x\in H^2(M)\), \(x|_{V_{-4}}=(x\cdot S)u\) with \(u\) a generator of \(H^2(V_{-4})=\mathbb Z\). Hence \(E_i|_{V_{-4}}=-\varepsilon_iu\) with \(\varepsilon=(1,-1,-1,-1)\), and \(K_M|_{V_{-4}}=2u\) (\(K\cdot S=2\)). Since \(K|_B\) has order \(n\) in \(H^2(B)=\mathbb Z_n\) (Cartier index \(n\) of a T-singularity), \(u_B\) is a generator and \(u_B=hK|_B\) with \(h=2^{-1}\bmod n\). The basic class \(c_1=-K_M+2\sum_{i\in F}E_i\) therefore has local twist \(m=nj\) with
\[
j_F=\sum_{i\in F\cap\{1,..,4\}}(-\varepsilon_i h)\bmod n .
\]
Generic exceptional classes away from \(V_{-4}\) and \(K_X\) contribute nothing. The Step-89 isotropy table shows that \(\Phi(p)\) can be nonzero only for \(j\in\{0,1\}\), i.e. \(m\in\{0,n\}\); these are the twists of \(\mp K\) type, and both lie in the extendible set. Counting over the 16 sign patterns on \(E_1,\dots,E_4\) (data file): for \(n=3\), 6/16 force \(\Phi_\infty(p)=0\); for every odd \(n=5,\dots,15\), 8/16 do. The \(+K\)-side classes give \(j\mapsto1-j\) and the same counts. For \(n=2\) the extendible set is \(\{0,2\}\), which equals the allowed set, so **no** supplied class has a forced zero.

Thus, for \(n\ge3\), for every orbifold metric on \(V\) — Einstein or not — the orbifold monopoles of at least 6 of the 16 local sign classes vanish at the Wahl point. Their first jets are also invariant-free (Step 89: Phi_first_jet = 0 for every twist), so they vanish to order at least two. For \(n=2\) the channel is locally indistinguishable even at this level.

## 6. Local Einstein algebra at a Wahl point and the remaining implication

**Lemma 93.W.** Let \(g\) be any Γ-invariant metric on the uniformizer with \(\Gamma=\frac1{n^2}(1,n-1)\), \(n\ge3\). Then \(\Lambda^+_0\) splits invariantly as \(\mathbb R\omega_0\oplus\operatorname{Re}\Lambda^{2,0}\) with weights \(0,\pm n\). Every Γ-invariant element of \(\operatorname{Sym}^2_0\Lambda^+\) has weight \(0\) (weights \(\pm n,\pm2n\) are nonzero mod \(n^2\) because \(n\nmid2\)). Hence
\[
W^+(p)=\mu\,\operatorname{diag}(2,-1,-1)\quad\text{in the basis }(\omega_0/\sqrt2,\operatorname{Re}\Lambda^{2,0}),
\]
and every invariant self-dual 2-form at \(p\) is a multiple of \(\omega_0\). For \(n=2\) the weight \(2n=n^2\) admits a 3-dimensional invariant subspace. In particular, an Einstein orbifold metric at a Wahl point with \(n\ge3\) has Kähler-type \(W^+\) algebra at \(p\), but the eigenvalue \(\mu\) is not tied to \(s/12\). All orbifold harmonic self-dual forms and all \(F_A^+=q(\Phi)\) are multiples of \(\omega_0\) at \(p\).

**What WFL does and does not supply for Einstein \(V\).** If \(g\) is Einstein with \(s=-\lambda\), the transferred fields satisfy globally on \(V\)
\[
0\le U\le\lambda,\quad 4\int|\nabla_A\Phi|^2=\int U(\lambda-U),\quad
\tfrac18\int U^2-4\pi^2\|a^+\|^2=\tfrac12\|d\alpha\|^2,
\]
together with the self-dual Hodge–Weitzenböck identity for \(F_A^+\) and \(\delta W^+=0\). By the transfer principle, integral combinations of these reproduce on \(V\) exactly what they give on \(M\). The new local information consists of:
(a) for \(n\ge3\), forced double zeros of \(\Phi_\sigma\) at \(p\) for 6/16 or 8/16 of the local sign classes, simultaneously for one metric when \(b^+>1\);
(b) Lemma 93.W.
Neither yields a topological inequality by itself, because a forced zero costs \(\int(\lambda-U)\) only in proportion to a local curvature scale that is not topologically controlled.

The precise missing implication is therefore: *a quantitative estimate, for negative Einstein orbifold metrics, of \(\int(\lambda^2-U_\sigma^2)\) or of \(\|d\alpha_\sigma\|^2\) for a class \(\sigma\) whose field is forced to vanish at an isolated orbifold point, uniform in the geometry, or a construction showing that such a defect can be made arbitrarily small.* The second alternative is natural to test on Kähler orbifold metrics on \(Y\). On \(Y\), Kähler monopoles are holomorphic sections vanishing on divisors through \(p\), so the forced zeros are the (−1)-curves through \(p\). Whether their cost is visible in the optimal LeBrun inequality — which uses only the maximizing class and has slack \(4\pi^2(A/3-k)\) — determines whether this local datum can enter Q1 at all.

## 7. Status

Proved: Theorem 93.A (given (S); \(b^+=1\) needs its chamber input); Lemmas 93.R, 93.Q, 93.I, 93.W; Prop. 93.Y (dependent on the PPS complex-model structure as recorded in A02 Step 102 §1, plus Grauert linearization); Prop. 93.C (dependent on 93.Y and on the identification of the smooth-family canonical class with the Milnor-fibre canonical lift).
Exact computations: Kawasaki/RR/signature-defect consistency for \(n\le8\); extendible-coset characterization; supplied-class twist multisets for odd \(n\le15\).
Not proved: any Einstein exclusion on \(V\); the orbifold–smooth SW-invariant equality (expected by Lemma 93.I plus gluing of the unobstructed flat reducible bubble on the filler, but not needed for 93.A); the even-\(n\) character computation (spinᶜ lift, not only determinant).
Strategic reading: the Wahl branch does not offer a cheaper route to Q1. It is the orbifold version of Q1, with identical integral and field data. Q1 progress must come from a genuinely Einstein-differential mechanism or from a construction, and the same mechanism would then decide both branches.

## 8. Independent verification and corrections (authoritative; supersedes conflicting text above)

Source: `trace/ttcs/results/step93_ttcs01_verifier1_integration.md` (branches `step93_ttcs01_sub1_verifier.md`, `sub2_verifier.md`).

1. **Gauge factor.** \(A\) is the determinant connection (\(D_A=D_{A_0}+\frac i2c(a)\)); with \((A,\Phi)\mapsto(A-2u^{-1}du,u\Phi)\) the gauge is \(u=e^{if/2}\). The real primitive \(f\) exists globally on \(B^*\).
2. **Bootstrap.** \(W^{2,4}\not\subset C^{1,\alpha}\) in dimension 4. The correct chain is \(\Phi'\in W^{1,4}\cap L^\infty\Rightarrow a'\in W^{2,4}\subset C^{0,\alpha}\cap W^{1,p}\Rightarrow\Phi'\in W^{1,p}\Rightarrow a'\in W^{2,p}\ (p>4)\Rightarrow C^{1,\alpha}\), and then iteration. The Coulomb problem \(da'=F,\ d^*a'=0,\ \iota_\nu a'=0\) is the first-order Hodge problem: Sobolev Poincaré primitive, then a Neumann correction; uniqueness holds by absolute \(H^1(B)=0\). Lemma 93.R is proved after these repairs. Its ingredients are standard, and the lemma is a short adaptation rather than a new removability phenomenon.
3. **Lemma 93.Q.** Correct. The spinor is equivariant for the fibre representation \(\gamma_0\otimes\chi\), not an invariant \(\mathbb C^4\)-valued function. The extension is exactly \(\operatorname{res}(\mathfrak s)\), with no character shift.
4. **Item 4 / mixed estimate.** (S) for one recovery family does not give supply for other metrics; item 4 needs metric-wise supply for all smooth metrics. The unperturbed SW system is **not** conformally covariant: Dirac weight \(\Omega^{-3/2}\) differs from curvature weight \(\Omega^{-1}\). The orbifold estimate \(\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A\) is correct. It follows either from fresh supply and WFL for each conformal metric with LeBrun's orbifold argument, or directly from A02 §4 curvature-integral recovery (\(s=W^+=0\) on the filler, and the transition contribution tends to zero).
5. **Index computation status.** The script uses 50-digit mpmath with rational reconstruction; it is numerical evidence, not exact cyclotomic arithmetic. The verifier supplied an exact all-\(n\) proof. With \(H(a)=\frac1p\sum_k\zeta^{ka}/(1-\zeta^{-k})=(p-1-2a)/(2p)\) for \(0\le a<p\), one has \(\delta(m)-\delta(m-1)=H([-(n+1)m]_p)\). Writing \(m=an+b\) and \(c=n-a-1\),
\[
2n^2(\delta(an+b)-\delta(0))=\begin{cases}b((n+1)b+2na-n(n-1)),&b\le c,\\(b-n)((n+1)b-2nc),&b>c,\end{cases}
\]
which vanishes only for \(b=0\). Hence \(\delta(m)=\delta(0)\iff m\in n\mathbb Z/n^2\) for **every** \(n\ge2\). The values \(\delta(0)=(1-n^{-2})/12\) and \(\tau_{CW}-\tau_{\rm top}=\frac23(1-n^{-2})\) follow from the Dedekind-sum identity. The discrepancy entries in the JSON are assigned formulas, verified by hand from \(\sum_ja_jC_j\cdot C_i=K\cdot C_i\). The ALE weight analysis in Lemma 93.I has been made explicit. Indicial exponents are \(-3/2-\mu\) with \(|\mu|\ge3/2\) (Friedrich), so none lies in \((-3,0)\). The cylindrical \(L^2\) threshold \(-3/2\) and the ALE \(L^2\) threshold \(-2\) both lie in that root-free interval.
6. **Prop. 93.Y scope.** The result is existential and marked. One must choose the holomorphic sphere and the marked PPS complex-model embedding from the outset. A homology diffeomorphism does not identify arbitrary embedded sphere neighbourhoods, so the result does not cover every embedding in Thm 102.R. It covers odd \(n\ge3\) through \(V_{-4}\) and \(n=2\) through \(V_{-3}\), but not the even-\(n\ge4\) route through \(B_{2,1}\#\overline{\mathbb{CP}}^2\). The PPS identification is a marked smooth identification of complements, not a biholomorphism of fibres. Projectivity uses algebraic contraction of the rational configuration. Non-nefness is correct. KE exclusion for **every** orientation-compatible complex structure follows from the transferred scalar estimate: a negative KE metric would have \(\int s^2=32\pi^2(A-k)<32\pi^2A\). Any Einstein metric is therefore negative and non-Kähler in this orientation.
7. **Transfer principle repaired.** What transfers is \(a^2\), \(T_+^{\rm orb}=A-k\), extendible Dirac indices, metric-wise supply, and the scalar and \(W^+\) LeBrun bounds. \(T_-^{\rm orb}=T_-(M)-4\sum(1-n_j^{-2})\) does **not** transfer; A02 shows the \(W^-\)-side bound is slack for this family. Local characters, forced zeros, full SW invariants and moduli geometry also do not transfer. The statement "a proof on \(M\) by any field/index/curvature argument kills \(V\)" is withdrawn. The valid form: the standard \(+\)-chirality LeBrun argument gives the same threshold on \(V\) and \(M\).
8. **Prop. 93.C.** The exact order \(n\) of \(K_M|_B\) needs the relative canonical marking of the PPS smoothing, equivalently the free-quotient ALE model, in which the holomorphic volume form transforms by an order-\(n\) character; the Cartier index alone is not enough. The twist formula with factor \(h\) and the counts are confirmed: for \(n\ge5\) the forced classes are exactly the odd-cardinality subsets of \(\{1,..,4\}\). The positive-spinor weights are \(nj,\ n(j-1)\), and cotangent weights \(\pm1,\pm(n-1)\) cannot cancel these, so forced zeros have order \(\ge2\). Simultaneous fields need simultaneous supply.
9. **New: forced-subfamily selection (verifier).** The forced set is closed under complementation (\(j_{F^c}=1-j_F\)), so its local sign vector has mean zero. Averaging gives \(\operatorname{Avg}_{\rm forced}(a_F^+)^2\ge|K_X^+|^2+\sum_{i>4}|E_i^+|^2+\operatorname{Avg}|\sum_{i\le4}\sigma_iE_i^+|^2\ge A\). Under simultaneous supply, WFL can therefore be run on forced-zero structures alone. The limit has \(\Phi(p)=0\), \(\nabla_A\Phi(p)=0\), and \(\int U^2\ge32\pi^2A\). It follows that \(\int(s^-)^2>32\pi^2A\) **strictly** for every orbifold metric on \(V\) (\(n\ge3\)), since equality would force \(\nabla_A\Phi=0\) and hence \(\Phi\equiv0\). This is strictness, not a uniform gap. Class selection is thus not the missing link.
10. **Missing implication, sharpened.** With a uniformizer regularity radius \(r_0\) at \(p\) (uniform elliptic control, \(\lambda r_0^2\) bounded), the double zero gives \(\int_{B_{cr_0}}(\lambda^2-U^2)\ge c'\lambda^2r_0^4/n^2\). The unresolved quantity is a lower bound on the dimensionless regularity scale \(\lambda r_0^2\) at the Wahl point along Einstein (or almost-Einstein) sequences, or control of the defect when that scale collapses through Ricci-flat bubbling at \(p\). The natural tool is a bubble tree that retains the marked spinᶜ character: can a forced character migrate into ever smaller bubbles at vanishing global defect? The proposed Green-function/conformal shortcut is unjustified. The Kähler-wall test on \(Y\) is a plausible construction route, but the zero divisor of the selected twist must be identified explicitly; it need not be a (−1)-curve through \(p\), and its cost is not yet shown to scale with area.
