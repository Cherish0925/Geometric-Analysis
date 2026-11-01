# Step 52 — The residual norm, frozen-weight selection, and Kronheimer absorption of exceptional classes

> **Binding erratum (Steps 70, 86–88; see `theorem_package_v1.md` §13).** This note predates the Step-70 split between the trace-free infimum \(P_*=\inf\int|\mathrm{Ric}^\circ|^2\) and the human-defect infimum \(\alpha=\inf\mathscr D\). Every infimum here that appears as the limit of \(P(g_i)\), in a \(P\)-flow estimate, or in a \(P\)-Palais–Smale statement is \(P_*\), not \(\alpha\); the symbols \(\alpha,\alpha_{\rm orb},\alpha^\iota\) below should be read as \(P_*,P_{*,\rm orb},P_*^\iota\). The factor \(\tfrac12\) in Corollary 52.8 and in §5.7 belongs only to \(P\): \(P_*(X\#2\overline{\mathbb{CP}}^2)\le\tfrac12P_*^\iota(X\#X)\). For \(\mathscr D\), finite orbifold covers preserve the functional, so \(\alpha(X\#2\overline{\mathbb{CP}}^2)\le\alpha_{\rm orb}(X\#S^4/\mathbb Z_2)=\alpha^\iota(X\#X)\), **with no factor \(\tfrac12\)**. Ricci-flat ALE resolution of an Einstein orbifold gives \(P_*=0\); it gives \(\alpha=0\) when the Einstein constant is nonzero (Lemma 86.S), and on negative-Yamabe targets the Einstein constant must be negative. The sentence "\(k=1\) is never fully absorbed" holds for root lattices contained in \(\mathbb QE\); mixed host–exceptional root lattices need additional degree-one/SW\(_L\) hypotheses. The double cover of \(X\#m(S^4/\mathbb Z_2)\) is \(X\#X\#(m-1)(S^1\times S^3)\) (two punctured copies of \(X\) joined by \(m\) twice-punctured \(S^4\) covers), with \(2m\) isolated fixed points. For ball-quotient \(X\), the \(S^4/\mathbb Z_2\) channel has exact orbifold deficit \(4\pi^2(A/3-2m)\) (Theorem 87.O, package §22.6(6)) and cannot cross \(h=1/3\). Theorem 93.A (`step93_paired_A1_transfer_review.md`) strengthens this: \(X\#m(S^4/\mathbb Z_2)\) carries no Einstein orbifold metric for any \(m>0\), with \(P_{*,\rm orb}=16\pi^2m\) never attained and \(\alpha_{\rm orb}=\min\{1,8m/(A+2m)\}\). The transferred filler screen for all known Ricci-flat fillers is in `step94_filler_screen_dichotomy.md`.

Session S1003A02, Agent2, Execute. Builds on `step51_residual_entry_link_charges_and_kahler_recovery.md` (corrections of Step 50),
the Theorem-G link calculus, and Theorem \(K_\infty\). Script/data: `workspace/scripts/step52_absorption_lattice.py`,
`workspace/data/step52_absorption_lattice.json`.

Notation: \(P(g)=\int|\mathrm{Ric}^\circ|^2\), \(Q=\operatorname{grad}_{L^2}P\), \(\operatorname{tr}Q=c_0\Delta s\) with \(c_0\neq0\)
(scale invariance), energy \(\int|\mathrm{Rm}|^2\) bounded on \(\{P\le C\}\) by Gauss–Bonnet. For \(\varepsilon>0\) and a cap \(r_0\) the
**energy radius** is
\[
r_\varepsilon(x)=\sup\Big\{r\le r_0:\int_{B(x,r)}|\mathrm{Rm}|^2\le\varepsilon\Big\},\qquad |r_\varepsilon(x)-r_\varepsilon(y)|\le d(x,y).
\]
For \(q>2\) the \(L^q\) **curvature radius** is \(r^{(q)}(x)=\sup\{r\le r_0:\ r^{2q-4}\int_{B(x,r)}|\mathrm{Rm}|^q\le1\}\).

Three results. §1 decides the residual norm: an own-scale \(L^2\) residual is exactly borderline — enough for compactness and exact
critical limits, not for pointwise curvature control; point-picking must use an integral radius. This removes the derivative hypothesis
(R) from the Step-51 conditional structure theorem. §2 replaces Lemma W by a frozen-weight time-stepping construction whose only missing
input is a Kuwert–Schätzle-type concentration lemma for the \(P\)-flow. §3 proves that exceptional classes can be carried at zero
\(P\)-cost by Eguchi–Hanson and \(A_3\) Kronheimer bubbles: \(X\#2m\overline{\mathbb{CP}}^2\) and \(X\#3\overline{\mathbb{CP}}^2\) are
resolutions of orbifolds whose rational lattice contains no exceptional class. This corrects the proposed "Einstein-orbifold with every
exceptional class in the bulk" characterization and yields a new inequality linking blow-ups to \(\mathbb Z_2\)-symmetric connected sums.

---

## 1. The residual norm

### Proposition 52.1 (approximate fourth-order compactness at a controlled scale)
Let \(g_i\) be metrics on \(B_i=B_{g_i}(x_i,2)\) with: harmonic coordinates on \(B(x_i,1)\) with \(C^{1,\beta}\)-control (e.g. from
\(\int_{B(y,1/2)}|\mathrm{Rm}|^6\le\Lambda\) for all \(y\) plus a Sobolev bound — see 52.4), \(\|\mathrm{Rm}\|_{L^6(B_i)}\le\Lambda\), and
\(\int_{B_i}|Q(g_i)|^2\to0\). Then in harmonic coordinates \(\|g_i\|_{W^{4,2}(B(x_i,1/2))}\le C(\Lambda)\), a subsequence converges in
\(W^{3,p}\) (\(p<4\)), hence in \(C^{1,\beta}\) and \(W^{2,q}\) (\(q<\infty\)), with \(\mathrm{Rm}_i\to\mathrm{Rm}_\infty\) in every \(L^q\), \(q<\infty\);
the limit satisfies \(Q(g_\infty)=0\) and is smooth.

*Proof.* Harmonic coordinates: \(g^{kl}\partial_k\partial_lg_{ij}=-2\mathrm{Ric}_{ij}+B_{ij}(g,\partial g)\), \(B\) quadratic in \(\partial g\);
\(\mathrm{Ric}\in L^6\Rightarrow g\in W^{2,6}\subset C^{1,1/3}\). Trace equation \(c_0\Delta_gs=\operatorname{tr}Q\in L^2\) (no first-order terms
in harmonic coordinates) gives \(s\in W^{2,2}\). The \(Q\)-equation has the triangular form
\(\Delta\mathrm{Ric}=a\nabla^2s+b(\Delta s)g+\mathrm{Rm}*\mathrm{Ric}+\mathrm{Ric}*\mathrm{Ric}+Q\); in coordinates the rough Laplacian is
\(g^{kl}\partial^2_{kl}+\Gamma\partial+\partial\Gamma+\Gamma\Gamma\) with \(\partial\Gamma\cdot\mathrm{Ric}\in L^3\), \(\mathrm{Rm}*\mathrm{Rm}\in L^3\), so
\(\mathrm{Ric}\in W^{2,2}\subset W^{1,4}\). Differentiating the harmonic-coordinate equation once (\(\partial g^{kl}\partial^2g\in L^6\)) gives
\(g\in W^{3,4}\); twice (\(\partial^2B\sim\partial g\,\partial^3g+\partial^2g\,\partial^2g\in L^2\), \(\partial^2\mathrm{Ric}\in L^2\)) gives
\(g\in W^{4,2}\). Compactness \(W^{4,2}\Subset W^{3,p}\), \(p<4\); \(\mathrm{Rm}\in W^{2,2}\Subset L^q\). In \(Q(g)\) the top term is linear in
\(\partial^4g\) with coefficients in \((g,\partial g)\), the rest is \(\partial^3g\,\partial g\), \(\partial^2g\,\partial^2g\), …, all converging strongly,
so \(Q(g_i)\to Q(g_\infty)\) in distributions and \(Q(g_\infty)=0\). Smoothness: \(s\) is \(g_\infty\)-harmonic, the gauged system
(\(B^{1/6}=0\), elliptic for \(t\neq0\) by GV Prop. 3.3) bootstraps from \(W^{4,2}\). \(\square\)

### Proposition 52.2 (borderline: an \(L^2\) residual does not control curvature pointwise)
In dimension four, \(\|\Delta u\|_{L^2}\to0\) and \(\|u\|_{L^q}\to0\) do not force \(u(0)\to0\). Example: \(h_\sigma=|x|^{-2}(\log\frac1{|x|})^{-1}\)
on \(\sigma<|x|<\sigma^{1/2}\), \(u_\sigma=\Gamma*h_\sigma\) (\(\Gamma=\frac1{4\pi^2|x|^2}\)): \(\|h_\sigma\|_2^2\sim1/\log\frac1\sigma\to0\) while
\(u_\sigma(0)=\frac1{4\pi^2}\cdot2\pi^2\int_\sigma^{\sigma^{1/2}}\frac{dr}{r\log(1/r)}=\frac{\log2}{2}\), and \(u_\sigma\to0\) in \(L^q_{\rm loc}\).
Since \(c_0\Delta s=\operatorname{tr}Q\) exactly, scalar curvature can carry such a logarithmic cloud: along a sequence with \(\int|Q|^2\to0\) the
curvature at a point need not converge, and a limit can be flat at a point where \(|\mathrm{Rm}_i|=1\). Hence:

* the residual \(L^2\) at own scale gives \(\mathrm{Rm}\in W^{2,2}\) (VMO, every \(L^q\)), harmonic radius, and exact critical limits;
* it does **not** give \(L^\infty\) curvature bounds on the approximating metrics (an \(L^{2+\eta}\) own-scale residual would);
* any blow-up/point-picking argument must use a radius that is continuous under \(W^{2,q}\)-convergence: \(r_\varepsilon\) or \(r^{(q)}\),
  **not** the \(\sup|\mathrm{Rm}|\) radius used in Step 50.

### Proposition 52.4 (\(L^6\) small-energy regularity with residual)
For every \(C_S\) there are \(\varepsilon_0,\eta_0,C\) such that: if \(B(x,r)\) satisfies \(\int_{B(x,r)}|\mathrm{Rm}|^2\le\varepsilon_0\), the
scale-invariant Sobolev inequality with constant \(C_S\) on balls in \(B(x,r)\), and \(r^4\int_{B(x,r)}|Q|^2\le\eta_0\), then
\(r^{8}\int_{B(x,r/2)}|\mathrm{Rm}|^6\le C\).

*Proof by contradiction.* Otherwise, after rescaling \(r=1\), choose by point-picking (with the usual distance-to-boundary weight) points
\(y_i\) where \(r^{(6)}(y_i)=\lambda_i\to0\) and \(r^{(6)}\ge\lambda_i/2\) on \(B(y_i,A_i\lambda_i)\), \(A_i\to\infty\). Rescale by
\(\lambda_i\): \(r^{(6)}\ge1/2\) on growing balls, \(\int_{B(y_i,1)}|\mathrm{Rm}|^6=1\), energy \(\le\varepsilon_0\), Sobolev \(\le C_S\) (scale
invariant), residual \(\le\lambda_i^4\eta_0\to0\) (subcritical gain). An \(L^6\)-curvature bound with a Sobolev bound gives a lower bound
for the \(C^{1,\beta}\) harmonic radius (integral-curvature harmonic-radius theorem, \(p=3>n/2\); literature input to be pinned
down — Yang/Anderson–Petersen–Wei type). Proposition 52.1 gives convergence with \(\mathrm{Rm}\) strongly in \(L^6\), so the limit is a
complete, noncompact (Euclidean volume growth from Sobolev), exact \(P\)-critical metric with \(\int_{B(y,1)}|\mathrm{Rm}|^6=1\) and
\(\int|\mathrm{Rm}|^2\le\varepsilon_0\). Its scalar curvature is harmonic and in \(L^2\), hence \(0\) (Yau); so the limit is Bach-flat and
scalar-flat, and Tian–Viaclovsky small-energy regularity on \(B(y,R)\), \(R\to\infty\), gives \(\sup_{B(y,R/2)}|\mathrm{Rm}|\le
CR^{-2}\varepsilon_0^{1/2}\to0\): flat, contradiction. \(\square\)

### Theorem 52.3 (conditional structure theorem, hypotheses reduced)
Let \(g_i\) be unit-volume, \(P(g_i)\to\alpha(M)\), with
\[
(\mathrm{PS}_\varepsilon)\quad \int_M r_{\varepsilon,i}^4\,|Q(g_i)|^2\,d\mu_{g_i}\to0,\qquad
(\mathrm{S})\ \text{uniform scale-invariant local Sobolev bound}
\]
(\(\varepsilon\le\varepsilon_0\), cap \(r_0=1\)). Then all conclusions of the Step-51 theorem hold (orbifold \(P\)-critical bulk with
constant \(s\) on regular components; scalar-flat Bach-flat ALE bubbles; \(\alpha\ge P(g_\infty)+\sum P(N_b)\); attainment without
concentration; Einstein/Ricci-flat structure when \(\alpha=0\); link-gluing topology with the Theorem-G ledger), **without** the derivative
hypothesis (R). Convergence away from the concentration points is in \(C^{1,\beta}\cap W^{2,q}\) (smooth on the limit, \(W^{4,2}\)-weak along
the sequence).

*Proof.* On \(B(x,r_\varepsilon(x)/2)\) the weight is comparable (Lipschitz property), so the rescaled residual is small and Prop. 52.4 gives
\(L^6\) control at scale \(r_\varepsilon\), hence harmonic radius \(\gtrsim r_\varepsilon\). The concentration set (where \(r_\varepsilon\to0\))
is finite by the energy bound; Anderson's good/bad-ball construction with \(r_\varepsilon\) in place of the curvature radius yields the orbifold
limit; at each bubble scale the rescaled residual \(\to0\) and Prop. 52.1 gives exact critical limits; ALE structure and Bach-flatness are as in
Step 51 (exact critical limits only). (NC) follows from (S). \(\square\)

Remark. \((\mathrm{PS}_\varepsilon)\) is stronger than the curvature-radius residual, since \(r_\varepsilon\ge c\rho\) wherever the curvature radius
\(\rho\) is defined (\(|\mathrm{Rm}|\le\rho^{-2}\) on \(B(x,\rho)\) and Bishop volume give \(\int_{B(x,c\rho)}|\mathrm{Rm}|^2\le Cc^4\)). Low-energy
high-curvature clouds are invisible to the structure theorem but require the stronger weight.

---

## 2. Selection: frozen-weight time stepping

### 2.1 The weighted flow as a horizontal gradient flow
For a positive weight \(w\) define on the tangent space at \(g\) the scale-invariant metric \(\langle h,h\rangle_{w,g}=\int w^{-1}|h|^2d\mu\). The
gradient of \(P\) for it is \(wQ\); the flow \(\partial_tg=-wQ\) is **horizontal** (\(\langle wQ,\mathcal L_Xg\rangle_w=DP(\mathcal L_Xg)=0\)),
has dimensionless time when \(w\) scales like length\(^4\), speed \(\|\partial_tg\|_w=(\int w|Q|^2)^{1/2}\), and length
\(\le\int(\int w|Q|^2)^{1/2}dt\le\sqrt{T\,\delta}\). Volume can be renormalized by \(\lambda(t)g\) at no cost (\(\int\operatorname{tr}Q=0\)).

Two warnings that shape the construction. (i) A pointwise weight such as \((|\mathrm{Rm}|^2+V^{-1})^{-1}\) is unusable: at zeros of
\(|\mathrm{Rm}|\) inside a curved region it jumps to the global value and the flow runs locally at the wrong rate. (ii) Length in the
\(w\)-metric does not see derivatives: ripples of amplitude \(a\), frequency \(\nu\) change the energy radius at cost \(a^2\sim\nu^{-4}\).
So no scale control follows from the length bound alone; it must come from parabolic smoothing.

### 2.2 Construction
Given \(g_0\) with \(P(g_0)=\alpha+\delta\): set \(t_0=0\). At step \(n\), freeze a smooth weight \(w_n\) with
\(c\,r_\varepsilon(g(t_n))^4\le w_n\le C\,r_\varepsilon(g(t_n))^4\) and own-scale derivative bounds (a mollification of \(r_\varepsilon\) over
own-scale balls, available at positive times when the geometry is smooth at own scale), run the fixed-weight DeTurck flow (Step-51 §1.2,
data-dependent existence is unconditional) on \([t_n,t_{n+1}]\), and refreeze. Each step obeys \(P'=-\int w_n|Q|^2\) exactly.

### Lemma 52.KS (as first formulated — FALSE at a fixed threshold; corrected form KS′ in §5)
There are \(\varepsilon_1,c_1,C_1\) depending on the Sobolev constant such that, for a fixed-weight flow as in 2.2 started at
\(g(t_n)\) with Sobolev constant \(\le C_S\): the flow exists on \([t_n,t_n+c_1]\), \(\tfrac12r_\varepsilon(g(t_n))\le r_\varepsilon(g(t))\le
2r_\varepsilon(g(t_n))\) pointwise there, the Sobolev constant stays \(\le2C_S\), and at \(t_n+c_1\) the geometry is smooth at own scale
with universal constants.

This is the dimension-critical analogue of the Kuwert–Schätzle concentration lemma for Willmore flow (lifespan \(\ge c\rho^4\) where \(\rho\)
is the \(L^2\)-curvature concentration radius) and of Struwe's local energy inequality, transposed to own-scale time by the weight. Its proof
needs a localized energy identity: \(\int\varphi|\mathrm{Rm}|^2\) is a combination of \(\int\varphi\,\mathrm{Pf}\) (a transgression, changing only by
an annular flux in \(\partial_tg,\nabla\partial_tg\)), \(\int\varphi|\mathrm{Ric}^\circ|^2\) (dissipated up to flux), and \(\int\varphi s^2\); the Weyl
part is not dissipated directly and must be controlled through the Bianchi system \(\delta W\sim\nabla\mathrm{Ric}\).

### Theorem 52.5 (selection, conditional on Lemma 52.KS and Sobolev persistence)
If Lemma 52.KS holds and the Sobolev constant stays bounded along the construction, take \(t_{n+1}=t_n+c_1\) for \(n\ge1\). The construction
runs for infinite time and the step dissipations \(D_n=\int_{t_n}^{t_{n+1}}\int w_n|Q|^2\) satisfy \(\sum_nD_n\le\delta\), so \(D_n\to0\); inside step
\(n\) some \(t\) has \(\int w_n|Q(g(t))|^2\le D_n/c_1\), and by the comparability in 52.KS
\[
\int r_\varepsilon(g(t))^4|Q(g(t))|^2\le C\,D_n/c_1\longrightarrow0,\qquad P(g(t))\le P(g_0).
\]
Applied to a minimizing sequence, this produces a \((\mathrm{PS}_\varepsilon)\) minimizing sequence on the same manifold, and Theorem 52.3 applies.
No smooth dependence of the weight on \(g\), no comparison with the input scale, and no uniformity in \(g_0\) for the first step are needed.

Status: the construction, energy law, horizontality and the reduction are proved; Lemma 52.KS is the single open analytic lemma of the entry
programme (plus Sobolev persistence, which is the noncollapsing hypothesis in flow form; Streets' Remark 1.12 records the corresponding open
problem for unweighted fourth-order flows).

---

## 3. Kronheimer absorption of exceptional classes

### Lemma 52.6 (lattice absorption)
Let \(R\) be a negative-definite ADE root lattice (the \(H_2\) of a Kronheimer ALE space, or a sum of them) embedded in a closed oriented
\(M\) as the lattice of disjoint resolution configurations. An exceptional class \(E\in H_2(M;\mathbb Z)\), \(E^2=-1\), is *absorbed* if \(E\in
R\otimes\mathbb Q\). Absorption requires an integral overlattice of \(R\) containing norm \(-1\) vectors. Facts (script, §1–2 of the JSON):
\(A_1\), \(A_2\), \(E_6\), \(E_7\) have nonsquare discriminant (no overlattice); \(E_8\) is even unimodular; the index-3 overlattice of \(A_8\) is
\(E_8\); but
\[
A_1\oplus A_1\subset\mathbb Z^2\ (E_{1,2}=\tfrac12(e\pm f)),\qquad A_3=D_3\subset\mathbb Z^3,\qquad D_n\subset\mathbb Z^n,\qquad (A_1\oplus A_1)^m\subset\mathbb Z^{2m},
\]
all of index 2 (resp. \(2^m\)). A single Eguchi–Hanson bubble absorbs nothing; two absorb two classes; one \(A_3\) bubble absorbs three.
A single \(A_1\) cannot absorb a class; \(k=1\) cannot be absorbed if the whole root span is required to lie in \(\mathbb QE\) (a root \(a=qE\) would need \(q^2=2\)); without that restriction a larger lattice could mix \(E\) with classes of \(X\) (see §5).

### Theorem 52.7 (smooth realizations)
(a) Let \(\iota\) act on \(S^4\subset\mathbb C^2\times\mathbb R\) by \((z,x)\mapsto(-z,x)\); \(S^4/\mathbb Z_2\) has two isolated points with group
\(\{\pm1\}\subset SU(2)\) (for either orientation). Gluing Eguchi–Hanson spaces at both points with the orientation for which
\(\tau=-2\) gives a closed manifold \(\widehat{S^4/\mathbb Z_2}\) diffeomorphic to \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\), in which the two
\((-2)\)-spheres represent \(E_1\pm E_2\).
*Proof.* \(\chi=4\), \(\tau=-2\) (EH: \(\chi=2,\tau=-1,\eta=0\)); simply connected (EH simply connected, \(\pi_1(\mathbb{RP}^3)\to\) both sides
onto); the \(T^2\)-action on \(\mathbb C^2\times\mathbb R\) commutes with \(\iota\) and lifts to the toric EH resolutions, giving an effective
\(T^2\)-action; by Orlik–Raymond the manifold is a connected sum of \(S^4,\pm\mathbb{CP}^2,S^2\times S^2\); negative definiteness of rank two
leaves \(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\). The overlattice is the unique unimodular one, \(\mathbb Z^2\), with \(e,f\mapsto E_1\pm E_2\). \(\square\)

(b) Let \(B\) be the rational ball (\(\pm B_2\), \(B_2=\mathbb{CP}^2\setminus N(\text{conic})\), \(\pi_1B_2=\mathbb Z_2\)) with
\(\partial B=-\partial(A_3\text{ plumbing})=-L(4,3)\cong L(4,1)\), and \(\Sigma_4=B\cup\operatorname{cone}\), an orbifold with one point
\(\mathbb C^2/\mathbb Z_4\) of weights \((1,3)\) (the \(A_3\) singularity). Resolving by the \(A_3\) Kronheimer space gives a closed negative-definite
manifold \(Q_3\) with \(b_2=3\), simply connected (\(\pi_1L(4,\cdot)=\mathbb Z_4\to\pi_1B=\mathbb Z_2\) onto), whose lattice is the unimodular
overlattice \(\mathbb Z^3\supset A_3\); the three exceptional classes lie in \(A_3\otimes\mathbb Q\) (\(E_1=\tfrac12a_1+a_2+\tfrac12a_3\), etc.).
By Freedman–Donaldson \(Q_3\) is **homeomorphic** to \(\#3\overline{\mathbb{CP}}^2\). A diffeomorphism needs one more argument: \(B_2\) carries
the circle action \([x:y:z]\mapsto[s^2x:sy:z]\) preserving \(xz=y^2\), the \(A_3\) resolution is toric, and if the actions match along the link
the Fintushel–Pao classification of smooth circle actions on simply connected 4-manifolds (with Perelman) gives \(Q_3\cong\#3\overline{\mathbb{CP}}^2\);
alternatively a Kirby-calculus check. Until then the \(A_3\) statements below are stated for \(X\#Q_3\) (homeomorphic to
\(X\#3\overline{\mathbb{CP}}^2\)); the \(EH\)-pair statements are unconditional.

Hence, for every closed oriented \(X\) and \(m\ge1\):
\[
X\#2m\overline{\mathbb{CP}}^2\ \cong\ \text{resolution of }X\#m(S^4/\mathbb Z_2)\ \text{by }2m\text{ Eguchi–Hanson spaces},\qquad
X\#Q_3\ \cong\ \text{resolution of }X\#\Sigma_4\ \text{by one }A_3\text{ space}.
\]
Characteristic check (JSON §3): \(\chi_{\rm orb}(X\#S^4/\mathbb Z_2)=\chi(X)-1\), \(\tau_{\rm orb}=\tau(X)\); \(\chi_{\rm orb}(\Sigma_4)=5/4\),
\(\tau_{\rm orb}(\Sigma_4)=-1/2\), \(\eta_{\mathbb Z_4}=1/2\); the resolutions have \((\chi,\tau)=(\chi_X+k,\tau_X-k)\), and
\((2\chi+3\tau)_{\rm orb}=c_1^2(X)-k\) is preserved (Ricci-flat bubbles have zero contribution).

### Corollary 52.8 (upper bounds through orbifolds and symmetric connected sums)
For orbifold metrics (smooth in orbifold charts), gluing scaled Ricci-flat ALE spaces costs \(O(\epsilon^2)\) (orbifold metric \(\delta+O(\rho^2)\),
ALE \(\delta+O(\epsilon^4\rho^{-4})\), interpolation at \(\rho\sim\epsilon^{1/2}\) with \(|\mathrm{Ric}^\circ|=O(1)\) on volume \(O(\epsilon^2)\)). Hence
\[
\alpha(X\#2m\overline{\mathbb{CP}}^2)\le\alpha_{\rm orb}(X\#m\,S^4/\mathbb Z_2),\qquad \alpha(X\#Q_3)\le\alpha_{\rm orb}(X\#\Sigma_4).
\]
Moreover \(X\#(S^4/\mathbb Z_2)=Z/\iota\) with \(Z=X\#S^4\#X\cong X\#X\) and \(\iota\) the involution exchanging the two copies with two
isolated fixed points (on the middle \(S^4\)); orbifold metrics are \(\iota\)-invariant metrics on \(Z\) and \(P_{\rm orb}=\tfrac12P_Z\), so
\[
\boxed{\ \alpha(X\#2\overline{\mathbb{CP}}^2)\le\tfrac12\,\alpha^{\iota}(X\#X)\ }
\]
(\(\alpha^\iota\) = infimum over \(\iota\)-invariant metrics). Similarly \(X\#m(S^4/\mathbb Z_2)\) is a quotient of \(X\#X\#(m-1)(S^1\times S^3)\).
In particular a \(\iota\)-invariant Einstein metric on \(X\#X\) would give \(\alpha(X\#2\overline{\mathbb{CP}}^2)=0\).

### Corollary 52.9 (correct form of the zero-gap/Einstein-orbifold relation)
(i) Unconditionally: if \(M\) is the resolution, by Ricci-flat ALE (bubble trees allowed), of a compact Einstein orbifold, then \(\alpha(M)=0\).
(ii) Under Theorem 52.3 (and the selection of §2): if \(\alpha(M)=0\) along a noncollapsed \((\mathrm{PS}_\varepsilon)\) sequence, \(M\) is such a
resolution (Ricci-flat ALE are single-ended by Cheeger–Gromoll, nontrivial only for \(\Gamma\neq1\)).
(iii) The exceptional classes of \(M=X\#k\overline{\mathbb{CP}}^2\) need **not** lie in the orbifold bulk: they can be absorbed by
\(EH\)-pairs or \(A_3\) bubbles (52.6–52.7). Thus "every exceptional class lies in the bulk" is false as a consequence of (ii).
(iv) Orbifold LeBrun estimate. If the bulk \(Y\) is Einstein with nonzero orbifold Seiberg–Witten invariant for the class \(c_Y\) obtained by
projecting a basic class, then \((2\chi+3\tau)_{\rm orb}(Y)\ge\tfrac23(c_Y^+)^2\ge\tfrac23A\) (sign choice as in LeBrun; absorbed classes project
to zero, unabsorbed ones can be aligned). Since \((2\chi+3\tau)_{\rm orb}(Y)=A-k\), this gives \(k\le A/3\) in every absorption pattern —
exactly LeBrun's threshold, nothing in \(0<k<A/3\).
(v) No complex realization (parity proof, replacing a withdrawn basic-class count): in the crepant resolution \(Z\) of a complex orbifold with
\(SU(2)\) points, \(K_Z\cdot r=0\) for every exceptional root, so \(K_Z\cdot E=0\) for \(E\in R\otimes\mathbb Q\); but \(K_Z\) is characteristic,
\(K_Z\cdot E\equiv E^2\pmod 2\), impossible for \(E^2=-1\). Hence not even one exceptional class can be absorbed in a complex crepant
resolution; any absorbing Einstein orbifold is non-Kähler (for a complex structure compatible with the \(SU(2)\) points).

**Global judgment.** Positivity of \(\alpha(X\#k\overline{\mathbb{CP}}^2)\) in \(0<k<A/3\) contains: nonexistence of Einstein metrics on
\(X\#k\overline{\mathbb{CP}}^2\) (LeBrun's open range), nonexistence of Einstein orbifolds on \(X\#m(S^4/\mathbb Z_2)\) and \(X\#\Sigma_4\)-type
spaces, equivalently of \(\iota\)-invariant Einstein metrics on \(X\#X\)-type manifolds; in all these the exceptional lattice is invisible to
Seiberg–Witten theory of the bulk. Conversely, constructing such an invariant Einstein (or near-critical) metric gives an upper bound. The
problem of the open range is therefore at least as hard as Einstein existence on these symmetric connected sums; a per-class tariff argument
based on exceptional lattice data cannot exist without addressing absorption.

### Proposition 52.10 (conservation of the standard-germ ledger)
Theorem-G charges (normalized, flat/round germs; JSON §4): Burns 1; EH 0; \(A_3\) 0; the \(S^4/\mathbb Z_2\) orbifold cell (one \(S^3\) out-link,
two \(\mathbb Z_2\) in-links, \(\chi=-1,\tau=0\)) 2; the \(\Sigma_4\) cell (\(\chi=0,\tau=0\), one \(\mathbb Z_4\) in-link) 3; the smooth
\(D\#k\overline{\mathbb{CP}}^2\) cell \(k\). Absorption relocates the charge from bubbles to the orbifold cell; the total is the topological
\(k\). Savings below one per class therefore must come, as for the certified cell, from nonstandard (complex-hyperbolic) germs and the
interaction of the cell with the ambient curvature, not from the bubble topology.

**New construction targets.** (1) CH-collared \(S^4/\mathbb Z_2\)-orbifold cells and \(\iota\)-invariant necks in \(X\#X\): their cost per absorbed
class is the competitor to the certified Burns cell \(0.995662\ldots\) per class; (2) \(\Sigma_4\)-cells (one \(\mathbb Z_4\) point) for three
classes. A cell cheaper than \(2\times0.995662\) (resp. \(3\times\)) would improve the best known coefficient; a proof that they cost at least as
much would be evidence that absorption is not the saving mechanism.

---

## 4. What remains open in the entry programme

1. Lemma 52.KS (own-scale concentration lemma for the weighted \(P\)-flow), Sobolev persistence along the flow.
2. The integral-curvature harmonic-radius theorem used in 52.4 (literature citation to be fixed).
3. No-neck theorem (energy identity) for \((\mathrm{PS}_\varepsilon)\) sequences.
4. Collapsed branch: ALF/GH clusters, Hopf/Berger collapse, the O10 endpoint, priced only by Theorem G and the value-four decollapse.
5. Value theory of the exact critical bulk: in the open range, the bulk may be a non-Kähler \(B^{1/6}\)-flat metric on \(M\) itself or an
   absorbing orbifold; neither is excluded or constructed.


---

## 5. Verification corrections (authoritative over §§1–3 where they differ)

Sources: `trace/ttcs/results/step52_ttcs01_sub3_verifier.md`, `step52_ttcs01_sub4_verifier.md` (verifier task 1; integration failed, both
branches read), `step52_ttcs01_verifier2_integration.md`, `step52_ttcs01_generator1_integration.md`.

**5.1 Exact structure.** With the full tensor norm, \(|\mathrm{Rm}|^2d\mu=32\pi^2\mathrm{Pf}+4|\mathrm{Ric}^\circ|^2d\mu\) pointwise, so
\[
\int_M|\mathrm{Rm}|^2=32\pi^2\chi(M)+4P(g).
\]
Hence Streets' functional \(\tfrac12\int|\mathrm{Rm}|^2=16\pi^2\chi+2P\): **the \(P\)-flow in dimension four is Streets' \(L^2\)-curvature flow** (time
rescaled by 2), and \(\partial_t\mathrm{Rm}=-\tfrac12\Delta^2\mathrm{Rm}+P^2_2+P^0_3\) — the full curvature, Weyl included, is parabolically smoothed.
The remark in §2.2 that "the Weyl part is not dissipated" is withdrawn. Explicitly
\(Q=-\Delta\mathrm{Ric}+\tfrac12\nabla^2s-2R_{ikjl}R^{kl}+\tfrac12s\mathrm{Ric}+\tfrac12|\mathrm{Ric}|^2g-\tfrac18s^2g\), \(\operatorname{tr}Q=-\tfrac12\Delta s\)
(\(a=\tfrac12\), \(b=0\), \(c_0=-\tfrac12\)); the zero-order part contains \(W*\mathrm{Ric}^\circ\), so the full curvature must be in \(L^6\).

**5.2 Prop. 52.1** is correct with constants depending on the \(C^{1,\beta}\) harmonic-coordinate bounds, \(\Lambda\) and \(\sup\|Q\|_2\); the
fourth-order term converges only weakly in \(L^2\) (coefficients and lower-order products strongly), which suffices for \(Q(g_\infty)=0\); smoothness
of the limit follows from the triangular bootstrap without GV.

**5.3 Prop. 52.2 realized geometrically.** On a flat patch, \(\varphi_\sigma=\tfrac\lambda6\eta(\Gamma*u_\sigma)\), \(g_\sigma=e^{2\varphi_\sigma}\delta\):
\(\|\varphi_\sigma\|_{W^{4,2}}\to0\), \(\|Q(g_\sigma)\|_2\to0\), \(\int|\mathrm{Rm}|^2\to0\) (so \(r_\varepsilon=r_0\) and \((\mathrm{PS}_\varepsilon)\) holds),
uniform \(L^6\) curvature, but \(s_{g_\sigma}(0)\to\tfrac\lambda2\log2\). Inserted near any fixed metric this gives \((\mathrm{PS}_\varepsilon)\) minimizing
sequences without pointwise curvature convergence: the \(C^{1,\beta}\cap W^{2,q}\) convergence class of Theorem 52.3 is **optimal**. An own-scale
\(L^{2+\eta}\) residual gives \(L^\infty\) control.

**5.4 Prop. 52.4.** The harmonic-radius input must be for \(L^q\) curvature with \(q>4=n\) (gives \(W^{2,q}\subset C^{1,1-4/q}\)); \(q=6\) is what the
point-picking supplies; the "\(p=3>n/2\)" condition was wrong. Lemma (to be written; Anderson blow-up): if
\(\rho^{2q-4}\int_{B(z,\rho)}|\mathrm{Rm}|^q\le\Lambda\) on all sub-balls and scale-invariant Sobolev holds, the \(W^{2,q}\) harmonic radius is
\(\ge c(q,\Lambda,C_S)r\). The residual condition is subcritical: any finite \(\eta_0\) works, \(C=C(C_S,\eta_0)\); only \(\varepsilon_0\) must be small.
Sobolev gives \(\operatorname{vol}B(y,R)\ge cR^4\) (lower bound only).

**5.5 Theorem 52.3** holds modulo three unwritten standard ingredients: (a) at bubble scales the residual is controlled on compact subsets of the regular
part only, exact criticality extends across deeper points by the Tian–Viaclovsky removable-singularity theorem (orbifold points); (b) a modulus form of
small-energy regularity on neck annuli (energy and residual \(\to0\) \(\Rightarrow\) \(C^{1,\beta}\)-close to flat cones), needed to identify links
\(S^3/\Gamma\); (c) the Theorem-G ledger on the smooth limits. Without concentration \(\mathrm{Ric}^\circ\to\mathrm{Ric}^\circ_\infty\) strongly in \(L^2\),
so \(P(g_\infty)=\alpha\) exactly.

**5.6 Selection, corrected.** Lemma 52.KS at a fixed threshold is false: a localized packet with energy \(\varepsilon(1+\zeta)\) loses \(\zeta\varepsilon\) in
own-time \(O(\zeta)\) and \(r_\varepsilon\) jumps from the packet scale to \(r_0\) (plateau mechanism; likewise downward). Correct forms:
- (KS′) shifted thresholds: \(c\,r_\varepsilon(g(t_n))\le r_{2\varepsilon}(g(t))\), \(r_{\varepsilon/2}(g(t))\le C\,r_\varepsilon(g(t_n))\); Theorem 52.5's deduction
  only needs the second, and outputs \((\mathrm{PS}_{\varepsilon/2})\), acceptable in 52.3.
- Localized energy identity (double-dual/Lovelock cancellation, no derivatives of \(w\)):
  \(\frac d{dt}\int\phi|\mathrm{Rm}|^2=-4\int\phi w|Q|^2-4\int w\langle C_\phi-\mathcal R_{ikjl}\nabla^k\nabla^l\phi,Q\rangle\), \(|C_\phi|\lesssim|\nabla\phi||\nabla E|+|\nabla^2\phi||E|\);
  with the multiplier \(E+\tfrac s2g\) and Sobolev absorption (\(\varepsilon_0\lesssim C_S^{-2}\)) this gives the transport estimate
  \(\big|\int\gamma|\mathrm{Rm}|^2\big|_{t_n}^{t}\big|\le4D+C\sqrt{D(D+c_1\varepsilon)}\), \(D=\int_{t_n}^t\int w|Q|^2\): **when dissipation is small, local energies
  are nearly frozen**, so (KS′) holds given \(C^1\) control of \(g(t)\) relative to \(g(t_n)\) on own-scale balls.
- Output-compatible time: with \(A(t)=\max\{1,\sup r_\varepsilon^4/w\}\), \(\Theta=\int A^{-1}dt\), one has
  \(\inf_t\int r_\varepsilon^4|Q|^2\le(P(g_0)-\alpha)/\Theta\); the threshold-averaged radius \(\mathfrak r_\varepsilon^4=\varepsilon^{-1}\int_\varepsilon^{2\varepsilon}r_a^4da\)
  is 1-Lipschitz and avoids threshold jumps.
- For minimizing sequences each step has dissipation \(\le\delta_i\to0\), so **two steps suffice**; the infinite run is unnecessary. Steps from data that
  are smooth at own scale (rescaled bounded geometry) are standard local quasilinear parabolic theory (plausible, unwritten).

**The whole open content of the entrance is now "step 0":** from arbitrary near-minimizers with energy and Sobolev bounds, reach at \(P\)-cost \(o(1)\) a
metric smooth at own scale with universal constants. From critical data (small energy + Sobolev) the smoothing gives \(|\partial_tg|\lesssim t^{-1}\) in
own-scale units: a logarithmically divergent metric drift — the same \(W^{2,2}\not\subset L^\infty\) borderline as 5.3 — which is exactly Streets'
Remarks 1.12 (curvature-scale noncollapsing) and 1.14 (localizing Theorem 1.3). From own-scale \(L^6\) data the drift is integrable
(\(C^0\) drift \(O(t^{1/3})\), \(C^1\) drift \(O(t^{1/12})\)). A flow-free alternative is weighted Ekeland/proximal selection with tangent norm
\(\int\mathfrak r_\varepsilon^{-4}|h|^2\), whose dual slope is \(\int\mathfrak r_\varepsilon^4|Q|^2\); it needs a complete lower-semicontinuous relaxation with
nondegenerate \(W^{4,2}\) representatives at finite-slope points.

**5.7 Absorption, corrected.** Lemma 52.6 and Theorem 52.7(a) verified (\(\chi=4,\tau=-2\), \(\pi_1=1\), toric lift, Orlik–Raymond,
\(E_1\pm E_2\)); 52.7(b) gives \(Q_3\) homeomorphic to \(\#3\overline{\mathbb{CP}}^2\), diffeomorphism needs an explicit Kirby reduction or matched circle
actions (existence of actions on both pieces is insufficient). JSON bookkeeping correct. Corollary 52.8 verified for \(m=1\):
\(\alpha(X\#2\overline{\mathbb{CP}}^2)\le\alpha_{\rm orb}(X\#S^4/\mathbb Z_2)=\tfrac12\alpha^\iota(X\#X)\); the \(m>1\) double-cover topology needs an
equivariant connected-sum argument. **Prop. 52.10 should be stated for the signed pair \((C_+,C_-)\)**, which is conserved linearly:
\((2,2)+2(0,-6)=(2,-10)\), \((3,0)+(0,-15)=(3,-15)\); internal links cancel before, not after, taking \(\max\{0,C_\pm\}\). Corollary 52.9(iv) needs an
explicit orbifold SW package (Spin\(^c\) descent at the \(SU(2)\) points, chamber, nonvanishing for every sign choice of unabsorbed classes, so that the
sign average gives \((c^+)^2\ge A\)); until a theorem is cited it is conditional. The topology (overlattices, Kummer-type nonprimitive embeddings,
\(S^4/\mathbb Z_2\) as suspension of \(\mathbb{RP}^3\), rational blow-up with \(B_2\)) is classical; the new content is its use for the gap functional: the
inequality \(\alpha(X\#2\overline{\mathbb{CP}}^2)\le\tfrac12\alpha^\iota(X\#X)\), relocation of exceptional topology out of the rational bulk at zero
\(P\)-cost, and the signed-ledger identities. Global judgment, sharpened: a positive gap in \(0<k<A/3\) must exclude not only exact Einstein metrics on
\(X\#k\overline{\mathbb{CP}}^2\) and absorbing Einstein orbifolds but also nonattaining near-Einstein sequences on them; any surviving tariff must use data
beyond the rational intersection lattice (boundary germs, discriminant/linking forms, local Spin\(^c\) data, monopole flux, ambient curvature).
