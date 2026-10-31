# O10 原缺陷到实际误差的幂次转接：独立审读与补全

2026-09-30。本文仅审核新附件第5节并补足其关键测试；不重新证明 R1、单解参数理论或第五线丛 Cartan 恒等式，也不宣称无密度 O10 已解决。

## 1. 审读结论

新附件 `O10_Quantitative_Escape_and_O11_Boundary(1).md` 第5.1—5.3节的幂次可以从所引定量前置推出。第5.4节省写的固定高幅度测试可补成严格能量证明，因此不是必须废弃的路线。此外，C轮直接 resolvent 也提供独立替代。

须区分两份文件中的误差：

- 原始量 \(x=\kappa_\beta+\beta^{-2}\)；
- D轮 `O10_Alternative_Global.md` 的实际误差总和 \(\mathfrak e_D\)，包括辅助截面与实际扭率的 \(H^1\) **及 \(L^4\)** 差。

若 R1 的固定慢梯度指数为 \(0<\epsilon_0\le1\)，令
\[
\gamma=\frac{\epsilon_0}{1+\epsilon_0}\le\frac12.
\]
可以取
\[
\boxed{\mathfrak e_D\le C x^{\gamma/16}.}\tag{A}
\]
常数不依赖 \(b=\fint|W^-|^2\)。最后的 \(1/16\) 包含了 \(L^4\) 转移的插值损失，不是只检查新附件较短误差清单后直接套用。

若同时采纳 D 轮已陈述的第五线丛排除，则得到条件性转接
\[
\boxed{x\ge c(1+b)^{-24/\gamma}.}\tag{B}
\]
它比新附件的指数下界强，但依然允许更快的 \(b\) 增长。本文不将(B)称为无条件端点闭合。其第五线丛前置应由相应审读单独确认。

## 2. 核对的准确原始来源

本次实际读取：

1. 新附件第5节及第2节误差定义；
2. C轮 `O10_Strong_Current_Prerequisite.md` 全文，特别式(12)—(23)；
3. C轮 `O10_Direct_Resolvent_Prerequisite.md`；
4. 原整合稿 `upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex` 中 `sec:endpoint-covariance` 式1.2—1.3、`sec:mixed-current` 式2.2—2.3及3.1—3.3、`sec:torsion-prolongation` 的实际分量定义；
5. D轮 `O10_Alternative_Global.md` 的完整误差清单和排除条件。

以下所有范数均相对于 \(dV/V\)。区分实际扭率质量 \(m=|\tau|^2\) 与辅助质量 \(a=|v|^2\)。固定
\[
\rho_*=4/3,\qquad m_*=128/81,\qquad
q=|\nabla\Phi|^2,\qquad \nu=2\rho^2q-m\ge0.
\]

## 3. 第5.1—5.2节的速率

继承的精确预算为
\[
\|\rho-\rho_*\|_2^2+\|\zeta\|_2^2+\|\operatorname{Ric}^{\circ}\|_2^2\le Cx,
\]
\[
\fint\frac{(S-2m_*)^2}{S}\le C\sqrt x,
\quad S=m_*+m+\nu=m_*+2\rho^2q,
\quad \|f-K\|_2^2\le C\sqrt x,
\]
\[
K=-\frac98\frac{\rho^3Q}{S},\quad |Q|^2=m^2/8,
\quad \nu\le4\rho|\zeta|^2,\quad0\le\rho\le2.
\]
R1 给
\[
\fint_{q>L^2}q^2\le CL^{-2\epsilon_0}+C\sqrt x.
\]
因此以 \(L=x^{-1/(2+2\epsilon_0)}\) 分割，
\[
\fint |\zeta|^2q+\fint|\zeta|^4\le Cx^\gamma,
\quad \|\nu\|_2\le Cx^{\gamma/2}.
\]
\(S\) 的加权方差及 \(\fint S\le C\) 给
\(\|m-m_*\|_1\le Cx^{1/4}\)。对 \(m\le M\) 使用
\((m-m_*)^2\le C M|m-m_*|\)，对 \(m>M\) 使用 R1；令
\(M=x^{-1/[4(1+\epsilon_0)]}\)，得
\[
\boxed{\|m-m_*\|_2\le Cx^{\gamma/8}.}\tag{3.1}
\]
原稿实际三次 Dirac 公式明确给
\[
\|D\tau\|_2^2\le C\{x+\fint|\zeta|^2q\},
\]
故 \(\|D\tau\|_2\le Cx^{\gamma/2}\)。这一步使用完整轴向消去，未用弱收敛猜测速率。

