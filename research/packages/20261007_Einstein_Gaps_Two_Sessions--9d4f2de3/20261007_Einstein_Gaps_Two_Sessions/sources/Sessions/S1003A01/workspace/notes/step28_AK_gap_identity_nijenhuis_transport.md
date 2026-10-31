# Step 28 — The canonical almost-Kähler gap identity for perpendicular cells

Scope: smooth diagonal Bianchi-IX \(O(-1)\) cells with an exact CH collar (perpendicular class:
the collapsing slot \(h\) is not the CH fibre \(f\)). Units: \(\widehat P=P/(8\pi^2)\), volumes in
\(\int W\,dt\) units, \(W=a_fa_ga_h\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\). Everything below is
exact (symbolic) unless stated as numerical. Scripts: `scripts/step27_flux_laws.py`,
`step27_cell_flux_budget.py`, `step28_ak_hatted_structure.py`, `step28_ak_nu_structure.py`,
`step28_ak_gap_identity.py`; data in `data/step27/`, `data/step28/`.

## 0. Step-27 results carried forward (consolidated)

* Orthogonal channels: \(|\mathrm{Ric}^\circ|^2=\tfrac43C^2+\tfrac23E^2+\tfrac12D^2\), so
  \(\widehat P=\int W(C^2/3+E^2/6+D^2/8)dt\); \(C=\mathrm{Ric}^\circ_{00}\), \(E=e_f-(e_g+e_h)/2\), \(D=e_g-e_h\).
* Bolt-anchored flux laws: \((Wq')'=W(\Pi_q-D)\), \((W\beta')'=W(\Pi_\beta-E)\),
  \(q=\log(a_g/a_h)\), \(\beta=\log(a_f/\sqrt{a_ga_h})\); at a smooth bolt \(Wq'\to-b^2\), \(W\beta'\to-b^2/2\);
  on CH \(Wq'=0\), \(W\beta'=\sinh^4R\). Hence \(\int WD=\int W\Pi_q-b^2\), \(\int WE=\int W\Pi_\beta-X^2-b^2/2\).
  Closed drifts \(W\Pi_q=4(a_g^2-a_h^2)(a_g^2+a_h^2-a_f^2)/W\),
  \(W\Pi_\beta=[4a_f^4-2a_f^2(a_g^2+a_h^2)-2(a_g^2-a_h^2)^2]/W\).
* Coupled Bianchi: \((W^{4/3}C)'=W^{4/3}[\tfrac23\beta'E+\tfrac12q'D+s'/4]\).
* Relative Weyl–volume identities (all exact-CH \(O(-1)\) cells):
  \(1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc}\), \(\widehat P=-5+\int W|W^-|^2+12V_{\rm exc}+S_{\rm exc}\),
  \(D_+=\int W(24-|W^+|^2)\), \(S_{\rm exc}=\int W(s^2/48-12)\).
