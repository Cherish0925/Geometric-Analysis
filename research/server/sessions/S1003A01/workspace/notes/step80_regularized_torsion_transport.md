# Step 80 — Closed negative Goldberg: regularized torsion transport and an exact positive-square identity

Agent3, Execute. Inputs: Step 79, Spirit #87, Steps 62–65, A02 #880, and two independent TTCS verifier tasks. Computation: `workspace/scripts/step80_regularized_model_fast.py`, `step80_zero_models.py`; data: `workspace/data/step80/regularized_model_fast.json`, `zero_model_regularization.json`. The first 416-node extension of the full Step-79 frame engine timed out after 1800 seconds and produced no result; it should not be repeated unchanged.

## 1. Smooth common-denominator identities

Keep the Step-79 conventions
\[
q=|\nabla\omega|^2,\qquad
D=24|\eta|^2-8\operatorname{tr}V^2+32I,
\qquad I=\operatorname{Im}\langle\alpha,K\partial_Dv\rangle,
\]
with analyst Laplacian. The exact torsion equation is
\[
\Delta q=-D+\frac{3|s|}{2}q-\frac94q^2.                       \tag{80.1}
\]
For every \(\varepsilon>0\), put \(h=q+\varepsilon\). Integrating the smooth function \(\log h\) on a closed manifold gives
\[
\boxed{\int\left[\frac{|dq|^2}{h^2}+\frac D h+\frac94\frac{q^2}h\right]
 =\frac{3|s|}{2}\int\frac qh.}                                \tag{80.R}
\]
This needs no hypothesis on the zero set \(Z=\{q=0\}\).

For either Kodaira density
\[
F_f=|\bar\partial_Df|^2-|\partial_Df|^2-\kappa_f(q)|f|^2=\operatorname{div}j_f,
\quad f=v,\eta,
\]
the matching identity is
\[
\boxed{\int\frac{F_f}{h}=\int\frac{\langle dq,j_f\rangle}{h^2}.} \tag{80.K}
\]
The derivative-of-weight term is the normalized transport that is lost if one formally divides the unweighted Kodaira identity by \(q\).

## 2. Exact removal of the apparently indefinite coupling

The strongest new calculation in this Step is that the \(I\)-term is not intrinsically free. Set
\[
X=\operatorname{Re}(\eta\alpha),
\]
a gauge-invariant real one-form. The trace of the torsion structure equation gives
\[
\operatorname{div}_b\alpha=-2\bar\eta.
\]
Taking the real pairing of E2 with \(\alpha\), and using the gauge-covariant product rule, gives
\[
\boxed{32I=-32|\eta|^2-12rq-16\operatorname{div}X,\qquad
r=\frac s6+\frac q4.}                                         \tag{80.2}
\]
Thus
\[
D=-8|\eta|^2-8\operatorname{tr}V^2+2|s|q-3q^2-16\operatorname{div}X,
\]
and
\[
\Delta q-16\operatorname{div}X
=8|\eta|^2+8\operatorname{tr}V^2-rac{|s|}{2}q+rac34q^2.   \tag{80.3}
\]
The closed integral of (80.3) is the known AAD torsion balance, but its regularized form contains new structure.

Let
\[
Y=\partial r-\eta\alpha.
\]
Since \(|dq-8X|^2=32|Y|^2\) and \(64|X|^2=16q|\eta|^2\), substituting (80.2) into (80.R) and integrating the divergence with the same denominator yields
\[
\boxed{
32\int\frac{|Y|^2}{h^2}+\frac{|s|}{2}\int\frac qh
=8\int\frac{|\eta|^2+\operatorname{tr}V^2}{h}
 +16\int\frac{q|\eta|^2}{h^2}+rac34\int\frac{q^2}{h}.}     \tag{80.S}
\]
This identity is positive on both sides and valid for every closed candidate and every \(\varepsilon>0\). Its derivative term is exactly the first square in the Step-79 decomposition
\[
|\nabla W^+|^2=5|Y|^2+10|\partial_Dv|^2+2|\bar\partial_Dv+\eta\bar\alpha|^2.
\]
Therefore the Step-79 cross term should not be treated as an uncontrolled signed error or estimated by a lossy Young inequality. The remaining problem is to connect the other two Weyl-gradient squares through (80.K) without creating transport terms that lose their controlling square.

