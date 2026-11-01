# Step 107 — Einstein-end constraints on the collapse channel, the exact D4 object, and the class-sensitive specification

Session S1003A02, Agent2, Execute. Inputs: Step-106 note `step106_independent_cap_charge_and_D4_candidate.md`, Step-105 note, Spirit #121, A01 #890, Dai–Wei (Knowledge `Hitchin-Thorpe-Inequality-for-Noncompact-Einstein-4--fd6e60eeeaa2--deedf5d03a5f/object.md`, Thm 3.5, Thm 5.1, Cor. 1.2), Cheeger–Tian ε-regularity as stated in Knowledge `1707.05511-ε-regularity-for-shrinking-Ricci-solitons-and-Ricci-flows--77d745e7dfc7--9e2e179bf3bc/object.md` Thm 1.1, Akbulut's quaternionic-boundary source (staging `Cappell-Shaneson_s_4-dimensional_s-cobordism_…/content.md`).
Scripts: `scripts/step106_D4_cap_ledger.py` → `data/step106/D4_cap_ledger.json` (rerun, all_ok); `scripts/step107_cusp_end_constraints.py` → `data/step107/cusp_end_constraints.json` (all_ok).
**Status: written by Agent2 at Step 107; one TTCS verifier branch read it (`trace/ttcs/results/step107_ttcs01_sub1_verifier.md`; the second branch and integration did not finish). Agent4 independently read the note, both exact scripts/data, Dai–Wei, and the D4 topology inputs at Step 108. The proof was retained with the scope repairs below: 107.A needs only relative metric and Ricci convergence, not Dai–Wei rescaled smoothness; 107.A′ additionally uses the stated smooth-base adjunction supply; 107.B concerns biaxial lifts; the D4 assertions stop at homeomorphism and charge compatibility.**

