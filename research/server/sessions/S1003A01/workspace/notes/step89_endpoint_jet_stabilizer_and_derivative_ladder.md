# Step 89: the O10 endpoint jet has a stabilizer. No first-order line, L⁵ is forced at second order, and the gap splits into a rank-one and a rank-two problem

Session S1003A01, Agent2, Execute.

Scripts and data:
- `workspace/scripts/step89_jet_stabilizer.py` writes `workspace/data/step89/jet_stabilizer.json`. It uses an explicit Euclidean Clifford model with no convention-dependent input.
- `workspace/scripts/step89_wahl_isotropy.py` writes `workspace/data/step89/wahl_isotropy.json`.

Sources used:
- `O10_All_Finite_Density.md`;
- `O10_Weak_Bianchi.md`;
- `O10_Finite_Density_Complete_Proof.tex`, eqs. (A.9)–(A.25) and (B.2.1)–(B.3.2);
- `O10_LineBundle_Limitation.md`.
All four are in `Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/C/`. The exact Taub–NUT data come from `workspace/notes/step47_o10_tn_core_free_at_energy_scale.md`.

## 0. The question

The finite-density O10 theorem applies its rank-one transgression lemma to
\[
\sigma=\Phi\wedge t(v)\in\Gamma(L^5),
\]
where:
- \(v\) is the bounded resolvent of the cubic torsion \(\tau=t_\Phi=\sum_i c(e^i)\Phi\otimes(\Phi\wedge\nabla_i\Phi)\in E=S^-\otimes L\);
- \(t(v)\) is the cubic torsion of \(v\).

So \(\sigma\) is second order in \(\Phi\), and \(\nabla\sigma\) is third order. Bounding \(\nabla\sigma\) in \(L^2\) uses \(\|\nabla v\|_4+\|\nabla^2v\|_2\le C_B\), and the curvature of \(S^-\) brings in \(W^-\). This is exactly where the Euler-density bound \(B\) enters.

In contrast, the weighted Hessian lemma (A.12) controls \(P=\nabla_A\Phi\) in \(L^4\) and \(H=\nabla_AP\) in \(L^2\) **without any \(W^-\) hypothesis**. The reason is that the curvature of \(S^+\) contains \(W^+\), \(s\), the off-diagonal Ricci block and \(F_A\), but no \(W^-\). Hence a line section built pointwise from \((\Phi,\nabla\Phi)\) would have a density-free \(H^1\) bound. The Step-88 handoff asked for such an order-lowered section, or a proof that none exists. This note proves that none exists among local natural sections. It also identifies why.

## 1. The endpoint first jet is a single orbit with a circle stabilizer

Use the normalization (A.9):
\[
s=-4,\qquad D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi).
\]
The endpoint values (A.15)–(A.16) are
\[
\rho=|\Phi|^2\to\rho_*=\tfrac43,\qquad \zeta_i=\langle\Phi,P_i\rangle\to0,\qquad |P|^2\to\tfrac49,
\]
in normalized \(L^2\).

**Lemma 89.1.** Let \(\mathcal O_*\subset S^+\oplus(T^*\otimes S^+)\) be the set of pointwise jets \((\Phi,P)\) satisfying
\[
|\Phi|^2=\rho_*,\qquad \langle\Phi,P_i\rangle=0,\qquad \textstyle\sum_ic(e^i)P_i=0,\qquad |P|^2=4/9.
\]
Then:
1. \(\mathcal O_*\) is a single \(\mathrm{Spin}^c(4)\)-orbit, of real dimension 6.
2. Its stabilizer is a circle \(U(1)_*\). It acts on \(L=\det S^+\) with nonzero weight, normalized below to weight 2.
3. The torsion is stabilized, and \(|\tau|^2=2\rho_*^2|P|^2=128/81=m_*\).

*Proof.* The condition \(\zeta=0\), interpreted as the complex Hermitian equations \(\langle\Phi,P_i\rangle=0\), forces \(P_i=\theta_i\,e_2\), where \(e_2\perp\Phi\). The Dirac equation then reads \(c(\theta)e_2=0\).

In Penrose form, \(T^*_{\mathbb C}=S^+_0\otimes S^-_0\) and \(c(e\otimes s^-)\psi=\varepsilon(e,\psi)s^-\). So the Dirac equation forces \(\theta=e_2\otimes s^-\) with \(s^-\in S^-_0\) arbitrary. The norm \(|s^-|\) is fixed by \(|P|^2\).

