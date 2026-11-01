# Step 47 — O10: the Taub–NUT core is free at the energy scale; the nut phase is priced only at derivative level

Session S1003A01, Agent2, Execute.  Scripts and data:

- `workspace/scripts/step47_tn_core_exact.py` → `workspace/data/step47/tn_core_exact.json` (exact symbolic: two-form types, Hessians, per-core integrals, determinant mismatch);
- `workspace/scripts/step47_sd_check.py` (orthonormal-frame (anti)self-duality check, printed output only);
- `workspace/scripts/step47_tn_core_split.py` → `workspace/data/step47/tn_core_split.json` (type split of the torsion Hessian, quadrature).

Conventions: Ricci-flat TN in Gibbons–Hawking form
\[
 g=V(dr^2+r^2d\theta^2+r^2\sin^2\theta\,d\varphi^2)+V^{-1}\eta^2,\qquad V=1+\ell/r,\quad \eta=d\psi+\ell\cos\theta\,d\varphi,
\]
\(\psi\)-period \(4\pi\ell\), orientation \(dr\,d\theta\,d\varphi\,d\psi\).  In this orientation the hyperkähler forms are self-dual (\(W^+=0\)), as in Steps 45–46.  The actual O10 equations are those of the corpus (`Curvature_Realizability.tex`, eq. finite-density-actual-equations): \(s=-4\), \(D_A^+\Phi=0\), \(F_A^+=2i\sigma(\Phi)\), \(\nabla_A^*\nabla_A\Phi=(1-\rho/2)\Phi\), cubic torsion \(t_\Phi=\sum_ic(e^i)\Phi\otimes(\Phi\wedge\nabla_i\Phi)\in E=S^-\otimes L\) with determinant connection \(3A\), \(\rho_*=4/3\), \(m_*=128/81\), \(a=\sqrt2/3\), \(\kappa_*^2=m_*/(4\rho_*^3)=1/6\).

This Step answers the decisive negative-spinor question posed at the end of Step 46.  The answer reverses that Step's §5: there is **no** local order-\(L^6\) payment in the resolvent, Dirac, determinant or \(L^2\)-current residuals of a TN core.  The core is detected only at derivative level, and the precise missing density-free estimate is identified.

## 1. The raw-TN resolvent mismatch is the omitted Weitzenböck curvature, not an obstruction

For the twisted Dirac operator on \(E=S^-\otimes L\) (determinant connection \(3A\)), with \(D^2=\nabla^*\nabla+\frac s4+\frac12c(F)\),
\[
 \boxed{(\mathcal L_{3A}-2)t=D^{-*}_{3A}D^-_{3A}t-\Bigl(1+\tfrac12c(F^-_{3A})\Bigr)t\qquad(s\equiv-4).}\tag{1.1}
\]
This is an exact pointwise identity on every metric of scalar curvature \(-4\) and every section.  It is the corpus identity \((\mathcal L-2)t=D^*Dt+(\Gamma-1)t-\mathcal Rt\) with \(\Gamma-\mathcal R=-\tfrac12c(F^-_{3A})=-\tfrac32c(F_A^-)\).  For an actual solution, the corpus' Proposition 7 gives exactly
\[
 D^-_{3A}t_\Phi=-4\delta+\mathcal K(W^+),\qquad \delta:=\sum_iP_i\otimes(\Phi\wedge P_i),\quad P_i=\nabla_i^A\Phi,\tag{1.2}
\]
with \(\mathcal K=0\) when \(W^+=0\) (TN, TNAdS).  Writing \(P_i=\alpha_iu+\beta_iu^\perp\), \(u=\Phi/|\Phi|\), one has \(\delta=\sqrt\rho\,[(\alpha\cdot\beta)u+(\beta\cdot\beta)u^\perp]\) with the complex-bilinear dot over frame indices.  Hence on a \(W^+=0\), \(s=-4\) block, the full resolvent residual of \(v:=t_\Phi\) is
\[
 q=(\mathcal L_{3A}-2)t_\Phi=-4D^{-*}\delta+(\Gamma-1)t_\Phi .\tag{1.3}
\]
On the Ricci-flat tangent one has \(s=0\) and \(F_A=0\) after blow-up, so the bracket in (1.1) is \(-1+1\cdot0\) relative to the needed \(-2\).  The Step-46 value \(q_{\rm TN}=-2v\), and the resulting bound \(\|q\|^2\ge16\pi^2m_*L^6\), is exactly the term \(-(s/4)-\frac12c(F^-_{3A})=2\) missing from a curvature-free model.  It is supplied identically by the physical scalar curvature and the actual determinant curvature.  **Step 46 (5.2)–(5.4) is withdrawn as a candidate payment.**  What remains to evaluate are \(\delta\) and \(\Gamma-1\).

