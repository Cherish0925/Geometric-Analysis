# O11 construction audit: all complete ordinary AE fillings are already excluded

Status: no O11 improvement. Further numerical model optimization has stopped. The calculation below clarifies the exact scope of an existing identity; it is not claimed as a new lower-bound theorem.

## 1. Full Euclidean collar: triaxial metrics are excluded too

Let a smooth compact filling have topology
\[
C=B^4\#m\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3)
\]
and agree with the Euclidean metric on a full round outer collar. Attach the Euclidean exterior. The resulting complete one-ended manifold \(N\) is exactly Euclidean outside a compact set, has trivial end group, and
\[
\chi(N)=1+m-2\ell,\qquad \tau(N)=-m.
\]
Write
\[
P=\int_N|\operatorname{Ric}^{\circ}|^2,\quad
S=\int_Ns^2,\quad W_\pm=\int_N|W^\pm|^2
\]
with Weyl-operator norms as in the manuscript. The boundary contributions at infinity are the ordinary Euclidean ones. Chern--Gauss--Bonnet and signature give
\[
\frac{S}{24}+W_++W_--\frac P2=8\pi^2(m-2\ell),
\qquad W_+-W_-=-12\pi^2m.
\]
Eliminating \(W_-\) gives the exact identity
\[
\boxed{P=8\pi^2(m+4\ell)+\frac S{12}+4W_+.}
\]
Thus every such complete filling satisfies \(P\ge8\pi^2(m+4\ell)+S/12\). The statement does not assume Kähler geometry, symmetry, scalar flatness, or independent separation of the cores. In particular, **every triaxial ordinary blow-up filling with a full flat outer collar is already covered**. Replacing a biaxial ansatz by a triaxial ansatz cannot bypass this obstruction.

The same computation applies to sufficiently decaying AE ends for which the usual boundary limits exist. Exact flat collars avoid any need to discuss the decay thresholds.

## 2. Finite CH collars have a different identity

For an exact complex-hyperbolic collar matching a background ball \(D\), with \(\operatorname{Ric}=-g\) and \(d=\operatorname{Vol}(D)\), the manuscript instead gives
\[
P=8\pi^2Q+\frac S{12}+4W_+-4d,
\qquad Q=m+4\ell.
\]
The first-order cost relevant to sparse replication is not \(P\) alone, but
\[
J=\int_C|\operatorname{Ric}+g|^2
=P+\frac14\int_C(s+4)^2.
\]
Hence
\[
J-8\pi^2Q
=\int_C\left[\frac{(s+3)^2}{3}+1+4|W^+|^2\right]-4d.
\]
A finite CH collar therefore leaves a signed volume term. It is not automatically covered by the flat-collar lower bound. However, if the entire changed background has \(d=o(Q)\), the displayed identity already gives
\[
J\ge8\pi^2Q-o(Q).
\]
The manuscript's supplier-based whole-cell estimate is stronger, \(J\ge8\pi^2Q-4d/3\). Accordingly, an improvement of the coefficient by a fixed amount requires a nonvanishing changed-background volume per unit surgery charge. Shrinking the bolt while reverting to CH outside a shrinking region cannot do it.

This distinction is the exact answer to the audit question: a finite-scale non-Kähler CH filling is not ruled out merely by the AE identity, but its shrinking-core limit is. A search that converges back to that limit is not probing a new mechanism.

## 3. Numerical check performed, and why it is not progress

For completeness, one diagnostic search allowed three Bianchi IX profiles
\[
g=dt^2+a_1(t)^2\sigma_1^2+a_2(t)^2\sigma_2^2+a_3(t)^2\sigma_3^2,
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k.
\]
All three profiles, the bolt radius, the radial length and the outer CH radius were optimized together. The interior anisotropy vanished to fourth order at the bolt, and all perturbations vanished on a full outer CH collar. With \(A_i=a_i^2\), the exact Ricci eigenvalues used were
\[
\lambda_0=-\sum_i\frac{a_i''}{a_i},
\qquad
\lambda_i=-\frac{a_i''}{a_i}
-\frac{a_i'}{a_i}\sum_{j\ne i}\frac{a_j'}{a_j}
+2\frac{A_i^2-(A_j-A_k)^2}{A_1A_2A_3}.
\]
The full, untruncated cost was
\[
J=2\pi^2\int a_1a_2a_3
\left[(\lambda_0+1)^2+\sum_i(\lambda_i+1)^2\right]dt.
\]

Twelve 21-parameter starts, each capped at 400 L-BFGS-B iterations, did not cross the threshold. The best returned value was \(J/(8\pi^2)=1.0007834383\). Re-evaluation of the same coefficients with 384, 768 and 1536 Gauss nodes gave 1.0007834461, 1.0007834416 and 1.0007834420. Six additional starts with large initial triaxial distortion, capped at 600 iterations, also stayed above the threshold; their best returned value was 1.0170357327.

These are finite-dimensional floating-point explorations, not rigorous global bounds or certified local minima; many runs hit their iteration cap. The low values returned to a small-bolt, almost-biaxial regime already consistent with the established AE cost. **No new global competitor, lower coefficient, or new excluded geometric class follows from these runs.** They should not be presented as mathematical progress. Further optimization of this template has been stopped.

## 4. Pure handle rearrangement cannot be the missing mechanism by itself

For \(m=0\), even without any cell structure or symmetry, the closed scalar monopole bound and the signature identity give
\[
P-32\pi^2\ell
=\frac{S-32\pi^2A}{12}+4W_-\ge0.
\]
Thus coupling or rearranging handles alone cannot lower their unrestricted global minimum on \(X\#\ell(S^1\times S^3)\). In the original balanced family, a genuine improvement must alter the joint exceptional-class scalar--Weyl balance; saving energy in an isolated handle calculation is insufficient.

No proof of that joint balance, and no admissible violating metric, was obtained here.
