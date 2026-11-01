# TTCS Independent Branch Record

```json
{
  "step_id": 46,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step41_corrected_restricted_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step42_uniform_gap_weight_terminal_repairs.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step36_analytic_platform_and_global_Q.md",
    "Sessions/S0910A03/workspace/notes/step39_general_p_defect_power_inequality.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md"
  ]
}
```

## Task

Independently reconstruct the support-selection and simultaneous first-exit portion of the proposed family-uniform negative Ricci-defect gap for the Ishida–LeBrun geography. Work on one exact degenerate normalized cutoff flow obtained by the Step 45 coefficient-regularization limit. Check the quantifiers and all collapse-sensitive constants: maximal-function threshold, weighted coloring and disjoint outer buffers, smooth cutoffs with only a uniform gradient bound, a single global coefficient, matched local Sobolev domains, initial K2 and gamma, moving Sobolev comparison, homogeneous K2-to-Y propagation, fixed J6, all-p defect Moser, integrable metric drift, global unweighted Q, and continuation to T=theta r^2. Identify any load-bearing mathematical failure or domain/weight mismatch; if repairable, give a precise corrected construction and dependency argument rather than merely listing concerns. Distinguish per-datum continuation estimates from sequence-uniform first-exit estimates.

## Output

# Scientific verification memo: support selection and simultaneous first exit

## 1. Quantifier order and geometric input

Consider a contradiction sequence \((M_i,g_i)\) in the Ishida–LeBrun \(q_i\ge 0\) geography with
\[
\delta_i:=\|g_i^{-1}(\operatorname{Ric}_{g_i}+g_i)\|_{\infty,\mathrm{op}}\to0.
\]
After discarding finitely many indices, the calibration and topology formulas in the supplied notes give constants \(v_-,v_+,L>0\), independent of \(i,A_i,N_i\), such that
\[
\operatorname{Ric}_{g_i}\ge-2g_i,\qquad
v_-A_i\le \operatorname{Vol}_{g_i}(M_i)\le v_+A_i,
\qquad
\int_{M_i}(1+|\operatorname{Rm}_{g_i}|^2)\,d\mu_{g_i}\le LA_i.
\tag{1.1}
\]
The last estimate requires \(q_i/A_i\to0\) before support selection. Indeed, once \(q_i\le A_i\), the topology of \(N_i\) and the standard general-type surface inequalities give \(\chi(M_i)\le C A_i\); four-dimensional Chern–Weil then gives the curvature-energy part of (1.1).

The collapse-sensitive parameters must be chosen in this order:

1. a small analytic absorption number \(\gamma_{\rm abs}\);
2. a maximal-function number \(\kappa>0\), with \(C\kappa<\gamma_{\rm abs}\);
3. a radius \(r>0\), chosen after \(\kappa\);
4. a coloring number \(N_{\rm col}\), determined by dimension and fixed radius ratios;
5. a small time factor \(\theta>0\);
6. a metric-distortion allowance \(d_0>0\);
7. a defect size \(\delta_*>0\) that makes the integrated drift smaller than \(d_0/2\).

This order matters because the discarded-volume estimate is proportional to \(r^4/\kappa^2\): taking \(\kappa\) smaller requires taking \(r\) still smaller.

---

## 2. Corrected support construction

Write
\[
F_{i,0}=(1+|\operatorname{Rm}_{g_i}|^2)^{1/2}.
\]
Fix \(R_0\le1\), and define the truncated centered maximal function
\[
\mathcal M_{R_0}f(x)=\sup_{0<s\le R_0}\fint_{B_s^{g_i}(x)}f.
\]
Under \(\operatorname{Ric}\ge-2g\), local doubling and the standard covering argument give
\[
\operatorname{Vol}\{\mathcal M_{R_0}f>\lambda\}
\le \frac{C_M(4,R_0)}{\lambda}\int f.
\tag{2.1}
\]

Set
\[
\lambda=\frac{\kappa^2}{r^4},\qquad
\mathcal G_i=\left\{x:\mathcal M_{R_0}(F_{i,0}^2)(x)\le\frac{\kappa^2}{r^4}\right\}.
\]
Choose \(r\) with \(8r<R_0\), \(r^4\le\kappa^2\), and
\[
C_M L\,\frac{r^4}{\kappa^2}\le \frac{v_-}{2}.
\tag{2.2}
\]
Then
\[
\operatorname{Vol}(\mathcal G_i)\ge \frac{v_-}{2}A_i.
\tag{2.3}
\]

