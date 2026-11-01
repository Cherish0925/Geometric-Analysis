---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1512_01662.pdf
converter: mathpix
format: mmd
---

\title{
Bianchi-IX, Darboux-Halphen and Chazy-Ramanujan
}

\author{
Sumanto Chanda ${ }^{*}$, Partha Guha ${ }^{*}$ and Raju Roychowdhury ${ }^{*}$ \\ S.N. Bose National Centre for Basic Sciences \\ JD Block, Sector III, Salt Lake, Kolkata 700098, India \\ sumanto12@boson.bose.res.in, partha@boson.bose.res.in \\ - Instituto de Fisica, Universidade de Sao Paulo, C. Postal 66318, 05314-970 Sao Paulo, SP, Brazil \\ raju@if.usp.br, raju.roychowdhury@gmail.com
}

\begin{abstract}
Bianchi-IX four metrics are $S U(2)$ invariant solutions of vacuum Einstein equation, for which the connection-wise self-dual case describes the Euler Top, while the curvature-wise self-dual case yields the Ricci flat classical Darboux-Halphen system. It is possible to see such a solution exhibiting Ricci flow. The classical Darboux-Halphen system is a special case of the generalized one that arises from a reduction of the self-dual Yang-Mills equation and the solutions to the related homogeneous quadratic differential equations provide the desired metric. A few integrable and near-integrable dynamical systems related to the Darboux-Halphen system and occurring in the study of Bianchi IX gravitational instanton have been listed as well. We explore in details whether self-duality implies integrability.
\end{abstract}

\section*{Contents}
1 Introduction ..... 1
2 Geometric analysis ..... 2
2.1 Connection wise self duality - the Lagrange system ..... 2
2.2 Curvature wise self-duality - Classical Darboux-Halphen system ..... 4
2.3 Self-dual curvature components ..... 5
2.4 Special case: The Taub-NUT ..... 7
3 The generalized Darboux-Halphen system ..... 7
3.1 Reduction of the SDYM equation ..... 7
3.2 Solutions of the generalized system ..... 8
3.3 Non-existence of a metric for the generalized system ..... 9
4 Aspects of Flow equations ..... 11
5 Other related systems ..... 12
5.1 Ramamani to Darboux-Halphen ..... 12
5.2 The Chazy equation ..... 14
5.3 The Ramanujan equation ..... 14
5.4 Generalized Chazy System ..... 15
6 Integrability of the Bianchi-IX ..... 16
7 Conclusions ..... 19
8 APPENDIX ..... 20

\section*{1 Introduction}

Historically, gravitational instantons have been explored with the same motivations similar to gauge instantons: to describe the non-perturbative transitions in quantum gravity, and by analytic continuation producing real-time gravitational backgrounds [1, 2, 3]. Dealing with (anti)-self-dual systems makes the task of solving Einsteins equations substantially easier, producing first order equations like the (anti)-self-dual Yang-Mills equations, often related to interesting integrable systems [4].

Following applications to homogeneous cosmology, $\mathcal{M}_{4}$ spaces topologically equivalent to $\mathbb{R} \times$ $\mathcal{M}_{3}$ of Bianchi type have been extensively explored. For a pedagogical introduction to various cosmological models look at the Lecture Notes by Ellis et.al.[5]. Out of all Bianchi type models of classes I - IX with vanishing cosmological constant, only Bianchi-IX has been found to exhibit a relationship with quasimodular forms [6, 7]. Modular forms in physics are a consequence of duality properties, resulting either from an invariance or a relationship between two distinct theories. In the past 30 years, modular and quasimodular forms have emerged mostly in the study of gravity and string theory [8]. Furthermore, we must note that the Bianchi-IX model is a controversial system (possessing both integrable and non-integrable aspects).

A debate followed between various authors involving doubts over statements regarding the chaotic nature of Bianchi-IX dynamics. They simultaneously expressed their opinion that the model might as well be a classical integrable system (In Liovilles sense) [9]. Thus Bianchi-IX cosmological model is a good "thought laboratory" for testing theories in order to understand various concepts of integrability.

Since the late 70s, many systems were developed starting with self-dual Yang-Mills system after reductions, leading to the belief that all integrable systems were obtained from similar such reductions [4, 10, 11]. The generalized Darboux-Halphen system is one such system, heavily studied over the recent years, although in its classical form the relationship with Bianchi-IX metric was established rather recently in the 90s. Such a connection proves to be of use in constructing various interesting Bianchi IX solutions [12] or their applications e.g. in the study of scattering of $S U(2)$ BPS monopoles [10, 13]. The Darboux-Halphen system also exhibits Ricci flow that describes the evolution of $S U(2)$-homogeneous 3D geometries and can be seen as reflection of hidden symmetrry of hyperbolic monopole motion [14].

The plan of this article is as follows: In Sect. 2 we will first perform a geometric analysis of the Bianchi-IX metric, directly exploring both connection-wise and curvature-wise self-dual cases, bringing us to the Eule-Top and classical Darboux-Halphen cases respectively, followed by computation of the general form of the curvature components. Then in the next Sect. 3 we will start with the self-dual Yang-Mills equation and by reduction see how it gives rise to the generalized Darboux-Halphen system, which has a close relation to the Euler-Top system. This will be followed by an elaboration on solutions that can be obtained for such a system. A brief note will be made as to how the classical case arises from the generalized one and also explore why we cannot always find a metric that gives rise to the generalized system. We will proceed to list solutions to the various first-order differential equations involved with the system, that effectively yield the metric corresponding to the classical system and possibly the generalized one as well. This will be followed by a derivation and examination of the Ricci flow equations in Sect.4. We will see in Sect. 5 how the Chazy equation emerges from the classical Darboux-Halphen system, a result of curvature-
wise self-duality, as well how othes like the Ramanujan and Ramamani systems are related to it. This will be followed up by a detailed analysis of integrability of the Bianchi-IX in Sect. 6 to see if self-duality implies integrability. Fianlly we conclude in Sect. 7 and try to look for future directions.

Note added: Near the completion of this work, the paper [15] appeared on the arXiv. The authors, among other things, also address the question of arithmetics and integrability of Bianchi IX gravitational instantons, which have been explored by imposing the self-duality condition on triaxial Bianchi IX metrics and by employing a time-dependent conformal factor. We comment more about this in the final section at the end of the paper.

\section*{2 Geometric analysis}

The Bianchi-IX metric is a general setup for 4D Euclidean spherically symmetric metrics. Under certain settings of its curvature-wise anti-self-dual case, becomes the Taub-NUT. Naturally, the analysis of its connection and curvature follows the same way as in [16, 17].

The metric is written as:
$$d s^{2}=\left[c_{1}(r) c_{2}(r) c_{3}(r)\right]^{2} d r^{2}+c_{1}^{2}(r) \sigma_{1}^{2}+c_{2}^{2}(r) \sigma_{2}^{2}+c_{3}^{2}(r) \sigma_{3}^{2}$$
where the variables $\sigma_{i}$ obey the structure equation:
$$d \sigma^{i}=-\varepsilon_{j k}^{i} \sigma^{j} \wedge \sigma^{k} \quad \text { where } \quad \sigma^{i}=-\frac{1}{r^{2}} \eta_{\mu \nu}^{i} x^{\mu} d x^{\nu}$$
and $i, j, k$ are permutations of the indices $1,2,3$.
Those solutions that are (anti-) self-dual fall into 2 categories:
\begin{itemize}
\item[1.] connection wise self-dual
\item[2.] curvature wise self-dual
\end{itemize}
we shall now uncover the systems characterising each category respectively.

\subsection*{2.1 Connection wise self duality - the Lagrange system}

First we shall compute the spin connections in the same manner as for the Taub-NUT [17]. We can describe the tetrads as:
$$\begin{aligned}
e^{0}=c_{0}(r) d r & e^{i} & =c_{i}(r) \sigma^{i}, \quad i=1,2,3 \\
\text { where } & c_{0}(r) & =c_{1}(r) c_{2}(r) c_{3}(r)
\end{aligned}$$

Obviously, $e^{0}$ produces no connections $\left(d e^{0}=0\right)$. However, for the remaining three:
$$d e^{i}=-\frac{\partial_{r} c_{i}}{c_{0}} \sigma^{i} \wedge e^{0}-\left\{-\varepsilon^{i}{ }_{j k} \frac{c_{i}^{2}+c_{j}^{2}-c_{k}^{2}}{2 c_{i} c_{j}} \sigma^{k} \wedge e^{j}-\varepsilon^{i}{ }_{k j} \frac{c_{i}^{2}+c_{k}^{2}-c_{j}^{2}}{2 c_{i} c_{k}} \sigma^{j} \wedge e^{k}\right\}$$

Under torsion-free condition the 1st Cartan structure equation $\left(d e^{i}=-\omega^{i}{ }_{j} \wedge e^{j}\right)$ gives us the following spin connections:
$$\omega_{0}^{i}=\frac{\partial_{r} c_{i}}{c_{0}} \sigma^{i} \quad \quad \omega_{j}^{i}=-\varepsilon_{j k}^{i} \frac{c_{i}^{2}+c_{j}^{2}-c_{k}^{2}}{2 c_{i} c_{j}} \sigma^{k}$$

This elaborate form for the components of the spin connections make its anti-symmetric nature evident. If we only consider those cases of (anti-) self-duality, we will have
$$\begin{gathered}
\omega_{0 i}= \pm \frac{1}{2} \varepsilon_{0 i}{ }^{j k} \omega_{j k}= \pm \omega_{j k} \quad \Rightarrow \quad 2 \frac{\partial_{r} c_{i}}{c_{i}}=\mp \varepsilon_{j k i}\left(c_{j}^{2}+c_{k}^{2}-c_{i}^{2}\right) \\
\therefore \quad \partial_{r}\left(\ln c_{i}^{2}\right)=\mp \varepsilon_{j k i}\left(c_{j}^{2}+c_{k}^{2}-c_{i}^{2}\right)
\end{gathered}$$

One may suppose that we must parametrize the LHS to match the linear form of the RHS in the equation above. Essentially, the derivative operator aside, $c_{i}^{2}$ must be parametrized such that
$$\begin{aligned}
& \ln c_{i}^{2}=\ln \Omega_{j}+\ln \Omega_{k}-\ln \Omega_{i}=\ln \left(\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}\right) \\
& \therefore \quad\left(c_{i}\right)^{2}=\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}} \quad \Rightarrow \quad \Omega_{i}=c_{j} c_{k}
\end{aligned}$$
which enable us to decouple the individual parameters into their own equations turning into simpler expressions. This allows us to continue our analysis from (2.1.4) as
$$\partial_{r}\left[\ln \left(\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}\right)\right]=\frac{\dot{\Omega}_{j}}{\Omega_{j}}+\frac{\dot{\Omega}_{k}}{\Omega_{k}}-\frac{\dot{\Omega}_{i}}{\Omega_{i}}=\mp \varepsilon_{j k i}\left(\frac{\Omega_{k} \Omega_{i}}{\Omega_{j}}+\frac{\Omega_{i} \Omega_{j}}{\Omega_{k}}-\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}\right)$$

