# An opposite-chirality energy gap and O10 beyond the critical Euler density

2026-09-29. This argument uses the same actual constant-weight monopole and the previously established strong-current upgrade. Its primary conclusion is a universal energy gap involving the opposite Weyl chirality, with no Euler-density hypothesis. As a corollary, it excludes the critical density \(B=3/8\) and gives an absolute open interval above that threshold. It does not settle O10 for arbitrary bounded Euler density.

The new mechanism is to smooth a bounded truncation of the actual cubic torsion by the **rough-Laplacian resolvent on its own actual bundle**. The resulting section need not itself be a monopole or cubic torsion. It is used only as a section of that bundle in the Chern transgression. Its topology is consequently unchanged, while its bounded rough Laplacian makes a critical derivative estimate available.

## 1. Statement

Retain O10's actual conformal monopole supply, \(p\ge A>0\), and \(a^2\ge T_+\).

**Primary theorem.** There is an absolute \(\eta_*>0\) such that every actual scalar-minus-four input and every \(\beta\ge4\) satisfy

\[
 \boxed{\kappa_\beta+\beta^{-2}+\fint|W^-|^2\ge\eta_*,
 \qquad \kappa_\beta=P/V+D_\beta/V.}\tag{0}
\]

This statement imposes **no bound on \(\chi/A\)**. It says that approaching the weak zero endpoint forces a definite amount of opposite-chirality curvature.

**Density corollary.** There are absolute constants \(\delta_*>0\) and \(c_*>0\) such that, if

\[
 \frac{\chi(M)}A\le\frac38+\delta_*,
\]

then for every admissible metric and every \(\beta\ge2\),

\[
 \boxed{\fint|\operatorname{Ric}+g|^2+\frac{D_\beta}V
       \ge c_*\frac{(\beta-2)^2}{\beta^2}.}\tag{1}
\]

No pointwise curvature, diameter, Sobolev, noncollapse, volume, or injectivity-radius bound is added. The constants obtained here are existential absolute constants; no numerical value for \(\delta_*\) is asserted.

It is enough to prove the following sequence exclusion:

> There is no sequence of actual scalar-minus-four solutions satisfying the class-square condition, \(\beta_j\to\infty\), \(\kappa_j=P_j/V_j+D_{\beta_j}/V_j\to0\), and \(\fint|W_j^-|^2\to0\).

If (0) were false, choose inputs with its left side tending to zero. Nonnegativity of all three terms then forces exactly the excluded sequence. Thus (0) is equivalent to the needed sequential conclusion. Section 8 deduces (1), including the small open extension above \(3/8\).

## 2. Inputs from the actual endpoint system

All integral norms in this proof use \(dV/V\). Work with one actual solution

\[
 s=-4,\qquad D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),
 \qquad \rho=|\Phi|^2\le2.
\]

Write \(\tau=t_\Phi\in\Gamma(E)\), where \(E=S^-\otimes L\), and put

\[
 m=|\tau|^2,\quad \rho_*=4/3,\quad m_*=128/81,
 \quad S=m_*+2\rho^2|\nabla_A\Phi|^2,
 \quad Q=-iq_-(\tau),
\]

\[
 f=-iF_A^-,\qquad K=-\frac98\frac{\rho^3Q}{S}.
\]

The original manuscript proves \(|K|\le C\), \(f-K\to0\) in normalized \(L^2\), and the scalar/curvature/current budgets. The strong-current upgrade proved on 2026-09-29 additionally gives

\[
 \rho\to\rho_*\text{ in }L^2,\quad
 m\to m_*\text{ in }L^2,\quad
 D^-_{3A}\tau\to0\text{ in }L^2,\quad
 \|\nabla_{3A}\tau\|_2\le C.
\tag{2}
\]

The new dependencies are only the short chain

\[
 \text{slow truncation of }\nabla_A\Phi
 \Longrightarrow |\nabla_A\Phi|^4\text{ uniformly integrable}
 \Longrightarrow D\tau\to0\text{ in }L^2,\quad m\to m_*\text{ in }L^2.
\]

