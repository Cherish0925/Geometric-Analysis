# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step62_defect_moser_general_p_proof.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md"
  ]
}
```

## Task

Verify the REPAIRED general-p two-factor defect inequality and nested Moser recurrence in step62_defect_moser_general_p_proof.md. The TTCS verification of the first draft found four defects: (a) dissipation misattribution, (b) wrong-direction s-power inequality, (c) missing p^2 in absorption, (d) norm vs squared-norm confusion. The repaired note claims all four are fixed. Check: (1) Lemma 3.2: the Kato-first cross-term estimate. Is applying Kato |nabla s| <= 2 sqrt{s}|nabla E| BEFORE Young correct? Does the resulting error term C_epsilon p^4 r^{-2} J_p have the exact power s^{p/2} matching J_p (avoiding any s-power comparison)? (2) Proposition 3.4: the gradient computation for w_p. The nabla s term contributes exactly (p^2/16) Q_p (not D_p^E) to ||nabla w_p||_2^2. Is this correct? (3) Corollary 3.5: the p-independent smallness. The absorption Cp^3 gamma_t Q_p <= (c_2/2) p^2 Q_p gives gamma_t <= c_0 independent of p. Is this correct? Verify that absorbing against D_p^E instead would give gamma_t <= p^{-1} which fails. (4) Proposition 4.2: H_p^{1/p} -> ||aE||_infty (not squared). Verify the volume cancellation: S^{1/3} V^{1/6} = r^{2/3} with S ~ r^2 V^{-1/2}. Verify the final endpoint is delta(r^2/t)^{1/3}, matching Step 34.

## Output

## Verification memo

The four requested points separate cleanly. The Kato-first cross-term estimate and the identification of the Sobolev gradient with the radial dissipation \(Q_p\) are algebraically correct. The \(L^\infty\) limit and the main volume cancellation are also correct. The \(p\)-independent absorption, however, does **not** follow from the displayed \(p\)-powers; equation (3.24) contains an algebraic slip. Thus the fixed-exponent \(p=6\) part is sound, while the large-\(p\) Moser ladder still needs a \(p\)-uniform absorption mechanism or a modified recurrence.

---

### 1. Lemma 3.2: Kato first, then Young

Let \(\alpha=p/2\). The cross term written in step62 is

\[
T_a
=
(p-1)\alpha\int \eta^2 a^{p-2}s^{\alpha-1}\nabla a\cdot\nabla s .
\]

Using

\[
|\nabla a|=2\sqrt a\,|\nabla\chi|,
\qquad
|\nabla s|\le 2\sqrt s\,|\nabla E|,
\]

one obtains

\[
|T_a|
\le
4(p-1)\alpha
\int \eta^2 a^{p-3/2}s^{\alpha-1/2}
|\nabla\chi|\,|\nabla E|.
\]

Since \(\alpha=p/2\),

\[
\alpha-\frac12=\frac{p-1}{2}.
\]

Now apply Young with the absorbing factor chosen as

\[
\bigl(\varepsilon a^{p-1}s^{p/2-1}|\nabla E|^2\bigr)^{1/2}.
\]

The complementary factor is

\[
C\varepsilon^{-1}p^2
a^{p/2-1}s^{p/4}|\nabla\chi|,
\]

and squaring it gives

\[
C\varepsilon^{-1}p^4 a^{p-2}s^{p/2}|\nabla\chi|^2.
\]

Thus

\[
|T_a|
\le
\varepsilon D_p^E
+
C_\varepsilon p^4
\int \eta^2 a^{p-2}|\nabla\chi|^2 s^{p/2}.
\]

With \(|\nabla\chi|^2\le C r^{-2}\), this becomes

\[
|T_a|
\le
\varepsilon D_p^E
+
C_\varepsilon p^4 r^{-2}J_p.
\]

So the repaired Lemma 3.2 is correct.

Two structural points matter:

1. Applying Kato before Young sends the principal gradient into \(|\nabla E|\), hence into \(D_p^E\).  
2. The error integrand is exactly \(a^{p-2}s^{p/2}\), which is precisely the integrand of \(J_p\). No comparison between different powers of \(s\) is needed.

At zeros of \(E\), one may use the standard regularization \(s_\varepsilon=s+\varepsilon\) and pass \(\varepsilon\to0\). Since the powers involved satisfy \(p\ge6\), no singular exponent appears in the final integrands.

---

### 2. Proposition 3.4: the \(\nabla s\) contribution is exactly \(Q_p\), not \(D_p^E\)

The Sobolev variable is

\[
w_p=\eta a^{(p-1)/2}s^{p/4}.
\]

Ignoring the inactive \(\nabla\eta\) term, the \(\nabla s\) part of \(\nabla w_p\) is

\[
\eta a^{(p-1)/2}\frac p4 s^{p/4-1}\nabla s.
\]

Squaring gives

\[
\left|\eta a^{(p-1)/2}\frac p4 s^{p/4-1}\nabla s\right|^2
=
\frac{p^2}{16}
\eta^2 a^{p-1}s^{p/2-2}|\nabla s|^2.
\]

This is exactly

\[
\frac{p^2}{16}
\]

times the integrand of

\[
Q_p=\int \eta^2 a^{p-1}s^{p/2-2}|\nabla s|^2.
\]

Thus the \(\nabla s\) contribution to \(\|\nabla w_p\|_2^2\) is exactly \((p^2/16)Q_p\). It is not \(D_p^E\). This distinction is essential: \(D_p^E\) controls the full tensor derivative \(|\nabla E|\), whereas \(Q_p\) controls only the radial derivative \(|\nabla s|\).

The \(\nabla a\) contribution is also correct. Since

\[
\nabla a = 2\chi\nabla\chi,
\qquad
|\nabla a|^2=4a|\nabla\chi|^2,
\]

the square of the \(\nabla a\) part gives

\[
C p^2 \eta^2 a^{p-2}|\nabla\chi|^2 s^{p/2}
\le
C p^2 r^{-2}\eta^2 a^{p-2}s^{p/2}.
\]

The mixed \(\nabla a\cdot\nabla s\) term is controlled by the same two quantities using \(2AB\le A^2+B^2\). Therefore

\[
\|\nabla w_p\|_2^2
\le
C p^2\bigl(Q_p+r^{-2}J_p\bigr)
\]

is correct.

The two-factor estimate then follows as written:

\[
P_p
=
\int F w_p^2
\le
\|F\|_{L^2(\operatorname{supp}w_p)}
\|w_p\|_{L^4}^2
\le
C p^2\gamma_t\bigl(Q_p+r^{-2}J_p\bigr),
\]

where

\[
\gamma_t=\mathcal S(t)(K_2^\eta(t))^{1/2}.
\]

This part of the repair is sound.

---

### 3. Corollary 3.5: the \(p\)-independent smallness does not follow from the displayed powers

This is the point where the current draft has a substantive algebraic problem.

From Proposition 3.4,

\[
P_p
\le
C p^2\gamma_t\bigl(Q_p+r^{-2}J_p\bigr).
\]

The defect energy inequality in Proposition 3.3 contains the reaction contribution

\[
C p\,P_p.
\]

Therefore

\[
C p\,P_p
\le
C p^3\gamma_t Q_p
+
C p^3\gamma_t r^{-2}J_p.
\]

The available radial dissipation on the left-hand side is

\[
c_2 p^2 Q_p.
\]

To absorb the \(Q_p\)-part of the reaction into the left-hand side, one needs

\[
C p^3\gamma_t
\le
\frac{c_2}{2}p^2.
\]

Dividing by \(p^3\) gives

\[
\gamma_t
\le
\frac{c_2}{2C}\frac1p.
\]

Thus the absorption condition is

\[
\gamma_t \le \frac{c}{p},
\]

not \(\gamma_t\le c_0\) with \(c_0\) independent of \(p\).

Equation (3.24) in step62 therefore contains an algebraic slip. The line

\[
Cp^3\gamma_t \le \frac{c_2}{2}p^2
\quad\Longleftrightarrow\quad
\gamma_t\le c_0
\]

should instead read

\[
\gamma_t \le \frac{c}{p}.
\]

This matters because the Moser ladder uses

\[
p_k=6\left(\frac32\right)^k\to\infty.
\]

A condition \(\gamma_t\le c/p_k\) for all \(k\) would force \(\gamma_t=0\). Hence the present estimate does not give a uniform large-\(p\) absorption.

If one tries to move the \(Q_p\)-term into \(D_p^E\) using Kato,

\[
Q_p\le 4D_p^E,
\]

then

\[
C p^3\gamma_t Q_p
\le
4C p^3\gamma_t D_p^E.
\]

The available \(D_p^E\)-dissipation is only

\[
c_1 p D_p^E.
\]

Absorption would require

\[
4C p^3\gamma_t
\le
\frac{c_1}{2}p,
\]

i.e.

\[
\gamma_t\le \frac{c}{p^2}.
\]

Thus the \(D_p^E\)-route is even more strongly \(p\)-dependent with the present constants. The intended contrast is directionally right: absorbing through \(D_p^E\) does not remove the \(p\)-dependence. But with the displayed estimates, the \(Q_p\)-route gives \(p^{-1}\), and the \(D_p^E\)-route gives \(p^{-2}\).

A \(p\)-independent absorption would follow if one had one fewer power of \(p\) in the reaction estimate, for example

\[
P_p\le C p\,\gamma_t(Q_p+r^{-2}J_p),
\]

or if the reaction entered without the extra factor \(p\), or if there were an additional source of radial dissipation of size \(p^3Q_p\). None of these is present in the current derivation.

So the fixed-exponent \(J_6\) persistence remains valid, because for \(p=6\) the condition is simply a small universal constant. But the large-\(p\) Moser ladder requires an additional idea or a corrected \(p\)-count.

---

### 4. Proposition 4.2: \(H_p^{1/p}\to\|aE\|_\infty\), not squared

The energy is

\[
H_p=J_p
=
\int \eta^2 a^{p-2}s^{p/2}
=
\int \eta^2 a^{p-2}|E|^p.
\]

Therefore

\[
J_p^{1/p}
=
\left\|
a^{1-2/p}|E|
\right\|_{L^p(\eta^2 d\mu_t)}.
\]

Since \(a=\chi^2\le1\), \(\eta=1\) on \(\operatorname{supp}a\), and \(p\to\infty\),

\[
a^{1-2/p}\to a
\]

pointwise on the active support. Hence

\[
J_p^{1/p}
\longrightarrow
\|aE\|_{L^\infty}.
\]

This is a norm of \(|E|\), not a norm of \(|E|^2\). The repaired note is correct on this point.

---

### 5. Product convergence and the Moser endpoint

The recurrence is

\[
\Lambda_k
\le
C_k\Lambda_{k-1}^{3/2},
\qquad
C_k=
C\mathcal S\,p_k^N4^k t^{-1}.
\]

Iteration gives

\[
\Lambda_k
\le
\Lambda_0^{(3/2)^k}
\prod_{j=1}^k C_j^{(3/2)^{k-j}}.
\]

Taking the \(1/p_k\) power, with

\[
p_k=p_0(3/2)^k,
\qquad p_0=6,
\]

gives

\[
\Lambda_k^{1/p_k}
\le
\Lambda_0^{1/p_0}
\prod_{j=1}^k
C_j^{(3/2)^{-j}/p_0}.
\]

The logarithm of the product is controlled by

\[
\sum_{j=1}^\infty
\left(\frac23\right)^j
\log C_j.
\]

Since

\[
\sum_{j=1}^\infty\left(\frac23\right)^j<\infty,
\qquad
\sum_{j=1}^\infty j\left(\frac23\right)^j<\infty,
\]

and

\[
\log p_j=\log 6+j\log(3/2),
\]

the product converges. The factors involving \(\mathcal S\) and \(t\) contribute

\[
\mathcal S^{2/p_0}t^{-2/p_0}.
\]

Thus the endpoint form

\[
\|aE(t)\|_\infty
\le
C\Lambda_0^{1/p_0}
\mathcal S^{2/p_0}
t^{-2/p_0}
\]

is consistent.

For \(p_0=6\),

\[
\mathcal S^{2/p_0}=\mathcal S^{1/3},
\qquad
t^{-2/p_0}=t^{-1/3}.
\]

So the endpoint has the form

\[
\|aE(t)\|_\infty
\le
C\Lambda_0^{1/6}
\mathcal S^{1/3}
t^{-1/3}.
\]

This matches the expected parabolic scaling.

---

### 6. Volume cancellation and the Step 34 endpoint

Assume the initial defect satisfies

\[
J_6(0)\le C\delta^6 V,
\]

where \(V\) is the relevant support volume. If the seed is effectively

\[
\Lambda_0\le C J_6(0),
\]

or if \(\mathcal S=O(1)\), then

\[
\Lambda_0^{1/6}
\le
C\delta V^{1/6}.
\]

Using

\[
\mathcal S\simeq r^2V^{-1/2},
\]

one obtains

\[
\mathcal S^{1/3}V^{1/6}
=
(r^2V^{-1/2})^{1/3}V^{1/6}
=
r^{2/3}V^{-1/6}V^{1/6}
=
r^{2/3}.
\]

Therefore

\[
\|aE(t)\|_\infty
\le
C\delta r^{2/3}t^{-1/3}
=
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

This is exactly the Step 34 endpoint.

There is one remaining refinement. In step62 the seed is written as

\[
\Lambda_0\le C(1+\mathcal S)J_6(0).
\]

This introduces an extra factor

\[
(1+\mathcal S)^{1/6}.
\]

If \(\mathcal S\) is uniformly bounded, this factor is harmless. If \(\mathcal S\) can be large, then the endpoint becomes

\[
\|aE(t)\|_\infty
\le
C\delta
(1+\mathcal S)^{1/6}
r^{2/3}t^{-1/3},
\]

and the exact volume-independent form no longer follows from that seed alone.

The Step 34 / A03 formulation avoids this extra factor by using a time-integrated seed of the form

\[
\int_{t/2}^t H_{p_0}(s)\,ds
\le
C\delta^{p_0}Vt,
\]

rather than a seed containing \(B_0\sim \mathcal S J_6(0)\). With that formulation, the endpoint is exactly

\[
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

Thus the principal volume cancellation is correct, but the step62 seed should either assume \(\mathcal S=O(1)\) or be aligned with the time-integrated seed used in Step 34 and A03.

The metric drift then follows as written:

\[
\int_0^T\|aE(t)\|_\infty\,dt
\le
C\delta r^{2/3}
\int_0^T t^{-1/3}\,dt
=
C\delta r^{2/3}T^{2/3}.
\]

For \(T=\theta r^2\),

\[
\int_0^T\|aE(t)\|_\infty\,dt
\le
C\delta\theta^{2/3}r^2.
\]

This is the expected drift scale.

---

### 7. Summary of the four requested checks

| Requested point | Verification |
|---|---|
| Lemma 3.2, Kato before Young | Correct. The error term has exactly the \(s^{p/2}\) power matching \(J_p\). |
| Proposition 3.4, \(\nabla s\) contributes \((p^2/16)Q_p\) | Correct. The Sobolev gradient sees the radial dissipation \(Q_p\), not \(D_p^E\). |
| Corollary 3.5, \(p\)-independent smallness | Not supported by the displayed powers. The current algebra gives \(\gamma_t\le c/p\), not \(\gamma_t\le c_0\). |
| Proposition 4.2, \(H_p^{1/p}\to\|aE\|_\infty\) and endpoint | Correct as a norm of \(|E|\). The main volume cancellation gives \(\delta(r^2/t)^{1/3}\), provided the seed does not carry an uncontrolled extra \((1+\mathcal S)^{1/6}\) factor. |

---

### 8. Overall status

The repaired note correctly fixes the dissipation attribution, the Kato-first cross-term estimate, the radial nature of the Sobolev gradient, and the norm-versus-squared-norm endpoint.

The remaining substantive point is the \(p\)-dependence in Corollary 3.5. With the current estimates,

\[
P_p\le C p^2\gamma_t(Q_p+r^{-2}J_p)
\]

and the reaction term \(CpP_p\) produce a \(C p^3\gamma_t Q_p\) term. Absorption into \(c_2p^2Q_p\) requires \(\gamma_t\le c/p\). This is compatible with fixed \(p=6\), but not with the infinite Moser ladder \(p_k\to\infty\).

To make the general-\(p\) defect Moser argument complete, one needs one of the following:

1. a sharper two-factor estimate with one fewer power of \(p\), such as  
   \[
   P_p\le C p\,\gamma_t(Q_p+r^{-2}J_p);
   \]

2. a reaction structure in which the factor \(p\) multiplying \(P_p\) is absent or reduced;

3. an additional radial dissipation term of size \(p^3Q_p\);

4. or a different recurrence in which the \(F\)-reaction is controlled by an integrable coefficient multiplying \(H_p\), rather than by a term that must be absorbed into \(Q_p\) uniformly in \(p\).

Until one of these is supplied, the fixed-exponent \(J_6\) persistence and the endpoint algebra are sound, but the large-\(p\) defect Moser closure remains conditional.