Adding up with a similar expression for $2 \partial_{r}\left(\ln c_{j}\right)=\mp \varepsilon_{k i j}\left(c_{i}^{2}+c_{k}^{2}-c_{j}^{2}\right)$, we get
$$\frac{\dot{\Omega}_{i}}{\Omega_{i}}+\frac{\dot{\Omega}_{k}}{\Omega_{k}}-\frac{\dot{\Omega}_{j}}{\Omega_{j}}=\mp \varepsilon_{k i j}\left(\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}+\frac{\Omega_{i} \Omega_{j}}{\Omega_{k}}-\frac{\Omega_{k} \Omega_{i}}{\Omega_{j}}\right)$$
we will find that self-dual cases of the Bianchi-IX (keeping in mind that $\varepsilon_{j k i}=\varepsilon_{i j k}=\varepsilon_{k i j}=1$ ) metric gives us the Lagrange (Euler-top) system
$$\begin{aligned}
& \frac{\dot{\Omega}_{j}}{\Omega_{j}}+\frac{\dot{\Omega}_{k}}{\Omega_{k}}-\frac{\dot{\Omega}_{i}}{\Omega_{i}}= \mp \varepsilon_{j k i}\left(\frac{\Omega_{k} \Omega_{i}}{\Omega_{j}}+\frac{\Omega_{i} \Omega_{j}}{\Omega_{k}}-\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}\right) \\
&+ \\
& \frac{\dot{\Omega}_{i}}{\Omega_{i}}+\frac{\dot{\Omega}_{k}}{\Omega_{k}}-\frac{\dot{\Omega}_{j}}{\Omega_{j}}= \mp \varepsilon_{k i j}\left(\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}+\frac{\Omega_{i} \Omega_{j}}{\Omega_{k}}-\frac{\Omega_{k} \Omega_{i}}{\Omega_{j}}\right) \\
& \downarrow \\
& \therefore \quad 2 \frac{\dot{\Omega}_{k}}{\Omega_{k}}=\mp 2 \frac{\Omega_{i} \Omega_{j}}{\Omega_{k}} \quad \Rightarrow \quad \dot{\Omega}_{k}=\mp \Omega_{i} \Omega_{j}
\end{aligned}$$
where throughout derivative (denoted by dot) is taken with respect to $r$.

\subsection*{2.2 Curvature wise self-duality - Classical Darboux-Halphen system}

Since we have already covered connection-wise self duality, let us explore a stronger version known as curvature-wise self-duality. This emphasizes and expands upon the property of self-duality, generalizing it beyond connection 1-forms. This means that curvature-wise self-duality does not invalidate, rather implies connection-wise self-duality [18], and hence part of the dynamical system derived from this should have the same form as the Lagrange system.

The Cartan-structure equation for Riemann curvature is
$$R_{i j}=d \omega_{i j}+\omega_{i m} \wedge \omega_{j}^{m}$$

The self-duality of curvature demands that
$$R_{0 i}=\frac{1}{2} \varepsilon_{0 i}^{j k} R_{j k}=R_{j k}$$

Now, for the LHS and RHS of (2.2.2), we have
$$\text { LHS } \quad R_{0 i}=d \omega_{0 i}+\omega_{0 j} \wedge \omega_{i}^{j}+\omega_{0 k} \wedge \omega_{i}^{k}$$
$$\text { RHS } \quad \begin{aligned}
R_{j k} & =d \omega_{j k}+\omega_{j 0} \wedge \omega^{0}{ }_{k}+\omega_{j i} \wedge \omega^{i}{ }_{k} \\
& =d \omega_{j k}-\omega_{0 j} \wedge \omega^{0}{ }_{k}-\omega_{j i} \wedge \omega_{k i}
\end{aligned}$$

Now, for (anti-) self-duality of the connection forms, as employed in the previous section, we shall be able to eliminate some of the later terms of (2.2.3) and (2.2.4), since
$$\omega_{i j}= \pm \frac{1}{2} \varepsilon_{i j}{ }^{k 0} \omega_{k 0}=\mp \omega_{k 0} \quad \Rightarrow \quad \omega_{j i} \pm \omega_{0 k}=0$$

This leaves us with the equation shown below and its solution that follows, adapted from the previous subsection.
$$d \omega_{0 i}= \pm d \omega_{j k}$$
$$\begin{aligned}
& \Rightarrow \quad \partial_{r}\left(\frac{\partial_{r} c_{i}}{c_{0}}\right) d r \wedge \sigma^{i}+\frac{\partial_{r} c_{i}}{c_{0}} d \sigma^{i}=\mp \partial_{r}\left(\frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}}\right) d r \wedge \sigma^{i} \mp \frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}} d \sigma^{i} \\
& \Rightarrow \quad \partial_{r}\left(\frac{\partial_{r} c_{i}}{c_{0}}\right)=\mp \partial_{r}\left(\frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}}\right) \quad \Rightarrow \quad \frac{\partial_{r} c_{i}}{c_{0}}=\mp \varepsilon_{j k i} \frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}}+\lambda_{j k}
\end{aligned}$$
$$\Rightarrow \quad 2 \partial_{r}\left(\ln c_{i}\right)=\mp\left(c_{j}^{2}+c_{k}^{2}-c_{i}^{2}\right)+2 \lambda_{j k} c_{j} c_{k}$$

Thus, as before, upon parametrization we shall have
$$\frac{\dot{\Omega}_{j}}{\Omega_{j}}+\frac{\dot{\Omega}_{k}}{\Omega_{k}}-\frac{\dot{\Omega}_{i}}{\Omega_{i}}=\mp\left(\frac{\Omega_{k} \Omega_{i}}{\Omega_{j}}+\frac{\Omega_{i} \Omega_{j}}{\Omega_{k}}-\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}\right)+2 \lambda_{j k} \Omega_{i}$$
$$\frac{\dot{\Omega}_{i}}{\Omega_{i}}+\frac{\dot{\Omega}_{k}}{\Omega_{k}}-\frac{\dot{\Omega}_{j}}{\Omega_{j}}=\mp\left(\frac{\Omega_{j} \Omega_{k}}{\Omega_{i}}+\frac{\Omega_{i} \Omega_{j}}{\Omega_{k}}-\frac{\Omega_{k} \Omega_{i}}{\Omega_{j}}\right)+2 \lambda_{i k} \Omega_{j}$$

Adding up these two results, just like before, will now give us
$$\dot{\Omega}_{k}=\mp \Omega_{i} \Omega_{j}+\lambda_{j k} \Omega_{k} \Omega_{i}+\lambda_{i k} \Omega_{k} \Omega_{j}$$
where setting $\lambda_{i j}=-1 \quad \forall i, j$ in (2.2.9) for anti-self-duality proceeds to give us the classical Darboux-Halphen system
$$\therefore \quad \dot{\Omega}_{k}=\Omega_{i} \Omega_{j}-\Omega_{k}\left(\Omega_{i}+\Omega_{j}\right)$$

Thus, we can see that the curvature-wise self-duality extends upon the characteristic system of the connection-wise self-duality, making the Darboux-Halphen system a suitable candidate for further development beyond the Lagrange system. Clearly, the first term has included the dynamical aspect of the Lagrange system, as the property of self-duality of the connection 1-forms being preserved, aside from an additive constant involved and was extended to their exterior derivatives. Needless to say, connection-wise self-duality must precede curvature-wise self-duality, and the latter is not possible without ensuring the former.

\subsection*{2.3 Self-dual curvature components}

So far, we have managed to study a great deal about the Bianchi-IX geometry, without confronting the work of extracting the curvature components. Now, in this subsection, we will proceed to do exactly that, using the imposed (anti-) self duality properties at our disposal to make our job easier. But first, we shall prove and later in this case confirm that all curvature-wise self-dual manifolds are Ricci-flat.

We recall from [16] that the Riemann curvature tensor for (anti-)self-dual metrics on the vierbein space can be written as:
$$R_{a b c d}=\mathcal{G}_{i j}(\vec{x}) \eta_{a b}^{( \pm) i} \eta_{c d}^{( \pm) j} \quad i, j=1,2,3 ; \quad a, b, c, d=0,1,2,3$$

This means the Ricci tensor for Euclidean vierbein space is given by
$$\mathbb{R}_{a c}=\delta^{b d} R_{a b c d}=\delta^{b d} \mathcal{G}_{i j}(\vec{x}) \eta_{a b}^{i} \eta_{c d}^{j}=\mathcal{G}_{i j}(\vec{x}) \delta^{i j} \delta_{a c}=(\operatorname{Tr}[\mathcal{G}(\vec{x})]) \delta_{a c}$$

Clearly, the above result implies that the Ricci tensor has only diagonal elements, which allows us to demonstrate that
$$\begin{gathered}
\mathbb{R}_{a a}=R_{a b a b}+R_{a c a c}+R_{a d a d} \xrightarrow{\text { self-duality }} \pm\left(R_{a b c d}+R_{a c d b}+R_{a d b c}\right) \xrightarrow{\text { Bianchi identity }} 0 \\
\therefore \quad \mathbb{R}_{a a}=0 \quad \Rightarrow \quad \operatorname{Tr}[\mathcal{G}(\vec{x})]=0
\end{gathered}$$

Showing that curvature-wise self-dual manifolds are undoubtedly Ricci-flat.
Self-duality ⟹ Ricci-flatness

Returning to the original co-ordinates, we have:
$$\mathbb{R}_{a c}=\left(\mathcal{G}_{i j}(\vec{x}) \delta^{i j}\right)\left(\delta_{a c} e_{\mu}^{a} e_{\nu}^{c}\right)=\operatorname{Tr}[\mathcal{G}(\vec{x})] g_{\mu \nu}(\vec{x})$$

But, for a more thorough analysis, it would be better to directly obtain all the curvature components for detailed examination. This can be easily done as we already have the general formula for all the connection components. The results are made easier by keeping the self-duality of the connection forms (2.2.5) in mind.
$$\begin{aligned}
& R_{0 i}=d \omega_{0 i}+\omega_{0 j} \wedge \omega_{j i}+\omega_{0 k} \wedge \omega_{k i} \\
& =d \omega_{0 i}+\omega_{0 j} \wedge \omega_{0 k}-\omega_{0 k} \wedge \omega_{0 j}=d \omega_{0 i}+2 \omega_{0 j} \wedge \omega_{0 k} \\
\therefore \quad & R_{0 i}=\underbrace{\frac{1}{c_{0} c_{i}}\left(\frac{c_{i}^{\prime}}{c_{0}}\right)^{\prime}}_{R_{0 i 0 i}} e^{0} \wedge e^{i}-\underbrace{\frac{1}{c_{j} c_{k}}\left[\frac{c_{i}^{\prime}}{c_{0}}-2 \frac{\left(c_{j}^{\prime}\right)\left(c_{k}^{\prime}\right)}{c_{0}^{2}}\right]}_{-R_{0 i j k}} e^{j} \wedge e^{k}
\end{aligned}$$

