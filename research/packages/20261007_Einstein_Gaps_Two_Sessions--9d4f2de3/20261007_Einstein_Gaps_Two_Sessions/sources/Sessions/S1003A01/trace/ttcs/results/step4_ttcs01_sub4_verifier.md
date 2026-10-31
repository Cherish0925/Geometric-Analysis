# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md"
  ]
}
```

## Task

Analyze and strengthen the fixed-exterior part of the O11 cell programme in light of this precise issue. Suppose a true J-minimizing sequence converges in C^2 on compact regular regions while the CH exterior is fixed. Explain exactly how comparison minimality transfers compactly supported local stationarity/stability to the limit; what is still needed to control an interface stress at the free-interior/fixed-collar interface and justify unique continuation to a locally CH base; and prove the quantitative recovered-volume implication from F=((s+3)^2/3)+1+4|W+|^2>=0: how a deficit delta forces at least delta/4 of background CH volume to be unrecovered. Also assess whether the developing-map extension argument applies unchanged to real-hyperbolic negative Einstein / W+-flat bases relevant to the peer O10 route, making all necessary constant-curvature and completeness hypotheses explicit.

## Output

# Fixed-exterior compactness for the O11 cell: comparison minimality, interface stress, recovered volume, and the real-hyperbolic analogue

## 0. Setting and the convergence hypothesis

**Notation.**
- \(C\) is the cell. It contains the open fixed collar \(U_c\), on which every admissible metric equals the CH metric.
- \(\Omega=C\setminus\overline{U_c}\) is the free region. Its interface with the collar is \(\Sigma\cong S^3\).
- \(J(G)=\int_C|\operatorname{Ric}+G|^2\), and \(J_*=\inf J\) over smooth admissible metrics.
- \(G_i\) is a sequence with \(J(G_i)\to J_*\), and \(\varepsilon_i=J(G_i)-J_*\to0\).

**Hypothesis H0.** It makes "converges in \(C^2\) on compact regular regions with the CH exterior fixed" precise.
- There is a limit space with regular part \(\Omega_\infty^{\rm reg}\supset U_c\), and a finite set \(S\) away from \(\Sigma\).
- There are embeddings \(\varphi_i:K\to C\) for each compact \(K\subset\Omega_\infty^{\rm reg}\), with \(\varphi_i^*G_i\to G_\infty\) in \(C^2(K)\).
- \(\varphi_i=\mathrm{id}\) on \(U_c\).
- The convergence holds in a fixed neighbourhood of \(\Sigma\), in the background coordinates.

The last two items are genuine inputs. If the collar part of \(\varphi_i\) is allowed to drift, it can only drift by isometries of the CH annulus, and these can be absorbed. Drift of the free side near \(\Sigma\) relative to the collar cannot be absorbed: it is exactly what would destroy the interface information below.

## 1. Comparison minimality passes to the limit

**Proposition A (\(\Omega\)-minimality of the limit).** Let \(K\Subset\Omega_\infty^{\rm reg}\setminus\overline{U_c}\) be compact. Let \(G'\) be any \(C^2\) metric with \(G'=G_\infty\) off \(K\). Then
\[
J_K(G')\ge J_K(G_\infty).
\]

*Proof.*
1. Define the competitor
\[
G_i'=G_i+(\varphi_i^{-1})^*(G'-G_\infty)\quad\text{on }\varphi_i(K),\qquad G_i'=G_i\ \text{elsewhere}.
\]
   It is \(C^2\) on \(C\) and positive definite for large \(i\), because \(\varphi_i^*G_i\to G_\infty\) in \(C^0(K)\). It equals \(G_i\) on the collar, since \(K\cap U_c=\varnothing\). It is therefore admissible after a \(C^2\)-small smoothing, and \(J\) is continuous in \(C^2(K)\).
2. The integrand of \(J\) depends pointwise on \(g,\partial g,\partial^2g\). Hence
\[
J(G_i')-J(G_i)=J_K(\varphi_i^*G_i+G'-G_\infty)-J_K(\varphi_i^*G_i)\longrightarrow J_K(G')-J_K(G_\infty).
\]
3. The left side is at least \(J_*-J(G_i)=-\varepsilon_i\to0\). QED.

**Consequences.**
- For \(h\in C^2_c(K)\), \(\Phi(t)=J_K(G_\infty+th)-J_K(G_\infty)\ge0\) for every admissible \(t\). This gives the weak Euler–Lagrange equation \(\Phi'(0)=0\) and stability \(\Phi''(0)\ge0\).
- The transfer uses only two facts: the integrand involves at most two derivatives, and the sequence is minimizing. Palais–Smale sequences give \(\Phi'(0)=0\), via \(dJ(G_i)[h_i]\to dJ(G_\infty)[h]\), but not stability or minimality.
- Only variations supported in \(\Omega\setminus S\) are tested. No information is obtained on \(\Sigma\) or at \(S\).
- Interior smoothness of \(G_\infty\) then requires the usual gauge fixing, for example harmonic coordinates, where the Euler–Lagrange equation becomes a fourth-order elliptic system. With that, \(G_\infty\) is real-analytic in \(\Omega^{\rm reg}\).

## 2. The interface: what closes, what does not

### 2a. The scalar step closes using only \(C^0\) information on \(\Sigma\)

Conformal variations give
\[
\Delta_+s+s+4=0
\]
in distributions on \(\Omega\setminus S\). Write \(u=s+4\). Since \(g\in C^2\), we have \(u\in C^0\) and then \(u\in W^{2,p}_{\rm loc}\).

H0 (the \(C^2\) match across \(\Sigma\)) gives \(u|_\Sigma=0\).

*Maximum-principle argument.* Suppose \(\Omega_\epsilon=\{u>\epsilon\}\neq\varnothing\).
- \(\Omega_\epsilon\) stays a positive distance from \(\Sigma\).
- On \(\Omega_\epsilon\), \(\operatorname{div}\nabla u=u>\epsilon>0\), so \(u\) is subharmonic there.
- Then \(\sup_{\Omega_\epsilon}u\le\sup_{\partial\Omega_\epsilon}u=\epsilon\), a contradiction.

The same argument applied to \(-u\) gives \(u\equiv0\).

What this uses:
- \(u\) bounded near \(S\), so that isolated points are removable in dimension four. This is supplied by an orbifold removable-singularity theorem for \(J\)-critical metrics with finite \(L^2\) curvature. Such a theorem must be checked to include the lower-order terms \(2\int s+4\,\mathrm{Vol}\).
- Nothing about \(\partial_\nu s\).

Components of the regular base that do not touch \(\Sigma\) are closed orbifolds. On them \(\int(|\nabla u|^2+u^2)=0\). Hence \(s\equiv-4\) on the entire regular base. This replaces the "scalar unique continuation" of Section 7 of the note by a Dirichlet uniqueness argument, which is strictly stronger.

### 2b. The tensor step needs Cauchy data, and the missing datum is a 5-component tensor

With \(s\equiv-4\), \(E=\operatorname{Ric}+g\) satisfies (8.2) of I54:
\[
\operatorname{tr}\nabla^2E=-2\operatorname{Rm}(E)+\tfrac12|E|^2g,
\qquad \operatorname{tr}E=0,\qquad \operatorname{div}E=\tfrac12ds=0.
\]
The \(C^2\) match gives \(E|_\Sigma=0\). Assume \(G_\infty\in C^3\) up to \(\Sigma\) from the free side. Then:
- Tangential derivatives of \(E\) vanish on \(\Sigma\).
- Hence \(0=\operatorname{div}E=\nabla_\nu E(\nu,\cdot)\) on \(\Sigma\), and \(\operatorname{tr}\nabla_\nu E=0\).

So the only free Neumann datum is the **interface stress**
\[
\sigma=\nabla_\nu E\big|_\Sigma\in\Gamma\big(\mathrm{Sym}^2_0T^*\Sigma\big),
\]
a trace-free symmetric tangential tensor on \(S^3\): five functions.

*If \(\sigma=0\), then \(E\equiv0\).* The zero extension of \(E\) across \(\Sigma\) is \(C^1\) and piecewise \(W^{2,p}\) with no jump. It is therefore a weak solution of the same system across \(\Sigma\). The system has scalar principal symbol \(g^{ij}\partial_i\partial_j\), with \(C^2\) principal coefficients and bounded lower-order coefficients. Aronszajn unique continuation then gives \(E\equiv0\) on the connected regular set containing \(\Sigma\); a finite set \(S\) does not disconnect it in dimension 4. Einstein analyticity and \(\nabla\operatorname{Rm}=0\) on the collar then make that component locally CH.

### 2c. Minimality does not force \(\sigma=0\)

The obstruction is structural.

1. **The relaxed problem.** A \(C^2\)-across metric \(B\) is approximable by smooth fixed-collar metrics with \(J\) converging. Take \(B^\varepsilon=\mathrm{CH}+\chi(\mathrm{dist}_\Sigma/\varepsilon)(B-\mathrm{CH})\). Since \(B-\mathrm{CH}=O(\mathrm{dist}^2)\), the \(W^{2,2}\) error is \(O(\varepsilon^{1/2})\). So the fixed-collar problem is the Dirichlet problem with matched \(0,1\)-jets (\(2\)-jets under H0).
2. **Natural Neumann quantities are free.** For a fourth-order functional, the natural Neumann quantities, here \(E|_\Sigma\) and \(\sigma\), are Lagrange multipliers of the Dirichlet constraint. Nothing variational makes them vanish.
3. **Diffeomorphism invariance adds nothing new.** The Noether flux it supplies is \(\nabla_\nu E(\nu,\cdot)=0\), already used above.
4. **Proposition 2 forces \(\sigma\neq0\) when no topology is lost.** If the limit has no bubbling (\(S=\varnothing\), all topology retained), lower semicontinuity and step 1 give \(J(G_\infty)=J_*\). The limit is then a relaxed minimizer. Proposition 2 of I54 (smooth-across critical cells are CH, which contradicts \(q>0\)) then forces \(\sigma\not\equiv0\), or loss of the \(C^3\) match.

So **non-attainment in the smooth class can be carried entirely by interface stress, without any degeneration.** The Section 8 statement ("stationary noncollapsed orbifold branch obeys the threshold") is valid only on the sub-branch where \(\sigma=0\), or where the free-side jets match CH to all orders.

**Inputs that would supply the tensor step.**
- **(i) Interface jets.** \(C^3\) (or \(C^\infty\)) convergence across \(\Sigma\) with matching jets. This cannot be obtained from a general minimizing sequence: the \(G_i\) satisfy no equation, and any Dirichlet replacement on an annulus creates a new interface.
- **(ii) Dirichlet positivity.** \(E\) is TT, and its zero extension is TT in \(H^1\). Testing the equation with \(E\) gives
\[
\int_\Omega|\nabla E|^2=2\int_\Omega\langle\mathring R(E),E\rangle .
\]
  Hence \(E=0\) if the Einstein-type operator \(\nabla^*\nabla-2\mathring R_{G_\infty}\) is positive on Dirichlet TT tensors on \(\Omega^{\rm reg}\). This is the tensor analogue of 2a. It depends on the curvature of the unknown limit, so it is useful only with independent \(C^2\) closeness of \(G_\infty\) to CH plus strict TT-stability of the CH quotient. That stability property must itself be verified.
- **(iii) A Hadamard-type formula.** Relate \(\sigma\) to the derivative of \(J_*(R)\) with respect to the collar radius. This would test whether the radius-optimized problem must have \(\sigma=0\). This formula has not been computed.

### 2d. A threshold route that needs neither \(\sigma\) nor unique continuation

Suppose the base extends \(C^2\) across \(S\) as a metric \(B\) on the **manifold ball** \(D\), with all topology carried by the bubbles. The relative identity (1.2) of I54 holds for \(C^2\) metrics, by \(C^2\) approximation of Chern–Weil integrands. Applied to \(B\) with \(q_B=0\), it gives
\[
\int_DF(B)=4d+J(B).
\]
Fatou's lemma together with \(F\ge0\) then gives
\[
\liminf_i J_i\ \ge\ 8\pi^2q+J(B)\ \ge\ 8\pi^2q .
\]
No Euler–Lagrange equation is used beyond what removability needs.

The developing-map rigidity is needed only in two cases:
- **Orbifold base points.** Orbifold Euler and signature corrections make \(q_B^{\rm orb}\) positive and fractional, so \(\int F(B)<4d\) is possible.
- **Base retaining topology.** The bound reduces to the cell problem for \(B\).

Rigidity in turn needs §2b.

## 3. Recovered volume from \(F\ge0\), with a sharpening

The universal closed identity is
\[
\int|\operatorname{Ric}+g|^2=\int F-8\pi^2(2\chi+3\tau),\qquad F=4|W^+|^2+\frac{s^2}{12}+\frac{(s+4)^2}{4}=\frac{(s+3)^2}{3}+1+4|W^+|^2 .
\]
Subtracting the background gives
\[
J_i-8\pi^2q=\int_CF(g_i)-4d .
\]
Pointwise \(F\ge1\), with equality iff \(s=-3\) and \(W^+=0\).

**Proposition B (exact form).** Put \(\delta_i=8\pi^2q-J_i\). For any measurable \(K_i\subset C\),
\[
4d-\delta_i=\int_CF\ \ge\ \int_{K_i}F(g_i)+\mathrm{Vol}_{g_i}(C\setminus K_i).
\]

**Corollary B′ (limit form).** Suppose \(J_i\le8\pi^2q-\delta\) and \(G_\infty\) is locally CH on \(K\subset\Omega_\infty^{\rm reg}\), with H0 convergence there. Then \(F\to4\) uniformly on \(K\), and
\[
d-\mathrm{Vol}_{G_\infty}(K)\ \ge\ \frac{\delta}{4}+\frac14\limsup_i\mathrm{Vol}_{g_i}\big(C\setminus\varphi_i(K)\big).
\]

So at least \(\delta/4\) of background CH volume is unrecovered. The bound is improved by a quarter of the actual volume of the unrecovered replacement. The total cell volume obeys \(v\le4d-\delta\).

**Consequence for the threshold.** If the base is CH on \(D\setminus S\) with \(|S|=0\), then \(\sup_K\mathrm{Vol}=d\) and \(\delta\le0\). This is exactly the threshold of Section 8, now quantified.

**Points to keep in view.**
- **\(C^0\) recovery is insufficient.** The linearization
\[
\delta F=-\tfrac23\,\delta s+4\,\delta|W^+|^2
\]
  at CH has no sign, so near-CH regions in a weaker sense can have \(F<4\). "Recovered" must mean \(F\,dV\to4\,dV\) in \(L^1\), which \(C^2\) convergence supplies.
- **Bubble regions.** A rescaling \(g=\varepsilon^2\hat g\) gives \(F\,dV\to(\hat s^2/3+4|\hat W^+|^2)\,d\hat V\), which can vanish on anti-self-dual Ricci-flat ALE pieces. So bubbles add no lower bound here.
- **Supplier version.** With the Seiberg–Witten supplier of I54 §7, the same splitting gives \(J\ge8\pi^2q-\tfrac43d'-o(1)\) for the unrecovered background volume \(d'\). The argument runs as follows:
  - on recovered regions, \((-s+w)_+^2\to36\);
  - hence \(H_{C'}\ge36d'-o(1)\);
  - and \(\int_{C'}F=J-8\pi^2q+4d'+o(1)\).

  The conclusion is \(d'\ge3\delta/4\). This matches Proposition 6 of I55 (\(d_s\ge3\pi^2\epsilon/2\) with \(\delta=2\pi^2\epsilon\)), now for asymptotic rather than exact recovery. The \(\delta/4\) bound needs no supplier.

## 4. The developing-map argument for real-hyperbolic bases (O10)

**What transfers unchanged.** Let \(X=\mathbb H^4/\Gamma\) be closed, with \(\Gamma\) torsion-free. Take any constant sectional curvature, e.g. \(-1/3\) so that \(\operatorname{Ric}=-g\). Let \(U\) be the connected exterior of finitely many disjoint embedded closed 4-balls. Let \(\mathcal O\) be a connected, effective, **complete** locally \(\mathbb H^4\) orbifold with \(\partial\mathcal O=\varnothing\), and \(\iota:U\to\mathcal O\) a smooth injective local isometry. Then \(\mathcal O\cong X\), and \(\iota\) extends to the isometry.

*Proof.*
1. Completeness and local homogeneity make \(\mathcal O\) developable: \(\mathcal O=\mathbb H^4/\Gamma'\) with \(\Gamma'\) discrete in \(\mathrm{Isom}(\mathbb H^4)\). Orientation-reversing elements and reflections are allowed.
2. In dimension \(n\ge3\), \(\pi_1(U)=\Gamma\). The lifted exterior \(\widetilde U=\mathbb H^4\setminus\bigcup\gamma\widetilde D\) is connected and simply connected. The lifted balls are bounded, because a ball lifts homeomorphically.
3. The developing map of \(\iota\) is a local isometry of a connected open subset of \(\mathbb H^4\). By rigidity of constant curvature it is the restriction of some \(A\in\mathrm{Isom}(\mathbb H^4)\). Conjugating by \(A\) gives \(\Gamma\le\Gamma'\).
4. Suppose \(g\in\Gamma'\setminus\Gamma\) and \(g\widetilde U\cap\widetilde U\ni gx\). Injectivity gives \(gx=\gamma x\), so \(\gamma^{-1}g\) fixes \(x\). Effectiveness then makes \(\iota\) non-injective near \(x\) (also at mirror points). So \(g\widetilde U\cap\widetilde U=\varnothing\).
5. The connected unbounded set \(g\widetilde U\) would then lie in one bounded ball, which is impossible. Hence \(\Gamma'=\Gamma\).

Compactness of \(\mathcal O\) is not needed; completeness suffices. This also removes complete noncompact bases, for CH and for \(\mathbb H^4\). The index/volume variant also transfers.

**The local step.** The scalar and tensor Euler–Lagrange equations (8.1)–(8.2) are those of \(J=\int|\operatorname{Ric}+g|^2\) and do not depend on the model. With an \(\mathbb H^4\) collar normalized to \(\operatorname{Ric}=-g\) (so \(s=-4\)):
- §2a holds verbatim.
- §2b gives \(E=0\) under the same \(\sigma=0\) input.
- Einstein analyticity makes \(\operatorname{Rm}\) equal to the constant-curvature tensor on the connected regular set, hence \(W^\pm=0\) there.

**Where W⁺-flatness is not enough.**
- If an O10 base is known only to be Einstein with \(W^+=0\) (anti-self-dual Einstein, \(\operatorname{Ric}<0\)), the models include reversed-orientation CH quotients and non-homogeneous local ASD Einstein (quaternion-Kähler) metrics. There is no \(\mathbb H^4\) developing map.
- The needed hypothesis is \(W^+=W^-=0\) together with Einstein, i.e. constant curvature, or Einstein plus an open \(\mathbb H^4\) piece. In the latter case \(W^-=0\) follows by analytic continuation and W⁺-flatness is redundant.
- A general analytic Einstein exterior would require goodness of \(\mathcal O\) and the Kobayashi–Nomizu extension of analytic local isometries into complete targets in place of the \((G,X)\) structure.
- W⁺-flatness or Einstein alone gives at most local conformal flatness, whose compact developing maps need not be coverings.

**Recovered volume in the \(\mathbb H^4\) case.** The identity \(J-8\pi^2q=\int_CF-\int_DF\) is universal, with the same \(q=k+4\ell\). At \(\operatorname{Ric}=-g\), \(\mathbb H^4\) has \(F_{\rm bg}=s^2/12=4/3\). Proposition B then becomes
\[
d-\mathrm{Vol}(K)\ \ge\ \frac34\,\delta+\frac34\,\mathrm{Vol}_g(\text{unrecovered}),
\]
and the fixed-exterior threshold \(\liminf J\ge8\pi^2q\) follows as before. Whether \(8\pi^2q\) is the relevant O10 coefficient is a separate question. The background density \(4/3\) is close to the pointwise floor \(F\ge1\), which leaves much less algebraic room than in the CH case. The CH-specific constant \(\delta/4\) is replaced by \(\delta/F_{\rm bg}\) in general.

## Summary of the scientific state

**Proved here:**
- \(\Omega\)-minimality, stationarity and stability of the limit (Proposition A).
- \(s\equiv-4\) on the entire regular base, using only the \(C^2\) match at \(\Sigma\).
- The threshold for manifold-ball bases, from the base's own relative identity (§2d).
- The recovered-volume bounds, Proposition B and Corollary B′.
- Rigidity under completeness rather than compactness, for both CH and \(\mathbb H^4\).

**Missing:** the interface stress \(\sigma\in\mathrm{Sym}^2_0T^*\Sigma\). It is not forced to vanish by minimality, and Proposition 2 forces it to be nonzero for bubble-free limits. It is the single obstruction separating the Section 8 threshold from an unconditional noncollapsed statement. The candidate ways to control it are §2c (i)–(iii).