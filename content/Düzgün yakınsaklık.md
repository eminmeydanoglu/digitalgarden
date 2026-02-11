---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---
[[Düzgün yakınsaklık neden noktasal yakınsaklığı kapsar]]

[[Düzgün Yakınsama için Supremum Testi (T_n Testi)]]

![[Pasted image 20251023171003.png]]- **Noktasal Yakınsaklıkta:** "Her $x$ noktasını _tek tek_ ele aldığımızda, ona uygun bir $N$ bulabiliriz." demiştik. $N$ hem $\epsilon$'a hem de $x$'e bağlıydı: $N(\epsilon, x)$. $x=0.5$ için $N=100$ gerekebilirken, $x=0.9$ için $N=1,000,000$ gerekebilirdi.
    
- **Düzgün Yakınsaklıkta:** "Her $\epsilon > 0$ için, _bütün $x$'ler için aynı anda çalışan_ bir tane $N$ bulabiliriz." der. $N$ artık $x$'e bağlı olamaz; sadece $\epsilon$'a bağlıdır: $N(\epsilon)$.
    

Bunu bir oyun gibi düşünün:

- **Noktasal:** Ben bir $x$ noktası ve bir $\epsilon$ hata payı seçerim, siz de bir $N$ (eşik değer) bulursunuz.
    
- **Düzgün:** Ben _sadece_ bir $\epsilon$ hata payı seçerim (örneğin $\epsilon = 0.1$). Sizin bulduğunuz _tek bir $N$ (örneğin $N=1000$)_, $n > 1000$ olduğunda $f_n(x)$'in $f(x)$'e $0.1$'den daha yakın olmasını _aralıktaki tüm $x$'ler için aynı anda_ garantilemelidir.
    

Slayttaki İngilizce (Folland) tanım da bu "can alıcı noktayı" vurguluyor:

> Alıntı (Slayt): "The crucial point in this definition is that N depends only on $\epsilon$ and not on $x \in A$, whereas for a pointwise convergent sequence N may depend on both $\epsilon$ and x." 3
> 
> (Çevirisi: Bu tanımdaki can alıcı nokta, N'nin sadece $\epsilon$'a bağlı olup $x \in A$'ya bağlı olmamasıdır, oysa noktasal yakınsak bir dizide N hem $\epsilon$'a hem de $x$'e bağlı olabilir.)

**Özetle:** Düzgün yakınsaklık, dizideki fonksiyonların limit fonksiyonuna "hep birlikte", "aynı hızda" yakınsamasını talep eder. Noktasal yakınsaklık ise bazı $x$'lerin çok hızlı, bazılarının (Örnek 2'de $x \to 1$ durumu gibi) _keyfi olarak yavaş_ yakınsamasına izin veriyordu4. İşte bu "aynı hızda yakınsama" şartı, limit ve integral/türev işlemlerinin yer değiştirebilmesi için aradığımız anahtar olacak.



