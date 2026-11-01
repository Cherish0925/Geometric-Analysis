# TTCS Independent Branch Record

```json
{
  "step_id": 71,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step70_critical_identity_and_corrections.md",
    "Sessions/S0910A03/workspace/notes/step70_mixed_boundary_formulation.md",
    "Sessions/S0910A03/workspace/scripts/step71_linearized_detruck_hyperbolic.py",
    "Sessions/S0910A03/workspace/data/step71_linearized_detruck_hyperbolic.json",
    "Sessions/S0910A01/workspace/notes/step72_graph_neck_weighted_shear_budget.md",
    "Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md"
  ]
}
```

## Task

The active goal is Yau Problem 26, but this task concerns the current negative-branch graph-neck route. Read the Step 70 and Step 71 materials plus the Li–Liu source excerpts. Independently derive and check: (i) the correct weighted normal balance for E=Ric+3g in Gaussian gauge; (ii) whether a complete exact reflection-symmetric half-core with a flat T^3 Poincare-Einstein end is ruled out by doubling and Proposition 6.6 (Witten–Yau/Cai–Galloway), including the warped-product exception; (iii) a complementing, reflection-compatible boundary formulation for the five T^2-invariant metric components in Einstein–DeTurck/Bianchi gauge. Be explicit about parity at t=0, which central metric data may vary, what geometric and gauge data belong at t=R, and why a zero of the gauge-fixed equations is or is not automatically Einstein on a manifold with boundary. Correct any sign, normalization, or boundary-count errors; do not infer nonlinear existence.

## Output

# Scientific verification memo

## 1. Weighted normal balance in Gaussian gauge

