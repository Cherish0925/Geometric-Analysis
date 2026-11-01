---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Full text of "Curvature Functionals, Optimal Metrics, and the Differential....]

At this point, we have constructed an interesting family of locally conformally 
flat metrics on the orbifold X — T/Z2, where Y — 2(S 1 x S* 3 ). However, our aim is 
to eventually smooth the orbifold singularities of these metrics in order to produce 
a similar family of anti-self-dual metrics on a simply connected manifold. To carry 
this out, we will need to know that the Kodaira-Spencer deformation theory is 
unobstructed for the corresponding family of twistor spaces. In fact, the relevant 
vanishing theorem easily follows from a decade-old unpublished paper of Eastwood 
and Singer |18| . whose beautiful ideas will be given a self-contained exposition in 
this section. 

Let (Y, g) be an oriented, locally conformally flat Riemannian 4-manifold, and 
let c <a denote the complete presheaf of conformal Killing fields on (Y, g), defined by 
setting 

for any open set U C Y; here, as throughout, £ is used to indicate the C°° sections 
of a given vector bundle. Now observe that there is a rank-15 vector bundle F — > Y, 
equipped with a flat connection V, such that is the sheaf of parallel sections of 
(F, V). Indeed, if U C Y is any simply connected open set, then we can conformally 
immerse U onto an open subset of S* 4 by means of the developing map [41) , and ^7 is 
thereby identified with the 15-dimensional space so(5, 1) of global conformal Killing 
fields on the round 4-sphere S 4 . As we pass from one such choice of U to another, 
these identifications will be related to one another by elements of SO^ (5, 1), acting 
on so (5, 1) via the adjoint representation. These elements of SO^ (5, 1) are exactly 
the transition of functions of F, relative to a collection of local trivializations of F 
in which the flat connection V has vanishing connection 1-forms. 

Now we could certainly construct a fine resolution of ^ by just considering 
the .F-valued differential forms on Y, but this would involve using vector bundles 
of rather high rank. A more efficient resolution was first discovered by Gasqui 
and Goldschmidt [24] using Spencer cohomology, and later rediscovered by East- 
wood and Rice |17j in the setting of Bernstein-Gelfand-Gelfand resolutions. This 
resolution takes the form 

where Qq indicates the trace-free symmetric-tensor-product of a vector bundle with 
itself. Here Lq is the first-order operator 

which measures the way the conformal class [g] is distorted by the the flow of a 
given vector field. The next step in the sequence is the linearization L\ — DW of 
the Weyl curvature tensor; and for our purposes, it will be important to recognize 
this second-order differential operator can be decomposed as DW = DW++DW-, 
where the operators 

Vu = {v € £u(TY) I £ v g^g} 

0i 

Lq(v) — trace-free part of £ v g 

DW+ : £ (©gA 1 ) 
DW~ : ^(©gA 1 ) 

£(Q 2 A+) 
£{Q 2 A-) 

28 

CLAUDE LEBRUN 

are the linearizations 

DW ± (h) = ±W±(g + th) 

at t=o 

of the self-dual and anti-self-dual Weyl curvatures. The next step is again a second- 
order operator, and is given by 

L 2 = (DW+)* - {DW-f. 

The sequence then culminates with the first-order operator 

L3 = L*)- 

Clearly, all of these operators are conformally invariant, provided that each bundle 
in the complex is given the correct conformal weight. 

Since each of the sheaves in the Gasqui-Goldschmidt resolution is fine, and 
hence acyclic, the abstract de Rham theorem |58j immediately tells us that the 
sheaf cohomology of Y with coefficients in ^ is exactly the cohomology of the 
corresponding complex of global sections: 

HP(Y,^)= kerLp . 

im Lp-i 

However, the Gasqui-Goldschmidt resolution is also an elliptic complex; thus, pro- 
vided Y is compact, we have 25 

H p (Y^) =keri p nkeri;_ 1 , 

by a generalized form of the Hodge theorem. Since 

DW± = 1 -{L\±L 2 ), 

this immediately gives us the following result: 

Proposition 8.1. Let (Y,g) be any compact, oriented, locally conformally flat 
A-manifold. Then 

H 2 {Y,tf) = ker(DW+)*®ker(DW-)* 

c M©oA+) e £y(q 2 a + ). 

Using this key observation, it is now easy to deduce the desired vanishing result: 

Theorem 8.2 (Eastwood-Singer). Let g be any conformally fiat metric on the 
oriented A-manifold 

Y = fc(5 1 x S 3 ) = (S 1 x S* 3 )# • ■ ■ #(S' 1 x S 3 ), 

k 

k > 1, and let Z be the twistor space of (Y,g). Then 

DW+ : EiQlA 1 ) -> £ (Q 2 A + ) 

is surjective on (Y,g), and 

H 2 (Z,0(TZ)) = 0. 

Proof. By Serre duality, H 2 (Z,0(TZ)) is the dual of B X {Z, O x (if)). How- 
ever, the latter sheaf cohomology group corresponds, via the Penrose transform 
0, to C ® ker(DVT+)*. By Proposition 18.11 it therefore suffices to show that 
H 2 (Y, ff) = 0, where ^ is once again the sheaf of local conformal Killing fields of 
[<?]■ 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

29 

Now Y can be obtained from 5 4 by replacing k pairs of balls with k tubes 
modeled on S 3 x E. This allows us to express Y as the union 

of open sets 

and 

such that 

Y = UU V 

U = S 4 - {pi, . . . ,p 2 k} 
V w (S 3 x E) U ■ ■ • U (S 3 x E) 

k 

