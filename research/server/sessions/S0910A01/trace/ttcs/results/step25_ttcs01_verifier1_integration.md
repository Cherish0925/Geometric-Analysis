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
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step25_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step25_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the q=2 curvature energy derivation in workspace/notes/step25_tensor_energy_derivation.md. The note claims that under the buffered cutoff flow d_t g = -2 chi^2(Ric+g) on a closed 4-manifold with supp(chi) compactly inside {eta=1} and supp(grad eta) in {chi=0}, the energy H_2 = int eta^2 F^2 dmu satisfies H_2' + c D_2 <= C int(eta^2 a F^3) + C r^{-2} H_2, where D_2 = int(eta^2 a |grad Rm|^2). Check: (1) Is the term classification (Types A-D, metric variation, volume form) complete? Are there missing terms from the curvature variation formula under h = -2aE? (2) Is the integration by parts of the Hessian(a) terms correct? Does the cross term grad a . grad eta genuinely vanish? (3) Are the Young inequality absorptions correct with the coefficient |grad a|^2/a = 4|grad chi|^2? (4) Is the global defect identity Q_global(t) <= e^{C theta} Q_global(0) correct? (5) For the first-exit Approach A: is it correct that the short-time existence interval theta r^2 <= c/K_0 is compatible with the maximal-function good center hypothesis K_0 ~ r^{-2}? Identify any errors, missing terms, or logical gaps.

## Integrated Scientific Memo

# 核验结论

## 总判定

在假设：

- 流在所讨论时间段内光滑存在；
- \(\chi,\eta\) 是固定的时间无关函数；
- 相对于 \(g(t)\) 有 \(|\nabla\chi|\le Cr^{-1}\)（例如由度量可比性推出）；
- \(\operatorname{supp}\chi\Subset\{\eta=1\}\)，且
  \(\operatorname{supp}d\eta\subset\{\chi=0\}^{\circ}\)；

则目标 \(q=2\) 不等式在**张量示意层面成立**：

\[
\boxed{
H_2'(t)+cD_2(t)
\le
C\int_M\eta^2aF^3\,d\mu
+Cr^{-2}H_2(t),
}
\]

其中

\[
H_2=\int_M\eta^2F^2\,d\mu,\qquad
D_2=\int_M\eta^2a|\nabla\mathrm{Rm}|^2\,d\mu.
\]

但原笔记有两个明确的局部错误，并且 first-exit Approach A 存在实质性逻辑缺口。

---

## 1. 曲率变分项是否完整

对一般变分 \(h=\partial_tg\)，全降指标曲率张量满足

\[
D\mathrm{Rm}(h)
=
\frac12\mathcal S(\nabla^2h)+\mathrm{Rm}*h.
\]

代入

\[
h=-2aE,\qquad E=\mathrm{Ric}+g,
\]

并展开

\[
\nabla^2(aE)
=
a\nabla^2E+(\nabla a)*\nabla E+(\nabla^2a)*E,
\]

得到

\[
\partial_t\mathrm{Rm}
=
a\Delta\mathrm{Rm}
+a\,\mathrm{Rm}*\mathrm{Rm}
+(\nabla a)*\nabla E
+(\nabla^2a)*E
+a\,\mathrm{Rm}*E,
\]

其中 \(a\nabla^2\mathrm{Ric}\) 经 Bianchi 恒等式和协变导数交换化为
\(a\Delta\mathrm{Rm}+a\,\mathrm{Rm}*\mathrm{Rm}\)。

规范化部分 \(E=\mathrm{Ric}+g\) 中的 \(g\) 贡献：

\[
(\nabla^2a)*g,\qquad a\,\mathrm{Rm}*g,
\]

分别已包含在 Type C 与 Type D/低阶代数项中。因此 Types A–D 没有漏项；原文只是把 \((\nabla^2a)*g\) 同时在 A、C 的讨论中出现，属于分类重叠，不是遗漏。

此外：

- 逆度量变分给出
  \[
  aE*\mathrm{Rm}*\mathrm{Rm},
  \]
  由 \(CaF^3\) 控制；
- 体积形式变分
  \[
  \partial_td\mu=-a\,\operatorname{tr}E\,d\mu
  \]
  也由 \(CaF^3\) 控制；
- \(a,\eta\) 是固定标量函数，因此没有 \(\partial_ta,\partial_t\eta\) 项；
- \(F^2=1+|\mathrm{Rm}|^2\) 中常数 \(1\) 只通过体积形式变化。

所以项分类在示意层面完整。不过脚本没有验证完整指标公式；正式证明仍应写出 Bianchi 化简，以锁定主项系数确为

\[
2a\langle\mathrm{Rm},\Delta\mathrm{Rm}\rangle
=
a\Delta|\mathrm{Rm}|^2-2a|\nabla\mathrm{Rm}|^2.
\]

