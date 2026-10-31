"""Stage-2 test of triaxial descent in the conformal one-bolt class.

1. Optimize (F, phi) with w = 0 (conformally Kahler biaxial cell).
2. At that optimum compute the full Hessian of j in all coefficients and the
   restricted w-block (w enters evenly, so grad_w = 0 there). Report min eigs.
3. Restart the full (F, w, phi) optimization from the optimum plus w-kicks of
   several amplitudes along the lowest w-eigenvector and random directions.
Output: one JSON line per (mu, Rc) to --out.
"""
import argparse, json, sys, os, math, torch
sys.path.insert(0, os.path.dirname(__file__))
from cell_opt import Cell
torch.set_default_dtype(torch.float64)


def lbfgs(cell, cF, cw, cp, free, iters):
    params = [t for t, f in zip((cF, cw, cp), free) if f]
    for t in params:
        t.requires_grad_(True)
    opt = torch.optim.LBFGS(params, lr=1, max_iter=iters, history_size=60,
                            tolerance_grad=1e-12, tolerance_change=1e-16, line_search_fn='strong_wolfe')
    def closure():
        opt.zero_grad()
        j, pen = cell.cost(cF, cw, cp)
        (j + pen).backward()
        return j + pen
    opt.step(closure)
    j, pen = cell.cost(cF, cw, cp)
    return float(j.detach()), float(pen.detach())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mu', type=float, required=True)
    ap.add_argument('--Rc', type=float, required=True)
    ap.add_argument('--deg', type=int, default=24)
    ap.add_argument('--nq', type=int, default=900)
    ap.add_argument('--iters', type=int, default=8000)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    cell = Cell(a.mu, a.Rc, a.deg, nq=a.nq, coord='log')
    n = a.deg + 1
    cF = torch.zeros(n); cw = torch.zeros(n); cp = torch.zeros(n)
    j0, pen0 = lbfgs(cell, cF, cw, cp, (True, False, True), a.iters)
    j0, pen0 = lbfgs(cell, cF.detach(), cw, cp.detach(), (True, False, True), a.iters) if False else (j0, pen0)
    base = [cF.detach().clone(), cw.detach().clone(), cp.detach().clone()]
    # Hessian
    z = torch.cat(base)
    def f(zz):
        j, pen = cell.cost(zz[:n], zz[n:2 * n], zz[2 * n:])
        return j + pen
    H = torch.autograd.functional.hessian(f, z)
    Hw = H[n:2 * n, n:2 * n]
    ew, vw = torch.linalg.eigh(Hw)
    Hfp = H[[i for i in range(3 * n) if not (n <= i < 2 * n)]][:, [i for i in range(3 * n) if not (n <= i < 2 * n)]]
    efp = torch.linalg.eigvalsh(Hfp)
    res = dict(mu=a.mu, Rc=a.Rc, deg=a.deg, j_biaxial_conf=j0, pen=pen0,
               kahler_bound=(2 + a.mu)**2 / (1 - a.mu**2 / a.Rc**4),
               hess_w_min=float(ew[0]), hess_w_max=float(ew[-1]),
               hess_Fphi_min=float(efp[0]), restarts=[])
    torch.manual_seed(0)
    dirs = [vw[:, 0]] + [torch.randn(n) / math.sqrt(n) for _ in range(3)]
    for di, d in enumerate(dirs):
        for amp in (0.05, 0.3, 1.0):
            cF = base[0].clone(); cp = base[2].clone(); cw = amp * d.clone()
            j, pen = lbfgs(cell, cF, cw, cp, (True, True, True), a.iters)
            wmax = float(cell.fields(cF.detach(), cw.detach(), cp.detach())[1][0].abs().max())
            res['restarts'].append(dict(dir=di, amp=amp, j=j, pen=pen, wmax=wmax))
    res['j_full_best'] = min([r['j'] for r in res['restarts'] if r['pen'] < 1e-8] + [j0])
    with open(a.out, 'w') as fh:
        fh.write(json.dumps(res) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k != 'restarts'}))


if __name__ == '__main__':
    main()
