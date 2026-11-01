"""
Step 21 (S0910A02): cheap scaling audit for whether the opposite-warp/CZ spike
mechanism immediately falsifies the weighted degenerate parabolic estimate used
in the A01/A03 negative-branch smoothing route.

The target estimate being stress-tested schematically is
    |a Rm|(x,t) <= C beta/t,
where a=chi^2 is the cutoff diffusivity and beta is the critical 4D Sobolev
product A^2 ||Rm||_2 on a local ball.  This script uses exact Gaussian heat-flow
models with constant diffusivity a0 to see whether high pointwise/low-L2 spikes
can make t*a0*||u(t)||_infty / beta blow up as chi0->0 or spike scale sigma->0.

It is not a proof of the geometric tensor theorem; it is an adversarial scaling
check.  It shows the old elliptic CZ obstruction does not by itself break the
positive-time weighted heat estimate.
"""
import json, math, os

OUT = "Sessions/S0910A02/workspace/data/step21_weighted_cz_heat_scaling_audit.json"


def gaussian_ratio(k_active: int, sigma: float, a0: float, B: float, fiber_volume: float = 1.0):
    """Return ratios for a k-dimensional Gaussian spike extended constantly in
    the remaining local directions of total volume fiber_volume.

    Initial u0 = B exp(-|x|^2/(2 sigma^2)) in k active directions.
    Heat with diffusivity a0 in the active variables gives
      u(0,t)=B (sigma^2/(sigma^2+2 a0 t))^(k/2).
    L2 norm over active directions times passive volume is
      ||u0||_2 = B * sqrt(fiber_volume) * (pi^(k/4)) * sigma^(k/2).
    For a Euclidean ball with fixed relative Sobolev product, beta is modeled by
      A2_factor * ||u0||_2.  We take A2_factor=1 for the ratio; chi/a0
      dependence is the question under test.
    Maximize R(s)= t*a0*u(0,t)/||u0||_2 with s=a0 t/sigma^2.
    """
    l2 = B * math.sqrt(fiber_volume) * (math.pi ** (k_active/4.0)) * (sigma ** (k_active/2.0))
    # R(s) = sigma^2 * s * B * (1+2s)^(-k/2) / l2.
    # For k>2, max at s=1/(k-2). For k=2, increasing to limit 1/2.
    if k_active > 2:
        s_star = 1.0/(k_active-2.0)
        max_factor = s_star * (1+2*s_star) ** (-k_active/2.0)
    else:
        s_star = float("inf")
        max_factor = 0.5
    max_R = (sigma**2 * B * max_factor) / l2
    # Initial elliptic ratio a0*u0/beta can be huge; record separately.
    elliptic_ratio = a0*B/l2
    # Ratios at representative effective times s.
    samples = []
    for s in [1e-6, 1e-3, 0.01, 0.1, 0.5, 1.0, 10.0, 1e3]:
        t = s*sigma*sigma/a0
        u = B * (1+2*s)**(-k_active/2.0)
        R = t*a0*u/l2
        samples.append({"s=a0t/sigma2": s, "t": t, "u_center": u, "R=t*a0*u/l2": R})
    return {
        "k_active": k_active,
        "sigma": sigma,
        "a0=chi0^2": a0,
        "B_amplitude": B,
        "fiber_volume": fiber_volume,
        "L2_norm_model_beta_without_A2": l2,
        "max_s": s_star if math.isfinite(s_star) else "infty_limit",
        "max_R=t*a0*Linf/beta_model": max_R,
        "elliptic_initial_ratio=a0*B/beta_model": elliptic_ratio,
        "samples": samples,
    }


def scan():
    configs = []
    for k in [2, 3, 4]:
        for sigma in [1e-1, 1e-3, 1e-6]:
            for chi0 in [1.0, 1e-2, 1e-4]:
                # Choose B=sigma^{-k/2+0.25}; L2 tends to 0 like sigma^0.25,
                # while pointwise amplitude blows up for k>=1.
                B = sigma ** (-k/2.0 + 0.25)
                configs.append(gaussian_ratio(k, sigma, chi0**2, B))
    return configs


def main():
    results = scan()
    # Extract worst ratios for each k and sigma, across chi0, to verify no cutoff degeneracy.
    grouped = {}
    for r in results:
        key = f"k{r['k_active']}_sigma{r['sigma']}"
        grouped.setdefault(key, []).append(r)
    summary = {}
    for key, rows in grouped.items():
        summary[key] = {
            "max_over_chi0": max(row["max_R=t*a0*Linf/beta_model"] for row in rows),
            "min_over_chi0": min(row["max_R=t*a0*Linf/beta_model"] for row in rows),
            "elliptic_ratios": [row["elliptic_initial_ratio=a0*B/beta_model"] for row in rows],
        }
    report = {
        "title": "Step 21 weighted CZ/heat scaling audit",
        "target_estimate": "|a Rm|(t) <= C beta/t with a=chi^2",
        "model": "Gaussian high-curvature spike evolved by constant-diffusivity heat u_t=a0 Delta u; beta modeled by local L2 critical product.",
        "main_result": "For k=4 active dimensions the worst positive-time ratio is constant (1/(8*pi) with this normalization); for k=2 fiber-invariant CZ-type spikes it is O(sigma) and tends to zero.  The ratio is independent of chi0=a0^1/2.  Thus the old elliptic CZ spike does not by itself falsify the weighted positive-time smoothing estimate.",
        "important_contrast": "The initial elliptic ratio a0*B/beta can be arbitrarily large (especially for small sigma), which is exactly why Step 11 killed elliptic pointwise regularity.  The parabolic t^{-1} factor is large at small times and removes this immediate contradiction.",
        "grouped_summary": summary,
        "sample_records": [
            gaussian_ratio(4, 1e-6, 1.0, (1e-6)**(-4/2+0.25)),
            gaussian_ratio(2, 1e-6, 1e-8, (1e-6)**(-2/2+0.25)),
        ],
        "scientific_conclusion": [
            "A direct transplant of the opposite-warp/CZ spike is not an immediate counterexample to A01/A03's zero-order weighted parabolic estimate; the degeneracy weight a cancels the slow diffusion in the constant-coefficient model.",
            "The remaining falsification target is not high pointwise curvature at t=0 but the exact localized weak recurrence/finite-neighbor estimate under evolving normalized cutoff flow, especially transition terms and support leakage.",
            "This supports reallocating away from toric numerics while not claiming the negative smoothing theorem is proved."
        ]
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(report, f, indent=2)
    print(json.dumps({
        "title": report["title"],
        "main_result": report["main_result"],
        "k4_sigma1e-6_max_R": report["sample_records"][0]["max_R=t*a0*Linf/beta_model"],
        "k2_sigma1e-6_chi1e-4_max_R": report["sample_records"][1]["max_R=t*a0*Linf/beta_model"],
        "saved": OUT,
    }, indent=2))

if __name__ == "__main__":
    main()
