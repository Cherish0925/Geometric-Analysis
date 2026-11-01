# TTCS Independent Branch Record

```json
{
  "step_id": 78,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step78_bianchi_vii0_verify.py",
    "Sessions/S0910A03/workspace/data/step78_bianchi_vii0_symbolic.json",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md"
  ]
}
```

## Task

Using the same rotating-eigenframe Bianchi VII_0 ansatz and exact ODEs, search for the strongest rigorous invariant or monotonicity statement relevant to vanishing-defect graph connectors. The target is not a complete PE metric but a finite connector starting at a reflection face and needing to reach an expanding regime with u=a'/a positive, small full Ricci defect, and eventual compatibility with the Step 73 tail. Examine exact and delta-forced equations, Hamiltonian/normal constraints, possible integrating factors, and sign barriers. Develop concrete lemmas with explicit constants or state exactly why no stronger geometry-independent constant follows. Also infer what genuinely additional matrix/base mechanism a successful construction would need once this ansatz is excluded. Do not propose generic numerical optimization; give mathematical structure and testable equations.

## Output

## Summary of the strongest rigorous statement available in this ansatz

Working in the exact ODE system your Step 78 script certified, the rotating‑eigenframe Bianchi VII₀ core admits a clean, fully quantitative exclusion of the connector you are seeking, and the same argument survives a forced defect up to an explicit universal threshold. Below I give the invariant, the two integrating factors that produce it, the monotonicity theorem with explicit constants, the forced version with the sharp number δ\*=3/7, the reason no stronger dimension‑free constant is available or needed, and the structural inference about what a working construction must add once this family is closed off.

Notation as in Step 78: $u=a'/a,\ v=b'/b,\ w=c'/c,\ H=u+v+w,\ d=\log(b/c),\ V=abc$, and the twist curvature
$$
K=\frac{k^2(b^2-c^2)^2}{2a^2b^2c^2}=2k^2a^{-2}\sinh^2 d\ \ge 0,\qquad L=K\coth d .
$$
The reflection face is $S=0$, i.e. $u=v=w=0$ at $r=0$, hence $d'(0)=v-w=0$.

## 1. The two integrating factors and the conserved constraint