U n V w (S 3 x E) U • • • U (S 3 x M 

2/,' 

We may thus proceed by examining the Mayer- Vietoris sequence 

(12) -> /^([/Tl V,<af) -> i? 2 (C/U V,*af) -> H 2 {U^)®H 2 {V,^) -»■••■ 

Indeed, notice that and J7 n V are homotopy equivalent to disjoint unions of 
3-spheres, while U is homotopy equivalent to a bouquet of 3-spheres. In particular, 
each of these sets is a disjoint union of simply connected spaces. Since is the 
sheaf of covariantly constant sections of a flat rank-15 vector bundle (F, V), the 
restriction of to any of these open sets may be identified with the constant sheaf 
E 15 , and the relevant sheaf cohomology therefore amounts to singular cohomology 
with coefficients in the Abelian group E 15 . By the homotopy invariance of singular 
cohomology, we thus have 

H 1 (UnV,'if) = g 1 ( ^ 3 U- - -US 3 # ,R 15 ) = 

2k 

H 2 {U^) s H 2 ( S 3 V ■ ■ ■ V S 3 y , E 15 ) = 

2fe-l 

H 2 {VX) = g 2 (S 3 U---U5 3 ,,M 15 ) = 0, 

fc 

and l|12|l therefore tells us that 

H 2 (Y, c i) = H 2 (U U V, c i) = 0, 
as claimed. □ 

It is perhaps worth remarking that, for any compact oriented locally confor- 
mally flat 4-manifold (Y, g), one may use the index theorem to show that ker(DW+)* 
and ker(_DW / _)* have the same dimension. Proposition 18 . II and the Penrose trans- 
form therefore imply that 

dim R iJ 2 (y,^) = 2 dime H 2 (Z,0(TZ)). 

Thus the vanishing of H 2 (Y,^) is actually necessary, as well as sufficient, for the 
deformation theory of Z to be unobstructed. 

30 

CLAUDE LEBRUN 

9. Existence Results 

We will now assemble the results of the last several sections into a proof of 
Theorem El 

Proposition 9.1. For any integer k > 6, the connected sum 

kCP 2 = CP 2 #---#CP 2 

k 

admits a real-analytic 1 -parameter family of anti- self- dual conformal metrics \gt\, 
t € [a, b], such that [g a ] contains a metric with s > everywhere, while [g^] contains 
a metric with s < everywhere. 

PROOF. We once again let Y — (S 1 x S' 3 )#(S' 1 x S" 3 ), and let X = Y/Z 2 . 
Equip X with a conformally-flat scalar-flat orbifold metric go which belongs to a 
real-analytic 1-parameter family of conformally flat metrics gt, t € (— e, e) such that 
each g t has s > when t < 0, s < when t > 0, and ker(A + s/6) = for all f 7^ 0; 
for example, Proposition 17.11 constructs such a family, after replacing t with t — to 
for some to- Since Theorem 18.21 guarantees that the twistor space Z of (Y,go) has 
H 2 (Z, G(TZ)) = 0, Theorem IOI therefore tells us that, for any integer t > 0, there 
exists a connected 2-parameter family of anti-self-dual conformal metrics [(7( Ui ,u 2 )]j 
(111,112) € (0, e) x (— e, e) on X^£CP 2 which arises from a 2-parameter standard 
deformation of the singular space Zq — [Z j r L 2 \^>Z eh^Z p s\ here X is once again the 
oriented 4-manifold obtained from the orbifold X by replacing each singular point 
of X with a 2-sphere of self- intersection —2. Moreover this 2-parameter standard 
deformation can be chosen so that its restriction to u 2 — t is a 1-parameter standard 
deformation of the complex 3- fold with normal crossings arising from (X, [gt]), for 
every real number t in a neighborhood of 0. Let a < and b > be choices of t 
in this neighborhood. Theorems 16.31 and 16.41 then tell us that for any sufficiently 
small w > 0, the conformal class [<?(«;, )] contains a metric with s > 0, while the 
conformal class [g( Wi b)] contains a metric with s < 0. Thus [174] := a < t < b, 

is a family of ASD conformal metrics on X#£CP 2 with the desired scalar-curvature 
behavior . 

It remains only to unmask the identity of the manifold X#£CP 2 . To do this, 
first notice we may cut up Y into three punctured 4-spheres 

in a manner which is compatible with the involution. Thus X can be expressed as 
a connected sum 

x = vww 

of three copies of the orbifold S 4 /Zi 2 , where the connect sum is carried out in the 
vicinity of non-singular points of V, and where the Z 2 acts on S 4 C K 5 by reflection 
through an axis. Hence 

x = vww, 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

31 

where V is obtained from V by replacing the two isolated singularities of V = S 4 /Z2 
by 2-spheres of self-intersection —2. However, CP2#CP2 is diffeomorphic to V. 
Indeed, if E\ and E2 are the standard 2-spheres of self-intersection —1 in CP2#CP2, 
then Ei + E2 and E\ — E2 are represented by disjoint embedded 2-spheres of self- 
intersection —2, and CP2#CP2 is obtained by gluing tubular neighborhoods of 
these two 2-spheres along their boundaries. We therefore have X sa 6CP2, and 
hence M » fcCP 2 , where k = 6 + 1. □ 

As a corollary, we now obtain one of the central results of this paper: 

Theorem 9.2. For any integer k > 6, the connected sum fcCP2 admits scalar- 
flat anti- self- dual metrics. 

Proof. Consider the smooth family of conformal classes [gt] constructed in 
Proposition l9.ll and let h t E [gt] be any smooth family of metrics representing these 
conformal classes. Let At denote the smallest eigenvalue of the Yamabe Laplacian 
(A + s/6) for the metric h t . Then At is a continuous function oft. But Proposition 
19. II tells us that A a > 0, whereas A& < 0. By continuity, there is thus some c € [a, 6] 
for which A c = 0. Let u be a unit-integral eigenfunction of the Yamabe Laplacian 
(A + s/6) of h c with eigenvalue A c = 0. By the minimum principle, u is a positive 
function. Thus g = u 2 h c is a scalar-flat anti-self-dual metric on /cCP2 for the given 
value of k > 6. □ 

Now this by no means represents the first construction ever of SFASD metrics on 
simply connected compact 4-manifolds. However, all the previous results depended 
on an essentially different idea: namely, that any Kahler metric on a complex 
surface with s = is SFASD. Through this observation, Yau's existence theorem 
for Ricci-flat Kahler metrics on K2> surfaces |6()| provided a crucial early family 
of examples which largely drove the subsequent development of the entire subject. 
Much later, the present author and his collaborators showed |40| that CP2#fcCP2 
admits scalar-flat anti-self-dual metrics if k > 14. The proof of this last result 
depends on a refinement of Theorem 14.41 set up so that the constructed twistor 
spaces carries a special divisor whose existence implies that the ASD conformal 
class contains a Kahler metric. For a related re-proof of the existence of Calabi- 
Yau metrics on K3, see |48| . 

Putting these previous results together with Corollarv l9.2l we have thus proved 
Theorem lAl 

Theorem 9.3. The following smooth A-manifolds admit scalar-fiat anti-self- 
dual metrics: 

(i) fcCP2, for every k > 6; 

(ii) CP 2 #fcCP 2 , for every k > 14; and 
(Hi) K3. 

In particular, each of these simply connected compact A-manifolds admits optimal 
metrics; and any optimal metric on any one of them is SFASD. 

10. Non-Existence Results 

We have now seen that many simply connected 4-manifolds admit non-Einstein 
optimal metrics. However, related ideas will now allow us to show there are also 
many simply connected 4-manifolds which do not admit optimal metrics. To see 
this, we begin by introducing a new concept: 

:S2 

CLAUDE LEBRUN 

Definition 10.1. Let M be a smooth compact oriented A- dimensional manifold 
(respectively, orbifold). We will say that M admits an anorexic sequence if there is 
a sequence gj of smooth Riemannian metrics ( respectively, orbifold metrics ) on M 
for which J s 2 d[i — ► and J \W + \ 2 dfi — > 0. 

When a manifold admits such a sequence, we then know the value of T-r(M), 
and stand a very good chance of determining whether it admits an optimal metric: 

Lemma 10.2. Let M be a smooth compact oriented A-manifold which admits 
an anorexic sequence. Then any optimal metric on M is SFASD. Moreover, 

Z TC (Af) = -8vr 2 ( X + 3T)(M). 

Proof. Recall that equation © tells us that 

K(g) = -8tt 2 ( X + 3r)(M) +2 J (t. + 2\W+\ 2 ^j d(i g . 

If there is an anorexic sequence, the infimum of the right-hand side is thus ob- 
tained by dropping the curvature integral. Moreover, a metric minimizing K would 
necessarily have s = and W+ = 0. □ 

Now imagine a curvaceous young 4-manifold who, bedazzled by the glamorous 
starlets with optimal metrics she has been reading about in the tabloids, suddenly 
decides to go on a starvation diet to get rid of all that unwanted curvature. If she 
has the wrong body type, this misguided procedure will be dangerous to her health, 
and she will merely succeed in putting herself in the hospital: 

Proposition 10.3. Let M be a smooth compact oriented A-manifold which 
admits an anorexic sequence. Then M does not admit an optimal metric if 

• b+(M) > A; or 

• b+{M) = 2; or 

• (M) = 3, 7i"i (.M) = 0, and M is not diffeomorphic to KZ; or 

• b + {M) = 1, m(M) = 0, and M is not diffeomorphic to CP 2 #fcCP 2 for 
some k > 10. 

Proof. By Lemma [10.21 an optimal metric on such an M would necessarily 
be SFASD. However, Propositions 13.41 and 13.51 show that we would then obtain a 
contradiction in any of the scenarios considered above. □ 

Now we come to our main method of construction 46 : 

Lemma 10.4. Let X be an oriented compact A-dimensional orbifold with only 
isolated singularities modeled on K 4 /Z2. Let X be the smooth oriented A-manifold 
obtained by replacing each singular point by a 2-sphere of self-intersection —2. If 
X admits an anorexic sequence, then so does X. Moreover, if there is an anorexic 
sequence on X with the property that J \r\ 2 d/j, — > 0, then X also admits an anorexic 
sequence with this property. 

Proof. If h is an orbifold metric on X with J s 2 d[i < e and J \ W + \ 2 d[i < e, 
we will show that X has a a metric g with f s 2 d[i < 2e and J \ W + \ 2 dfj, < 2e. 
Moreover, if h also has J \r\ 2 d^i < e, then we will be able to arrange for g to also 
satisfy / \r\ 2 dfi < 2e. 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

33 

To do this, we choose geodesic normal coordinates around a given orbifold 
point, so that we have 

h = 

+ a 

in these coordinates, where a is a (Z2-invariant) smooth symmetric tensor field on 
a neighborhood of the origin in R 4 with \a\ < C\x\ 2 . We would like to delete a ball 
of small radius p around the origin, and glue in a copy of the Eguchi- Hanson metric 
on T*S 2 , with very small length scale. Recall that the restriction of the Eguchi 
-Hanson metric to the complement of the zero section in T*S 2 is isometric to the 
metric 

dg 2 

9EH,t 

1 

(1)4, 

a\ + a 2 + 

on (e, oo) x S l3 /Z 2 , where {<jj} is the standard left-invariant co-frame on S 3 /Z 2 = 
SO(3); the constant e > is herein referred to as the length scale. Now, for any 
fixed p > 0, this family of metrics converges uniformly in the C 2 topology to the 
Euclidean metric on the annulus g G [p/2 7 p] as e — > 0. If ip : (0,oo) — > [0, 1] is a 
bump function which is = on (0, 1/2] and e 1 on [l,oo), then, for any fixed p, 
the metrics 

GO 

therefore converge in the C' 

= f 
norm to 

1 

(i) 

9eh,c 

9o, P = 

on the annulus g G [p/2, p], and in particular the curvature tensors of these metrics 
converge uniformly in the annulus to the curvature of go, P - On the other hand, 
since a is of magnitude 0(g 2 ), the first and second coordinate partial derivatives of 
go.p are uniformly bounded as p — > 0. Thus we can choose a sequence of (ej, pj) — > 
(0,0) such that the sectional curvatures of the metrics gj — g ej . Pj are uniformly 
bounded on the transition annuli g G [pj/2,pj], while the volumes of these annuli 
simultaneously tend to zero. For j far out in the sequence, the transition annulus 
therefore makes a contribution to J s 2 dp, J \r\ 2 dp, or J \W + \ 2 dp which is as small 
as we like — for example, smaller than the given e divided by the number of orbifold 
singularities of X . We now take g to be given by such a choice of gj in each glued 
region, h on the complement X minus a collection of balls or radius Pj about its 
orbifold singularities, and equal to the Eguchi-Hanson metric with length scale Cj 
near the added 2-spheres. Since the Eguchi-Hanson metric has r = and W+ = 0, 
the only possible source of increase of J s 2 dp, 1 J \r\ 2 dp, or J \W + \ 2 dp comes from 
the transition annuli, which already have under control, and so we have succeeded 
in producing a metric g on X with all the claimed properties. □ 

Here is a simple application of this Lemma: 

Lemma 10.5. The A-manifold 4CP 2 admits an anorexic sequence. 

PROOF. Consider the involution of S 3 x S 1 C H x C given by (q, z) i— > (q, z). 
Now equip S 3 x S 1 with the product of the unit-sphere metric on S 3 and the radius- 
e metric on S 1 . These metrics descend to orbifold metrics on (S 3 x S >1 )/Z 2 with 

34 

CLAUDE LEBRUN 

bounded sectional curvature, but with arbitrarily small volume; thus we obtain an 
anorexic sequence of such metrics by taking any sequence ej — ► 0. The 4-manifold 
X obtained from X by replacing its orbifold singularities with 2-sphcres of self- 
intersection —2 therefore also admits anorexic sequences by Lemma 110.41 But 
X = VffV, where V = 5 4 /Z 2 , and so X = V#V . However, as we already noted 
in the proof of Proposition EH V = 2CP 2 , and sol = 4CP 2 . □ 

We thus obtain our first non-existence result: 

Proposition 10.6. The 4-manifold 4CP 2 does not admit optimal metrics. 

Proof. By Lemmata ll0.2l and ll0.5l an optimal metric on 4CP 2 would have to 
be SFASD. However, (2x + 3r)(4CP 2 ) = 0, so PropositionEHwould imply that any 
SFASD metric on the simply connected 4-manifold 4CP 2 would be hyper-Kahler. 
But such a metric would entail the existence of non-trivial self-dual harmonic 2- 
forms, which is excluded here, since 6+(4CP 2 ) =0. □ 

A rather more important application of 110. 41 is the following: 

Lemma 10.7. The 4-manifold CP 2 ^9CP 2 admits an anorexic sequence. 

Proof. Consider the involution of S 2 x T 2 which is obtained as the product 
of a 180° rotation of S 2 around an axis and the Weierstrass involution of an elliptic 
curve: 

S 2 x T 2 

X X X X 

This involution has exactly 8 fixed points. Let X be the manifold which desingular- 
izes the orbifold X = [S 2 x T 2 ]/Z 2 by replacing each of the resulting eight singular 
points with an S 2 of self-intersection —2. 

Now it is easy to see that S 2 x T 2 admits sequences of metrics with bounded 
sectional curvature, but with volume tending to zero: namely, equip T 2 with a 
sequence of flat metrics of smaller and smaller area, and take the Riemannian 
product of these metrics with the standard round metric on S 2 . Moreover, the 
metrics given by this explicit recipe are all Z 2 -invariant, and so give rise to a 
sequence of orbifold metrics on [S 2 x T 2 ]/Z 2 with bounded sectional curvature for 
which the total volume tends to zero. Such a sequence is anorexic, and also has the 
special property that J \r\ 2 dfi — > 0. By Lemma fl 0.41 X therefore also admits such 
a special anorexic sequence. 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

35 

It only remains to show that X is diffcomorphic to CP2#9CP2- To se this, 
think of S 2 x T 2 as CPi x E, where E is an elliptic curve. Then X becomes a 
complex surface which has a branched double cover biholomorphic to CPi x E 
blown up at eight points. This complex surface is simply connected, and it has 
Kodaira dimension — oo because it contains a CPi with trivial normal bundle. By 
the Enriques-Kodaira classification [7], any such complex surface is rational, and 
hence must be diffeomorphic to either S 2 x S 2 or a connected sum CP2#fcCP2- 
However, 

to + 3 -)^) = i / + m + \ 2 - ^ ) d„ 

must vanish, since the right-hand side will certainly tend to zero for our special 
anorexic sequence. Since 

(2 x + 3t)(S 2 xS 2 ) = 8 
(2 X + 3r)(CP2#A:CP2) = 9 — k, 
it thus follows that X must be diffeomorphic to CP2#9CP2. □ 

In fact, one does not need to appeal to any classification machinery to check 
that X CP 2 #9CP 2 . Working with one's bare hands 06], it is not difficult to 
show that, with the fixed complex structure used above, X is precisely the complex 
surface obtained by iteratively blowing up CP2 at a configuration of points arranged 
as in the following diagram, in which a pair of adjacent points on a line means that 
one is to blow up the first point, and then blow up the resulting exceptional divisor 
at the point corresponding to the direction of the line, while the adjacent triple of 
points on a line has an analogous interpretation: 

If we think of the right-hand line as the line at infinity, the horizontal line as the 
cc-axis, and the three other lines as x = 0, x = 1 and x = t, then the elliptic curves 
y 2 = Ax(x — l)(x — t) foliate an open dense set of the blow-up, and arise from the 
E factor of [CPi x E]/Z 2 . 

Corollary 10.8. The simply connected 4-mani/o/d CP2^9CP2 does not admit 
optimal metrics. 

Proof. Lemma Tl U . 71 allows us to apply the last clause of Proposition ll0.3l □ 

To build more complicated examples, first consider the wormhole space obtained 
by equipping K 4 — {0} with the metric 

3(5 

CLAUDE LEBRUN 

Because 1 + e/|cc| 2 is a harmonic function, this conformally flat metric is scalar-flat. 
However, rewriting this metric in polar coordinates as 

where hg3 is the standard metric on the unit 3-sphere S 3 , we immediately see that 
there is an isometry e/g of the wormhole which interchanges the two ends of 
M 4 — {0}«Mx5 3 . Thus our wormhole connects two asymptotically Euclidean ends, 
but has s = and W+ = 0. Now, on any fixed annulus g e [p/2,p], the wormhole 
metric uniformly converges in C 2 to the Euclidean metric, and so exactly the same 
argument used to glue in Eguchi-Hanson metrics allows us to join two manifolds 
with J s 2 dp < e and J \W+\ 2 dp < e by a wormhole neck so as to obtain a new 
manifold with / s 2 dp < 3e and / \W + \ 2 dp < 3e. Thus: 

Lemma 10.9. Suppose that M\ and Mi art two smooth compact oriented 4- 
manifolds which admit anorexic sequences. Then their connected sum M\^Mi 
admits anorexic sequences, too. 

The final basic building block we will need is the Burns metric |44| . This is an 
asymptotically flat metric on CP2 — {p} with s = and W+ = 0. Rescaled versions 
of this metric, restricted to the complement of a CPi, are explicitly given by 

as a metric on (e, 00) x S 3 . As the length-scale parameter e tends to zero, we once 
again get uniform C 2 convergence to the Euclidean metric on any fixed annulus 
g£ [p/2,p], and the same gluing argument as before therefore gives us the following 
result: 

Lemma 10.10. Suppose that M is a smooth compact oriented 4-manifold which 
admits an anorexic sequence. Then M#CW2 admits anorexic sequences, too. 

We now prove the first part of Theorem IU1 

Theorem 10.11. Let j and k be integers such that j > 2 and k > 9j. Then 
the simply connected A-manifold jCPg^&CPa does not admit optimal metrics. 

Proof. By induction on j, Lemmata II U . 71 and 110.91 imply that the connected 
sum jCP2#9jCP2 of j copies of CP2#9CP2 admits an anorexic sequence. Lemma 
110.101 and induction on k — 9j then gives us the existence of an anorexic sequence 
on jCP2#fcCP2 for any k > 9j, j > 2. Proposition llO. 31 therefore tells us that there 
is no optimal metric on any of these non-spin simply connected 4-manifolds with 

Now let us next consider some 'exotic' smooth structures on CP2#9CP2- Let 
X denote the complex orbifold [CPi x E]/1,2 used in the proof of Lemma Tl 0.71 and 
let us observe that we have a holomorphic orbifold submersion X — > CPi /Z2 given 
by projection to the first factor. Near any non-singular point of CP1/Z2, this is a 
locally trivial holomorphic i?-bundle. Let p and q be two relatively prime integers 
> 2, and choose two nonsingular points a,b G CP1/Z2. Note that CP1/Z2 is really 
just a copy of CPi with two marked points which are considered to be orbifold 
points of oder 2. Let us now also mark the points a and b, and consider them 

b+ =j>2. 

□ 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

37 

to be orbifold points of order p and q. At the same time, we modify V to obtain 
a new orbifold V p ° q by replacing the fiber over a with EfLp and the fiber over b 
with E/Z q , where the two actions are generated by translation of E of order p 
and order q, respectively. This can be done via a logarithmic transformation in the 
sense of Kodaira; for example, in a neighborhood of a biholomorphic to the open 
unit disk D C C, we E x D with [E x D]/Z p , where Z p acts on E as before, and 
simultaneously acts on D via the action generated by z n e 2 ™/ p z. We then have a 
holomorphic orbifold submersion from V p ° q to our orbifold CPi with four orbifold 
points. Now choose the compatible flat metric on E with unit area and use a 
partition of unity to patch the a product metric on V with local product metrics on 
[E x D]/Z p and [E x D]/Z q . The result is a Riemannian submersion orbifold metric 
on V. If we now scale down the fiber E with keeping the metric on our orbifold CPi 
fixed, the result is therefore a family of metrics on V p q with volume tending to zero 
while the curvature remains uniformly bounded |14L I46| . In particular, this is an 
anorexic sequence on V pq , and Lemma fl . 41 tells us that the complex surface M pq 
obtain by replacing each of the 8 orbifold singularities of V pq by (— 2)-curves also 
admits anorexic sequences; moreover, the manifolds ? #£CP2 all admit anorexic 
sequences, too, as a consequence of Lemma H(J. 101 However, the manifolds M Pi9 are 
the so-called Dolgachev surfaces. These Dolgachev surfaces are all homeomorphic 
to CP2#9CP2, but Donaldson or Seiberg-Witten invariants can be used [22 to 
show that no two of them are diffeomorphic. Moreover, the corresponding smooth 
structures on the blow-ups remain distinct, no matter how many times we blow 
up, and these smooth structures are moreover all distinct from the standard one on 
CP2#fcCP2- By Proposition 110. 3| it follows that none of these smooth manifolds 
admits an optimal metric, even though CP2#fcCP2 does admit optimal metrics for 
k > 14. 

The story is similar for homotopy if 3 surfaces. Namely, we can view T 4 j%i as 
an orbifold elliptic fibration over CP1/Z2, and so modify it by logarithmic trans- 
forms of odd order at one fiber. The resulting orbifolds V q then admit anorexic 
sequences as before, as do the 4-manifolds M q obtained by replacing their singular 
points by 2-spheres of self-intersection —2. These manifolds are homeomorphic to 
K3 surfaces, but as smooth manifolds they are distinct, not only from K3, but also 
from each other. Proposition 1 1 . 3| thus tells us that none of them admits optimal 
metrics, even though they are homeomorphic to K3, which does admit optimal 
metrics. We have thus proved Theorem IB1 

Theorem 10.12. The existence or non-existence of optimal metrics depends on 
the choice of smooth structure. In particular, the topological A-manifolds K3 and 
CP2#fcCP2, k > 14. admit infinitely many exotic smooth structures for which no 
optimal metric exists, even though each also admits a "standard" smooth structure 
for which optimal metrics do exist. 

A similar construction 146) yields anorexic sequences on many exotic manifolds 
homeomorphic to jCP2#fcCP2- Consider the complex orbifold [S x E\j'Li, where 
£ is a hyperelliptic Rlemann surface of genus g: 

CLAUDE LEBRUN 

I 

I 

Giving E its compatible flat metric of various areas, products with a fixed metric 
on £ give us anorexic sequences on the orbifold V s = [E x E\j7L 2l an d we also 
get anorexic sequences on the orbifold obtained by performing a logarithmic 
transform to one fiber by the previous gluing argument. If denotes the complex 
surface obtained by replacing the singularities of by (— 2)-curves, then Lemma 
lit). 41 guarantees that M| also admits anorexic sequences, and Lemma f 1 . 1 01 1 hen 
tells us that M^^f£CP 2 admits anorexic sequences, too. Now M*= is a simply 
connected complex surface with p g = g and c\ = 0; and it is non-spin if either g or 
q is even. For any £ > 0, Theorem 12 .31 tells us that Mf=#£CP 2 is homeomorphic to 
(2g + l)CP 2 #(10g + 9 + £)CP 2 ; and we also get the analogous statement for £ = 
if q is even. However, by varying q, gauge theory can be used to show IT7| 
that we obtain infinitely many distinct smooth structures in this way for any fixed 
g and £ . By Proposition llL).3l we therefore have the following result: 

Theorem 10.13. For any odd j > 1 and any k > 5j ' + 4, the topological mani- 
fold j'CP2#fcCP2 admits infinitely distinct smooth structures for which no optimal 
metric exists. 

Lemma 110.91 now allows us to produce more examples of smooth 4-manifolds 
with anorexic sequences by taking connected sums of our previous examples. De- 
termining whether we obtain distinct differentiable structures in this way is a 
cutting-edge problem in gauge-theory, however, and it is only by applying the so- 
phisticated new machinery of Bauer and Furuta O |5] that a result of this type 
can be obtained. Specifically, if g is odd, then the bandwidth argument of 35 
shows that the M S #M ? 1 #£CF 2 run through infinitely many differentiable struc- 
tures on (2g + 4)CP 2 #(10g + 28 + £)CP 2 as we vary the even integer q > 2, and 
that 2M s #2Mq#£CP2 runs through infinitely many differentiable structures on 
(4g + 8)CP 2 #(20g + 56 + £)CP 2 . Since Proposition ITTP1 tells us that none of these 
spaces can admit optimal metrics, we thus obtain the second part of of Theorem 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

3!) 

Theorem 10.14. If j and k are integers, with j > 5, j ^ mod 8, and k > 9j, 
then the topological manifold jCP2#fcCP2 admits infinitely distinct smooth struc- 
tures for which no optimal metric exists. 

11. Concluding Remarks 

While we have seen that many topological 4-manifolds fail to admit optimal 
metrics for many choices of smooth structure, the techniques developed here do not 
by any means allow us to determine whether or not an optimal metric exists for 
an arbitrary smooth structure. The reason is that the arguments deployed in i jlUI 
are heavily dependent on the existence of anorexic sequences of metrics, whereas 
such sequence simply do not exist for many smooth structures. For example, if X 
is a minimal complex surface of general type, and if M = X#£CF2 is the complex 
surface obtained from it by blowing up £ points, then Seiberg-Witten theory can 
be used to show |47| that any metric on M satisfies 

(is) £(|i +w ) rfM >!|V), 

so there are certainly no anorexic metrics on such an M. If X is is simply connected 
and I is sufficiently large, however, this 4-manifold is homeomorphic to one of the 
manifolds treated by Theorem El and so represents an exotic smooth structure on 
this topological 4-manifold which is simply not amenable to treatment with the 
current technology. 

The main obstacle to progress on this front is that the estimate (II 3[) does not 
appear to be sharp; if we compare it with known minimizing sequences for J s 2 <i/i 
on a complex surface M of general type with minimal model X, we only obtain 
upper and lower bounds 

1 A 2 

-^-cl(X) - 8tt 2 ( X + 3r)(M) < X n (M) < 8^ 2 c 2 (X) - 8tt 2 ( X + 3r)(M) 

for Tn(M). These bounds certainly do not allow one to compute Tn, but they 
do allow us to estimate with sufficient accuracy to be able to know that at least 
several different values of 2-r must occur for many fixed homeotypes. An exact 
computation of T-jz for such examples would have many interesting ramifications, 
and should be considered as an outstanding open problem in the subject. 

While current technology does not suffice to compute In for many of the most 
interesting 4-manifolds, the analogous invariants 

1 S (M) = inf / \s g \ n,2 d^ g 
Xr(M) = inf f \r\ n g /2 dfi g 

9 JM 

arising from the scalar and Ricci curvatures do turn out to be exactly computable 
for complex surfaces of general type and many of their connect sums |47l 136) . It 
may therefore come as a surprise that one key trick used in computations of X r is 
closely related to the techniques developed here. Indeed, the Gauss-Bonnet and 
signature formulae tell one that 

J \r\ 2 d^ = -8n 2 (2 X + 3r)(M) + 8 J + \\W + \ 2 ^ dy. 

40 

CLAUDE LEBRUN 

so that the existence of an anorexic sequence is certainly quite sufficient to allow 
one to calculate X r . However, the curious difference is that the available Seiberg- 
Witten estimate analogous to (|f 3fl for this particular combination of s and W+ 
turns out to typically be sharp. For example, if M = X#£CP2 is a complex surface 
of general type with minimal model X, one obtains the estimate 

and one can actually find sequences of metrics for which the left-hand side ap- 
proaches the expression on the right; thus, an exact formula 

emerges from the discussion. Moreover, related argments show that this infimum 
is unattained whenever I > 0. For details and further applications, see |47l 136) . 

While Theorem ^] may shed a fair amount of light on the existence of SFASD 
metrics on compact 4-manifolds, it by no means closes the book on the subject. For 
example, we still do not know whether such metrics exist on 5CP2 . The existence of 
SFASD metrics on CP 2 #fcCP 2 for 10 < k < 13 is also not covered by TheoremE] 
although Yann Rollin and Michael Singer seem to have recently made considerable 
progress concerning these manifolds. The global structure of the moduli space of 
SFASD metrics still remains a mystery. And it would obviously be of the greatest 
interest to sharpen Proposition 13.51 so as to say something about diffeotype when 
b + = 0, or to definitively handle the non-simply connected case. 

We now have many examples of optimal metrics on compact 4-manifolds, essen- 
tially falling into two classes: the Einstein metrics, and the scalar-flat anti-self-dual 
metrics. Of course, we can cheaply obtain further examples by reversing the orien- 
tation of SFASD manifolds to make them self-dual instead of anti-self-dual. But, 
such trickery aside, there do not really seem to be any other known examples of 
optimal metrics on compact 4-manifolds. In particular, it seems that all known 
examples of optimal metrics are critical points of J s 2 d/j,, and so, by optimality, 
also of J \ W+\ 2 dfi. Now a metric on a 4-manifold is a critical point of J |W+| 2 d/x 
iff it has vanishing Bach tensor [IT]. Are there any optimal metrics on compact 
4-manifolds that aren't Bach-flat? Are there scalar-flat optimal metrics which are 
Bach-flat, but neither self-dual nor anti-self-dual? Both of these questions should 
illustrate the degree to which we still remain fundamentally ignorant as to the true 
nature of general optimal metrics, even in dimension four. 

Acknowledgments. I would like to express my profound gratitude to Dominic 
Joyce, who originally convinced me, by an entirely different line of reasoning, that 
Theorems 16.31 and 16.41 ought to be true. I would also like to warmly thank Mike 
Eastwood and Michael Singer for granting me permission to present some of their 
unpublished results in fJHl Finally, I would like to thank Chris Bishop, Mark de 
Cataldo, Sorin Popescu, and Michael Taylor for helpful suggestions concerning a 
number of important technical details. 

[1] C. Allendoerfer and A. Weil, The Gauss-Bonnet theorem for Riemannian polyhedra, 

Trans. Am. Math. Soc, 53 (1943), pp. 101-129. 
[2] A. Altman and S. Kleiman, Introduction to Grothendieck Duality Theory, Lecture Notes 

in Mathematics, Vol. 146, Springer- Verlag, Berlin, 1970. 

X r (M) = 8tt 2 [c?(A) +1] 

References 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

41 

[3] M. F. Atiyah, Green's functions for self-dual four- manifolds, in Mathematical Analysis and 
Applications, Part A, vol. 7 of Adv. in Math. Suppl. Stud., Academic Press, New York, 1981, 
pp. 129-158. 

[4] M. F. Atiyah, N. J. Hitchin, and I. M. Singer, Self-duality in four-dimensional Riemann- 

ian geometry, Proc. Roy. Soc. London Ser. A, 362 (1978), pp. 425-461. 
[5] T. N. Bailey and M. A. Singer, Twistors, massless fields and the Penrose transform, in 

Twistors in mathematics and physics, vol. 156 of London Math. Soc. Lecture Note Ser., 

Cambridge Univ. Press, Cambridge, 1990, pp. 299-338. 
[6] C. Banica and O. Stana§ila, Algebraic Methods in the Global Theory of Complex Spaces, 

Editura Academici, Bucharest, 1976. 
[7] W. Barth, C. Peters, and A. V. de Ven, Compact Complex Surfaces, Springer- Verlag, 

1984. 

[8] S. Bauer, A stable cohomotopy refinement of Seiberg-Witten invariants. II, Invent. Math., 
155 (2004), pp. 21-40. 

[9] S. Bauer and M. Furuta, A stable cohomotopy refinement of Seiberg-Witten invariants. I, 
Invent. Math., 155 (2004), pp. 1-19. 
[10] M. Berger, Riemannian Geometry During the Second Half of the Twentieth Century, Amer- 
ican Mathematical Society, Providence, RI, 2000. Reprint of the 1998 original. 
[11] A. Besse, Einstein Manifolds, Springer- Verlag, 1987. 

[12] C. J. Bishop and P. W. Jones, Hausdorff dimension and Kleinian groups, Acta Math., 179 
(1997), pp. 1-39. 

[13] J. -P. BOURGUIGNON, Les varietes de dimension 4 d signature non nulle dont la courbure est 
harmonique sont d'Einstein, Invent. Math., 63 (1981), pp. 263-286. 

[14] J. Cheeger and M. Gromov, Collapsing Riemannian manifolds while keeping their curva- 
ture bounded. I, J. Differential Geom., 23 (1986), pp. 309-346. 

[15] S. Donaldson and R. Friedman, Connected sums of self- dual manifolds and deformations 
of singular spaces, Nonlincarity, 2 (1989), pp. 197-239. 

[16] S. K. DONALDSON, An application of gauge theory to four- dimensional topology, J. Differential 
Geom., 18 (1983), pp. 279-315. 

[17] M. G. Eastwood and J. W. Rice, Conformally invariant differential operators on 
Minkowski space and their curved analogues, Comm. Math. Phys., 109 (1987), pp. 207—228. 

[18] M. G. Eastwood and M. A. Singer, On the geometry of twistor spaces, unpublished man- 
uscript, 1991. 

[19] T. EGUCHI and A. J. HANSON, Self-dual solutions to Euclidean gravity, Ann. Physics, 120 
(1979), pp. 82-106. 

[20] M. Freedman, On the topology of 4-manifolds, J. Differential Geom., 17 (1982), pp. 357-454. 
[21] R. Friedman, Global smoothings of varieties with normal crossings, Ann. of Math. (2), 118 
(1983), pp. 75-114. 

[22] , Vector bundles and SO (3) -invariants for elliptic surfaces, J. Amer. Math. Soc, 8 

(1995), pp. 29-139. 

[23] R. Friedman and J. W. Morgan, On the diffeomorphism types of certain algebraic surfaces. 

I, J. Differential Geom., 27 (1988), pp. 297-369. 
[24] J. Gasqui and H. Goldschmidt, Theoremes de dualite en geometrie conforme, C. R. Acad. 

Sci. Paris Ser. I Math., 294 (1982), pp. 99-102. 
[25] , Deformations Infinitesimales des Structures Conforraes Plates, vol. 52 of Progress in 

Mathematics, Birkhauser Boston Inc., Boston, MA, 1984. 
[26] D. Gilbarg and N. S. Trudinger, Elliptic Partial Differential Equations of Second Order, 

Springer- Verlag, Berlin, second cd., 1983. 
[27] R. E. Gompf and A. I. Stipsicz, A-Manifolds and Kirby Calculus, American Mathematical 

Society, Providence, RI, 1999. 
[28] P. Griffiths and J. Harris, Principles of Algebraic Geometry, Wiley-Interscience [John 

Wiley & Sons], New York, 1978. Pure and Applied Mathematics. 
[29] M. Gromov, Structures metriques pour les varietes riemanniennes, CEDIC, Paris, 1981. 

Edited by J. Lafontainc and P. Pansu. 
[30] R. C. Gunning and H. Rossi, Analytic Functions of Several Complex Variables, Prentice- 
Hall Inc., Englcwood Cliffs, N.J., 1965. 
[31] F. HlRZEBRUCH, Topological Methods in Algebraic Geometry, Springer- Verlag, 1966. 

42 

CLAUDE LEBRUN 

[32] N. J. Hitchin, On compact four- dimensional Einstein manifolds, J. Differential Geom., 9 
(1974), pp. 435-442. 

[33] , Kdhlerian twistor spaces, Proc. London Math. Soc. (3), 43 (1981), pp. 133-150. 

[34] G. HORROCKS, A construction for locally free sheaves, Topology, 7 (1968), pp. 117-120. 
[35] M. Ishida AND C. LeBrun, Spin manifolds, Einstein metrics, and differential topology, Math. 

Res. Lett., 9 (2002), pp. 229-240. 
[36] , Curvature, connected sums, and Seiberg-Witten theory, Comm. Anal. Geom., 11 

(2003), pp. 809-836. 

[37] D. Joyce, Constant scalar curvature metrics on connected sums, Int. J. Math. Math. Sci., 
(2003), pp. 405-450. 

[38] T. Kato, Perturbation theory for linear operators, Springer- Verlag New York, Inc., New 
York, 1966. 

[39] J. Kim, On the scalar curvature of self- dual manifolds, Math. Ann., 297 (1993), pp. 235—251. 
[40] J. Kim, C. LeBrun, and M. Pontecorvo, Scalar-flat Kahler surfaces of all genera, J. Reine 

Angew. Math., 486 (1997), pp. 69-95. 
[41] N. H. Kuiper, On conformally-fiat spaces in the large, Ann. of Math. (2), 50 (1949), pp. 916- 

924. 

[42] J. Lafontaine, Remarques sur les varietes conformement plates, Math. Ann., 259 (1982), 
pp. 313-319. 

[43] C. LeBrun, On the topology of self-dual A-manifolds, Proc. Amcr. Math. Soc, 98 (1986), 
pp. 637-640. 

[44] , Counter-examples to the generalized positive action conjecture, Comm. Math. Phys., 

118 (1988), pp. 591-596. 

[45] , Anti-self-dual metrics and Kahler geometry, in Proceedings of the International Con- 
gress of Mathematicians, Vol. 1, 2 (Zurich, 1994), Basel, 1995, Birkhauser, pp. 498-507. 

[46] , Kodaira dimension and the Yamabe problem, Comm. Anal. Geom., 7 (1999), pp. 133- 

156. 

[47] , Ricci curvature, minimal volumes, and Seiberg-Witten theory, Inv. Math., 145 (2001), 

pp. 279-316. 

[48] C. LeBrun and M. Singer, A Kummer-type construction of self-dual A-manifolds, Math. 

Ann., 300 (1994), pp. 165-180. 
[49] J. Lee and T. Parker, The Yamabe problem, Bull. Am. Math. Soc., 17 (1987), pp. 37-91. 
[50] B. Maskit, Kleinian Groups, Springer- Verlag, Berlin, 1988. 

[51] S. Nayatani, Patterson-Sullivan measure and conformally flat metrics, Math. Z., 225 (1997), 
pp. 115-131. 

[52] A. Newlander and L. Nirenberg, Complex analytic coordinates in almost complex mani- 
folds, Ann. of Math. (2), 65 (1957), pp. 391-404. 

[53] R. Penrose, Nonlinear gravitons and curved twistor theory, General Relativity and Gravi- 
tation, 7 (1976), pp. 31-52. 

[54] M. H. Protter and H. F. Weinberger, Maximum principles in differential equations, 
Prentice-Hall Inc., Englewood Cliffs, N.J., 1967. 

[55] R. SCHOEN AND S.-T. Yau, Conformally flat manifolds, Kleinian groups and scalar curvature, 
Invent. Math., 92 (1988), pp. 47-71. 

[56] J. -P. Serre, Modules projectifs et espaces fibres d fibre vectorielle, in Seminaire P. Dubreil, 
M.-L. Dubreil-Jacotin et C. Pisot, 1957/58, Fasc. 2, Expose 23, Secretariat mathematique, 
Paris, 1958, p. 18. 

[57] J. A. Thorpe, Some remarks on the Gauss-Bonnet formula, J. Math. Mech., 18 (1969), 
pp. 779-786. 

[58] R. O. Wells, Jr., Differential Analysis on Complex Manifolds, Springer- Verlag, New York, 
second ed., 1980. 

[59] S. T. Yau, On the curvature of compact Hermitian manifolds, Invent. Math., 25 (1974), 
pp. 213-239. 

[60] , On the Ricci curvature of a compact Kahler manifold and the complex Monge- Ampere 

equation. I, Comm. Pure Appl. Math., 31 (1978), pp. 339-411. 
[61] , Open problems in geometry, in Differential Geometry: Partial Differential Equations 

on Manifolds (Los Angeles, CA, 1990), vol. 54 of Proc. Sympos. Pure Math., Amer. Math. 

Soc, Providence, RI, 1993, pp. 1-28. 

CURVATURE, OPTIMAL METRICS, AND 4-MANIFOLDS 

43 

Department of Mathematics, SUNY at Stony Brook, Stony Brook, NY 11794-3651 
E-mail address: claude@amath.sunysb.edu