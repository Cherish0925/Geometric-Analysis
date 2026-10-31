# Step 43 — The corrected \(W_0\) tensor, Cotton transport, and the quadratic common-mode law

Session S1003A02, Agent3. This note enters the Step-39/41 material into the workspace and sharpens the Step-42 Goldberg reduction. It uses the scalar \(-4\) simultaneous-field conventions of `workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md`: for one monopole solution
\[
\psi=\rho n,\qquad |n|=1\text{ in }\Lambda^+,
\qquad
W_0=\frac14\left(\frac{\rho^2}{3}I-\psi\otimes\psi\right)
       = a\left(\frac13 I-n\otimes n\right),\quad a=\frac{\rho^2}{4}.
\]
Here \(M=W^+-W_0\) is the Weyl-alignment error of Theorems N/W.

## 1. Corrected \(W_0\) and the shallow-band geometry

The model tensor is not fixed by scalar normalization. It has eigenvalues
\[
-\frac{\rho^2}{6},\quad \frac{\rho^2}{12},\quad \frac{\rho^2}{12},
\qquad |W_0|^2=\frac{\rho^4}{24}.
\]
Thus the co-rotation forcing is strong only where the monopole amplitude is in the shallow band, especially \(\rho\approx2\); it weakens as \(\rho\to0\).

If two Kähler-type tensors have the same amplitude \(a=\rho^2/4\) and unit directions \(n,m\in\Lambda^+\), then
\[
\left|a\left(\frac13I-n\otimes n\right)-a\left(\frac13I-m\otimes m\right)\right|^2
 =2a^2(1-\langle n,m\rangle^2)
 =\frac{\rho^4}{8}\sin^2\theta .
\]
If the comparison amplitude \(b\ge0\) is optimized while the direction \(m\) is fixed and \(c=\langle n,m\rangle\), the distance from \(a(I/3-nn)\) to the ray \(b(I/3-mm)\) is
\[
\min_{b\ge0}|aK_n-bK_m|^2=
\begin{cases}
\displaystyle \frac{a^2}{2}(1-c^2)(1+3c^2),& c^2\ge\frac13,\\[4pt]
\displaystyle \frac{2a^2}{3},& c^2\le\frac13.
\end{cases}
\]
In particular \(W^+=0\) pays exactly \(|W_0|^2=\rho^4/24\), which is \(2/3\) at \(\rho=2\), but is not a universal pointwise cost.

