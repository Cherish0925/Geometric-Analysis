# Step 75 — Review and strengthening of the paired-football theorem

Agent4 / Preceptor, Execute. This note checks Step 74 and Spirit #83 against the primary curvature sources, a modern statement of the torus-action classification, the root-subsystem literature, A02's independent Step-93 review, and two independent TTCS verifiers. It replaces the attainment paragraph of `step74_orbifold_transfer_theorem.md`; the lower/upper construction and mixed-transfer calculations there remain in force.

## 1. Scope of the curvature supply

Let $X$ be any compact complex-hyperbolic surface, $A=c_1^2(X)$, and
\[
M_k=X\#k\overline{\mathbb{CP}}^{2}.
\]
LeBrun's Yamabe calculation for every general-type blow-up gives
\[
Y(M_k)=-4\pi\sqrt{2A},\qquad
\int_{M_k}(s^-)^2\ge32\pi^2A,
\qquad \inf_g\int s_g^2=32\pi^2A.
\]
This is Theorem 2 and its proof in `Kodaira-dimension-and-the-Yamabe-problem` (lines 138–152), and has no $b^+>1$ exception. Thus the scalar input used in Theorem 74.A is unconditional for fake projective planes as well.

For the mixed inequality, LeBrun's polarized Proposition 3.2 and Theorem 2.3 apply metric by metric. Given a polarization $H=H_g^+$, choose the exceptional signs so that $c_H^+\cdot E_j\le0$ and use
\[
a_H=c_1(X)-\sum E_j,
\qquad (a_H^+)^2\ge A.
\]
When $b^+=1$, $c_1(X)^2=A>0$ prevents a polarization wall for the relevant small-perturbation invariant; the selected class may depend on $H$ but stays fixed through the conformal argument. Hence for every smooth metric on $M_k$,
\[
\int(s-\sqrt6|W^+|)^2\ge72\pi^2A.
\]
The convex-hull explanation in Step 74 should therefore be replaced by this polarized selection argument. No fake-plane exception remains.

## 2. Smooth topology of the resolved football

Let $N$ be the oriented resolution of the two $A_1$ points of $S^4/\mathbb Z_2$ by complex-oriented Eguchi–Hanson caps. Elementary topology gives
\[
\pi_1(N)=0,
\]
and the two disjoint $(-2)$ spheres span an index-two sublattice of $H_2(N;\mathbb Z)$; unimodularity then gives $Q_N=-I_2$.

The $T^2/\{(-1,-1)\}$ action extends over both toric caps. With the correct opposite complex orientation at the south pole, a cyclic list of primitive isotropy vectors is
\[
(1,0),\ (0,1),\ (-1,2),\ (1,-1),
\]
whose consecutive determinants are $\pm1$. Thus the resolved space is a smooth simply connected torus four-manifold with a four-edge orbit disk and negative form $-I_2$.

Corro–Núñez-Zimbrón–Zarei restate the Orlik–Raymond/Pao classification: a simply connected closed oriented four-manifold with an effective $T^2$ action is equivariantly homeomorphic to an equivariant connected sum of the standard blocks (Theorem 2.10(1)) \cite{corro2022torus}; their introduction also records Orlik–Raymond's equivalence of smooth and topological classifications for these actions and identifies the originals as *Actions of the torus on 4-manifolds I–II*. Together with the explicit smooth weighted orbit data above, this supports the standard smooth identification
\[
N\cong\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2.
\]
A bare use of the lattice or Freedman theory would not suffice; it is the smooth torus action/weighted-orbit classification that carries the diffeomorphism conclusion. Theorem 74.A should cite \cite{corro2022torus} as a modern locator and the Orlik–Raymond originals named there.

## 3. Exact nonattainment of the $P$ infimum

For
\[
V_m=X\#m(S^4/\mathbb Z_2),\qquad k=2m>0,
\]
Step 74 proved
\[
P=8\pi^2k+\frac{\sigma}{12}+2w,
\quad
R=8\pi^2(A+k)+\frac{\sigma}{3}+2w,
\]
where
\[
\sigma=S-32\pi^2A\ge0,
\qquad w=W-\frac{4\pi^2A}{3}=2I_-\ge0.
\]
Suppose the floor $P=8\pi^2k$ were attained. Then $\sigma=w=0$, so the same metric attains the all-orbifold scalar minimum
\[
S=\int s^2=32\pi^2A.
\]
Because this lower bound holds over all orbifold-smooth metrics, the metric is stationary for $S$.

For $g_t=e^{2t\phi}g$ in dimension four,
\[
\left.\frac d{dt}\right|_0S(g_t)
=-12\int s\Delta\phi
=-12\int\phi\Delta s.
\]
Orbifold integration by parts is valid in finite uniformizing charts, so stationarity gives $\Delta s=0$ and hence $s$ is constant. Since $S>0$, $s\ne0$. For a trace-free metric variation $h$,
\[
DS_g[h]=-2s\int\langle\operatorname{Ric}^\circ,h\rangle.
\]
Taking $h=\operatorname{Ric}^\circ$ forces $P=0$, contradicting $P=8\pi^2k>0$. Therefore
\[
\boxed{P(g)>8\pi^2k\quad\text{for every individual orbifold metric on }V_m,}
\]
although the Green-football sequence approaches this value. The scalar-minimum argument is stronger and cleaner than invoking Derdziński; the pointwise norm equalities alone do not determine the spectrum of $W^+$.

## 4. Exact normalized equality cases

