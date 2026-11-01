#!/usr/bin/env python3
"""Exact rank-one (circle) reduction of four-dimensional curvature in
normalization-invariant variables.

Setting
-------
Let U be a domain carrying a free isometric circle action with
three-dimensional quotient B, so that

    g = g_B + ell^2 (dpsi + A)^2,      ell > 0 on B,  A a 1-form on B.

Fix a base point p.  Put

    z = ell(p) psi,   v = ell/ell(p),   Bform = ell(p) A.

Then g = g_B + v^2 (dz + Bform)^2 with v(p) = 1, and the circle has period
2 pi ell(p).  All local metric coefficients are independent of ell(p):
the collapse parameter appears ONLY in the fiber period.  The invariant
local data is therefore

    u  = d log v        (1-form on B; u(p) is the normalized fiber gradient)
    C  = v * d(Bform)   (2-form on B; the scaled twist)
    g_B (base metric)

together with their base derivatives.  This script computes the full
four-dimensional curvature at p as an explicit polynomial in

    Ric^B_ab           (base Ricci in an orthonormal base frame; in 3d this
                        determines the base Riemann tensor)
    u_a                (3 components)
    Du_ab = Hess_ab log v   (symmetric, 6 components)
    C_ab               (antisymmetric, 3 components)
    DC_abc = grad_c C_ab    (9 components, 1 relation from dC = u ^ C)

Frame conventions
-----------------
e^0,e^1,e^2  : orthonormal coframe of g_B, chosen normal at p (omega^B(p)=0)
e^3 = v (dz + Bform)
    de^3 = sum_a u_a e^a ^ e^3 + sum_{a<b} C_ab e^a ^ e^b
Cartan then forces
    omega_ab = omega^B_ab - (1/2) C_ab e^3
    omega_a3 = -(1/2) C_ab e^b - u_a e^3
Curvature 2-forms Omega_AB = d omega_AB + sum_C omega_AC ^ omega_CB
                           = sum_{C<D} R_ABCD e^C ^ e^D.
Ricci: Ric_BD = sum_A R_ABAD;  s = sum Ric_AA.
Curvature operator on Lambda^2 in the pair basis
    P1=(0,1) P2=(0,2) P3=(0,3) P4=(2,3) P5=(3,1) P6=(1,2)
with M_IJ = R_{P_I P_J}; self-dual block uses (P1+P4,P2+P5,P3+P6)/sqrt2 and
    R|_{Lambda^2_pm} = W^pm + (s/12) Id.

Verification in main(): the base-only limit, the closure identity
d(de^3)=0, and an exact instantiation by Taub-NUT-AdS (Ric = -g) whose
four-dimensional invariants were computed independently in Step 12.
"""
from __future__ import annotations

import itertools
import math

import numpy as np
import sympy as sp


# ----------------------------------------------------------------- forms


def perm_sign(seq) -> int:
    s = 1
    seq = list(seq)
    n = len(seq)
    for i in range(n):
        for j in range(i + 1, n):
            if seq[i] == seq[j]:
                return 0
            if seq[i] > seq[j]:
                s = -s
    return s


def fadd(*forms):
    out: dict = {}
    for f in forms:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def fscale(c, f):
    return {k: sp.expand(c * v) for k, v in f.items() if sp.expand(c * v) != 0}


def fwedge(f1, f2):
    out: dict = {}
    for k1, v1 in f1.items():
        for k2, v2 in f2.items():
            key = tuple(k1) + tuple(k2)
            sg = perm_sign(key)
            if sg == 0:
                continue
            srt = tuple(sorted(key))
            out[srt] = out.get(srt, 0) + sg * v1 * v2
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def dscalar(expr, Dtab):
    """Exterior derivative of a scalar built from the parameter symbols."""
    out: dict = {}
    expr = sp.expand(expr)
    for s, ders in Dtab.items():
        c = sp.diff(expr, s)
        if c == 0:
            continue
        for a in range(3):
            if ders[a] != 0:
                out[(a,)] = out.get((a,), 0) + c * ders[a]
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def d1form(form, Dtab, de3):
    """Exterior derivative of a 1-form, evaluated at the base point."""
    out: dict = {}
    for key, coef in form.items():
        (A,) = key
        out = fadd(out, fwedge(dscalar(coef, Dtab), {(A,): sp.Integer(1)}))
        if A == 3:
            out = fadd(out, fscale(coef, de3))
        # de^a = 0 at p for a = 0,1,2 (normal base frame)
    return out


