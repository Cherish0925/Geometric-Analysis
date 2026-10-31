# Step 18 — Corrected transverse Riccati variables, exact CH benchmark, and real-hyperbolic comparison

## 1. The quadratic HJ variable has been repaired

Near the invariant Kähler manifold \(N=\{u_1=u_3=0\}\), set \(\xi=(u_1,u_3)\) and
\[
\Phi=\frac12\xi^TA\xi,
\qquad
A=\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},
\qquad
D=\frac1W\operatorname{diag}(a_1^2,a_3^2).
\]
For an actual transverse Hessian
\[
S=\frac12\xi^TK\xi+O(|\xi|^3),
\]
the quadratic term in \(\mathcal H_S\) is
\[
\frac12D_0K+\frac12(KDA+ADK)+KDK.                 \tag{1.1}
\]
The shifted variable is
\[
Y=K+\frac A2,
\]
and only this shifted variable obeys
\[
\frac12D_0Y+YDY\le\frac14(ADA+D_0A).             \tag{1.2}
\]
Consequently
\[
S=-\Phi:\quad (K,Y)=(-A,-A/2),
\qquad
S=0:\quad (K,Y)=(0,A/2).                         \tag{1.3}
\]
The Step-17 note had combined the ansatz \(S=-\Phi+\frac12\xi^TY\xi\) with the shifted equation and then identified \(Y=0\) with \(S=0\). That was wrong. `notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md` has been corrected in place.

## 2. Exact CH scalar Riccati solutions are the Step-7 ground states

On exact complex hyperbolic space,
\[
a_1=a_3=\sqrt x,
\quad a_2=\sqrt{x(1+x)},
\quad u_2=3x.
\]
In the eigenchannels \(v_\pm\), (1.1) becomes
\[
K_\pm'+\frac{K_\pm(K_\pm+2\pm3x)}{x(1+x)}=0.     \tag{2.1}
\]
For the hard outgoing condition at \(x=1\), the exact Dirichlet-to-Neumann solutions are
\[
K_+(x)=-\frac{2}{\Delta_+(x)},
\qquad
K_-(x)=-\frac{2(1+x)^5}{\Delta_-(x)},             \tag{2.2}
\]
where \(\Delta_\pm\) are the closed expressions from Step 7. SymPy reduces both residuals in (2.1) to zero in `scripts/riccati_ch_benchmark.py`; results are in `data/hj/riccati_ch_benchmark.json`.

If \(z=1/K\), then
\[
z'-\frac{2\pm3x}{x(1+x)}z=\frac1{x(1+x)}.       \tag{2.3}
\]
Its positive homogeneous multipliers are exactly
\[
f_+^2=x^2(1+x),
\qquad
f_-^2=\frac{x^2}{(1+x)^5},                        \tag{2.4}
\]
the squares of the positive zero modes previously proved in Step 7; in the conventional linear-ODE terminology, the integrating factors multiplying (2.3) are \(f_\pm^{-2}\). Thus the Riccati and Sturm descriptions are the same linear Hamiltonian/Jacobi system in different charts.

Numerical propagation of seed-like entrance Hessians \(K_\pm(\rho)=-c(2\pm3\rho)\) illustrates why poles must not be interpreted as negative CH modes. In the minus channel, \(c=1\) gives graph poles at
\[
\rho=.003:.05252,
\quad .01:.10826,
\quad .03:.22632,
\quad .1:.59560.
\]
For \(c=.985\), no pole appears before the numerical cutoff \(x=20\) at \(\rho=.003\), while the first poles occur at \(.51947,.29736,.64553\) for \(\rho=.01,.03,.1\). The `null` field in the data means only absence before that cutoff; the explicit Jacobi formula can still place a later pole. These poles are zeros of the graph block in the Jacobi evolution; the Lagrangian plane remains defined. They retain focal/Maslov information and can obstruct one smooth quadratic graph, but they do not imply a singular Jacobi evolution or a negative compactly supported CH mode. The meaningful matching problem is whether the bolt-side Lagrangian data lie on the admissible side of the outgoing DtN plane, possibly represented through more than one graph chart.

This already changes the proposed experiment: integrate the linear Jacobi/Lagrangian system, or use (2.2) as the outgoing benchmark for the hard target \(x=1\), rather than declaring bulk instability when one Riccati graph develops a pole. For a general terminal point \(X\), the outgoing plane is
\[
K_\pm^X(\rho)=-\left[f_\pm(\rho)^2\int_\rho^X\frac{ds}{s(1+s)f_\pm(s)^2}\right]^{-1},
\]
As \(X\to\infty\), the minus-channel integral diverges and \(K_-^X(\rho)\to0\): the free transverse minus mode alone has vanishing asymptotic DtN cost. The full cell relation must therefore carry the longitudinal torsion-free variable \(\theta=\delta\log(a_1/a_3)\), whose Step-7 moment relation couples back to \(v_-\). This explains why the positive compactly supported CH operator is insufficient for a large-collar lower bound.

## 3. Correctly normalized \(H^4\) comparison

The round profile \(a_i=\sinh t\) has \(\operatorname{Ric}=-3g\). In the common \(\operatorname{Ric}=-6g\) normalization it is
\[
a_i(t)=\frac1{\sqrt2}\sinh(\sqrt2t).             \tag{3.1}
\]
The coordinate used by the cell code is \(x=a^2\); hence an exact real-hyperbolic collar is
\[
F=x,
\qquad G=x+2x^2,
\qquad w=0.                                       \tag{3.2}
\]
The symbolic check in `scripts/u2_general_cell.py verify` gives \(s=-24\) and \(P\)-density zero for this collar.

