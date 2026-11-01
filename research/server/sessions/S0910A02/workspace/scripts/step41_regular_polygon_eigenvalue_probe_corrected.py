#!/usr/bin/env python3
"""Step 41 corrected FEM probe for constant-curvature diagonal toric polygons.

Correction relative to the first Step-41 probe: the Poincare disk metric is
    g = lambda2 * (dx^2+dy^2),  lambda2 = 4/(1-r^2)^2.
In dimension 2 the Dirichlet energy is conformally invariant, while the L2 mass
is weighted by lambda2, not lambda2^2. The earlier script incorrectly squared
this weight; this file supersedes it.

Mathematical target (constant-K subansatz only, not a proof): for curvature -A
and Einstein constant Lambda=1, a constant-curvature diagonal Einstein polygon
would require simultaneously
    side match:    pi/sqrt(1+2A) = s_unit(m)/sqrt(A),
    eigenvalue:    lambda1(Polygon_{K=-A}) = 2.
Since lambda1 scales as A*lambda1_unit, the eigenvalue requirement is
    A_eig = 2/lambda1_unit.
"""
import json, math, os
import numpy as np
from scipy.spatial import Delaunay
from scipy.sparse.linalg import eigsh
from skfem import MeshTri, Basis, ElementTriP1, asm, condense
from skfem import BilinearForm
from shapely.geometry import Point, Polygon

OUT = "Sessions/S0910A02/workspace/data/step41_regular_polygon_eigenvalue_probe_corrected.json"
os.makedirs(os.path.dirname(OUT), exist_ok=True)


def side_unit(m: int) -> float:
    return 2.0 * math.acosh(math.sqrt(2.0) * math.cos(math.pi / m))


def A_match_side(m: int) -> float:
    s = side_unit(m)
    return s * s / (math.pi * math.pi - 2.0 * s * s)


def circumradius_unit(m: int) -> float:
    # Hyperbolic right triangle center--midpoint--vertex: angle at vertex pi/4,
    # center angle pi/m, right angle at side midpoint, hence cosh R=cot(pi/m).
    return math.acosh(1.0 / math.tan(math.pi / m))


def geodesic_circle_center(z1: complex, z2: complex):
    A = np.array([[2*z1.real, 2*z1.imag], [2*z2.real, 2*z2.imag]], dtype=float)
    b = np.array([abs(z1)**2 + 1.0, abs(z2)**2 + 1.0], dtype=float)
    c = np.linalg.solve(A, b)
    R = math.sqrt(float(np.dot(c, c) - 1.0))
    return c[0] + 1j*c[1], R


def arc_points_inside(z1: complex, z2: complex, n: int):
    c, R = geodesic_circle_center(z1, z2)
    a1 = math.atan2((z1-c).imag, (z1-c).real)
    a2 = math.atan2((z2-c).imag, (z2-c).real)
    def normalize_delta(d):
        while d <= -math.pi:
            d += 2*math.pi
        while d > math.pi:
            d -= 2*math.pi
        return d
    d_short = normalize_delta(a2-a1)
    candidates = [d_short, d_short - 2*math.pi if d_short > 0 else d_short + 2*math.pi]
    best = None
    for d in candidates:
        mid = c + R * complex(math.cos(a1 + 0.5*d), math.sin(a1 + 0.5*d))
        score = abs(mid)
        if best is None or score < best[0]:
            best = (score, d)
    d = best[1]
    pts = []
    for k in range(n):  # omit endpoint to avoid duplicates
        t = k / float(n)
        ang = a1 + d * t
        z = c + R * complex(math.cos(ang), math.sin(ang))
        pts.append((z.real, z.imag))
    return pts


def boundary_polygon_points(m: int, per_edge: int):
    R = circumradius_unit(m)
    rho = math.tanh(R/2.0)
    verts = [rho * complex(math.cos(2*math.pi*j/m), math.sin(2*math.pi*j/m)) for j in range(m)]
    pts = []
    for j in range(m):
        pts.extend(arc_points_inside(verts[j], verts[(j+1)%m], per_edge))
    return np.array(pts, dtype=float)


