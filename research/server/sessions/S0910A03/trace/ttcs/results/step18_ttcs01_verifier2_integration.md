# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 18,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step18_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step18_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the topological-uniformity correction for the critical Ishida–LeBrun family. Derive c2≤5c1²+36 for each minimal complex surface of general type from Noether's formula and Noether's inequality, then compute χ(M)/A for M=(#_{j=1}^m X_j)#N, m=2 or 3, using exact connected-sum formulas and D=4m-(2χ+3τ)(N)=A/3. Determine under the actual standard hypotheses on N in the Ishida–LeBrun construction whether χ(N)/A is automatically bounded above; distinguish what follows from D alone, from negative-definiteness/b1 assumptions, and from the common choices of N. Correct any convention mismatch. The aim is an exact, reusable bound or a precise statement of the missing N input.

## Integrated Scientific Memo

## 核验结论

令
\[
a_j=c_1^2(X_j),\qquad e_j=c_2(X_j)=\chi(X_j),\qquad
A=\sum_{j=1}^m a_j,\qquad m\in\{2,3\}.
\]

若每个 \(X_j\) 都是极小一般型复曲面，且 \(N\) 满足 Ishida–LeBrun Einstein 障碍定理中的实际假设 \(b_+(N)=0\)，则临界关系
\[
D:=4m-(2\chi+3\tau)(N)=\frac A3
\]
确实自动给出 \(\chi(N)/A\) 的统一上界，并最终得到
\[
\boxed{\frac{\chi(M)}A\le \frac{65}{6}}.
\]
因此这里没有遗漏额外的 \(N\)-假设；真正必须显式保留的是 \(X_j\) 为一般型，从而可使用 Noether 不等式。此前将该上界归因于 BMY 是方向错误。

---

### 1. Noether 上界

对极小一般型复曲面 \(X\)，记
\[
p_g=h^{2,0}(X),\qquad q=h^{1,0}(X),\qquad
\chi_h=1-q+p_g.
\]
Noether 公式与 Noether 不等式分别为
\[
c_1^2+c_2=12\chi_h,\qquad c_1^2\ge 2p_g-4.
\]
所以
\[
p_g\le \frac{c_1^2+4}{2},\qquad
\chi_h\le1+p_g\le\frac{c_1^2+6}{2}.
\]
代回 Noether 公式：
\[
c_2=12\chi_h-c_1^2
\le 6(c_1^2+6)-c_1^2
=\boxed{5c_1^2+36}.
\]
求和得到
\[
\boxed{\sum_{j=1}^m c_2(X_j)\le 5A+36m.}
\]

这不是 BMY 的推论。BMY 给出
\[
c_1^2\le3c_2,
\]
即 \(c_2\ge c_1^2/3\)，方向与所需的 Euler 特征数上界相反。

---

### 2. 精确连通和公式

