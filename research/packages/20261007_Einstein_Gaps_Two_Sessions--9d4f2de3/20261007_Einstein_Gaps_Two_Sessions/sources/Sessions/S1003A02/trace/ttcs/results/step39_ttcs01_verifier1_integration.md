# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 39,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step39_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step39_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the simultaneous signed-cost/amplitude identity as a proof-level mathematical statement. Check every coefficient and normalization from the single-solution identities through Walsh Parseval, the Weitzenböck formula at s=-4, the clean amplitude completion, and the necessary condition for a sequence with P/(8π^2 k)->c<1. Determine the exact band interpretation using m(rho), including the root near 0.77579, and state which nonnegative terms measure the realized fraction of the deficit bound. Identify any unsupported equation or quantifier. The active goal is a same-metric lower theory for M=X#k CPbar^2 that must permit the certified subunit cell. Read the actual files, not merely this task prose.

## Integrated Scientific Memo

## Verification result

Let
\[
M=X\#k\overline{\mathbf{CP}}^{\,2},\qquad
a_\epsilon=c+\sum_{i=1}^k\epsilon_iE_i,
\]
with \(c^2=A\), \(c\cdot E_i=0\), and \(E_i\cdot E_j=-\delta_{ij}\). Assume, as an actual hypothesis, that every \(a_\epsilon\) is represented by an unperturbed ordinary monopole on the **same** scalar-\(-4\) metric:
\[
D_{\mathcal A_\epsilon}\Phi_\epsilon=0,\qquad
F_{\mathcal A_\epsilon}^+=2i\sigma(\Phi_\epsilon).
\]
The chamber-independent supply in the paper provides this in its stated \(b_+(M)\ge2\) setting; \(b_+\ge2\) by itself is not a theorem producing the classes.

Write
\[
f_\epsilon=-iF_{\mathcal A_\epsilon},\quad
\rho_\epsilon=|\Phi_\epsilon|^2,\quad
K_\epsilon=\int|\nabla_{\mathcal A_\epsilon}\Phi_\epsilon|^2,\quad
\zeta_\epsilon=\langle\Phi_\epsilon,\nabla_{\mathcal A_\epsilon}\Phi_\epsilon\rangle .
\]
With \(|\sigma(\Phi)|^2=|\Phi|^4/8\),
\[
|f_\epsilon^+|^2=\frac{\rho_\epsilon^2}{2}.
\]

All coefficients in the simultaneous signed-cost identity and its amplitude completion check exactly.

---

## 1. Single-solution algebra

For
\[
p_\epsilon=(a_{\epsilon,g}^+)^2,\qquad
J_\epsilon=\|f_\epsilon^+-(f_\epsilon^+)_H\|_2^2,
\]
the supplied identities are
\[
\frac{D_\epsilon}{18}
=J_\epsilon+2\|\zeta_\epsilon\|_2^2
+\|W^+-W_{0,\epsilon}\|_2^2
+\frac12\int C(\rho_\epsilon)(2-\rho_\epsilon)^2,
\]
and
\[
\Sigma_\epsilon
=16K_\epsilon+4\int(2-\rho_\epsilon)^2+8J_\epsilon,
\]
where
\[
C(t)=t+1-\frac{(t+2)^2}{12},\qquad
b(t)=2C(t)-1=\frac{-t^2+8t+2}{6}.
\]
On \(0\le t\le2\),
\[
b(t)\ge b(0)=\frac13.
\]

Harmonic projection gives
\[
\|f_\epsilon^+\|_2^2=4\pi^2p_\epsilon+J_\epsilon,
\qquad
\boxed{\int\rho_\epsilon^2=8\pi^2p_\epsilon+2J_\epsilon.}
\]
Consequently,
\[
4W_++\frac{4V}{3}-\int\rho_\epsilon^2
=\frac{2D_\epsilon}{9}-\frac{\Sigma_\epsilon}{4}-2J_\epsilon.
\]
Substitution yields
\[
\boxed{
\begin{aligned}
4W_++\frac{4V}{3}-\int\rho_\epsilon^2
={}&8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2\\
&+\int b(\rho_\epsilon)(2-\rho_\epsilon)^2-4K_\epsilon .
\end{aligned}}
\]
The \(J_\epsilon\)-coefficient is exactly
\[
4-2-2=0,
\]
and the amplitude coefficient is exactly \(2C-1=b\).

