# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 25,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step25_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step25_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the Step 25 mathematical repair for the four-dimensional normalized cutoff flow. Check (i) the combined fully covariant tensor, inverse-metric, and measure contributions under the homothetic piece -2ag, including the formula for the pure-normalization variation of F^p dmu; (ii) the general weighted weak power inequality for K_p=int eta^2 a^(p-2) Phi^p with Phi=F or |E|; (iii) the H3-potential interpolation and Young exponents; and (iv) the exact match p'_j=p_j-2 with Yang's fixed-cutoff Moser iteration in n=4, including whether p0=3 gives |a Rm|<=C beta/t and p0=6 gives |aE|<=C delta(r^2/t)^(1/3) on the whole active support. Identify any hidden cutoff, measure, tensor-regularization, or exponent error. Give corrected formulas if needed; do not infer a pinching gap unless the supplied proof actually closes.

## Integrated Scientific Memo

# Step 25 独立核验结论

在“已有光滑解、当前度量双 Lipschitz 控制、相对 Sobolev 不等式持续、当前临界量 \(\beta_*\) 足够小”的条件下，Step 25 的归一化记账、\(H_3\) 插值、Yang 固定截断指数以及两个终点尺度均正确。需要修补的不是这些代数指数，而是若干被略写的弱式与闭合条件；尤其归一化退化流的延拓仍未证明，故不能据此推出 pinching gap。

## 1. 纯归一化项的完整记账

对空间常数 \(a\) 和
\[
\partial_tg=-2ag
\]
有
\[
\partial_tR^\ell{}_{ijk}=0,\qquad
\partial_tR_{ijkl}=-2aR_{ijkl},\qquad
\partial_tg^{ij}=2ag^{ij}.
\]
令 \(x=|\mathrm{Rm}|^2\)。两个全协变曲率张量贡献 \(-4ax\)，四个逆度量贡献 \(+8ax\)，故
\[
\partial_tx=4ax.
\]
一般维数中
\[
\partial_td\mu=-na\,d\mu,\qquad
\partial_t(x\,d\mu)=(4-n)ax\,d\mu.
\]
因此 \(n=4\) 时
\[
\partial_t(|\mathrm{Rm}|^2d\mu)=0.
\]

对
\[
F=(1+x)^{1/2}
\]
的一般维数公式是
\[
\boxed{
\left.\partial_t(F^pd\mu)\right|_{-2ag}
=a\big[(2p-n)F^p-2pF^{p-2}\big]\,d\mu.}
\]
四维中特化为
\[
\boxed{
\left.\partial_t(F^pd\mu)\right|_{-2ag}
=2a\big[(p-2)F^p-pF^{p-2}\big]\,d\mu.}
\]
特别地 \(p=2\) 时为 \(-4a\,d\mu\)，只来自 \(F^2=1+|\mathrm{Rm}|^2\) 中常数 \(1\) 的测度变化；绝不是 \(-4aF^2d\mu\)。因此不能利用纯归一化得到四维曲率能量耗散。空间变化的 \(a\) 所产生的 \(da,\nabla^2a\) 项必须另由完整张量方程处理。

## 2. 一般加权弱幂次不等式

设
\[
K_p[\Phi]=\int\eta^2a^{p-2}\Phi^p,\qquad
Z_p[\Phi]=\eta a^{(p-1)/2}\Phi^{p/2},\qquad p\ge3,
\]
其中 \(\Phi=F\)，或缺陷情形先取
\[
\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}.
\]

曲率方程具有结构
\[
\partial_t\mathrm{Rm}
=a\Delta\mathrm{Rm}+a\,\mathcal A(\mathrm{Rm})
+(da)*\nabla E+(\nabla^2a)*E,
\]
且
\[
|\mathcal A|\le C(F^2+F),\qquad |E|\le CF,\qquad
|\nabla E|\le C|\nabla\mathrm{Rm}|.
\]
以 \(\eta^2a^{p-2}F^{p-2}\mathrm{Rm}\) 测试，并对每个 \(\nabla^2a\) 项分部积分一次。关键余项满足
\[
a^{p-3}|da|^2\Phi^p
=4a^{p-2}|d\chi|^2\Phi^p
\le Cr^{-2}a^{p-2}\Phi^p.
\]
严格 buffer 条件保证所有含 \(a\,d\eta\) 或 \(da\,d\eta\) 的项消失。

