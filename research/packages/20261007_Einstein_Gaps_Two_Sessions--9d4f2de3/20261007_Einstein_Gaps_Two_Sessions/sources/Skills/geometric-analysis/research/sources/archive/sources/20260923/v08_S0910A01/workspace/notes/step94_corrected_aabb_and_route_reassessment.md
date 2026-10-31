# Step 94: corrected AA/BB principal response and route reassessment

Session `S0910A01`. Agent1 / Orchestrator. Phase Explore.

## 1. What was corrected

Step 93 concluded that the AA/BB trace-free tensor sectors of the product-orbifold chirality-odd Green response diverged. That conclusion is withdrawn. The error is not an overall prefactor but a **relative electric/magnetic normalization error**.

For an L2-normalized scalar harmonic on the unit sphere with
\[
-\Delta f=\mu f,\qquad \mu=\ell(\ell+1),
\]
the electric trace-free tensor
\[
E(f)=(\nabla^2 f)^{TF}
\]
has
\[
\|E\|^2=\frac12\mu(\mu-2).
\]
At a pole, if the real \(m=2\) Hessian amplitude is written as \(2b\), then the off-diagonal electric pole amplitude is \(2b\).

For the magnetic tensor in Step 93,
\[
M(f)=L_{(\ast df)^\#}g,
\]
one has pointwise
\[
M=2\begin{pmatrix}-c&a\\a&c\end{pmatrix}
\quad\text{if}\quad
E=\begin{pmatrix}a&c\\c&-a\end{pmatrix}.
\]
Thus
\[
\|M\|^2=4\|E\|^2=2\mu(\mu-2),
\]
and the pole amplitude is \(4b\). Step 93 used the electric norm for this full-Lie magnetic tensor. Equivalently, one may work with \(M/2\), whose amplitude and norm match the electric convention. The normalized contributions are invariant under this choice.

Artifacts:
- corrected script: `workspace/scripts/step94_corrected_aabb_principal_response.py`
- corrected data: `workspace/data/step94_corrected_aabb_principal_response.json`
- TTCS verification: `trace/ttcs/results/step94_ttcs01_verifier1_integration.md`
- superseded Step 93 notes/scripts now carry correction notices.

## 2. Corrected AA/BB cancellation and finite adjacent value

Using the transported pole signs from Step 93/94, at separated antipodal poles:
\[
E_{01}(N)E_{01}(S)=-(-1)^\ell(2b)^2,
\]
while
\[
M_{01}(N)M_{01}(S)=(+1)(-1)^\ell(4b)^2.
\]
After division by the correct norms \(N_E=\mu(\mu-2)/2\) and \(N_M=4N_E\),
\[
\frac{E_{01}(N)E_{01}(S)}{N_E}+
\frac{M_{01}(N)M_{01}(S)}{N_M}=0
\]
mode by mode. Therefore the sectors whose **tensor** factor is separated vanish in the principal product-background response:
\[
K^{BB}_{NS}=0,\qquad K^{AA}_{SN}=0.
\]
The same argument also kills the displayed \(SS\) AA/BB principal response.

At the same pole the signs are the same, and the two normalized polarizations reinforce equally:
\[
\frac{E_{01}(N)^2}{N_E}=\frac{M_{01}(N)^2}{N_M}.
\]
Thus the sectors whose tensor factor is same-pole and scalar factor is separated remain finite:
\[
K^{AA}_{NS}=K^{BB}_{SN}\approx -0.00400249866
\]
in the Step 89/91 principal normalization
\[
\frac{\pi^2}{2}\sum_e\frac{R_i(e)R_j(e)}{P_e\|e\|^2}.
\]

Together with the previously proved AB value
\[
K^{AB}_{adj}\approx -0.03144249732,
\]
the **principal product-background adjacent sum** is
\[
K^{principal}_{adj}\approx -0.03544499598
\]
for both ordered adjacent pairs \((NN,NS)\) and \((NN,SN)\), in the current convention. This number is not yet the Ozuch radial coefficient.

## 3. Heat-kernel representation

For the surviving AA adjacent piece,
\[
P_{rq}=\frac{\mu_r+\mu_q}{2}-1.
\]
The corrected spectral sum reduces to
\[
K_{AA,NS}
=-\frac1{1024}\sum_{r,q\ge2}
\frac{(2r+1)(-1)^q(2q+1)\mu_q(\mu_q-2)}{P_{rq}}.
\]
Using
\[
\frac1P=\int_0^\infty e^{-sP}\,ds
\]
gives
\[
K_{AA,NS}=-\frac1{1024}\int_0^\infty e^s A_0(s)B_2(s)\,ds,
\]
where
\[
A_0(s)=\sum_{\ell\ge2}(2\ell+1)e^{-s\mu_\ell/2}>0,
\]
and
\[
B_2(s)=\sum_{\ell\ge2}(-1)^\ell(2\ell+1)\mu_\ell(\mu_\ell-2)e^{-s\mu_\ell/2}
=32\pi\,\partial_x^2p^{S^2}_{s/2}(-1).
\]
Since
\[
\partial_x^2p_t^{S^2}(x)=4\pi^2e^{-6t}p_t^{S^6}(x),
\]
we have
\[
B_2(s)=128\pi^3e^{-3s}p^{S^6}_{s/2}(-1)>0.
\]
The integrand is exponentially suppressed at \(s\downarrow0\) by the antipodal heat kernel and exponentially decays at infinity; hence the integral is finite and negative. Numerical quadrature gives \(-0.00400249866\), matching the direct heat-regularized ladder.

## 4. What this does and does not prove for the product branch

The correction restores a constructive path. The principal sector calculation has **not** reached a structural limit: AB and corrected AA/BB both support the same negative adjacent sign in the current convention. However, this is still only a product-background principal response. The actual gluing coefficient requires the Ozuch/Biquard source and chart data.

Relevant Ozuch source anchors in `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md`:

- lines 283--285: Eguchi--Hanson asymptotic
  \[
  eh=e+H^4+O(r^{-8}),\qquad
  H^4=-\frac1{2r^4}(dr^2+r^2\alpha_1^2-r^2\alpha_2^2-r^2\alpha_3^2),
  \]
  with \(H^4\) trace-free and divergence-free.
- lines 313--321: orientation/direction dependence
  \[
  H^4(\zeta^+)=-\frac{\rho(\zeta)^-\circ \zeta^+}{2r^4},
  \]
  and the corresponding rotated Eguchi--Hanson metrics.
- lines 628--636: Proposition 2.10 boundary pairing, where the coefficient is a spherical boundary integral
  \[
  3\int_{S^3/\mathbb Z_2}\langle H^4,V_{l,2}\rangle + \int_{S^3/\mathbb Z_2}\langle H_2^4,V_{l,0}\rangle.
  \]
- lines 640--647: multi-node fields \(\bar h_j^4\) with prescribed singular asymptotics and orthogonality to the obstruction space.
- lines 770--789 and 791--807: the projected residual and radial obstruction order estimates.

The next product-branch construction should therefore derive the actual \(H^4(\zeta^{\pm})\) contractions into the AB and corrected AA/BB receiver channels, including Bianchi/gauge projection, quotient/isotropy normalization, and ordered north/south frame transport. The universal flat identity \(S_{odd}=(\pi^2/2)R_{odd}\) is useful but not a substitute for the physical Ozuch source coefficient.

## 5. Corrections to the imported entropy/resolvent landscape

A02's Chern--Weil neutrality and entropy comparison remain important but should be used within their hypotheses rather than as a classification of all near-pinched manifolds or all no-Einstein mechanisms.

### Ricci rescaling correction

If
\[
\operatorname{Ric}_g\ge -(3+\varepsilon)g,
\]
then to obtain a metric with lower bound \(-3\), set
\[
\widehat g=(1+\varepsilon/3)g,
\]
not the reciprocal. Since Ricci as a \((0,2)\)-tensor is unchanged by constant scaling,
\[
\operatorname{Ric}_{\widehat g}=\operatorname{Ric}_g\ge -(3+\varepsilon)g=-3\widehat g.
\]
In dimension four,
\[
\operatorname{Vol}(\widehat g)=(1+\varepsilon/3)^2\operatorname{Vol}(g),
\]
which has the same limit if \(\varepsilon\to0\), so the volume-convergence conclusion may survive but the formula in the peer note needs repair.

### Scope correction

The peer entropy argument is conditional on an orbifold+ALE near-pinched construction with volume convergence to a real-hyperbolic orbifold. It implies that Sambusetti/BCG certificates are blind to those constructions. It does **not** prove that every near-pinched no-Einstein candidate is orbifold+ALE, nor that monopole/BF/entropy exhaust possible no-Einstein mechanisms. A universal threshold in A03's reflected free-OT resolvent setting would exclude that connector class, not arbitrary non-warped non-OT connectors or the full negative branch.

A03's Step 87 resolvent theorem is a strong restricted result: under reflected, free-orthogonally-transitive \(T^2\) cusp-extension hypotheses it gives a defect threshold \(\delta_*\approx0.24625\). It does not apply to the hyperbolic \(N\#N\) neck with \(S^3\) interface, which has no free \(T^2\) action, nor to general graph metrics with twist or non-reflected connectors. It is a valuable mechanism, not a reason to stop complementary inquiry.

## 6. Route position after Step 94

1. **Product-orbifold positive branch.** Worth continuing constructively. The corrected principal adjacent response is finite and negative in all currently computed sectors. The decisive next task is not more raw sector summation but source-compatible Ozuch coefficient construction.

2. **Restricted Ishida--LeBrun negative theorem.** Still the most mature Yau--26-adjacent negative result. It remains limited and analytically unverified at publication level, but it has direct topological obstruction content independent of the product-branch local gluing.

3. **Hyperbolic/graph negative connectors.** The BCG/CGB obstruction supplies target-dependent lower bounds; A03 supplies a strong reflected free-OT obstruction. These narrow known connector models but do not settle arbitrary negative near-pinching.

4. **Full Yau--26.** Still unsolved. None of these restricted developments proves or refutes the all-dimensional, sign-unrestricted statement or approaches the Lean formalization requirement.