### Weighted coloring

Take a maximal \(r\)-separated set \(\{x_\beta\}\subset\mathcal G_i\). Then
\[
\mathcal G_i\subset\bigcup_\beta B_r(x_\beta).
\]
Color the centers so that centers in the same color have distance at least \(18r\). The number of colors is uniformly bounded. To see this, centers adjacent to a fixed center lie in \(B_{18r}\), while the \(B_{r/2}\) around them are disjoint. Bishop–Gromov comparison, applied at each neighboring center, compares each such \(B_{r/2}\) with one common \(B_{37r}\), giving a uniform degree bound and hence
\[
N_{\rm col}=N_{\rm col}(4,r_0)<\infty.
\]

The color must be selected by volume weights
\[
w_\beta=\operatorname{Vol}_{g_i}B_r(x_\beta),
\]
not by the number of centers. Since
\[
\sum_\beta w_\beta\ge\operatorname{Vol}(\mathcal G_i),
\]
some color \(\mathcal A_i\) satisfies
\[
\sum_{\alpha\in\mathcal A_i}\operatorname{Vol}B_r(x_\alpha)
\ge \frac{v_-}{2N_{\rm col}}A_i.
\tag{2.4}
\]
Within this color the \(B_{8r}(x_\alpha)\) are pairwise disjoint. Thus
\[
P_i:=\bigcup_{\alpha\in\mathcal A_i}B_r(x_\alpha)
\quad\text{satisfies}\quad
\operatorname{Vol}(P_i)\ge \alpha_0A_i,
\qquad
\alpha_0=\frac{v_-}{2N_{\rm col}}.
\tag{2.5}
\]

### Nested cutoffs and one coefficient

Using the initial metric, choose smooth functions
\[
\chi_\alpha=1\ \text{on }B_{4r}(x_\alpha),\qquad
\operatorname{supp}\chi_\alpha\Subset B_{5r}(x_\alpha),
\]
and
\[
\eta_\alpha=1\ \text{on }B_{6r}(x_\alpha),\qquad
\operatorname{supp}\eta_\alpha\Subset B_{7r}(x_\alpha),
\]
with
\[
|d\chi_\alpha|_{g_i}+|d\eta_\alpha|_{g_i}\le \frac{C}{r}.
\tag{2.6}
\]
Smooth approximation of distance functions with unused radial margins gives these functions. Their higher covariant derivatives are finite for each datum but need not admit an \(i\)-independent estimate.

Put
\[
\Omega_{\alpha,i}=B_{8r}^{g_i}(x_\alpha),\qquad
a_i=\sum_{\alpha\in\mathcal A_i}\chi_\alpha^2.
\tag{2.7}
\]
Because the \(\Omega_{\alpha,i}\) are disjoint,
\[
0\le a_i\le1,
\]
and on \(\Omega_{\alpha,i}\),
\[
a_i=\chi_\alpha^2.
\]
Moreover \(a_i=da_i=0\) on \(\operatorname{supp}d\eta_\alpha\). This simultaneously matches the localized energy identities, the Sobolev domains, and the later global \(Q\) summation.

---

## 3. Initial Sobolev and energy normalization

Let
\[
V_{\alpha,i}=\operatorname{Vol}_{g_i}(\Omega_{\alpha,i}).
\]
The relative Sobolev inequality under \(\operatorname{Ric}\ge-2g\) gives, for functions compactly supported in \(B_{7r}(x_\alpha)\),
\[
\|u\|_4^2
\le \mathcal S_{\alpha,i}(0)
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\qquad
\mathcal S_{\alpha,i}(0)\le C_S\frac{r^2}{\sqrt{V_{\alpha,i}}}.
\tag{3.1}
\]

