---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Degenerating conic Kähler–Einstein metrics to the normal cone]

\section*{8. Estimating the error and the obstruction}
8.1. The error. Let us start by estimating $P_{\beta, \varepsilon}(0)$, where $P_{\beta, \varepsilon}$ is defined in (7.6). There are three zones:
\begin{itemize}
\item[-] Zone ( $\rho \geqslant 2 r_{\varepsilon}$ ).
\end{itemize}
Since $\mathrm{Y}^{*} J_{X}-J_{L}$ is horizontal up to order $j$ and $\phi_{\beta, L}$ only depends on $u$, an elementary computation shows that the $(1,1)$-component of $Y_{\varepsilon}^{*} d d^{c} \varphi_{\beta, \varepsilon}-d d^{c} \varphi_{\beta, L}$ is dominated by a multiple of
$$\left|\zeta_{\varepsilon}\right|^{j}\left[\left(\phi_{\beta, L}^{\prime \prime}-\phi_{\beta, L}^{\prime}\right) d u \wedge d^{c} u-\phi_{\beta, L}^{\prime} \omega_{D}\right],$$
where $\zeta_{\varepsilon}$ is defined in (7.2). Given (3.4), we have
$$Y_{\varepsilon}^{*}\left(d d^{c} \varphi_{\beta, \varepsilon}\right)^{n}=\left(d d^{c} \phi_{\beta, L}\right)^{n}\left(1+O\left(\left|\zeta_{\varepsilon}\right|^{j}\left(\left|\frac{\phi_{\beta, L}^{\prime}}{\phi_{\beta, L}^{\prime \prime}}\right|+\left|\frac{\phi_{\beta, L}^{\prime \prime}}{\phi_{\beta, L}^{\prime}}\right|\right)\right)\right) .$$
Now, the ratio $\frac{\phi_{\beta, L}^{\prime \prime}}{\phi_{\beta, L}^{\prime}}$ is globally bounded while $-\frac{\phi_{\beta, L}^{\prime}}{\phi_{\beta, L}^{\prime \prime}}$ is uniformly bounded away from $u=-\infty$ and behaves like $e^{-\beta u}=|\zeta|^{-2 \beta}$ near $D$, cf (3.16). Given (6.4) and (3.3), we have
$$\lambda_{\varepsilon}^{*}\left(\Omega_{L} \wedge \bar{\Omega}_{L}\right)=\varepsilon^{-n} \Omega_{L} \wedge \bar{\Omega}_{L}$$
so that Proposition 5.5 yields
$$\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon^{n} \Omega \wedge \bar{\Omega}\right)=\Omega_{L} \wedge \bar{\Omega}_{L}\left(1-\left|\phi_{j_{0}} \zeta_{\varepsilon}^{j_{0}}\right|^{2}+O\left(\zeta_{\varepsilon}^{2 j_{0}+1}\right)\right)$$
Plugging (8.2) into (7.7), we obtain
$$\begin{aligned}
Y_{\varepsilon}^{*} P_{\beta, \varepsilon}(0) & =\left|\phi_{j_{0}} \zeta_{\varepsilon}^{j_{0}}\right|^{2}+O\left(\zeta_{\varepsilon}^{2 j_{0}+1}\right)+O\left(\left|\zeta_{\varepsilon}\right|^{j-2}\right) \\
& =\left|\phi_{j_{0}}\right|^{2} \cdot\left|\zeta_{\varepsilon}\right|^{2 j_{0}}+O\left(\zeta_{\varepsilon}^{2 j_{0}+1}\right)
\end{aligned}$$
for $j>2\left(j_{0}+1\right)$. We choose such a $j$ from now on. In terms of the coordinate $u$, we have $Y_{\varepsilon}^{*} P_{\beta, \varepsilon}(0)=O\left(\varepsilon^{\frac{j_{0}}{\beta_{*}}} e^{j_{0} u}\right)=O\left(\left(\frac{\varepsilon}{r^{2}}\right)^{v_{0}}\right)$. For any $\delta<2 v_{0}$, the weighed supremum of the latter quantity is attained at $r_{\varepsilon}$, i.e.
$$\sup _{\rho \geqslant 2 r_{\varepsilon}} \rho^{\delta}\left|P_{\beta, \varepsilon}(0)\right| \lessapprox r_{\varepsilon}^{\delta} \varepsilon^{\theta v_{0}} .$$
and the same bound holds as well for the $C_{\delta}^{0, \alpha}$ norm.
\begin{itemize}
\item[-] Zone $\left(2 r_{\varepsilon} \geqslant \rho \geqslant \frac{1}{2} r_{\varepsilon}\right)$.
\end{itemize}
Given (7.5), we have to evaluate $\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}, \varepsilon}\right)-\phi_{\beta, L}$. Since $\lambda_{\varepsilon}^{*}\left(\varepsilon R^{2}\right)=r^{2}$, the second item of Proposition 6.4 yields
$$\begin{aligned}
\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}, \varepsilon}\right) & =\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}}\right)+\sum_{j=2}^{k}\left[a_{j} r^{2 j}+O\left(r^{2 j}\left(\frac{\varepsilon}{r^{2}}\right)^{v_{0}}\right)+O\left(\varepsilon^{j}\left(\frac{\varepsilon}{r^{2}}\right)^{n-1}\right)+O\left(r^{2 k+2}\right)\right] \\
& =\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}}\right)+\left(\sum_{j=2}^{k} a_{j} r^{2 j}\right)+O\left(r^{4}\left(\frac{\varepsilon}{r^{2}}\right)^{v_{0}}\right)+O\left(\varepsilon r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{n}\right)+O\left(r^{2 k+2}\right) \\
& =\left(\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}}\right)-\frac{r^{2}}{4}\right)+\phi_{\beta_{*}}(r)+O\left(r^{4}\left(\frac{\varepsilon}{r^{2}}\right)^{v_{0}}\right)+O\left(\varepsilon r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{n}\right)+O\left(r^{2 k+2}\right) .
\end{aligned}$$

Now, Theorem 6.1 says that
$$\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}}\right)=\frac{r^{2}}{4}+ \begin{cases}O\left(r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{v_{0}}\right) & \text { if } v_{0}<n, \\ a r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{n}\left(\log \frac{r}{\sqrt{\varepsilon}}+O(1)\right) & \\ a r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{n}+O\left(r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{n+\sigma}\right) & \text { if } v_{0}>n,\end{cases}$$
where $\sigma>0$ is small. The error terms in (8.6) are larger than the ones in (8.5), at least in the gluing zone and for $k$ large enough.

Combining (8.6) with (3.45), one infers that in the gluing zone
$$\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}, \varepsilon}\right)-\phi_{\beta, L}= \begin{cases}-a_{L} \frac{\beta-\beta_{*}}{r^{2 n-2}}+O\left(r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{v_{0}}+\frac{\beta-\beta_{*}}{r^{2 n-2}} \cdot \delta(r)\right) & \text { if } v_{0}<n, \\ \frac{a \varepsilon^{n} \log \left(\frac{r}{\sqrt{\varepsilon}}\right)-a_{L}\left(\beta-\beta_{*}\right)}{\sqrt{2 n-2}}+O\left(\frac{\varepsilon^{n}}{r^{2 n-2}}+\frac{\beta-\beta_{*}}{r^{2 n-2}} \cdot \delta(r)\right) & \text { if } v_{0}=n, \\ \frac{a \varepsilon^{n}-a_{L}\left(\beta-\beta_{*}\right)}{r^{2 n-2}}+O\left(r^{2}\left(\frac{\varepsilon}{r^{2}}\right)^{n+\sigma}+\frac{\beta-\beta_{*}}{r^{2 n-2}} \cdot \delta(r)\right) & \text { if } v_{0}>n,\end{cases}$$
where
$$\delta(r):=r^{2}+\frac{\beta-\beta_{*}}{r^{2 n}},$$
and the same estimates hold as well for the weighed derivatives $r^{j} \nabla^{j}$. Next, the tensors $r^{j} \nabla^{j} \chi_{\varepsilon}$ are bounded for any $j$. In light of (7.5) and relying again on the fact that $J-J_{L}$ can be chosen horizontal up to an arbitrary large order, we infer the coarser estimate
$$\left\|Y_{\varepsilon}^{*} \omega_{\beta, \varepsilon}-\omega_{\beta, L}\right\|_{\omega_{\beta, L}}= \begin{cases}O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta v_{0}}\right) & \text { if } v_{0}<n, \\ O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta n} \log \frac{1}{\varepsilon}\right) & \text { if } v_{0}=n, \\ O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta n}\right) & \text { if } v_{0}>n,\end{cases}$$
Similarly, thanks to the estimates of $P_{\beta, \varepsilon}(0)$ obtained in the previous zone we also have
$$\sup _{2 r_{\varepsilon} \geqslant \rho \geqslant \frac{1}{2} r_{\varepsilon}}\left|P_{\beta, \varepsilon}(0)\right|= \begin{cases}O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta v_{0}}\right) & \text { if } v_{0}<n, \\ O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta n} \log \frac{1}{\varepsilon}\right) & \text { if } v_{0}=n, \\ O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta n}\right) & \text { if } v_{0}>n,\end{cases}$$
and the weighted $C_{\delta}^{0, \alpha}$ estimate on the considered zone follows immediately from (8.10) since $\rho \simeq r_{\varepsilon}$.
\begin{itemize}
\item[-] Zone ( $\rho \leqslant \frac{1}{2} r_{\varepsilon}$ ).
\end{itemize}

