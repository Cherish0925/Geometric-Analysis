# Global energy and boundary geometry of the complete Bianchi VIII example

8 October 2026. Continuation of the user's A01 construction; not a new construction and not a solution of the closed Goldberg problem.

## Scope and inherited input

Use the smooth complete disk-bundle quotient in Section 2 of `upload/03_Subsequent_Mathematical_Developments.tex`, with base a compact hyperbolic surface of genus \(g\ge2\). Its metric and almost-Kähler form satisfy
\[
\operatorname{Ric}=-3g,\qquad W^-=0,\qquad d\Omega=0,
\qquad |\Omega|^2=2,\qquad
q:=|\nabla\Omega|^2={36(1-x^2)^3\over(1+3x^2)^3},
\quad \tfrac13\le x<1.
\]
Write \(V_\Gamma=\int_{\Gamma\backslash\mathrm{SL}(2,\mathbb R)}\sigma_{123}
=2\pi^2(g-1)\). The source already proves
\[
\int q\,dV=64V_\Gamma,\qquad
\int q^2\,dV={512\over3}V_\Gamma.
\]
These two integrals are inherited and must not be registered as new results. The finite integrals concern this compact-base disk bundle, not the simply connected \(\mathbb R^4\) cover, whose invariant orbit volume is infinite.

The new calculation below identifies the entire integrability threshold, computes an absolutely convergent curvature-density defect, and gives the exact boundary contribution explaining why finite almost-Kähler energy does not reproduce the closed topological obstruction.

## 1. A curvature-adapted radial coordinate

Set
\[
t={1-x^2\over1+3x^2},\qquad 0<t\le\tfrac23.
\]
Then
\[
x^2={1-t\over1+3t},\qquad q=36t^3,
\qquad dV={8\over3}t^{-3}|dt|\wedge\sigma_{123}.
\tag{1}
\]
The last formula follows directly from the source volume density
\[
{64x(1+3x^2)\over3(1-x^2)^3}\,dx\wedge\sigma_{123}
\]
and \(dt/dx=-8x/(1+3x^2)^2\). This variable is intrinsic to the metric-form pair because \(t=(q/36)^{1/3}\).

For any \(a>2/3\), therefore,
\[
\boxed{\int q^a\,dV={8\over3}36^a V_\Gamma
{(2/3)^{3a-2}\over3a-2}.}
\tag{2}
\]
The integral diverges for \(a\le2/3\). Equivalently,
\[
\boxed{\nabla\Omega\in L^p\ \Longleftrightarrow\ p>4/3}
\tag{3}
\]
for finite positive \(p\). It is bounded as well. At the endpoint \(p=4/3\), it belongs to weak \(L^{4/3}\), because for \(0<\lambda<\sqrt{32/3}\),
\[
\operatorname{Vol}\{|\nabla\Omega|>\lambda\}
={4\over3}V_\Gamma
\left(36^{2/3}\lambda^{-4/3}-{9\over4}\right).
\tag{4}
\]

Thus completeness, bounded curvature, and finite \(L^p\) torsion for all \(p>4/3\), including the quadratic and quartic torsion integrals, are compatible with strict nonintegrability. This is a precise counterexample to an integrability assertion based only on those properties. No existing theorem is claimed to assert that false implication.

## 2. Finite torsion does not control normalized torsion

The inverse radial metric gives the exact identity
\[
|dt|^2=t^2K(t),\qquad K(t)=(t-1)(3t-2)(3t+1)>0
\quad(0<t<2/3).
\tag{5}
\]
Consequently
\[
\boxed{|d\log q|^2=9K(t)\longrightarrow18\quad(t\downarrow0).}
\tag{6}
\]
In particular \(d\log q\) lies in no finite \(L^p\). The torsion itself tends to zero and has finite energy, while the logarithmic derivative of its amplitude does not decay. A proof involving division by the torsion amplitude must therefore establish its cancellations or estimates separately. Formula (6) does not by itself compute the covariant derivative of the normalized Nijenhuis tensor: radial amplitude terms can cancel when a section is normalized.

