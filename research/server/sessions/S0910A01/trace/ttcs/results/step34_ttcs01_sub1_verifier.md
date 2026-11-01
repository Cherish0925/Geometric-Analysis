# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/scripts/step34_integrated_potential_q3_verify.py",
    "Sessions/S0910A01/workspace/notes/step33_curvature_power_inequality.md",
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md"
  ]
}
```

## Task

Verify the Step 34 corrected fixed-exponent analytic layer for the selected-support normalized cutoff flow in the Yau-26 restricted 4D negative route. Read the new note and script, plus the prior Step 33 power note and Step 25 q=2 derivation as background. Focus on scientific correctness: (i) the all-lower curvature convention and pure scaling test; (ii) the corrected diffusion dissipation -p D_Rm - p(p-2) D_F before cutoff absorption; (iii) the volume-form term being controlled by the curvature reaction via |s+4|<=CF rather than C delta K_p; (iv) the integrated-potential bound B(t)<=C gamma^3 from q=2 and its use to obtain q=3 same-support propagation by good-slice + Gronwall without circularity; (v) the regularized defect derivation from Ricci variation and whether the no-additive-source conclusion is justified at the stated level. Identify any mathematical faults or missing assumptions that would invalidate these fixed-exponent consequences, and distinguish them from the later unproved moving-Sobolev/cutoff-jet continuation obligations.

## Output

# 科学核验备忘录

## 总体结论

Step 34 的核心固定指数链条在下列明确化之后是数学上一致的：

\[
q=2\text{ 能量}
\Longrightarrow
\int_0^tY
\Longrightarrow
B(t)=\int_0^t\mathcal S^2Y
\Longrightarrow
q=3\text{ 时刻传播及 }J_6\text{ 保持}.
\]

其中：

- 纯缩放计算、扩散耗散系数和体积形式项的修正是正确的；
- \(B(t)\le C\gamma^3\) 与 good-slice–Gronwall 之间没有循环依赖；
- 正则化 defect 能量在精确张量方程成立时确实可以在 \(\varepsilon\downarrow0\) 后不留下与 \(E\) 无关的加性源项；
- 当前文本仍有一个实质性的记号冲突：按 (0.6) 字面定义，\(K_2=\int F^2\) 不是 Step 25 的局部缓冲能量，因而 (0.7)、(3.1)–(3.5) 不能按字面同时成立；
- Hessian 分部积分还需要补写 \(\nabla B\)、\(\nabla C\) 的结构估计。仅有 \(|B|\le CF^2\)、\(|C|\le Cf_\varepsilon^2\) 并不足以推出相应能量估计。

这些是当前固定指数推导本身需要明确的数学内容。移动 Sobolev 系数、度量可比性、光滑流存在性和高阶 cutoff jets 属于另一层几何闭合工作。

---

## 1. all-lower 曲率约定与纯缩放

采用
\[
R_{ijkl}=g_{l\alpha}R_{ijk}{}^\alpha
\]
时，若
\[
\partial_tg=-2g,\qquad g(t)=e^{-2t}g_0,
\]
则 Levi-Civita 联络和 \(R_{ijk}{}^l\) 不变，而
\[
R_{ijkl}(t)=e^{-2t}R_{ijkl}(0),\qquad
\partial_tR_{ijkl}=-2R_{ijkl}.
\]
因此张量本身的两份贡献为
\[
2\langle R,\partial_tR\rangle=-4|R|^2.
\]
四个逆度量各满足 \(\partial_tg^{-1}=2g^{-1}\)，总贡献为
\[
+8|R|^2.
\]
故
\[
\partial_t|\operatorname{Rm}|^2=4|\operatorname{Rm}|^2.
\]
在四维，
\[
\partial_td\mu=-4d\mu,
\]
所以
\[
\frac d{dt}\int|\operatorname{Rm}|^2\,d\mu=0.
\]
同时
\[
\frac d{dt}\int F^2\,d\mu
=\frac d{dt}\int(1+|\operatorname{Rm}|^2)\,d\mu
=-4\int1\,d\mu.
\]

这正确排除了把 \(-2g\) 记录成 \(|\operatorname{Rm}|^2\) 点态阻尼的做法。Step 33 §1B 中出现的 \(\nabla a\otimes\nabla a\) 也不属于度量一阶变分：曲率一阶变分对 \(h\) 线性，只产生 \(\nabla^2a\) 而不产生二次的 \(\nabla a\) 项。

缩放计算只能固定正规化部分的系数。完整的 (1.2) 仍需由
\[
\partial_t\operatorname{Rm}=\nabla^2h+\operatorname{Rm}*h,
\qquad h=-2a(\operatorname{Ric}+g),
\]
逐项推出。更精确的写法应是
\[
\partial_tF^2
\le a\Delta F^2-2a|\nabla\operatorname{Rm}|^2
+C|\nabla a|F|\nabla\operatorname{Rm}|
+CaF^3
+\sum_\alpha c_\alpha(\nabla_i\nabla_ja)B_\alpha^{ij},
\]
保留每个 Hessian 收缩的符号，而不是先取绝对值。

---

## 2. 扩散耗散系数

直接测试
\[
a\Delta F^2-2a|\nabla\operatorname{Rm}|^2
\]
得到
\[
\begin{aligned}
\frac p2\int a^{p-2}F^{p-2}a\Delta F^2
={}&-p(p-2)\int a^{p-1}F^{p-2}|\nabla F|^2\\
&-p(p-1)\int a^{p-2}F^{p-1}\nabla a\cdot\nabla F ,
\end{aligned}
\]
以及
\[
\frac p2\int a^{p-2}F^{p-2}
\bigl(-2a|\nabla\operatorname{Rm}|^2\bigr)
=-pD_p^{\rm Rm}.
\]
所以 cutoff 交叉项吸收以前的耗散严格为
\[
\boxed{-pD_p^{\rm Rm}-p(p-2)D_p^F.}
\]

Step 33 的 \(-p(p-3)D_p^F\) 来自重复加入一个 \(+pD_p^F\)。Step 34 的修正正确，且在 \(p=3\) 时仍保留 \(3D_3^F\)，这对于后续 Sobolev 反应吸收很重要。

由
\[
|\nabla a|^2=4a|\nabla\chi|^2\le Cr^{-2}a
\]
可得
\[
a^{p-3}|\nabla a|^2F^p\le Cr^{-2}a^{p-2}F^p,
\]
所以径向 cutoff 项和 \(\nabla a*\nabla\operatorname{Rm}\) 项分别由
\(D_p^F\)、\(D_p^{\rm Rm}\) 吸收，权重与 \(K_p\) 完全匹配。

### Hessian 分部积分所需的补充结构

(2.9) 不能仅由
\[
|B^{ij}|\le CF^2
\]
推出。还需要每个实际收缩满足
\[
B=B(\operatorname{Rm},E,g),\qquad
|\nabla B|\le CF|\nabla\operatorname{Rm}|.
\]
由于
\[
E=\operatorname{Ric}+g,\qquad
|\nabla E|\le C|\nabla\operatorname{Rm}|,
\]
这一估计对预期的代数收缩确实成立。加入它以后，
\[
\begin{aligned}
\left|\int a^{p-2}F^{p-2}\nabla^2a*B\right|
\le{}&
\varepsilon pD_p^{\rm Rm}
+\varepsilon p(p-2)D_p^F\\
&+C_\varepsilon p^Nr^{-2}K_p
\end{aligned}
\]
是正确的。文本中的“typical contribution”需要扩展为所有实际收缩的有限列表。

反应三因子恒等式
\[
a^{p-1}F^{p+1}
=(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}z_p^{4/3}
\]
及其 Sobolev–Young 吸收也正确。这里
\[
\|\nabla z_p\|_2^2
\le Cp^2(D_p^F+r^{-2}K_p).
\]
因此在上述张量结构成立时，(2.14) 成立。

---

## 3. 体积形式项

四维有
\[
\partial_td\mu=-a(s+4)d\mu.
\]
由
\[
s+4=\operatorname{tr}E,\qquad
|s+4|\le 2|E|\le CF,
\]
可得
\[
\left|
\int a^{p-2}F^p\,\partial_td\mu
\right|
\le C\int a^{p-1}F^{p+1}.
\]
这与曲率三次反应具有完全相同的权重。因此 Step 34 把它并入 \(R_p\) 是正确的；Step 33 中的 \(C\delta K_p\) 在 defect 点态保持尚未得到时没有依据。

对于 \(F\) 中常数 \(1\) 产生的低阶项，\(p\ge3\) 时均带有至少 \(a^{p-2}\) 或 \(a^{p-1}\)，并可由
\[
C(r^{-2}+1)K_p
\]
控制，不需要加入无权体积常数。

---

## 4. \(q=2\) 局部记号必须修正

按 Step 34 (0.6) 字面定义，
\[
K_2=\int a^0F^2=\int F^2.
\]
若积分在整个闭流形上，这是全局能量，不能由一个 macro-support 的
\(K_0V\) 控制；若积分只在 macro-support 上，则分部积分需要处理端项。

与 Step 25 一致的定义应是
\[
K_2^\eta=\int\eta^2F^2,\qquad
D_2^\eta=\int\eta^2a|\nabla\operatorname{Rm}|^2,
\]
其中 \(\eta=1\) 于 \(\operatorname{supp}a\) 的邻域。对 \(p\ge3\) 仍可使用
\[
K_p=\int_Ma^{p-2}F^p,
\]
因为 \(a^{p-2}\) 已提供紧支撑。

在这个修正下，
\[
Y=\int aF^3
=\int(\eta F)(\chi F)^2
\le (K_2^\eta)^{1/2}\|\chi F\|_4^2,
\]
而
\[
\|\chi F\|_4^2
\le C\mathcal S
\left(D_2^\eta+r^{-2}K_2^\eta\right).
\]
故
\[
Y\le C\mathcal S(K_2^\eta)^{1/2}
\left(D_2^\eta+r^{-2}K_2^\eta\right).
\]

还需要 enlarged support 上的初始平均估计
\[
K_2^\eta(0)\le CK_0V,
\]
才能推出
\[
\gamma=\mathcal S(0)K_2^\eta(0)^{1/2}
\le Cr^2\sqrt{K_0}.
\]

---

## 5. integrated potential 与 \(q=3\) 传播

在光滑流、移动 Sobolev 估计、cutoff 梯度估计以及
\[
\mathcal S(t)\le2\mathcal S(0),\qquad
K_2^\eta(t)\le2K_2^\eta(0)
\]
成立的时间段内，Step 25 的 \(q=2\) 不等式给出
\[
(K_2^\eta)'+cD_2^\eta
\le CY+Cr^{-2}K_2^\eta.
\]
若 \(C\gamma\) 足够小，\(Y\) 中的 \(D_2^\eta\) 部分可吸收，因而在
\(t\le\theta r^2\) 上
\[
\sup_{s\le t}K_2^\eta(s)+\int_0^tD_2^\eta(s)\,ds
\le CK_2^\eta(0).
\]
于是
\[
\int_0^tY(s)\,ds
\le C\gamma K_2^\eta(0).
\]
再由 \(\mathcal S(s)\le2\mathcal S(0)\)，
\[
\begin{aligned}
B(t)
&=\int_0^t\mathcal S(s)^2Y(s)\,ds\\
&\le C\mathcal S(0)^2\gamma K_2^\eta(0)
=C\gamma^3.
\end{aligned}
\]
最后一步使用
\[
\gamma=\mathcal S(0)K_2^\eta(0)^{1/2}.
\]

这一推导只使用 \(q=2\) 能量与 Sobolev 插值，没有使用 \(q=3\) 时刻估计。

对任意 \(t>0\)，由区间 \([t/4,t/2]\) 的平均值可取 \(\tau\) 使
\[
Y(\tau)\le\frac4t\int_{t/4}^{t/2}Y(s)\,ds
\le\frac{C\gamma K_2^\eta(0)}t.
\]
随后从
\[
Y'\le C(r^{-2}+1+\mathcal S^2Y)Y
\]
积分到 \(t\)，得到
\[
Y(t)\le\frac{C\gamma K_2^\eta(0)}t
\exp\!\left(C\theta(1+r^2)+C\gamma^3\right).
\]
若 \(r\le r_0\) 且 \(r_0\) 固定，这就是
\[
Y(t)\le\frac{C\gamma K_2^\eta(0)}t,
\qquad
\mathcal S(t)^2Y(t)\le\frac{C\gamma^3}t.
\]

所以 good-slice–Gronwall 链条没有循环。需要注意，\(\mathcal S^2Y\sim t^{-1}\) 只在正时间 dyadic slab 上使用；从零时刻出发的 Gronwall 系数来自 \(B(t)\)，不是来自这个 \(t^{-1}\) 上界。

---

## 6. regularized defect 能量

结构上，
\[
E_t=D\operatorname{Ric}_g[-2aE]-2aE.
\]
\(D\operatorname{Ric}\) 对 \(h\) 及其前两阶导数线性，因此所有项均含
\(E,\nabla E\) 或 \(\nabla^2E\)。再利用
\[
\nabla^jE_{ij}=\frac12\nabla_i\operatorname{tr}E
\]
可将二阶主部整理为
\[
a\Delta E+(\nabla a)*\nabla E+(\nabla^2a)*E,
\]
其余为
\[
a\operatorname{Rm}*E+aE*E+aE.
\]
因此不存在与 \(E\) 无关的张量项。不过，获得正号为 \(a\Delta E\) 的精确式仍需逐指标推导；仅由“\(E=0\) 时流静止”不能单独推出所需耗散。

令
\[
f_\varepsilon=(|E|^2+\varepsilon)^{1/2}.
\]
因为
\[
\Delta f_\varepsilon^2=\Delta|E|^2,
\]
扩散部分实际产生
\[
-pD_{p,\varepsilon}^E
-p(p-2)D_{p,\varepsilon}^{f},
\]
其中
\[
D_{p,\varepsilon}^{f}
=\int a^{p-1}f_\varepsilon^{p-2}|\nabla f_\varepsilon|^2
\le D_{p,\varepsilon}^E.
\]
Step 34 只保留第一项并舍去第二个有利项，这是允许的；cutoff 交叉项仍可由
\[
|\nabla f_\varepsilon|\le|\nabla E|
\]
和 \(D_{p,\varepsilon}^E\) 吸收。

defect Hessian 分部积分还需要实际结构
\[
C^{ij}=C^{ij}(E,E),\qquad
|C|\le C|E|^2,\qquad
|\nabla C|\le C|E||\nabla E|.
\]
文本只显示了 \(|C|\le Cf_\varepsilon^2\)，应补入后两个结构式。加入后，(5.7) 的常数可取为与 \(\varepsilon\) 无关。

代数项、度量范数变化和体积形式项均满足
\[
C\int a^{p-1}Ff_\varepsilon^p.
\]
三因子分解 (5.9) 正确，并给出
\[
J_{p,\varepsilon}'+cD_{p,\varepsilon}^E
\le Cp^N(r^{-2}+1+\mathcal S^2Y)J_{p,\varepsilon}.
\]

正则化后用 \(Ff_\varepsilon^p\) 作上界，会在 \(E=0\) 时给出非零的上界 integrand，但它始终乘在 \(J_{p,\varepsilon}\) 上，而不是形成独立加性项。因此
\[
J_{p,\varepsilon}(t)
\le J_{p,\varepsilon}(0)
\exp\!\int_0^tCp^N(r^{-2}+1+\mathcal S^2Y)\,ds.
\]
当 \(\varepsilon\downarrow0\) 时，
\[
J_{p,\varepsilon}\downarrow J_p,
\qquad
D_{p,\varepsilon}^E\downarrow
\int a^{p-1}|E|^{p-2}|\nabla E|^2,
\]
可在时间积分形式中使用单调收敛。于是极限不等式没有曲率独立的加性源项。

对 \(p=6\)，
\[
J_6(t)\le
J_6(0)\exp\!\left(C\theta(1+r^2)+CB(t)\right)
\le C J_6(0).
\]
这里常数还依赖固定的 \(r_0\)，除非预先取 \(r\le1\) 并将 \(+1\) 吸收到 \(r^{-2}\) 中。

---

## 7. 当前层所用假设与高阶 continuation 的区别

固定指数推导当前需要：

1. \([0,T]\) 上存在光滑解；
2. \(a=\chi^2\) 为固定的光滑非负函数；
3. \(|\nabla\chi|_{g(t)}\le Cr^{-1}\)；
4. 缓冲函数 \(\eta\) 与 \(K_2^\eta,D_2^\eta\) 的明确使用；
5. \(\mathcal S(t)\le2\mathcal S(0)\) 和 \(K_2^\eta(t)\le2K_2^\eta(0)\)；
6. 曲率、defect 方程中所有 Hessian 收缩的逐指标形式，以及
   \(|\nabla B|\)、\(|\nabla C|\) 的结构估计。

signed Hessian 分部积分使 (2.14)、(5.11) 不需要预先给出
\(|\nabla^2a|_{L^\infty}\) 的统一估计。相比之下，度量漂移闭合、移动 Sobolev 系数恢复、光滑延拓以及
\((\nabla U,\nabla^2\chi)\) 等高阶耦合估计仍属于后续 continuation 内容。

---

## 8. 脚本的证据强度

`step34_integrated_potential_q3_verify.py` 正确复现了：

- 四维纯缩放指数；
- \(-pD_p^{\rm Rm}-p(p-2)D_p^F\) 的形式；
- 三因子幂次；
- \(\gamma\) 和 defect endpoint 的体积消去；
- \(B\) 的 \(\gamma^3\) 代数关系。

脚本按其说明没有编码张量 PDE、移动 Sobolev 或流存在性，这是恰当的。

第 7 节数值例中保留了 \(r=0.01\)，而所取各个 \(t\) 均不满足
\(t\le\theta r^2\)。此外 `gronwall_bound` 与 `expected_form` 是同一表达式的重新书写。因此该段只验证代数恒等关系，不能作为容许时间段内 ODE 行为的数值证据；这不影响纸面 good-slice 推导。

综合而言，修正 \(K_2\) 的缓冲局部定义并补齐 \(B,C\) 的导数结构后，Step 34 的三个固定指数结果
\[
B(t)\le C\gamma^3,\qquad
Y(t)\le \frac{C\gamma K_2^\eta(0)}t,\qquad
J_6(t)\le CJ_6(0)
\]
从所列前提出发均可严格推出。