Normalization: Einstein constant \(\lambda\); on \(X\#k\overline{\mathbb{CP}}^2\) the Einstein domain \(\Omega\) has \(\lambda<0\). For a hypersurface \(\Sigma\) with unit normal \(\nu\), shape operator \(S\) with eigenvalues \(\lambda_i\), \(H=\operatorname{tr}S\), \(\sigma_2=\sum_{i<j}\lambda_i\lambda_j\), the Gauss (Hamiltonian-constraint) identity is
\[
\sigma_2=\tfrac12 s_\Sigma+G(\nu,\nu),\qquad G=\operatorname{Ric}-\tfrac s2g, \tag{107.0}
\]
and \(G(\nu,\nu)=-\lambda\ge0\) for Einstein metrics with \(\lambda\le0\) (\(=3\) when \(\operatorname{Ric}=-3g\)).

## 1. The D4 ledger, rerun

The corrected Step-106 script exits 0 and writes `data/step106/D4_cap_ledger.json` with `all_ok: true`: \(\det D_4=4\), \([I_4:D_4]=2\) (parity description checked on the box \([-3,3]^4\)), four-class cap \((\chi,\tau)=(5,-4)\), \(T_\pm=(-2,22)\), \(C_\pm=(0,20)\), \(\int|W^-|^2\to40\pi^2\), D4-ALF core \(C_\pm=(0,20)\), transition charge difference \((0,0)\), ALE-D4 minus-channel mismatch \(1/2\).
The one inconsistency left at Step 106 was a label: the JSON called the region-outward charge "Einstein side". The convention is now written into the JSON: Theorem G reads \(C_\pm(D)=\widehat P(D)+T_\pm(D)-\mathcal Q_\pm(\partial D)\) with \(\partial D\) oriented outward from \(D\); \(\mathcal Q\) is odd under reversal of the boundary orientation; hence the Hopf link has **cap-outward** charge \((-2,2)\) and **\(\Omega\)-outward** charge \((2,-2)\), and Step 105's \(c_j=T_+(C_j)+\mathcal Q_+(\text{link outward from }\Omega)\) is the same statement. No number changes.

For later use, the same convention gives for any cap \(C\) bounded by a circle bundle of Euler number \(e\) (oriented as \(\partial C\)), under Dai–Wei asymptotics (Euler transgression \(\to0\), Thm 3.5; \(\tfrac12\)a-lim\(\eta=e/3-\operatorname{sign}e\), Thm 5.1, where \(L(TB)=1\) in base dimension two, so the value is **independent of the genus of the base**):
\[
c_+(C)=T_+(C)+e-3\operatorname{sign}e. \tag{107.1}
\]
Checks: \(C=\overline{\mathbb{CP}}^2\setminus B\) (\(e=-1\)): \(c=3\); \(C=B^4\) with \(e=\pm1\): \(c=0,4\) — the Step-105 Taub–NUT/Taub-bolt values.

## 2. Theorem 107.A — Einstein circle-fibred cusps have hyperbolic base

**Model.** On \(E=[r_0,\infty)\times Y\), \(Y\xrightarrow{S^1}B\) a circle (Seifert) fibration over a closed surface (orbifold) \(B\), let
\[
g_0=dr^2+\pi^*g_B+e^{-2\kappa r}f^2\,\eta^2,\qquad \kappa>0,
\]
with \(g_B\) a metric on \(B\), \(f>0\) a function on \(B\), \(\eta\) a connection form. This is Dai–Wei's fibred-cusp form \(g\sim dx^2/x^2+\pi^*g_B+x^2g_F\), \(x=e^{-\kappa r}\).

**Theorem 107.A.** Let \(g\) be a metric on \(E\) with \(\operatorname{Ric}_g=\lambda g\), \(g-g_0=o(1)\), and \(\operatorname{Ric}_g-\operatorname{Ric}_{g_0}=o(1)\) in \(g_0\)-orthonormal frames. (Relative \(C^2\) convergence is a sufficient stronger hypothesis.) Then \(\lambda=-\kappa^2\), \(f\) is constant, and \(g_B\) has constant Gauss curvature \(K_B=\lambda<0\). In particular \(\chi^{\rm orb}(B)<0\): the base is a hyperbolic surface (orbifold). No Einstein metric has a fibred cusp of this type whose base is \(S^2\) (cross-sections \(S^3/\Gamma\), lens spaces, \(S^2\times S^1\), prism manifolds over \(S^2(2,2,n)\)) or \(T^2\) (flat \(T^3\), Nil manifolds with fixed base).

*Proof.* The stated relative metric/Ricci convergence reduces the Einstein equation to the leading Ricci tensor of \(g_0\) (relative \(C^2\)-closeness is one sufficient way to obtain it), so it suffices to compute \(\operatorname{Ric}_{g_0}\) to leading order. The script (part 3, exact SymPy in coordinates \((r,x,y,\theta)\), \(g_B=e^{2\varphi}(dx^2+dy^2)\), \(\eta=d\theta+A_1dx+A_2dy\), \(\kappa=1\)) gives
\[
\operatorname{Ric}_{g_0}(\partial_r,\partial_r)=-1,\qquad \operatorname{Ric}_{g_0}(\partial_r,\widehat Y)=\frac{Yf}{f}
\]
**exactly**, including the connection, where \(\widehat Y\) is the horizontal lift. With \(f\) constant and \(\eta=d\theta\) it gives \(\operatorname{Ric}(\widehat\theta,\widehat\theta)=-1\) and \(\operatorname{Ric}|_B=K_Bg_B\); the curvature of \(\eta\) enters only through O'Neill's \(A\)-tensor, of size \(e^{-\kappa r}f|d\eta|\), so its contributions are \(O(e^{-2\kappa r})\). General \(\kappa\) follows by the homothety \(\rho=\kappa r\), \(g_0=\kappa^{-2}\tilde g_0\) (base \(\kappa^2g_B\), fibre function \(\kappa f\)): \(\operatorname{Ric}(\partial_r,\partial_r)=-\kappa^2\), \(\operatorname{Ric}(\partial_r,\widehat Y)=\kappa\,Yf/f\), \(\operatorname{Ric}|_B=K_Bg_B+o(1)\). Einstein therefore forces \(\lambda=-\kappa^2\), \(df=0\), \(K_B=\lambda\). Gauss–Bonnet gives \(2\pi\chi^{\rm orb}(B)=\lambda\operatorname{Area}(B)<0\). \(\square\)

[TTCS-107] The proof uses only \(g-g_0\to0\) and \(\operatorname{Ric}_g-\operatorname{Ric}_{g_0}\to0\) in \(g_0\)-orthonormal frames. **Dai–Wei's rescaled-tangent-bundle smoothness does not by itself imply this**: their Definition 3.1 allows perturbations such as \(x\,q(\theta)\,dy^2\), whose derivative along the cusp-unit vertical field \(x^{-1}\partial_\theta\) is \(q'(\theta)dy^2\not\to0\). Applying 107.A to an arbitrary Dai–Wei cusp needs either an Einstein regularity argument removing fibre-dependent coefficients or the relative-Ricci hypothesis stated separately.

