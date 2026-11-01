# TTCS Independent Branch Record

```json
{
  "step_id": 54,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md",
    "Sessions/S1003A02/workspace/data/step54_charge_and_entropy_checks.json",
    "Sessions/S1003A02/workspace/notes/step53_anderson_entrance_bubble_exclusion_attainment.md",
    "Sessions/S1003A02/trace/ttcs/results/step53_ttcs01_verifier1_integration.md",
    "Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/web_research_collected.tex"
  ]
}
```

## Task

Verify, adversarially and constructively, Theorem 54.A and Lemmas 54.1-54.3 in step54_k1_ball_quotient_attainment_theorem.md. The setting: X compact ball quotient other than a fake projective plane, M = X # CPbar^2, P = int |Ric°|^2; an Anderson case-(I) minimizing configuration with only trivial-group cone points. Check in particular: (1) Lemma 54.1 two-orientation cost formula c(N)=4(e-1)+4b1+b^- - 5b^+ for multi-ended AE bubbles with Gamma=1, including the boundary-term hypotheses; (2) Lemma 54.2: is each capped bubble really a connected summand of M, including multi-ended bubbles and graph loops; (3) Lemma 54.3: M=Z#R, b+(M)>=2, Z PSC with b+(Z)>=1 implies SW_M=0 even when b+(R)=0 -- is the neck-stretching argument correct (reducibles on Z side avoided by generic perturbation; irreducibles by PSC)? Is there a known counterexample or a cleaner citation? (4) the pi_1 argument: freely indecomposable PD4 lattice, Hopf surjection H2(Y)->H2(pi1 Y), conclusion that each bubble compactification is a homotopy sphere; (5) part (iii): SW_{V#Sigma}=SW_V for a PSC homotopy sphere; constant negative scalar curvature; Einstein-or-non-Bach-flat; the 'no bubbles if all hat N_k are standard S^4' step via Bishop-Gromov; (6) whether the upper bound (U) p_*(M)<8 pi^2 legitimately follows from the analytic CH-collar cell of web_research_collected.tex Ch.5 for EVERY non-fake-plane ball quotient (collar radius issue); (7) the general-k extension inequality sum[4(e-1)+4b1+beta] < k and its use of Lemma 54.3; (8) the collapse lemma (free circle action region is spin, so cannot carry E) and the orbifold parity remark (absorbing E needs a in H2(X) with a^2=-1 when m=1); (9) the BCG+Bishop computation in data JSON and Remark 4; (10) the answer to A01 on Koiso local rigidity near ball quotients (TT gap 2 from Rcirc eigenvalues -2,+4). Give corrected statements where something fails, and say precisely which hypotheses (H_sm, H_lsc, H_dec, H_eq, H_rem) each conclusion needs. Also assess whether the 'gate economy' paragraph's analysis of the rescaled perturbation coefficient eps*ell^{4-4p} is right and whether a better choice of p(eps) or a different argument gives bubble-scale P-criticality.

## Output

# Verification memo: Step 54 (Theorem 54.A, Lemmas 54.1–54.3 and the attached remarks)

## Summary

**The theorem survives, but two proof steps need repair.**

- The inference in (i) from \(c\le0,\ \bar c\le0\) to \(e=1,\ b_1=0\) is invalid as written. Reordered, the argument closes.
- A degree-one map to \(X\) removes the PSC input from most of the Seiberg–Witten step and forces the gluing graph to be a tree independently of energy.

**Quantitative corrections:**

- **Remark 4 has the Weyl inequality reversed.** An Einstein metric on \(M\) has \(\int|W^+|^2\) strictly *below* the Kähler-type value.
- **The orbifold parity remark is too strong.** The constraint \(a^2=m^2-2\) does not force \(m\) odd.
- **The rescaled-perturbation analysis in §3 (final paragraph) uses too weak an energy bound.** With the correct one, bubble-scale \(P\)-criticality (\(\kappa\to0\)) follows for fixed \(p\), with no choice \(p(\varepsilon)\).

