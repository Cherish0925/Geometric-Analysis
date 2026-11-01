# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/scripts/step76_center_energy_flux_verify.py",
    "Sessions/S0910A03/workspace/data/step76_center_energy_flux.json"
  ]
}
```

## Task

For the Yau-26 negative graph-manifold route, verify and sharpen the new center-energy/transport synthesis from first principles. In the diagonal orthogonally-transitive class, derive with correct physical measures: (i) the periodic center identity for q=ds^2+G(s), rho=sqrt(det G), h=rho'/rho, A0=A-(h/2)I, including the approximate scalar error e=R_q+6; (ii) the diagonal d=b-c specialization and its normalization under lattice quotients; (iii) the invariant exact and forced equations div_gamma(rho grad d)=-rho(E_x-E_y), total signed flux, boundary covariance pairing with arbitrary constant c, and all signs; (iv) the slice evolution F'(r) in Gaussian distance; and (v) for one Fourier mode on an expanding flat-cusp background, the reflection-normalized solution, asymptotic derivative, weighted pairing, and normalized decay. State exactly whether these identities imply a positive Ricci-defect cost or instead exhibit a feasible energy-dilution mechanism, and identify assumptions needed for either conclusion.

## Output

# Scientific memo: center energy and anisotropy transport

The center formulas recorded in `step76_center_energy_flux_verify.py` and its JSON output are algebraically correct. The main refinement is to insert the physical orbit density, slice line element, lattice covolume, and the forcing term consistently. With those factors included, the identities support energy dilution on an expanding end; by themselves they do not produce a dimension-only positive lower bound for \(\|\operatorname{Ric}+3g\|_{\mathrm{op}}\).

## 1. Periodic center identity

Let

\[
q=ds^2+G(s)_{ab}\,dx^a dx^b,\qquad s\in\mathbb R/L\mathbb Z,
\]

where \(G(s)\) is positive definite and periodic. Define

\[
\rho=\sqrt{\det G},\qquad
A=\frac12G^{-1}G',\qquad
h=\operatorname{tr}A=\frac{\rho'}{\rho},
\qquad
A_0=A-\frac h2I.
\]

Here \(A\) is self-adjoint with respect to \(G\), and

\[
|A|^2=\operatorname{tr}(A^2)
      =|A_0|^2+\frac12h^2.
\]

The \(T^2\) orbit metric is intrinsically flat. With the convention
\(A=\frac12G^{-1}G'\), the scalar Gauss formula is

\[
R_q=-2h'-|A|^2-h^2
    =-2h'-|A_0|^2-\frac32h^2.
\tag{1}
\]

Writing

\[
e=R_q+6,\qquad R_q=-6+e,
\]

multiply (1) by \(\rho\) and integrate over one \(s\)-period. Since
\(\rho'=\rho h\),

\[
\int_0^L\rho h'\,ds
=[\rho h]_0^L-\int_0^L\rho h^2\,ds
=-\int_0^L\rho h^2\,ds.
\]

Consequently,

\[
\boxed{
\int_0^L\rho |A_0|^2\,ds
=
6\int_0^L\rho\,ds
+\frac12\int_0^L\rho h^2\,ds
-\int_0^L\rho e\,ds.
}
\tag{2}
\]

In weighted-average notation,

\[
\langle f\rangle_\rho
=\frac{\int_0^L\rho f\,ds}{\int_0^L\rho\,ds},
\]

this is

\[
\boxed{
\langle |A_0|^2\rangle_\rho
=6+\frac12\langle h^2\rangle_\rho-\langle e\rangle_\rho.
}
\tag{3}
\]

### Relation to the ambient Ricci defect

Suppose this slice is a totally geodesic reflection face of

\[
g=dr^2+q_r,\qquad E=\operatorname{Ric}_g+3g.
\]

At \(r=0\), \(S=0\). The scalar Gauss identity gives

\[
R_q=R_g-2\operatorname{Ric}_g(n,n)
=-6+\operatorname{tr}_{Tq}E-E_{nn}.
\]

Thus

\[
e=\operatorname{tr}_{Tq}E-E_{nn}.
\tag{4}
\]

If \(\lVert E\rVert_{\mathrm{op}}\le\delta\), then

\[
|e|\le4\delta.
\tag{5}
\]

This is the precise source of the \(4\delta\) factor in the supplied JSON file.

---

## 2. Diagonal specialization and lattice normalization

For

\[
G=\begin{pmatrix}e^{2b}&0\\0&e^{2c}\end{pmatrix},
\qquad
d=b-c,\qquad \sigma=b+c,
\]

one has

\[
\rho=e^\sigma,\qquad
A=\operatorname{diag}(b_s,c_s),\qquad
h=b_s+c_s,
\]

and

\[
A_0=\frac12
\begin{pmatrix}
d_s&0\\0&-d_s
\end{pmatrix},
\qquad
|A_0|^2=\frac12d_s^2.
\]

Equation (2) becomes

\[
\boxed{
\int_0^L\rho d_s^2\,ds
=
12\int_0^L\rho\,ds
+\int_0^L\rho h^2\,ds
-2\int_0^L\rho e\,ds.
}
\tag{6}
\]

Hence

\[
\boxed{
\langle d_s^2\rangle_\rho
=
12+\langle h^2\rangle_\rho-2\langle e\rangle_\rho.
}
\tag{7}
\]

For \(e=0\),

\[
\langle d_s^2\rangle_\rho\ge12.
\tag{8}
\]

Under (5),

\[
\boxed{
\langle d_s^2\rangle_\rho\ge12-8\delta.
}
\tag{9}
\]

Let \(\Lambda\subset\mathbb R^2\) be the orbit lattice and
\(\mathcal A_\Lambda\) its coordinate covolume. Then

\[
d\mu_q=\mathcal A_\Lambda\,\rho(s)\,ds,
\qquad
\operatorname{Vol}(q)
=\mathcal A_\Lambda\int_0^L\rho\,ds.
\]

Both sides of (6) acquire the same factor \(\mathcal A_\Lambda\). Thus (7)–(9) are unchanged by passage to finite lattice quotients. Likewise, replacing both orbit scales by \(N^{-1}\) multiplies \(\rho\), every energy integral, and the volume by \(N^{-2}\), but leaves normalized energy unchanged. Anisotropic constant rescaling shifts \(d\) by a constant and therefore leaves \(d_s\) unchanged.

Thus lattice collapse does not reduce the intensive center energy.

---

## 3. Invariant anisotropy equation, signed flux, and face pairing

Consider the diagonal orthogonally-transitive metric

\[
g=\gamma_{ij}(y)\,dy^i dy^j
  +e^{2b(y)}dx^2+e^{2c(y)}dy_2^2
\]

over a two-dimensional base \((B,\gamma)\). Put

\[
d=b-c,\qquad \sigma=b+c,\qquad \rho=e^\sigma.
\]

The orthonormal orbit Ricci components are

\[
\operatorname{Ric}_x
=-\bigl(\Delta_\gamma b+\langle db,d\sigma\rangle_\gamma\bigr),
\]

\[
\operatorname{Ric}_y
=-\bigl(\Delta_\gamma c+\langle dc,d\sigma\rangle_\gamma\bigr).
\]

Therefore

\[
\operatorname{Ric}_x-\operatorname{Ric}_y
=-\Delta_\gamma d-\langle d\sigma,dd\rangle_\gamma
=-\rho^{-1}\operatorname{div}_\gamma(\rho\nabla_\gamma d).
\]

Since the \(+3g\) terms cancel in the difference, with

\[
X=E_x-E_y,
\]

the exact forced equation is

\[
\boxed{
\operatorname{div}_\gamma(\rho\nabla_\gamma d)
=-\rho X.
}
\tag{10}
\]

The sign in (10) is therefore fixed.

Let \(\Omega=[r_0,r_1]\times S^1\), with \(r\) increasing toward the outer face, and define the physical signed flux

\[
Q(r)=\mathcal A_\Lambda
\int_{C_r}\rho\,d_r\,d\ell_r.
\tag{11}
\]

Integration of (10) gives

\[
\boxed{
Q(r_1)-Q(r_0)
=
-\mathcal A_\Lambda\int_\Omega\rho X\,d\mu_\gamma.
}
\tag{12}
\]

For an exact \(\operatorname{Ric}=-3g\) metric, \(X=0\), so \(Q\) is constant. Reflection gives \(d_r(r_0)=0\), hence

\[
Q(r)=0
\tag{13}
\]

on every slice.

For any fixed constant \(c_0\), define

\[
F_{c_0}(r)=\mathcal A_\Lambda
\int_{C_r}(d-c_0)\rho d_r\,d\ell_r.
\tag{14}
\]

Multiplication of (10) by \(d-c_0\) and integration by parts yields

\[
\boxed{
F_{c_0}(r_1)-F_{c_0}(r_0)
=
\mathcal A_\Lambda\int_\Omega\rho|\nabla_\gamma d|^2\,d\mu_\gamma
-\mathcal A_\Lambda\int_\Omega(d-c_0)\rho X\,d\mu_\gamma.
}
\tag{15}
\]

Equivalently,

\[
\mathcal A_\Lambda\int_\Omega\rho|\nabla d|^2
=
F_{c_0}(r_1)-F_{c_0}(r_0)
+\mathcal A_\Lambda\int_\Omega(d-c_0)\rho X.
\tag{16}
\]

For the exact reflected problem,

\[
\boxed{
F_{c_0}(r_1)
=
\mathcal A_\Lambda\int_\Omega\rho|\nabla d|^2.
}
\tag{17}
\]

Because \(Q=0\), (17) is independent of \(c_0\). This is precisely the weighted covariance property: the signed measure
\(\rho d_r\,d\ell_r\) has total mass zero, but its pairing with the varying function \(d\) can be large.

For the forced problem, changing \(c_0\) changes \(F_{c_0}\) whenever \(Q\ne0\). The combination appearing on the right of (16) remains independent of \(c_0\), as required by (12).

---

## 4. Slice evolution in Gaussian distance

Write the base metric as

\[
\gamma=dr^2+\alpha(r,z)^2dz^2,
\qquad
d\ell_r=\alpha\,dz.
\]

Equation (10) is

\[
\partial_r(\alpha\rho d_r)
+\partial_z(\rho\alpha^{-1}d_z)
=-\alpha\rho X.
\tag{18}
\]

Consequently,

\[
Q'(r)
=-\mathcal A_\Lambda\int_{C_r}\rho X\,d\ell_r,
\tag{19}
\]

and direct differentiation of (14), followed by periodic integration in \(z\), gives

\[
\boxed{
F_{c_0}'(r)
=
\mathcal A_\Lambda\int_{C_r}
\rho\left(
d_r^2+|\nabla_{C_r}d|^2-(d-c_0)X
\right)d\ell_r.
}
\tag{20}
\]

No extra mean-curvature term appears: it is already contained in the derivative of the physical density \(\alpha\rho\).

For an exact metric,

\[
\boxed{
F_{c_0}'(r)=N(r)+Z(r),
}
\tag{21}
\]

where

\[
N(r)=\mathcal A_\Lambda\int_{C_r}\rho d_r^2\,d\ell_r,
\qquad
Z(r)=\mathcal A_\Lambda\int_{C_r}
\rho|\nabla_{C_r}d|^2\,d\ell_r,
\]

and \(N,Z\ge0\).

At a reflection face, \(d_r(0)=0\), so \(F(0)=0\). At the center, physical arclength is \(ds=d\ell_0\), and therefore

\[
F'(0)
=\mathcal A_\Lambda\int\rho d_s^2\,ds.
\]

Combining this with (6),

\[
\boxed{
F'(0)
=
12V_0
+\mathcal A_\Lambda\int\rho h^2\,ds
-2\mathcal A_\Lambda\int\rho e\,ds
}
\tag{22}
\]

for the exact anisotropy equation, where
\(V_0=\mathcal A_\Lambda\int\rho ds\). In particular, when \(e=0\),

\[
F'(0)\ge12V_0.
\tag{23}
\]

For the forced equation,

\[
F_{c_0}'(0)
=
12V_0+\int\rho h^2-2\int\rho e
-\int\rho(d-c_0)X,
\tag{24}
\]

with all three integrals carrying \(\mathcal A_\Lambda ds\). Although
\(|X|\le2\delta\), the final term is not controlled by \(\delta\) alone:

\[
\left|\int\rho(d-c_0)X\right|
\le2\delta\int\rho|d-c_0|.
\tag{25}
\]

A uniform oscillation or Poincaré estimate is required to turn (25) into a geometry-independent estimate.

Also, the pointwise value \(F'(0)\ge12V_0\) does not by itself provide a fixed-thickness collar on which comparable energy persists. Such a statement needs uniform radial regularity, ellipticity, and volume comparison.

---

## 5. One Fourier mode on an expanding flat cusp

Consider

\[
g_d=dt^2+e^{2t}dz^2
+\ell_x^2e^{2t+d}dx^2
+\ell_y^2e^{2t-d}dy^2.
\tag{26}
\]

Here

\[
\gamma=dt^2+e^{2t}dz^2,\qquad
\rho=\ell_x\ell_y e^{2t}.
\]

The homogeneous anisotropy equation becomes

\[
\partial_t(e^{3t}d_t)+\partial_z(e^t d_z)=0.
\tag{27}
\]

For

\[
d(t,z)=A\psi_k(t)\cos(kz),
\qquad k>0,
\]

it reduces to

\[
\psi_k''+3\psi_k'-k^2e^{-2t}\psi_k=0.
\tag{28}
\]

With

\[
\psi_k(0)=1,\qquad \psi_k'(0)=0,
\]

set \(x=ke^{-t}\). The exact solution is

\[
\boxed{
\psi_k(t)=
\frac{e^{x-k}(x-1)+e^{k-x}(x+1)}{2k}.
}
\tag{29}
\]

Its exact derivative is

\[
\boxed{
\psi_k'(t)=\frac{x^2}{k}\sinh(k-x).
}
\tag{30}
\]

Thus

\[
\lim_{t\to\infty}\psi_k(t)=\frac{\sinh k}{k},
\tag{31}
\]

and, for fixed \(k\),

\[
\psi_k'(t)
=
k\sinh k\,e^{-2t}
-k^2\cosh k\,e^{-3t}
+O_k(e^{-4t}).
\tag{32}
\]

In particular,

\[
\boxed{
e^{2t}\psi_k'(t)\longrightarrow k\sinh k.
}
\tag{33}
\]

This is not uniform in frequency: \(\sinh k/k\) and \(k\sinh k\) grow exponentially in \(k\).

Let the \(z\)-period be \(L\), with
\(\int_0^L\cos^2(kz)\,dz=L/2\), and put

\[
V_0=\mathcal A_\Lambda\ell_x\ell_y L,
\qquad
V(t)=V_0e^{3t}.
\]

The total signed flux vanishes because \(\int\cos(kz)\,dz=0\). Nevertheless the covariance pairing is

\[
\boxed{
F(t)=\frac{A^2V_0}{2}e^{3t}\psi_k(t)\psi_k'(t).
}
\tag{34}
\]

The ODE gives

\[
\boxed{
F'(t)=\frac{A^2V_0}{2}
\left(e^{3t}\psi_k'^2+k^2e^t\psi_k^2\right),
}
\tag{35}
\]

and hence

\[
F(t)=\frac{A^2V_0}{2}
\int_0^t
\left(e^{3u}\psi_k'^2+k^2e^u\psi_k^2\right)du.
\tag{36}
\]

As \(t\to\infty\),

\[
\boxed{
F(t)\sim
\frac{A^2V_0}{2}\sinh^2(k)\,e^t.
}
\tag{37}
\]

Thus the total weighted pairing grows even though the pointwise normal derivative tends to zero. Dividing by physical slice volume gives

\[
\boxed{
\frac{F(t)}{V(t)}
=\frac{A^2}{2}\psi_k\psi_k'
\sim
\frac{A^2}{2}\sinh^2(k)e^{-2t},
}
\tag{38}
\]

and

\[
\boxed{
\frac{F'(t)}{V(t)}
=
\frac{A^2}{2}
\left(\psi_k'^2+k^2e^{-2t}\psi_k^2\right)
\sim
\frac{A^2}{2}\sinh^2(k)e^{-2t}.
}
\tag{39}
\]

The two intensive gradient energies are

\[
\frac1{V(t)}\int d_t^2
=\frac{A^2}{2}\psi_k'^2
\sim\frac{A^2k^2\sinh^2k}{2}e^{-4t},
\tag{40}
\]

\[
\frac1{V(t)}\int|\nabla_{C_t}d|^2
=\frac{A^2k^2}{2}e^{-2t}\psi_k^2
\sim\frac{A^2\sinh^2k}{2}e^{-2t}.
\tag{41}
\]

For the metric (26), equation (28) sets \(E_x=E_y=0\), while the remaining base block is

\[
E|_\gamma=-\frac12\,dd\otimes dd.
\tag{42}
\]

Hence, for fixed \(k\),

\[
\|E\|_{\mathrm{op},\infty}
=
\frac{A^2}{2}
\max\{\psi_k'^2,k^2e^{-2t}\psi_k^2\}
\sim
\frac{A^2}{2}\sinh^2(k)e^{-2t}.
\tag{43}
\]

The Neumann condition in (29) reflects only the anisotropy field. At \(t=0\), the full shape operator of (26) is \(S=I\), not \(S=0\), and its initial slice does not generally satisfy \(R_q=-6\). Thus this Fourier mode is an exact transport model for the expanding region, not a reflected Einstein core.

For varying frequencies \(k_j\), normalized dilution at exits \(t=R_j\) requires at least

\[
A_j e^{-R_j}\sinh k_j\longrightarrow0.
\tag{44}
\]

Small normal derivative alone requires the weaker expression

\[
A_j k_j e^{-2R_j}\sinh k_j\longrightarrow0.
\tag{45}
\]

Therefore fixed-frequency calculations do not supply a frequency-uniform inverse.

---

## 6. Scientific consequence for the graph construction

These identities establish three distinct facts.

1. **Order-one center energy.**  
   A scalar-\(-6\) reflected center in the \(T^2\)-cohomogeneity-one class satisfies the lattice-invariant density floor

   \[
   \langle d_s^2\rangle_\rho\ge12.
   \]

2. **No finite exactly umbilic exit for nonconstant \(d\).**  
   In the exact equation, reflection gives \(Q=0\), while

   \[
   F(R)=\int_\Omega\rho|\nabla d|^2.
   \]

   If \(d_r(R)\equiv0\), then \(F(R)=0\), forcing \(d\) to be constant.

3. **Small exit derivative remains compatible with large transported energy.**  
   The Fourier solution has \(d_t=O(e^{-2t})\), while the physical area grows as \(e^{3t}\) and the total covariance grows as \(e^t\). Its intensive pairing and energy density decay as \(e^{-2t}\). Thus no dimension-only positive Ricci-defect cost follows from center energy and flux conservation alone.

A quantitative positive defect lower bound would require additional geometry-independent estimates. For example, if one had

\[
\int_\Omega\rho|\nabla d|^2\ge \varepsilon_*V_0,
\qquad
|F(R)|\le\eta V_0,
\qquad
\int_\Omega\rho|d-c_0|\le B_0V_0,
\]

then (16) and \(|X|\le2\delta\) would give

\[
\delta\ge\frac{\varepsilon_*-\eta}{2B_0}.
\tag{46}
\]

Producing uniform \(\varepsilon_*,\eta,B_0\) requires, in concrete terms:

- a fixed physical collar on which the center tangential energy persists;
- radial derivative and ellipticity control for \(q_r\);
- uniform slice-volume growth and trace constants;
- a Poincaré or oscillation estimate for \(d-c_0\);
- control of exit area together with exit \(d_r\);
- frequency or Sobolev control strong enough to suppress the \(\sinh k\) amplification;
- estimates for every component of \(E\), not only \(E_x-E_y\).

The expanding cusp violates the volume-growth premise deliberately. It therefore supplies a mathematically explicit energy-dilution mechanism: finite exits retain a nonzero anisotropy derivative somewhere, total signed flux remains zero, and the covariance pairing carries the energy over an increasingly large slice while all intensive quantities decay. What remains unresolved is the reflected center-to-expansion connector satisfying the full Ricci system with small operator defect throughout.