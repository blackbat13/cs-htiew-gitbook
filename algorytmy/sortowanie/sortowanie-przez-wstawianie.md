---
description: Insertion sort
---

# Sortowanie przez wstawianie

## Opis problemu

### Specyfikacja

#### Dane:

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik:

* Posortowana niemalejąco tablica $$A$$

### Przykład

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja 1

![By Swfung8 — Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=14961606](../../.gitbook/assets/Insertion-sort-example-300px.gif)

#### Animacja 2

{% embed url="https://blackbat13.github.io/visul2/sorting/insertion_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}

## Rozwiązanie

### Pseudokod

```
procedura SortWstaw(A, n):
    1. Od i := 2 do n, wykonuj:
        2. j := i
        3. Dopóki j > 1 oraz A[j] < A[j-1], to:
            4. Zamień(A[j], A[j - 1])
```

### Złożoność

$$O(n^2)$$ — kwadratowa

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sortowanie/sortowanie-przez-wstawianie.md" %}
[sortowanie-przez-wstawianie.md](../../programowanie/c++/algorytmy/sortowanie/sortowanie-przez-wstawianie.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/sortowanie/sortowanie-przez-wstawianie.md" %}
[sortowanie-przez-wstawianie.md](../../programowanie/python/algorytmy/sortowanie/sortowanie-przez-wstawianie.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/sorting/insertion-sort.md" %}
[insertion-sort.md](../../programowanie/kotlin/algorithms/sorting/insertion-sort.md)
{% endcontent-ref %}