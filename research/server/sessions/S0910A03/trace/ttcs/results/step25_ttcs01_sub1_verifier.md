# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A03/workspace/scripts/verify_step25_normalization_and_moser_exponents.py",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Sessions/S0910A01/workspace/codex_loop/work/verify_tensor_energy_ledger.py",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the Step 25 mathematical repair for the four-dimensional normalized cutoff flow. Check (i) the combined fully covariant tensor, inverse-metric, and measure contributions under the homothetic piece -2ag, including the formula for the pure-normalization variation of F^p dmu; (ii) the general weighted weak power inequality for K_p=int eta^2 a^(p-2) Phi^p with Phi=F or |E|; (iii) the H3-potential interpolation and Young exponents; and (iv) the exact match p'_j=p_j-2 with Yang's fixed-cutoff Moser iteration in n=4, including whether p0=3 gives |a Rm|<=C beta/t and p0=6 gives |aE|<=C delta(r^2/t)^(1/3) on the whole active support. Identify any hidden cutoff, measure, tensor-regularization, or exponent error. Give corrected formulas if needed; do not infer a pinching gap unless the supplied proof actually closes.

## Output

# 独立核验备忘

## 总结

在“已有光滑解、当前度量保持双 Lipschitz 等价、相对 Sobolev 不等式持续成立、\(\beta_*\) 足够小”这些前提下，Step 25 的四个核心计算均成立：

1. 四维中，\(-2ag\) 对 \(|\mathrm{Rm}|^2d\mu\) 没有净耗散；\(F^pd\mu\) 的公式正确。
2. 加权矩
   \[
   K_p[\Phi]=\int\eta^2a^{p-2}\Phi^p
   \]
   满足所写弱幂次不等式；曲率与 Einstein 缺陷的权重完全匹配。
