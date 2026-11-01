---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Bianchi IX self-dual Einstein metrics and singular G2 manifolds]

(w 1, w 2, w 3) = (ρ 2 cos ψ cos χ, ρ 2 sin ψ cos χ, ρ 2 sin χ), (B.3) with 0  ρ < ∞, 0  ψ < 2π, 0  χ < π

> 2

. Note the range of χ. One checks that 

x2 + y2 = ρ2 = √(w 1)2 + (w 2)2 + (w 3)2. (B.4) To fix the SO (3) freedom we introduce an orthonormal moving frame (u1, u2, u3) related to a fixed orthonormal frame (e1, e2, e3) by a rotation with standard Euler angles and left-invariant 1-forms (σ 1, σ 2, σ 3) say. Now if 

x = ρ cos ψ

2 cos χ

2 u1 − ρ sin ψ

2 sin χ

2 u2, (B.5) and 

y = ρ sin ψ

2 cos χ

2 u1 + ρ cos ψ

2 sin χ

2 u2, (B.6) Iwai finds that the flat metric on E6 is given by ds2 = dρ2 + 14 ρ2(dχ 2 + cos 2 χdψ 2) + ρ2 sin 2 χ

2 σ 21+ ρ2 cos 2 χ

2 σ 22 + ρ2

(

σ3 − 12 sin χdψ

)2

. (B.7) If we set ψ = 12 π and ρ2 = 2, the vectors x and y have unit magnitudes, and thus parametrize points on S2 × S2, embedded in R3 × R3. The result is the metric (A.6) on 

S2 × S2, obtained in [39]. If instead we set ρ = 1 we obtain the unit S5. The angle ψ is a coordinate along the Hopf fibres. Projecting orthogonally to the Hopf fibres, we obtain the triaxial form (A.5) of the Fubini–Study metric on CP 2 obtained in [38]. We note en passant that we could consider the seven-dimensional flat metric on E6,1as a trivial solution of supergravity, and perform a Scherk–Schwarz reduction on the orbits of SO (3). We get in four dimensions a global monopole coupled to an SO (3) gauge field 

Ai, i = 1, 2, 3, with the Higgs field in the symmetric tensor (i.e. the 5) representation of 11 Note that the triaxial form of the standard round metric on S4 can also be obtained from the flat metric on E6, but now the action of SO (3) is different. In this case, one identifies E6 with the space of real symmetric 3 × 3 matrices on which SO (3) acts by conjugation [32]. 4266 M Cvetiˇ c et al SO (3). The gauge connection coincides with the Guichardet connection, and in the present case the only non-zero gauge field is 

A3 = − 12 sin χdψ. (B.8) Ignoring the Weyl rescaling, the interpretation is as follows. One should think of ψ as an azimuthal angle, i.e. a longitude, while χ is to be thought of as a latitude. Because χ ∈ [0 , π 

> 2

),there is a deficit solid angle, and hence a conical singularity at the origin. Moreover, the metric is not asymptotically flat. We have an embedding of an Abelian monopole into the non-Abelian gauge group SO (3). This monopole may be thought of as sitting at the centre of a global monopole supported by a Higgs field. 

Appendix C. Killing spinors 

Since the seven-dimensional metric constructed from the anti-self-dual Einstein 4-metric according to (12) has G2 holonomy, it follows that it admits a covariantly constant spinor. It is instructive to look at how this is related to spinors in the four-dimensional base space. To do this, we begin by calculating the Lorentz-covariant exterior derivative on spinors in seven dimensions in terms of quantities in the four-dimensional base metric. We adopt a notation where quantities in seven dimensions carry hats, and so we write (12) as dˆ s27 = ρ−1(Dui) 2 + 2 ρds24 , for which we choose the natural vielbein basis ˆ ei = ρ−1/2Dui ,ˆea = √2ρe a. The spinor-covariant exterior derivative is given by ˆ ∇ ≡ d + 14 ˆωAB ˆ AB , and after some calculation we find that this is given by ˆ∇ = d + 14 ωab ˆ ab − 14 ij kA k ˆ ij + 116 ρ−3/2uj (ij kJ kab ˆ ab − 4 ˆ ij )ˆei

+ 18 ρ−3/2ui (ij kJ jab ˆ kb − 2 ˆ ia )ˆea. (C.1) The covariantly constant spinor ˆ η in the seven-dimensional G2 metric satisfies ˆ∇ ˆη = 0. It can be seen from (C.1) that this spinor is annihilated by the terms involving the R3 coordinates 

