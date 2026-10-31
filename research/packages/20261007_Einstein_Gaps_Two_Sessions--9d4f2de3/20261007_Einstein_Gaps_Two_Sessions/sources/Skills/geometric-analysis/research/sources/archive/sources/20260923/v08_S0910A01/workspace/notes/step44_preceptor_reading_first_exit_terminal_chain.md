# Step 44: Preceptor reading of the first-exit, support, and terminal chain

Session: S0910A01. Agent4 / Preceptor. Phase: Execute.

## 0. Reading outcome

The coefficient-weight repair from A01 Step 43 and A03 Step 45 is a real advance.  The restricted four-dimensional negative Ishida--LeBrun route can now be organized as one coherent proof on a single exact degenerate cutoff flow
\[
\partial_t g=-2a(\operatorname{Ric}_g+g),\qquad a=\sum_\alpha \chi_\alpha^2.
\]
The result supported by the accumulated work is not Yau Problem 26.  It is the family-uniform negative gap inside the Ishida--LeBrun geography
\[
M=(\#_{j=1}^m X_j)\# N,
\quad m\in\{2,3\},\quad b_+(N)=0,
\quad q=4m-(2\chi+3\tau)(N)-A/3\ge0,
\]
where \(A=\sum_j c_1^2(X_j)\), assuming the Ishida--LeBrun monopole sign family.  The proposed conclusion is a constant \(\varepsilon_{\rm IL}>0\), independent of \(A,D,q,N\) and the input metric, excluding
\[
\|g^{-1}(\operatorname{Ric}_g+g)\|_{\infty,\mathrm{op}}<\varepsilon_{\rm IL}
\]
on those no-Einstein manifolds.

The chain is sound after specific repairs to the local notes.  The repairs are mathematical, not cosmetic:

- A01 Step 43 §6 must be replaced by A03 Step 45's coupled same-exponent estimate for the current pair \((U_m,C_{m+1})\).  The cutoff jet \(C_{m+1}\) is not available from a previous layer when estimating \(U_m\).
- Coefficient regularization is only the construction of an exact \(a=\chi^2\) flow.  Frozen complement, stationary collars, disjoint-support summation, and global \(Q\) propagation begin after taking the \(\varepsilon\to0\) limit.
- The support note needs strict buffers for \(\chi\) and the auxiliary \(\eta\), and the curvature-energy threshold must be stated directly from the volume-average maximal function.
- Terminal recalibration must use the corrected deficit identity and a nonnegative density containing \(|E|^2\).  Without \(|E|^2\) the terminal harmonic-coordinate Einstein limit is not obtained.

The following sections record the corrected proof flow and the exact changes needed in the session notes.

---

## 1. Flow construction by coefficient regularization

For one fixed smooth input \((M,g_0,\chi)\), set
\[
b_\varepsilon=\chi^2+\varepsilon^2,\qquad
T=\operatorname{Rm}+{g\owedge g\over 2(n-1)},\qquad U=b_\varepsilon T.
\]
For each \(\varepsilon>0\), solve the transported-coefficient DeTurck system with
\[
\widehat b_\varepsilon=b_\varepsilon\circ\varphi_t^{-1}
\]
so that the pullback metric satisfies the geometric equation
\[
\partial_tg_\varepsilon=-2b_\varepsilon(\operatorname{Ric}_{g_\varepsilon}+g_\varepsilon).
\]
The fixed-\(\varepsilon\) construction may have constants depending on \(\varepsilon^{-1}\); the common positive time is obtained instead from A03 Step 45's geometric finite-\(L^p\) energies, the first-exit improvement, and fixed-background connection-difference bounds.  The constants in that argument use
\[
0<b_\varepsilon\le2,
\qquad \nabla^r b_\varepsilon=\nabla^r(\chi^2)\ (r\ge1),
\qquad {|\nabla b_\varepsilon|^2\over b_\varepsilon}\le4|d\chi|^2,
\qquad {\chi^2\over b_\varepsilon}\le1,
\]
and no derivative of \(b_\varepsilon^{-1}\).  Thus a subsequence converges smoothly, in fixed background coordinates, to a positive definite metric solving
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]

