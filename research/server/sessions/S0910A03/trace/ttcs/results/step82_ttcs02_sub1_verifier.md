# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step82_slice_balances_and_reversal_energy.md",
    "Sessions/S0910A03/workspace/scripts/step82_center_jet_invariants.py",
    "Sessions/S0910A03/workspace/data/step82_center_jet_invariants.json",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md"
  ]
}
```

## Task

Resolve a possible error in the proposed radial production law for K in the Step-82 note. Work in fixed periodic z coordinates with physical arclength derivative D_s=e^{-a}∂_z, measure dμ=e^aρ dz=ρ ds, σ=logρ, h=D_sσ, U:S^1→H^2, A=D_sU, b=∂_rU, e=|A|^2, k=e-h^2, K=<k>, u=a_r, v=σ_r, H=u+v, x=<u>, y=<v>. Use only target covariant derivatives, [∂_r,D_s]=-uD_s, and normalized moving averages. Independently derive K'. Check whether the exact kinematic identity is K'=-2<τ,b>+2<vc>+Cov(v-u,k)-2xK with τ=∇_sA+hA and c=h_s+h^2, or whether an additional explicit traceless-orbit defect term belongs while τ is retained. Then derive the Codazzi relation with E=Ric+3g and all normalization factors. For exact reflected scalar-minus-six center, verify u_r=-k/4, v_r=3+k/4, b_r=-τ (under the chosen target normalization), K'(0)=0, and K''(0)=72+2<|τ|^2>+(3/8)Var(k). State precisely how orbit defect enters if one substitutes the orbit evolution for τ, and flag double counting. Also check the x cubic coefficient. Ground the answer in the actual Step-82 files, but recompute rather than trusting the prior generator.

## Output

## Scientific memo: radial production of \(K\)

### 1. Moving-average and commutator calculation

All \(r\)-derivatives below are at fixed periodic \(z\). Since
\[
d\mu=\rho\,ds=e^a\rho\,dz,\qquad (d\mu)_r=H\,d\mu,
\]
the normalized average satisfies
\[
\frac{d}{dr}\langle f\rangle
=\langle f_r\rangle+\operatorname{Cov}(f,H),
\qquad H=u+v.
\tag{1.1}
\]

With
\[
A=D_sU,\qquad b=\partial_rU,
\]
torsion-freeness of the target connection and
\[
[\partial_r,D_s]=-uD_s
\]
give
\[
\nabla_rA=\nabla_sb-uA.
\tag{1.2}
\]
Hence
\[
e_r=2\langle A,\nabla_sb\rangle_{\mathbb H^2}-2ue.
\tag{1.3}
\]
Likewise,
\[
h_r=\partial_r(D_s\sigma)=D_sv-uh.
\tag{1.4}
\]
Therefore, for \(k=e-h^2\),
\[
k_r
=2\langle A,\nabla_sb\rangle_{\mathbb H^2}
-2hD_sv-2uk.
\tag{1.5}
\]

Periodicity and \(D_s\rho=h\rho\) imply
\[
\left\langle\langle A,\nabla_sb\rangle_{\mathbb H^2}\right\rangle
=-\langle\langle\nabla_sA+hA,b\rangle_{\mathbb H^2}\rangle
=-\langle\langle\tau,b\rangle_{\mathbb H^2}\rangle,
\tag{1.6}
\]
and
\[
\langle hD_sv\rangle=-\langle v(h_s+h^2)\rangle=-\langle vc\rangle.
\tag{1.7}
\]
Thus
\[
\langle k_r\rangle
=-2\langle\tau,b\rangle+2\langle vc\rangle-2\langle uk\rangle.
\tag{1.8}
\]
Using (1.1),
\[
\begin{aligned}
K'
&=-2\langle\tau,b\rangle+2\langle vc\rangle
-2\langle uk\rangle+\operatorname{Cov}(k,u+v)\\
&=\boxed{
-2\langle\tau,b\rangle
+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)-2xK}.
\end{aligned}
\tag{1.9}
\]

This is a purely kinematic identity. No Einstein equation and no defect tensor entered its derivation. Consequently, while the geometric tension
\[
\tau=\nabla_sA+hA
\]
is retained, there is **no additional explicit traceless-orbit defect term**. The final \(+2\langle\mathcal E_0,b\rangle\) in Step-82 equation (8.1) must therefore be omitted in that representation.

---

### 2. Orbit evolution and the precise defect convention

Write
\[
G=\rho M,\qquad \det M=1,
\]
and identify target vectors \(W\in T_U\mathbb H^2\) with traceless orbit endomorphisms
\[
L_W=\frac12M^{-1}dM(W).
\]
The Step-81/82 normalization is
\[
\langle W,Z\rangle_{\mathbb H^2}
=\frac12\operatorname{tr}\!\left((M^{-1}dM(W))(M^{-1}dM(Z))\right)
=2\operatorname{tr}(L_WL_Z).
\tag{2.1}
\]
In particular,
\[
B_0=L_b,\qquad C_0=L_A,\qquad
|b|^2=2|B_0|^2.
\tag{2.2}
\]

Let
\[
\mathsf E_0
=\left(E_{\rm orb}^{\sharp}\right)_0
\]
be the traceless part of the orbit endomorphism, and define the target vector
\[
\varepsilon=L^{-1}(\mathsf E_0).
\tag{2.3}
\]
The traceless orbit Ricci equation is then
\[
\boxed{\nabla_rb+Hb+\tau=-\varepsilon.}
\tag{2.4}
\]
Indeed, the intrinsic orbit Ricci traceless part is \(-L_\tau\), while the radial contribution is
\(-L_{\nabla_rb+Hb}\). Since the \(3g\) term has no traceless orbit part,
\[
\mathsf E_0=-L_{\nabla_rb+Hb+\tau}.
\]

If \(\tau\) is eliminated using (2.4), then
\[
-2\langle\tau,b\rangle
=\left\langle (|b|^2)_r\right\rangle
+2\langle H|b|^2\rangle
+2\langle\varepsilon,b\rangle.
\tag{2.5}
\]
The explicit defect contraction has normalization
\[
2\langle\varepsilon,b\rangle_{\mathbb H^2}
=4\operatorname{tr}(\mathsf E_0B_0).
\tag{2.6}
\]

If instead Step 82 defines its source by
\[
\nabla_rb+Hb+\tau=\mathcal E_0,
\]
then \(\mathcal E_0=-\varepsilon\), and eliminating \(\tau\) produces
\[
-2\langle\mathcal E_0,b\rangle,
\]
not \(+2\langle\mathcal E_0,b\rangle\).

Thus there are two equivalent forms:

* retain \(-2\langle\tau,b\rangle\), with no explicit orbit-defect term;
* eliminate \(\tau\), producing exactly one explicit defect contraction with the sign fixed by the chosen source convention.

Writing both \(-2\langle\tau,b\rangle\) and an extra orbit-defect contraction counts the same orbit equation twice.

---

### 3. Codazzi relation, including all factors

On a slice let
\[
C=\frac12G^{-1}D_sG=\frac h2I+C_0,
\qquad
B=\frac12G^{-1}G_r=\frac v2I+B_0.
\tag{3.1}
\]
For \(S=\frac12q^{-1}q_r\), its slice divergence in the \(D_s\) direction is
\[
(\operatorname{div}_qS)_s=D_su+hu-\operatorname{tr}(CB).
\tag{3.2}
\]
With the curvature convention already used in Step 82,
\[
\operatorname{Ric}_g(\partial_r,D_s)
=(\operatorname{div}_qS)_s-D_sH
=hu-\operatorname{tr}(CB)-D_sv.
\tag{3.3}
\]
Since \(g(\partial_r,D_s)=0\),
\[
E_{rs}=\operatorname{Ric}_{rs}.
\]
Moreover, by (2.1),
\[
\operatorname{tr}(CB)
=\frac{hv}{2}+\operatorname{tr}(C_0B_0)
=\frac{hv}{2}+\frac12\langle A,b\rangle_{\mathbb H^2}.
\tag{3.4}
\]
Consequently,
\[
\boxed{
D_sv
=h\left(u-\frac v2\right)
-\frac12\langle A,b\rangle_{\mathbb H^2}
-E_{rs}.}
\tag{3.5}
\]

This verifies both the minus sign on \(E_{rs}\) and the factor \(1/2\) in the target contraction.

Equation (3.5) also gives an alternative representation of the \(2\langle vc\rangle\) term:
\[
\boxed{
2\langle vc\rangle
=-2\langle h^2u\rangle+\langle h^2v\rangle
+\langle h\langle A,b\rangle_{\mathbb H^2}\rangle
+2\langle hE_{rs}\rangle.}
\tag{3.6}
\]
Thus \(E_{rs}\) appears only if \(2\langle vc\rangle\) is replaced by its Codazzi form; it is not added alongside both forms.

---

### 4. Reflected scalar-minus-six center

At a reflected center,
\[
u=v=b=H=0.
\tag{4.1}
\]
For the intrinsic slice metric \(q=ds^2+G\),
\[
R^q_{ss}=-h_s-\frac12(h^2+e),
\qquad
R^q_{\rm orb}=-h_s-h^2=-c,
\tag{4.2}
\]
and hence
\[
R(q)=-2h_s-\frac32h^2-\frac12e
=-2c-\frac12k.
\tag{4.3}
\]
The condition \(R(q)=-6\) gives the pointwise relation
\[
\boxed{4c+k=12,\qquad c=\frac{12-k}{4}.}
\tag{4.4}
\]
Weighted periodic integration gives
\[
\langle c\rangle
=\langle h_s+h^2\rangle=0,
\qquad K(0)=\langle k\rangle=12.
\tag{4.5}
\]

At an exact Einstein center, the Gaussian tangential equations yield
\[
u_r=R^q_{ss}+3,\qquad
v_r=R^q_{\rm orb}+6.
\]
Using (4.2)–(4.4),
\[
\boxed{
u_r=-\frac{k}{4},\qquad
v_r=3+\frac{k}{4}.}
\tag{4.6}
\]
Equation (2.4), with \(E(0)=0\), gives
\[
\boxed{\nabla_rb=-\tau.}
\tag{4.7}
\]
Since \(b=0\) at the center, this is also the coordinate statement \(b_r=-\tau\) in any target chart.

Substituting (4.1) into (1.9) immediately gives
\[
\boxed{K'(0)=0.}
\tag{4.8}
\]

---

### 5. Second derivative of \(K\)

Differentiate the four terms of (1.9) at \(r=0\). Moving-measure terms vanish there because \(H=0\).

First,
\[
\left[-2\langle\tau,b\rangle\right]'_{r=0}
=2\langle|\tau|^2\rangle.
\tag{5.1}
\]
Next, using \(v_r=3+k/4\) and \(c=(12-k)/4\),
\[
\left[2\langle vc\rangle\right]'_{r=0}
=2\left\langle
\left(3+\frac k4\right)\frac{12-k}{4}
\right\rangle
=18-\frac18\langle k^2\rangle.
\tag{5.2}
\]
Since
\[
(v-u)_r=3+\frac k2,
\]
\[
\left[\operatorname{Cov}(v-u,k)\right]'_{r=0}
=\frac12\operatorname{Var}(k).
\tag{5.3}
\]
Finally,
\[
x'(0)=\langle u_r\rangle=-3,
\]
so
\[
[-2xK]'_{r=0}=72.
\tag{5.4}
\]
Adding these contributions,
\[
\begin{aligned}
K''(0)
&=2\langle|\tau|^2\rangle
+18-\frac18\langle k^2\rangle
+\frac12\operatorname{Var}(k)+72\\
&=\boxed{
72+2\langle|\tau|^2\rangle
+\frac38\operatorname{Var}(k)}.
\end{aligned}
\tag{5.5}
\]
Equivalently,
\[
K''(0)=18+2\langle|\tau|^2\rangle+\frac38\langle k^2\rangle.
\]

This reproduces the algebra recorded in
`step82_center_jet_invariants.py` and
`step82_center_jet_invariants.json`; the derivation above supplies the geometric inputs that the script explicitly treated as assumptions.

---

### 6. Cubic coefficient of \(x\)

For an exact Einstein germ,
\[
x'=3-\frac12K-x(x+y).
\tag{6.1}
\]
Reflection gives
\[
K=12+\frac12K''(0)r^2+O(r^4),
\quad
x=-3r+Ar^3+O(r^5),
\quad
y=6r+O(r^3).
\]
Since
\[
x(x+y)=-9r^2+O(r^4),
\]
comparison of the \(r^2\) coefficients in (6.1) yields
\[
\boxed{A=3-\frac1{12}K''(0).}
\tag{6.2}
\]
Thus
\[
\boxed{
x(r)=-3r-
\left(
3+\frac16\langle|\tau|^2\rangle
+\frac1{32}\operatorname{Var}(k)
\right)r^3+O(r^5).}
\tag{6.3}
\]
The generic script output `3 - K2/12` is therefore correct.

The cubic formula uses an exact Einstein germ, so \(\langle E_{zz}\rangle\equiv0\) near the center. If only \(E(0)=0\) is imposed, the \(r^2\) coefficient of \(\langle E_{zz}\rangle\) also contributes to \(A\).

### Final resolution

The kinematic production law in Step 82 is
\[
\boxed{
K'=-2\langle\tau,b\rangle+2\langle vc\rangle
+\operatorname{Cov}(v-u,k)-2xK.}
\]
The explicit traceless-orbit defect term in the displayed Step-82 equation (8.1) does not belong while \(\tau\) remains present. It appears exactly once only after the orbit equation is used to eliminate \(\tau\), with its sign determined by whether the source is denoted by \(\varepsilon=L^{-1}(E_{\rm orb}^{\sharp})_0\) or by the right-hand side \(\mathcal E_0=-\varepsilon\).