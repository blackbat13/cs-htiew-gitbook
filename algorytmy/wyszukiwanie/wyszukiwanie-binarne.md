# Wyszukiwanie binarne

## Opis problemu

W wielu przypadkach, gdy musimy coś znaleźć, np. książkę na półce w bibliotece, to będziemy mieć do czynienia z konkretnym porządkiem.
Książki mogą być ułożone według tematyki, **posortowane** po nazwisku autora i tytule.
Znacząco ułatwia to znalezienie pożądanej pozycji, ponieważ **wiemy, gdzie szukać**.

Tak samo jest też w świecie algorytmiki. Gdy pracujemy na danych **posortowanych**, to zazwyczaj możemy skonstruować efektywne algorytmy do rozwiązania problemu. 

Jak zwykle, zacznijmy od formalnej specyfikacji, by lepiej zrozumieć problem, z którym będziemy się mierzyć.

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ - $$n-elementowa$$ tablica liczb całkowitych, posortowana niemalejąco, indeksowana od jedynki
* $$k$$ - liczba całkowita, szukana wartość

#### Wynik:

* Indeks wartości $$k$$ w tablicy $$A$$, lub $$-1$$ jeżeli tej wartości nie ma w tablicy

### Przykład

#### Dane

```
n := 5
A := [1, 2, 5, 7, 9]
k := 7 
```

**Wynik**: $$4$$ 

## Rozwiązanie iteracyjne

TODO

### Pseudokod

```
funkcja SzukajBinIter(n, A, k)
    1. ind := -1
    2. pocz := 1
    3. kon := n
    4. Dopóki pocz <= kon, wykonuj:
        5. srodek := (pocz + kon) div 2
        6. Jeżeli k = A[srodek], to:
            7. ind := srodek
            8. Wyjdź z pętli
        
        9. Jeżeli k < A[srodek], to:
            10. kon := srodek - 1
        
        11. W przeciwnym przypadku:
            12. pocz := srodek + 1

    13. Zwróć ind, zakończ
```

### Złożoność

$$O(\log n)$$ - logarytmiczna

## Rozwiązanie rekurencyjne

TODO

### Pseudokod

```
funkcja SzukajBinRek(A, k, pocz, kon)
    1. Jeżeli pocz > kon, to:
        2. Zwróć -1, zakończ
    
    3. srodek := (pocz + kon) div 2
    4. Jeżeli k == A[srodek], to:
        5. Zwróć srodek, zakończ
    
    6. Jeżeli k < A[srodek], to:
        7. Zwróć SzukajBinRek(A, k, pocz, srodek-1)
    
    8. W przeciwnym przypadku:
        9. Zwróć SzukajBinRek(A, k, srodek+1, kon)
```

{% hint style="info" %}
**div **oznacza dzielenie całkowite
{% endhint %}

### Złożoność 

$$O(\log n)$$ - logarytmiczna

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/wyszukiwanie/wyszukiwanie-binarne.md" %}
[wyszukiwanie-binarne.md](../../programowanie/c++/algorytmy/wyszukiwanie/wyszukiwanie-binarne.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/wyszukiwanie/wyszukiwanie-binarne.md" %}
[wyszukiwanie-binarne.md](../../programowanie/python/algorytmy/wyszukiwanie/wyszukiwanie-binarne.md)
{% endcontent-ref %}

### Blockly

{% content-ref url="../../programowanie/blockly/algorytmy/wyszukiwanie/wyszukiwanie-binarne.md" %}
[wyszukiwanie-binarne.md](../../programowanie/blockly/algorytmy/wyszukiwanie/wyszukiwanie-binarne.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/searching/binary-search.md" %}
[binary-search.md](../../programowanie/kotlin/algorithms/searching/binary-search.md)
{% endcontent-ref %}