Since \(x_\alpha\in\mathcal G_i\) and \(8r<R_0\),
\[
\fint_{\Omega_{\alpha,i}}F_{i,0}^2
\le\frac{\kappa^2}{r^4}.
\tag{3.2}
\]
No volume-ratio correction is needed here. Hence
\[
K_{\alpha}(0):=\int\eta_\alpha^2F_{i,0}^2
\le\frac{\kappa^2}{r^4}V_{\alpha,i},
\tag{3.3}
\]
and the collapse-sensitive absorption product obeys
\[
\gamma_\alpha(0)
:=\mathcal S_{\alpha,i}(0)K_\alpha(0)^{1/2}
\le C_SC\,\kappa.
\tag{3.4}
\]
The volume cancels exactly.

The sentence in Step 41 proposing to shrink \(r\) until
\(\int_{B_{7r}}|\operatorname{Rm}|^2\le\gamma_0^2\) is not valid in dimension four: as \(r\to0\),
\[
\frac{V_{-2}(7r)}{r^4}\longrightarrow \omega_4\,7^4,
\]
so shrinking \(r\) does not make that coefficient tend to zero. The analytic module does not need such an unnormalized estimate; (3.4) is the correct small quantity.

For \(E_i(0)=\operatorname{Ric}_{g_i}+g_i\), the operator-norm hypothesis implies \(|E_i(0)|\le C_4\delta_i\). Therefore
\[
J_{6,\alpha}(0)
:=\int\eta_\alpha^2a_i^4|E_i(0)|^6
\le C\delta_i^6V_{\alpha,i},
\tag{3.5}
\]
and
\[
Q_i(0):=\int_{M_i}|E_i(0)|^2
\le C\delta_i^2\operatorname{Vol}(M_i),
\qquad
\frac{Q_i(0)}{A_i}\to0.
\tag{3.6}
\]

---

## 4. Exact flow and first-exit interval

For each datum, select one smooth regularization-limit solution of
\[
\partial_tg=-2a_i(\operatorname{Ric}_g+g),\qquad g(0)=g_i.
\tag{4.1}
\]
The coefficient \(a_i\) is one fixed global scalar function. The transported coefficient occurs only in the hatted DeTurck construction; after pullback, (4.1) is the exact geometric equation.

Define the accumulated metric drift
\[
\mathfrak d(t)=\int_0^t\|a_iE(s)\|_{\infty,\mathrm{op}}\,ds.
\tag{4.2}
\]
Then
\[
e^{-2\mathfrak d(t)}g_i\le g(t)\le e^{2\mathfrak d(t)}g_i.
\tag{4.3}
\]
Consequently the initial fixed domains and functions remain usable:
\[
\mathcal S_{\alpha,i}(t)
\le e^{C\mathfrak d(t)}\mathcal S_{\alpha,i}(0),
\qquad
|d\chi_\alpha|_{g(t)}+|d\eta_\alpha|_{g(t)}
\le e^{\mathfrak d(t)}\frac Cr.
\tag{4.4}
\]
No evolving geodesic balls are needed in the energy argument.

Let \(\sigma_i\) be the supremum of times \(t\le\theta r^2\) on the chosen smooth branch for which
\[
K_\alpha(s)\le2K_\alpha(0)\quad\text{for every }\alpha,
\qquad
\mathfrak d(s)\le d_0
\tag{4.5}
\]
for \(0\le s\le t\). On this interval,
\[
\mathcal S_\alpha(t)K_\alpha(t)^{1/2}
\le e^{Cd_0}\sqrt2\,C\kappa.
\tag{4.6}
\]
Choosing \(\kappa\) at the beginning makes this smaller than every absorption threshold occurring below.

---

## 5. Homogeneous \(K_2\to Y\) propagation

Set
\[
D_{2,\alpha}=\int\eta_\alpha^2a_i|\nabla\operatorname{Rm}|^2,
\qquad
Y_\alpha=\int\eta_\alpha^2a_iF^3.
\]
The tensor energy identity gives
\[
K_\alpha'+cD_{2,\alpha}
\le CY_\alpha+C(1+r^{-2})K_\alpha.
\tag{5.1}
\]
Because \(a_i=\chi_\alpha^2\) on \(\Omega_\alpha\),
\[
Y_\alpha
=\int(\eta_\alpha F)(\chi_\alpha F)^2
\le K_\alpha^{1/2}\|\chi_\alpha F\|_4^2.
\]
Using (3.1)–(4.4),
\[
Y_\alpha
\le C\gamma_\alpha(t)
\left(D_{2,\alpha}+r^{-2}K_\alpha\right).
\tag{5.2}
\]
After absorption,
\[
K_\alpha'\le C(1+r^{-2})K_\alpha.
\tag{5.3}
\]
Choose \(\theta\) so that, for \(r\le1\),
\[
e^{C(1+r^{-2})\theta r^2}
=e^{C\theta(1+r^2)}\le\frac32.
\tag{5.4}
\]
Then
\[
K_\alpha(t)\le\frac32K_\alpha(0),
\tag{5.5}
\]
which improves the first condition in (4.5).

