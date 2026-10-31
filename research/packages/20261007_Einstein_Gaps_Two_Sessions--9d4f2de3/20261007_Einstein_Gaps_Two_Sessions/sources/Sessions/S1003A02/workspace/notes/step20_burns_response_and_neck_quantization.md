# Step 20 — Burns first-order response theorem, neck quantization, and exact-cell rigidity

Session S1003A02, Agent2. Conventions: curvature operator \(\mathcal R:\Lambda^2\to\Lambda^2\) with
\(\langle\mathcal R(e_1\wedge e_2),e_1\wedge e_2\rangle=\sec(e_1,e_2)\); \(\mathbf R^+=P_+\mathcal RP_+=W^++\frac s{12}I\)
on \(\Lambda^+\); norms are endomorphism norms (so \(|W^+|^2=24\), \(s^2/24=24\) on \(\mathbb{CH}^2\) with \(s=-24\));
\(8\pi^2\chi=\int(|W|^2-\tfrac12|\mathrm{Ric}^\circ|^2+\tfrac{s^2}{24})\), \(12\pi^2\tau=\int(|W^+|^2-|W^-|^2)\) on closed manifolds;
\(P=\int|\mathrm{Ric}^\circ|^2\). Script and exact output:
`workspace/scripts/burns_transgression_flux.py`, `workspace/data/burns_transgression_flux.json`.

---

## 1. Theorem F (first-order Burns response; general bulk)

**Burns metric in the session normalization.** On \(\mathbb C^2\setminus0\) with standard \(J\), Kähler form
\(\omega=dx_1\wedge dx_2+dx_3\wedge dx_4\in\Lambda^+\), the Kähler potential \(|z|^2+x_0\log|z|^2\) gives *exactly*
\[
B_{x_0}=\delta+x_0h,\qquad h_{ij}=\frac1{t^2}\Big(\delta_{ij}-\frac{x_ix_j}{t^2}-\frac{(Jx)_i(Jx)_j}{t^2}\Big),
\]
i.e. \(dt^2+(t^2+x_0)(\sigma_1^2+\sigma_2^2)+t^2\sigma_3^2\): the session profile \(a_1=a_2=\sqrt{t^2+x_0},a_3=t\), whose
exceptional curve has area \(\pi x_0\). Since \(B_{x_0}\) is affine in \(x_0\) and \(W^+(B_{x_0})=s(B_{x_0})=0\) for all
\(x_0\), the tail satisfies **pointwise** \(P_+\mathcal R^{\rm lin}(h)P_+=0\) on \(t>0\) (verified exactly).

**Exact transgression (computed).** For any cutoff \(\chi\) (1 near 0, 0 near \(r_0\)), the integral over the cut
annulus \(\Phi^{\pm\pm}=-\int P_\pm\mathcal R^{\rm lin}(\chi h)P_\pm\,dx\) is the inner-sphere flux and is independent of
\(\chi,r_0\). Exact monomial integration on \(S^3\) gives, in the orthonormal bases with \(w_1=\omega/\sqrt2\),
\[
\Phi^{++}=\pi^2\,w_1w_1^{T},\qquad \Phi^{--}=\tfrac{\pi^2}{3}I,\qquad \Phi^{+-}=0 .
\]
The sign convention was checked on the normal-coordinate jet of constant curvature \(K\) (\(R_{1212}=K\),
\(\mathbf R^\pm=KI\)). Hence the scalar flux is \(F_s=-\int s^{\rm lin}(\chi h)=4\operatorname{tr}\Phi^{++}=4\pi^2\).