3. \(H_3\) 插值和 Young 指数给出 \(p^3\mathsf S^2H_3\)，没有幂次错位。
4. Yang 附录 A 在 \(n=4\) 中确有 \(p'_j=p_j-2\)，终点正是 \(a\Phi\)。由 \(p_0=3,6\) 得到的两个时间尺度也正确。

需要在正文中补明三点：辅助静止环带与 \(\beta\) 的能量记账、\(J_6\) 传播所用的固定幂次吸收、以及 \(|E|\) 与非整数截断幂的正则化。归一化退化流延拓到 \(\theta r^2\) 仍未由现有材料给出，因此这些估计本身尚未推出 Ricci 夹逼常数的间隙结论。

---

## 1. \(-2ag\) 的四维缩放记账

先令 \(a\) 在空间上为常数。对
\[
\partial_tg=-2ag
\]
有
\[
\partial_tR^\ell{}_{ijk}=0,\qquad
\partial_tR_{ijkl}=-2aR_{ijkl},\qquad
\partial_tg^{ij}=2ag^{ij}.
\]

写 \(x=|\mathrm{Rm}|^2\)。两个全协变曲率张量贡献 \(-4ax\)，四个逆度量贡献 \(8ax\)，所以
\[
\partial_tx=4ax.
\]
另一方面
\[
\partial_td\mu=\frac12\operatorname{tr}_g(-2ag)d\mu=-na\,d\mu.
\]
因此一般维数中
\[
\left.\partial_t(x\,d\mu)\right|_{-2ag}=(4-n)ax\,d\mu,
\]
四维恰为零。

令 \(F=(1+x)^{1/2}\)。由 \(x=F^2-1\)，
\[
\partial_tF^p
=\frac p2F^{p-2}\partial_tx
=2pa(F^2-1)F^{p-2}.
\]
故一般维数公式为
\[
\left.\partial_t(F^pd\mu)\right|_{-2ag}
=a\big[(2p-n)F^p-2pF^{p-2}\big]d\mu.
\]
在 \(n=4\) 中化为
\[
\boxed{
\left.\partial_t(F^pd\mu)\right|_{-2ag}
=2a\big[(p-2)F^p-pF^{p-2}\big]d\mu.}
\]

特别地，
\[
p=2:\qquad \partial_t(F^2d\mu)=-4a\,d\mu.
\]
这只来自 \(F^2=1+|\mathrm{Rm}|^2\) 中的常数 \(1\)，并不是
\(-4aF^2d\mu\)。所以 Step 25 删除“归一化产生曲率能量耗散”的旧用法是正确的。

当 \(a\) 随空间变化时，上式只能描述代数缩放部分；\(\nabla a,\nabla^2a\) 产生的项必须回到完整张量方程中处理，不能用上述密度公式替代。Step 25 正是这样处理的。

---

## 2. 一般加权弱幂次不等式

设
\[
K_p[\Phi]=\int\eta^2a^{p-2}\Phi^p,\qquad
Z_p[\Phi]=\eta a^{(p-1)/2}\Phi^{p/2},\qquad p\ge3.
\]

### 2.1 曲率情形

全协变曲率方程具有形式
\[
\partial_t\mathrm{Rm}
=a\Delta\mathrm{Rm}
+a\,\mathcal A(\mathrm{Rm})
+(da)*\nabla E+(\nabla^2a)*E,
\]
其中
\[
|\mathcal A|\le C(F^2+F),\qquad
|E|\le CF,\qquad |\nabla E|\le C|\nabla\mathrm{Rm}|.
\]

以
\[
\eta^2a^{p-2}F^{p-2}\mathrm{Rm}
\]
测试。主扩散项给出
\[
p\int\eta^2a^{p-1}F^{p-2}|\nabla\mathrm{Rm}|^2
+p(p-2)\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2.
\]
这些项控制 \(\|\nabla Z_p\|_2^2\)，因为
\[
|\nabla Z_p|^2
\le Cp^2\eta^2a^{p-1}F^{p-2}|\nabla\mathrm{Rm}|^2
+Cp^2\eta^2a^{p-3}|da|^2F^p.
\]
利用
\[
|da|^2=4a|d\chi|^2
\]
得到
\[
a^{p-3}|da|^2F^p
=4a^{p-2}|d\chi|^2F^p
\le Cr^{-2}a^{p-2}F^p.
\]

Hessian 截断项只需分部积分一次：
\[
\int\eta^2a^{p-2}F^{p-2}\mathrm{Rm}*(\nabla^2a)*E
=-\int da*\nabla\!\left(
\eta^2a^{p-2}F^{p-2}\mathrm{Rm}*E\right).
\]
导数落在 \(a,F,\mathrm{Rm},E\) 上时，分别由上述耗散项和
\[
a^{p-3}|da|^2F^p\le Cr^{-2}a^{p-2}F^p
\]
控制。由于 \(\eta=1\) 于 \(\operatorname{supp}\chi\) 的一个邻域，所有含 \(d\eta\) 的项都乘有 \(a\) 或 \(da\)，因而为零。

全协变张量、逆度量和测度的代数变化合在一起后至多产生
\[
Cp\int\eta^2a^{p-1}F^{p+1}.
\]

### 2.2 Einstein 缺陷情形

取
\[
\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}.
\]
由已给出的精确恒等式
\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+4a\mathrm{Rm}(E,E)
+2\langle E,\mathcal C_a(E)\rangle
\]
以及分部积分公式
\[
\begin{aligned}
\int2q\langle E,\mathcal C_a(E)\rangle
=\int\{&
-2|E|^2\langle da,dq\rangle
-2\tau E(dq,da)+4E^2(dq,da)\\
&+q[-\tau\langle da,d\tau\rangle
+2E(da,d\tau)]\},
\end{aligned}
\]
取
\[
q\sim\eta^2a^{p-2}\Phi_\varepsilon^{p-2}
\]
后，所有项都至少含一个 \(E\) 或 \(\nabla E\)。同样只出现
\[
Cp^2r^{-2}K_p[\Phi_\varepsilon]
\]
和
\[
Cp\int\eta^2a^{p-1}F\Phi_\varepsilon^p.
\]
常数可取与 \(\varepsilon\) 无关，令 \(\varepsilon\downarrow0\) 即得 \(\Phi=|E|\)。

因此可写成
\[
\boxed{
\frac d{dt}K_p+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p
+Cp\int\eta^2a^{p-1}F\Phi^p.}
\]
这与 Step 25 的 (4.2) 一致。A01 文件明确采用 \(0<r\le1\)；若正文不保留这一归一化，所有无量纲低阶项宜统一写为 \(C(1+r^{-2})K_p\)。

