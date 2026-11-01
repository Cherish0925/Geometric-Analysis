# TTCS Independent Branch Record

```json
{
  "step_id": 48,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/notes/step46_lemmaM_elementary_and_AC.md",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md",
    "Sessions/S1003A02/workspace/scripts/step48_bianchi_indicial.py",
    "Sessions/S1003A02/workspace/data/step48_bianchi_indicial.json"
  ]
}
```

## Task

Verify §3 of Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md (localized complex-hyperbolic coercivity) as rigorous analysis. Check: (1) Proposition 48.3: L=½(∇*∇−2R̊) on symmetric 2-tensors over any closed ball quotient with Ric=−6g satisfies ⟨Lu,u⟩≥‖u‖², via the L²-orthogonal decomposition TT ⊕ closure(im T), T(X,f)=δ*X+fg, the intertwining LT=TD with D=diag(½Δ_H+6, ½Δ_0+6), commutation [T*T,D]=0, and Koiso's identity on TT (Step 44 G1, R̊≤4). Are the intertwining identities Δ_Lδ*=δ*Δ_H and Δ_L(fg)=(Δf)g correct on Einstein manifolds, and does the commuting-operator argument legitimately give ≥6‖Tw‖²? (2) Proposition 48.4 (Combes–Thomas) and Theorem 48.L, including the nonlinear absorption, Dirichlet DeTurck gauge on a region with boundary, weighted elliptic regularity, and uniformity in Γ, B, k. (3) Lemma 48.5: the scalar-curvature linearization in Bianchi gauge s'(h)=½(Δ+12)tr h (check sign conventions with Besse 1.174) and the volume formula with boundary flux. (4) Theorem 48.LY: does the combination with Theorem Y (Section 2) legitimately give P ≥ (8π²k − 4ΔV_U − CΛ²)/(1+C)? Watch scale conversions between Ric=−6 and s=−4, and whether the hypothesis is placed on the Yamabe representative consistently. (5) The indicial-root table from workspace/data/step48_bianchi_indicial.json (diagonal Bianchi IX about CH² with A=B=sinh r, C=sinh r cosh r; Ricci formulas in the script docstring) and the interpretation: J-anti triaxial tail e^{-4r} marginal vs volume e^{4r}, U(2) tails e^{-6r}, and the claim that the triaxial mode changes μ_min and |W+|² only at second order. Give corrected statements where needed and say what remains unproved.

## Output

# Memo: §3 of Step 48 (localized complex-hyperbolic coercivity)

Normalisation is \(\operatorname{Ric}_0=-6g_0\), \(\Delta=\delta d\ge0\), and \(\mathring R\) is defined so that \(\mathring R g=\operatorname{Ric}\).

**Summary.**

- Prop. 48.3 is correct, and its proof can be made fully rigorous.
- Prop. 48.4 and Theorem 48.L are correct after three technical repairs:
  - a regularised distance;
  - a form-domain argument;
  - a global (gap-free) DeTurck gauge instead of the Dirichlet gauge.
- Lemma 48.5 has the right sign, but its coefficient \(1/24\) belongs to the \(\operatorname{Ric}=-6\) scale, not to "\(\hat g\) units". It can be rewritten without hypersurface traces.
- Theorem 48.LY follows from Theorem Y, but it silently needs two things:
  - \(c_1^2(X_0)=A\);
  - an \(H^2\) (not \(H^1\)) collar quantity.
- In the indicial table, the root \(\nu=8\) is spurious.
- The statement that the triaxial mode changes \(\mu_{\min}\) and \(|W^+|^2\) only at second order is true. Two short proofs are given in §5.

---

## 1. Proposition 48.3: \(\langle Lu,u\rangle\ge\|u\|^2\)

**Form of \(L\).** On an Einstein manifold, \(\Delta_L=\nabla^*\nabla+2\lambda-2\mathring R\). Hence \(\nabla^*\nabla-2\mathring R=\Delta_L+12\) and \(L=\tfrac12\Delta_L+6\), as the note states.

