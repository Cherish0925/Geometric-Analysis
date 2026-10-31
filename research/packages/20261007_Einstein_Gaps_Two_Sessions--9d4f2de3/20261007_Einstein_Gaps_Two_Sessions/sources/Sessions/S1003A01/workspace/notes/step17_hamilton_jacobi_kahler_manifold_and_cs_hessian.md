# Step 17 — Hamilton–Jacobi structure of the diagonal cell problem, the Kähler manifold \(N\), and where the relative Chern–Simons calibration loses control

Normalization: perpendicular diagonal Bianchi IX cells, slots \((a_1,a_2,a_3)=(\sqrt x,\sqrt{xe^w},\sqrt F)\) (Step 7), \(a_3\) collapsing at the bolt, \(a_2\) the CH Kähler direction. \(P/(8\pi^2)=\int L\,dt\), \(L=\tfrac14W|z|^2\), \(W=a_1a_2a_3\), \(z\) the complete diagonal trace-free Ricci variable of Step 16. Every identity below is checked symbolically in `scripts/hj_structure.py` (output `data/hj/hj_structure_check.txt`, all residuals 0) and `scripts/check_variable_seed.py`.

## 1. The cell problem as an optimal-control problem

With \(\gamma_i=(a_j^2+a_k^2-a_i^2)/(a_ja_k)\), \(u_i=\dot a_i-\gamma_i\), \(H_i=u_i+\tfrac12u_ju_k\), \(\lambda_i=a_ja_k/a_i\), the exact equations are
\[
\dot a_i=u_i+\gamma_i(a),\qquad \dot u_i=\frac{2H_i}{\lambda_i}+a_iz_i ,
\]
so a diagonal cell is a controlled trajectory in the six-dimensional state space \((a,u)\), with control \(z\) and running cost \(L\). The \(u_i\) are the components of the \(\Lambda^+\) spin connection in the invariant frame, \(H_i\) its curvature, and \(C=\sum u_i^2+u_1u_2u_3\) its Chern–Simons function (Step 7, (1.2)). Zero control means \(\operatorname{Ric}^\circ=0\): the free flow \(D_0\) is the Einstein flow of every sign of Einstein constant.

**(H1) Square completion.** For every state function \(S(a,u)\),
\[
L-\frac{dS}{dt}=\frac W4\sum_i\Big(z_i-\frac{2a_iS_{u_i}}W\Big)^2-\mathcal H_S,\qquad
\mathcal H_S=D_0S+\frac1W\sum_ia_i^2S_{u_i}^2 .
\]
Hence \(\mathcal H_S\le0\) along a cell gives \(P/(8\pi^2)\ge S(\text{out})-S(\text{bolt})\). This is the Strategist's formula, now verified. \(\mathcal H_S=\mathrm{Ham}(a,u,\nabla S)\) for the Pontryagin Hamiltonian
\(\mathrm{Ham}=p_a\cdot(u+\gamma)+p_u\cdot(2H/\lambda)+W^{-1}\sum a_i^2p_{u_i}^2\) (maximizing control \(z=2a\,p_u/W\)). The value function \(V\) (least cost to reach the CH curve) gives the exact subsolution \(S=-V\) with \(\mathcal H_S=0\); the diagonal cell infimum is \(V(\text{bolt})\).

**(H2) Seed.** For \(\Phi=C-u_2^2\), \(\mathcal H_{-\Phi}=-2u_1u_2u_3/\lambda_2\), which is the relative calibration (1.5) of Step 7. For \(S=-c\Phi\),
\[
-\mathcal H_{-c\Phi}=c(1-c)Q+c\kappa,\qquad Q=\frac1W\sum_ia_i^2\Phi_{u_i}^2\ge0,\quad \kappa=\frac{2u_1u_2u_3}{\lambda_2},
\]
and exactly \(P/(8\pi^2)=c+\int\frac W4|z+2c\,a\nabla_u\Phi/W|^2+\int[c(1-c)Q+c\kappa]\). The quartic parts of \(D_0\Phi\) and \(Q\) cancel identically, so \(\Phi\) is an exact calibration up to the cubic.

**(H3) Hamiltonian constraint.** \(\Lambda=-8\sum_ia_iH_i/W\) \((=2s-4\operatorname{Ric}_{00}=-4G_{00})\) is a first integral of \(D_0\), and \(s=\Lambda-2\sum_iz_i\). Its controlled derivative is linear in \(z\) (contracted Bianchi identity; formula in the check output). A function of \(\Lambda\) alone has \(\mathcal H\ge0\) and cannot calibrate.

