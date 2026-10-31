# Step 35: Index-level tensor variation and Hessian-a contraction tensors

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

This note derives the two Hessian-a contraction tensors that the fixed-exponent
module (Step 34) depends on, proves their derivative structures from first
principles, and verifies the complete curvature/defect power inequality at the
tensor level.  It resolves obligations 1–2 from Step 34 §7.

**Convention.**  All-lower curvature \(R_{ijkl}=g_{l\alpha}R_{ijk}{}^\alpha\),
Ricci \(R_{ij}=g^{kl}R_{kilj}\), norm
\(|\operatorname{Rm}|^2=R_{ijkl}R^{ijkl}\), dimension \(n=4\).
Defect \(E_{ij}=R_{ij}+g_{ij}\), scalar defect
\(\tau=\operatorname{tr}E=R+4\).  Flow:
\[
\partial_tg_{ij}=h_{ij}=-2aE_{ij},
\qquad a=\chi^2,\qquad \chi\in C^\infty(M,[0,1]).
\tag{0.1}
\]
Cutoff gradient: \(|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}\).
Stationary collar: \(a=\nabla a=0\) on \(\operatorname{supp}\nabla\eta\).

---

## 1. Scaling test and normalization benchmark

Under \(\partial_tg=-2g\) (i.e.\ \(a=1\), \(E=g\), Ricci = 0):

- **Connection**: \(\partial_t\Gamma^k_{ij}=0\) because \(\nabla g=0\).
  Hence \(\partial_tR_{ijk}{}^\ell=0\).
- **Lowering**: \(\partial_tR_{ijkl}=R_{ijk}{}^\alpha\partial_tg_{\alpha l}
  =-2R_{ijkl}\).
- **Inverse metric**: \(\partial_tg^{ij}=2g^{ij}\).
- **Norm**: \(\partial_t|R|^2
  =2R^{ijkl}\partial_tR_{ijkl}+4\cdot2\cdot g^{ij}\cdot W_{ij}
  =-4|R|^2+8|R|^2=+4|R|^2\),
  where \(W_{pq}=R_p{}^{jkl}R_{qjkl}\), using
  \(W_{pq}g^{pq}=|R|^2\).
- **Volume**: \(\partial_td\mu=-4\,d\mu\).
- **\(\int|R|^2d\mu\)**: rate \(=4-4=0\).  **Invariant** in dimension 4. ✓

This confirms: no net pointwise damping from conformal/normalization.
The term \(CaF^3\) in the reaction must absorb the \(+4|R|^2\)
normalization contribution together with the Hamilton quadratic,
**not** be treated as a separate damping.

---

## 2. All-lower curvature variation under \(h=-2aE\)

The standard all-lower variation is (see e.g.\ Besse, Theorem 1.174):
\[
\partial_tR_{ijkl}
=\underbrace{g_{l\alpha}[\nabla_j(\delta\Gamma^\alpha_{ik})
-\nabla_i(\delta\Gamma^\alpha_{jk})]}_{\text{(1,3) variation, lowered}}
+\underbrace{R_{ijk}{}^\alpha h_{\alpha l}}_{\text{lowering variation}},
\tag{2.1}
\]
with connection variation
\[
\delta\Gamma^\alpha_{ik}
=\tfrac12g^{\alpha\beta}(\nabla_ih_{k\beta}+\nabla_kh_{i\beta}
-\nabla_\beta h_{ik}).
\tag{2.2}
\]

**Expanding (2.1) for \(h=-2aE\).**

After the product-rule expansion of \(\nabla_j\nabla_k(aE_{il})\) etc.,
the variation separates into four structural types:

\[
\partial_tR_{ijkl}
=\underbrace{a\cdot(\text{standard Ricci-flow variation with }E)
}_{\text{Type P: principal}}
+\underbrace{\text{Type G: gradient-cutoff}
}_{\nabla a\cdot\nabla E}
+\underbrace{\text{Type H: Hessian-cutoff}
}_{(\nabla^2a)\cdot E}
+\underbrace{\text{Type N: normalization from }+g
}_{\text{algebraic}}.
\tag{2.3}
\]

### 2.1 Type P (principal)

