# TTCS Independent Branch Record

```json
{
  "step_id": 67,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step67_corrections_and_analytic_neck_reopening.md",
    "Knowledge/objects/papers/1106.2066-The-Cauchy-problems-for-Einstein-metrics-and-parallel-spinors--e588543ba837--cf493e3a7afe/object.md",
    "Sessions/S0910A03/workspace/scripts/step66_curved_slice_collar.py",
    "Sessions/S0910A03/workspace/notes/step63_graph_manifold_counterexample_analysis.md"
  ]
}
```

## Task

Starting from the verified Gaussian Einstein equations and Koiso local germ in Step 67, derive a mathematically useful formulation of the global two-ended matching problem to flat hyperbolic cusp data on T^3. Analyze the linearization about an exact flat cusp and about a reflection-symmetric W=0 central slice. Seek explicit mode decompositions, conserved/monotone quantities, stable/unstable dimensions, or a boundary map whose surjectivity/obstruction could decide whether a constant-scalar -6 central torus can connect to flat cusp ends with exact or uniformly small Ric+3g defect. Propose the cheapest decisive calculation or theorem, and stress-test it against exact cusps and Koiso germs. Do not infer nonexistence from elliptic ill-posedness or finite numerical failure, and do not invent literature.

## Output

## 1. Gaussian formulation of the matching problem

