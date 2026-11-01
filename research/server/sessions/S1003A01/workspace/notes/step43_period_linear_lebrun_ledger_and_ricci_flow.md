# Step 43 — The period-linear LeBrun ledger, the Yamabe ledger of the certified cells, and the Ricci-flow consequence

Conventions. \(X\) minimal of general type, \(A=c_1^2(X)=K^2\), \(M=X\#k\overline{\mathbb{CP}}^2\) with exceptional classes \(E_i\), \(E_i^2=-1\), \(K\cdot E_i=0\) (\(K=K_X\) pulled back). Sign-family hypothesis (as in A02 Theorems N/W/K): for every metric, every \(a_\varepsilon=K+\sum\varepsilon_iE_i\), \(\varepsilon\in\{\pm1\}^k\), is a monopole class (true for \(b^+(X)\ge2\); chamber version for \(b^+=1\)). \(\hat g\) = Yamabe representative with \(s\equiv-4\), \(\Delta V=\operatorname{Vol}(\hat g)-2\pi^2A\). For a class \(c\), \(c^\pm\) are its \(g\)-harmonic SD/ASD projections; \(|c^-|^2:=-(c^-)^2\ge0\). \(\Pi_g:=\max_\varepsilon (a_\varepsilon^+)^2-A\).

LeBrun's inputs (Proposition 4 of math/0111228, read via A02's step48 note, and LeBrun's scalar estimate): for every monopole class \(a\),
\[
\int(s-\sqrt6|W^+|)^2\ge72\pi^2(a^+)^2,\qquad \int s^2\ge32\pi^2(a^+)^2 .
\]
At \(s\equiv-4\) these give, exactly as in A02's (LeB\(_{\rm full}\)),
\[
8\pi^2k-P(\hat g)\le4\Delta V-\tfrac49\!\int(\sqrt6|W^+|-2)^2-16\pi^2\Pi_g,\qquad \Delta V\ge2\pi^2\Pi_g. \tag{L}
\]
(Derivation check: \((4+w)^2=3w^2+24-2(w-2)^2\) with \(w=\sqrt6|W^+|\), Gauss–Bonnet \(P=\tfrac23\int w^2+\tfrac43V-8\pi^2(A-k)\).)

## 1. The period term is linear in exceptional periods

A02 bounded \(\Pi_g\ge|K^-|^2+\sum|E_i^+|^2\) (average over signs), which is quadratic in periods. Maximizing over signs instead gives a linear term.

**Proposition 43.1.** For every metric \(g\) and every \(c\in\mathcal H^+_g\) with \(c^2>0\),
\[
\Pi_g\ \ge\ \frac{\bigl(|K\cdot c|+\sum_i|E_i\cdot c|\bigr)^2}{c^2}-A .
\]
With \(c=K^+\) and \(e_i:=E_i\cdot K^+\) (the exceptional periods of the SD-harmonic part of the canonical class),
\[
\Pi_g\ \ge\ |K^-|^2+2\sum_i|e_i|+\frac{(\sum_i|e_i|)^2}{(K^+)^2}.
\]
If \(\mathcal H^+_g\) contains a class \(c=K-\sum\sigma_iE_i\) (the situation of every exact-collar cell configuration, including the Step-40/41 rotated symplectic family, where \(c=[\psi]/2\pi\) in the \(\operatorname{Ric}=-g\) scale and \(\sigma_i=3p_i/\pi\) with \(p_i\) the profile-scale period), then exactly \(K\cdot c=A\), \(E_i\cdot c=\sigma_i\), \(c^2=A-|\sigma|_2^2\) and
\[
\Pi_g\ \ge\ \frac{(A+|\sigma|_1)^2}{A-|\sigma|_2^2}-A\ \ge\ 2|\sigma|_1+|\sigma|_2^2 ,\qquad
e_i=\sigma_i+\sum_j G_{ij}\sigma_j,\ \ G_{ij}=E_i^+\cdot E_j^+ .
\]
*Proof.* \((a^+)^2\ge(a\cdot c)^2/c^2\) (projection onto the line \(\mathbb Rc\subset\mathcal H^+_g\)); choose \(\varepsilon_i=\operatorname{sign}(K\cdot c)\operatorname{sign}(E_i\cdot c)\), so \(|a_\varepsilon\cdot c|=|K\cdot c|+\sum|E_i\cdot c|\). For \(c=K^+\), \(K\cdot K^+=(K^+)^2=A+|K^-|^2\) and \((x+y)^2/x\ge x+2y\). For \(c=K-\sum\sigma_jE_j\): \(E_i\cdot c=\sigma_i\), \(K\cdot c=A\); the formula for \(e_i\) follows from \(P_gK=c+\sum\sigma_jP_gE_j\) with \(P_g\) the projection to \(\mathcal H^+_g\). ∎

**Theorem 43.2 (period-linear LeBrun ledger).** Under the sign-family hypothesis, with \(\Delta V_{\rm free}:=\Delta V-2\pi^2\Pi_g\ge0\),
\[
\boxed{\;P(g)\ \ge\ P(\hat g)\ \ge\ 8\pi^2\Bigl(k+2\sum_i|e_i|\Bigr)-4\Delta V_{\rm free}+\tfrac49\!\int_M(\sqrt6|W^+_{\hat g}|-2)^2d\mu_{\hat g},\qquad \Delta V\ge 4\pi^2\sum_i|e_i| .\;}
\]
*Proof.* \(4\Delta V-16\pi^2\Pi_g=4\Delta V_{\rm free}-8\pi^2\Pi_g\) and \(\Pi_g\ge2\sum|e_i|\) in (L). ∎

Scope of the improvement (TTCS correction). The linear bound does not dominate A02's averaged bound pointwise when \(b^+>1\): one can have \(e_i=0\) with \(E_i^+\neq0\). The safe combined statement is \(\Pi_g\ge|K^-|^2+\max\{2\sum|e_i|+(\sum|e_i|)^2/(K^+)^2,\ \sum|E_i^+|^2\}\). For several rotated cells, \(e=(I+G)\sigma\) does not by itself give \(\|e\|_1\ge\|\sigma\|_1\); use the direct \(c\)-estimate \(\Pi_g\ge2\|\sigma\|_1+\|\sigma\|_2^2\) there, and read Theorem 43.2 with \(\sum|e_i|\) replaced by \(\|\sigma\|_1\) whenever \(c=K-\sum\sigma_iE_i\in\mathcal H^+_g\). For one cell, \(e=\sigma(1+G_{11})\) and \(|e|\ge|\sigma|\).

Interpretation. Exceptional SD periods are charged **linearly**: either directly in \(P\) (when the Yamabe excess is only the period-forced amount \(2\pi^2\Pi_g\)) or by forcing at least \(4\pi^2\sum|e_i|\) of Yamabe excess. Only *free* Yamabe excess can finance a saving below \(8\pi^2k\).

**Corollary 43.3 (the aligned Kähler tariff is LeBrun's period term).** For an aligned Kähler blow-up cell of exceptional area \(t\) in the profile scale (\(\operatorname{Ric}=-6g\) on the CH collar), \(\sigma=3t/\pi\). The ledger gives \(P\ge8\pi^2(1+6t/\pi)-4\Delta V_{\rm free}\). For a Kähler metric \(\int s\,d\mu=-8\pi^2(A+\sigma)\), \(V=2\pi^2(A-\sigma^2)\) (single cell, \(\operatorname{Ric}=-g\) scale), so \(16\hat V=Y^2\le\int s^2=L_s+32\pi^2(A+\sigma)^2/(A-\sigma^2)\), i.e. \(4\Delta V\le8\pi^2[(A+\sigma)^2/(A-\sigma^2)-A]+L_s/4\). The bracket is exactly the \(c=K-\sigma E\) lower bound for \(\Pi_g\), so exactly (no \(O(\sigma^2)\) error)
\[
4\Delta V_{\rm free}\le L_s/4,\qquad
P_{\rm K\ddot ahler\ cell}\ \ge\ 8\pi^2\bigl(1+6t/\pi\bigr)-L_s/4+\tfrac49\!\int(\sqrt6|W^+|-2)^2 .
\]
Its topological term has exactly the first-order slope of the inherited Kähler law \(P=2(2\pi+6t)^2+L/4=8\pi^2(1+6t/\pi)+\dots\) (Step 8); the scalar-variance terms enter with opposite signs (\(+L/4\) in the law, \(-L_s/4\) in the bound), so equality of full first derivatives needs \(L_s=o(t)\). The linear Kähler blow-up tariff is therefore the LeBrun period term at period-forced Yamabe excess; the perpendicular escape lives entirely in free Yamabe excess at zero period.

**Remark 43.4 (zero-period strictness, quantitative form).** For a smooth family \(g_\psi\) with \(c_\psi=K-\sum\sigma_i(\psi)E_i\in\mathcal H^+_{g_\psi}\), \(\sigma(0)=0\), the functions \(F_\varepsilon(\psi)=4\Delta V+P(\hat g)-8\pi^2k-16\pi^2((a_\varepsilon^+)^2-A)\) are smooth (Yamabe metrics are unique and smooth in \(g\) when \(Y<0\); harmonic projections are smooth) and nonnegative, \(F_\varepsilon(0)=F_{-\varepsilon}(0)\), and, since \((a_\varepsilon^+)^2-(a_{-\varepsilon}^+)^2=4\varepsilon\cdot e\) and \(e=(I+G)\sigma\), \(F_\varepsilon'(0)-F_{-\varepsilon}'(0)=-64\pi^2\,\varepsilon\cdot(I+G(0))\sigma'(0)\). \(I+G(0)\) is positive definite, so if \(\sigma'(0)\neq0\) some \(\varepsilon\) makes this nonzero and \(F_\varepsilon(0)>0\). Quantitatively, if on \(|\psi|\le r\) the relevant second-order remainders are bounded by \(\Lambda\psi^2/2\), then with \(d=32\pi^2|\varepsilon\cdot e'(0)|\), \(F(0)\ge\sup_{0\le\rho\le r}(d\rho-\Lambda\rho^2/2)\), which equals \(d^2/2\Lambda\) only if \(d/\Lambda\le r\). Qualitative strictness already follows from LeBrun's equality case; the new content is that the cutoff rotation of Step 41 (\(\sigma'(0)\ne0\) rigorously) converts the second variation into a quantitative slack. \(\Lambda\) along the rotation is not computed.

## 2. The Yamabe ledger of the actual cells (floating, checked)

Script `workspace/scripts/step43_yamabe_lebrun_ledger.py`; data `workspace/data/step43/ledger_*.json`. The complete metric is the cell plus exact CH; the Yamabe equation \(-6\Delta u+su+24u^3=0\) is solved for \(v=u-1\) (finite volume, zero bolt flux, \(v=0\) at \(x=1.28\times10^6\)). Direct integration of \(\int(u^4-1)\) is unreliable at the needed precision: the CH tail \(v\sim x^{-1-\sqrt3}\) multiplies a volume growing like \(x^2\), so a \(10^{-8}\) error in \(v(X)\) shifts \(\Delta V\) by \(10^{-4}\). The volume is therefore taken from the exact tail-free identity
\[
\int s^2d\mu_g-576\hat V\ (\text{relative})=\int\bigl[e^2+48ev-1152v^3-576v^4\bigr]d\mu_g,\qquad e=s+24,
\]
whose integrand vanishes in the exterior up to \(O(v^3)\). The direct and identity values differ by \(3R_{\rm trap}=1.45\times10^{-4}\), \(R_{\rm trap}\) the trapezoidal integral of the Yamabe equation; it comes mainly from truncating the integrals at \(100X\) while the solve extends to \(10^4X\) (TTCS reading). The JSON headline fields `DeltaV`, `D_W`, `F_LeB`, `F_Y` are the superseded direct values; the table uses `DeltaV_identity`, `F_LeB_identity`, `F_Y_identity`, and \(D_W=\delta W+\tfrac23\Delta V\) recomputed. The pointwise discrete residual is dominated by near-bolt conditioning, so the solve is not pointwise certified; the integrated residual suggests an uncertainty of order \(10^{-5}\) in \(4\Delta V\). These are relative noncompact model ledgers (cell plus CH end); closed-host statements require the collar and global Yamabe bookkeeping. Independent checks: Gauss–Bonnet for \(g\) closes to \(2\times10^{-8}\) (x₀=.03) and \(1.8\times10^{-7}\) (x₀=.038); the identity gives \(P(g)-P(\hat g)=1.88172049\times10^{-6}\), agreeing with the conformal formula \(24\int|\nabla u|^2+3\int(\Delta u/u)^2\) to \(10^{-11}\); results are stable between \(N=4\times10^4,8\times10^4,1.6\times10^5\) to \(10^{-8}\).

Per cell, relative to the replaced CH ball, \(8\pi^2\) units, \(\operatorname{Ric}=-g\) scale:

| quantity | x₀=.03, X=128 (certified profile) | x₀=.038, X=128 |
|---|---|---|
| \(1-P(g)\) | 0.0043373 | 0.0047126 |
| saving \(1-P(\hat g)\) | 0.0043391 | 0.0047127 |
| conformal Weyl deficit \(\delta W=\int_{CH}|W^+|^2-\int_{\rm cell}|W^+|^2\) | 0.0187835 | 0.0240548 |
| Yamabe excess \(\Delta V\) | 0.0530963 | 0.0686297 |
| \(4\Delta V\) | 0.212385 | 0.274519 |
| A02 \(D_W=\delta W+\tfrac23\Delta V\); \(4D_W\) | 0.216724 | 0.279232 |
| LeBrun term \(\tfrac49\int(\sqrt6|W^+|-2)^2\) | 0.0042971 | 0.0064352 |
| \(2\int\Psi(W^+_{\hat g})\) | 0.026465 | 0.039573 |
| \(\int\operatorname{dist}(W^+_{\hat g},\mathcal K)^2\) | 0.0075024 | 0.0111805 |
| LeBrun slack \(F_{\rm LeB}=4\Delta V-\text{saving}-\text{LeB}\) | 0.203749 | 0.263371 |
| Theorem-Y slack \(4\Delta V-\text{saving}-2\int\Psi\) | 0.181581 | 0.230234 |
| efficiency \(\text{saving}/4\Delta V\) | 0.0204 | 0.0172 |
| \(\int|W^-|^2\) (exact, signature) \(=\tfrac32-\delta W\) | 1.481216 | 1.475945 |

Corrections to the peer record. A02's Step-48 checks quoted "\(4D_W\approx0.07513\), \(4\Delta V\approx0.07080\)". Those numbers are \(4\delta W\) and \(48\,\Delta V_{\rm profile}\), the two terms of the equivalent identity \(8\pi^2-P(\hat g)=4\delta W-\tfrac43\Delta V\) (Ric=−g scale). In A02's own variables, \(4D_W=0.2167\) and \(4\Delta V=0.2124\). The Yamabe excess per cell is \(\Delta V/2\pi^2=0.2124\), about 49 times the minimum \(1-c=0.00434\) required by Corollary Y1. Both the LeBrun inequality and Theorem Y hold with slack about 0.2 per cell, so the actual cells convert only about 2% of their free Yamabe excess into saving. The formal common mode converts essentially all of it (A02: it saturates (Y-LeB)). The real cells are therefore far from the extremal regime of the field inequalities.

The \(\mu_{\min}\) eigenvector of \(W^+_{\hat g}\) lies in the Kähler/harmonic-form slot (\(e^{0f}+e^{gh}\)) everywhere except a bolt layer \(x\in[0.03,0.0315]\) of profile volume \(5.3\times10^{-6}\cdot8\pi^2\). In this layer the slot-0 eigenvalue of the profile metric \(g\) rises to \(-1.12\) (CH value \(-4\)); in the \(s=-4\) Yamabe scale the corresponding values are about \(-0.187\) and \(-2/3\). The Yamabe factor is \(u_{\rm bolt}=1.000315\), and \(u-1\) is below \(10^{-8}\) at the collar.

## 3. What this changes

* The O11 lower theory is now organized by the free Yamabe excess. Every saving must satisfy \(8\pi^2k-P\le4\Delta V_{\rm free}-16\pi^2\sum|e_i|-\text{LeB}\). Kähler cells have \(\Delta V_{\rm free}\approx0\) and pay the period linearly. Perpendicular cells have zero period and use \(\Delta V_{\rm free}\) at about 2% efficiency. The field inequalities control the saving only through \(\Delta V_{\rm free}\), which is not itself bounded by \(O(k)\). A tariff \(P\ge8\pi^2ck\) therefore needs an independent geometric bound on the saving relative to \(k\). The useful structure is a joint bound on saving and free Yamabe excess, for example \(4\Delta V_{\rm free}\le C(P+\text{collar flux})\) on CH-close regions. A bound on the efficiency \(\kappa=(8\pi^2k-P)/(4\Delta V_{\rm free})\) alone is neither necessary nor sufficient. \(\kappa\) measures how far a given metric lies from the field-extremal regime. The formal common mode shows that no pointwise field inequality can do this. The measured \(\kappa\approx0.02\) on the localized cells is an upper construction datum, not a lower bound.
* Constructive consequence. The cell saving is the small difference \(4\delta W-\tfrac43\Delta V\). Better cells have no ledger obstruction: the field inequalities permit savings roughly fifty times larger at the same Yamabe excess. Any obstruction must come from the Einstein/Bianchi structure, not from \(W^+\)-only field estimates. The \(\int\Psi\) measurement answers A02's request (a): \(2\int\Psi=0.0265<4\Delta V-\text{saving}\), with no tension.
* Rotations. By Theorem 43.2, the Step-41 symplectic rotations with period \(p\) must keep, in \(8\pi^2\) units and to first order, \(4\Delta V\ge\text{saving}+\text{LeB}+12|p|/\pi\) (equivalently \(4\Delta V_{\rm free}\ge\text{saving}+\text{LeB}+6|p|/\pi\), the other \(6|p|/\pi\) being the period-forced excess \(8\pi^2\Pi\)). The available slack 0.204 admits \(|p|\lesssim0.053\) (bolt rotation \(|\psi|\lesssim0.077\)) before the even variation must supply additional excess. This is compatible with all Step-41 data, where \(|p|\le0.0035\).

## 4. Ricci-flow consequence of an Einstein gap (adopted sources: family 351 Thm 1.1; Ishida Props 3, 5)

**Theorem 43.5.** Let \(M\) be closed with \(Y(M)<0\) and \(\alpha(M)>0\). Then every maximal volume-normalized Ricci flow on \(M\) has unbounded scalar curvature on its maximal interval.

*Proof.* Volume-normalized flow \(\partial_tg=-2\operatorname{Ric}+\tfrac12\bar s g\) with \(P=\int|\operatorname{Ric}^\circ|^2\), \(L_s=\int(s-\bar s)^2\), \(S=\int s^2\), fixed \(V\). (i) Immortal, \(|s|\le C\): direct differentiation with the moving volume form gives \(\bar s'=2P/V-L_s/(2V)\). Ishida's Proposition 5 and the bounded-scalar argument give a uniform negative bound for \(\min s\) when \(Y<0\), and time-integrability of the scalar oscillation. Bounded \(s\) upgrades this to \(\int_0^\infty L_s<\infty\), and then \(\int_0^\infty P<\infty\) because \(\bar s\) is bounded. So there are \(t_j\to\infty\) with \(P+L_s\to0\). Since \(S\ge Y(M)^2>0\) and \(E=(4P+L_s)/(P+S/4)\), we get \(E(g(t_j))\to0\), contradicting \(\alpha>0\). (ii) Finite maximal time, \(|s|\le C\): the normalization factor stays bounded on a finite interval, so the corresponding unnormalized flow has bounded scalar curvature up to a finite time. By the four-dimensional bounded-scalar extension theorem (family 351, Theorem 1.1, read in Step 41: a closed four-dimensional Ricci flow with scalar curvature uniformly bounded up to a finite time extends smoothly past that time on the same manifold), it extends, contradicting maximality. ∎ The immortal branch uses only the classical inputs. The finite-time branch is exactly as strong as that external smooth-extension statement; an orbifold or weak continuation would not suffice.

Applicability: pure-handle manifolds \(X\#\ell(S^1\times S^3)\) in the established range, and the linear-window families where an all-metric lower theorem gives \(\alpha>0\) and the monopole input gives \(Y<0\). It also applies to any future O11 tariff family. The theorem is one-way: \(\alpha=0\) (for example the Dehn-twist bundle) yields neither a bounded-scalar flow nor an Einstein limit. No monopole branch needs to be followed along the flow.

## 5. Open items carried forward

* \(\Lambda\) in Remark 43.4. It needs Yamabe solves on non-diagonal rotated metrics.
* The pointwise location of \(W^-\) in cells and collars. Only the total \(\tfrac32-\delta W\) is computed here.
* O10: the Gibbons–Hawking charged-tangent matching question (does closing a tangent with \(\int|\nabla v|^2\propto\ell^2\) force an order-\(\ell^2\) residual?) was not addressed in this Step.
