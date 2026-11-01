# TTCS Independent Branch Record

```json
{
  "step_id": 85,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/workspace/notes/step77_goldberg_first_tier_collapse_and_canonical_curve_identity.md",
    "Sessions/S1003A01/workspace/briefing/Session.md"
  ]
}
```

## Task

Research question (Einstein metrics on nonminimal general-type surfaces, and positive Weyl deficit). Let X be a minimal complex surface of general type with b+>1, A=c1^2(X), M = X # k CPbar^2, and g an Einstein metric on M (Ric = (s/4) g, s<0). Notation: D_W = int (s^2/24 - |W+|^2), S = int s^2, P = int |Ric0|^2; Chern-Weil gives D_W = S/16 - P/4 - 2 pi^2 (2chi+3tau), and on M this is 8 pi^2 k - P = 4 D_W - (S - 32 pi^2 A)/4. LeBrun's estimates force D_W >= 4 pi^2 k for an Einstein candidate. The session's certified non-Einstein metrics show that positive D_W alone is not forbidden, so any restriction must use exact Einstein / actual-field compatibility. Proposed mechanism to evaluate: for b+>1 and the basic classes c = c1(K_X) + sum ±E_i (all sign choices are monopole classes by the blowup formula, so simultaneous supply holds for every metric; do NOT use b+=1 chambers), take two actual Seiberg-Witten solutions (psi_a, A_a), (psi_b, A_b) on the SAME Einstein metric g with classes a and b = a + 2e, e = E_j (or a sum of several E_i). The spinors live in different bundles V_a^+ and V_b^+ = V_a^+ (x) L_e^{2}... (be careful: V_b^+ = V_a^+ (x) L where c1(L) = e-type class; state the correct line bundle). Form the twisted Hom bilinear Phi = psi_b (x) psi_a^* , a section of Hom(V_a^+, V_b^+) = L-twisted End, its trace-free self-dual part, and the relative connection A_b - A_a on L with curvature F_b - F_a representing 2 pi * (relative class). Derive the exact Weitzenbock/Bochner identity for Phi or for the relative section sigma = <psi_b, psi_a>-type section of L (a genuine section of a line bundle with c1 = relative class) using both SW equations and the Einstein condition (W+ enters the Weitzenbock formula on Lambda+ valued pieces; Bianchi delta W+ = 0 for Einstein). Determine precisely: (1) whether the zero locus/degree of the relative section, which is a topological pairing with e (e.g. degree e.[omega-type class] or e^2 = -1), together with the curvature identity, yields an inequality on D_W, on int |W+|^2 restricted, or on the exceptional flux int (F_b-F_a) wedge omega_a that is NOT already a consequence of the individual LeBrun scalar/Weyl inequalities for each class; (2) whether at an exact Einstein metric with the LeBrun bounds saturated or near-saturated one obtains a contradiction for k in the open range 1 <= k < A/3 (the Hitchin-Thorpe-allowed range where existence is open); (3) if the mixed identity reduces to the old individual balances, say so explicitly with the algebra, so the route can be dropped. Keep zeros of the spinors and the full connection curvature; do not identify spinors in different bundles; check every sign and the normalization |psi|^2 = -s at solutions of the scalar estimate. Output a direct mathematical memo with full derivations, the exact identity obtained, and a clear verdict on whether it supplies information beyond the signed scalar inequalities.

## Output

# Mathematical memo: two signed monopoles on one Einstein metric

Let
\[
M=X\# k\,\overline{\mathbb {CP}}^{\,2},\qquad
A=c_1^2(X),\qquad 1\le k<A/3,
\]
and let \(g\) be Einstein with \(\operatorname{Ric}=(s/4)g\), \(s<0\). Write \(K=c_1(K_X)\), and choose two blow-up basic classes
\[
a=K-\sum_{j\in J}E_j+\sum_{j\notin J}\epsilon_jE_j,
\qquad
b=a+2e,\qquad e=\sum_{j\in J}E_j .
\]
Put \(r=|J|\). Then
\[
e^2=-r,\qquad a\cdot e=r,\qquad b\cdot e=-r,\qquad a^2=b^2=A-k.
\]

