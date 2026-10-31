# Exact relative conformal energy on the ordinary Eguchi--Hanson quotient

Date: 2026-10-11. This computes a complete, compactly supported conformal comparison, including the cutoff annulus. Its background metrics are Ricci-flat; it is not the complete desingularization expansion of a prescribed non-Einstein P-critical orbifold.

## 1. Metric, mode and normalization

Use the Eguchi--Hanson length normalization in which the bolt occurs at r=1:

\[
G(r)=1-r^{-4},\qquad
 g_{\rm EH}=G^{-1}dr^2+\frac{r^2}{4}
 (\sigma_1^2+\sigma_2^2+G\sigma_3^2).
\]

Take the ordinary free quotient with asymptotic link S³/Z₄ and write

\[
V_\Gamma=\operatorname{Vol}(S^3/\mathbb Z_4)=\frac{\pi^2}{2}.
\]

The radial volume measure is r³dr times the unit-link measure, exactly as on the flat cone. Choose the descending perpendicular harmonic quadratic mode supplied by the Gibbons--Hawking rotation, written in the Hopf-angle convention as

\[
q_{\rm EH}(r,\Omega)=A(r)Y(\Omega),\quad A(r)=\sqrt{r^4-1},
\qquad q_0(r,\Omega)=r^2Y(\Omega),\qquad \fint Y^2=\frac13.
\]

Here Y is the perpendicular mode (in the convention of the companion singular-core calculation, Y=sinθ cosψ, with ψ the squashed Hopf angle). The invariant statement is that q_EH is a descending smooth harmonic quadratic-growth function, and q_0 is its leading flat harmonic polynomial. The formula is not valid with an arbitrary angular function or after silently interchanging φ and ψ.

Fix a smooth radial profile χ with χ=1 for ρ≤1 and χ=0 for ρ≥Λ, Λ>1. Put

\[
f_{{\rm EH},R}=\chi(r/R)q_{\rm EH},\qquad
f_{0,R}=\chi(r/R)q_0.
\]

These are compactly supported and smooth on their respective complete quotient/orbifold spaces.

## 2. Exact P formula for compactly supported conformal changes

For a Ricci-flat four-metric g and a compactly supported smooth f, curvature normalization P=∫|Ric°|² gives

\[
\boxed{P(e^{2tf}g)=3\int_M\bigl(t\Delta f+t^2|df|^2\bigr)^2dV_g.}\tag{1}
\]

Here Δ=div grad. Indeed s_{e^{2tf}g}=e^{-2tf}(-6tΔf-6t²|df|²). The scalar-square integral is therefore 36 times the integral on the right. Weyl energy is conformally invariant; the Chern--Gauss--Bonnet boundary terms are unchanged because the conformal change is compactly supported. Thus P(e^{2tf}g)-P(g)=S(e^{2tf}g)/12, while P(g)=0.

Let a_R(g,f)=3∫(Δf)² be the coefficient of t² in (1). The Hessian itself is 2a_R=6∫(Δf)². Distinguishing the coefficient from the Hessian avoids a factor-of-two error.

## 3. The full relative quadratic coefficient

Because q_EH is harmonic,

\[
\Delta_{\rm EH}(\chi q_{\rm EH})
=\left[A G\,\chi_{rr}+A(7/r+r^{-5})\chi_r\right]Y.\tag{2}
\]

This follows from Δχ=Gχ_rr+(3/r+r^{-5})χ_r and A'=2r/√G. Write ρ=r/R, and primes below mean differentiation in ρ. Then

\[
L_0=\rho^2\chi''+7\rho\chi',
\]