The original manuscript already supplies the bound on \(\nabla\tau\). No conclusion about \(d\gamma\), \(\nabla\zeta\), the full torsion projection \(N\), or the precise limit of \(\fint|\nabla\tau|^2\) is used. The short chain does not assume the Euler-density restriction being proved here, so the argument is not circular.

Let \(D=D^-_{3A}\). Its Lichnerowicz potential is

\[
 D^*D=T+\mathcal V,\quad
 T=\nabla_{3A}^*\nabla_{3A},\quad
 \mathcal V=-I+\frac32c(F_A^-).
\tag{3}
\]

The connection curvature of \(E\) is

\[
 F^E=F^{S^-}_{\rm LC}+\frac32F_A I.
\]

Under the additional contradictory assumption \(\|W^-\|_2\to0\), it has a decomposition

\[
 F^E=F_0+\mathcal E_F,\qquad |F_0|\le C,
 \qquad\|\mathcal E_F\|_2\to0.\tag{4}
\]

Indeed keep the scalar curvature block, the bounded actual \(F_A^+\), and the bounded ASD model \(iK\) in \(F_0\). The remaining blocks are \(W^-\), trace-free Ricci, and \(f-K\). No derivative of any of these quantities is required. This is precisely where the critical-density argument is stronger than the arbitrary-density case.

## 3. A bounded truncation with small Dirac residual

