# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 32,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step32_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step32_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 32 corrected analytic calculations for the four-dimensional normalized cutoff-flow route toward the Ishida--LeBrun negative Ricci-pinching gap. Focus only on two mathematical points. (1) In the fixed convention ||z||_4^2 <= C_S(||grad z||_2^2+r^{-2}||z||_2^2), beta=C_S H_2(0)^{1/2}, check the nested-time recurrence derived from H_{3p/2}<=H_p^{1/2}||z_p||_4^2: integral recurrence, exponent sums, no division by L_k^{1/2}, endpoint ||af(t)||_inf <= C C_S^{2/p0} t^{-3/p0}(int_{t/2}^t H_{p0})^{1/p0}, and the curvature/defect cancellations giving beta/t and delta(r^2/t)^{1/3} under the stated conditional seeds. Also check the collapsed flat product counterexample to a volume-independent unnormalized Dirichlet constant. (2) Check the tensor audit: Step 31 general-p curvature derivation is not a completed proof because Hessian-a integration differentiates a^{p-2}F^{p-2} and requires retaining both full-tensor D_p^Rm and radial D_p^F, and the defect hierarchy still needs a regularized |E| derivation. Check whether the m=2 continuation replacement using Hölder (4,4,2), ||nabla^2 chi||_4, and weighted Sobolev is a valid current formulation, rather than the prior L^infty shortcut. Return direct mathematical corrections, any remaining exponent/normalization errors, and the sharp next proof obligation. Do not assess final writing readiness.

## Integrated Scientific Memo

## 核验结论

### 1. 嵌套时间 Moser 递推

令
\[
H_p=\int a^{p-2}f^p,\qquad
D_p=\int a^{p-1}f^{p-2}|\nabla f|^2,\qquad
z_p=a^{(p-1)/2}f^{p/2}.
\]
则
\[
H_{3p/2}
=\int (a^{p-2}f^p)^{1/2}z_p^2
\le H_p^{1/2}\|z_p\|_4^2
\]
完全正确，因为 \(a\) 的指数为
\[
\frac{p-2}{2}+p-1=\frac{3p}{2}-2.
\]

在固定约定
\[
\|z\|_4^2\le C_S\bigl(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2\bigr)
\]
下，由
\[
\|\nabla z_p\|_2^2\le Cp^2(D_p+r^{-2}H_p),\qquad
\|z_p\|_2^2\le H_p
\]
得到
\[
\|z_p\|_4^2\le Cp^2C_S(D_p+r^{-2}H_p).
\]

若
\[
A_k=\int_{I_k}H_{p_k},\qquad p_{k+1}=\frac32p_k,
\]
并且
\[
\sup_{I_{k+1}}H_{p_k}
+\int_{I_{k+1}}(D_{p_k}+r^{-2}H_{p_k})
\le L_kA_k,
\]
则
\[
A_{k+1}
\le Cp_k^NC_S L_k^{3/2}A_k^{3/2}.
\]
这里确实是 \(L_k^{3/2}\)，没有也不能出现 \(L_k^{-1/2}\)：上确界项贡献 \((L_kA_k)^{1/2}\)，时空耗散项贡献 \(L_kA_k\)。

取
\[
L_k\lesssim Cp_k^N4^k(t^{-1}+r^{-2}),
\]
有
\[
\sum_{k\ge0}\frac1{p_{k+1}}=\frac2{p_0},\qquad
\frac32\sum_{k\ge0}\frac1{p_{k+1}}=\frac3{p_0}.
\]
多项式 \(p_k\) 损失和 \(4^k\) 损失对应的对数级数均收敛。因此正确端点为
\[
\boxed{
\|af(t)\|_\infty
\le C C_S^{2/p_0}(t^{-1}+r^{-2})^{3/p_0}
\left(\int_{t/2}^{t}H_{p_0}(s)\,ds\right)^{1/p_0}.
}
\]
当 \(t\le cr^2\) 时，
\[
\boxed{
\|af(t)\|_\infty
\le C C_S^{2/p_0}t^{-3/p_0}
\left(\int_{t/2}^{t}H_{p_0}(s)\,ds\right)^{1/p_0}.
}
\]
极限量是 \(af\)，因为
\[
(a^{p-2}f^p)^{1/p}=a^{1-2/p}f\longrightarrow af.
\]