## 1. The correct relative bundle

Let \(\mathfrak s_a,\mathfrak s_b\) be the corresponding spin\(^c\) structures, with positive spinor bundles \(V_a^+,V_b^+\) and determinant lines \(\mathcal L_a,\mathcal L_b\). There is a Hermitian line bundle \(E\) with
\[
c_1(E)=e
\]
such that
\[
V_b^\pm=V_a^\pm\otimes E,\qquad
\mathcal L_b=\mathcal L_a\otimes E^2.
\]
Thus it is \(E\), not \(E^2\), that twists the spinor bundle.

For determinant connections \(A_a,A_b\), the induced connection \(B\) on \(E\) is defined by
\[
A_b=A_a\otimes B^2.
\]
If
\[
f_a=-iF_{A_a},\qquad f_b=-iF_{A_b},\qquad f_B=-iF_B
\]
are real curvature forms, then
\[
f_B=\frac{f_b-f_a}{2},\qquad
\left[\frac{f_B}{2\pi}\right]=e.
\]

Take actual unperturbed Seiberg–Witten solutions
\[
D_{A_a}u=0,\quad f_a^+=q(u),\qquad
D_{A_b}v=0,\quad f_b^+=q(v),
\]
where \(u=\psi_a\), \(v=\psi_b\). Normalize \(q\) by
\[
|q(u)|^2=\frac{|u|^4}{8},
\]
so the spinor Weitzenböck equation is
\[
\nabla_{A_a}^*\nabla_{A_a}u+\frac{s+|u|^2}{4}u=0,
\tag{1.1}
\]
and similarly for \(v\).

The globally defined mixed fields are
\[
\Phi=v\otimes u^*\in \Gamma\!\left(E\otimes\operatorname{End}V_a^+\right),
\]
\[
\sigma=\operatorname{tr}\Phi=\langle u,v\rangle\in\Gamma(E),
\]
and
\[
\phi=\Phi-\frac{\sigma}{2}\operatorname{Id}
 \in\Gamma\!\left(E\otimes\operatorname{End}_0V_a^+\right)
 \cong\Gamma(E\otimes\Lambda^+_{\mathbb C}).
\]
No identification of \(u\) and \(v\) as spinors in the same bundle is being made.

Set
\[
U=|u|^2,\qquad V=|v|^2.
\]
Then
\[
|\Phi|^2=UV,\qquad
|\phi|^2=UV-\frac{|\sigma|^2}{2}.
\tag{1.2}
\]

## 2. Exact relative curvature identity

In a local unit frame for \(E\), the standard Fierz identity gives
\[
\langle q(u),q(v)\rangle
 =\frac{|\sigma|^2}{4}-\frac{UV}{8}.
\tag{2.1}
\]
Since
\[
f_B^+=\frac{q(v)-q(u)}{2},
\]
one obtains pointwise
\[
\boxed{\;
|f_B^+|^2
 =\frac{(U+V)^2}{32}-\frac{|\sigma|^2}{8}.
\;}
\tag{2.2}
\]
The right side is \(\ge0\), since \(|\sigma|^2\le UV\).

Chern–Weil for \(E\) gives
\[
4\pi^2e^2
 =\int_M f_B\wedge f_B
 =\int_M\left(|f_B^+|^2-|f_B^-|^2\right)d\mu.
\]
As \(e^2=-r\), this becomes
\[
\boxed{\;
\int_M|f_B^-|^2
 =4\pi^2r
 +\int_M\left[
 \frac{(U+V)^2}{32}-\frac{|\sigma|^2}{8}
 \right]d\mu .
\;}
\tag{2.3}
\]
In particular,
\[
\int_M|f_B^-|^2\ge 4\pi^2r.
\tag{2.4}
\]
This is the only immediate coercive statement supplied by the relative class. It is the standard curvature cost of a line bundle with \(e^2=-r\); it does not involve \(D_W\) or \(\int|W^+|^2\).