对
\[
M=\left(\#_{j=1}^mX_j\right)\#N
\]
共有 \(m+1\) 个 summand、进行了 \(m\) 次连通和，故
\[
\boxed{\chi(M)=\sum_{j=1}^m c_2(X_j)+\chi(N)-2m.}
\]
签名可加，而一般型曲面满足
\[
(2\chi+3\tau)(X_j)=c_1^2(X_j),
\]
因此
\[
(2\chi+3\tau)(M)
=A+(2\chi+3\tau)(N)-4m=A-D.
\]
在 \(D=A/3\) 时，
\[
(2\chi+3\tau)(M)=\frac{2A}{3}.
\]

---

### 3. \(D\) 单独能推出什么

一般闭定向四流形满足
\[
\chi(N)=2-2b_1+b_++b_-,
\qquad
\tau(N)=b_+-b_-.
\]
所以
\[
(2\chi+3\tau)(N)=4-4b_1+5b_+-b_-,
\]
以及
\[
D=4(m-1)+4b_1-5b_++b_-.
\]
由 \(D=A/3\) 消去 \(b_-\)，得到精确恒等式
\[
\boxed{\chi(N)=\frac A3+6-4m+6\bigl(b_+(N)-b_1(N)\bigr).}
\tag{1}
\]

故：

- **仅有 \(D=A/3\)** 时，\(b_+-b_1\) 未受控制，不能推出 \(\chi(N)/A\) 的统一上界。
- **仅有 \(b_1(N)=0\)** 也不够，因为 \(b_+\) 仍可增大。
- 一般化情形所需的准确附加输入是
  \[
  \frac{b_+(N)-b_1(N)}A
  \]
  的上界；例如 \(b_+(N)/A\) 的上界即充分。

---

### 4. Ishida–LeBrun 的实际 \(N\)-假设

所给论文的 Theorem D 明确假设 \(b_+(N)=0\)。Theorem C 假设 \(N\) 承载正标量曲率的反自对偶度量，论文亦指出这蕴含 \(b_+(N)=0\)。

令 \(b_+=0\)，则 (1) 化为
\[
\boxed{\chi(N)=\frac A3+6-4m-6b_1(N).}
\tag{2}
\]
特别地，对 \(m=2,3\)，
\[
\boxed{\frac{\chi(N)}A\le\frac13.}
\]
因此实际标准假设已经自动控制 \(\chi(N)/A\)，完全不需要再假设 \(b_1(N)=0\)。

此时
\[
\boxed{D=4(m-1)+4b_1(N)+b_-(N).}
\tag{3}
\]
临界条件还给出
\[
A=12(m-1)+12b_1(N)+3b_-(N),
\]
故
\[
\boxed{A\ge12(m-1).}
\tag{4}
\]

---

### 5. 约定错位的修正

若 \(N\) 负定且 \(b_1(N)=0\)，写 \(k=b_-(N)=b_2(N)\)，则
\[
\chi(N)=2+k,\qquad \tau(N)=-k,
\]
且
\[
(2\chi+3\tau)(N)=4-k.
\]
因此
\[
\boxed{D=4(m-1)+k,}
\]
而不是 \(D=k\)。临界时
\[
\boxed{k=\frac A3-4(m-1),}
\qquad
\boxed{\chi(N)=\frac A3+6-4m.}
\]
遗漏的 \(4(m-1)\) 正是当前 \(D=4m-(2\chi+3\tau)(N)\) 约定下的连通和修正项。

---

### 6. 常用 \(N\) 的精确公式

对论文 Corollary 16 中的常见选择
\[
N=k\,\overline{\mathbb{CP}}{}^2\#
\ell(S^1\times S^3),
\]
有
\[
b_1(N)=\ell,\qquad b_+(N)=0,\qquad b_-(N)=k,
\]
以及
\[
\chi(N)=2+k-2\ell,\qquad \tau(N)=-k.
\]
故
\[
\boxed{D=4(m-1)+k+4\ell.}
\]
临界时
\[
\boxed{k+4\ell=\frac A3-4(m-1)}
\]
且
\[
\boxed{\chi(N)=\frac A3+6-4m-6\ell.}
\]

---

### 7. \(\chi(M)/A\) 的可复用上界

记
\[
C=\sum_{j=1}^m c_2(X_j).
\]
由连通和公式和 (2)，
\[
\chi(M)=C+\frac A3+6-6m-6b_1(N),
\]
即
\[
\boxed{
\frac{\chi(M)}A
=\frac CA+\frac13+
\frac{6-6m-6b_1(N)}A.
}
\tag{5}
\]
使用 \(C\le5A+36m\)，得到
\[
\boxed{
\frac{\chi(M)}A
\le
\frac{16}{3}
+\frac{30m+6-6b_1(N)}A.
}
\tag{6}
\]
再用 \(A\ge12(m-1)\) 并舍去有利的 \(-6b_1/A\) 项：
\[
m=2:\qquad
\frac{\chi(M)}A\le
\frac{16}{3}+\frac{66}{12}
=\boxed{\frac{65}{6}},
\]
\[
m=3:\qquad
\frac{\chi(M)}A\le
\frac{16}{3}+\frac{96}{24}
=\boxed{\frac{28}{3}}.
\]
因此两种情形可统一写为
\[
\boxed{\frac{\chi(M)}A\le\frac{65}{6}.}
\]

---

### 8. 精确适用范围

该统一常数要求：

1. 每个 \(X_j\) 是极小一般型复曲面，以便使用
   \[
   c_2(X_j)\le5c_1^2(X_j)+36;
   \]
2. \(N\) 满足 \(b_+(N)=0\)，这正是 Ishida–LeBrun Theorem D 的假设，也是 Theorem C 的几何假设所蕴含的结论；
3. \(D=A/3\)。

若只采用 Theorem D 更广的 almost-complex summand 范围，而不要求 \(X_j\) 一般型，则上述上界并不自动成立：必须另行假设
\[
\frac{\sum_j\chi(X_j)}A
\]
有统一上界。特别是允许 \(c_1^2=0\) 而 Euler 特征数增大的非一般型曲面时，该比值可失控。

因此 Step 17 中“BMY 自动给出所需 bounded \(\chi/A\)”应改为：

> 对极小一般型 \(X_j\)，Noether 公式与 Noether 不等式控制 \(\sum c_2(X_j)/A\)；对标准 Ishida–LeBrun 的 \(N\)，\(b_+(N)=0\) 与临界关系控制 \(\chi(N)/A\)。二者合起来给出 \(\chi(M)/A\le65/6\)。BMY 只提供相反方向的下界，不能承担该论证。