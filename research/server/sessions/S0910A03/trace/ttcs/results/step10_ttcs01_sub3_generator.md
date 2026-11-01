# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Knowledge/objects/papers/Chern-simons-forms-on-associated-bundles-and-boundary-terms--3042b35791e1--e9926094f32d/object.md",
    "Knowledge/objects/papers/Equivariant-differential-characters-and-Chern-Simons-bundles--77afec5243aa--a7a34ef1ebd0/object.md"
  ]
}
```

## Task

Construct the corrected Pontryagin/transgression approach for a collapsed near-critical Ishida–LeBrun sequence. Use the Levi-Civita characteristic density rho_+=(1/(4pi^2))(s^2/24+2|W+|^2-|Ric0|^2/2), whose L1 distance from 3/(16pi^2) tends to zero, so characteristic mass follows volume. Compare the Levi-Civita connection on Lambda^2_+ to a basic or split connection on a regular circle/nil collapse region. Derive the exact Chern–Simons transgression structure, explain what non-basic/O'Neill terms must persist for rho_+ to remain diffuse, and seek an inequality linking diffuse characteristic density to fixed-scale cover accessibility, fiber holonomy, or eigenline rotation. Avoid assuming local charge quantization or concentration at NUT cores. Give concrete equations and a viable proof program or a counterexample mechanism.

## Output

### 1. Correct Chern–Weil object: \(p_1(\Lambda^2_+)\) is diffuse, not core-localized

Let  
\[
E=\Lambda^2_+,\qquad A=A^{LC}_+
\]
be the Levi–Civita \(SO(3)\)-connection induced on \(E\). Normalize the invariant quadratic polynomial \(p\) on \(\mathfrak{so}(3)\) so that
\[
p(F_A)=\rho_+\,d\mu_g,
\]
where
\[
\rho_+
=\frac1{4\pi^2}\left(\frac{s^2}{24}+2|W_+|^2-\frac{|\operatorname{Ric}^\circ|^2}{2}\right).
\]
Equivalently,
\[
|F_A^+|^2=\frac{s^2}{24}+2|W_+|^2,\qquad
|F_A^-|^2=\frac{|\operatorname{Ric}^\circ|^2}{2},
\]
so
\[
p(F_A)=\frac1{4\pi^2}\bigl(|F_A^+|^2-|F_A^-|^2\bigr)d\mu_g.
\]

For a near-critical Ishida–LeBrun sequence with
\[
\operatorname{Ric}_{g_i}+g_i\to0\quad\text{in }L^\infty,
\]
and with the scalar–Weyl completion term
\[
s_i+8\sqrt6\,|W^+_i|\to0\quad\text{in }L^2,
\]
one gets
\[
s_i\to -4,\qquad |W_i^+|\to\frac1{2\sqrt6},\qquad
\operatorname{Ric}_{g_i}^\circ\to0
\]
in the relevant norms. Hence
\[
\boxed{\;
\left\|\rho_{+,i}-\frac{3}{16\pi^2}\right\|_{L^1(M,g_i)}\to0.
\;}
\]
Thus for every measurable region \(U_i\subset M\),
\[
\int_{U_i}p(F_{A_i})
=
\frac{3}{16\pi^2}\operatorname{Vol}_{g_i}(U_i)+o(1),
\]
uniformly in \(U_i\). The characteristic density follows volume. It is not legitimate to place the whole \(p_1(\Lambda^2_+)\)-mass at NUT cores or singular strata unless those regions carry comparable four-volume.

---

### 2. Ordinary Chern–Simons comparison with a basic or split connection

On a regular collapsed region \(U\), choose a comparison connection \(B\) on \(E|_U\), usually pulled back from the collapse base or split with respect to the vertical–horizontal decomposition. Put
\[
a=A-B,\qquad A_t=B+t a.
\]
Then the exact transgression identity is
\[
\boxed{\;
p(F_A)-p(F_B)=d\,T_p(A,B),
\;}
\]
with
\[
\boxed{\;
T_p(A,B)
=
2\int_0^1p(a,F_{A_t})\,dt.
\;}
\]
Using
\[
F_{A_t}=F_B+t\,d_Ba+\frac{t^2}{2}[a,a],
\]
this becomes
\[
\boxed{\;
T_p(A,B)
=
2p(a,F_B)+p(a,d_Ba)+\frac13p(a,[a,a]).
\;}
\]

If \(B\) is basic over a base of dimension \(\le3\), then
\[
p(F_B)=0
\]
as a four-form. Therefore, for a compact domain \(U\) with smooth frontier \(\Sigma\),
\[
\boxed{\;
\int_U \rho_+\,d\mu_g
=
\int_\Sigma T_p(A,B)
\qquad\text{if }p(F_B)=0.
\;}
\]
Since the left side is approximately
\[
\frac{3}{16\pi^2}\operatorname{Vol}(U),
\]
a regular collapsed region of definite four-volume cannot have \(A\) close to a basic/split \(B\) with small Chern–Simons flux. Some part of
\[
a,\quad d_Ba,\quad [a,a]
\]
must remain visible at order one. In geometric terms these are precisely the non-basic Levi–Civita pieces: O’Neill curvature, variation of the fiber metric, nil twisting, vertical connection coefficients, and their horizontal derivatives.

---

### 3. Associated-bundle transgression using the eigenline of \(W^+\)

Johnson’s associated-bundle formula gives a second exact decomposition, better adapted to eigenline rotation.

Let \(n\) be a unit section of \(S(E)\), for instance the lowest \(W^+\)-eigenline on a region where the eigenvalue is simple. Pull the \(SO(3)\)-frame bundle of \(E\) to \(S(E)\). The connection splits as
\[
A=\psi+\phi,
\]
where \(\psi\) is the induced \(SO(2)\)-connection on \(n^\perp\) and \(\phi\) is the complement. For degree \(2\), Johnson’s formula gives
\[
d\Phi p(A)=p(F_A)-p(F_\psi),
\]
with
\[
\boxed{\;
\Phi p(A)
=
p(\phi,F_A)+p(\phi,F_\psi)-\frac16p(\phi,[\phi,\phi]).
\;}
\]
Pulling back by \(n\) yields
\[
\boxed{\;
p(F_A)
=
p(F_{\psi_n})+d\,n^*\Phi p(A).
\;}
\]

The \(SO(2)\)-curvature may be written through the gauge-invariant “electromagnetic” curvature of the line \(n\):
\[
\mathcal F_n
=
\langle F_A,n\rangle
-\frac12\langle n,D_A n\wedge D_A n\rangle,
\]
so
\[
p(F_{\psi_n})
=
\frac1{4\pi^2}\mathcal F_n\wedge \mathcal F_n.
\]

If \(n\), \(D_A n\), and \(\psi_n\) are all basic over a base of dimension \(\le3\), then
\[
p(F_{\psi_n})=0,\qquad d\,n^*\Phi p(A)=0.
\]
Thus
\[
p(F_A)=0,
\]
which is incompatible with
\[
p(F_A)\approx \frac{3}{16\pi^2}d\mu_g
\]
on a region of definite volume. Therefore diffuse characteristic density forces at least one of the following to persist:

\[
\boxed{
\text{vertical component of }D_A n,\quad
\text{non-basic curvature of }\psi_n,\quad
\text{O'Neill/nil terms entering }F_A.
}
\]

This is the clean eigenline version of the corrected transgression picture.

---

### 4. Circle collapse: exact dimensional reduction of \(p(F_A)\)

Consider a regular circle-collapsed region
\[
\pi:U\to B^3.
\]
Let \(\eta\) be the unit vertical one-form, so
\[
d\mu_g=\eta\wedge d\nu_B.
\]
For an \(S^1\)-adapted connection write
\[
F_A=F_H+\eta\wedge \Xi,
\]
where
\[
F_H\in\Omega^2(B;\mathfrak{so}(3)),\qquad
\Xi\in\Omega^1(B;\mathfrak{so}(3)).
\]
Since \(B\) has dimension \(3\),
\[
F_H\wedge F_H=0,\qquad
(\eta\wedge\Xi)\wedge(\eta\wedge\Xi)=0.
\]
Hence
\[
\boxed{\;
p(F_A)
=
\frac1{2\pi^2}\,\eta\wedge\langle \Xi\wedge F_H\rangle.
\;}
\]
Thus the near-critical density equation becomes
\[
\boxed{\;
\frac1{2\pi^2}*_{B}\langle \Xi\wedge F_H\rangle
=
\frac{3}{16\pi^2}+o_{L^1}(1),
\;}
\]
or equivalently
\[
\boxed{\;
*_{B}\langle \Xi\wedge F_H\rangle
=
\frac38+o_{L^1}(1).
\;}
\]

This gives an immediate energy inequality:
\[
\int_U \rho_+\,d\mu
\le
\frac1{2\pi^2}
\left(\int_U|F_H|^2\,d\mu\right)^{1/2}
\left(\int_U|\Xi|^2\,d\mu\right)^{1/2}.
\]
Therefore,
\[
\boxed{\;
\left(\int_U \rho_+\,d\mu\right)^2
\le
\frac1{4\pi^4}
\left(\int_U|F_H|^2\,d\mu\right)
\left(\int_U|\Xi|^2\,d\mu\right).
\;}
\]
Since
\[
\int_U\rho_+\,d\mu
=
\frac{3}{16\pi^2}\operatorname{Vol}(U)+o(1),
\]
one obtains
\[
\boxed{\;
\int_U|\Xi|^2\,d\mu
\gtrsim
\frac{\operatorname{Vol}(U)^2}{\int_U|F_H|^2\,d\mu}.
\;}
\]
On a curvature-good region with
\[
\fint_U |F_H|^2\,d\mu\le K,
\]
this gives
\[
\boxed{\;
\fint_U|\Xi|^2\,d\mu
\gtrsim
\frac{9}{64K}
\;}
\]
up to the harmless convention constant in \(\langle\cdot,\cdot\rangle\).

So a circle-collapsed region carrying definite four-volume must have definite vertical–horizontal curvature of the Levi–Civita \(SO(3)\)-connection on \(\Lambda^2_+\). A purely basic connection gives zero \(p_1\)-density.

---

### 5. What \(\Xi\) is for the Levi–Civita connection

For a Kaluza–Klein circle metric
\[
g=\pi^*g_B+\ell^2\vartheta^2,\qquad \eta=\ell\vartheta,
\]
with \(\vartheta\) an angular connection and \(\Omega=d\vartheta\), the self-dual Levi–Civita connection has the schematic form
\[
A_+=\pi^*\bar A+\alpha,
\]
where \(\bar A\) is the \(SO(3)\)-connection coming from the base, and
\[
\boxed{\;
\alpha_i
=
-(e_i\log\ell)\,\eta
-\frac{\ell}{2}\Omega_{ij}e^j
-\frac{\ell}{2}(*_B\Omega)_i\,\eta
\quad
\text{up to the standard sign convention}.
\;}
\]
Thus the non-basic pieces are built from
\[
\nabla\log\ell,\qquad \ell\,\Omega,\qquad \nabla(\ell\Omega),\qquad \nabla^2\log\ell,
\]
and their analogues when the fiber metric is not scalar.

Consequently,
\[
\Xi=F_A(V_{\mathrm{unit}},\cdot)
\]
contains horizontal derivatives of the scaled fiber holonomy and O’Neill tensors. If these quantities tend to zero in \(L^2\), then
\[
p(F_A)\to0
\]
on the regular circle region. The diffuse density
\[
p(F_A)\approx \frac{3}{16\pi^2}d\mu
\]
therefore forces an order-one \(L^2\) amount of these O’Neill/holonomy-variation terms.

---

### 6. Fiber holonomy interpretation

Let \(K\) be the period-\(2\pi\) vertical generator and write
\[
A=A_H+\Phi\,\vartheta.
\]
Then the fiber holonomy is
\[
h(x)=\operatorname{Pexp}\int_{\gamma_x}A
=
\exp(2\pi\Phi(x))
\]
in an \(S^1\)-invariant gauge. Since
\[
\eta=\ell\vartheta,
\]
one has
\[
F_A=F_H+\eta\wedge \Xi,
\qquad
\Xi=\ell^{-1}D_H\Phi
\]
up to the extra terms from \(d\ell\), vertical-frame variation, and non-invariant gauge choices.

Thus the density equation is really a scaled holonomy-gradient equation:
\[
\boxed{\;
p(F_A)
=
\frac1{2\pi^2}\eta\wedge
\left\langle \ell^{-1}D_H\Phi\wedge F_H\right\rangle.
\;}
\]
Equivalently, if \(h\) is close to the identity and
\[
\mathcal H=\ell^{-1}\log h,
\]
then
\[
\Xi\sim D_H\mathcal H.
\]
So diffuse \(p_1(\Lambda^2_+)\)-density forces
\[
\boxed{\;
\int_U|D_H\mathcal H|^2\,d\mu
\gtrsim
\frac{\operatorname{Vol}(U)^2}{\int_U|F_H|^2\,d\mu}.
\;}
\]

This is sharper than an unscaled holonomy statement. The ordinary holonomy \(h\) may vary only by \(O(\ell)\) on a unit base ball, while the scaled logarithmic holonomy \(\ell^{-1}\log h\) varies at order one. That is exactly how a collapsed region can carry diffuse characteristic density without producing large ordinary holonomy on small loops.

---

### 7. Relation to fixed-scale cover accessibility

A short fiber loop gives noncollapse in the local universal cover only when the loop survives in the local fundamental group at the chosen scale. If it contracts inside the buffered ball, the cover does not unwrap the fiber.

For a contractible fiber loop \(\gamma_x\), nonabelian Stokes gives
\[
d_{SO(3)}(h(x),1)
\le
C\int_{D_x}|F_A|
\]
for any filling disk \(D_x\) inside the buffered ball, with the usual path-ordering constants. For two nearby fibers over a horizontal path \(\sigma\subset B\), the holonomy variation satisfies
\[
d_{SO(3)}\!\left(h(\sigma(1)),
P_\sigma^{-1}h(\sigma(0))P_\sigma\right)
\le
C\int_{\pi^{-1}\sigma}|F_A|.
\]
After scaling by \(\ell^{-1}\), this becomes an estimate on \(\Xi\).

The transgression inequality suggests the following precise theorem shape for regular circle collapse:

\[
\boxed{\;
\left(\int_U\rho_+\,d\mu\right)^2
\le
C
\left(\int_U|F_H|^2\,d\mu\right)
\left(
E_{\mathrm{acc}}(U)+E_{\mathrm{fill}}(U)+E_{\mathrm{ON}}(U)
\right).
\;}
\]

Here the three terms should be:

\[
E_{\mathrm{acc}}(U)
=
\int_{\{\text{fiber survives in local }\pi_1\}}
|\Xi|^2\,d\mu,
\]
which corresponds to fixed-scale cover accessibility;

\[
E_{\mathrm{fill}}(U)
=
\int_{\{\text{fiber contracts locally}\}}
\ell^{-2}\left(\inf_{D_x}\int_{D_x}|F_A|\right)^2d\mu,
\]
which measures how much curvature-area is needed to contract the short holonomy;

\[
E_{\mathrm{ON}}(U)
=
\int_U
\bigl(
|\nabla(\ell\Omega)|^2
+
|\nabla^2\log\ell|^2
+
|\text{vertical-frame twisting}|^2
\bigr)d\mu.
\]

The exact circle identity already proves the same inequality with \(E_{\mathrm{acc}}+E_{\mathrm{fill}}+E_{\mathrm{ON}}\) replaced by \(\int_U|\Xi|^2\). The remaining mathematical content is to express \(\Xi\) in terms of cover accessibility, filling curvature, and O’Neill geometry.

This route does not use integer packets of characteristic mass. It uses diffuse density plus exact transgression.

---

### 8. Nil collapse: the same mechanism with Higgs fields and commutators

For a nil or torus collapse with vertical coframe \(\eta^a\), write
\[
A=A_B+\sum_a\Phi_a\eta^a.
\]
Let
\[
d\eta^a
=
\Omega^a-\frac12 c^a_{bc}\eta^b\wedge\eta^c+\Gamma^a_b\wedge\eta^b.
\]
Then the curvature decomposes as
\[
\boxed{\;
F_A
=
F_0
+
\sum_a\eta^a\wedge P_a
+
\frac12\sum_{a,b}\eta^a\wedge\eta^b\,Q_{ab},
\;}
\]
where
\[
F_0
=
F_B+\sum_a\Phi_a\Omega^a,
\]
\[
P_a
=
D_B\Phi_a+\text{vertical-frame terms},
\]
and
\[
Q_{ab}
=
[\Phi_a,\Phi_b]
-
c^c_{ab}\Phi_c
+
\text{metric-frame twisting terms}.
\]

Now \(p(F_A)\) is obtained by multiplying the pieces whose vertical degree plus horizontal degree equals \(4\).

#### Rank \(1\): circle collapse over a \(3\)-base
\[
\boxed{\;
p(F_A)=2p(F_0,P_1)\wedge\eta^1.
\;}
\]
Diffuse density forces \(P_1\neq0\) in \(L^2\), paired with \(F_0\).

#### Rank \(2\): two-dimensional fiber over a \(2\)-base
\[
\boxed{\;
p(F_A)_{\eta^1\eta^2}
=
2p(F_0,Q_{12})\,\eta^1\wedge\eta^2
+
2p(P_1,P_2)\,\eta^1\wedge\eta^2.
\;}
\]
Diffuse density forces either a vertical commutator/nil term \(Q_{12}\), or two independent Higgs gradients \(P_1,P_2\), or both.

#### Rank \(3\): three-dimensional fiber over a \(1\)-base
\[
\boxed{\;
p(F_A)_{\eta^1\eta^2\eta^3}
=
2\sum_{\mathrm{cyc}}p(P_a,Q_{bc})\,
\eta^1\wedge\eta^2\wedge\eta^3.
\;}
\]
Diffuse density forces interaction between horizontal variation of vertical holonomy and nil/commutator curvature.

Thus a nil-collapsed region can carry diffuse \(p_1(\Lambda^2_+)\)-density only through persistent Higgs variation, noncommuting vertical holonomies, nil structure constants, or O’Neill curvature. A purely split nil model has zero characteristic density.

---

### 9. Eigenline rotation as the same obstruction in \(SO(3)\) language

Let \(n\) be the calibrated lowest \(W^+\)-eigenline. In a circle decomposition,
\[
D_A n
=
D_H n+\eta\,D_Vn.
\]
If \(A=A_H+\Phi\vartheta\), then
\[
D_Vn
=
\ell^{-1}(\Phi\cdot n)
\]
under the adjoint \(SO(3)\)-action. Therefore vertical eigenline rotation is controlled by the scaled logarithmic fiber holonomy. Horizontal rotation enters through \(D_Hn\).

The associated-bundle transgression gives
\[
p(F_A)
=
\frac1{4\pi^2}\mathcal F_n\wedge\mathcal F_n
+
d\,n^*\Phi p(A),
\]
with
\[
\mathcal F_n
=
\langle F_A,n\rangle
-\frac12\langle n,D_A n\wedge D_A n\rangle.
\]
If \(n\) is basic and \(D_Vn=0\), then \(\mathcal F_n\) is basic in a regular collapse chart, hence \(\mathcal F_n\wedge\mathcal F_n=0\). Also \(n^*\Phi p(A)\) is basic of degree \(3\), so its exterior derivative has no four-dimensional component. Thus diffuse \(\rho_+\) forces
\[
\boxed{\;
D_Vn\not\to0
\quad\text{or}\quad
\mathcal F_n^{\mathrm{nonbasic}}\not\to0
\quad\text{or}\quad
n^*\Phi p(A)\text{ has non-basic derivative}.
\;}
\]

This dovetails with the Weitzenböck rotation computation: near the calibrated spectrum, harmonic self-dual forms aligned with \(n\) have order-one covariant derivative energy. Collapse can absorb that only by making the eigenline rotate through the base or through scaled fiber holonomy, not by making \(\Lambda^2_+\) pulled back from a low-dimensional base.

---

### 10. A viable proof route

The strongest proof architecture is now quite concrete.

On the high-volume part of the near-critical sequence one has
\[
\rho_{+,i}\to\frac{3}{16\pi^2}
\quad\text{in }L^1.
\]
Cover this part by regular collapse charts. In each chart compare \(A_i=A^{LC}_{+,i}\) to a basic/split \(B_i\). The exact transgression gives
\[
p(F_{A_i})-p(F_{B_i})=dT_p(A_i,B_i),
\]
and \(p(F_{B_i})=0\) for genuinely basic/split models over bases of dimension at most \(3\).

In circle charts the sharper identity is
\[
p(F_{A_i})
=
\frac1{2\pi^2}\eta_i\wedge
\langle \Xi_i\wedge F_{H,i}\rangle.
\]
Therefore,
\[
\int|\Xi_i|^2
\]
has an order-one lower bound on every volume-carrying curvature-good chart.

A full proof of a fixed-topology pinching gap would follow from an upper estimate of the form
\[
\int_{\text{regular collapsed good set}}|\Xi_i|^2
\le
C\int_{\text{transition/singular set}}|\operatorname{Rm}_i|^2
+
o(1),
\]
or from a sharper alternative:
\[
\int|\Xi_i|^2
\le
C\left(
\text{fixed-scale cover-accessible volume}
+
\text{curvature-area of contracting fiber fillings}
+
\text{nil commutator energy}
\right).
\]
The lower bound from diffuse \(\rho_+\) would then force either:

1. a fixed-scale cover-accessible region of definite volume, producing a noncollapsed calibrated germ, or  
2. an order-one amount of O’Neill/nil/contracting-filling energy, which must be paid for by the global \(L^2\)-curvature budget.

The proof would be especially strong if combined with the monopole sign-cube information: several near-harmonic self-dual forms force spatial orthogonality, while the \(SO(3)\) fiber has only three dimensions. Rank \(\ge2\) flat torus collapse is then highly constrained, because two independent calibrated forms tend to make the split connection too basic, whereas diffuse \(p_1(\Lambda^2_+)\) requires non-basic curvature. Rank \(1\) circle collapse remains the most flexible channel.

---

### 11. Counterexample mechanism compatible with the corrected transgression

A countermodel would not concentrate \(p_1(\Lambda^2_+)\) at NUT cores. It would instead solve the reduced Chern–Weil equation diffusely.

For a circle collapse, the effective equation is
\[
\boxed{\;
\frac1{2\pi^2}*_{B}
\left\langle \ell^{-1}D_H\Phi\wedge F_H\right\rangle
=
\frac{3}{16\pi^2}.
\;}
\]
Equivalently,
\[
\boxed{\;
*_{B}\left\langle D_H(\ell^{-1}\log h)\wedge F_H\right\rangle
=
\frac38.
\;}
\]
Thus one can imagine a long collapsed base carrying an \(SO(3)\)-connection \(A_H\) and a scaled holonomy field
\[
\mathcal H=\ell^{-1}\log h
\]
with
\[
|F_H|=O(1),\qquad |D_H\mathcal H|=O(1),
\]
so that
\[
p(F_A)\approx \frac{3}{16\pi^2}d\mu
\]
throughout the regular region. The ordinary holonomy \(h\) may vary only by \(O(\ell)\) on unit base balls, so local covers need not unwrap the fiber. NUT-type caps can make the circle fibers contract, while the total characteristic number is read as the net Chern–Simons flux accumulated along a long base direction:
\[
d\,T_p(A,B)
=
\frac{3}{16\pi^2}d\mu+o(1).
\]

In nil collapse, the analogous diffuse equations are
\[
2p(F_0,Q_{12})+2p(P_1,P_2)
\approx
\frac{3}{16\pi^2}d\nu_B
\]
for rank \(2\), and
\[
2\sum_{\mathrm{cyc}}p(P_a,Q_{bc})
\approx
\frac{3}{16\pi^2}d\nu_B
\]
for rank \(3\). These allow diffuse characteristic density through noncommuting vertical holonomies and nil twisting, again without assigning integer charge to isolated cores.

The known Taub–NUT–AdS geometry shows that exact Einstein metrics may have short contractible circle fibers with bounded curvature and collapsed local universal covers. What is still missing for the Ishida–LeBrun problem is a closed near-critical realization satisfying simultaneously:

\[
\operatorname{Ric}+g\to0,\qquad
s+8\sqrt6|W^+|\to0,\qquad
\rho_+\to\frac{3}{16\pi^2},
\]
plus the Seiberg–Witten near-saturation constraints on harmonic self-dual forms.

So the corrected picture is:

\[
\boxed{
\text{Diffuse }p_1(\Lambda^2_+)\text{ forces persistent non-basic Levi–Civita connection energy.}
}
\]

It does not force local integer packets, and it does not by itself force NUT-core concentration. The decisive inequality is the reduced Chern–Weil estimate
\[
\boxed{\;
\left(\int_U\rho_+\,d\mu\right)^2
\lesssim
\left(\int_U|F_H|^2\,d\mu\right)
\left(\int_U|\Xi|^2\,d\mu\right),
\;}
\]
together with a geometric interpretation of \(\Xi\) in terms of fixed-scale cover accessibility, scaled fiber holonomy, O’Neill tensors, nil commutators, and calibrated eigenline rotation.