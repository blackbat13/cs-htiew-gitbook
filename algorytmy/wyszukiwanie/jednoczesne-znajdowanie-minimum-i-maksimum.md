# Jednoczesne wyszukiwanie minimum i maksimum

## Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, liczba elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik:

* Największa oraz najmniejsza wartość z tablicy $$A$$

### Przykład

#### Dane

```
n := 5
A := [6, 3, 1, 9, 2]
```

#### Wynik

```
minimum := 1
maksimum := 9
```

## Rozwiązanie naiwne

TODO

### Pseudokod

```
funckja SzukajMinMax(n, A):
    1. min := A[1]
    2. max := A[1]
    3. Od i := 2 do n, wykonuj:
        4. Jeżeli min < A[i], to:
            5. min := A[i]
        6. Jeżeli max > A[i], to:
            7. max := A[i]
    8. Zwróć min, max
```

### Złożoność

$$O(2n)$$ 

## Rozwiązanie optymalne

TODO

{% hint style="warning" %}
**Uwaga**

Dla ułatwienia zakładamy, że długość tablicy (wartość $$n$$) jest liczbą **parzystą**. Jeżeli tak nie jest, możemy np. powielić ostatni element tablicy, albo rozważyć ten szczególny przypadek w algorytmie.
{% endhint %}

### Pseudokod

```
funkcja SzukajMinMax(n, A):
    1. kandMin := []
    2. kandMax := []
    3. i := 1
    4. k := 1
    5. Dopóki i + 1 <= n, wykonuj:
        6. Jeżeli A[i] < A[i+1], to:
            7. kandMin[k] := A[i]
            8. kandMax[k] := A[i+1]
        9. w przeciwnym przypadku:
            10. kandMin[k] := A[i+1]
            11. kandMax[k] := A[i]
        12. k := k + 1
        13. i := i + 2
    14. min := kandMin[1]
    15. max := kandMax[1]
    16. Od i := 2 do (n div 2), wykonuj:
        17. Jeżeli min < kandMin[i], to:
            18. min := kandMin[i]
        19. Jeżeli max > kandMax[i], to:
            20. max := kandMax[i]
    21. Zwróc min, max
```

### Złożoność

$$O(3\frac{n}{2})$$ 

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/wyszukiwanie/jednoczesne-wyszukiwanie-minimum-i-maksimum.md" %}
[jednoczesne-wyszukiwanie-minimum-i-maksimum.md](../../programowanie/c++/algorytmy/wyszukiwanie/jednoczesne-wyszukiwanie-minimum-i-maksimum.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/wyszukiwanie/naiwne-wyszukiwanie-minimum-i-maksimum.md" %}
[naiwne-wyszukiwanie-minimum-i-maksimum.md](../../programowanie/python/algorytmy/wyszukiwanie/naiwne-wyszukiwanie-minimum-i-maksimum.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/searching/min-max-search.md" %}
[min-max-search.md](../../programowanie/kotlin/algorithms/searching/min-max-search.md)
{% endcontent-ref %}