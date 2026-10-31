# Precise specification for the normalized Yang–Wang continuation adaptation

> **Superseded by Step 27.** This Step 26 specification omitted the
> \((\nabla^2a)\owedge g\) contribution and therefore did not track the
> highest \(\nabla^{m+2}\chi\) terms in the cutoff-curvature induction.  The
> corrected shifted-curvature argument is in
> `step27_shifted_curvature_continuation_analysis.md` and
> `step27_normalized_local_flow_extension_theorem.md`.  Retain this file only
> as the earlier task specification, not as a proof.

## Target theorem

**Theorem (Normalized Local Flow Extension).** Let $(M^4, g_0)$ be a closed
Riemannian four-manifold, $\chi \in C_0^\infty(M)$, and $\{g(t)\}_{t\in[0,T)}$
a smooth solution of

$$
\partial_t g = -2\chi^2(\operatorname{Ric} + g), \qquad g(0) = g_0.
$$

If $T < \infty$ and $|\chi^2\operatorname{Rm}|_\infty \le C$ on $[0,T)$ with
$C$ independent of $t$, then the solution extends smoothly past $T$.

## Strategy

Follow Wang (Theorem 4.1 in the pseudolocality paper) with systematic tracking
of the additional $-2\chi^2 g$ term.

## Step 1: Short-time existence via normalized DeTurck

The DeTurck trick converts the flow into a strictly parabolic system. For
the unnormalized LRF $\partial_t g = -2\chi^2\operatorname{Ric}$, Yang
(Section 8, lines 787–823) constructs the DeTurck flow:

$$
\partial_t\hat g = -2\hat\chi^2\operatorname{Ric}(\hat g) + L_V\hat g,
$$

where $\hat\chi = \chi\circ\phi^{-1}$ and $V$ is the DeTurck vector field.

**Adaptation:** Add $-2\hat\chi^2\hat g$ to the right side:

$$
\partial_t\hat g = -2\hat\chi^2(\operatorname{Ric}(\hat g) + \hat g) + L_V\hat g.
$$

The term $-2\hat\chi^2\hat g$ is a zeroth-order expression in $\hat g$.  It
does not change the principal symbol $-2\hat\chi^2\Delta$, which is the same
degenerate/strictly-parabolic structure as the unnormalized flow.  Therefore
the same fixed-point/contraction argument gives short-time existence.

**What to check:** Verify that pullback by the diffeomorphism $\phi(t)$ gives
$\partial_tg = -2\chi^2(\operatorname{Ric}+g)$ with the fixed spatial
coefficient $\chi$.

## Step 2: Evolution of $\nabla^m\operatorname{Rm}$

Wang's Lemma 4.4 gives:

$$
\partial_t\nabla^m\operatorname{Rm}
= \chi^2\Delta\nabla^m\operatorname{Rm}
+ \sum_{i+j+k=m+2,\,k\le m+1}\nabla^i\chi*\nabla^j\chi*\nabla^k\operatorname{Rm}
+ \sum_{i+j+k=m}\nabla^i(\chi^2)*\nabla^j\operatorname{Rm}*\nabla^k\operatorname{Rm}.
$$

**Adaptation:** The new $-2\chi^2g$ contributes to the Christoffel variation:
$\partial_t\Gamma = \chi^2\nabla\operatorname{Ric} + \nabla(\chi^2)*\operatorname{Ric}
+ \chi^2\nabla g + \nabla(\chi^2)*g$.

The term $\chi^2\nabla g = 0$ (Levi-Civita connection is metric-compatible).
The term $\nabla(\chi^2)*g$ is zeroth order in curvature.  In the commutator
$[\partial_t, \nabla^m]$, these produce:

$$
\text{NEW:} \sum_{i+j=m}\nabla^i(\chi^2)*\nabla^j g
= \sum_{i=0}^m \nabla^i(\chi^2)\text{ (zeroth order in Rm)}.
$$