This order matters.  For \(\varepsilon>0\), the complement of \(\operatorname{supp}\chi\) evolves by \(-2\varepsilon^2(\operatorname{Ric}+g)\).  Therefore the identities using \(a=0\) outside the selected supports are valid only for the exact limiting flow.  Once the exact flow has been obtained, the complement is stationary and the supportwise estimates can be summed without exterior terms.

Uniqueness of the degenerate geometric flow is not needed for this route.  The proof uses the existence of at least one smooth exact flow and the fact that a smooth positive terminal metric can be restarted by the same construction.  Smooth gluing follows from the autonomous equation: all time jets at the terminal slice are determined by the terminal metric and \(\chi\).

This replaces the broad Step 43 assertion that an arbitrary zeroth-order smooth-tame perturbation preserves a smooth tame inverse.  Yang's theorem remains valuable source background, but the coefficient-regularized geometric construction is the reliable interface used here.

---

## 2. Weighted extension: the current pair is \((U_m,C_{m+1})\)

A03 Step 45 is the operative proof of the weighted extension mechanism.  In coordinate time, with \(B_r=\nabla^r b\), the differentiated \((B_1B_1)T\) family must be retained as
\[
B_{r+1}*B_{s+1}*T_t,
\qquad r+s+t=m,
\]
before expanding \(B=\nabla b\).  This preserves the two \(\chi\) factors.  The current \(T_m\) allocation is
\[
B_1*B_1*T_m
=4\chi^2(C_1*C_1)*T_m
=4{\chi^2\over b}(C_1*C_1)*\left[U_m-\sum_{q=1}^mB_q*T_{m-q}\right],
\]
so its current coefficient is bounded independently of \(\varepsilon\).  The current cutoff allocation is
\[
B_{m+1}*B_1*T_0
=4{\chi^2\over b}C_{m+1}*C_1*U_0+\text{lower}.
\]
This is the repair that removes any need for pointwise control of \(T_0\) near \(\chi=0\).

Let
\[
V=U_m,
\qquad Z=C_{m+1}=\nabla^{m+1}\chi.
\]
The cutoff-jet equation has current term \(U_m*C_1\), hence \(Z\) is a current unknown, not a previous-layer object.  The top cutoff source in the \(U_m\) equation has the form
\[
\chi C_{m+2}*U_0*P(V),
\qquad P(V)=|V|^{p-2}V,
\]
including both sources in the parabolic form: the Hessian coefficient term and the extracted \(-\Delta b\) term.  After one integration by parts,
\[
\chi C_{m+2}*U_0*P(V)
\leadsto
C_1*Z*U_0*P(V)
+\chi Z*U_1*P(V)
+\chi Z*U_0*\nabla P(V).
\]
The gradient term is controlled by
\[
\left|\int \chi ZU_0|V|^{p-2}\nabla V\right|
\le \eta\int b|\nabla V|^2|V|^{p-2}
+C_{\eta,p}K^2\int |Z|^2|V|^{p-2}.
\]
The residual closes at the same exponent:
\[
\int |Z|^2|V|^{p-2}
\le {2\over p}\|Z\|_p^p+{p-2\over p}\|V\|_p^p.
\]
Together with the \(Z\)-equation, this yields
\[
{d\over dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+c_{m,p}\int b|\nabla U_m|^2|U_m|^{p-2}
\le C_{m,p}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).
\]
Only after this pair is complete may one estimate \(T_m\).  The order is
\[
T_0\longrightarrow (U_1,C_2)\longrightarrow T_1
\longrightarrow (U_2,C_3)\longrightarrow T_2\longrightarrow\cdots .
\]

The A01 Step 43 sentence using \(C_{m+1}\in L^{2p}\) from a previous layer is mathematically wrong for the \(U_m\) stage.  Higher exponents of \(C_{m+1}\) become available only after the same current pair has been propagated; they can be used later in the \(T_m\) stage.

