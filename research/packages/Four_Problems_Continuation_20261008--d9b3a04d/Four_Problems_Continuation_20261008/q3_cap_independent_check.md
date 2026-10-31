# Independent check of the AE standard-cap connection

The proposition in `q3_work.md` is valid under its stated smooth one-ended AE, scalar-flat, decay and Betti-number hypotheses. I checked the following points independently.

## Fixed AE homogeneous Sobolev inequality

This does not require a uniform Sobolev constant across all bubbles. For one fixed end, choose a fixed annulus in the AE chart. For a compactly supported smooth function,
\[
u(r,\theta)=-\int_r^\infty\partial_tu(t,\theta)\,dt,
\]
so Cauchy--Schwarz gives
\[
|u(r,\theta)|^2\le\frac1{2r^2}\int_r^\infty |\partial_tu|^2t^3\,dt.
\]
After integrating over a fixed annulus, its \(L^2\) norm is bounded by the end Dirichlet integral. On a fixed connected compact interior together with this annulus, Poincaré with the mean anchored on the annulus controls the compact-interior \(L^2\) norm by the total Dirichlet integral. Ordinary local Sobolev on that compact domain, and Euclidean Sobolev on the cutoff end, then give the global homogeneous inequality. Uniform quasi-isometry of the truncated metrics transfers it with a common constant for all sufficiently large truncation radii.

## Scalar-curvature and compactification steps

The original scalar curvature is zero. The truncated metric changes only in an annulus with \(s_-=O(R^{-2-\tau})\) and volume \(O(R^4)\), so \(\|s_-\|_2=O(R^{-\tau})\). This is enough for positivity of the conformal Laplacian form. The Weyl energy change is \(O(R^{-2\tau})\). Multiplication by a positive function equal to \(r^{-2}\) on the exactly Euclidean tail produces an exactly Euclidean inverted metric near the added point. The conformal energy identity is valid for functions supported away from that point. A point has zero \(H^1\) capacity in dimension four, so the positive inequality extends to all smooth functions on the cap.

## CGY normalization

I read the original Chang--Gursky--Yang paper, arXiv:math/0309287, pp. 2--3. Its Theorem A uses
\[
\int|W_{(0,4)}|^2<16\pi^2\chi
\]
and the paper explicitly states \(|W_{(0,4)}|^2=4|W_{\mathrm{op}}|^2\). The AE relative identity and \(b_1=b_2=0\) give
\[
\chi(N)=1,\quad \chi(\widehat N)=2,\quad
\int|W_{(0,4)}|^2=2P.
\]
Thus the strict threshold is exactly \(P<16\pi^2\). Orientation excludes \(\mathbb RP^4\). No Bach-flat assumption appears in Theorem A.

Primary source: https://arxiv.org/pdf/math/0309287 ; 

## No hidden smooth Schoenflies assumption

After CGY, \(\widehat N\cong S^4\). Removing the actual added point immediately gives \(N\cong\mathbb R^4\).

If a compact core is needed, take the complement of a small coordinate ball around the added point. Under a diffeomorphism \(\widehat N\to S^4\), the removed neighbourhood is the image of an actual smooth disk embedding \(f:D^4\to S^4\). For fixed small \(\varepsilon>0\), the family \(f_t(x)=f(tx)\), \(\varepsilon\le t\le1\), is an isotopy of disk embeddings. Isotopy extension, followed by local linearization in a coordinate chart, identifies its image with a small standard ball. Its complement is therefore a standard disk.

This argument is different from assuming that an arbitrary embedded \(S^3\subset S^4\) bounds a disk: here one side is known from the construction to be the image of \(D^4\). No general smooth four-dimensional Schoenflies statement is used.

The application still needs the independent input \(b^+=0\), the smooth trivial-group end, compact smooth bulk, and the reconstruction/energy hypotheses listed in `q3_work.md`. The cap theorem does not establish those inputs.