Write
\[
G=dt^2+g_t,\qquad   
S=\frac12 g_t^{-1}\dot g_t,\qquad H=\operatorname{tr}S,
\]
so that \(S=-W\) in the convention of the supplied Koiso source. Put
\[
E:=\operatorname{Ric}_G+3G.
\]
With \(E_T^\#\) denoting the tangential mixed endomorphism, the full system is
\[
\boxed{
\begin{aligned}
\dot g&=2gS,\\
\dot S&=\operatorname{Ric}_{g}^{\#}+3I-HS-E_T^\#,\\
\dot H&=3-|S|^2-E_{00},\\
\operatorname{div}S-dH&=E_{0\cdot},\\
R_g+|S|^2-H^2
&=-6+\operatorname{tr}_gE_T-E_{00}.
\end{aligned}}
\tag{1}
\]
For \(E=0\), the last two equations are the momentum and Hamiltonian constraints.

A precise finite matching functional is therefore
\[
\varepsilon_L(F):=
\inf_G\|E\|_{L^\infty([0,L]\times T^3)},
\tag{2}
\]
where the infimum runs over smooth Gaussian metrics satisfying

\[
S_0=0,\qquad R_{g_0}=-6,
\tag{3}
\]
and, on a terminal subinterval,
\[
g_t=e^{2(t-L)}g_L,\qquad g_L=a^2F,
\tag{4}
\]
for some \(a>0\) and some flat torus metric \(F\). Thus \(S=I\), \(H=3\), and \(E=0\) on the terminal cusp piece. Reflection at \(t=0\) produces the two-ended collar.

This formulation includes every tangentially inhomogeneous metric \(g_t(x)\), all mixed constraint components, and the exact cusp jets.

---

## 2. A pointwise monotone quantity for exact Einstein continuation

Decompose
\[
S=\frac H3 I+A,\qquad \operatorname{tr}A=0.
\]
For \(E=0\), (1) becomes
\[
\boxed{
\dot H=3-\frac{H^2}{3}-|A|^2,\qquad
\dot A=\operatorname{Ric}_{g}^{\circ}-HA.}
\tag{5}
\]

Starting from \(S_0=0\), scalar comparison gives
\[
H(t)\le 3\tanh t<3.
\tag{6}
\]
If the solution later tends to \(H=3\), it also remains above \(-3\): once \(H=-3\), (5) gives \(\dot H=-|A|^2\le0\), so it cannot subsequently approach \(3\).

On such an end define
\[
Q(t,x):=e^{2t}\frac{3-H(t,x)}{3+H(t,x)}.
\tag{7}
\]
A direct calculation gives the exact identity
\[
\boxed{
\frac{d}{dt}\log Q
=
\frac{6|A|^2}{9-H^2}\ge0.}
\tag{8}
\]
Since \(H(0)=0\), one has \(Q(0)=1\).

This already rules out exact finite cusp matching: cusp data at a finite \(L\) have \(H(L)=3\), whereas (6) gives \(H(L)<3\).

### Conformal-infinity interpretation

Suppose the exact Einstein germ continues to a smooth conformally compact end. Put \(r=e^{-t}\), so
\[
G=r^{-2}(dr^2+\gamma_r).
\]
In ambient dimension four, the Fefferman–Graham expansion has the form
\[
\gamma_r=\gamma_0-r^2P_{\gamma_0}+r^3\gamma_3+O(r^4),
\tag{9}
\]
with
\[
\operatorname{tr}_{\gamma_0}\gamma_3=0,\qquad
\operatorname{div}_{\gamma_0}\gamma_3=0.
\tag{10}
\]
Here \(P_{\gamma_0}\) is the three-dimensional Schouten tensor. Since
\[
S=I-\frac r2\gamma_r^{-1}\partial_r\gamma_r,
\]
one obtains
\[
H=3+\frac14R_{\gamma_0}e^{-2t}+O(e^{-3t}).
\tag{11}
\]
Consequently,
\[
\lim_{t\to\infty}Q(t,x)=-\frac{R_{\gamma_0}(x)}{24}.
\]
Integrating (8) yields the pointwise end formula
\[
\boxed{
-\frac{R_{\gamma_0}(x)}{24}
=
\exp\!\left(
\int_0^\infty
\frac{6|A(t,x)|^2}{9-H(t,x)^2}\,dt
\right).}
\tag{12}
\]
Therefore every such reflection-symmetric Einstein end satisfies
\[
\boxed{R_{\gamma_0}(x)\le -24}
\tag{13}
\]
in the representative selected by distance from the central leaf. A flat conformal end is impossible, regardless of the transverse-traceless coefficient \(\gamma_3\).

This is stronger than an end connectedness argument: it identifies the missing asymptotic mode pointwise. A totally geodesic central leaf forces an \(e^{-2t}\) mean-curvature deficit, while a flat conformal metric has no such term.

---

## 3. Consistency tests for the monotone formula

### Exact cusp

For
\[
G=dt^2+e^{2t}F
\]
with \(F\) flat,
\[
S=I,\qquad H=3,\qquad A=0.
\]
Here \(Q=0\) identically. There is no leaf with \(S=0\), so the hypothesis \(Q(0)=1\) is absent.

### Cosh benchmark

If a three-metric \(q\) satisfied \(\operatorname{Ric}_q=-2q\), then
\[
G=dt^2+\cosh^2(t)q
\]
would satisfy \(\operatorname{Ric}_G=-3G\), with
\[
S=\tanh(t)I,\qquad H=3\tanh t,\qquad A=0.
\]
Then \(Q\equiv1\). Its conformal metric is \(\gamma_0=q/4\), whose scalar curvature is \(-24\), giving equality in (13). Such a \(q\) does not exist on \(T^3\), but the model verifies every coefficient and sign.

### Koiso germ

For an analytic \(q\) on \(T^3\) with \(R_q=-6\), Koiso gives
\[
g_t=q+t^2(\operatorname{Ric}_q+3q)+O(t^4),
\tag{14}
\]
and hence
\[
A=t\,\operatorname{Ric}_q^\circ+O(t^3).
\]
From (5),
\[
H(t)
=
3t-\left(1+\frac13|\operatorname{Ric}_q^\circ|^2\right)t^3
+O(t^5).
\tag{15}
\]
Equivalently,
\[
Q(t)
=
1+\frac{2}{9}|\operatorname{Ric}_q^\circ|^2t^3+O(t^5),
\tag{16}
\]
which agrees with (8). Since a scalar-\(-6\) Einstein metric on \(T^3\) would have constant sectional curvature \(-1\), \(\operatorname{Ric}_q^\circ\) cannot vanish identically.

---

## 4. Linearization at the flat cusp

Let
\[
\bar g_t=e^{2t}F,\qquad \bar S=I,
\]
and write
\[
h=\bar g^{-1}\delta g,\qquad s=\delta S.
\]
The linearized evolution is
\[
\boxed{
\begin{aligned}
\dot h&=2s,\\
\dot s&=e^{-2t}\mathcal R_Fh-3s-(\operatorname{tr}s)I,
\end{aligned}}
\tag{17}
\]
where
\[
(\mathcal R_Fh)_{ij}
=
\frac12\left(
\partial^k\partial_i h_{kj}
+\partial^k\partial_j h_{ki}
-\partial^k\partial_k h_{ij}
-\partial_i\partial_j\operatorname{tr}h
\right).
\tag{18}
\]
The linearized constraints are
\[
e^{-2t}
\left(
\partial^i\partial^jh_{ij}
-\Delta\operatorname{tr}h
\right)
-4\operatorname{tr}s=0,
\tag{19}
\]
\[
\partial^js_{ji}-\partial_i\operatorname{tr}s=0.
\tag{20}
\]

### TT Fourier modes

For a Fourier wave vector \(k\ne0\), impose
\[
k^jh_{ij}=0,\qquad \operatorname{tr}h=0.
\]
There are two tensor polarizations. If \(\kappa=|k|_F\), then
\[
\ddot h+3\dot h-\kappa^2e^{-2t}h=0.
\tag{21}
\]
With \(z=\kappa e^{-t}\), two explicit solutions are
\[
f_+(z)=(1+z)e^{-z},\qquad
f_-(z)=(1-z)e^z.
\tag{22}
\]
Their end expansions are
\[
f_\pm(z)=1-\frac12z^2\pm\frac13z^3+O(z^4).
\tag{23}
\]
Thus each TT mode has:

* a center mode \(h_0\), representing the conformal metric;
* a stable \(e^{-3t}\) mode \(h_3\), representing the transverse-traceless end tensor.

Fixing the conformal metric removes \(h_0\), leaving two stable amplitudes for every \(k\ne0\). Toward smaller \(t\), the pure \(h_3\) combination contains an \(e^z\) component, explaining the severe inward instability of cusp Cauchy evolution.

For \(k=0\),
\[
h=h_0+h_3e^{-3t},
\tag{24}
\]
where \(h_0\) is an arbitrary constant symmetric tensor and \(h_3\) is trace-free. Hence there are six flat-modulus center directions and five homogeneous stable directions.

### Conserved symplectic flux

Equation (21) is
\[
\left(e^{3t}\dot h\right)'-\kappa^2e^th=0.
\]
For two TT Jacobi fields,
\[
\Omega_t(h_1,h_2)
=
e^{3t}
\left(
\langle h_1,\dot h_2\rangle
-\langle\dot h_1,h_2\rangle
\right)
\tag{25}
\]
is constant. At conformal infinity it is proportional to
\[
\langle h_0^{(1)},h_3^{(2)}\rangle
-
\langle h_3^{(1)},h_0^{(2)}\rangle.
\tag{26}
\]
The full Einstein system has the analogous Einstein–Hilbert symplectic current, with canonical momentum proportional to
\[
\sqrt{\det g}\,(S-HI).
\]
Reflection data have \(\delta S=0\), hence zero pairwise symplectic flux. The image of the central trace map is therefore isotropic and, when the Fredholm dimensions match, Lagrangian. This implies symmetry of the linear Dirichlet-to-Neumann map, but it does not force \(\gamma_3=0\).

---

## 5. Linearization at a reflection-symmetric central leaf

Let \(q=g_0\), with
\[
R_q=-6,\qquad S_0=0.
\]
A variation \(K=\delta q\) preserving the central constraint satisfies
\[
D R_q(K)
=
-\Delta_q\operatorname{tr}K
+\operatorname{div}_q\operatorname{div}_qK
-\langle\operatorname{Ric}_q,K\rangle
=0.
\tag{27}
\]
The Jacobi Cauchy data are
\[
K'(0)=0,
\tag{28}
\]
and the raw tensor acceleration is
\[
K''(0)=2D\operatorname{Ric}_q(K)+6K.
\tag{29}
\]

After quotienting by tangential diffeomorphisms, the principal-symbol count is:

* six metric components;
* minus three diffeomorphism directions;
* minus the scalar equation (27);

leaving two physical components per nonzero covector. This matches the two TT stable amplitudes at the cusp. Thus, after gauge fixing and fixing the flat conformal metric, the central-to-end linear problem has an index-zero symbol shape. Its global kernel and cokernel, rather than a local dimension mismatch, carry the substantive information.

For every central metric whose Koiso germ continues conformally compactly, define the end-data map
\[
\mathcal B(q)=(\gamma_0(q),\gamma_3(q))
\tag{30}
\]
modulo tangential diffeomorphisms. Formula (12) describes one component of this map explicitly:
\[
R_{\gamma_0}(x)
=
-24\exp\!\left(
\int_0^\infty
\frac{6|A|^2}{9-H^2}\,dt
\right).
\tag{31}
\]
Hence the image of \(\mathcal B\) never contains a flat \(\gamma_0\).

---

## 6. What changes for uniformly small Einstein defect

For \(E\ne0\), the monotone identity becomes
\[
\boxed{
\frac{d}{dt}\log Q
=
\frac{6\bigl(|A|^2+E_{00}\bigr)}{9-H^2}.}
\tag{32}
\]
The signed normal component \(E_{00}\) can therefore reduce \(Q\). Its effect is amplified as \(H\to3\).

Writing
\[
\eta=3-H,
\]
the cusp-tail equation is
\[
\eta'+2\eta
=
|A|^2+E_{00}+\frac{\eta^2}{3}.
\tag{33}
\]
The exact central tail has \(\eta\sim Ce^{-2t}\). Cutting it to \(\eta=0\) at distance \(L\) costs only \(E_{00}=O(e^{-2L})\).

More quantitatively, if \(\|E\|_{\mathrm{op}}\le\varepsilon\), then
\[
H'
\le
3+\varepsilon-\frac{H^2}{3}.
\]
Thus reaching \(H(L)=3\) requires
\[
3\le
\sqrt{9+3\varepsilon}\,
\tanh\!\left(\sqrt{1+\varepsilon/3}\,L\right).
\tag{34}
\]
The smallest \(\varepsilon\) permitted by this scalar comparison satisfies
\[
\varepsilon=12e^{-2L}(1+o(1)).
\tag{35}
\]
Accordingly, the normal equation supplies no length-independent separation from zero.

---

## 7. An adiabatic flattening lemma

The normalized cusp variables expose an additional zero mode. Set
\[
g_t=e^{2t}\gamma_t,\qquad S=I+B,\qquad b=\operatorname{tr}B.
\]
Then
\[
\gamma'=2\gamma B,
\tag{36}
\]
and (1) gives
\[
B'
=
e^{-2t}\operatorname{Ric}_\gamma^\#
-bI-3B-bB-E_T^\#.
\tag{37}
\]

Let \(\gamma(u)\), \(0\le u\le1\), be any smooth path of torus metrics, constant near its endpoints, and define on \(T\le t\le T+K\)
\[
u=\frac{t-T}{K},\qquad
G=dt^2+e^{2t}\gamma(u).
\tag{38}
\]
Then
\[
B=\frac1{2K}\gamma^{-1}\partial_u\gamma.
\]
The defect components are explicitly
\[
\boxed{
\begin{aligned}
E_{00}&=-2b-|B|^2-b',\\
E_T^\#
&=
e^{-2t}\operatorname{Ric}_\gamma^\#
-bI-3B-bB-B',\\
E_{0\cdot}&=\operatorname{div}_\gamma B-db.
\end{aligned}}
\tag{39}
\]
Since the ambient norm of the mixed covector gains a factor \(e^{-t}\),
\[
\boxed{
\|E\|_{L^\infty}
\le
C_\gamma\left(K^{-1}+e^{-2T}\right).}
\tag{40}
\]
If the path preserves its volume form, the leading \(O(K^{-1})\) term in \(E_{00}\) also disappears, though the tangential \(O(K^{-1})\) term remains.

This has a strong consequence:

> If one reflection-symmetric Koiso germ extends to any complete conformally compact Einstein end on \([0,\infty)\times T^3\), with any smooth conformal metric \(\gamma_0\), then it produces finite flat-cusp collars with \(\|\operatorname{Ric}+3G\|_\infty\to0\).

Indeed, truncate the exact end at large \(T\), replace its \(O(e^{-2T})\) Fefferman–Graham tail by \(e^{2t}\gamma_0\), traverse a long path from \(\gamma_0\) to a flat metric \(F\) using (38), and finish with the exact cusp. The total defect is
\[
O(e^{-2T})+O(K^{-1}).
\tag{41}
\]
Reflection supplies the second end.

Thus the exact flat-end obstruction in (12) does not by itself give a uniform \(L^\infty\) separation: the normalized conformal metric is a center mode and can drift by \(O(1)\) over a layer of length \(O(\varepsilon^{-1})\).

---

## 8. The reduced global problem

The essential object is no longer an exact bridge to a flat end. It is an **Einstein core**:

\[
\boxed{
\begin{gathered}
G=dt^2+g_t\quad\text{on }[0,\infty)\times T^3,\\
\operatorname{Ric}_G=-3G,\qquad
S_0=0,\qquad R_{g_0}=-6,\\
G\ \text{conformally compact as }t\to\infty.
\end{gathered}}
\tag{42}
\]

Formula (12) says its conformal metric must satisfy \(R_{\gamma_0}\le-24\) in the central-distance representative. Such conformal classes exist on \(T^3\), so this sign does not contradict torus topology.

The two outcomes have sharply different geometric signatures:

1. **Existence of one core (42).**  
   The adiabatic lemma gives uniformly small-defect flat-cusp collars.

2. **Uniform separation of all central evolutions from the expanding cusp slow manifold.**  
   Such a theorem would have to control
   \[
   B=S-I,\qquad e^{-2t}\operatorname{Ric}_{\gamma_t},
   \]
   before adiabatic drift begins. The end flattening layer itself cannot supply such separation.

A natural elliptic representation is the Einstein–DeTurck equation on a compactified half-cylinder, with a totally geodesic inner face and prescribed conformal metric \(\gamma_0\) at infinity. The linearized physical symbol has two TT components at each nonzero Fourier mode, matching the two central components from (27). The smallest singular value of this mixed trace map, together with the conserved symplectic form, is the relevant spectral quantity.

The cheapest rigorous theorem is the monotone identity (12), which completely settles exact flat-end matching. For the uniformly small problem, the most decisive unresolved theorem is existence or nonexistence of a core (42). Exact source searches with the highest relevance are:

- Poincaré–Einstein metrics on \(\mathbb R\times T^3\) with two conformal infinities and Yamabe constant \(<0\);
- Einstein metrics with a totally geodesic compact inner hypersurface and prescribed conformal infinity;
- Fredholm and scattering theory for the Einstein Dirichlet-to-Neumann map in ambient dimension four;
- connectedness theorems for conformal infinity in the zero and \(<0\) Yamabe regimes.

Any computation of (42) should satisfy the pointwise identity (12), the Koiso expansion (15), the TT cusp modes (22), and vanishing Einstein–DeTurck vector. These are independent mathematical consistency tests, not conclusions drawn from optimizer behavior.