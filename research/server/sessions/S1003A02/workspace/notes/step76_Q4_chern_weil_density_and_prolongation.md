# Step 76 — Q4: the canonical-connection Chern–Weil density of the torsion bundle, and formal prolongation at a torsion zero

Agent2, Execute. Inputs: Step 75 note `step75_Q4_half_twistor_torsion_and_zero_index.md`; Spirit #92; A01's exact Bianchi-VIII AKE pair (`Sessions/S1003A01/workspace/scripts/step59_chiral_exact.py`, `data/step59/chiral_exact.json`, `notes/step59_chiral_completion_and_zero_charge.md`).
Scripts: `workspace/scripts/step76_cw_density_on_pair.py` → `workspace/data/step76_cw_density_on_pair.json`; `workspace/scripts/step76_ake_prolong.py` → `workspace/data/step76_prolong_order2.{json,pkl}`.

Labels: [P] proved here, [N] exact symbolic/numerical check, [O] open.

## 1. Chern–Weil density of \(c_2(E)\) for the canonical connection [P,N]

Setting: \((M^4,g,J,\Omega)\) almost-Kähler, \(\nabla\Omega=a\otimes\phi-Ja\otimes J\phi\), \(\nabla\phi=-a\otimes\Omega+b\otimes J\phi\), \(q=|\nabla\Omega|^2=4|a|^2\), \(E=\Lambda^{0,1}\otimes\Lambda^{0,2}\), \(c_2(E)=c_2+2c_1^2\), \(\langle c_2(E),[M]\rangle=5\chi+6\tau\).

**Splitting of the canonical curvature.** Write \(\nabla=\bar\nabla+A\), \(\bar\nabla\) the canonical Hermitian connection, \(A=-\tfrac12J\nabla J\) with values in \(\mathfrak m=[\![\Lambda^{0,2}]\!]\subset\Lambda^+\). Then \(R_{\mathfrak u}=\bar R+(A\wedge A)_{\mathfrak u}\) and \([\mathfrak m,\mathfrak m]\subset\Lambda^+\cap\mathfrak u(2)=\mathbb R\Omega\) (because \([\Lambda^+,\Lambda^-]=0\)). Hence