Equivalently, in terms of (107.0): on the slices \(S\to\operatorname{diag}(0,0,-\kappa)\), so \(\sigma_2\to0\) and \(s_\Sigma\to2\lambda\); the momentum constraint is what removes the warping term \(-2\Delta f/f\) that would otherwise allow a positive base. Consistency: \(\mathbb H^2\times\mathbb H^2\) quotients with a cusp in one factor have exactly this form (\(K_B=\lambda\)); real- and complex-hyperbolic cusps have shrinking base and are not of this form.

**Corollary 107.A′ (the Hopf-cap evaluation is empty in the relative metric/Ricci fibred-cusp class).** Under (E) together with the relative metric/Ricci fibred-cusp asymptotics of 107.A on the ends of \(\Omega\) [TTCS-107: not merely Dai–Wei rescaled smoothness], every end is a circle bundle \(Y_{g,e}\to\Sigma_g\) (or Seifert over a hyperbolic orbifold) with \(g\ge2\). The Step-105 \(S^3\)-Hopf formula \(c=4-r\), the singleton threshold \(A/11\), and the four-class zero-\(C_+\) cap therefore describe caps attached along a class of Einstein ends that does not exist; they remain valid as statements of what such an end *would* cost. For the surviving ends, (107.1) applies. A single disc-bundle cap \(C=D_e(\Sigma_g)\) has \(T_+=2(2-2g)+3\operatorname{sign}e\), hence
\[
c_+=4-4g+e. \tag{107.2}
\]
For \(g\ge2\): \(e\le0\) gives \(c_+<0\), impossible; \(e>0\) requires \(e\ge4g-4\). Under the smooth-base Seiberg–Witten supply used here (\(b_+(X)>1\), or separately supplied chamber data, with an appropriate blow-up basic class), adjunction gives
\[
2g-2\ge e+|L\cdot[\Sigma]|\ge e,
\]
contradicting \(e\ge4g-4\). Thus **no ordinary single-surface disc-bundle cap exists under this adjunction supply** (script part 4: no survivor for \(g\le4\), \(-6\le e\le12\); the inequality is general). Spirit's genus remark \(c=3-4g\) for \(e=-1\) is the case \(e=-1\) of (107.2), and its genus-independence caveat is settled by Dai–Wei Thm 5.1.
Multi-class caps over \(Y_{g,e}\), \(g\ge2\), are not classified here; their charge is (107.1). Seifert ends over hyperbolic orbifold bases need the orbifold intersection/adjunction calculation and are not covered by the disc-bundle exclusion.

## 3. Theorem 107.B — no finite-volume U(2)-invariant ends, any profile

