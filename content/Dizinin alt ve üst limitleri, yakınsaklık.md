---
publish: 1
tags:
  - type/index
entity_extraction_done: true
---

![[Pasted image 20251016170759.png]]
Bu bölüm, bir dizinin yakınsaklığını (convergence) test etmek için kullanılan çok temel bir fikri açıklar. Her dizi düzgün bir şekilde tek bir hedefe gitmez; bazıları farklı değerler etrafında "yığılır". Alt ve üst limitler bu "yığılma" davranışının sınırlarını tanımlar.

#### Tanımlar

1. **Yığılma Noktaları (Limit Points / Accumulation Points):** Bir dizinin içinden seçebileceğimiz farklı yakınsak alt dizilerin (convergent subsequences) limitlerine o dizinin yığılma noktaları denir. Örneğin, $a_n = (-1)^n$ dizisinin iki yığılma noktası vardır: 1 (çift terimler alt dizisinin limiti) ve -1 (tek terimler alt dizisinin limiti).
    
2. **Üst Limit (Limit Superior):** Bir dizinin sahip olduğu tüm yığılma noktaları kümesinin **en büyüğüne** (teknik olarak supremumuna) dizinin üst limiti denir. Bu, dizinin sonsuza giderken "ulaşabildiği en yüksek zirve" olarak düşünülebilir.
    
    - Gösterimler: $\overline{\lim}(a_n)$ veya $\limsup(a_n)$
        
3. **Alt Limit (Limit Inferior):** Bir dizinin sahip olduğu tüm yığılma noktaları kümesinin **en küçüğüne** (teknik olarak infimumuna) dizinin alt limiti denir. Bu da, dizinin "inebildiği en derin çukur" olarak düşünülebilir.
    
    - Gösterimler: $\underline{\lim}(a_n)$ veya $\liminf(a_n)$
        

#### Yakınsaklık Şartı

Görseldeki en önemli sonuç şudur:

> "$(a_n)$ dizisinin yakınsak olması için alt ve üst limitleri eşit olmalıdır."

Matematiksel olarak:

$$\underline{\lim}(a_n) = \overline{\lim}(a_n) = L \iff \lim_{n \to \infty} a_n = L$$

Bu kuralın sezgisel anlamı şudur: Eğer bir dizinin tırmanabildiği en yüksek zirve ile inebildiği en derin çukur aynı noktadaysa, bu dizinin artık salınım yapma veya farklı hedeflere gitme lüksü kalmamıştır. Bütün alt dizileri tek bir hedefe kilitlenmiştir, bu da dizinin kendisinin yakınsak olduğu anlamına gelir.