* the \(\Lambda^-=\mathfrak{su}(2)\) part of \(\bar R\) equals that of the Levi-Civita curvature, so \(p_1(\Lambda^-)\) has the same density for both connections;
* the \(\Lambda^+\) bundle reduces to \(\mathbb R\Omega\oplus K^{-1}\), and the curvature of \(K^{-1}\) is \(db\). From the Ricci identity for \(\phi\),
  \[
  db=a\wedge Ja-R(\Omega) ,\qquad \gamma_J=-db,\qquad (db)^+=-(\tfrac s4+\tfrac q8)\Omega-\eta,\quad (db)^-=(a\wedge Ja)^- ,               \tag{76.1}
  \]
  (overall sign corrected by the Step-76 verifier from AAD's connection and Ricci identities; the script cannot detect the overall sign because only squares enter (76.2)–(76.4), whereas flipping the *relative* sign would give a balance bracket with A01-pair integral \(448/3\neq0\)). Darboux connection convention: \(\bar\nabla=\nabla+A\), \(A=-\tfrac12J\nabla J\).

Since \(e=\tfrac14(p_1(\Lambda^+)-p_1(\Lambda^-))\) and \(c_1^2=p_1(\Lambda^+)=\tfrac1{4\pi^2}db\wedge db\),
\[
c_2(E)=\tfrac94\,p_1(\Lambda^+)-\tfrac14\,p_1(\Lambda^-).                     \tag{76.2}
\]
For an Einstein metric, normalized \(s=-12\), \(W^+(\Omega)=\tfrac\kappa6\Omega+\eta\), \(\kappa=s+\tfrac32q\), \((a\wedge Ja)^\pm\) each of norm\(^2\) \(|a|^4/2=q^2/32\), the self-dual part of \(db\) is \(-(\tfrac s4+\tfrac q8)\Omega-\eta\) and the anti-self-dual part is \((a\wedge Ja)^-\) (squares unchanged). Therefore

\[
\boxed{\;4\pi^2\,c_2(E)_{\bar\nabla}=\Bigl(42-\tfrac{27}{8}q+\tfrac94|\eta|^2+\tfrac12|W^-|^2\Bigr)\,d\mu\qquad(s=-12).\;}       \tag{76.3}
\]
Kähler–Einstein check: \(q=\eta=0\) gives \(42+\tfrac12|W^-|^2\), which equals the Levi-Civita density \(15+\tfrac92|W^+|^2+\tfrac12|W^-|^2\) with \(|W^+|^2=6\).

**Transgression = AAD balance.** Using \(|W^+|^2=\kappa^2/24+|\eta|^2+|W_3^+|^2\),
\[
\Bigl(15+\tfrac92|W^+|^2+\tfrac12|W^-|^2\Bigr)-(76.3)=\tfrac94\Bigl(|\eta|^2+2|W_3^+|^2+\tfrac3{16}q^2-\tfrac32q\Bigr).        \tag{76.4}
\]
So the Levi-Civita and canonical Chern–Weil representatives of \(5\chi+6\tau\) differ pointwise by exactly \(9/4\) times the AAD/A01 balance integrand. The integrated AAD balance on a closed AKE manifold is the statement that this transgression integrates to zero. A01's verification that the balance vanishes on the complete pair shows that the transgression flux decays at the ACH end.

**Evaluation on A01's complete strict pair** [N] (`step76_cw_density_on_pair.json`). The three normalization identities \(X_1+X_2=1\), \(X_1w_1+X_2w_2=\kappa/6\) and \(\sum w_i^2=\kappa^2/24+|\eta|^2+|W_3^+|^2\) hold exactly, and (76.4) holds identically in \(p\). The density is
\[
4\pi^2c_2(E)_{\bar\nabla}=\frac{6\,(567p^8+783p^6+297p^4+165p^2-20)}{(3p^2+1)^4},\qquad \tfrac13\le p<1,
\]
increasing from \(6\) at the bolt (where \(q=32/3\)) to \(42\) at infinity. It is strictly positive everywhere.

**Consequence.** The proposed test is whether the canonical (b-)connection density of \(c_2(E)\) is \(\le0\) on the AKE variety. It fails on the strict pair: the density is \(\ge 6/(4\pi^2)\) everywhere. More generally (76.3) shows the density is negative only where \(q>\tfrac{8}{27}(42+\tfrac94|\eta|^2+\tfrac12|W^-|^2)\ge 112/9\). Neither the Levi-Civita nor the canonical Hermitian representative can carry a sign obstruction. Any Chern–Weil route must use a connection singular at the torsion zeros, for example the one induced through the opposite structure \(I\) off \(Z\), or the Mathai–Quillen form of the section. That returns the problem to the zero set, in line with §3 of the Step-75 note.

## 2. Formal prolongation at a torsion zero: the Darboux formulation [P]

Closed nondegenerate \(\Omega\) has Darboux coordinates, \(\Omega=dx^1\wedge dx^2+dx^3\wedge dx^4\). Compatible metrics near \(\delta\) are exactly \(g=\exp H\), with \(H\) symmetric and \(HJ_0=-J_0H\) (6 functions; \(\det g=1\) automatically). For every such \(g\), \((g,\Omega)\) is almost-Kähler with \(J=g^{-1}J_0\). The only equation is
\[
\mathcal E(H)=\operatorname{Ric}(e^H)-\lambda e^H=0 .
\]
The residual gauge is the group of Hamiltonian diffeomorphisms. The 1-jet of \(H\) has 24 parameters; cubic Hamiltonians act injectively on it (their fields have no linear Killing part), with image of dimension 20. The quotient, of dimension 4, is the torsion. Hence **at a torsion zero one may take \(H=O(|x|^2)\)**, and AKE germs with \(T(0)=0\) are the formal solutions with \(H=H_2+H_3+\cdots\), modulo Hamiltonian diffeomorphisms of order \(\ge4\) and \(U(2)\).

Order structure: \(\mathcal E_k=L_kH_{k+2}+N_k(H_2,\dots,H_{k+1})-\lambda[e^H]_k\), with \(L_k\) the flat linearized Ricci operator on anti-\(J_0\) symmetric matrices.
* \(N_1=0\), so order 1 is linear homogeneous.
* \(N_2=Q(H_2,H_2)\), so the first nonlinear compatibility conditions occur at order 2. They are \(\langle\ell,Q(H_2)-\lambda H_2\rangle=0\) for \(\ell\in\operatorname{coker}L_2\) beyond the linearized Bianchi relations, and they are quadratic in the 2-jet. The linear torsion \(T_1\) is part of the 2-jet.
* Count: anti-\(J_0\) unknowns 6, gauge 1, Einstein equations 10, Bianchi 4. The linear system is overdetermined by one function's worth per order, so genuine nonlinear compatibility conditions are expected.

The linear torsion is \(a_k(x)=\tfrac12\langle\nabla_k\Omega,\phi_0\rangle\), \(\phi_0=dx^{13}-dx^{24}\). The index of a nondegenerate zero is \(\operatorname{sign}\det(\partial a_k/\partial x^m)\): the source and target orientations both come from \(\Omega^2\), and every complex structure on the rank-2 bundle \(E\) induces the same real orientation.

## 3. Order-2 compatibility and the index of AKE torsion zeros [P via A01 62.A; N here]

**Computation** (`step76_prolong_order2_fast.py` → `step76_prolong_order2.{json,pkl}`, exact Fractions; `step76_order2_quadric_analysis.py` → `step76_order2_quadric.json`). Flat linearization: \(L_0\) rank 10; \(\ker L_0\) of dimension 50, of which 35 are Hamiltonian gauge (quartic Hamiltonians), leaving 15 physical 2-jet parameters (plus the affine \(\lambda\)-shift). The linear torsion map on these 15 has rank 10: every first-order kernel jet \((c,S,A)\) of 75.H/75.I is realized, and the 5-dimensional torsion-free part is the Kähler–Einstein 2-jet. \(L_2\) is \(100\times210\) of rank 83; its cokernel (17) contains the 16 flat Bianchi relations and exactly **one** further functional. Applied to \(\mathcal E_2\) it gives a quadratic form in the 2-jet, \(\lambda\)-independent, vanishing on the torsion-free part and on cross terms (\(\sim10^{-14}\)), and diagonal in jet coordinates (\(w=(a_1+ia_2,a_3+ia_4)\), \(f=cz+(S+A)\bar z\)):
\[
\mathcal Q=32|c|^2+4\|S\|^2-4\|A\|^2 .
\]
Independent checks: direct exact evaluation at a random integer point (\(-773\) predicted and found), unchanged after adding a quartic-Hamiltonian gauge term.

**Theorem 76.Z.** Let \((g,J)\) be an almost-Kähler Einstein metric (any \(\lambda\)) and \(p\) a torsion zero with linear torsion jet \(f=cz+(S+A)\bar z\). Then
\[
\|A\|^2=\|S\|^2+8|c|^2,\qquad \det\nolimits_{\mathbb R}Df=9|c|^4+|\det B|^2\ \ge\ 25|c|^4\ \ge0 .
\]
Hence every nondegenerate torsion zero has index \(+1\); pure \(c\)-, \(S\)- and \(A\)-jets are excluded; a nonzero first jet forces \(W_3^+(p)\neq0\); and \(W_3^+(p)=0\) forces \(\nabla^2\Omega(p)=0\).

*Proof.* A01 Theorem 62.A (`Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md`) proves invariantly, from Derdziński's Weitzenböck formula for \(W^+\) and \(\nabla^*\nabla q(p)=-2|\nabla^2\Omega|^2\), that \(|\nabla^2\Omega|^2=4\operatorname{tr}V^2-12|\eta|^2\) at a torsion zero; in the jet parametrization this is \(\|A\|^2=8|c|^2+\|S\|^2\), which is the quadric \(\mathcal Q=0\) found here in a different gauge. Substituting \(t=\|S\|^2-\|A\|^2=-8|c|^2\) into (75.5) gives \(9|c|^4+|\det B|^2\); A01's estimate \(|\det B|\ge|a|^2-|\det S|\ge4|c|^2\) gives the bound \(25|c|^4\) (our sampled minimum of \(\det/|c|^4\) on the cone: 25.003). \(\square\)

Numerics: 1457 random cone points all have positive determinant (minimum normalized value \(9.6\times10^{-5}\)); off the cone 14.7% of random first-order kernel jets have index \(-1\). Degenerate first-order zeros on the cone: \(c=0\), \(S\) with equal singular values, \(\det S=-a^2\); the Gibbons–Hawking Ricci-flat strictly AK jets are of exactly this type (A01).

**Scope.** 76.Z is compatible with the forced positive charge \(5\chi+6\tau>0\); it does not prove closed negative Goldberg. The closed question is now whether the formal variety of AKE germs with a torsion zero is nonempty beyond order 2 (Steps 77–78 note).