These are bounded by $C(m)\sup_k |\nabla^k\chi|$, which is controlled by
the induction.

## Step 3: Evolution of $\nabla^m(\chi^2\operatorname{Rm})$

Wang's Lemma 4.5:

$$
\partial_t\nabla^m(\chi^2\operatorname{Rm})
= \chi^2\Delta\nabla^m(\chi^2\operatorname{Rm})
+ (\text{same sums as 4.5})
+ \chi^2\operatorname{Rm}*\nabla^m(\chi^2\operatorname{Rm}).
$$

**Adaptation:** The tensor evolution now has an additional linear
$-2\chi^2\operatorname{Rm}$ term (from index lowering).  After applying
$\nabla^m$, this gives:

$$
\text{NEW:} -2\sum_{i+j=m}\nabla^i(\chi^2)*\nabla^j\operatorname{Rm}
\subset \sum_{i+j+k=m}\nabla^i(\chi^2)*\nabla^j(\chi^2\operatorname{Rm})*\nabla^k\operatorname{Rm}.
$$

This is already present in Wang's Lemma 4.5 structure.  No new type of term
appears.

## Step 4: Evolution of $\nabla^m\chi$

Wang's Lemma 4.6:

$$
\partial_t|\nabla^m\chi|
\le C(n,k)\sum_{k\le m-1}|\nabla^k(\chi^2\operatorname{Ric})||\nabla^{m-k}\chi|.
$$

**Adaptation:** Replace $\operatorname{Ric}$ by $\operatorname{Ric}+g$:

$$
\partial_t|\nabla^m\chi|
\le C\sum_{k\le m-1}\bigl(|\nabla^k(\chi^2\operatorname{Ric})|
+ |\nabla^k(\chi^2 g)|\bigr)|\nabla^{m-k}\chi|.
$$

Now $|\nabla^k(\chi^2 g)| \le C\sum_{j\le k}|\nabla^j\chi|$, which is
bounded by the same induction hypothesis at level $m-1$.  Therefore the
induction closes as before, possibly with larger constants.

## Step 5: $L^p$ estimates and Moser iteration

Wang's induction (Remark 4.2) couples:
1. $|\nabla^m(\chi^2\operatorname{Rm})|_p$ via $|\nabla^{m-1}\operatorname{Rm}|_{\dot p}$
2. $|\nabla^{m-1}\operatorname{Rm}|_{\dot p}$ via $|\nabla^m\chi|_{\ddot p}$
3. $|\nabla^m\chi|_{\ddot p}$ via $|\nabla^{m-1}(\chi^2\operatorname{Rm})|_{\breve p}$

At each level, the new terms from $-2\chi^2g$ contribute:
- To (1): terms involving $\nabla^{m-1}g$ (zeroth order in Rm)
- To (2): terms involving $\nabla^m\chi$ (same induction level)
- To (3): terms involving $\nabla^k(\chi^2g)$ (lower induction level)

All new contributions are controlled.  The $L^p$ estimates and Sobolev embedding
close with the same structure, giving bounded $|\nabla^m(\chi^2\operatorname{Rm})|_\infty$
for all $m$.

## Step 6: Extension

Proposition 4.3 (Hamilton's argument) applies unchanged: bounded
$|\nabla^m(\chi^2\operatorname{Rm})|_\infty$ for all $m$ implies smooth
extension past $T$.

## Summary of what needs to be written

1. **DeTurck construction:** 1 page.  Verify pullback and principal symbol.
2. **Modified Lemma 4.4:** 1/2 page.  List the new terms and bound them.
3. **Modified Lemma 4.5:** 1/2 page.  Show new terms fit existing structure.
4. **Modified Lemma 4.6:** 1/4 page.  Bound $\nabla^k(\chi^2g)$.
5. **$L^p$ closure:** 1 page.  Carry the new terms through Wang's induction.
6. **Verification script:** Check that the schematic term structure closes.

Total: ~3 pages of adaptation, no new ideas or geometric quantities needed.
