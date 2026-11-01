# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 44,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step44_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step44_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the normalized transported-coefficient Yang/DeTurck start-restart construction in Step 44 against Yang Theorem 8.2 itself. Focus on mathematical sufficiency: exact pullback/gauge transport; variation delta(a_hat) with the diffeomorphism variable; the coupled H^k energy estimate for Yang's linearized metric-transport system with epsilon^2 Delta h; whether integration by parts removes derivative loss in chi C nabla psi; whether constants are uniform in epsilon; whether these estimates really give the smooth tame inverse needed by Yang's fixed-point/Nash-Moser argument after adding -2 a_hat g_hat; coupled uniqueness when transported coefficients differ; and restart from a smooth endpoint. Identify any missing regularity, derivative, compatibility, or nonlinear argument. The goal is a rigorous scientific verdict, not a generic review.

## Integrated Scientific Memo

# Step 44 核验结论

## 总判定

Step 44 对新增归一化项
\[
-2\widehat a\,\widehat g,\qquad
\widehat a=(\chi\circ\varphi^{-1})^2
\]
的**增量分析基本正确**：

- 它不改变 Yang 的规范消去与拉回方程；
- 其线性化对 \((h,\psi)\) 是零阶光滑 tame 扰动；
- \(\widehat\chi C\nabla\psi\) 的表面导数损失可由一次分部积分消除；
- 线性正则项 \(\varepsilon^2\Delta h\) 可取得与 \(\varepsilon\) 无关的 Sobolev 能量估计；
- transported coefficient 不同的两个解必须进行 \((\widehat g,\varphi)\) 联立唯一性估计。

但按照现有文本，Step 44 **尚未独立证明 Yang 非线性构造真正需要的 smooth tame inverse**。Yang Theorem 8.2 的原文自身只说 tame estimates 来自“standard arguments using energy integrals and interpolation inequalities”，并没有给出这些估计。Step 44 写出了关键的同阶 \(H^k\) 估计，却仍缺少：

1. Yang 的 \(\psi\)-方程最高阶输运算子的明确可对称化结构；
2. 高—低范数 tame 估计及固定导数损失；
3. 线性逆关于参考对 \((\widehat g,\varphi)\) 的邻域一致 smooth-tame 依赖；
4. 相应时间半范数/高阶时间导数估计；
5. 几何唯一性所需的共同 Yang gauge 构造；
6. 终点重启时的严格光滑拼接论证。

因此，严格措辞应为：

> **归一化项保留 Yang 线性化系统的 principal、导数计数和 tame 结构；若完整导入 Yang Theorem 8.2 所声称的 smooth-tame inverse 机制，则 normalized start theorem 成立。Step 44 本身还不是该 inverse theorem 的自足证明。**

---

## 1. transported gauge 与精确拉回

Yang 原文的系统是
\[
\partial_t\widehat g
=-2\left[
\widehat a\,\operatorname{Ric}_{\widehat g}
-\widehat\delta^*
 \bigl(\widehat a S^{-1}\delta G(S)\bigr)
\right],
\]
连同其特定的 \(\varphi\)-方程。归一化后加入
\[
-2\widehat a\,\widehat g.
\]

设
\[
Z_t=\partial_t\varphi_t\circ\varphi_t^{-1}.
\]
Yang 的 gauge 约定给出
\[
\mathcal L_{Z_t}\widehat g
=-2\widehat\delta^*
 \bigl(\widehat aS^{-1}\delta G(S)\bigr).
\tag{1}
\]
于是
\[
\begin{aligned}
\frac d{dt}\varphi_t^*\widehat g
&=\varphi_t^*
  \left(\partial_t\widehat g+\mathcal L_{Z_t}\widehat g\right)\\
&=-2\varphi_t^*
  \left[\widehat a
  (\operatorname{Ric}_{\widehat g}+\widehat g)\right]\\
&=-2\chi^2(\operatorname{Ric}_{g}+g),
\end{aligned}
\tag{2}
\]
其中 \(g=\varphi_t^*\widehat g\) 且
\[
\varphi_t^*\widehat a
=(\chi\circ\varphi_t^{-1}\circ\varphi_t)^2=\chi^2.
\]

