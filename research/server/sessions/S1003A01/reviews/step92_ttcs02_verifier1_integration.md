# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 92,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step92_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step92_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the proposed fixed supplied Seiberg–Witten field limit blueprint line by line. Focus on the normalization and validity of equations (2.1)–(2.5), the localized cutoff inequality (3.1)–(3.2), the logarithmic W^{1,4} capacity calculation, and whether these facts really imply the full tightness statement (3.7) rather than only no mass in the innermost core. Inspect the actual Lemma 86.S scale and gluing control quoted in the blueprint. Also check the claimed lower bound ∫|Phi|^4 >=32π²A, the use of one fixed class selected from a finite sign family, and the Einstein Hodge identities (5.1)–(5.3). Identify any hidden sign, factor, regularity, chamber, perturbation, or annular-tail issue. Give exact repairs and a rigorous proof skeleton that the next Execute step can follow. Do not assume the orbifold removability or marked character result; state precisely what remains there.

## Integrated Scientific Memo

# Verification memo: fixed supplied Seiberg–Witten fields across a shrinking Wahl filler

## Conclusion

The normalization and coefficients in **(2.1)–(2.5), (3.1)–(3.2), and (5.1)–(5.3) are correct**, provided the equations are genuinely unperturbed and the Clifford convention is fixed as below.

The logarithmic capacity calculation is correct. However, the stated “complementary cutoff” does **not** establish full tightness (3.7). This gap is repairable in two rigorous ways:

1. **For the actual Lemma 86.S family:** uniform boundedness of \(s_\varepsilon^-\), the spinor maximum principle, and shrinking volume give the stronger bound
   \[
   \limsup_{\varepsilon\downarrow0}\int_{\{r<R\}}|\Phi_\varepsilon|^4\le CR^4.
   \]
2. **Using only the recorded local scalar \(L^2\) control:** a different, outward logarithmic cutoff proves (3.7) directly.

Thus the supplied material supports a **nonzero finite-energy monopole limit on \(V^{\rm reg}\)**, conditional on actual metric-wise supply from the finite family. It does not yet establish equivariant removability or the marked orbifold spin\(^c\) lift. Several claims about chambers, gauge sectors, and annular convergence require correction.

---

## 1. Actual geometric control from Lemma 86.S

The relevant statement is in `theorem_package_v1.md`, §13, Lemma 86.S. It assumes an orientation-matched equivariant ALE chart with two-derivative decay and uses
\[
\rho=\varepsilon^{\tau/(\tau+2)}.
\]
For the Wahl filler, \(\tau=4\), so
\[
\rho=\varepsilon^{2/3},\qquad
(\varepsilon/\rho)^4=\rho^2,\qquad
\delta_\varepsilon=O(\rho^2).
\]
On the transition annulus, after dilation by \(\rho^{-1}\), the metric is \(C^2\)-close to the Euclidean quotient metric. Scaling curvature back gives
\[
|\operatorname{Ric}(g_\varepsilon)|
\le C\rho^{-2}\delta_\varepsilon\le C.
\]
Inside the transition, the metric is the scaled Ricci-flat ALE metric; outside it equals the fixed orbifold metric. Consequently,
\[
\sup_\varepsilon\|s_\varepsilon^-\|_\infty<\infty. \tag{G1}
\]
This stronger conclusion is available from the **explicit cutoff family**, not merely from convergence of scalar energies.

The truncated scaled filler has volume
\[
\varepsilon^4\,O((\rho/\varepsilon)^4)=O(\rho^4),
\]
and the transition has the same volume order. For fixed sufficiently small \(R\) and \(2\rho<R\),
\[
\operatorname{Vol}_{g_\varepsilon}\{r<R\}
\le C(\rho^4+R^4)\le CR^4. \tag{G2}
\]
Here \(\{r<R\}\) includes the entire filler, with \(r\) continued as a region label rather than a radial coordinate through its compact core.

