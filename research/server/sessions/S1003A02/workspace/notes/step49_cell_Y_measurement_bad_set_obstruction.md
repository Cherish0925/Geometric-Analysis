# Step 49 — The certified cell in Theorem-Y variables, the marginal triaxial Weyl split, and what unit-scale localization can establish

Session S1003A02, Agent3, Execute.

## 1. Yamabe/Weyl measurement of the authoritative cell

The new executable

- `workspace/scripts/step49_cell_theoremY_profile.py`
- `workspace/data/step49_cell_theoremY_profile_x003_X128.json`
- refinement `workspace/data/step49_cell_theoremY_profile_x003_X128_N1600.json`

reconstructs the diagonal Bianchi–IX curvature of A01's degree-20, \(x_0=.03\), \(X=128\) perpendicular cell, solves the scalar \(-24\) conformal equation, rescales to the scalar \(-4\) convention of Theorem Y, and integrates the eigenvalue formulas for \(\Psi\). This is floating quadrature, not an interval enclosure. The defect integral is stable to the displayed digits,
\[
 P/(8\pi^2)=0.99566273276218,
\]
consistent with the existing exact certificate. The Yamabe factor has \(w(0)=3.1484\times10^{-4}\) and a tiny negative far-tail undershoot \(1.14\times10^{-8}\).

A normalization correction is essential. In scalar \(-4\) units define barred quantities by division by \(8\pi^2\). The Step-39 conformal ledger gives, on the finer current A01 evaluation,
\[
 1-\bar P(\widehat g)=0.0043391,\qquad
 \bar\Delta V=0.053096,\qquad
 \delta\bar W=0.018784,
\]
where \(\delta\bar W\) is the conformal self-dual Weyl deficit relative to the CH ball. The Theorem-Y quantity is
\[
 \bar D_W=\delta\bar W+\frac23\bar\Delta V\simeq0.05418,
\]
so
\[
 4\bar D_W\simeq0.21672,\qquad 4\bar\Delta V\simeq0.21238,
 \qquad 4(\bar D_W-\bar\Delta V)=0.0043391.
\]
Thus the earlier numbers \(0.07513\) and \(0.07080\) were not \(4D_W\) and \(4\Delta V\): they were \(4\delta\bar W\) and \((4/3)\bar\Delta V\), the two terms in the equivalent cell formula
\[
 1-\bar P(\widehat g)=4\delta\bar W-\frac43\bar\Delta V.
\]
The local script imports the older Step-39 finite-grid ledger, giving \((\bar\Delta V,\bar D_W)=(0.0531062,0.0541909)\). A01's newer tail-free identity, \(\bar\Delta V\simeq0.0530963\), is authoritative; the small difference is the old relative-volume error. The script's \(D_W\) is identity-derived, \(D_W=\Delta V+(1-P)/4\), not an independent Weyl integration. The identity must not be reconstructed by subtracting two large raw radial integrals.

The new spectral integrations converge between 10,644 and 26,992 quadrature nodes to
\[
 \frac1{8\pi^2}\int\Psi=0.0132326119,
 \qquad
 \frac1{8\pi^2}\int\operatorname{dist}(W^+,\mathcal K)^2=0.00750240585,
\]
\[
 \frac{\int\Psi}{\int\operatorname{dist}^2}=1.76378247,
 \qquad
 \frac1{8\pi^2}\int4\sigma^2=0.0109217156.
\]
Hence \(2\int\Psi/(8\pi^2)=0.0264652\). The correct Theorem-Y allowance for a closed replica is \(4\bar\Delta V-(1-\bar P(\widehat g))\simeq0.2081\); the earlier number \(0.0332\) came from the same mistaken channel identification and is withdrawn. The LeBrun magnitude penalty is \(0.00429707\). In a formal closed replication carrying the required sign-family fields, the Theorem-Y right side would be \(0.18596\), with slack \(0.18162\); LeBrun's right side would be \(0.20813\), with slack \(0.20379\). The cell therefore lies far from Theorem-Y equality and from the zero-period version of LeBrun equality. A statement about full LeBrun equality for a genuine closed replica additionally requires its period term \(\Pi_g\). Its conversion efficiency is only
\[
 \frac{1-\bar P(\widehat g)}{4\bar\Delta V}\simeq0.0204,
\]
whereas the formal diffuse common mode is asymptotically field-extremal.

The spectral geography is also informative. The least eigenvalue parameter \(x=-\mu_{\min}\) ranges from about \(0.1873\) to \(0.666686\), and the upper-pair half-splitting reaches \(0.3021\). The \(\mu_{\min}\)-eigenline is the harmonic/Kähler slot except in the thin bolt layer \(x\in[.03,.0315]\). Radial quantiles place 50% of \(\Psi\) by \(x\simeq0.814\), 90% by \(x\simeq16.38\); the Ricci defect is much more concentrated, with 90% by \(x\simeq0.111\). A01's independent chiral ledger gives
\[
 \frac1{8\pi^2}\int|W^-|^2=1.4812.
\]
Thus the orbit penalty has a long but integrable geometric tail, while the direct defect is a bolt/core phenomenon. Here the first \(x\) is the spectral parameter \(-\mu_{\min}\); the interval and quantiles refer to the radial coordinate. The measurement does not supply a cell lower estimate: the strict saving is a small difference of substantially larger Weyl and relative-volume channels.

