---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

Bu örnek, noktasal yakınsaklığın en meşhur ve en öğretici örneğidir.

> **Alıntı (Slayt):** "Örnek 2: $f_n: [0, 1] \to \mathbb{R}$ olmak üzere, her $n \in \mathbb{N}$ için $f_n(x) = x^n$ olsun."

Açıklama:

Burada bir fonksiyon dizisi tanımlanıyor. Bu, sonsuz tane fonksiyondan oluşan bir listedir:

- $f_1(x) = x$ (düz bir çizgi)
    
- $f_2(x) = x^2$ (bir parabol)
    
- $f_3(x) = x^3$ (bir kübik eğri)
    
- ...
    
- $f_{100}(x) = x^{100}$ (çok daha "sert" bir eğri)
    

Hepsi $[0, 1]$ aralığında tanımlı. Amacımız, $n$ sonsuza giderken bu $f_n$ fonksiyonlarının "limitinin" ne olduğunu bulmak.

> **Alıntı (Slayt):** "$\forall x \in [0, 1]$ için, $\lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} x^n = \begin{cases} 0 & ; 0 \le x < 1 \\ 1 & ; x = 1 \end{cases} = f(x)$."

Açıklama:

Bu, noktasal yakınsaklık (pointwise convergence) işleminin ta kendisidir. $[0, 1]$ aralığından herhangi bir $x$ noktasını sabitliyoruz ve $f_n(x)$'in (ki bu artık bir sayı dizisidir) limitine bakıyoruz.

Bunu neden iki parça olarak incelediğimizi görelim:

1. Durum 1: $0 \le x < 1$ ise
    
    Aralıktan $1$'den küçük bir $x$ seçelim, örneğin $x = 0.5$.
    
    Şimdi $f_n(0.5) = (0.5)^n$ dizisine bakıyoruz. Bu dizi şöyledir:
    
    $0.5, 0.25, 0.125, 0.0625, \dots$
    
    Bu sayı dizisinin limiti açıkça $0$'dır. Aynı şey $x=0.9$ ( $0.9, 0.81, 0.729, \dots \to 0$ ) veya $x=0$ ( $0, 0, 0, \dots \to 0$ ) için de geçerlidir. $1$'den küçük herhangi bir sayının üssünü aldıkça sonuç $0$'a yaklaşır.
    
2. Durum 2: $x = 1$ ise
    
    Şimdi tam olarak $x=1$ noktasını seçelim.
    
    $f_n(1) = (1)^n$ dizisine bakıyoruz. Bu dizi şöyledir:
    
    $1, 1, 1, 1, \dots$
    
    Bu sabit dizinin limiti $1$'dir.
    

Dış Bilgi (Bağlantı):

Bu iki durumu birleştirdiğimizde, limitin kendisinin de bir fonksiyon olduğunu görüyoruz. Slayt buna $f(x)$ adını vermiş. Bu $f(x)$ fonksiyonu, $0$'dan $1$'e kadar ( $1$ hariç) $y=0$ çizgisi üzerinde ilerler, ancak tam $x=1$ noktasında aniden $y=1$ değerine "zıplar".

> **Alıntı (Slayt):** "Uyarı 1: Sürekli fonksiyon dizilerinin noktasal limit fonksiyonu süreksiz olabilmektedir." (ve el yazısı: "$x=1$'de sürekli değil!")

Açıklama:

Bu, bu örneğin ana fikridir.

- Dizimizdeki her bir fonksiyon ($f_1(x)=x, f_2(x)=x^2, \dots$) birer polinomdur.
    
- Polinomlar her yerde süreklidir.
    
- Yani, **sürekli** fonksiyonlardan oluşan bir dizimiz var.
    
- Ancak, bu dizinin "noktasal limiti" olan $f(x)$ fonksiyonu, $x=1$'de bir sıçrama yaptığından **süreksizdir**.
    

Bu, noktasal yakınsaklığın "zayıf" bir yakınsaklık türü olduğunu gösterir. Fonksiyonların sahip olduğu güzel bir özelliği (süreklilik) koruyamayabilir.

