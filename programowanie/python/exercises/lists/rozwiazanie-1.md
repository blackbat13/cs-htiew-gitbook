# Rozwiązanie 1

## Treść zadania

Napisz program zgodny z poniższą specyfikacją.&#x20;

### Specyfikacja

#### Dane

* $$n$$ - liczba naturalna
* $$a_1,a_2,\dots,a_n$$ - $$n$$ liczb całkowitych

#### Wynik

* $$a_n,a_{n-1},\dots,a_2,a_1$$ - podane liczby w odwrotnej kolejności

## Rozwiązanie

```python
n = int(input("Podaj liczbę wartości: "))

tab = []

for i in range(n):
    liczba = int(input(f"Podaj liczbę nr {i + 1}: "))
    tab.append(liczba)

tab.reverse()
print(tab)
```

### Opis rozwiązania

Na początku wczytujemy od użytkownika liczbę elementów i zapisujemy ją w zmiennej $$n$$ (**linia 1**).

Następnie tworzymy pustą listę do przechowywania wartości (**linia 3**).

W kolejnym kroku, w pętli wczytujemy kolejne wartości od użytkownika i dopisujemy je do listy za pomocą polecenia `append` (**linia 7**).

Ostatnim etapem rozwiązania jest odwrócenie kolejności elementów listy za pomocą polecenia `reverse` (**linia 9**). Na końcu wypisujemy odwróconą listę (**linia 10**).