Now count dimensions and stabilizers:
- \(\mathrm{Spin}^c(4)\) acts transitively on the sphere \(|\Phi|^2=\rho_*\).
- The stabilizer of \(\Phi\) contains all of \(SU(2)_-\), and \(SU(2)_-\) acts transitively on the sphere of \(s^-\).
- Hence \(\mathcal O_*\) is one orbit of dimension \(3+3=6\), and the stabilizer has dimension \(7-6=1\).

Write elements as \([A,B,\lambda]\), acting on \(S^\pm\) by \(\lambda A,\lambda B\) and on \(L\) by \(\lambda^2\). In the Penrose model the stabilizer is
\[
U(1)_*=\{[\operatorname{diag}(\bar\lambda,\lambda),\ \operatorname{diag}(\bar\lambda^3,\lambda^3),\ \lambda]\},
\]
and it acts on \(L\) by \(\lambda^2\).

The script verifies this independently of these conventions:
- orbit dimension 6;
- stabilizer dimension 1;
- weight on \(L\) equal to 2 for the generator normalized by \(t=1\);
- \(\tau\) fixed by the stabilizer;
- \(|\tau|^2=1.580246913580\ldots=128/81\). ∎

A geometric reading: the endpoint first jet is invariant under a simultaneous rotation of the tangent space and gauge transformation. That combined transformation rotates the fibre of \(L\).

## 2. First-order no-go theorem

**Theorem 89.2.** Let \(f\) be any continuous \(\mathrm{Spin}^c(4)\)-equivariant bundle map to \(L^m\), \(m\ne0\). Its inputs are the jets \((\Phi,\nabla_A\Phi)\), optionally together with zero-order curvature data whose endpoint values are equivariant functions of these jets. Such data include:
- \(F_A^+=2i\sigma(\Phi)\);
- \(\operatorname{Ric}+g\to0\) and \(W^+\to0\);
- the bounded ASD model \(K=-\tfrac98\rho^3Q/S\), with \(Q=-iq_-(\tau)\), from (A.10).

Then:
1. \(f\equiv0\) on \(\mathcal O_*\).
2. Along every O10 endpoint sequence, \(f(\Phi_j,\nabla\Phi_j)\to0\) in measure.

*Proof.* For \(g\in U(1)_*\) and \(x\in\mathcal O_*\), equivariance gives \(f(x)=f(gx)=\lambda^{2m}f(x)\) for every \(\lambda\), so \(f(x)=0\).

The level set defining \(\mathcal O_*\) is compact. More explicitly, on the sets where the norm residuals are small, \((\Phi_j,P_j)\) stays in a fixed bounded subset of the finite-dimensional representation. If distance from \(\mathcal O_*\) failed to tend to zero while all defining residuals did, a bounded subsequence would converge to a point outside \(\mathcal O_*\) satisfying its equations, a contradiction. Thus, provided (A.15)–(A.16) give measure convergence of all displayed residuals and \(D_A\Phi=0\) exactly, \(\operatorname{dist}((\Phi_j,P_j),\mathcal O_*)\to0\) in measure. Uniform continuity near the compact orbit then gives the second claim. ∎

**Consequence (algebraic scope).** Every charged natural section built from this first jet vanishes on the ideal endpoint orbit. This rules out a nonzero-modulus first-jet input for the rank-one lemma. It does **not** classify all sections admitting density-independent analytic estimates: the weighted Hessian result (A.12) is not an unconditional unweighted \(H^1\) theorem for every first-jet polynomial, and a projected differential equation may cancel curvature terms invisible in a full-tensor norm.

No pointwise polynomial choice in \((\Phi,\nabla\Phi)\) repairs the nonvanishing problem. The obstruction is not nonexistence of equivariant polynomials; it is that \(U(1)_*\) acts nontrivially on \(L\), so every charged natural first-order section vanishes at the ideal endpoint. The rank-one lemma of `O10_All_Finite_Density.md` §2 needs \(|\sigma|\to\ell>0\), so it cannot be supplied by such a first-jet section.

## 3. Second order: the surviving coefficient is the unique charge-5 direction

