# Step 58 — exact negative-Einstein almost-Kähler branch and the closed zero-locus problem

## 1. Statement secured in this Step

Use left-invariant one-forms on Bianchi VIII with
\[
d\sigma _1=-2\sigma _2\wedge\sigma _3,\qquad
d\sigma _2=2\sigma _3\wedge\sigma _1,\qquad
d\sigma _3=2\sigma _1\wedge\sigma _2.
\]
For \(1/3<p<1\), set
\[
 g=G\,dp^2+A_1\sigma _1^2+A_2\sigma _2^2+A_3\sigma _3^2,
\]
where
\[
G={4(3p^2+1)\over(1-p)^2(1+p)^2(3p-1)(3p+1)},
\]
\[
A_1={4(3p-1)(3p^2+1)\over3(1-p)(1+p)^2},\quad
A_2={4(3p+1)(3p^2+1)\over3(1-p)^2(1+p)},
\]
\[
A_3={64p^2\over(1-p)(1+p)(3p^2+1)}.
\]
Let \(e^0=\sqrt G\,dp\), \(e^i=\sqrt{A_i}\sigma_i\), and
\(\omega_i=e^0\wedge e^i+e^j\wedge e^k\). Define
\[
 X_1={(1-p)^3(3p+1)\over16p^3},\qquad
 X_2={(1+p)^3(3p-1)\over16p^3},
\]
so \(X_1+X_2=1\), and choose the positive branches
\[
 \Omega=\sqrt{X_1}\,\omega_1+\sqrt{X_2}\,\omega_2.
\]
Then, on the open interval,
\[
 d\Omega=0,\qquad |\Omega|_g^2=2,\qquad \operatorname{Ric}_g=-3g,
\]
and
\[
 q:=|\nabla\Omega|^2={36(1-p^2)^3\over(1+3p^2)^3}>0.
\]
Thus \((g,\Omega)\) is a real-analytic strictly almost-Kähler Einstein structure with scalar curvature \(-12\). This is now an actual local existence theorem, not a numerical jet or merely an invariant ideal.

### Exact proof

