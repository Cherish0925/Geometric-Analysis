# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step34_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step34_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the restored weighted-flow analysis in Step 34. Focus on four load-bearing points: (i) whether the Sobolev convention and collapse cancellation are now correct; (ii) whether the nested-time mixed recurrence and endpoint time powers in equations (4.2)-(4.9) follow from the cited energy structure, identifying any missing factors or circular use of Y, J6, or moving Sobolev control; (iii) whether direct J6 absorption via the unweighted L2 curvature coefficient in (4.10) is mathematically plausible from the exact defect equation, and what exact tensor/Kato calculation remains; (iv) whether the evolving cutoff-Hessian discussion and proposed base coupled estimate correctly isolate the m=2 continuation issue. Give corrected formulas where needed and sharply distinguish derived consequences from open estimates. Do not infer any pinching-gap theorem.

## Integrated Scientific Memo

# Step 34 核验结论

## 1. Sobolev 约定与塌缩消去：正确，但必须匹配同一支撑域

采用唯一约定
\[
\|u\|_4^2\le \mathcal S
\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\qquad
\mathcal S\asymp \frac{r^2}{\sqrt V},
\]
是自洽的。若另写
\[
\|u\|_4\le S\,\mathcal E(u)^{1/2},
\]
则 \(S^2=\mathcal S\)，不能再把具有 \(\mathcal S\) 缩放的量平方一次。

对 \(z_2=\chi F\)，
\[
K_3=\int Fz_2^2
\le \|F\|_2\|z_2\|_4^2
\le C\mathcal S K_2^{1/2}(D_2+r^{-2}K_2).
\]
故临界吸收参数确为
\[
\boxed{\gamma=\mathcal S K_2^{1/2}}.
\]
若 Sobolev 常数和 \(K_2\) 使用同一宏支撑，或二者体积统一可比，并且
\(K_2\le K_0V\)，则
\[
\gamma\le C\frac{r^2}{\sqrt V}\sqrt{K_0V}
=Cr^2\sqrt{K_0}.
\]
因此该步骤没有塌缩体积障碍。若两个量来自体积比不可控的不同区域，则会残留体积比；“同一支撑”是必要条件。

归一化平均公式也正确，但在演化度量下不能默认为 \(V(t)\) 固定。宜使用未归一化能量，或固定 \(V(0)\) 并显式保留双 Lipschitz 测度比较因子。

---

## 2. 式 (4.2)–(4.9)：时间幂正确，但 (4.3) 的 \(L^1\)-平均系数不成立

### 2.1 反应系数和混合插值

由
\[
R_p=\int a^{p-1}Ff^p
\le Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3},
\qquad Y=\int aF^3,
\]
及
\[
\|z_p\|_4^2
\le Cp^2\mathcal S(D_p+r^{-2}H_p),
\]
Young 不等式给出
\[
pR_p\le \varepsilon D_p+
C_{\varepsilon}p^N\mathcal S^2Y\,H_p+
Cp^Nr^{-2}H_p.
\]
所以反应系数确实是 \(\mathcal S^2Y\)。

逐时混合恒等式
\[
\boxed{H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2}
\]
的权重完全匹配：
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2.
\]

不过一般 \(p\) 曲率能量及正则化缺陷能量目前仍只是结构式；特别是导数落到
\(a^{p-2}F^{p-2}\) 或正则化缺陷幂时的全部 Hessian-\(a\) 项尚未逐项完成。

### 2.2 必须修正式 (4.3)

