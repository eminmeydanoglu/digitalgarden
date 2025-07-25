---
publish: 1
---

 The transfer function, `H(jw)`, equaling to Y/U, is a [[frequency domain]] representation of the system's input-output relationship.

 ![[Pasted image 20250227131149.png]]
 where 
 ![[Pasted image 20250227131213.png]]
 
 It can be derived directly from the state-space matrices `A`, `B`, `C`, and `D`.
It's a _matrix_ transfer function if we have multiple inputs and outputs (MIMO). In the SISO case, it becomes a scalar function.

---
Lets analyze this:
![[Pasted image 20250307140123.png]]
1. H is in complex domain. U is in complex domain. 
2. **cos(ωt + ∠H(jω) + ∠U(jω))**: The output is a cosine wave with the original frequency (ω) but with a phase shift equal to the sum of the phase shifts introduced by the system and the input signal.