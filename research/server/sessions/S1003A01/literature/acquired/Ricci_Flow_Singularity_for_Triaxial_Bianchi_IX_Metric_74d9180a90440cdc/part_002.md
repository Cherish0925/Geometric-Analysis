---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Ricci Flow Singularity for Triaxial Bianchi IX Metric]

Remark A.10. Note that by choosing this gauge, the new space variable $s$ depends on both the original space and time variables. Furthermore, from the relation $d s=\phi(z, t) d z$, we have the chain rule identity $\frac{\partial}{\partial s}=\frac{1}{\phi(z, t)} \frac{\partial}{\partial z}$. Thus, the derivatives in the $t$ direction and $s$ direction do not commute as the original variables $z$ and $t$ do. Therefore, we have the following commutator relation:
$$\left[\partial_{t}, \partial_{s}\right]=-\frac{\partial_{t} \phi}{\phi} \partial_{s} .$$

From now on, keeping this in mind, we suppress the dependence of the variable $s$ on the variables $z$ and $t$. \(\square\)

The sectional curvatures of the manifold $B \times S^{3}$ are given by:
$$\begin{aligned}
& K_{01}=-\frac{a^{\prime \prime}}{a} \\
& K_{02}=-\frac{b^{\prime \prime}}{b}, \\
& K_{03}=-\frac{c^{\prime \prime}}{c}, \\
& K_{12}=-\frac{a^{\prime} b^{\prime}}{a b}+\frac{\left(a^{2}-b^{2}\right)^{2}-3 c^{4}}{(a b c)^{2}}+\frac{2}{a^{2}}+\frac{2}{b^{2}}=-\frac{a^{\prime} b^{\prime}}{a b}+\hat{K}_{12}, \\
& K_{13}=-\frac{a^{\prime} c^{\prime}}{a c}+\frac{\left(a^{2}-c^{2}\right)^{2}-3 b^{4}}{(a b c)^{2}}+\frac{2}{a^{2}}+\frac{2}{c^{2}}=-\frac{a^{\prime} c^{\prime}}{a c}+\hat{K}_{13}, \\
& K_{23}=-\frac{b^{\prime} c^{\prime}}{b c}+\frac{\left(b^{2}-c^{2}\right)^{2}-3 a^{4}}{(a b c)^{2}}+\frac{2}{b^{2}}+\frac{2}{c^{2}}=-\frac{b^{\prime} c^{\prime}}{b c}+\hat{K}_{23} .
\end{aligned}$$

Since the off-diagonal terms in the Ricci tensor vanish identically, the Ricci flow equation preserves the form of the initial metric; that is, for all time for which the solution exists, the metric $g(t)$ would be of the form (A.1) for some positive functions $\phi, a, b$, and $c$ which are all functions of $z$ and $t$. Equating the first component in the Ricci flow equation gives us:
$$\begin{aligned}
\partial_{t}\left(\phi^{2}\right) & =2\left(\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}\right) \phi^{2} \\
\Rightarrow \quad \partial_{t}(\log \phi) & =\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}=-\left(K_{01}+K_{02}+K_{03}\right),
\end{aligned}$$
and thus $\left[\partial_{t}, \partial_{s}\right]=\left(K_{01}+K_{02}+K_{03}\right) \partial_{s}$.
The remaining equations are:
$$\begin{aligned}
& \partial_{t} a=a^{\prime \prime}+a^{\prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)-a\left(\hat{K}_{12}+\hat{K}_{13}\right), \\
& \partial_{t} b=b^{\prime \prime}+b^{\prime}\left(\frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)-b\left(\hat{K}_{12}+\hat{K}_{23}\right), \\
& \partial_{t} c=c^{\prime \prime}+c^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}\right)-c\left(\hat{K}_{13}+\hat{K}_{23}\right) .
\end{aligned}$$

