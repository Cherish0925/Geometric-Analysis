#!/usr/bin/env python3
"""Certified relative W+ energy and packing figures for frozen CH cells.

For a one-blow-up cell in the Ric_CH=-6g normalization,

    p-1 = Delta W+/(2 pi^2) + Delta S/(96 pi^2).

FrozenCell integrates over x in [x0,X].  The relative integral must also remove
the omitted CH core 0<=x<x0.  In these coordinates the latter contribution to
Delta S/(96 pi^2) is -3*x0^2.  Thus

    ds96 = ds96_shell - 3*x0^2,
    eta  = -Delta W+/(2 pi^2) = -(p-1-ds96).

Here eta is precisely the fraction of the ordinary 4*pi^2 Weyl-deficit loss
saved by one special blow-up.  All interval endpoints are emitted as exact
dyadics and outward decimal strings.
"""
import argparse
import json
import sys
import time
from pathlib import Path
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "Sessions/S1003A01/workspace/scripts"))
from perp_rigorous_enclosure import FrozenCell, _dyadic, _dec  # noqa: E402


def enc(x):
    lo, hi = _dyadic(x.lower()), _dyadic(x.upper())
    return {
        "ball": x.str(35, radius=True),
        "lower_dec_outward": _dec(lo, False),
        "upper_dec_outward": _dec(hi, True),
        "lower_dyadic": [str(lo.numerator), str(lo.denominator)],
        "upper_dyadic": [str(hi.numerator), str(hi.denominator)],
    }


def hull(obj):
    ln, ld = map(int, obj["lower_dyadic"])
    un, ud = map(int, obj["upper_dyadic"])
    return arb.union(arb(ln) / ld, arb(un) / ud)


def choose_interval(record, key):
    obj = record[key]
    if "lower_dyadic" in obj:
        return hull(obj)
    # Legacy strict certificate: its printed Arb ball is far tighter than the
    # binary64 lower/upper display.  Parse the Arb string directly.
    return arb(obj["ball"])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record", required=True)
    ap.add_argument("--certificate", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--x0-num", type=int, required=True)
    ap.add_argument("--x0-den", type=int, required=True)
    ap.add_argument("--prec", type=int, default=256)
    ap.add_argument("--tol", type=float, default=1e-18)
    ap.add_argument("--pieces", type=int, default=4)
    args = ap.parse_args()
    ctx.prec = args.prec

    rec = json.load(open(ROOT / args.record))
    cert = json.load(open(ROOT / args.certificate))
    x0 = arb(args.x0_num) / args.x0_den
    cell = FrozenCell(rec, x0=x0)

    def relative_scalar_shell(u, analytic):
        R, vol, profile = cell.ricci(u, analytic, want_profile=True)
        x = profile["x"]
        vol_ch = x * cell.ell * x / 8
        scalar = sum(R)
        # vol=dV/(8*pi^2), so this is Delta int s^2/(96*pi^2).
        return (scalar * scalar * vol - 576 * vol_ch) / 12

    t0 = time.time()
    z = acb(0)
    for j in range(args.pieces):
        z += acb.integral(
            relative_scalar_shell,
            arb(j) / args.pieces,
            arb(j + 1) / args.pieces,
            rel_tol=args.tol,
            abs_tol=args.tol / args.pieces,
        )
    ds_shell = z.real
    core = 3 * x0 * x0
    ds_total = ds_shell - core
    p = choose_interval(cert, "P")
    delta_wplus_over_2pi2 = p - 1 - ds_total
    eta = -delta_wplus_over_2pi2
    loss = 1 - eta
    h_all_cell = 1 / (3 * loss)

    # Ric=-g support radius and elementary volume lower-packing coefficient.
    # In the Ric=-6g cell scale dV/(8*pi^2)=x dx/8, hence V(B_r)=pi^2*x^2/2.
    # Rescaling by 6 to Ric=-g multiplies volume by 36, so V(B_R)=18*pi^2*x^2.
    # Since V(host)=2*pi^2*A, beta0=N/A >= 2*pi^2/V(B_2R)=1/(9*X(2R)^2).
    # sinh(2 asinh sqrt(X))^2=4 X(1+X).
    X = cell.X
    x2R = 4 * X * (1 + X)
    beta0 = 1 / (9 * x2R * x2R)
    # A maximal 2R-separated set supplies disjoint R-balls.  For the mixed
    # theorem all N sites may carry special cells, so h<1/3+eta*(N/A).
    h_packing = arb(1) / 3 + eta * beta0
    # |W+|^2=2/3 at Ric=-g, so the ball contains 12*pi^2*X^2,
    # namely 3*X^2 units of 4*pi^2 self-dual Weyl energy.
    footprint_energy_fraction = 3 * X * X
    annihilation_efficiency = eta / footprint_energy_fraction
    # Literal fraction of the ball's self-dual Weyl energy removed:
    # -Delta I+ = 2*pi^2*eta, I+(B_R) = 12*pi^2*X^2, ratio eta/(6 X^2).
    literal_removed_fraction = eta / (6 * X * X)
    # Disjoint-volume ceiling: N*V(B_R) <= V(Y) = 2*pi^2*A, i.e. N/A <= 1/(9 X^2).
    beta_max = 1 / (9 * X * X)

    out = {
        "record": args.record,
        "certificate": args.certificate,
        "prec": args.prec,
        "pieces": args.pieces,
        "seconds": time.time() - t0,
        "x0": enc(x0),
        "X": enc(X),
        "p": enc(p),
        "ds96_shell": enc(ds_shell),
        "removed_CH_core_3x0sq": enc(core),
        "ds96_total": enc(ds_total),
        "delta_Wplus_over_2pi2": enc(delta_wplus_over_2pi2),
        "eta_W": enc(eta),
        "ordinary_deficit_loss_fraction": enc(loss),
        "formal_all_cell_h": enc(h_all_cell),
        "packing": {
            "X_at_2R": enc(x2R),
            "beta0_N_over_A": enc(beta0),
            "realized_h_lower_endpoint": enc(h_packing),
            "host_Wplus_footprint_in_4pi2_units": enc(footprint_energy_fraction),
            "eta_per_host_Wplus_footprint": enc(annihilation_efficiency),
            "literal_removed_Wplus_fraction_of_ball": enc(literal_removed_fraction),
            "disjoint_volume_ceiling_N_over_A": enc(beta_max),
            "ceiling_h_if_all_sites_used": enc(arb(1) / 3 + eta * beta_max),
        },
    }
    (ROOT / args.out).write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