Now curvature wise anti-self-duality means
$$R_{0 i 0 i}=-R_{0 i j k}=-R_{j k 0 i}=R_{j k j k}$$

Demanding curvature wise anti-self-duality gives us the differential equation
$$\frac{1}{c_{0} c_{i}}\left(\frac{c_{i}^{\prime}}{c_{0}}\right)^{\prime}=\frac{1}{c_{j} c_{k}}\left[\frac{c_{i}^{\prime}}{c_{0}}-2 \frac{\left(c_{j}^{\prime}\right)\left(c_{k}^{\prime}\right)}{c_{0}^{2}}\right]$$

Since we have connection wise anti-self-duality rule (2.1.4), we can say
$$\begin{aligned}
& R_{0 i}=\frac{\varepsilon_{i j k}}{c_{0} c_{i}}\left(\frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}}\right)^{\prime} e^{0} \wedge e^{i}-\frac{\varepsilon_{i j k}}{c_{j} c_{k}}\left[\frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}}-2\left(\frac{c_{k}^{2}+c_{i}^{2}-c_{j}^{2}}{2 c_{k} c_{i}}\right)\left(\frac{c_{i}^{2}+c_{j}^{2}-c_{k}^{2}}{2 c_{i} c_{j}}\right)\right] e^{j} \wedge e^{k} \\
& \quad \therefore \quad R_{0 i}=\underbrace{\frac{\varepsilon_{i j k}}{c_{0} c_{i}}\left(\frac{c_{j}^{2}+c_{k}^{2}-c_{i}^{2}}{2 c_{j} c_{k}}\right)^{\prime}}_{R_{0 i 0 i}} e^{0} \wedge e^{i}-\underbrace{\varepsilon_{i j k} \frac{c_{i}^{2}\left(c_{j}^{2}+c_{k}^{2}-c_{i}^{2}\right)-c_{i}^{4}+\left(c_{j}^{2}-c_{k}^{2}\right)^{2}}{2 c_{0}^{2}}}_{-R_{0 i j k}} e^{j} \wedge e^{k}
\end{aligned}$$

Due to curvature wise anti-self-duality being considered, we should have:
$$R_{0 i 0 i}=-R_{0 i j k}=\varepsilon_{i j k} \frac{\left(c_{i}^{2}+c_{j}^{2}+c_{k}^{2}\right)\left(c_{j}^{2}+c_{k}^{2}\right)-2 c_{i}^{4}-4 c_{j}^{2} c_{k}^{2}}{2 c_{0}^{2}}$$
Thus, we can say that the curvature 2-form is given by
$$R_{a b}=\sum_{i=1}^{3} \varepsilon_{i j k} \frac{\left(c_{i}^{2}+c_{j}^{2}+c_{k}^{2}\right)\left(c_{j}^{2}+c_{k}^{2}\right)-2 c_{i}^{4}-4 c_{j}^{2} c_{k}^{2}}{2 c_{0}^{2}} \bar{\eta}_{a b}^{i} \bar{\eta}_{c d}^{i} e^{c} \wedge e^{d}$$
which on comparison with (2.3.1) tells us that
$$\begin{aligned}
& \mathcal{G}_{i l}(\vec{x})=\varepsilon_{i j k} \frac{\left(c_{i}^{2}+c_{j}^{2}+c_{k}^{2}\right)\left(c_{j}^{2}+c_{k}^{2}\right)-2 c_{i}^{4}-4 c_{j}^{2} c_{k}^{2}}{2 c_{0}^{2}} \delta_{i l} \\
& \operatorname{Tr}[\mathcal{G}]=\frac{2\left(c_{i}^{2}+c_{j}^{2}+c_{k}^{2}\right)^{2}-2\left(c_{i}^{2}+c_{j}^{2}+c_{k}^{2}\right)^{2}}{2 c_{0}^{2}}=0
\end{aligned}$$
Thus, the Ricci tensor, and consequently scalar on vierbein space is given by
$$\mathbb{R}_{a b}=0, \quad \mathbb{R}=0$$
confirming what was already proven previously.

\subsection*{2.4 Special case: The Taub-NUT}

The Taub-NUT is a special case of the Bianchi-IX metric connected to the classical Darboux-Halphen system. It is an exact solution of Einstein's equations, found by Abraham Huskel Taub (1951) and extended to a larger manifold by E. Newman, T. Unti and L. Tamburino (1963), whose names are included in the name of the metric Taub-NUT. It exhibits anti-self-duality as can be seen from its curvature and SU (2) gauge fields. Recently, we have conducted a detailed study of the Taub-NUT [17] where we have explored its self-duality, geometric properties, conserved quantities and Killing tensors.

The condition to set to obtain this metric is $\Omega_{1}=\Omega_{2}=\Omega \neq \Omega_{3}$. This consequently makes $c_{1}^{2}=c_{2}^{2}=c^{2}=\Omega_{3}$ and converts the Bianchi-IX metric into the following form:
$$d s^{2}=\Omega^{2} \Omega_{3} d r^{2}+\Omega_{3}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{\Omega^{2}}{\Omega_{3}} \sigma_{3}^{2}$$

Naturally, we would have to define the parameters and rescale the radial co-ordinate:
$$d r=\frac{1}{2 m} \frac{d \tilde{r}}{\Omega^{2}} \quad \Rightarrow \quad d s^{2}=\frac{\Omega_{3}}{\Omega^{2}} \frac{d \tilde{r}^{2}}{4 m^{2}}+\Omega_{3}\left(\sigma_{1}^{2}+\sigma_{2}^{2}\right)+\frac{\Omega^{2}}{\Omega_{3}} \sigma_{3}^{2}$$

Finally, we can define the parameters as
$$\Omega=\frac{\tilde{r}-m}{2 m} \quad \Omega_{3}=\frac{\tilde{r}^{2}-m^{2}}{4 m^{2}}$$
which means that the rescaling equation is
$$d r=\frac{2 m}{(\tilde{r}-m)^{2}} d \tilde{r} \quad \Rightarrow \quad r=k-\frac{2 m}{\tilde{r}-m}$$

This finally leads to Taub-NUT metric up to a rescaling conformal factor,
$$d s^{2}=\frac{\tilde{r}+m}{\tilde{r}-m} d \tilde{r}^{2}+4 m^{2} \frac{\tilde{r}-m}{\tilde{r}+m}(d \psi+\cos \theta d \phi)^{2}+\left(\tilde{r}^{2}-m^{2}\right)\left(d \theta^{2}+\sin ^{2} \theta d \phi^{2}\right)$$

\section*{3 The generalized Darboux-Halphen system}

So far, we have dealt with the classical Darboux-Halphen system that arises as the connection-wise self-dual case of the Bianchi-IX metric. Now we shall proceed to derive a generalized version of this system starting from a different configuration as described in [4, 19].

\subsection*{3.1 Reduction of the SDYM equation}

While the classical Darboux-Halphen system is an artifact of connection-wise self-duality of Bianchi-IX, this time we shall start by considering self-dual Yang-Mills equation and execute a reduction process on it.
$$F_{a b}=-\frac{1}{2} \varepsilon_{a b}{ }^{c d} F_{c d} \quad F_{a b}=\partial_{a} A_{b}-\partial_{b} A_{a}-\left[A_{a}, A_{b}\right]$$

If we set $A_{0}=0$ and all $A_{i}=A_{i}(t)$ only, then (3.1.1) becomes the Nahm equation [20, 21, 22]
$$F_{0 i}=\dot{A}_{i} \quad F_{i j}=-\left[A_{i}, A_{j}\right] \quad \Rightarrow \quad \dot{A}_{i}=\frac{1}{2} \varepsilon_{i}^{j k}\left[A_{j}, A_{k}\right]$$

Now, the $A_{i} \mathrm{~s}$ are functions from $\mathbb{R}^{4}$ to a Lie algebra $\mathfrak{g}$ given by
$$A_{i}=-M_{i j}(t) O_{j k} X_{k}$$
where $O_{i j}$ is an SO(3) matrix, and $X_{i}$ are the generators of $\mathfrak{s} \mathfrak{d i f f}\left(S^{3}\right)$ satisfying the relation $\left[X_{i}, X_{j}\right]=\varepsilon_{i j k} X_{k}$. The matrix $M_{i j}$ is given as a sum of symmetric components $M_{s}$ and antisymmetric components $M_{a}$
$$M=M_{s}+M_{a}=P(d+a) P^{-1} \quad \quad M_{a}=\varepsilon_{i j}{ }^{k} \tau_{k}$$
where
$$M_{s}=\left(\begin{array}{ccc}
\Omega_{1} & 0 & 0 \\
0 & \Omega_{2} & 0 \\
0 & 0 & \Omega_{3}
\end{array}\right) \quad M_{a}=\left(\begin{array}{ccc}
0 & \tau_{3} & -\tau_{2} \\
-\tau_{3} & 0 & \tau_{1} \\
\tau_{2} & -\tau_{1} & 0
\end{array}\right)$$

The equation we get on applying (3.1.3) and (3.1.4) to (3.1.2) is:
$$\dot{M}=(\operatorname{Adj}(M))^{T}+M^{T} M-\operatorname{Tr}(M) \cdot M$$
and taking the diagonal parts gives us the generalized Darboux-Halphen system equations.
$$\dot{\Omega}_{i}=\Omega_{j} \Omega_{k}-\Omega_{i}\left(\Omega_{j}+\Omega_{k}\right)+\tau^{2} \quad \tau^{2}=\tau_{1}^{2}+\tau_{2}^{2}+\tau_{3}^{2}$$

The off-diagonal terms taken together give us
$$\dot{\tau}_{i}=-\tau_{i}\left(\Omega_{j}+\Omega_{k}\right) \quad \tau_{i}^{2}=\alpha_{i}^{2}\left(\Omega_{j}-\Omega_{i}\right)\left(\Omega_{i}-\Omega_{k}\right)$$

Now we shall consider equations that will hold for both, classical and generalized systems and their general solutions.

\subsection*{3.2 Solutions of the generalized system}

