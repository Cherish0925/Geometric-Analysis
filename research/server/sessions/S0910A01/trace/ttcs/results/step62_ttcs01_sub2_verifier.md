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

Verify the general-p two-factor defect inequality and nested Moser recurrence for the restricted 4D cutoff flow. The claimed results are in the attached note step62_defect_moser_general_p_proof.md. Check adversarially: (1) Proposition 3.2: the general-p defect energy inequality J_p' + c'p^2 D_p^E <= Cp^N(1+r^{-2})J_p + Cp P_p. Is the chain rule dissipation computation correct for s^alpha with alpha=p/2? Is the integration by parts of the a^{p-2} weight correct, including the favorable dissipation and the error Cp^2 r^{-2} J_p? (2) Proposition 3.3: the two-factor absorption P_p = int F w_p^2 <= C gamma_t (D_p^E + r^{-2} J_p). Is the gradient computation for w_p = eta a^{(p-1)/2} s^{p/4} correct? The nabla s term gives a^{p-1} s^{p/2-2} |nabla s|^2 <= 4 D_p^E — verify this uses |nabla s|^2 <= 4s|nabla E|^2 correctly. (3) Proposition 4.1: the recurrence Lambda_k <= C_k Lambda_{k-1}^{3/2} with C_k = C S p_k^N 4^k t^{-1}. Is the time-cutoff argument correct? (4) Proposition 4.2: the endpoint ||aE||_inf^2 <= C Lambda_0^{1/p_0} S^{2/p_0} t^{-2/p_0}. Is the product convergence correct? The sums sum_j (2/3)^j = 2 and sum_j (2/3)^j j = 6 — verify. (5) The volume cancellation: S ~ r^2 V^{-1/2}, J_6(0) <= C delta^6 V, giving ||aE||_inf^2 <= C delta r^{2/3} t^{-1/3}, hence ||aE||_inf <= C delta^{1/2} (r^2/t)^{1/6}. Is this correct, and does it contradict or correct the Step 34 claim ||aE||_inf <= C delta (r^2/t)^{1/3}?

## Output

## Verification memo: general-\(p\) defect two-factor estimate and nested Moser recurrence

This memo checks the calculations in `step62_defect_moser_general_p_proof.md` against the definitions in `step34_integrated_potential_q3_and_defect.md` and `weighted_moser_and_continuation_repair.md`. The main outcome is:

