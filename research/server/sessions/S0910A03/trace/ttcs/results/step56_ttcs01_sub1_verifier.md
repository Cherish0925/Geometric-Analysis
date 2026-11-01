# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step55_direct_nonlinear_flow_construction.md",
    "Sessions/S0910A03/workspace/notes/step54_exact_synchronized_output_ledger.md",
    "Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md"
  ]
}
```

## Task

Independently verify the mathematical core of Step 56's proposed repair of the direct nonlinear transported-cutoff flow. Focus on whether the tame product/commutator estimate (2.6) really follows from the stated derivative budget and low H^{s0} control; whether all principal, Q, Lie, and transport allocations in Sections 3-4 yield an epsilon,nu-uniform hierarchy linear in the current high energy on one low-order interval; and whether the doubly parabolic approximation legitimately yields a smooth limit solving the original transported-cutoff system. Identify any omitted top derivative, circular dependence, invalid Galerkin/parabolic assertion, or needed correction. Give exact repaired inequalities where possible; do not assume Theorem 9.1 is already proved.

## Output

# 科学复核备忘录

## 总结

Step 56 的核心能量机制可以严密化：

1. 式 (2.6) 确实由“总微分阶不超过 \(m+2\)、每个因子不超过 \(m\)”推出；最清楚的证明是以 \(W^{4,\infty}\) 与 \(H^m\) 做 Gagliardo–Nirenberg 插值，而不是正文中较含混的 \(L^{p_i}\) 参数叙述。
2. 主项、\(Q\) 项、Lie 交叉项和输运项的最高阶分配完整。所有 \(D^{m+1}G\) 都带有可由
   \[
   (\beta^2+\varepsilon)|D^{m+1}G|^2
   \]
   吸收的 \(\beta\)、\(\beta^2\) 或 \(\beta^2+\varepsilon\)；Lie 项中唯一的 \(D^{m+1}\beta\) 可积分转移到 \(G\)，因而不需要除以 \(\nu\)。
3. 对固定 \(\varepsilon,\nu>0\)，系统确为对角主部的强抛物系统。通过低阶停时论证可得到同一 datum 的参数一致时间，再在该时间上逐阶传播全部 \(H^m\) 范数。
4. 参数趋零可产生至少一个光滑退化系统解。这里得到的是存在性；文中没有比较两个任意退化解所需的差分估计，因此唯一性并未随之得到。
5. Galerkin 段落中的“投影消失，所以原能量估计自动保持”写得过快。标准强抛物理论已经足够；若使用谱截断，必须改用与投影相容的谱 Sobolev 能量并重新处理交换子。

---

## 1. 式 (2.6) 的严密证明

令
\[
X_m=\|G\|_{H^m}+\|\beta\|_{H^m},
\qquad
\|G\|_{H^{s_0}}+\|\beta\|_{H^{s_0}}\le R,
\]
且 \(s_0>n/2+4\)。于是
\[
\|G\|_{W^{4,\infty}}+\|\beta\|_{W^{4,\infty}}\le C_R.
\]

考虑单项式
\[
P=F(G,G^{-1})\prod_{i=1}^N D^{q_i}u_i,
\qquad
u_i\in\{G,\beta\},
\]
其中
\[
0\le q_i\le m,\qquad \sum_i q_i\le m+2.
\]

对每个 \(q_i>4\)，置
\[
a_i=\frac{q_i-4}{m-4}\in(0,1].
\]
标准 Gagliardo–Nirenberg 插值给出
\[
\|D^{q_i}u_i\|_{L^{2/a_i}}
 \le C_m
 \|u_i\|_{W^{4,\infty}}^{1-a_i}
 \|u_i\|_{H^m}^{a_i}.
\tag{A}
\]
所有 \(q_i\le4\) 的因子放入 \(L^\infty\)。

若只有一个 \(q_i>4\)，则 \(a_i\le1\)。若有 \(k\ge2\) 个这样的因子，则
\[
\sum_{q_i>4}(q_i-4)
\le m+2-4k
\le m-6<m-4,
\]
所以
\[
A:=\sum_{q_i>4}a_i<1.
\]
Hölder 不等式先把乘积置于 \(L^{2/A}\)，而闭流形上 \(L^{2/A}\hookrightarrow L^2\)。结合 (A)，得到
\[
\|P\|_2
 \le C_{m,R}\bigl(1+X_m^A\bigr)
 \le C_{m,R}(1+X_m).
\tag{B}
\]
这正是 (2.6)。这里的“两阶余量”很重要：当至少两个因子超过四阶时，\(m+2-4k\le m-6\) 严格小于 \(m-4\)。

光滑复合 \(F(G,G^{-1})\) 的高阶导数展开成同型单项式；度量正定性保证所有复合常数只依赖于 \(\lambda,R,m\)。因此该证明也覆盖 \(A=(\beta^2+\varepsilon)G^{-1}\)、\(W(G)\) 及 \(Q\) 的系数。

特别地，
\[
\sum_{j=2}^m
 \|D^jA*D^{m-j+2}G\|_2
 \le C_{m,R}(1+X_m),
\tag{C}
\]
参数常数不含 \(\varepsilon^{-1}\)。此外
\[
D^{m+1}(\beta^2)-2\beta D^{m+1}\beta
 =\sum_{k=1}^{m}c_kD^k\beta*D^{m+1-k}\beta,
\]
故
\[
\bigl\|D^{m+1}(\beta^2)-2\beta D^{m+1}\beta\bigr\|_2
 \le C_{m,R}\|\beta\|_{H^m}.
\tag{D}
\]
式 (D) 没有常数项，因为左侧在 \(\beta=0\) 时消失。

---

## 2. 最高阶能量分配

记
\[
w=\beta^2+\varepsilon.
\]

### 2.1 主度量项

展开 \(D^m(wG^{-1}D^2G)\) 后，零阶系数分配经一次分部积分给出
\[
-c\int w|D^{m+1}G|^2.
\]
一次系数微分来自
\[
D(wG^{-1})
 =2\beta D\beta\,G^{-1}+wD(G^{-1}).
\]
相应两类项分别满足
\[
\begin{aligned}
\left|\int \beta D\beta*D^mG*D^{m+1}G\right|
&\le \eta\int w|D^{m+1}G|^2
 +C_{\eta,R}\|D^mG\|_2^2,\\
\left|\int wDG*D^mG*D^{m+1}G\right|
&\le \eta\int w|D^{m+1}G|^2
 +C_{\eta,R}\|D^mG\|_2^2,
\end{aligned}
\]
使用了
\[
\frac{\beta^2}{w}\le1,\qquad 0<w\le2.
\]
其余 \(j\ge2\) 的系数微分由 (C) 控制，配对 \(D^mG\) 后得到
\[
C_{m,R}(1+\mathcal E_m).
\]
固定背景曲率产生的交换子只含不超过 \(m\) 阶的 \(G\)。

### 2.2 \(Q(G,DG)\) 项

唯一超过 \(m\) 阶的结构是
\[
w\,B(G,DG)*D^{m+1}G.
\]
因此
\[
\left|
 \int D^mG*wB*D^{m+1}G
\right|
\le
\eta\int w|D^{m+1}G|^2
+C_{\eta,R}\|D^mG\|_2^2.
\]
所有其他分配中，每个因子阶数至多为 \(m\)，总阶数至多为 \(m+2\)，故由 (B) 得到 \(C_{m,R}(1+\mathcal E_m)\)。乘在 \(R,Q\) 前的额外 \(\varepsilon\) 不改变任何常数。

### 2.3 Lie 交叉项

写成
\[
D(\beta^2)*W(G).
\]

最高 \(G\) 分配为
\[
2\beta D\beta*B(G)D^{m+1}G,
\]
可由度量耗散吸收。

最高 \(\beta\) 分配为
\[
2\int D^mG*\beta D^{m+1}\beta*W.
\]
沿产生 \(D^{m+1}\beta\) 的那个协变微分分部积分后，
\[
\begin{aligned}
&-2\int \beta D^{m+1}G*D^m\beta*W\\
&\quad
-2\int D^mG*D\beta*D^m\beta*W
-2\int D^mG*\beta D^m\beta*DW,
\end{aligned}
\]
另有固定背景曲率交换子。第一项满足
\[
\left|\int\beta D^{m+1}G*D^m\beta*W\right|
\le
\eta\int w|D^{m+1}G|^2
+C_{\eta,R}\|D^m\beta\|_2^2.
\]
其余项由
\[
W\in L^\infty,\qquad DW\in L^\infty
\]
和低阶 \(H^{s_0}\) 控制。式 (D) 控制 \(D^{m+1}(\beta^2)\) 的非线性余项。因此 Lie 项没有留下 \(D^{m+1}\beta\)。

### 2.4 输运项

令 \(V=\beta^2W(G)\)。最高纯输运项满足
\[
\int D^m\beta\,V\cdot D(D^m\beta)
 =
-\frac12\int\operatorname{div}_{\bar g}V\,|D^m\beta|^2
+\text{固定背景交换子}.
\]
由于
\[
DV=\beta D\beta*W+\beta^2DW
\]
由 \(H^{s_0}\) 控制，此项至多为 \(C_R\|\beta\|_{H^m}^2\)。

最高度量分配为
\[
\int D^m\beta*\beta^2B(G)D^{m+1}G*D\beta,
\]
并有
\[
\begin{aligned}
|\cdot|
&\le
\eta\int w|D^{m+1}G|^2
+C_{\eta,R}
 \int\frac{\beta^4}{w}|D^m\beta|^2\\
&\le
\eta\mathcal D_m^G+C_{\eta,R}\|\beta\|_{H^m}^2.
\end{aligned}
\]
其余分配再次满足 (B)。

### 2.5 标量黏性

固定背景拉普拉斯给出
\[
\nu\langle D^m\beta,D^m\bar\Delta\beta\rangle
\le
-\frac{\nu}{2}\|D^{m+1}\beta\|_2^2
+C_m\nu\|\beta\|_{H^m}^2.
\]
这里也没有出现 \(\nu^{-1}\)。

综上，对任意固定有限 \(A_m>0\)，选择各处 \(\eta\) 足够小后，
\[
\frac d{dt}\mathcal E_m
+c_{m,\lambda}\mathcal D_m^G
+c_m\nu\|D^{m+1}\beta\|_2^2
\le C_{m,R}(1+\mathcal E_m),
\tag{E}
\]
且常数与 \(0<\varepsilon,\nu\le1\) 无关。取 \(A_m=1\) 已经足够；若采用其他 \(A_m\)，Young 常数会依赖于 \(A_m\)，但不影响参数一致性。

---

## 3. 同一低阶时间区间

正文第 4 节的多项式叙述可用一个更直接的停时论证替代。

先取 \(R\) 严格大于初值 \(H^{s_0}\) 范数，并取度量邻域
\[
\lambda\bar g\le G\le\lambda^{-1}\bar g
\]
严格包含 \(g_0\)。在首次离开这两个条件之前，(E) 对 \(m=s_0\) 成立，常数为固定的 \(C_{s_0,R}\)。Grönwall 给出
\[
\sup_{t\le T}\mathcal E_{s_0}(t)
\le
\bigl(\mathcal E_{s_0}(0)+1\bigr)e^{C_{s_0,R}T}-1.
\]
另一方面，由方程和 Sobolev 乘积估计，
\[
\|\partial_tG\|_{H^{s_0-2}}
+\|\partial_t\beta\|_{H^{s_0-2}}
\le C_R,
\tag{F}
\]
而 \(s_0-2>n/2\)，所以 (F) 控制 \(G(t)-g_0\) 的 \(C^0\) 大小。选取只依赖于 datum 的 \(T_0>0\)，上述两个量在 \(T_0\) 前都不会达到预设值。

对每个固定 \((\varepsilon,\nu)\)，强抛物延拓定理只需要该参数下的椭圆性、度量正定性和足够高的 Sobolev 控制。因此所有正参数解均到达同一个 \([0,T_0]\)。随后对任意 \(m>s_0\) 在这个已经确定的区间应用 (E)，得到
\[
\sup_{t\le T_0}\mathcal E_m(t)
+\int_0^{T_0}
 \left(\mathcal D_m^G+\nu\|D^{m+1}\beta\|_2^2\right)dt
\le C_m(g_0,\chi,T_0).
\]
高阶常数依赖于 \(m\) 和光滑初值，但时间不随 \(m\) 缩短。

---

## 4. 正参数系统与趋零过程

固定 \(\varepsilon,\nu>0\) 时，主符号为
\[
\operatorname{diag}\!\left(
 wG^{ab}\xi_a\xi_b\,I_{\mathrm{Sym}^2},
 \nu\bar g^{ab}\xi_a\xi_b
\right),
\]
严格为正。Lie 项和输运项只含一阶空间导数，所以标准闭流形拟线性强抛物理论适用。标量最大值原理还给出
\[
0\le\beta_{\varepsilon,\nu}\le1.
\]

由任意阶空间估计和方程，
\[
\|\partial_tG\|_{H^{m-2}}
+\|\partial_t\beta\|_{H^{m-2}}\le C_m.
\]
对方程反复取时间导数，每次只损失有限个空间阶数，且系数中只有 \(\varepsilon,\nu\)，没有其倒数。因此可得到任意时空阶的一致控制。对一列
\[
(\varepsilon_j,\nu_j)\to(0,0)
\]
取对角子列后，
\[
(G_j,\beta_j)\longrightarrow(G,\beta)
\]
在每个有限时空 \(C^k\) 中成立。

趋零时应把全部额外项写出：
\[
\varepsilon_j
\bigl[
G_j^{-1}D^2G_j+R(G_j,G_j)+Q(G_j,DG_j)
\bigr]\to0,
\]
以及
\[
\nu_j\bar\Delta\beta_j\to0.
\]
Step 56 的 (5.2) 只显示了主度量项；\(R,Q\) 部分同样需要在文字中注明，虽然其消失是直接的。极限于是满足原 transported-cutoff 系统，并保持正定性及 \(0\le\beta\le1\)。

随后令
\[
\partial_t\varphi
=-\beta^2W(G)\circ\varphi.
\]
由
\[
\frac d{dt}(\beta\circ\varphi)
=(\beta^2W\cdot D\beta-\beta^2W\cdot D\beta)\circ\varphi=0
\]
得到 \(\beta\circ\varphi=\chi\)，而 \(g=\varphi^*G\) 满足
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]
这给出至少一个光滑 per-datum 解。

---

## 5. Galerkin 段落与文献对应

谱截断段落不能仅由“投影自伴且与 Sobolev multiplier 对易”直接推出正文的 \(D^m\)-能量公式：

- 谱投影一般不与协变微分 \(D\) 对易；
- 有限维标量方程不保留逐点最大值原理；
- 投影后的度量正定性需要在 \(C^0\) 中单独维持；
- 若改用 \((1+\bar\Delta)^{m/2}\) 能量，还需给出相应伪微分交换子估计。

这些技术可处理，但并非 Step 56 现有段落的直接推论。采用固定参数强抛物理论即可绕开该部分。

Yang 1992 的第 8 节、Theorem 8.2 明确支持退化局部 Ricci 流通过 DeTurck 与抛物正则化构造的总体思路；其 Approach 1 讨论线性化方程加入 \(\varepsilon^2\Delta h\)，Approach 2 讨论 \((\varepsilon^2+\chi^2)\operatorname{Rc}\)。该来源没有逐项给出 Step 56 的 transported-\(\beta\) 双正则系统，因此这里的 tame 乘积证明和 Lie/transport 最高阶分配仍是必要的新内容。

另有两个排版问题：式 (3.11) 中出现了损坏的 `ext{background commutators}`，式 (6.1) 的 `g\owedge g` 应改为 `g\owedge g` 对应的正确 LaTeX 命令 `g\owedge g`/项目统一使用的 Kulkarni–Nomizu 记号。它们不影响上述能量推导，但会妨碍独立阅读。