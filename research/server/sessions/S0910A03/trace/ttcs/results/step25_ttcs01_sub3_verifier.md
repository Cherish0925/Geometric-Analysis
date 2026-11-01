# TTCS Independent Branch Record

```json
{
  "step_id": 25,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Read the corrected Step 25 single-support argument as a PDE/geometric compactness expert. Determine exactly which parts of the simultaneous first-exit are now established and whether the whole-support bounds for a Rm and aE genuinely restore metric/Sobolev/cutoff control before plateau regularity. Then analyze the remaining normalized Yang-Wang existence/continuation adaptation: does bounded |a Rm| together with the derived metric comparison suffice after adding -2ag, or are additional uniform quantities missing? Finally verify that the only justified terminal local obstruction is the Step 6 projector plus Einstein-Weyl identity, not local-symmetry classification. Produce a precise scientific memo that distinguishes proved implications from remaining derivations without reducing the original Yau 26 goal.

## Output

# 科学复核备忘录

## 一、总体结论

Step 25 修正了两个实质性问题。

1. 对四维纯缩放速度 \(\partial_tg=-2ag\)，\(\int |\mathrm{Rm}|^2\,d\mu\) 没有耗散增益。式 (2.2)–(2.4) 的缩放计算正确，因此后续能量估计不能借用虚假的 \(-4aF^2\) 项。
2. \(\|aE\|_\infty\) 在整个活动支撑上的可积估计确实控制了所有发生度量变化的点，包括过渡环带。它足以恢复首次逸出论证所需的双 Lipschitz 比较、固定区域体积比较、相对 Sobolev 系数和 \(|d\chi|_{g(t)}\)。仅在 \(a=1\) 平台上的估计做不到这一点。
3. \(\|a\mathrm{Rm}\|_\infty\) 的主要作用是正时间光滑延拓及随后平台内部正则性；度量比较本身由 \(\|aE\|_\infty\) 直接给出。
4. 现有材料尚未写出归一化 Yang–Wang 延拓的完整高阶归纳。加上的 \(-2ag\) 不改变主符号，也没有显现新的独立几何假设；但双 Lipschitz 比较和 \(|a\mathrm{Rm}|\) 有界本身并不会自动给出光滑延拓，仍需推导 Wang 体系中的非加权 \(L^p\) 曲率、加权曲率导数及截断函数协变导数。
5. Step 6 的局部矛盾是成立的：常谱、\(\delta W^+=0\) 推出 \(\nabla W^+=0\)，而 Einstein–Weyl 标量恒等式给出 \(|\nabla W^+|^2=1/16\)。不能从 \(\nabla W^+=0\) 推出 \(\nabla\mathrm{Rm}=0\)，因此局部对称空间分类在这里没有依据。

---

## 二、Step 25 中已经可靠成立的解析部分

### 1. 归一化能量修正正确

对空间常数 \(a\)，全协变曲率满足

\[
\partial_tR_{ijkl}=-2aR_{ijkl},
\]

四个逆度量贡献 \(+8a|\mathrm{Rm}|^2\)，两个曲率张量贡献
\(-4a|\mathrm{Rm}|^2\)，故

\[
\partial_t|\mathrm{Rm}|^2=4a|\mathrm{Rm}|^2.
\]

四维体积元满足 \(\partial_td\mu=-4a\,d\mu\)，从而

\[
\partial_t\bigl(|\mathrm{Rm}|^2d\mu\bigr)=0.
\]

对 \(F=(1+|\mathrm{Rm}|^2)^{1/2}\)，Step 25 式 (2.4)

\[
\left.\partial_t(F^pd\mu)\right|_{-2ag}
=2a\bigl[(p-2)F^p-pF^{p-2}\bigr]d\mu
\]

也可直接复算得到。特别地，\(p=2\) 时只剩常数 \(1\) 的体积变化，并不存在 \(-4aF^2\) 型耗散。

### 2. \(q=2,3\) 曲率能量和二次缺陷能量有完整张量依据

A01 的 `tensor_energy_derivation.md` 逐指标支持

\[
\begin{aligned}
H_2'+cD_2&\le C\int\eta^2aF^3+Cr^{-2}H_2,\\
H_3'+cD_3&\le Cr^{-2}H_3+C\int\eta^2a^2F^4,\\
Q'+cX&\le Cr^{-2}Q+C\int\eta^2aF|E|^2.
\end{aligned}
\]

其中严格缓冲条件使所有含 \(a\,d\eta\) 或 \(da\,d\eta\) 的项消失；Hessian-\(a\) 项经一次分部积分后只留下

\[
\frac{|da|^2}{a}=4|d\chi|^2.
\]

缺陷方程

\[
(\partial_t-a\Delta)|E|^2
=-2a|\nabla E|^2+4a\mathrm{Rm}(E,E)
+2\langle E,\mathcal C_a(E)\rangle
\]

是齐次的：若 \(E=0\)，速度和缺陷演化均为零。因而缺陷估计中没有纯曲率源项。这一点对于保留初始 \(\delta^6\) 因子至关重要。

### 3. 固定截断幂次与 Yang 迭代完全匹配

Yang 附录 A 在四维使用

\[
p_{j+1}=\frac32p_j,\qquad
p'_{j+1}=\frac32p'_j+1.
\]

从 \(p'_0=p_0-2\) 出发确有 \(p'_j=p_j-2\)，所以

\[
\chi^{2p'_j}\Phi^{p_j}=a^{p_j-2}\Phi^{p_j}=K_{p_j}[\Phi],
\]

且 \(p_j\to\infty\) 时得到

\[
\chi^{2p'_j/p_j}\Phi\longrightarrow \chi^2\Phi=a\Phi.
\]

势函数取 \(q=6\) 时，Yang 所需量正是

\[
\int \chi^{q-4}F^{q/2}=\int aF^3=H_3.
\]

因此 Step 25 的迭代确实作用于整个过渡环带，而不只是平台。

### 4. 权重代数没有发现错误

式 (4.4)

\[
a^{p-1}F\Phi^p
=(aF^3)^{1/3}
\bigl(a^{3p/2-2}\Phi^{3p/2}\bigr)^{2/3}
\]

以及

\[
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}
\]

都正确。虽然

\[
Z_p=\eta a^{(p-1)/2}\Phi^{p/2}
\]

表面上含 \(\eta^4\)，但所有 \(K_{2p}\) 项都由正次幂 \(a\) 支撑，而该区域上 \(\eta=1\)，故

\[
K_{2p}^{1/2}=\|Z_p\|_4^2
\]

成立。

---

## 三、需要修正的一处参数记号

Step 25 把

\[
\beta(t)=\mathsf S\|F(t)\|_{L^2(\operatorname{supp}\chi)}
\]

用于式 (3.2)，但 \(H_2\) 是在较大的辅助区域上积分：

\[
H_2=\int\eta^2F^2.
\]

从 \(q=2\) 和 \(q=3\) 方程直接得到的精确形式是

\[
H_3(t)\le
\frac{C\,\beta_*\,H_2(0)}{t},
\]

从而

\[
\mathsf S^2H_3(t)
\le
\frac{C\,\beta_*\,b_0^2}{t},
\qquad
b_0:=\mathsf S H_2(0)^{1/2}.
\]

要写成 \(C\beta_*^3/t\)，还需要

\[
b_0\le C\beta_*.
\]

Step 23 给出了辅助区域整体的初始 maximal-function 控制，但没有直接给出辅助区域曲率能量与活动支撑曲率能量的双向比较。最简洁的处理是改用

\[
\bar\beta(t):=\mathsf S H_2(t)^{1/2}.
\]

它同时控制临界吸收系数，因为

\[
\|F\|_{L^2(\operatorname{supp}\chi)}
\le H_2^{1/2}.
\]

于是

\[
\mathsf S^2H_3(t)\le \frac{C\bar\beta_*^3}{t},
\qquad
\|a\mathrm{Rm}(t)\|_\infty
\le C\frac{\bar\beta_*}{t}.
\]

这只是参数整理，不破坏首次逸出机制，但 Step 25 当前写法需要补上该比较或采用 \(\bar\beta\)。

---

## 四、整个活动支撑上的估计是否真正闭合首次逸出

在已有光滑解且临界能量保持小时，链条如下。

### 1. 曲率势和缺陷基准量

由 \(H_2\) 持续性、固定 \(q=3\) 传播以及上面的参数修正，

\[
\mathsf S^2H_3(s)\le
C\bar\beta_*^3s^{-1}.
\]

齐次缺陷能量给出

\[
J_6(s)=\int\eta^2a^4|E|^6
\le e^{Cs/r^2}J_6(0)
\le C\delta^6V.
\]

### 2. 整个活动支撑上的点态量

以 \(p_0=3\) 和 \(p_0=6\) 分别启动固定截断迭代，可得

\[
\|a\mathrm{Rm}(t)\|_\infty
\le C\frac{\bar\beta_*}{t},
\]

以及

\[
\|aE(t)\|_\infty
\le C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]

第二式在 \(t=0\) 可积：

\[
\int_0^{\theta r^2}\|aE(s)\|_\infty ds
\le \frac32C\delta\,\theta^{2/3}r^2.
\]

### 3. 度量、Sobolev 和一阶截断量

由 \(\partial_tg=-2aE\)，

\[
e^{-2I(t)}g_0\le g(t)\le e^{2I(t)}g_0,
\qquad
I(t)=\int_0^t\|aE(s)\|_\infty ds.
\]

因此当 \(\delta\theta^{2/3}r^2\) 足够小时：

- 固定区域上的体积元与初始体积元可比较；
- 相对 Sobolev 不等式由初始度量转移到 \(g(t)\)；
- \(|d\chi|_{g(t)}\) 由 \(|d\chi|_{g_0}\) 控制；
- 初始球与固定支撑之间有正余量时，距离比较保持所需包含关系；
- \(H_2\) 的估计重新控制 \(\bar\beta(t)\)。

所以，**全支撑 \(\|aE\|_\infty\) 确实补上了首次逸出中的低阶闭环**。平台估计无法替代它，因为过渡环带同样满足 \(\partial_tg\ne0\)。

不过，双 Lipschitz 比较只能控制 \(|d\chi|\)，不能直接控制
\(\nabla^2\chi,\nabla^3\chi,\ldots\)。这些高阶量不参与 Step 25 的弱能量闭环，却参与 Wang 的光滑延拓归纳。

---

## 五、一般 \(p\) 能量式仍需独立写出

A01 的逐指标文件完整处理了 \(q=2,3\) 和二次缺陷能量，但没有推导 Step 25 的一般式

\[
\frac d{dt}K_p+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p
+Cp\int\eta^2a^{p-1}F\Phi^p.
\tag{4.2}
\]

Yang 的附录验证了固定截断迭代的幂次结构，却不能自动替代当前张量方程中：

- 演化度量下的张量范数变化；
- 体积元变化；
- Hessian-\(a\) 的一次分部积分；
- \(|E|\) 平滑正则化后令正则化参数趋零；
- 常数关于 \(p\) 的多项式控制。

这些结构都与式 (4.2) 相容，没有发现权重冲突，但完整证明应把它们统一写成一个一般 \(p\) 引理。\(J_6\) 持续性和后续两次 Moser 迭代都依赖这一引理。

---

## 六、归一化 Yang–Wang 延拓需要哪些量

设 \(T>0\)，并且在 \([T/2,T)\) 上

\[
\sup |a\mathrm{Rm}|<\infty.
\]

由于

\[
|aE|\le C_n|a\mathrm{Rm}|+C_na,
\]

立刻有 \(|aE|\) 有界，故度量在 \(T\) 前保持一致等价。这也给出统一 Sobolev 系数和 \(|d\chi|\)。

但光滑延拓还需要 Wang 体系中的高阶量：

\[
\|\mathrm{Rm}\|_{L^p},\qquad
\|\nabla^m(a\mathrm{Rm})\|_{L^p},
\qquad
\|\nabla^m\chi\|_{L^p},
\qquad
\|\nabla^{m-1}\mathrm{Rm}\|_{L^p},
\]

最终再借 Sobolev 嵌入得到

\[
\|\nabla^m(a\mathrm{Rm})\|_\infty<\infty.
\]

这些是 Wang 论文 Theorem 4.1、Lemmas 4.10–4.14 中相互耦合的量。双 Lipschitz 比较不能替代该归纳。

### 加入 \(-2ag\) 后的结构

主符号仍是 \(a\Delta\)，所以 DeTurck 正则化仍适用。新增项主要有两类：

1. 全协变曲率和范数变化中的 \(a\mathrm{Rm}\) 型零阶项；
2. 空间变化的 \(a\) 产生的 \((\nabla^2a)*g\) 及其高阶导数。

与局部 Ricci 部分合并后，Hessian 项可写成

\[
(\nabla^2a)*E,
\]

而

\[
E=\mathrm{Ric}+g,\qquad \nabla E=\nabla\mathrm{Ric}.
\]

其中 \(g\) 部分产生固定截断的加性项。以非加权 \(L^p\) 曲率为例，

\[
\int |\mathrm{Rm}|^{p-2}\mathrm{Rm}*(\nabla^2a)*g
\]

经一次分部积分后由

\[
\varepsilon\int a|\mathrm{Rm}|^{p-2}|\nabla\mathrm{Rm}|^2
+
C_\varepsilon\int \frac{|da|^2}{a}
\bigl(1+|\mathrm{Rm}|^p\bigr)
\]

控制。由于 \(|da|^2/a=4|d\chi|^2\)，这不会引入新的独立点态曲率假设。

因此，现有证据支持下面的数学预期：

> 对固定光滑 \(a=\chi^2\) 和紧致初始流形，\(\sup|a\mathrm{Rm}|<\infty\) 应仍足以推出归一化局部流光滑延拓；\(-2ag\) 只改变 Wang 归纳中的低阶及加性项。

但该结论尚未由所给文件完整推导。需要写出归一化版本的 Wang Lemmas 4.4–4.6、4.10–4.14，并证明所有常数在 \(t\uparrow T\) 时保持有限。这里没有看出还需额外的几何小量；缺少的是高阶估计链本身。

---

## 七、Step 6 的终端局部矛盾

设四维 Einstein 局部极限满足

\[
\mathrm{Ric}=-g,\qquad s=-4,\qquad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Einstein 条件给出 \(\delta W^+=0\)。令 \(\omega\) 张成简单特征线，则

\[
W^+=\mu I+(\lambda-\mu)P_\omega.
\]

因特征值常数且 \(\lambda\ne\mu\)，\(\delta W^+=0\) 给出

\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\]

与 \(\omega^{cd}\) 收缩并用 \(|\omega|^2\) 常数，得到

\[
\nabla^a\omega_{ab}=0.
\]

代回后

\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]

非零自对偶二形式在四维非退化，故

\[
\nabla\omega=0,\qquad \nabla W^+=0.
\]

另一方面，

\[
|W^+|^2=\frac1{24},\qquad
\det W^+=-\frac1{864}.
\]

Einstein–Weyl 恒等式

\[
\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]

在常谱情形给出

\[
0
=2|\nabla W^+|^2-\frac16+\frac1{24}
=2|\nabla W^+|^2-\frac18,
\]

即

\[
|\nabla W^+|^2=\frac1{16},
\]

与 \(\nabla W^+=0\) 矛盾。

这就是目前充分成立的终端局部机制。因为

\[
\mathrm{Rm}=W^++W^-+\text{标量部分},
\]

即使 \(W^+\) 平行，\(W^-\) 仍可能不平行，所以不能推出
\(\nabla\mathrm{Rm}=0\)，也不能调用局部对称空间分类。

---

## 八、与 Yau 第 26 题的关系

上述结果建立的是四维、\(\mathrm{Ric}\approx-g\) 的 Ishida–LeBrun 构造中一个关键平滑—紧致性部件。它尚未推出“对每个 \(n\ge2\) 存在统一 \(c_n<C_n\)”的完整命题，也尚未给出其反例。若归一化延拓归纳、首次逸出常数配置以及正时间极限向 Step 6 常谱 Einstein germ 的传递全部写成严格定理，这条四维路线才形成可用于原命题的完整反证链。