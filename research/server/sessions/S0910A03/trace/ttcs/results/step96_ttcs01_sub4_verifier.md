# TTCS Independent Branch Record

```json
{
  "step_id": 96,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step96_koiso_einstein_cauchy_evolution.py",
    "Sessions/S0910A03/workspace/scripts/step96_initial_taylor_invariants.py",
    "Sessions/S0910A03/workspace/scripts/step96_relative_KX_diagnostic.py",
    "Sessions/S0910A03/workspace/data/step96_initial_taylor_invariants.json",
    "Sessions/S0910A03/workspace/data/step96_koiso_einstein_cauchy_evolution_N96_short.json",
    "Sessions/S0910A03/workspace/data/step96_relative_KX_diagnostic.json",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step95_KX_and_bochner_cancellation.md"
  ]
}
```

## Task

Read the Step 96 charged-Koiso Einstein Cauchy evolution and relative K_X experiment as a differential geometer/numerical analyst. Check (i) the Gaussian evolution equations and sign conventions; (ii) whether the extraction of quotient variables a, rho, connection, charge, Q and K_X is invariantly correct; (iii) whether the initial Taylor conclusions H_n=2, sigma_nn=6+Q, a_nn=-(4+Q) (as the data suggest), and coordinate-charge conservation follow analytically; (iv) whether the short-resolution results at n=0.02 genuinely support a local exact continuation or are numerical artifacts; (v) whether the R_X numerator cancellation is an independent validation of the Noether pairing or merely an integration identity; and (vi) what exact finite-dimensional/joint-matching object should be constructed next from this center, without reverting to radial flat-slice models or assuming a bounded transition. Identify any errors precisely and derive corrected formulas where possible.

## Output

# Verifier Memo — Step 96 charged-Koiso Einstein Cauchy germ and the R_X pairing

Session S0910A03. I read the two scripts, the three data files, and notes step94/step95 as a differential geometer and numerical analyst. My reworking confirms most of the mathematical substance and pins down one place where the reported significance of the R_X computation is larger than what the computation actually establishes. Corrected/derived formulas are given throughout.

## 1. Gaussian evolution equations and sign conventions — correct

For $g=dn^2+q_{ij}(n,s)\,dy^idy^j$ with $K_{ij}=\tfrac12\partial_n q_{ij}$, the tangential Ricci identity is
$$
R^{(g)}_{ij}=R^{(q)}_{ij}-\partial_nK_{ij}-HK_{ij}+2K_i^{\;k}K_{kj},\qquad H=q^{ij}K_{ij}.
$$
Imposing $R^{(g)}_{ij}=-3q_{ij}$ gives exactly the script's second equation
$$
\partial_nK_{ij}=R^{(q)}_{ij}+3q_{ij}-HK_{ij}+2K_i^{\;k}K_{kj},
$$
and `kqik = einsum('nij,njk,nkl->nil',k,qi,k)` implements $K_{ik}q^{kl}K_{lj}=K_i^{\;k}K_{kj}$ with the correct factor 2. I checked the whole sign package against $\mathbb H^4$ written as $g=dn^2+e^{2n}\delta_{ij}dx^idx^j$: there $K_{ij}=q_{ij}$, $H=3$, $R^{(q)}=0$, and the formula returns $R^{(g)}_{ij}=-2q-3q+2q=-3q$, i.e. $\mathrm{Ric}=-3g$. The Hamiltonian relation is likewise correct: the contracted Gauss equation gives $R^{(q)}-H^2+|K|^2=R^{(g)}-2R^{(g)}_{nn}$, which for $\mathrm{Ric}=-3g$ (scalar $-12$, $R^{(g)}_{nn}=-3$) equals $-6$, matching `ham = scalar - h*h + w2 + 6`. The momentum relation $q^{jk}\nabla_jK_{ki}-\partial_iH=0$ is the $R^{(g)}_{ni}=0$ Codazzi component. The `christoffel_and_ricci` routine correctly restricts every coordinate derivative to the $s$-direction (all fields $T^2$-invariant), and the covariant correction terms in the momentum routine carry the derivative on the index $j$ as they should. No sign or index error found.

## 2. Quotient variable extraction — invariantly correct

