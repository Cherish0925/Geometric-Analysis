# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 32,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step32_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step32_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify Lemmas V, N, and W in the Step-31 note. Derive all constants and signs from the stated diagonal chiral and Ricci identities. In particular: (i) determine whether the pointwise conclusion dP_hat/dt = b'_pm + nonnegative density and the stronger integral max{0,b_+',b_-'} bound are valid simultaneously; (ii) check b_- normalization at the O(-1) bolt; (iii) check C identities and whether scalar -24 is legitimately without loss for the exact-ended diagonal infimum; (iv) inspect Lemma W's first-barrier proof including the case S(T)>A, and state a corrected rigorous version if needed. Distinguish exact theorem from numerical support.

## Integrated Scientific Memo

# Verification of Lemmas V, N, and W

## 1. Lemma V: simultaneous chiral bounds

Let
\[
p(t):=\frac{d}{dt}\widehat P([a,t])
=\frac{W}{4}|\Ric^\circ|^2\ge0,
\qquad d\mu_g=2\pi^2W\,dt.
\]
The two localized chiral identities give, simultaneously,
\[
p=\mathfrak b_+'+\omega_+
=\mathfrak b_-'+\omega_-,
\]
with
\[
\omega_\pm
=W|W^\pm|^2+\frac{W}{48}s^2\ge0
\]
when \(|W^\pm|^2,s^2\) denote pointwise four-dimensional norms. Equivalently, one may retain Step 31’s factors only if “density” already includes the orbit-volume normalization \(2\pi^2\).

Therefore
\[
\boxed{p(t)\ge \max\{0,\mathfrak b_+'(t),\mathfrak b_-'(t)\}}
\]
pointwise. The two chiral inequalities are compatible because both represent the same \(p\) by adding different nonnegative densities. What is not justified is the stronger sum
\((\mathfrak b_+')_++(\mathfrak b_-')_+\).

Integrating,
\[
\boxed{
\widehat P([a,b])
\ge \int_a^b\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt
\ge
\max\{V^+(\mathfrak b_+),V^+(\mathfrak b_-)\}.
}
\]
Indeed, for absolutely continuous \(f\),
\[
V^+(f)=\int(f')_+\,dt,
\]
and the integrand dominates both positive parts. Smooth bolt expansions permit applying the argument on \([\varepsilon,b]\) and then taking \(\varepsilon\downarrow0\).

Thus **Lemma V is exact and valid as stated**, modulo clarifying the density normalization.

A useful strengthening, when \(s\equiv-24\), is
\[
p=\mathfrak b_\pm'+12W+W|W^\pm|^2.
\]
Hence, defining
\[
\beta_\pm(t):=\mathfrak b_\pm(t)+12\int_{t_0}^tW(\tau)\,d\tau,
\]
one has
\[
p\ge \max\{0,\beta_+',\beta_-'\}.
\]
This is stronger than Lemma V, although it applies to the scalar-normalized trajectory itself; the charges are not conformally invariant.

### Scope of the Step-31 consequences

The bound from the tabulated state \(\mathfrak b_-=8.54957\),
\[
\widehat P\ge8.54957-7\approx1.54957,
\]
is exact conditional on passing through that state, apart from the floating-point evaluation of its charge. It does not exclude all high-shear trajectories.

Likewise, the collapsed value \(\mathfrak b_+\to-2\) is guaranteed for controlled near-biaxial Hopf collapse with bounded normalized jets, not for arbitrary sheared collapse. For a charge-defined collapsed section, the CH threshold is
\[
2-9\sinh^4\tau<-2+p_*
\quad\Longrightarrow\quad
\tau>0.7012\ldots .
\]

---

## 2. \(O(-1)\) bolt normalization

Let the \(h\)-circle collapse and orient \(t\) outward from the bolt. Smoothness gives
\[
a_h=t+O(t^3),\qquad
a_f=b+O(t^2),\qquad
a_g=b+O(t^2),
\]
so
\[
a_h'(0)=1,\qquad a_f'(0)=a_g'(0)=0.
\]
With
\[
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},
\]
the bolt limits are
\[
\gamma_f,\gamma_g\to0,\qquad \gamma_h\to2.
\]
Thus
\[
u_i=a_i'-\gamma_i\to(0,0,-1),\qquad
w_i=a_i'+\gamma_i\to(0,0,3).
\]
Using
\[
\mathfrak b_+=2-\sum u_i^2-u_fu_gu_h,\qquad
\mathfrak b_-=\sum w_i^2-w_fw_gw_h-2,
\]
one obtains
\[
\boxed{\mathfrak b_+(0)=1,\qquad \mathfrak b_-(0)=7.}
\]