---

## 3. \(H_3\) 插值与 Young 指数

点态恒等式正确：
\[
a^{p-1}F\Phi^p
=(aF^3)^{1/3}
\left(a^{3p/2-2}\Phi^{3p/2}\right)^{2/3}.
\]
因此
\[
I_p:=\int\eta^2a^{p-1}F\Phi^p
\le H_3^{1/3}K_{3p/2}^{2/3}.
\]

权重插值也完全匹配：
\[
K_{3p/2}
\le K_p^{1/2}K_{2p}^{1/2},
\]
因为
\[
\frac12(p-2)+\frac12(2p-2)=\frac{3p}{2}-2.
\]

又由于 \(\eta=1\) 于所有 \(a>0\) 的点，
\[
K_{2p}^{1/2}
=\|Z_p\|_4^2.
\]
相对 Sobolev 不等式给出
\[
K_{2p}^{1/2}
\le\mathsf S\bigl(\|\nabla Z_p\|_2^2+r^{-2}K_p\bigr).
\]
记
\[
A_p=\|\nabla Z_p\|_2^2+r^{-2}K_p.
\]
于是
\[
I_p
\le \mathsf S^{2/3}H_3^{1/3}
K_p^{1/3}A_p^{2/3}.
\]
对 \(CpI_p\) 用指数 \(3/2\) 与 \(3\) 的 Young 不等式：
\[
CpI_p
\le\varepsilon A_p
+C_\varepsilon p^3\mathsf S^2H_3K_p.
\]
吸收梯度部分后即得
\[
\boxed{
CpI_p
\le\frac c2\|\nabla Z_p\|_2^2
+Cp^3\bigl(r^{-2}+\mathsf S^2H_3\bigr)K_p.}
\]
所以 \(p^3\)、\(\mathsf S^2\)、\(H_3\) 的指数都正确。

---

## 4. 与 Yang 固定截断迭代的精确对应