Let
\[
g=dt^2+h_t,\qquad
S=\frac12h_t^{-1}\partial_t h_t,\qquad H=\operatorname{tr}S
\]
on a four-dimensional collar, with \(t\) increasing toward the expanding end. The Riccati formula is
\[
\operatorname{Ric}_g(\partial_t,\partial_t)=-\partial_tH-|S|^2.
\]
For
\[
E=\operatorname{Ric}_g+3g
\]
this gives
\[
E_{00}=3-H'-|S|^2.
\]
Set
\[
B=S-I,\qquad b=H-3.
\]
Since
\[
|S|^2=|I+B|^2=3+2b+|B|^2,
\]
the exact pointwise identity is
\[
\boxed{b'+2b+|B|^2=-E_{00}.}
\]
Consequently,
\[
\boxed{
e^{2R}b(R)-b(0)+\int_0^R e^{2t}|B|^2\,dt
=-\int_0^R e^{2t}E_{00}\,dt.
}
\tag{1}
\]

For a reflection center, \(S(0)=0\), hence \(b(0)=-3\). If the terminal data have \(H(R)=3\), then
\[
\boxed{
3+\int_0^R e^{2t}|S-I|^2\,dt
=-\int_0^R e^{2t}E_{00}\,dt.
}
\tag{2}
\]
Thus the weighted average of \(E_{00}\) must have the compensating sign. If
\(\|E\|_{\mathrm{op}}\leq\delta\), then \(|E_{00}|\leq\delta\) and
\[
\boxed{
\delta\ge
\frac{2\left(3+\int_0^R e^{2t}|S-I|^2dt\right)}
{e^{2R}-1}
\ge \frac6{e^{2R}-1}.
}
\tag{3}
\]
The logarithmic length estimate in Step 70 is therefore correct, but the displayed integrated equation there has the sign of the \(E_{00}\)-integral reversed. Step 72 has the correct sign.

For an exact Einstein metric,
\[
3-H(t)
=e^{-2t}\left(3+\int_0^t e^{2s}|S-I|^2\,ds\right)>0.
\tag{4}
\]
Equation (4) proves \(H<3\) and
\[
3-H\ge 3e^{-2t}.
\]
It does not by itself prove \(H\to3\): that also requires
\[
e^{-2t}\int_0^t e^{2s}|S-I|^2\,ds\longrightarrow0.
\]
Thus the Step 70 summary phrase asserting exponential cusp convergence from the normal identity alone is not justified.

### Two further normalization corrections

1. The isotropic calculation in Step 70 is not an exact Einstein example. For
   \[
   h_t=e^{2f(t)}h_{\mathrm{flat}},
   \]
   the normal and tangential equations are respectively
   \[
   f''+(f')^2=1,\qquad f''+3(f')^2=3.
   \]
   Together they force \((f')^2=1\) and \(f''=0\). Hence no such solution has \(f'(0)=0\). The profile
   \(f'=\tanh(\sqrt3\,t)\) solves the tangential equation only.

2. The Li–Liu Type-I equation quoted in Step 70 is
   \[
   (e^v)_{\xi\xi}+\Delta_{T^2}v=0,
   \]
   exactly as stated in their Section 2 and BVP1. If \(v=v(\xi,\theta)\), it becomes
   \[
   (e^v)_{\xi\xi}+v_{\theta\theta}=0,
   \]
   not
   \[
   (e^v)_{\xi\xi}+(e^v)_{\theta\theta}=0.
   \]
   Its principal part is
   \[
   e^v v_{\xi\xi}+v_{\theta\theta},
   \]
   which is elliptic because \(e^v>0\), but \(e^v\) is not generally harmonic.

### PE asymptotics recover the scalar-curvature identity

Suppose the exact half-core has a smooth PE expansion with
\[
\rho=e^{-t},\qquad
g=dt^2+e^{2t}\bigl(g_0+\rho^2g_2+O(\rho^3)\bigr).
\]
In conformal dimension three,
\[
g_2=-P_{g_0},\qquad \operatorname{tr}_{g_0}g_2=-\frac14R_{g_0}.
\]
It follows that
\[
B=-\rho^2g_2^\sharp+O(\rho^3),\qquad
e^{2t}b\longrightarrow\frac14R_{g_0}.
\]
Taking \(t\to\infty\) in (1) with \(E=0\) gives
\[
\boxed{
\frac14R_{g_0}(\theta)
=-3-\int_0^\infty e^{2s}|S-I|^2(s,\theta)\,ds.
}
\tag{5}
\]
Thus the scalar normalization in Step 70 is correct under this smooth PE expansion. Since \(B(0)=-I\), the integral is strictly positive, so the center-normalized representative satisfies \(R_{g_0}<-12\). Flat conformal infinity is impossible.

---

## 2. Doubling and Li–Liu Proposition 6.6

Assume an exact half-core has:

- \(\operatorname{Ric}=-3g\);
- a smooth reflection \(t\mapsto -t\) fixing the central \(T^3\);
- one complete PE end with flat \(T^3\) conformal infinity.

The reflection gives a smooth Einstein double with two isometric PE ends. The flat \(T^3\) conformal class has Yamabe value \(0\), so Proposition 6.6 in the supplied Li–Liu source applies.

The double has two topological ends, excluding the one-end alternatives in Proposition 6.6. It would therefore have to be
\[
(\mathbb R\times N,\; ds^2+e^{-2s}g_N),
\qquad \operatorname{Ric}_{g_N}=0.
\tag{6}
\]
But (6) has:

- a PE end as \(s\to-\infty\);
- an AH cusp as \(s\to+\infty\).

The latter has finite volume,
\[
\int^\infty e^{-3s}\,ds<\infty,
\]
whereas a four-dimensional PE end has infinite volume near conformal infinity. Hence (6) cannot be isometric to the reflection double, whose two ends are both PE. The warped-product alternative therefore does not rescue the reflection construction.

This also explains why Li–Liu’s PE-to-cusp metrics do not provide reflection cores. They have one PE end and one cusp end, exactly the end structure admitted by (6) in the flat conformal-infinity case. Their general nonflat conformal infinities have Yamabe value below zero and are not covered by the \(Y\ge0\) argument.

The smooth reflection assumption matters. Merely knowing \(S(0)=0\) makes the first normal derivative match under even extension, but an arbitrary smooth metric can still have unmatched odd higher jets. Here reflection symmetry supplies all required parity. For an Einstein metric one may alternatively invoke an Einstein reflection theorem, but \(S=0\) alone is not the complete smooth-doubling argument.

---

## 3. Correct Einstein–DeTurck sign

Within the five-field ansatz,
\[
g=A\,dt^2+2D\,dt\,d\theta+C\,d\theta^2
  +P\,dx^2+Q\,dy^2,
\tag{7}
\]
all coefficients depend on \((t,\theta)\). This is \(T^2\)-invariance together with separate \(x\mapsto-x\), \(y\mapsto-y\) symmetries and an orthogonal \(x,y\) splitting; unrestricted \(T^2\)-invariance has additional components.

For a reference metric \(\bar g\), define
\[
W^\mu=g^{\alpha\beta}
\bigl(\Gamma(g)^\mu_{\alpha\beta}
-\Gamma(\bar g)^\mu_{\alpha\beta}\bigr).
\]
The elliptic DeTurck equation with this convention is
\[
\boxed{
\Phi_{\bar g}(g)
=\operatorname{Ric}_g+3g-\frac12\mathcal L_Wg=0.
}
\tag{8}
\]
Its principal linearization is componentwise
\[
-\frac12g^{\alpha\beta}\partial_\alpha\partial_\beta h_{\mu\nu}.
\]

The Step 71 script instead computes
\[
\operatorname{Ric}+3g+\frac12\mathcal L_Wg.
\]
That sign does not cancel the diffeomorphism terms. The JSON output visibly retains mixed second derivatives and terms such as \(r_{tt},s_{tt},u_{tt}\) in the \(tt\) equation. It also records that its linear Bianchi one-form is the metric dual of \(-W\). Replacing `+1/2*LV` by `-1/2*LV` gives the minimal elliptic principal symbol.

Equivalently, with the linear Bianchi one-form
\[
\beta(h)=-\nabla^jh_{ij}+\frac12d_i\operatorname{tr}h,
\]
one adds \(+\delta^*\beta\), since \(\beta=-W^\flat\) at linear order.

---

## 4. Reflection-compatible complementing face data

Take \(\bar g\) to have the same reflection and torus symmetries.

### Central face \(t=0\)

Reflection acts by
\[
(t,\theta,x,y)\mapsto(-t,\theta,x,y).
\]
Therefore
\[
A,C,P,Q\ \text{are even},\qquad D\ \text{is odd}.
\]
The five scalar conditions are
\[
\boxed{
D=0,\qquad
\partial_tA=\partial_tC=\partial_tP=\partial_tQ=0
\quad\text{at }t=0.
}
\tag{9}
\]
These are one Dirichlet and four Neumann conditions, hence complement the five Laplace-type equations componentwise.

The central induced metric is
\[
q=C(0,\theta)d\theta^2+P(0,\theta)dx^2+Q(0,\theta)dy^2.
\]
Its three coefficient functions are outputs of this mixed problem, not prescribed inputs. Prescribing a particular \(q_N\) in addition to (9) gives eight scalar conditions at that face for five second-order fields.

For an eventual Einstein solution, the Gauss equation and \(S=0\) yield
\[
R_q=R_g-2\operatorname{Ric}(\nu,\nu)=-12+6=-6.
\]
Thus scalar curvature \(-6\) follows from the Einstein equation; it is not an independent condition in (9). The value \(A(0,\theta)\) is lapse data rather than part of \(q\), while \(\partial_tD(0,\theta)\) remains free under parity.

### Outer face \(t=R\)

Let
\[
\gamma=C\,d\theta^2+P\,dx^2+Q\,dy^2
\]
be the induced metric and \(H\) its mean curvature with respect to the unit normal pointing toward the expanding end. A geometric/gauge set of five conditions is
\[
\boxed{
[\gamma]=[\gamma_*],\qquad
H=H_*,\qquad
W^t=0,\qquad W^\theta=0.
}
\tag{10}
\]
Here:

- \([\gamma]=[\gamma_*]\) contributes two scalar functions, for example
  \[
  \log(P/C),\qquad \log(Q/C);
  \]
- \(H=H_*\) contributes one geometric scalar;
- \(W^t=W^\theta=0\) contributes two gauge scalars;
- \(W^x=W^y=0\) identically in ansatz (7).

For a truncated expanding hyperbolic end,
\[
[\gamma_*]=[\gamma_{\mathrm{flat}}],\qquad H_*=3.
\]
The common conformal factor of \(\gamma\) remains an output. Likewise, the trace-free part of the second fundamental form is not prescribed. Exact attachment to a specified cusp slice would require the actual induced metric and full second fundamental form to agree; that is stronger Cauchy matching rather than the elliptic face data (10).

### Principal complementing calculation

Use an orthonormal frozen frame and write a variation as
\[
(p,q,r,s,u)
=(h_{nn},h_{n\theta},h_{\theta\theta},h_{xx},h_{yy}).
\]
For tangential frequency \(\xi\), let \(k=|\xi|\) and consider a decaying mode \(e^{-kx+i\xi\theta}\). The principal parts of (10) are
\[
r-s=0,\qquad r-u=0,
\]
\[
H'=\frac12\partial_n(r+s+u)-\partial_\theta q=0,
\]
\[
\beta_n=-\frac12\partial_np
+\frac12\partial_n(r+s+u)-\partial_\theta q=0,
\]
\[
\beta_\theta=-\partial_nq
+\frac12\partial_\theta(p-r+s+u)=0.
\]
Writing \(r=s=u=a\), the decaying mode equations become
\[
-\frac32ka-i\xi q=0,\qquad
\frac12kp=0,\qquad
kq+\frac{i\xi}{2}(p+a)=0.
\]
They force
\[
p=a=q=0,
\]
and hence all five amplitudes vanish. This verifies the Lopatinski condition for the reduced five-field system.

By contrast, prescribing all three tangential metric components together with only the two Bianchi equations is not complementing. With \(r=s=u=0\), the principal equations admit the nonzero decaying mode
\[
q=-\frac{i}{2}p
\qquad(\xi=k>0).
\]
Full Dirichlet data for all five components are complementing for the DeTurck operator, but they neither prescribe \(H\) nor force \(W=0\).

---

## 5. When a gauge-fixed zero is Einstein

A zero of (8) on a finite cylinder is not Einstein merely because it solves the elliptic DeTurck equation. Elimination of \(W\) is also required.

For the reflection formulation above, parity extends the solution and reference metric smoothly to
\[
[-R,R]\times T^3.
\]
The central slice becomes an interior hypersurface. Conditions (10) impose \(W=0\) at both outer faces.

The contracted Bianchi identity applied to (8) gives
\[
\nabla^i\nabla_iW_j+\operatorname{Ric}_{jk}W^k=0.
\]
Using
\[
\operatorname{Ric}=-3g+\operatorname{sym}\nabla W
\]
and \(\phi=|W|^2\), one obtains
\[
\boxed{
\frac12\bigl(\Delta\phi+W\cdot\nabla\phi\bigr)
=|\nabla W|^2+3\phi.
}
\tag{11}
\]
Since \(\phi=0\) at both outer faces, the maximum principle gives
\[
W\equiv0.
\]
Thus every sufficiently smooth zero of the specific reflected problem (8)–(10) is Einstein. With five-component Dirichlet data alone, \(W\) need not vanish at the outer face, so the same conclusion does not follow.

These calculations establish the correct elliptic formulation and its geometric meaning. They do not provide invertibility of the linearized operator or a nonlinear solution.