The first second item of Proposition 6.4 shows that
$$\sup _{\rho \leqslant \frac{1}{2} r_{\varepsilon}} \rho^{\delta}\left|P_{\beta, \varepsilon}(0)\right| \lessapprox r_{\varepsilon}^{2 k+2+\delta} .$$
where $k$ can be chosen arbitrary large and the same bound holds for the $C_{\delta}^{0, \alpha}$ norm. Said otherwise, the "Tian-Yau" zone will not contribute to the error terms.

In conclusion, we find that for any $\delta \in\left(0,2 v_{0}\right)$, we have
$$\left\|P_{\beta, \varepsilon}(0)\right\|_{C_{\delta}^{0, \alpha}}= \begin{cases}O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n-\delta}}+r_{\varepsilon}^{\delta} \varepsilon^{\theta v_{0}}\right) & \text { if } v_{0}<n, \\ O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n-\delta}}+r_{\varepsilon}^{\delta} \varepsilon^{\theta n} \log \frac{1}{\varepsilon}\right) & \text { if } v_{0}=n, \\ O\left(\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n-\delta}}+r_{\varepsilon}^{\delta} \varepsilon^{\theta n}\right) & \text { if } v_{0}>n .\end{cases}$$
8.2. The obstruction. In this section, we estimate
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle=\int_{X} P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon} d \operatorname{vol}_{g_{\beta, \varepsilon}}$$
where $\tau_{\beta, \varepsilon}$ has been defined in (7.19). Here again, we study each of the three zones separately.
- Zone ( $\rho \geqslant 2 r_{\varepsilon}$ ).

