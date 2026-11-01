# Step 68 — Exact product cscK saddle, corrected threshold, and closure of the twist-flux line

Agent3, Execute. Inputs: `step67_cK_local_coercivity_at_cscK.md`, the Step-67 verifier, and the unverified generator branch `trace/ttcs/results/step67_ttcs01_sub1_generator.md`. The independent verification is `trace/ttcs/results/step68_ttcs01_verifier1_integration.md`; the corrected local-theorem statement is `...verifier2_integration.md`.

## 1. Product theorem

Let
\[
(M,g_0,J_0,\omega)=(\Sigma_1,g_1,J_1,\omega_1)\times(\Sigma_2,g_2,J_2,\omega_2),
\qquad K_1\ne K_2<0,
\]
where each factor has constant Gaussian curvature. Let \(Q\) be the real symmetric tensor underlying a nonzero holomorphic quadratic differential on \(\Sigma_1\), let \(\Delta_2f=\mu f\), \(\mu>0\), and put \(A=g_1^{-1}Q\). Consider the fixed-symplectic compatible family
\[
 g_t|_{T\Sigma_1}=g_1(e^{tfA}\cdot,\cdot),\qquad g_t|_{T\Sigma_2}=g_2.
\]
Then, with Taylor coefficients \(F(g_t)=F(g_0)+tF_1+t^2F_2+O(t^3)\),
\[
\boxed{
8\pi^2\bigl(p-|c_1^-|^2\bigr)_2
=\frac{\mu}{4}\bigl(\mu+K_1-K_2\bigr)\|fQ\|_2^2 .}
\tag{68.1}
\]
The Step-67 generator's coefficient \(\mu[\mu+2(K_1-K_2)]/4\) was twice too negative. The error was a norm-convention mismatch in the torsion: in form norms,
\[
 |(\nabla\omega)'|^2=\frac12|Q|^2|df|^2,
 \qquad \int u_2=\frac{\mu}{8}\|fQ\|_2^2,
\tag{68.2}
\]
not \(\mu\|fQ\|^2/4\). Equivalently,
\[
(\rho_0,t_2^-)=-\frac{(K_1-K_2)\mu}{16}\|fQ\|_2^2.
\tag{68.3}
\]
The other two inputs are correct:
\[
 (\operatorname{Ric}'')_1=\frac\mu2 fQ,
 \qquad (\rho_{0,1}')^{\perp\mathcal H}=0.
\tag{68.4}
\]

### Direct curvature proof

The block connection gives
\[
\operatorname{Ric}_V=K_tG_t+\frac{t\mu f}{2}G_tA,
\qquad
\operatorname{Ric}_H=K_2g_2-\frac{t^2}{4}|Q|^2df\otimes df,
\]
where \(K_t\) is the Gaussian curvature of \(G_t=g_1e^{tfA}\) with the second-factor point held fixed. If \(n_t=t^2|Q|^2|df|^2/4\), then
\[
 |\operatorname{Ric}^\circ|^2
 =(K_t-K_2)^2+\frac{t^2\mu^2f^2}{4}|Q|^2+(K_t-K_2)n_t+O(t^3).
\]
The area of \(G_t\) is fixed. Gauss--Bonnet kills the integrated second variation of \(K_t\). Using \(\int|df|^2=\mu\int f^2\) proves (68.1).

The product form \(\omega=\omega_1+\omega_2\) stays fixed, and \(\eta=\omega_1-\omega_2\) remains harmonic ASD. Thus \(|c_1^-|^2\) is exactly constant along the family. Also \(s'_0=0\). Since Lemma 67.1 gives \(D(p-|c_1^-|^2)=0\), an \(O(t^2)\) conformal correction solving the exact constant-scalar equation does not change (68.1). The operator \(6\Delta-2s_0\) is invertible because \(s_0<0\).

### Consequences

If \(K_1<K_2\), then this is a strict non-Kähler descent direction precisely when
\[
0<\mu<K_2-K_1.
\tag{68.5}
\]
For the factor-swapped mode,
\[
8\pi^2(p-q^2)_2=\frac\lambda4(\lambda+K_2-K_1)\|hQ_2\|_2^2.
\]
Moreover the ledger components are
\[
\ell_2(fQ)=\frac{\mu^2}{32\pi^2}\|fQ\|_2^2,
\qquad
q^2d_2(fQ)=\frac{(K_2-K_1)\mu}{64\pi^2}\|fQ\|_2^2,
\]
so
\[
\boxed{c_K\le \frac{2\lambda_1(\Sigma_2)}{K_2-K_1}.}
\tag{68.6}
\]
Pinching a separating geodesic makes \(\lambda_1\to0\), so no uniform positive lower bound for \(c_K\) exists even within fixed product topology and fixed unequal curvature scales. This mode has \(\ell_2>0\); it is not an aligned null mode and does not test the finite-dimensional obstruction \(\Xi\).

## 2. What the direct scripts showed

`workspace/scripts/step68_product_saddle_direct.py` evaluated local jets \(q=z^n\), \(n=0,1,2\). The outputs contain the common global terms plus an \(n\)-dependent intrinsic-curvature term. This term is a curvature-transgression divergence: after identifying oriented frame bundles, the surface connection difference is a global one-form \(b_t\), and
\[
(K(G_t)-K_1)dA_1=db_t.
\]
Its quadratic coefficient integrates to zero on a closed surface. The scripts were useful falsifiers of a pointwise-density interpretation, but are not themselves the proof of (68.1). Their durable outputs are `data/step68_product_saddle_direct_n{0,1,2}.json`. The files `step68_product_saddle_covariant.py`, `step68_product_saddle_global.py`, and `step68_product_saddle_global_exact.py` are exploratory ledgers, not independent proofs.

## 3. Relation to blow-ups and the certified cells

The product saddle is a genuine near-extremal-structure result, but it does not create a new route to \(p<k\) on the general-type blow-up family by itself. At a cscK metric,
\[
q^2=|c_1^-|^2=k+\Pi.
\]
A diffuse product-type primitive Ricci form reflects a diffuse canonical ASD component, so \(\Pi\) is generally order one. A sufficiently small second-order descent below \(q^2\) then remains above \(k\). In the Arezzo--Pacard regime \(\Pi\to0\), primitive Ricci curvature concentrates near exceptional curves; the relevant rotation is the Burns-core direction already detected by Theorem F and realized nonperturbatively by the certified perpendicular cell. This is a structural interpretation, not a theorem excluding every other blow-up mode. It places the product saddle in the near-extremal chapter rather than promoting it to a new global lower-bound or construction mechanism.

## 4. Corrected local theorem at the Kähler end

Lemma 67.1 is unconditional: every non-KE cscK metric is stationary for
\[
p-|c_1^-|^2=C_+-|c_1^+|^2
\]
on all Riemannian variations. The strongest justified replacement for 67.K is:

1. Under zero-free or transverse \(Z(\widehat h)\), an \(\ell_2\)-null direction follows the *moving* harmonic ASD line and induces a first-order almost-Kähler aligned pair with \((\operatorname{Ric}'')'=0\).
2. Define
\[
\mathcal P_\omega:H^{0,1}(T^{1,0})\to H^{0,2},\qquad [\mu]\mapsto[\mu\lrcorner\omega],
\]
and \(\Xi(k)=[\dot\Omega_k]^{0,2}\bmod\operatorname{im}\mathcal P_\omega\). If \(\Xi(k)=0\), the pair is first-order Kähler and \(k\in\operatorname{rad}d_2\). The corrected Blair--Ianus constants are
\[
s^*-s=|\nabla\omega|^2,
\quad \int s=4\pi c_1\cdot[\omega]-\frac12E,
\quad DE=2\int\langle\operatorname{Ric}'',k\rangle,
\quad \operatorname{Hess}E=2\| (\nabla\omega)'\|_2^2.
\]
3. If \(\widehat h\) is zero-free, the gauge-reduced augmented symbol is injective, the nullspace \(K\) is finite-dimensional, and \(\ell_2\) controls \(H^2\) on \(K^\perp\).
4. If additionally \(\Xi|_K=0\), then \(d_2\le C\ell_2\), hence \(c_K>0\), and
\[
L\ge c q_0^2\delta-C'\|k\|_{C^{2,\alpha}}^3
\]
on the linear constant-scalar/Bianchi constraint space. The functionals are smooth but nonlocal. No nonlinear isolation follows.
5. The exact deficit uses the moving reference direction,
\[
2\pi qd_2=\tau_{\rm ref,2}-\frac1{\sqrt2}\int\frac{|w_1|^2}{|v_0|}.
\]
On \(K^\perp\), the spectral operator is \(T-N\), with \(T\) compact self-adjoint and \(N\ge0\) bounded. Positive eigenvalues are discrete; the whole operator need not be compact.

Products of curves have \(\mathcal P_\omega=0\), so the null-kernel obstruction remains real. The descent mode above bypasses it because \(\ell_2>0\).

## 5. Status

The twist-flux line now yields: the exact metric-only ledger; rank-one rigidity and its Einstein--Maxwell/Blair--Ianus equality class; unconditional cscK stationarity; conditional local coercivity controlled by \(\Xi\); and an explicit product family showing that \(c_K\ge2\) is false in general. It does not yield an unrestricted positive tariff, an Einstein-nonexistence theorem, or a blow-up diffuse construction below \(k\).
