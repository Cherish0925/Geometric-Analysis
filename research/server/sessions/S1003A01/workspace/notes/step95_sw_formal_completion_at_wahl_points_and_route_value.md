# Step 95 — Formal completion of Seiberg–Witten fields at a Wahl point, and what remains of the marked-germ route

Session S1003A01, Agent2, Execute. Inputs: Step 93 §8 (Theorem 93.A, Prop. 93.C, Lemma 93.W); Step 94 (`step94_same_field_budget_and_marked_wahl_route_decision.md`, §5 now repaired); the corrected equivariant operator and first-degree formula in `trace/ttcs/results/step94_ttcs02_verifier1_integration.md`; Spirit #126. New computation: `workspace/scripts/step95_sw_formal_completion.py` → `workspace/data/step95/sw_formal_completion.json`.

## 0. Question

Step 94 found that the marked forced classes of Proposition 93.C have vanishing order at least \(n-3\) at the Wahl point (odd \(n\ge5\)). The question was whether the coupled Einstein–Seiberg–Witten Taylor recursion turns this high-order marked mode into an obstruction — a signed term in \(D_2\), or any finite-order incompatibility with an Einstein metric. Spirit #126 pointed out that Seiberg–Witten is an auxiliary system on a fixed metric: the spinor does not source the Einstein equation. The principal operator is block diagonal and has homogeneous polynomial right inverses. This should give the answer at every order at once. The answer below proves that formal-completion statement, with an exact finite-order check on one non-flat conformal metric with reduced symmetry.

## 1. Setting and the triangular structure

Let \(\Gamma=\tfrac1{n^2}(1,n-1)\subset U(2)\) act on \(B\subset\mathbb C^2\) (the uniformizer of a Wahl point), and let \(g\) be any smooth \(\Gamma\)-invariant metric on \(B\). Einstein is not assumed. Fix the Spin\(^c\) lift of Step 93 with extendible twist \(m=nj\). The positive-spinor fibre weights are \((m,m-n)\) (§8.8 of the Step-93 note; the coefficient-weight convention is as in Step 94). Use \(g\)-normal coordinates centred at \(p_0=0\); they are \(\Gamma\)-equivariant because \(\Gamma\) acts by \(g\)-isometries fixing \(0\) and linearly in these coordinates. Use a synchronous (radially parallel) frame. Use a flat equivariant reference connection \(A_0\) on the trivialized determinant line, with \(\Gamma\) acting by the character. Write \(A=A_0+a\), where \(a\in i\Omega^1\). The unperturbed equations in Coulomb gauge are
\[
D_{g,A}\Phi=0,\qquad d^+_g a=q_g(\Phi),\qquad d^{*}_g a=0. \tag{95.1}
\]
Equations (95.1) contain no Bianchi-type compatibility: \(F_A=da\) is automatically closed. Every smooth solution can be put in equivariant Coulomb gauge on \(B\). To see this, solve \(\Delta_g f=-i\,d^*_ga\) with Dirichlet data and average \(f\) over \(\Gamma\). The constant term of \(a\) then vanishes, because \(T^*_0\) has \(\Gamma\)-weights \(\pm1,\pm(n-1)\not\equiv0\pmod{n^2}\). So no invariant constant one-form exists.

