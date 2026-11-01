---
retention_scope: session
part: 4
total_parts: 4
---

[Part 4/4 of: Low-regularity Seiberg–Witten moduli spaces on manifolds with boundary]

1. Piotr Suwara\
\
\
[View author publications](https://link.springer.com/search?sortBy=newestFirst&contributor=Piotr%20Suwara)\
\
\
\
\
\
Search author on:[PubMed](https://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=search&term=Piotr%20Suwara) [Google Scholar](https://scholar.google.co.uk/scholar?as_q=&num=10&btnG=Search+Scholar&as_epq=&as_oq=&as_eq=&as_occt=any&as_sauthors=%22Piotr%20Suwara%22&as_publication=&as_ylo=&as_yhi=&as_allsubj=all&hl=en)\
\
\
### Corresponding author\
\
Correspondence to\
[Piotr Suwara](mailto:psuwara@impan.pl).\
\
## Additional information\
\
### Publisher's Note\
\
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.\
\
## Appendix\
\
### Appendix\
\
This section presents some standard analytical results which are used repeatedly in the article. We recall the Gårding inequality, Sobolev multiplication and trace theorems and the Implicit Function Theorem.\
\
### Theorem A.1\
\
(Sobolev multiplication theorem) Let _M_ be a manifold with compact boundary and cylindrical ends.\
\
Assume k, l \\ge m and  1/p + 1/q \\ge 1/r for p,q,r \\in (1,\\infty ) . Then the multiplication\
\
\\begin{aligned} L\_k^p(M) \\times L\_l^q(M) \\rightarrow L\_m^r(M) \\end{aligned}\
\
is continuous if any of these hold:\
\
- (k-n/p) + (l-n/q) \\ge m - n/r  and both  k - n/p< 0, l - n/q < 0,\
\
- \\min (k-n/p, l-n/q) \\ge m - n/r  and either  k - n/p > 0  or  l - n/q > 0,\
\
- \\min (k-n/p, l-n/q) > m - n/r and either  k - n/p = 0  or  l - n/q = 0.\
\
\
What is more, whenever it is continuous, it restricts to a compact map on  \\{f\\} \\times L\_l^q(M) \\rightarrow L\_m^r(M)  provided that  l > m  and  l - n/q > m - n/r .\
\
### Proof\
\
We can reduce to the case of a manifold without boundary by considering a double of _M_, or by attaching cylindrical ends along \\partial M.\
\
To obtain continuity, combine \[ [27](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR27 "Palais, R.S.: Foundations of global non-linear analysis. W. A. Benjamin Inc, New York-Amsterdam (1968)"), Theorem 9.6\] for compact manifolds together with \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Theorem 13.2.2\] for an infinite cylinder.\
\
For the compactness statement on a compact manifold, for each sequence g\_i \\xrightarrow {L^q\_l(M)} g take any sequence f\_j \\in C^\\infty (M) such that \\Vert f - f\_j\\Vert \_{L^p\_k(M)} \\le \\frac{1}{2^j}. By continuity of multiplication there is a constant _C_ such that\
\
\\begin{aligned} \\Vert (f-f\_j) g\_i\\Vert \_{L^r\_m(M)} \\le C \\Vert f-f\_j\\Vert \_{L^p\_k(M)} \\le \\frac{C}{2^j}. \\end{aligned}\
\
Set a\_{0,i} = i and define inductively a\_{j,i} in the following manner. Take a\_{j,i} = a\_{j-1,i} whenever i < j. Since f\_j \\in C^\\infty (M), the sequence f\_j g\_i is bounded in L^q\_l(M) and by Sobolev embedding is precompact in L^r\_m(M). Thus, we can choose  (a\_{j,i})\_i  to be a subsequence of  (a\_{j-1,i})\_i  satisfying\
\
\\begin{aligned} \\Vert f\_j g\_{a\_{j,j}} - f\_j g\_{a\_{j,i}}\\Vert \_{L^r\_m(M)} \\le \\frac{1}{2^j} \\end{aligned}\
\
for any i \\ge j. We finally get, for i \\ge 0,\
\
\\begin{aligned} \\Vert f g\_{a\_{j,j} - f g\_{a\_{j+i,j+i}}} \\Vert \_{L^r\_m(M)}&\\le \\Vert (f-f\_{j}) (g\_{a\_{j,j} - g\_{a\_{j+i,j+i}}}) \\Vert \_{L^r\_m(M)}\\\&\\quad + \\Vert f\_{j} (g\_{a\_{j,j} - g\_{a\_{j+i,j+i}}}) \\Vert \_{L^r\_m(M)}\\\&\\le \\frac{2 C}{2^j} + \\frac{1}{2^j} \\end{aligned}\
\
making f g\_{a\_{j,j}} a Cauchy sequence in L^r\_m(M), as wished.\
\
Compactness for a cylinder is proved in \[ [14](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR14 "Kronheimer, P.B., Mrowka, T.S.: Monopoles and Three-Manifolds. New Mathematical Monographs, vol. 10. Cambridge University Press, Cambridge (2007)"), Theorem 13.2.2\]. \\square\
\
### Theorem A.2\
\
(Sobolev trace theorem)\
\
Suppose  N \\subset M is a closed compact n-j-dimensional smooth submanifold,  1 \\le p < \\infty , and  k, l \\ge 0 with  k - j/p \\ge l > 0 . Then the restriction map extends to continuous\
\
\\begin{aligned} L^p\_k(M) \\rightarrow L^p\_l(N). \\end{aligned}\
\
### Proof\
\
See \[ [27](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR27 "Palais, R.S.: Foundations of global non-linear analysis. W. A. Benjamin Inc, New York-Amsterdam (1968)"), Theorem 9.3\]. \\square\
\
We will make use of the Implicit Function Theorem in the following form (cf. \[ [17](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR17 "Lang, S.: Real and Functional Analysis. Graduate Texts in Mathematics, vol. 142, 3rd edn. Springer-Verlag, New York (1993)")\]).\
\
### Implicit Function Theorem\
\
Suppose _A_, _B_ are Hilbert spaces and {\\mathcal {F}}: A \\rightarrow B is a smooth map such that the derivative D\_p {\\mathcal {F}} at _p_ is surjective and that its kernel splits with _C_ as a complementary subspace, A = \\ker \\left( D\_p {\\mathcal {F}} \\right) \\oplus C. Let {\\Pi }: A \\rightarrow \\ker \\left( D\_p {\\mathcal {F}} \\right)  denote the projection onto the kernel along _C_. Then there are open neighborhoods U \\subset A of _p_, V \\subset B of {\\mathcal {F}}(p) and W \\subset \\ker \\left( D\_p {\\mathcal {F}} \\right)  of 0 and a smooth diffeomorphism {\\mathcal {G}}: V \\times W \\rightarrow U such that\
\
\\begin{aligned} V \\times W \\xrightarrow {{\\mathcal {G}}} U \\xrightarrow {({\\mathcal {F}},{\\Pi })} B \\oplus \\ker \\left( D\_p {\\mathcal {F}} \\right) \\end{aligned}\
\
is the identity map (i.e., {\\mathcal {G}} = {\\mathcal {F}}^{-1}).\
\
In particular, the projection\
\
\\begin{aligned} {\\Pi }: {\\mathcal {F}}^{-1}(0) \\cap U \\rightarrow \\ker \\left( D\_p {\\mathcal {F}} \\right) \\end{aligned}\
\
along _C_ is a local diffeomorphism.\
\
We will also utilize the Gårding inequality.\
\
### Theorem A.3\
\
(Gårding inequality) Let _D_ be a first-order elliptic operator with smooth coefficients on a compact manifold _M_ (possibly with boundary) and M' \\subset M be open with compact closure. Then there is a constant _C_ such that for any \\gamma \\in L^p\_{k+1}(M) we have\
\
\\begin{aligned} \\Vert \\gamma \\Vert \_{L^p\_{k+1}(M')} \\le C ( \\Vert D \\gamma \\Vert \_{L^p\_k(M)} + \\Vert \\gamma \\Vert \_{L^p\_k(M)}). \\end{aligned}\
\
### Proof\
\
This follows from \[ [30](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR30 "Shubin, M.A.: Spectral theory of elliptic operators on noncompact manifolds. Astérisque 2075, 35–108 (1992). Méthodes semi-classiques, vol. 1 (Nantes, 1991)"), Appendix 1, Lemma 1.4\] by extending _D_ to the cylindrical-end manifold M^\*= M \\cup (\\partial M) \\times \[0,\\infty ). Indeed, taking a smooth bump function \\rho  such that \\rho \|\_{M'} = 1 and \\rho \|\_{M^\*{\\setminus } M} = 0 we get\
\
\\begin{aligned} \\Vert \\gamma \\Vert \_{L^p\_{k+1}(M')}&\\le \\Vert \\rho \\gamma \\Vert \_{L^p\_{k+1}(M^\*)}\\\&\\le C ( \\Vert D(\\rho \\gamma ) \\Vert \_{L^p\_k(M^\*)} + \\Vert \\rho \\gamma \\Vert \_{L^p\_k(M^\*)}) \\\&\\le C C'\_\\gamma ( \\Vert D(\\gamma ) \\Vert \_{L^p\_k(M)} + \\Vert \\gamma \\Vert \_{L^p\_k(M)}) \\end{aligned}\
\
where the middle inequality follows from \[ [30](https://link.springer.com/article/10.1007/s00029-023-00845-y#ref-CR30 "Shubin, M.A.: Spectral theory of elliptic operators on noncompact manifolds. Astérisque 2075, 35–108 (1992). Méthodes semi-classiques, vol. 1 (Nantes, 1991)")\]. \\square\
\
## Rights and permissions\
\
**Open Access** This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit [http://creativecommons.org/licenses/by/4.0/](http://creativecommons.org/licenses/by/4.0/).\
\
[Reprints and permissions](https://s100.copyright.com/AppDispatchServlet?title=Low-regularity%20Seiberg%E2%80%93Witten%20moduli%20spaces%20on%20manifolds%20with%20boundary&author=Piotr%20Suwara&contentID=10.1007%2Fs00029-023-00845-y&copyright=The%20Author%28s%29&publication=1022-1824&publicationDate=2023-06-08&publisherName=SpringerNature&orderBeanReset=true&oa=CC%20BY)\
\
## About this article\
\
[![Check for updates. Verify currency and authenticity via CrossMark](<Base64-Image-Removed>)](https://crossmark.crossref.org/dialog/?doi=10.1007/s00029-023-00845-y)\
\
### Cite this article\
\
Suwara, P. Low-regularity Seiberg–Witten moduli spaces on manifolds with boundary.\
_Sel. Math. New Ser._ **29**, 47 (2023). https://doi.org/10.1007/s00029-023-00845-y\
\
[Download citation](https://citation-needed.springer.com/v2/references/10.1007/s00029-023-00845-y?format=refman&flavour=citation)\
\
- Accepted: 21 September 2022\
\
- Published: 08 June 2023\
\
- Version of record: 08 June 2023\
\
- DOI: https://doi.org/10.1007/s00029-023-00845-y\
\
\
### Share this article\
\
Anyone you share the following link with will be able to read this content:\
\
Get shareable link\
\
Sorry, a shareable link is not currently available for this article.\
\
Copy shareable link to clipboard\
\
Provided by the Springer Nature SharedIt content-sharing initiative\
\
\
### Keywords\
\
- [Seiberg–Witten equations](https://link.springer.com/search?query=Seiberg%E2%80%93Witten%20equations&facet-discipline=%22Mathematics%22)\
- [Global analysis](https://link.springer.com/search?query=Global%20analysis&facet-discipline=%22Mathematics%22)\
- [Boundary value problem](https://link.springer.com/search?query=Boundary%20value%20problem&facet-discipline=%22Mathematics%22)\
- [Floer homology](https://link.springer.com/search?query=Floer%20homology&facet-discipline=%22Mathematics%22)\
\
### Mathematics Subject Classification\
\
- [Primary 58J32](https://link.springer.com/search?query=Primary%2058J32&facet-discipline=%22Mathematics%22)\
- [Secondary 57K41](https://link.springer.com/search?query=Secondary%2057K41&facet-discipline=%22Mathematics%22)\
- [57R58](https://link.springer.com/search?query=57R58&facet-discipline=%22Mathematics%22)\
\
### Profiles\
\
1. Piotr Suwara [View author profile](https://link.springer.com/researchers/31413310SN)