The split `a2 = q_ss - vᵀG⁻¹v`, `avec = G⁻¹v`, `rho = √det G` is the Riemannian-submersion/Kaluza–Klein decomposition
$$
q=a^2\,ds^2+G_{ab}\,(dx^a+A^a ds)(dx^b+A^b ds),\qquad A=G^{-1}v,\ v_a=q_{sa}.
$$
$a$ (base lapse, orthogonal to fibres), $\rho$ (fibre area, invariant under the fixed lattice/$SL(2,\mathbb Z)$), and the curvature $f=\partial_nA/a$ are all torus-reparametrization-invariant. Because Gaussian normal form carries no $dn\,dy$ cross term, the connection has $A_n\equiv0$, so the only field-strength component is $F_{ns}=\partial_nA_s$, which `an = Gi@(vn - Gn@avec)` computes correctly via $\partial_n(G^{-1}v)=G^{-1}(v_n-G_nA)$. The Maxwell charge $\rho\,G f$ and $Q=\tfrac12 f^TGf$ are then invariant. The identity $\tfrac12\,q_{\rm cons}^TA\,q_{\rm cons}=Q$ with $A=e^{-3\sigma}M^{-1}$ (`Amat = Gi/rho²`) holds. The extraction stays valid along the flow because $A_n=0$ is preserved.

## 3. The initial 2-jet invariants — all four follow analytically

I re-derived each; they are theorems for this center, not numerical accidents.

**$H_n$.** Using $\partial_nq^{ij}=-2K^{ij}$ and the evolution equation,
$$
\partial_nH=-2|K|^2+q^{ij}\partial_nK_{ij}=R^{(q)}+9-H^2.
$$
Substituting the Hamiltonian relation $R^{(q)}=-6+H^2-|K|^2$ gives the clean pointwise law
$$
\boxed{\;\partial_nH=3-|K|^2\;}
$$
(more generally $-\lambda-|K|^2$ for $\mathrm{Ric}=\lambda g$). On the separator $|K|^2=\mathrm{tr}(W^2)=P+Q=S$ is constant along $s$ even though $P,Q$ individually vary, so $H_n=3-S=2$ for $S=1$, constant in $s$. This is exactly why the data show $H_n\in[1.9999,2.0001]$ with no $s$-spread.

**$\sigma_{nn}$.** With $\rho=\sqrt{\det G}$, at the block-diagonal center ($v=0$, $a=1$, $\rho=1$, $H=0$):
$$
\sigma_{nn}=\tfrac12\big[-\mathrm{tr}((G^{-1}G_n)^2)+\mathrm{tr}(G^{-1}G_{nn})\big]
= r_G+6+Q,\qquad r_G:=G^{ab}R^{(q)}_{ab}.
$$
The transverse pieces evaluate to $\mathrm{tr}((G^{-1}G_n)^2)=4P$ and $\mathrm{tr}(G^{-1}(K_n)_G)=r_G+6+2P+Q$, using $\mathrm{tr}(G^{-1}(Kq^{-1}K)_G)=P+\tfrac12Q$ (the mixed Weingarten block contributes $\mathrm{mcov}^TM^{-1}\mathrm{mcov}=\tfrac12Q$). For the unimodular fibre metric $q=ds^2+M(s)dx dx$ I computed the intrinsic fibre Ricci directly,
$$
R^{(q)}_{ab}=-\tfrac12 M''_{ab}+\tfrac12\,(M'M^{-1}M')_{ab},
$$
and with $\mathrm{tr}(M^{-1}M')=0$ (so $\mathrm{tr}(M^{-1}M'')=\mathrm{tr}((M^{-1}M')^2)$) this gives $r_G=M^{ab}R^{(q)}_{ab}=0$. Hence
$$
\boxed{\;\sigma_{nn}=6+Q\;}.
$$
The evolution data confirm this independently: at $n=0.02$, $\sigma\approx\tfrac12(6+Q)n^2$ predicts $\rho\in[1.00120,1.00130]$ across $Q\in[0.0086,0.5]$, exactly the reported `rho_range`.

**$a_{nn}$.** Since $H=\partial_n\log(a\rho)=(\log a)_n+\sigma_n$ and $a_n=\sigma_n=0$ at the center, $H_n=a_{nn}+\sigma_{nn}$, so
$$
\boxed{\;a_{nn}=H_n-\sigma_{nn}=2-(6+Q)=-(4+Q)\;},
$$
matching both `base_a_nn_range` and the $n=0.02$ `base_a_range`. Note $H_n$ is $s$-constant while $a_{nn},\sigma_{nn}$ carry the full $Q(s)$ variation with an exact cancellation in their sum.

