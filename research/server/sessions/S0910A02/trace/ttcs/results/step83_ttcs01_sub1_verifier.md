# TTCS Independent Branch Record

```json
{
  "step_id": 83,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step83_near_pinched_construction_and_frontier_reduction.md",
    "Sessions/S0910A02/workspace/scripts/step83_full_weyl_log_annulus_audit.py",
    "Sessions/S0910A02/workspace/data/step83_full_weyl_log_annulus_audit.json",
    "Sessions/S0910A02/workspace/data/step68_qLambda_core_verify.json",
    "Sessions/S0910A02/workspace/data/step68_log_weyl_operator_check.json",
    "Sessions/S0910A02/workspace/data/step82_sign_leg_and_ricciflat_scope.json",
    "Skills/qiushi-yau26/references/research/20260912.tex"
  ]
}
```

## Task

Check the Step 83 theorem-grade audit of the fixed-A1 log-Weyl near-pinched construction for Yau--26. The central question is whether the claimed metrics on fixed A1 resolutions really satisfy ||Ric-sigma g||_op <= C/|log a| after raising an index in all three zones: EH core, log annulus, and ambient patching. Pay special attention to the sharp concern that the interpolated ambient quadratic jet may not be pure Weyl in all angular sectors at product nodes, that the Step 83 full Weyl-sector symbolic audit may or may not cover all relevant H_2 components and both chiralities, and that four-node patching/uniform constants must not hide an O(1) defect. Also check whether the note states the exact scope correctly: fixed representation/marking near-pinched input metrics only, not exact Einstein existence or nonexistence. Give a mathematical verification memo with any defects, missing hypotheses, or corrected theorem statement needed.

## Output

# Mathematical verification memo

## Main finding

With one important textual strengthening, the fixed-\(A_1\) construction supports the estimate
\[
\bigl\|\operatorname{Ric}_{g_a}-\sigma g_a\bigr\|_{\mathrm{op},\infty;g_a}
\le \frac{C}{|\log a|}
\]
on every fixed smooth resolution described in Step 83. The needed strengthening is that the ambient quadratic jet and the gauged Eguchi–Hanson quadratic jet are expressed in the **same radial normal gauge**, not merely that their Ricci contractions agree.

Under that gauge identification:

* the core estimate acquires the essential factor \(a^{-2}\) when an index is raised, but the \((0,2)\) residual is \(O(a^4(1+\rho)^2)\), leaving an operator residual \(O(a^2(1+\rho)^2)\);
* the annular mismatch is a general ten-dimensional Weyl quadratic tensor, and the logarithmic cutoff produces \(O(L^{-1})\);
* the outer truncation contributes \(O(R^2)\) because the \(A_1\) symmetry removes the cubic Taylor term;
* finitely many disjoint node regions contribute through a maximum of local constants, with no cross-node curvature term.

I find no hidden \(O(1)\) contribution in these three regions.

---

## 1. Why the quadratic mismatch is pure Weyl

In an equivariant normal chart at an \(A_1\) point, the lifted orbifold metric has
\[
g_0=e+H_0+E_4,\qquad
\partial^jE_4=O(r^{4-j}),\quad 0\le j\le2,
\]
and
\[
D\operatorname{Ric}_e(H_0)=\sigma e.
\]
The \(O(r^4)\) remainder follows because the deck action is exactly \(x\mapsto-x\) in exponential coordinates, so the component functions of the metric are even.

The supplied Eguchi–Hanson calculation gives a smooth tensor \(\widetilde h\) with
\[
D\operatorname{Ric}_{g_{\rm EH}}\widetilde h=g_{\rm EH},
\qquad
\widetilde h=H_*+O(\rho^{-2})
\]
with differentiable ALE tails, where
\[
H_*=-\frac5{36}\bigl(r^2e-(x\cdot dx)^2\bigr)
+\frac1{12}\langle Jx,dx\rangle^2.
\]
Directly,
\[
H_*(x,\cdot)=0,\qquad D\operatorname{Ric}_eH_*=e.
\]
Thus, after applying the fixed orthogonal marking and setting \(H_1=\sigma H_*\),
\[
D\operatorname{Ric}_e(H_1)=\sigma e,\qquad H_1(x,\cdot)=0.
\]