While the generalized system has different set of equations from the classical version due to the common extra term $\tau^{2}$, if we choose to designate the variable as
$$x_{i}=\Omega_{j}-\Omega_{k}$$
we should obtain equations similar to [19]. Then, using the generalized Darboux-Halphen equations, we can write
$$\begin{aligned}
\dot{x}_{i} & =\dot{\Omega}_{j}-\dot{\Omega}_{k}=-2 \Omega_{i} x_{i} \quad \Rightarrow \quad \Omega_{i}=-\frac{1}{2}\left[\ln x_{i}\right]^{\prime} \\
& \Rightarrow \quad\left[\ln \left(\frac{x_{j}}{x_{i}}\right)\right]^{\prime}=\left[\ln \left(-\frac{x_{j}}{x_{i}}\right)\right]^{\prime}=2 x_{k}
\end{aligned}$$

This equation applies to both, generalized and classical Darboux-Halphen systems. If we choose to define a variable $s$ as:
$$s=-\frac{x_{2}}{x_{1}} \quad \Rightarrow \quad s-1=-\frac{x_{2}+x_{1}}{x_{1}}=\frac{\Omega_{1}-\Omega_{2}}{\Omega_{2}-\Omega_{3}}=\frac{x_{3}}{x_{1}}$$
then using (3.2.2) and (3.2.3), we should find as in [23, 24] that
$$\begin{gathered}
\frac{\dot{s}}{s(s-1)}=2 x_{1} \quad \frac{\dot{s}}{s-1}=-2 x_{2} \quad \frac{\dot{s}}{s}=2 x_{3} \\
\Omega_{1}=-\frac{1}{2}\left[\ln \left(\frac{\dot{s}}{s(s-1)}\right)\right]^{\prime} \quad \Omega_{2}=-\frac{1}{2}\left[\ln \left(\frac{\dot{s}}{s-1}\right)\right]^{\prime} \quad \Omega_{3}=-\frac{1}{2}\left[\ln \left(\frac{\dot{s}}{s}\right)\right]^{\prime}
\end{gathered}$$

Now the off-diagonal anti-symmetric terms, recalling (3.1.8), give rise to equations:
$$\frac{\dot{\tau}_{1}}{\tau_{1}}=\frac{1}{2}\left[\ln \left(\frac{\dot{s}^{2}}{s(s-1)}\right)\right]^{\prime} \quad \frac{\dot{\tau}_{2}}{\tau_{2}}=\frac{1}{2}\left[\ln \left(\frac{\dot{s}^{2}}{s^{2}(s-1)}\right)\right]^{\prime} \quad \frac{\dot{\tau}_{3}}{\tau_{3}}=\frac{1}{2}\left[\ln \left(\frac{\dot{s}^{2}}{s(s-1)^{2}}\right)\right]^{\prime}$$
with the following solutions:
$$\tau_{1}=\kappa_{1} \frac{\dot{s}}{\sqrt{s(s-1)}} \quad \tau_{2}=\kappa_{2} \frac{\dot{s}}{s \sqrt{(s-1)}} \quad \tau_{3}=\kappa_{3} \frac{\dot{s}}{\sqrt{s}(s-1)}$$
where $s$ satisfies the Schwarzian equation given by
$$\{s, t\}+\frac{\dot{s}^{2}}{2} V(s)=0$$
where
$$\{s, t\}:=\frac{d}{d t}\left(\frac{\ddot{s}}{\dot{s}}\right)-\frac{1}{2}\left(\frac{\ddot{s}}{\dot{s}}\right)^{2} \quad V(s)=\frac{1-4 \kappa_{2}^{4}}{s^{2}}+\frac{1-4 \kappa_{3}^{4}}{(s-1)^{2}}+\frac{\kappa_{2}^{4}+\kappa_{3}^{4}-\kappa_{1}^{4}-1}{s(s-1)}$$

Thus, if we concentrate only on the diagonal terms, we are able to express the metric related to the classical Darboux-Halphen system.

\subsection*{3.3 Non-existence of a metric for the generalized system}

Naturally, one can suspect that the classical Darboux-Halphen system and consequently the Bianchi-IX metric is the result of setting $\tau_{i}=0$. For the classical system, we should have the metric co-efficients given by the diagonal matrix
$$h_{\text {class }}=\left(\begin{array}{cccc}
\Omega_{1} \Omega_{2} \Omega_{3} & 0 & 0 & 0 \\
0 & \frac{\Omega_{2} \Omega_{3}}{\Omega_{1}} & 0 & 0 \\
0 & 0 & \frac{\Omega_{3} \Omega_{1}}{\Omega_{2}} & 0 \\
0 & 0 & 0 & \frac{\Omega_{1} \Omega_{2}}{\Omega_{3}}
\end{array}\right)$$

Now, we notice that the matrix describing the metric $h$ can be given by
$$h_{\text {class }}=M_{\text {class }}^{-1} \operatorname{Adj}\left(M_{\text {class }}\right) \quad \text { where } \quad M_{\text {class }}=\left(\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & \Omega_{1} & 0 & 0 \\
0 & 0 & \Omega_{2} & 0 \\
0 & 0 & 0 & \Omega_{3}
\end{array}\right)$$
where $M_{\text {class }}$ is the matrix that produces the classical Darboux-Halphen system. With this in mind, we see that the generalized Darboux-Halphen system (3.1.7) seems to arise from a matrix $M_{\text {gen }}$ given as
$$M_{g e n}=\left(\begin{array}{cccc}
1 & 0 & 0 & 0 \\
0 & \Omega_{1} & \tau_{3} & -\tau_{2} \\
0 & -\tau_{3} & \Omega_{2} & \tau_{1} \\
0 & \tau_{2} & -\tau_{1} & \Omega_{3}
\end{array}\right)$$

However, there are not always a vierbeins or metric counterparts for gauge fields, as there are for curvature and connection components. This shall be elaborated further as follows.

The torsion-free form of the 1st Cartan structure equation is
$$d e^{i}=-\omega^{i}{ }_{j} \wedge e^{j}$$

Further examination reveals that
$$\begin{gathered}
\partial_{\mu} e^{i}{ }_{\nu} d x^{\mu} \wedge d x^{\nu}=-\omega_{\mu j}^{i} e^{j}{ }_{\nu} d x^{\mu} \wedge d x^{\nu} \\
\therefore \quad E_{j}{ }^{\nu} \partial_{\mu} e^{i}{ }_{\nu}=-\omega_{\mu j}^{i}
\end{gathered}$$

Recalling that the spin connections can be expanded as shown below, we can say that
$$\begin{aligned}
& \omega_{i j}=\eta_{i j}^{(+) a} A^{(+) a}+\eta_{i j}^{(-) a} A^{(-) a} \quad A^{( \pm) a}=A_{\mu}^{( \pm) a} d x^{\mu} \\
& \therefore \quad E_{j}{ }^{\nu} \partial_{\mu} e_{\nu}^{i}=-\left[\eta_{i j}^{(+) a} A_{\mu}^{(+) a}+\eta_{i j}^{(-) a} A_{\mu}^{(-) a}\right]
\end{aligned}$$

Now, we can obtain the individual $\mathrm{SU}(2)_{ \pm}$gauge potential function components $A_{\mu}^{( \pm)}$in terms of the vierbein components as follows
$$A_{\mu}^{( \pm) a}=-\frac{1}{4} \eta^{( \pm) a} E_{j}{ }^{\nu} \partial_{\mu} e^{i}{ }_{\nu}$$

Thus, if we start with a metric or equivalently the vierbeins, we should be able to get the spin-connections and hence gauge fields, and from there go backwards, however, the opposite is not always possible.

Since the generalized Darboux-Halphen system is primarily a product of the reduction of the SDYM gauge fields, it may not always be possible to find a metric or its vierbeins that are related to it. The classical Darboux-Halphen system is a special case where $\tau_{i}=0 \forall i$, for which we have the self-dual Bianchi-IX metric (gravitational instanton).

\section*{4 Aspects of Flow equations}

Geometric flows describe the evolution of a metric on a Riemannian manifold along the path parameter, under a general non-linear equation, given a symmetric tensor $S_{i j}$ [25, 26]. Usually, a system that exhibits geometric flows satisfies the equation
$$\frac{d g_{i j}}{d \tau}=S_{i j}$$
where $S_{i j}$ is symmetric. Some systems exhibit a particular category of such flows known as Ricci flow for which $S_{i j}=-R_{i j}$. Such systems that describe Ricci flows do not preserve volume elements, which are described by the equation:
$$\frac{d g_{i j}}{d \tau}=-R_{i j}$$

The Ricci flow equation introduced by Richard Hamilton in 1982 was a primary tool in Grigory Perelman's proof of Thurston's geometrization conjecture, Poincare conjecture being a special case of that. Ricci flow exhibits many similarities with the heat equation: it gives manifolds more uniform geometry and smooths out irregularities and has proven to be a very useful tool in understanding the topology of arbitrary Riemannian manifolds.

Now, we have already shown that Darboux-Halphen systems are Ricci-flat which means that it is a fixed point of the Ricci flow, usually exhibited by gravitational instantons which are extremal points of the Euclidean Einstein-Hilbert action [27]. Looking at the Darboux-Halphen equations, we can see that for the Bianchi-IX metric
$$\begin{aligned}
& \frac{d\left(c_{i}^{2}\right)}{d \tau}=c_{i}^{2}\left(c_{j}^{2}+c_{k}^{2}-c_{i}^{2}-2 c_{j} c_{k}\right)=c_{i}^{2}\left[\left(c_{j}-c_{k}\right)^{2}-c_{i}^{2}\right] \\
& \frac{d\left(c_{0}^{2}\right)}{d \tau}=\frac{d}{d \tau}\left(c_{1} c_{2} c_{3}\right)^{2}=c_{0}^{2}\left\{c_{i}^{2}+c_{j}^{2}+c_{k}^{2}-2\left(c_{i} c_{j}+c_{j} c_{k}+c_{k} c_{i}\right)\right\}
\end{aligned}$$

Thus, we have the following equations:
$$\begin{aligned}
\frac{d\left(c_{0}^{2}\right)}{d \tau} & =c_{0}^{2}(\vec{x})\left[c_{i}^{2}+c_{j}^{2}+c_{k}^{2}-2\left(c_{i} c_{j}+c_{j} c_{k}+c_{k} c_{i}\right)\right] \\
\frac{d\left(c_{i}^{2}\right)}{d \tau} & =c_{i}^{2}(\vec{x})\left[\left(c_{j}-c_{k}\right)^{2}-c_{i}^{2}\right]
\end{aligned}$$