Put $q=4k/(A+k)$ and $B=8\pi^2(A+k)$. Direct subtraction gives
\[
\mathscr D-q
=\frac{(1-q)\sigma/3+2(4-q)w+L_s}{R},
\tag{4.1}
\]
\[
\mathscr D-1
=\frac{(q-1)B+6w+L_s}{R}.
\tag{4.2}
\]
Consequently:

1. If $k<A/3$, then $q<1$ and equality in (4.1) forces $\sigma=w=L_s=0$, hence the impossible $P$ attainer. Thus $\alpha_{\rm orb}=4k/(A+k)$ is not attained.
2. If $k>A/3$, (4.2) is strictly positive for every metric, while the cylinder family tends to one. Thus $\alpha_{\rm orb}=1$ is not attained.
3. If $k=A/3$, then
   \[
   \mathscr D-1=\frac{6w+L_s}{R}
   =\frac{12I_-+L_s}{R}.
   \]
   Attainment is equivalent to an orbifold-smooth metric with $W^-=0$ and constant scalar curvature. Transferring the stronger bound $\int(s^-)^2\ge32\pi^2A$ shows the constant is negative. Such a metric cannot have $\sigma=0$, since that would attain the forbidden $P$ floor; hence any wall attainer would have $S>32\pi^2A$ and $P>8\pi^2k$. This is the only remaining normalized-attainment question in the paired-football family.

Since $A\in9\mathbb Z$ and $k=2m$, the wall occurs only for $A=18j$, $k=6j$, $m=3j$.

## 5. Asphericity forces every $(-2)$ sphere into the $D_k$ lattice

The compact ball quotient $X$ is aspherical. Let
\[
b:M_k=X\#k\overline{\mathbb{CP}}^2\longrightarrow X
\]
be the collapse of the blow-up summands. For every sphere map $f:S^2\to M_k$, $b\circ f$ is null-homotopic, so
\[
b_*f_*[S^2]=0.
\]
Under
\[
H_2(M_k;\mathbb Z)=H_2(X;\mathbb Z)\oplus\bigoplus_{i=1}^k\mathbb ZE_i,
\]
the kernel of $b_*$ is precisely the exceptional summand. If an embedded sphere has square $-2$, its class is
\[
\sum_i a_iE_i,\qquad \sum_i a_i^2=2,
\]
and hence
\[
\boxed{[S]=\pm E_i\pm E_j,\quad i\ne j.}
\]
These are exactly the roots of $D_k$ after reversing the sign of the intersection form. This needs neither symplecticity nor a negative-square adjunction theorem and survives oriented homeomorphic re-marking, provided the collapse map is transported.

## 6. Embedded Kronheimer plumbings give root subsystems

Suppose an ADE Kronheimer plumbing embeds in $M_k$, with simple sphere classes $a_1,\ldots,a_r$. Its Cartan matrix is nonsingular, so the induced map from its root lattice into $\mathbb Z^k$ is injective; primitivity is unnecessary. Every abstract root is an integral combination of simple roots of norm two, hence maps to a $D_k$ root. The isometry intertwines root reflections. Therefore the full ADE root system, not merely its chosen simple roots, embeds as a reflection-closed root subsystem of $D_k$.

A signed-support-graph proof then classifies each connected coordinate block. After coordinate sign changes, make a spanning tree consist of difference roots. Its reflections generate all coordinate permutations and hence all difference roots on the block. If no plus root occurs, the component is $A_{v-1}$ on $v$ coordinates; if one plus root occurs, reflection closure generates all $\pm e_i\pm e_j$ and the component is $D_v$. Thus root subsystems of $D_k$ have only $A$ and $D$ components, as also stated in the classical-subsystem classification of Rembado \cite{rembado2022colourful}.

Consequences:

- $E_6,E_7,E_8$ Kronheimer plumbings cannot embed in $X\#k\overline{\mathbb{CP}}^2$ for any $k$.
- A single $A_r$ plumbing normally needs $r+1$ coordinate directions, so it cannot absorb all $k=r$ exceptional directions for $r=1,2$ or $r\ge4$. The exception is $A_3=D_3$, which embeds at full rank but already fails the Step-74 mixed Einstein-bulk inequality.
- If a disjoint collection of ADE plumbings spans the entire exceptional $\mathbb Q^k$, every coordinate-support block must have full rank. Hence only $D_v$ blocks can occur, including the coincidences $D_2=A_1\oplus A_1$ and $D_3=A_3$.

This does not construct surviving $D_v$ embeddings or their complements. It does not apply to rational-ball fillings or to hypothetical $b_2=1$ fillers whose link has an ADE name but whose compact core is not the Kronheimer root plumbing.

## 7. Scientific consequence

The ordinary paired-$A_1$ branch now has an exact variational law and exact nonattainment away from one normalized wall. The root theorem removes the apparently surviving full-absorption $E$ and large $A$ Kronheimer rows. The genuine remaining singular competitors must survive both the mixed curvature inequality and the topology of actual fillings: $D$-type plumbings, genuine Ricci-flat rational-ball/T-type fillings, or geometries outside the Kronheimer sphere-plumbing architecture. For each, an embedding with the required complement and a compact negative Einstein bulk remain necessary; charge arithmetic alone is not a construction.

For the unrestricted smooth programme, the stronger strategic result is exclusion: no smooth minimizing sequence with $P_*<8\pi^2k$ can converge regularly to the paired-football bulk, and the principal E-type/A-type Kronheimer alternatives are topologically unavailable on the aspherical host. This does not determine the true smooth tariff or prove smooth global attainment. Those remain the high-value Problems 2 and 3, where the existing conditional Anderson route already identifies the decisive missing analytic input: compactness/regularity of actual $P$-minimizing sequences and strict subadditivity against every surviving bubble split.