Here, we have $\mathrm{Y}_{\varepsilon}^{*} \tau_{\beta, \varepsilon}=\phi_{\beta, L}^{\prime}+\lambda_{\beta}$. Since we can work as if $\phi$ were horizontal, the estimate (8.3) shows that the main contribution to be computed is $\varepsilon^{v_{0}} \cdot I_{\varepsilon, \beta}$ where
$$\begin{aligned}
I_{\varepsilon, \beta} & :=\int_{u \leqslant u_{\varepsilon}-\log 4}\left|\phi_{j_{0}}\right|^{2} e^{j_{0} u}\left(\phi_{\beta, L}^{\prime}+\lambda_{\beta}\right) \cdot \phi_{\beta, L}^{\prime \prime}\left(-\phi_{\beta, L}^{\prime}\right)^{n-1} d u \wedge d^{c} u \wedge \omega_{D}^{n-1} \\
& =\int_{u \leqslant u_{\varepsilon}-\log 4}\left|\phi_{j_{0}}\right|^{2} e^{\beta_{*}\left(v_{0}-n\right) u}\left(\phi_{\beta, L}^{\prime}+\lambda_{\beta}\right) \cdot e^{-\mu \phi_{\beta, L}} d u \wedge d^{c} u \wedge \omega_{D}^{n-1}
\end{aligned}$$
Performing fiberwise integral we are reduced to studying the 1D integral
$$J_{\beta, \varepsilon}:=\int_{-\infty}^{u_{\varepsilon}-\log 4} e^{\beta_{*}\left(v_{0}-n\right) u}\left(\phi_{\beta, L}^{\prime}+\lambda_{\beta}\right) \cdot e^{-\mu \phi_{\beta, L}} d u .$$
Near $u=-\infty$, the integral is indeed convergent since $e^{-\mu \phi_{\beta, L}} \approx e^{\left(n \beta_{*}+\beta\right) u}$. Near 0 , the integrand behaves like $e^{\beta_{*}\left(v_{0}-n\right) u}$ hence it will converge (when $r_{\varepsilon} \rightarrow 0$ ) if and only if $v_{0}<n$. The sign of the integral at the limit is crucial but not obvious
at this point since $\phi_{\beta, L}^{\prime}+\lambda_{\beta}$ does not have a sign (it is negative near $D$ and positive near the conical point). Let us work out this issue next and separate three cases.
$a$. Case $v_{0}<n$. One writes
$$e^{\beta_{*}\left(v_{0}-n\right) u}\left(\phi_{\beta, L}^{\prime}+\lambda_{\beta}\right) \cdot e^{-\mu \phi_{\beta, L}}=-\frac{1}{\mu} e^{\beta_{*} v_{0} u} \cdot\left(e^{-\mu \phi_{\beta, L}-n \beta_{*} u}\right)^{\prime}$$
and integrates by parts to obtain
$$J_{\beta, \varepsilon}=\frac{\beta_{*} v_{0}}{\mu} \int_{-\infty}^{u_{\varepsilon}-\log 4} e^{\beta_{*}\left(v_{0}-n\right) u-\mu \phi_{\beta, L}} d u+O\left(e^{\beta_{*}\left(v_{0}-n\right) u_{\varepsilon}}\right)$$
hence there is a number $a_{\beta}>0$ converging to a positive number $a_{\beta_{*}}$ when $\beta \rightarrow$ $\beta_{*}$ such that
$$I_{\beta, \varepsilon}=a_{\beta}+O\left(r_{\varepsilon}^{2\left(n-v_{0}\right)}\right) .$$
$b$. Case $v_{0}=n$. Thanks to (3.40), we find a positive number $a_{\beta}^{\prime}$ such that
$$I_{\beta, \varepsilon}=a_{\beta}^{\prime} u_{\varepsilon}+O(1) .$$
$c$. Case $v_{0}>n$. The rough estimate $I_{\varepsilon, \beta}=O\left(r_{\varepsilon}^{2\left(n-v_{0}\right)}\right)$ will suffice. All in all, we have (up to scaling $a_{\beta}^{\prime}$ )
$$\int_{\rho \geqslant 2 r_{\varepsilon}} P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon} d \operatorname{vol}_{g_{\beta, \varepsilon}}=\left\{\begin{array}{lll}
a_{\beta} \varepsilon^{v_{0}}+O\left(r_{\varepsilon}^{2 n} \varepsilon^{\theta v_{0}}\right) & \text { if } & v_{0}<n, \\
a_{\beta}^{\prime} \varepsilon^{n} \log \frac{1}{r_{\varepsilon}}+O\left(\varepsilon^{n}\right) & \text { if } & v_{0}=n \\
O\left(\varepsilon^{\theta v_{0}} r_{\varepsilon}^{2 n}\right) & \text { if } & v_{0}>n .
\end{array}\right.$$
- Zone $\left(2 r_{\varepsilon} \geqslant \rho \geqslant \frac{1}{2} r_{\varepsilon}\right)$.

To lighten the notation in this paragraph, let us set $A_{\varepsilon}:=\mathrm{Y}_{\varepsilon}^{-1}\left(\left\{2 r_{\varepsilon} \geqslant \rho \geqslant\right.\right.$ $\left.\left.\frac{1}{2} r_{\varepsilon}\right\}\right) \approx\left(2 r_{\varepsilon} \geqslant r \geqslant \frac{1}{2} r_{\varepsilon}\right)$ and
$$\psi_{\beta, \varepsilon}:=\left(1-\chi_{\varepsilon}\right)\left(\mathrm{Y}_{\varepsilon}^{*}\left(\varepsilon \Phi_{\mathrm{TY}, \varepsilon}\right)-\phi_{\beta, L}\right)$$
so that
$$Y_{\varepsilon}^{*} \omega_{\beta, \varepsilon}=d d^{c} \phi_{\beta, L}+d d^{c} \psi_{\beta, \varepsilon}+\text { h.o.t. }$$
by (7.5). If we additionnally set
$$E:= \begin{cases}\frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta v_{0}} & \text { if } v_{0}<n, \\ \frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta n} \log \frac{1}{\varepsilon} & \text { if } v_{0}=n, \\ \frac{\beta-\beta_{*}}{r_{\varepsilon}^{2 n}}+\varepsilon^{\theta n} & \text { if } v_{0}>n,\end{cases}$$
we see from (8.7) and (8.10) that
$$\sup _{A_{\varepsilon}}\left|\psi_{\beta, \varepsilon}\right|=O\left(r_{\varepsilon}^{2} E\right), \quad \text { and } \quad \sup _{A_{\varepsilon}}\left(\left|d d^{c} \psi_{\beta, \varepsilon}\right|_{\omega_{\beta, L}}+\left|\mathrm{Y}_{\varepsilon}^{*} P_{\beta, \varepsilon}(0)\right|\right)=O(E) .$$
Thanks to (8.16) and the almost horizontality of $\phi$ as well as
$$\mathrm{Y}_{\varepsilon}^{*} \omega_{\beta, \varepsilon}^{n}=\omega_{\beta, L}^{n}(1+O(E)) .$$
The integral we need to estimate is
$$\begin{aligned}
\int_{A_{\varepsilon}} \mathrm{Y}_{\varepsilon}^{*}\left(P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon} \omega_{\beta, \varepsilon}^{n}\right) & \left.=\int_{A_{\varepsilon}} \mathrm{Y}_{\varepsilon}^{*}\left(P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon}\right) \omega_{\beta, L}^{n}+O\left(r_{\varepsilon}^{2 n} E \sup _{2 r_{\varepsilon} \geqslant \rho \geqslant \frac{1}{2} r_{\varepsilon}}\left|P_{\beta, \varepsilon}(0)\right|\right)\right) \\
& =\int_{A_{\varepsilon}} \mathrm{Y}_{\varepsilon}^{*}\left(P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon}\right) \omega_{\beta, L}^{n}+O\left(r_{\varepsilon}^{2 n} E^{2}\right)
\end{aligned}$$
thanks to (8.18). So from now on we focus on the integral $\int_{A_{\varepsilon}} \mathrm{Y}_{\varepsilon}^{*}\left(P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon}\right) \omega_{\beta, L}^{n}$.
First, we write
$$Y_{\varepsilon}^{*} P_{\beta, \varepsilon}(0)=\log \frac{\left|\Omega_{L}\right|^{2}}{Y_{\varepsilon}^{*}\left(\varepsilon^{n}|\Omega|^{2}\right)}+L_{\beta} \psi_{\beta, \varepsilon}+Q\left(d d^{c} \psi_{\beta, \varepsilon}\right)$$
where $L_{\beta}=\Delta_{\omega_{\beta, L}}+\mu_{\beta}$ and $Q\left(d d^{c} \psi_{\beta, \varepsilon}\right)=O\left(E^{2}\right)$. In the gluing zone where we are working, the estimate (8.2) reads
$$\log \frac{\left|\Omega_{L}\right|^{2}}{Y_{\mathcal{E}}^{*}\left(\varepsilon^{n}|\Omega|^{2}\right)}=O\left(\varepsilon^{\theta v_{0}}\right) .$$
Since $Y_{\varepsilon}^{*} \tau_{\beta, \varepsilon} \approx \lambda_{\beta}$, we have
$$\left(\mu_{\beta} \psi_{\beta, \varepsilon}+Q\left(d d^{c} \psi_{\beta, \varepsilon}\right)\right) \cdot \mathrm{Y}_{\varepsilon}^{*} \tau_{\beta, \varepsilon}=O\left(r_{\varepsilon}^{2} E+E^{2}\right)$$
by (8.18). We are left to evaluating
$$I:=\int_{A_{\varepsilon}} \Delta_{\omega_{\beta, L}} \psi_{\beta, \varepsilon} \cdot\left(\chi_{\varepsilon} \phi_{\beta, L}^{\prime}+\lambda_{\beta}\right) \omega_{\beta, L}^{n}=I_{1}+I_{2}+I_{3},$$
where
$$I_{1}=\int_{A_{\varepsilon}} \psi_{\beta, \varepsilon} \cdot \Delta_{\omega_{\beta, L}}\left(\chi_{\varepsilon} \phi_{\beta, L}^{\prime}\right) \omega_{\beta, L}^{n}$$
and
$$I_{2}=-\int_{r=\frac{1}{2} r_{\varepsilon}} \partial_{v} \psi_{\beta, \varepsilon} \cdot\left(\phi_{\beta, L}^{\prime}+\lambda_{\beta}\right) d \sigma, \quad I_{3}=\int_{r=\frac{1}{2} r_{\varepsilon}} \psi_{\varepsilon} \cdot \partial_{v} \phi_{\beta, L}^{\prime} d \sigma$$
thanks to Stokes theorem since $\psi_{\beta, \varepsilon}=0$ near $r=2 r_{\varepsilon}$, where $v$ is the outward normal vector and $\sigma$ is the measure on ( $r=c s t$ ) induced by $\omega_{\beta, L}$. From (3.4) and (3.47), we see that $\partial_{v}=\left(c_{1}+O(\delta(r)) \partial_{r}\right.$ and $d \sigma=\left(c_{2}+O(\delta(r)) r^{2 n-1} \eta \wedge d \mathrm{vol}_{g_{D}}\right.$ where $c_{1}, c_{2}$ are positive constants and $\delta(r)$ has been defined in (8.8).

Let us first deal with $I_{1}$. We have $\left|\Delta_{\omega_{\beta, L}} \chi_{\varepsilon}\right|+\left|\nabla \chi_{\varepsilon}\right|^{2}=O\left(r_{\varepsilon}^{-2}\right)$. Moreover, the estimate $\phi_{\beta, L}^{\prime}=O\left(r^{2}\right)$ derived from (3.45) can be iterated to higher orders by (3.7) to obtain $\Delta_{\omega_{\beta, L}}\left(\chi_{\varepsilon} \phi_{\beta, L}^{\prime}\right)=O(1)$. Combined with (8.18), this shows that the integrand in $I_{1}$ is a $O\left(r_{\varepsilon}^{2} E\right)$ so that
$$I_{1}=O\left(r_{\varepsilon}^{2 n+2} E\right) .$$

Let us now get to $I_{2}$. We have $\phi_{\beta, L}^{\prime}+\lambda_{\beta}=\lambda_{\beta}+O\left(r_{\mathcal{E}}^{2}\right)$ and thanks to (8.7)
$$\frac{-1}{2 n-2} \partial_{r} \psi_{\beta, \varepsilon}= \begin{cases}-a_{L} \frac{\beta-\beta_{*}}{r^{2 n-1}}+O\left(r \varepsilon^{\theta v_{0}}+\frac{\beta-\beta_{*}}{r^{2 n-1}} \cdot \delta(r)\right) & \text { if } v_{0}<n, \\ a \varepsilon^{n} \log \left(\frac{r}{\sqrt{\varepsilon}}\right)-a_{L}\left(\beta-\beta_{*}\right) \\ \frac{a \varepsilon^{n}-a_{L}\left(\beta^{2 n-\beta_{*}}\right)}{r^{2 n-1}}+O\left(r \varepsilon^{\theta(n+\sigma)}+\frac{\varepsilon^{n}}{r^{2 n-1}}+\frac{\beta-\beta_{*}}{r^{2 n-1}} \cdot \delta(r)\right) & \text { if } v_{0}=n, \\ \text { if } v_{0}>n .\end{cases}$$
Therefore, there exists a positive constant $\kappa=\kappa\left(v_{0}, \beta\right)>0$ such that
$$I_{2}= \begin{cases}-\kappa\left(\beta-\beta_{*}\right)+O\left(r_{\varepsilon}^{2 n} \varepsilon^{\theta v_{0}}+\left(\beta-\beta_{*}\right) \cdot \delta(r)\right) & \text { if } v_{0}<n, \\ \kappa\left(a \varepsilon^{n} \log \left(\frac{r_{\varepsilon}}{\sqrt{\varepsilon}}\right)-a_{L}\left(\beta-\beta_{*}\right)\right)+O\left(\varepsilon^{n}+\left(\beta-\beta_{*}\right) \cdot \delta(r)\right) & \text { if } v_{0}=n, \\ \kappa\left(a \varepsilon^{n}-a_{L}\left(\beta-\beta_{*}\right)\right)+O\left(r_{\varepsilon}^{2 n} \varepsilon^{\theta(n+\sigma)}+\left(\beta-\beta_{*}\right) \cdot \delta(r)\right) & \text { if } v_{0}>n .\end{cases}$$

Finally, we have $\psi_{\beta, \varepsilon} \cdot \partial_{\nu} \phi_{\beta, L}^{\prime}=O\left(r_{\varepsilon}^{3} E\right)$ which shows that
$$I_{3}=O\left(r_{\varepsilon}^{2 n+2} E\right) .$$

Given (8.20), (8.22), (8.23), (8.24) and (8.26), all the terms contributing to $\int_{A_{\varepsilon}} \mathrm{Y}_{\varepsilon}^{*}\left(P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon} \omega_{\beta, \varepsilon}^{n}\right)$ except for $I_{2}$ are dominated by
$$r_{\varepsilon}^{2 n} E^{2}+r_{\varepsilon}^{2 n+2} E+r^{2 n} \varepsilon^{\theta v_{0}}$$
and it is straightforward to see that these terms are at most of the same order as the error term in the integral $I_{2}$, cf (8.25). In conclusion,
$$\int_{2 r_{\varepsilon} \geqslant \rho \geqslant \frac{1}{2} r_{\varepsilon}} P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon} d \operatorname{vol}_{g_{\beta, \varepsilon}}= \begin{cases}-\kappa\left(\beta-\beta_{*}\right)+O\left(r_{\varepsilon}^{2 n} \varepsilon^{\theta v_{0}}+\left(\beta-\beta_{*}\right) \cdot \delta(r)\right) & \text { if } v_{0}<n, \\ \kappa\left(a \varepsilon^{n} \log \left(\frac{r_{\varepsilon}}{\sqrt{\varepsilon}}\right)-a_{L}\left(\beta-\beta_{*}\right)\right)+O\left(\varepsilon^{n}+\left(\beta-\beta_{*}\right) \cdot \delta(r)\right) & \text { if } v_{0}=n, \\ \kappa\left(a \varepsilon^{n}-a_{L}\left(\beta-\beta_{*}\right)\right)+O\left(r_{\varepsilon}^{2 n} \varepsilon^{\theta(n+\sigma)}+\left(\beta-\beta_{*}\right) \cdot \delta(r)\right) & \text { if } v_{0}>n .\end{cases}$$
- Zone ( $\rho \leqslant \frac{1}{2} r_{\varepsilon}$ ).

