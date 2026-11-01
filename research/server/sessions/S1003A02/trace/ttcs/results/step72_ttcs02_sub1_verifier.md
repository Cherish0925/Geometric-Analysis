# TTCS Independent Branch Record

```json
{
  "step_id": 72,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step72_verification_bundle.md",
    "Sessions/S1003A02/workspace/scripts/step72_weyl_deficit_identity.py",
    "Sessions/S1003A02/workspace/data/step72_weyl_deficit_identity.json",
    "Sessions/S1003A02/workspace/scripts/step72_dumbbell_numeric.py",
    "Sessions/S1003A02/workspace/data/step72_dumbbell_numeric.json"
  ]
}
```

## Task

Verify every statement (A)–(G) in this focused bundle. Check constants, conformal/Yamabe quantifiers, Ricci-flat boundary cases, dumbbell smoothness and O(1) estimates, connected-sum deficit arithmetic, the #n CPbar2 threshold, the general-type KE deficit, and the conversion to the W+ inequality in the stated endomorphism norm. Give corrected statements and concise proofs wherever needed. Do not assume the desired result.

## Output

# 科学核验备忘录

## 1. 总结

- **(A)** 正确，且只在 \(R>0\) 时可写成带 \(R\) 分母的形式。
- **(B)** 两个曲率恒等式正确；\(\mathcal E(\widehat g)\) 的公式要求 \(R(\widehat g)>0\)。唯一出现 \(R(\widehat g)=0\) 的 Yamabe 情形是 \(Y=0,d=0\)，此时 \(\widehat g\) 为 Ricci-flat，原始定义给出 \(\mathcal E=4\)。
- **(C)** 正确。条件 \(Y([g])\neq0\) 实际由 \(d([g])>0\) 自动推出。
- **(D)** 正确。关键补充是：在每个 \(d>0\) 的共形类内，Yamabe 度量确实使 \(\mathcal E\) 取该共形类的下确界；\(Y=0\) 类、非 Yamabe 代表元和 Ricci-flat 度量都不会产生小于 \(1\) 的值。
- **(E)** 理论构造正确。数值脚本中的 quintic 拼接只有 \(C^2\)，不能直接充当光滑度量；改用端点处无限阶平坦的 \(C^\infty\) 截断函数后，全部 \(O(1)\) 估计和极限保持不变。
- **(F)** 正确，系数 \(16\pi^2\) 正确。
- \(\#_n\overline{\mathbb{CP}}^2\) 的阈值 \(n=4\) 正确。
- Kähler–Einstein 部分的 \(d=4\pi^2A/3\) 及吹起后的下界正确。
- **(G)** 正确，但其前一行的 signature 公式少了因子 \(1/3\)：
  \[
  \tau(X\#k\overline{\mathbb{CP}}^2)
  =\frac{A-2\chi(X)}3-k.
  \]
  在会话采用的曲率算子范数下，右端确为 \(2\pi^2(A-k)\)。

---

## 2. 泛函本身与 \(R=0\) 情形

由
\[
\int|\operatorname{Ric}-\lambda g|^2
=R-2\lambda T_s+4\lambda^2V
\]
并令 \(x=\lambda^{-1}\)，得到
\[
\mathcal E
=\inf_{x\neq0}\left(4-\frac{2T_s}{V}x+\frac RVx^2\right).
\]
当 \(R>0\) 时，
\[
\mathcal E=4-\frac{T_s^2}{RV}
=\frac{4R-T_s^2/V}{R}
=\frac{4P+L_s}{R}.
\]
若 \(T_s=0\)，二次式的极小点为 \(x=0\)，它不对应有限的 \(\lambda\)，但下确界仍是上述数值。

若 \(R=0\)，则 \(\operatorname{Ric}\equiv0\)，因而
\[
\mathcal E
=\frac{\int|\lambda g|^2}{\lambda^2V}=4.
\]
同时 \(s=P=S=T_s=L_s=0\)，Gauss–Bonnet 给出
\[
\mathcal W=8\pi^2\chi,\qquad d=0.
\]
该 Ricci-flat 度量也是 \(Y=0\) 的 Yamabe 度量。于是 \(R=0\) 不会降低 \(\alpha\)。

---

## 3. (A)–(D)

### (A)

由
\[
8\pi^2\chi=\mathcal W+\frac S{24}-\frac P2
\]
直接得到
\[
P=\frac S{12}+2\mathcal W-16\pi^2\chi,
\]
以及
\[
R=P+\frac S4=\frac S3+2\mathcal W-16\pi^2\chi.
\]
当 \(R>0\) 时，
\[
\begin{aligned}
R(\mathcal E-1)
&=4P+L_s-R\\
&=3P+L_s-\frac S4\\
&=6\mathcal W-48\pi^2\chi+L_s.
\end{aligned}
\]
因此
\[
\boxed{\mathcal E-1
=\frac{6(\mathcal W-8\pi^2\chi)+L_s}{R}}.
\]
脚本 `step72_weyl_deficit_identity.py` 对这一消元给出的精确残差为零。

### (B)

在 Yamabe 代表元 \(\widehat g\) 上，标量曲率为常数，故
\[
S(\widehat g)=Y([g])^2,\qquad L_s(\widehat g)=0.
\]
写
\[
d=8\pi^2\chi-\mathcal W,
\]
则
\[
P(\widehat g)=\frac{Y^2}{12}-2d,
\qquad
R(\widehat g)=\frac{Y^2}{3}-2d.
\]
这与原式
\[
R(\widehat g)=\frac{Y^2}{3}+2\mathcal W-16\pi^2\chi
\]
完全相同。若 \(R(\widehat g)>0\)，则
\[
\boxed{\mathcal E(\widehat g)=1-\frac{6d}{R(\widehat g)}}.
\]

若 \(Y=0\)，则 \(P(\widehat g)=-2d\ge0\)，所以 \(d\le0\)：

- \(d<0\) 时，\(R=P=-2d>0\)，且 \(\mathcal E(\widehat g)=4\)；
- \(d=0\) 时，\(P=R=0\)，\(\widehat g\) 为 Ricci-flat，原始定义仍给出 \(\mathcal E=4\)。

特别地，\(d>0\) 自动推出 \(Y\neq0\)。

### (C)

若 \(\alpha<1\)，则存在某个度量满足 \(\mathcal E<1\)。它不可能是 Ricci-flat，所以可应用 (A)：
\[
-6d+L_s<0.
\]
于是
\[
d>\frac{L_s}{6}\ge0.
\]
该共形类有
\[
\mathcal W<8\pi^2\chi,
\]
且由上面的 \(Y=0\) 分析可知 \(Y\neq0\)。

反之，若某个共形类有 \(d>0\)，其 Yamabe 代表元满足 \(Y\neq0\)、\(R>0\)，而 (B) 给出
\[
\mathcal E(\widehat g)=1-\frac{6d}{R(\widehat g)}<1.
\]
所以
\[
\boxed{
\alpha<1
\iff
\exists[g]\colon
Y([g])\neq0,\quad
\mathcal W([g])<8\pi^2\chi }.
\]
其中 \(Y\neq0\) 是冗余但正确的条件。

### (D)：非 Yamabe 代表元为何不能给出更小值

对任意共形类及其中任意度量 \(g\)，有
\[
\int s_g^2\,d\mu_g\ge Y([g])^2.
\]
证明分两种符号：

- 若 \(Y>0\)，在 Yamabe 商中取测试函数 \(u=1\)，得到
  \[
  Y\le \frac{T_s}{\sqrt V}\le\sqrt S.
  \]
- 若 \(Y\le0\)，记 \(s_-=\max\{-s,0\}\)。对任意 \(u\)，
  \[
  Q_g(u)\ge-\frac{\int s_-u^2}{\|u\|_4^2}
  \ge-\|s_-\|_2,
  \]
  因而 \(|Y|\le\|s_-\|_2\le\sqrt S\)。

在固定共形类内 \(d\) 不变，且
\[
R_g=\frac{S_g}{3}-2d
\ge\frac{Y^2}{3}-2d=R_{\widehat g}.
\]
若 \(d>0\)，则
\[
P(\widehat g)=\frac{Y^2}{12}-2d\ge0,
\]
所以 \(Y^2\ge24d\) 且 \(R_{\widehat g}\ge6d>0\)。对任意代表元，
\[
\mathcal E(g)
=1-\frac{6d-L_s(g)}{R_g}
\ge 1-\frac{6d}{R_{\widehat g}}
=\mathcal E(\widehat g).
\]
若 \(d\le0\)，则由 (A)
\[
\mathcal E(g)-1=\frac{-6d+L_s}{R_g}\ge0
\]
；Ricci-flat 代表元的值则为 \(4\)。

因此 Yamabe 度量在每个 \(d>0\) 的共形类内给出 \(\mathcal E\) 的最小值，而 \(d\le0\) 的类不能给出小于 \(1\) 的值。结合 (E) 的 \(\alpha\le1\)，得到
\[
\boxed{
\alpha
=
1-6\max\left\{
0,\ 
\sup_{\,[g]:Y([g])\neq0}
\frac{d([g])}{P(\widehat g)+Y([g])^2/4}
\right\}.}
\]
不同 Yamabe 代表元不会造成歧义，因为分母由 \(Y^2\) 和共形不变量 \(d\) 唯一确定。

---

## 4. Dumbbell 构造与 (E)

对
\[
g=dr^2+f(r)^2g_{S^3(1)}
\]
有
\[
K_{0a}=-\frac{f''}{f},\qquad
K_{ab}=\frac{1-(f')^2}{f^2}.
\]
在 \(f\equiv1\) 的圆柱上，
\[
\operatorname{Ric}=(0,2,2,2),\qquad s=6,
\]
从而
\[
|\operatorname{Ric}|^2=12,\qquad
|\operatorname{Ric}^\circ|^2=3.
\]
因为 \(\operatorname{Vol}(S^3)=2\pi^2\)，每单位长度贡献
\[
V=2\pi^2,\quad T_s=12\pi^2,\quad
S=72\pi^2,\quad
P=6\pi^2,\quad R=24\pi^2.
\]

在 \(f>0\) 处令 \(dt=dr/f\)，则
\[
g=f^2(dt^2+g_{S^3})
=f^2\rho^{-2}(d\rho^2+\rho^2g_{S^3}),\qquad \rho=e^t,
\]
所以该 warped product 共形平坦。取 \(f=\sin r\) 于两个极点附近可保证极点光滑。

将所有固定部分及在 \(M\) 上的固定连通和拼接记入常数，可写成
\[
\begin{aligned}
V&=vL+V_0,&T_s&=6vL+T_0,\\
S&=36vL+S_0,&P&=3vL+P_0,\\
R&=12vL+R_0,
\end{aligned}
\qquad v=2\pi^2.
\]
于是有精确展开
\[
L_s
=S_0-12T_0+36V_0
-\frac{(T_0-6V_0)^2}{vL+V_0}
=O(1).
\]
因此
\[
\mathcal E
=\frac{12vL+4P_0+O(1)}{12vL+R_0}
\longrightarrow1.
\]

用固定球、固定颈部和固定的 \(M\setminus B^4\) 替换一个帽内区域时，所有被替换区域均与 \(L\) 无关，因此 \(V,T_s,S,P,R\) 的变化均为固定常数。拓扑上
\[
M\#S^4\cong M.
\]
故
\[
\boxed{\alpha(M)\le1}
\]
对每个闭四维流形成立。

数值文件中 Gauss–Bonnet 残差约为 \(10^{-13}\)，且 \(P/L\)、\(R/L\) 分别趋向 \(6\pi^2\)、\(24\pi^2\)，\(\mathcal E\) 趋向 \(1\)。但脚本的 quintic smoothstep 在拼接点只匹配到二阶导数。理论构造应改用端点处无限阶平坦的 \(C^\infty\) 截断函数；这只改变固定帽常数，不改变上述渐近式。

---

## 5. \(T_{\min}\le0\) 时的值与达到性

由 signature 公式，
\[
\mathcal W\ge12\pi^2|\tau|.
\]
因此
\[
\mathcal W-8\pi^2\chi
\ge12\pi^2|\tau|-8\pi^2\chi
=-4\pi^2T_{\min}.
\]
若 \(T_{\min}\le0\)，则所有 \(R>0\) 度量满足 \(\mathcal E\ge1\)，而 Ricci-flat 度量有 \(\mathcal E=4\)。结合 dumbbell，
\[
\alpha=1.
\]

- 若 \(T_{\min}<0\)，则上式严格为正，所以每个度量都有 \(\mathcal E>1\)；下确界 \(1\) 不由单个度量实现。
- 若 \(T_{\min}=0\)，则 \(\mathcal E=1\) 等价于
  \[
  \mathcal W=12\pi^2|\tau|=8\pi^2\chi,\qquad L_s=0.
  \]
  第一式等价于某一 Weyl chirality 消失，第二式等价于标量曲率常数。该常数不能为零，否则 Gauss–Bonnet 同时给出 \(P=0\) 和 \(R=0\)，而 Ricci-flat 度量的 \(\mathcal E\) 是 \(4\)。故对应共形类有 \(Y\neq0\)。

反过来，若存在半共形平坦且 \(Y\neq0\) 的共形类，其 Yamabe 代表元满足上述两个等式。因此 bundle 中关于达到性的叙述正确，且这里的“严格”应理解为 \(T_{\min}<0\)。

---

## 6. (F) 与 \(\#_n\overline{\mathbb{CP}}^2\)

Kobayashi 连通和不等式给出
\[
\mathcal W_*(M\#N)\le\mathcal W_*(M)+\mathcal W_*(N).
\]
所以
\[
\begin{aligned}
d_*(M\#N)
&=8\pi^2(\chi(M)+\chi(N)-2)-\mathcal W_*(M\#N)\\
&\ge d_*(M)+d_*(N)-16\pi^2.
\end{aligned}
\]
即
\[
\boxed{d_*(M\#N)\ge d_*(M)+d_*(N)-16\pi^2.}
\]

对 \(\overline{\mathbb{CP}}^2\)，\(\chi=3,\tau=-1\)。Signature 给出
\[
\mathcal W\ge12\pi^2,
\]
反向定向的 Fubini–Study 度量取等号，故
\[
\mathcal W_*(\overline{\mathbb{CP}}^2)=12\pi^2,\qquad
d_*=24\pi^2-12\pi^2=12\pi^2.
\]
迭代 (F) 得
\[
d_*(\#_n\overline{\mathbb{CP}}^2)
\ge12n\pi^2-16(n-1)\pi^2
=(16-4n)\pi^2.
\]
于是 \(n=1,2,3\) 时 \(d_*>0\)，由 (C)
\[
\alpha<1.
\]

另一方面
\[
\chi(\#_n\overline{\mathbb{CP}}^2)=n+2,\qquad
\tau=-n,
\]
故
\[
T_{\min}=2(n+2)-3n=4-n.
\]
当 \(n\ge4\) 时，上一节给出
\[
\boxed{\alpha(\#_n\overline{\mathbb{CP}}^2)=1.}
\]
阈值 \(n=4\) 完全正确。

---

## 7. Kähler–Einstein 曲面与 (G)

这里需明确假设：\(X\) 携带光滑 Kähler–Einstein 度量
\[
\operatorname{Ric}=\lambda g,\qquad \lambda<0.
\]
仅有“minimal general type”并不自行提供这一个光滑度量。

令 \(A=c_1^2(X)>0\)。Ricci 形式满足
\[
\rho=\lambda\omega,\qquad [\rho]=2\pi c_1(X),
\]
所以
\[
A=\frac1{4\pi^2}\int\rho\wedge\rho
=\frac{\lambda^2}{4\pi^2}\int\omega^2
=\frac{\lambda^2V}{2\pi^2}.
\]
而
\[
R=\int|\operatorname{Ric}|^2=4\lambda^2V=8\pi^2A.
\]
Einstein 度量有 \(P=L_s=0\)，由 (A) 得 \(d=R/6\)，因而
\[
\boxed{d=\frac{4\pi^2A}{3}.}
\]

迭代 (F)：
\[
\begin{aligned}
d_*(X\#k\overline{\mathbb{CP}}^2)
&\ge d_*(X)+k(12\pi^2)-16k\pi^2\\
&\ge \frac{4\pi^2A}{3}-4k\pi^2\\
&=4\pi^2\left(\frac A3-k\right).
\end{aligned}
\]
故 \(k<A/3\) 时 \(\alpha<1\)。

取复杂定向。正确的 signature 算术是
\[
A=2\chi(X)+3\tau(X),
\qquad
\tau(X\#k\overline{\mathbb{CP}}^2)
=\frac{A-2\chi(X)}3-k.
\]
同时
\[
2\chi(X\#k\overline{\mathbb{CP}}^2)
+3\tau(X\#k\overline{\mathbb{CP}}^2)=A-k.
\]

记
\[
U(g)=\int|W^+|^2,\qquad D(g)=\int|W^-|^2.
\]
由
\[
U-D=12\pi^2\tau,\qquad \mathcal W=U+D
\]
得到
\[
\mathcal W=2U-12\pi^2\tau.
\]
因此逐度量有
\[
\begin{aligned}
\mathcal W<8\pi^2\chi
&\iff
2U-12\pi^2\tau<8\pi^2\chi\\
&\iff
U<4\pi^2\chi+6\pi^2\tau\\
&\iff
U<2\pi^2(2\chi+3\tau)\\
&\iff
U<2\pi^2(A-k).
\end{aligned}
\]
取下确界后即得
\[
\boxed{
\inf_g\int|W^+|^2
<2\pi^2(A-k).}
\]
所以 (G) 的常数正确；bundle 中只有其前置 signature 行漏写了 \(1/3\)。

若文献采用
\[
|W|_{(0,4)}^2=4|W|_{\mathrm{end}}^2,
\]
则同一不等式写成
\[
\inf_g\int|W^+|_{(0,4)}^2<8\pi^2(A-k).
\]
相应的 Gauss–Bonnet 与 signature 公式也必须在 Weyl 项前加入 \(1/4\)，不能把两种范数的公式交叉使用。