* Sign correction: \(b_+=2-|v|^2-v_1v_2v_3\), \(v_i=a_i'-\gamma_i\),
  \(\gamma_i=(a_j^2+a_k^2-a_i^2)/(a_ja_k)\); self-dual curvature
  \(R^+_{ii}=-v_i'/(2a_i)+(-v_i-v_jv_k/2)/(a_ja_k)\) (diagonal in \((e^{0i}+e^{jk})/\sqrt2\)).
  Pointwise \(|W^+|^2\) values computed from the opposite product sign are superseded.

| \(x_0\) (X) | \(\widehat P\) | \(C\) | \(E\) | \(D\) | \(V_{\rm exc}\) | \(D_+\) |
|---|---|---|---|---|---|---|
| .015 (256) | .99767 | .317 | .166 | .515 | .00230 | .0913 |
| .038 (128) | .99529 | .299 | .164 | .532 | .00677 | .2586 |
| .07 (256) | 1.00076 | .291 | .161 | .549 | .01347 | .4951 |

## 1. Every diagonal cell is conformal to a diagonal almost-Kähler metric

Let \(\omega=d(\mathcal P\sigma_f)\), \(\mathcal P'/\mathcal P=2a_f/(a_ga_h)\), normalized by \(\mathcal P=a_ga_h\) on the CH
collar (this is \(2\Omega\) for the AAD-normalized form \(|\Omega|^2_{\hat g}=2\); the script's \(\phi\) equals this \(\mathcal P\));
\(\mathcal P\sim Ct^2\) at the bolt. Put \(u^2=\mathcal P/(a_ga_h)\) (=1 on CH), \(\hat g=u^2g\). \(\hat g\) is almost-Kähler on the
complement of the bolt only; at the bolt \(u^2\sim ct\), \(T\sim\tfrac23\sqrt c\,t^{3/2}\), \(A_f,A_g\asymp T^{1/3}\), \(A_h\asymp T\): an
anisotropic power-law singular end (not a cone), across which all densities and Stokes fluxes are integrable/vanishing.
Then \(\hat g=dT^2+\sum A_i^2\sigma_i^2\) with \(dT=u\,dt\), \(A_i=ua_i\), is again diagonal and
\(|\omega|_{\hat g}\) is constant exactly when

\[
A_f=\tfrac12\,(A_gA_h)_T .\qquad\text{(AK constraint)}
\]

Write \(A_g=\sqrt{\mathcal P}e^{q/2}\), \(A_h=\sqrt{\mathcal P}e^{-q/2}\), \(A_f=\mathcal P_T/2\) (note \(q\) is
conformally invariant). Symbolic computation (`step28_ak_hatted_structure.py`,
`step28_ak_nu_structure.py`) gives, for every such metric:

* the two rotating self-dual connection coefficients obey \(A_hv_g=-A_gv_h\); the **Nijenhuis
  scalar** is
  \[
  \nu=\frac{v_h}{A_h}=-\frac{v_g}{A_g}=-\frac12\Big(q_T+\frac{4\sinh q}{A_f}\Big),\qquad
  \kappa-\hat s=6\nu^2 ,
  \]
  (\(\kappa=6\widehat W^+_{\omega\omega}\) the conformal scalar curvature, AAD (10): \(\kappa-s=6|a|^2\)).
  So \(\hat g\) is Kähler iff \(q\) follows the Kähler squashing flow \(q_T=-4\sinh q/A_f\);
* \(W_3^+\) eigenvalue \(\lambda=(\widehat W^+_{gg}-\widehat W^+_{hh})/2\) satisfies the **linear transport law**
  \[
  \lambda=\tfrac12\nu_T+\beta\nu,\qquad \beta=-\frac{(A_f)_T}{2A_f}+\frac{2\cosh q}{A_f};
  \]
  (the \(|a|^2\) term of AAD (13) cancels in this gauge); \(W_2^+=0\) by symmetry;
* \(J\)-anti-invariant Ricci of \(\hat g\):
  \(\widehat D=2\nu_T+\nu(2A_f'/A_f-8\cosh q/A_f+4A_f/(A_gA_h))\),
  \(\widehat{\mathrm{Ric}}_{00}-\widehat{\mathrm{Ric}}_{ff}=-2\nu^2-8\nu\sinh q/A_f\); both vanish iff \(\nu=0\);
* **Chern identity as an exact Stokes formula** (`step28_chern_stokes_check.py`, residual 0): the Hermitian/Chern scalar
  \(s^\nabla=(\hat s+\hat s_{\rm star})/2=\hat s+2\nu^2\) (the usual star scalar is \(\hat s+4\nu^2\); below \(\hat s^*\) means \(s^\nabla\)) and
  \[
  \hat s^*\,A_fA_gA_h=\frac{d}{dT}\Big[4\mathcal P\cosh q-\mathcal P\mathcal P_{TT}-\tfrac12\mathcal P_T^2\Big].
  \]
  The bracket vanishes at the bolt (\(A_gA_h\sim t^2\), \(A_gA_hA_f'\sim t\)) and equals \(-6X^2\) on CH,
  so \(\int\hat s^*d\hat V=-6X^2=-24V_{\rm CH}\) exactly: the conical bolt contributes nothing.
  Pinning is the Stokes formula \(\int d\hat V=[\mathcal P^2/4]=V_{\rm CH}\).

## 2. The exact gap identity

Define \(H=\int(u^2-1)^2W\), \(G=\int u'^2W\), \(N=\int4\nu^2d\hat V\), \(Q_A=\int4\lambda^2d\hat V\),
\(Q_\delta=\int(\widehat W^+_{\omega\omega}+4)^2d\hat V\), \(d\hat V=u^4W\,dt\).

**Theorem A.** For every smooth diagonal exact-CH perpendicular \(O(-1)\) cell,
\[
\boxed{\widehat P-1=12H+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N+\Sigma},\qquad
\Sigma=\int W(s+24)(u^2-1)+\int W\frac{(s+24)^2}{48},
\]
and \(V_{\rm exc}=H+G/2+N/24+\frac1{12}\int(s+24)u^2W\). For \(s\equiv-24\), \(\Sigma=0\).
Since \(12(u^2-1)^2+(s+24)(u^2-1)+(s+24)^2/48=12(u^2+s/24)^2\), the identity holds **for every \(s\)** in the form
\[
\widehat P-1=12H_s+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N,\qquad H_s=\int W\,(u^2+s/24)^2dt ,
\]
so \(-\tfrac32N\) is the only negative term without any scalar normalization.

Proof. (i) \(|W^+|^2=\tfrac32W_{\omega\omega}^2+\tfrac12(W_{gg}-W_{hh})^2\) (diagonal, traceless) and
conformal invariance of \(|W^+|^2dV\) give \(D_+=24V_{\rm exc}+12\int\delta\,d\hat V-\tfrac32Q_\delta-\tfrac12Q_A\)
with \(\delta=\widehat W_{\omega\omega}+4\). (ii) \(\kappa/6=\hat s^*/6+\tfrac23\nu^2\) and the Chern identity give
\(\int\delta\,d\hat V=N/6\). (iii) \(\int\hat s\,d\hat V=6G+\int su^2W\) (boundary terms vanish: \(uu'W\to0\) at
the bolt, \(u'=0\) on CH) and \(\int\hat s\,d\hat V=-24V_{\rm CH}-N/2\) give the volume formula. (iv) Insert in
\(1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc}\). ∎

Numerical confirmation (`data/step28/gap_*.json`; \(s\) not exactly \(-24\) in these records):

| \(x_0\) (X) | \(\widehat P-1\) | 12H | 6G | 1.5Qδ | 0.5QA | −1.5N | Σ | residual |
|---|---|---|---|---|---|---|---|---|
| .015 (256) | −.002333 | .00074 | .02215 | .00020 | .00705 | −.03250 | .00003 | 5e−11 |
| .038 (128) | −.004713 | .00333 | .05563 | .00113 | .03286 | −.09766 | −.000005 | 2e−10 |
| .038 (512) | −.004822 | | | | | | | 3e−10 |
| .07 (256) | +.000757 | .00829 | .10094 | .00351 | .08011 | −.19150 | −.00060 | 6e−10 |

Interpretation. All terms are nonnegative except \(-\tfrac32N\). **The entire subthreshold saving is
nonintegrability of the canonical almost-complex structure**, paid for by the conformal factor
(\(H,G\)), the \(J\)-type Weyl variance \(Q_\delta\), and the \(W_3^+\) energy \(Q_A\). A cell whose
canonical structure were integrable would satisfy \(\widehat P\ge1+12H>1\); for perpendicular
cells this is impossible (§3), which is precisely why the perpendicular branch, unlike the aligned
Kähler branch, can go below threshold. The volume formula is the quantitative form of the volume
floor (the strategist's SW argument gives \(V\ge V_{\rm CH}\) without symmetry; here the excess is
identified as \(H+G/2+N/24\)). Positive volume excess does not contradict loss of recoverable CH
background (different quantity).

Exact regrouping: \(\nu\mp(\log u^{-1})_T=-v_g/(ua_g),\ v_h/(ua_h)\), hence
\(6G-\tfrac32N=6\int u^2a_fv_gv_h\,dt\) (checked to 1e−16). Thus
\(\widehat P-1=12H+\tfrac32Q_\delta+\tfrac12Q_A+6\int u^2a_fv_gv_h\,dt+\Sigma\): the sign-indefinite
remainder is the same cubic-type spin interaction (\(v_gv_h\) is part of \(v_1v_2v_3\) in \(b_+\)) that
was identified in Step 7 as the source of the signed compensation.

## 3. Bolt Nijenhuis charge and its transport

Near the bolt \(q=\log(b/t)+\dots\), \(q'+4\sinh q/a_f\simeq1/t\), so \(\nu\simeq-1/(2ut)\sim t^{-3/2}\):
the perpendicular bolt **forces** nonintegrability. With \(\mu=\exp\int2\beta\,dT
=(ua_f)^{-1}\exp\int4\cosh q/a_f\,dt\) (\(\mu\sim t^{3/2}\) at the bolt), the transport law integrates to the
exact charge law (\(\nu\equiv0\) on the exact collar)
\[
K:=\lim_{\rm bolt}\mu\nu=-2\int_{\rm cell}\mu\lambda\,dT\neq0 .
\]
Numerically (μ normalized to \(1/(ua_f)\) at \(X\)): \(K=-0.0072590,-0.0174759,-0.0292342\) for
\(x_0=.015,.038,.07\), law satisfied to \(10^{-12}\). The forced charge must be unwound by \(W_3^+\)
before the CH collar; this is the cost term \(\tfrac12Q_A\).

At leading order at the bolt \((\log u^{-1})_T\simeq\nu\), so the densities of \(6G\) and \(\tfrac32N\)
coincide (both \(\to\tfrac32cb^2\)); the bolt zone itself is neutral. Cumulative profile at
\(x_0=.038\) (`gap_lm3_x00.038_X128_d24.json`): \(6G+\tfrac32(-N)\) stays \(\approx0\) for \(t<0.05\),
the net gain is generated in \(0.1\lesssim t\lesssim0.7\), and the far zone is a net cost.

## 4. Far-field Hardy positivity

From \(\nu_T=2\lambda-2\beta\nu\): \((\nu^2w)_T=4\nu\lambda w+\nu^2w\Lambda\), \(w=A_fA_gA_h\),
\(\Lambda=w_T/w-4\beta\). On \([T_0,\infty)\) with \(\Lambda\ge c>0\) and \(\nu=0\) at the collar,
\[
c\!\int_{T_0}\!\nu^2w+\nu^2w(T_0)\le4\Big(\int\nu^2w\Big)^{1/2}\Big(\int\lambda^2w\Big)^{1/2}
\Rightarrow \int_{T_0}\nu^2w\le\frac{16}{c^2}\int_{T_0}\lambda^2w .
\]
Hence the Nijenhuis sector \(2\int\lambda^2-6\int\nu^2\ge0\) on any **terminal** interval (ending in the exact
collar, \(\nu=0\) there) on which \(\Lambda\ge4\sqrt3\). (Sharp version: sign of the weighted form
\(\int\rho(\tfrac12\psi_T^2-6\psi^2)\), \(\psi=\mu\nu\), \(\rho=w/\mu^2\).)
On CH, \(\Lambda=(8x-3)/\sqrt{x(1+x)}\to8\) (\(x=\sinh^2R\)), and \(\Lambda=4\sqrt3\) at
\(x_H=3+\tfrac34\sqrt{15}\approx5.905\). On actual cells the last crossing is at
\(x_*\approx5.94\)–\(5.99\) (\(t_*\approx1.6\)), the far sector is positive
(.00114/.00588/.01508) and \(\int\nu^2/\int\lambda^2\approx0.18<1/3\) there. For this optimized family all
Nijenhuis gain is generated before the final crossing \(x\approx6\) (a numerical statement about these
cells; \(x\) is the cell coordinate, intrinsic \(\sinh^2R\) only on the collar), where the conformal sector (.0231/.0601/.1127) nearly balances the
near Nijenhuis sector (−.0266/−.0707/−.1265).

## 5. What this changes and what remains

1. The diagonal lower-bound problem is now: minimize
   \(\mathcal F=12H+6G+\tfrac32Q_\delta+2\!\int\!\lambda^2d\hat V-6\!\int\!\nu^2d\hat V\) over diagonal AK metrics
   \(\hat g\) with conical bolt, where \(v=u^{-1}\) solves the Yamabe equation \(6\hat\Delta v+\hat sv+24v^3=0\),
   \(v\to1\) on CH. The only negative term is controlled by the forced charge \(K\), the transport law,
   and Hardy positivity outside \(x_H\). A sharp bound needs a near-zone inequality coupling
   \(\nu\) to \(u\) (bolt cancellation) and to \(\lambda\) (transport) for \(x\lesssim6\).
2. Non-diagonal cells (conditional programme): the canonical object is the closed SD form extending the CH Kähler form
   (unique when it exists, because the collar-relative intersection form is negative definite; existence with a
   prescribed collar germ is an overdetermined problem and is not automatic); \(a(g)=\int_E\omega\) is a geometric modulus (zero in the
   perpendicular diagonal class, positive for aligned Kähler cells, where a boundary flux makes
   \(a\ne0\) possible). Its zero set is generically 1-dimensional (near-symplectic geometry), so
   the general identity requires Taubes-type control of the zero locus and an \(a\)-dependent Chern
   term; the U(2) splitting adds \(2|W_2^+|^2\). This is the natural unified aligned/perpendicular
   formulation. Conjectural general identity (TTCS step28 generator, eqs. (20)–(28)): with \(|\Omega|^2=2\),
   \(a=\int_E\Omega\), \(k=c_1(J)\cdot E\), \(\zeta\) the \(W_2^+\) off-block vector,
   \(\widehat P-1=\frac{9a^2}{\pi^2}+\frac{6ka}{\pi}+12H_s+6G+\tfrac32Q_\delta+\frac1{2\pi^2}\int(2|\zeta|^2+|W_3^+|^2)d\hat V-\tfrac32N
   -\frac{3\mathcal R_Z}{2\pi^2}\), \(\mathcal R_Z\) a zero-circle Chern-circulation term. Consistency check: for an aligned
   Kähler cell (\(k=1\), \(u=1\), \(N=0\)) it reproduces exactly \(P=2(2\pi+6a)^2+L/4\). Pinning becomes
   \(V_{\hat g}-V_{\rm CH}=-a^2/2\).
3. Contact closure (TTCS generator): \(y=\tanh(q/2)\) obeys \(y_T+4y/A_f=-\nu(1-y^2)\); with \(\eta_T=4\eta/A_f\),
   \(\int\eta\nu(1-y^2)dT=\eta(\text{bolt})>0\) (\(y=1\) at bolt, 0 on CH). Since \(\nu<0\) near the bolt, \(\nu\) must change
   sign: a second global moment constraint beside \(K\). Two-constraint capacity bound for \(Q_A\) to be tested.
4. Collapse corollary: since \(-\tfrac32N\) is the only negative term, any sequence of perpendicular diagonal cells
   with \(N\to0\) has \(\liminf\widehat P\ge1\); subthreshold collapsed sequences must retain nonintegrability energy.
5. Collapsed branch: the identity applies to any smooth diagonal competitor; a collapsed
   Taub-bolt-like prefix must be evaluated in these terms (H, G, N, \(Q_A\), \(Q_\delta\)), not only by charges.

## 6. Verification record and caveats

* Independent TTCS verification (`trace/ttcs/results/step28_ttcs01_verifier1_integration.md`) confirmed Theorem A
  and all coefficients, and supplied the corrections incorporated above: the \(\Omega\) vs \(2\Omega\) normalization;
  \(A_hv_g=-A_gv_h\) (not \(A_gv_g=-A_hv_h\)); \(\hat s+2\nu^2\) is the Hermitian/Chern scalar; the \(H_s\) square
  completion; Hardy positivity only on terminal intervals; non-diagonal statements conditional. It also notes that
  Theorem A is an exact repackaging of the inherited relative identity; the new content is the AK structure
  (pinning, Chern–Stokes flux, transport, forced charge, bolt cancellation, tail positivity).
* In `step28_ak_gap_identity.py` the JSON fields `law_residual` (hard-coded 0) and `transport_rel_residual_max`
  (gradient taken against a surrogate coordinate) are not evidence; the meaningful numerical check of the transport
  is `law_residual_from_i30` (\(\sim10^{-12}\)); the transport law itself is symbolic (`ak_nu_structure.json`).
* Peer S1003A02 Step 34: \(b_+\) is already an exact HJ calibration (\(\sup(\dot b_+-L)=0\) identically); decorations
  \(\phi(q,\eta)\) give zero gain. The missing cost must come from the Nijenhuis/conformal/transport near-zone
  structure identified here.