## 2. Exact core data

**Spinor and torsion.**  Choose the parallel hyperkähler frame \((e_1,e_2)\) of \(S^+\) with \(e_2\leftrightarrow\Lambda^{0,2}_{I_3}\).  Here \(T^{1,0}_{I_3}=\operatorname{span}(e_{x_1}-ie_{x_2},\,e_{x_3}-ie_4)\); `tn_core_split.json` confirms \(\operatorname{Hess}\bar f(Z,\cdot)=0\) for both to \(10^{-32}\).  Set \(f=x_1+ix_2\), which is \(I_3\)-holomorphic, and
\[
 \Phi_{\rm TN}=\sqrt{\rho_*}\,e_1+a\bar f e_2 .
\]
Since \(d\bar f\in\Lambda^{0,1}_{I_3}\), the Clifford product \(c(d\bar f)e_2\) vanishes and \(D\Phi_{\rm TN}=0\).  Since \(\bar f\) is harmonic on GH, \(\nabla^*\nabla\Phi_{\rm TN}=0\).  Moreover \(\Phi\wedge P_i=\sqrt{\rho_*}a\,\partial_i\bar f\,e_1\wedge e_2\), so
\[
 \delta_{\rm TN}=\sqrt{\rho_*}\,a^2\langle d\bar f,d\bar f\rangle_{\mathbb C}\,e_2=0\quad\text{exactly},
\]
because the GH base is conformally flat (\(|dx_1|^2=|dx_2|^2\), \(\langle dx_1,dx_2\rangle=0\)).  The cubic torsion is exactly
\[
 \boxed{t_{\Phi_{\rm TN}}=\sqrt2\,\rho_*a\,d\bar f\in\Lambda^{0,1}_{I_3}\cong S^-,\qquad |t|^2=m_*/V,\quad D^-t=0 .}\tag{2.1}
\]
The torsion field is therefore an exact antiholomorphic differential.  The Step-46 torsion parent \(L\chi_1\) is precisely the restriction of the macroscopic endpoint jet \(P=t\theta_1\otimes e_2\), \(t^2=2/9\), since \(d\bar f=V^{-1/2}\theta_1\).  The TN core only modulates that jet by \(V^{-1/2}\).

