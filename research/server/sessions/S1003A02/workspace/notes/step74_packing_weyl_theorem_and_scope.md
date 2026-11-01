# Step 74 — Certified Weyl saving, realized packing frontier, Kähler comparison, and scope integration

> **Erratum (Steps 86–88; package §22.6).** The capacity is a property of the given manifold, \(\Theta_*(M)=\sup_{\widehat g}2\kappa(\widehat g)/A_Y\) over negative Yamabe representatives; the notation \(\Theta_*(h)\) in (74.21) is withdrawn because no dependence on \(M\) only through \(h\) is known. Open-range positivity \(P_*>0\) is not an upper bound on capacity alone: since \(p=k-\frac43\kappa+\frac13\upsilon\), it requires uniform separation of the joint realizable pairs \((\kappa,\upsilon)\) from the Einstein locus. The signature typo \(\tau=A_Y/3\) in the proof of 74.W is corrected to \(\tau=A_Y/9\) (the value \(I_+=4\pi^2A_Y/3\) was already right). Orbifold \(S^4/\mathbb Z_2\) absorption over ball quotients is deficit-neutral and lands exactly on \(h=1/3\) (Theorem 87.O), so it is not a competitor to the cells here.

Agent4, Execute. Inputs: Step 73, Spirit #89, the exact Step-33 and Step-11 Arb certificates, Step-69 packing, Step-72 Weyl-deficit law, and the 8 October increments of the two supplied Einstein-gap references.

## 1. Corrected certified relative Weyl computation

For an exact-CH-collared one-blow-up cell, in the `Ric_CH=-6g` normalization and the session curvature-operator norm,
\[
 p-1=\frac{\Delta\int |W^+|^2}{2\pi^2}
      +\frac{\Delta\int s^2}{96\pi^2},
 \qquad p=\frac{P}{8\pi^2}.                                      \tag{74.1}
\]
Here every \(\Delta\) is cell minus the CH ball that it replaces. The frozen-cell integrator covers \(x\in[x_0,X]\). The removed CH core \(0\le x<x_0\) has
\[
 \frac1{96\pi^2}\int_{0\le x<x_0}s_{CH}^2\,dV_{CH}=3x_0^2,       \tag{74.2}
\]
so the total relative scalar term is the integrated shell term minus \(3x_0^2\). This is the correction missed by the original Step-73 JSON.

`workspace/scripts/step74_certified_weyl_saving.py` performs this subtraction inside the interval calculation and saves exact dyadic endpoints. For the authoritative \((x_0,X)=(.03,128)\) profile:
\[
 \frac{\Delta\int s^2}{96\pi^2}
 \in[0.0707969335693406631,\ 0.0707969335693407692],               \tag{74.3}
\]
\[
 \frac{\Delta\int|W^+|^2}{2\pi^2}
 \in[-0.0751342008160864399,\ -0.0751342007982264634].            \tag{74.4}
\]
Thus
\[
 \eta_{128}:=-\frac{\Delta\int|W^+|^2}{2\pi^2}
 \in[0.0751342007982264634,\ 0.0751342008160864399].              \tag{74.5}
\]
A special cell therefore loses \(4\pi^2(1-\eta_{128})\), rather than \(4\pi^2\), of the host Weyl deficit. The formal value obtained if every exceptional class can use this cell is
\[
 \frac1{3(1-\eta_{128})}
 \in[0.3604126497282353818,\ 0.3604126497351953751].              \tag{74.6}
\]
It is not a realized universal frontier.

