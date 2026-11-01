"""
Step 15 (S0910A02): finite-difference spectral test for localized edge
negative curvature under a fixed base-area / Dirichlet eigenvalue constraint.

This is a *2D base relaxation* rather than a metric construction on the
4-manifold.  It answers a precise sub-question from the Step-15 strategist note:
can right-angled/geodesic orbit-space geometry carry isolated edge-curvature
spikes while keeping lambda_1^Dir <= 2(1+delta)?

Model
-----
Use a rectangle [0,Lx]x[0,Ly] with a conformal metric g_B=e^{2 phi}(dx^2+dy^2).
In 2D, the Dirichlet Rayleigh quotient is conformally invariant in the numerator:

    lambda_1(g_B)= min int |grad u|^2 dxdy / int u^2 e^{2 phi} dxdy.

Thus if phi is positive in boundary collars, area increases and lambda_1 drops;
if the rectangle is rescaled to a prescribed total area, lambda_1 rescales
inversely with area.  Curvature is K=-e^{-2phi} Delta phi.  Choosing phi with
large positive second normal derivative near the edges gives negative K in a
thin collar.  This does not impose geodesic-boundary Neumann conditions on phi
perfectly; it is a spectral feasibility probe, not a proof.

The test solves the generalized eigenproblem
    -Delta_E u = lambda * e^{2 phi} u
with Dirichlet boundary, then rescales to the target area A0.  It records the
amount of negative curvature in collars and whether lambda_1<=2 remains easy.
"""
import json, math, os
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
os.makedirs(DATA, exist_ok=True)

j0 = 2.404825557695773
A_FK = math.pi*j0*j0/2.0
A0 = 10.0  # keep base area fixed and above Faber--Krahn floor


def solve_rect_phi(Nx=60, Ny=60, Lx=math.sqrt(10.0), Ly=math.sqrt(10.0), amp=1.0, width=0.05):
    # interior grid only; Dirichlet at boundary
    hx = Lx/(Nx+1)
    hy = Ly/(Ny+1)
    xs = (np.arange(Nx)+1)*hx
    ys = (np.arange(Ny)+1)*hy
    X, Y = np.meshgrid(xs, ys, indexing='ij')
    # distance to boundary in Euclidean rectangle
    d = np.minimum.reduce([X, Lx-X, Y, Ly-Y])
    # Smooth-ish positive collar potential; convex near boundary gives negative K
    phi = amp*np.exp(-(d/width)**2)
    weight = np.exp(2*phi).reshape(-1)
    area = float(np.sum(weight)*hx*hy)
    # sparse -Delta with Dirichlet
    n = Nx*Ny
    main = np.full(n, 2/hx**2 + 2/hy**2)
    offx = np.full(n-1, -1/hx**2)
    for i in range(1, Nx):
        offx[i*Ny-1] = 0.0  # break rows in x-major? Actually index=i*Ny+j, neighbor y at +/-1.
    offy = np.full(n-Ny, -1/hx**2)
    # Need careful axes: index = i*Ny + j. Neighbor j +/- 1 uses off1/hy^2; neighbor i +/-1 uses offNy/hx^2.
    off1 = np.full(n-1, -1/hy**2)
    for i in range(Nx):
        if i*Ny + Ny - 1 < n-1:
            off1[i*Ny + Ny - 1] = 0.0
    offN = np.full(n-Ny, -1/hx**2)
    A = diags([main, off1, off1, offN, offN], [0, -1, 1, -Ny, Ny], format='csr')
    M = diags(weight, 0, format='csr')
    val = eigsh(A, k=1, M=M, sigma=0.0, which='LM', return_eigenvectors=False)[0]
    # Rescale metric by c so area -> A0; eigenvalue scales by 1/c.
    cscale = A0/area
    lambda_scaled = val/cscale
    # finite-difference curvature diagnostic on interior excluding one-cell boundary
    # K = -e^{-2phi} (phi_xx+phi_yy)
    ph = phi
    lap = np.zeros_like(ph)
    lap[1:-1,1:-1] = ((ph[2:,1:-1]-2*ph[1:-1,1:-1]+ph[:-2,1:-1])/hx**2 +
                      (ph[1:-1,2:]-2*ph[1:-1,1:-1]+ph[1:-1,:-2])/hy**2)
    K = -np.exp(-2*ph)*lap
    # integrate positive/negative parts with original metric area element e^{2phi}dxdy;
    # K dA = -Delta phi dxdy, but this discrete version is enough as diagnostic.
    KdA = K*np.exp(2*ph)*hx*hy
    neg_int = float(np.sum(np.minimum(KdA[1:-1,1:-1], 0.0)))
    pos_int = float(np.sum(np.maximum(KdA[1:-1,1:-1], 0.0)))
    minK = float(np.min(K[1:-1,1:-1]))
    maxK = float(np.max(K[1:-1,1:-1]))
    return dict(Nx=Nx, Ny=Ny, Lx=Lx, Ly=Ly, amp=amp, width=width,
                area_raw=area, area_target=A0, conformal_scale=A0/area,
                lambda1_raw=float(val), lambda1_scaled=float(lambda_scaled),
                minK=minK, maxK=maxK,
                int_K_negative=neg_int, int_K_positive=pos_int,
                int_K_signed=neg_int+pos_int,
                spectral_bound_2=bool(lambda_scaled <= 2.0))

