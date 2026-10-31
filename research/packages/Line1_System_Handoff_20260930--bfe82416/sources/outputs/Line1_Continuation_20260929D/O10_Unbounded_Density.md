# O10 without an Euler-density bound: two valid reductions and one exact cancellation

Date: 2026-09-29. Scope: the unrestricted O10 continuation. This note does not re-prove the already established finite-density theorem and does not claim that the unrestricted gap has been proved.

## 1. Inputs that do not use opposite-Weyl energy

All integrals below are normalized by the actual volume. The inherited strong-current and direct-resolvent arguments give, along a putative unrestricted zero-end sequence,

\[
 |v|\le C,
 \qquad |Lv|\le C,
 \qquad Lv-2v\longrightarrow0\quad\hbox{in }L^2,
 \qquad m=|v|^2\longrightarrow m_*={128\over81}\quad\hbox{in }L^2,
 \tag{1.1}
\]

where \(L=\nabla^*\nabla\) on \(S^-\otimes L\). In particular

\[
 \fint|\nabla v|^2=\fint\operatorname{Re}\langle v,Lv\rangle
 \longrightarrow2m_*.
 \tag{1.2}
\]

The positive spinor has \(\rho=|\Phi|^2\to\rho_*=4/3\), with \(d\rho\to0\) in \(L^2\). Its first torsion projection transfers to \(N_v\to0\) in \(L^2\) on each fixed positive-\(\rho\) region. None of these assertions requires a bound for \(\fint|W^-|^2\).

By contrast, the available bounds for \(\nabla^2v\) in \(L^2\) and \(\nabla v\) in \(L^4\) still depend on opposite-Weyl energy. The arguments below do not use those bounds.

## 2. Original-spinor zero regions can be removed by capacity, without an L4 estimate

The following elementary Caccioppoli estimate is useful here precisely because it only requires (1.1). For every smooth scalar cutoff \(0\le\chi\le1\), testing the equation for \(v\) by \(\chi^2v\) gives

\[
 \fint\chi^2|\nabla v|^2
 =\fint\chi^2\operatorname{Re}\langle Lv,v\rangle
 -2\fint\chi\operatorname{Re}\langle\nabla v,d\chi\otimes v\rangle.
\]

Young's inequality and the pointwise bounds in (1.1) imply

\[
 \boxed{\fint\chi^2|\nabla v|^2
 \le C\fint\bigl(\chi^2+|d\chi|^2\bigr).}
 \tag{2.1}
\]

Fix \(0<a<b<\rho_*\), and take \(\chi=\chi(\rho)\), equal to one on \(\rho\le a\) and zero on \(\rho\ge b\). Since \(\rho\to\rho_*\) in measure and \(d\rho\to0\) in \(L^2\),

\[
 \fint\chi^2+|d\chi|^2\longrightarrow0.
\]

Consequently

\[
 \boxed{\fint_{\{\rho\le a\}}|\nabla v|^2\longrightarrow0.}
 \tag{2.2}
\]

Thus removing the original positive-spinor low-amplitude region does not need the finite-density L4 estimate. The remaining difficulty lies in low amplitude of \(v\) itself, where no corresponding capacity estimate has yet been obtained.

More generally, (2.1) removes any exceptional set admitting scalar cutoffs whose normalized \(H^1\) norms tend to zero. Vanishing relative volume alone is insufficient for this purpose.

## 3. Any unresolved amplitude-gradient concentration is confined to lower wells

Use the positive scalar Laplacian \(\Delta=d^*d\). The exact identity is

\[
 \Delta m=2\operatorname{Re}\langle Lv,v\rangle-2|\nabla v|^2\le C.
 \tag{3.1}
\]

For \(a\ge0\), use the Lipschitz test \((m-a)_+\), justified by smooth convex approximation. It gives

\[
 \fint_{\{m>a\}}|dm|^2
 =\fint(m-a)_+\Delta m
 \le C\fint(m-a)_+.
 \tag{3.2}
\]

In particular,

