---
publish: 1
tags:
  - topic/math
  - topic/linear-algebra
related:
  - "[[Lineer Cebir]]"
  - "[[Vektör Uzayları]]"
  - "[[Teoremler]]"
---

# Alt Uzay Teoremi ve Kanıtı

> [[Lineer Cebir]] notları: Alt uzay tanımı, Subspace Test teoremi ve kanıtı.
> İlgili: [[Vector space axioms cheat sheet]], [[Polinomlar]], [[Kapalılık]]

---

## 1. Alt Uzay (Subspace) Tanımı
Bir $V$ vektör uzayının boş olmayan bir $W$ alt kümesi, eğer $V$'deki tanımlı işlemlerle (toplama ve skaler çarpma) kendi başına bir vektör uzayı oluşturuyorsa, $W$'ya $V$'nin bir **Alt Uzayı (Subspace)** denir.

Matematiksel gösterim: $W \subseteq V$.

---

## 2. Teorem 4.2 (Subspace Test)
Bir alt kümenin alt uzay olup olmadığını anlamak için 10 vektör uzayı aksiyomunu tek tek kontrol etmeye gerek yoktur. Aşağıdaki iki "Kapalılık" (Closure) şartının sağlanması yeterlidir.

**Teorem:** Boş olmayan bir $W \subseteq V$ kümesi, $V$'nin bir alt uzayıdır ancak ve ancak şu iki şart sağlanırsa:

1.  **Closure under Addition (Toplamaya Göre Kapalılık):**
    Her $u, v \in W$ için, $u + v \in W$ olmalıdır.

2.  **Closure under Scalar Multiplication (Skaler Çarpmaya Göre Kapalılık):**
    Her $c \in \mathbb{R}$ ve $u \in W$ için, $c \cdot u \in W$ olmalıdır.

### Kanıt (Proof)

**Yön 1 ($\Rightarrow$):**
Eğer $W$ zaten bir alt uzay ise, tanım gereği bir vektör uzayıdır. Dolayısıyla bir vektör uzayının sağlaması gereken tüm kapalılık özelliklerini (1 ve 2) zaten sağlar.

**Yön 2 ($\Leftarrow$):**
Diyelim ki $W$ kümesi 1 ve 2 numaralı kapalılık şartlarını sağlıyor. $W$ bir vektör uzayı mıdır?
* **Miras Kalan Özellikler (Inheritance):** $W$ kümesi $V$'nin içinde olduğu için ($W \subseteq V$), vektörlerin genel davranış kuralları (Değişme, Birleşme, Dağılma özellikleri) $V$'den miras alınır. Örneğin, $V$'deki elemanlar için $u+v=v+u$ geçerli olduğu için, bu $W$'daki elemanlar için de otomatik olarak geçerlidir.
* **Varlık Şartları (Existence):** Bir vektör uzayı için kritik olan **Sıfır Vektörü ($\mathbf{0}$)** ve **Ters Eleman ($-u$)** kümede var mıdır?
    * 2 numaralı özellikten (Skaler Kapalılık) faydalanırız.
    * Herhangi bir $u \in W$ için $c=0$ seçilirse: $0 \cdot u = \mathbf{0}$. Kapalılık gereği $\mathbf{0} \in W$ olur.
    * Herhangi bir $u \in W$ için $c=-1$ seçilirse: $(-1) \cdot u = -u$. Kapalılık gereği $-u \in W$ olur.

Tüm şartlar sağlandığına göre, $W$ bir alt uzayıdır.

---

## 3. Örnek: Derecesi Tam Olan Polinomlar Tuzağı

**Soru:** $V$, derecesi **tam olarak 2** olan polinomlar kümesi olsun.
$$V = \{ a t^2 + bt + c \mid a, b, c \in \mathbb{R}, a \neq 0 \}$$
Bu küme, tüm polinomlar uzayı $P$'nin bir alt uzayı mıdır?

**Çözüm:**
Alt uzay değildir. Bunu göstermek için "Toplamaya Göre Kapalılık" kuralının ihlal edildiğini (Counter-Example) bulmak yeterlidir.

1.  $W$'dan iki polinom seçelim:
    $$p_1(t) = 1t^2 + t + 1 \quad (\text{Burada } a=1 \neq 0, \text{kümede var})$$
    $$p_2(t) = -1t^2 + t + 1 \quad (\text{Burada } a=-1 \neq 0, \text{kümede var})$$

2.  Bu iki polinomu toplayalım:
    $$(p_1 + p_2)(t) = (1 + (-1))t^2 + (1+1)t + (1+1)$$
    $$(p_1 + p_2)(t) = 0t^2 + 2t + 2 = 2t + 2$$

3.  **Sonuç:** Elde edilen $2t+2$ polinomunun derecesi 1'dir. Ancak kümemiz sadece derecesi **2** olanları kabul ediyordu. Sonuç küme dışına çıktığı için $V$ kapalı değildir ve **alt uzay olamaz.**

> **Pratik Not:** Ayrıca, $a \neq 0$ şartı olduğu için **Sıfır Polinomu** ($0t^2+0t+0$) bu kümede yoktur. Sıfır vektörü olmayan hiçbir küme, vektör uzayı (veya alt uzay) olamaz.

Bkz: [[Matematik]] • [[Engineering]]