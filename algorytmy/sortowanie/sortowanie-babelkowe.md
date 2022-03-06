# Sortowanie bąbelkowe

## Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik:

* Posortowana niemalejąco tablica $$A$$&#x20;

### Przykład

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja 1

![By Swfung8 - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=14953478](../../.gitbook/assets/Bubble-sort-example-300px.gif)

#### Animacja 2

{% embed url="https://blackbat13.github.io/visul2/sorting/bubble_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}

## Rozwiązanie

TODO

### Pseudokod

```
procedura SortowanieBabelkowe(n, A):
    1. posortowane := Fałsz
    2. i := 0
    3. Dopóki posortowane = Fałsz, wykonuj:
        4. posortowane := Prawda
        5. Dla j = 1 do n - i, wykonuj:
            6. Jeżeli A[j] > A[j+1], to:
                7. Zamień(A[j], A[j+1])
                8. posortowane := Fałsz
        9. i := i + 1
```

### Złożoność

$$O(n^2)$$ - kwadratowa

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sortowanie/sortowanie-babelkowe.md" %}
[sortowanie-babelkowe.md](../../programowanie/c++/algorytmy/sortowanie/sortowanie-babelkowe.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/sortowanie/sortowanie-babelkowe.md" %}
[sortowanie-babelkowe.md](../../programowanie/python/algorytmy/sortowanie/sortowanie-babelkowe.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/sorting/bubble-sort.md" %}
[bubble-sort.md](../../programowanie/kotlin/algorithms/sorting/bubble-sort.md)
{% endcontent-ref %}

### Julia

{% content-ref url="../../programowanie/julia/algorithms/sorting/bubble-sort.md" %}
[bubble-sort.md](../../programowanie/julia/algorithms/sorting/bubble-sort.md)
{% endcontent-ref %}