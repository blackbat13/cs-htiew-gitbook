# Listy

Listy w języku Python są podstawową strukturą dynamiczną służącą do przechowywania wielu wartości.

{% hint style="info" %}
Elementy listy indeksujemy (numerujemy) od $$0$$.
{% endhint %}

## Inicjalizacja listy

### Pusta lista

```python
tab = []
```

### Inicjalizacja danymi początkowymi

```python
tab = [1, 2, 3, 4, 5]
```

Gdy tworzymy listę, to nie podajemy jej długości.
Możemy ją jednak wypełnić wartościami. Wówczas lista będzie długość równą liczbie podanych wartości.

### Tablica o długości zadanej przez zmienną

Nie możemy podać, ile elementów ma mieć lista, możemy ją jednak wygenerować używając tzw. _list comprehension_.

```python
n = 10

tab = [0 for _ in range(n)]
```

## Podstawowe operacje

### Odczytanie wartości pod zadanym indeksem

```python
print(tab[2])
```

### Zmiana wartości pod zadanym indeksem

```python
tab[2] = 10
```

### Wypisanie listy

```python
print(tab)
```

### Pobranie długości listy

```python
length = len(tab)

print(length)
```

### Dodanie elementu do listy

```python
tab.append(45)
```

### Usunięcie ostatniego elementu z listy

```python
tab.pop()
```

### Usunięcie i-tego elementu z listy

```python
i = 2

tab.pop(i)
```

### Iteracja po elementach listy

```python
tab = [1, 2, 3, 4, 5]
for el in tab:
    print(el)
```

### Iteracja po indeksach listy

```python
tab = [1, 2, 3, 4, 5]
for i in range(len(tab)):
    print(tab[i])
```