I built `scripts/h4_perp_cell.py`, the triaxial analogue of the certified CH perpendicular ansatz, with an ordinary \(O(-1)\) bolt and exact collar (3.2). An initial base profile had the wrong bolt derivative for \(G\); it was repaired so that the unexponentiated base has \(F'(x_0)=G'(x_0)=1\), and the coefficient shift enforces \(q_F(0)+q_G(0)=0\). The main \(X=64\) files prefixed `corrected_`, and the later `biaxial_` and `random{1,2}_` files, use the repaired profile. Earlier unprefixed `perp_` files are superseded and must not be used.

Floating-point optimized \(P/(8\pi^2)\) values at \(X=64\), degree 16, are
\[
\begin{array}{c|c|c|c}
x_0&P/(8\pi^2)&J_6/(8\pi^2)&\max|w|\\\hline
.003&1.0060563827&1.0061852180&4.4\times10^{-5}\\
.01&1.0204668804&1.0216523289&6.5\times10^{-5}\\
.03&1.0630695665&1.0721494158&3.6\times10^{-5}
\end{array}                                                     \tag{3.3}
\]
The corresponding files are `data/h4_cells/corrected_perp_x0.{003,01,03}_X64_P_d16.json`. For \(x_0=.01\), the seeded larger-collar run changed \(P\) from \(1.0205588060\) at \((X,\deg,n_q)=(8,12,800)\) to \(1.0204668804\) at \((64,16,1000)\), and every tested cell remained above the topological threshold. Because the basis and quadrature also changed, this is not a one-parameter collar comparison. The older biaxial code independently found \(P=1.0647909208\) at \((x_0,X)=(.03,4)\). The optimized \(\|w\|_\infty\) is extremely small. Two additional degree-12, \(X=8\), \(x_0=.01\) random anisotropic starts converged to \(P=1.0205583805\) and \(1.0205583791\), while the exactly biaxial run gave \(1.0205615593\). Thus a tiny symmetry-breaking improvement of about \(3.18\times10^{-6}\) is reproducible within this ansatz, but it is four orders of magnitude smaller than the positive excess. `scripts/h4_anisotropy_hessian.py` evaluated the degree-12 \(w\)-sector at the biaxial optimum: all Hessian eigenvalues are positive, from \(3.24\times10^{-5}\) to \(.734\), and the quadratic Newton gain \(2.97\times10^{-6}\) agrees with the direct optimization. The nonzero \(w\)-gradient \(2.57\times10^{-4}\) indicates that the chosen \(w=0\) slice is not stationary in this slot parametrization; the metric is numerically near-biaxial, not exactly forced to be biaxial.

These runs are numerical constructions, not a proof that \(P_{1,0}^{H^4}=8\pi^2\). The gradients remain around \(10^{-5}\); only two random anisotropic restarts were made at one parameter point, and no systematic degree/quadrature refinement or interval enclosure was performed. They do provide a useful contrast: in the tested finite-dimensional diagonal class, no large-collar subthreshold mechanism was detected. The excesses satisfy \((P-1)/x_0\approx2.02,2.05,2.10\) at \(x_0=.003,.01,.03\), consistent with the first-order response from \(R^+=(s/12)I=-2I\). This supports the curvature-response picture that \(H^4\) charges every Burns direction at first order, while CH has a perpendicular kernel enabling a second-order signed interaction.

## 4. Consequences

1. The CH bulk question remains controlled by the exact positive ground states. The zero of the relative primitive at \(u_2=2\) concerns matching a bolt-side calibration to outgoing data, not a compactly supported instability.
2. The corrected boundary data are \(Y=-A/2\) for the seed and \(Y=A/2\) for zero. Any tube calculation or subsolution optimization must use these values.
3. A continuous restricted lower result would require a uniform Hamiltonian inequality on a specified tube and an independent estimate for diagonal trajectories leaving it. Sampled near-optimal values alone do not do this.
4. The next lower-theory calculation should transport a Lagrangian subspace through the core and compare it with the exact outgoing planes (2.2), while adding the longitudinal torsion-free state. This can survive Riccati chart changes and is the appropriate linear precursor to a nonlinear HJ construction.
5. The \(H^4\) result should remain a comparison branch. It suggests, but does not establish, that the sign/kernel structure of \(R^+\) separates first-order rigidity from finite-scale CH saving.

## 5. Independent and formal checks

Two independent TTCS readings found the \(K/Y\) algebra, CH Riccati equations, DtN factors, \(H^4\) normalization, bolt smoothness, collar two-jet contact, and energy normalization consistent. They prompted the clarified terminology and scope above: \(f_\pm^2\) are homogeneous multipliers rather than the conventional integrating factors; `null` records a bounded integration window; the displayed DtN formulas use the hard target \(x=1\); and graph-chart continuation does not remove the endpoint order needed for a valid subsolution. The integrations are saved under `trace/ttcs/results/step18_ttcs01_verifier1_integration.md` and `step18_ttcs01_verifier2_integration.md`.

The scalar shift identity and its seed/zero boundary translations are formalized in `workspace/proofs/RiccatiShift.lean`. `workspace/proofs/riccati-shift-check.json` dependency-checks `RiccatiShift.qiushi_scalar_shift` using only the configured allowed Mathlib axioms. This formal check certifies the algebraic shift, not the geometric derivation of the transverse HJ system.
