---
description: Quicksort
---

# Sortowanie szybkie

## Opis problemu

Sortowanie szybkie to jeden ze szczególnych algorytmów. W ogólności jest bardzo wydajną metodą sortowania, ale w szczególnych przypadkach jego złożoność jest nie lepsza niż sortowania bąbelkowego.

Sortowanie szybkie opiera się bardzo mocno na rekurencji i podziale tablicy na dwie części. Ogólna idea przedstawia się następująco:
1. Znajdujemy element środkowy, tzw. pivot.
2. Elementy mniejsze przemieszczamy od pivota przemieszczamy na jego lewą stroną, elementy większe natomiast przemieszczamy na prawo.
3. Rekurencyjnie sortujemy lewą część i prawą część tablicy.

### Specyfikacja

#### Dane:

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik:

* Posortowana niemalejąco tablica $$A$$

## Rozwiązanie

By lepiej zrozumieć ten zaawansowany algorytm, prześledźmy jego przebieg na poniższej prezentacji.

{% file src="../../.gitbook/assets/Sortowanie Szybkie.pdf" %}
Sortowanie szybkie
{% endfile %}

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

{% content-ref url="../../programming/c++/algorithms/sorting/quick-sort.md" %}
[quick-sort.md](../../programming/c++/algorithms/sorting/quick-sort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/sorting/quick-sort.md" %}
[quick-sort.md](../../programming/python/algorithms/sorting/quick-sort.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/sorting/quick-sort.md" %}
[quick-sort.md](../../programming/kotlin/algorithms/sorting/quick-sort.md)
{% endcontent-ref %}