In the arclength coordinate $s$, the Ricci flow is a semilinear parabolic system of equations:
$$\begin{aligned}
& \partial_{t} a=a^{\prime \prime}+a^{\prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)-2 a\left(\frac{a^{4}-\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right), \\
& \partial_{t} b=b^{\prime \prime}+b^{\prime}\left(\frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)-2 b\left(\frac{b^{4}-\left(a^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right), \\
& \partial_{t} c=c^{\prime \prime}+c^{\prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}\right)-2 c\left(\frac{c^{4}-\left(a^{2}-b^{2}\right)^{2}}{(a b c)^{2}}\right) .
\end{aligned}$$

This system, along with the commutator relation $\left[\partial_{t}, \partial_{s}\right]=-\left(\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}\right) \partial_{s}$, will be the system of equations that we will analyse in the next few chapters. Furthermore, from equations (A.3)-(A.7), we can calculate the scalar curvature S for $g$, which will be useful later:
$$\begin{aligned}
\mathrm{S} & =2\left(K_{01}+K_{02}+K_{03}+K_{12}+K_{13}+K_{23}\right) \\
& =2\left(-\frac{a^{\prime \prime}}{a}-\frac{b^{\prime \prime}}{b}-\frac{c^{\prime \prime}}{c}-\frac{a^{\prime} b^{\prime}}{a b}-\frac{a^{\prime} c^{\prime}}{a c}-\frac{b^{\prime} c^{\prime}}{b c}+\frac{2 a^{2} b^{2}+2 a^{2} c^{2}+2 b^{2} c^{2}-a^{4}-b^{4}-c^{4}}{a^{2} b^{2} c^{2}}\right) .
\end{aligned}$$

Under the Ricci flow, the scalar curvature evolves according to:
$$\partial_{t} \mathrm{~S}=\Delta \mathrm{S}+2|\operatorname{Ric}|_{g}^{2} \geq \Delta \mathrm{S}+\frac{2}{n} \mathrm{~S}^{2} .$$

To help us with the analysis, the evolution of the some derived quantities are also considered. We first consider the quantity $\xi:=a-b$. From equations (A.10) and (A.11), we can derive the evolution equation for $\xi$, which is given by:
$$\partial_{t} \xi=\xi^{\prime \prime}+\frac{c^{\prime}}{c} \xi^{\prime}+\left(\frac{a^{\prime} b^{\prime}}{a b}-\frac{2\left(a^{4}+b^{4}-c^{4}\right)}{a^{2} b^{2} c^{2}}-\frac{4\left(a^{2}+b^{2}-c^{2}\right)}{a b c^{2}}-\frac{4}{c^{2}}\right) \xi .$$

Similarly, the quantities $\zeta:=b-c$ and $\chi:=a-c$ satisfy the equations:
$$\begin{aligned}
& \partial_{t} \zeta=\zeta^{\prime \prime}+\frac{a^{\prime}}{a} \zeta^{\prime}+\left(\frac{b^{\prime} c^{\prime}}{b c}-\frac{2\left(b^{4}+c^{4}-a^{4}\right)}{a^{2} b^{2} c^{2}}-\frac{4\left(b^{2}+c^{2}-a^{2}\right)}{a^{2} b c}-\frac{4}{a^{2}}\right) \zeta, \\
& \partial_{t} \chi=\chi^{\prime \prime}+\frac{b^{\prime}}{b} \chi^{\prime}+\left(\frac{a^{\prime} c^{\prime}}{a c}-\frac{2\left(a^{4}+c^{4}-b^{4}\right)}{a^{2} b^{2} c^{2}}-\frac{4\left(a^{2}+c^{2}-b^{2}\right)}{a b^{2} c}-\frac{4}{b^{2}}\right) \chi .
\end{aligned}$$

In the vein the analysis in [6], we consider the quantities $\frac{\xi}{a}=\frac{a-b}{a}$ and $\frac{\xi}{b}=\frac{a-b}{b}$. These quantities can be thought of the measure for eccentricity of the fibre at each $z \in B$. These eccentricity quantities evolve according to the PDEs:
$$\begin{aligned}
& \partial_{t}\left(\frac{\xi}{a}\right)=\left(\frac{\xi}{a}\right)^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)\left(\frac{\xi}{a}\right)^{\prime}-4\left(\frac{1}{c^{2}}-\frac{1}{a^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{a^{2}+b^{2}-c^{2}}{a b c^{2}}\right)\left(\frac{\xi}{a}\right), \\
& \partial_{t}\left(\frac{\xi}{b}\right)=\left(\frac{\xi}{b}\right)^{\prime \prime}+\left(2 \frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right)\left(\frac{\xi}{b}\right)^{\prime}-4\left(\frac{1}{c^{2}}-\frac{1}{b^{2}}+\frac{a^{2}}{b^{2} c^{2}}+\frac{a^{2}+b^{2}-c^{2}}{a b c^{2}}\right)\left(\frac{\xi}{b}\right) .
\end{aligned}$$

Furthermore, the other eccentricity quantities, defined by $\frac{\zeta}{b}=\frac{b-c}{b}, \frac{\zeta}{c}=\frac{b-c}{c}, \frac{\chi}{a}=\frac{a-c}{a}$, and $\frac{\chi}{c}=\frac{a-c}{c}$ evolve according to the following PDEs:
$$\begin{aligned}
& \partial_{t}\left(\frac{\zeta}{b}\right)=\left(\frac{\zeta}{b}\right)^{\prime \prime}+\left(2 \frac{b^{\prime}}{b}+\frac{a^{\prime}}{a}\right)\left(\frac{\zeta}{b}\right)^{\prime}-4\left(\frac{1}{a^{2}}-\frac{1}{b^{2}}+\frac{c^{2}}{a^{2} b^{2}}+\frac{b^{2}+c^{2}-a^{2}}{a^{2} b c}\right)\left(\frac{\zeta}{b}\right), \\
& \partial_{t}\left(\frac{\zeta}{c}\right)=\left(\frac{\zeta}{c}\right)^{\prime \prime}+\left(2 \frac{c^{\prime}}{c}+\frac{a^{\prime}}{a}\right)\left(\frac{\zeta}{c}\right)^{\prime}-4\left(\frac{1}{a^{2}}-\frac{1}{c^{2}}+\frac{b^{2}}{a^{2} c^{2}}+\frac{b^{2}+c^{2}-a^{2}}{a^{2} b c}\right)\left(\frac{\zeta}{c}\right), \\
& \partial_{t}\left(\frac{\chi}{a}\right)=\left(\frac{\chi}{a}\right)^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}\right)\left(\frac{\chi}{a}\right)^{\prime}-4\left(\frac{1}{b^{2}}-\frac{1}{a^{2}}+\frac{c^{2}}{a^{2} b^{2}}+\frac{a^{2}+c^{2}-b^{2}}{a b^{2} c}\right)\left(\frac{\chi}{a}\right), \\
& \partial_{t}\left(\frac{\chi}{c}\right)=\left(\frac{\chi}{c}\right)^{\prime \prime}+\left(2 \frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}\right)\left(\frac{\chi}{c}\right)^{\prime}-4\left(\frac{1}{b^{2}}-\frac{1}{c^{2}}+\frac{a^{2}}{b^{2} c^{2}}+\frac{a^{2}+c^{2}-b^{2}}{a b^{2} c}\right)\left(\frac{\chi}{c}\right) .
\end{aligned}$$

