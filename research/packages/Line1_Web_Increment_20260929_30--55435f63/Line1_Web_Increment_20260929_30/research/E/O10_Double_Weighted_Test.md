# O10: a double weighted test removes a class of uncontrolled negative Hessians

2026-09-30 (Asia/Shanghai). Independent proof of the bilinear estimate proposed by the root agent. This is a new usable analytic lemma under the displayed hypotheses. It is not, by itself, a proof of unrestricted O10.

All integrals below are normalized by total volume. The manifolds and bundles may vary; each individual manifold is closed and smooth.

## 1. A weighted section estimate with no curvature term

Let \(v\) be a smooth section of a Hermitian bundle with unitary connection and rough Laplacian \(L_v\). Suppose
\[
\|v\|_\infty+\|L_vv\|_\infty\le C_v.
\]
For every real scalar \(e\in H^1\),
\[
\boxed{
\|e\nabla v\|_2
\le C(C_v)\bigl(\|e\|_2+\|de\|_2\bigr).
}
\tag{1}
\]
To prove this, first take smooth \(e\), test the section equation against \(e^2v\), and integrate by parts:
\[
\int e^2|\nabla v|^2
=\operatorname{Re}\int e^2\langle L_vv,v\rangle
-2\operatorname{Re}\int e\langle de\otimes v,\nabla v\rangle.
\]
Young's inequality absorbs half of the left-hand side. No commutator, bundle curvature, Riemann tensor or Sobolev inequality occurs. Density proves the \(H^1\) version whenever the product is initially interpreted by approximation.

For the norm of a smooth bundle-valued tensor \(E\), use
\(e_\delta=(\delta^2+|E|^2)^{1/2}\), Kato's inequality, and let \(\delta\downarrow0\). Hence
\[
\boxed{
\||E|\nabla v\|_2\le C(C_v)\|E\|_{H^1}.
}
\tag{2}
\]
The estimate requires no uniform bound for \(E\) itself.

## 2. Two applications that replace the growing fourth-derivative budget

Let \(w\) be a section of another Hermitian bundle with
\[
\|w\|_\infty+\|L_ww\|_\infty\le C_w,
\qquad \|\nabla w\|_2+\|\nabla^2w\|_2\le C_{w,2}.
\]
Let \(\Phi\) be a further section satisfying
\[
\|\nabla\Phi\|_2+\|\nabla^2\Phi\|_2\le C_{\Phi,2}.
\]
Applying (2) first to \(v\), with \(E=\nabla w\), and then to \(w\), with \(E=\nabla\Phi\), gives
\[
\boxed{
\||\nabla v||\nabla w|\|_2
\le C(C_v)C_{w,2},
}
\tag{3}
\]
\[
\boxed{
\||\nabla\Phi||\nabla w|\|_2
\le C(C_w)C_{\Phi,2}.
}
\tag{4}
\]
These are not consequences of an \(L^4\) bound for \(\nabla v\). In particular their constants do not depend on \(\fint|W^-|^2\).

For the actual positive line resolvent,
\[
(L_w+10/3)w=T_M(c),
\]
the fixed height \(M\) yields bounded \(w,L_ww\). Its line curvature is \(5F_A\); the already established bounded-model Ricci and line-curvature estimates give \(C_{w,2}\) independent of the negative Weyl budget. Thus (3)–(4) apply to those tests once \(M\) is fixed.

## 3. Bilinear Hessian cancellation by one integration by parts

Let \(\zeta\) be a one-form or a section of a fixed-rank tensor bundle, with
\[
\|\zeta\|_{H^1}\to0.
\]
Let \(\mathcal C\) be a globally defined smooth contraction tensor of the appropriate bundle type. Assume uniformly
\[
|\mathcal C|\le C_0,
\qquad
|\nabla\mathcal C|\le C_0(1+|\nabla\Phi|+|\nabla v|).
\tag{5}
\]
For any fixed index pattern, including the symmetric negative Hessian, define
\[
I=\operatorname{Re}\fint
\zeta_a\mathcal C^{iajk}\bigl(\nabla_i\nabla_jv,\nabla_kw\bigr).
\]
Then
\[
\boxed{|I|\le C\|\zeta\|_{H^1}\longrightarrow0.}
\tag{6}
\]
The constant depends on the displayed bounds, but not on \(\|\nabla^2v\|_2\), \(\|\nabla v\|_4\), or the opposite Weyl curvature.

