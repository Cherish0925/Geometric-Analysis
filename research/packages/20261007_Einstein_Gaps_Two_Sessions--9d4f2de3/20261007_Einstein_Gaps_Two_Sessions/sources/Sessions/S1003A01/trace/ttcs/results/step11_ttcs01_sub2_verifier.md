# TTCS Independent Branch Record

```json
{
  "step_id": 11,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/perp_rigorous_enclosure.py",
    "Sessions/S1003A01/workspace/scripts/check_bianchi_ricci_closed_form.py",
    "Sessions/S1003A01/workspace/scripts/perp_cartan_verify.py",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json",
    "Sessions/S1003A01/workspace/data/perp_collar/rigorous_x0.01_X8_J_d8.json",
    "Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A02/workspace/data/o11_peer_rigorous_replication_256.json"
  ]
}
```

## Task

Independently verify the computer-assisted theorem that the frozen perpendicular Bianchi-IX cell has J_6<8π². Read the actual enclosure code, frozen JSON profile, symbolic Ricci checker, Step-10 theorem note, and peer independent reconstruction. Focus on the acb.integral holomorphy contract (including the piecewise phi_derivs series/quotient, complex-ball tail bound, analytic flags for log/sqrt), the desingularized Ricci algebra, exact interpretation of coefficients, volume/energy normalization, and faithful transcription of the profile. Identify any mathematically load-bearing flaw; if sound, state precisely what the certificate proves and its trust base. Do not merely summarize the files.

## Output

# Verification memo: frozen perpendicular CH cell, certified \(J_6/(8\pi^2)<1\)

## 1. Result

I found no mathematically load-bearing flaw in the computer-assisted part. I re-derived every identity in the integrand by hand and checked the enclosure code line by line against the Arb holomorphic-enclosure contract.

The certificate establishes the following. For the metric of Step-10 §1, with:

- \(x_0=1/100\) exactly (passed as the ball `arb(1)/100`),
- \(X=8\),
- \(z\) the 24 IEEE doubles of `x0.01_X8_J_d8.json`, read exactly,

the cell integral satisfies

\[
\frac1{8\pi^2}\int_{x_0\le x\le X}|\operatorname{Ric}+6g|^2dV\in[0.999116243135324311\pm2.3\times10^{-19}]\quad(256\text{ bit}).
\]

The 192-bit ball \([0.99911624314\pm7.0\times10^{-12}]\) contains this value, so the two runs nest. The 256-bit numbers satisfy \(J=P+S\) to every printed digit:

\[
0.999108702733592648+0.000007540401731663=0.999116243135324311.
\]

This is the exact pointwise identity \(|\operatorname{Ric}+6g|^2=|\operatorname{Ric}^\circ|^2+\tfrac14(s+24)^2\), which follows from \(\operatorname{Ric}+6g=\operatorname{Ric}^\circ+(s/4+6)g\) with \(|g|^2=4\). It is an internal consistency test of the three integrands.

The margin \(\eta\approx8.84\times10^{-4}\approx 8.8\,x_0^2\) exceeds the enclosure radius by about eight orders of magnitude.

## 2. Holomorphy contract of the integrand

**`phi_derivs`.** Both branches enclose the same entire function \(\varphi(z)=(e^z-1)/z\) and its derivatives. Choosing a branch from a non-holomorphic quantity (`abs(z)`) is therefore harmless.