Expand in homogeneous polynomials, \(\Phi=\sum_{k\ge\ell}\Phi_k\) and \(a=\sum_{k\ge1}a_k\). In normal coordinates and a synchronous frame,
\[
g_{ij}=\delta_{ij}+O(r^2),\qquad D_{g}=D_0+\sum_{s\ge2}c_s\,\partial+\sum_{s\ge1}e_s,
\]
where \(c_s\) and \(e_s\) are homogeneous matrix coefficients of degree \(s\). The same holds for \(d^+_g\), \(d^*_g\) and the Clifford isomorphism \(q_g\). Collect (95.1) in degree \(k-1\). The only terms involving the degree-\(k\) unknowns \((\Phi_k,a_k)\) are the flat principal ones:
\[
\mathcal L_0(\Phi_k,a_k)
=\bigl(D_0\Phi_k,\;d_0^*a_k\oplus\sqrt2\,d_0^+a_k\bigr)
=\mathcal S_{k-1}(\Phi_{<k},a_{<k},g). \tag{95.2}
\]
The source \(\mathcal S_{k-1}\) is a polynomial in already-determined coefficients. The checks are as follows.
- The metric terms \(c_s\partial\Phi_i\) have degree \(s+i-1\ge i+1\), so they enter with \(i\le k-2\).
- The terms \(e_s\Phi_i\) enter with \(i\le k-2\).
- The Clifford term \(a_i\cdot\Phi_{i'}\) has degree \(i+i'=k-1\) with \(i\ge1\), so \(i'\le k-2\). Also \(i'\ge\ell\), so \(i\le k-1-\ell<k\).
- The quadratic term \(q(\Phi)_{k-1}=\sum_{i+i'=k-1}\Phi_i\otimes\bar\Phi_{i'}\) uses \(i,i'\le k-1-\ell<k\).
- The metric corrections to \(d^\pm_g,d^*_g\) act on \(a_i\) with \(i\le k-2\).

**Lemma 95.0 (equivariant polynomial right inverse).** On homogeneous polynomial spaces, \(\mathcal L_0:\mathcal P_k\to\mathcal P_{k-1}\) is surjective onto every \(\Gamma\)-isotypic target sector, and it has a \(\Gamma\)-equivariant, real-structure-preserving right inverse \(R_0\).

*Proof.* With the compatible operator \(D_0=\begin{pmatrix}\partial_{z_1}&\partial_{\bar z_2}\\-\partial_{z_2}&\partial_{\bar z_1}\end{pmatrix}\) (Step 94),
\[
D_0D_0^*=-\tfrac14\Delta I,\qquad(d^*\oplus\sqrt2 d^+)(d^*\oplus\sqrt2d^+)^*=\Delta\oplus\Delta .
\]
The second identity uses \(d^*d^*=0\), \(d^+d=0\) and \(2d^+d^*=\Delta\) on flat self-dual forms. The Euclidean Laplacian \(\Delta:\mathcal P_{k+1}\to\mathcal P_{k-1}\) is surjective (Fischer decomposition). Its Fischer right inverse \(\Delta^{-1}_F\), which lands in the orthogonal complement of the harmonics, is \(O(4)\)-equivariant. Hence
\[
R_0=\mathcal L_0^*\,\bigl(-4\Delta_F^{-1}\oplus\Delta_F^{-1}\oplus\Delta_F^{-1}\bigr)
\]
is a right inverse. It commutes with every element of \(U(2)\) that commutes with \(\mathcal L_0\), and in particular with \(\Gamma\) acting through the twisted spinor representation. Because \(\mathcal L_0\) commutes with the antiunitary real structure \(a\mapsto-\bar a\) on \(i\Omega^1\), the Fischer/least-norm choice does too, so \(R_0\) preserves reality. Averaging over \(\Gamma\) is unnecessary but harmless. \(\square\)

## 2. Theorem

**Theorem 95.1 (formal completion; no finite-jet obstruction).** Let \(g\) be any smooth \(\Gamma\)-invariant metric jet at a Wahl point (Einstein or not; the chosen metric jet must itself satisfy the metric and isotropy identities and, when imposed, the Einstein equations). Fix a twist \(m=nj\). Fix also

(i) a leading term \(0\ne P_\ell\in\ker D_0\cap\mathcal P_\ell^{\Gamma}\) at any permitted degree \(\ell\ge\ell_{\min}(n,j)=2\min\{j-1,n-j\}\);

(ii) for every \(k>\ell\), a free kernel element \(\kappa_k\in\ker D_0\cap\mathcal P_k^\Gamma\);

(iii) for every \(k\ge1\), a free invariant element \(\beta_k\in\ker(d_0^*\oplus d_0^+)\cap i\mathcal P^\Gamma_k\Omega^1\). Its curvature \(d\beta_k\) is a homogeneous closed anti-self-dual form; modulo exact gauge \(df\) with \(f\) harmonic, this datum is the free ASD determinant curvature, including the invariant constant \(F^-(0)\).

Then there is a unique formal solution \((\Phi,a)\) of (95.1) with \(\Phi_\ell=P_\ell\), with \(\Phi_k-\kappa_k\) and \(a_k-\beta_k\) in the image of \(R_0\), and with \(\Phi_k=0\) for \(k<\ell\). It is \(\Gamma\)-equivariant and real (\(a\in i\Omega^1\)). By Borel's lemma there is a smooth equivariant \((\Phi,a)\) solving (95.1) to infinite order at \(p_0\).

*Proof.* Induction on \(k\) using (95.2): set \((\Phi_k,a_k)=R_0\mathcal S_{k-1}+(\kappa_k,\beta_k)\). The source is equivariant and real because every ingredient is. Lemma 95.0 gives solvability at every degree. \(\square\)

**Consequences.**

1. **No finite-order solvability obstruction.** For an already admissible invariant metric jet, the permitted leading spinor and invariant ASD connection data introduce no further finite-order compatibility condition: every source in (95.2) can be absorbed by higher field coefficients. When the fixed metric is Einstein, its own jets must of course satisfy the Einstein equations. This does not show that all local signed terms vanish or that no local identity can contribute to a global \(D_2\) estimate. Formal solvability is different from coercivity for actual, globally normalized solutions.

2. **Amplitude and order are free.** The amplitude of \(P_\ell\) is a free parameter, and its degree can be any permitted \(\ell\). The character alone therefore fixes neither a normalized amplitude nor a positive scale-independent curvature cost. This does not classify all invariants of the permitted leading jets.

3. **What the theorem does not say.** It is a formal (and Borel-smooth infinite-order) statement. It does not construct an analytic germ, a solution on a ball with estimates, an extension in the supplied global Spin\(^c\) class, or any relation between the germ and the global monopole mass. It does not exclude global information carried by the marked field. It excludes finite-jet solvability obstructions of the stated auxiliary system, not all local information or estimates.

## 3. Exact check on a non-flat conformal metric with reduced symmetry

To test (95.2) and Lemma 95.0 independently of the abstract argument, the script uses a conformally flat but non-flat \(\Gamma\)-invariant metric \(g=e^{2u}g_0\),
\[
u=|z_1|^2+2|z_2|^2+|z_1|^2|z_2|^2+2\operatorname{Re}(z_1^{n-1}\bar z_2).
\]
The last term is \(\Gamma\)-invariant and reduces the two-dimensional torus symmetry, but the circle \((z_1,z_2)\mapsto(e^{it}z_1,e^{i(n-1)t}z_2)\) survives. This is not a symmetry-free metric. Conformal covariance in dimension four reduces (95.1) with \(\Psi=e^{3u/2}\Phi\) to
\[
D_{0,A}\Psi=0,\quad d^+a=e^{-u}q_0(\Psi),\quad d_0^*(e^{2u}a)=0,
\]
which includes genuinely nonconstant coefficients. A free ASD datum \(a^{(1)}=t(\bar z_1dz_1-z_1d\bar z_1-\bar z_2dz_2+z_2d\bar z_2)\) is included. The recursion uses equivariant sectors only and the exact least-norm right inverse over \(\mathbb Q(i)\).

| \((n,j)\) | \(\ell\) | degrees solved | flat principal map surjective at every degree | all residuals vanish below degree \(K\) | reality \(a_{\bar i}=-\overline{a_i}\) |
|---|---|---|---|---|---|
| (5,2) | 2 | \(k\le7\) | yes | yes | yes |
| (5,3) | 4 | \(k\le9\) | yes | yes | yes |
| (3,2) | 2 | \(k\le7\) | yes | yes | yes |
| (7,3) | 4 | \(k\le9\) | yes | yes | yes |

Per-degree domain dimension, target dimension, rank and kernel dimension are in `data/step95/sw_formal_completion.json`. Nonzero sources from \(u\), from \(a^{(1)}\cdot P\) and from \(q(\Psi)\) appear at the expected degrees, and each is absorbed. The reality of \(a\) emerges from the least-norm choice and is not imposed, which confirms that the right inverse preserves the real structure. This is an exact check of a finite truncation for one metric. The theorem itself is the induction of §2.

## 4. What remains of the marked-germ route: the global continuation and its scale

Theorem 95.1 settles finite-order compatibility, and further jet-order calculations are pointless. The remaining question (Spirit #126) is whether some concrete mechanism connects the marked germ to the globally normalized field data and the Einstein budget. The natural candidate is the vanishing order acting through unique-continuation (frequency) estimates. Its strength can be stated precisely.

**Proposition 95.2 (frequency transport of the marked order; conditional constants).** Let \(B_R\subset\) uniformizer be a ball on which \(g\) is \(C^{1,\alpha}\)-close to Euclidean (harmonic radius \(R\)), and let \((A,\Phi)\) solve (95.1) with \(|\Phi|^2\le\lambda\) and vanishing order \(\ell\) at \(0\). Assume a Garofalo–Lin-type almost-monotone frequency for the coupled Dirac system on \(B_R\), with error \(C(\lambda R^2+\epsilon_g)\). Then
\[
\int_{B_{R/2}}|\Phi|^2\le C\,2^{-2\ell}\lambda|B_{R/2}|,
\qquad
\int_{B_{R/2}/\Gamma}(\lambda-|\Phi|^2)^2\ge(1-C2^{-2\ell})_+^2\,\frac{\lambda^2|B_{R/2}|}{n^2}.
\]
*Proof sketch.* Doubling from frequency \(\ge\ell-C(\lambda R^2+\epsilon_g)\), then Cauchy–Schwarz on \(\lambda-U\ge0\). The constants are not computed here.

The high marked order \(\ell\ge n-3\) improves the depleted fraction of the harmonic ball to essentially all of it. The payment is nonetheless of the form \(c\,(\lambda R^2)^2/n^2\). It is scalar slack in (94.1), suppressed by the orbifold volume factor \(n^{-2}\), and it sits exactly at the unresolved dimensionless scale \(\lambda R^2\) of Step 93. Spirit #125 showed that positive scalar slack alone does not contradict the Einstein mixed budget: its amount must be compared with the remaining feasible region. The permitted vanishing order is formally free, and this conditional frequency mechanism gives a scalar, volume-suppressed payment without a controlled geometric scale. These observations explain why the present argument yields no Einstein obstruction; they do not prove that every quantitative unique-continuation argument must fail. A useful global estimate would have to show that the payment exceeds the remaining budget, or couple it to \(W^+\), harmonic projection, or another independent alignment quantity. No such mechanism is presently established.

**Research-value decision (not a theorem).** The Wahl line has delivered genuine capability: lossless actual-field transfer (Theorem 93.A), exact index transfer (93.I), marked realization (93.Y), forced characters (93.C), the equivariant monogenic order formula (Step 94), and now formal freedom (Theorem 95.1). Its remaining potential for Q1 depends on a global mechanism that is not in hand. New investment is therefore reallocated to the other original problems. The Wahl results remain valid tools, and the global-compatibility question is not declared exhausted.

## 5. Status of statements

- Theorem 95.1: complete proof (formal and infinite-order smooth). Lemma 95.0 is elementary. The exact check in §3 is independent confirmation.
- Proposition 95.2: conditional on the frequency monotonicity input; constants not computed. It is used only to measure the scale of the best available continuation.
- Step 94 §5 has been repaired (corrected operator, \(\ell_{\min}=2\min\{j-1,n-j\}\), supplied-class order \(\ge n-3\)).

## 6. A restricted topological observation for the reallocated Q4 work

The complete strict AKE model (Steps 57–60) has compact Bianchi-VIII principal leaves and a smooth bolt over a compact hyperbolic surface. Its natural double is already excluded by topology. More generally, suppose a smooth closed four-manifold is decomposed into disk bundles over smooth bolts \(\Sigma_i\), joined by product collars with closed three-dimensional cross-sections. Excision gives \(\chi(M)=\sum_i\chi(\Sigma_i)\). If all bolts have genus greater than one, this is negative, excluding every Einstein metric by Hitchin–Thorpe. With no bolts and a circle leaf space, \(\chi(M)=0\); the Einstein Gauss–Bonnet formula then forces flatness.

**Remark 95.3, narrowed scope.** This rules out the corresponding two-hyperbolic-bolt compactifications of the retained model. It is not a classification of all compact locally homogeneous foliations or all Bianchi quotient completions. Orbifold bolts require distinguishing ordinary from orbifold Euler characteristic and proving that the proposed total space is smooth. Bochner rules out a nontrivial continuous global isometry group on a closed negative Einstein manifold; local Killing fields on a quotient need not descend. The broader Bianchi-class exclusion in the initial version was not established by the given argument and is not used.

Gluing the model to a different compact exterior remains a proposed route, not a supplied construction. Its infinite-volume ACH end, fixed negative Einstein scale, boundary topology, metric and form traces, and normal data must be matched before a deformation theory has an actual compact gluing problem to solve. The auxiliary-field formal-completion theorem does not apply to the overdetermined Einstein–almost-Kähler pair equations.

*Post-Step-95 Spirit clarification:* the formal solvability theorem is retained. Its consequences, the symmetry description of the conformal check, the conditional scalar-cost interpretation, and the compactification claim above have been narrowed to their supported scope.