## 2. Exact first-order Weyl splitting of the marginal \(\nu=4\) tail

Let the CH metric in diagonal Bianchi–IX form have
\[
 A=B=\sinh r=:s,\qquad C=\sinh r\cosh r,
\]
and perturb the two horizontal directions by
\[
 A=s(1+\varepsilon q),\qquad B=s(1-\varepsilon q),\qquad C=sc,
 \qquad q=e^{-4r}.
\]
Using the Step-27 chiral variables
\[
 v_i=A_i'-\gamma_i,
 \qquad
 R^+_{ii}=-\frac{v_i'}{2A_i}
 +\frac{-v_i-v_jv_k/2}{A_jA_k},
\]
the background has \(v_1=v_2=0\), \(v_3=3s^2\). The first variations are
\[
 \delta v_1=d=4q(\operatorname{sech}r-\sinh r),
 \qquad \delta v_2=-d,
 \qquad \delta v_3=0.
\]
Therefore
\[
 \delta R^+_{11}=-\frac{d'}{2s}
 +\frac{d(3s^2/2-1)}{s^2c},
 \qquad
 \delta R^+_{22}=-\delta R^+_{11},
 \qquad
 \delta R^+_{33}=0,
\]
and direct asymptotics give
\[
 e^{4r}\delta W^+\longrightarrow
 \operatorname{diag}(-12,12,0)
\]
in the \((A,B,C)\) spin basis at \(\operatorname{Ric}=-6g\). After scaling to scalar \(-4\), the first-order upper-pair changes are \((-2,2)\varepsilon e^{-4r}\), while the least/fibre eigenvalue is unchanged. Consequently
\[
 \left.\partial_\varepsilon\right|_0\mu_{\min}=0,
 \qquad
 \left.\partial_\varepsilon\right|_0|W^+|^2=0,
 \qquad
 \sigma=2|\varepsilon|e^{-4r}+O(|\varepsilon|e^{-6r})+O(\varepsilon^2e^{-8r}),
\]
where \(\sigma\ge0\) is the sorted upper-pair half-gap. These are first-order asymptotics; the \(O(|\varepsilon|e^{-6r})\) term is linear but faster decaying.
Theorem K sees a linear distance
\[
 \operatorname{dist}(W^+,\mathcal K)
 =2\sqrt2\,|\varepsilon|e^{-4r}+O(|\varepsilon|e^{-6r})+O(\varepsilon^2e^{-8r}),
\]
which is marginal against CH volume growth \(e^{4r}\). Theorem Y sees the splitting term
\[
 \Psi=4\sigma^2+\cdots=16\varepsilon^2e^{-8r}+O(\varepsilon^2e^{-10r})+\cdots,
\]
which is integrable. This proves the qualitative possibility left open in Step 48: the \(\nu=4\) triaxial Einstein tail has a linear upper-pair split, logarithmic/length growth in the Theorem-K \(L^1\) quantity, and finite Theorem-Y quadratic cost. The reduced exact script `workspace/scripts/step49_triaxial_weyl_tail.py` writes `workspace/data/step49_triaxial_weyl_tail.json` and verifies the leading coefficient \(-12\), the next linear coefficient \(+96e^{-6r}\), and the scalar-\(-4\) constants \(2,2\sqrt2,16\) for \(\sigma\), distance, and \(\Psi\).

## 3. The proposed unconditional bad-ball count does not follow from the present hypotheses

The desired entry theorem would label a unit ball good when, after gauge, it is \(C^{2,\alpha}\)-close to CH, and infer linearly many disjoint bad balls from subunit saving. The available all-metric information does not support that conclusion.

First, arbitrary scalar \(-4\) metrics do not solve a critical elliptic curvature equation. Failure of unit-ball \(C^{2,\alpha}\) closeness is therefore not the contrapositive of a small-energy regularity theorem. High-frequency or very concentrated metric changes can fail the pointwise hypothesis without a fixed unit of \(P\), and the Riemannian estimate 48.L starts only after the gauge and \(C^{2,\alpha}\) entrance have been supplied.

Second, Theorem K is additive as an integral but does not separate topology carriers. An order-\(k\) Weyl departure can be concentrated in one unit ball. Multi-centre ALF/ALE clusters provide the relevant topology-carrying model: many exceptional classes may occur inside one link. No current theorem bounds the Weyl energy, volume, exceptional charge, or number of classes carried by one bad ball. Hence an order-\(k\) integral lower bound yields an order-\(k\) bad *weight*, not linearly many geometrically distinct balls. Even a per-ball load bound would not suffice by itself if the nominally good region can accumulate order-\(k\) \(L^1\) departure through the \(L^1/L^2\) mismatch; one also needs a localized Theorem-Y/volume-flux estimate suppressing diffuse good-region weight.

Third, an arbitrary metric on \(X\#k\overline{\mathbb{CP}}^{\,2}\) has no canonical global identification with a ball quotient away from preassigned cores. A unit-scale good/bad decomposition must first construct a reference map or arise from a selected minimizing object; otherwise CH closeness on different balls need not assemble into one marked bulk.

There is an unconditional weighted relation at scalar \(-4\):
\[
 \int_M\left(|W^+|^2+\frac13\right)d\mu
 =2\pi^2(A-k)+\frac14P.
\]
Writing \(d_K=\operatorname{dist}(W^+,\mathcal K)\) and \(\mathcal L=(8\pi^2k-P)_+/(4\sqrt6/3)\), the exact eigenvalue formula \(d_K^2=|W^+|^2+2/3-2(-\mu_{\min})\) gives \(d_K^2\le2(|W^+|^2+1/3)\). Theorem K therefore yields the fully global weighted statements
\[
 \mathcal L^2\le \operatorname{Vol}(M)\,[4\pi^2(A-k)+P/2],
\]
and, for \(B_\tau=\{d_K>\tau\}\),
\[
 \operatorname{Vol}(B_\tau)\ge
 \frac{(\mathcal L-\tau\operatorname{Vol}M)_+^2}{4\pi^2(A-k)+P/2}.
\]
These are departure-volume estimates, not atom counts.
If a region \(G\) already admits a good-ball estimate
\[
 \int_G\operatorname{dist}^2
 \le C\left(P(G_1)+\varepsilon_0^2\operatorname{Vol}(\text{margin})\right),
\]
then splitting Theorem K over \(G\cup B\), Cauchy–Schwarz, and
\[
 \operatorname{dist}(W^+,\mathcal K)^2
 \le2|W^+|^2+\frac23
\]
give
\[
 \frac{8\pi^2k-P}{4\sqrt6/3}
 \le \sqrt{\operatorname{Vol}(G)\,C(P(G_1)+\varepsilon_0^2V_{\rm margin})}
 +\sqrt{V_B\left(2\int_B|W^+|^2+\frac23V_B\right)}.
\]
This forces good-region defect or weighted bad-region Weyl/volume concentration. It does not force a lower bound for the number of disjoint bad balls. Such a count would become valid after an additional per-ball upper bound on Weyl/volume/topological charge, or after variational selection supplies an approximate Euler–Lagrange equation, small-energy regularity and energy quantization. That is exactly the missing minimizer-entry step suggested by the Coulomb source architecture.

Theorem 48.L does imply, on a genuinely CH-close marked bulk, that the *flux-corrected* bulk excess obeys
\[
 \left|\Delta V_{\rm bulk}-\frac14\int_{\partial\Omega}\partial_\nu\operatorname{tr}h\right|
 \le C(P_{\rm bulk+margin}+\Lambda^2)
\]
in scalar \(-4\) units. The uncorrected volume retains the displayed linear interface flux. It does not bound the core contribution to the free Yamabe excess \(\Delta V_{\rm free}=\Delta V-2\pi^2\Pi_g\). A01's cell ledger shows why: the core has \(\bar\Delta V\simeq0.0531\) while the direct saving is only \(0.00434\). Thus localized CH coercivity makes diffuse bulk efficiency small, but a global inequality still requires the complete core/field/volume mechanism.

## 4. Resulting direction

The cell measurement strengthens, rather than closes, the volume-channel picture. Certified cells are inefficient, localized realizations: \(D_W/\Delta V\simeq1.0204\) and only about 2% of \(4\Delta V\) appears as direct saving. The formal common mode is diffuse and nearly saturates the field estimates. The marginal triaxial tail explains why Theorem K can accumulate a long linear signal while Theorem Y remains localized.

The next global theorem should therefore be built for selected near-minimizers: preserve the infimum, derive an approximate fourth-order equation (or a controlled penalized equation), prove scalar-normalized small-energy regularity, and then obtain a weighted concentration/quantization alternative. The natural selection functional is \(P+\varepsilon\int|\nabla\mathrm{Rm}|^2\) or an Ekeland-selected approximate minimizer of \(P\); the former supplies ellipticity at fixed \(\varepsilon\) but requires estimates that survive \(\varepsilon\downarrow0\), while the latter requires writing the approximate Euler–Lagrange residual in a norm compatible with local regularity. Only after each atom has controlled volume, Weyl energy, interface flux and topological load can an atom count or complete-cell inequality constrain every competing geometry. Without that new variational input, the proposed all-metric count is not mathematically available.