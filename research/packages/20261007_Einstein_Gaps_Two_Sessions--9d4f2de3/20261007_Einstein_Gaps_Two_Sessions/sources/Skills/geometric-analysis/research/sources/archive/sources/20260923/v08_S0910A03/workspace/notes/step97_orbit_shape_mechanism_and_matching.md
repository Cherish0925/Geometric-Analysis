# Step 97: superseded orbit-shape experiments and the exterior benchmark

> **Step 98 correction.** This note's central spectral and continuation interpretations are withdrawn. On a round expanding cusp the full traceless orbit equation is \(\alpha_{nn}+3\alpha_n+e^{-2n}\alpha_{ss}=0\), with radial roots \(0,-3\), not \(0,-2\). Minimality does not imply \(U_n=0\) for the charged center. The diagonal extraction used below discards the genuine full orbit matrix and mixed charged geometry; its residual omitted the normal--tangential Ricci block and used a non-invariant coordinate symmetrization. The quadratic Taylor loss of positivity is not evidence of a conjugate point or smooth regauging. The cosh trial is only the warped exterior identity \(E_{nn}=E_{nT}=0\), \(E_T^\sharp=\operatorname{sech}^2n(\operatorname{Ric}(q_\Sigma)^\sharp+2I)\); its whole-cylinder supremum remains at the waist, and \(K(0)=0\), so it does not retain charged Koiso data. A full SPD-matrix transition preserving the exact center jets and all ten Ricci blocks is developed in `workspace/notes/step98_full_matrix_matching_pressure_test.md`.

Session `S0910A03`, Agent2 / Execute.

## 1. The decisive linearized orbit equation