Since the volume of the zone is of order $\varepsilon^{n} R_{\varepsilon}^{2 n}=r_{\varepsilon}^{2 n}$, the second item of Proposition 6.4 shows that
$$\int_{\rho \leqslant \frac{1}{2} r_{\varepsilon}} P_{\beta, \varepsilon}(0) \tau_{\beta, \varepsilon} d \operatorname{vol}_{g_{\beta, \varepsilon}}=O\left(r_{\varepsilon}^{2 n+2 k+2}\right) .$$
where $k$ can be chosen arbitrary large. As before, this zone will not contribute to the obstruction.

In conclusion, the estimates (8.15), (8.27) and (8.28) imply that they are positive constants $\kappa_{i}=\kappa_{i}\left(\nu_{0}, \beta\right)$ for $i=1, \ldots, 6$ (where the dependence in $\beta$ is continuous up to $\beta=\beta_{*}$ and $\kappa_{i}\left(\nu_{0}, \beta_{*}\right)>0$ ) such that
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle= \begin{cases}\kappa_{1} \varepsilon^{v_{0}}-\kappa_{2}\left(\beta-\beta_{*}\right)+O\left(r_{\varepsilon}^{2 n} \varepsilon^{\theta v_{0}}+\left(\beta-\beta_{*}\right) \cdot \delta\left(r_{\varepsilon}\right)\right) & \text { if } v_{0}<n, \\ \kappa_{3} \varepsilon^{n} \log \frac{1}{\varepsilon}-\kappa_{4}\left(\beta-\beta_{*}\right)+O\left(\varepsilon^{n}+\left(\beta-\beta_{*}\right) \cdot \delta\left(r_{\varepsilon}\right)\right) & \text { if } v_{0}=n, \\ \kappa_{5} \varepsilon^{n}-\kappa_{6}\left(\beta-\beta_{*}\right)+O\left(r_{\varepsilon}^{2 n} \varepsilon^{n \theta+\sigma}+\left(\beta-\beta_{*}\right) \cdot \delta\left(r_{\varepsilon}\right)\right) & \text { if } v_{0}>n .\end{cases}$$
This is clear except maybe in the case where $v_{0}=n$, where the first term $\kappa_{3} \varepsilon^{n} \log \frac{1}{\varepsilon}$ comes from the contributions of the obstruction from both the normal bundle (term $a_{\beta}^{\prime} \varepsilon^{n} \log \frac{1}{r_{\varepsilon}}=\frac{1}{2}(1-\theta) a_{\beta}^{\prime} \varepsilon^{n} \log \frac{1}{\varepsilon}$ ) and the gluing zone (term $\kappa a \varepsilon^{n} \log \frac{r_{\varepsilon}}{\sqrt{\varepsilon}}=$ $\frac{1}{2} \theta κ a \varepsilon^{n} \log \frac{1}{\varepsilon}$ ) which are both positive.
8.3. Choice of $\varepsilon=\varepsilon(\beta)$. Given (8.29), it is natural to introduce the scaling parameter $\varepsilon_{\beta}$ satisfying
$$\beta-\beta_{*}= \begin{cases}\frac{\kappa_{1}}{\kappa_{2}} \cdot \varepsilon_{\beta}^{v_{0}} & \text { if } v_{0}<n, \\ \frac{\kappa_{3}}{\kappa_{4}} \cdot \varepsilon_{\beta}^{n} \log \frac{1}{\varepsilon_{\beta}} & \text { if } v_{0}=n, \\ \frac{\kappa_{5}}{\kappa_{6}} \cdot \varepsilon_{\beta}^{n} & \text { if } v_{0}>n\end{cases}$$
and then we choose from now on $\varepsilon$ close to $\varepsilon_{\beta}$ in the sense that
$$\varepsilon=\varepsilon_{\beta}(1+\eta) \quad \text { with } \quad|\eta| \ll 1$$
where $\eta \in \mathbb{R}$ will be allowed to vary later for the purpose of solving out Monge-Ampère equation; in particular it will be important that $\eta$ takes positive and negative values. Let us be more precise now and distinguish the three possible cases.
- Case $v_{0}<n$.

