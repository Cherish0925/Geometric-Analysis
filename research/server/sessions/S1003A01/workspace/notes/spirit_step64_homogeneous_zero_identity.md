# Spirit follow-up to Step 64: the ten quadrics are coefficients of one homogeneous identity

This is a focused derivation for Core's independent verification and integration. It uses the harmonic-form and Einstein Weyl equations already proved in Step 62. It does not use numerical completeness of the Step-64 obstruction, does not establish analytic realization of a jet, and makes no priority claim.

## 1. What the unread intrinsic result actually says

`data/step64/intrinsic_lam-1.0_s0.json` has a 16-dimensional intrinsic coordinate map and ten independent quadratic conditions. Its sixth stored invariant fit is

`|delta|^2 + (4/15)|Q|^2 - (4/15)|P|^2`

with relative residual `3.043392342923468e-12`. Thus the proposed `15/4` trace relation is supported by the saved data. The other nine SVD basis vectors need not themselves be invariant scalars.

There is a geometric explanation of the entire ten-dimensional space. It is the coefficient space of a homogeneous real quadratic polynomial in the four source coordinates, obtained from the lowest-order part of the exact scalar Delta-q equation. The short comparison script `scripts/spirit_step64_homogeneous_quadric_check.py` constructs these ten coefficient quadrics and compares their span with the saved matrices. All principal-angle cosines are 1 to numerical precision; the largest relative projection error is `6.24e-9`, consistent with the saved matrices being rounded to eight decimals. Its surface restriction has rank three, also matching Step 64. Output is `data/spirit_step64/homogeneous_quadric_comparison.json`.

This is a comparison of necessary equations, not a proof that they exhaust nonlinear jet compatibility.

## 2. Exact scalar identity before taking a leading term

Use Delta=tr(nabla^2), u=Omega/sqrt(2), q=|nabla Omega|^2, and the Step-62 block convention

 W+ = [[r,eta^T],[eta,-r I/2+V]],  r=s/6+q/4.

The harmonic-form and Einstein Weyl equations are

 Delta u=-2W+ u+(s/3)u,
 Delta W+=(s/2)W+-6(W+)^2+2|W+|^2 I.

The AAD gauge gives

 sum_i (nabla_i u) tensor (nabla_i u) = (q/4) I on u-perp.

Applying the product rule to r yields the exact identity

 Delta q = 8 tr(V^2)-24|eta|^2-(3s/2)q-(9/4)q^2
           +16 sum_i <(nabla_i W+) nabla_i u,u>.                 (G)

For clarity, the algebraic terms in Delta r are

 (7s/6)r-7r^2-(q/2)r-6|eta|^2+2tr(V^2),

which become `-(3s/8)q-(9/16)q^2-6|eta|^2+2tr(V^2)` after substituting r. Equation (G) does not drop the derivative source that obstructed earlier scalar coercivity.

## 3. Leading homogeneous compatibility at any finite-order torsion zero

At a torsion zero of order m>=1, take normal coordinates and an AAD gauge at the point. Encode the leading coefficient of a by f_m in C^2, with q leading term 4|f_m|^2. The principal half-twistor equation gives

 f_m(z,bar z)=z h(bar z)+g(bar z),

where h is scalar homogeneous of degree m-1 and g is C^2-valued homogeneous of degree m. Put w=bar z,

 B(z,w)=z tensor D_w h+D_w g,   A=(B-B^T)/2,   S=(B+B^T)/2.

The complex-linear derivative is h I. To leading order the exact Step-62 coframe dictionary gives

 |eta|^2=4|h|^2,  tr(V^2)=4||A||^2,
 ||Df_m||_R^2=4|h|^2+2||A||^2+2||S||^2.

The mixed derivative term in (G) has leading part

 sum_i <(nabla_i W+) nabla_i u,u>
 = -4 Re sum_j conjugate(f_m,j) (partial_{w_j}h).

Indeed eta=(-2 Re h,-2 Im h), and in the AAD expression nabla u=a tensor(phi/sqrt2)-Ja tensor(psi/sqrt2) the contraction is `a·d eta_1-Ja·d eta_2`. Since h is antiholomorphic in z, this equals the displayed expression.

At degree 2m-2, the s q and q^2 terms in (G) vanish. Metric/frame correction terms are of higher degree. Also Delta_flat f_m=4 D_w h. Comparing both sides therefore gives the pointwise polynomial identity

 ||A||^2-||S||^2-8|h|^2
 -6 Re sum_j conjugate(f_m,j) (partial_{w_j}h) = 0.             (H_m)

For m=1 this is exactly the Step-62 cone. For m=2, its ten real source-coordinate coefficients are precisely the quadrics compared in section 1. Its spatial trace is `-8` times

 ||Q||^2-|P|^2+(15/4)|delta|^2,