- Several algebraic ingredients are correct: the basic chain rule, the principal \(pD_p^E\) dissipation, the gradient computation for \(w_p\), the mixed Hölder weight identity, and the product sums in the Moser iteration.
- Proposition 3.2 as stated is not supported by the displayed integration-by-parts estimate. The cross-term estimate in (3.8)–(3.10) uses an incorrect power of \(s\). A corrected estimate is available, but it gives dissipation of the form
  \[
  pD_p^E + c p^2 Q_p,
  \qquad
  Q_p:=\int \eta^2 a^{p-1}s^{p/2-2}|\nabla s|^2,
  \]
  not \(c'p^2D_p^E\).
- Proposition 3.3 is algebraically correct only after inserting the missing \(p^2\) factor. This \(p^2\) makes the absorption condition \(p\)-dependent. Since the Moser recurrence sends \(p_k=6(3/2)^k\to\infty\), the two-factor absorption as written does not establish a uniform closed inequality for all \(p_k\) unless an additional mechanism removes the \(p\)-dependent smallness requirement.
- The Moser product convergence sums are correct, but the endpoint interpretation contains a square/norm confusion. The moment \(H_p^{1/p}\) converges to \(\|aE\|_\infty\), not to \(\|aE\|_\infty^2\). Therefore the recurrence, if valid, yields
  \[
  \|aE(t)\|_\infty \le C\delta\left(\frac{r^2}{t}\right)^{1/3},
  \]
  which is the same exponent as in Step 34 and A03’s weighted Moser computation. The Step 62 exponent
  \[
  \|aE(t)\|_\infty \le C\delta^{1/2}\left(\frac{r^2}{t}\right)^{1/6}
  \]
  comes from treating a norm bound as a squared-norm bound.

The detailed verification follows.

---

## 1. Proposition 3.2: chain rule, integration by parts, and dissipation

Let
\[
\alpha=\frac p2,\qquad s=|E|^2,\qquad
J_p=\int \eta^2 a^{p-2}s^\alpha,
\qquad
D_p^E=\int \eta^2 a^{p-1}s^{\alpha-1}|\nabla E|^2.
\]

Assume \(a=\chi^2\) is fixed in time on the interval under consideration. The exact chain rule is
\[
(\partial_t-a\Delta)s^\alpha
=
\alpha s^{\alpha-1}(\partial_t-a\Delta)s
-\alpha(\alpha-1)a s^{\alpha-2}|\nabla s|^2.
\tag{1}
\]
Using
\[
(\partial_t-a\Delta)s=-2a|\nabla E|^2+\Sigma_s,
\tag{2}
\]
one obtains
\[
(\partial_t-a\Delta)s^\alpha
\le
-2\alpha a s^{\alpha-1}|\nabla E|^2
-\alpha(\alpha-1)a s^{\alpha-2}|\nabla s|^2
+\alpha s^{\alpha-1}\Sigma_s.
\tag{3}
\]

### 1.1 Principal dissipation

Testing against \(\eta^2a^{p-2}\), the first term gives
\[
2\alpha\int \eta^2a^{p-1}s^{\alpha-1}|\nabla E|^2
=
pD_p^E.
\tag{4}
\]
This part of Step 62, equation (3.3), is correct.

### 1.2 Favorable \(s\)-gradient dissipation

The second term in (3) gives the favorable quantity
\[
\alpha(\alpha-1)
\int \eta^2 a^{p-1}s^{\alpha-2}|\nabla s|^2
=
\alpha(\alpha-1)Q_p,
\tag{5}
\]
where
\[
Q_p:=\int \eta^2 a^{p-1}s^{\alpha-2}|\nabla s|^2.
\tag{6}
\]
Since \(\alpha=p/2\), this carries a \(p^2\) coefficient.

Step 62 attributes a favorable term to the integration by parts of the \(a\Delta s^\alpha\) term in (3.4). That attribution is not correct: the positive \(Q_p\) term comes from the chain rule applied to the diffusion operator, namely the second term in (1), not from integrating by parts the weight \(a^{p-2}\). The integration by parts of the Laplacian produces a cross term involving \(\nabla a\), not a positive term by itself.

### 1.3 The cross term from \(\nabla a\)

After integrating the diffusion term by parts, the active \(\nabla a\) cross term has the form
\[
T_a
=
\alpha(p-1)
\int \eta^2 a^{p-2}s^{\alpha-1}\,\nabla a\cdot \nabla s.
\tag{7}
\]
Using \(|\nabla a|^2=4a|\nabla\chi|^2\le C r^{-2}a\), one can estimate it against the favorable \(Q_p\) term. For any small \(\varepsilon>0\),
\[
\begin{aligned}
|T_a|
&\le
\varepsilon\,\alpha(\alpha-1)Q_p
+
C_\varepsilon p^2 r^{-2}
\int \eta^2 a^{p-2}s^\alpha  \\
&=
\varepsilon\,\alpha(\alpha-1)Q_p
+
C_\varepsilon p^2 r^{-2}J_p.
\end{aligned}
\tag{8}
\]
This is the correct structure.

Step 62’s estimate (3.8)–(3.10) instead attempts to bound the error by an integral involving
\[
\int \eta^2 a^{p-2}s^{\alpha-1}
=
\int \eta^2 a^{p-2}s^{p/2-1}.
\tag{9}
\]
It then states that on the first-exit interval, where \(s\le 1\), one has
\[
s^{p/2-1}\le C s^{p/2}.
\tag{10}
\]
This inequality is reversed for \(0<s\le 1\): since \(p/2>p/2-1\), one has \(s^{p/2}\le s^{p/2-1}\). Thus the passage from (3.9) to (3.10) is not valid.

The corrected factorization (8) avoids this problem because the error contains \(s^\alpha=s^{p/2}\), hence exactly \(J_p\), not \(s^{p/2-1}\).

### 1.4 The dissipation coefficient \(c'p^2D_p^E\) is not obtained

The direct computation gives
\[
\frac{d}{dt}J_p
+
pD_p^E
+
c p^2 Q_p
\le
Cp^N(1+r^{-2})J_p
+
Cp\,P_p,
\tag{11}
\]
up to the signed Hessian and first-derivative cutoff terms, which are discussed in the note.

Because
\[
|\nabla s|^2\le 4s|\nabla E|^2,
\]
one has
\[
Q_p
\le
4D_p^E.
\tag{12}
\]
But this is an upper bound on \(Q_p\) in terms of \(D_p^E\). It does not imply a lower bound
\[
Q_p\ge cD_p^E.
\]
Indeed, \(Q_p\) sees only the radial derivative \(\nabla |E|\), while \(D_p^E\) sees the full tensor derivative \(\nabla E\). Therefore the term \(c p^2 Q_p\) cannot be converted into \(c'p^2D_p^E\).

Thus Proposition 3.2 as displayed,
\[
J_p'+c'p^2D_p^E
\le
Cp^N(1+r^{-2})J_p+CpP_p,
\tag{13}
\]
does not follow from the computation. The supported inequality is closer to
\[
J_p'
+
c pD_p^E
+
c p^2Q_p
\le
Cp^N(1+r^{-2})J_p
+
CpP_p.
\tag{14}
\]
This distinction matters for the absorption of \(P_p\), because \(P_p\) naturally couples to \(Q_p\) through the gradient of \(w_p\), not to \(D_p^E\) alone.

---

## 2. Proposition 3.3: gradient of \(w_p\) and two-factor absorption

The Sobolev variable is
\[
w_p=\eta a^{(p-1)/2}s^{p/4}.
\tag{15}
\]
Since \(\eta=1\) on \(\operatorname{supp} a\) and \(\operatorname{supp} d\eta\subset\{a=0\}\), the \(\nabla\eta\) contribution is inactive for \(p>1\).

Differentiating,
\[
\nabla w_p
=
\eta\frac{p-1}{2}a^{(p-3)/2}(\nabla a)s^{p/4}
+
\eta\frac p4 a^{(p-1)/2}s^{p/4-1}\nabla s.
\tag{16}
\]

### 2.1 The \(\nabla a\) contribution

Squaring the first term gives
\[
\left(\frac{p-1}{2}\right)^2
a^{p-3}|\nabla a|^2 s^{p/2}.
\]
Using \(|\nabla a|^2=4a|\nabla\chi|^2\) and \(|\nabla\chi|^2\le Cr^{-2}\),
\[
a^{p-3}|\nabla a|^2s^{p/2}
=
4a^{p-2}|\nabla\chi|^2s^{p/2}
\le
Cr^{-2}a^{p-2}s^{p/2}.
\tag{17}
\]
After integration this contributes
\[
Cp^2r^{-2}J_p.
\tag{18}
\]
This part is correct.

### 2.2 The \(\nabla s\) contribution

Squaring the second term gives
\[
\left(\frac p4\right)^2
a^{p-1}s^{p/2-2}|\nabla s|^2.
\tag{19}
\]
Since \(s=|E|^2\),
\[
\nabla s=2\langle \nabla E,E\rangle,
\]
and therefore
\[
|\nabla s|^2\le 4s|\nabla E|^2.
\tag{20}
\]
Hence
\[
a^{p-1}s^{p/2-2}|\nabla s|^2
\le
4a^{p-1}s^{p/2-1}|\nabla E|^2.
\tag{21}
\]
The right-hand side is the integrand of \(4D_p^E\). More sharply, the left-hand side is exactly the integrand of \(Q_p\) with \(\alpha=p/2\):
\[
a^{p-1}s^{p/2-2}|\nabla s|^2
=
a^{p-1}s^{\alpha-2}|\nabla s|^2.
\tag{22}
\]
Thus
\[
\|\nabla w_p\|_2^2
\le
Cp^2(Q_p+r^{-2}J_p)
\le
Cp^2(D_p^E+r^{-2}J_p).
\tag{23}
\]
This verifies the gradient computation, with the important clarification that the natural dissipation is \(Q_p\).

Also,
\[
\|w_p\|_2^2
=
\int \eta^2a^{p-1}s^{p/2}
\le
\int \eta^2a^{p-2}s^{p/2}
=
J_p,
\tag{24}
\]
because \(0\le a\le 1\).

### 2.3 The missing \(p^2\) in the statement of Proposition 3.3

From Hölder,
\[
P_p
=
\int Fw_p^2
\le
\|F\|_{L^2(\operatorname{supp}w_p)}
\|w_p\|_4^2.
\tag{25}
\]
Since \(\|F\|_{L^2}\le (K_2^\eta)^{1/2}\), Sobolev gives
\[
\|w_p\|_4^2
\le
\mathcal S(t)
\left(
\|\nabla w_p\|_2^2+r^{-2}\|w_p\|_2^2
\right).
\tag{26}
\]
Using (23) and (24),
\[
P_p
\le
C p^2\gamma_t
\left(
Q_p+r^{-2}J_p
\right),
\tag{27}
\]
where
\[
\gamma_t=\mathcal S(t)(K_2^\eta(t))^{1/2}.
\]
Equivalently, using \(Q_p\le 4D_p^E\),
\[
P_p
\le
C p^2\gamma_t
\left(
D_p^E+r^{-2}J_p
\right).
\tag{28}
\]

Step 62’s displayed Proposition 3.3, equation (3.16), writes this without the \(p^2\) factor. The proof, equation (3.23), includes \(Cp^2\). The \(p^2\) is real and comes from differentiating \(a^{(p-1)/2}\) and \(s^{p/4}\). It cannot be omitted if one wants constants uniform in \(p\).

### 2.4 Absorption requires \(p\)-dependent smallness

The unabsorbed energy inequality contains the reaction as
\[
Cp\,P_p.
\tag{29}
\]
Using (27),
\[
Cp\,P_p
\le
C p^3\gamma_t Q_p
+
C p^3\gamma_t r^{-2}J_p.
\tag{30}
\]
The available favorable dissipation contains \(c p^2Q_p\). To absorb the \(Q_p\) part of the reaction into \(c p^2Q_p\), one needs
\[
C p^3\gamma_t \le \frac c2 p^2,
\]
i.e.
\[
\gamma_t \le \frac{c}{Cp}.
\tag{31}
\]
If one uses the coarser bound \(Q_p\le 4D_p^E\) and tries to absorb into the principal \(pD_p^E\) term, the condition becomes even more restrictive:
\[
\gamma_t\lesssim p^{-2}.
\tag{32}
\]

Corollary 3.4 states a condition of the form
\[
Cp^2\gamma_t<\frac{c'}2.
\tag{33}
\]
This is not aligned with the displayed constants: depending on whether one absorbs into \(Q_p\) or \(D_p^E\), the natural conditions are \(\gamma_t\lesssim p^{-1}\) or \(\gamma_t\lesssim p^{-2}\). In either case, the required smallness depends on \(p\).

This matters because the Moser recurrence uses
\[
p_k=6\left(\frac32\right)^k\to\infty.
\]
For a fixed nonzero \(\gamma_t\), the condition \(\gamma_t\lesssim p_k^{-1}\) or \(\gamma_t\lesssim p_k^{-2}\) cannot hold for all \(k\). Therefore the two-factor absorption, as written, does not establish the closed general-\(p\) inequality (3.24) for the entire Moser sequence. It establishes a fixed-\(p\) estimate when \(p\) is finite and \(\gamma\) is small relative to that \(p\). The \(p=6\) case is therefore much safer than the general-\(p\) endpoint.

To obtain the full endpoint from this route, one would need an additional mechanism: for example, a \(p\)-uniform treatment of \(P_p\), a three-factor decomposition involving an integrated curvature quantity, a spacetime norm of \(F\) that improves with \(k\), or a different recurrence that does not require absorbing \(P_p\) for arbitrarily large \(p\).

---

## 3. Proposition 4.1: time-cutoff recurrence

The mixed time-slice identity is
\[
H_{3p/2}
\le
H_p^{1/2}\|z_p\|_4^2,
\qquad
z_p=\eta a^{(p-1)/2}s^{p/4}.
\tag{34}
\]
The weight identity is
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2.
\tag{35}
\]
This is correct. The auxiliary cutoff \(\eta\) does not spoil it because \(\eta=1\) on \(\operatorname{supp}a\), and the \(H_p\) integrand contains a positive power of \(a\).

The time-cutoff idea is also standard. Let
\[
\tau_k=t(1-2^{-(k+1)}),
\qquad
p_{k+1}=\frac32p_k,
\qquad
p_0=6.
\tag{36}
\]
Choose \(\zeta_k\) with \(\zeta_k(\tau_{k-1})=0\), \(\zeta_k=1\) on \([\tau_k,t]\), and
\[
|\zeta_k'|\le C\frac{2^k}{t}.
\tag{37}
\]
Testing the \(p_k\)-energy inequality against \(\zeta_k\) removes the need to control \(H_{p_k}(\tau_{k-1})\) directly and replaces it by
\[
\int_{\tau_{k-1}}^t \zeta_k'(s)H_{p_k}(s)\,ds.
\tag{38}
\]
Using
\[
H_{p_k}=H_{3p_{k-1}/2}
\le
H_{p_{k-1}}^{1/2}\|z_{p_{k-1}}\|_4^2,
\tag{39}
\]
one obtains
\[
\int_{\tau_{k-1}}^t \zeta_k'H_{p_k}
\le
C\frac{2^k}{t}
A_{k-1}^{1/2}B_{k-1},
\tag{40}
\]
where
\[
A_k=\sup_{[\tau_k,t]}H_{p_k},
\qquad
B_k=\int_{\tau_k}^t\|z_{p_k}\|_4^2.
\tag{41}
\]
This part of the recurrence is structurally sound.

There are nevertheless two important qualifications.

### 3.1 The recurrence depends on the closed energy inequality

The recurrence uses the energy inequality at level \(p_k\). As shown above, the closed inequality for arbitrary \(p_k\) is not established by the two-factor absorption unless the \(p\)-dependent smallness condition is resolved. Therefore Proposition 4.1 is conditional on a uniform general-\(p\) energy inequality that Step 62 has not yet supplied.

### 3.2 The Gronwall coefficient and slab shrinking

The differential inequality contains a coefficient
\[
Cp_k^N(1+r^{-2})H_{p_k}.
\tag{42}
\]
When testing with \(\zeta_k\), this contributes
\[
Cp_k^N(1+r^{-2})\int_{\tau_{k-1}}^t H_{p_k}.
\tag{43}
\]
Using (39), this can be bounded by
\[
Cp_k^N(1+r^{-2})A_{k-1}^{1/2}B_{k-1}.
\tag{44}
\]
If \(t\le \theta r^2\) and \(t\le 1\), then \(1+r^{-2}\le Ct^{-1}\), so this can be absorbed into a recurrence constant of the form
\[
Cp_k^N4^kt^{-1}.
\tag{45}
\]
However, if one instead tries to keep this term as a true Gronwall coefficient, one would generate factors like \(\exp(Cp_k^Nt)\). Such factors would endanger product convergence unless the time slabs shrink fast enough in \(k\). The note uses dyadic slabs with factor \(2^k\); whether this dominates \(p_k^N\) depends on the size of \(N\). A safer construction would choose the slab shrinking rate larger than the growth rate of \(p_k^N\). This is not fatal in itself, but it is not fully addressed in the displayed proof.

### 3.3 Addition of \(A_k\) and \(B_k\)

The quantities \(A_k\) and \(B_k\) have different analytic origins. In many parabolic Moser arguments one introduces explicit time or Sobolev scaling factors before adding them. The recurrence in Step 62 adds them directly:
\[
\Lambda_k=A_k+B_k.
\tag{46}
\]
This can be justified by absorbing dimensional constants into \(C_k\), especially because the final argument only uses logarithmic convergence of the product. But the proof should state the normalization. As written, the direct addition is acceptable only as a schematic recurrence, not as a dimensionally exact estimate.

---

## 4. Proposition 4.2: product convergence and endpoint exponent

Assume, conditionally, that the recurrence has the form
\[
\Lambda_k\le C_k\Lambda_{k-1}^{3/2},
\qquad
C_k=C\mathcal S p_k^N4^kt^{-1}.
\tag{47}
\]
Iteration gives
\[
\Lambda_k
\le
\Lambda_0^{(3/2)^k}
\prod_{j=1}^k C_j^{(3/2)^{k-j}}.
\tag{48}
\]
Since
\[
p_k=p_0\left(\frac32\right)^k,
\qquad p_0=6,
\tag{49}
\]
taking the \(p_k\)-th root gives
\[
\Lambda_k^{1/p_k}
\le
\Lambda_0^{1/p_0}
\prod_{j=1}^k
C_j^{(3/2)^{-j}/p_0}.
\tag{50}
\]

The logarithm of the product contains
\[
\sum_{j=1}^\infty \left(\frac23\right)^j
\log C_j.
\tag{51}
\]
The needed numerical sums are
\[
\sum_{j=1}^\infty \left(\frac23\right)^j
=
\frac{2/3}{1-2/3}=2,
\tag{52}
\]
and
\[
\sum_{j=1}^\infty j\left(\frac23\right)^j
=
\frac{2/3}{(1-2/3)^2}=6.
\tag{53}
\]
These are correct.

Because
\[
\log C_j
=
\log C+\log\mathcal S-\log t+N\log p_j+j\log4,
\tag{54}
\]
and
\[
\log p_j=\log 6+j\log\frac32,
\tag{55}
\]
all weighted sums converge. Therefore
\[
\prod_{j=1}^\infty
C_j^{(3/2)^{-j}/p_0}
=
C'\mathcal S^{2/p_0}t^{-2/p_0}.
\tag{56}
\]
For \(p_0=6\),
\[
\mathcal S^{2/p_0}t^{-2/p_0}
=
\mathcal S^{1/3}t^{-1/3}.
\tag{57}
\]
Thus the product convergence calculation is correct, provided the recurrence constants remain polynomial/geometric in \(k\) and do not acquire factors such as \(\exp(Cp_k^N)\).

---

## 5. The endpoint: \(H_p^{1/p}\) controls \(\|aE\|_\infty\), not \(\|aE\|_\infty^2\)

This is the most important correction.

By definition,
\[
H_p=J_p=\int \eta^2a^{p-2}s^{p/2}
=
\int \eta^2
\left(a^{1-2/p}|E|\right)^p.
\tag{58}
\]
Therefore
\[
H_p^{1/p}
=
\left\|a^{1-2/p}|E|\right\|_{L^p(\eta^2d\mu)}.
\tag{59}
\]
As \(p\to\infty\),
\[
H_p^{1/p}\to \|aE\|_\infty.
\tag{60}
\]
Equivalently,
\[
H_p^{2/p}\to \|aE\|_\infty^2.
\tag{61}
\]

The Moser iteration above bounds \(\Lambda_k^{1/p_k}\), not \(\Lambda_k^{2/p_k}\). Hence the endpoint obtained from (50) is a bound on \(\|aE(t)\|_\infty\), not on \(\|aE(t)\|_\infty^2\).

Thus the correct endpoint, conditional on the recurrence, is
\[
\|aE(t)\|_\infty
\le
C\Lambda_0^{1/p_0}
\mathcal S^{2/p_0}t^{-2/p_0}.
\tag{62}
\]
With \(p_0=6\),
\[
\|aE(t)\|_\infty
\le
C\Lambda_0^{1/6}
\mathcal S^{1/3}t^{-1/3}.
\tag{63}
\]

Step 62 instead writes
\[
\|aE(t)\|_\infty^2
\le
C\Lambda_0^{1/p_0}
\mathcal S^{2/p_0}t^{-2/p_0},
\tag{64}
\]
and then takes a square root. That step is not compatible with (58)–(60). The quantity controlled by the \(p\)-root is the norm itself.

If one wants a bound on \(\|aE\|_\infty^2\), one should square (63):
\[
\|aE(t)\|_\infty^2
\le
C\Lambda_0^{1/3}
\mathcal S^{2/3}t^{-2/3}.
\tag{65}
\]
This is different from Step 62’s (4.28).

---

## 6. Volume cancellation and comparison with Step 34

Assume the seed estimate
\[
\Lambda_0\le C(1+\mathcal S)J_6(0),
\tag{66}
\]
and
\[
J_6(0)\le C\delta^6 V.
\tag{67}
\]
Using the norm endpoint (63),
\[
\|aE(t)\|_\infty
\le
C\left[(1+\mathcal S)J_6(0)\right]^{1/6}
\mathcal S^{1/3}t^{-1/3}.
\tag{68}
\]
Substitute \(J_6(0)\le C\delta^6V\):
\[
\|aE(t)\|_\infty
\le
C\delta
(1+\mathcal S)^{1/6}
V^{1/6}
\mathcal S^{1/3}
t^{-1/3}.
\tag{69}
\]
With
\[
\mathcal S\simeq r^2V^{-1/2},
\tag{70}
\]
one obtains
\[
V^{1/6}\mathcal S^{1/3}
\simeq
V^{1/6}r^{2/3}V^{-1/6}
=
r^{2/3}.
\tag{71}
\]
In the noncollapsed regime where \((1+\mathcal S)^{1/6}\le C\), this gives
\[
\boxed{
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
}
\tag{72}
\]

This is exactly the exponent appearing in Step 34 and in A03’s weighted Moser computation.

Step 62 instead obtains
\[
\|aE(t)\|_\infty
\le
C\delta^{1/2}\left(\frac{r^2}{t}\right)^{1/6}.
\tag{73}
\]
That exponent follows only if (64) is treated as a bound on the squared norm. Since the Moser \(p\)-root actually bounds the norm, (73) is a square-root weakening caused by the square/norm confusion. It does not correct Step 34. Rather, the consistent computation reproduces the Step 34 exponent, conditional on the general-\(p\) energy inequality being established.

The corresponding metric drift integrals are:

- Using the Step 34/A03 exponent:
  \[
  \int_0^T\|aE(t)\|_\infty\,dt
  \le
  C\delta r^{2/3}\int_0^T t^{-1/3}\,dt
  =
  C\delta r^{2/3}T^{2/3}.
  \tag{74}
  \]
  With \(T=\theta r^2\),
  \[
  \int_0^T\|aE(t)\|_\infty\,dt
  \le
  C\delta\theta^{2/3}r^2.
  \tag{75}
  \]

- Using the Step 62 exponent:
  \[
  \int_0^T\|aE(t)\|_\infty\,dt
  \le
  C\delta^{1/2}r^{1/3}\int_0^T t^{-1/6}\,dt
  =
  C\delta^{1/2}r^{1/3}T^{5/6}.
  \tag{76}
  \]
  With \(T=\theta r^2\),
  \[
  \int_0^T\|aE(t)\|_\infty\,dt
  \le
  C\delta^{1/2}\theta^{5/6}r^2.
  \tag{77}
  \]
Both singularities are integrable at \(t=0\), but the first gives the stronger and algebraically consistent dependence on \(\delta\).

---

## 7. Summary of the adversarial verification

### Proposition 3.2

The chain rule and principal dissipation \(pD_p^E\) are correct. However:

1. The favorable \(Q_p\) dissipation comes from the chain rule, not from the integration by parts of \(a\Delta s^\alpha\) as written.
2. The cross-term estimate in (3.8)–(3.10) uses the false inequality \(s^{p/2-1}\le Cs^{p/2}\) for \(s\le1\). The corrected estimate uses \(s^{p/2}\) and gives an error \(Cp^2r^{-2}J_p\).
3. The computation gives
   \[
   J_p'+cpD_p^E+cp^2Q_p\le \cdots,
   \]
   not
   \[
   J_p'+c'p^2D_p^E\le \cdots.
   \]
   The step from \(Q_p\) to \(D_p^E\) with a \(p^2\) lower coefficient is not valid.

### Proposition 3.3

The gradient computation for \(w_p\) is correct, including
\[
|\nabla s|^2\le4s|\nabla E|^2.
\]
But the estimate necessarily contains a \(p^2\) factor:
\[
P_p\le Cp^2\gamma_t(Q_p+r^{-2}J_p).
\]
The statement without \(p^2\) is incomplete. Because the energy inequality contains \(CpP_p\), absorption requires roughly
\[
\gamma_t\lesssim p^{-1}
\]
or stronger, depending on the dissipation used. This is not uniform as \(p_k\to\infty\). Thus the closed general-\(p\) inequality needed for the full Moser iteration is not established by the two-factor argument alone.

### Proposition 4.1

The mixed Hölder identity and time-cutoff structure are correct. The recurrence is plausible if a closed general-\(p\) energy inequality is available. But it currently inherits the unresolved \(p\)-dependent absorption condition. The treatment of the \(Cp_k^N(1+r^{-2})H_{p_k}\) term also needs either a slab schedule adapted to \(p_k^N\) or an explanation of why the resulting constants remain polynomial/geometric rather than exponential in \(p_k\).

### Proposition 4.2

The product convergence calculation and the sums
\[
\sum_{j\ge1}(2/3)^j=2,
\qquad
\sum_{j\ge1}j(2/3)^j=6
\]
are correct. The endpoint interpretation is not: \(\Lambda_k^{1/p_k}\) controls \(\|aE\|_\infty\), not \(\|aE\|_\infty^2\). Therefore the endpoint should be
\[
\|aE(t)\|_\infty
\le
C\Lambda_0^{1/6}\mathcal S^{1/3}t^{-1/3},
\]
not a squared version of that estimate.

### Volume cancellation and Step 34

With the correct endpoint interpretation, the volume cancellation gives
\[
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]
This agrees with Step 34 and A03’s weighted Moser endpoint. The Step 62 exponent
\[
C\delta^{1/2}(r^2/t)^{1/6}
\]
does not follow from the moment definitions; it is produced by treating the \(p\)-root bound as a squared-norm bound.

---

## 8. What remains mathematically unresolved

The main unresolved substance is not the algebra of the product convergence, but the uniform general-\(p\) energy estimate. To make the Step 62 route complete, one needs a derivation of one of the following:

1. A two-factor absorption of \(P_p\) with constants that do not require \(\gamma_t\lesssim p^{-1}\) or \(p^{-2}\) as \(p\to\infty\).
2. A replacement of the two-factor absorption by a three-factor or integrated-curvature mechanism that remains valid for all Moser levels.
3. A modified Moser scheme that stops at finite \(p\) and obtains the \(L^\infty\) endpoint by another argument.
4. A corrected energy inequality explicitly using
   \[
   pD_p^E+p^2Q_p,
   \]
   together with an absorption argument that respects the distinction between \(D_p^E\) and \(Q_p\).
5. A time-slab schedule or Gronwall treatment that keeps the recurrence constants polynomial/geometric in \(k\), even in the presence of \(p_k^N\) coefficients.

Until one of these is supplied, the general-\(p\) defect Moser endpoint remains conditional. The fixed-exponent \(p=6\) persistence estimate is on much firmer ground, while the full \(p\to\infty\) endpoint requires the additional uniform absorption mechanism described above.