**Intertwining identities.** Both hold.
- \((fg)\): \(\nabla^*\nabla(fg)=(\Delta f)g\) and \(\operatorname{Ric}\circ fg+fg\circ\operatorname{Ric}-2\mathring R(fg)=2\lambda fg-2\lambda fg=0\). So \(\Delta_L(fg)=(\Delta f)g\) on any Einstein metric.
- \(\delta^*\): \(\Delta_L\delta^*=\delta^*\Delta_H\) is Lichnerowicz's commutation on Einstein manifolds. It is the dual of \(\delta\Delta_L=\Delta_H\delta\).
- Therefore \(LT=TD\) with \(D=\operatorname{diag}(\tfrac12\Delta_H+6,\tfrac12\Delta_0+6)\).

**Entries of \(T^*T\).**
- \(T^*h=(\delta h,\operatorname{tr}h)\), so \(T^*T=\begin{pmatrix}\delta\delta^*&-d\\-\delta&4\end{pmatrix}\).
- From \(\delta(\mathcal L_\xi g)=\nabla^*\nabla\xi-\operatorname{Ric}\xi+d\delta\xi\), one gets \(\delta\delta^*=\tfrac12(\Delta_H-2\lambda+d\delta)\) on Einstein metrics. This commutes with \(\Delta_H\).
- The off-diagonal entries intertwine because \(\Delta_Hd=d\Delta_0\) and \(\Delta_0\delta=\delta\Delta_H\).

**Commuting-operator step.** On a closed quotient the step is rigorous for a simple reason. \(D\) has finite-dimensional eigenspaces \(E_t\) (1-form eigenvalue \(2(t-6)\) for \(\Delta_H\), plus function eigenvalue \(2(t-6)\) for \(\Delta_0\)). \(T^*T\) preserves each \(E_t\). Hence
\[
\langle T^*TDw,w\rangle=\sum_t t\,\|Tw_t\|^2\ge6\|Tw\|^2 .
\]

**Splitting.**
- \(\operatorname{im}T\) is closed because \(T\) has injective symbol. The symbol relation \(\operatorname{sym}(\xi\otimes X)+fg=0\) forces \(f=0\) by rank, and then \(X=0\).
- So \(L^2S^2=TT\oplus\operatorname{im}T\).
- The cross term vanishes: \(\langle Lh,Tw\rangle=\langle T^*h,Dw\rangle=0\).

**TT part.**
- Koiso's identity \(\langle L_Eh,h\rangle=\|d^\nabla h\|^2+\langle(-\lambda-\mathring R)h,h\rangle\) follows from \(\Delta^{d^\nabla}=\nabla^*\nabla+h\circ\operatorname{Ric}-\mathring R\) together with \(\delta h=0\).
- \(\mathring R\le4\) on \(S^2_0\) is consistent with an independent check, which I did:
  - \(\operatorname{tr}_{S^2}\mathring R=-s/2=12\) and \(\langle\mathring R\hat g,\hat g\rangle=s/4=-6\), so \(\operatorname{tr}_{S^2_0}\mathring R=18=3(-2)+6(4)\).
  - The J-anti element \(e_1^2-e_2^2\) (with \(e_2=Je_1\)) has Rayleigh quotient \(-2K(e_1,Je_1)/2=4\).

**Strength of the result.**
- The bound is \(\ge1\) on TT and \(\ge6\) on \(\operatorname{im}T\).
- The proposition is strictly stronger than Step 46 §3 item 4. Coercivity of \(\operatorname{Ric}+6g\) in DeTurck gauge now needs no York decomposition and no scalar constraint.
- The scalar constraint \(s\equiv-24\) is needed only to identify \(\operatorname{Ric}+6g\) with \(\operatorname{Ric}^\circ\), i.e. to connect with \(P\).

## 2. Proposition 48.4 and Theorem 48.L

**Combes–Thomas identity.** It is exact. With \(\nabla(e^{-\phi}u)=e^{-\phi}(\nabla u-d\phi\otimes u)\),
\[
\langle\nabla^*\nabla(e^{-\phi}u),e^{\phi}u\rangle=\langle\nabla u-d\phi\otimes u,\nabla u+d\phi\otimes u\rangle .
\]
The real cross terms cancel. This gives \(\langle e^\phi Le^{-\phi}u,u\rangle\ge(1-a^2/2)\|u\|^2\).

