# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Skills/geometric-analysis/research/paper/sections/single_solution_coercivity.tex",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A02/workspace/scripts/paired_cross_field_algebra.py",
    "Sessions/S1003A02/workspace/data/paired_cross_field_algebra.json"
  ]
}
```

## Task

Verify the simultaneous signed-cost/amplitude identity as a proof-level mathematical statement. Check every coefficient and normalization from the single-solution identities through Walsh Parseval, the Weitzenböck formula at s=-4, the clean amplitude completion, and the necessary condition for a sequence with P/(8π^2 k)->c<1. Determine the exact band interpretation using m(rho), including the root near 0.77579, and state which nonnegative terms measure the realized fraction of the deficit bound. Identify any unsupported equation or quantifier. The active goal is a same-metric lower theory for M=X#k CPbar^2 that must permit the certified subunit cell. Read the actual files, not merely this task prose.

## Output

## Scientific verification memo

### 1. Hypotheses and conventions needed for the identity

Consider
\[
M=X\#k\overline{\mathbf{CP}}^{\,2},
\qquad
a_\epsilon=c+\sum_{i=1}^k\epsilon_iE_i,
\qquad \epsilon\in\{\pm1\}^k,
\]
with
\[
c^2=A,\qquad c\cdot E_i=0,\qquad E_i\cdot E_j=-\delta_{ij}.
\]
The simultaneous formula requires that every \(a_\epsilon\) admit an unperturbed ordinary monopole on the same metric. This follows from the chamber-independent monopole-class supply used in the paper when \(b_+(M)\ge2\); the inequality \(b_+\ge2\) alone does not produce these classes.

Normalize the metric by \(s=-4\), and choose for every sign
\[
D_{\mathcal A_\epsilon}\Phi_\epsilon=0,\qquad
F_{\mathcal A_\epsilon}^+=2i\sigma(\Phi_\epsilon).
\]
Set
\[
f_\epsilon=-iF_{\mathcal A_\epsilon},\qquad
\rho_\epsilon=|\Phi_\epsilon|^2,\qquad
K_\epsilon=\int|\nabla_{\mathcal A_\epsilon}\Phi_\epsilon|^2,
\qquad
\zeta_\epsilon=\langle\Phi_\epsilon,\nabla_{\mathcal A_\epsilon}\Phi_\epsilon\rangle.
\]
The normalization
\[
|\sigma(\Phi)|^2=\frac{|\Phi|^4}{8}
\]
gives
\[
f_\epsilon^+=2\sigma(\Phi_\epsilon),\qquad
|f_\epsilon^+|^2=\frac{\rho_\epsilon^2}{2}.
\]

All expectations below are uniform sign averages. In expressions
\(\mathbb E_{\epsilon,\epsilon'}\), the two signs must be independent and uniformly distributed over the entire sign cube.

---

### 2. Single-solution coefficients

For one solution, put
\[
p_\epsilon=(a_{\epsilon,g}^+)^2,\qquad
J_\epsilon=\|f_\epsilon^+-(f_\epsilon^+)_H\|_2^2,
\]
and
\[
D_\epsilon=24V+18W_+-72\pi^2p_\epsilon,\qquad
\Sigma_\epsilon=16V-32\pi^2p_\epsilon.
\]
The source identities are
\[
\frac{D_\epsilon}{18}
=J_\epsilon+2\|\zeta_\epsilon\|_2^2
 +\|W^+-W_{0,\epsilon}\|_2^2
 +\frac12\int C(\rho_\epsilon)(2-\rho_\epsilon)^2,
\]
\[
\Sigma_\epsilon
=16K_\epsilon+4\int(2-\rho_\epsilon)^2+8J_\epsilon,
\]
where
\[
C(t)=t+1-\frac{(t+2)^2}{12},\qquad
b(t)=2C(t)-1=\frac{-t^2+8t+2}{6}.
\]

The harmonic projection identity is
\[
\|f_\epsilon^+\|_2^2=4\pi^2p_\epsilon+J_\epsilon,
\]
hence
\[
\boxed{\int\rho_\epsilon^2=8\pi^2p_\epsilon+2J_\epsilon.}
\]

The required linear combination is
\[
\begin{aligned}
4W_++\frac{4V}{3}-\int\rho_\epsilon^2
&=\frac{2D_\epsilon}{9}-\frac{\Sigma_\epsilon}{4}-2J_\epsilon\\
&=8\|\zeta_\epsilon\|_2^2
 +4\|W^+-W_{0,\epsilon}\|_2^2\\
&\quad+\int b(\rho_\epsilon)(2-\rho_\epsilon)^2-4K_\epsilon.
\end{aligned}
\]
The \(J_\epsilon\)-coefficient vanishes exactly:
\[
4J_\epsilon-2J_\epsilon-2J_\epsilon=0,
\]
and the amplitude coefficient is
\[
2C-1=b.
\]
Thus every coefficient in equation \((\mathrm{webvar:signed\text{-}single\text{-}remainder})\) is correct.

For \(M=X\#k\overline{\mathbf{CP}}^{\,2}\),
\[
a_\epsilon^2=A-k.
\]
Since
\[
\|f_\epsilon^+\|_2^2-\|f_\epsilon^-\|_2^2
=4\pi^2(A-k),
\]
the closed Chern–Weil formula
\[
P=4W_++\frac{4V}{3}-8\pi^2(A-k)
\]
becomes
\[
\boxed{
P
=2\|f_\epsilon^-\|_2^2
 +4W_++\frac{4V}{3}-\int\rho_\epsilon^2.
}
\]
Combining the last two formulas gives the exact one-field identity
\[
\boxed{
\begin{aligned}
P={}&2\|f_\epsilon^-\|_2^2
 +8\|\zeta_\epsilon\|_2^2
 +4\|W^+-W_{0,\epsilon}\|_2^2\\
&+\int b(\rho_\epsilon)(2-\rho_\epsilon)^2-4K_\epsilon.
\end{aligned}}
\]

---

### 3. Weitzenböck normalization at \(s=-4\)

In these conventions the spinor equation implies
\[
4\nabla_{\mathcal A_\epsilon}^*\nabla_{\mathcal A_\epsilon}\Phi_\epsilon
 +(-4+2\rho_\epsilon)\Phi_\epsilon=0.
\]
The pointwise maximum argument gives
\[
0\le \rho_\epsilon\le2.
\]
The upper estimate is a maximum-principle result, rather than a consequence of integration alone.

After integration,
\[
4K_\epsilon-4\int\rho_\epsilon+2\int\rho_\epsilon^2=0,
\]
so
\[
\boxed{
K_\epsilon=\int\rho_\epsilon-\frac12\int\rho_\epsilon^2
=\frac12\int\rho_\epsilon(2-\rho_\epsilon).
}
\]
This also independently verifies the scalar-slack formula:
\[
\begin{aligned}
16K_\epsilon+4\int(2-\rho_\epsilon)^2+8J_\epsilon
&=16V-4\int\rho_\epsilon^2+8J_\epsilon\\
&=16V-32\pi^2p_\epsilon.
\end{aligned}
\]

---

### 4. Walsh Parseval and the \(8\pi^2k\) term

Define
\[
f_I=\mathbb E_\epsilon\!\left[
\left(\prod_{i\in I}\epsilon_i\right)f_\epsilon
\right].
\]
Fourier inversion on \(\{\pm1\}^k\) and the linearity of the Hodge splitting give
\[
\mathbb E_\epsilon\|f_\epsilon^\pm\|_2^2
=\sum_I\|f_I^\pm\|_2^2.
\]
Their cohomology classes are
\[
[f_\varnothing/(2\pi)]=c,\qquad
[f_{\{i\}}/(2\pi)]=E_i,\qquad
[f_I]=0\quad (|I|\ge2).
\]
For a singleton,
\[
\|f_{\{i\}}^+\|_2^2-\|f_{\{i\}}^-\|_2^2
=4\pi^2E_i^2=-4\pi^2,
\]
and for \(|I|\ge2\), the two squared norms agree. Therefore
\[
\boxed{
\mathbb E_\epsilon\|f_\epsilon^-\|_2^2
=4\pi^2k+\|f_\varnothing^-\|_2^2
 +\sum_{I\ne\varnothing}\|f_I^+\|_2^2.
}
\]
Averaging the single-field identity yields
\[
\boxed{
P-8\pi^2k
=\mathscr A-4\mathbb E_\epsilon K_\epsilon,
}
\]
where
\[
\boxed{
\begin{aligned}
\mathscr A={}&
2\|f_\varnothing^-\|_2^2
+2\sum_{I\ne\varnothing}\|f_I^+\|_2^2\\
&+\mathbb E_\epsilon\!\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int b(\rho_\epsilon)(2-\rho_\epsilon)^2
\right].
\end{aligned}}
\]
Since \(b(t)\ge1/3\) on \(0\le t\le2\), every displayed summand is \(\ge0\). This verifies the simultaneous signed-cost formula exactly.

---

### 5. Pairwise Fierz form and clean amplitude completion

For independent signs \(\epsilon,\epsilon'\), write
\[
f_\epsilon^+=\frac{\rho_\epsilon}{\sqrt2}n_\epsilon,
\qquad |n_\epsilon|=1
\]
away from the zero set. The polynomial Fierz formula extends across zeros and gives
\[
|f_\epsilon^+-f_{\epsilon'}^+|^2
=\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
 +2|w_{\epsilon\epsilon'}|^2.
\]
Walsh variance is
\[
\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=\frac12\mathbb E_{\epsilon,\epsilon'}
 \|f_\epsilon^+-f_{\epsilon'}^+\|_2^2.
\]
Consequently,
\[
\boxed{
2\sum_{I\ne\varnothing}\|f_I^+\|_2^2
=\mathbb E_{\epsilon,\epsilon'}\int
\left[
\frac{(\rho_\epsilon-\rho_{\epsilon'})^2}{2}
+2|w_{\epsilon\epsilon'}|^2
\right].
}
\]

Set
\[
L=\mathbb E_\epsilon\int(2-\rho_\epsilon).
\]
Using
\[
4K_\epsilon=2\int\rho_\epsilon(2-\rho_\epsilon),
\]
one finds
\[
4\int(2-\rho_\epsilon)-4K_\epsilon
=2\int(2-\rho_\epsilon)^2.
\]
Hence the exact completed identity is
\[
\boxed{P-8\pi^2k+4L=\mathcal S,}
\]
with
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
+4\|W^+-W_{0,\epsilon}\|_2^2\right.\\
&\hspace{42mm}\left.
+\int (b(\rho_\epsilon)+2)(2-\rho_\epsilon)^2
\right].
\end{aligned}}
\]
Here
\[
b(t)+2=\frac{-t^2+8t+14}{6}\ge\frac73
\qquad(0\le t\le2),
\]
so \(\mathcal S\ge0\). Therefore
\[
\boxed{P\ge8\pi^2k-4L.}
\]

If
\[
\Delta=8\pi^2k-P>0,
\]
then
\[
\boxed{\Delta=4L-\mathcal S.}
\]
Thus the realized fraction of the linear amplitude allowance is
\[
\boxed{
\frac{\Delta}{4L}=1-\frac{\mathcal S}{4L}.
}
\]
The summands of \(\mathcal S\) measure, exactly and additively, the part not converted into curvature-cost deficit:

* \(2\|f_\varnothing^-\|_2^2\): the anti-self-dual cost of the sign centroid;
* pairwise amplitude mismatch \((\rho_\epsilon-\rho_{\epsilon'})^2/2\);
* pairwise spin-direction disagreement \(2|w_{\epsilon\epsilon'}|^2\);
* \(8\|\zeta_\epsilon\|_2^2\): longitudinal spinor variation;
* \(4\|W^+-W_{0,\epsilon}\|_2^2\): Weyl–spinor misalignment;
* \((b+2)(2-\rho)^2\): quadratic amplitude departure.

---

### 6. Consequence for a subunit sequence

Let \(k_j\to\infty\) and suppose
\[
\frac{P(g_j)}{8\pi^2k_j}\longrightarrow c<1.
\]
For every selection of one actual solution for every sign class,
\[
L_j\ge\frac{8\pi^2k_j-P(g_j)}4.
\]
Therefore
\[
\boxed{
\liminf_{j\to\infty}\frac{L_j}{k_j}
\ge2\pi^2(1-c).
}
\]
Since \(2-\rho_\epsilon\le2\), this also gives
\[
\liminf_{j\to\infty}\frac{V(g_j)}{k_j}
\ge\pi^2(1-c).
\]

For the certified cell coefficient
\[
c\approx0.99566273276,
\]
the first necessary amount is only
\[
\frac{L_j}{k_j}\gtrsim
2\pi^2(1-c)\approx0.0856142.
\]
Thus the identity fully permits the certified subunit cell; it does not imply a unit tariff.

---

### 7. Exact amplitude-band interpretation

Eliminate \(K_\epsilon\) directly in the signed-cost formula and define
\[
m(\rho)
=2\rho(2-\rho)-b(\rho)(2-\rho)^2.
\]
Algebra gives
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

The cubic factor has a unique zero in \((0,2)\):
\[
-\rho_*^3+10\rho_*^2-2\rho_*-4=0,
\qquad
\boxed{\rho_*=0.775788981\ldots}.
\]
On the allowed interval,
\[
m(\rho)<0\quad(0\le\rho<\rho_*),\qquad
m(\rho)>0\quad(\rho_*<\rho<2),
\]
with \(m(\rho_*)=m(2)=0\). Therefore
\[
\boxed{
\begin{aligned}
\mathbb E_\epsilon
\int_{\{\rho_*<\rho_\epsilon<2\}}m(\rho_\epsilon)
={}&8\pi^2k-P+\mathcal R_0\\
&+\mathbb E_\epsilon
\int_{\{0\le\rho_\epsilon<\rho_*\}}|m(\rho_\epsilon)|.
\end{aligned}}
\]
This is the exact band statement:

* only amplitudes in \(\rho_*<\rho<2\) can finance \(8\pi^2k-P>0\);
* amplitudes below \(\rho_*\) impose an additional payment;
* pair dispersion, \(\zeta\)-energy, Weyl misalignment, and the centroid term also reduce the realized deficit.

The maximum of \(m\) on \([0,2]\) occurs at
\[
\rho_{\max}=\frac{9-\sqrt{37}}2=1.458618735\ldots,
\]
and equals
\[
\boxed{
m_{\max}=\frac{37\sqrt{37}-221}{4}
=1.015553405\ldots.
}
\]
Thus a subunit sequence also satisfies
\[
\boxed{
\liminf_{j\to\infty}
\frac1{k_j}\,
\mathbb E_\epsilon
\operatorname{Vol}\{\rho_*<\rho_{\epsilon,j}<2\}
\ge
\frac{8\pi^2(1-c)}{m_{\max}}.
}
\]
For the certified cell coefficient, the right side is approximately \(0.3372\) per exceptional unit.

---

### 8. Formulations in the files that need explicit qualification

1. **Pointwise amplitude estimate.**  
   The sentence saying the integrated Weitzenböck identity gives \(0\le\rho\le2\) compresses two arguments. Integration gives the formula for \(K\); the upper estimate \(\rho\le2\) uses the maximum principle.

2. **Meaning of the coefficient four.**  
   The coefficient \(4\) is algebraically optimal for this completion: replacing it by \(C<4\) makes the residual linear term
   \[
   (C-2\rho)(2-\rho)+b(\rho)(2-\rho)^2
   \]
   less than zero for \(\rho\) sufficiently close to \(2\). The supplied files do not exhibit a closed sequence making every other term negligible, so a global best-constant theorem does not follow from this algebra alone.

3. **Pair expectation.**  
   The Walsh–Fierz equation uses independent uniform ordered pairs from the full sign cube. Averaging only over adjacent single-sign flips gives a different Fourier weighting.

4. **Kinetic split at spinor zeros.**  
   The formula
   \[
   |\nabla_A\Phi|^2
   =\frac{|\zeta|^2}{\rho}+\frac{\rho}{4}|\nabla n|^2
   \]
   is pointwise on \(\{\rho>0\}\). At zeros, \(n\) is undefined; an almost-everywhere or limiting interpretation is needed. This formula is not used in the signed-cost or amplitude proof.

5. **Computational artifact.**  
   `paired_cross_field_algebra.py` correctly returns zero symbolic residuals for the Fierz formulas and machine-level agreement for Walsh and kinetic examples. Its random Walsh tests and finite-difference kinetic tests are corroboration, while the finite Fourier and spinor algebra above supply the mathematical proof.

6. **Tube scaling and isolated-cell fields.**  
   The estimates
   \[
   \int|\nabla n|^2=O(A_E),\qquad
   \int|w|^2=O(A_Er^2)
   \]
   are dimensional model estimates in the note. No closed monopole family realizing them is supplied. They do not enter the exact identities. Likewise, the certified metric cell supplies the geometric upper construction, but the files contain no explicit full sign-family monopole profiles on that cell.

Overall, the simultaneous signed-cost identity, its coefficient \(8\pi^2k\), the clean coefficient-four completion, and the \(m(\rho)\)-band formula are algebraically consistent. Their exact content permits the certified subunit construction: a deficit below \(8\pi^2k\) is financed by averaged amplitudes in the band \(0.775788981\ldots<\rho<2\), while the displayed \(\ge0\) terms record how much of the linear amplitude allowance is not realized as curvature-cost deficit.