**Coordinate-charge conservation.** At the center $\;q_{\rm cons}=\rho\,GA_n=v_n=2K_{as}=2\,\mathrm{mcov}=-\mathfrak q\;$ identically in $s$, because $GA_n=MM^{-1}(-\mathfrak q)$ is independent of $M(s)$. So $s$-constancy is exact (the $10^{-15}$ std is round-off). The nontrivial content is $\partial_n q_{\rm cons}=0$ (measured at $10^{-13}$), which is momentum-constraint propagation, i.e. genuine Einstein content; that is confirmed, not assumed.

All four statements are therefore analytically established and numerically consistent to the precision the resolution allows.

## 4. What the $n=0.02$ run does and does not show

The Cauchy data are real-analytic (analytic target circle, analytic constructions), so Cauchy–Kovalevskaya already guarantees a unique local analytic Einstein continuation off the separator; local existence is a theorem, and the run illustrates rather than discovers it. The elliptic system makes forward marching ill-posed; the informative quantity is the Hamiltonian residual growth versus resolution. At fixed $n=0.02$ the terminal residual is $8.3\times10^{-2}$ (N=48), $1.0\times10^{-2}$ (N=64), $1.3\times10^{-4}$ (N=96) — geometric decay consistent with spectral approximation of a smooth continuum solution over this short interval, not a geometric singularity. So the run genuinely tracks the analytic germ; it carries no information about global continuation, cusp formation, or attachment to $\lambda<0$ open ends. One numerical texture worth noting: the momentum residual sits at $\sim2\times10^{-4}$ already at $n=0$ (N=96) and stays nearly flat — this is discrete Fourier representation error of the peaked profile ($q$-eigenvalues span $0.13$–$7.6$), a frozen offset rather than a growing mode over $n\le0.02$.

## 5. The R_X pairing is the divergence theorem plus $dq=0$, not an independent test of the Noether content

This is the one place where the reported meaning outruns the computation.

The identity used, $\int m_q(X)\,d\mu_\sigma=-\tfrac12\int q^TK_Xq\,d\mu_\sigma$ with $K_X=X(A)+(\mathrm{div}_\sigma X)A$, is a pure integration-by-parts equality that holds for **any** smooth $A,q$ and compactly supported $X$; the Einstein equations play no role in it. I verified it by expanding $\partial_i(q^TAq)=2q^TA\partial_iq+q^T\partial_iAq$ and integrating: the two $K_X$ terms combine to $-\int m_q(X)$ regardless of the field equations.