To calculate the evolution of the curvatures, we need to find the evolution equations of the first and second derivatives of the metric components. For the first derivatives, by using the commutator relation (A.8) to swap the order of the time and space derivatives $\partial_{t}$ and $\partial_{s}$, we derive the following evolution equations:
$$\begin{aligned}
\partial_{t}\left(a^{\prime}\right)= & \left(\partial_{t} a\right)^{\prime}+\left[\partial_{t}, \partial_{s}\right] a^{\prime}=\left(\partial_{t} a\right)^{\prime}-\left(\frac{a^{\prime \prime}}{a}+\frac{b^{\prime \prime}}{b}+\frac{c^{\prime \prime}}{c}\right) a^{\prime} \\
= & a^{\prime \prime \prime}+a^{\prime \prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}-\frac{a^{\prime}}{a}\right)-a^{\prime}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{6 a^{4}+2\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +4\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right), \\
\partial_{t}\left(b^{\prime}\right)= & b^{\prime \prime \prime}+b^{\prime \prime}\left(\frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}-\frac{b^{\prime}}{b}\right)-b^{\prime}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{6 b^{4}+2\left(a^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +4\left(\frac{b^{3} a^{\prime}}{a^{3} c^{2}}+\frac{b^{3} c^{\prime}}{a^{2} c^{3}}-\frac{c^{2} a^{\prime}}{b a^{3}}-\frac{a^{2} c^{\prime}}{b c^{3}}+\frac{c c^{\prime}}{b a^{2}}+\frac{a a^{\prime}}{b c^{2}}\right), \\
\partial_{t}\left(c^{\prime}\right)= & c^{\prime \prime \prime}+c^{\prime \prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}-\frac{c^{\prime}}{c}\right)-c^{\prime}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{6 c^{4}+2\left(a^{2}-b^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +4\left(\frac{c^{3} a^{\prime}}{a^{3} b^{2}}+\frac{c^{3} b^{\prime}}{a^{2} b^{3}}-\frac{b^{2} a^{\prime}}{c a^{3}}-\frac{a^{2} b^{\prime}}{c b^{3}}+\frac{a a^{\prime}}{c b^{2}}+\frac{b b^{\prime}}{c a^{2}}\right),
\end{aligned}$$

Furthermore, we have:
$$\begin{aligned}
\partial_{t}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}\right)=\Delta_{g} & \left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}\right)-2 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}\left(2 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{4\left(a^{4}+\left(b^{2}-c^{2}\right)^{2}\right)}{a^{2} b^{2} c^{2}}\right) \\
& +8 \frac{a^{\prime}}{a^{2}}\left(\frac{a^{3} b^{\prime}}{b^{3} c^{2}}+\frac{a^{3} c^{\prime}}{b^{2} c^{3}}-\frac{c^{2} b^{\prime}}{a b^{3}}-\frac{b^{2} c^{\prime}}{a c^{3}}+\frac{c c^{\prime}}{a b^{2}}+\frac{b b^{\prime}}{a c^{2}}\right)-2 K_{01}^{2}-4 \frac{\left(a^{\prime}\right)^{2}}{a^{2}} K_{01}, \\
\partial_{t}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}\right)=\Delta_{g} & \left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}\right)-2 \frac{\left(b^{\prime}\right)^{2}}{b^{2}}\left(2 \frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{4\left(b^{4}+\left(a^{2}-c^{2}\right)^{2}\right)}{a^{2} b^{2} c^{2}}\right) \\
& +8 \frac{b^{\prime}}{b^{2}}\left(\frac{b^{3} a^{\prime}}{a^{3} c^{2}}+\frac{b^{3} c^{\prime}}{a^{2} c^{3}}-\frac{c^{2} a^{\prime}}{b a^{3}}-\frac{a^{2} c^{\prime}}{b c^{3}}+\frac{c c^{\prime}}{b a^{2}}+\frac{a a^{\prime}}{b c^{2}}\right)-2 K_{02}^{2}-4 \frac{\left(b^{\prime}\right)^{2}}{b^{2}} K_{02}, \\
\partial_{t}\left(\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)=\Delta_{g} & \left(\frac{\left(c^{\prime}\right)^{2}}{c^{2}}\right)-2 \frac{\left(c^{\prime}\right)^{2}}{c^{2}}\left(2 \frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{4\left(c^{4}+\left(a^{2}-b^{2}\right)^{2}\right)}{a^{2} b^{2} c^{2}}\right) \\
& +8 \frac{c^{\prime}}{c^{2}}\left(\frac{c^{3} a^{\prime}}{a^{3} b^{2}}+\frac{c^{3} b^{\prime}}{a^{2} b^{3}}-\frac{b^{2} a^{\prime}}{c a^{3}}-\frac{a^{2} b^{\prime}}{c b^{3}}+\frac{a a^{\prime}}{c b^{2}}+\frac{b b^{\prime}}{c a^{2}}\right)-2 K_{03}^{2}-4 \frac{\left(c^{\prime}\right)^{2}}{c^{2}} K_{03},
\end{aligned}$$
where $\Delta_{g}$ is the Laplacian operator, which is defined as:
$$\Delta_{g} f=f^{\prime \prime}+\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}\right) f^{\prime},$$
for any $f \in C^{2}(I)$. As for the second derivatives, we can calculate:
$$\begin{aligned}
& \partial_{t}\left(a^{\prime \prime}\right)=a^{\prime \prime \prime \prime}+a^{\prime \prime \prime}\left(\frac{b^{\prime}}{b}+\frac{c^{\prime}}{c}-\frac{a^{\prime}}{a}\right)+a^{\prime \prime}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}-2 \frac{\left(b^{\prime}\right)^{2}}{b^{2}}-2 \frac{\left(c^{\prime}\right)^{2}}{c^{2}}-2 \frac{a^{\prime \prime}}{a}-\frac{6 a^{4}+2\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& -2 a^{\prime}\left(\frac{b^{\prime} b^{\prime \prime}}{b^{2}}-\frac{\left(b^{\prime}\right)^{3}}{b^{3}}+\frac{c^{\prime} c^{\prime \prime}}{c^{2}}-\frac{\left(c^{\prime}\right)^{3}}{c^{3}}+\frac{6 a a^{\prime}}{b^{2} c^{2}}+\frac{4 b b^{\prime}}{a^{2} c^{2}}+\frac{4 c c^{\prime}}{a^{2} b^{2}}-\frac{2 a^{\prime} c^{2}}{a^{3} b^{2}}-\frac{2 a^{\prime} b^{2}}{a^{3} c^{2}}+\frac{4 a^{\prime}}{a^{3}}\right. \\
& \left.-\frac{12 a^{2} b^{\prime}}{b^{3} c^{2}}-\frac{12 a^{2} c^{\prime}}{b^{2} c^{3}}-\frac{4 b^{2} c^{\prime}}{a^{2} c^{3}}-\frac{4 c^{2} b^{\prime}}{a^{2} b^{3}}\right)+4 a^{3}\left(\frac{b^{\prime \prime}}{b^{3} c^{2}}-\frac{3\left(b^{\prime}\right)^{2}}{b^{4} c^{2}}-\frac{4 b^{\prime} c^{\prime}}{b^{3} c^{3}}+\frac{c^{\prime \prime}}{b^{2} c^{3}}-\frac{3\left(c^{\prime}\right)^{2}}{b^{2} c^{4}}\right) \\
& +4\left(\frac{\left(c^{\prime}\right)^{2}+c c^{\prime \prime}}{a b^{2}}+\frac{\left(b^{\prime}\right)^{2}+b b^{\prime \prime}}{a c^{2}}+\frac{3\left(b^{\prime}\right)^{2} c^{2}}{a b^{4}}+\frac{3 b^{2}\left(c^{\prime}\right)^{2}}{a c^{4}}-\frac{4 c c^{\prime} b^{\prime}+c^{2} b^{\prime \prime}}{a b^{3}}-\frac{4 b b^{\prime} c^{\prime}+b^{2} c^{\prime \prime}}{a c^{3}}\right), \\
& \partial_{t}\left(b^{\prime \prime}\right)=b^{\prime \prime \prime \prime}+b^{\prime \prime \prime}\left(\frac{a^{\prime}}{a}+\frac{c^{\prime}}{c}-\frac{b^{\prime}}{b}\right)+b^{\prime \prime}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}-2 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}-2 \frac{\left(c^{\prime}\right)^{2}}{c^{2}}-2 \frac{b^{\prime \prime}}{b}-\frac{6 b^{4}+2\left(a^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& -2 b^{\prime}\left(\frac{a^{\prime} a^{\prime \prime}}{a^{2}}-\frac{\left(a^{\prime}\right)^{3}}{a^{3}}+\frac{c^{\prime} c^{\prime \prime}}{c^{2}}-\frac{\left(c^{\prime}\right)^{3}}{c^{3}}+\frac{6 b b^{\prime}}{a^{2} c^{2}}+\frac{4 a a^{\prime}}{b^{2} c^{2}}+\frac{4 c c^{\prime}}{a^{2} b^{2}}-\frac{2 b^{\prime} c^{2}}{b^{3} a^{2}}-\frac{2 b^{\prime} a^{2}}{b^{3} c^{2}}+\frac{4 b^{\prime}}{b^{3}}\right. \\
& \left.-\frac{12 b^{2} a^{\prime}}{a^{3} c^{2}}-\frac{12 b^{2} c^{\prime}}{a^{2} c^{3}}-\frac{4 a^{2} c^{\prime}}{b^{2} c^{3}}-\frac{4 c^{2} a^{\prime}}{b^{2} a^{3}}\right)+4 b^{3}\left(\frac{a^{\prime \prime}}{a^{3} c^{2}}-\frac{3\left(a^{\prime}\right)^{2}}{a^{4} c^{2}}-\frac{4 a^{\prime} c^{\prime}}{a^{3} c^{3}}+\frac{c^{\prime \prime}}{a^{2} c^{3}}-\frac{3\left(c^{\prime}\right)^{2}}{a^{2} c^{4}}\right) \\
& +4\left(\frac{\left(c^{\prime}\right)^{2}+c c^{\prime \prime}}{b a^{2}}+\frac{\left(a^{\prime}\right)^{2}+a a^{\prime \prime}}{b c^{2}}+\frac{3\left(a^{\prime}\right)^{2} c^{2}}{b a^{4}}+\frac{3 a^{2}\left(c^{\prime}\right)^{2}}{b c^{4}}-\frac{4 c c^{\prime} a^{\prime}+c^{2} a^{\prime \prime}}{b a^{3}}-\frac{4 a a^{\prime} c^{\prime}+a^{2} c^{\prime \prime}}{b c^{3}}\right) \text {, } \\
& \partial_{t}\left(c^{\prime \prime}\right)=c^{\prime \prime \prime \prime}+c^{\prime \prime \prime}\left(\frac{a^{\prime}}{a}+\frac{b^{\prime}}{b}-\frac{c^{\prime}}{c}\right)+c^{\prime \prime}\left(\frac{\left(c^{\prime}\right)^{2}}{c^{2}}-2 \frac{\left(a^{\prime}\right)^{2}}{a^{2}}-2 \frac{\left(b^{\prime}\right)^{2}}{b^{2}}-2 \frac{c^{\prime \prime}}{c}-\frac{6 c^{4}+2\left(a^{2}-b^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& -2 c^{\prime}\left(\frac{a^{\prime} a^{\prime \prime}}{a^{2}}-\frac{\left(a^{\prime}\right)^{3}}{a^{3}}+\frac{b^{\prime} b^{\prime \prime}}{b^{2}}-\frac{\left(b^{\prime}\right)^{3}}{b^{3}}+\frac{6 c c^{\prime}}{a^{2} b^{2}}+\frac{4 a a^{\prime}}{b^{2} c^{2}}+\frac{4 b b^{\prime}}{a^{2} b^{2}}-\frac{2 c^{\prime} b^{2}}{c^{3} a^{2}}-\frac{2 c^{\prime} a^{2}}{c^{3} b^{2}}+\frac{4 c^{\prime}}{c^{3}}\right. \\
& \left.-\frac{12 c^{2} a^{\prime}}{a^{3} b^{2}}-\frac{12 c^{2} b^{\prime}}{a^{2} b^{3}}-\frac{4 b^{2} a^{\prime}}{c^{2} a^{3}}-\frac{4 a^{2} b^{\prime}}{c^{2} b^{3}}\right)+4 c^{3}\left(\frac{a^{\prime \prime}}{a^{3} b^{2}}-\frac{3\left(a^{\prime}\right)^{2}}{a^{4} b^{2}}-\frac{4 a^{\prime} b^{\prime}}{a^{3} b^{3}}+\frac{b^{\prime \prime}}{a^{2} b^{3}}-\frac{3\left(b^{\prime}\right)^{2}}{a^{2} b^{4}}\right) \\
& +4\left(\frac{\left(b^{\prime}\right)^{2}+b b^{\prime \prime}}{c a^{2}}+\frac{\left(a^{\prime}\right)^{2}+a a^{\prime \prime}}{c b^{2}}+\frac{3 a^{2}\left(b^{\prime}\right)^{2}}{c b^{4}}+\frac{3\left(a^{\prime}\right)^{2} b^{2}}{c a^{4}}-\frac{4 a a^{\prime} b^{\prime}+a^{2} b^{\prime \prime}}{c b^{3}}-\frac{4 b b^{\prime} a^{\prime}+b^{2} a^{\prime \prime}}{c a^{3}}\right) .
\end{aligned}$$

Thus, from the above equations, the sectional curvatures $K_{01}, K_{02}$, and $K_{03}$ evolve according to the following PDEs:
$$\begin{aligned}
\partial_{t} K_{01}= & \partial_{t}\left(-\frac{a^{\prime \prime}}{a}\right)=-\frac{\partial_{t}\left(a^{\prime \prime}\right)}{a}+\frac{a^{\prime \prime} \partial_{t} a}{a^{2}} \\
= & \Delta_{g} K_{01}+2 K_{01}^{2}-2 K_{01}\left(\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{2 a^{4}+2\left(b^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +2 K_{02}\left(\frac{2 a^{2}}{b^{2} c^{2}}+\frac{2 b^{2}}{a^{2} c^{2}}-\frac{2 c^{2}}{a^{2} b^{2}}-\frac{a^{\prime} b^{\prime}}{a b}\right)+2 K_{03}\left(\frac{2 a^{2}}{b^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}-\frac{2 b^{2}}{a^{2} c^{2}}-\frac{a^{\prime} c^{\prime}}{a c}\right) \\
& +2 \frac{a^{\prime}}{a}\left(-\frac{\left(b^{\prime}\right)^{3}}{b^{3}}-\frac{\left(c^{\prime}\right)^{3}}{c^{3}}+\frac{6 a a^{\prime}}{b^{2} c^{2}}+\frac{4 b b^{\prime}}{a^{2} c^{2}}+\frac{4 c c^{\prime}}{a^{2} b^{2}}-\frac{2 a^{\prime} c^{2}}{a^{3} b^{2}}-\frac{2 a^{\prime} b^{2}}{a^{3} c^{2}}+\frac{4 a^{\prime}}{a^{3}}\right. \\
& \left.-\frac{12 a^{2} b^{\prime}}{b^{3} c^{2}}-\frac{12 a^{2} c^{\prime}}{b^{2} c^{3}}-\frac{4 b^{2} c^{\prime}}{a^{2} c^{3}}-\frac{4 c^{2} b^{\prime}}{a^{2} b^{3}}\right)+4 a^{2}\left(\frac{3\left(b^{\prime}\right)^{2}}{b^{4} c^{2}}+\frac{4 b^{\prime} c^{\prime}}{b^{3} c^{3}}+\frac{3\left(c^{\prime}\right)^{2}}{b^{2} c^{4}}\right) \\
& -\frac{4}{a}\left(\frac{\left(c^{\prime}\right)^{2}}{a b^{2}}+\frac{\left(b^{\prime}\right)^{2}}{a c^{2}}+\frac{3\left(b^{\prime}\right)^{2} c^{2}}{a b^{4}}+\frac{3 b^{2}\left(c^{\prime}\right)^{2}}{a c^{4}}-\frac{4 c c^{\prime} b^{\prime}}{a b^{3}}-\frac{4 b b^{\prime} c^{\prime}}{a c^{3}}\right),
\end{aligned}$$
$$\begin{aligned}
\partial_{t} K_{02}=\Delta_{g} & K_{02}+2 K_{02}^{2}-2 K_{02}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(c^{\prime}\right)^{2}}{c^{2}}+\frac{2 b^{4}+2\left(a^{2}-c^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +2 K_{01}\left(\frac{2 a^{2}}{b^{2} c^{2}}+\frac{2 b^{2}}{a^{2} c^{2}}-\frac{2 c^{2}}{a^{2} b^{2}}-\frac{a^{\prime} b^{\prime}}{a b}\right)+2 K_{03}\left(\frac{2 b^{2}}{a^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}-\frac{2 a^{2}}{b^{2} c^{2}}-\frac{b^{\prime} c^{\prime}}{b c}\right) \\
& +2 \frac{b^{\prime}}{b}\left(-\frac{\left(a^{\prime}\right)^{3}}{a^{3}}-\frac{\left(c^{\prime}\right)^{3}}{c^{3}}+\frac{6 b b^{\prime}}{a^{2} c^{2}}+\frac{4 a a^{\prime}}{b^{2} c^{2}}+\frac{4 c c^{\prime}}{a^{2} b^{2}}-\frac{2 b^{\prime} c^{2}}{b^{3} a^{2}}-\frac{2 b^{\prime} a^{2}}{b^{3} c^{2}}+\frac{4 b^{\prime}}{b^{3}}\right. \\
& \left.-\frac{12 b^{2} a^{\prime}}{a^{3} c^{2}}-\frac{12 b^{2} c^{\prime}}{a^{2} c^{3}}-\frac{4 a^{2} c^{\prime}}{b^{2} c^{3}}-\frac{4 c^{2} a^{\prime}}{b^{2} a^{3}}\right)+4 b^{2}\left(\frac{3\left(a^{\prime}\right)^{2}}{a^{4} c^{2}}+\frac{4 a^{\prime} c^{\prime}}{a^{3} c^{3}}+\frac{3\left(c^{\prime}\right)^{2}}{a^{2} c^{4}}\right) \\
& -\frac{4}{b}\left(\frac{\left(c^{\prime}\right)^{2}}{b a^{2}}+\frac{\left(a^{\prime}\right)^{2}}{b c^{2}}+\frac{3\left(a^{\prime}\right)^{2} c^{2}}{b a^{4}}+\frac{3 a^{2}\left(c^{\prime}\right)^{2}}{b c^{4}}-\frac{4 c c^{\prime} a^{\prime}}{b a^{3}}-\frac{4 a a^{\prime} c^{\prime}}{b c^{3}}\right),
\end{aligned}$$
$$\begin{aligned}
\partial_{t} K_{03}=\Delta_{g} & K_{03}+2 K_{03}^{2}-2 K_{03}\left(\frac{\left(a^{\prime}\right)^{2}}{a^{2}}+\frac{\left(b^{\prime}\right)^{2}}{b^{2}}+\frac{2 c^{4}+2\left(a^{2}-b^{2}\right)^{2}}{(a b c)^{2}}\right) \\
& +2 K_{01}\left(\frac{2 a^{2}}{b^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}-\frac{2 b^{2}}{a^{2} c^{2}}-\frac{a^{\prime} c^{\prime}}{a c}\right)+2 K_{02}\left(\frac{2 b^{2}}{a^{2} c^{2}}+\frac{2 c^{2}}{a^{2} b^{2}}-\frac{2 a^{2}}{b^{2} c^{2}}-\frac{b^{\prime} c^{\prime}}{b c}\right) \\
& +2 \frac{c^{\prime}}{c}\left(-\frac{\left(a^{\prime}\right)^{3}}{a^{3}}-\frac{\left(b^{\prime}\right)^{3}}{b^{3}}+\frac{6 c c^{\prime}}{a^{2} b^{2}}+\frac{4 a a^{\prime}}{b^{2} c^{2}}+\frac{4 b b^{\prime}}{a^{2} b^{2}}-\frac{2 c^{\prime} b^{2}}{c^{3} a^{2}}-\frac{2 c^{\prime} a^{2}}{c^{3} b^{2}}+\frac{4 c^{\prime}}{c^{3}}\right. \\
& \left.-\frac{12 c^{2} a^{\prime}}{a^{3} b^{2}}-\frac{12 c^{2} b^{\prime}}{a^{2} b^{3}}-\frac{4 b^{2} a^{\prime}}{c^{2} a^{3}}-\frac{4 a^{2} b^{\prime}}{c^{2} b^{3}}\right)+4 c^{2}\left(\frac{3\left(a^{\prime}\right)^{2}}{a^{4} b^{2}}+\frac{4 a^{\prime} b^{\prime}}{a^{3} b^{3}}+\frac{3\left(b^{\prime}\right)^{2}}{a^{2} b^{4}}\right) \\
& -\frac{4}{c}\left(\frac{\left(b^{\prime}\right)^{2}}{c a^{2}}+\frac{\left(a^{\prime}\right)^{2}}{c b^{2}}+\frac{3 a^{2}\left(b^{\prime}\right)^{2}}{c b^{4}}+\frac{3\left(a^{\prime}\right)^{2} b^{2}}{c a^{4}}-\frac{4 a a^{\prime} b^{\prime}}{c b^{3}}-\frac{4 b b^{\prime} a^{\prime}}{c a^{3}}\right) .
\end{aligned}$$

\section*{Appendix B. Maximum Principles}

All of the equations computed in the previous section are of parabolic type. In order to study the behaviour of the metric components and the various other quantities computed earlier under the Ricci flow, we require some tools from parabolic theory, namely the max-imum principles. Let $I$ be a bounded open interval of $\mathbb{R}$ and define the initial-boundary
value problem for a linear parabolic equation:
$$\begin{aligned}
\mathcal{P}(u)=\partial_{t} u-u^{\prime \prime}-f(x, t) u^{\prime}-g(x, t) u & =0 \quad \text { on } \quad I \times[0, T) \subset \mathbb{R} \times \mathbb{R}_{+}, \\
\left.u\right|_{I \times\{0\}}(x) & =v(x), \\
\left.u\right|_{\partial I \times[0, T)} & =w(x, t) .
\end{aligned}$$

First, we define the parabolic boundary for the domain of the solution as follows:
Definition B. 1 (Parabolic domain, closure, interior, and boundary). Suppose that the solution of the parabolic problem (B.1)-(B.3) exists up to a time $T>0$. For a given $\tau \leq T$, the parabolic domain $I_{\tau}$ for the equation is given by the set $I \times[0, \tau)$. The closure and interior of $I_{\tau}$ are defined as $\bar{I}_{\tau}=\bar{I} \times[0, \tau]$ and $\stackrel{\circ}{I}_{\tau}=\stackrel{\circ}{I} \times(0, \tau)$ respectively. Furthermore, the parabolic boundary of $I_{\tau}$ is given by the set $\mathscr{P} I_{\tau}=I \times\{0\} \cup \partial I \times[0, \tau)$. \(\square\)

We now state the parabolic maximum principles that we are going to employ in the proofs of the results in this work.

Theorem B. 2 (Maximum Principle I). [4] Suppose that $I$ is a bounded and connected open domain in $\mathbb{R}$. Let $\mathcal{P}(u)=\partial_{t} u-u^{\prime \prime}-f(x, t) u^{\prime}-g(x, t) u$ be a parabolic operator such that $f, g: I \times \mathbb{R}_{+} \rightarrow \mathbb{R}$ are some functions with $g(x, t) \leq 0$ in $I_{T}$ where $T>0$. Suppose that $u \in C^{2,1}\left(I_{T}\right) \cap C^{0,0}\left(\bar{I}_{T}\right)$. Then:
\begin{itemize}
\item[(1)] If $u$ satisfies the parabolic inequality $\mathcal{P}(u) \leq 0$, then we have $\max _{I_{T}}(u)=\max _{\mathscr{P} I_{T}}\left(u^{+}\right)$ where $u^{+}=\max (u, 0)$.
\item[(2)] If $u$ satisfies the parabolic inequality $\mathcal{P}(u) \geq 0$, then we have $\min _{I_{T}}(u) \geq-\min _{\mathscr{P}_{T}}\left(u^{-}\right)$ where $u^{-}=-\min (u, 0)$.
\item[(3)] In particular, if $\mathcal{P}(u)=0$, then we have $\max _{I_{T}}(|u|)=\max _{\mathscr{P} I_{T}}(|u|)$ and consequently $|u| \leq \max _{\mathscr{P} I_{T}}(|u|)$. \(\square\)
\end{itemize}

Theorem B. 3 (Maximum Principle II). [11] Suppose that $I$ is a bounded open interval in $\mathbb{R}$ and $u \in C^{2,1}\left(I_{T}\right) \cap C^{0,0}\left(\bar{I}_{T}\right)$ satisfies the parabolic inequality:
$$\partial_{t} u \leq u^{\prime \prime}+f(x, t) u^{\prime}+g(u, t),$$
for some functions $f: I \times \mathbb{R}_{+} \rightarrow \mathbb{R}$ and $g: \mathbb{R} \times \mathbb{R}_{+} \rightarrow \mathbb{R}$. Assume that $g$ is locally Lipschitz in the $u$ variable and $u \leq C$ on $\mathscr{P} I_{T}$ where $T>0$ is the maximal time for which the solution exists. If $v$ is the solution of the associated ODE:
$$\begin{aligned}
\frac{d v}{d t} & =g(v, t), \\
v(0) & =C,
\end{aligned}$$
then we have $u(x, t) \leq v(t)$ for all $(x, t) \in I_{T}$ for which $v$ exists. \(\square\)

If we have non-positive data on the parabolic boundary, then we have a stronger result which does not require any sign conditions on the reaction term $g(x, t)$ as in Theorem B.2. A classical result [9] simply requires this reaction term to be uniformly bounded. In fact, the uniformly bounded condition can be weakened to locally bounded since the analysis are all done locally. For our purposes, we provide the proof for a simpler case for which we have vanishing boundary data and the coefficients are allowed to blow up to infinity at the boundaries.

Theorem B.4. Suppose that $I \subset \mathbb{R}$ is a bounded open interval and $u \in C^{2,1}\left(I_{T}\right) \cap C^{0,0}\left(\bar{I}_{T}\right)$ is a solution to the parabolic inequality $\mathcal{P}(u)=\partial_{t} u-u^{\prime \prime}-f(x, t) u^{\prime}-g(x, t) u \leq 0$ where $f, g: \stackrel{\circ}{I}_{T} \rightarrow \mathbb{R}$ are continuous functions in $I_{T}$. If $u \leq 0$ on $\mathscr{P} I_{T}$, then $u \leq 0$ in $I_{T}$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] Angenent, S., Isenberg, J., and Knopf, D. Formal Matched Asymptotics for Degenerate Ricci Flow Neckpinches. Nonlinearity, 24 (2011): 2265-2280.
\item[] [2] Angenent, S., Isenberg, J., and Knopf, D. Degenerate Neckpinches in Ricci Flow. Journal für die reine und angewandtte Mathematik (Crelles Journal) 709 (2015): 81-117.
\item[] [3] Angenent, S., and Knopf, D. An Example of Neckpinching in Ricci Flow on $S^{n+1}$. Mathematical Research Letters, 11 (2004), no. 4: 493-518.
\item[] [4] Evans, L.C. Partial Differential Equations. American Mathematical Society, Providence (2002).
\item[] [5] Hamilton, R.S. Four-Manifolds with Positive Curvature Operator. Journal of Differential Geometry, 24 (1986): 153-179.
\item[] [6] Isenberg, J., Knopf, D., and Šešum, N. Ricci Flow Neckpinches without Rotational Symmetry. Communications in Partial Differential Equations, 41 (2016), no. 12: 1860-1894.
\item[] [7] Isenberg, J., Knopf, D., and Šešum, N. Non-Kähler Ricci Singularities that Converge to Kähler-Ricci Solitons (2018). arXiv:1703.02918 [math.DG].
\item[] [8] Johar, M.S. Ricci Flow in Milnor Frames (2019). PhD Thesis.
\item[] [9] Protter, M.H., and Weinberger, H.F. Maximum Principles in Differential Equations. Springer-Verlag, New York (1984).
\item[] [10] Šešum, N. Curvature Tensor Under the Ricci Flow. American Journal of Mathematics, 127 (2005), no. 6: 1315-1324.
\item[] [11] Topping, P. Lectures on the Ricci Flow. Cambridge University Press, Cambridge (2006).
\end{itemize}

Modelling and Data Science Centre, National University of Malaysia, Bangi, Malaysia E-mail address: msyajoh@ukm.edu