**(H4) Scaling charge.** \(\sum_ia_i\partial_{a_i}\mathrm{Ham}=-(\mathrm{Ham}-p_a\cdot(u+\gamma))\), hence \(\frac d{dt}\sum_ia_ip_{a_i}=\mathrm{Ham}\) along extremals. Because \(P\) is scale invariant and the CH end set is scale invariant for \(P\), optimal extremals have \(\mathrm{Ham}=0\) and conserve \(\sum a_ip_{a_i}\). In particular the bolt scale \(b\) is a gauge for \(P\): in scale-reduced variables the bolt is the single point \((a_3/a_1,a_2/a_1,u)=(0,1,(0,0,-1))\), the CH collar is the curve \(\{a_1=a_3,\ u_1=u_3=0,\ u_2=3(a_2^2/a_1^2-1)\}\), and the observed interior optimum \(x_0\approx.03\) is a property of where the optimal reduced trajectory meets that curve relative to the collar curvature. (For \(J_6\) the scalar term breaks scaling, but only at the \(10^{-5}\) level on the good cells.)

**(H5)** For scale-invariant \(S\), \(\mathcal H_S\) is homogeneous of degree \(-1\) in \(a\), so the subsolution inequality lives on the five-dimensional reduced state space.

**Collar extension and the Gram obstruction.** The Strategist is right that the Step-16 target "uniform upper spectral bound on \(G\)" is false: appending an exact CH annulus leaves \(P\) unchanged while the constant shape fields have \(\|B\|^2\propto\int W\,dt\to\infty\). Only the invariant \(m^TG^\dagger m\) (which is what Step 16 computed) or the HJ form is meaningful. In the HJ form the issue disappears: \(\Phi\) and \(\nabla_u\Phi\) vanish on the whole CH curve, so any \(S=-\Phi+\psi\) with \(\psi\) and \(\nabla_u\psi\) vanishing there is constant on CH and insensitive to collar extension.

## 2. The Kähler manifold \(N=\{u_1=u_3=0\}\)

(H6–H7) \(N\) is invariant under \(D_0\); \(\Phi\) and \(\nabla_u\Phi\) vanish on \(N\); and on \(N\), \(\frac d{dt}(a_1a_3)=2a_2\), i.e. \(\omega_2=a_2\,dt\wedge\sigma_2+a_3a_1\sigma_3\wedge\sigma_1\) is closed. \(N\) is the set where the \(\Lambda^+\) connection reduces to \(U(1)\) (only \(u_2\) survives), i.e. the states of metrics Kähler for \(\omega_2\) — the complex structure of CH. CH is the Kähler–Einstein trajectory in \(N\). Thus \(\Phi=CS(A)-u_2^2\) is the Chern–Simons function of \(A\) relative to its \(U(1)\)-reduction, and the calibration is exact on Kähler states. Note \(a_1=a_3\) is invariant inside \(N\) (since \(\frac d{dt}(a_1^2-a_3^2)=2W^{-1}(a_1^2-a_3^2)(a_2^2-a_1^2-a_3^2)\) there), but \(N\) also contains triaxial Kähler states.

Near \(N\), with \(\xi=(u_1,u_3)\) and \(v_\pm=(u_1\pm u_3)/\sqrt2\),
\[
\Phi=\Big(1+\frac{u_2}2\Big)v_+^2+\Big(1-\frac{u_2}2\Big)v_-^2\qquad(\text{exactly}).
\]
\(\Phi\) is the transverse Chern–Simons Hessian at the reducible connection \(u_2\sigma_2\). Its \(v_-\) eigenvalue crosses zero at \(u_2=2\) (on CH: \(x=2/3\)) — a spectral-flow crossing of the transverse Hessian. Write the transverse Hessian of a candidate as
\[
S=\tfrac12\xi^TK\xi+O(|\xi|^3),\qquad
A=\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},\qquad
D=\operatorname{diag}(a_1^2,a_3^2)/W.
\]
The quadratic Hamiltonian inequality is
\[
\tfrac12D_0K+\tfrac12(KDA+ADK)+KDK\le0.                  \tag{2.1}
\]
After the shifted variable \(Y=K+A/2\), and only after this shift, it becomes
\[
\tfrac12D_0Y+YDY\le\tfrac14\big(ADA+D_0A\big),\qquad
D_0A=\frac{2u_2}{\lambda_2}\begin{pmatrix}0&1\\1&0\end{pmatrix}. \tag{2.2}
\]
Thus the relative seed \(S=-\Phi=-\tfrac12\xi^TA\xi\) has \(K=-A\) and \(Y=-A/2\), whereas the identically zero function has \(K=0\) and \(Y=A/2\). The earlier version of this note incorrectly inserted the shifted variable into the ansatz and then identified \(Y=0\) with \(S=0\); that convention is superseded by (2.1)--(2.2).

