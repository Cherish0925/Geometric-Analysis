# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step82_slice_balance_verify.py",
    "Sessions/S0910A03/workspace/data/step82_slice_balance.json",
    "Sessions/S0910A03/workspace/scripts/step82_geometric_balance_check.py",
    "Sessions/S0910A03/workspace/data/step82_geometric_balance.json",
    "Sessions/S0910A03/workspace/scripts/step82_turning_covariance_model.py",
    "Sessions/S0910A03/workspace/data/step82_turning_covariance_model.json",
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step80_joint_base_response_and_inner_layer.md"
  ]
}
```

## Task

Independently verify the physical Gaussian-slice balance derivation for the orthogonally transitive T^2-invariant metric and sharpen what it says about reversal of mean horizontal contraction. Use E=Ric_g+3g, q_r=e^{2a}dz^2+G_ab dx^a dx^b, rho=sqrt(det G), u=a_r, B=(1/2)G^{-1}G_r, v=tr B, B0=B-(v/2)I, dmu=e^a rho dz, V=int dmu, I=int u dmu, J=int v dmu. Check (i) J'=6V-int tr_orbit(E)dmu, (ii) I'=3V+int R(q_r)dmu-int E_zz dmu, including why the intrinsic orbit-Ricci trace integrates to zero, and (iii) after the Hamilton constraint, whether the defect term is 2E_rr-E_zz or tr_orbit(E)-E_rr. Derive the necessary inequality at the first return I=0 after I<0 under ||E||op<=delta, carefully treating covariance, differentiability, and signs. Then investigate whether the orbit-map energy identity, matrix equation, base constraints, or J/V evolution yields a nontrivial bound on 2Cov(u,v)+<v^2>/2-<|B0|^2> strong enough to prevent reversal, or whether the balances alone admit algebraically favorable slices. Give direct mathematics, state exact hypotheses, and distinguish slice compatibility from dynamic reachability. Check the session scripts/data rather than trusting their summaries.

## Output

# Scientific memo: Gaussian-slice balances and horizontal mean reversal

## 1. Geometric hypotheses and conventions

Let
\[
g=dr^2+q_r,\qquad
q_r=e^{2a(r,z)}dz^2+G_{ab}(r,z)\,dx^a dx^b
\]
on an interval times a closed free \(T^2\)-invariant three-manifold, with \(z\) periodic and \(G\) positive definite. Set
\[
\rho=\sqrt{\det G},\quad
u=a_r,\quad
B=\frac12G^{-1}G_r,\quad
v=\operatorname{tr}B,\quad
B_0=B-\frac v2I.
\]
The slice shape operator and its trace are
\[
S=\operatorname{diag}(u,B),\qquad H=u+v.
\]
All components \(E_{rr},E_{zz},E_{\rm orb}\) below are orthonormal components of
\[
E=\operatorname{Ric}_g+3g,
\qquad E_{\rm orb}=\operatorname{tr}_{T^2}E.
\]
Finally,
\[
d\mu=e^a\rho\,dz,\qquad
V=\int d\mu,\quad I=\int u\,d\mu,\quad J=\int v\,d\mu.
\]
Since \((d\mu)_r=H\,d\mu\), differentiation under the integral gives
\[
I'=\int(u_r+Hu)\,d\mu,\qquad
J'=\int(v_r+Hv)\,d\mu.
\]

## 2. Tangential evolution and the two slice balances

For a Gaussian foliation,
\[
\operatorname{Ric}_g|_{Tq}
=\operatorname{Ric}(q)-S_r-HS.
\]
Thus
\[
S_r+HS=\operatorname{Ric}(q)+3I-E_T.
\]

Taking the orbit trace and the horizontal \(z\)-component gives
\[
v_r+Hv=R_{\rm orb}^{q}+6-E_{\rm orb},
\]
\[
u_r+Hu=R_{zz}^{q}+3-E_{zz}.
\]

### Why \(\int R_{\rm orb}^{q}\,d\mu=0\)

Use physical arclength \(ds=e^a dz\) and set
\[
A=\frac12G^{-1}G_s,\qquad \theta=\operatorname{tr}A=\frac{\rho_s}{\rho}.
\]
For \(q=ds^2+G(s)\) with flat \(T^2\) orbits,
\[
R_{\rm orb}^{q}=-\theta_s-\theta^2
=-\rho^{-1}\partial_s(\rho\theta).
\]
Since \(d\mu=\rho\,ds\),
\[
\int R_{\rm orb}^{q}\,d\mu
=-\int\partial_s(\rho\theta)\,ds=0
\]
by periodicity. In the original coordinate this is
\[
R_{\rm orb}^{q}
=-e^{-a}\rho^{-1}\partial_z\!\left(\rho e^{-a}\sigma_z\right),
\qquad \sigma=\log\rho.
\]

Consequently,
\[
\boxed{J'=6V-\int E_{\rm orb}\,d\mu.}
\]

Since \(R(q)=R_{zz}^{q}+R_{\rm orb}^{q}\), the same vanishing identity yields
\[
\boxed{I'=3V+\int R(q)\,d\mu-\int E_{zz}\,d\mu.}
\]

These formulas extend from diagonal \(G\) to the full matrix-valued orbit metric. The SymPy residuals in `step82_slice_balance_verify.py` correctly reproduce the two total derivatives. Its periodic numerical test also gives
\[
I'_{\rm FD}-I'_{\rm direct}=-1.45\times10^{-12},\qquad
J'_{\rm FD}-J'_{\rm direct}=6.50\times10^{-12}.
\]

## 3. The Hamilton/Gauss term: \(E_{\rm orb}-E_{rr}\) is the exact defect

The contracted Gauss equation is
\[
R(q)=R(g)-2\operatorname{Ric}_g(\partial_r,\partial_r)
      +H^2-|S|^2.
\]
Because
\[
R(g)=\operatorname{tr}_gE-12,\qquad
\operatorname{Ric}_{rr}=E_{rr}-3,
\]
one obtains the exact identity
\[
R(q)
=-6+H^2-|S|^2+\operatorname{tr}_gE-2E_{rr}.
\]
Since
\[
\operatorname{tr}_gE=E_{rr}+E_{zz}+E_{\rm orb},
\]
this is
\[
\boxed{
R(q)=-6+H^2-|S|^2+E_{zz}+E_{\rm orb}-E_{rr}.
}
\]

Moreover,
\[
|S|^2=u^2+\operatorname{tr}(B^2)
=u^2+\frac12v^2+|B_0|^2,
\]
so
\[
H^2-|S|^2
=2uv+\frac12v^2-|B_0|^2.
\]
Substitution into the \(I'\) balance gives
\[
\boxed{
I'=\int\left[
-3+2uv+\frac12v^2-|B_0|^2
+E_{\rm orb}-E_{rr}
\right]d\mu.
}
\]

Thus the exact Ricci-defect combination is
\[
\boxed{E_{\rm orb}-E_{rr},}
\]
not \(2E_{rr}-E_{zz}\).

Indeed,
\[
(2E_{rr}-E_{zz})-(E_{\rm orb}-E_{rr})
=4E_{rr}-\operatorname{tr}_gE.
\]
The alternative formula would require the additional relation
\[
\operatorname{tr}_gE=4E_{rr},
\]
which does not follow from \(E=\operatorname{Ric}+3g\).

Equivalently, if
\[
F=(\operatorname{Ric}-\tfrac12Rg)-3g
=E-\tfrac12(\operatorname{tr}E)g
\]
is the Einstein-tensor defect, then the Hamilton relation is
\[
R(q)=-6+H^2-|S|^2-2F_{rr}.
\]
Mixing \(F_{rr}\) with the Ricci defect \(E_{rr}\) produces the erroneous \(+2E_{rr}\) expression.

### What the supplied numerical data actually show

In `step82_slice_balance.json`,
\[
I'_{\rm direct}=0.06513607870995486.
\]
The entry labeled `rhsTurnProposed_if_constraint`, which uses
\(E_{\rm orb}-E_{rr}\), is
\[
0.06513607870995765,
\]
agreeing to \(2.8\times10^{-15}\). The entry using \(2E_{rr}-E_{zz}\) is
\[
-0.2993294913539239.
\]
Their difference is
\[
0.3644655700638816,
\]
exactly the stored Hamilton residual. Symbolically that residual is
\[
\operatorname{tr}_gE-4E_{rr}.
\]

Therefore `step82_geometric_balance_check.py` does not derive its stated Hamilton relation: it inserts
\[
R(q)=-6+H^2-|S|^2+2E_{rr}
\]
as a formal substitution, after which its zero residual is tautological. The direct coordinate computation supports \(E_{\rm orb}-E_{rr}\).

## 4. First-return inequality

Define the slice average
\[
\langle f\rangle=\frac1V\int f\,d\mu,
\]
and
\[
\operatorname{Cov}(u,v)
=\langle uv\rangle-\langle u\rangle\langle v\rangle.
\]

Suppose \(r_*\) satisfies
\[
I(r_*)=0,\qquad I(r)<0
\quad\text{for }r\in(r_*-\varepsilon,r_*).
\]
Smoothness gives \(I\in C^1\), and
\[
I'(r_*)
=\lim_{h\downarrow0}
\frac{I(r_*)-I(r_*-h)}{h}\ge0.
\]
At \(r_*\),
\[
\langle u\rangle=\frac IV=0,
\qquad
\langle uv\rangle=\operatorname{Cov}(u,v).
\]
Hence
\[
0\le\frac{I'}V
=-3+2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle
+\langle E_{\rm orb}-E_{rr}\rangle.
\]

If \(\|E\|_{\rm op}\le\delta\) pointwise, then
\[
|E_{\rm orb}|\le2\delta,\qquad |E_{rr}|\le\delta,
\]
and therefore
\[
\langle E_{\rm orb}-E_{rr}\rangle\le3\delta.
\]
The necessary inequality is
\[
\boxed{
2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle
\ge 3-3\delta.
}
\]

Writing \(y=\langle v\rangle=J/V\),
\[
\langle v^2\rangle=y^2+\operatorname{Var}(v),
\]
so the left side is
\[
2\operatorname{Cov}(u,v)
+\frac12\operatorname{Var}(v)
+\frac12y^2
-\langle|B_0|^2\rangle.
\]
Mean orbit expansion, orbit-expansion variance, and positive \(u\)-\(v\) covariance assist reversal; radial orbit shear opposes it.

Both candidate defect expressions happen to have absolute value at most \(3\delta\), so the coarse threshold \(3-3\delta\) survives the mistaken Hamilton substitution. Refined identities and component-sensitive estimates do not.

## 5. Intrinsic orbit energy gives an equivalent return condition

Write
\[
G=\rho M,\qquad \det M=1,
\]
and let \(U\) denote the corresponding map into
\(SL(2,\mathbb R)/SO(2)\), with
\[
|U_s|^2=\frac12\operatorname{tr}\bigl((M^{-1}M_s)^2\bigr).
\]
The intrinsic scalar curvature is
\[
R(q)
=-2\theta_s-\frac32\theta^2-\frac12|U_s|^2.
\]
After integration,
\[
\boxed{
\langle R(q)\rangle
=\frac12\langle\theta^2-|U_s|^2\rangle.
}
\]

The direct \(I'\) balance therefore becomes
\[
\frac{I'}V
=3+\frac12\langle\theta^2-|U_s|^2\rangle
-\langle E_{zz}\rangle.
\]
At a return,
\[
\boxed{
\langle|U_s|^2-\theta^2\rangle
\le 6-2\langle E_{zz}\rangle
\le 6+2\delta.
}
\]

For an exact reflected center with \(R(q_0)=-6\),
\[
\langle|U_s|^2-\theta^2\rangle_{r=0}=12,
\qquad
I'(0)=-3V.
\]
An exact later return therefore requires this tangential energy difference to fall from \(12\) to at most \(6\). This is a sharp description of the required geometric transition, but it does not by itself prevent that transition.

## 6. Matrix equation, base constraints, and \(J/V\)

Let
\[
P_r=M^{-1}M_r,\qquad P_z=M^{-1}M_z.
\]
The full traceless orbit equation is
\[
\partial_r(e^a\rho P_r)
+\partial_z(e^{-a}\rho P_z)
=-2e^a\rho\,(E^\sharp_{\rm orb})_0.
\]
For \(E=0\),
\[
Q(r)=\int e^a\rho P_r\,dz
\]
is constant. Reflection gives \(P_r=0\) initially, hence \(Q=0\). A zero matrix average permits \(P_r=0\), as well as large oscillatory \(P_r\); it gives no \(L^2\) estimate for
\[
|B_0|^2=\frac14\operatorname{tr}(P_r^2).
\]

The mixed base equation can be written, with
\[
A_0=\frac12M^{-1}M_s-\frac{\theta}{2}I,
\]
as
\[
E_{rs}
=-v_s+u\theta-\frac12v\theta-\langle A_0,B_0\rangle.
\]
This is a differential relation in the \(z\)-direction without a definite sign. It does not provide an upper estimate for \(\operatorname{Cov}(u,v)\) or \(\operatorname{Var}(v)\).

For
\[
x=\frac IV=\langle u\rangle,\qquad y=\frac JV=\langle v\rangle,
\]
one has
\[
\frac{V'}V=x+y,
\]
\[
x'=3+\langle R(q)\rangle-\langle E_{zz}\rangle-x(x+y),
\]
\[
\boxed{
y'=6-\langle E_{\rm orb}\rangle-y(x+y).
}
\]
At a return \(x=0\),
\[
y'=6-\langle E_{\rm orb}\rangle-y^2.
\]
This controls only the mean \(y\). It does not control \(\operatorname{Var}(v)\), \(\operatorname{Cov}(u,v)\), or \(|B_0|^2\). If reflection gives \(J(0)=0\) and \(\delta<3\) throughout the preceding interval, then
\[
J'\ge(6-2\delta)V>0,
\]
so \(y>0\) at every later slice. This favors the \(y^2/2\) term rather than excluding reversal.

## 7. Algebraically favorable and fully compatible slices

The profile scan in `step82_turning_covariance_model.py` correctly shows moment-level compatibility. For example,
\[
u=2\cos z,\qquad v=2\cos z,\qquad B_0=0
\]
has
\[
2\operatorname{Cov}(u,v)+\frac12\langle v^2\rangle=5.
\]
That script does not construct \(q\), evaluate \(E\), or impose the Hamilton and mixed equations.

Its “homogeneous control” at \(v=\sqrt6\), \(u=B_0=0\), also satisfies only the integrated turning balance. A homogeneous slice has \(R(q)=0\), while the exact Hamilton equation would require
\[
\frac12v^2=6,
\]
hence \(v=\sqrt{12}\), not \(\sqrt6\).

There is nevertheless a fully compatible local exact Einstein reversal germ. Consider
\[
g=dr^2+e^{2a(r)}dz^2+e^{2b(r)}(dx^2+dy^2),
\]
and set
\[
u=a',\qquad p=b',\qquad v=2p.
\]
Every slice is intrinsically flat. The tangential Einstein equations are
\[
u'=3-u(u+2p),\qquad
p'=3-p(u+2p).
\]
Choose at \(r=0\)
\[
u(0)=0,\qquad p(0)=\sqrt3.
\]
Then
\[
H=2\sqrt3,\qquad |S|^2=6,\qquad
H^2-|S|^2=6,
\]
so the Hamilton equation holds, while the mixed equation is identically zero. The quantity
\[
C=H^2-(u^2+2p^2)
\]
satisfies
\[
C'=2H(6-C),
\]
so \(C=6\) is preserved and \(E_{rr}=0\). Thus the ODE produces a local metric with \(\operatorname{Ric}=-3g\).

At \(r=0\),
\[
B_0=0,\qquad v=2\sqrt3,\qquad
T=\frac12v^2=6,
\]
and
\[
I'=V(u'+Hu)=3V>0.
\]
Since \(u(r)=3r+O(r^2)\), one has \(I(r)<0\) for sufficiently small \(r<0\). Hence this is a genuine local exact reversal, not merely a free moment assignment.

It is not reflected at the return, since \(p(0)\ne0\), and it is not a connection from the prescribed reflected \(R=-6\) center. That specific reachability question requires an interval estimate tying the initial tangential energy \(12\) to covariance, variance, and accumulated radial shear. No such estimate is present in the supplied matrix-current, scalar-energy, mixed-base, or \(J/V\) identities.

## 8. Scientific conclusion

The two direct slice balances are correct. The exact Hamilton-rewritten formula is
\[
I'=\int\left[-3+2uv+\frac12v^2-|B_0|^2
+E_{\rm orb}-E_{rr}\right]d\mu.
\]
The first-return requirement under \(\|E\|_{\rm op}\le\delta\) is
\[
2\operatorname{Cov}(u,v)
+\frac12\langle v^2\rangle
-\langle|B_0|^2\rangle
\ge3-3\delta.
\]
Equivalently, the tangential orbit-energy difference must satisfy
\[
\langle|U_s|^2-\theta^2\rangle\le6+2\delta.
\]

The listed identities permit favorable slices, and even a local exact Einstein reversal germ. What remains unresolved for the reflected \(R=-6\) construction is global reachability: whether evolution from that center can reduce the tangential energy sufficiently without radial orbit shear or another coupled equation preventing the return.