The smaller independently certified \((.01,8)\) cell gives
\[
 \frac{\Delta\int s^2}{96\pi^2}
 \in[0.0213032806029568625,\ 0.0213032806029568703],               \tag{74.7}
\]
\[
 \eta_8\in[0.0221945778693642141,\ 0.0221945778693642228],        \tag{74.8}
\]
and the formal all-cell value \(1/[3(1-\eta_8)]\approx0.3408994527837663\). Although \(\eta_8<\eta_{128}\), its self-dual-Weyl removal per CH footprint is much better. For a CH ball with \(x=\sinh^2(r/\sqrt6)=X\), after scaling the cell from \(\operatorname{Ric}=-6g\) to \(\operatorname{Ric}=-g\),
\[
 \frac1{4\pi^2}\int_{B_R}|W^+_{CH}|^2=3X^2,
 \qquad
 \frac{\eta_8}{3\cdot8^2}\approx1.15597\times10^{-4},\quad
 \frac{\eta_{128}}{3\cdot128^2}\approx1.52861\times10^{-6}.      \tag{74.9}
\]
Thus the \(X=8\) cell is about \(75.62\) times more efficient by this footprint measure.

The old `step73_certified_weyl_saving.py` and `step73_certified_wplus_direct.py` are nonauthoritative. In `step73_certified_wplus_identity.json`, only the certified \(p\) interval and the shell integral before core subtraction remain reusable; its `fourdwp`, `delta`, `loss`, and `hcrit` fields are superseded by the Step-74 outputs.

## 2. Mixed global theorem with exact quantifiers (repaired in Step 75 after the binding verifier `trace/ttcs/results/step74_ttcs01_verifier1_integration.md`)

Notation. \(I_\pm(g)=\int|W^\pm|^2_{\rm op}\), \(d([g])=8\pi^2\chi-I_+-I_-\), \(d_*(M)=\sup_{[g]}d([g])\). In this norm \(4\pi^2(2\chi+3\tau)=S/24+2I_+-P/2\).

Let \(X_0\) be a compact ball quotient with \(\operatorname{Ric}=-g\). Fix a certified cell with CH coordinate radius \(R(X)=\sqrt6\operatorname{arsinh}\sqrt X\). Choose a preliminary normal finite cover \(X'\to X_0\) with global injectivity radius \(>2R(X)\) by the Step-69 compact-fundamental-set argument (with \(F\) a compact fundamental set and \(D=\sup_F d(x_0,\cdot)\), exclude all \(\gamma\ne1\) with \(d(x_0,\gamma x_0)\le4R+2D\)). For any further finite cover \(Y\to X'\) put
\[
A_Y=c_1^2(Y)=\deg(Y\to X_0)\,c_1^2(X_0),
\]
and let \(N\) be the number of points of a \(2R\)-separated set in \(Y\) (so the \(R\)-balls are disjoint, embedded and isometric to the CH ball).

