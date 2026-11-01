# TTCS Independent Branch Record

```json
{
  "step_id": 106,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Sessions/S1003A02/workspace/scripts/step105_cap_charge_check.py",
    "Sessions/S1003A02/workspace/data/step105/cap_charge_check.json",
    "Knowledge/objects/papers/Hitchin-Thorpe-Inequality-for-Noncompact-Einstein-4--fd6e60eeeaa2--deedf5d03a5f/object.md"
  ]
}
```

## Task

Independently verify Theorem 105.Q and Corollaries 105.L/105.H in the Step-105 note. Check orientation and normalization from Theorem G and Dai–Wei, the scalar-cap vanishing argument, the C_+(Omega) decomposition, the cap contribution to the mixed LeBrun estimate, and the arithmetic 9k+8 sum c <=3A and A/11. Identify any gap or needed repair precisely. Also assess whether (E2) is exactly implied by D(g_i)->0 at a fixed nonzero Einstein normalization plus total-volume convergence.

## Output

# Independent verification memo

## 1. Theorem G, orientations, and Dai–Wei normalization

For a compact region \(D\), Theorem G is equivalent to
\[
C_+(g;D)
=\widehat P(g;D)+(2\chi+3\tau)(D)-\mathcal Q_+(\partial D).
\]
Fix \(\rho\), and orient each link \(L_{\ell,\rho}\) outward from \(\Omega_\rho\). Its orientation as an outward link of the corresponding cap is the opposite one, so
\[
\mathcal Q_+^{\mathrm{out}}(C_j)
=-\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_i).
\]
Consequently,
\[
\lim_{i\to\infty} C_+(g_i;C_j^{(\rho)})
=(2\chi+3\tau)(C_j)
+\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_\infty),
\]
because \(0\le \widehat P(g_i;C_j^{(\rho)})\le\widehat P(g_i)\to0\). This verifies the sign in Theorem 105.Q(1).

The normalization of the APS term needs explicit notation. Dai–Wei Theorem 3.5 gives
\[
\tau(\Omega)=\int_\Omega L-\frac12\,\mathrm a\!-\!\lim\eta_{\rm sig}.
\]
Since Theorem G defines \(\mathcal H\) through
\[
\int_\Omega L=\tau(\Omega)+\mathcal H,
\]
one has
\[
\mathcal H^\infty=\frac12\,\mathrm a\!-\!\lim\eta_{\rm sig}.
\]
Thus Step 33’s notation \(\mathcal H=\eta+\int T_{p_1}\) is consistent only if its \(\eta\) already denotes the half-normalized APS contribution.

For a circle bundle over a surface, Dai–Wei Theorem 5.1 gives, with the orientation convention used in Step 105,
\[
\mathcal H^\infty=\frac e3-\operatorname{sign}e.
\]
Therefore
\[
\mathcal Q_+^\infty=-e+3\operatorname{sign}e,\qquad
\mathcal Q_-^\infty=e-3\operatorname{sign}e.
\]
If \(e_{\rm out}\) is computed using the cap orientation, then the Einstein-side link has \(e=-e_{\rm out}\), and hence
\[
c=(2\chi+3\tau)(C)+e_{\rm out}
       -3\operatorname{sign}e_{\rm out}.
\]
This is exactly the formula in Step 105.

The supplied transcription of Dai–Wei Corollary 1.2 displays the opposite sign of \(e\), while Theorem 5.1 and the formula in §6 support the sign above. The independent Taub–NUT models settle the convention:

- \(e_{\rm out}=-1\), \((\chi,\tau)=(1,0)\): \(c=4\);
- \(e_{\rm out}=+1\): \(c=0\);
- Taub–bolt, \((\chi,\tau)=(2,-1)\), \(e_{\rm out}=-1\): \(c=3\);
- multi–Taub–NUT, \((\chi,\tau)=(m,-m+1)\), \(e_{\rm out}=m\): \(c=0\).

The first table row is numerically consistent:  
\[
\frac1{8\pi^2}\int |W^+|^2=1
\quad\Longleftrightarrow\quad
C_+=\frac1{2\pi^2}\int|W^+|^2=4.
\]
Its column heading could more clearly distinguish these two normalizations.

For fixed \(\rho\), \(C^2\) collar convergence controls the Euler and Pontryagin transgressions. Continuity of the odd-signature eta term follows from its APS variation formula; the kernel dimension is topological, so no spectral-flow jump occurs.

## 2. Existence of the cap limits and scalar-cap vanishing

There is one omitted argument for the \(\rho\to0\) limit. Put
\[
a_j(\rho)=\lim_{i\to\infty}C_+(g_i;C_j^{(\rho)}).
\]
With the caps labelled by their fixed end sets \(J_j\), nested exhaustion gives
\[
C_j^{(\rho_2)}\subset C_j^{(\rho_1)}
\qquad(\rho_2<\rho_1).
\]
Since the density defining \(C_+\) is pointwise \(\ge0\),
\[
a_j(\rho_2)\le a_j(\rho_1).
\]
Thus \(a_j(\rho)\) has a finite decreasing limit \(c_j\ge0\). The formula above then also proves the existence of the limiting link charge. If (E3) does not include consistent nested labels, individual \(c_j\) are not canonical; only sums over descendant cap components are canonical.