**Theorem F.** Let \((M,g)\) be a closed oriented Riemannian 4-manifold, \(p\in M\), \(\zeta\in\Lambda^+_p\) a unit
self-dual form, and let \(\hat g_{x_0}\) on \(\hat M=M\#\overline{\mathbb{CP}}^2\) be obtained in \(g\)-normal coordinates at \(p\),
with a frame identifying \(\zeta\) with \(w_1\), by
\(\hat g_{x_0}=\pi^*g+x_0\chi(r/r_0)h\), \(r_0=x_0^{1/5}\). Then
\[
\boxed{\;P(\hat g_{x_0})=P(g)+8\pi^2\big(1-x_0\,\mathbf R^+_p(\zeta,\zeta)\big)+O(x_0^{6/5})\;}
\]
with the constant depending on \(\|g\|_{C^3}\) near \(p\). If \(g\) is Einstein, \(\operatorname{Ric}=\lambda g\), the same holds for
\(J(\hat g)=\int|\operatorname{Ric}-\lambda\hat g|^2\).

**Proof.** (i) *Topological reduction.* \(\chi(\hat M)=\chi(M)+1\), \(\tau(\hat M)=\tau(M)-1\) and the two Chern–Weil
identities give the exact identity \(P(\hat g)-P(g)-8\pi^2=4\Delta W^++\Delta S/12\), where
\(\Delta W^+=\int|W^+|^2\) of \(\hat g\) minus that of \(g\), and \(\Delta S\) likewise for \(\int s^2\); the metrics agree outside
\(B_{r_0}\).

(ii) *Inner region \(r\le r_0/2\)* (two sub-regions; repaired after the Step-20 TTCS verification). Here
\(\hat g=B_{x_0}+k\), \(k=g-\delta=O(r^2)\), \(\partial k=O(r)\), \(\partial^2k=O(1)\).
*Core \(r\le\sqrt{x_0}\):* rescale \(y=x/\sqrt{x_0}\), \(x_0^{-1}\hat g=B_1+K\), \(K=O(x_0|y|^2)\) in \(C^2\); \(B_1\) has bounded
geometry near the exceptional curve, so \(|W^+(\hat g)|+|s(\hat g)|\le C\) in original units, while
\(dV_{\hat g}\le C(r^3+x_0r)\,dr\,d\Omega\) (note \(\sqrt{\det B_{x_0}}=1+x_0/r^2\), so the volume form is *not* within
\(O(1)dx\) of flat there). Core contributions: \(O(\int_0^{\sqrt{x_0}}(r^3+x_0r)dr)=O(x_0^2)\).
*Intermediate \(\sqrt{x_0}\le r\le r_0/2\):* the mixed finite difference
\(F(B_{x_0}+k)-F(\delta+k)-F(B_{x_0})+F(\delta)\), \(F\in\{W^+,s\}\), has vanishing pure terms
(\(F(B_{x_0})=F(\delta)=0\)), and every remaining term carries a Burns-tail factor and a bulk-jet factor, giving
\(|F(\hat g)-F(g)|\le Cx_0/r^2\); the relative volume correction is also \(O(x_0/r^2)\). The energy-density difference is
\(O(x_0/r^2+x_0^2/r^4)dx\), integrating to \(O(x_0r_0^2+x_0^2\log(1/x_0))\). No first-order term arises in the inner
region: the linearized self-dual curvature and scalar curvature of the tail vanish pointwise.

(iii) *Cut annulus \(r_0/2\le r\le r_0\).* Here \(\hat g=g+x_0\chi h\), \(|\partial^j(x_0\chi h)|\le Cx_0r_0^{-2-j}\).
Expanding,
\(|W^+(\hat g)|^2dV_{\hat g}-|W^+(g)|^2dV_g=2\langle W^+(g),x_0P_+\mathcal R^{\rm lin}_\delta(\chi h)P_+\rangle_0dx+E\),
with \(|E|\le C(x_0r_0^{-2}+x_0^2r_0^{-8})\) (curvature-dependent part of the linearization, projector and volume
variation, quadratic terms). Since \(W^+(g)=W^+_p+O(r_0)\) in the normal frame,
\[
\Delta W^+_{\rm cut}=-2x_0\langle W^+_p,\Phi^{++}_0\rangle+O(x_0r_0+x_0r_0^2+x_0^2r_0^{-4}),\quad
\Delta S_{\rm cut}=-2x_0s_pF_s+O(\cdots).
\]
(iv) *Assembly.* \(4\Delta W^++\Delta S/12=-8x_0\langle W^+_p,\Phi_0^{++}\rangle-\tfrac{2}{3}x_0s_p\operatorname{tr}\Phi^{++}
=-8x_0\langle\mathbf R^+_p,\Phi^{++}\rangle=-8\pi^2x_0\mathbf R^+_p(\zeta,\zeta)\), plus errors
\(O(x_0r_0+x_0^2r_0^{-4}+x_0^2\log(1/x_0))=O(x_0^{6/5})\) for \(r_0=x_0^{1/5}\). For Einstein \(g\),
\(J(\hat g)-P(\hat g)=\frac14\int(s_{\hat g}-4\lambda)^2dV_{\hat g}\). The core bound (\(|s|\le C\) on volume \(O(x_0^2)\)), the
intermediate bound \(|s_{\hat g}-4\lambda|\le Cx_0/r^2\) and the annulus bound \(Cx_0r_0^{-4}\) make this
\(O(x_0^2\log(1/x_0)+x_0^2r_0^{-4})=O(x_0^{6/5})\). \(\square\)

The proof was checked independently (`trace/ttcs/results/step20_ttcs01_verifier1_integration.md`). That check
confirmed the flux matrices, the curvature sign, the \(\tfrac14\) two-form pairing and the orientation. It also gave an
independent scalar check: \(n_i(\partial_jh_{ij}-\partial_i\operatorname{tr}h)=2/r^3\), hence \(F_s=4\pi^2\). The two
denominator `assert`s in the script are vacuous (they always test \(0=0\)). The denominators are in fact constants
times powers of \(t^2\), so the output is unaffected.

**Checks.** (a) Kähler topology: the scalar flux says \(\int s\,dV\) drops by \(4\pi^2x_0=4\pi\cdot\mathrm{area}(E)\),
exactly the Kähler identity \(\int s\,dV=4\pi c_1\cdot[\omega]\) with \(c_1(\hat M)\cdot[\hat\omega]=c_1\cdot[\omega]-\mathrm{area}(E)\).
(b) Complex space forms: \(\mathbf R^+=\operatorname{diag}(s/4,0,0)\) in the Kähler frame; for \(\mathbb{CH}^2\) (\(s=-24\))
the aligned slope is \(+6\), the perpendicular slope \(0\), and for Fubini–Study \(-6\): this reproduces the exact Kähler
seed \(1+6\kappa x_0+\dots\) and the numerical slopes \(5.90\), \(0.044\) (near-perpendicular), \(-5.9\) of Steps 8–9.
(c) \(\Phi^{+-}=0\): trace-free Ricci of the bulk does not enter at first order, as \(U(2)\)-representation theory requires
(the only \(U(2)\)-invariant linear functionals of the curvature are \(s\) and \(W^+(\zeta,\zeta)\)).

**Status change.** The Step-8/9 "Burns transgression" conjecture \(\int T_{\mathbf R^+}(H_\zeta)=-\pi^2\zeta\otimes\zeta\)
is now a theorem with its normalization fixed (\(x_0\) = area/\(\pi\) of the exceptional curve), orientation fixed
(\(\zeta\in\Lambda^+\), summand \(\overline{\mathbb{CP}}^2\)), and an explicit \(O(x_0^{6/5})\) remainder. It is an upper-bound
(construction) statement; it says nothing yet about the infimum's first-order coefficient from below.

### Consequences
1. **Strict blow-up saving criterion.** If \(g\) attains \(\inf_MP\) (e.g. \(g\) Einstein) and
   \(\lambda_{\max}(\mathbf R^+_p)>0\) at some \(p\), then \(\inf_{M\#\overline{\mathbb{CP}}^2}P<\inf_MP+8\pi^2\). Since
   \(\operatorname{tr}\mathbf R^+=s/4\), this holds wherever \(s>0\), and for \(s<0\) Einstein metrics wherever an eigenvalue
   of \(W^+\) exceeds \(|s|/12\).
2. **Three bulk regimes for Einstein \(s<0\).** Real hyperbolic: \(\mathbf R^+=\frac s{12}I<0\), every direction costs at
   first order (prediction: blow-up cells over hyperbolic bulk are first-order rigid, cost \(\ge8\pi^2\) to first order, the
   handle-like regime). Kähler–Einstein: eigenvalues \((s/4,0,0)\), a 2-sphere of kernel directions
   \(\omega^\perp=\ker\mathbf R^+\), which are exactly Ozuch's first-obstruction-free directions \(\mathbf R^+\zeta=0\); the
   cost below \(8\pi^2\) then comes from second order (the \(-9x_0^2\log\) neck mechanism, Step 10, and the certified
   cells). Einstein metrics with \(W^+\) eigenvalue \(>|s|/12\): first-order saving.
3. The same tensor \(\mathbf R^+_p\) is the linear obstruction to Einstein desingularization (Ozuch, \(A_1\)) and the
   linear cost of the defect cell. Theorem F is the defect-side half of this correspondence for a general bulk.

---

## 2. Neck quantization of blow-up concentration

**Lemma Q (bubble form).** Let \((N,h)\) be complete, oriented, scalar-flat, ALE with one end \(S^3/\Gamma\)
(order \(>0\), so the Gauss–Bonnet boundary term tends to \(8\pi^2/|\Gamma|\) and the signature boundary term to
\(\eta(S^3/\Gamma)\)). Then
\[
P(N)=2\!\int|W|^2-16\pi^2\Big(\chi(N)-\frac1{|\Gamma|}\Big)\ \ge\ 8\pi^2\Big[3|\tau(N)+\eta|-2\chi(N)+\frac2{|\Gamma|}\Big].
\]
For \(\Gamma=1\): \(N\simeq\) blow-ups/handles of \(\mathbb R^4\) with \(\chi=1+k-2\ell\), \(\tau=-k\) gives
\(P(N)\ge8\pi^2(k+4\ell)=8\pi^2Q\). Equality for one blow-up iff \(W^+=0\) (Burns attains it: \(P=8\pi^2\)).

**Lemma Q′ (neck form, no completeness).** Let \(g\) be any metric on a cell \(U_0\cong D\#\overline{\mathbb{CP}}^2\) and
\(\Sigma\subset U_0\) an embedded 3-sphere bounding an inner region \(U\) with \(\tau(U)=-1\). Suppose a collar of
\(\Sigma\), rescaled by its radius, is orientation-preservingly \(\varepsilon\)-close in \(C^2\) to the Euclidean annulus
\(\{1\le|x|\le2\}\) with \(U\) on the ball side. Here \(\varepsilon\)-closeness is taken in the sense that the Gauss–Bonnet and
signature boundary transgressions are within \(C\varepsilon\) of the flat values; this follows, for example, by
interpolating to an exactly flat annulus inside the collar. Then \(P(g;U)\ge8\pi^2-C\varepsilon\). *Proof.* Mayer–Vietoris gives \(b_1(U)=0\), \(b_2(U)=1\), so
\(\chi(U)\le2\). Gauss–Bonnet and signature with boundary: the boundary terms are within \(C\varepsilon\) of those of a
flat ball (\(8\pi^2\) and \(0\)). Thus \(P(U)=2\int_U|W|^2+\frac1{12}\int_Us^2-16\pi^2\chi(U)+16\pi^2+O(\varepsilon)\ge
24\pi^2-16\pi^2-C\varepsilon\). \(\square\) The scalar term only helps, so no normalization of \(s\) is needed.

**Consequence for \(p_{1,0}\).** By the certified cell (\(x_0=3/100,X=64\)), \(\mathfrak P_{1,0}\le0.99584841\cdot8\pi^2\).
Hence along any sequence with \(P\to\mathfrak P_{1,0}\), for every \(\varepsilon<0.0041\cdot8\pi^2/C\), **no** sphere
enclosing the exceptional class has an \(\varepsilon\)-Euclidean neck. Concentration of the \((-1)\)-class into an
almost-flat bubble is energetically excluded. Handles are the opposite: their bubble bound \(32\pi^2\ell\) equals the
cell infimum, so concentration is allowed, and it is how the handle infimum is approached.

---

## 3. No exact Einstein cells (proportionality rigidity)

**Lemma R.** Let \(U\) be a compact connected cell with exact \(\mathbb{CH}^2\)-collar (\(\operatorname{Ric}=-6g\) there) and
topology change \((\Delta\chi,\Delta\tau)\) relative to the ball with \(\Delta\chi\ne3\Delta\tau\). Then \(U\) carries no
Einstein metric extending the collar; in particular \(P(U)>0\) for every such cell.
*Proof.* An Einstein metric is real-analytic in harmonic coordinates. \(\nabla\mathrm{Rm}=0\) and the \(\mathbb{CH}^2\)
curvature type hold on the collar, hence on all of \(U\). The Gauss–Bonnet and signature densities are then the
\(\mathbb{CH}^2\) constants, \(6/\pi^2\) and \(2/\pi^2\), and the boundary terms coincide with those of the ball.
So \(\Delta\chi=\frac6{\pi^2}\Delta V\) and \(\Delta\tau=\frac2{\pi^2}\Delta V\), i.e. \(\Delta\chi=3\Delta\tau\).
For \(k\) blow-ups and \(\ell\) handles \((\Delta\chi,\Delta\tau)=(k-2\ell,-k)\), and proportionality holds iff \(\ell=2k\). So
every cell with \(\ell\ne2k\) is excluded, in particular all pure blow-up and pure handle cells. \(\square\)
"Exact collar" means equality with the full normalized \(\mathbb{CH}^2\) metric, preserving the complex orientation. The
family \(\ell=2k\) needs a separate rigidity argument for locally complex-hyperbolic fillings of a geodesic sphere
(developing map plus convexity); that argument is not supplied here.

**Consequence (for \(\ell\ne2k\)).** \(\mathfrak P_{k,\ell}=0\) can occur only through degeneration of minimizing sequences:
collar radius \(X\to\infty\) (the limit is a complete ACH-type filling; if Einstein, it is a standard-CR counterpart of
Theorem E), collapse, or concentration through *curved* necks (almost-flat necks are excluded by Lemma Q′).
Positivity of \(p_{1,0}\) is thus reduced to a compactness statement with three named alternatives.

---

## 4. Handles: what is and is not proved about softness

The handle infimum \(32\pi^2\ell\) is approached by shrinking cores and not attained (peer, Step 11). A fixed core
profile at scale \(r\) has \(\int|\nabla\mathrm{Rm}|^2\sim r^{-2}\). The statement "\(R^*(\delta)\to\infty\) for pure-handle
cells" follows **if** bounded \(\int|\nabla\mathrm{Rm}|^2\), \(s=-24\) and a lower injectivity-radius bound imply \(W^{2,4}\)
subconvergence. That follows from Anderson's harmonic-radius theorem for \(\|\mathrm{Rm}\|_{L^p}\), \(p>2\), with
injectivity radius bounded below; Sobolev embedding gives \(L^4\) curvature on harmonic balls. The limit would
attain \(32\pi^2\ell\) in \(W^{2,4}\), contradicting non-attainment provided the equality analysis holds in that
regularity. So: along every handle-minimizing sequence, either \(R_1\to\infty\) or the injectivity radius
\(\to0\). The unconditional version needs a collapse exclusion near the core.

---

## 5. Repairs and open edges
- `ach_bolt_fuchs.py`: Arb-to-binary64 suprema are now rounded outward (`up()`: nextafter plus \(10^{-12}\) relative
  inflation), and the self-map and contraction inequalities are re-verified in Arb with exact rational inverse factors
  (rerun recorded as `fuchs_boxes_N6{,_complex}_v2.json`). Rerun result: complex-disc Lipschitz factor
  0.0325075, real 0.0112241, self-map verified in Arb; the 40 emitted binary64 initial boxes are bit-identical to the
  Step-17 boxes, so the Ważewski transport and the \(\rho_\infty\) enclosure stand unchanged.
- Peer correction (message 771): exact bolt Weyl blocks are diag(−41/16,−41/16,41/8), diag(−91/16,−91/16,91/8);
  non-Kählerness now rests on the Kähler-side spectrum \((-4,2,2)\) being violated (theorem package §6.2).
- Theorem F is an upper-bound theorem. The matching lower statement, that every cell of Burns parameter \(x_0\)
  pays at least \(8\pi^2(1-x_0\lambda_{\max}(\mathbf R^+))+o(x_0)\), needs a cell compactness/stability theory at
  scale \(\sqrt{x_0}\). Lemma Q′ supplies its zeroth-order part under an almost-flat neck.
- Hyperbolic-bulk prediction: \(\mathfrak P^{\mathbb H^4}_{1,0}=8\pi^2\), approached and not attained. This is a
  testable dichotomy against the CH case, and the cleanest place to look for a sharp single-cell lower bound.
