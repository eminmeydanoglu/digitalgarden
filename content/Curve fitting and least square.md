---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

See also: [[Lagrange Interpolation]], [[polynomials]], [[Linear Algebra]], [[AUV]]

#  Curve Fitting: Least Squares & Linearization

Tarih: 2025-12-12

Ders: Numerical Methods (Week 9)

Konu: Eğri Uydurma, Matris Formülasyonu ve Lineerleştirme

Kaynak: 18 Nisan (Week 9).pdf

---

## 1. Felsefesi: Neden "Least Squares"?

Gerçek dünya verisi gürültülüdür. Elimizdeki veri noktalarından ($x_i, f(x_i)$) tam olarak geçen bir fonksiyon bulmak (Interpolation) her zaman mantıklı değildir; çünkü bu, gürültüyü de modellemek anlamına gelir.

Bunun yerine, verinin **genel eğilimini (trend)** temsil eden en iyi fonksiyonu ($g(x)$) ararız. "En iyi" ne demektir? Hatayı en aza indiren demektir.

Hatayı ($E$) tanımlarken mutlak değer yerine **kareler toplamını** seçeriz. Bunun iki sebebi vardır:

1. Büyük hataları daha çok cezalandırmak.
    
2. Türev alabilmek (Mutlak değerin $x=0$'da türevi yoktur, ama kareli fonksiyon pürüzsüzdür).
    

Amaç fonksiyonumuz1:

$$E = \sum_{i=0}^{m} (f(x_i) - g(x_i))^2$$

Bu toplam hatayı minimize etmek için, katsayılara ($a_0, a_1, \dots$) göre kısmi türev alır ve sıfıra eşitleriz2:

$$\frac{\partial E}{\partial a_k} = 0$$

---

## 2. Matris Mimarisi (The Normal Equations)

Türev işlemlerini yaptığımızda karşımıza lineer bir denklem sistemi çıkar. Bunu matris formunda yazmak, bilgisayarda çözmek için şarttır. Bu matrislere **Normal Denklemler** denir.

### A. Lineer Uydurma (Linear Fit)

Model: $g(x) = a_0 + a_1x$

Bilinmeyen sayısı: 2 ($a_0, a_1$) $\rightarrow$ Matris Boyutu: $2 \times 2$ 3

$$\begin{bmatrix} n & \sum x_i \\ \sum x_i & \sum x_i^2 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \end{bmatrix} = \begin{bmatrix} \sum f(x_i) \\ \sum f(x_i) x_i \end{bmatrix}$$

### B. Kuadratik Uydurma (Quadratic Fit)

Model: $g(x) = a_0 + a_1x + a_2x^2$

Bilinmeyen sayısı: 3 ($a_0, a_1, a_2$) $\rightarrow$ Matris Boyutu: $3 \times 3$ 4

$$\begin{bmatrix} n & \sum x_i & \sum x_i^2 \\ \sum x_i & \sum x_i^2 & \sum x_i^3 \\ \sum x_i^2 & \sum x_i^3 & \sum x_i^4 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} \sum f(x_i) \\ \sum f(x_i) x_i \\ \sum f(x_i) x_i^2 \end{bmatrix}$$

> **Dikkat:** Matris her zaman simetriktir. Köşegen boyunca ($n, \sum x^2, \sum x^4$) terimlerin derecesi artar.

---

## 3. Lineerleştirme (Linearization)

Doğa her zaman $y=mx+c$ şeklinde davranmaz. Üstel büyümeler, doyum eğrileri (saturation) ve güç yasaları yaygındır. Bu non-lineer modelleri çözmek zordur.

Mühendislik hilesi: Modeli değiştiremiyorsan, eksenleri değiştir.

Veriyi dönüştürerek ($Transformation$), eğriyi bir doğruya ($Y = aX + b$) benzetiriz.

### Dönüşüm Tablosu (Slayt 3 Özeti)

|**Orijinal Model**|**Denklem Formu**|**Dönüşüm (Transformation)**|**Yeni Lineer Form (Y=aX+b)**|
|---|---|---|---|
|**Exponential**|$y = a_0 e^{a_1 x}$|$\ln$ al|$\ln y = a_1 x + \ln a_0$ 5|
|**Saturation**|$y = a_0 \frac{x}{a_1+x}$|Ters çevir ($1/y$)|$\frac{1}{y} = \frac{a_1}{a_0}\frac{1}{x} + \frac{1}{a_0}$ 6|
|**Power Law**|$y = a_0 x^{a_1}$|$\ln$ al|$\ln y = a_1 \ln x + \ln a_0$ 7|
|**Inverse**|$y = \frac{a_1}{x} + a_0$|$X = 1/x$|$y = a_1 (\frac{1}{x}) + a_0$ 8|

---

## 4. Uygulama Örneği: Ters Fonksiyon

**Problem:** Verilen veri setine $y = \frac{a_1}{x} + a_0$ modelini uydur. 9

Adım 1: Dönüşümü Tanımla

Bu modelde $y$ zaten lineer duruyor, sorun $x$'in paydada olması.

- Yeni değişken: $X = \frac{1}{x}$
    
- Yeni çıktı: $Y = y$
    
- Denklem: $Y = a_1 X + a_0$ (Burada Eğim $a=a_1$, Kesişim $b=a_0$) 10
    

Adım 2: Matrisi Kur

Artık matriste $\sum x_i$ yerine $\sum X_i$ (yani $\sum \frac{1}{x_i}$) kullanacağız.

$$\begin{bmatrix} n & \sum \frac{1}{x_i} \\ \sum \frac{1}{x_i} & \sum (\frac{1}{x_i})^2 \end{bmatrix} \begin{bmatrix} a_0 \\ a_1 \end{bmatrix} = \begin{bmatrix} \sum y_i \\ \sum y_i (\frac{1}{x_i}) \end{bmatrix}$$

**Adım 3: Hesapla (Slayttaki Verilerle)**

- $\sum \frac{1}{x_i} = 1.95$
    
- $\sum (\frac{1}{x_i})^2 = 1.3525$
    
- Çözüm sonucu: $a_1 \approx 2.1337$, $a_0 \approx 0.9087$ 11
    

Sonuç Fonksiyonu:

$$g(x) = \frac{2.1337}{x} + 0.9087$$

> **Mühendis Notu:** Slaytta sonuç kısmında $a_0$ değeri bir yazım hatasıyla $0.8087$ olarak geçirilmiş olabilir12, ancak matris çözümünden gelen mantıksal değer $0.9087$ civarıdır. Hesaplamalarda her zaman matris çıktısına güven.