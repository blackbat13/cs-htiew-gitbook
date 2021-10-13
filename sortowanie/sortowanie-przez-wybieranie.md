---
description: Selection sort
---

# Sortowanie przez wybieranie

## Opis problemu

TODO

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$ 

### Przykład

#### Dane

```
n := 10
A := [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
```

#### Animacja 1

![By Joestape89, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=3330231](../.gitbook/assets/Selection-Sort-Animation.gif)

#### Animacja 2

{% embed url="https://blackbat13.github.io/visul2/sorting/selection_sort/#array=%5B8%2C5%2C2%2C6%2C9%2C3%2C1%2C4%2C0%2C7%5D" %}

## Rozwiązanie

TODO

### Pseudokod

```
funkcja SzukajMin(p, k, A):
    1. min := A[p]
    2. min_ind := p
    3. Od i := p + 1 do k, wykonuj:
        4. Jeżeli A[i] < min, to:
            5. min := A[i]
            6. min_ind := i
    7. Zwróc min_ind

procedura SortWybier(A, n):
    1. Od i := 1 do n-1, wykonuj:
        2. min_ind := SzukajMin(i, n, A)
        3. Zamień(A[i], A[min_ind])
```

### Złożoność

$$O(n^2)$$ - kwadratowa

## Implementacja

### C++

{% content-ref url="../implementacje/c++/algorytmy/sortowanie/sortowanie-przez-wybieranie.md" %}
[sortowanie-przez-wybieranie.md](../implementacje/c++/algorytmy/sortowanie/sortowanie-przez-wybieranie.md)
{% endcontent-ref %}

### Python

{% content-ref url="../implementacje/python/algorytmy/sortowanie/sortowanie-przez-wybieranie.md" %}
[sortowanie-przez-wybieranie.md](../implementacje/python/algorytmy/sortowanie/sortowanie-przez-wybieranie.md)
{% endcontent-ref %}

### Blockly

{% content-ref url="../implementacje/blockly/algorytmy/sortowanie/sortowanie-przez-wybieranie.md" %}
[sortowanie-przez-wybieranie.md](../implementacje/blockly/algorytmy/sortowanie/sortowanie-przez-wybieranie.md)
{% endcontent-ref %}