Because \(a_\epsilon^2=A-k\),
\[
\|f_\epsilon^+\|_2^2-\|f_\epsilon^-\|_2^2=4\pi^2(A-k).
\]
For \(\ell=0\), Chern–Weil therefore gives
\[
\boxed{
P
=2\|f_\epsilon^-\|_2^2
+4W_++\frac{4V}{3}-\int\rho_\epsilon^2.
}
\]
For the more general \(X\#k\overline{\mathbf{CP}}^{\,2}\#\ell(S^1\times S^3)\), the right side acquires \(32\pi^2\ell\), exactly as in the paper.

---

## 2. Weitzenböck normalization at \(s=-4\)

In these conventions,
\[
4\nabla_{\mathcal A_\epsilon}^*\nabla_{\mathcal A_\epsilon}\Phi_\epsilon
+(-4+2\rho_\epsilon)\Phi_\epsilon=0.
\]
The maximum principle gives
\[
0\le \rho_\epsilon\le2.
\]
Integration gives
\[
4K_\epsilon-4\int\rho_\epsilon+2\int\rho_\epsilon^2=0,
\]
hence
\[
\boxed{
K_\epsilon=\frac12\int\rho_\epsilon(2-\rho_\epsilon).
}
\]

The distinction matters: the integrated identity gives the formula for \(K_\epsilon\); the pointwise bound \(\rho_\epsilon\le2\) uses the maximum principle.

---

## 3. Walsh–Parseval and the topological tariff

Define
\[
f_I=\mathbb E_\epsilon\!\left[
\left(\prod_{i\in I}\epsilon_i\right)f_\epsilon
\right].
\]
Fourier Parseval on \(\{\pm1\}^k\) gives
\[
\mathbb E_\epsilon\|f_\epsilon^\pm\|_2^2
=\sum_I\|f_I^\pm\|_2^2.
\]
The cohomology classes are
\[
[f_\varnothing/(2\pi)]=c,\qquad
[f_{\{i\}}/(2\pi)]=E_i,\qquad
[f_I]=0\quad (|I|\ge2).
\]
For a singleton,
\[
\|f_{\{i\}}^-\|_2^2-\|f_{\{i\}}^+\|_2^2=4\pi^2,
\]
while for \(|I|\ge2\), the two norms agree. Thus
\[
\boxed{
\mathbb E_\epsilon\|f_\epsilon^-\|_2^2
=4\pi^2k+\|f_\varnothing^-\|_2^2
+\sum_{I\ne\varnothing}\|f_I^+\|_2^2.
}
\]
There is no missing \(2^k\) factor.

Averaging the one-field identity therefore gives, for \(Q=k\),
\[
\boxed{
P-8\pi^2k=\mathscr A-4\mathbb E_\epsilon K_\epsilon,
}
\]
where
\[
\boxed{
\begin{aligned}
\mathscr A={}&2\|f_\varnothing^-\|_2^2
+2\sum_{I\ne\varnothing}\|f_I^+\|_2^2\\
&+\mathbb E_\epsilon\!\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int b(\rho_\epsilon)(2-\rho_\epsilon)^2
\right]\ge0.
\end{aligned}}
\]
For \(\ell>0\), this becomes \(P-8\pi^2Q\) with \(Q=k+4\ell\).

Hence, if
\[
P\le 8\pi^2(1-\delta)Q,
\]
then exactly
\[
\boxed{
\mathbb E K_\epsilon\ge2\pi^2\delta Q+\frac{\mathscr A}{4}.
}
\]

---

## 4. Pairwise form and clean amplitude completion

For independent uniform signs \(\epsilon,\epsilon'\), Fierz and Walsh variance give
\[
\boxed{
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=
\mathbb E_{\epsilon,\epsilon'}\int
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right].
}
\]
The pair average must be over independent ordered pairs from the full sign cube, not merely adjacent sign flips.

Set
\[
L=\mathbb E_\epsilon\int(2-\rho_\epsilon).
\]
Since
\[
4K_\epsilon=2\int\rho_\epsilon(2-\rho_\epsilon),
\]
one has
\[
4\int(2-\rho_\epsilon)-4K_\epsilon
=2\int(2-\rho_\epsilon)^2.
\]
Therefore
\[
\boxed{
P-8\pi^2k+4L=\mathcal S,
}
\]
where
\[
\boxed{
\begin{aligned}
\mathcal S={}&2\|f_\varnothing^-\|_2^2\\
&+\mathbb E_{\epsilon,\epsilon'}\int
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right]\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int (b(\rho_\epsilon)+2)(2-\rho_\epsilon)^2
\right].
\end{aligned}}
\]
Because
\[
b(t)+2=\frac{-t^2+8t+14}{6}\ge\frac73
\quad(0\le t\le2),
\]
all summands are nonnegative. Thus
\[
\boxed{
P\ge8\pi^2k-4\,\mathbb E_\epsilon\int(2-\rho_\epsilon).
}
\]