with the conventions of `step64_intrinsic_quadric.py`. The comparison script verifies that trace identity exactly using dyadic coefficients. Thus the nine additional numerical relations need not be interpreted as unrelated new tensor obstructions: they retain the directional coefficients discarded when taking the trace.

## 4. An all-orders leading classification suggested by (H_m)

The following short argument appears to give a stronger result than going to one additional degree. Core should check the geometric leading-term passage and the bundle conventions before promoting it.

Assume m>=2. Regard h and g as holomorphic polynomials in w. Euler homogeneity transforms (H_m) into

 tr(conjugate(Dg) Dg) + (m+1)(m+3)|h|^2
 +2(m+3) Re sum_i conjugate(g_i) partial_{w_i}h = 0.           (I_m)

The first two terms have bidegree (m-1,m-1), whereas the last term has bidegrees (m,m-2) and (m-2,m). These are distinct, so

 sum_i conjugate(g_i) partial_{w_i}h=0,                       (J_m)
 tr(conjugate(Dg) Dg)+(m+1)(m+3)|h|^2=0.                     (K_m)

### Why h must vanish

If the two polynomial components of g are complex-linearly independent, (J_m), viewed as an identity in independent w and bar w variables, forces both partial derivatives of h to vanish; homogeneity then gives h=0.

Otherwise g takes values in a fixed complex line. After a unitary change of coordinates and gauge take g=(G,0). Equation (J_m) forces partial_{w1}h=0 unless g=0, a case settled directly by (K_m). But then

 tr(conjugate(Dg) Dg)=|partial_{w1}G|^2>=0,

so (K_m) again forces h=0. Thus h=0 for every m>=2.

### Why the remaining derivative has only one matrix direction

The Hermitian form on 2x2 complex matrices

 H(M,N)=tr(conjugate(M) N)

(where conjugation is entrywise, not adjoint) has signature (3,1):

 H(M,M)=|M11|^2+|M22|^2+2 Re(conjugate(M12) M21).

Write the holomorphic homogeneous matrix Dg(w) as a sum of its coefficient matrices times monomials. Equation (K_m) with h=0 says that all Hermitian pairings between these coefficient matrices vanish: the mixed monomials w^alpha bar(w)^beta are independent. Their span is therefore totally isotropic, of complex dimension at most one. Hence

 Dg(w)=M p(w)

for one constant matrix M and a scalar homogeneous polynomial p of degree m-1.

Equality of mixed partial derivatives shows that M cannot have rank two when m>=2, since rank two would force Dp=0. Thus M=v tensor ell has rank one. The same equalities force p to be a multiple of `(ell·w)^(m-1)`. Finally H(M,M)=0 is

 |ell·conjugate(v)|^2=0.

Integrating gives

 g(w)=kappa v (ell·w)^m,    ell·conjugate(v)=0.

After a unitary frame choice, the resulting normal form is

 **f_m(z)=kappa (bar z_2)^m e_1,  m>=2.**                    (L_m)

This is the Gibbons–Hawking-type leading form, not an analytic-germ classification. At m=1 the bidegree argument is absent and the larger Step-62 cone survives, as it must.

## 5. What this does and does not say about the compact winding problem

- If confirmed, (L_m) supplies one necessary leading normal form at every higher-order torsion zero, with no dependence on the sign of s. It replaces an indefinite sequence of separate degree tests for this particular leading question.
- The leading polynomial vanishes along a J-complex plane. Higher Taylor coefficients may change the actual zero set, so this does NOT exclude a degenerate isolated zero or establish a smooth zero surface.
- At an exceptional point on a smooth zero surface with dense rank-two locus, the Step-64 surface constraints and m=2 trace relation kill the tangential linear part of W3+|C. They do not determine its winding. More generally the lowest total-degree torsion term may be purely normal, while the coefficient of the first normal derivative varies only at higher total degree along C.
- This is why a normal expansion along the rank-two surface, retaining the connection and its second fundamental form, may be more informative for the global degree than simply increasing total Taylor degree at one exceptional point. The real target is the equation for b=W3+|C and whether its coefficients remain controlled through b=0.
- The Step-64 statement 'vanishing linear part implies the winding cannot be +/-1' is false for a general smooth or analytic section. In a local trivialization, b(z)=z|z|^2 has zero linear part and winding +1, while b(z)=bar z|z|^2 has winding -1. Multiplicity and winding must remain separate until the PDE gives the needed structure.
- Likewise, an inequality |dbar_C b|<=C|b| only on C minus its zeros is useful for a similarity principle if the coefficient control extends appropriately through the zeros. A pointwise bound with C blowing up like 1/|b| gives no winding restriction.

The geometric argument in sections 2–4 is the part needing Core's independent scrutiny. The numerical comparison in section 1 supports its match with the existing calculation but does not replace that argument.