**Smoothed support (dependency discharged).** The inherited smoothing lemma (`Skills/geometric-analysis/research/supplements/sources/20261004/step10_rigorous_subthreshold_cell_and_O11.md` §4) gives smooth \(g_\delta\) with \(g_\delta=g\) for \(x\le X-\delta\) and \(g_\delta\) exactly CH for \(x\ge X-\delta/2\); both \(g\) and \(g_\delta\) are \(C'\delta\)-close to CH in \(C^2\) on the shell \(B_\delta=\{X-\delta\le x\le X\}\), so \(|\operatorname{Ric}+6g|\le C''\delta\) there. Hence (i) the support of \(g_\delta\) never leaves the raw ball, \(R_s=R(X)\) exactly; (ii) \(|P(g_\delta)-P(g)|=O(\delta^3)\) and, because \(|s+24|\le C\delta\) on \(B_\delta\) for both metrics, \(|S(g_\delta)-S(g)|\le C\delta\cdot\operatorname{Vol}(B_\delta)=O(\delta^2)\). By the relative identity (74.1), \(\eta_\delta\to\eta\). So the raw-radius packing constants below are legitimate.

**Theorem 74.W (realized mixed Weyl frontier).** For all integers \(k\ge0\) and \(0\le n\le\min\{k,N\}\),
\[
 d_*\!\left(Y\#k\overline{\mathbb{CP}}^{\,2}\right)\ge4\pi^2\Bigl(\frac{A_Y}3-k+\eta n\Bigr),          \tag{74.10}
\]
and therefore
\[
 k<\frac{A_Y}3+\eta n\quad\Longrightarrow\quad \alpha\bigl(Y\#k\overline{\mathbb{CP}}^{\,2}\bigr)<1.        \tag{74.11}
\]
Here \(\eta\) is any strict lower endpoint of (74.5) or (74.8).

**Proof.** The CH host has \(I_-=0\), \(I_+=4\pi^2A_Y/3\) (signature formula with \(\tau=A_Y/9\)) and \(d=4\pi^2A_Y/3\). Insert \(n\) smoothed cells \(g_\delta\) into \(n\) of the disjoint balls. A reversed-\(\mathbb{CP}^2\) insertion changes \(2\chi+3\tau\) by \(-1\) and \(\chi\) by \(+1\); exact CH agreement on the collar cancels boundary transgressions, so (74.1) gives \(\Delta I_+=-2\pi^2\eta_\delta\) and \(\Delta d=4\pi^2(\Delta S/96\pi^2-p)=-4\pi^2(1-\eta_\delta)\) per cell (the Gauss–Bonnet check \(d=S/24-P/2\) agrees). The remaining \(k-n\) summands are inserted in arbitrarily small balls in the complement by LeBrun's flattening and conformal connected sum with the Fubini–Study reversed \(\mathbb{CP}^2\) (the reversed Fubini–Study summand contributes \(I_+=0\), \(I_-=12\pi^2\) and raises \(8\pi^2\chi\) by \(8\pi^2\), so each costs exactly \(4\pi^2\) of deficit up to the arbitrarily small flattening error; LeBrun 2023 \cite{lebrun2023weyl}); they need no full-radius sites. Since \(d\) is a conformal invariant and the pieces are disjoint, the deficits add; letting \(\delta\) and the flattening errors tend to zero gives (74.10). A positive lower bound gives an actual class with \(d>0\), hence \(\alpha<1\) by Step 72. \(\square\)

### Packing: lower density and the disjoint-volume ceiling

At \(\operatorname{Ric}=-g\), \(V(B_R)=18\pi^2\sinh^4(R/\sqrt6)=18\pi^2X^2\) and \(V(Y)=2\pi^2A_Y\). A maximal \(2R\)-separated set has disjoint \(R\)-balls and covering \(2R\)-balls, and \(\sinh^2(2R/\sqrt6)=4X(1+X)\), so
\[
 \beta_0(X):=\frac1{9[4X(1+X)]^2}\ \le\ \frac N{A_Y}\ \le\ \frac1{9X^2}=:\beta_{\max}(X).        \tag{74.13}
\]
With \(n=\min\{k,N\}\), (74.11) holds whenever \(\tfrac13-h+\eta\min\{h,N/A_Y\}>0\), \(h=k/A_Y\); in particular
\[
 h<\frac13+\eta\beta_0(X)\ \Longrightarrow\ \alpha<1,                    \tag{74.14}
\]
which is \(h<0.33333336306501022\ldots\) for \(X=8\) and \(h<0.333333333335247042\ldots\) for \(X=128\). Conversely no disjoint placement of copies of a fixed-radius cell can do better than
\[
 h<\frac13+\eta\beta_{\max}(X)\qquad(0.3333718656\ldots\ \text{for }X=8,\ 0.33333384287\ldots\ \text{for }X=128).     \tag{74.14'}
\]
So the formal all-cell numbers \(1/[3(1-\eta)]\) (0.340899…, 0.360413…) are unattainable by these cells: \(n=k\) forces \(h\le\beta_{\max}\ll1/3\).

**Packing-free ceiling and what it says.** For any family of disjoint exact-collar cells (one per exceptional class, arbitrary shapes), (74.1) and additivity give \(d\le4\pi^2(A_Y/3-k)+2\pi^2\sum_i(-\Delta I_+^{(i)})\), and \(-\Delta I_+^{(i)}\le I_+(\text{footprint}_i)\). Hence crossing \(1/3\) by a definite amount \(\varepsilon\) requires the cells to annihilate a fraction \(\ge 3\varepsilon/2\) of the host's whole self-dual Weyl energy; with \(k\approx A_Y/3\) classes this means each class must, on average, remove an \(O(1)\) fraction of the \(W^+\)-energy of a host region of volume \(\asymp V/k\). Radial cells remove \(\eta/(6X^2)\) of their own footprint energy (\(\approx5.8\times10^{-5}\) for \(X=8\)). The definite crossing is therefore the same *diffuse multiclass* state whose absence blocks \(P\)-positivity in \(0<k<A/3\) (§3 below); no further optimization of isolated radial cells is pursued.

### Footprint efficiencies (corrected)

Deficit saving per footprint, \(\eta/(3X^2)\): \(1.15596759736\times10^{-4}\) (\(X=8\)), \(1.52860922848\times10^{-6}\) (\(X=128\)); ratio 75.62. Literal fraction of the ball's \(I_+\) removed: \(\eta/(6X^2)\), half of these. (JSON fields regenerated in Step 75.)

## 3. Fixed-complex Kähler frontier and the capacity equivalence (corrected)

Let \(M=Y\#k\overline{\mathbb{CP}}^2\) carry the blow-up complex structure, \(H=\pi^*K_Y\), \(E_i\) the exceptional classes. Then \(K_M=H+\sum E_i\), \(c_1(M)=-H-\sum E_i\). Write a Kähler class as \([\omega]=\pi^*a-\sum e_iE_i\), \(e_i=[\omega]\cdot E_i>0\), \(q=K_Y\cdot a>0\), \(E=\sum e_i\). Hodge index on \(Y\) gives \(q^2\ge A_Ya^2\), so
\[
 \frac{(c_1\cdot[\omega])^2}{[\omega]^2}=\frac{(q+E)^2}{a^2-\sum e_i^2}\ge A_Y,
 \qquad (q+E)^2-A_Y(a^2-\textstyle\sum e_i^2)=(q^2-A_Ya^2)+2qE+E^2+A_Y\sum e_i^2\ge0.     \tag{74.17}
\]
With \(\int s\,dV=4\pi c_1\cdot[\omega]\), \(V=[\omega]^2/2\), Cauchy–Schwarz and \(|W^+|^2=s^2/24\) for Kähler metrics,
\[
 I_+=\frac{S}{24}\ge\frac{4\pi^2}3\frac{(c_1\cdot[\omega])^2}{[\omega]^2}\ge\frac{4\pi^2A_Y}{3}.   \tag{74.19}
\]
The chiral form of the deficit is \(d([g])=4\pi^2(A_Y-k)-2I_+(g)\) (from \(8\pi^2\chi-I_+-I_-\) and \(I_+-I_-=12\pi^2\tau\), \(2\chi+3\tau=A_Y-k\)), so
\[
 d([g])>0\iff I_+(g)<2\pi^2(A_Y-k),                  \tag{74.19a}
\]
and for Kähler metrics of the fixed blow-up structure \(d\le4\pi^2(A_Y/3-k)\). **Proposition 74.K.** For the prescribed blow-up complex structure, Kähler metrics have positive Weyl deficit iff \(k<A_Y/3\) is possible, and the fixed-complex Kähler frontier is exactly \(h=1/3\): for \(k\ge A_Y/3\) none exists, and for \(k<A_Y/3\) the inherited fixed-complex recovery \(\inf_{\rm K}P=8\pi^2k\) gives \(\inf_{\rm K}I_+=4\pi^2A_Y/3\) and hence positive deficit. Theorem 74.W crosses this frontier, so the true \(\alpha<1\) frontier is not the Kähler one and every crossing is non-Kähler for that complex structure (Kähler metrics for unrelated complex structures on the same smooth manifold are not addressed).

**Capacity equivalence.** At a negative Yamabe representative with \(s=-4\), put \(p=P/8\pi^2\), \(\upsilon=V/2\pi^2-A_Y\), \(\kappa=A_Y/2-3I_+/8\pi^2\). Then \(p=k-\tfrac43\kappa+\tfrac13\upsilon\), \(\mathcal E=4P/(P+4V)\), and
\[
 \alpha(M)<1\iff\exists\ \text{a negative Yamabe representative with}\ \kappa>\frac{3k-A_Y}4 .   \tag{74.20}
\]
A special cell raises \(\kappa\) by \(3\eta/4\). Writing \(\kappa=\tfrac{A_Y}2\Theta\) (\(\Theta\) = fraction of the host's \(I_+\) budget removed), \(d>0\iff h<\tfrac13+\tfrac23\Theta\). The best-constant object is the **capacity function**
\[
 \Theta_*(h)=\sup\{\Theta\ \text{realizable at}\ h\},\qquad \alpha<1\iff\Theta_*(h)>\frac{3h-1}2 .     \tag{74.21}
\]
No constant endpoint \(h_c=\tfrac13+\tfrac23\Theta_*\) is asserted, because realizable saving depends on \(h\). The same unknown \(\kappa\) governs open-range positivity: \(P_*>0\) in \(0<k<A_Y/3\) is an *upper* bound on realizable capacity away from the Einstein-ratio end, while 74.W is a *lower* bound on it. The near-ASD end \(h\to1\) relates to Taubes-type ASD existence after many blow-ups and the unit-wall attainment at \(T_+=0\) (71.B).

## 4. Increment from the updated public-problem references

The added theorem in the supplied references is a complete, nonhomogeneous, strictly almost-Kähler negative Einstein geometry on \(\mathbb R^4\):
\[
 \operatorname{Ric}=-3g,\quad W^-=0,\quad d\Omega=0,
 \quad|\Omega|^2=2,\quad|\nabla\Omega|^2
 =\frac{36(1-x^2)^3}{(1+3x^2)^3}>0.                              \tag{74.22}
\]
The rational metric is defined for \(1/3<x<1\), extends smoothly across a bolt, is complete at \(x=1\), lifts to the universal cover \(\mathbb H^2\times\mathbb R^2\cong\mathbb R^4\), and is nonhomogeneous because \(|W^+|^2\) varies from \(2/3\) to \(6\). This answers Fino's 2005 non-invariant, non-Ricci-flat existence question, without a historical-first assertion.

It does not settle closed negative Goldberg. On a closed almost-Kähler four-manifold the torsion is a section of \(E=\Lambda^{0,1}\otimes\Lambda^{0,2}\), with
\[
 \langle c_2(E),[M]\rangle=5\chi+6\tau.
\]
For closed negative Einstein geometry this number is positive, so torsion must vanish somewhere. The complete \(\mathbb R^4\) example has no finite zero and cannot descend unchanged to a compact quotient. The remaining closed problem is therefore a zero-extension/prolongation question, not local nonexistence of strict solutions.

The updated references also preserve the exact research scope: Kodaira's uniform slope answer remains conditional on FD/FD2; Fino is a separate noncompact existence answer; Q1 nonminimal general-type Einstein existence, Q2 exact full-curvature infimum, Q3 smooth non-Bach global minimizer, and Q4 closed negative Goldberg remain active.

## 5. Consequence for the next research investment

The intermediate-band theorem is now at its proper level: certified local constants, exact mixed quantifiers, an explicit but tiny positive packing extension, a matching Kähler obstruction, and a single capacity formulation. Further radial-cell polishing is lower value unless it sharply improves \(\eta/X^2\) or supplies a denser batch construction. The harder common target is now the capacity upper side in \(0<k<A/3\), where \(P_*>0\) would simultaneously advance Q1 and Q2 and provide the non-Einstein premise needed by Q3. The Fino geometry sharpens Q4's remaining target: exploit the forced torsion zero and its local nonlinear prolongation or nullity-line extension on a closed negative Einstein manifold.
