# Step 34 — Verified characteristic–constraint link calculus and the first HJ probe of non-round opening

Conventions are those of Steps 27–33: the curvature sign makes round spheres positively curved; on a collar in Gaussian gauge
\[
g=dt^2+h_t,
\qquad K=\tfrac12\partial_t h_t,
\qquad \Theta=\operatorname{tr}_{h_t}K,
\]
and \(\widehat P=P/(8\pi^2)\). The four-dimensional orientation is the blow-up orientation unless explicitly reversed.

## 1. Independent verification and corrections to Theorem G

The two independent readings in
`trace/ttcs/results/step34_ttcs01_verifier1_integration.md` confirmed the normalization
\[
\widehat P(\Omega)=\frac1{2\pi^2}\int_\Omega|W^\pm|^2
 +\frac1{96\pi^2}\int_\Omega s^2
 -(2\chi\pm3\tau)(\Omega)+\mathcal Q_\pm(\partial\Omega),
\qquad
\mathcal Q_\pm=2\mathcal E\mp3\mathcal H,
\tag{G}
\]
where
\[
\chi=\int e+\mathcal E,
\qquad
\int L=\tau+\mathcal H.
\]
For a product-topology annulus the inner link has the reversed boundary orientation, so
\[
\widehat P(C)\ge \mathcal Q_\pm(\Sigma_{\rm out})-\mathcal Q_\pm(\Sigma_{\rm in}).
\]
If the region between the links carries topology, the term \(-(2\chi\pm3\tau)(C)\) remains. A charge jump is therefore a lower payment; it is the complete energy only when the chosen Weyl and scalar remainders vanish.

The following model signs were confirmed.

* A thin radius-\(r\) disk bundle around a fixed smooth embedded \(\Sigma\) of normal Euler number \(n\) has
  \[
  \chi(D(n))=\chi(\Sigma),\quad \tau(D(n))=\operatorname{sgn}n,
  \quad
  \mathcal Q_\pm\to2\chi(\Sigma)\pm3\operatorname{sgn}n.
  \]
  Hence a \((-1)\)-sphere has \((\mathcal Q_+,\mathcal Q_-)=(1,7)\). Along a degenerating metric sequence the tube must be taken below the curvature scale for this fixed-smooth-germ limit to apply.

* At a flat-conical/ALE end \(S^3/\Gamma\), with the outgoing-link orientation and APS convention above,
  \[
  \mathcal Q_\pm\to\frac2{|\Gamma|}\mp3\eta_\Gamma.
  \]
  Thus a smooth complete scalar-flat ALE bubble satisfies
  \[
  \widehat P\ge\frac2{|\Gamma|}-2\chi+3|\tau+\eta_\Gamma|,
  \]
  exactly Lemma Q. The intrinsic round quotient alone does not determine the charge if its radial first jet is arbitrary; actual orbifold singularities also require orbifold characteristic corrections.

* For Taub–NUT in the blow-up orientation, \(W^-=0\), \(\operatorname{Ric}=0\), \(\chi=1\), \(\tau=0\). At its ALF links, the Euler transgression is \(O(R^{-2})\): the alternating index structure pairs the small fibre principal curvature with the complementary base curvature, or multiplies all three principal curvatures. Hence \(\mathcal E\to0\), \(\mathcal H\to2/3\), and
  \[
  (\mathcal Q_+,\mathcal Q_-)\to(-2,2).
  \]
  Reversing four-dimensional orientation exchanges the charges, yielding \((2,-2)\). The relation between \(\mathcal H\) and \(\mathcal E\) used here is a property of the Ricci-flat half-conformally-flat filling, not of an arbitrary half-conformally-flat filling. Unbounded radial collar shear also changes the limiting charge.

