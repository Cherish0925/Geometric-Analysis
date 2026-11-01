"""
Fit the 20x20 log-coefficient form Meff (from step57_general_form.py) to U(2)_zeta-invariant quadratic invariants.
usage: python step57_fit_invariants.py data/step57_general_form_D2_q10_32.json
Parameter order t: [s, W+ (TL basis 5), W- (TL basis 5), Bk (3x3 row-major; row index = Lambda^+ basis, row 0 = zeta)].
"""
import sys, json, os
import numpy as np
s2 = 1 / np.sqrt(2)
def tl_basis():
    b = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        m = np.zeros((3, 3)); m[i, j] = m[j, i] = s2; b.append(m)
    b.append(np.diag([1, -1, 0]) * s2)
    b.append(np.diag([1, 1, -2]) / np.sqrt(6))
    return b
TL = tl_basis()
def parts(t):
    s = t[0]; Wp = sum(t[1 + i] * TL[i] for i in range(5)); Wm = sum(t[6 + i] * TL[i] for i in range(5))
    Bk = np.asarray(t[11:20]).reshape(3, 3)
    return s, Wp, Wm, Bk
def invariants(t):
    s, Wp, Wm, Bk = parts(t)
    w = Wp[0, 0]
    perp = Wp[1:, 1:] - 0.5 * np.trace(Wp[1:, 1:]) * np.eye(2)
    return dict(s2=s * s, sw=s * w, w2=w * w, Wzp=Wp[0, 1] ** 2 + Wp[0, 2] ** 2,
                Wpp=np.sum(perp ** 2), Wm=np.sum(Wm ** 2), Rz=np.sum(Bk[0] ** 2), Rp=np.sum(Bk[1:] ** 2))
names = list(invariants(np.zeros(20)).keys())
def gram(name):
    G = np.zeros((20, 20)); E = np.eye(20)
    f = lambda t: invariants(t)[name]
    for a in range(20):
        for b in range(20):
            G[a, b] = 0.5 * (f(E[a] + E[b]) - f(E[a]) - f(E[b]))
    return G
Gs = [gram(n) for n in names]
if __name__ == '__main__':
    d = json.load(open(sys.argv[1]))
    M = np.array(d['Meff'])
    iu = np.triu_indices(20)
    A = np.array([G[iu] for G in Gs]).T
    coef, *_ = np.linalg.lstsq(A, M[iu], rcond=None)
    res = np.linalg.norm(A @ coef - M[iu]) / np.linalg.norm(M[iu])
    out = dict(zip(names, coef.tolist())); out['rel_residual'] = float(res)
    # kernel-direction reduction: w=-s/12, Wzp=0
    out['s2_coeff_kernel'] = float(coef[0] - coef[1] / 12 + coef[2] / 144)
    print(json.dumps(out, indent=1))
    if 'M' in d:
        Mr = np.array(d['M']); c2, *_ = np.linalg.lstsq(A, Mr[iu], rcond=None)
        print('raw (K=0) fit', dict(zip(names, np.round(c2, 8))), 'res', np.linalg.norm(A @ c2 - Mr[iu]) / np.linalg.norm(Mr[iu]))
    json.dump(out, open(sys.argv[1].replace('.json', '_invfit.json'), 'w'), indent=1)