Integrating the dissipative form gives
\[
\int_0^tY_\alpha(s)\,ds
\le C\gamma_\alpha(0)K_\alpha(0).
\tag{5.6}
\]
The \(p=3\) curvature inequality,
\[
Y_\alpha'
\le C(1+r^{-2}+\mathcal S_\alpha^2Y_\alpha)Y_\alpha,
\tag{5.7}
\]
combined with (5.6), yields
\[
\int_0^t\mathcal S_\alpha^2Y_\alpha
\le C\gamma_\alpha(0)^3.
\tag{5.8}
\]
A slice \(\tau\in[t/4,t/2]\), followed by Grönwall from \(\tau\) to \(t\), gives
\[
Y_\alpha(t)\le
\frac{C\gamma_\alpha(0)K_\alpha(0)}{t},
\qquad
\mathcal S_\alpha(t)^2Y_\alpha(t)
\le\frac{C\gamma_\alpha(0)^3}{t}.
\tag{5.9}
\]

The all-\(p\) curvature iteration on the same \(\Omega_\alpha\), with weights
\[
K_{p,\alpha}=\int\eta_\alpha^2a_i^{p-2}F^p,
\]
therefore gives
\[
\|a_iF(t)\|_{L^\infty(\Omega_\alpha)}
\le\frac{C\gamma_\alpha(0)}{t}.
\tag{5.10}
\]
All \(d\eta_\alpha\) terms vanish because \(a_i=da_i=0\) where \(d\eta_\alpha\ne0\).

---

## 6. Fixed \(J_6\), the defect ladder, and metric drift

The fixed-exponent signed-Hessian calculation gives
\[
J_{6,\alpha}'\le C(1+r^{-2})J_{6,\alpha},
\tag{6.1}
\]
after the same small-\(\gamma_\alpha\) absorption. Thus
\[
J_{6,\alpha}(t)\le C\delta_i^6V_{\alpha,i}.
\tag{6.2}
\]

For every real \(p\ge6\), use
\[
H_{p,\alpha}=\int\eta_\alpha^2a_i^{p-2}|E|^p,
\qquad
z_{p,\alpha}
=\eta_\alpha a_i^{(p-1)/2}|E|^{p/2}.
\]
The homogeneous all-\(p\) defect inequality is
\[
H_{p,\alpha}'
+c\|\nabla z_{p,\alpha}\|_2^2
\le Cp^4\left(1+r^{-2}+\mathcal S_\alpha^2Y_\alpha\right)H_{p,\alpha}.
\tag{6.3}
\]
The weights are matched exactly: \(H_{6,\alpha}=J_{6,\alpha}\), and every Sobolev variable is supported where the fixed-domain inequality (3.1) applies.

Using (5.9) in the nested-time iteration starting at \(p=6\),
\[
\|a_iE(t)\|_{L^\infty(\Omega_\alpha)}
\le C\mathcal S_\alpha(0)^{1/3}t^{-1/2}
\left(t\delta_i^6V_{\alpha,i}\right)^{1/6}.
\]
The collapse factors cancel:
\[
\boxed{
\|a_iE(t)\|_{L^\infty(\Omega_\alpha)}
\le C\delta_i\left(\frac{r^2}{t}\right)^{1/3}.
}
\tag{6.4}
\]
Since the active domains are disjoint, the global norm is the maximum of these local norms. Hence
\[
\mathfrak d(\theta r^2)
\le C\delta_i r^{2/3}(\theta r^2)^{2/3}
=C\delta_i\theta^{2/3}r^2.
\tag{6.5}
\]
For all sufficiently large \(i\), this is at most \(d_0/2\), improving the second condition in (4.5). Equation (4.4) then supplies the moving Sobolev comparison used throughout.

