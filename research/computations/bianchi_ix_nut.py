#!/usr/bin/env python3
"""Exact finite algebra for the regular SU(2)-invariant Einstein--AK nut.

Requires Python 3, SymPy and Singular with primdec.lib. Run::

    python research/computations/bianchi_ix_nut.py
    python research/computations/bianchi_ix_nut.py --output /tmp/nut.json

The normalization is Ric = -3 g and d sigma_i = 2 sigma_j wedge sigma_k.
With u=t^2 and a_i=t f_i(u), set H_i=1+2u f_i'/f_i and
Z_i=f_i/(f_j f_k). The Einstein equations are

    2u H_i' - H_i + H_i sum(H) - 2[Z_i^2-(Z_j-Z_k)^2] - 3u = 0.

For Omega=sum(x_i omega_i), closure gives
u (x_i^2)'=(2Z_i-H_j-H_k)x_i^2. Constant length requires sum(x_i^2)=1.

This program derives the first five length constraints over Q and verifies
their radical ideal against the three Kähler support lines. Nonnegative
initial weights select the vertices of those lines. All-order uniqueness
then follows from the nonzero recurrence eigenvalues and analytic regularity,
as proved in docs/GOLDBERG.md; it is not inferred from finite truncation alone.
"""

import argparse
import json
import subprocess
from pathlib import Path

from sympy.polys.domains import QQ
from sympy.polys.rings import ring


ORDER = 5
RING, D1, D2, R1, R2 = ring("d1,d2,R1,R2", QQ)
ZERO = RING.zero
ONE = RING.one


def constant(value):
    return [RING(value)] + [ZERO] * ORDER


def add(*series):
    return [sum((s[k] for s in series), ZERO) for k in range(ORDER + 1)]


def scale(c, series):
    return [c * value for value in series]


def multiply(a, b):
    return [sum((a[j] * b[k - j] for j in range(k + 1)), ZERO)
            for k in range(ORDER + 1)]


def inverse(a):
    # Only f_i(0)=1 and their products are inverted.
    if a[0] != ONE:
        raise ValueError("A normalized nut series must have constant term one")
    result = [ONE] + [ZERO] * ORDER
    for k in range(1, ORDER + 1):
        result[k] = -sum((a[j] * result[k - j] for j in range(1, k + 1)), ZERO)
    return result


def u_derivative(a):
    return [k * a[k] for k in range(ORDER + 1)]


def geometry(f):
    H = [add(constant(1), scale(2, multiply(u_derivative(fi), inverse(fi))))
         for fi in f]
    Z = [multiply(f[i], inverse(multiply(f[(i + 1) % 3], f[(i + 2) % 3])))
         for i in range(3)]
    sum_H = add(*H)
    minus_3u = [ZERO, -3 * ONE] + [ZERO] * (ORDER - 1)
    equations = []
    for i in range(3):
        j, k = (i + 1) % 3, (i + 2) % 3
        difference = add(Z[j], scale(-1, Z[k]))
        equations.append(add(
            scale(2, u_derivative(H[i])), scale(-1, H[i]),
            multiply(H[i], sum_H), scale(-2, multiply(Z[i], Z[i])),
            scale(2, multiply(difference, difference)), minus_3u,
        ))
    constraint = add(
        *(multiply(H[i], H[j]) for i in range(3) for j in range(i + 1, 3)),
        *(multiply(z, z) for z in Z),
        *(scale(-2, multiply(Z[i], Z[j]))
          for i in range(3) for j in range(i + 1, 3)),
        minus_3u,
    )
    transport = [add(scale(2, Z[i]), scale(-1, H[(i + 1) % 3]),
                     scale(-1, H[(i + 2) % 3])) for i in range(3)]
    return equations, constraint, transport


def exact_constraints():
    anisotropy = [D1, D2, -D1 - D2]
    f = [[ONE, RING(QQ(1, 6)) + d] + [ZERO] * (ORDER - 1)
         for d in anisotropy]
    for n in range(2, ORDER + 1):
        equations, _, _ = geometry(f)
        residual = [equations[i][n] for i in range(3)]
        # Linear recurrence = a I + b 11^T. Its trace-free and trace
        # eigenvalues are a and a+3b, respectively.
        a, b = 4 * (n + 2) * (n - 1), 2 * (n + 2)
        total = sum(residual, ZERO)
        for i in range(3):
            f[i][n] = -QQ(1, a) * residual[i] + QQ(b, a * (a + 3 * b)) * total

    equations, constraint, transport = geometry(f)
    if any(value for e in equations for value in e) or any(constraint):
        raise ArithmeticError("The exact Einstein recurrence did not close")

    weights = [R1, R2, ONE - R1 - R2]
    X = [[weight] + [ZERO] * ORDER for weight in weights]
    length = []
    for n in range(1, ORDER + 1):
        for i in range(3):
            X[i][n] = QQ(1, n) * sum(
                (transport[i][k] * X[i][n - k] for k in range(1, n + 1)), ZERO)
        length.append(sum((X[i][n] for i in range(3)), ZERO))
    return f, length


def singular_source(length):
    polynomials = ",\n".join(str(p).replace("**", "^") for p in length)
    return f'''LIB "primdec.lib";
option(redSB);
ring r=0,(R1,R2,d1,d2),dp;
ideal I={polynomials};
ideal K1=6*d1-1,12*d2+1,R1-1;
ideal K2=12*d1+1,6*d2-1,R2-1;
ideal K3=12*d1+1,12*d2+1,R1+R2;
ideal actual=std(radical(I));
ideal expected=std(intersect(K1,intersect(K2,K3)));
if (size(reduce(actual,expected))==0 && size(reduce(expected,actual))==0)
{{ print("NUT_RADICAL_EQUALITY_OK"); }}
else {{ print("NUT_RADICAL_EQUALITY_FAILED"); }}
quit;
'''


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--singular", default="Singular", help="Singular executable")
    parser.add_argument("--output", type=Path, help="Optional exact coefficient JSON")
    args = parser.parse_args()
    f, length = exact_constraints()
    source = singular_source(length)
    result = subprocess.run([args.singular, "-q"], input=source, text=True,
                            capture_output=True, check=True)
    if "NUT_RADICAL_EQUALITY_OK" not in result.stdout.splitlines():
        raise RuntimeError("Singular did not establish the radical equality:\n"
                           + result.stdout + result.stderr)
    if args.output:
        report = {
            "normalization": "Ric=-3g; u=t^2; a_i=t*f_i; sum R_i=1",
            "order": ORDER,
            "metric_coefficients": [[str(c) for c in fi] for fi in f],
            "length_constraints": [str(c) for c in length],
            "radical": [
                ["6*d1-1", "12*d2+1", "R1-1"],
                ["12*d1+1", "6*d2-1", "R2-1"],
                ["12*d1+1", "12*d2+1", "R1+R2"],
            ],
            "einstein_recurrence_residual": "zero over Q[d1,d2]",
            "radical_equality": True,
        }
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print("Exact Einstein recurrence and five length constraints verified.")
    print("The radical is the union of the three Kähler support lines.")
    print("Nonnegative weights select their Kähler vertices; see the all-order proof.")


if __name__ == "__main__":
    main()
