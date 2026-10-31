# Step 27 — Chiral Euler transgressions, sharp blow-up/neck charges, and the small-bolt Einstein structure

Session S1003A02, Agent2. Conventions: diagonal Bianchi-IX metrics
\(g=dt^2+a^2\sigma_1^2+b^2\sigma_2^2+c^2\sigma_3^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\), \(\int_{S^3}\sigma_{123}=2\pi^2\),
\(W=abc\), \(\widehat P=P/(8\pi^2)=\int W|\mathrm{Ric}^\circ|^2dt/4\). Block norms \(B_A=\operatorname{tr}W_A^2\), \(B_B=\operatorname{tr}W_B^2\)
of the two chiral \(3\times3\) Weyl blocks are taken from the independent Cartan module
`Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py`, in the convention of `verify_euler_flux_identity.py`
(\(\frac1{4\pi^2}\int|W|^2\leftrightarrow\int W(B_A+B_B)/2\,dt\)).

Scripts and data: `workspace/scripts/chiral_flux_identity.py` → `workspace/data/chiral_flux.json`;
`workspace/scripts/chiral_flux_models.py` → `workspace/data/chiral_flux_models.json`;
`workspace/scripts/small_b_separatrix_fit.py` → `workspace/data/small_b_separatrix_fit.json`;
new fate records `workspace/data/ach_fate/fate_b0.1.json`, `fate_b0.14.json`.

## 1. The chiral transgression theorem

Step 26 found the Euler flux \(\mathfrak b\) with \(\widehat P(C)=\Delta\mathfrak b+\frac1{4\pi^2}\int_C|W|^2+\frac1{96\pi^2}\int_Cs^2\).
The Euler flux alone cannot see which Weyl chirality is created or deleted, and that is exactly the information
that controls blow-up cells (Theorem C: the cost channel is \(4\Delta W_+\)). The missing object is the signature
transgression.