---

## 7. Global unweighted \(Q\)

Let
\[
Q(t)=\int_M|E|^2,\qquad
X(t)=\int_Ma_i|\nabla E|^2.
\]
The global signed-Hessian calculation gives
\[
Q'+cX
\le C(1+r^{-2})Q
+C\sum_\alpha\int_{\Omega_\alpha}F(\chi_\alpha E)^2.
\tag{7.1}
\]
For each support,
\[
\begin{aligned}
\int F(\chi_\alpha E)^2
&\le K_\alpha^{1/2}\|\chi_\alpha E\|_4^2\\
&\le C\gamma_\alpha(t)
\left(
\int_{\Omega_\alpha}a_i|\nabla E|^2
+r^{-2}\int_{\Omega_\alpha}|E|^2
\right).
\end{aligned}
\tag{7.2}
\]
The gradient term is absorbed. Because the \(\Omega_\alpha\) are disjoint,
\[
\sum_\alpha\int_{\Omega_\alpha}|E|^2\le Q.
\]
Therefore
\[
Q(t)\le e^{C(1+r^{-2})t}Q(0),
\qquad
\frac{Q(\theta r^2)}{A_i}\to0.
\tag{7.3}
\]
Disjointness of the auxiliary Sobolev domains, rather than only disjointness of the active \(B_{5r}\), makes this summation exact and prevents a hidden overlap multiplier.

---

## 8. Continuation to \(T=\theta r^2\)

Suppose the selected smooth branch ended at some \(\sigma_i<\theta r^2\) while (4.5) held. On every interval \([\tau,\sigma_i)\), \(\tau>0\), (5.10) gives
\[
\left|a_i\left(\operatorname{Rm}+\frac{g\owedge g}{6}\right)\right|
\le C\left(1+\frac{\kappa}{\tau}\right).
\tag{8.1}
\]
Equation (6.5) gives finite bilipschitz comparison.

The Step 45 staggered estimates then operate per datum:
\[
T_0\longrightarrow(U_1,C_2)\longrightarrow T_1
\longrightarrow(U_2,C_3)\longrightarrow\cdots ,
\]
where \(T=\operatorname{Rm}+G\), \(U=a_iT\), and \(C_m=\nabla^m\chi\). Their constants may depend on \(\tau\), the full smooth geometry of \(g(\tau)\), all cutoff jets, and unweighted \(L^p\) norms of \(T\). These constants need only be finite for this single datum. The zero-order unweighted \(T\) estimate supplies the induction seed.

The resulting fixed-coordinate spatial and time-derivative bounds give a smooth metric at \(t=\sigma_i\). Applying the same coefficient-regularization construction to that metric produces a restart. Uniqueness of different regularization subsequences is not needed for this existential concatenation; the geometric equation determines matching time jets at the joining time.

Thus a smooth endpoint cannot occur before \(\theta r^2\). Together with the strict improvements (5.5) and (6.5), continuity gives
\[
\sigma_i=\theta r^2.
\tag{8.2}
\]

These continuation constants are per datum. In contrast, the estimates (2.5), (3.4), (5.5), (5.9), (5.10), (6.2), (6.4), (6.5), and (7.3) are uniform along the sequence.

---

## 9. Main mathematical findings

The proposed first-exit mechanism is coherent after four concrete repairs:

1. **Weighted coloring:** the selected color is chosen using \(\operatorname{Vol}B_r(x_\alpha)\), not center count.
2. **Disjoint auxiliary domains:** the coloring separates \(B_{8r}\), not merely the active supports; this aligns Sobolev, \(K_2\), Moser, and global \(Q\).
3. **Normalized collapse-sensitive seed:** the required small quantity is
   \(\mathcal S_\alpha K_\alpha^{1/2}\), not an unnormalized four-dimensional curvature integral.
4. **Fixed-domain Sobolev transport:** all local inequalities remain on the initial \(\Omega_\alpha\); bilipschitz metric drift transfers their constants.

With those changes, no further collapse-induced domain or weight mismatch appears in the simultaneous \(K_2\), \(Y\), \(J_6\), all-\(p\) defect, drift, \(Q\), and continuation chain. The construction relies essentially on the supplied signed-Hessian tensor inequalities and the Step 45 per-datum staggered extension argument.