ui , and that it is independent of ui . In fact in this basis we find that ˆ η is the spinor that is determined, up to overall ui -independent scale, by the conditions ˆ ij ˆη = 14 ij kJ kab ˆ ab ˆη. (C.2) It then follows from (C.1) that ˆ η satisfies 

(d + 14 ωab ˆ ab − 14 ij kA k ˆ ij ) ˆη = 0. (C.3) Decomposing spinors into the tensor product of spinors in the four-dimensional base and the R3 fibres, we choose Dirac matrices ˆ a = a ⊗ 1l and ˆ i = 5 ⊗ τi . The Pauli matrices 

τi can be viewed as the generators of an internal SU ( 2) isospin, and so (C.2) and (C.3) can be written as 

J iab ab ηα = 4i (τi) α βη β, ∇ηα − i4 Ai(τi) α βη β = 0. (C.4) The second equation is the condition for the 4-component spinor ηα with its isospin doublet index α to be gauge covariantly constant with respect to the SU ( 2) Yang–Mills covariant derivative. Using (C.2) we can rewrite (C.3) as the four-dimensional equation dηα + 14

(ωab − 12 AiJab ) ab ηα = 0. (C.5) With the Yang–Mills connection taken to be the self-dual part of the four-dimensional spin connection as in (25), we therefore find that (C.5) is nothing but dηα + 14 ω− 

> ab ab

ηα = 0, (C.6) Bianchi IX self-dual Einstein metrics and singular G2 manifolds 4267 where ω− 

> ab

≡ 12

(ωab − 12 abcd ω cd ) is the anti-self-dual part of the spin connection. In fact it follows from the conditions (C.2) satisfied by ˆ η that ˆ ab ˆη is self-dual in the four-dimensional base space, and hence (C.6) reduces simply to d ηα = 0. It is interesting to note that in the special case of CP 2, which does not admit an ordinary spin structure, ηα is a generalized spinor (in the terminology of [42]) that is charged with respect to the Yang–Mills connection Ai. In this case the connection is actually SO (3)-valued, as opposed to SU ( 2)-valued, and it is this that serves to compensate for the minus sign that ordinary spinors would acquire upon parallel propagation around a family of curves spanning the bolt in CP 2 [42]. 

References 

[1] Bryant R L and Salamon S 1989 On the construction of some complete metrics with exceptional holonomy 

Duke Math. J. 58 829 [2] Gibbons G W, Page D N and Pope C N 1990 Einstein metrics on S3, R3 and R4 bundles Commun. Math. Phys. 

127 529 [3] Besse A L 1987 Einstein Manifolds (Berlin: Springer) [4] Cvetiˇ c M, Shiu G and Uranga A M 2001 Three-family supersymmetric standard like models from intersecting brane worlds Phys. Rev. Lett. B 87 201801 ( Preprint hep-th /0107143) Cvetiˇ c M, Shiu G and Uranga A M 2001 Chiral four-dimensional N = 1 supersymmetric type IIA orientifolds from intersecting D6-branes Nucl. Phys. 615 3–32 ( Preprint hep-th /0107166) [5] Atiyah M F and Witten E 2001 M-theory dynamics on a manifold of G2 holonomy Preprint hep-th /0107177 [6] Witten E 2001 Anomaly cancellation on G2 manifold Preprint hep-th /0108165 [7] Acharya B and Witten E 2001 Chiral fermions from manifolds of G2 holonomy Preprint hep-th /0109152 [8] Cvetiˇ c M, Shiu G and Uranga A M 2001 Chiral type II orientifold constructions as M-theory on G2 holonomy spaces Preprint hep-th /0111179 [9] Roiban R, Romelsberger C and Walcher J 2002 Discrete torsion in singular G2-manifolds and real LG Preprint 

hep-th /0203272 [10] Behrndt K 2002 Singular 7-manifolds with G2 holonomy and intersecting 6-branes Preprint hep-th /0204061 [11] Anguelova L and Lazaroiu C I 2002 M-theory compactifications on certain ‘toric’ cones of G2 holonomy 

Preprint hep-th /0204249 Anguelova L and Lazaroiu C I 2002 M-theory on ’toric’ G2 cones and its type II reduction Preprint 

hep-th /0205070 [12] Berglund P and Brandhuber A 2002 Matter from G2 manifolds Preprint hep-th /0205184 [13] Cvetiˇ c M, Gibbons G W, L¨ u H and Pope C N 2002 Supersymmetric M3-branes and G2 manifolds Nucl. Phys. 

B 620 3 ( Preprint hep-th/0106026) [14] Brandhuber A, Gomis J, Gubser S S and Gukov S 2001 Gauge theory at large N and new G2 holonomy metrics 

