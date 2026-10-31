# Step 43: H-DT assessment — transported DeTurck normalized start/restart

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

Independent assessment of A03 Step 44 (`step44_normalized_yang_tame_start_restart.md`)
against Yang's source material.  The question: does adding $-2ag$ to Yang's flow
$\partial_t g = -2\chi^2 \operatorname{Ric}_g$ preserve the smooth tame inverse
and short-time existence?

---

## 1. Yang's Theorem 8.2 — what the source says

Source: `Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`, lines 785–823.

Yang proves short-time smooth existence for $\partial_t g = -2\chi^2 \operatorname{Ric}_g$
on a closed manifold.  The proof architecture:

1. **Transported coefficient DeTurck gauge:** $\hat{a} = a \circ \varphi_t^{-1}$,
   gauge term $\hat{\delta}^*(\hat{a} S^{-1} \delta G(S))$.  The gauge-modified
   equation is strictly parabolic (lines 803–807).

2. **Pullback recovery:** Yang shows that pullback by $\varphi_t$ restores the
   original equation with fixed coefficient $a$ (lines 807–808).

3. **Smooth tame inverse:** The linearized system (metric + transport) has a smooth
   tame inverse; Yang asserts this reduces nonlinear existence to "standard
   arguments" (lines 808–816).

4. **Per-datum output:** Existence time $T = T(g_0, \chi) > 0$.

---

## 2. What the normalization changes

A03's system (equations 1.1–1.3) replaces $-2\hat{a}\operatorname{Ric}_{\hat{g}}$
with $-2\hat{a}(\operatorname{Ric}_{\hat{g}} + \hat{g})$.  The gauge cancellation
is unchanged: $\varphi_t^* \hat{a} = a$, so pullback gives $-2a(\operatorname{Ric}_g + g)$.

The linearization of the new term (A03 equation 2.3):

$$
\delta(-2\hat{a}\hat{g}) = -2\hat{a}h - 2(\delta\hat{a})\hat{g},
$$

where $\delta\hat{a} = -2\hat{\chi}\,d\hat{\chi}(\zeta)$ for the transport variation
$\zeta = \delta\varphi \circ \varphi^{-1}$.

**Key property:** Both $-2\hat{a}h$ and $-2\hat{\chi}\,d\hat{\chi}*\hat{g}*\zeta$
are zeroth-order in $(h, \zeta)$ — no derivatives of the unknowns, no inverse
powers of $\hat{\chi}$.  They change only the lower-order coefficient matrices
$D, E$ in Yang's schematic linearization (A03 equations 2.1–2.2).

---

## 3. Why coefficient regularization is the operative existence route

A03 Step 45 gives a cleaner construction than importing a general perturbation
theorem for Yang's smooth-tame inverse.  For a fixed smooth datum, replace
\(a=\chi^2\) by
\[
  b_\varepsilon=\chi^2+\varepsilon^2>0.
\]
For each \(\varepsilon>0\), solve the transported-coefficient DeTurck system with
\(\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}\), so that pullback
produces the geometric equation
\[
  \partial_t g_\varepsilon
  =-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon).
\]
Fixed-\(\varepsilon\) parabolic constants may depend on \(\varepsilon^{-1}\).
The common positive interval is obtained instead from the geometric estimates in
A03 Step 45: the coupled finite-\(L^p\) propagation for \(T,U\), the current
\((U_m,C_{m+1})\) pair, and the fixed-background connection-difference induction.
Those estimates use
\[
0<b_\varepsilon\le2,
\qquad \nabla^r b_\varepsilon=\nabla^r(\chi^2)\ (r\ge1),
\qquad {|\nabla b_\varepsilon|^2\over b_\varepsilon}\le4|d\chi|^2,
\qquad {\chi^2\over b_\varepsilon}\le1,
\]
and do not differentiate \(b_\varepsilon^{-1}\).  Hence they have no negative
power of \(\varepsilon\) on the fixed datum's bootstrap interval.

The smooth compactness step is also geometric.  With
\(\bar\nabla=\nabla^{g_0}\) and \(A_\varepsilon=\nabla^{g_\varepsilon}-\bar\nabla\),
\[
  \partial_tA_\varepsilon
  =g_\varepsilon^{-1}*\nabla\operatorname{Ric}(U_\varepsilon).
\]
The already obtained spatial bounds for \(U\), followed by induction using
\(\bar\nabla=\nabla+A_\varepsilon\), give uniform fixed-background space-time
bounds.  A smooth subsequential limit solves
\[
  \partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]
Only after this limit is obtained may one use the exact-flow identities
\(a=0\) on the complement, stationary collars, and disjoint-support summation.
For \(\varepsilon>0\) the complement still evolves by
\(-2\varepsilon^2(\operatorname{Ric}+g)\), so the global \(Q\) decomposition is
not available before the limit.

---

## 4. Restart and the role of uniqueness

The construction supplies existence and restart, not a canonical maximal flow.
If an exact solution has a smooth positive terminal metric \(g_*\), apply the
same fixed-datum construction to \((g_*,\chi)\).  The equation is autonomous, so
all time jets at the joining time are determined recursively by \(g_*\) and
\(\chi\); the right-hand solution glues smoothly to the left-hand solution.

Uniqueness of the degenerate geometric flow would be useful for a canonical flow
or for identifying all regularization subsequential limits, but this restricted
negative-gap argument needs only one extendible smooth exact flow carrying the
energy estimates.

---

## 5. Relation to Yang's theorem

Yang's Theorem 8.2 remains the source model for transported coefficients and for
why the fixed-\(\varepsilon\) DeTurck equation is the correct parabolic system.
The normalization term
\[
  \delta(-2\widehat a\widehat g)
  =-2\widehat a h-2(\delta\widehat a)\widehat g
\]
is zeroth order in the metric and transport variations.  This supports the
adaptation, but by itself it does not prove that every lower-order smooth-tame
perturbation preserves Yang's inverse.  The proof used here is therefore the
coefficient-regularized geometric construction above, with Step 45's corrected
finite-exponent ledger.

---

## 6. Summary of the analytic input supplied

| Input | Present source | Role |
|-------|----------------|------|
| H-WU | A01 Step 43 corrected by A03 Step 45 and Step 44 review | Weighted extension through the current pair \((U_m,C_{m+1})\), then \(T_m\) |
| H-DT | A03 Step 45 coefficient regularization, with transported coefficient | Per-datum existence of at least one exact flow and smooth restart |

The per-datum flow platform is now usable for the restricted Ishida--LeBrun
negative route after the Step 44 corrections.  Sequence-uniform estimates are
not part of this start theorem; they enter later on the exact flow through the
selected-support first-exit system.