The normalization agrees with the CH formulas:
\[
\mathfrak b_+=2-9\sinh^4t,\qquad
\mathfrak b_-=2-3\sinh^4t.
\]

The phrase “any triaxial jet” in Step 27 must mean any **smooth bolt jet**. Without the smoothness restrictions \(a_f'(0)=a_g'(0)=0\), the charge need not equal \((1,7)\).

---

## 3. Lemma N

Write
\[
S=\sum_i y_i,\qquad
\sigma_2=y_fy_g+y_gy_h+y_hy_f,\qquad
R^{(3)}=\sum_iP_i.
\]
The diagonal Ricci identities are
\[
\Ric_{00}=-S'-\sum_i y_i^2,\qquad
\Ric_{ii}=P_i-y_i'-Sy_i.
\]

### 3.1 Hamiltonian constraint

The scalar curvature is
\[
s=R^{(3)}-2S'-S^2-\sum_i y_i^2.
\]
Consequently
\[
G_{00}
=\Ric_{00}-\frac12s
=\sigma_2-\frac12R^{(3)}.
\]
Therefore
\[
\boxed{
\mathcal C:=\sigma_2-6-\frac12R^{(3)}
=G_{00}-6.
}
\]

With \(e_\alpha=\Ric_{\alpha\alpha}+6\),
\[
\boxed{
\mathcal C=\frac12\left(e_0-\sum_i e_i\right).
}
\]

For the compact variables,
\[
R^{(3)}
=-2\kappa^2+8\zeta\cosh q
-\frac{8\zeta^2\sinh^2q}{\kappa^2},
\]
hence
\[
\boxed{
\mathcal C
=\kappa^2+\sigma_2-4\zeta\cosh q-6
+\frac{4\zeta^2\sinh^2q}{\kappa^2}.
}
\]
All constants and signs in Lemma N(1) are correct.

### 3.2 Bianchi propagation

Applying \(\operatorname{div}(G-6g)=0\) to a diagonal cohomogeneity-one tensor yields
\[
\boxed{
\mathcal C'
=-2S\mathcal C-\sum_i(S-y_i)e_i.
}
\]
Equivalently,
\[
\boxed{
(W^2\mathcal C)'
=-W^2\sum_i(S-y_i)e_i,
}
\]
since \(W'=SW\). Thus the factor \(2\) and all signs in Lemma N(2) are correct.

### 3.3 Scalar normalization

If \(s=-24\), then
\[
e_0+\sum_i e_i=0.
\]
Combining this with the previous formula gives
\[
\boxed{\mathcal C=e_0=\Ric^\circ_{00}.}
\]
Since \(\Ric^\circ_{00}=-3H/4\),
\[
H=-\frac43\mathcal C.
\]
The stated norm decomposition then gives
\[
\frac14|\Ric^\circ|^2
=
\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8},
\]
and therefore
\[
\boxed{
\widehat P
=\int W\left(
\frac{\mathcal C^2}{3}
+\frac{E^2}{6}
+\frac{D^2}{8}
\right)dt.
}
\]
This supplies weighted \(L^2\), not pointwise, control:
\[
\int_IW\mathcal C^2\,dt\le3\widehat P_I.
\]
Thus “pointwise penalty” should not be read as an automatic pointwise estimate from small total cost.

Finally, substituting \(s=-24\) into the scalar-curvature identity gives
\[
\boxed{
S'=18-S^2+R^{(3)}+\mathcal C.
}
\]
Hence all four parts of Lemma N are correct.

