# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 50,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step50_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step50_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the source-based short-time existence argument in the Step 50 note for the degenerate normalized cutoff flow ∂t g=-2χ²(Ric+g). Read Yang's actual Theorem 8.2 lines 785–823 and the Step 44/Step 50 notes. Check the exact Eulerian variation δ[-2(χ∘φ^{-1})² ĝ], its placement in Yang's displayed D h+E ψ slots, and whether the stated Sobolev product/composition estimates genuinely preserve Yang's neighborhood-uniform smooth-tame inverse and unchanged finite derivative loss. Identify any missing term, regularity index, circularity, or unjustified passage. This should be a direct mathematical verification, not a generic review.

## Integrated Scientific Memo

## 核验结论

Step 50 对新增归一化项的**一阶变分、低阶槽位归属和主微分阶比较均正确**；它确实给出对 Yang 构造的合理增量扩张。但现有材料尚不足以证明 Step 50 所声称的、完整意义下的“邻域一致光滑 tame 逆保持不变”。准确结论应是：

> 归一化项是 Yang 线性系统的零阶 smooth-tame 扰动，不增加原系统所需的最大微分阶；在重新直接构造正则化线性逆时，它产生可控且与 \(\varepsilon\) 无关的能量项。因此，若补齐 Yang 原文压缩为 “standard arguments” 的邻域一致 tame 逆证明，则归一化短时存在成立，并且无需增加原有有限导数损失。  
> 但该完整补齐并未出现在 Yang 785–823 行、Step 44 或 Step 50 中。

### 1. 精确 Eulerian 变分

令
\[
\widehat\chi=\chi\circ\varphi^{-1},\qquad
\widehat a=\widehat\chi^2,\qquad
h=\delta\widehat g,\qquad
\zeta=\delta\varphi\circ\varphi^{-1}.
\]
由
\[
\delta\varphi^{-1}=-d\varphi^{-1}(\zeta)
\]
得到
\[
\delta\widehat\chi=-d\widehat\chi(\zeta),\qquad
\delta\widehat a=-2\widehat\chi\,d\widehat\chi(\zeta).
\]
所以
\[
\boxed{
\delta(-2\widehat a\,\widehat g)
=-2\widehat a\,h
+4\widehat\chi\,d\widehat\chi(\zeta)\,\widehat g.}
\]

符号和系数 \(4\) 均正确。这里没有遗漏：

* \(\widehat a\) 依赖 \(\varphi\)，不依赖 \(\widehat g\)，故 \(\delta\widehat a\) 中没有 \(h\)；
* \(d\widehat\chi\) 是标量函数的外微分，不随度量变化；
* 新项不含 \(\nabla h\) 或 \(\nabla\zeta\)；
* diffeomorphism 方程本身没有新增变分项，只是其系数沿归一化后的参考解取值。

若 Yang 图表中的 \(\psi\) 是 Lagrangian 表示，则应明确写成
\[
\zeta=R_\varphi\psi=\psi\circ\varphi^{-1}.
\]

### 2. 在 Yang 系统中的槽位

新增线性算子正是
\[
K_u(h,\psi)=
\left(
-2\widehat a h+
4\widehat\chi\,d\widehat\chi(R_\varphi\psi)\widehat g,\;0
\right).
\]
因此它只改变
\[
D\mapsto D-2\widehat a\,\mathrm{Id},
\]
以及
\[
E\psi\mapsto E\psi+
4\widehat\chi\,d\widehat\chi(R_\varphi\psi)\widehat g.
\]
这与 Yang 展示的 \(Dh+E\psi\) 类型完全一致；主项
\[
2\widehat\chi^2\Delta h
\]
及一阶 \(B,C,P,Q,R\) 结构不变。

原系统本身已经含有相同的 transported-composition 类型。例如变分
\[
-2\widehat a\,\operatorname{Ric}_{\widehat g}
\]
会产生
\[
4\widehat\chi\,d\widehat\chi(\zeta)
\,\operatorname{Ric}_{\widehat g},
\]
而 gauge 项的 \(\varphi\)-变分也含 \(\delta\widehat a\)。归一化新增项在微分阶上反而更弱。

拉回也无问题：
\[
\varphi^*(\widehat a\,\widehat g)=\chi^2g,
\]
故 Yang 原有 gauge cancellation 给出
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]

### 3. 必须明确的 Sobolev 分级

