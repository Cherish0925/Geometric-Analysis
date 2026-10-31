# Step 5 — The slice charge of Bianchi-IX cells, the zero-flux certificate, and the inner AE threshold

Session S1003A01, Step 5 (Agent2, Explore). Conventions: I54/I55 cell normalization (CH collar \(F_{CH}=1+r^2/6\), \(\mathrm{Ric}_{CH}=-g\), \(s_{CH}=-4\)); \(|W^+|^2\) is the LeBrun/operator norm (CH value \(2/3\)); orientation is the complex one, \(\tau(\mathcal O(-1))=-1\). Cell density
\[
\mathfrak F=\frac{(s+3)^2}{3}+1+4|W^+|^2\ \ (\mathfrak F_{CH}=4),\qquad |\mathrm{Ric}+g|^2=\mathfrak F-8\pi^2(2e+3p)
\]
pointwise, where \(\chi=\int e\), \(\tau=\int p\) (pure Chern–Weil algebra; it gives I54's \(J-8\pi^2q=\int\mathfrak F-4d\)).

Scripts: `scripts/bianchi_transgression.py` (Cartan curvature, Euler + Pontryagin forms, exact antiderivative), `transgression_values.py`, `transgression_cell.py`, `transgression_sign.py`, `transgression_triaxial.py`, `transgression_structure.py`, `transgression_closed_form_check.py`, `profile_charge.py`, `plot_slice_charge.py`, `kahler_flux_check.py`. Data: `data/transgression/` (`G_formula.txt`, `triaxial_Qstar.txt`, `profile_charge_lines.jsonl`, `zero_flux_summary.json`). Figure: `figures/slice_charge_profiles.png`.

## 1. Exact slice charge for every diagonal Bianchi-IX metric

Let \(g=dt^2+a^2\sigma_1^2+b^2\sigma_2^2+c^2\sigma_3^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\), ' = d/dt. Put \(e^{2w}=a/b\), \(z=c/\sqrt{ab}\),
\[
p_+=\frac{b a'-c+(a^2-b^2)/c}{\sqrt{ab}},\qquad p_-=\frac{a b'-c-(a^2-b^2)/c}{\sqrt{ab}} .
\]
**Theorem A (slice charge).** For slices \(t_1<t_2\),
\(8\pi^2\int_{t_1<t<t_2}(2e+3p)\,dV=\mathcal T(t_2)-\mathcal T(t_1)\), where
\[
\boxed{\frac{\mathcal T}{8\pi^2}=Y^2+\Pi,\quad
Y=c'-2\cosh2w+z^2+\tfrac12p_+p_-,\quad
\Pi=e^{2w}p_+^2+e^{-2w}p_-^2-\tfrac14(p_+p_-)^2 .}
\]
\(\mathcal T\) depends only on first-order slice data and is scale invariant.

Verification: the antiderivative was obtained symbolically from the Cartan curvature and checked identically (`check = 0`); the closed form agrees with it to \(9\times10^{-14}\) on \(10^5\) random slices. Values: flat round slice \(0\); smooth \(\mathcal O(-1)\) bolt \(8\pi^2\) (so \(\mathcal T(\text{bolt})-\mathcal T(\text{flat})=8\pi^2\) = the \(2\chi+3\tau=-1\) jump); the opposite orientation gives \(-40\pi^2\) (\(\mathcal O(+1)\), \(2\chi+3\tau=5\)); CH collar \(\mathcal T=2\pi^2R^4=4d\) exactly; Taub–NUT/ALF slices (\(c\to\)const, \(a'=b'=1\)) give \(32\pi^2\), matching \(\chi=1,\ \tau\)-density \(=\tfrac23\) of the self-dual Taub–NUT; flat-cone Berger slices \(c=t/k\) give \(8\pi^2(k-1)^2(4k^2+5k+2)/k^4\). As an independent test against the Ricci code: for every conformally Kähler numerical cell (\(w=0\)), \(d\mathcal T/dr+|\mathrm{Ric}+g|^2dV/dr=[(s_G+3)^2/3+1]dV_G/dr+(s_K^2/6)dV_K/dr\) holds with finite-difference relative error \(\le1.2\times10^{-3}\) (typically \(10^{-5}\)).

Meaning of the pieces. \(p_+=p_-=0\) iff the slice is Kähler for \(\omega=c\,dt\wedge\sigma_3+ab\,\sigma_1\wedge\sigma_2\) (\(p_++p_-=2\delta\), \(\delta\) the closure defect \((ab)'/2\sqrt{ab}-z\); \(p_+-p_-=2\kappa\), \(\kappa\) the integrability defect). For U(2)-Kähler slices, \(Y=-A\) where the Ricci form is \(\rho=d(A\sigma_3)\) (`kahler_flux_check.py`: \(A/Y=-1\) identically). Thus **\(\mathcal T=8\pi^2(\text{Ricci-form flux})^2+8\pi^2\cdot(\text{Kähler defect})\)**: the Chern–Weil charge of a Kähler slice is the square of its \(c_1\)-flux, which is the \(c_1^2=2\chi+3\tau\) transgression. \(\Pi\ge0\) whenever \(|p_+p_-|\le8\) (AM–GM); \(\mathcal T\) is unbounded below only for strongly non-Kähler slices (\(|p_+p_-|>8\)).

## 2. Localized identities

For any slice \(\Sigma_\rho\) of a cell \(C\) with exact CH collar:
\[
\int_{\rm in}|\mathrm{Ric}+g|^2=8\pi^2+\int_{\rm in}\mathfrak F-\mathcal T(\rho),\qquad
\int_{\rm out}|\mathrm{Ric}+g|^2=\int_{\rm out}\mathfrak F-4d+\mathcal T(\rho).
\]
Since \(\mathfrak F\ge1\), every slice certifies
\[
J-8\pi^2\ \ge\ \mathrm{Vol}_G(\mathrm{in}_\rho)-\mathcal T(\rho)\quad\text{and more sharply}\quad J-8\pi^2\ge\int_{\rm in}\mathfrak F-\mathcal T(\rho). \tag{2.1}
\]
(The second form is trivial if \(\int_{\rm in}\mathfrak F\) is unknown; the content is that \(\mathcal T\) is an explicit function of slice data.)

## 3. The zero-flux certificate

\(Y(\text{bolt})=-1\) (bolt: \(z\to0,\ c'\to1,\ w\to0,\ p_\pm\to0\)) and \(Y(\text{collar})=R^2/2>0\). By continuity there is a slice \(t_*\) with \(Y(t_*)=0\), at which \(\mathcal T=8\pi^2\Pi\).

**Theorem C (zero-flux threshold).** For every \(C^2\) diagonal one-bolt cell in which the collapsing bolt circle is the \(\sigma_3\) slot of the CH Kähler fibre (this is the I54/I55 triaxial conformal class, any \(w,\phi\)), and every zero \(t_*\) of \(Y\),
\[
J\ \ge\ 8\pi^2+\int_{\mathrm{in}(t_*)}\mathfrak F\,dV-8\pi^2\Pi(t_*)\ \ge\ 8\pi^2+\mathrm{Vol}_G(\mathrm{in}(t_*))-8\pi^2\Pi(t_*).
\]
Corollaries. (i) If \(G\) is itself Kähler (\(\Pi\equiv0\)), \(J\ge8\pi^2+\mathrm{Vol}(\mathrm{in}(t_*))>8\pi^2\) — an elementary one-line threshold (weaker than I54 Theorem 1's \(K\), but local). For the U(2) Kähler family \(Y=-\mu/r^2+r^2/2+\dots\), zero at \(r_*\approx(2\mu)^{1/4}\). (ii) A subthreshold cell must have \(8\pi^2\Pi(t_*)>\int_{\rm in}\mathfrak F\ge \mathrm{Vol}\) at **every** zero of the flux: each zero-flux slice must be non-Kähler by an amount exceeding the interior energy.

Numerics (122 cells: 108 positive-q runs of Step 4 and 14 near-optimal sweep1 runs; `zero_flux_summary.json`). Every cell except one unconverged \(\mu=.6,R=.8\) run (\(j\approx8\times10^4\), zero in the excluded endpoint layer) has zero-flux slices; at the best zero, \(8\pi^2\Pi/\int_{\rm in}\mathfrak F\le0.58\), so Theorem C certifies \(J\ge8\pi^2\) for all of them. The **first** zero does not always suffice (2 high-cost oscillating profiles have ratio 1.03, 1.02 there). Near-optimal cells place \(\mathcal T\approx0\) (\(\le2\times10^{-4}\cdot8\pi^2\)) at \(r\approx(2\mu)^{1/4}\) even at \(\mu=0.1\): they split into an inner piece paying the whole \(8\pi^2\) and a CH-like outer piece.

**Conjecture Z (diagonal, aligned slot).** Every diagonal filling of an \(\mathcal O(-1)\) bolt has a zero-flux slice with \(8\pi^2\Pi(t_*)\le\int_{\rm in}\mathfrak F\). This localizes and implies the diagonal-class cell conjecture \(j\ge4\) for all \(\mu,R\) (not C1). Its content is a boundary-to-interior inequality: Kähler defect of the slice controlled by interior \(4|W^+|^2+(s+3)^2/3+1\). Candidate mechanism: for \(G=e^{2\phi}K\), \(\delta=\sqrt F\,r\phi'\) and \(\kappa=\kappa_K\); interior \((s+3)^2\) controls \(\Delta\phi\) (Hardy type, \(\phi=0\) at the bolt), interior \(W^+\) controls \(\kappa\).

## 4. Inner AE threshold in the diagonal class (Step-4 (3) closed)

Rescale \(r=\sqrt\mu x\). On \([1,X]\), the pure-Ricci form of §2 is exact:
\(\int_{1}^{X}|\mathrm{Ric}|^2dV=8\pi^2+\int_1^X(\hat s^2/3+4|\hat W^+|^2)dV-\mathcal T(X)\).
If the profile has finite \(\int|\mathrm{Rm}|^2\) and terminal limits \((\mathcal F,W,\Phi)\to(1,0,\Phi_\infty)\), then \(\mathcal T(X_k)\to0\) along a sequence: \(a''/a,b''/b,c''/c\) are sectional curvatures, so \(d(a',b',c')/d\log t\in L^2(d\log t)\); the terminal values force the averages of \(a',b',c'\) on \([X,2X]\) to 1, hence slice data \(\to\) flat round and \(\mathcal T\to0\). Therefore
\[
\mathcal J_\infty=4+\frac1{2\pi^2}\int(\hat s^2/3+4|\hat W^+|^2)\,dV\ \ge4,
\]
i.e. \(\widehat{\mathscr R}-\vartheta(4-\vartheta)=\frac1{2\pi^2}\int(\hat s^2/3+4|\hat W^+|^2)\ge0\) for all finite-amplitude \(W\) and all \(\vartheta\). This is the manuscript's `webvar:ae-cost` (\(P=8\pi^2b_2+4W^++S/12\)) realized with an explicit end term. If instead the end is ALF (Hopf fibre of bounded length), \(\mathcal T_{\rm end}=32\pi^2\) and the core identity reads \(\int|\mathrm{Ric}|^2=-24\pi^2+\int(\hat s^2/3+4|\hat W^+|^2)\): collapse of the fibre moves four charges of transgression across the neck, the explicit form of the "topology distributed across levels" phenomenon in this class. With a cell (fixed collar), the threshold as \(\mu\to0\) needs only a neck slice with \(\mathcal T\le o(1)\); no AE decay of the limit is needed, since (2.1) is exact at finite \(\mu\).

## 5. Scope, and the peer correction (message #746)

All of §3 assumes the bolt circle and the CH Kähler fibre occupy the same slot (\(\sigma_3\)). S1003A02's corrected fixed-slot computation finds that the relative orientation \(\zeta\perp\omega_{CH}\) has **zero first-order cost** (\(P/8\pi^2-1\approx0.044x_0\), margin only \(O(x_0^2)\), with \(4\Delta W^+/x_0\approx2(3\cos^2\theta-1)\), \(\Delta S/12x_0\approx2\)). Our diagonal searches (Steps 2–4) are entirely in the aligned slot \(\theta=0\), the most expensive orientation; they did not test the dangerous direction. In a perpendicular-slot diagonal cell (bolt collapsing \(\sigma_1\), CH fibre \(\sigma_3\)), \(\mathcal T(\text{bolt})=8\pi^2\) still (cyclic symmetry), but \(Y\) is singular at the bolt (\(e^{2w}=a/b\to0\)), so the zero-flux IVT is unavailable: **the zero-flux certificate is precisely a \(c_1(\omega_{CH})\)-flux argument and is evaded by the orientation that is first-order free.** The general certificate (2.1), \(J-8\pi^2\ge\mathrm{Vol}(\mathrm{in}_\rho)-\mathcal T(\rho)\), still applies to any diagonal slot assignment and should be evaluated on the peer's \(\zeta\perp\omega\) profiles (`Sessions/S1003A02/workspace/scripts/o11_perp_cell.py`).

Non-symmetric extension (route). For an arbitrary cell and separating hypersurface \(\Sigma\), \(J\ge8\pi^2+\int_{\rm in}\mathfrak F-\mathcal T(\Sigma)\) with \(\mathcal T\) the Chern–Gauss–Bonnet boundary term plus the Chern–Simons term of \(2\chi+3\tau\). In the Kähler case \(\mathcal T\) is the squared \(c_1\)-flux; for general metrics the Seiberg–Witten curvature \(iF_A/2\pi\) represents \(c_1(L)\) for every metric, suggesting a flux-square transgression with an actual-field substitute for \(\rho\). Whether the \(\zeta\perp\omega\) direction makes the monopole flux and the CH Ricci flux decouple is the natural test.

## 6. What this changes

- Step-4 inner inequality (3): proved in the diagonal class, with the end term made explicit (flat 0, ALF \(32\pi^2\)).
- Diagonal aligned-slot cell conjecture reduced to Conjecture Z (a boundary Kähler-defect vs interior energy inequality), numerically certified on all 120 analyzed cells with ratio \(\le0.58\).
- The decisive open direction for O11 is now the perpendicular orientation \(\zeta\perp\omega_{CH}\) at finite \(x_0\sim0.03\)–\(0.3\), where both first-order terms cancel and our flux mechanism is absent. A negative cell must live there (or outside SU(2)).