## 4. 第5.3节的两个乘积必须这样处理

### 4.1 \(Q\) 乘子没有隐藏 \(L^2\times L^2\) 估计

记
\[
h(\rho,S)=2-\frac98\frac{\rho^6}{S}.
\]
由于 \(S\ge m_*\)、\(0\le\rho\le2\)，\(h\) 有界且在该区域对 \(\rho,S\) 全局 Lipschitz；又 \(h(\rho_*,2m_*)=0\)。不能直接用 \(\|h\|_2\|Q\|_2\) 控制其乘积的 \(L^2\) 范数。正确的点态分解是
\[
|hQ|\le C|m-m_*|+C m_*|h|.
\]
因此
\[
\|hQ\|_2\le C\{\|m-m_*\|_2+\|\rho-\rho_*\|_2+
\|S-2m_*\|_2\}\le Cx^{\gamma/8}.
\]
实际多项式曲率式遂给
\(\|\rho^2(d\operatorname{Im}\zeta)^-\|_2\le Cx^{\gamma/8}\)。

### 4.2 低正旋量幅度区的去权

固定 \(0<c_0<\rho_*\)，其低幅度集合体积比例 \(\le Cx\)。分割 \(q\le R\) 与 \(q>R\) 可得
\[
\fint_{\rho<c_0}q^2\le C\{xR^2+R^{-\epsilon_0}+\sqrt x\}.
\]
令 \(R=x^{-1/(2+\epsilon_0)}\)，右侧为
\(Cx^{\epsilon_0/(2+\epsilon_0)}+C\sqrt x\)。由于
\[
\frac{\epsilon_0}{2(2+\epsilon_0)}\ge\frac\gamma8,
\]
它足以给所需的 \(L^2\) 速率。正手性曲率是有界模型加 \(L^2\) 误差，且
\(|d\zeta|\le C(q+\rho|F^{S^+}|)\)。于是去权后仍有
\(\|d\operatorname{Im}\zeta\|_2\le Cx^{\gamma/8}\)，其中另一手性由闭流形 Stokes 恒等式恢复。

同样分割得到 \(\|q-4/9\|_2\le Cx^{\gamma/8}\)，因此 \(\|\Delta\rho\|_2\le Cx^{\gamma/8}\)。对 \(\operatorname{Im}\zeta\) 和 \(d\rho\) 的 Bochner 公式，Ricci 误差配对满足
\[
\left|\fint (\operatorname{Ric}+g)(\zeta,\zeta)\right|
\le C x^{1/2}\|\zeta\|_4^2\le Cx^{(1+\gamma)/2}.
\]
这个指数快于主项 \(\gamma/4\)。所以
\[
\|\nabla\zeta\|_2+\|N_\tau\|_2\le Cx^{\gamma/8}.
\tag{4.1}
\]
完整 \(N_\tau\) 使用原多项式投影式，而非仅 Dirac 迹。

## 5. 补出第5.4节省略的高幅度测试

扭率 Lichnerowicz 方程可写为
\[
D^*D\tau=L\tau-(1+\Gamma)\tau+e\tau,
\quad \Gamma=\frac{27}{32}\frac{\rho^3m}{S},
\quad \|e\|_2\le Cx^{1/4},
\tag{5.1}
\]
其中 \(L=\nabla^*\nabla\)，\(0\le\Gamma\le C\)。这里只用有界性即可。

