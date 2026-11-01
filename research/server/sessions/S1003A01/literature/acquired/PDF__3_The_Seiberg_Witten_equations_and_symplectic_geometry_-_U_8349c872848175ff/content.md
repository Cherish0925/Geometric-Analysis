---
retention_scope: session
part: 1
total_parts: 1
---

# [PDF] 3 The Seiberg–Witten equations and symplectic geometry - UT Math

> Source: https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf
> Fetched: 2026-10-09 12:12
> Method: FULLTEXT_HTML_FIRECRAWL|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

---

## Verified object metadata

```json
{
  "object_type": "web",
  "identifier": "",
  "identifiers": {},
  "identifier_aliases": {},
  "version": "",
  "published_at": "",
  "updated_at": "",
  "license": "",
  "language": "",
  "source": "tavily",
  "source_url": "https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf",
  "metadata": {
    "provenance_urls": [
      "https://web.ma.utexas.edu/users/perutz/Northwestern/NorthwesternL3.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Taubes Seiberg-Witten canonical class J-holomorphic curves arbitrary compatible almost complex structure closed symplectic 4-manifold"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

Lectures on gauge theory and symplectic geometry TIM PERUTZ 3 The Seiberg–Witten equations and symplectic geometry 3.1 The SW equations on symplectic 4-manifolds On a symplectic 4-manifold (X, ω), equipped with a compatible almost complex struc-ture J, Spinc-structures correspond to complex line bundles. Given a line bundle L →X, construct a Spinc-structure s as follows. Let S+ = L ⊗(1 ⊕Λ0,2), S−= L ⊗Λ0,1.
If B is a U(1)-connection in L, one has a Cauchy–Riemann operator 1 √ 2 (∂B + ∂ ∗ B): Γ(S+) →Γ(S−).
The symbol ρ of this operator deﬁnes a Clifford multiplication T∗X →Hom(S+, S−), deﬁning the Spinc-structure s. The operator DB = 1 √ 2(∂B + ∂ ∗ B) then becomes the Dirac operator for the Clifford connection induced by B. [...] Translation-invariant SW monopoles on Σ × C are identiﬁed with vortices; slowly-varying vortices correspond to holomorphic maps from C to the vortex moduli space.
On a symplectic 4-manifold, there is just one solution to SW in the canonical Spinc-structure. Solutions to SW (deformed by high multiples of the symplectic form) localize on pseudo-holomorphic curves; the unique solution for the canonical Spinc-structure is the empty curve. Conversely, one can obtain monopoles from pseudo-holomorphic curves by applying the implicit function theorem to approximate solutions which are given, in a tubular neighbourhood of the curve, by holomorphic multisections of a bundle of vortex moduli spaces associated with the normal bundle.

## Retrieved source content

# Lectures on gauge theory and symplectic geometry

## TIM PERUTZ

# 3 The Seiberg–Witten equations and symplectic geometry

## 3.1 The SW equations on symplectic 4-manifolds

On a symplectic 4-manifold (*X,ω*), equipped with a compatible almost complex structure *J*, Spin<sup>c</sup>-structures correspond to complex line bundles. Given a line bundle *L→X*, construct a Spin<sup>c</sup>-structure s as follows. Let

S<sup>+</sup> = *L ⊗* (**1** *⊕* Λ<sup>0,2</sup>)*,* S<sup>−</sup> = *L ⊗* Λ<sup>0,1</sup>*.*

If *B* is a *U*(1)-connection in *L*, one has a Cauchy–Riemann operator

<u>1</u> *∗* <s>√</s> (*∂<sub>B</sub>* + *∂<sub>B</sub>*) : Γ(S<sup>+</sup>) *→* Γ(S<sup>−</sup>)*.* 2

The symbol *ρ* of this operator defines a Clifford multiplication <u>T<sup>∗</sup></u>*X →* Hom(S<sup>+</sup>*,* S<sup>−</sup>), <sup>c</sup> <u>1</u> *∗* defining the Spin-structure s. The operator *DB* =<s>√</s>(*∂<sub>B</sub>* + *∂<sub>B</sub>*) then becomes the 2 Dirac operator for the Clifford connection induced by *B*.

We write positive spinors as *φ* = (*α,β*). We also note that

## Λ<sup>+</sup> ⊗ C=Cω ⊕ Λ<sup>0,2</sup>.

## Following Taubes, we consider the perturbation

## η = τ<sup>1/2</sup>ω.

The equations become *∗*

(1) *∂<sub>B</sub>α* = *−∂<sub>B</sub>β*
(2) *FB⁰²* = *ᾱβ*
(3) *iFB¹¹ · ω* = *|β|<sup>2</sup> −|α|<sup>2</sup>* + *τ<sup>2</sup>.* When *L* is trivial, these equations have a trivial solution: take *B* to be the trivial connection, *β* = 0, and *α ≡ τ*. We will call this the *canonical monopole*.

**2** *Tim Perutz*

**Theorem 3.1** (Taubes) *When L ∼*= **1** *and τ* 0*, the canonical monopole is the only* *one, up to gauge.*

The proof is a deft integration by parts invoking the Weitzenböck formula for *∂<sub>B</sub>*.

(3.1) Taubes’s result about the canonical monopole is from [Tau]; it is explained clearly in [Don2].

**3.2** Σ *×* C Let’s specialize to Σ *×* R², taking *L*, the metric, and the symplectic form *ω* to be pulled back from Σ. Then¶
S<sup>+</sup> *∼* = Λ<sup>0,∗</sup>(Σ*, L*) *∼* = S<sup>−</sup>*.*

If we take (*B,α,β*) also to be pullbacks from Σ, the equations read *∗*

(4) *∂<sub>B</sub>α* = *−∂<sub>B</sub>β* 0(5) *ᾱβ* =
(6) *iFB* = (*|β|<sup>2</sup> −|α|<sup>2</sup>* + *τ*)*ω.*
∫ Either *β* = 0 or *α* = 0; the former implies that 2*πd ≥ <sub>Σ</sub> τα*, the latter the reverse

(*≤*) inequality. If *β* = 0 we obtain the *τ*-vortex equations in *L*. If *α* = 0, we get what are essentially the (2*g −* 2 *− τ*)-vortex equations in the Serre-dual line bundle *K<sub>Σ</sub> ⊗ L<sup>∗</sup>*. **Remark** Suppose one considers monopoles on Σ *×* C which vary slowly in the C- coordinate (an ‘adiabatic limit’). These are well approximated as holomorphic maps C *→ Vor*(Σ*, L*).
## 3.3 Monopoles localize on holomorphic curves

Suppose that (*A<sub>n</sub>,α<sub>n</sub>,β<sub>n</sub>*) is sequence of *r<sub>n</sub>ω*-monopoles, where *r<sub>n</sub> →∞*. The zero set *α<sub>n−</sub><sup>1</sup>*(0) is a surface in *X*, Poincaré dual to *c₁*(*L*).

A deep analysis, due to Taubes, shows that, after passing to a subsequence,

- *α<sub>n−</sub><sup>1</sup>*(0) converges (as a point set) to a *J*-holomorphic curve *C*.
- ** Everything localizes along *C*. For instance, *FA<sub>n</sub>* converges (as a current) to the Dirac-delta-current along *C*.
- *|β<sub>n</sub>|* and *τ −|α<sub>n</sub>|* are bounded by *c₁e<sup>−c</sup>*2<sup>dist(x,C)/τ</sup>.

*Lectures on gauge theory and symplectic geometry* **3**

## Monopoles from holomorphic curves

If we are given an embedded holomorphic curve *C⊂X*, we can construct approximate monopoles, supported in a tubular neighborhood of near *C*. We take a holomorphic section of Sym<sup>d</sup>(*NC*), convert it to a family of vortices on the normal planes of *C*, and cut off using a bump function.

Taubes proves using the implicit function theorem that these approximate monopoles are close to true monopoles.

## 3.4 Summary

Solutions to the vortex equations in a line bundle *L →* Σ, modulo gauge, form a complex manifold which is identified with Sym<sup>deg(L)</sup>(Σ) by the map [*A,φ*] *7→ φ<sup>−1</sup>*(0). Translation-invariant SW monopoles on Σ *×* C are identified with vortices; slowly- varying vortices correspond to holomorphic maps from C to the vortex moduli space. On a symplectic 4-manifold, there is just one solution to SW in the canonical Spin<sup>c</sup>- structure. Solutions to SW (deformed by high multiples of the symplectic form) localize on pseudo-holomorphic curves; the unique solution for the canonical Spin<sup>c</sup>-structure is the empty curve. Conversely, one can obtain monopoles from pseudo-holomorphic curves by applying the implicit function theorem to approximate solutions which are given, in a tubular neighbourhood of the curve, by holomorphic multisections of a bundle of vortex moduli spaces associated with the normal bundle.

## 3.5 Monopole invariants for closed 4-manifolds

**The configuration space.** Let (*X,* s) be a closed 4-manifold with a Spin<sup>c</sup>-structure. One has a space C(*X,* s) of *SW configurations* (*A,φ*): here *A* is a Clifford connection in S<sup>+</sup>, and *φ ∈* Γ(S<sup>+</sup>) is a positive spinor. The gauge group G = *C* *∞* (*X, U*(1)) acts on C = C(*X,* s) with quotient B. The stabilizer of (*A,φ*) is *U*(1) if *φ* = 0 (in which case (*A,φ*) is called *reducible*) and is trivial otherwise (call (*A,φ*) *irreducible*). We write C<sup>∗</sup> for the irreducible connections, and B<sup>∗</sup> for the free quotient C<sup>∗</sup>*/*G. For any *x ∈ X*, the ‘based gauge group’, G<sub>x</sub> *⊂* G, the subgroup of maps *X→U*(1) sending *x* to 1, acts freely on C, and C*/*G<sub>x</sub> has a residual action of *U*(1).

**Proposition 3.2** *Assume b₁*(*X*)=0*. Then there is an S¹-equivariant deformation* *retraction* C<sup>∗</sup>*/*G<sub>x</sub> *→{*0*}× S*(H) *to the unit sphere in* H = Γ(S<sup>+</sup>)*. Hence* B<sup>∗</sup> *’* P(H)*.* *One has H<sup>∗</sup>*(B<sup>∗</sup>) *∼* = Z[*U*]*; the generator U ∈ H² is the class c₁*(L<sub>x</sub>)*, where* L<sub>x</sub> *→* C<sup>∗</sup> *is the S¹-bundle* C<sup>∗</sup>*/*G<sub>x</sub> *→* B<sup>∗</sup>*.*

**4** *Tim Perutz*

**Proof** Let *A₀* be a reference connection in Λ²S. An arbitrary connection is then *A* = *A₀* + *ia*, where *a ∈* Ω¹<sub>X</sub>. By the Hodge theorem, Ω¹<sub>X</sub> = im*d ⊕* im*d<sup>∗</sup>*. Since *H¹*(*X*) = 0, the group of gauge transformations is path connected, and every gauge transformation *u* has a logarithm: *u* = exp(*iξ*). The gauge action on connections is *u · A* = *A −* 2*u<sup>−1</sup>du* = *A − idξ*. Hence, for every connection *A* there is a unique based gauge transformation *u<sub>A</sub> ∈* G<sub>x</sub> such that *u<sub>A</sub> ·A∈A₀* + *i*im*d<sup>∗</sup>*. Thus C<sup>∗</sup>*/*G<sub>x</sub> is equivariantly homeomorphic to im*d<sup>∗</sup> ×*(H*\{*0*}*) with the *S¹*-action *t ·*(*a,φ*)=(*a, tφ*). From this the result is easy.

**The moduli space.** The monopole moduli space M(*g,η*) = M(*X,* s; *g,η*) *⊂* B depends on the Riemannian metric and the closed 2-form *η*.

**Proposition 3.3** *If b<sup>+</sup>*(*X*) *>* 0 *then for generic pairs* (*g,η*) *of metric and closed* *2-form, one has* M(*g,η*) *⊂* B<sup>∗</sup>*. If b<sup>+</sup>*(*X*) *>* 1 *then this holds for generic 1-parameter* *families of metrics.*

**Proof** M(*g,η*) intersects the locus of reducible pairs [*A,φ*]=[*A,*0] where (*iFA −* *η*)<sup>+</sup> = 0. But *iFA − η* represents the class 2*πc₁*(S<sup>+</sup>) *−* [*η*], and so [*iFA − η*]<sup>+</sup> *∈* *H²*(*X*)=H²<sub>g</sub>(*X*) represents the component of [*iFA − η*] in the SD subspace H<sub>g</sub><sup>+</sup>. The monopole equation says that [*iFA − η*] *∈* H<sub>g−</sub>.

The map from *{metrics}* to the Grassmannian of *Gr<sub>b</sub>−<sub>(X)</sub>H²*(*X*), *g 7→* H<sub>g−</sub>, can be shown to be a submersion. Hence, if *b<sup>+</sup> >* 0, the locus of metrics *g* such that H<sub>g−</sub> includes 2*πc₁*(S<sup>+</sup>) is a codimension 1 submanifold.

**Theorem 3.4** (1) *The space* M(*η*) *is compact.*

(2) *Generic pairs* (*g,η*) *are* regular *in the sense that* M(*g,η*) *⊂* B<sup>∗</sup> *with* M(*η*) *cut* *out transversely by its defining equations. In this case,* M(*g,η*) *has the structure* *of a smooth manifold of dimension*
<sup>+</sup> <sup>∗</sup> <sup>+</sup> <u>1</u> *d*(s) = ind<sub>R</sub>(*d* + *d*) + ind<sub>R</sub> *DA* = (1 *− b₁* + *b*) + (*c₁*(S)²[*X*] *− σ*)*.* 4

(3) *A ‘homology orientation’—an orientation for* H<sub>g</sub><sup>+</sup> *⊕ H¹*(*X*; R)*—induces an* *orientation for* M(*g,η*)*.*
Clause (2) is typical of elliptic problems. The index formula uses Hodge theory and the index theorem. (3) is not unusual. The compactness clause (1) is the Seiberg–Witten miracle. It depends critically on the special shape of the equations—for instance, on the sign of the 0th-order quadratic term (*φ<sup>∗</sup> ⊗ φ*)₀.

*Lectures on gauge theory and symplectic geometry* **5**

**Definition 3.5** Assume *b<sup>+</sup>*(*X*) *>* 1, and take (*g,η*) generic in the sense of the theorem. Define the Seiberg–Witten invariant

*SW*(*X,* s) *∈ H<sub>d(s)</sub>*(B<sup>∗</sup>)*, SW*(*X,* s) = [M(*g,η*)]*.*

Note that *H<sub>d(s)</sub>*(B<sup>∗</sup>)=Z if *d*(s) is even, and *H<sub>d(s)</sub>*(B<sup>∗</sup>) = 0 otherwise.

**Corollary 3.6** *When b<sup>+</sup> >* 1*, SW*(*X,* s) *is an invariant of X (except that its sign* *depends on a homology orientation).*

# References

[Don2] S. K. Donaldson, *The Seiberg–Witten equations and 4-manifold topology*, Bull. Amer. Math. Soc. (N.S.) 33 (1996), no. 1, 45–70. [Tau] C. H. Taubes, *More constraints on symplectic forms from Seiberg–Witten invariants*, Math. Res. Lett. 2 (1995), no. 1, 9–13.
