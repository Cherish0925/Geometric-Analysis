```{=latex}
\maketitle
```
```{=latex}
\begingroup
```
```{=latex}
\small
```
```{=latex}
\linespread{1.0}
```
```{=latex}
\selectfont
```
```{=latex}
\setlength{\parskip}{0pt}
```
```{=latex}
\tableofcontents
```
```{=latex}
\endgroup
```
```{=latex}
\clearpage
```
原题、量词与成功标准
--------------------

本会话组的工作命题保持为：对每个维数 $n\ge2$，是否存在只依赖 $n$ 的实常数 $c_n<C_n$，使任意闭、连通、光滑实流形 $M^n$ 只要承载一个度量 $g$ 满足 $$\label{eq:Q}
 c_ng\le\operatorname{Ric}_g\le C_ng,$$ 就承载某个光滑 Einstein 度量 $h$，即 $\operatorname{Ric}_h=\lambda h$，$\lambda\in\mathbb R$？不要求 $h$ 接近 $g$，不要求 $h$ 与 $g$ 的 Ricci 符号相同；结论针对同一*光滑流形*，不是仅同胚类型。

历史归属为 Yau 1982 年 *Problem Section* 的第26题[@Yau1982]。当前归档没有附上原始题页的完整可核对影像；上式是三个会话反复确认的工作表述，而不是本文件宣称已经逐字认证的历史引文。续接时应在当前工作区核对原始任务书与题页，若发现实质差异，单列差异并调整对应推论，不把相邻的稳定性问题替换成原题。

定义 $$\label{eq:defect}
 \delta_\sigma(g)=\left\lVert g^{-1}\operatorname{Ric}_g-\sigma\operatorname{Id}\right\rVert_{L^\infty,\mathrm{op}},\qquad
 e_\sigma(M)=\inf_{g\in\operatorname{Met}(M)}\delta_\sigma(g),\qquad \sigma\in\{+1,-1\}.$$ $P_n^\sigma$ 表示存在仅依赖 $n$ 的 $\varepsilon_n>0$，使 $\delta_\sigma(g)<\varepsilon_n$ 推出 $M$ 承载某个 Einstein 度量。工作命题满足 $$\label{eq:branches}
 Q_n\quad\Longleftrightarrow\quad P_n^+\ \lor\ P_n^-.$$ 证明只用缩放：$\widehat g=ag$ 时，作为 $(0,2)$ 张量的 Ricci 不变，Ricci 端同态变为 $a^{-1}g^{-1}\operatorname{Ric}_g$。任一非退化区间都有一个非零内点 $\mu$ 及同号小邻域；将 $\operatorname{Ric}\approx\operatorname{sign}(\mu)g$ 的度量按 $1/|\mu|$ 缩放即可进入该邻域。反向直接取以 $\pm1$ 为中心的小区间。

因此，一个固定维数的*证明*只需要完成其中一个符号分支；*完整反驳*要在同一维数击败两个符号分支，可以使用不同流形。每个流形都必须排除任意符号的全部 Einstein 度量。构造 $e_\sigma(M)=0$ 本身是一项独立结论，但它只有与该 $M$ 的全部 Einstein 不存在性相结合，才构成分支反例。

二维由一致化、三维正分支由 Hamilton 的正 Ricci 结果提供经典基线；不得把这些作为本项目的新成果。四维的专门工具不会自动推广到 $n\ge5$。本文件允许严谨的强中间结果独立成文，但不把它们改称原题的完整解决。

### 统一范数，避免四倍因子再次混入

下列 $W^\pm$ 与签名公式在定向四维范畴内使用；非定向情形须另行处理定向双覆盖及等变下降，不能由覆盖的Einstein存在直接推出原流形结论。四维设 $s=\operatorname{tr}_g\operatorname{Ric}$、$E=\operatorname{Ric}-\frac{s}{4}g$。本文件的 $W^\pm$ 使用在 $\Lambda^2_\pm$ 上的曲率*算子*范数；$E$ 和 Ricci 使用张量范数。于是 $$\begin{aligned}
8\pi^2\chi(M)&=\int_M\left(|W^+|^2+|W^-|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)\,d\mu_g,\label{eq:CGB}\\
12\pi^2\tau(M)&=\int_M(|W^+|^2-|W^-|^2)\,d\mu_g,\label{eq:signature}\\
|\operatorname{Rm}_{\rm full}|^2&=4(|W^+|^2+|W^-|^2)+2|E|^2+\frac{s^2}{6}.\end{aligned}$$ 若写 $\mathcal R$ 表示完整曲率算子，则 $|\operatorname{Rm}_{\rm full}|^2=4|\mathcal R|^2$。精确 Einstein 时分别有 $\int|\mathcal R|^2=8\pi^2\chi$ 和 $\int|\operatorname{Rm}_{\rm full}|^2=32\pi^2\chi$。Eguchi--Hanson 的 $12\pi^2$ 能量采用前一种规范；后一种为 $48\pi^2$。

$\delta_\sigma\le\delta$ 给出 $$|s-4\sigma|\le4\delta,\qquad |E|^2\le4\delta^2,\qquad
 |\operatorname{Ric}-\sigma g|^2\le4\delta^2.$$ 全文不把小 $L^p$ 积分、小加权范数、局部精确解，替换成原题要求的全域无权 Ricci 端同态上确界。

材料边界与使用方式
------------------

本文件供研究在任何合适的会话或阶段继续，不规定下一步编号或固定分工。它保留网页端续接原稿的详细论证，并结合本地现存的完整 `\path{Yau26_uniform_gap.tex}`{=latex}、20260910研究稿、20260912累积稿第一及第五章、逐步归档04/06/10/11以及A01的原始笔记校正。A01的100条canonical Cell-Relay均按任务、接续和推理片段作过阶段扫描，用于找回主题和后期修正；这不等于逐行复核100步内的全部证明和程序。

完整统一间隙原稿现已取得，在本目录以 `\path{20260916_uniform_gap.tex}`{=latex} 原样保存。其他详细证明和程序仍可沿用户工作区路径读取。早期网页上下文中"原稿没有上传""只有摘要"的描述，不再表示目前的资料状态。外部文献条目及原有核查记录继承自所引原稿；本次整合直接检查的是这些本地材料，不宣称重新逐篇核查了全部外部论文或完成全球查新。

下列标签只用于区分证据，不对数学内容按平台打分：**【文献】**表示原稿采用的外部定理或明确引用；**【原稿审读】**表示已有实质审读记录支持；**【轨迹】**表示会话记载的推导或内部核验；**【本稿重算】**表示下文完整展示的代数或逻辑推导；**【待证】**表示仍需新证明的目标。已撤回结论只作为边界保存，不进入定理依赖。

精确 Einstein 的统一*拓扑*间隙已有原稿审读支持，不能再因一般 near-Einstein 平滑接口未闭合而降回"只有摘要的想法"。一般 near-Einstein 的统一*Ricci夹逼*间隙仍未完成，不能因前一项成立就自动升级。固定 $A_1$ 近 Einstein 构造与全局 Einstein 不存在性也是两个命题。

第一次接续应读取本会话当前任务书、工作区最近修正及下文列出的原稿，记录版本；*不重启已经做完的300步，也不把审读报告当成原稿全文*。三份文件彼此独立可编译；没有要求安装新应用或改变系统基础架构。缺失来源的恢复应服务于一个具体定理，不应演变为无期限重复检索。

已经取得的主结果及其逻辑位置
----------------------------

### 精确Einstein的统一拓扑间隙

```{=latex}
\begin{theorem}[原稿审读支持的主定理]\label{thm:topgap}
设 $X$ 是闭极小一般型复曲面，$b_+(X)>1$，$A=c_1^2(X)>0$，并令
\[
M=X\#k\overline{\CP^2},\qquad k\in\Z_{\ge0}.
\]
存在与 $X,k$ 无关的 $\gamma\in(0,1/3)$，使
\begin{equation}\label{eq:topgap}
 k\ge(1/3-\gamma)A\quad\Longrightarrow\quad
 M\text{ 不承载任何Einstein度量}.
\end{equation}
\end{theorem}
```
`\noindent`{=latex}*来源与状态：*完整证明在同目录 `\path`{=latex}，原上传位置与审读报告见[@Project; @CodexReview]。主证明不依赖(SC)，其能量规范、覆盖重数和族统一常数有既有实质审读支持；本文保留该状态，并把完整原稿而非摘要作为后续使用入口。证明成立与文献首创性是不同判断。

最接近的已核对外部基线是 LeBrun Corollary 3.4 的 $k\ge A/3$ 不存在性[@LeBrun2001]。新命题的增量是跨越 $X,k$ 变化仍不消失的正宽度，不是 $1/3$ 本身。经典逐个严格不等式 $k/A<1/3$ 并不排除 $k_i/A_i\uparrow1/3$；整数性在 $A_i\to\infty$ 时也不给统一宽度。首创性应围绕这一精确增量查新，不能从尚未查到同式就宣布全球首次。

这是指定无限流形族上的*全局*不存在性定理。证明使用局部极限不使其变成局部结论；但它仍不是 $P_4^-$，也不是对所有四维流形的存在性定理。

### 近临界序列的必要退化

```{=latex}
\begin{theorem}[进展包与审读报告中的配套结论]\label{thm:collapse}
在上述吹起族中，若 $M_i=X_i\#k_i\overline{\CP^2}$，
\[
\delta_i=\delta_-(g_i)\longrightarrow0,
\qquad d_i=\left(\frac13-\frac{k_i}{A_i}\right)_+\longrightarrow0,
\]
则对任意固定 $r,v>0$，
\begin{equation}\label{eq:measurecollapse}
\frac{\Vol_{g_i}\{p:\Vol_{g_i}B_r(p)\ge v\}}
{\Vol_{g_i}M_i}\longrightarrow0,
\qquad \diam(M_i,g_i)\longrightarrow\infty.
\end{equation}
有界直径版本为：$\delta_-\le1/4$、$\diam\le D$ 时，
\begin{equation}\label{eq:diambound}
\delta_-^2+\left(\frac13-\frac{k}{A}\right)_+\ge c(D)>0.
\end{equation}
\end{theorem}
```
`\noindent`{=latex}*来源与状态：*进展包第1、3节与Codex审读；A03第3--8步提供其临界族前身。变化拓扑时只能断言测度比例塌缩，不能擅自升级为 $\sup_p\operatorname{Vol}B_r(p)\to 0$。固定拓扑临界族的更强版本应保留其原始额外条件。