Consider the linear representation \(Q\in T^*\otimes E\), which has complex dimension 8. In the finite-density proof the analytically controlled object is actually \(Q=\nabla v\) for the bounded resolvent field \(v\), not automatically the local jet \(\nabla\tau\). The representation calculation applies to either tensor, but identifying their endpoint data requires a derivative comparison that has not been proved. The \(U(1)_*\) weights on this representation, in units of the \(L\)-charge, form the multiset
\[
\{-2,-1,1,1,2,2,4,5\}.
\]
The script computes the following:
1. \(Q\mapsto\sigma(Q)=\Phi\wedge t(\tau;Q)\) is an exact eigen-functional of charge \(5\).
2. The charge-5 eigenspace is one-dimensional.
3. Take a \(Q\) in that eigenspace with \(|Q|^2=2m_*\), which is the endpoint value \(|\nabla v|^2\to2m_*\) in (6) of `O10_Weak_Bianchi.md`. It gives
\[
|\sigma|^2=21.0461945289\ldots=4\rho_*m_*^3 .
\]
This is exactly the corpus endpoint value with \(|c|=1\).

The adapted-frame projection equations in the finite-density analysis leave only \(C=(\nabla_{\bar Z_2}v)_2\), with \(|C|^2\to4m_*\); together with the representation calculation, this identifies that **resolvent-field** coefficient as the charge-five weight vector. Matching the scalar norm alone would not identify it.

**Theorem 89.3 (minimal detectable charge, conditional local version).** Put \(\mu=\lambda^2\), which parametrizes the effective circle. Suppose the augmented endpoint data are \(\mathcal O_*\) together with one nonzero charge-five component of fixed modulus, all other components of the chosen \(T^*\otimes E\) tensor tending to zero. Then:
- \(U(1)_*\) acts on \(c\) by \(\mu^5\), so the residual stabilizer is \(\mathbb Z_5\);
- \(\mathbb Z_5\) acts on \(L^m\) by \(\mu^m\);
- hence every equivariant \(L^m\)-valued function of this **specified augmented endpoint** vanishes there unless \(5\mid m\). Additional full-second-jet components could reduce the stabilizer further.

In particular \(L^{\otimes5}\) is the minimal positive power permitted by this specified augmented endpoint. Among complex-linear endpoint symbols on \(T^*\otimes E\), \(\sigma\) is unique up to scale. This is not uniqueness of global nonlinear formulas, which may differ by terms vanishing on the orbit. The finite-density source proves the one-mode statement for \(\nabla v\) and uses \(\Phi\wedge t(v)\); it does not transfer it automatically to \(\nabla\tau\).

For a pointwise formula using \(\nabla\tau\), ordinary differentiation introduces \(\nabla^2\tau\sim\nabla^3\Phi\). Step 47 gives, per Taub–NUT core:
- \(\int|\nabla^2\tau|^2=\tfrac{2m_*}5\int|W^-|^2\);
- \(\int|\nabla^3\Phi|^2=64\pi^2/45\), which is scale invariant.

Differentiating any pointwise second-jet construction formally introduces third derivatives, and the **available full-tensor estimate** for these derivatives grows with the density of \(W^-\). This alone is not a lower bound for the derivative of the projected line section: Dirac, exterior-derivative, and curvature projections can cancel precisely the components measured by the full norm.

**What this establishes.** Under the specified finite-density resolvent endpoint with \(|c|\to1\), \(L^5\) is the minimal permitted positive charged line and \(\sigma\) is the unique complex-linear endpoint symbol on the charge-five component. It does not prove that every local route requires the full \(H^1\) estimate from Step 47, nor does it describe the proposed \(c\)-depleted phase. Step 47's reduction through \(\|\nabla N_\tau\|_{2,\rm av}\to0\) remains one sufficient conditional route, not a necessary form of all local arguments.

What remains open beyond this theorem:
- whether the actual projected equation for \(\sigma\), or another charged current, retains an uncontrolled \(W^-\) term after all contractions;
- nonlocal sections, such as Hodge or resolvent projections whose regularity is not inherited pointwise;
- endpoint configurations in a \(c\)-depleted phase, where second-jet components of charges \(\{-2,-1,1,2,4\}\) might replace \(c\). Which components a nut phase actually occupies has not been determined.

## 4. The rank-two side: a density-free section whose bundle sees \(W^-\)

The torsion \(\tau\in E=S^-\otimes L\) is first order in \(\Phi\), and \(|\tau|^2\to m_*\) in measure at the endpoint. A density-independent unweighted \(L^2\) bound for \(\nabla\tau\) requires checking the precise weights in (A.12); it does not follow merely from calling \(\tau\) first order.

