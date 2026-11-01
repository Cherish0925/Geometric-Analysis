#!/usr/bin/env python3
"""Numerical implementation checks, not bounds for the variational problem."""

import unittest
import json
from pathlib import Path
import numpy as np
from search_coupled_cell import Cell


def geometric_residual(cell, parameters):
    """Independent diagonal Bianchi-IX Ricci and conformal calculation."""
    (f,fp,fpp),(w,wp,wpp),(phi,pp,ppp) = cell.profiles(parameters)
    r = cell.r
    lengths = np.array([r*np.exp(w),r*np.exp(-w),r*np.sqrt(f)])
    log_derivatives = np.array([1/r+wp,1/r-wp,1/r+fp/(2*f)])
    log_second = np.array([-1/r**2+wpp,-1/r**2-wpp,
                           -1/r**2+fpp/(2*f)-fp**2/(2*f**2)])
    velocities = np.sqrt(f)*log_derivatives
    acceleration = f*(log_second+log_derivatives**2)+fp*log_derivatives/2
    lam0 = -np.sum(acceleration,axis=0)
    tangential = []
    for k in range(3):
        j,l = [t for t in range(3) if t != k]
        orbit_ric = 2*(lengths[k]**4-(lengths[j]**2-lengths[l]**2)**2)/np.prod(lengths**2,axis=0)
        tangential.append(-acceleration[k]-velocities[k]*(velocities[j]+velocities[l])+orbit_ric)
    hess0 = f*ppp+fp*pp/2
    hesst = log_derivatives*f*pp
    lap = hess0+np.sum(hesst,axis=0)
    norm = f*pp**2
    conformal0 = lam0-2*hess0-lap+np.exp(2*phi)
    conformalt = np.array(tangential)-2*hesst-lap-2*norm+np.exp(2*phi)
    return np.vstack([conformal0,conformalt])*cell.sqrt_weight


class CellChecks(unittest.TestCase):
    def test_actual_negative_mode_fixture(self):
        path=Path(__file__).resolve().parents[1]/'verification/computations/20260928_coupled_negative_mode.json'
        item=json.loads(path.read_text())
        p=np.array(item['parameters'])
        base=p.copy()
        base[8:16]=0
        values=[]
        for panels,order in ((36,14),(144,18),(576,24)):
            cell=Cell(item['bolt'],item['radius'],item['count'],panels,order)
            values.append(cell.cost(p))
            self.assertGreater(cell.cost(base),values[-1])
            self.assertGreater(values[-1],item['threshold'])
        self.assertLess(max(values)-min(values),2e-10)
        self.assertAlmostEqual(values[-1],item['finite_cost_over_2pi2'],places=9)

    def test_complete_radial_moment(self):
        cell=Cell(.12,1.4,5,96,20)
        parameters=np.random.default_rng(1482).normal(0,.04,15)
        (f,fp,fpp),(w,wp,wpp),(phi,pp,ppp)=cell.profiles(parameters)
        r,wt=cell.r,cell.sqrt_weight**2
        residual=cell.residual(parameters).reshape(4,-1)/cell.sqrt_weight
        a0,a3,ah,vw=residual[0],residual[1],residual[2]/np.sqrt(2),residual[3]/np.sqrt(2)
        x,y,z=2*ah-a0-a3,a0+a3+2*ah,a0-a3
        positive=np.dot(wt,2*f*wp**2/r**4+8*(np.cosh(2*w)-1)/r**6
                        +8*np.sinh(2*w)**2/(r**6*f))
        conformal=2*np.dot(wt,f*pp**2/r**4)
        mu=cell.bolt**2
        integral=(mu**-2-cell.radius**-4)/4
        moment=1+2/mu+positive-conformal
        self.assertLess(abs(np.dot(wt,x/r**4)-moment),2e-9)
        completed=(moment**2/(4*integral)+np.dot(wt,(x-moment/(integral*r**4))**2)/4
                   +np.dot(wt,y*y)/4+np.dot(wt,z*z)/2+2*np.dot(wt,vw*vw))
        self.assertLess(abs(cell.cost(parameters)-completed),2e-9)

    def test_independent_geometric_cost(self):
        cell=Cell(.12,1.2,5,48,16)
        p=np.random.default_rng(142).normal(0,.04,15)
        expected=np.sum(geometric_residual(cell,p)**2)
        self.assertAlmostEqual(cell.cost(p),expected,places=10)

    def test_scalar_identity_and_quadrature(self):
        p=np.random.default_rng(842).normal(0,.03,15)
        coarse=Cell(.1,1,5,48,16)
        fine=Cell(.1,1,5,96,20)
        self.assertLess(abs(fine.receipt(p)['scalar_identity_error']),2e-10)
        self.assertLess(abs(coarse.cost(p)-fine.cost(p)),2e-9)

    def test_complex_step_jacobian(self):
        cell=Cell(.1,1,4,32,12)
        p=np.random.default_rng(23).normal(0,.01,12)
        direction=np.random.default_rng(24).normal(0,.1,12)
        cs=np.imag(cell.residual(p+1e-25j*direction))/1e-25
        fd=(cell.residual(p+1e-5*direction)-cell.residual(p-1e-5*direction))/2e-5
        self.assertLess(np.linalg.norm(cs-fd)/np.linalg.norm(cs),1e-8)


if __name__ == '__main__':
    unittest.main()
