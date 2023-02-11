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
procedura Scal(A, pocz, kon, sr):
    1. dl := kon - pocz
    2. scalona := [1..dl]
    3. i1 := pocz
    4. i2 := sr

    5. Dla i := 1 do dl, wykonuj:
        6. Jeżeli i1 >= sr lub (i2 < kon oraz A[i1] > A[i2]), to:
            7. scalona[i] := A[i2]
            8. i2 := i2 + 1
        10. w przeciwnym przypadku, jeżeli i2 >= kon lub A[i1] <= A[i2], to:
            11. scalona[i] := A[i1]
            12. i1 := i1 + 1

    13. Dla i := 1 do dl, wykonuj:
        14. A[pocz + i] := scalona[i]
```

```
procedura SortowaniePrezScalanie(A, pocz, kon):
    1. Jeżeli kon - pocz <= 1, to:
        2. Zakończ

    3. sr := (pocz + kon) div 2
    
    4. SortowaniePrezScalanie(A, pocz, sr)
    5. SortowaniePrezScalanie(A, sr, kon)
    
    6. Scal(A, pocz, kon, sr)
```

### Schemat blokowy

```mermaid
flowchart TD
    START(["Scal(A, pocz, kon, sr)"]) --> K1["dl := kon - pocz\nscalona := [1..dl]\ni1 := pocz\ni2 := sr\ni := 1"]
    K1 --> K5{i <= dl}
    K5 -- PRAWDA --> K6{"i1 >= sr\nlub\n(i2 < kon\noraz\nA[i1] > A[i2])"}
    K6 -- PRAWDA --> K7["scalona[i] := A[i2]\ni2 := i2 + 1"]
    K6 -- FAŁSZ --> K10{"i2 >= kon\nlub\nA[i1] <= A[i2]"}
    K10 -- PRAWDA --> K11["scalona[i] := A[i1]\ni1 := i1 + 1"]
    K10 -- FAŁSZ --> K5i[i := i + 1]
    K7 --> K5i
    K11 --> K5i
    K5i --> K5
    K5 -- FAŁSZ --> K13p[i := 1]
    K13p --> K13{i <= dl}
    K13 -- PRAWDA --> K14["A[pocz + i] := scalona[i]"]
    K14 --> K13i[i := i + 1]
    K13i --> K13
    K13 -- FAŁSZ ---> STOP([STOP])
```

```mermaid
flowchart TD
    START(["SortowaniePrzezScalanie(A, pocz, kon)"]) --> K1{kon - pocz <= 1}
    K1 -- PRAWDA --> STOP([STOP])
    K1 -- FAŁSZ --> K3["sr := (pocz + kon) / 2\nSortowaniePrzezScalanie(A, pocz, sr)\nSortowaniePrzezScalanie(A, sr, kon)\nScal(A, pocz, kon, sr)"]
    K3 --> STOP
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