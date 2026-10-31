"""Evaluate the Bianchi-IX transgression G (from data/transgression/G_formula.txt,
produced by bianchi_transgression.py) at bolt / flat / ALF / lens / CH slices.

Convention: T(slice) = 2 pi^2 (G(slice) - G_flat) so that, between slices,
  int 8 pi^2 (2e+3p) dV = T(t2) - T(t1).
"""
import os
import sympy as sp

here = os.path.dirname(os.path.abspath(__file__))
x, y, z, a1, b1, c1 = sp.symbols('x y z a1 b1 c1')
loc = {'x': x, 'y': y, 'z': z, 'a1': a1, 'b1': b1, 'c1': c1}


def load():
    txt = open(os.path.join(here, '..', 'data', 'transgression', 'G_formula.txt')).read()
    out = {}
    for block in txt.strip().split('\n\n'):
        lines = block.split('\n')
        o = int(lines[0].split()[1])
        out[o] = sp.sympify(lines[1].split('=', 1)[1], locals=loc)
    return out


if __name__ == '__main__':
    Gs = load()
    tt, a0, al, be, kap, k = sp.symbols('tt a0 alpha beta kappa k', positive=True)
    for o, G in Gs.items():
        flat = sp.simplify(G.subs({x: 1, y: 1, z: 1, a1: 1, b1: 1, c1: 1}))
        Gb = sp.simplify(G.subs({x: a0 + al * tt**2 / 2, y: a0 + be * tt**2 / 2, z: tt,
                                 a1: al * tt, b1: be * tt, c1: 1}))
        bolt = sp.limit(Gb, tt, 0)
        alf = sp.factor(sp.simplify(G.subs({x: 1, y: 1, z: kap, a1: 1, b1: 1, c1: 0}) - flat))
        lens = sp.factor(sp.simplify(G.subs({x: 1, y: 1, z: 1 / k, a1: 1, b1: 1, c1: 1 / k}) - flat))
        # smooth centre of R^4: a=b=c=t, a'=1
        print(f'orient {o}: G_flat={flat}, G_bolt={sp.simplify(bolt)}, '
              f'T_bolt/(2pi^2)={sp.simplify(bolt-flat)}, ALF(a=b=1,c=kappa,c\'=0)-flat={alf}, '
              f'flat cone c=t/k: {lens}')
