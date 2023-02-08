---
description: Selection sort
---

# Sortowanie przez wybieranie

## Opis problemu

Wyobraź sobie, że przed tobą leżą książki, ułożone tak, że widzisz tytuł i autora każdej z nich. Twoje zadanie polega na uporządkowaniu tych książek na półce w kolejności alfabetycznej po nazwiskach autorów. Najpierw przeglądasz dostępne książki szukając autora z nazwiskiem pierwszym w kolejności alfabetycznej. Znajdujesz, bierzesz książkę do ręki i umieszczasz na półce. Teraz patrzysz na pozostałe książki i ponownie szukasz pierwszego (w kolejności alfabetycznej) nazwiska z tych, które pozostały. Znajdujesz i odkładasz na półkę, jako drugą książkę. Postępujesz podobnie, powtarzając te czynności tak długo, aż ułożysz wszystkie książki na półce, posortowane po nazwiskach autorów. Brawo, właśnie zastosowałeś algorytm sortowania przez wybieranie!

### Specyfikacja

#### Dane

* $$n$$ — liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ — tablica $$n$$ wartości całkowitych

#### Wynik

* Posortowana niemalejąco tablica $$A$$

### Przykład

Na początek przyjrzyjmy się poniższym animacjom. Spróbuj prześledzić jak kolejne wartości zamieniają się miejscami. Czy potrafisz, własnymi słowami, opisać przebieg algorytmu?

#### Dane

```
n := 10
A := [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
```

#### Animacja 1

![By Joestape89, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=3330231](../../.gitbook/assets/Selection-Sort-Animation.gif)

#### Animacja 2

{% embed url="https://blackbat13.github.io/visul2/sorting/selection_sort/#array=%5B8%2C5%2C2%2C6%2C9%2C3%2C1%2C4%2C0%2C7%5D" %}

## Rozwiązanie

Sortowanie przez wybieranie składa się tak właściwie z dwóch części: znajdowania minimum i samego sortowania. Opis algorytmu znajdowania minimum można znaleźć tutaj: [Wyszukiwanie minimum i maksimum](../searching/min-or-max.md).

Sam algorytm wyszukiwania minimum musimy zmodyfikować tak, by działał na określonym przedziale w tablicy, tzn. chcemy wyszukać minimum nie w całej tablicy, a w jej konkretnym przedziale $$[p..k]$$. Co więcej, potrzebujemy nie tyle znać wartość minimalną, co jej **pozycję** w tablicy. Gdy to już mamy, samo sortowanie jest bardzo proste. Przechodzimy przez kolejne indeksy w naszej tablicy i wyszukujemy pozycję minimum od obecnego indeksu do końca tablicy, a następnie zamieniamy z elementem na obecnie sprawdzanej pozycji.

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

$$O(n^2)$$ — kwadratowa

Wyszukiwanie minimum ma złożoność liniową. Wywołujemy ten algorytm $$n-1$$ razy, więc w efekcie otrzymujemy złożoność kwadratową algorytmu sortowania przez wybieranie.

## Implementacja

### C++

{% content-ref url="../../programming/c++/algorithms/sorting/selection-sort.md" %}
[selection-sort.md](../../programming/c++/algorithms/sorting/selection-sort.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programming/python/algorithms/sorting/selection-sort.md" %}
[selection-sort.md](../../programming/python/algorithms/sorting/selection-sort.md)
{% endcontent-ref %}

### Blockly

{% content-ref url="../../programming/blockly/algorithms/sorting/selection-sort.md" %}
[selection-sort.md](../../programming/blockly/algorithms/sorting/selection-sort.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programming/kotlin/algorithms/sorting/selection-sort.md" %}
[selection-sort.md](../../programming/kotlin/algorithms/sorting/selection-sort.md)
{% endcontent-ref %}