定理`\ref{thm:topgap}`{=latex}扩展"无Einstein"的拓扑范围；定理`\ref{thm:collapse}`{=latex}直接限制原题允许的近似输入。这两项互相关联，却不是彼此自动推出。尤其 $d_i\to0$ 是沿原 $1/3$ 边界的条件，不能把它照搬到新禁止带内部每个固定比值。

精确主定理的证明机制：必须保留的五个环节
----------------------------------------

### 统一平均能量，而非总量紧致性

假设存在 Einstein 度量。monopole条件排除非负 Einstein 常数后，归一化为 $\operatorname{Ric}=-g$。标量曲率估计和式`\eqref{eq:CGB}`{=latex}给出 $$\label{eq:budget}
 \operatorname{Vol}_gM\ge2\pi^2A,
 \qquad \mathop{\rlap{\,\raisebox{0.1ex}{\tiny$-$}}\int}\nolimits_M|\operatorname{Rm}_{\rm full}|^2\,d\mu_g
 \le16\frac{\chi(M)}A.$$ 这里允许 $\operatorname{Vol}M$、总曲率能量和直径全部无界。需要统一的是 $\chi/A$，而不是 $\chi$ 本身。

Codex检查的 Noether 输入为 $\chi(X)\le5A+36$。其数值可由 $A\ge2p_g-4$、$\chi(X)=12(1-q+p_g)-A$、$q\ge0$ 得到。再用*已有*的 Einstein 必要条件 $k\le A/3$ 及正整数 $A\ge1$， $$\frac{\chi(M)}A\le5+\frac{36}A+\frac13\le\frac{124}3<42.$$ 所以可统一取 $L=42$。这一步没有循环使用新 $\gamma$ 定理。若改为其他monopole流形族，首先要重新证明相应的 $\chi/A$ 界。

### 同时选择低能量与低平均缺陷的固定尺度中心

设 $H\ge0$，并令 $\mathcal A_rH(x)=\operatorname{Vol}(B_r(x))^{-1}\int_{B_r(x)}H$。在统一 Ricci 下界及固定有界尺度下，Bishop--Gromov局部倍增和Fubini给出 $$\label{eq:fubini}
 \int_M\mathcal A_rH(x)\,d\mu(x)\le C_{\rm BG}\int_MH\,d\mu.$$ 证明时用 $y\in B_r(x)$ 导致 $\operatorname{Vol}B_r(x)$ 与 $\operatorname{Vol}B_r(y)$ 在统一倍增常数内可比，再交换积分。无需绝对体积下界。

由Markov不等式，平均全曲率不超过固定倍数 $C_0$ 的中心占据固定正比例；对非负近等号密度也可同时选择局部均值很小的中心。将两个坏集比例各压到 $1/4$，交集仍有至少 $1/2$ 的体积比例。Ricci下界又给 $\operatorname{Vol}B_r\le V_{-1}(r)$，故选取仅依赖 $C_0$ 的小固定 $r$，可将局部*绝对* $L^2$ 能量压入下述正则性阈值。

这是 $r=r(L)>0$，不是依序列变化的 $r_i\to0$。保留原尺度使后续极限仍有非零Einstein常数，避免放大后只得到Ricci-flat而丢失局部矛盾。

### 允许塌缩的正则性究竟给了什么

Cheeger--Tian的四维精确Einstein小能量估计，经Ge--Jiang Theorem 1.1明确重述：$\operatorname{Ric}=\lambda g$、$|\lambda|\le3$，在 $r\le1$ 的球上 $\int|\operatorname{Rm}|^2\le\varepsilon$，则内球 $\sup|\operatorname{Rm}|\le Cr^{-2}$；$\varepsilon,C$ 不依赖球体积下界[@CT2006; @GJ2017]。范数换算只改变固定常数。

它给固定尺度曲率*有界*，并不说随着绝对能量趋零，塌缩球上的曲率必趋零。也不直接给底空间注入半径下界。接下来需要在足够小的无共轭半径内拉回度量，获得受控的局部展开片。

### 展开不必单射：小平均缺陷如何传输

```{=latex}
\begin{lemma}[缓冲局部等距映射的重数传输]\label{lem:transport}
设 $\pi:(\widetilde U,\widetilde g)\to(U,g)$ 是局部等距映射。给定中心及半径 $s$，假设需要的长度不超过 $2s$ 的路径均可从 $\widetilde B_s$ 内原像提升，且提升留在 $\widetilde B_{3s}\Subset\widetilde U$。对 $x,y\in B_s$，假设它们可由上述路径连接；记 $n_s(x)$ 为 $x$ 在 $\widetilde B_s$ 的原像数，并假设面积公式适用。则对 $F\ge0$，
\begin{equation}\label{eq:transport}
\fint_{\widetilde B_s}\pi^*F\le
\frac{\Vol(\widetilde B_{3s})}{\Vol(\widetilde B_s)}\fint_{B_s}F.
\end{equation}
\end{lemma}
```
```{=latex}
\begin{proof}
从 $x$ 的每个小球原像提升同一条 $x$ 到 $y$ 的路径。唯一提升及反向提升保证这些终点互异，故 $n_s(x)\le n_{3s}(y)$。对 $y\in B_s$ 积分，得到
\[
n_s(x)\Vol B_s\le\int_{B_s}n_{3s}(y)\,d\mu(y)\le\Vol\widetilde B_{3s}.
\]
于是 $\int_{\widetilde B_s}\pi^*F=\int_{B_s}F n_s\le(\Vol\widetilde B_{3s}/\Vol B_s)\int_{B_s}F$，除以 $\Vol\widetilde B_s$ 即得。实际指数展开中需另外检查定义域、缓冲及局部等距拉回；本证明没有假设全局单射或正规覆盖。
\end{proof}
```
`\noindent`{=latex}*来源与状态：*这是Codex所述重数机制的显式化。原稿中的球选择与缓冲条件仍应逐项对应；不能将本引理用于不具有路径提升空间的抽象多值参数化。

受控展开片上的体积比有统一界，故底空间的小*平均*密度能传到展开片。仅知道底空间绝对积分小则不够：$U\times S^1_\ell$ 的固定密度积分可随 $\ell\to0$ 消失，展开后密度却不变。

### 禁止的是开集Einstein模式，而不是单点代数数据

临界近等号迫使展开后的光滑极限具有 $$\label{eq:forbidden}
\operatorname{Ric}=-g,\quad s=-4,\quad
\operatorname{Spec}(W^+)=(-1/6,1/12,1/12).$$ 设简单本征形式为定长 $\omega$，常数谱给 $W^+=\mu\operatorname{Id}+(\lambda-\mu)P_\omega$。由 Einstein 条件 $\operatorname{div}W^+=0$，展开乘积法则后先与 $\omega$ 收缩得 $\operatorname{div}\omega=0$，再由非零自对偶二形式在四维的非退化性得 $\nabla\omega=0$。于是 $\nabla W^+=0$。这也与Derdziński Proposition 5一致[@Derdzinski]。

但式`\eqref{eq:forbidden}`{=latex}给 $|W^+|^2=1/24$、$\det W^+=-1/864$。代入 Einstein--Weyl 恒等式 $$\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$$ 要求 $|\nabla W^+|^2=1/16$，矛盾。等价地，局部Kähler--Einstein谱应为 $(-2/3,1/3,1/3)$。这个论证针对*开集上持续成立的*模式；它不排除某点的代数曲率恰好取同样数值。

把代数缺陷写完整：一组可直接复算的连接估计
------------------------------------------

这一节保留原续接稿的粗常数推导，并补上完整证明中的更强联合估计。必须修正一个材料间的误判：下文 $\Phi_*$、统一间隙原稿的 $\mathcal D$ 以及A01第67步的终端 $\Phi$，*逐项定义相同*。119与109、912与864来自估计的松紧，不是不同密度。不同流形范畴的monopole输入和拓扑余量仍须分别检查。

取适用LeBrun估计的monopole类 $a$，使 $(a^+)^2\ge A$。此处正投影范数不是类的拓扑自交数 $a^2=A-k$。令 $\omega=|W^+|$、$w=\lambda_{\min}(W^+)$， $$\begin{aligned}
 I&=\frac1{4\pi^2}\int_M(s^2/24+2\omega^2)\,d\mu_g,
 &J&=\frac1{8\pi^2}\int_M|E|^2\,d\mu_g,\\
 D_a&=I-\frac23(a^+)^2\ge0,
 &q&=k-A/3,\qquad d=(-q/A)_+.\end{aligned}$$ Chern--Weil 给 $I-J=A-k$，从而 $$\label{eq:Da}
D_a=J-q-\frac23\big((a^+)^2-A\big)\le J+Ad.$$ LeBrun Theorem 2.3及其证明式(11)分别支持 $$\begin{aligned}
\int(s-\sqrt6\omega)^2\,d\mu_g&\ge72\pi^2(a^+)^2,\\
\int\left(\frac23s+2w\right)_{-}^{\!2}\,d\mu_g&\ge32\pi^2(a^+)^2,\end{aligned}$$ 其中 $u_-=\min(u,0)$；全部monopole与极化假设必须同时成立[@LeBrun2001]。

