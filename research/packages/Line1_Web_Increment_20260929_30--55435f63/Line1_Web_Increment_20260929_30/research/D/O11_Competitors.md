# O11: changing the entire complex bulk does not change the standard recovery cost

2026-09-29, continuation D. This is a rigorous exclusion of a global construction route, not a proof of the O11 lower bound. No closed competitor below coefficient four is constructed here.

## 1. Question tested

The original family is
\[
 M_j=X_j\#k_j\overline{\mathbb {CP}}^2
             \#\ell_j(S^1\times S^3),
 \qquad A_j=c_1^2(X_j),\quad Q_j=k_j+4\ell_j,
\]
where \(X_j\) is complex hyperbolic. Standard surgery recovery has
\[
 S\longrightarrow32\pi^2A_j,\qquad
 R\longrightarrow8\pi^2(A_j+Q_j),\qquad
 P=R-S/4\longrightarrow8\pi^2Q_j.
\]
Could one change the *entire* complex bulk, use a different connected-sum decomposition, and obtain the usual recovery construction with a smaller surgery count? This would be a genuine global construction mechanism, rather than an optimization of one prescribed cap. The following proposition rules it out throughout the minimal-general-type surgery class.

## 2. Exact invariance under an alternative bulk decomposition

Write
\[
 I_s(N)=\inf_g\int_Ns_g^2\,dV_g,\qquad
 I_r(N)=\inf_g\int_N|\operatorname{Ric}_g|^2\,dV_g.
\]
These infima are smooth invariants; they do not depend on an orientation.

**Proposition.** Suppose a fixed smooth four-manifold has two descriptions
\[
 N\cong X\#k\overline{\mathbb {CP}}^2\#\ell(S^1\times S^3),
 \qquad
 N\cong Y\#k'\overline{\mathbb {CP}}^2\#\ell'(S^1\times S^3),
\]
where \(X,Y\) are minimal complex surfaces of general type. The diffeomorphisms need not identify the complex orientations. Then
\[
 \boxed{c_1^2(Y)=c_1^2(X),\qquad k'+4\ell'=k+4\ell.}\tag{1}
\]
In particular, applying the standard scalar-flat surgery recovery to either decomposition produces the same limiting traceless-Ricci energy.

**Proof.** Put \(A_X=c_1^2(X)>0\), \(Q_X=k+4\ell\), and similarly for \(Y\). The classical actual monopole supply on this surgery class gives, for every metric, a polarized class whose positive square is at least \(A_X\). The scalar monopole estimate therefore gives
\[
 \int_Ns_g^2\,dV_g\ge32\pi^2A_X.
\]
The recovery construction in LeBrun's Theorem 4.3 approaches the negative Kähler–Einstein canonical model of \(X\), resolves any canonical-model quotient singularities with the scalar-flat pieces used there, and inserts the blow-up and handle pieces. The scalar integral squared approaches \(32\pi^2A_X\). Thus
\[
 I_s(N)=32\pi^2A_X.\tag{2}
\]
The same theorem states, with Ricci *tensor* norm,
\[
 I_r(N)=8\pi^2(A_X+k+4\ell)=8\pi^2(A_X+Q_X).\tag{3}
\]
Both statements apply to \(Y\) as well. Equality of the two values of \(I_s\) yields \(A_Y=A_X\), and equality of the two values of \(I_r\) then yields \(Q_Y=Q_X\). This proves (1). The common recovery has \(P\to I_r-I_s/4=8\pi^2Q_X\). \(\square\)

For an orientation-preserving alternative decomposition, (2) is not even needed: the two equations
\[
 (2\chi+3\tau)(N)=A_X-Q_X,
 \qquad I_r(N)/(8\pi^2)=A_X+Q_X
\]
recover \(A_X\) and \(Q_X\) separately. Formula (2) is included to treat a possible reversal of orientation without ambiguity.

The proof does **not** require a Yamabe invariant identity, an attained scalar infimum, or a smooth Einstein metric on \(X\). In particular, canonical models with rational double points are covered by the cited recovery. The source theorem is stated for every minimal complex surface of general type; in the case \(b^+=1\), the scalar lower bound uses the actual polarized supply from the proof of its Proposition 3.2, not an extra assertion that arbitrary chambers have nonzero invariants. Handle insertions have weight four in (3), exactly as in the source theorem and the project family.