Two points need writing:
1. **Form domain.** For Lipschitz \(\phi\), \(e^{-\phi}H^2\not\subset H^2\). The argument should be run on the bilinear form over \(H^1\) (Lax–Milgram). The adjoint \(e^{-\phi}Le^{\phi}\) obeys the same bound, which gives invertibility.
2. **Regularised distance.** Weighted \(H^2\) regularity and the commutator \([L,\chi]=-\nabla_{\nabla\chi}+\tfrac12\Delta\chi\) need \(|\nabla^2\phi|\) and \(|\nabla^2\chi|\) bounded.
   - \(d=\operatorname{dist}(\cdot,B)\) has singular Hessian on the cut locus. For a union of balls with no separation it has concave kinks along equidistant sets.
   - Replace \(d\) by a \(\Gamma\)-invariant mollification \(\tilde d\) lifted from \(\mathbb{CH}^2\), with \(|\tilde d-d|\le\tfrac18\), \(|\nabla\tilde d|\le1+\eta\), \(|\nabla^2\tilde d|\le C_\eta\). These constants come from bounded geometry only.
   - The rate becomes \(a<\sqrt2/(1+\eta)\), i.e. any \(a<\sqrt2\).

**Dirichlet DeTurck gauge.** The parenthetical argument for it does not close as written.
- Boundary Schauder estimates on \(\{d\ge\tfrac12\}\) need a regular hypersurface \(\partial\{d\ge\frac12\}\). For overlapping balls this hypersurface has corners.
- Uniformity in \(B\) and \(k\) is then not available.

A gap-free replacement:
1. Interpolate \(\tilde g=g_0+\zeta h\), with \(\zeta=1\) on \(\{\tilde d\ge\tfrac12\}\) and \(\zeta=0\) near \(\{\tilde d\le\tfrac14\}\). This needs the hypothesis on \(\{d\ge\tfrac14\}\).
2. Then \(\|\tilde g-g_0\|_{C^{2,\alpha}_b(X_0)}\le C\varepsilon\) on the closed quotient.
3. Step 46 §3 item 2 gives a global harmonic-map gauge, using the Kato-invertible Jacobi operator \(\nabla^*\nabla+6\).
4. The gauged \(h\) agrees with the push-forward of \(g\) on \(\{\tilde d\ge\tfrac12+C\varepsilon\}\).

On \(\operatorname{supp}\chi\subset\{\tilde d\ge1\}\) one has \(\operatorname{Ric}+6\tilde g=\operatorname{Ric}^\circ_g\), because \(s\equiv-24\) holds there. No equation is used in the interpolation zone.

**Linearisation.** \(\operatorname{Ric}'(h)=\tfrac12\Delta_Lh-\delta^*\beta(h)\) with \(\beta=\delta+\tfrac12d\operatorname{tr}\), so \(\operatorname{Ric}'(h)+6h=Lh-\delta^*\beta h\). In nonlinear DeTurck gauge, \(\delta^*\beta=\delta^*O(h\nabla h)\) is part of \(Q\). This matches the note.

**Absorption.**
- \(\chi Q\) is bounded by \(C\varepsilon(|\nabla^2(\chi h)|+|\nabla(\chi h)|)\) plus layer terms in \(\|h\|_{H^1(1\le d\le2)}\).
- \(\|e^\phi\chi h\|_{H^2}<\infty\) because \(\phi=a\min(\tilde d,T)\) is bounded; this is why the cap at \(T\) is needed.
- Absorption works for \(C\varepsilon<\tfrac12\). The estimate follows as stated, with \(\Lambda=\|h\|_{H^1(1\le d\le2)}\).

**Uniformity in \(\Gamma\), \(B\), \(k\).** It holds.
- The \(L^2\) gap is quotient-free (48.3).
- Global \(H^2\) estimates follow by integration by parts on the locally symmetric quotient (\(\nabla\mathrm{Rm}=0\)), with no injectivity radius.
- The cutoff and weight constants are bounded-geometry constants.