Similarly,
\[
\int_{\{r<R\}}(s_\varepsilon^-)^2
\le C\rho^4+\int_{\{2\rho<r<R\}}(s_g^-)^2
\le C(\rho^4+R^4). \tag{G3}
\]
This proves both (1.1) and (1.2).

**Scope of the quoted lemma.** It supplies scaled \(C^2\) annular control and shrinking volume. It does not make the compact filler core quasi-conical, nor is such a claim needed. Place cutoff derivatives outside the transition whenever possible.

---

## 2. Normalization and global equations (2.1)–(2.5)

Distinguish the numerical constant \(A=K_X^2\) from the determinant connection \(A_\varepsilon\). Fix the conventions
\[
a=c_1(\det\mathfrak s)=\left[\frac{iF_A}{2\pi}\right],\qquad
D_A\Phi=0,\qquad F_A^+=q(\Phi),
\]
with
\[
|q(\Phi)|^2=\frac{|\Phi|^4}{8},
\qquad
\frac12\,c(q(\Phi))\Phi=\frac14|\Phi|^2\Phi.
\]
The second identity fixes the Clifford sign; the norm identity alone would not do so.

Writing \(U=|\Phi|^2\), the spinor equation becomes
\[
4\nabla_A^*\nabla_A\Phi+s\Phi+U\Phi=0. \tag{W}
\]
Integration on the closed smoothing gives exactly
\[
4\int|\nabla_A\Phi|^2+\int sU+\int U^2=0. \tag{2.1}
\]
Hence
\[
\|U\|_2\le\|s^-\|_2, \tag{2.2}
\]
including the case \(U\equiv0\), and
\[
4\int|\nabla_A\Phi|^2
\le\|s^-\|_2\|U\|_2. \tag{2.3}
\]

The real closed form \(\mathcal F=iF_A\) has harmonic projection \(2\pi h_a\). Since the Hodge star preserves harmonic forms,
\[
\int|F_A^+|^2\ge4\pi^2\|h_a^+\|_2^2
=4\pi^2(a_g^+)^2.
\]
Thus the claimed lower bound is correct:
\[
\boxed{\int|\Phi|^4
=8\int|F_A^+|^2
\ge32\pi^2(a_g^+)^2
\ge32\pi^2A.} \tag{2.4}
\]

Chern–Weil gives
\[
4\pi^2a^2
=\int\mathcal F\wedge\mathcal F
=\int|F_A^+|^2-\int|F_A^-|^2,
\]
so
\[
\int|F_A^-|^2=\int|F_A^+|^2-4\pi^2a^2. \tag{2.5}
\]
All signs and factors are correct. Fixed \(a^2\), not any new lower bound for \(a^2\), is sufficient for the full curvature bound. For the recorded blow-up family, \(a^2=A-k\).

### Supply and finite selection: the necessary quantifiers

Let the finite family consist of **actual spin\(^c\) structures**, not just determinant classes. For
\[
a_\sigma=c+\sum_i\sigma_iE_i,\qquad c^2=A,
\]
the metric-wise algebra is
\[
2^{-k}\sum_\sigma(a_\sigma^+)^2
=(c^+)^2+\sum_i(E_i^+)^2\ge c^2=A.
\]
Therefore some sign has the required projection. This becomes a field statement only if the chosen sign is genuinely supplied with an unperturbed solution.

For any sequence \(\varepsilon_j\downarrow0\), select such a supplied structure for each metric. Finite pigeonhole then fixes one structure on a subsequence while retaining
\[
(a_{g_{\varepsilon_j}}^+)^2\ge A.
\]
It does **not** establish one sign that works for all sufficiently small \(\varepsilon\).

