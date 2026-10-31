#!/usr/bin/env python3
"""Algebra only: literal-projection model, not Leung sign identification."""

import sympy as s


def main():
    x, y, z, t = s.symbols("x y z t", real=True)
    v = s.Matrix([x + s.I * y, z + s.I * t])
    jv = s.Matrix([[-v[1], v[0]]])
    vv = v * v.conjugate().T
    norm = s.expand((v.conjugate().T * v)[0])
    identity = jv.conjugate().T * jv - (norm * s.eye(2) - vv)
    assert identity.applyfunc(s.simplify) == s.zeros(2)
    q = vv - s.trace(vv) * s.eye(2) / 2
    dual = jv.conjugate().T * jv
    dual -= s.trace(dual) * s.eye(2) / 2
    assert (dual + q).applyfunc(s.simplify) == s.zeros(2)
    print("PASS [algebra only]: wedge-dual trace-free Hermitian identity")

    a, b, c, d = s.symbols("a b c d")
    u = s.Matrix([[a, b], [c, d]])
    uv = u * v
    juv = s.Matrix([[-uv[1], uv[0]]])
    # j(Uv) U = det(U) j(v), polynomial form of frame covariance.
    assert (juv * u - u.det() * jv).applyfunc(s.simplify) == s.zeros(1, 2)
    print("PASS [algebra only]: determinant-twisted frame covariance")

    bconn, lconn = s.symbols("B D_L")
    aconn = (bconn + lconn) / 2
    assert s.expand(2 * aconn - lconn - bconn) == 0
    assert s.expand(-lconn / 2 + aconn - bconn / 2) == 0
    print("PASS [algebra only]: active-line determinant charge 2 A - D_L")

    h = s.symbols("h")
    scale = s.symbols("scale", positive=True)
    projected_defect = s.expand((h + h) / 2 + scale * h)
    assert s.simplify(projected_defect - (1 + scale) * h) == 0
    assert (1 + scale).is_positive
    iv = s.I * v
    assert (iv * iv.conjugate().T - vv).applyfunc(s.simplify) == s.zeros(2)
    alternative_defect = s.expand((h + h) / 2 - scale * h)
    assert s.simplify(alternative_defect.subs(scale, 1)) == 0
    print("PASS [algebra only]: model residual bound; alternative sign cancels harmonic residual")
    print("NOT CHECKED: identification of model sign with published Leung equations")


if __name__ == "__main__":
    main()