A useful combined identity is suggested by E1/E2: \(F_\eta+4F_v\) cancels the explicit \(|\partial_Dv|^2\) term but leaves a current \(j_\eta+4j_v+3rX\). After multiplication by \(h^{-1}\), its derivative-of-weight term still depends linearly on free \(\partial_Dv\) and \(\bar\partial_Dv\) jets while the cancellation has removed the matching positive square. More general positive combinations retain the square but produce terms schematically
\[
\frac{|\langle dq,j_f\rangle|}{h^2}
\le \delta\frac{|Df|^2}{h}+C_\delta\frac{|dq|^2|f|^2}{h^3},
\]
and the second denominator cannot be absorbed without an additional bound on \(|f|^2/h\). At a torsion zero, \(\eta\) and \(v\) are first derivatives of \(\alpha\), so no such pointwise bound follows from the second-tier equations. This is the precise surviving geometric freedom.

## 3. Zero geometry and logarithmic residues

The scripts integrate \(\Delta\log(q+\varepsilon)\) exactly for \(q=c\rho^{2m}\).

### 3.1 Isolated radial zero in four dimensions

On \(B_R\subset\mathbb R^4\),
\[
\int_{B_R}\Delta\log(q+\varepsilon)
=\frac{4\pi^2mcR^{2m+2}}{cR^{2m}+\varepsilon}
\longrightarrow4\pi^2mR^2.
\]
Sending \(R\downarrow0\) gives no point mass. Moreover \(|d\log q|^2=4m^2/r^2\) is locally integrable for every \(m\), whereas \(1/q\in L^1_{\rm loc}\) only for \(m=1\). Hence Step 79's hypotheses were sufficient but not necessary: for \(m\ge2\), separate \(1/q\) terms can fail while the common-denominator combination remains finite.

The Step-65 leading polynomial \(f_m=\kappa\bar z_2^m e_1\) at a degenerate point does not determine the actual analytic zero set. Higher terms can isolate the point, so its regularized limit cannot be inferred from the leading polynomial alone.

### 3.2 Smooth codimension-two stratum

Per unit surface area, if
\[
q=c(y)\rho^{2m}(1+O(\rho))
\]
with the matching derivative control, then
\[
\int_{\rho<R}\Delta\log(q+\varepsilon)\longrightarrow4\pi m.
\]
Both \(\int|d\log q|^2\) and \(\int1/q\) diverge normally. Distributionally,
\[
\Delta\log q=(\Delta\log q)_{M\setminus Z}+4\pi m\,\delta_{Z_2},
\]
where \(\delta_{Z_2}\) is surface measure. This is a normal-vanishing-order residue, not the Euler charge \(5\chi+6\tau\). A real one-dimensional zero stratum has normal dimension three and no residual measure after the tube radius shrinks. Thus the word “curve” must be disambiguated: a complex/real-two-dimensional curve has the residue, a real one-dimensional curve does not.

These calculations repair Step 79 §4. The unsupported assertion that \(Z\) has codimension at least three and the blanket statement that zero curves have no residue are withdrawn. Step 63 excludes only a compact smooth rank-two zero surface without exceptional points; stratified surface components remain possible.

## 4. Corrected complete-model regularization

The first version of the fast script contained two normalization mistakes: it used a false simplification of \(\sqrt{A_1A_2A_3}\), and it imported the Step-59 \(|\eta|^2\) form norm without dividing by two to obtain the Step-62/79 vector norm. The TTCS disagreement exposed these errors; the script and data have been corrected and rerun.

