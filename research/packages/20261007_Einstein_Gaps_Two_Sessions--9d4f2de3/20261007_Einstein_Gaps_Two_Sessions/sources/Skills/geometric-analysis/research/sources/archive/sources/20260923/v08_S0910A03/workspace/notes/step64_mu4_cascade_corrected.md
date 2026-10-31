# Slice-defect bounds — corrected again in Step 67

> The numerical lower bounds for isolated tori are retained. Step 67 withdraws the claim that these bounds close corresponding ambient collar dimensions: intrinsic slice defect can be compensated by the second fundamental form and normal evolution. The exact value of \(\mu_4\) is not determined. See `step67_corrections_and_analytic_neck_reopening.md`.

Session: S0910A03. Phase: Explore. Written Step 65 after the Strategist's
correction; supersedes `step64_mu4_bifurcation.md`, which is retained only as
provenance (its "unknown / Weyl absorbs / caveat" claims are all wrong — see
`step65_mu4_correction_and_neck_fusion.md` §1.3).

## The invariant

\[
\mu_m:=\inf_{\gamma\in\mathcal M(T^m)}\|\operatorname{Ric}_\gamma+(m-1)\gamma\|_{C^0(\gamma)},
\]
the \(C^0\) operator-norm distance of the \(m\)-torus from a negative Einstein
metric of Einstein constant \(-(m-1)\). (The homothetic normalization is
explicit: scaling \(\gamma\) trades volume against the constant.)

## Valid isolated-slice bounds

| \(m\) | value / bound | mechanism |
|---|---|---|
| 2 | \(\mu_2=1\) | Gauss–Bonnet: \(\int_{T^2}R\,dA=0\), so \(R\) cannot be uniformly close to \(-2\). |
| 3 | \(\mu_3\ge2/3\) | \(\|\operatorname{Ric}+2g\|_{\mathrm{op}}<2/3\Rightarrow K<0\) everywhere; Preissmann excludes \(\mathbb Z^3\). |
| 4 | \(\mu_4\ge3(\sqrt3-1)/2\approx1.0981\) | Chern–Gauss–Bonnet (the session's Step 2 estimate): \(8\pi^2\chi=\int(|W|^2+s^2/24-|\mathring{\operatorname{Ric}}|^2/2)\); on \(T^4\) (\(\chi=0\)) the pinching forces \(s^2/24\ge\tfrac23\Lambda^2(1-\delta)^2\) against \(\tfrac12\int|\mathring{\operatorname{Ric}}|^2\le2\delta^2\Lambda^2\operatorname{Vol}\); \(|W|^2\ge0\) only worsens the deficit. Threshold \((2/3)(1-\delta_0)^2=2\delta_0^2\), \(\delta_0=(\sqrt3-1)/2\). |
| \(\ge5\) | open | No Euler characteristic (odd \(m\)), no Preissmann control (Ricci does not control sectional curvature in \(m\ge4\)). Adjacent to the open question of negative Einstein metrics on (exotic) tori in \(n\ge5\). **Monitor, do not attack.** |

## Scope for the ambient program

1. The Step 63 theorem remains valid for intrinsically flat slices, including every coordinate-independent matrix family \(G(r)\). It does not cover a general tangentially dependent \(\gamma_r(x)\).
2. The isolated-slice bounds do not imply that higher-dimensional ambient constructions need slice dimension at least five. No first-open-ambient-dimension conclusion is currently established.
3. **Cheap absolute gap class:** every closed 4-manifold with
   \(2\chi\le3|\tau|\) carries no metric with
   \(\|\operatorname{Ric}-\Lambda g\|_{\mathrm{op}}<\delta_0|\Lambda|\) for any
   \(\Lambda\ne0\), either sign, no compactness or no-Einstein input.
   Membership includes \(T^4\), K3, and the appropriate connected-sum examples; it does **not** include \(\Sigma_g\times\Sigma_h\) for \(g,h\ge2\), since those have \(\chi>0,\tau=0\) and admit an Einstein product. \(\#_k(S^2\times S^2)\)
   and A02's balanced \(\chi=8\) mixed rows are NOT in it. Extended graph
   manifolds escape this mechanism only because \(2\chi>3|\tau|\) there.
4. The Chern–Weil computation proves only \(\mu_4\ge3(\sqrt3-1)/2\); its exact value is not determined. \(\mu_5\) remains open, but neither invariant alone settles an ambient collar construction.