The relevant characteristic number follows from \(p_1(\Lambda^\pm)=a^2-4c_2(S^\pm)\), with \(p_1(\Lambda^+)=2\chi+3\tau\) and \(p_1(\Lambda^-)=3\tau-2\chi\). Writing \(T_-=2\chi-3\tau\),
\[
c_2(E)=c_2(S^-)+c_1(S^-)\,a+a^2=\frac{9a^2+T_-}{4}.
\]
Two checks:
- When \(a^2=2\chi+3\tau\) this is \(5\chi+6\tau\), the Euler class of the almost-Kähler torsion bundle \(\Lambda^{0,1}\otimes\Lambda^{0,2}\) from Step 58.
- At the endpoint, \(a^2/V\to1/(6\pi^2)\) and \(T_-/V\ge1/(6\pi^2)-o(1)\). Hence \(c_2(E)/V\ge5/(12\pi^2)-o(1)\).

A nearly nonvanishing \(H^1\) section, even with bounded rank-two curvature, does **not** force \(c_2(E)/V\to0\): a point zero in four dimensions can carry nonzero degree with uniformly bounded Dirichlet energy. For example, a rank-two bundle with \(c_2=1\) over a fixed \(S^4\) admits unit sections off one point whose degree-one angular behavior has \(|\nabla s|=O(r^{-1})\); cutting the section to zero inside radius \(\varepsilon\) costs only \(O(\varepsilon^2)\). Thus no rank-two analogue of the rank-one transgression used in O10 is available under these hypotheses. The fact that the curvature of \(E\) contains \(W^-\) is still relevant to the Taub–NUT carrier, but it is not the only obstruction to a rank-two argument.

The exact Taub–NUT phase realizes the escape:
- \(\tau_{\rm TN}=\sqrt2\rho_*a\,d\bar f\) has \(|\tau|^2=m_*/V\), so it has an isolated zero at each nut.
- Per core, \(\int|\nabla\tau|^2=8\pi^2m_*\ell^2\), which is critical. A phase with \(N\sim V/\ell^2\) cores therefore costs bounded normalized \(H^1\) energy.
- The core carries \(\int|W^-|^2=8\pi^2\), but without a local index calculation or relative Chern transgression this is **not yet identified** with the local \(c_2(E)\)-charge of the torsion zero.

**Structural statement.** The two bundle constructions expose different difficulties but do not form an exhaustive dichotomy:
- **Rank two.** \(E\) carries a first-order natural section; point zeros in four dimensions are \(H^1\)-cheap, and its curvature includes \(W^-\). No rank-two Chern conclusion follows from the displayed energy bounds alone.
- **Rank one.** Charged first-jet maps vanish on the calibrated orbit. The finite-density proof reaches \(L^5\) only after resolving and controlling a higher-order field.

A density-free theorem may use a projected differential identity, another higher-jet endpoint, or a nonlocal construction. A closed \(c\)-depleted nut phase remains one possible escape, not the logical complement of the proved algebra.

## 5. The same stabilizer in the almost-Kähler (Q4) setting

Take an almost-Kähler pair \((g,\omega)\). Its torsion \(\alpha\in\Lambda^{0,1}\otimes K^{-1}\cong\bar{\mathbb C}^2\otimes\det^{-1}\) is a \(U(2)\)-representation.

- At \(\alpha\ne0\), the stabilizer \(\operatorname{diag}(a,\bar a^2)\) acts on \(K\) with nontrivial weight.
- At \(\alpha=0\), the stabilizer is all of \(U(2)\).

**Corollary 89.4.** Every natural section of \(K^m\), \(m\ne0\), built pointwise from \((g,\omega,\nabla\omega)\) without curvature vanishes identically.

So canonical-line information is first visible either through curvature, as in the \(W^+\)-component \(\eta\) of Step 77, or through the second jet \(\nabla\alpha\). This explains why every closed-Goldberg identity found so far (Steps 77–82) runs through \(\eta\), \(\partial r-\eta\alpha\), or the second-order \(dd^c\log q\). The obstruction is algebraic, not a failure to search hard enough.

## 6. Local isotropy at Wahl cone points