\[
 \fint_{\{m>m_*\}}|dm|^2\longrightarrow0,
 \tag{3.3}
\]

and for each \(0<\delta<m_*\),

\[
 \boxed{\limsup_j\fint_{\{m>m_*-\delta\}}|dm|^2\le C\delta.}
 \tag{3.4}
\]

The first-order projection has the algebraic phase identity, with a sign depending on the chosen projection convention,

\[
 |j_v\mp J_+dm/2|\le C|v|\,|N_v|,
 \qquad j_v=\operatorname{Im}\langle v,\nabla v\rangle.
 \tag{3.5}
\]

Equations (2.2), (3.4), and (3.5) imply the analogous double-limit vanishing of \(j_v\) outside the lower-amplitude wells. Therefore the unresolved phase/radial defect cannot be an upper-amplitude spike. It is confined to sets on which \(m\) falls below its limiting value, whose relative volumes vanish for every fixed depth.

This conclusion is weaker than \(dm\to0\) in \(L^2\). In particular, (3.4) does not bound the gradient energy on \(\{m\le m_*-\delta\}\). It would be incorrect to remove that set using its vanishing volume and the available L2 gradient bound.

## 4. The proposed weighted projection shortcut cancels exactly

A natural possible shortcut is to test the nearly vanishing holomorphic-type projection by \(v f(m)\), hoping to obtain a new positive \(f'(m)|dm|^2\) term without differentiating \(v\) twice. The relevant term cancels against the phase current.

Here is the pointwise algebra with fixed conventions. Take the Hermitian metric linear in its second argument and the projection

\[
 \mathsf P={I-iJ_+\over2},\qquad N=\mathsf P\nabla v.
\]

Then

\[
 \langle v,\nabla v\rangle={dm\over2}+ij_v,
 \qquad N\simeq0\quad\Longrightarrow\quad j_v\simeq J_+dm/2.
 \tag{4.1}
\]

For real \(f=f(m)\),

\[
 N(fv)=fN+\mathsf P(df)\otimes v.
\]

Since \(\mathsf P\) is an orthogonal complex projection,

\[
 \begin{aligned}
 \operatorname{Re}\langle N,\mathsf P(df)\otimes v\rangle
 &=\frac14\langle dm,df\rangle
   -\frac12\langle j_v,J_+df\rangle\\
 &=\frac14f'(m)|dm|^2
   -\frac12\langle J_+dm/2,J_+f'(m)dm\rangle
   +\text{projection error}\\
 &=\text{projection error}.
 \end{aligned}
 \tag{4.2}
\]

For fixed bounded \(f'\), the integral of that error tends to zero by \(N\to0\), bounded \(v\), and the L2 bound for \(dm\). Reversing the projection convention reverses the phase identity and the skew term together, leaving the cancellation unchanged.

The associated projection Weitzenboeck formula only involves the self-dual curvature contraction, which is attractive because that contraction contains no uncontrolled \(W^-\). However, its rough-Laplacian and curvature-potential terms already match at this endpoint. After the exact cancellation (4.2), it supplies no independent positive radial-gradient term. A proof using this test must provide an additional term not present in this formal weighted identity.

## 5. What the new L5 argument still requires in the unrestricted case

The positive line-bundle resolvent test at the end of the supplied fifth-line proof depends only on Ricci and determinant-line curvature bounds. That final inverse is not where the uncontrolled opposite-Weyl energy enters.

The unproved unrestricted connections occur earlier:

1. The finite-density argument turns \(m\to m_*\) into \(dm\to0\). The above calculations remove the original-spinor zero region and locate the remaining radial defect, but do not eliminate the lower wells of \(m\).
2. The reduction to a single surviving off-diagonal coefficient requires the phase/radial error to be negligible. It is presently established globally by the finite-density gradient/Hessian estimates.
3. Even after that reduction, the weak CR errors contain products of a small L2 coefficient with \(\nabla v\). Without additional integrability this is only L1-small, whereas the line-resolvent test has an L4 first derivative, not a uniform pointwise first-derivative bound.
4. A positive L2 mass of the resulting line section need not survive a fixed amplitude truncation without uniform integrability. The finite-density L4 estimate supplies exactly that missing property.

These issues cannot be removed merely by noting that the final test line bundle has no \(W^-\) curvature. Nor does \(\forall B<\infty\,\exists c(B)>0\) yield one positive constant uniform in \(B\).

## 6. Full Cartan calculation: a second attempted radial estimate also cancels

It is essential not to write \(b=c\theta_2\) before the radial current has been controlled. With \(N_v=Dv=0\) but with \(dm\) retained, the adapted-frame equations give

\[
 q={1\over2m}(m_2,-m_1,m_4,-m_3),
 \qquad
 b=d\theta_1+c\theta_2,
 \qquad
 d=-{m_3+im_4\over2m}.
 \tag{6.1}
\]

Here \(m_i=e_i(m)\), and \(d\) in (6.1) denotes a coefficient, not the exterior derivative. The additional coefficient follows from the second component of the Dirac equation: the radial component of \(\nabla_{\bar Z_2}v\) is cancelled by the second component of \(\nabla_{\bar Z_1}v\).

The complete Cartan equation is

\[
 d\theta_1=-i(\mathfrak a+p-q)\wedge\theta_1
             +\kappa\Xi_+-d\overline{\Xi_+},
 \qquad
 (F^{S^+})_{21}
 =(d\kappa+i\kappa(q-3p))\wedge\theta_1
       +\kappa^2\Xi_+-\kappa d\overline{\Xi_+}.
 \tag{6.2}
\]

The coefficient \(c\) cancels from \(d\theta_1\), but \(d\) does not. Since

\[
 \kappa={\sqrt m\over2\rho^{3/2}},
 \qquad q\simeq-{J_+dm\over2m},
\]

the mass-dependent part in (6.2) is

\[
 {\kappa\over2m}(dm-iJ_+dm)\wedge\theta_1.
 \tag{6.3}
\]

Using \(\overline{\Xi_+}=\theta_1\wedge\theta_2\), (6.3) equals

\[
 -\kappa{m_3+im_4\over2m}\,\overline{\Xi_+}
 =\kappa d\overline{\Xi_+}.
\]

It therefore cancels the last term in (6.2) exactly. The first-plane component was already in the wedge kernel. Thus the full positive-connection equation does not supply the hoped-for second-plane radial estimate. Dropping \(d\theta_1\) from \(b\) at this stage would introduce a circular argument.

This does not invalidate the finite-density proof's reduction to \(b=c\theta_2+o_{L^2}(1)\): in that proof \(dm\to0\) has already been established, so the additional coefficient \(d\) is small. The issue concerns only an attempted extension that omits that established input.

There is nevertheless a potentially useful exact weight. If the second-plane component of \(dm\) can be made negligible at the needed strength, then \(J_+dm\simeq J_-dm\). The symbol from the fifth-line proof obeys

\[
 \mathcal L(iJ_-\alpha)=-\mathcal L(\alpha).
\]

Consequently, in the exact model with \(q=-J_-dm/(2m)\),

\[
 \boxed{
 \mathcal L(D_5c-3iqc)
 =m^{3/2}\mathcal L\bigl(D_5(m^{-3/2}c)\bigr).
 }
 \tag{6.4}
\]

This conditional algebraic weight does not resolve the full system: the second-plane reduction is not provided by (6.2), and the full equation for \(b\) has the extra \(d\theta_1\) component and its derivatives. Formula (6.4) must not be substituted for that full equation. Control at low \(m\) and a legal weak test also remain necessary.

## 7. Status

The unrestricted O10 gap and a genuine closed-manifold escape construction remain unresolved in this note. The two proved reductions are (2.2) and (3.4); the weighted-projection route in Section 4 is excluded as an independent source of coercivity. These conclusions preserve the original unrestricted quantifiers and identify the exact concentration information that a further proof must add.