The mixed flux against the \(a\)-connection is also exact. Since \(a\cdot e=r\),
\[
4\pi^2r=\int_M f_B\wedge f_a.
\]
Using \(f_a^+=q(u)\) and (2.1),
\[
\boxed{\;
4\pi^2r
=\int_M\left[
\frac{|\sigma|^2}{8}
-\frac{U(U+V)}{16}
-\langle f_B^-,f_a^-\rangle
\right]d\mu .
\;}
\tag{2.5}
\]
The final term has both signs and carries precisely the exceptional flux not seen by the self-dual spinor equations.

Equations (2.3)–(2.5) are the polarization of
\[
f_b=f_a+2f_B,\qquad
b=a+2e.
\]
Indeed,
\[
\int f_b\wedge f_b-\int f_a\wedge f_a
 =4\int f_a\wedge f_B+4\int f_B\wedge f_B
 =16\pi^2(a\cdot e+e^2)=0.
\]
Thus the relative Chern identities add no curvature balance beyond the two individual Chern–Weil identities and the relation \(b=a+2e\).

## 3. Exact Bochner equations for \(\Phi,\sigma,\phi\)

Define
\[
C=\sum_i \nabla_i^{A_b}v\otimes
             \big(\nabla_i^{A_a}u\big)^*,
\qquad
c=\operatorname{tr}C,
\qquad C_0=C-\frac{c}{2}\operatorname{Id},
\]
and
\[
h=\frac{s}{2}+\frac{U+V}{4}.
\]
Applying the product rule to (1.1) and its \(b\)-analogue gives
\[
\boxed{\;
\nabla^*\nabla\Phi+h\Phi=-2C,
\;}
\tag{3.1}
\]
hence
\[
\boxed{\;
\nabla_B^*\nabla_B\sigma+h\sigma=-2c,
\;}
\tag{3.2}
\]
and
\[
\boxed{\;
\nabla^*\nabla\phi+h\phi=-2C_0.
\;}
\tag{3.3}
\]

The integrated scalar mixed identity is
\[
\boxed{\;
\int_M|\nabla_B\sigma|^2
+\int_M h|\sigma|^2
=-2\operatorname{Re}\int_M\langle c,\sigma\rangle .
\;}
\tag{3.4}
\]
The right side is an uncontrolled correlation of the two spinor derivatives. It is not a zero-counting term.

To display \(W^+\), identify \(\operatorname{End}_0V_a^+\) with
\(\Lambda^+_{\mathbb C}\). For an \(E\)-valued self-dual two-form \(\zeta\),
\[
P_+\Delta_B\zeta
 =\nabla_B^*\nabla_B\zeta
 +\left(\frac{s}{3}\operatorname{Id}-2W^+\right)\zeta
 +\mathcal K_B^+\zeta,
\tag{3.5}
\]
where, with \(d_B^2=F_B\wedge\),
\[
\mathcal K_B^+
=P_+\left[
\sum_{i,j}e^i\wedge\iota_{e_j}\,
F_B(e_j,e_i)
\right]P_+.
\]
Substituting (3.3) yields
\[
\boxed{\;
P_+\Delta_B\phi
=-\left(\frac{s}{6}+\frac{U+V}{4}\right)\phi
-2W^+(\phi)+\mathcal K_B^+\phi-2C_0 .
\;}
\tag{3.6}
\]
Therefore
\[
\begin{aligned}
\int_M\bigl(|d_B\phi|^2+|d_B^*\phi|^2\bigr)
={}&-\int_M\left(\frac{s}{6}+\frac{U+V}{4}\right)|\phi|^2\\
&-2\operatorname{Re}\int_M\langle W^+\phi,\phi\rangle
+\operatorname{Re}\int_M\langle\mathcal K_B^+\phi,\phi\rangle\\
&-2\operatorname{Re}\int_M\langle C_0,\phi\rangle .
\end{aligned}
\tag{3.7}
\]
This is the exact mixed Weyl identity. It contains:

* a directional Weyl term \(\langle W^+\phi,\phi\rangle\), not \(|W^+|^2\);
* a relative-curvature term with no fixed sign;
* the derivative correlation \(C_0\), also with no fixed sign.