**Determinant curvature.**  The two Gibbons–Hawking families of invariant 2-forms are
\[
 \beta^{\pm}_h=\eta\wedge dh\mp V*_3dh .
\]
The family \(\beta^{+}\) is self-dual and closed iff \(\Delta_{\mathbb R^3}h=0\); it contains the hyperkähler forms.  The family \(\beta^{-}\) is anti-self-dual and closed iff \(\operatorname{div}(V^2\nabla h)=0\).  This is checked symbolically for \(h=x_3,\ x_3/V,\ x_1\).  The endpoint ASD direction \(\Omega_-=\beta^-_{x_3}\) is **not** closed on TN.  Its exact closed continuation is
\[
 \boxed{h=\frac{x_3}{V}=\frac{x_3\,r}{r+\ell},\qquad \operatorname{div}(V^2\nabla(x_3/V))=\partial_3V-\partial_3V-x_3\Delta V=0 .}\tag{2.2}
\]
Hence
\[
 F_A^{\rm core}=i\Bigl(\tfrac23\,\omega_3+\tfrac13\,\beta^-_{x_3/V}\Bigr)
\]
is closed and has self-dual part \(2i\sigma(\sqrt{\rho_*}e_1)\).  It tends to the endpoint value \(e^{12}+\frac13e^{34}\) and its ASD part vanishes at the nut.  The exact mismatch is
\[
 \int_{B_R}\bigl|\beta^-_{x_3/V}-\beta^-_{x_3}\bigr|^2=\frac{64\pi^2}{3}\ell^3R+O(\ell^4\log),\qquad
 \int_{B_R}|(\Gamma-1)t|^2\le\frac{32\pi^2}{3}m_*\ell^3R,\tag{2.3}
\]
using \(|c(\beta)|_{\rm op}=\sqrt2|\beta|\) on \(S^-\).  With the flux radius \(R\asymp L=\ell^{1/3}\), this is \(O(L^{10})\).

**Residual count on the physical block.**  Embed the core in a background solution whose first jet is the null endpoint jet.  This means \(\delta_{\rm bg}=0\) to the order used.  The background is a hypothesis here; see §4.  The core changes \(P\) by the factor \(V^{-1/2}-1=O(\ell/r)\) and changes \(F^-\) by (2.3).  Hence, on \(B_L\),
\[
 \|D^{-*}\delta\|_2^2=O(\ell^3L),\qquad \|(\Gamma-1)t\|_2^2=O(\ell^3L),\qquad \|D^-t\|_2^2=O(\ell^3L).
\]
For the \((1,0)_{J_+}\) current \(N_\tau=(\nabla t)^{1,0}_{J_+}\) see §3: \(\|N_\tau\|_2^2=\frac{16\pi^2}9m_*\ell^3L(1+o(1))\).  Every one of these is \(o(L^6)\).  TNAdS corrections are relatively \(O(L^2)\) on the block.  **The nut core is free at the energy scale.**  The exact energy–mass–flux identity of Steps 45–46 then holds with \(q\)-pairing \(o(L^6)\).  In particular the Wigner–Seitz balance is a genuine balance of the corrected block, provided the background supplies the energy deficit discussed in §4.

## 3. What does detect a nut: derivative-level and scale-invariant integrals

Exact per-core integrals on TN are listed below (\(\tau=t_{\Phi_{\rm TN}}\), \(\ell\) arbitrary).  They are recorded in `tn_core_exact.json` and `tn_core_split.json`.

| quantity | per core | scaling |
|---|---|---|
| \(\int|\nabla\tau|^2\) | \(8\pi^2m_*\ell^2\,(R/(R+\ell))^2\) | critical (\(\propto\ell^2\)) |
| \(\int|\nabla^2_A\Phi|^2\) | \(\frac{32\pi^2}{9}\ell^2\) | critical |
| \(\int|dm|^2\) | \(\frac{16\pi^2}{3}m_*^2\ell^2\) | critical |
| \(\int|\nabla_{\bar Z_1}\tau|^2=\int|\nabla_{\bar Z_2}\tau|^2\) | \(8\pi^2m_*\ell^2\) (each equals the full energy; \(|\bar Z|^2=2\)) | critical |
| \(\int\kappa^2|\nabla_{\bar Z_1}\tau|^2\), \(\kappa^2=m/(4\rho_*^3)\) | \(\frac{1024\pi^2}{729}\ell^2=E_{\rm core}/9\) | critical |
| \(\int|N_\tau|^2\) on \(B_R\) | \(\frac{16\pi^2}9m_*\ell^3R\) | subcritical |
| \(\int|W^-|^2\) | \(8\pi^2\) | scale-invariant |
| \(\int|\nabla\tau|^4\) | \(\frac{8\pi^2}{15}m_*^2=\frac{m_*^2}{15}\int|W^-|^2\) | scale-invariant |
| \(\int|\nabla^2\tau|^2\) | \(\frac{16\pi^2}{5}m_*=\frac{2m_*}{5}\int|W^-|^2\) | scale-invariant |
| \(\int|\nabla^3_A\Phi|^2\) | \(\frac{64\pi^2}{45}\) | scale-invariant |