这里必须保留 Yang 对 \(S^{-1}\delta G(S)\)、sharp 和 pushforward 的原始 source/target 约定。仅凭 Step 44 的简写符号不能重新推导 (1)；最稳妥的写法是直接把 (1) 作为 Yang gauge 的定义性恒等式。将 \(\widehat a\) 放在 \(\widehat\delta^*\) 内部是必要的，因为
\[
2\widehat\delta^*(\widehat a\omega)
=\mathcal L_{(\widehat a\omega)^\sharp}\widehat g
\]
自动包含 \(d\widehat a\) 项，而
\(\widehat a\,\mathcal L_{\omega^\sharp}\widehat g\) 不包含这些项。

归一化项完全不参与 gauge 消去，因此这部分适配是严格正确的。

---

## 2. \(\delta\widehat a\) 的精确公式

令
\[
\zeta=\delta\varphi\circ\varphi^{-1}.
\]
则
\[
\delta\widehat\chi
=-\mathcal L_\zeta\widehat\chi
=-d\widehat\chi(\zeta),
\]
所以
\[
\boxed{\delta\widehat a
=-d\widehat a(\zeta)
=-2\widehat\chi\,d\widehat\chi(\zeta).}
\tag{3}
\]
因此
\[
\delta(-2\widehat a\,\widehat g)
=-2\widehat a\,h
+4\widehat\chi\,d\widehat\chi(\zeta)\,\widehat g.
\tag{4}
\]

这对 Eulerian diffeomorphism variation \(\zeta\) 是零阶的；若 Yang 的坐标变量记为 \(\psi=\delta\varphi\)，则
\(\zeta=\psi\circ\varphi^{-1}\)，外加所选 diffeomorphism chart 的光滑点态束映射。因此新增项只有
\[
\widehat\chi^2*h+
\widehat\chi\,d\widehat\chi*\psi,
\tag{5}
\]
没有 \(\nabla\psi\) 或 \(\nabla h\)，也没有 \(\widehat\chi^{-1}\)。

Step 44 的符号正确；Step 37 中把它写成正号并暗示可归入
\(\widehat\chi C\nabla\psi\) 不精确，应以 (3)–(5) 为准。

---

## 3. \(\varepsilon\)-一致的联立 \(H^k\) 估计

考虑
\[
\partial_th
=2\widehat\chi^2\Delta h+\varepsilon^2\Delta h
+\widehat\chi(B\nabla h+C\nabla\psi)
+\widetilde Dh+\widetilde E\psi+f,
\tag{6}
\]
以及 Yang 的 \(\psi\)-输运方程。取固定参考联络和测度。

### 3.1 退化扩散

最高阶部分满足
\[
2\langle\nabla^kh,\nabla^k(\widehat\chi^2\Delta h)\rangle
\le
-c\|\widehat\chi\nabla^{k+1}h\|_2^2
+C_k\|h\|_{H^k}^2.
\tag{7}
\]
分部积分产生的唯一最高阶 cutoff 导数是
\[
\nabla(\widehat\chi^2)=2\widehat\chi\,d\widehat\chi,
\]
故可直接由 weighted dissipation 吸收；不需除以
\(\widehat\chi\)。若至少两个导数落在系数上，则未知量的阶数至多为 \(k\)。

正则项给出
\[
-c\varepsilon^2\|\nabla^{k+1}h\|_2^2
+C_k\varepsilon^2\|h\|_{H^k}^2.
\tag{8}
\]
在 \(0<\varepsilon\le1\) 时常数与 \(\varepsilon\) 无关。

### 3.2 \(\widehat\chi C\nabla\psi\) 不产生导数损失

