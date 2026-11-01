# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step80_joint_base_response_and_inner_layer.md",
    "Sessions/S0910A03/workspace/data/step82_geometric_balance.json",
    "Sessions/S0910A03/workspace/data/step82_turning_covariance_model.json"
  ]
}
```

## Task

Develop the strongest mathematically plausible next step from the slice balances for the finite small-defect graph connector. Focus on the actual reversal problem: starting at a reflected scalar-minus-six center with I(0)=J(0)=0 and I'(0)=-3V, J'(0)=6V, can the coupled OT Einstein or small-defect equations dynamically create the covariance/orbit-expansion term needed for I to return to zero before singularity? Seek either (a) a coercive evolution identity controlling the turning expression 2Cov(u,v)+<v^2>/2-<|B0|^2> using the orbit H^2 energy, Codazzi/base constraints, and J' balance, or (b) a constraint-compatible perturbative center family whose exact early radial jets make the expression grow toward 3. Work in physical measures and retain all Einstein components. Do not return to constant-exit maximum principles or Noether current alone. Provide explicit equations/calculations and a decisive low-cost computation or theorem target, while clearly separating a mechanism from an established connector.

## Output

A strong way to sharpen the reversal problem is to stop viewing the first-return term primarily as a covariance expression and rewrite it as a spatial orbit-energy statement. In the OT Gaussian variables this gives a much more rigid target.

Let

\[
g=dr^2+q_r,\qquad 
q_r=ds^2+e^\sigma M_{ab}d\xi^ad\xi^b,\qquad \det M=1,
\]

where \(s\) is physical arclength on the base circle of the slice, and

\[
d\mu=e^\sigma ds\,d\xi^1d\xi^2,\qquad V=\int d\mu.
\]

Write

\[
u=S^s{}_s,\qquad 
S_{\mathrm{orb}}=\frac v2 I+B_0,\qquad 
H=u+v,
\]

and denote normalized averages by \(\langle f\rangle=V^{-1}\int f\,d\mu\). Let

\[
x=\langle u\rangle=I/V,\qquad y=\langle v\rangle=J/V.
\]

For the intrinsic slice geometry define

\[
h=D_s\sigma,\qquad a=U_s,\qquad e=|a|_{\mathbb H^2}^2,\qquad 
K:=\langle e-h^2\rangle .
\]

Here \(U=M:S^1\to SL(2,\mathbb R)/SO(2)\cong \mathbb H^2\), with the same normalization as in Steps 79–81.

The intrinsic scalar curvature identity on every closed free \(T^2\)-slice is

\[
R(q)=-2D_sh-\frac32h^2-\frac12 e,
\]

hence, after physical integration,

\[
\boxed{\langle R(q)\rangle=-\frac12\langle e-h^2\rangle=-\frac12K.}
\]

The Hamilton equation with \(E=\operatorname{Ric}_g+3g\) gives

\[
R(q)=-6+H^2-|S|^2+2E_{rr}
     =-6+2uv+\frac12v^2-|B_0|^2+2E_{rr}.
\]

Therefore, at any differentiable first return \(x=I/V=0\),

\[
\boxed{
2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle-\langle |B_0|^2\rangle
=
6-\frac12K-2\langle E_{rr}\rangle .
}
\]

Also

\[
\boxed{
x'=3-\frac12K-\langle E_{ss}\rangle-x(x+y),
}
\]

and at a first return \(x=0\),

\[
\boxed{
x'\ge0
\quad\Longrightarrow\quad
K\le 6-2\langle E_{ss}\rangle .
}
\]

Thus the true reversal target is:

\[
\boxed{
\text{the spatial orbit-energy excess }K=\langle |U_s|^2_{\mathbb H^2}-h^2\rangle
\text{ must fall from }12\text{ to about }6.
}
\]

At the reflected scalar-minus-six center,

\[
S(0)=0,\qquad R(q_0)=-6,
\]

so

\[
K(0)=12,\qquad x(0)=y(0)=0,\qquad x'(0)=-3,\qquad y'(0)=6
\]

for the exact Einstein equation, or with the corresponding averaged defect traces set to zero.

The coupled OT dynamics gives an exact evolution identity for \(K\). Let \(b=U_r\), so \(|b|_{\mathbb H^2}^2=2|B_0|^2\), and define the weighted spatial tension

\[
\tau=\nabla_s a+h\,a .
\]

The traceless orbit equation has the physical form

\[
\boxed{
\nabla_r b+H b+\tau=\mathcal E_0,
}
\]

where \(\mathcal E_0\) is the \(\mathbb H^2\)-tangent representative of the traceless orbit defect. The commutator identity is

\[
\boxed{
\nabla_r a=\nabla_s b-u\,a.
}
\]

The mixed Einstein component gives the Codazzi relation

\[
\boxed{
D_s v=h\left(u-\frac v2\right)-\frac12\langle a,b\rangle_{\mathbb H^2}-E_{rs}.
}
\]

Set

\[
c:=D_sh+h^2=-R_{\mathrm{orb}}^{\mathrm{tr}},
\qquad
k:=e-h^2.
\]

Then

\[
\boxed{
K'
=
-2\langle \langle \tau,b\rangle\rangle
+2\langle v c\rangle
+\operatorname{Cov}(v-u,k)
-2xK
+\mathcal E_K,
}
\]

with

\[
\mathcal E_K
=
2\langle \langle \mathcal E_0,b\rangle\rangle
\]

if the orbit defect is placed in the displayed orbit equation convention. Using Codazzi,

\[
\boxed{
\langle vc\rangle
=
-\langle hD_sv\rangle
=
-\left\langle h^2\left(u-\frac v2\right)\right\rangle
+\frac12\langle h\langle a,b\rangle\rangle
+\langle hE_{rs}\rangle .
}
\]

So an exact reduction of \(K\) before first return requires a very specific dynamical alignment:

\[
-2\langle \tau,b\rangle
+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)
\]

must overcome the positive term \(-2xK\), since along the pre-return interval one has \(x<0\). In words: the radial orbit velocity \(b\) must eventually align with \(+\tau\), not with its reflected initial direction, and/or the Codazzi-controlled area/orbit correlations must become strongly favorable. This is a sharper mechanism than the raw covariance expression.

The reflected center jets make this especially rigid. At the center,

\[
b(0)=u(0)=v(0)=0,
\qquad
b_r(0)=-\tau_0
\]

for exact Einstein. Moreover scalar-minus-six implies

\[
e=12-4D_sh-3h^2,
\qquad
k=e-h^2=12-4(D_sh+h^2),
\]

hence

\[
c=D_sh+h^2=\frac{12-k}{4},
\]

and

\[
\boxed{
u_1:=u_r(0)=-\frac14 k,\qquad
v_1:=v_r(0)=3+\frac14 k,\qquad
\langle k\rangle=12.
}
\]

Consequently

\[
\boxed{
K'(0)=0,
}
\]

and the exact averaged second jet is

\[
\boxed{
K''(0)
=
2\langle |\tau_0|_{\mathbb H^2}^2\rangle
+18+\frac38\langle k^2\rangle
\ge
72+2\langle |\tau_0|_{\mathbb H^2}^2\rangle .
}
\]

Thus \(K\) initially moves upward, not downward, for every reflected exact scalar-minus-six OT center. In normalized mean form,

\[
x'=3-\frac12K-x(x+y)
\]

in the exact case, so near the center

\[
\boxed{
x(r)
=
-3r+
\frac13\left(9-\frac14K''(0)\right)r^3+O(r^5).
}
\]

Since \(K''(0)\ge72\),

\[
\boxed{
x(r)\le -3r-3r^3+O(r^5).
}
\]

So reversal cannot be a very short radial effect. It requires a later transfer that first allows \(K\) to rise and then drives it below roughly \(6\).

There is nevertheless a useful perturbative center test. For a constant-area center \(h=0\), scalar-minus-six means simply

\[
|U_s|_{\mathbb H^2}^2=12.
\]

The center may be any constant-speed closed curve in \(\mathbb H^2\), not only the polar circle \(d=d_*,\psi=mz\). Then \(k=12\), \(u_1=-3\), \(v_1=6\), and

\[
B_{0,r}(0)=-\frac12\tau_0.
\]

The first nonzero coefficient of the turning expression is

\[
\boxed{
2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle-\langle |B_0|^2\rangle
=
r^2\left(
18-\frac12\langle |\tau_0|_{\mathbb H^2}^2\rangle
\right)
+O(r^4).
}
\]

For the polar rotating loop from Step 81,

\[
\langle |\tau_0|^2\rangle=12(m^2+12),
\]

so the coefficient is

\[
18-6(m^2+12)<0.
\]

That bad sign is a property of the circular polar loop, not of all scalar-minus-six centers.

The most economical center-level variational problem is therefore:

\[
\boxed{
\inf
\left\{
\frac12\langle |\nabla_sU_s|^2_{\mathbb H^2}\rangle:
U:S^1\to\mathbb H^2,\ 
|U_s|^2=12,\ 
U \text{ closed}
\right\}.
}
\]

If this infimum is \(<18\), there are scalar-minus-six reflected centers whose turning expression initially grows in the favorable direction, although \(x\) still moves downward because \(K''(0)>0\). If the infimum is \(\ge18\), then even the best constant-area center has nonpositive quadratic turning coefficient.

For variable area centers the analogous exact one-dimensional functional is

\[
\boxed{
\mathcal Q[h,U]
=
\frac12\langle |\tau_\rho(U)|^2\rangle
+\frac{3}{32}\operatorname{Var}_\rho(k),
}
\]

where

\[
\rho_s=h\rho,\qquad
e=|U_s|^2=12-4D_sh-3h^2,\qquad
k=e-h^2.
\]

Then

\[
\boxed{
T(r)
=
r^2\left(18-\mathcal Q[h,U]\right)+O(r^4).
}
\]

This is a clean scalar-minus-six center test retaining the exact Hamilton, orbit-trace, traceless-orbit, and Codazzi content at the first nontrivial order.

A decisive low-cost computation is a one-dimensional hyperbolic-elastica solve in the Poincaré disk or hyperboloid model:

\[
U(s)\in\mathbb H^2,\qquad |U_s|^2=12,
\qquad U(0)=U(L),
\]

minimizing

\[
\frac12\langle |\nabla_sU_s|^2\rangle .
\]

For graph-specific use, the same computation can be repeated with whatever loop class in the orbit-shape space is required by the graph block matching. The output is just a center \(q_0\). Its exact reflected Einstein jets are then generated by

\[
S_1=\operatorname{Ric}(q_0)+3I,
\]

\[
S_2=0,
\]

\[
\boxed{
S_3
=
D\operatorname{Ric}_{q_0}[\,2S_1^\flat\,]-6S_1,
}
\]

and higher odd \(S\)-jets by differentiating

\[
S'+HS=\operatorname{Ric}(q_r)+3I-E_T.
\]

The accompanying scalar observables are

\[
x(r),\qquad y(r),\qquad K(r),\qquad
T(r)=2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle-\langle |B_0|^2\rangle .
\]

This computation distinguishes three mathematically different possibilities:

1. The elastica minimum still has  
   \[
   \frac12\langle |\tau|^2\rangle\ge18,
   \]
   so the turning expression does not even begin to grow favorably in the constant-area class.

2. A low-tension closed curve gives  
   \[
   \frac12\langle |\tau|^2\rangle<18,
   \]
   producing favorable \(T_2\), but the exact \(x\)-jet remains downward because \(K''(0)\ge72\). Then the later \(K\)-drop mechanism becomes the central issue.

3. A variable-area center lowers  
   \[
   \mathcal Q[h,U]
   =
   \frac12\langle |\tau_\rho|^2\rangle
   +\frac{3}{32}\operatorname{Var}_\rho(k)
   \]
   below the constant-area value and also creates favorable Codazzi terms
   \[
   -2\left\langle h^2\left(u-\frac v2\right)\right\rangle
   +\langle h\langle a,b\rangle\rangle ,
   \]
   giving a concrete candidate mechanism for later reduction of \(K\).

None of these gives a connector by itself. The established exact facts are the first-return identity

\[
x=0,\ x'\ge0
\quad\Longrightarrow\quad
K\le6-2\langle E_{ss}\rangle,
\]

the \(K'\) identity with Codazzi substitution, and the universal center behavior

\[
K(0)=12,\qquad K'(0)=0,\qquad K''(0)\ge72.
\]

The unresolved dynamical question is now precise: can the coupled OT equations, with all defect components small in physical norm, drive

\[
K=\langle |U_s|^2-h^2\rangle
\]

from its universal initial rise down to roughly \(6\) before the Gaussian evolution develops a singularity?