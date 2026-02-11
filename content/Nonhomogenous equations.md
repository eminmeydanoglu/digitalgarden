---
publish: 1
tags:
  - topic/math
---


[[homogenous equations vs nonhomogenous equations]]


### 1. Sistemin Tanımı ve Tutarlılık (Consistency)

> Tahtadan Alıntı:
> 
> "The system in the form $AX=b$ denotes a nonhomogeneous system. For such system the solution may be exist as trivial [unique] or infinitely many solutions... That is, A nonhomogeneous system may be consistent or inconsistent."

Analiz ve Açıklama:

Burada $AX=b$ denklemini görüyoruz.

- **$A$**: Katsayılar matrisi (Matrix of coefficients).
    
- **$X$**: Bilinmeyenler vektörü.
    
- **$b$**: Sabitler vektörü.
    

Eğer $b \neq \mathbf{0}$ ise, bu sisteme **Homojen Olmayan Sistem** diyoruz. Eğer $b = \mathbf{0}$ olsaydı, sistem "Homojen" olurdu ve her zaman en az bir çözümü (trivial solution, $\mathbf{0}$ vektörü) olurdu.

Tahtada "trivial" kelimesi biraz gevşek kullanılmış olabilir. Homojen olmayan bir sistemde $X=0$ (trivial çözüm) asla bir çözüm olamaz (çünkü $A(0) = 0 \neq b$). Burada hoca muhtemelen **"Unique Solution" (Tek Çözüm)** durumunu kastediyor.

Tahta bize 3 temel senaryoyu hatırlatıyor:

1. **Tek Çözüm (Unique):** Doğrular/Düzlemler tek bir noktada kesişir.
    
2. **Sonsuz Çözüm (Infinitely Many):** Doğrular/Düzlemler çakışıktır veya bir doğru boyunca kesişirler (Serbest değişkenler vardır).
    
3. **Çözüm Yok (Inconsistent):** Doğrular/Düzlemler paraleldir, asla kesişmezler.
    

---

### 2. Çözüm Metodu: Augmented Matrix

> Tahtadan Alıntı:
> 
> "To find a basis for the solution set of $AX=b$...
> 
> 1. Write the augmented matrix $[A|b]$. By applyin elementary row operations find the solution set if there exists"
>     

Analiz ve Açıklama:

Mühendislikte bir sistemi çözmenin en "algoritmik" yolu budur. Matrisi genişletiriz: $[A|b]$.

Burada yapılan işlem **Gaussian Elimination** (veya Gauss-Jordan) yöntemidir. Amacımız matrisi **Row Echelon Form (REF)** veya **Reduced Row Echelon Form (RREF)** haline getirmek.

Neden bunu yapıyoruz?

Çünkü "Elementary Row Operations" (Satır işlemleri), denklemlerin çözüm kümesini değiştirmez. Sistemin "genetiğiyle" oynamadan, onu en sade haline (pivotları ve serbest değişkenleri görebileceğimiz hale) getiririz.

- Eğer RREF sonucunda $[0 \ 0 \ \dots \ 0 \ | \ 5]$ gibi bir satır görürsen (yani $0=5$), sistem **Inconsistent** (Tutarsız) demektir. Çözüm yoktur.
    

---

### 3. Çözümün Anatomisi: Genel Çözüm = Özel + Homojen

Bu kısım tahtanın (ve lineer cebirin bu konusunun) kalbidir.

> Tahtadan Alıntı:
> 
> "2) If there exists, we will find the solution in the form
> 
> $$X = \underbrace{[constant \ vector]}_{X_p} + \underbrace{c_1 u_1 + c_2 u_2 + ... + c_k u_k}_{X_h}$$
> 
> $X_p = \text{The particular sol.}$
> 
> $X_h = \text{Homogeneous solution}$"

Derinlemesine Analiz:

Bu formül, lineer sistemlerin "Süperpozisyon İlkesi"nin (Superposition Principle) doğrudan bir sonucudur. Diferansiyel denklemler dersinde de aynısını göreceksin ($y = y_h + y_p$).

Denklemimiz: $AX = b$.

Çözümün yapısı şöyledir:

$$X = X_p + X_h$$

Bunu kanıtlayalım (Feynman tarzı basitlikte):

1. **$X_p$ (Particular Solution):** Sistemin sağ tarafını ($b$) sağlayan herhangi bir "özel" çözümdür. Yani $A X_p = b$.
    
2. **$X_h$ (Homogeneous Solution):** Sistemin sağ tarafını sıfırlayan ($0$) çözümler kümesidir (Null Space / Kernel). Yani $A X_h = 0$.
    

Şimdi bu ikisini toplayıp $A$ matrisine sokalım:

$$A(X_p + X_h) = A X_p + A X_h$$

Lineerlik gereği dağıttık. Bildiklerimizi yerine yazalım:

$$= b + 0$$

$$= b$$

Gördüğün gibi, $X_p$'nin üzerine ne kadar $X_h$ eklersen ekle, sonuç hala $b$ çıkar. Çünkü $X_h$, matrisin "yutan elemanıdır", $b$'ye etki etmez, sadece $X$ uzayında "gezmeni" sağlar.

**Geometrik Olarak Ne Oluyor?**

- **$X_h$:** Orijinden geçen bir alt uzaydır (bir doğru veya düzlem).
    
- **$X_p$:** Bu alt uzayı orijinden alıp, uzayda başka bir yere "öteleyen" (shift) vektördür.
    

Yani homojen olmayan bir sistemin çözüm kümesi, **orijinden geçmeyen bir düzlem** (affine subspace) belirtir.

Bkz: [[Matematik]] • [[Engineering]] • [[Feynman]]