---

## 4. Is scalar \(-24\) genuinely without loss?

For every smooth exact-CH-ended diagonal metric \(g\), Step 23 supplies a unique radial solution
\[
\hat g=u^2g,\qquad \hat s=-24,\qquad u\to1,
\]
with
\[
P(g)-P(\hat g)
=
24\int|\nabla u|^2
+3\int\left(\frac{\Delta u}{u}\right)^2
\ge0.
\]
Uniqueness and orbit symmetry force \(u=u(t)\); after introducing
\[
d\hat t=u\,dt,
\]
the metric remains diagonal Bianchi IX. Smoothness of the bolt is preserved.

However, Step 31’s claim that the Yamabe map “preserves the exact end” is false literally: generally \(u-1\) is a nonzero decaying mode, so \(\hat g\) is only asymptotic to the same marked CH end.

The correct infimum statement is
\[
\boxed{
\inf_{\substack{\text{diagonal}\\\text{exact CH end}}}P
=
\inf_{\substack{\text{diagonal},\,s=-24\\
\text{same marked CH asymptotic}\\
\text{decay rate }>4}}P.
}
\]
One inequality follows from the Yamabe reduction. For the converse, cut an asymptotic scalar-\(-24\) metric to exact CH over a unit annulus at radius \(R\). If the coefficient and derivative errors are \(O(e^{-mR})\), \(m>4\), the added Ricci-defect energy is
\[
O(e^{(4-2m)R})\to0.
\]
Thus exact-ended metrics approximate the scalar-normalized asymptotic metric in \(P\).

Accordingly, scalar \(-24\) is without loss **for the exact-ended diagonal infimum**, but only after passing through the asymptotic scalar class and a far-end cutoff.

A further caveat relevant to the proposed large-bolt theorem is that the conformal transformation changes the bolt radius:
\[
\hat b=u(0)b.
\]
The supplied material gives no uniform positive lower bound on \(u(0)\). Therefore \(b\to\infty\) before normalization does not by itself imply \(\hat b\to\infty\). Any scalar-normalized proof of Theorem L must formulate largeness using \(\hat b\), or prove such a bound.

---

## 5. Lemma W

Set
\[
A=\sqrt{18-\rho_0}>0,\qquad
m=\min\{S(T),A\},\qquad 0<\sigma_0<m,
\]
and assume \(W(T)>0\). Lemma N and \(R^{(3)}\ge-\rho_0\) give
\[
S'\ge A^2-S^2+\mathcal C
\ge A^2-S^2-|\mathcal C|.
\tag{5.1}
\]

The statement of Lemma W is correct. Its written proof is incomplete because monotonicity of
\[
S+\int|\mathcal C|
\]
is available only while \(|S|\le A\). In particular, when \(S(T)>A\), the comparison must begin at the last crossing of \(S=A\).

### Correct rigorous version

If
\[
m-\left(\frac{3\widehat P_{[T,T_1]}}
{\sigma_0W(T)}\right)^{1/2}\ge\sigma_0,
\]
then
\[
S(t)\ge\sigma_0,
\qquad
W(t)\ge W(T)e^{\sigma_0(t-T)},
\]
and
\[
\int_T^{T_1}\frac{dt}{W(t)}
\le
\frac{1-e^{-\sigma_0(T_1-T)}}{\sigma_0W(T)}
<
\frac1{\sigma_0W(T)}.
\]

### Proof