For
\[
D\cong(\#^{k_D}\overline{\mathbb{CP}}^{\,2}\#^{\ell_D}(S^1\times S^3))\setminus B^4,
\]
the verified bound remains
\[
\widehat P(D)\ge k_D+4\ell_D-(2-\mathcal Q_+(\partial D)).
\tag{G1}
\]
Its Betti-number form for an \(S^3\) boundary is
\[
\widehat P(D)\ge b_2^-+4b_1-5b_2^+-(2-\mathcal Q_+(\partial D)).
\]
The finite disjoint-region addition is valid. The old broader reading of G3 was corrected: when \(k=1\) and \(\widehat P<1-\varepsilon\), every standard negative-definite blow-up region obeys
\[
\mathcal Q_+(\partial D)\le1+\widehat P(D)\le1+\widehat P(g)<2-\varepsilon.
\tag{G3}
\]
Thus the exceptional subtree cannot be separated from the bulk by an outer \(S^3\) collar converging in \(C^2\) to the Euclidean flat-conical germ. This remains true even if there are deeper inner bubbles. It does not exclude \(S^3/\Gamma\) necks, Taub–NUT-chirality collapse, curved or sheared links under the charge threshold, bulk bubbling, or regions carrying positive intersection form. For multiple classes, addition requires pairwise disjoint regions (or one region enclosing all classes), so the numerical count applies only to the classes contained in such a disjoint family.

The detailed corrections were inserted into `notes/step33_link_charges_global_decomposition_static_channel.md` and should supersede its original G3 title and broad degeneration sentence.

## 2. The symmetry-free characteristic–constraint link calculus

The hypersurface equations give the second half of the link theory. The traced Gauss equation implies
\[
R_{h_t}=s-2\operatorname{Ric}(\nu,\nu)+\Theta^2-|K|^2.
\]
Define
\[
\mathcal C:=\operatorname{Ric}^\circ(\nu,\nu)
 =\frac12(\Theta^2-|K|^2-R_h)+\frac{s}{4},
\tag{2.1}
\]
so for \(s=-24\), \(\mathcal C=\frac12(\Theta^2-|K|^2-R_h)-6\). Contracted Codazzi gives the momentum residual
\[
\mathcal J:=\operatorname{Ric}^\circ(\nu,\cdot)
 =\operatorname{div}_{h_t}K-d\Theta.
\tag{2.2}
\]
The tangential trace-free evolution residual is
\[
\mathcal S:=\left(\operatorname{Ric}^\circ|_{T\Sigma_t}\right)^{\circ_h}
 =\left(\operatorname{Ric}^{h_t}-\partial_tK-\Theta K+2K^2\right)^{\circ_h}.
\tag{2.3}
\]
Orthogonality gives the exact pointwise identity
\[
|\operatorname{Ric}^\circ|^2
 =\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2.
\tag{2.4}
\]
Thus \(P\) controls the squared Hamiltonian, momentum, and tangential evolution residuals, but it does not separately control \(R_h\), \(K\), \(\Theta\), injectivity radius, lapse, focal radius, or any boundary transgression.

Every exact transport identity
\[
\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\mathcal F
=\int_C\bigl(f\mathcal C+\langle X,\mathcal J\rangle+\langle T,\mathcal S\rangle\bigr)d\mu
\tag{2.5}
\]
has the dual consequence
\[
\widehat P(C)\ge
\frac{|\mathcal A_b-\mathcal A_a-\mathcal F|^2}
{8\pi^2\int_C(\frac34f^2+\frac12|X|^2+|T|^2)d\mu}.
\tag{2.6}
\]
The reference drift \(\mathcal F\) is indispensable: an Einstein metric can have nontrivial hypersurface evolution at zero defect.

In diagonal Bianchi IX, \(\mathcal J=0\), and
\[
\mathcal C=\sigma_2(y)-6-\frac12R^{(3)},
\qquad
\widehat P=\int W\left(\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}\right)dt.
\]
This is Lemma N. The CR observable satisfies \(\widetilde\Phi'=F_\Phi-D/4\), and the fibre/base observable satisfies \(\widetilde B'=F_\beta-E/4\); these are projections of \(\mathcal S\), not of the Codazzi momentum residual. The exact Green identity for \((Wq')'=W(P_g-P_h-D)\) is another weighted transport form of the same \(D\)-channel.

The unified statement is therefore:

* the characteristic channel (G) prices topology and boundary-germ changes through Euler, APS, and collar transgressions;
* the constraint/kinematic channel (2.1)–(2.6) prices drift-corrected changes of intrinsic link geometry and second fundamental form through \(\mathcal C,\mathcal J,\mathcal S\);
* their lower bounds are generally combined by a maximum, not added, unless the regions or defect components have been separated;
* link regularity is convergence/control of precisely the link germ \((h,K)\), its characteristic and spectral transgressions, and any field boundary data needed on the bulk side.

This is a theorem-level accounting principle, not a compactness result. Critical \(L^2\) control of \(\operatorname{Ric}^\circ\) alone does not supply controlled links, convergence of transgressions, Dai small-eigenvalue terms, or localized Seiberg–Witten fluxes.

## 3. Exact HJ reduction and why \(\mathfrak b_++\phi(q,\eta)\) does not strengthen N

For the exact scale-free controlled system
\[
X=(x,z,p,\chi,\eta),\quad q=-3\log z,
\]
\[
\begin{aligned}
x'&=\chi,&q'&=\eta,\\
p'&=A_p-\bar H/2,&
\chi'&=A_\chi-\bar E+\bar D/2,&
\eta'&=A_\eta-\bar D,
\end{aligned}
\]
with
\[
L=\frac{3\bar H^2}{16}+\frac{\bar E^2}{6}+\frac{\bar D^2}{8},
\]
let \(b=\mathfrak b_+\) and \(V=b+\phi(q,\eta)\). Maximizing \(\dot V-L\) over the three controls yields
\[
\bar H_*=-\frac43b_p,
\qquad
\bar E_*=-3b_\chi,
\qquad
\bar D_*=2b_\chi-4(b_\eta+\phi_\eta).
\]
A direct exact SymPy reduction (`scripts/hj_symbolic_reduction.py`, `data/saturation_control/hj_symbolic_reduction.json`) proves
\[
\sup_{\bar H,\bar E,\bar D}(\dot b-L)\equiv0.
\tag{3.1}
\]
This is the Hamilton–Jacobi form of the chiral identity: the charge itself is an exact calibration, not a strict subsolution with unused pointwise slack. Put
\[
K=A_\eta-2b_\chi+4b_\eta.
\]
Then \(V=b+\phi(q,\eta)\) is a global subsolution only if
\[
\boxed{\eta\phi_q+K\phi_\eta+2\phi_\eta^2\le0}
\tag{3.2}
\]
pointwise on the domain. The exact, nonzero formula for \(K\) is stored in the same JSON file.

Equation (3.2) exposes the obstruction. At a fixed \((q,\eta)\), the hidden variables \((x,p,\chi)\) vary \(K\). A common \(\phi\) must work for the whole hidden-state fibre. Any \(q\)-only potential satisfies \(\eta\phi_q\le0\). On the swap band \(\eta<0\), increasing the endpoint lower bound requires the opposite sign of \(\phi_q\), so no \(q\)-only function improves the charge bound. Allowing \(\phi_\eta\) can exploit the linear \(K\)-term only if the hidden-state fibres give coherent sign and magnitude for \(K\); the nonnegative \(2\phi_\eta^2\) prevents a universal gain where \(K\) changes sign or approaches zero.

`scripts/hj_qeta_probe.py` evaluated the exact reduction on the cap-\(-1\) optimizer trajectories for \(\varepsilon=1/16,1/32,1/64\), writing `data/saturation_control/hj_qeta_probe.json`. This is a finite-sample route probe, not a proof over state space. It found:

* \(\sup(\dot b-L)\) is zero to floating error (sampled \(m=-\sup(\dot b-L)\) in \([-2.9\times10^{-11},3.0\times10^{-12}]\));
* \(K\) ranges from about \(-3.34\) to \(4.46\) along the three paths and changes sign through the swap;
* a convex search for \(\phi=-aq+bq^2+cq\eta+d\eta^2\) on the sampled descending swap segments returns zero maximal \(\phi\)-gain (\(-1.7\times10^{-10}\) numerically), with coefficients essentially zero.

So the bounded-effort \(\phi(q,\eta)\) route is exhausted more strongly than anticipated: the exact charge calibration has no pointwise margin to redistribute, and the sampled hidden-state dynamics makes the \(K\)-lever sign-incoherent. A nontrivial subsolution must use at least one additional geometric/jet variable, split the domain into regions with boundary matching, or use a different exact structure rather than merely decorating \(\mathfrak b_+\) by \((q,\eta)\).

## 4. The canonical almost-Kähler identity is the stronger next structure

Peer S1003A01 supplied an exact identity for every smooth diagonal exact-CH perpendicular \(O(-1)\) cell; see `Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md`. The metric is canonically conformal to a diagonal almost-Kähler metric \(\hat g=u^2g\), and with its Nijenhuis scalar \(\nu\), \(W_3^+\) eigenvalue \(\lambda\), and the nonnegative quantities \(H,G,Q_\delta,Q_A,N\) defined there,
\[
\boxed{
\widehat P-1
=12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N+\Sigma.
}
\tag{4.1}
\]
For \(s=-24\), \(\Sigma=0\). The only negative term is the Nijenhuis energy. The exact transport
\[
\lambda=\frac12\nu_T+\beta\nu,
\qquad
(\mu\nu)_T=2\mu\lambda,
\tag{4.2}
\]
forces the perpendicular bolt's Nijenhuis charge to unwind before the CH collar. A Hardy estimate makes
\[
2\int\lambda^2d\hat V-6\int\nu^2d\hat V\ge0
\]
on every tail where \(\Lambda\ge4\sqrt3\); on CH this begins at \(\sinh^2R=3+3\sqrt{15}/4\). Hence every possible subunit saving is generated in a compact near zone. The numerical \(x_0=.038,X=128\) identity is satisfied to \(2.1\times10^{-10}\):
\[
\widehat P-1=-0.0047126289,
\]
with contributions
\[
12H=0.0033318,
\quad6G=0.0556282,
\quad\tfrac32Q_\delta=0.0011325,
\quad\tfrac12Q_A=0.0328569,
\quad-\tfrac32N=-0.0976572,
\]
and \(\Sigma=-4.75\times10^{-6}\).

An independent Step-34 verification (`trace/ttcs/results/step34_ttcs02_verifier1_integration.md`) checked every coefficient and exposed the correct near-zone object. Two scope points matter. The canonical almost-Kähler metric is singular at the perpendicular bolt, although all displayed energies are integrable; Stokes arguments must be made on a truncated cell and passed to the bolt using the smooth original-metric expansions. Also the header of `step28_ak_nu_structure.py` says \(A_gA_h=2\phi\), but the formulas and the correct normalization have \(A_gA_h=\phi\).

Put \(v=u^{-1}\), \(\rho=(\log v)_T\), \(w=A_fA_gA_h\), and \(m_0=(\log w)_T\). The exact scalar/conformal coupling is
\[
\delta=\rho_T+\rho^2+m_0\rho+\nu^2+4(1-v^2),
\]
while \(2\lambda=\nu_T+2\beta\nu\). Thus at \(s=-24\)
\[
\widehat P-1=\int w\left[6\rho^2-6\nu^2+\frac12(\nu_T+2\beta\nu)^2+\frac32\delta^2+12(v^2-1)^2\right]dT.
\tag{4.3}
\]
Equivalently, with \(z=\mu\nu\) and \(m=w/\mu^2\), the indefinite sector is
\[
\int m\left(\frac12z_T^2-6z^2\right)dT,
\]
a compact weighted Sturm–Liouville problem with forced bolt charge and zero terminal charge. The far Hardy estimate is an endpoint interval statement: it uses \(\nu=0\) at the exact collar and cannot be applied to a disconnected set merely because \(\Lambda\ge4\sqrt3\) there.

This identity is stronger than \(b_++\phi(q,\eta)\), but it does not support a universal \(\widehat P\ge1\): the certified subthreshold cells are precisely negative middle-zone modes. In the \(x_0=.038\) record the near zone contributes approximately \(-0.01059\), while the far tail returns only \(+0.00588\), leaving the observed deficit \(-0.00471\). The plausible theorem is therefore a sharp subunit lower value and classification of the coupled weighted mode, or a conditional unit bound under an additional coercive middle-zone hypothesis—not a contradiction of the already certified subunit metrics. The next construction task for N is to determine the lowest coupled compact action (4.3), with the smooth-bolt and exact-CH boundary data, and compare it with the required branch threshold. If one focused attempt does not produce a rigorous estimate, N should remain a named numerical-margin input while work moves to the large-bolt and face theorems.

## 5. Consequences for the global programme

The characteristic–constraint calculus now supplies the requested common mechanism beyond symmetry:

1. Theorem G, Lemma Q, Theorem F, and Q″ are relative characteristic calibrations. They price topology only after the whole boundary germ—including radial collar data—is controlled.
2. Gauss–Codazzi splitting and transport identities price the shape and first-jet changes that charges cannot see. Lemma Z and (3.1) show why this second channel is mathematically independent rather than a technical refinement.
3. The global monopole estimate is blow-up blind through \(\beta^2(X\#k\overline{\mathbb{CP}}^2)=c_1^2(X)\). It should pin the regular bulk's global scalar/Weyl budget, while Theorem G and Theorem C price the cells on the same metric. A localized boundary-value monopole theory is not the first missing ingredient.
4. For a ball-quotient one-blow-up sequence below one unit, G3 excludes Euclidean-round separation of the exceptional ALE subtree. The remaining possibilities include collapse, curved/sheared links, orbifold necks, and bulk behaviour; these are exactly where controlled link germs and the constraint channel are needed. This is sharper than saying that all bubble trees are excluded.

The corrected link-charge note and this calculus should be used together. The central unresolved issue remains deriving controlled link germs and sufficient near-zone kinematic coercivity from near-minimality, not another static topological charge.