若已有
\[
H_p'+cD_p
\le Cp^N\bigl(r^{-2}+1+\mathcal S_*^2Y(t)\bigr)H_p,
\qquad
\mathcal S_*=\sup_I\mathcal S(t),
\tag{E_p}
\]
则时间截断后，能直接推出
\[
\sup_{I'}H_p+\int_{I'}D_p
\le Cp^N\Lambda(I,I')\int_IH_p
\]
所需的是
\[
\boxed{
\Lambda(I,I')
=(\tau'-\tau)^{-1}+r^{-2}+1+
\operatorname*{ess\,sup}_{s\in I}\mathcal S_*^2Y(s).
}
\tag{2.1}
\]

Step 34 的
\[
|I|^{-1}\|\mathcal S^2Y\|_{L^1(I)}
\]
不能一般性替代本质上确界，因为能量中出现的是
\[
\int_I(\mathcal S^2Y)H_p,
\]
时间平均本身不能控制它。只用 Gronwall 会产生
\(\exp(Cp^N\int_I\mathcal S^2Y)\)，其 \(p\)-增长不适合该无限迭代。

这里已有的更强点态种子正好修复问题：
\[
\mathcal S_*^2Y(s)\le \frac{C\gamma^3}{s}.
\]
在 \(I_t=[t/2,t]\) 上，
\[
\operatorname*{ess\,sup}_{I_t}\mathcal S_*^2Y
\le \frac{C\gamma^3}{t}.
\]
该估计来自固定 \(q=2,3\) 能量和好时间片传播，不依赖一般 \(p\) Moser，因此不循环。式 (4.4) 的积分界本身不足以证明所写递推。

### 2.3 正确的一步递推及端点

在上述点态控制下，
\[
\boxed{
\int_{I'}H_{3p/2}
\le Cp^N\mathcal S_*
\left[\Lambda(I,I')\int_IH_p\right]^{3/2}.
}
\tag{2.2}
\]
令 \(p_{k+1}=\frac32p_k\)，则
\[
\sum_{k\ge0}\frac1{p_k}=\frac3{p_0},
\qquad
\sum_{k\ge0}\frac1{p_{k+1}}=\frac2{p_0}.
\]
故更准确的端点是
\[
\boxed{
\|af\|_{\infty,\mathrm{terminal}}
\le C\mathcal S_*^{2/p_0}
\Lambda_t^{3/p_0}
\left(\int_{t/2}^{t}H_{p_0}(f,s)\,ds\right)^{1/p_0},
}
\tag{2.3}
\]
其中
\[
\Lambda_t=t^{-1}+r^{-2}+1+\gamma^3t^{-1}.
\]
在 \(t\lesssim \min\{r^2,1\}\) 时，
\[
\Lambda_t\le C(\gamma)t^{-1},
\]
于是才简化为
\[
\|af(t)\|_\infty
\le C(\gamma,\theta)\mathcal S_*^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^{t}H_{p_0}\right)^{1/p_0}.
\]
因此 \(t^{-3/p_0}\) 是真实的时间截断代价，不能因
\(\int_{t/2}^t\mathcal S^2Y=O(1)\) 而删除。

### 2.4 曲率与缺陷端点

曲率取 \(p_0=3\)，使用
\[
\int_{t/2}^tY(s)\,ds\le C\gamma K_2(0),
\]
得到
\[
\|aF(t)\|_\infty
\le C\mathcal S_*^{2/3}t^{-1}
(\gamma K_2(0))^{1/3}.
\]
若在首出区间中 \(\gamma\) 与初值统一可比，则
\[
\boxed{\|aF(t)\|_\infty\le C(\gamma,\theta)\frac{\gamma}{t}}.
\]
这不是零时刻一致界。

若
\[
\sup_{0<s<T}J_6(s)\le C\delta^6V_0,
\tag{J6}
\]
则 \(p_0=6\) 给出
\[
\begin{aligned}
\|aE(t)\|_\infty
&\le C\mathcal S_*^{1/3}t^{-1/2}
(\delta^6V_0t)^{1/6}\\
&\le C\delta\,r^{2/3}t^{-1/3}
=C\delta(r^2/t)^{1/3}.
\end{aligned}
\]
其中
\[
\mathcal S_*^{1/3}V_0^{1/6}\lesssim
(r^2V_0^{-1/2})^{1/3}V_0^{1/6}=r^{2/3}.
\]
因而
\[
\boxed{
\int_0^T\|aE(t)\|_\infty\,dt
\le C\delta r^{2/3}T^{2/3}
=C\delta\theta^{2/3}r^2,
\qquad T=\theta r^2.
}
\]
这些都是条件性推论：依赖 \((E_p)\)、(J6) 以及首出区间内移动 Sobolev、测度和支撑几何的比较。

---

## 3. 直接 \(J_6\) 吸收：函数不等式成立，精确缺陷能量式仍开放

令
\[
\phi_\varepsilon=(|E|^2+\varepsilon^2)^{1/2},
\qquad
z_{m,\varepsilon}
=\eta a^{(m-1)/2}\phi_\varepsilon^{m/2}.
\]
纯粹 Sobolev–Hölder 计算给出
\[
\int Fz_{m,\varepsilon}^2
\le \|F\|_{L^2(U)}\|z_{m,\varepsilon}\|_4^2.
\]
又有
\[
\|\nabla z_{m,\varepsilon}\|_2^2
\le C_mX_{m,\varepsilon}
+C_mr^{-2}J_{m,\varepsilon},
\qquad
|\nabla\phi_\varepsilon|\le|\nabla E|.
\]
故
\[
\boxed{
\int Fz_{m,\varepsilon}^2
\le C_m\gamma
\bigl(X_{m,\varepsilon}+r^{-2}J_{m,\varepsilon}\bigr).
}
\tag{3.1}
\]
特别对 \(m=6\)，
\[
z_6=\chi^5|E|^3,\qquad
|\nabla z_6|^2
\lesssim a^5|E|^4|\nabla E|^2+
r^{-2}a^4|E|^6.
\]
这里 cutoff 项的精确权重是 \(a^4=\chi^8\)，正好是 \(J_6\) 的权重。因此 Step 34 的 (4.10) 作为函数不等式是正确的。

真正待证的是从精确缺陷方程推出、且对 \(\varepsilon\) 一致的
\[
\boxed{
J_{m,\varepsilon}'
+c_mX_{m,\varepsilon}
\le C_m(r^{-2}+1)J_{m,\varepsilon}
+C_m\int Fz_{m,\varepsilon}^2.
}
\tag{3.2}
\]
所需逐项核验包括：

1. 测试
   \[
   \partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E)
   \]
   时，Lichnerowicz 代数项、移动张量范数及移动测度只能产生
   \(F\phi_\varepsilon^m\) 型势和低阶 \(J_m\)，不能出现纯曲率源；

2. 对 \(\tau\nabla^2a\)、\((\nabla^2a)*E\) 和
   \(da*\nabla E\) 全部分部积分，并保留足以吸收的完整张量梯度正项；

3. 使用
   \[
   a^{m-3}|da|^2\phi_\varepsilon^m
   =4|d\chi|^2a^{m-2}\phi_\varepsilon^m
   \]
   消除负 cutoff 幂；

4. 证明正则化余项一致趋零，不留下与 \(E\) 无关的源。

若 (3.2) 成立且 \(C_6\gamma<c_6\)，由 (3.1)
\[
J_{6,\varepsilon}'\le C(r^{-2}+1)J_{6,\varepsilon},
\]
再令 \(\varepsilon\to0\)，即可得到 (J6)，而完全不使用
\(\|aF\|_\infty\)。这正是避免积分零时刻 \(t^{-1}\) 曲率系数的机制。

因此“(4.10) 可信”不能等同于“\(J_6\) 持续性已证明”：开放对象是 (3.2) 的精确张量/Kato 推导。

---

## 4. 演化 cutoff Hessian 与 \(m=2\) 延拓：问题定位正确，基层估计尚未完成

固定标量 \(\chi\) 的协变 Hessian依赖演化连接：
\[
\partial_t(\nabla_i\nabla_j\chi)
=-(\partial_t\Gamma^k_{ij})\nabla_k\chi.
\]
对 \(h=-2aE=-2\operatorname{Ric}(U)\)，
\[
\partial_t\Gamma=g^{-1}*\nabla h,
\]
故主结构为
\[
\partial_t\nabla^2\chi=\nabla U*\nabla\chi.
\]
移动范数和测度还产生 \(U*C_2\) 型零阶项。双 Lipschitz 比较只控制已固定张量的范数，不能控制连接，因此不能单独推出
\(\nabla^2_{g(t)}\chi\) 有界。

Wang 的 Lemma 4.11 确实同时估计
\(\nabla(\chi^2\mathrm{Rm})\) 与 \(\nabla^2\chi\)，支持以
\[
(W_1,C_2)=(\nabla U,\nabla^2\chi)
\]
作为基层耦合对。恰当的目标应写成正则化平方范数形式：
\[
\mathcal X_{1,p}
=(\varepsilon+\|W_1\|_p^p)^{2/p},\qquad
\mathcal Z_{2,p}
=(\varepsilon+\|C_2\|_p^p)^{2/p},
\]
并证明
\[
\boxed{
(\mathcal X_{1,p}+\mathcal Z_{2,p})'
+c(\varepsilon+\|W_1\|_p^p)^{2/p-1}D_{1,p}
\le C_p(t)(1+\mathcal X_{1,p}+\mathcal Z_{2,p}),
}
\tag{4.1}
\]
其中 \(C_p\in L^1(0,T)\)，由 \(\|U\|_\infty\)、有限的未加权 \(T\)-矩及低阶量控制。

在 \(m=2\) 时，分部积分留下真正关键项
\[
I=\int\chi|C_2||W_2|^p.
\]
令 \(u=\chi|W_2|^{p/2}\)、\(X=\|W_2\|_p^p\)，则
\[
I\le \|C_2\|_4\|u\|_4X^{1/2},
\]
且
\[
\|\nabla u\|_2^2\le Cp^2D_{2,p}+Cr^{-2}X.
\]
由 Sobolev 和 Young，
\[
\boxed{
I\le \varepsilon D_{2,p}
+C_{\varepsilon,p}
\left[1+\mathcal S_*\|C_2\|_4^2(1+r^{-2})\right]X.
}
\tag{4.2}
\]
Step 34 式 (6.6) 的主要机制和 \(\mathcal S\|C_2\|_4^2\) 幂正确；严格展开时会出现
\(\mathcal S^{1/2}r^{-1}\|C_2\|_4X\)，可由 Young 吸收到 (4.2) 的零阶 \(1+\cdots\) 中。

因此：

- 基层 \((W_1,C_2)\) 必须先给出统一的 \(\|C_2\|_4\)；
- 然后 (4.2) 才能控制 \(m=2\) 的单-\(\chi\) 项；
- 这不是双 Lipschitz 比较或初始光滑性自动提供的；
- Wang 的未平移局部 Ricci 流论证只支持该架构，不能替代当前 \(U=a(\mathrm{Rm}+G)\) 方程的逐项检查。

仍待完成的是：显式推导 \(W_1\) 与 \(C_2\) 的耦合能量、确认基层曲率交换项不要求尚未控制的 \(\nabla^2U\)，以及随后 \((W_2,C_3)\) 的全部收缩项估计。

---

## 最终科学状态

**已核验：**

- \(\gamma=\mathcal S K_2^{1/2}\) 及匹配支撑下的塌缩消去；
- 混合权重恒等式和 \(p\mapsto3p/2\)；
- 在点态 \(Y(s)\lesssim s^{-1}\) 输入下，端点时间幂 \(t^{-3/p_0}\)；
- 条件性的
  \[
  \|aF(t)\|_\infty\lesssim\gamma/t,\qquad
  \|aE(t)\|_\infty\lesssim\delta(r^2/t)^{1/3},
  \]
  以及可积漂移；
- (4.10) 的 Sobolev–Hölder 权重计算；
- cutoff Hessian 基层耦合及 \(m=2\) 单-\(\chi\) 难点的定位。

**必须修正：**

- Step 34 式 (4.3) 的 \(L^1_t\) 平均不能直接控制
  \(\int(\mathcal S^2Y)H_p\)；需使用点态
  \(\operatorname*{ess\,sup}_I\mathcal S^2Y\)，或另行发明带相关性控制的迭代。

**仍开放：**

- 一般 \(p\) 曲率/缺陷张量能量式；
- 一致正则化的缺陷式 (3.2)，从而 \(J_6\) 持续性；
- 移动 Sobolev、测度、\(K_2\) 和支撑几何的定量首出闭合；
- \((W_1,C_2)\) 及 \((W_2,C_3)\) 的完整逐项耦合估计。

这些结论仅核验加权流解析链，不推出任何 Ricci 夹逼间隙或 Einstein 度量存在性定理。