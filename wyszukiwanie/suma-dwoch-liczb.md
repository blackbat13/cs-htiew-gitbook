# Suma dwóch liczb

## Opis problemu

Mamy pewien posortowany zbiór różnych liczb. W tym zbiorze mamy odnaleźć dwie liczby, które po dodaniu do siebie dadzą pożądaną sumę. Oczywiście, takie liczby wcale nie muszą w tym zbiorze się znajdować.

Problem może wydawać się dość abstrakcyjny i słabo związany z rzeczywistością. Niemniej jest to świetny problem do zaprezentowania, jak pomocne czasem jest pracowanie z danymi posortowanymi i jak duży wpływ może mieć na złożoność obliczeniową rozwiązania.

Zacznijmy od formalnej specyfikacji problemu.

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna, liczebność zbioru
* $$A[1..n]$$ - $$n-elementowa$$ tablica różnych liczb całkowitych, posortowana rosnąco, indeksowana od jedynki
* $$k$$ - liczba naturalna, szukana suma

#### Wynik

* $$a, b$$ - dwie różne wartości ze zbioru $$A$$ takie, że ich suma wynosi $$k$$( $$a+b=k$$ ), lub $$-1$$, jeżeli takich liczb nie ma w zbiorze (jeżeli takich par jest wiele, to dowolna z nich)

### Przykład

#### Dane

```
n := 10
A[1..10] := [1, 2, 4, 6, 8, 9, 10, 12, 13, 15]
k := 18
```

**Wynik**: $$6,\ 12$$(lub $$8,\ 10$$)

## Rozwiązanie naiwne

TODO

### Pseudokod

```
funkcja SumaDwoch(n, A, k):
    1. Dla i := 1 do n - 1, wykonuj:
        2. Dla j := i + 1 do n, wykonuj:
            3. Jeżeli A[i] + A[j] = k, to:
                4. Wypisz A[i], A[j]
                5. Zakończ
    6. Wypisz -1
```

### Złożoność

$$O(n^2)$$ - kwadratowa

## Rozwiązanie optymalne

TODO

### Pseudokod

```
funkcja SumaDwoch(n, A, k):
    1. lewy := 1
    2. prawy := n
    3. Dopóki lewy < prawy oraz A[lewy] + A[prawy] != k, wykonuj:
        4. Jeżeli A[lewy] + A[prawy] < k, to:
            5. lewy := lewy + 1
        6. w przeciwnym przypadku:
            7. prawy := prawy + 1
    8. Jeżeli lewy < prawy, to:
        9. Wypisz A[lewy], A[prawy]
    10. w przeciwnym przypadku:
        11. Wypisz -1
```

### Złożoność

$$O(n)$$ - liniowa

## Implementacja

### C++

{% content-ref url="../implementacje/c++/algorytmy/wyszukiwanie/suma-dwoch-liczb.md" %}
[suma-dwoch-liczb.md](../implementacje/c++/algorytmy/wyszukiwanie/suma-dwoch-liczb.md)
{% endcontent-ref %}

### Python

{% content-ref url="../implementacje/python/algorytmy/wyszukiwanie/suma-dwoch-liczb.md" %}
[suma-dwoch-liczb.md](../implementacje/python/algorytmy/wyszukiwanie/suma-dwoch-liczb.md)
{% endcontent-ref %}