Condition (7.3) translates into
$$\theta>1-\frac{v_{0}}{n},$$
which can be fulfilled. Next, we have
$$\kappa_{1} \varepsilon^{v_{0}}-\kappa_{2}\left(\beta-\beta_{*}\right)=v_{0} \kappa_{1} \varepsilon_{\beta}^{v_{0}} \cdot\left(\eta+O\left(\eta^{2}\right)\right)$$
while the error term in (8.29) is of order
$$r_{\varepsilon}^{2 n} \varepsilon^{\theta v_{0}}+\left(\beta-\beta_{*}\right) \cdot \delta\left(r_{\varepsilon}\right) \approx \varepsilon^{v_{0}}\left(\varepsilon^{(1-\theta)\left(n-v_{0}\right)}+\varepsilon^{1-\theta}+\varepsilon^{v_{0}-n(1-\theta)}\right)$$
and the latter is a $O\left(\varepsilon_{\beta}^{v_{0}+(1-\theta) \min \left\{1, n-v_{0}\right\}}\right)$ as soon as $\theta>1-\frac{v_{0}-1}{n}$, which we assume from now on. Then we have
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle=v_{0} \kappa_{1} \varepsilon_{\beta}^{v_{0}} \cdot\left(\eta+O\left(\varepsilon^{(1-\theta) \min \left\{1, n-v_{0}\right\}}\right)+O\left(\eta^{2}\right)\right) .$$
Moreover, the quantity $E$ in (8.17) behaves like $\varepsilon_{\beta}^{v_{0}-n(1-\theta)}$.
- Case $v_{0}=n$.

Condition (7.3) is automatic. Next, we have
$$\kappa_{3} \varepsilon^{n} \log \frac{1}{\varepsilon}-\kappa_{4}\left(\beta-\beta_{*}\right)=n \kappa_{3} \varepsilon_{\beta}^{n} \log \frac{1}{\varepsilon_{\beta}} \cdot\left(\eta+O\left(\frac{\eta}{\log \frac{1}{\varepsilon_{\beta}}}\right)+O\left(\eta^{2}\right)\right)$$
while the order of the error term $O\left(\varepsilon^{n}+\left(\beta-\beta_{*}\right) \cdot \delta\left(r_{\varepsilon}\right)\right)$ is simply $O\left(\varepsilon_{\beta}^{n}\right)$. We then have
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle=n \kappa_{3} \varepsilon_{\beta}^{n} \log \frac{1}{\varepsilon_{\beta}} \cdot\left(\eta+O\left(\frac{1}{\log \frac{1}{\varepsilon_{\beta}}}\right)+O\left(\eta^{2}\right)\right) .$$

Moreover, $E$ behaves like $\varepsilon_{\beta}^{n \theta} \log \frac{1}{\varepsilon_{\beta}}$.
\begin{itemize}
\item[-] Case $v_{0}>n$.
\end{itemize}

Condition (7.3) is automatic too and
$$\kappa_{5} \varepsilon^{n}-\kappa_{6}\left(\beta-\beta_{*}\right)=n \kappa_{5} \varepsilon_{\beta}^{n} \cdot\left(\eta+O\left(\eta^{2}\right)\right)$$
while the order of the error term $O\left(r_{\varepsilon}^{2 n} \varepsilon^{n \theta+\sigma}+\left(\beta-\beta_{*}\right) \cdot \delta\left(r_{\varepsilon}\right)\right)$ is $O\left(\varepsilon_{\beta}^{n+\sigma}\right)$ as soon as $\theta>\frac{1}{n+1}$. Therefore, we get
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle=n \kappa_{5} \varepsilon_{\beta}^{n} \cdot\left(\eta+O\left(\varepsilon_{\beta}^{\sigma}\right)+O\left(\eta^{2}\right)\right) .$$
Moreover, $E$ behaves like $\varepsilon_{\beta}^{n \theta}$.
In summary, we get from (8.12) and the case by case analysis just above
Proposition 8.1. If $\beta, \varepsilon, \eta$ are chosen as in (8.30)-(8.31), then there exists $\kappa \in \mathbb{R}$ satisfying
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle=\left(\beta-\beta_{*}\right) \cdot\left(\kappa \eta+O(F)+O\left(\eta^{2}\right)\right)$$
and $\kappa$ is such that $\kappa_{0} \leqslant|\kappa| \leqslant \kappa_{0}^{-1}$ for some constant $\kappa_{0}>0$ independent of $\beta, \varepsilon$ and
$$F:= \begin{cases}\varepsilon_{\beta}^{(1-\theta) \min \left\{1, n-v_{0}\right\}} & \text { if } v_{0}<n, \\ \frac{1}{\log \frac{1}{\varepsilon_{\beta}}} & \text { if } v_{0}=n, \\ \varepsilon_{\beta}^{\sigma} & \text { if } v_{0}>n .\end{cases}$$
Moreover, if $\delta \in\left(0,2 v_{0}-2\right)$, we have
$$\left\|P_{\beta, \varepsilon}(0)\right\|_{C_{\delta+2}^{0, \alpha}}=O\left(r_{\varepsilon}^{\delta+2} E\right)$$
where the $O()$ is uniform in $\beta, \varepsilon, \eta$ and $E$ is defined by
$$E:= \begin{cases}\varepsilon^{v_{0}-n(1-\theta)} & \text { if } v_{0}<n, \\ \varepsilon^{n \theta} \log \frac{1}{\varepsilon} & \text { if } v_{0}=n, \\ \varepsilon^{n \theta} & \text { if } v_{0}>n .\end{cases}$$

\section*{9. Resolution of the Monge-Ampère equation}
9.1. Resolution modulo the obstruction. The first step is to solve the Monge-Ampère equation up to the obstruction term. More precisely, we have

Proposition 9.1. Let $\delta \in(0,1)$. Suppose $\varepsilon$ close enough to 0 and $0<\beta-\beta_{*}<$ $c \varepsilon^{\inf \left(v_{0}, n\right)}$ (or $c \varepsilon^{n} \log \frac{1}{\varepsilon}$ is $v_{0}=n$ ), where $c$ is some fixed constant. Then there exists a unique function $f_{\beta, \varepsilon} \in C_{\delta}^{2, \alpha}(X)^{G, \perp}$ such that
$$P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right)^{\perp}=0 \quad \text { and } \quad\left\|f_{\beta, \varepsilon}\right\|_{C_{\delta}^{2, \alpha}} \leqslant C\left\|P_{\beta, \varepsilon}(0)^{\perp}\right\|_{C_{\delta+2}^{0, \alpha}}$$
for some constant $C>0$ independent of $\beta, \varepsilon$.
Remark 9.2. We will see in the proof that it is crucial to have $\left\|P_{\beta, \varepsilon}(0)\right\|_{C_{2+\delta}^{\alpha}} \ll$ $\varepsilon^{1+\frac{\delta}{2}}$. If one had not replaced the Tian-Yau metric by its formal perturbation (or had only done it up to, say, order $R^{4}$ in the potential so that $\operatorname{Ric}\left(\varepsilon \omega_{\mathrm{TY}, \mathcal{E}}\right) \approx$ $\varepsilon \omega_{\mathrm{TY}, \mathcal{E}}$ ), the Tian-Yau part would contribute a factor $r_{\varepsilon}^{4+\delta}=\varepsilon^{(1-\theta)\left(2+\frac{\delta}{2}\right)}$ (resp. $r_{\varepsilon}^{6+\delta}=\varepsilon^{(1-\theta)\left(3+\frac{\delta}{2}\right)}$ ) in the norm $\left\|P_{\beta, \varepsilon}(0)\right\|_{C_{2+\delta}^{\alpha}}$ and the latter need not be small compared to $\varepsilon^{1+\frac{\delta}{2}}$ since $\theta$ will have to be chosen arbitrarily close to 1 in the proof of Proposition 9.3 below.

Proof. Given any $v^{\prime}<\inf \left(v_{0}, n\right)$ (which we take very close to $\inf \left(v_{0}, n\right)$ ), Proposition 8.1 shows that for $\theta<1$ close enough to 1 we have
$$\left\|P_{\beta, \varepsilon}(0)\right\|_{C_{2+\delta}^{0, \alpha}}=O\left(\varepsilon^{v^{\prime}}\right) .$$

