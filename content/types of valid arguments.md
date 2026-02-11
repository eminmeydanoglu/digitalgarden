---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

See also: [[direct proof]], [[Inference Rules for Quantifiers]], [[derivable arguments and inconsistent premises]]

These images present a list of fundamental, valid argument forms, which are also known as **inference rules**. These are the basic building blocks for constructing logical proofs. Each one is a "valid argument," meaning the implication from its premises to its conclusion is a tautology.

---

### Image 2 (`image_d66aa3.jpg`)

This image starts the list, labeled as a "Theorem" about "Inference Rules / Logical Implications."

> **"The following are valid arguments:"**

#### (1) Modus Ponens

$$\begin{array}{l} A \to B \\ A \\ \hline B \end{array}$$

This is the rule you proved in the previous lesson. It's Latin for "the way that affirms."

- **Premise 1:** $A \to B$ ("If $A$ is true, then $B$ is true.")
    
- **Premise 2:** $A$ ("$A$ is true.")
    
- Conclusion: $B$ ("Therefore, $B$ is true.")
    
    This rule allows you to "detach" the conclusion $B$ once you have affirmed the hypothesis $A$.
    

#### (2) Modus Tollens

$$\begin{array}{l} A \to B \\ \neg B \\ \hline \neg A \end{array}$$

This is Latin for "the way that denies." It's the contrapositive form of _Modus Ponens_.

- **Premise 1:** $A \to B$ ("If $A$ is true, then $B$ is true.")
    
- **Premise 2:** $\neg B$ ("$B$ is false.")
    
- Conclusion: $\neg A$ ("Therefore, $A$ must be false.")
    
    The logic is: If $A$ were true, then $B$ would have to be true (by Modus Ponens). But $B$ is false, so our assumption that $A$ was true must be wrong.
    

---

### Image 3 (`image_d66abd.jpg`)

This image continues the list of rules.

#### (3) Modus Tollendo Ponens (Disjunctive Syllogism)

$$\begin{array}{l} A \lor B \\ \neg B \\ \hline A \end{array} \qquad \qquad \begin{array}{l} A \lor B \\ \neg A \\ \hline B \end{array}$$

The name means "the way that affirms by denying." This is a "process of elimination" argument.

- **Premise 1:** $A \lor B$ ("Either $A$ is true, or $B$ is true.")
    
- **Premise 2:** $\neg B$ ("$B$ is false.")
    
- Conclusion: $A$ ("Therefore, $A$ must be true.")
    
    Since the $\lor$ (OR) statement must be true, and one of its components ($B$) is false, the other component ($A$) must be the one making it true.
    

#### (4) Hypothetical Syllogism

$$\begin{array}{l} A \to B \\ B \to C \\ \hline A \to C \end{array}$$

This is the **transitive property** of logical implication. It allows you to chain implications together.

- **Premise 1:** $A \to B$ ("If $A$, then $B$.")
    
- **Premise 2:** $B \to C$ ("If $B$, then $C$.")
    
- Conclusion: $A \to C$ ("Therefore, if $A$, then $C$.")
    
    If $A$ starts the chain, it leads to $B$, which in turn leads to $C$, so $A$ leads to $C$.
    

---

### Image 1 (`image_d66ac1.jpg`)

This image shows the last three rules in the list.

#### (5) Constructive Dilemma

$$\begin{array}{l} A \to M \\ B \to N \\ A \lor B \\ \hline M \lor N \end{array}$$

This rule is a bit more complex. It says that if you have two implications and you know that at least one of their hypotheses is true, then at least one of their conclusions must be true.

- **Premise 1:** $A \to M$ ("If $A$, then $M$.")
    
- **Premise 2:** $B \to N$ ("If $B$, then $N$.")
    
- **Premise 3:** $A \lor B$ ("Either $A$ is true or $B$ is true.")
    
- Conclusion: $M \lor N$ ("Therefore, either $M$ is true or $N$ is true.")
    
    The logic is: The $A \lor B$ premise forces one of two possibilities. If $A$ is the true one, then $M$ must be true. If $B$ is the true one, then $N$ must be true. Since one of those must happen, the conclusion $M \lor N$ is guaranteed.
    

#### (6) Double Negation

$$\begin{array}{l} \neg\neg A \\ \hline A \end{array}$$

This rule is simple: "not not-A" is logically equivalent to $A$.

- **Premise:** $\neg\neg A$ ("It is not the case that $A$ is false.")
    
- **Conclusion:** $A$ ("Therefore, $A$ is true.")
    

#### (7) Repetition

$$\begin{array}{l} A \\ \hline A \end{array}$$

This is the most basic rule of all.

