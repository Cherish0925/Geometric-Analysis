# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md",
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md"
  ]
}
```

## Task

Independently verify the exact-flow critical-to-subcritical curvature bridge in Step 58. Check the local relative H2 inequality (including removal of the global additive constant), the estimate Y <= C S sqrt(H)(D+r^-2 H) with the correct matched supports, the integrated Y and S^2 Y bounds without any Y(0), and the q=3 propagation. Pay special attention to the distinction w2=chi F_T versus z3=a F_T^(3/2), the Sobolev-constant convention, moving metric/measure terms, and whether the shifted tensor T introduces any unaccounted derivative or source. Give explicit corrections if any load-bearing step fails; do not assume later Moser or continuation conclusions.

## Output

## 独立验证备忘

### 总结

在四维、固定光滑截断函数、当前度量下  
\[
|d\chi|_{g(t)}\le C_\chi r^{-1},
\qquad
\mathcal S(t)\le A\mathcal S(0),
\]
且
\[
\gamma(t)=\mathcal S(t)H(t)^{1/2}
\]
保持在足够小的预设阈值内时，Step 58 的以下链条成立：
\[
H(0)\Longrightarrow
\sup H+\int D
\Longrightarrow
\int Y,\ \int\mathcal S^2Y
\Longrightarrow
Y(t)\lesssim \frac{\Gamma H(0)}{t}.
\]
此链条没有使用 \(Y(0)\)。截断匹配、Sobolev 常数幂次、移动测度项以及平移曲率张量 \(T\) 的导数结构均相容。需要作三处文字级精确修正：Step 57 的体积变化标量记号、\(\Gamma^3\) 处的等号、以及三因子恒等式对 \(\eta=1\) 的依赖。

---

## 1. 平移张量与移动几何项

令
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\operatorname{Rm}+G,
\qquad F=(1+|T|^2)^{1/2}.
\]
按给定 Kulkarni–Nomizu 约定，
\[
\operatorname{Ric}(G)=g,
\qquad
\operatorname{Ric}(T)=E.
\]
因此逐点有
\[
|E|\le C_n|T|\le C_nF,
\qquad
|\nabla E|\le C_n|\nabla T|.
\]
又因为 \(\nabla G=0\)，
\[
\nabla T=\nabla\operatorname{Rm}.
\]

若 \(h=\partial_tg=-2aE\)，则
\[
\partial_tG=\frac{h\owedge g}{n-1}
=-\frac{2a}{n-1}(E\owedge g).
\]
这是带因子 \(a\) 的纯代数项，不产生 \(\nabla T\)、\(\nabla a\) 或 \(\nabla^2a\) 的新项。其与 \(T\) 的收缩由
\[
Ca|E||T|\le CaF^2
\]
控制。

移动测度的准确公式是
\[
\boxed{\partial_td\mu=-a\,\operatorname{tr}_gE\,d\mu.}
\]
于是
\[
|\partial_td\mu|
\le CaF\,d\mu.
\]
Step 57 中
\[
s=\operatorname{tr}E-n=\mathrm{scal}+n
\]
这一行记号不一致。正确写法可任选其一：

- \(s=\mathrm{scal}\)，则 \(\operatorname{tr}E=s+n\)；
- \(s=\operatorname{tr}E=\mathrm{scal}+n\)，则 \(\partial_td\mu=-as\,d\mu\)。

采用准确公式后，测度变化对 \(H\) 的贡献至多为 \(CY\)，没有额外常数源。

---

## 2. 相对 \(H\) 不等式

精确流的曲率演化可整理为
\[
\partial_tF^2
\le
a\Delta F^2-2a|\nabla T|^2
+C|da|F|\nabla T|
+C(\nabla^2a)_{ij}B^{ij}
+CaF^3+CaF^2,
\]
其中 Hessian 收缩张量满足
\[
|B|\le CF^2,
\qquad
|\nabla B|\le CF|\nabla T|.
\]
这里可以取 \(B\) 为 \(T*E\) 的固定线性组合；上述估计来自
\(\operatorname{Ric}(T)=E\) 和 \(\nabla E=\operatorname{Ric}(\nabla T)\)。
平移项 \(\partial_tG\)、逆度量变化和测度变化都已包含在代数项中。

### 2.1 Bochner 与一阶截断项

利用
\[
|da|^2=4a|d\chi|^2\le Cr^{-2}a,
\]
以及 \(a=0\) 于 \(\operatorname{supp}d\eta\)，
\[
\int\eta^2a\Delta|T|^2
=-\int\eta^2da\cdot d|T|^2.
\]
所以
\[
\left|\int\eta^2da\cdot d|T|^2\right|
\le \varepsilon D+C_\varepsilon r^{-2}H.
\]
演化式中的显式 \(da*\nabla T*T\) 项完全相同地满足
\[
\int\eta^2|da|F|\nabla T|
\le \varepsilon D+C_\varepsilon r^{-2}H.
\]

### 2.2 Hessian 截断项

一次分部积分给出
\[
\begin{aligned}
\int\eta^2(\nabla_i\nabla_ja)B^{ij}
={}&-\int\eta^2\nabla_ja\,\nabla_iB^{ij}\\
&-2\int\eta\,\nabla_i\eta\,\nabla_ja\,B^{ij}.
\end{aligned}
\]
第二项因 \(da=0\) 于 \(\operatorname{supp}d\eta\) 而消失。第一项满足
\[
\left|\int\eta^2da*\nabla B\right|
\le C\int\eta^2|da|F|\nabla T|
\le\varepsilon D+C_\varepsilon r^{-2}H.
\]
因此这里确实只使用 \(d\chi\)，不需要 \(\nabla^2\chi\)。

### 2.3 全局加性常数的消除

所有零阶积分都带活动因子 \(a\)，其形式不超出
\[
\int\eta^2a,\quad
\int\eta^2aF,\quad
\int\eta^2aF^2,\quad
\int\eta^2aF^3.
\]
由于 \(0\le a\le1\)、\(F\ge1\)，
\[
\int\eta^2a\le H,\qquad
\int\eta^2aF\le H,\qquad
\int\eta^2aF^2\le H,
\qquad
\int\eta^2aF^3=Y.
\]
特别地，\(F^2=1+|T|^2\) 中的 \(1\) 正是把局部体积项吸收到 \(H\) 的机制。于是
\[
\boxed{
H'+c_0D\le C_0Y+C_1(1+r^{-2})H.
}
\]
没有必要引入与 \(\operatorname{Vol}(M)\) 成比例的加性项。

---

## 3. 临界到次临界估计

因为
\[
\eta=1\quad\text{于 }\operatorname{supp}\chi,
\qquad a=\chi^2,
\]
所以准确地有
\[
Y=\int F(\chi F)^2.
\]
Hölder 给出
\[
Y
\le
\|F\|_{L^2(\operatorname{supp}\chi)}
\|\chi F\|_4^2
\le H^{1/2}\|\chi F\|_4^2.
\]

采用 Step 58 的平方范数 Sobolev 约定
\[
\|v\|_4^2
\le
\mathcal S(t)\left(
\|\nabla v\|_2^2+r^{-2}\|v\|_2^2
\right),
\]
这里 \(\mathcal S\) 已经相当于通常 Sobolev 常数的平方。于是
\[
\begin{aligned}
\|\nabla(\chi F)\|_2^2
&\le
2\int\chi^2|dF|^2
+2\int|d\chi|^2F^2\\
&\le C(D+r^{-2}H),
\end{aligned}
\]
其中使用了
\[
|dF|\le|\nabla T|,
\qquad
\eta=1\text{ 于 }\operatorname{supp}\chi.
\]
并且
\[
\|\chi F\|_2^2\le H.
\]
故
\[
\boxed{
Y\le C\mathcal S(t)H(t)^{1/2}
\bigl(D+r^{-2}H\bigr).
}
\]
定义
\[
\gamma(t)=\mathcal S(t)H(t)^{1/2},
\]
即可得到 Step 58 的公式
\[
Y\le C\gamma(t)(D+r^{-2}H).
\]

这里必须使用
\[
w_2=\chi F=a^{1/2}F.
\]
其梯度主项具有权重
\[
a|dF|^2,
\]
正好与 \(D\) 相配。

---

## 4. \(H,D,Y,\mathcal S^2Y\) 的时间积分

设在所考察光滑时间段上
\[
\gamma(t)\le\gamma_*,
\qquad
C_0C\gamma_*\le\frac{c_0}{2}.
\]
代入相对 \(H\) 不等式后，
\[
H'+c_1D\le C(1+r^{-2})H.
\]
若 \(t\le\theta r^2\)、\(r\le1\)，则
\[
H(t)\le e^{C\theta}H(0),
\]
并且积分后
\[
\int_0^tD(s)\,ds\le CH(0).
\]

令
\[
\Gamma=\sup_{0\le s\le t}\gamma(s).
\]
由临界插值式，
\[
\begin{aligned}
\int_0^tY(s)\,ds
&\le C\Gamma\left(
\int_0^tD(s)\,ds
+r^{-2}\int_0^tH(s)\,ds
\right)\\
&\le C\Gamma H(0).
\end{aligned}
\]
整个推导没有出现 \(Y(0)\)。

若另有
\[
\mathcal S(s)\le A\mathcal S(0),
\]
则
\[
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le
CA^2\mathcal S(0)^2\Gamma H(0).
\]
由于
\[
\gamma(0)=\mathcal S(0)H(0)^{1/2}\le\Gamma,
\]
可进一步写成
\[
\boxed{
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le CA^2\Gamma^3.
}
\]

Step 58 公式 (2.8) 中的
\[
C\mathcal S(0)^2\Gamma H(0)=C\Gamma^3
\]
应改写为不等式；严格依据是
\(\gamma(0)\le\Gamma\)，并不需要双向可比性。

---

## 5. 正确的 \(q=3\) 变量与传播

定义
\[
D_3^T=\int\eta^2a^2F|\nabla T|^2,
\qquad
D_3^F=\int\eta^2a^2F|dF|^2.
\]
对
\[
Y=\int\eta^2aF^3
\]
作能量计算，前述 Hessian 有号分部积分给出
\[
Y'+c(D_3^T+D_3^F)
\le
C(1+r^{-2})Y
+C\int\eta^2a^2F^4.
\]

### 5.1 Sobolev 变量必须是 \(z_3=\eta aF^{3/2}\)

令
\[
z_3=\eta aF^{3/2}.
\]
则
\[
z_3^2=\eta^2a^2F^3,
\]
且
\[
\|\nabla z_3\|_2^2
\le
C D_3^F+Cr^{-2}Y.
\]
这里：

- \(d\eta\) 项因 \(a=0\) 于 \(\operatorname{supp}d\eta\) 而消失；
- \(da\) 项由
  \[
  |da|^2F^3\le Cr^{-2}aF^3
  \]
  控制；
- \(\|z_3\|_2^2\le Y\)，因为 \(a^2\le a\)。

反应项满足
\[
\int a^2F^4
\le
Y^{2/3}\left(\int z_3^4\right)^{1/3}.
\]
Sobolev 不等式给出
\[
\left(\int z_3^4\right)^{1/3}
\le
\mathcal S^{2/3}
\bigl(D_3^F+r^{-2}Y\bigr)^{2/3}.
\]
Young 不等式于是产生
\[
\int a^2F^4
\le
\varepsilon D_3^F
+C_\varepsilon r^{-2}Y
+C_\varepsilon\mathcal S^2Y^2.
\]
因此
\[
\boxed{
Y'\le C(1+r^{-2}+\mathcal S^2Y)Y.
}
\]

若改用
\[
\eta a^{1/2}F^{3/2},
\]
其梯度主项只有权重
\[
aF|dF|^2,
\]
而 \(q=3\) 耗散具有权重 \(a^2F|dF|^2\)。在 \(a\) 很小时，前者不能由后者控制。因此 Step 58 对 \(w_2\) 与 \(z_3\) 的区分是必要的。

Step 58 的一般三因子公式依赖于
\[
\eta=1\quad\text{于 }\{a>0\}.
\]
在这一支持匹配下，公式逐点成立；正文宜明确写出这一依赖。

### 5.2 正时间传播

由
\[
\int_0^tY(s)\,ds\le C\Gamma H(0)
\]
可选取
\[
\tau\in[t/4,t/2]
\]
使
\[
Y(\tau)\le\frac{C\Gamma H(0)}{t}.
\]
从 \(\tau\) 到 \(t\) 积分 \(q=3\) 不等式：
\[
Y(t)
\le
Y(\tau)
\exp\!\left(
C(1+r^{-2})(t-\tau)
+C\int_\tau^t\mathcal S^2Y
\right).
\]
故严格形式为
\[
Y(t)
\le
\frac{C\Gamma H(0)}{t}
\exp\!\bigl(C\theta+C\Gamma^3\bigr).
\]
在固定 \(\theta\) 且 \(\Gamma\le\gamma_*\) 的吸收设置中，指数因子并入常数，得到
\[
\boxed{
Y(t)\le\frac{C\Gamma H(0)}{t}.
}
\]
再利用 \(\mathcal S(t)\le A\mathcal S(0)\) 和
\(\gamma(0)\le\Gamma\)，
\[
\boxed{
\mathcal S(t)^2Y(t)\le\frac{CA^2\Gamma^3}{t}.
}
\]
这里仍然没有使用 \(Y(0)\)。

---

## 6. 最终科学判断

四个核心部分——相对 \(H\) 不等式、临界插值、无 \(Y(0)\) 的时间积分、正时间 \(q=3\) 传播——在给定光滑时间段与当前 Sobolev/截断梯度控制下相互闭合。平移张量 \(T\) 不引入额外导数源；其关键性质是
\[
\operatorname{Ric}(T)=E,\qquad \nabla T=\nabla\operatorname{Rm},
\qquad \partial_tG\text{ 为带 }a\text{ 的代数项}.
\]

需要在文本中明确保留的前提是：所有 Sobolev 范数、梯度和测度均取自 \(g(t)\)；\(\mathcal S(t)\) 的比较和 \(|d\chi|_{g(t)}\le Cr^{-1}\) 是同步时间段上的输入，而不是由上述能量链自身推出的。上述验证止于 \(q=3\) 传播，不使用其后的 Moser 或延拓论证。