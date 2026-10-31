# O10: independent verification of the torsion resolvent argument

**Date:** 2026-09-29.  
**Role:** independent mathematical verification by the geometry/PDE subagent.  
**Sources:** the integrated manuscript \(\texttt{27b3cef6-aeed-442c-9e66-fef1a757828e.tex}\), especially the single-solution ASD fit, actual opposite-spinor equation, and rank-two Chern transgression; and the independently checked strong-current result \(\texttt{01\_O10\_Strong\_Current.md}\).

## Result

The proposed bundle resolvent argument closes the hypothetical weak zero endpoint when
\[
\frac{\chi(M)}A\le\frac38.
\]
It also gives a strictly larger, non-sharp density range: there are universal constants \(\delta_0>0\) and \(c_0>0\), depending only on the fixed conventions and the existing universal single-solution estimates, for which the O10 estimate holds when
\[
\frac{\chi(M)}A\le\frac38+\delta_0.
\]
The argument does not settle O10 for every prescribed finite Euler-density bound, and does not address the version with no Euler-density bound.

The decisive change is to replace the actual torsion section by a bounded section of the **same bundle** having bounded rough Laplacian. The replacement retains the asymptotically constant positive amplitude and the bundle's characteristic number. A derivative-free weighted Hessian argument supplies the needed critical derivative control without a Sobolev inequality, a coordinate regularity theorem, or noncollapse.

Everything below is conditional on the previously proved strong-current theorem, not a reproof of that entire theorem. The new arrows are checked explicitly.

## 1. Endpoint inputs and what the critical density supplies

Suppose an O10 countersequence exists. By the existing finite-parameter estimate and exact negative Yamabe reduction, it is enough to consider
\[
s_{g_j}=-4,\qquad \beta_j\to\infty,\qquad
r_j=\fint|\operatorname{Ric}_{g_j}+g_j|^2\to0,\qquad
D_{\beta_j}/V_j\to0.
\]
The same actual solution can be normalized as
\[
D_{A_j}\Phi_j=0,\qquad F_{A_j}^+=2i\sigma(\Phi_j),\qquad
\rho_j=|\Phi_j|^2\le2.
\]
Write \(\tau_j=t_{\Phi_j}\in E_j=S_j^-\otimes L_j\), \(m_j=|\tau_j|^2\), and \(m_*=128/81\). All integrals and norms below are normalized by \(V_j\), except when explicitly displayed as unnormalized integrals.

The established strong-current theorem gives
\[
\rho_j\to\frac43,\quad |\nabla\Phi_j|^2\to\frac49,\quad
m_j\to m_*\quad\text{strongly in }L^2_{\rm avg},
\tag{1.1}
\]
\[
\|D^-_{3A_j}\tau_j\|_{2,\rm avg}\to0,\qquad
\sup_j\fint|\nabla\tau_j|^2<\infty.
\tag{1.2}
\]
It also gives the same-solution bounded ASD fit
\[
f_j=-iF_{A_j}^-=K_j+e_{F,j},\qquad
K_j=-\frac98\,\frac{\rho_j^3Q_j}{S_j},\qquad
Q_j=-iq_-(\tau_j),\quad
S_j=m_*+2\rho_j^2|\nabla\Phi_j|^2,
\tag{1.3}
\]
where
\[
|K_j|\le C,\qquad \|e_{F,j}\|_{2,\rm avg}\to0.
\tag{1.4}
\]
The fit is a prior result and does not depend on regularity of the new resolvent section constructed below.