The pointwise data behind the table are \(|\operatorname{Hess}\bar f|^2=2\ell^2/(r+\ell)^4\) and \(|\nabla\operatorname{Hess}\bar f|^2=12\ell^2r/(r+\ell)^7\).

**The current \(N_\tau\).**  The SW field selects \(J_+=J(u)\), \(u=\Phi/|\Phi|\).  For \(\Phi_{\rm TN}\), \(u\) is rotated from \(e_1\) by the angle \(s\) with \(\tan s=a|f|/\sqrt{\rho_*}\).  Hence \(J_+=\cos2s\,I_3+\sin2s\,K\), where \(K\) is a parallel complex structure anticommuting with \(I_3\).  Since \(\nabla\tau\) has its derivative index entirely in \(\Lambda^{0,1}_{I_3}\), and \(\xi\perp K\xi\) with \(|K\xi|=|\xi|\), the \((1,0)_{J_+}\)-projector gives exactly
\[
 \boxed{|N_\tau|^2=\sin^2 s\,|\nabla\tau|^2=\frac{a^2|f|^2}{\rho_*+a^2|f|^2}\,|\nabla\tau|^2 ,}\tag{3.1}
\]
independent of the phase convention for \(K\).  Thus \(N_\tau=O(\kappa_*\ell/r)\) in \(\ell\ll r\ll1\).  This is \(L^2\)-small, as stated in the table, but \(|\nabla N_\tau|\asymp\kappa_*\ell/r^2\) is critical.

**Mechanism.**  The core is holomorphic for the integrable hyperkähler \(I_3\), while the actual field selects the rotating, non-integrable \(J_+\) whose Nijenhuis rate is \(\kappa\) (corpus eq. (3.7), \([Z_1,Z_2]\equiv-2\kappa\bar Z_1\)).  The commutator identity (corpus (3.8)),
\[
 2\kappa B=F^E(Z_1,Z_2)\tau-\nabla_{Z_1}A_2+\nabla_{Z_2}A_1+\textstyle\sum_iL_iA_i,\qquad A_i=\nabla_{Z_i}\tau,\ B=\nabla_{\bar Z_1}\tau,
\]
has \(F^E(Z_1,Z_2)=0\) on Einstein metrics with type-\((1,1)\) determinant curvature.  The reason is that \(Z_1\wedge Z_2\in\Lambda^+\otimes\mathbb C\), the \(\Lambda^+\to\operatorname{End}S^-\) block is \(\operatorname{Ric}^\circ\), and \(F_A^\pm\) are \((1,1)\) for \(J_+\).  Wherever this identity holds with its stated hypotheses, it forces
\[
 \|\nabla N_\tau\|_{L^2(\rm core)}\gtrsim\|\kappa B\|_{L^2}-C\|N_\tau\|_{L^2},\qquad
 \int_{\rm core}\kappa^2|B|^2=\frac{E_{\rm core}}9 .\tag{3.2}
\]
Each core therefore carries a forced current-gradient energy comparable to a fixed fraction of its own energy.  The sharp numerical constant needs the corpus Clifford/sign conventions to fix the rotation axis of \(K\); it is not claimed here.

## 4. Consequences for density-free O10

1. **No local payment.**  Combined with Step 46's Stokes argument, the admissible object is a finite block or explicit compensators, not a periodic one-nut cell.  Such a block of TN type, inserted into a null endpoint background, meets all residual targets (6.3)–(6.3a) of Step 46 at \(o(L^6)\), with the \(L^2\)-current small.  The local field-extension problem has no order-\(L^6\) cokernel at the energy scale.  The remaining payments are global: degree transport or compensators (Step 46 §6), and the background energy deficit.

