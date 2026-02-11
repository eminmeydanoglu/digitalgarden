---
publish: 1
tags:
  - topic/math
---
**Source:** MAT116E Lecture 3 1

---

## 1. Temel İndeksleme Mantığı (The Golden Rules)

MATLAB'de (C veya Python'un aksine) indeksleme **1'den başlar**. Bu, matematiksel matris notasyonuna ($A_{ij}$) sadık kalmak içindir.

> [!WARNING] Dikkat
> 
> İndeksler pozitif tamsayı (positive integer) olmak zorundadır. $A(0)$ veya $A(-2)$ kullanımı hata döndürür

### Erişim Sözdizimi

Bir matrisin elemanına erişmek için:

MatrixName(Row, Column)

Örnek $A$ matrisi için:

$$A = \begin{bmatrix} 1 & 2 & 5 \\ 3 & 4 & 6 \end{bmatrix}$$

- `A(2, 3)` $\rightarrow$ 2. Satır, 3. Sütun $\rightarrow$ Değer: **6**.
    
- `A(4, 2)` $\rightarrow$ **Hata:** "Index exceeds matrix dimensions."4.
    

---

## 2. Dilimleme (Slicing) ve Kolon Operatörü (:)

Matrislerin belirli bloklarını, satırlarını veya sütunlarını çekip almak için `:` (colon) operatörü "joker" (wildcard) görevi görür.

### Tüm Satır veya Sütunu Seçmek

- **Tüm Sütun:** `A(:, n)` $\rightarrow$ $n$. sütundaki tüm satırlar.
    
- **Tüm Satır:** `A(m, :)` $\rightarrow$ $m$. satırdaki tüm sütunlar.
    

### Aralık Belirterek Seçmek (Range)

Bitişik (consecutive) elemanları seçmek için `start:end` yapısı kullanılır.

- `A(1:2, :)` $\rightarrow$ 1. ve 2. satırların tamamını getir.
    
- `A(:, 2:3)` $\rightarrow$ 2. ve 3. sütunların tamamını getir8.
    

### Bitişik Olmayan Seçim (Discontinuous)

Belli, dağınık satır veya sütunları seçmek için indeksleri bir **vektör** olarak veririz `[]`.

- `A([1, 3], :)` $\rightarrow$ Sadece 1. ve 3. satırları getir (2. satırı atla)
    

---

## 3. Değer Değiştirme ve Atama (Assignment)

Bir matrisin elemanlarını tek tek veya toplu olarak değiştirebiliriz.

- **Tek Eleman:** `Results(3,4) = 10`.
    
- **Toplu Sıfırlama:** `Results(:, 3) = 0` (3. sütundaki tüm değerleri 0 yap)
    
- **Blok Değiştirme:** `Results([3,6], :) = 0` (3. ve 6. satırların tamamını 0 yap).
    
- **Hesaplamalı Atama:** `Results(:, 5) = Results(:, 3) + Results(:, 4)` (İki sütunu toplayıp 5. sütuna yaz)13.
    

> [!TIP] AUV İpucu: ROI (Region of Interest)
> 
> Görüntü işlerken kameradan gelen kare bir matristir. Sadece merkeze odaklanmak istiyorsan slicing kullanırsın:
> 
> CenterImage = CameraFrame(200:400, 300:500);
> 
> Bu işlem, tüm resim üzerinde işlem yapmaktan çok daha hızlıdır.

---

## 4. Researcher Note: Linear Indexing & Memory Layout

Slaytta `A(6)` gibi tek parametreli bir kullanım görüyoruz14. Buna **Linear Indexing** denir.

Nasıl Çalışır?

MATLAB matrisleri bellekte Column-Major Order (Sütun Öncelikli) olarak tutar. Yani yukarıdan aşağıya sütunları doldura doldura ilerler.

$$A = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

Bellekteki dizilim: `[1, 2, 3, 4, 5, 6]`

Bu yüzden $3 \times 2$'lik bir matriste:

- `A(1, 2)` (1. satır, 2. sütun) = **4**
    
- `A(4)` (Bellekteki 4. eleman) = **4** (Aynı kapıya çıkar).
    

> Neden Önemli?
> 
> Büyük verilerle çalışırken (Big Data/Robotics), iç içe döngülerde dış döngünün sütunları (j), iç döngünün satırları (i) gezmesi ("cache locality" açısından) kodunu hızlandırır. Python/C++'ta ise tam tersidir (Row-Major).

Bkz: [[Matematik]] • [[Engineering]]