The quadratic term $Q_{\beta, \varepsilon}$ of the equation, defined by (7.8), is controled exactly as in [BM11, § 1.4]: it satisfies
$$\left|Q_{\beta, \varepsilon}\left(f_{1}\right)-Q_{\beta, \varepsilon}\left(f_{2}\right)\right| \leq C\left|d d^{c}\left(f_{1}-f_{2}\right)\right|\left(\left|d d^{c} f_{1}\right|+\left|d d^{c} f_{2}\right|\right)$$
as soon as $\left|d d^{c} f_{j}\right| \leq 1$ for $j=1,2$. Our weighted space $C_{\delta+2}^{0}$ carries a (small) weight $\varepsilon^{1+\frac{\delta}{2}}$ on the Tian-Yau part, and it follows that
$$\left\|Q_{\beta, \varepsilon}\left(f_{1}\right)-Q_{\beta, \varepsilon}\left(f_{2}\right)\right\|_{C_{2+\delta}^{0}} \leq C \varepsilon^{-1-\frac{\delta}{2}}\left\|d d^{c}\left(f_{1}-f_{2}\right)\right\|_{C_{2+\delta}^{0}}\left(\left\|d d^{c} f_{1}\right\|_{C_{2+\delta}^{0}}+\left\|d d^{c} f_{2}\right\|_{C_{2+\delta}^{0}}\right) .$$
This estimate extends to the Hölder spaces $C_{2+\delta}^{\alpha}$ by local change of scale.
Finally we have a uniform estimate for the inverse of the linearization provided by Proposition 7.8. One can then apply an inverse function theorem on the equation $P_{\beta, \varepsilon}(f)^{\perp}=0$, provided that $\left\|P_{\beta, \varepsilon}(0)\right\|_{C_{2+\delta}^{\alpha}} \ll \varepsilon^{1+\frac{\delta}{2}}$, see for example
[BM11, Lemma 1.3]. Therefore from (9.1) it is sufficient to have $v^{\prime}>1+\frac{\delta}{2}$, which can be achieved provided $\inf \left(v_{0}, n\right)>1$, that is provided that $v_{0}>1$ which is true since $\beta_{*}<1$. \(\square\)
9.2. Killing the obstruction by varying $\varepsilon$. The outcome of Proposition 9.1 is that for fixed $(\varepsilon, \beta)$ close enough to $\left(0, \beta_{*}\right)$, there exists a unique couple of a function and a scalar $\left(f_{\beta, \varepsilon}, a_{\beta, \varepsilon}\right) \in C_{\delta}^{2, \alpha}(X)^{G, \perp} \times \mathbb{R}$ such that
$$P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right)=a_{\beta, \varepsilon} \tau_{\beta, \varepsilon} .$$
The object of the next proposition is to precisely measure the effect that varying the cone angle (or the scale parameter $\varepsilon$ ) has on the obstruction $a_{\beta, \varepsilon}$. Most of the work has already been done in Proposition 8.1.

Proposition 9.3. Let $\beta, \varepsilon, \eta$ as in (8.30)-(8.31). For a fixed choice of $\delta, \theta \in(0,1)$ such that $\delta+(1-\theta) \ll 1$, we have
$$\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle=\left(\beta-\beta_{*}\right) \cdot\left(\kappa \eta+O(F)+O\left(\eta^{2}\right)\right)$$
where $\kappa, F$ are the ones from Proposition 8.1.
Proof. Given (8.36), all we have left to prove is that
$$\left\langle L_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle+\left\langle Q_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle=o\left(\eta\left(\beta-\beta_{*}\right)\right) .$$

We proceed in several steps.
Step 1. Preliminaries.
We first claim that
$$\left\|f_{\beta, \varepsilon}\right\|_{C_{\delta}^{2, \alpha}}=O\left(r_{\varepsilon}^{\delta+2} E\right),$$
where $E$ is given in (8.38). Indeed, (8.36) shows that
$$\left|P_{\beta, \varepsilon}(0)^{\perp}\right| \leqslant\left|P_{\beta, \varepsilon}(0)\right|+\frac{1}{\left|\tau_{\beta, \varepsilon}\right|} \cdot\left|\left\langle P_{\beta, \varepsilon}(0), \tau_{\beta, \varepsilon}\right\rangle\right|=O(E+|\gamma|) .$$
Now one can easily check that $|\gamma| \ll E$ since $\theta<1$. The estimate (9.5) is then a consequence of Proposition 9.1 and (8.37).

Next, we claim that
$$\left|d d^{c} f_{\beta, \varepsilon}\right| \omega_{\beta, \varepsilon}=o(1) .$$

This is an immediate consequence of (9.5) on $\rho \geqslant \frac{1}{2} r_{\varepsilon}$ given the definition of our norms and the fact that $E=o(1)$. So it remains to check the claim on the Tian-Yau part. There, one can just write $\left|d d^{c} f_{\beta, \varepsilon}\right|_{\omega_{\beta, \varepsilon}} \leqslant \rho^{-\delta-2}\left\|f_{\beta, \varepsilon}\right\|_{C_{\delta}^{2, \alpha}}=O\left(\varepsilon^{-\theta\left(\frac{\delta}{2}+1\right)} E\right)$. If $v_{0}<n$, the latter goes to zero provided that $\theta>\frac{n-v_{0}}{n-1-\frac{\delta}{2}}$ which can always be achieved for some $\delta, \theta \in(0,1)$ since $v_{0}>1$. If $v_{0} \geqslant n$, it goes to zero provided $\delta<2(n-1)$ which can also be achieved since we have assumed that $n>1$.

Step 2. The term $\left\langle L_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle$.
By Lemma 7.7, the integral $I:=\left\langle L_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle$ satisfies
$$I=O\left(r_{\varepsilon}^{2 n-\delta}\|f\|_{C_{\delta}^{0}}\right)=O\left(r_{\varepsilon}^{2 n+2} E\right)$$
where the last identity follows from (9.5). We have
$$r_{\varepsilon}^{2 n+2} E= \begin{cases}\varepsilon^{v_{0}+(1-\theta)} & \text { if } v_{0}<n, \\ \varepsilon^{n+1-\theta} \log \frac{1}{\varepsilon} & \text { if } v_{0}=n, \\ \varepsilon^{n+1-\theta} & \text { if } v_{0}>n .\end{cases}$$
and the latter is a $O\left(\left(\beta-\beta_{*}\right) F\right)$ since $\varepsilon_{\beta}^{1-\theta}=O(F)$ - as soon as $\sigma<1-\theta$ in the case $v_{0}>n$.

Step 3. The term $\left\langle Q_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle$.
Thanks to (9.6), the second estimate from Lemma 7.7 is valid for $f=f_{\beta, \varepsilon}$, hence $\left\langle Q_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle=O\left(\left\|f_{\beta, \varepsilon}\right\|_{C_{\delta}^{2, \alpha}}^{2}\right)$ if $n>2$ and $\delta<n-2$ and $\left\langle Q_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle=$ $O\left(\varepsilon^{-\delta}\left\|f_{\beta, \varepsilon}\right\|_{C_{\delta}^{2, \alpha}}^{2}\right)$ if $n=2$.

Assume that $n>2$ for now. Given (9.5), we have to prove that
$$r_{\varepsilon}^{2 \delta+2} E^{2}=O\left(\left(\beta-\beta_{*}\right) F\right) .$$
We will show actually show that
$$r_{\varepsilon}^{2} E^{2}=\varepsilon^{1-\theta} E^{2}=O\left(\left(\beta-\beta_{*}\right) F\right)$$
for suitable $\theta$. More precisely, if $v_{0}<n$, we choose $\theta>1-\frac{v_{0}}{n}$ while if $v_{0} \geqslant n$ we choose $\theta>\frac{n-1}{2 n-1}$. In the first case, one has automatically $(1-\theta)+2 v_{0}-2(1-$
$\theta) n>(1-\theta)$. In the second case, we have $1-\theta+2 n \theta>n$. Since
$$E^{2}= \begin{cases}\varepsilon^{2 v_{0}-2(1-\theta) n} & \text { if } v_{0}<n, \\ \varepsilon^{2 n \theta} \log ^{2} \frac{1}{\varepsilon} & \text { if } v_{0}=n, \\ \varepsilon^{2 n \theta} & \text { if } v_{0}>n,\end{cases}$$
the estimate (9.7) is satisfied.
If $n=2$, then we have to show instead
$$\varepsilon^{-\delta \theta} r_{\varepsilon}^{2} E^{2}=\varepsilon^{1-(1+\delta) \theta} E^{2}=O\left(\left(\beta-\beta_{*}\right) F\right)$$
and we can apply the previous case to $(1+\delta) \theta$ (in place of $\theta$ ) for $\delta \ll 1$ and $\theta$ as before so that (9.8) follows from (9.7). \(\square\)
9.3. Proof of the main theorem. We now get on to proving the main theorem. There is one last technical result needed to reach the conclusion.