There is a second useful form involving the ordinary self-dual form
\[
\alpha=f_B^+=\frac{q(v)-q(u)}2.
\]
The self-dual two-form Weitzenböck identity gives
\[
\boxed{\;
2\int_M|d\alpha|^2
=\int_M\left(
|\nabla\alpha|^2+\frac{s}{3}|\alpha|^2
-2W^+(\alpha,\alpha)
\right)d\mu .
\;}
\tag{3.8}
\]
Since \(df_B=0\),
\[
d\alpha=-df_B^-.
\]
Thus the Weyl term is balanced by derivatives of the unconstrained anti-self-dual relative curvature.

For an Einstein metric,
\[
\delta W^+=0,
\]
and \(W^+\) separately satisfies
\[
\nabla^*\nabla W^+
+\frac{s}{2}W^+
-6(W^+\circ W^+)_0=0,
\]
hence
\[
\int_M\left(
|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+
\right)d\mu=0.
\tag{3.9}
\]
Combining (3.6) with \(\delta W^+=0\) does not remove \(C_0\) or
\(\mathcal K_B^+\). Integration by parts merely replaces them by the corresponding mixed spinor and relative-connection currents. No unweighted \(\int|W^+|^2\) term results.

## 4. Zero set and exceptional flux

The section
\[
\sigma=\langle u,v\rangle\in\Gamma(E)
\]
is genuine. If transverse, its zero surface represents \(\operatorname{PD}(e)\), and
\[
[Z_\sigma]^2=e^2=-r.
\]
For any closed two-form \(\eta\),
\[
\int_{Z_\sigma}\eta
=e\cdot[\eta]
=\frac1{2\pi}\int_M f_B\wedge\eta.
\tag{4.1}
\]
But \(\sigma\) satisfies the inhomogeneous equation (3.2), not a covariant holomorphic or vortex equation. Consequently its zero current has no positivity relation with \(|\sigma|\), \(f_B^+\), or \(W^+\).

On \(\{U>0\}\), the spinor determines the length-\(\sqrt2\) self-dual form
\[
\omega_u=\frac{4q(u)}{U}.
\]
The exact pointwise relative flux is
\[
\boxed{\;
f_B\wedge\omega_u
=\left(
\frac{|\sigma|^2}{2U}-\frac{U+V}{4}
\right)d\mu .
\;}
\tag{4.2}
\]
In general \(\omega_u\) is neither globally defined across the zeros of \(u\) nor closed. Therefore (4.2) does not compute \(e\cdot[\omega_u]\). The globally valid replacement is the unnormalized formula
\[
f_B\wedge q(u)
=\left(
\frac{|\sigma|^2}{8}-\frac{U(U+V)}{16}
\right)d\mu
-f_B^-\wedge f_a^-,
\]
which is exactly (2.5).

Only when the individual scalar estimate is saturated does \(\omega_u\) become parallel and closed.

## 5. Relation with the individual scalar estimates

For \(t=-s>0\), equation (1.1) gives
\[
4\int|\nabla u|^2+\int(U^2-tU)=0.
\tag{5.1}
\]
Since \(f_a^+=q(u)\),
\[
4\pi^2(a^+)^2\le\int|q(u)|^2=\frac18\int U^2.
\]
More precisely,
\[
\boxed{\;
S-32\pi^2(a^+)^2
=
\int(U-t)^2
+8\int|\nabla u|^2
+8\left(\int|q(u)|^2-4\pi^2(a^+)^2\right).
\;}
\tag{5.2}
\]
Every term on the right is \(\ge0\). Thus saturation gives
\[
|u|^2=t=-s,\qquad \nabla u=0,
\tag{5.3}
\]
with the requested normalization. The same holds for \(v\) if its scalar estimate is also saturated.

If both estimates are saturated, then \(h=0\), \(C=0\), and \(\Phi,\sigma,\phi\) are parallel. There are two possibilities:

1. \(\sigma\not\equiv0\). Then \(\sigma\) is a nowhere-zero parallel section of \(E\), forcing \(e=0\) in real cohomology, contrary to \(e^2=-r\).