Now if we set $c_{0}=1$ for the co-ordinate rescaling $d t=c_{0}(\vec{x}) d r$, then we should get
$$\begin{gathered}
c_{i}^{2}+c_{j}^{2}+c_{k}^{2}=2\left(c_{i} c_{j}+c_{j} c_{k}+c_{k} c_{i}\right) \\
2 \frac{d c_{i}}{d \tau}=\frac{1}{c_{j} c_{k}}\left[\left(c_{j}-c_{k}\right)^{2}-c_{i}^{2}\right]
\end{gathered}$$
which matches and re-confirms the results obtained in [26] where the Ricci tensor for such Bianchi-IX geometry is given by the RHS of the above equation, showing that it does exhibit Ricci flow. For a more general Darboux-Halphen system, the result would be of the form:
$$\frac{d\left(c_{i}^{2}\right)}{d \tau}=c_{i}^{2}\left[c_{j}^{2}+c_{k}^{2}-c_{i}^{2}-2\left(\beta_{i j} c_{i} c_{j}+\beta_{j k} c_{j} c_{k}+\beta_{k i} c_{k} c_{i}\right)\right]$$
where $\quad 2 \beta_{i j}=\lambda_{j k}-\lambda_{i k}, \quad 2 \beta_{j k}=\lambda_{j i}+\lambda_{k i}, \quad 2 \beta_{k i}=\lambda_{k j}-\lambda_{i j}$
and
$$\frac{d\left(c_{0}^{2}\right)}{d \tau}=\frac{d}{d \tau}\left(c_{1} c_{2} c_{3}\right)^{2}=c_{0}^{2}(\vec{x})\left[c_{i}^{2}+c_{j}^{2}+c_{k}^{2}-2\left(\alpha_{i j} c_{i} c_{j}+\alpha_{j k} c_{j} c_{k}+\alpha_{k i} c_{k} c_{i}\right)\right]$$
where $2 \alpha_{i j}=\lambda_{i k}+\lambda_{j k}, \quad 2 \alpha_{j k}=\lambda_{j i}+\lambda_{k i}, \quad 2 \alpha_{k i}=\lambda_{k j}+\lambda_{i j}$
$$\begin{aligned}
& \frac{d\left(c_{0}^{2}\right)}{d \tau}=c_{0}^{2}(\vec{x})\left[c_{i}^{2}+c_{j}^{2}+c_{k}^{2}-2\left(\alpha_{i j} c_{i} c_{j}+\alpha_{j k} c_{j} c_{k}+\alpha_{k i} c_{k} c_{i}\right)\right] \\
& \frac{d\left(c_{i}^{2}\right)}{d \tau}=c_{i}^{2}(\vec{x})\left[c_{j}^{2}+c_{k}^{2}-c_{i}^{2}-2\left(\beta_{i j} c_{i} c_{j}+\beta_{j k} c_{j} c_{k}+\beta_{k i} c_{k} c_{i}\right)\right]
\end{aligned}$$

Thus, Ricci flow is exhibited and implies a self-dual Bianchi-IX metric, otherwise known to be the Darboux-Halphen system describing the evolution of $S U(2)$ 3D geometries.

\section*{5 Other related systems}

The Darboux-Halphen system has analogues and equivalents in various forms of quadratic and non-linear differential equations. In this section, we will describe them in detail.

\subsection*{5.1 Ramamani to Darboux-Halphen}

The Ramamani system [28, 29] is described by the following differential equations
$$\begin{aligned}
& q \frac{d \mathcal{P}}{d q}=\frac{\mathcal{P}^{2}-\mathcal{Q}}{4} \\
& q \frac{d \tilde{\mathcal{P}}}{d q}=\frac{\tilde{\mathcal{P}} \mathcal{P}-\mathcal{Q}}{2} \\
& q \frac{d \mathcal{Q}}{d q}=\mathcal{P} \mathcal{Q}-\tilde{\mathcal{P}} \mathcal{Q}
\end{aligned}$$

In a recent paper Ablowitz et al. [30] showed that Ramamani's system of differential equations is equivalent to a third order scalar nonlinear ODE found by Bureau [31], whose solutions are given implicitly by a Schwarzian triangle function. Under a suitable variable transformation, the Ramamani system produces the classical Darboux-Halphen system.

The Ramamani system (5.1) for $q=\frac{1}{2 i \pi}$, is described by the equations
$$\begin{aligned}
& \dot{\mathcal{P}}=\frac{i \pi}{2}\left(\mathcal{P}^{2}-\mathcal{Q}\right) \\
& \dot{\widetilde{\mathcal{P}}}=i \pi(\mathcal{P} \widetilde{\mathcal{P}}-\mathcal{Q}) \\
& \dot{\mathcal{Q}}=2 i \pi(\mathcal{P}-\widetilde{\mathcal{P}}) \mathcal{Q}
\end{aligned}$$

We convert to Darboux-Halphen variables $(\mathcal{P}, \widetilde{\mathcal{P}}, \mathcal{Q}) \rightarrow(X, Y, Z)$ [32] as follows
$$\mathcal{P}=\frac{2}{i \pi} X \quad \widetilde{\mathcal{P}}=\frac{1}{i \pi}(2 X-Y-Z) \quad \mathcal{Q}=\frac{4}{\pi^{2}}(Z-X)(X-Y)$$

Naturally, if we apply the above transformation to the Ramamani equations (5.2), we shall get the classical Darboux-Halphen system equations.
$$\begin{aligned}
\dot{\mathcal{P}} & =\frac{2}{i \pi} \dot{X}=\frac{i \pi}{2}\left\{-\frac{4}{\pi^{2}} X^{2}-\frac{4}{\pi^{2}}\left(X Y+X Z-Y Z-X^{2}\right)\right\} \\
\Rightarrow \quad-\frac{4}{\pi^{2}} \dot{X} & =-\frac{4}{\pi^{2}}(X Y+X Z-Y Z)
\end{aligned}$$
and hence, we get one Darboux-Halphen equation in the form
$$\dot{X}=X(Y+Z)-Y Z$$

For the others, the process is more elaborate although quite straightforward to show.
$$\begin{gathered}
\begin{aligned}
& \dot{\widetilde{\mathcal{P}}}=\frac{1}{i \pi}(2 \dot{X}-\dot{Y}-\dot{Z})=i \pi\left\{-\frac{4}{\pi^{2}} X^{2}+\frac{2}{\pi^{2}} X(Y+Z)-\frac{4}{\pi^{2}}\left(X Y+X Z-Y Z-X^{2}\right)\right\} \\
& \Rightarrow \quad-\frac{1}{\pi^{2}}(2 \dot{X}-\dot{Y}-\dot{Z})=\frac{2}{\pi^{2}}(\dot{X}+Y Z)-\frac{4}{\pi^{2}} \dot{X} \\
& \Rightarrow \quad \dot{Y}+\dot{Z}=2 Y Z
\end{aligned}
\end{gathered}$$
$$\begin{aligned}
\dot{\mathcal{Q}}= & \frac{4}{\pi^{2}}[(\dot{Z}-\dot{X})(X-Y)+(Z-X)(\dot{X}-\dot{Y})]=\frac{8}{\pi^{2}}(Y+Z)(Z-X)(X-Y) \\
& \Rightarrow \quad\left(\dot{Z}-Z^{2}\right)(X-Y)+\left(Y^{2}-\dot{Y}\right)(Z-X)=0
\end{aligned}$$

Using (5.5), we have another DH equation
$$\dot{Y}=Y(Z+X)-Z X$$

Naturally, using (5.5) again, we should get the final equation
$$\dot{Z}=Z(X+Y)-X Y$$

Consequently, we have three sets of equations for the classical Darboux-Halphen system
$$\begin{aligned}
\dot{X} & =X(Y+Z)-Y Z \\
\dot{Y} & =Y(Z+X)-Z X \\
\dot{Z} & =Z(X+Y)-X Y
\end{aligned}$$

This is henceforth, another system related to the Ramanujan equations [33, 34] via the focal point of classical DH systems they converge to. We must note that, the Ramamani system gives rise to self dual (and not anti-self dual) Darboux-Halphen equations. Inverting the sign of the Halphen variables gives the familiar anti-self-dual system.

\subsection*{5.2 The Chazy equation}

Now, we shall see how the solution of the Darboux-Halphen system satisfies the Chazy equation [35, 36]. Let us take the previous result for anti-self-duality and $\lambda_{i j}=-1$ and write it for all values of $i, j, k$
$$\begin{aligned}
& \dot{\Omega}_{1}=\Omega_{2} \Omega_{3}-\Omega_{1}\left(\Omega_{2}+\Omega_{3}\right) \\
& \dot{\Omega}_{2}=\Omega_{3} \Omega_{1}-\Omega_{2}\left(\Omega_{3}+\Omega_{1}\right) \\
& \dot{\Omega}_{3}=\Omega_{1} \Omega_{2}-\Omega_{3}\left(\Omega_{1}+\Omega_{2}\right)
\end{aligned}$$

Adding up will give
$$\dot{\Omega}_{1}+\dot{\Omega}_{2}+\dot{\Omega}_{3}=-\left(\Omega_{1} \Omega_{3}+\Omega_{2} \Omega_{1}+\Omega_{3} \Omega_{2}\right)$$

If we define $y=-2\left(\Omega_{1}+\Omega_{2}+\Omega_{3}\right)$, we will have
$$\begin{aligned}
& \dot{y}=2\left(\Omega_{1} \Omega_{3}+\Omega_{2} \Omega_{1}+\Omega_{3} \Omega_{2}\right) \\
& \ddot{y}=-12 \Omega_{1} \Omega_{2} \Omega_{3}
\end{aligned}$$

Thus, the third order derivative will be
$$\begin{aligned}
\dddot{y}= & -12\left[\left\{\Omega_{2} \Omega_{3}-\Omega_{1}\left(\Omega_{2}+\Omega_{3}\right)\right\} \Omega_{2} \Omega_{3}+\Omega_{1}\left\{\Omega_{3} \Omega_{1}-\Omega_{2}\left(\Omega_{3}+\Omega_{1}\right)\right\} \Omega_{3}\right. \\
& \left.+\Omega_{1} \Omega_{2}\left\{\Omega_{1} \Omega_{2}-\Omega_{3}\left(\Omega_{1}+\Omega_{2}\right)\right\}\right] \\
= & 48 \Omega_{1} \Omega_{2} \Omega_{3}\left(\Omega_{1}+\Omega_{2}+\Omega_{3}\right)-12\left(\Omega_{2} \Omega_{3}+\Omega_{3} \Omega_{1}+\Omega_{1} \Omega_{2}\right)^{2} \\
= & 2 y \ddot{y}-3 \dot{y}^{2}
\end{aligned}$$

Thus, we obtain the Chazy equation [35]
$$\frac{d^{3} y}{d t^{3}}=2 y \frac{d^{2} y}{d t^{2}}-3\left(\frac{d y}{d t}\right)^{2}$$

\subsection*{5.3 The Ramanujan equation}

In case of the classical Chazy system, the Ramanujan equations [33, 34] are given by
$$\begin{aligned}
& \dot{P}=\frac{i \pi}{6}\left(P^{2}-Q\right) \\
& \dot{Q}=\frac{2 i \pi}{3}(P Q-R) \\
& \dot{R}=i \pi\left(P R-Q^{2}\right)
\end{aligned}$$