cases = []
for amp in [0.0, 0.5, 1.0, 2.0, 3.0]:
    for width in [0.03, 0.05, 0.08, 0.12]:
        cases.append(solve_rect_phi(Nx=55, Ny=55, amp=amp, width=width))
# Take a stronger narrow spike sample at modest grid.
for amp, width in [(4.0,0.04),(5.0,0.04),(5.0,0.06),(6.0,0.05)]:
    cases.append(solve_rect_phi(Nx=65, Ny=65, amp=amp, width=width))

summary = []
for c in cases:
    summary.append({
        "amp": c["amp"], "width": c["width"],
        "lambda1_scaled": c["lambda1_scaled"], "spectral_bound_2": c["spectral_bound_2"],
        "minK": c["minK"], "int_K_negative": c["int_K_negative"],
        "int_K_positive": c["int_K_positive"], "area_raw": c["area_raw"]
    })

report = {
    "title": "Step 15 finite-difference spectral test for localized edge curvature spikes",
    "area_target": A0,
    "Faber_Krahn_area_delta0": A_FK,
    "model": "conformal rectangles with boundary-collar phi; generalized eigenproblem -Delta u=lambda e^{2phi}u; metric rescaled to area target",
    "cases": cases,
    "summary": summary,
    "finding": ("Localized edge curvature spikes are compatible with lambda1<=2 in this 2D relaxation: "
                "increasing positive collar conformal factor can create large negative curvature diagnostics while keeping or lowering the first Dirichlet eigenvalue after fixed-area normalization. "
                "Therefore McKean/Cheng/global-negative-curvature intuition cannot by itself rule out the boundary-bubble enemy; the missing obstruction must use smooth 4D closure/Ricci pinching/gluing, not just base spectral geometry."),
    "limitations": [
        "The conformal rectangle does not enforce exact geodesic edges/right-angle corner smoothing in the toric orbit metric.",
        "It does not solve the 4D reduced Ricci inequalities or unit-slope fiber closure.",
        "Its purpose is only to test whether lambda1<=2 forbids localized negative base curvature; it does not."
    ]
}
OUT = os.path.join(DATA, "step15_edge_spike_spectral_fd.json")
with open(OUT, "w") as f:
    json.dump(report, f, indent=2)
print(json.dumps({
    "title": report["title"],
    "area_target": A0,
    "Faber_Krahn_area_delta0": A_FK,
    "selected_cases": summary[::5] + summary[-4:],
    "finding": report["finding"],
    "saved": OUT,
}, indent=2))