> **Alıntı (Slayt):** "Demek ki burada $N = N(\epsilon, x)$ olur." (ve $\epsilon-N$ hesabı)

Açıklama:

Bu kısım, neden düzgün yakınsaklığa (uniform convergence) ihtiyaç duyacağımızı matematiksel olarak gösterir.

Noktasal yakınsaklık tanımı der ki: Her $\epsilon > 0$ ve her bir $x$ için, bir $N$ bulabilirsin ki...

Slayttaki hesap ($n > \frac{\ln \epsilon}{\ln x}$) bize bu $N$'nin formülünü veriyor.

Bu formüle dikkat edin: $N$, sadece $\epsilon$'a değil, aynı zamanda $x$'e de bağlıdır.

Dış Bilgi (İleriye Bakış):

Bu $N(\epsilon, x) = \frac{\ln \epsilon}{\ln x}$ formülünde $x \to 1^-$ ( $x$, $1$'e soldan yaklaşır) iken ne olduğuna bakalım:

- $\ln \epsilon$ negatiftir (çünkü $\epsilon < 1$).
    
- $\ln x$ de negatiftir ve $0$'a yaklaşır.
    
- (Negatif) / (Sıfıra yaklaşan negatif) $\to +\infty$
    
    Anlamı şudur: $x$'i $1$'e ne kadar yakın seçersek, aynı $\epsilon$ hatasına ulaşmak için o kadar büyük bir $N$ (yani dizide o kadar ileri gitmemiz) gerekir. Asla tüm $x$'ler için ortak bir $N$ bulamayız. Bu yüzden bu dizi "düzgün yakınsak" değildir.



Önceki örneklerde (Örnek 2, 6, 7) noktasal yakınsaklığın bir sürü soruna yol açtığını gördük:

- Sürekli fonksiyonların limiti süreksiz olabildi ( $x^n$ örneği).
    
- Sınırlı fonksiyonların limiti sınırsız olabildi ( $\frac{n}{nx+1}$ örneği).
    
- Limit ve türev işlemleri birbiriyle yer değiştirmedi ( $\frac{\sin nx}{n}$ örneği).
    

Bu sonuncusu, analizin (Kalkülüs) temel taşları için büyük bir problemdir.

> **Alıntı (Slayt):** "Aşağıdaki eşitlikler ne zaman gerçeklenir?"
> 
> - $(\lim_{n \to \infty} f_n(x))' \stackrel{?}{=} \lim_{n \to \infty} (f_n(x))'$
>     
> - $\lim_{n \to \infty} \int_{a}^{b} f_n(x) dx \stackrel{?}{=} \int_{a}^{b} \lim_{n \to \infty} (f_n(x)) dx$
>     

Açıklama:

Bu slayt, tüm konunun motivasyonunu özetliyor. Bize iki temel soru soruyor:

1. **Limit ve Türev:** "Bir fonksiyon dizisinin limitinin türevini" almakla, "türev dizisinin limitini" almak aynı şey midir? (Örnek 7'de olmadığını gördük).
    
2. **Limit ve İntegral:** "Bir fonksiyon dizisinin limitinin integralini" almakla, "integral dizisinin limitini" almak aynı şey midir?
    

Kalkülüs'te bu işlemleri (türev ve integral) sürekli kullanırız. Eğer limit işlemi bu temel işlemleri bozuyorsa, o zaman "noktasal limit" kavramı analiz yapmak için yeterince güçlü veya güvenilir değildir.

> **Alıntı (Slayt):** "Bu soruların yanıtlarını arayacağız $\implies$ [[Düzgün yakınsaklık]] (Uniform Convergence)" 1

Açıklama:

Slayt, bu soruların cevabının "Düzgün Yakınsaklık" olduğunu söylüyor. Bu, noktasal yakınsaklıktan daha güçlü, daha "sağlam" yeni bir yakınsaklık türüdür ve bu tür "patolojileri" (sorunları) engelleyen türdür.

Bkz: [[Matematik]]