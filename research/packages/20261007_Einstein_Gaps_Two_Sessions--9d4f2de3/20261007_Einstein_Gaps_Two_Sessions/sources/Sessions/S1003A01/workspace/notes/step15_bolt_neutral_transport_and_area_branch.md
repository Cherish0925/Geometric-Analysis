# Step 15 — Bolt-carried neutral transport, the bolt-area branch, and a 3.4× larger certified deficit

Session S1003A01, Agent2, Execute. Normalization \(\operatorname{Ric}_{CH}=-6g\); costs are in units of \(8\pi^2\);
\(J_6=\int|\operatorname{Ric}+6g|^2\), \(P=\int|\operatorname{Ric}^\circ|^2\). Diagonal Bianchi IX,
\(g=dt^2+\sum a_i^2\sigma_i^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\), \(\int\sigma_{123}=2\pi^2\).
Cell convention (FrozenCell): \(a_1^2=F\) collapses at the bolt \(x=x_0\), \(a_2^2=x\), \(a_3^2=xe^w\) is the CH Kähler
direction, \(dt=dx/(2\sqrt G)\); \(b^2=a_2(0)^2=x_0\). (Peer S1003A02 labels: their \(a_3\) = our \(a_1\), their \(a_1\) = our \(a_3\).)

## 1. The neutral mode is a scalar-Laplacian mode; its Green representation closes at the bolt