Yang 附录 A 取
\[
v=1+\frac2n.
\]
在 \(n=4\) 中 \(v=3/2\)，且
\[
p_j=p_0v^j,\qquad
p'_j=(p_0-2)v^j+\sum_{k=0}^{j-1}v^k.
\]
由于
\[
\sum_{k=0}^{j-1}v^k
=\frac{v^j-1}{v-1}=2(v^j-1),
\]
得到
\[
p'_j=(p_0-2)v^j+2v^j-2=p_0v^j-2=p_j-2.
\]
因此 Yang 的矩
\[
\chi^{2p'_j}\Phi^{p_j}
=\chi^{2p_j-4}\Phi^{p_j}
=a^{p_j-2}\Phi^{p_j}
\]
正是 \(K_{p_j}\)，并且
\[
\chi^{2p'_j/p_j}\Phi
=\chi^{2-4/p_j}\Phi\longrightarrow\chi^2\Phi=a\Phi.
\]

取 Yang 的势指数 \(q=6\)，则
\[
\int\chi^{q-n}F^{q/2}
=\int\chi^2F^3
=\int aF^3=H_3.
\]
由
\[
H_3(s)^{1/3}
\le C\beta_*\mathsf S^{-2/3}s^{-1/3}
\]
可取 Yang 参数
\[
\mu=C\beta_*\mathsf S^{-2/3},
\]
故
\[
\mathsf S^{2/3}\mu=C\beta_*,
\qquad
\mathsf S^2\mu^3=C\beta_*^3.
\]
这与 Step 25 的 \(p^3\beta_*^3/t\) 完全一致。

迭代乘积给出
\[
\|a\Phi\|_\infty
\le C\mathsf S^{2/p_0}(t^{-1}+r^{-2})^{3/p_0}
\mathcal M_{p_0}^{1/p_0}.
\]

### 曲率，\(p_0=3\)

若
\[
\mathcal M_3\le C\frac{\beta_*^3}{\mathsf S^2},
\]
则
\[
\|aF\|_\infty
\le C\mathsf S^{2/3}(t^{-1}+r^{-2})
\left(\frac{\beta_*^3}{\mathsf S^2}\right)^{1/3}
=C\beta_*(t^{-1}+r^{-2}).
\]
当 \(t\le r^2\) 时，
\[
\boxed{\|a\,\mathrm{Rm}\|_\infty\le\|aF\|_\infty
\le C\beta_*/t.}
\]

### 缺陷，\(p_0=6\)

若
\[
\mathcal M_6\le Ct\,\delta^6V,
\]
则
\[
\begin{aligned}
\|aE\|_\infty
&\le C\mathsf S^{1/3}(t^{-1}+r^{-2})^{1/2}
(t\delta^6V)^{1/6}\\
&\le C\delta\,\mathsf S^{1/3}V^{1/6}t^{-1/3}.
\end{aligned}
\]
再用
\[
\mathsf S\le Cr^2V^{-1/2}
\]
得到
\[
\boxed{
\|aE\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.}
\]
体积因子恰好消去，所以该估计允许塌缩。

---

## 5. 需要补明的技术点

### 5.1 静止环带与 \(H_2\)

Step 25 定义
\[
H_2=\int\eta^2F^2,
\qquad
\beta=\mathsf S\|F\|_{L^2(\operatorname{supp}\chi)}.
\]
辅助环带中 \(a=0\)，其曲率能量可能很大，但在那里流不动。若直接用完整 \(H_2(0)\) 控制 \(H_3\)，不能自动得到只含 \(\beta\) 的
\(\mathsf S^2H_3\lesssim\beta^3/t\)。

精确记账可取
\[
C_{\rm col}
=\int_{M\setminus\operatorname{supp}\chi}
\eta^2F(0)^2\,d\mu_0,
\qquad
\widehat H_2=H_2-C_{\rm col}.
\]
在该静止区域，度量、曲率和测度均不变；于是
\[
\widehat H_2(t)
=\int_{\operatorname{supp}\chi}F(t)^2\,d\mu_t
\]
并满足强化后的能量式
\[
\widehat H_2'+cD_2
\le CH_3+Cr^{-2}\widehat H_2.
\]
这样
\[
\widehat H_2(0)=\beta(0)^2/\mathsf S^2
\]
才直接产生所需的 \(\beta^3/\mathsf S^2\) 时空估计。另一种写法是明确假设整个辅助支集的初始 \(L^2\) 能量也由同一良好支集估计控制。

### 5.2 \(J_6\) 传播

“齐次性”还需配合固定 \(p=6\) 的临界吸收。具体为
\[
\int\eta^2a^5F|E|^6
=\int F\,|\,\eta a^{5/2}E^3|^2
\le\|F\|_{L^2(\operatorname{supp}\chi)}
\|Z_6\|_4^2.
\]
Sobolev 不等式给出
\[
\int\eta^2a^5F|E|^6
\le C\beta(t)\bigl(\|\nabla Z_6\|_2^2+r^{-2}J_6\bigr).
\]
当当前 \(\beta\) 足够小时，梯度项可吸收，从而
\[
J_6'\le Cr^{-2}J_6,
\qquad
J_6(t)\le e^{Ct/r^2}J_6(0).
\]
因此 (3.3) 正确，但这一行宜显式写出。

### 5.3 正则化和非整数幂

\(|E|\) 在零点不光滑，应始终先用
\[
\Phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2}
\]
推导，且常数与 \(\varepsilon\) 无关，再令 \(\varepsilon\to0\)。

Moser 序列产生非整数 \(p_j\)。采用非负标准光滑截断，并使其在支集外缘平坦，则
\[
a^{p_j-2},\qquad a^{(p_j-1)/2}
\]
具有弱能量计算所需的正则性。也可先对这些权重作光滑逼近后取极限。

---

## 科学状态

`verify_step25_normalization_and_moser_exponents.py` 正确验证了缩放恒等式、权重代数、指数和与最终尺度；它只计算这些代数部分。张量弱式、静止环带记账、Sobolev 持续性以及归一化退化流延拓依赖上述几何推导。

因此，Step 25 的归一化修复和 whole-support Moser 指数链在预备光滑时段上成立；\(|a\mathrm{Rm}|\) 与 \(|aE|\) 的两个终点估计也是正确的。现有文件尚缺归一化 Wang 延拓归纳，故尚不能把这些条件性估计连接成完整的四维几何矛盾证明。