The coefficient \(4\) is algebraically optimal for a pointwise completion near \(\rho=2\). This does **not** establish a globally attained best constant: that would require a closed sequence for which the other nonnegative terms are negligible.

---

## 5. Which terms measure the realized fraction?

Let
\[
\Delta=8\pi^2k-P.
\]
Then
\[
\boxed{\Delta=4L-\mathcal S.}
\]
Whenever \(L>0\),
\[
\boxed{
\frac{\Delta}{4L}=1-\frac{\mathcal S}{4L}.
}
\]
Thus the following terms measure exactly the fraction of the linear amplitude allowance that is **not** realized as curvature-cost deficit:

1. \(2\|f_\varnothing^-\|_2^2\): anti-self-dual energy of the sign centroid;
2. \(\frac12(\rho_\epsilon-\rho_{\epsilon'})^2\): pairwise amplitude dispersion;
3. \(2|w_{\epsilon\epsilon'}|^2\): pairwise spin-direction disagreement;
4. \(8\|\zeta_\epsilon\|_2^2\): spinor covariant variation;
5. \(4\|W^+-W_{0,\epsilon}\|_2^2\): Weyl–spinor misalignment;
6. \((b(\rho_\epsilon)+2)(2-\rho_\epsilon)^2\): quadratic inefficiency of amplitude depletion.

These are the requested nonnegative “unrealized fraction” terms.

---

## 6. Exact \(m(\rho)\)-band interpretation

Eliminating \(K_\epsilon\) directly from the signed identity gives
\[
m(\rho)=2\rho(2-\rho)-b(\rho)(2-\rho)^2.
\]
Exactly,
\[
\boxed{
m(\rho)
=\frac{(2-\rho)(-\rho^3+10\rho^2-2\rho-4)}6
=\frac{\rho^4-12\rho^3+22\rho^2-8}{6}.
}
\]
Let
\[
\begin{aligned}
\mathcal R_0={}&2\|f_\varnothing^-\|_2^2\\
&+\mathbb E_{\epsilon,\epsilon'}\int
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right]\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
\right].
\end{aligned}
\]
Then
\[
\boxed{
8\pi^2k-P
=\mathbb E_\epsilon\int m(\rho_\epsilon)-\mathcal R_0.
}
\]

The cubic
\[
-\rho^3+10\rho^2-2\rho-4
\]
has a unique root in \((0,2)\),
\[
\boxed{\rho_*=0.775788981\ldots}.
\]
Hence
\[
m(\rho)<0\quad(0\le\rho<\rho_*),\qquad
m(\rho)>0\quad(\rho_*<\rho<2),
\]
and \(m(\rho_*)=m(2)=0\). Therefore
\[
\boxed{
\begin{aligned}
\mathbb E_\epsilon\int_{\{\rho_*<\rho_\epsilon<2\}}m(\rho_\epsilon)
={}&8\pi^2k-P+\mathcal R_0\\
&+\mathbb E_\epsilon
\int_{\{0\le\rho_\epsilon<\rho_*\}}|m(\rho_\epsilon)|.
\end{aligned}}
\]

Thus:

- only the shallow-depletion band
  \[
  \boxed{\rho_*<\rho<2}
  \]
  can finance a positive deficit \(8\pi^2k-P\);
- amplitudes below \(\rho_*\) are not helpful—they impose an additional cost;
- centroid energy, pairwise dispersion, \(\zeta\)-energy, and Weyl misalignment further reduce the realized deficit.

The maximum occurs at
\[
\rho_{\max}=\frac{9-\sqrt{37}}2=1.458618735\ldots,
\]
with
\[
\boxed{
m_{\max}=\frac{37\sqrt{37}-221}{4}
=1.015553405\ldots.
}
\]

---

## 7. Necessary conditions for a subunit sequence

Suppose \(k_j\to\infty\) and
\[
\frac{P(g_j)}{8\pi^2k_j}\longrightarrow c<1.
\]
For every same-metric selection of all sign solutions,
\[
4L_j\ge8\pi^2k_j-P(g_j),
\]
so
\[
\boxed{
\liminf_{j\to\infty}\frac{L_j}{k_j}
\ge2\pi^2(1-c).
}
\]
Equivalently,
\[
\boxed{
\liminf_{j\to\infty}\frac{\mathbb E K_{\epsilon,j}}{k_j}
\ge2\pi^2(1-c)
}
\]
after dropping the additional nonnegative \(\mathscr A/4\) contribution.

The sharper exact band condition is
\[
\boxed{
\mathbb E_\epsilon\int_{\{\rho_*<\rho_{\epsilon,j}<2\}}
m(\rho_{\epsilon,j})
\ge 8\pi^2(1-c)k_j+o(k_j)+\mathcal R_{0,j}.
}
\]
In particular,
\[
\boxed{
\liminf_{j\to\infty}\frac1{k_j}
\mathbb E_\epsilon
\operatorname{Vol}\{\rho_*<\rho_{\epsilon,j}<2\}
\ge
\frac{8\pi^2(1-c)}{m_{\max}}.
}
\]

For the certified cell value
\[
c\approx0.99566273276,
\]
the required averaged linear depletion is only
\[
\frac{L_j}{k_j}\gtrsim 2\pi^2(1-c)\approx0.08561,
\]
and the band-volume lower bound is approximately \(0.337\) per exceptional unit in the \(s=-4\) normalization. Hence the exact identity **permits**, rather than excludes, the certified subunit cell.

No universal unit tariff follows without the missing compensation estimate
\[
4\mathbb E K_\epsilon\le \mathscr A+o(k).
\]

---

## 8. Corrections and unsupported statements

1. **Same-metric quantifier.**  
   The identity is valid for every choice of actual solutions once the full sign family exists on the fixed metric. “Minimal surface of general type” alone does not supply this metric-wise chamber-independent family.

2. **Scalar normalization.**  
   The amplitude identities are statements for the scalar-\(-4\) representative. Since \(\rho\) is not conformally invariant, for a general metric they must be applied after Yamabe replacement.

3. **Coefficient-four sharpness.**  
   It is pointwise/algebraic near \(\rho=2\), not a proved global sharp-constant theorem.

4. **Kinetic split at zeros.**  
   The expression
   \[
   |\nabla_A\Phi|^2=\frac{|\zeta|^2}{\rho}
   +\frac{\rho}{4}|\nabla n|^2
   \]
   is valid on \(\{\rho>0\}\), with only an almost-everywhere or limiting interpretation at spinor zeros. It is not needed for the verified amplitude identity.

5. **Rotation-energy claim.**  
   The source note’s estimates
   \[
   \int|\nabla n|^2=O(A_E),\qquad \int|w|^2=O(A_Er^2)
   \]
   are heuristic tube scalings; no closed same-metric monopole family realizing them is supplied. Moreover, vanishing rotation energy alone cannot account for a fixed per-cell deficit. In the alternative kinetic decomposition, a fixed deficit requires a corresponding nonvanishing weighted spin-direction energy, modulo the \(\zeta\) and other nonnegative costs.

6. **Host topology formulas.**  
   Formulas such as \(\chi(X)=A/3\) or the stated reference Weyl value require the special ball-quotient context and should not be silently applied to a general minimal surface of general type. The simultaneous identity itself only needs the invariant Chern–Weil combination and \(a_\epsilon^2=A-k\).

7. **Computational evidence.**  
   The script correctly verifies the Fierz residuals symbolically and Walsh variance numerically, but the random and finite-difference tests are corroboration, not proof. The Fourier, Chern–Weil, and Weitzenböck derivations above provide the proof-level justification.

The final verified conclusion is therefore:
\[
\boxed{
P-8\pi^2k+4\mathbb E_\epsilon\int(2-\rho_\epsilon)
=\mathcal S\ge0,
}
\]
with the exact nonnegative remainder \(\mathcal S\) displayed above, and equivalently
\[
\boxed{
8\pi^2k-P=\mathbb E_\epsilon\int m(\rho_\epsilon)-\mathcal R_0,
}
\]
where only the band \(0.775788981\ldots<\rho<2\) contributes positively.