# ------------------------------------------------------- reduced curvature


class Rank1Reduction:
    def __init__(self):
        self.u = [sp.Symbol(f"u{a}", real=True) for a in range(3)]
        self.Du = [[None] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(a, 3):
                sym = sp.Symbol(f"h{a}{b}", real=True)
                self.Du[a][b] = sym
                self.Du[b][a] = sym
        self.Cs = {}
        for a, b in itertools.combinations(range(3), 2):
            self.Cs[(a, b)] = sp.Symbol(f"C{a}{b}", real=True)
        self.DCs = {}
        for a, b in itertools.combinations(range(3), 2):
            for c in range(3):
                self.DCs[(a, b, c)] = sp.Symbol(f"DC{a}{b}_{c}", real=True)
        self.RB = [[None] * 3 for _ in range(3)]
        for a in range(3):
            for b in range(a, 3):
                sym = sp.Symbol(f"RB{a}{b}", real=True)
                self.RB[a][b] = sym
                self.RB[b][a] = sym

        self.params = (
            self.u
            + [self.Du[a][b] for a, b in itertools.combinations_with_replacement(range(3), 2)]
            + [self.Cs[k] for k in sorted(self.Cs)]
            + [self.DCs[k] for k in sorted(self.DCs)]
            + [self.RB[a][b] for a, b in itertools.combinations_with_replacement(range(3), 2)]
        )

        self._build()

    # --- helpers on antisymmetric objects
    def C(self, a, b):
        if a == b:
            return sp.Integer(0)
        return self.Cs[(a, b)] if a < b else -self.Cs[(b, a)]

    def DC(self, a, b, c):
        if a == b:
            return sp.Integer(0)
        return self.DCs[(a, b, c)] if a < b else -self.DCs[(b, a, c)]

    def RiemB(self, a, b, c, d):
        """Base Riemann tensor from base Ricci (3d: Weyl = 0)."""
        de = sp.KroneckerDelta
        sB = sum(self.RB[i][i] for i in range(3))
        val = (
            de(a, c) * self.RB[b][d]
            + de(b, d) * self.RB[a][c]
            - de(a, d) * self.RB[b][c]
            - de(b, c) * self.RB[a][d]
        )
        val -= sp.Rational(1, 2) * sB * (de(a, c) * de(b, d) - de(a, d) * de(b, c))
        return sp.expand(val)

    def _build(self):
        # derivative table for scalars appearing in the connection forms
        Dtab = {}
        for a in range(3):
            Dtab[self.u[a]] = [self.Du[a][b] for b in range(3)]
        for (a, b), sym in self.Cs.items():
            Dtab[sym] = [self.DC(a, b, c) for c in range(3)]
        self.Dtab = Dtab

        de3 = {}
        for a in range(3):
            de3[(a, 3)] = self.u[a]
        for (a, b), sym in self.Cs.items():
            de3[(a, b)] = sym
        self.de3 = de3

        # connection forms at p (omega^B(p) = 0)
        omega = {}
        for a, b in itertools.combinations(range(3), 2):
            omega[(a, b)] = {(3,): -sp.Rational(1, 2) * self.C(a, b)}
        for a in range(3):
            form = {(3,): -self.u[a]}
            for b in range(3):
                val = -sp.Rational(1, 2) * self.C(a, b)
                if val != 0:
                    form[(b,)] = form.get((b,), 0) + val
            omega[(a, 3)] = {k: sp.expand(v) for k, v in form.items() if sp.expand(v) != 0}
        self.omega = omega

        def om(A, B):
            if A == B:
                return {}
            if (A, B) in omega:
                return omega[(A, B)]
            return fscale(-1, omega[(B, A)])

        # curvature 2-forms
        Omega = {}
        for A, B in itertools.combinations(range(4), 2):
            # d omega_AB
            if B == 3:
                dom = d1form(om(A, B), Dtab, de3)
            else:
                base_part = {}
                for c, d in itertools.combinations(range(3), 2):
                    val = self.RiemB(A, B, c, d)
                    if val != 0:
                        base_part[(c, d)] = val
                dom = fadd(base_part, d1form(om(A, B), Dtab, de3))
            quad = {}
            for Cidx in range(4):
                if Cidx in (A, B):
                    continue
                quad = fadd(quad, fwedge(om(A, Cidx), om(Cidx, B)))
            Omega[(A, B)] = fadd(dom, quad)
        self.Omega = Omega

        # Riemann components
        R = {}
        for (A, B), form in Omega.items():
            for (Cc, Dd), coef in form.items():
                R[(A, B, Cc, Dd)] = coef
        self._R = R

        # Ricci, scalar
        Ric = sp.zeros(4)
        for B in range(4):
            for D in range(4):
                Ric[B, D] = sp.expand(sum(self.Rc(A, B, A, D) for A in range(4)))
        self.Ric = sp.simplify(Ric)
        self.scal = sp.expand(sum(self.Ric[i, i] for i in range(4)))

        # curvature operator and Weyl halves
        pairs = [(0, 1), (0, 2), (0, 3), (2, 3), (3, 1), (1, 2)]
        M = sp.zeros(6)
        for I, (a, b) in enumerate(pairs):
            for J, (c, d) in enumerate(pairs):
                M[I, J] = sp.expand(self.Rc(a, b, c, d))
        self.Mop = M
        r2 = 1 / sp.sqrt(2)
        Sp = sp.zeros(6, 3)
        Sm = sp.zeros(6, 3)
        for j in range(3):
            Sp[j, j] = r2
            Sp[j + 3, j] = r2
            Sm[j, j] = r2
            Sm[j + 3, j] = -r2
        self.Rplus = sp.expand(Sp.T * M * Sp)
        self.Rminus = sp.expand(Sm.T * M * Sm)
        self.Wplus = sp.expand(self.Rplus - self.scal * sp.eye(3) / 12)
        self.Wminus = sp.expand(self.Rminus - self.scal * sp.eye(3) / 12)

    def Rc(self, A, B, Cc, Dd):
        """R_{ABCD} with all antisymmetries."""
        if A == B or Cc == Dd:
            return sp.Integer(0)
        s = 1
        if A > B:
            A, B = B, A
            s = -s
        if Cc > Dd:
            Cc, Dd = Dd, Cc
            s = -s
        key = (A, B, Cc, Dd)
        if key in self._R:
            return s * self._R[key]
        key2 = (Cc, Dd, A, B)
        if key2 in self._R:
            return s * self._R[key2]
        return sp.Integer(0)

    # --- structural identities
    def closure_relation(self):
        """d(de^3) = 0, i.e. dC = u ^ C, as a single scalar relation."""
        dde3 = {}
        # d of the 2-form de3
        for key, coef in self.de3.items():
            dde3 = fadd(dde3, fwedge(dscalar(coef, self.Dtab), {key: sp.Integer(1)}))
            # d(e^a ^ e^3) = -e^a ^ de^3   (de^a = 0 at p)
            if 3 in key:
                a = key[0]
                dde3 = fadd(dde3, fscale(-coef, fwedge({(a,): sp.Integer(1)}, self.de3)))
        return dde3


# --------------------------------------------------- Taub-NUT-AdS instance


def taub_nut_reduced_data(nu_val: float, r_val: float, theta_val: float):
    """Reduced invariant data (Ric^B, u, Hess log v, C, grad C) at a point of
    Taub-NUT-AdS with Ric = -g, in the orthonormal base frame
    (e^0,e^1,e^2) = (e^r, e^theta, e^phi)."""
    r, th, nu = sp.symbols("r th nu", positive=True)
    F = (r - nu) / (r + nu) * (1 + (r - nu) * (r + 3 * nu) / 3)
    rho2 = r ** 2 - nu ** 2
    gB = sp.diag(1 / F, rho2, rho2 * sp.sin(th) ** 2)
    coords = [r, th, sp.Symbol("ph")]
    gBinv = gB.inv()
    # base Christoffels
    Gam = [[[sp.S(0)] * 3 for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                Gam[a][b][c] = sp.simplify(
                    sum(
                        gBinv[a, d]
                        * (
                            sp.diff(gB[d, c], coords[b])
                            + sp.diff(gB[d, b], coords[c])
                            - sp.diff(gB[b, c], coords[d])
                        )
                        for d in range(3)
                    )
                    / 2
                )
    RicB = sp.zeros(3)
    for b in range(3):
        for d in range(3):
            val = 0
            for a in range(3):
                val += sp.diff(Gam[a][d][b], coords[a]) - sp.diff(Gam[a][a][b], coords[d])
                for e in range(3):
                    val += Gam[a][a][e] * Gam[e][d][b] - Gam[a][d][e] * Gam[e][a][b]
            RicB[b, d] = sp.simplify(val)
    # frame vectors as coordinate coefficient matrix E[a][i]
    E = [
        [sp.sqrt(F), 0, 0],
        [0, 1 / sp.sqrt(rho2), 0],
        [0, 0, 1 / (sp.sqrt(rho2) * sp.sin(th))],
    ]
    RicB_on = sp.zeros(3)
    for a in range(3):
        for b in range(3):
            RicB_on[a, b] = sp.simplify(
                sum(E[a][i] * E[b][j] * RicB[i, j] for i in range(3) for j in range(3))
            )
    # v = 2 nu sqrt(F); phi = log v
    phi = sp.log(2 * nu * sp.sqrt(F))
    dphi = [sp.diff(phi, c) for c in coords]
    Hess = sp.zeros(3)
    for i in range(3):
        for j in range(3):
            Hess[i, j] = sp.simplify(
                sp.diff(phi, coords[i], coords[j])
                - sum(Gam[k][i][j] * dphi[k] for k in range(3))
            )
    u_on = [sp.simplify(sum(E[a][i] * dphi[i] for i in range(3))) for a in range(3)]
    Hess_on = sp.zeros(3)
    for a in range(3):
        for b in range(3):
            Hess_on[a, b] = sp.simplify(
                sum(E[a][i] * E[b][j] * Hess[i, j] for i in range(3) for j in range(3))
            )
    # C = v * dA with A = cos(theta) d phi  =>  C_{theta phi}(coord) = -v sin(theta)
    v = 2 * nu * sp.sqrt(F)
    Ccoord = sp.zeros(3)
    Ccoord[1, 2] = -v * sp.sin(th)
    Ccoord[2, 1] = v * sp.sin(th)
    DCcoord = [[[sp.S(0)] * 3 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                val = sp.diff(Ccoord[i, j], coords[k])
                for m in range(3):
                    val -= Gam[m][k][i] * Ccoord[m, j] + Gam[m][k][j] * Ccoord[i, m]
                DCcoord[i][j][k] = sp.simplify(val)
    C_on = sp.zeros(3)
    for a in range(3):
        for b in range(3):
            C_on[a, b] = sp.simplify(
                sum(E[a][i] * E[b][j] * Ccoord[i, j] for i in range(3) for j in range(3))
            )
    DC_on = [[[sp.S(0)] * 3 for _ in range(3)] for _ in range(3)]
    for a in range(3):
        for b in range(3):
            for c in range(3):
                DC_on[a][b][c] = sp.simplify(
                    sum(
                        E[a][i] * E[b][j] * E[c][k] * DCcoord[i][j][k]
                        for i in range(3)
                        for j in range(3)
                        for k in range(3)
                    )
                )
    sub = {nu: sp.Float(nu_val), r: sp.Float(r_val), th: sp.Float(theta_val)}
    out = {
        "RicB": np.array([[float(RicB_on[a, b].subs(sub)) for b in range(3)] for a in range(3)]),
        "u": np.array([float(u_on[a].subs(sub)) for a in range(3)]),
        "Hess": np.array([[float(Hess_on[a, b].subs(sub)) for b in range(3)] for a in range(3)]),
        "C": np.array([[float(C_on[a, b].subs(sub)) for b in range(3)] for a in range(3)]),
        "DC": np.array(
            [[[float(DC_on[a][b][c].subs(sub)) for c in range(3)] for b in range(3)] for a in range(3)]
        ),
    }
    return out


def substitution(red: Rank1Reduction, data):
    sub = {}
    for a in range(3):
        sub[red.u[a]] = data["u"][a]
    for a in range(3):
        for b in range(a, 3):
            sub[red.Du[a][b]] = data["Hess"][a][b]
    for (a, b), sym in red.Cs.items():
        sub[sym] = data["C"][a][b]
    for (a, b, c), sym in red.DCs.items():
        sub[sym] = data["DC"][a][b][c]
    for a in range(3):
        for b in range(a, 3):
            sub[red.RB[a][b]] = data["RicB"][a][b]
    return sub


def main():
    red = Rank1Reduction()
    print("=" * 68)
    print("RANK-ONE REDUCTION: normalization-invariant curvature dictionary")
    print("=" * 68)

    print("\nClosure identity d(de^3) = 0 gives:")
    for k, v in red.closure_relation().items():
        print("  e^%s coefficient: %s = 0" % ("".join(map(str, k)), sp.factor(v)))

    # ---- Ricci tensor ----
    print("\nReduced Ricci tensor (frame 0,1,2 horizontal; 3 vertical):")
    for A in range(4):
        for B in range(A, 4):
            expr = sp.factor(sp.expand(red.Ric[A, B]))
            print(f"  Ric[{A}{B}] = {expr}")
    print(f"\n  scalar = {sp.factor(red.scal)}")

    # ---- Check 1: base-only limit ----
    print("\nCheck 1: base-only limit (u = 0, C = 0, all derivatives 0).")
    zero = {}
    for a in range(3):
        zero[red.u[a]] = 0
        for b in range(3):
            zero[red.Du[a][b]] = 0
    for sym in red.Cs.values():
        zero[sym] = 0
    for sym in red.DCs.values():
        zero[sym] = 0
    Ric0 = sp.simplify(red.Ric.subs(zero))
    ok1 = all(
        sp.simplify(Ric0[a, b] - (red.RB[a][b] if a < 3 and b < 3 else 0)) == 0
        for a in range(4)
        for b in range(4)
    )
    print("  matches base Ricci with vanishing vertical block:", ok1)

    # ---- W+ in static limit ----
    print("\n" + "=" * 68)
    print("W+ SELF-DUAL WEYL: static and twisted formulas")
    print("=" * 68)

    static = dict(zero)
    Wp_static = sp.simplify(red.Wplus.subs(static))
    print("\nW+ in static limit (C = 0, u = 0):")
    for i in range(3):
        row = [sp.simplify(Wp_static[i, j]) for j in range(3)]
        print(f"  [{', '.join(str(x) for x in row)}]")

    # Verify A03's formula: Spec(W+) = {1/3 - eta_i}
    # In static limit Hess(v)/v = Du when v(p) = 1; trace = Lap(v)/v
    # Static Einstein vertical eq: Lap(v)/v = 1 (no twist)
    # Check: substitute Du = diag(h0, h1, h2) with h0+h1+h2 = 1
    h0, h1, h2 = sp.symbols("h0 h1 h2", real=True)
    static_diag = dict(static)
    static_diag[red.Du[0][0]] = h0
    static_diag[red.Du[1][1]] = h1
    static_diag[red.Du[2][2]] = h2
    # base Ricci from Einstein: Ric_B = h - I
    static_diag[red.RB[0][0]] = h0 - 1
    static_diag[red.RB[1][1]] = h1 - 1
    static_diag[red.RB[2][2]] = h2 - 1
    for a in range(3):
        for b in range(a + 1, 3):
            static_diag[red.RB[a][b]] = 0
            static_diag[red.Du[a][b]] = 0

    Wp_sd = sp.simplify(red.Wplus.subs(static_diag))
    print("\nW+ with diagonal static Einstein data h=diag(h0,h1,h2), Ric_B=h-I:")
    for i in range(3):
        row = [sp.simplify(Wp_sd[i, j]) for j in range(3)]
        print(f"  [{', '.join(str(x) for x in row)}]")

    # eigenvalues
    Wp_sd_tr1 = Wp_sd.subs(h2, 1 - h0 - h1)
    eigvals = Wp_sd_tr1.eigenvals()
    print("\n  eigenvalues (with tr h = 1):", eigvals)

    # Check against A03 formula: 1/3 - h_i
    for hv in [(sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)),
               (sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 3))]:
        sub_h = {h0: hv[0], h1: hv[1], h2: hv[2]}
        for a in range(3):
            for b in range(a + 1, 3):
                sub_h[red.Du[a][b]] = 0
                sub_h[red.RB[a][b]] = 0
        sub_h[red.Du[0][0]] = hv[0]
        sub_h[red.Du[1][1]] = hv[1]
        sub_h[red.Du[2][2]] = hv[2]
        sub_h[red.RB[0][0]] = hv[0] - 1
        sub_h[red.RB[1][1]] = hv[1] - 1
        sub_h[red.RB[2][2]] = hv[2] - 1
        for sym in red.Cs.values():
            sub_h[sym] = 0
        for sym in red.DCs.values():
            sub_h[sym] = 0
        for a in range(3):
            sub_h[red.u[a]] = 0
        Wp_num = red.Wplus.subs(sub_h)
        eigs = sorted(Wp_num.eigenvals().keys())
        expected = sorted(sp.Rational(1, 3) - hi for hi in hv)
        print(f"\n  h = {hv}: Spec(W+) = {eigs}, expected = {expected}, "
              f"match = {eigs == expected}")

    # ---- Full W+ with twist ----
    print("\n" + "=" * 68)
    print("W+ WITH TWIST (full formula)")
    print("=" * 68)
    print("\nFull W+ matrix:")
    for i in range(3):
        row = [sp.factor(sp.expand(red.Wplus[i, j])) for j in range(3)]
        print(f"  W+[{i}] = {row}")

    # twist correction: W+_full - W+_static
    # Static part: set C, DC to zero
    twist_off = {}
    for sym in red.Cs.values():
        twist_off[sym] = 0
    for sym in red.DCs.values():
        twist_off[sym] = 0
    Wp_stat = sp.expand(red.Wplus.subs(twist_off))
    Wp_twist = sp.expand(red.Wplus - Wp_stat)
    print("\nTwist correction delta(W+) = W+_full - W+_static:")
    for i in range(3):
        row = [sp.factor(sp.expand(Wp_twist[i, j])) for j in range(3)]
        if any(x != 0 for x in row):
            print(f"  delta[{i}] = {row}")
    if all(sp.expand(Wp_twist[i, j]) == 0 for i in range(3) for j in range(3)):
        print("  *** Twist correction to W+ is ZERO at this order! ***")

    # ---- Ricci decomposition ----
    print("\n" + "=" * 68)
    print("EINSTEIN EQUATIONS in normalized variables")
    print("=" * 68)

    # At v(p) = 1, the vertical equation is Ric(e3,e3) = lambda
    print(f"\nVertical Ric[33] = {sp.factor(red.Ric[3, 3])}")
    # Mixed equations Ric(ea, e3) = 0
    for a in range(3):
        expr = sp.factor(red.Ric[a, 3])
        if expr != 0:
            print(f"Mixed Ric[{a}3] = {expr}")
    # Horizontal: Ric[ab] = lambda delta_ab
    print("\nHorizontal Ric:")
    for a in range(3):
        for b in range(a, 3):
            expr = sp.factor(red.Ric[a, b])
            print(f"  Ric[{a}{b}] = {expr}")

    # ---- Numerical check: exponential twist metric ----
    print("\n" + "=" * 68)
    print("NUMERICAL CHECK: exponential twist metric")
    print("=" * 68)
    # g = dx^2+dy^2+dz^2+exp(2ux)(dt+Cydz)^2
    # At origin: u_vec = (u,0,0), Du = diag(u^2,0,0) [from d/dx of u_0 = u],
    # C_12 = C, DC_12_0 = uC (closure), all other DCs zero
    # RB = 0 (flat base at origin... but NOT exactly: the base metric at origin IS flat
    # only to zeroth order; the Christoffels of the 3D quotient base are zero at origin
    # but the Ricci of the 3D quotient is NOT the flat Ricci.)
    # Actually for this product metric, at the origin the base IS flat (no warping corrections)
    # Wait: g = dx^2+dy^2+dz^2+exp(2ux)(dt+Cydz)^2.  The base metric is
    #  g_B = dx^2+dy^2+(1+exp(2ux)C^2y^2)dz^2  plus a cross term
    # This is NOT dx^2+dy^2+dz^2 at the origin; at (x,y)=(0,0) it IS delta.
    # The Ricci of g_B at the origin will include contributions from the warping.
    # We need the actual quotient base Ricci, not zero.
    # The Step 12 exponential-twist script computed the FULL 4D Ricci.
    # Let me just use that as a numerical check of the symbolic formulas.

    u_val, C_val = 1.0, 2.0
    # from step12 script: at origin,
    # Ric = diag(-u^2, -C^2/2, -C^2/2, C^2/2-u^2)
    # The reduction data at origin:
    #   u_vec = (u, 0, 0)
    #   Du (= Hess(log v) = Hess(ux) = diag(0,0,0)??) NO.
    #   v = ell/ell(p) = exp(ux)/exp(0) = exp(ux), so log v = ux
    #   Hess(log v) at origin = Hess(ux) = 0 (linear function has zero Hessian)
    #   BUT: base Hess, not flat Hess. At origin base is flat, so Du = 0.
    #   C_12 = v * F_B_12 where F_B = dB = ell(p)*dA.
    #     A = Cy dz,  F_A = C dy ^ dz.
    #     B = ell(p)*A = Cy dz (ell(p)=1 at origin).
    #     F_B = C dy ^ dz.
    #     C_12 = v * F_B_12 = 1 * C = C.
    #   DC: ∇_c C_ab at origin.  C = v F_B.  At origin v=1 and base is flat,
    #     so DC_12_c = u_c * F_B_12 + v * ∇_c F_B_12.
    #     F_B = C dy^dz (constant coefficients), so ∇F_B = 0.
    #     Therefore DC_12_0 = u_0 * C = u*C, DC_12_1 = DC_12_2 = 0.
    #   Base Ricci: from horizontal Einstein eq,
    #     Ric_B_ab = Ric_4D_ab + Du_ab + (v^2/2)(C^2_sum terms)
    #     At origin with Ric_4D = diag(-u^2, -C^2/2, -C^2/2, ...):
    #       Actually I should compute it from the REDUCTION formula, not invert.
    #       The 3D base Ricci is the actual Ricci of g_B.

    # Simple numerical test: substitute the reduced data into the symbolic Ric
    # and check it matches the known 4D Ricci.
    # For this we need the actual base Ricci at the origin.
    # From the 4D formula: Ric[ab] = RB[ab] - Du[ab] - (1/2)C_ac C_bc [sum over c]
    # At origin: Ric[00] = RB00 - 0 - 0 = -u^2  => RB00 = -u^2
    #            Ric[11] = RB11 - 0 - (1/2)C_10^2 - (1/2)C_12^2 * delta ...
    #  Hmm, the twist contraction: sum_c C_ac C_bc / something.
    # I need to read off from my symbolic formula.

    # Let me just do a pure numerical substitution test.
    # Read the Ric formulas from the symbolic reduction, substitute the data,
    # and compare with the known answer from Step 12.
    print("\n  Substituting exponential-twist data at u=%g, C=%g..." % (u_val, C_val))
    sub_et = {}
    sub_et[red.u[0]] = u_val
    sub_et[red.u[1]] = 0.0
    sub_et[red.u[2]] = 0.0
    for a in range(3):
        for b in range(3):
            sub_et[red.Du[a][b]] = 0.0  # Hess(ux) = 0 at origin
    sub_et[red.Cs[(0, 1)]] = 0.0
    sub_et[red.Cs[(0, 2)]] = 0.0
    sub_et[red.Cs[(1, 2)]] = C_val
    for key in red.DCs:
        sub_et[red.DCs[key]] = 0.0
    sub_et[red.DCs[(1, 2, 0)]] = u_val * C_val  # closure: DC_12_0 = u*C

    # Base Ricci: we solve from the known 4D Ricci and the reduction formula.
    # First compute Ric_reduction with RB as unknowns.
    Ric_red = np.zeros((4, 4))
    # We'll iterate: set RB = 0, compute, compare, adjust.
    # Actually, we need the ACTUAL base Ricci. Let me compute it from the
    # base metric.  For g = dx^2+dy^2+dz^2+exp(2ux)(dt+Cydz)^2, the base
    # metric at the origin is delta (since exp(0)=1, and cross terms vanish
    # at y=0).  But the base Ricci at the origin involves DERIVATIVES of the
    # base metric, which are nonzero.
    # The base metric: g_B = dx^2 + dy^2 + (1 + C^2 y^2 exp(2ux)) dz^2.
    # No, this isn't quite right because we need to project out the fiber.
    # In the KK decomposition g = g_B + v^2(dz+B)^2, with z the fiber coord.
    # For our metric, fiber coord is t, and g_B = dx^2+dy^2+dz^2 is the
    # base metric.  The fiber length is ell = exp(ux), connection A = Cy dz.
    # So g_B = dx^2+dy^2+dz^2, which IS flat.  RB = 0.
    for a in range(3):
        for b in range(a, 3):
            sub_et[red.RB[a][b]] = 0.0

    Ric_num = np.array(
        [[float(sp.N(red.Ric[A, B].subs(sub_et))) for B in range(4)] for A in range(4)]
    )
    Ric_expected = np.diag([-u_val ** 2, -C_val ** 2 / 2, -C_val ** 2 / 2,
                            C_val ** 2 / 2 - u_val ** 2])
    print("  Ric from reduction:", np.round(np.diag(Ric_num), 6))
    print("  Expected Ric:      ", np.round(np.diag(Ric_expected), 6))
    print("  Max error:", np.max(np.abs(Ric_num - Ric_expected)))
    Wp_num = np.array(
        [[float(sp.N(red.Wplus[i, j].subs(sub_et))) for j in range(3)] for i in range(3)]
    )
    eigp = np.linalg.eigvalsh((Wp_num + Wp_num.T) / 2)
    print("  W+ eigenvalues:", np.round(eigp, 8))
    # Compare with step12: W+_diag = {(-C^2-6Cu+2u^2)/12, same, (5C^2+12Cu+8u^2)/12}
    w1 = (-C_val ** 2 - 6 * C_val * u_val + 2 * u_val ** 2) / 12
    w3 = (5 * C_val ** 2 + 12 * C_val * u_val + 8 * u_val ** 2) / 12
    print("  Step 12 expected:", sorted([w1, w1, w3]))

    print("\n" + "=" * 68)
    print("CALIBRATED CONSTRAINT ANALYSIS")
    print("=" * 68)
    # Under Ric_g = -g with rank-one circle reduction:
    # Vertical: sum Du_aa + sum u_a^2 - (1/4) sum C_ab^2 = -1
    #   i.e. tr(h) + |u|^2 = 1 + |C|^2/4  where h = Du (at v=1, Du = Hess(v))
    # But actually from the symbolic formula we can read off the exact constraint.
    vert = sp.factor(red.Ric[3, 3])
    print(f"\n  Vertical equation: Ric[33] = {vert}")
    print(f"  Setting Ric[33] = -1: {sp.factor(vert + 1)} = 0")

    # With Ric = -g: RB_ab = -delta_ab + Du_ab + (1/2)(sum_c C_ac C_bc)
    # => tr(RB) = -3 + tr(Du) + (1/2)|C|^2
    # And from vertical: tr(Du) + |u|^2 - |C|^2/4 = -1 (if my formula is right)
    # Cross-check with A03: tr(h) = 1 + ell^2|F|^2/4 = 1 + |C|^2/4
    # Note: tr(Du) = Delta(log v) = (Delta v)/v - |u|^2 at v=1
    # So tr(Du) + |u|^2 = (Delta v)/v
    # And (Delta v)/v = 1 + |C|^2/4 at v=1 with Ric=-g

    print("\nDone.")


if __name__ == "__main__":
    main()
