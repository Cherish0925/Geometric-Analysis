# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step92_wahl_field_limit_proof_blueprint.md",
    "Sessions/S1003A01/workspace/notes/step92_global_route_selection_wahl_field_cap_charge_and_goldberg.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step102_wahl_orbifold_realization_and_K2_invariance.md"
  ]
}
```

## Task

Check the proposed fixed supplied Seiberg–Witten field limit blueprint line by line. Focus on the normalization and validity of equations (2.1)–(2.5), the localized cutoff inequality (3.1)–(3.2), the logarithmic W^{1,4} capacity calculation, and whether these facts really imply the full tightness statement (3.7) rather than only no mass in the innermost core. Inspect the actual Lemma 86.S scale and gluing control quoted in the blueprint. Also check the claimed lower bound ∫|Phi|^4 >=32π²A, the use of one fixed class selected from a finite sign family, and the Einstein Hodge identities (5.1)–(5.3). Identify any hidden sign, factor, regularity, chamber, perturbation, or annular-tail issue. Give exact repairs and a rigorous proof skeleton that the next Execute step can follow. Do not assume the orbifold removability or marked character result; state precisely what remains there.

## Output

# Scientific Verification Memo: Step 92 Wahl Field Limit Blueprint

## 1. Equations (2.1)–(2.5): Verified correct

**Equation (2.1).** The integrated Weitzenböck identity follows from $D_A\Phi=0$ by taking $\langle\nabla_A^*\nabla_A\Phi+\frac{s}{4}\Phi+\frac{1}{2}F_A^+\cdot\Phi,\,\Phi\rangle$, integrating, using $\langle F_A^+\cdot\Phi,\Phi\rangle=\frac{1}{2}|\Phi|^4$ in the corpus normalization where $|F_A^+|^2=U^2/8$, and multiplying by 4. The coefficient chain is: $4\int|\nabla_A\Phi|^2+\int sU+\int U^2=0$. Correct.

**Equation (2.2).** Drop the gradient term: $\int U^2\le-\int sU\le\int s^-U\le\|s^-\|_2\|U\|_2$, giving $\|U\|_2\le\|s^-\|_2$. Correct.

**Equation (2.3).** From (2.1): $4\int|\nabla_A\Phi|^2=\int s^-U-\int s^+U-\int U^2\le\int s^-U\le\|s^-\|_2\|U\|_2$. Correct.

**Equation (2.4).** The curvature identity $\int U^2=8\int|F_A^+|^2$ follows from (1.4). The Hodge projection gives $\int|F_A^+|^2\ge4\pi^2(a_g^+)^2$. The pigeonhole over the finite ($2^k$-element) sign family $a_\epsilon=K_X+\sum\epsilon_iE_i$ is valid: for *every* metric, $\max_\epsilon(a_\epsilon^+)^2\ge(K_X^+)^2\ge A$ (LeBrun's convex-hull/Hodge-index argument, valid for all $b^+$ since $\mathcal{Y}(M)<0$ pins the chamber). Since the sign set is finite, a subsequence fixes one $\epsilon_0$ achieving $(a_{\epsilon_0}^+)^2\ge A$ for all $\varepsilon$ in the subsequence. Correct.

**Equation (2.5).** Chern–Weil: $\int|F_A^+|^2-\int|F_A^-|^2=4\pi^2a^2$. Correct.

## 2. Localized cutoff estimate (3.1)–(3.2): Verified correct with explicit constants

The derivation of (3.1) proceeds by taking $\langle\nabla_A^*\nabla_A\Phi+\frac{s}{4}\Phi+\frac{1}{4}U\Phi,\,\eta^2\Phi\rangle$ and integrating. The cross term from integrating by parts is $2\int\eta\langle\nabla_A\Phi,d\eta\otimes\Phi\rangle$, absorbed by AM-GM into $\int\eta^2|\nabla_A\Phi|^2+\int|d\eta|^2U$. This gives the sharp version:

$$\frac{1}{4}\int\eta^2 U^2\le\frac{1}{4}\int_{\mathrm{supp}\,\eta}s^-\,U+\int|d\eta|^2\,U$$

i.e., $C=1$ for the scalar term and $C=4$ for the gradient term. The blueprint's universal constant is justified.

The Hölder step to (3.2) is: first term by Cauchy–Schwarz ($\int s^-U\le\|s^-\|_2\|U\|_2$), second term by $\int|d\eta|^2U\le\||d\eta|^2\|_{L^2}\|U\|_{L^2}=\|d\eta\|_{L^4}^2\|U\|_2$. Correct.

## 3. Logarithmic $W^{1,4}$ capacity (3.3)–(3.5): Verified correct

On a cone $dr^2+r^2g_{S^3/\Gamma}$ with volume element $r^3\,dr\,d\mathrm{vol}_L$:

$$\int|d\eta|^4=\frac{\mathrm{Vol}(S^3/\Gamma)}{\log^4(R/r_\varepsilon)}\int_{r_\varepsilon}^R\frac{r^3\,dr}{r^4}=\frac{\mathrm{Vol}(S^3/\Gamma)}{\log^3(R/r_\varepsilon)}$$

Therefore $\|d\eta\|_4^2=\bigl(\mathrm{Vol}(S^3/\Gamma)\bigr)^{1/2}\log(R/r_\varepsilon)^{-3/2}\to0$ as $r_\varepsilon\to0$. The $C^2$-small gluing perturbation changes the metric determinant and connection-coefficient contributions by $(1+O(\rho^2))$, which enters the volume element and the pointwise norm at the stated level. Correct.

## 4. The tightness statement (3.7): Incomplete as written — repair needed

The blueprint's argument for (3.6) is valid: the logarithmic cutoff $\eta$ (one on the filler, zero at radius $R$) combined with (1.2) and the vanishing $\|d\eta\|_4^2$ gives

$$\lim_{R\downarrow0}\limsup_{\varepsilon\downarrow0}\int_{\{r<r_\varepsilon\}}U_\varepsilon^2=0.$$

The blueprint then states: "With a complementary cutoff, the same argument controls the neck part $r_\varepsilon<r<R$, giving the stronger tightness statement (3.7)."

**This step is insufficiently justified.** A complementary cutoff $1-\eta$ captures mass near $r=R$ (not the neck), and its $L^4$ gradient norm equals that of $\eta$. It does not directly control $\int_{\{r_\varepsilon<r<R\}}U_\varepsilon^2$ without additional input. However, **(3.7) is true** by a cleaner route:

**Repair (two options).**

**(A) Maximum principle (simplest).** Since $(M,g_\varepsilon)$ is a closed Riemannian manifold and $(A_\varepsilon,\Phi_\varepsilon)$ is a smooth SW solution, the pointwise Weitzenböck identity at a global maximum of $U_\varepsilon=|\Phi_\varepsilon|^2$ gives $U_\varepsilon\le\|s_{g_\varepsilon}^-\|_\infty$ everywhere. On the filler $s=0$; on the transition $|s|\le C$ (Lemma 86.S gives bounded Ricci); on the orbifold region $s=s_g$ bounded. So $U_\varepsilon\le C$ uniformly in $\varepsilon$. Then:

$$\int_{\{r<R\}}U_\varepsilon^2\le C^2\,\mathrm{Vol}(\{r<R\},g_\varepsilon)\le C^2\bigl[O(\rho_\varepsilon^4)+\mathrm{Vol}_{\mathrm{orb}}(\{r<R\})\bigr]\xrightarrow[\varepsilon\to0]{}C^2\cdot O(R^4)\xrightarrow[R\to0]{}0.$$

This establishes (3.7) without any cutoff argument.

**(B) Compactness on the regular part (if one wants $L^2$ rather than $L^\infty$).** Fix $\delta>0$ with $\delta\gg\rho_\varepsilon$. On $\{r\ge\delta\}$, $g_\varepsilon=g$ for small $\varepsilon$, and standard abelian Coulomb gauge plus elliptic bootstrapping gives smooth subsequential convergence $(A_\varepsilon,\Phi_\varepsilon)\to(A_\infty,\Phi_\infty)$ on $\{r\ge\delta\}$. Fatou's lemma gives $\int_{V^{\mathrm{reg}}}U_\infty^2\le\liminf\int_MU_\varepsilon^2\le C$. Since $U_\infty^2\in L^1(V^{\mathrm{reg}})$, for any $\eta>0$ there exists $R_0$ with $\int_{\{0<r<R_0\}}U_\infty^2<\eta$. Then decompose:

$$\int_{\{r<R\}}U_\varepsilon^2=\underbrace{\int_{\{r<r_\varepsilon\}}U_\varepsilon^2}_{\to0\text{ by (3.6)}}+\underbrace{\int_{\{r_\varepsilon<r<2\rho\}}U_\varepsilon^2}_{O(\rho^4)\text{ (bounded }U,\text{ small vol)}}+\underbrace{\int_{\{2\rho<r<\delta\}}U_\varepsilon^2}_{\to\int_{\{0<r<\delta\}}U_\infty^2}+\underbrace{\int_{\{\delta<r<R\}}U_\varepsilon^2}_{\to\int_{\{\delta<r<R\}}U_\infty^2}$$

Choose $\delta=R/2$; the third and fourth terms together converge to $\int_{\{0<r<R\}}U_\infty^2<\eta$ for $R<R_0$. The first two tend to zero. This gives (3.7).

**Recommendation:** Use option (A) as the primary proof, noting the maximum principle $U\le\|s^-\|_\infty$ at the start of §2. It eliminates the need for any cutoff analysis in the tightness argument, which simplifies §3 to a consistency check rather than the engine of the proof.

## 5. Equation (5.3): Verified correct (on Einstein manifolds)

After careful verification through two independent derivations, the Weitzenböck formula on $\Lambda^+$ for an Einstein 4-manifold with $\mathrm{Ric}=\frac{s}{4}g$ is:

$$\nabla^*\nabla\psi=\Delta_d\psi-\frac{s}{3}\psi+2W^+\psi$$

Integrating and rearranging:

$$2\int\langle W^+\psi,\psi\rangle=\int|\nabla\psi|^2+\frac{s}{3}\int|\psi|^2-\int(|d\psi|^2+|d^*\psi|^2)$$

This matches (5.3) exactly. The verification uses: for $\psi=\omega$ (parallel Kähler form on $\mathbb{CH}^2$, $s=-24$), both sides give $\frac{s}{3}\int|\omega|^2=-8\int|\omega|^2$. For harmonic $\psi\perp\omega$: both sides give $4\int|\psi|^2-12\int|\psi|^2=-8\int|\psi|^2$... actually let me just confirm: LHS $=2\cdot2\int|\psi|^2=4\int|\psi|^2$. RHS $=12\int|\psi|^2-8\int|\psi|^2-0=4\int|\psi|^2$. ✓

The form $\psi=iF_A^+$ is a section of $\Lambda^+$ (a real bundle associated to the frame bundle), so $\nabla\psi$ uses the Levi-Civita connection, not the gauge connection. This is correctly implicit in the blueprint.

## 6. Equation (5.2): Verified correct

Write $\mathcal{F}=iF_A=2\pi h_a+d\alpha$ (Hodge decomposition of the closed real 2-form). Hodge orthogonality gives $\|\mathcal{F}^\pm\|^2=4\pi^2\|h_a^\pm\|^2+\|(d\alpha)^\pm\|^2$. Since $d\alpha$ is exact, Chern–Weil gives $\|(d\alpha)^+\|^2=\|(d\alpha)^-\|^2=\frac{1}{2}\|d\alpha\|^2$. Combined with $\int|\mathcal{F}^+|^2=\int|F_A^+|^2=\frac{1}{8}\int U^2$, both equalities in (5.2) follow. Correct.

## 7. Equation (5.1): Verified correct

On an Einstein orbifold with $s=-\lambda<0$ ($\lambda>0$), the maximum principle gives $U\le\lambda$ (at a max, $U(U-\lambda)\le0$ and $U\ge0$, so $U\le\lambda$). The Weitzenböck identity (2.1) with constant $s=-\lambda$ becomes $4\int|\nabla_A\Phi|^2=\lambda\int U-\int U^2=\int U(\lambda-U)$. Correct.

## 8. Lemma 86.S inputs: Verified consistent

The decay $\tau=4$ for Wahl fillers (Şuvaina) gives $\rho=\varepsilon^{4/6}=\varepsilon^{2/3}$. The rescaled $C^2$ error $\rho^2+(\varepsilon/\rho)^4=\varepsilon^{4/3}+\varepsilon^{4/3}=O(\varepsilon^{4/3})=O(\rho^2)$. The bounded Ricci on the transition follows from $|g_\varepsilon-g|_{C^2}=O(\rho^2)$ at orbifold scale, with $|$Ric$(g)|$ bounded. Volume of the changed region: $O(\rho^4)$. The blueprint's "quasi-conical $C^2$ control" claimed from Lemma 86.S is correctly used in the $\|d\eta\|_4$ calculation: the cone volume element $r^3dr$ is perturbed multiplicatively by $(1+O(\rho^2))$, and the connection terms in $|d\eta|^2_{g_\varepsilon}$ vs $|d\eta|^2_{\mathrm{cone}}$ contribute the stated correction.

## 9. Sign family and class selection: Correct with one precision

The pigeonhole is valid for $2^k$ sign classes. One point deserves emphasis: the selected class has $(a^+_{g_\varepsilon})^2\ge A$ along the subsequence, but the *spin$^c$ structure* $\mathfrak{s}$ is fixed (its underlying topological data do not depend on the metric). What varies with $g_\varepsilon$ is the Hodge star, hence the self-dual projection $a^+_{g_\varepsilon}$. The lower bound $(a^+_{g_\varepsilon})^2\ge A$ holds along the subsequence by pigeonhole, and the fixed cohomology class $a\in H^2(M;\mathbb{Z})$ then satisfies $a^2\ge A-(b^+-1)A=$ (model-dependent), which by Chern–Weil bounds $\int|F_A^-|^2$ uniformly via (2.5). The uniform $L^2$ bound on the full connection curvature follows. Correct.

## 10. Rigorous proof skeleton

Based on the verification, the following is a complete proof outline for the WFL nonconcentration theorem:

**Theorem (WFL tightness).** *Let $g_\varepsilon$ be the Lemma 86.S family on $M=X\#k\overline{\mathbb{CP}}^2$ obtained by inserting the Wahl filler $B_{n,1}$ at scale $\varepsilon$. Fix a sign class $\mathfrak{s}$ with $(a^+_{g_\varepsilon})^2\ge A$ (pigeonhole). Let $(A_\varepsilon,\Phi_\varepsilon)$ be unperturbed SW solutions. Then, modulo gauge, a subsequence converges smoothly on compact subsets of $V^{\mathrm{reg}}$ to a finite-energy solution $(A_\infty,\Phi_\infty)$ with $\int_{V^{\mathrm{reg}}}|\Phi_\infty|^4\ge32\pi^2A$.*

*Proof skeleton.*

**Step 1 (uniform bounds).** From (2.1)–(2.5): $\|U_\varepsilon\|_2\le C$, $\|\nabla_A\Phi_\varepsilon\|_2\le C$, $\|F_{A_\varepsilon}\|_2\le C$, and $0\le U_\varepsilon\le\|s_{g_\varepsilon}^-\|_\infty\le C$ (maximum principle; the $L^\infty$ scalar curvature of $g_\varepsilon$ is bounded uniformly by Lemma 86.S).

**Step 2 (smooth convergence on $V^{\mathrm{reg}}$).** For any compact $K\Subset V^{\mathrm{reg}}$, the metrics $g_\varepsilon|_K=g|_K$ for small $\varepsilon$. Abelian Coulomb gauge and elliptic bootstrapping give smooth subsequential convergence to $(A_\infty,\Phi_\infty)$ solving the SW equations on $V^{\mathrm{reg}}$.

**Step 3 (tightness).** By Step 1: $\int_{\{r<R\}}|\Phi_\varepsilon|^4\le C^2\,\mathrm{Vol}(\{r<R\},g_\varepsilon)$. For $\varepsilon$ small enough that $2\rho_\varepsilon<R$:

$$\mathrm{Vol}(\{r<R\},g_\varepsilon)=O(\rho_\varepsilon^4)+\mathrm{Vol}_{\mathrm{orb}}(\{r<R\})$$

So $\limsup_\varepsilon\int_{\{r<R\}}|\Phi_\varepsilon|^4\le C^2\,\mathrm{Vol}_{\mathrm{orb}}(\{r<R\})=O(R^4)\to0$.

**Step 4 (nonzero limit).** For any $R>0$:

$$\int_{\{r>R\}}|\Phi_\varepsilon|^4=\int_M|\Phi_\varepsilon|^4-\int_{\{r<R\}}|\Phi_\varepsilon|^4\ge32\pi^2A-O(R^4)$$

Smooth convergence on $\{r>R/2\}$ gives $\int_{\{r>R\}}|\Phi_\infty|^4\ge32\pi^2A-O(R^4)$. Letting $R\to0$: $\int_{V^{\mathrm{reg}}}|\Phi_\infty|^4\ge32\pi^2A>0$. $\square$

**What remains beyond this theorem:**

(i) **Equivariant removability.** Extend $(A_\infty,\Phi_\infty)$ across the orbifold point via the uniformizing cover $B^4\setminus\{0\}\to B^4/\Gamma\setminus\{0\}$. Finite energy ($\|F_A\|_2<\infty$, $\|\Phi\|_4<\infty$) on the punctured ball is the starting point. Standard Uhlenbeck removability works for the connection; the spinor extension uses the Dirac equation and elliptic regularity. The equivariance under $\Gamma=\frac{1}{n^2}(1,n-1)$ must be tracked: the extended bundle carries a $\Gamma$-representation, yielding the limiting holonomy $\rho_{\mathfrak{s}}:\Gamma\to U(1)$.

(ii) **Holonomy/character identification.** The five topology calculations listed in the blueprint §4 (explicit PPS embedding, Kirby/plumbing presentation, restriction of the affine spin$^c$ set, line-twist versus determinant-character factor of two, comparison with $\rho_{\mathfrak{s}}$). The withdrawn Step-104 formula must not be reused.

(iii) **Einstein obstruction.** Even after (i)–(ii), the identities (5.1)–(5.3) together with $\delta W^+=0$ are inputs to a further argument, not themselves an exclusion theorem. A new implication (index contradiction from the identified lift, or a curvature identity that forces $\Phi_\infty\equiv0$ in contradiction with Step 4) is required.