## 3. Consequences for the balanced family

Apply (1) separately for every \(j\). The competing bulk \(Y_j\), the counts \(k'_j,\ell'_j\), and the decomposition may all depend on \(j\). Nevertheless
\[
 A'_j=A_j,\qquad Q'_j=Q_j
\]
are exact equalities. Choosing the gluing scales diagonally so that the scalar and Ricci errors are \(o(Q_j)\) therefore still gives
\[
 P(g_j)=8\pi^2Q_j+o(Q_j).
\]
With the already proved O11 comparison, this recovery has coefficient four. Changing the number and placement of collapsed pieces, or changing to a different minimal-general-type complex bulk, cannot lower that coefficient through the same standard recovery mechanism.

There is also an orientation restriction. If \(N\) and its orientation reverse both possessed descriptions in the displayed minimal-general-type surgery class, (1) would give the same \(A,Q\), and hence
\[
 2\chi(N)+3\tau(N)=A-Q=2\chi(N)-3\tau(N).
\]
Thus \(\tau(N)=0\). In the original balanced family
\[
 \tau(M_j)=A_j/9-k_j>0
\]
for sufficiently large \(j\). Its orientation reverse therefore has no such alternative description. Simply reversing which chirality is called Kähler cannot provide an admissible cheaper recovery on these smooth manifolds.

## 4. Why this does not prove O11

It is essential not to infer
\[
 \inf_g\bigl(R(g)-S(g)/4\bigr)
 =\inf_gR(g)-\tfrac14\inf_gS(g).
\]
This equality has not been proved and does not follow from the two invariant computations. The recovery realizes both individual infima along one sequence, giving the **upper** bound for \(\inf P\). A different metric could pay larger \(S\) and still have smaller \(P\).

Consequently (1) rules out a global *change-of-decomposition strategy within the standard recovery class*. It does not classify all metrics, rule out a non-Kähler competitor, control a coupled nonshrinking filling, or provide the desired all-metric estimate
\[
 P\ge8\pi^2Q-o(Q).
\]
No such stronger claim is made.

## 5. Previously closed construction routes are not counted again

The manuscript already proves that every smooth biaxial ordinary-blow-up filling with the specified complete radial complex-hyperbolic collar is conformally Kähler relative to that collar, and hence has complete residual cost strictly above \(8\pi^2\). This includes any proposed Taub-bolt interior joined by an entirely biaxial transition. The fact that the isolated Ricci-flat Taub-bolt core has \(P=0\) does not evade that theorem. This was checked before deciding not to carry out another local bolt optimization.

Likewise, the manuscript already contains a replication argument for an actual finite filling with eight blow-ups and seven handles. The present note does not rediscover that argument, and no subthreshold filling satisfying its complete matching conditions was obtained.

## 6. Source verification and status

The external primary source checked for the exact constants and scope is:

- Claude LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*, arXiv:math/0003068, Proposition 3.2 and its actual polarized supply; Proposition 4.2; Theorem 4.3 and its proof. https://arxiv.org/pdf/math/0003068 . Theorem 4.3 states \(I_r=8\pi^2(c_1^2+k+4\ell)\). Its recovery provides the scalar upper bound used in (2); the scalar lower bound is the ordinary SW estimate applied to the supplied class.

Project locations in the unchanged integrated manuscript:

- Lines 5334–5567: original family, actual supply, and joint recovery limits.
- Lines 7820–7998: complete relative cell identity, replication, conformally Kähler cost, and the biaxial reduction.

As a check on the scope of the literature, LeBrun's *Curvature Functionals, Optimal Metrics, and the Differential Topology of 4-Manifolds*, arXiv:math/0404251, final discussion on pp. 38–40, explicitly distinguishes known scalar/Ricci minima from the undetermined full-curvature minimum in general-type examples. That historical statement is not a claim that all later literature has been exhausted. https://arxiv.org/pdf/math/0404251 .

**Status:** an exact, elementary consequence of established curvature invariants excludes a class of global alternative constructions. It does not strengthen the O11 lower coefficient, and it is not presented as a new major theorem or as a solution of O11.