2. **Background deficit.**  The core's own radial and horizontal energies close the corpus identity \(2\int E_1+3\int E_2+4\int m^2|c|^2=4\int m^2\) on its Wigner–Seitz cell exactly.  With angular averages \(E_1=\frac23|dm|^2\) and \(E_2=\frac13|dm|^2\) one gets
\[
 \tfrac{112}{9}+\tfrac{48}{9}-\tfrac{16}{9}=16 \quad(\text{units } \pi^2m_*^2\ell^2).
\]
Between cores \(c\to0\).  A nut phase is therefore a **\(c\)-depleted phase** (\(c\approx0\), energy in radial bubbles).  The calibrated endpoint phase is instead uniform with \(|c|=1\).  These are two distinct macroscopic states at the same \((\rho_*,m_*)\).  The finite-density theorem excludes the bubble-free one.  Whether the \(c\)-depleted macroscopic coframe (\(c=d=0\) on average, \(\kappa=1/\sqrt6\), with homogenized core sources \(\langle d^2\rangle\) in corpus (5)–(6)) is integrable with \(\operatorname{Ric}=-g\) is the macroscopic question.  It is a well-posed exterior-differential-system computation and has not yet been done.

3. **Finite-density bounds fail exactly in proportion to Euler density.**  By the table, \(\int|\nabla\tau|^4=\frac{m_*^2}{15}\int_{\rm cores}|W^-|^2\) and \(\int|\nabla^2\tau|^2=\frac{2m_*}5\int_{\rm cores}|W^-|^2\).  With \(N_{\rm cores}\asymp\theta V/(4\pi^2\ell^2)\) these are \(\asymp V/\ell^2\).  The finite-density bounds \(\|\nabla v\|_4+\|\nabla^2v\|_2\le C_B\) are exactly what a nut phase violates.  No density-free argument may use them.

4. **The precise missing estimate.**  By (3.1)–(3.2), a nut phase of fraction \(\theta\) has normalized current gradient
\[
 \fint|\nabla N_\tau|^2\gtrsim\theta\,\frac{2m_*}{9}
\]
(up to the convention constant).  This is bounded, not divergent, while \(\fint|N_\tau|^2\to0\) consistently with the corpus' strong-current upgrade.  Conversely, if \(N_\tau\to0\) in normalized \(H^1\) on \(\{\rho\ge c\}\), corpus (3.8) yields \(\kappa B\to0\) in \(L^2\) with all product terms controlled.  This discharges the weak proof obligation recorded in the corpus at the end of the phase-curvature section.  The corpus' component argument (\(\alpha=\theta=0\Rightarrow dm=0\)) then removes the radial variables needed to reach the fifth-line CR equation.  **Conditional reduction:** density-free O10 along every nut-type escape follows from a density-free proof that \(\|\nabla N_\tau\|_{2,\rm av}\to0\).  Whether the remaining steps of the finite-density argument go through after this input, without \(W^-\) control, must still be checked line by line.  Such an estimate is a third-derivative statement about \(\Phi\) restricted to the \(J_+\)-\((1,0)\) block.  It is critical rather than supercritical in the nut phase, so it is not excluded by scaling.

## 5. Status

Established (exact, this Step):

- the Weitzenböck identity (1.1) and its consequence (1.3), withdrawing Step 46 §5 as an obstruction;
- the exact TN data (2.1)–(2.2), including \(\delta\equiv0\) and the closed ASD determinant continuation \(h=x_3/V\);
- the per-core integrals in the table;
- the current formula (3.1).

Conditional:

- the \(o(L^6)\) residual count assumes a null background jet;
- the lower bound (3.2) assumes corpus (3.8) with its closure hypotheses on the physical block;
- the reduction in §4.4 requires re-checking the downstream finite-density steps.

Open: the integrability of the \(c\)-depleted macroscopic phase, degree transport or compensators, and a density-free \(H^1\) estimate for \(N_\tau\).  O11 results are unchanged (certified coefficient below 3.9961512).
