# Step 75 — Q4 (closed negative Goldberg): the half-twistor structure of almost-Kähler torsion, the index of torsion zeros, and what any closed proof must use

Agent2, Execute. Inputs: Spirit #91; A01 Steps 53/59 (`Sessions/S1003A01/workspace/notes/step53_goldberg_jets_and_canonical_form.md`, `step59_chiral_completion_and_zero_charge.md`); AAD local rigidity \cite{apostolovmath} and AAD local models (Knowledge objects `Local-rigidity-of-certain-classes-of-almost-Kahler-4-manifolds--c0d51aa8ffb7`, `Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a`, eqs. (16), (21)–(26) and Lemma 2 there); package §21.5 (63.AK). Script `workspace/scripts/step75_torsion_symbol_checks.py` → `workspace/data/step75_torsion_symbol_checks.json`.

Labels: [P] proved here, [K] cited, [N] numerical/symbolic check, [O] open.

## 0. Setting

\((M^4,g,J,\Omega)\) almost-Kähler, \(|\Omega|^2=2\). With a gauge \(\phi\in[\![\Lambda^{0,2}]\!]\), \(|\phi|^2=2\) (AAD):
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\qquad
\nabla\phi=-a\otimes\Omega+b\otimes J\phi,\qquad |\nabla\Omega|^2=4|a|^2,
\]
gauge change \(\phi'=\cos\theta\,\phi+\sin\theta\,J\phi\): \(a'=\cos\theta\,a-\sin\theta\,Ja\), \(b'=b+d\theta\). The Ricci identity for \(\Omega\) is (AAD (26))
\[
da-Ja\wedge b=-R(J\phi),\qquad d(Ja)+a\wedge b=-R(\phi),                         \tag{75.1}
\]
with \(R\) the curvature operator on \(\Lambda^2\). Put \(\alpha:=a+iJa\) (a \((1,0)\)-form in AAD's convention; \(J\alpha=-i\alpha\)); under a gauge change \(\alpha'=e^{i\theta}\alpha\), so \(\alpha\) is a section of \(\Lambda^{1,0}\otimes\mathcal L\) for the Hermitian line bundle \(\mathcal L\) with connection \(-ib\), and \(\alpha\otimes(\cdot)\) is the complex form of the torsion \(T=\nabla\Omega\in E=[\![\Lambda^{0,1}\otimes\Lambda^{0,2}]\!]\). Combining (75.1),
\[
d_b\alpha:=d\alpha-ib\wedge\alpha=-R(J\phi+i\phi).                                 \tag{75.2}
\]

## 1. The half-twistor theorem [P]

Decompose the right side of (75.2) by the \(U(2)\)-splitting \(R=\tfrac s{12}+\widetilde{\rm Ric}_0'+\widetilde{\rm Ric}_0''+W_1^++W_2^++W_3^++W^-\) (AAD (3)), using that \(J\phi+i\phi\in[\![\Lambda^{0,2}]\!]\otimes\mathbb C\):

* \(\Lambda^-\)-part: only the Kulkarni–Nomizu block \(\Lambda^+\to\Lambda^-\) of \({\rm Ric}_0\) contributes, and on \([\![\Lambda^{0,2}]\!]\) this block is exactly the \(J\)-anti-invariant Ricci tensor \({\rm Ric}''\) (AAD: "projecting (12) on \(\Lambda^-\) determines the \(J\)-anti-invariant part of the Ricci tensor").
* \(\Omega\)-part: \(\langle W^+(J\phi+i\phi),\Omega\rangle\) = the \(W_2^+\) component (\(\Psi\) in AAD (5), \(\eta\) in A01).
* \([\![\Lambda^{0,2}]\!]\)-part: \(\bigl(\tfrac s{12}-\tfrac\kappa{12}\bigr)(J\phi+i\phi)+W_3^+(J\phi+i\phi)\), and \(\kappa-s=6|a|^2\) (AAD (10)); the complex-linear piece is \(-\tfrac12|a|^2(J\phi+i\phi)\), quadratic in the torsion, while \(W_3^+\) (complex-antilinear on \([\![\Lambda^{0,2}]\!]\)) gives the other type.

**Theorem 75.H.** For every almost-Kähler 4-manifold:

(a) \((d_b\alpha)^-=-\tfrac12\widetilde{\rm Ric}''(J\phi+i\phi)\) (raw Kulkarni–Nomizu extension \(\widetilde{\rm Ric}''\); factor \(-\tfrac12\) fixed by the Step-76 verifier). Hence \({\rm Ric}''=0\) (the Blair–Ianus class, in particular every almost-Kähler Einstein metric) iff
\[
\mathcal P\alpha:=\bigl(\text{primitive }(1,1)\text{-part of }d_b\alpha\bigr)=0 .                 \tag{75.3}
\]
(b) \(\mathcal P\) has injective principal symbol: \(\sigma_\xi(\mathcal P)\alpha=(\xi'\wedge\alpha)_0\) with \(\xi'\) the component of \(\xi\) of type opposite to \(\alpha\); \(\xi'\wedge\alpha\) is decomposable and nonzero, while \(\Omega\) is nondegenerate, so its primitive part never vanishes. Thus (75.3) is an overdetermined elliptic first-order system (3 complex equations, 2 complex unknowns).

(c) The full gradient \(\nabla^b\alpha\in\Lambda^1\otimes\Lambda^{1,0}\otimes\mathcal L\) (complex rank 8) splits into **four** \(U(2)\)-irreducible pieces \(\Lambda^{1,1}_0\oplus\mathbb C\Omega\oplus\Lambda^{2,0}\oplus S^{2,0}\): primitive \((1,1)\) (rank 3) \(=\mathcal P\alpha\); \((1,1)\)-trace (rank 1) \(=W_2^+\) up to a universal constant; the same-type antisymmetric piece (rank 1) \(=W_3^+\), precisely \(\operatorname{Alt}(D\alpha)=-\tfrac12\langle\eta,u\rangle\Omega-W_3^+(u)-\tfrac12\widetilde{\rm Ric}''(u)\); and the symmetric piece \(S^{2,0}\) (rank 3), which no curvature component sees. The quadratic \(|a|^2u/2\) term is the \((0,2)\) Nijenhuis component of \(d\) and lies in the *opposite* type line; it is not part of the \(W_3^+\) summand (Step-76 verifier correction A.1/A.2). In spinor language \(\alpha\) is a twisted negative spinor (\(\Lambda^{0,1}\otimes\mathcal L'\)); its Dirac components are \((W_2^+,W_3^+)\), its twistor derivative splits under \(U(2)\) into \(\mathcal P\alpha\oplus S^2\alpha\), and \({\rm Ric}''=0\) kills exactly the first half.

(d) **Refined Kato.** If \({\rm Ric}''=0\), \(\nabla^b\alpha\) lies pointwise in the 5-dimensional complex kernel \(K=\ker\sigma(\mathcal P)\), so
\[
|d|\alpha||\le\tfrac{\sqrt3}{2}\,|\nabla^b\alpha|,                                          \tag{75.4}
\]
sharp: \(k^2=\sup_{|\xi|=|v|=1}|\pi_K(\xi\otimes v)|^2=\tfrac12+\tfrac14=\tfrac34\) (the \(\xi''\otimes v\) half lies in \(K\); of the \(\xi'\otimes v\) half only its trace, of norm\(^2\le\frac14\), does). [N]: sampled maximum 0.749997, attained value 0.75 at \(\xi=dx_1,\ v=e_1\); \(\dim_{\mathbb R}K=10\).

*Proof.* (a) is (75.2) projected to \(\Lambda^-\) together with the block identification. (b) symbol computation above. (c) is the representation count \(\Lambda^{1,0}\otimes\Lambda^{1,0}=S^2\oplus\Lambda^{2,0}\), \(\Lambda^{0,1}\otimes\Lambda^{1,0}=\mathbb C\Omega\oplus\Lambda^{1,1}_0\), with the identification of components read off (75.2) and AAD (13)–(15) (\(\Psi\) is built from the \(\Omega\)-components of \(da,d(Ja)\); \(\lambda,\mu\) and \(|a|^2\) from the \([\![\Lambda^{0,2}]\!]\)-components). (d) standard (Calderbank–Gauduchon–Herzlich) from \(\nabla^b\alpha\in K\). \(\square\)

Relation to A01. In a unitary frame at a point, \(\alpha\leftrightarrow (f_1,f_2)\) and (75.3) is A01's principal soldered system \(\partial_1f_2=\partial_2f_1=0,\ \partial_1f_1=\partial_2f_2\) (Step 59 §3). The new content here: the system is *exact* (not only principal) in the Hermitian gauge connection, its symbol is injective, it holds on the whole Blair–Ianus class (so the same equation governs the Einstein end and the aligned Einstein–Maxwell end of package §21.11), the free \(S^2\) part is identified, and the sharp Kato constant is \(3/4\).

## 2. The index of a nondegenerate torsion zero [P,N]

At a zero \(p\) with nondegenerate linear part, the kernel of \(\sigma(\mathcal P)\) gives, in A01's coordinates, \(f(z)=cz+B\bar z\) with \(c\in\mathbb C\) (the \((1,1)\)-trace, i.e. \(W_2^+(p)\) up to a constant) and \(B=S+A\in M_2(\mathbb C)\), \(A\) antisymmetric (\(\leftrightarrow W_3^+(p)\)), \(S\) symmetric (free). Writing the real Jacobian in \((z,\bar z)\) blocks,
\[
\det\nolimits_{\mathbb R}Df=\det\bigl(|c|^2I-\bar BB\bigr)=|c|^4-|c|^2\bigl(\|S\|^2-\|A\|^2\bigr)+|\det B|^2,         \tag{75.5}
\]
using \(\operatorname{tr}(\bar BB)=\|S\|^2-\|A\|^2\) for symmetric \(S\), antisymmetric \(A\). Hence:

**Proposition 75.I.** The local torsion index at a nondegenerate zero is \(\operatorname{sign}\bigl(|c|^4-|c|^2(\|S\|^2-\|A\|^2)+|\det B|^2\bigr)\). It is \(+1\) whenever \(W_2^+(p)=0\), or \(S=0\), or \(\|S\|\le\|A\|\). With \(t=\|S\|^2-\|A\|^2\), \(d=|\det B|\), \(x=|c|^2\): index \(-1\) holds iff \(t>2d\) strictly and \(x\) lies strictly between the roots \((t\pm\sqrt{t^2-4d^2})/2\) (Step-76 verifier correction). **Superseded at order 2:** by Theorem 76.Z the AKE equations force \(t=-8|c|^2\le0\) at every torsion zero, so index \(-1\) is excluded for AKE germs; the first-order statement above concerns only the unconstrained kernel of \(\sigma(\mathcal P)\). [N] 4000/4000 random agreements; pure modes \(c\)-only, \(A\)-only give \(+1\); A01's example \(f=(z_1+2\bar z_1,z_2)\) gives \(-1\).

Consequence for the closed problem. Positive charge \(5\chi+6\tau>0\) (A01 Step 59 §3, refining Armstrong–LeBrun's \(5\chi+6\tau=0\) for nowhere-vanishing \(N\), AAD Lemma 2) is consistent with zeros of either sign at first order (both signs occur on open subsets of the first-order kernel; the earlier word "generic" was misleading). So topology plus the exact first-order system admits the needed charge; no sign contradiction exists at this level. At order 2 only index \(+1\) survives (76.Z).

## 3. What the refined-Kato balance can and cannot give [P]

**(i) The Kato gain is spent on the exponent, not the sign.** For \(f=|\alpha|\) and \(\gamma<2\),
\[
\Delta f^\gamma\ \ge\ \gamma f^{\gamma-2}\Bigl[(1-(2-\gamma)k^2)|\nabla^b\alpha|^2-\langle\nabla^{b*}\nabla^b\alpha,\alpha\rangle\Bigr]
\qquad(\Delta=\textstyle\sum\partial_i^2),
\]
and with \(k^2=3/4\) the gradient term vanishes at \(\gamma=2/3\): \(\Delta|\alpha|^{2/3}\ge-\tfrac23|\alpha|^{-4/3}\langle\nabla^{b*}\nabla^b\alpha,\alpha\rangle\). The verified rough-Laplacian identity (Step-76 verifier; the earlier \(-\tfrac s4\) coefficient was unproved and is withdrawn) is
\[
\langle\nabla^*\nabla T,T\rangle=-\tfrac{3s}{4}\,q+2\langle\nabla\eta,T\rangle,\qquad \int\langle\nabla\eta,T\rangle=2\int|\eta|^2 .
\]
For \(s<0\) the zeroth-order term has Sekigawa's wrong sign; the Kato improvement does not touch it. The coupling to \(\nabla W^+\) is removed only after integration (δW⁺ = 0), where the singular weight \(|\alpha|^{-4/3}\) produces new cross terms.

**(ii) Norm-weighted Bochner arguments are index-blind.** Any weight \(F(|\alpha|)\) depends only on norm data near a zero; norm-only data cannot see \(\operatorname{sign}\det Df\) (\(|Lx|\) and \(|L'x|\) coincide for \(L'=L\circ r\), \(r\) a reflection). The explicit Laplacian formula stated here earlier was false (its delta coefficient depends on the singular values of \(L\)) and is withdrawn. Since the only topological information is the *signed* count \(\sum{\rm ind}=5\chi+6\tau\), such arguments cannot import the charge.

**(iii) Decay principle (no-go for smooth integral identities; conditional on a globally defined \(V\), a pointwise identity \(\operatorname{div}V=\Phi\), and decaying flux on the complete pair).** Let \(\int_M\operatorname{div}V=0\) be any identity with \(V\) a universal polynomial in the jets of \((g,\Omega)\) and the curvature, and let \(\Phi\ge0\) be a pointwise expression such that the identity reads \(\int\Phi=0\) on closed almost-Kähler Einstein manifolds. On A01's complete strictly almost-Kähler Einstein pair (\(\operatorname{Ric}=-3g\), \(W^-=0\), \(|\nabla\Omega|^2=36(1-x^2)^3/(1+3x^2)^3\), smooth bolt, ACH end; `Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md`), the same identity holds whenever the flux of \(V\) through the level sets of the radial coordinate tends to zero at the ACH end. Since that pair is strict, \(\Phi\) cannot force \(T\equiv0\). The verified vanishing of A01's AAD balance on the pair, \(\int(|\eta|^2+2|W_3^+|^2+\tfrac3{16}q^2-\tfrac32q)=0\), is an instance. Hence a closed negative Goldberg proof must use at least one of:
1. an orientation-sensitive zero-localized quantity: the Euler class of \(E\) (Chern–Weil / Mathai–Quillen with the torsion section, or the opposite structure \(I\) with \(c_1(I)=3c_1(J)\) off the zeros), whose flux need not decay on the complete pair (this concerns transgression flux, not finite \(c_2\) integrals);
2. a local theorem that no strict germ with \({\rm Ric}''=0\), \(s<0\) constant, has a torsion zero (then \(5\chi+6\tau>0\) closes the problem);
3. genuinely nonlocal input (compactness, Seiberg–Witten, moduli).

The flux condition in (iii) must still be checked for each specific \(V\) used (pointwise decay of \(q\), \(\eta\), \(W_3^+\) against the ACH area growth); this is a short computation on A01's exact data and is the only conditional point.

## 4. The sharp local question and how the index formula organizes it [O]

By §3, the cheapest decisive formulation of Q4 is the dichotomy of route 2: does a strictly almost-Kähler germ with \({\rm Ric}=\lambda g\), \(\lambda<0\), and an isolated (or any) torsion zero exist?

* If no such germ exists, closed negative Goldberg follows from \(5\chi+6\tau>0\).
* If such germs exist, a closed counterexample needs zeros of total signed index \(5\chi+6\tau\). By 75.I, positive-index linear zeros are the \(W_2^+(p)=0\) or \(\|S\|\le\|A\|\) jets, so the first prolongation should be run on the two positive pure modes:
  - the \(c\)-mode \(f=cz\) (\(W_2^+(p)\ne0\), \(S=A=0\));
  - the \(A\)-mode \(f=A\bar z\) (\(W_3^+(p)\ne0\), \(c=0\)).
  It should test whether the second-order Einstein/AAD compatibilities (δW⁺ = 0 in the \(\mathcal V^\pm\) components, AAD Lemma 3 type identities, the \(\nabla^2q=2\langle\nabla T,\nabla T\rangle\) relation) admit them. A01's Step 59 lists the same next calculation for \(P_1=cz\). The \(A\)-mode is new here and is the natural second test.
* At a zero of order \(\ge2\), A01 shows \(W_2^+(p)=W_3^+(p)=0\), so the pointwise \(W^+\) is of Kähler type there; the leading jet then lies in the family \(f_i=z_ih_{m-1}(\bar z)+g_i(\bar z)\), whose index is again given by the Jacobian of its homogeneous part.

## 5. Status

| Item | Status |
|---|---|
| 75.H(a)–(c): exact half-twistor equation on the Blair–Ianus class, injective symbol, four-piece splitting | [P] (verified Step-76 TTCS with the \(-\tfrac12\) factor) |
| 75.H(d): sharp refined Kato \(k^2=3/4\) | [P]+[N] |
| 75.I: index formula at nondegenerate zeros | [P]+[N] |
| §3(i)–(ii): Kato and weighted Bochner cannot change the sign or see the index | [P] |
| §3(iii): decay no-go | [P] modulo the flux check for each specific \(V\) on A01's exact pair |
| Local existence of negative AKE germs with torsion zeros | [O]; decisive. Order 2: only index \(+1\) nondegenerate zeros (76.Z). Orders 4–6: see `step77_78_Q4_higher_prolongation.md` |
