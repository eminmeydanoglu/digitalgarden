---
publish: 1
---

A **causal system** is one where the **output at any time depends only on the present and past values** of the input, **not future values**. This means that the system does not "anticipate" future inputs.

> Present and past effects, future doesnt effect -> casual


- **All real-time physical systems are causal**. Since time only moves forward, **effect always follows cause** in physical systems.
- All [[memoryless systems]]  are causal. A **memoryless system** is one where the output depends **only on the current input value**, meaning it does not rely on past or future inputs.

Maybe the independent variable is not time. Then, causality is not an essential constraint. 
- In image processing, we can move both left and right, up and down.

 y[n]=x[n]−x[n+1], y(t)=x(t+1): Non causal (not )

y[n]=x[−n] ? 
Is fine in terms of causality if n > 0. But if n<0, then it behaves by the future inputs. Than this system is not causal. 

y(t)=x(t)cos(t+1)?
	The cosine function cos⁡(t+1) is simply a **time-varying multiplier** and does not introduce dependency on future values of x(t). The system is **causal** and **memoryless**.


[[Casuality of linear systems]]