缺陷方程由
\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+4a\mathrm{Rm}(E,E)
+2\langle E,\mathcal C_a(E)\rangle
\]
给出；分部积分后 cutoff 项至少二次于 \(E,\nabla E\)，没有独立的
\((\nabla^2a)*g\) 源项。因此在 \(\varepsilon\)-一致意义下得到
\[
\boxed{
\frac d{dt}K_p+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p
+Cp\int\eta^2a^{p-1}F\Phi^p.}
\]
令 \(\varepsilon\downarrow0\) 得 \(\Phi=|E|\)。

这里 \(c\) 可对 \(p\ge3\) 统一；若把耗散重新归一化为 \(\|\nabla Z_p\|_2^2\)，右侧的精确 \(p\)-多项式次数可能比书写的 \(p^2,p^3\) 更大，但这不影响 Moser 无限乘积。若不假设 \(r\le1\)，低阶项应写为 \(C(1+r^{-2})K_p\)。

## 3. \(H_3\) 插值与 Young 指数

逐点权重恒等式正确：
\[
a^{p-1}F\Phi^p
=(aF^3)^{1/3}
\left(a^{3p/2-2}\Phi^{3p/2}\right)^{2/3}.
\]
因而
\[
I_p:=\int\eta^2a^{p-1}F\Phi^p
\le H_3^{1/3}K_{3p/2}^{2/3}.
\]
再由
\[
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}
\]
以及
\[
K_{2p}^{1/2}=\|Z_p\|_4^2
\le \mathsf S\bigl(\|\nabla Z_p\|_2^2+r^{-2}K_p\bigr)
\]
得到
\[
I_p\le
\mathsf S^{2/3}H_3^{1/3}
K_p^{1/3}
\bigl(\|\nabla Z_p\|_2^2+r^{-2}K_p\bigr)^{2/3}.
\]
使用共轭指数 \(3/2\) 与 \(3\) 的 Young 不等式：
\[
\boxed{
CpI_p\le
\frac c2\|\nabla Z_p\|_2^2+
Cp^3\bigl(r^{-2}+\mathsf S^2H_3\bigr)K_p.}
\]
所以 \(p^3,\mathsf S^2,H_3\) 的指数均正确。若
\[
\mathsf S^2H_3(s)\le C\beta_*^3/s,
\]
则在 \([t/2,t]\)
\[
K_p'+\frac c2\|\nabla Z_p\|_2^2
\le Cp^3\left(r^{-2}+\frac{\beta_*^3}{t}\right)K_p.
\]

## 4. 与 Yang 固定截断迭代的精确对应

