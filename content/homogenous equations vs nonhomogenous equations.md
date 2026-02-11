---
publish: 1
tags:
  - topic/math
---

See also: [[Linear Algebra]], [[column space, null space, solution space]], [[variation of parameters]]

### The Comparison: $AX=0$ vs. $AX=b$

Here is the structured reconstruction of the concepts on the board:

| **Feature**          | **Homogeneous System**                                                                                                                          | **Nonhomogeneous System**                                                                                                                                           |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Form**             | $$AX = 0$$                                                                                                                                      | $$AX = b$$                                                                                                                                                          |
| **Consistency**      | **Always consistent.**<br><br>  <br><br>_(Why? Because the zero vector $\vec{0}$ is always a solution. This is called the "trivial solution".)_ | **Maybe consistent or inconsistent.**<br><br>  <br><br>_(If $b$ is outside the column space of $A$, there is no solution.)_                                         |
| **Solution Set**     | **Is a Subspace.**<br><br>  <br><br>The set of solutions forms the Null Space, $N(A)$. It passes through the origin.                            | **Is NOT a Subspace** (if $b \neq 0$).<br><br>  <br><br>It does not contain the zero vector, and adding two solutions yields a vector that is no longer a solution. |
| **General Solution** | $$X_h = c_1v_1 + \dots + c_kv_k$$<br><br>  <br><br>(Linear combination of basis vectors)                                                        | $$X_g = X_p + X_h$$<br><br>  <br><br>(Particular Solution + Homogeneous Solution)                                                                                   |

---

### The "Deep Dive": Why isn't $AX=b$ a Subspace?

The board presents a mini-proof in the third row that is very important for understanding "Linearity."

For a set of vectors to be a **Subspace**, it must satisfy two main rules:

1. **Closure under Addition:** If $x_1$ and $x_2$ are solutions, then $x_1 + x_2$ must be a solution.
    
2. **Closure under Scalar Multiplication:** If $x$ is a solution, then $c \cdot x$ must be a solution.
    

Why Homogeneous ($AX=0$) works:

If $Ax_1 = 0$ and $Ax_2 = 0$, then:

$$A(x_1 + x_2) = Ax_1 + Ax_2 = 0 + 0 = 0$$

The sum is still a solution.

Why Nonhomogeneous ($AX=b$) fails:

The board explicitly writes this derivation. If $Ax_1 = b$ and $Ax_2 = b$, look what happens when you add them:

$$A(x_1 + x_2) = Ax_1 + Ax_2 = b + b = 2b$$

Since $2b \neq b$ (assuming $b \neq 0$), the sum is not a solution. The set is "broken" under addition.

> **Geometric Intuition:**
> 
> - The solution to $AX=0$ is a **line (or plane) passing through the origin**.
>     
> - The solution to $AX=b$ is that same line (or plane), but **shifted** away from the origin by the vector $X_p$. Since it doesn't go through the origin, it can't be a subspace. (Mathematically, we call this an _Affine Space_).
>     

### The "Engineering" Connection: $X_g = X_p + X_h$

The final row ($X_g = X_p + X_h$) is a concept you will see repeatedly, not just in Linear Algebra, but in **Differential Equations** and Control Theory.

The logic is:

To describe all possible solutions to the complex problem ($AX=b$), you only need:

1. **One** single specific working example ($X_p$, the Particular solution).
    
2. **All** the ways you can have "zero effect" ($X_h$, the Null space).
    

You essentially say: "Here is one path to the target $b$, and from there, I can move anywhere along the 'zero' directions without messing up my target."

Bkz: [[Matematik]] • [[Engineering]] • [[Feynman]]