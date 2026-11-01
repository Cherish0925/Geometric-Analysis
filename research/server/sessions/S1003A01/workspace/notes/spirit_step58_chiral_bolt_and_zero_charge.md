# Spirit follow-up to Step 58: short chiral calculation, polar extension, and the zero-charge question

These are focused deductions to simplify the next Core argument. They do not replace Core's independent geometric reading or the unresolved identification against prior literature.

## 1. The all-p chiral check does not require square roots of all metric coefficients

Use the Step-58 exact h_i,W_i in Q(p,y), the same positive y and geodesic derivative. Put, cyclically,

C_i=W_j+W_k-W_i,    b_i=h_i-C_i,    d_i=h_i+C_i.

For the oriented orthonormal coframe,

de^i=h_i e^0 wedge e^i+2W_i e^j wedge e^k.

Cartan's equation gives the spatial connection coefficient omega^j_k=C_i e^i and omega^i_0=h_i e^i. Accordingly the two chiral connection triples can be represented by b_i e^i and d_i e^i, with opposite cross-product signs. Their curvature components are

F_i^+=(b_i'+h_i b_i)e^{0i}+(2W_i b_i+b_j b_k)e^{jk},
F_i^-=(d_i'+h_i d_i)e^{0i}+(2W_i d_i-d_j d_k)e^{jk}.

With the usual curvature-operator convention consistent with Ric=-3g, the corresponding R^+ eigenvalues are minus the radial F^+ coefficients; trace-free vanishing is insensitive to a simultaneous overall curvature sign.

Exact substitution and rational reduction in the **existing** quadratic field gave, for every i,

 d_i'+h_i d_i=1,
 2W_i d_i-d_j d_k=-1,
 b_i'+h_i b_i=2W_i b_i+b_j b_k.

Thus F_i^-=e^{0i}-e^{jk}: its curvature block is scalar, and W^-=0 identically. This avoids expanding nine metric square roots. The three W^+ eigenvalues, in the omega_i basis and operator normalization, are

w1=-4(9p^6-18p^5-9p^4-6p^3+9p^2-1)/(3p^2+1)^3,
w2=-4(9p^6+18p^5-9p^4+6p^3+9p^2-1)/(3p^2+1)^3,
w3=8(9p^6-9p^4+9p^2-1)/(3p^2+1)^3.

They were computed as 1-(b_i'+h_i b_i). They agree with the Step-58 point matrices after converting the script's unnormalized, opposite-sign curvature convention. In particular their limits at p=1 are (1,-2,1), the CH spectrum at s=-12.

In the form-norm convention eta=W^+(Omega)_{Omega-perp}, the two active components give directly

|eta|^2=2 X1 X2 (w1-w2)^2
=-18(p-1)^3(p+1)^3(3p-1)(3p+1)/(3p^2+1)^4,

|W3^+|^2=[X2 w1+X1 w2-w3]^2/2
=81(p-1)^4(p+1)^4(3p-1)^2(3p+1)^2/[2(3p^2+1)^6].

These are exactly the formerly conditional profiles. The mathematical bridge to check is the displayed small Cartan calculation, not another large all-p curvature expansion. The known AK balance therefore remains a genuine identity of this pair once that bridge is accepted. All recorded radial integrals still multiply the chosen invariant orbit volume integral of sigma123.

## 2. A polar expression supplies the missing all-orders bolt test

Let r be the outward geodesic coordinate. The exact rational coefficients imply p-1/3 is real-analytic in r^2, with leading term 2r^2/9. Thus a1=r times a positive analytic function of r^2, a2,a3 and x1 are analytic in r^2, and x2=r times an analytic function of r^2 on the chosen ray.

Fix the compact generator to have period 2pi. Locally over the bolt choose an angle theta and base connection A such that

sigma1=dtheta+A,    sigma2+i sigma3=e^{2i theta} eta0,

where eta0 is a local complex horizontal coframe. These transformation laws follow from L_{E1}(sigma2+i sigma3)=2i(sigma2+i sigma3). Put z=r e^{i theta} and Dz=dz+i z A. Then

dr+i r sigma1=e^{-i theta}Dz,
dr-i r sigma1=e^{i theta}Dbar z.

For the metric:

- dr^2+a1^2 sigma1^2=|Dz|^2+[(a1^2-r^2)/r^4](Im(bar z Dz))^2;
- the horizontal mean is analytic in |z|^2 times |eta0|^2;
- the horizontal anisotropy is [(a2^2-a3^2)/(2r^4)] Re(z^4 eta0^2).

The existing exact expansion a2^2-a3^2=(10/3)r^4+O(r^6), together with analyticity in r^2, therefore gives precisely the required smooth divisibility. The limiting metric is positive.

For the mixed Omega component define

Cdr=sqrt(X2 A2),    Ctheta=sqrt(X2 A3 A1),
fplus=(Cdr+Ctheta/r)/2,    fminus=(Cdr-Ctheta/r)/2.

Then exactly

Omega2=Re{[(fplus/r) z Dz+(fminus/r^3) z^3 Dbar z] wedge eta0}.

Step 58 gives Cdr=4r+O(r^3), Ctheta=4r^2+O(r^4), and both are respectively r and r^2 times analytic functions of r^2. Hence fplus/r and fminus/r^3 are analytic at r=0. No further parity conditions at higher orders are missing. Omega1 is also smooth: x1 a1 dr wedge sigma1 is an analytic multiple of the normal area form, and x1 a2 a3 sigma2 wedge sigma3 is an analytic multiple of the base area form. At the bolt the form remains nondegenerate; closure and norm extend by continuity.

This is a direct local slice argument, subject to fixing the global group and period as above. It is substantially stronger than checking finitely many series coefficients, because analyticity and exact divisibility establish all orders.

### Period and normal Euler sign

For the stated structure constants, one compact generator is the matrix [[0,1],[-1,0]] in sl(2,R), with period 2pi; its adjoint action on the horizontal plane has weight two. A torsion-free lift to SL(2,R) of a cocompact surface group, avoiding the central element, is the natural quotient to use. Such lifts correspond to spin structures on the oriented hyperbolic surface.

The normal Euler sign should be derived in the Omega-induced orientations, not guessed from the phrase 'spin bundle'. At the bolt, the normal connection rotation is sigma1, whereas the tangent connection rotation is -2 sigma1. Thus c1(normal)=-c1(TSigma)/2, giving degree g-1 for a genus g bolt, i.e. topologically a square root of K_Sigma with this complex orientation. This also follows from d sigma1=-2 sigma2 wedge sigma3 and the normal Chern convention calibrated against the tangent Euler class. It corrects the earlier unverified sign guess used in a search description; no prior theorem depended on that guess. Core should fix this convention explicitly in the global construction.

## 3. What a zero-locus attack must add

For an AK four-manifold the torsion is a section of the complex rank-two bundle

E=Lambda^{0,1} tensor Lambda^{0,2},

with c2(E)=c2(TM)+2c1(TM)^2=5chi+6tau. On a closed Einstein four-manifold with nonzero scalar curvature,

5chi+6tau=chi+2(2chi+3tau)>0.

This is stronger research guidance than merely asserting that a zero exists: the zero set has a nontrivial localized top Chern class. If zeros are isolated, their signed local indices sum to this positive integer. In general neither isolatedness nor positivity of individual indices follows; use a localized class rather than silently perturbing the actual solution to achieve transversality.

Ordinary strong unique continuation cannot exclude a finite-order zero. For unrestricted Einstein AK pairs, the cited AAD unique-continuation/classification results also retain additional curvature hypotheses; their Proposition 3 treats zeros in the third-Gray branch using its opposite Kahler structure and extra integrability, not analyticity alone.

There is a simple principal-part warning. At a zero, choose J-standard coordinates and a unitary L-frame. The type-constrained off-diagonal field can be written alpha=f1 dbar z1+f2 dbar z2. The leading condition (d alpha)^-=0 says

partial_z1 f2=partial_z2 f1=0,    partial_z1 f1=partial_z2 f2.

For linear f this permits f=c z+B bar z. In particular f=z has an isolated positive-degree coefficient-map zero and satisfies this necessary principal condition; its nonzero divergence is an eta source. It is NOT a constructed Einstein AK germ or a solution of all prolonged AAD equations. It shows why a zero-index obstruction cannot come from the type condition and this principal symbol alone. A useful zero argument must show what additional nonlinear curvature/prolongation or global comparison rules out the locally permitted positive charge. Conversely, if a finite-order zero survives the full equations, zero existence alone will not settle closed Goldberg.

The verified strict example remains an essential control: it realizes the open q>0 geometry and even the familiar finite torsion budgets, while avoiding the required zero charge by sending q to zero only at infinity.