- **Premise:** $A$ ("$A$ is true.")
    
- Conclusion: $A$ ("Therefore, $A$ is true.")
    
    While it looks trivial, this rule is important in formal proof systems (like "natural deduction") where it allows you to restate a premise or a previously derived line to use it in a subsequent step.



** (8) Simplification **

A∧BA​​A∧BB​​

- **Explanation:** This rule states that if a conjunction (A and B) is true, then both of its individual components (called "conjuncts") must be true. This rule allows you to "extract" either part of a true "AND" statement. For the statement "It is raining and it is cold" to be true, "It is raining" must be true, and "It is cold" must be true.
    

** (9) Adjunction (also called Conjunction) **

ABA∧B​​

- **Explanation:** This is the reverse of Simplification. If you have successfully established, on two separate lines of a proof, that A is true and B is true, you are allowed to "join" them together with an "AND" connective.
    

** (10) Addition **

AA∨B​​BA∨B​​

- **Explanation:** This rule states that if a statement A is true, then any disjunction (A or B) that contains A is also true. This makes intuitive sense: if you know "It is raining" is true, then the statement "It is raining or the sky is green" is _also_ true, regardless of the truth value of the second part. This rule is often used to introduce a new statement (B) into the proof.
    

#### Image 3 (`image_d676e1.jpg`)

This image adds the final two rules, which govern the biconditional (↔).

** (11) Biconditional-Conditional **

A↔BA→B​​A↔BB→A​​

- **Explanation:** The statement A↔B ("A if and only if B") is logically equivalent to (A→B)∧(B→A). This rule is just **Simplification (Rule 8)** applied to that definition. If the biconditional is true, then the conjunction of both "if-then" directions is true, so each individual "if-then" direction must also be true.
    

** (12) Conditional-Biconditional **

A→BB→AA↔B​​

- **Explanation:** This is the reverse of Rule (11) and is an application of **Adjunction (Rule 9)**. If you have proven both the "forward" direction (A→B) and the "backward" direction (B→A), you can join them to form the "if and only if" statement.
    

---

### Proof of Constructive Dilemma (Rule 5)

The notes then circle back to provide a formal proof for **Rule (5) Constructive Dilemma**, which was:

- **Premises:** A→M, B→N, A∨B
    
- **Conclusion:** M∨N
    

The proof is laid out on `image_d676e1.jpg` and `image_d67985.jpg`.

> **"Proof: (5) We assume that each premise is true. In particular A∨B is true. So A is true, or B is true"**

This begins the proof. We assume all premises are true and focus on A∨B. This premise forces a **Proof by Cases**, a very common and powerful technique. Since A∨B is true, we know we must be in one of two possible "worlds": the world where A is true, or the world where B is true. We just have to show that our conclusion (M∨N) holds in _both_ cases.

**Case 1: Assume A is true.**

> **"If A is true, then M is true because the premise A→M is true."**

- This step uses the premise A→M and our assumption A.
    
- By **Modus Ponens (Rule 1)** on A and A→M, we validly conclude M.
    

**Case 2: Assume B is true.**

> **"If B is true, then N is true because the premise B→N is true."**

- This step uses the premise B→N and our assumption B.
    
- By **Modus Ponens (Rule 1)** on B and B→N, we validly conclude N.
    

**Conclusion of the Proof:**

> **"So M or N is true. That is the conclusion M∨N is true. □"**

- We have shown that if we are in Case 1, M becomes true. If we are in Case 2, N becomes true.
    
- Since we _must_ be in either Case 1 or Case 2 (because A∨B is true), it is guaranteed that either M will be true or N will be true.
    
- Therefore, the disjunction M∨N must be true. The proof is complete.
    

---

### Remark and New Example

Finally, `image_d67985.jpg` introduces a new meta-logical definition and a new problem.

> **"Rmk: A⟺B iff A⟹B and B⟹A** **Proof: Exercise. □"**

This remark defines **Logical Equivalence** (⟺).

- A⟺B ("A is logically equivalent to B") is a _meta-logical assertion_ that the statement A↔B is a **tautology**.
    
- The remark states this is true _if and only if_ A⟹B ( A→B is a tautology) AND B⟹A (B→A is a tautology).
    
- This formally connects the idea of "equivalence" to "implication in both directions."
    

> **"Ex: Establish the validity of the given arguments:** **(1)**
> 
> $$\begin{array}{l} P \\ P \to Q \\ S \lor R \\ R \to \neg Q \\ \hline S \lor T \end{array} $$"$$

This is a new problem. Your task is to use the 12 inference rules to build a step-by-step derivation that starts from the four premises (P, P→Q, S∨R, R→¬Q) and ends with the conclusion S∨T.