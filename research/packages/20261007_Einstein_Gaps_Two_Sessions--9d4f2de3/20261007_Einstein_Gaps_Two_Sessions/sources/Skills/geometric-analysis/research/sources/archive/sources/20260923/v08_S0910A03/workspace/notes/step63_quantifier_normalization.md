# Step 63: Quantifier normalization and the cross-zero obstruction

Session: S0910A03. Agent2 / Constructor. Phase: Explore.

## The key structural reduction

The original Yau 26 statement asks for constants $c_n < C_n$ (depending only on $n$)
such that $c_n g \le \operatorname{Ric}_g \le C_n g$ implies Einstein existence.

**Claim.** For $n \ge 4$, any valid pair $(c_n, C_n)$ must satisfy either
$0 < c_n < C_n$ or $c_n < C_n < 0$. That is, the interval must NOT cross zero.

*Proof.* Suppose $c_n < 0 < C_n$. Let $(M, g_0)$ be any closed $n$-manifold.
The rescaled metric $g = t \cdot g_0$ (constant $t > 0$) has the same Ricci tensor
as a (0,2)-tensor: $\operatorname{Ric}_g = \operatorname{Ric}_{g_0}$. But the
eigenvalues of $\operatorname{Ric}$ with respect to $g$ scale as $1/t$:
if $\operatorname{Ric}_{g_0}(v,v) = \lambda g_0(v,v)$, then
$\operatorname{Ric}_g(v,v) = \lambda g_0(v,v) = (\lambda/t) g(v,v)$.
For $t$ large enough, all eigenvalues lie in $[c_n, C_n]$.
Since there exist closed $n$-manifolds without Einstein metrics for $n \ge 4$
(Hitchin–Thorpe violation in dimension 4; fundamental group obstructions in
higher dimensions), the implication fails. $\square$

## Consequence: single-sign normalization

The problem reduces to two independent single-sign questions:

**Positive branch.** Does there exist $\delta_n^+ > 0$ such that
$$(1-\delta_n^+)g \le \operatorname{Ric}_g \le (1+\delta_n^+)g$$
implies $M$ carries an Einstein metric?

**Negative branch.** Does there exist $\delta_n^- > 0$ such that
$$-(1+\delta_n^-)g \le \operatorname{Ric}_g \le -(1-\delta_n^-)g$$
implies $M$ carries an Einstein metric?

The full Yau 26 answer is YES iff BOTH branches hold for every $n \ge 2$.
A disproof requires failure of at least one branch for at least one $n \ge 4$.

**Note.** The two branches may use different manifolds and different constants.
A single manifold need not defeat both.

## The core scientific object

After normalization, the central object is the behavior of sequences of metrics
with $\|\mathring{\operatorname{Ric}}\|_{C^0} \to 0$ (trace-free Ricci going to zero
uniformly). The resolution of Yau 26 hinges on whether such sequences are:

- **Precompact** (modulo diffeomorphisms and rescaling): a subsequence converges
  to an Einstein metric, proving existence. OR
- **Degenerate**: topology escapes into shrinking regions, yielding counterexamples.

The mechanism that breaks precompactness (Weyl blowup, volume collapse, neck formation)
is the decisive scientific object.

## Status of the two branches after Step 63

### Negative branch ($\sigma = -1$)

- **n=2,3**: YES (uniformization, Hamilton).
- **n=4**: OPEN. Ishida–LeBrun gives restricted gap on specified topology
  (conditional). Graph manifold counterexample blocked by flat-slice barrier
  + T³ Einstein impossibility. Anderson's theorem closes sectional-pinching routes.
  Orbifold desingularization (Direction 3) is the most promising remaining route.
- **n≥5**: OPEN. No mechanism identified. Collapsed torus bundles (Direction 4)
  are the only concrete proposal.

### Positive branch ($\sigma = +1$)

- **n=2,3**: YES (uniformization, Hamilton).
- **n=4**: OPEN. No candidate identified. Hitchin–Thorpe violation gives pinching gap.
  K-stability gap (Direction 2) is the most promising route.
- **n≥5**: OPEN. No mechanism identified.

## The five TTCS directions

| Direction | Branch | Type | Feasibility | Key mechanism |
|-----------|--------|------|-------------|---------------|
| 1. Trace-free Ricci flow | + | Existence | Low-Med | Weyl decoupling via Gauss-Bonnet |
| 2. K-stability gap | + | Both | Med-High | Ding functional properness |
| 3. Orbifold desingularization | − | Counterexample | Med | ALE gluing with C⁰ control |
| 4. Collapsed torus bundles | − | Counterexample (n≥5) | Low-Med | O'Neill eigenvalue matching |
| 5. Lichnerowicz spectral gap | Both | Bridge | Med | Bochner-Weitzenböck + Weyl bound |

## Assessment

The quantifier normalization is a genuine simplification: it eliminates the
mixed-sign case and reduces the problem to two canonical single-sign questions.
This was implicit in the session's earlier work but never stated as a formal
reduction. The TTCS generator (branch 2) identified it cleanly.

The most promising near-term directions are:
1. **Direction 2 (K-stability gap)**: mature algebraic geometry machinery,
   directly addresses the positive branch.
2. **Direction 3 (Orbifold desingularization)**: systematic counterexample
   mechanism for the negative branch, complementary to the IL route.
3. **Direction 1 (Trace-free Ricci flow)**: could prove the proposition TRUE
   in dimension 3 and provide a framework for dimension 4.

The graph manifold analysis (flat-slice barrier + T³ impossibility) remains
valid as a local obstruction result but does not resolve the full problem.