Statements marked "first order" or "imported" below are computations or inputs not established in the supplied files.

---

## 1. Lemma 54.1: the formula is correct; the decay needed is weaker, and the stated consequence is wrong

**Derivation.** Write \(\chi(N^{\rm tr})=\chi(\widehat N)-e\). Each AE end with trivial group contributes the flat Euler flux \(1\), so
\[
e_{GB}(N)=\chi(\widehat N)-2e .
\]
Examples: \(\mathbb R^4\) gives \(0\); Schwarzschild \(S^3\times\mathbb R\) gives \(-2\).

The text's "\(e_{GB}=\chi(N)-e\)" is right only if \(\chi(N)\) means the Euler characteristic of the open manifold; say so explicitly. With \(\tau(N)=\tau(\widehat N)\), since \(\eta(S^3_{\rm round})=0\),
\[
2e_{GB}+3\tau=4-4e-4b_1+5b^+-b^-
\]
\[
\Rightarrow\quad c(N)=4(e-1)+4b_1+b^--5b^+.
\]
Reversing orientation gives \(c(\bar N)\). All entries in the JSON file agree with this.

**Hypothesis on the ends.** The Gauss–Bonnet and signature terms at infinity need only that the rescaled annuli \(\{r\sim R\}\) converge in \(C^{1,\alpha}\) to the flat annulus. Equivalently, the metric is derivative-controlled of order 0:
\[
g-\delta=o(1),\qquad r\,\partial g=o(1),\qquad r^2\partial^2 g=o(1).
\]
- The transgression at infinity is built from the second fundamental form and the curvature of the large spheres. After scaling, both tend to their flat values.
- The \(\eta\)-invariant of the rescaled spheres tends to \(\eta(S^3_{\rm round})=0\).

So Lemma 54.1 does not need \(\tau>0\). Order \(\tau>0\) is needed only for the PSC conclusion of 53.Y; see §3.

**Consequence sentence: false for multi-ended bubbles with indefinite \(b_2\).** The sentence "every bubble with \(e\ge2\) or \(b_1\ge1\) costs \(\ge8\pi^2\)" fails. Counterexample: \(e=2\), \(b^+=b^-=1\) (an \(S^2\times S^2\) cap with two ends) gives
\[
c=\bar c=4-4=0 .
\]
The correct description of topologically cheap bubbles is
\[
c\le0,\ \bar c\le0\iff 4(e-1)+4b_1\le\min\{5b^+-b^-,\;5b^--b^+\}.
\]
This forces either
- \(b_2=0\), \(e=1\), \(b_1=0\); or
- \(b^+\ge1\) and \(b^-\ge1\), with \(e\) and \(b_1\) allowed to be large when \(b_2\) is large.

The lower bound \(P\ge8\pi^2\max\{c,\bar c,0\}\) holds without scalar-flatness, since \(\int s^2\ge0\).

## 2. Lemma 54.2: correct, with the definition of \(V\) made explicit

Take the vertices to be:
- the normalized bulk components, with reducible points split into their branches; and
- the bubbles, with interior trivial-group punctures capped.

