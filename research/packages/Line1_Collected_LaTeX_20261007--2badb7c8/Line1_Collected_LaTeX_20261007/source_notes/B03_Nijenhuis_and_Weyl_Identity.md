# Step 40 — The Nijenhuis form of the signed field cost, its Weyl form, and pointwise exhaustion at LeBrun's threshold

Session S1003A02, Agent2. Conventions are those of the simultaneous-field identity,
`Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex`
(Prop. *Simultaneous signed cost identity*, lines 319–447): \(s_g=-4\);
\(M=X\#k\overline{\mathbf{CP}}^2\#\ell(S^1\times S^3)\), \(Q=k+4\ell\); for each sign vector
\(\epsilon\) an actual solution \(D_{\mathcal A_\epsilon}\Phi_\epsilon=0\),
\(F^+_{\mathcal A_\epsilon}=2i\sigma(\Phi_\epsilon)\), \(\rho_\epsilon=|\Phi_\epsilon|^2\in[0,2]\),
\(\psi_\epsilon=2\sqrt2\sigma(\Phi_\epsilon)\) (so \(|\psi|=\rho\)),
\(W_{0,\epsilon}=\tfrac14(\rho^2 I/3-\psi\otimes\psi)\), \(\zeta=\langle\Phi,\nabla\Phi\rangle\),
\(M_\epsilon=W^+-W_{0,\epsilon}\). The field quantifiers are those verified in Step 39
(`trace/ttcs/results/step39_ttcs01_verifier{1,2}_integration.md`): fixed Spin\(^c\) structures
\(a_\epsilon=c+\sum\epsilon_iE_i\); for \(b^+\ge2\) chamber-independent nonzero invariants give
unperturbed solutions for every metric by LeBrun's limiting argument; when \(A-k>0\) every
solution is irreducible; the formula is applied to the scalar \(-4\) Yamabe representative
\(\hat g\) and \(P(g)\ge P(\hat g)\); handle summands need the higher-type supplier. Below,
"saving" means \(\mathfrak S:=8\pi^2Q-P\), and
\[
\mathcal W:=2\|f_\varnothing^-\|^2+2\sum_{I\neq\varnothing}\|f_I^+\|^2\ \ge0
\]
is the Walsh part of \(\mathscr A\). Starting identity (proved in the paper and rechecked in
Step 37/39):
\[
P-8\pi^2Q=\mathcal W+\mathbb E_\epsilon\Big[8\|\zeta\|^2+4\|M\|^2+\int b(\rho)(\rho-2)^2\Big]
-4\,\mathbb E_\epsilon K_\epsilon,\qquad K_\epsilon=\int|\nabla\Phi_\epsilon|^2 .
\tag{0}
\]

## 1. Pointwise anatomy of a monopole first jet

On \(\{\rho>0\}\) (complement of a null set by unique continuation) write
\(\Phi=\sqrt\rho\,u\), \(|u|=1\), \(\nabla_{\mathcal A}u=i\beta u+v\,u^\perp\) with \(\beta\) a real
1-form and \(v\in T^*\otimes\mathbf C\). Put \(a=d\sqrt\rho\), \(b=\sqrt\rho\,\beta\). Then
\[
|\nabla\Phi|^2=|a|^2+|b|^2+\rho|v|^2,\qquad |\zeta|^2=\rho(|a|^2+|b|^2),\qquad
|\nabla n|^2=4|v|^2,
\]
where \(n=\psi/\rho\) is the unit Bloch (almost-complex) direction of \(\Phi\).

**Lemma 1 (Dirac pins the Lee form; it never sees the Nijenhuis tensor).** Let
\(c(v)=\sum_ie_i\cdot(v_iu^\perp)\in S^-\). Then (i) \(cc^*=2\,\mathrm{Id}_{S^-}\);
(ii) \(\ker c\) equals the space of first jets of \(u\) for which the Bloch form satisfies
\(d\omega=0\) at the point, i.e. the Gray–Hervella almost-Kähler component \(\mathcal W_2\)
(equivalently the Nijenhuis component of \(\nabla J_n\)); its orthogonal complement is the Lee
component \(\mathcal W_4\); (iii) \((a+ib)\cdot u=(a+J'b)\cdot u\) for an orthogonal complex
structure \(J'\) and \(|(a+J'b)\cdot u|=|a+J'b|\). Writing \(v=v_2+v_4\), the equation
\(D_{\mathcal A}\Phi=(a+ib)\cdot u+\sqrt\rho\,c(v)=0\) is therefore equivalent to
\[
\rho|v_4|^2=\tfrac12|a+J'b|^2,\qquad v_2\ \text{unconstrained}.
\]
*Proof.* (i): \(c\) is \(U(2)\)-equivariant onto the irreducible real module \(S^-\);
\(\operatorname{tr}cc^*=4\cdot2\). (ii): both kernels are 4-dimensional; Taubes' canonical-spinor
identity \(D_{A_0}u_0=0\) for almost-Kähler \(\omega\) is pointwise algebraic in the first jet, so
\(\mathcal W_2\subset\ker c\). (iii) is Clifford linearity. All three were checked numerically at
random spinors (residuals \(\le4\times10^{-15}\); principal angles between the two kernels all
zero): `workspace/scripts/step40_nijenhuis_tariff_check.py`,
`workspace/data/step40_nijenhuis_tariff_check.json`. \(\square\)

Thus \(|\nabla n|^2_{\mathcal W_2}:=4|v_2|^2\) is the Nijenhuis (integrability-obstructing)
energy of the SW-selected almost-complex structure \(J_\epsilon\), and the Lee part of its
rotation is not free: it costs \(\zeta\).

## 2. Theorem N (Nijenhuis form of the saving)

The pointwise Weitzenböck formula for an actual solution at \(s=-4\) is
\(\tfrac12\Delta\rho+|\nabla\Phi|^2=\tfrac12\rho(2-\rho)\) (\(\Delta=d^*d\)); its integral is the
recorded \(K_\epsilon=\frac12\int\rho(2-\rho)\). Multiplying by \(\psi(\rho)=2\rho\) and
integrating gives \(\int2\rho|\nabla\Phi|^2+4\int\rho|a|^2=\int\rho^2(2-\rho)\). Adding
this zero to (0) after substituting \(K=\frac12\int\rho(2-\rho)\):

**Theorem N.** Under the quantifiers above,
\[
\boxed{\;
\mathfrak S\;=\;\frac12\mathbb E_\epsilon\!\int\rho_\epsilon^2|\nabla n_\epsilon|^2_{\mathcal W_2}
-\mathbb E_\epsilon\!\int\frac{(2-\rho)^2(2+2\rho-\rho^2)}6
-\mathbb E_\epsilon\!\int\rho\bigl(|a|^2+5|b|^2-2\langle a,J'b\rangle\bigr)
-4\mathbb E_\epsilon\|M_\epsilon\|^2-\mathcal W\; }
\]
Every subtracted term is nonnegative: \(2+2\rho-\rho^2>0\) on \([0,2]\); the quadratic form
\(\begin{psmallmatrix}1&-1\\-1&5\end{psmallmatrix}\) has determinant 4. Inputs:
\(m(\rho)-\rho^2(2-\rho)=-(2-\rho)^2(2+2\rho-\rho^2)/6\) with
\(m=(2-\rho)(-\rho^3+10\rho^2-2\rho-4)/6\), and the coefficient matrix
\(\begin{psmallmatrix}-\rho&\rho\\ \rho&-5\rho\end{psmallmatrix}\) (both in the JSON).

**Corollaries.**
1. *Hermitian tariff.* If, for a scalar \(-4\) metric, some simultaneous choice of the
   \(2^k\) solutions has Bloch structures \(J_\epsilon\) integrable on \(\{\Phi_\epsilon\ne0\}\),
   then \(P\ge8\pi^2Q\). This contains the scalar \(-4\) Kähler instance and every
   scalar \(-4\) metric whose monopole structures are Hermitian, Kähler or not. It does not by
   itself reproduce the Step-38 theorem for arbitrary Kähler metrics, because Yamabe
   normalization generally destroys Kählerness (Step 38 used Hodge index directly).
2. *Necessary condition on near-minimizers.* If \(P/(8\pi^2k)\to c<1\) (pure blow-ups), then
   \(\mathbb E_\epsilon\int\rho^2|\nabla n_\epsilon|^2_{\mathcal W_2}\ge16\pi^2(1-c)k\): the
   monopole almost-complex structures are non-integrable, with Nijenhuis energy at least
   \(16\pi^2(1-c)\) per class. For a closed replica of the certified \(X=128\) cell,
   \(1-c\in[0.0043372672289,0.0043372672468]\), i.e. asymptotically at least \(0.684914\)
   per class (an \(o(k)\) error is retained at finite \(k\)).
3. *Scale law* (for geometrically controlled regions of bounded multiplicity). Since the weight is \(\rho^2\le4\), rotation of \(J_\epsilon\) by a fixed angle
   across a region of diameter \(r\) buys at most \(O(r^2)\). Saving bounded away from zero per
   class requires the monopole almost-complex structure to rotate non-integrably across
   unit-size regions in the \(s=-4\) normalization. This is the precise field-side form of the
   observed hierarchy: Burns cells of scale \(\sqrt{x_0}\) are first-order neutral in
   \(\ker\mathbf R^+\), the second-order gain is \(x_0^2\log\), and the certified cell saves
   \(0.43\%\).
4. *Agreement with the almost-Kähler identity.* A01's identity has the single negative term
   \(-\tfrac32N\) (Nijenhuis); Theorem N shows that the same channel is the only free saving
   mode of the whole monopole family. The Lee component of \(\nabla J\), which in the
   Step-37 decomposition was mixed into \(\rho|\nabla n|^2\), is now shown to be paid by
   \(\zeta\).

## 3. Theorem W (Weyl form): rotation is Weyl deletion along the monopole direction

For the self-dual form \(\psi\), the Weitzenböck formula
\(\nabla^*\nabla\psi=\Delta_H\psi+2W^+\psi-\tfrac s3\psi\) integrates to
\(\int|\nabla\psi|^2=2\|d\psi\|^2+2\int(W^+-W_0)(\psi,\psi)+\int\tfrac{\rho^2}3(4-\rho^2)\),
using \(\|d^*\psi\|=\|d\psi\|\), \(W_0\psi=-\rho^2\psi/6\), \(s=-4\). With
\(|\nabla\psi|^2=4\rho|a|^2+4\rho^2|v_2|^2+2\rho|a+J'b|^2\) and, under the Dirac equation,
\(|d\psi|^2=2\rho|b|^2\) (the \(\mathcal W_2\) part lies in \(\ker d\); checked numerically, form
eigenvalues \(\{0^4,2^4\}\)), substitution into Theorem N gives, with
\(x_\epsilon=M_\epsilon(n_\epsilon,n_\epsilon)\):

**Theorem W.**
\[
\mathfrak S=\mathbb E_\epsilon\!\int\bigl[\rho^2x_\epsilon-4|M_\epsilon|^2\bigr]
+\mathbb E_\epsilon\!\int\frac{(2-\rho)(\rho-1)(3\rho+2)}3
-4\mathbb E_\epsilon\|\zeta_\epsilon\|^2-\mathcal W .
\]
(The \((a,b)\) form collapses exactly to \(-4(|a|^2+|b|^2)\rho=-4|\zeta|^2\); eigenvalues of the
combined form are all \(-4\) in the JSON.)

Interpretation. Non-integrable rotation of the monopole structure is, by the Weitzenböck formula,
the same thing as the Rayleigh component \(W^+(n_\epsilon,n_\epsilon)=x-\rho^2/6\) rising above
its aligned value \(-\rho^2/6\) (\(x>0\)); \(x\) is not an eigenvalue in general and \(x>0\)
alone does not force \(|W^+|<|W_0|\) (the exact channel is \(\rho^2x-4|M|^2\)).
This is exactly the sign of the Theorem-C channel on the certified cell
(\(4\Delta W_+=-0.07513\), paid by \(48\,\mathrm{RV}\approx+0.07080\); Step 39 numerics). The
field saving is thus Weyl-type, while the amplitude depletion terms \(m\) and
\((2-\rho)(\rho-1)(3\rho+2)/3\) are volume-type. The linear Weyl gain \(\rho^2x\) is quadratically
penalized by \(4|M|^2\ge6x^2\): densities of order one pay, diffuse low-density rotation does not.

## 4. Theorem E (pointwise exhaustion at LeBrun's threshold)

Combine the amplitude form \(\mathfrak S\le\mathbb E\int m-8\|\zeta\|^2-4\|M\|^2-\mathcal W\) and
Theorem W with weight \(\lambda\), and the closed identity
\(P=4W_++4V/3-8\pi^2(A-k)\) with \(|W^+|^2=\rho^4/24-\rho^2x/2+|M|^2\) with weight \(1-t\)
(pure blow-ups, \(Q=k\)). Using \(|M|^2\ge\frac32x^2\) and dropping
\(\zeta\)- and Walsh terms,
\[
P\ \ge\ 8\pi^2\bigl[k-(1-t)A\bigr]+\mathbb E_\epsilon\!\int g_{t,\lambda}(\rho_\epsilon),
\]
\[
g_{t,\lambda}=(1-t)\Bigl(\frac{\rho^4}6+\frac43\Bigr)
-t\Bigl[\lambda\frac{(2-\rho)(\rho-1)(3\rho+2)}3+(1-\lambda)m\Bigr]
-\frac{(t\lambda+2-2t)^2\rho^4}{24}.
\]
Exactly (sympy): \(g_{2/3,2/3}=-\tfrac2{243}(2\rho-3)^2(\rho^2-24\rho-18)\ge0\) on \([0,2]\),
which reproduces LeBrun's \(C_+\ge2A/3\), i.e. \(P/(8\pi^2)\ge k-A/3\); and
\(\max_\lambda g_{t,\lambda}(3/2)=-\tfrac34(3t-2)<0\) for every \(t>2/3\).

**Theorem E (affine pointwise exhaustion).** Constant affine combinations of the exact
identities (amplitude form, Nijenhuis/Weyl form, closed Weyl–volume identity), followed by
discarding terms of known sign and the sharp estimate \(|M|^2\ge\frac32x^2\), prove exactly
LeBrun's \(C_+\ge 2A/3\) and nothing more. (Not excluded: non-affine pointwise inequalities,
other weighted Weitzenböck multipliers, joint algebraic constraints among the \(2^k\) spinors
sharing one \(W^+\), and all differential/global information.) The envelope binds only at uniform amplitude \(\rho=3/2\), not at
Kähler–Einstein points (where \(g_{2/3,2/3}(2)=124/243>0\)).

Consequences for the route. (a) The "compensation inequality" sought in Step 39 cannot come
from this affine pointwise scheme: shallow depletion and Nijenhuis rotation can be spread at
low density with no pointwise penalty in it (see §5 for the explicit formal state). (b) Combined with the Step-38 blindness theorem (the exceptional charge of
a sign flip sits in \(h^-\), while all self-dual data measure \(h^+\); the forced zero of \(u\)
unwinds through \(w\) in \(S^3\)), every \(k\)-dependent improvement must come from genuinely
global or differential information: the Walsh self-dual energy, the harmonic-projection terms
\(J_\epsilon\), the \(\zeta\)-terms (which price the Lee component and amplitude gradients), or
elliptic/regularity structure of the actual solutions. (c) For constructions toward small \(c\),
the pointwise saving density (sign-averaged) is at most \(\max_\rho F_{3/4}=0.8\) (attained at \(\rho=1.6\);
\(F_\lambda=\max_\rho[\lambda^2\rho^4/24+\lambda p_2+(1-\lambda)m]\)), so the saving region must
have volume at least \(10\pi^2(1-c)\) per class in the \(s=-4\) normalization, with \(J_\epsilon\)
non-integrable and \(W^+(n_\epsilon,n_\epsilon)>-\rho^2/6\) there.

## 5. The formal common mode: the identities permit \(c\to0\), and what would forbid it

(Integrated from `trace/ttcs/results/step40_ttcs01_generator1_integration.md`, §7–8, and
checked by hand.) Take constant amplitude \(\rho=r\), \(\zeta=0\), \(d\psi=0\) (so \(b=0\),
\(v_4=0\)): an almost-Kähler structure \(\omega=\sqrt2 n\) with harmonic \(\psi=rn\). The spinor
Weitzenböck formula gives \(|\nabla n|^2=2(2-r)\); the self-dual one gives
\(x=(2-r)(4-r)/6\), i.e. \(W^+(n,n)=\tfrac43-r\). With \(M=\mathrm{diag}(x,-x/2,-x/2)\),
\(\mathcal W=0\) (so \(r^2V=8\pi^2A\) by \(\mathcal W=\mathbb E\int\rho^2-8\pi^2A\)) and the closed
identity,
\[
\frac{P}{8\pi^2}=k-A\beta(r),\qquad \beta(r)=\frac{16}r-5-\frac{12}{r^2},\qquad
\beta(2-h)=h-\tfrac{h^2}4+O(h^3).
\]
\(r=3/2\) is LeBrun's threshold \(\beta=1/3\). For \(h=k/A\), \(r=2-h\) gives \(P/(8\pi^2)=O(kh)=o(k)\)
with torsion \(|\nabla J|^2\sim2h\) spread uniformly over the volume \(2\pi^2A\). So the exact
identities are consistent with \(c\to0\) through a *uniform, low-density, common almost-Kähler
rotation*. Since all \(\psi_\epsilon\) coincide in this state, the harmonic self-dual parts of
all \(a_\epsilon\) coincide: every \(E_i\) is anti-self-dual harmonic for \(g\). This is the
global form of the null-period mechanism of the certified cell (zero almost-Kähler period on
\(E\)); the classes must be carried by small sign-dependent defects with charge in \(h^-\).

The decisive obstruction to this mode is linear versus quadratic. In the formal state
\(P\sim(\int|\nabla J|^2)^2/V\). Perturbatively about a Kähler–Einstein host \(g_0\),
\(g=g_0+tH\), both \(P=t^2\|\mathcal L_EH\|^2+O(t^3)\) and the torsion energy
\(t^2\|\mathcal TH\|^2\) are quadratic in \(t\); hence a finite *torsion quotient*
\[
C_{AK}(g_0)=\sup_{H\perp\text{gauge, KE moduli}}\frac{\|\mathcal TH\|^2}{\|\mathcal L_EH\|^2}
\]
forces \(P\gtrsim C_{AK}^{-1}\int|\nabla J|^2\), which is incompatible with the common mode
(\(P=o(\int|\nabla J|^2)\)). Koiso's theorem that Einstein deformations of negative KE surfaces
are Kähler makes the kernel torsion-free, so \(C_{AK}<\infty\) on each fixed host; the real
question is uniformity along cover towers (spectral gap of \(\mathcal L_E\) on TT tensors on
ball-quotient covers) and the nonperturbative regime. This is a quantitative negative-scalar
Goldberg problem: a uniform estimate \(P\ge\kappa\int|\nabla J|^2\) for monopole almost-Kähler
structures near negative KE metrics would make diffuse rotation pay linearly, confining any
saving to non-perturbative cores where the Theorem-G whole-core accounting applies.

## 6. What remains open

- A \(k\)-dependent lower bound for \(0<k<A/3\) needs differential input (Theorem E). The
  natural candidates are (i) a Bochner/elliptic estimate showing that the Nijenhuis energy of
  \(J_\epsilon\) cannot be diffuse because the Walsh singleton curvature (\(h^-\), fixed
  \(4\pi^2\)) localizes near a 2-cycle dual to \(E_i\); (ii) an argument that diffuse rotation of
  all \(2^k\) structures forces \(\sum_I\|f_I^+\|^2\) or \(J_\epsilon\) to grow; (iii) the converse
  construction: a metric family with \(\rho\approx1.6\), \(x>0\) on volume \(\gtrsim10\pi^2(1-c)k\)
  while \(\mathcal W\) and the \(\zeta\)-terms stay \(o(k)\).
- The pointwise identity \(|d\psi|^2=2\rho|b|^2=2|\operatorname{Im}\zeta|^2\) and the integrated
  self-dual Weitzenböck form were confirmed numerically and by the independent verification
  `trace/ttcs/results/step40_ttcs01_verifier1_integration.md` (Lemma 1, Theorems N, W, E
  verified as exact; repairs above incorporated). A direct residual \(\|Q_d-2I_b\|\) should
  be added to the script.
