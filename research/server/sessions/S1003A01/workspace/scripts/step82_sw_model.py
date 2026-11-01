"""Step 82: the LeBrun Seiberg-Witten Weyl integrand and the Weyl-Bochner
integrand on the complete Bianchi-VIII strict AKE model (s=-12).

The model is NOT closed, so the SW inequality is not asserted on it.  The
computation asks whether the SW integral constraint would distinguish the
model from a closed candidate (if int psi0 < 0 on the model, SW is a genuinely
compactness-sensitive input; if >= 0, SW adds nothing that the model does not
already satisfy).  Norm conventions: Step-62/79 (vector norm for eta).
Output: workspace/data/step82/sw_model.json
"""
import json, os
import mpmath as mp
mp.mp.dps = 30
S = mp.mpf(12)

def G(p): return 4*(3*p*p+1)/((1-p)**2*(1+p)**2*(3*p-1)*(3*p+1))
def vol(p): return 32*p*mp.sqrt((9*p*p-1)*(3*p*p+1))/(3*(1-p*p)**2)
def q(p): return 36*(1-p*p)**3/(1+3*p*p)**3
def e(p): return 9*(1-p*p)**3*(9*p*p-1)/(3*p*p+1)**4
def v(p): return 81*(1-p*p)**4*(9*p*p-1)**2/(2*(3*p*p+1)**6)

def dens(p):
    qq, ee, vv = q(p), e(p), v(p)
    r = -S/6 + qq/4
    W2 = mp.mpf(3)/2*r*r + 2*ee + vv
    psi0 = (S + mp.sqrt(6*W2))**2 - mp.mpf(9)/4*S*S + 36*(vv + mp.mpf(3)/32*qq*qq)
    Zs = S*qq/16 - ee - vv - mp.mpf(3)/32*qq*qq
    pointwise_W_excess = W2 - S*S/24
    return {'psi0': psi0, 'Zs': Zs, 'q': qq, 'e': ee, 'v': vv, 'q2': qq*qq,
            'Wexc': pointwise_W_excess, 'psi36': psi0 + 36*Zs}

def integrate(key):
    f = lambda p: dens(p)[key]*vol(p)*mp.sqrt(G(p))
    return mp.quad(f, [mp.mpf(1)/3, mp.mpf('0.34'), mp.mpf('0.4'), mp.mpf('0.6'), mp.mpf('0.9'), 1])

def main():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    out = os.path.join(root, 'data', 'step82'); os.makedirs(out, exist_ok=True)
    res = {k: mp.nstr(integrate(k), 15) for k in ['q', 'e', 'v', 'q2', 'Zs', 'psi0', 'psi36', 'Wexc']}
    prof = []
    for p in ['0.3334', '0.35', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '0.99']:
        d = dens(mp.mpf(p)); prof.append({'p': p, **{k: mp.nstr(val, 10) for k, val in d.items()}})
    res['profile'] = prof
    print(json.dumps(res, indent=1))
    json.dump(res, open(os.path.join(out, 'sw_model.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
