# Polarized scope of the integral gap and the symplectic chamber

22 September 2026.

The extension to \(b_+=1\), including standard blow-ups and
\(S^1\times S^3\) additions, was already proved in
[round 13](round13_chamber.md). It is not a new result of round 21.
This note identifies the exact scope of the comparison with LeBrun and
resolves the chamber condition for a concrete symplectic class of bases.
The analytic gap remains the input from
[round 4](round4_rigidity.md) and its
[all-sign consequence](round4_all_sign_gap.md); the arguments below do
not constitute another independent verification of that analytic proof.

## 1. The analytic input is conformal, not chamber-independent

Let \(g\) be a smooth metric on a closed oriented four-manifold, with
\(T=2\chi+3\tau\). Suppose a fixed spin-c structure, of real Chern class
\(a\), has unperturbed Seiberg--Witten solutions for every metric in
\([g]\), and

\[
 p=(a_g^+)^2\ge A>0,\qquad a^2\ge T.
 \tag{1}
\]

The inherited integral theorem gives, with its same universal constant,

\[
 \mathcal E(g)+\left(\frac{T}{A}-\frac23\right)_+
 \ge\varepsilon_0>0.
 \tag{2}
\]

Indeed, for any smooth \(f>0\), solve the ordinary equations on
\(\widehat g=f^{-2}g\). Conformal covariance gives

\[
 \Phi=f^{-3/2}\widehat\Phi,\qquad
 D_A^g\Phi=0,\qquad -iF_A^+=f\sigma_g(\Phi).
\]

Thus the same structure supplies every weight used in the bounded-spinor
and self-testing argument. Its self-dual projection is unchanged because
the Hodge star on two-forms is conformally invariant. The auxiliary
structure may depend on \(g\); it must not change when \(f\) changes.
No continuity of the selection in the space of metrics is needed.

This conformal scope is already explicit in LeBrun's curvature theorem;
his polarized definition is a sufficient, slightly stronger input.
See [LeBrun, Definition 1 and Theorem 2.3](https://arxiv.org/pdf/math/0003068),
and [the conformal rescaling lemma](https://arxiv.org/pdf/math/0611450).

## 2. The full positive-budget connected-sum application is already present

Suppose \(X\) has \(T_X=2\chi(X)+3\tau(X)>0\), and a nonzero ordinary
Seiberg--Witten invariant with Chern class \(c\), so \(A=c^2\ge T_X\).
For \(b_+(X)=1\), nonvanishing is required in the small-perturbation
chamber. On

\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}
       \#\ell(S^1\times S^3),\qquad D=k+4\ell,
\]

round 13 supplies, for each polarization \(H=H_g^+\), a selected
polarized class

\[
 a_H=c-\sum_{j=1}^k E_j,
 \qquad c_H^+\cdot E_j\le0.
\]

Here the signs of the exceptional generators are selected at \(H\),
and then held fixed. Their squares and orthogonality give

\[
\begin{split}
 (a_H^+)^2
 &= (c_H^+)^2-2\sum_j c_H^+\cdot E_j
                  +\left(\sum_j E_{j,H}^+\right)^2
 \ge c^2=A,\\
 a_H^2&=A-k\ge T_X-k=T_M+4\ell\ge T_M.
\end{split}
 \tag{3}
\]

Consequently (2) yields

\[
 \mathcal E(g)+
   \left(\frac{T_X-k-4\ell}{A}-\frac23\right)_+
 \ge\varepsilon_0.
 \tag{4}
\]

LeBrun's Proposition 3.2 provides the polarized gauge-theoretic input.
For positive-dimensional base invariants, the original insertion is
retained and each handle adds a degree-one loop insertion; round 13,
Section 2a, verifies the dimensions and the chamber-compatible surgery
formula. Nothing here requires simple type.

For a minimal general-type complex surface, \(A=T_X=c_1^2(X)>0\),
so this is already the universal estimate

\[
 \boxed{\mathcal E(g)+
 \left(\frac13-\frac{k+4\ell}{c_1^2(X)}\right)_+
 \ge\varepsilon_0.}
 \tag{5}
\]

It includes \(b_+=1\). In particular, re-proving the same chamber
selection cannot be counted as a further enlargement of this family.

## 3. A geometric sufficient condition for the symplectic chamber

The chamber qualifier in (4) can be discharged directly for the following
symplectic bases. This is an application of classical Taubes theory to
the existing integral theorem, not a new gauge-theoretic theorem.

**Proposition.** Let \((X,\omega)\) be a closed symplectic four-manifold
with \(b_+(X)=1\), and let \(K=K_\omega\) be its symplectic canonical
class. Suppose