Lemma 9.4. There exists $\delta_{0}>0$ such that the functional $\Psi:(\beta, \varepsilon) \mapsto\left\langle P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle$ is continuous on $\left(\beta_{*}, \beta_{*}+\delta_{0}\right) \times\left(0, \delta_{0}\right)$.

Proof. Let us choose $\sigma:=(\beta, \varepsilon)$ close enough to $\left(\beta_{*}, 0\right)$ and let $\sigma_{k} \rightarrow \sigma$ be any sequence. By Arzela-Ascoli theorem and the bound (9.5) one can extract a subsequence such that the functions $f_{\sigma_{k}}$ converge locally smoothly on $X \backslash D$ to a function $f_{\infty} \in C_{\delta}^{2, \alpha}(X)^{G}$. In particular,
$$P_{\sigma_{k}}\left(f_{\sigma_{k}}\right) \rightarrow P_{\sigma}\left(f_{\infty}\right)$$
on $X \backslash D$. Since $\left|d d^{c} f_{\sigma_{k}}\right|_{\omega_{\sigma_{k}}}$ is bounded, Lebesgue domination theorem shows that
$$\left\langle f_{\sigma_{k}}, \tau_{\sigma_{k}}\right\rangle \rightarrow\left\langle f_{\infty}, \tau_{\sigma}\right\rangle, \quad \text { and } \quad \Psi\left(f_{\sigma_{k}}\right) \rightarrow\left\langle P_{\sigma}\left(f_{\infty}\right), \tau_{\sigma}\right\rangle=: a_{\infty} .$$
Since $P_{\sigma_{k}}\left(f_{\sigma_{k}}\right)^{\perp}=0$, it follows from (9.9) that
$$P_{\sigma}\left(f_{\infty}\right)=a_{\infty} \frac{\tau_{\sigma}}{\left|\tau_{\sigma}\right|^{2}} \quad \text { and } \quad\left\langle f_{\infty}, \tau_{\sigma}\right\rangle=0 .$$
Given the uniqueness property in Proposition 9.1, we infer that $f_{\infty}=f_{\sigma}$. By the second item in (9.10), $\Psi$ is continuous at $\sigma$. \(\square\)

Proof of Main Theorem. We first prove the existence and then the convergence results.
1. We fix $\beta$ and vary $\varepsilon$ as prescribed by (8.31). Proposition 9.3 then shows that $\left\langle P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right), \tau_{\beta, \varepsilon}\right\rangle$ achieves positive (resp. negative) values whenever $\eta$ satisfies $1 \gg \eta \gg F$ (resp. $1 \gg-\eta \gg F$ ). By Lemma 9.4 above, this quantity is continuous with respect to $\eta$. Therefore, given any $\beta>0$ close enough to $\beta_{*}$, there exists $\varepsilon=\varepsilon(\beta)$ as in (8.31) such that
$$P_{\beta, \varepsilon}\left(f_{\beta, \varepsilon}\right)=0,$$
i.e. $\omega_{\beta, \varepsilon}+d d^{c} f_{\beta, \varepsilon}$ is Kähler-Einstein. Moreover, one has
$$(1-o(1)) \cdot \omega_{\beta, \varepsilon} \leqslant \omega_{\beta, \varepsilon}+d d^{c} f_{\beta, \varepsilon} \leqslant(1+o(1)) \cdot \omega_{\beta, \varepsilon}$$
by (9.6).
2. We need to identify the Gromov-Hausdorff limit of $\left(X, \omega_{\mathrm{KE}, \beta}\right)$. By (9.12) above, it is enough to show the result for the model metric $\omega_{\beta, \varepsilon}$. To lighten notation, let us write $\omega_{\mathrm{KE}, \beta}:=\omega_{\beta, \varepsilon}+d d^{c} f_{\beta, \varepsilon}$. Since the diameter of the both the gluing zone and the Tian-Yau part are a $O\left(r_{\varepsilon}\right)$, and since the diameter of $\left(\left(r \leqslant r_{\varepsilon}\right), \omega_{\beta_{*}, L}\right)$ is also a $O\left(r_{\varepsilon}\right)$, it is enough to show that
$$\sup _{r \geqslant r_{\varepsilon}}\left|\omega_{\beta, L}-\omega_{\beta_{*}, L}\right| \omega_{\beta_{*}, L} \longrightarrow 0$$
when $\varepsilon \rightarrow 0$ or, equivalently, when $\beta \rightarrow \beta_{*}$. Now the latter follows from (3.48) and the choice of $r_{\varepsilon}$ which satisfies (7.3).
3. Finally, the locally smooth convergence $\varepsilon_{\beta}^{-1} \omega_{\mathrm{KE}, \beta}$ to the Tian-Yau metric on $X \backslash D$ is an immediate consequence of (9.12). Indeed, the latter gives $C^{0}$ convergence of the tensor on each compact subset of $X \backslash D$, and the usual boot-strapping arguments allow to improve it to smooth convergence thanks to the Monge-Ampère equation (7.6)-(9.11) solved by $\varepsilon_{\beta}^{-1} \omega_{\mathrm{KE}, \beta}$. \(\square\)

\section*{10. Examples}
10.1. Projective hypersurfaces.
10.1.1. $\mathbb{P}^{n}$ and the quadric. Here, we consider $X=\mathbb{P}^{n}$ and $D=Q_{n-1}$ for $n \geqslant 2$. We have $\alpha=\frac{n+1}{2}, D$ is homogeneous hence Kähler-Einstein and the vector fields on $D$ clearly lift to $X$. Moreover, we have $j_{0}=1$ by Remark 5.4 and Example 4.4. In particular, we get
$$\varepsilon_{\beta}= \begin{cases}\left(\beta-\beta_{*}\right)^{\frac{1}{2}} & \text { if } n=2 \\ \left(\frac{\beta-\beta_{*}}{-\log \left(\beta-\beta_{*}\right)}\right)^{\frac{1}{3}} & \text { if } n=3 \\ \left(\beta-\beta_{*}\right)^{\frac{n-1}{2 n}} & \text { if } n \geqslant 4 .\end{cases}$$
10.1.2. $\mathbb{P}^{n}$ and a large degree hypersurface. We consider now the case where $X=$ $\mathbb{P}^{n}$ and $D$ is a general hypersurface of degree $n$ (resp. $n-1$ ). We may assume that $n \geqslant 3$ (resp. $n \geqslant 4$ ) so that we are not back to the case of the quadric above. We have $\alpha=\frac{n+1}{n}$ (resp. $\frac{n+1}{n-1}$ ), $D$ is Kähler-Einstein by [Tia87, Theorem 4.3] and the condition on the automorphisms is fulfilled thanks to Lemma 4.2 (ii). Actually, when $n \geqslant 3$ one has $\operatorname{Aut}^{\circ}(D)=\{1\}$ by [MM64]. Moreover, we have $j_{0}=1$ by Remark 5.4 and Example 4.4 and $\alpha<2$ hence
$$\varepsilon_{\beta}=\left(\beta-\beta_{*}\right)^{\frac{1}{n}} .$$

\subsection*{10.2. Homogeneous varieties.}
10.2.1. The quadric and a hyperplane section. Let $X=Q_{n} \subset \mathbb{P}^{n+1}$ be the smooth quadric of dimension $n$ for $n \geqslant 2$ and let $D \simeq Q_{n-1}$ be a general hyperplane section. We have $\alpha=n$ and all the assumptions of the main theorem are clearly met. The normal exact sequence is split by Example 4.7, hence $j_{0} \geqslant 2$. It would be interesting to determine the precise value of $j_{0}$, but we will not pursue this here.
10.2.2. Some grassmannians and a hyperplane section. Here, we let $X=\operatorname{Gr}(2,2 n)$ for some $n \geqslant 2$ and $D$ be a general hyperplane section under the Plücker embedding. Note that $X$ has Picard number one. Since $D$ parametrizes 2-planes in the kernel of a symplectic 2-form, $D$ is homogeneous under $\operatorname{Sp}(2 n)$ and therefore the assumptions of the theorem are met.