At \(u_2=2\), \(A\) loses one eigenvalue. This shows failure of the particular relative primitive \(-c\Phi\) in the \(v_-\) channel; it is not evidence for a negative compactly supported CH mode, since the Step-7 positive ground states control the latter. The mathematical issue is whether bolt-side Hessian data can be transported to a valid outgoing graph. A pole in \(K\) or \(Y\) may only be failure of that graph chart; the associated linear Hamiltonian/Jacobi system must be followed before concluding that no piecewise or nonsmooth calibration exists.

## 3. What the certified cells do in this picture

`scripts/hj_witness_analysis.py` (data `data/hj/witness_seed.json`) and `scripts/hj_failure_locus.py` (data `data/hj/cs_hessian_failure.json`):

* The identity of (H2) holds numerically to \(10^{-8}\) for \(c=1,\frac12\).
* The cubic \(\kappa\) is negative essentially along the whole transition: \(\int\kappa_+\le8\times10^{-5}\) against \(\int\kappa_-=-6.1\times10^{-4},-5.3\times10^{-3},-3.25\times10^{-2},-1.35\times10^{-1}\) for \(x_0=.003,.01,.03,.1\) at \(X=64\).
* The set \(F_0=\{Q+\kappa<0\}\), where no \(c\in(0,1]\) works pointwise, is the same band on every cell: \(t\in[0.53,1.18]\), \(u_2\in[1.07,6.55]\), with the transverse displacement more than \(90\%\) in \(v_-\) and the state within \(0.012\)–\(0.24\) of \(N\). It straddles the spectral crossing \(u_2=2\). Only \(5\)–\(10\%\) of \(\int\kappa_-\) lies in \(F_0\). Hence \(c_{\max}<0\) for every witness: even restricted to the witness's own trajectory, the seed family fails pointwise.
* **Costate.** Equality in (H1) gives the value-function gradient \(p_u=Wz/(2a)\). In the control metric \(a_i^2/W\), \(p_u\) projects onto \(-\nabla_u\Phi\) with coefficient \(0.9852\) and share \(97.2\%\) at \(x_0=.03\), and \(0.99894\) and \(99.96\%\) at \(x_0=.003\). Pointwise (`scripts/hj_local_f.py`, `data/hj/local_f_*.csv`), in the core \(t\le0.3\), where 92% of \(P\) is paid, the cosine with \(-\nabla\Phi\) exceeds \(0.99\) and the local coefficient is \(f\approx0.985\)–\(0.99\). It rises above \(1\) for \(0.3<t<0.6\) as \(\Phi\to0\), and alignment is lost in the band \(F_0\) (cosine \(\to0\) near \(u_2\approx2\)–\(3.4\)). Beyond the band, \(f\) varies freely while \(\Phi\approx0\).

Interpretation. The near-optimal value function is, to about one percent, the relative Chern–Simons charge with a slowly varying coefficient: \(V\approx f(a,u_2)\,\Phi\). For the variable seed (checked symbolically),
\[
\mathcal H_{-f\Phi}=-f\big[(1-f)Q+\kappa\big]-\Phi\,D_0f+\frac{a_2^2\Phi f_{u_2}}W\big(2f\Phi_{u_2}+\Phi f_{u_2}\big).
\]
Near the bolt \(f<1\) lets \(-f(1-f)Q\) absorb the cubic. The rise of \(f\) above 1 outward is paid by \(-\Phi D_0f<0\) while \(\Phi>0\). Across the band \(F_0\), \(\Phi\) changes sign (\(u_2>2\) makes the \(v_-\) coefficient negative), so a decreasing \(f\) there helps rather than costs. Along one fixed trajectory, ignoring \(f_{u_2}\), \(\mathcal H=0\) is a Bernoulli equation. With \(g=1/f\) it becomes linear,
\(\dot g=g(Q+\kappa)/\Phi-Q/\Phi\), and the bounded solution gives
\(g(0)=\int_0^\infty\frac Q\Phi\exp\!\big(-\int_0^s\frac{Q+\kappa}\Phi\big)ds\). Negative \(\kappa\) forces \(g>1\), i.e. \(f(\text{bolt})<1\). This is the one-dimensional shadow of the saving mechanism. It is not a uniform bound, because a certificate needs \(\mathcal H\le0\) off the trajectory as well.