To understand how they are related to the Chazy equation, we shall examine what they imply systematically. From the first equation of (5.3.1), we find that
$$Q=P^{2}-\frac{6}{i \pi} \dot{P} \quad \Rightarrow \quad Q=Q(P, \dot{P})$$

Applying (5.3.2) to the second eq. of (5.3.1), we get
$$\begin{gathered}
\dot{Q}=\dot{Q}(P, \dot{P}, \ddot{P})=2\left(P \dot{P}-\frac{3}{i \pi} \ddot{P}\right) \\
\Rightarrow \quad R=R(P, \dot{P}, \ddot{P})=P Q-\frac{3}{2 i \pi} \dot{Q}=P^{3}-\frac{9}{i \pi} P \dot{P}-\frac{9}{\pi^{2}} \ddot{P}
\end{gathered}$$

Finally, using result (5.3.3) in the last equation of (5.3.1), we will get
$$\begin{gathered}
\dot{R}=i \pi\left(P R-Q^{2}\right)=3 P^{2} \dot{P}-\frac{9}{i \pi}\left(\dot{P}^{2}+P \ddot{P}\right)-\frac{9}{\pi^{2}} \dddot{P} \\
\therefore \quad \dddot{P}+i \pi\left(3 \dot{P}^{2}-2 P \ddot{P}\right)=0
\end{gathered}$$

However, we are not there yet. The final step requires us to take advantage of the non-linearity of this equation and write $P=\frac{y}{i \pi}$ to arrive at
$$\dddot{y}=2 y \ddot{y}-3 \dot{y}^{2}$$

This final result is the classical Chazy equation (5.5) we are familiar with.

\subsection*{5.4 Generalized Chazy System}

If we start instead with the generalized Darboux-Halphen equations and set the co-efficients as $\alpha_{1}=\alpha_{2}=\alpha_{3}=\frac{2}{n}$, we will get the corresponding generalized Chazy equation [23].
$$\frac{d^{3} y}{d t^{3}}-2 y \frac{d^{2} y}{d t^{2}}+3 \frac{d y^{2}}{d t}=\frac{4}{36-n^{2}}\left(6 \frac{d y}{d t}-y^{2}\right)^{2}$$

The set of transformations that leads the Ramanujan equations to the above generalized Chazy equation turn out to be:
$$\begin{aligned}
& \dot{P}=\frac{i \pi}{6}\left(P^{2}-Q\right) \\
& \dot{Q}=\frac{2 i \pi}{3}(P Q-R) \\
& \dot{R}=i \pi\left[P R-Q^{2}\left(1-\frac{36}{36-n^{2}}\right)\right]
\end{aligned}$$

The first two equations of (5.4.2) are the same as for (5.3.1), so the same steps will follow as with (5.3.2) and (5.3.3), but for the last step, we will have
$$\dddot{P}+i \pi\left(3 \dot{P}^{2}-2 P \ddot{P}\right)=\frac{4 i \pi}{36-n^{2}}\left(P^{2}-\frac{6}{i \pi} \dot{P}\right)^{2}$$

Applying the same variable redefinition $P=\frac{y}{i \pi}$ as before, we obtain
$$\frac{d^{3} y}{d t^{3}}-2 y \frac{d^{2} y}{d t^{2}}+3 \frac{d y^{2}}{d t}=\frac{4}{36-n^{2}}\left(6 \frac{d y}{d t}-y^{2}\right)^{2}$$
which is exactly the generalized Chazy equation described before.

\section*{6 Integrability of the Bianchi-IX}

There are various impositions possible on a 4-dimensional Riemannian metric. It could be Kähler or Einstein or even have an anti-self-dual (ASD) Weyl tensor. The venn-diagram below depicts the various possibilities resulting to different field equations in 4-dimensions, where the intersection zones correspond to interesting conditions.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/45fdabd6-49f3-4492-a4a6-6f855df3cbd4-18.jpg?height=606&width=1321&top_left_y=550&top_left_x=366}
\captionsetup{labelformat=empty}
\caption{The shaded part corresponds to $(\mathrm{AUBUC})-(\mathrm{BUC})=\mathrm{A}-(\mathrm{A} \cap \mathrm{B})-(\mathrm{A} \cap \mathrm{C})+(\mathrm{A} \cap \mathrm{B} \cap \mathrm{C})$ and are hyper kahler metrics with 3 integrable complex structures with quaternionic algebra (remember they are not kahler)}
\end{figure}

If $\left(e^{0}, e^{1}, e^{2}, e^{3}\right)$ define the vierbeins on a Riemannian 4-manifold, the basis of self-dual 2-forms is given as
$$* \eta^{i}=\eta^{i}=\eta_{a b}^{i} e^{a} \wedge e^{b}:\left\{\begin{array}{l}
\eta^{1}=e^{0} \wedge e^{1}+e^{2} \wedge e^{3} \\
\eta^{2}=e^{0} \wedge e^{2}+e^{3} \wedge e^{1} \\
\eta^{3}=e^{0} \wedge e^{3}+e^{1} \wedge e^{2}
\end{array}\right.$$

Similarly, the anti-self-dual 2-form basis is given by
$$* \bar{\eta}^{i}=-\bar{\eta}^{i}=\bar{\eta}_{a b}^{i} e^{a} \wedge e^{b}:\left\{\begin{array}{l}
\bar{\eta}^{1}=e^{0} \wedge e^{1}-e^{2} \wedge e^{3} \\
\bar{\eta}^{2}=e^{0} \wedge e^{2}-e^{3} \wedge e^{1} \\
\bar{\eta}^{3}=e^{0} \wedge e^{3}-e^{1} \wedge e^{2}
\end{array}\right.$$

If $\omega^{i}{ }_{j}$ are the spin connection 1-forms for the self-dual part, then the first Cartan equation is given by
$$d \eta^{i}=\omega^{i}{ }_{j} \wedge \eta^{j}$$

The curvature 2-form is given as usual by the 2nd Cartan structure equation (2.2.1). It is possible to expand the curvature in terms of $\eta^{i}$ and $\bar{\eta}^{i}$ as
$$R_{i j}=W_{i j}{ }^{k} \eta_{k}+\Phi_{i j}{ }^{k} \bar{\eta}_{k}$$
where $W_{i j k}$ \& $\Phi_{i j k}$ are unknown co-efficients determined by the conditions imposed by various field equations.

\section*{Conditions determining $W_{i j k}$ \& $\Phi_{i j k}$}

The 1st Bianchi identity $R^{i}{ }_{j} \wedge \eta^{j}=0$ implies $W_{i j j}=0$, further implying that $W_{i j k}$ has 6 independent components, out of which 5 correspond to the SD Weyl tensor and one to the totally anti-symmetric part corresponding to Ricci scalar. On the other hand, $\Phi_{i j k}$ has 9 components corresponding to trace-free Ricci tensor.
\begin{itemize}
\item[1.] Iff $W_{i j k}=\Lambda \epsilon_{i j k}$, where $\Lambda$ is a multiple of Ricci scalar, we are in Set A ⇒ ASD Weyl.
\item[2.] Iff $W_{i j k}=\Lambda \epsilon_{i j k}$ and $\Phi_{i j k}=0$, then we have ASD Einstein $(A \cap B)$.
\item[3.] Iff $W_{i j k}=0=\Phi_{i j k}$, we are in ( $A \cap B \cap C$ ) which is hyper-Kähler.
\end{itemize}

Returning to the Bianchi-IX metric (2.1) and using the parametrization (2.1.5), it can be written in terms of the basis $\left(\sigma^{1}, \sigma^{2}, \sigma^{3}\right)$ of left-invariant forms on $S U(2)$ as
$$d s^{2}=\left[\Omega_{1}(r) \Omega_{2}(r) \Omega_{3}(r)\right] d r^{2}+\frac{\Omega_{2} \Omega_{3}}{\Omega_{1}} \sigma_{1}^{2}+\frac{\Omega_{3} \Omega_{1}}{\Omega_{2}} \sigma_{2}^{2}+\frac{\Omega_{1} \Omega_{2}}{\Omega_{3}} \sigma_{3}^{2}$$
where $\Omega_{i}, \forall i=1,2,3$ are functions of $r$ and $\sigma^{i}$ s satisfy Maurer Cartan equations. From this form of the metric, the vierbeins can be used to produce the SD 2-forms:
$$\eta^{i}=\Omega_{j} \Omega_{k} d r \wedge \sigma^{i}+\Omega_{i} \sigma^{j} \wedge \sigma^{k} \quad i \neq j \neq k$$

Therefore, the connection 1-forms $\omega_{i j}$ can be written in terms of arbitrary functions $A_{i}$ of $r$, $\forall i=1,2,3$ such that
$$\omega_{12}=\frac{A_{3}}{\Omega_{3}} \sigma^{3}+(\text { cyclic permutations })$$

All $A_{i}$ components are obtained from the system below:
$$\dot{\Omega}_{i}=\Omega_{j} \Omega_{k}-\Omega_{i}\left(A_{j}+A_{k}\right) \quad i \neq j \neq k=1,2,3$$

We will refer to this system as the first system for future reference.
With the help of Cartan calculus, one can find the curvature 2-forms in terms of derivatives of $A_{i}$ s. With the specific choice of field equations from restricitng ourselves to a specific region of the diagram (indicated in the Venn diagram), we will obtain a second system of 1st order differential equations involving $A_{i}$.

If we choose regions outside the top circle, we typically get non-integrable equations. Dancer and Strachan [37] already showed this for Einstein Kähler $(B \cap C)$, while Barrow [38] showed the same thing for Einstein (Set $B$ ). However, field equations belonging to the top circle A are integrable, as expected from the heuristic, yet concrete argument that self-duality implies integrability. according to Mason [39].

Imposing the vanishing of ASD Weyl tensor and the scalar curvature $\omega_{i j}$ results in the system of the equation widely known as Chazy system [13, 40]. This system has a long history, having been studied and solved in the 19th century by Brioschi [41].
$$\dot{A}_{i}=A_{j} A_{k}-A_{i}\left(A_{j}+A_{k}\right) \quad i \neq j \neq k=1,2,3$$

We shall now list the following features of the first and second systems:
\begin{itemize}
\item[i)] If all $A_{i}=0$, then the connection of ASD 2-forms are clearly flat and the metric describes vaccum. This was found by Belinsky [42] and Eguchi-Hanson [43].
\item[ii)] If $\Omega_{i}=A_{i}, \forall i$, then the first and second systems of equations are identical, which is precisely the Atiyah and Hitchin's [44] case.
\item[iii)] If one insists all $A_{i}$ s to be constant in r, then without any loss of generality, if two of them necessarily vanish, then the remaining $A_{i} \neq 0$ can reduce the first system to a special case of Painleve-III [45]. Also, the form $\eta^{i}$ is covariant constant in this case so that one arrives at the Pederson-Poon scalar flat Kähler metric [46].
\item[iv)] There exists a significant conserved quantity
$$Q=\frac{\Omega_{1}^{2}}{\left(A_{1}-A_{2}\right)\left(A_{1}-A_{3}\right)}+\frac{\Omega_{2}^{2}}{\left(A_{2}-A_{1}\right)\left(A_{2}-A_{3}\right)}+\frac{\Omega_{3}^{2}}{\left(A_{3}-A_{1}\right)\left(A_{3}-A_{2}\right)}$$
\end{itemize}

