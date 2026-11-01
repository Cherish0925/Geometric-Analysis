# TTCS Independent Branch Record

```json
{
  "step_id": 106,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Knowledge/objects/papers/Gravitational-instantons-with-faster-than-quadratic-curvature--7396e04be7db--eb0491a0eaa4/object.md",
    "Knowledge/objects/papers/Harmonic-forms-on-ALF-gravitational-instantons--7096f93c68b0--be37c8f41b08/object.md",
    "Knowledge/objects/papers/ALF-gravitational-instantons-and-collapsing-Ricci-flat-metrics-on-the-K3--a233cd85736a--55c6bc2acb81/object.md",
    "Sessions/S1003A02/staging/acquired/Cappell-Shaneson_s_4-dimensional_s-cobordism_4136aa318e619742/content.md"
  ]
}
```

## Task

Analyze the proposed zero-charge four-class Hopf cap using exact topology and link charges. Determine what can actually be concluded about decompositions into hyperkähler ALE/ALF bubbles and zero-energy collapsed cobordisms. In particular check: (i) whether Chen–Chen classifies all bubbles available under Step-105 hypotheses or only faster-than-quadratic hyperkähler instantons; (ii) the D4 ALF indexing/end—whether its large link is S^3/Q8 or a different binary-dihedral quotient; (iii) whether a D4 block can account for -D4⊂-I4 at index 2; (iv) what boundary-charge equation a cobordism from the D4 end to S3 must obey; and (v) whether the data suffice to exclude or construct the cap. Return a direct mathematical memo, correcting the premise if needed rather than forcing a decision.

## Output

## Mathematical memo

### 1. Chen–Chen does not classify every possible cap bubble

Chen–Chen use “gravitational instanton” for a complete hyperkähler four-manifold with faster-than-quadratic curvature decay,
\[
|\mathrm{Rm}|=O(r^{-2-\varepsilon}).
\]
Their Theorem 1.1 improves the asymptotics of such spaces, while Theorems 1.2–1.3 identify the ALF \(D_k\) and \(A_k\) families. These results do not turn an arbitrary rescaling supplied by Step-105 hypotheses (E) into one of those instantons.

Indeed, (E) gives no curvature-scale extraction theorem on the caps. If a rescaled cap region converges smoothly to a complete nonflat space, then the scale-invariant vanishing
\[
\int |\mathrm{Ric}^{\circ}|^2\to0,\qquad
\int s^2\to0,\qquad
\int |W^+|^2\to0
\]
would make that limit Ricci-flat and anti-self-dual. Its simply connected cover would then be hyperkähler. Completeness, finite energy, ALF/ALE volume growth, and faster-than-quadratic decay still require separate arguments. Non-simply-connected Ricci-flat pieces, orbifold limits, necks, and curvature behavior without smooth rescaled convergence are also not addressed by Chen–Chen.

Thus the \(D_4\) ALF model is a mathematically consistent candidate, not an exhaustive consequence of (E).

---

### 2. Exact energy and charge budget of the four-class cap

For
\[
C=\#4\,\overline{\mathbb{CP}}^{\,2}\setminus B^4
\]
one has
\[
\chi(C)=5,\qquad \tau(C)=-4,
\]
and hence
\[
2\chi+3\tau=-2,\qquad 2\chi-3\tau=22.
\]

In the admissible Hopf chirality \(e_{\mathrm{out}}=-1\), the outer \(S^3\) link has
\[
(q_+,q_-)=(-2,2).
\]
Theorem G therefore gives, when \(\widehat P\to0\) and the scalar contribution vanishes,
\[
C_+(C)\longrightarrow (-2)-(-2)=0,
\]
but also
\[
C_-(C)\longrightarrow 22-2=20.
\]
Thus the cap has zero \(C_+\)-charge while carrying exactly twenty normalized units of anti-self-dual curvature:
\[
\frac1{2\pi^2}\int_C |W^-|^2\longrightarrow20.
\]
Any proposed bubble decomposition must account for this entire \(C_-\)-budget.

---

### 3. The \(D_4\) ALF index and its large link

The conventions in the supplied ALF sources are:

