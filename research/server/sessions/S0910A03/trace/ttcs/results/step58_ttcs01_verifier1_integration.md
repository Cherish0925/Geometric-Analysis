# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 58,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step58_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step58_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the exact-flow critical-to-subcritical curvature bridge in Step 58. Check the local relative H2 inequality (including removal of the global additive constant), the estimate Y <= C S sqrt(H)(D+r^-2 H) with the correct matched supports, the integrated Y and S^2 Y bounds without any Y(0), and the q=3 propagation. Pay special attention to the distinction w2=chi F_T versus z3=a F_T^(3/2), the Sobolev-constant convention, moving metric/measure terms, and whether the shifted tensor T introduces any unaccounted derivative or source. Give explicit corrections if any load-bearing step fails; do not assume later Moser or continuation conclusions.

## Integrated Scientific Memo

# Step 58 独立核验结论

## 结论

在四维精确截断流
\[
\partial_tg=-2aE,\qquad a=\chi^2,\qquad
E=\Ric_g+g,
\]
的任一光滑暂定 first-exit 时间区间上，若同步假设

\[
|d\chi|_{g(t)}\le Cr^{-1},\qquad
\mathcal S(t)\le A\mathcal S(0),\qquad
\gamma(t):=\mathcal S(t)H(t)^{1/2}\le\gamma_*
\]
且 \(\gamma_*\) 足够小，则 Step 58 的核心链条成立：
\[
H(0)\Longrightarrow
\sup H+\int D
\Longrightarrow
\int Y,\ \int\mathcal S^2Y
\Longrightarrow
Y(t)\lesssim \frac{\Gamma H(0)}{t},
\qquad
\Gamma:=\sup\gamma.
\]
全程不使用 \(Y(0)\)。

需要作三项明确修正：

1. Step 57 的移动测度标量记号有误，应写
   \[
   \partial_t d\mu=-a\,\tr_gE\,d\mu.
   \]
2. Step 58 (2.8) 中 \(C\mathcal S(0)^2\Gamma H(0)=C\Gamma^3\) 一般应写为不等式，除非已明确给出双向 first-exit 可比性。
3. Step 58 (3.5) 不是含 \(\eta\) 的字面逐点恒等式；必须明确利用 \(\eta=1\) 于 \(\supp a\)，或在 Hölder 三因子间精确分配 \(\eta\)。

除此之外，所检查的关键步骤没有发现负载性失败。

---

## 1. 相对 \(H_2\) 不等式与全局常数的消除

置
\[
T=\Rm+\frac{g\owedge g}{2(n-1)},\qquad
F=(1+|T|^2)^{1/2},
\]
以及
\[
H=\int\eta^2F^2,\qquad
D=\int\eta^2a|\nabla T|^2,\qquad
Y=\int\eta^2aF^3.
\]

### 1.1 移动测度修正

准确公式为
\[
\boxed{\partial_t d\mu=-a\,\tr_gE\,d\mu.}
\]
Step 57 中
\[
s=\tr E-n=\mathrm{scal}+n
\]
不一致。正确选择是以下二者之一：

- \(s=\mathrm{scal}\)，则 \(\tr E=s+n\)；
- \(s=\tr E=\mathrm{scal}+n\)，则 \(\partial_td\mu=-as\,d\mu\)。

由于 \(|\tr E|\le C|E|\le CF\)，测度变化贡献满足
\[
\left|\int\eta^2F^2\,\partial_td\mu\right|
\le C\int\eta^2aF^3=CY.
\]

### 1.2 截断导数项

利用
\[
\frac{|da|^2}{a}=4|d\chi|^2\le Cr^{-2}
\]
及 \(a=da=0\) 于 \(\supp d\eta\)，Bochner 交叉项和显式
\(da*\nabla T*T\) 项都满足
\[
\le \varepsilon D+C_\varepsilon r^{-2}H.
\]

Hessian-\(a\) 项写成
\[
\int\eta^2(\nabla_i\nabla_ja)B^{ij}.
\]
其中对平移张量仍有
\[
|B|\le CF^2,\qquad |\nabla B|\le CF|\nabla T|.
\]
一次有号分部积分给出
\[
-\int\eta^2\nabla_ja\,\nabla_iB^{ij}
-2\int\eta\nabla_i\eta\,\nabla_ja\,B^{ij}.
\]
第二项由支持分离消失，第一项由 Young 不等式控制为
\[
\varepsilon D+C_\varepsilon r^{-2}H.
\]
因此此处只需要 \(d\chi\)，不需要 \(\nabla^2\chi\) 的点态控制。

### 1.3 无全局加性源

