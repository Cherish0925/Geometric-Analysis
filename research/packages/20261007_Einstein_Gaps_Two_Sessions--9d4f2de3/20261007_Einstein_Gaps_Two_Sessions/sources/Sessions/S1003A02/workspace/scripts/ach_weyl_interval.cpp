// Interval Weyl-discriminant enclosure for the validated O(-1) ACH Einstein bolt flow.
//
// State: (m,de,L3,ym,eta,y3,d), identical to ach_bolt_capd.cpp.
// The metric is g=dt^2+a1^2 sigma1^2+a2^2 sigma2^2+a3^2 sigma3^2,
// d sigma_i=2 sigma_j wedge sigma_k.  For diagonal Einstein metrics the
// curvature operator is block diagonal in the paired 2-form basis
// (01,02,03,23,31,12).  The sectional curvatures are
// K0i=-(yi'+yi^2), and the complementary off-diagonal entries follow from
// Einstein's diagonal equations determine the orbit sectional curvatures.
// The mixed entries are computed from Cartan's equations.  With
// n_i=2a_i/(a_j a_k), A=(n1+n2-n3)/2, B=(-n1+n2+n3)/2,
// C=(n1-n2+n3)/2, one has
//   R_0123=-y1*n1+y2*A+y3*C,
// and its cyclic analogues.
// Consequently the two chiral Weyl blocks are diagonal, and their pairwise
// gaps equal the pairwise gaps of
//   WA_i=(K0i+Kjk)/2 + R_0ijk,
//   WB_i=(K0i+Kjk)/2 - R_0ijk.
// Subtracting s/12 does not affect gaps.  Output interval enclosures of all
// three pairwise gaps and the tracefree discriminant product.
//
// Usage: ach_weyl_interval duration order lo0 hi0 ... lo6 hi6
#include "capd/capdlib.h"
#include <cmath>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
using I=capd::interval; using V=capd::IVector;

double number(const char* input){std::size_t e=0;double r=std::stod(input,&e);if(e!=std::string(input).size()||!std::isfinite(r))throw std::runtime_error("bad number");return r;}
void printI(const I& x){std::cout<<"[\""<<std::hexfloat<<x.leftBound()<<"\",\""<<x.rightBound()<<"\"]";}
int main(int argc,char** argv){try{
 if(argc!=17)throw std::runtime_error("usage: duration order lo0 hi0 ... lo6 hi6");
 double duration=number(argv[1]);std::size_t oe=0;int order=std::stoi(argv[2],&oe);
 if(oe!=std::string(argv[2]).size()||duration<=0||order<2||order>100)throw std::runtime_error("bad duration/order");
 V initial(7);for(int i=0;i<7;++i){double lo=number(argv[3+2*i]),hi=number(argv[4+2*i]);if(lo>hi)throw std::runtime_error("reversed");initial[i]=I(lo,hi);}
 const std::string vf=
  "var:m,de,L3,ym,eta,y3,d;fun:ym,eta,y3,"
  "6-ym*(2*ym+y3)+2*exp(-2*m)*(exp(de)+exp(-de))-2*exp(2*L3-4*m),"
  "-eta*(2*ym+y3)+4*exp(-2*L3)*(exp(2*de)-exp(-2*de))-4*exp(-2*m)*(exp(de)-exp(-de)),"
  "6-y3*(2*ym+y3)+2*exp(2*L3-4*m)-2*exp(-2*L3)*(exp(de)-exp(-de))^2,0;";
 capd::IMap field(vf);capd::IOdeSolver solver(field,order);capd::ITimeMap flow(solver);capd::C0Rect2Set set(initial);V out=flow(I(duration),set);V der=field(out);
 I y[3]={out[3]+out[4]/2,out[3]-out[4]/2,out[5]};
 I yp[3]={der[3]+der[4]/2,der[3]-der[4]/2,der[5]};
 I K0[3];for(int i=0;i<3;++i)K0[i]=-(yp[i]+y[i]*y[i]);
 // Ric_ii=K0i+Kij+Kik=-6, solve for orbit sectional curvatures.
 I K12=(-I(6)-K0[0]-K0[1]+K0[2])/2;
 I K13=(-I(6)-K0[0]-K0[2]+K0[1])/2;
 I K23=(-I(6)-K0[1]-K0[2]+K0[0])/2;
 I Ko[3]={K23,K13,K12};
 I a[3]={exp(out[0]+out[1]/2),exp(out[0]-out[1]/2),exp(out[2])};
 I n[3]={2*a[0]/(a[1]*a[2]),2*a[1]/(a[2]*a[0]),2*a[2]/(a[0]*a[1])};
 I connA=(n[0]+n[1]-n[2])/2;
 I connB=(-n[0]+n[1]+n[2])/2;
 I connC=(n[0]-n[1]+n[2])/2;
 I cross[3]={-y[0]*n[0]+y[1]*connA+y[2]*connC,
             -y[1]*n[1]+y[2]*connB+y[0]*connA,
             -y[2]*n[2]+y[0]*connC+y[1]*connB};
 I A[3],B[3];for(int i=0;i<3;++i){A[i]=(K0[i]+Ko[i])/2+cross[i];B[i]=(K0[i]+Ko[i])/2-cross[i];}
 I Ag[3]={A[0]-A[1],A[0]-A[2],A[1]-A[2]};I Bg[3]={B[0]-B[1],B[0]-B[2],B[1]-B[2]};
 I Ad=Ag[0]*Ag[0]*Ag[1]*Ag[1]*Ag[2]*Ag[2];I Bd=Bg[0]*Bg[0]*Bg[1]*Bg[1]*Bg[2]*Bg[2];
 std::cout<<"{\"endpoint_hex\":[";for(int i=0;i<7;++i){if(i)std::cout<<',';printI(out[i]);}
 std::cout<<"],\"Araw\":[";for(int i=0;i<3;++i){if(i)std::cout<<',';printI(A[i]);}
 std::cout<<"],\"Braw\":[";for(int i=0;i<3;++i){if(i)std::cout<<',';printI(B[i]);}
 std::cout<<"],\"Agaps\":[";for(int i=0;i<3;++i){if(i)std::cout<<',';printI(Ag[i]);}
 std::cout<<"],\"Bgaps\":[";for(int i=0;i<3;++i){if(i)std::cout<<',';printI(Bg[i]);}
 std::cout<<"],\"Adisc\":";printI(Ad);std::cout<<",\"Bdisc\":";printI(Bd);std::cout<<"}\n";return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}}