The scalar argument is correct after repairing one sentence. In general, when several caps occur, it is not true that each
\[
\operatorname{Vol}(g_i;C_j^{(\rho)})
\longrightarrow
\operatorname{Vol}(g_\infty;\Omega\setminus\Omega_\rho).
\]
What follows from total-volume convergence and local convergence is
\[
\sum_j\operatorname{Vol}(g_i;C_j^{(\rho)})
=
\operatorname{Vol}(g_i;M)-\operatorname{Vol}(g_i;\Omega_\rho)
\longrightarrow
\operatorname{Vol}(g_\infty;\Omega\setminus\Omega_\rho).
\]
Hence, for each \(j\),
\[
\limsup_i\operatorname{Vol}(g_i;C_j^{(\rho)})
\le
\operatorname{Vol}(g_\infty;\Omega\setminus\Omega_\rho).
\]
Using
\[
\int_{C_j^{(\rho)}}s_i^2
\le
2\int_M(s_i-\bar s_i)^2+
2\bar s_i^2\operatorname{Vol}(g_i;C_j^{(\rho)}),
\]
the boundedness of \(\bar s_i\), and the finite volume of \(g_\infty\), one obtains
\[
\lim_{\rho\to0}\limsup_{i\to\infty}
\int_{C_j^{(\rho)}}s_i^2=0.
\]
Therefore
\[
c_j
=
\lim_{\rho\to0}\lim_{i\to\infty}
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W^+_{g_i}|^2,
\]
which verifies Theorem 105.Q(2).

## 3. The \(C_+(\Omega)\) decomposition

On the closed manifold,
\[
C_+(g_i;M)
=(2\chi+3\tau)(M)+\widehat P(g_i)
\longrightarrow A-k.
\]
For fixed \(\rho\), additivity of the curvature integrals gives
\[
C_+(g_i;M)
=
C_+(g_i;\Omega_\rho)
+\sum_j C_+(g_i;C_j^{(\rho)}).
\]
Local \(C^2\) convergence implies
\[
C_+(g_i;\Omega_\rho)\longrightarrow
C_+(g_\infty;\Omega_\rho).
\]
Thus
\[
A-k=C_+(g_\infty;\Omega_\rho)+\sum_j a_j(\rho).
\]
Letting \(\rho\to0\), monotone convergence of the curvature integral on \(\Omega_\rho\) and \(a_j(\rho)\to c_j\) yield
\[
\boxed{C_+(g_\infty;\Omega)=A-k-\sum_jc_j.}
\]
No curvature energy is omitted here. The formula also proves finiteness of \(C_+(g_\infty;\Omega)\).

## 4. Corollary 105.L and the cap contribution

Let
\[
I(g;D)=\int_D(s-\sqrt6|W^+|)^2.
\]
On a cap, Minkowski’s inequality gives
\[
I(g_i;C_j^{(\rho)})
\le
\left(
\|s_i\|_{L^2(C_j^{(\rho)})}
+\sqrt6\|W^+_{g_i}\|_{L^2(C_j^{(\rho)})}
\right)^2.
\]
The scalar term tends to zero in the iterated limit, while
\[
\int_{C_j^{(\rho)}}|W^+|^2\longrightarrow 2\pi^2c_j.
\]
Hence
\[
\lim_{\rho\to0}\limsup_i I(g_i;C_j^{(\rho)})
\le12\pi^2c_j.
\]
This verifies that a cap of charge \(c_j>0\) cannot be discarded from the mixed LeBrun functional.

On \(\Omega\), set
\[
x=\frac1{96\pi^2}\int_\Omega s_\infty^2,\qquad
y=\frac1{2\pi^2}\int_\Omega|W^+_{g_\infty}|^2.
\]
Then \(x+y=A-k-\sum c_j\), and
\[
\begin{aligned}
I(g_\infty;\Omega)
&\le12\pi^2(\sqrt{8x}+\sqrt y)^2\\
&\le108\pi^2(x+y)\\
&=108\pi^2\left(A-k-\sum_jc_j\right).
\end{aligned}
\]
Passing the global LeBrun inequality through the decomposition gives
\[
72\pi^2A
\le
108\pi^2\left(A-k-\sum_jc_j\right)
+12\pi^2\sum_jc_j.
\]
After division and rearrangement,
\[
\boxed{9k+8\sum_jc_j\le3A.}
\]
The coefficient \(8\) and all normalizing factors are correct.

The further statement
\[
k+\sum_jc_j\le\frac{2A}{3}
\]
is valid, but the proof as written invokes the separate scalar estimate
\[
\int_Ms^2\ge32\pi^2A,
\]
which is not explicitly listed in the corollary’s hypothesis. It is unnecessary for the displayed conclusion: since \(k\ge0\) and \(c_j\ge0\),
\[
8\left(k+\sum_jc_j\right)
\le9k+8\sum_jc_j\le3A,
\]
so the mixed estimate actually gives the stronger relation
\[
k+\sum_jc_j\le\frac{3A}{8}.
\]