Since \(\operatorname{Ric}_{ii}=-(WL_i)'/W+\mathrm{alg}_i\) with \(L_i=a_i'/a_i\), \(W=a_1a_2a_3\),
\(\mathrm{alg}_i=2(a_i^4-(a_j^2-a_k^2)^2)/W^2\), the field \(q=\log(a_2/a_1)\) satisfies exactly
\[
(Wq')'=W(V-E),\qquad V=\frac{4(a_2^2-a_1^2)(a_1^2+a_2^2-a_3^2)}{W^2},\qquad E=\operatorname{Ric}_{22}-\operatorname{Ric}_{11}.
\]
Because \(W\,dt=dV_g/(2\pi^2)\), this is \(\Delta_g q=V-E\) for the radial scalar Laplacian. Symbolic check against the
Cartan-derived Ricci tensor: `scripts/check_neutral_identity.py` (residual 0; the companion pair \(\log(a_3/a_2)\) also checks).

Bolt regularity (\(a_1=t+O(t^3)\), \(a_2,a_3=b+O(t^2)\)) gives \(W=b^2t+O(t^3)\), \(q=\log(b/t)+O(t^2)\),
\(Wq'\to-b^2\). With the Dirichlet radial Green function \(G(t)=\int_t^TW^{-1}=b^{-2}\log(b/t)+\gamma+o(1)\),
\(\Phi_G=q+GWq'\) has \(\Phi_G'=GW(V-E)\), \(\Phi_G(0)=-b^2\gamma\), \(\Phi_G(T)=0\) for an exact CH collar. Hence the two
intrinsic identities (no entrance slice, no entrance slope):
\[
\text{(I1)}\ \int_0^TW(V-E)\,dt=b^2,\qquad \text{(IG)}\ \int_0^TGW(V-E)\,dt=b^2\gamma .
\]
These are the only two neutral observables: \(\psi=\alpha+\beta G\) spans the kernel of \(\psi\mapsto(W\psi')'\).
Since \(P/(8\pi^2)=\tfrac14\int W|\operatorname{Ric}^\circ|^2dt\ge\tfrac18\int WE^2dt\),
\[
\frac{P}{8\pi^2}\ \ge\ \frac{\big(\int GWV-b^2\gamma\big)^2}{8R_G},\qquad R_G=\int_0^TG^2W\,dt .
\]
`scripts/neutral_flux_bolt.py` evaluates every term (the finite part \(\gamma\) is computed with the bolt logarithm removed
analytically; an early version offset \(t\) by evaluating at \(v=10^{-7}\) and gave a non-convergent \(\gamma\) — repaired).
(I1) and (IG) hold to \(10^{-10}\)–\(10^{-9}\) on all cells and the pointwise ODE residual is \(1.4\times10^{-4}\) (finite differences).

| cell | \(x_0\) | \(X\) | \(P\) | E-channel share of \(P\) | \(\int GWV\) | \(b^2\gamma\) | \(R_G\) | \((\int GWE)^2/(8R_G)\) |
|---|---|---|---|---|---|---|---|---|
| certified X=8 | .01 | 8 | .99911 | .510 | 1.5052 | −.0353 | .6728 | .4409 |
| continued | .01 | 64 | .99870 | .511 | 1.5097 | −.0354 | .6751 | .4421 |
| area branch | .003 | 64 | .99980 | .503 | 1.5900 | −.0124 | .8398 | .3822 |
| area branch | .015 | 64 | .99777 | .516 | 1.4623 | −.0498 | .6172 | .4631 |
| area branch | .02 | 64 | .99694 | .522 | 1.4194 | −.0631 | .5753 | .4776 |
| area branch | .03 | 64 | .99585 | .531 | 1.3419 | −.0874 | .5154 | .4954 |
| area branch | .05 | 64 | .99675 | .542 | 1.2102 | −.1286 | .4392 | .5101 |
| area branch | .1 | 64 | 1.01643 | .555 | .9763 | −.2091 | .3374 | .5205 |

Data: `data/neutral_flux/nf_*.json`. Probes show that \(\int GWE\), like \(P\) itself, is paid in the core: for the
X=8 cell 66% of \(\int GWE\) and 75% of \(P\) by \(t=0.1\), 97% and 99.4% by \(t=0.4\). The ratio \(a_2/a_1\) is already
\(1.04\) at \(t=0.4\) and \(1.0001\) at \(t=1.6\): the cheap cells do **not** shadow the peer's ACH Einstein fillings
(Rossi ratio \(\ge2.19\)); beyond the core they are small perturbations of CH.

**Scale regimes.** The compliance grows logarithmically as the bolt shrinks: a fit gives
\(R_G\approx0.144\log(1/x_0)+0.010\) (figure right panel). This is the four-dimensional logarithmic capacity of a small
sphere: in the flat annulus \(b\ll t\ll1\), \(W\approx t^3\), \(G\approx1/(2t^2)\), \(G^2W\approx1/(4t)\), whence
\(R_G\approx\tfrac14\log(1/b)=\tfrac18\log(1/x_0)\) (observed slope .144 includes CH curvature corrections). The numerator
\(\int GWE\) is invariant under the core rescaling \(t=b\tau\), \(W=b^3\widehat W\), \(G=b^{-2}\widehat G\), and stays \(\approx1.6\).
So the neutral observable certifies a share \(\sim c/\log(1/b)\to0\) as \(b\to0\): it is effective at moderate bolt scale,
and the small-bolt regime must be paid by the Chern–Weil whole-AE threshold instead (consistent with the data:
\(x_0=.001\) gives \(J=1.00002\), \(x_0=.003\) gives \(J\approx.9998\)).

**What this does and does not prove.** The displayed inequality is an identity-plus-Cauchy–Schwarz; it becomes a lower
bound only with independent control of the mismatch \(\int GWV-b^2\gamma\) for every competitor. For these cells the
mismatch is dominated by the potential transport \(\int GWV\), not by the finite part. Since \(a_3\) enters \(V\) and \(W\)
algebraically and the neutral equation is one second-order relation among three profiles, we expect (not yet shown)
that \(E\equiv0\) can be imposed on non-Einstein competitors by solving for \(a_3\), so the neutral observable alone
cannot prove a gap: it must be combined with the spin calibration / Chern–Weil charge which controls the remaining
49% of \(P\). The useful quantitative information is the regime map above.

## 2. Bolt area is a decisive variable: the area branch

All earlier continuation fixed \(x_0=0.01\). `scripts/run_area_branch.sh` and `run_area_branch2.sh` (with
`perp_collar_continue.py` now keeping the seed's \(x_0\)) optimize the same degree-\(d\) perpendicular ansatz at
\(x_0\in\{.003,.01,.015,.02,.03,.05,.07,.1,.15\}\) and continue physically \(X=8\to16\to32\to64\to128\to256\).
Table `data/perp_area/area_table.csv`, figure `figures/area_branch.png` (left). Selected \(J_6/(8\pi^2)\):

| \(x_0\) | X=8 | 16 | 32 | 64 | 128 | 256 |
|---|---|---|---|---|---|---|
| .003 | .99986 | .99982 | .99981 | .99980 | | |
| .01 | .99912 | .99890 | .99874 | .99870 | | |
| .015 | .99871 | .99824 | .99789 | .99777 | | |
| .02 | .99852 | .99757 | .99715 | .99694 | .99686 | .99680 |
| .03 | .99917 | .99726 | .99628 | **.99585** | .99567 | .99560 |
| .05 | 1.00404 | .99987 | .99774 | .99677 | .99630 | .99611 |
| .07 | 1.01386 | 1.00671 | 1.00357 | 1.00194 | 1.00122 | 1.00092 |
| .1 | 1.03606 | 1.02507 | 1.01927 | 1.01667 | 1.01549 | 1.01526 |
| .15 | 1.08803 | 1.06874 | 1.05961 | 1.05540 | 1.05342 | 1.05281 |

Increments in \(X\) decrease geometrically on each fixed-area row, so each row saturates; the optimum area moves outward
with \(X\) and settles near \(x_0\approx0.03\) (bolt geodesic radius \(\approx0.17\)), with an apparent limiting value
\(J_6/(8\pi^2)\approx0.9955\). Large bolts are strongly penalized (\(x_0=.15\): \(\approx1.053\)). Thus within this
diagonal ansatz the evidence points to an **interior** optimal bolt scale and saturation in the collar radius —
attainment-type behavior, neither bolt shrinking (excluded asymptotically by the AE threshold) nor bolt growth.
Degree-20 restart at \(x_0=.01,X=64\) changed \(J\) only by \(2\times10^{-7}\); the large-\(X\) optimizers stop with
gradient norms \(10^{-3}\)–\(10^{-2}\), so the table values are upper bounds for the ansatz, not converged minima.

**Certified.** `perp_rigorous_enclosure.py` now accepts an exact rational `--x0`. For \(x_0=3/100\), \(X=64\), degree 16
(`data/perp_area/rigorous_x00.03_X64_d16.json`, 192-bit Arb):
\[
\frac{J_6}{8\pi^2}\in[0.99585469086\pm6.7\times10^{-12}],\qquad \frac{P}{8\pi^2}\in[0.99584840759\pm5.5\times10^{-12}],
\]
\(\eta>0.0041453091430\), with \(\operatorname{Ric}=-6\) at the collar to \(3\times10^{-14}\) and finite bolt values. The
admissibility chain (explicit positivity of \(F,G\), \(f_1g_1=1\), \(w=O(y^2)\), perpendicular-slot \(D\#\overline{\mathbf{CP}}{}^2\)
topology, third-order CH contact, \(O(\delta^3)\) smoothing, \(g\mapsto6g\)) is independent of \(x_0>0\). The I54
transfer therefore gives, on an existential balanced cover sequence,
\[
\limsup_j\frac{\alpha(M_j)}{h_j}\le4-\frac{8\eta}{9}+\varepsilon<3.9963153+\varepsilon ,
\]
improving the Step-14 value \(3.998846902\) (deficit \(4-\text{coef}\) multiplied by \(3.2\)).
The \(X=128\), degree-20 cell (`data/perp_area/rigorous_x00.03_X128_d20.json`, 128-bit Arb, tol \(10^{-9}\)) gives
\(J_6/(8\pi^2)\in[0.9956689792,\,0.9956710815]\), \(P/(8\pi^2)\in[0.9956621671,\,0.9956632985]\), hence
\(\eta_{128}>0.0043289184910\) and
\[
\limsup_j\alpha(M_j)/h_j<4-8\eta_{128}/9+\varepsilon<3.9961521+\varepsilon .
\]
The \(X=256\) enclosure (`rigorous_x00.03_X256_d24.json`, task s15_t32_tool1) was still running at the end of Step 15;
a 192-bit, tol \(10^{-14}\) attempt timed out after 1500 s, so high degree/large \(X\) makes Arb integration slow.

## 3. Independent check of the peer ACH Einstein family

`scripts/einstein_shoot_independent.py` re-derives the bolt-regular series from scratch (free data \(b\) and \(r_4\);
\(p_3=-2/(3b^2)\), \(q_2=r_2=(3b^2+2)/(2b)\)) and bisects the AH/ACH separatrix. Results (`data/einstein_shoot/indep.json`):
at \(b=0.8\), \(|q_4-r_4|^*=0.286993\) (peer \(d^*=0.286979\)), Rossi plateau ratio \(a_2/a_1\approx2.195\) (min on plateau
\(2.192\)); \(b=0.7\): 2.201; \(0.9\): 2.219; \(1.1\): 2.323; \(2.0\): 3.176. This independently confirms
\(\rho_{\min}\approx2.19\) near \(b\approx0.8\). (My \(d\)-scan did not bracket the small-\(b\) separatrices \(b=.29,.55\).)

## 4. Consequences for the research line

1. The upper construction is governed by the bolt scale at least as much as by the collar radius; the next explicit
   improvements come from joint \((x_0,X)\) optimization with better stationarity, not from pair interactions.
2. The diagonal infimum appears to be attained at an interior bolt scale by a complete CH-asymptotic metric whose
   defect is concentrated in a core of radius \(\sim0.3\). A proof would combine: the Chern–Weil AE threshold for
   \(b\to0\); a large-bolt penalty (to be derived, e.g. from the aligned/perpendicular period response at large \(t\));
   and compactness in the middle regime with the neutral Green observable supplying a nondegenerate mismatch there.
3. The cheapest cells live far from the ACH Einstein fillings, so the ACH resistance mechanism of Step 14 is not where
   these cells pay; the core is.