def make_mesh(m: int, per_edge=56, grid_n=70):
    bpts = boundary_polygon_points(m, per_edge)
    poly = Polygon(bpts)
    minx, miny, maxx, maxy = poly.bounds
    interior = []
    xs = np.linspace(minx, maxx, grid_n)
    ys = np.linspace(miny, maxy, grid_n)
    for x in xs:
        for y in ys:
            p = Point(float(x), float(y))
            if poly.contains(p) and poly.exterior.distance(p) > 1e-5:
                interior.append((float(x), float(y)))
    pts = np.vstack([bpts, np.array(interior, dtype=float)])
    tri = Delaunay(pts)
    keep = []
    for simp in tri.simplices:
        centroid = pts[simp].mean(axis=0)
        if poly.contains(Point(float(centroid[0]), float(centroid[1]))):
            keep.append(simp)
    mesh = MeshTri(pts.T, np.array(keep, dtype=int).T)
    boundary_nodes = np.arange(len(bpts), dtype=int)
    return mesh, boundary_nodes, len(interior)


@BilinearForm
def laplace(u, v, w):
    return u.grad[0] * v.grad[0] + u.grad[1] * v.grad[1]


@BilinearForm
def hyperbolic_mass(u, v, w):
    r2 = w.x[0]**2 + w.x[1]**2
    lambda2 = 4.0 / (1.0 - r2)**2
    return lambda2 * u * v


def lambda1_unit(m: int, per_edge=56, grid_n=70):
    mesh, boundary_nodes, nint = make_mesh(m, per_edge=per_edge, grid_n=grid_n)
    basis = Basis(mesh, ElementTriP1())
    K = asm(laplace, basis)
    M = asm(hyperbolic_mass, basis)
    Kc, Mc, _, _ = condense(K, M, D=boundary_nodes)
    vals = eigsh(Kc, k=3, M=Mc, sigma=0.0, which='LM', return_eigenvectors=False)
    vals = np.sort(vals)
    return float(vals[0]), mesh.p.shape[1], mesh.t.shape[1], nint


def evaluate_case(m: int, per_edge: int, grid_n: int):
    lam, nv, nt, nint = lambda1_unit(m, per_edge=per_edge, grid_n=grid_n)
    A_side = A_match_side(m)
    A_eig = 2.0 / lam
    L_at_eig = math.pi / math.sqrt(1.0 + 2.0*A_eig)
    s_at_eig = side_unit(m) / math.sqrt(A_eig)
    return {
        "lambda1_unit_curvature_minus1": lam,
        "A_eig_for_lambda1_2": A_eig,
        "A_match_side": A_side,
        "relative_A_gap_Aeig_over_Aside_minus1": A_eig / A_side - 1.0,
        "lambda1_at_side_match": A_side * lam,
        "lambda1_defect_at_side_minus_2": A_side * lam - 2.0,
        "rod_over_side_at_Aeig": L_at_eig / s_at_eig,
        "rod_side_defect_at_Aeig_percent": (L_at_eig / s_at_eig - 1.0) * 100.0,
        "vertices": nv,
        "triangles": nt,
        "interior_grid_points": nint,
        "per_edge": per_edge,
        "grid_n": grid_n,
    }


def main():
    results = {
        "scope": "Corrected numerical FEM probe for constant-curvature right-angled hyperbolic m-gons; not proof.",
        "supersedes": "Sessions/S0910A02/workspace/data/step41_regular_polygon_eigenvalue_probe.json used lambda2^2 mass weight and is invalid.",
        "criterion": "constant-K diagonal Einstein with Λ=1 requires A_match_side(m)=2/lambda1_unit(m)",
        "metric_weight": "Poincare disk g=lambda2*(dx^2+dy^2), lambda2=4/(1-r^2)^2; mass uses lambda2, energy is Euclidean.",
        "main_cases": {},
        "m6_convergence": []
    }
    # Main cases at one moderately fine resolution.
    for m in [5, 6, 8, 10, 12]:
        results["main_cases"][str(m)] = evaluate_case(m, per_edge=60, grid_n=76)
    # m=6 convergence check.
    for pe, gn in [(32, 44), (44, 58), (56, 72), (70, 90)]:
        results["m6_convergence"].append(evaluate_case(6, per_edge=pe, grid_n=gn))
    with open(OUT, 'w') as f:
        json.dump(results, f, indent=2)
    print(json.dumps({
        "output": OUT,
        "main_cases": {k: {"lambda1_unit": v["lambda1_unit_curvature_minus1"],
                              "A_eig": v["A_eig_for_lambda1_2"],
                              "A_side": v["A_match_side"],
                              "lambda1_at_side": v["lambda1_at_side_match"],
                              "rod_side_defect_at_Aeig_percent": v["rod_side_defect_at_Aeig_percent"]}
                        for k, v in results["main_cases"].items()},
        "m6_convergence_lambda1": [v["lambda1_unit_curvature_minus1"] for v in results["m6_convergence"]]
    }, indent=2))

if __name__ == "__main__":
    main()