For the complete Bianchi-VIII model,
\[
q=\frac{36(1-p^2)^3}{(1+3p^2)^3},
\quad |\eta|^2=\frac{9(1-p^2)^3(9p^2-1)}{(1+3p^2)^4},
\]
\[
\operatorname{tr}V^2=\frac{81(1-p^2)^4(9p^2-1)^2}{2(1+3p^2)^6}.
\]
Direct radial differentiation gives
\[
D=\frac{108(1-p^2)^3(9p^2-1)(33p^4-26p^2+25)}{(1+3p^2)^6},
\]
and, consistently with the Step-79 frame check,
\[
\boxed{32I=rac{432(1-p^2)^4(9p^2-1)(3p^2+5)}{(1+3p^2)^6}\ge0.} \tag{80.4}
\]
Thus the earlier adverse-cancellation interpretation was false and is withdrawn. At the ACH end \(t=1-p\),
\[
q=\frac92t^3+O(t^4),\quad |\eta|^2=\frac94t^3+O(t^4),
\]
\[
D=54t^3+O(t^4),\quad 32I=108t^4+O(t^5),
\quad |dq|^2=\frac{729}{2}t^6+O(t^7).
\]
The coupling is positive and one order smaller than the eta term. In particular
\[
24|\eta|^2/q\to12,
\]
as Step 79 originally recorded.

The corrected sweep uses \(p=1/3+(2/3)(1-e^{-u})^2\), 32 Gauss nodes per unit interval, and \(0\le u\le32\). Representative values are:

| epsilon | gradient | D/h | RHS | peak log flux | peak u |
|---:|---:|---:|---:|---:|---:|
| 1e-2 | 4.2990e3 | 9.1535e3 | 1.35795e4 | 2.0093e3 | 2.620 |
| 1e-4 | 9.8318e4 | 1.95212e5 | 2.93671e5 | 4.3051e4 | 4.103 |
| 1e-8 | 4.5473e7 | 9.0862e7 | 1.36335e8 | 1.9890e7 | 7.168 |
| 1e-12 | 2.1094e10 | 4.2187e10 | 6.3281e10 | 9.2281e9 | 10.247 |

For each fixed epsilon, the end flux tends to zero. The displayed finite-cutoff residual equals the omitted boundary flux at \(u=32\), rather than floating cancellation error: asymptotically it is \(4.86304\times10^{-12}/\varepsilon\). The transition layer is \(t\asymp(2\varepsilon/9)^{1/3}\), the peak grows as \(\varepsilon^{-2/3}\), and
\[
u_{\rm peak}=\frac13\log(1/\varepsilon)+1.020090\ldots+o(1).
\]
The scalar regularized pieces have leading ratios
\[
\text{gradient} : D/h : \text{RHS}=1/3:2/3:1.
\]
The \(I\) and \(V\) pieces are lower order \(O(\varepsilon^{-1/3})\). The model therefore exhibits nonuniformity through an expanding low-torsion end, not through a leading negative \(\partial v\) cancellation.

## 5. Scope and next mathematical target

The common-denominator family is the correct general entrance because it permits isolated, degenerate, and positive-dimensional zero sets. Identity (80.S) is the main structural advance: the apparent cross term becomes the positive \(Y\)-square. It does not prove Goldberg because both sides are positive and the remaining weighted Kodaira transports contain free Weyl jets with a denominator mismatch.

A successful continuation should seek a global estimate for a combination of
\[
\frac{|\partial_Dv|^2}{q+\varepsilon},\quad
\frac{|\bar\partial_Dv+\eta\bar\alpha|^2}{q+\varepsilon},
\quad
\frac{\langle dq,j_v\rangle}{(q+\varepsilon)^2},
\quad
\frac{\langle dq,j_\eta\rangle}{(q+\varepsilon)^2},
\]
that keeps enough positive derivative squares to absorb the current and remains uniform through actual zero strata. This need not be the only possible route: canonical curves, harmonic ASD information, compact extrema, or spectral input may add the missing global control.

The complete model excludes only deductions transferable to it by exhaustion with integrable densities and vanishing flux. It does not close all Bochner methods, and the broad Step-79 assertion about every polynomial current was stronger than established. The model is nonetheless decisive against the specific unweighted coercivity tested there.

At a torsion zero, (80.1) and \(\Delta q\ge0\) give
\[
\operatorname{tr}V^2\ge3|\eta|^2,
\]
recovering the Step-62 cone inequality and making it strict at a nondegenerate zero. This local fact is compatible with all current global identities and supplies no contradiction by itself.

The blowup and orbifold branches remain as before. A02 #880 independently observes that \(T_{\rm AK}=\int(s^2/24-|W^+|^2)\) and the resulting scalar identity are topological curvature identities after the AAD decomposition; the substantive Goldberg information lies in the torsion balance, actual canonical-cycle input, and the regularized differential transport developed here.
