# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md",
    "Sessions/S1003A02/workspace/notes/step27_chiral_transgression_and_small_bolt.md",
    "Sessions/S1003A02/workspace/notes/step23_yamabe_identity_hyperbolic_sharp_gap_and_cell_channels.md",
    "Sessions/S1003A02/workspace/scripts/scalar_normalized_constraint.py",
    "Sessions/S1003A02/workspace/scripts/chiral_two_sided_bound.py"
  ]
}
```

## Task

Independently verify Lemmas V, N, and W in the Step-31 note. Derive all constants and signs from the stated diagonal chiral and Ricci identities. In particular: (i) determine whether the pointwise conclusion dP_hat/dt = b'_pm + nonnegative density and the stronger integral max{0,b_+',b_-'} bound are valid simultaneously; (ii) check b_- normalization at the O(-1) bolt; (iii) check C identities and whether scalar -24 is legitimately without loss for the exact-ended diagonal infimum; (iv) inspect Lemma W's first-barrier proof including the case S(T)>A, and state a corrected rigorous version if needed. Distinguish exact theorem from numerical support.

## Output

# Scientific verification memo: Lemmas V, N, and W

## 1. Lemma V and the simultaneous two-chirality estimate

Write
\[
p(t):=\frac{d}{dt}\widehat P([a,t])
      =\frac14W|\operatorname{Ric}^{\circ}|^2,
\qquad
d\mu_g=2\pi^2W\,dt .
\]
The localized chiral identities from Theorem X give, on every regular orbit interval,
\[
p(t)=\mathfrak b_\pm'(t)+\omega_\pm(t).
\]

### Density normalization

If \(|W^\pm|^2\) and \(s^2\) denote their pointwise four-dimensional norms, then the exact radial density is
\[
\boxed{\;
\omega_\pm
 =W|W^\pm|^2+\frac{W}{48}s^2\ge0 .
\;}
\]
Indeed,
\[
\frac1{2\pi^2}\int |W^\pm|^2\,d\mu_g
 =\int W|W^\pm|^2\,dt,
\qquad
\frac1{96\pi^2}\int s^2\,d\mu_g
 =\int \frac{W}{48}s^2\,dt.
\]
Thus the Step-31 notation involving “density” is correct only if that word already includes the appropriate \(2\pi^2\) orbit normalization. If it means the pointwise scalar itself, the displayed factors there should be replaced by the boxed formula. The sign argument is unaffected.

Since the same \(p(t)\) satisfies both identities,
\[
p(t)\ge \mathfrak b_+'(t),\qquad
p(t)\ge \mathfrak b_-'(t),\qquad
p(t)\ge0.
\]
Consequently the three estimates hold simultaneously:
\[
\boxed{\;
p(t)\ge\max\{0,\mathfrak b_+'(t),\mathfrak b_-'(t)\}.
\;}
\]
There is no incompatibility from using the two chiral decompositions: each separately expresses the same \(p(t)\) as a charge derivative plus a square density. What does not follow is a sum such as
\((\mathfrak b_+')_++(\mathfrak b_-')_+\).

After integration,
\[
\widehat P([a,b])
 \ge\int_a^b\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt.
\]
For an absolutely continuous function \(f\),
\[
V^+_{[a,b]}(f)=\int_a^b(f')_+\,dt.
\]
Therefore
\[
\int_a^b\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt
\ge
\max\{V^+(\mathfrak b_+),V^+(\mathfrak b_-)\}.
\]
The same conclusion follows directly by summing increments on finite disjoint interval families. At a bolt one first works on \([\varepsilon,b]\) and then lets \(\varepsilon\downarrow0\); smooth bolt expansions give finite charge limits.

Hence Lemma V is an exact consequence of Theorem X.

---

## 2. The \(O(-1)\) bolt normalization of \(\mathfrak b_-\)

Take the collapsing direction to be \(h\), with \(t\) increasing away from the bolt. Smoothness in the stated \(d\sigma_i=2\sigma_j\wedge\sigma_k\) convention gives
\[
a_h=t+O(t^3),\qquad
a_f=b+O(t^2),\qquad
a_g=b+O(t^2).
\]
Thus
\[
a_h'(0)=1,\qquad a_f'(0)=a_g'(0)=0.
\]
For
\[
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},
\]
the bolt limits are
\[
\gamma_f,\gamma_g\longrightarrow0,\qquad
\gamma_h\longrightarrow2.
\]
Therefore
\[
u_i=a_i'-\gamma_i\longrightarrow(0,0,-1),
\qquad
w_i=a_i'+\gamma_i\longrightarrow(0,0,3).
\]
Using
\[
\mathfrak b_+=2-\sum_i u_i^2-u_fu_gu_h,
\qquad
\mathfrak b_-=\sum_iw_i^2-w_fw_gw_h-2,
\]
one obtains
\[
\boxed{\mathfrak b_+(0)=1,\qquad \mathfrak b_-(0)=7.}
\]

This also matches the CH normalization. For
\[
a_f=\sinh t\cosh t,\qquad a_g=a_h=\sinh t,
\]
putting \(x=\sinh^2t\) gives
\[
w_f=2+x,\qquad w_g=w_h=2\cosh t,
\]
and hence
\[
\mathfrak b_-=2-3x^2=2-3\sinh^4t.
\]
Thus the bolt value \(7\), the smooth-centre value \(2\), and the CH formula use one consistent additive normalization. Reversing the radial orientation would alter the endpoint calculation, but it is not the convention used in Steps 27–31.

---

## 3. Lemma N

Let
\[
S=y_f+y_g+y_h,\qquad
\sigma_2(y)=y_fy_g+y_gy_h+y_hy_f,
\qquad
R^{(3)}=\sum_iP_i.
\]
The diagonal Ricci formulas encoded by
\[
y_i'=6-y_iS+P_i-e_i,\qquad e_i=\operatorname{Ric}_{ii}+6,
\]
are equivalently
\[
\operatorname{Ric}_{00}=-S'-\sum_i y_i^2,
\qquad
\operatorname{Ric}_{ii}=P_i-y_i'-Sy_i.
\]

### 3.1 Hamiltonian identity

The scalar curvature is
\[
s=R^{(3)}-2S'-S^2-\sum_i y_i^2.
\]
Thus
\[
G_{00}
=\operatorname{Ric}_{00}-\frac12s
=\frac12\left(S^2-\sum_i y_i^2-R^{(3)}\right)
=\sigma_2(y)-\frac12R^{(3)}.
\]
It follows that
\[
\boxed{\;
\mathcal C:=\sigma_2(y)-6-\frac12R^{(3)}
       =G_{00}-6.
\;}
\]

Writing \(e_0=\operatorname{Ric}_{00}+6\),
\[
\frac12\left(e_0-\sum_i e_i\right)
=\frac12\left(\operatorname{Ric}_{00}-\sum_i\operatorname{Ric}_{ii}-12\right)
=G_{00}-6,
\]
so
\[
\boxed{\;
\mathcal C=\frac12\left(e_0-\sum_i e_i\right).
\;}
\]

For the compact variables in the script,
\[
R^{(3)}
=-2\kappa^2+8\zeta\cosh q
-\frac{8\zeta^2\sinh^2q}{\kappa^2},
\]
which gives
\[
\mathcal C
=\kappa^2+\sigma_2(y)-4\zeta\cosh q-6
+\frac{4\zeta^2\sinh^2q}{\kappa^2}.
\]
The constants and signs in Step 31 are therefore correct.

### 3.2 Bianchi propagation

Set
\[
K:=G-6g.
\]
Then \(\operatorname{div}K=0\) and \(K_{00}=\mathcal C\). If
\[
e_{\mathrm{tr}}=e_0+\sum_i e_i=s+24,
\]
then
\[
K_{ii}=e_i-\frac12e_{\mathrm{tr}}.
\]
Since
\[
\frac12e_{\mathrm{tr}}=\mathcal C+\sum_i e_i,
\]
one has
\[
K_{ii}=e_i-\mathcal C-\sum_j e_j.
\]
For a diagonal cohomogeneity-one tensor,
\[
0=(\operatorname{div}K)_0
=\mathcal C'+\sum_i y_i(\mathcal C-K_{ii}).
\]
Substitution yields
\[
\boxed{\;
\mathcal C'
=-2S\mathcal C-\sum_i(S-y_i)e_i.
\;}
\]
This confirms both the factor \(2\) and the minus signs.

### 3.3 Scalar value \(-24\)

When \(s=-24\),
\[
e_0+\sum_i e_i=0.
\]
Combining this with
\(\mathcal C=(e_0-\sum e_i)/2\) gives
\[
\boxed{\mathcal C=e_0=\operatorname{Ric}^{\circ}_{00}.}
\]
With the stated convention
\[
\operatorname{Ric}^{\circ}_{00}=-\frac34H,
\]
one gets
\[
H=-\frac43\mathcal C.
\]
Therefore
\[
\frac14|\operatorname{Ric}^{\circ}|^2
=\frac14\left(\frac34H^2+\frac23E^2+\frac12D^2\right)
=\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}.
\]
Hence
\[
\boxed{\;
\widehat P
=\int W\left(
\frac{\mathcal C^2}{3}
+\frac{E^2}{6}
+\frac{D^2}{8}\right)dt.
\;}
\]

The exact consequence is weighted \(L^2\) control,
\[
\int_I W\mathcal C^2\,dt\le3\widehat P_I.
\]
Large \(W\) alone does not force \(\mathcal C=0\) at each individual point; a pointwise estimate needs interval information or derivative control. Lemma W provides precisely the integrated use of this channel.

### 3.4 The \(S\)-equation

From the scalar-curvature formula and
\(\sum y_i^2=S^2-2\sigma_2\),
\[
s=-24
\quad\Longrightarrow\quad
S'=12+\frac12R^{(3)}-S^2+\sigma_2.
\]
Since
\[
\sigma_2=\mathcal C+6+\frac12R^{(3)},
\]
this becomes
\[
\boxed{\;
S'=18-S^2+R^{(3)}+\mathcal C.
\;}
\]
Thus all four identities in Lemma N have the stated signs and constants.

---

## 4. Scalar normalization and the exact-ended infimum

For an exact-CH-ended diagonal metric \(g\), the Yamabe solution
\[
\hat g=u^2g,\qquad \hat s=-24,\qquad u\to1,
\]
satisfies
\[
P(g)-P(\hat g)
=24\int|\nabla u|^2
 +3\int\left(\frac{\Delta u}{u}\right)^2
\ge0.
\]
For \(\widehat P=P/(8\pi^2)\), the right side is divided by \(8\pi^2\).

Uniqueness of \(u\) and invariance of \(g\) under the orbit action imply that \(u\) is radial. Moreover,
\[
u^2dt^2+\sum_i(ua_i)^2\sigma_i^2
\]
returns to unit-lapse diagonal form after \(d\hat t=u\,dt\). Thus the diagonal cohomogeneity-one structure is preserved.

There is, however, an important textual correction:

\[
\boxed{\text{The Yamabe metric is generally asymptotic to the same marked CH end, not exactly CH outside a compact set.}}
\]

A nonzero decaying Yamabe mode usually remains on the exterior. Thus scalar normalization does not map every exact-ended metric into the scalar-\(-24\), exact-ended subclass.

It is nevertheless valid at the level of the infimum, using the decay supplied in Step 23. Let

* \(\mathcal A_{\mathrm{ex}}\) be the exact-CH-ended diagonal metrics;
* \(\mathcal A_{-24,\mathrm{as}}\) be the diagonal scalar-\(-24\) metrics approaching the same marked CH end with all required derivatives at rate \(e^{-mr}\), \(m>4\).

The Yamabe map gives
\[
\inf_{\mathcal A_{-24,\mathrm{as}}}P
\le
\inf_{\mathcal A_{\mathrm{ex}}}P.
\]
Conversely, for \(h\in\mathcal A_{-24,\mathrm{as}}\), interpolate its diagonal coefficients to the exact CH coefficients on \([R,R+1]\), leaving \(h\) unchanged before \(R\) and exactly CH after \(R+1\). In an orthonormal CH frame the induced Ricci defect on the interpolation interval is \(O(e^{-mR})\), while CH volume there is \(O(e^{4R})\). Its \(P\)-contribution is therefore
\[
O(e^{(4-2m)R})\longrightarrow0.
\]
The tail contribution also tends to zero. Hence exact-ended diagonal metrics \(h_R\) exist with
\[
P(h_R)\longrightarrow P(h),
\]
and consequently
\[
\boxed{\;
\inf_{\mathcal A_{\mathrm{ex}}}P
=
\inf_{\mathcal A_{-24,\mathrm{as}}}P.
\;}
\]

Thus scalar \(-24\) is valid for computing this infimum, provided “same exact end” in Step 31 is replaced by “same marked asymptotic end, followed by an arbitrarily small far-end cutoff.” This argument concerns the \(P\) or \(\widehat P\) cell functional; a different functional would require its own conformal comparison.

---

## 5. Lemma W and the case \(S(T)>A\)

Let
\[
A=\sqrt{18-\rho_0}>0,\qquad
m=\min\{S(T),A\},\qquad
0<\sigma_0<m,
\]
and assume \(W(T)>0\). From Lemma N and
\(R^{(3)}\ge-\rho_0\),
\[
S'
=18-S^2+R^{(3)}+\mathcal C
\ge A^2-S^2+\mathcal C
\ge A^2-S^2-|\mathcal C|.
\tag{5.1}
\]

The Step-31 sentence about \(S+\int|\mathcal C|\) is valid only while
\(|S|\le A\). This is automatic on the relevant first-contact interval, but it needs to be stated explicitly. When \(S(T)>A\), one starts the comparison at the last crossing of \(S=A\), not at \(T\).

### Corrected rigorous form

Set
\[
\delta
=\left(
\frac{3\widehat P_{[T,T_1]}}
{\sigma_0W(T)}
\right)^{1/2}.
\]
If
\[
m-\delta\ge\sigma_0,
\]
then
\[
S(t)\ge\sigma_0,\qquad
W(t)\ge W(T)e^{\sigma_0(t-T)},\qquad
\int_T^{T_1}\frac{dt}{W(t)}
\le\frac1{\sigma_0W(T)}.
\]

### Proof

Suppose that \(S\) reaches \(\sigma_0\) at a first time \(\tau>T\) on its way below that value. Then
\[
S\ge\sigma_0\quad\text{on }[T,\tau].
\]
Because \(W'=SW\),
\[
W(t)\ge W(T)e^{\sigma_0(t-T)}
\quad (T\le t\le\tau),
\]
and
\[
\int_T^\tau\frac{dt}{W(t)}
\le
\frac{1-e^{-\sigma_0(\tau-T)}}{\sigma_0W(T)}
<
\frac1{\sigma_0W(T)}.
\tag{5.2}
\]

Let \(a\le\tau\) be the last time at which \(S(a)=m\).

* If \(S(T)\le A\), then \(m=S(T)\), or \(a\) is a later return to \(m\).
* If \(S(T)>A\), then \(m=A\); continuity supplies a crossing \(S(a)=A\) before \(S\) can reach \(\sigma_0<A\).

On \((a,\tau)\),
\[
\sigma_0<S<m\le A.
\]
Define
\[
r(t)=\int_T^t|\mathcal C|\,ds.
\]
Using (5.1),
\[
(S+r)'
=S'+|\mathcal C|
\ge A^2-S^2+\mathcal C+|\mathcal C|
\ge0
\]
on \((a,\tau)\). Therefore
\[
S(\tau)+r(\tau)
\ge S(a)+r(a)
=m+r(a)\ge m,
\]
so
\[
S(\tau)\ge m-r(\tau).
\tag{5.3}
\]

The \(\mathcal C\)-part of Lemma N gives
\[
\int_T^\tau\frac{W\mathcal C^2}{3}\,dt
\le\widehat P_{[T,T_1]}.
\]
Cauchy–Schwarz and (5.2) yield
\[
\begin{aligned}
r(\tau)
&=\int_T^\tau
\left(\sqrt{\frac W3}\,|\mathcal C|\right)
\left(\sqrt{\frac3W}\right)dt\\
&\le
\left(\int_T^\tau\frac{W\mathcal C^2}{3}\,dt\right)^{1/2}
\left(3\int_T^\tau\frac{dt}{W}\right)^{1/2}\\
&<
\left(
\frac{3\widehat P_{[T,T_1]}}
{\sigma_0W(T)}
\right)^{1/2}
=\delta
\end{aligned}
\]
when \(\widehat P_{[T,T_1]}>0\). If it vanishes, then \(r(\tau)=0\). In either case, using \(m>\sigma_0\),
\[
S(\tau)>m-\delta\ge\sigma_0,
\]
contrary to \(S(\tau)=\sigma_0\). Hence \(S\ge\sigma_0\) throughout. Integrating \(W'=SW\) gives the remaining two conclusions.

The strict inequality in (5.2) also handles the equality case
\(m-\delta=\sigma_0\). Thus the statement of Lemma W is correct after adding \(W(T)>0\); its proof needs the last-crossing argument above to cover \(S(T)>A\) and to justify the use of \(|S|\le A\).

---

## 6. Exact results versus computation

### Exact consequences of the supplied identities

* Lemma V, including the integral of the pointwise maximum and both positive-variation estimates.
* The bolt charges \((\mathfrak b_+,\mathfrak b_-)=(1,7)\).
* Every algebraic and differential identity in Lemma N.
* The weighted decomposition
  \[
  \widehat P=\int W\left(\mathcal C^2/3+E^2/6+D^2/8\right)dt.
  \]
* Lemma W with the first-contact proof above.
* Reduction of the exact-ended \(P\)-infimum to scalar-\(-24\) asymptotic metrics, once the Yamabe existence and decay theorem from Step 23 is used together with the far-end cutoff argument.

### Computation-based evidence

* The decimals \(8.54957\), \(1.5496\), and the charge values reconstructed along collocation paths depend on the stored numerical states.
* The costs \(5.37\), \(6.48\), \(11.87\), and their channel splits are values of computed local constrained minimizers. They do not provide a universal lower estimate for non-round opening.
* The large-bolt face convergence and the laws
  \(d/b\to0.90535\) and \(\rho_\infty/b\to1.345\) are numerical asymptotics.
* The proposed \(b^2(\log b)^2\) growth requires the compactness, face-trajectory, and ACH pinning arguments outlined in Step 31.
* The SymPy residuals in `scalar_normalized_constraint.py` are exact symbolic confirmations of Lemma N; the hand derivations above independently establish the same formulas.

In summary, Lemmas V and N are correct with the radial density normalization made explicit. The \(O(-1)\) bolt has \(\mathfrak b_-=7\). Lemma W has the correct statement, while its written proof needs the last-crossing argument for \(S(T)>A\). Scalar normalization is valid for the exact-ended diagonal infimum through passage to the asymptotic scalar class and a far-end cutoff, not because the Yamabe factor generally remains identically one on the exterior.