Write \(h_i=(\log a_i)'\), \(W_i=n_i a_i/(a_ja_k)\), where prime is geodesic differentiation and \(n=(-1,1,1)\). Introduce
\[
y^2=(3p-1)(3p+1)(3p^2+1).
\]
All \(h_i,W_i\) become rational elements of \(\mathbb Q(p,y)\). Reduction modulo this quadratic relation verifies identically
\[
Q=\sum_{i<j}h_ih_j+\sum_iW_i^2-2\sum_{i<j}W_iW_j=3,
\]
\[
h_i'=-h_i\sum_jh_j+2\{W_i^2-(W_j-W_k)^2\}+3,
\qquad W_i'=W_i(h_i-h_j-h_k).
\]
These are the diagonal Bianchi class-A Einstein equations with \(\lambda=-3\). For
\(\mu_i=2W_i-h_j-h_k\), exact reduction also gives
\[
X_i'=2\mu_iX_i\quad(i=1,2),\qquad X_1+X_2=1.
\]
Choosing fixed positive square roots yields \(x_i'=\mu_ix_i\), which is exactly the invariant closure equation. Substitution in the connection formula for \(|\nabla\Omega|^2\) gives the displayed rational \(q\).

The reproducible calculation is `workspace/scripts/step58_exact_bianchiVIII_fast.py`, with output `workspace/data/step58/exact_verification_fast.json`. It also substitutes the exact witness \(W=(-1/15,1,192/245)\), \(h=(176/147,656/735,76/147)\) into every lifted ideal generator and obtains \(Q=256/105\), \((\mu_1,\mu_2)=(-54/35,2/7)\), \((X_1,X_2)=(5/32,27/32)\), and \(q=27648/12005\), independently securing real admissibility of the invariant component. It independently substitutes the metric into the Step-56 Koszul curvature engine and obtains \(\operatorname{Ric}+3g=0\) exactly at \(p=2/5,1/2,3/4\). These point checks are independent confirmation of conventions; the all-\(p\) proof is the exact Einstein ODE plus explicit metric reconstruction.

The three rational-point curvature blocks supplied an independent convention check. The all-\(p\) statement is now exact. Put \(C_i=W_j+W_k-W_i\), \(b_i=h_i-C_i\), and \(d_i=h_i+C_i\). Cartan's two chiral curvature triples are
\[
F_i^+=(b_i'+h_i b_i)e^{0i}+(2W_i b_i+b_jb_k)e^{jk},\qquad
F_i^-=(d_i'+h_i d_i)e^{0i}+(2W_i d_i-d_jd_k)e^{jk}.
\]
Reduction in the same quadratic field gives
\[
d_i'+h_i d_i=1,\qquad 2W_i d_i-d_jd_k=-1,
\qquad b_i'+h_i b_i=2W_i b_i+b_jb_k.
\]
Thus \(F_i^-=e^{0i}-e^{jk}\); after the common curvature-index sign conversion, \(\mathcal R|_{\Lambda^-}=-I=W^-+(s/12)I\), and since \(s=-12\),
\[
W^-\equiv0.
\]
The exact \(W^+\) eigenvalues are
\[
\begin{aligned}
w_1&=-{4(9p^6-18p^5-9p^4-6p^3+9p^2-1)\over(3p^2+1)^3},\\
w_2&=-{4(9p^6+18p^5-9p^4+6p^3+9p^2-1)\over(3p^2+1)^3},\\
w_3&={8(9p^6-9p^4+9p^2-1)\over(3p^2+1)^3}.
\end{aligned}
\]
They sum to zero and tend to \((1,-2,1)\), with \(\Omega\to\omega_2\), fixing the normalization. This is reproduced by `workspace/scripts/step59_chiral_exact.py` and `workspace/data/step59/chiral_exact.json`; the earlier failed radical expansions remain unused.

## 2. Global formulas

Let \(r\) denote outward geodesic distance from \(p=1/3\). Exact series inversion gives
\[
p-\tfrac13={2\over9}r^2-{2\over81}r^4-{11\over1458}r^6+O(r^8),
\]
\[
A_1=r^2+{2\over9}r^4+O(r^6),\qquad
A_2=A_3=6+7r^2+O(r^4),
\]
\[
A_2-A_3={10\over3}r^4+O(r^6),\qquad
X_2={8\over3}r^2+O(r^4),
\]
and \(q\to32/3\). These divisibilities give a full smooth completion, not only a finite-order test. Choose a cocompact torsion-free \(\bar\Gamma<PSL(2,\mathbb R)\) and a lift \(\Gamma<SL(2,\mathbb R)\) with \(-I\notin\Gamma\); this fixes compact-generator period \(2\pi\). Locally write
\[
\sigma_1=d\theta+A,\qquad \sigma_2+i\sigma_3=e^{2i\theta}\eta_0,
\qquad z=re^{i\theta},\qquad Dz=dz+izA.
\]
Analyticity of \(p-1/3\) in \(r^2\), together with \(A_1-r^2\in r^4\mathbb R\{r^2\}\) and \(A_2-A_3\in r^4\mathbb R\{r^2\}\), gives
\[
dr^2+A_1\sigma_1^2=|Dz|^2+{A_1-r^2\over r^4}\bigl(\operatorname{Im}(\bar zDz)\bigr)^2,
\]
\[
A_2\sigma_2^2+A_3\sigma_3^2={A_2+A_3\over2}|\eta_0|^2+{A_2-A_3\over2r^4}\operatorname{Re}(z^4\eta_0^2),
\]
with analytic coefficients. For the second form component, set \(C_r=\sqrt{X_2A_2}=ru(r^2)\), \(C_\theta=\sqrt{X_2A_3A_1}=r^2v(r^2)\), where \(u(0)=v(0)=4\). Then
\[
\Omega_2=\operatorname{Re}\left\{\left[{f_+\over r}zDz+{f_-\over r^3}z^3D\bar z\right]\wedge\eta_0\right\},
\qquad f_\pm={1\over2}\left(C_r\pm {C_\theta\over r}\right),
\]
and both \(f_+/r\) and \(f_-/r^3\) are analytic in \(r^2\). The \(\omega_1\) component is the sum of analytic normal and base area forms. Hence \(g\) and \(\Omega\) extend smoothly and nondegenerately over the bolt; the Einstein, closedness, norm, strictness, and \(W^-=0\) identities extend by continuity. The completed pair is complete because the other end has infinite radial length.

The orbit quotient is \(P=\Gamma\backslash SL(2,\mathbb R)\to\Sigma_g\). Using the full inverse image of \(\bar\Gamma\), or a quotient containing \(-I\), would reduce the effective period to \(\pi\) and produce a normal cone. With the \(\Omega\)-induced normal and tangent orientations, \(e(N)=-\tfrac12e(T\Sigma)\), so \(\deg N=g-1\) and \(N^{\otimes2}\cong K_\Sigma\). This sign is fixed by the nonsingular polar coframe: the normal connection is \(-A\), while the tangent connection is \(2A\).

At the other endpoint set \(x=1-p\). Then
\[
G={1\over2x^2}+O(x^{-1}),\quad
A_1={8\over3x}+O(1),\quad
A_2={32\over3x^2}+O(x^{-1}),\quad
A_3={8\over x}+O(1).
\]
Hence radial length diverges like \(2^{-1/2}\log(1/x)\), the metric is complete toward this end, and its rates are ACH-like: one direction grows as \(x^{-2}\), the other two as \(x^{-1}\). The exact CR boundary identification still depends on the orbit quotient and marking.

`workspace/scripts/step58_global_exact.py` gives these series and, per fixed compact orbit quotient, the unconditional torsion integrals
\[
\int q=64,\qquad \int q^2={512\over3}.
\]
The exact chiral calculation also proves
\[
|\eta|^2={18(1-p^2)^3(9p^2-1)\over(1+3p^2)^4},\qquad
|W_3^+|^2={81(1-p^2)^4(9p^2-1)^2\over2(1+3p^2)^6},
\]
where \(\eta\) has the ordinary form norm and \(W_3^+\) the operator Hilbert--Schmidt norm. Therefore the same exact integration gives, per unit invariant orbit volume,
\[
\int|\eta|^2=32,\qquad \int|W_3^+|^2=16
\]
and the genuine geometric identity
\[
\int\left(|\eta|^2+2|W_3^+|^2+{3q^2\over16}-{3q\over2}\right)=0.
\]
For the lifted genus-\(g\) orbit quotient, \(\int_P\sigma_{123}=2\pi^2(g-1)\), so every displayed radial integral is multiplied by this factor. Total four-volume is infinite.

## 3. What this changes about the closed Goldberg problem

The explicit branch rules out any local theorem asserting that negative Einstein plus almost-Kähler implies Kähler on the open strict set \(q>0\). The Step-56 uncontrolled symmetric-Hessian mode is geometrically realized. A closed proof must use information unavailable on this branch: topology, recurrence/compactness, an actual field, or the structure near zeros of the Nijenhuis tensor.

Armstrong's topological theorem says that a compact almost-complex four-manifold with nowhere-zero Nijenhuis tensor satisfies
\[
5\chi+6\tau=0.
\]
For an almost-Kähler structure \(N=0\) exactly where \(\nabla\Omega=0\). In the present Einstein problem the apparent exceptional topological equality is itself impossible: a closed Einstein four-manifold satisfies \(2\chi+3\tau\ge0\), whereas \(5\chi+6\tau=0\) gives \(2\chi+3\tau=-\chi/2<0\); here \(\chi>0\) because \(s=-12\ne0\). Consequently **every** closed negative-Einstein almost-Kähler four-manifold has a zero of \(q\). More precisely, the torsion \(T=\nabla\Omega\) is a section of the complex rank-two bundle
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},\qquad
c_2(E)=c_2(TM)+2c_1(TM)^2,
\]
so
\[
\langle c_2(E),[M]\rangle=5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
For its zero set \(Z\), the pullback Thom class gives a nonzero localized class in \(H^4(M,M\setminus Z;\mathbb Z)\). If the zeros are isolated, their signed Brouwer indices sum to \(5\chi+6\tau\); for a nonisolated zero set the supported class remains meaningful, but no pointwise multiplicity or sign follows. The present explicit pair has \(q>0\) at every finite point (including the bolt, where \(q=32/3\)) and \(q\to0\) only at infinity, so it evades this charge rather than realizing it compactly.

The remaining local question is sharply posed: can a negative Einstein almost-Kähler germ have a finite-order torsion zero without being Kähler nearby? Einstein metrics and their harmonic self-dual form are analytic, so infinite-order vanishing would imply local Kählerness, but finite-order zeros remain. In a unitary frame, the leading homogeneous torsion coefficient satisfies
\[
P_m=(f_1d\bar z_1+f_2d\bar z_2)\otimes\ell,
\qquad f_i=z_i h_{m-1}(\bar z)+g_i^{(m)}(\bar z).
\]
For \(m=1\), \(P_1=cz+B\bar z\). Both positive and negative local degrees occur already in this principal class, while the symmetric part of \(B\) is invisible to the leading \(dP_1,d^*P_1\) curvature data. Thus topology plus the principal soldered equation does not decide Goldberg. The first consequential unresolved calculation is the nonlinear prolongation at, for example, \(P_1=cz\), retaining the Levi-Civita soldering, the full Einstein curvature symmetries, and differentiated AAD equations rather than treating \(\eta,W_3^+\) derivatives as free.

## 4. Relation to the defect programme

A02's Steps 71--72 correction is separate but consequential. Because the human functional minimizes over \(\lambda\ne0\), Ricci-flat metrics have \(E=4\), not zero, and the orientation-free identity is
\[
E-1={6(\int|W|^2-8\pi^2\chi)+L_s\over R}.
\]
A long \(\mathbb R\times S^3\) neck gives \(\alpha\le1\) on every closed four-manifold, while \(2\chi\le3|\tau|\) forces \(\alpha=1\); moreover \(\alpha<1\) is equivalent to a strict Weyl deficit \(\inf\int|W|^2<8\pi^2\chi\), with the quantitative formula recorded by A02. This supersedes the orientation-specific summary previously written here. Nothing in the present exact Einstein pair changes that law. The pair itself is noncompact and of infinite volume, so it is a control for differential compatibility and the closed Goldberg problem, not a closed-manifold value of \(\alpha\).

## 5. Literature and novelty

The full Armstrong 2002 paper `An ansatz for almost-Kähler, Einstein 4-manifolds` (DOI 10.1515/crll.2002.009; citation key `armstrong2002ansatz`) remains unavailable; novelty is unresolved. Retrieved self-dual Einstein Bianchi VIII, quaternionic quotient, ACH, and compact self-dual almost-Kähler sources do not identify the displayed rational pair. This absence is not a novelty proof. The metric's geometric validity, end completion, and priority remain separate questions.

## 6. Tool record and correction

The first symbolic script `step58_exact_bianchiVIII.py` generated unmanageable square-root branch expressions and timed out; it is superseded by the quadratic-extension script `step58_exact_bianchiVIII_fast.py`. The attempted global Weyl scripts likewise stopped on branch simplification and are not used. A Wolfram cross-check was prepared at `workspace/scripts/wolfram/inputs/step58_verify.wl`, but the installed Wolfram Engine license is expired, so it produced no mathematical evidence. The TTCS verification task timed out with no result. Exact SymPy reduction plus the independent Koszul engine are the current evidence.
