# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/notes/step29_consolidated_conditional_theorem.md",
    "Sessions/S0910A03/workspace/notes/step29_terminal_density_bridge_lemma.md",
    "Sessions/S0910A03/trace/ttcs/results/step16_ttcs02_sub1_generator.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md"
  ]
}
```

## Task

Adversarially verify and strengthen the proposed common-union first-exit route for varying Ishida–LeBrun manifolds. Use the Step 23/26/A01 Moser files and the Step 29 terminal lemma. Focus on: (i) a quantitatively correct disjoint macro-support selection in collapsed Ricci-lower-bound geometry retaining a fixed total volume fraction; (ii) one common cutoff flow a=Σχ_j² with componentwise H2/H3/J6 and global Q closing noncircularly; (iii) strict center set P versus a larger bounded-curvature plateau containing every chart geodesic; (iv) terminal errors normalized by A or volume for σ/A→0, with positive-weight regularization ε chosen correctly when Q itself need not tend to zero; and (v) eigenline density restricted to the bounded-curvature region and extended by zero. Identify any remaining mathematical obstruction, especially any false use of maximal-function constants, Sobolev domains, or flow existence.

## Output

# Scientific verification memo: common-union first-exit route

## 1. Quantitative macro-support selection

The selection in Step 29 §3.1 is numerically incorrect as written. From a truncated centered maximal inequality on a doubling space,

\[
\mu\{\mathcal M_R f>\Lambda \bar f\}
 \le \frac{C_{\rm M}}{\Lambda}\mu(M),
\qquad
\bar f=\frac1{\mu(M)}\int_M f,
\]

the threshold \(4\bar f\) gives a useful good-set proportion only if \(C_{\rm M}<4\). The sentence using \(C_D\le2\) cannot hold even for Euclidean four-space, whose radius-doubling ratio is \(16\).

A quantitatively valid construction is as follows.

Let

\[
F=(1+|\operatorname{Rm}|^2)^{1/2},
\qquad
\bar K=\fint_M F^2,
\]

and assume \(\operatorname{Ric}\ge-\kappa g\). Fix \(r\) so that doubling is uniform through radius \(30r\), and define

\[
G=\left\{x:\sup_{0<s\le 6r}\fint_{B_s(x)}F^2
       \le \Lambda\bar K\right\},
\qquad
\Lambda=2C_{\rm M}.
\]

Then \(\mu(G)\ge\mu(M)/2\).

Take a maximal \(r\)-separated family \(\{p_\alpha\}\subset G\). The balls
\(B_r(p_\alpha)\) cover \(G\), while \(B_{r/2}(p_\alpha)\) are disjoint. Form the graph whose vertices are the \(p_\alpha\) and whose edges join centers at distance at most \(12r\). Doubling through radius \(25r\) bounds the degree by

\[
N=N(4,\kappa r^2)<\infty.
\]

An \((N+1)\)-coloring exists. Weight a vertex by
\(w_\alpha=\mu(B_r(p_\alpha))\), and take a color with maximal total weight. For that color,

\[
\sum_j\mu(B_r(p_j))
 \ge \frac1{N+1}\sum_\alpha\mu(B_r(p_\alpha))
 \ge \frac{\mu(G)}{N+1}
 \ge \frac{\mu(M)}{2(N+1)}.
\tag{1.1}
\]

The balls \(B_{6r}(p_j)\) are mutually disjoint. Thus one may arrange

\[
\begin{aligned}
&P_j=B_r(p_j),\\
&\chi_j=1 \text{ on }B_{4r}(p_j),\qquad
  \operatorname{supp}\chi_j\Subset B_{5r}(p_j),\\
&\eta_j=1\text{ near }\operatorname{supp}\chi_j,\qquad
  \operatorname{supp}\eta_j\Subset B_{6r}(p_j),
\end{aligned}
\tag{1.2}
\]

with \(|d\chi_j|\le C/r\). Equation (1.1) gives the required fixed total proportion for the strict center set \(P=\bigcup_jP_j\), while the larger balls \(B_{4r}(p_j)\) serve as curvature plateaux.

This construction also repairs a second issue in Step 23. A good center controls the average on the ball \(B_{6r}(p_j)\), not automatically on an arbitrary set \(U_j\subset B_{6r}(p_j)\). Indeed, \(\mu(U_j)\) may be much smaller than \(\mu(B_{6r})\). Taking the Sobolev domain to be the actual ball \(B_{6r}(p_j)\) avoids that problem.

On this ball the quoted relative Sobolev estimate gives

\[
\|u\|_4^2
 \le S_j\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad
S_j\le C_S r^2\mu(B_{6r}(p_j))^{-1/2},
\tag{1.3}
\]

for \(u\) compactly supported in \(B_{6r}(p_j)\). The maximal estimate then yields

\[
S_j\|F\|_{L^2(B_{6r}(p_j))}
 \le C_S\sqrt{\Lambda}\,r^2\sqrt{\bar K}.
\tag{1.4}
\]

Hence the critical product is uniformly small if

\[
r=c\,\bar K^{-1/4}
\]

with \(c\) sufficiently small relative to the constants in the \(q=2\) energy inequality.

## 2. The common cutoff and the fixed-exponent energy layer

Because the macro-balls are disjoint,

\[
a=\sum_j\chi_j^2
\]

equals \(\chi_j^2\) on the \(j\)-th component. Moreover,
\(\chi=\sum_j\chi_j\) is smooth and \(a=\chi^2\). Thus the union flow is genuinely one cutoff flow,

\[
\partial_tg=-2a(\operatorname{Ric}+g),
\tag{2.1}
\]

rather than an interacting system. On each component,

\[
\frac{|da|^2}{a}=4|d\chi_j|^2\le Cr^{-2},
\tag{2.2}
\]

with the continuous value \(0\) on the zero set.

Under provisional metric comparison and Sobolev comparison, the Step 23 fixed-exponent estimates are compatible component by component:

\[
H_{2,j}'+cD_{2,j}
 \le Cr^{-2}H_{2,j}+C H_{3,j},
\tag{2.3}
\]

\[
H_{3,j}'+cD_{3,j}
 \le Cr^{-2}H_{3,j}
    +C\int a^2F^4,
\tag{2.4}
\]

where \(H_{3,j}=\int\eta_j^2aF^3\). The small product in (1.4) absorbs the reaction terms and gives

\[
H_{2,j}(t)\le e^{Ct/r^2}H_{2,j}(0),
\qquad
S_j^2H_{3,j}(t)
 \le \frac{C\gamma_{j,*}^3}{t}.
\tag{2.5}
\]

The active \(H_2\) estimate must be derived directly with all remainders restricted to the set where \(a\), \(da\), or \(|da|^2/a\) is nonzero. Merely subtracting a stationary collar from Step 23 equation (2.7) leaves an artificial additive collar term. The direct active-region calculation removes it.

The fixed \(J_6\) estimate is also compatible with the union construction:

\[
J_{6,j}(t)
 =\int\eta_j^2a^4|E|^6
 \le e^{Ct/r^2}J_{6,j}(0)
 \le C\delta^6\mu(B_{6r}(p_j)).
\tag{2.6}
\]

For the global tensor energy

\[
Q(t)=\int_M|E|^2\,d\mu_t,
\qquad E=\operatorname{Ric}+g,
\]

disjointness is exactly what prevents dependence on the number of components. Componentwise Sobolev absorption in

\[
\int\chi_j^2|\operatorname{Rm}|\,|E|^2
 \le \|\operatorname{Rm}\|_{2,B_{6r}}
       \|\chi_jE\|_4^2
\]

gives, after summing,

\[
Q'(t)\le Cr^{-2}Q(t),
\qquad
Q(t)\le e^{Ct/r^2}Q(0).
\tag{2.7}
\]

No neighbor terms occur, and all stationary regions contribute only their unchanged initial \(E\)-energy.

Thus the \(H_2/H_3/J_6/Q\) layer can coexist in one flow without a factor proportional to the number of selected components.

## 3. The supplied weighted Moser step does not yield the stated endpoint bounds

The central unresolved analytic point is visible directly in Step 26 §5. For

\[
K_p=\int\eta^2a^{p-2}\Phi^p,
\qquad
Z_p=\eta a^{(p-1)/2}\Phi^{p/2},
\]

the four-dimensional parabolic Sobolev step controls

\[
\int Z_p^3
 =\int \eta^3a^{\,3(p-1)/2}\Phi^{3p/2}.
\tag{3.1}
\]

The proposed next energy is

\[
K_{3p/2}
 =\int\eta^2a^{\,3p/2-2}\Phi^{3p/2}.
\tag{3.2}
\]

The exponent difference is

\[
\frac{3(p-1)}2-\left(\frac{3p}{2}-2\right)=\frac12.
\]

Since \(0\le a\le1\),

\[
\int Z_p^3
 \le K_{3p/2},
\tag{3.3}
\]

rather than the upper estimate on \(K_{3p/2}\) needed by the recurrence. Therefore Step 26 equation (5.3), and consequently its displayed bounds

\[
\|aF(t)\|_\infty\le C\bar\beta/t,
\qquad
\|aE(t)\|_\infty
 \le C\delta(r^2/t)^{1/3},
\tag{3.4}
\]

do not follow from the weighted \(K_p\) hierarchy. The correction inserted at the beginning of the A01 Step 27 file identifies the same half-power discrepancy.

The fixed \(p=2,3,6\) estimates above are unaffected. What is absent from the supplied derivations is a complete weak iteration for the actual evolved variables

\[
U=a(\operatorname{Rm}+G),
\qquad
V=aE,
\tag{3.5}
\]

including the exact shifted tensor \(G\), all \(da\) and \(\nabla^2a\) contractions, regularization at \(V=0\), and a recurrence whose next energy is controlled in the correct direction. This missing calculation is also the source of the metric-drift estimate needed by the first-exit argument.

There is a second analytic gap at the flow level. The equation (2.1) is only weakly parabolic where \(a=0\). Smooth short-time existence and extension for the normalized equation require the Wang-type degenerate-flow theorem with the added \(-2ag\) term and the shifted curvature in (3.5). Step 29 records this as Assumption (A4); the supplied files do not contain a complete theorem proof. For an exit time \(T_0>0\), the bound \(C/t\) would be finite on \([T_0/2,T_0]\), while ordinary smoothness controls the earlier interval, so a genuine continuation theorem would fit the first-exit structure.

## 4. Strict centers versus the larger curvature plateau

The center set used in terminal averaging cannot be the entire set where \(\chi_j=1\). Points arbitrarily close to the edge of that set have no uniform radial buffer.

The quantitative selection above gives a clean separation:

\[
P=\bigcup_jB_r^{g(0)}(p_j),
\qquad
L=\bigcup_jB_{4r}^{g(0)}(p_j),
\tag{4.1}
\]

where \(P\) is the center set and \(L\) is the larger plateau. Suppose

\[
e^{-2I}g(0)\le g(T)\le e^{2I}g(0).
\]

For \(p\in P\), a \(g(T)\)-geodesic segment of length \(\rho=c_0r\) remains in \(L\) whenever

\[
r+e^I\rho<4r.
\tag{4.2}
\]

On \(L\), \(a=1\), so a valid endpoint estimate for \(a\operatorname{Rm}\) gives

\[
|\sec_{g(T)}|\le
K\le \frac{C\bar\beta}{\theta r^2}+C,
\qquad T=\theta r^2.
\tag{4.3}
\]

Taking \(c_0\) small enough gives both (4.2) and

\[
K\rho^2<\pi^2/4.
\tag{4.4}
\]

Meanwhile, (1.1) and metric comparison give

\[
\operatorname{Vol}_{g(T)}(P)
 \ge e^{-4I}\frac{\operatorname{Vol}_{g(0)}(M)}
                    {2(N+1)}.
\tag{4.5}
\]

If \(\operatorname{Vol}(M)/A\ge v_0>0\), this is the required
\(\alpha A\) lower bound.

A sequence-uniform physical radius \(\rho\) additionally needs
\(r\ge r_{\min}>0\). From the corrected four-dimensional identity

\[
\int|\operatorname{Rm}|^2
 =32\pi^2\chi(M)+4\int|\operatorname{Ric}_0|^2,
\tag{4.6}
\]

one obtains a uniform upper bound for \(\bar K\) only when
\(\chi(M)/A\) is uniformly bounded and \(\operatorname{Vol}(M)/A\) is uniformly comparable. The condition \(\sigma/A\to0\) by itself does not supply an upper bound for \(\chi(M)/A\). Without it, \(r_i\) and \(\rho_i\) may tend to zero, and the terminal normalized Einstein germ is not obtained on a fixed-radius domain.

The body of Step 29 §6.1 still displays coefficient \(6\) in (4.6), while its correction paragraph states the proper coefficient \(4\).

## 5. Terminal normalization and the positive weight

For varying manifolds the relevant small quantity is

\[
\frac{Q_i}{A_i}\longrightarrow0,
\tag{5.1}
\]

not necessarily \(Q_i\to0\). With \(V_i=\operatorname{Vol}(g_i(T))\) and
\(V_i/A_i\asymp1\), equation (5.1) gives \(Q_i/V_i\to0\).

Let

\[
q_i=\sqrt6|W_i^+|-s_i,
\qquad
u_i=q_i^+,
\qquad
E_i^+=\int u_i^2,
\qquad
I_i=\int u_i.
\]

The choice \(\varepsilon_i=Q_i\) in the Step 16 record is unsuitable when \(Q_i\) grows while \(Q_i/A_i\to0\). A normalized choice that preserves all required estimates is

\[
\boxed{\varepsilon_i=\frac{Q_i}{V_i}}
\tag{5.2}
\]

when \(Q_i>0\). If \(Q_i=0\), the calibrated constant weight is available directly.

For \(f_i^2=u_i+\varepsilon_i\), the exact algebra gives

\[
0\le
L_i^+(f_i)-E_i^+
\le\varepsilon_i^2V_i
=\frac{Q_i^2}{V_i}=o(Q_i).
\tag{5.3}
\]

Also \(I_i\le C V_i\), so

\[
2\varepsilon_i I_i+\varepsilon_i^2V_i
\le C Q_i.
\tag{5.4}
\]

Smooth positive approximants can be selected with functional error at most
\(Q_i/i\) and with value bounded by \(C(K)+1\) on the curvature plateau. No derivative of the approximating weight enters the monopole decomposition. Consequently all harmonic-amplitude estimates remain \(O(Q_i)\), hence become \(o(A_i)\).

The terminal bridge lemma’s displayed conclusion should therefore be normalized as

\[
A_\rho\mathfrak D_i(p_i)
 \le C(K,\rho,\alpha)\frac{Q_i}{A_i},
\tag{5.5}
\]

rather than \(C\varepsilon\) with \(\varepsilon=Q_i/(8\pi^2)\). Its internal averaging calculation already has the correct \(Q_i/A_i\) factor.

For \(\sigma_i/A_i\to0\), the topological identity gives
\(\sigma_i\le R_i\le C Q_i\), so all additional \(\sigma_i\)-terms also vanish after division by \(A_i\).

## 6. Regional eigenline density

The estimate for

\[
\langle\mathscr A_iH_i,H_i\rangle,
\qquad
\mathscr A_i=W_i^+
 +\sqrt{\frac23}|W_i^+|I,
\]

uses a local upper bound for \(f_i^2\) and for \(\mathscr A_i\). It is therefore established only on the bounded-curvature plateau \(L_i\), not on all of \(M_i\).

The correct nonnegative terminal density is

\[
\begin{aligned}
\mathfrak D_i={}&
|E_i|^2+(s_i+4)^2
 +(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i\\
&+\left(|2\pi H_i|-\frac{u_i}{3\sqrt2}\right)^2
 +2\mathbf1_{L_i}\langle\mathscr A_iH_i,H_i\rangle .
\end{aligned}
\tag{6.1}
\]

The regional term is extended by zero outside \(L_i\). Then

\[
\int_{M_i}\mathfrak D_i\le C(K)Q_i.
\tag{6.2}
\]

Every radial geodesic used for a center \(p\in P_i\) remains inside \(L_i\), so the characteristic function in (6.1) equals one throughout the exponential-pullback chart. The averaging lemma therefore selects

\[
A_\rho\mathfrak D_i(p_i)
 \le \frac{C(K,\rho)}{\operatorname{Vol}(P_i)}
       \int_{M_i}\mathfrak D_i
 \le C(K,\rho,\alpha)\frac{Q_i}{A_i}
 \longrightarrow0.
\tag{6.3}
\]

This supplies the full eigenline information on the limit chart without asserting any global curvature bound.

## 7. Mathematical status

The following pieces are quantitatively consistent:

- disjoint macro-supports retaining a fixed total volume proportion, after replacing the threshold \(4\bar K\) by a threshold involving the maximal weak-type constant and using weighted graph coloring;
- one union cutoff \(a=\sum\chi_j^2\), with componentwise \(H_2,H_3,J_6\) and a global \(Q\) estimate independent of the number of components;
- a strict center set \(P\) lying well inside a larger bounded-curvature plateau;
- terminal normalization by \(A_i\), with \(\varepsilon_i=Q_i/V_i\);
- regional eigenline energy extended by zero.

Three substantive mathematical objects remain absent from the supplied files:

1. a correct shifted-variable Moser theorem producing the two bounds in (3.4), since the Step 26 weighted recurrence has the half-power mismatch (3.3);
2. a complete smooth existence and continuation theorem for the normalized degenerate cutoff flow;
3. a sequence-uniform upper bound for \(\chi(M_i)/A_i\), or another mechanism giving \(r_i,\rho_i\ge c>0\), for varying Ishida–LeBrun manifolds beyond the controlled subfamilies.

These are the points on which the common-union route presently depends.