# Focused verification bundle for Step 72

## Conventions and target

For a closed oriented four-manifold, let
\[
P=\int|\operatorname{Ric}^\circ|^2,\quad S=\int s^2,\quad
T_s=\int s,\quad V=\operatorname{Vol},\quad R=\int|\operatorname{Ric}|^2=P+S/4,
\]
\[
L_s=S-T_s^2/V,\qquad \mathcal W=\int|W|^2,
\qquad \mathcal E=\inf_{\lambda\ne0}\frac{\int|\operatorname{Ric}-\lambda g|^2}{\lambda^2V}
=\frac{4P+L_s}{R}\quad(R>0).
\]
Curvature convention:
\[
8\pi^2\chi=\mathcal W+S/24-P/2,
\quad 12\pi^2\tau=\int(|W^+|^2-|W^-|^2).
\]

## Claims to check

Gauss–Bonnet gives
\[
P=S/12+2\mathcal W-16\pi^2\chi,
\quad R=S/3+2\mathcal W-16\pi^2\chi,
\]
and hence
\[
\tag{A}\mathcal E-1=\frac{6(\mathcal W-8\pi^2\chi)+L_s}{R}.
\]
Define \(d([g])=8\pi^2\chi-\mathcal W([g])\), conformally invariant in dimension four.

Every conformal class has a Yamabe representative \(\widehat g\), with constant scalar curvature and \(S(\widehat g)=Y([g])^2\). At that metric,
\[
\tag{B}R(\widehat g)=P(\widehat g)+Y^2/4
=Y^2/3+2\mathcal W-16\pi^2\chi,
\quad \mathcal E(\widehat g)=1-6d/R(\widehat g).
\]
If some metric has \(\mathcal E<1\), (A) gives \(d>0\). A conformal class with \(d>0\) cannot have \(Y=0\): its scalar-flat Yamabe metric would satisfy \(P=2\mathcal W-16\pi^2\chi=-2d<0\). Conversely, if a class has \(d>0\), its Yamabe representative has \(Y\ne0\) and (B) gives \(\mathcal E<1\). Thus
\[
\tag{C}\alpha<1\iff\exists[g]:Y([g])\ne0,\ \mathcal W([g])<8\pi^2\chi.
\]
Because the dumbbell below gives \(\alpha\le1\), this implies
\[
\tag{D}\alpha=1-6\max\left\{0,\sup_{[g]:Y\ne0}\frac{d([g])}{P(\widehat g)+Y^2/4}\right\}.
\]
Please check whether any class with \(Y=0\), any non-Yamabe representative, or \(R=0\) invalidates (C) or (D).

## Dumbbell construction

Choose a smooth warped metric \(dr^2+f(r)^2g_{S^3(1)}\) on \(S^4\) with two fixed caps and a cylinder \([0,L]\times S^3(1)\). One may use \(f=\sin r\) near each pole and a fixed smooth interpolation to \(f=1\); all cap integrals are independent of \(L\). Such a one-dimensional warped product with space-form fiber is conformally flat. On the cylinder
\[
\operatorname{Ric}=(0,2,2,2),\ s=6,\ |\operatorname{Ric}^\circ|^2=3,
\ |\operatorname{Ric}|^2=12,
\]
so
\[
P=6\pi^2L+O(1),\quad R=24\pi^2L+O(1),\quad L_s=O(1).
\]
Replace a fixed ball in one cap by a fixed punctured/rescaled metric on arbitrary closed \(M\), through a fixed neck. Since \(M\#S^4\cong M\), this gives metrics on \(M\); all changes in \(P,R,S,T_s,V\) are \(O(1)\) independent of \(L\). Hence \(\mathcal E\to1\) and
\[
\tag{E}\alpha(M)\le1\quad\text{for every closed four-manifold}.
\]
Combined with the chiral lower bound for \(T_{\min}=2\chi-3|\tau|\le0\), this gives \(\alpha=1\). At strict inequality no metric attains one; at equality, attainment is equivalent to a half-conformally-flat conformal class with nonzero Yamabe constant.

## Connected-sum deficit

Set \(\mathcal W_*(M)=\inf_g\mathcal W(g)\), \(d_*(M)=8\pi^2\chi(M)-\mathcal W_*(M)\). Kobayashi subadditivity says
\[
\mathcal W_*(M\#N)\le\mathcal W_*(M)+\mathcal W_*(N).
\]
Since \(\chi(M\#N)=\chi(M)+\chi(N)-2\),
\[
\tag{F}d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.
\]
In the session norm, signature gives \(\mathcal W_*(\overline{\mathbb{CP}}^2)=12\pi^2\), so \(d_*=12\pi^2\). Therefore
\[
d_*(\#_n\overline{\mathbb{CP}}^2)\ge(16-4n)\pi^2.
\]
For \(n\le3\), positive deficit plus (C) gives \(\alpha<1\); for \(n\ge4\), \(T_{\min}=4-n\le0\) and (E) give \(\alpha=1\).

For a minimal negative Kähler–Einstein general-type surface with \(A=c_1^2>0\), its Einstein metric has \(d=R/6=4\pi^2A/3\) in the session normalization. Iterating (F) with \(\overline{\mathbb{CP}}^2\) gives
\[
 d_*(X\#k\overline{\mathbb{CP}}^2)\ge4\pi^2(A/3-k),
\]
so \(k<A/3\Rightarrow\alpha<1\). In the band \(A/3\le k<A\), (C) reduces \(\alpha<1\) to
\[
\inf\mathcal W<8\pi^2\chi.
\]
Using signature and \(\tau(X\#k\overline{\mathbb{CP}}^2)=(A-2\chi(X))-k\), the claimed equivalent inequality in the session endomorphism norm is
\[
\tag{G}\inf_g\int|W^+|^2<2\pi^2(A-k).
\]
Please check all constants in (F)–(G), noting that some literature uses the (0,4)-tensor norm four times the session endomorphism norm.
