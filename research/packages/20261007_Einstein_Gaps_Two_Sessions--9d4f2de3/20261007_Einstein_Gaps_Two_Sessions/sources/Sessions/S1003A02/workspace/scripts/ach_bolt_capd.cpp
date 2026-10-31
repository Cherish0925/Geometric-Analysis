// Rigorous CAPD enclosure of the anisotropy-resolving Einstein bolt flow.
//
// The state is X=(m,delta,L3,ym,eta,y3,d), with b=0.8 fixed and d'=0.
// Initial boxes at a regular positive time t0 are supplied by the companion
// Arb bolt-series enclosure script.  The ODE is exactly the rhs_md system in
// ach_projected.py, rewritten without subtraction-unstable Pot1-Pot2.
//
// Usage:
//   ach_bolt_capd duration order lo0 hi0 ... lo6 hi6
// Output is an exact-hex interval enclosure of the endpoint and the compact
// ACH/block coordinates when defined.
#include "capd/capdlib.h"
#include <cmath>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>

using I = capd::interval;
using V = capd::IVector;

double number(const char* input) {
  std::size_t end = 0;
  double result = std::stod(input, &end);
  if (end != std::string(input).size() || !std::isfinite(result))
    throw std::runtime_error("expected finite binary64 endpoint");
  return result;
}

void printI(const I& x){
  std::cout << "[\"" << std::hexfloat << x.leftBound() << "\",\""
            << std::hexfloat << x.rightBound() << "\"]";
}

int main(int argc, char** argv){
 try {
  if(argc != 17) throw std::runtime_error("usage: ach_bolt_capd duration order lo0 hi0 ... lo6 hi6");
  double duration=number(argv[1]);
  std::size_t oe=0; int order=std::stoi(argv[2],&oe);
  if(oe!=std::string(argv[2]).size() || duration<=0 || order<2 || order>100)
    throw std::runtime_error("bad duration/order");
  V initial(7);
  for(int i=0;i<7;++i){
    double lo=number(argv[3+2*i]), hi=number(argv[4+2*i]);
    if(lo>hi) throw std::runtime_error("reversed interval");
    initial[i]=I(lo,hi);
  }
  const std::string vf =
    "var:m,de,L3,ym,eta,y3,d;"
    "fun:"
    "ym,"
    "eta,"
    "y3,"
    // (P1+P2)/2 = 4 exp(-2m) cosh(de) - 2 exp(2L3-4m)   [exact; the cosh(2de) e^{-2L3} terms cancel]
    "6-ym*(2*ym+y3)+2*exp(-2*m)*(exp(de)+exp(-de))-2*exp(2*L3-4*m),"
    // P1-P2 cancellation-free; use exponentials because CAPD's expression parser lacks sinh/cosh.
    "-eta*(2*ym+y3)+4*exp(-2*L3)*(exp(2*de)-exp(-2*de))-4*exp(-2*m)*(exp(de)-exp(-de)),"
    // P3 = 2 exp(2L3-4m)-8 exp(-2L3)sinh(de)^2
    "6-y3*(2*ym+y3)+2*exp(2*L3-4*m)-2*exp(-2*L3)*(exp(de)-exp(-de))^2,"
    "0;";
  capd::IMap field(vf);
  capd::IOdeSolver solver(field,order);
  capd::ITimeMap flow(solver);
  capd::C0Rect2Set set(initial);
  V out=flow(I(duration),set);

  // Fibre slot 1 (a1), horizontal g=slot2, h=slot3.
  I L1=out[0]+out[1]/2, L2=out[0]-out[1]/2;
  I y1=out[3]+out[4]/2, y2=out[3]-out[4]/2, y3=out[5];
  I k=exp(L1-L2-out[2]), q=L2-out[2], z=exp(-L2-out[2]);
  I dyf=y1-2, ds=y2+y3-2, dk=k-1, a=y2-y3;
  I u=dyf-ds+6*dk-2*cosh(q)*z;
  I s1=dyf-ds-2*dk+2*cosh(q)*z;
  I s2=2*dyf+3*ds+2*dk-4*cosh(q)*z;
  I ah=a+4*sinh(q)*z;
  I ub=u/z, s1b=s1/z, s2b=s2/z, ab=ah/z;
  I phi=q+(y2-y3)/4-z*sinh(q), rho=exp(phi);

  std::cout << "{\"status\":\"validated_bolt_flow_endpoint\",\"duration_hex\":\""
            << std::hexfloat << duration << "\",\"order\":" << order << ",\"endpoint_hex\":[";
  for(int i=0;i<7;++i){if(i) std::cout<<','; printI(out[i]);}
  std::cout << "],\"compact\":{\"kappa\":"; printI(k);
  std::cout << ",\"q\":"; printI(q); std::cout << ",\"zeta\":"; printI(z);
  std::cout << ",\"ub\":"; printI(ub); std::cout << ",\"s1b\":"; printI(s1b);
  std::cout << ",\"s2b\":"; printI(s2b); std::cout << ",\"ab\":"; printI(ab);
  std::cout << ",\"phi\":"; printI(phi); std::cout << ",\"rho\":"; printI(rho);
  std::cout << "}}\n";
  return 0;
 } catch(const std::exception& e){std::cerr<<e.what()<<'\n'; return 2;}
}