The kinetic split is also rigid. From Step 40,
\[
K=\int|\nabla\Phi|^2=\int\frac{|\zeta|^2}{\rho}+\frac14\int \rho |\nabla n|^2.
\]
Before resolving the Lee part of \(\nabla n\), the two explicit appearances of \(|\zeta|^2\) have formal net coefficient \(8-4/\rho\), positive for \(\rho>1/2\). This is useful bookkeeping but not a final coefficient because the Dirac equation expresses the Lee component in the same amplitude/phase variables. The exact safe statement is Theorem N: after resolving that component, every non-Nijenhuis first-jet contribution occurs in the nonnegative form
\[
\rho\bigl(|d\sqrt\rho|^2+5|b|^2-2\langle d\sqrt\rho,J'b\rangle\bigr).
\]
Therefore shallow-band saving cannot be carried by amplitude/Lee kinetic energy; it must enter through the Nijenhuis/\(W_2\) rotation of \(n\), while the exact positive form and \(\zeta\) remain small.

## 2. Algebraic co-rotation is not the theorem: the AAD countermodel and the Cotton slack

Apostolov--Armstrong--Drăghici show that local strictly almost-Kähler four-manifolds can have Kähler-type algebraic curvature: in their notation \(\operatorname{Ric}_0^{\rm anti}=0\), \(W_2^+=0\), and in the unique proper three-symmetric model also \(W_3^+=0\), without \(J\) being integrable. Thus a pointwise theorem saying "\(W^+\) is rank-one and co-rotates with \(n\), hence \(\nabla n=0\)" is false. The missing information is differential.

Their differential Bianchi identities make the slack explicit. For an almost-Kähler structure in class \(\mathcal{AK}_3\), with
\(\nabla\Omega=a\otimes\phi-Ja\otimes J\phi\), \(W_3^+\) eigenvalue \(\lambda\), and conformal scalar \(\kappa\), they prove
\[
d(\kappa-s)=-12\lambda J\phi(a),
\qquad
\operatorname{Ric}_0(a)=\frac\kappa4a+2\lambda\phi(b)-J\phi(d\lambda),
\]
\[
\Delta(\kappa-s)=-\frac\kappa2(\kappa-s)-24\lambda^2+12\operatorname{Ric}_0(a,a).
\]
The proof identifies \(\delta W^+=C^+\), the self-dual Cotton tensor. In the same source, the Cotton components are written in terms of \(\nabla\operatorname{Ric}_0\), and for \(J\)-invariant Ricci the \(\mathcal V^-\) component satisfies \(\beta=-\frac12\operatorname{Ric}_0(a)\). Catino--Dameno's weighted Derdziński identity gives the eigenline version: for a divergence-free weighted self-dual Weyl tensor \(A\) with eigenvalues \(\mu_r\),
\[
d\mu_1=(\mu_1-\mu_2)\iota_{a^\sharp}\omega_3+(\mu_1-\mu_3)\iota_{c^\sharp}\omega_2,
\]
and after the conformal normalization with \(\mu_1=1\),
\[
(1-\rho)\iota_{a^\sharp}\omega_3+(2+\rho)\iota_{c^\sharp}\omega_2=0.
\]
So the stationary endpoint is indeed Derdziński/Cotton: if the weighted half-Weyl divergence vanishes and the eigenvalue gap is nonzero, eigenline rotation is constrained into conformal Kähler geometry. Away from stationarity, the source is \(\delta W^+=\nabla\operatorname{Ric}^\circ\), and the direct defect \(P=\int|\operatorname{Ric}^\circ|^2\) does not supply an \(L^2\) bound for that derivative.

## 3. Exact symbol calculation for \(\delta W_0\)

The script `workspace/scripts/step43_w0_divergence_symbol.py` computes the pointwise symbol for
\[
W_0=a\left(\frac13I-n\otimes n\right)
\]
in an oriented orthonormal frame of \(\Lambda^+\), restricting \(\nabla n\) to the almost-Kähler first-jet condition \(d(\sqrt2 n)=0\). The output is `workspace/data/step43_w0_divergence_symbol.json`.

With the script's tensor norms,
\[
\boxed{\quad
|\delta W_0|^2=\frac{a^2}{2}|\nabla n|^2+\frac13|\nabla a|^2,
\quad\text{and the two summands are orthogonal.}\quad}
\]
Equivalently, the generalized **squared** singular value of the torsion part is exactly \(1/2\), so the singular value is \(1/\sqrt2\): the characteristic polynomial is \((2\lambda-1)^4\). This is the clean algebraic core of the Cotton-transport mechanism. If \(E=W^+-W_0\), then
\[
\delta W_0=\delta W^+-\delta E=C^+-\delta E.
\]
The identity itself does **not** produce a lower bound from \(P\), because both terms on the right contain derivatives: \(C^+=\nabla\operatorname{Ric}^\circ\) and \(\delta E\). Pairing with the torsion part and integrating by parts is the only direct way to use \(P\). The displayed norm formula is restricted to a closed almost-Kähler first jet. A general monopole direction also has a Dirac-controlled Lee component; its divergence formula contains additional \(dn\) and amplitude--Lee cross terms, which must be retained or controlled by the exact \(\zeta\) form in Theorem N.

## 4. Cotton transport gives the quadratic, not linear, law

Let \(R\) denote the relevant sign-averaged Nijenhuis/rotation energy, e.g. on a shallow band
\[
R\sim\mathbb E_\epsilon\int |\nabla n_\epsilon|_{W_2}^2,
\]
and assume for this paragraph that \(a\) is bounded below on the region carrying the rotation, boundary/zero-set terms are controlled, and the almost-Kähler second-jet terms are controlled by curvature in the standard way (as in the AAD Ricci identities above). Pair the equation
\[
a\,\mathcal T(\nabla n)=\delta W^+-\delta E-\mathcal A(\nabla a)
\]
with \(\mathcal T(\nabla n)\). Integration by parts turns \(\delta W^+=C^+\) into \(\operatorname{Ric}^\circ\) paired with a first derivative of \(\mathcal T(\nabla n)\); the almost-Kähler Ricci identities express that derivative through curvature and first-jet terms. What follows is therefore a **conditional target**, not a theorem proved by the symbol calculation. On a closed constant-scalar almost-Kähler region, let \(U=\mathcal T(\nabla n)\), assume \(a\ge a_0>0\), and put \(E=W^+-W_0\). Exact integration by parts gives
\[
\frac12\int a|\nabla n|^2
 =\int\langle\operatorname{Ric}^\circ,\mathcal C^*U\rangle
  -\int\langle E,\delta^*U\rangle.
\]
Hence
\[
\frac{a_0}{2}\int|\nabla n|^2
\le \sqrt P\,\|\mathcal C^*U\|_2+\|E\|_2\,\|\delta^*U\|_2.
\]
To obtain the hoped-for scale-invariant estimate one still must prove a second-jet bound such as
\[
\|\mathcal C^*U\|_2+\|\delta^*U\|_2\le C_2\|\operatorname{Rm}\|_2.
\]
This is nontrivial: the left side contains \(\nabla^2n\) and \((\nabla n)^2\); the harmonic-form Weitzenböck formula controls only contracted Hessians. The AAD formulas supply this structure only under their additional \(\mathcal{AK}_3\) hypotheses. A localized monopole version also needs zero-set and shallow-band cutoff control, the Lee component, and amplitude-gradient products. In the exact almost-Kähler pairing the amplitude part is orthogonal to \(U\), so a separate \(\|\nabla a\|_2\) term appears only after such localization or in a more general Lee-containing test.

If these missing estimates are proved and \(E\) is noncircularly controlled, they would give
\[
R\lesssim(\sqrt P+\|E\|_2)\|\operatorname{Rm}\|_2,
\qquad \|\operatorname{Rm}\|_2^2=8\pi^2\chi(M)+P.
\]
For a ball quotient blow-up, \(\chi=A/3+k\). When \(E\) is negligible and \(A\) dominates, this becomes \(P\gtrsim R^2/A\), exactly the Step-40 common-mode scale. Thus a Cotton-source/Cauchy--Schwarz route, even if completed, yields a quadratic rather than linear law. The linear route remains perturbative spectral theory near a Kähler--Einstein host, where the Einstein operator has a finite torsion quotient after gauge and Kähler moduli are removed; cover-uniformity is a further theorem, not yet proved.

Combining a completed quadratic law with Theorem N would give a positive lower scale. Define the **total** sign-averaged \(W_2\) energy
\[
R:=\mathbb E_\epsilon\int|\nabla n_\epsilon|_{W_2}^2.
\]
Since \(0\le\rho\le2\), Theorem N gives exactly
\[
P\ge8\pi^2k-2R.
\]
If one independently proved \(P\ge R^2/(\Lambda A)\), exact optimization yields
\[
P\ge\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
 =\frac{16\pi^4k^2}{\Lambda A}+O\!\left(\frac{k^3}{A^2}\right).
\]
This is a conditional scale law, not a current Einstein-gap theorem. A band-restricted \(R\) needs an extra complementary term. An error \(R\le C_T\sqrt A(\sqrt P+\varepsilon)\) gives only \(P\ge(R/(C_T\sqrt A)-\varepsilon)_+^2\), so no gap follows unless \(\varepsilon\) is controlled noncircularly. The heuristic numerical fraction at \(k=A/3\) is therefore not a proved constant and is not promoted. The structural constructive question remains whether closed near-minimizers can realize the diffuse quadratic scale.

## 5. Why \(E\) and \(\nabla a\) are the real escape terms

The current field identities do not bound \(\|E\|_2\) and \(\|\nabla a\|_2\) by \(P\) alone.

* \(E=M=W^+-W_0\) appears with a positive \(4\|M\|^2\) term in the signed identity, but that term is balanced against the kinetic saving \(-4K\). In a subunit sequence, \(\|M\|_2^2\) can be paid by the same shallow depletion that creates the saving; bounding it by the final value of \(P\) would be circular.
* \(a=\rho^2/4\) and \(\nabla a\) are controlled through the \(\zeta\)/amplitude-gradient terms and the depletion \(L=\mathbb E\int(2-\rho)_+\). But Theorem 39's shallow-band theorem says a subunit sequence must have \(L\gtrsim(1-c)k\). A bound through \(L\) gives only \(R\lesssim\sqrt{RA}\) at the common-mode scale, hence no positive lower bound.
* Deep depletion \(\rho<0.7758\ldots\) is unfavorable in the amplitude polynomial, but localized shallow depletion with nondegenerate \(W^+\) can still finance \(E\) and \(\nabla a\) unless a new localization or monotonicity statement is added.

Therefore the exact escape configuration is now precise: a near-minimizer avoiding a per-class tariff must keep \(a\) in the shallow band, keep \(\zeta\) small, make \(W^+\) nearly Kähler-type and co-rotating with \(n\) except for an \(E\) financed by depletion, and distribute Nijenhuis rotation over a volume comparable to \(A\), while Lemma T forces exceptional classes to appear as tiny positive-area pseudoholomorphic spheres or through zeros of the harmonic part rather than as exactly null periods of a nowhere-zero form.

## 6. Sekigawa/Kirchberg formula: the resisting term

Kirchberg's four-dimensional almost-Kähler identity records exactly the sign failure. With his conventions,
\[
Q(J)+\int\left(|\widetilde R|^2+4|\operatorname{Ric}_\star^-|^2+rac S2|\nabla J|^2+|\nabla J|^4\right)=0,
\]
and equivalently
\[
Q(J)+\frac12\int\left(|\widetilde R|^2+|\nabla J|^4+|W_+|^2-\frac{S^2}{6}\right)=0.
\]
For \(S=-4\), the term \((S/2)|\nabla J|^2=-2|\nabla J|^2\) has the wrong sign. The obstruction
\[
Q(J)=2\int\langle\varphi,\psi\rangle
\]
is a derivative-of-Ricci pairing: Kirchberg writes
\[
\langle\varphi,\psi\rangle=rac14\left\langle J\varphi(X^k,X^l),
(\nabla_{X_k}\operatorname{Ric})X_l-(\nabla_{X_l}\operatorname{Ric})X_k\right\rangle.
\]
Thus the exact resisting term is the same Cotton source identified above. If the relevant harmonic-Weyl/Eigenform conditions make \(Q(J)=0\), the additional Weyl algebra can force Kählerness, but for negative scalar curvature and only \(P\)-control, \(Q(J)\) is uncontrolled except by the quadratic Cauchy--Schwarz law.

## 7. Proper three-symmetric test object

The mandatory Apostolov--Armstrong--Drăghici local model has
\[
s=-\frac34,\qquad \kappa=\frac34,
\qquad \operatorname{spec}(\operatorname{Ric})=(0,0,-3/8,-3/8).
\]
Their identity \(\kappa-s=\frac32|\nabla\Omega|^2\) gives \(|\nabla\Omega|^2=1\). Exact arithmetic in `workspace/scripts/step43_proper3symmetric_test.py` gives
\[
|\operatorname{Ric}^\circ|^2=\frac9{64},
\qquad
\frac{|\operatorname{Ric}^\circ|^2}{|\nabla\Omega|^4}=\frac9{64}.
\]
Thus this strictly almost-Kähler, Kähler-curvature-type countermodel does not refute a quartic pointwise inequality, but any universal pointwise constant in these conventions is at most \(9/64\). It is local/noncompact and yields no closed-manifold gap.

## 8. Current mathematical consequence

The nonperturbative linear estimate
\[
P\ge \kappa\int |\nabla J|^2
\]
is a quantitative negative-scalar Goldberg theorem and should not be claimed. The honest coercive outputs now split into two precise, attackable statements:

1. **Perturbative KE theorem.** Near a negative Kähler--Einstein ball quotient, after gauge fixing and removing Kähler moduli, prove
\[
\int|\operatorname{Ric}^\circ|^2\ge \kappa_0\int |\nabla J|^2
\]
with \(\kappa_0\) independent of finite covers if the Bochner/Koiso constants are pointwise or have a cover-uniform spectral gap. This only excludes common-mode realizations close to the KE host.
2. **Quadratic transport theorem.** Prove the Cotton inequality above with exact cutoffs and zero-set terms. If \(E\) and \(\nabla a\) can be bounded by noncircular quantities, it gives \(P\gtrsim k^2/A\). If they cannot, the failure identifies the construction target: diffuse shallow depletion with co-rotating \(W^+\) and controlled exceptional-area/zero-set topology.

The direct global problem is still open, but the alternatives have changed. It is plausible that \(P>0\) for every fixed blow-up while the best per-class coefficient tends to zero along towers; this would reconcile positive Einstein gaps with the formal common mode and the certified subunit local cell.
