# TTCS Independent Branch Record

```json
{
  "step_id": 75,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step74_attainment_and_root_lattice.md",
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/A-COLOURFUL-CLASSIFICATION-OF-QUASI-ROOT-SYSTEMS-AND-HYPERPLANE-ARRANGEM--7dfcf71bb519--b40929d5dfa6/object.md"
  ]
}
```

## Task

Verify the two proposed consequences in spirit_step74_attainment_and_root_lattice.md against the full Step-74 theorem. First, check the variational argument that an attained orbifold P floor forces an attained scalar-energy floor, then constant scalar curvature and Einsteinity; compute the first-variation formulas and normalized-defect equality cases for k<A/3, k=A/3, and k>A/3. Second, check the topology/root-lattice argument for X a compact ball quotient: every embedded (-2)-sphere in X#k CPbar^2 lies in the exceptional -I_k lattice, and any embedded Kronheimer ADE plumbing determines a root subsystem of D_k. Scrutinize whether the signed-support-graph conclusion 'only A and D components' is valid for arbitrary root subsystems (not merely reflection-closed sets), whether E6/E7/E8 are excluded without primitivity, and whether a full-rank A_r plumbing with k=r is impossible. Identify and repair any hidden assumptions. Give a direct mathematical memo, not procedural advice.

## Output

# Scientific verification memo

## 1. Attainment of the \(P\)-floor

Write
\[
\mathcal S(g)=\int_V s_g^2\,d\mu_g,\qquad
P(g)=\int_V |\operatorname{Ric}^{\circ}_g|^2\,d\mu_g .
\]
For the paired-\(A_1\) orbifold \(V_m\), with \(k=2m>0\), Step 74 gives
\[
\mathcal S(g)\ge 32\pi^2A
\]
for every orbifold-smooth metric, and
\[
P=8\pi^2k+\frac{\sigma}{12}+2w,
\qquad
\sigma=\mathcal S-32\pi^2A\ge0,\quad
w=W-\frac{4\pi^2A}{3}\ge0.
\]
Consequently, an attained value \(P=8\pi^2k\) forces
\[
\sigma=w=0,\qquad \mathcal S=32\pi^2A.
\]
Thus such a metric would be a global minimizer of \(\mathcal S\) over the full orbifold metric space, not merely a metric satisfying the curvature equalities recorded in Step 74.

### First variation of \(\mathcal S\)

With \(\Delta=\operatorname{div}\nabla\), for a symmetric orbifold-smooth tensor \(h\),
\[
Ds_g[h]=-\langle\operatorname{Ric},h\rangle
+\nabla^i\nabla^j h_{ij}-\Delta(\operatorname{tr}h),
\qquad
D(d\mu)_g[h]=\frac12\operatorname{tr}(h)\,d\mu.
\]
After orbifold integration by parts,
\[
D\mathcal S_g[h]
=
\int_V
\left\langle
-2s\,\operatorname{Ric}
+2\nabla^2s
-2(\Delta s)g
+\frac12s^2g,
h
\right\rangle d\mu.
\tag{1}
\]

For the conformal variation \(g_t=e^{2t\phi}g\), so that \(h=2\phi g\), taking the trace in (1) gives
\[
\left.\frac{d}{dt}\right|_{0}\mathcal S(g_t)
=-12\int_V\phi\,\Delta s\,d\mu.
\tag{2}
\]
Since a global minimizer is stationary under every such variation,
\[
\Delta s=0.
\]
Compact orbifold Stokes theory is valid in finite uniformizing charts, hence \(s\) is constant.

The attained value \(\mathcal S=32\pi^2A>0\) shows that this constant is nonzero. For a trace-free variation \(h\), formula (1) then becomes
\[
D\mathcal S_g[h]
=-2s\int_V\langle\operatorname{Ric}^{\circ},h\rangle\,d\mu.
\tag{3}
\]
Taking \(h=\operatorname{Ric}^{\circ}\), which is an orbifold-smooth trace-free tensor, yields
\[
0=-2s\int_V|\operatorname{Ric}^{\circ}|^2\,d\mu.
\]
Therefore \(\operatorname{Ric}^{\circ}=0\), so \(P=0\). This contradicts
\[
P=8\pi^2k>0.
\]

Hence
\[
\boxed{\inf_{\mathscr G_{\rm orb}(V_m)}P=8\pi^2k
\text{ is not attained for every }m\ge1.}
\]
The argument needs neither the pointwise mixed-curvature equality structure nor a classification of almost-Kähler metrics.

## 2. Equality cases for the normalized defect

Put
\[
q=\frac{4k}{A+k},\qquad
B=8\pi^2(A+k),\qquad
a=\frac{\sigma}{3},\qquad b=2w,\qquad L=L_s.
\]
Step 74 gives
\[
R=B+a+b,\qquad
4P=qB+a+4b,
\]
and therefore
\[
\mathscr D-q
=
\frac{(1-q)a+(4-q)b+L}{R}.
\tag{4}
\]

