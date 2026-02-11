---
publish: 1
---

See also: [[Linear Algebra]], [[Special Matrices]], [[column space, null space, solution space]]

### 1. The Multiplicative Property (The "Powerhouse")

This is the single most useful property for algebraic proofs involving determinants.

$$\det(AB) = \det(A)\det(B)$$

This means the determinant of a product is the product of the determinants.

- **Why it matters:** It lets you break complex matrix equations into simple scalar equations.
    
- Corollary (Powers): If you multiply $A$ by itself $k$ times:
    
    $$\det(A^k) = (\det(A))^k$$
    
    This is exactly the rule used in your $A^2=A$ example.
    

### 2. The Inverse Property

If $A$ is invertible (nonsingular), then:

$$\det(A^{-1}) = \frac{1}{\det(A)}$$

- Derivation:
    
    $$A A^{-1} = I$$
    
    $$\det(A A^{-1}) = \det(I)$$
    
    $$\det(A)\det(A^{-1}) = 1 \quad (\text{Since } \det(I)=1)$$
    
    $$\det(A^{-1}) = \frac{1}{\det(A)}$$
    

### 3. The Scalar Multiplication "Trap"

This is the most common mistake students make. If you multiply the entire matrix $A$ (size $n \times n$) by a scalar constant $k$:

$$\det(kA) = k^n \det(A)$$

- Why $k^n$ and not just $k$?
    
    Recall that the determinant measures volume. If you scale a 3D box ($n=3$) by 2 in every direction ($k=2$), the volume doesn't double; it gets multiplied by $2 \times 2 \times 2 = 8$.
    
    - Example: If $\det(A) = 3$ and $A$ is $3 \times 3$, then $\det(2A) = 2^3 \cdot 3 = 8 \cdot 3 = 24$.
        

### 4. The Transpose Property

$$\det(A^T) = \det(A)$$

This means "rows and columns are equal" in the eyes of the determinant. Any rule that applies to rows (like row operations) also applies to columns.

---



|**Operation**|**Property**|**Note**|
|---|---|---|
|**Product**|$\det(AB) = \det(A)\det(B)$|Determinant of product = product of determinants.|
|**Power**|$\det(A^k) = (\det(A))^k$|Follows from product rule.|
|**Inverse**|$\det(A^{-1}) = \frac{1}{\det(A)}$|Only if $\det(A) \neq 0$.|
|**Transpose**|$\det(A^T) = \det(A)$|Rows vs Columns doesn't matter for det.|
|**Scalar Scale**|$\det(kA) = k^n \det(A)$|**Crucial:** $n$ is the dimension of the matrix.|
|**Identity**|$\det(I) = 1$|The unit volume.|
|**Orthogonal**|$\det(Q) = \pm 1$|Rotations ($+1$) or Reflections ($-1$).|

Would you like to try a "trick question" involving the **Scalar Scale** property ($\det(kA)$) to make sure you've mastered it?