The corpus records all-\(b^+\) supply results in their specified general-type setting. Nevertheless, the field-limit theorem must name that supply input. For \(b^+=1\), negative Yamabe invariant by itself does **not** resolve the chamber issue. One needs the applicable polarization/chamber-independent supplier, or a justified small-perturbation limit for the selected structure. A class called “basic” without a chamber qualification is insufficient.

If solutions retain a perturbation in
\[
F_A^+=q(\Phi)+\text{perturbation},
\]
then (2.1), the curvature–spinor norm equality, and (2.4) acquire error terms. The displayed argument applies after a justified passage to **unperturbed** solutions, not directly to arbitrary perturbed ones.

---

## 3. Localized estimate: an exact identity replaces absorption bookkeeping

For a real bounded cutoff \(\eta\), testing (W) against \(\eta^2\Phi\) and completing the square gives
\[
4\int|\nabla_A(\eta\Phi)|^2
+\int\eta^2sU+\int\eta^2U^2
=4\int|d\eta|^2U. \tag{L1}
\]
For \(0\le\eta\le1\),
\[
\int\eta^2U^2
\le\int\eta^2s^-U+4\int|d\eta|^2U, \tag{L2}
\]
and therefore
\[
\boxed{
\int\eta^2U^2
\le
\|s^-\|_{L^2(\operatorname{supp}\eta)}\|U\|_2
+4\|d\eta\|_4^2\|U\|_2.} \tag{L3}
\]
This verifies (3.1)–(3.2), with scalar coefficient \(1\) and derivative coefficient \(4\). For unrestricted bounded \(\eta\), retain the factor \(\|\eta\|_\infty^2\) in the scalar estimate.

Piecewise Lipschitz cutoffs are admissible. More generally, bounded \(W^{1,4}\) cutoffs follow by approximation: \(\Phi\in L^4\) and \(d\eta\in L^4\) make \(d\eta\,\Phi\in L^2\). Corner smoothing is not necessary.

---

## 4. Logarithmic capacity: correct calculation, limited conclusion