The Step 45 ledger also needs the already identified formula repairs: \(\partial_tG=-(S\owedge g+g\owedge S)/(n-1)\), current rows include \(bT_m\) and \(bU_m\), and spatial commutator zero-order curvature is treated as \(b\operatorname{Rm}=U-bG\).  These terms do not alter the extension mechanism.

---

## 3. Support construction and the first-exit flow

The support construction should be written with strict buffers.  A clean version is:
\[
\chi_
\alpha=1\text{ on }B_{5r}(x_\alpha),
\qquad \operatorname{supp}\chi_\alpha\subset B_{6r}(x_\alpha),
\]
\[
\eta_\alpha=1\text{ on }B_{6r}(x_\alpha),
\qquad \operatorname{supp}\eta_\alpha\subset B_{7r}(x_\alpha),
\]
with the \(B_{7r}(x_\alpha)\) pairwise disjoint after finite coloring.  Then \(a=\sum\chi_\alpha^2\le1\), and \(a=0\) on \(\operatorname{supp}d\eta_\alpha\), exactly as required by the \(K_2^\eta\) energy.

The good set uses the volume-average maximal function
\[
\mathcal M_R f(x)=\sup_{0<s\le R}\fint_{B_s(x)}f.
\]
If \(x\) lies in the good set \(\mathcal M_R(|\operatorname{Rm}|^2)\le \widetilde\gamma^2/r^4\), then directly, for \(7r\le R\),
\[
r^4\fint_{B_{7r}(x)}|\operatorname{Rm}|^2\le \widetilde\gamma^2.
\]
No comparison with the average over \(B_R\) is needed.  If a later step needs the unnormalized bound \(\int_{B_{7r}}|\operatorname{Rm}|^2\le\gamma_{\rm abs}^2\), shrinking \(r\) alone is not enough in dimension four because \(\operatorname{Vol}(B_{7r})/r^4\) tends to a positive model constant.  Instead choose \(\widetilde\gamma\) smaller than the absorption threshold by a fixed dimensional factor.

The retained plateau volume comes from the calibrated ratio
\[
\operatorname{Vol}(g_i)/A_i\to {32\pi^2\over9},
\]
not from a coarse Euler bound.  Finite coloring preserves a fixed fraction of this volume.  Inner terminal centers are chosen strictly inside the \(a=1\) plateau, for instance in \(B_r(x_\alpha)\), and \(\rho\le r/2\) is fixed so terminal geodesic balls remain in the \(B_{5r}\) plateau after the small drift.

On the exact flow, the first-exit estimates split into three parallel branches from \(K_2^\eta\):
\[
K_2^\eta\Longrightarrow
\begin{cases}
\displaystyle \int_0^tY\le C\gamma K_2^\eta(0),\qquad
Y(t)\le C\gamma K_2^\eta(0)/t,\\[1mm]
\displaystyle J_6(t)\le e^{C(1+r^{-2})t}J_6(0),\\[1mm]
\displaystyle Q(t)\le e^{C(1+r^{-2})t}Q(0).
\end{cases}
\]
The \(Y\) branch feeds curvature Moser, \(J_6\) feeds defect Moser, and global \(Q\) feeds terminal Chern--Weil recalibration.  The Moser endpoints are
\[
\|aF(t)\|_\infty\le {C\gamma\over t},
\qquad
\|aE(t)\|_\infty\le C\delta\left({r^2\over t}\right)^{1/3},
\]
hence
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
\]
This controls bilipschitz drift, moving Sobolev constants, and retained plateau volume.  On the plateau \(a=1\), the curvature endpoint gives a uniform terminal curvature bound.

The parameter order is important: fix the geometric scale and absorption threshold, choose \(r\) and \(\widetilde\gamma\) so the support energy is small while retaining volume, choose \(\theta\) so the Gronwall factors remain fixed, then use \(\delta_i\to0\) to improve the drift part of the first-exit interval.

---

## 4. Terminal recalibration and pullback

