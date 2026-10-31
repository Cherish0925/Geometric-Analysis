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

## Scientific verification memo

### 1. The \(K\)-versus-\(Y\) correction is algebraically correct

On \(N=\{u_1=u_3=0\}\), write \(\xi=(u_1,u_3)^T\). The free transverse evolution is
\[
D_0\xi=D A\xi,
\qquad
A=\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},
\qquad
D=\frac1W\operatorname{diag}(a_1^2,a_3^2),
\]
because
\[
\dot u_1=\frac{2u_1+u_2u_3}{\lambda_1},
\qquad
\dot u_3=\frac{u_2u_1+2u_3}{\lambda_3},
\qquad
\lambda_i^{-1}=\frac{a_i^2}{W}.
\]

For
\[
S=\frac12\xi^TK\xi+O(|\xi|^3),
\]
where \(D_0K\) means differentiation of the coefficient matrix along the longitudinal flow on \(N\),
\[
D_0S
=\frac12\xi^T(D_0K)\xi
+\frac12\xi^T(KDA+ADK)\xi,
\]
and
\[
\frac1W\sum_i a_i^2S_{u_i}^2=\xi^TKDK\xi.
\]
Thus the quadratic Hamiltonian matrix is exactly
\[
E(K)=\frac12D_0K+\frac12(KDA+ADK)+KDK.
\]

Now put \(Y=K+A/2\), so \(K=Y-A/2\). Direct substitution gives
\[
\begin{aligned}
E(K)
&=\frac12D_0Y-\frac14D_0A
+\frac12(YDA+ADY)-\frac12ADA\\
&\quad+YDY-\frac12(YDA+ADY)+\frac14ADA\\
&=\frac12D_0Y+YDY-\frac14(ADA+D_0A).
\end{aligned}
\]
Therefore
\[
E(K)\le0
\quad\Longleftrightarrow\quad
\frac12D_0Y+YDY\le\frac14(ADA+D_0A).
\]

The endpoint identifications are consequently
\[
S=-\Phi=-\frac12\xi^TA\xi
\quad\Longrightarrow\quad
K=-A,\quad Y=-\frac A2,
\]
whereas
\[
S=0
\quad\Longrightarrow\quad
K=0,\quad Y=\frac A2.
\]
The corrected Step-18 convention is right; \(Y=0\) is neither the seed nor the zero function.

---

### 2. Exact CH reduction gives the stated scalar Riccati equations

On CH,
\[
a_1=a_3=\sqrt x,\qquad a_2=\sqrt{x(1+x)},\qquad u_2=3x.
\]
Set
\[
q=x(1+x).
\]
Then
\[
W=x\sqrt q,\qquad
D=q^{-1/2}I,\qquad
\frac{dx}{dt}=2\sqrt q.
\]
In the orthonormal transverse coordinates
\[
\eta_\pm=\frac{u_1\pm u_3}{\sqrt2},
\]
the eigenvalues of \(A\) are
\[
a_\pm=2\pm3x.
\]

