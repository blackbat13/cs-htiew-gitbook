# Sortowanie odd-even

## Opis problemu

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$

### Przykład

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
procedura OddEvenSort(n, A):
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

### Schemat blokowy

```mermaid
flowchart TD
    START(["OddEvenSort(n, A)"]) --> K0[i := 1]
    K0 --> K1{i <= n}
    K1 -- PRAWDA --> K2{i mod 2 = 1}
    K2 -- PRAWDA --> K3p[j := 2]
    K3p --> K3{j <= n}
    K3 -- PRAWDA --> K4{"A[j] < A[j - 1]"}
    K4 -- PRAWDA --> K5["Zamień(A[j], A[j - 1])"]
    K5 --> K3i[j := j + 2]
    K4 -- FAŁSZ --> K3i
    K3i --> K3
    K3 -- FAŁSZ --> K1i[i := i + 1]
    K2 -- FAŁSZ --> K7p[j := 1]
    K7p --> K7{j <= n}
    K7 -- PRAWDA --> K8{"A[j] < A[j - 1]"}
    K8 -- PRAWDA --> K9["Zamień(A[j], A[j - 1])"]
    K9 --> K7i[j := j + 2]
    K8 -- FAŁSZ --> K7i
    K7i --> K7
    K7 -- FAŁSZ --> K1i
    K1i --> K1
    K1 -- FAŁSZ -------> STOP([STOP])
```

### Złożoność

$$O(n^2)$$ — kwadratowa

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/sorting/odd-even-sort.md" %}
[odd-even-sort.md](../../programming/c++/algorithms/sorting/odd-even-sort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/sorting/odd-even-sort.md" %}
[odd-even-sort.md](../../programming/python/algorithms/sorting/odd-even-sort.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/sorting/odd-even-sort.md" %}
[odd-even-sort.md](../../programming/kotlin/algorithms/sorting/odd-even-sort.md)
{% endcontent-ref %}