- **Closed forms.** I re-derived them:
  - \(\varphi'=(ze^z-e^z+1)/z^2\);
  - \(\varphi''=(z^2e^z-2ze^z+2e^z-2)/z^3\), obtained by differentiating the numerator \(ze^z-e^z+1\) to \(ze^z\).
- **Zero-containing balls.** If a wide ball with upper modulus \(>1\) contains \(0\), `acb_div` returns an indeterminate value. The integrator then subdivides. This costs efficiency only and cannot produce a wrong enclosure.
- **Series coefficients.** The coefficients are \(1/(k+1)!\), \((k+1)/(k+2)!=1/((k+2)k!)\), and \((k+1)(k+2)/(k+3)!=1/((k+3)k!)\). All are \(\le1/k!\).
- **Tail bound.** Since consecutive-term ratios are \(r/(k+1)\le r/(N+1)\), the tail satisfies \(\sum_{k\ge N}r^k/k!\le r^N/N!\,(1-r/(N+1))^{-1}\). This is correct.
- **Error box.** `acb(arb(0,t),arb(0,t))` is a box of half-width \(t\) in each coordinate, so it contains the disk of radius \(t\).
- **Radius \(r\).** \(r=(\text{mid}+\text{rad})(1+2^{-30})+10^{-300}\) dominates the float rounding of `abs(z)`. Here \(r\) enters only the tail bound and the branch choice.

**Shc identity.** \(\varphi(w)+\varphi(-w)=2\sinh w/w\), so `shc` is \(\sinh w/w\). Also \((e^w-1)^2=w^2\varphi(w)^2\).

**Branch-cut functions.** The only ones are `log(1+x)` and `sqrt(FH/GH)`, and both carry the `analytic` flag. The remaining operations are as follows.

- `exp`, ring operations and integer squares are entire. Integer powers in Arb go through the exact-integer path of `acb_pow`. Even a general power would be holomorphic here, because the bases \(x_0\ell\varphi\) and \(R+6\) never cross a cut on the relevant balls.
- Division returns a finite value only when the denominator ball excludes 0, and the quotient is then holomorphic on the ball.
- `abs`, `mid` and `rad` are used only to compute \(r\).

So every finite output is an enclosure of a function holomorphic on the input ball, which is exactly the `acb_calc_integrate` contract.

**Parameter balls.** \(x_0\) and the bolt shift enter as balls. Each evaluation encloses the integrand for every parameter value in the ball, uniformly on each Gauss–Legendre ellipse. The returned enclosure therefore contains the integral for the exact parameters. At 128+ bits the shift (a signed sum of 16 doubles) is computed exactly anyway.

**Holomorphic extension and real part.** Squares \((R+6)^2\) are used rather than \(|R+6|^2\), which is the correct holomorphic extension of the real integrand. Taking `.real` of a real integral is legitimate.

**Holomorphy near the endpoints.** For \(u\) slightly below 0, \(y<0\) but \(\hat F,\hat G,\hat w\) stay analytic and \(\hat F/\hat G\approx e^{q_F-q_G}>0\). Holomorphy only affects convergence speed; correctness follows from the contract.

## 3. Desingularized Ricci algebra (independent hand derivation)

**Radial derivatives.** With \(h=a^2\) and \(d/dt=2\sqrt G\,d/dx\):

- \(\dot a/a=\sqrt G\,h'/h\);
- \(\ddot a/a=G'h'/h+2Gh''/h-Gh'^2/h^2\).

This reproduces `D3`, and with \(h_2=x\) it reproduces `D2` \(=G'/x-G/x^2\).

**Bolt slot.** With \(h_1=y\hat F\) and \(G=y\hat G\):

\[
\frac{G'h_1'}{h_1}-\frac{Gh_1'^2}{h_1^2}=\frac{h_1'}{y\hat F}\big[\hat G+y\hat G'-\rho(\hat F+y\hat F')\big]=h_1'\frac{\hat G'\hat F-\hat G\hat F'}{\hat F^2},
\]

so `D1` is exact. The products \(L_{1j}=\rho\,h_1'h_j'/h_j\) and \(L_{23}=Gh_3'/(xh_3)\) are exact.

**Algebraic terms.** For \(h_2=x\), \(h_3=xe^w\), \(w=y^2\hat w\):

- \(A_1=2h_1/(xh_3)-2y^3\hat w^2\varphi(w)^2/(\hat Fe^w)\);
- \(A_2=-4y\hat w\,\mathrm{shc}/\hat F+4/x-2h_1/(x^2e^w)\);
- \(A_3=+4y\hat w\,\mathrm{shc}/\hat F+4/(xe^w)-2h_1/(x^2e^w)\).

All three match the code.

**The base formula.** I checked it independently of the Cartan script.

- Milnor's formula gives \(\mathrm{Ric}^{(3)}_{11}=2\mu_2\mu_3\) with \(L_i=2a_i/(a_ja_k)\). This equals \((L_1^2-(L_2-L_3)^2)/2=2(a_1^4-(a_2^2-a_3^2)^2)/(a_1^2a_2^2a_3^2)\).
- The radial terms come from Gauss–Codazzi for \(dt^2+g_t\).
- Off-diagonal Ricci vanishes for diagonal class-A Bianchi IX. Hence \(|\operatorname{Ric}+6g|^2=\sum_a(R_{aa}+6)^2\) is complete.

**Jet arithmetic.**

- Product, quotient, exp and log rules are correct to second order.
- Converting \(u\)-jets to \(x\)-jets via \(x=x_0e^{\ell u}\) gives \(f_x=f_u/(\ell x)\) and \(f_{xx}=(f_{uu}-\ell f_u)/(\ell^2x^2)\), as coded.
- The jet of \(\varphi(\ell u)\) is \((\varphi,\ell\varphi',\ell^2\varphi'')\).

**Hatted profile.** The decomposition is consistent:

- \(x_0S/y=u^2(10-15u+6u^2)/(\ell\varphi)\);
- \(\hat G=(1+(x^2+x_0)u^2(\cdots)/(x_0\ell\varphi))e^{q_G}\);
- \(\hat w=[\log(1+x)u(\cdots)+(1-u)^3C_w]/(x_0\ell\varphi)^2\).

The pointwise values at \(u=0\) (\(R_{00}=R_{11}\), \(R_{22}=R_{33}\)) and at \(u=1\) (all entries \(-6\) to \(10^{-14}\)) agree with this algebra.

## 4. Coefficients and transcription

**Formula match.** The coded profile, the Step-10 §1 formula, `PerpCell.prof_factory` (non-aligned, \(\beta_0=0\), `wpow=2`), and the peer reconstruction `Metric.profile` all agree:

- slot order \(z[0{:}8]\to q_F\), \(z[8{:}16]\to q_G\), \(z[16{:}24]\to C_w\);
- the shift \(\tilde z_8=z_8-\sum(-1)^k(z_k+z_{8+k})\), which uses \(T_k(-1)=(-1)^k\).

**Reading the doubles.** `json` loading of the shortest-repr decimals returns the original doubles, and `arb(float)` is exact. So "\(z\in\mathbb Q^{24}\) = the stored doubles" is accurate.

**`wpow` value.** The record does not store `wpow`. The theorem, however, concerns the metric *defined* by the formula with \(u^2(1-u)^3C_w\), so the certificate stands on its own terms. Separately, the agreement of the record's float \(J\) (0.99911624282) with the ball to \(3\times10^{-10}\) shows the optimizer used the same `wpow=2` profile. With \(C_w\approx7\text{–}10\), replacing \(u^2\) by \(u\) would change \(J\) at order one.

**\(x_0\) value.** The float runs used \(x_0=0.01_{\rm double}\), while the certificate uses exact \(1/100\). The difference is irrelevant to the stated theorem.

## 5. Normalization

**Volume.** \(dV=a_1a_2a_3\,dt\,\sigma_{123}\), with \(\int\sigma_{123}=2\pi^2\) for \(d\sigma_i=2\sigma_j\wedge\sigma_k\) (round unit \(S^3\)). This gives \(\pi^2\sqrt{h_1h_2h_3/G}\,dx\). Then \(h_1h_2h_3/G=x^2e^w\hat F/\hat G\) and \(dx=\ell x\,du\) give the coded density \(\tfrac18x e^{w/2}\sqrt{\hat F/\hat G}\,\ell x\) per \(8\pi^2\,du\).

**Collar metric.** With \(x=\sinh^2r\), the collar is \(dr^2+\sinh^2r(\sigma_1^2+\sigma_2^2)+\sinh^2r\cosh^2r\,\sigma_3^2\). This is \(\mathbb{CH}^2\) with \(\operatorname{Ric}=-6g\), and the integrand vanishes identically beyond \(X\).

**Scale invariance.** \(\int|T|^2dV\) is scale invariant for a (0,2)-tensor in dimension 4, so \(J_6(g)=\int|\operatorname{Ric}_{\tilde g}+\tilde g|^2\) for \(\tilde g=6g\).

**Collar radius.** \(\sqrt6\,\operatorname{arsinh}\sqrt8=4.318\), matching the note.

## 6. Hand-proved ingredients (outside the computer part)

**Bolt smoothness.**

- \(y\) is analytic in \(t^2\), since \(t^2=y/\hat G(0)+O(y^2)\).
- \(a_1^2=t^2\cdot(\text{analytic in }t^2)\) with \(\hat F(0)\hat G(0)=e^{q_F(0)+q_G(0)}=1\). This gives \(a_1'(0)=1\), the full Hopf period \(2\pi\) in the unit-\(S^3\) normalization, i.e. an \(\mathcal O(-1)\) bolt.
- \(a_2^2=x\) is even in \(t\).
- \(a_2^2-a_3^2=x(1-e^w)=O(y^2)=O(t^4)\) times an analytic function of \(t^2\). This matches the weight-4 action of the Hopf circle on \(\sigma_2^2-\sigma_3^2\).
- The bolt sphere is round (\(w(x_0)=0\)).

These are the complete smoothness conditions. They hold exactly for `wpow=2` and would not hold for the default `wpow=1`.

**Collar matching.**

- Every deviation \(d_F,d_G,d_w\) carries the factor \((1-u)^3\), via \(1-S=(1-u)^3(1+3u+6u^2)\). So the metric is exactly \(C^2\), but not \(C^3\), at \(X\), and the curvature is continuous.
- I checked \(d_G=(x+x^2)(e^{q_G}-1)-(x^2+x_0)(1-S)e^{q_G}\).
- Positivity holds because \(0\le S\le1\) and \(\hat F\ge e^{q_F}\).

**Topology.**

- The cyclic permutation \(\sigma_1\to\sigma_2\to\sigma_3\to\sigma_1\) is an automorphism preserving the structure equations and \(\sigma_{123}\).
- The left-invariant fields dual to the \(\sigma_i\) all generate right-translation Hopf fibrations of the same handedness, connected through the \(S^2\) of unit left-invariant fields.
- Hence the \(\sigma_1\)-collapse filling is oriented-diffeomorphic to the \(\sigma_3\)-collapse (Burns) filling, compatibly with the collar sphere.
- An opposite-handed (left-translation) collapse would have produced the \(\#\mathbb{CP}^2\) orientation instead; that does not occur here.

**Smoothing lemma.**

- \(|d^{(k)}|\le C(X-x)^{3-k}\) and \(|\chi_\delta^{(k)}|\le C\delta^{-k}\) give a \(C^2\) distance \(O(\delta)\) from the CH jet on \(B_\delta\).
- \(\operatorname{Ric}+6g\) is a smooth function of the 2-jet vanishing at the CH jet, so it is \(O(\delta)\) on \(B_\delta\).
- With \(\mathrm{Vol}(B_\delta)=O(\delta)\), the energy change is \(O(\delta^3)\). The argument is correct.

**Corollary arithmetic.**

- \(28/9+8(1-\eta/2)/9=4-4\eta/9\).
- \(4-8\eta_{16}/9=3.99902484\) for \(\eta_{16}=1.0970563\times10^{-3}\).

## 7. Precise statement and trust base

**Certified by machine.** The enclosures of \(J\), \(P\), \(S\) (per \(8\pi^2\)) for the explicit \(C^2\) cell with \(x_0=1/100\), \(X=8\), and the stated rational coefficients.

**Trust base.**

1. Correctness of Arb's `acb_calc_integrate` and of the python-flint wrapper that passes the `analytic` flag to the callback.
2. Arb semantics:
   - `acb_div` returns a non-finite value for denominators containing 0;
   - `acb_log` and `acb_sqrt` with the analytic flag return non-finite values on balls meeting the cut;
   - integer powers are exact polynomial operations.
3. Python operator dispatch: `acb*Jet` falls back to `Jet.__rmul__`. The successful runs confirm it does not mis-dispatch.
4. The ~150-line integrand. I have checked it against items 2–3 above.

The symbolic checker's stdout (`s10_t11_tool1/stdout.log`) is cited but not supplied. The hand derivation in §3 independently covers every identity it is said to confirm.

**Proved by hand, not by the certificate.** Bolt smoothness, collar \(C^2\) matching, positivity, topology, and the smoothing lemma. I found all of them correct.

**Not supported by the supplied files.**

- **The \(X=16\) witness.** Neither `x00.01_X16_J_d8.json` nor its rigorous output is supplied (the "x00.01" filename also looks mistyped). The numbers \(\eta_{16}\) and \(3.99902484\) are therefore unverified here. The \(X=8\) witness alone gives \(4-8\eta/9+\epsilon\) with \(8\eta/9=7.856\times10^{-4}\).
- **The global transfer** (O11 corollary). It rests on I54 §2, which is not supplied: the definition of \(h_j\), the energy accounting \(\mathcal E(g_j)/h_j\), the value \(8\pi^2\) for the inherited Burns-cell and handle weights, and the relation between the functional \(\mathscr D\) defining \(\alpha\) and \(J_6\). The cell bound \(J_6<8\pi^2\) is certified, but the statement "coefficient four is not sharp" inherits I54's accounting.
- **The 256-bit "peer replication".** It reruns the same enclosure script, so it confirms reproducibility rather than providing independent code. The independent evidence is `o11_collar_independent_verify.py`. That script uses a different representation: cyclically reordered axes, spin variables \(u_i,H_i\), and a Chern–Simons relative completion. Its float agreement (0.9991162431353) checks the transcription and the Ricci algebra, since any algebra slip would show up far above \(10^{-11}\).

**Scientific reading.** The certified margin is \(\eta\approx8.8\,x_0^2\), i.e. second order in the bolt size. This is consistent with the Step-8 response law (first-order critical, second-order cubic compensation). The subthreshold effect is real but quantitatively small at this \(x_0\). The open quantity remains the cell infimum \(\kappa_1\) over collar radii and bolt sizes.