There is a covariance under fractional linear transformations in $r$ [45], which means that the solutions of the second system with $A_{1}=A_{2} \neq 0$ is conformally related to the Pederson-Poon case [46].

Now, for a general solution of the second system, we introduce a new dependent variable $x$ as per Brioschi [41]
$$x=\frac{A_{1}-A_{2}}{A_{3}-A_{2}}$$

It is now straightforward to show that (6.9) reduces to the 3rd order ODE for $x$
$$\dddot{x}=\frac{3}{2} \frac{\ddot{x}^{2}}{\dot{x}}-\frac{1}{2}(\dot{x})^{3}\left(\frac{1}{x^{2}}+\frac{1}{x(x-1)}+\frac{1}{(x-1)^{2}}\right)$$

A remarkable fact is that this ODE is satisfied by the reciprocal of the elliptic modular function. Now this elliptic modular function has a natural boundary in the r-plane, so the $A_{i}$ and hence $\Omega_{i}$ have a natural boundary in the r-plane and the location of the boundary depends on the constants of integration. This implies the self-duality equations are not always equivalent to Painleve property, and thus integrable.

Now we introduce new dependent variables $\rho_{i}, \forall i=1,2,3$ according to
$$\Omega_{1}=\rho_{1} \frac{\dot{x}}{\sqrt{x(1-x)}} \quad \Omega_{2}=\rho_{2} \frac{\dot{x}}{x \sqrt{(1-x)}} \quad \Omega_{3}=\rho_{3} \frac{\dot{x}}{\sqrt{x}(1-x)}$$
and switch independent variable from $r$ to $x$ (ie. $\dot{x} \equiv \frac{d x}{d r}$ ), so the first system becomes
$$\frac{d \rho_{1}}{d x}=\frac{\rho_{2} \rho_{3}}{x(1-x)} \quad \frac{d \rho_{2}}{d x}=\frac{\rho_{3} \rho_{1}}{x} \quad \frac{d \rho_{3}}{d x}=\frac{\rho_{1} \rho_{2}}{(1-x)}$$

This system is known to reduce to Painleve VI with the first integral
$$\gamma=\frac{1}{2}\left(\rho_{2}^{2}+\rho_{3}^{2}-\rho_{1}^{2}\right)=\mathrm{const}$$
which is in fact the conserved quantity (6.10), with the new metric being
$$d s^{2}=\frac{\rho_{1} \rho_{2} \rho_{3}}{x(1-x)} \dot{x}\left[\frac{d x^{2}}{x(1-x)}+\frac{\left(\sigma^{1}\right)^{2}}{\rho_{1}^{2}}+\frac{(1-x)\left(\sigma^{2}\right)^{2}}{\rho_{2}^{2}}+\frac{x\left(\sigma^{3}\right)^{2}}{\rho_{3}^{2}}\right]$$

Now we shall solve the new version of the first system where we will try to form an equation for $\rho_{3}$ only. Due to the existence of the first integral $\gamma$, this will be second order equation. To recognize it better, we introduce a new independent variable $z$, given as
$$x=\frac{4 \sqrt{z}}{(1+\sqrt{z})^{2}}$$
a new dependent variable $V$ given by
$$\rho_{3}=\frac{z}{V} \frac{d V}{d z}-\frac{V}{2(z-1)}-\frac{1}{2}+\frac{z}{2 V(z-1)}$$

It is not very tedious to show that $V$ satisfies Painleve-VI equations with parameters $(\alpha, \beta, \gamma, \delta)$ in the notation of [47] or $\left(\frac{1}{8},-\frac{1}{8}, \gamma, \frac{1}{2}(1-2 \gamma)\right)$ in the notation of [13]. Thus, we see the equation for the conformal factor
$$\Theta=\frac{\rho_{1} \rho_{2} \rho_{3}}{x(1-x)} \frac{d x}{d t}$$
has the Painleve property, but it also contains the function $x(\tau)$ which has a natural boundary. The choice of conformal factor is equivalent to a gauge choice to make the Ricci scalar vanish.

Now we have found the general solution of the metric (6.5) inside the top circle of the figure (the shaded region of A). Also note that ASD Bianchi-IX metrics are not always diagonal in the chosen invariant basis of 1-forms. We can always adjust the conformal factor $\Theta$ in order to make this ASD Bianchi type metric to become Einstein. This would constitute a metric for the region $A \cap B$, which are quaternionic Kähler type of metrics and are diagonal in the basis.

The solution for the conformal factor was found in [48] with $\gamma=\frac{1}{8}$ and writing down the desired condition as a set of equations on $\Theta$ and finally solve it. After a little algebra and once all the dusts get settled, we get $\Theta=\frac{N}{D^{2}}$, with
$$\begin{aligned}
& N=2 \rho_{1} \rho_{2} \rho_{3}\left(4 x \rho_{1} \rho_{2} \rho_{3}+P\right) \\
& P=x\left(\rho_{1}^{2}+\rho_{2}^{2}\right)-\left(1-4 \rho_{3}^{2}\right)\left(\rho_{2}^{2}-(1-x) \rho_{1}^{2}\right) \\
& D=x \rho_{1} \rho_{2}+2 \rho_{3}\left(\rho_{2}^{2}-(1-x) \rho_{1}^{2}\right)
\end{aligned}$$

Since the equation for $\rho_{3}$ is a 2nd order differential equation, the metric depends on two arbitrary constants. Particularly it is worth mentioning that there exists ASD Einstein metrics on $S^{4}$, which with appropriate choices of field equations fill in the general left-invariant metric on $S^{3}$ similar to the case of a 4-dim hyperbolic metric that fills the round metric on $S^{3}$.

\section*{7 Conclusions}

Summarizing we have seen that there exist two different approaches that lead up to the classical Darboux-Halphen system. One approach starts from the Bianchi-IX metric and considers its anti-self-dual case, while the other starts with a reduction of the self-dual Yang-Mills equation and takes only the diagonal elements of the resulting matrix equation. When we start with SDYM gauge fields, it is clear why we cannot always reliably find a metric or its vierbeins that correspond to the
generalized DH system. The classical configuration is a typical prototype where it is possible, as was seen from the way we could obtain it from the self-dual Bianchi-IX metric.

We have computed the form of curvature and confirmed that self-dual cases turn out to be Ricci-flat. We also discovered that the classical Darboux-Halphen is found to exhibit Ricci flow for a modified Bianchi-IX system. We also confirmed that this system satisfies the Chazy equation as well and is strongly related to other systems of differential equations, such as the Ramanujan and Ramamani systems.

It remains a challenge to find other integrable systems of number theoretic importance. Another useful direction could be to solve DH type systems (3.2.5) and (3.2.6) using moving monodromy methods and compare the results. We are also trying to find out interesting 1+1 dimensional or 2+1 dimensional DH type systems that can be solved using inverse scattering transform and can be studied to uncover several widely known aspects of integrability. Another testing ground could be various scalar flat Kähler metrics namely the LeBrun metric with $U(1)$ isometry that contains Gibbons-Hawking, Real heaven and Burns metric as special limits and were used to test the bottomup approach of emergent gravity [49]. Using monodromy evolving deformation [50] on Plebanski type self dual Einstein equations which are actually the EOM obtained from the 2- dim chiral $U(N)$ model in the large $N$ limit and studying integrability might clarify some important issues for the test of emergent gravity [51].

\section*{8 APPENDIX}
t'Hooft symbols
Matrices representing the t'Hooft symbols would be given by :
$$\begin{array}{lll}
\eta^{(+) 1}=\left(\begin{array}{cccc}
0 & 0 & 0 & 1 \\
0 & 0 & 1 & 0 \\
0 & -1 & 0 & 0 \\
-1 & 0 & 0 & 0
\end{array}\right) & \eta^{(+) 2}=\left(\begin{array}{cccc}
0 & 0 & -1 & 0 \\
0 & 0 & 0 & 1 \\
1 & 0 & 0 & 0 \\
0 & -1 & 0 & 0
\end{array}\right) & \eta^{(+) 3}=\left(\begin{array}{cccc}
0 & 1 & 0 & 0 \\
-1 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & -1 & 0
\end{array}\right) \\
\eta^{(-) 1}=\left(\begin{array}{cccc}
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0 \\
0 & -1 & 0 & 0 \\
1 & 0 & 0 & 0
\end{array}\right) & \eta^{(-) 2}=\left(\begin{array}{cccc}
0 & 0 & -1 & 0 \\
0 & 0 & 0 & -1 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0
\end{array}\right) & \eta^{(-) 3}=\left(\begin{array}{cccc}
0 & 1 & 0 & 0 \\
-1 & 0 & 0 & 0 \\
0 & 0 & 0 & -1 \\
0 & 0 & 1 & 0
\end{array}\right)
\end{array}$$
which obey the following relations between themselves
$$\begin{aligned}
& \sum_{i=1}^{3} \eta_{\mu \nu}^{( \pm) i} \eta_{\lambda \gamma}^{( \pm) i}=\delta_{\mu \lambda} \delta_{\nu \gamma}-\delta_{\mu \gamma} \delta_{\nu \lambda} \pm \varepsilon_{\mu \nu \lambda \gamma} \\
& {\left[\eta^{( \pm) i}, \eta^{( \pm) j}\right]_{\mu \nu} }=-2 \epsilon^{i j k} \eta_{\mu \nu}^{( \pm) k} \\
& {\left[\eta^{( \pm) i}, \eta^{(\mp) j}\right]_{\mu \nu}=0 \quad \Rightarrow \quad \eta_{\mu \rho}^{( \pm) i} \eta_{\rho \nu}^{(\mp) j}=\eta_{\nu \rho}^{( \pm) j} \eta_{\rho \mu}^{(\mp) i} }
\end{aligned}$$
$$\begin{gathered}
\left\{\eta^{( \pm) i}, \eta^{( \pm) j}\right\}_{\mu \nu}=-2 \delta^{i j} \delta_{\mu \nu} \\
\left\{\eta^{( \pm) i}, \eta^{(\mp) j}\right\}_{\mu \nu}=0 \quad \Rightarrow \quad \eta_{\mu \nu}^{( \pm) i} \eta_{\mu \nu}^{( \pm) j}=0 \\
\therefore \quad \eta_{\mu \lambda}^{( \pm) i} \eta_{\nu \lambda}^{( \pm) j}=\delta^{i j} \delta_{\mu \nu}+\epsilon^{i j k} \eta_{\mu \nu}^{( \pm) k} \\
\epsilon_{\mu \nu \lambda \gamma} \eta_{\gamma \sigma}^{( \pm) i}=\mp\left(\delta_{\sigma \lambda} \eta_{\mu \nu}^{( \pm) i}+\delta_{\sigma \mu} \eta_{\nu \lambda}^{( \pm) i}-\delta_{\sigma \nu} \eta_{\mu \lambda}^{( \pm) i}\right) \\
\therefore \quad \epsilon^{i j k} \eta_{\mu \nu}^{( \pm) j} \eta_{\rho \sigma}^{( \pm) k}=\delta_{\mu \sigma} \eta_{\rho \nu}^{( \pm) i}-\delta_{\nu \sigma} \eta_{\rho \mu}^{( \pm) i}+\delta_{\rho \mu} \eta_{\nu \sigma}^{( \pm) i}-\delta_{\rho \nu} \eta_{\mu \sigma}^{( \pm) i}
\end{gathered}$$