\[
D_K\text{ ALF}\quad\Longrightarrow\quad
L_\infty=S^3/D_{K-2}^{*},
\]
where \(D_n^{*}\) has order \(4n\). Consequently,
\[
D_4\text{ ALF}\quad\Longrightarrow\quad
L_\infty=S^3/D_2^{*}=S^3/Q_8.
\]

Chen–Chen sometimes write the binary dihedral group using its order, \(D_{4(K-2)}\). For \(K=4\) this is the order-eight quaternion group. The link is therefore \(S^3/Q_8\), not a quotient by a group of order \(16\).

For a compact truncation \(N\) of the \(D_4\) ALF space,
\[
b_2(N)=4,\qquad \chi(N)=5,\qquad \tau(N)=-4,
\]
and its intersection lattice is \(-D_4\). In the hyperkähler orientation \(W^+=0\). The ALF Euler transgression tends to zero, so
\[
\frac1{8\pi^2}\int_N |W^-|^2=5,
\qquad C_-(N)=20.
\]
Theorem G then gives
\[
q_+(S^3/Q_8)=-2,\qquad q_-(S^3/Q_8)=2.
\]
Hence the \(D_4\) ALF end and the admissible Hopf \(S^3\) link have exactly the same charge pair:
\[
(-2,2).
\]

This equality uses ALF first-jet geometry. The topologically identical \(Q_8\) link at an ALE \(D_4\) end has a different \(q_-\)-value.

---

### 4. The index-two lattice extension is exact

Inside \((\mathbb Z^4,-I_4)\),
\[
D_4=\left\{x=(x_1,\dots,x_4)\in\mathbb Z^4:
\sum_i x_i\equiv0\pmod2\right\}
\]
is an index-two sublattice. A simple-root basis is
\[
e_1-e_2,\quad e_2-e_3,\quad e_3-e_4,\quad e_3+e_4,
\]
whose Gram matrix is minus the \(D_4\) Cartan matrix. Thus
\[
[-I_4:-D_4]=2,\qquad \det(D_4)=4.
\]

There is also an exact topological carrier for this extension. Akbulut’s \(W\) is the orientable real rank-two disk bundle over \(\mathbb{RP}^2\), with
\[
\partial W=S^3/Q_8,\qquad
H_1(W;\mathbb Z)=\mathbb Z_2,\qquad H_2(W;\mathbb Z)=0.
\]
Remove an interior \(B^4\) and write \(W^\circ=W\setminus\operatorname{int}B^4\). Then
\[
\partial W^\circ=(S^3/Q_8)\sqcup S^3,
\]
and
\[
H_1(W^\circ)=\mathbb Z_2,\quad H_2(W^\circ)=0,\quad
H_3(W^\circ)=\mathbb Z,\quad
\chi(W^\circ)=\tau(W^\circ)=0.
\]

Since
\[
H_1(S^3/Q_8)=Q_8^{\mathrm{ab}}
             \cong\mathbb Z_2\oplus\mathbb Z_2
\]
maps onto \(H_1(W^\circ)=\mathbb Z_2\), gluing \(N\) to \(W^\circ\) gives
\[
0\longrightarrow H_2(N)
\longrightarrow H_2(N\cup W^\circ)
\longrightarrow \ker\!\left[
(\mathbb Z_2)^2\to\mathbb Z_2
\right]
\longrightarrow0.
\]
The final kernel has order two. Consequently, \(H_2(N)\) sits with index two in the free rank-four lattice of the glued space. Under the standard identification of
\[
H_1(S^3/Q_8)\cong D_4^*/D_4,
\]
this is precisely an index-two integral extension of \(-D_4\), isometric to \(-I_4\).

Thus a \(D_4\) block can account for the even sublattice, while \(W^\circ\) carries the parity change and the characteristic information. The individual exceptional generators \(e_i\) do not lie in the \(D_4\) core.