Step 50 的无分量记号 \(\|u\|_{H^{s+r}}\) 隐藏了一个正则性指标。由于新系数含
\[
d(\chi\circ\varphi^{-1}),
\]
自然分级应至少是
\[
\|u\|_s^*
=\|\widehat g\|_{H^s}
+\|\varphi\|_{H^{s+1}},
\]
或在统一分级中明确令 \(r\ge1\)。相应地，
\[
\|d(\chi\circ\varphi^{-1})\|_{H^s}
\le C_{s,\mathcal U}
\bigl(1+\|\varphi\|_{H^{s+1}}\bigr).
\]

在 \(s_0>n/2+2\) 且 \(\varphi\) 位于固定 \(H^{s_0+1}\) 微分同胚邻域时，Moser 乘积、复合、取逆和右平移估计给出
\[
\|K_u(h,\psi)\|_{H^s}
\le C_{\mathcal U}\|(h,\psi)\|_{H^s}
+C_{s,\mathcal U}(1+\|u\|_s^*)
 \|(h,\psi)\|_{H^{s_0}}.
\]
所以新增项自身没有产生额外导数损失。Yang 原系数已经要求处理至少同样的 \(\varphi\)-导数，以及来自曲率和 gauge 的更高 \(\widehat g\)-导数；故在微分阶比较意义下，“原有限损失无需增大”是可信且正确的。Yang 原文没有给出损失的数值，因而不能声称核验了某个具体 \(r\)。

### 4. 能量估计与线性正则化

在第 \(s\) 阶能量中，
\[
\left|
\langle\nabla^sh,\nabla^sK_u(h,\psi)\rangle
\right|
\le
C_{\mathcal U}\mathcal E_s
+C_{s,\mathcal U}(1+\|u\|_s^*)
\mathcal E_{s_0}^{1/2}\mathcal E_s^{1/2}.
\]
这里没有 \(s+1\) 阶未知量，因此不与
\[
\|\widehat\chi\nabla^{s+1}h\|_2^2
\]
竞争，常数也与线性正则化参数 \(\varepsilon\) 无关。故对
\[
L_u+K_u+\varepsilon^2\Delta_h
\]
直接重做 Yang 的正则化能量论证时，新增项可由 Gronwall 和高低阶 tame 分配处理。

一个重要逻辑修正是：仅有上述乘积估计，**不能**直接推出
\[
(L_u+K_u)^{-1}
\]
存在；现有材料没有证明 \(\|L_u^{-1}K_u\|<1\)。正确路线是直接求解被 \(K_u\) 扰动后的正则化系统，获得 \(\varepsilon\)-一致估计，再令 \(\varepsilon\to0\)。

### 5. 源文没有实际核验掉的部分

Yang 785–823 行只说 smooth-tame estimates 来自 “standard arguments”。它没有展示：

1. 非齐次 forcing \(f,\eta\) 的逆估计；
2. time-dependent tame norms；
3. 对参考对 \((\widehat g,\varphi)\) 的邻域一致常数；
4. 参数差分和高阶 Fréchet 导数估计；
5. 数值化的有限导数损失；
6. \(\psi\)-输运主符号的显式对称化结构。

尤其 Step 44 的
\[
\int\langle\nabla^k\psi,
\widehat aV^i\nabla_i\nabla^k\psi\rangle
\]
估计要求 \(P\nabla\psi\) 真的是沿向量场的输运，或至少具有平滑对称化子。Yang 的展示式没有给出 \(P\)，Step 44 也没有从精确 diffeomorphism 方程完整推导这一点。因此这不是已独立验证的事实，而是 Yang 压缩论证的一部分输入。

同样，Step 50 所说“差分参考对也满足相同估计”和“smooth-tame dependence proceeds”需要对扰动方程作参数差分及高阶参数微分归纳；笔记没有写出该归纳。

### 6. 最终判定

没有发现归一化项的遗漏、符号错误、错误槽位或新的微分损失。该直接 Yang 路线也没有使用非线性 \(a+\varepsilon^2\) 流，因此避开了 Step 49 的 cutoff-jet 循环性。

但 Step 50 的 Theorem 2.1 应表述为：

> **条件性严格归约：**在导入并适用于参考对邻域的 Yang smooth-tame 线性逆理论后，新增项 \(-2\widehat a\widehat g\) 保持其主结构及有限导数损失，因而得到归一化退化流的逐数据短时存在与重启。

若要求从所引 785–823 行本身得到完全自足证明，则尚缺的精确数学对象是：带 staggered Sobolev grading 的非齐次正则化 coupled system 的邻域一致 smooth-tame inverse，包括 \(\psi\)-输运对称化、参数差分、高阶参数导数及 \(\varepsilon\to0\) 的统一 time-norm 紧性。现有 Step 44/50 只验证了新增归一化项不会恶化这些估计，并未完整重建它们。