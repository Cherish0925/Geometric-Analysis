# O11: exceptional topology, all-sign supply, and two concrete competitor tests

Date: 2026-09-29, continuation C. This note does **not** solve O11. It separates an exact global target from two explicit metric mechanisms tested here. The global target and its scalar–Weyl version are already present in the earlier classical-budget note; their restatement is not registered as a new theorem. The all-sign projection estimate and the asymptotically hyperbolic neck calculation below are proved directly, with their limited role stated.

## 1. The sharp obstruction is exactly an exceptional-class compensation problem

For
\[
M=X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3),\qquad
A=c_1^2(X),\quad Q=k+4\ell,
\]
let \(S=\int s^2\), \(P=\int|\operatorname{Ric}^\circ|^2\), and \(B=\int|W^-|^2\), using the manuscript's Weyl-operator norm. Its exact characteristic identity is
\[
P=\frac{S-32\pi^2A}{12}+4B+8\pi^2(4\ell-5k).
\]
Consequently
\[
\boxed{P-8\pi^2Q=\frac{S-32\pi^2A}{12}+4B-48\pi^2k.}\tag{1}
\]
Thus a global O11 proof must recover the exceptional-class cost on the right of (1). The handles have canceled from this identity; they remain important to the supply and the balanced parameter range. No new claim that handles can be discarded geometrically is intended.

For the balanced family, put
\[
x=\frac{S-32\pi^2A}{32\pi^2Q},\qquad
y=\frac{B}{12\pi^2k},\qquad c=\frac{P}{8\pi^2Q}.
\]
Then \(k/Q\to2/9\) gives
\[
c=\frac{x+4y-1}{3}+o(1).
\]
The classical Ricci bound only gives \(x+y\ge1+o(1)\); sharpness would require \(x+4y\ge4-o(1)\). The standard recovery has \((x,y)\to(0,1)\). These are the same feasible-region statements already proved in `Line1_O10_O11_20260929/03_O11_Classical_Budget.md`, written to make the exceptional contribution explicit.

## 2. What the simultaneous sign choices really add

Let \(c_0\) be the pullback canonical class, \(c_0^2=A\), and let \(E_i\cdot E_j=-\delta_{ij}\), \(c_0\cdot E_i=0\). On a fixed metric with Hodge positive space \(H\), write
\[
u=\|(c_0)^-\|^2,\qquad d=\sum_i\|E_i^+\|^2,
\qquad a_\epsilon=c_0+\sum_i\epsilon_iE_i.
\]
Averaging over all \(2^k\) signs gives the exact identity
\[
2^{-k}\sum_\epsilon\|(a_\epsilon)^+\|^2
=\|(c_0)^+\|^2+\sum_i\|E_i^+\|^2=A+u+d.\tag{2}
\]
Hence, wherever the manuscript's all-sign supply applies,
\[
\boxed{S\ge32\pi^2(A+u+d).}\tag{3}
\]
In particular, a near-minimizer with scalar excess \(\Delta S=O(Q)\) satisfies \(u+d=O(Q)\), and one selected actual solution has
\[
p\ge A+u+d,\qquad p-a^2\ge k+u+d,
\]
because every sign class has square \(a^2=A-k\). The determinant anti-self-dual curvature therefore has the corresponding harmonic-projection lower bound.

This is a metric-dependent improvement, not a new uniform budget above A. There is an algebraic positive space for which \((c_0)^-=0\) and every \(E_i^+=0\): choose a maximal positive space inside the intersection-form summand of X containing \(c_0\). Thus (2) can equal A. This does not assert that every such algebraic period is realized by a metric. It proves that sign averaging alone contains no positive multiple of k beyond A. The earlier complete-class budget result \(\mathfrak a^2=\mathfrak b^2=A\) is stronger as a statement about all classes and is not superseded here.

A proof of (1)'s lower bound by multiple monopoles must therefore use their **differential relationship**, or a geometric estimate on \(u+d\) at near-minimizers. Merely maximizing or averaging their squares cannot supply the missing \(48\pi^2k\).

## 3. Kähler enlargement of the blow-ups raises the cost