The supplied material does not identify \(N\cup W^\circ\) diffeomorphically with the standard punctured \(\#4\,\overline{\mathbb{CP}}^{\,2}\), although it has the required fundamental group and intersection lattice.

---

### 5. Two-link charge equation for the cobordism

Let \(Z\) run from an inner link \(L_{\mathrm{in}}\) to an outer link \(L_{\mathrm{out}}\), so
\[
\partial Z=L_{\mathrm{out}}\sqcup(-L_{\mathrm{in}}).
\]
The exact identity is
\[
\widehat P(Z)
=C_\pm(Z)-(2\chi\pm3\tau)(Z)
+q_\pm(L_{\mathrm{out}})
-q_\pm(L_{\mathrm{in}}).
\]

For \(Z=W^\circ\),
\[
\chi(Z)=\tau(Z)=0.
\]
With a \(D_4\) ALF inner link and the admissible Hopf outer link,
\[
q_\pm(L_{\mathrm{out}})
=q_\pm(L_{\mathrm{in}})
=(-2,2).
\]
Therefore
\[
\widehat P(Z)=C_+(Z),\qquad
\widehat P(Z)=C_-(Z).
\]
Since the global sequence has \(\widehat P\to0\), this equation permits
\[
C_+(Z)\to0,\qquad C_-(Z)\to0.
\]
The \(D_4\) ALF block then carries all twenty units of cap \(C_-\)-energy, while \(W^\circ\) may collapse without residual curvature energy.

The ALE \(D_4\) model behaves differently. Its asymptotic group is also \(Q_8\), but
\[
\frac1{8\pi^2}\int |W^-|^2
=5-\frac18=\frac{39}{8},
\qquad C_-=\frac{39}{2}.
\]
Hence its link charges are
\[
(q_+,q_-)=\left(-2,\frac52\right).
\]
A cobordism from that ALE link to the Hopf \(S^3\) must satisfy
\[
\widehat P(Z)=C_+(Z),\qquad
\widehat P(Z)=C_-(Z)-\frac12.
\]
Thus \(\widehat P\to0\) forces
\[
C_-(Z)\to\frac12.
\]
An ALE \(D_4\) bubble has the right lattice but cannot be followed by a cobordism whose two chiral curvature energies both vanish. The missing half-unit must occur in the transition region or in another ASD concentration.

---

### 6. Conditional structural consequence

Suppose additionally that:

1. every curvature concentration is a simply connected Chen–Chen ALF block;
2. these blocks carry all four rational \(H_2\)-classes;
3. the intervening cobordisms have \(H_2=0\) and \(C_-\to0\).

For an ALF \(A_r\) or \(D_r\) block,
\[
\chi=r+1,\qquad C_-=4(r+1).
\]
If the total root rank is four and there are \(m\) blocks, then
\[
20=C_-^{\mathrm{cap}}
=4\sum_{a=1}^m(r_a+1)
=4(4+m).
\]
Hence \(m=1\). The rank-four possibilities are \(A_4\) and \(D_4\). Since
\[
\det A_4=5
\]
cannot equal the square of an integral index in the unimodular cap lattice, whereas
\[
\det D_4=4=2^2,
\]
the single block must be \(D_4\).

This is a genuine consequence of those three added assumptions. Hypotheses (E) themselves do not provide them.

---

### 7. What the present data establish

The topology and link charges do **not** exclude the four-class zero-\(C_+\) Hopf cap. They instead exhibit a sharply matched architecture:
\[
\boxed{\text{\(D_4\) ALF core }N
\quad+\quad
\text{punctured \(\mathbb{RP}^2\)-disk bundle }W^\circ}
\]
with

- inner link \(S^3/Q_8\);
- outer Hopf link \(S^3\);
- lattice extension \(-D_4\subset-I_4\) of index two;
- identical charge pair \((-2,2)\) at the two links;
- \(C_-(N)=20\), equal to the full cap budget;
- \(\chi(W^\circ)=\tau(W^\circ)=0\), compatible with vanishing curvature energy there.

The same data do not construct the required metric degeneration. Missing analytic content includes a metric family on \(W^\circ\) realizing the two prescribed collar geometries while
\[
C_+(W^\circ),\ C_-(W^\circ),\ \widehat P(W^\circ)\to0,
\]
a smooth rescaling theorem producing the \(D_4\) ALF core from a Step-105 sequence, and a gluing or insertion theorem placing this cap into the ambient Einstein-domain degeneration. Thus the proposed mechanism is topologically and energetically coherent, but its metric realization remains unresolved.