逐点配方恒等式是 $$\label{eq:square}
27(s^2/24+2\omega^2)-(s-\sqrt6\omega)^2
=\frac18(s+8\sqrt6\omega)^2.$$ 因此 $\int(s+8\sqrt6\omega)^2\le864\pi^2D_a$。设 $$f=\tfrac23s-2\sqrt{2/3}\,\omega,\quad a_*=\tfrac23s+2w,
\quad\mathcal G=f^2-(a_{*,-})^2.$$ $w\ge-\sqrt{2/3}\omega$ 给 $a_*\ge f$，所以 $\mathcal G\ge0$；又 $\int f^2\le48\pi^2I$，故 $$\int\mathcal G\,d\mu_g\le48\pi^2D_a.$$ 令 $Q(g)=\int|\operatorname{Ric}+g|^2\,d\mu_g$，统一使用密度 $$\label{eq:Phistar}
\Phi_*:=|\operatorname{Ric}+g|^2+(s+4)^2+(s+8\sqrt6\omega)^2+\mathcal G.$$ 它正是原证明中的 $\mathcal D$。记 $P=\int|E|^2$、$Z=\int(s+4)^2$、$B=\int(s+8\sqrt6\omega)^2$，则 $Q=P+Z/4$。由逐点恒等式 $$\label{eq:joint-density-identity}
(s+8\sqrt6\omega)^2+18\mathcal G
=216(s^2/24+2\omega^2)-18(a_{*,-})^2$$ 及谱monopole估计可得，若 $T=2\chi+3\tau$， $$B+18\int\mathcal G\le108P+864\pi^2(T-2A/3).$$ 因此，在相同monopole输入下， $$\label{eq:109}
\boxed{\int\Phi_*\le109Q+864\pi^2(T-2A/3)_+.}$$ 对本节吹起族，$T=A-k$，右端即 $109Q+864\pi^2Ad$。若 $\delta_-\le1/4$，由 $Q/\operatorname{Vol}\le4\delta_-^2$ 和下述体积下界得到 $$\label{eq:436675}
\boxed{\mathop{\rlap{\,\raisebox{0.1ex}{\tiny$-$}}\int}\nolimits\Phi_*\le436\delta_-^2+432(1+\delta_-)^2d
\le436\delta_-^2+675d.}$$ 这里保留 $B+18\int\mathcal G$ 的联合预算，避免先分别估计再相加造成的常数损失。它与完整统一间隙证明一致，不增加新的假设。

原续接稿以及第67步采用的较粗推导同样有用： 因为 $\int(s+4)^2\le4Q$、$J\le Q/(8\pi^2)$，有 $$\label{eq:119}
\boxed{\int_M\Phi_*\,d\mu_g\le119Q+912\pi^2 A d.}$$ 特别是 $q\ge0$ 时恢复一个 $119Q$ 型终端重新校准界；精确 $\operatorname{Ric}=-g$ 时则只有 $912\pi^2Ad$。

若 $\delta_-\le1/4$，标量曲率monopole界给 $\operatorname{Vol}\ge2\pi^2A/(1+\delta_-)^2$。于是 $$\label{eq:meanPhi}
\mathop{\rlap{\,\raisebox{0.1ex}{\tiny$-$}}\int}\nolimits_M\Phi_*\le476\delta_-^2+456(1+\delta_-)^2d
\le713(\delta_-^2+d).$$ 零密度的光滑极限满足式`\eqref{eq:forbidden}`{=latex}：前两项给 $\operatorname{Ric}=-g$、$s=-4$，第三项给 $\omega=1/(2\sqrt6)$，最后一项迫使最小本征值达到迹零对称算子的极值，另外两个本征值相等。

这说明从小Ricci缺陷到小*平均校准缺陷*的代数环节已经可以明确写出。尚未解决的不是"再找一个平方恒等式"，而是在任意塌缩的近似方程上取得足以传递这个密度的正则区域。

从精确方程到近似方程：三个可竞争的证明方向
------------------------------------------

```{=latex}
\begin{target}[主攻联合间隙]\label{tar:joint}
在指定吹起族内，证明或严格否定存在统一 $c_*>0$，使所有度量在 $\delta_-\le1/4$ 时满足
\begin{equation}\label{eq:joint}
\delta_-^2+\left(\frac13-\frac{k}{A}\right)_+\ge c_*.
\end{equation}
不得额外默认有界直径、非塌缩或全曲率上确界。若只能得到带这些条件的版本，则准确记录它加强了哪个已有定理。
\end{target}
```
### 方向A：正体积比例的局部展开可达性

目标不必是"处处正则"，而是至少在一组固定正比例、局部平均 $\Phi_*$ 趋零的中心上，产生固定尺度受控展开。已知有界Ricci的尺度选择[@GJ2017 Theorem 3.4]可以把小绝对能量转成某个可比尺度上的小归一化能量，但不自动给点态曲率界。Naber--Zhang与Jiang--Kong--Xu需要额外的纤维化秩、模型或局部覆盖几何[@NZ; @JKX]。

真正要证明的是这些额外结构能否由*本问题的*小校准密度和能量预算获得；或者秩下降、不可展开区域是否必消耗固定正比例的校准缺陷。若构造出同时满足全部预算而不可展开的反模型，就限定这一方向，不重复把覆盖结构当成一般有界Ricci的免费结论。

### 方向B：弱测试张量与直接定量刚性

寻找不先要求全曲率点态界的估计：将 $\operatorname{Ric}+g$ 的导数通过分部积分移到受控测试张量上，用 $\mathcal G$、谱间隔和Hodge缺陷控制局部几何。$\left\lVert\operatorname{Ric}+g\right\rVert_\infty\to0$ 不控制 $\nabla\operatorname{Ric}$；不能把 Bianchi 恒等式写成点态 $\operatorname{div}W=O(\delta)$。

有价值的结果应是明确的"密度小则有一个禁止模式可被传递的片"定理，或者一个给定测试空间中的反例。使用有限 $W^{2,p}$ 强收敛往往足够传递二次曲率量，不必强求输入序列 $C^\infty$ 收敛。需要说明 $p$、规范、边界缓冲及系数紧性的实际来源。

### 方向C：有控制的局部平滑与终端重新校准

如果采用局部流，最小需求是得到一个定义在原闭流形上的终端度量，使正比例支撑区上曲率受控，并且 $Q(T)/A\to0$；再对终端度量重新应用式`\eqref{eq:119}`{=latex}或原稿对应密度。无需分别运输所有初始SW形式的缺陷。

但这一简化不解决流的共同存在时间、支撑过渡区域和退化系数问题。必须从实际初始数据证明，而不是因为权重代数通过检查就宣称流存在。若该接口的复杂性长期超过直接弱刚性路线，应保存有效引理后调整路线，而不是以"已经投入几十步"为理由继续同一闭合循环。

### 同等允许的反向结果

若在已由定理`\ref{thm:topgap}`{=latex}排除Einstein的拓扑上构造 $\delta_-\to0$，则得到真正负分支反例。构造应满足所有临界密度和能量约束；只展示一个塌缩局部模型或某种负Ricci度量不够。新禁止带内部的固定 $k/A<1/3$ 不受 $d\to0$ 的同一必要退化结论直接覆盖，可以重新检查，但不能因此预先认定那里容易构造。

### 一个足够完成矛盾、但不要求输入曲率处处有界的接口

```{=latex}
\begin{proposition}[受控谐和片上的密度传递准则]\label{prop:minimalbridge}
设假想序列满足 $\delta_-(g_i)^2+d_i\to0$。假设可选定固定半径的局部展开片及谐和坐标，将其识别到同一个欧氏球 $B_2$，使拉回度量 $\widetilde g_i$ 一致正定、具有统一 $C^{1,\alpha}$ 控制，且拉回的 $\Phi_*$ 在该球的平均值趋零。则这样的序列不可能存在。
\end{proposition}
```
```{=latex}
\begin{proof}
先取 $C^{1,\beta}$ 收敛子列，$\beta<\alpha$。谐和坐标中的Ricci方程主部为 $-\frac12 g^{ab}\partial_a\partial_b g_{jk}$，其余项只含度量的一阶导数。$\Ric_{\widetilde g_i}+\widetilde g_i\to0$ 一致成立，因此分布极限满足 $\Ric_{g_\infty}=-g_\infty$。内点椭圆估计先给任意有限 $p$ 的 $W^{2,p}$ 控制，随后极限的Einstein方程给光滑性。对差分方程再次应用统一椭圆估计，在更小球上得到强 $W^{2,p}$ 收敛；取 $p>4$ 即足够传递本文全部二次曲率密度。于是 $\Phi_*(g_\infty)=0$，得到被式\eqref{eq:forbidden}排除的Einstein开集。
\end{proof}
```
该命题的分析含义是：最终需要的是*一个小密度受控片*，不是把所有输入度量变成有界曲率。真正待证的是这样的片能否在任意塌缩序列中找到，以及底空间平均值能否传到同一片。它不与A02的尖峰构造矛盾，因为尖峰例并不满足本主线的趋零禁止谱密度。

必须保留的300步技术积累及其当前边界
-----------------------------------

### 旧IL连接和族与新吹起族不能混成一个范畴