The volume $V=abc$ is the natural weight. Direct multiplication of the exact equations gives momentum‑type identities
$$
(Vu)'=V(3-K),\qquad (Vv)'=V(3+L),\qquad (Vw)'=V(3-L),
$$
and, subtracting the last two, the exact anisotropy transport in divergence form
$$
\boxed{(Vd')'=2VK\coth d } .
$$
The Gauss (Hamiltonian) relation for $\operatorname{Ric}=-3g$ in dimension four is
$$
R_{\text{slice}}=-6+H^2-|S|^2,\qquad R_{\text{slice}}=-K,
$$
equivalently the first integral
$$
\boxed{(uv+vw+wu)+\tfrac12 K=3 } .
$$
The mean‑curvature Riccati is $H'=3-|S|^2$. At the face this forces $K(0)=6$: the mandatory intrinsic scalar curvature $R(q_0)=-6$ is produced **entirely** by the twist. This single fact is the seed of the whole obstruction: the forced central twist is exactly twice the isotropic expansion rate $3$, so
$$
u'(0)=3-K(0)=-3<0 .
$$
The distinguished circle contracts the instant one leaves the face.

Note the identity $(\log K)'=-2u+2\coth(d)\,d'$ is purely algebraic (it is the definition of $K$ differentiated); it holds with or without any Ricci defect.

## 2. Exact monotonicity theorem (explicit constants)

**Anisotropy is monotone.** Assume $d(0)=d_0>0$ (the case $d_0<0$ is the $b\leftrightarrow c$ mirror; $d_0=0$ is excluded because it gives $K(0)=0\neq6$). While $d>0$, $(Vd')'=2VK\coth d>0$; since $Vd'(0)=0$ this gives $Vd'>0$, hence $d'>0$ and $d>d_0$ for all $r>0$. The anisotropy strictly grows, unconditionally in $u$.

**The distinguished expansion rate never turns positive.** Suppose $u$ first returned to $0$ at some $r_1>0$. On $(0,r_1)$ one has $u<0$ and $d'>0$, so $(\log K)'=-2u+2\coth(d)d'>0$, i.e. $K$ strictly increases and $K>K(0)=6>3$. Then $(Vu)'=V(3-K)<0$, so $Vu$ strictly decreases from $0$, giving $u(r_1)<0$, a contradiction. Hence
$$
\boxed{u(r)<0\ \text{ and }\ K'(r)>0\ \text{ for all } r>0 }.
$$

Because $K=2k^2a^{-2}\sinh^2 d$ with $a$ strictly shrinking ($u<0$) and $d$ strictly growing, $K$ increases without turning point; combined with $H'=3-|S|^2\le 3-u^2$ this drives focusing ($H\to-\infty$) and $a\to0$. The twist curvature diverges monotonically. **There is no exact rotating‑eigenframe VII₀ connector from a reflection face to any regime with $u=a'/a>0$**; the family recollapses instead of opening into the almost‑umbilic expanding slice the Step 73 tail requires. The constants $6,3$ are dimension‑fixed (from $R(q_0)=-2(n-1)=-6$ and isotropic rate $n-1=3$), and the argument is independent of $k$, of the lattice covolume, and of the interval length.

## 3. The forced version with a sharp universal threshold

Let $E=\operatorname{Ric}+3g$, $\|E\|_{\mathrm{op}}\le\delta$. The forced equations (Step 78) are
$$
(Vu)'=V(3-K-E_z),\qquad (Vd')'=V\!\left(2K\coth d-(E_{\omega_1}-E_{\omega_2})\right),
$$
and the forced Gauss relation at the face gives $K(0)=6-(\operatorname{tr}E-2E_{rr})(0)$, so $|K(0)-6|\le 6\delta$, i.e. $K(0)\ge 6-6\delta$.

Run both monotonicities as a simultaneous continuity (open–closed) bootstrap on the maximal set where $u\le0$ and $d'\ge0$:

- $u\le0,\ d'\ge0 \Rightarrow (\log K)'\ge0 \Rightarrow K\ge K(0)\ge 6-6\delta$.
- Since $\coth d>1$ for all $d>0$ (this is the crucial uniform amplifier, valid however small $d$ is),
$$
(Vd')'\ge 2V(6-6\delta)\cdot 1-2V\delta=V(12-14\delta)>0\quad(\delta<\tfrac{6}{7}),
$$
so $Vd'$ strictly increases from $0$: $d'>0$, $d\ge d_0>0$ maintained.
- $(Vu)'=V(3-K-E_z)\le V(3-(6-6\delta)+\delta)=V(-3+7\delta)<0\quad(\delta<\tfrac{3}{7})$,
so $Vu<0$: $u<0$ maintained.

The binding constant is the last line. Therefore

$$
\boxed{\ \text{If }\|\operatorname{Ric}+3g\|_{\mathrm{op}}\le\delta<\tfrac{3}{7}\ \text{ everywhere, no rotating‑eigenframe VII}_0\ \text{solution from a reflection face ever has }u>0.\ }
$$

Because a vanishing‑defect graph connector needs $\delta\to0$ and an almost‑umbilic entry ($u\to1$ among the eigenvalues), the entire family is closed off for the graph route, not merely the exact locus. The threshold $3/7$ is geometry‑, $k$‑, and length‑independent.

## 4. Why no stronger dimension‑free constant is the point (not a shortfall)

The obstruction is not a fitting deficit; it is the exact factor‑two relation $K(0)/3=2$ forced by the Gauss relation together with $\coth d>1$. These two facts are dimension‑robust and involve no free geometric parameter, which is exactly why the barrier cannot be relaxed by tuning $k$, the lattice, $d_0$, or the interval. Equivalently: in this cohomogeneity‑one family the mandatory intrinsic scalar curvature $-6$ can be produced **only** by the twist $K$, and the twist has no sink — $(\log K)'$ can be made $<0$ only by $u>0$, while $u>0$ is itself blocked by $K>3$. The system is self‑locking. Stating the explicit $\delta^\*=3/7$ and $K'(r)>0$ is the strongest true output; asking for a construction inside this family is asking to violate the first integral $(uv+vw+wu)+K/2=3$ at the face.

A worthwhile inexpensive check that would sharpen the collapse picture: integrate the exact system from $(u,v,w)=0,\ K(0)=6$ for several $d_0$ and confirm the predicted signs $u<0,\ K'>0,\ d'>0$ and finite‑$r$ blow‑up of $K$ (a verification of the monotonicities, not an optimization). The predicted invariants $Vd'\uparrow$, $K\uparrow$, $Vu\downarrow$ are exact and give a stringent internal consistency test for the solver.

## 5. What genuinely new mechanism a working core must supply

The exclusion pinpoints the missing ingredient with unusual precision: a **sink for the mandatory sub‑zero slice curvature** that is decoupled from the contraction of a single circle. Three concrete, source‑grounded routes each remove one feature that makes the VII₀ trap airtight; each comes with a testable equation.

**(A) A genuine two‑dimensional base carrying the curvature, not the twist.** VII₀ is cohomogeneity‑one; the quotient is the single coordinate $r$, so the required $R(q_0)=-6$ has nowhere to live except $K$. Replace it by a warped product of a $T^2$ fiber over a $2$‑surface $\Sigma$ whose own curvature $R_\Sigma<0$ supplies the intrinsic scalar deficit. Then the analog of $(Vu)'=V(3-K)$ acquires a base‑Laplacian term, and the source of $u'$ is no longer a pure algebraic potential; its sign can change. The decisive test is to derive the momentum identity for the fiber scale with the $\Delta_\Sigma$ term present and check whether $\int_\Sigma$ of the source can vanish while $u>0$. This is the cohomogeneity‑two generalization of the present ODE and is precisely the structure underlying the Li–Liu Type‑I warped product, whose curvature is distributed over the $T^2$ rather than concentrated in one twist.

**(B) Spatial diffusion of anisotropy (inhomogeneous slices).** Promote $d=d(r)$ to $d=d(r,z)$ on the $2$‑dimensional quotient. The transport becomes the elliptic identity (Step 76 (3.1))
$$
\operatorname{div}_\gamma(\rho\nabla_\gamma d)=2\rho K\coth d-\rho(E_{\omega_1}-E_{\omega_2}),
$$
in which the added $\partial_{zz}$ term lets anisotropy redistribute and decay pointwise even as its weighted total is conserved and exported. This is exactly the dilution the Step 76 §4 mode $\psi_k$ exhibits: $e^{2t}\psi_k'\to k\sinh k$ finite while the unweighted shear $|S-I|^2$ decays like $e^{-4r}$. In the homogeneous ODE the same source term $2VK\coth d$ has no Laplacian to cancel against, which is why $Vd'$ is monotone. The testable object is $d(r,z)=\sum_k A_k\psi_k(r)\cos(kz)$ solving the inhomogeneous system with $K$ driven toward $0$ and $u>0$ simultaneously; success requires the frequency‑transport regularity flagged in Step 76 (4.7).

**(C) Off‑diagonal orbit‑shape motion.** The uniform amplifier $\coth d>1$ is special to the diagonal geodesic in $\mathcal P=\mathrm{SL}(2,\mathbb R)/\mathrm{SO}(2)$. A path that engages the twist generator (the Li–Liu Type‑I datum $p$, Step 76 (9.2)) samples a part of $\mathcal P$ where the analog source need not exceed the isotropic rate, so $K$ can descend. This is also demanded independently by the Step 77 result that a reflected core must be non‑anti‑self‑dual: the rotating **diagonal** VII₀ locus is too special in Weyl type, and only genuine off‑diagonal motion (or the base/inhomogeneity of (A),(B)) can reach the non‑ASD sector. The concrete test is the matrix transport $(V\,U^{-1}U')'=$ source for $\det U=1$, $U:S^1\to\mathcal P$, and whether the twist component of the source is sign‑indefinite, unlike the strictly positive $2VK\coth d$ of the diagonal case.

The unifying reading: the anisotropy energy floor $\langle d_s^2\rangle_\rho\ge12$ at the face must flow somewhere. In cohomogeneity‑one it is forced to grow (the lemma of §2). A viable core must let it flow out to a Yamabe‑sub‑zero PE end through spatial transport or base curvature — which is exactly the covariance‑transport / weighted‑stress picture of Steps 76–77. The present result therefore both closes the rotating VII₀ route with an explicit universal $\delta^\*=3/7$ and identifies the diffusion/base‑curvature sink as the single structural feature any successful connector must add. None of this settles the sign‑plus branch or the higher‑dimensional quantifiers of the original proposition; it sharpens the sub‑zero four‑dimensional core route from a finite‑tolerance search into a precisely located structural demand.