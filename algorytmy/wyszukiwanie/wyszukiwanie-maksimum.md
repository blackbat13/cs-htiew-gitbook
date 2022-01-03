# Wyszukiwanie minimum i maksimum

## Opis problemu

Wyobraźmy sobie, że odwiedzamy pewien sklep internetowy, np. w poszukiwaniu nowego laptopa.
Na początek chcemy sprawdzić, jaki jest najdroższy z dostępnych sprzętów.
Co możemy w tym celu zrobić? Możemy oczywiście posortować produkty po cenie.
Nie potrzebna nam jednak lista wszystkich produktów, a tylko jeden - ten najdroższy.

W tym temacie zajmiemy się właśnie takim problemem - **znajdowaniem elementu maksymalnego (albo minimalnego) w zadanym zbiorze**.

## Wyszukiwanie wartości maksymalnej w tablicy

### Opis problemu

Zacznijmy od standardowej wersji problemu.
Jak to zwykle w informatyce, będziemy rozważać pewien uporządkowany zbiór elementów, a dokładnie tablicę liczb całkowitych.
Oczywiście w ogólności nie ma znaczenia, jakie to będą wartości, pod warunkiem, że możemy je ze sobą porównywać i można wśród nich znaleźć wartość największą.

Interesuje nas znalezienie wartości maksymalnej w zadanej tablicy.
Jak zwykle, zaczynamy od bardziej formalnej specyfikacji naszego problemu.

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, liczba elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik:

* Największa wartość z tablicy $$A$$

### Przykład

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

**Wynik**: $$8$$ 

### Animacja

{% embed url="https://blackbat13.github.io/visul2/searching/find_max/#array=%5B6%2C5%2C3%2C1%2C8%2C7%2C2%2C4%5D" %}
Wyszukiwanie maksimum
{% endembed %}

### Rozwiązanie

Zanim przejdziemy do rozwiązywania problemu warto przyjrzeć się dokładnie powyższej animacji.
Pokazuje ona, krok po kroku, metodę, którą zastosujemy.

Idea jest prosta: na początku przyglądamy się **pierwszemu** elementowi z tablicy i stwierdzamy "tak, to może być nasz element maksymalny", więc **zapamiętujemy** jego wartość.
Innymi słowy: wartość pierwszego elementu tablicy zapamiętujemy jako **dotychczasowe** maksimum.

Teraz możemy przejść do sprawdzania kolejnych elementów tablicy, które będziemy przeglądać jeden po drugim, czyli liniowo, podobnie jak w algorytmie wyszukiwania liniowego.
Każdy kolejny element tablicy będziemy porównywać z naszym dotychczasowym maksimum.
Jeżeli znajdziemy element o wartości większej niż nasze dotychczasowe maksimum, to znaczy, że właśnie tę większą wartość należy zapamiętać jako nasze dotychczasowe maksimum.
Poprzednią wartość możemy zapomnieć, jako że interesuje nas tylko jedna wartość: maksymalna.

Na końcu, gdy już sprawdzimy wszystkie elementy tablicy, nasze dotychczasowe maksimum będzie już maksimum z **całej tablicy** i tę właśnie wartość zwrócimy jako wynik naszego algorytmu.

Zapiszmy teraz nasz algorytm w postaci pseudokodu.

### Pseudokod

```
funkcja SzukajMaks(n, A):
    1. maks := A[1]
    2. Od i := 2 do n, wykonuj:
        3. Jeżeli maks < A[i], to:
            4. maks := A[i]

    5. Zwróć maks, zakończ
```

### Złożoność

Podobnie jak w przypadku wyszukiwania liniowego przeglądamy elementy jeden po drugim w poszukiwaniu maksimum.
Dlatego i w tym przypadku mamy złożoność liniową.

$$O(n)$$ - liniowa

## Wyszukiwanie indeksu wartości maksymalnej w tablicy

### Opis problemu

TODO

### Specyfikacja

#### Dane:

* $$n$$ - liczba naturalna, ilość elementów w tablicy
* $$A[1..n]$$ - tablica $$n$$ wartości całkowitych

#### Wynik:

* Indeks największej wartości z tablicy $$A$$ 

### Przykład

#### Dane

```
n := 8
A := [6, 5, 3, 1, 8, 7, 2, 4]
```

**Wynik**: $$5$$ 

{% hint style="info" %}
**Wyjaśnienie**

Największa wartość w tablicy to $$8$$. Wartość ta znajduje się na pozycji piątej.
{% endhint %}

### Rozwiązanie

TODO

### Pseudokod

```
funkcja SzukajIndeksMaks(n, A):
    1. maks := A[1]
    2. ind := 1
    3. Od i := 2 do n, wykonuj:
        4. Jeżeli maks < A[i], to:
            5. maks := A[i]
            6. ind := i
    
    7. Zwróć ind, zakończ    
```

### Złożoność

$$O(n)$$ - liniowa

## Implementacja

### C++

{% content-ref url="../../programowanie/c++/algorytmy/wyszukiwanie/wyszukiwanie-minimum-i-maksimum.md" %}
[wyszukiwanie-minimum-i-maksimum.md](../../programowanie/c++/algorytmy/wyszukiwanie/wyszukiwanie-minimum-i-maksimum.md)
{% endcontent-ref %}

### Python

{% content-ref url="../../programowanie/python/algorytmy/wyszukiwanie/wyszukiwanie-minimum-i-maksimum.md" %}
[wyszukiwanie-minimum-i-maksimum.md](../../programowanie/python/algorytmy/wyszukiwanie/wyszukiwanie-minimum-i-maksimum.md)
{% endcontent-ref %}

### Blockly

{% content-ref url="../../programowanie/blockly/algorytmy/wyszukiwanie/wyszukiwanie-minimum-i-maksimum.md" %}
[wyszukiwanie-minimum-i-maksimum.md](../../programowanie/blockly/algorytmy/wyszukiwanie/wyszukiwanie-minimum-i-maksimum.md)
{% endcontent-ref %}

### Kotlin

{% content-ref url="../../programowanie/kotlin/algorithms/searching/min-or-max.md" %}
[min-or-max.md](../../programowanie/kotlin/algorithms/searching/min-or-max.md)
{% endcontent-ref %}