# Listy

Listy w języku Python są podstawową strukturą dynamiczną służącą do przechowywania wielu wartości.

{% hint style="info" %}
Elementy listy indeksujemy (numerujemy) od $$0$$.
{% endhint %}

## Inicjalizacja listy

### Pusta lista

W celu utworzenia pustej listy wystarczy jako wartość zmiennej przypisać puste nawiasy kwadratowe.

```python
tab = []
```

### Inicjalizacja danymi początkowymi

Gdy tworzymy listę, to nie podajemy jej długości.
Możemy ją jednak wypełnić wartościami. Wówczas lista będzie miała długość równą liczbie podanych wartości.

```python
tab = [1, 2, 3, 4, 5]
```

### Lista o długości zadanej przez zmienną

Nie możemy podać, ile elementów ma mieć lista, możemy ją jednak wygenerować używając tzw. _list comprehension_.

```python
n = 10

tab = [0 for _ in range(n)]
```

## Podstawowe operacje

### Odczytanie wartości pod zadanym indeksem

W celu odczytania wartości zapisanej pod zadanym indeksem używamy notacji nawiasów kwadratowych.

```python
print(tab[2])
```

### Ujemne indeksy

Standardowo, by dostać się do zadanego elementu listy, podajemy jego indeks licząc od początku listy.
Możemy też jednak liczyć odległość od końca listy. Wtedy korzystamy z ujemnych indeksów, gdzie $$-1$$ oznacza ostatni element listy, $$-2$$ przedostatni itd.

```python
print(tab[-1])
```

### Zmiana wartości pod zadanym indeksem

Poszczególne elementy listy możemy traktować podobnie do zmiennych, możemy więc na nich przeprowadzać standardowe operacje, w szczególności przypisanie nowej wartości.

```python
tab[2] = 10
```

### Wypisanie listy

W celu wypisania całej listy wystarczy skorzystać z wbudowanej funkcji `print`.

```python
print(tab)
```

### Pobranie długości listy

Długość listy, tzn. liczbę elementów zapisanych w liście, możemy pobrać za pomocą funkcji `len`, jako parametr podając listę, której długość chcemy poznać.

```python
length = len(tab)

print(length)
```

## Modyfikacja zawartości listy

Ponieważ lista jest strukturą dynamiczną, możemy do niej swobodnie dodawać nowe elementy, a także je usuwać.

### Dodanie elementu do listy

W celu dodania nowej wartości na koniec listy używamy metody `append`, jako argument podając wartość nowego elementu.

```python
tab.append(45)
```

### Usunięcie ostatniego elementu z listy

Aby usunąć ostatni element listy możemy skorzystać z metody `pop` nie podając do niej żadnych argumentów.

```python
tab.pop()
```

### Usunięcie i-tego elementu z listy

Do metody `pop` możemy także jako argument podać indeks elementu do usunięcia z listy.

```python
i = 2

tab.pop(i)
```

## Przechodzenie po liście

### Iteracja po elementach listy

W celu przejścia po kolejnych elementach listy możemy skorzystać z pętli `for in`.

```python
tab = [1, 2, 3, 4, 5]
for el in tab:
    print(el)
```

### Iteracja po indeksach listy

Jeżeli chcemy przejść pętlą wyłącznie po indeksach, możemy np. skorzystać z funkcji `range` jako argument podająć długość listy pobraną za pomocą funckji `len`.

```python
tab = [1, 2, 3, 4, 5]
for ind in range(len(tab)):
    print(tab[ind])
```

### Iteracja po elementach i indeksach

Jeżeli chcemy jednocześnie przejść po indeksach elementów i ich wartościach, możemy skorzystać z funkcji `enumerate`, do której jako argument podajemy naszą listę.

```python
tab = [1, 2, 3, 4, 5]
for ind, el in enumerate(tab):
    print(ind, el)
```

## Kopiowanie listy

Podczas przypisywania listy do innej zmiennej trzeba zachować ostrożność, ponieważ domyślnie lista przekazywana jest przez **referencję**.
Spójrzmy na poniższy przykład, aby zrozumieć, co to oznacza.

```python
tab1 = [1, 2, 3, 4]
tab2 = tab1

tab2[0] = 25

print(tab1)
print(tab2)
```

Na początku tworzymy nową listę i zapisujemy ją w zmiennej `tab1`. Następnie wartość tej zmiennej przypisujemy do `tab2`. W kolejnym kroku zmieniamy pierwszy element listy zapisanej w zmiennej `tab2`. Gdy jednak wypiszemy obie listy okaże się, że wartość została także zmieniona w liście zapisanej w zmiennej `tab1`.

Dzieje się tak, ponieważ zmienne `tab1` i `tab2` wskazują na ten sam **obiekt w pamięci**. Gdy chcemy utworzyć faktyczną **kopię** listy, niepowiązaną z jej pierwotnym obiektem, możemy skorzystać z jednej z metod opisanych poniżej.

### Płytka kopia (ang. *shallow copy*)

Jeżeli nasza lista zawiera tylko proste typy, np. liczby, to możemy spokojnie skorzystać z tzw. **płytkiej kopii**.
W tym celu, podczas przypisywania wartości do nowej zmiennej, po nazwie naszej zmiennej zawierającej listę dopisujemy nawiasy kwadratowe z dwukropiek w środku.

```python
tab1 = [1, 2, 3, 4]
tab2 = tab1[:]

tab2[0] = 25

print(tab1)
print(tab2)
```

W tym wypadku tylko wartość zapisana w zmiennej `tab2` uległa zmianie, tak jak moglibyśmy się od początku spodziewać.

### Głęboka kopia (ang. *deep copy*)

Czasem płytka kopia nam nie wystarczy. Będzie tak w sytuacjach gdy w naszej liście przechowujemy złożone elementy, tzn. obiekty, np. inne listy.
Wówczas możemy wykonać tzw. **głęboką kopię**. Wykonamy ją za pomocą funkcji `deepcopy` z modułu `copy`.

Nie należy jednak nadużywać głębokiej kopii ponieważ w wielu przypadkach jest ona bardzo kosztowna i może negatywnie wpływać na wydajność programu.

```python
from copy import deepcopy


tab1 = [1, 2, 3, 4]
tab2 = deepcopy(tab1)

tab2[0] = 25

print(tab1)
print(tab2)
```