这也解决了 Step 31 关于“端点应当一致有界”的冲突：上述递推本身产生显式的时间奇性；没有更强的种子时，不能删去 \(t^{-3/p_0}\)。

### 2. 反应项归一化

对
\[
R_p=\int a^{p-1}Ff^p,\qquad Y=\int aF^3,
\]
精确分解为
\[
a^{p-1}Ff^p
=(aF^3)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}.
\]
故
\[
R_p
\le Cp^{4/3}C_S^{2/3}Y^{1/3}H_p^{1/3}
(D_p+r^{-2}H_p)^{2/3}.
\]
Young 吸收将 \(C_S^{2/3}Y^{1/3}\) 三次方，得到
\[
R_p\le \varepsilon(D_p+r^{-2}H_p)
+C_\varepsilon p^N C_S^2Y\,H_p.
\]
因此在此 Sobolev 约定下，势系数确为
\[
\boxed{C_S^2Y}.
\]
Step 31 中的 \(S^4Y\) 与此并不矛盾：其约定是 \(C_S=S^2\)。同时本步
\[
\beta=C_SH_2(0)^{1/2}
\]
等于旧记号中的 \(\gamma=S^2H_2(0)^{1/2}\)，并非旧笔记另一处的 \(SH_2^{1/2}\)。

### 3. 两个条件性消去

曲率取 \(p_0=3\)。若同支撑种子满足
\[
\int_{t/2}^tY(s)\,ds\le C\frac{\beta^3}{C_S^2},
\]
则
\[
C_S^{2/3}t^{-1}
\left(\frac{\beta^3}{C_S^2}\right)^{1/3}
=\frac{\beta}{t},
\]
故
\[
\boxed{\|aF(t)\|_\infty\le C\beta/t.}
\]

缺陷取 \(p_0=6\)。若
\[
J_6(s)=\int a^4|E|^6\le C\delta^6V,
\]
则
\[
\|aE(t)\|_\infty
\le C C_S^{1/3}t^{-1/2}(\delta^6Vt)^{1/6}.
\]
使用同支撑上界
\[
C_S\le Cr^2V^{-1/2}
\]
得到
\[
\boxed{
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.
}
\]
从而
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2.
\]

需要修正一处表述：
\[
\int_{t/2}^tY\le C\beta^3/C_S^2
\]
与
\[
C_S^2Y(s)\lesssim \beta^3/s
\]
并非单独“等价”。后者推出前者；反向还需要好时间片及 \(q=3\) 前向传播。并且递推同时需要前者作为初始时空量、后者控制 \(L_k\) 中的势系数。若 \(C_S,V\) 随时间变化，必须在同一支撑和同一时间片上使用一致的统一上界/参考体积。

### 4. 塌缩平直乘积反例

在
\[
B^3(1)\times S^1(\varepsilon)
\]
上取 \(u(x,\theta)=\phi(x)\)，其中
\(\phi\in C_c^\infty(B^3(1))\) 非零。则
\[
\|u\|_4^2\asymp\varepsilon^{1/2},\qquad
\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\asymp\varepsilon.
\]
所以任何未归一化 Dirichlet Sobolev 系数均满足
\[
C_S\gtrsim\varepsilon^{-1/2}.
\]
\(u\) 在内部紧支撑，因而零边界条件并不改变该结论。这与
\(V\asymp\varepsilon\) 和 \(C_S\asymp r^2V^{-1/2}\) 一致。脚本只核验这些指数，不核验 PDE 估计。

---

## 张量审计

Step 31 的一般 \(p\) 曲率不等式尚不是完整证明。典型 Hessian-\(a\) 项在分部积分后为
\[
-p\int \nabla a*
\nabla\!\left(a^{p-2}F^{p-2}T\right).
\]
三个微分目标必须分别处理：

1. 微分 \(a^{p-2}\)：
   \[
   p(p-2)a^{p-3}|\nabla a|^2F^p
   \lesssim p^2r^{-2}H_p.
   \]

2. 微分 \(F^{p-2}\)：
   \[
   p(p-2)a^{p-2}|\nabla a|F^{p-1}|\nabla F|,
   \]
   需由
   \[
   p(p-2)D_p^F
   \]
   吸收，并留下多项式 \(p\)-损失乘 \(r^{-2}H_p\)。