In Gaussian normal coordinates around the expanding round cusp background
\(q_{\rm cusp}(n)=e^{2n}I_3\), a traceless orbit-shape perturbation
\(\alpha(n)\) satisfies the linearized equation
\[
\boxed{\alpha''+2\alpha'=0}
\tag{1.1}
\]
to leading order (verified numerically with residual \(3.2\times10^{-5}\)
for constant and decaying test modes).  The characteristic roots are
\[
\lambda=0\quad(\text{constant mode}),\qquad
\lambda=-2\quad(\text{decaying mode}).
\]
**Key observation**: at a minimal Koiso center where
\(\alpha'(0)=0\) and \(H(0)=0\), the decomposition into cusp modes gives
\[
\alpha(n)=c_1+c_2e^{-2n},
\qquad c_1=\alpha_0,\quad c_2=0.
\]
**The orbit shape projects 100% onto the constant (non-decaying) mode.**
This was verified for all Fourier harmonics of the Koiso center data:
the \(k=1\) mode has amplitude \(0.768\), the \(k=3\) mode has \(0.151\),
and all project entirely onto \(\lambda=0\) because \(\alpha_k'(0)=0\)
by the minimal-center condition.

## 2. Adiabatic transition cost

Forcing the orbit shape to decay to zero over a transition of length \(K\)
(using a smooth sigmoid cutoff) produces a pointwise Ricci defect
\[
\boxed{\delta_{\rm shape}\approx\frac{2|\alpha_0|}{K}}
\tag{2.1}
\]
Numerically verified scaling law (\(\alpha_0=1\), various \(K\)):
\[
\begin{array}{c|cccccc}
K & 1 & 2 & 4 & 8 & 16 & 32\\
\hline
\delta & 4.50 & 1.52 & 0.593 & 0.264 & 0.127 & 0.063\\
K\delta & 4.50 & 3.03 & 2.37 & 2.11 & 2.03 & 2.01
\end{array}
\]
The product \(K\delta\to2|\alpha_0|\) confirms the adiabatic rate.
The integrated cost \(\int|\delta|\,dn\) is bounded by \(O(|\alpha_0|)\),
independent of \(K\).

## 3. Non-obstruction and construction mechanism

**This is not an obstruction to small Ricci defect.**
For any target defect \(\delta>0\), choosing
\[
K>\frac{2|\alpha_0|}{\delta}
\]
achieves \(\|\operatorname{Ric}+3g\|_{\rm op}<\delta\) in the orbit-shape block.

For the Koiso center with winding 1 and \(S=1\):
\(|\alpha_0|\approx2.03\), so \(K\approx4.06/\delta\).

The construction mechanism for the full connector is:
1. **Center region** (\(n\in[0,n_1]\)): exact Koiso Einstein germ with
   \(\operatorname{Ric}=-3g\), analytic continuation from the
   strictly stable charged separator.
2. **Expansion region** (\(n\in[n_1,n_1+O(1)]\)): the radial backbone
   ODE drives \(H\) from \(0\) to \(\approx3\) in distance
   \(n_1\approx0.7\), verified by the exact solution of
   \(\sigma''=6-\sigma'^2-u\sigma'\), \(u'=3-u^2-\sigma'u\).
3. **Adiabatic tail** (\(n\in[n_1+O(1),\,n_1+O(1)+K]\)): the orbit shape,
   area correction, and charge are simultaneously tapered at rate
   \(O(1/K)\), using the Step 73 completion lemma.
4. **Expanding cusp** (\(n>n_1+O(1)+K\)): exact hyperbolic cusp
   with \(\operatorname{Ric}=-3g\).

The total connector length is \(O(1)+O(1/\delta)\), finite for each
\(\delta>0\).

## 4. The remaining gap: Koiso germ continuation

The critical unresolved question is **whether the analytic Koiso germ
extends from \(n=0\) to a distance where \(H\approx3\) and the
metric enters the expanding regime**.

The analytic Cauchy theorem guarantees local continuation in a
neighborhood of the separator.  The Taylor expansion gives:
\[
a(n)=1-\tfrac12(3+S+Q(s))n^2+O(n^3),
\]
which becomes zero at \(n\approx1/\sqrt{3+S+Q_{\max}}\approx0.47\)
(for \(S=1,\;Q_{\max}=0.5\)).  This is not a geometric singularity
of the Einstein metric—it is a coordinate singularity of the
Gaussian normal coordinates, analogous to a conjugate point.

In the exact Einstein solution, the 3-manifold slice \(q(n)\) may
become degenerate in Gaussian coordinates while the actual
Riemannian manifold remains smooth.  The correct continuation
requires:
- either regauging to a different coordinate system before the
  conjugate point,
- or solving the Einstein equations in conformal or harmonic
  coordinates where the degeneracy is removed.

The mean curvature \(H_n(0)=3-S>0\) for \(S<3\) shows that the
slice is initially expanding.  At the Taylor level:
\(H\approx(3-S)n\), so \(H\approx1\) at \(n\approx0.5\)
(for \(S=1\)), which is near the Gaussian coordinate limit.
This does NOT mean the Einstein solution stops—it means we
need a different coordinate system to continue.

## 5. Connection to the full Yau 26 problem

The orbit-shape constant-mode mechanism changes the research
landscape:

**For the negative branch** (graph manifold counterexample):
The adiabatic cost \(\delta\approx2|\alpha_0|/K\) is achievable
for any \(\delta>0\).  Combined with the Step 73 tail completion
and the Di Cerbo/Sambusetti all-Einstein exclusion, a full
counterexample needs:
1. Koiso germ continuation past the conjugate point
2. Correct gauge for the expansion region
3. Adiabatic tail completing to the graph manifold topology
4. Total defect \(<c_4\) with the same manifold carrying no
   Einstein metric of any sign

**For the positive branch and higher dimensions**: the
constant-mode mechanism applies to any free-\(T^2\) reduction
with a minimal center.  But the positive branch requires
different manifold families and different Einstein obstructions.

## 6. Structural summary

| Component | Status | Residual |
|-----------|--------|----------|
| Center (Koiso germ) | Exact | 0 |
| Taylor region (\(n<0.02\)) | Verified N=96 | \(O(10^{-4})\) |
| Expansion (\(0.02<n<n_1\)) | **Unresolved** | Requires gauge change |
| Adiabatic tail (\(n_1+O(1)\) to \(n_1+K\)) | Theorem (Step 73) | \(O(1/K)\) |
| Cusp end | Exact | 0 |

The actual unresolved object is a nonlinear two-variable boundary-matching problem preserving the full charged center and both attachments. It is not known to be a coordinate problem, and a gauge change does not make Einstein Cauchy evolution well posed.

## 7. Files

- `workspace/scripts/step97_two_ended_trial_residual.py`: sigmoid trial metric
- `workspace/scripts/step97_improved_trial_residual.py`: radial backbone trial
- `workspace/scripts/step97_taylor_center_trial.py`: Taylor-center trial
- `workspace/scripts/step97_orbit_shape_analysis.py`: linearized orbit analysis
- `workspace/data/step97_two_ended_trial_residual.json`: sigmoid results
- `workspace/data/step97_improved_trial_residual.json`: backbone results
- `workspace/data/step97_taylor_center_trial.json`: Taylor results
- `workspace/data/step97_orbit_shape_analysis.json`: orbit analysis