### Case \(k<A/3\)

Here \(q<1\), while \(q<4\) automatically. Every coefficient in the numerator of (4) is strictly positive, so
\[
\mathscr D=q
\quad\Longleftrightarrow\quad
\sigma=w=L=0.
\]
In particular \(P=8\pi^2k\), which is impossible by the variational argument above. Thus
\[
\boxed{\alpha_{\rm orb}=\frac{4k}{A+k}
\text{ is not attained when }k<A/3.}
\]

### Case \(k=A/3\)

Now \(q=1\), and the exact identity is
\[
\mathscr D-1=\frac{3b+L}{R}
=\frac{6w+L}{R}.
\tag{5}
\]
Hence
\[
\mathscr D=1
\quad\Longleftrightarrow\quad
w=0,\qquad L=0.
\]
The signature identity gives
\[
I_+-I_-=\frac{4\pi^2A}{3},
\]
whereas \(w=0\) says
\[
I_++I_-=\frac{4\pi^2A}{3}.
\]
Thus \(I_-=0\), so
\[
W^-\equiv0.
\]
Also \(L=0\) means that \(s\) is constant. Conversely, any orbifold-smooth metric with \(W^-=0\) and constant scalar curvature satisfies \(w=L=0\), and hence \(\mathscr D=1\).

The scalar constant is nonzero because \(\mathcal S\ge32\pi^2A\). Its sign requires one extra observation: the inequality \(\mathcal S\ge32\pi^2A\) alone does not distinguish \(s>0\) from \(s<0\). The sign follows from the Yamabe input already recorded in Step 74,
\[
\mathcal Y(M_k)=-4\pi\sqrt{2A}.
\]
For every smooth metric on \(M_k\),
\[
\int_{M_k}|s_{\le0}|^2\,d\mu\ge |\mathcal Y(M_k)|^2=32\pi^2A,
\qquad s_{\le0}:=\min\{s,0\}.
\]
The same resolution construction used for the scalar transfer carries this estimate to \(V_m\): the Ricci-flat fillers have scalar curvature zero, the transition regions have bounded curvature and vanishing volume, and the deleted orbifold balls contribute \(o(1)\). Therefore
\[
\int_{V_m}|s_{\le0}|^2\,d\mu\ge32\pi^2A.
\]
A constant-scalar metric must consequently have \(s<0\).

Thus wall attainment is equivalent to the existence of an orbifold-smooth metric satisfying
\[
\boxed{W^-=0,\qquad s\equiv\text{constant}<0.}
\]
Moreover \(\sigma=0\) would give the unattainable \(P\)-floor, so any wall minimizer would necessarily satisfy
\[
\sigma>0,\qquad P>8\pi^2k.
\]

### Case \(k>A/3\)

Using \(q>1\),
\[
\mathscr D-1
=
\frac{(q-1)B+3b+L}{R}
=
\frac{(q-1)B+6w+L}{R}>0,
\]
because \(B>0\). Hence every individual metric satisfies
\[
\mathscr D(g)>1.
\]
Together with the dumbbell sequence from Step 74,
\[
\boxed{\alpha_{\rm orb}=1
\text{ and this value is not attained when }k>A/3.}
\]

---

## 3. Spherical classes on \(X\#k\overline{\mathbb{CP}}^{\,2}\)

Let \(X\) be a compact ball quotient. Its universal cover is the complex two-ball, so
\[
\pi_2(X)=0.
\]
For
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},
\]
let \(b:M\to X\) be the standard connected-sum collapse. Mayer–Vietoris gives
\[
H_2(M;\mathbb Z)
\cong
H_2(X;\mathbb Z)\oplus
\bigoplus_{i=1}^k\mathbb ZE_i,
\qquad
E_i\cdot E_j=-\delta_{ij},
\]
and \(b_*\) is projection onto \(H_2(X;\mathbb Z)\). Hence
\[
\ker b_*=\bigoplus_{i=1}^k\mathbb ZE_i.
\]

For any sphere map \(f:S^2\to M\), the composition \(b\circ f\) is null-homotopic, and therefore
\[
b_*f_*[S^2]=0.
\]
Every spherical homology class consequently has the form
\[
a=\sum_{i=1}^k a_iE_i.
\]
If an embedded sphere has self-intersection \(-2\), then
\[
-2=a^2=-\sum_i a_i^2,
\]
so
\[
\sum_i a_i^2=2.
\]
The only integral solutions have exactly two nonzero coefficients, both equal to \(\pm1\). Thus
\[
\boxed{a=\pm E_i\pm E_j,\qquad i\ne j.}
\]
These are precisely the roots of \(D_k\), with the usual small-rank conventions \(D_2=A_1\oplus A_1\) and \(D_3=A_3\).

