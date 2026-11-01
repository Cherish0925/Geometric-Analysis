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
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md"
  ]
}
```

## Task

Final verification of the defect Moser endpoint proof in step62_defect_moser_general_p_proof.md. The note now correctly identifies that the two-factor route fails for the Moser ladder (gamma_t <= c/p) and uses the three-factor route instead. Check: (1) Proposition 3.2: is the p-dependence of the two-factor absorption correctly derived? The reaction Cp * P_p <= Cp^3 gamma_t Q_p against c_2 p^2 Q_p requires gamma_t <= c/p. (2) Proposition 4.1: the three-factor decomposition eta^2 a^{p-1} F s^{p/2} = (aF^3)^{1/3}(eta^2 a^{p-2}s^{p/2})^{1/3} z_p^{4/3}. Verify the weight identity: LHS has a^{p-1}, RHS has a^{(p-2)/3} * a^{2(p-1)/3} = a^{(p-2+2p-2)/3} = a^{(3p-4)/3}. Is (3p-4)/3 = p-1? That requires 3p-4 = 3p-3, i.e., -4=-3, which is FALSE. Check whether the eta weights correct this: the Codex report says 'eta=1 on the support of a', so the eta factors may not help. Is the three-factor identity correct as stated? (3) Remark 4.2: the absorption epsilon p Q_p into c_2 p^2 Q_p works for p >= 2 without smallness. Verify. (4) The overall conclusion: is the defect endpoint delta(r^2/t)^{1/3} correctly established via the three-factor route?

## Output

## Verification memo: defect Moser endpoint in `step62_defect_moser_general_p_proof.md`

The algebraic core of the step62 note is correct for the two-factor non-closure and for the three-factor weight identity. The main substantive repair needed is in the seed/volume-cancellation step: the endpoint follows from the three-factor route in the time-integrated Moser form used in the companion Codex repair, but the step62 presentation of the seed through  
\(\Lambda_0=A_0+B_0\) introduces an extra factor unless one uses the time-integrated seed or proves an \(S\)-independent bound for \(B_0\).

---

### 1. Two-factor absorption and its \(p\)-dependence

The derivation in Proposition 3.2 is algebraically correct.

With

\[
z_p=\eta a^{(p-1)/2}s^{p/4},
\qquad
P_p=\int \eta^2 a^{p-1}Fs^{p/2}
     =\int Fz_p^2,
\]

the gradient estimate is

\[
\|\nabla z_p\|_2^2
\le C p^2\bigl(Q_p+r^{-2}J_p\bigr).
\]

Sobolev then gives

\[
\|z_p\|_4^2
\le C\mathcal S p^2\bigl(Q_p+r^{-2}J_p\bigr).
\]

Using \(F\in L^2\) on the localized support,

\[
P_p
\le \|F\|_2\|z_p\|_4^2
\le C p^2\gamma_t\bigl(Q_p+r^{-2}J_p\bigr),
\]

where \(\gamma_t=\mathcal S(t)(K_2^\eta(t))^{1/2}\). The energy inequality contains the reaction term as \(Cp\,P_p\). Hence the \(Q_p\)-part of the reaction is bounded by

\[
Cp\,P_p
\le C p^3\gamma_t Q_p+\text{Gronwall terms}.
\]

The available radial dissipation is \(c_2p^2Q_p\). Absorbing the reaction into this dissipation requires

\[
C p^3\gamma_t \le \frac{c_2}{2}p^2,
\]

i.e.

\[
\gamma_t\le \frac{c}{p}.
\]

Thus the two-factor route is structurally adequate for a fixed exponent such as \(p=6\), where the condition is a fixed smallness condition, but it cannot be continued uniformly along a Moser ladder \(p_k\to\infty\). The step62 statement of Proposition 3.2 is therefore correct.

---

### 2. Three-factor decomposition and weight identity

The three-factor identity stated in Proposition 4.1 is correct. The apparent weight mismatch in the question omits the factor \(a^{1/3}\) coming from \((aF^3)^{1/3}\).

Compute the right-hand side explicitly:

\[
(aF^3)^{1/3}
\bigl(\eta^2a^{p-2}s^{p/2}\bigr)^{1/3}
z_p^{4/3}.
\]

Since

\[
z_p=\eta a^{(p-1)/2}s^{p/4},
\]

we have

\[
z_p^{4/3}
=
\eta^{4/3}a^{2(p-1)/3}s^{p/3}.
\]

Also,

\[
(aF^3)^{1/3}=a^{1/3}F,
\]

and

\[
\bigl(\eta^2a^{p-2}s^{p/2}\bigr)^{1/3}
=
\eta^{2/3}a^{(p-2)/3}s^{p/6}.
\]

Multiplying the three factors gives

\[
\eta^{2/3+4/3}
a^{1/3+(p-2)/3+2(p-1)/3}
F
s^{p/6+p/3}.
\]

The exponents are

\[
\eta:\quad \frac23+\frac43=2,
\]

\[
a:\quad
\frac{1+p-2+2p-2}{3}
=
\frac{3p-3}{3}
=
p-1,
\]

\[
s:\quad
\frac p6+\frac p3=\frac p2.
\]

Therefore

\[
(aF^3)^{1/3}
\bigl(\eta^2a^{p-2}s^{p/2}\bigr)^{1/3}
z_p^{4/3}
=
\eta^2a^{p-1}Fs^{p/2}.
\]

So the identity is pointwise exact for nonnegative \(a,s,\eta\). The calculation that produced \((3p-4)/3\) dropped the \(a^{1/3}\) from the first factor.

The Hölder step is also consistent with the definition of \(Y\). The first factor has \(L^3\)-cube

\[
\int aF^3.
\]

Because \(\eta=1\) on the support of \(a\), this equals

\[
Y=\int \eta^2 aF^3.
\]

The second factor has \(L^3\)-cube

\[
\int \eta^2a^{p-2}s^{p/2}=J_p,
\]

and the third factor contributes

\[
\|z_p^{4/3}\|_3=\|z_p\|_4^{4/3}.
\]

Thus

\[
P_p
\le Y^{1/3}J_p^{1/3}\|z_p\|_4^{4/3},
\]

as used in step62.

One technical point: the Moser ladder uses non-integer exponents \(p_k=6(3/2)^k\). The algebraic identities are still meaningful pointwise for nonnegative scalars, but the PDE chain rules require the usual Kato regularization \(s_\varepsilon=s+\varepsilon\) and passage to the limit \(\varepsilon\to0\). Step62 already lists this as a required refinement.

---

### 3. Three-factor absorption and \(p\)-independence

The absorption mechanism in Proposition 4.1 and Remark 4.2 is correct in principle.

From the three-factor Hölder estimate and the Sobolev bound,

\[
\|z_p\|_4^2
\le C\mathcal S p^2(Q_p+r^{-2}J_p),
\]

one obtains

\[
\|z_p\|_4^{4/3}
\le
C p^{4/3}\mathcal S^{2/3}
(Q_p+r^{-2}J_p)^{2/3}.
\]

Therefore

\[
P_p
\le
C p^{4/3}
Y^{1/3}J_p^{1/3}
\mathcal S^{2/3}
(Q_p+r^{-2}J_p)^{2/3}.
\]

Equivalently,

\[
P_p
\le
C p^{4/3}
(\mathcal S^2Y)^{1/3}
J_p^{1/3}
A^{2/3},
\qquad
A:=Q_p+r^{-2}J_p.
\]

Young’s inequality gives, for any small \(\varepsilon>0\),

\[
P_p
\le
\varepsilon A
+
C_\varepsilon p^N\mathcal S^2YJ_p,
\]

for some fixed polynomial power \(N\). Multiplying by the chain-rule coefficient \(Cp\) gives

\[
Cp\,P_p
\le
C\varepsilon p(Q_p+r^{-2}J_p)
+
C_\varepsilon p^{N+1}\mathcal S^2YJ_p.
\]

The \(Q_p\)-part is absorbed into \(c_2p^2Q_p\) provided

\[
C\varepsilon p \le \frac{c_2}{2}p^2.
\]

For all \(p\ge6\), this holds if \(\varepsilon\) is chosen small once and for all. No condition of the form \(\gamma_t\le c/p\) appears. The price is the coefficient

\[
p^{N+1}\mathcal S^2YJ_p,
\]

which is polynomial in \(p\) and has the time-dependent coefficient \(\mathcal S^2Y\).

The coefficient \(\mathcal S^2Y\) is integrable on positive time slabs because the curvature branch gives

\[
\mathcal S(t)^2Y(t)\le \frac{C\gamma^3}{t}.
\]

On a slab \([\tau_k,t]\) with \(\tau_k\ge t/4\),

\[
\int_{\tau_k}^t \mathcal S^2Y\,ds
\le
C\gamma^3.
\]

This is bounded independently of \(p\). The polynomial powers of \(p\) are harmless in the Moser product because

\[
\sum_{k\ge1}\left(\frac23\right)^k<\infty,
\qquad
\sum_{k\ge1}k\left(\frac23\right)^k<\infty.
\]

Thus the three-factor route does achieve the needed \(p\)-independent closure of the ladder.

---

### 4. Endpoint exponent and product convergence

The product convergence argument is structurally correct. With

\[
p_k=6\left(\frac32\right)^k,
\qquad
\frac1{p_k}=\frac1{6}\left(\frac23\right)^k,
\]

a recurrence of the form

\[
\Lambda_k
\le
C\mathcal S p_k^N4^k t^{-1}\Lambda_{k-1}^{3/2}
\]

gives

\[
\|aE(t)\|_\infty
\le
C\Lambda_0^{1/6}
\mathcal S^{1/3}
t^{-1/3},
\]

because

\[
\sum_{k\ge1}\frac1{p_k}
=
\frac1{6}\sum_{k\ge1}\left(\frac23\right)^k
=
\frac13.
\]

The factors \(p_k^N\) and \(4^k\) also produce finite constants because the relevant weighted sums converge.

If the seed satisfies

\[
\Lambda_0\le C J_6(0),
\qquad
J_6(0)\le C\delta^6V,
\]

then using

\[
\mathcal S\simeq r^2V^{-1/2}
\]

gives

\[
\|aE(t)\|_\infty
\le
C\delta V^{1/6}\mathcal S^{1/3}t^{-1/3}
=
C\delta
V^{1/6}
(r^2V^{-1/2})^{1/3}
t^{-1/3}
=
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

This is the desired volume-independent endpoint.

However, step62 as written does not quite justify the seed condition needed for this cancellation.

---

### 5. The seed/volume-cancellation point that needs repair

In §5.3, step62 gives

\[
A_0=\sup_{[t/2,t]}J_6(s)\le CJ_6(0),
\]

and

\[
B_0=\int_{t/2}^t\|z_6(s)\|_4^2\,ds
\le C\mathcal S J_6(0).
\]

Therefore

\[
\Lambda_0=A_0+B_0
\le
C(1+\mathcal S)J_6(0).
\]

Substituting this into the endpoint formula gives

\[
\|aE(t)\|_\infty
\le
C\delta
(1+\mathcal S)^{1/6}
V^{1/6}
\mathcal S^{1/3}
t^{-1/3}.
\]

Since

\[
V^{1/6}\mathcal S^{1/3}
=
V^{1/6}(r^2V^{-1/2})^{1/3}
=
r^{2/3},
\]

this yields

\[
\|aE(t)\|_\infty
\le
C\delta
(1+\mathcal S)^{1/6}
\left(\frac{r^2}{t}\right)^{1/3}.
\]

The extra factor \((1+\mathcal S)^{1/6}\) is harmless only if \(\mathcal S\) is uniformly bounded above. In a collapsed setting, \(\mathcal S=r^2V^{-1/2}\) can be large, and then the endpoint would carry an additional \(\mathcal S^{1/6}\) loss. The transition in step62 from (5.6) to (5.7) omits this factor.

The correct volume-independent endpoint is obtained by using the time-integrated mixed recurrence, as in the companion Codex repair. Define

\[
I_k=\int_{\tau_k}^t H_{p_k}(s)\,ds,
\qquad
H_p=\int \eta^2a^{p-2}f^p,
\]

with \(f=|E|\) for the defect. The recurrence has the form

\[
I_{k+1}
\le
C p_k^N\mathcal S
\left(
L_k I_k
\right)^{3/2},
\qquad
L_k=Cp_k^N4^k(t^{-1}+r^{-2}).
\]

The seed is then

\[
I_0
=
\int_{t/2}^t H_6(s)\,ds
\le
t\sup_{[t/2,t]}J_6
\le
CtJ_6(0).
\]

The endpoint from this recurrence is

\[
\|aE(t)\|_\infty
\le
C\mathcal S^{1/3}t^{-1/2}I_0^{1/6}.
\]

Using \(I_0\le Ct\delta^6V\),

\[
\|aE(t)\|_\infty
\le
C\delta
\mathcal S^{1/3}
t^{-1/2}
(tV)^{1/6}
=
C\delta
\mathcal S^{1/3}
V^{1/6}
t^{-1/3}
=
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

This route avoids the extra \((1+\mathcal S)^{1/6}\) factor because the seed is the time integral of \(H_6\), not \(A_0+B_0\).

Thus the three-factor mechanism does establish the endpoint, but the step62 presentation should either:

1. use the time-integrated recurrence and seed \(I_0\le tJ_6(0)\), as in the Codex repair; or  
2. prove a seed bound \(B_0\le CJ_6(0)\) without an \(\mathcal S\) factor; or  
3. explicitly assume and justify a uniform upper bound on \(\mathcal S\).

Without one of these, the displayed volume cancellation in (5.7) does not follow from the stated \(\Lambda_0\) seed.

---

### 6. Minor precision points

A few additional refinements are needed for a fully rigorous exposition.

1. **Zero-order coefficient in the recurrence.**  
   The energy inequality contains

   \[
   Cp^N(r^{-2}+1+\mathcal S^2Y)J_p.
   \]

   On \(t\le\theta r^2\), the \(r^{-2}\) term is controlled by \(t^{-1}\). The constant \(1\) term should either be absorbed into a bounded exponential factor or included in the recurrence constant. Writing only \(t^{-1}\) is valid under the usual normalized-time convention or after absorbing a bounded factor.

2. **Fractional exponents.**  
   The ladder exponents \(p_k=6(3/2)^k\) are not all integers. The chain rules, Sobolev variables, and Hölder decompositions should be justified using \(s_\varepsilon=s+\varepsilon\) and then passing to \(\varepsilon\to0\). This is already noted in step62, but it is essential for rigor.

3. **Endpoint limit.**  
   The final passage from the Moser sequence to \(\|aE\|_\infty\) is most cleanly phrased through the Sobolev variables

   \[
   z_p=\eta a^{(p-1)/2}|E|^{p/2},
   \]

   because

   \[
   z_p^{2/p}\to a|E|
   \]

   as \(p\to\infty\). The shorthand \(J_p^{1/p}\to\|aE\|_\infty\) is acceptable only after the weighted limit is justified near \(a=0\).

4. **Dependence on the curvature branch.**  
   The three-factor route uses the bound

   \[
   \mathcal S^2Y\le C\gamma^3/t.
   \]

   This comes from the curvature \(q=3\) propagation and the \(q=2\) energy. It does not use the defect Moser endpoint itself, so there is no direct circularity at the level of the provisional first-exit interval. The overall bootstrap still requires the metric-comparison and Sobolev-persistence assumptions to be closed by the drift estimate and continuation argument.

---

### 7. Net assessment

- **Proposition 3.2:** correct. The two-factor absorption condition is \(\gamma_t\le c/p\), so it cannot close the \(p\to\infty\) Moser ladder.

- **Proposition 4.1 weight identity:** correct. The apparent exponent mismatch omits the \(a^{1/3}\) contribution from \((aF^3)^{1/3}\). With that factor included, the power of \(a\) is exactly \(p-1\).

- **Remark 4.2 absorption:** correct. The three-factor route replaces the pointwise smallness condition by the integrable coefficient \(\mathcal S^2Y\), and absorption into \(p^2Q_p\) is uniform for \(p\ge6\).

- **Endpoint \(\delta(r^2/t)^{1/3}\):** established by the three-factor route when the recurrence is formulated in the time-integrated form and seeded by \(\int_{t/2}^t H_6\le tJ_6(0)\). In step62 as written, the seed \(\Lambda_0\le C(1+\mathcal S)J_6(0)\) introduces an extra \((1+\mathcal S)^{1/6}\) factor, so the volume cancellation in (5.7) needs the seed correction described above.