For a diagonal Hessian channel \(K_\pm(x)\),
\[
E(K_\pm)=\frac12\dot K_\pm
+q^{-1/2}K_\pm(K_\pm+a_\pm).
\]
Since \(\dot K_\pm=2\sqrt q\,K_\pm'\), the equality equation \(E=0\) becomes
\[
\boxed{
K_\pm'
+\frac{K_\pm(K_\pm+2\pm3x)}{x(1+x)}=0.
}
\]
Thus Step 18, equation (2.1), has the correct sign and coefficient.

As an additional sign test, insert the seed \(K_\pm=-a_\pm\). Its Riccati residual is
\[
K_\pm'=\mp3.
\]
This agrees with
\[
\mathcal H_{-\Phi}=-\frac{2u_1u_2u_3}{\lambda_2}:
\]
the plus channel contributes \(-3\sqrt q\,\eta_+^2\), while the minus channel contributes \(+3\sqrt q\,\eta_-^2\).

---

### 3. Relation to the Step-7 ground states and DtN form

There is a normalization point that should be stated explicitly:

- Step 7 uses \(v_\pm=u_1\pm u_3\).
- The matrix eigenvalues \(K_\pm\) refer naturally to
  \(\eta_\pm=v_\pm/\sqrt2\).

For one unnormalized Step-7 channel \(v\), the direct quadratic \(P\)-cost on \([x,1]\) is
\[
J_\pm[v]
=\int_x^1 p(s)
\left(v'-\frac{a_\pm}{2s(1+s)}v\right)^2ds,
\qquad
p(s)=\frac{s(1+s)}4.
\]
The Step-7 functions
\[
f_+=x\sqrt{1+x},
\qquad
f_-=\frac{x}{(1+x)^{5/2}}
\]
satisfy
\[
\frac{f_\pm'}{f_\pm}
=\frac{a_\pm}{2x(1+x)},
\qquad
p\frac{f_\pm'}{f_\pm}=\frac{a_\pm}{8}=\beta_\pm.
\]
Hence
\[
J_\pm[v]
=\int_x^1 p f_\pm^2
\left((v/f_\pm)'\right)^2ds.
\]

For \(v(x)=V\) and the hard terminal condition \(v(1)=0\), weighted Cauchy–Schwarz is sharp:
\[
\inf J_\pm
=c_\pm(x)V^2,
\qquad
c_\pm(x)=\frac1{f_\pm(x)^2R_\pm(x)},
\]
where
\[
R_\pm(x)=\int_x^1\frac{ds}{p(s)f_\pm(s)^2}.
\]
Direct integration gives
\[
R_+(x)=\frac{2\Delta_+(x)}{x^2(1+x)},
\qquad
R_-(x)=\frac{2\Delta_-(x)}{x^2}.
\]
Consequently
\[
c_+(x)=\frac1{2\Delta_+(x)},
\qquad
c_-(x)=\frac{(1+x)^5}{2\Delta_-(x)}.
\]

Since \(v=\sqrt2\,\eta\), the value in an orthonormal channel is
\[
V_{\mathrm{cost},\pm}(\eta)=2c_\pm\eta^2.
\]
The Hamilton–Jacobi function is \(S=-V_{\mathrm{cost}}\), so
\[
\frac12K_\pm\eta^2=-2c_\pm\eta^2,
\qquad K_\pm=-4c_\pm.
\]
Therefore
\[
\boxed{
K_+(x)=-\frac2{\Delta_+(x)},
\qquad
K_-(x)=-\frac{2(1+x)^5}{\Delta_-(x)}.
}
\]

This also explains the factor of four in `riccati_ch_benchmark.py`. If one instead wrote a Hessian coefficient directly in the unnormalized variable \(v_\pm\), its coefficient would differ by a factor of two.

The relation to Step 7’s relative-action coefficient is
\[
d_\pm=c_\pm-\frac{a_\pm}{4}.
\]
Indeed, in unnormalized variables,
\[
\Phi=\frac{a_+}{4}v_+^2+\frac{a_-}{4}v_-^2.
\]
Thus the Step-7 relative action \(d_\pm v_\pm^2\), plus the entrance contribution from \(\Phi\), yields \(c_\pm v_\pm^2\). The Riccati formulas use \(c_\pm\), not \(d_\pm\) alone.

The sign convention is also consistent: the usual positive value Hessian is \(+4c_\pm\), while the supplied \(K_\pm\) is its opposite because the HJ function is \(S=-V\).

---

### 4. Direct verification of the Riccati residual and terminal behavior

Let \(h=f_\pm^2\). Then
\[
\frac{h'}h=\frac{a_\pm}{q},
\qquad
R'=-\frac4{qh}.
\]
For \(c=(hR)^{-1}\),
\[
c'
=-c\left(\frac{a_\pm}{q}+\frac{R'}R\right)
=\frac{4c^2-a_\pm c}{q}.
\]
With \(K=-4c\),
\[
K'
=-4c'
=-\frac{16c^2-4a_\pm c}{q}
=-\frac{K(K+a_\pm)}q.
\]
This reproduces both symbolic zero residuals in the JSON file.

For \(0<x<1\), the integral representation gives
\[
R_\pm(x)>0,
\]
so \(\Delta_\pm(x)>0\) on that interval. As \(x\uparrow1\),
\[
R_\pm(x)\sim\frac{1-x}{p(1)f_\pm(1)^2},
\qquad
c_\pm(x)\sim\frac1{2(1-x)},
\]
and therefore
\[
K_\pm(x)\sim-\frac2{1-x}.
\]
The divergence at \(x=1\) is exactly the vertical Lagrangian plane enforcing the hard Dirichlet terminal condition. There is no earlier pole in the outgoing DtN graph on \(0<x<1\).

---

### 5. Linear Jacobi/Lagrangian interpretation of finite Riccati poles

For one channel, write the Lagrangian line as a graph
\[
K=\Pi X^{-1}.
\]
A Hamiltonian linear system producing the scalar Riccati equation is
\[
X'=\frac{a_\pm}{2q}X+\frac1q\Pi,
\qquad
\Pi'=-\frac{a_\pm}{2q}\Pi.
\]
Indeed,
\[
K'=\frac{\Pi'}X-\frac{\Pi X'}{X^2}
=-\frac{K(K+a_\pm)}q.
\]

Where \(\Pi\ne0\), put
\[
z=\frac X\Pi=\frac1K.
\]
Then
\[
z'-\frac{a_\pm}{q}z=\frac1q.
\]
Since
\[
(f_\pm^2)'/f_\pm^2=a_\pm/q,
\]
\[
\boxed{
\left(\frac z{f_\pm^2}\right)'
=\frac1{qf_\pm^2}.
}
\]
Thus
\[
z(s)=f_\pm(s)^2
\left[
\frac{z(\rho)}{f_\pm(\rho)^2}
+\int_\rho^s\frac{dr}{q(r)f_\pm(r)^2}
\right].
\]

For seed-like data
\[
K(\rho)=-\gamma a_\pm(\rho),
\qquad
z(\rho)=-\frac1{\gamma a_\pm(\rho)},
\]
a Riccati pole occurs when the bracket vanishes. At that point
\[
X=0,\qquad \Pi\ne0.
\]
The Lagrangian line is regular and vertical; only the graph coordinate \(K=\Pi/X\) ceases to exist. The inverse graph \(z=X/\Pi\) passes smoothly through zero.

For the minus channel,
\[
\frac1{qf_-^2}=\frac{(1+s)^4}{s^3},
\]
with antiderivative
\[
F_-(s)=\frac{s^2}{2}+4s+6\log s-\frac4s-\frac1{2s^2}.
\]
The pole equation is therefore
\[
F_-(s_*)-F_-(\rho)
=
\frac{(1+\rho)^5}
{\gamma(2-3\rho)\rho^2}.
\]
At \(\rho=0.1,\gamma=1\), the right side is approximately \(94.7359\), giving
\[
s_*=0.59560392,
\]
in agreement with the stored \(0.5956039198\). The same equation gives the stored \(19.9806\) value for \(\rho=.003,\gamma=.99\). For \(\rho=.003,\gamma=.985\), the root is around \(29.9\), so the JSON statement “no pole before \(20\)” is accurate but does not mean no later pole. More generally, for \(0<\rho<2/3\), the minus-channel integral diverges as \(s\to\infty\), so every such seed with \(\gamma>0\) has one finite forward pole.

A terminology refinement: \(f_\pm^2\) is the homogeneous solution multiplier for the \(z\)-equation; the standard scalar integrating multiplier is \(f_\pm^{-2}\). The displayed equations themselves are correct.

---

### 6. Meaning of the crossing

The Step-7 factorization gives, for compactly supported \(v\),
\[
Q_\pm[v]
=\int p f_\pm^2\left((v/f_\pm)'\right)^2dx>0
\]
unless \(v=0\). Thus the sign-changing potential \(V_-\) does not produce a compactly supported direction whose quadratic energy is \(<0\).

A pole from propagated seed data has a different meaning. It is a vertical crossing of the Jacobi Lagrangian plane for a mixed initial Robin condition. Such a crossing is geometrically real—it can carry Maslov or focal information—but it is not a compact-support Sturm mode. Its relevance is whether the bolt-side plane intersects or matches the outgoing plane with the required terminal relations.

The transverse calculation alone does not determine the complete bolt-to-CH match. The longitudinal torsion-free variable, including the Step-7 moment relation
\[
\int_\rho^1 f_-v_-\,dx
=-2\left(\frac{\rho}{1+\rho}\right)^2\theta(\rho),
\]
and the regular bolt data still enter the full Lagrangian comparison.

### Overall finding

The corrected \(K/Y\) distinction, scalar CH Riccati equations, factors in the two \(\Delta_\pm\) formulas, and hard-terminal signs are all consistent. The computation does reframe the \(u_2=2\) transverse Chern–Simons crossing as a Lagrangian matching problem rather than evidence for a compactly supported CH direction of energy below zero. The main presentation points are the normalized-versus-unnormalized channel convention, the fact that \(K\) is the Hessian of \(S=-V\), and the distinction between a regular vertical Lagrangian crossing and a singular Riccati graph coordinate.