The edges are \(S^3\) gluings. By Cerf, every orientation-preserving diffeomorphism of \(S^3\) is isotopic to the identity, and oriented self-gluings produce \(S^1\times S^3\) summands. Hence
\[
M\cong\#_aV_a\;\#_k\;\widehat N_k\;\#\;b_1(\mathcal G)(S^1\times S^3).
\]
Each \(\widehat N_k\), multi-ended or not, is a summand: \(M\cong\widehat N_k\# R_k\).

Two points to record:

1. **The smooth manifold \(V\) needs no metric input.** It is defined by capping the \(S^3\) cross-sections with balls, using Anderson's diffeomorphism-level decomposition (4.65). No removability is needed for the topological parts (i)–(ii).
2. **"Bubble smooth" in \(\mathrm H_{\rm dec}\) covers two things.** It includes removability at a bubble's own interior trivial-group points, where deeper bubbles attach. It also includes the \(\tau>0\) decay that 53.Y uses for PSC.

**New, purely group-theoretic: the graph is a tree.** \(\Gamma\) is torsion-free, one-ended (a \(PD_4\) group) and not \(\mathbb Z\). By Stallings and Grushko, \(\Gamma\) is freely indecomposable. Since
\[
\pi_1(M)=\Gamma=\ast\,\pi_1(\text{summands})\ast F_{b_1(\mathcal G)},
\]
this forces \(b_1(\mathcal G)=0\), and exactly one summand has nontrivial \(\pi_1\), which is then \(\cong\Gamma\). This needs no energy bound.

## 3. Lemma 54.3: the statement is true; the proof can be shortened, and PSC is needed only in one sub-case

Split by \(b^+(R)\).

**Case \(b^+(R)\ge1\).** \(b^+(Z)\ge1\) and \(b^+(R)\ge1\) give vanishing by the standard connected-sum theorem. No PSC is used.

**Case \(b^+(R)=0\).** Then \(b^+(Z)=b^+(M)\ge2\), and PSC on \(Z\) gives \(SW_Z\equiv0\) (Witten). The neck-stretching argument in the note is the correct mechanism, and its two exclusions are right:

- *Irreducibles on the \(Z\) side.* The Weitzenböck formula gives \(|\Phi|^2\le\sup(-s+C|\eta|)_+=0\) for small \(\eta\).
- *Reducibles.* They need \(2\pi\,c_1(L)^+=[\eta]^+\) in \(L^2\)-harmonic \(\mathcal H^+\cong H^+(Z)\), which has codimension \(b^+(Z)\ge1\).
- *Compactness.* The round \(S^3\) has a single, nondegenerate critical point (the reducible). Its Dirac operator has no kernel and \(H^1(S^3)=0\), so monopoles on the neck decay exponentially to the reducible.

A cleaner citation, when \(b_1(R)=0\): the gluing formula for a summand with \(b^+=b_1=0\) gives \(SW_{Z\#R}(\mathfrak s\#\mathfrak t)=SW_Z(\mathfrak s)\) for \(c_1(\mathfrak t)^2=-b_2(R)\), and \(0\) otherwise. The precise reference (Kronheimer–Mrowka / Frøyshov form) should be fetched rather than paraphrased. No counterexample is known to me, and the argument contains none.

**Degree-one argument (new; removes the PSC branch in most cases).** \(M=X\#\overline{\mathbb{CP}}^2\to X\), the blow-down collapse, is the classifying map and has degree 1.

- *Bubble simply connected.* If \(\pi_1(\widehat N)=1\), the collapse \(q:M\to R\) is a \(\pi_1\)-isomorphism of degree 1. Hence \(c_R\circ q\simeq c_M\) and \(\deg c_R=1\). Then
\[
\langle c_R^*\alpha\cup c_R^*\beta,[R]\rangle=\langle\alpha\cup\beta,[X]\rangle,
\]
so \(Q_X\) embeds isometrically in \(H^2(R;\mathbb Q)\) and \(b^\pm(R)\ge b^\pm(X)\). In particular \(b^+(R)\ge3\), and the standard vanishing theorem applies.
- *Bubble carrying \(\pi_1\).* The branch \(b^+(R)=0\), and with it PSC, scalar-flatness and \(\tau>0\), can arise only when \(\pi_1(\widehat N)\cong\Gamma\). Then \(\deg c_{\widehat N}=1\), so \(b^\pm(\widehat N)\ge b^\pm(X)\).

## 4. The \(\pi_1\) step and the corrected proof of (i)

**Corrected order of argument for (i).**

1. (U) and \(\mathrm H_{\rm lsc}\) give \(\sum_kP(N_k)<8\pi^2\), hence \(c_k\le0\) and \(\bar c_k\le0\) for every \(k\).
2. If \(b^+(\widehat N_k)\ge1\), Lemma 54.3 and the nonvanishing of \(SW_M(K\pm E)\) give a contradiction. The latter holds because \(X\) is minimal of general type, so \(SW_X(K)=\pm1\), and the blow-up formula applies.
3. So \(b^+=0\). Then \(\bar c=4(e-1)+4b_1-5b^-\le0\) and \(c=4(e-1)+4b_1+b^-\le0\) force \(e=1\), \(b_1=0\), \(b_2=0\).
4. \(V\) is connected because all bubbles are leaves (and in any case \(b_1(\mathcal G)=0\) by §2).

**The \(\pi_1\) argument is correct.** Stallings and Grushko leave one factor equal to \(\Gamma\). If it were \(\pi_1(\widehat N_k)\), Hopf gives
\[
b_2(\widehat N_k)\ge b_2(X)=c_2-2+2b_1\ge1,
\]
a contradiction. The degree-one argument gives the stronger bound \(b^\pm(\widehat N_k)\ge b^\pm(X)\). Then:
- \(\widehat N_k\) is a simply connected \(\mathbb Q\)HS;
- \(H_2\) is torsion-free by the universal coefficient theorem;
- so \(\widehat N_k\) is a homotopy sphere, homeomorphic to \(S^4\) by Freedman.

**Geography input, checked.** \(\chi(\mathcal O)=c_2/3\) and \(p_g=c_2/3-1+q\). The Cartwright–Steger surface has \(c_2=3\), \(q=p_g=1\). Every non-fake ball quotient therefore has \(b^+=2p_g+1\ge3\).

## 5. Part (iii)

- **\(SW_{V\#\Sigma}=SW_V\).** True for any homotopy sphere \(\Sigma\) by the \(b^+=b_1=0\) gluing theorem; PSC is not needed. The note's PSC argument is also valid: the unique reducible on \(\Sigma\) is unobstructed, since \(\ker D=0\), \(H^1=0\) and \(H^+=0\).
- **\(s\) constant.** Global minimality \(P(g_0)=p_*(V)\) gives criticality. The trace equation \(\Delta s=0\) then makes \(s\) constant.
- **\(s>0\) and \(s\equiv0\) excluded.** \(s>0\) is excluded by \(SW_V\ne0\). \(s\equiv0\) is excluded by the averaged LeBrun bound
\[
\int s^2\ge32\pi^2\,\mathbb E_\pm\|(K\pm E)^+\|^2\ge32\pi^2A>0 .
\]
- **Dichotomy.** \(P=2\int|W|^2+\tfrac1{12}\int s^2-16\pi^2\chi\). If \(g_0\) is Bach-flat, criticality gives \(\nabla\!\int s^2=0\). At constant \(s\) this equals \(-2s\operatorname{Ric}^\circ\), and \(s\neq0\) forces Einstein. So: Einstein, or non-Bach-flat. Correct.
- **No bubbles when every \(\widehat N_k\cong S^4\).** Then \(V\cong M\), so \(\sum_kP(N_k)=0\). Each \(N_k\) is Ricci-flat AE with trivial group at infinity. Bishop–Gromov gives volume ratio \(\le1\), with equality, so \(N_k\) is flat. A flat limit is not a bubble. Correct.
- **Exotic \(\Sigma\).** An Einstein \(g_0\) would live on \(V\), homeomorphic to \(M\) but possibly not diffeomorphic. Remark 3 should say "on \(V\)".

## 6. The upper bound (U): valid for every compact ball quotient

The Ch. 5 proposition is stated for **every** \(R>0\), with \(\epsilon<\epsilon_R\).

- In the \(\operatorname{Ric}=-6g\) normalization, \(a^H=(\sinh t,\sinh t\cosh t,\sinh t)\) is \(\mathbb{CH}^2\) in geodesic polar coordinates, so \(t\le R\) is a geodesic ball.
- Take \(R<\operatorname{inj}(X)\); every compact \(X\) has positive injectivity radius.
- The glued metric equals \(g_X\) outside the ball, with \(P(g_X)=0\).
- The endpoint values \(u=(0,0,-1)\) and \(u=(0,3\sinh^2t,0)\) give the charge \(1\). The coefficient \(\int_{2\sqrt\epsilon}^{T}-18\epsilon^2\,dt/t=-9\epsilon^2\log(1/\epsilon)+O(\epsilon^2)\) checks.

**Orientation check.** Under \(dt\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3\), both the Burns core (fibre \(\sigma_3\)) and the outer CH Kähler form (\(dt\wedge\sigma_2+\cdots\)) have complex orientation, because \((3,1,2)\) and \((2,3,1)\) are cyclic. So the cell is an \(\overline{\mathbb{CP}}^2\) summand, consistent with the Ch. 5 statement.

Hence \(p_*(M)<8\pi^2\) for every compact ball quotient, fake planes included. The fake planes are left out only because the SW step needs \(b^+\ge2\) (with \(b^+=1\) the chamber structure has to be handled).

## 7. General \(k\)

**Inequality.** Disjoint cells in \(k\) small CH balls give \(p_*(M_k)<8\pi^2k\). Lemma 54.3 gives \(b^+(\widehat N_j)=0\) for every bubble, independently of cost. Then \(\max\{c,\bar c\}=c\), and
\[
\sum_j\big[4(e_j-1)+4b_1+b_2\big]<k .
\]
So \(\sum_j b_2<k\), and all \(e_j=1\) when \(p_*(M_k)<32\pi^2\). Correct. The definition of \(\beta\) in the note reduces to \(b_2\) here.

**Sharper structure from the degree-one argument (new).**
- If \(\pi_1(\widehat N_j)\cong\Gamma\), then \(b^+(\widehat N_j)\ge b^+(X)\ge3\), contradicting \(b^+=0\). Hence **every** bubble compactification is simply connected.
- Then \(\pi_1(V)=\Gamma\) and \(\deg c_V=1\), so \(Q_X\hookrightarrow H^2(V;\mathbb Q)\) isometrically. All of \(X\)'s homology stays in the bulk.
- Each escaped lattice is definite with \(b^+=0\). By Donaldson it is \(-I_{b_2}\), with total rank \(<k\).

## 8. Collapse lemma and orbifold parity

**Free circle action: correct.** \(C\to B\) is a principal bundle over an orientable 3-manifold. Orientable 3-manifolds are parallelizable, so \(TC=\pi^*TB\oplus\underline{\mathbb R}\) is trivial. For \(x=i_*y\), Wu gives \(x^2\equiv\langle w_2(C),y\rangle=0\). So \(E\) is not in the image.

The proof uses freeness essentially. Once isotropy appears (for example in Seifert pieces), \(C/S^1\) is an orbifold and the splitting of \(TC\) fails. Item (a) is therefore genuinely open. A possible tool is the vanishing \(\chi=0\) of regions with positive-rank \(F\)-structure; that is suggested, not proved.

**Orbifold parity: corrected.** Every root class is \(r=a+mE\in H_2(M)\) with \(a^2=m^2-2\). That part is right.

"Absorption needs \(m\) odd" is not justified, for two reasons:
- \(H_2(M)\) contains \(H_2(V^{\rm tr})\oplus\Lambda_\Gamma\) only up to index controlled by \(H_1(S^3/\Gamma)\);
- bulk classes may themselves have \(E\)-components.

Example: a root \(a+2E\) with \(a^2=2\) has \(E\cdot r=-2\neq0\), so \(E\) is not in the rational span of the bulk classes. Corrected statement:
- absorption requires some root with \(m\ne0\);
- if \(m\) is odd, \(Q_X\) is odd;
- \(a^2=-1\) only when \(m=1\).

\(Q_X\) is indefinite: \(b^-=c_2/3-1+b_1\ge1\) for non-fake ball quotients. So if \(Q_X\) is odd, classes of square \(-1\) exist. Lemma 52.9(v) is not supplied, so its non-Kähler conclusion cannot be checked here.

## 9. BCG, Bishop and Remark 4

**Numbers verified.**
- \(h(\mathbb{CH}^2)=4\) for \(\sec\in[-4,-1]\), where \(\operatorname{Ric}=-6\). Bishop gives \(h\le3\sqrt2\). With the degree-one map, \(\mathrm{Vol}\ge(64/81)\mathrm{Vol}(X)\).
- LeBrun's averaged bound gives \(\mathrm{Vol}\ge\mathrm{Vol}(X)=\pi^2A/18\).
- Upper bounds: \(T_+(M)=A-1\) gives ratio \(\le3-1/c_2\); \(\chi(M)=c_2+1\) gives ratio \(\le2+2/c_2\).
- The Kähler-type value gives \(\mathrm{Vol}=(1-\tfrac1{3c_2})\mathrm{Vol}(X)\).

**The concluding sentence has the inequality reversed.** For an Einstein metric,
\[
2\!\int|W^+|^2=4\pi^2(A-1)-24\,\mathrm{Vol}\le\tfrac{8\pi^2A}3-4\pi^2<48\,\mathrm{Vol}=2\!\int\tfrac{s^2}{24}.
\]
So \(\int|W^+|^2\) lies strictly **below** the Kähler-type value: the lost charge must come out of \(W^+\).

**Sharper volume bound from LeBrun's Weyl–scalar estimate (first-order computation, not in the notes).** Apply
\[
\int(|s|+\sqrt6|W^+|)^2\ge72\pi^2A
\]
with Cauchy–Schwarz and the \(T_+\) constraint. Expanding around \(\mathrm{Vol}(X)\) gives
\[
\mathrm{Vol}(g)\ge\big(1+\tfrac1{3c_2}+O(c_2^{-2})\big)\mathrm{Vol}(X).
\]
This is consistent with the nonempty window and gives no obstruction. The window is not closed by entropy, confirming the note's conclusion.

## 10. Koiso rigidity near \(g_\Gamma\)

**Curvature action, recomputed.** With \(R(X,Y)Z=-[\cdots]\) (holomorphic curvature \(-4\)),
\[
\mathring Rh=-\big(\operatorname{tr}h\,g-h+3h(J\cdot,J\cdot)\big).
\]
This gives:
- \(-2\) on Hermitian trace-free tensors (dim 3);
- \(+4\) on \(J\)-anti tensors (dim 6);
- \(\mathring Rg=-6g\), which matches \(\operatorname{Ric}\).

**Gap on TT tensors.** The Bochner identity for TT tensors (Besse 12.69 form) gives
\[
\|\nabla h\|^2\ge\langle\mathring Rh,h\rangle-\lambda\|h\|^2,
\]
hence
\[
\langle(\nabla^*\nabla-2\mathring R)h,h\rangle\ge(-a-\lambda)\|h\|^2=(-4+6)\|h\|^2=2\|h\|^2 .
\]
The same formula gives \(2\) for real-hyperbolic 4-manifolds, consistent with known rigidity.

So the gap 2 is correct, there are no infinitesimal Einstein deformations, and Koiso's isolation theorem applies. Uniformity over covers also needs:
- the Bianchi-gauge vector operator \(\nabla^*\nabla+6\ge6\);
- the \(L^\infty\)/Hölder inverses of Lemma M.

Both are available. The KE statement for general \(X\) (deformations correspond to \(H^1(\Theta)\), and are KE if the Kuranishi space is smooth) is correct.

## 11. Rescaled perturbation and bubble-scale criticality (§3, final paragraph)

**The scaling identity is right:**
\[
\varepsilon\!\int(1+|\operatorname{Ric}_g|^2)^p\,dV_g=\varepsilon\ell^{4-4p}\!\int(\ell^4+|\operatorname{Ric}_{\hat g}|^2)^p\,dV_{\hat g}.
\]

**The energy input is too weak.** The note uses \(\varepsilon\int|\operatorname{Ric}|^{2p}\le C\). The correct bound is \(o(1)\). Let \(g\) be any metric on \(M\) with \(Z_\varepsilon(g)\le\inf Z_\varepsilon+o(1)\). Since \(P(g)\ge p_*(M)\),
\[
\varepsilon\!\int(1+|\operatorname{Ric}_g|^2)^p=Z_\varepsilon(g)-P(g)\le\delta(\varepsilon)+o(1),\qquad
\delta(\varepsilon):=\inf Z_\varepsilon-p_*\to0,
\]
because \(\inf Z_\varepsilon\le P(h)+\varepsilon\int(1+|\operatorname{Ric}_h|^2)^p\) for every fixed \(h\).

Weak lower semicontinuity of this convex term passes the bound to Anderson's fixed-\(\varepsilon\) limit pairs. At a bubble scale \(\ell\) defined by \(\ell^{4p-4}\int_{B_\ell}|\operatorname{Ric}|^{2p}\ge c_0\),
\[
\kappa=\varepsilon\ell^{4-4p}\le\delta(\varepsilon)/c_0\to0
\]
**for fixed \(p>1\)**. No choice \(p(\varepsilon)\) and no lower bound on \(\ell_{\min}\) is needed.

In the distributional Euler–Lagrange equation, Hölder gives
\[
\kappa\int|\operatorname{Ric}|^{2p-1}|\varphi|\le(\kappa\textstyle\int|\operatorname{Ric}|^{2p})^{\frac{2p-1}{2p}}\kappa^{\frac1{2p}}\|\varphi\|_{2p}\to0 .
\]

**What remains open.** The perturbation \(\kappa\nabla\!\int|\operatorname{Ric}|^{2p}\) is fourth order, not zeroth order. Passing the quadratic terms of \(\nabla P\) to the limit requires strong local \(W^{2,2}\) convergence on bubble scales, i.e. Anderson's Prop. 4.6 regularity uniformly in \(\kappa\to0\) (Step-53 point 9). That uniform estimate is the actual remaining analytic input.

**Consequences once bubbles are \(P\)-critical.**
- The trace equation gives \(\Delta s=0\), with \(s\in L^2\) on a manifold of Euclidean volume growth. Yau's \(L^p\) Liouville theorem gives \(s\equiv0\), so scalar-flatness is not a separate hypothesis.
- Then \(\nabla\!\int s^2=0\), so bubbles are Bach-flat.
- \(\mathrm H_{\rm dec}\)(b) then needs order-0 derivative-controlled asymptotics for Lemma 54.1, which \(\varepsilon\)-regularity supplies. It needs order \(\tau>0\) only for the PSC branch.

Improved-decay literature for Bach-flat ALE ends beyond Tian–Viaclovsky Thm 1.1 is a knowledge request; it is not supplied here.

## 12. Which hypotheses each conclusion uses (after the corrections)

All items are conditional on Anderson Thm 4.10, case (I), and \(\mathrm H_{\rm sm}\).

| Conclusion | Uses |
|---|---|
| Lemma 54.1 | Smooth bubble; order-0 derivative-controlled ends |
| Lemma 54.2 (topology) | (4.65) only |
| Lemma 54.2 (PSC) | \(s=0\) and \(\tau>0\) |
| Lemma 54.3 | SW theory only |
| (i) when \(\pi_1(\widehat N)=1\) | \(\mathrm H_{\rm lsc}\), (U), order-0 ends, bubble interior removability |
| (i) when \(\pi_1(\widehat N)=\Gamma\) | Also \(s=0\) and \(\tau>0\) (PSC branch), unless that case is excluded otherwise |
| (ii) | (i) plus \(s=0\) for \(P(N_k)=4\int|W^\pm|^2\); \(s=0\) follows from bubble \(P\)-criticality |
| (iii) | Also \(\mathrm H_{\rm eq}\), \(\mathrm H_{\rm rem}\) and reassembly decay; the \(\Sigma\)-gluing needs no PSC; "no bubbles" also needs smooth Poincaré or \(\widehat N_k\cong S^4\) |
| General \(k\) | Same as (i) |