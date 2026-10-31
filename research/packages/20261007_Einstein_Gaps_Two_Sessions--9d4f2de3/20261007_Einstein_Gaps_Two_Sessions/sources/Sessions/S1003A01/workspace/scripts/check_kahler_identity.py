"""Check cell_opt cost against the exact Kahler cell identity (inherited eq. (3.2)):
for w = phi = 0 (K Kahler), j = (2+mu)^2 + (1/2) int (s+4)^2 r^3 dr.
Random F perturbations; both coordinate systems."""
import sys, os, torch, math
sys.path.insert(0, os.path.dirname(__file__))
from cell_opt import Cell
torch.manual_seed(1)
for coord in ('lin', 'log'):
    for mu in (0.05, 0.2):
        c = Cell(mu, 1.2, 8, nq=800, coord=coord)
        cF = 0.05 * torch.randn(9); z = torch.zeros(9)
        j, pen, (F, w, p, comps) = c.cost(cF, z, z, parts=True)
        s = sum(comps) - 4  # e^{2p}=1: comps = Ric+1
        rhs = (2 + mu)**2 + 0.5 * torch.sum(c.wx * c.jac * (s + 4)**2 * c.r**3)
        print(coord, mu, 'j=', float(j), 'identity rhs=', float(rhs), 'minF/x=', float((F / c.x).min()), 'pen', float(pen))
