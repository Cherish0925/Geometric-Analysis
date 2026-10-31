# O11: what ideal total-curvature minimizers actually supply

Status: a checked use of an existing global variational theorem, plus a relative curvature calculation. This does not prove the sharp O11 lower bound. It identifies precisely the geometric information that cannot be silently supplied by ideal-minimizer theory.

## 1. The available global theorem

Primary source: Michael T. Anderson, *Canonical Metrics on 3-Manifolds and 4-Manifolds*, arXiv:math/0511034, Theorem 4.10, equations (4.43), (4.45), Remark 4.12, and the discussion following Theorem 4.15. <https://arxiv.org/pdf/math/0511034>

For each fixed closed four-manifold, Anderson constructs total-curvature minimizing sequences with a critical orbifold limit, possibly open with collapse. The compact-orbifold alternative has an **energy equality including all ALE bubbles**. The open/collapsing alternative has an inequality. Completeness and full energy accounting in the latter are not conclusions of this theorem. The limits minimize against compact perturbations. The theorem does not identify the topology of the regular bulk with a prescribed connected-sum factor.

In the present curvature-operator convention,

\[
\mathcal R(g):=\int|\operatorname{Rm}_{\rm op}|^2
=8\pi^2\chi(M)+P(g),\qquad P(g)=\int|\operatorname{Ric}^{\circ}|^2.
\]

Thus these sequences genuinely minimize the O11 numerator. This is more than the previously available choice of an arbitrary nearly stationary sequence. It does not, however, place that sequence simultaneously in the constant-scalar gauge used by the actual-field estimates. A subsequent conformal change preserves the minimizing value asymptotically but is not automatically known to preserve the same ideal decomposition.

## 2. Exact relative tariff: why end groups cannot be discarded

Let \(N\) be a smooth connected four-manifold with finitely many sufficiently decaying ALE ends. Assume the usual Gauss–Bonnet and signature boundary limits exist, the compactification by end boundaries has finite homology, and the intersection form is negative definite. Put

\[
e=\#\{\text{ends}\},\quad m=b_2(N),\quad r=b_1(N),\quad
q_\infty=\sum_{a=1}^e |\Gamma_a|^{-1}.
\]

Orient boundary spectral corrections so that

\[
\int_N(|W^+|^2-|W^-|^2)
=12\pi^2\bigl(\tau(N)+\eta_\infty\bigr).
\]

The end boundaries are rational homology spheres. The long exact sequence of the compact core and Poincaré–Lefschetz duality give

\[
b_3=e-1+r,\qquad \chi(N)=2-e-2r+m,\qquad \tau(N)=-m.
\]

Write \(S_N=\int_Ns^2\), \(W_N^\pm=\int_N|W^\pm|^2\). Relative Gauss–Bonnet gives

\[
8\pi^2(\chi(N)-q_\infty)
=W_N^++W_N^--\frac12P_N+\frac1{24}S_N.
\]

Using \(W_N^++W_N^-\ge W_N^--W_N^+=12\pi^2(m-\eta_\infty)\), one obtains

\[
\boxed{P_N\ge
8\pi^2m+32\pi^2r
+16\pi^2(e-2+q_\infty)
-24\pi^2\eta_\infty+\frac1{12}S_N.}
\tag{2.1}
\]

No Einstein or scalar-flat assumption enters this calculation.

For genuinely Euclidean ends, \(\Gamma_a=1\) and \(\eta_\infty=0\), hence

\[
\boxed{P_N\ge8\pi^2b_2(N)+32\pi^2\bigl(b_1(N)+e-1\bigr)+\frac1{12}S_N.}
\tag{2.2}
\]

This is the blow-up and handle tariff required by O11. For a one-ended negative-definite core it gives \(8\pi^2b_2\); for a two-ended core with \(b_1=b_2=0\) it gives \(32\pi^2\).

But (2.2) is false for arbitrary ALE ends. Eguchi–Hanson has \(m=1\), \(r=0\), \(e=1\), \(\Gamma=\mathbb Z_2\), \(\eta_\infty=0\), and \(P_N=S_N=0\). Formula (2.1) gives exactly zero. Its nontrivial two-cycle is paid for by Weyl curvature and the quotient boundary correction, not by traceless Ricci energy. Accordingly, replacing arbitrary ALE bubbles by AE cores without retaining the outer marking loses exactly the information O11 needs.

## 3. A conditional sharp deduction with the missing hypothesis exposed

Suppose a minimizing configuration for

\[
M=X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3)
\]

can be assembled from one closed bulk diffeomorphic to \(X\) and disjoint complete **whole AE cores** \(N_\nu\), attached along all of their Euclidean ends. Assume negative-definite core intersection forms, convergence sufficient for the relative characteristic boundary terms above, and the lower-semicontinuity accounting \(\inf\mathcal R(M)\ge\mathcal R(X)+\sum_\nu\mathcal R(N_\nu)\). No equality of energies is needed. The marked topological decomposition is an additional hypothesis, not a consequence of Anderson's theorem.

Let \(m_\nu=b_2(N_\nu)\), \(r_\nu=b_1(N_\nu)\), and \(e_\nu\) be their end counts. Mayer–Vietoris gives

\[
k=\sum_\nu m_\nu,\qquad
\ell=\sum_\nu(r_\nu+e_\nu-1).
\]

Also

\[
\mathcal R(N_\nu)
=8\pi^2\bigl(\chi(N_\nu)-e_\nu\bigr)+P_{N_\nu}
\ge16\pi^2(m_\nu+r_\nu+e_\nu-1).
\]

The bulk has \(\mathcal R(X)\ge8\pi^2\chi(X)\), independently of whether it is Einstein. Total-curvature accounting therefore implies

\[
\inf P(M)\ge8\pi^2\chi(X)+16\pi^2(k+\ell)-8\pi^2\chi(M)
=8\pi^2(k+4\ell).
\]

An \(o(Q)\) version of these hypotheses yields the desired O11 asymptotic. Additional nonnegative energy lost elsewhere helps this lower bound; topology left unaccounted for elsewhere is the problem. Thus an energy identity should not be imposed as a necessary prerequisite for this argument. The calculation explains exactly why a marked, whole-core decomposition would suffice. It is not a new proof of the required decomposition and is not a new local core theorem.

## 4. Why the existing theorem does not finish O11

There are three specific missing implications.

1. A critical bulk need not already be the original \(X\). The theorem allows marked exceptional cycles and handle topology to remain in the regular bulk. A smooth non-Einstein global minimizer on \(M\), if one exists, is also an admissible configuration.
2. ALE bubbles have quotient ends. Their boundary corrections must be matched through the full configuration; summing \(8\pi^2\) per two-cycle is contradicted by (2.1). Passing to terminal bubbles erases the needed outer marking.
3. For the varying family, the total-curvature budget is \(O(A_j)\), while O11 needs an error \(o(Q_j)\), with \(Q_j/A_j\to0\). Per-manifold finiteness of the singular set does not provide this relative precision. In the open/collapsing alternative the topology and energy at infinity require additional control as well.

Thus ideal-minimizer theory is a legitimate way to impose exact Euler–Lagrange equations on regular limits. It does not replace the missing sharp topology-to-energy comparison. The compact-case equality is useful and should not be overlooked; treating it as if it also identified all the marked topology would be the erroneous step.