最高阶项
\[
I_k=\int\nabla^kh*
\widehat\chi C\nabla^{k+1}\psi
\]
经一次分部积分成为
\[
I_k=
-\int\widehat\chi C\nabla^{k+1}h*\nabla^k\psi
-\int\nabla(\widehat\chi C)\nabla^kh*\nabla^k\psi
+\text{低阶交换子}.
\]
所以
\[
|I_k|
\le
\rho\|\widehat\chi\nabla^{k+1}h\|_2^2
+C_{k,\rho}
\bigl(\|h\|_{H^k}^2+\|\psi\|_{H^k}^2\bigr).
\tag{9}
\]
闭流形假设消除了边界项。此处单个 \(\widehat\chi\) 因子正好与 metric dissipation 的权重匹配，这是整个估计闭合的关键。

### 3.3 \(\psi\)-输运项需要补充结构假设

Step 44 写的
\[
\int\nabla^k\psi*
\widehat\chi^2P\nabla^{k+1}\psi
\le C_k\|\psi\|_{H^k}^2
\tag{10}
\]
不能从任意矩阵 \(P\) 推出。必须使用 Yang 实际线性化中 \(P\nabla\psi\) 是输运型、或相对于某个平滑 symmetrizer 可对称化。若最高阶为
\[
\widehat a V^i\nabla_i\psi,
\]
则
\[
\int\langle\nabla^k\psi,
\widehat aV^i\nabla_i\nabla^k\psi\rangle
=
-\frac12\int\operatorname{div}(\widehat aV)
|\nabla^k\psi|^2+\text{低阶项}.
\tag{11}
\]
只有记录这一实际结构，(10) 才严格成立。

与 \(h\) 的耦合为
\[
\left|
\int\nabla^k\psi*
\widehat\chi^2Q\nabla^{k+1}h
\right|
\le
\rho\|\widehat\chi\nabla^{k+1}h\|_2^2
+C_{k,\rho}\|\psi\|_{H^k}^2.
\tag{12}
\]

### 3.4 新归一化项

由 tame 乘积估计，
\[
\|\widehat a h\|_{H^k}
+\|\widehat\chi\,d\widehat\chi(\zeta)\widehat g\|_{H^k}
\le C_k(\|h\|_{H^k}+\|\psi\|_{H^k}),
\tag{13}
\]
因此只增加 \(C_k\mathcal E_k\)。

综合后可得
\[
\frac d{dt}\mathcal E_k
+c_k\|\widehat\chi\nabla^{k+1}h\|_2^2
+c_k\varepsilon^2\|\nabla^{k+1}h\|_2^2
\le
C_k\mathcal E_k+
C_k\|(f,\eta)\|_{H^k}^2.
\tag{14}
\]
权重 \(A_k\) 与 Young 参数必须联合选择：先固定 \(A_k\)，再把由
\(A_k\)-加权输运耦合产生的 Young 参数取得足够小。不能只说“增大 \(A_k\)”而忽略该耦合也被乘以 \(A_k\)。这不影响结论，但应写明。

---

## 4. \(\varepsilon\downarrow0\) 与 smooth limit

(14) 在所有空间阶数上给出一致界。方程进一步给出
\[
\partial_t h_\varepsilon
\text{ 在 }H^{k-2}\text{ 中一致有界},\qquad
\partial_t\psi_\varepsilon
\text{ 在 }H^{k-1}\text{ 中一致有界}.
\]
反复对时间求导并使用高阶空间界，可得所有固定阶时间导数的一致较低 Sobolev 界。对空间、时间阶数作对角紧性抽取，即得光滑极限，而且
\[
\varepsilon^2\Delta h_\varepsilon\to0
\]
于每个固定的较低 Sobolev 拓扑。

所以 Step 44 关于**线性正则化问题的求解与去正则化**是可信且基本充分的。

---

## 5. 尚缺的 smooth-tame inverse

同阶估计 (14) 不是 Nash–Moser 所需结论的全部。至少还需形如
\[
\begin{aligned}
\mathcal E_k'
\le{}&
C(\|u\|_{H^{k_0+r}})\mathcal E_k\\
&+C_k(1+\|u\|_{H^{k+r}})\mathcal E_{k_0}
+\text{相应 forcing 高—低项},
\end{aligned}
\tag{15}
\]
其中 \(u=(\widehat g,\varphi)\)，\(k_0>n/2+\text{常数}\)，导数损失
\(r\) 与 \(k\) 无关。还要证明：