Consequently
\[
K=H_0-H_1
\]
is a homogeneous quadratic normal tensor with zero Ricci contraction. The standard isomorphism between quadratic normal tensors and algebraic curvature tensors therefore gives
\[
K_{ij}=-\frac13C_{ikjl}x^kx^l
\]
for a Ricci-free algebraic curvature tensor \(C\), hence a Weyl tensor. It follows that
\[
\operatorname{tr}K=0,\quad
\operatorname{div}K=0,\quad
\Delta K=0,\quad
K(x,\cdot)=0.
\]

Equality of Ricci contractions by itself does not imply these four displayed identities unless the two jets have first been placed in a common normal gauge. The displayed vector field
\[
V=\frac5{72}(r^3-r^{-1})\partial_r
\]
is therefore load-bearing: it both preserves the equation
\(D\operatorname{Ric}_{\rm EH}\widetilde h=g_{\rm EH}\) and produces the required radial far-field jet.

---

## 2. Coverage of all quadratic Weyl sectors

For a four-dimensional algebraic curvature operator,
\[
\mathcal R=
\begin{pmatrix}
W^++\frac{s}{12}I & \mathring{\operatorname{Ric}}^{\,\#}\\
(\mathring{\operatorname{Ric}}^{\,\#})^* & W^-+\frac{s}{12}I
\end{pmatrix}.
\]
Since \(H_0\) and \(H_1\) have identical Ricci contraction, the scalar and off-diagonal Ricci blocks cancel. The remaining space is
\[
\operatorname{Sym}^2_0(\Lambda^+)\oplus
\operatorname{Sym}^2_0(\Lambda^-),
\]
of dimension \(5+5=10\).

The Step 83 SymPy script constructs two diagonal and three off-diagonal trace-free \(3\times3\) matrices in each chirality. These are bases of the two five-dimensional summands. Thus it covers every Ricci-free quadratic mode, not just the \(U(2)\)-invariant Eguchi–Hanson mode. The Ricci-bearing quadratic modes are absent from the script for the correct reason: they have already canceled in \(H_0-H_1\).

An orientation-preserving orthogonal marking acts separately on the two summands; an orientation-reversing marking exchanges them. Since both are included, arbitrary fixed orthogonal markings and both Eguchi–Hanson chiralities are covered. At a product node, \(K\) may have simultaneous \(W^+\) and \(W^-\) components, but linear combinations across the ten basis elements are included.

The JSON records exact symbolic vanishing for every basis element. It does not explicitly record linear independence, algebraic Bianchi symmetry, or the rank ten of the polynomial tensors. Those facts follow from the curvature-operator construction, rather than from the Boolean output alone.

### General logarithmic-cutoff formula

The three monomial tests in the script corroborate the formula but are not the cleanest proof for a general profile. For any radial \(\eta(r)\),
\[
\operatorname{tr}(\eta K)=0,\qquad
\operatorname{div}(\eta K)=0
\]
because \(K(x,\cdot)=0\). Hence
\[
D\operatorname{Ric}_e(\eta K)=-\frac12\Delta(\eta K).
\]
Since \(K\) is harmonic and homogeneous of degree two,
\[
\Delta(\eta K)
=\left(\eta_{rr}+\frac7r\eta_r\right)K.
\]
Writing \(t=\log r\) gives
\[
D\operatorname{Ric}_e(\eta K)
=-\frac1{2r^2}\bigl(\eta_{tt}+6\eta_t\bigr)K.
\]
For
\[
\eta=\psi\!\left(\frac{\log(r/(4b))}{L}\right),
\]
this is precisely
\[
-\frac1{2r^2}
\left(\frac{\psi''}{L^2}+\frac{6\psi'}L\right)K.
\]
This analytic derivation completes the passage from the monomial computations to the actual cutoff.

---

## 3. Eguchi–Hanson core after raising an index

Let \(k=g_{\rm EH}\) and
\[
\widehat g_a=k+a^2\sigma\widetilde h,\qquad
G_a=a^2\widehat g_a.
\]
On
\[
1\le \rho\le b/a=a^{-1/2},
\]
the relative perturbation obeys
\[
a^2|\widetilde h|_k\le Ca^2(1+\rho)^2\le Ca,
\]
so \(\widehat g_a\) remains uniformly equivalent to \(k\).

Using
\[
D\operatorname{Ric}_k\widetilde h=k
\]
and the weighted bounds
\[
|\nabla^j\widetilde h|_k\le C_j(1+\rho)^{2-j},
\qquad 0\le j\le2,
\]
the nonlinear Ricci expansion gives
\[
\bigl|\operatorname{Ric}_{G_a}-\sigma G_a\bigr|_k
\le Ca^4(1+\rho)^2.
\]
The constant scaling does not change Ricci as a \((0,2)\) tensor. Raising an index with
\[
G_a^{-1}\sim a^{-2}k^{-1}
\]
therefore yields
\[
\bigl|G_a^{-1}
(\operatorname{Ric}_{G_a}-\sigma G_a)\bigr|
\le Ca^2(1+\rho)^2
\le C(a^2+b^2)=O(a).
\]
This is the decisive scale calculation. Treating the physical core as uniformly Euclidean would miss the factor \(a^{-2}\), but Step 83 uses it correctly.

In physical coordinates \(r=a\rho\), the core metric has the expansion
\[
G_a=e+H_1+E_a,
\]
with
\[
|\partial^jE_a|
\le C_j\left(a^4r^{-4-j}+a^4r^{-2-j}\right),
\qquad 0\le j\le2.
\]
A cutoff at \(r\asymp b\) therefore contributes
\[
C\left(a^4b^{-6}+a^4b^{-4}\right).
\]
The truncated model \(e+H_1\) itself has residual \(O(b^2)\). Hence the inner transition satisfies
\[
\delta_\sigma\le
C\left(a^2+b^2+a^4b^{-6}+a^4b^{-4}\right).
\]

The Step 68 JSON verifies the coefficients of \(\widetilde h\). The equation for \(\widetilde h\) rests on the exact Bianchi-IX family
\(\operatorname{Ric}(q_\Lambda)=\Lambda q_\Lambda\) and naturality under the gauge field \(V\); the JSON is supporting algebra rather than the entire argument.

---

## 4. Logarithmic annulus

On \(4b<r<R/2\), put
\[
g=e+q,\qquad q=H_1+\chi K.
\]
Because
\[
D\operatorname{Ric}_eH_1=\sigma e,
\]
one has
\[
\operatorname{Ric}_g-\sigma g
=D\operatorname{Ric}_e(\chi K)
+N_e(q)-\sigma q.
\]
The linear cutoff term is \(O(L^{-1})\), since \(K=O(r^2)\).

Moreover,
\[
q=O(r^2),\qquad
Dq=O(r)(1+L^{-1}),\qquad
D^2q=O(1+L^{-1}+L^{-2}),
\]
so the nonlinear part is more precisely
\[
N_e(q)=O\!\left(r^2(1+L^{-1}+L^{-2})\right).
\]
Thus
\[
\bigl\|\operatorname{Ric}_g-\sigma g\bigr\|_{\mathrm{op},g}
\le C\left(L^{-1}+R^2\right),
\]
because \(g\) is uniformly equivalent to \(e\) for small \(R\).

The \(O(L^{-1})\) term originates in the linear cutoff operator. No angular mode produces a larger contribution.

---

## 5. Outer patch and four-node assembly

At the outer interface,
\[
g_0=e+H_0+E_4,\qquad \partial^jE_4=O(r^{4-j}).
\]
Interpolating between \(e+H_0\) and \(g_0\) at \(r\asymp R\) produces
\[
O(R^{-2})\,O(R^4)=O(R^2)
\]
in Ricci. Uniform metric equivalence again converts this directly to an operator estimate.

For finitely many nodes, choose a fixed normal-chart radius below half the minimum node separation. Once \(a\) is small, all regions with radius \(R=a^{1/4}\) are disjoint. Ricci depends locally on the metric and its first two derivatives, so modifications in distinct balls create no cross-node terms. The global constant is the maximum of finitely many chart, marking, tail, and cutoff constants. Fixed markings are essential; no \(a\)-dependent rotation is being differentiated.

With
\[
b=a^{1/2},\qquad R=a^{1/4},\qquad
L=\log\frac{R}{8b}
=\frac14|\log a|-\log8,
\]
the combined estimate is
\[
\delta_\sigma(g_a)
\le C\left(
a^2+b^2+a^4b^{-6}+a^4b^{-4}
+L^{-1}+R^2
\right),
\]
hence
\[
\delta_\sigma(g_a)
\le C\left(a+a^{1/2}+|\log a|^{-1}\right)
\le \frac{C'}{|\log a|}
\]
for all sufficiently small \(a\).

---

## 6. Corrected theorem statement

A precise version supported by the supplied calculations is:

> **Fixed marked \(A_1\) resolution theorem.**  
> Let \((\mathcal O^4,g_0)\) be a closed oriented Einstein orbifold with
> \(\operatorname{Ric}_{g_0}=\sigma g_0\) and finitely many isolated \(A_1\) points. At each point fix an equivariant orthonormal chart with action \(x\mapsto-x\), a fixed Eguchi–Hanson end marking, and the gauged smooth tensor \(\widetilde h_i\) satisfying
> \[
> D\operatorname{Ric}_{g_{\rm EH}}\widetilde h_i=g_{\rm EH},\qquad
> \widetilde h_i=H_{*,i}+O_2(\rho^{-2}),
> \]
> where \(H_{*,i}(x,\cdot)=0\) and
> \(D\operatorname{Ric}_eH_{*,i}=e\).
> Let \(M\) be the fixed smooth manifold obtained from these marked fillings. Then there are \(a_0,C>0\) and smooth metrics \(g_a\) on \(M\), \(0<a<a_0\), such that
> \[
> \bigl\|\operatorname{Ric}_{g_a}-\sigma g_a\bigr\|_{\mathrm{op},\infty;g_a}
> \le C|\log a|^{-1}.
> \]
> The constants may depend on \((\mathcal O,g_0)\), the finite marked filling data, and the fixed cutoff profiles, but not on \(a\).

For \((S^2\times S^2)/\mathbb Z_2\), \(\sigma=1\). The analytic construction applies independently at the four nodes and therefore applies to every fixed chirality pattern. Identification of those patterns with the named connected sums is supplied by the separate toric-topology calculation in the TeX manuscript.

---

## 7. Exact reach for Yau–26

The construction establishes smooth **input metrics** on each fixed row with
\[
\|\operatorname{Ric}_{g_a}-g_a\|_{\mathrm{op}}\to0.
\]
It neither constructs an Einstein metric on those rows nor proves that none exists. The current uncertainty for \(\lambda>0\), \(\lambda=0\), and \(\lambda<0\) therefore remains logically separate from the local metric construction.

There is also a quantifier point relative to the stated research goal. If one row were shown to admit no Einstein metric for any \(\lambda\), this positive family would yield counterexamples to every proposed interval \(c_4<C_4\) with \(C_4>0\): after replacing \(g_a\) by \(t g_a\), the Ricci eigenvalues relative to \(t g_a\) are divided by \(t\), so they can be placed tightly around any chosen number in \((\max\{c_4,0\},C_4)\). Intervals with \(C_4\le0\) are not reached by this positive family. Thus all-\(\lambda\) Einstein nonexistence would settle the conclusion side for the fixed row, while the full negation of the original existential interval still requires input metrics addressing intervals contained in \((-\infty,0]\).

Overall, the \(O(|\log a|^{-1})\) construction is mathematically coherent once the common radial gauge and the weighted core remainder estimate are stated explicitly.