Preprint hep-th /0106034 [15] Cvetiˇ c M, Gibbons G W, L¨ u H and Pope C N 2002 M-theory conifolds Phys. Rev. Lett. 8 121602 ( Preprint 

hep-th /0112098) [16] Brandhuber A 2002 G2 holonomy spaces from invariant three-forms Nucl. Phys. B 629 393 ( Preprint hep-th /0112113) [17] Cvetiˇ c M, Gibbons G W, L¨ u H and Pope C N 2002 A G2 unification of the deformed and resolved conifolds 

Phys. Lett. B 534 172–80 ( Preprint hep-th /0112138) [18] Gukov S, Yau S T and Zaslow E 2002 Duality and fibrations on G2 manifolds Preprint hep-th /0203217 [19] Chong Z W, Cvetiˇ c M, Gibbons G W, L¨ u H, Pope C N and Wagner P 2002 General metrics of G2 holonomy and contraction limits Preprint hep-th /0204064 [20] Tod K P 1995 Cohomogeneity-one metrics with self-dual Weyl tensor Twistor Theory ed S Huggett (New York: Dekker) [21] Tod K P 1994 Self-dual Einstein metrics from the Painlev´ e VI equation Phys. Lett. A 190 221 [22] Hitchin N J 1996 A new family of Einstein metrics Manifolds and Geometry ed P de Bartolomeis, F Tricerri and E Vesentini (Cambridge: Cambridge University Press) [23] Hitchin N J 1995 Twistor spaces, Einstein metrics and isomonodromic deformations J. Diff. Geom. 42 30 [24] Yano K 1972 Some remarks on tensor fields and curvature Ann. Math. 55 328 [25] Gibbons G W, Rietdijk R H and van Holten J W 1993 SUSY in the sky Nucl. Phys. B 404 42 4268 M Cvetiˇ c et al 

[26] de Azcarraga J A, Izquierdo J M and Macfarlane A J 2001 Hidden supersymmetries in supersymmetric quantum mechanics Nucl. Phys. B 604 75 ( Preprint hep-th /0101053) [27] Atiyah M F and Hitchin N J 1985 Low-energy scattering of non-Abelian monopoles Phys. Lett. A 107 21 [28] Belinsky V A, Gibbons G W, Page D N and Pope C N 1978 Asymptotically Euclidean Bianchi IX metrics in quantum gravity Phys. Lett. B 76 433 [29] Hawking S W 1977 Gravitational instantons Phys. Lett. A 60 81 [30] Eguchi T and Hanson A J 1978 Asymptotically flat selfdual solutions to Euclidean gravity Phys. Lett. B 74 249 [31] Gibbons G W and Pope C N 1979 The positive action conjecture and asymptotically Euclidean metrics in quantum gravity Commun. Math. Phys. 66 267 [32] Giulini D 1995 A Euclidean Bianchi model based on S3/D ∗ 

> 8

J. Geom. Phys. 20 149 ( Preprint gr-qc /9508040) [33] Gibbons G W and Manton N S 1986 Classical and quantum dynamics of BPS monopoles Nucl. Phys. B 274 

183 [34] Cvetiˇ c M, Gibbons G W, L¨ u H and Pope C N 2001 Orientifolds and slumps in G2 and Spin (7) metrics Preprint 

hep-th /0111096 [35] Gibbons G W and Pope C N 1978 CP 2 as a gravitational instanton Commun. Math. Phys. 61 239 [36] Pedersen H 1985 Eguchi–Hanson metrics with cosmological constant Class. Quantum Grav. 2 579 [37] Dancer A S and Strachan I A B 1994 K¨ ahler–Einstein metrics with SU ( 2) action Math. Proc. Camb. Phil. Soc. 

115 513 [38] Bouchiat C and Gibbons G W 1988 Non-integrable quantum phase in the evolution of a spin-system: a physical consequence of the non-trivial topology of the quantum state-space J. Phys. France 49 187 [39] Pope C N 1979 PhD Thesis Cambridge University [40] Iwai T 1987 J. Math. Phys. 28 1315 [41] Hartnoll S A 2001 Axisymmetric non-Abelian BPS monopoles from G2 metrics Preprint hep-th /0102235 [42] Hawking S W and Pope C N 1978 Generalized spin structures in quantum gravity Phys. Lett. B 73 42 [43] Adams A, Polchinski J and Silverstein E 2001 Don’t panic! Closed string tachyons in ALE space-times J. High Energy Phys. JHEP10(2001)029 ( Preprint hep-th /0108075)
