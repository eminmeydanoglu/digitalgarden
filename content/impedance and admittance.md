---
publish: 1
entity_extraction_done: true
---

[[combining impedances and admittances in series and parallel]]
[[understanding the phase angle]]
[[quality factor]]

---
### impedance 
Impedance Z is essentially the ratio of the voltage across a circuit element to the current through it when we are dealing with sinusoidal signals. It is resistance generalized for AC. 
Z=V/I.
Of course these are in phasors, [[frequency domain]] 
![[Pasted image 20250309154137.png]]

### `Z = V/I = R + jX`
1. The `jX` term in the impedance equation `Z = V/I = R + jX` represents the _imaginary_ part of the impedance, called [[reactance]]
2. Reactance, like resistance, is measured in ohms. However, unlike resistance (which dissipates energy as heat), reactance _stores_ energy in either an electric field (in a capacitor) or a magnetic field (in an inductor).
3. The `j` is used as a mathematical tool to represent the 90-degree phase shift between voltage and current in reactive components. It allows us to handle this phase difference using complex number arithmetic. Check [[capacitor and inductance in frequency domain]] 

### admittance 
`Y = I / V = G + jB`

- This equation shows two important things:
    1. It restates the basic definition of admittance (Y = I/V).
    2. It decomposes admittance into its real and imaginary components:
        - `G`: _Conductance_ (the real part). Conductance is related to how easily a circuit conducts current _in phase_ with the voltage. For a purely resistive circuit, G = 1/R. However, G is _not_ simply 1/R if there's also reactance.
        - `B`: _Susceptance_ (the imaginary part). Susceptance is related to how easily a circuit allows current flow that is _out of phase_ with the voltage (due to energy storage in capacitors and inductors).
        - `j`: The imaginary unit, indicating the 90-degree phase shift associated with [[susceptance]].

### the table 
![[Pasted image 20250309155927.png]]

![[Pasted image 20250309160215.png]]

### resonance 
Resonance occurs at a particular resonance frequency, that is when the imaginary parts of impedances or admittances of circuit elements cancel each other.
![[Pasted image 20250316160040.png]]