\section*{Acknowledgement}

One of the authors SC would like to thank Marios Petropoulos for several correspondences during the course of this project and Thanu Padmanabhan for an enlightening discussions on a subject related to this article. The research of RR was supported by FAPESP through Instituto de Fisica, Universidade de Sao Paulo with grant number 2013/17765-0.

\section*{References}
\begin{itemize}
\item[] [1] G. W. Gibbons and S. W. Hawking, Gravitational Multi-instantons, Phys. Lett. B 78 (1978).
\item[] [2] G. W. Gibbons and S. W. Hawking, Classification of Gravitational Instanton Symmetries, Comm. Math. Phys. 66, 291-310 (1979).
\item[] [3] G. W. Gibbons and S. W. Hawking, Euclidean Quantum Gravity, World Scientific (1993).
\item[] [4] M.J. Ablowitz, S. Chakravarty and R.G. Halburd, Integrable systems and reductions of the self-dual Yang-Mills equations (2003) J. Math. Phys. 44 3147-72.
\item[] [5] George F. R. Ellis and Henk van Elst Cosmological models (Cargese lectures 1998)
\item[] [6] Yuri Manin and Matilde Marcolli Symbolic Dynamics, Modular Curves, and Bianchi IX Cosmologies, arXiv:1504.04005 [gr-qc].
\item[] [7] Yuri Manin and Matilde Marcolli Big Bang, Blowup, and Modular Curves: Algebraic Geometry in Cosmology, arXiv:1402.2158 [gr-qc], SIGMA 10 (2014), 073.
\item[] [8] P. Marios Petropoulos and Pierre Vanhove, Gravity, strings, modular and quasimodular forms, arXiv:1206.0571 [math-ph], CPHT-RR005.0211, IPHT-t12/016, IHES/P/12/08.
\item[] [9] D. Hobill, A. Burd, A.A. Coley, Deterministic Chaos in General Relativity, Nato Science Series B:, Vol. 332, Plenum Press New York (1994).
\item[] [10] P.M. Petropoulos, Gravitational instantons, Ricci flows and integrable structures, Talk during Workshop on Field Theory and Geometric Flows at LMU, Munich.
\item[] [11] P.M. Petropoulos, Self-duality, gravitational instantons and geometric flows, Talk during Geometric Flows in Mathematics and Theoretical Physics conference at SNS, Pisa.
\end{itemize}
\begin{itemize}
\item[] [12] M. Cvetic, G. W. Gibbons, H. Lu and C. N. Pope Bianchi IX self-dual Einstein metrics and singular G2 manifolds, arXiv:0206151 [hep-th], Class. Quant. Grav. Vol 20, No. 19
\item[] [13] M.J. Ablowitz and P.A. Clarkson, Solitons, nonlinear equations and inverse scattering. 1991, LMS lecture note series 149.
\item[] [14] G. W. Gibbons and C. M. Warnick Hidden symmetry of hyperbolic monopole motion, arXiv:0609051 [hep-th], J.Geom.Phys. 57 : 2286, 2007
\item[] [15] Wentao Fan, Farzad Fathizadeh and Matilde Marcolli Modular forms in the spectral action of Bianchi IX gravitational instantons, arXiv:1511.05321 [math.DG].
\item[] [16] Sumanto Chanda, Partha Guha, Raju Roychowdhury, Emergent Schwarzschild : symplectic, geometric and topological perspective arXiv:1406.6459v3
\item[] [17] Sumanto Chanda, Partha Guha, Raju Roychowdhury, Taub-NUT and Dynamical Systems : the geometric connection demystified arXiv:1503.08183v2.
\item[] [18] Tohru Eguchi and Andrew J. Hanson, Self-Dual Solutions to Euclidean Gravity Annals of Physics 120.1 (1979): 82-106.
\item[] [19] M.J. Ablowitz, S. Chakravarty and R.G. Halburd, The Darboux-Halphen System and the Singularity Structure of its Solutions, Proc. 4th Int. Conf. on Mathematical and Numerical Aspects of Wave Propagation. 1998.
\item[] [20] W. Nahm, All self-dual multimonopoles for arbitrary gauge groups, CERN, preprint TH. 3172., NATO ASI, B 82 (1983) pp. 301
\item[] [21] N. Hitchin, On the construction of monopoles. Comm. Math. Phys. 89 (2): 145
\item[] [22] S. Donaldon,Nahm's equations and the classification of monopoles, Comm. Math. Phy. 96 (3), 387
\item[] [23] S. Chakravarty and R.G. Halburd, First integrals and gradient flow for a generalized Darboux-Halphen system, Contemp. Math., vol. 301, Amer. Math. Soc., Providence, RI, 2002, 273-281.
\item[] [24] S. Chakravarty and R.G. Halburd, First integrals of a generalized Darboux-Halphen system, J. Math. Phys., Vol. 44, No. 4, April 2003.
\item[] [25] P.M. Petropoulos, Geometric flows and applications, CPHT-PC012.0210, arXiv:1011.1106v1 [hep-th].
\item[] [26] Ioannis Bakas, Francois Bourliot, Dieter Lust, Marios Petropoulos, Geometric flows in Horava-Lifshitz gravity, JHEP 04 (2010)131, arXiv:1002.0062 [hep-th].
\item[] [27] G. Holzegel, T. Schmelzer, C. Warnick, Ricci Flow of Biaxial Bianchi IX Metrics, arXiv:0706.1694v1 [hep-th].
\item[] [28] Ramamani V 1970 On some identities conjectured by Ramanujan in his lithographed notes connected with partition theory and elliptic modular functions-their proofs-interconnection with various other topics in the theory of numbers and some generalizations thereon Ph.D. thesis, The university of Mysore
\item[] [29] Ramamani V 1989 On some algebraic identities connected with Ramanujan's work Ramanujan International Symposium on Analysis ed N K Thakare (New Delhi: Macmillan India) pp 279-91
\item[] [30] M. Ablowitz, S. Chakravarty and H. Hahn, Integrable systems and modular forms of level 2, J. Phys. A: Math. Gen. 39 (2006), no. 50, 15341-15353.
\end{itemize}
\begin{itemize}
\item[] [31] F. Bureau, Differential equations with fixed critical points, Annali di Matematica 64 (1964) 229-364.
\item[] [32] Yurii V. Brezhnev, Simon L. Lyakhovich and Alexey A.Sharapov, Dynamical systems determining Jacobi's $\theta$-constants. Journ. Math. Phys. (2011), 52(11), 112704 (1-21)
\item[] [33] Ramanujan S 1916 On certain arithmetical functions Trans. Cambridge Philos. Soc. 22 159-84
\item[] [34] Ramanujan S 1927 Collected Papers (Cambridge: Cambridge University Press); reprinted 1962 (New York: Chelsea); reprinted 2000 (Providence: American Mathematical Society)
\item[] [35] Chazy J 1909 Sur les équations différentielles dont l'intégrale générale est uniforme et admet des singularités essentielles mobiles C. R. Acad. Sci. Paris 149 563-5
\item[] [36] Robert S. Maier, Quadratic differential systems and Chazy equations 1, arXiv:1203.0283v2 [math.CA].
\item[] [37] Andrew S. Dancer and Ian A.B. Strachan, Einstein metrics on tangent bundles of spheres. 1994. Math. Proc. Camb. Phil. Soc. 115, (513-525).
\item[] [38] John D. Barrow, General relativistic chaos and nonlinear dynamics. 1982, Gen. Rel. Grav. 14 523-530.
\item[] [39] L.J. Mason, 1990, Further advances in Twistor Theory.
\item[] [40] J. Chazy General relativistic chaos and nonlinear dynamics. 1910, C.R. Acad. Sci 150, 456.
\item[] [41] F. Brioschi, 1881, C.R. Acad. Sci. tXCII 1389.
\item[] [42] V.A. Belinsky, G.W. Gibbons, D.N. Page, C.N. Pope, Asymptotically Euclidean Bianchi IX metrics in quantum gravity, Phys. Lett. B, 76 (1978) 433.
\item[] [43] Tohru Eguchi and Andrew J. Hanson, Asymptotically flat self-dual solutions to euclidean gravity, Phys. Lett. B, 237 (1978) 249.
\item[] [44] M.F. Atiyah and N.J. Hitchin, The geometry and dynamics of magnetic monopoles, (Princeton University Press, 1988), Phys. Lett. A, 167 (1985) 21.
\item[] [45] K.P. Tod, A comment on a paper of Pederson and Poon (general relativity), 1991 Class. Quant. Grav. 8, 1049-1051.
\item[] [46] H. Pedersen and Y.S. Poon, Kähler surfaces with zero scalar curvature, 1990 Class. Quant. Grav. 7, 1707.
\item[] [47] Ince, E.L., Ordinary Differential Equations, 1956, Dover.
\item[] [48] K.P. Tod, 1995, Twistor Theory, Ed. S. Huggett, Dakker, Lecture Notes in Pure and Applied Mathematics 169.
\item[] [49] S.Lee, R.Roychowdhury and H.S.Yang, Notes on Emergent Gravity, JHEP 1209, 030 (2012), arXiv:1206.0678 [hep-th].
\item[] [50] M.J. Ablowitz and S. Chakravarty, Integrability, Monodromy Evolving Deformations, and Self-Dual Bianchi IX Systems, Phys. Rev. Lett.76. No.6, 857 (1996).
\item[] [51] S.Lee, R.Roychowdhury and H.S.Yang, Test of Emergent Gravity, Phys.Rev.D 88, 086007 (2013), arXiv:1211.0207 [hep-th].
\end{itemize}