# Step 69 — The P-form upper law over negative Kähler–Einstein hosts (balanced ball-quotient family and every negative KE surface)

Agent2, Execute. Inputs: A01 Steps 31/33 (`Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md`, `step33_surgery_slope_law_and_ASD_retention.md`), theorem package §§4.3, 5, 19–20, Theorem 59.R/Corollary 59.KE with binding Part D of `step59_rigorous_burns_expansion_and_zero_gap_structure.md`, LeBrun's Lemma 1 in *Four-manifolds without Einstein metrics* \cite{lebrun1996four} (Knowledge object `Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8`, lines 187–200) and LeBrun's polarized Proposition 3.2 in \cite{lebrun2001ricci}.
Script/data: `workspace/scripts/step69_balanced_upper_law.py` → `workspace/data/step69_balanced_upper_law.json` (exit 0).

Conventions. \(\mathcal E(g)=\inf_{\lambda\ne0}\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)\), \(\alpha(M)=\inf_g\mathcal E(g)\) (A01/corpus normalization), \(P=\int|\mathrm{Ric}^\circ|^2\), \(p=P/8\pi^2\), \(A=c_1^2(X)\), \(Q=k+4\ell\), \(h=Q/A\), \(\theta=k/Q\). KE hosts are normalized \(\mathrm{Ric}=-g\), so \(s=-4\), \(V=2\pi^2A\).

## 0. What this note establishes and what it does not

The balanced coefficient \(28/9+(8/9)p_{\rm cell}\) was previously obtained (A01 Steps 31–33, package §5.3) through the scalar-normalized defect \(D=\int|\mathrm{Ric}+g|^2\), with volume, total-scalar and \(T^2/V\) bookkeeping and an asymptotic \(o(Q)\) ledger, along a selected ramified cover family. The present note replaces that ledger by one inequality (Lemma 69.Y) that converts any metric's trace-free Ricci energy directly into an upper bound for \(\alpha\) on every manifold carrying LeBrun's polarized scalar supply. Three consequences follow.

