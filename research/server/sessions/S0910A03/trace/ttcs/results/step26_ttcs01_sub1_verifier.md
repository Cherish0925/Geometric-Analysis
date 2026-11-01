# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/scripts/verify_step26_general_p_and_sobolev.py"
  ]
}
```

## Task

Verify the Step 26 mathematical development for the 4D negative-branch cutoff-flow program. The note claims to resolve two of three remaining obstacles: (1) the general-p weighted tensor inequality and (2) the initial Sobolev inequality on collapsed balls. Check specifically:

(a) Does the general-p derivation (Section 3) correctly extend the A01 q=2,3 template? In particular: is the boundary term d(eta^2 a^{p-1}) correctly handled (vanishing deta part for p>=3, Young for da part giving Cp^2 r^{-2} K_p)? Is the Hessian-a IBP at general p correct (no singular terms)? Is the dissipation constant c>0 uniform in p? Is the polynomial p-dependence on the RHS (at most p^3 after the full Young/Sobolev chain) sufficient for the infinite-product convergence?

(b) Does the Maheux-Saloff-Coste theorem (Section 1) genuinely resolve the initial Sobolev question? The claim is that for n=4, p=2, p*=4, the relative Sobolev inequality gives S = Cr^2 Vol^{-1/2} with C depending only on n and Kr^2, valid on any geodesic ball regardless of collapse. Is the passage from the mean-subtracted form to the compactly-supported form correct? Are the constants truly volume-independent?

(c) Is the corrected beta-bar definition (Section 2) consistent: does subtracting the collar from H_2 and using S on the active support give a self-consistent absorption? Does the additive constant from the collar spoil the Gronwall bound?

(d) Is the explicit J_6 propagation (Section 4) a genuine critical absorption argument, not just an appeal to homogeneity?

(e) Does the first-exit closure (Section 6) genuinely self-improve all conditions simultaneously, conditional on smooth existence?

Identify any hidden error or gap. Give corrected formulas if needed.

## Output

# Step 26 科学复核备忘

## 总体判断

- Section 1 从所陈述的 Maheux–Saloff-Coste 不等式推出四维相对 Sobolev 不等式的计算是正确的，塌缩只通过显式因子 \(V(B_r)^{-1/2}\) 出现。
- 曲率的 general-\(p\) 能量估计可以由 A01 的 \(q=2,3\) 计算严格推广，而且耗散项前可以保留与 \(p\) 无关的正系数；但 Section 3.5 写错了一个 \(a\) 的幂次。
- 缺陷张量的 general-\(p\) 小节目前不是完整推导：\(\partial_t\Phi_\varepsilon\) 的公式有误，且 A01 式 (6.5) 在依赖 \(\Phi_\varepsilon\) 的测试函数下如何使用尚未展开。该部分可以按下述公式补齐。
- collar 修正在当前文字中不闭合：两处吸收式多写了 \(\mathsf S^{-1}\)，而由带 \(C_{\rm col}\) 的粗 Gronwall 估计不能推出 \(\bar\beta(t)\lesssim\bar\beta(0)\)。保留各误差项的实际支撑后，可以完全去掉 \(C_{\rm col}\)。
- \(J_6\) 确实来自临界 Sobolev 吸收，不只是齐次性描述。
- 使用修正后的活跃区 \(H_2\) 估计，Section 6 的同时自改善论证在光滑解已经存在的条件下成立。光滑延拓仍是独立的解析任务。

---

## (a) General-\(p\) 张量估计

### 1. 权重微分项

令
\[
w=\eta^2a^{p-2},\qquad wa=\eta^2a^{p-1}.
\]
扩散积分给出
\[
\begin{aligned}
p\int waF^{p-2}\langle R,\Delta R\rangle
={}&-p\int waF^{p-2}|\nabla R|^2\\
&-p(p-2)\int waF^{p-2}|\nabla F|^2\\
&-p\int\left\langle d(wa),
F^{p-2}\langle R,\nabla R\rangle\right\rangle .
\end{aligned}
\]

其中
\[
d(wa)=2\eta\,d\eta\,a^{p-1}
 +(p-1)\eta^2a^{p-2}da.
\]
因为 \(\operatorname{supp}d\eta\subset\{a=0\}^{\circ}\)，第一项确实为零。

利用 \(\langle R,\nabla R\rangle=F\nabla F\)，第二项满足
\[
\begin{aligned}
|B_p|
&\le \varepsilon p(p-2)
 \int\eta^2a^{p-1}F^{p-2}|\nabla F|^2\\
&\quad+
C_\varepsilon\frac{p(p-1)^2}{p-2}
 \int\eta^2a^{p-3}|da|^2F^p.
\end{aligned}
\]
对 \(p\ge3\)，
\[
\frac{p(p-1)^2}{p-2}\le Cp^2,
\]
并且
\[
a^{p-3}|da|^2
=4a^{p-2}|d\chi|^2.
\]
因此余项确为
\[
Cp^2r^{-2}K_p.
\]

### 2. Hessian-\(a\) 项

代表项为
\[
p\int \eta^2a^{p-2}F^{p-2}R*(\nabla^2a)*E.
\]
一次分部积分得到
\[
-p\int da*\nabla\!\left(
\eta^2a^{p-2}F^{p-2}R*E
\right).
\]

- 微分落在 \(\eta\) 上时，由 \(da=0\) 于 \(\operatorname{supp}d\eta\)，该项为零。
- 微分落在 \(a^{p-2}\) 上时，得到
  \[
  Cp(p-2)\int\eta^2a^{p-3}|da|^2F^p
  \le Cp^2r^{-2}K_p.
  \]
- 微分落在 \(F,R,E\) 上时，利用
  \[
  |E|\le CF,\qquad |\nabla E|\le C|\nabla R|,
  \]
  以及相对于扩散耗散的 Young 不等式，仍只留下
  \[
  Cp^2r^{-2}K_p.
  \]

因此这里没有不可积的 \(a\) 的负幂。

### 3. Section 3.5 的幂次错误与统一耗散常数

正确的微分公式是
\[
\begin{aligned}
\nabla Z_p
={}&a^{(p-1)/2}F^{p/2}d\eta\\
&+\frac{p-1}{2}\eta a^{(p-3)/2}F^{p/2}da\\
&+\frac p2\eta a^{(p-1)/2}F^{p/2-1}\nabla F.
\end{aligned}
\]
所以权重导数的平方是
\[
a^{p-3}|da|^2F^p
=a^{p-1}\left|\frac{da}{a}\right|^2F^p
=4a^{p-2}|d\chi|^2F^p.
\]
Step 26 式 (3.5) 写成了
\[
a^{p-2}|da/a|^2,
\]
少了一个 \(a\)。其后得到的 \(a^{p-2}|d\chi|^2\) 余项反而是正确的。

更重要的是，统一的 \(c>0\) 不能只从文中最后一句
\[
\|\nabla Z_p\|_2^2\le C_p(D_p+r^{-2}K_p)
\]
推出，因为若 \(C_p\sim p^2\)，这句话本身会损失 \(p\)。正确机制是保留标量梯度耗散：
\[
p(p-2)\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2.
\]
另一方面，
\[
\|\nabla Z_p\|_2^2
\le Cp^2\int\eta^2a^{p-1}F^{p-2}|\nabla F|^2
 +Cp^2r^{-2}K_p.
\]
由于
\[
p(p-2)\ge \frac13p^2,\qquad p\ge3,
\]
可得到与 \(p\) 无关的正系数 \(c\)。

### 4. 缺陷张量正则化需要改写

文中的
\[
\partial_t\Phi_\varepsilon
=\frac{|E|^2}{\Phi_\varepsilon}\partial_t|E|^2
\cdot\frac1{2\Phi_\varepsilon}
\]
不正确。应为
\[
\partial_t\Phi_\varepsilon
=\frac1{2\Phi_\varepsilon}\partial_t|E|^2.
\]

更适合直接使用
\[
\boxed{
(\partial_t-a\Delta)\Phi_\varepsilon^p
=
\frac p2\Phi_\varepsilon^{p-2}
(\partial_t-a\Delta)|E|^2
-p(p-2)a\Phi_\varepsilon^{p-4}
|\langle E,\nabla E\rangle|^2.}
\]
最后一项等于
\[
-p(p-2)a\Phi_\varepsilon^{p-2}
|\nabla\Phi_\varepsilon|^2
\]
并提供所需标量耗散。

对于 A01 式 (6.5)，应代入
\[
q=\frac p2\eta^2a^{p-2}\Phi_\varepsilon^{p-2}.
\]
微分 \(dq\) 后：

- \(da\)-项产生
  \[
  Cp^2\int\eta^2a^{p-3}|da|^2\Phi_\varepsilon^p;
  \]
- \(\nabla\Phi_\varepsilon\)-项由上述 \(p(p-2)\) 耗散吸收；
- 所有反应项由
  \[
  CpaF\Phi_\varepsilon^p
  \]
  控制。

这样才能完整得到缺陷版本的 (3.1)。令 \(\varepsilon\to0\) 时，零阶项可用控制收敛，梯度耗散应用弱下半连续性；仅写“dominated convergence”不足以处理梯度项。

### 5. 非整数幂

“任意非负光滑 \(\chi\) 的任意实次幂均光滑”并不成立。Moser 序列会产生如
\[
2(p-2)=9.5
\]
这样的指数。可采用两种严格处理：

1. 预先选择在零集处无限阶平坦且其所有所需正实次幂均光滑的标准 bump；
2. 只使用 \(C^1/W^{1,\infty}\) 链式法则并作平滑逼近。

这里所有指数至少为 \(2\)，而能量计算只需要一阶权重微分，因此第二种处理足够。验证脚本关于“所有实次幂光滑”的输出只是打印语句，并未证明该事实。

### 6. \(p\)-依赖与迭代

Sobolev–Young 链给出
\[
\begin{aligned}
I_p
&:=\int\eta^2a^{p-1}F\Phi^p\\
&\le H_3^{1/3}K_p^{1/3}K_{2p}^{1/3}\\
&\le \mathsf S^{2/3}H_3^{1/3}K_p^{1/3}
 \bigl(\|\nabla Z_p\|_2^2+r^{-2}K_p\bigr)^{2/3}.
\end{aligned}
\]
于是
\[
CpI_p
\le \frac c2\|\nabla Z_p\|_2^2
 +Cp^3(\mathsf S^2H_3+r^{-2})K_p.
\]
因此 \(p^3\) 的增长正确。对
\[
p_j=p_0(3/2)^j
\]
有
\[
\sum_j\frac{\log(Cp_j^3 4^j)}{p_j}<\infty,
\]
故无限乘积收敛；任何固定次数的 \(p\)-多项式都不会破坏该迭代。

---

## (b) 初始相对 Sobolev 不等式

以 Section 1 所写的定理为前提，推导正确。令
\[
V=\operatorname{Vol}(B_r(x)).
\]
四维 \(p=2,p^*=4\) 时，
\[
\|u-u_B\|_4
\le C(4,Kr^2)\,r\,V^{-1/4}\|\nabla u\|_2.
\]
又有
\[
\|u_B\|_{L^4(B_r)}
=V^{1/4}|u_B|
\le V^{-1/4}\|u\|_2.
\]
因此
\[
\|u\|_4^2
\le C(4,Kr^2)V^{-1/2}
\left(r^2\|\nabla u\|_2^2+\|u\|_2^2\right),
\]
即
\[
\boxed{
\|u\|_4^2
\le
C(4,Kr^2)r^2V^{-1/2}
\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right).}
\]

这里：

- \(C(4,Kr^2)\) 与 \(V\) 无关；
- \(\mathsf S\) 本身仍含显式的 \(V^{-1/2}\)；
- 该体积因子正是使塌缩情形仍可使用的归一化。

所给材料没有 Maheux–Saloff-Coste 论文 PDF 页或定理原文，因此定理号、同一个球还是扩大球、梯度积分所在集合等文字细节尚不能从这些文件独立核实。若原文右端使用 \(B_{2r}\)，对 \(u\in C_c^\infty(B_r)\) 作零延拓，再结合 Bishop–Gromov 比较，仍能得到同型不等式，只会改变 \(C(4,Kr^2)\)。

---

## (c) \(\bar\beta\) 与静止 collar

在标准 cutoff 下，\(\operatorname{supp}\eta\setminus\operatorname{supp}\chi\) 的邻域中 \(a=0\)，因而 \(g,F,d\mu\) 均不随时间变化。故减去 \(C_{\rm col}\) 这一代数操作本身成立。

但两处吸收式的 \(\mathsf S\) 因子写错。正确计算是
\[
\begin{aligned}
\int\eta^2aF^3
&\le \|F\|_{L^2(\operatorname{supp}\chi)}
 \|\chi F\|_4^2\\
&\le \frac{\bar\beta}{\mathsf S}
 \cdot \mathsf S
 \left(D_2+r^{-2}\widehat H_2\right)\\
&=\boxed{\bar\beta
 \left(D_2+r^{-2}\widehat H_2\right)}.
\end{aligned}
\]
Section 2.4 多写了 \(\mathsf S^{-1}\)。Section 4 对 \(J_6\) 的相同公式也有同样问题。

若只使用文中粗估计
\[
\widehat H_2'
\le Cr^{-2}(\widehat H_2+C_{\rm col}),
\]
则
\[
\widehat H_2(t)
\le e^{Ct/r^2}\widehat H_2(0)
 +(e^{Ct/r^2}-1)C_{\rm col}.
\]
这不能推出
\[
\bar\beta(t)\lesssim\bar\beta(0)
\]
，除非另有
\[
C_{\rm col}\lesssim\widehat H_2(0)
\quad\text{或}\quad
\mathsf S\sqrt{C_{\rm col}}\ll1.
\]
\(C_{\rm col}\le H_2(0)\) 是显然的，但文中的 \(H_2(0)\le CV\) 没有在所给公式中推导；即使是全局体积估计，也不能自动控制塌缩球上的
\(\mathsf S\sqrt{C_{\rm col}}\)。

这里有一个更直接的修正：A01 推导中的所有非零误差均含 \(a\)、\(da\) 或 \(|da|^2/a\)，实际都支撑在 \(\operatorname{supp}\chi\)。因此不必把
\[
Cr^{-2}H_2
\]
粗略保留为全辅助区能量，而可写成
\[
\boxed{
\widehat H_2'+cD_2
\le C\int\eta^2aF^3
 +Cr^{-2}\widehat H_2.}
\]
吸收后直接得到
\[
\widehat H_2(t)
\le e^{Ct/r^2}\widehat H_2(0),
\]
从而
\[
\bar\beta(t)
\le
\frac{\mathsf S(t)}{\mathsf S(0)}
e^{Ct/(2r^2)}\bar\beta(0).
\]
这是与活跃区临界小量真正相容的版本。

---

## (d) \(J_6\) 传播

在缺陷 general-\(p\) 公式按上文补齐后，\(p=6\) 给出
\[
J_6'+c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6
 +C\int\eta^2a^5F|E|^6.
\]
其中
\[
Z_6=\eta a^{5/2}|E|^3.
\]
反应项满足
\[
\begin{aligned}
\int\eta^2a^5F|E|^6
&=\int F|Z_6|^2\\
&\le \|F\|_{L^2(\operatorname{supp}\chi)}
 \|Z_6\|_4^2\\
&\le
\bar\beta\left(
\|\nabla Z_6\|_2^2+r^{-2}J_6
\right).
\end{aligned}
\]
故当 \(C\bar\beta<c/2\) 时，
\[
J_6'+\frac c2\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6,
\]
并且
\[
J_6(t)\le e^{Ct/r^2}J_6(0).
\]
所以这是标准的四维临界 \(L^2\)-势吸收，而不是单凭齐次性。

体积记号应分开：
\[
V_B=\operatorname{Vol}(B_r),\qquad
V_\eta=\operatorname{Vol}(\operatorname{supp}\eta)\le V_B.
\]
则
\[
J_6(0)\le C\delta^6V_\eta,\qquad
\mathsf S\le Cr^2V_B^{-1/2},
\]
Moser 终点实际给出
\[
\|aE(t)\|_\infty
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}
\left(\frac{V_\eta}{V_B}\right)^{1/6}
\le
C\delta\left(\frac{r^2}{t}\right)^{1/3}.
\]
Step 26 把局部球体积、辅助区体积和全局体积都记成 \(V\)，需要区分。

---

## (e) 同时自改善

采用修正后的
\[
\widehat H_2(t)\le e^{Ct/r^2}\widehat H_2(0)
\]
后，闭合链是自洽的：

1. 缺陷 Moser 估计给出
   \[
   \int_0^{\theta r^2}\|aE(s)\|_\infty ds
   \le C\delta\theta^{2/3}r^2.
   \]
2. 因而
   \[
   e^{-2I(t)}g_0\le g(t)\le e^{2I(t)}g_0.
   \]
3. 固定区域上的范数比较给出
   \[
   \mathsf S(t)\le e^{CI(t)}\mathsf S(0),
   \qquad
   |d\chi|_{g(t)}\le e^{I(t)}|d\chi|_{g_0}.
   \]
4. 活跃区能量和 Sobolev 系数共同给出
   \[
   \bar\beta(t)
   \le e^{CI(t)+C\theta}\bar\beta(0).
   \]
   预留初始小量余度即可保持所有临界吸收。
5. 同一 \(\bar\beta\) 分别吸收 \(Q\) 与 \(J_6\) 的势项，得到
   \[
   Q(t)\le e^{C\theta}Q(0),\qquad
   J_6(t)\le e^{C\theta}J_6(0).
   \]

相应地，(F3a) 应改成
\[
\boxed{\widehat H_2(t)\le2\widehat H_2(0)}
\]
而不是
\[
\widehat H_2(t)\le2H_2(0).
\]
后者不足以维持以活跃区能量定义的 \(\bar\beta\)。

另有一处几何表述需要调整：仅由 \(C^0\) 双线性型比较不能推出指数映射彼此 \(C^0\)-接近。这里其实只需距离比较
\[
e^{-I}d_{g_0}\le d_{g(t)}\le e^I d_{g_0},
\]
即可得到固定球之间的包含关系。指数映射的平滑比较需要连接或曲率导数信息，应放到正时间 plateau 正则性之后。

因此，经过上述公式修正后，Section 6 在已有光滑解的时间段上确实同时闭合；它本身仍不提供统一时间的光滑存在或延拓。