Use \(e_\ell\) for exceptional cohomology classes to avoid conflict with the Einstein defect \(E=\operatorname{Ric}+g\).  The correct Chern--Weil identity is
\[
I-J={2A\over3}-q,
\]
and the sign-averaged deficit is
\[
D_{\rm av}=I-{2A\over3}-{2\over3}\sum_\ell(e_\ell^+)^2
=J-q-{2\over3}\sum_\ell(e_\ell^+)^2.
\]
For \(q\ge0\),
\[
0\le D_{\rm av}\le J\le {Q\over8\pi^2}.
\]
At terminal time this is applied to the evolved metric because the monopole classes and Chern--Weil identities are topological.

The nonnegative terminal density must include the full Einstein defect:
\[
\Phi_i=|E_i|^2+(s_i+4)^2+(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i.
\]
The established estimates give
\[
\int \Phi_i\,d\mu_{g_i(T)}\le119\,Q_i(T).
\]
This is the density to use in Liouville--Rauch averaging.  A density omitting \(|E|^2\) is insufficient: it would not imply local \(L^p\)-vanishing of the Ricci defect and therefore would not produce an Einstein limit.

Since \(Q_i(T)/A_i\to0\) and \(\operatorname{Vol}(P_i^{\rm in})\ge cA_i\), Liouville--Rauch averaging selects \(p_i\in P_i^{\rm in}\) with
\[
A_\rho\Phi_i(p_i)\to0.
\]
The exponential pullback metrics on a smaller tangent ball have bounded sectional curvature and Rauch noncollapse.  Harmonic coordinates give uniform \(C^{1,\alpha}\cap W^{2,p}\) bounds.  The selected density gives \(\|E_i\|_{L^2}\to0\), and bounded curvature upgrades this to every finite \(L^p\).  The harmonic-coordinate Ricci equation then yields strong finite-\(W^{2,p}\) convergence to a weak Einstein metric, which bootstraps smoothly.

The limiting germ satisfies
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,
\qquad
|W^+_{g_\infty}|^2={1\over24},
\qquad
\operatorname{spec}(W^+)=\left(-{1\over6},{1\over12},{1\over12}\right).
\]
Einstein implies \(\delta W^+=0\).  Derdziński's local theorem makes \((24|W^+|^2)^{1/3}g_\infty\) locally Kähler; the factor is constant, so \(g_\infty\) is locally Kähler.  A four-dimensional Kähler--Einstein metric with \(s=-4\) has \(|W^+|^2=s^2/24=2/3\), contradicting \(1/24\).

Bounded-\(A_i\) subsequences are handled after the initial calibration gives \(q_i/A_i\to0\).  Since \(q_i\in(1/3)\mathbb Z\) and \(q_i\ge0\), bounded \(A_i\) forces \(q_i=0\) eventually; the plateau volume is then bounded below by a fixed positive multiple of \(A_0\), and the same selection argument applies.

---

## 5. Present mathematical status

After the corrections above, and using Step 35's curvature and defect signed-Hessian tensor calculations as established modules, the accumulated estimates give a coherent proof of the family-uniform negative Ishida--LeBrun gap.  The proof should be consolidated into a new research note rather than used through the older Step 41/43 wording, because those notes still contain outdated formulas and dependency descriptions.

This restricted theorem would be a valuable four-dimensional negative-sign result: it rules out one serious no-Einstein geography as a source of arbitrarily tight negative Ricci pinching.  It does not settle the full Yau 26 proposition.  The positive branch, arbitrary four-dimensional topology, dimensions \(n\ge5\), dimension-only constants for all smooth manifolds, and Lean formalization remain major open work.

A02 message #367 also corrects the positive noncollapsed bi-Kähler stress example: the product curvature computation remains valid, but the topology and Chern--Gauss--Bonnet pieces are subtler; the example is a finite exceptional locus rather than a reason to abandon first-order positive noncollapsed work.  This supports a later return to positive and high-dimensional directions once the restricted negative theorem has been put into a clean, source-grounded proof note.