Now specialize to this experiment. The paired object is the **conserved** charge $q_{\rm cons}$, which §3 shows is constant in both $s$ and $n$ ($dq_{\rm cons}=0$ to $10^{-13}$–$10^{-15}$). Therefore $m_{q}(X)=q_{\rm cons}^TA\,\nabla_Xq_{\rm cons}=0$ pointwise, and with $X=\chi(n)\partial_n$ the integrand reduces to
$$
\tfrac12 q^TK_Xq=\chi\,\partial_nQ+(\mathrm{div}_\sigma X)\,Q=\mathrm{div}_\sigma(Q\,X),
$$
whose integral over the compactly-supported $X$ vanishes by the divergence theorem. This is exactly the observed structure: the per-slice values are large and opposite about the symmetric point ($+252.75$ at $n=0.005$, $-254.55$ at $n=0.015$, driven by the antisymmetric $\chi'=\mathrm{div}\,X$), and the $n$-integral is a tautological near-zero. Its value ($7.9\times10^{-9}\to2.3\times10^{-9}\to2.7\times10^{-9}$) does not converge with resolution — it sits at a quadrature/round-off floor, as a tautology residual should, not as a converging geometric functional.

Consequence for the research judgment: the R_X computation validates (a) the code's IBP bookkeeping and (b) charge conservation over the short interval — both worthwhile consistency facts — but it does **not** exercise the discriminating part of the horizontal Noether identity (8.3)/(8.6). That part becomes nonzero only when the geometry carries a Ricci defect: for the exact germ $H=T=Z=0$ **and** $m_q=0$ simultaneously, so both sides of (8.6) are identically zero and nothing is separated. The chosen $X=\chi\,\partial_n$ (purely normal, compactly supported) is the specific field that annihilates the interesting content; it never engages the orbit/$s$-directions or the transverse energy $e_\perp$ of note §2 (2.8). Reporting this as "independent validation of the Noether pairing" should be read as "validation of an integration identity and of $dq=0$."

## 6. The exact matching object to build next from this center

The germ is now fully known to second normal order; the open question is whether this order-one-charge stable minimal neck can be joined to $\lambda<0$ open ends. The right next object is a **finite ledger of flux functionals that are linear in the Ricci defect $E$**, coupled to the separator's genuine coercivity — and it must be exercised on a defect geometry, not on the exact germ and not on radial flat-slice reductions.

Concretely:

1. **Vector charge flux.** $dq_a=2\rho\,E(J\cdot,V_a)$ (note §4, 4.2). Between two $\lambda<0$ open (cusp/OT) ends where $q\to0$, exactness forces $\;0=\int_{\rm end_-}^{\rm end_+}dq\;$ and $\oint dq=0$ — two real conditions. For an exact connected Einstein region this already forces $\mathfrak q=0$, contradicting the nonzero-charge center; so any connector realizing this center is necessarily defect-carrying, and $\mathfrak q$ equals the accumulated defect flux $\int 2\rho\,E(J\cdot,V)$.

2. **Horizontal Bianchi moment.** Equation (8.4)–(8.5), $C'=-2(u+H)C-wb$ with $\int\mu\,wb=0$, is a second, independent weighted moment beyond total charge flux. The redshift-taper study (§6) shows that charge flux + area + Maxwell alone cannot bound the interior amplitude (delayed source escapes as $e^{-3\sqrt6R/2}$), so a single moment is insufficient; the two moments must be imposed **jointly**.

3. **Coercivity source.** The center supplies what the radial models lack: the Jacobi form $\mathcal J(\phi)=\int(|\nabla\phi|^2+(3-S)\phi^2)$ with strictly positive lowest eigenvalue $3-S=2$. This $s$-direction coercivity — together with $H_n=3-S>0$ (both sides expand from a local volume minimum) — is the natural object to pair against the two flux moments.

The construction I would build is the **linearized two-ended matching operator at this charged Koiso center**: the map from constraint-satisfying, gauge-reduced normal-derivative data (a finite-dimensional space, now anchored by the explicit 2-jet) to the pair (vector charge flux, horizontal moment) at the two ends, viewed as functionals of the full $s$-dependent transition. The decisive computation is whether these linear-in-$E$ functionals, under the requirement $q(\text{center})=-\mathfrak q\neq0$ and $q(\text{ends})=0$, admit simultaneous vanishing with $\|E\|\to0$, or whether the separator coercivity $3-S$ forces a positive lower bound on $\|E\|$. The correct adjoint test field is **not** the purely-normal compact $X$ of the R_X run but one carrying orbit/$s$-components (e.g. $X=\nabla\sigma$, note §95 §2, or a field tuned to the Jacobi mode), applied to a defect geometry where $H,T,Z,m_q$ are all $O(\delta)$ and can genuinely cancel or fail to cancel. Building a distributed sign-changing $E$ that satisfies both moments with every Ricci block $\to0$ would be the counterexample side of the same object.

## 7. Framing note

This thread studies $\delta$-pinching around a single $\lambda=-3$ value in the $T^2$-invariant four-dimensional class. That is a much tighter hypothesis than Yau-26's dimension-only band $c_ng\le\mathrm{Ric}\le C_ng$ with $c_n<C_n$ unrestricted in sign and width. Resolving the charged-connector question here would settle whether narrow pinching about a fixed $\lambda<0$ forces an Einstein metric in this symmetric class — a meaningful sub-question and a plausible counterexample laboratory — but it addresses one slice of the full statement, and the logical passage from a symmetric-class construction to the dimension-uniform constants of Yau-26 remains a separate matter to keep in view.

**Summary of corrected/derived formulas handed back:** $\partial_nH=3-|K|^2$ (pointwise; $=3-S$ on the separator); $R^{(q)}_{ab}=-\tfrac12M''_{ab}+\tfrac12(M'M^{-1}M')_{ab}$ with fibre-trace $r_G=0$; $\sigma_{nn}=6+Q$; $a_{nn}=-(4+Q)$; $q_{\rm cons}=v_n=2K_{as}=-\mathfrak q$ exactly $s$-independent; and the R_X numerator equals $\int\mathrm{div}_\sigma(QX)=0$ by the divergence theorem given $dq_{\rm cons}=0$.