\[
                  K^2>0,\qquad K\cdot[\omega]>0.
 \tag{6}
\]

Then the canonical spin-c structure of determinant class \(-K\) has
nonzero invariant in the small-perturbation chamber for every metric.
Every metric on the standard connected sums in Section 2 satisfies
(5), with \(c_1^2(X)\) replaced by \(K^2\), and with the same
constant \(\varepsilon_0\). No integrable complex structure is assumed.

**Proof.** Choose the forward cone containing \([\omega]\). The
Lorentzian intersection form and (6) place \(K\) in that cone. For the
unit positive generator \(u_g\) of \(H_g^+\) in the forward cone, the
reverse Cauchy inequality gives

\[
             K\cdot u_g\ge\sqrt{K^2}>0.
 \tag{7}
\]

In Li--Liu's convention the chamber discriminant of a determinant
class \(c\), at perturbation \(\mu\), is
\(\Delta_c(g,\mu)=(c-\mu)\cdot u_g\), after their normalization of
the perturbation. At zero perturbation for \(c=-K\), (7) makes this
discriminant strictly negative for every \(g\). Thus the actual
small-perturbation chamber is exactly their negative, or symplectic,
chamber. Taubes' nonvanishing gives its canonical invariant equal to
one, up to the chosen homology orientation. These conventions and the
nonvanishing statement are in
[Li--Liu, Section 2.1 and Theorem 2.2](https://arxiv.org/pdf/math/0012048).

For any fixed metric, compactness as generic perturbations tend to zero
gives an unperturbed solution. It cannot be reducible, because
\(((-K)_g^+)^2\ge K^2>0\): a reducible would have \(F_A^+=0\),
contradicting its nonzero harmonic projection. The same argument works
throughout the conformal class. Finally \(K^2=T_X\) for the compatible
almost-complex structure, and (3)--(5) apply. QED.

Minimal symplectic manifolds of general type with positive canonical
square satisfy the displayed geometric hypotheses. Minimality is not
needed in the proposition once (6) is imposed. Its useful content is
that the small chamber is identified rather than stipulated.

The sign in (6) is essential. On \(\mathbb{CP}^2\), the canonical class
has square nine but negative pairing with the symplectic form. The
Taubes chamber is then not the zero-perturbation chamber for \(-K\).
This prevents a false application to its positive Einstein metric.

## 4. Exact and almost-Einstein consequences

The scalar monopole estimate excludes Ricci-flat metrics in all these
positive-budget families. For other Einstein metrics,
\(\mathcal E=0\). Hence (5) implies

\[
 \frac{k+4\ell}{A}\le\frac13-\varepsilon_0
 \quad\text{whenever an Einstein metric exists}.
 \tag{8}
\]

Using \(\gamma=\varepsilon_0/2\) avoids an endpoint ambiguity:
\(D\ge(1/3-\gamma)A\) implies no Einstein metric, and indeed
\(\mathcal E(g)\ge\varepsilon_0/2\) for every smooth metric. Therefore

\[
 \delta_\sigma(g)\ge\sqrt{\varepsilon_0/8},
 \qquad \sigma=\pm1,
 \tag{9}
\]

in this band. The implication from the quantitative theorem to the
classical exact obstruction is one-way. Exact nonexistence alone does
not imply a uniform gap for approximate solutions.

Equations (5)--(9) recover the positive-budget scope of LeBrun's
Theorem 3.3 and Corollary 3.4, not his whole Ricci-energy or minimal-volume
theory. The normalization \(A>0\) is indispensable. An assertion about
all \(T_X\le0\) edge cases must separately retain the Ricci-flat
Hitchin--Thorpe equality possibilities; it cannot be obtained by division
by \(T_X\).

The threshold is strictly improved as a real inequality. To name an
additional exact-obstruction example below the old threshold, one must
also exhibit a realized ratio \(D/A\) in the added band. This distinction
does not weaken the uniform integral estimate at the old boundary.

## 5. What remains an actual extension problem

No new argument is supplied here for replacing the standard negative
summands by an arbitrary negative-definite \(N\) when the base has
\(b_+=1\). The high-\(b_+\) result used in round 5 invokes
[Ishida, Proposition 6](https://msp.org/pjm/2012/258-2/pjm-v258-n2-p05-s.pdf),
whose stated hypothesis is \(b_+(X)\ge2\). Betti numbers and a diagonal
intersection form alone do not supply the required polarized gluing
theorem. An extension must produce, for every tested polarization, a
nonzero invariant in its actual small chamber and retain a class square
sufficient for the determinant-connection estimate. Once those inputs
are established, no new analytic gap mechanism is needed.
