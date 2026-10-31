# First-line research: new gauge scope, energy windows, and aspherical compactness

23 September 2026. Increment from local baseline `4401d28`.

The main advances are a realized Bauer--Furuta application outside the
former complex-base category, and a topological exclusion of all half-flat
ALE bubbles that removes an assumed curvature bound from the allowed-branch
application. A compactified functional pencil supplies a two-sided
quantitative energy window. These are different conclusions, not three
counts of the same estimate.

## 1. What has changed

| Result | New conclusion relative to the baseline | Proof |
| --- | --- | --- |
| Actual gauge category | Uniform integral and negative pointwise Ricci gaps on a realized connected-sum family with vanishing ordinary SW invariants and no almost-complex structure in either orientation | [Bauer--Furuta geography](line1_bauer_furuta_geography.md), Theorems 1--2 |
| Global regularity | On closed aspherical Einstein four-manifolds, a bounded Weyl half, noncollapse/diameter data and Euler budget control the whole curvature; rational-ball bubbles are excluded as well as sphere-carrying bubbles | [Aspherical no-bubbling](line1_aspherical_no_bubbles.md), Lemma 1 and Theorem 2 |
| Actual allowed branch | On the specified non-virtually-Kähler self-gluings, vanishing relative Weyl splitting forces diameter divergence; no opposite-Weyl bound or positive lower Weyl amplitude is assumed | [Diameter-only spectral gap](line1_aspherical_no_bubbles.md), Theorem 3 and Corollary 4 |
| Functional mechanism | A constant uniform over all finite parameters \(\beta\ge2\), with its necessary degenerating weight, and a quantitative upper as well as lower Einstein energy envelope | [Compactified pencil](line1_compactified_pencil.md), Theorems 1--2 |
| Route selection, not a new main theorem | Ordinary degree-to-rank-one entropy bounds are dominated by the scalar monopole budget throughout the classical complex-base family | [Entropy comparison](line1_rank_one_entropy_scope.md) |

## 2. The realized new category

Classical symplectic geography supplies simply connected \(X_n\) with
\(\chi_h(X_n)=20n\), \(c_1^2(X_n)=178n\), for sufficiently large \(n\).
With the explicitly specified even integers \(k_n,m_n\), put
\[
 M_n=X_n\#X_n\#k_n\overline{\mathbb{CP}}^{\,2}
                 \#m_n(S^1\times S^3),\qquad A_n=356n.
\]
Bauer--Furuta theory supplies actual classes despite ordinary SW
vanishing. For each metric one chosen class works for every auxiliary
positive weight and satisfies
\[
 (a_g^+)^2\ge A_n,\qquad a_g^2=A_n-k_n\ge2\chi+3\tau.
\]
The new family realizes
\[
 h_n=\frac{4+k_n+4m_n}{A_n}\to h_0=\frac{19}{300},\qquad
 0<U_n-F(h_n)<104/A_n.
\]
The inherited two-chirality estimate therefore gives, for every metric
and all sufficiently large \(n\),
\[
 \mathcal E(g)\ge ch_0^2/8>0.
\]
Both orientations have even \(b_+\), and the Todd-number parity excludes
almost-complex structures. Thus this is not a reparametrization of a
complex general-type base with blowups and handles. Its positive Ricci
exclusion also follows from Myers; the two signwise corollaries are not
counted as two independent discoveries.

## 3. The new topological information in the allowed branch

The initial argument only yielded "diameter growth or opposite-Weyl
blow-up." The further proof removes the second escape in the actual
aspherical family.

A nonflat smooth ASD Ricci-flat ALE core has finite fundamental group.
An embedding into a closed aspherical manifold would lift to an embedding
of that same core into its contractible universal cover. If its second
Betti number is positive, its negative-definite intersection form is
impossible there. If the second Betti number vanishes, the classification
gives a core with first homology \(\mathbb Z_n\) and lens boundary with
first homology \(\mathbb Z_{n^2}\). Mayer--Vietoris would force
\[
 \mathbb Z_{n^2}\cong\mathbb Z_n\oplus H_1(C),
\]
where the second summand must have order \(n\), an impossible exponent
identity. This handles the quotient bubbles missed by a sphere-only
argument. Spin is neither assumed nor sufficient on its own.

Global-maximum curvature rescaling now turns any proposed curvature
blow-up into precisely such a forbidden embedded core. Consequently,
for the specified self-gluings and fixed \(\theta<1/\sqrt3\),
\[
 \operatorname{Ric}=-g,\quad
 b\le4\theta t,\quad\operatorname{diam}(g)\le D
 \quad\Longrightarrow\quad \fint b^2\ge\varepsilon(D,\theta)>0,
\]
where \(t=-3\lambda_1(W^+)/4\) and
\(b=\lambda_3(W^+)-\lambda_2(W^+)\). This is a global statement about
every exact metric meeting these conditions, not a gluing-neighbourhood
statement. Nonzero splitting and diameter-divergent sequences remain
possible; the complete Einstein existence question is not decided.

The prior [bounded-geometry note](line1_allowed_branch_escape.md) is
retained to show the proof development. Its opposite-curvature hypothesis
is superseded for the aspherical self-gluings by the new no-bubbling proof.

## 4. The energy statement now has two walls

The parameter-uniform estimate is
\[
 (1+b_a)(r+D_\beta/V)
       \ge c(\beta-2)^2/\beta^4,\qquad \beta\ge2.
\]
It does not assert a positive constant uniform up to infinity without
the displayed decay. At the two ends lie different allowed models.
Under the actual special-class inputs, for \(1/4<h<1/3\), any
Einstein candidate must obey
\[
 F(h)+\varepsilon h^2\le e\le G(h)-c_*\Theta(h),
\]
where \(G(h)=(4+\sqrt{1-3h})^2/9\),
\(t_*=(1-2\sqrt{1-3h})/(8+2\sqrt{1-3h})\), and
\(\Theta=t_*^3(1-2t_*)^2\). The interval without the positive margins
is classical. The new result transfers the differential non-saturation
mechanism to its upper wall, including the all-sign infimum.

## 5. Proof inheritance, next mathematical issue, and use

The new gauge application uses the inherited
[two-chirality theorem](line1_two_chirality_topology.md), through the
[energy envelope](line1_energy_envelope_gap.md),
[functional pencil](line1_functional_pencil.md), and
[bounded-form compatibility](round21_analytic.md).
The new regularity argument uses the classical ALE classification and
Einstein compactness, and the inherited actual topology and monopoles
in [Round 11](round11_graph_topology.md),
[virtual Kähler obstruction](round11_kahler.md), and
[Round 12](round12_global.md). Full sources remain in this package.
The original actual-class and normalization requirements of the Yau26
Skill have been retained; a formal cohomology vector is never substituted
for a solvable gauge system.

The next obstruction on the aspherical side is now specifically
diameter escape, or leaving the relative spectral class. It is no longer
an unspecified ALE complex-gluing problem in the bounded-diameter regime.
On the gauge side, the new family demonstrates an actual scope increase,
but does not cover all no-Einstein smooth types. Neither result solves a
complete Yau26 sign branch, and no publication-priority claim is inferred
from internal novelty.

Markdown, generated standalone LaTeX and PDFs accompany the new notes.
`verify_line1_global.py` records the named finite checks, compilation,
local links and hashes in `line1_global_evidence/results.json`.
Those computations check exact formulas; the proofs of global topology,
gauge existence and PDE statements are the cited arguments, not test
output. The bundled `skill/` is the inherited research snapshot, not a
claim that installed system Skills were updated. No live Session,
system service or installed Skill was changed.
