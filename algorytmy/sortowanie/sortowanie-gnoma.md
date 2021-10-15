# Sortowanie gnoma

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$ 

### **Przykład**

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja

{% embed url="https://blackbat13.github.io/visul2/sorting/gnome_sort/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}

## Rozwiązanie

TODO

### Pseudokod

```
procedura SortGnoma(n, A):
    1. i := 1
    2. Dopóki i <= n, wykonuj:
        3. Jeżeli i = 1 lub A[i] >= A[i - 1], to:
            4. i := i + 1
        5. W przeciwnym przypadku:
            6. Zamień(A[i], A[i - 1])
            7. i := i - 1
```

### Złożoność

TODO

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sortowanie/sortowanie-gnoma.md" %}
[sortowanie-gnoma.md](../../programowanie/c++/algorytmy/sortowanie/sortowanie-gnoma.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/kotlin/algorytmy/sortowanie/sortowanie-gnoma.md" %}
[sortowanie-gnoma.md](../../programowanie/kotlin/algorytmy/sortowanie/sortowanie-gnoma.md)
{% endcontent-ref %}
