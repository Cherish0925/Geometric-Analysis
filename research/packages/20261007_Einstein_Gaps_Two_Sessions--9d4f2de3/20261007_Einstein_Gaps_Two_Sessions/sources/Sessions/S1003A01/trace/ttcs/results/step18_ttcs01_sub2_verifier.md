# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md",
    "Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md",
    "Sessions/S1003A01/workspace/notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md",
    "Sessions/S1003A01/workspace/scripts/riccati_ch_benchmark.py",
    "Sessions/S1003A01/workspace/data/hj/riccati_ch_benchmark.json"
  ]
}
```

## Task

Independently check the corrected Hamilton–Jacobi transverse Hessian/Riccati analysis in the Step-18 note. Verify the distinction between K and shifted Y, derive the exact CH scalar Riccati equations from the supplied formulas, check that K_+=-2/Delta_+ and K_-=-2(1+x)^5/Delta_- match the Step-7 positive ground states and outgoing Dirichlet-to-Neumann form, and interpret finite Riccati poles via the linear Jacobi/Lagrangian system. Identify any sign, factor, boundary-condition, or interpretation error. The scientific issue is whether the computation truly reframes the crossing as a graph-chart/matching problem rather than a compactly supported CH instability.

## Output

# Verification memo: the transverse Hamilton–Jacobi/Riccati analysis of Step 18 over exact CH

## Summary

- **Algebra.** The \(K\)/\(Y\) algebra, the exact CH scalar Riccati equations, the closed forms \(K_\pm\), and the identification of their integrating structure with the Step‑7 ground states are all correct. I rederived each one independently from the supplied formulas.
- **Poles.** The interpretation of the poles can be made sharper than Step 18 states it. Every pole in the JSON follows from a closed‑form equation, and the c = 1 poles before \(x=1\) restate exactly the Step‑7 fact \(d_-(\rho)<0\).
- **Crossing versus instability.** A transverse instability would require two poles of one solution. Exact CH forbids this: \(z/f^2\) is monotone, which is the same fact as positivity of \(f_\pm\). The reframing of the \(u_2=2\) crossing as a matching problem therefore holds.
- **What the benchmark leaves out.** It fixes the hard target at \(x=1\) and leaves the shape variable \(\theta=\delta\log(a_1/a_3)\) free. On realistic collars \(X\gg1\) the minus‑channel outgoing plane changes qualitatively, and the torsion‑free moment becomes the whole minus‑channel cost.

## 1. \(K\) versus \(Y\)

Linearize the free flow at \(N\). From \(H_1=u_1+\tfrac12u_2u_3\), \(H_3=u_3+\tfrac12u_1u_2\) and \(1/\lambda_1=a_1^2/W\):
\[
\dot\xi=DA\xi .
\]
Contributions through \(\dot a\), \(S_{u_2}\) and \(u_1u_3\) in \(\dot u_2\) are cubic or higher.

For \(S=\tfrac12\xi^TK\xi\) this gives \(\mathcal H_S=\xi^TM\xi\), with
\[
M=\tfrac12\dot K+\tfrac12(KDA+ADK)+KDK .
\]
So (1.1) is the matrix of the quadratic form; there is no missing factor ½.

Substituting \(K=Y-A/2\):
\[
M=\tfrac12\dot Y+YDY-\tfrac14(ADA+\dot A),\qquad \dot A=\frac{2u_2}{\lambda_2}\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
since \(H_2=u_2\) on \(N\). This is (1.2).

Checks:
- For \(K=-A\), \(M=-\tfrac12\dot A\), so \(\xi^TM\xi=-2u_1u_2u_3/\lambda_2=-\kappa\). This reproduces (H2).
- The assignments seed \((K,Y)=(-A,-A/2)\) and zero \((0,A/2)\) are correct.

## 2. Scalar CH Riccati

On CH I checked independently that \(u_1=0\) and \(u_2=1+2x-(1-x)=3x\).

Further:
- \(D=I/\sqrt{x(1+x)}\) is scalar because \(a_1=a_3\), so \(A\), \(D\) and \(\dot A\) are simultaneously diagonal in \(v_\pm\). Off CH inside \(N\) (triaxial Kähler states, \(a_1\neq a_3\)), \(D\) and \(A\) no longer commute and the 2×2 matrix Riccati is required.
- With \(d/dt=2\sqrt{x(1+x)}\,d/dx\) and eigenvalues \(\alpha_\pm=2\pm3x\), \(M=0\) becomes \(K'+K(K+\alpha)/(x(1+x))=0\). This is (2.1).
- \(z=1/K\) gives (2.3).
- Partial fractions give \(\alpha_+/(x(1+x))=2/x+1/(1+x)\) and \(\alpha_-/(x(1+x))=2/x-5/(1+x)\).

Small wording point: \(f_\pm^2\) is the homogeneous solution of the \(z\)-equation; the integrating factor is \(f_\pm^{-2}\). The solution is
\[
\frac{z}{f^2}(x)=\frac{z}{f^2}(\rho)+\int_\rho^x\frac{ds}{s(1+s)f^2}. \tag{A}
\]

## 3. DtN identification, factors and normalization

**Factor between \(K\) and \(c\).** In the Step‑7 normalization \(v_\pm=\xi\pm\zeta\):
- \(\tfrac12\xi^TK\xi=\tfrac14(k_+v_+^2+k_-v_-^2)\);
- \(\Phi=\tfrac{2+u_2}4v_+^2+\tfrac{2-u_2}4v_-^2\).

The value function is \(V=c_+V_+^2+c_-V_-^2\), and \(S=-V\) gives \(k_\pm=-4c_\pm\). This is the script's `kplus=-4*cplus`.

**Total cost per channel.** The Step‑7 total (Φ‑charge plus full relative action) collapses exactly. Since \(2\beta_\pm\) equals the Φ coefficient \((2\pm3\rho)/4\) and \(v(X)=0\):
\[
\text{cost}_\pm=\Phi_\pm(\rho)V^2+Q_\pm+[\beta v^2]_\rho^X=\int_\rho^X pf_\pm^2\big((v/f_\pm)'\big)^2dx .
\]
The ground‑state transform absorbs the entire relative Chern–Simons charge. Hence \(c_\pm=1/(f_\pm^2(\rho)R_\pm(\rho))\).

**Direct integration.** With \(R=4\int_\rho^1 ds/(s(1+s)f^2)\):
- Plus channel: \(\int ds/(s^3(1+s)^2)\) has antiderivative \(3\log\frac s{1+s}+\frac2s-\frac1{2s^2}+\frac1{1+s}\). This gives \(f_+^2R_+=2\Delta_+\) identically.
- Minus channel: \(\int(1+s)^4s^{-3}ds\) has antiderivative
\[
G(s)=\tfrac{s^2}2+4s+6\log s-\tfrac4s-\tfrac1{2s^2}.
\]
This gives \(f_-^2R_-=2\Delta_-/(1+\rho)^5\).

Hence \(K_+=-2/\Delta_+\) and \(K_-=-2(1+x)^5/\Delta_-\). Both are of the form (A) with \(z(1)=0\), so the vanishing residuals are automatic.

**Consistency with Step 7.**
- \(d_\pm=c_\pm-(2\pm3\rho)/4\) reproduces (3.5).
- The small‑\(\rho\) asymptotics are \(\pm\tfrac34\rho\).
- At \(\rho=.1\), \(d_-=-.03565\).

**Positivity of the outgoing plane.** \(\Delta_\pm>0\) on \((0,1)\) because \(R_\pm>0\). The DtN graph is therefore finite on \([\rho,1)\) and vertical only at \(x=1\). The seed eigenvalue \(-(2-3x)\) vanishes at \(x=2/3\), but \(K_-\) is smooth there.

**Riccati–Sturm dictionary.** Writing Sturm solutions as \(v=f(a+b\int 1/(pf^2))\) gives the exact dictionary
\[
K_\pm=4\Big(\frac{pv'}{v}-\beta_\pm\Big).
\]
Consequences:
- \(K=0\) is generated by the ground state \(v=f_\pm\) itself (zero energy).
- The DtN plane is generated by the Jacobi solution vanishing at the target.
- The seed \(K=-8\beta_\pm\) is the logarithmic derivative of \(1/f_\pm\).
- The crossing \(u_2=2\) on CH, i.e. \(x=2/3\), is the maximum of \(f_-=x(1+x)^{-5/2}\) (\(\beta_-=pf_-'/f_-=0\)). The Chern–Simons Hessian degeneracy is where the ground state turns over, not where it vanishes.

## 4. The poles in closed form

By (A), the seed \(K(\rho)=-c\alpha_-(\rho)\) has a pole at \(x_p\) where
\[
G(x_p)-G(\rho)=\frac{(1+\rho)^5}{c\,\rho^2(2-3\rho)} .
\]
Equivalently, \(K_{\rm seed}(\rho)=K^{x_p}_{\rm DtN}(\rho)\): **\(x_p\) is the hard‑target position at which the exact‑CH Dirichlet cost equals the seed charge.**

Spot checks against the JSON:
- \(\rho=.1,c=1\) gives \(.5956\).
- \(\rho=.3,c=1\) gives \(2.0598\).
- \(\rho=.003,c=.99\) gives \(19.98\).

The pole lies before \(x=1\) iff \(c>c^*(\rho)=2(1+\rho)^5/((2-3\rho)\Delta_-(\rho))\); for \(c=1\) this is iff \(d_-(\rho)<0\).

| ρ | Δ₋ | c₋ | (2−3ρ)/4 | c* | JSON poles (c = 1, .99, .985) |
|---|---|---|---|---|---|
| .003 | 1.024627 | .495345 | .49775 | .99517 | .0525, 19.98, none <20 |
| .01 | 1.085518 | .484106 | .4925 | .98296 | .108, .211, .519 |
| .03 | 1.277654 | .453673 | .4775 | .95010 | .226, .269, .297 |
| .1 | 2.068210 | .389352 | .425 | .91612 | .596, .628, .646 |
| .3 | 4.476190 | .414750 | .275 | 1.508 | 2.06–2.12 |
| .5 | 6.016944 | .631026 | .125 | 5.048 | 5.69–5.78 |

All 42 runs match. Two remarks on the JSON:
- `null` means no pole before `xmax=20`, not no pole. Because \(G\to\infty\), every minus seed with \(\rho<2/3\) has exactly one pole. For example, \(\rho=.003,c=.985\) has \(x_p\approx29.9\), and \(\rho=.65,c=1\) has \(x_p\approx29.4\).
- The plus channel has no pole for these data because \(\int^\infty ds/(s^3(1+s)^2)<\infty\) and \(c_+^\infty>(2+3\rho)/4\).

**Interpretation.**
1. **Instability versus matching.** \(z/f^2\) is strictly increasing, so each Riccati solution has at most one pole on \((0,\infty)\). Through the dictionary, a pole is a zero of the Sturm solution. A compactly supported mode with \(Q<0\) requires a Sturm solution with two zeros, i.e. two poles of one graph. This is excluded precisely by \(f_\pm>0\). The CH crossing is therefore not an instability, and Step 18's conclusion stands on an exact proof, not only numerics.
2. **The poles are not chart noise for certificates.** For any valid subsolution, \(V\ge -S\) with \(S(\text{out})=0\) forces \(K(\rho)\ge K^X_{\rm DtN}(\rho)\). Riccati comparison (\(M\le0\) pushes \(K\) below the equality solution) shows that a seed with \(x_p<X\) cannot be continued as a \(C^1\) quadratic subsolution to the target, in any chart. On the outgoing side no chart change is ever needed, since the DtN plane is a graph on \([\rho,X)\). Chart changes can only matter for the bolt‑side plane propagated through the non‑CH transition.
3. **The matching statement.** The precise form is an order relation between two graphs at the cut: \(K_{\rm in}(\rho)\ge K^X_{\rm DtN}(\rho)\). The phrase "meet … possibly across graph‑chart changes" should be replaced by this order relation.

## 5. Target position and the torsion‑free moment

The \(x=1\) target is a benchmark choice. In general,
\[
K^X_\pm(\rho)=-\Big[f_\pm^2(\rho)\int_\rho^X\frac{ds}{s(1+s)f_\pm^2}\Big]^{-1}.
\]

**Large collars.** As \(X\to\infty\):
- \(K_+^\infty=-1/\big(\rho^2(1+\rho)E(\rho)\big)\), with \(E=\frac1{2\rho^2}-\frac2\rho-\frac1{1+\rho}+3\log\frac{1+\rho}\rho\), which is finite.
- \(K_-^X\to0\), i.e. \(Y\to A/2\), the zero function. The reason is that \(f_-\sim x^{-3/2}\) is the recessive solution at infinity, so the ground state itself is the zero‑cost outgoing mode.

For \(X=64\) and every \(\rho<2/3\), the free‑\(\theta\) minus‑channel DtN therefore lies below \(c\Phi\) for every \(c\). The scalar benchmark cannot carry any minus‑channel lower bound on realistic collars.

**Role of \(\theta\).** The scalar Riccati leaves \(\theta\) free, whereas the CH curve requires \(\theta(X)=0\). At linear order, \(\dot\xi\) does not involve \(\delta a\). Using (4.3)–(4.4), set
\[
w=v_-/f_-,\quad w_0=V_-/f_-(\rho),\quad \mu=-2\Big(\tfrac\rho{1+\rho}\Big)^2\theta(\rho),\quad m(x)=\int_x^\infty f_-^2=\frac{6T^2-8T+3}{12T^4},\ T=1+x .
\]
Minimizing \(\int pf_-^2w'^2\) under the two linear constraints and letting \(X\to\infty\) (where \(R\sim2X^2\) dominates \(M_{12}^2\sim4\log^2X\)) gives the total minus‑channel quadratic cost
\[
\text{cost}_-^{\infty}=\frac{\big(\mu-w_0\,m(\rho)\big)^2}{\int_\rho^\infty m(x)^2/(pf_-^2)\,dx}.
\]
This is rank one. Its kernel is the decaying exact linearized‑Einstein Jacobi field \(v=f_-\), with \(\theta\sim x^{-2}\).

This refines Step 7 §4. On long collars the moment square is not an addition to the minus DtN; it is the entire minus‑channel cost. The lower theory in that channel depends on the bolt side delivering \((V_-,\theta(\rho))\) off this line. This is directly computable on the stored X = 64 profiles, provided the cut is placed where the profile is close to CH.

## 6. Points to correct in the text

- "Integrating factors are \(f_\pm^2\)": replace by "homogeneous solutions are \(f_\pm^2\)".
- "Absent before \(x=20\)": accurate, but the minus pole always exists for \(\rho<2/3\).
- The statement "graph poles … the Lagrangian plane remains defined" is true. It should be accompanied by the comparison statement in §4, item 2, so that it is not read as permission to continue seed‑type quadratic subsolutions past \(x_p\).
- The \(x=1\) DtN planes (2.2) are not the outgoing planes of the actual cell problem. That plane is the \(X\)-dependent joint \((v_+,v_-,\theta)\) Lagrangian of §5.