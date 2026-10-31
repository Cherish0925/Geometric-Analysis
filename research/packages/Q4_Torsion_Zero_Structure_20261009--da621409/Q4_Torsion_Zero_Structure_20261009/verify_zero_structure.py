#!/usr/bin/env python3
"""Exact algebra for Q4_Torsion_Zero_Structure.tex.

Requires Python 3.10+ and SymPy. This checks finite tensor/polynomial
identities, not the existence of an almost-Kaehler Einstein metric.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp


def require_zero(expression: sp.Expr, name: str) -> None:
    value = sp.factor(sp.cancel(sp.expand(expression)))
    if value != 0:
        raise AssertionError(f"{name}: nonzero residual {value}")


def twoform(entries: list[tuple[int, int, int]]) -> sp.Matrix:
    result = sp.zeros(4)
    for i, j, value in entries:
        result[i, j] = value
        result[j, i] = -value
    return result


def form_inner(left: sp.Matrix, right: sp.Matrix) -> sp.Expr:
    return sp.trace(left.T * right) / 2


def verify() -> dict[str, object]:
    O = twoform([(0, 1, 1), (2, 3, 1)])
    F = twoform([(0, 2, 1), (1, 3, -1)])
    H = twoform([(0, 3, 1), (1, 2, 1)])
    anti = [twoform([(0, 1, 1), (2, 3, -1)]),
            twoform([(0, 2, 1), (1, 3, 1)]),
            twoform([(0, 3, 1), (1, 2, -1)])]
    # J alpha = -alpha o J; O stores two-form components, not the
    # column-action endomorphism, which is -O.
    J = -O
    generic = sp.Matrix(4, 4, sp.symbols("k0:16"))
    da = generic - generic.T  # row = derivative index
    dJa = generic * J.T - J * generic.T
    linear_equations = [form_inner(da, a) for a in anti]
    linear_equations += [form_inner(dJa, a) for a in anti]
    coefficient_matrix, _ = sp.linear_eq_to_matrix(linear_equations, list(generic))
    assert coefficient_matrix.rank() == 6

    ell, em, p, q, r, t, u, v, w, z = sp.symbols(
        "ell em p q r t u v w z", real=True)
    K = sp.Matrix([[ell+p, em+q, u, v],
                   [-em+q, ell-p, v, -u],
                   [r, t, ell+w, em+z],
                   [t, -r, -em+z, ell-w]])
    A = sp.Matrix([[p+sp.I*q, r+sp.I*t],
                   [u+sp.I*v, w+sp.I*z]])
    c2 = ell**2 + em**2
    A2 = sp.expand_complex(sp.trace(A.conjugate().T*A))
    T = sp.expand_complex(sp.trace(A*A.conjugate()))
    detA2 = sp.expand_complex(A.det()*sp.conjugate(A.det()))
    da = K-K.T
    dJa = K*J.T-J*K.T
    for i, alpha in enumerate(anti):
        require_zero(form_inner(da, alpha), f"da ASD {i}")
        require_zero(form_inner(dJa, alpha), f"dJa ASD {i}")

    # R(phi)=-d(Ja), R(Jphi)=-da at a torsion zero.
    Rp, Rh = -dJa, -da
    r12, r13 = form_inner(Rp, O)/2, form_inner(Rh, O)/2
    r22, r23, r33 = form_inner(Rp, F)/2, form_inner(Rp, H)/2, form_inner(Rh, H)/2
    require_zero(form_inner(Rh,F)/2-r23, "curvature symmetry")
    require_zero(r22+r33, "transverse curvature trace")
    require_zero(r12+2*ell, "r12")
    require_zero(r13+2*em, "r13")
    eta2 = 2*(r12**2+r13**2)
    V2 = r22**2+2*r23**2+r33**2
    L2 = sp.trace(K.T*K)
    require_zero(eta2-8*c2, "eta norm")
    require_zero(L2-4*c2-2*A2, "real derivative norm")
    require_zero(V2-2*((r-u)**2+(t-v)**2), "V norm")
    require_zero(4*L2-4*V2+6*eta2-8*(T+8*c2), "zero balance")
    require_zero(K.det()-(c2**2-c2*T+detA2), "real determinant")
    Sym = (A+A.T)/2
    Sym2 = sp.expand_complex(sp.trace(Sym.conjugate().T*Sym))
    require_zero(V2-4*eta2-4*Sym2+4*(T+8*c2), "spectral balance")
    sharp = {p:0,q:0,r:2*ell,t:0,u:-2*ell,v:0,w:0,z:0,em:0}
    require_zero((T+8*c2).subs(sharp), "algebraic equality input")
    require_zero((K.det()-25*c2**2).subs(sharp), "determinant equality")
    require_zero((V2-4*eta2).subs(sharp), "spectral equality")

    # The local scalar identity on the supplied explicit noncompact model.
    x = sp.symbols("x", positive=True)
    D = 1+3*x*x
    G = 4*D/((1-x)**2*(1+x)**2*(3*x-1)*(3*x+1))
    vol = 64*x*D/(3*(1-x*x)**3)
    torsion = 36*(1-x*x)**3/D**3
    X1 = (1-x)**3*(3*x+1)/(16*x**3)
    X2 = (1+x)**3*(3*x-1)/(16*x**3)
    rr = [
        -3*(x-1)**2*(21*x**4+18*x**3+12*x*x-2*x-1)/D**3,
        -3*(x+1)**2*(21*x**4-18*x**3+12*x*x+2*x-1)/D**3,
        9*(x-1)**2*(x+1)**2*(5*x*x-1)/D**3,
    ]
    W = [a+1 for a in rr]
    tau = -2+torsion/4
    eta_sq = sp.factor(2*(X1*(W[0]-tau)**2+X2*(W[1]-tau)**2))
    V_sq = sp.factor(sum(a*a for a in W)-sp.Rational(3,2)*tau*tau-eta_sq)
    theta_x = sp.factor((W[0]-tau)*sp.diff(X1,x)+(W[1]-tau)*sp.diff(X2,x))
    div_theta = sp.diff(vol*theta_x/G,x)/vol
    lap_q = -sp.diff(vol*sp.diff(torsion,x)/G,x)/vol
    require_zero(lap_q/4+2*div_theta-sp.Rational(3,2)*torsion
                 +sp.Rational(3,16)*torsion**2+eta_sq+2*V_sq,
                 "scalar current identity on supplied model")
    return {
        "linear_constraints_rank": 6,
        "real_derivative_dimension": 10,
        "torsion_zero_balance": "exact",
        "curvature_and_complex_norms": "exact",
        "real_determinant_formula": "exact",
        "spectral_square_formula": "exact",
        "algebraic_equality_case": "exact; not a metric construction",
        "scalar_current_model_residual": "0",
        "scope": "finite identities only; no metric existence or Goldberg proof"
    }


if __name__ == "__main__":
    result = verify()
    text = json.dumps(result, ensure_ascii=False, indent=2)
    print(text)
    Path(__file__).with_name("verification.json").write_text(text+"\n", encoding="utf-8")
