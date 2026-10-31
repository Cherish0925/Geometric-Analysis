# Independent review of the Nil and all-sign corollaries

20 September 2026. Reviewed `round4_global.md` and
`round4_all_sign_gap.md` against their displayed equations and the local
monopole conventions. No blocking mathematical issue was found in the
stated results. Their symmetry, actual-monopole and topology hypotheses
must remain explicit.

## 1. Full-matrix Nil calculation

The Heisenberg bracket scale is correct with an arbitrary positive
matrix G. In the fixed Lie algebra, the determinant of an oriented
orthonormal frame \((e_1,e_2,Z/\ell)\) is \(1/v\). Its horizontal
two-by-two determinant is therefore \(\ell/v\), giving
\([e_1,e_2]=(\ell^2/v)e_Z\). Central components of the two horizontal
vectors do not affect the bracket. Thus
\(\mu=\ell^4/(2v^2)\) and the intrinsic slice Ricci tensor has
eigenvalues \((-\mu,-\mu,\mu)\), as stated.

The derivative of the normalized central vector is essential. In the
fixed frame \(e_Z'=-r e_Z\), while \(G'=2GS\). Consequently

\[
 r'=\langle S'e_Z,e_Z\rangle+2|Se_Z|^2-2r^2
    =\langle S'e_Z,e_Z\rangle+2|W|^2.
\]

Combining this with the tangential and trace equations gives exactly

\[
 \chi''+H\chi'=-\lambda+3\mu
               +(\operatorname{tr}E_T-2E_{ZZ})+4|W|^2.
\]

The mixing term is nonnegative. Since the error combination is
\(E_{11}+E_{22}-E_{ZZ}\), its absolute value is at most three times
the assumed operator-norm error. At an interior maximum of mu, this
gives \(\mu\le\lambda/3+\epsilon\).

Independently, at an actual zero of H, the normal constraint gives
\(\mu=2\lambda+|S|^2-\operatorname{tr}E_T+E_{00}
\ge2\lambda-4\epsilon\). This proves the finite-band inequality.
When v tends to infinity and mu tends to zero at both ends, the needed
volume minimum and positive curvature-scale maximum are attained in
the interior. The resulting \(\epsilon\ge\lambda/3\) follows with
the stated constants. No mixed Codazzi equation has been set to zero;
the proof uses necessary consequences of the full Ricci-error bound.

The retained exact cusp checks the signs: its shape eigenvalues are
\((1,1,2)/\sqrt6\), its bracket energy is 1/3, and for lambda=1 its
normal and tangential Ricci residuals vanish. It does not satisfy the
two expanding-end hypotheses.

The radial Kaluza--Klein coordinate changes also cancel the dr terms
exactly while preserving the torus periods. The resulting flat
three-dimensional slices satisfy the scalar constraint at a volume
minimum, giving \(\epsilon\ge\lambda/2\). This excludes the complete
radial class described in the note, including its off-diagonal and
radial charge terms. It does not exclude genuinely two-variable orbit
geometry.

Finally the lattice distinction is valid: a finite-index subgroup of
a Heisenberg lattice contains powers of both horizontal generators,
whose commutator is a nontrivial power of the infinite-order center.
It cannot become abelian and hence cannot be the fundamental group of
a finite torus cover. Shrinking the physical bracket norm does not
alter that group-theoretic fact.

## 2. Positive normalization and the all-sign energy fraction

Let \(r=V^{-1}\int|\operatorname{Ric}-g|^2\) and e=s-4.
The orthogonal Ricci decomposition gives
\(\int e^2\le4rV\) and \(\int|\operatorname{Ric}^{\circ}|^2\le rV\).
On the negative-scalar set, \(s_-^2\le(s-4)^2\). The actual-monopole
scalar inequality therefore proves

\[
                    A/V\le r/(8\pi^2).
\]

For r<=1/4, the reverse triangle inequality for s=4+e and Chern--Weil
give

\[
 4\pi^2T/V\ge(4-2\sqrt r)^2/24-r/2\ge1/4.
\]

The exact last-step certificate is
\((1/2-x)(4x+10)/12\ge0\), where x=\(\sqrt r\le1/2\).
If also d<=1/4, the topological upper bound is

\[
 4\pi^2T/V\le(r/2)(2/3+d)\le11/96<1/4.
\]

Thus r and d cannot both be at most 1/4, and in particular r+d>1/4.
After taking a scaling infimum the asserted weak inequality is the
correct formulation.

The signed scaling calculation is exact. With
\(R_2=\int|\operatorname{Ric}|^2>0\), \(S=\int s\), one minimizes

\[
                 R_2/(\lambda^2V)-2S/(\lambda V)+4.
\]

For S nonzero the minimizing signed lambda is \(R_2/S\), and the
value is \(4-S^2/(VR_2)\). For S=0 the infimum is four. The
identity

\[
 4R_2-S^2/V
       =4\int|\operatorname{Ric}^{\circ}|^2+\int(s-S/V)^2
\]

proves the displayed energy-fraction expression. R_2=0 is excluded by
the stated positive monopole projection, through its scalar inequality.
Combining the positive estimate with the new negative-sign theorem is
therefore valid, with the minimum of the two constants.

This is a corollary of two different arguments. The new truncation and
Hessian mechanism is needed for the negative side; the positive side
uses classical scalar and Chern--Weil inequalities. Neither conclusion
extends beyond the specified actual-monopole hypotheses and topological
band, and neither supplies a theorem for unrestricted Yau26.
