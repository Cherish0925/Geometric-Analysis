# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step17_rigidity_Tk_identity_and_route_assessment.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md",
    "Sessions/S0910A02/workspace/data/step17_Tk_spectral_identity.json",
    "Sessions/S0910A02/workspace/data/step17_separated_rigidity_proof.json"
  ]
}
```

## Task

Verify the three-bridge assessment for Yau Problem 26. The session claims: (1) Bridge 1 (general-to-invariant) is blocked because CZ spike prevents bounded sectional curvature from Ricci pinching, and CFG F-structure theory needs bounded sectional curvature. Is this assessment correct? Are there known results that give global structural decompositions under only Ricci bounds? Specifically check: Cheeger-Colding theory for Ricci limit spaces, Bamler's structure theory, Naber-Zhang accessible covers, and whether any of these can produce a global torus action or F-structure analog under Ricci alone. (2) Bridge 3 (finiteness-to-existence) claims that finite diffeomorphism type does not imply Einstein existence and that this is as hard as the general existence problem. Is this correct? Are there results showing that manifolds admitting Ric>0 (or near-Einstein) metrics must admit Einstein metrics? Check DeTurck's implicit function theorem approach, Besse's stability theory, and recent breakthroughs. (3) The T^k identity tr_h Ric^V = −Δ_B w/w is claimed for twist-free diagonal T^k metrics for all k and m. Verify the algebraic proof (product-rule identity for w=prod p_I). Also verify the Barta lower bound: does −Δw ≥ k(1−δ)w with w>0, w|_{∂Ω}=0 really imply λ₁≥k(1−δ)? Check whether the hypothesis of Barta's lemma requires w to be in the domain of the Dirichlet Laplacian or just a supersolution.

## Output

## Scientific verification memo

### 1. Bridge 1: Ricci pinching does not currently give global torus/F-structure data

The Step 11 CZ spike is enough to support the mathematical point being used here: a \(C^0\) two-sided Ricci estimate does **not** imply a pointwise sectional-curvature estimate. The supplied construction on \(S^2\times S^2\),

\[
g_j=dx^2+dy^2+e^{2(F_1+u_j)}d\theta^2+e^{2(F_2-u_j)}d\varphi^2,
\]

uses opposite warping so that the Hessian trace enters Ricci through \(\Delta u_j\), while the trace-free Hessian remains visible in \(\operatorname{Rm}\). With \(a_j=\Lambda_j^{-2/3}\), the note records

\[
\|\operatorname{Ric}_{g_j}-g_j\|_{\mathrm{op}}\to 0,
\qquad
|\operatorname{Rm}_{g_j}|(p_j)\to\infty .
\]

Thus bounded sectional curvature cannot be inferred from the Ricci pinching used in the invariant route.

This matters because Cheeger–Fukaya–Gromov F-structure theory is a bounded-sectional-curvature collapse theory. Its usual input is a sequence with \(|\sec|\le C\), small injectivity radius or small volume at controlled diameter, and smooth local models. The CZ spike does not refute CFG; it shows that CFG cannot be applied directly to the original Ricci-pinched metrics without an additional smoothing or curvature-control argument.

Known Ricci-only structure theories do not presently replace this with a global torus action or a global F-structure:

- **Cheeger–Colding theory.** Under Ricci lower bounds, it gives measured Gromov–Hausdorff limits, regular/singular decompositions, almost-splitting, volume convergence in the noncollapsed case, and quantitative stratification. In collapsed settings it describes the limit metric-measure space, but it does not produce a smooth global torus action on the prelimit manifolds. The output is local metric-measure geometry, not a global toric orbit space.

- **Bamler structure theory.** Bamler’s work gives powerful regularity and stratification for Ricci-limit and Einstein-limit spaces, especially in noncollapsed or Ricci-flow settings. It identifies regular regions, singular strata, and curvature-radius estimates under appropriate hypotheses. It still does not turn a general Ricci-bounded collapsed manifold into a smooth torus bundle, nor into a CFG-type global F-structure on the original manifold.

- **Naber–Zhang accessible covers.** These results are closer to the needed bridge. They give local cover-level information under \(|\operatorname{Ric}|\le n-1\), including generalized Margulis-type nilpotent structure and harmonic-radius estimates when the local fibered fundamental group has maximal nilpotency rank. The maximal-rank hypothesis is additional geometric information; it is not a consequence of Ricci bounds alone. The objects are local covers and deck groups at a chosen scale, with ranks that may vary. They do not assemble automatically into one global torus action or one global toric quotient.

So the Bridge 1 assessment is scientifically sound: present Ricci-only structure results do not supply the global invariant reduction required by the toric/separated program.

---

### 2. Bridge 3: finite diffeomorphism type does not imply Einstein existence

The Bridge 3 assessment is also correct. Finiteness of smooth types is topological compactness information; it is not a PDE existence theorem for

\[
\operatorname{Ric}_h=\lambda h .
\]

There is no known theorem of the form:

\[
M \text{ admits } \operatorname{Ric}>0
\quad\Longrightarrow\quad
M \text{ admits an Einstein metric}.
\]

In fact, broad Ricci positivity is far weaker than Einstein existence. Perelman/Sha–Yang type positive-Ricci connected-sum constructions give \(\operatorname{Ric}>0\) metrics on many connected sums. For example, applying positive-Ricci connected-sum constructions to \(\mathbb{CP}^2\) gives \(\operatorname{Ric}>0\) metrics on

\[
\#_k \mathbb{CP}^2 .
\]

For \(k\ge 5\),

\[
\chi(\#_k\mathbb{CP}^2)=k+2,\qquad \tau(\#_k\mathbb{CP}^2)=k,
\]

so Hitchin–Thorpe would require

\[
2\chi \ge 3|\tau|
\quad\Longleftrightarrow\quad
2k+4\ge 3k,
\]

which is false for \(k\ge 5\). Hence these manifolds have positive Ricci metrics but no Einstein metric.

For near-Einstein metrics, existing perturbative theory is local around a known Einstein metric:

- **DeTurck / prescribed-Ricci implicit-function theory** requires a background metric with an invertible gauge-fixed linearized Ricci or Einstein operator and closeness in \(C^{2,\alpha}\) or Sobolev norms strong enough to control the nonlinear equation. A \(C^0\) Ricci defect estimate alone gives neither an Einstein background nor high-norm closeness.

- **Besse–Koiso stability and Einstein moduli theory** describe the local structure near an existing Einstein metric, with hypotheses on the Lichnerowicz operator, infinitesimal Einstein deformations, and integrability. They do not create an Einstein metric from finite topology or from Ricci positivity.

- **Recent existence breakthroughs** such as Kähler–Einstein existence via K-stability, Einstein desingularization in special four-dimensional settings, and Ricci-flow stability near stable Einstein metrics all require extra geometric structures or a known nearby model. They do not apply to an arbitrary smooth manifold selected only by Ricci pinching.

Thus a result such as “only finitely many diffeomorphism types occur” would still leave the central Einstein-existence problem unresolved for each smooth type in the finite list.

---

### 3. Verification of the \(T^k\) determinant identity

For the twist-free diagonal metric

\[
g=g_B+\sum_{I=1}^k p_I(x)^2(d\phi^I)^2,
\qquad
w=\prod_{I=1}^k p_I,
\]

the identity

\[
\operatorname{tr}_h\operatorname{Ric}^V
=
-\frac{\Delta_B w}{w}
\]

is algebraically correct.

For the vertical unit vector \(E_I=p_I^{-1}\partial_{\phi^I}\), the multiply warped product Ricci formula gives

\[
\operatorname{Ric}(E_I,E_I)
=
-\frac{\Delta_B p_I}{p_I}
-
\sum_{J\ne I}
\frac{\langle \nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]

Summing over \(I\),

\[
\operatorname{tr}_h\operatorname{Ric}^V
=
-\sum_I \frac{\Delta_B p_I}{p_I}
-
\sum_{I\ne J}
\frac{\langle \nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]

On the other hand,

\[
\log w=\sum_I\log p_I,
\]

so

\[
\frac{\Delta_B w}{w}
=
\Delta_B(\log w)+|\nabla\log w|^2 .
\]

Expanding,

\[
\Delta_B(\log w)
=
\sum_I
\left(
\frac{\Delta_B p_I}{p_I}
-
\frac{|\nabla p_I|^2}{p_I^2}
\right),
\]

and

\[
|\nabla\log w|^2
=
\sum_{I,J}
\frac{\langle\nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]

The \(I=J\) terms cancel the \(-|\nabla p_I|^2/p_I^2\) terms, leaving

\[
\frac{\Delta_B w}{w}
=
\sum_I \frac{\Delta_B p_I}{p_I}
+
\sum_{I\ne J}
\frac{\langle\nabla p_I,\nabla p_J\rangle}{p_Ip_J}.
\]

Therefore

\[
\operatorname{tr}_h\operatorname{Ric}^V
=
-\frac{\Delta_B w}{w}.
\]

The symbolic file `step17_Tk_spectral_identity.json` verifies this for \(k=1,\dots,5\) on a flat two-coordinate base. The displayed product-rule proof is stronger than the symbolic test: it works for every base dimension \(m\), because the computation uses only the covariant product rule on \((B,g_B)\).

This identity is for diagonal, twist-free \(T^k\) metrics with one-dimensional circle factors. For a general matrix \(h_{IJ}(x)\) or for connection twist, extra terms appear.

---

### 4. Barta lower bound

The Barta step is mathematically valid if \(w\) is interpreted as a positive weak supersolution with zero Dirichlet trace.

From pinching

\[
\|\operatorname{Ric}_g-g\|_{\mathrm{op}}\le \delta,
\]

each vertical unit direction has Ricci value in \([1-\delta,1+\delta]\). Hence

\[
k(1-\delta)
\le
\operatorname{tr}_h\operatorname{Ric}^V
\le
k(1+\delta).
\]

Using the identity,

\[
-\frac{\Delta_B w}{w}
=
\operatorname{tr}_h\operatorname{Ric}^V,
\]

one gets

\[
-\Delta_B w \ge k(1-\delta)w .
\]

Let \(\alpha=k(1-\delta)\). If \(w>0\) in \(\Omega\), \(w\in H^1_0(\Omega)\cap C^2_{\mathrm{loc}}(\Omega)\), and

\[
-\Delta_B w\ge \alpha w
\]

holds weakly, then for every compactly supported smooth \(\eta\),

\[
\int_\Omega |\nabla \eta|^2\,dV_B
-
\alpha\int_\Omega \eta^2\,dV_B
=
\int_\Omega
w^2\left|\nabla\left(\frac{\eta}{w}\right)\right|^2\,dV_B
+
\int_\Omega
\left(\frac{-\Delta_B w}{w}-\alpha\right)\eta^2\,dV_B
\ge 0.
\]

By density in \(H^1_0(\Omega)\), the Rayleigh quotient satisfies

\[
\lambda_1^{\mathrm{Dir}}(\Omega,g_B)\ge \alpha
=
k(1-\delta).
\]

Thus Barta’s lower bound does **not** require \(w\) to lie in the strong operator domain \(H^2\cap H^1_0\). A positive weak supersolution is enough. The zero trace and finite-energy property are needed for the Dirichlet interpretation and for using \(w\) itself as a Rayleigh test function for the upper bound.

For smooth torus-degeneration orbit spaces, \(w=\sqrt{\det h}\) usually vanishes linearly or as a product of linear factors at rods/corners, so \(w\in H^1_0\) is plausible and often standard. The proof should still state this functional-analytic setting explicitly.

---

### 5. Related spectral-to-area point

The eigenvalue pinning

\[
k(1-\delta)
\le
\lambda_1^{\mathrm{Dir}}(\Omega,g_B)
\le
k(1+\delta)
\]

is supported by the \(T^k\) identity and Barta/Rayleigh. However, the Step 17 sentence using the Euclidean planar Faber–Krahn constant

\[
\operatorname{Area}(\Omega)\ge
\frac{\pi j_{0,1}^2}{k(1+\delta)}
\]

needs an additional geometric input. The classical constant \(\pi j_{0,1}^2\) applies to Euclidean planar domains. A general two-dimensional Riemannian orbit metric \(g_B\) does not satisfy that area estimate merely because it is two-dimensional. One needs flat Weyl coordinates with the correct measure, an isoperimetric inequality, a curvature hypothesis, or another conformal/geometric argument. The eigenvalue estimate itself remains correct; the conversion from eigenvalue to orbit-area is not automatic for arbitrary \(g_B\).