Fix \(L>m_*\). Choose a smooth nondecreasing \(\varphi\), zero for \(m\le L\), one for \(m\ge2L\), with \(m\varphi'\) bounded. Test (3) against \(\varphi(m)\tau\). The exact identity is

\[
 \int\varphi|\nabla\tau|^2+
 \frac12\int\varphi'|dm|^2
 =\int\varphi|D\tau|^2+
 \int\operatorname{Re}\langle D\tau,c(d\varphi)\tau\rangle
 -\int\varphi\langle\mathcal V\tau,\tau\rangle.
\tag{5}
\]

The mixed term is bounded by

\[
 \frac14\int\varphi'|dm|^2+
 C\int m\varphi'|D\tau|^2.
\]

The potential term tends to zero after division by \(V\). For its bounded-model part, \(m\to m_*\) in \(L^2\) and \(L>m_*\) imply \(\fint_{m>L}m\to0\). Its remaining part is bounded by
\(C\|f-K\|_{2,\rm avg}\|m\|_{2,\rm avg}\to0\). Thus (2) and (5) give

\[
 \fint_{m\ge2L}|\nabla\tau|^2\longrightarrow0.
\tag{6}
\]

Choose a smooth radial cap \(b(m)\) equal to one on \([0,2L]\), equal to a fixed constant times \(m^{-1/2}\) above \(3L\), and with \(|b|+m|b'|\le C_L\). Set

\[
 u=b(m)\tau.
\]

This is a globally smooth section, uniformly bounded in norm. Equations (2), (6) and the product rule give

\[
 \|u-\tau\|_{2,\rm avg}+\|\nabla(u-\tau)\|_{2,\rm avg}\to0,
 \qquad \|Du\|_{2,\rm avg}\to0,
 \qquad |u|^2\to m_*\text{ in }L^2_{\rm avg}.
\tag{7}
\]

The stronger last assertion also follows directly from boundedness of \(u\), (2), and convergence in measure.

## 4. The potential acts on this bounded section as \(-2\)

The cap \(u\) is collinear with \(\tau\). The exact Hopf identity
\(c(q_-(\tau))\tau=(m/2)\tau\) implies

\[
 \left[-I+\frac32c(iK)\right]u
 =-\left(1+\frac{27}{32}\frac{\rho^3m}{S}\right)u.
\tag{8}
\]

The displayed coefficient is uniformly bounded, because \(m\le S\) and \(\rho\le2\). By the actual calibration and (2), it tends in measure to

\[
 1+\frac{27}{32}\frac{\rho_*^3}{2}=2.
\]

Boundedness of \(u\), together with \(f-K\to0\) in \(L^2\), therefore gives

\[
 \boxed{\|(\mathcal V+2I)u\|_{2,\rm avg}\to0.}\tag{9}
\]

Equations (3), (7), and (9) say that \(Tu-2u\) tends to zero in the actual normalized \(H^{-1}\) norm. This negative-norm statement is used only in the following coercive resolvent equation.

## 5. Rough-Laplacian resolvent: bounded forcing and strong \(H^1\) approximation

Define, on each actual closed manifold and bundle,

\[
 v=3(I+T)^{-1}u.
\tag{10}
\]

The positive operator \(I+T\) is invertible on a closed manifold. The connection-Laplacian maximum principle (or its scalar Kato inequality) gives

\[
 \|v\|_\infty\le3\|u\|_\infty.
\tag{11}
\]

In particular \(v\) is a smooth bounded section and

\[
 Tv=3u-v=:h,\qquad \|h\|_\infty\le C.
\tag{12}
\]

Put \(z=v-u\). From (3),

\[
 (I+T)z=2u-Tu=-D^*Du+(\mathcal V+2I)u.
\]

Pair with \(z\). Since pointwise \(|Dz|\le2|\nabla z|\),

\[
 \|z\|_{2,\rm avg}^2+\|\nabla z\|_{2,\rm avg}^2
 \le2\|Du\|_{2,\rm avg}\|\nabla z\|_{2,\rm avg}
 +\|(\mathcal V+2I)u\|_{2,\rm avg}\|z\|_{2,\rm avg}.
\]

Thus

\[
 \boxed{\|v-u\|_{H^1_{\rm avg}}\to0,\qquad
               |v|^2\to m_*\text{ in }L^2_{\rm avg}.}\tag{13}
\]

The same equations give the stronger residuals

\[
 \|Dv\|_{2,\rm avg}\to0,\qquad
 \|Tv-2v\|_{2,\rm avg}=3\|u-v\|_{2,\rm avg}\to0.\tag{13a}
\]

The first follows from \(v-u\to0\) in \(H^1\) and \(Du\to0\); the second is the exact resolvent equation. These are valid even at arbitrary fixed Euler density. The rough-Laplacian residual is genuinely \(L^2\), rather than only \(H^{-1}\).

No spectral gap for \(T\) was used; the identity term in its resolvent supplies a universal coercivity constant. No derivative of \(Du\), of Ricci, or of bundle curvature was estimated.

## 6. Bounded rough Laplacian suffices for critical gradient control

We record the exact extension of the slow-truncation lemma used here. Let \(v\) be a smooth bounded section with bounded \(h=\nabla^*\nabla v\). Suppose Ricci and bundle curvature are each a uniformly bounded tensor plus an error whose normalized \(L^2\) norm tends to zero. Then, for some fixed \(\epsilon>0\),

\[
 \fint\left(\frac{|\nabla v|^2}{R^2+|\nabla v|^2}\right)^\epsilon
       \bigl(|\nabla^2v|^2+|\nabla v|^4\bigr)
 \le CR^{-2\epsilon}+o(1),\quad R\ge1.
\tag{14}
\]

In particular \(|\nabla v|^4\) is uniformly integrable relative to normalized volume.

### Proof of the extension

Put \(P=\nabla v\), \(H=\nabla P\), \(q=|P|^2\), and use

\[
 w=\left(\frac{q+\delta}{R^2+q+\delta}\right)^\epsilon,
 \quad |dw|\sqrt q\le2\epsilon w|H|.
\]

The derivative-free Hessian interchange starts with

\[
 \int w|H|^2
 =\int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
      +\frac12\int w\sum_{i,j}|F_{ij}v|^2.
\]

Integrating once and commuting derivatives on the covector-valued \(P\) produces the potential term \(\int w\langle P,\nabla h\rangle\), the Ricci and connection-curvature pairings with \(P^2\), and the weight derivative. Integrate this potential term once more:

\[
 \int w\operatorname{Re}\langle P,\nabla h\rangle
 =\int w|h|^2-\int\operatorname{Re}\langle dw\otimes P,h\rangle.
\tag{15}
\]

Boundedness of \(h\), the displayed weight derivative estimate, and Young's inequality absorb the resulting \(C\epsilon\int w|H|\) term into a small multiple of \(\int w|H|^2\) plus \(C\int w\). The weighted bounded-section interpolation remains

\[
 \int wq^2\le C\int wq+C\int wq|H|
 \le C_1\left(\int w|H|^2+\int wq\right).
\tag{16}
\]

The curvature errors pair with \(wq\); Young gives a small multiple of \(\int wq^2\) plus the normalized curvature-error squares. Thus the two inequalities jointly give

\[
 \int w(|H|^2+q^2)\le C\int w(1+q)+o(V).
\tag{17}
\]

First take \(w=1\). Since \(\int q=\int\langle v,h\rangle\le CV\), this proves the uniform fourth-power gradient and Hessian budget. Next use the displayed slow weight: \(w\le R^{-2\epsilon}(q+\delta)^\epsilon\), and the budget controls the average of \((q+\delta)^\epsilon(1+q)\) for \(\epsilon\le1\). Let \(\delta\downarrow0\). This proves (14). The proof uses bounded \(h\), not its derivative.

Apply the lemma to (4), (11), and (12). Its Ricci hypothesis follows from \(\operatorname{Ric}=-g+o_{L^2_{\rm avg}}(1)\).

## 7. The Chern transgression now has vanishing normalized cost

Choose \(d>0\) with \(4d^2<m_*\). The standard rank-two transgression applied to \(v/|v|\), with a smooth amplitude cutoff equal to one near zero and zero above \(2d\), gives

\[
 |c_2(E)[M]|
 \le C_d\left[
 \int_{\{|v|<2d\}}|F^E|^2+
 \int_{\{d<|v|<2d\}}|\nabla v|^4\right].
\tag{18}
\]

The cutoff vanishes before any division by \(|v|\) is made at a zero, so this is a global identity/estimate with all zero-set flux retained. It does not require transverse zeros.

By (13), both sets in (18) have relative volume tending to zero. The curvature squares are uniformly integrable by (4). The derivative fourth powers are uniformly integrable by (14). Divide (18) by \(V\):

\[
 \boxed{c_2(E)[M]/V\longrightarrow0.}\tag{19}
\]

On the other hand, the actual Chern--Weil formula is

\[
 16\pi^2\frac{c_2(E)[M]}V
 =\fint\left[
 2|W^-|^2+\frac{s^2}{24}
 -\frac12|\operatorname{Ric}^{\circ}|^2
 +9|F_A^+|^2-9|F_A^-|^2\right].
\]

The actual endpoint limits are
\(\fint|F_A^+|^2\to8/9\),
\(\fint|F_A^-|^2\to2/9\),
\(s=-4\), \(\fint|\operatorname{Ric}^{\circ}|^2\to0\), and the present assumption is \(\fint|W^-|^2\to0\). Therefore

\[
 \boxed{\frac{c_2(E)[M]}V\longrightarrow
                   \frac{5}{12\pi^2}>0.}\tag{20}
\]

Equations (19) and (20) contradict each other. This proves the sequence exclusion.

The auxiliary section \(v\) need not retain the actual cubic definition. Its sole role in (18) is as a genuine section of the same bundle \(E\). The actual field equations have already supplied its bounded approximate eigenmode \(u\), while the resolvent supplies the critical regularity. No field has been substituted into a monopole equation that it does not satisfy.

## 8. From sequence exclusion to a larger density interval and all parameters

The preceding proof establishes (0): otherwise choose a sequence whose three nonnegative summands tend to zero and apply Sections 2--7. In particular, whenever \(\kappa_\beta+\beta^{-2}\le\eta_*/2\), one has \(\fint|W^-|^2\ge\eta_*/2\). This is the direct mechanism behind the density extension.

Chern--Gauss--Bonnet and the same-solution amplitude/Hodge bounds give, under \(\chi/A\le B\),

\[
 \limsup\fint|W^-|^2\le\frac{16B}{9}-\frac23.
\tag{21}
\]

In particular no endpoint sequence exists at \(B=3/8\). There must also be some absolute \(\delta_*>0\) for which none exists under \(B\le3/8+\delta_*\). A direct diagonal proof avoids assigning an unsupported explicit value: if all such intervals failed, choose a violating endpoint sequence with \(B_n\le3/8+1/n\), then choose its parameter/error far enough along so that \(\beta_n\to\infty\), \(\kappa_n\to0\), and (21)'s finite-error terms tend to zero. This gives \(\fint|W_n^-|^2\to0\), already excluded.

For this fixed density interval, failure of an all-parameter scalar-minus-four estimate would produce \(\kappa_j\beta_j^2/(\beta_j-2)^2\to0\). The existing finite-parameter theorem, with class-square cost removed, rules out bounded \(\beta_j\); hence \(\beta_j\to\infty\) and \(\kappa_j\to0\), contradicting the established endpoint exclusion. Thus the scalar-minus-four version of (1) holds.

Finally the existing conformal comparison

\[
 \widehat\kappa\le\frac{\kappa}{1-\sqrt\kappa-\kappa/16}
\]

transfers it to every original admissible metric. For \(\kappa<1/16\) the denominator is larger than \(1/2\); for \(\kappa\ge1/16\) the desired estimate is immediate after reducing its constant. The actual class, its square, \(p\), and \(\chi/A\) are preserved in that comparison. This completes (1).

## 9. Exact advance and remaining boundary

The earlier result covered only \(B<3/8\). This proof reaches \(B=3/8\) and an absolute nonzero interval above it, by supplying a new global regularized-section mechanism. It uses information absent from the local hyperbolic core examples: a global bounded approximate eigensection on the actual closed bundle and a full bundle-curvature fit.

For arbitrary fixed \(B\), \(W^-\) is bounded in normalized \(L^2\) but need not be a small error or have uniformly integrable square. Then (4), and hence the strong critical estimate (14) with a vanishing error, is unavailable. Merely retaining an \(O(B)\) right side does not make (18) vanish on a small-volume set. That is the remaining restriction of this proof; it is not silently removed.


### The precise unresolved signed estimate at arbitrary fixed density

Even without small opposite-Weyl energy, bounded \(B\) gives a global normalized \(H^2\) budget for \(v\), a normalized \(L^4\) budget for \(\nabla v\), and (13a). Since \(v\) is bounded and

\[
 \Delta|v|^2=2\operatorname{Re}\langle v,Tv\rangle-2|\nabla v|^2,
\]

the Laplacian of its squared amplitude has a bounded normalized \(L^2\) norm. Integration by parts against \(|v|^2-m_*\to0\) in \(L^2\) gives \(d|v|^2\to0\) in normalized \(L^2\). This is still insufficient at the critical fourth-power scale.

To state the missing estimate without hiding boundary terms, choose a fixed smooth amplitude cutoff \(\vartheta\), zero near \(v=0\) and one for \(|v|\ge2d\), and let \(\chi=1-\vartheta^2\). Write \(\mathcal T_v\) for the exact rank-two transgression of \(v/|v|\), with the sign convention of the original manuscript. The globally valid localization identity is

\[
 16\pi^2\int d\chi\wedge\mathcal T_v
 =2\int\vartheta^2|W^-|^2+\int\vartheta^2 k,
 \quad k=9(|F_A^+|^2-|F_A^-|^2)+s^2/24-|\operatorname{Ric}^{\circ}|^2/2.
\]

The endpoint budgets imply \(\fint\vartheta^2 k\to20/3\). Hence a sufficient further theorem would be the signed estimate

\[
 16\pi^2\int d\chi\wedge\mathcal T_v
 \le2\int\vartheta^2|W^-|^2+o(V).
\tag{22}
\]

It would immediately contradict the positive bulk limit. It would also supply the sharp concentration-charge comparison with coefficient \(1/(8\pi^2)\). We have **not** proved (22). The exact transgression contains the critical products \(d\vartheta\,\nabla(v/|v|)F^E\) and \(d\vartheta\,|\nabla(v/|v|)|^3\); the available normalized \(L^2\) amplitude-gradient convergence and \(L^4\) full-gradient bound do not make their integrals vanish. Applying Young inequalities produces a nonsharp curvature coefficient. The previous signed-square completion cancels the same bulk term through scalar and central-curvature identities and therefore does not prove (22). The new residuals (13a) remain a concrete additional input for this further problem; a bubble decomposition or loss-free boundary framing has not been assumed.
