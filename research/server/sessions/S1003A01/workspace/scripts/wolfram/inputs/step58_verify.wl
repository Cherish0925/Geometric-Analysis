(* Independent exact check of the explicit Bianchi-VIII AKE formulas.
   Assumption: 1/3<p<1.  y^2=(3p-1)(3p+1)(3p^2+1). *)
Clear[p,y];
D0=(3p-1)(3p+1)(3p^2+1);
c=(1-p)(1+p)/(2(3p^2+1));
red[z_]:=Factor[PolynomialReduce[Together[z]//Numerator,{y^2-D0},{y}][[2]]/(Together[z]//Denominator)];
dt[z_]:=red[c y (D[z,p]+D[z,y] D[D0,p]/(2y))];
A={4(3p-1)(3p^2+1)/(3(1-p)(1+p)^2),4(3p+1)(3p^2+1)/(3(1-p)^2(1+p)),64p^2/((1-p)(1+p)(3p^2+1))};
h=red/@(c y D[Log[#],p]/2& /@ A);
W=red/@{y(p-1)/(8p(3p+1)),y(p+1)/(8p(3p-1)),-6p y(p-1)(p+1)/((3p-1)(3p+1)(3p^2+1)^2)};
mu=Table[red[2W[[i]]-h[[Mod[i,3]+1]]-h[[Mod[i+1,3]+1]]],{i,3}];
X={(1-p)^3(3p+1)/(16p^3),(1+p)^3(3p-1)/(16p^3),0};
S0=Total[h];
Q=red[h[[1]]h[[2]]+h[[1]]h[[3]]+h[[2]]h[[3]]+Total[W^2]-2(W[[1]]W[[2]]+W[[1]]W[[3]]+W[[2]]W[[3]])];
hres=Table[red[dt[h[[i]]]+h[[i]]S0-2(W[[i]]^2-(W[[Mod[i,3]+1]]-W[[Mod[i+1,3]+1]])^2)-3],{i,3}];
Wres=Table[red[dt[W[[i]]]-W[[i]](h[[i]]-h[[Mod[i,3]+1]]-h[[Mod[i+1,3]+1]])],{i,3}];
Xres=Table[red[dt[X[[i]]]-2mu[[i]]X[[i]]],{i,2}];
b={h[[1]]+W[[1]]-W[[2]]-W[[3]],h[[2]]-W[[1]]+W[[2]]-W[[3]],h[[3]]-W[[1]]-W[[2]]+W[[3]]};
q=red[2(Sum[X[[i]]mu[[i]]^2,{i,3}]+(X[[1]]+X[[2]])b[[3]]^2+(X[[1]]+X[[3]])b[[2]]^2+(X[[2]]+X[[3]])b[[1]]^2)];
Print["Q=",Q]; Print["hres=",hres]; Print["Wres=",Wres]; Print["Xres=",Xres]; Print["Xsum=",Factor[Total[X]]]; Print["q=",q]; Print["qtarget residual=",red[q-36(1-p^2)^3/(1+3p^2)^3]];