---

## 2. \(\nabla^2a\) 项分部积分

原文 (0.2) 的 Hessian 公式写错。正确张量恒等式是

\[
\boxed{
\nabla^2a
=
2\,d\chi\otimes d\chi+2\chi\nabla^2\chi,
}
\]

而不是 \(2|\nabla\chi|^2+2\chi\nabla^2\chi\)。

对典型项

\[
I_C=\int_M\eta^2(\nabla_i\nabla_j a)T^{ij}\,d\mu
\]

分部积分得到

\[
I_C
=
-\int_M\eta^2(\nabla_j a)\nabla_iT^{ij}\,d\mu
-2\int_M\eta(\nabla_i\eta)(\nabla_j a)T^{ij}\,d\mu.
\]

这里第二项并不一般等于
\((\nabla a\cdot\nabla\eta)T\)，所以单纯说“两梯度正交”并不充分。它消失的真正理由更强：

\[
d\eta(x)\neq0
\implies \chi(x)=0
\implies da(x)=2\chi(x)d\chi(x)=0.
\]

因此无论 \(T^{ij}\) 如何收缩，交叉项均逐点为零。

主项中

\[
T=\mathrm{Rm}*E\quad\text{或}\quad \mathrm{Rm}*g,
\]

从而

\[
|\nabla T|
\le
C\bigl(
|\nabla\mathrm{Rm}|\,|E|
+|\mathrm{Rm}|\,|\nabla E|
+|\nabla\mathrm{Rm}|
\bigr)
\le CF|\nabla\mathrm{Rm}|.
\]

所以 Type C 确实满足

\[
|I_C|
\le
\varepsilon D_2+C_\varepsilon r^{-2}H_2.
\]

---

## 3. Young 吸收及 (2.11) 的符号错误

最稳妥的写法是不在 \(a=0\) 处使用形式商：

\[
|da|=2|\chi||d\chi|=2\sqrt a\,|d\chi|.
\]

故

\[
C|da|F|\nabla\mathrm{Rm}|
\le
\varepsilon a|\nabla\mathrm{Rm}|^2
+C_\varepsilon |d\chi|^2F^2
\le
\varepsilon a|\nabla\mathrm{Rm}|^2
+C_\varepsilon r^{-2}F^2.
\]

这等价于在 \(\{a>0\}\) 使用

\[
\frac{|da|^2}{a}=4|d\chi|^2,
\]

并连续延拓到 \(a=0\)。

该估计可用于：

1. 加权 Bochner 项积分分部后的 \(da\) 项；
2. Type B；
3. Type C 分部积分后的主项。

但原文 (2.11) 的不等号方向与后续 (2.12) 不一致。需要的是上界

\[
\boxed{
\int_M\eta^2a\Delta|\mathrm{Rm}|^2\,d\mu
\le
\varepsilon D_2
+\frac{C}{\varepsilon r^2}H_2.
}
\]

原文写成了下界。由于此前实际获得的是绝对值估计，上下界都成立，因此修正后 (2.12) 和最终结论仍成立。

多个张量收缩的维数常数应纳入 \(C_\varepsilon\)。给三类误差分别指定耗散预算 \(\varepsilon_iD_2\)，令

\[
\sum_i\varepsilon_i=\delta_0<2,
\]

即可得到

\[
H_2'+(2-\delta_0)D_2
\le
C\int\eta^2aF^3+Cr^{-2}H_2.
\]

脚本中的 \(2-3\varepsilon\) 仅是示意 bookkeeping，不是指标级常数验证。

---

## 4. 全局 defect 估计

令各缓冲域两两不交，并定义真正受局部估计控制的量

\[
q_j(t)=\int_M\eta_j^2|E|^2\,d\mu_t.
\]

因为 \(\eta_j=1\) 于 \(\operatorname{supp}a_j\) 的邻域，而
\(d\eta_j\neq0\) 的 collar 上 \(a_j=0\)，该 collar 的度量、\(E\) 和体积形式均不变。因此

\[
Q_{\mathrm{global}}(t)-Q_{\mathrm{global}}(0)
=
\sum_j\bigl(q_j(t)-q_j(0)\bigr).
\]

若

\[
q_j(t)\le e^{Ct/r^2}q_j(0),\qquad t\le\theta r^2,
\]

则

\[
Q_{\mathrm{global}}(t)
\le
Q_{\mathrm{global}}(0)
+(e^{C\theta}-1)\sum_jq_j(0).
\]

由缓冲域不交及 \(0\le\eta_j\le1\)，

\[
\sum_jq_j(0)\le Q_{\mathrm{global}}(0),
\]

所以

\[
\boxed{
Q_{\mathrm{global}}(t)
\le e^{C\theta}Q_{\mathrm{global}}(0).
}
\]

结论正确，但必须明确：