固定 \(m_*<M_1<M_2\)。取非减光滑 \(\psi(m)\)，在 \(m\le M_1\) 为零，在 \(m\ge M_2\) 为一，令 \(\chi=\psi^2\)。它满足
\(m^2|\chi'|^2\le C\chi\)，且导数只在固定有限幅度环带上。

将(5.1)与 \(\chi\tau\) 配对：
\[
\fint\chi|\nabla\tau|^2+\tfrac12\fint\chi'|dm|^2
=\Re\fint\langle D\tau,D(\chi\tau)\rangle
+\fint(1+\Gamma)\chi m-\Re\fint\chi\langle e\tau,\tau\rangle.
\]
左侧第二项非负。右侧
\(D(\chi\tau)=\chi D\tau+c(d\chi)\tau\)，且
\[
|D\tau|\,|d\chi|\sqrt m
\le \varepsilon\chi|\nabla\tau|^2+C_\varepsilon|D\tau|^2.
\]
这里使用 \(|dm|\le2\sqrt m|\nabla\tau|\) 和固定环带常数，没有曲率导数。

由于 \(m\ge M_1>m_*\) 时 \(m\le C(m-m_*)^2\)，得到
\[
\fint_{m\ge M_2}|\nabla\tau|^2
\le C\left(\|D\tau\|_2^2+\|m-m_*\|_2^2+
\|e\|_2\|m\|_2\right)
\le Cx^{\gamma/4}.
\tag{5.2}
\]
最后用 \(\gamma\le1/2\)，故 \(x^{1/4}\le x^{\gamma/4}\)。这给出了新附件第5.4节声称的尾梯度估计的完整理由。

选择固定光滑径向 cap \(u=T(\tau)\)，在足够大的固定幅度以下恒等，其改变区域包含在(5.2)控制的集合内。则
\[
\|u-\tau\|_{H^1}\le Cx^{\gamma/8},
\quad |u|\le C,
\quad \|Du\|_2\le Cx^{\gamma/8}.
\]
由于 \(u\) 与 \(\tau\) 逐点共线，\((\mathcal V+2)u=(1-\Gamma)u+eu\)。\(\Gamma\) 对 \(\rho,m,\nu\) 是有界 Lipschitz 有理式，故
\(\|(\mathcal V+2)u\|_2\le Cx^{\gamma/8}\)。

令 \(v=3(I+L)^{-1}u\)，则
\[
(I+L)(v-u)=-D^*Du+(\mathcal V+2)u.
\]
能量测试给
\[
\boxed{\|v-\tau\|_{H^1}\le Cx^{\gamma/8},\quad
\|(L-2)v\|_2+\|Dv\|_2\le Cx^{\gamma/8}.}\tag{5.3}
\]
最大值原理同时给 \(|v|+|Lv|\le C\)。

## 6. D轮清单新增的 \(L^4\) 转移及拟合项

新附件的较短 \(\mathfrak e\) 定义未显式列入 \(\|v-\tau\|_4\)，而 D 轮列入了，故必须补查。

\(v-u\) 有界，(5.3) 给
\[
\|v-u\|_4^4\le C\|v-u\|_2^2\le Cx^{\gamma/4}.
\]
固定 cap 的改变区远离 \(m_*\)，因此
\[
\|u-\tau\|_4^4\le C\fint_{\rm cap\ region}m^2
\le C\|m-m_*\|_2^2\le Cx^{\gamma/4}.
\]
所以
\[
\boxed{\|v-\tau\|_4\le Cx^{\gamma/16}.}\tag{6.1}
\]

辅助幅度 \(a=|v|^2\) 的 \(L^2\) 误差为 \(O(x^{\gamma/8})\)：先与有界 cap \(u\) 比较，再用固定径向 cap 对 \(m\) 的 Lipschitz 依赖。\(N_v-N_\tau\) 由 \(H^1\) 差控制。

对于 Hopf 拟合，
\[
\|Q_v-Q_\tau\|_2\le C(\|v\|_4+\|\tau\|_4)\|v-\tau\|_4
\le Cx^{\gamma/16}.
\]
而
\(\|K+(27/32)Q_\tau\|_2\le Cx^{\gamma/8}\)，其证明同4.1节的有界系数与 \(m=m_*+(m-m_*)\) 分解。因此
\[
\|-iF_A^-+(27/32)Q_v\|_2\le Cx^{\gamma/16}.
\]
在固定正幅度区，正旋量的相位系数为 \(\operatorname{Im}\zeta/\rho\)，其 \(L^2\) 小量为 \(O(x^{1/2})\)。正旋量非对角联络的误差由实际三次扭率代数式给出，其相对于适配 \(v\) 的误差受 \(C(|v-\tau|+|\zeta|)\) 控制；固定截断使分母有界。因此其 \(L^2\) 速率也不慢于 \(x^{\gamma/8}\)。

至此 D 轮的每一个 primitive error 均已覆盖，得到(A)。不以任意可调的误差序列代替它。

## 7. 不依赖高幅度尾测试的直接 resolvent 复核

还可改用 C 轮
\[
(4+L)v=6T(\tau),\qquad w=v-\tau.
\]
只需固定 cap 的 \(L^2\) 差，不微分 cap。

(5.1)给
\[
(4+L)w=6(T\tau-\tau)-D^*D\tau-(\Gamma-1)\tau+e\tau.
\]
对此测试 \(w\)。特别注意有理系数的结构给
\[
\|(\Gamma-1)\tau\|_2
\le C(\|\rho-\rho_*\|_2+\|m-m_*\|_2+\|\nu\|_2)
\le Cx^{\gamma/8}.
\]
证明分 \(m\le2m_*+1\)（\(\sqrt m\) 有界、系数 Lipschitz）与补集（\(m\le C(m-m_*)^2\)、系数有界）。这是比机械 \(L^2\times L^4\) 更好的合法估计。

曲率余项仅需
\[
|\fint\langle e\tau,w\rangle|
\le\|e\|_2\|\tau\|_4\|w\|_4\le Cx^{1/4}.
\]
这里 \(\|w\|_4\le\|v\|_\infty+\|\tau\|_4\le C\)，不使用 Sobolev。

吸收其余线性项后
\[
\|w\|_{H^1}^2\le C(x^{\gamma/4}+x^{1/4})\le Cx^{\gamma/4}.
\]
于是同样得到(5.3)、(6.1)以及(A)。这条替代是对速率转接的独立检查，不注册为额外端点定理。

## 8. 与 D 轮正势排除组合的准确含义

D轮结论是：不存在满足
\[
\mathfrak e_D(1+b)^{3/2}\to0
\]
的原实际零端序列。若(B)不成立，可选择允许对象使
\(x(1+b)^{24/\gamma}\to0\)。于是 \(x\to0\)，且
\[
\mathfrak e_D(1+b)^{3/2}
\le C\{x(1+b)^{24/\gamma}\}^{\gamma/16}\to0,
\]
与该结论矛盾。由此得到某个普适 \(c>0\) 的(B)。此处没有假定事后选出的误差恰好比密度快。

若 \(\chi/A\le B\)、\(\kappa\le1\)，已有 Euler 预算给 \(1+b\le C(1+B)\)，故令 \(p=24/\gamma\)，可推导
\[
\kappa_\beta+\beta^{-2}\ge c(1+B)^{-p}.
\]
以 \(\beta_B=(2/m_B)^{1/2}\)、\(m_B=c(1+B)^{-p}\) 分割大小参数，再用已证有限参数估计及共形比较，得到
\[
\fint|\operatorname{Ric}_g+g|^2+D_\beta(g)/V_g
\ge c'(1+B)^{-p}\frac{(\beta-2)^2}{\beta^2}.
\]
这一步改变的是已知常数依赖及增长率排除，不排除 \(b\) 与 \(x^{-\gamma/24}\) 同阶或更快的实际情形。它不是最终无密度 O10，也没有提供 O11 的锐利拓扑补偿。
