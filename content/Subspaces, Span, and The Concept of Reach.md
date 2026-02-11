---
publish: 1
---

See also: [[Linear Algebra]], [[basis vectors]], [[column space, null space, solution space]], [[AUV]]

**Tags:**  #MathEngineering #AUV #ControlTheory 
**Date:** 2025-12-04

## 1. Alt Uzay (Subspace) Nedir?

Bir vektör uzayı $V$'nin içinde yer alan, ancak kendi başına da bir vektör uzayı özellikleri taşıyan alt kümeye **Alt Uzay ($W$)** denir.

Matematiksel olarak $W \subseteq V$ ifadesinin bir alt uzay belirtmesi için, kümenin "kendi içine kapalı" olması gerekir. Yani, o küme içinde yapılan işlemlerin sonucu, sizi kümenin dışına fırlatmamalıdır.

### Alt Uzay Testi (The Two-Step Test)
Bir $W$ kümesinin alt uzay olup olmadığını anlamak için şu iki soruya "Evet" cevabı vermemiz zorunludur:

1.  **Toplamaya Göre Kapalılık (Closure under Addition):**
    $W$ içindeki herhangi iki vektörün toplamı yine $W$ içinde kalıyor mu?
    $$\forall \vec{u}, \vec{v} \in W \implies \vec{u} + \vec{v} \in W$$

2.  **Skalerle Çarpmaya Göre Kapalılık (Closure under Scalar Multiplication):**
    $W$ içindeki bir vektörün, herhangi bir reel sayı ile çarpımı yine $W$ içinde kalıyor mu?
    $$c \in \mathbb{R}, \vec{u} \in W \implies c \vec{u} \in W$$

> [!NOTE] Kritik Geometrik Kural
> Bir kümenin alt uzay olabilmesi için **mutlaka orijini ($\vec{0}$) içermesi gerekir**. Çünkü skaler çarpımda $c=0$ seçilirse sonuç $\vec{0}$ olur. Orijinden geçmeyen hiçbir doğru veya düzlem alt uzay olamaz.

---

## 2. Germe (Span) Kavramı

**Span**, eldeki malzemelerle inşa edilebilecek yapının sınırlarını tanımlar. Bir $S = \{\vec{v}_1, \vec{v}_2, \dots, \vec{v}_n\}$ vektör kümesi verildiğinde, bu vektörlerin tüm olası **lineer kombinasyonlarına** o kümenin "Germesi" (Span) denir.

$$
\operatorname{Span}(S)
= \{\, c_1 \vec{v}_1 + \dots + c_n \vec{v}_n \mid c_i \in \mathbb{R} \,\}
$$

### Temel Teorem: Span Bir Alt Uzaydır
Herhangi bir vektör kümesinin Span'ı, ana uzayın içinde geçerli bir alt uzaydır. Bu, rastgele vektörlerin kombinasyonlarının kaotik bir yapı değil, matematiksel olarak düzenli (lineer) bir yapı (bir doğru, bir düzlem vb.) oluşturduğunu garanti eder.

---

## 3. Büyük Eşitlik: $Span(S) = V$

Mühendislikteki en kritik durum budur. Eğer elinizdeki $S$ kümesinin gerdiği alt uzay, ana uzayın ($V$) ta kendisine eşitse, şu ifadeyi kullanırız: **"$S$ kümesi, $V$ uzayını gerer (spans V)."**

Bu durum matematiksel olarak şöyledir:
$$\forall \vec{w} \in V, \exists c_1, \dots, c_n \in \mathbb{R} \text{ such that } \vec{w} = c_1\vec{v}_1 + \dots + c_n\vec{v}_n$$

Yani uzaydaki **her nokta**, elinizdeki vektörlerle erişilebilirdir. Hiçbir kör nokta yoktur.

---

## 4. Mühendislik ve Felsefe Bağlamı

### 🤖 AUV & Robotik: "Eyleyici Yeterliliği"
Bu konsept robotikte **Holonomik Sistemler** ile ilgilidir.
* **$Span(S) \subset V$ (Alt Küme):** Aracın motorları (vektörleri) uzayın tamamını geremiyor. Örneğin, standart bir araba yan yan gidemez. Sadece ileri-geri ve dönüş uzayını gerer. Bu sisteme "Underactuated" (Eksik Eyleyicili) denir.
* **$Span(S) = V$ (Eşitlik):** Aracın iticileri, $\mathbb{R}^3$ veya $\mathbb{R}^6$ uzayındaki her noktaya kuvvet uygulayabilir. Bu sistem "Fully Actuated" (Tam Eyleyicili) bir sistemdir. AUV tasarımında hedefimiz genellikle budur; akıntıya karşı her yönden direnç gösterebilmek isteriz.

### 🧠 Felsefi Bakış: "Potansiyel vs. Aktüel"
* **Vektörler ($S$):** Sahip olduğumuz yetenekler veya araçlar.
* **Span ($W$):** Bu yeteneklerle ulaşabileceğimiz potansiyel varoluş sahası.
* Bir insanın kendi hayatını ($V$) tamamen kontrol edebilmesi ($Span S = V$), sahip olduğu içsel araçların (erdem, irade, akıl) hayatın getireceği her duruma (vektöre) karşılık verebilecek bir kombinasyon üretebilmesi demektir. Stoacılıkta bu, dışsal olaylar ne olursa olsun (uzaydaki hangi vektör gelirse gelsin), içsel "Ruling Faculty" (Yönetici İlke) ile onu karşılayabilme kapasitesidir.

Bkz: [[Matematik]] • [[Stoa]] • [[Engineering]]