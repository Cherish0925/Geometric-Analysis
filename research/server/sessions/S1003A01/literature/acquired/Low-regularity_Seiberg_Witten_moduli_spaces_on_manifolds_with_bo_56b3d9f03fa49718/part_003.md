---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Low-regularity Seiberg–Witten moduli spaces on manifolds with boundary]

Assume \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} is not surjective. Proposition [4.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar63) implies its image is closed, so there is 0 \\ne {{\\tilde{v}}} \\in {\\mathcal {V}}(X,\\hat{{\\mathfrak {s}}}) \\oplus L^2(i \\Omega ^0(X)) orthogonal to {{\\,\\textrm{im}\\,}}\\widetilde{D {{\\,\\textrm{SW}\\,}}}. Recall that {{\\tilde{K}}} is a certain multiplication by  p = (A - A\_0, \\Phi ) \\in L\_1^2( i \\Omega ^1(X) \\oplus \\Gamma (S^+\_X)) . Let X^\*= X \\cup ( \[0,\\infty ) \\times Y ) with cylindrical metric on the end, and extend the spinor bundle S\_X to S\_{X^\*} which is cylindrical on ends. Extend _p_ to p^\*\\in L^2\_1( i \\Omega ^1(X^\*) \\oplus \\Gamma (S^+\_{X^\*})) in an arbitrary way and {{\\tilde{v}}} to {{\\tilde{v}}}^\*\\in {\\mathcal {V}}(X^\*,\\hat{{\\mathfrak {s}}}) \\oplus L^2(i \\Omega ^0(X^\*)) by zero on  \[0,\\infty ) \\times Y. We have\
\
\\begin{aligned} \\langle {{\\tilde{v}}}^\*, ({{\\tilde{D}}} + {{\\tilde{K}}}) (w) \\rangle \_{L^2(X^\*)} = \\langle {{\\tilde{v}}}, \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}(w\|\_X) \\rangle \_{L^2(X)} = 0 \\end{aligned}\
\
for any w \\in \\mathcal{T}\\mathcal{C}(X^\*, \\hat{{\\mathfrak {s}}}). Therefore {{\\tilde{v}}}^\* is a weak solution to  {{\\tilde{D}}}^\*{{\\tilde{v}}}^\*+ {{\\tilde{K}}}^\*{{\\tilde{v}}}^\*= 0 where {{\\tilde{D}}}^\*, {{\\tilde{K}}}^\* are formal adjoints of {{\\tilde{D}}}, {{\\tilde{K}}}, respectively. The map {{\\tilde{K}}}^\*:L^2\_1\\rightarrow L^2 is compact by Theorem [A.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar92). Thus from the Regularity Theorem it follows that {{\\tilde{v}}}^\*\\in L^2\_1(i \\Omega ^+(X^\*) \\oplus \\Gamma (S^-\_{X^\*}) \\oplus i \\Omega ^0(X^\*))  and it is a solution to  ({{\\tilde{D}}}^\*+ {{\\tilde{K}}}^\*) {{\\tilde{v}}}^\*= 0 . Furthermore, Corollary [2.5](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar12) implies that {{\\tilde{v}}}^\*= 0 and therefore v = 0. Thus, by contradiction, we have proved that D {{\\,\\textrm{SW}\\,}} is surjective. \\square\
\
Finally, we focus on the density of the restriction map from the kernel of \\widetilde{D{{\\,\\textrm{SW}\\,}}} to one boundary component. The proof of this proposition utilizes some of the ideas we have just seen (cf. \[ [21](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR21 "Lipyanskiy, M.: A semi-infinite cycle construction of Floer homology (2008). Thesis (Ph.D.)—Massachusetts Institute of Technology"), Lemma 5\]).\
\
### Proposition 4.4\
\
(Density of moduli on one boundary component) Assume the boundary _Y_ has at least two connected components and let Y\_0 \\subset Y be any one of these components. Then the restriction\
\
\\begin{aligned} R: \\ker \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} \\rightarrow L^2\_{1/2}\\bigl ({i\\Omega ^1\_{}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ) \\end{aligned}\
\
is dense.\
\
### Proof\
\
Assume, by contradiction, that it is not dense and choose a nonzero element v \\in L^2\_{1/2}\\bigl ({i\\Omega ^1\_{}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ) which is L^2\_{1/2}-perpendicular to its image. Since \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} is surjective by Proposition [4.3](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar65), the map\
\
![](https://media.springernature.com/lw326/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ132_HTML.png)\
\
has finite-dimensional cokernel, where \\Pi \_v is the L^2\_{1/2}-projection onto v \\in L^2\_{1/2}\\bigl ({i\\Omega ^1\_{}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ).\
\
From the definition of _v_ it follows that  \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} \\oplus \\Pi \_v R  is not surjective, since otherwise there would be an element ![](https://media.springernature.com/lw182/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq726_HTML.gif) which solves \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}(w) = 0 such that \\Pi \_v(R(w)) \\ne 0. Therefore, we can pick an element ( _a_, _v_) which is orthogonal to the image of  \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} \\oplus \\Pi \_v R , where ![](https://media.springernature.com/lw274/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq730_HTML.gif).\
\
As in the proof of Proposition [4.3](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar65), attach a cylindrical end along _Y_ to get X^\*= X \\cup \[0,\\infty ) \\times Y . Extend _a_ to a^\* by 0 on  \[0,\\infty ) \\times Y . Since {{\\tilde{K}}} is a certain multiplication by  p = (A - A\_0,\\Phi ) \\in L^2\_1( i \\Omega ^1(X) \\oplus \\Gamma (S^+\_X) ), extend _p_ to p^\*\\in L^2\_1(i \\Omega ^1(X^\*) \\oplus \\Gamma (S^+\_{X^\*})) in an arbitrary way to get {{\\tilde{K}}} defined on X^\*. By Theorem [A.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar92), \\widetilde{K} is a compact operator L^2\_1 \\rightarrow L^2.\
\
Since (a,v) \\perp {{\\,\\textrm{im}\\,}}\\left(\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} \\oplus {\\Pi }\_v R \\right), we get that a^\* is a weak solution to ({{\\tilde{D}}}^\*+ {{\\tilde{K}}}^\*) a^\*= 0 on the interior of X^\*\_1 = X^\*\\setminus (\[0,\\infty ) \\times Y\_0). Take any compact set C \\subset X^\*\_1 and a smooth bump function \\eta : X^\*\\rightarrow \[0,1\] such that \\eta \|\_C = 1 and {{\\,\\textrm{supp}\\,}}\\eta \\subset X^\*\_1. It follows that  (D^\*+K^\*)(\\eta a) = \\rho ^\*(d \\eta ) a \\in L^2(X^\*) . Therefore by the Regularity Theorem we get that \\eta a \\in L^2\_1(X^\*), and in particular a \\in L^2\_1(\\mathring{C}). Varying _C_ we obtain a^\*\\in L^2\_{1,loc}(X^\*\_1). Since a^\*\\equiv 0 on \[0,\\infty ) \\times (Y {\\setminus } Y\_0) \\subset X\_1^\*, Corollary [2.5](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar12) implies that a^\*= 0 on X^\*\_1, so a=0 on _X_.\
\
This is a contradiction since we can extend v \\in L^2\_{1/2}\\bigl ({i\\Omega ^1\_{}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ) to ![](https://media.springernature.com/lw178/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq759_HTML.gif) such that R({{\\tilde{v}}}) = v. Then\
\
\\begin{aligned} 0&= \\langle (\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}({{\\tilde{v}}}), \\Pi \_v R {{\\tilde{v}}}), (a, v) \\rangle \_{L^2\_{1/2}}\\\&= \\langle (\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}({{\\tilde{v}}}), v), (0, v) \\rangle \_{L^2\_{1/2}}\\\&= 0 + \\langle v,v\\rangle \_{L^2\_{1/2}} \\end{aligned}\
\
implying  \\Vert v\\Vert \_{L^2\_{1/2}} = 0, which contradicts the assumption that v \\ne 0. \\square\
\
### 4.2 Regularity and semi-infinite-dimensionality of moduli spaces\
\
We turn our focus to the operator D{{\\,\\textrm{SW}\\,}}. The main difficulty in transferring the results of Sect. [4.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#Sec15) from \\widetilde{D{{\\,\\textrm{SW}\\,}}} to D{{\\,\\textrm{SW}\\,}} is the presence of the Coulomb condition on both _X_ and \\partial X. The split gauge condition introduces an additional twist to the story.\
\
A key fact is that the differential of the gauge group action at _e_ (cf. Lemma [3.6](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar19)) preserves the kernel of D{{\\,\\textrm{SW}\\,}} at a solution  (A,\\Phi ) .\
\
### Lemma 4.5\
\
Assume ![](https://media.springernature.com/lw68/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq770_HTML.gif). Then for any f \\in L^2\_2(i \\Omega ^0(X)) we have  D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )}(df,-f \\Phi ) = 0.\
\
### Proof\
\
We compute:\
\
![](https://media.springernature.com/lw504/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ133_HTML.png)\
\
which finishes the proof. \\square\
\
Following the idea of \[ [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR12 "Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. 19(3), 1631–1655 (2015)"), Proposition 3.1\], we deduce the semi-infinite-dimensionality and compute the index of D{{\\,\\textrm{SW}\\,}} from Proposition [4.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar63). These methods will be utilized to prove further results in this section, too.\
\
### Proposition 4.6\
\
(Semi-infinite-dimensionality of D{{\\,\\textrm{SW}\\,}}) The operator\
\
![](https://media.springernature.com/lw290/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ11_HTML.png)\
\
(13)\
\
\
is Fredholm of index\
\
![](https://media.springernature.com/lw265/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ12_HTML.png)\
\
(14)\
\
\
where ![](https://media.springernature.com/lw64/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq776_HTML.gif) is the index of ![](https://media.springernature.com/lw28/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq777_HTML.gif) with the APS spectral boundary conditions. Moreover, the restriction  {\\Pi }^+ R: \\ker \\left(D\_{(A,\\Phi )}{{\\,\\textrm{SW}\\,}}\\right) \\rightarrow H^+(Y,{\\mathfrak {s}})  is compact, where ![](https://media.springernature.com/lw285/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq779_HTML.gif).\
\
### Proof\
\
Firstly, we compare the respective polarizations. Recall that the decomposition of L^2\_{1/2}\\bigl ({i\\Omega ^1\_{}\\bigl ({Y}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y}\\bigr )}\\bigr ) into \\widetilde{H}^+(Y,{\\mathfrak {s}}) \\oplus \\widetilde{H}^-(Y,{\\mathfrak {s}}) is given by the eigenspaces of \\widetilde{L}. Decomposing\
\
\\begin{aligned} i \\Omega ^1(Y) \\oplus \\Gamma (S\_Y) \\oplus i \\Omega ^0(Y) = \\left(i \\Omega ^1\_{cC}(Y) \\oplus \\Gamma (S\_Y)\\right) \\oplus \\left(\\Omega ^1\_C(Y) \\oplus i \\Omega ^0(Y)\\right) \\end{aligned}\
\
we see that \\widetilde{L} decomposes as ![](https://media.springernature.com/lw172/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq784_HTML.gif). Denote by {\\Pi }^\\pm \_1 the spectral projections of \\begin{pmatrix} 0 &{} -d \\\ -d^\*&{} 0 \\end{pmatrix} in L^2\_{1/2}(i \\Omega ^1\_C(Y) \\oplus i \\Omega ^0(Y)). It follows that  {\\widetilde{{\\Pi }}}^\\pm = {\\Pi }^\\pm \\oplus {\\Pi }^\\pm \_1.\
\
This is enough to prove the statement about compactness. Indeed, the map {\\Pi }^+R: \\ker \\left( D\_{(A,\\Phi )}{{\\,\\textrm{SW}\\,}}\\right) \\rightarrow H^+(Y,{\\mathfrak {s}}) is just the composition\
\
\\begin{aligned} \\ker \\left( D\_{(A,\\Phi )}{{\\,\\textrm{SW}\\,}}\\right) \\hookrightarrow \\ker \\left( \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} \\right) \\xrightarrow {{\\widetilde{{\\Pi }}}^+R} \\widetilde{H}^+(Y,{\\mathfrak {s}}) \\xrightarrow {{\\Pi }^+} H^+(Y,{\\mathfrak {s}}) \\end{aligned}\
\
where the map in the middle is compact by Proposition [4.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar63).\
\
For Fredholmness, denote by\
\
\\begin{aligned} \\Pi \_C: L^2\_{1/2}(\\Omega ^1\_C(Y) \\oplus \\Omega ^0(Y)) \\rightarrow L^2\_{1/2}(\\Omega ^1\_C(Y) \\oplus \\Omega ^0(Y)) \\end{aligned}\
\
the projection onto L^2\_{1/2}(\\Omega ^1\_C(Y)) \\oplus {\\mathbb {R}}^{\\pi \_0(Y)} (where {\\mathbb {R}}^{\\pi \_0(Y)} \\subset \\Omega ^0(Y) is the space of locally constant functions) along \\{0\\} \\oplus L^2\_{1/2}(\\Omega ^0\_0(Y)) (where  \\Omega ^0\_0(Y) = \\{ f \\in \\Omega ^0(Y) \| \\forall \_i \\int \_{Y\_i} f = 0 \\}). This projection can be used to define the split Coulomb slice for the orthogonal splitting s\_\\perp  (Definition [3.22](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar44)). Precisely, we have\
\
![](https://media.springernature.com/lw273/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ134_HTML.png)\
\
Khandhawit \[ [12](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR12 "Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. 19(3), 1631–1655 (2015)"), Proposition 3.1\] proves that {{\\,\\textrm{im}\\,}}\\Pi \_1^- and \\ker \\Pi \_C are complementary, and then \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Proposition 17.2.6\] implies that\
\
![](https://media.springernature.com/lw463/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ13_HTML.png)\
\
(15)\
\
\
is Fredholm since ( [11](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ9)) is Fredholm. Since \\Pi \_C\|\_{{{\\,\\textrm{im}\\,}}\\Pi \_1^-} is an isomorphism onto {{\\,\\textrm{im}\\,}}\\Pi \_C, therefore the proof of \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Proposition 17.2.6\] implies that the index of ( [15](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ13)) is the same as the index of ( [11](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ9)). \\square\
\
The following lemma is a simple exercise in Fredholm theory.\
\
### Lemma 4.7\
\
Let (F,G):H \\rightarrow A \\oplus B be Fredholm. Then {{\\tilde{F}}} = F\|\_{\\ker G}: {{\\tilde{H}}} = \\ker G \\rightarrow A is Fredholm and has index equal to {{\\,\\textrm{ind}\\,}}( (F,G) ) + \\dim {{\\,\\textrm{coker}\\,}}G .\
\
It implies that the operator  D\_{(A,\\Phi )}{{\\,\\textrm{SW}\\,}}\\oplus (\\Pi ^- R)  is Fredholm as a map ![](https://media.springernature.com/lw562/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq804_HTML.gif) and has index\
\
![](https://media.springernature.com/lw442/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ135_HTML.png)\
\
Thus, we have proven the Proposition for a particular splitting, s=s\_\\perp .\
\
For any splitting _s_, the inclusion \\Omega ^1\_{s}(X) \\hookrightarrow \\Omega ^1\_{CC}(X) is of codimension \\dim (H^1(X, Y; {\\mathbb {R}})) - \\dim (H^1(X; {\\mathbb {R}}) = b\_0(Y) - 1. Therefore, the split double Coulomb slice ![](https://media.springernature.com/lw150/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq808_HTML.gif) is a finite-dimensional subspace of the “full” double Coulomb slice ![](https://media.springernature.com/lw150/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq809_HTML.gif). Therefore the Fredholmness of ( [13](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ11)) for s = s\_\\perp  implies the Fredholmness of\
\
![](https://media.springernature.com/lw303/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ14_HTML.png)\
\
(16)\
\
\
and this, in turn, implies the Fredholmness of ( [13](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ11)) for any splitting _s_. Moreover, the index of ( [16](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ14)) is equal to b\_0(Y) - 1 plus ( [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ12)) for any splitting _s_, finishing the proof. \\square\
\
We turn to deducing the surjectivity of D{{\\,\\textrm{SW}\\,}} from the surjectivity of \\widetilde{D{{\\,\\textrm{SW}\\,}}}.\
\
### Proposition 4.8\
\
(Surjectivity of D{{\\,\\textrm{SW}\\,}}) For any gauge splitting _s_, the differential\
\
![](https://media.springernature.com/lw419/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ136_HTML.png)\
\
is surjective.\
\
### Proof\
\
We will prove a stronger statement, that this extended differential together with the exact part of the restriction to the boundary\
\
![](https://media.springernature.com/lw452/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ15_HTML.png)\
\
(17)\
\
\
is surjective, where ![](https://media.springernature.com/lw256/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq816_HTML.gif) is the projection along ![](https://media.springernature.com/lw104/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq817_HTML.gif) and {\\Pi }\_{V\_s}: \\Omega ^1(X) \\rightarrow V\_s = ({{\\,\\textrm{im}\\,}}s)^\\perp  is the orthogonal projection. The Proposition will follow since\
\
![](https://media.springernature.com/lw304/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ137_HTML.png)\
\
Proposition [4.3](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar65) implies that\
\
![](https://media.springernature.com/lw419/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ138_HTML.png)\
\
is surjective. To prove surjectivity of ( [17](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ15)) it thus remains to prove that\
\
![](https://media.springernature.com/lw289/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ139_HTML.png)\
\
is surjective and that\
\
\\begin{aligned} \\Pi \_{V\_s}: \\ker \\left(\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}, \\Pi \_d R\\right) \\rightarrow V\_s \\end{aligned}\
\
is surjective.\
\
We prove that \\Pi \_d R\|\_{\\ker \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}} is surjective. Take any g \\in L^2\_{3/2}(i \\Omega ^0(Y)) representing a given element dg \\in L^2\_{1/2}( i \\Omega ^1\_C(Y)). Take the unique f \\in L^2\_2(i \\Omega ^0(X)) such that \\Delta f = 0 and f\|\_Y = g. Then \\Pi \_d R(df, -f \\Phi ) = df\|\_Y = dg. The required surjectivity follows since  (df,-f \\Phi ) \\in \\ker \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}, which follows from d^\*d f = \\Delta f = 0 and Lemma [4.5](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar69).\
\
Similarly we prove \\Pi \_{V\_s}\|\_{\\ker \\left(\\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )}, \\Pi \_d R\\right)} is surjective. By ( [8](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ6)) and definition of V\_s, the orthogonal projection d({\\mathcal {H}}(X))) \\rightarrow V\_s is an isomorphism and therefore for any v \\in V\_s there is f \\in {\\mathcal {H}}(X) such that {\\Pi }\_{V\_s}(df)=v\_s. Moreover \\widetilde{D{{\\,\\textrm{SW}\\,}}}(df,-f\\Phi ) = 0 and {\\Pi }\_d R(df,-f\\Phi ) = 0, as wished. \\square\
\
Finally, we prove the density of the restriction map to a connected component of _Y_.\
\
### Proposition 4.9\
\
(Density of moduli on one boundary component) The restriction\
\
\\begin{aligned} R: \\ker \\left(D\_{(A,\\Phi )}{{\\,\\textrm{SW}\\,}}\\right) \\rightarrow L^2\_{1/2}\\bigl ({i \\Omega ^1\_{cC}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ) \\end{aligned}\
\
to a connected component Y\_0 \\subset Y is dense, where we consider  \\ker \\left(D\_{(A,\\Phi )}{{\\,\\textrm{SW}\\,}}\\right)  as a subset of ![](https://media.springernature.com/lw150/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq839_HTML.gif).\
\
### Proof\
\
Let  (b,\\psi ) \\in L^2\_{1/2}\\bigl ({i \\Omega ^1\_{cC}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ) \\subset L^2\_{1/2}\\bigl ({i\\Omega ^1\_{}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ). It follows from Proposition [4.4](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar67) that we can take a sequence  ({{\\tilde{a}}}\_k, \\phi \_k) \\in \\ker \\left( \\widetilde{D{{\\,\\textrm{SW}\\,}}}\_{(A,\\Phi )} \\right)  such that  R\_{Y\_0}({{\\tilde{a}}}\_k, \\phi \_k) \\rightarrow (b,\\psi ) in L^2\_{1/2}\\bigl ({i \\Omega ^1\_{cC}\\bigl ({Y\_0}\\bigr ) \\oplus \\Gamma \\bigl (S^{}\_{Y\_0}\\bigr )}\\bigr ). Using the decomposition ( [9](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ7)) we can write {{\\tilde{a}}}\_k = a\_k + d f\_k for f\_k \\in i \\Omega ^0(X) and a\_k \\in \\Omega ^1\_{s}(X). Since Y\_0 is connected, we can change f\_k by a constant to obtain \\int \_{Y\_0} f\_k = 0. Decomposing R\_{Y\_0}({{\\tilde{a}}}\_k) = R\_{Y\_0}(a\_k) + R\_{Y\_0}(d f\_k) we get that R\_{Y\_0}(a\_k) \\rightarrow b and R\_{Y\_0}(d f\_k) \\rightarrow 0. This together with \\int \_{Y\_0} f\_k = 0 implies that f\_k\|\_{Y\_0} \\rightarrow 0 and therefore\
\
\\begin{aligned} (b,\\psi )&= \\lim \_{k \\rightarrow \\infty } R\_{Y\_0}({{\\tilde{a}}}\_k, \\phi \_k) = \\lim \_{k \\rightarrow \\infty } R\_{Y\_0}(a\_k,\\phi \_k + i f\_k \\Phi ) \\end{aligned}\
\
which finishes the proof because ![](https://media.springernature.com/lw119/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq855_HTML.gif) and D{{\\,\\textrm{SW}\\,}}(a\_k,\\phi \_k + i f\_k \\Phi ) = D{{\\,\\textrm{SW}\\,}}(a\_k+i df\_k, \\phi \_k) = 0 by Lemma [4.5](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar69). \\square\
\
The results of Propositions [4.6](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar71), [4.8](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar74) and [4.9](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar76) can be summarized as follows.\
\
### Semi-infinite-dimensionality Theorem\
\
The moduli spaces ![](https://media.springernature.com/lw73/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq858_HTML.gif) are Hilbert manifolds. The differential of the twisted restriction map ![](https://media.springernature.com/lw211/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq859_HTML.gif) decomposes into ![](https://media.springernature.com/lw258/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq860_HTML.gif) which is Fredholm and ![](https://media.springernature.com/lw258/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq861_HTML.gif) which is compact.\
\
Moreover, if b\_0(\\partial X)>1, then for any connected component Y\_0 \\subset \\partial X the restriction R\_{\\tau ,Y\_0} to Y\_0 has dense differential.\
\
## 5 Gluing along a boundary component\
\
This section is devoted to the proof of the main result of this article, the Gluing Theorem, which relates the moduli spaces of solutions on X\_1, X\_2 and X = X\_1 \\cup \_{Y} X\_2, where _Y_ is a rational homology sphere, oriented as a component of the boundary of X\_1. Under the identification ![](https://media.springernature.com/lw170/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq870_HTML.gif) there are S^1-equivariant twisted restriction maps ![](https://media.springernature.com/lw229/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq872_HTML.gif), where {\\mathfrak {s}} = \\hat{{\\mathfrak {s}}}\|\_Y. One can expect the fiber product\
\
![](https://media.springernature.com/lw376/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ140_HTML.png)\
\
to be diffeomorphic to ![](https://media.springernature.com/lw73/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq874_HTML.gif), and this turns out to be true. One would also like to have this map intertwine the twisted restriction maps to \\partial X, but this is a bit too much: the splittings and twistings  (s,\\tau ), (s\_1,\\tau \_1), (s\_2,\\tau \_2), need to enjoy certain compatibility, and even then the restriction maps may not match on the nose but need to be homotoped to each other. This reflects the fact that we did not quotient by the action of S^1 on the configuration spaces.\
\
The proof utilizes the following fact which is of independent interest. Let X' \\subset X be a submanifold, the closure of which is contained in the interior of _X_. Then the restriction map from ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq881_HTML.gif) to L^2\_k-configurations on X' is well-defined and _smooth_ for any k \\ge 0. Well-definedness follows from a standard argument, but proving the smoothness of this map turns out to be a surprisingly delicate task which we tackle in Sect. [5.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#Sec18).\
\
The same strategy should work to prove smoothness of restriction maps to interior submanifolds for other types of moduli spaces appearing in gauge theory, e.g., for the space of anti-self-dual connections on G \\hookrightarrow P \\rightarrow X. The key is the ellipticity of the equations together with the gauge fixing.\
\
### 5.1 Smoothness of restrictions\
\
Assume X' \\subset \\mathring{X} is a submanifold with closure contained in \\mathring{X}. The goal is to show (cf. Theorem [5.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar80)) that the restriction map ![](https://media.springernature.com/lw218/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq888_HTML.gif) is smooth for any k \\ge 0, where\
\
![](https://media.springernature.com/lw356/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ141_HTML.png)\
\
We restrict ourselves to the case k=2, but the same strategy may be used iteratively, bootstraping the result to any _k_, if needed.\
\
Due to Theorem [A.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar94) we may assume, without loss of generality, that X' is of codimension 0. Since we require the closure of X' to be contained in the interior \\mathring{X}, and since \\partial X is compact, there exists a closed tubular neighborhood _N_ of the boundary \\partial X such that \\overline{X}' \\cap N = \\varnothing . This means that X'' = X {\\setminus } \\mathring{N} is a closed codimension-0 submanifold of _X_ with boundary. Moreover, X' \\subset X'', so (by possibly considering X'' instead of X') without loss of generality we may assume that X' itself is a closed codimension-0 submanifold with boundary.\
\
The following fundamental fact shows that any element in the image of the restriction map is itself a smooth configuration.\
\
### Lemma 5.1\
\
(Interior smoothness of solutions) \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Lemma 5.1.5\] Every ![](https://media.springernature.com/lw111/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq902_HTML.gif) is smooth on \\mathring{X}.\
\
We are ready to prove the main theorem of this subsection. Note that the surjectivity assumption is satisfied whenever \\partial X \\ne \\varnothing  due to Proposition [4.8](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar74).\
\
### Theorem 5.2\
\
(Restriction is smooth on solution sets) Assume that for any ![](https://media.springernature.com/lw146/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq905_HTML.gif) the operator D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )} is surjective. Then the restriction map ![](https://media.springernature.com/lw218/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq907_HTML.gif) is smooth.\
\
### Proof\
\
Choose a compact codimension-0 submanifold X'' \\subset \\mathring{X} such that X' \\subset \\mathring{X}''. Let us introduce an intermediate space L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr ) defined as the completion of i \\Omega ^1\_{CC}(X) \\oplus \\Gamma (S\_{X}^+) with respect to the norm  \\bigl \\Vert v\\bigr \\Vert \_{2,X''} = \\sqrt{\\Vert {\\hat{D}} v\\Vert ^2\_{L^2\_1(X'')} + \\Vert v\\Vert ^2\_{L^2\_1(X)}}, so that L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr ) is a Hilbert space. Define\
\
![](https://media.springernature.com/lw501/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ142_HTML.png)\
\
the set of solutions to the Seiberg–Witten equations in the corresponding configuration space. Since {{\\tilde{D}}} is elliptic and  {{\\tilde{D}}} v = ({\\hat{D}} v, 0) , by Theorem [A.3](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar97) the restriction map\
\
\\begin{aligned} L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr )\\rightarrow L^2\_2(i \\Omega ^1(X') \\oplus \\Gamma (S\_{X'}^+)) \\end{aligned}\
\
is continuous linear (thus smooth). It thus suffices to prove that the moduli space ![](https://media.springernature.com/lw102/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq916_HTML.gif) is a smooth submanifold of the configuration space (A\_0,0)+L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr ) and that the identity embedding ![](https://media.springernature.com/lw246/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq918_HTML.gif) is well-defined, continuous and smooth.\
\
Firstly, it is well-defined by Lemma [5.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar79).\
\
Secondly, we prove that ![](https://media.springernature.com/lw102/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq919_HTML.gif) is a smooth submanifold of (A\_0,0)+L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr ). Define L^2\_{1,X''}\\bigl (i \\Omega ^+(X) \\oplus \\Gamma \\left(S\_X^+\\right)\\bigr ) to be the Hilbert space obtained as the completion of i \\Omega ^+(X) \\oplus \\Gamma (S\_X^+) with respect to the norm  \\Vert v\\Vert \_{L^2(X) \\cap L^2\_1(X'')} = \\sqrt{\\Vert v\\Vert ^2\_{L^2(X)} + \\Vert v\\Vert ^2\_{L^2\_1(X'')}}. By the Implicit Function Theorem, it suffices to prove the following Lemma. \\square\
\
### Lemma 5.3\
\
The differential\
\
\\begin{aligned} D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )}: L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr )\\rightarrow L^2\_{1,X''}\\bigl (i \\Omega ^+(X) \\oplus \\Gamma \\left(S\_X^+\\right)\\bigr )\\end{aligned}\
\
is surjective at each ![](https://media.springernature.com/lw167/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq925_HTML.gif).\
\
### Proof\
\
We assumed that the operator  D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )}  is surjective. Choose any w \\in L^2\_{1,X''}\\bigl (i \\Omega ^+(X) \\oplus \\Gamma \\left(S\_X^+\\right)\\bigr ) and pick a solution ![](https://media.springernature.com/lw190/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq928_HTML.gif) to D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )}(v) = w. Then {\\hat{D}} v\|\_{X''} = - {\\hat{K}} v \|\_{X''} + w\|\_{X''} is in L^2\_1(X'') since w\|\_{X''} \\in L^2\_1(X''), v\|\_{X''} \\in L^2\_1(X'') and {\\hat{K}}\|\_{X''} is a certain multiplication by  (A - A\_0,\\Phi )\|\_{X''} , which is smooth by Lemma [5.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar79). \\square\
\
Finally, it remains to prove that the identity map\
\
![](https://media.springernature.com/lw209/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ143_HTML.png)\
\
is smooth. We start by identifying the tangent spaces at p = (A,\\Phi ); we have\
\
![](https://media.springernature.com/lw435/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ144_HTML.png)\
\
### Lemma 5.4\
\
(Isometry of the tangent spaces) The map  { {\\widetilde{{\\mathcal {M}}}^\\circ \_{CC,X''}({X},\\hat{{\\mathfrak {s}}}\_{})}} induced by the identity is well-defined, and an isometry.\
\
### Proof\
\
Take any ![](https://media.springernature.com/lw127/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq939_HTML.gif); in particular, D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )}(v)=0. Well-definedness follows since  {\\hat{D}} v\|\_{X''} = - {\\hat{K}} v\|\_{X''} and as before, {\\hat{K}}\|\_{X''} is a multiplication by a smooth configuration on X''. This also implies\
\
\\begin{aligned} \\Vert v\\Vert ^2\_{L^2\_1(X)}&\\le \\bigl \\Vert v\\bigr \\Vert \_{2,X''}^2 = \\Vert v\\Vert ^2\_{L^2\_1(X)} + \\Vert {\\hat{D}} v\\Vert ^2\_{L^2\_1(X'')}\\\&= \\Vert v\\Vert ^2\_{L^2\_1(X)} + \\Vert {\\hat{K}} v\\Vert ^2\_{L^2\_1(X'')}\\\&\\le \\Vert v\\Vert ^2\_{L^2\_1(X)} + C\_p \\Vert v\\Vert ^2\_{L^2\_1(X'')}\\\&\\le (1+C\_p) \\Vert v\\Vert ^2\_{L^2\_1(X)} \\end{aligned}\
\
which proves this map is an isometry. \\square\
\
While the L^2(X) norm is not complete on ![](https://media.springernature.com/lw163/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq946_HTML.gif), the L^2(X)-orthogonal complement _H_ to ![](https://media.springernature.com/lw99/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq948_HTML.gif) is a closed subspace of ![](https://media.springernature.com/lw163/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq949_HTML.gif) satisfying the conditions ![](https://media.springernature.com/lw175/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq950_HTML.gif) and ![](https://media.springernature.com/lw319/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq951_HTML.gif), thus by the open mapping theorem\
\
![](https://media.springernature.com/lw324/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ145_HTML.png)\
\
By the Implicit Function Theorem there is a neighborhood _U_ of _p_ such that the affine projection\
\
![](https://media.springernature.com/lw352/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ146_HTML.png)\
\
along _H_ is a diffeomorphism. Similarly, the Implicit Function Theorem implies that there is a neighborhood _V_ of _p_ such that the affine projection\
\
![](https://media.springernature.com/lw397/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ147_HTML.png)\
\
along H' = H \\cap L^2\_{2,X''}\\bigl (i \\Omega ^1\_{CC}(X) \\oplus \\Gamma \\left(S\_X\\right)\\bigr ) is a diffeomorphism since H' is the L^2(X)-orthogonal complement to ![](https://media.springernature.com/lw119/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq955_HTML.gif). Thus the identity map ![](https://media.springernature.com/lw211/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq956_HTML.gif) near _p_ factors as\
\
![](https://media.springernature.com/lw378/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ148_HTML.png)\
\
where the middle identity map is smooth by Lemma [5.4](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar84) and the two other maps are smooth since they are parametrizations coming from the Implicit Function Theorem, as we just showed.\\square\
\
### 5.2 Proof of the gluing theorem\
\
We are ready to prove the gluing theorem.\
\
Let X = X\_1 \\cup \_{Y} X\_2 with _Y_ connected and b\_1(\\partial X\_i) = 0. Let \\hat{{\\mathfrak {s}}} be a spin^{c} structure and A\_0 be a reference spin^{c} connection on _X_. Let restrictions of \\hat{{\\mathfrak {s}}} be the spin^{c} structures used to define configuration spaces and the restrictions of A\_0 to be the reference connections. Denote Y\_1 = \\partial X\_1 \\setminus Y, Y\_2 = \\partial X\_2 {\\setminus } Y, \\hat{{\\mathfrak {s}}}\_i = \\hat{{\\mathfrak {s}}}\|\_{X\_i}. Fix gauge splittings s,s\_1,s\_2 and twistings \\tau , \\tau \_1, \\tau \_2 on X, X\_1, X\_2.\
\
Denote by s\_{{\\mathbb {Z}}}, s\_{1,{\\mathbb {Z}}}, s\_{2,{\\mathbb {Z}}} the associated integral splittings given by Proposition [3.30](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar55). We say they are _compatible_ if s\_{{\\mathbb {Z}}} corresponds to (s\_{1,{\\mathbb {Z}}}, s\_{2,{\\mathbb {Z}}}) under the following identification.\
\
### Proposition 5.5\
\
(Integral splittings on a composite cobordism) There is a canonical identification between the set of integral splittings on _X_ and the set of pairs of integral splittings on X\_1 and X\_2.\
\
### Proof\
\
Choose an integral splitting _s_. Take any a \\in {\\mathcal {H}}^1\_D(X). Denote by {\\tilde{a}}\_i its restriction to X\_i. For each _i_ there is a unique f\_i \\in L^2\_2(\\Omega ^0(X\_i)) such that \\Delta f\_i = 0, f\_i\|\_Y = G\_d \\iota \_Y^\*(a), and f\_i\|\_{Y\_i} = 0. The resulting a\_i = {\\tilde{a}}\_i - df\_i is in {\\mathcal {H}}^1\_D(X\_i), thus we get a map\
\
\\begin{aligned} R\_{{\\mathcal {H}}}: {\\mathcal {H}}^1\_D(X) \\rightarrow {\\mathcal {H}}^1\_D(X\_1) \\times {\\mathcal {H}}^1\_D(X\_2) \\end{aligned}\
\
sending _a_ to  (a\_1,a\_2). Note that {\\mathcal {H}}^1\_D(X\_i) \\subset \\Omega ^1\_{CC}(X\_i) and therefore R\_{{\\mathcal {H}}} coincides with doing the gauge fixing of Lemma [3.17](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar36) on both components, i.e.,  a \\mapsto ({\\Pi }\_{CC}(a\|\_{X\_1}), {\\Pi }\_{CC}(a\|\_{X\_2})) . The cohomology class \[a\] \\in H^1(X; {\\mathbb {R}}) restricts to  (\[{\\tilde{a}}\_1\],\[{\\tilde{a}}\_2\]) = ( \[a\_1\], \[a\_2\]) \\in H^1(X\_1;{\\mathbb {R}}) \\times H^1(X\_2;{\\mathbb {R}}). It follows that the composition\
\
\\begin{aligned} H^1(X\_1;{\\mathbb {R}})&\\times H^1(X\_2;{\\mathbb {R}}) \\xrightarrow {\\iota \_\*} H^1(X; {\\mathbb {R}}) \\xrightarrow {s^H} {\\mathcal {H}}^1\_D(X) \\rightarrow \\\&\\xrightarrow {R\_{{\\mathcal {H}}}} {\\mathcal {H}}^1\_D(X\_1) \\times {\\mathcal {H}}^1\_D(X\_2) \\rightarrow H^1(X\_1;{\\mathbb {R}}) \\times H^1(X\_2;{\\mathbb {R}}) \\end{aligned}\
\
is the identity, where \\iota \_\* is the inverse of the restriction map H^1(X; {\\mathbb {R}})\\rightarrow H^1(X\_1;{\\mathbb {R}}) \\times H^1(X\_2;{\\mathbb {R}}) (invertible by Mayer–Vietoris). We can thus choose  (s\_1^H,s\_2^H)  to be the composition R\_{{\\mathcal {H}}} \\circ s^H \\circ \\iota \_\*. Since s^H was integral, thus s\_i^H are integral and by Proposition [3.24](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar46) there exist unique integral splittings s\_1, s\_2 inducing s\_1^H, s\_2^H.\
\
On the other hand, given integral splittings s\_1, s\_2 on X\_1, X\_2, we can choose s^H to be  (R\_{{\\mathcal {H}}})^{-1} \\circ (s\_1^H,s\_2^H) \\circ (\\iota \_\*)^{-1} and by Proposition [3.24](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar46) there is a unique integral splitting _s_ inducing s^H. \\square\
\
Proposition [4.8](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar74) guarantees that whenever \\partial X \\ne \\varnothing , the moduli ![](https://media.springernature.com/lw73/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1008_HTML.gif) is a smooth Hilbert manifold, and the same follows for ![](https://media.springernature.com/lw81/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1009_HTML.gif). We want to include the case when _X_ is a closed manifold, when it is well-known that to achieve surjectivity one, in general, needs to perturb the metric on _X_ or perturb the Seiberg–Witten equations. Therefore, we _assume_ that for any (A,\\Phi ) \\in {{\\,\\textrm{SW}\\,}}^{-1}(0) the operator D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )} is onto.\
\
### Remark 5.6\
\
The careful reader may notice that we do not assume any transversality of the maps R\_{\\tau \_i,Y} and thus the fiber product may not _a priori_ be a manifold. That it is a manifold follows from the proof of the theorem. What is not proven here, but may be useful in other contexts, is that the transversality is indeed equivalent to D{{\\,\\textrm{SW}\\,}}\_{(A,\\Phi )} being surjective for all ![](https://media.springernature.com/lw137/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1014_HTML.gif).\
\
### Gluing Theorem\
\
Assume s\_{{\\mathbb {Z}}} and  (s\_{1,{\\mathbb {Z}}}, s\_{2,{\\mathbb {Z}}}) are compatible. Then there is an S^1-equivariant diffeomorphism\
\
![](https://media.springernature.com/lw341/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ149_HTML.png)\
\
such that R\_{\\tau } is S^1-equivariantly homotopic to  \\left( R\_{\\tau \_1} \\times \_{Y} R\_{\\tau \_2} \\right) \\circ F.\
\
### Proof\
\
By Corollary [3.34](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar61) we can assume, without loss of generality, that s = s\_{{\\mathbb {Z}}} and s\_i = s\_{i,{\\mathbb {Z}}}, as well as \\tau \\equiv 1 and \\tau \_i \\equiv 1. We thus drop \\tau ’s from the notation entirely.\
\
The plan is as follows. We will construct a map\
\
![](https://media.springernature.com/lw318/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ150_HTML.png)\
\
and a homotopy\
\
![](https://media.springernature.com/lw314/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ151_HTML.png)\
\
between _R_ and  \\left(R\_{Y\_1} \\times R\_{Y}\\right) \\circ F. Then we will prove that _F_ intertwines the actions of ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1027_HTML.gif) and ![](https://media.springernature.com/lw140/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1028_HTML.gif), and that _H_ is ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1029_HTML.gif)-invariant; thus, both _F_ and _H_ descend to ![](https://media.springernature.com/lw73/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1030_HTML.gif). Furthermore, we will prove _F_ and _H_ are continuous and smooth, and that _F_ has image in the fiber product. Finally, we will show that _F_ is a smooth immersion onto ![](https://media.springernature.com/lw207/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1031_HTML.gif) The S^1-equivariance of _F_ and _H_ will be apparent from the construction.\
\
_Step 1_ We start by constructing _F_, proving its smoothness and that its image lies in the fiber product. Take ![](https://media.springernature.com/lw137/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1033_HTML.gif). We would like to simply restrict it to the components X\_i and then put into split Coulomb slice. By Lemma [3.17](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar36) modulo S^1 there a unique way of doing that using a nullhomotopic gauge transformation. Here we make a different choice than in Lemma [3.17](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar36), requiring \\int \_{Y} f = 0 instead of \\int \_X f = 0. Precisely, for ![](https://media.springernature.com/lw118/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1038_HTML.gif) choose {\\tilde{u}}^s\_a = e^{f\_a} such that f\_a \\in L^2\_2(i \\Omega ^0(X\_i)), \\int \_{Y} f\_a = 0 and ![](https://media.springernature.com/lw220/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1042_HTML.gif) Define\
\
\\begin{aligned} F(A,\\Phi ) = \\left( {\\tilde{u}}^s\_{(A-A\_0)\|\_{X\_1}} (A,\\Phi )\|\_{X\_1}, {\\tilde{u}}^s\_{(A-A\_0)\|\_{X\_2}} (A,\\Phi )\|\_{X\_2} \\right). \\end{aligned}\
\
Since\
\
A-A\_0 was in double Coulomb slice, thus (A-A\_0)\|\_{X\_1} (resp. (A-A\_0)\|\_{X\_2}) is already coclosed on X\_1 (resp. X\_2) and on Y\_1 (resp. Y\_2), moreover (A-A\_0)\|\_{X\_1} and (A-A\_0)\|\_{X\_2} agree on _Y_. Denoting the restriction to _Y_ by b\_{(A,\\Phi )} = \\iota ^\*\_{Y}(A-A\_0), Theorem [5.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar80) together with Theorem [A.2](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar94) imply that b\_{(A,\\Phi )} is smooth and depends smoothly on ![](https://media.springernature.com/lw133/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1054_HTML.gif) as an element of L^2\_{3/2}. Notice that f\_i = f\_{(A-A\_0)\|\_{X\_i}} can be decomposed as f\_i = f\_i^{\\partial } + f\_i^s, where f\_i^\\partial  are the unique solutions to\
\
\\begin{aligned} f\_i^\\partial \|\_{Y\_i} = 0, \\quad f\_i\|\_{Y} = g,&\\quad \\Delta f\_i = 0, \\end{aligned}\
\
(18)\
\
\
where g = G\_d \\Pi \_d b\_{(A,\\Phi )} depends smoothly on (A,\\Phi ) as an element of L^2\_{5/2}. Moreover, the map g \\mapsto f\_i^\\partial  is linear and continuous as a map L^2\_{s+1/2} \\rightarrow L^2\_{s+1} for s \\ge 0, so f\_i^\\partial  depend smoothly on (A,\\Phi ) as elements of L^2\_3. Furthermore, since a\|\_{X\_i} - df\_i^\\partial \\in L^2\_1(i\\Omega ^1\_{CC}(X\_i)), f\_i^s are the unique elements of {\\mathcal {H}}^1\_D(X\_i) such that a\|\_{X\_i} - df\_i^\\partial - d f\_i^s \\in L^2\_1(i \\Omega ^1\_s(X\_i)) and f\_i\|\_Y = 0. By Remark [3.18](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar38), f\_i^s depend continuously on a\|\_{X\_i} - d f\_i^\\partial \\in L^2\_1. Which proves that f\_i \\in L^2\_3 depend continuously and linearly on g \\in L^2\_{5/2}, thus depend smoothly on _g_, so they depend smoothly on  (A,\\Phi ).\
\
This establishes the well-definedness and smoothness of _F_. That its image lies in the fiber product follows directly from the construction.\
\
_Step 2_ We proceed to constructing _H_. By ( [18](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ16)), the functions f\_i are locally constant on Y\_i. We also have\
\
\\begin{aligned} R\_{Y\_i}(F(A,\\Phi )) = e^{f\_i\|\_{Y\_i}} \\cdot R\_{Y\_i}(A,\\Phi ) \\end{aligned}\
\
by the construction of _F_. Thus we can define\
\
\\begin{aligned} H(A,\\Phi ,t) = \\left( e^{t f\_1\|\_{Y\_1}}, e^{t f\_2\|\_{Y\_2}} \\right) R(A,\\Phi ) \\end{aligned}\
\
which at t=0 coincides with R(A,\\Phi ) and at t=1 coincides with  (R\_{Y\_1},R\_{Y\_2}) \\circ F(A,\\Phi ).\
\
_Step 3_ We now investigate the equivariance of _F_ under the actions of gauge groups. Let ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1084_HTML.gif). From Lemma [3.17](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar36) if follows that there is exactly one nullhomotopic {\\tilde{u}}\_i = e^{{\\tilde{f}}\_i}\\in {{\\mathcal {G}}}^{e}(X\_i) which puts -u^{-1}du into ![](https://media.springernature.com/lw89/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1087_HTML.gif) with \\int \_{Y} {\\tilde{f}}\_i = 0. Equivalently, this is the unique {\\tilde{u}}\_i = e^{{\\tilde{f}}\_i} \\in {{\\mathcal {G}}}^{e}(X\_i) with \\int \_{Y} {\\tilde{f}}\_i = 0 such that ![](https://media.springernature.com/lw122/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1091_HTML.gif). Define u\_i = {\\tilde{u}}\_i u\|\_{X\_i}. Since {\\tilde{u}}\_i is nullhomotopic, thus \[\\iota \_{X\_i}^\*(u^{-1}du)\] = \[u\_i^{-1}du\_i\] in H^1(X\_i; 2 \\pi i {\\mathbb {Z}}). Therefore the map u \\mapsto (u\_1,u\_2) provides the canonical isomorphism\
\
![](https://media.springernature.com/lw214/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_Equ17_HTML.png)\
\
(19)\
\
\
which agrees with the isomorphism coming from the Mayer–Vietoris sequence H^1(X; {\\mathbb {Z}}) \\simeq H^1(X\_1;{\\mathbb {Z}}) \\times H^1(X\_2;{\\mathbb {Z}}). From the construction of F(A,\\Phi ) it follows that (u\|\_{X\_1}^{-1},u\|\_{X\_2}^{-1}) F(u(A,\\Phi )) differs from F(A,\\Phi ) exactly by the factor of  (e^{{\\tilde{f}}\_1},e^{{\\tilde{f}}\_2}) . Thus  (u\_1^{-1},u\_2^{-1}) F(u(A,\\Phi )) = F(A,\\Phi ). This proves that _F_ commutes with the gauge group action as identified in ( [19](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ17)).\
\
_Step 4_ We prove the invariance of _H_ under ![](https://media.springernature.com/lw53/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1103_HTML.gif). By the construction of _H_, and since u\|\_{\\partial X} = 1 for ![](https://media.springernature.com/lw82/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1105_HTML.gif), we have H( u(A,\\Phi ), t) = (e^{t{\\tilde{f}}\_1\|\_{Y\_1}},e^{t{\\tilde{f}}\_2\|\_{Y\_2}}) H(A,\\Phi ,t) where {\\tilde{f}}\_i are as in the previous paragraph. Since R\_{{\\mathcal {H}}}({\\mathcal {H}}^1\_D(X)) \\in ({{\\,\\textrm{im}\\,}}s\_1^H) \\times ({{\\,\\textrm{im}\\,}}s\_2^H) we get that R\_{{\\mathcal {H}}}(u^{-1}du) is already in the split Coulomb slice on X\_1 and X\_2. Moreover, a\_i = \\iota ^\*\_{X\_i}(u^{-1} du) is coclosed on X\_i and Y\_i. Since there are functions \\hat{f}\_i satisfying\
\
\\begin{aligned} \\Delta \\hat{f}\_1 = 0, \\quad \\hat{f}\_1\|\_{Y\_1} = 0,&\\quad \\hat{f}\_1\|\_Y = G\_d \\iota ^\*\_Y a, \\\ \\Delta \\hat{f}\_2 = 0, \\quad \\hat{f}\_2\|\_{Y\_2} = 0,&\\quad \\hat{f}\_2\|\_{Y} = G\_d \\iota ^\*\_Y a, \\end{aligned}\
\
the uniqueness of {\\tilde{f}}\_i implies {\\tilde{f}}\_i = \\hat{f}\_i and therefore {\\tilde{f}}\_i\|\_{Y\_i} = 0. Therefore H(u(A,\\Phi ),t) = H(A,\\Phi ,t), as wished.\
\
_Step 5_ We show that _F_ is bijective onto the fiber product, following the argument in \[ [21](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR21 "Lipyanskiy, M.: A semi-infinite cycle construction of Floer homology (2008). Thesis (Ph.D.)—Massachusetts Institute of Technology")\]. Let ![](https://media.springernature.com/lw152/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1120_HTML.gif) such that  R\_{Y}(A\_1,\\Phi \_1) = R\_{Y}(A\_2,\\Phi \_2). These would give a configuration on _X_ if the normal components of connections A\_1 and A\_2 agreed on _Y_. Let h\_1\\,dt and h\_2\\,dt be the _dt_-components of  (A\_1-A\_0)\|\_{Y} and  (A\_2-A\_0)\|\_{Y}. We want to find harmonic functions f\_i \\in L^2\_2(X\_i;i {\\mathbb {R}}) such that\
\
\\begin{aligned}{} & {} f\_1\|\_{Y} = f\_2\|\_{Y},\\\{} & {} \\partial \_t f\_1\|\_{Y} + h\_1 = \\partial \_t f\_2\|\_{Y} + h\_2, \\\{} & {} f\_1\|\_{Y\_1} = 0, f\_2\|\_{Y\_2} = 0. \\end{aligned}\
\
Take a tubular neighborhood  \[-\\varepsilon ,\\varepsilon \] \\times Y \\subset X of _Y_. Let \\{\\phi \_\\lambda \\}\_{\\lambda \\in \\Lambda } be a normalized (\\Vert \\phi \_\\lambda \\Vert \_{L^2} = 1) eigenbasis for \\Delta \_{Y} (using the convention that \\Delta \_Y \\phi \_\\lambda = \\lambda \\phi \_\\lambda , \\lambda \\ge 0, for \\lambda  in the multiset of eigenvalues \\Lambda ) and write h\_2-h\_1 = \\sum \_{\\lambda \\in \\Lambda } c\_\\lambda \\phi \_\\lambda . Since h\_2 - h\_1 \\in L^2\_{1/2}, therefore\
\
\\begin{aligned} \\sum \_{\\lambda \\in \\Lambda } \\lambda ^{1/2} \|c\_\\lambda \|^2 < \\infty \\end{aligned}\
\
(20)\
\
\
and thus the following are well-defined as elements of  L^2\_2(\[-\\varepsilon ,0\] \\times Y; i {\\mathbb {R}}) and  L^2\_2(\[0,\\varepsilon \] \\times Y; i {\\mathbb {R}}), respectively:\
\
\\begin{aligned} g\_1&= \\frac{1}{2} \\sum \_{\\lambda \\in \\Lambda } c\_\\lambda \\lambda ^{-1/2} e^{\\lambda ^{1/2} t} \\phi \_\\lambda ,\\nonumber \\\ g\_2&= \\frac{1}{2} \\sum \_{\\lambda \\in \\Lambda } c\_\\lambda \\lambda ^{-1/2} e^{-\\lambda ^{1/2} t} \\phi \_\\lambda . \\end{aligned}\
\
(21)\
\
\
To show well-definedness, consider, for example, g\_1. The functions e^{\\lambda ^{1/2}t} \\phi \_\\lambda  on \[-\\varepsilon ,0\] \\times Y have L^2-norm bounded above by  \\Vert \\phi \_\\lambda \\Vert \_{L^2(Y)}\\sqrt{\\int \_{-\\varepsilon }^0 e^{2 \\lambda ^{1/2} t}dt} \\le \\lambda ^{-1/4}  (the last inequality coming from \\int e^{2 \\lambda ^{1/2} t} dt = \\frac{1}{2} \\lambda ^{-1/2} e^{2 \\lambda ^{1/2} t}), and are pairwise orthogonal, so ( [20](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ18)) implies that ( [21](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ19)) converges in L^2. Similarly, their _t_-derivatives are \\partial \_t e^{\\lambda ^{1/2}t} \\phi \_\\lambda = \\lambda ^{1/2} e^{\\lambda ^{1/2}t} \\phi \_\\lambda , pairwise L^2-orthogonal and with the L^2-norm bounded by \\lambda ^{1/4}. It thus follows that the sequence\
\
\\begin{aligned} \\sum \_{\\lambda \\in \\Lambda } c\_\\lambda \\lambda ^{-1/2} \\partial \_t e^{\\lambda ^{1/2} t} \\phi \_\\lambda \\end{aligned}\
\
converges in L^2 to \\partial \_t g\_1; and since \\sqrt{\\Delta \_Y} e^{\\lambda ^{1/2}t} \\phi \_\\lambda = \\lambda ^{1/2} e^{\\lambda ^{1/2}t} \\phi \_\\lambda , we also have the L^2-convergence\
\
\\begin{aligned} \\sqrt{\\Delta \_Y} g\_1 = \\sum \_{\\lambda \\in \\Lambda } c\_\\lambda \\lambda ^{-1/2} \\sqrt{\\Delta \_Y} e^{\\lambda ^{1/2} t} \\phi \_\\lambda , \\end{aligned}\
\
so g\_1 \\in L^2\_1. Since\
\
\\begin{aligned} \\partial \_t^2 e^{\\lambda ^{1/2}t} \\phi \_\\lambda \\partial \_t \\sqrt{\\Delta \_Y} e^{\\lambda ^{1/2}t} \\phi \_\\lambda \\Delta \_Y e^{\\lambda ^{1/2}t} \\phi \_\\lambda = \\lambda e^{\\lambda ^{1/2}t} \\phi \_\\lambda , \\end{aligned}\
\
with the L^2-norm bounded by \\lambda ^{3/4}, and\
\
\\begin{aligned} \\sum \_{\\lambda \\in \\Lambda } \|c\_\\lambda \|^2 \| \\lambda ^{-1/2} \|^2 \\Vert \\lambda e^{\\lambda ^{1/2}t} \\phi \_\\lambda \\Vert ^2\_{L^2} \\le \\sum \_{\\lambda \\in \\Lambda } \|c\_\\lambda \|^2 \\lambda ^{-1} \\lambda ^{3/2} = \\sum \_{\\lambda \\in \\Lambda } \|c\_\\lambda \|^2 \\lambda ^{1/2} \\le \\infty , \\end{aligned}\
\
thus by ( [20](https://link.springer.com/article/10.1007/s00029-023-00845-y#Equ18)) we get g\_1 \\in L^2\_2.\
\
These satisfy \\partial \_t g\_1\|\_{Y} - \\partial \_t g\_2\|\_{Y} = h\_1-h\_0. Let \\rho \\in C^\\infty (X;{\\mathbb {R}}) be a bump function supported in \[-\\varepsilon ,\\varepsilon \] \\times Y which is identically 1 in a neighborhood of _Y_. The configurations e^{\\rho g\_1}(A\_1,\\Phi \_1) and e^{\\rho g\_2} (A\_2,\\Phi \_2) patch to give a L^2\_1 configuration  (A',\\Phi '), but this is not necessarily in the Coulomb slice because \\rho f\_i' are not necessarily harmonic. Take f \\in L^2\_2(X;i {\\mathbb {R}}) such that\
\
\\begin{aligned} f\|\_{Y\_1} = 0, \\quad f\|\_{Y\_2} = 0, \\quad \\Delta f = - \\Delta (\\rho g\_1) - \\Delta (\\rho g\_2). \\end{aligned}\
\
Denote ![](https://media.springernature.com/lw255/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1169_HTML.gif). Finally, by Remark [3.18](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar38) we can continuously deform (A'',\\Phi '') to a configuration (A,\\Phi ) such that F(A,\\Phi ) = ( (A\_1,\\Phi \_1), (A\_2,\\Phi \_2) ).\
\
_Step 6_ We need to prove that F^{-1} constructed in the previous step is continuous. Notice  (g\_1,g\_2)  as elements of L^2\_2 depend continuously on h\_1-h\_0 \\in L^2\_{1/2} which in turn depends continuously on A\_1-A\_0 and A\_2-A\_0 \\in L^2\_{1/2}. Moreover, f \\in L^2\_3 depends continuously on  (g\_1,g\_2) \\in L^2\_2 . If the multiplication L^2\_2 \\times L^2\_1 \\rightarrow L^2\_1 was continuous on 4-manifolds then we would have shown that the map  ((A\_1,\\Phi \_1),(A\_2,\\Phi \_2)) \\rightarrow (A,\\Phi ) which we constructed is continuous. Since it is not true, we need to show that  e^{g\_i} \\Phi \_i \\in L^2\_1 depends continuously on the initial configurations.\
\
We will prove it depends continuously on  h\_2-h\_1 \\in L^2\_{1/2} and \\Phi \_i \\in L^2\_1. Let  (A\_1',\\Phi \_1') and  (A\_2',\\Phi \_2')  be another choice of configurations, and denote the corresponding harmonic functions on \[-\\varepsilon ,0\] \\times Y and  \[0,\\varepsilon \] \\times Y by g'\_1, g'\_2. Then\
\
\\begin{aligned} \\Vert e^{g\_1} \\Phi \_1 - e^{g'\_1} \\Phi \_1' \\Vert \_{L^2\_1}&\\le \\Vert e^{g'\_1} (\\Phi \_1 - \\Phi \_1') \\Vert \_{L^2\_1} + \\Vert (e^{g\_1} - e^{g'\_1}) \\Phi \_1 \\Vert \_{L^2\_1}\\\&\\le C(\\Vert e^{g'\_1} \\Vert \_{L^\\infty } + \\Vert e^{g'\_1} \\Vert \_{L^2\_2}) \\Vert \\Phi \_1 - \\Phi \_1'\\Vert \_{L^2\_1}\\\&\\quad + C \\Vert e^{g\_1}-e^{g'\_1}\\Vert \_{L^2\_2} \\Vert \\Phi \_1\\Vert \_{L^2\_1}\\\&\\quad + C \\Vert e^{g\_1}-e^{g'\_1}\\Vert \_{L^\\infty (\[-\\varepsilon ,-\\delta \] \\times Y)} \\Vert \\Phi \_1\\Vert \_{L^2\_1(\[-\\varepsilon ,-\\delta \] \\times Y)} \\\&\\quad + C \\Vert e^{g\_1}-e^{g'\_1}\\Vert \_{L^\\infty (\[-\\delta ,0\] \\times Y)} \\Vert \\Phi \_1\\Vert \_{L^2\_1(\[-\\delta ,0\] \\times Y)} \\end{aligned}\
\
for any \\delta . One can choose \\delta  to have  \\Vert \\Phi \_1\\Vert \_{L^2\_1(\[-\\delta ,0\] \\times Y} as small as one wants while  \\Vert e^{g\_1}-e^{g'\_1}\\Vert \_{L^\\infty (\[-\\delta ,0\] \\times Y)} \\le 2. Moreover, we have\
\
\\begin{aligned} \\Vert e^{g\_1}-e^{g'\_1}\\Vert \_{L^\\infty (\[-\\varepsilon ,-\\delta \] \\times Y)} \\le \\Vert g\_1 - g'\_1\\Vert \_{L^\\infty (\[-\\varepsilon ,-\\delta \] \\times Y)} \\le C \\Vert (h\_1 - h\_2) - (h\_1' - h\_2')\\Vert \_{L^2\_{1/2}} \\end{aligned}\
\
via a direct computation (or by interior regularity estimates following from Theorem [A.3](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar97)). This finishes the proof that the inverse map is continuous.\
\
_Step 7_ Finally, we prove that the differential of _F_ is invertible. Assume this is not the case, so that there exists ![](https://media.springernature.com/lw133/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1196_HTML.gif) such that for any \\varepsilon >0 there is ![](https://media.springernature.com/lw142/springer-static/image/art%3A10.1007%2Fs00029-023-00845-y/MediaObjects/29_2023_845_IEq1198_HTML.gif) such that 0< D = \\Vert F (A,\\Phi ) - F (A',\\Phi ') \\Vert \_{L^2\_1} < 1 and  \\Vert (A-A',\\Phi -\\Phi ') \\Vert \_{L^2\_1} \\le D \\varepsilon . We get that  \\Vert g-g'\\Vert \_{L^2\_{5/2}} \\le C\_{5/2} D \\varepsilon  and thus\
\
\\begin{aligned} \\Vert f\_i - f\_i'\\Vert \_{L^2\_3}&\\le C \\Vert g - g'\\Vert \_{L^2\_{5/2}}\\\&\\le C C\_{5/2} D \\varepsilon . \\end{aligned}\
\
From this and Theorem [A.1](https://link.springer.com/article/10.1007/s00029-023-00845-y#FPar92) it follows that  D = \\Vert F(A,\\Phi ) - F(A',\\Phi ') \\Vert \_{L^2\_1} \\le C'' \\Vert (A-A',\\Phi -\\Phi ') \\Vert \_{L^2\_1} \\le C''D \\varepsilon  for some C'' depending on \\Vert \\Phi \\Vert \_{L^2\_1}. Choosing \\varepsilon = \\frac{1}{1+C''} gives the desired contradiction. \\square\
\
### Remark 5.7\
\
The author’s understanding is that without the use of twistings there is (in general) no choice of s, s\_1, s\_2 making _F_ commute with the restriction maps on the nose. This problem does not show up in the construction of monopole Floer homology since there one quotients the moduli and configuration spaces by S^1 after blowing up.\
\
## References\
\
01. Abouzaid, M., Blumberg, A.J.: Arnold Conjecture and Morava K-theory (2021) preprint\
\
02. Atiyah, M.: New invariants of 3\- and 4-dimensional manifolds. The mathematical heritage of Hermann Weyl (Durham, NC, 1987). In: Proceedings of Symposium on Pure Mathematics, vol. 48. American Mathematical Society, Providence, pp. 285–299 (1988)\
\
03. Atiyah, M.F., Bott, R.: The Yang–Mills equations over Riemann surfaces. Philos. Trans. R. Soc. Lond. Ser. A **308**(1505), 523–615 (1983)\
\
04. Brezis, H., Mironescu, P.: Gagliardo–Nirenberg, composition and products in fractional Sobolev spaces. J. Evol. Equ. **1**(4), 387–404 (2001). ( **Dedicated to the memory of Tosio Kato**)\
\
05. Cohen, R.L., Jones, J.D.S., Segal, G.B.: Floer’s infinite dimensional Morse theory and Homotopy theory. In: The Floer memorial volume. Progress in Mathematics, vol. 133. Birkhäuser, Basel, pp. 297–325 (1995)\
\
06. Daemi, A., Scaduto, C.: Equivariant aspects of singular instanton Floer homology (2019) preprint\
\
07. Donaldson, S.K.: An application of gauge theory to four-dimensional topology. J. Differ. Geom. **18**(2), 279–315 (1983)\
\
    [Article](https://doi.org/10.4310%2Fjdg%2F1214437665) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=710056) [MATH](http://www.emis.de/MATH-item?0507.57010) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=An%20application%20of%20gauge%20theory%20to%20four-dimensional%20topology&journal=J.%20Differ.%20Geom.&doi=10.4310%2Fjdg%2F1214437665&volume=18&issue=2&pages=279-315&publication_year=1983&author=Donaldson%2CSK)\
\
08. Duff, G.F.D.: Differential forms in manifolds with boundary. Ann. Math. **2**(56), 115–127 (1952)\
\
    [Article](https://doi.org/10.2307%2F1969770) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=48136) [MATH](http://www.emis.de/MATH-item?0049.18804) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Differential%20forms%20in%20manifolds%20with%20boundary&journal=Ann.%20Math.&doi=10.2307%2F1969770&volume=2&issue=56&pages=115-127&publication_year=1952&author=Duff%2CGFD)\
\
09. Floer, A.: Morse theory for fixed points of symplectic diffeomorphisms. Bull. Am. Math. Soc. (N.S.) **16**(2), 279–281 (1987)\
\
10. Floer, A.: Morse theory for Lagrangian intersections. J. Differ. Geom. **28**(3), 513–547 (1988)\
\
    [Article](https://doi.org/10.4310%2Fjdg%2F1214442477) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=965228) [MATH](http://www.emis.de/MATH-item?0674.57027) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Morse%20theory%20for%20Lagrangian%20intersections&journal=J.%20Differ.%20Geom.&doi=10.4310%2Fjdg%2F1214442477&volume=28&issue=3&pages=513-547&publication_year=1988&author=Floer%2CA)\
\
11. Gilkey, P.B.: Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem. Studies in Advanced Mathematics, 2nd edn. CRC Press, Boca Raton (1995)\
\
12. Khandhawit, T.: A new gauge slice for the relative Bauer-Furuta invariants. Geom. Topol. **19**(3), 1631–1655 (2015)\
\
    [Article](https://doi.org/10.2140%2Fgt.2015.19.1631) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3352245) [MATH](http://www.emis.de/MATH-item?1316.57022) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20new%20gauge%20slice%20for%20the%20relative%20Bauer-Furuta%20invariants&journal=Geom.%20Topol.&doi=10.2140%2Fgt.2015.19.1631&volume=19&issue=3&pages=1631-1655&publication_year=2015&author=Khandhawit%2CT)\
\
13. Khandhawit, T., Lin, J., Sasahira, H.: Unfolded Seiberg-Witten Floer spectra, I: definition and invariance. Geom. Topol. **22**(4), 2027–2114 (2018)\
\
    [Article](https://doi.org/10.2140%2Fgt.2018.22.2027) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3784516) [MATH](http://www.emis.de/MATH-item?1395.57040) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Unfolded%20Seiberg-Witten%20Floer%20spectra%2C%20I%3A%20definition%20and%20invariance&journal=Geom.%20Topol.&doi=10.2140%2Fgt.2018.22.2027&volume=22&issue=4&pages=2027-2114&publication_year=2018&author=Khandhawit%2CT&author=Lin%2CJ&author=Sasahira%2CH)\
\
14. Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)\
\
15. Kronheimer, P.B., Mrowka, T.S.: Monopoles and contact structures. Invent. Math. **130**(2), 209–255 (1997)\
\
    [Article](https://link.springer.com/article/10.1007/s002220050183) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1474156) [MATH](http://www.emis.de/MATH-item?0892.53015) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Monopoles%20and%20contact%20structures&journal=Invent.%20Math.&doi=10.1007%2Fs002220050183&volume=130&issue=2&pages=209-255&publication_year=1997&author=Kronheimer%2CPB&author=Mrowka%2CTS)\
\
16. Kronheimer, P.B., Mrowka, T.S.: Khovanov homology is an unknot-detector. Publ. Math. Inst. Hautes Études Sci. **113**, 97–208 (2011)\
\
    [Article](https://link.springer.com/article/10.1007/s10240-010-0030-y) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=2805599) [MATH](http://www.emis.de/MATH-item?1241.57017) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Khovanov%20homology%20is%20an%20unknot-detector&journal=Publ.%20Math.%20Inst.%20Hautes%20%C3%89tudes%20Sci.&doi=10.1007%2Fs10240-010-0030-y&volume=113&pages=97-208&publication_year=2011&author=Kronheimer%2CPB&author=Mrowka%2CTS)\
\
17. Lang, S.: Real and Functional Analysis. Graduate Texts in Mathematics, vol. 142, 3rd edn. Springer-Verlag, New York (1993)\
\
18. Lang, S.: Real and Functional Analysis. Graduate Texts in Mathematics, vol. 142, 3rd edn. Springer-Verlag, New York (1993)\
\
19. Lin, F.: A Morse–Bott approach to monopole Floer homology and the triangulation conjecture. Mem. Am. Math. Soc. **255**(1221), v+162 (2018)\
\
20. Lin, J.: Pin(2)-equivariant KO-theory and intersection forms of spin 4-manifolds. Algebr. Geom. Topol. **15**(2), 863–902 (2015)\
\
    [Article](https://doi.org/10.2140%2Fagt.2015.15.863) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3342679) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Pin%282%29-equivariant%20KO-theory%20and%20intersection%20forms%20of%20spin%204-manifolds&journal=Algebr.%20Geom.%20Topol.&doi=10.2140%2Fagt.2015.15.863&volume=15&issue=2&pages=863-902&publication_year=2015&author=Lin%2CJ)\
\
21. Lipyanskiy, M.: A semi-infinite cycle construction of Floer homology (2008). Thesis (Ph.D.)—Massachusetts Institute of Technology\
\
22. Mandache, N.: Some remarks concerning unique continuation for the Dirac operator. Lett. Math. Phys. **31**(2), 85–92 (1994)\
\
    [Article](https://link.springer.com/article/10.1007/BF00750142) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1280386) [MATH](http://www.emis.de/MATH-item?0817.47041) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Some%20remarks%20concerning%20unique%20continuation%20for%20the%20Dirac%20operator&journal=Lett.%20Math.%20Phys.&doi=10.1007%2FBF00750142&volume=31&issue=2&pages=85-92&publication_year=1994&author=Mandache%2CN)\
\
23. Manolescu, C.: Seiberg–Witten–Floer stable homotopy type of three-manifolds with b\_1=0. Geom. Topol. **7**, 889–932 (2003). Erratum available at [arXiv:math/0104024](http://arxiv.org/abs/math/0104024)\
\
24. Manolescu, C.: The Conley index, gauge theory, and triangulations. J. Fixed Point Theory Appl. **13**(2), 431–457 (2013)\
\
    [Article](https://link.springer.com/article/10.1007/s11784-013-0134-3) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3122335) [MATH](http://www.emis.de/MATH-item?1282.57001) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=The%20Conley%20index%2C%20gauge%20theory%2C%20and%20triangulations&journal=J.%20Fixed%20Point%20Theory%20Appl.&doi=10.1007%2Fs11784-013-0134-3&volume=13&issue=2&pages=431-457&publication_year=2013&author=Manolescu%2CC)\
\
25. Manolescu, C.: On the intersection forms of spin four-manifolds with boundary. Math. Ann. **359**(3–4), 695–728 (2014)\
\
    [Article](https://link.springer.com/article/10.1007/s00208-014-1010-1) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=3231012) [MATH](http://www.emis.de/MATH-item?1305.57050) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=On%20the%20intersection%20forms%20of%20spin%20four-manifolds%20with%20boundary&journal=Math.%20Ann.&doi=10.1007%2Fs00208-014-1010-1&volume=359&issue=3%E2%80%934&pages=695-728&publication_year=2014&author=Manolescu%2CC)\
\
26. Miller, S.M.: Equivariant Instanton Homology, 2019. Thesis (Ph.D.)—University of California, Los Angeles\
\
27. Palais, R.S.: Foundations of global non-linear analysis. W. A. Benjamin Inc, New York-Amsterdam (1968)\
\
    [MATH](http://www.emis.de/MATH-item?0164.11102) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Foundations%20of%20global%20non-linear%20analysis&publication_year=1968&author=Palais%2CRS)\
\
28. Schwarz, G.: Hodge Decomposition-A Method for Solving Boundary Value Problems. Lecture Notes in Mathematics, vol. 1607. Springer-Verlag, Berlin (1995)\
\
29. Schwarz, M.: Morse Homology. Progress in Mathematics, vol. 111. Birkhäuser Verlag, Basel (1993)\
\
30. Shubin, M.A.: Spectral theory of elliptic operators on noncompact manifolds. Astérisque **207** 5, 35–108 (1992). Méthodes semi-classiques, vol. 1 (Nantes, 1991)\
\
31. Suwara, P.: Semi-infinite Homology of Floer spaces (2020). Thesis (Ph.D.)—Massachusetts Institute of Technology\
\
32. Witten, E.: Supersymmetry and Morse theory. J. Differ. Geom. **17**(4), 661–692 (1982)\
\
    [Article](https://doi.org/10.4310%2Fjdg%2F1214437492) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=683171) [MATH](http://www.emis.de/MATH-item?0499.53056) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=Supersymmetry%20and%20Morse%20theory&journal=J.%20Differ.%20Geom.&doi=10.4310%2Fjdg%2F1214437492&volume=17&issue=4&pages=661-692&publication_year=1982&author=Witten%2CE)\
\
33. Wolff, T.H.: A property of measures in { R}^N and an application to unique continuation. Geom. Funct. Anal. **2**(2), 225–284 (1992)\
\
    [Article](https://link.springer.com/article/10.1007/BF01896975) [MathSciNet](http://www.ams.org/mathscinet-getitem?mr=1159832) [MATH](http://www.emis.de/MATH-item?0780.35015) [Google Scholar](http://scholar.google.com/scholar_lookup?&title=A%20property%20of%20measures%20in%20%24%24%7B%20R%7D%5EN%24%24%20R%20N%20and%20an%20application%20to%20unique%20continuation&journal=Geom.%20Funct.%20Anal.&doi=10.1007%2FBF01896975&volume=2&issue=2&pages=225-284&publication_year=1992&author=Wolff%2CTH)\
\
\
[Download references](https://citation-needed.springer.com/v2/references/10.1007/s00029-023-00845-y?format=refman&flavour=references)\
\
## Acknowledgements\
\
I would like to express gratitude to my graduate advisor Tom Mrowka for his encouragement, support and sharing many insights on geometry, topology and analysis. I would like to thank Maciej Borodzik and Michał Miśkiewicz for helpful comments on a draft of this paper, an anonymous referee for pointing out an innacuracy in the statement of Regularity Theorem and another referee for many valuable comments and recommendations. Most results of this paper have been part of the author’s Ph.D. thesis \[ [31](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR31 "Suwara, P.: Semi-infinite Homology of Floer spaces (2020). Thesis (Ph.D.)—Massachusetts Institute of Technology")\], although the proofs have been revised and some results have been generalized. In particular, \[ [31](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR31 "Suwara, P.: Semi-infinite Homology of Floer spaces (2020). Thesis (Ph.D.)—Massachusetts Institute of Technology")\] does not consider 4-manifolds with more than two boundary components, or the general split Coulomb slice on them.\
\
## Author information\
\
### Authors and Affiliations\
\
1. Institute of Mathematics, Polish Academy of Sciences, ul. Śniadeckich 8, 00-656, Warsaw, Poland\
\
Piotr Suwara\
\
\
Authors\
\