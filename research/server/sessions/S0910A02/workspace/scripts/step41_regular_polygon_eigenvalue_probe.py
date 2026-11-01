#!/usr/bin/env python3
"""Step 41: finite-element probe for constant-curvature diagonal toric polygons.

For a diagonal positive Einstein metric with constant orbit curvature K_Σ=-A and
Einstein constant Λ=1, Liu Lemma 5.1 gives every edge length
    L_rod(A) = π / sqrt(1+2A).
A regular right-angled hyperbolic m-gon of curvature -A has side
    s_m(A)=s_m(1)/sqrt(A).
The orbit volume φ must also be the principal Dirichlet eigenfunction with
    λ1(Σ_A)=2.
Because λ1 scales as A times the λ1 of the curvature -1 polygon, a constant-K
solution would require simultaneously
    A = A_match_side(m) and A = A_eig(m)=2/λ1_unit(m).
Step 40 used Faber--Krahn only; this script approximates λ1_unit(m) directly for
regular right-angled hyperbolic polygons in the Poincare disk.

This is only a numerical probe, not a proof. It is meant to test whether the
constant-curvature subansatz is plausibly inconsistent and to quantify the gap.
"""
import json, math, os
import numpy as np
from scipy.spatial import Delaunay
from scipy.sparse.linalg import eigsh
from skfem import MeshTri, Basis, ElementTriP1, asm, condense
from skfem import BilinearForm
from shapely.geometry import Point, Polygon

OUT = "Sessions/S0910A02/workspace/data/step41_regular_polygon_eigenvalue_probe.json"
os.makedirs(os.path.dirname(OUT), exist_ok=True)


def side_unit(m: int) -> float:
    return 2.0 * math.acosh(math.sqrt(2.0) * math.cos(math.pi / m))


def A_match_side(m: int) -> float:
    s = side_unit(m)
    return s * s / (math.pi * math.pi - 2.0 * s * s)


def circumradius_unit(m: int) -> float:
    # Right triangle: center angle pi/m, vertex half-angle pi/4, right angle at side midpoint.
    # cosh R = cot(pi/m) cot(pi/4) = cot(pi/m).
    return math.acosh(1.0 / math.tan(math.pi / m))


def geodesic_circle_center(z1: complex, z2: complex):
    # Circle center c=(cx,cy) orthogonal to unit circle and passing through z1,z2.
    # 2 z_i dot c = |z_i|^2 + 1.
    A = np.array([[2*z1.real, 2*z1.imag], [2*z2.real, 2*z2.imag]], dtype=float)
    b = np.array([abs(z1)**2 + 1.0, abs(z2)**2 + 1.0], dtype=float)
    c = np.linalg.solve(A, b)
    R = math.sqrt(float(np.dot(c, c) - 1.0))
    return c[0] + 1j*c[1], R


def arc_points_inside(z1: complex, z2: complex, n: int):
    c, R = geodesic_circle_center(z1, z2)
    a1 = math.atan2((z1-c).imag, (z1-c).real)
    a2 = math.atan2((z2-c).imag, (z2-c).real)
    # two candidate arcs from a1 to a2; choose the one whose midpoint lies inside unit disk.
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
    for k in range(n):
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


def make_mesh(m: int, per_edge=52, grid_n=62):
    bpts = boundary_polygon_points(m, per_edge)
    poly = Polygon(bpts)
    minx, miny, maxx, maxy = poly.bounds
    interior = []
    xs = np.linspace(minx, maxx, grid_n)
    ys = np.linspace(miny, maxy, grid_n)
    for x in xs:
        for y in ys:
            p = Point(float(x), float(y))
            # avoid placing interior points too close to boundary approximation
            if poly.contains(p) and poly.exterior.distance(p) > 1e-4:
                interior.append((float(x), float(y)))
    pts = np.vstack([bpts, np.array(interior, dtype=float)])
    tri = Delaunay(pts)
    keep = []
    for simp in tri.simplices:
        centroid = pts[simp].mean(axis=0)
        if poly.contains(Point(float(centroid[0]), float(centroid[1]))):
            keep.append(simp)
    keep = np.array(keep, dtype=int)
    # skfem expects p shape (2,nvertices), t shape (3,nelements)
    mesh = MeshTri(pts.T, keep.T)
    boundary_nodes = np.arange(len(bpts), dtype=int)
    return mesh, boundary_nodes, len(interior)


@BilinearForm
def laplace(u, v, w):
    return u.grad[0] * v.grad[0] + u.grad[1] * v.grad[1]


@BilinearForm
def hyperbolic_mass(u, v, w):
    r2 = w.x[0]**2 + w.x[1]**2
    omega = 4.0 / (1.0 - r2)**2
    return (omega**2) * u * v


def lambda1_unit(m: int, per_edge=52, grid_n=62):
    mesh, boundary_nodes, nint = make_mesh(m, per_edge=per_edge, grid_n=grid_n)
    basis = Basis(mesh, ElementTriP1())
    K = asm(laplace, basis)
    M = asm(hyperbolic_mass, basis)
    Kc, Mc, _, _ = condense(K, M, D=boundary_nodes)
    vals = eigsh(Kc, k=3, M=Mc, sigma=0.0, which='LM', return_eigenvectors=False)
    vals = np.sort(vals)
    return float(vals[0]), mesh.p.shape[1], mesh.t.shape[1], nint


def main():
    results = {
        "scope": "Numerical FEM probe for constant-curvature right-angled hyperbolic m-gons; not proof.",
        "criterion": "constant-K diagonal Einstein with Λ=1 requires A_match_side(m)=2/lambda1_unit(m)",
        "mesh_notes": "Poincare disk, geodesic arcs approximated by boundary samples; P1 FEM; conformal invariance makes stiffness Euclidean and mass weighted by hyperbolic area factor.",
        "cases": {}
    }
    for m in [5, 6, 8, 10, 12]:
        lam, nv, nt, nint = lambda1_unit(m)
        A_side = A_match_side(m)
        A_eig = 2.0 / lam
        L_at_eig = math.pi / math.sqrt(1.0 + 2.0*A_eig)
        s_at_eig = side_unit(m) / math.sqrt(A_eig)
        ratio_at_eig = L_at_eig / s_at_eig
        lam_at_side = A_side * lam
        results["cases"][str(m)] = {
            "lambda1_unit_curvature_minus1": lam,
            "A_eig_for_lambda1_2": A_eig,
            "A_match_side": A_side,
            "relative_A_gap_Aeig_over_Aside_minus1": A_eig / A_side - 1.0,
            "lambda1_at_side_match": lam_at_side,
            "lambda1_defect_at_side_minus_2": lam_at_side - 2.0,
            "rod_over_side_at_Aeig": ratio_at_eig,
            "rod_side_defect_at_Aeig_percent": (ratio_at_eig - 1.0) * 100.0,
            "vertices": nv,
            "triangles": nt,
            "interior_grid_points": nint,
        }
    with open(OUT, 'w') as f:
        json.dump(results, f, indent=2)
    print(json.dumps({"output": OUT, "cases": {k: {"lambda1_unit": v["lambda1_unit_curvature_minus1"], "A_eig": v["A_eig_for_lambda1_2"], "A_side": v["A_match_side"], "rod_side_defect_at_Aeig_percent": v["rod_side_defect_at_Aeig_percent"], "lambda1_at_side": v["lambda1_at_side_match"]} for k,v in results["cases"].items()}}, indent=2))

if __name__ == "__main__":
    main()