## 5. Corollary 105.H

For a standard \(S^3\)-Hopf cap with
\[
b_1=b_3=b_2^+=0,\qquad b_2^-=r,
\]
one has
\[
\chi=1+r,\qquad \tau=-r,\qquad 2\chi+3\tau=2-r.
\]
Therefore
\[
c=
\begin{cases}
4-r,&e_{\rm out}=-1,\\
-r,&e_{\rm out}=+1.
\end{cases}
\]
Thus a cap carrying \(r\ge1\) classes can use only the first chirality, and positivity of \(c\) gives \(r\le4\).

For \(N\) such caps with \(\sum r_j=k\),
\[
\sum_{j=1}^N c_j=4N-k.
\]
If there are no further charge-\(4\) ball caps, Corollary 105.L becomes
\[
9k+8(4N-k)\le3A
\iff
\boxed{k+32N\le3A}.
\]
Hence:

- \(N=k\): \(33k\le3A\), so
  \[
  \boxed{k\le A/11}.
  \]
- \(r_j=4\) for every cap, so \(N=k/4\): \(9k\le3A\), hence
  \[
  k\le A/3.
  \]
- A single \(r=4\) cap requires
  \[
  4+32\le3A,\qquad A\ge12.
  \]

The \(A/11\) arithmetic is therefore correct.

There is one correction when further ball caps are present. If \(q\) ball caps have charge \(4\), while any others have charge \(0\), then the exact relation is
\[
\boxed{k+32N+32q\le3A.}
\]
Dropping \(32q\) gives the necessary relation \(k+32N\le3A\), but the “if and only if” wording applies only when \(q=0\).

The arithmetic only records compatibility with the transferred LeBrun estimate; it does not furnish a degeneration realizing the four-class configuration.

Scientifically, a four-class cap with \(c_+=0\) is invisible only to the \(C_+\)/LeBrun channel. It is visible to the opposite chirality. Indeed, for \(r=4\), \(e_{\rm out}=-1\),
\[
c_-=(2\chi-3\tau)(C)+\mathcal Q_-^\infty(L)
=22-2=20.
\]
Thus
\[
\lim\frac1{2\pi^2}\int_C|W^-|^2=20
\]
when its scalar and trace-free Ricci energies vanish. The phrase “invisible to every integrated curvature inequality” is therefore too broad.

## 6. Does \(\mathscr D(g_i)\to0\) give (E2)?

The supplied material does not state the formula for \(\mathscr D\), so this equivalence is conditional on its definition.

If
\[
\mathscr D(g)
\quad\text{is a positive multiple of}\quad
\int_M\left|\operatorname{Ric}
-\frac{\bar s}{4}g\right|^2d\mu,
\]
then the orthogonal decomposition
\[
\left|\operatorname{Ric}-\frac{\bar s}{4}g\right|^2
=
|\operatorname{Ric}^\circ|^2+\frac14(s-\bar s)^2
\]
shows directly that
\[
\widehat P(g_i)\to0,\qquad
\int_M(s_i-\bar s_i)^2\to0.
\]
With the normalization \(\bar s_i=s_\infty\ne0\), the scalar-average part of (E2) is automatic, and total-volume convergence supplies its remaining part. Under this definition, the Step-105 sentence is correct.

The same conclusion holds if \(\mathscr D\) uses a fixed Einstein constant \(\lambda\ne0\), because
\[
|\operatorname{Ric}-\lambda g|^2
=
|\operatorname{Ric}^\circ|^2+\frac14(s-4\lambda)^2.
\]

If instead \(\mathscr D\) contains only
\[
\int|\operatorname{Ric}^\circ|^2,
\]
then scalar variance does not follow from the stated information. The contracted Bianchi identity alone does not convert \(L^2\)-small trace-free Ricci curvature into \(L^2\)-small scalar oscillation without further geometric or derivative estimates.

Moreover, \(\mathscr D\to0\) does not itself imply total-volume convergence because the four-dimensional defect is scale invariant. The volume hypothesis is independent geometric information.

Finally, once local convergence and scalar variance are known, \(\bar s_i\to s_\infty\) can also be derived rather than assumed. On any fixed compact \(K\Subset\Omega\) with positive volume,
\[
\operatorname{Vol}_{g_i}(K)|\bar s_i-s_\infty|^2
\le
2\int_K(s_i-\bar s_i)^2+
2\int_K(s_i-s_\infty)^2\longrightarrow0.
\]

In summary: Theorem 105.Q and the coefficient \(9k+8\sum c_j\le3A\) are mathematically correct after inserting the nested-cap and total-cap-volume arguments. The \(A/11\) threshold is correct. Corollary 105.H needs the \(32q\) term for charge-\(4\) ball caps, and the zero \(C_+\)-charge sector remains highly visible in \(C_-\).