2. \(\sigma\equiv0\). Equal-length orthogonal spinors in complex rank two satisfy
   \[
   q(v)=-q(u).
   \]
   The two parallel forms define the complex structures \(J\) and \(-J\), so the corresponding determinant classes obey \(b=-a\). Together with \(b=a+2e\), this gives \(a=-e\), contradicting
   \[
   a^2=A-k>0,\qquad e^2=-r.
   \]

Thus two distinct signed classes cannot simultaneously attain their individual scalar equalities. This is an equality-rigidity reformulation; the one-field equality theory already produces a parallel Kähler form and supplies the same obstruction mechanism on a blow-up.

For all sign choices \(c_\epsilon=K+\sum\epsilon_iE_i\),
\[
2^{-k}\sum_\epsilon (c_\epsilon^+)^2
=|K^+|^2+\sum_i|E_i^+|^2\ge A.
\tag{5.4}
\]
This recovers the signed scalar estimate, but there is no general lower bound
\[
\sum_i|E_i^+|^2\ge k.
\]
The exceptional classes may be almost entirely anti-self-dual. That is exactly the configuration in which the relative flux is carried by \(f_B^-\).

## 6. The Weyl-deficit endpoint

For an Einstein metric,
\[
D_W=\frac{S}{16}-2\pi^2(A-k).
\]
Hence
\[
D_W=4\pi^2k
\quad\Longleftrightarrow\quad
S=32\pi^2(A+k).
\tag{6.1}
\]
At this value,
\[
\int_M|W^+|^2
=\frac{S}{24}-D_W
=\frac{4\pi^2}{3}(A-2k).
\tag{6.2}
\]
For \(k<A/3\), this is strictly positive and is fully consistent with the Einstein Chern–Weil relation
\[
\int_M\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu
=4\pi^2(A-k).
\tag{6.3}
\]

The one-field LeBrun Weyl estimate
\[
\int_M\bigl(s-\sqrt6|W^+|\bigr)^2d\mu
\ge72\pi^2(c^+)^2
\]
implies the weaker curvature combination
\[
\int_M\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu
\ge\frac{8\pi^2}{3}(c^+)^2.
\]
Using a signed class with \((c^+)^2\ge A\), the Einstein relation has slack
\[
4\pi^2(A-k)-\frac{8\pi^2}{3}A
=4\pi^2\left(\frac A3-k\right)>0.
\tag{6.4}
\]
Thus \(D_W=4\pi^2k\), or \(D_W\) close to it, does not force either spinor to be close to the scalar equality state \(|\psi|^2=-s\). Relative anti-self-dual curvature can carry the fixed amount \(4\pi^2r\) in (2.3) while the individual scalar and Weyl inequalities retain the slack shown above.

## Verdict

The mixed construction is globally well-defined only after using
\[
V_b^+=V_a^+\otimes E,\qquad c_1(E)=e,
\]
and taking the relative connection to be half the determinant-connection difference. Its exact output is:

* the relative curvature formula (2.2);
* the topological anti-self-dual energy identity (2.3);
* the flux identity (2.5);
* the inhomogeneous Bochner equations (3.2), (3.6), and (3.8).

These do **not** yield a stronger lower bound for \(D_W\), a stronger bound for \(\int|W^+|^2\), or a signed exceptional-flux inequality beyond the individual LeBrun estimates. The curvature identities are polarizations of the two individual Seiberg–Witten/Chern–Weil balances. The mixed Bochner identity retains the derivative source \(C_0\) and the relative-curvature term, while the topology \(e^2=-r\) is absorbed by \(f_B^-\).

Simultaneous exact scalar saturation is impossible, but \(D_W=4\pi^2k\) is not simultaneous scalar saturation and remains algebraically consistent throughout \(1\le k<A/3\). A genuinely stronger Einstein obstruction would require an additional relation controlling \(f_B^-\) or \(C_0\), or a geometric equation making \(\sigma\) holomorphic or vortex-like. The Einstein identities \(\delta W^+=0\) and (3.9) alone do not provide such a relation.