- \(q_j\) 是上述带权局部能量；
- buffered domains 两两不交；
- collar 的静止性用于精确差分恒等式。

若支持重叠，只能得到带重数常数的版本。

---

## 5. First-exit Approach A 不成立于当前假设下

这是主要逻辑缺口。

### 5.1 最大函数假设只给平均 \(L^2\) 控制

已知的是

\[
\mathcal M_{R_0}(|\mathrm{Rm}|^2)(p)\le K_0,
\]

故

\[
\fint_{B_\rho(p)}|\mathrm{Rm}|^2\le K_0.
\]

它不推出

\[
\sup_{B_{L_\chi r}(p)}|\mathrm{Rm}|\lesssim r^{-2}.
\]

平均曲率很小仍允许小区域中出现任意高的 Weyl 曲率峰；而
\(|E|=|\mathrm{Ric}+g|\le\delta\) 也不控制 Weyl 部分。

短时存在尺度 \(c/K\) 中的 \(K\) 应是点态曲率上界
\(K=\sup|\mathrm{Rm}|\)，不是 \(|\mathrm{Rm}|^2\) 的平均值。此外，对退化 cutoff 方程也不能直接援引标准全局 Ricci flow 定理；需要专门的局部/退化抛物存在定理，并追踪其对

\[
\sup|\mathrm{Rm}|,\quad r^{-1},\quad r^{-2}
\]

的依赖。

### 5.2 \(K_0\) 的量纲使用错误

这里 \(K_0\) 控制的是 \(|\mathrm{Rm}|^2\)，量纲为 \(L^{-4}\)。因此正确的曲率尺度关系应是

\[
\sqrt{K_0}\sim r^{-2},
\]

而不是 \(K_0\sim r^{-2}\)。若另有点态曲率界
\(\sup|\mathrm{Rm}|\lesssim\sqrt{K_0}\)，短时尺度才是

\[
t\lesssim \frac1{\sqrt{K_0}}\sim r^2.
\]

而且 Step 24 的吸收条件是

\[
\beta_0\lesssim r^2\sqrt{1+K_0}\ll1.
\]

若取临界关系 \(K_0\sim r^{-4}\)，则
\(r^2\sqrt{K_0}\sim1\)，不自动小。因而“临界尺度兼容短时存在”和“通过缩小 \(r\) 使 \(\beta_0\) 小”不是同一套无条件成立的论证。

### 5.3 位移并非由 \(\delta\) 自动控制

仅凭光滑性不能得到统一的

\[
E(t)-E(0)=O(\delta).
\]

若另有 \(\sup|\mathrm{Rm}|\lesssim r^{-2}\) 及相应导数估计，可由齐次 defect 方程期待

\[
\|E(t)\|_\infty
\lesssim
e^{C(r^{-2}+1)t}\|E(0)\|_\infty,
\]

从而在 \(t\lesssim r^2\) 上保持 \(E=O(\delta)\)，并得到小的度量位移。但这些点态与导数估计正是当前缺失的输入，不能由最大函数 good-center 条件直接推出。

因此

\[
\theta r^2\le c/K_0
\]

在原记号下既量纲错误，也未由现有假设建立。Approach A 不能作为已闭合的 F3 证明。

---

## 附带的 first-exit 缺口

从 F1、F3 只得到

\[
\beta_a(t)
\le C_{\rm met}\sqrt2\,\beta_0.
\]

原 bootstrap 阈值为 \(2\beta_0\)，但粗略度量可比性
\(\frac12g_0\le g(t)\le2g_0\) 并不保证

\[
C_{\rm met}\sqrt2<2.
\]

需要采用更大的 bootstrap 因子并相应缩小初始 \(\beta_0\)，或者使用更紧的度量可比性范围。

---

## 最终核验

- **Types A–D、norm variation、volume variation：** 完整，无漏项；但精确 Bianchi 指标推导尚未写出。
- **Hessian 分部积分：** 方法正确；原 Hessian 公式需改为张量公式。交叉项因 \(da=0\) 于 \(\operatorname{supp}d\eta\) 而消失。
- **Young 吸收：** 正确；应避免在 \(a=0\) 处直接除以 \(a\)。原 (2.11) 不等号方向错误，但不影响修正后的最终不等式。
- **全局 defect：** 在局部带权能量、静止 collar、缓冲域不交的条件下正确。
- **Approach A：** 未被 good-center 最大函数假设支持；存在平均量与点态量混用、量纲错误及短时存在定理缺失。

要修复 Approach A，需要额外证明一种适用于该 cutoff flow 的 \(\varepsilon\)-正则性/局部存在结果，将真正的小尺度临界能量条件转化为

\[
\sup_{\operatorname{supp}\chi}|\mathrm{Rm}(t)|\lesssim r^{-2}
\]

及相应 Shi 型导数界，并明确所需的小量条件是否确实由所选 good centers 满足。