"""Step 81c: sign of the leading Levi form of log q along the torsion line at a
nondegenerate torsion zero.

At a zero, in a unitary coframe, alpha(x) = B x + c conj(x) + O(|x|^2) with
B = S^T - A (holomorphic first jet; S complex symmetric, A = a[[0,1],[-1,0]])
and c scalar (antiholomorphic part, forced to be pure trace by the torsion
structure equation).  The Step-62 zero cone is ||A||_F^2 = ||S||_F^2 + 8|c|^2.
The torsion line at x is the complex line C*conj(alpha(x)).
Leading order:  L_{log q}(l_alpha)(x) = Delta_{l} log|f|^2,  f = Bx + c xbar.
We sample cone jets and directions and record the sign of
   Lambda = |f|^2 * L / 4 .
Also tests the off-cone and the 'convention-swapped' jet f = c x + B xbar as a control.
Output: workspace/data/step81/levi_leading_sign.json
"""
import json, os
import numpy as np

rng = np.random.default_rng(81)


def levi_logf(fun, x, w, h=1e-4):
    # Laplacian of log|f|^2 on the real plane spanned by w, i w (|w|=1), flat metric
    def phi(t, s):
        return np.log(np.sum(np.abs(fun(x + (t + 1j*s)*w))**2))
    p0 = phi(0, 0)
    return (phi(h, 0) + phi(-h, 0) + phi(0, h) + phi(0, -h) - 4*p0)/h**2


def lam_closed(B, c, x):
    f = B@x + c*np.conj(x)
    nf = np.linalg.norm(f); fh = f/nf; w = np.conj(fh)
    Bw = B@w
    return np.linalg.norm(Bw)**2 - abs(np.vdot(fh, Bw))**2 - 2*np.real(c*np.vdot(fh, Bw))


def sample(cone=True, swap=False, n=20000):
    vals = []
    for _ in range(n):
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); S = (S + S.T)/2
        c = (rng.normal() + 1j*rng.normal())*rng.uniform(0, 1.5)
        if cone:
            a = np.sqrt((np.linalg.norm(S)**2 + 8*abs(c)**2)/2)*np.exp(1j*rng.uniform(0, 2*np.pi))
        else:
            a = (rng.normal() + 1j*rng.normal())
        A = a*np.array([[0, 1], [-1, 0]])
        B = S.T - A
        x = rng.normal(size=2) + 1j*rng.normal(size=2); x /= np.linalg.norm(x)
        if swap:
            fun = lambda y, B=B, c=c: c*y + B@np.conj(y)
        else:
            fun = lambda y, B=B, c=c: B@y + c*np.conj(y)
        f = fun(x); nf2 = np.sum(abs(f)**2)
        if nf2 < 1e-10:
            continue
        w = np.conj(f)/np.sqrt(nf2)
        L = levi_logf(fun, x, w)
        vals.append(L*nf2/4)
    vals = np.array(vals)
    return dict(n=int(len(vals)), min=float(vals.min()), max=float(vals.max()),
                frac_negative=float(np.mean(vals < -1e-6)), median=float(np.median(vals)))


def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    outdir = os.path.join(root, 'data', 'step81c'); os.makedirs(outdir, exist_ok=True)
    # check closed formula vs finite difference on a few jets
    chk = []
    for _ in range(5):
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); S = (S + S.T)/2
        c = rng.normal() + 1j*rng.normal(); a = rng.normal() + 1j*rng.normal()
        B = S.T - a*np.array([[0, 1], [-1, 0]])
        x = rng.normal(size=2) + 1j*rng.normal(size=2)
        fun = lambda y: B@y + c*np.conj(y)
        f = fun(x); nf2 = np.sum(abs(f)**2); w = np.conj(f)/np.sqrt(nf2)
        chk.append([float(levi_logf(fun, x, w)*nf2/4), float(lam_closed(B, c, x))])
    out = {'closed_vs_fd': chk,
           'cone': sample(True, False), 'offcone': sample(False, False),
           'cone_swapped_convention': sample(True, True),
           'cone_c0': None}
    # c = 0 sector (pure holomorphic jet): must be >= 0 (plurisubharmonic)
    vals = []
    for _ in range(5000):
        S = rng.normal(size=(2, 2)) + 1j*rng.normal(size=(2, 2)); S = (S + S.T)/2
        a = np.sqrt(np.linalg.norm(S)**2/2)*np.exp(1j*rng.uniform(0, 2*np.pi))
        B = S.T - a*np.array([[0, 1], [-1, 0]])
        x = rng.normal(size=2) + 1j*rng.normal(size=2); x /= np.linalg.norm(x)
        vals.append(lam_closed(B, 0, x))
    out['cone_c0'] = dict(min=float(min(vals)), max=float(max(vals)))
    print(json.dumps(out, indent=1))
    json.dump(out, open(os.path.join(outdir, 'levi_leading_sign.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
