# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 18,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step18_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step18_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently check the corrected Hamilton–Jacobi transverse Hessian/Riccati analysis in the Step-18 note. Verify the distinction between K and shifted Y, derive the exact CH scalar Riccati equations from the supplied formulas, check that K_+=-2/Delta_+ and K_-=-2(1+x)^5/Delta_- match the Step-7 positive ground states and outgoing Dirichlet-to-Neumann form, and interpret finite Riccati poles via the linear Jacobi/Lagrangian system. Identify any sign, factor, boundary-condition, or interpretation error. The scientific issue is whether the computation truly reframes the crossing as a graph-chart/matching problem rather than a compactly supported CH instability.

## Integrated Scientific Memo

# Verification memo

## Verdict

The corrected Step-18 transverse Hamilton–Jacobi calculation is algebraically sound:

- the distinction between the actual Hessian \(K\) and the shifted variable \(Y=K+A/2\) is correct;
- the exact-CH scalar Riccati equations have the stated signs and factors;
- the closed forms
  \[
  K_+=-\frac{2}{\Delta_+},\qquad
  K_-=-\frac{2(1+x)^5}{\Delta_-}
  \]
  are exactly the hard-Dirichlet Dirichlet-to-Neumann Hessians associated with the Step-7 positive ground states;
- finite Riccati poles are vertical crossings of a propagated Lagrangian plane, not singularities of the underlying Jacobi system and not evidence of a negative compactly supported CH mode.

There are, however, three qualifications:

1. \(f_\pm^2\) are the homogeneous solution multipliers for the \(z=1/K\) equation; the conventional integrating factors are \(f_\pm^{-2}\).
2. A Riccati pole is not merely ignorable “chart noise”: it can obstruct continuation of a particular smooth quadratic graph/subsolution and carries focal/Maslov information, even though it does not imply a compactly supported instability.
3. Formulas (2.2) are outgoing planes for the benchmark target \(x=1\). For a collar ending at \(X\), the plane is \(X\)-dependent, and the full cell matching also includes the longitudinal torsion-free variable \(\theta\).

Thus the scientific conclusion is correct but should be phrased precisely: the Chern–Simons Hessian crossing is a **Lagrangian boundary/matching problem**, not a compactly supported CH spectral instability.

---

## 1. \(K\) and shifted \(Y\)

On
\[
N=\{u_1=u_3=0\},\qquad \xi=(u_1,u_3)^T,
\]
the transverse free flow is
\[
D_0\xi=DA\xi,
\qquad
A=\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},
\qquad
D=\frac1W\operatorname{diag}(a_1^2,a_3^2).
\]
Indeed,
\[
\dot u_1=\frac{2u_1+u_2u_3}{\lambda_1},\qquad
\dot u_3=\frac{u_2u_1+2u_3}{\lambda_3},
\qquad \lambda_i^{-1}=\frac{a_i^2}{W}.
\]

For
\[
S=\frac12\xi^TK\xi+O(|\xi|^3),
\]
where \(D_0K\) differentiates the coefficient matrix along the longitudinal flow on \(N\),
\[
D_0S
=\frac12\xi^T(D_0K)\xi
+\frac12\xi^T(KDA+ADK)\xi,
\]
while
\[
\frac1W\sum_i a_i^2S_{u_i}^2=\xi^TKDK\xi.
\]
Hence the quadratic Hamiltonian matrix is
\[
E(K)=\frac12D_0K+\frac12(KDA+ADK)+KDK.
\]

Set \(Y=K+A/2\), equivalently \(K=Y-A/2\). Then
\[
E(K)
=\frac12D_0Y+YDY-\frac14(ADA+D_0A),
\]
because all mixed \(YDA\) and \(ADY\) terms cancel. Therefore
\[
E(K)\le0
\iff
\frac12D_0Y+YDY\le\frac14(ADA+D_0A).
\]

The boundary identifications are consequently
\[
S=-\Phi=-\frac12\xi^TA\xi
\quad\Longrightarrow\quad
(K,Y)=(-A,-A/2),
\]
and
\[
S=0
\quad\Longrightarrow\quad
(K,Y)=(0,A/2).
\]
Thus Step 17’s earlier identification of \(Y=0\) with \(S=0\) was indeed wrong; the Step-18 correction is exact. In fact, \(Y=0\) corresponds to \(K=-A/2\).

