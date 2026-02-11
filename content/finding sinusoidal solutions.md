---
publish: 1
---

![[Pasted image 20250227124733.png]]
**Sinusoidal Solution:** The particular solution is `X = (jwI - A)^(-1)BU`. This gives us the complex vector `X`, which tells us the amplitude and phase of the state variables' sinusoidal responses. The full time-domain solution for the state vector is then `x(t) = Xe^(jwt)`.

**Existence Condition:** The solution exists _only if_ the matrix `(jwI - A)` is invertible. A matrix is invertible if and only if its determinant is non-zero. Therefore, the solution is valid when: `det(jwI - A) ≠ 0`
But this is equivalent to saying that the `jw` is not an eigenvalue of A. The eigenvalues of A represent the system's natural frequencies.  
So If the input frequency `w` is such that `jw` equals one of the eigenvalues of `A`, then `det(jwI - A) = 0`, the inverse doesn't exist, and the solution blows up (becomes infinitely large). This is the phenomenon of _resonance_. The system is being driven at one of its natural frequencies, leading to an unbounded response. Everything goes boom. 