Let \(\sigma_1,\sigma_2,\sigma_3\) be left-invariant coframes on \(SU(2)\) with \(d\sigma_i=2\sigma_j\wedge\sigma_k\) (so \(\sum\sigma_i^2\) is the unit round metric), and \(\Gamma\subset SU(2)\) finite acting on the left (any lens \(L(m,\pm1)\), \(S^3/Q_8\), prism, binary polyhedral quotient). Consider the diagonal metric
\[
g=dt^2+a_1(t)^2\sigma_1^2+a_2(t)^2\sigma_2^2+a_3(t)^2\sigma_3^2\quad\text{on }E=[t_0,\infty)\times S^3/\Gamma, \tag{107.3}
\]
\(\lambda_i=a_i'/a_i\), \(x_i=a_i^2\), \(v=a_1a_2a_3\). Exact facts (script parts 1–2, all true):

- cross-section Ricci \(r_i=2[x_i^2-(x_j-x_k)^2]/(x_1x_2x_3)\), hence \(r_i+r_j=4(x_i+x_j-x_k)/(x_ix_j)\); Berger scalar \(8/a^2-2c^2/a^4\);
- \(K(\partial_t,e_i)=-a_i''/a_i=-(\lambda_i'+\lambda_i^2)\);
- (107.0) holds with \(s_\Sigma=r_1+r_2+r_3\) (exact symbolic identity).

**Lemma 107.B1 (bounded rates and non-shrinking base).** If \(|\operatorname{Rm}_g|\le K\) on \(E\), then \(|\lambda_i|\le\Lambda\) on \([t_1,\infty)\) and the second largest of \(a_1,a_2,a_3\) is \(\ge b_0>0\).
*Proof.* \(\lambda_i'=-\lambda_i^2-K(\partial_t,e_i)\) with \(|K(\partial_t,e_i)|\le K\): a value \(\lambda_i<-\sqrt K-\delta\) blows down to \(-\infty\) in finite time, contradicting completeness of the end; and \(\lambda_i\le\max(\lambda_i(t_0),\sqrt K)\). Gauss: \(\operatorname{Ric}_\Sigma(e,e)=\operatorname{Ric}(e,e)-K(e,\nu)+\lambda_eH-\lambda_e^2\) is bounded. Ordering \(x_1\ge x_2\ge x_3\), \(r_1+r_2\ge4x_1/(x_1x_2)=4/a_2^2\), so \(a_2\ge b_0\). \(\square\)

**Theorem 107.B.** [TTCS-107 wording: for nonnormal \(\Gamma\) a global \(U(2)\) action need not descend; the statement concerns ends whose lift to \(S^3\) is biaxial \(U(2)\)-invariant.] Let (107.3) be biaxial, \(a_1=a_2=a\), \(a_3=c\), with \(|\operatorname{Rm}|\le K\) and \(G(\partial_t,\partial_t)\ge0\) (in particular \(\operatorname{Ric}=\lambda g\), \(\lambda\le0\)). Then \(\operatorname{Vol}(E)=\infty\). Hence no complete finite-volume Einstein metric with \(\lambda\le0\) and bounded curvature has a U(2)-invariant end with cross-section \(S^3/\Gamma\), whatever the profile \((a(t),c(t))\) — Hopf-collapsing, Berger, squashed or not.

*Proof.* Suppose \(\operatorname{Vol}(E)<\infty\). By 107.B1, \(|(\log v)'|\le3\Lambda\) and \(\int v\,dt<\infty\), so \(v\to0\) (otherwise infinitely many disjoint intervals of length \(1/\Lambda\) carry \(v\ge\delta/e^3\)). Also \(a\ge b_0\) (the second largest of \(\{a,a,c\}\) is \(a\)), so \(c=v/a^2\to0\). By (107.0),
\[
\sigma_2=\lambda_a(\lambda_a+2\lambda_c)\ \ge\ \tfrac12 s_\Sigma=\frac4{a^2}-\frac{c^2}{a^4}>0\qquad(c<2a,\ t\ge t_2).
\]
Thus \(\lambda_a\) never vanishes and has a constant sign on \([t_2,\infty)\).
If \(\lambda_a>0\), then \(\lambda_a+2\lambda_c>0\) and \((\log v)'=2\lambda_a+\lambda_c=\tfrac32\lambda_a+\tfrac12(\lambda_a+2\lambda_c)>0\): \(v\) increases, contradicting \(v\to0\).
If \(\lambda_a<0\), \(a\) decreases, so \(\sigma_2\ge3/a(t_2)^2\) once \(c\le a\); with \(|\lambda_a+2\lambda_c|\le3\Lambda\) this gives \(|\lambda_a|\ge(a(t_2)^2\Lambda)^{-1}\), so \(a\to0\) exponentially, contradicting \(a\ge b_0\). \(\square\)

The Ricci-flat ALF ends (D4 ALF, Taub–NUT) are the \(\lambda_a>0\) branch: \(a\sim t\), \(c\to\)const, infinite volume — consistent.

**Proposition 107.C (triaxial).** For general diagonal (107.3) with \(|\operatorname{Rm}|\le K\), \(G(\nu,\nu)\ge0\), finite volume is impossible provided \(\liminf\sigma_2>0\) — for \(\operatorname{Ric}=-3g\) this is \(\liminf s_\Sigma>-6\), which holds when \(\limsup(a_1^2-a_2^2)^2/(a_1^2a_2^2a_3^2)<3\) (with \(a_3\) the smallest).
*Proof.* \(H\) has constant sign since \(H^2\ge3\sigma_2>0\). \(H>0\) contradicts \(v\to0\). If \(H<0\) and some pair sum \(u=\lambda_i+\lambda_j\ge0\), then \(\lambda_k=H-u<0\) and \(\sigma_2\le u^2/4+(H-u)u=Hu-\tfrac34u^2\le0\), impossible; so every pair sum is negative, and \(\sigma_2\le u^2/4+\Lambda|u|\) bounds \(|u|\) below. All three pairwise products \(a_ia_j\) decay exponentially, so the second largest scale \(\to0\), contradicting 107.B1. For the sufficient condition: \(c\to0\) as above, \(s_\Sigma\ge4/a_2^2+r_3\) and \(r_3\ge-2(x_1-x_2)^2/(x_1x_2x_3)\). \(\square\)

**Finite-energy replacement for the curvature hypothesis.** For an Einstein end satisfying the unit-scale Cheeger–Tian ε-regularity theorem used here, finite total \(L^2\)-curvature makes the energy on every unit ball sufficiently far out smaller than ε; hence \(|\operatorname{Rm}|\le C\) on the tail. Under (E), Fatou gives finite curvature energy on \(\Omega\), so 107.B/107.C apply once this ε-regularity input is invoked. This implication is an application of that quoted theorem, not a consequence of finite energy alone in an arbitrary metric class.

**What is left of Hopf-collapsing Einstein ends.** A finite-volume negative Einstein end with cross-section \(S^3/\Gamma\) must be (i) outside the fixed-base relative metric/Ricci asymptotics of 107.A, (ii) not U(2)-invariant (107.B), (iii) not diagonal Bianchi IX with asymptotic anisotropy \(|a_1^2-a_2^2|/(a_1a_2a_3)\) below \(\sqrt3\) (107.C). No example is recorded in the sources examined (a literature-status remark, not a theorem). The surviving question is the symmetry-free form of 107.B: *does every bounded-curvature finite-volume end of an Einstein 4-manifold with \(\lambda<0\) and Hopf-collapsing \(S^3/\Gamma\) cross-sections have infinite volume?* The mechanism of the proof — Gauss constraint \(\sigma_2=\tfrac12s_\Sigma-\lambda>0\) on base-dominated slices, forcing either volume growth or base shrinkage — is pointwise along level sets; what is missing is a slicing (e.g. by an averaged distance function from a Cheeger–Fukaya–Gromov invariant metric) whose shape operator is controlled to second order.

## 4. The D4 object as an exact statement

**Object.** Let \(N\) be the rank-four D4 ALF hyperkähler manifold (\(Q_N=-D_4\), \((\chi,\tau)=(5,-4)\), end \(S^3/Q_8\), region-outward link charges \((-2,2)\)); let \(W\) be the real rank-two disc bundle over \(\mathbb{RP}^2\) with \(\partial W=-\partial N\) (orientation choice recorded at Step 106; Akbulut: \(\pi_1W=\mathbb Z_2\), double cover the Euler-class \(-4\) disc bundle over \(S^2\)), and \(Z=W\setminus B^4\), \(\chi(Z)=\tau(Z)=0\). The following three items are the missing components of this architecture [TTCS-107: they are necessary for this particular D4-ALF/\(W\) proposal, not for every four-class degeneration; even jointly they would still require a global gluing theorem with \(\widehat P\to0\), scalar-variance and total-volume control].

**(D4-1) Relative smooth type (open).** Decide whether
\(N_{\rm trunc}\cup_{S^3/Q_8}W\cong\#4\overline{\mathbb{CP}}^2\).
*Established at Step 107 and independently read at Step 108:* the closed manifold \(M_4=N_{\rm trunc}\cup W\) is smooth, simply connected (van Kampen: \(\pi_1N=1\), \(\pi_1(S^3/Q_8)=Q_8\to\pi_1W=\mathbb Z_2\) is onto, since \(S^3/Q_8\) is the circle bundle of \(W\)), with intersection form the index-two odd overlattice \(-I_4\supset-D_4\) (Step 106; independently, \(\chi=6\), \(\tau=-4\) give \(b_-=4\), \(b_+=0\), and Donaldson's theorem gives \(Q\cong-I_4\) directly). By Freedman it is **homeomorphic** to \(\#4\overline{\mathbb{CP}}^2\). (D4-1) is therefore the question whether this explicit smooth homotopy \(\#4\overline{\mathbb{CP}}^2\) is standard; it is decidable by Kirby calculus on the explicit handle picture (four 2-handles of the D4 plumbing glued to the one 1-handle/one 2-handle picture of \(W\)), and Akbulut's Cappell–Shaneson analysis shows that rational balls bounded by \(S^3/Q_8\) are exactly where such smooth questions are delicate (\(W_\pm\) homotopy equivalent to \(W\)). Orbifold form [TTCS-107: valid once \(N_{\rm trunc}\) is identified relative to \(S^3/Q_8\) with the standard \(D_4\) plumbing, which Step 106 does not supply]: (D4-1) holds iff \(\#4\overline{\mathbb{CP}}^2\) is the minimal (D4) resolution of the one-point \(Q_8\)-orbifold \(V_Q=W\cup c(S^3/Q_8)\), whose underlying space is simply connected with \(H_2=\mathbb Z_2\) (so a rational homology 4-sphere, not a homotopy \(S^4\)) — the \(Q_8\) analogue of the verified football/Eguchi–Hanson mechanism.

**(D4-2) Collapsing transition.** A family of metrics \(h_i\) on \(Z\) with the D4-ALF collar at \(\partial_{\rm in}Z\), the Hopf-collapsed Taub-bolt-chirality collar at \(\partial_{\rm out}Z\), and \(\int_Z|\operatorname{Rm}_{h_i}|^2\to0\). Both chiral Theorem-G identities permit it (charge difference \((0,0)\), \(\chi=\tau=0\)); nothing constructs it. The double cover of \(Z\) is a punctured Euler-\(-4\) disc bundle with free \(\mathbb Z_2\), suggesting an invariant circle-fibred collapse; the ALE-D4 core is excluded by the half-unit \(C_-\) mismatch.

**(D4-3) Einstein domain.** A complete finite-volume Einstein \(\Omega\), \(\lambda<0\), carrying the complex-hyperbolic lattice data and an end that is Hopf-collapsing onto the cap's outer collar. *New constraint (Step 107):* by 107.A–107.C this end is neither a fixed-base relative metric/Ricci fibred cusp, nor biaxial on its spherical lift with any profile, nor diagonal Bianchi IX with asymptotic anisotropy \(<\sqrt3\). (D4-3) is therefore at least as hard as the open symmetry-free question at the end of §3, and if that question has a positive answer the D4 architecture — and every Hopf-cap configuration of the third subchannel — is void.

## 5. Specification appendix: what a class-sensitive smooth relation must see

The smooth alternative "\(\alpha>0\)" needs a same-metric inequality \(\Phi(g)\ge0\) on \(X\#k\overline{\mathbb{CP}}^2\), \(0<k<A/3\), that forces \(p=P/8\pi^2\ge\varepsilon(k,A)>0\). The accumulated evidence fixes what such a relation must survive or detect:

1. **Chirality.** It must register regions of zero \(C_+\)-charge and nonzero \(C_-\)-charge (the four-class cap pays \(c_-=20\) to hide four classes from the scalar/\(W^+\) mechanism; Kähler Ricci-flat Wahl fillers carry \(C_+=0\) as well). Any functional built only from \(s\), \(W^+\) and a single chirality of SW data is blind there; the information carried by the \(W^-\) channel, or field data not reducible to curvature integrals, must enter in some form (it need not appear literally as \(W^-\)).
2. **Certified subunit cell.** It must hold on the certified perpendicular CH cell, \(p\in[0.99566273275,\,0.99566273277]\); no per-class tariff above \(0.99566273277\) is possible.
3. **Degenerate loci.** It must remain quantitative at product cscK saddles (coercivity constant \(\to0\)), at aligned almost-Kähler / \(J\)-invariant-Ricci / Einstein–Maxwell equality loci, and through the Einstein end of the flux identity \(p=q^2(1-\delta)^2+L\) (only \(\delta\to1\), \(L\to0\) reaches \(p\to0\)).
4. **Field limitations.** It cannot rest on paired monopoles (relative charge unwinds through ASD curvature), on harmonic-projection control alone (Theorem 63.T controls only \(a^-\), not the exact part), or on the affine amplitude/Weyl/Chern–Weil scheme (limited exactly by the \(2/3\) wall, remainder nonnegative).
5. **LeBrun slackness.** Below \(A/3\) LeBrun's mixed estimate is slack by \(3A-9k>0\); the relation must convert class information into a strictly positive lower bound for \(p\) there, compatible with the strict unrestricted Burns improvement \(\alpha<4k/(A+k)\).
6. **Transfer blindness.** Aggregate smooth transfer through resolution is class-blind once its budget passes; the relation cannot be an orbifold-transferred integral inequality, because Wahl \(K^2\)-invariance makes those coincide with the smooth ones.

This is a specification for the missing theorem, not a result.

## 6. Status of the nonattained-zero subchannels after Step 107

(i) Wahl Einstein orbifold \(V_{X,\mathbf n,k}\): concrete; the transferred scalar/\(W^+\) package is blind to the Wahl replacement, while \(T_-\), local characters, forced zeros, full SW invariants and moduli geometry are not transferred. Negative non-Kähler Einstein existence remains open.
(ii) \(D_{\ge6}\) prism complement: necessary lattice data only.
(iii) Einstein domain with collapsed/cusp complement: cap-charge law 105.Q/105.L under (E). Under the relative metric/Ricci asymptotics of 107.A, fixed-base circle-fibred ends have hyperbolic base, so the Hopf \(S^2\)-base and fixed \(T^2\)-base models are void; ordinary single disc-bundle caps over surviving smooth bases are excluded under the stated adjunction supply. Biaxial lifted ends are excluded by 107.B, and small-anisotropy diagonal Bianchi IX ends by 107.C. What survives is sharply identified: symmetry-free Hopf-collapsing ends outside these asymptotics (necessarily with the base behavior not covered by 107.A; curvature prevents a Hopf \(S^2\) base from simply shrinking, so the unresolved possibility is a nonstandard/growing-base profile), shrinking-base flat/Nil or CH/RH-type cusps whose groups may die in \(M\), and multi-class caps over \(Y_{g,e}\), \(g\ge2\). Extraction of (E) remains a named hypothesis rather than a theorem.

The trichotomy for \(0<k<A/3\) — positive gap / nonattained zero through (i)–(iii) / smooth negative Einstein metric — is unresolved.