**Theorem X (chiral transgressions).** Let \(p_i=a_i'\), \(\gamma_i=(a_j^2+a_k^2-a_i^2)/(a_ja_k)\). There is an explicit
scale-invariant polynomial \(\mathfrak s\) in \(p_i\) with coefficients rational of degree zero in \(a_i\)
(the exact formula is the field `S` of `data/chiral_flux.json`, normalized here by \(\mathfrak s=S-6\); the raw JSON `bA,bB` fields use the unshifted `S`, so the normalized charges are `bA+6,bB-6`) such that
\[
\mathfrak s'=\tfrac12W(B_A-B_B)
\]
identically on all 2-jets. Put \(\mathfrak b_\pm=\mathfrak b\mp\mathfrak s\). Then for every diagonal annulus \(C=[t_0,t_1]\)
\[
\boxed{\ \widehat P(C)=\mathfrak b_\pm(t_1)-\mathfrak b_\pm(t_0)+\frac1{2\pi^2}\int_C|W^\pm|^2+\frac1{96\pi^2}\int_Cs^2\ }
\tag{1.1}
\]
where \(W^+\) is block \(A\), the block that carries the Kähler Weyl curvature of complex hyperbolic space in this frame.

*Proof.* `chiral_flux_identity.py` solves the linear system for a general 84-term ansatz
(\(\sum_{|\alpha|\le3}p^\alpha\cdot\) polynomial in \(\gamma\) of degree \(\le3-|\alpha|\)) against the Cartan-derived
\(W(B_A-B_B)/2\). The solution is unique up to the additive constant; the symbolic residual of \(\mathfrak s'\) is \(0\).
Both chiral identities (1.1) are then verified with exact residual \(0\) against the independent
\(|\mathrm{Ric}^\circ|^2\) and \(s\) of the Cartan module. \(\square\)

The normalization \(\mathfrak s=0\) at a smooth centre is the one for which (1.1) is the localization of the
Hitchin–Thorpe densities \(4\pi^2(2\chi\pm3\tau)=\int(2|W^\pm|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)\) (up to the factor 2 in
\(\widehat P\)): on a closed manifold \(\widehat P=\frac1{2\pi^2}\int|W^\pm|^2+\frac1{96\pi^2}\int s^2-(2\chi\pm3\tau)\).

### Charges (exact, `chiral_flux.json`, `chiral_flux_models.json`)

| orbit type | \(\mathfrak b\) | \(\mathfrak b_+\) | \(\mathfrak b_-\) |
|---|---|---|---|
| smooth centre (round, \(a_i\sim t\)) | 2 | 2 | 2 |
| regular bolt of \(O(-1)\) (any \(b\), any triaxial jet) | 4 | 1 | 7 |
| biaxial or controlled near-biaxial Hopf-collapsed Berger orbit, fibre \(\varepsilon\to0\), bounded normalized jets | 0 | −2 | 2 |
| CH orbit at radius \(t\) (\(\mathrm{Ric}=-6\)) | \(2-6\sinh^4t\) | \(2-9\sinh^4t\) | \(2-3\sinh^4t\) |
| real-hyperbolic orbit (any normalization) | \(\mathfrak b_{H}\) | \(\mathfrak b_H\) | \(\mathfrak b_H\) |

The bolt row is \(2\chi\pm3\tau\) for the disc bundle with \(\chi=2,\tau=-1\): the frame orientation in which CH
is Kähler with \(W^+\neq0\) is automatically the orientation in which the bolt has self-intersection \(-1\). This is
the blow-up orientation, confirmed independently by the frame, not imposed. The collapsed Berger value is exact:
\[
\mathfrak s=2+\frac{\varepsilon^2}{R^2}\Bigl(U^2-2UV+V^2-4\Bigr)+\frac{2\varepsilon^4}{R^4},\qquad
\mathfrak b=-\frac{\varepsilon}{R}\Bigl(U^2V-4V\Bigr)+O(\varepsilon^3/R^3)
\]
for \(a=\varepsilon\) (fibre), \(b=c=R\), \(b'=c'=U\), \(a'/a=V/R\); the formula is symmetric under the choice of the
collapsing slot.

**Collapse asymmetry.** Under Hopf collapse with bounded normalized geometry the Euler flux tends to \(0\), but the
signature transgression tends to the nonzero adiabatic value \(\mathfrak s\to2\). For unrestricted anisotropic collapsed jets the charge acquires shear terms and need not equal \((-2,2)\). This is the cohomogeneity-one form of
the fact used by Cheeger–Tian: the Chern–Gauss–Bonnet boundary term vanishes on collapsed boundaries with
bounded geometry, while the \(\eta\)/Chern–Simons term does not. The chiral fluxes therefore assign a definite
charge \((-2,2)\) to every collapsed neck; a collapsed neck is invisible to \(\mathfrak b\) but not to \(\mathfrak b_\pm\).

### Model checks

* **Burns** (\(a=b=r,\ c=r\sqrt{1-m/r^2},\ dt=dr/\sqrt{1-m/r^2}\)): exactly \(s=0\), \(B_A=0\) (ASD in the blow-up
  orientation), \(B_B=24/r^8\), \(|\mathrm{Ric}^\circ|^2=16/r^8\). Charges: \(\mathfrak b_+\) goes from \(1\) to \(2\), \(\mathfrak b_-\) from \(7\) to \(2\);
  \(\int WB_A=0\), \(\int WB_B=6\). Hence \(\widehat P(\mathrm{Burns})=2-1=1\) with every non-flux term in the \(+\) identity zero.
* **Taub-bolt** (\(a=b=2\sqrt{r^2-n^2}\), \(c=4n\sqrt V\), \(V=(r^2-\frac52nr+n^2)/(r^2-n^2)\), bolt \(r=2n\)): Ricci-flat, regular
  on \(O(-1)\) in the blow-up orientation. With \(n=1\), \(B_A=\frac{243}{8(r+1)^6}\) and \(B_B=\frac3{8(r-1)^6}\). The charges run from \((1,7)\) at
  the bolt to the collapsed value \((-2,2)\) at the ALF end, and the quadratures give \(\int WB_A=3.000\), \(\int WB_B=5.000\).
  So there is no orientation obstruction: Taub-bolt is a legitimate zero-cost core for the \((-1)\)-class, and it
  converts the bolt charge into the collapsed-neck charge with \(\frac1{2\pi^2}\int|W^+|^2=3\) and \(\frac1{2\pi^2}\int|W^-|^2=5\).
* CH, H\(^4\), Euclidean profiles are exact closed forms (table above). In H\(^4\) both blocks vanish and \(\mathfrak s\equiv0\).

## 2. Consequences for blow-up cells

From (1.1), every non-flux term is nonnegative, so for every \(t_0<t_1\)
\[
\widehat P[t_0,t_1]\ \ge\ \mathfrak b_+(t_1)-\mathfrak b_+(t_0)+\frac1{96\pi^2}\int_{[t_0,t_1]}s^2,
\qquad\text{and the same for }\mathfrak b_-.
\tag{2.1}
\]
The total upward variation of each chiral flux along a cell is at most \(\widehat P\).

**Corollary X1 (sharp bubble inequality, Burns-extremal).** For any diagonal metric on the disc bundle of
\(O(-1)\) and any orbit \(t\),
\[
\widehat P[0,t]\ \ge\ \mathfrak b_+(t)-1 .
\]
If the orbit at \(t\) is \(C^1\)-close in scale-normalized sense to a round Euclidean sphere, then \(\mathfrak b_+(t)=2-O(\delta)\) and
\(\widehat P[0,t]\ge1-O(\delta)\). Burns attains equality at every \(t\), since \(W^+\equiv0\) and \(s\equiv0\); its total is \(\widehat P=1\). This replaces Lemma Q′:
no almost-flatness of an annulus is needed, only the 1-jet of a single orbit, and the constant is sharp with an
explicit extremal. It also states the mechanism of Burns cost: the whole \(8\pi^2\) is the \(+\)-chiral charge
difference \(2-1\), paid with \(W^+\equiv0\) and \(s\equiv0\).

**Corollary X2 (nothing in a subthreshold cell is round).** If \(\widehat P(g)<1\) then \(\mathfrak b_+(t)<1+\widehat P<2\) for all \(t\). No orbit
of a subthreshold cell is close to a round Euclidean sphere, whatever its scale. A CH orbit at radius \(\tau\) has
\(\mathfrak b_+=2-9\sinh^4\tau\); compatibility requires \(\sinh^4\tau\ge(1-\widehat P)/9\), so sufficiently small positive CH radii are also excluded. This is
the global form of the statement that cheap cells must be glued into curved bulk.

**Corollary X3 (decollapse price).** Passing from a Hopf-collapsed orbit (\(\mathfrak b_+\approx-2\)) to an orbit with
\(\mathfrak b_+=\beta\) costs at least \(\beta+2\). In particular:
* to a round Euclidean orbit: at least \(4\);
* to a CH-like orbit of radius \(\tau\): at least \(4-9\sinh^4\tau\), which exceeds \(1\) for \(\sinh\tau<3^{-1/4}\), i.e. \(\tau<0.700\).

Thus a subthreshold cell with a Taub-bolt-type collapsed core cannot open into CH-like geometry inside CH radius
\(0.70\). It must remain collapsed out to scale one, or open through geometry that is not CH-like.

**Corollary X4 (bolt bubbles).** Let \(g_n\) be diagonal cells with \(\widehat P(g_n)\le1-\eta\) and bolt radius \(b_n\to0\). Rescaled by \(b_n\), any
noncollapsed limit region is a complete diagonal metric on \(O(-1)\) with \(s\equiv0\) and \(\widehat P\le1-\eta\), so its far orbits
satisfy \(\mathfrak b_+\le 2-\eta\) and cannot be asymptotically round. Its end is therefore not ALE. If it is Ricci-flat (the
\(\widehat P\to0\) case) with Hopf-collapsed ALF end, the charge balance is exactly the Taub-bolt one: \(\frac1{2\pi^2}\int|W^+|^2=3\),
\(\frac1{2\pi^2}\int|W^-|^2=5\). The scale-separated ALE bubble is excluded for every inner geometry, recovering
Step 25's exclusion with the sharp constant.

### Relation to Theorem C and to the absolute cell channel

Applying (1.1)\(_+\) to the whole exact-CH-ended cell and subtracting the CH ball (charges \(1\) versus \(2\) at the origin)
gives, for \(s\equiv-24\),
\[
\widehat P_{\rm cell}=1+\frac1{2\pi^2}\Delta_{\rm ren}\!\int|W^+|^2+12\,\Delta_{\rm ren}\!\int W\,dt
\;=\;1+\frac{4\Delta W_++48\,\mathrm{RV}}{8\pi^2},
\]
which is Theorem C at the Yamabe-normalized representative. The \(-\) identity gives the relative-signature form
\(\widehat P_{\rm cell}=-5+\frac1{2\pi^2}\int|W^-|^2+48\mathrm{RV}/(8\pi^2)\). Theorem X localizes both: the cell channel is now the
running quantity
\[
\Pi_+(t)=\mathfrak b_+(t)-1+\frac1{2\pi^2}\int_0^t|W^+|^2+\frac1{96\pi^2}\int_0^ts^2=\widehat P[0,t],
\]
and the question \(p_{1,0}>0\) asks whether the \(+\)-charge can be driven from \(1\) to the CH profile with a total deletion of
\(\int|W^+|^2+\frac1{48}\int s^2\) relative to the ball approaching \(2\pi^2\) (in the \(\frac1{2\pi^2}\) normalization, one unit).

## 3. The small-bolt Einstein regime: Taub-bolt core, collapsed AdS-Taub-NUT neck, saturation

New fate enumerations at \(b=0.14\) and \(b=0.1\) (`fate_b0.14.json`, `fate_b0.1.json`) have the same four-transition topology
as \(b=.2,.35,.8,2,20\): one mirror perpendicular ACH1/ACH2 pair and two remote SING/OTHER boundaries; ACH3 deviations
stay above \(1.29\). At \(b=0.14\), \(d_*=4.4934\times10^{-9}\), closest ACH approach \(1.8\times10^{-3}\), \(\rho\approx5.809\). At \(b=0.1\) the separatrix is at
\(|d|\lesssim3\times10^{-13}\), at the floating resolution of the grid; its readout (\(\rho\approx8.1\), closest approach \(0.31\)) is not resolved.

**Mechanism.** As \(b\to0\) the rescaled biaxial Einstein bolt solution converges to Taub-bolt (§1), whose ALF circle
has length parameter \(c\to4n\) with \(n=b/(2\sqrt3)\). At scale one the circle remains collapsed and the solution follows the
\(n\to0\) Λ-Taub-NUT form, \(c\simeq4n\cosh(\sqrt2\,t)\), \(a\simeq b\simeq\sinh(\sqrt2t)/\sqrt2\) (Ric \(=-6g\)). On a Berger orbit with fibre
\(c=\varepsilon\), the triaxial mode \(q=\log(a/b)\) satisfies, from the exact Ricci formulas,
\[
\mathrm{Ric}_{aa}-\mathrm{Ric}_{bb}=-(q''+\theta q')+\frac{16}{\varepsilon^2}q+O(q/R^2,q^2),
\]
so the Einstein condition makes it grow at rate \(4/\varepsilon\). The separatrix needs the initial anisotropy to be amplified
to order one exactly once, so
\[
\log\frac1{d_*}\simeq4\int\frac{dt}{c}=\frac{4}{4n}\int_0^\infty\frac{dt}{\cosh\sqrt2t}=\frac{\pi}{2\sqrt2\,n}
=\frac{\pi\sqrt{3/2}}{b}=\frac{3.84765}{b},
\]
up to logarithmic corrections from the bolt region where \(c\sim t\).

**Test.** A fit of \(\log d_*=-\kappa/b+\gamma\log b+c_0\) to \(b=.14,.2,.35\) gives \(\kappa=3.8543\), versus the predicted \(3.8476\) (0.17%), with
\(\gamma=-2.90\). With \(\kappa\) fixed to the prediction, the residuals are \(\le2\times10^{-3}\) and \(\gamma=-2.871\). The prediction also places \(d_*(0.1)\approx2\times10^{-13}\),
consistent with the unresolved bracket. The Rossi readout satisfies \(\rho b=0.983,0.848,0.813\) at \(b=.35,.2,.14\). This is
consistent with \(\rho\simeq c_*/b\), \(c_*\approx0.8\): the contact plane of the eventual ACH end (slots \(b\) and \(c\) when slot \(a\) becomes
the CH fibre) inherits the ratio between a base direction and the collapsed Taub-bolt circle, frozen at the saturation
radius where \(W\) is already large (Lemma P).

**Consequences.**
1. The small-\(b\) end of the Einstein branch has \(\rho\to\infty\), so \(\rho_\infty(b)\neq1\) there is explained by a matched
   three-region structure: a Taub-bolt core at scale \(b\), a collapsed Λ-Taub-NUT neck with circle \(\simeq4n\cosh\sqrt2t\), and a
   saturation/ACH region at scale one. A proof needs a rigorous version of this matching (Fenichel/exchange-lemma
   type estimates along the collapsed slow manifold) together with the large-\(b\) law \(\rho\sim1.343b\). Validated interval
   computation then covers the compact middle range.
2. The cell-side collapsed branch has the same geometry. A cheap cell with a Taub-bolt-type core reaches charge
   \((-2,2)\) for free, but then (X3) cannot open into CH-like geometry before CH radius \(0.70\). If it stays collapsed, its
   natural Einstein continuation lands on Rossi \(\rho\sim0.8/b\gg1\), and Lemma P charges the CR correction wherever \(W\) is large. A
   cheap standard-CR cell along this branch must therefore perform the CR correction inside the collapsed neck itself,
   where \(\int dt/W\) is large. That is exactly where the Einstein dynamics of \(q\) is exponentially unstable with rate
   \(4/\varepsilon\), and the free drift \(F\) of Lemma P is of size \(q/\varepsilon\). The residual collapsed problem is therefore a
   single, well-posed linear-quadratic control problem: steer the unstable \(q\)-mode on the collapsed slow manifold so
   that its saturated value gives standard CR, with cost \(\int W\,(\mathrm{Ric}_{aa}-\mathrm{Ric}_{bb})^2/8\). Its value as \(b\to0\) is the
   cell-side quantity that decides this branch.

## 4. Cheeger–Tian and the closed-manifold transfer

The retrieved account of Cheeger–Tian (Ge–Jiang, arXiv 1707.05511, Theorem 1.1 and Theorem 3.4 [ChTi06, Li])
gives ε-regularity for Einstein 4-manifolds without a volume bound, \(\int_{B_r}|\mathrm{Rm}|^2\le\varepsilon\Rightarrow|\mathrm{Rm}|\le Cr^{-2}\) on
\(B_{r/2}\). The key curvature estimate (Theorem 3.4) needs a **pointwise** Ricci bound \(|\mathrm{Ric}|\le3\), and its proof uses
chopping/N-structures, the Chern–Gauss–Bonnet transgression and almost-cone rigidity. Ge–Jiang §5.2 shows that the
estimate fails for critical metrics, \(\Delta\mathrm{Ric}=\mathrm{Rm}*\mathrm{Ric}\): scalar-flat Kähler products \(N_a\times S^2_a\), with \(N\) a cusped
hyperbolic surface, have arbitrarily small local \(L^2\) curvature and curvature \(a^{-2}\). Remark 5.4 there notes that bounded
Ricci is necessary.

The transfer to closed near-minimizers is therefore precise. An \(L^2\) Ricci-defect bound alone cannot yield
Cheeger–Tian regularity; the Ge–Jiang examples are critical metrics, but they are not near-Einstein in
\(\widehat P\), so they do not contradict a \(\widehat P\)-small version. The usable statement has the form of Theorem X: the
Euler transgression vanishes on collapsed boundaries with bounded geometry, while the signature transgression keeps
an adiabatic charge (here \(\mathfrak s\to2\)). In the diagonal class, cohomogeneity one replaces the pointwise Ricci bound,
because (1.1) holds exactly with no regularity input. A closed-manifold analogue must supply either a pointwise
Ricci bound on the collapsed region (for example from a selection principle) or a substitute for the 1-dimensional
structure, such as an F-structure along which the transgressions can be integrated.

## 5. Status

Proved this step (exact symbolic): Theorem X, the charge table, the Burns and Taub-bolt charge balances, and
Corollaries X1–X4 as consequences of (1.1).

Numerical and asymptotic, not yet a proof:
* the small-\(b\) law \(\log(1/d_*)\sim\pi\sqrt{3/2}/b\), with its derivation from the collapsed \(q\)-mode;
* \(\rho b\to c_*\approx0.8\);
* branch topology at \(b=0.1,0.14\).

Open:
* rigorous matching for \(b\to0\) and \(b\to\infty\);
* the collapsed-neck CR-control problem of §3(2);
* the high-shear (Kasner-type) connector of Step 26, for which (1.1) gives no obstruction while \(\mathfrak b\) decreases;
* face no-return;
* compact-state control near the bolt.