\[
\Delta_{\rm EH}f_{{\rm EH},R}
=\left[L_0+R^{-4}
 \left(-\frac32\rho^{-2}\chi''-\frac52\rho^{-3}\chi'\right)
 +O_\chi(R^{-8})\right]Y.
\]

The flat Laplacian is precisely L_0Y. Both Laplacians vanish in the inner region; consequently all of (1)'s quadratic energy is in the annulus R≤r≤ΛR. Using the exact volume equality and ∫Y²=VΓ/3 yields

\[
\begin{aligned}
\lim_{R\to\infty}\left[
\int|\Delta_{\rm EH}f_{{\rm EH},R}|^2-
\int|\Delta_0f_{0,R}|^2\right]
&=\frac{V_\Gamma}{3}\int_1^\Lambda
  \left[-3\rho^3(\chi'')^2-26\rho^2\chi''\chi'-35\rho(\chi')^2\right]d\rho\\
&=-V_\Gamma\int_1^\Lambda
 \left[\rho^3(\chi'')^2+3\rho(\chi')^2\right]d\rho.
\end{aligned}\tag{3}
\]

The last step uses ∫ρ²χ''χ'=-∫ρ(χ')² and χ'=0 at the endpoints. Define the positive quantity

\[
J_\chi=\int_1^\Lambda\left[\rho^3(\chi'')^2+3\rho(\chi')^2\right]d\rho.
\]

The exact comparison of quadratic coefficients is consequently

\[
\boxed{\lim_{R\to\infty}(a_R^{\rm EH}-a_R^0)=-3V_\Gamma J_\chi<0.}\tag{4}
\]

The corresponding Hessian difference is -6VΓ Jχ. At general bolt scale a, the relative coefficient has the prefactor a⁴ after matching the same homogeneous quadratic mode.

This establishes that the full cutoff-conformal comparison has a negative relative coefficient. It is not correct to claim that every negative inner term must automatically cancel to zero. Nor can (4) alone be identified with the invariant coefficient for a fixed P-critical compact bulk.

## 4. How the inner Hessian finite part relates to (4)

For the uncut harmonic mode one has

\[
\fint |dq_{\rm EH}|^2=4r^2-\frac{4}{3r^2}.
\]

Ricci-flat Bochner and the exact radial boundary measure give

\[
\int_{r<R}|\nabla^2q_{\rm EH}|^2
=V_\Gamma\left(4R^4-\frac83-\frac4{3R^4}\right).
\]

The lower endpoint r=1 contributes zero. On the flat cone the integral is 4VΓR⁴. Hence the renormalized Hessian integral is -8VΓ/3. Since DE[2qg]=-2Hess q for harmonic q, the inner relative coefficient of ∫|DE|² is -32VΓ/3.

The cutoff-annulus contribution is indispensable: after it is included the full coefficient is (4), not -32VΓ/3. Its value depends on χ.

## 5. Logarithmic cutoff dependence

Set x=logρ, L=logΛ and u(x)=χ(e^x). Then

\[
\boxed{J_\chi=\int_0^L\left[(u'')^2+4(u')^2\right]dx.}\tag{5}
\]

The boundary conditions are u(0)=1, u(L)=0 and u'(0)=u'(L)=0. In particular Jχ≥4/L by Cauchy--Schwarz. Conversely, for any fixed smooth profile ψ that is flat near 0 and 1, setting u_L(x)=ψ(x/L) gives

\[
J_{\chi_L}=L^{-3}\int_0^1(\psi'')^2+4L^{-1}\int_0^1(\psi')^2\longrightarrow0.
\]

Thus (4) is genuinely cutoff-dependent and approaches zero for a sufficiently long gentle cutoff. The order of limits is first R→∞ for each fixed profile, then L→∞; no uniform simultaneous-limit assertion is needed.

## 6. Exact scope of the result

The comparison is between conformal perturbations of two Ricci-flat backgrounds. The flat-cone conformal metric with compact cutoff is generally not P-critical. For a prescribed compact P-critical orbifold, a complete gluing expansion also includes its nonconformal curvature jet, the ALE metric's order-r^{-4} tail, the matched order-r^{-2} correction, and the outer first-variation boundary pairing. Formula (4) does not contain those terms.

Therefore this calculation neither proves nor disproves strict improvement below the orbifold minimum. It replaces an isolated inner-energy estimate by the full cutoff-conformal relative energy, and determines exactly which quantity is negative and which dependence remains to be removed in the compact critical-bulk calculation.
