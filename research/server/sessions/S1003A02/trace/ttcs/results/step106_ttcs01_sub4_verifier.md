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

## Mathematical memo: zero-charge four-class Hopf cap

### 1. Exact cap invariants

The proposed cap is

\[
C \cong \#4\,\overline{\mathbb{CP}}^{2}\setminus B^{4},
\qquad \partial C=S^{3},
\]

with the Hopf chirality used in Step 105, namely \(e_{\rm out}=-1\). Its topological invariants are

\[
\chi(C)=5,\qquad \tau(C)=-4,
\]
so

\[
T(C):=(2\chi+3\tau)(C)=10-12=-2.
\]

Step 105 gives the cap charge

\[
c=4-r=0\qquad (r=4).
\]

Thus in the zero-charge limit

\[
C_{+}(C)\to 0,\qquad \widehat P(C)\to 0.
\]

The outer Hopf-collapsed \(S^{3}\) link in this chirality has

\[
\mathcal Q_{+}(S^{3}_{\rm Hopf})=-2.
\]

This is consistent with Theorem G:

\[
0=\widehat P(C)=C_{+}(C)-T(C)+\mathcal Q_{+}(\partial C)
   =0-(-2)+(-2).
\]

So the zero-charge cap requires exactly an outer link charge \(-2\).

---

### 2. What Chen–Chen does and does not classify

Chen–Chen classifies **complete hyperkähler 4-manifolds with faster-than-quadratic curvature decay**,

\[
|\mathrm{Rm}|=O(r^{-2-\varepsilon}),
\]

and obtains the ALE, ALF-\(A_k\), ALF-\(D_k\), ALG, and ALH families. In particular:

- ALF-\(A_k\) are multi-Taub–NUT;
- ALF-\(D_k\) are Cherkis–Hitchin–Ivanov–Kapustin–Lindström–Roček metrics.

But Step 105’s hypotheses do **not** supply:

1. faster-than-quadratic decay for every bubble;
2. hyperkähler structure for every piece;
3. noncollapse of every piece;
4. absence of collapsed, finite-group, or F-structure regions.

Finite-energy Ricci-flat bubbles with merely quadratic decay, orbifold bubbles, and collapsed cobordisms are outside the Chen–Chen classification. Foscolo also notes that finite-energy bubbles give quadratic decay, while faster-than-quadratic decay is a stronger condition and is not automatic.

Therefore Chen–Chen cannot be used to assert that all bubbles available under Step 105 are ALE/ALF hyperkähler instantons. It classifies only the fast-decay hyperkähler sector.

---

### 3. The \(D_4\) ALF end and its link

Use the convention in which an ALF-\(D_m\) instanton has intersection graph \(D_m\), rank \(m\). Then for \(m\ge 3\),

\[
b_2=m,\qquad \chi=m+1,\qquad \tau=-m,
\]

and the large link is

\[
S^{3}/D_{m-2}^{*},
\]

where \(D_{m-2}^{*}\) is the binary dihedral group of order \(4(m-2)\).

For \(m=4\),

\[
\chi=5,\qquad \tau=-4,\qquad T=2\chi+3\tau=-2,
\]

and

\[
D_{4-2}^{*}=D_{2}^{*}
\]

has order \(8\). This group is the quaternion group \(Q_8\). Hence the large link of the rank-four \(D_4\) ALF instanton is

\[
S^{3}/Q_8.
\]

If another text calls the binary dihedral group of order \(16\) “\(D_4\)”, that is a shifted indexing convention. The ALF instanton whose intersection lattice is \(D_4\) has link \(S^{3}/Q_8\).

Now choose the orientation used in Step 105, namely the one in which the hyperkähler metric has \(W^{+}=0\). Then

\[
C_{+}=0,\qquad \widehat P=0.
\]

Theorem G applied to a large truncated \(D_4\) ALF block \(A\) gives

\[
\mathcal Q_{+}(\partial A)=T(A)=2\chi(A)+3\tau(A)=2\cdot 5+3(-4)=-2.
\]

Thus the \(D_4\) ALF end carries exactly the same \(\mathcal Q_{+}\)-charge as the required outer Hopf \(S^{3}\):

\[
\mathcal Q_{+}(S^{3}/Q_8)=-2,
\qquad
\mathcal Q_{+}(S^{3}_{\rm Hopf})=-2.
\]

