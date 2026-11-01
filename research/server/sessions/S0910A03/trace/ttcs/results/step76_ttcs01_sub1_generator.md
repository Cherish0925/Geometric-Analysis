# TTCS Independent Branch Record

```json
{
  "step_id": 76,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/notes/step70_mixed_boundary_formulation.md",
    "Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md"
  ]
}
```

## Task

Develop a mathematically serious next route for the unresolved reflection-core entry problem in the negative branch of Yau 26, using the integrated center anisotropy floor, exact boundary-pairing transport, the expanding-tail lemma, and the actual Li-Liu PE+cusp constructions. Explore both directions: a parameter-dependent exact or small-defect core that converts the scalar-minus-six reflected center into a nonflat expanding PE-type end, and a global inequality that would forbid this. Derive concrete equations or monotone quantities rather than broad suggestions. Pay particular attention to CMC/volume gauge evolution P'+3a'P=e^{-2a}Ric(q)^circ, constraint propagation, Fourier-mode amplification, lattice quotient scaling, and whether Li-Liu's metrics or their Toda boundary problems supply a nearby mechanism despite lacking a totally geodesic torus. Identify one or two distinguishing mathematical calculations that would genuinely decide whether the core-tail construction is viable.

## Output

A serious formulation is to replace the finite cylinder picture by an **AHE half-core problem** and then regard the finite core as a truncation.  The reflected center is at \(r=0\); the desired outer regime is a PE-type expanding end with nonflat conformal infinity and small tracefree shape.  The adiabatic tail can then flatten that nonflat infinity at small Ricci cost.

## 1. CMC/volume gauge equations: the right dynamical variables

Write, in physical Gaussian distance,
\[
g=dr^2+e^{2a(r)}q_r,\qquad a'=\alpha,
\]
with \(q_r\) in pointwise volume gauge,
\[
q_r'=2q_rP,\qquad \operatorname{tr}_{q_r}P=0,
\]
so that the shape operator is
\[
S=\alpha I+P,\qquad H=3\alpha .
\]