The endpoint calibration is
\[
\frac{8\pi^2p_j}{V_j}\longrightarrow\frac{16}{9}.
\tag{1.5}
\]
Since \(A_j\le p_j\), Gauss--Bonnet at \(s=-4\) gives, if \(\chi_j/A_j\le3/8\),
\[
\begin{split}
\fint\bigl(|W_j^+|^2+|W_j^-|^2\bigr)+\frac23-\frac12r_j
&=\frac{8\pi^2\chi_j}{V_j}\\
&\le\frac38\,\frac{8\pi^2p_j}{V_j}
=\frac23+o(1).
\end{split}
\tag{1.6}
\]
Consequently both Weyl tensors tend to zero in normalized \(L^2\). In particular, the full unitary curvature of \(E_j\) admits a bounded-model decomposition
\[
\mathbb F_j=\mathbb F_{0,j}+\mathbb E_j,\qquad
|\mathbb F_{0,j}|\le C,\qquad
\|\mathbb E_j\|_{2,\rm avg}\to0.
\tag{1.7}
\]
Indeed the noncentral spin curvature contains \(W_j^-\), the fixed scalar block, and the small trace-free Ricci block; the central curvature is \(3F_{A_j}/2\), whose self-dual part and fitted anti-self-dual part are bounded. No derivative bound for \(\mathbb F_{0,j}\) is used.

For later use, if \(w_j=\fint|W_j^-|^2\) is merely bounded, the same decomposition satisfies
\[
\fint|\mathbb E_j|^2\le Cw_j+o(1).
\tag{1.8}
\]

## 2. A bounded truncation retains the small Dirac residual

The Lichnerowicz formula on \(E_j\) is
\[
D_j^*D_j=\nabla_j^*\nabla_j+\mathcal V_j,\qquad
\mathcal V_j=-1+\frac32c(F_{A_j}^-).
\tag{2.1}
\]
The fitted curvature acts on the actual torsion direction by
\[
\frac32c(iK_j)\tau_j
=-\frac{27}{32}\frac{\rho_j^3m_j}{S_j}\tau_j.
\tag{2.2}
\]
The coefficient on the right is uniformly bounded and tends to \(1\) in normalized measure, by (1.1).

An upper-amplitude cutoff must be justified before using the curvature error on \(\tau_j\); a direct \(L^2\) product of the unbounded torsion and \(e_{F,j}\) is unavailable.