This charge match is special to \(D_4\). For a general \(D_m\) ALF block,

\[
\mathcal Q_{+}(\partial A)=2-m,
\]

so matching the outer Hopf charge \(-2\) forces \(m=4\).

---

### 4. The lattice embedding \(-D_4\subset -I_4\)

The core of a \(D_4\) ALF instanton deformation-retracts onto four spheres with intersection graph \(D_4\). With the cap orientation, its intersection form is

\[
-D_4.
\]

Inside \(-I_4\), this is an index-two sublattice:

\[
D_4=\{x\in \mathbb Z^{4}: x_1+x_2+x_3+x_4\equiv 0 \pmod 2\}
\subset \mathbb Z^{4}=I_4,
\]

so

\[
[I_4:D_4]=2.
\]

Thus a \(D_4\) ALF block can carry the even part of the four exceptional classes. However, it cannot by itself be the whole cap:

- its end is \(S^{3}/Q_8\), not \(S^{3}\);
- its lattice \(-D_4\) is even, whereas \(-I_4\) is odd;
- the cap must also account for the missing index-two coset.

Therefore one needs an additional cobordism \(B\) from the \(D_4\) end to the outer \(S^{3}\):

\[
\partial B = S^{3}\sqcup (-S^{3}/Q_8).
\]

This cobordism must supply the lattice extension from \(-D_4\) to \(-I_4\).

There is a standard topological mechanism for exactly this kind of extension. Since

\[
H_1(S^{3}/Q_8)\cong Q_8^{\rm ab}\cong (\mathbb Z/2)^2,
\]

the Mayer–Vietoris sequence for

\[
C=A\cup_{S^{3}/Q_8} B
\]

allows the quotient

\[
H_2(C)/H_2(A)
\]

to be controlled by a subgroup of \(H_1(S^{3}/Q_8)\). An order-two kernel can produce an index-two overlattice. This is the algebraic form of the needed extension.

The Akbulut rational ball \(W\) with

\[
\partial W=S^{3}/Q_8
\]

is directly relevant. It is a disk bundle over \(\mathbb{RP}^{2}\), has

\[
\chi(W)=1,\qquad \tau(W)=0,\qquad \pi_1(W)=\mathbb Z/2,
\]

and its two-fold cover is the Euler-class \(-4\) disk bundle over \(S^{2}\). Removing an interior ball gives a cobordism

\[
B=W\setminus \operatorname{int}(B^4),
\qquad
\partial B=(S^{3}/Q_8)\sqcup S^{3},
\]

with

\[
\chi(B)=0,\qquad \tau(B)=0.
\]

Gluing a \(D_4\) plumbing or \(D_4\) ALF core to this \(W\) gives invariants

\[
\chi=5+1=6,\qquad \tau=-4.
\]

If the map \(H_1(S^{3}/Q_8)\to H_1(W)=\mathbb Z/2\) is surjective, the resulting closed manifold is simply connected, has rank four, sign \(-\), and odd unimodular form, hence has form \(-I_4\). Removing a ball then gives the topology of

\[
\#4\,\overline{\mathbb{CP}}^{2}\setminus B^4.
\]

Thus the algebraic/topological premise is coherent: a \(D_4\) block plus a suitable \(Q_8\)-to-\(S^{3}\) cobordism can account for \(-D_4\subset -I_4\).

---

### 5. Link-charge equation for the cobordism

Let \(B\) be a cobordism from the \(D_4\) ALF link \(L_D=S^{3}/Q_8\) to the outer Hopf \(S^{3}\), oriented as part of the cap:

\[
\partial B=S^{3}\sqcup (-L_D).
\]

Theorem G gives

\[
\widehat P(B)
=
C_{+}(B)
-
(2\chi+3\tau)(B)
+
\mathcal Q_{+}(\partial B).
\]

If \(B\) is zero-energy in the same sense,

\[
C_{+}(B)=0,\qquad \widehat P(B)=0,
\]

then

\[
(2\chi+3\tau)(B)=\mathcal Q_{+}(\partial B).
\]

Since

\[
\mathcal Q_{+}(\partial B)
=
\mathcal Q_{+}(S^{3}_{\rm Hopf})
+
\mathcal Q_{+}(-L_D),
\]

and \(\mathcal Q_{+}\) changes sign when the 3-manifold orientation is reversed,

\[
\mathcal Q_{+}(-L_D)=-\mathcal Q_{+}(L_D).
\]