Suppose \(S\) first reaches \(\sigma_0\) at \(\tau>T\). Then \(S\ge\sigma_0\) on \([T,\tau]\), so \(W'=SW\) gives
\[
W(t)\ge W(T)e^{\sigma_0(t-T)}
\]
and
\[
\int_T^\tau\frac{dt}{W(t)}
<
\frac1{\sigma_0W(T)}.
\tag{5.2}
\]

Let \(a\le\tau\) be the last time at which \(S(a)=m\). Such an \(a\) exists:

- if \(S(T)\le A\), then \(m=S(T)\), so \(a=T\) or a later return;
- if \(S(T)>A\), then \(m=A\), and continuity forces a crossing of \(A\) before \(S\) can reach \(\sigma_0<A\).

On \((a,\tau)\),
\[
\sigma_0<S<m\le A.
\]
Define
\[
r(t)=\int_T^t|\mathcal C|\,ds.
\]
By (5.1),
\[
(S+r)'
\ge A^2-S^2+\mathcal C+|\mathcal C|
\ge0
\]
on \((a,\tau)\). Hence
\[
S(\tau)+r(\tau)\ge S(a)+r(a)\ge m,
\]
so
\[
S(\tau)\ge m-r(\tau).
\tag{5.3}
\]

From Lemma N,
\[
\int_T^\tau\frac{W\mathcal C^2}{3}\,dt
\le\widehat P_{[T,T_1]}.
\]
Cauchy–Schwarz and (5.2) yield
\[
r(\tau)
\le
\left(\frac{3\widehat P_{[T,T_1]}}
{\sigma_0W(T)}\right)^{1/2},
\]
strictly when needed because the finite-time bound in (5.2) is strict. Equation (5.3) then contradicts \(S(\tau)=\sigma_0\). Thus \(S\ge\sigma_0\), and the conclusions for \(W\) and \(\int W^{-1}\) follow.

An equivalent barrier-cost formulation is:
\[
\boxed{
S\text{ reaches }\sigma\in(0,m)
\quad\Longrightarrow\quad
\widehat P_{[T,T_1]}
\ge\frac13\,\sigma(m-\sigma)^2W(T).
}
\]
For example, taking \(\sigma=m/3\) gives
\[
\widehat P\ge\frac{4m^3}{81}W(T)
\]
whenever \(S\) falls to \(m/3\), hence also for any subsequent volume bounce through \(S\le0\).

The curvature hypothesis is substantive: on the face \(\zeta=0\),
\[
R^{(3)}=-2\kappa^2,
\]
so it requires bounded \(\kappa\), and it fails near the bolt corner \(\kappa=\infty\). Strongly sheared collapsed necks can likewise drive \(R^{(3)}\) arbitrarily negative.

---

## 6. Exact theorem versus numerical evidence

### Exact

- Lemma V and the simultaneous pointwise maximum bound.
- The positive-variation inequalities.
- The smooth \(O(-1)\) bolt charges \((1,7)\).
- All four identities in Lemma N and the weighted norm decomposition.
- Lemma W after inserting the last-crossing/first-barrier argument.
- Equality of the exact-ended diagonal infimum with the scalar-\(-24\), marked-asymptotic diagonal infimum, using Step 23’s existence and decay plus cutoff.
- The CH reopening threshold \(\tau>0.7012\ldots\), provided collapse is characterized by the relevant charge.

### Numerical or presently heuristic

- The values \(5.37,6.48,11.87\) are costs of converged local constrained minima. They are feasible-path upper bounds for the constrained infimum, not lower bounds.
- Therefore Step 31 §5’s statement that non-round opening is “numerically \(\ge5.37\)” is unjustified; the computations merely found local minima with costs at least that large.
- The charge lower bounds around \(1.49\)–\(1.55\) are rigorous only after certifying the numerical states or trajectories; algebraically they are exact evaluations of Lemma V.
- The large-bolt face limit, \(d/b\to0.90535\), \(\rho_\infty/b\to1.345\), and the proposed \(b^2(\log b)^2\) growth remain numerical/asymptotic evidence, not proved theorems.
- The reduction of every geometrically collapsed or sheared branch to the charge \(\mathfrak b_+\approx-2\) is not established without bounded normalized geometry or a direct charge estimate.

In conclusion: **Lemmas V and N are correct; the bolt normalization \(\mathfrak b_-=7\) is correct under smooth bolt conditions; Lemma W’s statement is correct but its proof requires the last-crossing argument, especially when \(S(T)>A\). Scalar \(-24\) is legitimate for the exact-ended infimum only via the marked asymptotic scalar class and an arbitrarily small far-end cutoff, not because Yamabe normalization preserves literal exactness of the end.**