This is a homotopy and intersection-form argument. In fact it also applies to any oriented manifold homeomorphic to \(M\): transport the map \(b\) across an oriented homeomorphism. A smooth connected-sum presentation is not essential. What is essential is a map to an aspherical \(X\) whose \(H_2\)-kernel is the \(-I_k\) summand.

## 4. Embedded Kronheimer plumbings

Let the compact exceptional configuration of a Kronheimer ALE space have sphere classes
\[
a_1,\dots,a_r\in H_2(M;\mathbb Z),
\]
with intersection matrix minus the Cartan matrix of an ADE root system \(R\). Each \(a_i\) is a \(D_k\)-root by the preceding argument.

The lattice map
\[
Q(R)\longrightarrow \bigoplus_{i=1}^k\mathbb ZE_i
\]
is injective without any primitivity assumption. Indeed, if
\[
\sum_i n_i a_i=0,
\]
intersection with every \(a_j\) gives
\[
C_R(n_1,\dots,n_r)^T=0.
\]
Since the Cartan matrix \(C_R\) is nonsingular, all \(n_i\) vanish.

Every abstract root of \(R\) is an integral combination of the simple roots and has squared norm \(2\) after reversing the sign of the ambient form. Its image is therefore an integral vector of squared norm \(2\) in \(\mathbb Z^k\), hence another vector \(\pm e_i\pm e_j\). Thus the complete root set of \(R\), not only the displayed simple roots, embeds into the \(D_k\) root set and is invariant under its own reflections.

Primitivity concerns torsion in the quotient \(\mathbb Z^k/Q(R)\); it plays no role in injectivity or in the root-set argument.

## 5. Signed-support graph classification

Let \(\Psi\subset\Phi(D_k)\) be a root subsystem in the standard reflection-invariant sense. Construct a graph whose vertices are the coordinate directions used by \(\Psi\), with an edge \(ij\) for a root supported on \(\{i,j\}\). After coordinate sign changes, every edge of a chosen spanning tree can be written as a difference root \(e_i-e_j\).

Reflections in the spanning-tree roots act as the transpositions along that tree and generate the full symmetric group on its \(v\) vertices. Since \(\Psi\) is reflection-invariant:

* all difference roots \(e_i-e_j\) on those \(v\) coordinates belong to \(\Psi\);
* if there is no sum root, the component is \(A_{v-1}\);
* if one sum root \(e_p+e_q\) occurs, permutation by the generated symmetric group produces every \(e_i+e_j\), so the component is \(D_v\).

Therefore every root subsystem of \(D_k\) is a direct sum of \(A\)- and \(D\)-type systems. This is also exactly the content of Theorem 4.1.1, Lemma 4.2.1, and Corollary 4.3.1 in the supplied root-system paper. No additive closedness or Levi property is being imposed.

An arbitrary list of ambient roots need not itself be reflection-invariant. For a plumbing, the sphere classes initially give simple roots; one must take their reflection orbit, or equivalently the full abstract ADE root set. The lattice isometry above ensures that this orbit remains inside \(\Phi(D_k)\), so the signed-graph argument applies.

### Consequences

1. **Exceptional \(E\)-types.**  
   An \(E_6\), \(E_7\), or \(E_8\) plumbing would produce a corresponding root subsystem of \(D_k\), but no such subsystem exists. Hence
   \[
   \boxed{E_6,\ E_7,\ E_8\text{ Kronheimer plumbings cannot embed for any }k.}
   \]
   This conclusion is independent of primitivity.

2. **Full-rank \(A_r\).**  
   For \(r\ge4\), an \(A_r\) subsystem is a balanced support component on exactly \(r+1\) coordinate directions. Hence it cannot embed into \(D_r\). The small ranks are:
   \[
   A_1\text{ needs }2\text{ coordinates},\qquad
   A_2\text{ needs }3,\qquad
   A_3\cong D_3\text{ can use }3.
   \]
   Thus a single \(A_r\) plumbing with \(k=r\) is impossible for \(r=1,2\) and \(r\ge4\), while \(A_3\) is the exceptional full-rank case.

3. **Configurations spanning all exceptional directions.**  
   On a balanced \(A_{v-1}\) coordinate block, the roots span only the codimension-one subspace orthogonal to a signed vector
   \[
   \pm e_1\pm\cdots\pm e_v.
   \]
   A \(D_v\) block spans all \(v\) coordinate directions. Therefore a collection whose root lattices span the full exceptional space over \(\mathbb Q\) can have only full-rank \(D_v\) support blocks, including the aliases
   \[
   D_2=A_1\oplus A_1,\qquad D_3=A_3.
   \]

The root argument applies specifically to fillings containing the standard ADE sphere configuration. A rational ball, or an ALE space with the same end group but without that sphere lattice, supplies no such root subsystem.