With

\[
\mathcal Q_{+}(S^{3}_{\rm Hopf})=-2,
\qquad
\mathcal Q_{+}(L_D)=-2,
\]

we obtain

\[
\mathcal Q_{+}(\partial B)=(-2)-(-2)=0.
\]

Therefore a zero-energy cobordism from the \(D_4\) end to the outer \(S^{3}\) must satisfy

\[
\boxed{\,2\chi(B)+3\tau(B)=0.\,}
\]

The punctured Akbulut rational ball has \(\chi(B)=0\) and \(\tau(B)=0\), so it satisfies this charge equation exactly.

More generally, if one tried to use a \(D_m\) ALF block, then

\[
\mathcal Q_{+}(L_D)=2-m,
\]

and the cobordism equation would become

\[
2\chi(B)+3\tau(B)
=
(-2)-(2-m)
=
m-4.
\]

Thus \(m=4\) is precisely the case in which a zero-\(T\) cobordism can connect the \(D_4\) end to the Hopf \(S^{3}\) without additional topological charge.

---

### 6. What can and cannot be concluded

The exact topology and link charges give the following.

#### What is established

1. **Chen–Chen does not decide the cap.**  
   It classifies only fast-decay hyperkähler instantons. Step 105 allows collapsed, zero-energy regions that are not covered by that classification.

2. **The relevant \(D_4\) ALF end is \(S^{3}/Q_8\).**  
   With the rank-four convention, the large link is \(S^{3}/Q_8\), not a larger binary-dihedral quotient.

3. **A \(D_4\) ALF block carries \(-D_4\).**  
   This is an index-two sublattice of \(-I_4\). The block alone cannot produce the cap because its end is \(S^{3}/Q_8\) and its lattice is even.

4. **A cobordism \(B\) from \(S^{3}/Q_8\) to \(S^{3}\) must satisfy**
   \[
   2\chi(B)+3\tau(B)=0.
   \]

5. **The Akbulut rational ball gives a topological model for \(B\).**  
   The punctured rational ball \(W\setminus B^{4}\) has the correct links, \(\chi=0\), \(\tau=0\), and the correct \(\mathbb Z/2\) quotient to permit the index-two lattice extension.

6. **The charge identities do not exclude the cap.**  
   The \(D_4\) ALF charge \(-2\), the outer Hopf charge \(-2\), and the zero-\(T\) cobordism equation are mutually consistent.

#### What is not established

The supplied data do **not** construct the cap geometrically. To turn the topological model into a Step-105 realization, one would still need:

1. a metric sequence on the cobordism \(B\) with
   \[
   C_{+}(B)\to 0,\qquad \widehat P(B)\to 0;
   \]

2. controlled Hopf-collapsed link geometry on both \(S^{3}/Q_8\) and \(S^{3}\), including the correct adiabatic eta and transgression terms;

3. collar regularity matching the \(D_4\) ALF asymptotics to the collapsed cobordism, so that the \(\mathcal Q_{+}\) charges are stable;

4. a geometric mechanism by which the cobordism carries the odd coset of \(-I_4\) while remaining energy-free in the Einstein-gap functional.

Conversely, the supplied data do **not** exclude the cap. A purely topological exclusion is not available, because the \(D_4\)+rational-ball construction satisfies the basic Euler, signature, fundamental-group, lattice-index, and charge relations. A geometric exclusion would need an additional invariant or obstruction, for example from \(w_2\), characteristic vectors, eta invariants, or gauge theory, showing that no zero-energy cobordism with these properties can exist. No such obstruction is present in the supplied materials.

---

### Final status

The correct conclusion is not that the zero-charge four-class Hopf cap is constructed or excluded by Chen–Chen. The precise state is:

- The \(D_4\) ALF instanton is a coherent carrier of the even sublattice \(-D_4\subset -I_4\).
- Its end is \(S^{3}/Q_8\), and its \(\mathcal Q_{+}\)-charge is \(-2\), matching the required Hopf \(S^{3}\) charge.
- A zero-energy cobordism from \(S^{3}/Q_8\) to \(S^{3}\) must have \(2\chi+3\tau=0\).
- The Akbulut rational ball provides a natural topological cobordism satisfying that equation and capable of producing the index-two overlattice.
- The geometric existence of such a collapsed, zero-energy cobordism under Step-105 hypotheses remains open.