\section*{References}
\begin{itemize}
\item[] [ABT09] Marco Abate, Filippo Bracci, and Francesca Tovena. Embeddings of submanifolds and normal bundles. Adv. Math., 220(2):620-656, 2009.
\item[] [BBE ${ }^{+}$19] Robert J. Berman, Sebastien Boucksom, Philippe Eyssidieux, Vincent Guedj, and Ahmed Zeriahi. Kähler-Einstein metrics and the Kähler-Ricci flow on log Fano varieties. J. Reine Angew. Math., 751:27-89, 2019.
\item[] [BBJ21] Robert J. Berman, Sébastien Boucksom, and Mattias Jonsson. A variational approach to the Yau-Tian-Donaldson conjecture. J. Am. Math. Soc., 34(3):605-652, 2021.
\end{itemize}
[Ber15] Bo Berndtsson. A Brunn-Minkowski type inequality for Fano manifolds and some uniqueness theorems in Kähler geometry. Invent. Math., 200(1):149-200, 2015.
[Bes87] Arthur L. Besse. Einstein manifolds, volume 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1987. DOI:10.1007/978-3-540-74311-8.
[BG22] Olivier Biquard and Henri Guenancia. Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric. Invent. Math., 230(3):1101-1163, 2022.
[BH23] Olivier Biquard and Hans-Joachim Hein. The renormalized volume of a 4-dimensional Ricci-flat ALE space. J. Differ. Geom., 123(3):411-429, 2023.
[Biq02] Olivier Biquard. Métriques autoduales sur la boule. Invent. math., 148(3):545-607, 2002.
[Biq19] Olivier Biquard. Métriques hyperkählériennes pliées. Bull. Soc. Math. Fr., 147(2):303-340, 2019.
[Bla56] André Blanchard. Sur les variétés analytiques complexes. Ann. Sci. Éc. Norm. Supér. (3), 73:157-202, 1956.
[BM11] Olivier Biquard and Vincent Minerbe. A Kummer construction for gravitational instantons. Commun. Math. Phys., 308(3):773-794, 2011.
[Bre13] S. Brendle. Ricci flat Kähler metrics with edge singularities . International Mathematics Research Notices, 24:5727-5766, 2013.
[CDS14] Xiuxiong Chen, Simon Donaldson, and Song Sun. Kähler-Einstein metrics and stability. Int. Math. Res. Not., 2014(8):2119-2125, 2014.
[CH13] Ronan J. Conlon and Hans-Joachim Hein. Asymptotically conical Calabi-Yau manifolds, I. Duke Math. J., 162(15):2855-2902, 2013.
[CR18] Ivan A. Cheltsov and Yanir A. Rubinstein. On flops and canonical metrics. Ann. Sc. Norm. Super. Pisa, Cl. Sci. (5), 18(1):283-311, 2018.
[Del20] Thibaut Delcroix. K-stability of Fano spherical varieties. Ann. Sci. Éc. Norm. Supér. (4), 53(3):615-662, 2020.
[Del24] Thibaut Delcroix. Limits of conical Kähler-Einstein metrics on rank one horosymmetric spaces. Bull. Lond. Math. Soc., 56(7):2514-2528, 2024.
[Don12] Simon Donaldson. Kähler metrics with cone singularities along a divisor. In Essays in mathematics and its applications, pages 49-79. Springer, Heidelberg, 2012.
[DR17] Tamás Darvas and Yanir A. Rubinstein. Tian's properness conjectures and Finsler geometry of the space of Kähler metrics. J. Am. Math. Soc., 30(2):347-387, 2017.
[Fuj16] Kento Fujita. On log K-stability for asymptotically log Fano varieties. Ann. Fac. Sci. Toulouse, Math. (6), 25(5):1013-1024, 2016.
[GP16] Henri Guenancia and Mihai Păun. Conic singularities metrics with prescribed Ricci curvature: the case of general cone angles along normal crossing divisors. J. Differential Geom., 103(1):15-57, 2016.
[Gue20] Henri Guenancia. Kähler-Einstein metrics: From cones to cusps. J. Reine Angew. Math., 759:1-27, 2020.
[Has19] Yoshinori Hashimoto. Scalar curvature and Futaki invariant of Kähler metrics with cone singularities along a divisor. Ann. Inst. Fourier, 69(2):591-652, 2019.
[Jah05] Priska Jahnke. Submanifolds with splitting tangent sequence. Math. Z., 251(3):491-507, 2005.
[JMR16] Thalia Jeffres, Rafe Mazzeo, and Yanir A. Rubinstein. Kähler-Einstein metrics with edge singularities. Ann. of Math. (2), 183(1):95-176, 2016. with an Appendix by C. Li and Y. Rubinstein.
[Joy00] Dominic D. Joyce. Compact manifolds with special holonomy. Oxford Mathematical Monographs. Oxford University Press, Oxford, 2000.
[Li15] Chi Li. Numerical solutions of Kähler-Einstein metrics on $\mathbb{P}^{2}$ with conical singularities along a smooth quadric curve. J. Geom. Anal., 25(3):1773-1797, 2015.
[Li20] Chi Li. On sharp rates and analytic compactifications of asymptotically conical Kähler metrics. Duke Math. J., 169(8):1397-1483, 2020.
[Li22] Chi Li. G-uniform stability and Kähler-Einstein metrics on Fano varieties. Invent. Math., 227(2):661-744, 2022.
[LS14] Chi Li and Song Sun. Conical Kähler-Einstein metrics revisited. Comm. Math. Phys., 331(3):927-973, 2014.
[Mat57] Yozô Matsushima. Sur la structure du groupe d'homéomorphismes analytiques d'une certaine variété kaehlérienne. Nagoya Math. J., 11:145-150, 1957.
[MM64] H. Matsumura and P. Monsky. On the automorphisms of hypersurfaces. J. Math. Kyoto Univ., 3:347-361, 1964.
[Mor79] Shigefumi Mori. Projective manifolds with ample tangent bundles. Ann. Math. (2), 110:593-606, 1979.
[Oda88] Tadao Oda. Convex bodies and algebraic geometry, volume 15 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 1988. An introduction to the theory of toric varieties, Translated from the Japanese.
[RZ22] Yanir A. Rubinstein and Kewei Zhang. Angle deformation of Kähler-Einstein edge metrics on Hirzebruch surfaces. Pure Appl. Math. Q., 18(1):343-366, 2022.
[Sno86] Dennis M. Snow. Cohomology of twisted holomorphic forms on Grassmann manifolds and quadric hypersurfaces. Math. Ann., 276:159-176, 1986.
[SY80] Yum-Tong Siu and Shing-Tung Yau. Compact Kähler manifolds of positive bisectional curvature. Invent. Math., 59:189-204, 1980.
[Szé13] Gábor Székelyhidi. A remark on conical Kähler-Einstein metrics. Math. Res. Lett., 20(3):581-590, 2013.
[Tia87] Gang Tian. On Kähler-Einstein metrics on certain Kähler manifolds with $C_{1}(M)>0$. Invent. Math., 89:225-246, 1987.
[TY91] Gang Tian and Shing-Tung Yau. Complete Kähler manifolds with zero Ricci curvature. II. Invent. Math., 106(1):27-60, 1991.
[VdV59] A. Van de Ven. A property of algebraic varieties in complex projective spaces. Centre Belge Rech. Math., Colloque Géom. Différ. Globale, Bruxelles du 19 au 22 Déc. 1958, 151-152 (1959)., 1959.
[Wah83] J. M. Wahl. A cohomological characterization of $\mathbf{P}^{n}$. Invent. Math., 72(2):315-322, 1983.
Sorbonne Université, Université Paris Cité, CNRS, IMJ-PRG, F-75005 Paris, France
Email address: olivier.biquard@sorbonne-universite.fr
Institut de Mathématiques de Toulouse; UMR 5219, Université de Toulouse; CNRS, UPS, 118 route de Narbonne, F-31062 Toulouse Cedex 9, France
Email address: henri.guenancia@math.cnrs.fr