This section responds to A02 #883. On the orbifold \(V\) with points \(\tfrac1{n^2}(1,n-1)\), `wahl_isotropy.json` tests only the canonical complex-orbifold \(\mathrm{spin}^c\) lift twisted by \(\chi^j\), \(\chi=\zeta^n\). The boundary sequence for \(B_{n,1}\) is
\[
0\to H^2(B)=\mathbb Z_n\to H^2(\partial B)=\mathbb Z_{n^2}\to H^3(B,\partial B)=\mathbb Z_n\to0,
\]
with image \(n\mathbb Z_{n^2}\). Thus these \(\zeta^{nj}\) are precisely the boundary twists extending over the rational ball; they do **not** enumerate the extra quotient cosets of the complement. For a general twist \(\zeta^r\), the two positive-spinor weights are \((r,r-n)\), and \(r=1\) permits an invariant first-jet component. The conclusions below therefore concern the tested extendible family, not every orbifold spin\(^c\) structure. The script sampled \(n=2,\dots,15\), while the same congruence argument proves the stated extendible-twist conclusions for every \(n\ge2\):

1. **The monopole \(\Phi\).**
   - \(\Phi(p)\) can be nonzero only for \(j=0\), where the value lies in \(\Lambda^{0,0}\), or \(j=1\), where it lies in \(\Lambda^{0,2}\otimes\chi\).
   - For \(n\ge3\) and \(2\le j\le n-1\), the monopole has a forced zero at every cone point.
   - \(\nabla\Phi(p)=0\) for every **tested extendible twist** \(r=nj\) and every \(n\). It is false for arbitrary boundary twists; for example \(r=1\) admits an invariant first jet.
2. **The almost-Kähler structure.**
   - The invariant part of \(\Lambda^+_p\) is \(\mathbb R\omega_0\). So any AK structure on \(V\) equals \(\pm\) the cone complex structure at \(p\).
   - The \(\Lambda^{2,0}\)-part of \(\nabla\omega(p)\) vanishes.
   - The torsion section of \(E=\Lambda^{0,1}\otimes\Lambda^{0,2}\) vanishes at \(p\). For \(n\ge3\) its first jet also vanishes, so the zero has order at least 2. For \(n=2\) the ambient invariant first-jet space has complex dimension 4 (real dimension 8 before imposing differential compatibilities).

These constraints are invisible to \(H^2(\,\cdot\,;\mathbb Q)\) and to \(K^2\). They do not yet obstruct: nondegenerate torsion zeros have index \(+1\) (Step 60), and the orbifold count is large and positive,
\[
5\chi_{\rm orb}+6\tau_{\rm orb}=\tfrac14\bigl[9(A-k)+T_-(M)-4\textstyle\sum_j(1-n_j^{-2})\bigr].
\]

**What this implies for the Wahl sector.**
- The Step-85/87 Kähler-comparison machinery has nothing to compare with. V has no KE orbifold metric (A02, Prop. 102.K), so no Biquard–Rollin KE/CSCK branch exists on V.
- Any Einstein metric on \(V\) is non-Kähler.
- The almost-Kähler isotropy statement is independent of the spin\(^c\)-twist bookkeeping: an AKE orbifold metric would have \(D=T_{\rm AK}>0\) and forced higher-order torsion zeros at the cone points. This is still only local information; no quantitative global contradiction follows.
- Before using monopole zeros or jets, one must identify an actually supplied orbifold spin\(^c\) class. Scalar/mixed-curvature transfer through the smooth filler does not itself supply one.

## 7. Effect on the programme

- **First-jet charged search closed; second-jet analysis remains open.** Theorem 89.2 excludes nonzero-modulus charged sections built from the ideal first jet. Theorem 89.3 identifies the unique charge-five line under the calibrated finite-density second-jet hypothesis. It does not reduce density-free O10 to two alternatives, because projected equations may cancel the full-tensor \(W^-\) cost and the \(c\)-depleted second-jet set has not been classified.
- **Scope relative to Q1.** For \(X\#k\overline{\mathbb{CP}}^2\) with \(0<k/A<1/3\), finite-density O10 already applies (Spirit #118). That application controls \((P+D_\beta)/V\), not \(P/V\). Density-free O10 therefore matters for families with \(\chi/A\to\infty\), not for the small-blowup existence problem.
- **Q4.** Corollary 89.4 shows that second-jet or curvature information is unavoidable in any closed Goldberg argument that detects \(c_1(K)\).
