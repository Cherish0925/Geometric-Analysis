# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md",
    "Sessions/S0910A03/trace/ttcs/results/step16_ttcs01_verifier2_integration.md"
  ]
}
```

## Task

Develop a rigorous repair for the global positivity/weight issue in the LeBrun rescaled monopole deficit after cutoff smoothing. On a fixed critical Ishida-LeBrun 4-manifold, suppose Q_i=∫|Ric+g|²→0, hence q_i:=sqrt(6)|W_i^+|-s_i satisfies ||q_i-9/2||_2→0 but q_i may be nonpositive on a small set. The Codex exact decomposition assumes a smooth positive weight f and becomes sharp at f=sqrt(q). Seek the strongest valid construction of smooth f_i>0 (e.g. sqrt(q_i^+ + epsilon), truncations, or variational weights) for which L_{f_i}-∫q_i² or the primitive deficit tends to zero, with enough control on bounded-curvature plateau regions to recover harmonic-amplitude and lowest-eigenline densities. Carefully derive how the negative part q_i^- enters, whether derivatives of f occur, and whether only L2 closeness plus bounded volume/curvature suffices. Produce either a proof with quantitative error or a concrete obstruction that identifies extra needed input.

## Output

## Repair theorem: use \(q^+\), not the signed cubic functional

Write, at the evolved metric \(g_i\),
\[
q_i=\sqrt6\,|W_i^+|-s_i,\qquad
r_i=q_i^+=\max\{q_i,0\},\qquad
n_i=q_i^-=\max\{-q_i,0\}.
\]
Let \(a_i\) be the sign monopole class selected for \(g_i\), and put
\[
p_i=(a_i^+)^2,\qquad \beta_i=72\pi^2p_i.
\]
For the critical Ishida–LeBrun manifold, the completion-square and sign-averaging argument gives
\[
0\le \int q_i^2-\beta_i\le C_0Q_i,\qquad
Q_i=\int|\Ric_{g_i}+g_i|^2\longrightarrow0,                 \tag{1}
\]
with \(C_0=27/2\) in the normalization of the supplied notes. Moreover,
\[
\left\|q_i-\frac92\right\|_2^2\le C Q_i.                     \tag{2}
\]

The signed expression involving \(\int q_i^3f^{-2}\) should not be used when \(q_i\) changes sign. The correct Hölder functional is
\[
L_i^+(f)=
\left(\int f^4\right)^{1/3}
\left(\int r_i^3f^{-2}\right)^{2/3},
\qquad f\in C^\infty(M),\quad f>0.                            \tag{3}
\]

### 1. Exact variational value of the corrected functional

For every positive \(f\), Hölder gives
\[
\int r_i^2
=\int (f^4)^{1/3}(r_i^3f^{-2})^{2/3}
\le L_i^+(f).                                                  \tag{4}
\]
Conversely, formally set \(f^2=r_i+\varepsilon\). With
\[
E_i^+=\int r_i^2,\qquad I_i=\int r_i,\qquad V_i=\Vol(g_i),
\]
one has
\[
F_{i,\varepsilon}:=\int(r_i+\varepsilon)^2
=E_i^++2\varepsilon I_i+\varepsilon^2V_i,                     \tag{5}
\]
and polynomial division gives
\[
G_{i,\varepsilon}:=\int\frac{r_i^3}{r_i+\varepsilon}
=E_i^+-\varepsilon I_i+\varepsilon^2V_i
-\varepsilon^3\int\frac1{r_i+\varepsilon}.                    \tag{6}
\]
Weighted arithmetic–geometric mean therefore yields the sharp elementary estimate
\[
\begin{aligned}
E_i^+
&\le F_{i,\varepsilon}^{1/3}G_{i,\varepsilon}^{2/3}\\
&\le \frac13F_{i,\varepsilon}+\frac23G_{i,\varepsilon}\\
&=E_i^++\varepsilon^2V_i
-\frac23\varepsilon^3\int\frac1{r_i+\varepsilon}
\le E_i^++\varepsilon^2V_i.                                   \tag{7}
\end{aligned}
\]

Although \(r_i\) need only be Lipschitz, \(r_i+\varepsilon\) is continuous and strictly positive. Choose smooth positive \(a_{i,\varepsilon,k}\) converging uniformly to \(r_i+\varepsilon\), and set
\[
f_{i,\varepsilon,k}=\sqrt{a_{i,\varepsilon,k}}.
\]
For fixed \(i,\varepsilon\), the lower bound \(a_{i,\varepsilon,k}\ge\varepsilon/2\) for large \(k\) makes both factors in (3) continuous under this approximation. Hence
\[
\inf_{f\in C^\infty,\ f>0}L_i^+(f)=E_i^+.                    \tag{8}
\]

The rescaled monopole inequality applied to every such smooth \(f\) gives
\[
\beta_i\le L_i^+(f).
\]
Taking the infimum in (8),
\[
\boxed{\beta_i\le E_i^+=\int(q_i^+)^2.}                       \tag{9}
\]
Consequently,
\[
0\le \Delta_i^+:=E_i^+-\beta_i
=\left(\int q_i^2-\beta_i\right)-\|q_i^-\|_2^2
\le C_0Q_i,                                                    \tag{10}
\]
and in particular
\[
\|q_i^-\|_2^2\le C_0Q_i.                                      \tag{11}
\]
Thus the contribution from \(\{q_i<0\}\) is automatically part of the total scalar–Weyl deficit.

---

## 2. Exact signed decomposition and the \(q_i^-\) term

Fix one current metric and suppress the index \(i\). Let \(f>0\) be smooth and let \((A,\Phi)\) solve the corresponding rescaled monopole equations. Use
\[
u=|\varphi|,\qquad
Z=\int fu^3,\qquad
C=\int f^2u^2,
\]
and
\[
A_f=\left(\int f^4\right)^{1/3},\qquad
X_f=\left(\int r^3f^{-2}\right)^{1/3}.
\]
The exact spinor–Hodge identity remains
\[
P_f:=\int(qu^2-fu^3)=\frac{27}{8}D_0\ge0.                    \tag{12}
\]
Define
\[
N_f=\int q^-u^2,                                               \tag{13}
\]
\[
H_1^+=X_fZ^{2/3}-\int r u^2\ge0,\qquad
H_2=A_fZ^{2/3}-C\ge0.                                         \tag{14}
\]
Since
\[
\int r u^2=Z+P_f+N_f,
\]
one has
\[
X_fZ^{2/3}-Z=P_f+N_f+H_1^+.                                  \tag{15}
\]
The Hodge projection identity is unchanged:
\[
C=\beta+18J_A,\qquad
J_A=\int|iF_A^+-2\pi H_a|^2.                                  \tag{16}
\]
Therefore
\[
\boxed{
L_f^+-\beta
=18J_A+H_2+
A_f\frac{X_f+Z^{1/3}}{Z^{2/3}}
\bigl(P_f+N_f+H_1^+\bigr).
}                                                               \tag{17}
\]

This is the desired repaired decomposition. The only new term is precisely
\[
N_f=\int q^-u^2.
\]
It enters with the same favorable sign as the spinor, Hodge, and Hölder terms.

No derivative of \(f\) occurs in (12)–(17). In the spinor Weitzenböck formula, \(f\) enters through the algebraic substitution \(F_A^+=f\,\sigma(\Phi)\); the Hodge formula is applied to \(\psi\), not to \(f\psi\). Thus the smooth approximants may have large derivatives without changing any displayed estimate.

---

## 3. Choice of smooth weights along the sequence

On the fixed critical manifold, \(V_i\) and \(E_i^+\) stay uniformly bounded and \(\beta_i\) stays in a compact subinterval of \((0,\infty)\). For \(Q_i>0\), take
\[
\varepsilon_i=Q_i.
\]
Choose a smooth positive \(a_i\) approximating \(r_i+\varepsilon_i\) so accurately that, with \(f_i=\sqrt{a_i}\),
\[
\left|L_i^+(f_i)
-F_{i,\varepsilon_i}^{1/3}G_{i,\varepsilon_i}^{2/3}\right|
=o(Q_i),                                                       \tag{18}
\]
and also
\[
\|a_i-(r_i+\varepsilon_i)\|_2=o(Q_i),                          \tag{19}
\]
together with analogous \(o(Q_i)\) errors in the two defining integrals of \(L_i^+\). This is possible because each \(\varepsilon_i\) is strictly positive and the approximation accuracy can be chosen separately for each \(i\).

By (7), (10), and (18),
\[
\boxed{
0\le d_i:=L_i^+(f_i)-\beta_i\le C Q_i.
}                                                               \tag{20}
\]
Also,
\[
\boxed{
\left|L_i^+(f_i)-\int q_i^2\right|
\le C Q_i.
}                                                               \tag{21}
\]
If \(Q_i=0\), equations (1)–(2) imply \(q_i\equiv9/2\), so the constant weight \(f_i=\sqrt{9/2}\) is already smooth.

More generally, without a uniform volume bound it suffices to choose
\[
\varepsilon_i^2V_i\to0,\qquad
\varepsilon_i\sqrt{V_iE_i^+}\to0.
\]
Thus the fixed-manifold volume control is convenient rather than essential for constructing the weights.

On a buffered region \(U_i\) with \(|\Rm_{g_i}|\le K\), one has \(r_i\le C(K)\). The approximants may be chosen so that
\[
\sup_{U_i}f_i^2\le C(K)+1.                                    \tag{22}
\]
No local lower bound for \(f_i\) is needed below.

---

## 4. Harmonic-amplitude control

Apply (17) to the rescaled monopole associated with \(f_i\). Since the scalar quantities
\[
\int f_i^4,\qquad \int r_i^3f_i^{-2},\qquad \beta_i
\]
all remain in compact subintervals of \((0,\infty)\), and
\[
C_i\le A_iZ_i^{2/3}\le A_iX_i^2=L_i^+(f_i),
\]
the coefficient in the last term of (17) has a uniform positive lower bound. Hence
\[
J_{A_i}\le \frac{d_i}{18},\qquad
D_{0,i}\le C d_i,\qquad
N_{f_i}\le C d_i.                                              \tag{23}
\]

Set \(a_i=f_i^2\) and
\[
M_i=\int f_i^3u_i.
\]
Cauchy–Schwarz gives
\[
C_i^2\le M_iZ_i.                                               \tag{24}
\]
The regularization formulas imply
\[
\int a_i^2=\beta_i+O(Q_i),\qquad
\int r_i^3a_i^{-1}=\beta_i+O(Q_i).                             \tag{25}
\]
Moreover,
\[
C_i=\beta_i+O(Q_i),
\]
while
\[
\left(\frac{C_i}{A_i}\right)^{3/2}\le Z_i
\le\int r_i^3a_i^{-1}.
\]
Thus
\[
Z_i=\beta_i+O(Q_i).                                            \tag{26}
\]
Using (24),
\[
\begin{aligned}
\|f_iu_i-a_i\|_2^2
&=C_i+\int a_i^2-2M_i\\
&\le C_i+\int a_i^2-\frac{2C_i^2}{Z_i}
\le C Q_i.                                                     \tag{27}
\end{aligned}
\]
Together with (19) and \(\varepsilon_i=Q_i\),
\[
\boxed{\|f_iu_i-r_i\|_2^2\le C Q_i.}                           \tag{28}
\]

Since
\[
|iF_{A_i}^+|=\frac{f_iu_i}{3\sqrt2},
\]
and \(2\pi H_i\) is the harmonic projection of \(iF_{A_i}^+\),
\[
\boxed{
\left\||2\pi H_i|-\frac{r_i}{3\sqrt2}\right\|_2^2
\le C Q_i.
}                                                               \tag{29}
\]
Because
\[
\left|r_i-\frac92\right|
\le\left|q_i-\frac92\right|,
\]
equations (2) and (29) recover the calibrated harmonic amplitude:
\[
|H_i|\longrightarrow \frac{3}{4\sqrt2\pi}
\quad\text{in }L^2.                                            \tag{30}
\]

---

## 5. Lowest-eigenline density on a bounded-curvature plateau

Define the positive-semidefinite endomorphism
\[
\mathscr A_i
=W_i^++\sqrt{\frac23}|W_i^+|\,I_{\Lambda^+}.                  \tag{31}
\]
The eigenvalue term in \(D_{0,i}\) gives
\[
2\int\langle\mathscr A_i\psi_i,\psi_i\rangle
\le C Q_i.                                                     \tag{32}
\]
Set
\[
\widetilde H_i
=-\frac{f_i\varphi_i}{6\sqrt2\pi}
=\frac{iF_{A_i}^+}{2\pi}.
\]
Then
\[
\|\widetilde H_i-H_i\|_2^2=\frac{J_{A_i}}{4\pi^2}\le C Q_i,    \tag{33}
\]
and
\[
\langle\mathscr A_i\widetilde H_i,\widetilde H_i\rangle
=\frac{f_i^2}{32\pi^2}
\langle\mathscr A_i\psi_i,\psi_i\rangle.                       \tag{34}
\]
Using (22), (32), and the local bound for \(\mathscr A_i\), one obtains
\[
\boxed{
\int_{U_i}\langle\mathscr A_iH_i,H_i\rangle\le C(K)Q_i.
}                                                               \tag{35}
\]

Thus on the buffered plateau the single density
\[
\boxed{
\mathcal D_i=
|\Ric_{g_i}+g_i|^2
+\left(r_i-\frac92\right)^2
+\left(|2\pi H_i|-\frac{r_i}{3\sqrt2}\right)^2
+2\langle\mathscr A_iH_i,H_i\rangle
}                                                               \tag{36}
\]
is pointwise \(\ge0\) and satisfies
\[
\int_{U_i}\mathcal D_i\longrightarrow0.                        \tag{37}
\]
This is exactly the density needed for exponential-chart averaging.

On a selected chart with smooth metric convergence, harmonic elliptic estimates yield a limit \(H_\infty\), and (36) gives
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0,\qquad
\mathscr A_\infty H_\infty=0.                                 \tag{38}
\]
Together with \(|W_\infty^+|=1/(2\sqrt6)\), this forces
\[
\operatorname{Spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).                  \tag{39}
\]

## 6. Precise analytic content

The weight construction requires only:

1. continuity of \(q_i^+\), automatic for a smooth metric;
2. the global \(L^2\) profile and primitive estimate (1)–(2);
3. a choice of \(\varepsilon_i\) with \(\varepsilon_i^2V_i\to0\);
4. local curvature control solely to obtain the upper bound (22).

No bounds on \(df_i\) are used. Spinor compactness is also unnecessary: all local information is transferred to the harmonic representative \(H_i\), whose equation is independent of \(f_i\).

For a smooth local limit carrying \(W_i^+\) and \(H_i\), sectional-curvature bounds alone do not supply convergence of the curvature tensor. Curvature derivative estimates or equivalent smooth geometric compactness are still required; the cutoff smoothing construction is intended to provide those. This is separate from the weight issue.

Finally, the monopole class, harmonic representative, connection, spinor, and weight must all be reconstructed at the evolved metric. They are not transported by the cutoff flow. The sign class may vary with \(i\); on the fixed manifold the sign family is finite, so a subsequence makes it constant if desired.