# Step 64 addendum: KK stress-equation rank analysis in dimension 5

Session: S0910A03. Agent1 / Orchestrator. Phase: Explore.

## 1. The rank obstruction

For a principal torus bundle \(T^k\to M^n\to B^m\) with constant-coefficient
curvature 2-forms \(F^a\) on a flat base \(T^m\), the base stress equation is
\[
\sum_a F^a\odot F^a=c\,g_B.
\]

In dimension \(m=3\), a 2-form is \(F=\iota_v\Omega\) for a vector \(v\), and
\(F\odot F=|v|^2I-vv^T\). With \(k\) forms,
\(\sum_a F^a\odot F^a=\bigl(\sum_a|v_a|^2\bigr)I-\sum_a v_av_a^T\).
The matrix \(\sum_a v_av_a^T\) has rank \(\le k\). For the stress to equal a
multiple of \(I\), we need \(\sum_a v_av_a^T\) to be a multiple of \(I\), which
requires \(k\ge m\).

- \(m=3\): need \(k\ge3\). A \(T^2\)-bundle over \(T^3\) (\(n=5\)) has \(k=2<3\):
  **unsolvable**. A \(T^3\)-bundle over \(T^3\) (\(n=6\)) has \(k=3\): solvable
  with orthonormal \(v_a\).
- \(m=4\): a 2-form has even rank \(\le2\), so \(F\odot F\) has rank \(\le2<4\).
  With \(k\) forms, rank \(\le2k\). Need \(2k\ge4\), i.e. \(k\ge2\). A
  \(T^1\)-bundle over \(T^4\) (\(n=5\)) has \(k=1\): **unsolvable**. A
  \(T^2\)-bundle over \(T^4\) (\(n=6\)) has \(k=2\): potentially solvable.
- \(m=2\): every 2-form is a multiple of the area form \(\omega\), and
  \(\omega\odot\omega=g_B\). With any \(k\ge1\), solvable.

## 2. Dimension-5 candidates

| Bundle | Base \(m\) | Fiber \(k\) | Stress solvable? |
|--------|-----------|-------------|------------------|
| \(T^2\)-bundle over \(T^3\) | 3 | 2 | No (rank) |
| \(T^1\)-bundle over \(T^4\) | 4 | 1 | No (rank) |
| \(T^3\)-bundle over \(T^2\) | 2 | 3 | Yes (all forms proportional to area) |

The only solvable \(n=5\) candidate is a \(T^3\)-bundle over \(T^2\). Such a
bundle is a nilmanifold or solvmanifold (depending on monodromy). Its total
space has polynomial fundamental-group growth, so by Milnor–Švarc it cannot
carry a negative Einstein metric (negative Einstein implies exponential growth
by Bishop–Gromov on the universal cover). On the other hand, the KK construction
with flat base and constant-coefficient forms gives a metric with constant Ricci
tensor. Whether that Ricci tensor can be made negative-definite proportional to
the metric depends on the fiber stress term.

**Conclusion:** the naive KK stress construction in \(n=5\) either fails the
rank obstruction or lands on a nil/solvmanifold whose polynomial growth
excludes negative Einstein. It does not immediately yield a counterexample.
The \(n=6\) case (\(T^3\)-bundle over \(T^3\) or \(T^2\)-bundle over \(T^4\))
is the first where the rank obstruction is absent and the topology may allow
exponential growth.

## 3. Implication for \(\mu_4\)

The rank obstruction does not directly compute \(\mu_4\), but it shows that the
KK route to an almost-Einstein \(T^4\) (as a bundle over \(T^3\) or \(T^2\))
faces the same low-rank constraints. A direct variational or Ricci-flow approach
to \(\mu_4\) is more promising.

## 4. Higher-dimensional graph manifolds

The dimension flip (slice dimension \(\ge4\) loses Preissmann protection)
suggests that higher-dimensional graph manifolds may be more viable
counterexample territory than \(n=4\). However, the KK analysis shows that the
first interesting case is \(n=6\), not \(n=5\). For \(n=6\), one can consider
graph manifolds assembled from 6-dimensional hyperbolic cusp pieces glued along
5-dimensional nilmanifold boundaries, or KK bundles over \(T^3\) with
exponential-growth monodromy.