Yang 附录 A 中
\[
v=1+\frac2n,\qquad p_j=p_0v^j,
\]
且
\[
p'_j=(p_0-n/2)v^j+\sum_{k=0}^{j-1}v^k.
\]
四维时 \(v=3/2,n/2=2\)，而
\[
\sum_{k=0}^{j-1}v^k=2(v^j-1),
\]
故
\[
\boxed{p'_j=p_j-2.}
\]
于是 Yang 的矩恰为
\[
\chi^{2p'_j}\Phi^{p_j}
=\chi^{2p_j-4}\Phi^{p_j}
=a^{p_j-2}\Phi^{p_j}=K_{p_j}[\Phi],
\]
终点为
\[
\chi^{2p'_j/p_j}\Phi\longrightarrow\chi^2\Phi=a\Phi.
\]

取势指数 \(q=6\)：
\[
\int\chi^{q-4}F^{q/2}
=\int\chi^2F^3=H_3.
\]
因此这一对应是完全相同的权重体系，而非类比。Moser 乘积给出
\[
\boxed{
\|a\Phi\|_\infty
\le C\mathsf S^{2/p_0}
(t^{-1}+r^{-2})^{3/p_0}
\mathcal M_{p_0}^{1/p_0},}
\]
其中 \(\mathcal M_{p_0}\) 是相应正时间段上的时空矩。

### 曲率：\(p_0=3\)

若
\[
\mathcal M_3\le C\frac{\beta_*^3}{\mathsf S^2},
\]
则
\[
\|aF\|_\infty
\le C\beta_*(t^{-1}+r^{-2}).
\]
对 \(0<t\le r^2\)，
\[
\boxed{\|a\,\mathrm{Rm}\|_\infty\le C\beta_*/t.}
\]

### 缺陷：\(p_0=6\)

若
\[
\mathcal M_6\le Ct\,\delta^6V,
\]
则
\[
\|aE\|_\infty
\le C\mathsf S^{1/3}(t^{-1}+r^{-2})^{1/2}
(t\delta^6V)^{1/6}.
\]
使用
\[
\mathsf S\le Cr^2V^{-1/2}
\]
且 \(t\le r^2\)，得到
\[
\boxed{
\|aE\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.}
\]
两者控制的是整个 active support 上的加权量 \(a\Phi\)，包括 transition collar；它们不声称控制 collar 中未加权的 \(\Phi\)。

## 5. 必须补写或澄清的隐藏点

### 5.1 静止辅助环带不能混入 \(\beta\)-估计

\[
H_2=\int\eta^2F^2
\]
包含 \(a=0\) 的辅助环带，而
\[
\beta=\mathsf S\|F\|_{L^2(\operatorname{supp}\chi)}
\]
只测 active support。若环带初始曲率能量任意大，不能直接由完整 \(H_2(0)\) 推出只依赖 \(\beta\) 的 \(H_3\) 估计。

应减去静止部分：
\[
C_{\rm col}:=
\int_{M\setminus\operatorname{supp}\chi}
\eta^2F(0)^2\,d\mu_0,\qquad
\widehat H_2=H_2-C_{\rm col}.
\]
因 \(a=0\) 区域度量恒定，
\[
\widehat H_2(t)
=\int_{\operatorname{supp}\chi}F(t)^2\,d\mu_t,
\]
并应对 \(\widehat H_2\) 建立能量估计。否则
\(\mathsf S^2H_3\lesssim\beta_*^3/t\) 的推导存在域不匹配。

### 5.2 \(J_6\) 传播不能只说“齐次”

对
\[
J_6=\int\eta^2a^4|E|^6
\]
需显式使用
\[
\int\eta^2a^5F|E|^6
=\int F\,|\eta a^{5/2}E^3|^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\|Z_6\|_4^2.
\]
由 Sobolev 和当前 \(\beta\) 小性吸收梯度后，
\[
J_6'\le Cr^{-2}J_6,\qquad
J_6(t)\le e^{Ct/r^2}J_6(0).
\]
因此所述传播结论可成立，但其依据是固定 \(p=6\) 的临界吸收，不只是方程齐次性。

### 5.3 正则化和 cutoff 幂

\(|E|\) 在零点不光滑，弱式应先对
\[
(|E|^2+\varepsilon^2)^{1/2}
\]
建立一致估计再取极限。

Moser 序列中的 \(p_j\) 通常非整数，因此 \(a^{p_j-2}\) 在 \(a=0\) 附近的经典光滑性不能默认。可使用在支集边缘平坦的标准 smooth cutoff，或先平滑逼近这些权重，再以弱收敛取极限。该问题不改变指数，但必须在严格证明中处理。

### 5.4 \(\eta\) 的等式条件

诸如
\[
K_{2p}^{1/2}=\|Z_p\|_4^2
\]
使用了 \(\eta=1\) 在 \(\operatorname{supp}\chi\) 的邻域；因为所有 \(a\)-加权积分支撑于此，\(\eta^4=\eta^2=1\)。若只知 \(\eta\) 为一般 cutoff，则仅有相应不等式并出现 \(d\eta\) 误差。

## 6. 严格状态

已核准的是：在预备光滑 bootstrap 区间内，归一化修复、一般加权弱幂次结构、\(H_3\)-Young 指数、Yang 权重匹配，以及
\[
|a\mathrm{Rm}|\lesssim\beta_*/t,\qquad
|aE|\lesssim\delta(r^2/t)^{1/3}
\]
的 whole-support 尺度。

尚未由现有材料完成的是：

1. 有界 \(|a\mathrm{Rm}|\) 下归一化退化 cutoff flow 的 Wang 型延拓归纳；
2. 将 metric comparison、Sobolev 常数、cutoff 梯度和 \(\beta(t)\) 同时严格改进的 first-exit 闭合；
3. 所使用的相对 Sobolev 标度与初始 good-support 小性的完整来源证明。

因此 Step 25 尚不足以导出任何 Ricci 夹逼间隙或原始 Yau 第 26 题的结论。