3. 微分张量 \(T\)：
   会出现
   \[
   \nabla\operatorname{Rm}*E,\qquad
   \operatorname{Rm}*\nabla E.
   \]
   利用 \(|\nabla E|\le C|\nabla\operatorname{Rm}|\)，这些项必须由
   \[
   pD_p^{\operatorname{Rm}}
   \]
   支付，不能只用 \(D_p^F\)。

因此必须保留完整 Bochner 耗散
\[
-pD_p^{\operatorname{Rm}}-p(p-2)D_p^F
\]
直到所有全张量项和径向项分别吸收完毕，之后才能压缩为 Moser 所需的标量耗散。因为
\[
D_p^{\operatorname{Rm}}\ge D_p^F
\]
只允许以全张量耗散控制径向耗散，不能反向用 \(D_p^F\) 支付任意 \(\nabla\operatorname{Rm}\) 项。

缺陷层级也仍未完成。必须对
\[
f_\varepsilon=(|E|^2+\varepsilon)^{1/2}
\]
明确推导，跟踪：

- 全 \(\nabla E\) 与径向 \(\nabla f_\varepsilon\) 耗散；
- Hessian-\(a\) 分部积分；
- 随时间变化的张量范数与体积测度；
- \(\varepsilon\to0\) 的一致性；
- 无曲率独立源项。

方程关于 \(E\) 的齐次性只提示最终结构，不能替代这项证明。

---

## \(m=2\) 延拓项

令
\[
W=\nabla^2U,\quad B=\nabla^2\chi,\quad
X_p=\int|W|^p,\quad
D_p=\int\chi^2|\nabla W|^2|W|^{p-2},
\quad u=\chi|W|^{p/2}.
\]
则 Hölder \((4,4,2)\) 给出
\[
\int\chi|B||W|^p
\le \|B\|_4\|u\|_4X_p^{1/2}.
\]
加权 Sobolev 给出
\[
\|u\|_4^2
\le CC_S\bigl(p^2D_p+(1+r^{-2})X_p\bigr).
\]
因此该 \(L^4\) 方案是当前有效形式，但 Step 32 的盒装式遗漏了一个无害的零阶项。安全的写法是
\[
\boxed{
\int\chi|\nabla^2\chi||W|^p
\le \varepsilon D_p+
C_\varepsilon\Bigl[
(1+r^{-2})
+p^2C_S\|\nabla^2\chi\|_4^2
\Bigr]X_p.
}
\]
也可粗化为
\[
\varepsilon D_p+
C_\varepsilon(1+r^{-2})
\bigl(1+p^2C_S\|\nabla^2\chi\|_4^2\bigr)X_p.
\]
仅写
\[
C_\varepsilon p^2C_S\|\nabla^2\chi\|_4^2(1+r^{-2})X_p
\]
一般不能直接由 Hölder、Sobolev、Young 推出，除非另有 cutoff 范数下界或归一化关系。

旧的 \(L^\infty\) 快捷处理不能作为当前基步：\(\nabla^2_{g(t)}\chi\) 含演化联络，度量双 Lipschitz 比较本身并不给出其点态控制。前一级耦合估计提供
\(\|\nabla^2\chi\|_4\) 后，上式才与
\((\nabla^mU,\nabla^{m+1}\chi)\) 的归纳顺序相容。

## 最尖锐的后续证明义务

需要在统一约定下证明下列实际 PDE 引理：

\[
K_p'
+c\,pD_p^{\operatorname{Rm}}
+c\,p(p-2)D_p^F
\le Cp^N(1+r^{-2}+C_S^2Y)K_p,
\]
其中所有 Hessian-\(a\) 与一阶 cutoff 项逐项完成吸收；并证明其对
\(|E|_\varepsilon\) 一致的缺陷版本及从 \(t=0\) 开始的 \(J_6\) 持久性。

同时还需证明同支撑的 \(H_2\to H_3\) 时空种子及 \(q=3\) 前向传播，以分别提供
\[
\int_{t/2}^tY\le C\beta^3/C_S^2
\quad\text{和}\quad
C_S^2Y(s)\lesssim\beta^3/s.
\]
延拓方面，必须把上述修正后的 \(m=2\) 估计嵌入
\((\nabla^2U,\nabla^3\chi)\) 耦合能量，并逐项处理其余乘积；或者证明精确的 shifted-Wang 分组恒等式以替换该单-\(\chi\) 项。