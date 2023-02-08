---
description: Mergesort
---

# Sortowanie przez scalanie

## Opis problemu

### Specyfikacja

#### Dane:

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik:

* Posortowana niemalejąco tablica $$A$$&#x20;

### Przykład

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

#### Animacja

![By Swfung8 - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=14961648](../../.gitbook/assets/Merge-sort-example-300px.gif)

### Prezentacja

{% file src="../../.gitbook/assets/Sortowanie przez scalanie.pdf" %}
Sortowanie przez scalanie
{% endfile %}

## Rozwiązanie

### Pseudokod

```
Procedura Scal(A, p, k, sr):
    1. dl := k - p
    2. scalona := pusta tablica
    3. i1 := p
    4. i2 := sr

    5. Dla i := 1 do dl, wykonuj:
        6. Jeżeli i1 >= sr lub (i2 < right oraz A[i1] > A[i2]), to:
            7. Dopisz A[i2] do scalona
            8. i2 := i2 + 1
        10. w przeciwnym przypadku, jeżeli i2 >= k lub A[i1] <= A[i2], to:
            11. Dopisz A[i1] do scalona
            12. i1 := i1 + 1

    13. Dla i := 1 do dl, wykonuj:
        14. A[p + i] := scalona[i]
```

```
Procedura SortScal(A, p, k):
    1. Jeżeli k - p <= 1, to:
        2. Zakończ

    3. sr := (p + k) div 2
    
    4. SortScal(A, p, sr)
    5. SortScal(A, sr, k)
    
    6. Scal(A, p, k, sr)
```

### Złożoność

$$O(n\log{n})$$ — liniowo logarytmiczna

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/sorting/merge-sort.md" %}
[merge-sort.md](../../programming/c++/algorithms/sorting/merge-sort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/sorting/merge-sort.md" %}
[merge-sort.md](../../programming/python/algorithms/sorting/merge-sort.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/sorting/merge-sort.md" %}
[merge-sort.md](../../programming/kotlin/algorithms/sorting/merge-sort.md)
{% endcontent-ref %}