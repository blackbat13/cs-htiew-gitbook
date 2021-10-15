# Sortowanie przez zliczanie

## Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$m$$ - największa liczba w tablicy wyznaczająca zakres elementów
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych z przedziału $$[1,m]$$ 

#### Wynik:

* Posortowana niemalejąco tablica $$A$$ 

### Przykład

TODO

## Rozwiązanie

TODO

### Pseudokod

```
procedura SortZlicz(A, n, m):
    1. liczniki := tablica [1..m] wypełniona zerami
    2. Od i := 1 do n, wykonuj:
        3. liczniki[A[i]] := liczniki[A[i]] + 1
    4. pozycja := 1
    5. Od i := 1 do m, wykonuj:
        6. Od j := 1 do liczniki[i], wykonuj:
            7. A[pozycja] := i
            8. pozycja := pozycja + 1  
    9. Zwróc A
```

### Złożoność

$$O(n+m)$$ - liniowa

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/sortowanie/sortowanie-przez-zliczanie.md" %}
[sortowanie-przez-zliczanie.md](../../programowanie/c++/algorytmy/sortowanie/sortowanie-przez-zliczanie.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/kotlin/algorytmy/sortowanie/sortowanie-przez-zliczanie.md" %}
[sortowanie-przez-zliczanie.md](../../programowanie/kotlin/algorytmy/sortowanie/sortowanie-przez-zliczanie.md)
{% endcontent-ref %}

### Blockly

{% content-ref url="../../programowanie/blockly/algorytmy/sortowanie/sortowanie-przez-zliczanie.md" %}
[sortowanie-przez-zliczanie.md](../../programowanie/blockly/algorytmy/sortowanie/sortowanie-przez-zliczanie.md)
{% endcontent-ref %}