This tests a specific possible construction; it makes no assertion about arbitrary non-Kähler competitors. Normalize the positive class on the minimal surface by \(K_X^2=A\). On its k-fold complex blow-up consider a Kähler class
\[
\Omega=K_X-t\sum_iE_i,\qquad t>0,
\]
whenever it is Kähler. Then
\[
\Omega^2=A-kt^2,\qquad c_1(M)\cdot\Omega=-A-kt,
\qquad c_1(M)^2=A-k.
\]
For any Kähler metric in this class, the scalar integral and Cauchy–Schwarz give
\[
S\ge32\pi^2\frac{(A+kt)^2}{A-kt^2}.
\]
The Kähler identity \(W_+=S/24\) gives
\[
P=\frac S4-8\pi^2(A-k),
\]
so
\[
\boxed{P\ge8\pi^2k+
8\pi^2\frac{2Akt+Akt^2+k^2t^2}{A-kt^2}>8\pi^2k.}\tag{4}
\]
For \(k/A\to0\) and a fixed admissible t, the cost per exceptional sphere is at least
\[
8\pi^2(1+t)^2+o(1).
\]
Thus enlarging the exceptional area within this natural Kähler family does not produce a cheaper blow-up. This is an explicit calculation from standard Kähler identities, not a new general obstruction theorem. It does not cover the handle-connected-sum geometry or changes of complex class.

## 4. A negative-scalar-curvature spherical wormhole also fails to lower the handle cost

Consider a complete two-ended warped metric
\[
g=dr^2+f(r)^2g_{S^3},\qquad s_g=-4,
\]
with a smooth positive minimum \(f(0)=a>0\), \(f'(0)=0\). The scalar equation integrates to
\[
(f')^2=1+\frac{f^2}{3}-\frac C{f^2},\qquad
C=a^2+\frac{a^4}{3}.
\]
It determines the reflected complete asymptotically hyperbolic neck. Its traceless Ricci tensor obeys
\[
|\operatorname{Ric}^\circ|^2=\frac{12C^2}{f^8}.
\]
Since \(\operatorname{Vol}(S^3)=2\pi^2\), integration over both ends gives
\[
P(a)=48\pi^2C^2\int_a^\infty
\frac{f^{-5}\,df}{\sqrt{1+f^2/3-C/f^2}}.
\]
Set \(q=a^2/3\) and \(t=a^2/f^2\). Then the exact dimensionless formula is
\[
P(a)=24\pi^2(1+q)^2
\int_0^1\frac{t^{3/2}}{\sqrt{(1-t)(q+(1+q)t)}}\,dt.\tag{5}
\]
Use the probability measure \(d\mu=(3/4)t(1-t)^{-1/2}dt\). The integral in (5) is
\[
\frac43\,\mathbb E_\mu[(1+q(1+1/t))^{-1/2}].
\]
Here \(\mathbb E_\mu[1+1/t]=5/2\). The function \(x\mapsto(1+qx)^{-1/2}\) is convex, so Jensen gives
\[
\boxed{P(a)\ge32\pi^2
\frac{(1+q)^2}{\sqrt{1+(5/2)q}}>32\pi^2\quad(q>0).}\tag{6}
\]
The final strict inequality follows from \((1+q)^4>1+(5/2)q\). Dominated convergence in (5) gives \(P(a)\to32\pi^2\) as \(a\downarrow0\).

Thus an exact constant-negative-scalar spherical neck has more, not less, total traceless-Ricci cost than the scalar-flat shrinking handle model. This rejects this complete two-ended model as a cheaper handle. It does **not** prove a lower bound for a finitely truncated neck: truncation changes the curvature integral, and its matching transition must be counted. It also does not turn the real-hyperbolic ends into complex-hyperbolic ends, or produce a closed competitor on the original M.

## 5. Precise status

No lower-cost closed metric on the balanced family was constructed. No all-metric lower bound with coefficient four was obtained. Equations (2)–(6) close two tempting elementary construction routes and identify what simultaneous sign supply can and cannot prove. They should remain a short supporting note, not replace the global O11 task or be presented as a main-theorem improvement.

The genuine unresolved link remains a proof of (1)'s nonnegativity up to \(o(Q)\) along a true near-minimizing sequence, or a complete metric construction violating it with every transition included.

Source scope: manuscript section “Surgery limits and the first-order variational problem”; preceding `03_O11_Classical_Budget.md`; LeBrun's original Ricci-curvature theorem, arXiv:math/0003068, and the final discussion of full curvature in arXiv:math/0404251. The calculations (2), (4), (5), (6) above are explicitly derived here; no publication-level novelty is asserted for them.