所有零阶局部项都带活动因子 \(a\)，并归入
\[
\int\eta^2a,\quad
\int\eta^2aF,\quad
\int\eta^2aF^2,\quad
\int\eta^2aF^3.
\]
因为 \(0\le a\le1\)、\(F\ge1\)，前三项均不超过 \(H\)，最后一项等于
\(Y\)。故严格的相对形式是
\[
\boxed{
H'+c_0D\le C_0Y+C_1(1+r^{-2})H.
}
\]
不应保留与 \(\Vol(M)\) 成比例的加性常数。

---

## 2. 匹配支持上的临界桥

由于
\[
\eta=1\quad\text{于 }\supp\chi,\qquad a=\chi^2,
\]
有
\[
Y=\int F(\chi F)^2.
\]
因此
\[
Y\le
\|F\|_{L^2(\supp\chi)}\|\chi F\|_4^2
\le H^{1/2}\|\chi F\|_4^2.
\]

这里必须使用平方范数 Sobolev 约定
\[
\boxed{
\|v\|_4^2\le
\mathcal S(t)\bigl(\|\nabla v\|_2^2+r^{-2}\|v\|_2^2\bigr).
}
\]
于是 \(\mathcal S\) 已是“平方后的”Sobolev 常数，后续反应系数为
\(\mathcal S^2Y\)，不能再额外平方或开方。

取
\[
w_2=\chi F=a^{1/2}F.
\]
由
\[
|dF|\le|\nabla T|,\qquad |d\chi|\le Cr^{-1},
\]
以及 \(\eta=1\) 于 \(\supp\chi\)，
\[
\|\nabla(\chi F)\|_2^2
\le C(D+r^{-2}H),\qquad
\|\chi F\|_2^2\le H.
\]
故
\[
\boxed{
Y\le C\mathcal S(t)H(t)^{1/2}
\bigl(D+r^{-2}H\bigr).
}
\]
即
\[
Y\le C\gamma(t)(D+r^{-2}H).
\]

这个估计的支持匹配是精确的；若 \(\eta\) 不在 \(\supp\chi\) 上恒等于
\(1\)，则 \(H^{1/2}\) 不再直接控制所需的 \(F\)-范数。

---

## 3. 不含 \(Y(0)\) 的积分估计

若
\[
C_0C\gamma_*\le \frac{c_0}{2},
\]
则把临界桥代入相对 \(H\) 不等式得到
\[
H'+c_1D\le C(1+r^{-2})H.
\]
对 \(t\le\theta r^2\)、\(r\le1\)，
\[
H(t)\le e^{C\theta}H(0),\qquad
\int_0^tD(s)\,ds\le CH(0).
\]

令
\[
\Gamma=\sup_{0\le s\le t}\gamma(s).
\]
则
\[
\boxed{
\int_0^tY(s)\,ds
\le C\Gamma\left(
\int_0^tD+r^{-2}\int_0^tH
\right)
\le C\Gamma H(0).
}
\]
这一步完全没有 \(Y(0)\)。

若 \(\mathcal S(s)\le A\mathcal S(0)\)，则
\[
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le CA^2\mathcal S(0)^2\Gamma H(0).
\]
又因
\[
\gamma(0)=\mathcal S(0)H(0)^{1/2}\le\Gamma,
\]
得到
\[
\boxed{
\int_0^t\mathcal S(s)^2Y(s)\,ds
\le CA^2\Gamma^3.
}
\]

因此 Step 58 (2.8) 最稳妥的写法是
\[
C\mathcal S(0)^2\Gamma H(0)\le C\Gamma^3,
\]
而非无条件等号。若 first-exit 比较另行证明
\(\Gamma\simeq\mathcal S(0)H(0)^{1/2}\)，才可用 \(\simeq\)。

---

## 4. \(q=3\) 变量、反应吸收与传播

### 4.1 必须区分 \(w_2\) 与 \(z_3\)

临界桥使用
\[
w_2=\chi F=a^{1/2}F.
\]
而 \(q=3\) 能量
\[
Y=K_3=\int\eta^2aF^3
\]
的正确 Sobolev 变量是
\[
\boxed{z_3=\eta aF^{3/2}.}
\]
其平方为
\[
z_3^2=\eta^2a^2F^3,
\]
与耗散
\[
D_3^T=\int\eta^2a^2F|\nabla T|^2,\qquad
D_3^F=\int\eta^2a^2F|dF|^2
\]
具有正确的 \(a^2\) 权重。

若误用 \(\eta a^{1/2}F^{3/2}\)，梯度主项只有
\(aF|dF|^2\)，不能由退化区域中的 \(a^2F|dF|^2\) 控制。这是负载性区别。

### 4.2 \(q=3\) 反应估计

