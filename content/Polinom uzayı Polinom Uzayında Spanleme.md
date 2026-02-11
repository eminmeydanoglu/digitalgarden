---
publish: 1
entity_extraction_done: true
---

See also: [[Linear Algebra]], [[basis vectors]], [[column space, null space, solution space]]

## 1. The Problem Statement

**Objective:**
Let $V$ be the vector space $P_2$ (polynomials of degree at most 2).
Given the set $S = \{\vec{v}_1, \vec{v}_2\}$ where:
* $\vec{v}_1 = t^2 + 2t + 1$
* $\vec{v}_2 = t^2 + 2$

**Question:** Does the set $S$ span the entire vector space $V$? (i.e., Is $\text{Span}(S) = P_2$?)

---

## 2. Theoretical Approach

To span $P_2$, *any* arbitrary polynomial $\vec{v} = At^2 + Bt + C$ must be expressible as a linear combination of $\vec{v}_1$ and $\vec{v}_2$.

$$\vec{v} = a\vec{v}_1 + b\vec{v}_2$$

Where $a, b$ are scalars to be determined, and $A, B, C$ are arbitrary constants representing any possible polynomial in the universe of $P_2$.

---

## 3. The Derivation

### Step A: Expanding the Equation
We substitute the vectors into the linear combination formula:

$$At^2 + Bt + C = a(t^2 + 2t + 1) + b(t^2 + 2)$$

Regrouping the terms on the right side by powers of $t$:

$$At^2 + Bt + C = t^2(a + b) + t(2a) + (a + 2b)$$

### Step B: System of Linear Equations
By comparing coefficients on both sides, we generate the system:

1.  **$t^2$ term:** $a + b = A$
2.  **$t$ term:** $2a = B$
3.  **Constant term:** $a + 2b = C$

### Step C: Solving for Scalars
From equation (2), we isolate $a$:
$$a = \frac{B}{2}$$

Substitute $a$ into equation (1) to find $b$:
$$\frac{B}{2} + b = A \implies b = A - \frac{B}{2}$$

### Step D: The Consistency Check (The Trap)
Now, we must verify if these scalar values satisfy the 3rd equation (the constant term).
$$C = a + 2b$$
Substitute our found values:
$$C = \frac{B}{2} + 2\left(A - \frac{B}{2}\right)$$
$$C = \frac{B}{2} + 2A - B$$
$$C = 2A - \frac{B}{2} = \frac{4A - B}{2}$$

---

## 4. The Conclusion & Counter-Example

**The Result:**
The system is consistent **ONLY IF** the polynomial's coefficients satisfy the specific relationship $C = \frac{4A - B}{2}$.
Since a general polynomial in $P_2$ (like $t^2 + t + 100$) does not necessarily obey this rule, the system is generally inconsistent.

**Formal Answer:**
$$\text{Span}(S) \neq P_2$$

**Counter-Example Proof:**
Consider the polynomial $\vec{p} = t^2 + 2t + 3$.
* Here, $A=1, B=2, C=3$.
* According to our constraint, $C$ must be: $\frac{4(1) - 2}{2} = 1$.
* However, our actual $C$ is $3$.
* Since $3 \neq 1$, this polynomial cannot be built using $\vec{v}_1$ and $\vec{v}_2$.

---

## 5. Key Takeaway for Engineering

**The Dimensionality Rule:**
The vector space $P_2$ is isomorphic to $\mathbb{R}^3$ (it has 3 dimensions: $t^2, t, 1$).
To span a 3-dimensional space, you generally need **at least 3 linearly independent vectors**.

In this problem, we were given only **2 vectors**. Geometrically, this means $\{\vec{v}_1, \vec{v}_2\}$ creates a 2D plane cutting through the 3D space of polynomials. We can reach any point *on* that plane, but we cannot reach points (polynomials) that float "above" or "below" it.

> **Rule of Thumb:** If the number of vectors in your set is less than the dimension of the space ($n < \dim(V)$), the set cannot span $V$. It can only form a subspace.