For
\[
E=\operatorname{Ric}_g+3g,
\]
the exact equations become
\[
\boxed{\alpha'=1-\alpha^2-\frac13|P|^2-\frac13E_{rr}}
\tag{1}
\]
and
\[
\boxed{P'+3\alpha P=e^{-2a}\operatorname{Ric}(q_r)^\circ-E_T^\circ .}
\tag{2}
\]
The constraints are
\[
\boxed{
e^{-2a}R(q_r)+6(1-\alpha^2)+|P|^2=\operatorname{tr}_T E-E_{rr},
}
\tag{3}
\]
\[
\boxed{\operatorname{div}_{q_r}P=E_{r\cdot}.}
\tag{4}
\]

The essential transport identity is obtained by multiplying (2) by \(e^{3a}\):
\[
\boxed{
(e^{3a}P)'=e^a\operatorname{Ric}(q_r)^\circ-e^{3a}E_T^\circ .
}
\tag{5}
\]
Thus, in an exact region,
\[
P(R)=e^{-3a(R)}
\int_0^R e^{a(s)}\operatorname{Ric}(q_s)^\circ\,ds .
\tag{6}
\]
Once \(a(s)\sim s\), a uniformly controlled intrinsic tracefree Ricci source produces
\[
P(R)=O(e^{-2R}),
\]
not \(O(1)\).  This is the main mechanism by which an order-one center impulse can become small shape error at the outer face.

The normal balance is equally rigid:
\[
\boxed{
e^{2R}\bigl(3-H(R)\bigr)
=
3+\int_0^R e^{2r}\bigl(|S-I|^2+E_{rr}\bigr)\,dr .
}
\tag{7}
\]
So small \(3-H(R)\) requires \(R\to\infty\), but the identity itself allows this.

For the reflected center,
\[
\alpha(0)=0,\qquad P(0)=0,\qquad R(q_0)=-6e^{2a(0)}.
\]
In the \(T^2\)-cohomogeneity-one center class
\[
q_0=ds^2+G(s)_{ab}dx^a dx^b,
\]
with
\[
A=\frac12G^{-1}G',\qquad h=\operatorname{tr}A,
\]
the scalar equation
\[
R(q_0)=-2h'-|A|^2-h^2=-6
\]
gives the integrated floor
\[
\boxed{
\int_{S^1}\left(|A^\circ|^2+\frac32h^2\right)\,ds=6\,\operatorname{Length}(S^1).
}
\tag{8}
\]
At some orbit plane,
\[
K_{\rm orb}\ge 3,
\]
hence for the center acceleration
\[
P'(0)=\operatorname{Ric}(q_0)^\circ
\]
one principal direction has acceleration at most \(-3\) after the trace contribution is restored.  This is an initial impulse; equations (5)–(7) show how it could still be redshifted into a small outer shear.

Constraint propagation in this gauge has the expected homogeneous structure.  For the exact evolution system, if
\[
C=e^{-2a}R(q)+6(1-\alpha^2)+|P|^2,\qquad M=\operatorname{div}_{q}P,
\]
then a direct variation of scalar curvature under \(q'=2qP\) gives
\[
\boxed{
C'=-2\alpha C+2e^{-2a}\operatorname{div}_{q}M,
}
\tag{9}
\]
and the momentum equation has the schematic exact form
\[
\boxed{
M'=-3\alpha M+\frac12\,dC+\mathcal B(q,P)M .
}
\tag{10}
\]
Thus a construction that enforces (1)–(2) while keeping (3)–(4) on one slice propagates the constraints; a small-defect construction must measure all four equations, not only the tangential tracefree evolution.

---

## 2. PE-type expanding end and Li–Liu as the outer model

A complete reflected half-core would have an asymptotically hyperbolic expansion
\[
g=dr^2+e^{2r}
\left(
\gamma+e^{-2r}\gamma_{(2)}
+e^{-3r}\gamma_{(3)}
+O(e^{-4r})
\right),
\tag{11}
\]
where
\[
\gamma_{(2)}=-\operatorname{Sch}_\gamma,\qquad
\operatorname{tr}_\gamma\gamma_{(3)}=0,\qquad
\operatorname{div}_\gamma\gamma_{(3)}=0 .
\]
Consequently
\[
S-I
=
-e^{-2r}\gamma_{(2)}^\sharp
-\frac32e^{-3r}\gamma_{(3)}^\sharp
+O(e^{-4r}),
\]
so
\[
\boxed{
(S-I)^\circ
=
e^{-2r}\operatorname{Sch}_\gamma^\circ
-\frac32e^{-3r}\gamma_{(3)}^\sharp
+O(e^{-4r}).
}
\tag{12}
\]
This is exactly the desired entry behavior:
\[
\|S-I\|\to0,\qquad e^{-2r}\|\operatorname{Ric}(\gamma)\|\to0,
\]
while the weighted shear
\[
e^{2r}(S-I)^\circ\to \operatorname{Sch}_\gamma^\circ
\tag{13}
\]
may remain nonzero.  That nonzero weighted trace is the geometric carrier of the center anisotropy.

Li–Liu’s Type I construction supplies exact Ric\(=-3g\) metrics on
\[
(0,\infty)_\xi\times T^3
\]
with one PE end and one AH cusp.  In the trivial bundle case,
\[
h=\xi^{-2}\left(W\,d\xi^2+W^{-1}\eta^2+W e^v g_{T^2}\right),
\qquad
W=1-\frac12\xi v_\xi,
\tag{14}
\]
where
\[
(e^v)_{\xi\xi}+\Delta_{T^2}v=0.
\tag{15}
\]
For quotient-compatible symmetry one can take \(v=v(\xi,z)\).  Writing \(u=e^v\), the equation is
\[
u_{\xi\xi}+(\log u)_{zz}=0,
\tag{16}
\]
not a linear Laplace equation for \(u\).  Li–Liu prove the relevant Dirichlet trace problem and exponential convergence to the model end.  Near \(\xi=0\), after \(r=-\log\xi\), the metric has the PE expansion (11).  Hence their metrics provide exact nonflat expanding PE-type outer data with
\[
E=0,\qquad S-I=O(e^{-2r}),\qquad e^{-2r}\operatorname{Ric}(q_r)=O(e^{-2r}).
\]

They do not directly provide the reflected center.  Indeed, for a \(\xi\)-level face, the unit normal is
\[
n=\xi W^{-1/2}\partial_\xi,
\]
and the principal curvatures in the circle-fiber direction and the two quotient directions are
\[
\kappa_\eta
=
-W^{-1/2}-\frac{\xi W_\xi}{2W^{3/2}},
\]
\[
\kappa_B
=
-W^{-1/2}
+\frac{\xi}{2W^{1/2}}
\left(\frac{W_\xi}{W}+v_\xi\right).
\]
If both vanished, then
\[
\frac{\xi W_\xi}{W}=-2,
\qquad
\xi\left(\frac{W_\xi}{W}+v_\xi\right)=2,
\]
so
\[
\xi v_\xi=4.
\]
But then
\[
W=1-\frac12\xi v_\xi=-1,
\]
which is impossible for a Riemannian metric.  Thus Li–Liu’s simple moment-map faces cannot be the reflected \(T^3\).  Their value is instead that they give the exact PE stable end and its nonlinear Toda Dirichlet-to-Neumann map.

---

## 3. Outer-face pairing and Fourier transport

In the diagonal orthogonally transitive model
\[
g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,\qquad d=b-c,\quad \sigma=b+c,
\]
the anisotropy equation with defect is
\[
\boxed{
\operatorname{div}(e^\sigma\nabla d)
=
-e^{\sigma+2\phi}(E_x-E_y).
}
\tag{17}
\]
For a finite domain \(D_R\), reflection gives no inner flux.  For any constant \(c_R\),
\[
\boxed{
\int_{D_R}e^\sigma|\nabla d|^2
=
\int_{\Gamma_R}(d-c_R)e^\sigma d_n
+
\int_{D_R}(d-c_R)e^{\sigma+2\phi}(E_x-E_y).
}
\tag{18}
\]
Thus the correct transport object is the weighted covariance
\[
\int_{\Gamma_R}(d-c_R)e^\sigma d_n,
\]
not the signed total flux
\[
\int_{\Gamma_R}e^\sigma d_n,
\]
which vanishes in the reflected exact case.

The linearized expanding equation for one Fourier mode is
\[
\psi''+3\psi'-k^2e^{-2r}\psi=0,
\qquad
\psi(0)=1,\quad \psi'(0)=0.
\tag{19}
\]
The reflected solution satisfies
\[
\psi_\infty=\frac{\sinh k}{k},
\]
and
\[
\boxed{
\psi'(R)=k\sinh(k)\,e^{-2R}+O(e^{-3R}).
}
\tag{20}
\]
So the unweighted outer shear tends to zero, while the weighted quantity
\[
e^{2R}\psi'(R)\to k\sinh k
\tag{21}
\]
remains finite and carries the center anisotropy.

This calculation rules out any attempted no-go estimate that tries to control the center anisotropy using only
\[
\|P(R)\|_\infty\to0,\qquad \|E\|_\infty\to0.
\]
A genuine forbidding inequality would have to control the weighted PE stress or the outer-face pairing (18).

The same formulas are compatible with lattice quotients.  If the functions are invariant under the collapsed \(x,y\)-translations, changing the \(x,y\) periods does not change local Ricci estimates.  The identities above scale by the fundamental volume and remain the same after normalization.  Perturbations depending on collapsed directions introduce \(N^2\)-sized derivatives, so the quotient-compatible route naturally stays in the \(T^2\)-invariant class.

---

## 4. Existence route versus forbidding route

### Existence route: reflected AHE half-core with Yamabe constant \(<0\) at infinity

The clean exact object is:

\[
[0,\infty)_r\times T^3,\qquad
\operatorname{Ric}_g=-3g,
\]
with
\[
S(0)=0,\qquad R(q_0)=-6,
\]
and PE expansion (11) as \(r\to\infty\), with conformal infinity \(\gamma\) in a Li–Liu-realizable \(T^2\)-cohomogeneity-one class whose Yamabe constant is \(<0\).

This avoids the Witten–Yau/Cai–Galloway obstruction that applies to Yamabe \(\ge0\) conformal infinity.  If such a half-core exists, truncating at \(R_j\to\infty\) gives
\[
\|E\|=0,\qquad
\|S-I\|=O(e^{-2R_j}),\qquad
e^{-2R_j}\|\operatorname{Ric}(q_{R_j})\|=O(e^{-2R_j}),
\]
which is precisely the input required by the expanding-tail lemma.

Li–Liu metrics give the outer PE model and the exact nonlinear stable map.  The missing cap is the transition from the reflected scalar \(-6\) center to that PE asymptotic class.  In CMC variables, this is a stable-manifold intersection problem for (1)–(4), with inner data
\[
q_0\in\{R=-6\},\quad P(0)=0,\quad \alpha(0)=0,
\]
and outer asymptotic data
\[
q_r\to\gamma,\qquad
P\sim e^{-2r}\operatorname{Sch}_\gamma^\circ-\frac32e^{-3r}\gamma_{(3)}.
\]

The damping identity (5) makes this intersection plausible: after expansion begins, tracefree intrinsic curvature creates only \(O(e^{-2r})\) shear.  The center floor supplies an order-one initial acceleration, but it is not by itself incompatible with the PE decay law.

### Forbidding route: only a weighted inequality can work

A global obstruction would need to prove something of the form
\[
\mathcal I(q_0)
\le
\text{weighted outer flux}
+
\text{bulk defect}
+
\text{constraint residue},
\tag{22}
\]
where the center quantity is, for example,
\[
\mathcal I(q_0)=
\int_{S^1}\left(|A^\circ|^2+\frac32h^2\right)\,ds=6L.
\]
But (18) and (20) show that the weighted outer flux can remain order one while
\[
\|P(R)\|_\infty=O(e^{-2R}).
\]
Moreover PE asymptotics give exactly such weighted data:
\[
e^{2R}P(R)\to \operatorname{Sch}_\gamma^\circ.
\]
Therefore a theorem forbidding the core-tail construction would have to show something much stronger: for reflected \(T^2\)-cohomogeneity-one centers, the allowed PE stress
\[
\operatorname{Sch}_\gamma^\circ,\quad \gamma_{(3)}
\]
cannot match the center energy transport identity.  Li–Liu’s Toda construction supplies many \(\gamma\)’s and a concrete stress tensor, so this incompatibility is a computable statement, not a broad topological principle.

---

## 5. Two calculations with real deciding power

### Calculation A: reflected center scattering versus Li–Liu Toda Dirichlet-to-Neumann map

Linearize the Type I Li–Liu equation around the flat model with a one-mode trace
\[
v(0,z)=\varepsilon\cos(kz).
\]
At first order,
\[
w_{\xi\xi}+w_{zz}=0,\qquad
w(0,z)=\cos(kz),\qquad w(\infty,z)=0,
\]
so
\[
w(\xi,z)=e^{-k\xi}\cos(kz),
\]
and the Li–Liu Dirichlet-to-Neumann symbol is
\[
w_\xi(0,z)=-k\cos(kz).
\tag{23}
\]

The reflected Gaussian expanding mode has symbol
\[
\psi_\infty=\frac{\sinh k}{k},
\qquad
e^{2R}\psi'(R)\to k\sinh k.
\tag{24}
\]
Thus, at linear order, the two maps are explicit.  The real test is the quadratic zero mode: the normal balance (7) produces a definite \(O(\varepsilon^2)\) contribution to
\[
e^{2R}(3-H_R),
\]
while the Li–Liu PE expansion produces an \(O(\varepsilon^2)\) mean term in \(\gamma_{(2)}\) and in the Toda-determined stress.  If those two zero-mode coefficients can be matched by the length/scale parameter, the small-defect core has a viable perturbative mechanism.  If the coefficients have an invariant sign mismatch after imposing the Hamilton and momentum constraints, the \(T^2\)-cohomogeneity route is blocked.

This calculation is finite-dimensional for each \(k\), source-aware, and uses the actual Li–Liu equation rather than a heuristic harmonic replacement.

### Calculation B: sharp nonlinear flux identity with PE asymptotic substitution

Use (17)–(18) together with the PE expansion (12).  For an exact reflected core truncated at \(R\),
\[
\int_{D_R}e^\sigma|\nabla d|^2
=
\int_{\Gamma_R}(d-c_R)e^\sigma d_n .
\tag{25}
\]
Substituting
\[
d_n(R)=2(P_x-P_y)(R)
=
2e^{-2R}\bigl(\operatorname{Sch}_\gamma^\circ\bigr)_{xy\text{-diff}}
+O(e^{-3R})
\tag{26}
\]
gives a finite nonzero limit for the outer-face pairing.  The center identity (8) gives the inner amount of anisotropy that must be transported.

The decisive nonlinear question is whether the limit of (25), expressed through
\[
\operatorname{Sch}_\gamma^\circ,\qquad \gamma_{(3)},
\]
can equal the center energy forced by scalar \(-6\).  Li–Liu supplies \(\gamma\) and its Toda stress explicitly from the trace function \(v(0,\cdot)\).  A matching identity would make the core-tail construction credible; a strict inequality for all Li–Liu-compatible \(\gamma\) would forbid this route in the present symmetry class.

The important point is that the outer shear itself may vanish.  The weighted covariance is the object that matters, and both the Fourier model and the PE expansion show it naturally survives.