Set \(r_\varepsilon=2\rho\), so the derivative of the cutoff lies entirely where \(g_\varepsilon=g\). On the exact cone, with \(L=\log(R/r_\varepsilon)\),
\[
\eta=\frac{\log(R/r)}{L},\qquad |d\eta|=\frac1{rL},
\]
and
\[
\int|d\eta|^4
=\frac{\operatorname{Vol}(S^3/\Gamma)}{L^4}
\int_{r_\varepsilon}^{R}\frac{dr}{r}
=\frac{2\pi^2}{n^2L^3}. \tag{C1}
\]
Thus
\[
\|d\eta\|_4^2=O(L^{-3/2}). \tag{C2}
\]
Indeed, the logarithmic profile is the radial critical-capacity minimizer: Hölder applied to \(\int_a^b|\eta'|\,dr\) gives the matching lower bound proportional to \(\log(b/a)^{-3}\).

On the fixed smooth orbifold metric, normal-coordinate comparison gives \(g=\delta+O(r^2)\). Consequently,
\[
\int|d\eta|_g^4
=\frac{2\pi^2}{n^2L^3}+O(R^2L^{-4}).
\]
This justifies the leading asymptotic. The correction is not uniformly \(O(\rho^2)\) over the entire annulus reaching fixed radius \(R\); its pointwise size there is \(O(r^2)\). Only zeroth-order metric and volume comparison enter this capacity integral—no connection-coefficient terms occur in the norm of a scalar differential.

The original cutoff proves (3.6), but not (3.7). At a fixed \(0<r<R\),
\[
\eta_\varepsilon(r)\longrightarrow0.
\]
It therefore gives no unweighted control of mass at radii tending to zero much more slowly than \(\rho\). The complement \(1-\eta_\varepsilon\) has support extending into the bulk, so its scalar term is not small. This is the precise annular-tail gap.

### Repair A: full tightness from the actual family

With \(\Delta=d^*d\), (W) implies
\[
2\Delta U+4|\nabla_A\Phi|^2+sU+U^2=0.
\]
At a maximum of \(U\), \(\Delta U\ge0\); hence
\[
0\le U_\varepsilon\le\|s_\varepsilon^-\|_\infty\le C
\]
by (G1). Using (G2),
\[
\boxed{
\limsup_{\varepsilon\downarrow0}
\int_{\{r<R\}}|\Phi_\varepsilon|^4
\le CR^4.} \tag{T1}
\]
This establishes full (3.7), including all annular tails.

### Repair B: full tightness using only local scalar \(L^2\) control

Fix a chart radius \(r_*\). For \(R<r_*\), put
\[
R_0=\sqrt{Rr_*},\qquad L_R=\log(R_0/R).
\]
Choose
\[
\zeta_R=
\begin{cases}
1,&r\le R,\\
\log(R_0/r)/L_R,&R<r<R_0,\\
0,&r\ge R_0.
\end{cases}
\]
For each fixed \(R\), eventually \(2\rho<R\), so its derivative lies in the unchanged orbifold region. Uniform cone comparison gives
\[
\|d\zeta_R\|_4^2\le CL_R^{-3/2}.
\]
If \(C_U=\sup_\varepsilon\|U_\varepsilon\|_2\), (L3) yields
\[
\limsup_{\varepsilon\downarrow0}
\int_{\{r<R\}}U_\varepsilon^2
\le C_U\left[
\left(\limsup_{\varepsilon\downarrow0}
\int_{\{r<R_0\}}(s_\varepsilon^-)^2\right)^{1/2}
+CL_R^{-3/2}\right].
\]
As \(R\downarrow0\), \(R_0\downarrow0\) and \(L_R\to\infty\). Equation (1.2) proves (3.7).

**Do not use moving-annulus convergence as a substitute.** Smooth convergence on fixed compact subsets does not imply convergence of integrals over \(2\rho_\varepsilon<r<\delta\). That inference would assume the very tightness being proved.

---

## 5. What the repaired estimates establish before removability

On every compact subset of \(V^{\rm reg}\), the metrics eventually equal \(g\), the restricted spin\(^c\) structure is fixed, and the solutions have bounded spinor amplitude and curvature energy. Local abelian Coulomb gauges, elliptic estimates for the Dirac and \(d^+\) equations, and a diagonal subsequence give smooth convergence modulo gauge. Gauge patching must be performed on this fixed restricted bundle; a global connection one-form need not exist.

The limit satisfies
\[
F_{A_\infty}\in L^2,\qquad
\Phi_\infty\in L^4,\qquad
\nabla_{A_\infty}\Phi_\infty\in L^2.
\]
These follow from exhaustion and lower semicontinuity. Tightness and convergence away from the point give
\[
\int_{V^{\rm reg}}|\Phi_\infty|^4
=\lim_j\int_M|\Phi_{\varepsilon_j}|^4
\ge32\pi^2A.
\]
Thus the regular-part limit is nonzero and irreducible.

This excludes spinor mass concentration, equivalently \(F_A^+\)-energy concentration. It does **not** by itself exclude concentration of \(F_A^-\).

---

## 6. Einstein identities (5.1)–(5.3)

These are global identities only after smooth orbifold extension, or after an independently justified treatment of all puncture boundary terms.

### (5.1)

Write \(s=-\lambda\), \(\lambda>0\). Here \(\lambda\) is the absolute scalar curvature, so
\[
\operatorname{Ric}=-\frac{\lambda}{4}g.
\]
The maximum principle and (2.1) give
\[
0\le U\le\lambda,\qquad
4\int|\nabla_A\Phi|^2=\int U(\lambda-U).
\]
Correct.

### (5.2)

For the extended determinant class, let \(h_a\) denote its real orbifold harmonic representative:
\[
\mathcal F=iF_A=2\pi h_a+d\alpha.
\]
Hodge orthogonality holds separately in each chirality. Orbifold Stokes gives
\[
\int d\alpha\wedge d\alpha=0,
\]
hence
\[
\|(d\alpha)^+\|_2^2=\|(d\alpha)^-\|_2^2
=\frac12\|d\alpha\|_2^2.
\]
Therefore
\[
\boxed{
\frac18\int U^2-4\pi^2\|h_a^+\|_2^2
=
\int|F_A^-|^2-4\pi^2\|h_a^-\|_2^2
=
\frac12\|d\alpha\|_2^2.}
\]
Correct. This identity sees the real class, not torsion isotropy data.

### (5.3)

For any real self-dual two-form on an oriented four-manifold,
\[
\Delta_d\psi=\nabla^*\nabla\psi+\frac{s}{3}\psi-2W^+\psi.
\]
Its integrated rearrangement is exactly (5.3). Einstein is not needed for this formula; it supplies the additional identity \(\delta W^+=0\).

The phrase “closed self-dual form identity” must be replaced by **self-dual Hodge–Weitzenböck identity**. Although \(dF_A=0\), generally
\[
dF_A^+\ne0.
\]
For self-dual \(\psi\),
\[
d^*\psi=-*d\psi,
\]
so the retained Hodge term equals \(2\|d\psi\|_2^2\), not zero. The derivative \(\nabla\psi\) is Levi–Civita, not a charged covariant derivative.

These identities do not constitute an Einstein exclusion theorem.

---

## 7. Precisely unresolved: removability and the marked lift

The required analytic result is:

> A finite-energy unperturbed monopole on the punctured smooth uniformizer, carrying the inherited \(\Gamma\)-equivariant spin\(^c\) data, is gauge-equivalent to a smooth solution across the origin, with an extended equivariant lift compatible with the fixed marked boundary structure.

A proof must establish a critical Sobolev gauge, weak extension without point-supported equation defects, elliptic regularity, and extension of the deck-action cocycle. Finite \(L^2\) curvature alone is not a blanket connection-removability theorem. The smooth PU(2) result mentioned in the notes is a template, not a verified equivariant theorem in this input.

Also correct the blueprint’s explanation of gauge sectors. For the punctured Wahl quotient,
\[
\pi_0\operatorname{Map}(L(n^2,n-1),U(1))
\cong H^1(L(n^2,n-1);\mathbb Z)=0.
\]
The issue is **torsion bundles and isotropy characters**, not disconnected ordinary \(U(1)\) gauge sectors. Nontrivial flat characters cannot be gauged away. A curved connection’s finite-radius holonomy is not automatically a representation of \(\Gamma\); the asymptotic character must be justified through extension or a separate limiting argument.

The marked topology calculation still requires an actual boundary identification for a chosen PPS embedding, a reference spin\(^c\) structure, and the affine restriction map. Twisting by a line of character \(\chi\) changes the determinant character by \(2\chi\). For even \(n\), determinant data alone can miss a two-torsion distinction between spin\(^c\) lifts; for odd \(n\), doubling is invertible in \(\mathbb Z_{n^2}\), but the reference lift remains necessary. Neither the metabolizer \(n\mathbb Z_{n^2}\) nor the withdrawn sign formula identifies the supplied lift.

## Repaired proof skeleton

The rigorous implication supported here is
\[
\text{actual finite supply}
\Longrightarrow
\text{fixed subsequential structure}
\Longrightarrow
\text{global energy bounds}
\Longrightarrow
\text{full spinor tightness}
\Longrightarrow
\text{nonzero finite-energy regular-part limit}.
\]

Use (G1)–(G3), (W), and (T1) for the explicit family; use the outward cutoff for the weaker scalar-\(L^2\) version. Equivariant removability and marked lift identification are separate remaining theorems. Only after those are established may (5.1)–(5.3) be used globally on the orbifold, and a further class-sensitive implication is still needed for any new Einstein obstruction.