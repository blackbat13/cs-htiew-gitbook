# Permutacje

## Opis problemu

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, liczba elementów tablicy, $$n>0$$
* $$A[1..n]$$ - $$n$$-elementowa tablica 

#### Wynik

* Wszystkie permutacje tablicy $$tab$$

### Pseudokod

```
procedura Permutacje(A, pocz, kon):
    1. Jeżeli pocz > kon, to:
        2. Wypisz A
        3. Zakończ
    4. Dla i := pocz do kon, wykonuj:
        5. Zamień(A[start], A[i])
        6. Permutacje(A, pocz + 1, kon)
        7. Zamień(A[pocz], A[i])
```

### Schemat blokowy

```mermaid
flowchart TD
    START(["Permutacje(A, pocz, kon)"]) --> K1{pocz > kon}
    K1 -- PRAWDA --> K2[/Wypisz A/]
    K2 --> STOP([STOP])
    K1 -- FAŁSZ --> K4p[i := pocz]
    K4p --> K4{i <= kon}
    K4 -- PRAWDA --> K5["Zamień(A[start], A[i])\nPermutacje(A, pocz + 1, kon)\nZamień(A[pocz], A[i])"]
    K5 --> K4i[i := i + 1]
    K4i --> K4
    K4 -- FAŁSZ --> STOP
```

## Implementacja

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/backtracking/permutations.md" %}
[permutations.md](../../programming/kotlin/algorithms/backtracking/permutations.md)
{% endcontent-ref %}