Here and below \(\Delta=\operatorname{div}\nabla\), the nonpositive spectral convention. For a radial function \(f(t)\),
\[
\Delta f={t^3\over1}\,{d\over dt}
\left(t^{-1}K(t)f'(t)\right).
\tag{7}
\]
For the compact domain \(M_\epsilon=\{t\ge\epsilon\}\), including the smooth zero section, the outward boundary flux is
\[
\int_{M_\epsilon}\Delta f\,dV
=-{8\over3}V_\Gamma\epsilon^{-1}K(\epsilon)f'(\epsilon).
\tag{8}
\]
There is no inner boundary at the bolt. In particular,
\[
\Delta(t^2)=2t^3(27t^2-24t+1),\qquad
\boxed{\int_M\Delta(t^2)\,dV=-{32\over3}V_\Gamma.}
\tag{9}
\]
The Laplacian in (9) is absolutely integrable; nevertheless its integral is nonzero. There is no contradiction with complete-manifold Stokes theorems: \(d(t^2)\notin L^1\). More generally, \(d(t^a)\in L^1\) exactly when \(a>2\); its total flux tends to zero in that range. In particular \(q=36t^3\) has zero total Laplacian flux, while normalization involving smaller powers need not.

This distinguishes two separate issues. The ordinary \(\Delta q\) boundary term does vanish. It would be wrong to attribute every failure of a negative-scalar Sekigawa-type argument to that particular term. The normalized-torsion and characteristic-class arguments have different integrability requirements.

## 3. An integrable curvature defect with an exact topological value

Use the curvature-operator norm, so that the previously verified function is
\(w=\operatorname{tr}((W^+)^2)\). Substitution in its rational expression gives
\[
w=6+486t^6-486t^5+108t^4-18t^3.
\tag{10}
\]
Thus \(w\) and the full curvature are bounded. In fact \(w<6\) for \(t>0\):
\[
w-6=18t^3\big[(3t-1)^3-(3t-1)-1\big],
\]
and \(u^3-u-1<0\) on \([-1,1]\). Formula (1) proves absolute integrability of \(w-6\), and elementary integration yields
\[
\boxed{\int_M(w-6)\,dV=-32V_\Gamma
=-64\pi^2(g-1)=32\pi^2\chi(M).}
\tag{11}
\]
Since \(\chi(M)=\chi(\Sigma_g)=2-2g\), this can also be written
\[
\boxed{\int_M(w-6)\,dV=-\tfrac12\int_Mq\,dV.}
\tag{12}
\]
For an Einstein four-metric in this norm,
\(|\operatorname{Rm}_{\mathrm{op}}|^2=w+s^2/24=w+6\). Hence the equivalent formula is
\[
\boxed{\int_M\left(|\operatorname{Rm}_{\mathrm{op}}|^2-12\right)dV
=32\pi^2\chi(M).}
\tag{13}
\]
These are absolutely convergent subtracted densities, not differences of two divergent integrals and not a cutoff-dependent finite-part convention. The constant \(6\) is the limiting self-dual Weyl density; the normalization is fixed by \(\operatorname{Ric}=-3g\).

## 4. Exact Chern–Gauss–Bonnet boundary contribution

The bulk Euler form is
\[
e(g)={w+6\over8\pi^2}\,dV.
\]
Directly integrating (10) on \(M_\epsilon\) gives
\[
\int_{M_\epsilon}e(g)
=(g-1)\left({4\over\epsilon^2}-17+12\epsilon
-36\epsilon^2+108\epsilon^3-81\epsilon^4\right).
\tag{14}
\]
Let \(\mathcal B(\partial M_\epsilon)\) denote the standard boundary correction with the convention
\[
\chi(M_\epsilon)=\int_{M_\epsilon}e(g)+\mathcal B(\partial M_\epsilon).
\]
Since every \(M_\epsilon\) retracts onto \(\Sigma_g\), the boundary term is exactly
\[
\boxed{\mathcal B(\partial M_\epsilon)
=(g-1)\left(-{4\over\epsilon^2}+15-12\epsilon
+36\epsilon^2-108\epsilon^3+81\epsilon^4\right).}
\tag{15}
\]
In particular, it diverges to \(-\infty\). The total torsion energy remains finite while the characteristic boundary contribution does not disappear. The closed argument requiring positive Einstein Euler density to equal the Euler characteristic cannot be transferred to this complete end.

Equations (11)–(15) supply a concrete relation among torsion, the asymptotic curvature density, topology, and the boundary correction. They do not produce a compact quotient: \(q>0\) everywhere and \(q\to0\) at infinity, which already rules out a compact quotient preserving the metric–form pair.

## 5. What this continuation establishes

The previously constructed complete examples have much stronger integrability than merely pointwise decay: all torsion \(L^p\) norms above the exact threshold \(4/3\) are finite. Nevertheless the logarithmic amplitude derivative is nondecaying and the characteristic boundary term is divergent. The global distinction from the closed problem is therefore explicit, not an uncomputed cutoff error.

The construction, the values \(64V_\Gamma\) and \((512/3)V_\Gamma\), and noncompactness were already in the system manuscript. The new formulas are the full distribution/integrability law, the normalized derivative and flux identities, the convergent curvature-defect identity, and the exact boundary polynomial. They strengthen the geometric understanding of the existing example; they do not settle any of Q1–Q4 or establish independent literature priority.

Classical background used: S.-S. Chern, *On the Curvatura Integra in a Riemannian Manifold*, Annals of Mathematics (2) 46 (1945), 674–684, https://www.jstor.org/stable/1969203 ; M. P. Gaffney, *A Special Stokes's Theorem for Complete Riemannian Manifolds*, Annals of Mathematics (2) 60 (1954), 140–145, https://www.jstor.org/stable/1969703 . The flux (8) is computed directly, and no unstated noncompact Stokes extension is used.
