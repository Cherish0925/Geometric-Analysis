# Step 90 support — the gauge-invariant part of the TN dipole, and the location of line curvature

This is a focused consequence of the proposed formula (90.1), not a closed-field construction or a new gap theorem. Write
\[
\sigma_\tau=C\frac{\ell\bar f}{(r+\ell)^3},\qquad f=x_1+ix_2,\qquad C^2=\rho_*m_*^3=\frac{8388608}{1594323}.
\]
The subscript distinguishes the raw model \(\Phi\wedge t(\tau;\nabla\tau)\) from the finite-density proof's section formed from its actual bounded resolvent \(v\).

## 1. A connection cannot cancel the amplitude energy

On TN, \(V=1+\ell/r\), with fibre period \(4\pi\ell\),
\[
|\sigma_\tau|=C H(r)\sin\theta,\qquad H(r)=\frac{\ell r}{(r+\ell)^3}.
\]
For fibre-invariant scalars, \(|dh|_g^2=V^{-1}|dh|_{\mathbb R^3}^2\), whereas the volume density is \(Vr^2\sin\theta\). The factors \(V\) cancel. Thus
\[
\int |d|\sigma_\tau||^2
=8\pi^2\ell C^2\int_0^\infty
\left(\frac43r^2H'(r)^2+\frac23H(r)^2\right)dr.
\]
With \(t=r/\ell\), the two radial integrals are
\[
\int_0^\infty\frac{t^2(1-2t)^2}{(1+t)^8}\,dt=\frac2{105},\qquad
\int_0^\infty\frac{t^2}{(1+t)^6}\,dt=\frac1{30}.
\]
Consequently
\[
\boxed{\int |d|\sigma_\tau||^2=\frac{8\pi^2C^2}{21}
=\frac5{12}\int|d\sigma_\tau|^2
=\frac{67108864\pi^2}{33480783}.}
\]
The ordinary energy is \(32\pi^2C^2/35\), as in (90.2). These radial integrations were checked exactly with SymPy; stdout is `Sessions/S1003A01/trace/shell/9d955b3ff4d64add9369cddb68dcf28c/stdout.log`.

For **every unitary connection on the line carrying this same section**, Kato gives
\[
\int|\nabla^{5A}\sigma_\tau|^2\ge\int|d|\sigma_\tau||^2.
\]
Thus the connection cannot erase the critical energy of this dipole. It can change the phase part; computing its exact energy is not needed to decide survival of the amplitude cost. On a truncation \(r\le R\), with \(R/\ell\to\infty\), the omitted amplitude energy is \(O(C^2(\ell/R)^3)\).

This is not a universal per-nut lower bound for actual endpoint sequences. Such a transfer needs the model to be forced and its modulus to converge at the required rescaled derivative level. For a fixed spinor, adding a scalar line-connection term to its derivative cancels in the wedge defining cubic torsion, since v∧(a v)=0. Thus the explicit scalar connection term does not change this raw algebraic projection when the model fields are held fixed. Solving the coupled field and resolvent equations can change the fields themselves; Kato does not identify that corrected section with this one.

## 2. The determinant-line characteristic density cannot concentrate in vanishing-volume cores

The inherited density-free strong-current statement gives, in normalized norms,
\[
F_A:=-iF_{\mathcal A}=F_0+e,\qquad |F_0|\le C,\qquad\|e\|_{2,\mathrm{av}}\to0,
\]
while \(a^2/V\to1/(6\pi^2)\). See `Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex`, the strong-current lemma and equations `finite-density-determinant-fit`, `finite-density-characteristic-limit`.

For any sets \(U_j\) of normalized volume \(\mu_j(U_j)\to0\),
\[
\left|\frac1{V_j}\int_{U_j} F_A\wedge F_A\right|
\le2C^2\mu_j(U_j)+2\|e_j\|_{2,\mathrm{av}}^2\longrightarrow0.
\]
The same holds for \(F_{L^5}=5F_A\). In the proposed phase with \(N\asymp V/\ell^2\) nuts, fixed rescaled cores have total normalized volume \(N\ell^4/V=O(\ell^2)\). They can carry \(W^-\) curvature and rank-two/Euler charge, but not the nonzero normalized **Chern–Weil square of this determinant line**.

This does not prohibit a singular current representation of the line class supported on zero surfaces. It says that such a representation requires its own relative transgression and boundary matching; the \(W^-\) charge of a nut is not automatically \(c_1(L^5)^2\). TN is topologically \(\mathbb R^4\), so its line bundle has no nonzero absolute first Chern class. Its relative boundary data remain meaningful.

## 3. The model's phase and amplitude are macroscopic matching questions

The zero locus of (90.1) is the entire preimage \(f^{-1}(0)\), not only the nut. Over the two halves of the \(x_3\)-axis these are two-dimensional sets reaching every outer truncation boundary. Hence \(\sigma_\tau\) itself does not give a nowhere-zero phase trivialization of that boundary.

On the flux-radius block \(R_\ell\asymp\ell^{1/3}\), its volume is \(\asymp\ell^2\). For each fixed threshold \(b>0\),
\[
|\sigma_\tau|>b\implies r<\sqrt{C\ell/b},\qquad
\frac{\operatorname{Vol}\{|\sigma_\tau|>b\}}{\operatorname{Vol}(B_{R_\ell})}
=O_b(\ell^{1/2})\longrightarrow0.
\]
Thus the raw section tends to zero in normalized measure on these blocks, despite \(\int|\sigma_\tau|^2\asymp\ell^2\) and a scale-invariant derivative cost. This is a concentrated-amplitude phenomenon, not a positive-modulus section with a few bad points. The finite-density line lemma's positive-modulus hypothesis is independently missing.

The useful finite-block calculation therefore concerns whether the **actual** connection, spinor and bounded resolvent can realize this c-depleted exterior and match their phase/zero-surface traces while retaining the nonzero determinant square. A complete ordinary-to-covariant energy coefficient alone would not answer that question. Track the relative line current and determinant pairing separately from the rank-two nut charge.

## 4. Evidence level of (90.1)

The current `step90_tn_sigma_projection.py` computes a symbolic Hessian but evaluates the spinor contraction by floating samples; `step90_tn_sigma_exact.py` recovers \(C^2\) from sampled decimals using `nsimplify`, then performs exact radial integration. The amplitude and scaling consequences above are exact **conditional on (90.1)**. An algebraic derivation of the contraction would promote the model formula itself from a strongly supported identification to an exact identity; it does not require another parameter sweep.

## 5. A useful continuity statement for the actual bounded resolvent

There is a cheaper way to compare the line-section **modulus in measure** than solving the full core resolvent again. Work with the same metric, spinor bundle and actual connection on each closed member. Suppose the already used hypotheses hold:
\[
\|v-\tau\|_{H^1,\mathrm{av}}\to0,\qquad |v|\le C,\qquad
\||\tau|^2-m_*\|_{2,\mathrm{av}}\to0,\qquad |\Phi|\le C.
\]
The last mass convergence makes \(|\tau|^4\) uniformly integrable. Splitting at a fixed \(|\tau|\)-threshold and using the boundedness of \(v\) therefore gives \(\|v-\tau\|_{4,\mathrm{av}}\to0\), without a Sobolev inequality. The cubic algebra yields
\[
\|\Phi\wedge(t(v)-t(\tau))\|_{1,\mathrm{av}}
\le C\bigl[(\|v\|_4+\|\tau\|_4)\|v-\tau\|_4\|\nabla v\|_2
+\|\tau\|_4^2\|\nabla(v-\tau)\|_2\bigr]\longrightarrow0.
\]
Thus, under these hypotheses, \(\sigma_v-\sigma_\tau\to0\) in measure. A raw actual-field section that is c-depleted in measure cannot be changed into a positive-constant-modulus section merely by this bounded H¹-close resolvent. This does not transfer its H¹ energy: it is only an L¹/measure comparison. The strong-current lemma provides the mass and first-derivative hypotheses without Euler-density control, and the displayed proof of resolvent H¹ approximation in `finite_density_endpoint.tex` uses no opposite-Weyl bound before the subsequent second-derivative estimate. Core should check this continuation under its exact sequence assumptions.

The model still needs a common-connection physical field realization and its blockwise/global approximation. The continuity estimate removes a potential redundant local calculation; it does not produce those fields or decide whether they can close.