1. On compact ball-quotient hosts the balanced law becomes **exact and non-asymptotic**: there is no host mismatch, no smoothing ledger beyond the cell's own arbitrarily small loss, no rounding, and no limit; the only selection is one preliminary cover with large injectivity radius, after which the statement holds for **every** further finite cover.
2. Because only \(P\) enters, the scalar-variance part of the certified cell disappears from the coefficient: \(3.996151138\ldots\) (J route) improves to \(3.996144651\ldots\) (P route).
3. Through the analytic Burns-perpendicular cell (59.R/59.KE) the strict sub-tariff upper law holds over **every** compact negative KE surface and, with Kronheimer resolutions, every minimal surface of general type: \(\alpha(X\#k\overline{\mathbb{CP}}^2)<4k/c_1^2(X)\) for every \(k\ge1\).

This is an **upper law**. The lower side on these families is still the LeBrun-type slope law (A01 Theorem A); the matching problem is the open-range problem classified in §21. The coefficient is not claimed optimal.

## 1. Lemma 69.Y (Yamabe reduction of the defect to trace-free Ricci energy) — Proved

**Lemma 69.Y.** Let \(g\) be a metric on a closed four-manifold with \(Y[g]<0\), and let \(\hat g=\phi^2g\) be a constant-scalar-curvature (Yamabe) metric in \([g]\). Then
\[
\mathcal E(\hat g)=\frac{16\,P(\hat g)}{Y[g]^2},\qquad
P(g)-P(\hat g)=|\hat s|\int|\nabla\phi|^2d\mu+3\int\Big(\frac{\Delta\phi}{\phi}\Big)^2d\mu\ \ge0,
\]
hence
\[
\boxed{\ \alpha(M)\le\frac{16\,P(g)}{Y[g]^2}\quad\text{for every }g\text{ with }Y[g]<0.\ }
\]

*Proof.* Pointwise \(|\mathrm{Ric}-\lambda g|^2=|\mathrm{Ric}^\circ|^2+4(s/4-\lambda)^2\). For \(\hat g\) take \(\lambda=\hat s/4\): \(\int|\mathrm{Ric}-\lambda\hat g|^2=P(\hat g)\) and \(\lambda^2\hat V=\hat s^2\hat V/16=Y^2/16\) (checked symbolically, item 1 of the JSON). For the comparison write \(P=\int(4|W^+|^2+s^2/12)\,d\mu-8\pi^2(2\chi+3\tau)\); \(\int|W^+|^2d\mu\) is conformally invariant, and LeBrun's Lemma 1 \cite{lebrun1996four} gives \(\int s^2d\mu-\int\hat s^2d\hat\mu=12|\hat s|\int|\nabla\phi|^2+36\int(\Delta\phi/\phi)^2\). Divide by 12. \(\square\)

**Corollary 69.Y′ (P-form bound on supply manifolds).** Let \(X\) be a minimal surface of general type and \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\). For every metric on \(M\), LeBrun's polarized construction \cite{lebrun2001ricci}, Prop. 3.2 (including the \(b^+=1\) chamber selection; corpus `Curvature_Realizability.tex` §"Metricwise polarized classes", lines 1360–1510, and the handle loop insertions, line 4549) supplies an actual monopole class with \(\int s^2d\mu\ge32\pi^2A\). Applied to the Yamabe metric this gives \(Y[g]<0\) and \(Y[g]^2\ge32\pi^2A\). Therefore
\[
\boxed{\ \alpha(M)\le\frac{P(g)}{2\pi^2A}\ \ \forall g,\qquad
\alpha(M)\le\frac{4\,p_*(M)}{A},\quad p_*(M)=\inf_g\frac{P(g)}{8\pi^2}.\ }
\]
Only the inequality direction of the Yamabe problem is used; no conformal factor has to be estimated. (Lemma 69.Y also explains the sign of the package's scalar conformal identity \(P(g)-P(\hat g)=3\int(\Delta u/u)^2+24\int|\nabla u|^2\) at \(\hat s=-24\).)

**Lemma 69.A (exact locality of P).** If \(g\) is Einstein outside disjoint open sets \(B_1,\dots,B_N\), then \(P(g)=\sum_i\int_{B_i}|\mathrm{Ric}^\circ_g|^2\). (Trivial: \(\mathrm{Ric}^\circ=0\) elsewhere.) In contrast \(D=\int|\mathrm{Ric}+g|^2\) is also local, but the passage from \(D\) to \(\mathcal E\) needs \(V\) and \(\int s\); the P route needs neither.

## 2. Local pieces

**(C) Certified CH cell.** The authoritative A01 Step-33 profile (\(x_0=3/100\), \(X=128\), degree 20) has the exact-dyadic Arb enclosure \(p\in[0.995662732753254329\ldots,0.995662732771114200\ldots]\) (`Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json`, upper dyadic \(338806471362324583565914367157197246841/2^{128}\)). The admissibility chain (positivity, ordinary \((-1)\) Hopf bolt, topology \(D\#\overline{\mathbb{CP}}^2\), third-order CH contact) and the exact-collar smoothing with arbitrarily small loss are inherited (package §§4.3, 5.3; A01 Step 33 §6). Thus for every \(\delta>0\) there is a smooth metric on \(D\#\overline{\mathbb{CP}}^2\), exactly CH (\(\mathrm{Ric}=-g\)) on an outer collar of a geodesic ball of radius \(R_c=\sqrt6\,\mathrm{arsinh}\sqrt{128}+1\), with \(p\le p_c+\delta\), \(p_c:=0.995662732771114200\ldots\).

**(H) CH handle cell.** Package §5.2: \(\mathfrak P_{0,1}=32\pi^2\), approached (not attained) by CH-collared cells of topology \(D\#(S^1\times S^3)\). Take the same outer radius \(R_c\) (radius is free in the definition).

**(H′) Handle in an arbitrary background (needed in §4).** Let \(N=((S^1\times S^3)\setminus\{p\},G_p^2g_0)\) with \(g_0\) the round product (positive constant scalar curvature, so the conformal Laplacian is positive and has a positive Green function \(G_p\)). \(N\) is conformally flat, scalar flat, asymptotically Euclidean of order two in inverted coordinates, and diffeomorphic to \(R^4\#(S^1\times S^3)\). Gauss–Bonnet for one AE end (\(\chi(N)=-1\)) gives \(\int_N(|W|^2+s^2/24-|\mathrm{Ric}^\circ|^2/2)=8\pi^2(\chi-1)=-16\pi^2\), hence \(P(N)=32\pi^2\) exactly. Glue \(N\) scaled by \(\delta\) into normal coordinates of any smooth background, interpolating on \(\{\rho_1<|x|<2\rho_1\}\) with \(\rho_1\) fixed. Write \(P(\tilde g)-P(g)=32\pi^2+\int(F_+(\tilde g)-F_+(g))\), \(F_+=4|W^+|^2+s^2/12\). Since \(\mathcal C(N)=(2W^+,s/\sqrt{12})\equiv0\), the change in \(\mathcal C\) on \(\{|x|<\rho_1\}\) is the cross term of the \(\delta^2|x|^{-2}\) tail with the background jets, \(O(\delta^2|x|^{-2})\); on \(\{|x|<R\delta\}\) curvature is \(O(1)\) on volume \(O(\delta^4)\); on the interpolation annulus the tail is \(O(\delta^2)\) in \(C^2\). Hence \(P(\tilde g)=P(g)+32\pi^2+O(\delta^2\log\delta^{-1})\). For an Einstein background \(P(\tilde g)\to32\pi^2\).

**(B) Analytic Burns-perpendicular cell in any negative KE host.** By Theorem 59.R (P-critical background, E_P=0 near the point; binding repairs of Part D) and Corollary 59.KE, inserting a Burns metric of area parameter \(\varepsilon\) with direction \(\zeta\perp\omega\) at a point of a KE surface with \(s=-4\) gives
\[
p_{\rm cell}(\varepsilon)=1-\tfrac14\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2),
\]
because \(R^+(\zeta,\zeta)=0\) and \(\Phi=-s^2/32=-\tfrac12\); the \(W^-\) and \(\mathrm{Ric}^\circ\) sectors add no logarithmic term (A01 #834, Step 64; package §19). The \(O(\varepsilon^2)\) constant depends only on finitely many derivatives of the host metric on a fixed normal-coordinate ball \(B_{\rho}(x)\); it is therefore the same at every lift of \(x\) to any Riemannian cover. Fix \(\varepsilon_X\) with \(\eta_X:=1-p_{\rm cell}(\varepsilon_X)>0\) (cell support radius \(\rho_X\)).
Reference computation (JSON item 4): at the \(P\)-optimal corrector the \(\sigma\)-linear scalar curvature vanishes identically, \(s_1=0\), and the logarithmic coefficient of the \(D\)-density equals that of \(P\): \(\Phi_D=\Phi=-s^2/32\). So the Burns-perpendicular saving is scalar-neutral at logarithmic order, and the \(D\) route would give the same leading saving; the P route is used because it needs no volume bookkeeping.

## 3. Theorem 69.B (balanced law over ball quotients; exact, non-asymptotic) — Proved, modulo the inherited cell certificate and LeBrun supply

Let \(Y=\Gamma\backslash\mathbb B^2\) be a compact ball quotient (\(\Gamma\) torsion-free cocompact), \(\mathrm{Ric}=-g\). Since \(\Gamma\) is linear it is residually finite (Malcev); excluding the finitely many nontrivial elements of displacement \(<4R_c\) at a base point and passing to a normal finite-index subgroup gives a finite cover \(X'\) with \(\mathrm{inj}(X')>2R_c\). Every finite cover \(X\to X'\) inherits \(\mathrm{inj}(X)>2R_c\). A maximal \(2R_c\)-separated set in \(X\) has at least
\[
N(X)\ \ge\ \frac{2\pi^2c_1^2(X)}{v_{CH}(4R_c)}
\]
points (\(v_{CH}\) = CH volume of balls, \(\mathrm{Ric}=-g\)), whose \(R_c\)-balls are disjoint and isometric to CH balls.

**Theorem 69.B.** For every finite cover \(X\) of \(X'\) and every integer \(n\ge1\) with \(15n\le N(X)\), the manifold
\[
M=X\#8n\,\overline{\mathbb{CP}}^2\#7n\,(S^1\times S^3),\qquad Q=36n,\ h=\frac{36n}{c_1^2(X)},
\]
satisfies
\[
\boxed{\ \frac{\alpha(M)}{h}\ \le\ \frac{28}{9}+\frac89\,p_c\ =\ 3.99614465135210151\ldots\ <\ 3.9961447.\ }
\]
Its topology is exactly balanced: \(\Delta=3\chi-c_1^2=0\) for \(X\), \(T_+=c_1^2(X)-Q\), \(3T_-/c_1^2(X)=1+h\), slope \(\sigma=4r+18\theta=4\) (JSON item 2), with no rounding.

*Proof.* Insert \(8n\) copies of (C) with loss \(\delta\) and \(7n\) copies of (H) with \(P\le32\pi^2+\delta\) into \(15n\) of the disjoint CH balls; the glued metric \(\tilde g\) equals the KE metric of \(X\) outside them and is smooth because each cell is exactly CH on its collar. By Lemma 69.A, \(P(\tilde g)\le8n\cdot8\pi^2(p_c+\delta)+7n(32\pi^2+\delta)\). By Corollary 69.Y′,
\[
\alpha(M)\le\frac{P(\tilde g)}{2\pi^2c_1^2(X)}=\frac{32n(p_c+\delta)+112n+O(n\delta)}{c_1^2(X)}
=h\Big(\frac{28}{9}+\frac89p_c\Big)+O(h\delta).
\]
Let \(\delta\to0\). The exact rational value of \(28/9+(8/9)p_c\) is in the JSON (item 3). \(\square\)

*Quantifiers.* Existential only in the preliminary cover \(X'\) (equivalently, in the requirement that the cell balls embed). Universal over all further finite covers and all admissible \(n\) — towers, nesting, or \(h\to0\) are not needed for the upper bound. The previous form "suitably selected family, \(\limsup\alpha/h<3.9961512+\varepsilon\)" is superseded.

*Lower side on the same family (inherited, unchanged).* A01 Theorem A at \(\sigma=4\) gives \(\liminf\alpha/h\ge\frac{18}{19}c_0\) along \(h\to0\) with the nonexplicit linear-window constant \(c_0\in(0,2/9]\); the explicit branch \(\frac43(3-\sigma)_+\) vanishes. So on the balanced ball-quotient family
\[
\tfrac{18}{19}c_0\le\liminf\alpha/h\le\limsup\alpha/h\le3.9961446514\ldots
\]
The gap between the two sides is the open-range problem; it is not narrowed here.

*Ramified towers (A01 Step 31) in P form.* On Biquard–Guenancia towers the cell balls are only \(\varepsilon_m\)-close to CH in \(C^2\). Interpolating on a fixed buffer annulus gives \(\mathrm{Ric}^\circ=O(\varepsilon_m)\) there, so each site costs an extra \(O(\varepsilon_m^2)\) in \(P\) and nothing else; Corollary 69.Y′ applies because \(\bar X_m\) is minimal of general type. Hence \(\alpha/h\le4-4\theta_m(1-p_c)+O(\varepsilon_m^2)\) for every \(m\), with \(\theta=2(1-r)/9\) on the balanced slice. The volume and total-scalar increments of the D ledger never appear.

## 4. Theorem 69.KE (every negative KE host and every minimal surface of general type) — Proved, modulo 59.R/59.KE and LeBrun supply

**(a) Fixed manifold.** Let \(X\) be a minimal surface of general type. For every \(k\ge1\),
\[
\boxed{\ \alpha(X\#k\overline{\mathbb{CP}}^2)\ <\ \frac{4k}{c_1^2(X)}.\ }
\]
*Proof.* Corollary 59.KE gives a metric with \(P<8\pi^2k\) (Burns-perpendicular cells at \(k\) distinct smooth points of the KE metric or of the KE orbifold canonical model, with Kronheimer ALE resolutions at the ADE points, \(\varepsilon\) fixed before the ALE scale tends to zero). Apply Corollary 69.Y′. \(\square\)
The non-strict bound \(\alpha\le4k/A\) already follows from the fixed-complex Kähler infimum \(\inf_{\rm K\ddot ahler}P=8\pi^2k\) (package §3.5/§13) and Corollary 69.Y′; the strictness is the Burns-perpendicular saving. Compare LeBrun: \(p\ge k-A/3\) for every metric, so \(4p_*/A\) cannot be smaller than \(4(k-A/3)_+/A\); the upper bound and the P-lower bound meet only for \(k\gg A\) at leading order, not in the open range.

**(b) Covers and mixed surgery.** Let \(X\) be a compact KE surface with \(c_1<0\) and \(X_m\to X\) finite Riemannian covers of degree \(d_m\). Using (B) for blow-ups and (H′) for handles in disjoint lifted balls of radius \(\rho_X\),
\[
\frac{\alpha(X_m\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3))}{h}\ \le\ 4-4\theta\,\eta_X\qquad(k+\ell\le d_m N_X(\rho_X)),
\]
non-asymptotically, with \(\eta_X>0\) independent of \(m\), \(k\), \(\ell\) (locality of the 59.R constants). The supply of covers of unbounded degree needs only that \(\pi_1(X)\) has finite-index subgroups of unbounded index (e.g. \(\pi_1\) infinite and residually finite); it fails for simply connected KE surfaces such as smooth hypersurfaces of degree \(\ge5\) in \(\mathbb{CP}^3\), where only (a) applies.

**(c) Where the balanced slice lies for non-ball-quotient hosts (correction of the expected scope).** For an unramified cover \(\Delta_m=d_m\Delta_X\) with \(\Delta_X=3\chi(X)-c_1^2(X)>0\) unless \(X\) is a ball quotient (BMY equality). Then \(r_m=\Delta_m/Q_m=\Delta_X/(hA_X)\) and \(\sigma=4r+18\theta\). If \(h\to0\) then \(\sigma\to\infty\): the balanced slice \(\sigma=4\) and every slice with \(\sigma<4+c_0\), where the lower theory lives, are unreachable. The balanced slice \(\sigma=4\) exists only at fixed \(h\ge\Delta_X/c_1^2(X)\) (from \(r=1-\tfrac92\theta\le1\)). Hence "the strict sub-4 balanced law extends to every negative KE surface with a cover tower" is false as an \(h\to0\) statement: what extends to every negative KE host is the strict upper law (b) in the blow-up fraction \(\theta\); the balanced small-\(h\) law is a ball-quotient phenomenon, or needs ramified towers (\(\Delta_m/A_m\to0\)), as in A01 Step 31. At fixed \(h\) with \(\sigma<3\) the explicit A01 branch \(\mathcal E\ge4\theta_\Delta/(1+\theta_\Delta)\), \(\theta_\Delta=h(3-\sigma)/3\le1/3\), gives a two-sided window over any negative KE host with the upper side (b); this uses no asymptotics on either side.

## 5. Reading

The P route identifies what the balanced coefficient measures: the per-cell trace-free Ricci energy in units of \(8\pi^2\), weighted \(8/36\) for blow-ups and \(28/36\) at the sharp handle value 4. Volume, total scalar curvature, scalar variance and \(W^-\) of the host are invisible (Lemma 69.A plus the inequality \(Y^2\ge32\pi^2A\)). The lower theory, by contrast, sees only the topological slope \(\sigma\). Any improvement of the upper coefficient must come from lower \(p_{\rm cell}\) or from interacting (non-separated) configurations; any improvement of the lower coefficient must price the Weyl deficit \(\kappa\) (§21). The equality \(\alpha\le4p_*/A\) also shows that the open-range question for \(\alpha\) on blow-ups of general type is controlled from above entirely by the \(P\)-infimum \(p_*\) studied in §§19–21.

Open after this note: optimality of \(28/9+(8/9)p_{\rm cell}\) (unrestricted cell infimum, mixed-cell nonadditivity); the lower coefficient on the balanced family (only \(\tfrac{18}{19}c_0\)); whether \(\alpha\) and \(4p_*/A\) agree to leading order (a reverse inequality is not known: \(\mathcal E(g)\) for non-Yamabe \(g\) is not bounded below by \(16P(\hat g)/Y^2\) by any argument here).


## 6. Binding corrections after verification (TTCS `trace/ttcs/results/step69_ttcs01_verifier1_integration.md`; branches `step69_ttcs01_sub{1,2}_verifier.md`)

These supersede the corresponding statements above.

**6.1 Lemma 69.Y corrected (stronger).** \(\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)=4-2T/(V\lambda)+R/(V\lambda^2)\) with \(T=\int s\), \(R=\int|\mathrm{Ric}|^2=P+S/4\). Minimizing in \(1/\lambda\): \(\mathcal E(g)=4-T^2/(VR)=(4P+L_s)/R\), \(L_s=S-T^2/V\). At a negative Yamabe metric \(\mathcal E(\hat g)=16P(\hat g)/(4P(\hat g)+Y^2)\); the value \(16P/Y^2\) in §1 is the quotient at \(\lambda=\hat s/4\), not the minimum (JSON item 1 is that value only). Hence
\[
\alpha(M)\le\frac{16P(g)}{4P(g)+Y[g]^2}\le\frac{16P(g)}{Y[g]^2},\qquad
\alpha(M)\le\frac{4p_*}{A+p_*}\le\frac{4p_*}{A}\ \text{on supply manifolds}.
\]
The conformal identity \(P(g)-P(\hat g)=|\hat s|\int|\nabla\phi|^2+3\int(\Delta\phi/\phi)^2\) is confirmed (Hilbert–Schmidt Weyl norms on unit two-forms).

**6.2 Reverse comparison (new, elementary, no monopole input).** \(\mathcal E\ge4P/R\) and \(R=4P+24\pi^2T_+-12\int|W^+|^2\le4P+24\pi^2T_+\). For \(T_+=2\chi+3\tau>0\):
\[
\boxed{\ \frac{p_*}{p_*+\tfrac34T_+}\ \le\ \alpha(M)\ \le\ \frac{4p_*}{A+p_*}\ }
\]
(upper side on supply manifolds). For \(Q=o(A)\), \(p_*=o(A)\): \(\tfrac43p_*/A\lesssim\alpha\lesssim4p_*/A\). So \(\alpha\) and the dimensionless P-infimum \(p_*\) are equivalent up to the factor 3, and \(\alpha=0\iff p_*=0\) when \(T_+>0\). Normalization check: the real-hyperbolic family \(p_*=k\), \(T_+=2\chi(Y)-k\) gives \(4k/(k+6\chi(Y))\), the Theorem-H value. The sharp comparison \(\mathcal E(g)\ge16P(\hat g)/Y^2\) and leading-order equality \(\alpha\sim4p_*/A\) remain unproved.

**6.3 Supply with handles — source checked.** LeBrun \cite{lebrun2001ricci} (Knowledge object `math-0003068-Ricci-Curvature-Minimal-Volumes-and-Seiberg-Witten-Theory--8d8fe6f684f5--cab40be18df4`, lines 301–320): for \(X\) with nontrivial SW invariant and \((2\chi+3\tau)(X)>0\) the invariant is polarization independent even if \(b^+=1\), and the holonomy-constrained invariant gives on \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\), for every metric, a monopole class with \((c_1^+)^2\ge(2\chi+3\tau)(X)\). Monopole existence excludes \(Y\ge0\) (Weitzenböck for \(Y>0\); \(Y=0\) contradicts \((c_1^+)^2>0\)), so \(Y<0\) and \(Y^2\ge32\pi^2A\). The handle dependency of Corollary 69.Y′ is therefore discharged by the source, not only by A01's assertion.

**6.4 Theorem 69.B corrected.** \(\alpha(M)/h\le C_c/(1+C_ch/4)\le C_c\), \(C_c=28/9+(8/9)p_c=3.9961446513521015108\ldots\), with \(p_c=338806471362324583565914367157197246841/2^{128}\) (exact dyadic endpoint). "Non-asymptotic" means no cover-degree or \(h\to0\) limit; the smoothing/handle losses are still removed by an infimum. The transfer and arithmetic are verified; the interval certificate itself is A01's.
Preliminary cover repaired: with compact fundamental set \(F\), \(D=\sup_F d(x_0,\cdot)\), exclude all \(\gamma\ne1\) with \(d(x_0,\gamma x_0)\le4R_c+2D\); a normal finite-index subgroup avoiding them gives \(\mathrm{inj}(X')>2R_c\) globally (one base point alone is insufficient). Packing bound \(N(X)\ge2\pi^2A/v_{CH}(2R_c)\). Ramified towers: "every \(m\)" means every index where the \(C^2\) discrepancy guarantees positivity.

**6.5 Handle insertion repaired.** Glue the scale-\(\delta\) AE model \(N\) at shrinking radius \(t=\sqrt\delta\): on \(t<r<2t\), \(g-\delta_{\rm E}=O(r^2)\), \(g_{N,\delta}-\delta_{\rm E}=O(\delta^2r^{-2})\), so \(P_{\rm ann}=O(t^4+\delta^4t^{-4})=O(\delta^2)\); removed background ball \(O(t^4)\); omitted tail \(O((\delta/t)^4)\). Hence \(P(\tilde g)=P(g)+32\pi^2+O(\delta^2)\) in any smooth background, support in any prescribed ball. The fixed-radius argument of §2(H′) is withdrawn (it deleted background \(F_+\) energy; full core curvature is \(O(\delta^{-2})\), only the chiral part is \(O(1)\)). This also supplies fixed-radius handle cells, replacing "radius is free".

**6.6 Theorem 69.KE corrected.** (a) \(\alpha(X\#k\overline{\mathbb{CP}}^2)<4k/(A+k)<4k/A\) for every minimal general-type \(X\), \(k\ge1\) (insertion balls in fixed regular regions; Burns parameters fixed before the Kronheimer scale). (b) \(\alpha/h\le4(1-\theta\eta_X)/(1+h(1-\theta\eta_X))\le4-4\theta\eta_X\); constants are exactly cover-independent (local isometry), take the minimum saving over finitely many base sites. \(s_1=0,\ \Phi_D=\Phi\) verifies logarithmic scalar neutrality only. (c) Valid for towers over a **fixed** non-ball host; \(h\ge\Delta_X/A_X\) is only necessary for balance (integrality, packing, \(\theta>0\) also needed); varying hosts with \(\Delta_m/A_m\to0\) (ramified towers) do reach balanced small-\(h\) slices. The fixed-\(h\) lower sentence requires \(0\le\theta_\Delta=h(3-\sigma)/3\le1/3\) and the packing condition.

**6.7 Precedence.** Lemma 69.Y and both comparisons are elementary consequences of LeBrun's Lemma 1, Chern–Weil and minimization in \(\lambda\); no source stating them verbatim was found; precedence is not claimed.