由
\[
\|\nabla z_3\|_2^2
\le C(D_3^F+r^{-2}Y),\qquad
\|z_3\|_2^2\le Y,
\]
以及
\[
\int a^2F^4
\le Y^{2/3}\left(\int z_3^4\right)^{1/3},
\]
Sobolev 与 Young 给出
\[
\int a^2F^4
\le
\varepsilon D_3^F+
C_\varepsilon r^{-2}Y+
C_\varepsilon\mathcal S^2Y^2.
\]
因此
\[
\boxed{
Y'\le C(1+r^{-2}+\mathcal S^2Y)Y.
}
\]

更一般的三因子论证中，Step 58 (3.5) 应补充支持说明。字面上
\(z_p\) 含有 \(\eta\)，故最好将 Hölder 因子写成
\[
\begin{aligned}
u_1&=\eta^{2/3}(aF^3)^{1/3},\\
u_2&=\eta^{2/3}(a^{p-2}F^p)^{1/3},\\
u_3&=\eta^{2/3}
\left(a^{(p-1)/2}F^{p/2}\right)^{4/3}.
\end{aligned}
\]
这样
\[
\int u_1^3=Y,\qquad
\int u_2^3=K_p,\qquad
\int u_3^3=\|z_p\|_4^4,
\]
最后一个等式使用 \(\eta=1\) 于 \(\supp a\)。这消除了原式中的
\(\eta\)-幂次歧义。

### 4.3 正时间传播

由积分 \(Y\) 估计，在任意 \(t>0\) 可选
\[
\tau\in[t/4,t/2]
\]
使
\[
Y(\tau)\le \frac{C\Gamma H(0)}{t}.
\]
从 \(\tau\) 到 \(t\) 对 \(q=3\) 不等式作 Grönwall：
\[
Y(t)\le
Y(\tau)\exp\left(
C(1+r^{-2})(t-\tau)
+C\int_\tau^t\mathcal S^2Y
\right).
\]
故严格地
\[
Y(t)\le
\frac{C\Gamma H(0)}{t}
\exp(C\theta+C\Gamma^3).
\]
在固定 \(\theta\) 且 \(\Gamma\le\gamma_*\) 的 first-exit 区间上，指数并入常数：
\[
\boxed{
Y(t)\le \frac{C\Gamma H(0)}{t}.
}
\]
进一步，
\[
\boxed{
\mathcal S(t)^2Y(t)
\le\frac{CA^2\Gamma^3}{t}.
}
\]
仍未使用 \(Y(0)\)；\(\mathcal S^2Y\) 出现在自身系数中也不循环，因为其时间积分已经由 \(q=2\) 层先验控制。

---

## 5. 平移张量 \(T\) 没有遗漏导数源

令
\[
G=\frac{g\owedge g}{2(n-1)},\qquad T=\Rm+G.
\]
则
\[
\Ric(T)=E,\qquad \nabla G=0,\qquad
\nabla T=\nabla\Rm.
\]
故耗散与未平移曲率完全相同。

同时
\[
\partial_tG
=\frac{\partial_tg\owedge g}{n-1}
=-\frac{2a}{n-1}(E\owedge g),
\]
是带因子 \(a\) 的纯代数项，收缩后由 \(CaF^2\) 控制，不产生
\(\nabla a,\nabla^2a\) 或新的曲率导数。

平移后 Hessian-\(a\) 收缩除 \(\Rm*E\) 外还含 \(G*E\)，但
\[
\nabla(G*E)=G*\nabla E,\qquad
|\nabla E|\le C|\nabla T|,
\]
所以仍满足
\[
|\nabla B|\le CF|\nabla T|.
\]
此外 \(\Delta G=0\)，而 \(\Delta_LG-\Delta G\) 只是
\(\Rm*G\) 的代数项。因此 principal part 与 Bochner 耗散没有改变。

结论是：\(T\) 的平移只增加受控代数项，没有遗漏的导数或外部源。

---

## 6. 核验边界

以上结论仅在给定的光滑暂定 first-exit 区间上成立，并依赖同步输入：

\[
\mathcal S(t)\le A\mathcal S(0),\qquad
|d\chi|_{g(t)}\le Cr^{-1},
\]
以及足够小的 \(\gamma(t)\)。这些移动几何比较并非由本桥自身证明。

本核验止于 \(q=3\) 传播。它不证明后续 Moser 端点，也不解决退化 collar 上的 cutoff-jet continuation。尤其，曲率有界并不自动控制
\(\nabla^3\chi,\nabla^4\chi\) 等演化截断 jet；共同观察时间仍需有限阶耦合层级和固定背景 restart 估计。