旧研究还处理 $M=(\#_{j=1}^{m}X_j)\#N$，$m=2,3$，使用 $$A=\sum_j c_1^2(X_j),\qquad D=4m-(2\chi+3\tau)(N),\qquad
2\chi(M)+3\tau(M)=A-D.$$ 相应临界参数是 $D/A$，某些具体例子中 $D=k+4$ 或 $k+8$，不是一律 $k/A$。Bauer--Furuta给出全符号类的条件须从Ishida--LeBrun原文逐项恢复[@IL]。

临界近等号记录包括 $\operatorname{Vol}/A\to32\pi^2/9$、$\int|W^+|^2/(\pi^2A)\to4/27$、正负投影收敛及多形式空间相分离。这些是有用的几何约束。一般符号平均应写为实际投影范数的和；不能把 $(K_X^+)^2$ 无理由等同于 $A$。固定 $A$ 的绝对误差趋零与变化 $A_i$ 时的 $o(A_i)$ 必须区分。

### 选择支撑、加权Moser与共同时间

这些内容是可继续研究的*一种平滑方案*，不是定理`\ref{thm:topgap}`{=latex}的必经步骤。附录`\ref{app:flow}`{=latex}保留7倍半径缓冲、平方形式Sobolev常数、实指数权重、真实时间链、交错导数对和first-exit结构，使读者能接续具体分析，而非只读到"使用局部流"的标签。尚未闭合的是实际退化流的统一存在、延拓及所需极限接口，不能由有限阶代数检查替代。

### 终端几何与全局闭性

多个中心不能各自演化后被当成同一个终端闭度量。需要一个由不交支撑/着色构造的全局权重及一套共同流。Ricci流没有有限传播速度；区域远离初始坏点不足以使该区域自动不受影响。SW/Chern--Weil的终端应用要求同一闭流形与规范一致的度量，不能只在若干片上重新定义。

Prior-art审计：要回答的不是名称是否出现
---------------------------------------

```{=latex}
\begin{longtable}{L{.23\textwidth}L{.33\textwidth}L{.35\textwidth}}
\toprule 最近来源 & 已有内容 & 本项目需要确认的增量\\\midrule\endhead
LeBrun\cite{LeBrun2001} & $1/3$ 不存在性与SW曲率估计 & 指定无限族的统一 $\gamma$ 是否已有等价定理或直接推论；不把尖锐积分式等同于尖锐Einstein阈值。\\
Cheeger--Tian\cite{CT2006} & 精确4维Einstein、无体积下界的小能量正则性 & 与近饱和缺陷及展开重数传输组合后，是否产生此前未有的族一致结论。\\
Derdzi\'nski\cite{Derdzinski} & harmonic $W^+$ 的两本征值局部结构 & 禁止谱本身是经典机制；新增重点应在量化强迫和跨退化传递。\\
Ge--Jiang\cite{GJ2017} & 精确定理复述、有界Ricci尺度选择 & 不重新命名已有尺度选择；真正新增接口是近似方程下的正则/密度传递。\\
Anderson、Naber--Zhang\cite{Anderson1989,NZ} & 不同附加假设下的紧性与正则性 & 逐项核对附加条件，不能从题名推断可解决本题；核查既有推论是否覆盖统一间隙。\\\bottomrule
\end{longtable}
```
按定理相互蕴含关系查新：保持同一范畴、同一归一化、同一常数依赖；检索拓扑近饱和、monopole退化、局部密度、Einstein塌缩及最小体积文献的交叉，而不是仅搜索"uniform topology gap"。未获得全文的文章标为来源待核，不替它补写定理。

可独立推进的三个科研目标
------------------------

续接时以完整主原稿和最后有效修正为起点。式`\eqref{eq:109}`{=latex}--`\eqref{eq:436675}`{=latex}是与原稿对齐后的较强预算；式`\eqref{eq:119}`{=latex}--`\eqref{eq:meanPhi}`{=latex}保存早期粗推导，不必重复把它们当成密度冲突。研究可根据当前进展在以下目标之间选择，不要求每个会话按同一顺序执行。

若精确结果和必要退化完整且查新支持，第一种终点是完成一篇以*统一拓扑间隙及定量近等号退化*为核心的投稿稿。不能把第一稿的价值取决于尚未解决的式`\eqref{eq:joint}`{=latex}；也不为追求期刊名人为添上未经证明的广泛推广。

第二种终点是实质加强式`\eqref{eq:joint}`{=latex}：在三个竞争方向中选择一个最小分析接口，先证明真实输入上的统一版本，再推广范畴。可先获得覆盖可达的正比例定理、受控秩下降代价或保留密度的平滑定理；这些要明确说明排除了哪些先前仍开放的序列。

第三种终点是构造满足全部预算的逃逸模型，并与A03的全局拓扑机制拼接。模型失败时，只排除该模型，不宣布一般塌缩不存在。A02提供的曲率尖峰必须作为正则性压力测试保留，但它的底层本来有Einstein度量，不能误当此处的拓扑反例。

每次路线分叉用一条可判真的命题决定，而非预先耗满100步。论文整理、证明推进和新方向探索允许切换；切换应由证据触发，禁止重复宣布"只差一个标准技术步骤"而未展示该步骤。

跨会话接口与原稿定位
--------------------

A01持有本主线主定理与密度；A02持有近似构造和正则性反例；A03持有同一光滑拓扑的全局存在/不存在性。交接只需要准确的输入、输出、常数依赖与可用版本，不能传递"同伴已突破"的评价替代数学。

`\noindent`{=latex}**主原稿（本Skill原样保留）**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**原上传位置**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**共同入口与300步可追溯索引**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**累积研究稿**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**旧IL组装（逐模块核对状态）**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**终端重新校准**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**选支撑的独立模块**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**实指数缺陷Moser**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**共同bootstrap**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**局部禁止谱与退化**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**平均传输的修正版**`\quad`{=latex}`\path`{=latex}

统一间隙TeX原稿已收入本目录；其余路径指向现有用户工作区，不需要将所有程序和笔记重复复制进Skill。A03第31--60步的加权估计、选择支撑、正则化与延拓笔记保留为条件性技术储备；使用时以最后修正为准，不从早期"完成"标签倒推证明状态。后文附录保存可继续使用的分析接口，但它们不属于精确Einstein统一拓扑间隙的证明前提。

### 必须继承的纠错

纯 $W^+$ 独立下界的早期推导已撤回；不丢弃符号不利的梯度项，不把 $F_A^+$ 当成调和形式。compact Armstrong定理不直接用于非紧正则片。平均缺陷传输要保留重数。Noether比例界不等于全局体积界。正Ricci给体积上界，不给体积下界。旧的 $A^{-1/2}$ 界仅限制特定旧链，不能否定新精确统一间隙。Min-Oo旧论证的来源争议没有解决前，不把其存在性当作本主线依赖[@Ye1993]。

结果交付与论文标准
------------------

研究结论以具体命题和证明为单位，而不是以Agent数量、步数或平台认可次数为单位。同一公式在多个会话复算，可以提高证据质量，不产生多项独立新发现。

可完成的结果应及时冻结成可独立阅读的数学稿：准确的假设与量词，新增结论相对最接近文献的差别，所有分析接口及常数依赖，完整证明，必要时附有限计算及独立复算说明。假设增多或结论缩小必须在主定理中显式反映。无需等到整个Yau26解决才允许发表严谨的中间结果，也不把一个证明链拆成若干缺乏独立贡献的论文。

Annals、Inventiones、JAMS、Acta可以作为高质量写作与结果强度的目标，但任何文件都不预设已达到其录用标准。完整性、首创性、重要性和选刊是四项判断。用经典工具证明新的重要定理可以完全原创；出现一个新名称、搜不到同名词或构造了"框架"，并不能确认首创性。按*精确命题及假设*进行查新，并记录最近定理、包含关系及真正新增的证明步骤。

无论本轮选择论文收束还是进一步探索，结束时只需留下四类必要材料：更新后的主定理与证明；当前最小未闭合命题；确切被否定的模型及原因；可供同伴直接使用的来源、版本和计算。除非出现新的反证或新缺口，不再次从零争论已审读的同一结果。反过来，发现具体错误就修正所有依赖它的结论，而不是只新增一份不被后续读取的纠错说明。

```{=latex}
\appendix
```
可选平滑方案：保留技术细节与真实未闭合接口 {#app:flow}
------------------------------------------

本附录汇合A01第25--45、54--71步及归档06的有效内容。其用途是支持新证明，不是恢复已撤回的"全阶统一延拓已经完成"结论。精确Einstein间隙使用上一节的Cheeger--Tian路径，不依赖这里任何流动假设。

### 旧IL参数与终端重新校准

设旧IL范畴的拓扑参数为 $T=2\chi+3\tau=A-D$，$q=D-A/3$。第67步的终端密度与式`\eqref{eq:Phistar}`{=latex}相同；其 $119Q(T)$ 结论采用 $q\ge0$、适用的全符号monopole类和相应投影预算。若换为吹起族且 $k/A<1/3$，必须补上正的 $Ad$ 余量，不能直接沿用 $119Q$。在共同monopole假设下，式`\eqref{eq:109}`{=latex}还给较强的 $109Q$ 或 $109Q+864\pi^2Ad$。

这使终端策略相当具体：只要在原闭流形得到终端度量 $g(T)$，保持适用拓扑范畴，并证明 $Q(T)/A\to0$、正比例中心可受控展开，即可重新使用SW与Chern--Weil估计。无需沿流逐项搬运初始自旋子、Hodge投影和每个旧缺陷；但终端重算并不产生流本身。

### 流模块的统一变量：缺陷、加权曲率与截断jet分开

以下 $T$ 专指移位曲率张量，不再表示上一小节的拓扑数。采用后期一致规范 $$E_-=\operatorname{Ric}+g,\qquad T=\operatorname{Rm}-G,\qquad
G=\frac{g\mathbin{\bigcirc\mkern-15mu\wedge}g}{2(n-1)},\qquad \operatorname{Ric}(G)=-g.$$ 这是与相应曲率符号配套的定义，故 $\operatorname{Ric}(T)=E_-$。旧式 $T=\operatorname{Rm}+G_{\rm old}$ 仅在 $G_{\rm old}=-G$ 时等价。每个不交支撑内置 $a=\chi^2$，并定义 $$U=aT,\quad U_m=\nabla^mU,\quad T_m=\nabla^mT,\quad C_m=\nabla^m\chi.$$ 因此 $U_m$ 是*加权移位曲率*的导数，$C_m$ 是*截断函数*的协变导数；二者分别不是缺陷导数和曲率导数。$aE_-$ 是 $U$ 的Ricci缩并。这里的 $\nabla$ 是当前 $g(t)$ 的连接，固定背景连接将在延拓接口中另记 $\bar\nabla$。

### 固定尺度选点、着色与7倍半径缓冲

在假想IL临界序列中，设已有 $\operatorname{Vol}M\asymp A$、$\int|\operatorname{Rm}_{\rm full}|^2\le C A$ 及统一Ricci下界。对 $F=(1+|T_0|^2)^{1/2}$ 使用局部最大函数，阈值取 $\widetilde\gamma^2/r^4$。先选小 $\widetilde\gamma$，再选只依赖预算的小固定 $r$；弱型估计使坏中心体积不超过 $Cr^4A/\widetilde\gamma^2$。

用 $r$-网及有限着色选出不交的 $B_{7r}(p_j)$，保留内球体积总和至少 $\alpha A$。邻接度由Ricci下界的局部相对体积比较控制，例如比较半径 $29r$ 与 $r/2$，不需要绝对球体积下界。选择 $$\chi_j=1\text{ 于 }B_{5r},\quad\operatorname{supp}\chi_j\subset B_{6r},
\qquad \eta_j=1\text{ 于 }\operatorname{supp}\chi_j\text{ 的邻域},\quad
\operatorname{supp}\eta_j\subset B_{7r}.$$ 距离函数的Lipschitz截断可在预留缓冲内平滑；对固定光滑数据得到高阶导数有限，不等于这些高阶常数跨序列统一。设全局 $a=\sum_j\chi_j^2$，在相应支撑上有 $$a|d\eta_j|^2=0,\qquad da\cdot d\eta_j=0.$$ 外层缓冲的作用是让能量截断的导数不落入演化主系数活跃区；不能把 $\eta$ 与 $\chi$ 取成同一个截断而仍保留这些消去。

### Sobolev常数的正确量纲

本文用*平方形式*系数 $S$： $$\|u\|_4^2\le S\big(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\big),
\qquad S\le C r^2 V^{-1/2},\quad V=\operatorname{Vol}U.$$ 选择支撑上的初始 $H_2=\int\eta^2F^2$ 满足 $$H_2\le C(1+\widetilde\gamma^2/r^4)V,\qquad
S\sqrt{H_2}\le C(r^2+\widetilde\gamma).$$ 因此真正的小量是 $\gamma=S\sqrt{H_2}$，不是 $S^2\sqrt{H_2}$。塌缩体积在这个乘积中抵消，不能解释为全局无权Sobolev常数不依赖塌缩。该区分修复了早期记录的平方常数混用。

### 实指数缺陷能量与三因子吸收

设 $E_-=\operatorname{Ric}+g$、$s_\varepsilon=|E_-|^2+\varepsilon$。第71步修正后的实指数权重为 $$\begin{aligned}
J_{p,\varepsilon}&=\int\eta^2a^{p-2}s_\varepsilon^{p/2},
&z_p&=\eta a^{(p-1)/2}s_\varepsilon^{p/4},\\
D_{p,\varepsilon}&=\int\eta^2a^{p-1}s_\varepsilon^{p/2-1}|\nabla E_-|^2,
&Q_{p,\varepsilon}&=\int\eta^2a^{p-1}s_\varepsilon^{p/2-2}|\nabla s_\varepsilon|^2.\end{aligned}$$ 不能在所有 $p$ 中固定使用 $a^2$。曲率系数项通过三个因子分配：$aF^3$、$J_p$的被积量和 $z_p^4$，先用Hölder再用上述Sobolev式。令 $Y=\int\eta^2aF^3$，已整理的能量目标形如 $$J_p'+c_1pD_p+c_2p^2Q_p
\le Cp^N(1+r^{-2}+S^2Y)J_p.$$ 这避免要求固定初始小量对每个 $p$ 都满足 $\gamma<c/p$。曲率的低阶加权能量先给 $\int S^2Y\,dt\le C\gamma^3$；$S^2Y(t)\le C\gamma^3/t$ 只用于远离零时刻的区间，不能从 $0$ 积分 $1/t$ 后宣称得到了统一Gronwall界。

曲率模块中还保留精确配权关系 $$K_p=\int a^{p-2}\mathcal K^p,\qquad Z_p=a^{(p-1)/2}\mathcal K^{p/2},
\qquad K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}.$$ 最后一个式子来自Cauchy--Schwarz；$\|Z_p\|_3^3$ 与 $K_{3p/2}$ 的权重不同，不能相互替代。Kato正则化 $s_\varepsilon$ 与主系数正则化 $a\mapsto a+\varepsilon$ 也不同；后者会激活原本冻结的区域，需另外证明一致极限。

### 不能省略的Moser时间链与初始种子

第70--71步保留的时间安排为 $$p_k=6(3/2)^k,\qquad \tau_k=t(1-2^{-k-1}),\qquad
I_k=\int_{\tau_k}^{t}J_{p_k}(s)\,ds.$$ 先在 $[t/2,t]$ 取得真实初始种子 $I_0\le Ct\delta^6V$。空间Sobolev、时间截断和能量式联合产生 $$I_{k+1}\le Cp_k^N S(L_kI_k)^{3/2},\qquad
L_k\le Cp_k^N4^k/t.$$ 必须保留 $L_k^{3/2}$，不能在迭代中减成一次幂。若上述能量和时空极限步骤均在实际流上成立，迭代给 $$\|aE_-(t)\|_\infty\le C I_0^{1/6}S^{1/3}t^{-1/2}
\le C\delta(r^2/t)^{1/3}.$$ 它只在 $a=1$ 的平台转成无权缺陷界。端点结论仍需与实际流的时间连续性对应，不是仅写下形式递推便得到存在性。

### first-exit、交错导数与固定背景连接

若演化为 $\partial_tg=-2a(\operatorname{Ric}+g)$，设 $$\Gamma(t)=\sup_{s\le t}S(s)\sqrt{H_2(s)},\qquad
\mathcal V(t)=\int_0^t\|aE_-(s)\|_\infty ds.$$ 度量漂移给 $e^{-2\mathcal V}g(0)\le g(t)\le e^{2\mathcal V}g(0)$，粗Sobolev传输可用 $S(t)\le e^{8\mathcal V}S(0)$。典型能量闭合目标为 $$H_2(t)\le H_2(0)\exp\{C(1+r^{-2})t+C\mathcal V(t)\}.$$ 在假设的共同存在区间内，先选漂移门限 $\mathcal V_*$、再选 $T=\theta r^2$ 和初始 $\Gamma(0)\le\gamma_*/2$，使 $\Gamma$ 改善到 $3\gamma_*/4$；缺陷界给 $\mathcal V(T)\le C\delta\theta^{2/3}r^2$，从而改善到 $\mathcal V_*/2$。first-exit说明这些预算不会先触及门限，*不单独保证光滑解不会因尚未控制的高阶量终止*。

高阶账本需交错控制 $(U_m,C_{m+1})$，即加权曲率和截断jet。对 $a=\chi^2$，Leibniz展开给 $$\nabla^{m+2}a=2\chi C_{m+2}
+\sum_{j=1}^{m+1}c_{m,j}\,C_j*C_{m+2-j}.$$ 其中 $*$ 表示按原演化式所需的张量排列及缩并；求和中的单个截断导数阶数均不超过 $m+1$。关键反应项满足 $$a(\nabla^2a)*T=(\nabla^2a)*U.$$ 所以对该项作 $m$ 次微分时，最高截断jet以 $$2\chi C_{m+2}*U$$ 出现，而不是无权的 $C_{m+2}U$。保留 $\chi$ 因子才能与退化耗散配平；signed分部积分若打到 $\chi$，被积分转移的最高截断阶数降低一阶。其余乘积可能仍含 $U_m$ 或 $C_{m+1}$，不能一概称为已知低阶项。对应耦合项包括 $\int|C_{m+1}|^2|U_m|^{p-2}$，因此需要同指数的双能量估计，不能只估 $U_m$。

后期记录的基底依赖顺序为 $$U_0\in L^\infty,\quad T_0\in L^q
\ \Longrightarrow\ (U_1,C_2)
\ \Longrightarrow\ T_1
\ \Longrightarrow\ T_0\in L^\infty
\ \Longrightarrow\ m\ge2\text{ 的交错估计}.$$ 这是待用于实际流的分析模块顺序；每个箭头仍须满足原模块的支撑、规范和正时间条件。不得通过在 $a=0$ 附近除以 $a$，从 $U_m$ 直接获得 $T_m$。

连接必须相对固定背景 $\bar\nabla=\nabla^{g(\tau)}$，$\tau>0$。令 $\mathscr A=\nabla_{g(t)}-\bar\nabla$，对 $h=\partial_tg=-2aE_-$，精确变分式为 $$\partial_t\mathscr A^k{}_{ij}
=\tfrac12g^{k\ell}(\nabla_i h_{j\ell}+\nabla_j h_{i\ell}-\nabla_\ell h_{ij}).$$ 其结构是 $g^{-1}*\nabla(aE_-)$，*不是*漏掉权重的 $g^{-1}*\nabla E_-$。利用 $aE_-=\operatorname{Ric}(U)$ 及当前连接的度量相容性，原第55步模块要求的三角形式为 $$\partial_t\bar\nabla^m\mathscr A
=g^{-1}*U_{m+1}
+\mathcal P_m(\mathscr A,\ldots,\bar\nabla^{m-1}\mathscr A;
U_0,\ldots,U_m;g^{-1}).$$ 这里的低阶多项式应由具体张量式逐项检验，不能将尚未控制的当阶背景连接系数隐入它。对随时间移动的 $\nabla_g^m g=0$ 积分，不能获得固定坐标延拓。

规范也须一致。后期采用 $T_0=\operatorname{Rm}-G$，$G=g\mathbin{\bigcirc\mkern-15mu\wedge}g/[2(n-1)]$ 配合使 $\operatorname{Ric}(G)=-g$ 的曲率符号；旧 $T_0=\operatorname{Rm}+G_{\rm old}$ 只有在 $G_{\rm old}=-G$ 时相同。纯缩放演化会产生背景修正，不能假定 $T_0$ 齐次缩放。具体用前须保持算子/全张量范数及曲率符号成套一致。

剩余任务是实际退化系数下的局部起始定理、与所选规范兼容的唯一性及重启、需要的全阶一致界和正则化极限。归档中的有限阶检查可作为其输入，但截至最后撤回记录，不能称这些接口全部完成。研究也可以绕过此方案，直接寻找密度保留的弱正则片。

### 详细证明的对应位置与本附录覆盖范围

本附录已经写出共同变量、支撑结构、能量及时间递推和最高阶配权；没有逐字收录数百行支撑证明、全部张量分部积分或程序。需要接续具体证明时，直接读以下原章节，而非从摘要重新猜测：

-   `\path{Sessions/S0910A01/workspace/notes/step70_selected_support_lemma.md}`{=latex} 第2--3节给全曲率与体积预算，第4节最大函数，第5节相对packing与着色，第6节光滑缓冲和全局权重，第7.1--7.3节初始种子与Sobolev体积抵消。

-   `\path{Sessions/S0910A01/workspace/notes/step70_defect_moser_real_exponent.md}`{=latex} 第2节固定实指数权重，第3节三因子吸收，第4节 $J_6$ 种子，第5节真实时间链，第6节体积抵消；文件已包含第71步修正。它以其第1节的曲率分支估计作为输入。

-   `\path{Sessions/S0910A01/workspace/notes/step55_joint_bootstrap_background_continuation_repair.md}`{=latex} 第1.1--1.4节是first-exit，第2.1--2.4节是固定背景连接和每数据重启的条件性桥梁，第3节是终端展开片。旧曲率符号须按本附录对齐。

-   网页逐步归档06第6--10节保存 $\chi C_{m+2}U$、交错阶数、基底顺序、背景连接和主系数正则化的区别，原件为 `\path{Sessions/S0910A03/workspace/briefing/Yau26_第26题_完整逐步研究归档_2026-09-16/Yau26_full_research_archive_2026-09-16/06_详细推导_加权Moser_选择支撑_退化局部流.md}`{=latex}。

这些入口是研究资料的组成部分。现有TeX不声称已经内嵌全部计算文件，也不把原笔记曾使用的"完成"措辞凌驾于后来明确保留的存在和延拓缺口。

早期塌缩研究仍可使用的精确约化 {#app:reduction}
------------------------------

本节补回A01第9--14步留下的有效公式，不恢复其中已经撤回的全局可达性结论。所有约化都先假设真实的局部等距群作用或明确的齐次模型；一般有界Ricci塌缩序列并不自动满足这些假设。

### Nil三维纤维：正确符号、周期障碍与实际cusp

在固定Heisenberg标架 $[X_1,X_2]=X_3$ 上，考虑 $$g=dt^2+\sum_{i=1}^3 a_i(t)^2\sigma_i^2,\qquad
f_i=a_i'/a_i,\quad v=a_1a_2a_3,\quad
\mu=\frac{a_3^2}{2a_1^2a_2^2}.$$ 纤维内蕴Ricci的对角分量为 $(-\mu,-\mu,+\mu)$。因而 $\operatorname{Ric}_g=-g$ 的切向方程是 $$\begin{aligned}
f_1'+f_1(f_1+f_2+f_3)+\mu&=1,\\
f_2'+f_2(f_1+f_2+f_3)+\mu&=1,\\
f_3'+f_3(f_1+f_2+f_3)-\mu&=1.\end{aligned}$$ 法向方程为 $\sum_i(f_i'+f_i^2)=1$。令 $F_0=\sum_i f_i=v'/v$，三个切向式相加给 $F_0'+F_0^2+\mu=3$，最后一个式子给 $f_3'+F_0f_3=1+\mu$。因而 $$\boxed{v''=(3-\mu)v,}\qquad
\boxed{(vf_3)'=(1+\mu)v>0.}$$ 第一式不是旧稿误写的 $(3+\mu)v$，所以不能用它排除全部Nil塌缩。第二式只在 $v,f_3$ 为正则周期数据时直接给周期积分矛盾；不能把这一结论用于缺少相同边界条件的区间或奇异端。

实际精确Einstein区间模型为 $$a_1=a_2=e^{t/\sqrt6},\qquad
a_3=\sqrt{2/3}\,e^{2t/\sqrt6}.$$ 此时 $\mu=1/3$、$v''/v=8/3$，法向方程也满足。它明确显示cusp可与负Einstein方程相容。保留的是模型公式和周期障碍，不是"所有正规塌缩已经排除"。原纠正脚本中另写的最大原理捷径未在这里作为依赖；上述周期结论直接使用已列出的单调性恒等式。

`\noindent`{=latex}**Nil符号修正与cusp代入**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**撤回后的可达性范围**`\quad`{=latex}`\path`{=latex}

### 圆约化中消去的是纤维周期，不是重构困难

在自由等距圆作用的正则域写 $$g=q+\ell^2(d\psi+\mathcal A)^2.$$ 固定 $p$ 后取 $y=\ell(p)\psi$、$v=\ell/\ell(p)$、$\mathcal B=\ell(p)\mathcal A$，在展开纤维上 $$g=q+v^2(dy+\mathcal B)^2,\qquad v(p)=1.$$ 绝对塌缩量 $\ell(p)$ 从局部系数消失，只留在周期 $2\pi\ell(p)$ 中。这个归一化本身不提供 $v$ 在固定球上的统一上下界，也不保证该纤维能在所需缓冲域内展开。

令 $F=d\mathcal A$、$u=d\log\ell$、$Z=\ell F$、$z=*_{q}Z$、$H=\ell^{-1}\operatorname{Hess}_q\ell=\nabla u+u\otimes u$，其中 $|z|^2=\sum_{a<b}Z_{ab}^2$。对于精确方程 $\operatorname{Ric}_g=-\kappa g$，保持同一取向和标架规范后，保留的约化式为 $$\begin{aligned}
\operatorname{tr}_q H&=\kappa+\tfrac12|z|^2,
&dz&=-2u\wedge z,&\operatorname{div}_qz&=\langle u,z\rangle,\\
\operatorname{Ric}^q_{ab}&=-\kappa q_{ab}+H_{ab}
+\tfrac12\sum_cZ_{ac}Z_{bc}.\end{aligned}$$ 尤其不能把四维Ricci控制改写成普通基底Ricci的双边界，因为右端的 $H$ 和twist项尚未受控。

以单位竖直向量 $V$ 识别自对偶与反自对偶三维空间，电Weyl块给 $$H=\frac{\kappa}{3}I+\frac14(|z|^2I-z\otimes z)
-\frac12(W^++W^-).$$ 因此校准 $W^+$ 并不控制 $H$ 的符号；$W^-$ 可以改变其最小特征值。进一步设 $$\alpha_+=u-z/2,\qquad \alpha_-=u+z/2.$$ 原记录中的手性分解可写为 $$\begin{aligned}
W^\pm&=-[\operatorname{sym}\nabla\alpha_\pm+
\alpha_\pm\otimes\alpha_\pm]_0,\\
d\alpha_+&=\alpha_+\wedge\alpha_-,\qquad
d\alpha_-=-\alpha_+\wedge\alpha_-.\end{aligned}$$ 下标0表示无迹部分，取向反转交换正负标签。它说明大的 $u,z$ 可能在一个手性组合中抵消、在另一个中保留；单独控制twist振幅不能替代控制其导数或基底几何。

其中微分关系直接来自 $du=0$ 和 $dz=-2u\wedge z$。二次张量的平均满足 $$\frac12\sum_{\pm}
(\operatorname{sym}\nabla\alpha_\pm+\alpha_\pm\otimes\alpha_\pm)
=H+\tfrac14z\otimes z;$$ 用 $\operatorname{tr}H=\kappa+|z|^2/2$ 取无迹部分，恰恢复上式中的 $(W^++W^-)/2$。这同时固定了twist二次项的四分之一因子。

无twist时 $\operatorname{Spec}(W^+)=\{\kappa/3-\eta_i\}$，$\eta_i$ 为 $H$ 的特征值。取局部 $\mathbb H^2\times\mathbb H^2$ 的一个极坐标圆作用，$\kappa=1$、$\operatorname{Spec}(H)=(1,0,0)$，从而 $\operatorname{Spec}(W^+)=(-2/3,1/3,1/3)$；这反驳"静态常谱必为零"的过强推断。实际禁止谱仍须使用正文的Einstein开集刚性。

本节只保留精确对称域中的公式。推广到近Einstein度量需要写出相应误差及其范数；推广到一般塌缩需要真实的局部作用、覆盖或极限结构。两者均不能由一个相容的点态jet推出。

`\noindent`{=latex}**归一化变量与约化账本（须读顶部修正）**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**可达性撤回与有效Hessian关系**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**同一规范的完整手性公式与反例**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**手性恒等式计算**`\quad`{=latex}`\path`{=latex}

第一轮100步的研究脉络与纠错继承 {#app:100steps}
-------------------------------

下面是对S0910A01全部100条canonical记录的主题扫描，保留数学发展与最后修正的先后关系；逐步来源索引见同目录 `\path{20260916.tex}`{=latex}。编号指历史位置，不是未来研究命令。早期记录中的"完成""突破"须与后期反例和撤回一起阅读。

```{=latex}
\begin{longtable}{L{.12\textwidth}L{.79\textwidth}}
\toprule 步段 & 形成的内容、修正与可继续使用的入口\\\midrule\endhead
1--4 & 原题符号量词、SW与曲率预算；Min--Oo公式OCR校正。纯 $W^+$ 独立下界及过强的无条件优化推论撤回，保留LeBrun谱不等式和完成平方。\\
5--8 & 临界密度与禁止 $W^+$ 常谱；从固定拓扑绝对误差改为变化拓扑的 $o(A)$。局部极限不能直接套紧致Armstrong结论；改用Derdzi\'nski开集结构。小 $C^0$ Ricci误差不直接给Schauder高阶界。\\
9--14 & 覆盖平均传输、Noether平均能量、nil3/圆纤维约化和局部展开路线。nil3符号修正后，不能保留“所有正规塌缩都排除”的总括判断；最大幂零秩与可展开性仍是额外输入。秩一KK公式中的 $W^-$ 项可改变Hessian符号，局部 $\mathbb H^2\times\mathbb H^2$ 模型使过强凸性推断失效。\\
15--24 & 从全中心局部平滑转向好中心、缓冲和选择支撑。Whitney覆盖总量估计、把全网当好点集以及有限传播式直觉先后修正。只有有证明的相对体积选点继续保留。\\
25--35 & 张量演化账本、三因子Moser、终端119Q、平方Sobolev系数、初始 $p=6$ 种子及Hessian分部积分。第29步的半幂配权缺口由第30步Cauchy--Schwarz结构修正；第32--34步校正常数与零时刻积分。\\
36--45 & transported DeTurck、交错导数与条件性IL组装。早期以除以退化系数闭合的步骤被撤回；后续重复“流已闭合”的标签不能覆盖最终保留的起始、延拓及极限缺口。\\
46--48 & 将IL族与所有无Einstein拓扑分开；恢复双曲 $X\#X$ 的度二映射、BCG与Euler预算路线。固定拓扑Ricci缺陷下界可随复杂度衰减，不自动给维数一致间隙；图流形体积饱和也不自动矛盾。\\
49--53 & BCGP六节点 $\mathbb Z_4^2$ 商的全局 $\mathbb Q$-Gorenstein 平滑及同一光滑流形上的负KE存在链；局部EH核不等于全局平滑。反射层、表示特征标和Lee--Park输入共同作用；其余表格项有非零障碍空间不等于不存在平滑。详见下节。\\
54--60 & 共同bootstrap、first-exit、固定背景连接及加权曲率/截断jet交错对 $(U_m,C_{m+1})$。修正原始度量差唯一性中的规范问题和把当阶项算作低阶的循环；这些是平滑方法的条件性部件。\\
61--65 & 三因子端点、规范化曲率张量符号和纯缩放检验。第63--64步校正 $T_0$ 的定义及背景演化项；每数据的光滑起始不等于退化序列的统一全阶寿命。\\
66--71 & 吸收20260912累积稿，恢复第67步终端校准、第68步模块组装、第69--70步7r支撑与种子；第71步将缺陷权重改为 $a^{p-2}$ 并保留真实时间递推。\\
72--74 & 图流形连接器和加权shear预算。各向同性tanh腰部失败不排除所有连接器；$T^3$ 上反向翘曲再作Yamabe修正可构造特定负标量曲率中心，但不等于小Ricci缺陷连接器。\\
75--80 & 正曲率产品轨形的精确解消实验；逆对数误差不能强迫所有高阶障碍消失。第76步“全核为零”由第77步四个标量零模纠正；A/J对称减少投影但不消灭整个核。$O(t^{5/2})$ 余项不够控制 $t^3$ 主项。\\
81--84 & L交换修正径向缩放为 $F_i=t_i\sum_jB_{ij}t_j^2+R_i$。Ozuch必要条件不是充分存在性定理；已知del Pezzo KE例须匹配同一规范。局部角Gram均值 $8/3$ 不是全局Green响应系数。\\
85--89 & 明确源--传播--接收 $c_{ij}=L_iG_P^\perp S_j$。第86步从零模正交推出全部相互作用消失被第87步遗漏的Killing--Killing混合模否定；轴向源可保留。第89步区分Hessian与二次系数，撤回全TT算子正性及去掉奇异对角项仍保正的推断。\\
90--94 & K反射消去交叉奇偶块，限定到线性背景问题；恢复双曲连接和旧结果并修正Ricci-box三倍因子。第93步AA/BB各自发散的结论由第94步磁型张量归一化修正撤回，不可把它当不可行性定理。\\
95--97 & 产品曲率为 $R^\pm=\operatorname{diag}(\Lambda,0,0)$，不是 $(\Lambda/3)I$；奇接收器规范不变不等于完整Ozuch障碍。物理源在正秩一锥 $M_j=t_j^2u_ju_j^T$ 内，混合23/32项需先对称化；节点标架依赖不可忽略。\\
98--100 & 计算全部手性响应后，第99步撤回“完整首阶几何障碍”说法；第100步把AA/BB已实现节点间谱模型中的 $B_{++}=B_{--}=0$ 变成代数证明。AB结构、对角自作用、形变、正交补及同阶余项尚未整体闭合；局部解消障碍不排除底层所有Einstein度量。\\\bottomrule
\end{longtable}
```
不可丢失的存在性支线与累积稿数学资源
------------------------------------

### 六节点商面的全局平滑：一条具体的正向存在链

A01第49--53步不是统一拓扑间隙证明的一部分，但它提供了同样重要的研究方向：对已有近Einstein输入的对象，寻找真正Einstein度量，而非预设所有对象都应成为反例。

具体实验为BCGP表中的 $G=\mathbb Z_4^2$ 商，两个属3曲线的生成向量为 $$((1,3),(1,0),(2,1)),\qquad ((3,2),(0,1),(1,1)).$$ 商面有六个 $A_1$ 点；其极小解消 $S$ 满足 $K^2=2$、$p_g=q=0$、$\pi_1(S)=\mathbb Z_2^3$，因此 $b_+=1$，不属于旧 $m=2,3$ 的IL连接和范畴。第51步记录的存在性论证分为：

1.  对 $Y=C_1\times C_2$、在余维一自由的有限商 $\pi:Y\to X$，确认反射切层 $T_X^0=(\pi_*T_Y)^G$；这里的反射性及深度条件是证明内容，不能从局部平滑自动推出。

2.  由有限映射、Reynolds投影及Serre对偶，将 $H^2(T_X^0)^*$ 化为 $$\big[H^0(2K_{C_1})\otimes H^0(K_{C_2})\big]^G
    \oplus\big[H^0(K_{C_1})\otimes H^0(2K_{C_2})\big]^G.$$

3.  特征标计算给两项均零，具体标为 $$\begin{aligned}
    H^0(K_{C_1}) &: (2,3),(3,0),(3,1),\\
    H^0(K_{C_2}) &: (0,3),(1,2),(3,3),\\
    H^0(2K_{C_1}) &: (0,2),(1,0),(1,3),(2,0),(2,1),(2,2),\\
    H^0(2K_{C_2}) &: (0,1),(0,2),(1,1),(2,0),(2,2),(3,2).
    \end{aligned}$$ 在同一表示约定下检查配对不变量。

4.  应用相应局部--全局 $\mathbb Q$-Gorenstein 平滑定理。$K_X$ 的充足性由有限拉回的产品典范丛得到，不能仅由 $K^2>0$ 推出；平滑小纤维上充足性开放，故由Aubin--Yau得到负KE度量。

5.  对ADE点使用有限基变换后的同时解消及Ehresmann，核对光滑纤维与给定极小解消的微分同胚类型，从而结论落在同一个光滑流形上。

上述为现有内部证明链及计算内容，不将其包装成已经完成外部首创性认证的新定理。仅由基本群相同不能把不同Campedelli构造认成同一平滑分支；第50步专门保留了这一区别。第52--53步的其他产品商表格项常有非零 $H^2(T_X^0)$，这只阻止直接使用同一个无障碍充分条件，不能推出平滑不存在，更不能推出Einstein不存在。

`\noindent`{=latex}**全局平滑证据与Campedelli区分**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**反射层、特征标与存在性证明**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**表格扫描及Lefschetz计算**`\quad`{=latex}`\path`{=latex}

### 可复用的Lefschetz方法与实际20项扫描

上述六节点实例之外，第52步采用全纯Lefschetz公式，避免把 $H^0(2K)=\operatorname{Sym}^2H^0(K)$ 的特殊捷径误用于超椭圆曲线，也不要求先分解非阿贝尔群的全部不可约表示。

对属 $g\ge2$ 曲线 $C$ 的非恒等自同构 $u$，令 $\lambda_p$ 为固定点 $p$ 的切向乘子。在两条曲线上使用相同拉回约定，则 $$\begin{aligned}
\chi_{1,C}(u)&:=\operatorname{tr}(u\mid H^0(K_C))
=1+\sum_{p\in\operatorname{Fix}(u)}\frac{\lambda_p}{1-\lambda_p},\\
\chi_{2,C}(u)&:=\operatorname{tr}(u\mid H^0(2K_C))
=\sum_{p\in\operatorname{Fix}(u)}\frac{\lambda_p^2}{1-\lambda_p}.\end{aligned}$$ 第一式的1来自 $H^1(K_C)\cong H^0(\mathcal O_C)^*$；第二式使用 $H^1(2K_C)=0$。在恒等元处另取 $\chi_{1,C}(1)=g$、$\chi_{2,C}(1)=3g-3$，不代入固定点分母公式。

对分支生成元 $e_i$、稳定子 $H_i=\langle e_i\rangle$，陪集 $aH_i$ 对 $u$ 贡献固定点当且仅当 $a^{-1}ua=e_i^k\ne1$；局部乘子由 $k/|e_i|$ 给定。若统一反转指数约定，两条曲线的特征标同时对偶，不变量维数不变。需要的障碍对偶维数是群平均 $$\begin{aligned}
d_{21}&=\frac1{|G|}\sum_{u\in G}\chi_{2,C_1}(u)\chi_{1,C_2}(u),\\
d_{12}&=\frac1{|G|}\sum_{u\in G}\chi_{1,C_1}(u)\chi_{2,C_2}(u),\qquad
d=d_{21}+d_{12}.\end{aligned}$$ 原程序同时检查群阶、分支阶数、生成性、源文献的左乘关系、Riemann--Hurwitz属数、商曲线 $H^0(K)^G=0$、两种乘子约定和最终近整数值。这些一致性检查有实际作用，但不能把浮点字符平均自动改称精确证明。

下表逐项取自实际JSON的20个 `results`，按源文献节号排序。属数按该节展示的两套分支数据排列，部分行与原总表的曲线顺序相反。未扫描的其他 $K^2=2$ 行不在表中。

  源节号    $K^2$  $G$                                  $(g_1,g_2)$    $d_{21}$   $d_{12}$   $d$
  -------- ------- ----------------------------------- ------------- ---------- ---------- -----
  6.7         2    $\mathbb Z_4^2$                        $(3,3)$             0          0     0
  6.9         4    $\mathfrak S_5$                       $(4,21)$             1          1     2
  6.10        4    $\mathfrak A_5$                       $(11,4)$             2          1     3
  6.11        4    $\mathfrak S_4\times\mathbb Z_2$      $(13,3)$             2          1     3
  6.12        4    $\mathfrak S_4\times\mathbb Z_2$      $(13,3)$             3          1     4
  6.13        4    $\mathbb Z_2^4\rtimes\mathbb Z_2$      $(5,5)$             2          2     4
  6.14        4    $\mathfrak S_4$                        $(7,3)$             3          1     4
  6.15        4    $\mathfrak S_3\times\mathbb Z_3$       $(4,4)$             2          1     3
  6.16        4    $\mathbb Z_3^2\rtimes\mathbb Z_2$      $(4,4)$             2          2     4
  6.17        4    $D_4\times\mathbb Z_2$                 $(5,3)$             3          2     5
  6.18        4    $\mathbb Z_4\times\mathbb Z_2$         $(3,3)$             2          2     4
  6.19        4    $\mathbb Z_2^3$                        $(3,3)$             3          3     6
  6.20        6    $\mathfrak A_6$                       $(19,16)$            2          2     4
  6.21        6    $\mathfrak A_6$                       $(19,16)$            2          2     4
  6.22        6    $\mathfrak S_5\times\mathbb Z_2$      $(11,19)$            2          2     4
  6.23        6    $\operatorname{PSL}(2,7)$             $(19,8)$             2          2     4
  6.24        6    $\operatorname{PSL}(2,7)$             $(19,8)$             2          2     4
  6.25        6    $\mathfrak A_5$                       $(16,4)$             3          2     5
  6.26        6    $\mathfrak S_4\times\mathbb Z_2$      $(19,3)$             4          2     6
  6.27        6    $D_4\times\mathbb Z_2$                 $(7,3)$             4          3     7

第6.7行还由前述显式特征标独立确认。第6.9行在第53步进一步于 $\mathbb Q(\zeta_{60})$ 中精确复算，得到 $d_{21}=d_{12}=1$；240个候选点对分成4个大小60的节点轨道。因此该行的局部--全局边界映射形如 $$\beta:\mathbb C^4\longrightarrow H^2(X,T_X^0),\qquad
\dim H^2(X,T_X^0)=2,\quad \dim\ker\beta\ge2.$$ 这个维数界不保证核中有四个坐标同时非零的向量。真正需要的是具体边界映射，或对偶的残数/评价映射；还须处理高阶提升。源分支表示把4节点分成两对，不能仅凭取商前的甲板群宣称商上节点具有传递对称性。

表中其余非零维数目前按原数值扫描等级保留，不统一升级成精确分圆域证书。更重要的是，$d>0$ 只表示 $H^2(T_X^0)=0$ 这个充分条件不适用；它不证明所有节点不能同时平滑，不证明其他复结构不存在，也不排除任何非Kähler Einstein度量。这20项不是整个BCGP表的分类结论。

`\noindent`{=latex}**20项计算方法及回归检查**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**20项原始数值、属数及分支检查**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**6.9行精确分圆域与节点轨道计算**`\quad`{=latex}`\path`{=latex}

`\noindent`{=latex}**6.9行精确结果和边界映射范围**`\quad`{=latex}`\path`{=latex}

本节已保存方法、全部已扫描行和第53步的精确输出，但未嵌入完整有限群枚举代码。六节点存在链中反射层延拓的完整论证见第51步原笔记第2节，上同调比较见第3节，Serre/Künneth计算见第4节，全局平滑、充足性及微分同胚桥梁分别见第5--7节。这样保留的是可继续计算的数学对象，而非一个"已检查20例"的计数。

### 20260910与20260912：原有证明和限制继续可读

这两份原始TeX保留全文。本文件不以专题摘要取代其中推导；以下说明哪些材料可直接改变下一步研究判断。

-   `\path{20260910.tex}`{=latex} 保存原题符号分支、四维Hitchin--Thorpe兼容性、LeBrun与IL范畴、精确/近似方程差别、正负分支及不同维数的候选。它是开放研究地图，不规定证明优于反例，亦不规定必须用流。

-   `\path{20260912.tex}`{=latex} 第一章保存严格Hitchin--Thorpe预算、复/辛四维正分支的经典存在性归约、SW可显式化的夹逼障碍、有限覆盖与熵路线、固定拓扑和变化拓扑必要退化的区别。附加全曲率、直径、非塌缩或Bach-flat条件的结论须带原假设使用。

-   第五章集中研究具体有理吹降 $W_{4,1}$：$\chi=47$、$\tau=-31$、$b_+=7$、$K^2=1$。其中精确负Einstein、体积接近 $2\pi^2$ 与直径有界是*专门的联合假设*；体积亏损 $d=\operatorname{Vol}-2\pi^2$ 不是 $\delta_-$。不能把这一精确序列与一般近Einstein序列混用。

-   第五章的SW饱和恒等式、四项缺陷分解、闭校准形式 $\Omega=(1+q)\omega-b\wedge c$、Hodge修正和半Weyl估计，为把积分近等号升级为几何结构提供工具。单个正类的控制不等于整个Hodge正平面的控制；半Weyl一阶闭合不自动延伸到全部高阶。

-   其极限中出现的 $H^0(\Omega^1\otimes K)$ 全纯截面、低Dirac谱隙、Dolbeault/Kuranishi框架、Lorentz空间与气泡树、Green--Jacobi外部项、双典范残数和局部KE通量，均保留适用对象及尺度。形式变形、真正可积变形和 $\mathbb Q$-Gorenstein 平滑是不同接口。

-   第五章末的条件性体积--直径间隙仍需分类所有可能极限，并证明相应有限点评价映射的单射性；没有完成这两项就不能称无条件结论。既有五次曲面KE退化例表明，固定拓扑和SW饱和本身并不控制直径。

这些资源允许产生正向存在、统一刚性、定量退化或反例构造等不同结果。只有当新估计确实对应同一对象和同一量词时才组合它们；若产生新的表示、全局控制或构造机制，可以接入现有主线，也可以成为独立路线。

```{=latex}
\begin{thebibliography}{99}
\bibitem{Yau1982} S.-T. Yau, \emph{Problem Section}, in \emph{Seminar on Differential Geometry}, Annals of Mathematics Studies 102, Princeton University Press, 1982, pp. 669--706. 历史题页仍需在工作区逐字核对；本稿采用任务书中的区间命题。

\bibitem{LeBrun2001} C. LeBrun, \emph{Ricci curvature, minimal volumes, and Seiberg--Witten theory}, Invent. Math. 145 (2001), 279--316. \url{https://arxiv.org/abs/math/0003068}. 原稿采用 Theorem 2.3 的证明及式(11)、Proposition 3.1--3.2、Corollary 3.4；不把 $1/3$ 说成已证明最优的 Einstein 拓扑阈值。

\bibitem{CT2006} J. Cheeger and G. Tian, \emph{Curvature and injectivity radius estimates for Einstein 4-manifolds}, J. Amer. Math. Soc. 19 (2006), 487--525. DOI: \url{https://doi.org/10.1090/S0894-0347-05-00511-4}. 本稿所用精确 Einstein 小能量版本同时由 Ge--Jiang Theorem 1.1 核对。

\bibitem{GJ2017} H. Ge and W. Jiang, \emph{$\epsilon$-regularity for shrinking Ricci solitons and Ricci flows}, arXiv:1707.05511. \url{https://arxiv.org/abs/1707.05511}. 原稿采用 Theorem 1.1、Theorem 3.4；后者为有界 Ricci 的尺度选择，不是一般有界 Ricci 的点态曲率结论。

\bibitem{Derdzinski} A. Derdzi\'nski, \emph{Self-dual K\"ahler manifolds and Einstein manifolds of dimension four}, Compositio Math. 49 (1983), 405--433, Proposition 5. \url{https://www.numdam.org/item/CM_1983__49_3_405_0/}. 局部两本征值与恒模长结构；本稿另给出对应一阶投影证明。

\bibitem{CN} J. Cheeger and A. Naber, \emph{Regularity of Einstein manifolds and the codimension 4 conjecture}, arXiv:1406.6534. \url{https://arxiv.org/abs/1406.6534}. 引用须区分有界 Ricci 的非塌缩正则片与精确 Einstein 的更强正则性。

\bibitem{NZ} A. Naber and R. Zhang, \emph{Topology and $\epsilon$-regularity theorems on collapsed manifolds with Ricci curvature bounds}, Geom. Topol. 20 (2016), 2575--2664. \url{https://doi.org/10.2140/gt.2016.20.2575}. 最大纤维化幂零秩、模型几何等输入不能省去；本稿不宣称这些输入已由夹逼推出。

\bibitem{JKX} W. Jiang, L. Kong and S. Xu, \emph{Convergence of Ricci-limit spaces under bounded Ricci curvature and local covering geometry I}, arXiv:2205.00373. \url{https://arxiv.org/abs/2205.00373}. local covering geometry 是额外结构；具体使用前核对版本与定理。

\bibitem{Anderson1989} M. T. Anderson, \emph{Ricci curvature bounds and Einstein metrics on compact manifolds}, J. Amer. Math. Soc. 2 (1989), 455--490. \url{https://doi.org/10.1090/S0894-0347-1989-0999661-1}. 原续接稿仅记录文献身份，所需 Corollary B(4) 全文当时未取得；本次整合未额外完成该文献核查，不据二手概述填写其假设或用它排除输入曲率尖峰。

\bibitem{Ye1993} R. Ye, \emph{Ricci flow, Einstein metrics and space forms}, Trans. Amer. Math. Soc. 338 (1993), 871--896. \url{https://doi.org/10.1090/S0002-9947-1993-1108615-3}. 项目记录提示其对 Min-Oo 投影论证的修正；本稿不据尚未核准的旧存在性陈述建立结论。

\bibitem{IL} M. Ishida and C. LeBrun, \emph{Spin manifolds, Einstein metrics, and differential topology}, arXiv:math/0107111. \url{https://arxiv.org/abs/math/0107111}. Proposition 4 与 Theorem 7 为旧 IL 连接和路线来源；实际应用前逐项核对 Bauer--Furuta/模4等原始假设，不能只保留拓扑比值。

\bibitem{Project} Qiushi Engine 项目资料：2026-09-15进展包、2026-09-16逐步归档，S0910A01/A02/A03各100步 meta-trace；源文件名与本地工作区定位见正文。原稿、脚本与摘要须分别识别，不能把记录中的成功标签视作外部定理。

\bibitem{CodexReview} 用户提供的原稿审读记录（截至2026-09-16），对应 \path{Sessions/S0910A03/workspace/briefing/Yau26_uniform_gap.tex}；完整TeX现同时保存为同目录 \path{20260916_uniform_gap.tex}。既有审读结论为其所检查依赖链中未发现实质缺口，且精确拓扑间隙不依赖(SC)。本引用不代替原证明，也不表示文献首创性已完成认证。

\end{thebibliography}
```
