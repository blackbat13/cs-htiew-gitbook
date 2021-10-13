# Sortowanie bąbelkowe

## Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik:

* Posortowana niemalejąco tablica $$A$$ 

### Przykład

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja 1

![By Swfung8 - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=14953478](../.gitbook/assets/Bubble-sort-example-300px.gif)

#### Animacja 2

{% embed url="https://blackbat13.github.io/visul2/sorting/bubble_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}

## Rozwiązanie

TODO

### Pseudokod

```
procedura SortowanieBabelkowe(n, A):
    1. Dla i = 1 do n, wykonuj:
        2. Dla j = 1 do n - 1, wykonuj:
            3. Jeżeli A[j] > A[j+1], to:
                4. Zamień(A[j], A[j+1])
```

#### Optymalizacja 1

```
procedura SortowanieBabelkowe(n, A):
    1. Dla i = 1 do n, wykonuj:
        2. Dla j = 1 do n - i, wykonuj:
            3. Jeżeli A[j] > A[j+1], to:
                4. Zamień(A[j], A[j+1])
```

### Złożoność

$$O(n^2)$$  - kwadratowa

## Implementacja

### C++

{% content-ref url="../implementacje/c++/algorytmy/sortowanie/sortowanie-babelkowe.md" %}
[sortowanie-babelkowe.md](../implementacje/c++/algorytmy/sortowanie/sortowanie-babelkowe.md)
{% endcontent-ref %}

### Python

{% content-ref url="../implementacje/python/algorytmy/sortowanie/sortowanie-babelkowe.md" %}
[sortowanie-babelkowe.md](../implementacje/python/algorytmy/sortowanie/sortowanie-babelkowe.md)
{% endcontent-ref %}