**Proof.** Integrate the \(i\) derivative off \(\nabla_jv\). Since all contractions are covariant and the manifold is closed, there are exactly three types of terms:
\[
\begin{aligned}
I_1&=-\operatorname{Re}\fint(\nabla_i\zeta_a)\mathcal C^{iajk}
 (\nabla_jv,\nabla_kw),\\
I_2&=-\operatorname{Re}\fint\zeta_a(\nabla_i\mathcal C^{iajk})
 (\nabla_jv,\nabla_kw),\\
I_3&=-\operatorname{Re}\fint\zeta_a\mathcal C^{iajk}
 (\nabla_jv,\nabla_i\nabla_kw).
\end{aligned}
\]
There is no interchange of covariant derivatives. Thus no curvature is introduced.

By (3),
\[
|I_1|\le C\|\nabla\zeta\|_2
\||\nabla v||\nabla w|\|_2
\le C\|\nabla\zeta\|_2.
\]
Apply (2) with \(E=\zeta\) to obtain
\[
\||\zeta|\nabla v\|_2\le C\|\zeta\|_{H^1}.
\tag{7}
\]
Consequently
\[
|I_3|\le C\||\zeta|\nabla v\|_2\|\nabla^2w\|_2
\le C\|\zeta\|_{H^1}.
\]
For \(I_2\), use (5), (3), (4), and (7):
\[
\begin{aligned}
|I_2|
&\le C\||\zeta|\nabla v\|_2
\left(\|\nabla w\|_2+
\||\nabla\Phi||\nabla w|\|_2+
\||\nabla v||\nabla w|\|_2\right)\\
&\le C\|\zeta\|_{H^1}.
\end{aligned}
\]
This proves (6). In particular, **no antisymmetry of \(i,j\) is necessary**. The same proof applies termwise to any fixed finite linear combination or to the symmetrized Hessian.

## 4. Fixed amplitude cutoffs and adapted-frame tensors

An expression written in adapted frames is eligible for (6) only after it is a genuine globally defined contraction. If it is built tensorially from bounded \(\Phi,v\), parallel Clifford multiplication, and smooth functions of their norms which vanish on fixed lower-amplitude neighborhoods, then its denominators are bounded wherever it is nonzero. Its covariant derivative satisfies (5). Cutoff derivatives are included in (5), since
\[
|d\chi(|v|^2)|\le C|\nabla v|,
\qquad |d\chi(|\Phi|^2)|\le C|\nabla\Phi|.
\]
This verifies eligibility for such tensors without assuming a global adapted frame. It does not automatically verify that any particular frame expression descends correctly; that algebraic check remains necessary.

## 5. Further directly usable estimates

The same argument immediately gives, for a tensor error \(R\),
\[
\left|\fint R*(\nabla v)*(\nabla w)\right|
\le C\|R\|_2.
\tag{8}
\]
Thus a small \(L^2\) first-order error can be paired with these two gradients without paying a separate \(\nabla v\) fourth-power norm. Also
\[
\fint |\zeta||\nabla v|^2|\nabla w|
\le \||\zeta|\nabla v\|_2
     \||\nabla v||\nabla w|\|_2
\to0.
\tag{9}
\]
These estimates identify a class of growing-budget losses in the earlier CR bookkeeping that can genuinely be removed.

## 6. What this does and does not close

The new lemma resolves the displayed bilinear term involving \(\zeta\nabla^2v\nabla w\), and also the small-error triple product (8). It avoids the uncontrolled negative Hessian rather than merely assigning it a slower growth rate.

For a proof of unrestricted O10, one must still derive the **complete** actual weak CR identity with every term accounted for and show it belongs to this class or another uniformly controlled class. In particular, this lemma does not prove
\(d|v|^2\to0\), does not automatically give nonvanishing uniformly integrable mass for the fifth-line section, and does not make a radial coefficient small when its only information is a bounded \(H^1\) norm. Fixed amplitude cutoffs do not erase these requirements.

The fixed-height resolvent hypothesis also remains meaningful: if the mass of \(c\) escapes to arbitrarily high values, the existing contradiction requires a separate argument that fixes the truncation height. This lemma should therefore be inserted into the actual proof and the remaining radial and mass terms checked explicitly; it is not a license to declare the full endpoint solved.