On \(N\),
\[
D_0A=\dot u_2
\begin{pmatrix}0&1\\1&0\end{pmatrix}
=\frac{2u_2}{\lambda_2}
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
since \(H_2=u_2\).

A useful sign check is \(K=-A\):
\[
E(-A)=-\frac12D_0A,
\]
and hence
\[
\xi^TE(-A)\xi
=-\frac{2u_1u_2u_3}{\lambda_2},
\]
which reproduces the supplied relative-calibration Hamiltonian.

---

## 2. Exact-CH scalar Riccati equations

On exact CH,
\[
a_1=a_3=\sqrt{x},\qquad
a_2=\sqrt{x(1+x)},\qquad
u_2=3x.
\]
Put \(q=x(1+x)\). Then
\[
W=x\sqrt q,\qquad D=q^{-1/2}I,\qquad
\frac{dx}{dt}=2\sqrt q.
\]

In the orthonormal channels
\[
\eta_\pm=\frac{u_1\pm u_3}{\sqrt2},
\]
\(A\) has eigenvalues
\[
a_\pm=2\pm3x.
\]
For a scalar channel Hessian \(K_\pm(x)\), the equality equation \(E(K)=0\) is
\[
\frac12\dot K_\pm+q^{-1/2}K_\pm(K_\pm+a_\pm)=0.
\]
Using \(\dot K_\pm=2\sqrt q\,K_\pm'\) gives
\[
\boxed{
K_\pm'
+\frac{K_\pm(K_\pm+2\pm3x)}{x(1+x)}=0.
}
\]
There is no missing factor or sign.

For \(z_\pm=1/K_\pm\),
\[
\boxed{
z_\pm'
-\frac{2\pm3x}{x(1+x)}z_\pm
=\frac1{x(1+x)}.
}
\]
Now
\[
\frac{2+3x}{x(1+x)}
=\frac2x+\frac1{1+x},
\qquad
\frac{2-3x}{x(1+x)}
=\frac2x-\frac5{1+x}.
\]
Thus the positive functions
\[
f_+^2=x^2(1+x),\qquad
f_-^2=\frac{x^2}{(1+x)^5}
\]
satisfy
\[
\frac{(f_\pm^2)'}{f_\pm^2}
=\frac{2\pm3x}{x(1+x)}.
\]
Equivalently,
\[
\boxed{
\left(\frac{z_\pm}{f_\pm^2}\right)'
=\frac1{x(1+x)f_\pm^2}.
}
\]

Terminology correction: \(f_\pm^2\) are homogeneous solutions/multipliers for \(z\); in the standard linear-ODE convention, the integrating factors multiplying the equation are \(f_\pm^{-2}\).

---

## 3. Relation to Step-7 ground states and the factor in \(K_\pm\)

Step 7 uses the unnormalized variables
\[
v_\pm=u_1\pm u_3=\sqrt2\,\eta_\pm,
\]
whereas \(K_\pm\) are eigenvalues in the orthonormal \(\eta_\pm\) basis. This normalization is responsible for the otherwise easy-to-miss factors.

The Step-7 ground states are
\[
f_+=x\sqrt{1+x},\qquad
f_-=\frac{x}{(1+x)^{5/2}},
\]
and, with
\[
p=\frac{x(1+x)}4,\qquad
\beta_\pm=\frac{2\pm3x}{8},
\]
they satisfy
\[
\frac{f_\pm'}{f_\pm}
=\frac{2\pm3x}{2x(1+x)},
\qquad
p\,\frac{f_\pm'}{f_\pm}=\beta_\pm.
\]

For prescribed \(v(\rho)=V\) and hard terminal condition \(v(1)=0\), the total positive channel cost—relative action plus the entrance \(\Phi\)-charge—is
\[
\int_\rho^1p f_\pm^2
\left((v/f_\pm)'\right)^2dx.
\]
Its sharp minimum is
\[
c_\pm(\rho)V^2,
\qquad
c_\pm(\rho)=\frac1{f_\pm(\rho)^2R_\pm(\rho)},
\]
where
\[
R_\pm(\rho)=\int_\rho^1\frac{ds}{p(s)f_\pm(s)^2}.
\]
Direct integration gives
\[
R_+(\rho)=\frac{2\Delta_+(\rho)}
{\rho^2(1+\rho)},
\qquad
R_-(\rho)=\frac{2\Delta_-(\rho)}{\rho^2},
\]
and therefore
\[
c_+=\frac1{2\Delta_+},
\qquad
c_-=\frac{(1+\rho)^5}{2\Delta_-}.
\]

Because \(v=\sqrt2\,\eta\), the value function in the orthonormal channel is
\[
V_{\rm out}(\eta)=2c_\pm\eta^2.
\]
The Hamilton–Jacobi calibration is \(S=-V_{\rm out}\), so
\[
\frac12K_\pm\eta^2=-2c_\pm\eta^2,
\qquad K_\pm=-4c_\pm.
\]
Hence
\[
\boxed{
K_+(x)=-\frac2{\Delta_+(x)},\qquad
K_-(x)=-\frac{2(1+x)^5}{\Delta_-(x)}.
}
\]
Thus the script’s `kplus=-4*cplus`, `kminus=-4*cminus` is correct.

The Step-7 relative-action coefficients satisfy
\[
d_\pm=c_\pm-\frac{2\pm3\rho}{4},
\]
because
\[
\Phi=\frac{2+3\rho}{4}v_+^2+
     \frac{2-3\rho}{4}v_-^2.
\]
Therefore the Riccati Hessian is built from the **total** coefficient \(c_\pm\), not from \(d_\pm\) alone.

The sign is also correct: \(K\) is the Hessian of \(S=-V\), so it is the negative of the positive outgoing value Hessian.

---

## 4. Direct residual and hard-target boundary behavior

Let \(h=f_\pm^2\) and \(c=(hR)^{-1}\). Since
\[
\frac{h'}h=\frac{a_\pm}{q},
\qquad
R'=-\frac4{qh},
\]
one obtains
\[
c'
=-c\left(\frac{a_\pm}{q}+\frac{R'}R\right)
=\frac{4c^2-a_\pm c}{q}.
\]
For \(K=-4c\),
\[
K'
=-4c'
=-\frac{K(K+a_\pm)}q.
\]
This proves the symbolic zero residuals reported in the JSON.

For \(0<x<1\),
\[
R_\pm(x)>0,
\]
so \(\Delta_\pm(x)>0\), and the outgoing graph has no pole before the target. As \(x\uparrow1\),
\[
R_\pm(x)\sim\frac{1-x}{p(1)f_\pm(1)^2},
\qquad
K_\pm(x)\sim-\frac2{1-x}.
\]
The terminal divergence is precisely the vertical Lagrangian plane implementing \(v_\pm(1)=0\). It is not a defect in the solution.

The Chern–Simons seed eigenvalue \(K_-^{\rm seed}=-(2-3x)\) vanishes at \(x=2/3\), but the outgoing \(K_-\) above is smooth there. In Sturm language, \(x=2/3\) is where
\[
f_-'(x)=0,
\]
the positive ground state turns over; it is not a zero of the ground state.

---

## 5. Linear Jacobi/Lagrangian interpretation

A Hamiltonian linear system producing the scalar Riccati equation is
\[
X'=\frac{a_\pm}{2q}X+\frac1q\Pi,
\qquad
\Pi'=-\frac{a_\pm}{2q}\Pi.
\]
If the Lagrangian line is transverse to the \(X=0\) vertical, it is represented by
\[
K=\Pi X^{-1}.
\]
Then
\[
K'=-\frac{K(K+a_\pm)}q.
\]
In the inverse chart
\[
z=\frac X\Pi=\frac1K,
\]
one obtains the regular linear equation
\[
z'-\frac{a_\pm}{q}z=\frac1q.
\]

A finite Riccati pole means
\[
X=0,\qquad \Pi\ne0.
\]
The Lagrangian line itself is regular and vertical; only the graph coordinate \(K=\Pi/X\) fails. The inverse chart \(z=X/\Pi\) passes smoothly through zero.

For seed-like data
\[
K(\rho)=-\gamma(2\pm3\rho),
\qquad
z(\rho)=-\frac1{\gamma(2\pm3\rho)},
\]
the solution is
\[
z(x)=f_\pm(x)^2\left[
\frac{z(\rho)}{f_\pm(\rho)^2}
+\int_\rho^x\frac{ds}{s(1+s)f_\pm(s)^2}
\right].
\]
Thus poles are exactly zeros of the bracket.

For the minus channel,
\[
\frac1{x(1+x)f_-^2}=\frac{(1+x)^4}{x^3},
\]
with primitive
\[
G(x)=\frac{x^2}{2}+4x+6\log x-\frac4x-\frac1{2x^2}.
\]
The pole position \(x_p\) therefore satisfies
\[
\boxed{
G(x_p)-G(\rho)
=
\frac{(1+\rho)^5}
{\gamma\,\rho^2(2-3\rho)}.
}
\]
This reproduces, for example,
\[
(\rho,\gamma)=(0.1,1)
\quad\Longrightarrow\quad
x_p=0.595603919\ldots,
\]
matching the stored result.

For \(0<\rho<2/3\), \(G(x)\to\infty\), so every such minus seed has exactly one finite forward pole. Consequently, JSON `null` means only “no pole before \(x=20\),” not “no pole at all.” In particular, the \(\rho=.003,\gamma=.985\) pole lies beyond the integration window.

The monotonicity
\[
\left(z/f_\pm^2\right)'>0
\]
also implies that one scalar solution has at most one pole. This is the Riccati counterpart of the positive-ground-state/disconjugacy result: a negative compactly supported Sturm direction would require the relevant zero-energy Jacobi solution to develop two zeros, which cannot occur here.

---

## 6. What the poles do and do not prove

The Step-18 interpretation is correct in its principal claim but should avoid two extremes.

A pole does **not** mean:

- that the Jacobi evolution ceases to exist;
- that the Lagrangian plane becomes singular;
- that exact CH has a negative compactly supported transverse mode.

Indeed, for compactly supported \(v\),
\[
Q_\pm[v]
=\int p f_\pm^2\left((v/f_\pm)'\right)^2dx\ge0,
\]
with equality only in the trivial compactly supported case.

But a pole is not mathematically irrelevant. It is a real vertical/focal crossing and can show that a particular Hessian graph cannot be continued globally in that chart. For a smooth quadratic HJ subsolution, outgoing value comparison still imposes an order relation at a cut. With the present sign convention,
\[
S_{\rm in}(\eta)=\frac12K_{\rm in}\eta^2,\qquad
S_{\rm out}(\eta)=\frac12K_{\rm DtN}\eta^2,
\]
the admissible inequality \(S_{\rm in}\le V_{\rm out}\) or its equivalent calibration form must be checked with the chosen orientation; after fixing that convention, Riccati comparison determines whether the incoming graph lies on the admissible side of the outgoing plane. A chart change preserves the Lagrangian plane but cannot erase a genuine failure of this comparison.

Accordingly, “possibly across graph-chart changes” is appropriate for transporting the bolt-side plane, but should not be read as allowing an inadmissible seed graph to bypass the outgoing boundary inequality.

For \(c=1\), the occurrence of a minus-channel pole before the benchmark target \(x=1\) is equivalent to
\[
d_-(\rho)<0.
\]
It is therefore another representation of the Step-7 signed endpoint mismatch, not a new bulk instability.

---

## 7. Scope of the outgoing benchmark

The formulas in Step 18 fix the hard target at \(x=1\). For a general terminal point \(X\),
\[
\boxed{
K_\pm^{X}(\rho)=
-\left[
f_\pm(\rho)^2
\int_\rho^X
\frac{ds}{s(1+s)f_\pm(s)^2}
\right]^{-1}.
}
\]
The factors here agree with the \(x=1\) formulas because this expression is in the orthonormal Hessian normalization.

Thus (2.2) is an exact benchmark, but it is not universally the outgoing plane of a cell whose CH collar terminates elsewhere. In particular, as \(X\to\infty\),
\[
K_-^X(\rho)\to0,
\]
because the minus integral diverges. The free transverse minus mode by itself then has vanishing asymptotic DtN cost.

This does not settle the actual cell matching, because torsion-free reconstruction couples the minus channel to
\[
\theta=\delta\log(a_1/a_3)
\]
through
\[
\frac d{dx}\left[
\left(\frac{x}{1+x}\right)^2\theta
\right]
=\frac12f_-v_-.
\]
For \(\theta(X)=0\),
\[
\int_\rho^X f_-v_-\,dx
=-2\left(\frac{\rho}{1+\rho}\right)^2\theta(\rho).
\]
Hence the full outgoing object is a joint Lagrangian relation in the transverse and longitudinal variables, not merely the two scalar \(K_\pm\). This is exactly why the scalar verification proves absence of compactly supported CH instability but does not by itself close the bolt-to-CH lower-bound problem.

---

## Final assessment

No substantive sign, factor, or \(K/Y\) boundary-condition error remains in the corrected Step-18 derivation. The exact CH formulas and the script residuals are consistent with the Step-7 factorization and hard-Dirichlet DtN problem.

The text should make the following corrections or clarifications:

- replace “integrating factors are \(f_\pm^2\)” by “homogeneous multipliers are \(f_\pm^2\), equivalently the integrating factors are \(f_\pm^{-2}\)”;
- state explicitly that `null` records no pole before the numerical cutoff, not absence of a later pole;
- identify (2.2) as the \(X=1\) hard-target plane;
- distinguish regular Lagrangian continuation through a vertical crossing from admissibility of a global smooth HJ graph;
- include the longitudinal torsion-free state in the actual outgoing matching problem.

With these qualifications, the computation genuinely reframes the \(u_2=2\) crossing: it is the degeneracy of the particular relative Chern–Simons seed and a graph/Lagrangian matching issue. It is not evidence for a compactly supported negative CH mode.