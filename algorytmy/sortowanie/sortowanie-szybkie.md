---
description: Quicksort
---

# Sortowanie szybkie

## Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik:

* Posortowana niemalejąco tablica $$A$$

### Prezentacja

{% file src="../../.gitbook/assets/Sortowanie Szybkie.pdf" %}
Sortowanie szybkie
{% endfile %}

## Rozwiązanie

### Pseudokod

```
Procedura SortSzybkie(A, p, k):
    1. Jeżeli right <= left, to:
        2. Zakończ

    3. pivot := A[(p + k) div 2]
    4. i := p
    5. j := k
    
    6. Dopóki i <= j, wykonuj:
        7. Dopóki A[i] < pivot, wykonuj:
            8. i := i + 1

        9. Dopóki A[j] > pivot, wykonuj:
            10. j := j - 1

        10. Jeżeli i > j, to:
            11. Przerwij pętlę

        11. Zamień(A[i], A[j])

        12. i := i + 1
        13. j := j - 1

    SortSzybkie(A, p, j)
    SortSzybkie(A, i, k)
```

### Złożoność

#### Pesymistyczna

$$O(n^2)$$ — kwadratowa

#### Średnia

$$O(n\log{n})$$ — liniowo logarytmiczna

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sortowanie/sortowanie-szybkie.md" %}
[sortowanie-szybkie.md](../../programowanie/c++/algorytmy/sortowanie/sortowanie-szybkie.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/sortowanie/sortowanie-szybkie.md" %}
[sortowanie-szybkie.md](../../programowanie/python/algorytmy/sortowanie/sortowanie-szybkie.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/sorting/quick-sort.md" %}
[quick-sort.md](../../programowanie/kotlin/algorithms/sorting/quick-sort.md)
{% endcontent-ref %}