- (15) 对参考对的一个邻域一致成立；
- 逆映射关于 \(u\) smooth tame；
- 时间半范数也满足相应 tame 估计；
- 对参数求导所得方程可用同一 inverse estimate 递归控制。

新增归一化项自身满足标准高—低 tame 乘积估计，例如
\[
\|\widehat a h\|_{H^k}
\lesssim
\|\widehat a\|_{H^{k_0}}\|h\|_{H^k}
+\|\widehat a\|_{H^k}\|h\|_{H^{k_0}},
\tag{16}
\]
而
\(\widehat a=\chi^2\circ\varphi^{-1}\) 的 composition/inversion 已是 Yang 系统原本包含的 smooth-tame 操作。因此：

> 新归一化项不会破坏 Yang 的 smooth-tame inverse；但 Step 44 只陈述、没有完整证明 inverse 的高—低与参数依赖部分。

这正是目前最重要的未闭合对象，而不是归一化本身。

---

## 6. transported coefficients 不同情况下的唯一性

应使用精确的均值公式，而非“线性项加二次余项”。若 \(u_s\) 是连接两个解的局部图中线段，则
\[
\widehat a_1-\widehat a_2
=
\int_0^1D_\varphi\widehat a(u_s)
[\varphi_1-\varphi_2]\,ds,
\tag{17}
\]
其中
\[
D_\varphi\widehat a(u_s)[\Psi]
=-d\widehat a_s(\zeta_s).
\tag{18}
\]
整个非线性差恰为沿 \(u_s\) 的线性化积分。因此差
\[
(h,\psi)=(\widehat g_1-\widehat g_2,\varphi_1-\varphi_2)
\]
满足与 Yang 系统同型的齐次联立线性系统。由 (14) 和零初值可得
\[
h=\psi=0.
\]

这证明的是局部 gauge 唯一性。要推出几何唯一性，还需说明：每个几何解都能用同一个背景 \(S\) 规范化成该 Yang 系统的解；然后才能应用联立唯一性并拉回。Step 44 目前只陈述了这一步。

---

## 7. 光滑终点重启

假设必须是
\[
g(t)\to g_*\quad\text{于 }C^\infty,
\qquad g_*>0,
\tag{19}
\]
而不能仅仅是“极限 \(g_*\) 本身光滑”。对 \((g_*,\chi)\) 重新应用局部定理并取新背景 \(S=g_*\)，可在 \(T_*\) 后开始新解。

Step 44 所说“在 overlap 上由唯一性识别”一般不准确：旧解定义于
\([0,T_*)\)，新解定义于 \([T_*,T_*+\delta]\)，未必有非空时间重叠。严格拼接应使用自治方程
\[
\partial_tg=F(g):=-2\chi^2(\operatorname{Ric}_g+g).
\]
由 \(C^\infty\) 收敛，
\[
\partial_tg(t)=F(g(t))\to F(g_*),
\]
这与重启解的右时间导数相同；反复对方程求导可得所有单边时间 jets 相等，故拼接族在 \(T_*\) 光滑。之后几何唯一性保证延拓唯一。

---

## 最终科学结论

Step 44 已正确识别并验证了归一化适配的核心事实：

1. transported coefficient 与 weighted gauge 必须保留；
2. \(-2\widehat a\widehat g\) 的线性化是零阶；
3. \(\widehat\chi C\nabla\psi\) 的导数损失由分部积分消除；
4. 线性正则化估计可与 \(\varepsilon\) 无关；
5. 唯一性必须联立比较 metric 与 diffeomorphism；
6. 有 \(C^\infty\) 正定终点时可以重启。

但当前文本还不能标为“完整自足的 normalized Yang theorem 证明”。精确剩余对象是：

\[
\boxed{\text{Yang 线性化族的邻域一致 smooth-tame inverse，
含输运 symmetrizer、高—低估计、时间估计及参数依赖。}}
\]

一旦该对象从 Yang 的证明中完整导入或重新证明，归一化项通过 (4)、(13)、(16) 自动保持它，normalized short-time existence、联立唯一性及 smooth restart 随即严格成立。