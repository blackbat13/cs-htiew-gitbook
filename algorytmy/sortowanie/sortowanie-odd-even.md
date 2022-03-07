# Sortowanie odd-even

## Opis problemu

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$

### **Przykład**

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja

{% embed url="https://blackbat13.github.io/visul2/sorting/odd_even_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}
Sortowanie odd-even
{% endembed %}

## Rozwiązanie

### Pseudokod

```
Procedura SortOddEven(A, n):
    1. Od i := 1 do n, wykonuj:
        2. Jeżeli i mod 2 = 1, to:
            3. Dla j := 2 do n, z krokiem 2, wykonuj:
                4. Jeżeli A[j] < A[j - 1]:
                    5. Zamień(A[j], A[j - 1])
        6. w przeciwnym przypadku:
            7. Dla j := 1 do n, z krokiem 2, wykonuj:
                8. Jeżeli A[j] < A[j - 1]:
                    9. Zamień(A[j], A[j - 1])
```

### Złożoność

$$O(n^2)$$ — kwadratowa

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sortowanie/sortowanie-odd-even.md" %}
[sortowanie-odd-even.md](../../programowanie/c++/algorytmy/sortowanie/sortowanie-odd-even.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/sortowanie/sortowanie-odd-even.md" %}
[sortowanie-odd-even.md](../../programowanie/python/algorytmy/sortowanie/sortowanie-odd-even.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/sorting/odd-even-sort.md" %}
[odd-even-sort.md](../../programowanie/kotlin/algorithms/sorting/odd-even-sort.md)
{% endcontent-ref %}