The second-derivative and algebraic terms with the factor \(a\):
\[
a\bigl[\text{Hamilton's } \partial_tR_{ijkl}\big|_{\text{Ricci flow}}\bigr]
=a\bigl[\Delta R_{ijkl}+2(B_{ijkl}-B_{ijlk}-B_{iljk}+B_{ilkj})
-R_i{}^pR_{pjkl}-R_j{}^pR_{pikl}\bigr],
\]
where \(B_{ijkl}=R_{ipjq}R_k{}^p{}_l{}^q\).

This uses \(\nabla E=\nabla\operatorname{Ric}\) (since \(\nabla g=0\)),
so the principal \(a\nabla^2E\) terms coincide exactly with the Ricci-flow
double-divergence of \(\operatorname{Ric}\).

### 2.2 Type G (gradient-cutoff)

From the product rule on \(\nabla(aE)\):
\[
G_{ijkl}=-[(\nabla_ja)(\nabla_kE_{il})+(\nabla_ka)(\nabla_jE_{il})
+\cdots\text{ (8 terms from 4 pairs)}].
\tag{2.4}
\]
Each term has the structure \(|\nabla a||\nabla\operatorname{Ric}|\).

### 2.3 Type N (normalization)

The \(+g\) in \(E=\operatorname{Ric}+g\) modifies the algebraic/lowering terms.
After the detailed calculation:
\[
\text{Type N contribution to }\partial_tR_{ijkl}=-2aR_{ijkl}.
\tag{2.5}
\]
**Proof:** In the lowering variation, \(R_{ijk}{}^\alpha h_{\alpha l}
=-2aR_{ijk}{}^\alpha E_{\alpha l}
=-2a(R_{ijk}{}^\alpha R_{\alpha l}+R_{ijkl})\).
The commutator terms contribute
\(\tfrac12(R_{ijk}{}^sE_{sl}+R_{ijl}{}^sE_{ks})\).
For \(E_l^p=R_l^p+\delta_l^p\):
\[
R_{ijkp}E_l^p+R_{ijlp}E_k^p
=R_{ijkp}R_l^p+R_{ijlp}R_k^p+R_{ijkl}-R_{ijkl}
=R_{ijkp}R_l^p+R_{ijlp}R_k^p.
\]
The \(\pm R_{ijkl}\) terms cancel by the skew symmetry
\(R_{ijlk}=-R_{ijkl}\).  Hence the \(+g\) produces **no** additional
quadratic curvature term in the algebraic part, and only the
lowering variation \(-2aR_{ijkl}\).

This gives the **normalization reaction** in \(\partial_t|R|^2\):
\(2R^{ijkl}\cdot(-2aR_{ijkl})=-4a|R|^2\).  Combined with the
\(+8a\cdot W_{pq}E^{pq}\) from inverse-metric variation
(where \(W_{pq}E^{pq}=W_{pq}R^{pq}+|R|^2\)):
\[
\text{normalization + metric variation}
=4a|R|^2+8aW_{pq}R^{pq}\le CaF^3.
\tag{2.6}
\]
At \(\operatorname{Ric}=0\): \(+4a|R|^2\), matching the scaling test.

### 2.4 Type H (Hessian-cutoff)

The Hessian-of-\(a\) terms in the variation (2.1) are:
\[
(H_a)_{ijkl}
=-(\nabla_j\nabla_ka)E_{il}-(\nabla_i\nabla_la)E_{jk}
+(\nabla_i\nabla_ka)E_{jl}+(\nabla_j\nabla_la)E_{ik}.
\tag{2.7}
\]
This has the algebraic symmetries of a curvature tensor.

---

## 3. The curvature Hessian-a contraction tensor

### 3.1 Derivation

The contribution of Type H to \(\partial_t|R|^2\) is:
\[
\Sigma_H^{\mathrm{Rm}}
=2R^{ijkl}(H_a)_{ijkl}
=2R^{ijkl}\bigl[-A_{jk}E_{il}-A_{il}E_{jk}+A_{ik}E_{jl}+A_{jl}E_{ik}\bigr],
\tag{3.1}
\]
where \(A_{pq}=\nabla_p\nabla_qa\) is the Hessian of \(a\).

**Using pair symmetry** \(R^{ijkl}=R^{klij}\):

- Terms 1 and 2 are equal: swap \((ij)\leftrightarrow(kl)\) in
  \(-R^{ijkl}A_{jk}E_{il}\to -R^{klij}A_{lk}E_{kj}=-R^{ijkl}A_{il}E_{jk}\)
  (relabel, use \(A_{lk}=A_{kl}\), \(E_{kj}=E_{jk}\)).

- Terms 3 and 4 are equal by the same pair exchange.

Therefore:
\[
\Sigma_H^{\mathrm{Rm}}
=4R^{ijkl}(A_{ik}E_{jl}-A_{jk}E_{il}).
\tag{3.2}
\]

**Using first-pair antisymmetry** \(R^{ijkl}=-R^{jikl}\):

In the second term, relabel the dummy \(j\to i'\), \(i\to j'\):
\[
R^{ijkl}A_{jk}E_{il}
=R^{j'i'kl}A_{i'k}E_{j'l}
=-R^{i'j'kl}A_{i'k}E_{j'l}
=-R^{ijkl}A_{ik}E_{jl}.
\]
Hence \(A_{ik}E_{jl}-A_{jk}E_{il}=2\cdot A_{ik}E_{jl}\)
after summing the two copies, and:
\[
\boxed{
\Sigma_H^{\mathrm{Rm}}
=8A_{pq}B_{\mathrm{curv}}^{pq},
\qquad
B_{\mathrm{curv}}^{pq}=R^{p}{}_{j}{}^{q}{}_{l}\,E^{jl}.}
\tag{3.3}
\]

### 3.2 Size and derivative structure

**Size.**
\[
|B_{\mathrm{curv}}^{pq}|
\le|\operatorname{Rm}|\cdot|E|\le CF^2.
\tag{3.4}
\]

**Derivative.**
\[
\nabla_rB_{\mathrm{curv}}^{pq}
=(\nabla_rR^{p}{}_{j}{}^{q}{}_{l})E^{jl}
+R^{p}{}_{j}{}^{q}{}_{l}(\nabla_rE^{jl}).
\tag{3.5}
\]
Since \(|\nabla E|=|\nabla\operatorname{Ric}|\le C|\nabla\operatorname{Rm}|\)
and \(|E|\le CF\):
\[
\boxed{
|\nabla B_{\mathrm{curv}}|
\le|\nabla\operatorname{Rm}|\cdot|E|+|\operatorname{Rm}|\cdot|\nabla E|
\le CF|\nabla\operatorname{Rm}|.}
\tag{3.6}
\]
This is the derivative-structure bound (Step 34, eq.\ 2.10).  It holds
because \(B_{\mathrm{curv}}\) is an algebraic contraction of \(\operatorname{Rm}\)
and \(E\), both of which have controlled gradients.

### 3.3 Signed IBP for the curvature power inequality

Testing \(\partial_t|R|^2\) with the weight
\(\frac{p}{2}\eta^2a^{p-2}F^{p-2}\) and integrating, the Hessian-a
contribution becomes:
\[
T_H^{\mathrm{Rm}}
=4p\int\eta^2a^{p-2}F^{p-2}A_{pq}B_{\mathrm{curv}}^{pq}\,d\mu.
\tag{3.7}
\]
Integrate by parts, moving one covariant derivative from \(A_{pq}=\nabla_p\nabla_qa\)
to the rest.  Writing \(A_{pq}=\nabla_p(\nabla_qa)\):
\[
T_H^{\mathrm{Rm}}
=-4p\int(\nabla_qa)\nabla_p\bigl[\eta^2a^{p-2}F^{p-2}B_{\mathrm{curv}}^{pq}\bigr]\,d\mu.
\tag{3.8}
\]
The derivative hits four factors.  We bound each:

**(i) \(\nabla_p\eta^2=2\eta\nabla_p\eta\):**
Vanishes because \(a=0\) on \(\operatorname{supp}\nabla\eta\).

**(ii) \(\nabla_p(a^{p-2})=(p-2)a^{p-3}\nabla_pa\):**
\[
|(\nabla_qa)(p-2)a^{p-3}(\nabla_pa)F^{p-2}B^{pq}|
\le(p-2)a^{p-3}|\nabla a|^2F^{p-2}\cdot CF^2
\le Cpr^{-2}a^{p-2}F^p.
\]
Integrated: \(\le Cpr^{-2}K_p\).

**(iii) \(\nabla_p(F^{p-2})=(p-2)F^{p-3}\nabla_pF\):**
\[
|(\nabla_qa)(p-2)a^{p-2}F^{p-3}(\nabla_pF)B^{pq}|
\le Cpa^{p-2}|\nabla a|F^{p-1}|\nabla F|.
\]
Young \((2,2)\): \(\le\varepsilon a^{p-1}F^{p-2}|\nabla F|^2
+C_\varepsilon p^2a^{p-3}|\nabla a|^2F^p
=\varepsilon D_p^F\text{-density}+C_\varepsilon p^2r^{-2}K_p\text{-density}\).

**(iv) \(\nabla_pB_{\mathrm{curv}}^{pq}\):**
\[
|(\nabla_qa)a^{p-2}F^{p-2}\nabla_pB^{pq}|
\le a^{p-2}|\nabla a|F^{p-2}\cdot CF|\nabla\operatorname{Rm}|
=C|\nabla a|a^{p-2}F^{p-1}|\nabla\operatorname{Rm}|.
\]
Young \((2,2)\): \(\le\varepsilon a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
+C_\varepsilon a^{p-3}|\nabla a|^2F^p
=\varepsilon D_p^{\mathrm{Rm}}\text{-density}+C_\varepsilon r^{-2}K_p\text{-density}\).

**Combining (i)–(iv)** with outer factor \(4p\):
\[
\boxed{
|T_H^{\mathrm{Rm}}|
\le\varepsilon p\bigl[D_p^{\mathrm{Rm}}+(p-2)D_p^F\bigr]
+C_\varepsilon p^3r^{-2}K_p.}
\tag{3.9}
\]
The full-tensor dissipation \(D_p^{\mathrm{Rm}}\) appears from route (iv) via
the derivative structure (3.6).  The radial dissipation \(D_p^F\) appears from
route (iii).  **Both are available from the Bochner principal term** (§4.1).

---

## 4. Assembly of the curvature power inequality

### 4.1 Dissipation

From the diffusion part \(a\Delta|R|^2\) tested with
\(\tfrac{p}{2}\eta^2a^{p-2}F^{p-2}\) and integrated by parts:

- Bochner: \(-pD_p^{\mathrm{Rm}}\).
- Radial from \(\nabla(a^{p-2})\) hitting \(\nabla(F^2)\):
  after Young, net \(-p(p-2)D_p^F+Cp^2r^{-2}K_p\).
- Cross term \(\nabla\eta\): vanishes.

Pre-absorption dissipation:
\[
\boxed{-pD_p^{\mathrm{Rm}}-p(p-2)D_p^F.}
\tag{4.1}
\]

### 4.2 Reaction

The Hamilton quadratic (\(\le C|R|^3\le CF^3\)), normalization
(\(\le CaF^3\), see (2.6)), and volume form
(\(|a\tau|\le CaF\), contributes \(Ca^{p-1}F^{p+1}\)) all have the
schematic size \(Ca^{p-1}F^{p+1}\) after testing.

By the three-factor Hölder identity (Step 34 eq.\ 2.12) with exponents
\((3,3,3)\) on \(\operatorname{supp}a\):
\[
a^{p-1}F^{p+1}=(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}(z_p^2)^{2/3},
\]
where \(z_p=\eta a^{(p-1)/2}F^{p/2}\).  Hölder, Sobolev, and Young:
\[
Cp\int a^{p-1}F^{p+1}
\le\varepsilon\bigl[pD_p^{\mathrm{Rm}}+p(p-2)D_p^F\bigr]
+C_\varepsilon p^N{\mathcal S}^2YK_p
+C_\varepsilon p^Nr^{-2}K_p.
\tag{4.2}
\]
(See Step 34 eq.\ 2.13 for details; \(N\le5\) is universal.)

### 4.3 Cutoff gradient terms (Type G)

By Young against \(D_p^{\mathrm{Rm}}\) and \(D_p^F\):
\[
|\text{Type G contribution}|
\le\varepsilon p\bigl[D_p^{\mathrm{Rm}}+(p-2)D_p^F\bigr]
+C_\varepsilon p^Nr^{-2}K_p.
\tag{4.3}
\]

### 4.4 Final curvature power inequality

Choosing \(\varepsilon\) small, absorbing into the dissipation (4.1):
\[
\boxed{
K_p'+c\bigl[pD_p^{\mathrm{Rm}}+p(p-2)D_p^F\bigr]
\le Cp^N(r^{-2}+1+{\mathcal S}^2Y)K_p,
\qquad p\ge3.}
\tag{4.4}
\]
The lower-order source from \(F^2=1+|R|^2\) contributes \(Cp(1+r^{-2})K_p\),
absorbed into the RHS.

---

## 5. Defect variation from the Ricci linearization

### 5.1 Ricci linearization formula

The linearization of Ricci under \(h\) is (Besse, Theorem 1.174):
\[
2(D\operatorname{Ric})[h]_{ij}
=g^{kl}\bigl(-\nabla_k\nabla_lh_{ij}
+\nabla_k\nabla_ih_{jl}+\nabla_k\nabla_jh_{il}
-\nabla_i\nabla_jh_{kl}\bigr)
+2R_{ikjl}h^{kl}-R_i{}^kh_{kj}-R_j{}^kh_{ki}.
\tag{5.1}
\]

For \(h=-2aE\), the Hessian-of-\(a\) terms arise from the four
second-derivative terms in (5.1) after the product rule
\(\nabla^2(aE)=a\nabla^2E+\nabla a\otimes\nabla E
+\nabla E\otimes\nabla a+(\nabla^2a)\cdot E\).

### 5.2 Extracting the Hessian-a part of \(\partial_tR_{ij}\)

From each of the four terms in (5.1):

1. \(-g^{kl}\nabla_k\nabla_l(aE_{ij})\): Hessian-\(a\) part \(=
   -(\Delta a)E_{ij}\).  In the Ricci variation with factor \(+2\) on
   the LHS, this contributes \(+2(\Delta a)E_{ij}\) to
   \(2\partial_tR_{ij}\).

2. \(+g^{kl}\nabla_k\nabla_i(aE_{jl})\): Hessian part
   \(=g^{kl}(\nabla_k\nabla_ia)E_{jl}=(\nabla^l\nabla_ia)E_{jl}\).
   With factor \(-2\) from \(h=-2aE\): contributes
   \(-2(\nabla^l\nabla_ia)E_{jl}\) to \(2\partial_tR_{ij}\).

3. By symmetry with (2): contributes
   \(-2(\nabla^l\nabla_ja)E_{il}\).

4. \(-g^{kl}\nabla_i\nabla_j(aE_{kl})\): Hessian part
   \(=-(\nabla_i\nabla_ja)\tau\).  Contributes
   \(+2(\nabla_i\nabla_ja)\tau\).

**Assembling** (dividing \(2\partial_tR_{ij}\) by 2):
\[
(\partial_tR_{ij})\big|_{\nabla^2a}
=(\Delta a)E_{ij}
-(\nabla_i\nabla^la)E_{jl}
-(\nabla_j\nabla^la)E_{il}
+(\nabla_i\nabla_ja)\tau.
\tag{5.2}
\]
Adding \(\partial_tg_{ij}=-2aE_{ij}\) (no Hessian-\(a\) term):
\[
(\partial_tE_{ij})\big|_{\nabla^2a}
=(\Delta a)E_{ij}
-A_i{}^lE_{jl}
-A_j{}^lE_{il}
+A_{ij}\tau.
\tag{5.3}
\]

### 5.3 Contribution to \(\partial_ts\)

The Hessian-\(a\) part of \(\partial_t|E|^2\) is
\(2E^{ij}(\partial_tE_{ij})|_{\nabla^2a}\) (the \(\partial_tg^{-1}\)
terms are algebraic in \(a\), not in \(\nabla^2a\)):
\[
\Sigma_H^E
=2E^{ij}\bigl[(\Delta a)E_{ij}-A_i{}^lE_{jl}-A_j{}^lE_{il}+A_{ij}\tau\bigr].
\tag{5.4}
\]
Computing:
\begin{align}
2E^{ij}(\Delta a)E_{ij}&=2(\Delta a)s, \tag{5.4a}\\
-2E^{ij}A_i{}^lE_{jl}&=-2A_{il}(E^2)^{il}, \tag{5.4b}\\
-2E^{ij}A_j{}^lE_{il}&=-2A_{jl}(E^2)^{jl}=-2A_{il}(E^2)^{il}, \tag{5.4c}\\
2E^{ij}A_{ij}\tau&=2\tau\langle A,E\rangle. \tag{5.4d}
\end{align}
Therefore:
\[
\boxed{
\Sigma_H^E=2A_{pq}B_{\mathrm{def}}^{pq},
\qquad
B_{\mathrm{def}}^{pq}
=sg^{pq}+\tau E^{pq}-2(E^2)^{pq}.}
\tag{5.5}
\]

**Equivalently:** \(B_{\mathrm{def}}^{pq}=|E|^2g^{pq}
+(\operatorname{tr}E)E^{pq}-2E^{pi}E_i{}^q\).

**Cross-check with A03 Step 35 (eq.\ 3.5b):**
A03 writes \(B^{ij}=2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j\).
This is exactly \(2B_{\mathrm{def}}^{ij}\), and appears because A03's
test function \(q=3\eta^2a^4s^2\) includes a factor \(3\) and the
chain rule \(3s^2\cdot\Sigma_H^E=3s^2\cdot2A_{pq}B_{\mathrm{def}}^{pq}
=6s^2A_{pq}B_{\mathrm{def}}^{pq}\).  In A03's convention,
\(T_H=\int A_{ij}B^{ij}(q)\) with \(B^{ij}(q)=q\cdot2B_{\mathrm{def}}^{ij}\).
The factor-of-2 match is confirmed. ✓

---

## 6. The defect Hessian-a contraction tensor

### 6.1 Quadratic vanishing at \(E=0\)

Every term in \(B_{\mathrm{def}}^{pq}\) is at least quadratic in \(E\):
\[
s=|E|^2,\quad \tau E^{pq}=(\operatorname{tr}E)E^{pq},
\quad (E^2)^{pq}=E^{pi}E_i{}^q.
\]
Therefore:
\[
B_{\mathrm{def}}^{pq}\big|_{E=0}=0.
\tag{6.1}
\]
This is the critical property: **no bare Hessian-\(a\) source** at \(E=0\).
The defect equation is genuinely homogeneous.

### 6.2 Size bound
\[
|B_{\mathrm{def}}|\le|E|^2\cdot n+|\operatorname{tr}E|\cdot|E|
+2|E|^2\le Cs.
\tag{6.2}
\]

### 6.3 Derivative structure

\[
\nabla_rB_{\mathrm{def}}^{pq}
=(\nabla_rs)g^{pq}+(\nabla_r\tau)E^{pq}+\tau(\nabla_rE^{pq})
-2\nabla_r(E^{pi}E_i{}^q).
\tag{6.3}
\]
Since \(\nabla s=2\langle E,\nabla E\rangle\),
\(\nabla\tau=\operatorname{tr}(\nabla E)\) (so \(|\nabla\tau|\le C|\nabla E|\)),
and \(|\nabla(E^2)|\le2|E||\nabla E|\), **every term** in (6.3) is bounded
by \(C|E||\nabla E|\).  In particular, the \((\nabla\tau)E\) term contributes
\(|\nabla\tau|\cdot|E|\le C|\nabla E|\cdot|E|=Cs^{1/2}|\nabla E|\), not a bare
\(C|\nabla E|\).  Hence:
\[
\boxed{
|\nabla B_{\mathrm{def}}|
\le C|E||\nabla E|
=Cs^{1/2}|\nabla E|.}
\tag{6.4}
\]
(TTCS correction: the earlier draft included a spurious \(+C|\nabla E|\) from
mishandling \(\nabla\tau\); since \(\nabla\tau=\operatorname{tr}(\nabla E)\)
rather than \(\nabla\operatorname{Rm}\)-bounded, it is not needed.)

### 6.4 Signed IBP for \(J_6\)

After testing \(\partial_ts^3=3s^2\partial_ts\) with \(\eta^2a^4\) and
integrating, the Hessian-a contribution (from §5.3 via the chain rule) is:
\[
T_H^E
=6\int\eta^2a^4s^2A_{pq}B_{\mathrm{def}}^{pq}\,d\mu.
\tag{6.6}
\]
Integrate by parts as in §3.3:
\[
T_H^E=-6\int(\nabla_qa)\nabla_p\bigl[\eta^2a^4s^2B_{\mathrm{def}}^{pq}\bigr]\,d\mu.
\]
The four routes:

**(i)** \(\nabla_p\eta^2\): vanishes (\(a=0\) on \(\operatorname{supp}\nabla\eta\)).

**(ii)** \(\nabla_p(a^4)=4a^3\nabla_pa\): gives
\(a^3|\nabla a|^2s^2|B|\le4a^4r^{-2}|d\chi|^2\cdot Cs^3
\le Cr^{-2}a^4s^3\), integrating to \(Cr^{-2}J_6\).

**(iii)** \(\nabla_p(s^2)=2s\nabla_ps=4sE^{ij}\nabla_pE_{ij}\): gives
\(|\nabla a|a^4\cdot4s^{3/2}|E||\nabla E|\cdot|B|\le
C|\nabla a|a^4s^{5/2}|\nabla E|\).
Young: \(\le\varepsilon X_6+C_\varepsilon r^{-2}J_6\).

**(iv)** \(\nabla_pB_{\mathrm{def}}^{pq}\): using (6.4),
\(|\nabla a|a^4s^2\cdot Cs^{1/2}|\nabla E|\le
C|\nabla a|a^4s^{5/2}|\nabla E|\).
Same structure as (iii): \(\le\varepsilon X_6+C_\varepsilon r^{-2}J_6\).

**Combined:**
\[
\boxed{
|T_H^E|\le\varepsilon X_6+C_\varepsilon r^{-2}J_6.}
\tag{6.7}
\]
Exactly as in A03 Step 35, eq.\ (3.5d).  ✓

---

## 7. Summary of proved tensor identities

### 7.1 Curvature

The Hessian-\(a\) contraction tensor for \(\partial_t|R|^2\) is
\(B_{\mathrm{curv}}^{pq}=R^p{}_{j}{}^q{}_{l}E^{jl}\),
satisfying \(|B|\le CF^2\) and \(|\nabla B|\le CF|\nabla\operatorname{Rm}|\).
Via signed IBP, its contribution to \(K_p'\) is absorbed by
\(\varepsilon p(D_p^{\mathrm{Rm}}+(p-2)D_p^F)+Cp^3r^{-2}K_p\).

The complete curvature power inequality (4.4) holds at the tensor level
with dissipation \(-pD_p^{\mathrm{Rm}}-p(p-2)D_p^F\), reaction coefficient
\({\mathcal S}^2Y\), polynomial \(p\)-growth \(p^N\) (\(N\le5\)), and
Hessian absorption by signed IBP (not an assumed evolving pointwise bound).

### 7.2 Defect

The Hessian-\(a\) contraction tensor for \(\partial_t|E|^2\) is
\(B_{\mathrm{def}}^{pq}=|E|^2g^{pq}+(\operatorname{tr}E)E^{pq}
-2(E^2)^{pq}\), satisfying \(B|_{E=0}=0\), \(|B|\le Cs\),
and \(|\nabla B|\le Cs^{1/2}|\nabla E|\).
Via signed IBP, its contribution to \(J_6'\) is absorbed by
\(\varepsilon X_6+Cr^{-2}J_6\).

This confirms A03 Step 35's formula and the complete \(J_6\) persistence
estimate with constant Gronwall coefficient \(C(1+r^{-2})\).

### 7.3 What this establishes and what remains

**Established:**
- the curvature power inequality (4.4) is now proved at the index level;
- the defect Hessian-a tensor matches A03 from first principles;
- both derivative structures are proved, not assumed;
- the scaling test passes at the formula level.

**Still open:**
- simultaneous first-exit bootstrap (A03 Step 35 assembly note);
- degenerate-flow existence (A03 Step 35 companion note);
- cutoff-jet continuation (A03 Step 35 companion note, #339);
- terminal calibration and exponential-pullback selection;
- even completion of the above covers only the near-critical
  Ishida–LeBrun negative four-dimensional laboratory.

---

## 8. Verification

`workspace/scripts/step35_tensor_hessian_verification.py` — checks
the tensor identities, derivative structures, dissipation coefficients,
scaling test, and cross-consistency with A03.
