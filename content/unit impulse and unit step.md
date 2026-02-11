---
sr-due: 2025-04-13
sr-interval: 4
sr-ease: 270
publish: 1
tags:
  - topic/signals
  - topic/engineering
entity_extraction_done: true
---

 
### Unit impulse (sample)
![[Pasted image 20250309141523.png]]

### Unit step 
You take a step, and you never go back. Always 1 afterwards. 
![[Pasted image 20250309141545.png]]

1. the discrete-time unit impulse is the first difference of the discrete-time step 
![[Pasted image 20250309141645.png]]
or the derivative! 
![[Pasted image 20250309142531.png]]


2. discrete-time unit step is the running sum of the unit sample. That is,

![[Pasted image 20250309141702.png]]
or the running integral!
![[Pasted image 20250309142501.png]]

3. The unit impulse sequence can be used to sample the value of a signal at n = 0. In particular, since 8[n] is nonzero (and equal to 1) only for n = 0, it follows that
![[Pasted image 20250309142307.png]]
Or, 
![[Pasted image 20250309143641.png]]

Bkz: [[Matematik]] • [[Engineering]] • [[Fizik]]