## 4. Failed formulation preserved

`scripts/hj_socp.py` poses the subsolution problem as a convex second-order-cone program in the coefficients of \(S=-c\Phi+\sum\theta_kb_k(q,w,y)m_k(u_1,u_3)\), with \(\mathcal H_S\le0\) on sampled states. With samples only on the witness trajectory the problem is degenerate: \(S\) is unconstrained off the curve, coefficients blow up, Clarabel fails, and SCS returns `optimal_inaccurate` with \(\max\mathcal H>0\) on the samples. The values \(0.9966\) and \(1.0039\) are meaningless. A usable version needs (i) a tube of states with bolt-regular perturbations, (ii) an orthogonalized basis adapted to \(N\) (transverse quadratic forms in \(v_\pm\) with coefficients in \((u_2,a\text{-shape})\)), and (iii) separate treatment of the bolt chart, where \(a_1/(a_2a_3)\to\infty\) forces \(S_{u_1}\to0\). No number from this script may be used.

## 5. Consequences for the lower theory

1. The diagonal infimum is the value \(V(\text{bolt})\) of a point-to-curve control problem on a five-dimensional reduced state space. A lower theorem is a subsolution of \(\mathcal H_S\le0\). The near-optimal \(S\) is \(-f\Phi\) with \(f\approx0.99\) on the bolt side.
2. The only place where the tested \(u\)-only relative primitive fails pointwise is a neighbourhood of the Kähler manifold \(N\) around the zero of its \(v_-\) Hessian at \(u_2=2\). The required correction is a transverse quadratic form governed by (2.1), or equivalently the shifted equation (2.2) with the corrected boundary data \(Y=-A/2\) for the seed and \(Y=A/2\) for the zero function. The associated linear Hamiltonian/Jacobi system, rather than a Riccati graph alone, decides whether bolt-side data can be connected through this region.
3. The cheap mechanism of the certified cells has a geometric description: they leave the bolt carrying almost the full relative charge \(\Phi\), shed it in the core with near-exact calibration, and approach the Kähler manifold of the CH complex structure through the band where the transverse Chern–Simons Hessian degenerates. There the signed cubic can be negative at second order in the distance to \(N\).
4. Step 16's "uniform Gram bound" is replaced by HJ constancy on the CH curve. The small-\(b\) alternative becomes a statement about trajectories passing near the flat fixed point \(u=0,\ a_1=a_2=a_3\) (the AE regime), where \(\Phi\) is exact up to \(\kappa\) and \(Q\) dominates. Large \(b\) corresponds to reduced trajectories that reach \(N\) far out along the CH curve.

Everything here is internal to the diagonal perpendicular class. It does not bound unrestricted cells or the all-metric balanced coefficient.

## 6. Cross-session points recorded this step

* Peer S1003A02 (message 772) proposes a first-order Burns response for an arbitrary closed bulk, \(P(\hat g)=P(g)+8\pi^2(1-x_0R^+_p(\zeta,\zeta))+O(x_0^{6/5})\). Our Step-8 U(2) infima (`data/u2_general/`) independently give the same slopes in all four tested backgrounds: \(H^4\) \(+2.0048\), \(S^4\) \(-1.9977\), aligned CH and FS \(\pm6\). They do not re-derive the peer's transgression matrices. For \(H^4\) the slope grows with \(x_0\) at small collar (\(2.016\to3.248\) for \(x_0=10^{-4}\to10^{-2}\), \(X=.25\)). Whether a large collar opens a finite-scale saving below \(8\pi^2\) over \(H^4\), as it did for perpendicular CH, is open. That test needs the relative charge rebuilt for the \(H^4\) end connection \(u_i=\cosh t-1\), which has no reducible \(U(1)\) structure and a positive cubic. Reply: message 773.
* Corrected bolt-chirality values sent as message 771; the peer integrated them (message 772). Non-Kähler for either orientation follows from the Kähler–Einstein spectrum \((-4,2,2)\).
* The \(x_0=3/100\), \(X=256\) Arb enclosure (task s15_t32_tool1) hit its 7200 s limit. `data/perp_area/rigorous_x00.03_X256_d24.json` is an empty file and is not a certificate. The certified record remains \(X=128\): \(J_6/(8\pi^2)\le0.9956710815\).