Fix \(M>m_*\). Choose a smooth nondecreasing function \(w(m)\), zero for \(m\le M\), one for \(m\ge2M\), with \(mw'(m)\le C_M\). Test (2.1) against \(w(m_j)\tau_j\):
\[
\begin{split}
\int w|\nabla\tau|^2+\frac12\int w'|dm|^2
+\int w\langle\mathcal V\tau,\tau\rangle
&=\int w|D\tau|^2+
\operatorname{Re}\int\langle D\tau,c(dw)\tau\rangle.
\end{split}
\tag{2.3}
\]
Here \(dw=w'dm\). The last term is bounded by
\[
\frac14\int w'|dm|^2+C_M\int|D\tau|^2.
\tag{2.4}
\]
Using the bounded fit,
\[
\left|\int w\langle\mathcal V\tau,\tau\rangle\right|
\le C\int_{\{m>M\}}m+C\int|e_F|m=o(V).
\tag{2.5}
\]
The first term is small by strong \(m\to m_*\) in \(L^2_{\rm avg}\); the second by Cauchy--Schwarz and (1.4). Thus
\[
\fint_{\{m_j\ge2M\}}|\nabla\tau_j|^2\longrightarrow0.
\tag{2.6}
\]

Choose a smooth scalar cutoff \(\theta(m)\), equal to one below \(2M\) and zero above \(4M\), and set
\[
u_j=\theta(m_j)\tau_j.
\tag{2.7}
\]
Then \(u_j\) is smooth and uniformly bounded. Since
\[
|dm|\le2\sqrt m\,|\nabla\tau|,\qquad m|\theta'(m)|\le C_M,
\]
equation (2.6) proves
\[
\|u_j-\tau_j\|_{H^1_{\rm avg}}\to0,\qquad
\|D_ju_j\|_{2,\rm avg}\to0.
\tag{2.8}
\]
Also \(|u_j|^2\to m_*\) strongly in normalized \(L^2\).

Boundedness now makes the potential estimate legitimate:
\[
(\mathcal V_j+2)u_j
=\left(1-\frac{27}{32}\frac{\rho_j^3m_j}{S_j}\right)u_j
+\frac32c(ie_{F,j})u_j
\longrightarrow0
\quad\text{in }L^2_{\rm avg}.
\tag{2.9}
\]
The first term is a bounded quantity tending to zero in measure, and the second uses bounded \(u_j\) and (1.4).

## 3. The same-bundle resolvent removes the uncontrolled second derivative

Let \(L_j=\nabla_j^*\nabla_j\ge0\). Define the normalized \(H^1\) norm by
\[
\|\xi\|_{H^1_{\rm avg}}^2=\fint(|\xi|^2+|\nabla_j\xi|^2),
\]
and use its dual \(H^{-1}_{\rm avg}\).
By (2.1), (2.8), and (2.9),
\[
(L_j-2)u_j=D_j^*D_ju_j-(\mathcal V_j+2)u_j
\longrightarrow0\quad\text{in }H^{-1}_{\rm avg}.
\tag{3.1}
\]
This uses only
\[
|\langle D_j^*D_ju_j,\xi\rangle|
=|\langle D_ju_j,D_j\xi\rangle|
\le C\|D_ju_j\|_{2,\rm avg}\|\xi\|_{H^1_{\rm avg}}.
\]
The pointwise Clifford estimate for \(D_j\xi\) has a dimension-only constant; no geometric Poincaré or Sobolev inequality is invoked.

Set
\[
v_j=3(1+L_j)^{-1}u_j.
\tag{3.2}
\]
The positive operator \(1+L_j\) is an isometry between \(H^1_{\rm avg}\) and its dual in the associated energy formulation. Therefore
\[
v_j-u_j=-(1+L_j)^{-1}(L_j-2)u_j
\longrightarrow0\quad\text{in }H^1_{\rm avg}.
\tag{3.3}
\]
Elliptic regularity on each individual smooth compact manifold gives smooth \(v_j\); no uniform chart estimate is needed. The unitary rough-Laplacian maximum principle gives
\[
\|v_j\|_\infty\le3\|u_j\|_\infty.
\tag{3.4}
\]
For example, at a maximum of \(|v_j|^2\), the identity
\[
\tfrac12\Delta|v_j|^2
=\operatorname{Re}\langle L_jv_j,v_j\rangle-|\nabla_jv_j|^2
\]
and \(L_jv_j=3u_j-v_j\) imply (3.4). Consequently
\[
|v_j|+|L_jv_j|\le C,\qquad
|v_j|^2\longrightarrow m_*\quad\text{in }L^2_{\rm avg}.
\tag{3.5}
\]
This is the required replacement: \(v_j\) is a section of the original bundle \(E_j\), not of a limit or modified bundle.

## 4. Bounded rough Laplacian suffices for critical gradient control

**Lemma.** Let \(v\) be a smooth section of a unitary bundle over a closed Riemannian manifold of fixed dimension and bundle rank. Assume
\[
|v|+|Lv|\le C_0,\quad
\operatorname{Ric}=R_0+e,\quad F=F_0+E,\quad
|R_0|+|F_0|\le C_0,
\]
and
\[
\mu=\fint(|e|^2+|E|^2)\le C_0.
\]
There are constants \(C,\epsilon>0\), depending only on these displayed constants, dimension and rank, such that
\[
\fint(|\nabla^2v|^2+|\nabla v|^4)\le C
\tag{4.1}
\]
and, for \(q=|\nabla v|^2\), \(H=\nabla^2v\), \(L_0\ge1\),
\[
\fint
\left(\frac q{L_0^2+q}\right)^\epsilon
\bigl(|H|^2+q^2\bigr)
\le CL_0^{-2\epsilon}+C\mu.
\tag{4.2}
\]
No semilinearity of \(Lv\), nor any bound on \(\nabla Lv\), is required.

**Proof.** Put \(f=Lv\), \(P_i=\nabla_i v\), \(H_{ij}=\nabla_iP_j\), and use the smooth weight
\[
w=\left(\frac{q+\varepsilon}{L_0^2+q+\varepsilon}\right)^\epsilon,\qquad \varepsilon>0.
\]
It satisfies
\[
|dw|\,|P|\le2\epsilon w|H|.
\tag{4.3}
\]
Let \(I=\int w|H|^2\), \(J=\int wq^2\), \(A_w=\int w(1+q)\). The exact Hessian interchange is
\[
I=\int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
+\frac12\int w\sum_{ij}|F_{ij}v|^2.
\tag{4.4}
\]
Integrate the derivative indexed by \(j\) in the first term. In \(\nabla_j\nabla_iP_j\), interchange \(j,i\); the commutator is only \(\operatorname{Ric}*P+F*P\), and \(\sum_j\nabla_jP_j=-f\). Thus the derivative of \(f\) appears only in
\[
\int w\operatorname{Re}\langle P,\nabla f\rangle
=\int w|f|^2-\int\operatorname{Re}\langle dw\otimes P,f\rangle.
\tag{4.5}
\]
The second integral is at most \(2\epsilon\int w|H||f|\), which is absorbed by a small part of \(I\) plus \(C\int w\). The other differentiated-weight term is bounded by \(2\epsilon I\). Since \(f\) is bounded, (4.4)--(4.5) yield
\[
I\le CA_w+C\int w(|e|+|E|)q+C\int(|e|^2+|E|^2)
\tag{4.6}
\]
for sufficiently small fixed \(\epsilon\).

Integrate the divergence of \(wq\,\operatorname{Re}\langle v,P\rangle\). Bounded \(v,f\) and (4.3) give
\[
J\le C\int wq+C\sqrt{IJ},\qquad J\le C_1(I+A_w).
\tag{4.7}
\]
For any chosen \(a>0\),
\[
\int w(|e|+|E|)q\le aJ+C_a\int(|e|^2+|E|^2).
\]
Choosing \(a\) after \(C_1\) and absorbing gives
\[
I+J\le CA_w+C\mu V.
\tag{4.8}
\]
First take \(w=1\). The bound
\[
\int q=\int\operatorname{Re}\langle f,v\rangle\le CV
\]
proves (4.1). Next use \(w\le L_0^{-2\epsilon}(q+\varepsilon)^\epsilon\), with \(0<\epsilon\le1\). Equation (4.1) controls the average of \((q+\varepsilon)^\epsilon(1+q)\). Apply (4.8) and let \(\varepsilon\downarrow0\) to prove (4.2). \(\square\)

An immediate consequence, important also for the density extension below, is: if \(\operatorname{Vol}(A_j)/V_j\to0\), then
\[
\limsup_j\fint_{A_j}|\nabla v_j|^4
\le C\limsup_j\mu_j.
\tag{4.9}
\]
Indeed split \(A_j\) into \(q_j<L_0^2\), whose integral is at most \(L_0^4\operatorname{Vol}(A_j)/V_j\), and its complement; apply (4.2), take \(j\to\infty\), then \(L_0\to\infty\).

At the critical density, (1.7) and \(r_j\to0\) make \(\mu_j\to0\). Thus \(|\nabla v_j|^4\) is uniformly integrable relative to normalized volume.

## 5. Chern localization needs a section, not a monopole equation

Fix \(0<a<b<m_*\), and a smooth cutoff \(\chi(t)\) equal to one for \(t\le a\) and zero for \(t\ge b\). Set
\[
B_j=\{|v_j|^2<b\}.
\]
By (3.5), \(\operatorname{Vol}(B_j)/V_j\to0\).

On \(\{v_j\ne0\}\), the unit section \(\widehat v_j=v_j/|v_j|\) defines a unitary splitting into its trivialized line and its orthogonal complement. Replace the connection by the connection making \(\widehat v_j\) parallel on the first line and using the projected connection on the second line. Its second Chern form is zero. The ordinary rank-two Chern--Weil transgression \(T_j\) therefore satisfies
\[
dT_j=c_2(\mathbb F_j),\qquad
|T_j|\le C\bigl(|\mathbb F_j||\nabla\widehat v_j|
+|\nabla\widehat v_j|^3\bigr).
\tag{5.1}
\]
This construction applies to any smooth nonzero section on its nonzero set. It has no field-equation requirement.

Since \(1-\chi(|v_j|^2)\) vanishes near every zero, the transgression localizes globally:
\[
c_2(E_j)[M_j]=
\int\chi(|v_j|^2)c_2(\mathbb F_j)
+\int d\chi(|v_j|^2)\wedge T_j.
\tag{5.2}
\]
On the transition region, the amplitude is uniformly bounded above and away from zero. Hence
\[
|c_2(E_j)[M_j]|
\le C\int_{B_j}
\bigl(|\mathbb F_j|^2+
|\mathbb F_j||\nabla v_j|^2+
|\nabla v_j|^4\bigr).
\tag{5.3}
\]
At the critical density, (1.7), (4.9), and Cauchy--Schwarz make the right side \(o(V_j)\). Thus
\[
\frac{c_2(E_j)[M_j]}{V_j}\longrightarrow0.
\tag{5.4}
\]

The unchanged bundle has the exact characteristic number
\[
c_2(E_j)[M_j]
=5\chi_j+6\tau_j+\frac94(a_j^2-T_{+,j}).
\tag{5.5}
\]
With the original condition \(a_j^2\ge T_{+,j}\) and \(s=-4\),
\[
\begin{split}
\frac{8\pi^2(5\chi_j+6\tau_j)}{V_j}
&=\fint\left(9|W_j^+|^2+|W_j^-|^2+\frac{10}{3}
-\frac52|\operatorname{Ric}^\circ_j|^2\right)\\
&\ge\frac{10}{3}-o(1).
\end{split}
\tag{5.6}
\]
Consequently
\[
\liminf_j\frac{c_2(E_j)[M_j]}{V_j}\ge\frac5{12\pi^2}>0,
\tag{5.7}
\]
contradicting (5.4). This closes the critical density case.

## 6. The argument gives a positive margin beyond \(3/8\)

This conclusion is stronger than merely adding the endpoint \(3/8\) to the previously proved strict range.

Suppose the same endpoint sequence has
\[
\nu=\limsup_j\fint|W_j^-|^2\le1.
\]
All torsion truncation and resolvent steps remain valid: none used small \(W^-\). The curvature error in (1.8) satisfies \(\limsup\mu_j\le C\nu\); all constants in the lemma are uniform for this bounded range. Since \(B_j\) has vanishing relative volume,
\[
\limsup_j\fint_{B_j}|\mathbb F_j|^2\le C\nu,\qquad
\limsup_j\fint_{B_j}|\nabla v_j|^4\le C\nu.
\tag{6.1}
\]
Equation (5.3) and Cauchy--Schwarz therefore give
\[
\limsup_j\frac{|c_2(E_j)[M_j]|}{V_j}\le C_*\nu.
\tag{6.2}
\]
Comparison with (5.7) yields a universal positive lower bound for \(\nu\). Applying the argument after passing to a subsequence realizing a liminf proves
\[
\boxed{\liminf_j\fint|W_j^-|^2\ge\nu_0>0}
\tag{6.3}
\]
for every hypothetical endpoint sequence; choose \(\nu_0\le1\) so that the case with liminf larger than \(1\) is automatic.

Finally, (1.5) and Gauss--Bonnet imply
\[
\liminf_j\frac{\chi_j}{A_j}
\ge\liminf_j\frac{\chi_j}{p_j}
\ge\frac38+\frac9{16}\nu_0.
\tag{6.4}
\]
Here \(\chi_j>0\) eventually, by the same Gauss--Bonnet identity. Choosing, for example, any
\[
0<\delta_0<\frac9{16}\nu_0
\]
rules out endpoints under \(\chi/A\le3/8+\delta_0\). Combined with the existing finite-parameter estimate, this gives a uniform O10 gap in that density range by the standard countersequence contradiction. The resulting constants are not claimed sharp or numerically evaluated.

## 7. Verification findings and precise scope

The proposed proof has no hidden use of local coordinate convergence or metric noncollapse:

1. The upper-amplitude cutoff is justified by testing the actual torsion equation; it is not assumed to preserve a small Dirac residual.
2. The \(H^{-1}\) estimate uses only pointwise Clifford contraction and the energy norm of the same connection.
3. The resolvent has a geometry-independent energy estimate and a unitary maximum-principle \(L^\infty\) bound.
4. The weighted Hessian argument differentiates neither curvature nor the bounded rough-Laplacian source after the displayed integration by parts.
5. The transgression uses the original bundle's topology and an arbitrary smooth replacement section. It does not assert that \(v_j\) is a new actual monopole or torsion section.
6. The critical result and the positive density margin retain the original \(a^2\ge T_+\) and actual-supply hypotheses.

The new proof removes the need to obtain regular charts in this density range. For larger Euler density the uncontrolled part of \(W^-\) can still carry a fixed fraction of the critical curvature and section-gradient energy. Equations (6.2)--(6.4) quantify that remaining obstruction; they do not eliminate it.

## 8. Any finite-density escape must contain a universal amount of Weyl concentration

There is a stronger consequence than the total-energy lower bound (6.3).
Assume a fixed finite Euler-density bound \(\chi/A\le B<\infty\). Then
\(\fint|W^-|^2\le C(B)\) along an endpoint sequence. Define its normalized concentration defect by
\[
\gamma_W=
\lim_{R\to\infty}\limsup_{j\to\infty}
\fint_{\{|W_j^-|>R\}}|W_j^-|^2.
\tag{8.1}
\]
The limit exists because the expression is decreasing in \(R\). With the bounded total energy, this is equivalently the limiting largest mass assignable to sets of vanishing relative volume.

The lemma in Section 4 can be sharpened to track the dependence on the bounded curvature model:
\[
I+J\le C_K A_w+C\mu V.
\tag{8.2}
\]
Here \(K\) bounds the curvature model, but \(\epsilon\) and the coefficient \(C\) of \(\mu\) are independent of \(K\). To check this, the differentiated-weight absorption uses only (4.3); the interpolation coefficient in (4.7) uses only \(\|v\|_\infty,\|Lv\|_\infty\); and the coefficients of \((|e|+|E|)q\) and \(|E|^2\) use only the same section bounds and dimension. The bounded curvature enters only the term \(C_K\int w(1+q)\). Therefore the choice of the Young parameter absorbing \(J\), and hence the coefficient of the squared curvature error, can be made before specifying \(K\).

Now put the part of \(W_j^-\) of amplitude at most \(R\) into the bounded curvature model, leaving its large-amplitude tail in the error. A smooth cutoff in \(|W^-|/R\) may be used; no derivative of that cutoff is needed. Then
\[
\limsup_j\mu_{j,R}
\le C\limsup_j\fint_{\{|W_j^-|>R\}}|W_j^-|^2.
\]
The unweighted bound (4.1) may depend on \(R\), which is harmless: first fix \(R\), then let the gradient cutoff \(L_0\to\infty\). The resulting small-set estimate has the uniform coefficient
\[
\limsup_j\fint_{A_j}|\nabla v_j|^4
\le C\limsup_j\fint_{\{|W_j^-|>R\}}|W_j^-|^2
\]
whenever \(\operatorname{Vol}(A_j)/V_j\to0\). Only after this limit is \(R\to\infty\). Thus
\[
\limsup_j\fint_{A_j}|\nabla v_j|^4\le C\gamma_W.
\tag{8.3}
\]
The same decomposition gives
\[
\limsup_j\fint_{A_j}|\mathbb F_j|^2\le C\gamma_W.
\tag{8.4}
\]
Apply (8.3)--(8.4) to the low-amplitude set \(B_j\) in Section 5. Its Chern localization gives
\[
\limsup_j\frac{|c_2(E_j)[M_j]|}{V_j}\le C_{\rm conc}\gamma_W.
\tag{8.5}
\]
The coefficient is universal and does not depend on the particular finite bound \(B\); \(B\) ensures the existence of the unweighted finite budgets and justifies the fixed-\(R\) limiting argument. Therefore
\[
\boxed{\gamma_W\ge
\frac{5}{12\pi^2 C_{\rm conc}}>0.}
\tag{8.6}
\]
In particular, O10 admits no finite-density endpoint sequence for which \(|W_j^-|^2\) is uniformly integrable relative to normalized volume.

This statement distinguishes energy from concentration. A large but bounded diffuse opposite Weyl tensor cannot enable endpoint escape: a fixed positive amount of its normalized energy must concentrate on sets of vanishing relative volume. The proof still does not provide the sharp coefficient \(1/(8\pi^2)\) in a comparison of concentrated Weyl energy with localized Chern charge.

## 9. A further finite-density consequence: the replacement has a strong radial derivative

For any fixed finite \(B\), (4.1) applies to \(v_j\), even without uniform integrability. Set \(a_j=|v_j|^2\) and \(q_j=|\nabla v_j|^2\). Since
\[
\Delta a_j=2\operatorname{Re}\langle L_jv_j,v_j\rangle-2q_j,
\]
the right side is bounded in normalized \(L^2\). Equation (3.5) and integration by parts show
\[
\fint|da_j|^2
=\fint(a_j-m_*)\Delta a_j\longrightarrow0.
\tag{9.1}
\]
Thus the resolvent does improve amplitude convergence to a strong \(L^2\) derivative statement. It does not follow that \(\nabla^2a_j\to0\) in \(L^2\), or that \(|da_j|^4\) is uniformly integrable; those would discard the concentration measured in Section 8.

## 10. Independent sign audit for the subsequent prolongation

This section checks two proposed continuations after the first actual Nijenhuis-bracket estimate. It does not modify the proved conclusions above.

In a frame adapted to the positive spinor and to \(v=\sqrt m\,e_1\), put
\[
Z_1=e_1-ie_2,\qquad Z_2=e_3-ie_4.
\]
The first bracket estimate leaves, up to small errors, only the horizontal component
\[
\nabla_1v=\nabla_2v=0,\qquad
\nabla_3v=(0,k),\quad \nabla_4v=(0,-ik).
\tag{10.1}
\]
The corresponding negative-spinor off-diagonal connection is
\[
b=(0,0,c,-ic),\qquad c=k/\sqrt m.
\]

For \(\Omega_-=e^{12}-e^{34}\), the negative Clifford matrices in the manuscript convention give
\[
c^-(\Omega_-)=2i\,\operatorname{diag}(1,-1),\quad
c^-(e^{13}+e^{24})=2C_3,\quad
c^-(e^{14}-e^{23})=2C_4.
\]
Differentiating \(c^-(\Omega_-)e_1=2ie_1\) yields
\[
\nabla\Omega_-
=2\operatorname{Im}b\otimes(e^{13}+e^{24})
-2\operatorname{Re}b\otimes(e^{14}-e^{23}).
\]
The \((1,0)\) vectors for this opposite structure are \(U_1=Z_1\), \(U_2=\overline Z_2\), and therefore
\[
(\nabla_XU_1)^{0,1}=-b(X)\overline U_2,\qquad
(\nabla_XU_2)^{0,1}=b(X)\overline U_1.
\]
Its Nijenhuis bracket is consequently
\[
[U_1,U_2]^{0,1}
=b(U_1)\overline U_1+b(U_2)\overline U_2
=2cZ_2.
\tag{10.2}
\]
It points in the \(Z_2\) direction, where the original positive spinor already has small derivative. It does **not** point in the \(\overline Z_1\) direction carrying the original nonzero derivative. A second copy of the same bracket argument therefore does not eliminate the remaining coefficient \(c\).

Likewise, the cubic opposite-spinor expression of \(v\) uses \(c^-(e_j)=-C_j^*\). Its components are
\[
t_v=m(-k_1+ik_2,\,-k_3-ik_4).
\]
Under (10.1), this is
\[
t_v=(0,-2mk),
\tag{10.3}
\]
aligned with the positive spinor direction orthogonal to \(\Phi\), not with \(\Phi\). The resulting bundle is \(S^+\otimes L^4\), with determinant \(9A\). Since
\[
c^+(F_A^+)=\operatorname{diag}(\rho,-\rho),
\]
its Lichnerowicz potential \(-1+\tfrac92c^+(F_A^+)\) tends to \(+5\) along \(\Phi\), but to \(-7\) along the actual direction (10.3). Thus the positive-potential argument cannot be applied to this cubic section.

## 11. Independent audit of the stronger \(50/3\) excess-energy theorem

**Later update, 2026-09-29.** I independently read Sections 6.1–8 of
\(\texttt{O10\_Strengthened\_Endpoint.md}\), including the inputs and proof order. The stronger theorem passes this audit. It supersedes the density threshold in Sections 1–6 above; those sections remain a valid shorter-dependency argument.

The audited argument assumes for contradiction only an endpoint sequence with
\(\limsup\fint|W^-|^2\le50/3\). This gives a bounded full connection-curvature \(L^2_{\rm avg}\) norm. The **unweighted** Hessian estimate therefore gives \(\nabla^2v\) bounded in \(L^2_{\rm avg}\) and \(\nabla v\) bounded in \(L^4_{\rm avg}\); it does not yet give uniform integrability.

The four particularly sensitive checks are as follows.

1. **The original type projection transfers to the resolvent section.** On \(\rho\ge c>0\), \(\|(\nabla v)^{1,0}_{J_+}\|_2\to0\) follows from the original full projection and \(v-\tau\to0\) in \(H^1_{\rm avg}\). The low-\(\rho\) region has vanishing relative volume, and its \(|\nabla v|^2\) integral vanishes by the already established \(L^4\) bound. Writing \(\alpha=\langle v,\nabla v\rangle=\frac12d|v|^2+ij_v\), its \((1,0)\) part controls \(j_v\) once \(d|v|^2\to0\) in \(L^2\). This is an algebraic decomposition, not a field equation for \(v\).

2. **The Hopf constants agree with the manuscript norm.** At \(v=\sqrt a(1,0)\), a variation \((x+iy,z+iw)\) has Hopf derivative squared norm \(a(x^2+z^2+w^2)/2\). Thus
   \[
   |Q_v|^2=a^2/8,\qquad
   |\nabla Q_v|^2=\frac a2|\nabla v|^2-\frac12|j_v|^2.
   \]
   The Hopf divergence identity uses the residual \(Dv\to0\), which is proved from the resolvent approximation; it does not require \(v\) to satisfy a monopole curvature equation. These identities give
   \[
   \fint|\nabla Q_v|^2\to m_*^2,\qquad
   \fint|Q_v|^2\to m_*^2/8.
   \]
   The ASD Bochner formula at scalar curvature \(-4\) consequently gives the pairing \(5m_*^2/12\).

3. **The spectral and polynomial-model normalizations are exact.** The mean Rayleigh value forced by that pairing is \(10/3\). A trace-free symmetric \(3\times3\) operator with that eigenvalue has minimum squared Hilbert--Schmidt norm
   \[
   \frac32(10/3)^2=\frac{50}{3}.
   \]
   With \(q_0^2=m_*^2/8\), the proposed polynomial model
   \[
   W_0=\frac5{q_0^2}
   \left(Q_v\otimes Q_v-\frac{|Q_v|^2}{3}I\right)
   \]
   has limiting eigenvalues \(10/3,-5/3,-5/3\). Directly,
   \[
   \fint|W_0|^2\to50/3,\qquad
   \fint\langle W^-,W_0\rangle
   =\frac5{q_0^2}\fint\langle W^-Q_v,Q_v\rangle\to50/3.
   \]
   Bounded amplitude of \(v\) justifies the required fourth moment of \(Q_v\), before any derivative uniform integrability is known. The upper energy hypothesis now forces \(\|W^--W_0\|_{2,\rm avg}\to0\).

4. **The final regularity and topology step is noncircular.** Only after this bounded full-Weyl fit has been proved does the slow-weight argument yield uniform integrability of \(|\nabla v|^4\). Chern localization then uses \(v\) solely as a smooth section of the unchanged bundle. Its topological limit is
   \[
   \frac{2(50/3)+20/3}{16\pi^2}=\frac5{2\pi^2}>0,
   \]
   contradicting the localized \(o(1)\) result. No actual equation has been assigned to the auxiliary section.

Finally,
\[
\frac{16}{9}\cdot\frac{39}{4}-\frac23=\frac{50}{3},
\]
so the stated Euler-density threshold and its existential positive extension are correct. The passage from sequence exclusion to a universal positive excess gap, and then to the original admissible metrics using the stated conformal comparison, preserves the quantifiers. The explicit topology-excess inequality also follows by the two density cases described in that file.

**Audit conclusion:** no algebraic, norm, equation-substitution, or regularity-circularity error was found in this new proof. Its precise conclusion retains either the opposite-Weyl energy excess or the corresponding Euler-density restriction; it does not establish unrestricted O10 after deleting both.