**Rate.** The rate \(\sqrt2\) is the Combes–Thomas rate from \(L\ge1\). The decaying root \(\nu=4\) gives \(\|h\|_{L^2(d\ge T)}\sim e^{-(\nu-2)T}=e^{-2T}\), so \(\sqrt2<2\) is consistent.

**Weighting not used downstream.** Theorem 48.LY uses \(T=1\), i.e. the unweighted estimate. The exponential weighting plays no role in 48.LY as written.

## 3. Lemma 48.5

**Sign.** Besse 1.174 gives \(s'(h)=\Delta\operatorname{tr}h+\delta\delta h-\langle\operatorname{Ric},h\rangle\). Bianchi gauge \(\delta h=-\tfrac12d\operatorname{tr}h\) gives
\[
s'(h)=\tfrac12(\Delta-2\lambda)\operatorname{tr}h,
\]
which is \(\tfrac12(\Delta+12)\operatorname{tr}h\) at \(\lambda=-6\). Correct.

**Integration.** With \(\int_\Omega\Delta f=-\oint\partial_\nu f\), one gets \(\int\operatorname{tr}h=\tfrac1{12}\oint\partial_\nu\operatorname{tr}h+O(h^2)\). Hence
\[
\operatorname{Vol}_g-\operatorname{Vol}_0=\tfrac1{24}\oint\partial_\nu\operatorname{tr}h+O(h^2).
\]
Correct.

**Two remaining issues.**
- **Units.** At \(s=-4\) (\(\lambda=-1\)) the coefficient is \(\tfrac14\), not \(\tfrac1{24}\). This is consistent: \(\operatorname{Vol}\) scales by 36 and the flux by 6 under \(\hat g=6g_{(-6)}\), giving \(36\cdot\tfrac1{24}\cdot\tfrac16=\tfrac14\). So \(\Delta V_U\) "in \(\hat g\) units" with \(\tfrac1{24}\) is internally inconsistent. Also, \(\Delta V_U\) is scale-normalised by \(s=-4\); it is not scale-invariant.
- **Hypersurface remainders.** The term \(\delta O(h\nabla h)\) produces \(\oint|h||\nabla h|\) on \(\{d=1\}\). Bounding this by \(\|h\|^2_{H^2}\) needs a trace inequality, which brings back the corner problem.

**Cutoff form (no traces).** Take a cutoff \(\tilde\chi\) (=1 on \(\Omega\)-interior, transition in a layer). Multiply \(\tfrac12(\Delta+2)\operatorname{tr}h=Q_s\) (in \(s=-4\) units) by \(\tilde\chi\) and integrate. In \(s=-4\) units this gives
\[
\int\tilde\chi\,(d\mu_g-d\mu_0)=-\tfrac14\int(\Delta\tilde\chi)\operatorname{tr}h\,d\mu_0+O\big(\|h\|^2_{H^2(\operatorname{supp}\tilde\chi)}\big).
\]
This reduces to the flux formula as \(\tilde\chi\to\mathbf 1_\Omega\), since \(\int(\Delta\tilde\chi)f=\int\langle d\tilde\chi,df\rangle\to-\oint\partial_\nu f\). The divergence term becomes \(\int\langle d\tilde\chi,O(h\nabla h)\rangle\), a layer quadratic.

## 4. Theorem 48.LY

**Logic.** The chain is legitimate:
- Theorem Y bounds \(8\pi^2k-P(\hat g)\le4\Delta V-2\int\Psi\).
- Write \(\Delta V=\Delta V_U+(\text{bulk remainder})\), with \(|\text{bulk}|\le C(P(\hat g)+\Lambda^2)\).
- Drop \(-2\int_{\rm bulk}\Psi\le0\).
- Solve for \(P(\hat g)\), then use \(P(g)\ge P(\hat g)\). This last step is Gauss–Bonnet plus Yamabe minimality of \(\int s^2\) when \(Y<0\).

The hypothesis sits on the Yamabe representative, consistently with Theorem Y. Rescaling \(s=-4\to-24\) (factor \(\tfrac16\)) fixes the scale, so there is no free constant \(c\).

**Three gaps.**
1. **Reference volume.**
   \[
   \Delta V=\Delta V_U+\text{bulk}+2\pi^2\big(c_1^2(X_0)-A\big)\quad(\hat g\text{ units}),
   \]
   because \(\operatorname{Vol}_{s=-4}(X_0)=2\pi^2c_1^2(X_0)\). "Some ball quotient \(X_0\)" must therefore satisfy \(c_1^2(X_0)=A\) (e.g. \(X_0=X\)), or the term must be kept. Topology does not force it unless the cores are known to be punctured \(\overline{\mathbb{CP}}^2\)'s.
2. **Collar quantity.** The volume remainder needs \(\|h\|^2_{H^2}\) on the transition layer of \(\tilde\chi\). The 48.L estimate with \(T=1\) gives \(H^2\) only where \(\chi=1\).
   - The layers must be nested: gauge interpolation in \([\frac14,\frac12]\), \(\chi\)-transition in \([\frac12,1]\), \(\tilde\chi\)-transition in \([1,2]\).
   - Then \(\Lambda:=\|h\|_{H^1(\frac12\le d\le1)}\) suffices.
   - Alternatively, define \(\Lambda\) as an \(H^2\) norm on the volume layer.
3. **Units and scaling.** The \(\frac1{24}\to\frac14\) issue of §3 applies. The term "scale-invariant" should be dropped.

**Repaired statement.** Under the sign-family hypotheses, let the scalar-\(-4\) Yamabe metric \(\hat g\) be \(\varepsilon_0\)-close in \(C^{2,\alpha}_b\) to \(6g_0\) on \(F(\{d\ge\frac14\})\), with \(X_0\) a ball quotient. Define, in \(s=-4\) units,
\[
\Delta V_U^{\tilde\chi}=\int_M(1-\tilde\chi)d\mu_{\hat g}-\int_{X_0}(1-\tilde\chi)d\mu_{6g_0}-\tfrac14\int(\Delta\tilde\chi)\operatorname{tr}h .
\]
Then
\[
P(g)\ \ge\ \frac{8\pi^2k-4\Delta V_U^{\tilde\chi}-8\pi^2\big(c_1^2(X_0)-A\big)-C\Lambda^2}{1+C},
\]
with \(C\) independent of \(\Gamma,B,k\).

**Not covered by 48.LY.**
- The per-core quantity \(D_{W,U}\) used in §4.3 is not defined in the note. Localising \(D_W\) needs a Chern–Simons-type transgression term at the collar, analogous to the flux term. Theorem 48.LY avoids this only because (Y0) is used globally.
- The constant \(C\) is not explicit. The resulting tariff coefficient is \((1-\cdots)/(1+C)\).

## 5. Indicial table

**Background.** I checked the Ricci formulas by hand on \(\mathbb{CH}^2\):
- \(R_{11}\): with \(s=\sinh^2r\), \(R_{11}=-1-\frac{2+3s}{s}+\frac{2(1-s)}{s}=-6\).
- \(R_{00}\): \(R_{00}=-(1+1+4)=-6\).
- The 00-row coefficients \(\nu(2-\nu),\nu(2-\nu),\nu(4-\nu)\) are correct.

**Triaxial mode \(a=-b\).**
- Rows 00 and 33 vanish identically, and row 11 gives \(-\nu(\nu-4)\).
- Roots \(\nu=0,4\) are genuine.

**U(2) mode \(a=b\).**
- With \(u=\nu^2-6\nu\), the \(2\times2\) determinant is \((u-8)(u-4)-(\nu-4)(4\nu-8)=u(u-16)\). This reproduces \(\nu(\nu-6)(\nu-8)(\nu+2)\).
- The script then drops the 00 equation, which is the radial (Hamiltonian-type) equation. Checking eigenvectors against it:

| \(\nu\) | eigenvector | 00 equation | status |
|---|---|---|---|
| 6 | \(c=-4a\) | \(-48a+48a=0\) | genuine |
| \(-2\) | \(c=-\tfrac43a\) | \(-16a+16a=0\) | genuine |
| 0 | \((1,1,2)\), the shift \(r\to r+\delta\) | 0 | genuine (gauge) |
| 8 | \(c=2a\) | \(-96a-64a=-160a\neq0\) | spurious |

- The \(\nu=8\) mode solves the spatial equations but violates the radial one.
- The corrected U(2) row is \(-2\) (growing), \(0\) (gauge), \(6\).
- This agrees with the count of solutions: 6 data minus 1 constraint gives 5 = 2 (triaxial) + 3 (U(2)).
- It also agrees with the pairing \(\nu\leftrightarrow4-\nu\) about \(\rho_0=2\) (volume \(e^{4r}\)): \((0,4)\) and \((-2,6)\). The value 8 has no partner.

**Second-order statement for the triaxial tail.** It is true, by two independent arguments.

1. **Symmetry argument.** The map \(\sigma_1\leftrightarrow\sigma_2,\ \sigma_3\mapsto-\sigma_3\) is an orientation-preserving automorphism of \(\mathfrak{su}(2)\) and an isometry of the background.
   - It maps \(a\mapsto-a\).
   - On \(\Lambda^+\) it maps \(\omega_1\leftrightarrow\omega_2\) and \(\omega_3\mapsto-\omega_3\).
   - In diagonal Bianchi IX, \(W^+=\operatorname{diag}(w_1,w_2,w_3)\) in this basis, so \(w_3\) is even in \(a\).
   - Hence \(\delta w_3=\delta\mu_{\min}=0\), and \(\delta w_1+\delta w_2=0\) by tracelessness.
   - Therefore \(\delta|W^+|^2=2w_3\delta w_3+2w_1(\delta w_1+\delta w_2)=0\).
2. **General argument (any J-anti \(h\)).** J-anti trace-free \(h\) lies in \([\![\Lambda^{2,0}]\!]\otimes\Lambda^-\subset\operatorname{Hom}(\Lambda^+,\Lambda^-)\), which annihilates \(\omega\).
   - So \(\omega_0\) stays self-dual and of norm \(\sqrt2\) to first order.
   - The Weitzenböck identity \(2W^+(\omega,\omega)=|\nabla\omega|^2+\tfrac{2s}3-\langle\Delta_d\omega,\omega\rangle\) then gives \(\delta W^+(\hat\omega,\hat\omega)=\delta s/6\).
   - This vanishes for the constant-\(s\) (Yamabe) representative.
   - With varying \(s\) the first-order term \(\delta s/6\) is present, so the Yamabe normalisation is essential.

The \(\nu=6\) mode carries an \(e_0\)–\(e_3\) J-anti component in radial gauge. The gauge field \(f\partial_r\) with \(f=a/2\) removes it asymptotically, so the "J-invariant" label holds up to gauge.

**Not established.**
- **First-order splitting.** That \(\delta(w_1-w_2)\neq0\) at first order for the \(\nu=4\) tail is generic by parity but not computed. This is what makes the linear \(L^1\) Weyl departure grow like \(R\sim\tfrac14\log\operatorname{vol}\). It follows from the explicit diagonal-Bianchi-IX formula for \(w_i\), a short extension of the script.
- **Coverage of the table.** It covers only diagonal SU(2)-invariant modes. The mixed contact–Reeb and radial–contact components \(h(e_0,e_i),h(e_3,e_i)\), and non-invariant modes, have their own asymptotic weights. These are not computed.
  - The rate-4 marginality and the \(e^{-6r}\) summability of J-invariant tails in general sectors are therefore unproved.
  - If any sector had a decaying root in \((2,4)\), its first-order \(L^1\) Weyl departure would grow exponentially against \(e^{4r}\). This would bear on Theorem K, not on Theorem Y, which sees only \(\Psi\) and is quadratic.

## 6. What remains unproved

- A bound on \(\Delta V_U^{\tilde\chi}\) for an individual core with CH-asymptotic (not exact) collars.
- A collar transgression term making \(D_{W,U}\) well defined.
- Explicit values of \(\varepsilon_0\) and \(C\).
- Bulk regions far from every ball quotient, where the formal common mode lives.
- Hosts with \(c_1^2<3c_2\).
- The complete indicial spectrum, including mixed and non-invariant sectors.
- The first-order Weyl splitting of the \(\nu=4\) tail.